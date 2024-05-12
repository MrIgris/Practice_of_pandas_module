import pandas as pd
#accessing dataset
 
credit_of_movies = pd.read_csv("credits.csv")
print(credit_of_movies)
#Acessing data set single name column 

names = credit_of_movies["name"]
print(names)
#dictionary into data frame

dict_1 = {
    'Assault Rifles': ['AK-47', 'M4A1', 'M16A2', 'SCAR-L', 'FN FAL'],
    'Shotguns': ['Remington 870', 'Mossberg 500', 'Winchester 1200', 'Benelli M4', 'Franchi Affinity'],
    'Sniper Rifles': ['Barrett.50cal', 'M24', 'M40A3', 'Dragunov SVD', 'L96A1'],
    'Handguns': ['Glock 19', 'Smith & Wesson M&P', 'Sig Sauer P226', 'Beretta 92FS', 'Colt 1911'],
    'Machine Guns': ['M249 SAW', 'M60', 'M2 Browning', 'PKM', 'RPK'],
    'Carbines': ['M4 Carbine', 'CAR-15', 'XM177', 'HK416', 'SIG MCX'],
    'Submachine Guns': ['MP5', 'Uzi', 'MAC-10', 'PPSh-41', 'Sten'],
    'Rifles': ['M14', 'M1 Garand', 'Lee-Enfield', 'Mosin-Nagant', 'Karabiner 98k'],
    'Pistols': ['Beretta 92', 'Glock 17', 'Sig Sauer P220', 'Colt Python', 'Walther P38'],
    'Revolver': ['Smith & Wesson Model 29', 'Colt Python', 'Ruger GP100', 'Smith & Wesson Model 10', 'Colt Single Action Army'],
    'Anti-Tank Rifles': [' Boys Anti-Tank Rifle', 'Lahti L-39', 'PTRS-41', 'Wz. 35 anti-tank rifle', 'Solothurn S-18/100'],
    'Anti-Material Rifles': ['Barrett M95', 'McMillan Tac-50', 'CheyTac Intervention', 'Denel NTW-20', 'ZVI Falcon'],
    'Grenade Launchers': ['M203', 'M320', 'M79', 'Mk 19', 'AGS-30'],
    'Rocket Launchers': ['RPG-7', 'M47 Dragon', 'M72 LAW', 'AT4', 'Panzerfaust 3'],
    'Machine Pistols': ['Uzi', 'MAC-10', 'Sten', 'MP 40', 'PPSh-41'],
    'Carbine Rifles': ['M1 Carbine', 'M2 Carbine', 'M3 Carbine', 'SKS', 'z. 52 rifle'],
    'Battle Rifles': ['M14', 'M1 Garand', 'Lee-Enfield', 'Mosin-Nagant', 'Karabiner 98k'],
    'Designated Marksman Rifles': ['Mk 12 SPR', 'M24', 'M40A3', 'Dragunov SVD', 'L96A1'],
    'Semi-Automatic Rifles': ['AR-15', 'AK-47', 'M14', 'M1 Garand', 'Lee-Enfield']
}

df_guns = pd.DataFrame(dict_1)
print(df_guns)
# data frame from a 9x9 2d array with specific rows and columns from a dictionary

anime_manhwa = [
    ['Naruto', 'Bleach', 'One Piece', 'Death Note', 'Attack on Titan', 'Tower of God', 'Noblesse', 'The God of High School', 'Kubera'],
    ['Fullmetal Alchemist', 'Cowboy Bebop', 'Samurai Champloo', 'Trigun', 'Ghost in the Shell', 'Girls of the Wild\'s', 'The Gamer', 'DICE', 'UnOrdinary'],
    ['Sailor Moon', 'Fruits Basket', 'Cardcaptor Sakura', 'Magic Knight Rayearth', 'Venus Project', 'Priest', 'Id', 'Dead End', 'Her Majesty\'s Swarm'],
    ['Akira', 'Ghost in the Shell', 'Paranoia Agent', 'Ergo Proxy', 'Psycho-Pass', 'The Breaker', 'Ability', 'The Remarried Empress', 'Omniscient Reader'],
    ['Nana', 'Honey and Clover', 'aradise Kiss', 'Solanin', 'Honey Mustard', 'Omniscient Reader', 'The Remarried Empress', 'Her Majesty\'s Swarm', 'Surviving as the'],
    ['Omniscient Reader', 'The Remarried Empress', 'Her Majesty\'s Swarm', 'Surviving as the Hero\'s Wife', 'Dead End', 'Priest', 'Id', 'The Breaker', 'Ability'],
    ['The God of High School', 'Kubera', 'Tower of God', 'Noblesse', 'Girls of the Wild\'s', 'The Gamer', 'DICE', 'UnOrdinary', 'The S-Classes That I Raised'],
    ['Death Note', 'Attack on Titan', 'One Piece', 'Bleach', 'Naruto', 'Fullmetal Alchemist', 'Cowboy Bebop', 'Samurai Champloo', 'Trigun'],
    ['Dragon Ball Z', 'Yu Yu Hakusho', 'Rurouni Kenshin', 'Inuyasha', 'Neon Genesis Evangelion', 'Ghost in the Shell', 'Akira', 'Paranoia Agent', 'Ergo Proxy']
]  
col_labels = ['Anime 1', 'Anime 2', 'Anime 3', 'Anime 4', 'Anime 5', 'Manhwa 1', 'Manhwa 2', 'Manhwa 3', 'Manhwa 4']
row_labels = ['Shonen','Shonen','Shojo','Seinen','Josei','Manhwa','Manhwa','Anime','Anime']
df_anime = pd.DataFrame(data = anime_manhwa,index=row_labels ,columns=col_labels )
print(df_anime)
#Series from a list 

