import abc
import numpy as _np


class AbstractGraph(abc.ABC):
    """Abstract class for NetKet graph objects"""

    @property
    @abc.abstractmethod
    def is_connected(self):
        r"""bool: True if the graph is connected"""
        raise NotImplementedError

    @property
    @abc.abstractmethod
    def is_bipartite(self):
        r"""bool: True if the graph is bipartite"""
        raise NotImplementedError

    @abc.abstractmethod
    def edges(self):
        r"""list: List containing the edges of the graph"""
        raise NotImplementedError

    @abc.abstractmethod
    def distances(self):
        r"""list[list]: List containing the distances between the nodes.
		The fact that some node may not be reachable from another is represented by -1"""
        raise NotImplementedError

    @abc.abstractmethod
    def automorphisms(self):
        r"""list[list]: List containing the automorphisms of the graph"""
        raise NotImplementedError

    @property
    @abc.abstractmethod
    def n_nodes(self):
        r"""int: The number of vertices in the graph"""
        raise NotImplementedError

    @property
    @abc.abstractmethod
    def adjacency_list(self):
        r"""list[list]: List containing the adjacency list of the graph where each node
		is represented by an integer in [0, n_sites)"""
        raise NotImplementedError