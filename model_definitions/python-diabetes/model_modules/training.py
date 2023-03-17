from xgboost import XGBClassifier
from sklearn.preprocessing import MinMaxScaler
from sklearn.pipeline import Pipeline
from nyoka import xgboost_to_pmml
from teradataml import DataFrame
from aoa import (
    record_training_stats,
    save_plot,
    aoa_create_context,
    ModelContext
)

import joblib


def train(context: ModelContext, **kwargs):
    aoa_create_context()