sword_users = [
    'Himura Kenshin',
    'Guts',
    'Miyamoto Musashi',
    'Manji',
    'Clare',
    'Inuyasha',
    'Jubei Yagyu',
    'Mugen',
    'Nanashi',
    'Kirito',
    'Saber',
    'Shichika Yasuri',
    'Iwamoto Kogan',
    'Yashiro Isana',
    'Akame',
    'Goblin Slayer',
    'Thorfinn',
    'Parn',
    'Meliodas',
    'Gennosuke Kouga'
]

anime = [
    'Rurouni Kenshin',
    'Berserk',
    'Vagabond',
    'Blade of the Immortal',
    'Claymore',
    'Inuyasha',
    'Ninja Scroll',
    'Samurai Champloo',
    'Sword of the Stranger',
    'Sword Art Online',
    'Fate/stay night',
    'Katanagatari',
    'Shigurui',
    'K',
    'Akame ga Kill!',
    'Goblin Slayer',
    'Vinland Saga',
    'Record of Lodoss War',
    'The Seven Deadly Sins',
    'Basilisk'
]
series = pd.Series(data=sword_users,index=anime)
print(series)
print(type(series))

#AAcessing 

print(series.index)
print(series.ndim)
print(series.shape)
print(series.size)

#using ind3ex to access a series
# series[] and loc uses index
print(series["Berserk"])  
print(series["K"])  
print(series['Berserk':"K"])

print(series.loc["Berserk"])  
print(series.loc["K"])  
print(series.loc["Berserk":"K"])
# iloc uses location
print(series.iloc[1])  
print(series.iloc[3])  
print(series.iloc[3:8])

#negative index

print(series.iloc[-1])
#series of a single valiue

v = pd.Series(data = 106)
print(v)
#creating an empty series

v1 = pd.Series(dtype=int)
print(v1)
#adding two series with same index
anime = pd.Series(['Rurouni Kenshin','Berserk', 'Vagabond', 'Blade of the Immortal', 'Claymore', 'Inuyasha', 'Ninja Scroll', 'Samurai Champloo', 'Sword of the Stranger', 'Sword Art Online', 'Fate/stay night', 'Katanagatari', 'Shigurui', 'K', 'Akame ga Kill!', 'Goblin Slayer', 'Vinland Saga', 'Record of Lodoss War', 'The Seven Deadly Sins', 'Basilisk'])
space = pd.Series(["+","+","+","+","+","+","+","+","+","+","+","+","+","+","+","+","+","+","+","+"])
characters = pd.Series(['Himura Kenshin', 'Guts', 'Miyamoto Musashi', 'Manji', 'Clare', 'Inuyasha', 'Jubei Yagyu', 'Mugen', 'Nanashi', 'Kirito', 'Saber', 'Shichika Yasuri', 'Iwamoto Kogan', 'Yashiro Isana', 'Akame', 'Goblin Slayer', 'Thorfinn', 'Parn', 'Meliodas', 'Gennosuke Kouga'])
result = anime + space + characters
print(result)

# with different index

s1 = pd.Series([1.1, 2.2, 3.3,4.4,5.9,6.9], index=[0,1,2,3,4,5])
s2 = pd.Series([4.4, 5.5, 6.6, 7.7,8.8,9.9], index=[0,3,4,5,6,7])
s3 = s1 + s2

print(s1)
print(s2)
print(s3)

# now using .add for addition
print(s1.add(s2, fill_value=0.0))

print(s1.add(s2, fill_value=10.0))
