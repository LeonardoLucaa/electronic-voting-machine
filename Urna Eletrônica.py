#Lista de Candidatos a Governador
nomeGov1 = "Chewbacca de Assis"
nomeGov2 = "Bem-te-vi Almeida"
nomeGov3 = "Princesa Leia Organa"
nomeGov4 = "R2D2"
nomeGov5 = "Ada Lovelace"
 

#Acumulador de Votos para Governador
votoGov1 = 0
votoGov2 = 0
votoGov3 = 0
votoGov4 = 0
votoGov5 = 0

 
#Lista de Candidatos a Presidente
nomePres1 = "DÂMINA DE CARVALHO PEREIRA"
nomePres2 = "DEHON JUNIO DE MORAIS"
nomePres3 = "JUSSARA MENICUCCI DE OLIVEIRA"
nomePres4 = "CARLOS LINDOMAR DE SOUSA"
nomePres5 = "CARLOS EDUARDO SILVA VOLPATO"


#Acumulador de Votos para Presidente
votoPres1 = 0
votoPres2 = 0
votoPres3 = 0
votoPres4 = 0
votoPres5 = 0


#Inicialização da Contagem de Votos Nulos e Brancos
nuloPres = 0
brancoPres = 0
nuloGov = 0
brancoGov = 0


#Função Imprimir o Menu da Urna
def imprimeMenu():
    print("\n----------- Urna Eletrônica 1.0 -----------\n")
    print("1: Listar candidatos")
    print("2: Iniciar Votação")
    print("3: Apurar votos")
    print("4: Desligar a urna")
    
    return imprimeMenu


#Função Listar os Candidatos
def listarCandidatos():
    print("\nLista de Candidatos a Governador")
    print(f"\nCandidato(a) Governador 1: {nomeGov1}")
    print(f"Candidato(a) Governador 2: {nomeGov2}")
    print(f"Candidato(a) Governador 3: {nomeGov3}")
    print(f"Candidato(a) Governador 4: {nomeGov4}")
    print(f"Candidato(a) Governador 5: {nomeGov5}")
 
    print("\nLista de Candidatos a Presidente ")
    print(f"\nCandidato(a) Presidente 1: {nomePres1}")
    print(f"Candidato(a) Presidente 2: {nomePres2}")
    print(f"Candidato(a) Presidente 3: {nomePres3}")
    print(f"Candidato(a) Presidente 4: {nomePres4}")
    print(f"Candidato(a) Presidente 5: {nomePres5}")

    return listarCandidatos


#Função de Apuração dos Votos
def apuracao(opcao):
    print("\n\nApuração dos Votos para Governador")
    print(f"\nVotos do(a) Candidato(a) {nomeGov1} {votoGov1}")
    print(f"\nVotos do(a) Candidato(a) {nomeGov2} {votoGov2}")
    print(f"\nVotos do(a) Candidato(a) {nomeGov3} {votoGov3}")
    print(f"\nVotos do(a) Candidato(a) {nomeGov4} {votoGov4}")
    print(f"\nVotos do(a) Candidato(a) {nomeGov5} {votoGov5}")
    print(f"\nVotos em Branco para Governador {brancoGov}")
    print(f"\nVotos Nulos para Governador {nuloGov}")
        
    print("\n\nApuração dos Votos para Presidente")
    print(f"\nVotos do(a) Candidato(a) {nomePres1} {votoPres1}")
    print(f"\nVotos do(a) Candidato(a) {nomePres2} {votoPres2}")
    print(f"\nVotos do(a) Candidato(a) {nomePres3} {votoPres3}")
    print(f"\nVotos do(a) Candidato(a) {nomePres4} {votoPres4}")
    print(f"\nVotos do(a) Candidato(a) {nomePres5} {votoPres5}")
    print(f"\nVotos em Branco para Presidente {brancoPres}")
    print(f"\nVotos Nulos para Presidente {nuloPres}")

    return apuracao

 
#Iniciando o contador com 0
opcao = 0


#Inicializando a Urna
imprimeMenu()


#Iniciando laço de repetição
while opcao != 4:
    
    opcao = int(input("\nDigite a sua opção: "))

 
#Opção 1 LISTAR CANDIDATOS
    if opcao == 1:
    
        listarCandidatos()


