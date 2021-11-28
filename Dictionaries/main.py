translator = {'sowa': 'owl',
              'pies': 'dog',
              'kot': 'cat',
              'mysz': 'mouse'}

print(len(translator))

#print(translator[0])
#print(translator['tygrys'])
print(translator['pies'])

print(translator.get('mysz'))
print(translator.get('tygrys'))

print(translator.keys())
print(translator.values())
print(translator.items())

print("----------------------------")

translator.update({'tygrys': 'tiger', 'ryba': 'fish'})
print(translator.get('tygrys'))

print(translator.pop('mysz'))
print(translator.popitem())
translator.clear()
print(translator)
