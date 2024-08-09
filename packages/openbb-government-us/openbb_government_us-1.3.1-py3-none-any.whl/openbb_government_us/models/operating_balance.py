"""US Government Operating Balance Model."""

url = (
    "https://api.fiscaldata.treasury.gov/services/api/fiscal_service/v1/accounting/dts/"
    + "operating_cash_balance?"
    + "filter=record_date:gte:2019-06-14,record_date:lte:2024-06-13&sort=-record_date&page[size]=4313"
)

base_url = "https://api.fiscaldata.treasury.gov/services/api/fiscal_service/v1/accounting/dts/operating_cash_balance"
