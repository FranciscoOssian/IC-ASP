import os
import matplotlib.pyplot as plt
import random
from heapq import heappop, heappush

def random_tuple_pos(x, y, enviroment):
    N1 = random.randint(1, x)
    N2 = random.randint(1, y)
    while enviroment[N1][N1] == 2:
        N1 = random.randint(0, x)
        N2 = random.randint(0, y)
    return (N1, N2)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def plot_performance_over_time(time_steps, scores, title=''):
    plt.figure(figsize=(10, 6))
    plt.plot(time_steps, scores, marker='o', linestyle='-', color='b')
    plt.title(f"""Pontuação ao Longo do Tempo - {title}""")
    plt.xlabel('Tempo (ou Número de Movimentos)')
    plt.ylabel('Pontuação Acumulada')
    plt.grid(True)
    plt.show()

def print_environment(agent, env):
    clear_screen()
    print("Current Environment:")
    
    print(' ', end="")
    for i in range(len(env)):
        print(f"""{i}  """, end="")
    print('')
    
    # Define emoji mappings
    emoji_map = {
        2: "📦",  # Obstacle
        1: "🥥",  # Dirty
        0: "  ",   # Clean (space for formatting)
    }
    
    # Print the environment with emojis
    for i, row in enumerate(env):
        row_display = f"""{i}"""
        for j, cell in enumerate(row):
            if (i, j) == agent.position:
                row_display += "🧹 "  # Vacuum emoji for the agent's position
            else:
                row_display += emoji_map.get(cell, " ") + " "
        print(row_display)
    
    print("\nBattery:", agent.battery)
    print("Current position:", agent.position)
    print("Score:", agent.score)

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star_search(map, start, goal):
    rows, cols = len(map), len(map[0])
    
    # Lista de posições possíveis para se mover (cima, baixo, esquerda, direita)
    neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    # Usaremos um heap para nossa fila de prioridade
    open_list = []
    heappush(open_list, (0 + heuristic(start, goal), 0, start, []))
    
    # Mantém rastreamento das posições visitadas
    closed_list = set()

    while open_list:
        _, cost, current, path = heappop(open_list)
        
        if current in closed_list:
            continue
        
        path = path + [current]
        
        # Se alcançamos o objetivo, retornamos o caminho
        if current == goal:
            return path
        
        closed_list.add(current)
        
        # Explorar os vizinhos
        for dx, dy in neighbors:
            neighbor = (current[0] + dx, current[1] + dy)
            
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and map[neighbor[0]][neighbor[1]] != 2:
                heappush(open_list, (cost + 1 + heuristic(neighbor, goal), cost + 1, neighbor, path))
    
    return None  # Retorna None se não encontrar um caminho