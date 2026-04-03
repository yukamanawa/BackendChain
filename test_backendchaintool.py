# test_backendchaintool.py
"""
Tests for BackendChainTool module.
"""

import unittest
from backendchaintool import BackendChainTool

class TestBackendChainTool(unittest.TestCase):
    """Test cases for BackendChainTool class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BackendChainTool()
        self.assertIsInstance(instance, BackendChainTool)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BackendChainTool()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
