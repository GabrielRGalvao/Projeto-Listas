
import os

def adicionar_tarefa(tarefas, fazercompras, supermercado, urgente, compra_do_mes):
    tarefa = {
        'nome': fazercompras,
        'descricao': supermercado,
        'prioridade': urgente ,
        'categoria': compra_do_mes,
        'concluida': False
    }
    tarefas.append(tarefa)

def listar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa encontrada.")
    else:
        for idx, tarefa in enumerate(tarefas):
            print(f"{idx+1}. {tarefa['nome']} - {tarefa['descricao']} - Prioridade: {tarefa['prioridade']} - Categoria: {tarefa['categoria']} - Concluída: {tarefa['concluida']}")

def marcar_concluida(tarefas, indice):
    if 1 <= indice <= len(tarefas):
        tarefas[indice - 1]['concluida'] = True
        print("Tarefa marcada como concluída.")
    else:
        print("Índice inválido.")

def exibir_por_prioridade(tarefas, prioridade):
    print(f"Tarefas com prioridade {prioridade}:")
    for tarefa in tarefas:
        if tarefa['prioridade'] == prioridade:
            print(f"- {tarefa['nome']}")

def exibir_por_categoria(tarefas, categoria):
    print(f"Tarefas na categoria {categoria}:")
    for tarefa in tarefas:
        if tarefa['categoria'] == categoria:
            print(f"- {tarefa['nome']}")


def menu():
    tarefas = []
    while True:
        print("\n==== Menu ====")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Marcar Tarefa como Concluída")
        print("4. Exibir Tarefas por Prioridade")
        print("5. Exibir Tarefas por Categoria")
        print("6. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Nome da tarefa: ")
            descricao = input("Descrição da tarefa: ")
            prioridade = input("Prioridade da tarefa: ")
            categoria = input("Categoria da tarefa: ")
            adicionar_tarefa(tarefas, nome, descricao, prioridade, categoria)
        elif opcao == '2':
            listar_tarefas(tarefas)
        elif opcao == '3':
            listar_tarefas(tarefas)
            indice = int(input("Informe o índice da tarefa concluída: "))
            marcar_concluida(tarefas, indice)
        elif opcao == '4':
            prioridade = input("Informe a prioridade: ")
            exibir_por_prioridade(tarefas, prioridade)
        elif opcao == '5':
            categoria = input("Informe a categoria: ")
            exibir_por_categoria(tarefas, categoria)
        elif opcao == '6':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()