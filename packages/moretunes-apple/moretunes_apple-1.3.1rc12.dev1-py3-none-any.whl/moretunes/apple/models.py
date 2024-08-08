from __future__ import annotations
from pydantic import BaseModel, Field, RootModel
from typing import Literal, Dict


class ConfiguredBase(BaseModel):
    class Config:
        extra = 'allow'


class NotFoundResponse(ConfiguredBase):
    """Resource does not exist."""


class ViewMeta(BaseModel):
    """Information about the request or response."""


class ResourceMeta(BaseModel):
    """Information about the request or response."""


class ViewAttributes(BaseModel):
    """Attributes representing the metadata of the view."""


class PlayParameters(BaseModel):
    """An object that represents play parameters for resources."""
    id: str = Field(
        None, alias="id", description="The ID of the content to use for playback.")
    kind: str = Field(
        None, alias="kind", description="The kind of the content to use for playback.")


class RelationshipMeta(BaseModel):
    """Information about the request or response."""


class RatingsAttributes(BaseModel):
    """The attributes for a rating resource."""
    value: Literal['-1', '1'] | None = Field(
        None, alias="value", 
        description="""
        The value for the resource’s rating. The possible values for
        the value key are 1 and -1. If a value isn’t present, the content
        doesn’t have a rating
        """)


class EmptyBodyResponse(BaseModel):
    """A response object that contains no content."""


class ResourceAttributes(BaseModel):
    """Attributes representing the metadata of the resource."""


class UnauthorizedResponse(BaseModel):
    """
    A response object indicating that the request’s authorization
    is missing or invalid
    """


class StorefrontsAttributes(BaseModel):
    """The attributes for the storefronts resource."""
    default_language_tag: str = Field(
        None, alias="defaultLanguageTag", 
        description="""
        The default supported RFC4646 language tag for the storefront
        """)
    explicit_content_policy: Literal['allowed', 'opt-in', 'prohibited'] = Field(
        None, alias="explicitContentPolicy", 
        description="""
        Attribute indicating the level that this storefront can display
        explicit content
        """)
    name: str = Field(
        None, alias="name", description="The localized name of the storefront.")
    supported_language_tags: list[str] = Field(
        None, alias="supportedLanguageTags", description="The supported RFC4646 language tags for the storefront.")


class RatingRequestAttributes(BaseModel):
    """The attributes for a rating request object."""
    value: Literal['-1', '1'] = Field(
        None, alias="value", description="The value for the rating request.")


class StationGenresAttributes(BaseModel):
    """The attributes for the station genre resource."""
    name: str = Field(
        None, alias="name", description="The name of the station genre.")


class RelationshipResponseMeta(BaseModel):
    """Contextual data about the relationship."""


class LibraryArtistsAttributes(BaseModel):
    """The attributes for a library artist resource."""
    name: str = Field(
        None, alias="name", description="The artist’s name.")


class LangageTagResponseResults(BaseModel):
    """
    Results included in the response for a storefront resource request
    """
    tag: str = Field(
        None, alias="tag", description="The RFC4646 language tag for the request.")


class SearchHintsResponseResults(BaseModel):
    """
    An object that represents the autocomplete options for the hint
    """
    terms: list[str] = Field(
        None, alias="terms", description="The autocomplete options derived from the search hint.")


class RelationshipViewResponseMeta(BaseModel):
    """Contextual data about the view."""


class LibraryPlaylistTracksRequestData(BaseModel):
    """
    An object that represents a single track when added to a library
    playlist in a request
    """
    id: str = Field(
        None, alias="id", description="The unique identifier of the library playlist track.")
    type: Literal['library-music-videos', 'library-songs', 'music-videos', 'songs'] = Field(
        None, alias="type", 
        description="""
        The type of the track to be added. The possible values are library-music-videos,
        library-songs,  music-videos, or songs
        """)


class RelationshipViewResponseAttributes(BaseModel):
    """The attribute metadata for the view."""


class PersonalRecommendationAttributesTitle(BaseModel):
    """
    An object that represents the title of a personal recommendation
    """
    string_for_display: str = Field(
        None, alias="stringForDisplay", description="The localized title for the recommendation.")


class PersonalRecommendationAttributesReason(BaseModel):
    """
    An object that represents the reason for a personal recommendation
    """
    string_for_display: str = Field(
        None, alias="stringForDisplay", description="The localized reason for the recommendation.")


class ArtistsViewsArtistsSinglesViewAttributes(BaseModel):
    """
    Albums associated with the artist and categorized as singles
    """
    title: str = Field(
        None, alias="title", description="A localized title for this view.")


class AlbumsViewsAlbumsAppearsOnViewAttributes(BaseModel):
    """The attributes for the view."""
    title: str = Field(
        None, alias="title", description="A localized title to display for the view.")


class ArtistsViewsArtistsTopSongsViewAttributes(BaseModel):
    """
    Songs associated with the artist based on popularity in the current
    storefront
    """
    title: str = Field(
        None, alias="title", description="A localized title for this view.")


class ArtistsViewsArtistsLiveAlbumsViewAttributes(BaseModel):
    """
    Albums associated with the artist and categorized as live performances
    """
    title: str = Field(
        None, alias="title", description="A localized title for this view.")


class ArtistsViewsArtistsFullAlbumsViewAttributes(BaseModel):
    """Full-release albums associated with the artist."""
    title: str = Field(
        None, alias="title", description="A localized title for this view.")


class AlbumsViewsAlbumsRelatedVideosViewAttributes(BaseModel):
    """The attributes for the view."""
    title: str = Field(
        None, alias="title", description="A localized title to display for the view.")


class AlbumsViewsAlbumsRelatedAlbumsViewAttributes(BaseModel):
    """The attributes for the view."""
    title: str = Field(
        None, alias="title", description="A localized title to display for the view.")


class AlbumsViewsAlbumsOtherVersionsViewAttributes(BaseModel):
    """The attributes for the view."""
    title: str = Field(
        None, alias="title", description="A localized title to display for the view.")


class SearchSuggestionsResponseResultsTermSuggestion(BaseModel):
    """A suggested search term from a search suggestion response."""
    display_term: str = Field(
        None, alias="displayTerm", 
        description="""
        A potentially censored term to display to the user to select
        from. Use the searchTerm value for the actual search
        """)
    kind: Literal['terms'] = Field(
        None, alias="kind", description="The kind of suggestion.")
    search_term: str = Field(
        None, alias="searchTerm", 
        description="""
        The term to use as a search input when using this suggestion
        """)


class LibraryPlaylistsTracksRelationshipResponseMeta(BaseModel):
    """
    An object that represents the meta information for response to
    a library playlists tracks relationship request
    """


class LibraryPlaylistFolderCreationRequestAttributes(BaseModel):
    """
    The attributes for a library playlist folder creation request
    object
    """
    name: str = Field(
        None, alias="name", description="The name of the playlist folder of the creation request.")


class ArtistsViewsArtistsLatestReleaseViewAttributes(BaseModel):
    """
    The latest release for the artist determined to still be recent
    by the Apple Music Catalog
    """
    title: str = Field(
        None, alias="title", description="A localized title for this view.")


class ArtistsViewsArtistsTopMusicVideosViewAttributes(BaseModel):
    """Relevant music videos associated with the artist."""
    title: str = Field(
        None, alias="title", description="A localized title for this view.")


class ArtistsViewsArtistsSimilarArtistsViewAttributes(BaseModel):
    """Other artists similar to this artist."""
    title: str = Field(
        None, alias="title", description="A localized title for this view.")


class ArtistsViewsArtistsFeaturedAlbumsViewAttributes(BaseModel):
    """
    A collection of selected albums to be featured with the artist
    """
    title: str = Field(
        None, alias="title", description="A localized title for this view.")


class ArtistsViewsArtistsAppearsOnAlbumsViewAttributes(BaseModel):
    """
    Albums from other artists on which this artist appears or with
    which they’re associated
    """
    title: str = Field(
        None, alias="title", description="A localized title for this view.")


class PlaylistsViewsPlaylistsMoreByCuratorViewAttributes(BaseModel):
    """
    Attribute metadata for the view containing additional content
    by the same curator for this playlist
    """
    title: str = Field(
        None, alias="title", description="A localized title for this view.")


class ArtistsViewsArtistsFeaturedPlaylistsViewAttributes(BaseModel):
    """Relevant playlists associated with the artist."""
    title: str = Field(
        None, alias="title", description="A localized title for this view.")


class ArtistsViewsArtistsCompilationAlbumsViewAttributes(BaseModel):
    """
    Albums associated with the artist categorized as compilations
    """
    title: str = Field(
        None, alias="title", description="A localized title for this view.")


class PlaylistsViewsPlaylistsFeaturedArtistsViewAttributes(BaseModel):
    """Attribute metadata for the playlist featured artists view."""
    title: str = Field(
        None, alias="title", description="A localized title for this view")


class MusicVideosViewsMusicVideosMoreInGenreViewAttributes(BaseModel):
    """More music videos in a specific music video genre."""
    title: str = Field(
        None, alias="title", description="A localized title for this view.")


class ArtistsViewsArtistsFeaturedMusicVideosViewAttributes(BaseModel):
    """
    A collection of selected music videos to be featured with the
    artist
    """
    title: str = Field(
        None, alias="title", description="A localized title for this view.")


class LibraryPlaylistCreationRequestRelationshipsTracksData(BaseModel):
    """Data of the tracks too add to the created library playlist."""
    id: str = Field(
        None, alias="id", 
        description="""
        The unique identifier for the track. This ID can be a catalog
        identifier or a library identifier, depending on the track type
        """)
    type: Literal['library-music-videos', 'library-songs', 'music-videos', 'songs'] = Field(
        None, alias="type", description="The type of the track to be added.")


class LibraryPlaylistCreationRequestRelationshipsParentData(BaseModel):
    """
    Data of the library playlist folder which contains the created
    library playlist that the user creates
    """
    id: str = Field(
        None, alias="id", description="The unique identifier for the library playlist folder.")
    type: Literal['library-playlist-folders'] = Field(
        None, alias="type", description="The type of the track to be added.")


class MusicVideosViewsMusicVideosMoreByArtistViewAttributes(BaseModel):
    """More content of some other type by the artist."""
    title: str = Field(
        None, alias="title", description="A localized title for this view.")


class RecordLabelsViewsRecordLabelsTopReleasesViewAttributes(BaseModel):
    """The attributes for the record label top releases view."""
    title: str = Field(
        None, alias="title", description="A localized title to display for the view.")


class RecordLabelsViewsRecordLabelsLatestReleasesViewAttributes(BaseModel):
    """The attributes for the record label latest releases view."""
    title: str = Field(
        None, alias="title", description="A localized title to display for the view.")


class LibraryPlaylistFolderCreationRequestRelationshipsParentData(BaseModel):
    """
    Data of the parent of the library playlist folder of the creation
    request
    """
    id: str = Field(
        None, alias="id", 
        description="""
        The unique identifier for the parent folder of the library playlist
        folder of the creation request
        """)
    type: Literal['library-playlist-folders'] = Field(
        None, alias="type", 
        description="""
        The type of the parent folder of the library playlist folder
        of the creation request
        """)


class RatingRequest(BaseModel):
    """A request containing the data for a rating."""
    attributes: RatingRequestAttributes = Field(
        None, alias="attributes", 
        description="""
        The dictionary that includes the value for the resource’s rating.
        """)
    type: Literal['ratings'] = Field(
        None, alias="type", description="The type of the payload.")


class LangageTagResponse(BaseModel):
    """The response to a language tag request."""
    results: LangageTagResponseResults = Field(
        None, alias="results", 
        description="""
        The results included in the response for a language tag resource
        request
        """)


class SearchHintsResponse(BaseModel):
    """The response to a request for search hints."""
    results: SearchHintsResponseResults = Field(
        None, alias="results", 
        description="""
        The results included in the response to a request for search
        hints
        """)


class LibraryPlaylistTracksRequest(BaseModel):
    """A request to add tracks to a library playlist."""
    data: list[LibraryPlaylistTracksRequestData] = Field(
        None, alias="data", 
        description="""
        A list of dictionaries with information about the tracks to add
        """)


class LibraryPlaylistCreationRequestRelationshipsTracks(BaseModel):
    """
    The songs and music videos to add to the created playlist’s tracklist
    """
    data: list[LibraryPlaylistCreationRequestRelationshipsTracksData] = Field(
        None, alias="data", 
        description="""
        A dictionary that includes strings for the identifier and type
        of the new playlist
        """)


class LibraryPlaylistCreationRequestRelationshipsParent(BaseModel):
    """
    Library playlist folder which contains the playlist that the
    user creates
    """
    data: list[LibraryPlaylistCreationRequestRelationshipsParentData] = Field(
        None, alias="data", 
        description="""
        A dictionary that includes strings for the identifier and type
        of the library playlist folder
        """)


class LibraryPlaylistFolderCreationRequestRelationshipsParent(BaseModel):
    """The parent of the playlist folder of the creation request."""
    data: list[LibraryPlaylistFolderCreationRequestRelationshipsParentData] = Field(
        None, alias="data", 
        description="""
        The data of the parent of the library playlist folder of the
        creation request
        """)


class LibraryPlaylistCreationRequestRelationships(BaseModel):
    """
    The relationships for a library playlist creation request object
    """
    tracks: LibraryPlaylistCreationRequestRelationshipsTracks = Field(
        None, alias="tracks", 
        description="""
        The songs and music videos the user adds to the playlist for
        the creation request.
        """)
    parent: LibraryPlaylistCreationRequestRelationshipsParent = Field(
        None, alias="parent", 
        description="""
        The library playlist folder which contains the created playlist
        """)


class LibraryPlaylistFolderCreationRequestRelationships(BaseModel):
    """
    The relationships of the library playlist folder of the creation
    request
    """
    parent: LibraryPlaylistFolderCreationRequestRelationshipsParent = Field(
        None, alias="parent", description="The parent of the playlist folder of the creation request.")


class View(BaseModel):
    """
    A to-one or to-many relationship view from one resource object
    to others representing interesting associations
    """
    href: str | None = Field(
        None, alias="href", 
        description="""
        A URL subpath that fetches the view resources and attributes
        as the primary objects. This member is only present in responses
        """)
    next: str | None = Field(
        None, alias="next", 
        description="""
        Link to the next page of resources in the view. Contains the
        offset query parameter that specifies the next page. See Fetch
        Resources by Page
        """)
    attributes: ViewAttributes | None = Field(
        None, alias="attributes", description="Attributes specific to the view.")
    data: list[Resource] = Field(
        None, alias="data", description="One or more destination objects.")
    meta: ViewMeta | None = Field(
        None, alias="meta", 
        description="""
        Contextual information about the view for the request or response
        """)


class Songs(BaseModel):
    """A resource object that represents a song."""
    id: str = Field(
        None, alias="id", description="The identifier for the song.")
    type: Literal['songs'] = Field(
        None, alias="type", description="This value is always songs.")
    href: str = Field(
        None, alias="href", description="The relative location for the song resource.")
    attributes: SongsAttributes | None = Field(
        None, alias="attributes", description="The attributes for the song.")
    relationships: SongsRelationships | None = Field(
        None, alias="relationships", description="The relationships for the song.")


class SongsResponse(BaseModel):
    """The response to a songs request."""
    data: list[Songs] = Field(
        None, alias="data", description="The Songs included in the response for the request.")


class Error(BaseModel):
    """
    Information about an error that occurred while processing a request
    """
    code: str = Field(
        None, alias="code", 
        description="""
        The code for this error. For possible values, see HTTP Status
        Codes
        """)
    detail: str | None = Field(
        None, alias="detail", description="A long, possibly localized, description of the problem.")
    id: str = Field(
        None, alias="id", description="A unique identifier for this occurrence of the error.")
    source: ErrorSource | None = Field(
        None, alias="source", 
        description="""
        An object containing references to the source of the error. For
        possible members, see Source object
        """)
    status: str = Field(
        None, alias="status", description="The HTTP status code for this problem.")
    title: str = Field(
        None, alias="title", description="A short, possibly localized, description of the problem.")


