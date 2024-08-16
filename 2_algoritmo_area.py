# Criando a função que calcula a área dos comodos
def calcular_area_comodos():
    # Criando uma váriavel para somar todas as áreas que forem calculadas (de todos os comodos)
    total_area = 0
    # Criando um Loop que serve para adicionar mais comodos e calcular suas respectivas áreas
    while True:

        # Criando variáveis para receber os valores de largura e comprimento
        # Utilizando o input para o usuário digitar (recebe um valor em string)
        # Convertendo automaticamente os valores recebidos para ponto flutuante utilizando o método "float" (valores decimais)
        largura = float(input("Digite a largura do cômodo (em metros): "))
        comprimento = float(input("Digite o comprimento do cômodo (em metros): "))

        # Criando a variavel que calcula a área do comodo
        area_comodo = largura * comprimento
        # Imprimindo o valor do comodo informado
        print(f"A área deste cômodo é: {area_comodo:.2f} metros quadrados.")

        # Somando a area do atual comodo na variavel que armazena a area total dos comodos
        total_area += area_comodo

        # Perguntando se o usuário deseja adicionar mais comodos
        mais_comodos = input("Deseja adicionar mais cômodos? (s/n): ").strip().lower()

        # Caso o valor recebido seja diferente de "s" (sim), o loop While será interrompido pelo "break"
        if mais_comodos != 's':
            break
    # Fazendo a função retornar o valor da area total
    return total_area

# Chamando a função e atribuindo uma variavel a ela
area_total = calcular_area_comodos()
# Impressão dos resultados
print(f"A área total da casa é: {area_total:.2f} metros quadrados.")