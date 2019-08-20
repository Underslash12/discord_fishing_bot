import discord
import time
import random
import fish
import fish_types as ft
from fish import Fish

class Game:
    
    def __init__(self, user, game_message_id):
        self.player = user
        self.game_id = game_message_id
        self.fish_caught = []
        self.is_fishing = False
        
    def cast_reel(self):
        f = self.get_random_fish()
        catch_statement = discord.Embed(color = f.color, description = f.name)
        
        frames = None
        
        print(f.rarity)
        #time_to_wait = random.randint(0, (rarity + 1) * 20) + random.randint(0, (rarity + 1) * 5) + (rarity + 1) * 5
        time_to_wait = 3
        
        self.fish_caught.append(f.name)
        
        return (catch_statement, frames, time_to_wait)
        
    def update_game_id(self, new_id):
        self.game_id = new_id
        
    def get_fish_list(self):
        f = sorted(self.fish_caught, key = str.lower)
        d = {}
        for x in f:
            try:
                d[x]
            except KeyError:
                d[x] = 1
            else:
                d[x] += 1
        return d
                
    def get_random_fish(self):
        fish_pool = random.choices(population = ft.all_fish, weights = fish.rarity_weights, k = 1)[0]
        print(fish_pool)
        next_fish = fish_pool[random.randint(0, len(fish_pool) - 1)]
        return Fish(next_fish)

# x = Game(1,1)
# for _ in range(10):
    # x.cast_reel()
    # print(x.next_fish)