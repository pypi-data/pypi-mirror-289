"""
 Descriptors derived from a molecule's 3D structure

"""
from __future__ import annotations
from rdkit.Chem.Descriptors import _isCallable
from rdkit.Chem import rdMolDescriptors
__all__ = ['CalcMolDescriptors3D', 'descList', 'rdMolDescriptors']
def CalcMolDescriptors3D(mol, confId = None):
    """
    
        Compute all 3D descriptors of a molecule
        
        Arguments:
        - mol: the molecule to work with
        - confId: conformer ID to work with. If not specified the default (-1) is used
        
        Return:
        
        dict
            A dictionary with decriptor names as keys and the descriptor values as values
    
        raises a ValueError 
            If the molecule does not have conformers
        
    """
def _setupDescriptors(namespace):
    ...
descList: list  # value = [('PMI1', <function <lambda> at 0xffffb0532950>), ('PMI2', <function <lambda> at 0xffffa579b250>), ('PMI3', <function <lambda> at 0xffffa579b2e0>), ('NPR1', <function <lambda> at 0xffffa579b370>), ('NPR2', <function <lambda> at 0xffffa579b400>), ('RadiusOfGyration', <function <lambda> at 0xffffa579b490>), ('InertialShapeFactor', <function <lambda> at 0xffffa579b520>), ('Eccentricity', <function <lambda> at 0xffffa579b5b0>), ('Asphericity', <function <lambda> at 0xffffa579b640>), ('SpherocityIndex', <function <lambda> at 0xffffa579b6d0>), ('PBF', <function <lambda> at 0xffffa579b760>)]
