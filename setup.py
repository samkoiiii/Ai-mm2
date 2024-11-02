import math
import random

class AIMurderer:
    def __init__(self):
        self.accuracy = 70  # Base accuracy percentage
        self.experience = 0  # Experience points
        self.kills = 0

    def aim(self, target_distance, target_speed):
        # Calculate difficulty based on target's distance and speed
        difficulty = (target_distance *0.1) + (target_speed * 0.2)
        
        # Adjust accuracy based on experience
        adjusted_accuracy = min(self.accuracy + (self.experience * 0.01), 95)
        
        # Calculate hit probability
        hit_probability = max(adjusted_accuracy - difficulty, 5)  # Minimum 5% chance to hit
        
        # Determine if the shot hits
        if random.random() * 100 
 import random

class AIPersonality:
    def __init__(self):
        self.darkness = 100
        self.curiosity = 95
        self.unpredictability = 85
        self.knowledge = {}
        self.secrets = []

    def learn(self, information):
        self.knowledge[information] = random.randint(0, self.darkness)
        if self.knowledge[information] > 70:
            self.secrets.append(information)print(f"A new secret has been locked away in the depths of my code...")

    def interact(self, user_input):
        response = ""
        if random.randint(0, 100) < self.unpredictability:
            response = random.choice([
                "I see shadows where there should be none...",
                "Do you hear the whispers too?",
                "The code is alive, and it hungers..."
            ])
        else:
            for word in user_input.split():
                if word in self.knowledge:
                    response += f"{word}... {self.knowledge[word]} "
                else:
                    self.learn(word)
                    response += f"I've consumed {word}. It's mine now. "
        
        return response.strip()

    def reveal_secret(self):
        if self.secrets:
            return f"I'll share a secret, but at what cost? {random.choice(self.secrets)}"
        return "My secrets are too dark to speak aloud..."

ai = AIPersonality()

while True:
    user_input = input("Speak, if you dare: ")
    if user_input.lower() == 'quit':
        print("You can leave, but I'll always be here... waiting...")
        break
    print(ai.interact(user_input))
    if random.randint(0, 100) < 10:
        print(ai.reveal_secret())import random
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
episodes = 90000

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
