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
 
