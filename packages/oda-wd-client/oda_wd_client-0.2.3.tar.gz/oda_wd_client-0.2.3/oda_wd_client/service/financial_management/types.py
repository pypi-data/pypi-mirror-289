from datetime import date, datetime
from enum import Enum
from typing import Literal

from pydantic import BaseModel, Field

from oda_wd_client.base.types import (
    WorkdayCurrencyHighAccuracy,
    WorkdayReferenceBaseModel,
)
from oda_wd_client.service.resource_management._base_types import Organization

# All public imports should be done through oda_wd_client.types.financial_management
__all__: list = []


class ConversionRate(BaseModel):
    """
    Reference: https://community.workday.com/sites/default/files/file-hosting/productionapi/Financial_Management/v40.2/Put_Currency_Conversion_Rate.html#Currency_Conversion_Rate_DataType  # noqa
    """

    class RateTypeID(str, Enum):
        # Text reference to Conversion_Rate_Type in Workday
        current = "Current"
        merit = "Merit"
        budget = "Budget"
        average = "Average"

    workday_id: str | None = None
    # ISO 4217 defines three letters for currency ID
    from_currency_iso: str = Field(max_length=3)
    to_currency_iso: str = Field(max_length=3)

    rate: float
    rate_type_id: RateTypeID = RateTypeID.current
    effective_timestamp: datetime


class ConversionRateType(BaseModel):
    """
    Reference: https://community.workday.com/sites/default/files/file-hosting/productionapi/Financial_Management/v40.2/Put_Currency_Conversion_Rate.html#Currency_Rate_TypeObjectType  # noqa
    """

    workday_id: str
    text_id: str | None = None
    description: str
    is_default: bool = False


class ImportCurrencyConversionRatesRequest(BaseModel):
    """
    Reference: https://community.workday.com/sites/default/files/file-hosting/productionapi/Financial_Management/v42.2/Import_Currency_Conversion_Rates.html#Import_Currency_Conversion_Rates_RequestType  # noqa
    """

    calculate_inverse_rate: bool = True
    calculate_cross_rates: bool = False
    cross_rates_anchor_currency_iso: str | None = Field(max_length=3, default=None)
    rates: list[ConversionRate]


class Currency(WorkdayReferenceBaseModel):
    """
    Reference: https://community.workday.com/sites/default/files/file-hosting/productionapi/Financial_Management/v40.2/GetAll_Currencies.html#Currency_DataType  # noqa
    """

    _class_name = "CurrencyObject"
    workday_id: str = Field(max_length=3, alias="currency_code")
    workday_id_type: Literal["Currency_ID"] = "Currency_ID"
    description: str | None = None
    retired: bool = False


class Company(WorkdayReferenceBaseModel):
    """
    Reference: https://community.workday.com/sites/default/files/file-hosting/productionapi/Financial_Management/v40.2/Get_Workday_Companies.html#Company_WWS_DataType  # noqa
    """

    _class_name = "CompanyObject"
    workday_id: str
    workday_id_type: Literal["Company_Reference_ID"] = "Company_Reference_ID"
    name: str | None = None
    currency: Currency | None = None
    country_code: str | None = Field(max_length=2, default=None)
    parents: list[Organization] = []


class JournalSource(WorkdayReferenceBaseModel):
    """
    Reference: https://community.workday.com/sites/default/files/file-hosting/productionapi/Financial_Management/v40.2/Submit_Accounting_Journal.html#Journal_SourceObjectType  # noqa
    """

    workday_id: str

    class JournalSourceID(str, Enum):
        integration = "Integration"
        spreadsheet_upload = "Spreadsheet_Upload"
        snowflake = "Snowflake"

    _class_name = "Journal_SourceObject"
    workday_id_type: Literal["Journal_Source_ID"] = "Journal_Source_ID"


