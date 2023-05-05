# sets = collection of data which is unordered,unindexed, no duplicate values

games = {"Minecraft", "Roblox", "Lego"}
games_2 = {"Fortnite", "PUBG", "freefire", "Lego"}

games.add("Clash of clans")
games.remove("Roblox")
# games.clear()
# games_2.update(games)   ## both are the same
# games.update(games_2)   ## both are the same 

Total_games = games.union(games_2)  ## combines the both data as same as before

print(games.difference(games_2))
print(games_2.difference(games))

print(games.intersection(games_2))  ## cheaks whether the data has any common in them

for data in Total_games:
    print(data)