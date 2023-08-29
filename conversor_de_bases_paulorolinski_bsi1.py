def converter_para_decimal(numero, base_de):
    numero_decimal = 0
    potencia = 0

    digitos = '0123456789ABCDEF'
    for digito in numero[::-1].upper():
        numero_decimal += digitos.index(digito) * (base_de ** potencia)
        potencia += 1

    return numero_decimal


def converter_de_decimal(numero_decimal, base_para):
    if numero_decimal == 0:
        return '0'

    digitos = '0123456789ABCDEF'
    numero_convertido = ''
    while numero_decimal > 0:
        resto = numero_decimal % base_para
        numero_convertido = digitos[resto] + numero_convertido
        numero_decimal //= base_para

    return numero_convertido


def converter_base(numero, base_de, base_para):
    try:
        digitos = '0123456789ABCDEF'
        for digito in numero.upper():
            if digito not in digitos[:base_de]:
                return None

        if '.' in numero:
            numero_inteiro, numero_decimal = numero.split('.')
            decimal_part = converter_para_decimal(numero_decimal, base_de) / (base_de ** len(numero_decimal))
            numero_decimal_convertido = converter_de_decimal(int(decimal_part * (base_para ** 6)), base_para)
            return f"{converter_de_decimal(int(numero_inteiro), base_para)}.{numero_decimal_convertido}"
        else:
            return converter_de_decimal(converter_para_decimal(numero, base_de), base_para)
    except ValueError:
        return None


def validar_entrada(numero, base):
    digitos = '0123456789ABCDEF'
    for digito in numero.upper():
        if digito not in digitos[:base]:
            return False
    return True


def testar_conversoes():
    bases = [2, 8, 10, 16]
    numeros = ['1010', '37', '255', 'ABC', '10.101', '57.25', 'F.A', '1001.001']

    for base_de in bases:
        for base_para in bases:
            if base_de != base_para:
                for numero in numeros:
                    if validar_entrada(numero, base_de):
                        numero_convertido = converter_base(numero, base_de, base_para)
                        if numero_convertido:
                            print(f"{numero} (base {base_de}) -> {numero_convertido} (base {base_para})")
                        else:
                            print(f"Erro na conversão de {numero} (base {base_de}) para base {base_para}")


def main():
    print("Conversor de Bases Numéricas")
    print("Bases disponíveis: binário (2), octal (8), decimal (10), hexadecimal (16)")

    while True:
        base_de = int(input("Digite a base de entrada: "))
        base_para = int(input("Digite a base de saída: "))

        if base_de not in [2, 8, 10, 16] or base_para not in [2, 8, 10, 16]:
            print("Bases inválidas. Tente novamente.")
            continue

        numero = input(f"Digite o número na base {base_de}: ")

        if not validar_entrada(numero, base_de):
            print("Número inválido para a base escolhida. Tente novamente.")
            continue

        numero_convertido = converter_base(numero, base_de, base_para)

        if numero_convertido:
            print(f"O número convertido para a base {base_para}: {numero_convertido}")
        else:
            print("Erro na conversão. Certifique-se de que o número está em conformidade com a base escolhida.")

        break


if __name__ == "__main__":
    main()
    print("\nTestando todas as conversões possíveis:")
    testar_conversoes()