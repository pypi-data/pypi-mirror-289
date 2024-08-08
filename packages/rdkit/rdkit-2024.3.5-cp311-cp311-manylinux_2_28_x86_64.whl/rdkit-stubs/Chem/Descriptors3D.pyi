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
descList: list  # value = [('PMI1', <function <lambda> at 0x7fa0c4a234c0>), ('PMI2', <function <lambda> at 0x7fa0b5ae9260>), ('PMI3', <function <lambda> at 0x7fa0b5ae93a0>), ('NPR1', <function <lambda> at 0x7fa0b5ae9440>), ('NPR2', <function <lambda> at 0x7fa0b5ae94e0>), ('RadiusOfGyration', <function <lambda> at 0x7fa0b5ae9580>), ('InertialShapeFactor', <function <lambda> at 0x7fa0b5ae9620>), ('Eccentricity', <function <lambda> at 0x7fa0b5ae96c0>), ('Asphericity', <function <lambda> at 0x7fa0b5ae9760>), ('SpherocityIndex', <function <lambda> at 0x7fa0b5ae9800>), ('PBF', <function <lambda> at 0x7fa0b5ae98a0>)]
