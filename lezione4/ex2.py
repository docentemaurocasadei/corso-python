# l'obiettivo è di registrare l'ingresso di dipendenti in una azienda
# per primo entra Stefano alle 8:30
# successivamente entra Debora alle 8:40
# per ultima entra Alessia alle 8:45
# realizzare tale esempio con:
# - tupla nominata t_timbratura
# - lista nominata l_timbratura
# - dictionary nominato d_timbratura
# #
t_timbratura = ('Stefano', 'Debora', 'Alessia')
l_timbratura = ['Stefano']
l_timbratura.append('Debora')
l_timbratura.append('Alessia')
d_timbratura = {'Stefano': '8:30'}
d_timbratura['Debora'] = '8:40'
d_timbratura['Alessia'] = '8:45'

print('tupla', t_timbratura)
print('lista', l_timbratura)
print('dictionary', d_timbratura)