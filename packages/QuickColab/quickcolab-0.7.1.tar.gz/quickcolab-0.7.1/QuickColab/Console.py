import subprocess
import shlex
from typing import Callable, Any
from .install_descriptor import AptInstallDescriptor, PipInstallDescriptor

class Console:
    """A class that provides various console-related utility methods."""

    aptinstall = AptInstallDescriptor()
    pipinstall = PipInstallDescriptor()

    @staticmethod
    def print(text: str) -> Callable[[Any], None]:
        """
        Returns a function that prints the given text.

        Args:
            text (str): The text to be printed.

        Returns:
            Callable[[Any], None]: A function that prints the text.
        """
        def inner_print(b):
            print(text)
        return inner_print

    @staticmethod
    def run_command(cmd: str) -> str:
        """
        Executes a shell command and returns its output.

        Args:
            cmd (str): The command to be executed.

        Returns:
            str: The command's stdout if successful, stderr if an error occurred.
        """
        try:
            result = subprocess.run(cmd, shell=True, check=True, text=True, capture_output=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            print(f"Error executing command: {cmd}")
            print(f"Error message: {e}")
            return e.stderr

    @staticmethod
    def update_apt() -> Callable[[], None]:
        """
        Returns a function that updates the apt package lists.

        Returns:
            Callable[[], None]: A function that updates apt package lists.
        """
        def update():
            try:
                subprocess.check_call(['sudo', 'apt-get', 'update'])
                print("Successfully updated apt package lists")
            except subprocess.CalledProcessError as e:
                print("Error updating apt package lists")
                print(f"Error message: {e}")
        return update

    @staticmethod
    def ls(path: str = '.', options: str = '-al') -> Callable[[Any], str]:
        """
        Returns a function that lists directory contents.

        Args:
            path (str): The path to list. Defaults to current directory.
            options (str): The options for the ls command. Defaults to '-al'.

        Returns:
            Callable[[Any], str]: A function that executes the ls command.
        """
        def inner_ls(b):
            return Console.run_command(f"ls {options} {shlex.quote(path)}")
        return inner_ls

    @staticmethod
    def rm(path: str, recursive: bool = False, force: bool = False) -> Callable[[], str]:
        """
        Returns a function that removes files or directories.

        Args:
            path (str): The path to remove.
            recursive (bool): Whether to remove directories and their contents recursively.
            force (bool): Whether to ignore nonexistent files and never prompt.

        Returns:
            Callable[[], str]: A function that executes the rm command.
        """
        options = '-r ' if recursive else ''
        options += '-f ' if force else ''
        def inner_rm(b):
            return Console.run_command(f"rm {options}{shlex.quote(path)}")
        return inner_rm

    @staticmethod
    def cp(source: str, destination: str, recursive: bool = False) -> Callable[[Any], str]:
        """
        Returns a function that copies files or directories.

        Args:
            source (str): The source path.
            destination (str): The destination path.
            recursive (bool): Whether to copy directories recursively.

        Returns:
            Callable[[Any], str]: A function that executes the cp command.
        """
        options = '-r' if recursive else ''
        def inner_cp():
            return Console.run_command(f"cp {options} {shlex.quote(source)} {shlex.quote(destination)}")
        return inner_cp

    @staticmethod
    def mv(source: str, destination: str) -> Callable[[Any], str]:
        """
        Returns a function that moves files or directories.

        Args:
            source (str): The source path.
            destination (str): The destination path.

        Returns:
            Callable[[Any], str]: A function that executes the mv command.
        """
        def inner_mv(b):
            return Console.run_command(f"mv {shlex.quote(source)} {shlex.quote(destination)}")
        return inner_mv

    @staticmethod
    def extract_response(output: str) -> str:
        """
        Extracts the response from the given output string.

        Args:
            output (str): The output string to extract from.

        Returns:
            str: The extracted response or the stripped output if no "Response:" is found.
        """
        if "Response:" in output:
            return output.split("Response:", 1)[1].strip()
        return output.strip()
