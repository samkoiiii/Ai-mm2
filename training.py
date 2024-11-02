import random
from collections import defaultdict

class MM2_AI:
    def __init__(self):
        self.q_table = defaultdict(lambda: [0, 0, 0])  # Actions: Hide, Run, Attack
        self.learning_rate = 0.1
        self.discount_factor = 0.9
        self.epsilon = 0.1

    def choose_action(self, state):
        if random.uniform(0, 1) < self.epsilon:
            return random.randint(0, 2)
        else:
            return self.q_table[state].index(max(self.q_table[state]))

    def update_q_table(self, state, action, reward, next_state):
        current_q = self.q_table[state][action]
        max_next_q = max(self.q_table[next_state])
        new_q = current_q + self.learning_rate * (reward + self.discount_factor * max_next_q - current_q)
        self.q_table[state][action] = new_q

def simulate_mm2_environment():
    # Simplified MM2 environment simulation
    states = ["Innocent", "Sheriff", "Murderer"]
    return random.choice(states)

def get_reward(state, action):
    # Simplified reward system
    if state == "Murderer" and action == 2:  # Attack
        return 10
    elif state == "Innocent" and action == 0:  # Hide
        return 5
    elif state == "Sheriff" and action == 1:  # Run
        return 5
    else:
        return -5

# Training loop
ai_agent = MM2_AI()
episodes =  90000

for episode in range(episodes):
    state = simulate_mm2_environment()
    
    while True:
        action = ai_agent.choose_action(state)
        reward = get_reward(state, action)
        next_state = simulate_mm2_environment()
        
        ai_agent.update_q_table(state, action, reward, next_state)
        
        state = next_state
        
        if random.random() < 0.1:  # 10% chance to end episode
            break

print("Training complete. The AI has learned... but at what cost?")
