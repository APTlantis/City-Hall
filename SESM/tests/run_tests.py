import unittest
import sys
from pathlib import Path

def main():
    # Resolve the start directory relative to this script
    start_dir = str(Path(__file__).parent)
    
    print("Discovering and running tests under tests/...")
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir=start_dir, pattern='test_*.py')
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    if not result.wasSuccessful():
        print("Test suite failed.")
        sys.exit(1)
    
    print("Test suite completed successfully.")
    sys.exit(0)

if __name__ == '__main__':
    main()
