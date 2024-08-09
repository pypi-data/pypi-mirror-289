import concurrent.futures
from datetime import (
    date as dateType,
    datetime,
)
from typing import Any, Literal, Optional, Union

import pandas as pd
from openbb_ecb.utils.ecb_helpers import get_series_data
from openbb_provider.abstract.data import Data
from pydantic import Field

date = "2023-11-10"


def format_date(date: Optional[Union[datetime, str]]) -> Union[str, None]:
    """Format date."""
    if date:
        if isinstance(date, str):
            return datetime.strptime(date, "%Y-%m-%d").strftime("%y%m%d")
        if isinstance(date, datetime):
            return datetime.strftime(date, "%y%m%d")
    return None


eligible_collateral_url = (
    f"https://www.ecb.europa.eu/paym/coll/assets/html/dla/ea_MID/ea_csv_{date}.csv.gz"
)


BASE_URL = "https://data.ecb.europa.eu/data-detail-api/"

BPS_FREQUENCIES = Literal["monthly", "quarterly"]
BPS_FREQUENCIES_DICT = {"monthly": "M", "quarterly": "Q"}
BPS_ITEMS = Literal[
    "main", "summary", "services", "investment_income", "direct_investment"
]


class ECBMain(Data):
    """ECB Main Balance of Payments Items."""

    period: dateType = Field(
        default=None,
        description="The date representing the beginning of the reporting period.",
    )
    current_account: Optional[float] = Field(
        default=None, description="Current Account Balance (Billions of EUR)"
    )
    goods: Optional[float] = Field(
        default=None, description="Goods Balance (Billions of EUR)"
    )
    services: Optional[float] = Field(
        default=None, description="Services Balance (Billions of EUR)"
    )
    primary_income: Optional[float] = Field(
        default=None, description="Primary Income Balance (Billions of EUR)"
    )
    secondary_income: Optional[float] = Field(
        default=None, description="Secondary Income Balance (Billions of EUR)"
    )
    capital_account: Optional[float] = Field(
        default=None, description="Capital Account Balance (Billions of EUR)"
    )
    net_lending_to_rest_of_world: Optional[float] = Field(
        default=None,
        description="Balance of net lending to the rest of the world (Billions of EUR)",
    )
    financial_account: Optional[float] = Field(
        default=None, description="Financial Account Balance (Billions of EUR)"
    )
    direct_investment: Optional[float] = Field(
        default=None, description="Direct Investment Balance (Billions of EUR)"
    )
    portfolio_investment: Optional[float] = Field(
        default=None, description="Portfolio Investment Balance (Billions of EUR)"
    )
    financial_derivatives: Optional[float] = Field(
        default=None, description="Financial Derivatives Balance (Billions of EUR)"
    )
    other_investment: Optional[float] = Field(
        default=None, description="Other Investment Balance (Billions of EUR)"
    )
    reserve_assets: Optional[float] = Field(
        default=None, description="Reserve Assets Balance (Billions of EUR)"
    )
    errors_and_ommissions: Optional[float] = Field(
        default=None, description="Errors and Omissions (Billions of EUR)"
    )


class ECBSummary(Data):
    """ECB Summary Balance of Payments Items."""

    period: dateType = Field(
        default=None,
        description="The date representing the beginning of the reporting period.",
    )
    current_account_credit: Optional[float] = Field(
        default=None, description="Current Account Credit (Billions of EUR)"
    )
    current_account_debit: Optional[float] = Field(
        default=None, description="Current Account Debit (Billions of EUR)"
    )
    current_account_balance: Optional[float] = Field(
        default=None, description="Current Account Balance (Billions of EUR)"
    )
    goods_credit: Optional[float] = Field(
        default=None, description="Goods Credit (Billions of EUR)"
    )
    goods_debit: Optional[float] = Field(
        default=None, description="Goods Debit (Billions of EUR)"
    )
    services_credit: Optional[float] = Field(
        default=None, description="Services Credit (Billions of EUR)"
    )
    services_debit: Optional[float] = Field(
        default=None, description="Services Debit (Billions of EUR)"
    )
    primary_income_credit: Optional[float] = Field(
        default=None, description="Primary Income Credit (Billions of EUR)"
    )
    primary_income_employee_compensation_credit: Optional[float] = Field(
        default=None,
        description="Primary Income Employee Compensation Credit (Billions of EUR)",
    )
    primary_income_debit: Optional[float] = Field(
        default=None, description="Primary Income Debit (Billions of EUR)"
    )
    primary_income_employee_compensation_debit: Optional[float] = Field(
        default=None,
        description="Primary Income Employee Compensation Debit (Billions of EUR)",
    )
    secondary_income_credit: Optional[float] = Field(
        default=None, description="Secondary Income Credit (Billions of EUR)"
    )
    secondary_income_debit: Optional[float] = Field(
        default=None, description="Secondary Income Debit (Billions of EUR)"
    )
    capital_account_credit: Optional[float] = Field(
        default=None, description="Capital Account Credit (Billions of EUR)"
    )
    capital_account_debit: Optional[float] = Field(
        default=None, description="Capital Account Debit (Billions of EUR)"
    )


