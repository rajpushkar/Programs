#!/usr/bin/python
#Creating lists, nested lists and printing the elements of the lists


#create a nested list
names=['me', 'you', 'Mehandiratta', ['Pushkar', 'Raj'], 'everyone']

#print the nested list
print names
#this prints the list as it is

#to print the elements individually
for each_item in names:
  print each_item
#this prints all the elements of a list
#if an element of a list is another list, it is printed as it is

#to print all the elements of the sub-list individually:
for each_item in names:
  if(isinstance(each_item, list)):
    for each_sub_item in each_item:
      print each_sub_item
  else:
    print each_item


#if there are many nested lists then:
def nested_list(list1):
  for each_item in list1:
    if(isinstance(each_item, list)):
      nested_list(each_item)
    else:
      print each_item

new_names=['me', 'you', ['Pushkar', 'Raj',['Pushkar Raj', 'Mehandiratta'], 'everyone']]


nested_list(new_names)
