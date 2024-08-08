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
descList: list  # value = [('PMI1', <function <lambda> at 0x105617ba0>), ('PMI2', <function <lambda> at 0x108556ac0>), ('PMI3', <function <lambda> at 0x108556c00>), ('NPR1', <function <lambda> at 0x108556ca0>), ('NPR2', <function <lambda> at 0x108556d40>), ('RadiusOfGyration', <function <lambda> at 0x108556de0>), ('InertialShapeFactor', <function <lambda> at 0x108556e80>), ('Eccentricity', <function <lambda> at 0x108556f20>), ('Asphericity', <function <lambda> at 0x108556fc0>), ('SpherocityIndex', <function <lambda> at 0x108557060>), ('PBF', <function <lambda> at 0x108557100>)]
