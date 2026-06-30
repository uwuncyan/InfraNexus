# test_infranexus.py
"""
Tests for InfraNexus module.
"""

import unittest
from infranexus import InfraNexus

class TestInfraNexus(unittest.TestCase):
    """Test cases for InfraNexus class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = InfraNexus()
        self.assertIsInstance(instance, InfraNexus)
        
    def test_run_method(self):
        """Test the run method."""
        instance = InfraNexus()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
