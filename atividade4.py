def calculadora(parametro1, parametro2, parametro3) -> int:
    calculo = (parametro1+parametro2) or (parametro1-parametro2) or (parametro1*parametro2) or (parametro1/parametro2)
    parametro1 = int(input())
    parametro2 = int(input())
    print("Qual operação deve ser realizada?")
    parametro3 = int(input())
    if (parametro3 == 1):
        return parametro1+parametro2
    if (parametro3 == 2):
        return parametro1-parametro2
    if (parametro3 == 3):
        return parametro1*parametro2
    if (parametro3 == 4):
        return parametro1/parametro2
    else:
        return 0
parametro1 = 10
parametro2 = 10
parametro3 = 4
resultado = calculadora(parametro1, parametro2,parametro3)
print("o resultado é " + str(resultado))
        