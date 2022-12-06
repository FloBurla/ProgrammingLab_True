def sum_csv(file_name):
    values=[]
    sum=0
    myfile=open(file_name,'r')
    for line in myfile:
        elements=line.split(',')
        if elements[0] != 'Date':

            value=float(elements[1])

            sum=sum+value
            values.append(value)
    myfile.close()
    return sum
    
sum=sum_csv('shampoo_sales.csv')
print(sum)

    
    