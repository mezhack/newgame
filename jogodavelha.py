import json

def verificar_empate(tabuleiro):
    """Retorna True se não há posições livres (empate)."""
    return " " not in tabuleiro

def exibir_tabuleiro(tabuleiro):
    """Mostra o tabuleiro formatado na tela."""
    print()
    print(f" {tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]} ")
    print("---+---+---")
    print(f" {tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]} ")
    print("---+---+---")
    print(f" {tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]} ")
    print()

def jogar():
    tabuleiro = [" "] * 9
    jogador_atual = "X"
 
    print("=== JOGO DA VELHA ===")
    print("Posições:")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")
 
    while True:
        exibir_tabuleiro(tabuleiro)
        posicao = pedir_jogada(tabuleiro, jogador_atual)
        fazer_jogada(tabuleiro, posicao, jogador_atual)
 
        if verificar_vitoria(tabuleiro, jogador_atual):
            exibir_tabuleiro(tabuleiro)
            print(f"🏆 Jogador {jogador_atual} venceu!")
            break
 
        if verificar_empate(tabuleiro):
            exibir_tabuleiro(tabuleiro)
            print("🤝 Empate!")
            break
 
        # Troca de jogador
        jogador_atual = "O" if jogador_atual == "X" else "X"
def pedir_jogada(tabuleiro, jogador):
    """Pede e retorna uma posicao valida para o jogador."""
    while True:
        try:
            posicao = int(input(f"Jogador {jogador}, escolha uma posicao (0-8): "))
            if posicao < 0 or posicao > 8:
                print("Posicao invalida. Escolha entre 0 e 8.")
            elif tabuleiro[posicao] != " ":
                print("Posicao ja ocupada. Escolha outra.")
            else:
                return posicao
        except ValueError:
            print("Digite um numero.")

def fazer_jogada(tabuleiro, posicao, jogador):
    """
    Marca a posicao com o simbolo do jogador.
    Retorna True se a jogada foi valida, False se a posicao ja estava ocupada.
    """
    if tabuleiro[posicao] == " ":
        tabuleiro[posicao] = jogador
        return True
    else:
        return False

def verificar_vitoria(tabuleiro, jogador):
    """Retorna True se o jogador venceu, False caso contrario."""

    # Todas as combinacoes possiveis de vitoria
    combinacoes = [
        [0, 1, 2],  # linha de cima
        [3, 4, 5],  # linha do meio
        [6, 7, 8],  # linha de baixo
        [0, 3, 6],  # coluna esquerda
        [1, 4, 7],  # coluna do meio
        [2, 5, 8],  # coluna direita
        [0, 4, 8],  # diagonal principal
        [2, 4, 6],  # diagonal secundaria
    ]

    for combo in combinacoes:
        if (tabuleiro[combo[0]] == tabuleiro[combo[1]] ==
                tabuleiro[combo[2]] == jogador):
            return True

    return False

def salvar_placar(jogador):
    with open("placar.json", "r") as f:
        placar = json.load(f)
    with open("placar.json", "w") as f:
        if jogador == "x":
            placar["x"] = placar["x"] + 1
        elif jogador == "o":
            placar["o"] = placar["o"] + 1
        else:
            print("Jogador invalido para salvar placar.")
            return
        json.dump(placar, f)

def carregar_placar():
    with open("placar.json", "r") as f:
        return json.load(f)

def novo_jogador(nome):
    nome = input ("digite o nome do jogador:")

    return  nome

jogar()
