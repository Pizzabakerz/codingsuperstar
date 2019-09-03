from fysom import *

fs = Fysom({'initial': 'one',
             'final': 'one',
             'events': [
                 {'name': 'one', 'src': 'one', 'dst': 'two'},
                 {'name': 'two',  'src': 'two',   'dst': 'one'}]})



print('''
    ---------------------------------
        Finite automata to parse
        string ends with 0
        
        1 - cant reach final state
        0 - will reach final state
        
    ---------------------------------
''')


a = input("enter the parsing string: ")
print(fs.current)

if a[-1] == '1':
    fs.one()
    print(fs.current)
    print("unable to parse the string")
elif a[-1] == '0':
    fs.one()
    fs.two()
    print(fs.current)
    print("Reached final state")