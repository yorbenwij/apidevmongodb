# 4.1 mongodb

dit is de repo waar ik met mongodb ben bezig geweest. we moesten normaal van heel onze api een copy maken in de mongodb maar hier had ik niet genoeg tijd voor ik heb bij het opzetten van de mongodb heel lang in de knoop gezeten maar uiteindelijk heb ik er toch iets kunnen uithalen

uiteindelijk na dat ik door had hoe mongodb werkte is het eigenlijk niet zo moeilijk.

In mongodb wordt er geen gebruik gemaakt van tabelen zoals in sql. Mongodb maakt gebruik van bson of ook wel genoemd binary json dit kunnen we zelf niet lezen maar in mongodb zitten er tools dat dit gaan omzetten in leesbare json voor ons.
hier zie je een voorbeeld van een collection in mijn mongodb database.

![img_1](https://github.com/yorbenwij/apidevmongodb/assets/91123168/ccee3541-d29f-4735-9a13-47572a560821)


dit is data dat in een collection zit die ik heb aangemaakt.
mongodb atlas is een cloud platform dus moeten we op een andere manier gaan conecteren naar onze database.
![img](https://github.com/yorbenwij/apidevmongodb/assets/91123168/043bd40b-ccec-426c-849a-e7300b936b74)


dit is onze database config file en zoals je kunt zien zit hier niet zo veel in zoals we een sql database zouden maken want we moeten onze database cluster eerst gaan aanmaken in de GUI van mondodb atlas. als we dit gedaan hebben krijgen we een connection string die er als volgt ongeveer uit ziet
### mongodb+srv://"gebruikersnaam":"wachtwoord"@"cluster-URL"/"databasenaam"

deze zetten we dan in MongoClient()
je hebt ook de optie om de link te testen. hier kan je dus gaan zien of je connectie met de database werkt dit doen we door het volgende te doen.
![img_2](https://github.com/yorbenwij/apidevmongodb/assets/91123168/c451b0e1-3dde-4a64-bcd1-166b36dc2529)

als we op "view full code sample" klikken krijgen we een code te zien deze copy paste je gewoon in je main.py en run de code dit gaat je database pingen en als het werkt ga je in de terminal tezien krijgen "pinged your deployment. enz."
als dit werkt weet je dat de connectie met de database werkt en kan je beginnen met de api en de andere dingen te maken

# screenshots postman and api docs
## api docs
![img_3](https://github.com/yorbenwij/apidevmongodb/assets/91123168/894a8fcd-f85e-4650-bb04-34ab6c1850d4)
![img_4](https://github.com/yorbenwij/apidevmongodb/assets/91123168/757aa7fd-0f1c-4eaa-81f9-7f144bee1028)
![img_5](https://github.com/yorbenwij/apidevmongodb/assets/91123168/e6e9ed64-1410-4a18-864b-350f8dac3f39)
![img_6](https://github.com/yorbenwij/apidevmongodb/assets/91123168/ab53cd29-f522-4dc8-a1a4-b4b32e360107)
![img_7](https://github.com/yorbenwij/apidevmongodb/assets/91123168/1a407bdc-3e87-4598-a145-a6149125bf24)
![img_8](https://github.com/yorbenwij/apidevmongodb/assets/91123168/e7a36cc1-29d6-4375-862f-7cd8d4fe4b44)
![img_9](https://github.com/yorbenwij/apidevmongodb/assets/91123168/0389fd38-b043-4cf4-8749-57fc490975ef)
![img_10](https://github.com/yorbenwij/apidevmongodb/assets/91123168/982d57cd-4347-40b2-9325-621ac7774f8f)
![img_11](https://github.com/yorbenwij/apidevmongodb/assets/91123168/c3aa15b4-1f83-43e8-99f0-cf38257b5c1a)
![img_12](https://github.com/yorbenwij/apidevmongodb/assets/91123168/d16373e9-dcff-4a00-91bf-d74595d0561b)
![img_13](https://github.com/yorbenwij/apidevmongodb/assets/91123168/2a43fabd-fffe-4746-94a9-3fc206649af0)
![img_14](https://github.com/yorbenwij/apidevmongodb/assets/91123168/b3f7d3f8-d9d0-4b3c-b413-1739870ddfaf)
de screenshots hier boven tonen aan dat de endpoints die ik heb werken. nu kunnen we ook naar het dashboard gaan om naar de monitoring te kijken en daar gaan we zien dat er verschillende wirte's zijn.
![img_15](https://github.com/yorbenwij/apidevmongodb/assets/91123168/0847f826-5358-44ab-8ef3-39baf11b3539)
