# Instructor Guide - IL-B1 Cheminformatics Assignment

## Assignment Overview

This repository is designed as a hands-on Git/GitHub workflow assignment combined with basic cheminformatics concepts using SMILES notation.

**Student Learning Objectives:**
- Practice Git branching and pull request workflows
- Understand SMILES chemical notation
- Collaborate on a shared repository
- Experience real-world development workflows

---

## Setup Instructions for Instructors

### 1. Repository Setup

This repository is already configured and ready for students. You should:

1. **Push to GitHub:**
   ```bash
   # If not already initialized
   git init
   git add .
   git commit -m "Initial assignment setup"
   git branch -M main
   git remote add origin https://github.com/ISI-IL-B1/IL-B1-Mini-Project.git
   git push -u origin main
   ```

2. **Configure Repository Settings:**
   - Go to Settings → General
   - Enable "Allow forking"
   - Under "Pull Requests", enable "Allow merge commits"
   - Optionally enable "Automatically delete head branches"

3. **Branch Protection (Optional but Recommended):**
   - Settings → Branches → Add rule for `main`
   - Enable "Require pull request reviews before merging"
   - Enable "Require status checks to pass before merging"
   - This prevents direct commits to main

---

## Student Assignment Structure

**7 Student Slots Available:** IDs 6-12 in `chemicals.json`

Each student will:
1. Fork the repository
2. Clone their fork
3. Create a branch with their name
4. Add ONE chemical compound (choose from IDs 6-12)
5. Commit and push their changes
6. Create a Pull Request to the main ISI repository

---

## Reviewing Student Submissions

### What to Look For

#### 1. Git Workflow (40%)
- [ ] Student forked the repository
- [ ] Created a branch with their name (format: `firstname-lastname`)
- [ ] Made commits only to their branch
- [ ] Submitted PR from their fork to ISI main branch
- [ ] Descriptive commit message

