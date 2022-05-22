from faker import Factory
import gender_guesser.detector as gender


class UserData:

    def __init__(self):
        self.dico_username = {}
        self.faked_name_generator = Factory.create('fr_FR')
        self.gender_detector = gender.Detector()

    def is_male(self) -> bool:
        return self.gender_detector.get_gender(u"{}".format(self.first_name)) == "male"

    def is_female(self) -> bool:
        return self.gender_detector.get_gender(u"{}".format(self.first_name)) == "female"

    def get_new_first_name(self) -> str:
        if self.is_female():
            return self.faked_name_generator.first_name_female()
        if self.is_male():
            return self.faked_name_generator.first_name_male()
        return self.faked_name_generator.first_name()

    def get_new_last_name(self) -> str:
        # TODO implement and test
        return ''

    def get_new_email(self) -> str:
        # TODO implement and test
        return ''

    def get_new_username(self) -> str:
        # TODO implement and test
        return ''

    def get_new_normalized_username(self) -> str:
        # TODO implement and test
        return ''

    def get_new_password(self) -> str:
        return '$2a$10$TsIdgpP16FYCufdR8ldrXer1Gm64JAlPnmnEjJ9I4Z.GKEPSDCjtG'

    def get_new_user(self):
        # TODO test
        new_user = UserData()
        new_user.first_name = self.get_new_first_name()
        new_user.last_name = self.get_new_last_name()
        new_user.email = self.get_new_email()
        new_user.username = self.get_new_username()
        new_user.normalized_username = self.get_new_normalized_username()
        new_user.pasword = self.get_new_password()
        return new_user


