from src.entrada import ler_nome, ler_data_nascimento, ler_idade
from src.saida import exibir_dados


def main():
    print("=== Cadastro básico ===\n")
    nome = ler_nome()
    data_nascimento = ler_data_nascimento()
    idade = ler_idade()
    exibir_dados(nome, data_nascimento, idade)


if __name__ == "__main__":
    main()
