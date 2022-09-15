# Scrivi una funzione a cui passerai come parametro una stringa, e che manderà in print una versione inversa (al contrario) della stessa stringa (ad esempio "abcd" diventerà "dcba")
def reverse(str):
    str2 = ''
    for i in range(len(str)-1, -1, -1):
        str2 += str[i]
    return str2

def reverse2(str):
    return str[::-1]

print(reverse("ciao a tutti"))
print(reverse2("ciao a tutti"))
