from ..models import *
from ..token import MTAppleMusic


class AppleMusicAPI(MTAppleMusic):
    def get_catalog(
            self,
            storefront: str,
            include: list[str] | None = None,
            lang: str | None = None,
            extend: list[str] | None = None,
            stations_ids: list[str] | None = None,
            station_genres_ids: list[str] | None = None,
            songs_ids: list[str] | None = None,
            record_labels_ids: list[str] | None = None,
            ratings_ids: list[str] | None = None,
            playlists_ids: list[str] | None = None,
            music_videos_ids: list[str] | None = None,
            genres_ids: list[str] | None = None,
            curators_ids: list[str] | None = None,
            artists_ids: list[str] | None = None,
            apple_curators_ids: list[str] | None = None,
            albums_ids: list[str] | None = None,
            activities_ids: list[str] | None = None,
    ) -> ResourceCollectionResponse:
        """
        Fetch one or more catalog resources by using their identifiers
        """
        method = "GET"
        url = f"/v1/catalog/{storefront}"
        req_map = {'params': {}}
        if include is not None:
            req_map["params"]["include"] = ','.join(str(x) for x in include)
        
        if lang is not None:
            req_map["params"]["l"] = lang
        
        if extend is not None:
            req_map["params"]["extend"] = ','.join(str(x) for x in extend)
        
        if stations_ids is not None:
            req_map["params"]["ids[stations]"] = ','.join(str(x) for x in stations_ids)
        
        if station_genres_ids is not None:
            req_map["params"]["ids[station-genres]"] = ','.join(str(x) for x in station_genres_ids)
        
        if songs_ids is not None:
            req_map["params"]["ids[songs]"] = ','.join(str(x) for x in songs_ids)
        
        if record_labels_ids is not None:
            req_map["params"]["ids[record-labels]"] = ','.join(str(x) for x in record_labels_ids)
        
        if ratings_ids is not None:
            req_map["params"]["ids[ratings]"] = ','.join(str(x) for x in ratings_ids)
        
        if playlists_ids is not None:
            req_map["params"]["ids[playlists]"] = ','.join(str(x) for x in playlists_ids)
        
        if music_videos_ids is not None:
            req_map["params"]["ids[music-videos]"] = ','.join(str(x) for x in music_videos_ids)
        
        if genres_ids is not None:
            req_map["params"]["ids[genres]"] = ','.join(str(x) for x in genres_ids)
        
        if curators_ids is not None:
            req_map["params"]["ids[curators]"] = ','.join(str(x) for x in curators_ids)
        
        if artists_ids is not None:
            req_map["params"]["ids[artists]"] = ','.join(str(x) for x in artists_ids)
        
        if apple_curators_ids is not None:
            req_map["params"]["ids[apple-curators]"] = ','.join(str(x) for x in apple_curators_ids)
        
        if albums_ids is not None:
            req_map["params"]["ids[albums]"] = ','.join(str(x) for x in albums_ids)
        
        if activities_ids is not None:
            req_map["params"]["ids[activities]"] = ','.join(str(x) for x in activities_ids)
        
        code, resp = self._api_request(endpoint=url, method=method, **req_map)
        result = {
            200: ResourceCollectionResponse,
            401: UnauthorizedResponse,
            500: ErrorsResponse,
            404: NotFoundResponse
        }[code](**resp)
        if code > 400:
            raise Exception(result)
        
        return result

    def get_library(
            self,
            user_token: str,
            include: list[str] | None = None,
            lang: str | None = None,
            extend: list[str] | None = None,
            library_songs_ids: list[str] | None = None,
            library_playlists_ids: list[str] | None = None,
            library_playlist_folders_ids: list[str] | None = None,
            library_music_videos_ids: list[str] | None = None,
            library_artists_ids: list[str] | None = None,
            library_albums_ids: list[str] | None = None,
    ) -> ResourceCollectionResponse:
        """
        Fetch one or more library resources by using their identifiers
        """
        method = "GET"
        url = f"/v1/me/library"
        req_map = {'params': {}}
        if include is not None:
            req_map["params"]["include"] = ','.join(str(x) for x in include)
        
        if lang is not None:
            req_map["params"]["l"] = lang
        
        if extend is not None:
            req_map["params"]["extend"] = ','.join(str(x) for x in extend)
        
        if library_songs_ids is not None:
            req_map["params"]["ids[library-songs]"] = ','.join(str(x) for x in library_songs_ids)
        
        if library_playlists_ids is not None:
            req_map["params"]["ids[library-playlists]"] = ','.join(str(x) for x in library_playlists_ids)
        
        if library_playlist_folders_ids is not None:
            req_map["params"]["ids[library-playlist-folders]"] = ','.join(str(x) for x in library_playlist_folders_ids)
        
        if library_music_videos_ids is not None:
            req_map["params"]["ids[library-music-videos]"] = ','.join(str(x) for x in library_music_videos_ids)
        
        if library_artists_ids is not None:
            req_map["params"]["ids[library-artists]"] = ','.join(str(x) for x in library_artists_ids)
        
        if library_albums_ids is not None:
            req_map["params"]["ids[library-albums]"] = ','.join(str(x) for x in library_albums_ids)
        
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

    def get_test(
            self,
            lang: str | None = None,
    ) -> EmptyBodyResponse:
        """"""
        method = "GET"
        url = f"/v1/test"
        req_map = {'params': {}}
        if lang is not None:
            req_map["params"]["l"] = lang
        
        code, resp = self._api_request(endpoint=url, method=method, **req_map)
        result = {
            200: EmptyBodyResponse,
            401: UnauthorizedResponse,
            500: ErrorsResponse,
            404: NotFoundResponse
        }[code](**resp)
        if code > 400:
            raise Exception(result)
        
        return result

    def get_storefront_any(
            self,
            user_token: str,
            lang: str | None = None,
            limit: int | None = None,
            include: list[str] | None = None,
            offset: str | None = None,
            extend: list[str] | None = None,
    ) -> PaginatedResourceCollectionResponse:
        """Fetch a storefront for a specific user."""
        method = "GET"
        url = f"/v1/me/storefront"
        req_map = {'params': {}}
        if lang is not None:
            req_map["params"]["l"] = lang
        
        if limit is not None:
            req_map["params"]["limit"] = limit
        
        if include is not None:
            req_map["params"]["include"] = ','.join(str(x) for x in include)
        
        if offset is not None:
            req_map["params"]["offset"] = offset
        
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
