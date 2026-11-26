# INTEGRANTES:
# Pamella de Rossi Oliveira
# Yasmin Aparecida Araujo Rocha
# Luana Alves Ferreira
# Giulia Beatriz da Silva Freitas


from datetime import datetime


SALARIO_BASE = 2000.00

CARGOS = {
    "1": "Assistente Administrativo",
    "2": "Auxiliar de TI",
    "3": "Auxiliar Financeiro",
    "4": "Auxiliar de Produção"
}

colaboradores = []

class Colaborador:
    def __init__(
        self,
        matricula,
        nome,
        salarioBase,
        cargo,
        regime,
        vale_transporte,
        data_admissao
    ):
        self.matricula = matricula
        self.nome = nome
        self.salarioBase = salarioBase
        self.cargo = cargo
        self.regime = regime
        self.vale_transporte = vale_transporte
        self.data_admissao = data_admissao

    def calcularSalarioFinal(self):
        return self.salarioBase

    def exibirDados(self):
        print(f"Nome: {self.nome}")
        print(f"Matrícula: {self.matricula}")
        print(f"Cargo: {self.cargo}")
        print(f"Regime: {self.regime}")
        print(f"Vale-transporte: {self.vale_transporte}")
        print(f"Data de admissão: {self.data_admissao}")
        print(f"Salário-base: {moeda(self.salarioBase)}")

class ColaboradorPadrao(Colaborador):
    def calcularSalarioFinal(self):
        return self.salarioBase

class ColaboradorComissionado(Colaborador):
    def __init__(
        self,
        matricula,
        nome,
        salarioBase,
        cargo,
        regime,
        vale_transporte,
        data_admissao
    ):
        super().__init__(
            matricula,
            nome,
            salarioBase,
            cargo,
            regime,
            vale_transporte,
            data_admissao
        )
        self.valorVendas = 0.0
        self.percentualComissao = 0.0

    def calcularComissao(self):
        return round(
            self.valorVendas * self.percentualComissao / 100,
            2
        )

    def calcularSalarioFinal(self):
        return round(
            self.salarioBase + self.calcularComissao(),
            2
        )

class ColaboradorProducao(Colaborador):
    def __init__(
        self,
        matricula,
        nome,
        salarioBase,
        cargo,
        regime,
        vale_transporte,
        data_admissao
    ):
        super().__init__(
            matricula,
            nome,
            salarioBase,
            cargo,
            regime,
            vale_transporte,
            data_admissao
        )
        self.quantidadePecas = 0
        self.valorPorPeca = 0.0

    def calcularProdutividade(self):
        return round(
            self.quantidadePecas * self.valorPorPeca,
            2
        )

    def calcularSalarioFinal(self):
        return round(
            self.salarioBase + self.calcularProdutividade(),
            2
        )

def moeda(valor):
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def obter_tipo_colaborador(colaborador):
    if isinstance(colaborador, ColaboradorComissionado):
        return "Comissionado"
    elif isinstance(colaborador, ColaboradorProducao):
        return "Produção"
    else:
        return "Padrão"


def buscar_colaborador(matricula):
    for colaborador in colaboradores:
        if colaborador.matricula == matricula:
            return colaborador
    return None


def ler_sim_nao(mensagem):
    resposta = input(mensagem).strip().casefold()

    while resposta not in ("sim", "não", "nao"):
        print("Digite Sim ou Não.")
        resposta = input(mensagem).strip().casefold()

    return "SIM" if resposta == "sim" else "NÃO"


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


