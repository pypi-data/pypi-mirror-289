"""Daily Treasury Statement."""

url = (
    "https://api.fiscaldata.treasury.gov/services/api/fiscal_service/v1/accounting/dts/"
    + "operating_cash_balance?"
    + "filter=record_date:gte:2019-06-14,record_date:lte:2024-06-13&sort=-record_date&page[size]=4313"
)


categories = [
    "operating_cash_balance",
    "deposits_withdrawals_operating_cash",
    "public_debt_transactions",
    "adjustment_public_debt_transactions_cash_basis",
    "debt_subject_to_limit",
    "inter_agency_tax_transfers",
    "income_tax_refunds_issued",
    "federal_tax_deposits",
    "short_term_cash_investments",
]
