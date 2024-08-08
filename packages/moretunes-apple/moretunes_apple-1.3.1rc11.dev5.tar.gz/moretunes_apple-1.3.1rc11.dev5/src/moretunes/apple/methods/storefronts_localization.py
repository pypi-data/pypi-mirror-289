from ..models import *
from ..token import MTAppleMusic


class StorefrontsLocalization(MTAppleMusic):
    def get_storefront(
            self,
            item_id: str,
            lang: str | None = None,
            include: list[str] | None = None,
            extend: list[str] | None = None,
    ) -> StorefrontsResponse:
        """Fetch a single storefront by using its identifier."""
        method = "GET"
        url = f"/v1/storefronts/{item_id}"
        req_map = {'params': {}}
        if lang is not None:
            req_map["params"]["l"] = lang
        
        if include is not None:
            req_map["params"]["include"] = ','.join(str(x) for x in include)
        
        if extend is not None:
            req_map["params"]["extend"] = ','.join(str(x) for x in extend)
        
        code, resp = self._api_request(endpoint=url, method=method, **req_map)
        result = {
            200: StorefrontsResponse,
            401: UnauthorizedResponse,
            500: ErrorsResponse,
            404: NotFoundResponse
        }[code](**resp)
        if code > 400:
            raise Exception(result)
        
        return result

    def get_storefronts(
            self,
            ids: list[str],
            lang: str | None = None,
            include: list[str] | None = None,
            extend: list[str] | None = None,
    ) -> StorefrontsResponse:
        """Fetch one or more storefronts by using their identifiers."""
        method = "GET"
        url = f"/v1/storefronts"
        req_map = {'params': {}}
        req_map["params"]["ids"] = ','.join(str(x) for x in ids)
        
        if lang is not None:
            req_map["params"]["l"] = lang
        
        if include is not None:
            req_map["params"]["include"] = ','.join(str(x) for x in include)
        
        if extend is not None:
            req_map["params"]["extend"] = ','.join(str(x) for x in extend)
        
        code, resp = self._api_request(endpoint=url, method=method, **req_map)
        result = {
            200: StorefrontsResponse,
            401: UnauthorizedResponse,
            500: ErrorsResponse,
            404: NotFoundResponse
        }[code](**resp)
        if code > 400:
            raise Exception(result)
        
        return result

    def get_storefronts_any(
            self,
            lang: str | None = None,
            limit: int | None = None,
            offset: str | None = None,
            include: list[str] | None = None,
            extend: list[str] | None = None,
    ) -> StorefrontsResponse:
        """Fetch all the storefronts in alphabetical order."""
        method = "GET"
        url = f"/v1/storefronts"
        req_map = {'params': {}}
        if lang is not None:
            req_map["params"]["l"] = lang
        
        if limit is not None:
            req_map["params"]["limit"] = limit
        
        if offset is not None:
            req_map["params"]["offset"] = offset
        
        if include is not None:
            req_map["params"]["include"] = ','.join(str(x) for x in include)
        
        if extend is not None:
            req_map["params"]["extend"] = ','.join(str(x) for x in extend)
        
        code, resp = self._api_request(endpoint=url, method=method, **req_map)
        result = {
            200: StorefrontsResponse,
            401: UnauthorizedResponse,
            500: ErrorsResponse,
            404: NotFoundResponse
        }[code](**resp)
        if code > 400:
            raise Exception(result)
        
        return result

    def get_tag(
            self,
            storefront: str,
            accept_language: list[str],
            lang: str | None = None,
    ) -> LangageTagResponse:
        """
        Fetch the best supported language for a storefront from a list
        """
        method = "GET"
        url = f"/v1/language/{storefront}/tag"
        req_map = {'params': {}}
        req_map["params"]["acceptLanguage"] = ','.join(str(x) for x in accept_language)
        
        if lang is not None:
            req_map["params"]["l"] = lang
        
        code, resp = self._api_request(endpoint=url, method=method, **req_map)
        result = {
            200: LangageTagResponse,
            401: UnauthorizedResponse,
            500: ErrorsResponse,
            404: NotFoundResponse
        }[code](**resp)
        if code > 400:
            raise Exception(result)
        
        return result