def criar_colaborador(
    tipo,
    matricula,
    nome,
    cargo,
    regime,
    vale_transporte,
    data_admissao,
    salario_base=SALARIO_BASE
):
    if tipo == "1":
        return ColaboradorPadrao(
            matricula, nome, salario_base, cargo, regime,
            vale_transporte, data_admissao
        )
    elif tipo == "2":
        return ColaboradorComissionado(
            matricula, nome, salario_base, cargo, regime,
            vale_transporte, data_admissao
        )
    else:
        return ColaboradorProducao(
            matricula, nome, salario_base, cargo, regime,
            vale_transporte, data_admissao
        )

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
        editar_colaborador()
    elif opcao == "5":
        excluir_colaborador()
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
        or buscar_colaborador(matricula) is not None
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

    cargo_opcao = input("Escolha o cargo: ").strip()

    while cargo_opcao not in CARGOS:
        print("Cargo inválido. Escolha uma opção de 1 a 4.")
        cargo_opcao = input("Escolha o cargo: ").strip()

    cargo = CARGOS[cargo_opcao]

    print("_" * 40)
    print("\n[  REGIME DE CONTRATAÇÃO  ]\n")

    regime = input("Regime de contratação (CLT ou PJ): ").strip().upper()

    while regime not in ("CLT", "PJ"):
        print("Digite CLT ou PJ.")
        regime = input("Regime de contratação (CLT ou PJ): ").strip().upper()

    print("_" * 40)

    if regime == "CLT":
        print("\n[  VALE-TRANSPORTE  ]\n")
        resposta = ler_sim_nao("Recebe vale-transporte? (Sim/Não): ")
        vale_transporte = resposta
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

    colaborador = criar_colaborador(
        tipo,
        matricula,
        nome,
        cargo,
        regime,
        vale_transporte,
        data_admissao
    )

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
    print(f"Salário-base: {moeda(SALARIO_BASE)}")
    print("=" * 48)

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

    meses = [
        "", "JANEIRO", "FEVEREIRO", "MARÇO",
        "ABRIL", "MAIO", "JUNHO",
        "JULHO", "AGOSTO", "SETEMBRO",
        "OUTUBRO", "NOVEMBRO", "DEZEMBRO"
    ]

    periodo = f"{meses[datetime.now().month]} / {datetime.now().year}"

    print("\n" + "=" * 60)
    print("                  FOLHAFÁCIL")
    print("               GERAÇÃO DA FOLHA")
    print("=" * 60)

    print(f"\nForam encontrados {len(colaboradores)} colaboradores.")
    print("\nIniciando atualização dos dados de pagamento...")

    for indice, colaborador in enumerate(colaboradores, start=1):
        tipo = obter_tipo_colaborador(colaborador)

        print("\n" + "_" * 60)
        print(f"\n[{indice}/{len(colaboradores)}] {colaborador.nome.upper()}")
        print(f"\nMatrícula: {colaborador.matricula}")
        print(f"Tipo: {tipo}")
        print(f"Regime: {colaborador.regime}")

        vendas = 0
        percentual_comissao = 0
        comissao = 0
        pecas = 0
        valor_peca = 0
        total_producao = 0

        if isinstance(colaborador, ColaboradorComissionado):
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

            colaborador.valorVendas = vendas
            colaborador.percentualComissao = percentual_comissao
            comissao = colaborador.calcularComissao()

            print("\n" + "-" * 40)
            print(f"Comissão cadastrada: {percentual_comissao:g}%")
            print(f"Comissão calculada: {moeda(comissao)}")

        elif isinstance(colaborador, ColaboradorProducao):
            pecas = ler_quantidade(
                "\nInforme a quantidade de peças produzidas:\n> "
            )

            valor_peca = ler_valor(
                "\nInforme o valor pago por peça:\n> "
            )

            colaborador.quantidadePecas = pecas
            colaborador.valorPorPeca = valor_peca
            total_producao = colaborador.calcularProdutividade()

            print("\n" + "-" * 40)
            print(f"Valor por peça: {moeda(valor_peca)}")
            print(f"Total da produção: {moeda(total_producao)}")

        else:
            print("\n" + "-" * 40)
            print("Nenhuma informação adicional necessária.")

        print("\nDados registrados com sucesso!")

        salario_bruto = colaborador.calcularSalarioFinal()

        desconto_inss = 0
        desconto_vt = 0

        if colaborador.regime == "CLT":
            desconto_inss = 155.69

            if colaborador.vale_transporte == "SIM":
                desconto_vt = round(colaborador.salarioBase * 0.06, 2)

        descontos = round(desconto_inss + desconto_vt, 2)
        salario_liquido = round(salario_bruto - descontos, 2)

        dados_folha = {
            "nome": colaborador.nome,
            "matricula": colaborador.matricula,
            "cargo": colaborador.cargo,
            "tipo": tipo,
            "regime": colaborador.regime,
            "salario_base": colaborador.salarioBase,
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
            consulta.casefold() in colaborador.nome.casefold()
            or consulta == colaborador.matricula
        ):
            encontrados.append(colaborador)

    if not encontrados:
        print("\nNenhum colaborador encontrado.")
        return

    for colaborador in encontrados:
        tipo = obter_tipo_colaborador(colaborador)

        print("\n" + "=" * 60)
        print("                 DADOS DO COLABORADOR")
        print("=" * 60)

        print(f"{'Funcionário':<32}{'Matrícula'}")
        print(f"{colaborador.nome:<32}{colaborador.matricula}")
        print()

        print(f"{'Cargo':<32}{'Data de admissão'}")
        print(f"{colaborador.cargo:<32}{colaborador.data_admissao}")
        print()

        print(f"{'Tipo de colaborador':<32}{'Regime'}")
        print(f"{tipo:<32}{colaborador.regime}")
        print()

        if colaborador.regime == "PJ":
            vale_transporte_exibicao = "Não se aplica"
        else:
            vale_transporte_exibicao = colaborador.vale_transporte.capitalize()

        print(f"{'Vale-transporte':<32}{'Salário bruto'}")
        print(
            f"{vale_transporte_exibicao:<32}"
            f"{moeda(colaborador.salarioBase)}"
        )

        print("=" * 60)

