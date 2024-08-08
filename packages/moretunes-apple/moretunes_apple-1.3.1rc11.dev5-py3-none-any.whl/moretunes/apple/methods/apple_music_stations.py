from ..models import *
from ..token import MTAppleMusic


class AppleMusicStations(MTAppleMusic):
    def get_station(
            self,
            item_id: str,
            storefront: str,
            include: list[str] | None = None,
            lang: str | None = None,
            extend: list[str] | None = None,
    ) -> StationsResponse:
        """Fetch a station by using its identifier."""
        method = "GET"
        url = f"/v1/catalog/{storefront}/stations/{item_id}"
        req_map = {'params': {}}
        if include is not None:
            req_map["params"]["include"] = ','.join(str(x) for x in include)
        
        if lang is not None:
            req_map["params"]["l"] = lang
        
        if extend is not None:
            req_map["params"]["extend"] = ','.join(str(x) for x in extend)
        
        code, resp = self._api_request(endpoint=url, method=method, **req_map)
        result = {
            200: StationsResponse,
            401: UnauthorizedResponse,
            500: ErrorsResponse,
            404: NotFoundResponse
        }[code](**resp)
        if code > 400:
            raise Exception(result)
        
        return result

    def get_station_relation(
            self,
            item_id: str,
            relationship: str,
            storefront: str,
            lang: str | None = None,
            include: list[str] | None = None,
            extend: list[str] | None = None,
            limit: int | None = None,
    ) -> RelationshipResponse:
        """Fetch a station's relationship using its identifier."""
        method = "GET"
        url = f"/v1/catalog/{storefront}/stations/{item_id}/{relationship}"
        req_map = {'params': {}}
        if lang is not None:
            req_map["params"]["l"] = lang
        
        if include is not None:
            req_map["params"]["include"] = ','.join(str(x) for x in include)
        
        if extend is not None:
            req_map["params"]["extend"] = ','.join(str(x) for x in extend)
        
        if limit is not None:
            req_map["params"]["limit"] = limit
        
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

    def get_stations(
            self,
            storefront: str,
            ids: list[str],
            lang: str | None = None,
            include: list[str] | None = None,
            extend: list[str] | None = None,
    ) -> StationsResponse:
        """Fetch one or more stations by using their identifiers."""
        method = "GET"
        url = f"/v1/catalog/{storefront}/stations"
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
            200: StationsResponse,
            401: UnauthorizedResponse,
            500: ErrorsResponse,
            404: NotFoundResponse
        }[code](**resp)
        if code > 400:
            raise Exception(result)
        
        return result

    def get_stations_by_featured(
            self,
            storefront: str,
            featured: list[str],
            include: list[str] | None = None,
            lang: str | None = None,
            extend: list[str] | None = None,
    ) -> StationsResponse:
        """
        Fetch the Apple Music live radio stations for the storefront
        """
        method = "GET"
        url = f"/v1/catalog/{storefront}/stations"
        req_map = {'params': {}}
        req_map["params"]["filter[featured]"] = ','.join(str(x) for x in featured)
        
        if include is not None:
            req_map["params"]["include"] = ','.join(str(x) for x in include)
        
        if lang is not None:
            req_map["params"]["l"] = lang
        
        if extend is not None:
            req_map["params"]["extend"] = ','.join(str(x) for x in extend)
        
        code, resp = self._api_request(endpoint=url, method=method, **req_map)
        result = {
            200: StationsResponse,
            401: UnauthorizedResponse,
            500: ErrorsResponse,
            404: NotFoundResponse
        }[code](**resp)
        if code > 400:
            raise Exception(result)
        
        return result

    def get_stations_by_identity(
            self,
            storefront: str,
            identity: list[str],
            include: list[str] | None = None,
            lang: str | None = None,
            extend: list[str] | None = None,
    ) -> StationsResponse:
        """Fetch the current user’s personal Apple Music station."""
        method = "GET"
        url = f"/v1/catalog/{storefront}/stations"
        req_map = {'params': {}}
        req_map["params"]["filter[identity]"] = ','.join(str(x) for x in identity)
        
        if include is not None:
            req_map["params"]["include"] = ','.join(str(x) for x in include)
        
        if lang is not None:
            req_map["params"]["l"] = lang
        
        if extend is not None:
            req_map["params"]["extend"] = ','.join(str(x) for x in extend)
        
        code, resp = self._api_request(endpoint=url, method=method, **req_map)
        result = {
            200: StationsResponse,
            401: UnauthorizedResponse,
            403: ForbiddenResponse,
            500: ErrorsResponse,
            404: NotFoundResponse
        }[code](**resp)
        if code > 400:
            raise Exception(result)
        
        return result

    def get_station_genre(
            self,
            item_id: str,
            storefront: str,
            include: list[str] | None = None,
            lang: str | None = None,
            extend: list[str] | None = None,
    ) -> StationGenresResponse:
        """Fetch a station genre by using its identifier."""
        method = "GET"
        url = f"/v1/catalog/{storefront}/station-genres/{item_id}"
        req_map = {'params': {}}
        if include is not None:
            req_map["params"]["include"] = ','.join(str(x) for x in include)
        
        if lang is not None:
            req_map["params"]["l"] = lang
        
        if extend is not None:
            req_map["params"]["extend"] = ','.join(str(x) for x in extend)
        
        code, resp = self._api_request(endpoint=url, method=method, **req_map)
        result = {
            200: StationGenresResponse,
            401: UnauthorizedResponse,
            500: ErrorsResponse,
            404: NotFoundResponse
        }[code](**resp)
        if code > 400:
            raise Exception(result)
        
        return result

    def get_station_genre_relation(
            self,
            item_id: str,
            relationship: str,
            storefront: str,
            include: list[str] | None = None,
            lang: str | None = None,
            limit: int | None = None,
            extend: list[str] | None = None,
    ) -> RelationshipResponse:
        """
        Fetch a station genre’s relationship by using its identifier
        """
        method = "GET"
        url = f"/v1/catalog/{storefront}/station-genres/{item_id}/{relationship}"
        req_map = {'params': {}}
        if include is not None:
            req_map["params"]["include"] = ','.join(str(x) for x in include)
        
        if lang is not None:
            req_map["params"]["l"] = lang
        
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

    def get_station_genres(
            self,
            storefront: str,
            ids: list[str],
            include: list[str] | None = None,
            lang: str | None = None,
            extend: list[str] | None = None,
    ) -> StationGenresResponse:
        """
        Fetch one or more station genres by using their identifiers
        """
        method = "GET"
        url = f"/v1/catalog/{storefront}/station-genres"
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
            200: StationGenresResponse,
            401: UnauthorizedResponse,
            500: ErrorsResponse,
            404: NotFoundResponse
        }[code](**resp)
        if code > 400:
            raise Exception(result)
        
        return result

    def get_station_genres_any(
            self,
            storefront: str,
            include: list[str] | None = None,
            lang: str | None = None,
            limit: int | None = None,
            offset: str | None = None,
            extend: list[str] | None = None,
    ) -> StationGenresResponse:
        """Fetch all station genres for a given storefront."""
        method = "GET"
        url = f"/v1/catalog/{storefront}/station-genres"
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
        
        code, resp = self._api_request(endpoint=url, method=method, **req_map)
        result = {
            200: StationGenresResponse,
            401: UnauthorizedResponse,
            500: ErrorsResponse,
            404: NotFoundResponse
        }[code](**resp)
        if code > 400:
            raise Exception(result)
        
        return result
