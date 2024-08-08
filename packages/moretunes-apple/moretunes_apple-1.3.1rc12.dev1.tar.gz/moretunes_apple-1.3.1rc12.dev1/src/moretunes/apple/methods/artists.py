from ..models import *
from ..token import MTAppleMusic


class Artists(MTAppleMusic):
    def get_artist(
            self,
            item_id: str,
            storefront: str,
            lang: str | None = None,
            include: list[str] | None = None,
            views: list[str] | None = None,
            extend: list[str] | None = None,
    ) -> ArtistsResponse:
        """Fetch an artist by using the artist’s identifier."""
        method = "GET"
        url = f"/v1/catalog/{storefront}/artists/{item_id}"
        req_map = {'params': {}}
        if lang is not None:
            req_map["params"]["l"] = lang
        
        if include is not None:
            req_map["params"]["include"] = ','.join(str(x) for x in include)
        
        if views is not None:
            req_map["params"]["views"] = ','.join(str(x) for x in views)
        
        if extend is not None:
            req_map["params"]["extend"] = ','.join(str(x) for x in extend)
        
        code, resp = self._api_request(endpoint=url, method=method, **req_map)
        result = {
            200: ArtistsResponse,
            401: UnauthorizedResponse,
            500: ErrorsResponse,
            404: NotFoundResponse
        }[code](**resp)
        if code > 400:
            raise Exception(result)
        
        return result

    def get_artist_relation(
            self,
            item_id: str,
            relationship: str,
            storefront: str,
            lang: str | None = None,
            include: list[str] | None = None,
            limit: int | None = None,
            extend: list[str] | None = None,
    ) -> RelationshipResponse:
        """Fetch an artist’s relationship by using its identifier."""
        method = "GET"
        url = f"/v1/catalog/{storefront}/artists/{item_id}/{relationship}"
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

    def get_artist_view(
            self,
            item_id: str,
            storefront: str,
            view: str,
            extend: list[str] | None = None,
            include: list[str] | None = None,
            lang: str | None = None,
            limit: int | None = None,
            attr_fields: list[str] | None = None,
    ) -> RelationshipViewResponse:
        """
        Fetch related resources for a single artist’s relationship view
        """
        method = "GET"
        url = f"/v1/catalog/{storefront}/artists/{item_id}/view/{view}"
        req_map = {'params': {}}
        if extend is not None:
            req_map["params"]["extend"] = ','.join(str(x) for x in extend)
        
        if include is not None:
            req_map["params"]["include"] = ','.join(str(x) for x in include)
        
        if lang is not None:
            req_map["params"]["l"] = lang
        
        if limit is not None:
            req_map["params"]["limit"] = limit
        
        if attr_fields is not None:
            req_map["params"]["with"] = ','.join(str(x) for x in attr_fields)
        
        code, resp = self._api_request(endpoint=url, method=method, **req_map)
        result = {
            200: RelationshipViewResponse,
            401: UnauthorizedResponse,
            500: ErrorsResponse,
            404: NotFoundResponse
        }[code](**resp)
        if code > 400:
            raise Exception(result)
        
        return result

    def get_artists(
            self,
            storefront: str,
            ids: list[str],
            lang: str | None = None,
            include: list[str] | None = None,
            extend: list[str] | None = None,
    ) -> ArtistsResponse:
        """Fetch one or more artists by using their identifiers."""
        method = "GET"
        url = f"/v1/catalog/{storefront}/artists"
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
            200: ArtistsResponse,
            401: UnauthorizedResponse,
            500: ErrorsResponse,
            404: NotFoundResponse
        }[code](**resp)
        if code > 400:
            raise Exception(result)
        
        return result

    def get_library_artist(
            self,
            user_token: str,
            item_id: str,
            lang: str | None = None,
            include: list[str] | None = None,
            extend: list[str] | None = None,
    ) -> LibraryArtistsResponse:
        """Fetch a library artist by using its identifier."""
        method = "GET"
        url = f"/v1/me/library/artists/{item_id}"
        req_map = {'params': {}}
        if lang is not None:
            req_map["params"]["l"] = lang
        
        if include is not None:
            req_map["params"]["include"] = ','.join(str(x) for x in include)
        
        if extend is not None:
            req_map["params"]["extend"] = ','.join(str(x) for x in extend)
        
        code, resp = self._api_request(endpoint=url, method=method, **req_map, user_token=user_token)
        result = {
            200: LibraryArtistsResponse,
            401: UnauthorizedResponse,
            403: ForbiddenResponse,
            500: ErrorsResponse,
            404: NotFoundResponse
        }[code](**resp)
        if code > 400:
            raise Exception(result)
        
        return result

    def get_library_artist_relation(
            self,
            user_token: str,
            item_id: str,
            relationship: str,
            lang: str | None = None,
            include: list[str] | None = None,
            limit: int | None = None,
            extend: list[str] | None = None,
    ) -> RelationshipResponse:
        """
        Fetch a library artist’s relationship by using its identifier
        """
        method = "GET"
        url = f"/v1/me/library/artists/{item_id}/{relationship}"
        req_map = {'params': {}}
        if lang is not None:
            req_map["params"]["l"] = lang
        
        if include is not None:
            req_map["params"]["include"] = ','.join(str(x) for x in include)
        
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

    def get_library_artists(
            self,
            user_token: str,
            ids: list[str],
            lang: str | None = None,
            include: list[str] | None = None,
            extend: list[str] | None = None,
    ) -> LibraryArtistsResponse:
        """
        Fetch one or more library artists by using their identifiers
        """
        method = "GET"
        url = f"/v1/me/library/artists"
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
            200: LibraryArtistsResponse,
            401: UnauthorizedResponse,
            403: ForbiddenResponse,
            500: ErrorsResponse,
            404: NotFoundResponse
        }[code](**resp)
        if code > 400:
            raise Exception(result)
        
        return result

    def get_library_artists_any(
            self,
            user_token: str,
            include: list[str] | None = None,
            lang: str | None = None,
            limit: int | None = None,
            offset: str | None = None,
            extend: list[str] | None = None,
    ) -> LibraryArtistsResponse:
        """Fetch all the library artists in alphabetical order."""
        method = "GET"
        url = f"/v1/me/library/artists"
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
        
        code, resp = self._api_request(endpoint=url, method=method, **req_map, user_token=user_token)
        result = {
            200: LibraryArtistsResponse,
            401: UnauthorizedResponse,
            403: ForbiddenResponse,
            500: ErrorsResponse,
            404: NotFoundResponse
        }[code](**resp)
        if code > 400:
            raise Exception(result)
        
        return result
