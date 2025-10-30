def adicionar_funcionario(funcionarios):
    nome = input("Digite o nome do funcionário: ")
    salario = float(input("Digite o salário do funcionário (use ponto para decimais): "))
    funcionarios[nome] = {"salario": salario}
    print(f"Funcionário {nome} cadastrado com sucesso!\n")


def listar_funcionarios(funcionarios):
    if not funcionarios:
        print("Nenhum funcionário cadastrado.\n")
    else:
        print("\n--- Lista de Funcionários ---")
        for nome, dados in funcionarios.items():
            print(f"Nome: {nome} | Salário: R$ {dados['salario']:.2f}")
        print()


def buscar_funcionario(funcionarios):
    if not funcionarios:
        print("Nenhum funcionário cadastrado.\n")
        return
    nome = input("Digite o nome do funcionário que deseja buscar: ")
    if nome in funcionarios:
        print(f"Funcionário encontrado: {nome} — Salário: R$ {funcionarios[nome]['salario']:.2f}\n")
    else:
        print("Funcionário não encontrado.\n")


def calcular_media_salarial(funcionarios):
    if not funcionarios:
        print("Nenhum funcionário cadastrado.\n")
        return
    total = sum(dados["salario"] for dados in funcionarios.values())
    media = total / len(funcionarios)
    print(f"Média salarial dos funcionários: R$ {media:.2f}\n")


# Programa principal
funcionarios = {}

print("=== SISTEMA DE GERENCIAMENTO DE FUNCIONÁRIOS ===")

while True:
    print("\nQual opção deseja?")
    print("1 - Cadastrar Funcionário")
    print("2 - Listar Funcionários")
    print("3 - Buscar Funcionário por Nome")
    print("4 - Calcular Média Salarial")
    print("5 - Sair")

    try:
        opcao = int(input("Digite a opção desejada: "))
    except ValueError:
        print("Por favor, digite um número válido.\n")
        continue

    if opcao == 1:
        print("\n--- Cadastro de Funcionário ---")
        adicionar_funcionario(funcionarios)
    elif opcao == 2:
        listar_funcionarios(funcionarios)
    elif opcao == 3:
        buscar_funcionario(funcionarios)
    elif opcao == 4:
        calcular_media_salarial(funcionarios)
    elif opcao == 5:
        print("Saindo do sistema... Até mais!")
        break
    else:
        print("Opção inválida, tente novamente.\n")
