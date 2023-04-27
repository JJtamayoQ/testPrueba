def cambio_min_no_construible(coins):
    coins.sort()                # ordena array monedero
    change = 0                  # cambio construido
    for coin in coins:          # evalua cada moneda del array monedero
        """ Pueden ocurrir tres casos:
        Con cambio = 13
        1. moneda < cambio + 1      Es construible e.g. (moneda = 3) 13-2=11 -> 11+3=14
        2. moneda = cambio + 1      Es construible e.g. (moneda = 14) se entrega moneda como cambio
        3. moneda > cambio + 1      No es construible e.g. (moneda = 15) el cambio máx. es 13
                                    con 15 tendría que restarse un valor para llegar a 14
        """
        if coin > change + 1:       # condición suficiente para conocer el cambio minimo no construible
            break
        change += coin              # actualiza el cambio máx.
    return change + 1


print(cambio_min_no_construible([5, 7, 1, 1, 2, 3, 22]))
print(cambio_min_no_construible([1, 1, 1, 1, 1]))
print(cambio_min_no_construible([1, 5, 1, 1, 1, 10, 15, 20, 100]))
