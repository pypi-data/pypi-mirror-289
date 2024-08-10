"""
Module to format the code.
"""

from multiprocessing import Pool

import requests
from rich.progress import track

from auto_dev.cli_executor import CommandExecutor
from auto_dev.constants import DEFAULT_ENCODING


class Formatter:
    """Formatter class to run the formatter."""

    def __init__(self, verbose, remote):
        self.verbose = verbose
        self.remote = remote

    def format(self, path):
        """Format the path."""
        func = self._format_path if not self.remote else self._remote_format_path
        return func(path, verbose=self.verbose)

    def _remote_format_path(self, path, verbose=False):
        """Format the path."""
        # pylint: disable=R1732
        with requests.Session() as session:
            result = session.post(
                "http://localhost:26659/format",
                data=open(path, "rb").read(),
                timeout=150,
            )
        if verbose:
            print(result.json())

        if result.json():
            if 'new_data' in result.json():
                with open(path, "w", encoding=DEFAULT_ENCODING) as file:
                    file.write(result.json()['new_data'])
                return True
            if 'result' in result.json():
                return result.json()['result']

        return False

    def _format_path(self, path, verbose=False):
        """Format the path."""

        results = all(
            [
                self.run_autoflake8(path, verbose=verbose),
                self.run_isort(path, verbose=verbose),
                self.run_black(path, verbose=verbose),
            ]
        )
        return results

    @staticmethod
    def run_black(path, verbose=False):
        """Run black on the path."""
        command = CommandExecutor(
            [
                "poetry",
                "run",
                "black",
                str(path),
            ]
        )
        result = command.execute(verbose=verbose)
        return result

    @staticmethod
    def run_isort(path, verbose=False):
        """Run isort on the path."""
        command = CommandExecutor(
            [
                "poetry",
                "run",
                "isort",
                str(path),
            ]
        )
        result = command.execute(verbose=verbose)
        return result

    @staticmethod
    def run_autoflake8(path, verbose=False):
        """Run autoflake8 on the path."""
        command = CommandExecutor(
            [
                "poetry",
                "run",
                "autoflake8",
                "--remove-unused-variables",
                "--in-place",
                "--recursive",
                str(path),
            ]
        )
        result = command.execute(verbose=verbose)
        return result


def single_thread_fmt(paths, verbose, logger, remote=False):
    """Run the formatting in a single thread."""
    results = {}
    formatter = Formatter(verbose, remote=remote)
    local_formatter = Formatter(verbose, remote=False)
    for package in track(range(len(paths)), description="Formatting..."):
        path = paths[package]
        if verbose:
            logger.info(f"Formatting: {path}")
        result = formatter.format(path)
        if not result:
            logger.error(f"Failed to format {path} remotely, trying locally")
            result = local_formatter.format(path)
        results[package] = result
    return results


def multi_thread_fmt(paths, verbose, num_processes, remote=False):
    """Run the formatting in multiple threads."""
    formatter = Formatter(verbose, remote=remote)
    with Pool(num_processes) as pool:
        results = pool.map(formatter.format, paths)

    # We chekc with the local formatter if the remote formatter fails
    local_formatter = Formatter(verbose, remote=False)
    for i, result in enumerate(results):
        if not result:
            results[i] = local_formatter.format(paths[i])

    return dict(zip(paths, results))