class ECBServices(Data):
    """ECB Services Balance of Payments Items."""

    period: dateType = Field(
        default=None,
        description="The date representing the beginning of the reporting period.",
    )
    services_total_credit: Optional[float] = Field(
        default=None, description="Services Total Credit (Billions of EUR)"
    )
    services_total_debit: Optional[float] = Field(
        default=None, description="Services Total Debit (Billions of EUR)"
    )
    transport_credit: Optional[float] = Field(
        default=None, description="Transport Credit (Billions of EUR)"
    )
    transport_debit: Optional[float] = Field(
        default=None, description="Transport Debit (Billions of EUR)"
    )
    travel_credit: Optional[float] = Field(
        default=None, description="Travel Credit (Billions of EUR)"
    )
    travel_debit: Optional[float] = Field(
        default=None, description="Travel Debit (Billions of EUR)"
    )
    financial_services_credit: Optional[float] = Field(
        default=None, description="Financial Services Credit (Billions of EUR)"
    )
    financial_services_debit: Optional[float] = Field(
        default=None, description="Financial Services Debit (Billions of EUR)"
    )
    communications_credit: Optional[float] = Field(
        default=None, description="Communications Credit (Billions of EUR)"
    )
    communications_debit: Optional[float] = Field(
        default=None, description="Communications Debit (Billions of EUR)"
    )
    other_business_services_credit: Optional[float] = Field(
        default=None, description="Other Business Services Credit (Billions of EUR)"
    )
    other_business_services_debit: Optional[float] = Field(
        default=None, description="Other Business Services Debit (Billions of EUR)"
    )
    other_services_credit: Optional[float] = Field(
        default=None, description="Other Services Credit (Billions of EUR)"
    )
    other_services_debit: Optional[float] = Field(
        default=None, description="Other Services Debit (Billions of EUR)"
    )


class ECBInvestmentIncome(Data):
    """ECB Investment Income Balance of Payments Items."""

    period: dateType = Field(
        default=None,
        description="The date representing the beginning of the reporting period.",
    )
    investment_total_credit: Optional[float] = Field(
        default=None, description="Investment Total Credit (Billions of EUR)"
    )
    investment_total_debit: Optional[float] = Field(
        default=None, description="Investment Total Debit (Billions of EUR)"
    )
    equity_credit: Optional[float] = Field(
        default=None, description="Equity Credit (Billions of EUR)"
    )
    equity_reinvested_earnings_credit: Optional[float] = Field(
        default=None, description="Equity Reinvested Earnings Credit (Billions of EUR)"
    )
    equity_debit: Optional[float] = Field(
        default=None, description="Equity Debit (Billions of EUR)"
    )
    equity_reinvested_earnings_debit: Optional[float] = Field(
        default=None, description="Equity Reinvested Earnings Debit (Billions of EUR)"
    )
    debt_instruments_credit: Optional[float] = Field(
        default=None, description="Debt Instruments Credit (Billions of EUR)"
    )
    debt_instruments_debit: Optional[float] = Field(
        default=None, description="Debt Instruments Debit (Billions of EUR)"
    )
    portfolio_investment_equity_credit: Optional[float] = Field(
        default=None, description="Portfolio Investment Equity Credit (Billions of EUR)"
    )
    portfolio_investment_equity_debit: Optional[float] = Field(
        default=None, description="Portfolio Investment Equity Debit (Billions of EUR)"
    )
    portfolio_investment_debt_instruments_credit: Optional[float] = Field(
        default=None,
        description="Portfolio Investment Debt Instruments Credit (Billions of EUR)",
    )
    portofolio_investment_debt_instruments_debit: Optional[float] = Field(
        default=None,
        description="Portfolio Investment Debt Instruments Debit (Billions of EUR)",
    )
    other_investment_credit: Optional[float] = Field(
        default=None, description="Other Investment Credit (Billions of EUR)"
    )
    other_investment_debit: Optional[float] = Field(
        default=None, description="Other Investment Debit (Billions of EUR)"
    )
    reserve_assets_credit: Optional[float] = Field(
        default=None, description="Reserve Assets Credit (Billions of EUR)"
    )


