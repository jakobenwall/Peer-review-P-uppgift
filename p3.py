import random
#P-uppgift av Jakob Enwall


class Grundämne: #Tecknar en klass som kan konstruera objekt med dessa fyra attribut
    def __init__(self, atom_nummer, beteckning, namn, atom_vikt):
        self.atom_nummer = atom_nummer
        self.beteckning = beteckning
        self.namn = namn
        self.vikt = atom_vikt

    def __lt__(self, other):  #Definierar hur objekten ska sorteras
        return self.atom_nummer < other.atom_nummer


def tabellvärde_kopplaren(textfilen): #läser in data från textfilen och kopplar datat till respektive attribut för varje objekt
    grundämnes_lista = [] #Skapar periodiska systemet där varje element i listan är ett Grundämne:s-objekt som innehåller attributen från textfilen
    with open(textfilen, 'r', encoding='utf-8') as tabellvärden:
        for rad in tabellvärden: #itererar över varje rad dvs grundämne i textfilen
            värden = rad.split(" ") #splittar varje rad till ord 
            beteckning = värden[0] 
            atom_nummer = int(värden[1])
            namn = värden[2]
            atom_vikt = float(värden[3])
            grundämnes_lista.append(Grundämne(atom_nummer, beteckning, namn, atom_vikt)) #lägger varje respektive objekt(grundämne) i listan(periodiska systemet)
    return grundämnes_lista


def se_alla_grundämnen(grundämnes_lista): #presentera alla grundämnen
    print("\nLista på varje grundämne:")
    grundämnes_lista.sort() #använder less than funktionen i klassen ovan för att sortera listan
    for grundämne in grundämnes_lista:
        print(f"#: {grundämne.atom_nummer} {grundämne.beteckning} {grundämne.namn}, {grundämne.vikt}")


def quizza_atomnummer(grundämnes_lista): 
    print("\nDu kommer nu bli testad på Atomnummer! svara med siffror! :)") #uppmanar att använda siffror
    antal_försök = 3
    rätt_svar = 0
    fel_svar = 0

    while True: #Skapar loopen där varje varv ger det nya efterfrågade grundämnet
        grundämne = random.choice(grundämnes_lista) #bestämmer den nuvarande efterfrågade grundämnet
        print(f"Vilket atomnummer har grundämnet {grundämne.namn}?")

        for försök in range(antal_försök): #skapar loopen som ger användaren 3 försök att svara rätt
            svar = input(f"Försök {försök + 1} av {antal_försök}: ")
            if int(svar) == grundämne.atom_nummer: #kollar om det är rätt
                print("Rätt svar!")
                rätt_svar += 1
                break
            else:
                print(f"Fel svar. Du har {antal_försök - försök - 1} försök kvar.")

        else:
            print(f"Tyvärr, rätt svar var {grundämne.atom_nummer}.") #om användaren inte svarar rätt
            fel_svar += 1

        print(f"Hittills har du {rätt_svar} rätt och {fel_svar} fel.")
        if input("Vill du fortsätta quizza? (ja/nej): ").lower() != "ja": 
            break


def quizza_atombeteckning(grundämnes_lista): 
    print("\nDu kommer nu bli testad på Atombeteckningar! svara med bokstäver!") #uppmanar att svara med bokstäver
    antal_försök = 3
    rätt_svar = 0
    fel_svar = 0

    while True: #skapar objekt loopen
        grundämne = random.choice(grundämnes_lista)
        print(f"Vilken atombeteckning har grundämnet {grundämne.namn}?")

        for försök in range(antal_försök): #skapar försök loopen
            svar = input(f"Försök {försök + 1} av {antal_försök}: ").capitalize() #gör så att AU och au är giltiga svar till Au etc. 
            if svar == grundämne.beteckning: #kollar om svaret är rätt
                print("Rätt svar!")
                rätt_svar += 1
                break
            else:
                print(f"Fel svar. Du har {antal_försök - försök - 1} försök kvar.")

        else:
            print(f"Tyvärr, rätt svar var {grundämne.beteckning}.") #om användaren inte svarar rätt på 3 försök
            fel_svar += 1

        print(f"Hittills har du {rätt_svar} rätt och {fel_svar} fel.")
        if input("Vill du fortsätta quizza? (ja/nej): ").lower() != "ja":
            break


def quizza_atomnamn(grundämnes_lista):
    print("\nDu kommer nu bli testad på atom namn! Svara med bokstäver!") #ledning
    antal_försök = 3
    rätt_svar = 0
    fel_svar = 0

    while True:
        grundämne = random.choice(grundämnes_lista)
        print(f"Vad heter grundämnet med atombeteckningen {grundämne.beteckning}?")

        for försök in range(antal_försök):
            svar = input(f"Försök {försök + 1} av {antal_försök}: ").strip().capitalize()
            if svar == grundämne.namn:
                print("Rätt svar!")
                rätt_svar += 1
                break
            else:
                print(f"Fel svar. Du har {antal_försök - försök - 1} försök kvar.")

        else:
            print(f"Tyvärr, rätt svar var {grundämne.namn}.")
            fel_svar += 1

        print(f"Hittills har du {rätt_svar} rätt och {fel_svar} fel.")
        if input("Vill du fortsätta quizza? (ja/nej): ").strip().lower() != "ja":
            break



def huvudmeny(grundämnes_lista): #själva menyn och också bakgrunden för hela programmet liksom the backbone
    while True: #Skapar loopen som håller programmet igång tills användaren stänger av det
        print("\n------ MENY ------")
        print("1. Visa alla grundämnen")
        print("2. Träna på atomnummer")
        print("3. Träna på atombeteckningar")
        print("4. Träna på atomnamn")
        print("5. sluta")
        print("------------------")

        val = input("Vad vill du göra? (1-5): ")

        if val == "1":
            se_alla_grundämnen(grundämnes_lista)
        elif val == "2":
            quizza_atomnummer(grundämnes_lista)
        elif val == "3":
            quizza_atombeteckning(grundämnes_lista)
        elif val == "4":
            quizza_atomnamn(grundämnes_lista)
        elif val == "5":
            print("Avslutar programmet. Tack för att du använde det!")
            break
        else:
            print("Ogiltigt val, försök igen!")


if __name__ == "__main__": #gör så att tabellvärdena kan ändras med att byta textfilen
    filnamn = "avikt.txt"
    grundämnes_lista = tabellvärde_kopplaren(filnamn)
    huvudmeny(grundämnes_lista)
