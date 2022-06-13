total_1 = 0
total_2 = 0
count = 0

name_1, name_2 = input("Enter Name 1: ").lower().replace(" ", ""), input("Enter Name 2: ").lower().replace(" ", "")

for letter in name_1:
    if letter in name_2:
        count += 1
        total_1 += 1

for letter in name_2:
    if letter in name_1:
        count += 1
        total_2 += 1
print(count)

number = count % 6
relationship = ""

if number == 1:
    relationship = "FRIENDS"
elif number == 2:
    relationship = "LOVERS"
elif number == 3:
    relationship = "ACQUAINTANCES"
elif number == 4:
    relationship = "MARRIAGES"
elif number == 5:
    relationship = "ENEMY"
elif number == 0:
    relationship = "SIBLINGS"

print(f"Result for {name_1} ==> {total_1}")
print(f"Result for {name_2} ==> {total_2}")
print(f"FINAL RESULT {count} ==> {relationship}")
