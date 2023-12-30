import argparse
import subprocess

from IPython.core.magic import (
    Magics,
    magics_class,
    line_magic,
)

__all__ = ["Grep", "load_ipython_extension"]

from IPython.terminal.interactiveshell import TerminalInteractiveShell


@magics_class
class Grep(Magics):
    @staticmethod
    def get_args_parser() -> argparse.ArgumentParser:
        parser = argparse.ArgumentParser()
        parser.add_argument(
            "-l", "--line", dest="line", type=int, default=None, help="wtf"
        )
        parser.add_argument(
            "grep_args", metavar="grep_args", nargs="+", type=str, help="wtf"
        )
        return parser

    @line_magic  # type: ignore[misc]
    def greps(self, params: str = "") -> str:
        parser = self.get_args_parser()
        args = parser.parse_args(params.split())
        grep_args = " ".join(args.grep_args)
        line = args.line
        assert self.shell, "Shell isn't Initialized"

        if line is None:
            if len(self.shell.history_manager.output_hist_reprs) < 1:
                raise ValueError("Output history is empty")
            output_line = list(
                sorted(self.shell.history_manager.output_hist_reprs.keys())
            )[-1]
        else:
            if line not in self.shell.history_manager.output_hist_reprs:
                raise ValueError(f"There is no output for line: {line}")
            output_line = line

        last_output = self.shell.history_manager.output_hist_reprs[output_line]
        output = subprocess.run(
            f'echo "{last_output}" | grep {grep_args}',
            shell=True,
            stdout=subprocess.PIPE,
            check=False,
        ).stdout.decode()
        return output


def load_ipython_extension(ipython: TerminalInteractiveShell) -> None:
    ipython.register_magics(Grep)  # type: ignore[no-untyped-call]
