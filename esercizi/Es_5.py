class NumericalCSVFile():
    def __init__(self,name):
        self.name=name
        if(type(name)!=str):
            raise Exception('Il nome del tuo file non è una stringa')

    def get_data(self):
        data=[]
        try: 
            file=open(self.name,'r')
        except:
            print("Devi aver fatto un Errore nell'inserire il nome del file, perchè non esiste")

        for line in file:
            item=line.split(',')
            if item[0]!='Date':
                try:
                    item[1]=float(item)
                except:
                    print('Errore nella conversione a float, forse hai delle stringhe di lettere')
                    item[1]=float(item[1])
            data.append(item)
        file.close()
        return(data)
    
file=NumericalCSVFile('shampoo_sales.csv')
datifile=[]
datifile=file.get_data()
print(datifile)