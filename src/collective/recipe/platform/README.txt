
Limitations:
============

The recipe currently only generates platform strings for darwin10 and darwin9.
Due to the simplicity of the recipe itself, it should not be hard ta add
further platform-prefixes. (Patches and other contributions are welcome).

Example usage
=============

This recipe provides a way of defining buildout variables which can be
referenced form other parts with platform specific values. It does not try
being intelligent and guess what values it should set, but gives the user full
control, with the drawback/advantage of keeping all settings in a single or
multiple configuration sections.

But examples are probably a better explanation:

    >>> write(sample_buildout, 'buildout.cfg',
    ... """
    ... [buildout]
    ... parts = debug
    ...
    ... [platform]
    ... recipe = collective.recipe.platform
    ... environment =
    ... darwin10-environment =
    ...     CC=gcc-4.0
    ... flags =
    ... darwin9-flags =
    ...     CPP=cpp-4.0
    ...
    ... [debug]
    ... recipe = zc.buildout:debug
    ... env = ${platform:environment}
    ... flags = ${platform:flags}
    ... plname = ${platform:platform}
    ... """)

Ok, we have a part called 'debug'. This part just prints all given options
to stdout. In our case it uses values referenced in the platform part.

The platform recipe looks for options starting with a platform prefix, taxes
the remainder of the option name and replaces the value.

The result of a buildout running on OSX 10.6 (darwin10) is the following:

    >>> print system(buildout)
    Installing platform.
    Unused options for platform: 'darwin9-flags'.
    Installing debug.
      env='\nCC=gcc-4.0'
      flags=''
      plname='darwin10'
      recipe='zc.buildout:debug'

