from teradataml import copy_to_sql, DataFrame
from aoa import (
    record_scoring_stats,
    aoa_create_context,
    ModelContext
)

import joblib
import pandas as pd


def score(context: ModelContext, **kwargs):

    aoa_create_context()
