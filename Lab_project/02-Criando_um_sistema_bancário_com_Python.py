#importação de bibliotecas
from datetime import datetime
import time  

#Informações iniciais do cliente
saldo = 100
numero_saques_dia = 0
LIMITE_SAQUES_DIA = 3
extrato = ""

#Menu que será utilizado como modelo para o menu principal
menu = """
===============================================

            DIGITE A OPÇÃO DESEJADA
    
    [d] = depositar
    [s] = sacar
    [e] = extrato 
    [q] = sair

===============================================
=> """

#Menu que será utilizado como modelo para o depósito
def menu_saldo (saldo):
    print(f"""
===============================================

              VALOR DE SALDO

R$ {saldo:.2f}       

===============================================
""")

#Menu que será utilizado como modelo para o depósito
menu_deposito = """
===============================================

        DIGITE O VALOR DO DEPÓSITO

===============================================
=> """

#Menu que será utilizado como modelo para o saque
menu_saque = """
===============================================

        DIGITE O VALOR DO SAQUE

===============================================
=> """


while True:
    
    opcao = input(menu)

    #Opção de depósito
    if opcao == "d":

        valor_depositado = round(float(input(menu_deposito)), 2)
        saldo += valor_depositado

        #Registra essa movimentação no extrato
        extrato += f"""
===============================================
                            
                DEPÓSITO
        
R$ {valor_depositado:.2f}

"""     
        #Computa essa movimentação no extrato
        print(f"""
        Sua movimentação foi executada""")
        menu_saldo(saldo = saldo)
        time.sleep(5)
    
    #Opção de saque
    elif opcao == "s":
        #O número de saques feitos está acima do limite
        if numero_saques_dia > LIMITE_SAQUES_DIA:
            print("Você já atingiu a quantidade de saques diários")
            time.sleep(5)
            pass
        
        #Há saques possíveis
        else:
            valor_saque = round(float(input(menu_saque)), 2)
            valor_final = saldo - valor_saque

            #Ultrapassa o limite de saque
            if valor_saque > 500:
                print("Seu limite de saque diário é R$500.00")
                time.sleep(5)

            #Não há saldo suficiente para a movimentação
            elif valor_final < 0:
                print(f"""
Você não tem saldo o suficiente para executar essa movimentação""")
                menu_saldo(saldo = saldo)
                time.sleep(5)

            #Movimentação foi aceita    
            else:
                #Calcula o novo saldo + computa 1 saque adicional feito
                saldo = valor_final
                numero_saques_dia += 1

                #Registra essa movimentação no extrato
                extrato += f"""            
===============================================
                                
                    SAQUE
            
    R$ {valor_saque:.2f}

            """

                #Confirma a execução da movimentação + mostra o saldo existente
                print(f"""
                Sua movimentação foi executada""")
                menu_saldo(saldo = saldo)

                time.sleep(5)


    #Opção de extrato
    elif opcao == "e":
        #Verifica quantos saques tem disponíveis
        saques_disponíveis = LIMITE_SAQUES_DIA-numero_saques_dia

        if extrato == "":
            #Mostra o extrato na tela
            menu_extrato = f"""
      Não foram realizadas movimentações
===============================================

                    INFORMAÇÕES
        
    Saldo: R$ {saldo:.2f} 
    Saques disponíveis: {(saques_disponíveis):.0f}

===============================================

                DIGITE A OPÇÃO DESEJADA
        
    [m] = menu 
    [q] = sair

===============================================
    => """

            opcao = input(menu_extrato)
            
            #Volta para o menu principal
            if opcao == "m":
                pass

            #Para a execução caso o cliente escolha sair    
            elif opcao == "q":
                break

            "Opção não encontrada"
            time.sleep(3)

        else: 
            #Mostra o extrato na tela
            menu_extrato = f"""
            {extrato}
===============================================

                    INFORMAÇÕES
        
    Saldo: R$ {saldo:.2f} 
    Saques disponíveis: {(saques_disponíveis):.0f}

===============================================

                DIGITE A OPÇÃO DESEJADA
        
    [m] = menu 
    [q] = sair

===============================================
    => """

            opcao = input(menu_extrato)
            
            #Volta para o menu principal
            if opcao == "m":
                pass

            #Para a execução caso o cliente escolha sair    
            elif opcao == "q":
                break

            "Opção não encontrada"
            time.sleep(3)

    #Opção de saída
    elif opcao == "q":
        break

    #Ajusta caso nao seja selecionada a opção acessível
    else:
        print("Opção não encontrada")
        time.sleep(3)