class ErrorsResponse(BaseModel):
    """
    A response object indicating that an error occurred while processing
    the request
    """
    errors: list[Error] = Field(
        None, alias="errors", 
        description="""
        The collection of errors that occurred while processing the request
        """)


class ForbiddenResponse(BaseModel):
    """
    A response object indicating that the request wasn’t accepted
    due to an issue with the authentication
    """
    errors: list[Error] = Field(
        None, alias="errors", 
        description="""
        The collection of errors that occurred while processing the request
        """)


class Genres(BaseModel):
    """A resource object that represents a music genre."""
    id: str = Field(
        None, alias="id", description="The identifier for the genre.")
    type: Literal['genres'] = Field(
        None, alias="type", description="This value must always be genres.")
    href: str = Field(
        None, alias="href", description="The relative location for the genre resource.")
    attributes: GenresAttributes | None = Field(
        None, alias="attributes", description="The attributes for the genre.")


class GenresResponse(BaseModel):
    """The response to a genres request."""
    data: list[Genres] = Field(
        None, alias="data", description="The Genres included in the response for the request.")


class Albums(BaseModel):
    """A resource object that represents an album."""
    id: str = Field(
        None, alias="id", description="The identifier for the album.")
    type: Literal['albums'] = Field(
        None, alias="type", description="This value is always albums.")
    href: str = Field(
        None, alias="href", description="The relative location for the album resource.")
    attributes: AlbumsAttributes | None = Field(
        None, alias="attributes", description="The attributes for the album.")
    relationships: AlbumsRelationships | None = Field(
        None, alias="relationships", description="The relationships for the album.")
    views: AlbumsViews | None = Field(
        None, alias="views", description="The relationship views for the album.")


class AlbumsResponse(BaseModel):
    """The response to an albums request."""
    data: list[Albums] = Field(
        None, alias="data", description="The Albums included in the response for the request.")


class Preview(BaseModel):
    """An object that represents a preview for resources."""
    artwork: Artwork | None = Field(
        None, alias="artwork", description="The preview artwork for the associated preview music video.")
    url: str = Field(
        None, alias="url", description="The preview URL for the content.")
    hls_url: str | None = Field(
        None, alias="hlsUrl", description="The HLS preview URL for the content.")


class Artwork(BaseModel):
    """An object that represents artwork."""
    bg_color: str | None = Field(
        None, alias="bgColor", description="The average background color of the image.")
    height: int | None = Field(
        None, alias="height", description="The maximum height available for the image.")
    width: int | None = Field(
        None, alias="width", description="The maximum width available for the image.")
    text_color_1: str | None = Field(
        None, alias="textColor1", 
        description="""
        The primary text color used if the background color gets displayed
        """)
    text_color_2: str | None = Field(
        None, alias="textColor2", 
        description="""
        The secondary text color used if the background color gets displayed
        """)
    text_color_3: str | None = Field(
        None, alias="textColor3", 
        description="""
        The tertiary text color used if the background color gets displayed
        """)
    text_color_4: str | None = Field(
        None, alias="textColor4", 
        description="""
        The final post-tertiary text color used if the background color
        gets displayed
        """)
    url: str = Field(
        None, alias="url", 
        description="""
        The URL to request the image asset. {w}x{h}must precede image
        filename, as placeholders for the width and height values as
        described above. For example, {w}x{h}bb.jpeg)
        """)


class Ratings(BaseModel):
    """An object that represents a rating for a resource."""
    id: str = Field(
        None, alias="id", description="The identifier for the rating.")
    type: Literal['ratings'] = Field(
        None, alias="type", description="This value is always ratings.")
    href: str = Field(
        None, alias="href", description="The relative location for the playlist resource.")
    attributes: RatingsAttributes | None = Field(
        None, alias="attributes", description="The attributes for the rating.")
    relationships: RatingsRelationships | None = Field(
        None, alias="relationships", description="The relationships from ratings to other resources.")


class RatingsResponse(BaseModel):
    """The response to a request for a rating."""
    data: list[Ratings] = Field(
        None, alias="data", description="The Ratings included in the response for the request.")


class Artists(BaseModel):
    """
    A resource object that represents the artist of an album where
    an artist can be one or more people
    """
    id: str = Field(
        None, alias="id", description="The identifier for the artist.")
    type: Literal['artists'] = Field(
        None, alias="type", description="This value is always artists.")
    href: str = Field(
        None, alias="href", description="The relative location for the artist resource.")
    attributes: ArtistsAttributes | None = Field(
        None, alias="attributes", description="The attributes for the artist.")
    relationships: ArtistsRelationships | None = Field(
        None, alias="relationships", description="The relationships for the artist.")
    views: ArtistsViews | None = Field(
        None, alias="views", 
        description="""
        The views for associations between artists and other resources
        """)


class ArtistsResponse(BaseModel):
    """The response to an artists request."""
    data: list[Artists] = Field(
        None, alias="data", description="The Artists included in the response for the request.")


class Curators(BaseModel):
    """A resource object that represents a curator."""
    id: str = Field(
        None, alias="id", description="The identifier for the curator.")
    type: Literal['curators'] = Field(
        None, alias="type", description="This value must always be curators.")
    href: str = Field(
        None, alias="href", description="The relative location for the curator resource.")
    attributes: CuratorsAttributes | None = Field(
        None, alias="attributes", description="The attributes for the curator.")
    relationships: CuratorsRelationships | None = Field(
        None, alias="relationships", description="The relationships for the curator.")


class CuratorsResponse(BaseModel):
    """The response to a request for curators."""
    data: list[Curators] = Field(
        None, alias="data", description="The Curators included in the response for the request.")


class Stations(BaseModel):
    """A resource object that represents a station."""
    id: str = Field(
        None, alias="id", description="The identifier for the station.")
    type: Literal['stations'] = Field(
        None, alias="type", description="This value must always be stations.")
    href: str = Field(
        None, alias="href", description="The relative location for the station resource.")
    attributes: StationsAttributes | None = Field(
        None, alias="attributes", description="The attributes for the station.")
    relationships: StationsRelationships | None = Field(
        None, alias="relationships", description="The relationships for the station.")


class StationsResponse(BaseModel):
    """The response to a stations request."""
    data: list[Stations] = Field(
        None, alias="data", description="The Stations included in the response for the request.")


class Resource(BaseModel):
    """A resource—such as an album, song, or playlist."""
    id: str = Field(
        None, alias="id", description="Persistent identifier of the resource. ")
    type: str = Field(
        None, alias="type", description="The type of resource. ")
    href: str | None = Field(
        None, alias="href", 
        description="""
        A URL subpath that fetches the resource as the primary object.
        This member is only present in responses
        """)
    attributes: ResourceAttributes | None = Field(
        None, alias="attributes", 
        description="""
        Attributes belonging to the resource (can be a subset of the
        attributes). The members are the names of the attributes defined
        in the object model
        """)
    relationships: ResourceRelationships | None = Field(
        None, alias="relationships", 
        description="""
        Relationships belonging to the resource (can be a subset of the
        relationships). The members are the names of the relationships
        defined in the object model. See Relationship object for the
        values of the members
        """)
    meta: ResourceMeta | None = Field(
        None, alias="meta", 
        description="""
        Information about the request or response. The members may be
        any of the endpoint parameters
        """)
    views: ResourceViews | None = Field(
        None, alias="views", description="The relationship views for the resource.")


class ResourceCollectionResponse(BaseModel):
    """
    A response object composed of resource objects for the request
    """
    data: list[Resource] = Field(
        None, alias="data", description="The collection of resources for the request.")


class Playlists(BaseModel):
    """A resource object that represents a playlist."""
    id: str = Field(
        None, alias="id", description="The identifier for the playlist.")
    type: Literal['playlists'] = Field(
        None, alias="type", description="This value is always playlists.")
    href: str = Field(
        None, alias="href", description="The relative location for the playlist resource.")
    attributes: PlaylistsAttributes | None = Field(
        None, alias="attributes", description="The attributes for the playlist.")
    relationships: PlaylistsRelationships | None = Field(
        None, alias="relationships", description="The relationships for the playlist.")
    views: PlaylistsViews | None = Field(
        None, alias="views", 
        description="""
        The views for associations between playlists and other resources
        """)


class PlaylistsResponse(BaseModel):
    """The response to a playlists request."""
    data: list[Playlists] = Field(
        None, alias="data", description="The Playlists included in the response for the request.")


class Activities(BaseModel):
    """A resource object that represents an activity curator."""
    id: str = Field(
        None, alias="id", description="The identifier for the activity.")
    type: Literal['activities'] = Field(
        None, alias="type", description="This value must always be activities.")
    href: str = Field(
        None, alias="href", description="The relative location for the activity resource.")
    attributes: ActivitiesAttributes | None = Field(
        None, alias="attributes", description="The attributes for the activity.")
    relationships: ActivitiesRelationships | None = Field(
        None, alias="relationships", description="The relationships for the activity.")


class ActivitiesResponse(BaseModel):
    """The response to a request for activities."""
    data: list[Activities] = Field(
        None, alias="data", description="The Activities included in the response for the request.")


class MusicVideos(BaseModel):
    """A resource object that represents a music video."""
    id: str = Field(
        None, alias="id", description="The identifier for the music video.")
    type: Literal['music-videos'] = Field(
        None, alias="type", description="This value is always music-videos.")
    href: str = Field(
        None, alias="href", description="The relative location for the music video resource.")
    attributes: MusicVideosAttributes | None = Field(
        None, alias="attributes", description="The attributes for the music video.")
    relationships: MusicVideosRelationships | None = Field(
        None, alias="relationships", description="The relationships for the music video.")
    views: MusicVideosViews | None = Field(
        None, alias="views", description="The relationship views for the music video.")


class MusicVideosResponse(BaseModel):
    """The response to a music videos request."""
    data: list[MusicVideos] = Field(
        None, alias="data", description="The MusicVideos included in the response for the request.")


class AlbumsViews(BaseModel):
    """The relationship views for an album resource."""
    appears_on: AlbumsViewsAlbumsAppearsOnView | None = Field(
        None, alias="appears-on", 
        description="""
        A selection of playlists that tracks from this album appear on
        """)
    other_versions: AlbumsViewsAlbumsOtherVersionsView | None = Field(
        None, alias="other-versions", description="Other versions of this album.")
    related_albums: AlbumsViewsAlbumsRelatedAlbumsView | None = Field(
        None, alias="related-albums", description="Other albums related or similar to this album.")
    related_videos: AlbumsViewsAlbumsRelatedVideosView | None = Field(
        None, alias="related-videos", description="Music videos associated with tracks on this album.")


class ErrorSource(BaseModel):
    """The Source object represents the source of an error."""
    parameter: str | None = Field(
        None, alias="parameter", description="The URI query parameter that caused the error.")
    pointer: str | None = Field(
        None, alias="pointer", description="A pointer to the associated entry in the request document.")


class Storefronts(BaseModel):
    """
    A resource object that represents a storefront, an Apple Music
    and iTunes Store territory that the content is available in
    """
    id: str = Field(
        None, alias="id", description="The identifier for the storefront.")
    type: Literal['storefronts'] = Field(
        None, alias="type", description="This value must always be storefronts.")
    href: str = Field(
        None, alias="href", description="The relative location for the storefront resource.")
    attributes: StorefrontsAttributes | None = Field(
        None, alias="attributes", description="The attributes for the storefront.")


class StorefrontsResponse(BaseModel):
    """The response to a storefront request."""
    data: list[Storefronts] = Field(
        None, alias="data", 
        description="""
        The data included in the response for a storefront resource request
        """)


class RecordLabels(BaseModel):
    """A resource object that represents a record label."""
    id: str = Field(
        None, alias="id", description="The identifier for the record label.")
    type: Literal['record-labels'] = Field(
        None, alias="type", description="This value must always be record-labels.")
    href: str = Field(
        None, alias="href", description="A relative location for the record label resource.")
    attributes: RecordLabelsAttributes | None = Field(
        None, alias="attributes", description="The attributes of the record label.")
    views: RecordLabelsViews | None = Field(
        None, alias="views", description="The relationship views for the record label.")


class RecordLabelsResponse(BaseModel):
    """The response to a request for record labels."""
    data: list[RecordLabels] = Field(
        None, alias="data", description="The collection of record labels for the request.")


class LibrarySongs(BaseModel):
    """A resource object that represents a library song."""
    id: str = Field(
        None, alias="id", description="The identifier for the library song.")
    type: Literal['library-songs'] = Field(
        None, alias="type", description="This value is always library-songs.")
    href: str = Field(
        None, alias="href", description="The relative location for the library song resource.")
    attributes: LibrarySongsAttributes | None = Field(
        None, alias="attributes", description="The attributes for the library song.")
    relationships: LibrarySongsRelationships | None = Field(
        None, alias="relationships", description="The relationships for the library song.")


class LibrarySongsResponse(BaseModel):
    """The response to a library songs request."""
    data: list[LibrarySongs] = Field(
        None, alias="data", description="The LibrarySongs included in the response for the request.")


class ArtistsViews(BaseModel):
    """
    The views for associations between artists and other resources
    """
    appears_on_albums: ArtistsViewsArtistsAppearsOnAlbumsView | None = Field(
        None, alias="appears-on-albums", 
        description="""
        A selection of albums from other artists this artist appears
        on
        """)
    compilation_albums: ArtistsViewsArtistsCompilationAlbumsView | None = Field(
        None, alias="compilation-albums", 
        description="""
        Albums associated with the artist categorized as “compilations.
        """)
    featured_albums: ArtistsViewsArtistsFeaturedAlbumsView | None = Field(
        None, alias="featured-albums", description="A collection of albums selected as featured for the artist.")
    featured_music_videos: ArtistsViewsArtistsFeaturedMusicVideosView | None = Field(
        None, alias="featured-music-videos", 
        description="""
        A collection of music videos selected as featured for the artist
        """)
    featured_playlists: ArtistsViewsArtistsFeaturedPlaylistsView | None = Field(
        None, alias="featured-playlists", description="Relevant playlists associated with the artist.")
    full_albums: ArtistsViewsArtistsFullAlbumsView | None = Field(
        None, alias="full-albums", description="Full-release albums associated with the artist.")
    latest_release: ArtistsViewsArtistsLatestReleaseView | None = Field(
        None, alias="latest-release", 
        description="""
        The latest release for the artist deemed to still be recent
        """)
    live_albums: ArtistsViewsArtistsLiveAlbumsView | None = Field(
        None, alias="live-albums", 
        description="""
        Albums associated with the artist categorized as live performances
        """)
    similar_artists: ArtistsViewsArtistsSimilarArtistsView | None = Field(
        None, alias="similar-artists", description="Other artists similar to this artist.")
    singles: ArtistsViewsArtistsSinglesView | None = Field(
        None, alias="singles", description="Albums associated with the artist categorized as “singles.”")
    top_music_videos: ArtistsViewsArtistsTopMusicVideosView | None = Field(
        None, alias="top-music-videos", description="Relevant music videos associated with the artist.")
    top_songs: ArtistsViewsArtistsTopSongsView | None = Field(
        None, alias="top-songs", 
        description="""
        Songs associated with the artist based on popularity in the current
        storefront
        """)


class Relationship(BaseModel):
    """
    A to-one or to-many relationship from one resource object to
    others
    """
    href: str | None = Field(
        None, alias="href", 
        description="""
        A URL subpath that fetches the relationship resources as the
        primary object. This member is only present in responses
        """)
    next: str | None = Field(
        None, alias="next", 
        description="""
        Link to the next page of resources in the relationship. Contains
        the offset query parameter that specifies the next page. See
        Fetch Resources by Page
        """)
    data: list[Resource] = Field(
        None, alias="data", description="One or more destination objects.")
    meta: RelationshipMeta | None = Field(
        None, alias="meta", 
        description="""
        Contextual information about the relationship for the request
        or response
        """)


class AppleCurators(BaseModel):
    """A resource object that represents an Apple curator."""
    id: str = Field(
        None, alias="id", description="The identifier for the Apple curator.")
    type: Literal['apple-curators'] = Field(
        None, alias="type", description="This value must always be apple-curators.")
    href: str = Field(
        None, alias="href", description="The relative location for the Apple curator resource.")
    attributes: AppleCuratorsAttributes | None = Field(
        None, alias="attributes", description="The attributes for the Apple curator.")
    relationships: AppleCuratorsRelationships | None = Field(
        None, alias="relationships", description="The relationships for the Apple curator.")


