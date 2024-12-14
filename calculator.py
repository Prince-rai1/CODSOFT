print("Enter two numbers : ")
num1 = int(input("Number1: "))
num2 = int(input("Number2: "))

txt = '''
Choose an arthimetic operation: 
Addition (+)
Subtraction (-)
Multipliction (*)
Division (/)
  '''

print(txt)

operation = input("Operation: ")

try:
   match(operation):
         case ('+'):
             result = num1+num2

         case ('-'):
             result = num1-num2

         case ('*'):
             result = num1*num2
    
         case ('/'):
            if(num2==0):
              raise ZeroDivisionError("Division by zero")

            result = num1/num2
    
         case _:
             print("Invalid Airthematic operation")
             result = None

   if(result!=None): 
     print(f"The Result is: {result}")

except ZeroDivisionError as zd:
    print(zd)
