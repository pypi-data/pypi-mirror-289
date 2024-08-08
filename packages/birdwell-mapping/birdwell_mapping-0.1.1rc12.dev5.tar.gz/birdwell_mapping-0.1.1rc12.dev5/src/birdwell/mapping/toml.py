import tomlkit
from contextlib import contextmanager
from os import PathLike


@contextmanager
def edit_toml(file_path: str):
    with open(file_path) as f:
        loaded = tomlkit.load(f)

    try:
        yield loaded
    finally:
        with open(file_path, 'w') as f2:
            tomlkit.dump(loaded, f2)


def load_toml(file_path: str | PathLike):
    with open(file_path) as f:
        return tomlkit.load(f)


def save_toml(obj: dict, file_path: str | PathLike):
    with open(file_path, 'w') as f:
        tomlkit.dump(obj, f)
