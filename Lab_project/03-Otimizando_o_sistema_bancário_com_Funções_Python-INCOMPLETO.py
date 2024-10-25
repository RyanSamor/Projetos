#importação de bibliotecas
from datetime import datetime
import time
import textwrap

def hora_agora():
    agora = datetime.today()
    hora = datetime.strftime(agora,'%d/%m/%Y %H:%M:%S')
    return hora

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
    [vi]\tVerificar informações de usuário
    [q]\tSair
    => """)

    return input(menu)

#Menu que será utilizado como modelo para o depósito
def menu_saldo (saldo):
    print(textwrap.dedent(f"""
    ==================== SALDO ====================

                VALOR DISPONÍVEL

    R$ {saldo:.2f}       

    ==============================================="""))

#Função de depósito
def depositar (valor, saldo, extrato):

    #Valor positivo de depósito    
    if valor > 0:
        saldo += valor
        hora = hora_agora()

        #Registra essa movimentação no extrato
        extrato += textwrap.dedent(f"""
        ===============================================
        {hora}                

                        DEPÓSITO
        
        R$ {valor:.2f}
        """)

        #Computa essa movimentação no extrato
        print(textwrap.dedent(f"""
        ================= DEPÓSITO ====================
                              
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
                  
            Você atingiu a quantidade de saques diários"""))
        time.sleep(3)
        pass
    
    #Há saques possíveis
    else:
        valor_final = saldo - valor

        #Ultrapassa o limite de saque
        if valor > 500:
            print(textwrap.dedent("""
                     !!!! MOVIMENTAÇÃO INVÁLIDA !!!
                  
                  Seu limite de saque diário é R$500.00"""))
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
            hora = hora_agora()

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
                {hora}            

                                    SAQUE
        
                R$ {valor:.2f}
                """)
            
            print(numero_saques_dia)
                    
    return saldo, extrato, numero_saques_dia
    
