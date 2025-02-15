import streamlit as st
import nltk
from transformers import pipeline
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

#Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')

#Load a pre-trained Hugging face model
chatbot = pipeline("text-generation", model="distilgpt2")

#Define healthcare-specific response logic (or use a model to generate responses)
def healthcare_chatbot(user_input):
    #Simple rule-based keywords to respond
    if "symptom" in user_input:
        return "Please consult Doctor for accurate advice"
    elif "appointment" in user_input:
        return "Would you like to schedule an appointment with the Doctor?"
    elif "medication" in user_input:
        return "It's important to take prescribed medicines regularly. If you have concerns, consult a doctor."
    elif "diet" in user_input:
        return "Maintaining a balanced diet is essential for good health. Would you like some recommendations?"
    elif "exercise" in user_input:
        return "Regular exercise is crucial for maintaining good health. Need some workout tips?"
    elif "blood pressure" in user_input:
        return "Managing blood pressure requires a proper diet and medication. Have you checked it recently?"
    elif "diabetes" in user_input:
        return "Diabetes management involves diet, exercise, and medication. Would you like to consult a specialist?"
    elif "mental health" in user_input:
        return "Mental health is important. If you are feeling stressed, consider talking to a professional."
    elif "covid" in user_input:
        return "If you have COVID-19 symptoms, consider isolating and consulting a healthcare provider."
    elif "insurance" in user_input:
        return "Would you like to check available healthcare insurance plans?"
    elif "vaccination" in user_input:
        return "Vaccination is crucial for preventing diseases. Would you like information on available vaccines?"
    elif "heart disease" in user_input:
        return "Heart disease management includes a healthy diet, exercise, and medication. Would you like tips on maintaining heart health?"
    elif "allergy" in user_input:
        return "Allergy symptoms vary. If you experience severe reactions, consult a doctor immediately."
    elif "hydration" in user_input:
        return "Staying hydrated is essential for good health. Aim for at least 8 glasses of water a day."
    elif "stress" in user_input:
        return "Managing stress involves relaxation techniques, exercise, and a balanced lifestyle. Need some tips?"
    elif "headache" in user_input:
        return "Headaches can have various causes. Rest, hydration, and stress management may help."
    elif "sleep" in user_input:
        return "Good sleep is vital for health. Try maintaining a regular sleep schedule and avoiding screens before bed."
    elif "nutrition" in user_input:
        return "Proper nutrition supports overall health. Would you like personalized dietary suggestions?"
    else:
        #For other input, use the Hugging face model to generate a response
        response = chatbot(user_input, max_length=300, num_return_sequences=1)
        return response[0]['generated_text']

#Streamlit web app interface
def main():
    #set up the web app title and input area
    st.title("Healthcare Assistant Chatbot")

    #display a simple text input and for user queries
    user_input = st.text_input("How can I assist you today?")

    #display chatbot response
    if st.button("Submit"):
        if user_input:
            st.write("User : ", user_input)
            with st.spinner("Processing your query, Please wait ... "):
                response = healthcare_chatbot(user_input)
            st.write("Healthcare Assistant : ", response)
        else:
            st.write("please enter a message to get a response.")

if __name__ == "__main__":
    main()
