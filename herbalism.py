#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from random import randint
import math
#import numpy as np

specialMax = 1
rareMax = 2
uncommonMax = 3
commonMax = 4

commonTable = {
    2:  {
    'ingredient': "Mandrake Root"},
    12:
    {
    'ingredient': "Mandrake Root"},
    3: {
    'ingredient': "Quicksilver Lichen"},
    4: {
    'ingredient': "Quicksilver Lichen"},
    5: {
    'ingredient': "Wild Sageroot"},
    6: {
    'ingredient': "Wild Sageroot"},
    7: {
    'ingredient': "Bloodgrass",
    'amount': commonMax
    },
    8: {
    'ingredient': "Wyrmtongue Petals"},
    9: {
    'ingredient': "Wyrmtongue Petals"},
    10: {
    'ingredient': "Milkweed Seeds"},
    11: {
    'ingredient': "Milkweed Seeds"},
    }

        # arctic ingredients
arcticTable = {
    2:  {
    'ingredient': "Silver Hibiscus",
    'amount': rareMax},

    3: {
    'ingredient': "Mortflesh Powder",
    'amount': uncommonMax},
    4: {
    'ingredient': "Ironwood Heart",
    'amount': uncommonMax},
    5: {
    'ingredient': "Frozen Seedlings",
    'amount': uncommonMax,
    'additionalRules': "Find 2x the rolled amount"},
    6: {
    'ingredient': 'Common',
    'amount': commonMax,
    'additionalRules': "Roll on 'Common' Ingredient table"},
    7: {
    'ingredient': 'Common',
    'amount': commonMax,
    'additionalRules': "Roll on 'Common' Ingredient table"},
    8: {
    'ingredient': 'Common',
    'amount': commonMax,
    'additionalRules': "Roll on 'Common' Ingredient table"},
    9: {
    'ingredient':  "Arctic Creeper",
    'amount': uncommonMax,
    'additionalRules': "Find 2x the rolled amount"},
    10: {
    'ingredient': "Fennel Silk",
    'amount': uncommonMax},
    11: {
    'ingredient': "Fiend's Ivy",
    'amount': uncommonMax},
    12: {'ingredient':"Void Root",
    'amount': rareMax}
}
# underwater ingredients
underwaterTable = {
    2: {'ingredient': "Hydrathistle",
        'amount': rareMax,
        'additionalRules': "Find 2x the rolled amount"},
    3:{'ingredient': "Amanita Cap",
    'amount': uncommonMax},

    4:  {'ingredient': "Hyancinth Nectar",
     'amount': uncommonMax},
    5:   {'ingredient': "Chromus Slime",
      'amount': uncommonMax,
      'additionalRules': "Find 1'Difficulty': -2x the rolled amount"},

    6:{'ingredient': 'Common',
    'amount': commonMax,
    'additionalRules': "Roll on 'Common' Ingredient table"},
    7:{'ingredient': 'Common',
    'amount': commonMax,
    'additionalRules': "Roll on 'Common' Ingredient table"},
    8:{'ingredient': 'Common',
    'amount': commonMax,
    'additionalRules': "Roll on 'Common' Ingredient table"},
    9:{'ingredient': "Lavender Sprig",       'amount': uncommonMax,        'additionalRules': "Coastal Only"},
    10:{'ingredient': "Blue Toadshade",       'amount': uncommonMax,        'additionalRules': "Coastal Only"},
    11:{'ingredient': "Wrackwort Bulbs",      'amount': uncommonMax},
    12:{'ingredient': "Cosmos Glond",         'amount': rareMax,            'additionalRules': "Find 1'Difficulty': -2x the rolled 'amount'"}
    }
    # desert ingredients
