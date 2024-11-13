import streamlit as st
from fakedex_functions import *

trainer_teams = {
    "Red": ["Pikachu", "Charizard", "Venusaur", "Blastoise", "Snorlax", "Lapras"],
    "Blue": ["Pidgeot", "Alakazam", "Rhydon", "Arcanine", "Gyarados", "Exeggutor"],
    "Ash Ketchum": ["Pikachu", "Charizard", "Bulbasaur", "Squirtle", "Snorlax", "Butterfree"],
    "Ash Ketchum World Champion": ["Pikachu", "Dragonite", "Gengar", "Lucario", "Sirfetch’d", "Dracovish"],
    "Misty": ["Starmie", "Staryu", "Psyduck", "Gyarados", "Togepi", "Corsola"],
    "Brock": ["Onix", "Geodude", "Vulpix", "Crobat", "Forretress", "Ludicolo"],
    "Giovanni": ["Rhydon", "Nidoking", "Nidoqueen", "Dugtrio", "Persian", "Kangaskhan"],
    "Ethan": ["Cyndaquil", "Totodile", "Chikorita", "Lugia", "Ho-Oh", "Tyranitar"],
    "Silver": ["Sneasel", "Golbat", "Houndoom", "Tyranitar", "Feraligatr", "Lugia"],
    "Lance": ["Dragonite", "Aerodactyl", "Gyarados", "Charizard", "Dragonite", "Dragonite"],
    "Jasmine": ["Steelix", "Magnemite", "Lanturn", "Forretress", "Magnezone", "Scizor"],
    "Clair": ["Kingdra", "Dragonair", "Dratini", "Gyarados", "Lugia", "Charizard"],
    "May": ["Blaziken", "Beautifly", "Skitty", "Venusaur", "Munchlax", "Wartortle"],
    "Steven Stone": ["Metagross", "Aggron", "Skarmory", "Claydol", "Armaldo", "Cradily"],
    "Wallace": ["Milotic", "Gyarados", "Seaking", "Luvdisc", "Swampert", "Lileep"],
    "Maxie": ["Mightyena", "Camerupt", "Houndoom", "Zubat", "Aggron", "Charizard"],
    "Archie": ["Mightyena", "Sharpedo", "Gyarados", "Wailord", "Crawdaunt", "Surskit"],
    "Wally": ["Ralts", "Kirlia", "Gardevoir", "Swellow", "Altaria", "Gallade"],
    "Lucas": ["Turtwig", "Piplup", "Chimchar", "Luxray", "Garchomp", "Staraptor"],
    "Dawn": ["Piplup", "Buneary", "Pachirisu", "Mamoswine", "Quilava", "Togekiss"],
    "Barry": ["Infernape", "Staraptor", "Luxray", "Roselia", "Floatzel", "Empoleon"],
    "Cynthia": ["Garchomp", "Lucario", "Milotic", "Spiritomb", "Togekiss", "Roserade"],
    "Volkner": ["Luxray", "Electivire", "Raichu", "Magneton", "Jolteon", "Zekrom"],
    "Saturn": ["Toxicroak", "Golbat", "Bronzong", "Honchkrow", "Electivire", "Gliscor"],
    "Cyrus": ["Dialga", "Palkia", "Giratina", "Weavile", "Honchkrow", "Electivire"],
    "Hilbert": ["Snivy", "Tepig", "Oshawott", "Zoroark", "Emolga", "Leavanny"],
    "Hilda": ["Snivy", "Tepig", "Oshawott", "Zoroark", "Lilligant", "Simisear"],
    "Cheren": ["Snivy", "Patrat", "Pansear", "Pignite", "Watchog", "Zoroark"],
    "Bianca": ["Tepig", "Oshawott", "Musharna", "Vanilluxe", "Blitzle", "Simipour"],
    "N": ["Reshiram", "Carracosta", "Zoroark", "Archeops", "Klinklang", "Vanilluxe"],
    "Ghetsis": ["Hydreigon", "Cofagrigus", "Seviper", "Zoroark", "Volcarona", "Darmanitan"],
    "Iris": ["Haxorus", "Excadrill", "Emolga", "Dragonite", "Gible", "Hydreigon"],
    "Serena": ["Delphox", "Pancham", "Sylveon", "Braixen", "Jigglypuff", "Vaporeon"],
    "Calem": ["Fennekin", "Chespin", "Froakie", "Lugia", "Gardevoir", "Charizard"],
    "Shauna": ["Chespin", "Talonflame", "Sylveon", "Leavanny", "Lilligant", "Hawlucha"],
    "Tierno": ["Squirtle", "Magikarp", "Butterfree", "Corphish", "Starmie", "Swampert"],
    "Trevor": ["Chespin", "Tropius", "Zorua", "Magmar", "Flabébé", "Zygarde"],
    "Diantha": ["Gardevoir", "Aurorus", "Meowstic", "Hawlucha", "Tyranitar", "Aegislash"],
    "Lysandre": ["Gyarados", "Magnezone", "Houndoom", "Honchkrow", "Pyroar", "Chandelure"],
    "Alain": ["Mega Charizard X", "Krookodile", "Bisharp", "Zygarde", "Metagross", "Talonflame"],
    "Elio": ["Rowlet", "Popplio", "Litten", "Lycanroc", "Solgaleo", "Toucannon"],
    "Selene": ["Litten", "Popplio", "Rowlet", "Toxapex", "Gumshoos", "Torterra"],
    "Hau": ["Litten", "Raichu", "Dartrix", "Toucannon", "Gumshoos", "Shinotic"],
    "Lillie": ["Solgaleo", "Lunala", "Mimikyu", "Nihilego", "Jangmo-o", "Minior"],
    "Professor Kukui": ["Rowlet", "Primeape", "Nihilego", "Lycanroc", "Solgaleo", "Toucannon"],
    "Guzma": ["Golisopod", "Ariados", "Pinsir", "Scizor", "Salandit", "Hoothoot"],
    "Victor": ["Sobble", "Galarian Farfetch'd", "Zamazenta", "Greedent", "Corviknight", "Inteleon"],
    "Gloria": ["Grookey", "Meowth", "Zamazenta", "Bede", "Cinderace", "Zygarde"],
    "Hop": ["Wooloo", "Dubwool", "Corviknight", "Snorlax", "Pincurchin", "Zamazenta"],
    "Marnie": ["Morpeko", "Grimmsnarl", "Toxicroak", "Scrafty", "Liepard", "Galarian Moltres"],
    "Bede": ["Galarian Ponyta", "Hatterene", "Machoke", "Zacian", "Galarian Weezing", "Alcremie"],
    "Leon": ["Charizard", "Aegislash", "Dragapult", "Mr. Rime", "Haxorus", "Seismitoad"],
    "Rose": ["Charizard", "Magnezone", "Sableye", "Haxorus", "Scrafty", "Gardevoir"],
    "Juliana": ["Sprigatito", "Fuecoco", "Quaxly", "Iron Treads", "Koraidon", "Ceruledge"],
    "Florian": ["Fidough", "Meowstic", "Lechonk", "Quaxly", "Ceruledge", "Iron Treads"],
    "Nemona": ["Meowstic", "Charizard", "Armarouge", "Iron Treads", "Donphan", "Tinkaton"],
    "Arven": ["Lechonk", "Miraidon", "Flittle", "Greedent", "Eiscue", "Rabsca"],
    "Penny": ["Eevee", "Umbreon", "Sylveon", "Galarian Weezing", "Houndoom", "Gardevoir"],
    "Clavell": ["Ceruledge", "Armarouge", "Iron Treads", "Garchomp", "Pangoro", "Palafin"],
    "Ritchie": ["Pikachu", "Charmander", "Butterfree", "Mankey", "Sparky", "Squirtle"],
    "Harrison": ["Blaziken", "Donphan", "Steelix", "Feraligatr", "Pidgeot", "Lugia"],
    "Tyson": ["Meowth", "Electivire", "Linoone", "Lugia", "Snorlax", "Latios"],
    "Paul": ["Electivire", "Magmortar", "Torterra", "Weavile", "Honchkrow", "Toxicroak"],
    "Tobias": ["Darkrai", "Latios", "Mewtwo", "Registeel", "Zekrom", "Lugia"],
    "Gladion": ["Zorua", "Lycanroc", "Mimikyu", "Type: Null", "Silicobra", "Gumshoos"]
}



