# creare e stampare:
# 1 variabile con scope globale
# 1 variabile con scope locale
# 1 variabile con scope enclosing
# stampare 1 variabile con scope built-in

var_global = 10
print('globale:', var_global)


def func():
    var_enclosing = 15
    print('enclosing:', var_enclosing)

    def func2():
        var_local = 20
        print('locale:', var_local)

    func2()


func()

print('built-in:', list)
