from ..models import *
from ..token import MTAppleMusic


class Recommendations(MTAppleMusic):
    def get_recommendation(
            self,
            user_token: str,
            item_id: str,
            lang: str | None = None,
            include: list[str] | None = None,
            extend: list[str] | None = None,
    ) -> PersonalRecommendationResponse:
        """Fetch a recommendation by using its identifier."""
        method = "GET"
        url = f"/v1/me/recommendations/{item_id}"
        req_map = {'params': {}}
        if lang is not None:
            req_map["params"]["l"] = lang
        
        if include is not None:
            req_map["params"]["include"] = ','.join(str(x) for x in include)
        
        if extend is not None:
            req_map["params"]["extend"] = ','.join(str(x) for x in extend)
        
        code, resp = self._api_request(endpoint=url, method=method, **req_map, user_token=user_token)
        result = {
            200: PersonalRecommendationResponse,
            401: UnauthorizedResponse,
            403: ForbiddenResponse,
            500: ErrorsResponse,
            404: NotFoundResponse
        }[code](**resp)
        if code > 400:
            raise Exception(result)
        
        return result

    def get_recommendation_relation(
            self,
            user_token: str,
            item_id: str,
            relationship: str,
            include: list[str] | None = None,
            lang: str | None = None,
            limit: int | None = None,
            extend: list[str] | None = None,
    ) -> RelationshipResponse:
        """
        Fetch a recommendation’s relationship by using its identifier
        """
        method = "GET"
        url = f"/v1/me/recommendations/{item_id}/{relationship}"
        req_map = {'params': {}}
        if include is not None:
            req_map["params"]["include"] = ','.join(str(x) for x in include)
        
        if lang is not None:
            req_map["params"]["l"] = lang
        
        if limit is not None:
            req_map["params"]["limit"] = limit
        
        if extend is not None:
            req_map["params"]["extend"] = ','.join(str(x) for x in extend)
        
        code, resp = self._api_request(endpoint=url, method=method, **req_map, user_token=user_token)
        result = {
            200: RelationshipResponse,
            401: UnauthorizedResponse,
            403: ForbiddenResponse,
            500: ErrorsResponse,
            404: NotFoundResponse
        }[code](**resp)
        if code > 400:
            raise Exception(result)
        
        return result

    def get_recommendations(
            self,
            user_token: str,
            ids: list[str],
            lang: str | None = None,
            include: list[str] | None = None,
            extend: list[str] | None = None,
    ) -> PersonalRecommendationResponse:
        """
        Fetch one or more recommendations by using their identifiers
        """
        method = "GET"
        url = f"/v1/me/recommendations"
        req_map = {'params': {}}
        req_map["params"]["ids"] = ','.join(str(x) for x in ids)
        
        if lang is not None:
            req_map["params"]["l"] = lang
        
        if include is not None:
            req_map["params"]["include"] = ','.join(str(x) for x in include)
        
        if extend is not None:
            req_map["params"]["extend"] = ','.join(str(x) for x in extend)
        
        code, resp = self._api_request(endpoint=url, method=method, **req_map, user_token=user_token)
        result = {
            200: PersonalRecommendationResponse,
            401: UnauthorizedResponse,
            403: ForbiddenResponse,
            500: ErrorsResponse,
            404: NotFoundResponse
        }[code](**resp)
        if code > 400:
            raise Exception(result)
        
        return result

    def get_recommendations_any(
            self,
            user_token: str,
            lang: str | None = None,
            limit: int | None = None,
            offset: str | None = None,
            include: list[str] | None = None,
            extend: list[str] | None = None,
    ) -> PersonalRecommendationResponse:
        """Fetch default recommendations."""
        method = "GET"
        url = f"/v1/me/recommendations"
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
        
        code, resp = self._api_request(endpoint=url, method=method, **req_map, user_token=user_token)
        result = {
            200: PersonalRecommendationResponse,
            401: UnauthorizedResponse,
            403: ForbiddenResponse,
            500: ErrorsResponse,
            404: NotFoundResponse
        }[code](**resp)
        if code > 400:
            raise Exception(result)
        
        return result
