
#frågar efter antan personer
antal=int(input("För hur många personer vill du ha recept? skriv med siffra"))
antal=antal
#receptet delas med 4 för att kunna få för en person, för enkelhet skull.
def Recept(antal):
    agg=0.75
    socker= 0.75
    vanlijsocker=0.5
    bakpulver=0.5
    vetemjol= 0.75
    smor= 18.75
    vatten=0.25
    if antal >=1:

        print("ägg: ",(int(antal*agg)),"st")
        print ("socker:", (antal*socker),"dl")
        print ("vaniljsocker", (antal*vanlijsocker),"tsk")
        print("bakpulver", (antal*bakpulver), "tsk")
        print("vetemjöl", (antal*vetemjol), "dl")
        print("smör", (antal*smor), "g",)
        print("vatten", (antal*vatten), "dl")


#defination för tiden som tar att blanda
def Tidblanda(antal):

    #tid som tar att blanda
    global tid_blandar
    tid_blanda=10

    #satser
    tid_blandar=tid_blanda+antal
    print("för", antal, " personer tidblanda är:",tid_blandar)
    print(("     ")*50)

#defination för graddan.
def Tidgradda(antal):
    #tid att tar för gradden
    global tid_graddas
    tid_gradda=30
    tid_graddas=tid_gradda+(antal*3)
    print("för", antal, " personer tidgradde är",tid_graddas)
    print(("     ")*50)


#den totala tiden
def sockerkaka(antal):
    global total_tid

    total_tid=tid_graddas+tid_blandar
    print("Den totala tiden som tar är:",total_tid)
    print(("     ")*50)

Recept(antal)
Tidblanda(antal)
Tidgradda(antal)
sockerkaka(antal)

print(("===")*80)
print("för fyra personer behöver du den recepten")
Recept(4)
Tidblanda(4)
Tidgradda(4)
sockerkaka(4)

print(("===")*80)
print("för 7 personer behöver du den recepten")

Recept(7)
Tidblanda(7)
Tidgradda(7)
sockerkaka(7)









