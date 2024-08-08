from ..models import *
from ..token import MTAppleMusic


class Albums(MTAppleMusic):
    def get_album(
            self,
            item_id: str,
            storefront: str,
            lang: str | None = None,
            include: list[str] | None = None,
            views: list[str] | None = None,
            extend: list[str] | None = None,
    ) -> AlbumsResponse:
        """Fetch an album by using its identifier."""
        method = "GET"
        url = f"/v1/catalog/{storefront}/albums/{item_id}"
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
            200: AlbumsResponse,
            401: UnauthorizedResponse,
            500: ErrorsResponse,
            404: NotFoundResponse
        }[code](**resp)
        if code > 400:
            raise Exception(result)
        
        return result

    def get_album_relation(
            self,
            item_id: str,
            relationship: str,
            storefront: str,
            lang: str | None = None,
            include: list[str] | None = None,
            limit: int | None = None,
            extend: list[str] | None = None,
    ) -> RelationshipResponse:
        """Fetch an album’s relationship by using its identifier."""
        method = "GET"
        url = f"/v1/catalog/{storefront}/albums/{item_id}/{relationship}"
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
            403: ForbiddenResponse,
            500: ErrorsResponse,
            404: NotFoundResponse
        }[code](**resp)
        if code > 400:
            raise Exception(result)
        
        return result

    def get_album_view(
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
        Fetch related resources for a single album’s relationship view
        """
        method = "GET"
        url = f"/v1/catalog/{storefront}/albums/{item_id}/view/{view}"
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

    def get_albums(
            self,
            storefront: str,
            ids: list[str],
            include: list[str] | None = None,
            lang: str | None = None,
            extend: list[str] | None = None,
    ) -> AlbumsResponse:
        """Fetch one or more albums by using their identifiers."""
        method = "GET"
        url = f"/v1/catalog/{storefront}/albums"
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
            200: AlbumsResponse,
            401: UnauthorizedResponse,
            500: ErrorsResponse,
            404: NotFoundResponse
        }[code](**resp)
        if code > 400:
            raise Exception(result)
        
        return result

    def get_albums_by_upc(
            self,
            storefront: str,
            upc: list[str],
            extend: list[str] | None = None,
            include: list[str] | None = None,
            lang: str | None = None,
    ) -> AlbumsResponse:
        """Fetch one or more albums by using their UPC values."""
        method = "GET"
        url = f"/v1/catalog/{storefront}/albums"
        req_map = {'params': {}}
        if extend is not None:
            req_map["params"]["extend"] = ','.join(str(x) for x in extend)
        
        req_map["params"]["filter[upc]"] = ','.join(str(x) for x in upc)
        
        if include is not None:
            req_map["params"]["include"] = ','.join(str(x) for x in include)
        
        if lang is not None:
            req_map["params"]["l"] = lang
        
        code, resp = self._api_request(endpoint=url, method=method, **req_map)
        result = {
            200: AlbumsResponse,
            401: UnauthorizedResponse,
            500: ErrorsResponse,
            404: NotFoundResponse
        }[code](**resp)
        if code > 400:
            raise Exception(result)
        
        return result

    def get_albums_by_equivalents(
            self,
            storefront: str,
            equivalents: list[str],
            include: list[str] | None = None,
            lang: str | None = None,
            restrict: list[str] | None = None,
            extend: list[str] | None = None,
    ) -> AlbumsResponse:
        """
        Fetch the equivalent, available content in the storefront for
        the provided albums’ identifiers
        """
        method = "GET"
        url = f"/v1/catalog/{storefront}/albums"
        req_map = {'params': {}}
        req_map["params"]["filter[equivalents]"] = ','.join(str(x) for x in equivalents)
        
        if include is not None:
            req_map["params"]["include"] = ','.join(str(x) for x in include)
        
        if lang is not None:
            req_map["params"]["l"] = lang
        
        if restrict is not None:
            req_map["params"]["restrict"] = ','.join(str(x) for x in restrict)
        
        if extend is not None:
            req_map["params"]["extend"] = ','.join(str(x) for x in extend)
        
        code, resp = self._api_request(endpoint=url, method=method, **req_map)
        result = {
            200: AlbumsResponse,
            401: UnauthorizedResponse,
            500: ErrorsResponse,
            404: NotFoundResponse
        }[code](**resp)
        if code > 400:
            raise Exception(result)
        
        return result

    def get_library_album(
            self,
            user_token: str,
            item_id: str,
            lang: str | None = None,
            include: list[str] | None = None,
            extend: list[str] | None = None,
    ) -> LibraryAlbumsResponse:
        """Fetch a library album by using its identifier."""
        method = "GET"
        url = f"/v1/me/library/albums/{item_id}"
        req_map = {'params': {}}
        if lang is not None:
            req_map["params"]["l"] = lang
        
        if include is not None:
            req_map["params"]["include"] = ','.join(str(x) for x in include)
        
        if extend is not None:
            req_map["params"]["extend"] = ','.join(str(x) for x in extend)
        
        code, resp = self._api_request(endpoint=url, method=method, **req_map, user_token=user_token)
        result = {
            200: LibraryAlbumsResponse,
            401: UnauthorizedResponse,
            403: ForbiddenResponse,
            500: ErrorsResponse,
            404: NotFoundResponse
        }[code](**resp)
        if code > 400:
            raise Exception(result)
        
        return result

    def get_library_album_relation(
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
        Fetch a library album’s relationship by using its identifier
        """
        method = "GET"
        url = f"/v1/me/library/albums/{item_id}/{relationship}"
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

    def get_library_albums(
            self,
            user_token: str,
            ids: list[str],
            lang: str | None = None,
            include: list[str] | None = None,
            extend: list[str] | None = None,
    ) -> LibraryAlbumsResponse:
        """
        Fetch one or more library albums by using their identifiers
        """
        method = "GET"
        url = f"/v1/me/library/albums"
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
            200: LibraryAlbumsResponse,
            401: UnauthorizedResponse,
            403: ForbiddenResponse,
            500: ErrorsResponse,
            404: NotFoundResponse
        }[code](**resp)
        if code > 400:
            raise Exception(result)
        
        return result

    def get_library_albums_any(
            self,
            user_token: str,
            include: list[str] | None = None,
            lang: str | None = None,
            limit: int | None = None,
            offset: str | None = None,
            extend: list[str] | None = None,
    ) -> LibraryAlbumsResponse:
        """Fetch all the library albums in alphabetical order."""
        method = "GET"
        url = f"/v1/me/library/albums"
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
            200: LibraryAlbumsResponse,
            401: UnauthorizedResponse,
            403: ForbiddenResponse,
            500: ErrorsResponse,
            404: NotFoundResponse
        }[code](**resp)
        if code > 400:
            raise Exception(result)
        
        return result

    def set_library_albums(
            self,
            user_token: str,
            ids: list[str],
            lang: str | None = None,
    ) -> EmptyBodyResponse:
        """Add a catalog resource to a user’s iCloud Music Library."""
        method = "POST"
        url = f"/v1/me/library"
        req_map = {'params': {}}
        req_map["params"]["ids"] = ','.join(str(x) for x in ids)
        
        if lang is not None:
            req_map["params"]["l"] = lang
        
        code, resp = self._api_request(endpoint=url, method=method, **req_map, user_token=user_token)
        result = {
            202: EmptyBodyResponse,
            401: UnauthorizedResponse,
            403: ForbiddenResponse,
            500: ErrorsResponse,
            404: NotFoundResponse
        }[code](**resp)
        if code > 400:
            raise Exception(result)
        
        return result
