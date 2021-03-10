class TelefonBok:
    #initializer  objekt, den kallas oxå  en konstruktör i objektorienterad terminologi.
    def __init__(self):

        #lagras allt i detta
        self.Dictionary= {}

        #kommandon för olika operationer som är lagrat i dictionary
        Kommandon_till_Dic = {"add": self.add,
                              "lookup": self.lookup,
                              "alias": self.alias,
                              "save": self.save,
                              "load": self.load,
                              "remove": self.remove,
                              "quit": self.quit,
                              "change": self.change}


        #så länge det är sant
        while True:
            #första frågan
            question_1 = input("telefonbok: ")

            #splitrar varje meningen du skrivit, annars får man som en string
            split_question_1 = question_1.split()


            if split_question_1:
                try:
                #kollar om den första inputen matchar den Kommandon_till_Dic i dict då körs kollar vad detta är, sen kollar resten.
                    #Kommandon_till_Dic[split_question_1[0]](*split_question_1[1:])
                    if split_question_1[0]=='add':
                        self.add(*split_question_1[1:])

                    if split_question_1[0]=='lookup':
                        self.lookup(*split_question_1[1:])

                    if split_question_1[0]=='alias':
                        self.alias(*split_question_1[1:])

                    if split_question_1[0]=='save':
                        self.save(*split_question_1[1:])

                    if split_question_1[0]=='laod':
                        self.load(*split_question_1[1:])

                    if split_question_1[0]=='change':
                        self.change(*split_question_1[1:])

                    if split_question_1[0]=='remove':
                        self.remove(*split_question_1[1:])
                    if split_question_1[0]=='quit':
                        self.quit()


                # if questionsplit[0] == "add":
                #     self.add(questionsplit[1:])

                #detta körs för att hindra craschet.
                except TypeError:
                    print('fel antal argument')

                #om du inte hittar nånting från din dic..
                except KeyError:
                    print("Denna funktion finns inte")

                #om du inte har skrivit nåt
                except IndexError:
                    print("Du har inte skrivit nåt")
                #när en input eller output operation går fel
                except IOError:
                    print('fillen hittades inte')


    #kollar alltid om nummer hittades elle inte
    def find(self, namn):
        traff = 0 #start värde för traff
        nr = 0 #den har koll på antal numret

        for number, names in self.Dictionary.items(): #kollar i dectionary om det finns
            #kollar om namnet är med, om det är det så skickar värder vidare till nästa koden
            if namn in names:
                nr = number
                traff += 1
        #om den inte hittar
        if traff == 0:
            return 0
        #om den hittar en person, returnar den exakta numret
        elif traff == 1:
            return nr
        #om den hittar mer än en person
        elif traff>1:
            return -1

    #lägg till funktionen
    def add(self, namn, nummer):
    #kollar och numret finns inte med, isf lägger till den
        if nummer not in self.Dictionary:
            print("Namn:",namn,"\nNummer:",nummer,"\nSparat i telefonboken")
            self.Dictionary[nummer] = [namn]
        #annars skriver meddelandet
        else:
              print('Fler personer med samma nummer går ej')

    #kollar upp
    def lookup(self, namn ):
        traff=0
        #kollar och number och names finns in dic
        for number, names in self.Dictionary.items():
            #skriver ut alla med detta namn
            if namn in names:
                #för att ha koll på hur många hittats
                traff = 1
                print("Namn",namn,"\nNummer:",number)
                print("Done...")

            #om den inte hittar
        if traff !=1:
            print("Namnet finns inte")


    #ger ett smenkt namn till  personer
    def alias(self, namn, newname, mobile_number=None):

        if newname:
            #den kollar i find funktionen
            nr = self.find(namn)
            #om find en person
            if int(nr) >1: #om det är exakt en person
                self.Dictionary[nr].append(newname)
                print("Alias angivet...")

            #om den hittar inte allas
            if int(nr)==0:
                print('hittade inte')

            #isf om det finns fler persone med samma namn
            elif int(nr) ==-1 and mobile_number == None:
                print("Flera personer har detta namn, ge nummer")

            #om det finns fler personer med samma namn och angivna alias
            elif int(nr) == -1 and mobile_number != None:
                #tar mobil_nummer som key för att nr är -1 när find funktionen hittar fler personer med detta nman
                self.Dictionary[mobile_number].append(newname)
                print("Klart, alias lades till")




    #sparar innehållet till en fil.txt
    def save(self, filename):
        f = open(filename, "w")
        #kollar number and names i dci
        for number, names in self.Dictionary.items():
            #Sen sätter nummer och alla names till nummer i en i string och alla ord separerade med detta tecken ;
            line = number + ";" + ";".join(names)  +  ';' +"\n"
            #skriver den som vi hade skrivet som input
            f.write(line)
        print("Sparar...")


    #läser innehåller från filen och även byter ut
    def load(self, filename):

        f = open(filename, "r")
        #tomar dic
        self.Dictionary.clear()
        #loppar varje rad separat
        for line in f:
            #splitrar vid detta tecken
            line = line.split(";")
            del line[-1]
            #nummer blir det första inex av line
            nummer = line[0]
            #name blir från 1 och så vidare
            namn = line[1:]
            #ger värde från filen till de två variablar.
            self.Dictionary[nummer] = namn


        print('Filen är loadat!!')




    #byter nummert
    #oldnr=none är standardvärde
    def change(self, namn, newnumber, oldnr = None):
        if namn:
            #kollar i find funktionen
            nr = self.find(namn)
            #om det numret finns inte i dictionary
            if newnumber not in self.Dictionary:
                if int(nr) > 1: #om nr är större en 1.
                    self.Dictionary[newnumber] = self.Dictionary[nr]
                    del self.Dictionary[nr]
                    print("nummret ändrats...")

            #isf om den nya numret är upptagen med någon annan
            elif newnumber in self.Dictionary:
                 print('detta nummer finns med, välj ett annat nummer')
                #om det inte hittar
                 if int(nr) == 0:
                    print("Hittar inga med det nummer")


                #om det är fler personer med detta namn och inte pecificerat med numret
                 elif int(nr) ==-1 and oldnr == None:
                    print("Flera personer har detta namn, ge exakta numret")

                #specifikerat personen med nummer

                 elif int(nr) == -1 and oldnr != None:
                    self.Dictionary[newnumber] = self.Dictionary[oldnr]
                    del self.Dictionary[oldnr]
                    print("Klart, numret på denna person ändrades")






    #tar bort inputen
    def remove(self, namn, nr=None):
        #kollar i find funktionen
        nummer = self.find(namn)
        # om det finns bara en person
        if int(nummer) >1:
            del self.Dictionary[nummer]
            print("uppdraget är klart!!")
        #om det finns inga med detta namn
        elif int(nummer) == 0:
            print("Namnet finns inte")

            #om det är många med detta namn och numret är inte angivet
        elif int(nummer) ==-1 and nr == None:
              print("Flera personer har detta namn, ge nummer")

         #om det är många med detta namn och numret är angivet
        elif int(nummer) == -1 and nr != None:
            del self.Dictionary[nr]
            print('Klart, namn och telefon nummer på denna person är borttagen')

    #quit funktionen
    def quit(self):
        print("Du aavslutade precis programmet!!!")
        quit()




t = TelefonBok()
