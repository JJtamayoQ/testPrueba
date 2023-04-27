# MD5 Hash =  7b3dd5401d0755ea6baf87f3757951eb

S = "7"

entrada_int = [70, 6777777, 5, 4, 3, 2, 7, 7, 29, 1]    # vector dado
entrada_str = [str(x) for x in entrada_int]             # int to str
tamano = len(entrada_str)                               # tamaño del vector de entrada
salida = [0]*tamano                                     # resultado
pos = 0                                                 # posición en la lista


def remplazar(entrada):
    out = ""
    for x in entrada:
        if x != S:
            out = out + x
    return out


if tamano <= 100:               # n debe ser menor o igual a 100
    for x in entrada_str:       # list comprehension
        if len(x) > int(S):     # verifica el número de digitos
            print("Número de digitos excedido")
            exit()
        if S in x:              # busqueda de S en la lista
            entrada_str[pos] = remplazar(entrada_str[pos])
        pos += 1                # posición en la lista
        salida[tamano-pos] = entrada_str[pos-1]
else:
    print("n es mayor a 100 -> entrada no es valido")
    exit()

salida = [int(x) for x in salida if x != ""]

print(salida)