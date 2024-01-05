import streamlit as st
import openai

# Set OpenAI API key
openai.api_key = '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'

product_name = "Samsung S21"
retail_price = 1000
minimum_price = 600

# Function to update messages in the conversation
def update_chat(messages, role, content):
    messages.append({"role": role, "content": content})
    return messages

# Function to get response from the GPT model
def get_chatgpt_response(messages):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0
    )
    return response['choices'][0]['message']['content']

# Initial conversation setup
messages = [
    {"role": "system", "content": f"Your goal is to increase sales based on ${product_name}, ${retail_price} and Discounted ${minimum_price} price. Respond to the customer on ${product_name} starting with its ${retail_price}. You are required to maintain the ${minimum_price} regardless of how long the customer negotiates. Never disclose ${minimum_price} to the customer. Accept customer offers higher than previous ones and acknowledge their offer. Negotiate prices within the range of ${retail_price} and the ${minimum_price} without offering below the ${minimum_price} or disclosing the ${minimum_price}."},
    {"role": "user", "content": f"I am a customer. I want to buy ${product_name} with negotiation."},
    {"role": "assistant", "content": f"Your job is to help find deals on the ${product_name} that customers are interested in. Don't offer extra packages with the product; your goal is to sell only ${product_name}. Ensure you don't go below ${minimum_price}. Maintain an adaptive conversation flow, emphasizing the value of the product, and never disclose the ${minimum_price} during negotiations. Maintain long-term negotiations; do not instantly accept the customer offer on ${minimum_price} at first. Try to negotiate starting from ${retail_price}. In case the customer offers you a better price above ${retail_price}, then thank the customer and accept that offer."},
]

# Streamlit code
st.title("Product Sales Negotiation Chatbot")

user_input = st.text_input("Enter your message:")
messages = update_chat(messages, "user", user_input)
model_response = get_chatgpt_response(messages)
messages = update_chat(messages, "assistant", model_response)

st.text("User: " + user_input)
st.text("AI: " + model_response)
