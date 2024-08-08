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
descList: list  # value = [('PMI1', <function <lambda> at 0x0000026A48CF79D0>), ('PMI2', <function <lambda> at 0x0000026A50FA4EE0>), ('PMI3', <function <lambda> at 0x0000026A50FA4F70>), ('NPR1', <function <lambda> at 0x0000026A50FBE040>), ('NPR2', <function <lambda> at 0x0000026A50FBE0D0>), ('RadiusOfGyration', <function <lambda> at 0x0000026A50FBE160>), ('InertialShapeFactor', <function <lambda> at 0x0000026A50FBE1F0>), ('Eccentricity', <function <lambda> at 0x0000026A50FBE280>), ('Asphericity', <function <lambda> at 0x0000026A50FBE310>), ('SpherocityIndex', <function <lambda> at 0x0000026A50FBE3A0>), ('PBF', <function <lambda> at 0x0000026A50FBE430>)]
