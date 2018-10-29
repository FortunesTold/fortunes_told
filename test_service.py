from service import *
import unittest

class TestService(unittest.TestCase):
    """Python unit tests for difficult/interesting service method scenarios."""
    

    def test_random_fortunes_contained_in_fortunes_list(self):
        """Test that random fortunes output is contained in available fortunes."""
        
        self.assertIn(random_fortune(), fortunes)










########################
if __name__ == '__main__':
    unittest.main()