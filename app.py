{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "d98ab194-71d6-4dbe-b4dd-d2cc681705d2",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2024-12-29 00:19:28.348126: I tensorflow/core/platform/cpu_feature_guard.cc:182] This TensorFlow binary is optimized to use available CPU instructions in performance-critical operations.\n",
      "To enable the following instructions: AVX2 FMA, in other operations, rebuild TensorFlow with the appropriate compiler flags.\n"
     ]
    }
   ],
   "source": [
    "import tensorflow as tf\n",
    "import streamlit as st\n",
    "\n",
    "st.title(\"Superhero Name Generator\")\n",
    "st.write(\"Enter a seed string of at least two characters, and the model will generate a superhero name!\")\n",
    "\n",
    "@st.cache_resource\n",
    "def load_model():\n",
    "    # Load the trained model\n",
    "    model = tf.keras.models.load_model(\"superheromodel_v2.keras\")\n",
    "    \n",
    "    return model\n",
    "\n",
    "model = load_model()\n",
    "\n",
    "def generate_names(seed):\n",
    "    # Directly use the model to predict a superhero name based on the seed\n",
    "    generated_name = model.generate_names(seed) \n",
    "    return generated_name\n",
    "\n",
    "# User input for seed string\n",
    "user_input = st.text_input(\"Enter a seed word or phrase:\", \"\")\n",
    "\n",
    "if user_input:\n",
    "    # Generate superhero name\n",
    "    superhero_name = generate_names(user_input)\n",
    "\n",
    "    # Display result\n",
    "    st.write(\"Generated Superhero Name:\")\n",
    "    st.write(superhero_name)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:anaconda3]",
   "language": "python",
   "name": "conda-env-anaconda3-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
