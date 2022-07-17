from userproject import Property, User
import unittest

class TestProperty(unittest.TestCase):
    def test_property(self):
        testProperty = Property()
        self.assertEquals("I am a property", testProperty.description)

class TestUser(unittest.TestCase):
    def test_user(self):
        testUser = User()
        self.assertTrue(isinstance(testUser, dict))