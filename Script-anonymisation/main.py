from mysql.connector import (connection)
from faker import Factory
import gender_guesser.detector as gender
import unidecode



## connexion to database

cnx = connection.MySQLConnection(user='elaastic', password='elaastic',
                                 host='127.0.0.1', port='6603',
                                 database='elaastic-questions')



## chepa comment on appel ca moi wsh chuis en terminale EH OH

cursor1 = cnx.cursor(buffered=True)
cursor2 = cnx.cursor(buffered=True)
print(cursor2.execute("SELECT * FROM terms;"))
detect = gender.Detector()

crea = Factory.create('fr_FR')


def anonynisation(fixedvalue_newpasswd):

  #j ai fais un dico (PAS UN LAROUSSE T AS CAPTÉ)
  dico_username = {}
  
  
  #beh la j ai fais comme le tuto
  cursor1.execute("SELECT first_name, last_name, username, email, normalized_username, password FROM user ")


  #la aussi
  for (first_name, last_name, username, email, normalized_username, password) in cursor1:
    

    #ok la ca se corse fais gaffe, on check si c est un monsieur ou une madame ou autre et en fonction on créé un nouveau prénom

    if detect.get_gender(u"{}".format(first_name))=="female":
      new_first_name = crea.first_name_female()
    if detect.get_gender(u"{}".format(first_name))=="male":
      new_first_name = crea.first_name_male()
    else :
      new_first_name = crea.first_name()

    

    #la on créé le nom

    new_last_name = crea.last_name()
    

    #la le username et on fait en sorte qu il soit unique avec une méthode que j ai inventé pcq j ai pas compris cque mon papa il a dit

    new_username = "{}{}".format(new_first_name[:3],new_last_name[:4])
    if new_username in dico_username:
      dico_username[new_username] +=1
      a = str(dico_username[new_username])
      new_username = "{}{}{}".format(new_first_name[:3],new_last_name[:4], a)
    else:
      dico_username[new_username] = 0
      new_username = "{}{}".format(new_first_name[:3],new_last_name[:4])


    # la on le normalize

    new_normalized_username = unidecode.unidecode(new_username)


    #La on créé le mail

    new_email = '{}@example.com'.format(new_normalized_username)


    # et le mdp

    new_password = fixedvalue_newpasswd

    ### la on va modif la base omg ###

    #beh on modifie ducoup hein

    cursor2.execute("UPDATE user SET first_name = '{}', last_name = '{}', email = '{}', password = '{}' WHERE username = '{}'".format(new_first_name, new_last_name, new_email, new_password, username))
    #cursor2.execute("UPDATE user_consent SET username = '{}' WHERE username = '{}'".format(new_username, username))


#on appel la fonction stylax a max
anonynisation('$2a$10$TsIdgpP16FYCufdR8ldrXer1Gm64JAlPnmnEjJ9I4Z.GKEPSDCjtG')
print(cursor2.execute("SELECT email FROM user;"))
#enft je l ai pas encore fais ca

cnx.close()


#class DataAccessService:

 # def __init__(self, connection: MySQLConnection):
  #  self.connection = connection

  #def updateUserForUsername(self, username: str):
   # cursor = cnx.cursor(buffered=True)
    #cursor.execute("UPDATE user SET first_name = '{}', last_name = '{}', email = '{}', password = '{}' WHERE username = '{}'".format(new_first_name, new_last_name, new_email, new_password, username))
    


