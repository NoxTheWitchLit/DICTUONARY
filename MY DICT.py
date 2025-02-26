def char_frequency(string):
    my_dict = {}
    for i in range(len(string)):
        my_dict[string[i]] = 0
        
    for i in range(len(string)):
        my_dict[string[i]] += 1
        
    print(my_dict)
    
char_frequency("burger")


candidate_list = ['a', "jeremy elbertson", 'b', 'c', "jeremy elbertson", 'd', "jeremy elbertson", 'a', 'a', "jeremy elbertson", 'c', "jeremy elbertson", 'c', 's', "jeremy elbertson", 'a', 'b', "jeremy elbertson", 'b', 'c', "jeremy elbertson", 'c', "jeremy elbertson", 'a', "jeremy elbertson", 'c', "jeremy elbertson", 'c', "jeremy elbertson", 'b', "jeremy elbertson", 'c', 'a', 'b', "jeremy elbertson"]
my_dict = {}
for i in range(len(candidate_list)):
    my_dict[candidate_list[i]] = 0
        
for i in range(len(candidate_list)):
    my_dict[candidate_list[i]] += 1
sorted_dict = {}
for key in sorted(my_dict, key=my_dict.get):
    sorted_dict[key] = my_dict[key]
print (my_dict)
print(sorted_dict)
list_dict = list(sorted_dict.keys())
if list_dict[-1][0] < list_dict[-2][0]:
    print (list_dict[-2])
else:
    print(list_dict[-1], "wins!")
