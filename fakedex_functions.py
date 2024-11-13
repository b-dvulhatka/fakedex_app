import streamlit as st
from PIL import Image
from io import BytesIO
import numpy as np
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt
import requests
import re

def fetch_pokemon_info(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            "name": data["name"],
            "id": data["id"],
            "types": [t["type"]["name"] for t in data["types"]],
            "height": data["height"],
            "weight": data["weight"],
            "sprite": data["sprites"]["other"]["showdown"]["front_default"]
        }
    else:
        return None
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

@st.cache_resource
def get_data():

	return pd.read_csv('pokedex.csv', keep_default_na = False).iloc[:1046] 

def show_basic_info(match):

	name = match['name'].iloc[0]
	id = match['pokedex_number'].iloc[0]
	height = str(match['height_m'].iloc[0])
	weight = str(match['weight_kg'].iloc[0])
	species = ' '.join(match['species'].iloc[0].split(' ')[:-1])
	type1 = match['type_1'].iloc[0]
	type2 = match['type_2'].iloc[0]
	type_number = match['type_number'].iloc[0]
	ability1 = match['ability_1'].iloc[0]
	ability2 = match['ability_2'].iloc[0]
	ability_hidden = match['ability_hidden'].iloc[0]
	
	st.title(name + ' #' + str(id).zfill(3), anchor=False)
	col1, col2, col3 = st.columns(3)
	

	try:
		name = name.lstrip()
		name = transform_pokemon_name(name)
		url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
		response = requests.get(url)
		if response.status_code == 200:
			data = response.json()
			

			sprites_pokemon = [
				data["sprites"]["other"]["showdown"]["front_default"],
				data["sprites"]["other"]["showdown"]["back_default"],
				data["sprites"]["other"]["showdown"]["front_shiny"],
				data["sprites"]["other"]["showdown"]["back_shiny"],
			]
			

			cols = st.columns(len(sprites_pokemon))
			

			for i, sprite in enumerate(sprites_pokemon):
				cols[i].image(sprite)
			

			return {
				"sprites_pokemon": sprites_pokemon
			}
	except:
		col1.write('Image not available in PokeAPI.')
	
	
	with col2.container():		
		col2.write('Type')

		type_text = f'<span class="icon type-{type1.lower()}">{type1}</span>'
		if type_number == 2:
			type_text += f' <span class="icon type-{type2.lower()}">{type2}</span>'

		col2.markdown(type_text, unsafe_allow_html=True)
		col2.metric("Height", height + " m")
		col2.metric("Weight", weight + " kg")
	

	with col3.container():
		col3.metric("Species", species)
		col3.write('Abilities')
		if ability1 != '':
			col3.subheader(ability1)
		if ability2 != '':
			col3.subheader(ability2)
		if ability_hidden != '':
			col3.subheader(ability_hidden + ' (Hidden)')

def show_base_stats_type_defenses(match):

	weakness_2_types = []
	weakness_4_types = []
	resistance_half_types = []
	resistance_quarter_types = []
	

	for i, j in match.iterrows():
		for column, value in j.items():
			if column.startswith('against_'):
				type = column.split('_')[1]
				if value == 0.5:
					resistance_half_types.append(type)
				elif value == 0.25:
					resistance_quarter_types.append(type)
				elif value == 2:
					weakness_2_types.append(type)
				elif value == 4:
					weakness_4_types.append(type)
					
	with st.container():	
		col1, col2 = st.columns(2)	
		

		col1.subheader('Base Stats', anchor=False)

		df_stats = match[['hp', 'attack', 'defense', 'sp_attack', 'sp_defense', 'speed']]
		df_stats = df_stats.rename(columns={'hp': 'HP', 'attack': 'Attack', 'defense': 'Defense', 'sp_attack': 'Special Attack', 'sp_defense': 'Special Defense', 'speed': 'Speed'}).T
		df_stats.columns=['stats']
		

		fig, ax = plt.subplots()
		ax.barh(y = df_stats.index, width = df_stats.stats)
		plt.xlim([0, 250])
		col1.pyplot(fig)
		

		col2.subheader('Type Defenses', anchor=False)
		col2.write('Strong Weaknesses (x4)')	
		weakness_text = ''
		for type in weakness_4_types:
			weakness_text += f' <span class="icon type-{type}">{type}</span>'
		col2.markdown(weakness_text, unsafe_allow_html=True)		
		col2.write('Weaknesses (x2)')	
		weakness_text = ''
		for type in weakness_2_types:
			weakness_text += f' <span class="icon type-{type}">{type}</span>'
		col2.markdown(weakness_text, unsafe_allow_html=True)
		
		col2.write('Resistances (x0.5)')
		resistance_half_text = ''
		for type in resistance_half_types:
			resistance_half_text += f' <span class="icon type-{type}">{type}</span>'
		col2.markdown(resistance_half_text, unsafe_allow_html=True)
		
		col2.write('Strong Resistances (x0.25)')
		resistance_quarter_text = ''
		for type in resistance_quarter_types:
			resistance_quarter_text += f' <span class="icon type-{type}">{type}</span>'
		col2.markdown(resistance_quarter_text, unsafe_allow_html=True)


