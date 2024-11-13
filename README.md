# Fakedex Application

This project is a web application built using Streamlit that serves as a Pokédex, allowing users to search for Pokémon and view detailed information about them. The application also includes a feature to explore famous Pokémon trainers and their teams.

## Features

Search Pokémon by Name: Users can search for Pokémon by entering their names. The application will display detailed information about the selected Pokémon, including its types, height, weight, and sprite images.
Explore Trainer Teams: Users can search for famous Pokémon trainers and view their teams. The application provides detailed information about each Pokémon in the trainer's team.
View Pokémon Information: The application provides various details about Pokémon, including basic information, base stats, type defenses, training and breeding information, and a radar chart of base stats.
Search by Base Stats: Users can search for Pokémon based on a range of base stats, such as HP, attack, defense, special attack, special defense, and speed.

## File Structure

app.py: The main application file that sets up the Streamlit interface and handles user interactions.
fakedex_functions.py: Contains various utility functions used in the application, such as fetching Pokémon data and transforming Pokémon names.
style.css: Contains custom CSS styles for the application.

## Data Sources

Pokémon dataset: Kaggle Pokémon Dataset

## Credits

The data used in this application is sourced from Kaggle. Based on the research I've conducted, this is the most comprehensive data available for this type of project.

## Notes

The application currently supports Pokémon data up to Calyrex Shadow Rider. Newer Pokémon may not be available in the dataset.
The application uses the PokeAPI to fetch additional Pokémon information and images.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
