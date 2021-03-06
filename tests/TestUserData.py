import unittest

from elaastic.db.anonymization.UserData import UserData

class TestUserData(unittest.TestCase):
    def test_get_is_male(self):
        user = UserData()
        # given a user with a male first name
        user.first_name = "Franck"
        # Then he is regognised as a male
        self.assertTrue(user.is_male())
        self.assertFalse(user.is_female())

    def test_get_is_female(self):
        user = UserData()
        # given a user with a female first name
        user.first_name = "Jeanine"
        # Then she is regognised as a male
        self.assertFalse(user.is_male())
        self.assertTrue(user.is_female())

    def test_gender_is_not_known(self):
        user = UserData()
        # given a user with an unreferenced first name
        user.first_name = "Guindoulous"
        # then the user is not recognised as a male neither a female
        self.assertFalse(user.is_male())
        self.assertFalse(user.is_female())

    def test_get_new_first_name(self):
        user = UserData()
        # given a user with a male first name
        user.first_name = "Franck"
        # when getting the new first name
        user.first_name = user.get_new_first_name()
        # Then the new first name is different from the old one
        self.assertNotEqual("Franck", user.first_name)
        # and the first name is still a male first name
        self.assertTrue(user.is_male())
        # given a user with a female first name
        user.first_name = "Marie"
        # when getting the new first name
        user.first_name = user.get_new_first_name()
        # Then the new first name is different from the old one
        self.assertNotEqual("Marie", user.first_name)
        # and the first name is still a female first name
        self.assertTrue(user.is_female())

    def test_get_new_last_name(self):
        # Given a user with a last_name
        user = UserData()
        initial_last_name = "Durand"
        user.last_name = initial_last_name
        self.assertEqual(user.last_name, initial_last_name)
        # When getting the new last name
        user.last_name = user.get_new_last_name()
        # then we have a new last name different from the initial one
        self.assertIsNotNone(user.last_name)
        self.assertNotEqual(user.last_name, initial_last_name)


if __name__ == '__main__':
    unittest.main()
