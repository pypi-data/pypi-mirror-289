import unittest
from unittest.mock import patch, MagicMock
import numpy as np
from umap_jsonl.utils import load_jsonl_file, extract_features, default_config

class TestUtils(unittest.TestCase):

    @patch('umap_jsonl.utils.jsonlines.open')  # Updated import path
    def test_load_jsonl_file(self, mock_jsonlines_open):
        mock_jsonlines_open.return_value = MagicMock()
        mock_jsonlines_open.return_value.__enter__.return_value = [
            {'feature1': 1, 'feature2': 2},
            {'feature1': 3, 'feature2': 4}
        ]
        data = load_jsonl_file('test.jsonl')
        self.assertEqual(len(data), 2)

    def test_extract_features(self):
        data = [{'feature1': 1, 'feature2': 2}, {'feature1': 3, 'feature2': 4}]
        features = extract_features(data)
        self.assertEqual(features.shape, (2, 2))

    def test_default_config(self):
        config = default_config()
        self.assertEqual(config['n_neighbors'], 15)
        self.assertEqual(config['output_file'], 'output.png')

if __name__ == '__main__':
    unittest.main()
