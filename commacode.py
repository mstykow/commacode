# Program prints a user-input list separated by commas and a final "and".

def enum(list):
    a = ''
    for i in list[:-1]:
        a = a + i + ', '
    a = a + 'and ' + list[-1]
    return a

sampleList = []
while True:
    print('Enter list item ' + str(len(sampleList) + 1) +
      ' (Or enter nothing to stop.):')
    item = input()
    if item == '':
        break
    # sampleList = sampleList + [item] # Option to concatenate
    sampleList.append(item) # Option to append

print(enum(sampleList))
