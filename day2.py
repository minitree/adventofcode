rules_outcome = {"A X": "A Z",
        "A Y" : "A X",
        "A Z" : "A Y",
        "B X" : "B X",
        "B Y" : "B Y",
        "B Z" : "B Z",
        "C X" : "C Y",
        "C Y" : "C Z",
        "C Z" : "C X" 
        }

rules_score = {"A X": 4,
        "A Y" : 8,
        "A Z" : 3,
        "B X" : 1,
        "B Y" : 5,
        "B Z" : 9,
        "C X" : 7,
        "C Y" : 2,
        "C Z" : 6 
        }

with open("day2input.txt","r") as f:
   lines = f.readlines()
lines = [line.replace("\n","") for line in lines]

sum = 0
# for line in lines:
#     sum += rules_score[line]
for line in lines:
    sum += rules_score[rules_outcome[line]]

print(sum)