
from tkinter import *     
from analys2 import Aktie 
import yfinance as yf 

root = Tk()       # skapar vårt fönster 
root.title("—————————Meny———————————")

svarsruta = Label(root, width=35, borderwidth=5, text= "", font=('Helvetica', 30)) 
svarsruta.grid(row=0, column=0, columnspan=1, padx=10, pady=10)
 
def läs_data(aktier): #läser från källan och returnerar informationen i den som en dataframe, kolumn  
    
    df = yf.download(aktier, start = "2021-11-05", end = "2021-12-07")
    
    return df

def fundamental_analys_fönster(aktier_namn, aktier): # Låter aktien välja vilken aktie hen vill göra fundamental analys på och gör sedan en fundamental analys för den aktien
                                            #Indata är aktiernas namn i olika format vilket används för att ta fram fundementaldata för det specifika namnet.
    
    top = Toplevel()    
    top.title("Fundamental Analys") 
    fund = Label(top, width=35, borderwidth=5, text= "", font=('Helvetica', 20)) 
    fund.grid(row=0, column=0,columnspan=1, padx=10, pady=10)

    def klickfunktion(j):           # Funktion inuti funktion, vi vill returnera andra funktionen 
        def fundamental_analys():
                nyckeltal = Aktie(aktier[j]).fundamental_analys()
                meddelande = "—————Fundamental analys för " + str(aktier_namn[j])  + "—————" + "\n" + "Företagets soliditet är: " + str(nyckeltal[0]) + "%" + "\n" + "Företagets p/e-tal är: " + str(nyckeltal[1]) + "\n" + "Företagets p/s-tal är: " + str(nyckeltal[2]) 
                fund.config(text = meddelande)
        return fundamental_analys
    
    instruktioner_tek = Label(top, text = "En fundamental analys kan utföras för följande aktier. Klicka för att välja.")
    instruktioner_tek.grid(row=2, column = 0)


    # Skapar våra knappar 
    n = range(len(aktier_namn)) 
    for j in n:
        knapp = Button(top, text = aktier_namn[j], command = klickfunktion(j)) 
        knapp.grid(row=j+3, column=0)


def teknisk_analys_fönster(aktier_namn, aktier, df, omx_df):  # Låter användaren välja vilken aktie hen vill göra teknisk analys på och gör sedan en teknisk analys på den aktien
                                                              # Indata är aktiernas namn i olika format och två dataframes för aktierna respektive OMX värdena.    
    top = Toplevel()     # skapar nya fönstret för Teknisk analys 
    top.title("Teknisk Analys")  
    tek = Label(top, width=35, borderwidth=5, text= "", font=('Helvetica', 20)) 
    tek.grid(row=0, column=0,columnspan=2, padx=10, pady=10)

    def klickfunktion(j):           # Funktion inuti funktion, vi vill returnera andra funktionen 
        def teknisk_analys():
            värden = Aktie(aktier[j]).teknisk_analys(df, omx_df)  # Aktier och aktier_namn har korresponderande index
            meddelande = "—————Teknisk analys för " + str(aktier_namn[j]) + "—————" + "\n" + "Kursutveckling (30 senaste dagarna): " + str(värden[0]) + "%" +"\n" + "Betavärde: " + str(värden[1]) +"\n" + "Lägsta kurs (30 senaste dagarna): " + str(värden[2]) +"\n" + "Högsta kurs (30 senaste dagarna): " + str(värden[3]) 
            tek.config(text = meddelande)
    
        return teknisk_analys

    instruktioner_tek = Label(top, text = "En teknisk analys kan utföras för följande aktier. Klicka för att välja.")
    instruktioner_tek.grid(row=2, column = 0)


    # Skapar våra knappar 
    n = range(len(aktier_namn)) 
    for j in n:
        knapp = Button(top, text = aktier_namn[j], command = klickfunktion(j)) 
        knapp.grid(row=j+3, column=0)
    



def rangordna_beta_värde(aktier_namn, aktier, df, omx_df): # Tar betavärdet för alla aktier i listan och rangordnar dem 
    beta_värde = [] #Kommer ha formatet ["Aktienamn Betavärde"]
    for index in aktier: 
       
        beta_värde.append((aktier_namn[aktier.index(index )] + " " + str(Aktie(index).teknisk_analys(df, omx_df)[1])))
    beta_värde.sort(key= lambda företag: float(företag.split()[-1]), reverse=True) #källa https://www.pythontutorial.net/python-basics/python-sort-list/ anonymfunktion som kallas .
    a='\n'.join(beta_värde)
    svarsruta.config(text=a)
    button_5 = Button(root, text = "Radera", command = lambda: svarsruta.config(text = ""))
    button_5.grid(row=5,column = 2)



# Vår data som ska analyseras 
omx = "^OMX"
omx_df = läs_data(omx)
aktier= ["ERIC-B.ST", "AZN.ST","ELUX-B.ST","KINV-B.ST"] 
df = läs_data(aktier)
aktier_namn = ['Ericsson', 'AstraZeneca', 'Elektrolux', 'Kinnevik']

# Våra knappar 
instruktioner = Label(root, text = "Klicka på ett alternativ nedan!")
knapp_1 = Button(root, text="Fundamental analys (Vid långsiktigt aktieinnehav)", padx=35, pady=20, command= lambda: fundamental_analys_fönster(aktier_namn, aktier))
knapp_2 = Button(root, text="Teknisk analys (Vid kort aktieinnehav)", padx=70, pady=20, command= lambda: teknisk_analys_fönster(aktier_namn, aktier, df, omx_df)) 
knapp_3 = Button(root, text="Rangordning av aktier med avseende på dess betavärde", padx=14, pady=20, command= lambda: rangordna_beta_värde(aktier_namn, aktier, df, omx_df))
knapp_4 = Button(root, text="Avsluta", padx=163, pady=20, command=root.destroy)


# Gör så att knapparna hamnar på skärmen 
instruktioner.grid(row=2, column = 0)
knapp_1.grid(row=3, column=0)
knapp_2.grid(row=4, column=0)
knapp_3.grid(row=5, column=0)
knapp_4.grid(row=6, column=0)


root.mainloop()

#Daniel Say 2022-06-10
#20021229-3518