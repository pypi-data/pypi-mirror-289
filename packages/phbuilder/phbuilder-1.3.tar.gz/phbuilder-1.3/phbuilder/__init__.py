# PYTHON_ARGCOMPLETE_OK

def entryFunction():
    """Entry point for phbuilder. When phbuilder is run, this function is
    called first.
    """

    # PYTHON_ARGCOMPLETE_OK

    # Execute this as soon as possible because of the TAB autocomplete thing.
    from .parsecmdline import parsecmdline

    # Parse command line input.
    CLI = parsecmdline()

    # Import everything else.
    from .phbuilder import phbuilder

    # Run main program.
    return phbuilder(CLI).runner()
