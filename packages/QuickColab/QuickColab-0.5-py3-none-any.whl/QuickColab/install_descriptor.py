# install_descriptor.py

import json
import os
import subprocess
import sys
from typing import Union, List
import ipywidgets as widgets
from IPython.display import display

class InstallDescriptor:
    """
    Base class for install descriptors.
    Provides methods for saving, loading, and clearing installation progress.
    """

    PROGRESS_FILE = '/tmp/{}_install_progress.json'

    @staticmethod
    def _save_progress(installer_type: str, packages: List[str], current_index: int):
        """
        Save the current installation progress to a file.

        Args:
            installer_type (str): Type of installer (e.g., 'apt', 'pip')
            packages (List[str]): List of packages being installed
            current_index (int): Index of the current package in the installation process
        """
        with open(InstallDescriptor.PROGRESS_FILE.format(installer_type), 'w') as f:
            json.dump({'packages': packages, 'current_index': current_index}, f)

    @staticmethod
    def _load_progress(installer_type: str):
        """
        Load the saved installation progress from a file.

        Args:
            installer_type (str): Type of installer (e.g., 'apt', 'pip')

        Returns:
            dict or None: Saved progress data if file exists, None otherwise
        """
        file_path = InstallDescriptor.PROGRESS_FILE.format(installer_type)
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                return json.load(f)
        return None

    @staticmethod
    def _clear_progress(installer_type: str):
        """
        Clear the saved installation progress by removing the file.

        Args:
            installer_type (str): Type of installer (e.g., 'apt', 'pip')
        """
        file_path = InstallDescriptor.PROGRESS_FILE.format(installer_type)
        if os.path.exists(file_path):
            os.remove(file_path)

class AptInstallDescriptor(InstallDescriptor):
    """
    Descriptor class for installing packages using apt-get.
    """

    @staticmethod
    def _install_single_package(package: str) -> bool:
        """
        Install a single package using apt-get.

        Args:
            package (str): Name of the package to install

        Returns:
            bool: True if installation was successful, False otherwise
        """
        try:
            subprocess.check_call(['sudo', 'apt-get', 'install', '-y', package])
            print(f"Successfully installed {package}")
            return True
        except subprocess.CalledProcessError as e:
            print(f"Error installing package: {package}")
            print(f"Error message: {e}")
            return False

    @staticmethod
    def _install_multiple_packages(packages: List[str]) -> None:
        """
        Install multiple packages using apt-get.

        Args:
            packages (List[str]): List of package names to install
        """
        progress_data = AptInstallDescriptor._load_progress('apt')
        
        if progress_data:
            packages = progress_data['packages']
            start_index = progress_data['current_index']
            print("Resuming apt installation from previous session...")
        else:
            start_index = 0

        output = widgets.Output()
        progress = widgets.IntProgress(value=start_index, min=0, max=len(packages), description='Progress:')
        display(output, progress)

        for i, pkg in enumerate(packages[start_index:], start=start_index):
            with output:
                print(f"Installing package {i+1}/{len(packages)}: {pkg}")
                success = AptInstallDescriptor._install_single_package(pkg)
                if success:
                    progress.value = i + 1
                    AptInstallDescriptor._save_progress('apt', packages, i + 1)
                else:
                    print(f"Installation paused at package {pkg}. Please restart the system if needed and run the installation again.")
                    return

        with output:
            if progress.value == len(packages):
                print("All packages installed successfully")
                AptInstallDescriptor._clear_progress('apt')
            else:
                print("Installation incomplete")

    def __set__(self, obj, package: Union[str, List[str]]) -> None:
        """
        Descriptor method to install package(s) when the attribute is set.

        Args:
            obj: The object instance that the descriptor is being used on
            package (Union[str, List[str]]): Package name or list of package names to install
        
        Raises:
            TypeError: If package is not a string or a list of strings
        """
        if isinstance(package, str):
            self._install_single_package(package)
        elif isinstance(package, list):
            self._install_multiple_packages(package)
        else:
            raise TypeError("Package must be a string or a list of strings")

class PipInstallDescriptor(InstallDescriptor):
    """
    Descriptor class for installing packages using pip.
    """

    @staticmethod
    def _install_single_package(package: str) -> bool:
        """
        Install a single package using pip.

        Args:
            package (str): Name of the package to install

        Returns:
            bool: True if installation was successful, False otherwise
        """
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            print(f"Successfully installed {package}")
            return True
        except subprocess.CalledProcessError as e:
            print(f"Error installing package: {package}")
            print(f"Error message: {e}")
            return False

    @staticmethod
    def _install_multiple_packages(packages: List[str]) -> None:
        """
        Install multiple packages using pip.

        Args:
            packages (List[str]): List of package names to install
        """
        progress_data = PipInstallDescriptor._load_progress('pip')
        
        if progress_data:
            packages = progress_data['packages']
            start_index = progress_data['current_index']
            print("Resuming pip installation from previous session...")
        else:
            start_index = 0

        output = widgets.Output()
        progress = widgets.IntProgress(value=start_index, min=0, max=len(packages), description='Progress:')
        display(output, progress)

        for i, pkg in enumerate(packages[start_index:], start=start_index):
            with output:
                print(f"Installing package {i+1}/{len(packages)}: {pkg}")
                success = PipInstallDescriptor._install_single_package(pkg)
                if success:
                    progress.value = i + 1
                    PipInstallDescriptor._save_progress('pip', packages, i + 1)
                else:
                    print(f"Installation paused at package {pkg}. Please restart the system if needed and run the installation again.")
                    return

        with output:
            if progress.value == len(packages):
                print("All packages installed successfully")
                PipInstallDescriptor._clear_progress('pip')
            else:
                print("Installation incomplete")

    def __set__(self, obj, package: Union[str, List[str]]) -> None:
        """
        Descriptor method to install package(s) when the attribute is set.

        Args:
            obj: The object instance that the descriptor is being used on
            package (Union[str, List[str]]): Package name or list of package names to install
        
        Raises:
            TypeError: If package is not a string or a list of strings
        """
        if isinstance(package, str):
            self._install_single_package(package)
        elif isinstance(package, list):
            self._install_multiple_packages(package)
        else:
            raise TypeError("Package must be a string or a list of strings")
