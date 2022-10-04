def calcular_imc():
    # Função que calcula o IMC de um paciente
    print("## Informe os dados do paciente ##")
    nomePaciente = input("Nome: ")
    telefonePaciente = input("Telefone: ")
    peso = float(input("Peso (kg): "))
    altura = float(input("Altura (mt): "))
    imc = peso / altura ** 2
    print(f"O imc do paciente {nomePaciente} é {imc:.2f}")

    
