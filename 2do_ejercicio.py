def cuadrado(arr):
    out = [0 for _ in arr]      # vector de ceros - tamaño de arr
    out_izq = 0                 # selector posición izquierda de arr
    out_der = len(arr) - 1      # selector posición derecha de arr
    pos = len(arr) - 1          # posición actual
    while out_izq <= out_der:   # compara desde los extremos -  mayor a menor magnitud
        if abs(arr[out_izq]) > abs(arr[out_der]):   # ¿cuál magnitud es mayor? -> cuadrado y añade al final
            out[pos] = arr[out_izq] ** 2
            out_izq += 1
        else:
            out[pos] = arr[out_der] ** 2
            out_der -= 1
        pos -= 1
    return out


# Main
S = "7"
salida = cuadrado([-11, -9, -4, -2, -1, 0, 1, 3, 5, 6, 7, 8, 10, 12])
salida = [x for x in salida if int(x) < int(S+S)]
print(salida)
