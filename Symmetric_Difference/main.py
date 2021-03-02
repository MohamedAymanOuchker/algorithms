# Find the Symmetric Difference

def sym(args1, args2):
    return args1.symmetric_difference(args2)

i , j = '', ''
args1, args2 = {''}, {''}

while i != 'q':
    i = input("Add element to set 1 (type 'q' to quit): ")
    if i == 'q':
        break
    else:
        args1.add(i)

while j != 'q':
    j = input("Add element to set 2 (type 'q' to quit): ")
    if j == 'q':
        break
    else:
        args2.add(j)

args1.remove('')
args2.remove('')

print('\nThe symmetric difference: ', sym(args1, args2))
