# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3. 
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!
import os

def calcula(x,y, escolha):
    try:
        if escolha == 1:
            return [f'\n{x} + {y} = {x+y}', True]
        elif escolha == 2:
            return [f'\n{x} - {y} = {x-y}', True]
        elif escolha == 3:
            return [f'\n{x} * {y} = {x*y}', True]
        elif escolha == 4:
            return [f'\n{x} / {y} = {x/y}', True]
        else:
            return ['\nEscolha inválida!', False]
    except:
        return ['\nErro no sistema! Parâmetros inválidos...', False]


def main():
    continuar = True
    while continuar:
        #Imprime instruções de escolha de operação aritmética
        print('\nSelecione a operação desejada: ')
        print('\n1. Soma\n2.Subtração\n3.Mutiplicação\n4.Divisão')

        #Captura em tela e válida Escolha do Operador Aritmético
        escolhavalida = False
        while not escolhavalida:    
            try:
                escolha = int(input('\nDigite sua opção: '))
                escolhavalida = True
            except:
                print('\nEscolha inválida! Escolha um número: [1 - 2 - 3 - 4]...')

        #Captura em tela e válida Dados a serem calculados
        dadosvalidos = False
        while not dadosvalidos:    
            try:
                num1 = float(input('\nDigite o primeiro número: '))
                num2 = float(input('Digite o segundo número: '))
                
                if num2 == 0 and escolha == 4:
                    print('\nNão é permitido divisor igual a Zero! Digite novamente o dividendo e o divisor...')
                else:
                    dadosvalidos = True
            except:
                print('\nDados inválidos! Digite um número inteiro ou decimal...')

        #Calcula valores e retorna lista como resultado
        resultado = calcula(num1, num2, escolha)
        
        #Se ocorrer algum erro na execução da função "calcula", Retorna False
        #Se a função for executada com sucesso, Retorna True
        print(resultado[0])
        
        #Se não houver erros na execução da função Calcular, pergunta pro usuário se deseja continuar
        # execução dos cálculos
        if resultado[1]:
            #Se usuário escolher não continuar, variável Continuar = False
            if not input('\nDeseja executar mais cálculos? (s/n) ').upper() == 'S':
                continuar = False


if __name__ == '__main__':
    #limpa tela do sistema
    os.system('cls')

    #imprime titulo do programa
    print("\n******************* Python Calculator *******************")

    #chama função principal
    main()

    #imprime mensagem de agradecimento e fim da execução do programa
    print('\nMuito obrigada, volte sempre! Fim da execução do sistema...\n')