class AppleCuratorsResponse(BaseModel):
    """The response to a request for Apple curators."""
    data: list[AppleCurators] = Field(
        None, alias="data", description="The AppleCurators included in the response for the request.")


class SearchResponseResultsTopResultsSearchResult(BaseModel):
    """An object containing a top results’ search result."""
    data: list[Activities | Albums | AppleCurators | Artists | Curators | MusicVideos | Playlists | RecordLabels | Songs | Stations] = Field(
        None, alias="data", description="The resources for the search result.")


class SearchSuggestionsResponseResultsTopResultSuggestion(BaseModel):
    """A suggested popular result for similar search prefix terms."""
    content: Activities | Albums | AppleCurators | Artists | Curators | MusicVideos | Playlists | RecordLabels | Songs | Stations = Field(
        None, alias="content", description="The actual resource for the suggested content.")
    kind: Literal['topResults'] = Field(
        None, alias="kind", description="The kind of suggestion.")


class SearchSuggestionsResponseResults(BaseModel):
    """
    An object that represents the results of a search suggestions
    query
    """
    suggestions: list[SearchSuggestionsResponseResultsTermSuggestion | SearchSuggestionsResponseResultsTopResultSuggestion] = Field(
        None, alias="suggestions", 
        description="""
        An array of possible valid search queries determined from the
        search suggestion
        """)


class SearchSuggestionsResponse(BaseModel):
    """The response to a request for search suggestions."""
    results: SearchSuggestionsResponseResults = Field(
        None, alias="results", 
        description="""
        The results included in the response to a request for search
        suggestions
        """)


class ChartResponse(BaseModel):
    """The response to a request for a chart."""
    results: ChartResponseResults = Field(
        None, alias="results", description="A mapping of a requested type to an array of charts.")


class StationGenres(BaseModel):
    """A resource object that represents a station genre."""
    id: str = Field(
        None, alias="id", description="The identifier for the station genre.")
    type: Literal['station-genres'] = Field(
        None, alias="type", description="This value must always be station-genres.")
    href: str = Field(
        None, alias="href", description="The relative location for the station genre resource.")
    attributes: StationGenresAttributes | None = Field(
        None, alias="attributes", description="The attributes for the station genre.")
    relationships: StationGenresRelationships | None = Field(
        None, alias="relationships", description="The relationships for the station genre.")


class StationGenresResponse(BaseModel):
    """The response to a specific station genres resource request."""
    data: list[StationGenres] = Field(
        None, alias="data", description="The StationGenres included in the response for the request.")


class LibraryAlbums(BaseModel):
    """A resource object that represents a library album."""
    id: str = Field(
        None, alias="id", description="The identifier for the library album.")
    type: Literal['library-albums'] = Field(
        None, alias="type", description="This value is always library-albums.")
    href: str = Field(
        None, alias="href", description="The relative location for the library album resource.")
    attributes: LibraryAlbumsAttributes | None = Field(
        None, alias="attributes", description="The attributes for the library album.")
    relationships: LibraryAlbumsRelationships | None = Field(
        None, alias="relationships", description="The relationships for the library album.")


class LibraryAlbumsResponse(BaseModel):
    """The response to a library albums request."""
    data: list[LibraryAlbums] = Field(
        None, alias="data", description="The LibraryAlbums included in the request.")


class ResourceViews(RootModel):
    """Views belonging to the resource."""
    root: Dict[str, View | None] = Field(
        None, 
        description="""
        A named relationship view for the resource creating an association
        from the resource to other resources
        """)


class EditorialNotes(BaseModel):
    """An object that represents a notes attribute."""
    short: str | None = Field(
        None, alias="short", 
        description="""
        Abbreviated notes shown inline or when the content appears alongside
        other content
        """)
    standard: str | None = Field(
        None, alias="standard", description="Notes shown when the content is prominently displayed.")
    name: str | None = Field(
        None, alias="name", description="Name for the editorial notes.")
    tagline: str | None = Field(
        None, alias="tagline", description="The tag line for the editorial notes.")


class SearchResponse(BaseModel):
    """The response to a search request."""
    results: SearchResponseResults = Field(
        None, alias="results", description="The results included in the response to a search request.")


class PlaylistsViews(BaseModel):
    """The views for a music video resource."""
    featured_artists: PlaylistsViewsPlaylistsFeaturedArtistsView | None = Field(
        None, alias="featured-artists", description="Artists that are featured on this playlist.")
    more_by_curator: PlaylistsViewsPlaylistsMoreByCuratorView | None = Field(
        None, alias="more-by-curator", description="Additional content by the same curator for this playlist.")


class LibraryArtists(BaseModel):
    """
    A resource object that represents an artist present in a user’s
    library
    """
    id: str = Field(
        None, alias="id", description="The identifier for the library artist.")
    type: Literal['library-artists'] = Field(
        None, alias="type", description="This value is always library-artists.")
    href: str = Field(
        None, alias="href", description="The relative location for the library artist resource.")
    attributes: LibraryArtistsAttributes | None = Field(
        None, alias="attributes", description="The attributes for the library artist. ")
    relationships: LibraryArtistsRelationships | None = Field(
        None, alias="relationships", description="The relationships for the library artist.")


class LibraryArtistsResponse(BaseModel):
    """The response to a library artists request."""
    data: list[LibraryArtists] = Field(
        None, alias="data", 
        description="""
        The LibraryArtists included in the response for the request
        """)


class SongsAttributes(BaseModel):
    """The attributes for a song resource."""
    album_name: str = Field(
        None, alias="albumName", description="The name of the album the song appears on.")
    artist_name: str = Field(
        None, alias="artistName", description="The artist’s name.")
    artist_url: str | None = Field(
        None, alias="artistUrl", description="(Extended) The URL of the artist for the content.")
    artwork: Artwork = Field(
        None, alias="artwork", description="The album artwork.")
    attribution: str | None = Field(
        None, alias="attribution", 
        description="""
        (Classical music only) The name of the artist or composer to
        attribute the song with
        """)
    audio_variants: list[Literal['dolby-atmos', 'dolby-audio', 'hi-res-lossless', 'lossless', 'lossy-stereo']] | None = Field(
        None, alias="audioVariants", description="(Extended) Indicates the specific audio variant for a song.")
    composer_name: str | None = Field(
        None, alias="composerName", description="The song’s composer.")
    content_rating: Literal['clean', 'explicit'] | None = Field(
        None, alias="contentRating", 
        description="""
        The Recording Industry Association of America (RIAA) rating of
        the content. No value means no rating
        """)
    disc_number: int | None = Field(
        None, alias="discNumber", description="The disc number of the album the song appears on.")
    duration_in_millis: int = Field(
        None, alias="durationInMillis", description="The duration of the song in milliseconds.")
    editorial_notes: EditorialNotes | None = Field(
        None, alias="editorialNotes", 
        description="""
        The notes about the song that appear in the Apple Music catalog
        """)
    genre_names: list[str] = Field(
        None, alias="genreNames", description="The genre names the song is associated with.")
    has_lyrics: bool = Field(
        None, alias="hasLyrics", 
        description="""
        Indicates whether the song has lyrics available in the Apple
        Music catalog. If true, the song has lyrics available; otherwise,
        it doesn't
        """)
    is_apple_digital_master: bool = Field(
        None, alias="isAppleDigitalMaster", 
        description="""
        Indicates whether the response delivered the song as an Apple
        Digital Master
        """)
    isrc: str | None = Field(
        None, alias="isrc", 
        description="""
        The International Standard Recording Code (ISRC) for the song
        """)
    movement_count: int | None = Field(
        None, alias="movementCount", description="(Classical music only) The movement count of the song.")
    movement_name: str | None = Field(
        None, alias="movementName", description="(Classical music only) The movement name of the song.")
    movement_number: int | None = Field(
        None, alias="movementNumber", description="(Classical music only) The movement number of the song.")
    name: str = Field(
        None, alias="name", description="The localized name of the song.")
    play_params: PlayParameters | None = Field(
        None, alias="playParams", 
        description="""
        When present, this attribute indicates that the song is available
        to play with an Apple Music subscription. The value map may be
        used to initiate playback. Previews of the song audio may be
        available with or without an Apple Music subscription
        """)
    previews: list[Preview] = Field(
        None, alias="previews", description="The preview assets for the song.")
    release_date: str | None = Field(
        None, alias="releaseDate", 
        description="""
        The release date of the song, when known, in YYYY-MM-DD or YYYY
        format. Prerelease songs may have an expected release date in
        the future
        """)
    track_number: int | None = Field(
        None, alias="trackNumber", description="The number of the song in the album’s track list.")
    url: str = Field(
        None, alias="url", description="The URL for sharing the song in Apple Music. ")
    work_name: str | None = Field(
        None, alias="workName", description="(Classical music only) The name of the associated work.")


class GenresAttributes(BaseModel):
    """The attributes for a genre resource."""
    name: str = Field(
        None, alias="name", description="The localized name of the genre.")
    parent_id: str | None = Field(
        None, alias="parentId", description="The identifier of the parent for the genre.")
    parent_name: str | None = Field(
        None, alias="parentName", description="The localized name of the parent genre.")
    chart_label: str | None = Field(
        None, alias="chartLabel", 
        description="""
        (Extended) A localized string to use when displaying the genre
        in relation to charts
        """)


class LibraryPlaylists(BaseModel):
    """A resource object that represents a library playlist."""
    id: str = Field(
        None, alias="id", description="The identifier for the library playlist.")
    type: Literal['library-playlists'] = Field(
        None, alias="type", description="This value is always library-playlists.")
    href: str = Field(
        None, alias="href", description="The relative location for the library playlist resource.")
    attributes: LibraryPlaylistsAttributes | None = Field(
        None, alias="attributes", description="The attributes for the library playlist. ")
    relationships: LibraryPlaylistsRelationships | None = Field(
        None, alias="relationships", description="The relationships for the library playlist.")


class LibraryPlaylistsResponse(BaseModel):
    """The response to a library playlists request."""
    data: list[LibraryPlaylists] = Field(
        None, alias="data", 
        description="""
        The LibraryPlaylists included in the response for the request
        """)


class MusicVideosViews(BaseModel):
    """The views for a music video resource."""
    more_by_artist: MusicVideosViewsMusicVideosMoreByArtistView | None = Field(
        None, alias="more-by-artist", description="More music videos of some type by the artist.")
    more_in_genre: MusicVideosViewsMusicVideosMoreInGenreView | None = Field(
        None, alias="more-in-genre", description="More music videos in the given music video genre.")


class AlbumsAttributes(BaseModel):
    """The attributes for an album resource."""
    artist_name: str = Field(
        None, alias="artistName", description="The name of the primary artist associated with the album.")
    artist_url: str | None = Field(
        None, alias="artistUrl", description="(Extended) The URL of the artist for this content.")
    artwork: Artwork = Field(
        None, alias="artwork", description="The artwork for the album.")
    audio_variants: list[Literal['dolby-atmos', 'dolby-audio', 'hi-res-lossless', 'lossless', 'lossy-stereo']] | None = Field(
        None, alias="audioVariants", 
        description="""
        (Extended) Indicates the specific audio variant for the album.
        """)
    content_rating: Literal['clean', 'explicit'] | None = Field(
        None, alias="contentRating", 
        description="""
        The Recording Industry Association of America (RIAA) rating of
        the content. No value means no rating
        """)
    copyright: str | None = Field(
        None, alias="copyright", description="The copyright text.")
    editorial_notes: EditorialNotes | None = Field(
        None, alias="editorialNotes", description="The notes about the album that appear in the iTunes Store.")
    genre_names: list[str] = Field(
        None, alias="genreNames", description="The names of the genres associated with the album.")
    is_compilation: bool = Field(
        None, alias="isCompilation", 
        description="""
        Indicates whether the album is marked as a compilation. If true,
        the album is a compilation; otherwise, it's not
        """)
    is_complete: bool = Field(
        None, alias="isComplete", 
        description="""
        Indicates whether the album is complete. If true, the album is
        complete; otherwise, it's not. An album is complete if it contains
        all its tracks and songs
        """)
    is_mastered_for_itunes: bool = Field(
        None, alias="isMasteredForItunes", 
        description="""
        Indicates whether the response delivered the album as an Apple
        Digital Master
        """)
    is_single: bool = Field(
        None, alias="isSingle", description="Indicates whether the album contains a single song.")
    name: str = Field(
        None, alias="name", description="The localized name of the album.")
    play_params: PlayParameters | None = Field(
        None, alias="playParams", 
        description="""
        When present, this attribute indicates that one or more tracks
        on the album are available to play with an Apple Music subscription.
        The value map may be used to initiate playback of available tracks
        on the album
        """)
    record_label: str | None = Field(
        None, alias="recordLabel", description="The name of the record label for the album.")
    release_date: str | None = Field(
        None, alias="releaseDate", 
        description="""
        The release date of the album, when known, in YYYY-MM-DD or YYYY
        format. Prerelease content may have an expected release date
        in the future
        """)
    track_count: int = Field(
        None, alias="trackCount", description="The number of tracks for the album.")
    upc: str | None = Field(
        None, alias="upc", description="The Universal Product Code for the album.")
    url: str = Field(
        None, alias="url", description="The URL for sharing the album in Apple Music.")


class RecordLabelsViews(BaseModel):
    """The relationship views for a record label resource."""
    latest_releases: RecordLabelsViewsRecordLabelsLatestReleasesView | None = Field(
        None, alias="latest-releases", description="The latest releases for the record label.")
    top_releases: RecordLabelsViewsRecordLabelsTopReleasesView | None = Field(
        None, alias="top-releases", description="The top releases for the record label.")


class ArtistsAttributes(BaseModel):
    """The attributes for an artist resource."""
    artwork: Artwork | None = Field(
        None, alias="artwork", description="The artwork for the artist image.")
    editorial_notes: EditorialNotes | None = Field(
        None, alias="editorialNotes", 
        description="""
        The notes about the artist that appear in the Apple Music catalog
        """)
    genre_names: list[str] = Field(
        None, alias="genreNames", description="The names of the genres associated with this artist.")
    name: str = Field(
        None, alias="name", description="The localized name of the artist.")
    url: str = Field(
        None, alias="url", description="The URL for sharing the artist in Apple Music.")


class CuratorsAttributes(BaseModel):
    """The attributes for a curator resource."""
    artwork: Artwork = Field(
        None, alias="artwork", description="The curator artwork.")
    editorial_notes: EditorialNotes | None = Field(
        None, alias="editorialNotes", description="The notes about the curator.")
    name: str = Field(
        None, alias="name", description="The localized name of the curator.")
    url: str = Field(
        None, alias="url", description="The URL for sharing the curator in Apple Music.")


class StationsAttributes(BaseModel):
    """The attributes for a station resource."""
    artwork: Artwork = Field(
        None, alias="artwork", description="The radio station artwork.")
    duration_in_millis: int | None = Field(
        None, alias="durationInMillis", 
        description="""
        The duration of the stream. This value isn’t emitted for ‘live’
        or programmed stations
        """)
    editorial_notes: EditorialNotes | None = Field(
        None, alias="editorialNotes", description="The notes about the station that appear in Apple Music.")
    episode_number: str | None = Field(
        None, alias="episodeNumber", 
        description="""
        The episode number of the station. This value appears when the
        station represents an episode of a show or other content
        """)
    content_rating: Literal['clean', 'explicit'] | None = Field(
        None, alias="contentRating", 
        description="""
        The rating of the content possibly heard while playing the station.
        The possible values for this rating are clean and explicit. No
        value means no rating
        """)
    is_live: bool = Field(
        None, alias="isLive", description="Indicates whether the station is a livestream.")
    media_kind: Literal['audio', 'video'] = Field(
        None, alias="mediaKind", 
        description="""
        The media kind for the station. It can have value audio or video
        depending on whether it has video stream or audio stream
        """)
    name: str = Field(
        None, alias="name", description="The localized name of the station.")
    play_params: PlayParameters | None = Field(
        None, alias="playParams", 
        description="""
        When present, this attribute indicates that the radio station
        or episode is available to play with an Apple Music subscription.
        The value map may be used to initiate playback of the station.
        Live radio stations and episodes initiate streaming playback.
        Track-based stations initiate playback of individual tracks
        """)
    station_provider_name: str | None = Field(
        None, alias="stationProviderName", 
        description="""
        The name of the entity that provided the station, when specified
        """)
    url: str = Field(
        None, alias="url", description="The URL for sharing the station in Apple Music.")


