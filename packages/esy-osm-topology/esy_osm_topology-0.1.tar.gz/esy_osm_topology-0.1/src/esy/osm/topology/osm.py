'''
Utility functions for accessing and processing OpenStreetMap data.
'''

import os, itertools, functools

import numpy as np, scipy.spatial.distance, scipy.cluster.hierarchy
import shapely.geometry, esy.osm.shape

import esy.osm.topology.cache


cache = esy.osm.topology.cache.File()


ref_data_dir = 'cache/ref_data'


def geofabrik_ref(name):
    '''
    Download and write dataset `name` from [GEOFABRIK](https://geofabrik.de).

    The data is written into the directory `cache/ref_data`.
    '''
    import urllib.request

    filename = f'{ref_data_dir}/{name}'
    if os.path.exists(filename):
        return filename
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    urllib.request.urlretrieve(f'http://download.geofabrik.de/{name}', filename)
    return filename


@cache
def items(pbffile, filter, max_tasks=2 ** 20):
    '''
    Extract all shape items in the form of `(id, tags, shape)`, subject to
    `filter`, from the OpenStreetMap `pbffile`.
    '''
    return [
        (id, tags, shape)
        for shape, id, tags in esy.osm.shape.Shape(pbffile)(filter, max_tasks)
        if type(shape) is not esy.osm.shape.Invalid
    ]


def counter():
    '''
    Create a counting generator.
    '''
    def count(generator):
        for item in generator:
            count.value += 1
            yield item
    count.value = 0
    return count


def unknown():
    '''
    Key for representing unknown shape items.
    '''
    pass #pragma: nocover


def normalize(items, normalizers):
    '''
    Normalize and map shape `items` by applying `normalizers`.
    '''
    map = {**{normalizer: [] for normalizer in normalizers}}
    unknowns = []
    for id, tags, shape in items:
        count = counter()
        for normalizer, nitems in map.items():
            nitems.extend(count(normalizer(id, tags, shape)))
        if count.value == 0:
            unknowns.append((id, tags, shape))

    map[unknown] = unknowns
    return map


def group_by_tag(items, tag):
    '''
    Group shape `items` by a `tag` value.
    '''
    return {
        key: list(values)
        for key, values in itertools.groupby(
            sorted(items, key=lambda item: item[1].get(tag) or -1),
            key=lambda item: item[1].get(tag)
        )
    }


def lonlat_to_cartesian_transformer():
    '''
    Setup a `pyproj.Transformer` instance for projecting coordinates between the
    `lonlat` and `cart` projection.
    '''
    # TODO Wrap import errors in a novice readable explanation.
    import pyproj
    if not hasattr(lonlat_to_cartesian_transformer, 'value'):
        lonlat_to_cartesian_transformer.value = pyproj.Transformer.from_crs(
            {'proj': 'lonlat'}, {'proj': 'cart'}
        )
    return lonlat_to_cartesian_transformer.value


def lonlat_to_cartesian(lonlat):
    '''
    Convert `lonlat` coordinates into cartesian.

    >>> lonlat_to_cartesian([0, 0])
    array([6378137.,       0.,       0.])
    '''
    lonlat = np.asarray(lonlat)
    return np.stack(
        lonlat_to_cartesian_transformer().transform(
            lonlat[..., 0], lonlat[..., 1], np.zeros(lonlat.shape[:-1])
        ), axis=-1
    )


def cartesian_to_lonlat(coords):
    '''
    Convert cartesian `coords` into latitude/longitude coordinates.

    >>> cartesian_to_lonlat([6378137, 0, 0])
    array([0., 0.])
    '''
    coords = np.asarray(coords)
    return np.stack(
        lonlat_to_cartesian_transformer().transform(
            coords[..., 0], coords[..., 1], coords[..., 2],
            direction='inverse'
        )[:2], axis=-1
    )
