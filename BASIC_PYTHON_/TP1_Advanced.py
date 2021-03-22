#AVANCEE

#-------Pratique / Solution
##--- Récupérer un élément dans une liste sans générer d'erreur
#indication: créer une fonction qui nous permette de récupérer un élément dans une
#liste à partir de son indice, sans retourner d'erreur au cas où l'indice est
#en dehors des limites de la liste
## exemple:


def recuperer_item(liste, indice):
    if indice < 0 and abs(indice) <= len(liste):
        return liste[indice]
    elif indice > 0 and indice < len(liste):
        return liste[indice]
    elif indice == 0 and liste:
        return liste[0]

    return "Index {} hors de la liste".format(indice)

liste = [1,3,5,7,9, 11]
print(recuperer_item(liste, 0))    #--- correct
print(recuperer_item(liste, 5))    #--- la liste ne contient pas le 4eme element
print(recuperer_item(liste, -13))  #--- la liste ne contient pas 12 element si on la parcourt de la fin


# ------- Pratique ------
#Écrire un programme qui invite l'utilisateur à entrer une chaîne et compte le nombre d'occurrences
#de chaque lettre dans la chaîne, indépendamment de la casse

def counter_chars(mot):
    x=[];
    for i in range(len(mot)):
        if (not(mot[i] in x)):
            print('Character {} its {}'.format(mot[i], mot.count(mot[i])))

        x.append(mot[i]) #Pour eviter les letres repetitives

counter_chars('ecole')


#-------Pratique
#Écrire un programme qui invite l'utilisateur à entrer une chaîne , écrire une première fonction qui retourne sa longueur.
#Ecrire une seconde fonction qui retourne la longueur d'une chaîne après l'avoir transformée en liste.

def entrerChaine():
    chaine = str( input('Input data:  ') )
    print('Length: ', len(chaine))

def lengthLikeList():
    chaine = str( input('Input data:  ') )
    list1=[]
    list1[:0]=chaine
    print('Length: ', len(list1))

entrerChaine()
lengthLikeList()


#-------Pratique
#Écrire un programme qui invite l'utilisateur à entrer une phrase, puis fait des statistiques
#sur cette phrase ( donne le mot le plus long, le mot le plus court et nombre totale de mots
#dans la phrase

def ConvertToList(phrase):
    listMots = list(phrase.split(" "))
    return listMots


def counter_mots(phrase):
    listMots = list(phrase.split(" "))
    x=[]
    for i in range(len(listMots)):
        if (not(listMots[i] in x)):
            print('Mot {} its {} times'.format(listMots[i], listMots.count(listMots[i])))

        x.append(listMots[i]) #Pour eviter les letres repetitives
    print('Numero total de mots: ', len(listMots))

counter_mots('ecole rose de vents')

def mot_plus_long(phrase):
    listMots = list(phrase.split(" "))
    x=[]
    maxMotLen = len(listMots[0])
    for i in range(len(listMots)):

        if len( listMots[i]) > maxMotLen:
            maxMot = listMots[i]
            maxMotLen = len(listMots[i])

    print('Le mot plus long {} a {} characters.'.format(maxMot, maxMotLen))

mot_plus_long('Ecole rose de vents de Brossard')


#-------Pratique
#Écrire un programme  qui nettoit une chaîne de caractères (String) de tout type de séparateurs (espaces, tabulations,
#guillemets, ponctuations et apostrophes)

# initialising string
notAcceptedChars = '{},.:-_()[]$%*@#* '

# code to find characters in string
res1 = ""
def netoyer_mot(mot):
    x="";
    for i in range(len(mot)):
        if ((not(mot[i] in notAcceptedChars))):
            x=x+(mot[i])

    print('Mot Netoye: ', x)

netoyer_mot('Ricardo*@#$Vall&:ej()o')

#----- Pratique
#Pour acheter en ligne un billet de cinéma ( déterminer les objets à manipuler + les actions à faire)
#Objets à manipuler ( site web cinema, nom du film, date présentation, heure présentation, montant a payer)
#Actions à faire ( entrer le site web du cinéma, choisir nom film, entrer date et heure présentation, afficher montant a payer

        #Objets

        #InfoClients (idClient, name, email, phone)
        #InfoMovies (idMovie, name, Schedules)
        #Cinemas(idCinema, nameCinema, pageWebCinema, max_ocupation)
        #Ubications(idUbication, chaise_reference)
        #Schedules(idMovie, date, Ubication, init_time, final_time)
        #Billets (idBillet, InfoClient, InfoMovies, Schedules, montant)

        #Actions
        #Add/Find/Delete?Update films
        #Add/Find/Delete?Update Movies,
        #Add/Find/Delete?Update Cinemas
        #Add/Find/Delete?Update  Ubications, Schedules
        #Add/Find/Delete?Update  Billets

        #Regles de validations des schedules (cycle de vie de films, repetiability..etc
        #Validation de dates de achat a future


# --- Pratique
#Pour prendre le bus  (déterminer les objets à manipuler + les actions à faire)
#Objets à manipuler ( numéro bus , ticket but, date du jour, heure du jour, montant a payer)
#Actions à faire ( aller dans la station bus, chercher le numéro de bus à apprendre, acheter ticket bus,
#entrer date et heure, introduire montant à payer


        #Objets

        #InfoBus(idBus, model, marca, capacite_max, idPlate)
        #InfoClient(idUser, Name, mail, Tickets)
        #Schedule(idRoute, InfoBus, departure, arrival, departure_time, arrival_Time, montant, departure_door, arrival_door, duration)
        #Tickets(IdTicket, Schedule)

        #Actions

        #User buy tickets with Routes, chaque route peut avoir son montant en dependant de distance
        #The Route peut informer ou l'usager prend l'autobus, lequelle est l'id de Autobus, la duration de voyage et la port de destination.



# --- Pratique
# pour réserver  une chambre d’hôtel  sans carte de crédit ( déterminer les objets à manipuler + les actions à faire)
# Objets à manipuler ( nom de l’hôtel, date d’arrivée, date départ, nuitées, nombre de chambres, nombre d’adultes, nombre enfants , lit_bébé, montant à payer par nombre de chambres, montant total à payer, confirmation réservation
# Actions à faire ( introduire le nom de l’hôtel, introduire les dates d’arrivée et départ, introduire le nombre de chambres, introduire le nombre d’adultes, le nombre d’enfants

        # Objects

        #CHAMBRES(idChambre, NoLits, capMax, montant_nuit. PreferencesVIP)
        #CLIENTS(IdClient, name, email)
        #PREFERENCES_VIP(IdPreference, NamePreference, montantpreference)  ex: LitBebe, sauna, HomeTheater
        #RESERVATIONS_PREFERENCES_VIP(IdPreference, NamePreference, time_hrs, montant)  ex: LitBebe, sauna, HomeTheater
        #RESERVATIONS_ROOMS(Id Reservation, IdClient, Arrive Date, Departure Date, IdChambres, numero_nuits,
        #             List_preferences_VIP, NoAdults, NoNinos, isConfirmed, ListReservationsVIP)

        # Actions
        #User do reservations for any chambre used.
        #Any room reservation define relations between Client, Chambre et List de privileges
        #flag isConfirmed is used to validate is room was confirmed by client.
        #Each romm has privileges that could be used by client
        #Each reservation shows total day of ocupation and time of any privilige.
