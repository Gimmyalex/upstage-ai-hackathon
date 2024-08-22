import streamlit as st
from openai import OpenAI

# Streamlit App UI
st.title("Solar AI Multi-Tool App")
st.sidebar.title("Choose Service")

# Widget for user to input their own API key
api_key = st.sidebar.text_input("Enter your Solar API Key:", type="password")
if not api_key:
    st.warning("Please enter your API key to continue.")
else:
    # Initialize the Upstage Solar API client using the user's API key
    client = OpenAI(
        api_key=api_key,
        base_url="https://api.upstage.ai/v1/solar"
    )

    # Set the model and system prompt
    model = "solar-1-mini-chat"
    system_prompt = {"role": "system", "content": "You are a helpful assistant."}

    # Define functions for each category
    def generate_content(prompt):
        messages = [system_prompt, {"role": "user", "content": prompt}]
        response = client.chat.completions.create(
            model=model,
            messages=messages
        )
        return response.choices[0].message.content

    def translate_text(prompt, target_language):
        messages = [system_prompt, {"role": "user", "content": f"Translate this to {target_language}: {prompt}"}]
        response = client.chat.completions.create(
            model=model,
            messages=messages
        )
        return response.choices[0].message.content

    def coding_assistant(prompt):
        messages = [system_prompt, {"role": "user", "content": f"Assist with coding: {prompt}"}]
        response = client.chat.completions.create(
            model=model,
            messages=messages
        )
        return response.choices[0].message.content

    # Select between Content Generation, Translation, and Coding Assistant
    service = st.sidebar.radio("Select Service", ["Content Generation", "Translation", "Coding Assistant"])

    if service == "Content Generation":
        st.header("Content Generation")
        content_prompt = st.text_area("Enter a prompt for content generation (e.g., product description, article topic, etc.):")
        
        if st.button("Generate Content"):
            if content_prompt:
                result = generate_content(content_prompt)
                st.write("### Generated Content")
                st.write(result)
            else:
                st.warning("Please enter a prompt for content generation.")

    elif service == "Translation":
        st.header("Translation Service")
        text_to_translate = st.text_area("Enter text to translate:")
        target_language = st.text_input("Enter target language (e.g., French, Spanish, etc.):")
        
        if st.button("Translate"):
            if text_to_translate and target_language:
                translated_text = translate_text(text_to_translate, target_language)
                st.write("### Translated Text")
                st.write(translated_text)
            else:
                st.warning("Please enter text and target language.")

    elif service == "Coding Assistant":
        st.header("Coding Assistant")
        coding_prompt = st.text_area("Enter a coding-related query (e.g., code snippet, debugging question, concept explanation):")
        
        if st.button("Get Coding Assistance"):
            if coding_prompt:
                coding_result = coding_assistant(coding_prompt)
                st.write("### Coding Assistance")
                st.write(coding_result)
            else:
                st.warning("Please enter a coding-related query.")

    # Streamlit Feedback
    sentiment_mapping = ["one", "two", "three", "four", "five"]
    selected = st.feedback("stars")
    if selected is not None:
        st.markdown(f"You selected {sentiment_mapping[selected]} star(s).")
