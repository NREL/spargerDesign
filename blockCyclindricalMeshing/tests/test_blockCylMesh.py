import os
import sys

import numpy as np

sys.path.append("../util")
import argument
from meshing import *
from myparser import parseJsonFile

sys.path.append("..")
from writeBlockMesh import *


def base_mesh(argsDict):
    geomDict = assemble_geom(argsDict)
    meshDict = assemble_mesh(argsDict, geomDict)
    writeBlockMeshDict(argsDict, geomDict, meshDict)


def test_side_sparger():
    argsDict = {
        "input_file": "../sideSparger/input.json",
        "topo_file": "../sideSparger/topology.json",
        "out_folder": "../case/system",
    }
    base_mesh(argsDict)


def test_flat_donut():
    argsDict = {
        "input_file": "../flatDonut/input.json",
        "topo_file": "../flatDonut/topology.json",
        "out_folder": "../case/system",
    }
    base_mesh(argsDict)


def test_base_column():
    argsDict = {
        "input_file": "../baseColumn/input.json",
        "topo_file": "../baseColumn/topology.json",
        "out_folder": "../case/system",
    }
    base_mesh(argsDict)


def test_base_column_refine():
    argsDict = {
        "input_file": "../baseColumn_refineSparg/input.json",
        "topo_file": "../baseColumn_refineSparg/topology.json",
        "out_folder": "../case/system",
    }
    base_mesh(argsDict)


def test_base_column_projected():
    argsDict = {
        "input_file": "../baseColumn_projected/input.json",
        "topo_file": "../baseColumn_projected/topology.json",
        "out_folder": "../case/system",
    }
    base_mesh(argsDict)


def test_multiring():
    argsDict = {
        "input_file": "../multiRing_simple/input.json",
        "topo_file": "../multiRing_simple/topology.json",
        "out_folder": "../case/system",
    }
    base_mesh(argsDict)


def test_multiring_coarse():
    argsDict = {
        "input_file": "../multiRing_coarse/input.json",
        "topo_file": "../multiRing_coarse/topology.json",
        "out_folder": "../case/system",
    }
    base_mesh(argsDict)
