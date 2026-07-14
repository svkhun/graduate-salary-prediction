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

The original CSV is intentionally excluded from this public-ready repository. Only use a dataset that you are authorised to use and publish.

```powershell
python train_model.py --data "C:\path\to\your\authorised_dataset.csv" --output model.pkl
```

This command overwrites `model.pkl`, prints RMSE and R² on a fixed 80/20 train-test split, and keeps the app's required feature engineering consistent with training.

## Data and privacy

The original project contained a 100,000-row CSV with a `student_id` field. It is not included here because its licence, origin, and anonymisation status need to be confirmed before a public release. See [data/README.md](data/README.md) before adding data to GitHub.

## Research limitations

The saved model is intentionally described as an estimate rather than a decision tool. Historical notebook outputs show limited and inconsistent predictive performance across experiments (R² values roughly 0.01 to 0.21). Reproduce evaluation from a versioned, authorised dataset and report fresh metrics before making any accuracy claim.

More detail is available in the [model card](docs/MODEL_CARD.md).

## Notebooks

- `01_data_cleaning.ipynb` — cleaning steps
- `02_exploratory_data_analysis.ipynb` — exploratory analysis and visualisation
- `03_model_training.ipynb` — model experiments
- `04_final_research_workflow.ipynb` — final research workflow

The original notebooks refer to the CSV filename `D3_student_placement_prediction_dataset_2026 (1).csv` in the repository root. Do not add that file to a public repository until the checks in `data/README.md` are complete.

## Licence

No licence has been selected for this repository yet. Choose a licence only after confirming that the code, model, notebooks, and any dataset you publish can legally be distributed under it.