class ECBDirectInvestment(Data):
    """ECB Direct Investment Balance of Payments Items."""

    period: dateType = Field(
        default=None,
        description="The date representing the beginning of the reporting period.",
    )
    assets_total: Optional[float] = Field(
        default=None, description="Assets Total (Billions of EUR)"
    )
    assets_equity: Optional[float] = Field(
        default=None, description="Assets Equity (Billions of EUR)"
    )
    assets_debt_instruments: Optional[float] = Field(
        default=None, description="Assets Debt Instruments (Billions of EUR)"
    )
    assets_mfi: Optional[float] = Field(
        default=None, description="Assets MFIs (Billions of EUR)"
    )
    assets_non_mfi: Optional[float] = Field(
        default=None, description="Assets Non MFIs (Billions of EUR)"
    )
    assets_direct_investment_abroad: Optional[float] = Field(
        default=None, description="Assets Direct Investment Abroad (Billions of EUR)"
    )
    liabilities_total: Optional[float] = Field(
        default=None, description="Liabilities Total (Billions of EUR)"
    )
    liabilities_equity: Optional[float] = Field(
        default=None, description="Liabilities Equity (Billions of EUR)"
    )
    liabilities_debt_instruments: Optional[float] = Field(
        default=None, description="Liabilities Debt Instruments (Billions of EUR)"
    )
    liabilities_mfi: Optional[float] = Field(
        default=None, description="Liabilities MFIs (Billions of EUR)"
    )
    liabilities_non_mfi: Optional[float] = Field(
        default=None, description="Liabilities Non MFIs (Billions of EUR)"
    )
    liabilities_direct_investment_euro_area: Optional[float] = Field(
        default=None,
        description="Liabilities Direct Investment in Euro Area (Billions of EUR)",
    )


class ECBPortfolioInvestment(Data):
    """ECB Portfolio Investment Balance of Payments Items."""

    period: dateType = Field(
        default=None,
        description="The date representing the beginning of the reporting period.",
    )
    assets_total: Optional[float] = Field(
        default=None, description="Assets Total (Billions of EUR)"
    )
    assets_equity_and_fund_shares: Optional[float] = Field(
        default=None,
        description="Assets Equity and Investment Fund Shares (Billions of EUR)",
    )
    assets_equity_shares: Optional[float] = Field(
        default=None, description="Assets Equity Shares (Billions of EUR)"
    )
    assets_investment_fund_shares: Optional[float] = Field(
        default=None, description="Assets Investment Fund Shares (Billions of EUR)"
    )
    assets_debt_short_term: Optional[float] = Field(
        default=None, description="Assets Debt Short Term (Billions of EUR)"
    )
    assets_debt_long_term: Optional[float] = Field(
        default=None, description="Assets Debt Long Term (Billions of EUR)"
    )
    assets_resident_sector_eurosystem: Optional[float] = Field(
        default=None, description="Assets Resident Sector Eurosystem (Billions of EUR)"
    )
    assets_resident_sector_mfi_ex_eurosystem: Optional[float] = Field(
        default=None,
        description="Assets Resident Sector MFIs outside Eurosystem (Billions of EUR)",
    )
    assets_resident_sector_government: Optional[float] = Field(
        default=None, description="Assets Resident Sector Government (Billions of EUR)"
    )
    assets_resident_sector_other: Optional[float] = Field(
        default=None, description="Assets Resident Sector Other (Billions of EUR)"
    )
    liabilities_total: Optional[float] = Field(
        default=None, description="Liabilities Total (Billions of EUR)"
    )
    liabilities_equity_and_fund_shares: Optional[float] = Field(
        default=None,
        description="Liabilities Equity and Investment Fund Shares (Billions of EUR)",
    )
    liabilities_equity: Optional[float] = Field(
        default=None, description="Liabilities Equity (Billions of EUR)"
    )
    liabilities_investment_fund_shares: Optional[float] = Field(
        default=None, description="Liabilities Investment Fund Shares (Billions of EUR)"
    )
    liabilities_debt_short_term: Optional[float] = Field(
        default=None, description="Liabilities Debt Short Term (Billions of EUR)"
    )
    liabilities_debt_long_term: Optional[float] = Field(
        default=None, description="Liabilities Debt Long Term (Billions of EUR)"
    )
    liabilities_resident_sector_government: Optional[float] = Field(
        default=None,
        description="Liabilities Resident Sector Government (Billions of EUR)",
    )
    liabilities_resident_sector_other: Optional[float] = Field(
        default=None, description="Liabilities Resident Sector Other (Billions of EUR)"
    )


