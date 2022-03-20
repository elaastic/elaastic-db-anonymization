from faker import Factory
import gender_guesser.detector as gender

class UserData:

  def __init__(self):
    self.dico_username = {}
    self.fakedNameGenerator = Factory.create('fr_FR')
    self.genderDetector = gender.Detector()

  def isMale(self) -> bool:
    return self.genderDetector.get_gender(u"{}".format(self.first_name))=="male"

  def isFemale(self) -> bool:
    return self.genderDetector.get_gender(u"{}".format(self.first_name))=="female"

  def getNewFirstName(self) -> str:
    if self.isFemale():
       return self.fakedNameGenerator.first_name_female()
    if self.isMale():
      return self.fakedNameGenerator.first_name_male()
    return self.fakedNameGenerator.first_name()


if __name__ == '__main__':
    def testGetIsMale():
        user = UserData()
        user.first_name = "Franck"
        assert(user.isMale())

    testGetIsMale()


