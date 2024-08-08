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
descList: list  # value = [('PMI1', <function <lambda> at 0x10b8cf160>), ('PMI2', <function <lambda> at 0x110d450d0>), ('PMI3', <function <lambda> at 0x110d45160>), ('NPR1', <function <lambda> at 0x110d451f0>), ('NPR2', <function <lambda> at 0x110d45280>), ('RadiusOfGyration', <function <lambda> at 0x110d45310>), ('InertialShapeFactor', <function <lambda> at 0x110d453a0>), ('Eccentricity', <function <lambda> at 0x110d45430>), ('Asphericity', <function <lambda> at 0x110d454c0>), ('SpherocityIndex', <function <lambda> at 0x110d45550>), ('PBF', <function <lambda> at 0x110d455e0>)]
