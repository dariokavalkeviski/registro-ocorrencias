4# ============================================================
#  SISTEMA DE REGISTRO DE OCORRÊNCIAS
#  Desenvolvido por: Dario Kavalkeviski
#  Descrição: Simula o registro de ocorrências policiais,
#  permitindo cadastrar, listar, buscar e salvar em arquivo CSV.
# ============================================================

import csv                    # Biblioteca para ler e salvar arquivos CSV
import os                     # Biblioteca para verificar se arquivo existe
from datetime import datetime # Biblioteca para pegar data e hora atual

# Nome do arquivo onde as ocorrências serão salvas
ARQUIVO = "ocorrencias.csv"

# Cabeçalho das colunas do arquivo CSV
CABECALHO = ["ID", "Data", "Hora", "Tipo", "Local", "Descrição", "Status"]


# ------------------------------------------------------------
# FUNÇÃO: Carregar ocorrências salvas no arquivo CSV
# ------------------------------------------------------------
def carregar_ocorrencias():
    ocorrencias = []  # Lista vazia que vai receber os dados

    # Verifica se o arquivo já existe antes de tentar abrir
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, mode="r", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)  # Lê o CSV como dicionário
            for linha in leitor:
                ocorrencias.append(linha)     # Adiciona cada linha na lista

    return ocorrencias


# ------------------------------------------------------------
# FUNÇÃO: Salvar todas as ocorrências no arquivo CSV
# ------------------------------------------------------------
def salvar_ocorrencias(ocorrencias):
    with open(ARQUIVO, mode="w", encoding="utf-8", newline="") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=CABECALHO)
        escritor.writeheader()         # Escreve o cabeçalho (primeira linha)
        escritor.writerows(ocorrencias) # Escreve todas as ocorrências


# ------------------------------------------------------------
# FUNÇÃO: Registrar uma nova ocorrência
# ------------------------------------------------------------
def registrar_ocorrencia(ocorrencias):
    print("\n--- REGISTRAR NOVA OCORRÊNCIA ---")

    # Gera ID automático baseado na quantidade de ocorrências existentes
    novo_id = len(ocorrencias) + 1

    # Captura data e hora atual automaticamente
    agora = datetime.now()
    data = agora.strftime("%d/%m/%Y")  # Formato: dia/mês/ano
    hora = agora.strftime("%H:%M")     # Formato: hora:minuto

    # Tipos de ocorrência disponíveis
    tipos = {
        "1": "Furto",
        "2": "Roubo",
        "3": "Perturbação do sossego",
        "4": "Violência doméstica",
        "5": "Acidente de trânsito",
        "6": "Outros"
    }

    print("\nTipos de ocorrência:")
    for chave, valor in tipos.items():
        print(f"  {chave} - {valor}")

    escolha = input("\nEscolha o tipo (1-6): ").strip()
    tipo = tipos.get(escolha, "Outros")  # Se digitar errado, usa "Outros"

    local = input("Local da ocorrência (ex: Rua das Flores, 123): ").strip()
    descricao = input("Descrição resumida: ").strip()

    # Monta o dicionário com os dados da nova ocorrência
    nova_ocorrencia = {
        "ID": novo_id,
        "Data": data,
        "Hora": hora,
        "Tipo": tipo,
        "Local": local,
        "Descrição": descricao,
        "Status": "Aberta"
    }

    ocorrencias.append(nova_ocorrencia)  # Adiciona na lista
    salvar_ocorrencias(ocorrencias)      # Salva no arquivo

    print(f"\n✅ Ocorrência nº {novo_id} registrada com sucesso!")


# ------------------------------------------------------------
# FUNÇÃO: Listar todas as ocorrências
# ------------------------------------------------------------
def listar_ocorrencias(ocorrencias):
    print("\n--- LISTA DE OCORRÊNCIAS ---")

    if len(ocorrencias) == 0:
        print("Nenhuma ocorrência registrada ainda.")
        return

    for oc in ocorrencias:
        print(f"\n🔹 Ocorrência nº {oc['ID']}")
        print(f"   Data/Hora : {oc['Data']} às {oc['Hora']}")
        print(f"   Tipo      : {oc['Tipo']}")
        print(f"   Local     : {oc['Local']}")
        print(f"   Descrição : {oc['Descrição']}")
        print(f"   Status    : {oc['Status']}")

    print(f"\nTotal: {len(ocorrencias)} ocorrência(s) registrada(s).")


