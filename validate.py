#!/usr/bin/env python3
"""
Chemical SMILES Validator
This script validates the chemicals.json file to ensure:
1. Valid JSON syntax
2. All required fields are present
3. No duplicate IDs
4. SMILES notation is not empty (basic check)

Usage:
    python validate.py

Optional: Install RDKit for advanced SMILES validation
    pip install rdkit
"""

import json
import sys

def validate_json_file(filename='chemicals.json'):
    """Validate the chemicals.json file"""
    
    print("🔍 Validating chemicals.json...")
    print("-" * 50)
    
    try:
        # Read and parse JSON
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        print("✅ JSON syntax is valid")
        
    except FileNotFoundError:
        print(f"❌ Error: {filename} not found!")
        return False
    except json.JSONDecodeError as e:
        print(f"❌ JSON syntax error: {e}")
        return False
    
    # Check structure
    if 'molecules' not in data:
        print("❌ Error: 'molecules' key not found in JSON")
        return False
    
    molecules = data['molecules']
    print(f"✅ Found {len(molecules)} molecules")
    
    # Track validation
    errors = []
    warnings = []
    seen_ids = set()
    required_fields = ['id', 'name', 'smiles', 'formula', 'contributor']
    
    # Validate each molecule
    for i, mol in enumerate(molecules):
        mol_id = mol.get('id', f'unknown-{i}')
        
        # Check required fields
        for field in required_fields:
            if field not in mol:
                errors.append(f"Molecule ID {mol_id}: Missing field '{field}'")
        
        # Check for duplicate IDs
        if 'id' in mol:
            if mol['id'] in seen_ids:
                errors.append(f"Duplicate ID found: {mol['id']}")
            seen_ids.add(mol['id'])
        
        # Check for empty values (warnings for template entries)
        if mol.get('smiles', '').strip() == '':
            if 'Add your molecule here' not in mol.get('name', ''):
                warnings.append(f"Molecule ID {mol_id}: Empty SMILES notation")
        
        if mol.get('contributor', '').strip() == '':
            if 'Add your molecule here' not in mol.get('name', ''):
                warnings.append(f"Molecule ID {mol_id}: Empty contributor field")
    
    # Try advanced SMILES validation if RDKit is available
    try:
        from rdkit import Chem
        rdkit_available = True
        print("✅ RDKit available - performing advanced SMILES validation")
    except ImportError:
        rdkit_available = False
        print("ℹ️  RDKit not installed - skipping advanced SMILES validation")
        print("   Install with: pip install rdkit")
    
    if rdkit_available:
        for mol in molecules:
            mol_id = mol.get('id', 'unknown')
            smiles = mol.get('smiles', '')
            
            if smiles.strip() and 'Add your molecule here' not in mol.get('name', ''):
                try:
                    mol_obj = Chem.MolFromSmiles(smiles)
                    if mol_obj is None:
                        errors.append(f"Molecule ID {mol_id}: Invalid SMILES '{smiles}'")
                    else:
                        # Optionally verify formula
                        if 'formula' in mol:
                            from rdkit.Chem import Descriptors
                            mol_formula = Chem.rdMolDescriptors.CalcMolFormula(mol_obj)
                            if mol_formula != mol['formula']:
                                warnings.append(
                                    f"Molecule ID {mol_id}: Formula mismatch. "
                                    f"Expected '{mol['formula']}', SMILES suggests '{mol_formula}'"
                                )
                except Exception as e:
                    errors.append(f"Molecule ID {mol_id}: Error validating SMILES - {e}")
    
    # Print results
    print("-" * 50)
    
    if warnings:
        print("\n⚠️  Warnings:")
        for warning in warnings:
            print(f"   {warning}")
    
    if errors:
        print("\n❌ Errors found:")
        for error in errors:
            print(f"   {error}")
        print("\n❌ Validation failed!")
        return False
    else:
        print("\n✅ All validation checks passed!")
        print("✅ Your chemicals.json file is ready to commit!")
        return True


def main():
    """Main function"""
    success = validate_json_file()
    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()
