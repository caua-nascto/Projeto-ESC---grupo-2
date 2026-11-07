from datetime import datetime


def ler_nome():
    while True:
        nome = input("Nome: ").strip()
        if nome:
            return nome
        print("O nome não pode ficar vazio.")


def ler_data_nascimento():
    while True:
        texto = input("Data de nascimento (dd/mm/aaaa): ").strip()
        try:
            data = datetime.strptime(texto, "%d/%m/%Y")
            if data > datetime.now():
                print("A data não pode estar no futuro.")
                continue
            return data.strftime("%d/%m/%Y")
        except ValueError:
            print("Data inválida. Use o formato dd/mm/aaaa.")


def ler_idade():
    while True:
        texto = input("Idade: ").strip()
        if texto.isdigit() and 0 <= int(texto) <= 150:
            return int(texto)
        print("Idade inválida. Digite um número inteiro.")
