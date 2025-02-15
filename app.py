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


#Define healthcare-specific response logic (or use a mmodel to generate responses)
def healthcare_chatbot(user_input):
    #Simple rule-based keywords to respond
    if "symptom" in user_input:
        return "Please consult Doctor for accurate advice"
    elif "appointment" in user_input:
        return "Would you like to schedule appointment with the Doctor?"
    elif "medication" in user_input:
        return "It's important to take prescribed medicines regularly. If you have concerns, consult a dostor."
    else:
        #For other input, use the Hugging face model to generate a response
        response = chatbot(user_input,max_length = 300,num_return_sequences=1)
        #specifies the maximum length of the generated text response, including the input and the generated tokens.
        #If set to 3, the model generated three different possible responses based on the input.
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
            st.write("User : ",user_input)
            with st.spinner("Processing your query, Please wait ... "):
                response=healthcare_chatbot(user_input)
            st.write("Healthcare Assistant : ",response)
        else:
            st.write("please enter a message to get a response.")

if __name__ == "__main__":
    main()