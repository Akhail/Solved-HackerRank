mayor = None
suma = 0
for j in range(0,4):
    for i in range(0,4):
        for idx, x in enumerate(arr[j:j+3]):
            if idx == 1:
                suma += x[i+1]
            else:
                suma += sum(x[i:i+3])
        if mayor is None:
            mayor = suma
        elif suma > mayor:
            mayor = suma
        suma = 0
print(mayor)