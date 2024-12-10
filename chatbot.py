import streamlit as st 
import nltk 
from nltk.chat.util import Chat, reflections



#Setting the data
data = [[r"(.*Hi|.*Hello|.*Hey|.*What's up)", ["Hello! How can I help you today?", "Hi there! What's on your mind?", "Hey! Feel free to ask me anything."]],
        [r"(.*name)", ["My name is Uthman"]], 
        [r"(.*age|.*old)", ["I am 450 years old, but I am still a very agile 😉."]],
        [r"(.*colour|.*color)", ["My favourite colour is White ⚪."]],
        [r"(.*sport)", ["I am a huge fan of Football ⚽, Basketball 🏀 and Tennis 🎾."]],
        [r"(.*skills)", ["I am skilled in Python, Power BI, Machine Learning and SQL."]],
        [r"(.*hobbies|.*interests|.*interest)", ["I am really interested in sports⚽, coding💻 and Economic theories."]],
        [r"(.*yourself|.*brief|.*about)", [" Economics graduate with a strong foundation in statistical analysis, economic modeling, and data science. Skilled in Python, Power BI, and SQL, with hands-on experience in machine learning, data visualization, and handling large datasets. Adept at uncovering insights through advanced analytics to support data-driven decision-making. Passionate about applying economic principles and cutting-edge data science techniques to solve real-world challenges in areas like market analysis, financial forecasting, and business optimization."]]

]


#Creating the chatbot

chatbot =  Chat(data, reflections)

def main():
    st.title("Chatbot Interface")
    st.write("Hello! I'm your chatbot. Type your question below. Type 'exit' to end the conversation.")

    user_input = st.text_input("You: ")

    if user_input.lower() == 'exit' :
        st.write("Chatbot: Goodbye!!")
        st.stop()
    elif user_input.strip():
        response = chatbot.respond(user_input)
        if response:
            st.write(f"Chatbot: {response}")
        else:
            st.write("Chatbot: I could not understand your statement, kindly rephrase your statement")


if __name__ == "__main__":
    main()
        


