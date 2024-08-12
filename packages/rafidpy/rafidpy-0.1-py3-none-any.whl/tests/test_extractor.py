import unittest
from color_extractor import extract_dominant_colors

class TestColorExtractor(unittest.TestCase):
    def test_extract_dominant_colors(self):
        try:
            colors = extract_dominant_colors('test_image.png', max_clusters=5, save_plots=False)
            self.assertIsNotNone(colors)
            self.assertGreater(len(colors), 0)
        except Exception as e:
            self.fail(f"extract_dominant_colors raised an exception: {e}")

if __name__ == '__main__':
    unittest.main()

