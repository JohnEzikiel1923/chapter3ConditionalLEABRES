# Breaking out of a loop
while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)
print('Done!')

# Continue
while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done!')

# indefinite loop = while
# definite loop = for

for i in [5, 4, 3, 2, 1]:
    print (i)
print ('blastoff!')

friends = ['joseph', 'glenn', 'sally']
for friend in friends:
    print('Happy new year: ' +friend)
print('done')
