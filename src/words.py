master_list = ["stone","gravel","dirt","leaves","apple","bamboo","melon","cactus","carrot","beans","potato","pumpkin",
               "tree","wood","kelp","barrel","furnace","bed","bookshelf","ladder","bee","lantern","cake","campfire",
               "candle","doorbell","sign","sponge","fence","farmland","torch","camel","chicken","cat","donkey","frog",
               "dog","horse","mule","parrot","pig","rabbit","salmon","sheep","squid","tadpole","spider",
               "dolphin","fox","goat","panda","llama","pufferfish","wolf","house","crossbow","painting","snowball",
               "string","lava","water","sandstone","tulip","poppy","turtle","glass","grass","iron","chain","vault",
               "flammable","aesthetic","projectile","inventory","survival", "ingredient","mechanism","vertical",
               "horizontal","skeleton","button","slab","stick","sword","chest","enchant","table","monument","mansion",
               "fortress","creative"]

easy = []
medium = []
hard = []

for i in range(len(master_list)):
    if len(master_list[i]) <6:
        easy.append(master_list[i])
    elif len(master_list[i]) < 8:
        medium.append(master_list[i])
    else:
        hard.append(master_list[i])

def word_list(difficulty):
    if difficulty == "easy":
        return easy
    elif difficulty == "medium":
        return medium
    else:
        return hard