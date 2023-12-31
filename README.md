# 4.1 mongodb

dit is de repo waar ik met mongodb ben bezig geweest. we moesten normaal van heel onze api een copy maken in de mongodb maar hier had ik niet genoeg tijd voor ik heb bij het opzetten van de mongodb heel lang in de knoop gezeten maar uiteindelijk heb ik er toch iets kunnen uithalen

uiteindelijk na dat ik door had hoe mongodb werkte is het eigenlijk niet zo moeilijk.

In mongodb wordt er geen gebruik gemaakt van tabelen zoals in sql. Mongodb maakt gebruik van bson of ook wel genoemd binary json dit kunnen we zelf niet lezen maar in mongodb zitten er tools dat dit gaan omzetten in leesbare json voor ons.
hier zie je een voorbeeld van een collection in mijn mongodb database.

![img_1.png](pictures/img_1.png)

dit is data dat in een collection zit die ik heb aangemaakt.
mongodb atlas is een cloud platform dus moeten we op een andere manier gaan conecteren naar onze database.
![img.png](pictures/img.png)

dit is onze database config file en zoals je kunt zien zit hier niet zo veel in zoals we een sql database zouden maken want we moeten onze database cluster eerst gaan aanmaken in de GUI van mondodb atlas. als we dit gedaan hebben krijgen we een connection string die er als volgt ongeveer uit ziet
### mongodb+srv://"gebruikersnaam":"wachtwoord"@"cluster-URL"/"databasenaam"

deze zetten we dan in MongoClient()
je hebt ook de optie om de link te testen. hier kan je dus gaan zien of je connectie met de database werkt dit doen we door het volgende te doen.
![img_2.png](pictures/img_2.png)
als we op "view full code sample" klikken krijgen we een code te zien deze copy paste je gewoon in je main.py en run de code dit gaat je database pingen en als het werkt ga je in de terminal tezien krijgen "pinged your deployment. enz."
als dit werkt weet je dat de connectie met de database werkt en kan je beginnen met de api en de andere dingen te maken

# screenshots postman and api docs
## api docs
![img_3.png](pictures/img_3.png)
![img_4.png](pictures/img_4.png)
![img_5.png](pictures/img_5.png)
![img_6.png](pictures/img_6.png)
![img_7.png](pictures/img_7.png)
![img_8.png](pictures/img_8.png)
![img_9.png](pictures/img_9.png)
![img_10.png](pictures/img_10.png)
![img_11.png](pictures/img_11.png)
![img_12.png](pictures/img_12.png)
![img_13.png](pictures/img_13.png)
![img_14.png](pictures/img_14.png)
de screenshots hier boven tonen aan dat de endpoints die ik heb werken. nu kunnen we ook naar het dashboard gaan om naar de monitoring te kijken en daar gaan we zien dat er verschillende wirte's zijn.
![img_15.png](pictures/img_15.png)