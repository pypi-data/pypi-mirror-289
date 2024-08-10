from typing import Iterator

from suds import sudsobject

from oda_wd_client.base.api import WorkdayClient
from oda_wd_client.base.tools import suds_to_dict
from oda_wd_client.service.financial_management.types import (
    AccountingJournalData,
    Company,
    ConversionRate,
    ConversionRateType,
    CostCenterWorktag,
    Currency,
    ImportCurrencyConversionRatesRequest,
    ProjectWorktag,
    SpendCategory,
)
from oda_wd_client.service.financial_management.utils import (
    get_business_process_parameters,
    make_conversion_rate_reference_object,
    pydantic_accounting_journal_to_workday,
    pydantic_conversion_rate_to_workday,
    pydantic_conversion_rates_request_to_workday,
    workday_company_to_pydantic,
    workday_conversion_rate_to_pydantic,
    workday_conversion_rate_type_to_pydantic,
    workday_cost_center_to_pydantic,
    workday_currency_to_pydantic,
    workday_project_to_pydantic,
    workday_spend_category_to_pydantic,
    workday_tax_applicability_to_pydantic,
)


class FinancialManagement(WorkdayClient):
    service = "Financial_Management"

    def get_currency_rates(
        self, return_suds_object=False
    ) -> Iterator[sudsobject.Object | ConversionRate]:
        method = "Get_Currency_Conversion_Rates"
        results = self._get_paginated(method, "Currency_Conversion_Rate")
        for rate in results:
            yield rate if return_suds_object else workday_conversion_rate_to_pydantic(
                suds_to_dict(rate)
            )

    def get_currency_rate_types(
        self, return_suds_object=False
    ) -> Iterator[sudsobject.Object | ConversionRateType]:
        method = "Get_Currency_Rate_Types"
        results = self._get_paginated(method, "Currency_Rate_Type")
        for rate_type in results:
            yield rate_type if return_suds_object else workday_conversion_rate_type_to_pydantic(
                suds_to_dict(rate_type)
            )

    def put_currency_rate(self, rate: ConversionRate) -> sudsobject.Object:
        request_kwargs = {
            "Currency_Conversion_Rate_Data": pydantic_conversion_rate_to_workday(
                rate, client=self
            ),
        }

        # If we're updated an existing rate, we need to reference that in the request
        if rate.workday_id:
            request_kwargs[
                "Currency_Conversion_Rate_Reference"
            ] = make_conversion_rate_reference_object(self, rate.workday_id)

        return self._request("Put_Currency_Conversion_Rate", **request_kwargs)

    def import_currency_rates(
        self, rates_request: ImportCurrencyConversionRatesRequest
    ) -> sudsobject.Object:
        request_kwargs = pydantic_conversion_rates_request_to_workday(
            client=self, request=rates_request
        )
        return self._request("Import_Currency_Conversion_Rates", **request_kwargs)

    def get_cost_centers(
        self, return_suds_object=False
    ) -> Iterator[sudsobject.Object | CostCenterWorktag]:
        method = "Get_Cost_Centers"
        results = self._get_paginated(method, "Cost_Center")
        for cost_center in results:
            yield cost_center if return_suds_object else workday_cost_center_to_pydantic(
                suds_to_dict(cost_center)
            )

    def get_companies(
        self, return_suds_object=False
    ) -> Iterator[sudsobject.Object | Company]:
        method = "Get_Workday_Companies"
        results = self._get_paginated(method, "Company")
        for company in results:
            yield company if return_suds_object else workday_company_to_pydantic(
                suds_to_dict(company)
            )

    def get_currencies(
        self, return_suds_object=False
    ) -> Iterator[sudsobject.Object | Currency]:
        method = "GetAll_Currencies"
        response = self._request(method)
        results = response.Currency_Data
        for currency in results:
            yield currency if return_suds_object else workday_currency_to_pydantic(
                suds_to_dict(currency)
            )

    def get_projects(
        self, return_suds_object: bool = False
    ) -> Iterator[sudsobject.Object | ProjectWorktag]:
        method = "Get_Basic_Projects"
        results = self._get_paginated(method, "Basic_Project")
        for project in results:
            yield project if return_suds_object else workday_project_to_pydantic(
                suds_to_dict(project)
            )

    def get_spend_categories(
        self, return_suds_object: bool = False
    ) -> Iterator[sudsobject.Object | SpendCategory]:
        method = "Get_Resource_Categories"
        results = self._get_paginated(method, "Resource_Category")
        for category in results:
            yield category if return_suds_object else workday_spend_category_to_pydantic(
                suds_to_dict(category)
            )

    def get_tax_applicabilities(
        self, return_suds_object: bool = False
    ) -> Iterator[sudsobject.Object | dict]:
        method = "Get_Tax_Applicabilities"
        results = self._get_paginated(method, "Tax_Applicability")
        for tax_applicability in results:
            if return_suds_object:
                yield tax_applicability
            else:
                yield workday_tax_applicability_to_pydantic(
                    suds_to_dict(tax_applicability)
                )

    def submit_accounting_journal(
        self, journal: AccountingJournalData, auto_complete: bool = True
    ) -> sudsobject.Object:
        accounting_journal_data_object = pydantic_accounting_journal_to_workday(
            journal, client=self
        )
        business_process_parameters = get_business_process_parameters(
            auto_complete=auto_complete, client=self
        )

        return self._request(
            "Submit_Accounting_Journal",
            Accounting_Journal_Data=accounting_journal_data_object,
            Business_Process_Parameters=business_process_parameters,
        )
