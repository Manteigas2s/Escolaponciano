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

# ── Utilitário ──────────────────────────────────────────────

SEPARADOR = "=" * 44

def linha():
    print(SEPARADOR)

def cabecalho(titulo: str):
    """Exibe um cabeçalho padronizado."""
    print(f"\n{SEPARADOR}")
    print(f"  {titulo.upper()}")
    print(SEPARADOR)

# ── Validação ──────────────────────────────────────────────

def cpf_exist(cpf):
    for dados in alunos:
        if dados["cpf"]==cpf:
            return True
    return False

# ── Funções principais ───────────────────────────────────────

def cadastro_alunos():
    cabecalho("Cadastro de Novo Aluno")

    # Nome
    while True:
        nome = input("\n  Nome: ").strip()
        if not nome:
            print(" O nome não pode estar vazio.")
        elif not nome.replace(" ", "").isalpha():
            print(" Nome inválido. Use apenas letras.")
        else:
            break

    
    # CPF
    while True:
        cpf = input("  CPF (somente números): ").strip()
        if not cpf:
            print(" CPF não pode estar vazio.")
        elif len(cpf) != 11:
            print(" CPF deve ter exatamente 11 dígitos.")
        elif not cpf.isdigit():
            print(" CPF deve conter apenas números.")
        elif cpf_exist(cpf):
            print(" CPF já cadastrado.")
        else:
            break
    
    # Idade
    while True:
        try:
            idade = int(input("  Idade: ").strip())
            if idade <= 0:
                print(" Idade deve ser maior que zero.")
            else:
                break
        except ValueError:
            print(" Digite apenas números. ")
    
    # Adicionando Alunos a Lista     
    global ultima_matricula
    ultima_matricula += 1
    novo_aluno = {
        "nome": nome,
        "cpf": cpf,
        "idade": idade,
        "matricula": str (ultima_matricula) 
                 }
    alunos.append(novo_aluno)
    print(f"\n  Aluno '{nome}' cadastrado! Matrícula: {ultima_matricula}\n")

def ver_alunos():
    print("LISTA DE ALUNOS")
    contador = 1
    for aluno in alunos:
        print(f"{contador}. {aluno['nome']} - {aluno['cpf']}- {aluno['idade']}- {aluno['matricula']}")
        contador += 1

def escolher_alunos():
    while True:
        try:
            num = int(input("Digite o número do aluno: ")).strip()

            if num <1 or num > len(alunos):
                print("DIGITE UM NÚMERO VÁLIDO")
                continue
            else:
                print("ALUNO ENCONTRADO!")
                return num
        except:

            print("DIGITE APENAS NÚMEROS")

def alterar_alunos():
    ver_alunos()

    num_alunos = escolher_alunos()

    alunos_escolhido = alunos[num_alunos-1]
    
    print(f"""
    INFORMAÇÕES DO ALUNO:
          
    Nome: {alunos_escolhido["nome"]}
    CPF: {"*"*8}{alunos_escolhido['cpf'][8::]}
    Idade: {alunos_escolhido['idade']}
    Matricula: {alunos_escolhido['matricula']}
          """)
    
    novo_nome = input(f"Digite o novo nome ({alunos_escolhido["nome"]}): ")
    
    if novo_nome:
        alunos_escolhido["nome"] = novo_nome

    novo_cpf = input(f"Digite o novo cpf: ")
    if novo_cpf:
        alunos_escolhido["cpf"] = novo_cpf

    nova_idade = input(f"Digite a nova idade: ")
    if nova_idade:
        alunos_escolhido["idade"] = int(nova_idade)

    nova_matricula = input(f"Digite a nova matricula: ")
    if nova_matricula:
        alunos_escolhido["matricula"] = nova_matricula

    print(f"""
    INFORMAÇÕES DO ALUNO:
          
    Nome: {alunos_escolhido["nome"]}
    CPF: {"*"*8}{alunos_escolhido['cpf'][8::]}
    Idade:  {alunos_escolhido['idade']}
    Matricula: {alunos_escolhido['matricula']}
          """)

def remover_alunos():

    ver_alunos()

    num_alunos = escolher_alunos()
    
    aluno_removido = alunos.pop(num_alunos-1)

    print(f"{aluno_removido["nome"]} foi expulso!")

def ver_situacao_alunos():
    while True:
        print("""
========================================
      SITUAÇÃO DOS ALUNOS
========================================

    1. Ver alunos Ativos
    2. Ver alunos Suspensos
    3. Ver alunos com Advertência
    4. Ver alunos Inativos
    5. Ver alunos Expulsos

    0. Voltar ao menu principal
========================================
""")
        op_situacao = input("Digite o número do menu: ")
        situacao = "ativo"
        if op_situacao == "1":
            situacao = "ativo"
        elif op_situacao == "2":
            situacao = "suspenso"
        elif op_situacao == "3":
            situacao = "advertencia"
        elif op_situacao == "4":
            situacao = "inativo"
        elif op_situacao == "5":
            situacao = "expulso"
        elif op_situacao == "0":
            break
        else:
            print("Não identificado")
            continue
        contador = 1
        for aluno in alunos:
            if aluno["situacao"] == situacao:
                print(f"{contador}. {aluno['nome']} - {aluno['cpf']}- {aluno['idade']}- {aluno['matricula']}- {aluno['situacao']}")
                contador += 1

def ver_aluno_matricula():
        ver_alunos()
        matricula = input("Digite a matrícula do aluno: ")

        for aluno in alunos:
            if aluno["matricula"] == matricula:
                print("\nAluno encontrado:")
                print(f"Nome: {aluno['nome']}")
                print(f"CPF: {aluno['cpf']}")
                print(f"Idade: {aluno['idade']}")
                print(f"Matrícula: {aluno['matricula']}")
                print(f"Situação: {aluno['situacao']}")
                return

        print("Aluno não encontrado.")

# ── Menu principal ───────────────────────────────────────────

while True:
    print("""
========================================
        BEM VINDO À ESCOLA PONCIANO
========================================

Menu:
========================================
    1. Cadastrar novo Aluno
    2. Ver Alunos
    3. Alterar Aluno
    4. Remover Aluno
    5. Ver situação dos Alunos
    6. Ver Alunos por matrículas

    0. Sair
========================================
""")

    op = input("Digite o número do menu: ")

    if op == "1":
        cadastro_alunos()
    if op == "2":
        ver_alunos()
    if op == "3":
        alterar_alunos()
    if op == "4":
        remover_alunos()
    if op == "5":
        ver_situacao_alunos()
    if op == "6":
        ver_aluno_matricula()