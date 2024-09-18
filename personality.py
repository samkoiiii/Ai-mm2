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
        print(ai.reveal_secret())
