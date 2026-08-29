# Contributing to IL-B1 Cheminformatics Project

Thank you for contributing to this project! This document provides guidelines for students submitting chemical compounds.

## Assignment Submission Process

### 1. Prerequisites
- A GitHub account
- Git installed on your computer
- A text editor (VS Code, Sublime, Notepad++, etc.)

### 2. Workflow

#### Fork & Clone
```bash
# Fork the repository on GitHub first, then:
git clone https://github.com/YOUR-USERNAME/IL-B1-Mini-Project.git
cd IL-B1-Mini-Project
```

#### Create Your Branch
Use your actual name (lowercase, hyphenated):
```bash
git checkout -b firstname-lastname
```
**Example:** `git checkout -b jane-doe`

#### Make Your Changes
1. Open `chemicals.json`
2. Find an empty student slot (id 6-12)
3. Fill in all fields:
   - `name`: Chemical compound name
   - `smiles`: Valid SMILES notation
   - `formula`: Molecular formula
   - `contributor`: Your full name

#### Validate Your SMILES
Before committing, verify your SMILES notation:
- Use [PubChem](https://pubchem.ncbi.nlm.nih.gov/)
- Use [NCI CACTUS Translator](https://cactus.nci.nih.gov/translate/)
- Use [ChemSpider](http://www.chemspider.com/)

#### Commit & Push
```bash
git add chemicals.json
git commit -m "Add [Chemical Name] by [Your Name]"
git push origin firstname-lastname
```

#### Create Pull Request
1. Go to your fork on GitHub
2. Click "Compare & pull request"
3. Fill out the PR template completely
4. Submit!

## Code of Conduct

### Do's ✅
- Work on your own branch
- Edit only ONE chemical entry
- Use valid SMILES notation
- Fill all required fields
- Write descriptive commit messages
- Be respectful in PR descriptions

### Don'ts ❌
- Don't edit other students' entries
- Don't commit directly to main branch
- Don't submit invalid SMILES
- Don't leave fields empty
- Don't make multiple PRs for the same assignment

## JSON Format Guidelines

Your entry should look like this:
```json
{
  "id": 6,
  "name": "Glucose",
  "smiles": "C(C1C(C(C(C(O1)O)O)O)O)O",
  "formula": "C6H12O6",
  "contributor": "Jane Doe"
}
```

**Important:**
- Keep the JSON structure intact
- Use double quotes for strings
- Don't forget commas between entries
- Ensure valid JSON syntax

## Getting Help

If you encounter issues:
1. Check [ASSIGNMENT.md](ASSIGNMENT.md) for detailed instructions
2. Review existing entries in `chemicals.json`
3. Verify your SMILES notation using online tools
4. Contact your instructor

## Review Process

Your PR will be reviewed for:
- Correct Git workflow
- Valid SMILES notation
- Complete information
- Proper JSON formatting
- Following naming conventions

## Questions?

If you have questions about:
- **Git/GitHub**: Review the [Git Handbook](https://guides.github.com/introduction/git-handbook/)
- **SMILES**: Check the [SMILES Tutorial](https://www.daylight.com/dayhtml/doc/theory/theory.smiles.html)
- **Assignment**: Read [ASSIGNMENT.md](ASSIGNMENT.md)
- **Other issues**: Contact your instructor

---

Happy contributing! 🧪✨