def editar_colaborador():
    print("\n" + "=" * 48)
    print("          >>> EDITAR COLABORADOR <<<")
    print("=" * 48)

    if not colaboradores:
        print("\nNenhum colaborador cadastrado.")
        return

    print("\n[  MATRÍCULA  ]\n")
    matricula = input("Digite a matrícula do colaborador: ").strip()

    colaborador = buscar_colaborador(matricula)

    if colaborador is None:
        print("\nColaborador não encontrado.")
        return

    print("\n" + "-" * 48)
    print("          DADOS DO COLABORADOR")
    print("-" * 48)

    colaborador.exibirDados()
    print("-" * 48)

    while True:
        print("\n[  OPÇÕES DE EDIÇÃO  ]\n")
        print("1. Nome")
        print("2. Tipo de colaborador")
        print("3. Cargo")
        print("4. Regime de contratação")
        print("5. Vale-transporte")
        print("6. Data de admissão")
        print("0. Cancelar edição")
        print("\n" + "-" * 48)

        campo = input("Escolha uma opção (0 a 6): ").strip()

        if campo == "0":
            print("\nEdição cancelada.")
            return

        elif campo == "1":
            print("\n[  NOME  ]\n")
            nome = input("Novo nome completo: ").strip()

            if nome:
                colaborador.nome = nome
                print("\nNome atualizado com sucesso!")
            else:
                print("\nO nome não pode ficar vazio.")

        elif campo == "2":
            print("\n[  TIPO DE COLABORADOR  ]\n")
            print("1 - Padrão")
            print("2 - Comissionado")
            print("3 - Produção")

            tipo = input("\nEscolha o novo tipo: ").strip()

            if tipo in ("1", "2", "3"):
                indice = colaboradores.index(colaborador)

                novo_colaborador = criar_colaborador(
                    tipo,
                    colaborador.matricula,
                    colaborador.nome,
                    colaborador.cargo,
                    colaborador.regime,
                    colaborador.vale_transporte,
                    colaborador.data_admissao,
                    colaborador.salarioBase
                )

                colaboradores[indice] = novo_colaborador
                colaborador = novo_colaborador

                print("\nTipo atualizado com sucesso!")
            else:
                print("\nTipo inválido.")

        elif campo == "3":
            print("\n[  CARGO  ]\n")

            for numero, nome_cargo in CARGOS.items():
                print(f"{numero} - {nome_cargo}")

            cargo = input("\nEscolha o novo cargo: ").strip()

            if cargo in CARGOS:
                colaborador.cargo = CARGOS[cargo]
                print("\nCargo atualizado com sucesso!")
            else:
                print("\nCargo inválido.")

        elif campo == "4":
            print("\n[  REGIME DE CONTRATAÇÃO  ]\n")
            print("1 - CLT")
            print("2 - PJ")

            regime = input("\nEscolha o novo regime: ").strip()

            if regime == "1":
                colaborador.regime = "CLT"
                print("\nRegime atualizado para CLT.")

                print("\n[  VALE-TRANSPORTE  ]\n")
                resposta = ler_sim_nao(
                    "Recebe vale-transporte? (Sim/Não): "
                )
                colaborador.vale_transporte = resposta

            elif regime == "2":
                colaborador.regime = "PJ"
                colaborador.vale_transporte = "NÃO SE APLICA"
                print("\nRegime atualizado para PJ.")
                print("Vale-transporte: Não se aplica.")
            else:
                print("\nRegime inválido.")

        elif campo == "5":
            if colaborador.regime == "PJ":
                print("\nVale-transporte não se aplica ao regime PJ.")
                continue

            print("\n[  VALE-TRANSPORTE  ]\n")
            colaborador.vale_transporte = ler_sim_nao(
                "Recebe vale-transporte? (Sim/Não): "
            )
            print("\nVale-transporte atualizado com sucesso!")

        elif campo == "6":
            print("\n[  DATA DE ADMISSÃO  ]\n")
            data = input("Nova data (DD/MM/AAAA): ").strip()

            while True:
                try:
                    datetime.strptime(data, "%d/%m/%Y")
                    break
                except ValueError:
                    print("Data inválida. Digite no formato DD/MM/AAAA.")
                    data = input("Nova data (DD/MM/AAAA): ").strip()

            colaborador.data_admissao = data
            print("\nData de admissão atualizada com sucesso!")

        else:
            print("\nOpção inválida.")

        print("\n" + "-" * 48)

        continuar = ler_sim_nao(
            "Deseja editar outra informação? (Sim/Não): "
        )

        if continuar != "SIM":
            print("\nEdição finalizada com sucesso!")
            break

