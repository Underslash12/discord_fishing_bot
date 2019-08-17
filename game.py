import discord
import time
import random
import fish

class Game:
    
    def __init__(self, user, game_message_id):
        self.player = user
        self.game_id = game_message_id
        
    def cast_reel(self):
        #self.game_state = 
        fish_pool = random.choices(population = fish.fish, weights = fish.fish_rarity_weights, k = 1)
        self.next_fish = fish_pool[random.randint(0, len(fish_pool) - 1)]
        
    def update_game_id(self, new_id):
        self.game_id = new_id

x = Game(1,1)
for _ in range(10):
    x.cast_reel()
    print(x.next_fish)