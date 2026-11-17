# Publish Equipment Failure Prediction to GitHub (Windows)

**This is a separate GitHub repository**, not a folder in a combined repository.

1. Extract the ZIP to `C:\Data Science\manufacturing_ml_project`. Open **Anaconda Prompt**.
2. Run `cd /d "C:\Data Science\manufacturing_ml_project"` then `dir`. Confirm `README.md`, `requirements.txt`, `notebooks`, `src`, and `tests` are visible. If not, navigate to the actual extracted folder.
3. Install Git from https://git-scm.com/downloads/win if necessary, then verify with `git --version`.
4. Configure identity once: `git config --global user.name "Your Name"` and `git config --global user.email "you@example.com"`.
5. Test the project:

```cmd
conda create -n manufacturing-ml python=3.11 -y
conda activate manufacturing-ml
python -m pip install -r requirements.txt
python -m pytest -q
jupyter notebook
```

6. On https://github.com/new create an **empty** repository named `manufacturing-machine-learning-project`. Do not pre-create README, license, or .gitignore.
7. From the **same project root** in Anaconda Prompt run:

```cmd
git init
git branch -M main
git add .
git status
git commit -m "Initial manufacturing ML project"
git remote add origin https://github.com/YOUR_USERNAME/manufacturing-machine-learning-project.git
git push -u origin main
```

Replace `YOUR_USERNAME`. Confirm no private data or secrets in `git status`. Browser sign-in or Git Credential Manager may prompt for authentication.

8. To manage this repository in **GitHub Projects** (optional): GitHub profile → Projects → New project → Board; name it `Equipment Failure Prediction Delivery`, then add tasks for EDA, statistics, modeling, testing and documentation. Link issues from **this repository**.

9. Future updates: `git add .`, `git commit -m "Improve model"`, `git push`. Do not repeat `git init` or `git remote add origin`.

## Troubleshooting

- `pathspec 'README.md' did not match any files`: wrong folder; run `cd` and `dir`, then `git add .`.
- `remote origin already exists`: check `git remote -v`; use `git remote set-url origin URL` if needed.
- Import error: start Jupyter from the repository root.
- Push rejected: verify branch and remote; do not force push without checking.
- `.gitignore` prevents generated data/models/reports from being committed.