class LibraryMusicVideos(BaseModel):
    """A resource object that represents a library music video."""
    id: str = Field(
        None, alias="id", description="The identifier for the library music video.")
    type: Literal['library-music-videos'] = Field(
        None, alias="type", description="This value is always library-music-videos.")
    href: str = Field(
        None, alias="href", description="The relative location for the library music video resource.")
    attributes: LibraryMusicVideosAttributes | None = Field(
        None, alias="attributes", description="The attributes for the library music video.")
    relationships: LibraryMusicVideosRelationships | None = Field(
        None, alias="relationships", description="The relationships for the library music video.")


class LibraryMusicVideosResponse(BaseModel):
    """The response to a library music videos request."""
    data: list[LibraryMusicVideos] = Field(
        None, alias="data", 
        description="""
        The LibraryMusicVideos included in the response for the request
        """)


class SongsRelationships(BaseModel):
    """The relationships for a song resource."""
    albums: SongsRelationshipsSongsAlbumsRelationship | None = Field(
        None, alias="albums", 
        description="""
        The albums associated with the song. By default, albums includes
        identifiers only.
        """)
    artists: SongsRelationshipsSongsArtistsRelationship | None = Field(
        None, alias="artists", 
        description="""
        The artists associated with the song. By default, artists includes
        identifiers only.
        """)
    composers: SongsRelationshipsSongsComposersRelationship | None = Field(
        None, alias="composers", description="The composers for a catalog song.")
    genres: SongsRelationshipsSongsGenresRelationship | None = Field(
        None, alias="genres", 
        description="""
        The genres associated with the song. By default, genres is not
        included.
        """)
    library: SongsRelationshipsSongsLibraryRelationship | None = Field(
        None, alias="library", description="Library song for a catalog song if added to library.")
    music_videos: SongsRelationshipsSongsMusicVideosRelationship | None = Field(
        None, alias="music-videos", description="Music videos for a catalog song.")
    station: SongsRelationshipsSongsStationRelationship | None = Field(
        None, alias="station", 
        description="""
        The station associated with the song. By default, station is
        not included.
        """)


class PlaylistsAttributes(BaseModel):
    """The attributes for a playlist resource."""
    artwork: Artwork | None = Field(
        None, alias="artwork", description="The playlist artwork.")
    curator_name: str = Field(
        None, alias="curatorName", description="The display name of the curator.")
    description: DescriptionAttribute | None = Field(
        None, alias="description", description="A description of the playlist.")
    is_chart: bool = Field(
        None, alias="isChart", 
        description="""
        Indicates whether the playlist represents a popularity chart
        """)
    last_modified_date: str | None = Field(
        None, alias="lastModifiedDate", description="The date the playlist was last modified.")
    name: str = Field(
        None, alias="name", description="The localized name of the playlist.")
    playlist_type: Literal['editorial', 'external', 'personal-mix', 'replay', 'user-shared'] = Field(
        None, alias="playlistType", description="The type of playlist. Possible values are:")
    play_params: PlayParameters | None = Field(
        None, alias="playParams", 
        description="""
        The value map may be used to initiate playback of available tracks
        in the playlist
        """)
    url: str = Field(
        None, alias="url", description="The URL for sharing the playlist in Apple Music.")
    track_types: list[Literal['music-videos', 'songs']] | None = Field(
        None, alias="trackTypes", 
        description="""
        (Extended) The resource types that are present in the tracks
        of the playlists
        """)


class AlbumsRelationships(BaseModel):
    """The relationships for an album resource."""
    artists: AlbumsRelationshipsAlbumsArtistsRelationship | None = Field(
        None, alias="artists", 
        description="""
        The artists associated with the album. By default, artists includes
        identifiers only.
        """)
    genres: AlbumsRelationshipsAlbumsGenresRelationship | None = Field(
        None, alias="genres", description="The genres for the album. By default, genres not included. ")
    tracks: AlbumsRelationshipsAlbumsTracksRelationship | None = Field(
        None, alias="tracks", 
        description="""
        The songs and music videos on the album. By default, tracks includes
        objects.
        """)
    library: AlbumsRelationshipsAlbumsLibraryRelationship | None = Field(
        None, alias="library", 
        description="""
        The album in the user’s library for the catalog album, if any
        """)
    record_labels: AlbumsRelationshipsAlbumsRecordLabelsRelationship | None = Field(
        None, alias="record-labels", description="The record labels for the album")


class RelationshipResponse(BaseModel):
    """The response for a direct resource relationship fetch."""
    data: list[Resource] = Field(
        None, alias="data", description="A paginated collection of resources in the relationship.")
    meta: RelationshipResponseMeta | None = Field(
        None, alias="meta", description="Contextual data about the relationship.")
    next: str | None = Field(
        None, alias="next", 
        description="""
        A relative cursor to fetch the next paginated collection of resources
        in the relationship if more exist
        """)


class DescriptionAttribute(BaseModel):
    """An object that represents a description attribute."""
    short: str | None = Field(
        None, alias="short", 
        description="""
        An abbreviated description to show inline or when the content
        appears alongside other content
        """)
    standard: str = Field(
        None, alias="standard", 
        description="""
        A description to show when the content is prominently displayed
        """)


class ActivitiesAttributes(BaseModel):
    """The attributes for an activities resource."""
    artwork: Artwork = Field(
        None, alias="artwork", description="The activity artwork.")
    editorial_notes: EditorialNotes | None = Field(
        None, alias="editorialNotes", 
        description="""
        The notes about the activity that appear in the Apple Music catalog
        """)
    name: str = Field(
        None, alias="name", description="The localized name of the activity.")
    url: str = Field(
        None, alias="url", description="The URL for sharing the activity in Apple Music.")


class ChartResponseResults(BaseModel):
    """A mapping of a requested type to an array of charts."""
    albums: list[ChartResponseResultsAlbumsChart] = Field(
        None, alias="albums", description="The albums results of a chart.")
    music_videos: list[ChartResponseResultsMusicVideosChart] = Field(
        None, alias="music-videos", description="The music videos results of a chart.")
    playlists: list[ChartResponseResultsPlaylistsChart] = Field(
        None, alias="playlists", description="The playlists results of a chart.")
    songs: list[ChartResponseResultsSongsChart] = Field(
        None, alias="songs", description="The songs results of a chart.")


class RatingsRelationships(BaseModel):
    """The relationships for a rating resource."""
    content: RatingsRelationshipsRatingsContentRelationship | None = Field(
        None, alias="content", description="The content associated with the rating.")


class ArtistsRelationships(BaseModel):
    """The relationships for an artist resource."""
    albums: ArtistsRelationshipsArtistsAlbumsRelationship | None = Field(
        None, alias="albums", 
        description="""
        The albums associated with the artist. By default, albums includes
        identifiers only.
        """)
    genres: ArtistsRelationshipsArtistsGenresRelationship | None = Field(
        None, alias="genres", 
        description="""
        The genres associated with the artist. By default, genres not
        included.
        """)
    music_videos: ArtistsRelationshipsArtistsMusicVideosRelationship | None = Field(
        None, alias="music-videos", 
        description="""
        The music videos associated with the artist. By default, musicVideos
        not included.
        """)
    playlists: ArtistsRelationshipsArtistsPlaylistsRelationship | None = Field(
        None, alias="playlists", 
        description="""
        The playlists associated with the artist. By default, playlists
        not included.
        """)
    station: ArtistsRelationshipsArtistsStationRelationship | None = Field(
        None, alias="station", 
        description="""
        The station associated with the artist. By default, station not
        included
        """)


class CuratorsRelationships(BaseModel):
    """The relationships for a curator resource."""
    playlists: CuratorsRelationshipsCuratorsPlaylistsRelationship | None = Field(
        None, alias="playlists", 
        description="""
        The playlists associated with the curator. By default, playlists
        includes identifiers only.
        """)


class LibrarySearchResponse(BaseModel):
    """The response to a request for a library search."""
    results: LibrarySearchResponseResults = Field(
        None, alias="results", 
        description="""
        The results included in the response to a request for a library
        search
        """)


class SearchResponseResults(BaseModel):
    """
    An object that represents the results of a catalog search query
    """
    activities: SearchResponseResultsActivitiesSearchResult | None = Field(
        None, alias="activities", 
        description="""
        The activities results for a term search for specific resource
        types
        """)
    albums: SearchResponseResultsAlbumsSearchResult | None = Field(
        None, alias="albums", 
        description="""
        The albums results for a term search for specific resource types
        """)
    apple_curators: SearchResponseResultsAppleCuratorsSearchResult | None = Field(
        None, alias="apple-curators", 
        description="""
        The Apple curators results for a term search for specific resource
        types
        """)
    artists: SearchResponseResultsArtistsSearchResult | None = Field(
        None, alias="artists", 
        description="""
        The artists results for a term search for specific resource types
        """)
    curators: SearchResponseResultsCuratorsSearchResult | None = Field(
        None, alias="curators", 
        description="""
        The curators results for a term search for specific resource
        types
        """)
    music_videos: SearchResponseResultsMusicVideosSearchResult | None = Field(
        None, alias="music-videos", 
        description="""
        The music videos results for a term search for specific resource
        types
        """)
    playlists: SearchResponseResultsPlaylistsSearchResult | None = Field(
        None, alias="playlists", 
        description="""
        The playlists results for a term search for specific resource
        types
        """)
    record_labels: SearchResponseResultsRecordLabelsSearchResult | None = Field(
        None, alias="record-labels", 
        description="""
        The record labels results for a term search for specific resource
        types
        """)
    songs: SearchResponseResultsSongsSearchResult | None = Field(
        None, alias="songs", 
        description="""
        The songs results for a term search for specific resource types
        """)
    stations: SearchResponseResultsStationsSearchResult | None = Field(
        None, alias="stations", 
        description="""
        The stations results for a term search for specific resource
        types
        """)
    top: SearchResponseResultsTopResultsSearchResult | None = Field(
        None, alias="top", 
        description="""
        The top results for a term search for specific resource types
        """)


class StationsRelationships(BaseModel):
    """
    The name of the relationship you want to fetch for this resource
    """
    radio_show: StationsRelationshipsStationsRadioShowRelationship | None = Field(
        None, alias="radio-show", 
        description="""
        The relationship to be added. The possible value is radio-show
        """)


class MusicVideosAttributes(BaseModel):
    """The attributes for a music video resource."""
    album_name: str | None = Field(
        None, alias="albumName", description="The name of the album the music video appears on.")
    artist_name: str = Field(
        None, alias="artistName", description="The artist’s name.")
    artist_url: str | None = Field(
        None, alias="artistUrl", description="(Extended) The URL of the artist for this content.")
    artwork: Artwork = Field(
        None, alias="artwork", description="The artwork for the music video’s associated album.")
    content_rating: Literal['clean', 'explicit'] | None = Field(
        None, alias="contentRating", 
        description="""
        The Recording Industry Association of America (RIAA) rating of
        the content. No value means no rating
        """)
    duration_in_millis: int = Field(
        None, alias="durationInMillis", description="The duration of the music video in milliseconds.")
    editorial_notes: EditorialNotes | None = Field(
        None, alias="editorialNotes", description="The editorial notes for the music video.")
    genre_names: list[str] = Field(
        None, alias="genreNames", description="The music video’s associated genres.")
    has_4_k: bool = Field(
        None, alias="has4K", description="Whether the music video has 4K content.")
    has_hdr: bool = Field(
        None, alias="hasHDR", description="Whether the music video has HDR10-encoded content.")
    isrc: str | None = Field(
        None, alias="isrc", 
        description="""
        The International Standard Recording Code (ISRC) for the music
        video
        """)
    name: str = Field(
        None, alias="name", description="The localized name of the music video.")
    play_params: PlayParameters | None = Field(
        None, alias="playParams", 
        description="""
        When present, this attribute indicates that the music video is
        available to play with an Apple Music subscription. The value
        map may be used to initiate playback. Previews of the music video
        may be available with or without an Apple Music subscription
        """)
    previews: list[Preview] = Field(
        None, alias="previews", description="The preview assets for the music video.")
    release_date: str | None = Field(
        None, alias="releaseDate", 
        description="""
        The release date of the music video, when known, in YYYY-MM-DD
        or YYYY format. Prerelease music videos may have an expected
        release date in the future
        """)
    track_number: int | None = Field(
        None, alias="trackNumber", 
        description="""
        The number of the music video in the album’s track list, when
        associated with an album
        """)
    url: str = Field(
        None, alias="url", description="The URL for sharing the music video in Apple Music. ")
    video_sub_type: Literal['preview'] | None = Field(
        None, alias="videoSubType", description="The video subtype associated with the content.")
    work_id: str | None = Field(
        None, alias="workId", 
        description="""
        (Classical music only) A unique identifier for the associated
        work
        """)
    work_name: str | None = Field(
        None, alias="workName", description="(Classical music only) The name of the associated work.")


class ResourceRelationships(RootModel):
    """Relationships belonging to the resource."""
    root: Dict[str, Relationship | None] = Field(
        None, 
        description="""
        A named relationship for the resource creating an association
        from the resource to other resources
        """)


class PersonalRecommendation(BaseModel):
    """
    A resource object that represents recommended resources for a
    user calculated using their selected preferences
    """
    id: str = Field(
        None, alias="id", description="The identifier for the recommendation.")
    type: Literal['personal-recommendation'] = Field(
        None, alias="type", description="This value must always be personal-recommendation.")
    href: str = Field(
        None, alias="href", description="The relative location for the recommendation resource.")
    attributes: PersonalRecommendationAttributes | None = Field(
        None, alias="attributes", description="The attributes for the recommendation.")
    relationships: PersonalRecommendationRelationships | None = Field(
        None, alias="relationships", description="The relationships for the playlist.")


class PersonalRecommendationResponse(BaseModel):
    """The response to a request for personal recommendations."""
    data: list[PersonalRecommendation] = Field(
        None, alias="data", 
        description="""
        The PersonalRecommendation resources included in the response
        for the request
        """)


class RecordLabelsAttributes(BaseModel):
    """The attributes for a record label resource."""
    artwork: Artwork = Field(
        None, alias="artwork", description="Artwork associated with this content.")
    description: DescriptionAttribute | None = Field(
        None, alias="description", description="A map of description information.")
    name: str = Field(
        None, alias="name", description="The (potentially) censored name of the content.")
    url: str = Field(
        None, alias="url", description="The URL to load the record label from.")


class LibraryPlaylistFolders(BaseModel):
    """
    A resource object that represents a library playlist folder
    """
    id: str = Field(
        None, alias="id", description="The identifier for the library playlist folder.")
    type: Literal['library-playlist-folders'] = Field(
        None, alias="type", description="This value is always library-playlist-folders.")
    href: str = Field(
        None, alias="href", 
        description="""
        The relative location for the library playlist folder resource
        """)
    attributes: LibraryPlaylistFoldersAttributes | None = Field(
        None, alias="attributes", 
        description="""
        The attributes for the library-playlist-folders resource type
        """)
    relationships: LibraryPlaylistFoldersRelationships | None = Field(
        None, alias="relationships", 
        description="""
        The relationships from library-playlist-folders to other resources
        """)


class LibraryPlaylistFoldersResponse(BaseModel):
    """The response to a library playlist folders request."""
    data: list[LibraryPlaylistFolders] = Field(
        None, alias="data", 
        description="""
        The LibraryPlaylistFolders included in the response for the request
        """)


