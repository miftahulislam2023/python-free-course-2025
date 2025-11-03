#project create a calculator 
try:
  x = float(input('enter number:'))

  y = float(input('enter another digit:'))

  opperator = (input('enter an operator(+ - * / ):'))

  if opperator == '+':
        print(x + y)
        
  elif opperator == '-':
        print(x - y)
        
  elif opperator == '*':
        print(x * y)
        
  elif opperator == '/':
        print(x / y)	
        if (y == 0):
            print('divisor cannot be divine ')
        else:
                print('x / y')     
  else:
        print('error! please check the number or opperator ') 
except ValueError:
	  	print('sob thikh kore lekh')