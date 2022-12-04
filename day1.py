with open("day1input.txt","r") as f:
   lines = f.readlines()

lines = [line.replace("\n","") for line in lines]

a = 0
list_of_calories = []
for line in lines:
    if line != "": 
        a = a + int(line)
    else:
        list_of_calories.append(a)
        a = 0
        # if a > a_max:
        #     a_max = a
        #     a = 0
        # else:
        #     a = 0

list_of_calories = sorted(list_of_calories, reverse=True)

answer1 = sum(list_of_calories[:3])
answer2 = list_of_calories[0]+list_of_calories[1]+list_of_calories[2]

print(answer2)