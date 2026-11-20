from datetime import datetime

colaboradores = []

SALARIO_BASE = 2000.00

CARGOS = {
    "1": "Assistente Administrativo",
    "2": "Auxiliar de TI",
    "3": "Auxiliar Financeiro",
    "4": "Auxiliar de Produção"
}


def mostrar_menu():
    print("\n" + "-" * 48)
    print("                   MENU PRINCIPAL")
    print("-" * 48)
    print("                    FolhaFácil")
    print("          Sistema de Folha de Pagamento")
    print("-" * 48)

    print("1. Cadastrar colaborador")
    print("2. Gerar Folha de Pagamento")
    print("3. Pesquisar colaborador")
    print("4. Editar colaborador")
    print("5. Excluir colaborador")
    print("6. Relatórios")
    print("0. Sair")

    print("-" * 48)


def executar_opcao(opcao):

    if opcao == "1":
        cadastrar_colaborador()

    elif opcao == "2":
        print("\nGeração de folha de pagamento:")

    elif opcao == "3":
        pesquisar_colaborador()

    elif opcao == "4":
        print("\nEdição de colaborador:")

    elif opcao == "5":
        print("\nExclusão de colaborador:")

    elif opcao == "6":
        print("\nRelatórios:")


def main():

    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção (0 a 6): ").strip()

        if opcao not in ("0", "1", "2", "3", "4", "5", "6"):
            print("\nEssa opção não existe. Digite um número de 0 a 6.")
            input("Pressione Enter para continuar...")
            continue

        if opcao == "0":
            print("\nVocê saiu do FolhaFácil. Até mais!")
            break

        executar_opcao(opcao)



from datetime import datetime


from datetime import datetime


from datetime import datetime

colaboradores = []

SALARIO_BASE = 2000.00

CARGOS = {
    "1": "Assistente Administrativo",
    "2": "Auxiliar de TI",
    "3": "Auxiliar Financeiro",
    "4": "Auxiliar de Produção"
}


def cadastrar_colaborador():

    print("\n" + "=" * 48)
    print("          >>> CADASTRO DE COLABORADOR <<<")
    print("=" * 48)

    print("_" * 40)

    print("\n[  NOME  ]\n")
    nome = input("Nome completo: ").strip()

    while nome == "":
        print("O nome não pode ficar vazio.")
        nome = input("Nome completo: ").strip()

    print("_" * 40)

    print("\n[  TIPO DE COLABORADOR  ]\n")
    print("1 - Padrão")
    print("2 - Comissionado")
    print("3 - Produção")

    print()
    tipo = input("Escolha o tipo: ").strip()

    while tipo not in ("1", "2", "3"):
        print("Tipo inválido. Escolha 1, 2 ou 3.")
        tipo = input("Escolha o tipo: ").strip()

    print("_" * 40)

    print("\n[  MATRÍCULA  ]\n")

    matricula = input("Digite a matrícula (4 dígitos): ").strip()

    while (
        not matricula.isdigit()
        or len(matricula) != 4
        or matricula in [c["matricula"] for c in colaboradores]
    ):
        if not matricula.isdigit() or len(matricula) != 4:
            print("A matrícula deve conter exatamente 4 números.")
        else:
            print("Essa matrícula já está cadastrada.")

        matricula = input("Digite a matrícula (4 dígitos): ").strip()

    print("_" * 40)

    print("\n[  CARGO  ]\n")
    print("1 - Assistente Administrativo")
    print("2 - Auxiliar de TI")
    print("3 - Auxiliar Financeiro")
    print("4 - Auxiliar de Produção")

    print()
    cargo = input("Escolha o cargo: ").strip()

    while cargo not in CARGOS:
        print("Cargo inválido. Escolha uma opção de 1 a 4.")
        cargo = input("Escolha o cargo: ").strip()

    cargo = CARGOS[cargo]

    print("_" * 40)

    print("\n[  REGIME DE CONTRATAÇÃO  ]\n")
    regime = input("Regime de contratação (CLT ou PJ): ").strip().upper()

    while regime not in ("CLT", "PJ"):
        print("Digite CLT ou PJ.")
        regime = input("Regime de contratação (CLT ou PJ): ").strip().upper()

    print("_" * 40)

    if regime == "CLT":

        print("\n[  VALE-TRANSPORTE  ]\n")
        vale_transporte = input(
            "Recebe vale-transporte? (Sim/Não): "
        ).strip().upper()

        while vale_transporte not in ("SIM", "NÃO", "NAO"):
            print("Digite Sim ou Não.")
            vale_transporte = input(
                "Recebe vale-transporte? (Sim/Não): "
            ).strip().upper()

        if vale_transporte == "NAO":
            vale_transporte = "NÃO"

    else:
        vale_transporte = "NÃO SE APLICA"

    print("_" * 40)

    print("\n[  DATA DE ADMISSÃO  ]\n")
    data_admissao = input("Data de admissão (DD/MM/AAAA): ").strip()

    while True:
        try:
            datetime.strptime(data_admissao, "%d/%m/%Y")
            break

        except ValueError:
            print("Data inválida. Digite no formato DD/MM/AAAA.")
            data_admissao = input(
                "Data de admissão (DD/MM/AAAA): "
            ).strip()

    print("_" * 40)

    colaborador = {
        "nome": nome,
        "tipo": tipo,
        "matricula": matricula,
        "cargo": cargo,
        "regime": regime,
        "vale_transporte": vale_transporte,
        "data_admissao": data_admissao,
        "salario_base": SALARIO_BASE
    }

    colaboradores.append(colaborador)

    print("\n" + "=" * 48)
    print("       >>> CADASTRO REALIZADO COM SUCESSO <<<")
    print("=" * 48)

    tipos = {
        "1": "Padrão",
        "2": "Comissionado",
        "3": "Produção"
    }

    print(f"Nome: {nome}")
    print(f"Matrícula: {matricula}")
    print(f"Tipo: {tipos[tipo]}")
    print(f"Cargo: {cargo}")
    print(f"Regime: {regime}")
    print(f"Vale-transporte: {vale_transporte.capitalize()}")
    print(f"Data de admissão: {data_admissao}")
    print(f"Salário-base: R$ {SALARIO_BASE:.2f}")

    print("=" * 48)


