'''
This module contains functions to categorize OpenStreetMap primitives and to
convert those into shapes, as well as a basic workflow to reconstruct an
electrictity grid from these shapes.

`powergrid_items` can be used to load items from OpenStreetMap protobuf dumps:

>>> import os, matplotlib.pyplot as plt, esy.osm.topology.mpl
>>> from matplotlib.lines import Line2D
>>> itemmap = powergrid_itemmap('europe/germany/bremen-230101.osm.pbf', [110000])

`topology_features` is an example workflow to reconstruct a power grid topology
of a given voltage level from `itemmap`:

>>> osm, link, topology = topology_features(itemmap, 110000)
>>> len(osm), len(link), len(topology)
(393, 24, 24)

The `osm`, `link` and `topology` variables are features in the form of a
`(shape, properties)` tuple. These shapes can be visualized using matplotlib
using `esy.osm.topology.osm.patches`:

>>> fig, ax = plt.subplots(
...     figsize=(8, 4), subplot_kw=dict(aspect=1), layout='tight',
... )
>>> _ = fig.suptitle('Bremen 110 kV electricity grid')
>>> iax = ax.inset_axes(
...     [0.02, 0.03, 0.4, 0.4], xlim=(8.6780, 8.6818), ylim=(53.1296, 53.1312),
...     xticks=[], yticks=[]
... )
>>> legend = []
>>> for features, style, label in ((
...     (osm, dict(edgecolor='gray', facecolor='gray', alpha=.5), 'OSM'),
...     (link, dict(lw=2, edgecolor='orange', alpha=.5), 'Link'),
...     (topology, dict(lw=2, edgecolor='steelblue', alpha=.5), 'Topology'),
... )):
...     for a in (ax, iax):
...         _ = a.add_collection(esy.osm.topology.mpl.patches(
...             [shape for shape, properties in features], **style
...         ))
...     legend.append((
...         Line2D([0], [1], color=style['edgecolor'], lw=style.get('lw', 1)),
...         label
...     ))
>>> _ = ax.set(
...     ylabel='Latitude', ylim=[53.04, 53.19],
...     xlabel='Longitude', xlim=[8.53, 8.85],
... )
>>>
>>> _ = ax.indicate_inset_zoom(iax, edgecolor='gray')
>>> _ = ax.legend(*zip(*legend))
>>> os.makedirs('doc/figure/power', exist_ok=True)
>>> fig.savefig('doc/figure/power/grid.svg')

![](../../../../doc/figure/power/grid.svg)

Furthermore, the `geojson` function can be used to export the features to a set
of geojson files:

>>> geojson('doc/example', osm, link, topology)
>>> sorted(os.listdir('doc/example'))
['link.json', 'osm.json', 'topology.json']

'''

import functools, pathlib, json

import numpy as np, shapely.geometry

from esy.osm.topology.osm import geofabrik_ref, items, normalize, group_by_tag
import esy.osm.topology.graph


def parse_voltages(s):
    '''
    Parse the voltage string `s` into a set of voltages.

    >>> sorted(parse_voltages('380000;medium;400000'))
    [110000, 380000, 400000]

    Invalid values are represented using a value of `None`.

    >>> sorted(parse_voltages('spam'))
    [None]
    '''
    try:
        s = s.replace('medium', '110000')
        return set([int(v) for v in s.split(';')])
    except Exception as e:
        return {None}


def is_power_voltage(item, voltages=None):
    '''
    Predicate for OSM `item`s with a `power` tag, with a voltage in the given
    `voltages` set.
    '''
    return (
        'power' in item.tags and
        (not voltages or voltages & parse_voltages(item.tags.get('voltage')))
    )


line_power_tags = {'line', 'cable'}


def power_line(id, tags, shape):
    '''
    Generate power line items from `id`, `tags` and `shape`.
    '''
    if not (
        type(shape) is shapely.geometry.LineString and
        tags.get('power') in line_power_tags
    ):
        return

    for voltage in parse_voltages(tags.get('voltage', '')):
        yield id, {**tags, '@power': 'line', '@voltage': voltage}, shape


tower_power_tags = {'tower'}


