print('Welcome to the tip and bill calculator!')

bill = float(input('What was the total bill? '))

tip = int(input('What percentage tip would you like to give; 10, 12 or 15%: '))

num_people = int(input('How many people should split the bill? '))

total_tip = (tip / 100) * bill

total_bill = bill + total_tip

each = round(total_bill / num_people, 2)

print(f'Each person should pay: ${each}')

