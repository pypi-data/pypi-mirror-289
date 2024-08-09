import logging
import os
import sys

from dataclasses import dataclass, field
from functools import partial

from bib2tex import custom_types as ct
from bib2tex.config import BIBTEX_ENTRY_TYPES, FORMAT_SCHEMES_DIR
from bib2tex.file_handler import read_json_file


@dataclass
class FormatSchemeManager:
    format_schemes: dict[str, dict[str, str]] = field(default_factory=dict)

    def __post_init__(self):
        self.add_format_schemes(schemes_dir=FORMAT_SCHEMES_DIR)

    def add_format_schemes(self, schemes_dir: str) -> None:
        """Load format schemes from provided directory."""
        if not os.path.exists(schemes_dir):
            raise ValueError("Format schemes directory not existing.")
        for filename in os.listdir(schemes_dir):
            file_path = os.path.join(schemes_dir, filename)
            name, _ = os.path.splitext(filename)
            if name in self.format_schemes:
                raise KeyError(f"Format scheme {name!r} already existing.")
            scheme = read_json_file(file_path)
            if not isinstance(scheme, dict):
                raise ValueError("Format scheme must be a dictionary.")
            self.format_schemes[name] = scheme
            logging.debug(f"Loaded format scheme {name!r}.")

    def add_format_scheme(self, name: str, entry_type: str, format_scheme: str) -> None:
        """Register a new format scheme.

        Args:
            name (str): Name of the format scheme.
            entry_type (str): Entry type of the provided format scheme.
            format_scheme (dict): Dictionary representing the format scheme.
        """
        if name not in self.format_schemes:
            self.format_schemes[name] = {}
        if entry_type in self.format_schemes[name]:
            logging.warning(
                f"Format scheme {name!r} already exists for {entry_type!r}. Overwriting."
            )
        self.format_schemes[name][entry_type] = format_scheme
        logging.debug(f"Added {name!r} format scheme for {entry_type!r}.")

    def get_format_scheme(self, entry_type: str, name: str = "default") -> str:
        """Retrieve a format scheme for a specific entry type.

        Args:
            entry_type (str): BibTeX entry type.
            name (str): Name of the format scheme. Fallback to 'default'.
        """
        default_scheme = self.format_schemes["default"][entry_type]
        try:
            format_scheme = self.format_schemes[name][entry_type]
            logging.debug(f"Retrieved {entry_type} format scheme {name!r}.")
        except:
            format_scheme = default_scheme
            logging.warning(
                f"No {name!r} format scheme exists for {entry_type!r}; using default."
            )
        return format_scheme

    def get_format_schemes(self, name: str = "default") -> dict[str, str]:
        """Get a dictionary of format schemes for all entry types.

        Args:
            name (str): Name of the format scheme. Fallback to 'default'.
        """
        entry_types = BIBTEX_ENTRY_TYPES + ct.get_custom_type_names()
        get_scheme = partial(self.get_format_scheme, name=name)
        return {entry_type: get_scheme(entry_type) for entry_type in entry_types}

    def list_format_schemes(self) -> None:
        """List existing format schemes."""
        for name, fs_dict in self.format_schemes.items():
            print(f"{name!r} format schemes:")
            for entry_type, format_scheme in fs_dict.items():
                print(f"  -> {entry_type}: {format_scheme}")

