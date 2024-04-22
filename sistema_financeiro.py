# Rafael Valnásio Santos Silva
# Atividade de Avaliação - Lógica de Programação
# Curso de Análise e Desenvolvimento de Sistemas
# Centro Universitário Nobre - UNIFAN

# Importando a classe date do módulo datetime para trabalhar com datas
from datetime import date

# Definição das classes para contas a pagar e a receber
class Conta:
    def __init__(self, valor, descricao):
        self.valor = valor
        self.descricao = descricao

class ContaPagar(Conta):
    def __init__(self, valor, descricao, data_vencimento):
        super().__init__(valor, descricao)
        self.data_vencimento = data_vencimento

class ContaReceber(Conta):
    def __init__(self, valor, descricao, data_prevista_recebimento):
        super().__init__(valor, descricao)
        self.data_prevista_recebimento = data_prevista_recebimento

# Classe principal que controla o sistema financeiro
class SistemaFinanceiro:
    def __init__(self):
        # Listas para armazenar contas a pagar e a receber
        self.contas_a_pagar = []
        self.contas_a_receber = []

    # Método para registrar uma nova conta a pagar
    def registrar_conta_pagar(self, valor, descricao, data_vencimento):
        conta_pagar = ContaPagar(valor, descricao, data_vencimento)
        self.contas_a_pagar.append(conta_pagar)

    # Método para registrar uma nova conta a receber
    def registrar_conta_receber(self, valor, descricao, data_prevista_recebimento):
        conta_receber = ContaReceber(valor, descricao, data_prevista_recebimento)
        self.contas_a_receber.append(conta_receber)

    # Método para visualizar as contas a pagar
    def visualizar_contas_a_pagar(self):
        print("Contas a Pagar:")
        for conta in self.contas_a_pagar:
            print(f"Valor: R${conta.valor}, Data de Vencimento: {conta.data_vencimento}, Descrição: {conta.descricao}")

    # Método para visualizar as contas a receber
    def visualizar_contas_a_receber(self):
        print("Contas a Receber:")
        for conta in self.contas_a_receber:
            print(f"Valor: R${conta.valor}, Data Prevista de Recebimento: {conta.data_prevista_recebimento}, Descrição: {conta.descricao}")

    # Método para calcular o saldo atual da empresa
    def calcular_saldo_atual(self):
        saldo_total = 0
        for conta_pagar in self.contas_a_pagar:
            saldo_total -= conta_pagar.valor
        for conta_receber in self.contas_a_receber:
            saldo_total += conta_receber.valor
        return saldo_total

# Função para exibir o menu e interagir com o usuário
def exibir_menu():
    print("\n=== Sistema Financeiro ===")
    print("1. Registrar Conta a Pagar")
    print("2. Registrar Conta a Receber")
    print("3. Visualizar Contas a Pagar")
    print("4. Visualizar Contas a Receber")
    print("5. Calcular Saldo Atual")
    print("6. Sair")

# Instanciando o sistema financeiro
sistema = SistemaFinanceiro()

# Loop principal do programa
while True:
    # Exibindo o menu
    exibir_menu()
    # Obtendo a escolha do usuário
    opcao = input("Escolha uma opção: ")

    # Realizando ações de acordo com a escolha do usuário
    if opcao == "1":
        valor = float(input("Informe o valor da conta a pagar: "))
        descricao = input("Informe a descrição da conta a pagar: ")
        data_vencimento = input("Informe a data de vencimento (dd/mm/aaaa): ")
        sistema.registrar_conta_pagar(valor, descricao, data_vencimento)
    elif opcao == "2":
        valor = float(input("Informe o valor da conta a receber: "))
        descricao = input("Informe a descrição da conta a receber: ")
        data_prevista_recebimento = input("Informe a data prevista de recebimento (dd/mm/aaaa): ")
        sistema.registrar_conta_receber(valor, descricao, data_prevista_recebimento)
    elif opcao == "3":
        sistema.visualizar_contas_a_pagar()
    elif opcao == "4":
        sistema.visualizar_contas_a_receber()
    elif opcao == "5":
        saldo_atual = sistema.calcular_saldo_atual()
        print(f"Saldo atual da empresa: R${saldo_atual}")
    elif opcao == "6":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
