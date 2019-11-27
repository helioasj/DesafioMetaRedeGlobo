'''03 – QUESTÃO
Digamos que você tenha um array para o qual o elemento i é o preço de uma determinada
ação
no dia i.
Se você tivesse permissão para concluir no máximo uma transação (ou seja, comprar uma
e
vender uma ação), crie um algoritmo para encontrar o lucro máximo.
Note que você não pode vender uma ação antes de comprar.
Exemplo:
Input: [7,1,5,3,6,4]
Output: 5 (Comprou no dia 2 (preço igual a 1) e vendeu no dia 5 (preço
igual
a 6), lucro foi de 6 – 1 = 5
Input: [7,6,4,3,1]
Output: 0 (Nesse caso nenhuma transação deve ser feita, lucro máximo
igual a
0)'''

class Questao03:
    def lucroMaximo(precosDia):

        listaOrdenada = sorted(precosDia)
        print(precosDia)


        listaOrdenada.reverse()

        if listaOrdenada == precosDia:
            result = 0
        else:
            #print('E diferente - Significa que ela nao eh uma lista onde as acoes so descrescem')
            precoMinimoCompra = min(precosDia)
            proximoDiaDisponivel = precosDia.index(precoMinimoCompra)+1
            novaLista = precosDia[proximoDiaDisponivel:]

            precoMaximoVenda = max(novaLista)
            lucro = precoMaximoVenda - precoMinimoCompra
            result = lucro

        return result


precosDia = [7,1,5,3,6,4]
precosDia = [9,8,7,6,5,4,3,2,1]
precosDia = [7,1,5,3,6,10]


print(Questao03.lucroMaximo(precosDia))