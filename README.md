# AntiPhishStack 2.0 — Section 5.3 Implementation Draft

**Status: Published on GitHub — Section 5.3 implementation draft.**

This repository draft organizes the code snippets in section 5.3, “Method of Implementation,” of the supplied project report into Python modules. It is a reconstruction of those snippets, not a complete or validated end-to-end phishing-detection system.

**Authors credited in the report:** A Kalpana and S Irshad Ahammad.

## What is implemented here

- CSV loading and basic cleaning: removes the HTTP/HTTPS prefix and optional `www.`, then drops duplicate and missing rows.
- An 80/20 train/test split using `random_state=42`.
- Five URL features, in order: URL length, number of dots, IPv4-address pattern present, number of subdomains, and total occurrences of `@`, `-`, `_`, and `=`.
- A BERT module that loads `bert-base-uncased` and returns a 64-value representation.
- A Keras bidirectional-GRU/attention module that returns a sequence of 64-value representations.
- A CatBoost helper that fits a `CatBoostClassifier` with 200 iterations and depth 6 on caller-supplied training data.
- A Flask `/predict` endpoint that extracts the five URL features and sends them to a saved CatBoost model.
- A SHAP TreeExplainer helper that returns SHAP values for supplied feature values.

## Important limits of the source snippets

The report does not show a complete training or inference pipeline. In particular:

- The BERT and GRU modules are standalone and are **not connected to each other or to CatBoost** in the shown code. The CatBoost helper accepts arbitrary `X_train` and `y_train`; no fusion of transformer and GRU outputs is implemented here.
- The BERT module ends with a 64-unit linear layer, not a classification layer. No tokenizer use, fine-tuning loop, or label mapping is shown.
- The GRU module has no tokenizer/vocabulary construction or training loop, and returns a sequence tensor rather than a final class prediction.
- The Flask API uses only the five hand-engineered URL features and the saved CatBoost model. The report does not provide code that trains and saves `models/catboost_model.cbm`; no model artifact or dataset is included in this draft. The API and SHAP modules both expect that model file.
- In the API response, prediction value `1` is labeled `Phishing`; every other value is labeled `Benign`. The supplied snippets do not define or verify the training labels.
- The SHAP helper returns raw explainer values; it does not format or display a human-readable explanation.
- The API snippet runs Flask with `debug=True` and has no request validation or production security setup. It is not production-ready as written.

No accuracy, detection-rate, deployment-readiness, or integrated hybrid-model claims are made by this repository draft.

## Layout

```text
scripts/
  data_preprocessing.py
  feature_engineering.py
  transformer_model.py
  gru_model.py
  meta_classifier.py
  flask_api.py
  shap_explainer.py
models/                 # expected location for a separately supplied CatBoost model
requirements.txt
```

## Setup

Create a Python virtual environment compatible with the listed package releases, then install the dependencies:

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
python -m pip install -r requirements.txt
```

The BERT class loads the pretrained `bert-base-uncased` model when instantiated, which may download model files from Hugging Face if they are not already cached.

## Data expected by preprocessing

`load_and_clean_data(file_path)` expects a CSV with columns named `url` and `label`. It returns the cleaned dataframe. `split_data(df)` returns `X_train`, `X_test`, `y_train`, and `y_test`, where the `X` values are the URL strings; this helper does not extract the five CatBoost features for you.

## CatBoost API

The API expects a separately prepared model file at `models/catboost_model.cbm`, relative to the repository root. This draft does not create that file. Once a compatible model is supplied, run from the repository root:

```bash
python -m scripts.flask_api
```

The endpoint accepts a JSON body such as:

```json
{"url": "https://example.com/path"}
```

It returns the submitted URL and the label selected by the code's `prediction == 1` condition. The expected feature order is the order listed above.

## Source note

Implementation details are based on section 5.3 of the project report supplied for this task. This local draft has not been pushed to a public repository and should be reviewed by the credited authors before publication.
