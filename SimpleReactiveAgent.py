import random

# Constants definitions
CLEAN = 0
DIRTY = 1
OBSTACLE = 2

class SimpleReactiveAgent:
    def __init__(self, environment, initial_position, initial_battery):
        self.environment = [[cell for cell in line] for line in environment]
        self.position = initial_position
        self.battery = initial_battery
        self.score = 2

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

    def decide_movement(self):
        adjacent = self.sensors()
        dirty = [pos for pos in adjacent if self.environment[pos[0]][pos[1]] == DIRTY]
        clean = [pos for pos in adjacent if self.environment[pos[0]][pos[1]] == CLEAN]
        if dirty:
            return random.choice(dirty)
        elif clean:
            return random.choice(clean)
        else:
            return None

    def execute(self, dirty_number):
        while self.battery > 0:
            self.clean()
            next_position = self.decide_movement()
            if next_position:
                self.move(next_position)
            else:
                print("No more possible moves.")
                break
        if(dirty_number > self.score):
            print('fail to clean all')