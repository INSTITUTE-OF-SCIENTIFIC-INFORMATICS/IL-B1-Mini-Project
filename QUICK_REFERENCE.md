# Quick Reference Guide

## Git Commands Cheat Sheet

### Initial Setup
```bash
# Fork the repo on GitHub first, then:
git clone https://github.com/YOUR-USERNAME/IL-B1-Mini-Project.git
cd IL-B1-Mini-Project
```

### Create Branch
```bash
# Create and switch to your branch
git checkout -b your-firstname-lastname

# Example:
git checkout -b jane-doe
```

### Check Status
```bash
# See what files you've changed
git status

# See the differences
git diff
```

### Commit Changes
```bash
# Stage your changes
git add chemicals.json

# Commit with a message
git commit -m "Add [Chemical Name] by [Your Name]"

# Example:
git commit -m "Add Glucose by Jane Doe"
```

### Push to GitHub
```bash
# Push your branch to your fork
git push origin your-firstname-lastname

# Example:
git push origin jane-doe
```

### Useful Commands
```bash
# See current branch
git branch

# See commit history
git log --oneline

# Undo changes before commit
git checkout -- chemicals.json
```

---

## SMILES Quick Reference

### Basic Atoms
- Carbon: `C` (implicit hydrogens)
- Nitrogen: `N`
- Oxygen: `O`
- Phosphorus: `P`
- Sulfur: `S`
- Fluorine: `F`
- Chlorine: `Cl`
- Bromine: `Br`
- Iodine: `I`

### Bonds
- Single bond: `-` (usually implied)
- Double bond: `=`
- Triple bond: `#`
- Aromatic: lowercase letters (e.g., `c` for aromatic carbon)

### Rings
- Use numbers to indicate ring connections
- Example: Benzene = `c1ccccc1`

### Examples
| Molecule | SMILES | Structure |
|----------|--------|-----------|
| Water | `O` | H-O-H |
| Methane | `C` | CH₄ |
| Ethanol | `CCO` | CH₃-CH₂-OH |
| Acetic Acid | `CC(=O)O` | CH₃-COOH |
| Benzene | `c1ccccc1` | Aromatic ring |
| Aspirin | `CC(=O)Oc1ccccc1C(=O)O` | Complex drug |

---

## Finding SMILES for Your Chemical

### Method 1: PubChem (Recommended)
1. Go to https://pubchem.ncbi.nlm.nih.gov/
2. Search for your chemical name
3. Look for "Canonical SMILES" in the compound summary
4. Copy the SMILES string

### Method 2: ChemSpider
1. Go to http://www.chemspider.com/
2. Search for your chemical
3. Find the SMILES notation in the properties

### Method 3: NCI CACTUS
1. Go to https://cactus.nci.nih.gov/
2. Enter your chemical name
3. Select "SMILES" as output format

---

## Validating Your SMILES

### Online Validators
- **NCI CACTUS**: https://cactus.nci.nih.gov/translate/
  - Paste your SMILES → Convert to name or formula
  - If it works, your SMILES is valid!

- **PubChem Structure Editor**: https://pubchem.ncbi.nlm.nih.gov/edit3/index.html
  - Paste SMILES and visualize the structure

### Using the Validation Script
```bash
# Install Python 3 if needed
# Then run:
python validate.py

# For advanced validation, install RDKit:
pip install rdkit
python validate.py
```

---

## JSON Format

Your entry in `chemicals.json` should look like:

```json
{
  "id": 6,
  "name": "Your Chemical Name",
  "smiles": "YOUR_SMILES_HERE",
  "formula": "CxHyOz",
  "contributor": "Your Full Name"
}
```

**Important:**
- Use double quotes `"`, not single quotes `'`
- Don't forget commas between entries
- Keep the structure exactly as shown

---

## Common Issues & Solutions

### Issue: "Permission denied" when pushing
**Solution:** Make sure you forked the repo and are pushing to YOUR fork, not the original ISI repo.

### Issue: Branch already exists
**Solution:**
```bash
git checkout your-branch-name  # Switch to existing branch
# OR
git branch -D old-branch-name  # Delete old branch
git checkout -b new-branch-name  # Create new one
```

### Issue: Invalid JSON
**Solution:**
- Check for missing commas
- Ensure all quotes are double quotes
- Use https://jsonlint.com/ to validate
- Run `python validate.py`

### Issue: Can't find SMILES for my chemical
**Solution:**
- Try different spellings (e.g., "Vitamin C" vs "Ascorbic Acid")
- Use the chemical formula to search
- Ask your instructor for help

---

## Suggested Chemicals

Pick any ONE chemical you find interesting:

**Easy (Simple SMILES):**
- Glucose
- Acetic Acid
- Glycine
- Urea

**Medium:**
- Caffeine
- Vitamin C
- Dopamine
- Paracetamol

**Challenging:**
- Penicillin G
- Cholesterol
- Testosterone
- Adrenaline

---

## Important Reminders

✅ **DO:**
- Work on your own branch
- Add only ONE chemical
- Validate your SMILES
- Write descriptive commit messages
- Fill all fields completely

❌ **DON'T:**
- Edit directly on main branch
- Change other people's entries
- Submit empty fields
- Make multiple PRs
- Copy invalid SMILES

---

## Links

- **Assignment Instructions**: [ASSIGNMENT.md](ASSIGNMENT.md)
- **Examples**: [EXAMPLES.md](EXAMPLES.md)
- **Contributing Guide**: [CONTRIBUTING.md](CONTRIBUTING.md)
- **PubChem**: https://pubchem.ncbi.nlm.nih.gov/
- **SMILES Tutorial**: https://www.daylight.com/dayhtml/doc/theory/theory.smiles.html
- **Git Handbook**: https://guides.github.com/introduction/git-handbook/

---

**Need help? Contact your instructor!** 📧

Good luck! 🧪✨
