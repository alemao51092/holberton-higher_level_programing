def list_division(my_list_1, my_list_2, list_length):
    # Creamos una nueva lista para almacenar los resultados de la división
    newList = []
    # Creamos una lista para almacenar los errores ocurridos durante la división
    errorList = []
    
    # Iteramos sobre el rango especificado por list_length
    for idx in range(list_length):
        try:
            # Intentamos realizar la división
            div = my_list_1[idx] / my_list_2[idx]
            # Si la división es exitosa, agregamos el resultado a la nueva lista
            newList.append(div)
        except ZeroDivisionError:
            # Si ocurre una excepción ZeroDivisionError (división por cero)
            # Añadimos un mensaje de error a la lista de errores y agregamos un 0 a la nueva lista
            errorList.append("división por 0")
            newList.append(0)
        except TypeError:
            # Si ocurre una excepción TypeError (tipos incorrectos)
            # Añadimos un mensaje de error a la lista de errores y agregamos un 0 a la nueva lista
            errorList.append("tipo incorrecto")
            newList.append(0)
        except IndexError:
            # Si ocurre una excepción IndexError (índice fuera de rango)
            # Añadimos un mensaje de error a la lista de errores y agregamos un 0 a la nueva lista
            errorList.append("fuera de rango")
            newList.append(0)
        finally:
            # La cláusula finally se ejecuta siempre después de los bloques try y except
            pass
    
    # Imprimimos los errores capturados durante la división
    for e in errorList:
        print(e)
    
    # Retornamos la nueva lista con los resultados de la división
    return newList
