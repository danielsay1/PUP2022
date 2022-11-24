import pandas as pd 
import yfinance as yf 

class Aktie: #klassen aktie med parametrarna self och aktie_namn i konstruktorn 
    def __init__(self, aktie_namn):  #aktie_namn används flera gånger för att få tekniska och fundementala analysen för just det namnet
       self.aktie_namn = aktie_namn

    
    
    def teknisk_analys(self, df, omx_df):    #den ska returnera antalet aktier och vi ska använda det för rang. beta och de aktier man kan göra T.A på
                                            #tar dataframes,df, som inparameter och läser av mha pandas. 
        
        max_pris= df['Adj Close'][self.aktie_namn].max()
        min_pris = df['Adj Close'][self.aktie_namn].min()
        avkastning_aktie = df["Adj Close"][self.aktie_namn].iloc[-1]/ df["Adj Close"][self.aktie_namn].iloc[0]
        kursutveckling = avkastning_aktie * 100 - 100
   
        avkastning_marknad = (omx_df["Adj Close"].iloc[-1])/(omx_df["Adj Close"].iloc[0])               
        beta_värde = avkastning_aktie/avkastning_marknad
       
        beta_värde= round(beta_värde, 3)
        min_pris = round(min_pris, 2)
        max_pris = round(max_pris,2)
        kursutveckling = round(kursutveckling, 2)

        return  kursutveckling, beta_värde, min_pris, max_pris        #
        
    def fundamental_analys(self): #läser från fundamenta.txt och returnerar nyckeltalen för varje aktie i listan 
                                 #med hjälp av yfinance library behöver vi endast aktiens namn för att hämta nyckeltalen. 
 

        PE = yf.Ticker(self.aktie_namn).info["forwardPE"]
        PS = yf.Ticker(self.aktie_namn).info["priceToSalesTrailing12Months"]
        soliditet = yf.Ticker(self.aktie_namn).info["debtToEquity"]
        nyckeltal_aktie = [soliditet, PE, PS]

        return nyckeltal_aktie
