def updateInventory(arr1, arr2):
        list = []
        arr1_dict = {x[1]: x[0] for x in arr1}
        arr2_dict = {x[1]: x[0] for x in arr2}
        arr1_dict.update(arr2_dict)
        [list.extend([k,v]) for k,v in arr1_dict.items()]
        return list

curInv =[
	     [21, "Bowling Ball"], 
	     [2, "Dirty Sock"],
	     [1, "Hair Pin"], 
	     [5, "Microphone"] 
] 
  
newInv =[
	    [2, "Hair Pin"], 
	    [3, "Half-Eaten Apple"], 
	    [67, "Bowling Ball"], 
	    [7, "Toothpaste"] 
]

print(updateInventory(curInv, newInv))
