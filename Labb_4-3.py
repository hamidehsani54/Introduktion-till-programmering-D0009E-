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


       
        while True:
           
            question_1 = input("telefonbok: ")

           
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
                
                except TypeError:
                    print('fel antal argument')

             
                except KeyError:
                    print("Denna funktion finns inte")

            
                except IndexError:
                    print("Du har inte skrivit nåt")
            
                except IOError:
                    print('fillen hittades inte')


  
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


    def add(self, namn, nummer):
    #kollar och numret finns inte med, isf lägger till den
        if nummer not in self.Dictionary:
            print("Namn:",namn,"\nNummer:",nummer,"\nSparat i telefonboken")
            self.Dictionary[nummer] = [namn]
    
        else:
              print('Fler personer med samma nummer går ej')

    def lookup(self, namn ):
        traff=0
        #kollar och number och names finns in dic
        for number, names in self.Dictionary.items():
           
            if namn in names:
                #för att ha koll på hur många hittats
                traff = 1
                print("Namn",namn,"\nNummer:",number)
                print("Done...")

        if traff !=1:
            print("Namnet finns inte")


    def alias(self, namn, newname, mobile_number=None):

        if newname:
           
            nr = self.find(namn)
   
            if int(nr) >1: #om det är exakt en person
                self.Dictionary[nr].append(newname)
                print("Alias angivet...")

            #om den hittar inte allas
            if int(nr)==0:
                print('hittade inte')

            #isf om det finns fler persone med samma namn
            elif int(nr) ==-1 and mobile_number == None:
                print("Flera personer har detta namn, ge nummer")

         
            elif int(nr) == -1 and mobile_number != None:
             
                self.Dictionary[mobile_number].append(newname)
                print("Klart, alias lades till")




    def save(self, filename):
        f = open(filename, "w")
        #kollar number and names i dci
        for number, names in self.Dictionary.items():
         
            line = number + ";" + ";".join(names)  +  ';' +"\n"
         
            f.write(line)
        print("Sparar...")


    def load(self, filename):

        f = open(filename, "r")
    
        self.Dictionary.clear()
  
        for line in f:
         
            line = line.split(";")
            del line[-1]
         
            nummer = line[0]
           
            namn = line[1:]
           
            self.Dictionary[nummer] = namn


        print('Filen är loadat!!')





 
    def change(self, namn, newnumber, oldnr = None):
        if namn:
         
            nr = self.find(namn)
         
            if newnumber not in self.Dictionary:
                if int(nr) > 1: #om nr är större en 1.
                    self.Dictionary[newnumber] = self.Dictionary[nr]
                    del self.Dictionary[nr]
                    print("nummret ändrats...")


            elif newnumber in self.Dictionary:
                 print('detta nummer finns med, välj ett annat nummer')
     
                 if int(nr) == 0:
                    print("Hittar inga med det nummer")



                 elif int(nr) ==-1 and oldnr == None:
                    print("Flera personer har detta namn, ge exakta numret")

                 elif int(nr) == -1 and oldnr != None:
                    self.Dictionary[newnumber] = self.Dictionary[oldnr]
                    del self.Dictionary[oldnr]
                    print("Klart, numret på denna person ändrades")





    def remove(self, namn, nr=None):
    
        nummer = self.find(namn)
 
        if int(nummer) >1:
            del self.Dictionary[nummer]
            print("uppdraget är klart!!")
  
        elif int(nummer) == 0:
            print("Namnet finns inte")

       
        elif int(nummer) ==-1 and nr == None:
              print("Flera personer har detta namn, ge nummer")

        elif int(nummer) == -1 and nr != None:
            del self.Dictionary[nr]
            print('Klart, namn och telefon nummer på denna person är borttagen')


    def quit(self):
        print("Du aavslutade precis programmet!!!")
        quit()




t = TelefonBok()
