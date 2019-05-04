import pytest
import os,sys,inspect
import numpy as np
import pybop.core as pc
import pybop.crystal_structures as pcs

def test_basic_system():
    #basic system tests
    sys = pc.System()
    sys.set_box([[0,1],[0,1],[0,1]])
    assert sys.get_box() == [[0,1],[0,1],[0,1]]
    #sys.read_inputfile("conf.dump")


def test_system_read():
    sys = pc.System()
    sys.read_inputfile('tests/conf.dump')
    atoms = sys.get_allatoms()
    assert len(atoms) == 500

    #check box
    assert sys.get_box() == [[-7.66608, 11.1901],[-7.66915, 11.1931],[-7.74357, 11.2676]]
    
    #check few atoms
    filtered_atoms = [ atom for atom in atoms if atom.get_id() == 204]
    assert filtered_atoms[0].get_x() == [-0.10301, -6.35752, -6.44787]

    #now check the same for zipped file
    sys = pc.System()
    sys.read_inputfile('tests/conf.dump.gz')
    atoms = sys.get_allatoms()
    assert len(atoms) == 500

    #check box
    assert sys.get_box() == [[-7.66608, 11.1901],[-7.66915, 11.1931],[-7.74357, 11.2676]]
    
    #check few atoms
    filtered_atoms = [ atom for atom in atoms if atom.get_id() == 204]
    assert filtered_atoms[0].get_x() == [-0.10301, -6.35752, -6.44787]

def test_system_atom_access():
    #create some atoms
    atoms, boxdims = pcs.make_crystal('bcc')
    sys = pc.System()
    sys.assign_atoms(atoms, boxdims)
    atom = sys.get_atom(0)
    assert atom.get_x() == [0, 0, 0]

    atom.set_x([0.1, 0.1, 0.1])
    sys.set_atom(atom)
    atom = sys.get_atom(0)
    assert atom.get_x() == [0.1, 0.1, 0.1]    