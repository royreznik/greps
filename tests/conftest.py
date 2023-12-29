from typing import Generator

import pytest
from IPython.conftest import get_ipython
from IPython.terminal.interactiveshell import TerminalInteractiveShell
from greps import Grep


@pytest.fixture
def ip() -> Generator[TerminalInteractiveShell, None, None]:
    ipython = get_ipython()  # type: ignore[no-untyped-call]
    ipython.magics_manager.register(Grep)
    yield ipython
    TerminalInteractiveShell.clear_instance()
