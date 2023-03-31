"""Models used by Telenet."""
from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field


@dataclass
class TelenetEnvironment:
    """Class to describe a Telenet environment."""

    ocapi: str
    openid: str
    referer: str
    x_alt_referer: str


@dataclass
class TelenetProduct:
    """Telenet product model."""

    product_name: str = ""
    product_key: str = ""
    product_description_key: str = ""
    product_suffix: str = ""
    product_state: str = "Inactive"
    product_identifier: str = ("",)
    product_type: str = ""
    product_description: str = ""
    product_specurl: str = ""
    product_info: list = field(default_factory=list)
    product_plan_identifier: str = ""
    product_subscription_info: list = field(default_factory=list)
    product_extra_attributes: list = field(default_factory=list)
    product_extra_sensor: bool = False
    product_ignore_extra_sensor: bool = False


class TelenetBaseProductExtraAttributes:
    """Telenet Product base extra attributes."""

    activationDate: str = ""
    identifier: str = ""
    label: str = ""
    status: str = ""
    productType: str = ""
    specurl: str = ""


class TelenetInternetProductExtraAttributes(TelenetBaseProductExtraAttributes):
    """Telenet Internet extra attributes."""

    internetType: str = ""


class TelenetMobileProductExtraAttributes(TelenetBaseProductExtraAttributes):
    """Telenet Mobile extra attributes."""

    isDataOnlyPlan: str = ""
    bundleIdentifier: str = ""
    hasVoiceMail: bool = False
    bundleType: str = ""


class TelenetDtvProductExtraAttributes(TelenetBaseProductExtraAttributes):
    """Telenet DTV extra attributes."""

    bundleIdentifier: str = ""
    isInteractive: bool = False
    lineType: str = ""


class TelenetTelephoneProductExtraAttributes(TelenetBaseProductExtraAttributes):
    """Telenet DTV extra attributes."""

    hasVoiceMail: bool = False


class TelenetBundleProductExtraAttributes(TelenetBaseProductExtraAttributes):
    """Telenet DTV extra attributes."""

    products: list = field(default_factory=list)
    bundleFamily: str = ""
    hasActiveMyBill: bool = False
