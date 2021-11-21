import calendar
yy = 2021
mm = 11
print(calendar.month(yy, mm))

my_dict = {'name': 'Agung', 'age': 20}
print(my_dict['name'])

# Program make a simple calculator that can add, subtract, multiply and divide using functions
# This function adds two numbers
def add(x, y):
   return x + y
# This function subtracts two numbers
def subtract(x, y):
   return x - y
# This function multiplies two numbers
def multiply(x, y):
   return x * y
# This function divides two numbers
def divide(x, y):
   return x / y
print("Pilih Operasi.")
print("1.Penjumlahan")
print("2.Pengurangan")
print("3.Perkalian")
print("4.Pembagian")
# Take input from the user
choice = input("masukan pilihan mu(1/2/3/4):")
num1 = int(input("masukan angka pertama: "))
num2 = int(input("masukan angka kedua: "))
if choice == '1':
   print(num1,"+",num2,"=", add(num1,num2))
elif choice == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))
elif choice == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))
elif choice == '4':
   print(num1,"/",num2,"=", divide(num1,num2))
else:
   print("Invalid input")

