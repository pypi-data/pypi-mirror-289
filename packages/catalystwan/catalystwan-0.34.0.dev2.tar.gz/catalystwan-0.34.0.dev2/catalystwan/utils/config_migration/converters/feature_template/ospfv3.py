# Copyright 2024 Cisco Systems, Inc. and its affiliates
# Copyright 2023 Cisco Systems, Inc. and its affiliates
from copy import deepcopy
from typing import List, Optional, Type, Union, get_args

from catalystwan.api.configuration_groups.parcel import Default, Global, as_global
from catalystwan.models.configuration.feature_profile.common import AddressWithMask
from catalystwan.models.configuration.feature_profile.sdwan.routing import RoutingOspfv3IPv4Parcel
from catalystwan.models.configuration.feature_profile.sdwan.routing.ospfv3 import (
    AdvancedOspfv3Attributes,
    BasicOspfv3Attributes,
    DefaultArea,
    DefaultOriginate,
    MaxMetricRouterLsa,
    MaxMetricRouterLsaAction,
    NormalArea,
    NssaArea,
    Ospfv3InterfaceParametres,
    Ospfv3IPv4Area,
    Ospfv3IPv6Area,
    RedistributedRoute,
    RedistributedRouteIPv6,
    RedistributeProtocol,
    RedistributeProtocolIPv6,
    RoutingOspfv3IPv6Parcel,
    SpfTimers,
    StubArea,
    SummaryRoute,
    SummaryRouteIPv6,
)
from catalystwan.utils.config_migration.converters.exceptions import CatalystwanConverterCantConvertException
from catalystwan.utils.config_migration.steps.constants import LAN_OSPFV3, WAN_OSPFV3

from .base import FTConverter


class BaseOspfv3Converter(FTConverter):
    supported_template_types = (LAN_OSPFV3, WAN_OSPFV3)
    name_suffix: str
    key_address_family: str
    key_distance: str
    parcel_model: Union[Type[RoutingOspfv3IPv4Parcel], Type[RoutingOspfv3IPv6Parcel]]
    area_model: Union[Type[Ospfv3IPv4Area], Type[Ospfv3IPv6Area]]

    delete_keys = (
        "default_information",
        "router_id",
        "table_map",
        "max_metric",
        "timers",
        "distance_ipv4",
        "distance_ipv6",
        "auto_cost",
        "compatible",
    )

    def create_parcel(
        self, name: str, description: str, template_values: dict
    ) -> Union[RoutingOspfv3IPv4Parcel, RoutingOspfv3IPv6Parcel]:
        name = f"{name}{self.name_suffix}"
        values = self.get_values(template_values)
        self.configure_basic_ospf_v3_attributes(values)
        self.configure_advanced_ospf_v3_attributes(values)
        self.configure_max_metric_router_lsa(values)
        self.configure_area(values)
        self.configure_redistribute(values)
        self.cleanup_keys(values)
        return self.parcel_model(parcel_name=name, parcel_description=description, **values)

    def get_values(self, template_values: dict) -> dict:
        values = deepcopy(template_values).get("ospfv3", {}).get("address_family", {}).get(self.key_address_family, {})
        return values

    def configure_basic_ospf_v3_attributes(self, values: dict) -> None:
        distance_configuration = self._get_distance_configuration(values)
        basic_values = self._get_basic_values(distance_configuration)
        values["basic"] = BasicOspfv3Attributes(router_id=values.get("router_id"), **basic_values)

    def _get_distance_configuration(self, values: dict) -> dict:
        return values.get(self.key_distance, {})

    def _get_basic_values(self, values: dict) -> dict:
        return {
            "distance": values.get("distance"),
            "external_distance": values.get("ospf", {}).get("external"),
            "inter_area_distance": values.get("ospf", {}).get("inter_area"),
            "intra_area_distance": values.get("ospf", {}).get("intra_area"),
        }

    def configure_advanced_ospf_v3_attributes(self, values: dict) -> None:
        values["advanced"] = AdvancedOspfv3Attributes(
            default_originate=self._configure_originate(values),
            spf_timers=self._configure_spf_timers(values),
            filter=values.get("table_map", {}).get("filter"),
            policy_name=values.get("table_map", {}).get("policy_name"),
            reference_bandwidth=values.get("auto_cost", {}).get("reference_bandwidth"),
            compatible_rfc1583=values.get("compatible", {}).get("rfc1583"),
        )

    def _configure_originate(self, values: dict) -> Optional[DefaultOriginate]:
        originate = values.get("default_information", {}).get("originate")
        if originate is None:
            return None
        if isinstance(originate, Global):
            return DefaultOriginate(originate=originate)
        metric = originate.get("metric")
        if metric is not None:
            metric = as_global(str(metric.value))
        return DefaultOriginate(
            originate=as_global(True),
            always=originate.get("always"),
            metric=metric,
            metric_type=originate.get("metric_type"),
        )

    def _configure_spf_timers(self, values: dict) -> Optional[SpfTimers]:
        timers = values.get("timers", {}).get("throttle", {}).get("spf")
        if timers is None:
            return None
        return SpfTimers(
            delay=timers.get("delay"),
            initial_hold=timers.get("initial_hold"),
            max_hold=timers.get("max_hold"),
        )

    def configure_max_metric_router_lsa(self, values: dict) -> None:
        max_metric_data = values.get("max_metric", {})
        router_lsa_data = max_metric_data.get("router_lsa", [])

        if not router_lsa_data:
            return

        router_lsa = router_lsa_data[0] if router_lsa_data else None
        if not router_lsa:
            return

        action = router_lsa.get("ad_type")
        if action:
            action = as_global(action.value, MaxMetricRouterLsaAction)

        on_startup_time = router_lsa.get("time")

        values["max_metric_router_lsa"] = MaxMetricRouterLsa(
            action=action,
            on_startup_time=on_startup_time,
        )

    def configure_area(self, values: dict) -> None:
        area = values.get("area")
        if area is None:
            raise CatalystwanConverterCantConvertException("Area is required for OSPFv3")
        area_list = []
        for area_value in area:
            area_list.append(
                self.area_model(
                    area_number=area_value.get("a_num"),
                    area_type_config=self._set_area_type_config(area_value),
                    interfaces=self._set_interfaces(area_value),
                    ranges=self._set_range(area_value),  # type: ignore
                )
            )
        values["area"] = area_list

    def _set_area_type_config(self, area_value: dict) -> Optional[Union[StubArea, NssaArea, NormalArea, DefaultArea]]:
        if "stub" in area_value:
            return StubArea(no_summary=area_value.get("stub", {}).get("no_summary"))
        elif "nssa" in area_value:
            return NssaArea(no_summary=area_value.get("nssa", {}).get("no_summary"))
        elif "normal" in area_value:
            return NormalArea()
        return DefaultArea()

    def _set_interfaces(self, area_value: dict) -> List[Ospfv3InterfaceParametres]:
        interfaces = area_value.get("interface", [])
        if interfaces == []:
            return []
        interface_list = []
        for interface in interfaces:
            if authentication := interface.pop("authentication", None):
                area_value["authentication_type"] = authentication.get("type")
            if network := interface.pop("network", None):
                interface["network_type"] = network
            interface_list.append(Ospfv3InterfaceParametres(**interface))
        return interface_list

    def _set_range(self, area_value: dict) -> Optional[Union[List[SummaryRoute], List[SummaryRouteIPv6]]]:
        raise NotImplementedError

    def configure_redistribute(self, values: dict) -> None:
        raise NotImplementedError

    def cleanup_keys(self, values: dict) -> None:
        for key in self.delete_keys:
            values.pop(key, None)