class PlaylistsRelationships(BaseModel):
    """The relationships for a playlist resource."""
    curator: PlaylistsRelationshipsPlaylistsCuratorRelationship | None = Field(
        None, alias="curator", 
        description="""
        The curator that created the playlist. By default, curator includes
        identifiers only.
        """)
    library: PlaylistsRelationshipsPlaylistsLibraryRelationship | None = Field(
        None, alias="library", 
        description="""
        Library playlist for a catalog playlist if added to library
        """)
    tracks: PlaylistsRelationshipsPlaylistsTracksRelationship | None = Field(
        None, alias="tracks", 
        description="""
        The songs and music videos included in the playlist. By default,
        tracks includes objects.
        """)


class LibrarySongsAttributes(BaseModel):
    """The attributes for a library song resource."""
    album_name: str | None = Field(
        None, alias="albumName", description="The name of the album the song appears on.")
    artist_name: str = Field(
        None, alias="artistName", description="The artist’s name.")
    artwork: Artwork = Field(
        None, alias="artwork", description="The album artwork.")
    content_rating: Literal['clean', 'explicit'] | None = Field(
        None, alias="contentRating", 
        description="""
        The Recording Industry Association of America (RIAA) rating of
        the content. The possible values for this rating are clean and
        explicit. No value means no rating
        """)
    disc_number: int | None = Field(
        None, alias="discNumber", description="The disc number the song appears on.")
    duration_in_millis: int = Field(
        None, alias="durationInMillis", description="The approximate length of the song in milliseconds.")
    genre_names: list[str] = Field(
        None, alias="genreNames", description="The genre names the song is associated with.")
    has_lyrics: bool = Field(
        None, alias="hasLyrics", 
        description="""
        Indicates if the song has lyrics available in the Apple Music
        catalog. If true, the song has lyrics available; otherwise, it
        does not
        """)
    name: str = Field(
        None, alias="name", description="The localized name of the song.")
    play_params: PlayParameters | None = Field(
        None, alias="playParams", 
        description="""
        When present, this attribute indicates that the song is available
        to play.  The value map may be used to initiate playback
        """)
    release_date: str | None = Field(
        None, alias="releaseDate", 
        description="""
        The release date of the song, when known, in YYYY-MM-DD or YYYY
        format. Pre-release songs may have an expected release date in
        the future
        """)
    track_number: int | None = Field(
        None, alias="trackNumber", description="The number of the song in the album’s track list.")


class AppleCuratorsAttributes(BaseModel):
    """The attributes for an Apple curator resource."""
    artwork: Artwork = Field(
        None, alias="artwork", description="The curator artwork.")
    editorial_notes: EditorialNotes | None = Field(
        None, alias="editorialNotes", 
        description="""
        The notes about the curator that appear in the Apple Music catalog
        """)
    kind: Literal['Curator', 'Genre', 'Show'] = Field(
        None, alias="kind", description="The type of curator. Possible values are:")
    name: str = Field(
        None, alias="name", description="The localized name of the curator.")
    short_name: str | None = Field(
        None, alias="shortName", description="The localized shortened name of the curator.")
    show_host_name: str | None = Field(
        None, alias="showHostName", description="The name of the host if kind is Show.")
    url: str = Field(
        None, alias="url", description="The URL for sharing the curator in Apple Music.")


class ActivitiesRelationships(BaseModel):
    """The relationships for an activity resource."""
    playlists: ActivitiesRelationshipsActivitiesPlaylistsRelationship | None = Field(
        None, alias="playlists", 
        description="""
        The playlists associated with this activity. By default, playlists
        includes identifiers only.
        """)


class LibraryAlbumsAttributes(BaseModel):
    """The attributes for a library album resource."""
    artist_name: str = Field(
        None, alias="artistName", description="The artist’s name.")
    artwork: Artwork = Field(
        None, alias="artwork", description="The album artwork.")
    content_rating: Literal['clean', 'explicit'] | None = Field(
        None, alias="contentRating", 
        description="""
        The Recording Industry Association of America (RIAA) rating of
        the content. The possible values for this rating are clean and
        explicit. No value means no rating
        """)
    date_added: str | None = Field(
        None, alias="dateAdded", 
        description="""
        The date the album was added to the library, in YYYY-MM-DD or
        YYYY format
        """)
    name: str = Field(
        None, alias="name", description="The localized name of the album.")
    play_params: PlayParameters | None = Field(
        None, alias="playParams", 
        description="""
        When present, this attribute indicates that tracks from the album
        are available to play.  The value map may be used to initiate
        playback of available tracks on the album
        """)
    release_date: str | None = Field(
        None, alias="releaseDate", 
        description="""
        The release date of the album, when known, in YYYY-MM-DD or YYYY
        format. Pre-release albums may have an expected release date
        in the future
        """)
    track_count: int = Field(
        None, alias="trackCount", description="The number of tracks.")
    genre_names: list[str] = Field(
        None, alias="genreNames", description="The names of the genres associated with this album.")


class RelationshipViewResponse(BaseModel):
    """The response for a direct resource view fetch."""
    attributes: RelationshipViewResponseAttributes | None = Field(
        None, alias="attributes", description="The attribute metadata for the view.")
    data: list[Resource] = Field(
        None, alias="data", description="A paginated collection of resources in the view.")
    meta: RelationshipViewResponseMeta | None = Field(
        None, alias="meta", description="Contextual data about the view.")
    next: str | None = Field(
        None, alias="next", 
        description="""
        A relative cursor to fetch the next paginated collection of resources
        in the view if more exist
        """)


class MusicVideosRelationships(BaseModel):
    """The relationships for a music video resource."""
    albums: MusicVideosRelationshipsMusicVideosAlbumsRelationship | None = Field(
        None, alias="albums", 
        description="""
        The albums associated with the music video. By default, albums
        includes identifiers only.
        """)
    artists: MusicVideosRelationshipsMusicVideosArtistsRelationship | None = Field(
        None, alias="artists", 
        description="""
        The artists associated with the music video. By default, artists
        includes identifiers only.
        """)
    genres: MusicVideosRelationshipsMusicVideosGenresRelationship | None = Field(
        None, alias="genres", 
        description="""
        The genres associated with the music video. By default, genres
        not included.
        """)
    library: MusicVideosRelationshipsMusicVideosLibraryRelationship | None = Field(
        None, alias="library", description="The library of a music video if added to library.")
    songs: MusicVideosRelationshipsMusicVideosSongsRelationship | None = Field(
        None, alias="songs", description="The songs associated with the music video.")


class LibrarySongsRelationships(BaseModel):
    """The relationships for a library song resource."""
    albums: LibrarySongsRelationshipsLibrarySongsAlbumsRelationship | None = Field(
        None, alias="albums", 
        description="""
        The library albums associated with the song. By default, albums
        not included.
        """)
    artists: LibrarySongsRelationshipsLibrarySongsArtistsRelationship | None = Field(
        None, alias="artists", 
        description="""
        The library artists associated with the song. By default, artists
        not included.
        """)
    catalog: LibrarySongsRelationshipsLibrarySongsCatalogRelationship | None = Field(
        None, alias="catalog", 
        description="""
        The song in the Apple Music catalog the library song is associated
        with, when known
        """)


class AppleCuratorsRelationships(BaseModel):
    """The relationships for an Apple curator resource."""
    playlists: AppleCuratorsRelationshipsAppleCuratorsPlaylistsRelationship | None = Field(
        None, alias="playlists", 
        description="""
        The playlists associated with this curator. By default, playlists
        includes identifiers only.
        """)


class StationGenresRelationships(BaseModel):
    """The relationships for a station genre resource."""
    stations: StationGenresRelationshipsStationGenresStationsRelationship | None = Field(
        None, alias="stations", description="Stations associated with the station genre.")


class LibraryPlaylistsAttributes(BaseModel):
    """The attributes for a library playlist resource."""
    artwork: Artwork | None = Field(
        None, alias="artwork", description="The playlist artwork.")
    can_edit: bool = Field(
        None, alias="canEdit", description="Indicates whether the playlist is editable.")
    date_added: str | None = Field(
        None, alias="dateAdded", 
        description="""
        The date and time the playlist was added to the user’s library
        """)
    description: DescriptionAttribute | None = Field(
        None, alias="description", description="A description of the playlist.")
    has_catalog: bool = Field(
        None, alias="hasCatalog", 
        description="""
        Indicates whether the playlist has a representation in the Apple
        Music catalog
        """)
    name: str = Field(
        None, alias="name", description="The localized name of the playlist.")
    play_params: PlayParameters | None = Field(
        None, alias="playParams", 
        description="""
        The value map may be used to initiate playback of available tracks
        in the playlist
        """)
    is_public: bool = Field(
        None, alias="isPublic", 
        description="""
        A flag to indicate whether the library playlist is a public playlist
        """)
    track_types: list[Literal['library-music-videos', 'library-songs']] | None = Field(
        None, alias="trackTypes", 
        description="""
        (Extended) The resource types that are present in the tracks
        of the library playlist
        """)


class LibraryAlbumsRelationships(BaseModel):
    """The relationships for a library album object."""
    artists: LibraryAlbumsRelationshipsLibraryAlbumsArtistsRelationship | None = Field(
        None, alias="artists", 
        description="""
        The library artists associated with the album. By default, artists
        not included.
        """)
    catalog: LibraryAlbumsRelationshipsLibraryAlbumsCatalogRelationship | None = Field(
        None, alias="catalog", 
        description="""
        The album in the Apple Music catalog the library album is associated
        with, when known
        """)
    tracks: LibraryAlbumsRelationshipsLibraryAlbumsTracksRelationship | None = Field(
        None, alias="tracks", 
        description="""
        The library songs and library music videos on the album. Only
        available when fetching single library album resource by ID.
        By default, tracks includes objects.
        """)


class LibraryArtistsRelationships(BaseModel):
    """The relationships for a library artist resource."""
    albums: LibraryArtistsRelationshipsLibraryArtistsAlbumsRelationship | None = Field(
        None, alias="albums", 
        description="""
        The library albums associated with the artist. By default, albums
        not included. It’s available only when fetching a single library
        artist resource by ID
        """)
    catalog: LibraryArtistsRelationshipsLibraryArtistsCatalogRelationship | None = Field(
        None, alias="catalog", 
        description="""
        The artist in the Apple Music catalog the library artist is associated
        with, when known
        """)


class LibrarySearchResponseResults(BaseModel):
    """
    An object that represents the results of a library search query
    """
    library_albums: LibrarySearchResponseResultsLibraryAlbumsSearchResult | None = Field(
        None, alias="library-albums", 
        description="""
        The library albums results for a term search for specific resource
        types
        """)
    library_artists: LibrarySearchResponseResultsLibraryArtistsSearchResult | None = Field(
        None, alias="library-artists", 
        description="""
        The library artists results for a term search for specific resource
        types
        """)
    library_music_videos: LibrarySearchResponseResultsLibraryMusicVideosSearchResult | None = Field(
        None, alias="library-music-videos", 
        description="""
        The library music videos results for a term search for specific
        resource types
        """)
    library_playlists: LibrarySearchResponseResultsLibraryPlaylistsSearchResult | None = Field(
        None, alias="library-playlists", 
        description="""
        The library playlists results for a term search for specific
        resource types
        """)
    library_songs: LibrarySearchResponseResultsLibrarySongsSearchResult | None = Field(
        None, alias="library-songs", 
        description="""
        The library songs results for a term search for specific resource
        types
        """)


class LibraryMusicVideosAttributes(BaseModel):
    """The attributes for the library music videos resource type."""
    album_name: str | None = Field(
        None, alias="albumName", description="The name of the album the music video appears on.")
    artist_name: str = Field(
        None, alias="artistName", description="The artist’s name.")
    artwork: Artwork = Field(
        None, alias="artwork", description="The artwork for the music video’s associated album.")
    content_rating: Literal['clean', 'explicit'] | None = Field(
        None, alias="contentRating", 
        description="""
        The Recording Industry Association of America (RIAA) rating of
        the content. The possible values for this rating are clean and
        explicit. No value means no rating
        """)
    duration_in_millis: int = Field(
        None, alias="durationInMillis", description="The duration of the music video in milliseconds.")
    genre_names: list[str] = Field(
        None, alias="genreNames", description="The names of the genres associated with this music video.")
    name: str = Field(
        None, alias="name", description="The localized name of the music video.")
    play_params: PlayParameters | None = Field(
        None, alias="playParams", 
        description="""
        When present, this attribute indicates that the music video is
        able to play.  The value map may be used to initiate playback
        """)
    release_date: str | None = Field(
        None, alias="releaseDate", 
        description="""
        The release date of the music video, when known, in YYYY-MM-DD
        or YYYY format. Pre-release content may have an expected release
        date in the future
        """)
    track_number: int | None = Field(
        None, alias="trackNumber", description="The number of the music video in the album’s track list.")


class LibraryPlaylistsRelationships(BaseModel):
    """The relationships for a library playlist resource."""
    catalog: LibraryPlaylistsRelationshipsLibraryPlaylistsCatalogRelationship | None = Field(
        None, alias="catalog", 
        description="""
        The corresponding playlist in the Apple Music catalog the playlist
        is associated with
        """)
    tracks: LibraryPlaylistsRelationshipsLibraryPlaylistsTracksRelationship | None = Field(
        None, alias="tracks", 
        description="""
        The library songs and library music videos included in the playlist.
        By default, tracks not included. Only available when fetching
        a single library playlist resource by ID.
        """)


class ChartResponseResultsSongsChart(BaseModel):
    """The songs results of a chart."""
    chart: str = Field(
        None, alias="chart", 
        description="""
        The unique name of the chart to use when fetching a specific
        chart
        """)
    data: list[Songs] = Field(
        None, alias="data", description="The popularity-ordered songs for the chart.")
    href: str | None = Field(
        None, alias="href", description="A relative location to fetch the chart results directly.")
    name: str = Field(
        None, alias="name", description="The localized display name for the chart.")
    next: str | None = Field(
        None, alias="next", 
        description="""
        A relative cursor to fetch the next paginated results for the
        chart if more exist
        """)


class LibraryPlaylistCreationRequest(BaseModel):
    """A request to create a new playlist in a user’s library."""
    attributes: LibraryPlaylistCreationRequestAttributes = Field(
        None, alias="attributes", 
        description="""
        A dictionary that includes strings for the name and description
        of the new playlist
        """)
    relationships: LibraryPlaylistCreationRequestRelationships | None = Field(
        None, alias="relationships", description="An optional key including tracks for the new playlist.")


class ArtistsViewsArtistsSinglesView(BaseModel):
    """
    A relationship view from this artist to albums associated with
    the artist categorized as singles
    """
    href: str | None = Field(
        None, alias="href", description="A relative location for the view.")
    next: str | None = Field(
        None, alias="next", 
        description="""
        A relative cursor to fetch the next paginated collection of resources
        in the view if more exist
        """)
    attributes: ArtistsViewsArtistsSinglesViewAttributes = Field(
        None, alias="attributes", description="The attributes for the view.")
    data: list[Albums] = Field(
        None, alias="data", description="Albums associated with the artist categorized as singles.")


class AlbumsViewsAlbumsAppearsOnView(BaseModel):
    """
    A relationship view from this album to a selection of playlists
    tracks from this album appear on
    """
    href: str | None = Field(
        None, alias="href", description="The relative location to fetch the view directly.")
    next: str | None = Field(
        None, alias="next", 
        description="""
        The relative location to request the next page of resources in
        the collection, if additional resources are available for fetching
        """)
    attributes: AlbumsViewsAlbumsAppearsOnViewAttributes = Field(
        None, alias="attributes", description="The attributes for the view.")
    data: list[Playlists] = Field(
        None, alias="data", 
        description="""
        A selection of playlists that tracks from this album appear on
        """)


class ChartResponseResultsAlbumsChart(BaseModel):
    """The albums results of a chart."""
    chart: str = Field(
        None, alias="chart", 
        description="""
        The unique name of the chart to use when fetching a specific
        chart
        """)
    data: list[Albums] = Field(
        None, alias="data", description="The popularity-ordered albums for the chart.")
    href: str | None = Field(
        None, alias="href", description="A relative location to fetch the chart results directly.")
    name: str = Field(
        None, alias="name", description="The localized display name for the chart.")
    next: str | None = Field(
        None, alias="next", 
        description="""
        A relative cursor to fetch the next paginated results for the
        chart if more exist
        """)


