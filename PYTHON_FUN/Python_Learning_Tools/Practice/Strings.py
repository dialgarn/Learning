#name = 'Matt'
#print('Hello {}' .format(name))

#print('I:{} R:{} S:{}'.format(1, 2.5, 'foo'))

#print('Name: {}'.format('Paul'))
#print('Name: {name}'.format(name = 'John'))
#print('Name: {[name]}'.format({'name':'George'}))

#print('Last: {2} First: {0}'.format('Paul', 'George', 'John')) #counting begins @ 0


#name = 'matt'
#print(f'My name is {name}')


        #Excercises
#1
name = 'Devin'
age = 17
print(f'{name} is {age}')

#2
paragraph = """\"Python is a great language!", said Fred.
\"I don\'t ever remember having this much fun before!\""""
print(paragraph)

#3  omega pi = 03D6
print('\u03D6')
print('\N{GREEK CAPITAL LETTER OMEGA}')



#4
item = 'car'
cost = 13499.99

print('{:<10}'.format(item), '{:>10,}'.format(cost))
