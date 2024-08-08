from ..models import *
from ..token import MTAppleMusic


class Curators(MTAppleMusic):
    def get_curator(
            self,
            item_id: str,
            storefront: str,
            lang: str | None = None,
            include: list[str] | None = None,
            extend: list[str] | None = None,
    ) -> CuratorsResponse:
        """Fetch a curator by using the curator’s identifier."""
        method = "GET"
        url = f"/v1/catalog/{storefront}/curators/{item_id}"
        req_map = {'params': {}}
        if lang is not None:
            req_map["params"]["l"] = lang
        
        if include is not None:
            req_map["params"]["include"] = ','.join(str(x) for x in include)
        
        if extend is not None:
            req_map["params"]["extend"] = ','.join(str(x) for x in extend)
        
        code, resp = self._api_request(endpoint=url, method=method, **req_map)
        result = {
            200: CuratorsResponse,
            401: UnauthorizedResponse,
            500: ErrorsResponse,
            404: NotFoundResponse
        }[code](**resp)
        if code > 400:
            raise Exception(result)
        
        return result

    def get_curator_relation(
            self,
            item_id: str,
            relationship: str,
            storefront: str,
            lang: str | None = None,
            include: list[str] | None = None,
            limit: int | None = None,
            extend: list[str] | None = None,
    ) -> RelationshipResponse:
        """Fetch a curator’s relationship by using its identifier."""
        method = "GET"
        url = f"/v1/catalog/{storefront}/curators/{item_id}/{relationship}"
        req_map = {'params': {}}
        if lang is not None:
            req_map["params"]["l"] = lang
        
        if include is not None:
            req_map["params"]["include"] = ','.join(str(x) for x in include)
        
        if limit is not None:
            req_map["params"]["limit"] = limit
        
        if extend is not None:
            req_map["params"]["extend"] = ','.join(str(x) for x in extend)
        
        code, resp = self._api_request(endpoint=url, method=method, **req_map)
        result = {
            200: RelationshipResponse,
            401: UnauthorizedResponse,
            500: ErrorsResponse,
            404: NotFoundResponse
        }[code](**resp)
        if code > 400:
            raise Exception(result)
        
        return result

    def get_curators(
            self,
            storefront: str,
            ids: list[str],
            include: list[str] | None = None,
            lang: str | None = None,
            extend: list[str] | None = None,
    ) -> CuratorsResponse:
        """Fetch one or more curators by using their identifiers."""
        method = "GET"
        url = f"/v1/catalog/{storefront}/curators"
        req_map = {'params': {}}
        req_map["params"]["ids"] = ','.join(str(x) for x in ids)
        
        if include is not None:
            req_map["params"]["include"] = ','.join(str(x) for x in include)
        
        if lang is not None:
            req_map["params"]["l"] = lang
        
        if extend is not None:
            req_map["params"]["extend"] = ','.join(str(x) for x in extend)
        
        code, resp = self._api_request(endpoint=url, method=method, **req_map)
        result = {
            200: CuratorsResponse,
            401: UnauthorizedResponse,
            500: ErrorsResponse,
            404: NotFoundResponse
        }[code](**resp)
        if code > 400:
            raise Exception(result)
        
        return result

    def get_apple_curator(
            self,
            item_id: str,
            storefront: str,
            lang: str | None = None,
            include: list[str] | None = None,
            extend: list[str] | None = None,
    ) -> AppleCuratorsResponse:
        """Fetch an Apple curator by using the curator’s identifier."""
        method = "GET"
        url = f"/v1/catalog/{storefront}/apple-curators/{item_id}"
        req_map = {'params': {}}
        if lang is not None:
            req_map["params"]["l"] = lang
        
        if include is not None:
            req_map["params"]["include"] = ','.join(str(x) for x in include)
        
        if extend is not None:
            req_map["params"]["extend"] = ','.join(str(x) for x in extend)
        
        code, resp = self._api_request(endpoint=url, method=method, **req_map)
        result = {
            200: AppleCuratorsResponse,
            401: UnauthorizedResponse,
            500: ErrorsResponse,
            404: NotFoundResponse
        }[code](**resp)
        if code > 400:
            raise Exception(result)
        
        return result

    def get_apple_curator_relation(
            self,
            item_id: str,
            relationship: str,
            storefront: str,
            lang: str | None = None,
            include: list[str] | None = None,
            limit: int | None = None,
            extend: list[str] | None = None,
    ) -> RelationshipResponse:
        """
        Fetch an Apple curator’s relationship by using its identifier
        """
        method = "GET"
        url = f"/v1/catalog/{storefront}/apple-curators/{item_id}/{relationship}"
        req_map = {'params': {}}
        if lang is not None:
            req_map["params"]["l"] = lang
        
        if include is not None:
            req_map["params"]["include"] = ','.join(str(x) for x in include)
        
        if limit is not None:
            req_map["params"]["limit"] = limit
        
        if extend is not None:
            req_map["params"]["extend"] = ','.join(str(x) for x in extend)
        
        code, resp = self._api_request(endpoint=url, method=method, **req_map)
        result = {
            200: RelationshipResponse,
            401: UnauthorizedResponse,
            500: ErrorsResponse,
            404: NotFoundResponse
        }[code](**resp)
        if code > 400:
            raise Exception(result)
        
        return result

    def get_apple_curators(
            self,
            storefront: str,
            ids: list[str],
            include: list[str] | None = None,
            lang: str | None = None,
            extend: list[str] | None = None,
    ) -> AppleCuratorsResponse:
        """
        Fetch one or more Apple curators by using their identifiers
        """
        method = "GET"
        url = f"/v1/catalog/{storefront}/apple-curators"
        req_map = {'params': {}}
        req_map["params"]["ids"] = ','.join(str(x) for x in ids)
        
        if include is not None:
            req_map["params"]["include"] = ','.join(str(x) for x in include)
        
        if lang is not None:
            req_map["params"]["l"] = lang
        
        if extend is not None:
            req_map["params"]["extend"] = ','.join(str(x) for x in extend)
        
        code, resp = self._api_request(endpoint=url, method=method, **req_map)
        result = {
            200: AppleCuratorsResponse,
            401: UnauthorizedResponse,
            500: ErrorsResponse,
            404: NotFoundResponse
        }[code](**resp)
        if code > 400:
            raise Exception(result)
        
        return result