desertTable = {
    2:{'ingredient': "Cosmos Glond",         'amount': rareMax},
    3:{'ingredient': "Arrow Root",           'amount': uncommonMax},
    4:{'ingredient': "Dried Ephedra",        'amount': uncommonMax},
    5:{'ingredient': "Cactus Juice",         'amount': uncommonMax,        'additionalRules': "Find 2x the rolled 'amount'"},
    6:{'ingredient': 'Common',    'amount': commonMax,          'additionalRules': "Roll on 'Common' Ingredient table"},
    7:{'ingredient': 'Common',    'amount': commonMax,          'additionalRules': "Roll on 'Common' Ingredient table"},
    8:{'ingredient': 'Common',    'amount': commonMax,          'additionalRules': "Roll on 'Common' Ingredient table"},
    9:{'ingredient': "Drakus Flower",        'amount': uncommonMax},
    10:{'ingredient': "Scillia Beans",        'amount': uncommonMax},
    11:{'ingredient': "Spineflower Berries",  'amount': uncommonMax},
    12:{'ingredient': "Voidroot",             'amount': rareMax,            'additionalRules': "Come with 1 Elemental Water"},
}
# forest ingredients
forestTable = {
    2: {'ingredient': "Harrada Leaf",         'amount': rareMax},
    3: {'ingredient': "Nightshade Berries",   'amount': uncommonMax},
    4:{'ingredient': "Emetic Wax",           'amount': uncommonMax},
    5:{'ingredient': "Verdant Nettle",       'amount': uncommonMax},
    6:{'ingredient': 'Common',    'amount': commonMax,          'additionalRules': "Roll on 'Common' Ingredient table"},
    7:{'ingredient': 'Common',    'amount': commonMax,          'additionalRules': "Roll on 'Common' Ingredient table"},
    8:{'ingredient': 'Common',    'amount': commonMax,          'additionalRules': "Roll on 'Common' Ingredient table"},
    9:{'ingredient': "Arrow Root",           'amount': uncommonMax},
    10:{'ingredient': "Ironwood Heart",       'amount': uncommonMax},
    11:{'ingredient': "Blue Toadshade",       'amount': uncommonMax},
    12:{'ingredient': "Wisp Stalks",          'amount': rareMax,            'additionalRules': "Find 2x during Night, Re-roll during Day"}
}
# grasslands ingredients
grasslandsTable = {
    2:  {'ingredient': "Harrada Leaf",         'amount': rareMax},
    3:  {'ingredient': "Drakus Flower",        'amount': uncommonMax},
    4:  {'ingredient': "Lavender Sprig",       'amount': uncommonMax,        'additionalRules': "Find 2x the rolled 'amount'"},
    5: {'ingredient': "Arrow Root",           'amount': uncommonMax},
    6:{'ingredient': 'Common',    'amount': commonMax,          'additionalRules': "Roll on 'Common' Ingredient table"},
    7:{'ingredient': 'Common',    'amount': commonMax,          'additionalRules': "Roll on 'Common' Ingredient table"},
    8:{'ingredient': 'Common',    'amount': commonMax,          'additionalRules': "Roll on 'Common' Ingredient table"},
    9:  {'ingredient': "Scillia Beans",        'amount': uncommonMax,        'additionalRules': "Find 2x the rolled 'amount'"},
    10:  {'ingredient': "Cactus Juice",         'amount': uncommonMax},
    11:   {'ingredient': "Tail Leaf",            'amount': uncommonMax},
    12:{'ingredient': "Hyancinth Nectar",     'amount': rareMax}
}
# hill ingredients
hillsTable = {
    2: {'ingredient': "Devil's Bloodleaf",    'amount': rareMax},
    3:{'ingredient': "Nightshade Berries",   'amount': uncommonMax},
    4:{'ingredient': "Tail Leaf",            'amount': uncommonMax,        'additionalRules': "Find 2x the rolled 'amount'"},
    5:{'ingredient': "Lavender Sprig",       'amount': uncommonMax},
    6:{'ingredient': 'Common',    'amount': commonMax,          'additionalRules': "Roll on 'Common' Ingredient table"},
    7:{'ingredient': 'Common',    'amount': commonMax,          'additionalRules': "Roll on 'Common' Ingredient table"},
    8:{'ingredient': 'Common',    'amount': commonMax,          'additionalRules': "Roll on 'Common' Ingredient table"},
    9:   {'ingredient': "Ironwood Heart",       'amount': uncommonMax},
    10:   {'ingredient': "Gengko Brush",         'amount': uncommonMax},
    11:   {'ingredient': "Rock Vine",            'amount': uncommonMax,        'additionalRules': "Find 2x the rolled 'amount'"},
    12:   {'ingredient': "Harrada Leaf",         'amount': rareMax}
}
# mountain ingredients
mountainTable = {
    2:{'ingredient': "Basilisk's Breath",    'amount': rareMax},
    3:{'ingredient': "Frozen Seedlings",     'amount': uncommonMax,        'additionalRules': "Find 2x the rolled 'amount'"},
    4:{'ingredient': "Arctic Creeper",       'amount': uncommonMax,        'additionalRules': "Find 2x the rolled 'amount'"},
    5:{'ingredient': "Dried Ephedra",        'amount': uncommonMax},
    6:{'ingredient': 'Common',    'amount': commonMax,          'additionalRules': "Roll on 'Common' Ingredient table"},
    7:{'ingredient': 'Common',    'amount': commonMax,          'additionalRules': "Roll on 'Common' Ingredient table"},
    8:{'ingredient': 'Common',    'amount': commonMax,          'additionalRules': "Roll on 'Common' Ingredient table"},
    10:{'ingredient': "Luminous Cap Dust",    'amount': uncommonMax,        'additionalRules': "Find 2x the rolled 'amount' in Caves"},
    11:{'ingredient': "Rock Vine",            'amount': uncommonMax},
    12:{'ingredient': "Primordial Balm",      'amount': rareMax}
}
# swamp ingredients
swampTable = {
    2:{'ingredient': "Devil's Bloodleaf",    'amount': rareMax},
    3:{'ingredient': "Spineflower Berries",  'amount': uncommonMax},
    4:{'ingredient': "Emetic Wax",           'amount': uncommonMax},
    5:{'ingredient': "Amanita Cap",          'amount': uncommonMax,        'additionalRules': "Find 2x the rolled amount"},
    6:{'ingredient': 'Common',    'amount': commonMax,          'additionalRules': "Roll on 'Common' Ingredient table"},
    7:{'ingredient': 'Common',    'amount': commonMax,          'additionalRules': "Roll on 'Common' Ingredient table"},
    8:{'ingredient': 'Common',    'amount': commonMax,          'additionalRules': "Roll on 'Common' Ingredient table"},
    9:{'ingredient': "Blue Toadshade",       'amount': uncommonMax,        'additionalRules': "Find 2x the rolled 'amount'"},
    10:{'ingredient': "Wrackwort Bulbs",      'amount': uncommonMax},
    11:{'ingredient': "Hydrathistle",         'amount': uncommonMax,        'additionalRules': "Find 2x the rolled 'amount' in rain"},
    12:{'ingredient': "Primordial Balm",      'amount': rareMax}
}
# underdark 'ingredient's
underdarkTable = {
    2:{'ingredient': "Primordial Balm",      'amount': rareMax,            'additionalRules': "Find 1'Difficulty': -2x the rolled 'amount'"},
    3:{'ingredient': "Silver Hibiscus",      'amount': uncommonMax},
    4:{'ingredient': "Devil's Bloodleaf",    'amount': uncommonMax},
    5:{'ingredient': "Chromus Slime",        'amount': uncommonMax},
    6:{'ingredient': "Mortflesh Powder",     'amount': commonMax,          'additionalRules': "Find 2x the rolled 'amount'"},
    7:{'ingredient': "Fennel Silk",          'amount': commonMax},
    8:{'ingredient': "Fiend's Ivy",          'amount': commonMax},
    9:{'ingredient': "Gengko Brush",         'amount': uncommonMax},
    10:{'ingredient': "Luminous Cap Dust",    'amount': uncommonMax,        'additionalRules': "Find 2x the rolled 'amount'"},
    11:{'ingredient': "Radiant Synthseed",    'amount': uncommonMax},
    12:{'ingredient': "Wisp Stalks",          'amount': rareMax}
}