class LibraryMusicVideosRelationships(BaseModel):
    """
    The relationships from library music videos to other resources
    """
    albums: LibraryMusicVideosRelationshipsLibraryMusicVideosAlbumsRelationship | None = Field(
        None, alias="albums", 
        description="""
        The library albums associated with the music video. By default,
        albums not included.
        """)
    artists: LibraryMusicVideosRelationshipsLibraryMusicVideosArtistsRelationship | None = Field(
        None, alias="artists", 
        description="""
        The library artists associated with the music video. By default,
        artists not included.
        """)
    catalog: LibraryMusicVideosRelationshipsLibraryMusicVideosCatalogRelationship | None = Field(
        None, alias="catalog", 
        description="""
        The music video in the Apple Music catalog the library music
        video is associated with, when known
        """)


class ArtistsViewsArtistsTopSongsView(BaseModel):
    """
    A relationship view from this artist to songs associated with
    the artist based on popularity in the current storefront
    """
    href: str | None = Field(
        None, alias="href", description="A relative location for the view.")
    next: str | None = Field(
        None, alias="next", 
        description="""
        A relative cursor to fetch the next paginated collection of resources
        in the view if more exist
        """)
    attributes: ArtistsViewsArtistsTopSongsViewAttributes = Field(
        None, alias="attributes", description="The attributes for the view.")
    data: list[Songs] = Field(
        None, alias="data", 
        description="""
        Songs associated with the artist based on popularity in the current
        storefront
        """)


class PersonalRecommendationAttributes(BaseModel):
    """The attributes for a recommendation resource."""
    is_group_recommendation: bool = Field(
        None, alias="isGroupRecommendation", description="Whether the recommendation is of group type.")
    kind: Literal['music-recommendations', 'recently-played', 'unknown'] = Field(
        None, alias="kind", description="The type of recommendation. Possible values are:")
    next_update_date: str = Field(
        None, alias="nextUpdateDate", 
        description="""
        The next date in UTC format for updating the recommendation
        """)
    reason: PersonalRecommendationAttributesReason | None = Field(
        None, alias="reason", description="The localized reason for the recommendation.")
    resource_types: list[str] = Field(
        None, alias="resourceTypes", description="The resource types supported by the recommendation.")
    title: PersonalRecommendationAttributesTitle | None = Field(
        None, alias="title", description="The localized title for the recommendation.")


class LibraryPlaylistFoldersAttributes(BaseModel):
    """
    A resource object that represents the attributes for a library
    playlist folder
    """
    date_added: str | None = Field(
        None, alias="dateAdded", 
        description="""
        The date this content added to the user’s library in ISO-8601
        format
        """)
    name: str = Field(
        None, alias="name", description="The (potentially) censored name of the content.")


class ArtistsViewsArtistsLiveAlbumsView(BaseModel):
    """
    A relationship view from this artist to albums associated with
    the artist categorized as live performances
    """
    href: str | None = Field(
        None, alias="href", description="A relative location for the view.")
    next: str | None = Field(
        None, alias="next", 
        description="""
        A relative cursor to fetch the next paginated collection of resources
        in the view if more exist
        """)
    attributes: ArtistsViewsArtistsLiveAlbumsViewAttributes = Field(
        None, alias="attributes", description="The attributes for the view.")
    data: list[Albums] = Field(
        None, alias="data", 
        description="""
        Albums associated with the artist categorized as live performances
        """)


class ArtistsViewsArtistsFullAlbumsView(BaseModel):
    """
    A relationship view from this artist to full-release albums associated
    with the artist
    """
    href: str | None = Field(
        None, alias="href", description="A relative location for the view.")
    next: str | None = Field(
        None, alias="next", 
        description="""
        A relative cursor to fetch the next paginated collection of resources
        in the view if more exist
        """)
    attributes: ArtistsViewsArtistsFullAlbumsViewAttributes = Field(
        None, alias="attributes", description="The attributes for the view.")
    data: list[Albums] = Field(
        None, alias="data", description="Full-release albums associated with the artist.")


class ChartResponseResultsPlaylistsChart(BaseModel):
    """The playlists results of a chart."""
    chart: str = Field(
        None, alias="chart", 
        description="""
        The unique name of the chart to use when fetching a specific
        chart
        """)
    data: list[Playlists] = Field(
        None, alias="data", description="The popularity-ordered playlists for the chart.")
    href: str | None = Field(
        None, alias="href", description="A relative location to fetch the chart results directly.")
    name: str = Field(
        None, alias="name", description="The localized display name for the chart.")
    next: str | None = Field(
        None, alias="next", 
        description="""
        A relative cursor to fetch the next paginated results for the
        chart if more exist
        """)


class AlbumsViewsAlbumsRelatedVideosView(BaseModel):
    """
    A relationship view from this album to music videos for the songs
    on the album
    """
    href: str | None = Field(
        None, alias="href", description="The relative location to fetch the view directly.")
    next: str | None = Field(
        None, alias="next", 
        description="""
        The relative location to request the next page of resources in
        the collection, if additional resources are available for fetching
        """)
    attributes: AlbumsViewsAlbumsRelatedVideosViewAttributes = Field(
        None, alias="attributes", description="The attributes for the view.")
    data: list[MusicVideos] = Field(
        None, alias="data", description="The music videos available for songs on the album.")


class AlbumsViewsAlbumsRelatedAlbumsView(BaseModel):
    """
    A relationship view from this album to related and similar albums
    """
    href: str | None = Field(
        None, alias="href", description="The relative location to fetch the view directly.")
    next: str | None = Field(
        None, alias="next", 
        description="""
        The relative location to request the next page of resources in
        the collection, if additional resources are available for fetching
        """)
    attributes: AlbumsViewsAlbumsRelatedAlbumsViewAttributes = Field(
        None, alias="attributes", description="The attributes for the view.")
    data: list[Albums] = Field(
        None, alias="data", 
        description="""
        A collection of other albums related or similar to the album
        """)


class AlbumsViewsAlbumsOtherVersionsView(BaseModel):
    """A relationship view for other versions of this album."""
    href: str | None = Field(
        None, alias="href", description="The relative location to fetch the view directly.")
    next: str | None = Field(
        None, alias="next", 
        description="""
        The relative location to request the next page of resources in
        the collection, if additional resources are available for fetching
        """)
    attributes: AlbumsViewsAlbumsOtherVersionsViewAttributes = Field(
        None, alias="attributes", description="The attributes for the view.")
    data: list[Albums] = Field(
        None, alias="data", description="Other versions of the album.")


class PaginatedResourceCollectionResponse(BaseModel):
    """
    A response object composed of paginated resource objects for
    the request
    """
    next: str | None = Field(
        None, alias="next", 
        description="""
        A relative cursor to fetch the next paginated collection of resources
        for the request if more exist
        """)
    data: list[Resource] = Field(
        None, alias="data", description="A paginated collection of resources for the request.")


class PersonalRecommendationRelationships(BaseModel):
    """The relationships for a recommendation resource."""
    contents: PersonalRecommendationRelationshipsPersonalRecommendationContentsRelationship | None = Field(
        None, alias="contents", 
        description="""
        The contents associated with the content recommendation type.
        By default, contents includes objects.
        """)


class LibraryPlaylistFoldersRelationships(BaseModel):
    """
    A resource Object that represents the relationships for a library
    playlist folder
    """
    children: LibraryPlaylistFoldersRelationshipsLibraryPlaylistFoldersChildrenRelationship | None = Field(
        None, alias="children", description="The playlists and sub-folders contained in this folder.")
    parent: LibraryPlaylistFoldersRelationshipsLibraryPlaylistFoldersParentRelationship | None = Field(
        None, alias="parent", description="The parent of this folder.")


class ChartResponseResultsMusicVideosChart(BaseModel):
    """The music videos results of a chart."""
    chart: str = Field(
        None, alias="chart", 
        description="""
        The unique name of the chart to use when fetching a specific
        chart
        """)
    data: list[MusicVideos] = Field(
        None, alias="data", description="The popularity-ordered music vidoes for the chart.")
    href: str | None = Field(
        None, alias="href", description="A relative location to fetch the chart results directly.")
    name: str = Field(
        None, alias="name", description="The localized display name for the chart.")
    next: str | None = Field(
        None, alias="next", 
        description="""
        A relative cursor to fetch the next paginated results for the
        chart if more exist
        """)


class LibraryPlaylistFolderCreationRequest(BaseModel):
    """Request object to create a new library playlist folder."""
    attributes: LibraryPlaylistFolderCreationRequestAttributes = Field(
        None, alias="attributes", 
        description="""
        The attributes of the library playlist folder creation request
        """)
    relationships: LibraryPlaylistFolderCreationRequestRelationships | None = Field(
        None, alias="relationships", 
        description="""
        The relationships of the library playlist folder creation request
        """)


class ArtistsViewsArtistsLatestReleaseView(BaseModel):
    """
    A relationship view from this artist to the latest release for
    the artist determined to still be recent by the Apple Music Catalog
    """
    href: str | None = Field(
        None, alias="href", description="A relative location for the view.")
    next: str | None = Field(
        None, alias="next", 
        description="""
        A relative cursor to fetch the next paginated collection of resources
        in the view if more exist
        """)
    attributes: ArtistsViewsArtistsLatestReleaseViewAttributes = Field(
        None, alias="attributes", description="The attributes for the view.")
    data: list[Albums] = Field(
        None, alias="data", 
        description="""
        The latest release for the artist determined to still be recent
        by the Apple Music Catalog
        """)


class ArtistsViewsArtistsTopMusicVideosView(BaseModel):
    """
    A relationship view from this artist to relevant music videos
    associated with the artist
    """
    href: str | None = Field(
        None, alias="href", description="A relative location for the view.")
    next: str | None = Field(
        None, alias="next", 
        description="""
        A relative cursor to fetch the next paginated collection of resources
        in the view if more exist
        """)
    attributes: ArtistsViewsArtistsTopMusicVideosViewAttributes = Field(
        None, alias="attributes", description="The attributes for the view.")
    data: list[MusicVideos] = Field(
        None, alias="data", description="Relevant music videos associated with the artist.")


class ArtistsViewsArtistsSimilarArtistsView(BaseModel):
    """
    A relationship view from this artist to other artists similar
    to this artist
    """
    href: str | None = Field(
        None, alias="href", description="A relative location for the view.")
    next: str | None = Field(
        None, alias="next", 
        description="""
        A relative cursor to fetch the next paginated collection of resources
        in the view if more exist
        """)
    attributes: ArtistsViewsArtistsSimilarArtistsViewAttributes = Field(
        None, alias="attributes", description="The attributes for the view.")
    data: list[Artists] = Field(
        None, alias="data", description="Other artists similar to this artist.")


class ArtistsViewsArtistsFeaturedAlbumsView(BaseModel):
    """
    A relationship view from this artist to a collection of albums
    selected as featured for the artist
    """
    href: str | None = Field(
        None, alias="href", description="A relative location for the view.")
    next: str | None = Field(
        None, alias="next", 
        description="""
        A relative cursor to fetch the next paginated collection of resources
        in the view if more exist
        """)
    attributes: ArtistsViewsArtistsFeaturedAlbumsViewAttributes = Field(
        None, alias="attributes", description="The attributes for the view.")
    data: list[Albums] = Field(
        None, alias="data", description="A collection of albums selected as featured for the artist.")


class SearchResponseResultsSongsSearchResult(BaseModel):
    """An object containing a songs’ search result."""
    data: list[Songs] = Field(
        None, alias="data", description="The resources for the search result.")
    href: str | None = Field(
        None, alias="href", description="The relative location to fetch the search result.")
    next: str | None = Field(
        None, alias="next", 
        description="""
        A relative cursor to fetch the next paginated collection of resources
        in the result, if more exist
        """)


class ArtistsViewsArtistsAppearsOnAlbumsView(BaseModel):
    """
    A relationship view from this artist to a selection of albums
    from other artists on which this artist also appears
    """
    href: str | None = Field(
        None, alias="href", description="A relative location for the view.")
    next: str | None = Field(
        None, alias="next", 
        description="""
        A relative cursor to fetch the next paginated collection of resources
        in the view if more exist
        """)
    attributes: ArtistsViewsArtistsAppearsOnAlbumsViewAttributes = Field(
        None, alias="attributes", description="The attributes for the view.")
    data: list[Albums] = Field(
        None, alias="data", 
        description="""
        A selection of albums from other artists this artist appears
        on
        """)


class SearchResponseResultsAlbumsSearchResult(BaseModel):
    """An object containing an albums’ search result."""
    data: list[Albums] = Field(
        None, alias="data", description="The resources for the search result.")
    href: str | None = Field(
        None, alias="href", description="The relative location to fetch the search result.")
    next: str | None = Field(
        None, alias="next", 
        description="""
        A relative cursor to fetch the next paginated collection of resources
        in the result, if more exist
        """)


class SearchResponseResultsArtistsSearchResult(BaseModel):
    """An object containing an artists’ search result."""
    data: list[Artists] = Field(
        None, alias="data", description="The resources for the search result.")
    href: str | None = Field(
        None, alias="href", description="The relative location to fetch the search result.")
    next: str | None = Field(
        None, alias="next", 
        description="""
        A relative cursor to fetch the next paginated collection of resources
        in the result, if more exist
        """)


class PlaylistsViewsPlaylistsMoreByCuratorView(BaseModel):
    """Additional content by the same curator for this playlist."""
    href: str | None = Field(
        None, alias="href", description="A relative location for the view.")
    next: str | None = Field(
        None, alias="next", 
        description="""
        A relative cursor to fetch the next paginated collection of resources
        in the view if more exist
        """)
    attributes: PlaylistsViewsPlaylistsMoreByCuratorViewAttributes = Field(
        None, alias="attributes", description="The attribute metadata for the view.")
    data: list[Playlists] = Field(
        None, alias="data", description="A paginated collection of resources in the view.")


class LibraryPlaylistCreationRequestAttributes(BaseModel):
    """
    The attributes for a library playlist creation request object
    """
    description: str | None = Field(
        None, alias="description", description="The description of the playlist.")
    name: str = Field(
        None, alias="name", description="The name of the playlist. ")


class ArtistsViewsArtistsFeaturedPlaylistsView(BaseModel):
    """
    A relationship view from this artist to relevant playlists associated
    with the artist
    """
    href: str | None = Field(
        None, alias="href", description="A relative location for the view.")
    next: str | None = Field(
        None, alias="next", 
        description="""
        A relative cursor to fetch the next paginated collection of resources
        in the view if more exist
        """)
    attributes: ArtistsViewsArtistsFeaturedPlaylistsViewAttributes = Field(
        None, alias="attributes", description="The attributes for the view.")
    data: list[Playlists] = Field(
        None, alias="data", description="Relevant playlists associated with the artist.")


class ArtistsViewsArtistsCompilationAlbumsView(BaseModel):
    """
    A relationship view from this artist to albums associated with
    the artist categorized as compilations
    """
    href: str | None = Field(
        None, alias="href", description="A relative location for the view.")
    next: str | None = Field(
        None, alias="next", 
        description="""
        A relative cursor to fetch the next paginated collection of resources
        in the view if more exist
        """)
    attributes: ArtistsViewsArtistsCompilationAlbumsViewAttributes = Field(
        None, alias="attributes", description="The attributes for the view.")
    data: list[Albums] = Field(
        None, alias="data", 
        description="""
        Albums associated with the artist categorized as compilations
        """)


class SearchResponseResultsStationsSearchResult(BaseModel):
    """An object containing a stations’ search result."""
    data: list[Stations] = Field(
        None, alias="data", description="The resources for the search result.")
    href: str | None = Field(
        None, alias="href", description="The relative location to fetch the search result.")
    next: str | None = Field(
        None, alias="next", 
        description="""
        A relative cursor to fetch the next paginated collection of resources
        in the result, if more exist
        """)


class SearchResponseResultsCuratorsSearchResult(BaseModel):
    """An object containing a curators’ search result."""
    data: list[Curators] = Field(
        None, alias="data", description="The resources for the search result.")
    href: str | None = Field(
        None, alias="href", description="The relative location to fetch the search result.")
    next: str | None = Field(
        None, alias="next", 
        description="""
        A relative cursor to fetch the next paginated collection of resources
        in the result, if more exist
        """)


