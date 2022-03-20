## Concerned Tables 

- user
- user_consent

## Concerned fields

### In table user

- email
- first_name
- last_name
- username
- normalized_username
- password : fixed value = '$2a$10$TsIdgpP16FYCufdR8ldrXer1Gm64JAlPnmnEjJ9I4Z.GKEPSDCjtG'

### In table user_consent

- username (corresponding with the one in table user)

## Some recommandations

- As far as possible : keep a male first name for male first names, female first name for female first name, neutral first name for neutral first name.
- You can generate a random name for each new name.
- Warning :  the username must be unique ; it can be generated as in elaastic by concatenating the three first letters of the first name with the first foor letters of the name with an index when it is necessary in case of doublon.