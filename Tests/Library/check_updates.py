import unittest
import SciPubStyle.library as library

class Nature(unittest.TestCase):
    def test_nature_research_update(self):
        for key, value in library.NATURE_RESEARCH_UPDATE.items():
            self.assertEqual(value, library.NATURE_RESEARCH[key])
class PhysRev(unittest.TestCase):
    def test_prl_update(self):
        for key, value in library.PHYSICAL_REIVEW_LETTERS_UPDATE.items():
            self.assertEqual(value, library.PHYSICAL_REVIEW_LETTERS[key])
if __name__ == '__main__':
    unittest.main()