class SongsRelationshipsSongsGenresRelationship(BaseModel):
    """A relationship from the song to its genres."""
    href: str | None = Field(
        None, alias="href", description="A relative location for the relationship.")
    next: str | None = Field(
        None, alias="next", 
        description="""
        A relative cursor to fetch the next paginated collection of resources
        in the relationship if more exist
        """)
    data: list[Genres] = Field(
        None, alias="data", description="The genres associated with the song.")


class SongsRelationshipsSongsAlbumsRelationship(BaseModel):
    """A relationship from the song to its albums."""
    href: str | None = Field(
        None, alias="href", description="A relative location for the relationship.")
    next: str | None = Field(
        None, alias="next", 
        description="""
        A relative cursor to fetch the next paginated collection of resources
        in the relationship if more exist
        """)
    data: list[Albums] = Field(
        None, alias="data", description="The albums associated with the song.")


class SearchResponseResultsPlaylistsSearchResult(BaseModel):
    """An object containing a playlists’ search result."""
    data: list[Playlists] = Field(
        None, alias="data", description="The resources for the search result.")
    href: str | None = Field(
        None, alias="href", description="The relative location to fetch the search result.")
    next: str | None = Field(
        None, alias="next", 
        description="""
        A relative cursor to fetch the next paginated collection of resources
        in the result, if more exist
        """)


class LibraryPlaylistsTracksRelationshipResponse(BaseModel):
    """
    The response to a library playlists tracks relationship request
    """
    data: list[LibraryMusicVideos | LibrarySongs] = Field(
        None, alias="data", 
        description="""
        The Songs or Music Videos included in the response for the request
        """)
    meta: LibraryPlaylistsTracksRelationshipResponseMeta | None = Field(
        None, alias="meta", description="Meta data for this object.")
    next: str | None = Field(
        None, alias="next", 
        description="""
        The relative location to request the next page of resources in
        the collection, if additional resources are available for fetching
        """)


class PlaylistsViewsPlaylistsFeaturedArtistsView(BaseModel):
    """Artists that are featured on this playlist."""
    href: str | None = Field(
        None, alias="href", description="A relative location for the view.")
    next: str | None = Field(
        None, alias="next", 
        description="""
        A relative cursor to fetch the next paginated collection of resources
        in the view if more exist
        """)
    attributes: PlaylistsViewsPlaylistsFeaturedArtistsViewAttributes = Field(
        None, alias="attributes", description="The attribute metadata for the view.")
    data: list[Artists] = Field(
        None, alias="data", description="A paginated collection of resources in the view.")


class MusicVideosViewsMusicVideosMoreInGenreView(BaseModel):
    """
    A relationship view from this music video to more music videos
    in a specific music video genre
    """
    href: str | None = Field(
        None, alias="href", description="A relative location for the view.")
    next: str | None = Field(
        None, alias="next", 
        description="""
        A relative cursor to fetch the next paginated collection of resources
        in the view if more exist
        """)
    attributes: MusicVideosViewsMusicVideosMoreInGenreViewAttributes = Field(
        None, alias="attributes", description="The attributes for the view.")
    data: list[MusicVideos] = Field(
        None, alias="data", description="Music videos in the given music video genre.")


class SongsRelationshipsSongsStationRelationship(BaseModel):
    """A relationship from the song to its station."""
    href: str | None = Field(
        None, alias="href", description="A relative location for the relationship.")
    next: str | None = Field(
        None, alias="next", 
        description="""
        A relative cursor to fetch the next paginated collection of resources
        in the relationship if more exist
        """)
    data: list[Stations] = Field(
        None, alias="data", description="The radio station associated with the song.")


class SongsRelationshipsSongsLibraryRelationship(BaseModel):
    """A relationship from the song to its library."""
    href: str | None = Field(
        None, alias="href", description="A relative location for the relationship.")
    next: str | None = Field(
        None, alias="next", 
        description="""
        A relative cursor to fetch the next paginated collection of resources
        in the relationship if more exist
        """)
    data: list[LibrarySongs] = Field(
        None, alias="data", description="The library associated with the song.")


class SongsRelationshipsSongsArtistsRelationship(BaseModel):
    """A relationship from the song to its artists."""
    href: str | None = Field(
        None, alias="href", description="A relative location for the relationship.")
    next: str | None = Field(
        None, alias="next", 
        description="""
        A relative cursor to fetch the next paginated collection of resources
        in the relationship if more exist
        """)
    data: list[Artists] = Field(
        None, alias="data", description="The artists associated with the song.")


class ArtistsViewsArtistsFeaturedMusicVideosView(BaseModel):
    """
    A relationship view from this artist to a collection of music
    videos selected as featured for the artist
    """
    attributes: ArtistsViewsArtistsFeaturedMusicVideosViewAttributes = Field(
        None, alias="attributes", description="The attributes for the view.")
    data: list[MusicVideos] = Field(
        None, alias="data", 
        description="""
        A collection of music videos selected as featured for the artist
        """)
    href: str | None = Field(
        None, alias="href", description="A relative location for the view.")
    next: str | None = Field(
        None, alias="next", 
        description="""
        A relative cursor to fetch the next paginated collection of resources
        in the view if more exist
        """)


class SearchResponseResultsActivitiesSearchResult(BaseModel):
    """An object containing an activities’ search result."""
    data: list[Activities] = Field(
        None, alias="data", description="The resources for the search result.")
    href: str | None = Field(
        None, alias="href", description="The relative location to fetch the search result.")
    next: str | None = Field(
        None, alias="next", 
        description="""
        A relative cursor to fetch the next paginated collection of resources
        in the result, if more exist
        """)


class MusicVideosViewsMusicVideosMoreByArtistView(BaseModel):
    """
    A relationship view from this music video to more music videos
    of various types by the artist
    """
    href: str | None = Field(
        None, alias="href", description="A relative location for the view.")
    next: str | None = Field(
        None, alias="next", 
        description="""
        A relative cursor to fetch the next paginated collection of resources
        in the view if more exist
        """)
    attributes: MusicVideosViewsMusicVideosMoreByArtistViewAttributes = Field(
        None, alias="attributes", description="The attributes for the view.")
    data: list[MusicVideos] = Field(
        None, alias="data", description="Music videos of some type by the artist.")


class AlbumsRelationshipsAlbumsTracksRelationship(BaseModel):
    """A relationship from the album to its tracks."""
    data: list[MusicVideos | Songs] = Field(
        None, alias="data", 
        description="""
        The ordered songs and music videos in the tracklist of the album
        """)
    href: str | None = Field(
        None, alias="href", description="A relative location for the relationship.")
    next: str | None = Field(
        None, alias="next", 
        description="""
        A relative cursor to fetch the next paginated collection of resources
        in the relationship if more exist
        """)


class AlbumsRelationshipsAlbumsGenresRelationship(BaseModel):
    """A relationship from the album to its genres. """
    href: str | None = Field(
        None, alias="href", description="The relative location to fetch the relationship directly.")
    next: str | None = Field(
        None, alias="next", 
        description="""
        The relative location to request the next page of resources in
        the collection, if additional resources are available for fetching
        """)
    data: list[Genres] = Field(
        None, alias="data", description="The album’s associated genre.")


class RecordLabelsViewsRecordLabelsTopReleasesView(BaseModel):
    """
    A relationship view from this record label to a selection of
    its top releases
    """
    href: str | None = Field(
        None, alias="href", description="A relative location for the view.")
    next: str | None = Field(
        None, alias="next", 
        description="""
        A relative cursor to fetch the next paginated collection of resources
        in the view if more exist
        """)
    attributes: RecordLabelsViewsRecordLabelsTopReleasesViewAttributes = Field(
        None, alias="attributes", description="The attributes for the view.")
    data: list[Albums] = Field(
        None, alias="data", description="A selection of top releases from this record label.")


class SearchResponseResultsMusicVideosSearchResult(BaseModel):
    """An object containing a music videos’ search result."""
    data: list[MusicVideos] = Field(
        None, alias="data", description="The resources for the search result.")
    href: str | None = Field(
        None, alias="href", description="The relative location to fetch the search result.")
    next: str | None = Field(
        None, alias="next", 
        description="""
        A relative cursor to fetch the next paginated collection of resources
        in the result, if more exist
        """)


class SongsRelationshipsSongsComposersRelationship(BaseModel):
    """A relationship from the song to its composers."""
    href: str | None = Field(
        None, alias="href", description="A relative location for the relationship.")
    next: str | None = Field(
        None, alias="next", 
        description="""
        A relative cursor to fetch the next paginated collection of resources
        in the relationship if more exist
        """)
    data: list[Artists] = Field(
        None, alias="data", description="The composers associated with the song.")


class AlbumsRelationshipsAlbumsLibraryRelationship(BaseModel):
    """
    A relationship from the album to an associated library album
    """
    href: str | None = Field(
        None, alias="href", description="The relative location to fetch the relationship directly.")
    next: str | None = Field(
        None, alias="next", 
        description="""
        The relative location to request the next page of resources in
        the collection, if additional resources are available for fetching
        """)
    data: list[LibraryAlbums] = Field(
        None, alias="data", 
        description="""
        The library content this album is associated with if added to
        the user’s library
        """)


class AlbumsRelationshipsAlbumsArtistsRelationship(BaseModel):
    """A relationship from the album to its artists."""
    href: str | None = Field(
        None, alias="href", description="The relative location to fetch the relationship directly.")
    next: str | None = Field(
        None, alias="next", 
        description="""
        The relative location to request the next page of resources in
        the collection, if additional resources are available for fetching
        """)
    data: list[Artists] = Field(
        None, alias="data", description="The artists for the album.")


class SearchResponseResultsRecordLabelsSearchResult(BaseModel):
    """An object containing a record labels’ search result."""
    data: list[RecordLabels] = Field(
        None, alias="data", description="The resources for the search result.")
    href: str | None = Field(
        None, alias="href", description="The relative location to fetch the search result.")
    next: str | None = Field(
        None, alias="next", 
        description="""
        A relative cursor to fetch the next paginated collection of resources
        in the result, if more exist
        """)


class ArtistsRelationshipsArtistsGenresRelationship(BaseModel):
    """A relationship from the artist to its genres."""
    href: str | None = Field(
        None, alias="href", description="A relative location for the relationship.")
    next: str | None = Field(
        None, alias="next", 
        description="""
        A relative cursor to fetch the next paginated collection of resources
        in the relationship if more exist
        """)
    data: list[Genres] = Field(
        None, alias="data", description="The artist’s associated genres.")


class ArtistsRelationshipsArtistsAlbumsRelationship(BaseModel):
    """A relationship from the artist to its albums."""
    href: str | None = Field(
        None, alias="href", description="A relative location for the relationship.")
    next: str | None = Field(
        None, alias="next", 
        description="""
        A relative cursor to fetch the next paginated collection of resources
        in the relationship if more exist
        """)
    data: list[Albums] = Field(
        None, alias="data", description="The albums for the artist.")


class RatingsRelationshipsRatingsContentRelationship(BaseModel):
    """
    A relationship between the rating and the assocaited content
    """
    data: list[Albums | LibraryMusicVideos | LibraryPlaylists | LibrarySongs | MusicVideos | Playlists | Songs | Stations] = Field(
        None, alias="data", description="The content associated with the rating.")
    href: str | None = Field(
        None, alias="href", description="A relative location for the relationship.")
    next: str | None = Field(
        None, alias="next", 
        description="""
        A relative cursor to fetch the next paginated collection of resources
        in the relationship if more exist
        """)


class SearchResponseResultsAppleCuratorsSearchResult(BaseModel):
    """An object containing the Apple curators’ search result."""
    data: list[AppleCurators] = Field(
        None, alias="data", description="The resources for the search result.")
    href: str | None = Field(
        None, alias="href", description="The relative location to fetch the search result.")
    next: str | None = Field(
        None, alias="next", 
        description="""
        A relative cursor to fetch the next paginated collection of resources
        in the result, if more exist
        """)


class SongsRelationshipsSongsMusicVideosRelationship(BaseModel):
    """A relationship from the song to its music videos."""
    href: str | None = Field(
        None, alias="href", description="A relative location for the relationship.")
    next: str | None = Field(
        None, alias="next", 
        description="""
        A relative cursor to fetch the next paginated collection of resources
        in the relationship if more exist
        """)
    data: list[MusicVideos] = Field(
        None, alias="data", description="The music videos associated with the song.")


class ArtistsRelationshipsArtistsStationRelationship(BaseModel):
    """A relationship from the artist to its station."""
    href: str | None = Field(
        None, alias="href", description="A relative location for the relationship.")
    next: str | None = Field(
        None, alias="next", 
        description="""
        A relative cursor to fetch the next paginated collection of resources
        in the relationship if more exist
        """)
    data: list[Stations] = Field(
        None, alias="data", description="The station for the artist.")


class RecordLabelsViewsRecordLabelsLatestReleasesView(BaseModel):
    """
    A relationship view from this record label to a selection of
    its latest releases
    """
    href: str | None = Field(
        None, alias="href", description="A relative location for the view.")
    next: str | None = Field(
        None, alias="next", 
        description="""
        A relative cursor to fetch the next paginated collection of resources
        in the view if more exist
        """)
    attributes: RecordLabelsViewsRecordLabelsLatestReleasesViewAttributes = Field(
        None, alias="attributes", description="The attributes for the view.")
    data: list[Albums] = Field(
        None, alias="data", description="A selection of latest releases from this record label.")


class ArtistsRelationshipsArtistsPlaylistsRelationship(BaseModel):
    """A relationship from the artist to its playlists."""
    href: str | None = Field(
        None, alias="href", description="A relative location for the relationship.")
    next: str | None = Field(
        None, alias="next", 
        description="""
        A relative cursor to fetch the next paginated collection of resources
        in the relationship if more exist
        """)
    data: list[Playlists] = Field(
        None, alias="data", description="The playlists for the artist.")


class PlaylistsRelationshipsPlaylistsTracksRelationship(BaseModel):
    """A relationship from the playlist to its tracks. """
    href: str | None = Field(
        None, alias="href", description="A relative location for the relationship.")
    next: str | None = Field(
        None, alias="next", 
        description="""
        A relative cursor to fetch the next paginated collection of resources
        in the relationship if more exist
        """)
    data: list[MusicVideos | Songs] = Field(
        None, alias="data", 
        description="""
        The ordered songs and music videos in the tracklist of the playlist
        """)


class AlbumsRelationshipsAlbumsRecordLabelsRelationship(BaseModel):
    """
    A relationship from the album to its associated record label
    """
    href: str | None = Field(
        None, alias="href", description="The relative location to fetch the relationship directly.")
    next: str | None = Field(
        None, alias="next", 
        description="""
        The relative location to request the next page of resources in
        the collection, if additional resources are available for fetching
        """)
    data: list[RecordLabels] = Field(
        None, alias="data", description="The album’s associated record label.")


class CuratorsRelationshipsCuratorsPlaylistsRelationship(BaseModel):
    """A relationship from the curator to its playlists."""
    href: str | None = Field(
        None, alias="href", description="A relative location for the relationship.")
    next: str | None = Field(
        None, alias="next", 
        description="""
        A relative cursor to fetch the next paginated collection of resources
        in the relationship if more exist
        """)
    data: list[Playlists] = Field(
        None, alias="data", description="The playlists for the curator.")


class StationsRelationshipsStationsRadioShowRelationship(BaseModel):
    """
    For radio show episodes, this relationship is the Apple Curator
    that represents the radio show
    """
    data: list[AppleCurators] = Field(
        None, alias="data", description="A collection of resources in the relationship.")
    href: str | None = Field(
        None, alias="href", 
        description="""
        A relative location to fetch the relationship, if it may be fetched
        directly
        """)
    next: str | None = Field(
        None, alias="next", 
        description="""
        A relative cursor to fetch the next paginated collection of resources
        in the relationship if more exist
        """)


