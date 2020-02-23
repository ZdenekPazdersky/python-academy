#2Do
#Create a script that will print each key - value pair to the terminal in format: "Key: <value> | Value: <value>"
####
film = {'name':'Forrest Gump',
        'made':1994,
        'director':'Robert Zemeckis',
        'soundtrack':'Multiple',
        'starring':'Tom Hanks',
        'fun_fact':'''The house used in Forrest Gump is
                    the same house used in The Patriot
                    (2000). Some paneling was changed
                    for interior shots  in the latter
                    film.'''}
while film:
    film_ext = film.popitem()
    print('Key: '+ str(film_ext[0]) + ' | ' + 'Value: '+ str(film_ext[1]))