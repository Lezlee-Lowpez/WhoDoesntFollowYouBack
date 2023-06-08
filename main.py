import json

with open('following.json') as f:
    following = json.load(f)

with open('followers (1).json') as f:
    followers = json.load(f)
# getting rid of the none type at the beginning of list

new_list = []
for value in following:
    if value != None:
        new_list.append(value)

# so now i have a list with a bunch of dictionaries inside and i just want the value from each kv pair

list_values = []
for value in new_list:
    list_values.append(value[" "])

list_values.remove(' ')

cleaned_following = list_values[0:-1:2]

new_list_two = []
for value in followers:
    if value != None:
        new_list_two.append(value)

list_values_two = []
for value in new_list_two:
    list_values_two.append(value[" "])

list_values_two.remove(' ')

cleaned_followers = list_values_two[0:-1:2]

following_list = []
for i in cleaned_following:
    if i not in cleaned_followers:
        following_list.append(i)

print(following_list)
print(len(following_list))