class PlaylistsRelationshipsPlaylistsLibraryRelationship(BaseModel):
    """A relationship from the playlist to its library."""
    href: str | None = Field(
        None, alias="href", description="A relative location for the relationship.")
    next: str | None = Field(
        None, alias="next", 
        description="""
        A relative cursor to fetch the next paginated collection of resources
        in the relationship if more exist
        """)
    data: list[LibraryPlaylists] = Field(
        None, alias="data", description="The library for the playlist.")


class PlaylistsRelationshipsPlaylistsCuratorRelationship(BaseModel):
    """A relationship from the playlist to its curator."""
    href: str | None = Field(
        None, alias="href", description="A relative location for the relationship.")
    next: str | None = Field(
        None, alias="next", 
        description="""
        A relative cursor to fetch the next paginated collection of resources
        in the relationship if more exist
        """)
    data: list[Activities | AppleCurators | Curators] = Field(
        None, alias="data", description="The curator for the playlist.")


class ArtistsRelationshipsArtistsMusicVideosRelationship(BaseModel):
    """A relationship from the artist to its music videos."""
    href: str | None = Field(
        None, alias="href", description="A relative location for the relationship.")
    next: str | None = Field(
        None, alias="next", 
        description="""
        A relative cursor to fetch the next paginated collection of resources
        in the relationship if more exist
        """)
    data: list[MusicVideos] = Field(
        None, alias="data", description="The music videos for the artist.")


class LibrarySearchResponseResultsLibrarySongsSearchResult(BaseModel):
    """
    The library songs results for a term search for specific resource
    types
    """
    data: list[LibrarySongs] = Field(
        None, alias="data", 
        description="""
        The library song resources matching the search term, ordered
        by best match
        """)
    href: str | None = Field(
        None, alias="href", description="A relative location for the resource.")
    next: str | None = Field(
        None, alias="next", 
        description="""
        A relative cursor to fetch the next paginated collection of resources
        if more exist
        """)


class MusicVideosRelationshipsMusicVideosSongsRelationship(BaseModel):
    """A relationship from the music video to its songs."""
    href: str | None = Field(
        None, alias="href", description="A relative location for the relationship.")
    next: str | None = Field(
        None, alias="next", 
        description="""
        A relative cursor to fetch the next paginated collection of resources
        in the relationship if more exist
        """)
    data: list[Songs] = Field(
        None, alias="data", description="The songs associated with the music video.")


class LibrarySearchResponseResultsLibraryAlbumsSearchResult(BaseModel):
    """
    The library albums results for a term search for specific resource
    types
    """
    data: list[LibraryAlbums] = Field(
        None, alias="data", 
        description="""
        The library album resources matching the search term, ordered
        by best match
        """)
    href: str | None = Field(
        None, alias="href", description="A relative location for the resource.")
    next: str | None = Field(
        None, alias="next", 
        description="""
        A relative cursor to fetch the next paginated collection of resources
        if more exist
        """)


class MusicVideosRelationshipsMusicVideosGenresRelationship(BaseModel):
    """A relationship from the music video to its genres."""
    href: str | None = Field(
        None, alias="href", description="A relative location for the relationship.")
    next: str | None = Field(
        None, alias="next", 
        description="""
        A relative cursor to fetch the next paginated collection of resources
        in the relationship if more exist
        """)
    data: list[Genres] = Field(
        None, alias="data", description="The genres associated with the music video.")


class MusicVideosRelationshipsMusicVideosAlbumsRelationship(BaseModel):
    """A relationship from the music video to its albums."""
    href: str | None = Field(
        None, alias="href", description="A relative location for the relationship.")
    next: str | None = Field(
        None, alias="next", 
        description="""
        A relative cursor to fetch the next paginated collection of resources
        in the relationship if more exist
        """)
    data: list[Albums] = Field(
        None, alias="data", description="The albums associated with the music video, if any.")


class ActivitiesRelationshipsActivitiesPlaylistsRelationship(BaseModel):
    """A relationship between the activity and its playlists."""
    href: str | None = Field(
        None, alias="href", description="A relative location for the relationship.")
    next: str | None = Field(
        None, alias="next", 
        description="""
        A relative cursor to fetch the next paginated collection of resources
        in the relationship if more exist
        """)
    data: list[Playlists] = Field(
        None, alias="data", description="The playlists associated with this activity.")


class LibrarySearchResponseResultsLibraryArtistsSearchResult(BaseModel):
    """
    The library artists results for a term search for specific resource
    types
    """
    data: list[LibraryArtists] = Field(
        None, alias="data", 
        description="""
        The library artist resources matching the search term, ordered
        by best match
        """)
    href: str | None = Field(
        None, alias="href", description="A relative location for the resource.")
    next: str | None = Field(
        None, alias="next", 
        description="""
        A relative cursor to fetch the next paginated collection of resources
        if more exist
        """)


class MusicVideosRelationshipsMusicVideosLibraryRelationship(BaseModel):
    """A relationship from the music video to its library."""
    href: str | None = Field(
        None, alias="href", description="A relative location for the relationship.")
    next: str | None = Field(
        None, alias="next", 
        description="""
        A relative cursor to fetch the next paginated collection of resources
        in the relationship if more exist
        """)
    data: list[LibraryMusicVideos] = Field(
        None, alias="data", description="The library associated with the music video, if any.")


class MusicVideosRelationshipsMusicVideosArtistsRelationship(BaseModel):
    """A relationship from the music video to its artists."""
    href: str | None = Field(
        None, alias="href", description="A relative location for the relationship.")
    next: str | None = Field(
        None, alias="next", 
        description="""
        A relative cursor to fetch the next paginated collection of resources
        in the relationship if more exist
        """)
    data: list[Artists] = Field(
        None, alias="data", description="The artists associated with the music video.")


class LibrarySongsRelationshipsLibrarySongsAlbumsRelationship(BaseModel):
    """A relationship from the library song to its albums."""
    href: str | None = Field(
        None, alias="href", description="A relative location for the relationship.")
    next: str | None = Field(
        None, alias="next", 
        description="""
        A relative cursor to fetch the next paginated collection of resources
        in the relationship if more exist
        """)
    data: list[LibraryAlbums] = Field(
        None, alias="data", description="The albums in the library associated with the song.")


class LibrarySearchResponseResultsLibraryPlaylistsSearchResult(BaseModel):
    """
    The library playlists results for a term search for specific
    resource types
    """
    data: list[LibraryPlaylists] = Field(
        None, alias="data", 
        description="""
        The library playlist resources matching the search term, ordered
        by best match
        """)
    href: str | None = Field(
        None, alias="href", description="A relative location for the resource.")
    next: str | None = Field(
        None, alias="next", 
        description="""
        A relative cursor to fetch the next paginated collection of resources
        if more exist
        """)


class LibrarySongsRelationshipsLibrarySongsCatalogRelationship(BaseModel):
    """
    A relationship from the library song to its associated catalog
    content
    """
    href: str | None = Field(
        None, alias="href", description="A relative location for the relationship.")
    next: str | None = Field(
        None, alias="next", 
        description="""
        A relative cursor to fetch the next paginated collection of resources
        in the relationship if more exist
        """)
    data: list[Songs] = Field(
        None, alias="data", 
        description="""
        The song from the Apple Music catalog associated with the library
        song, if any
        """)


class LibrarySongsRelationshipsLibrarySongsArtistsRelationship(BaseModel):
    """A relationship from the library song to its artists."""
    href: str | None = Field(
        None, alias="href", description="A relative location for the relationship.")
    next: str | None = Field(
        None, alias="next", 
        description="""
        A relative cursor to fetch the next paginated collection of resources
        in the relationship if more exist
        """)
    data: list[LibraryArtists] = Field(
        None, alias="data", description="The artists in the library associated with the song.")


class LibraryAlbumsRelationshipsLibraryAlbumsTracksRelationship(BaseModel):
    """A relationship from the library album to its tracks."""
    href: str | None = Field(
        None, alias="href", description="The relative location to fetch the relationship directly.")
    next: str | None = Field(
        None, alias="next", 
        description="""
        The relative location to request the next page of resources in
        the collection, if additional resources are available for fetching
        """)
    data: list[LibraryMusicVideos | LibrarySongs] = Field(
        None, alias="data", 
        description="""
        The songs and music videos from the library album’s tracklist
        added to the user’s library
        """)


class LibrarySearchResponseResultsLibraryMusicVideosSearchResult(BaseModel):
    """
    The library music videos results for a term search for specific
    resource types
    """
    data: list[LibraryMusicVideos] = Field(
        None, alias="data", 
        description="""
        The library music video resources matching the search term, ordered
        by best match
        """)
    href: str | None = Field(
        None, alias="href", description="A relative location for the resource.")
    next: str | None = Field(
        None, alias="next", 
        description="""
        A relative cursor to fetch the next paginated collection of resources
        if more exist
        """)


class LibraryAlbumsRelationshipsLibraryAlbumsCatalogRelationship(BaseModel):
    """
    A relationship from the library album to its associated catalog
    content
    """
    href: str | None = Field(
        None, alias="href", description="The relative location to fetch the relationship directly.")
    next: str | None = Field(
        None, alias="next", 
        description="""
        The relative location to request the next page of resources in
        the collection, if additional resources are available for fetching
        """)
    data: list[Albums] = Field(
        None, alias="data", 
        description="""
        The album from the Apple Music catalog associated with the library
        album, if any
        """)


class LibraryAlbumsRelationshipsLibraryAlbumsArtistsRelationship(BaseModel):
    """A relationship from the library album to its artist."""
    href: str | None = Field(
        None, alias="href", description="The relative location to fetch the relationship directly.")
    next: str | None = Field(
        None, alias="next", 
        description="""
        The relative location to request the next page of resources in
        the collection, if additional resources are available for fetching
        """)
    data: list[LibraryArtists] = Field(
        None, alias="data", description="The library artists for the library album.")


class StationGenresRelationshipsStationGenresStationsRelationship(BaseModel):
    """
    A relationship from the station genre to associated stations
    """
    href: str | None = Field(
        None, alias="href", description="A relative location for the relationship.")
    next: str | None = Field(
        None, alias="next", 
        description="""
        A relative cursor to fetch the next paginated collection of resources
        in the relationship if more exist
        """)
    data: list[Stations] = Field(
        None, alias="data", description="Stations associated with the station genre.")


class LibraryArtistsRelationshipsLibraryArtistsAlbumsRelationship(BaseModel):
    """A relationship from the library artist to thier albums."""
    href: str | None = Field(
        None, alias="href", description="A relative location for the relationship.")
    next: str | None = Field(
        None, alias="next", 
        description="""
        A relative cursor to fetch the next paginated collection of resources
        in the relationship if more exist
        """)
    data: list[LibraryAlbums] = Field(
        None, alias="data", 
        description="""
        The albums for the library artist present in the user’s library
        """)


class AppleCuratorsRelationshipsAppleCuratorsPlaylistsRelationship(BaseModel):
    """A relationship from the Apple curator to its playlists."""
    href: str | None = Field(
        None, alias="href", description="A relative location for the relationship.")
    next: str | None = Field(
        None, alias="next", 
        description="""
        A relative cursor to fetch the next paginated collection of resources
        in the relationship if more exist
        """)
    data: list[Playlists] = Field(
        None, alias="data", description="The playlists for the curator.")


class LibraryArtistsRelationshipsLibraryArtistsCatalogRelationship(BaseModel):
    """
    A relationship from the library artist to their associated catalog
    content
    """
    href: str | None = Field(
        None, alias="href", description="A relative location for the relationship.")
    next: str | None = Field(
        None, alias="next", 
        description="""
        A relative cursor to fetch the next paginated collection of resources
        in the relationship if more exist
        """)
    data: list[Artists] = Field(
        None, alias="data", 
        description="""
        The artist from the Apple Music catalog associated with the library
        artist, if any
        """)


class LibraryPlaylistsRelationshipsLibraryPlaylistsTracksRelationship(BaseModel):
    """A relationship from the playlist to its tracks."""
    href: str | None = Field(
        None, alias="href", description="A relative location for the relationship.")
    next: str | None = Field(
        None, alias="next", 
        description="""
        A relative cursor to fetch the next paginated collection of resources
        in the relationship if more exist
        """)
    data: list[LibraryMusicVideos | LibrarySongs] = Field(
        None, alias="data", 
        description="""
        The ordered library songs and library music videos in the tracklist
        of the playlist
        """)


class LibraryPlaylistsRelationshipsLibraryPlaylistsCatalogRelationship(BaseModel):
    """
    A relationship from the playlist to its associated catalog content
    """
    href: str | None = Field(
        None, alias="href", description="A relative location for the relationship.")
    next: str | None = Field(
        None, alias="next", 
        description="""
        A relative cursor to fetch the next paginated collection of resources
        in the relationship if more exist
        """)
    data: list[Playlists] = Field(
        None, alias="data", 
        description="""
        The playlist from the Apple Music catalog associated with the
        library playlist, if any
        """)


class LibraryMusicVideosRelationshipsLibraryMusicVideosAlbumsRelationship(BaseModel):
    """
    A relationship from the library music video to its albums in
    the library
    """
    href: str | None = Field(
        None, alias="href", description="A relative location for the relationship.")
    next: str | None = Field(
        None, alias="next", 
        description="""
        A relative cursor to fetch the next paginated collection of resources
        in the relationship if more exist
        """)
    data: list[LibraryAlbums] = Field(
        None, alias="data", 
        description="""
        The albums in the library the music video is associated with,
        if any
        """)


class LibraryMusicVideosRelationshipsLibraryMusicVideosCatalogRelationship(BaseModel):
    """
    A relationship from the library music video to its associated
    catalog content
    """
    href: str | None = Field(
        None, alias="href", description="A relative location for the relationship.")
    next: str | None = Field(
        None, alias="next", 
        description="""
        A relative cursor to fetch the next paginated collection of resources
        in the relationship if more exist
        """)
    data: list[MusicVideos] = Field(
        None, alias="data", 
        description="""
        The music video from the Apple Music catalog associated with
        the library music video, if any
        """)


class LibraryMusicVideosRelationshipsLibraryMusicVideosArtistsRelationship(BaseModel):
    """
    A relationship from the library music video to its artists in
    the library
    """
    href: str | None = Field(
        None, alias="href", description="A relative location for the relationship.")
    next: str | None = Field(
        None, alias="next", 
        description="""
        A relative cursor to fetch the next paginated collection of resources
        in the relationship if more exist
        """)
    data: list[LibraryArtists] = Field(
        None, alias="data", 
        description="""
        The artists in the library the music video is associated with
        """)


class LibraryPlaylistFoldersRelationshipsLibraryPlaylistFoldersParentRelationship(BaseModel):
    """
    A resource object that represents the parent relationship of
    a library playlist folder
    """
    href: str | None = Field(
        None, alias="href", description="The relative location for the parent relationship.")
    next: str | None = Field(
        None, alias="next", 
        description="""
        A relative cursor to fetch the next paginated collection of resources
        in the relationship if more exist
        """)
    data: list[LibraryPlaylistFolders] = Field(
        None, alias="data", description="The parent of the library playlist, if it exists.")


class PersonalRecommendationRelationshipsPersonalRecommendationContentsRelationship(BaseModel):
    """
    A relationship from the recommendation to its recommended content
    """
    href: str | None = Field(
        None, alias="href", description="A relative location for the relationship.")
    next: str | None = Field(
        None, alias="next", 
        description="""
        A relative cursor to fetch the next paginated collection of resources
        in the relationship if more exist
        """)
    data: list[Resource] = Field(
        None, alias="data", 
        description="""
        A list of recommended candidates that are a mixture of albums
        and playlists
        """)


class LibraryPlaylistFoldersRelationshipsLibraryPlaylistFoldersChildrenRelationship(BaseModel):
    """
    A resource object that represents the children relationship of
    a library playlist folder
    """
    href: str | None = Field(
        None, alias="href", description="The relative location for the children relationship.")
    next: str | None = Field(
        None, alias="next", 
        description="""
        A relative cursor to fetch the next paginated collection of resources
        in the relationship if more exist
        """)
    data: list[LibraryPlaylistFolders | LibraryPlaylists] = Field(
        None, alias="data", description="The children of the library playlist, if any exist.")