def power_tower(id, tags, shape):
    '''
    Generate power tower items from `id`, `tags` and `shape`.
    '''
    if not (
        type(shape) is shapely.geometry.Point and
        tags.get('power') in tower_power_tags
    ):
        return

    yield id, {**tags, '@power': 'tower'}, shape


substation_power_tags = {'substation', 'station'}


def power_substation(id, tags, shape):
    '''
    Generate power substation items from `id`, `tags` and `shape`.
    '''
    if not tags.get('power') in substation_power_tags:
        return

    for voltage in parse_voltages(tags.get('voltage', '')):
        yield id, {**tags, '@power': 'substation', '@voltage': voltage}, shape


normalizers = [power_line, power_tower, power_substation]


def power_items(filename, voltages):
    '''
    Extract and normalize all power related items from the OSM protobuf
    `filename`.
    '''
    return normalize(
        items(filename, functools.partial(is_power_voltage, voltages=voltages)),
        normalizers
    )


def powergrid_itemmap(filename, voltages):
    '''
    Extract and normalize all power related items from the OSM protobuf
    `filename` and group items by `'line'` and `'substation'` types.
    '''
    voltages = set(voltages)
    items = power_items(geofabrik_ref(filename), voltages)
    return {
        'line': group_by_tag(items[power_line], '@voltage'),
        'substation': group_by_tag(items[power_substation], '@voltage'),
    }


def topology_features(itemmap, voltage):
    '''
    Extracts `(osm, link, topology)` power features from `itemmap` for the given
    `voltage` level.
    '''
    lines = np.array([s for _, _, s in itemmap['line'][voltage]])
    area = np.array([s for _, _, s in itemmap['substation'][voltage]])

    osm_features = [
        (s, {'id': i, **t})
        for i, t, s in itemmap['line'][voltage] + itemmap['substation'][voltage]
    ]

    # Convert lines to graph.
    _, graph, line_index = esy.osm.topology.graph.from_string_coordinates([
        esy.osm.topology.osm.lonlat_to_cartesian(l.coords) for l in lines
    ])
    coords = np.concatenate([np.array(l.coords) for l in lines])

    # Join graph nodes with identical coordinates.
    # TODO If there are multiple lines using the same vertices, the first edge
    # will get chosen. Warn about this or let users choose? Or perhaps map to
    # multiple indice?
    graph, node_index, edge_index = esy.osm.topology.graph.unique(coords, graph)
    line_index = line_index[edge_index]

    terminals, terminal_index, edge_index = (
        esy.osm.topology.graph.query_terminals(coords, graph, area)
    )
    graph = esy.osm.topology.graph.filter_edges(graph, edge_index)
    line_index = line_index[edge_index]

    topology, shapes, edge_paths = esy.osm.topology.graph.terminal_topology(
        coords, graph, terminals, terminal_index
    )

    osmid_paths = [
        [
            itemmap['line'][voltage][i][0]
            for i in np.unique(line_index[edge_path])
        ]
        for edge_path in edge_paths
    ]

    link_features = [
        (shape, {'id': id, '@osm': osmid_path})
        for id, (shape, osmid_path) in enumerate(zip(shapes, osmid_paths))
    ]

    # Generate topology features from graph.
    topology_features = [
        (shapely.linestrings(coords[[row, col]]), {'id': id, 'dist': dist})
        for id, (row, col, dist) in enumerate(zip(
            topology.row, topology.col, topology.data
        ))
    ]

    return osm_features, link_features, topology_features


def geojson_from_shape_features(shape_features):
    '''
    Create a geojson FeatureCollection from a collection of `(shape,
    properties)` tuples.
    '''
    return {
        'type': 'FeatureCollection',
        'features': [
            {
                'type': 'Feature', 'properties': properties,
                'geometry': shape.__geo_interface__,
            }
            for shape, properties in shape_features
        ]
    }


def geojson(outdir, osm, link, topology):
    '''
    Export `osm`, `link` and `topology` features as geojson files into `outdir`.
    '''
    outdir = pathlib.Path(outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    for name, features in dict(osm=osm, link=link, topology=topology).items():
        with open(f'{outdir}/{name}.json', 'w') as out:
            json.dump(geojson_from_shape_features(features), out)
