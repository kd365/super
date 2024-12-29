import tensorflow as tf
import streamlit as st

st.title("Superhero Name Generator")
st.write("Enter a seed string of at least two characters, and the model will generate a superhero name!")

@st.cache_resource
def load_model():
    # Load the trained model
    model = tf.keras.models.load_model("superheromodel_v2.keras")
    return model

model = load_model()

def generate_names(seed):
    # Directly use the model to predict a superhero name based on the seed
    generated_name = model.generate_names(seed)
    return generated_name

# User input for seed string
user_input = st.text_input("Enter a seed word or phrase:", "")

if user_input:
    # Generate superhero name
    superhero_name = generate_names(user_input)

    # Display result
    st.write("Generated Superhero Name:")
    st.write(superhero_name)