alunos = [
    {"nome": "Maria",   "cpf": "12345678900", "idade": 19, "matricula": "2026001"},
{"nome": "João",     "cpf": "98765432100", "idade": 21, "matricula": "2026002"},
{"nome": "Ana",      "cpf": "11122233301", "idade": 18, "matricula": "2026003"},
{"nome": "Carlos",   "cpf": "11122233302", "idade": 22, "matricula": "2026004"},
{"nome": "Fernanda", "cpf": "11122233303", "idade": 20, "matricula": "2026005"},
{"nome": "Lucas",    "cpf": "11122233304", "idade": 23, "matricula": "2026006"},
{"nome": "Juliana",  "cpf": "11122233305", "idade": 19, "matricula": "2026007"},
{"nome": "Pedro",    "cpf": "11122233306", "idade": 24, "matricula": "2026008"},
{"nome": "Camila",   "cpf": "11122233307", "idade": 21, "matricula": "2026009"},
{"nome": "Rafael",   "cpf": "11122233308", "idade": 20, "matricula": "2026010"},
{"nome": "Patrícia", "cpf": "11122233309", "idade": 22, "matricula": "2026011"},
{"nome": "Bruno",    "cpf": "11122233310", "idade": 18, "matricula": "2026012"},
{"nome": "Larissa",  "cpf": "11122233311", "idade": 19, "matricula": "2026013"},
{"nome": "Diego",    "cpf": "11122233312", "idade": 25, "matricula": "2026014"},
{"nome": "Amanda",   "cpf": "11122233313", "idade": 20, "matricula": "2026015"},
{"nome": "Felipe",   "cpf": "11122233314", "idade": 21, "matricula": "2026016"},
{"nome": "Bianca",   "cpf": "11122233315", "idade": 23, "matricula": "2026017"},
{"nome": "Gustavo",  "cpf": "11122233316", "idade": 22, "matricula": "2026018"},
{"nome": "Renata",   "cpf": "11122233317", "idade": 18, "matricula": "2026019"},
{"nome": "Thiago",   "cpf": "11122233318", "idade": 24, "matricula": "2026020"},
{"nome": "Vanessa",  "cpf": "11122233319", "idade": 20, "matricula": "2026021"},
{"nome": "Eduardo",  "cpf": "11122233320", "idade": 21, "matricula": "2026022"},
]
ultima_matricula = 2026022

def cpf_exist(cpf):
    for dados in alunos:
        if dados["cpf"]==cpf:
            return True
    return False

def cadastro_alunos():
    print("CADASTRO DE ALUNOS")

    while True:
        nome = input("Digite o nome do Aluno: ")
    
        if nome == "":
                print("Preencha o campo nome")
        
        elif not nome.replace(" ", "").isalpha():
                print("Nome inválido")
        else:
            break
    while True:
        cpf = input("Digite o cpf do Aluno: ")
        if cpf =="":
            print("Digite um CPF")
        elif len(cpf) != 11:
            print("""Quantidade de dígitos fora do padrão
                """)
        elif not cpf.isdigit():
            print("Dados inválidos")
        elif cpf_exist(cpf):
            print("CPF já cadastrado. Tente outro número")
        else:
            break
    
    while True:
        try:
            idade = input("Digite a idade do aluno: ")
            idade = int(idade)
            if idade == "":
                print("Preencha o campo idade")
            elif idade < 0:
                 print("Idade deve ser maior que 0")
            else:
                break
            
        except ValueError:
            print("Digite apenas números")
    global ultima_matricula
    ultima_matricula += 1
    novo_aluno = {
        "nome": nome,
        "cpf": cpf,
        "idade": idade,
        "matricula": str (ultima_matricula) 
                 }
    alunos.append(novo_aluno)

def ver_alunos():
    print("LISTA DE ALUNOS")
    contador = 1
    for aluno in alunos:
        print(f"{contador}. {aluno['nome']} - {aluno['cpf']}- {aluno['idade']}- {aluno['matricula']}")
        contador += 1

while True:
    print(f"""
    BEM VINDO A ESCOLA PONCIANO
            
    Menu:
            
            1. Cadastrar novo Aluno
            2. Ver Alunos
            3. Alterar Aluno
            4. Remover Aluno

            0. Sair
    """)
    op = input("Digite o número do menu: ")

    if op == "1":
        cadastro_alunos()
    if op == "2":
        ver_alunos()