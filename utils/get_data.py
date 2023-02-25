from typing import Any, List, Dict, Tuple
import requests
from models.account.endpoint import AccountEndpoint
from models.transactions.endpoint import TransactionsEndpoint
from models.meta.params import Params
from utils.variables import HEADERS


def _transform_url(url: str, params: Params) -> Tuple[str, Params]:
    if AccountEndpoint.isin(url) or TransactionsEndpoint.isin(url):
        url = url.format(params.address)
        params.address = None
    return url, params


def get_response(url: str, params: Params) -> Dict[str, Any]:
    _url, _params = _transform_url(url, params)
    _response = requests.get(
        url=_url,
        params=_params,
        headers=HEADERS,
    )
    return _response