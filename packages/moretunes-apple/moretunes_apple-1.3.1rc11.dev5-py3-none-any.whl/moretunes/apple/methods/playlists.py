from ..models import *
from ..token import MTAppleMusic


class Playlists(MTAppleMusic):
    def get_playlist(
            self,
            item_id: str,
            storefront: str,
            lang: str | None = None,
            include: list[str] | None = None,
            views: list[str] | None = None,
            extend: list[str] | None = None,
    ) -> PlaylistsResponse:
        """Fetch a playlist by using its identifier."""
        method = "GET"
        url = f"/v1/catalog/{storefront}/playlists/{item_id}"
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
            200: PlaylistsResponse,
            401: UnauthorizedResponse,
            500: ErrorsResponse,
            404: NotFoundResponse
        }[code](**resp)
        if code > 400:
            raise Exception(result)
        
        return result

    def get_playlist_relation(
            self,
            item_id: str,
            relationship: str,
            storefront: str,
            lang: str | None = None,
            include: list[str] | None = None,
            limit: int | None = None,
            extend: list[str] | None = None,
    ) -> RelationshipResponse:
        """Fetch a playlist’s relationship by using its identifier."""
        method = "GET"
        url = f"/v1/catalog/{storefront}/playlists/{item_id}/{relationship}"
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

    def get_playlist_view(
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
        Fetch related resources for a single playlist’s relationship
        view
        """
        method = "GET"
        url = f"/v1/catalog/{storefront}/playlists/{item_id}/view/{view}"
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

    def get_playlists(
            self,
            storefront: str,
            ids: list[str],
            lang: str | None = None,
            include: list[str] | None = None,
            extend: list[str] | None = None,
    ) -> PlaylistsResponse:
        """Fetch one or more playlists by using their identifiers."""
        method = "GET"
        url = f"/v1/catalog/{storefront}/playlists"
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
            200: PlaylistsResponse,
            401: UnauthorizedResponse,
            500: ErrorsResponse,
            404: NotFoundResponse
        }[code](**resp)
        if code > 400:
            raise Exception(result)
        
        return result

    def get_playlists_by_storefront_chart(
            self,
            storefront: str,
            storefront_chart: list[str],
            extend: list[str] | None = None,
            include: list[str] | None = None,
            lang: str | None = None,
    ) -> PlaylistsResponse:
        """
        Fetch one or more Charts Playlists by using their Storefront
        value
        """
        method = "GET"
        url = f"/v1/catalog/{storefront}/playlists"
        req_map = {'params': {}}
        if extend is not None:
            req_map["params"]["extend"] = ','.join(str(x) for x in extend)
        
        req_map["params"]["filter[storefront-chart]"] = ','.join(str(x) for x in storefront_chart)
        
        if include is not None:
            req_map["params"]["include"] = ','.join(str(x) for x in include)
        
        if lang is not None:
            req_map["params"]["l"] = lang
        
        code, resp = self._api_request(endpoint=url, method=method, **req_map)
        result = {
            200: PlaylistsResponse,
            401: UnauthorizedResponse,
            500: ErrorsResponse,
            404: NotFoundResponse
        }[code](**resp)
        if code > 400:
            raise Exception(result)
        
        return result

    def get_library_playlist(
            self,
            user_token: str,
            item_id: str,
            lang: str | None = None,
            include: list[str] | None = None,
            extend: list[str] | None = None,
    ) -> LibraryPlaylistsResponse:
        """Fetch a library playlist by using its identifier."""
        method = "GET"
        url = f"/v1/me/library/playlists/{item_id}"
        req_map = {'params': {}}
        if lang is not None:
            req_map["params"]["l"] = lang
        
        if include is not None:
            req_map["params"]["include"] = ','.join(str(x) for x in include)
        
        if extend is not None:
            req_map["params"]["extend"] = ','.join(str(x) for x in extend)
        
        code, resp = self._api_request(endpoint=url, method=method, **req_map, user_token=user_token)
        result = {
            200: LibraryPlaylistsResponse,
            401: UnauthorizedResponse,
            403: ForbiddenResponse,
            500: ErrorsResponse,
            404: NotFoundResponse
        }[code](**resp)
        if code > 400:
            raise Exception(result)
        
        return result

    def get_library_playlist_relation(
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
        Fetch a library playlist’s relationship by using its identifier
        """
        method = "GET"
        url = f"/v1/me/library/playlists/{item_id}/{relationship}"
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

    def get_library_playlists(
            self,
            user_token: str,
            ids: list[str],
            lang: str | None = None,
            include: list[str] | None = None,
            extend: list[str] | None = None,
    ) -> LibraryPlaylistsResponse:
        """
        Fetch one or more library playlists by using their identifiers
        """
        method = "GET"
        url = f"/v1/me/library/playlists"
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
            200: LibraryPlaylistsResponse,
            401: UnauthorizedResponse,
            403: ForbiddenResponse,
            500: ErrorsResponse,
            404: NotFoundResponse
        }[code](**resp)
        if code > 400:
            raise Exception(result)
        
        return result

    def get_library_playlists_any(
            self,
            user_token: str,
            include: list[str] | None = None,
            lang: str | None = None,
            limit: int | None = None,
            offset: str | None = None,
            extend: list[str] | None = None,
    ) -> LibraryPlaylistsResponse:
        """Fetch all the library playlists in alphabetical order."""
        method = "GET"
        url = f"/v1/me/library/playlists"
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
            200: LibraryPlaylistsResponse,
            401: UnauthorizedResponse,
            403: ForbiddenResponse,
            500: ErrorsResponse,
            404: NotFoundResponse
        }[code](**resp)
        if code > 400:
            raise Exception(result)
        
        return result

    def get_library_playlist_folders_by_identity(
            self,
            user_token: str,
            identity: list[str],
            include: list[str] | None = None,
            lang: str | None = None,
            extend: list[str] | None = None,
    ) -> LibraryPlaylistFoldersResponse:
        """Fetch the root library playlists folder for the user."""
        method = "GET"
        url = f"/v1/me/library/playlist-folders"
        req_map = {'params': {}}
        req_map["params"]["filter[identity]"] = ','.join(str(x) for x in identity)
        
        if include is not None:
            req_map["params"]["include"] = ','.join(str(x) for x in include)
        
        if lang is not None:
            req_map["params"]["l"] = lang
        
        if extend is not None:
            req_map["params"]["extend"] = ','.join(str(x) for x in extend)
        
        code, resp = self._api_request(endpoint=url, method=method, **req_map, user_token=user_token)
        result = {
            200: LibraryPlaylistFoldersResponse,
            401: UnauthorizedResponse,
            403: ForbiddenResponse,
            500: ErrorsResponse,
            404: NotFoundResponse
        }[code](**resp)
        if code > 400:
            raise Exception(result)
        
        return result

    def get_library_playlist_folder(
            self,
            user_token: str,
            item_id: str,
            include: list[str] | None = None,
            lang: str | None = None,
            extend: list[str] | None = None,
    ) -> LibraryPlaylistFoldersResponse:
        """Fetch a library playlist folder by using its identifier."""
        method = "GET"
        url = f"/v1/me/library/playlist-folders/{item_id}"
        req_map = {'params': {}}
        if include is not None:
            req_map["params"]["include"] = ','.join(str(x) for x in include)
        
        if lang is not None:
            req_map["params"]["l"] = lang
        
        if extend is not None:
            req_map["params"]["extend"] = ','.join(str(x) for x in extend)
        
        code, resp = self._api_request(endpoint=url, method=method, **req_map, user_token=user_token)
        result = {
            200: LibraryPlaylistFoldersResponse,
            401: UnauthorizedResponse,
            403: ForbiddenResponse,
            500: ErrorsResponse,
            404: NotFoundResponse
        }[code](**resp)
        if code > 400:
            raise Exception(result)
        
        return result

    def get_library_playlist_folder_relation(
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
        Fetch a library playlist folder’s relationship by using its identifier
        """
        method = "GET"
        url = f"/v1/me/library/playlist-folders/{item_id}/{relationship}"
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

    def get_library_playlist_folders(
            self,
            user_token: str,
            ids: list[str],
            include: list[str] | None = None,
            lang: str | None = None,
            extend: list[str] | None = None,
    ) -> LibraryPlaylistFoldersResponse:
        """
        Fetch one or more library playlist folders by using their identifiers
        """
        method = "GET"
        url = f"/v1/me/library/playlist-folders"
        req_map = {'params': {}}
        req_map["params"]["ids"] = ','.join(str(x) for x in ids)
        
        if include is not None:
            req_map["params"]["include"] = ','.join(str(x) for x in include)
        
        if lang is not None:
            req_map["params"]["l"] = lang
        
        if extend is not None:
            req_map["params"]["extend"] = ','.join(str(x) for x in extend)
        
        code, resp = self._api_request(endpoint=url, method=method, **req_map, user_token=user_token)
        result = {
            200: LibraryPlaylistFoldersResponse,
            401: UnauthorizedResponse,
            403: ForbiddenResponse,
            500: ErrorsResponse,
            404: NotFoundResponse
        }[code](**resp)
        if code > 400:
            raise Exception(result)
        
        return result

    def add_library_playlist_folders(
            self,
            user_token: str,
            body: LibraryPlaylistFolderCreationRequest,
            lang: str | None = None,
    ) -> LibraryPlaylistFoldersResponse:
        """Create a new playlist folder in a user’s library."""
        method = "POST"
        url = f"/v1/me/library/playlist-folders"
        req_map = {'params': {}}
        if lang is not None:
            req_map["params"]["l"] = lang
        
        req_map["body"] = body
        
        code, resp = self._api_request(endpoint=url, method=method, **req_map, user_token=user_token)
        result = {
            201: LibraryPlaylistFoldersResponse,
            401: UnauthorizedResponse,
            403: ForbiddenResponse,
            500: ErrorsResponse,
            404: NotFoundResponse
        }[code](**resp)
        if code > 400:
            raise Exception(result)
        
        return result

    def add_library_playlists(
            self,
            user_token: str,
            body: LibraryPlaylistCreationRequest,
            lang: str | None = None,
    ) -> LibraryPlaylistsResponse:
        """Create a new playlist in a user’s library."""
        method = "POST"
        url = f"/v1/me/library/playlists"
        req_map = {'params': {}}
        if lang is not None:
            req_map["params"]["l"] = lang
        
        req_map["body"] = body
        
        code, resp = self._api_request(endpoint=url, method=method, **req_map, user_token=user_token)
        result = {
            201: LibraryPlaylistsResponse,
            401: UnauthorizedResponse,
            403: ForbiddenResponse,
            500: ErrorsResponse,
            404: NotFoundResponse
        }[code](**resp)
        if code > 400:
            raise Exception(result)
        
        return result

    def set_library_playlist_tracks(
            self,
            user_token: str,
            item_id: str,
            body: LibraryPlaylistTracksRequest,
            lang: str | None = None,
    ) -> LibraryPlaylistsTracksRelationshipResponse:
        """Add new tracks to the end of a library playlist."""
        method = "POST"
        url = f"/v1/me/library/playlists/{item_id}/tracks"
        req_map = {'params': {}}
        if lang is not None:
            req_map["params"]["l"] = lang
        
        req_map["body"] = body
        
        code, resp = self._api_request(endpoint=url, method=method, **req_map, user_token=user_token)
        result = {
            201: LibraryPlaylistsTracksRelationshipResponse,
            401: UnauthorizedResponse,
            403: ForbiddenResponse,
            500: ErrorsResponse,
            404: NotFoundResponse
        }[code](**resp)
        if code > 400:
            raise Exception(result)
        
        return result

    def set_library_playlists(
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
