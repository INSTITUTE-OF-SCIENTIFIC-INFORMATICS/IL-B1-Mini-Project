# IL-B1 Cheminformatics Mini Project 🧪

Welcome to the ISI-IL-B1 Cheminformatics Mini Project! This is a hands-on assignment designed to help you learn Git/GitHub workflows while working with chemical SMILES notation.

## 📚 About This Project

This repository contains a collaborative database of chemical compounds represented using SMILES (Simplified Molecular Input Line Entry System) notation. Students will practice version control by contributing chemical compounds to this shared database.

## 🎯 Assignment Overview

Students will:
1. **Fork** this repository to their GitHub account
2. **Clone** their fork to their local machine
3. **Create a branch** using their name
4. **Add a chemical compound** with valid SMILES notation to `chemicals.json`
5. **Commit and push** their changes
6. **Create a Pull Request** to submit their work

**📖 Full Assignment Instructions:** See [ASSIGNMENT.md](ASSIGNMENT.md)

## 📁 Repository Structure

```
IL-B1-Mini-Project/
├── README.md           # This file - project overview
├── ASSIGNMENT.md       # Detailed assignment instructions
├── chemicals.json      # Chemical database (students edit this)
└── LICENSE            # Project license
```

## 🧬 What is SMILES?

SMILES (Simplified Molecular Input Line Entry System) is a notation that allows you to represent chemical structures as simple text strings.

**Examples:**
- Water: `O`
- Methane: `C`
- Ethanol: `CCO`
- Benzene: `c1ccccc1`
- Aspirin: `CC(=O)Oc1ccccc1C(=O)O`

## 🚀 Quick Start for Students

```bash
# 1. Fork this repo on GitHub (click the Fork button)

# 2. Clone your fork
git clone https://github.com/YOUR-USERNAME/IL-B1-Mini-Project.git
cd IL-B1-Mini-Project

# 3. Create a branch with your name
git checkout -b your-firstname-lastname

# 4. Edit chemicals.json - add your chemical compound

# 5. Commit your changes
git add chemicals.json
git commit -m "Add [Chemical Name] by [Your Name]"

# 6. Push to your fork
git push origin your-firstname-lastname

# 7. Go to GitHub and create a Pull Request
```

## 📋 Student Checklist

Before submitting your Pull Request:
- [ ] Forked the repository
- [ ] Created a branch with your name
- [ ] Added ONE chemical compound to `chemicals.json`
- [ ] SMILES notation is valid
- [ ] All fields completed (name, smiles, formula, contributor)
- [ ] Committed with a descriptive message
- [ ] Pushed to your fork
- [ ] Created a Pull Request with proper title and description

## 🔍 Resources

### SMILES & Cheminformatics
- [SMILES Tutorial](https://www.daylight.com/dayhtml/doc/theory/theory.smiles.html)
- [PubChem](https://pubchem.ncbi.nlm.nih.gov/) - Find SMILES for any chemical
- [ChemSpider](http://www.chemspider.com/) - Chemical database
- [SMILES Validator](https://cactus.nci.nih.gov/translate/) - Verify your SMILES

### Git & GitHub
- [Git Handbook](https://guides.github.com/introduction/git-handbook/)
- [Forking a Repository](https://docs.github.com/en/get-started/quickstart/fork-a-repo)
- [Creating a Pull Request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request)
- [Git Branching](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging)

## ❓ Frequently Asked Questions

### How do I find the SMILES notation for a chemical?
Visit [PubChem](https://pubchem.ncbi.nlm.nih.gov/), search for your chemical, and look for the "Canonical SMILES" field.

### What if my SMILES notation is invalid?
Use the [SMILES Validator](https://cactus.nci.nih.gov/translate/) to check your notation before submitting.

### Can I add more than one chemical?
No, each student should add exactly ONE chemical compound for this assignment.

### What if someone else chose the same chemical?
That's okay! Multiple students can add the same chemical as long as they work on different entry slots (id 6-12).

### I'm getting merge conflicts. What should I do?
Contact your instructor. This usually happens if you didn't fork correctly or are not working on your own branch.

## 👥 Current Contributors

See the `chemicals.json` file for a list of all contributors.

## 📧 Support

If you need help:
1. Check this README and [ASSIGNMENT.md](ASSIGNMENT.md)
2. Review the existing entries in `chemicals.json` as examples
3. Search for similar issues in the repository
4. Contact your instructor

## 📜 License

This project is licensed under the terms specified in the LICENSE file.

---

**ISI-IL-B1 Team**  
*Learning through collaboration* 🚀