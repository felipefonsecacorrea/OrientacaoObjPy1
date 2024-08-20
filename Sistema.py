# 1- pessoa fisica / 2 -  pessoa juridica / 3 - Sair 
# 1 - cadastrar pessoa fisica / 2 - listar pessoa fisica / 3 - Sair 
# 1 - cadastrar pessoa juridica / 2 - listar pessoa juridica / 3 - Sair 

import __main__
from datetime import date, datetime
from pessoa import Endereco, PessoaFisica


def main():

    lista_pf = []

    while True:
        opcao = int(input("Escolha uma opção: 1- pessoa fisica / 2 -  pessoa juridica / 0 - Sair: "))
        print("")

        if opcao == 1 :
            while True:
                opcao_pf = int(input("Escolha uma opção: cadastrar pessoa fisica / 2 - listar pessoa fisica / 0 - Voltar ao menu anterior: "))
                print("")
                
                if opcao_pf == 1:
                    novapf = PessoaFisica()#importando a pessoa fisica para usar como molde
                    novo_end_pf = Endereco()#importando o enderco para usar como molde

                    novapf.nome = input("Digite o nome da pessoa fisica: ")
                    novapf.cpf = input("Digite o CPF: ")
                    novapf.rendimento = float(input("Digite o rendimento mensal (Digite somente numeros): "))
                    
                    data_nascimento = input("Digite a data de nascimento no formato (dd/mm/aaaa): ")
                    novapf.dataNascimento = datetime.strptime(data_nascimento, '%d/%m/%Y').date()
                    idade = (date.today() - novapf.dataNascimento).days // 365 #calculando quantos anos a pessoa tem, a cada 365 um ano de vida

                    if idade > 18:
                        print("A pessoa tem mais de 18 anos")
                    else:
                        print("A pessoa tem menos de 18 anos. Retorne ao menu...")
                        continue #retornando ao incio do loop
                    
                    #Cadastrando endereço
                    novo_end_pf.logradouro = input("Digite o logradouro: ")
                    novo_end_pf.numero = input("Digite o numero do enderço: ")
                    
                    end_comercial = input("este enderço é comercial ? [S/N]: ") # solicitar a resposta
                    novo_end_pf.endereco_Comercial = end_comercial.strip().upper() == "S" #Tratando a digitação para , definir a resposta 

                    novapf.endereco = novo_end_pf

                    lista_pf.append(novapf)

                elif opcao_pf == 2:
                    if lista_pf:
                        for cada_pf in lista_pf:
                            print(f"Nome: {cada_pf.nome}")
                            print(f"CPF: {cada_pf.cpf}")
                            print(f"Endereço: {cada_pf.endereco}")
                            print(f"Data de Nascimentto: {cada_pf.dataNascimento.strftime('%d/%m/%Y')}")
                            print(f"Imposto a ser pago: {cada_pf.calcular_imposto(cada_pf.rendimento)}")
                            print("")
                            
                    else:
                        print("Lista Vazia !")

                elif opcao_pf == 0:
                    print("Voltando ao menu anterior...")
                    break

                else:
                    print("Opção invalida, por favor digite uma opção valida !")

                print("")
                print("--------------------------------------------------------------------------")
                print("")

        elif opcao == 2:
            print("Funcionalidade pessoa juridica ainda não implementada.")
            pass

        elif opcao == 0:
            print("Obrigado por utilizar nosso sistema ! ;)")
            break

        else:
            print("Opção invalida, por favor digite uma opção valida !")


        print("")
        print("--------------------------------------------------------------------------")
        print("")

if True:
    main() #chama função principal
