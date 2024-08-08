import pickle
import os
from contextlib import contextmanager


class Pickler:
    def __init__(self, root_dir: str = '.', file_ext: str = '.pickle'):
        self.loc = self.ensure_root(root_dir)
        self.file_ext = file_ext if file_ext.startswith('.') else f'.{file_ext}'
        self.data = self.load_all()

    @staticmethod
    def ensure_root(root_path: str):
        full_path = os.path.abspath(f'{root_path}/.birdwell/pickles')
        if not os.path.exists(full_path):
            os.makedirs(full_path, exist_ok=True)
        return full_path

    def save_all(self):
        for k in self.data:
            self.save(self.data[k], k)

    def load_all(self):
        loaded = {}
        for x in os.listdir(self.loc):
            if not x.endswith(self.file_ext):
                continue
            name = x.removesuffix(self.file_ext)
            loaded[name] = self.load(name)
        return loaded

    def load(self, name: str):
        try:
            with open(f'{self.loc}/{name}{self.file_ext}', mode='rb') as f:
                return pickle.load(f)
        except FileNotFoundError as e:
            return e
        except AttributeError as e:
            print(f'[PICKLER]: Error loading "{name}" - class attribute change detected. -> {str(e.args)}')
            return e

    def save(self, obj, name: str):
        if not isinstance(name, (str, int)):
            raise ValueError('name should be a string or int!')

        with open(f'{self.loc}/{name}{self.file_ext}', mode='wb') as f:
            pickle.dump(obj, f)

        self.data[name] = obj

    def rm(self, name: str):
        file_name = f'{name}{self.file_ext}'
        if file_name in os.listdir(self.loc):
            os.remove(f'{self.loc}/{file_name}')
        if name in self.data:
            self.data.pop(name)

    def clear(self):
        ks = [k for k in self.data]
        for k in ks:
            self.rm(k)


@contextmanager
def edit_pickle(file_path: str):
    with open(file_path, mode='rb') as f:
        loaded = pickle.load(f)

    try:
        yield loaded
    finally:
        with open(file_path, 'wb') as f2:
            pickle.dump(loaded, f2)
