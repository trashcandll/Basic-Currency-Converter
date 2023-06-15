from forex_python.converter import CurrencyRates

c = CurrencyRates()
input_amount = float(input('Input your amount: '))
from_currency = input('Enter the currency you want to convert from: ').upper()
to_currency = input('Enter the currency you want to convert to: ').upper()

result = c.convert(from_currency,to_currency,input_amount)
print(f'From {from_currency} to {to_currency} = {result}')
