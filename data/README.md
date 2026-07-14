# Dataset guidance

The original project used `D3_student_placement_prediction_dataset_2026 (1).csv`, a 100,000-row CSV containing a `student_id` field, demographic and education-related variables, skill scores, placement status, and the `salary_package_lpa` target.

This repository deliberately does **not** include that CSV. Before adding any data to GitHub, confirm all of the following:

1. You created the data or have explicit permission and a compatible licence to publish it.
2. The data is synthetic, or all direct and indirect identifiers have been removed.
3. The records cannot reasonably be re-identified when combined with public information.
4. Publishing the salary target and other attributes is permitted by your institution or data owner.
5. You document the data source, collection period, population, preprocessing, and known limitations.

For private research, store the raw CSV outside the repository or under `data/raw/`; both locations are ignored by `.gitignore`. To run the original notebooks without changing their paths, place an authorised copy in the repository root with its original filename.

Do not commit real student records, contact details, API keys, or credentials.
