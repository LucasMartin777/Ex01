def pes_para_metros(pes):
    """Converte pés para metros."""
    return pes * 0.3048

def metros_para_pes(metros):
    """Converte metros para pés."""
    return metros * 3.281

def jardas_para_metros(jardas):
    """Converte jardas para metros."""
    return jardas * 0.9144

def jardas_para_pes(jardas):
    """Converte jardas para pés."""
    metros = jardas_para_metros(jardas)
    return metros_para_pes(metros)

def conversor():
    print("Bem-vindo ao Conversor de Unidades!")
    print("Escolha a conversão que deseja realizar:")
    print("1 - Pés para Metros")
    print("2 - Metros para Pés")
    print("3 - Jardas para Metros")
    print("4 - Jardas para Pés")

    opcao = input("Digite o número da opção desejada: ")

    if opcao == "1":
        valor = float(input("Digite o valor em pés: "))
        resultado = pes_para_metros(valor)
        print(f"{valor} pés equivalem a {resultado:.4f} metros.")

    elif opcao == "2":
        valor = float(input("Digite o valor em metros: "))
        resultado = metros_para_pes(valor)
        print(f"{valor} metros equivalem a {resultado:.4f} pés.")

    elif opcao == "3":
        valor = float(input("Digite o valor em jardas: "))
        resultado = jardas_para_metros(valor)
        print(f"{valor} jardas equivalem a {resultado:.4f} metros.")

    elif opcao == "4":
        valor = float(input("Digite o valor em jardas: "))
        resultado = jardas_para_pes(valor)
        print(f"{valor} jardas equivalem a {resultado:.4f} pés.")

    else:
        print("Opção inválida. Tente novamente.")
