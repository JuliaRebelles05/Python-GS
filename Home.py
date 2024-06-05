dados = {
    "empresas_parceiras": {},
    "clientes": {}
}

while True:
    # Exibir menu principal
    print(" Bem-vindo à Fazenda Marinha Tech4Change! ")
    print(" Escolha uma opção: ")
    print("1. Login como empresa parceira ")
    print("2. Login como cliente")
    print("3. Cadastro de empresa parceira ")
    print("4. Cadastro de cliente ")
    print("5. Sair ")

    opcao = input(" \nDigite o número da opção desejada: ")

    if opcao == "1":  # Login como empresa parceira
        login = input("\nDigite o login da empresa parceira: ")
        senha = input("Digite a senha: ")
        if login in dados["empresas_parceiras"] and dados["empresas_parceiras"][login] == senha:
            
            
            while True:
                print(f"\nBem-vindo, {login}!")
                # Lógica para a empresa parceira
                print ("1. Importância da sua Parceria")
                print ("2. Benefícios da sua Parceria")
    

                opcao = input(" \nDigite o número da opção desejada: ")

                if opcao == "1": # Importância da sua Parceria
                    print("\nÉ com grande satisfação que compartilhamos informações da Fazenda Marinha Tech4Change. Como parceira, sua empresa desempenha um papel fundamental em nosso compromisso com a sustentabilidade dos oceanos e o fornecimento de produtos marinhos de alta qualidade. Nossa fazenda marinha é dedicada à produção responsável de alimentos marinhos, utilizando práticas sustentáveis que visam a preservação dos ecossistemas aquáticos.")

                elif opcao == "2": # Benefícios da sua Parceria
                    print ("\nA intenção da Tech4Change é atingir positivamente todos que fazem parte deste projeto, incluindo você Empresa Parceira. Em muitas jurisdições, o investimento em atividades sustentáveis, como fazendas marinhas, pode qualificar as empresas para incentivos fiscais, subsídios ou outros benefícios governamentais. Esses incentivos podem incluir redução de impostos, créditos fiscais ou acesso a fundos de investimento específicos. Além de fortalecer a imagem corporativa da sua empresa, diante das causas ambientais que impactam o mundo como um todo.")

        else:
            print("\nLogin ou senha incorretos.")

    elif opcao == "2":  # Login como cliente
        email = input("\nDigite o e-mail do cliente: ")
        senha = input("Digite a senha: ")
        if email in dados["clientes"] and dados["clientes"][email] == senha:
            print(f"\nBem-vindo, {email}!")
            
            while True:
                print(f"\nBem-vindo, {email}!")
                # Lógica para o cliente
                print ("1. Importância da sua colaboração")
                print ("2. Benefícios da sua colaboração")
    

                opcao = input(" \nDigite o número da opção desejada: ")

                if opcao == "1": # Importância da sua Colaboração
                    print("\nVocê que mora próximo à pedaços de mar, rios e lagos, saiba quue você é importante para o nosso projeto. As Fazendas Marinhas da Tech4Change contam com centenas de colaboradores espalhadas em terriório nacional. As fazendas marinhas são essenciais para enfrentar os desafios globais relacionados à segurança alimentar, sustentabilidade ambiental e desenvolvimento econômico. Sua importância continuará a crescer à medida que a demanda por alimentos aumenta e a necessidade de práticas de produção sustentável se torna mais urgente.")

                elif opcao == "2": # Benefícios da sua Colaboração
                    print ("\nOs cuidadores de fazendas marinhas desempenham um papel vital na indústria da aquacultura, e os benefícios que recebem refletem a importância de seu trabalho. Além das recompensas financeiras, esses profissionais desfrutam de oportunidades de desenvolvimento, segurança alimentar, segurança no emprego, e a satisfação de contribuir para práticas sustentáveis e a conservação ambiental.")

        else:
            print("E-mail ou senha incorretos.")

    elif opcao == "3":  # Cadastro de empresa parceira
        login = input("Digite um login para a empresa: ")
        senha = input("Digite uma senha: ")
        dados["empresas_parceiras"][login] = senha
        print("Empresa cadastrada com sucesso!")

    elif opcao == "4":  # Cadastro de cliente
        email = input("Digite seu e-mail: ")
        senha = input("Digite uma senha: ")
        dados["clientes"][email] = senha
        print("Cliente cadastrado com sucesso!")

    elif opcao == "5":  # Sair
        print("Obrigado por usar a Fazenda Marinha Tech4Change! ")

        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")





