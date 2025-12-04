
import unittest
from auth import register, login

class TestAuth(unittest.TestCase):
    def test_register_and_login(self):
        register("testuser","pass")
        self.assertTrue(login("testuser","pass"))

if __name__ == '__main__':
    unittest.main()
