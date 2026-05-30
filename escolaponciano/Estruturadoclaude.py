# ============================================================
#                    ESCOLA PONCIANO
#              Sistema de Gestão de Alunos v1.0
# ============================================================

# ── Dados iniciais ───────────────────────────────────────────

alunos = [
    {"nome": "Maria",    "cpf": "12345678900", "idade": 19, "matricula": "2026001", "situacao": "ativo"},
    {"nome": "João",     "cpf": "98765432100", "idade": 21, "matricula": "2026002", "situacao": "advertencia"},
    {"nome": "Ana",      "cpf": "11122233301", "idade": 18, "matricula": "2026003", "situacao": "ativo"},
    {"nome": "Carlos",   "cpf": "11122233302", "idade": 22, "matricula": "2026004", "situacao": "suspenso"},
    {"nome": "Fernanda", "cpf": "11122233303", "idade": 20, "matricula": "2026005", "situacao": "ativo"},
    {"nome": "Lucas",    "cpf": "11122233304", "idade": 23, "matricula": "2026006", "situacao": "inativo"},
    {"nome": "Juliana",  "cpf": "11122233305", "idade": 19, "matricula": "2026007", "situacao": "ativo"},
    {"nome": "Pedro",    "cpf": "11122233306", "idade": 24, "matricula": "2026008", "situacao": "expulso"},
    {"nome": "Camila",   "cpf": "11122233307", "idade": 21, "matricula": "2026009", "situacao": "ativo"},
    {"nome": "Rafael",   "cpf": "11122233308", "idade": 20, "matricula": "2026010", "situacao": "advertencia"},
    {"nome": "Patrícia", "cpf": "11122233309", "idade": 22, "matricula": "2026011", "situacao": "ativo"},
    {"nome": "Bruno",    "cpf": "11122233310", "idade": 18, "matricula": "2026012", "situacao": "suspenso"},
    {"nome": "Larissa",  "cpf": "11122233311", "idade": 19, "matricula": "2026013", "situacao": "ativo"},
    {"nome": "Diego",    "cpf": "11122233312", "idade": 25, "matricula": "2026014", "situacao": "inativo"},
    {"nome": "Amanda",   "cpf": "11122233313", "idade": 20, "matricula": "2026015", "situacao": "ativo"},
    {"nome": "Felipe",   "cpf": "11122233314", "idade": 21, "matricula": "2026016", "situacao": "advertencia"},
    {"nome": "Bianca",   "cpf": "11122233315", "idade": 23, "matricula": "2026017", "situacao": "ativo"},
    {"nome": "Gustavo",  "cpf": "11122233316", "idade": 22, "matricula": "2026018", "situacao": "suspenso"},
    {"nome": "Renata",   "cpf": "11122233317", "idade": 18, "matricula": "2026019", "situacao": "ativo"},
    {"nome": "Thiago",   "cpf": "11122233318", "idade": 24, "matricula": "2026020", "situacao": "expulso"},
    {"nome": "Vanessa",  "cpf": "11122233319", "idade": 20, "matricula": "2026021", "situacao": "ativo"},
    {"nome": "Eduardo",  "cpf": "11122233320", "idade": 21, "matricula": "2026022", "situacao": "inativo"},
]

ultima_matricula = 2026022


# ── Utilitários ──────────────────────────────────────────────

SEPARADOR = "=" * 44

def linha():
    print(SEPARADOR)

def cabecalho(titulo: str):
    """Exibe um cabeçalho padronizado."""
    print(f"\n{SEPARADOR}")
    print(f"  {titulo.upper()}")
    print(SEPARADOR)

def cpf_ja_existe(cpf: str) -> bool:
    """Verifica se o CPF já está cadastrado."""
    return any(aluno["cpf"] == cpf for aluno in alunos)

def cpf_mascarado(cpf: str) -> str:
    """Retorna CPF com os 8 primeiros dígitos mascarados."""
    return f"{'*' * 8}{cpf[8:]}"

