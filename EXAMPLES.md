# Example Chemical Entries

This document shows examples of correctly formatted chemical entries to help you complete the assignment.

## Example 1: Simple Molecule - Glucose

```json
{
  "id": 6,
  "name": "Glucose",
  "smiles": "C(C1C(C(C(C(O1)O)O)O)O)O",
  "formula": "C6H12O6",
  "contributor": "Jane Smith"
}
```

**Why this is correct:**
- ✅ Valid SMILES notation
- ✅ Correct molecular formula
- ✅ Full contributor name provided
- ✅ All fields completed
- ✅ Proper JSON formatting

---

## Example 2: Aromatic Compound - Caffeine

```json
{
  "id": 7,
  "name": "Caffeine",
  "smiles": "CN1C=NC2=C1C(=O)N(C(=O)N2C)C",
  "formula": "C8H10N4O2",
  "contributor": "John Doe"
}
```

**Why this is correct:**
- ✅ Aromatic rings properly represented
- ✅ Nitrogen atoms included in SMILES
- ✅ Matches the chemical structure of caffeine
- ✅ Professional formatting

---

## Example 3: Drug Compound - Ibuprofen

```json
{
  "id": 8,
  "name": "Ibuprofen",
  "smiles": "CC(C)Cc1ccc(cc1)C(C)C(=O)O",
  "formula": "C13H18O2",
  "contributor": "Sarah Johnson"
}
```

**Why this is correct:**
- ✅ Complex molecule correctly represented
- ✅ Carboxylic acid group included
- ✅ Aromatic ring notation (lowercase 'c')
- ✅ Accurate formula

---

## Common Mistakes to Avoid

### ❌ Incorrect: Missing Information
```json
{
  "id": 6,
  "name": "Glucose",
  "smiles": "",
  "formula": "",
  "contributor": ""
}
```
**Problem:** All fields must be filled in!

---

### ❌ Incorrect: Invalid SMILES
```json
{
  "id": 7,
  "name": "Aspirin",
  "smiles": "aspirin",
  "formula": "C9H8O4",
  "contributor": "Student Name"
}
```
**Problem:** "aspirin" is not valid SMILES notation. Use the actual SMILES string!

---

### ❌ Incorrect: Wrong Formula
```json
{
  "id": 8,
  "name": "Water",
  "smiles": "O",
  "formula": "H2O2",
  "contributor": "Student Name"
}
```
**Problem:** The formula doesn't match the SMILES. Water is H2O, not H2O2!

---

## How to Verify Your Entry

### Step 1: Find the SMILES
Go to [PubChem](https://pubchem.ncbi.nlm.nih.gov/) and search for your chemical. Look for "Canonical SMILES".

### Step 2: Validate the SMILES
Paste your SMILES into the [NCI CACTUS Translator](https://cactus.nci.nih.gov/translate/):
- Input: Your SMILES string
- Output: IUPAC Name or Molecular Formula

If it returns a result, your SMILES is valid! ✅

### Step 3: Confirm the Formula
The molecular formula should match what you find on PubChem or what the validator returns.

---

## Suggested Chemicals for Students

Here are some interesting chemicals you might consider (with their SMILES):

| Chemical | SMILES | Formula | Category |
|----------|--------|---------|----------|
| Glucose | `C(C1C(C(C(C(O1)O)O)O)O)O` | C6H12O6 | Sugar |
| Caffeine | `CN1C=NC2=C1C(=O)N(C(=O)N2C)C` | C8H10N4O2 | Stimulant |
| Ibuprofen | `CC(C)Cc1ccc(cc1)C(C)C(=O)O` | C13H18O2 | Drug |
| Vitamin C | `C(C(C1C(=C(C(=O)O1)O)O)O)O` | C6H8O6 | Vitamin |
| Dopamine | `C1=CC(=C(C=C1CCN)O)O` | C8H11NO2 | Neurotransmitter |
| Paracetamol | `CC(=O)Nc1ccc(cc1)O` | C8H9NO2 | Drug |
| Acetic Acid | `CC(=O)O` | C2H4O2 | Acid |

**Note:** You can choose any chemical you like! These are just suggestions.

---

## Tips for Success

1. **Double-check your SMILES**: Use online validators before submitting
2. **Copy carefully**: SMILES notation is case-sensitive!
3. **Test your JSON**: Use a JSON validator to ensure no syntax errors
4. **Be unique**: Try to choose a chemical that interests you
5. **Research**: Learn about your chemical and share interesting facts in your PR

---

## Need More Help?

- **SMILES Syntax**: [SMILES Tutorial](https://www.daylight.com/dayhtml/doc/theory/theory.smiles.html)
- **Find Chemicals**: [PubChem Database](https://pubchem.ncbi.nlm.nih.gov/)
- **Validate SMILES**: [CACTUS Translator](https://cactus.nci.nih.gov/translate/)
- **JSON Validator**: [JSONLint](https://jsonlint.com/)

Good luck with your assignment! 🎓🧪