def pesquisar_colaborador():

    print("\n" + "=" * 60)
    print("             >>> PESQUISAR COLABORADOR <<<")
    print("=" * 60)

    print("\n[  CONSULTA  ]\n")
    consulta = input("Digite o nome ou a matrícula do colaborador: ").strip()

    while consulta == "":
        print("A pesquisa não pode ficar vazia.")
        consulta = input("Digite a matrícula ou o nome: ").strip()

    encontrados = []

    for colaborador in colaboradores:
        if (
            consulta.casefold() in colaborador["nome"].casefold()
            or consulta == colaborador["matricula"]
        ):
            encontrados.append(colaborador)

    if not encontrados:
        print("\nNenhum colaborador encontrado.")
        return

    def calcular_inss(salario):
        faixas = [
            (1621.00, 0.075),
            (2902.84, 0.09),
            (4354.27, 0.12),
            (8475.55, 0.14)
        ]

        total = 0
        limite_anterior = 0

        for limite, aliquota in faixas:
            if salario > limite_anterior:
                parcela = min(salario, limite) - limite_anterior
                total += parcela * aliquota
                limite_anterior = limite
            else:
                break

        return round(total, 2)

    def moeda(valor):
        return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

    tipos = {
        "1": "Padrão",
        "2": "Comissionado",
        "3": "Produção"
    }

    for colaborador in encontrados:

        nome = colaborador["nome"]
        matricula = colaborador["matricula"]
        cargo = colaborador["cargo"]
        data_admissao = colaborador["data_admissao"]
        tipo = tipos.get(colaborador["tipo"], colaborador["tipo"])
        regime = colaborador["regime"]
        vale_transporte = colaborador["vale_transporte"]
        salario = colaborador["salario_base"]

        print("\n" + "=" * 60)
        print("                 DADOS DO COLABORADOR")
        print("=" * 60)

        print(f"{'Funcionário':<32}{'Matrícula'}")
        print(f"{nome:<32}{matricula}")

        print()

        print(f"{'Cargo':<32}{'Data de admissão'}")
        print(f"{cargo:<32}{data_admissao}")

        print()

        print(f"{'Tipo de colaborador':<32}{'Regime'}")
        print(f"{tipo:<32}{regime}")

        print()

        if regime == "PJ":
            vale_transporte_exibicao = "Não se aplica"
        else:
            vale_transporte_exibicao = vale_transporte.capitalize()

        print(f"{'Vale-transporte':<32}{'Salário bruto'}")
        print(f"{vale_transporte_exibicao:<32}{moeda(salario)}")

        print("-" * 60)

        if regime == "CLT":

            desconto_inss = calcular_inss(salario)

            if vale_transporte == "SIM":
                desconto_vt = round(salario * 0.06, 2)
            else:
                desconto_vt = 0

            total_descontos = desconto_inss + desconto_vt
            salario_liquido = salario - total_descontos

            print(f"{'Desconto INSS':<32}{moeda(desconto_inss)}")
            print(f"{'Desconto vale-transporte':<32}{moeda(desconto_vt)}")

            print("-" * 60)

            print(f"{'Total de descontos':<32}{moeda(total_descontos)}")
            print()
            print(f"{'SALÁRIO LÍQUIDO':<25}{moeda(salario_liquido):>20}")

        else:
            print("Cálculo de descontos não aplicado automaticamente.")
            print("O regime PJ possui regras diferentes de tributação.")

        print("=" * 60)


if __name__ == "__main__":
    main()