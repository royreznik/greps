# mypy: disable-error-code="no-untyped-call"
from IPython.terminal.interactiveshell import TerminalInteractiveShell


def test_magic_without_line(ip: TerminalInteractiveShell) -> None:
    ip.run_cell("'reznik'", store_history=True)
    result = ip.run_cell("%greps rez").result
    assert result == "'reznik'\n"


def test_magic_with_line(ip: TerminalInteractiveShell) -> None:
    ip.run_cell("'one'", store_history=True)
    ip.run_cell("'two'", store_history=True)
    ip.run_cell("'three'", store_history=True)
    result = ip.run_cell("%greps -l 2 tw").result
    assert result == "'two'\n"


def test_magic_with_grep_arguments(ip: TerminalInteractiveShell) -> None:
    ip.run_cell(r"'Im Reznik!\n123'", store_history=True)
    result = ip.run_cell("%greps -- -P 'R.*!'").result
    assert result == "'Im Reznik!\n"


def test_magic_with_no_history(ip: TerminalInteractiveShell) -> None:
    exception = ip.run_cell("%greps 'Not existing'").error_in_exec
    assert isinstance(exception, ValueError)
    assert "Output history is empty" in exception.args


def test_magic_with_invalid_line_number(ip: TerminalInteractiveShell) -> None:
    exception = ip.run_cell("%greps -l 240 'Not existing'").error_in_exec
    assert isinstance(exception, ValueError)
    assert "There is no output for line: 240" in exception.args
