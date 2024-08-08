from ..models import *
from ..token import MTAppleMusic


class Activities(MTAppleMusic):
    def get_activity(
            self,
            item_id: str,
            storefront: str,
            lang: str | None = None,
            include: list[str] | None = None,
            extend: list[str] | None = None,
    ) -> ActivitiesResponse:
        """Fetch an activity by using its identifier."""
        method = "GET"
        url = f"/v1/catalog/{storefront}/activities/{item_id}"
        req_map = {'params': {}}
        if lang is not None:
            req_map["params"]["l"] = lang
        
        if include is not None:
            req_map["params"]["include"] = ','.join(str(x) for x in include)
        
        if extend is not None:
            req_map["params"]["extend"] = ','.join(str(x) for x in extend)
        
        code, resp = self._api_request(endpoint=url, method=method, **req_map)
        result = {
            200: ActivitiesResponse,
            401: UnauthorizedResponse,
            500: ErrorsResponse,
            404: NotFoundResponse
        }[code](**resp)
        if code > 400:
            raise Exception(result)
        
        return result

    def get_activity_relation(
            self,
            item_id: str,
            relationship: str,
            storefront: str,
            limit: int | None = None,
            lang: str | None = None,
            include: list[str] | None = None,
            extend: list[str] | None = None,
    ) -> RelationshipResponse:
        """Fetch an activity’s relationship by using its identifier."""
        method = "GET"
        url = f"/v1/catalog/{storefront}/activities/{item_id}/{relationship}"
        req_map = {'params': {}}
        if limit is not None:
            req_map["params"]["limit"] = limit
        
        if lang is not None:
            req_map["params"]["l"] = lang
        
        if include is not None:
            req_map["params"]["include"] = ','.join(str(x) for x in include)
        
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

    def get_activities(
            self,
            storefront: str,
            ids: list[str],
            include: list[str] | None = None,
            lang: str | None = None,
            extend: list[str] | None = None,
    ) -> ActivitiesResponse:
        """Fetch one or more activities by using their identifiers."""
        method = "GET"
        url = f"/v1/catalog/{storefront}/activities"
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
            200: ActivitiesResponse,
            401: UnauthorizedResponse,
            500: ErrorsResponse,
            404: NotFoundResponse
        }[code](**resp)
        if code > 400:
            raise Exception(result)
        
        return result
