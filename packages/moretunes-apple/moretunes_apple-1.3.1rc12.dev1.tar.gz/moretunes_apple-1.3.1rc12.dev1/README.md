This is the Apple Music API submodule of the moretunes namespace package.

Moretunes is a namespace package that aims to eventually contain apis for all music streaming 
or otherwise music adjacent services, in a universal, pydantic-ly modeled format. Currently, 
the namespace includes moretunes-spotify, moretunes-apple, and moretunes-youtube, 
each representing their respective service.

Included sub-packages vary in their source and content, 
moretunes-spotify being the most basic of the three, primarily being an addon for the 
already excellent ``tekore`` library with model adaptations and functions for interfacing with
Spotify's web browser apis. moretunes-youtube uses a heavily adapted fork of ``YTMusicAPI``, offering 
more efficient and comprehensive data parsing, PEP8 compliant and moretunes compatible api format, and 
an emphasis on OAuth token authentication. moretunes-apple is a fully original codebase, the focus of which is 
apple documentation parsing and code generation scripts. The resulting package consists of two distinct partitions, 
a raw, fully-generated, pydantic-ly modeled core that mirrors apple's api and documentation 1:1 
and a statically written adapter to the universal moretunes format. 