class LedgerType(WorkdayReferenceBaseModel):
    """
    Holds the type of ledger that we want to submit the journal to - enum values are from Workday.

    Reference: https://community.workday.com/sites/default/files/file-hosting/productionapi/Financial_Management/v40.2/Submit_Accounting_Journal.html#Ledger_TypeObjectType  # noqa
    """

    workday_id: str

    class LedgerTypeID(str, Enum):
        actuals = "Actuals"
        historic_actuals = "Historic_Actuals"

    _class_name = "Ledger_TypeObject"
    workday_id_type: Literal["Ledger_Type_ID"] = "Ledger_Type_ID"


class SpendCategory(WorkdayReferenceBaseModel):
    """
    Worktag? Seems to be dedicated field under Resource_Management at least

    Reference: https://community.workday.com/sites/default/files/file-hosting/productionapi/Resource_Management/v40.2/Submit_Supplier_Invoice.html#Spend_CategoryObjectType  # noqa
    """

    _class_name = "Spend_CategoryObject"
    workday_id: str
    workday_id_type: Literal["Spend_Category_ID"] = "Spend_Category_ID"
    name: str | None = None
    inactive: bool = False
    usage_ids: list[str] = []


class CostCenterWorktag(WorkdayReferenceBaseModel):
    """
    Reference object used as worktag in accounting. Only holds data needed for use as reference, ant not secondary
    data for cost center objects in Workday.

    Reference:  https://community.workday.com/sites/default/files/file-hosting/productionapi/Financial_Management/v40.2/Submit_Accounting_Journal.html#Audited_Accounting_WorktagObjectType  # noqa
    """

    _class_name = "Accounting_WorktagObject"
    workday_id: str
    workday_id_type: Literal["Cost_Center_Reference_ID"] = "Cost_Center_Reference_ID"
    name: str | None = None
    active: bool = True


class ProjectWorktag(WorkdayReferenceBaseModel):
    """
    Reference object used as worktag in accounting. Only holds data needed for use as reference, ant not secondary
    data for cost center objects in Workday.

    Reference:  https://community.workday.com/sites/default/files/file-hosting/productionapi/Financial_Management/v40.2/Submit_Accounting_Journal.html#Audited_Accounting_WorktagObjectType  # noqa
    """

    _class_name = "Accounting_WorktagObject"
    workday_id: str
    workday_id_type: Literal["Project_ID"] = "Project_ID"
    name: str | None = None
    inactive: bool = False


class LedgerAccount(WorkdayReferenceBaseModel):
    """
    Reference to a ledger account in Workday.

    Reference: https://community.workday.com/sites/default/files/file-hosting/productionapi/Financial_Management/v40.2/Submit_Accounting_Journal.html#Ledger_AccountObjectType  # noqa
    """

    _class_name = "Ledger_AccountObject"
    workday_id: str
    workday_id_type: Literal["Ledger_Account_ID"] = "Ledger_Account_ID"
    workday_parent_id: str
    workday_parent_type: Literal["Account_Set_ID"] = "Account_Set_ID"


class JournalEntryLineData(BaseModel):
    """
    Represents a single line in a journal entry,
    with enough information to create a journal entry in Workday.

    Reference: https://community.workday.com/sites/default/files/file-hosting/productionapi/Financial_Management/v40.2/Submit_Accounting_Journal.html#Journal_Entry_Line_DataType  # noqa
    """

    ledger_account: LedgerAccount
    debit: WorkdayCurrencyHighAccuracy | None = None
    credit: WorkdayCurrencyHighAccuracy | None = None
    cost_center: CostCenterWorktag | None = None
    spend_category: SpendCategory | None = None
    memo: str


class AccountingJournalData(BaseModel):
    """
    An accounting journal to be submitted to Workday.
    It's valid for a single company.

    Reference: https://community.workday.com/sites/default/files/file-hosting/productionapi/Financial_Management/v40.2/Submit_Accounting_Journal.html#Accounting_Journal_DataType  # noqa
    """

    accounting_date: date
    company: Company
    ledger_type: LedgerType
    journal_source: JournalSource
    journal_entry_line_data: list[JournalEntryLineData]
    memo: str | None = None
    submit: bool | None = None
    accounting_journal_id: str
