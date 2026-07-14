# Graduate Salary Prediction Research Prototype

A Data Science research project and Streamlit web prototype for estimating the entry-level salary of newly graduated computer-engineering students from four skill scores. The application predicts the `salary_package_lpa` value used in the research dataset.

> **Important:** This project is a research prototype, not a salary guarantee. Its predictions may be inaccurate and should be used only as supporting information. Actual salaries depend on job role, location, labour-market conditions, experience, skills, and each employer's criteria. The model needs further development and evaluation before any real-world use.

## What the web app uses

The user supplies four scores from 0 to 100:

- Aptitude
- Coding skill
- Communication skill
- Logical reasoning

The app derives `total_skill` and `avg_skill`, then passes all six features to the saved scikit-learn Linear Regression pipeline in `model.pkl`. The prediction is expressed in **LPA**, the unit named by the training dataset. It must not be interpreted as a Thai-baht estimate.

## Repository layout

```text
.
├── app.py                 # Streamlit web application
├── model.pkl              # Saved model used by the app
├── train_model.py         # Reproducible training and evaluation script
├── requirements.txt       # Python dependencies
├── notebooks/             # Original research notebooks
├── data/README.md         # Dataset publication and use guidance
└── docs/MODEL_CARD.md     # Scope, limitations, and evaluation notes
```

## Run the web app

Use Python 3.14, which matches the original virtual environment.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run app.py
```

The application opens locally in a browser. `model.pkl` must remain next to `app.py`.

## Publish to GitHub

This prepared folder is already an initialised local Git repository on the `main` branch, with the public-safe files staged. Configure your own Git identity, create a new **empty** repository on GitHub, then run:

```powershell
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"
git commit -m "Initial commit: graduate salary prediction research prototype"
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
git push -u origin main
```

Do not initialise the GitHub repository with a README, `.gitignore`, or licence before the first push; this avoids an unnecessary merge. Choose repository visibility and a licence only after completing the data and ownership checks below.

## Train a new model

The public synthetic dataset used by this project is included in the repository. It is published on Kaggle under the CC0 Public Domain licence; see [data/README.md](data/README.md) for attribution and scope.

```powershell
python train_model.py --data "D3_student_placement_prediction_dataset_2026 (1).csv" --output model.pkl
```

This command overwrites `model.pkl`, prints RMSE and R² on a fixed 80/20 train-test split, and keeps the app's required feature engineering consistent with training.

## Data and privacy

The included 100,000-row dataset is a synthetic dataset created for educational, research, and machine-learning use. Kaggle lists it under the CC0 Public Domain licence. Its `student_id` field is a synthetic identifier, not a real student record. See [data/README.md](data/README.md) for the source and attribution.

## Research limitations

The saved model is intentionally described as an estimate rather than a decision tool. Historical notebook outputs show limited and inconsistent predictive performance across experiments (R² values roughly 0.01 to 0.21). Reproduce evaluation from a versioned, authorised dataset and report fresh metrics before making any accuracy claim.

More detail is available in the [model card](docs/MODEL_CARD.md).

## Notebooks

- `01_data_cleaning.ipynb` — cleaning steps
- `02_exploratory_data_analysis.ipynb` — exploratory analysis and visualisation
- `03_model_training.ipynb` — model experiments
- `04_final_research_workflow.ipynb` — final research workflow

The original notebooks refer to `D3_student_placement_prediction_dataset_2026 (1).csv` in the repository root; that file is included for reproducibility.

## Licence

The included dataset is CC0 Public Domain according to its Kaggle data card. No licence has been selected for this repository's original code, model, and notebooks yet; choose one before inviting others to reuse them.
