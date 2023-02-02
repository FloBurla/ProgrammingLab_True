import os                                            #libreria utile per controllare l'esistenza del file

class ExamException(Exception):                      #eccezione data dalla consegna
    pass
    
def check_existance(file):                           #funzione per controllare se il percorso del file esiste
    if os.path.exists(file):
        return True 
    else:
        return False 

def TryConversionInt(x):                            #funzione per controllare che il soggetto sia convertibile a intero
    try:
        int(float(x))                               #uso float(int()) per convertire a intero anche eventuali float senza approssimare direttamente 
    except:
        return False
    return True

def TryConversionFloat(y):                           #funzione per controllare che il soggetto sia convertibile a floating point
    try:
        float(y)
    except:
        return False
    return True


def compute_daily_max_difference(time_series):       #funzione principale per ottenere l'escursione termica
    thermal_excursion=[]                             #lista vuota che conterrà il risultato
    list = []                                        #lista ausiliaria
    i=0                                              

    while i < len(time_series):
        daily_temp=[]                                #lista che si svuota ogni ciclo per indicare il nuovo giorno
        
        inf = time_series[i][0] - (time_series[i][0] % 86400)                #estremo inferiore sopra il quale è lo stesso giorno
        sup = time_series[i][0] - (time_series[i][0] % 86400) + (86400)       #estremo superiore sotto il quale è lo stesso giorno
        
        while i<len(time_series) and inf <= time_series[i][0] < sup:          #mentre la temperatura è compresa negli estremi del giorno
            daily_temp.append(time_series[i][1])                              #aggiungo le temperature legate allo steso giorno
            i += 1                                                            #i aumenta per poi guardare il giorno successivo una volta uscito

        list.append(daily_temp)                      #aggiungo alla lista ausiliaria la lista coi valori della giornata  
        
    day=0                                            #fuori dal precedente while considero una variabile giorno
    
    while day < len(list):                           #finchè il giorno è compreso in quelli individuati
        
        if(len(list[day])>1):                                                #se ho più di una temperatura per giorno
            thermal_excursion.append(max(list[day])-min(list[day]))
        else:
            thermal_excursion.append(None)
            
        day += 1
        
    return (thermal_excursion)


class CSVTimeSeriesFile():       
    
    def __init__(self,name=None):    
        self.name=name
        
    def get_data(self):
        data=[]

        if(self.name==None):                                                    #controllo che sia stato dato un nome
            raise ExamException('Non hai inserito il nome del file')
        
        if type(self.name)!=str:                                                #controllo che il nome sia una stringa
            raise ExamException('Il nome del file non è una stringa')

        file=open(self.name,'r')
        
        if not check_existance(self.name):                                      #se la funzione per l'esistenza è falsa
            raise ExamException('File non trovato') 


        prev_item=None                                             #controllo l'oggetto precedente (che all'inizio è nullo)
        
        for line in file:
            item = line.split(',')
            if (TryConversionInt(item[0]) and TryConversionFloat(item[1])):        #Questo per non considerare possibili stringhe o valori non convertibili
                item[0]=int(item[0])
                item[1]=float(item[1])

                if(prev_item!=None and item<prev_item):                        #dopo il primo caso vedo se sono ordinati
                    raise ExamException('La lista non è ordinata')
                if(prev_item!=None and item[0]==prev_item[0]):                 #dopo il primo caso vedo se ci sono doppioni
                    raise ExamException('Nella lista appaiono duplicati')

                prev_item=item
                
                data.append(item)
                
            else:                          #se ho valori non convertibili, ignoro la riga (es. la prima del file data.csv)
                continue
                
        file.close()

        return (data)

time_series_file=CSVTimeSeriesFile('data.csv')
time_series=time_series_file.get_data()
thermal_excursion=compute_daily_max_difference(time_series)
print(thermal_excursion)