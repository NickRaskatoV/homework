slovar = {'кот': 'cat', 'медведь': 'bear', 'лифт': 'elevator'}
print(slovar)
slovar['гитара'] = 'guitar'
print(slovar)
print(slovar['лифт'])
print(slovar.get('зебра', 'bear'))
print(slovar.setdefault('зебра', 'huebra'))
print(slovar)
