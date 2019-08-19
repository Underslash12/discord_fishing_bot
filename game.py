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
        fish_pool = random.choices(population = fish.fish, weights = fish.rarity_weights, k = 1)
        rarity = 0
        for x in range(fish.total_rarities):
            print(fish_pool, fish.fish[x])
            if fish_pool[0] == fish.fish[x]:
                rarity = x
        next_fish = fish_pool[random.randint(0, len(fish_pool) - 1)]
        next_fish = next_fish[0][0]
        
        catch_statement = discord.Embed(color = fish.rarity_color[rarity], description = next_fish)
        
        frames = None
        
        print(rarity)
        #time_to_wait = random.randint(0, (rarity + 1) * 20) + random.randint(0, (rarity + 1) * 5) + (rarity + 1) * 5
        time_to_wait = 3
        
        return [catch_statement, frames, time_to_wait]
        
    def update_game_id(self, new_id):
        self.game_id = new_id

# x = Game(1,1)
# for _ in range(10):
    # x.cast_reel()
    # print(x.next_fish)