#### 2. SMILES Notation (30%)
- [ ] Valid SMILES notation
- [ ] Can be verified at [PubChem](https://pubchem.ncbi.nlm.nih.gov/) or [CACTUS](https://cactus.nci.nih.gov/)
- [ ] Matches the chemical name provided

#### 3. Complete Information (20%)
- [ ] Chemical name filled in
- [ ] SMILES notation filled in
- [ ] Molecular formula filled in
- [ ] Contributor name filled in
- [ ] No empty fields

#### 4. PR Quality (10%)
- [ ] PR title follows format: "Add [Chemical] - [Name]"
- [ ] PR description is complete
- [ ] Student explained why they chose the chemical
- [ ] Included interesting facts
- [ ] Checklist completed

### Using the Validation Script

Run the validation script to automatically check for errors:

```bash
python validate.py
```

For advanced validation (recommended):
```bash
pip install rdkit
python validate.py
```

The script checks:
- JSON syntax validity
- Required fields present
- No duplicate IDs
- Valid SMILES (if RDKit installed)
- Formula matching (if RDKit installed)

---

## Grading Rubric

| Criteria | Points | Details |
|----------|--------|---------|
| **Git Workflow** | 40 | Fork, branch, commit, PR correctly |
| **Valid SMILES** | 30 | Chemically accurate SMILES notation |
| **Complete Info** | 20 | All fields filled, no blanks |
| **PR Description** | 10 | Quality, explanations, formatting |
| **Total** | 100 | |

### Deductions:
- Direct commit to main: -15 points
- Invalid SMILES: -20 points
- Missing fields: -5 points each
- Poor commit messages: -5 points
- Multiple PRs: -10 points
- Editing other entries: -20 points

---

## Handling Common Issues

### Issue: Student Committed to Main Branch
**Solution:**
1. Comment on PR asking them to create a proper branch
2. Reject the PR
3. Provide guidance from [CONTRIBUTING.md](CONTRIBUTING.md)

### Issue: Invalid SMILES Notation
**Solution:**
1. Comment on PR with the error
2. Request changes
3. Provide link to SMILES validator
4. Suggest they run `validate.py`

### Issue: Multiple Students Same Chemical
**Solution:**
- This is OK! They should use different ID slots (6-12)
- Each student can add the same chemical as long as they use different entries

### Issue: Merge Conflicts
**Solution:**
1. This shouldn't happen if students work on different IDs
2. If it does, guide student to:
   - Fetch latest changes from ISI main
   - Merge into their branch
   - Resolve conflicts
   - Push updated branch

---

## Merging Student PRs

### Manual Merge Process:
1. Review the PR against the rubric
2. Run `python validate.py` to verify
3. Check that only one entry was modified
4. Verify SMILES notation on PubChem
5. Add review comments
6. Either:
   - **Approve and Merge** if all criteria met
   - **Request Changes** with specific feedback
   - **Reject** if serious issues (direct to main, multiple entries, etc.)

### Automated Validation (Optional):
You can set up GitHub Actions to automatically run `validate.py` on each PR. Create `.github/workflows/validate.yml`:

```yaml
name: Validate Chemicals

on: [pull_request]

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.x'
      - name: Install dependencies
        run: |
          pip install rdkit-pypi
      - name: Validate
        run: python validate.py
```

---

## Expected Timeline

| Week | Activity |
|------|----------|
| Week 1 | Distribute assignment, students fork & clone |
| Week 2 | Students work on branches, submit PRs |
| Week 3 | Review PRs, request changes if needed |
| Week 4 | Merge approved PRs, grade assignment |

---

## Student Resources Provided

Students have access to:
- [README.md](README.md) - Overview and quick start
- [ASSIGNMENT.md](ASSIGNMENT.md) - Detailed instructions
- [EXAMPLES.md](EXAMPLES.md) - Example entries and common mistakes
- [CONTRIBUTING.md](CONTRIBUTING.md) - Contribution guidelines
- [QUICK_REFERENCE.md](QUICK_REFERENCE.md) - Command cheat sheet
- [validate.py](validate.py) - Validation script
- PR Template - Guides PR structure

---

## Tips for Success

1. **Set Clear Deadlines**: Give students 1-2 weeks
2. **Office Hours**: Be available for Git/GitHub questions
3. **Demo First**: Walk through the process once in class
4. **Use Validation Script**: Encourage students to use it before submitting
5. **Provide Feedback**: Give constructive comments on PRs
6. **Celebrate Success**: Acknowledge good PRs publicly (with permission)

---

## Extending the Assignment

### Advanced Variations:
1. **Add Molecular Properties**: Have students calculate molecular weight, logP, etc.
2. **3D Structures**: Convert SMILES to 3D coordinates using RDKit
3. **Visualization**: Generate molecular structure images
4. **Analysis**: Create a Python script to analyze the database
5. **Web Interface**: Build a simple web viewer for the chemicals

### Code Review Component:
- Assign students to review each other's PRs
- Teach peer review skills
- Students learn from reviewing others' work

---

## Assessment Checklist

For each student submission:
- [ ] Fork created successfully
- [ ] Branch named correctly (firstname-lastname)
- [ ] One entry modified (ID 6-12)
- [ ] All fields complete
- [ ] SMILES validated
- [ ] Formula correct
- [ ] Commit message descriptive
- [ ] PR title follows format
- [ ] PR description complete
- [ ] No merge conflicts
- [ ] JSON syntax valid

---

## Troubleshooting

### Students Can't Fork
- Check repository visibility (should be public)
- Ensure "Allow forking" is enabled

### PRs Not Appearing
- Verify students are PRing to ISI repo, not their own fork
- Check base branch is `main`

### Validation Script Fails
- Ensure Python 3.x installed
- Check file encoding (should be UTF-8)
- Install RDKit if needed: `pip install rdkit`

---

## Contact & Support

For technical issues with the assignment:
- Review the student documentation first
- Check GitHub repository issues
- Consult with IT department for GitHub access issues

---

## After Assignment Completion

### Repository Cleanup:
1. Keep all approved PRs merged
2. Document which students completed the assignment
3. Optionally create a "completed" tag
4. Archive or close remaining open PRs

### Student Feedback:
- Survey students about the assignment
- Ask what was most challenging
- Gather suggestions for improvement
- Use feedback to refine for next semester

---

## Files Overview

| File | Purpose |
|------|---------|
| README.md | Main overview, quick start |
| ASSIGNMENT.md | Detailed assignment instructions |
| EXAMPLES.md | Sample entries, common mistakes |
| CONTRIBUTING.md | Contribution guidelines |
| QUICK_REFERENCE.md | Command cheat sheet |
| INSTRUCTOR_GUIDE.md | This file - for instructors |
| chemicals.json | Main data file students edit |
| validate.py | Validation script |
| .github/PULL_REQUEST_TEMPLATE.md | PR template |

---

**Good luck with the assignment! This should be an engaging way for students to learn both Git workflows and basic cheminformatics.** 🎓🧪
