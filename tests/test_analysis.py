# test_analysis.py

import unittest
from unittest.mock import patch
from yourteamrepo.analysis import Analysis

class TestAnalysis(unittest.TestCase):

    def test_init(self):
        analysis_obj = Analysis('config.yml')
        self.assertIsNotNone(analysis_obj.config)

    @patch('yourteamrepo.analysis.Analysis._load_config')
    def test_load_data(self, mock_load_config):
        analysis_obj = Analysis('config.yml')
        analysis_obj.load_data()
        self.assertIsNotNone(analysis_obj.data)

    def test_compute_analysis(self):
        analysis_obj = Analysis('config.yml')
        analysis_obj.load_data()
        result = analysis_obj.compute_analysis()
        self.assertIsNotNone(result)

    def test_plot_data(self):
        analysis_obj = Analysis('config.yml')
        fig = analysis_obj.plot_data()
        self.assertIsNotNone(fig)

if __name__ == '__main__':
    unittest.main()
