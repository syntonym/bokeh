# -----------------------------------------------------------------------------
# Copyright (c) 2012 - 2019, Anaconda, Inc., and Bokeh Contributors.
# All rights reserved.
#
# The full license is in the file LICENSE.txt, distributed with this software.
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Boilerplate
# -----------------------------------------------------------------------------
import pytest  # noqa isort:skip

# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------

# External imports
import networkx as nx

# Module under test
from bokeh.models.graphs import StaticLayoutProvider, from_networkx  # isort:skip

# -----------------------------------------------------------------------------
# Setup
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# General API
# -----------------------------------------------------------------------------


def test_staticlayoutprovider_init_props():
    provider = StaticLayoutProvider()
    assert provider.graph_layout == {}


# TODO (bev) deprecation: 3.0
def test_from_networkx_deprecated():
    G = nx.Graph()
    G.add_nodes_from([0, 1, 2, 3])
    G.add_edges_from([[0, 1], [0, 2], [2, 3]])

    from bokeh.util.deprecation import BokehDeprecationWarning

    with pytest.warns(BokehDeprecationWarning):
        from_networkx(G, nx.circular_layout)


# -----------------------------------------------------------------------------
# Dev API
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Private API
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Code
# -----------------------------------------------------------------------------
