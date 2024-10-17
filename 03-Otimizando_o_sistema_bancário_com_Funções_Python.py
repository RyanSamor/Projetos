#importação de bibliotecas
from datetime import datetime
import time
import textwrap

def hora_agora():
    agora = datetime.today()
    hora = datetime.strftime(agora,'%d/%m/%Y %H:%M:%S')
    print (hora)

#Menu que será utilizado como modelo para o menu principal
def menu():
    menu = textwrap.dedent("""\n
    ================ MENU ================

            DIGITE A OPÇÃO DESEJADA

    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """)

    return input(menu)

#Menu que será utilizado como modelo para o depósito
def menu_saldo (saldo):
    print(textwrap.dedent(f"""
    =====================SALDO=====================

                VALOR DISPONÍVEL

    R$ {saldo:.2f}       

    ===============================================
    """))


#Função de depósito
def depositar (valor, saldo, extrato):

    #Valor positivo de depósito    
    if valor > 0:
        saldo += valor

        #Registra essa movimentação no extrato
        extrato += textwrap.dedent(f"""
        ===============================================
        {hora_agora}                    
                        DEPÓSITO
        
        R$ {valor:.2f}

        """)

        #Computa essa movimentação no extrato
        print(textwrap.dedent(f"""
        ==================DEPÓSITO=====================
                              
            Sua movimentação foi executada"""))
        menu_saldo(saldo = saldo)
        time.sleep(3)

    #Valor negativo ou zero de depósito
    else:
        print(textwrap.dedent("""
                !!!! MOVIMENTAÇÃO INVÁLIDA !!!
                  
            Valor depositado negativo ou igual a zero
            """))
    
    return saldo, extrato


#Função de saques
def sacar(numero_saques_dia, limite_saques_dia, saldo, extrato, valor):
    
    #O número de saques feitos está acima do limite
    if numero_saques_dia > limite_saques_dia:
        print(textwrap.dedent("""
                    !!!! MOVIMENTAÇÃO INVÁLIDA !!!
                  
            Você atingiu a quantidade de saques diários
            """))
        time.sleep(3)
        pass
    
    #Há saques possíveis
    else:
        valor_final = saldo - valor

        #Ultrapassa o limite de saque
        if valor > 500:
            print(textwrap.dedent("""
                     !!!! MOVIMENTAÇÃO INVÁLIDA !!!
                  
                  Seu limite de saque diário é R$500.00
                  """))
            time.sleep(3)

        #Não há saldo suficiente para a movimentação
        elif valor_final < 0:
            print(textwrap.dedent(f"""
                              !!!! MOVIMENTAÇÃO INVÁLIDA !!!
                                  
                Você não tem saldo o suficiente para executar essa movimentação
                                  
                """))
            menu_saldo(saldo = saldo)
            time.sleep(3)
        
        #Movimentação foi aceita    
        else:
            #Calcula o novo saldo + computa 1 saque adicional feito
            saldo = valor_final
            numero_saques_dia += 1

            #Confirma a execução da movimentação + mostra o saldo existente
            print(textwrap.dedent(f"""
                =====================SAQUE=====================
                              
                        Sua movimentação foi executada
                                  
                """))
            menu_saldo(saldo = saldo)

            time.sleep(3)

            #Registra essa movimentação no extrato
            extrato += textwrap.dedent(f"""            
                ===============================================
                {hora_agora}            
                                    SAQUE
        
                R$ {valor:.2f}

                """)
                    
    return saldo, extrato
    

#Mostra o extrato na tela
def extrato(numero_saques_dia, limite_saques_dia, saldo, extrato):
    
    #Verifica quantos saques tem disponíveis
    saques_disponíveis = limite_saques_dia-numero_saques_dia
    
    #Não foram feitas movimentações
    if extrato == "":
        menu_extrato = textwrap.dedent(f"""
                    Não foram realizadas movimentações
                                       
            ===============================================

                            INFORMAÇÕES
                    
            Saldo: R$ {saldo:.2f} 
            Saques disponíveis: {saques_disponíveis}

            ===============================================
            """)
        
    #Foram feitas movimentações
    else: 
         menu_extrato = textwrap.dedent(f"""
            {extrato}
            ===============================================

                                INFORMAÇÕES
                    
                Saldo: R$ {saldo:.2f} 
                Saques disponíveis: {saques_disponíveis}

            ===============================================
            """)


def processo():
    #Informações iniciais
    LIMITE_SAQUES_DIA = 3
   
    saldo = 100
    numero_saques_dia = 0
    extrato = ""

    while True:
        opcao = menu()

        #Caso depósito seja selecionado
        if opcao == "d":
            #Menu de depósito que será utilizad
            menu_deposito = textwrap.dedent("""
                ====================DEPÓSITO===================
                
                        DIGITE O VALOR DO DEPÓSITO

                => """)
    
            valor = float(input(menu_deposito))

            saldo, extrato = depositar(
                valor = valor, 
                saldo = saldo,
                extrato = extrato
            )

        #Caso saque seja selecionado    
        elif opcao == "s":
            #Menu que será utilizado como modelo para o saque
            menu_saque = textwrap.dedent("""
                =====================SAQUE=====================

                        DIGITE O VALOR DO SAQUE

                => """)

            valor = float(input(menu_saque))

            saldo, extrato = sacar(
                numero_saques_dia= numero_saques_dia,
                limite_saques_dia= LIMITE_SAQUES_DIA,
                saldo= saldo,
                extrato= extrato,
                valor= valor,
            )
            
        #Caso extrato seja selecionado
        elif opcao == "e":
            extrato(
                numero_saques_dia= numero_saques_dia, 
                limite_saques_dia= LIMITE_SAQUES_DIA, 
                saldo= saldo, 
                extrato= extrato
                )

        #Opção de saída
        elif opcao == "q":
            break

        #Ajusta caso nao seja selecionada a opção acessível
        else:
            print("Opção não encontrada")
            time.sleep(3)


processo()