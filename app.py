import random
import streamlit as st
Roles = ["Top", "Jungle", "Mid", "Bot", "Sup"]
Champions = ["Aatrox", "Ahri", "Akali", "Akshan", "Alistar", "Ambessa", "Amumu",
    "Anivia", "Annie", "Aphelios", "Ashe", "Aurelion Sol", "Aurora", "Azir",
    "Bard", "Bel'Veth", "Blitzcrank", "Brand", "Braum", "Briar",
    "Caitlyn", "Camille", "Cassiopeia", "Cho'Gath", "Corki",
    "Darius", "Diana", "Dr. Mundo", "Draven",
    "Ekko", "Elise", "Evelynn", "Ezreal",
    "Fiddlesticks", "Fiora", "Fizz",
    "Galio", "Gangplank", "Garen", "Gnar", "Gragas", "Graves", "Gwen",
    "Hecarim", "Heimerdinger", "Hwei",
    "Illaoi", "Irelia", "Ivern",
    "Janna", "Jarvan IV", "Jax", "Jayce", "Jhin", "Jinx",
    "Kai'Sa", "Kalista", "Karma", "Karthus", "Kassadin", "Katarina",
    "Kayle", "Kayn", "Kennen", "Kha'Zix", "Kindred", "Kled", "Kog'Maw",
    "K'Sante",
    "LeBlanc", "Lee Sin", "Leona", "Lillia", "Lissandra", "Lucian", "Lulu", "Lux",
    "Malphite", "Malzahar", "Maokai", "Master Yi", "Mel", "Milio",
    "Miss Fortune", "Mordekaiser", "Morgana",
    "Naafiri", "Nami", "Nasus", "Nautilus", "Neeko", "Nidalee",
    "Nilah", "Nocturne", "Nunu & Willump",
    "Olaf", "Orianna", "Ornn",
    "Pantheon", "Poppy", "Pyke",
    "Qiyana", "Quinn",
    "Rakan", "Rammus", "Rek'Sai", "Rell", "Renata Glasc", "Renekton",
    "Rengar", "Riven", "Rumble", "Ryze",
    "Samira", "Sejuani", "Senna", "Seraphine", "Sett", "Shaco",
    "Shen", "Shyvana", "Singed", "Sion", "Sivir", "Skarner",
    "Smolder", "Sona", "Soraka", "Swain", "Sylas", "Syndra",
    "Tahm Kench", "Taliyah", "Talon", "Taric", "Teemo", "Thresh",
    "Tristana", "Trundle", "Tryndamere", "Twisted Fate", "Twitch",
    "Udyr", "Urgot",
    "Varus", "Vayne", "Veigar", "Vel'Koz", "Vex", "Vi", "Viego",
    "Viktor", "Vladimir", "Volibear",
    "Warwick", "Wukong",
    "Xayah", "Xerath", "Xin Zhao",
    "Yasuo", "Yone", "Yorick", "Yuumi",
    "Zac", "Zed", "Zeri", "Ziggs", "Zilean", "Zoe", "Zyra"]
Starter = ["Cull", "Dark Seal", "Doran's Blade", "Doran's Bow", "Doran's Helm", "Doran's Ring", "Doran's Shield"]
Boots = ["Plated Steelcaps", "Mercury's Treads", "Ionian Boots of Lucidity", "Sorcerer's Shoes", "Boots of Swiftness"]
Items = ["Abyssal Mask", "Actualizer", "Archangel's Staff", "Ardent Censer", "Atma's Reckoning", "Axiom Arc", "Bandlepipes",
         "Banshee's Veil", "Bastionbreaker", "Black Cleaver", "Blackfire Torch", "Blade of the Ruined King", "Bloodletter's Curse",
         "Bloodthirster", "Chempunk Chainsword", "Cosmic Drive", "Cryptbloom", "Dawncore", "Dead Man's Plate", "Death's Dance", "Diadem of Songs",
         "Dream Maker", "Dusk and Dawn", "Echoes of Helia", "Eclipse", "Edge of Night", "Endless Hunger", "Essence Reaver", "Experimental Hexplate",
         "Fiendhunter Bolts", "Fimbulwinter", "Force of Nature", "Frozen Heart", "Guardian Angel", "Guinsoo's Rageblade", "Heartsteel",
         "Hexoptics C44", "Hextech Gunblade", "Hextech Rocketbelt", "Hollow Radiance", "Horizon Focus", "Hubris", "Hullbreaker", "Iceborn Guantlet",
         "Immortal Shieldbow", "Imperial Mandate", "Infinity Edge", "Jak'Sho The Protean", "Kaenic Rookern", "Knight's Vow", "Kraken Slayer",
         "Liandry's Torment", "Lich Bane", "Locket of the Iron Solari", "Lord Dominik's Regards", "Luden's Echo", "Malignance", "Manamune", "Maw of Malmortius",
         "Mejai's Soulstealer", "Mercurial Scimitar", "Mikael's Blessing", "Moonstone Renewer", "Morellonomicon", "Mortal Reminder", "Nashor's Tooth", "Navori Flickerblade",
         "Overlord's Bloodmail", "Phantom Dancer", "Profane Hydra", "Protoplasm Harness", "Rabadon's Deathcap", "Randuin's Omen", "Rapid Firecannon", "Ravenous Hydra", "Redemption",
         "Riftmaker", "Rod of Ages", "Runaan's Hurrican", "Rylai's Crystal Scepter", "Seraph's Embrace", "Serpent's", "Serylda's Grudge", "Shadowflame", "Shurelya's Battlesong", "Spear of Shojin",
         "Spirit Visage", "Staff of Flowing Water", "Statikk Shiv", "Sterak's Gage", "Stormrazor", "Stormsurge", "Stridebreaker", "Sundered Sky", "Sunfire Aegis", "Sword of Blossoming Dawn",
         "Terminus", "The Collector", "Thornmail", "Titanic Hydra", "Trinity Force", "Umbral Glaive", "Unending Despair", "Void Staff", "Voltaic Cyclosword", "Warmog's Armor", "Winter's Approach", "Wit's End",
         "Youmuu's Ghsotblade", "Yun Tal Wildarrows", "Zeke's Convergence", "Zhonya's Hourglass"]
Summoner = ["Heal", "Ghost", "Barrier", "Exhaust", "Flash", "Teleport", "Cleanse", "Ignite"]
Jungle_Summoner = ["Smite"]


st.title("League Role Randomizer")

if st.button("Generate Build"):

    Role = random.choice(Roles)
    Champion = random.choice(Champions)

    st.write("Role:", Role)
    st.write("Champion:", Champion)

    if Role == "Jungle":
        Selected_Summoners = ["Smite", random.choice(Summoner)]
    else:
        Selected_Summoners = random.sample(Summoner, 2)

    st.write("Summoners:")
    for spell in Selected_Summoners:
        st.write("-", spell)

    st.write("Starter:")
    st.write(random.choice(Starter))

    st.write("Boots:")
    st.write(random.choice(Boots))

    Build = random.sample(Items, 5)

    st.write("Items:")
    for item in Build:
        st.write("-", item)










