import unittest
from unit_test_tasks import AuthorizationError,access_resource

class TestUnitTestTasks(unittest.TestCase):
    def test_access_resource_invalid_role(self):
        with self.assertRaises(AuthorizationError) as cxt:
            access_resource('not admin')
        
        self.assertEqual(str(cxt.exception),'Access denied')

if(__name__ == '__main__'):
    unittest.main()