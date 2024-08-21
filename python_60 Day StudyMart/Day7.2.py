#from IPython.display import Screenshots
#Screenshots('electricity.png')

amount=0
net_units = float(input('Enter your unit='))
if net_units <=100:
    amount = 0
    print('amount is: ',amount)
elif net_units >100 and net_units <=200:
   amount = (net_units -100)+5
   

elif net_units >200:
    amount = ((net_units -200)+10)+500
print('amount is=',amount)