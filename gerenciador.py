def adicionar_tarefa(nome_tarefa):
  if nome_tarefa == "":
    global ids_tarefas
    print("Você precisa digitar um nome para sua tarefa")
  tarefa = {"id": ids_tarefas, "tarefa": nome_tarefa, "completada": False}
  tarefas.append(tarefa)
  print(f"Tarefa {nome_tarefa} foi adicionada com sucesso!")
  ids_tarefas = ids_tarefas + 1
  return

def ver_tarefas(atualizar_tarefa=None):
  if tarefas != []:
    print("Lista de Tarefas")
    for i, tarefa in enumerate(tarefas, start=1):
      status = "✓" if tarefa["completada"] else " "
      nome_tarefa = tarefa["tarefa"]
      print(f"{i}. [{status}] {nome_tarefa}")
    if atualizar_tarefa is not None:
      numero_tarefa = input("Digite o número da tarefa que deseja atualizar as informações: ")
      return numero_tarefa
  else:
    print("Você não possui nenhuma tarefa cadastrada")

def atualizar_tarefas(completar_tarefa=None, deletar_tarefa_completada=None):
  tarefa_escolhida = ver_tarefas(atualizar_tarefa=True)
  for tarefa in tarefas:
      tarefa_nome = tarefa["tarefa"]
      if tarefa["id"] == int(tarefa_escolhida):
        if completar_tarefa:
          tarefa["completada"] = True
          return tarefa_nome
        elif deletar_tarefa_completada:
          tarefas.remove(tarefa)
          return tarefa_nome
        else:
          novo_nome = input("Digite o novo nome da tarefa: ")
          if novo_nome.strip() == "":
            print("O nome da tarefa não pode ser vazio.")
            return
          tarefa["tarefa"] = novo_nome
          print(f"Tarefa escolhida foi atualizada para '{novo_nome}'.")
          return
  print("Não Foi encontrado a tarefa com o número digitado")    
      
def complentar_tarefa():
  tarefa_nome = atualizar_tarefas(completar_tarefa=True)
  print(f"Tarefa escolhida '{tarefa_nome}' foi concluída com sucesso.")
  
def deletar_tarefas_completadas():
  tarefa_nome = atualizar_tarefas(deletar_tarefa_completada=True)
  print(f"Tarefa '{tarefa_nome}' foi deletada com sucesso.")
  
  
ids_tarefas = 1
tarefas = []

while True:
  print("\n Menu do Gerenciador de Lista de Tarefas")
  print("1, Adicionar Tarefas")
  print("2, Ver Tarefas")
  print("3, Atualizar Tarefas")
  print("4, Completar Tarefas")
  print("5, Deletar Tarefas Completadas")
  print("6, Sair")
  
  escolha = input("Digite a sua escolha: ")
  switch = {
            "1": lambda: adicionar_tarefa(input("Digite o nome da tarefa: ")),
            "2": ver_tarefas,
            "3": atualizar_tarefas,
            "4": complentar_tarefa,
            "5": deletar_tarefas_completadas,
            "6": lambda: print("Programa Finalizado")
        }
  func = switch.get(escolha, lambda: print("Escolha inválida"))
  func()
        
  if escolha == "6":
    break
  

  
  
  
  
  