class CSVFile():
    def __init__(self,name):
        self.name=name

    def get_data(self):
        data=[]
        try: 
            file=open(self.name,'r')
        except:
            print("Devi aver fatto un Errore nell'inserire il nome del file, perchè non esiste")

        for line in file:
            item=line.split(',')
            if item[0]!='Date':
                item[1]=float(item[1])
            data.append(item)
        file.close()
        return(data)
    
file=CSVFile('shampoo_salez.csv')
datifile=[]
datifile=file.get_data()
print(datifile)