from ..models import *
from ..token import MTAppleMusic


class History(MTAppleMusic):
    def get_history_heavy_rotation_any(
            self,
            user_token: str,
            lang: str | None = None,
            limit: int | None = None,
            offset: str | None = None,
            include: list[str] | None = None,
            extend: list[str] | None = None,
    ) -> PaginatedResourceCollectionResponse:
        """Fetch the resources in heavy rotation for the user."""
        method = "GET"
        url = f"/v1/me/history/heavy-rotation"
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
            200: PaginatedResourceCollectionResponse,
            401: UnauthorizedResponse,
            403: ForbiddenResponse,
            500: ErrorsResponse,
            404: NotFoundResponse
        }[code](**resp)
        if code > 400:
            raise Exception(result)
        
        return result

    def get_recent_played_any(
            self,
            user_token: str,
            lang: str | None = None,
            limit: int | None = None,
            offset: str | None = None,
            include: list[str] | None = None,
            extend: list[str] | None = None,
    ) -> PaginatedResourceCollectionResponse:
        """Fetch the recently played resources for the user."""
        method = "GET"
        url = f"/v1/me/recent/played"
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
            200: PaginatedResourceCollectionResponse,
            401: UnauthorizedResponse,
            403: ForbiddenResponse,
            500: ErrorsResponse,
            404: NotFoundResponse
        }[code](**resp)
        if code > 400:
            raise Exception(result)
        
        return result

    def get_recent_played_tracks_any(
            self,
            user_token: str,
            types: list[str],
            include: list[str] | None = None,
            lang: str | None = None,
            limit: int | None = None,
            offset: str | None = None,
            extend: list[str] | None = None,
    ) -> PaginatedResourceCollectionResponse:
        """Fetch the recently played tracks for the user."""
        method = "GET"
        url = f"/v1/me/recent/played/tracks"
        req_map = {'params': {}}
        if include is not None:
            req_map["params"]["include"] = ','.join(str(x) for x in include)
        
        if lang is not None:
            req_map["params"]["l"] = lang
        
        if limit is not None:
            req_map["params"]["limit"] = limit
        
        if offset is not None:
            req_map["params"]["offset"] = offset
        
        if extend is not None:
            req_map["params"]["extend"] = ','.join(str(x) for x in extend)
        
        req_map["params"]["types"] = ','.join(str(x) for x in types)
        
        code, resp = self._api_request(endpoint=url, method=method, **req_map, user_token=user_token)
        result = {
            200: PaginatedResourceCollectionResponse,
            401: UnauthorizedResponse,
            403: ForbiddenResponse,
            500: ErrorsResponse,
            404: NotFoundResponse
        }[code](**resp)
        if code > 400:
            raise Exception(result)
        
        return result

    def get_recent_radio_stations_any(
            self,
            user_token: str,
            lang: str | None = None,
            limit: int | None = None,
            offset: str | None = None,
            include: list[str] | None = None,
            extend: list[str] | None = None,
    ) -> PaginatedResourceCollectionResponse:
        """Fetch recently played radio stations for the user."""
        method = "GET"
        url = f"/v1/me/recent/radio-stations"
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
            200: PaginatedResourceCollectionResponse,
            401: UnauthorizedResponse,
            403: ForbiddenResponse,
            500: ErrorsResponse,
            404: NotFoundResponse
        }[code](**resp)
        if code > 400:
            raise Exception(result)
        
        return result

    def get_library_recently_added(
            self,
            user_token: str,
            lang: str | None = None,
    ) -> ResourceCollectionResponse:
        """Fetch the resources recently added to the library."""
        method = "GET"
        url = f"/v1/me/library/recently-added"
        req_map = {'params': {}}
        if lang is not None:
            req_map["params"]["l"] = lang
        
        code, resp = self._api_request(endpoint=url, method=method, **req_map, user_token=user_token)
        result = {
            200: ResourceCollectionResponse,
            401: UnauthorizedResponse,
            403: ForbiddenResponse,
            500: ErrorsResponse,
            404: NotFoundResponse
        }[code](**resp)
        if code > 400:
            raise Exception(result)
        
        return result