def show_training_breeding(match):	

	catch_rate = match['catch_rate'].iloc[0]
	base_friendship	= match['base_friendship'].iloc[0] 
	base_experience	= match['base_experience'].iloc[0]
	growth_rate = match['growth_rate'].iloc[0]
	

	egg_type_number = match['egg_type_number'].iloc[0]
	egg_type_1	= match['egg_type_1'].iloc[0] 
	egg_type_2	= match['egg_type_2'].iloc[0]
	percentage_male = match['percentage_male'].iloc[0]
	egg_cycles = match['egg_cycles'].iloc[0]
		
	with st.container():
		col1, col2 = st.columns(2)
		

		col1.subheader('Training', anchor=False)		
		col1.metric('Catch Rate', catch_rate)
		col1.metric('Base Friendship', base_friendship)
		col1.metric('Base Experience', base_experience)
		col1.metric('Growth Rate', growth_rate)
		

		col2.subheader('Breeding', anchor=False)		
		if egg_type_number == 2:
			col2.metric('Egg Types', egg_type_1 + ', ' + egg_type_2)
		else:
			col2.metric('Egg Types', egg_type_1)
		if percentage_male != '':	
			percentage_female = str(100 - float(match['percentage_male'].iloc[0]))		
			col2.metric('Percentage Male/Female', percentage_male + '% / ' + percentage_female + '%' )
		else:

			col2.metric('Percentage Male/Female', 'NA')
		col2.metric('Egg Cycles', egg_cycles)
			
def show_radar_chart(match):
	st.header('Radar Chart of Base Stats', anchor=False)

	df_stats = match[['hp', 'attack', 'defense', 'sp_attack', 'sp_defense', 'speed']]
	df_stats = df_stats.rename(columns={'hp': 'HP', 'attack': 'Attack', 'defense': 'Defense', 'sp_attack': 'Special Attack', 'sp_defense': 'Special Defense', 'speed': 'Speed'}).T
	df_stats.columns=['stats']
	

	fig = px.line_polar(df_stats, r='stats', theta=df_stats.index, line_close=True, range_r=[0, 250])
	st.plotly_chart(fig)
	
	if st.button('Search for Pokemons with Similar Base Stats'):
		show_similar_pokemons(match)

def show_similar_pokemons(match):
    df = get_data()

    df_stats = match[['hp', 'attack', 'defense', 'sp_attack', 'sp_defense', 'speed']]
    df_stats = df_stats.rename(columns={'hp': 'HP', 'attack': 'Attack', 'defense': 'Defense', 'sp_attack': 'Special Attack', 'sp_defense': 'Special Defense', 'speed': 'Speed'})
    

    df_stats_all = df[['name', 'hp', 'attack', 'defense', 'sp_attack', 'sp_defense', 'speed']].set_index('name')
    df_stats_all = df_stats_all.rename(columns={'hp': 'HP', 'attack': 'Attack', 'defense': 'Defense', 'sp_attack': 'Special Attack', 'sp_defense': 'Special Defense', 'speed': 'Speed'})
    

    diff_df = pd.DataFrame(df_stats_all.values - df_stats.values, index=df_stats_all.index)
    

    norm_df = diff_df.apply(np.linalg.norm, axis=1)

    similar_pokemons = norm_df.nsmallest(6)[1:7].index

    similar_pokemons_df = df_stats_all.loc[similar_pokemons]
    

    for row in similar_pokemons_df.iterrows():
        name = row[0]
        st.subheader(name, anchor=False)
        
        try:
            name = transform_pokemon_name(name)
            url = f"https://pokeapi.co/api/v2/pokemon/{name}"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                image_url = data["sprites"]["other"]["official-artwork"]["front_default"]

                if image_url:
                    image_response = requests.get(image_url)
                    image = Image.open(BytesIO(image_response.content))
                    st.image(image)
                else:
                    st.write("Image not available.")
            else:
                st.write("Failed to retrieve Pokémon data.")
        except Exception as e:
            st.write("Error loading image:", e)
        

        fig = px.line_polar(
            pd.Series(row[1], index=row[1].index), 
            r=row[1].values, 
            theta=row[1].index, 
            line_close=True, 
            range_r=[0, 255]
        )
        st.plotly_chart(fig)
    
    st.subheader('5 Most Similar Pokemons', anchor=False)
    st.table(similar_pokemons_df)
