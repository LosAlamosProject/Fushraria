#oblika ID : DATA
#za blokove koji su unbreakable staviti veliki hardness i breaksound null
#za sad su slike i zvuci placeholderi
#breaktime je u fps-u
#hardness je koji tier toola treba da se razbije tipa 1-5 wood stone iron diamond niggerium
Block_Dict = {
    0 : {"block_name" : "Air" , "breaking_time" : 0 , "breaking_tool" : "null", "hardness" : 1000, "texture" : "air.png" , "walk_sound" : "null", "break_sound" : "null"},
    1 : {"block_name" : "Dirt" , "breaking_time" : 60 , "breaking_tool" : "shovel", "hardness" : 1, "texture" : "dirt.png" , "walk_sound" : "dirtwalk.ogg", "break_sound" : "dirtbreak.ogg"},
    2 : {"block_name" : "Stone" , "breaking_time" : 120 , "breaking_tool" : "pickaxe", "hardness" : 1, "texture" : "stone.png" , "walk_sound" : "stonewalk.ogg", "break_sound" : "stonebreak.ogg"},
    3 : {"block_name" : "Bedrok" , "breaking_time" : 0 , "breaking_tool" : "null", "hardness" : 6969, "texture" : "bedrock.png" , "walk_sound" : "bedrock.ogg", "break_sound" : "null"}
}
