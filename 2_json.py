import json


indian_states_and_capitals = {
    "Tamil Nadu": "Chennai",
    "Andhra Pradesh":"Amaravati",
    "Arunachal Pradesh": "Itanagar",
    "Assam": "Dispur",
    "Bihar": "Patna",
    "Karnataka": "Bengaluru",
    "Kerala": "Thiruvananthapuram"
    
}

with open(r'C:\Users\rabin\OneDrive\Pictures\Documents\assignment edyoda\assignment_6\states.json', 'w') as json_file:
    json.dump(indian_states_and_capitals, json_file)
    print("\nIndian states and capitals have been written to indian_states.json.\n")