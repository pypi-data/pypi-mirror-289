import subprocess
import shlex,json,os
from typing import Callable, Any
class Console:
    """A class that provides various console-related utility methods."""
    @staticmethod
    def pipinstall(cmd: str) -> Callable[[], None]:
        cmd=cmd
        def install(b):
            # 读取进度
            if os.path.exists("pipinstall.json"):
                with open("pipinstall.json", 'r') as f:
                    progress = json.load(f)
            else:
                progress = {}

            # 如果已经安装过了，直接返回
            if cmd in progress and progress[cmd] == "installed":
                print(f"{cmd} 已經安裝過了，跳過。")
                return

            if isinstance(cmd, str):
                cmd = shlex.split(cmd)

            try:
                # 安装命令
                subprocess.run(['pip', 'install'] + cmd, check=True)
                progress[cmd] = "installed"
                print(f"{cmd} 安裝成功")
            except subprocess.CalledProcessError as e:
                print(f"安裝 {cmd} 時出現錯誤：{e}")

            # 保存進度
            with open("pipinstall.json", 'w') as f:
                json.dump(progress, f)

        return install

    @staticmethod
    def aptinstall(cmd: str) -> Callable[[], None]:
        cmd=cmd
        def install(b):
            # 读取进度
            if os.path.exists("aptinstall.json"):
                with open("aptinstall.json", 'r') as f:
                    progress = json.load(f)
            else:
                progress = {}

            # 如果已经安装过了，直接返回
            if cmd in progress and progress[cmd] == "installed":
                print(f"{cmd} 已經安裝過了，跳過。")
                return

            if isinstance(cmd, str):
                cmd = shlex.split(cmd)

            try:
                # 安装命令
                subprocess.run(['apt-get', 'install', '-y'] + cmd, check=True)
                progress[cmd] = "installed"
                print(f"{cmd} 安裝成功")
            except subprocess.CalledProcessError:
                # 如果安装失败，检查是否需要重启
                if "reboot required" in subprocess.getoutput('apt-get -q check'):
                    print("安裝需要重啟，保存進度並計劃重啟。")
                    # 保存進度
                    with open("aptinstall.json", 'w') as f:
                        json.dump(progress, f)
                    
                    # 觸發重啟
                    subprocess.run(['reboot'])

            # 如果到這裡，正常保存進度
            with open("aptinstall.json", 'w') as f:
                json.dump(progress, f)

        return install
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
    def run_command(cmd: str) -> Callable[[], str]:
        """
        Returns a function that executes a shell command and returns its output.

        Args:
            cmd (str): The command to be executed.

        Returns:
            Callable[[], str]: A function that, when called, executes the command and returns
                                its stdout if successful, or stderr if an error occurred.
        """
        def execute():
            try:
                result = subprocess.run(cmd, shell=True, check=True, text=True, capture_output=True)
                return result.stdout
            except subprocess.CalledProcessError as e:
                print(f"Error executing command: {cmd}")
                print(f"Error message: {e}")
                return e.stderr
        
        return execute

# Example of usage:
# command_function = QuickColabConsole.run_command("ls -l")
# output = command_function()  # This will execute the command and return the output
# print(output)

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
    def run_command(*arg) -> Callable[[], str]:
        
        def inner_run_command(b):
            for i in arg:
                subprocess.Popen(i, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        return inner_run_command