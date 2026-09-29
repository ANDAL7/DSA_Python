sales=[100,200,150,300,250]
cum=[sales[0]]
while len(cum)<len(sales):
    cum.append(cum[-1]+sales[len(cum)])
print(cum)