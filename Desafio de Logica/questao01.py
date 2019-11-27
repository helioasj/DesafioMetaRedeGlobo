
'''01 - QUESTÃO
Dado um array de números inteiros, retorne os índices dos dois números de forma que
eles se
somem a um alvo específico.
Você pode assumir que cada entrada teria exatamente uma solução, e você não pode usar
o
mesmo elemento duas vezes.
Exemplo:
Dado nums = [2, 7, 11, 15], alvo = 9,
Como nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].'''


class Questao01:


    def encontra(nums,alvo):
        resposta = 'Sem Resposta'

        for i in range(len(nums)):
            if i+1<len(nums):
                resultado = nums[0] + nums[i+1]

                if resultado == alvo:
                    resposta = (0, i + 1)
                    #print('Looping 1=', resultado)
                    #print('Os indices sao',0,i+1)
                    break
                for i in range(len(nums)):
                    if i+1<len(nums) and i>0:
                        resultado = nums[1] + nums[i + 1]

                        if resultado == alvo:
                            resposta = (1, i + 1)
                            #print('Looping 2=', resultado)
                            #print('Os indices sao', 1, i + 1)
                            break
                        for i in range(len(nums)):
                            if i + 1 < len(nums) and i > 1:
                                resultado = nums[2] + nums[i + 1]

                                if resultado == alvo:
                                    resposta = (2, i + 1)
                                    #print('Looping 3=', resultado)
                                    #print('Os indices sao', 2, i + 1)
                                    break

        return resposta
# Definir aqui os numeros inteiros e o alvo a ser procurado
# A funcao atende um array de ate 4 numeros inteiros
nums = [2, 7,11,15]
nums = [2, 72,11,115]
alvo = 9
alvo = 126

print(Questao01.encontra(nums,alvo))
