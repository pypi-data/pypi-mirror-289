import json
from typing import List, Optional, cast

from catalystwan.endpoints.configuration_settings import CloudCredentials
from catalystwan.models.templates import FeatureTemplateInformation
from catalystwan.utils.feature_template.find_template_values import find_template_values


def parse_umbrella_credentials(template_values: dict) -> dict:
    credentials = template_values.get("umbrella", {})
    if "api-key-v2" in credentials and "api-secret-v2" in credentials:
        return dict(
            umbrella_org_id=credentials["org-id"],
            umbrella_sig_auth_key=credentials["api-key-v2"],
            umbrella_sig_auth_secret=credentials["api-secret-v2"],  # pragma: allowlist secret
        )
    elif "api-key" in credentials and "api-secret" in credentials:
        return dict(
            umbrella_org_id=credentials["org-id"],
            umbrella_sig_auth_key=credentials["api-key"],
            umbrella_sig_auth_secret=credentials["api-secret"],  # pragma: allowlist secret
        )
    return {}


def parse_zscaler_credentials(template_values: dict):
    FIELD_MAP = {
        "organization": "zscaler_organization",
        "partner-base-uri": "zscaler_partner_base_uri",
        "partner-key": "zscaler_partner_key",
        "username": "zscaler_username",
        "password": "zscaler_password",  # pragma: allowlist secret
    }
    credentials = template_values.get("zscaler", {})
    if not credentials:
        return {}
    parsed_credentials = {}
    for key, value in credentials.items():
        parsed_credentials[FIELD_MAP[key]] = value

    return parsed_credentials


def create_cloud_credentials_from_templates(templates: List[FeatureTemplateInformation]) -> Optional[CloudCredentials]:
    if len(templates) == 0:
        return None

    merged_credentials = {}
    for template in templates:
        template_definition_as_dict = json.loads(cast(str, template.template_definition))
        template_values = find_template_values(template_definition_as_dict)
        if template.name == "Cisco-Zscaler-Global-Credentials":
            merged_credentials.update(parse_zscaler_credentials(template_values))
        elif template.name == "Cisco-Umbrella-Global-Credentials":
            merged_credentials.update(parse_umbrella_credentials(template_values))

    return CloudCredentials(**merged_credentials)
