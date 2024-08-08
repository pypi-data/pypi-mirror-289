"""
GraphRag.py

This module provides functionality to initialize and manage GraphRAG configurations.

It includes a Create class that checks for GraphRAG installation, installs it if necessary,
and provides methods to interact with GraphRAG settings and environment variables.

Classes:
    Create: Manages GraphRAG initialization and configuration.

Dependencies:
    - importlib
    - yaml
    - os
    - dotenv
    - Console (from parent directory)

Usage:
    from QuickUse.GraphRag import Create
    graph_rag = Create('/path/to/directory')
"""

import importlib
import yaml
import os
from dotenv import load_dotenv, set_key

from ..QuickColab.Console import Console

class Create:
    """
    A class to manage GraphRAG initialization and configuration.

    This class checks for GraphRAG installation, installs it if necessary,
    and provides methods to interact with GraphRAG settings and environment variables.

    Attributes:
        dir (str): The directory path for GraphRAG configuration.
        settings (dict): The loaded settings from the YAML file.
        settings_file (str): The name of the settings file (default: 'settings.yaml').
        env_file (str): The name of the environment file (default: '.env').

    Methods:
        __init__(dir: str): Initialize the Create instance.
        _is_package_installed(package_name: str): Check if a package is installed.
        _install_package(package_name: str): Install a package using Console.pipinstall.
        init(): Initialize GraphRAG using the graphrag.index module.
        query_and_extract_response(query: str, method: str): Query GraphRAG and extract the response.
        index(): Index the GraphRAG directory.
        load_settings(): Load settings from the YAML file.
        save_settings(): Save settings to the YAML file.
        __setitem__(key: str, value): Set a value in settings or environment variables.
        __getitem__(key: str): Get a value from settings or environment variables.
        print_config_guide(): Print a guide for configuring settings.yaml and .env files.
    """

    def __init__(self, dir: str):
        """
        Initialize the Create instance.

        Args:
            dir (str): The directory path for GraphRAG configuration.

        Raises:
            ValueError: If the provided directory is not a string.
        """
        self.dir = str(dir)

        # Check if graphrag is installed
        if not self._is_package_installed('graphrag'):
            print("graphrag is not installed, attempting to install...")
            self._install_package('graphrag')
            self.init()
        else:
            print("graphrag is already installed")

    def query_and_extract_response(self, query: str, method: str = "global") -> str:
        """
        Query GraphRAG and extract the response.

        Args:
            query (str): The query string to process.
            method (str): The method to use for querying (default: "global").

        Returns:
            str: The extracted response from GraphRAG.
        """
        command = f"python -m graphrag.query --root {self.dir} --method {method} \"{query}\""
        output = Console.run_command(command)
        return Console.extract_response(output)

    def _is_package_installed(self, package_name):
        """
        Check if a package is installed.

        Args:
            package_name (str): The name of the package to check.

        Returns:
            bool: True if the package is installed, False otherwise.
        """
        try:
            importlib.import_module(package_name)
            return True
        except ImportError:
            return False

    def _install_package(self, package_name):
        """
        Install a package using Console.pipinstall.

        Args:
            package_name (str): The name of the package to install.
        """
        Console.pipinstall = "graphrag"
        print(f"{package_name} installed successfully")

    def init(self):
        """
        Initialize GraphRAG using the graphrag.index module.
        """
        Console.run_command(f"python -m graphrag.index --init --root {self.dir}")

    def index(self):
        """
        Index the GraphRAG directory.
        """
        Console.run_command(f"python -m graphrag.index --root {self.dir}")

    def load_settings(self):
        """
        Load settings from the YAML file.

        Raises:
            FileNotFoundError: If the settings file does not exist.
            yaml.YAMLError: If there's an error parsing the YAML file.
        """
        with open(self.dir + self.settings_file, 'r') as file:
            self.settings = yaml.safe_load(file)

    def save_settings(self):
        """
        Save settings to the YAML file.

        Raises:
            IOError: If there's an error writing to the file.
        """
        with open(self.dir + self.settings_file, 'w') as file:
            yaml.dump(self.settings, file)

    def __setitem__(self, key, value):
        """
        Set a value in settings or environment variables.

        Args:
            key (str): The key to set. Use dot notation for nested settings.
            value: The value to set.

        Raises:
            KeyError: If the key is not found in settings or .env.
        """
        keys = key.split('.')
        
        # Handle settings.yaml
        if keys[0] in self.settings:
            current = self.settings
            for k in keys[:-1]:
                if k not in current:
                    current[k] = {}
                current = current[k]
            current[keys[-1]] = value
            self.save_settings()
        
        # Handle .env
        elif key == 'GRAPHRAG_API_KEY':
            set_key(self.env_file, key, value)
        
        else:
            raise KeyError(f"Key '{key}' not found in settings or .env")

    def __getitem__(self, key):
        """
        Get a value from settings or environment variables.

        Args:
            key (str): The key to get. Use dot notation for nested settings.

        Returns:
            The value associated with the key.

        Raises:
            KeyError: If the key is not found in settings or .env.
        """
        keys = key.split('.')
        
        # Get from settings.yaml
        if keys[0] in self.settings:
            current = self.settings
            for k in keys:
                current = current[k]
            return current
        
        # Get from .env
        elif key == 'GRAPHRAG_API_KEY':
            return os.getenv(key)
        
        else:
            raise KeyError(f"Key '{key}' not found in settings or .env")

    def print_config_guide(self):
        """
        Print a guide for configuring settings.yaml and .env files.

        This method displays information about how to modify settings in the settings.yaml file
        and how to set the API key in the .env file. It also shows current settings and provides
        usage examples.
        """
        print("Configuration Guide for GraphRAG")
        print("================================\n")

        print("settings.yaml:")
        print("--------------")
        print("To modify settings, use: graph_rag['key.subkey'] = value")
        print("Example settings:")
        for key, value in self.settings.items():
            if isinstance(value, dict):
                print(f"  {key}:")
                for subkey, subvalue in value.items():
                    print(f"    {subkey}: {subvalue}")
            else:
                print(f"  {key}: {value}")
        
        print("\n.env:")
        print("-----")
        print("To set the API key, use: graph_rag['GRAPHRAG_API_KEY'] = 'your-api-key'")
        print(f"Current API key: {os.getenv('GRAPHRAG_API_KEY') or 'Not set'}")

        print("\nUsage examples:")
        print("---------------")
        print("1. Set LLM model:")
        print("   graph_rag['llm.model'] = 'gpt-4'")
        print("2. Set API base:")
        print("   graph_rag['llm.api_base'] = 'https://api.openai.com/v1'")
        print("3. Set API key:")
        print("   graph_rag['GRAPHRAG_API_KEY'] = 'sk-your-api-key'")
