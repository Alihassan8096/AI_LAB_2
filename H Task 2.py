originalList =  [
    {"V":"S001"}, {"V": "S002"},
    {"VI": "S001"}, {"VI": "S005"},
    {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}
]
print ("Original List :", originalList)

#printing unique values in the list

uniqueValues = set (val for dic in originalList for val in dic.values())
print("Unique Values in the list are :", uniqueValues)