def exibir_aluno(aluno: dict, numero: int = None, mostrar_situacao: bool = False):
    """Formata e imprime as informações de um aluno na listagem."""
    prefixo = f"{numero:>2}. " if numero else "    "
    situacao = f" | {aluno['situacao'].capitalize()}" if mostrar_situacao else ""
    print(
        f"{prefixo}{aluno['nome']:<12} "
        f"CPF: {cpf_mascarado(aluno['cpf'])}  "
        f"Idade: {aluno['idade']:>2}  "
        f"Matrícula: {aluno['matricula']}"
        f"{situacao}"
    )


# ── Funções principais ───────────────────────────────────────

def cadastrar_aluno():
    """Cadastra um novo aluno com validações de entrada."""
    cabecalho("Cadastro de Novo Aluno")

    # Nome
    while True:
        nome = input("\n  Nome: ").strip()
        if not nome:
            print("  ⚠  O nome não pode estar vazio.")
        elif not nome.replace(" ", "").isalpha():
            print("  ⚠  Nome inválido. Use apenas letras.")
        else:
            break

    # CPF
    while True:
        cpf = input("  CPF (somente números): ").strip()
        if not cpf:
            print("  ⚠  CPF não pode estar vazio.")
        elif len(cpf) != 11:
            print("  ⚠  CPF deve ter exatamente 11 dígitos.")
        elif not cpf.isdigit():
            print("  ⚠  CPF deve conter apenas números.")
        elif cpf_ja_existe(cpf):
            print("  ⚠  CPF já cadastrado.")
        else:
            break

    # Idade
    while True:
        try:
            idade = int(input("  Idade: ").strip())
            if idade <= 0:
                print("  ⚠  Idade deve ser maior que zero.")
            else:
                break
        except ValueError:
            print("  ⚠  Digite apenas números.")

    global ultima_matricula
    ultima_matricula += 1

    novo_aluno = {
        "nome": nome,
        "cpf": cpf,
        "idade": idade,
        "matricula": str(ultima_matricula),
        "situacao": "ativo",
    }
    alunos.append(novo_aluno)

    print(f"\n  ✔  Aluno '{nome}' cadastrado! Matrícula: {ultima_matricula}\n")


def listar_alunos(mostrar_situacao: bool = False):
    """Lista todos os alunos cadastrados."""
    cabecalho("Lista de Alunos")
    if not alunos:
        print("  Nenhum aluno cadastrado.\n")
        return
    for i, aluno in enumerate(alunos, start=1):
        exibir_aluno(aluno, numero=i, mostrar_situacao=mostrar_situacao)
    print()


def selecionar_aluno() -> int:
    """Solicita e valida a escolha de um aluno pelo número da lista."""
    while True:
        try:
            numero = int(input("  Digite o número do aluno: "))
            if 1 <= numero <= len(alunos):
                return numero
            print(f"  ⚠  Digite um número entre 1 e {len(alunos)}.")
        except ValueError:
            print("  ⚠  Digite apenas números.")


def alterar_aluno():
    """Permite editar os dados de um aluno existente."""
    listar_alunos()
    numero = selecionar_aluno()
    aluno = alunos[numero - 1]

    cabecalho(f"Editando: {aluno['nome']}")
    print(f"  Deixe em branco para manter o valor atual.\n")

    novo_nome = input(f"  Nome [{aluno['nome']}]: ").strip()
    if novo_nome:
        aluno["nome"] = novo_nome

    novo_cpf = input(f"  CPF [{cpf_mascarado(aluno['cpf'])}]: ").strip()
    if novo_cpf:
        if len(novo_cpf) == 11 and novo_cpf.isdigit() and not cpf_ja_existe(novo_cpf):
            aluno["cpf"] = novo_cpf
        else:
            print("  ⚠  CPF inválido ou já existente. Campo não alterado.")

    nova_idade = input(f"  Idade [{aluno['idade']}]: ").strip()
    if nova_idade:
        try:
            aluno["idade"] = int(nova_idade)
        except ValueError:
            print("  ⚠  Idade inválida. Campo não alterado.")

    nova_matricula = input(f"  Matrícula [{aluno['matricula']}]: ").strip()
    if nova_matricula:
        aluno["matricula"] = nova_matricula

    print(f"\n  ✔  Dados de '{aluno['nome']}' atualizados!\n")


