from rich import print
from pathlib import Path
from typing import Dict, List, Set, Optional

from raptor.logger import logger


FDIR = Path(__file__).resolve().parent


class Node:
    """
    Represents a node in the hierarchical tree structure.
    """

    def __init__(self, text: str, index: int, children: Set[int], embeddings) -> None:
        self.text = text
        self.index = index
        self.children = children
        self.embeddings = embeddings
        logger.info(f"{self.index} - {self.text}")


class Tree:
    """
    Represents the entire hierarchical tree structure.
    """

    def __init__(
        self,
        all_nodes,
        root_nodes,
        leaf_nodes,
        num_layers,
        layer_to_nodes,
        fname: Optional[str] = None,
    ) -> None:
        self.all_nodes = all_nodes
        self.root_nodes = root_nodes
        self.leaf_nodes = leaf_nodes
        self.num_layers = num_layers
        self.layer_to_nodes = layer_to_nodes
        self.fpath = FDIR / f"../data/{fname}.info"

        if not self.fpath.exists():
            self.fpath.touch()
