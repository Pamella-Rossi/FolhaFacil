from datetime import datetime

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
       folha_pagamento_geral()

    elif opcao == "3":
        pesquisar_colaborador()

    elif opcao == "4":
        print("\nEdição de colaborador:")

    elif opcao == "5":
        print("\nExclusão de colaborador:")

    elif opcao == "6":
        menu_relatorios()

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


def moeda(valor):
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

def folha_pagamento_geral():

    if not colaboradores:
        print("\nNenhum colaborador cadastrado.")
        return

    folha = []

    total_bruto = 0
    total_inss = 0
    total_vt = 0
    total_descontos = 0
    total_liquido = 0

    tipos = {
        "1": "Padrão",
        "2": "Comissionado",
        "3": "Produção"
    }

    meses = [
        "", "JANEIRO", "FEVEREIRO", "MARÇO",
        "ABRIL", "MAIO", "JUNHO",
        "JULHO", "AGOSTO", "SETEMBRO",
        "OUTUBRO", "NOVEMBRO", "DEZEMBRO"
    ]

    periodo = f"{meses[datetime.now().month]} / {datetime.now().year}"

    def ler_valor(mensagem):
        while True:
            try:
                valor = float(input(mensagem).strip().replace(",", "."))

                if valor < 0:
                    print("O valor não pode ser negativo.")
                    continue

                return valor

            except ValueError:
                print("Digite um valor numérico válido.")

    def ler_quantidade(mensagem):
        while True:
            try:
                quantidade = int(input(mensagem).strip())

                if quantidade < 0:
                    print("A quantidade não pode ser negativa.")
                    continue

                return quantidade

            except ValueError:
                print("Digite uma quantidade inteira válida.")

    print("\n" + "=" * 60)
    print("                  FOLHAFÁCIL")
    print("               GERAÇÃO DA FOLHA")
    print("=" * 60)

    print(f"\nForam encontrados {len(colaboradores)} colaboradores.")
    print("\nIniciando atualização dos dados de pagamento...")

    for indice, colaborador in enumerate(colaboradores, start=1):

        nome = colaborador["nome"]
        tipo = colaborador["tipo"]
        regime = colaborador["regime"]

        salario_base = colaborador["salario_base"]

        vendas = 0
        percentual_comissao = 0
        comissao = 0

        pecas = 0
        valor_peca = 0
        total_producao = 0

        print("\n" + "_" * 60)

        print(f"\n[{indice}/{len(colaboradores)}] {nome.upper()}")

        print(f"\nMatrícula: {colaborador['matricula']}")
        print(f"Tipo: {tipos[tipo]}")
        print(f"Regime: {regime}")

        if tipo == "2":

            vendas = ler_valor(
                "\nInforme o valor total de vendas no período:\n> "
            )

            percentual_comissao = ler_valor(
                "\nInforme o percentual de comissão:\n> "
            )

            while percentual_comissao > 100:
                print("O percentual não pode ser maior que 100%.")
                percentual_comissao = ler_valor(
                    "Informe o percentual de comissão:\n> "
                )

            comissao = round(
                vendas * percentual_comissao / 100, 2
            )

            print("\n" + "-" * 40)
            print(f"Comissão cadastrada: {percentual_comissao:g}%")
            print(f"Comissão calculada: {moeda(comissao)}")

        elif tipo == "3":

            pecas = ler_quantidade(
                "\nInforme a quantidade de peças produzidas:\n> "
            )

            valor_peca = ler_valor(
                "\nInforme o valor pago por peça:\n> "
            )

            total_producao = round(pecas * valor_peca, 2)

            print("\n" + "-" * 40)
            print(f"Valor por peça: {moeda(valor_peca)}")
            print(f"Total da produção: {moeda(total_producao)}")

        else:
            print("\n" + "-" * 40)
            print("Nenhuma informação adicional necessária.")

        print("\nDados registrados com sucesso!")

        salario_bruto = round(
            salario_base + comissao + total_producao, 2
        )

        desconto_inss = 0
        desconto_vt = 0

        if regime == "CLT":

            desconto_inss = 155.69

            if colaborador["vale_transporte"] == "SIM":
                desconto_vt = round(salario_base * 0.06, 2)

        descontos = round(desconto_inss + desconto_vt, 2)

        salario_liquido = round(salario_bruto - descontos, 2)

        # ARMAZENAMENTO DOS RESULTADOS DA FOLHA

        dados_folha = {
            "nome": nome,
            "matricula": colaborador["matricula"],
            "cargo": colaborador["cargo"],
            "tipo": tipos[tipo],
            "regime": regime,
            "salario_base": salario_base,
            "vendas": vendas,
            "percentual_comissao": percentual_comissao,
            "comissao": comissao,
            "pecas": pecas,
            "valor_peca": valor_peca,
            "total_producao": total_producao,
            "salario_bruto": salario_bruto,
            "inss": desconto_inss,
            "vale_transporte": desconto_vt,
            "descontos": descontos,
            "salario_liquido": salario_liquido
        }

        folha.append(dados_folha)

        total_bruto += salario_bruto
        total_inss += desconto_inss
        total_vt += desconto_vt
        total_descontos += descontos
        total_liquido += salario_liquido

    print("\n" + "_" * 60)
    print("\nTodos os dados foram atualizados!")

    print("\nCalculando salários e descontos...")
    print("\nAguarde...")

    print("\n" + "=" * 60)
    print("                  FOLHAFÁCIL")
    print("               FOLHA DE PAGAMENTO")
    print("=" * 60)

    print(f"\nPERÍODO: {periodo}")

    for indice, dados in enumerate(folha, start=1):

        print("\n")
        print(f"[{indice}] {dados['nome'].upper()}")
        print("-" * 60)

        print(f"Matrícula: {dados['matricula']}")
        print(f"Cargo: {dados['cargo']}")
        print(f"Tipo: {dados['tipo']}")
        print(f"Regime: {dados['regime']}")

        print("\nCOMPOSIÇÃO SALARIAL\n")

        print(f"{'Salário-base:':<34}{moeda(dados['salario_base']):>20}")

        if dados["tipo"] == "Comissionado":

            print(f"{'Total de vendas:':<34}{moeda(dados['vendas']):>20}")

            print(
                f"{'Percentual de comissão:':<34}"
                f"{str(dados['percentual_comissao']) + '%':>20}"
            )

            print(f"{'Valor da comissão:':<34}{moeda(dados['comissao']):>20}")

        elif dados["tipo"] == "Produção":

            print(f"{'Peças produzidas:':<34}{dados['pecas']:>20}")

            print(f"{'Valor por peça:':<34}{moeda(dados['valor_peca']):>20}")

            print(
                f"{'Total da produção:':<34}"
                f"{moeda(dados['total_producao']):>20}"
            )

        print()
        print(f"{'Salário bruto:':<34}{moeda(dados['salario_bruto']):>20}")

        print("\nDESCONTOS\n")

        if dados["regime"] == "CLT":

            print(f"{'INSS:':<34}{moeda(dados['inss']):>20}")

            print(
                f"{'Vale-transporte:':<34}"
                f"{moeda(dados['vale_transporte']):>20}"
            )

            print(
                f"{'Total de descontos:':<34}"
                f"{moeda(dados['descontos']):>20}"
            )

        else:
            print("Descontos automáticos não aplicados ao regime PJ.")

        print()

        print(
            f"{'SALÁRIO LÍQUIDO:':<34}"
            f"{moeda(dados['salario_liquido']):>20}"
        )

    print("\n" + "=" * 60)
    print("                 RESUMO GERAL DA FOLHA")
    print("=" * 60)

    print(
        f"{'Total de colaboradores:':<34}"
        f"{len(folha):>20}"
    )

    print()

    print(
        f"{'Total de salários brutos:':<34}"
        f"{moeda(total_bruto):>20}"
    )

    print()

    print(
        f"{'Total de INSS:':<34}"
        f"{moeda(total_inss):>20}"
    )

    print(
        f"{'Total de vale-transporte:':<34}"
        f"{moeda(total_vt):>20}"
    )

    print()

    print(
        f"{'Total de descontos:':<34}"
        f"{moeda(total_descontos):>20}"
    )

    print("\n" + "=" * 60)

    print(
        f"{'TOTAL LÍQUIDO A PAGAR:':<34}"
        f"{moeda(total_liquido):>20}"
    )

    print("=" * 60)

    print("\nFolha de pagamento gerada com sucesso!")

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

        print("=" * 60)

def menu_relatorios():

    while True:
        print("\n" + "-" * 48)
        print("                    RELATÓRIOS")
        print("-" * 48)

        print("1. Relatório geral")
        print("2. Relatório por cargo")
        print("0. Voltar ao menu principal")

        print("-" * 48)

        opcao_relatorio = input("Escolha uma opção (0 a 2): ").strip()

        if opcao_relatorio not in ("0", "1", "2"):
            print("\nEssa opção não existe. Digite um número de 0 a 2.")
            input("Pressione Enter para continuar...")
            continue

        if opcao_relatorio == "0":
            break

        executar_relatorio(opcao_relatorio)

def executar_relatorio(opcao_relatorio):

    if opcao_relatorio == "1":
        pass

    elif opcao_relatorio == "2":
        pass



if __name__ == "__main__":
    main()