#Escolha do Governador e Preisdente
    elif opcao == 2:
        
        candGov = int(input("\nDigite o numero do candidato escolhido a Governador: "))

    #Candidato a Governdaor 1        
        if candGov == 1:
            
            print(f"\nCandidato(a) escolhido(a): {nomeGov2}")
            confirma = input("\nConfirma o voto? (S ou N): ")
                
            if confirma == "S" or confirma == "s":
                votoGov1 += 1
                              
            elif confirma == "N" or confirma == "n":
                brancoOUnulo = input("\nDeseja votar em Branco ou Nulo (B ou N) ")
                
                if brancoOUnulo == "B" or brancoOUnulo == "b":
                    brancoGov += 1
                elif brancoOUnulo == "N" or brancoOUnulo == "n":
                    nuloGov += 1

                
    #Candidato a Governador 2             
        elif candGov == 2:
                
            print(f"\nCandidato(a) escolhido(a): {nomeGov2}")
            confirma = input("\nConfirma o voto? (S ou N): ")
                
            if confirma == "S" or confirma == "s":
                votoGov2 += 1
                              
            elif confirma == "N" or confirma == "n":
                brancoOUnulo = input("\nDeseja votar em Branco ou Nulo (B ou N) ")
                
                if brancoOUnulo == "B" or brancoOUnulo == "b":
                    brancoGov += 1
                elif brancoOUnulo == "N" or brancoOUnulo == "n":
                    nuloGov += 1

                
    #Candidato a Governador 3             
        elif candGov == 3:
                
            print(f"\nCandidato(a) escolhido(a): {nomeGov3}")
            confirma = input("\nConfirma o voto? (S ou N): ")
                
            if confirma == "S" or confirma == "s":
                votoGov3 += 1
                              
            elif confirma == "N" or confirma == "n":
                brancoOUnulo = input("\nDeseja votar em Branco ou Nulo (B ou N) ")
                
                if brancoOUnulo == "B" or brancoOUnulo == "b":
                    brancoGov += 1
                elif brancoOUnulo == "N" or brancoOUnulo == "n":
                    nuloGov += 1

                
    #Candidato a Governador 4             
        elif candGov == 4:
                
            print(f"\nCandidato(a) escolhido(a): {nomeGov4}")
            confirma = input("\nConfirma o voto? (S ou N): ")
                
            if confirma == "S" or confirma == "s":
                votoGov4 += 1
                              
            elif confirma == "N" or confirma == "n":
                brancoOUnulo = input("\nDeseja votar em Branco ou Nulo (B ou N) ")
                
                if brancoOUnulo == "B" or brancoOUnulo == "b":
                    brancoGov += 1
                elif brancoOUnulo == "N" or brancoOUnulo == "n":
                    nuloGov += 1

                
    #Candidato a Governador 5             
        elif candGov == 5:
                
            print(f"\nCandidato(a) escolhido(a): {nomeGov5}")
            confirma = input("\nConfirma o voto? (S ou N): ")
                
            if confirma == "S" or confirma == "s":
                votoGov5 += 1
                              
            elif confirma == "N" or confirma == "n":
                brancoOUnulo = input("\nDeseja votar em Branco ou Nulo (B ou N) ")
                
                if brancoOUnulo == "B" or brancoOUnulo == "b":
                    brancoGov += 1
                elif brancoOUnulo == "N" or brancoOUnulo == "n":
                    nuloGov += 1


    #Candidatos a Presidente
              
        nomePres = int(input("\nDigite o numero do candidato escolhido a Presidente: "))
                
    #Candidatos a Presidente 1             
        if nomePres == 1:
            print(f"\nCandidato(a) escolhido(a): {nomePres1}")
            confirma = input("\nConfirma o voto? (S ou N): ")
                
            if confirma == "S" or confirma == "s":
                votoPres1 += 1
                                  
            elif confirma == "N" or confirma == "n":
                brancoOUnulo = input("\nDeseja votar em Branco ou Nulo (B ou N) ")
                
                if brancoOUnulo == "B" or brancoOUnulo == "b":
                    brancoPres += 1
                elif brancoOUnulo == "N" or brancoOUnulo == "n":
                    nuloPres += 1
                

                
    #Candidato a Presidente 2
        elif nomePres == 2:
            print(f"\nCandidato(a) escolhido(a): {nomePres2}")
            confirma = input("\nConfirma o voto? (S ou N): ")
                
            if confirma == "S" or confirma == "s":
                votoPres2 += 1
                                  
            elif confirma == "N" or confirma == "n":
                brancoOUnulo = input("\nDeseja votar em Branco ou Nulo (B ou N) ")
                
                if brancoOUnulo == "B" or brancoOUnulo == "b":
                    brancoPres += 1
                elif brancoOUnulo == "N" or brancoOUnulo == "n":
                    nuloPres += 1

                
    #Candidato a Presidente 3
        elif nomePres == 3:
                    
            print(f"\nCandidato(a) escolhido(a): {nomePres3}")
            confirma = input("\nConfirma o voto? (S ou N): ")
                
            if confirma == "S" or confirma == "s":
                votoPres3 += 1
                                  
            elif confirma == "N" or confirma == "n":
                brancoOUnulo = input("\nDeseja votar em Branco ou Nulo (B ou N) ")
                
                if brancoOUnulo == "B" or brancoOUnulo == "b":
                    brancoPres += 1
                elif brancoOUnulo == "N" or brancoOUnulo == "n":
                    nuloPres += 1

            
    #Candidato a Presidente 4
        elif nomePres == 4:
                
            print(f"\nCandidato(a) escolhido(a): {nomePres4}")
            confirma = input("\nConfirma o voto? (S ou N): ")
                
            if confirma == "S" or confirma == "s":
                votoPres4 += 1
                                  
            elif confirma == "N" or confirma == "n":
                brancoOUnulo = input("\nDeseja votar em Branco ou Nulo (B ou N) ")
                
                if brancoOUnulo == "B" or brancoOUnulo == "b":
                    brancoPres += 1
                elif brancoOUnulo == "N" or brancoOUnulo == "n":
                    nuloPres += 1

                
    #Candidato a Presidente 5
        elif nomePres == 5:
                
            print(f"\nCandidato(a) escolhido(a): {nomePres5}")
            confirma = input("\nConfirma o voto? (S ou N): ")
                
            if confirma == "S" or confirma == "s":
                votoPres5 += 1
                                  
            elif confirma == "N" or confirma == "n":
                brancoOUnulo = input("\nDeseja votar em Branco ou Nulo (B ou N) ")
                
                if brancoOUnulo == "B" or brancoOUnulo == "b":
                    brancoPres += 1
                elif brancoOUnulo == "N" or brancoOUnulo == "n":
                    nuloPres += 1


    elif opcao == 3:
        print("\n\nApuração dos Votos para Governador")
        print(apuracao(opcao))
        
        
    elif opcao == 4:
        print("Obrigado por utilizar a Urna Eletrônica")
        
    else:
        print("Digite uma opção valida!")