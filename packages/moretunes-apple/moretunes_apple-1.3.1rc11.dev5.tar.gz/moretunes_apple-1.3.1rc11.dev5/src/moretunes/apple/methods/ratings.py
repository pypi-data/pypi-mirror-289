from ..models import *
from ..token import MTAppleMusic


class Ratings(MTAppleMusic):
    def get_ratings_album(
            self,
            user_token: str,
            item_id: str,
            include: list[str] | None = None,
            lang: str | None = None,
            extend: list[str] | None = None,
    ) -> RatingsResponse:
        """
        Fetch a user’s rating for an album by using the user’s identifier
        """
        method = "GET"
        url = f"/v1/me/ratings/albums/{item_id}"
        req_map = {'params': {}}
        if include is not None:
            req_map["params"]["include"] = ','.join(str(x) for x in include)
        
        if lang is not None:
            req_map["params"]["l"] = lang
        
        if extend is not None:
            req_map["params"]["extend"] = ','.join(str(x) for x in extend)
        
        code, resp = self._api_request(endpoint=url, method=method, **req_map, user_token=user_token)
        result = {
            200: RatingsResponse,
            401: UnauthorizedResponse,
            403: ForbiddenResponse,
            500: ErrorsResponse,
            404: NotFoundResponse
        }[code](**resp)
        if code > 400:
            raise Exception(result)
        
        return result

    def get_ratings_music_video(
            self,
            user_token: str,
            item_id: str,
            include: list[str] | None = None,
            lang: str | None = None,
            extend: list[str] | None = None,
    ) -> RatingsResponse:
        """
        Fetch a user’s rating for a music video by using the video’s
        identifier
        """
        method = "GET"
        url = f"/v1/me/ratings/music-videos/{item_id}"
        req_map = {'params': {}}
        if include is not None:
            req_map["params"]["include"] = ','.join(str(x) for x in include)
        
        if lang is not None:
            req_map["params"]["l"] = lang
        
        if extend is not None:
            req_map["params"]["extend"] = ','.join(str(x) for x in extend)
        
        code, resp = self._api_request(endpoint=url, method=method, **req_map, user_token=user_token)
        result = {
            200: RatingsResponse,
            401: UnauthorizedResponse,
            403: ForbiddenResponse,
            500: ErrorsResponse,
            404: NotFoundResponse
        }[code](**resp)
        if code > 400:
            raise Exception(result)
        
        return result

    def get_ratings_playlist(
            self,
            user_token: str,
            item_id: str,
            include: list[str] | None = None,
            lang: str | None = None,
            extend: list[str] | None = None,
    ) -> RatingsResponse:
        """
        Fetch a user’s rating for a playlist by using the playlist’s
        identifier
        """
        method = "GET"
        url = f"/v1/me/ratings/playlists/{item_id}"
        req_map = {'params': {}}
        if include is not None:
            req_map["params"]["include"] = ','.join(str(x) for x in include)
        
        if lang is not None:
            req_map["params"]["l"] = lang
        
        if extend is not None:
            req_map["params"]["extend"] = ','.join(str(x) for x in extend)
        
        code, resp = self._api_request(endpoint=url, method=method, **req_map, user_token=user_token)
        result = {
            200: RatingsResponse,
            401: UnauthorizedResponse,
            403: ForbiddenResponse,
            500: ErrorsResponse,
            404: NotFoundResponse
        }[code](**resp)
        if code > 400:
            raise Exception(result)
        
        return result

    def get_ratings_song(
            self,
            user_token: str,
            item_id: str,
            include: list[str] | None = None,
            lang: str | None = None,
            extend: list[str] | None = None,
    ) -> RatingsResponse:
        """
        Fetch a user’s rating for a song by using the song’s identifier
        """
        method = "GET"
        url = f"/v1/me/ratings/songs/{item_id}"
        req_map = {'params': {}}
        if include is not None:
            req_map["params"]["include"] = ','.join(str(x) for x in include)
        
        if lang is not None:
            req_map["params"]["l"] = lang
        
        if extend is not None:
            req_map["params"]["extend"] = ','.join(str(x) for x in extend)
        
        code, resp = self._api_request(endpoint=url, method=method, **req_map, user_token=user_token)
        result = {
            200: RatingsResponse,
            401: UnauthorizedResponse,
            403: ForbiddenResponse,
            500: ErrorsResponse,
            404: NotFoundResponse
        }[code](**resp)
        if code > 400:
            raise Exception(result)
        
        return result

    def get_ratings_station(
            self,
            user_token: str,
            item_id: str,
            include: list[str] | None = None,
            lang: str | None = None,
            extend: list[str] | None = None,
    ) -> RatingsResponse:
        """
        Fetch a user’s rating for a station by using the station’s identifier
        """
        method = "GET"
        url = f"/v1/me/ratings/stations/{item_id}"
        req_map = {'params': {}}
        if include is not None:
            req_map["params"]["include"] = ','.join(str(x) for x in include)
        
        if lang is not None:
            req_map["params"]["l"] = lang
        
        if extend is not None:
            req_map["params"]["extend"] = ','.join(str(x) for x in extend)
        
        code, resp = self._api_request(endpoint=url, method=method, **req_map, user_token=user_token)
        result = {
            200: RatingsResponse,
            401: UnauthorizedResponse,
            403: ForbiddenResponse,
            500: ErrorsResponse,
            404: NotFoundResponse
        }[code](**resp)
        if code > 400:
            raise Exception(result)
        
        return result

    def get_ratings_albums(
            self,
            user_token: str,
            ids: list[str],
            include: list[str] | None = None,
            lang: str | None = None,
            extend: list[str] | None = None,
    ) -> RatingsResponse:
        """
        Fetch the user’s ratings for one or more albums by using the
        albums' identifiers
        """
        method = "GET"
        url = f"/v1/me/ratings/albums"
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
            200: RatingsResponse,
            401: UnauthorizedResponse,
            403: ForbiddenResponse,
            500: ErrorsResponse,
            404: NotFoundResponse
        }[code](**resp)
        if code > 400:
            raise Exception(result)
        
        return result

    def get_ratings_music_videos(
            self,
            user_token: str,
            ids: list[str],
            include: list[str] | None = None,
            lang: str | None = None,
            extend: list[str] | None = None,
    ) -> RatingsResponse:
        """
        Fetch the user’s ratings for one or more music videos by using
        the music videos' identifiers
        """
        method = "GET"
        url = f"/v1/me/ratings/music-videos"
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
            200: RatingsResponse,
            401: UnauthorizedResponse,
            403: ForbiddenResponse,
            500: ErrorsResponse,
            404: NotFoundResponse
        }[code](**resp)
        if code > 400:
            raise Exception(result)
        
        return result

    def get_ratings_playlists(
            self,
            user_token: str,
            ids: list[str],
            include: list[str] | None = None,
            lang: str | None = None,
            extend: list[str] | None = None,
    ) -> RatingsResponse:
        """
        Fetch the user’s ratings for one or more playlists by using the
        playlists' identifiers
        """
        method = "GET"
        url = f"/v1/me/ratings/playlists"
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
            200: RatingsResponse,
            401: UnauthorizedResponse,
            403: ForbiddenResponse,
            500: ErrorsResponse,
            404: NotFoundResponse
        }[code](**resp)
        if code > 400:
            raise Exception(result)
        
        return result

    def get_ratings_songs(
            self,
            user_token: str,
            ids: list[str],
            include: list[str] | None = None,
            lang: str | None = None,
            extend: list[str] | None = None,
    ) -> RatingsResponse:
        """
        Fetch the user’s ratings for one or more songs by using the songs'
        identifiers
        """
        method = "GET"
        url = f"/v1/me/ratings/songs"
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
            200: RatingsResponse,
            401: UnauthorizedResponse,
            403: ForbiddenResponse,
            500: ErrorsResponse,
            404: NotFoundResponse
        }[code](**resp)
        if code > 400:
            raise Exception(result)
        
        return result

    def get_ratings_stations(
            self,
            user_token: str,
            ids: list[str],
            include: list[str] | None = None,
            lang: str | None = None,
            extend: list[str] | None = None,
    ) -> RatingsResponse:
        """
        Fetch the user’s ratings for one or more stations by using the
        stations' identifiers
        """
        method = "GET"
        url = f"/v1/me/ratings/stations"
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
            200: RatingsResponse,
            401: UnauthorizedResponse,
            403: ForbiddenResponse,
            500: ErrorsResponse,
            404: NotFoundResponse
        }[code](**resp)
        if code > 400:
            raise Exception(result)
        
        return result

    def set_ratings_album(
            self,
            user_token: str,
            item_id: str,
            body: RatingRequest,
            lang: str | None = None,
    ) -> RatingsResponse:
        """Add a user’s album rating by using the album’s identifier."""
        method = "PUT"
        url = f"/v1/me/ratings/albums/{item_id}"
        req_map = {'params': {}}
        if lang is not None:
            req_map["params"]["l"] = lang
        
        req_map["body"] = body
        
        code, resp = self._api_request(endpoint=url, method=method, **req_map, user_token=user_token)
        result = {
            200: RatingsResponse,
            401: UnauthorizedResponse,
            403: ForbiddenResponse,
            500: ErrorsResponse,
            404: NotFoundResponse
        }[code](**resp)
        if code > 400:
            raise Exception(result)
        
        return result

    def set_ratings_music_video(
            self,
            user_token: str,
            item_id: str,
            body: RatingRequest,
            lang: str | None = None,
    ) -> RatingsResponse:
        """
        Add a user’s music video rating by using the music video’s identifier
        """
        method = "PUT"
        url = f"/v1/me/ratings/music-videos/{item_id}"
        req_map = {'params': {}}
        if lang is not None:
            req_map["params"]["l"] = lang
        
        req_map["body"] = body
        
        code, resp = self._api_request(endpoint=url, method=method, **req_map, user_token=user_token)
        result = {
            200: RatingsResponse,
            401: UnauthorizedResponse,
            403: ForbiddenResponse,
            500: ErrorsResponse,
            404: NotFoundResponse
        }[code](**resp)
        if code > 400:
            raise Exception(result)
        
        return result

    def set_ratings_playlist(
            self,
            user_token: str,
            item_id: str,
            body: RatingRequest,
            lang: str | None = None,
    ) -> RatingsResponse:
        """
        Add a user’s playlist rating by using the playlist’s identifier
        """
        method = "PUT"
        url = f"/v1/me/ratings/playlists/{item_id}"
        req_map = {'params': {}}
        if lang is not None:
            req_map["params"]["l"] = lang
        
        req_map["body"] = body
        
        code, resp = self._api_request(endpoint=url, method=method, **req_map, user_token=user_token)
        result = {
            200: RatingsResponse,
            401: UnauthorizedResponse,
            403: ForbiddenResponse,
            500: ErrorsResponse,
            404: NotFoundResponse
        }[code](**resp)
        if code > 400:
            raise Exception(result)
        
        return result

    def set_ratings_song(
            self,
            user_token: str,
            item_id: str,
            body: RatingRequest,
            lang: str | None = None,
    ) -> RatingsResponse:
        """Add a user’s song rating by using the song’s identifier."""
        method = "PUT"
        url = f"/v1/me/ratings/songs/{item_id}"
        req_map = {'params': {}}
        if lang is not None:
            req_map["params"]["l"] = lang
        
        req_map["body"] = body
        
        code, resp = self._api_request(endpoint=url, method=method, **req_map, user_token=user_token)
        result = {
            200: RatingsResponse,
            401: UnauthorizedResponse,
            403: ForbiddenResponse,
            500: ErrorsResponse,
            404: NotFoundResponse
        }[code](**resp)
        if code > 400:
            raise Exception(result)
        
        return result

    def set_ratings_station(
            self,
            user_token: str,
            item_id: str,
            body: RatingRequest,
            lang: str | None = None,
    ) -> RatingsResponse:
        """
        Add a user’s station rating by using the station’s identifier
        """
        method = "PUT"
        url = f"/v1/me/ratings/stations/{item_id}"
        req_map = {'params': {}}
        if lang is not None:
            req_map["params"]["l"] = lang
        
        req_map["body"] = body
        
        code, resp = self._api_request(endpoint=url, method=method, **req_map, user_token=user_token)
        result = {
            200: RatingsResponse,
            401: UnauthorizedResponse,
            403: ForbiddenResponse,
            500: ErrorsResponse,
            404: NotFoundResponse
        }[code](**resp)
        if code > 400:
            raise Exception(result)
        
        return result

    def rm_ratings_album(
            self,
            user_token: str,
            item_id: str,
            lang: str | None = None,
    ) -> EmptyBodyResponse:
        """
        Remove a user’s album rating by using the album’s identifier
        """
        method = "DELETE"
        url = f"/v1/me/ratings/albums/{item_id}"
        req_map = {'params': {}}
        if lang is not None:
            req_map["params"]["l"] = lang
        
        code, resp = self._api_request(endpoint=url, method=method, **req_map, user_token=user_token)
        result = {
            204: EmptyBodyResponse,
            401: UnauthorizedResponse,
            403: ForbiddenResponse,
            500: ErrorsResponse,
            404: NotFoundResponse
        }[code](**resp)
        if code > 400:
            raise Exception(result)
        
        return result

    def rm_ratings_music_video(
            self,
            user_token: str,
            item_id: str,
            lang: str | None = None,
    ) -> EmptyBodyResponse:
        """
        Remove a user’s music video rating by using the music video’s
        identifier
        """
        method = "DELETE"
        url = f"/v1/me/ratings/music-videos/{item_id}"
        req_map = {'params': {}}
        if lang is not None:
            req_map["params"]["l"] = lang
        
        code, resp = self._api_request(endpoint=url, method=method, **req_map, user_token=user_token)
        result = {
            204: EmptyBodyResponse,
            401: UnauthorizedResponse,
            403: ForbiddenResponse,
            500: ErrorsResponse,
            404: NotFoundResponse
        }[code](**resp)
        if code > 400:
            raise Exception(result)
        
        return result

    def rm_ratings_playlist(
            self,
            user_token: str,
            item_id: str,
            lang: str | None = None,
    ) -> EmptyBodyResponse:
        """
        Remove a user’s playlist rating by using the playlist’s identifier
        """
        method = "DELETE"
        url = f"/v1/me/ratings/playlists/{item_id}"
        req_map = {'params': {}}
        if lang is not None:
            req_map["params"]["l"] = lang
        
        code, resp = self._api_request(endpoint=url, method=method, **req_map, user_token=user_token)
        result = {
            204: EmptyBodyResponse,
            401: UnauthorizedResponse,
            403: ForbiddenResponse,
            500: ErrorsResponse,
            404: NotFoundResponse
        }[code](**resp)
        if code > 400:
            raise Exception(result)
        
        return result

    def rm_ratings_song(
            self,
            user_token: str,
            item_id: str,
            lang: str | None = None,
    ) -> EmptyBodyResponse:
        """Remove a user’s song rating by using the song’s identifier."""
        method = "DELETE"
        url = f"/v1/me/ratings/songs/{item_id}"
        req_map = {'params': {}}
        if lang is not None:
            req_map["params"]["l"] = lang
        
        code, resp = self._api_request(endpoint=url, method=method, **req_map, user_token=user_token)
        result = {
            204: EmptyBodyResponse,
            401: UnauthorizedResponse,
            403: ForbiddenResponse,
            500: ErrorsResponse,
            404: NotFoundResponse
        }[code](**resp)
        if code > 400:
            raise Exception(result)
        
        return result

    def rm_ratings_station(
            self,
            user_token: str,
            item_id: str,
            lang: str | None = None,
    ) -> EmptyBodyResponse:
        """
        Remove a user’s station rating by using the station’s identifier
        """
        method = "DELETE"
        url = f"/v1/me/ratings/stations/{item_id}"
        req_map = {'params': {}}
        if lang is not None:
            req_map["params"]["l"] = lang
        
        code, resp = self._api_request(endpoint=url, method=method, **req_map, user_token=user_token)
        result = {
            204: EmptyBodyResponse,
            401: UnauthorizedResponse,
            403: ForbiddenResponse,
            500: ErrorsResponse,
            404: NotFoundResponse
        }[code](**resp)
        if code > 400:
            raise Exception(result)
        
        return result

    def get_ratings_library_album(
            self,
            user_token: str,
            item_id: str,
            include: list[str] | None = None,
            lang: str | None = None,
            extend: list[str] | None = None,
    ) -> RatingsResponse:
        """
        Fetch a user’s rating for specific content by using the content’s
        identifier
        """
        method = "GET"
        url = f"/v1/me/ratings/library-albums/{item_id}"
        req_map = {'params': {}}
        if include is not None:
            req_map["params"]["include"] = ','.join(str(x) for x in include)
        
        if lang is not None:
            req_map["params"]["l"] = lang
        
        if extend is not None:
            req_map["params"]["extend"] = ','.join(str(x) for x in extend)
        
        code, resp = self._api_request(endpoint=url, method=method, **req_map, user_token=user_token)
        result = {
            200: RatingsResponse,
            401: UnauthorizedResponse,
            403: ForbiddenResponse,
            500: ErrorsResponse,
            404: NotFoundResponse
        }[code](**resp)
        if code > 400:
            raise Exception(result)
        
        return result

    def get_ratings_library_music_video(
            self,
            user_token: str,
            item_id: str,
            include: list[str] | None = None,
            lang: str | None = None,
            extend: list[str] | None = None,
    ) -> RatingsResponse:
        """
        Fetch a user’s rating for a library music video by using the
        music video’s library identifier
        """
        method = "GET"
        url = f"/v1/me/ratings/library-music-videos/{item_id}"
        req_map = {'params': {}}
        if include is not None:
            req_map["params"]["include"] = ','.join(str(x) for x in include)
        
        if lang is not None:
            req_map["params"]["l"] = lang
        
        if extend is not None:
            req_map["params"]["extend"] = ','.join(str(x) for x in extend)
        
        code, resp = self._api_request(endpoint=url, method=method, **req_map, user_token=user_token)
        result = {
            200: RatingsResponse,
            401: UnauthorizedResponse,
            403: ForbiddenResponse,
            500: ErrorsResponse,
            404: NotFoundResponse
        }[code](**resp)
        if code > 400:
            raise Exception(result)
        
        return result

    def get_ratings_library_playlist(
            self,
            user_token: str,
            item_id: str,
            include: list[str] | None = None,
            lang: str | None = None,
            extend: list[str] | None = None,
    ) -> RatingsResponse:
        """
        Fetch a user’s rating for a library playlist by using the playlist’s
        library identifier
        """
        method = "GET"
        url = f"/v1/me/ratings/library-playlists/{item_id}"
        req_map = {'params': {}}
        if include is not None:
            req_map["params"]["include"] = ','.join(str(x) for x in include)
        
        if lang is not None:
            req_map["params"]["l"] = lang
        
        if extend is not None:
            req_map["params"]["extend"] = ','.join(str(x) for x in extend)
        
        code, resp = self._api_request(endpoint=url, method=method, **req_map, user_token=user_token)
        result = {
            200: RatingsResponse,
            401: UnauthorizedResponse,
            403: ForbiddenResponse,
            500: ErrorsResponse,
            404: NotFoundResponse
        }[code](**resp)
        if code > 400:
            raise Exception(result)
        
        return result

    def get_ratings_library_song(
            self,
            user_token: str,
            item_id: str,
            include: list[str] | None = None,
            lang: str | None = None,
            extend: list[str] | None = None,
    ) -> RatingsResponse:
        """
        Fetch a user’s rating for a library song by using the song’s
        library identifier
        """
        method = "GET"
        url = f"/v1/me/ratings/library-songs/{item_id}"
        req_map = {'params': {}}
        if include is not None:
            req_map["params"]["include"] = ','.join(str(x) for x in include)
        
        if lang is not None:
            req_map["params"]["l"] = lang
        
        if extend is not None:
            req_map["params"]["extend"] = ','.join(str(x) for x in extend)
        
        code, resp = self._api_request(endpoint=url, method=method, **req_map, user_token=user_token)
        result = {
            200: RatingsResponse,
            401: UnauthorizedResponse,
            403: ForbiddenResponse,
            500: ErrorsResponse,
            404: NotFoundResponse
        }[code](**resp)
        if code > 400:
            raise Exception(result)
        
        return result

    def get_ratings_library_albums(
            self,
            user_token: str,
            ids: list[str],
            include: list[str] | None = None,
            lang: str | None = None,
            extend: list[str] | None = None,
    ) -> RatingsResponse:
        """
        Fetch the user’s ratings for one or more pieces of content by
        using the contents’ identifiers
        """
        method = "GET"
        url = f"/v1/me/ratings/library-albums"
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
            200: RatingsResponse,
            401: UnauthorizedResponse,
            403: ForbiddenResponse,
            500: ErrorsResponse,
            404: NotFoundResponse
        }[code](**resp)
        if code > 400:
            raise Exception(result)
        
        return result

    def get_ratings_library_music_videos(
            self,
            user_token: str,
            ids: list[str],
            include: list[str] | None = None,
            lang: str | None = None,
            extend: list[str] | None = None,
    ) -> RatingsResponse:
        """
        Fetch the user’s ratings for one or more library music videos
        by using the library music videos' identifiers
        """
        method = "GET"
        url = f"/v1/me/ratings/library-music-videos"
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
            200: RatingsResponse,
            401: UnauthorizedResponse,
            403: ForbiddenResponse,
            500: ErrorsResponse,
            404: NotFoundResponse
        }[code](**resp)
        if code > 400:
            raise Exception(result)
        
        return result

    def get_ratings_library_playlists(
            self,
            user_token: str,
            ids: list[str],
            include: list[str] | None = None,
            lang: str | None = None,
            extend: list[str] | None = None,
    ) -> RatingsResponse:
        """
        Fetch the user’s ratings for one or more library playlists by
        using the library playlists' identifiers
        """
        method = "GET"
        url = f"/v1/me/ratings/library-playlists"
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
            200: RatingsResponse,
            401: UnauthorizedResponse,
            403: ForbiddenResponse,
            500: ErrorsResponse,
            404: NotFoundResponse
        }[code](**resp)
        if code > 400:
            raise Exception(result)
        
        return result

    def get_ratings_library_songs(
            self,
            user_token: str,
            ids: list[str],
            include: list[str] | None = None,
            lang: str | None = None,
            extend: list[str] | None = None,
    ) -> RatingsResponse:
        """
        Fetch the user’s ratings for one or more library songs by using
        the library songs' identifiers
        """
        method = "GET"
        url = f"/v1/me/ratings/library-songs"
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
            200: RatingsResponse,
            401: UnauthorizedResponse,
            403: ForbiddenResponse,
            500: ErrorsResponse,
            404: NotFoundResponse
        }[code](**resp)
        if code > 400:
            raise Exception(result)
        
        return result

    def set_ratings_library_album(
            self,
            user_token: str,
            item_id: str,
            body: RatingRequest,
            lang: str | None = None,
    ) -> RatingsResponse:
        """
        Add a user’s content rating by using the content’s identifier
        """
        method = "PUT"
        url = f"/v1/me/ratings/library-albums/{item_id}"
        req_map = {'params': {}}
        if lang is not None:
            req_map["params"]["l"] = lang
        
        req_map["body"] = body
        
        code, resp = self._api_request(endpoint=url, method=method, **req_map, user_token=user_token)
        result = {
            200: RatingsResponse,
            401: UnauthorizedResponse,
            403: ForbiddenResponse,
            500: ErrorsResponse,
            404: NotFoundResponse
        }[code](**resp)
        if code > 400:
            raise Exception(result)
        
        return result

    def set_ratings_library_music_video(
            self,
            user_token: str,
            item_id: str,
            body: RatingRequest,
            lang: str | None = None,
    ) -> RatingsResponse:
        """
        Add a user’s library music video rating by using the library
        music video’s identifier
        """
        method = "PUT"
        url = f"/v1/me/ratings/library-music-videos/{item_id}"
        req_map = {'params': {}}
        if lang is not None:
            req_map["params"]["l"] = lang
        
        req_map["body"] = body
        
        code, resp = self._api_request(endpoint=url, method=method, **req_map, user_token=user_token)
        result = {
            200: RatingsResponse,
            401: UnauthorizedResponse,
            403: ForbiddenResponse,
            500: ErrorsResponse,
            404: NotFoundResponse
        }[code](**resp)
        if code > 400:
            raise Exception(result)
        
        return result

    def set_ratings_library_playlist(
            self,
            user_token: str,
            item_id: str,
            body: RatingRequest,
            lang: str | None = None,
    ) -> RatingsResponse:
        """
        Add a user’s library playlist rating by using the library playlist’s
        identifier
        """
        method = "PUT"
        url = f"/v1/me/ratings/library-playlists/{item_id}"
        req_map = {'params': {}}
        if lang is not None:
            req_map["params"]["l"] = lang
        
        req_map["body"] = body
        
        code, resp = self._api_request(endpoint=url, method=method, **req_map, user_token=user_token)
        result = {
            200: RatingsResponse,
            401: UnauthorizedResponse,
            403: ForbiddenResponse,
            500: ErrorsResponse,
            404: NotFoundResponse
        }[code](**resp)
        if code > 400:
            raise Exception(result)
        
        return result

    def set_ratings_library_song(
            self,
            user_token: str,
            item_id: str,
            body: RatingRequest,
            lang: str | None = None,
    ) -> RatingsResponse:
        """
        Add a user’s library song rating by using the library song’s
        identifier
        """
        method = "PUT"
        url = f"/v1/me/ratings/library-songs/{item_id}"
        req_map = {'params': {}}
        if lang is not None:
            req_map["params"]["l"] = lang
        
        req_map["body"] = body
        
        code, resp = self._api_request(endpoint=url, method=method, **req_map, user_token=user_token)
        result = {
            200: RatingsResponse,
            401: UnauthorizedResponse,
            403: ForbiddenResponse,
            500: ErrorsResponse,
            404: NotFoundResponse
        }[code](**resp)
        if code > 400:
            raise Exception(result)
        
        return result

    def rm_ratings_library_album(
            self,
            user_token: str,
            item_id: str,
            lang: str | None = None,
    ) -> EmptyBodyResponse:
        """
        Remove a user’s content rating by using the content’s identifier
        """
        method = "DELETE"
        url = f"/v1/me/ratings/library-albums/{item_id}"
        req_map = {'params': {}}
        if lang is not None:
            req_map["params"]["l"] = lang
        
        code, resp = self._api_request(endpoint=url, method=method, **req_map, user_token=user_token)
        result = {
            204: EmptyBodyResponse,
            401: UnauthorizedResponse,
            403: ForbiddenResponse,
            500: ErrorsResponse,
            404: NotFoundResponse
        }[code](**resp)
        if code > 400:
            raise Exception(result)
        
        return result

    def rm_ratings_library_music_video(
            self,
            user_token: str,
            item_id: str,
            lang: str | None = None,
    ) -> EmptyBodyResponse:
        """
        Remove a user’s library music video rating by using the library
        music video’s identifier
        """
        method = "DELETE"
        url = f"/v1/me/ratings/library-music-videos/{item_id}"
        req_map = {'params': {}}
        if lang is not None:
            req_map["params"]["l"] = lang
        
        code, resp = self._api_request(endpoint=url, method=method, **req_map, user_token=user_token)
        result = {
            204: EmptyBodyResponse,
            401: UnauthorizedResponse,
            403: ForbiddenResponse,
            500: ErrorsResponse,
            404: NotFoundResponse
        }[code](**resp)
        if code > 400:
            raise Exception(result)
        
        return result

    def rm_ratings_library_playlist(
            self,
            user_token: str,
            item_id: str,
            lang: str | None = None,
    ) -> EmptyBodyResponse:
        """
        Remove a user’s library playlist rating by using the library
        playlist’s identifier
        """
        method = "DELETE"
        url = f"/v1/me/ratings/library-playlists/{item_id}"
        req_map = {'params': {}}
        if lang is not None:
            req_map["params"]["l"] = lang
        
        code, resp = self._api_request(endpoint=url, method=method, **req_map, user_token=user_token)
        result = {
            204: EmptyBodyResponse,
            401: UnauthorizedResponse,
            403: ForbiddenResponse,
            500: ErrorsResponse,
            404: NotFoundResponse
        }[code](**resp)
        if code > 400:
            raise Exception(result)
        
        return result

    def rm_ratings_library_song(
            self,
            user_token: str,
            item_id: str,
            lang: str | None = None,
    ) -> EmptyBodyResponse:
        """
        Remove a user’s library song rating by using the library song’s
        identifier
        """
        method = "DELETE"
        url = f"/v1/me/ratings/library-songs/{item_id}"
        req_map = {'params': {}}
        if lang is not None:
            req_map["params"]["l"] = lang
        
        code, resp = self._api_request(endpoint=url, method=method, **req_map, user_token=user_token)
        result = {
            204: EmptyBodyResponse,
            401: UnauthorizedResponse,
            403: ForbiddenResponse,
            500: ErrorsResponse,
            404: NotFoundResponse
        }[code](**resp)
        if code > 400:
            raise Exception(result)
        
        return result