st.set_page_config(page_title = "Pokédex", layout = "wide")
		
# load css file and get data
local_css('style.css')
df = get_data()



# sidebar configuration for searching Pokemon by name
st.sidebar.title('Pokédex')

# Input field for partial name search
pokemon_trainer_name = st.sidebar.text_input('Search Some Famous Trainer Name', '').lower()

# Method to search for trainer names based on partial input
pokemon_trainer_matches = [trainer for trainer in trainer_teams.keys() if pokemon_trainer_name.lower() in trainer.lower()]

# Dropdown menu with pokemon_trainer_matches
if len(pokemon_trainer_matches) >= 1:
    selected_trainer = st.sidebar.selectbox("Select Trainer", pokemon_trainer_matches)
else:  # If no match, show 'No match'
    selected_trainer = st.sidebar.selectbox("Select Trainer", ['No match'])

# Check if a trainer was selected and has a valid team
if selected_trainer != 'No match':
    # Create a toggle section using an expander (hidden by default)
    with st.expander(f"{selected_trainer}'s Pokemon Team"):
        # Display each Pokémon in the trainer's team
        team = trainer_teams[selected_trainer]
        for pokemon_name in team:
            pokemon_name = transform_pokemon_name(pokemon_name)
            pokemon_info = fetch_pokemon_info(pokemon_name)
            if pokemon_info:
                st.subheader(pokemon_info["name"].capitalize(), anchor=False)
                st.image(pokemon_info["sprite"])
                st.write(f"**Pokedex ID:** {pokemon_info['id']}")
                # Extract types
                types = pokemon_info['types']
                type_text = ""

                # Dynamically generate HTML for types
                for type_ in types:
                    type_text += f'<span class="icon type-{type_.lower()}">{type_}</span> '

                # Use columns for layout
                col1, col2 = st.columns([0.2, 3])  # Adjust the width if necessary

                # First column: Static text or any other content you want
                with col1:
                    col1.write('**Type**')

                # Second column: Pokemon types with custom CSS
                with col2.container():
                    col2.markdown(type_text.strip(), unsafe_allow_html=True)

                st.write(f"**Height:** {pokemon_info['height']} decimetres")
                st.write(f"**Weight:** {pokemon_info['weight']} hectograms")
