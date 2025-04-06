# Você deve desenvolver uma aplicação simples de console em C# ou Python que execute as seguintes tarefas:
# Cadastro de Usuários: A aplicação deve permitir o cadastro de usuários com as informações: nome, e-mail e idade.
# Os dados devem ser armazenados em uma lista em memória. Listagem de Usuários: Implementar uma funcionalidade que
#  liste todos os usuários cadastrados, exibindo suas informações no console. Busca de Usuário: A aplicação deve permitir
#  a busca de um usuário pelo nome e exibir suas informações, se encontrado. Instruções: O código deve ser claro e bem comentado.
#  Cole no campo de resposta abaixo o código-fonte e, também,
# coloque o link de algum tipo de drive contendo arquivo ZIP com os anexos utilizados.Esta pergunta é obrigatória*
# Lista para armazenar os usuários


# Lista onde serão armazenados os dados dos usuários
cadastro = []

# Solicita ao usuário quantos cadastros deseja realizar
quantidade = int(
    input('Digite a quantidade de usuários que deseja cadastrar: '))

# Loop para cadastrar os usuários
for i in range(quantidade):
    # Coleta os dados do usuário
    nome = input('Digite seu nome: ')
    email = input('Digite seu email: ')
    idade = int(input('Digite sua idade: '))

    # Cria um dicionário com as informações do usuário
    usuario = {
        'nome': nome,
        'email': email,
        'idade': idade
    }

    # Adiciona o dicionário à lista de cadastro
    cadastro.append(usuario)

# Exibe todos os usuários cadastrados
print('\nUsuários cadastrados:')
for usuario in cadastro:
    # Imprime as informações de cada usuário no console
    print(
        f"Nome: {usuario['nome']}, Email: {usuario['email']}, Idade: {usuario['idade']}")

# Solicita o nome do usuário que deseja buscar
buscador = input('\nDigite o nome que deseja buscar: ')

# Variável de controle para saber se o usuário foi encontrado
encontrado = False

# Loop para procurar o usuário pelo nome
for usuario in cadastro:
    # Compara o nome digitado com os nomes cadastrados (ignora letras maiúsculas/minúsculas)
    if usuario['nome'].lower() == buscador.lower():
        print(f"\nUsuário encontrado:")
        print(
            f"Nome: {usuario['nome']}, Email: {usuario['email']}, Idade: {usuario['idade']}")
        encontrado = True  # Marca que encontrou
        break  # Interrompe a busca

# Se nenhum usuário for encontrado, exibe a mensagem
if not encontrado:
    print('Usuário não encontrado.')
