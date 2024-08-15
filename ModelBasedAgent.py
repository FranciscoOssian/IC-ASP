import random
from utils import a_star_search

# Constants definitions
CLEAN = 0
DIRTY = 1
OBSTACLE = 2

class ModelBasedAgent:
    def __init__(self, environment, initial_position, initial_battery):
        self.environment = [[cell for cell in line] for line in environment]
        self.position = initial_position
        self.battery = initial_battery
        self.score = 0
        self.finded = set()

    def move(self, new_position):
        if self.battery <= 0:
            print("Battery depleted!")
            return False

        self.position = new_position
        self.battery -= 1
        return True

    def clean(self):
        x, y = self.position
        if self.environment[x][y] == DIRTY:
            self.environment[x][y] = CLEAN
            try:
                self.finded.remove((x,y))
            except:
                pass
            self.score += 1
            print(f"Cleaned at position {self.position}. Score: {self.score}")
    
    def sensors(self):
        x, y = self.position
        adjacent = []
        if x > 0: # Up
            adjacent.append((x-1, y))
        if x < len(self.environment) - 1: # Down
            adjacent.append((x+1, y))
        if y > 0: # Left
            adjacent.append((x, y-1))
        if y < len(self.environment[0]) - 1: # Right
            adjacent.append((x, y+1))
        return adjacent

    def decide_movement(self) -> list:
        adjacent = self.sensors()
        dirty = [pos for pos in adjacent if self.environment[pos[0]][pos[1]] == DIRTY]
        clean = [pos for pos in adjacent if self.environment[pos[0]][pos[1]] == CLEAN]
        
        for d in dirty:
            self.finded.add(d)
        
        if len(dirty) == 0 and len(clean) >= 1:
            if len(clean) == 1:
                self.environment[self.position[0]][self.position[1]] = OBSTACLE
                return [random.choice(clean)]
            else:
                return [random.choice(clean)]
        
        # Calcular os caminhos para cada ponto em self.finded
        finded_paths = []
        for f in self.finded:
            path = a_star_search(self.environment, self.position, f)
            if path:
                finded_paths.append(path)  # Armazenar apenas o caminho

        return sorted(finded_paths, key=len)[0][1:]  # Retorna o caminho mais curto

    def execute(self, dirty_number):
        while self.battery > 0:
            self.clean()
            next_path = self.decide_movement()
            if next_path:
                for p in next_path:
                    self.move(p)
            else:
                print("No more possible moves.")
                break
        if(dirty_number > self.score):
            print('fail to clean all')