else:
    st.write("No trainer found matching your input.")


name = st.sidebar.text_input('Search Name', '').lower() # input name
# find names that matches input and return it in a list
matches = list(df[df['name'].str.lower().str.contains(name)]['name'])
# dropdown menu with names that matches input
if len(matches) >= 1:
	name = st.sidebar.selectbox('Pokemon Matches', matches).lower()
else: # if no name matches input
	name = st.sidebar.selectbox('Pokemon Matches', ['No match'])

# filter row of data that matches Pokemon selected in dropdown menu
match = df[df['name'].str.lower() == name]

# select information to view
info_list = ['Basic Information', 'Base Stats & Type Defenses', 'Training and Breeding', 'Radar Chart']
selected_info = st.sidebar.multiselect('View Information', info_list, default = info_list)

# search Pokemon using min and max base stats (speed, special defense etc.)
with st.sidebar.expander("Search Base Stats Range", expanded=False):
    min_speed, max_speed = st.select_slider("Speed", range(251), value=[0, 250])
    min_sp_def, max_sp_def = st.select_slider("Special Defense", range(251), value=[0, 250])
    min_sp_atk, max_sp_atk = st.select_slider("Special Attack", range(251), value=[0, 250])
    min_def, max_def = st.select_slider("Defense", range(251), value=[0, 250])
    min_atk, max_atk = st.select_slider("Attack", range(251), value=[0, 250])
    min_hp, max_hp = st.select_slider("HP", range(251), value=[0, 250])

    # Display a button to trigger the search
    pressed = st.button("Search Pokemon")

# You can then handle the `pressed` variable outside the expander for further processing
if pressed:
    # Code to process the search based on selected stats
    st.write("Searching for Pokémon with the specified base stats range...")

# display credits on sidebar
st.sidebar.subheader('Credits')
st.sidebar.write("I've gather the data from these links below, where you can find more information about the source utilized on this page.")
st.sidebar.markdown('Pokemon dataset taken from <a href="https://www.kaggle.com/datasets/mariotormo/complete-pokemon-dataset-updated-090420?select=pokedex_%28Update_04.21%29.csv">this Kaggle link</a>.', unsafe_allow_html = True)
st.sidebar.markdown("**Why some pokemons isn't showing in Search Name?**")
st.sidebar.markdown('''As you can see in the dataset, the last pokemon with data is Calyrex Shadow Rider, 
                    so for now, any newest pokemon will be avaliable.''')

if not pressed:
	if len(match) == 0:
		st.write('Enter name to search for details.')
	
	elif len(match) == 1:
		if 'Basic Information' in selected_info:
			show_basic_info(match)
		if 'Base Stats & Type Defenses' in selected_info:
			show_base_stats_type_defenses(match)
		if 'Training and Breeding' in selected_info:
			show_training_breeding(match)
		if 'Radar Chart' in selected_info:
			show_radar_chart(match)
			
else:
	# get base stats of all Pokemon
	df_stats_all = df[['name', 'hp', 'attack', 'defense', 'sp_attack', 'sp_defense', 'speed']].set_index('name')
	df_stats_all = df_stats_all.rename(columns={'hp': 'HP', 'attack': 'Attack', 'defense': 'Defense', 'sp_attack': 'Special Attack', 'sp_defense': 'Special Defense', 'speed': 'Speed'})
	# filter stats according to search criteria from the sliders
	searched_pokemons_df = df_stats_all[
		(df_stats_all['HP'] >= min_hp) & (df_stats_all['HP'] <= max_hp) &
		(df_stats_all['Attack'] >= min_atk) & (df_stats_all['Attack'] <= max_atk) &
		(df_stats_all['Defense'] >= min_def) & (df_stats_all['Defense'] <= max_def) &
		(df_stats_all['Special Attack'] >= min_sp_atk) & (df_stats_all['Special Attack'] <= max_sp_atk) &
		(df_stats_all['Special Defense'] >= min_sp_def) & (df_stats_all['Special Defense'] <= max_sp_def) &
		(df_stats_all['Speed'] >= min_speed) & (df_stats_all['Speed'] <= max_speed)										
	]
	st.header('Pokemon Search Using Base Stats')
	st.table(searched_pokemons_df)

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
