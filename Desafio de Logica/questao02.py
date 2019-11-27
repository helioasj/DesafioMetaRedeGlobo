'''02 – QUESTÃO
Um bracket é considerado qualquer um dos seguintes caracteres: (, ), {, }, [ ou ].
Dois brackets são considerados um par combinado se o bracket de abertura (isto é, (, [ou {) ocorre à
esquerda de um
bracket de fechamento (ou seja,),] ou} do mesmo tipo exato. Existem três tipos de pares de brackets : [], {}
e ().
Um par de brackets correspondente não é balanceado se o de abertura e o de fechamento não
corresponderem entre
si. Por exemplo, {[(])} não é balanceado porque o conteúdo entre {e} não é balanceado. O primeiro bracket
inclui o
de abertura, (, e o segundo inclui um bracket de fechamento desbalanceado,].
Dado sequencias de caracteres, determine se cada sequência de brackets é balanceada. Se uma string
estiver
balanceada, retorne SIM. Caso contrário, retorne NAO.
Exemplo:
{[()]} SIM
{[(])} NAO
{{[[(())]]}} SIM'''

class Questao02:
    def balanceado(caracteres):

        tam = len(caracteres)
        result = 'Nao'
        if tam%2==0:

            #print(tam , )
            for i in range(int(tam/2)):
                #print(caracteres[i], caracteres[((i + 1) * -1)])
                #print(i,caracteres[i], '-',((i + 1) * -1),caracteres[((i + 1) * -1)])

                if caracteres[i] == '(' and caracteres[((i + 1) * -1)]==')':
                    result = 'Sim'
                    #print('If 1 - positivo')
                    print(caracteres[i], caracteres[((i + 1) * -1)], 'SIM')
                else:
                    #print('If 1 - negativo')
                    if caracteres[i] == '[' and caracteres[((i + 1) * -1)]==']':
                        result = 'Sim'
                        #print('If 2 - positivo')
                        print(caracteres[i], caracteres[((i + 1) * -1)],'SIM')
                    else:
                        #print('If 2 - negativo')
                        if caracteres[i] == '{' and caracteres[((i + 1) * -1)]=='}':
                            result = 'Sim'
                            #print('If 3 - positivo')
                            print(caracteres[i], caracteres[((i + 1) * -1)],'SIM')
                        else:
                            result = 'Nao'
                            print(caracteres[i], caracteres[((i + 1) * -1)], 'NAO')
                            break
        else:
            result = 'Nao - Numero de caracteres nao balanceado'


        return caracteres + ' ' + result


sequencia = '{[()]}'
#sequencia = '{[(])}'
#sequencia = '{{[[(())]]}}'
#sequencia = '{{{{{{{[[(())]]}}}}}}}'
#sequencia = '{{{{{{{[[(())])}}}}}}}'
#sequencia = '{{{{{{{[[(())])}}}}}}'

print(Questao02.balanceado(sequencia))
