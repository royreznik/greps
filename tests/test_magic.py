# mypy: disable-error-code="no-untyped-call"
from IPython.terminal.interactiveshell import TerminalInteractiveShell


def test_magic_without_line(ip: TerminalInteractiveShell) -> None:
    ip.run_cell("'reznik'", store_history=True)
    result = ip.run_cell("%grep rez").result
    assert result == "'reznik'\n"


def test_magic_with_line(ip: TerminalInteractiveShell) -> None:
    ip.run_cell("'one'", store_history=True)
    ip.run_cell("'two'", store_history=True)
    ip.run_cell("'three'", store_history=True)
    result = ip.run_cell("%grep -l 2 tw").result
    assert result == "'two'\n"


def test_magic_with_grep_arguments(ip: TerminalInteractiveShell) -> None:
    ip.run_cell(r"'Im Reznik!\n123'", store_history=True)
    result = ip.run_cell("%grep -- -P 'R.*!'").result
    assert result == "'Im Reznik!\n"
