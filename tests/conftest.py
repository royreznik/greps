from typing import Generator

import pytest
from IPython.conftest import get_ipython
from IPython.terminal.interactiveshell import TerminalInteractiveShell
from greps import load_ipython_extension


@pytest.fixture
def ip() -> Generator[TerminalInteractiveShell, None, None]:
    ipython = get_ipython()  # type: ignore[no-untyped-call]
    load_ipython_extension(ipython)

    yield ipython
    TerminalInteractiveShell.clear_instance()
