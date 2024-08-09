
"""
IPython extension for notifying with ntfy.

This module provides the NotifyMagics class and functions for creating topics
and registering the extension as an IPython magic extension.
"""
from .notify import NotifyMagics
from .utils import create_topic


def load_ipython_extension(ipython):
    """
    Registers the NotifyMagics class as an IPython extension.

    Args:
        ipython (IPython): The IPython instance to register the magics with.
    """
    ipython.register_magics(NotifyMagics)
