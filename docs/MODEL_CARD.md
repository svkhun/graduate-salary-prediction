# Model Card

## Model summary

- **Task:** Regression of `salary_package_lpa`
- **Model artifact:** `model.pkl`
- **Model family:** scikit-learn pipeline with feature scaling and Linear Regression
- **Intended use:** Research demonstration and exploratory discussion only
- **Out of scope:** Salary guarantees, recruitment decisions, compensation decisions, or advice about an individual's career prospects

## Inputs and output

The application accepts aptitude, coding, communication, and logical-reasoning scores. It derives `total_skill` and `avg_skill`, so the model receives six numeric features. The output unit is LPA, as defined by the training dataset.

## Data status

The source CSV is included for reproducibility. It is the [Student Placement Prediction Dataset 2026](https://www.kaggle.com/datasets/sehaj1104/student-placement-prediction-dataset-2026), which Kaggle describes as a 100,000-row synthetic dataset and lists under CC0 Public Domain. The `student_id` field is therefore treated as a synthetic identifier, not personal data.

## Evaluation status

The project notebooks contain exploratory results from different experiments. Reported R² values vary from approximately 0.01 to 0.21, and one four-feature experiment reports RMSE of about 1.41 LPA. These are historical notebook outputs, not a validated claim for the saved artifact. Re-run `train_model.py` on a versioned, authorised dataset and preserve the resulting evaluation report before publishing a performance figure.

## Limitations and risks

- The model uses only four self-reported or assessed skill scores and derived values; it omits many important salary factors.
- The data's population, geography, collection period, and currency context must be verified before the model is applied anywhere else.
- A prediction can be wrong for an individual and may encode bias present in the training data.
- The target unit is not Thai baht. Do not use the output to compare or negotiate Thai salaries without a validated conversion and locally representative data.

## Recommended next steps

1. Confirm data provenance and publish only an authorised, anonymised dataset or a documented synthetic sample.
2. Version the dataset and record preprocessing decisions.
3. Use cross-validation and evaluate error by relevant subgroups where lawful and appropriate.
4. Compare a baseline with alternative models, then document the selected model and metrics.
5. Test the app with valid score ranges and add model/version metadata to releases.