class Ospfv3Ipv4Converter(BaseOspfv3Converter):
    name_suffix = "_IPV4"
    key_address_family = "ipv4"
    key_distance = "distance_ipv4"
    parcel_model = RoutingOspfv3IPv4Parcel
    area_model = Ospfv3IPv4Area

    def _set_range(self, area_value: dict) -> Optional[List[SummaryRoute]]:
        ranges = area_value.get("range")
        if ranges is None:
            return None
        range_list = []
        for range_ in ranges:
            self._set_summary_prefix(range_)
            range_list.append(SummaryRoute(**range_))
        return range_list

    def _set_summary_prefix(self, range_: dict) -> None:
        if address := range_.pop("address"):
            range_["network"] = AddressWithMask(
                address=as_global(str(address.value.ip)),
                mask=as_global(str(address.value.netmask)),
            )

    def configure_redistribute(self, values: dict) -> None:
        redistributes = values.get("redistribute", [])
        if redistributes == []:
            return None
        redistribute_list = []
        for redistribute in redistributes:
            redistribute_list.append(
                RedistributedRoute(
                    protocol=as_global(redistribute.get("protocol").value, RedistributeProtocol),
                    route_policy=redistribute.get("route_map"),
                    nat_dia=redistribute.get("dia"),
                )
            )
        values["redistribute"] = redistribute_list


class Ospfv3Ipv6Converter(BaseOspfv3Converter):
    name_suffix = "_IPV6"
    key_address_family = "ipv6"
    key_distance = "distance_ipv6"
    parcel_model = RoutingOspfv3IPv6Parcel
    area_model = Ospfv3IPv6Area

    def _set_range(self, area_value: dict) -> Optional[List[SummaryRouteIPv6]]:
        ranges = area_value.get("range")
        if ranges is None:
            return None
        range_list = []
        for range_ in ranges:
            range_list.append(
                SummaryRouteIPv6(
                    network=range_.get("address"),
                    cost=range_.get("cost"),
                    no_advertise=range_.get("no_advertise", Default[bool](value=False)),
                )
            )
        return range_list

    def configure_redistribute(self, values: dict) -> None:
        redistributes = values.get("redistribute", [])
        if redistributes == []:
            return None
        redistribute_list = []
        for redistribute in redistributes:
            if redistribute.get("protocol").value not in get_args(RedistributeProtocolIPv6):
                continue
            redistribute_list.append(
                RedistributedRouteIPv6(
                    protocol=as_global(redistribute.get("protocol").value, RedistributeProtocolIPv6),
                    route_policy=redistribute.get("route_map"),
                )
            )
        values["redistribute"] = redistribute_list
