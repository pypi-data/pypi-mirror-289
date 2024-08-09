import base64
from typing import Literal

import requests

API_CLIENT = "35f29871d1a2413c88d8"

API_SECRET = "@egRNk2fx;Aq^@X"

ACCOUNT = 'F]TV3nR"#zAmE-&'


def get_access_token(
    api_client: str, api_secret: str, api_version: Literal[1, 2] = 1
) -> dict:
    """Get the access token for the API and return the request headers with bearer token."""
    POST_URL = "https://ews.fip.finra.org/fip/rest/ews/oauth2/access_token?grant_type=client_credentials"
    auth_string = f"{api_client}:{api_secret}"
    auth_string_bytes = auth_string.encode("ascii")
    base64_bytes = base64.b64encode(auth_string_bytes)
    base64_string = base64_bytes.decode("ascii")
    AUTH_HEADERS = {
        "Authorization": f"Basic {base64_string}",
    }
    response = requests.post(POST_URL, headers=AUTH_HEADERS, timeout=5)
    response.raise_for_status()
    REQUEST_HEADERS = {
        "Authorization": f"Bearer {response.json()['access_token']}",
        "Content-Type": "application/json",
        "Data-API-Version": f"{api_version}",
    }
    return REQUEST_HEADERS


EOD = "/public/reporting/v2/data/group/FixedIncomeMarket/name/EndOfDayPriceYield"

base = "services-dynarep.ddwa.finra.org/public/reporting/v2/data/group/FixedIncomeMarket/name/CollateralizedMortgageObligationsSecurities"

REF_DATA = '{"fields":["cusip","issueSymbolIdentifier","issuerName","isCallable","nextCallDate","productSubTypeCode","couponRate","maturityDate","industryGroup","traceGradeCode","lastSalePrice","lastSaleYield","lastTradeDate","moodysRating","moodyRatingDate","standardAndPoorsRatingDate","standardAndPoorsRating","issuingAgency","couponType","industryGroup","settlementDateMonth","referenceDataIdentifier","poolNumber","subProductType","mortgageProduct","weightedAverageCoupon","weightedAverageLoanAge","weightedAverageMaturity","amortizationType","is144A","benchmarkTermCode","lastTradeTime","lastSaleYield","lastSaleYieldDirectionFlag","securityDescription"],"orFilters":[{"compareFilters":[{"fieldName":"cusip","fieldValue":"AGMT5448212","compareType":"EQUAL"},{"fieldName":"issueSymbolIdentifier","fieldValue":"AGMT5448212","compareType":"EQUAL"}]}],"offset":0,"limit":1}'

CMO_TRADE_ACTIVITY_ROUTE = "/public/reporting/v2/data/group/FixedIncomeMarket/name/CollateralizedMortgageObligationsTradeActivity"
CMO_TRADE_ACTIVITY = '{"fields":["issueSymbolIdentifier","issuerName","reportedTradeVolume","lastSalePrice","couponRate","maturityDate","tradeExecutionTime","tradeExecutionDate","productSubTypeCode"],"dateRangeFilters":[],"domainFilters":[],"compareFilters":[],"multiFieldMatchFilters":[],"orFilters":[],"aggregationFilter":null,"sortFields":["-tradeExecutionDate"],"limit":50,"offset":0,"delimiter":null,"quoteValues":false}'

PAYLOAD = '{"fields":["issueSymbolIdentifier","issuerName","couponType","couponRate","maturityDate","lastSalePrice","lastTradeDate","productSubTypeCode"],"dateRangeFilters":[],"domainFilters":[],"compareFilters":[{"fieldName":"lastTradeDate","fieldValue":"2024-06-04","compareType":"GREATER"}],"multiFieldMatchFilters":[],"orFilters":[],"aggregationFilter":null,"sortFields":["+issueSymbolIdentifier","-lastTradeDate"],"limit":50,"offset":0,"delimiter":null,"quoteValues":false}'
