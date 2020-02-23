###2DO###
# At the beginning we have dictionary with tram stations. Our goal is to identify which stations are included in each list.
# Example of running script:
#
# {'Hlavni nadr.'}
#########
tram_stations = {
'No.1' : ['Reckovice', 'Semilasso', 'Husitska', 'Jungmannova', 'Kartouzska', 'Sumavska', 'Hrnicrska', 'Pionyrska', 'Antoninska', 'Moravske nam.', 'Malinovske nam', 'Hlavni nadr.', 'Nove sady', 'Hybesova', 'Vaclavska', 'Mendlovo nam.', 'Vystaviste main', 'Vystaviste G2', 'Lipova', 'Pisarky'],
'No.2' : ['Zidenice', 'Kuldova', 'Vojenska nemocnice', 'Tkalcovska', 'Kornerova', 'Malinovske nam.', 'Hlavni nadr.', 'Nove Sady', 'Hybesova', 'Vaclavska', 'Mendlovo nam.', 'Porici', 'Nemocnice UM', 'Celni', 'Hluboka', 'Ustredni hrbitov'],
'No.3' : ['Husovice','Nam. republiky','Vozovna Husovice','Mostecka','Travnickova', 'Tkalcovska', 'Kornerova', 'Malinovske nam.', 'Hlavni nadr.', 'Nove sady', 'Silingrovo nam.', 'Ceska', 'Komenskeho nam.', 'Obilni trh', 'Uvoz']
}

# station = input('Enter station: ')
# if station in tram_stations.get('No.1'):
#     print('Tram Number 1')
# elif station in tram_stations.get('No.2'):
#     print('Tram Number 2')
# elif station in tram_stations.get('No.3'):
#     print('Tram Number 3')
# else: print('Station not included in the list')
# :-) Engeto task was ti create an intersection
station_common = set(tram_stations['No.1']).intersection(set(tram_stations['No.2'])).intersection(set(tram_stations['No.3']))
print(station_common)