def remover_aluno():
    """Remove um aluno da lista após confirmação."""
    listar_alunos()
    numero = selecionar_aluno()
    aluno = alunos[numero - 1]

    confirmacao = input(f"\n  Remover '{aluno['nome']}'? (s/n): ").strip().lower()
    if confirmacao == "s":
        alunos.pop(numero - 1)
        print(f"\n  ✔  '{aluno['nome']}' foi removido do sistema.\n")
    else:
        print("  Operação cancelada.\n")


def ver_situacao_alunos():
    """Submenu para filtrar alunos por situação."""
    opcoes_situacao = {
        "1": ("ativo",       "Ativos"),
        "2": ("suspenso",    "Suspensos"),
        "3": ("advertencia", "Com Advertência"),
        "4": ("inativo",     "Inativos"),
        "5": ("expulso",     "Expulsos"),
    }

    while True:
        cabecalho("Situação dos Alunos")
        for chave, (_, rotulo) in opcoes_situacao.items():
            print(f"  {chave}. {rotulo}")
        print(f"  0. Voltar")
        linha()

        opcao = input("\n  Opção: ").strip()

        if opcao == "0":
            break
        elif opcao in opcoes_situacao:
            situacao, rotulo = opcoes_situacao[opcao]
            filtrados = [a for a in alunos if a["situacao"] == situacao]
            cabecalho(f"Alunos {rotulo}")
            if filtrados:
                for i, aluno in enumerate(filtrados, start=1):
                    exibir_aluno(aluno, numero=i)
            else:
                print(f"  Nenhum aluno com situação '{rotulo}'.")
            print()
        else:
            print("  ⚠  Opção inválida.\n")


def buscar_por_matricula():
    """Busca e exibe os dados completos de um aluno pela matrícula."""
    cabecalho("Busca por Matrícula")
    matricula = input("  Matrícula: ").strip()

    for aluno in alunos:
        if aluno["matricula"] == matricula:
            print(f"""
  ┌─ Aluno encontrado ──────────────────┐
  │  Nome:      {aluno['nome']:<27}│
  │  CPF:       {cpf_mascarado(aluno['cpf']):<27}│
  │  Idade:     {aluno['idade']:<27}│
  │  Matrícula: {aluno['matricula']:<27}│
  │  Situação:  {aluno['situacao'].capitalize():<27}│
  └─────────────────────────────────────┘
""")
            return

    print("  ⚠  Aluno não encontrado.\n")


# ── Menu principal ───────────────────────────────────────────

MENU_PRINCIPAL = """
{sep}
        ESCOLA PONCIANO
     Sistema de Gestão de Alunos
{sep}
  1. Cadastrar novo Aluno
  2. Ver Alunos
  3. Alterar Aluno
  4. Remover Aluno
  5. Ver Situação dos Alunos
  6. Buscar por Matrícula
  0. Sair
{sep}"""

ACOES = {
    "1": cadastrar_aluno,
    "2": listar_alunos,
    "3": alterar_aluno,
    "4": remover_aluno,
    "5": ver_situacao_alunos,
    "6": buscar_por_matricula,
}

def main():
    while True:
        print(MENU_PRINCIPAL.format(sep=SEPARADOR))
        opcao = input("  Opção: ").strip()

        if opcao == "0":
            print("\n  Até logo!\n")
            break
        elif opcao in ACOES:
            ACOES[opcao]()
        else:
            print("  ⚠  Opção inválida. Tente novamente.\n")


if __name__ == "__main__":
    main()