# Cheminformatics Assignment - Chemical SMILES Database

## Assignment Overview
In this assignment, you will practice Git/GitHub workflows while learning about chemical SMILES notation. You will add a chemical compound to our shared database using proper version control practices.

## Learning Objectives
- Understand and work with SMILES (Simplified Molecular Input Line Entry System) notation
- Practice Git branching and pull request workflows
- Contribute to a collaborative repository
- Learn basic cheminformatics concepts

## What is SMILES?
SMILES is a line notation for describing the structure of chemical species using short ASCII strings. For example:
- Water: `O`
- Methane: `C`
- Ethanol: `CCO`
- Benzene: `c1ccccc1`
- Aspirin: `CC(=O)Oc1ccccc1C(=O)O`

## Your Task
You will add ONE chemical compound to the `chemicals.json` file with its SMILES notation, molecular formula, and your name as the contributor.

## Assignment Instructions

### Step 1: Fork the Repository
1. Go to the repository: `https://github.com/ISI-IL-B1/IL-B1-Mini-Project`
2. Click the **Fork** button in the top-right corner
3. This creates a copy of the repository in your GitHub account

### Step 2: Clone Your Fork
Open your terminal/command prompt and run:
```bash
git clone https://github.com/YOUR-USERNAME/IL-B1-Mini-Project.git
cd IL-B1-Mini-Project
```
Replace `YOUR-USERNAME` with your actual GitHub username.

### Step 3: Create a Branch with Your Name
```bash
git checkout -b your-first-last-name
```
Example: `git checkout -b john-smith`

### Step 4: Choose a Chemical Compound
Choose ONE of the following compounds (or suggest your own):
1. Glucose (C6H12O6)
2. Caffeine (C8H10N4O2)
3. Acetic Acid (Vinegar)
4. Paracetamol (Acetaminophen)
5. Dopamine
6. Penicillin G
7. Ibuprofen
8. Vitamin C (Ascorbic Acid)

You can find SMILES notations at:
- [PubChem](https://pubchem.ncbi.nlm.nih.gov/)
- [ChemSpider](http://www.chemspider.com/)

### Step 5: Edit the chemicals.json File
1. Open `chemicals.json` in your text editor
2. Find one of the empty student entries (id 6-12)
3. Update the entry with your chosen chemical:
   - `name`: The chemical name
   - `smiles`: The SMILES notation
   - `formula`: The molecular formula
   - `contributor`: Your full name

**Example:**
```json
{
  "id": 6,
  "name": "Glucose",
  "smiles": "C(C1C(C(C(C(O1)O)O)O)O)O",
  "formula": "C6H12O6",
  "contributor": "John Smith"
}
```

### Step 6: Commit Your Changes
```bash
git add chemicals.json
git commit -m "Add [Chemical Name] by [Your Name]"
```
Example: `git commit -m "Add Glucose by John Smith"`

### Step 7: Push Your Branch
```bash
git push origin your-first-last-name
```

### Step 8: Create a Pull Request
1. Go to your forked repository on GitHub
2. You'll see a banner suggesting to create a Pull Request - click **Compare & pull request**
3. Set the base repository to: `ISI-IL-B1/IL-B1-Mini-Project` (main branch)
4. Set the head repository to: `YOUR-USERNAME/IL-B1-Mini-Project` (your branch)
5. Title your PR: "Add [Chemical Name] - [Your Name]"
6. In the description, include:
   - The chemical name
   - Why you chose this compound
   - Any interesting facts about the molecule
7. Click **Create pull request**

## Validation Checklist
Before submitting your PR, ensure:
- [ ] You created a branch with your name
- [ ] You edited only ONE entry in chemicals.json
- [ ] Your SMILES notation is valid (you can verify at [SMILES Validator](https://cactus.nci.nih.gov/))
- [ ] All fields are filled (name, smiles, formula, contributor)
- [ ] Your commit message is descriptive
- [ ] Your PR title follows the format

## Grading Criteria
- **Correct Git workflow** (fork, branch, PR): 40%
- **Valid SMILES notation**: 30%
- **Complete information** (all fields filled): 20%
- **PR description quality**: 10%

## Resources
- [SMILES Tutorial](https://www.daylight.com/dayhtml/doc/theory/theory.smiles.html)
- [PubChem](https://pubchem.ncbi.nlm.nih.gov/)
- [Git Handbook](https://guides.github.com/introduction/git-handbook/)
- [Creating a Pull Request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request)

## Need Help?
If you encounter issues:
1. Check the FAQ in the README.md
2. Review the example chemicals already in the database
3. Ask in the course discussion forum
4. Contact the instructor

Good luck! 🧪🔬
