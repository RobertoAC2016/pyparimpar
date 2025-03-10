# calcular el area de un rectangulo de lo basico a pro paso a paso

# def calcular_el_area_de_un_rectangulo(base, altura):
#     return base * altura

# def main():
#     longitud_base = float(input("Introduce la longitud de la base: "))
#     longitud_altura = float(input("Introduce la longitud de la altura: "))

#     area = calcular_el_area_de_un_rectangulo(longitud_base, longitud_altura)
#     print(f"El area del rectangulo es: {area}")

# if __name__ == "__main__":
#     main()
# // TODO: calcular el perimetro de un rectangulo

# Voy a mostrar como se utiliza un docstring basico y el complemento
# El docstring va inmediatamente debajo de la definicion de la funcion
# para verificar que docstring funciona correctamente se puede utilizar
# la funcion help(nombre_de_la_funcion) y se mostrara la documentacion
# de la funcion

def calcular_el_area_de_un_rectangulo(base, altura):
    """
    Esta funcion calcula el area de un rectangulo

    Args:
        base (float): La longitud de la base del rectangulo
        altura (float): La longitud de la altura del rectangulo

    Raises:
        ValueError: Si alguno de los argumentos no es numerico
        esto va a generar una excepcion de tipo ValueError

    Returns:
        float: El area del rectangulo

    Author:
        Carlos A. Rodriguez // Aqui vas aponer el author de la funcion

    Fecha:
        12/12/2020 // Aqui vas a poner la fecha de creacion de la funcion
    """
    # Esta es la documentacion basico de la docstring, esto se hace
    # para que cualquier persona que lea el codigo pueda entender
    # que hace la funcion y como utilizarla
    # los argumentos que recibe y el tipo de dato que retorna
    # sino retorna nada se pone None
    # ahora argumentos acionales que se pueden agregar en la docstring
    return base * altura

def calcular_el_perimetro_de_un_rectangulo(base, altura):
    return 2 * (base + altura)

def main():
    try:
        base = float(input("Introduce la longitud de la base: "))
        altura = float(input("Introduce la longitud de la altura: "))

        area = calcular_el_area_de_un_rectangulo(base, altura)
        perimetro = calcular_el_perimetro_de_un_rectangulo(base, altura)

        print(f"El area del rectangulo es: {area}")
        print(f"El perimetro del rectangulo es: {perimetro}")
    except ValueError:
        print("Por favor, introduce valores numericos validos")

if __name__ == "__main__":
    main()

