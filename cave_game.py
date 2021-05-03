import shelve
locations=shelve.open('location')
vocabulary=shelve.open('vocabularies')
loc='1'
while True:
    available_exits=",".join(locations['1']['exits'].keys())
    print(locations[loc]['desc'])
    if loc=='0':
        break
    else:
        allexits=locations[loc]['exits'].copy()
        allexits.update(locations[loc]['named exits'])
    direction=input('available exits are '+available_exits).upper()
    print('')
    if len(direction)>1:
        words=direction.split()
        for word in words:
            if word in vocabulary:
                direction=vocabulary[word]
                break
    if direction in allexits:
        loc=allexits[direction]
    else:
        print('you cant go in that direction ')
vocabulary.close()
locations.close()