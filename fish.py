# fish.py

import fish_types as ft

class Fish:
    
    def __init__(self, fish_name):
        self.name = fish_name
        self.rarity = 0
        for x in range(len(ft.all_fish)):
            if fish_name in ft.all_fish[x]:
                self.rarity = x + 1
        self.color = rarity_color[self.rarity - 1]
    



# fish_rarity = []
# fish_rarity_weights = [1, 0.5, 0.3, 0.1, 0.008, 0.003, ]
rarity_weights = [1, 1, 1, 1, 1, 1, 1, 1]

#hex
rarity_color_hex = ["E7E7E7", "4AD11D", "1D65E9", "9F40BF", "FFDA00", "8700FF", "FF007C", "EFA710"]
#decimal
rarity_color = [15198183, 4903197, 1926633, 10436799, 16767488, 8847615, 16711804, 15705872]

#cool_blue = "B4E1FF", "003E67"
total_rarities = 8