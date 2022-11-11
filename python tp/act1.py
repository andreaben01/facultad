#CALCULADORA DE IMPUESTOS
ing=float(input("Ingrese un valor:"))

if ing < 85718:
    imp= (ing * 18 / 100) - 596.2
    if imp < 0:
        print("El impuesto es 0.0 pesos.")
    else:
        print(f"El impuesto es:{round(imp)}")
else:
    exc=ing-85718
    imp= (exc * 32 / 100) + 14319.2
    print(f"El impuesto es: {round(imp)}")

