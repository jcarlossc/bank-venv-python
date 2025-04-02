from banco.usuario.PessoaFisica import PessoaFisica
from banco.usuario.PessoaJuridica import PessoaJuridica
from banco.conta.ContaPoupanca import ContaPoupanca
from banco.conta.ContaCorrente import ContaCorrente
from banco.extrato.Extrato import Extrato
from banco.log.Logging import Logging

class Menu:
    """Classe que representa o menu do sistema. 

    Atributos:
        None.
    """
    def __init__(self):
        pass

    @classmethod
    def get_menu(self):
        """Acessa o menu, centraliza todas as operações do sistema.

        Retorna:
            None.
        """
        log = Logging()

        def menu():
            print("\n------------------------------------- BANCO PYTHON ------------------------------------\n")
            print("1 - CADASTRAR USUÁRIO")
            print("2 - CRIAR CONTA")
            print("3 - DEPOSITAR")
            print("4 - SACAR")
            print("5 - EXTRATO")
            print("6 - SAIR")
            print("\n----------------------------------------- FIM -----------------------------------------\n")
        menu()

        while True:
            opcoes = input("\nDIGITE A OPÇÃO: ")
            if opcoes == "1":
                print("---------------------------------------------------------------------------------------")
                print("1 - Pessoa Física")
                print("2 - Pessoa Jurídica")
                print("---------------------------------------------------------------------------------------")
                opcoes_usuario = input("DIGITE O TIPO DE USUÁRIO: ")
                if opcoes_usuario == "1":
                    nome = input("DIGITE SEU NOME: ")
                    cpf = input("DIGITE SEU CPF: ")
                    pessoa_fisica = PessoaFisica(nome, cpf)
                    print("\nUsuário pessoa física cadastrado com sucesso!")

                    log.info("Usuário Cadastrado com sucesso.")
                elif  opcoes_usuario == "2":
                    nome = input("DIGITE SEU NOME: ")
                    cnpj = input("DIGITE SEU CNPJ: ")
                    pessoa_juridica = PessoaJuridica(nome, cnpj)
                    print("\nUsuário pessoa Jurídica cadastrado com sucesso!")

                    log.info("Usuário pessoa jurídica cadastrado com sucesso.")
                else:
                    print("Escolha inválida. Tente novamente.")
                menu()
            elif opcoes == "2":
                if opcoes_usuario == "1":
                    try:
                        cpf = input("DIGITE SEU CPF: ")
                        if cpf == pessoa_fisica.get_cpf():    
                            print("---------------------------------------------------------------------------------------")
                            print("1 - Conta Corrente")
                            print("2 - Conta Poupança")
                            print("---------------------------------------------------------------------------------------")
                            escolha = input("ESCOLHA O TIPO DE CONTA: ")
                            if escolha == "1":
                                conta_corrente = ContaCorrente(pessoa_fisica)
                                print("\nConta Corrente criada com sucesso.")
                            elif escolha == "2":
                                conta_poupanca = ContaPoupanca(pessoa_fisica)
                                print("\nConta Poupança criada com sucesso!")  
                            else:
                                print("Escolha inválida. Tente novamente.")      
                        else:
                            print("Cpf não encontrado. Cadastre-se na opção 1")    
                    except:
                        print("Cpf não encontrado. Cadastre-se na opção 1.")

                elif opcoes_usuario == "2":
                    try:
                        cnpj = input("DIGITE SEU CNPJ: ")
                        if cnpj == pessoa_juridica.get_cnpj():    
                            print("---------------------------------------------------------------------------------------")
                            print("1 - Conta Corrente")
                            print("2 - Conta Poupança")
                            print("---------------------------------------------------------------------------------------")
                            escolha = input("ESCOLHA O TIPO DE CONTA: ")
                            if escolha == "1":
                                conta_corrente = ContaCorrente(pessoa_juridica)
                                print("\nConta Corrente criada com sucesso.")
                            elif escolha == "2":
                                conta_poupanca = ContaPoupanca(pessoa_juridica)
                                print("\nConta Poupança criada com sucesso!")  
                            else:
                                print("Escolha inválida. Tente novamente.")      
                        else:
                            print("Cpf não encontrado. Cadastre-se na opção 1")    
                    except:
                        print("Cpf não encontrado. Cadastre-se na opção 1.")
                else:
                    print("Opcão inválida. Tente novamente.")            
                menu()   
            elif opcoes == "3":
                try:
                    if escolha == "1":
                        print("---------------------------------------------------------------------------------------")
                        valor_deposito = float(input("DIGITE O VALOR DO DEPÓSITO: "))
                        print("---------------------------------------------------------------------------------------")
                        if valor_deposito <= 0:
                            print("Valor inválido. Tente novamente.")
                        else:    
                            conta_corrente.depositar(valor_deposito)
                            print("Valor da conta corrente depositado com sucesso!")

                            log.info("Depósito em Conta Corrente realizado.")
                        menu()      
                    if escolha == "2":
                        print("---------------------------------------------------------------------------------------")
                        valor_deposito = float(input("DIGITE O VALOR DO DEPÓSITO: "))
                        print("---------------------------------------------------------------------------------------")
                        if valor_deposito <= 0:
                                print("Valor inválido. Tente novamente.")
                        else:    
                            conta_poupanca.depositar(valor_deposito)
                            print("Valor da conta poupança depositado com sucesso!")

                            log.info("Depósito em Conta Poupança realizado.")
                        menu()    
                except:
                    print("A opção depósito não é válida sem uma conta criada.")   
                    menu()      
            elif opcoes == "4":
                try:
                    if escolha == "1":
                        print("---------------------------------------------------------------------------------------")
                        valor_saque = float(input("DIGITE O VALOR DO SAQUE: "))
                        print("---------------------------------------------------------------------------------------")
                        if valor_saque > conta_corrente.get_saldo(): 
                            print("Saldo insuficiente.")
                        else: 
                            conta_corrente.sacar(valor_saque)
                            print("Valor da conta corrente sacado com sucesso!")

                            log.info("Saque em Conta Corrente realizado.")

                        menu()    
                    if escolha == "2":
                        print("---------------------------------------------------------------------------------------")
                        valor_saque = float(input("DIGITE O VALOR DO SAQUE: "))
                        print("---------------------------------------------------------------------------------------")
                        if valor_saque > conta_poupanca.get_saldo(): 
                            print("Saldo insuficiente.")
                        else: 
                            conta_poupanca.sacar(valor_saque)
                            print("Valor da conta poupança sacado com sucesso!")

                            log.info("Saque em Conta Poupança realizado.")

                        menu()    
                except:
                    print("A opção saque não é válida sem uma conta criada.")
                    menu() 
            elif opcoes == "5":   
                try:      
                    if escolha == "1":
                        Extrato.get_extrato(conta_corrente)
                    elif escolha == "2":
                        Extrato.get_extrato(conta_poupanca)    
                    else:
                        print("Escolha inválida. Tente novamente.")    
                except:
                    print("A opção Extrato não é válida sem uma conta criada.")      
                menu()           
            elif opcoes == "6": 
                print("OBIGADO E VOLTE SEMPRE!")

                log.info("Sistema encerrado.")

                exit()   
            else:
                print("Opção inválida!")        
            