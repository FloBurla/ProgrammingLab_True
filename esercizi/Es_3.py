class CSVfile():
    def __init__(self,name):
        self.name=name

    def get_data(self):
        data=[]
        file=open(self.name,'r')
        for line in file:
            item=line.split(',')
            data.append(item)
        file.close()
        return(data)
    
file=CSVfile('shampoo_sales.csv')
datifile=[]
datifile=file.get_data()
print(datifile)
