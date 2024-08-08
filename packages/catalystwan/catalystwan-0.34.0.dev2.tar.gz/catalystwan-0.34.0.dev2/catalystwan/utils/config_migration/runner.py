# Copyright 2024 Cisco Systems, Inc. and its affiliates
import logging
import re
from dataclasses import dataclass
from json import dumps
from pathlib import Path
from typing import Callable, cast
from uuid import UUID

from catalystwan.models.configuration.config_migration import ConfigTransformResult, UX1Config, UX2ConfigPushResult
from catalystwan.models.configuration.feature_profile.parcel import Parcel, list_types
from catalystwan.models.configuration.feature_profile.sdwan.policy_object import AnyPolicyObjectParcel
from catalystwan.session import ManagerSession
from catalystwan.typed_list import DataSequence
from catalystwan.utils.config_migration.creators.groups_of_interests_pusher import get_parcel_ordering_value
from catalystwan.workflows.config_migration import (
    collect_ux1_config,
    log_progress,
    push_ux2_config,
    rollback_ux2_config,
    transform,
)

DEFAULT_ARTIFACT_DIR = "artifacts"

logger = logging.getLogger(__name__)


@dataclass
class ConfigMigrationRunner:
    session: ManagerSession
    collect: bool = True
    push: bool = True
    rollback: bool = False
    add_suffix: bool = True
    dt_filter: str = ".*"
    ft_filter: str = ".*"
    lp_filter: str = ".*"
    cp_filter: str = ".*"
    sp_filter: str = ".*"
    artifact_dir = Path(DEFAULT_ARTIFACT_DIR)
    progress: Callable[[str, int, int], None] = log_progress

    def __post_init__(self) -> None:
        self.artifact_dir.mkdir(parents=True, exist_ok=True)
        self.ux1_dump: Path = self.artifact_dir / Path("ux1.json")
        self.ux2_dump: Path = self.artifact_dir / Path("ux2.json")
        self.ux2_push_dump: Path = self.artifact_dir / Path("ux2-push-result.json")
        self.ux1_schema_dump: Path = self.artifact_dir / Path("ux1-schema.json")
        self.transform_schema_dump: Path = self.artifact_dir / Path("transform-result-schema.json")
        self.push_schema_dump: Path = self.artifact_dir / Path("push-result-schema.json")

    def set_dump_prefix(self, prefix: str) -> None:
        self.ux1_dump = self.artifact_dir / Path(f"{prefix}-ux1.json")
        self.ux2_dump = self.artifact_dir / Path(f"{prefix}-ux2.json")
        self.ux2_push_dump = self.artifact_dir / Path(f"{prefix}-ux2-push-result.json")
        self.ux1_schema_dump = self.artifact_dir / Path(f"{prefix}-ux1-schema.json")
        self.transform_schema_dump = self.artifact_dir / Path(f"{prefix}-transform-result-schema.json")
        self.push_schema_dump = self.artifact_dir / Path(f"{prefix}-push-result-schema.json")

    def set_filters(
        self,
        dt_filter: str = ".*",
        ft_filter: str = ".*",
        lp_filter: str = ".*",
        cp_filter: str = ".*",
        sp_filter: str = ".*",
    ) -> None:
        """Set the filters for the device templates, feature templates,
        localized policies, centralized policies, and security policies

        Args:
            dt_filter (str, optional): Device Template filter. Defaults to ".*".
            ft_filter (str, optional): Feature Template filter. Defaults to ".*".
            lp_filter (str, optional): Localized Policy filter. Defaults to ".*".
            cp_filter (str, optional): Centralized Policy filter. Defaults to ".*".
            sp_filter (str, optional): Security Policy filter. Defaults to ".*".
        """
        self.dt_filter = dt_filter
        self.ft_filter = ft_filter
        self.lp_filter = lp_filter
        self.cp_filter = cp_filter
        self.sp_filter = sp_filter

    @staticmethod
    def collect_only(session: ManagerSession, filter: str = ".*") -> "ConfigMigrationRunner":
        return ConfigMigrationRunner(session=session, collect=True, push=False, rollback=False, dt_filter=filter)

    @staticmethod
    def collect_and_push(session: ManagerSession, filter: str = ".*") -> "ConfigMigrationRunner":
        return ConfigMigrationRunner(session=session, collect=True, push=True, rollback=False, dt_filter=filter)

    @staticmethod
    def rollback_only(session: ManagerSession, filter: str = ".*") -> "ConfigMigrationRunner":
        return ConfigMigrationRunner(session=session, collect=False, push=False, rollback=True, dt_filter=filter)

    @staticmethod
    def transform_only(session: ManagerSession, filter: str = ".*") -> "ConfigMigrationRunner":
        return ConfigMigrationRunner(session=session, collect=False, push=False, rollback=False, dt_filter=filter)

    @staticmethod
    def push_only(session: ManagerSession, filter: str = ".*") -> "ConfigMigrationRunner":
        return ConfigMigrationRunner(session=session, collect=False, push=True, rollback=False, dt_filter=filter)

    @staticmethod
    def push_and_rollback(session: ManagerSession, filter: str = ".*") -> "ConfigMigrationRunner":
        return ConfigMigrationRunner(session=session, collect=False, push=True, rollback=True, dt_filter=filter)

    @staticmethod
    def collect_push_and_rollback(session: ManagerSession, filter: str = ".*") -> "ConfigMigrationRunner":
        return ConfigMigrationRunner(session=session, collect=True, push=True, rollback=True, dt_filter=filter)

    def load_collected_config(self) -> UX1Config:
        return UX1Config.model_validate_json(open(self.ux1_dump).read())

    def load_transform_result(self) -> ConfigTransformResult:
        return ConfigTransformResult.model_validate_json(open(self.ux2_dump).read())

    def load_push_result(self) -> UX2ConfigPushResult:
        return UX2ConfigPushResult.model_validate_json(open(self.ux2_push_dump).read())

    def dump_schemas(self):
        with open(self.ux1_schema_dump, "w") as f:
            f.write(dumps(UX1Config.model_json_schema(by_alias=True), indent=4))
        with open(self.transform_schema_dump, "w") as f:
            f.write(dumps(ConfigTransformResult.model_json_schema(by_alias=True), indent=4))
        with open(self.push_schema_dump, "w") as f:
            f.write(dumps(UX2ConfigPushResult.model_json_schema(by_alias=True), indent=4))

    def clear_ux2(self) -> None:
        with self.session.login() as session:
            # GROUPS
            self.progress("deleting config groups...", 1, 12)
            session.api.config_group.delete_all()

            self.progress("deleting topology groups...", 2, 12)
            tg_api = session.endpoints.configuration.topology_group
            for tg in tg_api.get_all():
                tg_api.delete(tg.id)

            self.progress("deleting policy groups...", 2, 12)
            pg_api = session.endpoints.configuration.policy_group
            for pg in pg_api.get_all():
                pg_api.delete(pg.id)

            # PROFILES
            fp_api = session.api.sdwan_feature_profiles

            self.progress("deleting application priority profiles...", 3, 12)
            fp_api.application_priority.delete_all_profiles()

            self.progress("deleting cli profiles...", 4, 12)
            fp_api.cli.delete_all_profiles()

            self.progress("deleting dns security profiles...", 5, 12)
            fp_api.dns_security.delete_all_profiles()

            self.progress("deleting embedded security profiles...", 5, 12)
            fp_api.embedded_security.delete_all_profiles()

            self.progress("deleting other profiles...", 6, 12)
            fp_api.other.delete_all_profiles()

            self.progress("deleting service profiles...", 7, 12)
            fp_api.service.delete_all_profiles()

            self.progress("deleting sig security profiles...", 8, 12)
            fp_api.sig_security.delete_all_profiles()

            self.progress("deleting system profiles...", 9, 12)
            fp_api.system.delete_all_profiles()

            self.progress("deleting transport profiles...", 10, 12)
            fp_api.transport.delete_all_profiles()

            self.progress("deleting topology profiles...", 11, 12)
            fp_api.topology.delete_all_profiles()

            self.progress("deleting default policy object profile parcels...", 12, 12)
            po_profiles = fp_api.policy_object.get_profiles()
            if len(po_profiles) > 1:
                logger.warning("WARNING! MORE THAN ONE DEFAULT POLICY OBJECT PROFILE DETECTED")

            for po_profile in po_profiles:
                sorted_parcel_types = sorted(
                    list_types(AnyPolicyObjectParcel), key=lambda x: get_parcel_ordering_value(x), reverse=True
                )

                for dpo_parcel_type in sorted_parcel_types:
                    for parcel in cast(
                        DataSequence[Parcel[AnyPolicyObjectParcel]],
                        fp_api.policy_object.get(po_profile.profile_id, dpo_parcel_type),
                    ):
                        if parcel.created_by != "system":
                            parcel_uuid = UUID(str(parcel.parcel_id))
                            fp_api.policy_object.delete(po_profile.profile_id, type(parcel.payload), parcel_uuid)

    def filter_ux1(self, ux1: UX1Config) -> None:
        """Filter out the templates and policies based on the filters"""
        _filtered_dts = [
            dt for dt in ux1.templates.device_templates if re.search(self.dt_filter, dt.template_name) is not None
        ]
        ux1.templates.device_templates = _filtered_dts
        _filtered_fts = [ft for ft in ux1.templates.feature_templates if re.search(self.ft_filter, ft.name) is not None]
        ux1.templates.feature_templates = _filtered_fts
        _filtered_localized = [
            p for p in ux1.policies.localized_policies if re.search(self.lp_filter, p.policy_name) is not None
        ]
        ux1.policies.localized_policies = _filtered_localized
        _filtered_centralized = [
            p for p in ux1.policies.centralized_policies if re.search(self.cp_filter, p.policy_name) is not None
        ]
        ux1.policies.centralized_policies = _filtered_centralized
        _filtered_security = [
            p for p in ux1.policies.security_policies if re.search(self.sp_filter, p.policy_name) is not None
        ]
        ux1.policies.security_policies = _filtered_security

    def run(self):
        with self.session.login() as session:
            # collext and dump ux1 to json file
            if self.collect:
                ux1 = collect_ux1_config(session, self.progress)
                # ux1.templates = UX1Templates()
                with open(self.ux1_dump, "w") as f:
                    f.write(ux1.model_dump_json(exclude_none=True, by_alias=True, indent=4, warnings=False))

            # transform to ux2 and dump to json file
            _ux1 = self.load_collected_config()
            self.filter_ux1(_ux1)
            _transform_result = transform(_ux1, self.add_suffix)
            with open(self.ux2_dump, "w") as f:
                f.write(_transform_result.model_dump_json(exclude_none=True, by_alias=True, indent=4, warnings=False))

            # push ux2 to remote and dump push result
            if self.push:
                transform_result = self.load_transform_result()
                ux2_push_result = push_ux2_config(session, transform_result.ux2_config, self.progress)
                with open(self.ux2_push_dump, "w") as f:
                    f.write(ux2_push_result.model_dump_json(exclude_none=True, by_alias=True, indent=4, warnings=False))

            # rollback
            if self.rollback:
                ux2_push_result = self.load_push_result()
                rollback_ux2_config(session, ux2_push_result.rollback, self.progress)
