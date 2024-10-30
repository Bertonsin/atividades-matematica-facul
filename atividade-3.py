from itertools import product

def tabela_verdade():
    # Exibe o cabeçalho da tabela
    print(f"{'P':<5} {'Q':<5} {'R':<5} {'M':<5} {'C1':<5} {'C2':<5} {'C3':<5} {'Condições satisfeitas':<5}")
    print("-" * 60)
    
    # Itera por todas as combinações de P, Q, R, M
    for P, Q, R, M in product([True, False], repeat=4):
        # Avalia cada condição
        C1 = not P or Q  
        C2 = (P or Q) <= R 
        C3 = (not P) <= (not R or M)  
        
        # Verifica se todas as condições são satisfeitas
        todas_condicoes = C1 and C2 and C3
        
        # Imprime a linha da tabela
        print(f"{P:<5} {Q:<5} {R:<5} {M:<5} {C1:<5} {C2:<5} {C3:<5} {todas_condicoes}")

tabela_verdade()