from ModelBasedAgent import ModelBasedAgent
from SimpleReactiveAgent import SimpleReactiveAgent
from utils import print_environment, plot_performance_over_time, random_tuple_pos
from environment import environment, dirty_number

environment_1 = [[cell for cell in line] for line in environment]
environment_2 = [[cell for cell in line] for line in environment]

initial_position = random_tuple_pos(6,6, environment)
initial_battery = 300000
time_taken = 0
scores_over_time = [0]

def execute_simple(dirty_number):
    simpleReactiveAgent = SimpleReactiveAgent(environment_1, initial_position, initial_battery)
    input(f"""started in {initial_position}""")
    while simpleReactiveAgent.battery > 0:
        if(simpleReactiveAgent.score == dirty_number):
            break
        global time_taken
        time_taken = time_taken + 1
        scores_over_time.append(simpleReactiveAgent.score)
        print_environment(simpleReactiveAgent, simpleReactiveAgent.environment)
        #time.sleep(0.1)
        simpleReactiveAgent.clean()
        next_cell = simpleReactiveAgent.decide_movement()
        if next_cell:
            simpleReactiveAgent.move(next_cell)
        else:
            print("No more possible moves.")
            break
    
    print_environment(simpleReactiveAgent, simpleReactiveAgent.environment)
    
    if dirty_number > simpleReactiveAgent.score:
        print('Failed to clean all dirty spots.')

def execute(dirty_number):
    modelBasedAgent = ModelBasedAgent(environment_2, initial_position, initial_battery)
    input(f"""started in {initial_position}""")
    while modelBasedAgent.battery > 0:
        if(modelBasedAgent.score == dirty_number):
            break
        global time_taken
        time_taken = time_taken + 1
        scores_over_time.append(modelBasedAgent.score)
        print_environment(modelBasedAgent, modelBasedAgent.environment)
        #time.sleep(0.1)
        modelBasedAgent.clean()
        next_path = modelBasedAgent.decide_movement()
        if next_path:
            print("next_path", next_path)
            for p in next_path:
                modelBasedAgent.move(p)
        else:
            print("No more possible moves.")
            break
    
    print_environment(modelBasedAgent, modelBasedAgent.environment)
    
    if dirty_number > modelBasedAgent.score:
        print('Failed to clean all dirty spots.')



execute_simple(dirty_number)
l = list(range(time_taken, -1, -1))
l.reverse()
plot_performance_over_time(l, scores_over_time, 'simples')


time_taken = 0
scores_over_time = [0]
execute(dirty_number)
l = list(range(time_taken, -1, -1))
l.reverse()
plot_performance_over_time(l, scores_over_time, 'model')