class ECBOtherInvestment(Data):
    """ECB Other Investment Balance of Payments Items."""

    period: dateType = Field(
        default=None,
        description="The date representing the beginning of the reporting period.",
    )
    assets_total: Optional[float] = Field(
        default=None, description="Assets Total (Billions of EUR)"
    )
    assets_currency_and_deposits: Optional[float] = Field(
        default=None, description="Assets Currency and Deposits (Billions of EUR)"
    )
    assets_loans: Optional[float] = Field(
        default=None, description="Assets Loans (Billions of EUR)"
    )
    assets_trade_credits_and_advances: Optional[float] = Field(
        default=None, description="Assets Trade Credits and Advances (Billions of EUR)"
    )
    assets_eurosystem: Optional[float] = Field(
        default=None, description="Assets Eurosystem (Billions of EUR)"
    )
    assets_other_mfi_ex_eurosystem: Optional[float] = Field(
        default=None,
        description="Assets Other MFIs outside Eurosystem (Billions of EUR)",
    )
    assets_government: Optional[float] = Field(
        default=None, description="Assets Government (Billions of EUR)"
    )
    assets_other_sectors: Optional[float] = Field(
        default=None, description="Assets Other Sectors (Billions of EUR)"
    )
    liabilities_total: Optional[float] = Field(
        default=None, description="Liabilities Total (Billions of EUR)"
    )
    liabilities_currency_and_deposits: Optional[float] = Field(
        default=None, description="Liabilities Currency and Deposits (Billions of EUR)"
    )
    liabilities_loans: Optional[float] = Field(
        default=None, description="Liabilities Loans (Billions of EUR)"
    )
    liabilities_trade_credits_and_advances: Optional[float] = Field(
        default=None,
        description="Liabilities Trade Credits and Advances (Billions of EUR)",
    )
    liabilities_eurosystem: Optional[float] = Field(
        default=None, description="Liabilities Eurosystem (Billions of EUR)"
    )
    liabilities_other_mfi_ex_eurosystem: Optional[float] = Field(
        default=None,
        description="Liabilities Other MFIs outside Eurosystem (Billions of EUR)",
    )
    liabilities_government: Optional[float] = Field(
        default=None, description="Liabilities Government (Billions of EUR)"
    )
    liabilities_other_sectors: Optional[float] = Field(
        default=None, description="Liabilities Other Sectors (Billions of EUR)"
    )


class ECBBalanceOfPaymentsData(
    ECBMain,
    ECBSummary,
    ECBServices,
    ECBInvestmentIncome,
    ECBDirectInvestment,
    ECBPortfolioInvestment,
    ECBOtherInvestment,
):
    """ECB Balance of Payments Data."""


