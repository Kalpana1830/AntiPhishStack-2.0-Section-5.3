"""CatBoost fitting helper from report section 5.3."""

from catboost import CatBoostClassifier


def train_catboost(X_train, y_train):
    """Fit and return CatBoost on caller-supplied training values."""
    model = CatBoostClassifier(iterations=200, depth=6, verbose=0)
    model.fit(X_train, y_train)
    return model
