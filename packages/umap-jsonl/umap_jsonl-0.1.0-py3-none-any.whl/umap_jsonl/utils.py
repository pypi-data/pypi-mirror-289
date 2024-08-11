import jsonlines
import logging
from sklearn.feature_extraction import DictVectorizer
from sklearn.impute import SimpleImputer
import numpy as np

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def load_jsonl_file(filepath):
    logger.info(f"Loading JSONL file from {filepath}")
    try:
        with jsonlines.open(filepath) as reader:
            data = [obj for obj in reader]
        logger.info(f"Loaded {len(data)} records from {filepath}")
        return data
    except Exception as e:
        logger.error(f"Failed to load JSONL file: {e}")
        raise

def extract_features(data):
    try:
        logger.info("Extracting features using DictVectorizer")
        vectorizer = DictVectorizer()
        features = vectorizer.fit_transform(data)
        imp = SimpleImputer(missing_values=np.nan, strategy='constant', fill_value=None)
        imp.fit(features)
        imputed = imp.transform(features)
        logger.info(f"Extracted features with shape {imputed.shape}")
        return imputed
    except Exception as e:
        logger.error(f"Failed to extract features: {e}")
        raise

def default_config():
    return {
        'n_neighbors': 15,
        'min_dist': 0.1,
        'n_components': 2,
        'n_clusters': 3,
        'output_file': 'output.png',
        'plot_size': "8,6"
    }
