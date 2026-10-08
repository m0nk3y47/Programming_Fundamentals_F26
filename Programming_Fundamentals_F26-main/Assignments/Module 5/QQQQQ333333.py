def check_number(number):
  if number % 2 == 0:
    print(f"{number} is an even number.")
  else:
    print(f"{number} is an odd number.")
num = int(input("Pick a number: "))

check_number(num)