def transform_pokemon_name(name):

    name = name.lower()
    
    if "♀" in name:
        name = name.replace("♀", "-f")
    if "♂" in name:
        name = name.replace("♂", "-m")
    name = re.sub(r"[^a-z0-9\s-]", "", name)  


    if " rotom" in name:
        words = name.split()
        reversed_name = " ".join(reversed(words))
        return reversed_name.replace(" ", "-").strip()
    
    if "deoxys" in name and "forme" in name:
        return name.replace(" forme", "").replace(" ", "-").strip()

    if "forme" in name:
        return name.replace(" forme","").replace(" ", "-")
    if "zygarde" in name and "forme" in name:
        if "10%" in name:
            return "zygarde-10"
        if "50%" in name:
            return "zygarde-50"
        if "complete" in name:
            return "zygarde-complete"

    if " mega-y" in name:
        return name.replace(" mega-y", "-mega-y").strip()
    if " mega-x" in name:
        return name.replace(" mega-x", "-mega-x").strip()
    if "mega " in name:
        name = name.replace("mega ", "")
        return f"{name}-mega".strip()

    if " cloak" in name:
        return name.replace(" cloak", "").replace(" ", "-").strip()

    if "primal " in name:
        return name.replace("primal ", "") + "-primal".strip()

    if "galarian " in name:
        name = name.replace("galarian ", "")
        if "mr mime" in name:
            return "mr-mime-galar"
        return f"{name}-galar".strip()

    if "galar" in name:
        return name.replace(" galar", "-galar").strip()

    if "alolan" in name:
        return name.replace("alolan ", "") + "-alola".strip()

    if "calyrex" in name and "rider" in name:
        return name.replace(" rider", "").replace(" ", "-").strip()

    if "'" in name:
        return name.replace("'", "").strip()

    if "lycanroc " in name and "form" in name:
        if "midday" in name:
            return "lycanroc-midday".strip()
        if "midnight" in name:
            return "lycanroc-midnight".strip()
        if "dusk" in name:
            return "lycanroc-dusk".strip()

    if "aegislash" in name and "forme" in name:
        if "shield" in name:
            return "aegislash-shield".strip()
        if "blade" in name:
            return "aegislash-blade".strip()

    if "urshifu" in name and "style" in name:
        return name.replace(" style", "").replace(" ", "-").strip()

    if "crowned shield" in name or "crowned sword" in name:
        return name.replace(" crowned shield", "-crowned").replace(" crowned sword", "-crowned").strip()

    if "hero of many battles" in name:
        return name.replace(" hero of many battles", "").strip()

    if "wishiwashi" in name and "form" in name:
        return name.replace(" form", "").strip()

    if "morpeko" in name and "mode" in name:
        return name.replace(" mode", "").strip()

    if "eiscue" in name and "face" in name:
        return name.replace(" face", "").strip()

    if "necrozma" in name:
        if "dawn" in name:
            return "necrozma-dawn".strip()
        if "dusk" in name:
            return "necrozma-dusk".strip()
        if "ultra" in name:
            return "necrozma-ultra".strip()

    if "mr mime" in name or "mr rime" in name:
        return name.replace(" ", "-").strip()

    if "type null" in name:
        return name.replace("type null", "type-null").strip()

    if " style" in name:
        return name.replace(" style", "").replace(" ", "-")

    if "mimikyu" in name:
        return "mimikyu-disguised"
        
    if " " in name:
        return name.replace(" ", "-")
    return name.strip()

def get_image_url_from_pokeapi(name_or_id):
    url = f"https://pokeapi.co/api/v2/pokemon/{name_or_id}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data["sprites"]["other"]["official-artwork"]["front_default"]
    else:
        return None

	