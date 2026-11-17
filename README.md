# Equipment Failure Prediction

A standalone, reproducible **manufacturing** machine learning project for Jupyter Notebook using **synthetic** data. This repository is independent of the healthcare, manufacturing and eMobility companion repositories.

## Business problem
Predict equipment condition and failures. The notebook explains descriptive statistics, confidence intervals, Welch t-test, Mann–Whitney U, chi-square, Cohen's d, Pearson/Spearman correlations, Shapiro normality test, outlier analysis, data preprocessing, 10 classifiers including baseline, cross-validation, hyperparameter tuning, PR-AUC/ROC-AUC, feature importance and model persistence. These are representative methods, not every statistical method or ML model.

## Start on Windows (Anaconda Prompt)

Extract the ZIP to `C:\Data Science\manufacturing_ml_project`, then:

```cmd
cd /d "C:\Data Science\manufacturing_ml_project"
conda create -n manufacturing-ml python=3.11 -y
conda activate manufacturing-ml
python -m pip install -r requirements.txt
python -m ipykernel install --user --name manufacturing-ml --display-name "Python (manufacturing-ml)"
python -m pytest -q
jupyter notebook
```

Open `notebooks/01_manufacturing_ml.ipynb` and select **Run All**. Launch Jupyter from the project root for correct relative paths. The notebook generates its own dataset. Output CSVs, model files and reports are ignored by Git.

## Structure

```text
manufacturing_ml_project/
├── notebooks/01_manufacturing_ml.ipynb
├── src/project_utils.py
├── src/__init__.py
├── tests/test_project.py
├── docs/GITHUB_UPLOAD_GUIDE.md
├── data/.gitkeep
├── models/.gitkeep
├── reports/.gitkeep
├── README.md
├── requirements.txt
├── .gitignore
└── LICENSE
```

## GitHub

Publish this project to its **own repository** named `manufacturing-machine-learning-project`. See `docs/GITHUB_UPLOAD_GUIDE.md` for complete steps and troubleshooting.

> Educational use only. Synthetic results do not establish real-world medical or operational performance. Do not upload real patient data, secrets, or confidential records.
