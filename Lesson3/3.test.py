films={'name':'Shawshank redemption', 'rating': 87, 'year':1994, 'director':'Frank Darabont'}
films['starring'] = ['Tim Robbins','Morgan Freeman']
films['budget'] = 123000000
new_actor='Arnold'
films['starring'].append(new_actor)
#del films['rating'] # not reccomended
#films.clear() #to delete the whole dictionary
## films['budget'] = None #To delete value in the key

films['budget'] = None      #delete value only
del films['budget']         #delete the whole key-number
#films.clear()              #smaze cely slovnik

films_copy=films.copy() #copy of the dictionary; changes in new will be reflected in the original as well
films_copy.pop('year',1)
films_copy.get('name')      #return of the value
klice = films.keys()        #extrahuje klice
hodnoty = films.values()    #extrahuje hodnoty
pary = films.items()         #extrahuje pary
print(pary)
print(type(klice))

#print(films['budget'])
print(films['starring'])
print(films)
print(films_copy)