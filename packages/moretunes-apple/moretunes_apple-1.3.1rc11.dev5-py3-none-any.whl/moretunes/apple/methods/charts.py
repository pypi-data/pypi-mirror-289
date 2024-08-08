from ..models import *
from ..token import MTAppleMusic


class Charts(MTAppleMusic):
    def get_charts_any(
            self,
            storefront: str,
            types: list[str],
            lang: str | None = None,
            chart: str | None = None,
            genre: str | None = None,
            limit: int | None = None,
            offset: str | None = None,
            attr_fields: list[str] | None = None,
    ) -> ChartResponse:
        """Fetch one or more charts from the Apple Music Catalog."""
        method = "GET"
        url = f"/v1/catalog/{storefront}/charts"
        req_map = {'params': {}}
        req_map["params"]["types"] = ','.join(str(x) for x in types)
        
        if lang is not None:
            req_map["params"]["l"] = lang
        
        if chart is not None:
            req_map["params"]["chart"] = chart
        
        if genre is not None:
            req_map["params"]["genre"] = genre
        
        if limit is not None:
            req_map["params"]["limit"] = limit
        
        if offset is not None:
            req_map["params"]["offset"] = offset
        
        if attr_fields is not None:
            req_map["params"]["with"] = ','.join(str(x) for x in attr_fields)
        
        code, resp = self._api_request(endpoint=url, method=method, **req_map)
        result = {
            200: ChartResponse,
            401: UnauthorizedResponse,
            500: ErrorsResponse,
            404: NotFoundResponse
        }[code](**resp)
        if code > 400:
            raise Exception(result)
        
        return result