class Herbalism:
    def __init__(self):
          # rules state chance of special roll is 75-100 on a d100 if 2d6 comes up 2,3,4,10,11,12. This is roughly a 1-9 on a d100 overall chance
        # settings for various amounts

        # change to false if you don't want to auto-roll 'Rarity': ''Rarity': 'Common',', ingredients
        self.autoRollIfCommon = True,
                # mapping between terrain name and ingredient tables
        self.terrainTable = {
            'common': commonTable,
            'arctic': arcticTable,
            'underwater': underwaterTable,
            'coastal': underwaterTable,
            'desert': desertTable,
            'forest': forestTable,
            'grasslands': grasslandsTable,
            'hills': hillsTable,
            'mountain': mountainTable,
            'swamp': swampTable,
            'underdark': underdarkTable
        }
        
        self.description = {
            'Bloodgrass':{
            'Rarity': 'Common',
            'Effect': 'Can combine with any other Potion Effect ingredient to become a food source for 1 day. Cannot be altered by other ingredients.',
            'Difficulty': 0},

            'Chromus Slime':{
            'Rarity': 'Rare',
            'Effect': 'The final Effect after all other calculations is the exact opposite. This is up to the DM’s discretion on the specifics per potion/poison.',
            'Difficulty': 4},

            'Dried Ephedra':{
            'Rarity': 'Uncommon',
            'Effect': 'Increase the dice-type by 1 size for any healing Effect.',
            'Difficulty':2},

            'Emetic Wax':{
            'Rarity': 'Common',
            'Effect': 'Delay the Effect of an ingredient this was combined with by 1d6 rounds',
            'Difficulty':1},

            'Fennel Silk':{
            'Rarity': 'Common',
            'Effect': 'Stabilizes body heat to resist cold weather or wet condition penalties for 1 hour. Cannot be altered by other ingredients.',
            'Difficulty':2},

            'Gengko Brush':{
            'Rarity': 'Uncommon',
            'Effect':' Double the dice rolled of any healing Effect, but divide the total of the dice by 2 (rounding down); Then, the recipient receives that amount of healing per round for 2 rounds.',
            'Difficulty':2},

            'Hyancinth Nectar':{
            'Rarity': 'Common',
            'Effect': 'Removes 1d6 rounds of poison in the target’s system, but cannot remove it completely. One round of poison damage will still occur at minimum.',
            'Difficulty':1},

            'Lavender Sprig':{
            'Rarity': 'Common',
            'Effect': 'Makes the potion or toxin more stable and safer to craft.',
            'Difficulty': -2},

            'Mandrake Root':{
            'Rarity': 'Common',
            'Effect': 'Reduce any disease or poison’s potency by half for 2d12 hours. Only hinders already existing poisons or diseases in the body. Cannot be altered by other ingredients.',
            'Difficulty':0},

            'Milkweed Seeds':{
            'Rarity': 'Common',
            'Effect': 'Double the dice rolled of any healing Effect, but remove all Alchemy Modifier bonuses. This modifier can stack.',
            'Difficulty':2},

            'Wild Sageroot':{
            'Rarity': 'Common',
            'Effect': 'Heals for 2d4 + Alchemy Modifier.',
            'Difficulty':0},

            'Arctic Creeper':{
            'Rarity': 'Common',
            'Effect': 'Change poison damage to cold or necrotic damage; target is still [poisoned] for 1 minute on a failed CON saving throw; this toxin is still considered poison damage when combining with other ingredients.',
            'Difficulty':2},

            'Amanita Cap':{
            'Rarity': 'Common',
            'Effect': 'Changes any poison Effect to be non-lethal and only incapacitate the target.',
            'Difficulty':1},

            'Basilisk Breath':{
            'Rarity': 'VeryRare',
            'Effect': 'Slowly paralyzes opponent. Target makes a DC 5 + Alchemy Modifier CON saving throw each turn for 4 turns. While under this affect, target is considered slowed by the slow spell. On a failed save, the target is considered [paralyzed] for 4 rounds. Cannot be modified or altered by other ingredients.',
            'Difficulty':5},

            'Cactus Juice':{
            'Rarity': 'Common',
            'Effect':'The target will not notice any poison damage Effect in their system until they take 5 rounds of damage from the toxin.',
            'Difficulty':2},

            'Chromus Slime':{
            'Rarity': 'Rare',
            'Effect': 'The final Effect after all other calculations is the exact opposite. This is up to the DM’s discretion on the specifics per potion/poison.',
            'Difficulty':4},

            'Drakus Flower':{
            'Rarity': 'Common',
            'Effect': 'Change poison damage to fire or acid damage; target is still [poisoned] for 1 minute on a failed CON saving throw; this toxin is still considered poison damage when combining with other ingredients.',
            'Difficulty':2},

            'Emetic Wax':{
            'Rarity': 'Common',
            'Effect': 'Delay the Effect of an ingredient this was combined with by 1d6 rounds.',
            'Difficulty':2},

            'Frozen Seedlings':{
            'Rarity': 'Rare',
            'Effect': 'While [poisoned], target’s movement speed is reduced by 10 ft for 1 minute. Cannot be altered by other ingredients.',
            'Difficulty':4},

            'Harrada Leaf':{
            'Rarity': 'Common',
            'Effect': 'While [poisoned], target has disadvantage on ability checks. Cannot be altered by other ingredients.',
            'Difficulty':1},

            'Lavender Sprig':{
            'Rarity': 'Common',
            'Effect': 'Makes the potion or toxin more stable and safer to craft.',
            'Difficulty': -2},

            'Quicksilver Lichen':{
            'Rarity': 'Uncommon',
            'Effect': 'Double the dice rolled of any Toxin Effect, but reduce that Effect duration by half. This modifier can stack.',
            'Difficulty':3},

            'Radiant Synthseed':{
            'Rarity': 'Rare',
            'Effect': 'Change poison damage to radiant damage; target is still [poisoned] for 1 minute on a failed CON saving throw; this toxin is still considered poison damage when combining with other ingredients.',
            'Difficulty':2},

            'Spineflower Berries':{
            'Rarity': 'Uncommon',
            'Effect': 'Increase the dice-type by 1 size for any Toxin Effect.',
            'Difficulty':3},

            'Wyrmtongue Petals':{
            'Rarity': 'Common',
            'Effect': '1d4 + Alchemy Modifier poison damage per round; target is [poisoned] for 1 minute.',
            'Difficulty':0},

            'Arrow Root':{
            'Rarity': 'Uncommon',
            'Effect': '+1 to attack rolls for one minute when applied to a weapon.',
            'Difficulty':2},

            'Blue Toadshade':{
            'Rarity': 'Rare',
            'Effect': 'User creates a potion of gaseous form (DMG 187).',
            'Difficulty':3},

            'Cosmos Glond':{
            'Rarity': 'Rare',
            'Effect': 'User creates a potion of clairvoyance (DMG 187).',
            'Difficulty':3},

            'Devil’s Bloodleaf':{
            'Rarity': 'VeryRare',
            'Effect': 'User creates a potion of vitality (DMG 188).',
            'Difficulty':5},

            'Fiend’s Ivy':{
            'Rarity': 'Rare',
            'Effect': 'User creates a potion of mind reading (DMG 188).',
            'Difficulty':4},

            'Hydrathistle':{
            'Rarity': 'Uncommon',
            'Effect': 'User creates a potion of water breathing (DMG 188).',
            'Difficulty':2},

            'Ironwood Heart':{
            'Rarity': 'Uncommon',
            'Effect': 'User creates a potion of growth (DMG 187).',
            'Difficulty':3},

            'Luminous Cap Dust':{
            'Rarity': 'Rare',
            'Effect': 'User creates a potion of heroism (DMG 188).',
            'Difficulty':4},

            'Mortflesh Powder':{
            'Rarity': 'VeryRare',
            'Effect': 'User creates a potion of longevity (DMG 188).',
            'Difficulty':5},

            'Nightshade Berries':{
            'Rarity': 'Uncommon',
            'Effect': 'The effect of this “potion” is similar to the oil of slipperiness (DMG 184).',
            'Difficulty':3},

            'Primordial Balm':{
            'Rarity': 'Rare',
            'Effect': 'User creates a potion of frost/fire/stone giant strength (DMG 187).',
            'Difficulty':4},

            'Rock Vine':{
            'Rarity': 'Rare',
            'Effect': 'User creates a potion of invulnerability (DMG 188).',
            'Difficulty':4},

            'Scillia Beans':{
            'Rarity': 'Common',
            'Effect': 'User creates a potion of climbing (DMG 187).',
            'Difficulty':1},

            'Silver Hibiscus':{
            'Rarity': 'Rare',
            'Effect': 'When consumed by target, they can unleash a random elemental breathe weapon 3 times (PHB 34). Cannot be altered by other ingredients.',
            'Difficulty':4},

            'Tail Leaf':{
            'Rarity': 'VeryRare',
            'Effect': 'User creates a potion of speed (DMG 188).',
            'Difficulty':5},

            'Verdant Nettle':{
            'Rarity': 'Uncommon',
            'Effect': 'User creates a potion of animal friendship (DMG 187).',
            'Difficulty':2},

            'Voidroot':{
            'Rarity': 'VeryRare',
            'Effect': 'User creates a potion of flying (DMG 187).',
            'Difficulty':5},

            'Wisp Stalks':{
            'Rarity': 'VeryRare',
            'Effect': 'User creates a potion of invisibility (DMG 188).',
            'Difficulty':5},

            'Wrackwort Bulbs':{
            'Rarity': 'Rare',
            'Effect': 'User creates a potion of diminution (DMG 187).',
            'Difficulty':4},
            }
        # change to true if you want to auto-reroll bloodgrass
        # Table Entries
        # 'Rarity': ''Rarity': 'Common',', ingredients


        
    @classmethod        
    def rollOnTable(self,terrainTable,description): 
        terrain =str(input('Enter terrain: (common, hills, swamp, forest, mountain, arctic, grasslands, desert, underwater, underdark)'))
        terrainTable = terrainTable[terrain]
        roll = randint(1,6) + randint(1,6);
        entry = terrainTable[roll]
        print(['terrain:', terrain])
        print(['roll: ', str(roll)])
        print(entry)
        if entry['ingredient']!='Common':
            print(description[entry['ingredient']])
        
herb = Herbalism()
terrainTable = herb.terrainTable
description = herb.description

herb.rollOnTable(terrainTable,description)