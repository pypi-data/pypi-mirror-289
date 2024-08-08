from ..models import *
from ..token import MTAppleMusic


class Search(MTAppleMusic):
    def get_search_any(
            self,
            storefront: str,
            term: str,
            types: list[str],
            lang: str | None = None,
            limit: int | None = None,
            offset: str | None = None,
            attr_fields: list[str] | None = None,
    ) -> SearchResponse:
        """Search the catalog by using a query."""
        method = "GET"
        url = f"/v1/catalog/{storefront}/search"
        req_map = {'params': {}}
        req_map["params"]["term"] = term
        
        if lang is not None:
            req_map["params"]["l"] = lang
        
        if limit is not None:
            req_map["params"]["limit"] = limit
        
        if offset is not None:
            req_map["params"]["offset"] = offset
        
        req_map["params"]["types"] = ','.join(str(x) for x in types)
        
        if attr_fields is not None:
            req_map["params"]["with"] = ','.join(str(x) for x in attr_fields)
        
        code, resp = self._api_request(endpoint=url, method=method, **req_map)
        result = {
            200: SearchResponse,
            401: UnauthorizedResponse,
            500: ErrorsResponse,
            404: NotFoundResponse
        }[code](**resp)
        if code > 400:
            raise Exception(result)
        
        return result

    def get_search_hints(
            self,
            storefront: str,
            term: str,
            lang: str | None = None,
            limit: int | None = None,
    ) -> SearchHintsResponse:
        """Fetch the search term results for a hint."""
        method = "GET"
        url = f"/v1/catalog/{storefront}/search/hints"
        req_map = {'params': {}}
        req_map["params"]["term"] = term
        
        if lang is not None:
            req_map["params"]["l"] = lang
        
        if limit is not None:
            req_map["params"]["limit"] = limit
        
        code, resp = self._api_request(endpoint=url, method=method, **req_map)
        result = {
            200: SearchHintsResponse,
            401: UnauthorizedResponse,
            500: ErrorsResponse,
            404: NotFoundResponse
        }[code](**resp)
        if code > 400:
            raise Exception(result)
        
        return result

    def get_search_suggestions(
            self,
            storefront: str,
            kinds: list[str],
            term: str,
            lang: str | None = None,
            limit: int | None = None,
            types: list[str] | None = None,
    ) -> SearchSuggestionsResponse:
        """Fetch the search suggestions for a provided term input."""
        method = "GET"
        url = f"/v1/catalog/{storefront}/search/suggestions"
        req_map = {'params': {}}
        req_map["params"]["kinds"] = ','.join(str(x) for x in kinds)
        
        if lang is not None:
            req_map["params"]["l"] = lang
        
        if limit is not None:
            req_map["params"]["limit"] = limit
        
        req_map["params"]["term"] = term
        
        if types is not None:
            req_map["params"]["types"] = ','.join(str(x) for x in types)
        
        code, resp = self._api_request(endpoint=url, method=method, **req_map)
        result = {
            200: SearchSuggestionsResponse,
            401: UnauthorizedResponse,
            500: ErrorsResponse,
            404: NotFoundResponse
        }[code](**resp)
        if code > 400:
            raise Exception(result)
        
        return result

    def get_library_search_any(
            self,
            user_token: str,
            term: str,
            types: list[str],
            limit: int | None = None,
            offset: str | None = None,
            lang: str | None = None,
    ) -> LibrarySearchResponse:
        """Search the library by using a query."""
        method = "GET"
        url = f"/v1/me/library/search"
        req_map = {'params': {}}
        req_map["params"]["term"] = term
        
        req_map["params"]["types"] = ','.join(str(x) for x in types)
        
        if limit is not None:
            req_map["params"]["limit"] = limit
        
        if offset is not None:
            req_map["params"]["offset"] = offset
        
        if lang is not None:
            req_map["params"]["l"] = lang
        
        code, resp = self._api_request(endpoint=url, method=method, **req_map, user_token=user_token)
        result = {
            200: LibrarySearchResponse,
            401: UnauthorizedResponse,
            403: ForbiddenResponse,
            500: ErrorsResponse,
            404: NotFoundResponse
        }[code](**resp)
        if code > 400:
            raise Exception(result)
        
        return result
