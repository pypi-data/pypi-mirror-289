from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from random_forest_package.exceptions import ModelCreationError


def create_random_forest_classifier(n_estimators=100, max_depth=None, random_state=None):
    try:
        if not isinstance(n_estimators, int) or n_estimators <= 0:
            raise ValueError("n_estimators must be a positive integer")
        return RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth, random_state=random_state)
    except ValueError as e:
        raise ModelCreationError(f"Failed to create random forest model: {e}") from e


def create_random_forest_regressor(n_estimators=100, max_depth=None, random_state=None):
    try:
        if not isinstance(n_estimators, int) or n_estimators <= 0:
            raise ValueError("n_estimators must be a positive integer")
        return RandomForestRegressor(n_estimators=n_estimators, max_depth=max_depth, random_state=random_state)
    except Exception as e:
        raise ModelCreationError(f"Failed to create RandomForestRegressor: {e}") from e
