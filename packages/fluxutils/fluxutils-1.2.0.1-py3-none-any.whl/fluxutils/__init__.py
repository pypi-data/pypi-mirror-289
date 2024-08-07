"""
    fluxutils
    ~~~~~~~~~

    FluxUtils is a powerful, highly customizable, and versatile Python module designed to enhance the efficiency and performance of your programs. Whether you're a seasoned developer or just starting out, FluxUtils offers a suite of tools to streamline your workflow and improve code management. FluxUtils currently enables developers with a simple yet highly customizable logger with support for multiple streams, a set of utility decorators, like @cache and @rate_limiter, and a handful of tools to create a command-line interface with interactive prompts and argument handling.
"""

from . import log, decorators, cli

__version__ = "1.2.0.1"
__all__ = ["log", "decorators", "cli"]