#Mostra o extrato na tela
def exibir_extrato(numero_saques_dia, limite_saques_dia, saldo, extrato):
    
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
            ===============================================

                                INFORMAÇÕES
                    
                Saldo: R$ {saldo:.2f} 
                Saques disponíveis: {saques_disponíveis}

            ===============================================
            """)
         
    print (extrato)
    print (menu_extrato)
    time.sleep(3)

def verificar_usuario(usuarios, cpf):
    for usuario in usuarios:
        if usuario ["cpf"] == cpf:
            return True
        
        else:
            pass

def novo_usuario (usuarios):

    #Menu que será utilizado como modelo para o cpf
    cpf = input(textwrap.dedent("""
        ================= NOVO USUÁRIO ================

                        DIGITE O SEU CPF
        
        Modelo: apenas números

        => """))
    
    if verificar_usuario(usuarios= usuarios, cpf= cpf) == True:
        print(textwrap.dedent(f"""
                            !!!! CADASTRO INVÁLIDO !!!
                                  
                O CPF informado já está cadastrodo no nosso sistema     
                """))
        
        time.sleep(3)
    
    else:
        #Menu que será utilizado como modelo para o nome
        nome = input(textwrap.dedent("""
            ================= NOVO USUÁRIO ================

                        DIGITE O SEU NOME COMPLETO
            
            => """))
        
        #Menu que será utilizado como modelo para o data de nascimento
        data_nascimento = input(textwrap.dedent("""
            ================= NOVO USUÁRIO ================

                    DIGITE SUA DATA DE NASCIMENTO
            
            Modelo: dd/mm/aaaa
                                                
            => """))
        
        #Menu que será utilizado como modelo para o cep
        cep =  input(textwrap.dedent("""
            ================= NOVO USUÁRIO ================

                            DIGITE O SEU CEP
                                        
            Modelo: apenas números
            
            => """))
        
        #Menu que será utilizado como modelo para o endereço
        endereço = input(textwrap.dedent("""
            ================= NOVO USUÁRIO ================

                        DIGITE O SEU ENDEREÇO
                                        
            Modelo: Logradouro, n° - bairro - cidade/estado (sigla)
            
            => """))
        
        usuarios.append({"cpf": cpf, "nome": nome, "data_nascimento": data_nascimento, "cep": cep,  "endereço": endereço}) 

def nova_conta(usuarios,numero_contas, conta_corrente):
    #Menu que será utilizado como modelo para o cpf
    cpf = input(textwrap.dedent("""
        ================== NOVA CONTA =================

                        DIGITE O SEU CPF
        
        Modelo: apenas números

        => """))
    
    if verificar_usuario(usuarios= usuarios, cpf= cpf) == True:
        AGENCIA = "0001"
        numero_contas =+ 1
        conta =  f"{numero_contas:04}"
        conta_corrente.append ({"cpf": cpf, "AGENCIA": AGENCIA, "conta": conta})

        print(textwrap.dedent("""
        ================== NOVA CONTA =================

                    CONTA CRIADA COM SUCESSO

        ==============================================="""))

        
    else:
        print(textwrap.dedent(f"""
                      !!!! CADASTRO INVÁLIDO !!!
                                
            O CPF informado não se encontra no nosso sistema
            """))
        
        time.sleep(3)

def listar_contas(conta_corrente):
    #Menu que será utilizado como modelo para o cpf
    cpf = input(textwrap.dedent("""
        ================ LISTAR CONTAS ================

                        DIGITE O SEU CPF
        
        Modelo: apenas números

        => """))

    for conta in conta_corrente:
        if conta ["cpf"] == cpf:
            print(f"=> {conta_corrente["AGENCIA"]} - {conta_corrente["conta"]}")
        
        else:
            pass
        
def verificar_informações(usuarios):
    #Menu que será utilizado como modelo para o cpf
    cpf = input(textwrap.dedent("""
        ============ VERIFICAR INFORMAÇÕES ============

                        DIGITE O SEU CPF
        
        Modelo: apenas números

        => """))
    
    quantidade_de_contas = 0

    for usuario in usuarios:
        if usuario ["cpf"] == cpf:
            quantidade_de_contas += 1
            print(textwrap.dedent(f"""
            ============ VERIFICAR INFORMAÇÕES ============
                                  
            => Nome completo: {usuario["nome"]}
            => Data de nascimento: {usuario["data_nascimento"]}
            => CEP: {usuario["cep"]}
            => Endereço: {usuario["endereço"]}

            ==============================================="""))
            
            time.sleep(3)
        
    
    if quantidade_de_contas == 0:
        print("!!! Não foi encontrado nenhum usuário ou conta associado à esse CPF")

def processo():
    #Informações iniciais
    LIMITE_SAQUES_DIA = 3
    
    numero_contas = 0
    saldo = 100
    numero_saques_dia = 0
    extrato = ""
    usuarios = []
    conta_corrente = []

    while True:
        opcao = menu().lower().strip()

        #Caso depósito seja selecionado
        if opcao == "d":
            #Menu que será utilizado como modelo para o depósito
            valor = float(input(textwrap.dedent("""
                =================== DEPÓSITO ==================

                          DIGITE O VALOR DO DEPÓSITO

                => """)))
                        
            saldo, extrato = depositar(
                valor = valor, 
                saldo = saldo,
                extrato = extrato
            )

        #Caso saque seja selecionado    
        elif opcao == "s":
            #Menu que será utilizado como modelo para o saque
            valor = float(input(textwrap.dedent("""
                ==================== SAQUE ====================

                        DIGITE O VALOR DO SAQUE

                => """)))

            saldo, extrato, numero_saques_dia = sacar(
                numero_saques_dia= numero_saques_dia,
                limite_saques_dia= LIMITE_SAQUES_DIA,
                saldo= saldo,
                extrato= extrato,
                valor= valor,
            )
            
        #Caso extrato seja selecionado
        elif opcao == "e":
            exibir_extrato(
                numero_saques_dia= numero_saques_dia, 
                limite_saques_dia= LIMITE_SAQUES_DIA, 
                saldo= saldo, 
                extrato= extrato
                )
            
        elif opcao == "nu":
            novo_usuario(usuarios= usuarios)

        elif opcao == "nc":
            nova_conta(usuarios= usuarios, numero_contas= numero_contas, conta_corrente= conta_corrente)

        elif opcao == "lc":
            listar_contas(conta_corrente= conta_corrente)

        elif opcao == "vi":
            verificar_informações(usuarios= usuarios)

        #Opção de saída
        elif opcao == "q":
            break

        #Ajusta caso nao seja selecionada a opção acessível
        else:
            print("Opção não encontrada")
            time.sleep(3)

processo()