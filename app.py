import tensorflow as tf
import streamlit as st
import json

# Streamlit app title and description
st.title("Superhero Name Generator")
st.write("Enter a seed string of at least two characters, and the model will generate a superhero name!")

# Load model and mappings with caching
@st.cache_resource
def load_model_and_mappings():
    # Load the trained model
    model = tf.keras.models.load_model("superheromodel_v2.keras")
    
    # Load index-to-character mapping as exported from the trained model
    with open("index_to_char.json", "r") as f:
        index_to_char = json.load(f)

    # Load character-to-index mapping as exported from the trained model
    with open("char_to_index.json", "r") as f:
        char_to_index = json.load(f)

    return model, index_to_char, char_to_index

# Load the model and mappings
model, index_to_char, char_to_index = load_model_and_mappings()

# Parameters for sequence padding
max_len = 33  # Matching the model's training configuration

# Function to generate superhero names
def generate_names(seed):
    # Helper function to convert seed string to a sequence
    def name_to_seq(name):
        return [char_to_index[char] for char in name if char in char_to_index]

    # Generate the name
    for _ in range(33):  # Maximum of 40 iterations
        seq = name_to_seq(seed)
        padded = tf.keras.preprocessing.sequence.pad_sequences(
            [seq], maxlen=max_len - 1, padding="pre", truncating="pre"
        )

        # Predict the next character
        pred = model.predict(padded, verbose=0)[0]
        pred_char = index_to_char[str(tf.argmax(pred).numpy())]
        seed += pred_char

        # Stop generation if the predicted character is the end token
        if pred_char == "\t": 
            break

    return seed.strip()

# User input for seed string
user_input = st.text_input("Enter a seed word or phrase:", "")

if user_input:
    # Generate superhero name
    superhero_name = generate_names(user_input)

    # Display result
    st.write("Generated Superhero Name:")
    st.write(superhero_name)