#!/usr/bin/env python3
import unittest
import os
import sys
import argparse
from datetime import datetime

# Add scripts directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'scripts'))

# Import test cases
from tc_saucedemo import SauceDemoTest
from tc_dynamic_loading import DynamicLoadingTest
from tc_demoblaze import DemoBlazeTest
from tc_formy import FormyTest

def create_test_suite(test_name=None):
    """Create a test suite with the specified test or all tests if none specified."""
    suite = unittest.TestSuite()
    
    if test_name is None or test_name == 'saucedemo':
        suite.addTest(unittest.makeSuite(SauceDemoTest))
    
    if test_name is None or test_name == 'dynamic':
        suite.addTest(unittest.makeSuite(DynamicLoadingTest))
    
    if test_name is None or test_name == 'demoblaze':
        suite.addTest(unittest.makeSuite(DemoBlazeTest))
    
    if test_name is None or test_name == 'formy':
        suite.addTest(unittest.makeSuite(FormyTest))
    
    return suite

def run_tests(test_name=None, verbose=True):
    """Run the tests with the specified test name or all tests if none specified."""
    # Ensure directories exist
    os.makedirs('relatorios', exist_ok=True)
    os.makedirs('relatorios/screenshots', exist_ok=True)
    
    # Create test suite
    suite = create_test_suite(test_name)
    
    # Create a test runner
    runner = unittest.TextTestRunner(verbosity=2 if verbose else 1)
    
    # Run the tests
    print(f"\n{'=' * 80}")
    print(f"Running Selenium Test Suite: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'=' * 80}\n")
    
    result = runner.run(suite)
    
    # Print summary
    print(f"\n{'=' * 80}")
    print(f"Test Summary:")
    print(f"  Ran {result.testsRun} tests")
    print(f"  Failures: {len(result.failures)}")
    print(f"  Errors: {len(result.errors)}")
    print(f"  Skipped: {len(result.skipped)}")
    print(f"{'=' * 80}\n")
    
    return result

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run Selenium test cases')
    parser.add_argument('--test', type=str, help='Specify a test to run (saucedemo, dynamic, demoblaze, formy)')
    parser.add_argument('--quiet', action='store_true', help='Run in quiet mode with less output')
    
    args = parser.parse_args()
    
    result = run_tests(args.test, not args.quiet)
    
    # Exit with appropriate code
    sys.exit(len(result.failures) + len(result.errors))