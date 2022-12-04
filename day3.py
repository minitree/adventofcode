from input_reader import read

lines = read("day3input.txt")

    # if len(line) % 2 != 0:
    #     print("it's not even")

lowercase_list = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split(' ')
uppercase_list = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".split(' ')

# part 1
#print(lowercase_list.index('d'))
# sum_of_prios = 0
# all the lines have an even number of characters
# for line in lines:  
#     part_size = int(len(line)/2)
#     pairs = [line[:part_size],line[part_size:]]
#     intersect = list(set(pairs[0]).intersection(pairs[1]))[0]

#     if(intersect) in lowercase_list:
#         lowercase_prio = lowercase_list.index(intersect)
#         sum_of_prios += lowercase_prio+1
#     if(intersect) in uppercase_list:
#         uppercase_prio = uppercase_list.index(intersect)
#         sum_of_prios += uppercase_prio+27

#print(sum_of_prios)

# part 2
sum_of_prios = 0
grouper = 0
list_of_groups = []
for line in lines:
    if grouper == 3:
        list_of_groups = []
        grouper = 0

    list_of_groups.append(line)
    grouper += 1
    if len(list_of_groups) == 3:
        intersect2 = list(set(list_of_groups[0]) & set(list_of_groups[1]) & set(list_of_groups[2]))[0]
        if(intersect2) in lowercase_list:
            lowercase_prio = lowercase_list.index(intersect2)
            sum_of_prios += lowercase_prio+1
        if(intersect2) in uppercase_list:
            uppercase_prio = uppercase_list.index(intersect2)
            sum_of_prios += uppercase_prio+27

print(sum_of_prios)
    