"""SHAP TreeExplainer helper reconstructed from report section 5.3."""

import shap
from catboost import CatBoostClassifier

model = CatBoostClassifier()
model.load_model("models/catboost_model.cbm")
explainer = shap.TreeExplainer(model)


def explain_prediction(url_features):
    """Return raw SHAP values for one supplied feature vector."""
    return explainer.shap_values([url_features])