# ------------------------------------------------------------
# FUNÇÃO: Buscar ocorrências por tipo ou local
# ------------------------------------------------------------
def buscar_ocorrencias(ocorrencias):
    print("\n--- BUSCAR OCORRÊNCIAS ---")
    print("1 - Buscar por tipo")
    print("2 - Buscar por local")

    opcao = input("\nEscolha (1 ou 2): ").strip()

    if opcao == "1":
        termo = input("Digite o tipo (ex: Furto, Roubo): ").strip().lower()
        # Filtra ocorrências onde o tipo contém o termo digitado
        resultados = [oc for oc in ocorrencias if termo in oc["Tipo"].lower()]

    elif opcao == "2":
        termo = input("Digite parte do local (ex: Rua, Centro): ").strip().lower()
        # Filtra ocorrências onde o local contém o termo digitado
        resultados = [oc for oc in ocorrencias if termo in oc["Local"].lower()]

    else:
        print("Opção inválida.")
        return

    # Mostra os resultados encontrados
    if len(resultados) == 0:
        print("\nNenhuma ocorrência encontrada para essa busca.")
    else:
        print(f"\n{len(resultados)} ocorrência(s) encontrada(s):\n")
        for oc in resultados:
            print(f"  🔹 Nº {oc['ID']} | {oc['Data']} | {oc['Tipo']} | {oc['Local']}")


# ------------------------------------------------------------
# FUNÇÃO: Encerrar uma ocorrência (mudar status para Fechada)
# ------------------------------------------------------------
def encerrar_ocorrencia(ocorrencias):
    print("\n--- ENCERRAR OCORRÊNCIA ---")

    numero = input("Digite o número da ocorrência a encerrar: ").strip()

    encontrada = False
    for oc in ocorrencias:
        if str(oc["ID"]) == numero:
            if oc["Status"] == "Fechada":
                print("⚠️  Essa ocorrência já está encerrada.")
            else:
                oc["Status"] = "Fechada"
                salvar_ocorrencias(ocorrencias)
                print(f"✅ Ocorrência nº {numero} encerrada com sucesso!")
            encontrada = True
            break

    if not encontrada:
        print("❌ Ocorrência não encontrada.")


# ------------------------------------------------------------
# MENU PRINCIPAL
# ------------------------------------------------------------
def menu():
    print("\n" + "=" * 40)
    print("   SISTEMA DE REGISTRO DE OCORRÊNCIAS")
    print("=" * 40)
    print("  1 - Registrar nova ocorrência")
    print("  2 - Listar todas as ocorrências")
    print("  3 - Buscar ocorrência")
    print("  4 - Encerrar ocorrência")
    print("  5 - Sair")
    print("=" * 40)

    return input("  Escolha uma opção: ").strip()


# ------------------------------------------------------------
# INÍCIO DO PROGRAMA
# ------------------------------------------------------------
def main():
    print("\nBem-vindo ao Sistema de Registro de Ocorrências!")

    ocorrencias = carregar_ocorrencias()  # Carrega dados existentes ao iniciar

    while True:  # Loop que mantém o menu rodando até o usuário sair
        opcao = menu()

        if opcao == "1":
            registrar_ocorrencia(ocorrencias)
        elif opcao == "2":
            listar_ocorrencias(ocorrencias)
        elif opcao == "3":
            buscar_ocorrencias(ocorrencias)
        elif opcao == "4":
            encerrar_ocorrencia(ocorrencias)
        elif opcao == "5":
            print("\nSaindo do sistema. Até logo!\n")
            break  # Encerra o loop e fecha o programa
        else:
            print("\n⚠️  Opção inválida. Tente novamente.")


# Garante que o programa só roda quando executado diretamente
if __name__ == "__main__":
    main()
