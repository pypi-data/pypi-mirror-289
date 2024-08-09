'''
A function call cache using the `hashlib.sha256()` hashsum of the `pickle`d
arguments.

Similar to `functools.lru_cache()` function values are memoized by their
arguments but supports offline storage on disk. By default, all values are
stored in a directory `cache` inside the current working directory.

A `File` instance can be used to decorate callables[^setup][^teardown]:

[^setup]:
    For testing purposes, ensure a pristine file cache by switching to temporary
    working directory.

    >>> import os, tempfile, shutil
    >>> cwd, tmp = os.getcwd(), tempfile.mkdtemp()
    >>> os.chdir(tmp)

>>> cache = File()
>>> @cache
... def compute(count):
...     print(f'computing {count} spam')
...     return 'spam' * count
>>> compute(1)
computing 1 spam
'spam'
>>> compute(1) # Value is memoized and compute isn't called
'spam'
>>> compute(3)
computing 3 spam
'spamspamspam'
>>> sorted(os.listdir('cache')) # Verify cache entries #doctest: +ELLIPSIS
['compute-...', 'compute-...']

[^teardown]:
    Restore working directory and cleanup temporary directory.

    >>> os.chdir(cwd)
    >>> shutil.rmtree(tmp)

'''

import os, hashlib, base64, pickle, functools


class File(object):
    '''
    A function caching decorator, which serializes and deserializes to and from
    `pickle` data onto the storage into `basedir`.
    '''
    def __init__(self, basedir='cache'):
        self.basedir = basedir
        os.makedirs(self.basedir, exist_ok=True)

    def __getitem__(self, key):
        try:
            return open(f'{self.basedir}/{key}', 'rb').read()
        except FileNotFoundError as e:
            raise KeyError(key) from None

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __setitem__(self, key, value):
        return open(f'{self.basedir}/{key}', 'wb').write(value)

    def __call__(self, func):
        @functools.wraps(func)
        def call(*args, **kwargs):
            m = hashlib.sha256()
            m.update(pickle.dumps((args, kwargs)))
            digest = base64.urlsafe_b64encode(m.digest())[:-1].decode()
            key = f'{func.__name__}-{digest}'
            value = self.get(key)
            if value is None:
                self[key] = value = pickle.dumps(func(*args, **kwargs))
            return pickle.loads(value)
        return call
