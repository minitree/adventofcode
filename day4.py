import input_reader

lines = input_reader.read("day4input.txt")

answer = 0

for line in lines:
   line_list_1 = line.split(",")
   line_a = line_list_1[0].split("-")
   line_b = line_list_1[1].split("-")
   set_a = set([*range(int(line_a[0]),int(line_a[1])+1,1)])
   set_b = set([*range(int(line_b[0]),int(line_b[1])+1,1)])
   
   intersection = set_a.intersection(set_b)

   #part 1
   #if intersection == set_b or intersection == set_a:
   #   answer += 1
   #part 2
   if len(intersection) != 0:
      answer += 1

print(answer)