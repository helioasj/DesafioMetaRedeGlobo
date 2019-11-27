'''04 – QUESTÃO
Dados n inteiros não negativos representando um mapa de elevação onde a largura de
cada barra é 1, calcule quanta água é capaz de reter após a chuva.
Exemplo:
Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6'''

class Questao04:

    def qtdAguaChuva(numeros):
        lista1 = []
        contador = 0
        for i in range(max(numeros)):
            txt = ''
            for numero in numeros:
                if numero >=i+1:
                    lista1.append(1)
                else:
                    lista1.append(0)
            for number in lista1:
                txt += str(number)

            lista1 = []

            tamTxt = len(txt)
            txtIvertido = txt[tamTxt::-1]
            txt = str(int(txtIvertido))
            tamTxt = len(txt)
            txtIvertido = txt[tamTxt::-1]
            txt = str(int(txtIvertido))

            number = str(int(txt))

            for num in number:
                if num=='0':
                    contador = contador +1


        return contador


imput = [0,1,0,2,1,0,1,3,2,1,2,1]
#imput = [2,1,0,2,1,0,1,3,2,1,2,1]
#imput = [3,1,0,2,1,0,1,3,2,1,2,1]

print(Questao04.qtdAguaChuva(imput))