def excluir_colaborador():
    print("\n" + "=" * 48)
    print("          >>> EXCLUIR COLABORADOR <<<")
    print("=" * 48)

    if not colaboradores:
        print("\nNenhum colaborador cadastrado.")
        return

    print("\n[  MATRÍCULA  ]\n")
    matricula = input("Digite a matrícula do colaborador: ").strip()

    colaborador = buscar_colaborador(matricula)

    if colaborador is None:
        print("\nColaborador não encontrado.")
        return

    print("\n" + "-" * 48)
    print("          DADOS DO COLABORADOR")
    print("-" * 48)

    print(f"Nome: {colaborador.nome}")
    print(f"Matrícula: {colaborador.matricula}")
    print(f"Cargo: {colaborador.cargo}")
    print("-" * 48)

    print("\nTem certeza que deseja excluir este colaborador?")

    confirmacao = ler_sim_nao("Confirma a exclusão? (Sim/Não): ")

    if confirmacao == "SIM":
        colaboradores.remove(colaborador)

        print("\n" + "=" * 48)
        print("       COLABORADOR EXCLUÍDO COM SUCESSO")
        print("=" * 48)
    else:
        print("\nExclusão cancelada.")

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
        relatorio_geral()
    elif opcao_relatorio == "2":
        relatorio_por_cargo()


def relatorio_geral():
    print("\n" + "=" * 60)
    print("                 RELATÓRIO GERAL")
    print("=" * 60)

    if not colaboradores:
        print("\nNenhum colaborador cadastrado para exibir.")
        return

    total_salarios_base = sum(
        colaborador.salarioBase for colaborador in colaboradores
    )

    total_clt = sum(
        1 for colaborador in colaboradores
        if colaborador.regime == "CLT"
    )

    total_pj = sum(
        1 for colaborador in colaboradores
        if colaborador.regime == "PJ"
    )

    print(f"\nTotal de colaboradores: {len(colaboradores)}")
    print()
    print(f"Colaboradores CLT: {total_clt}")
    print()
    print(f"Colaboradores PJ: {total_pj}")
    print()
    print(f"Total dos salários-base: {moeda(total_salarios_base)}")

    print("\n" + "-" * 60)
    print("COLABORADORES CADASTRADOS")
    print("-" * 60)

    for indice, colaborador in enumerate(colaboradores, start=1):
        tipo = obter_tipo_colaborador(colaborador)

        print(f"\n{indice}. {colaborador.nome}")
        print(f"   Matrícula: {colaborador.matricula}")
        print(f"   Cargo: {colaborador.cargo}")
        print(f"   Tipo: {tipo}")
        print(f"   Regime: {colaborador.regime}")
        print(
            f"   Vale-transporte: "
            f"{colaborador.vale_transporte.capitalize()}"
        )
        print(f"   Data de admissão: {colaborador.data_admissao}")
        print(f"   Salário-base: {moeda(colaborador.salarioBase)}")

    print("\n" + "=" * 60)


def relatorio_por_cargo():
    print("\n" + "=" * 60)
    print("               RELATÓRIO POR CARGO")
    print("=" * 60)

    if not colaboradores:
        print("\nNenhum colaborador cadastrado para exibir.")
        return

    cargos = {}

    for colaborador in colaboradores:
        cargo = colaborador.cargo
        cargos.setdefault(cargo, []).append(colaborador)

    total_salarios_base = sum(
        colaborador.salarioBase for colaborador in colaboradores
    )

    for cargo in sorted(cargos):
        lista = cargos[cargo]

        soma_salarios = sum(
            colaborador.salarioBase for colaborador in lista
        )

        print("\n" + "-" * 60)
        print(cargo.upper())
        print("-" * 60)
        print(f"Quantidade de colaboradores: {len(lista)}")
        print()
        print(f"Total dos salários-base do cargo: {moeda(soma_salarios)}")
        print()
        print("Colaboradores:")

        for colaborador in lista:
            print(
                f"  - {colaborador.nome} "
                f"(matrícula {colaborador.matricula}) — "
                f"{colaborador.regime} — "
                f"salário-base {moeda(colaborador.salarioBase)}"
            )

    print("\n" + "-" * 60)
    print(f"Total de colaboradores: {len(colaboradores)}")
    print(f"Total dos salários-base: {moeda(total_salarios_base)}")
    print("=" * 60)


if __name__ == "__main__":
    main()