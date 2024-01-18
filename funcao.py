vitorias = int(input("Informe o número de vitórias: "))

derrotas = int(input("Informe o número de derrotas: "))  

def calculadoraPR (vitorias, derrotas):
    saldo = (vitorias-derrotas)
    nivel = "Indefinido"
    if saldo <= 10:
        nivel = "Ferro"
    else:
        if saldo >= 11 & saldo <=20:
            nivel = "Bronze"
        else:
            if  saldo >= 21 & saldo <=50:
                nivel = "Prata"
            else:
                if 51 <= saldo <=80:
                    nivel = "Ouro"
                else:
                    if 81 <= saldo <=90:
                        nivel = "Diamante"
                    else:
                        if 91 <= saldo <=100:
                            nivel = "Lendário"
                        else:
                            nivel = "Imortal"
    return(f'O Herói tem saldo de {saldo}  pontos e está no nível {nivel}')


vitorias = 80
derrotas = 15

calculadoraPR(vitorias, derrotas)