def generate_bps_series_ids(
    frequency: BPS_FREQUENCIES, items: BPS_ITEMS = "main"
) -> Any:
    """Generate series ids for EU area balance of payments."""

    freq = BPS_FREQUENCIES_DICT[frequency]

    main_items = dict(
        current_account=f"BPS.{freq}.N.I9.W1.S1.S1.T.B.CA._Z._Z._Z.EUR._T._X.N.ALL",
        goods=f"BPS.{freq}.N.I9.W1.S1.S1.T.B.G._Z._Z._Z.EUR._T._X.N.ALL",
        services=f"BPS.{freq}.N.I9.W1.S1.S1.T.B.S._Z._Z._Z.EUR._T._X.N.ALL",
        primary_income=f"BPS.{freq}.N.I9.W1.S1.S1.T.B.IN1._Z._Z._Z.EUR._T._X.N.ALL",
        secondary_income=f"BPS.{freq}.N.I9.W1.S1.S1.T.B.IN2._Z._Z._Z.EUR._T._X.N.ALL",
        capital_account=f"BPS.{freq}.N.I9.W1.S1.S1.T.B.KA._Z._Z._Z.EUR._T._X.N.ALL",
        net_lending_to_rest_of_world=f"BPS.{freq}.N.I9.W1.S1.S1.T.B.CKA._Z._Z._Z.EUR._T._X.N.ALL",
        financial_account=f"BPS.{freq}.N.I9.W1.S1.S1.T.N.FA._T.F._Z.EUR._T._X.N.ALL",
        direct_investment=f"BPS.{freq}.N.I9.W1.S1.S1.T.N.FA.D.F._Z.EUR._T._X.N.ALL",
        portfolio_investment=f"BPS.{freq}.N.I9.W1.S1.S1.T.N.FA.P.F._Z.EUR._T.M.N.ALL",
        financial_derivatives=f"BPS.{freq}.N.I9.W1.S1.S1.T.N.FA.F.F7.T.EUR._T.T.N.ALL",
        other_investment=f"BPS.{freq}.N.I9.W1.S1.S1.T.N.FA.O.F._Z.EUR._T._X.N.ALL",
        reserve_assets=f"BPS.{freq}.N.I9.W1.S121.S1.T.A.FA.R.F._Z.EUR.X1._X.N.ALL",
        errors_and_ommissions=f"BPS.{freq}.N.I9.W1.S1.S1.T.N.EO._Z._Z._Z.EUR._T._X.N.ALL",
    )

    summary_items = dict(
        current_account_credit=f"BPS.{freq}.N.I9.W1.S1.S1.T.C.CA._Z._Z._Z.EUR._T._X.N.ALL",
        current_account_debit=f"BPS.{freq}.N.I9.W1.S1.S1.T.D.CA._Z._Z._Z.EUR._T._X.N.ALL",
        current_account_balance=f"BPS.{freq}.N.I9.W1.S1.S1.T.B.CA._Z._Z._Z.EUR._T._X.N.ALL",
        goods_credit=f"BPS.{freq}.N.I9.W1.S1.S1.T.C.G._Z._Z._Z.EUR._T._X.N.ALL",
        goods_debit=f"BPS.{freq}.N.I9.W1.S1.S1.T.D.CA._Z._Z._Z.EUR._T._X.N.ALL",
        services_credit=f"BPS.{freq}.N.I9.W1.S1.S1.T.C.S._Z._Z._Z.EUR._T._X.N.ALL",
        services_debit=f"BPS.{freq}.N.I9.W1.S1.S1.T.D.S._Z._Z._Z.EUR._T._X.N.ALL",
        primary_income_credit=f"BPS.{freq}.N.I9.W1.S1.S1.T.C.IN1._Z._Z._Z.EUR._T._X.N.ALL",
        primary_income_employee_compensation_credit=f"BPS.{freq}.N.I9.W1.S1.S1.T.C.D1._Z._Z._Z.EUR._T._X.N.ALL",
        primary_income_debit=f"BPS.{freq}.N.I9.W1.S1.S1.T.D.IN1._Z._Z._Z.EUR._T._X.N.ALL",
        primary_income_employee_compensation_debit=f"BPS.{freq}.N.I9.W1.S1.S1.T.D.D1._Z._Z._Z.EUR._T._X.N.ALL",
        secondary_income_credit=f"BPS.{freq}.N.I9.W1.S1.S1.T.C.IN2._Z._Z._Z.EUR._T._X.N.ALL",
        secondary_income_debit=f"BPS.{freq}.N.I9.W1.S1.S1.T.D.IN2._Z._Z._Z.EUR._T._X.N.ALL",
        capital_account_credit=f"BPS.{freq}.N.I9.W1.S1.S1.T.C.KA._Z._Z._Z.EUR._T._X.N.ALL",
        capital_account_debit=f"BPS.{freq}.N.I9.W1.S1.S1.T.D.KA._Z._Z._Z.EUR._T._X.N.ALL",
    )

    services_items = dict(
        services_total_credit=f"BPS.{freq}.N.I9.W1.S1.S1.T.C.S._Z._Z._Z.EUR._T._X.N.ALL",
        services_total_debit=f"BPS.{freq}.N.I9.W1.S1.S1.T.D.S._Z._Z._Z.EUR._T._X.N.ALL",
        transport_credit=f"BPS.{freq}.N.I9.W1.S1.S1.T.C.SC._Z._Z._Z.EUR._T._X.N.ALL",
        transport_debit=f"BPS.{freq}.N.I9.W1.S1.S1.T.D.SC._Z._Z._Z.EUR._T._X.N.ALL",
        travel_credit=f"BPS.{freq}.N.I9.W1.S1.S1.T.C.SD._Z._Z._Z.EUR._T._X.N.ALL",
        travel_debit=f"BPS.{freq}.N.I9.W1.S1.S1.T.D.SD._Z._Z._Z.EUR._T._X.N.ALL",
        financial_services_credit=f"BPS.{freq}.N.I9.W1.S1.S1.T.C.SF._Z._Z._Z.EUR._T._X.N.ALL%20OR%20BPS.{freq}.N.I9.W1.S1.S1.T.C.SG._Z._Z._Z.EUR._T._X.N.ALL",  # noqa E501
        financial_services_debit=f"BPS.{freq}.N.I9.W1.S1.S1.T.D.SF._Z._Z._Z.EUR._T._X.N.ALL%20OR%20BPS.{freq}.N.I9.W1.S1.S1.T.D.SG._Z._Z._Z.EUR._T._X.N.ALL",  # noqa E501
        communications_credit=f"BPS.{freq}.N.I9.W1.S1.S1.T.C.SI._Z._Z._Z.EUR._T._X.N.ALL",
        communications_debit=f"BPS.{freq}.N.I9.W1.S1.S1.T.D.SI._Z._Z._Z.EUR._T._X.N.ALL",
        other_business_services_credit=f"BPS.{freq}.N.I9.W1.S1.S1.T.C.SJ._Z._Z._Z.EUR._T._X.N.ALL",
        other_business_services_debit=f"BPS.{freq}.N.I9.W1.S1.S1.T.D.SJ._Z._Z._Z.EUR._T._X.N.ALL",
        other_services_credit=f"BPS.{freq}.N.I9.W1.S1.S1.T.C.SA._Z._Z._Z.EUR._T._X.N.ALL%20OR%20BPS.{freq}.N.I9.W1.S1.S1.T.C.SB._Z._Z._Z.EUR._T._X.N.ALL%20OR%20BPS.{freq}.N.I9.W1.S1.S1.T.C.SE._Z._Z._Z.EUR._T._X.N.ALL%20OR%20BPS.{freq}.N.I9.W1.S1.S1.T.C.SH._Z._Z._Z.EUR._T._X.N.ALL%20OR%20BPS.{freq}.N.I9.W1.S1.S1.T.C.SK._Z._Z._Z.EUR._T._X.N.ALL%20OR%20BPS.{freq}.N.I9.W1.S1.S1.T.C.SL._Z._Z._Z.EUR._T._X.N.ALL%20OR%20BPS.{freq}.N.I9.W1.S1.S1.T.C.SN._Z._Z._Z.EUR._T._X.N.ALL",  # noqa E501
        other_services_debit=f"BPS.{freq}.N.I9.W1.S1.S1.T.D.SA._Z._Z._Z.EUR._T._X.N.ALL%20OR%20BPS.{freq}.N.I9.W1.S1.S1.T.D.SB._Z._Z._Z.EUR._T._X.N.ALL%20OR%20BPS.{freq}.N.I9.W1.S1.S1.T.D.SE._Z._Z._Z.EUR._T._X.N.ALL%20OR%20BPS.{freq}.N.I9.W1.S1.S1.T.D.SH._Z._Z._Z.EUR._T._X.N.ALL%20OR%20BPS.{freq}.N.I9.W1.S1.S1.T.D.SK._Z._Z._Z.EUR._T._X.N.ALL%20OR%20BPS.{freq}.N.I9.W1.S1.S1.T.D.SL._Z._Z._Z.EUR._T._X.N.ALL%20OR%20BPS.{freq}.N.I9.W1.S1.S1.T.D.SN._Z._Z._Z.EUR._T._X.N.ALL",  # noqa E501
    )

    investment_income_items = dict(
        investment_total_credit=f"BPS.{freq}.N.I9.W1.S1.S1.T.C.D4P._T.F._Z.EUR._T._X.N.ALL",
        investment_total_debit=f"BPS.{freq}.N.I9.W1.S1.S1.T.D.D4P._T.F._Z.EUR._T._X.N.ALL",
        equity_credit=f"BPS.{freq}.N.I9.W1.S1.S1.T.C.D4S.D.F5._Z.EUR._T._X.N.ALL",
        equity_reinvested_earnings_credit=f"BPS.{freq}.N.I9.W1.S1.S1.T.C.D43S.D.F5._Z.EUR._T._X.N.ALL",
        equity_debit=f"BPS.{freq}.N.I9.W1.S1.S1.T.D.D4S.D.F5._Z.EUR._T._X.N.ALL",
        equity_reinvested_earnings_debit=f"BPS.{freq}.N.I9.W1.S1.S1.T.D.D43S.D.F5._Z.EUR._T._X.N.ALL",
        debt_insruments_credit=f"BPS.{freq}.N.I9.W1.S1.S1.T.C.D4Q.D.FL._Z.EUR._T._X.N.ALL",
        debt_insruments_debit=f"BPS.{freq}.N.I9.W1.S1.S1.T.D.D4Q.D.FL._Z.EUR._T._X.N.ALL",
        portfolio_investment_equity_credit=f"BPS.{freq}.N.I9.W1.S1.S1.T.C.D4S.P.F5._Z.EUR._T._X.N.ALL",
        portfolio_investment_equity_debit=f"BPS.{freq}.N.I9.W1.S1.S1.T.D.D4S.P.F5._Z.EUR._T._X.N.ALL",
        portfolio_investment_debt_instruments_credit=f"BPS.{freq}.N.I9.W1.S1.S1.T.C.D41.P.F3.T.EUR._T._X.N.ALL",
        portfolio_investment_debt_instruments_debit=f"BPS.{freq}.N.I9.W1.S1.S1.T.D.D41.P.F3.T.EUR._T._X.N.ALL",
        other_investment_credit=f"BPS.{freq}.N.I9.W1.S1.S1.T.C.D4P.O.F._Z.EUR._T._X.N.ALL",
        other_investment_debit=f"BPS.{freq}.N.I9.W1.S1.S1.T.D.D4P.O.F._Z.EUR._T._X.N.ALL",
        reserve_assets_credit=f"BPS.{freq}.N.I9.W1.S121.S1.T.C.D4P.R.F._Z.EUR.X1._X.N.ALL",
    )

    direct_investment_items = dict(
        assets_total=f"BPS.{freq}.N.I9.W1.S1.S1.LE.A.FA.D.F._Z.EUR._T._X.N.ALL",
        assets_equity=f"BPS.{freq}.N.I9.W1.S1.S1.LE.A.FA.D.F5._Z.EUR._T._X.N.ALL",
        assets_debt_instruments=f"BPS.{freq}.N.I9.W1.S1.S1.LE.A.FA.D.FL._Z.EUR._T._X.N.ALL",
        assets_mfi=f"BPS.{freq}.N.I9.W1.S12K.S1.LE.A.FA.D.F._Z.EUR._T._X.N.ALL",
        assets_non_mfi=f"BPS.{freq}.N.I9.W1.S1Q.S1.LE.A.FA.D.F._Z.EUR._T._X.N.ALL",
        assets_direct_investment_abroad=f"BPS.{freq}.N.I9.W1.S1.S1.LE.NO.FA.D.F._Z.EUR._T._X.N.ALL",
        liabilities_total=f"BPS.{freq}.N.I9.W1.S1.S1.LE.L.FA.D.F._Z.EUR._T._X.N.ALL",
        liabilities_equity=f"BPS.{freq}.N.I9.W1.S1.S1.LE.L.FA.D.F5._Z.EUR._T._X.N.ALL",
        liabilities_debt_instruments=f"BPS.{freq}.N.I9.W1.S1.S1.LE.L.FA.D.FL._Z.EUR._T._X.N.ALL",
        liabilities_mfi=f"BPS.{freq}.N.I9.W1.S12K.S1.LE.L.FA.D.F._Z.EUR._T._X.N.ALL",
        liabilities_non_mfi=f"BPS.{freq}.N.I9.W1.S1Q.S1.LE.L.FA.D.F._Z.EUR._T._X.N.ALL",
        liabilities_direct_investment_euro_area=f"BPS.{freq}.N.I9.W1.S1.S1.LE.NI.FA.D.F._Z.EUR._T._X.N.ALL",
    )

    portfolio_investment_items = dict(
        assets_total=f"BPS.{freq}.N.I9.W1.S1.S1.LE.A.FA.P.F._Z.EUR._T.M.N.ALL",
        assets_equity_and_fund_shares=f"BPS.{freq}.N.I9.W1.S1.S1.LE.A.FA.P.F5._Z.EUR._T.M.N.ALL",
        assets_equity=f"BPS{freq}.N.I9.W1.S1.S1.LE.A.FA.P.F51._Z.EUR._T.M.N.ALL",
        assets_investment_fund_shares=f"BPS{freq}.N.I9.W1.S1.S1.LE.A.FA.P.F52._Z.EUR._T.M.N.ALL",
        assets_debt_short_term=f"BPS{freq}.N.I9.W1.S1.S1.LE.A.FA.P.F3.S.EUR._T.M.N.ALL",
        assets_debt_long_term=f"BPS{freq}.N.I9.W1.S1.S1.LE.A.FA.P.F3.L.EUR._T.M.N.ALL",
        assets_resident_sector_eurosystem=f"BPS{freq}.N.I9.W1.S121.S1.LE.A.FA.P.F._Z.EUR._T.M.N.ALL",
        assets_resident_sector_mfi_ex_eurosystem=f"BPS{freq}.N.I9.W1.S12T.S1.LE.A.FA.P.F._Z.EUR._T.M.N.ALL",
        assets_resident_sector_government=f"BPS{freq}.N.I9.W1.S13.S1.LE.A.FA.P.F._Z.EUR._T.M.N.ALL",
        assets_resident_sector_other=f"BPS{freq}.N.I9.W1.S1P.S1.LE.A.FA.P.F._Z.EUR._T.M.N.ALL",
        assets_issuer_sector_mfi=f"BPS{freq}.N.I9.W1.S1.S12K.LE.A.FA.P.F._Z.EUR._T.M.N.ALL",
        assets_issuer_sector_government=f"BPS{freq}.N.I9.W1.S1.S13.LE.A.FA.P.F._Z.EUR._T.M.N.ALL",
        assets_issuer_sector_other=f"BPS{freq}.N.I9.W1.S1.S1P.LE.A.FA.P.F._Z.EUR._T.M.N.ALL",
        liaibilities_total=f"BPS.{freq}.N.I9.W1.S1.S1.LE.L.FA.P.F._Z.EUR._T.M.N.ALL",
        liabilities_equity_and_fund_shares=f"BPS.{freq}.N.I9.W1.S1.S1.LE.L.FA.P.F5._Z.EUR._T.M.N.ALL",
        liabilities_equity=f"BPS{freq}.N.I9.W1.S1.S1.LE.L.FA.P.F51._Z.EUR._T.M.N.ALL",
        liabilities_investment_fund_shares=f"BPS{freq}.N.I9.W1.S1.S1.LE.L.FA.P.F52._Z.EUR._T.M.N.ALL",
        liabilities_debt_short_term=f"BPS{freq}.N.I9.W1.S1.S1.LE.L.FA.P.F3.S.EUR._T.M.N.ALL",
        liabilities_debt_long_term=f"BPS{freq}.N.I9.W1.S1.S1.LE.L.FA.P.F3.L.EUR._T.M.N.ALL",
        liabilities_resident_sector_government=f"BPS{freq}.N.I9.W1.S13.S1.LE.L.FA.P.F._Z.EUR._T.M.N.ALL",
        liabilities_resident_sector_other=f"BPS{freq}.N.I9.W1.S1P.S1.LE.L.FA.P.F._Z.EUR._T.M.N.ALL",
    )

    other_investment_items = dict(
        assets_total=f"BPS.{freq}.N.I9.W1.S1.S1.LE.A.FA.O.F._Z.EUR._T._X.N.ALL",
        assets_currency_and_deposits=f"BPS.{freq}.N.I9.W1.S1.S1.LE.A.FA.O.F2.T.EUR._T.N.N.ALL",
        assets_loans=f"BPS.{freq}.N.I9.W1.S1.S1.LE.A.FA.O.F4.T.EUR._T.N.N.ALL",
        assets_trade_credits_and_advances=f"BPS.{freq}.N.I9.W1.S1.S1.LE.A.FA.O.F81.T.EUR._T._X.N.ALL",
        assets_eurosystem=f"BPS.{freq}.N.I9.W1.S121.S1.LE.A.FA.O.F._Z.EUR._T._X.N.ALL",
        assets_other_mfi_ex_eurosystem=f"BPS.{freq}.N.I9.W1.S12T.S1.LE.A.FA.O.F._Z.EUR._T._X.N.ALL",
        assets_government=f"BPS.{freq}.N.I9.W1.S13.S1.LE.A.FA.O.F._Z.EUR._T._X.N.ALL",
        assets_other_sectors=f"BPS.{freq}.N.I9.W1.S1P.S1.LE.A.FA.O.F._Z.EUR._T._X.N.ALL",
        liaibilities_total=f"BPS.{freq}.N.I9.W1.S1.S1.LE.L.FA.O.F._Z.EUR._T._X.N.ALL",
        liabilities_currency_and_deposits=f"BPS.{freq}.N.I9.W1.S1.S1.LE.L.FA.O.F2.T.EUR._T.N.N.ALL",
        liaibilities_loans=f"BPS.{freq}.N.I9.W1.S1.S1.LE.L.FA.O.F4.T.EUR._T.N.N.ALL",
        liabilities_trade_credits_and_advances=f"BPS.{freq}.N.I9.W1.S1.S1.LE.L.FA.O.F81.T.EUR._T._X.N.ALL",
        liaibilities_eurosystem=f"BPS.{freq}.N.I9.W1.S121.S1.LE.L.FA.O.F._Z.EUR._T._X.N.ALL",
        liaibilities_other_mfi_ex_eurosystem=f"BPS.{freq}.N.I9.W1.S12T.S1.LE.L.FA.O.F._Z.EUR._T._X.N.ALL",
        liaibilities_government=f"BPS.{freq}.N.I9.W1.S13.S1.LE.L.FA.O.F._Z.EUR._T._X.N.ALL",
        liaibilities_other_sectors=f"BPS.{freq}.N.I9.W1.S1P.S1.LE.L.FA.O.F._Z.EUR._T._X.N.ALL",
    )

    if items == "main":
        return main_items
    if items == "summary":
        return summary_items
    if items == "services":
        freq = "Q"
        return services_items
    if items == "investment_income":
        freq = "Q"
        return investment_income_items
    if items == "direct_investment":
        freq = "Q"
        return direct_investment_items
    if items == "portfolio_investment":
        freq = "Q"
        return portfolio_investment_items
    if items == "other_investment":
        freq = "Q"
        return other_investment_items


# df = {"reserve_assets_credit": {d["PERIOD"]: d["OBS_VALUE_AS_IS"] for d in data}}


def get_balance_of_trade(items: BPS_ITEMS = "main", freq: BPS_FREQUENCIES = "monthly"):
    """Get Balance of Trade Data."""

    series_ids = generate_bps_series_ids(freq, items)
    series = list(series_ids.values())
    names = list(series_ids)
    results = []
    data = {}

    def get_one(serie, name):
        result = {}
        temp = get_series_data(serie)
        result.update({name: {d["PERIOD"]: d["OBS_VALUE_AS_IS"] for d in temp}})
        data.update(result)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(get_one, series, names)
    if data != {}:
        results = (
            pd.DataFrame(data)
            .reset_index()
            .rename(columns={"index": "period"})
            .to_dict("records")
        )

    return results
