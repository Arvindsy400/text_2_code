import streamlit as st
import openai
import getpass

# Streamlit app
def main():
    st.title("CodeGPT")
    st.write('The app uses the OpenAI API to interact with the GPT-3.5 model and \
             retrieves the generated code. It also includes exception handling code specific \
             to each programming language, ensuring that the generated code is equipped to handle any\
              runtime errors or exceptions that may occur during execution.')

    # Ask for OpenAI API key
    st.subheader("OpenAI API key")
    openai_api_key = st.text_input("Enter your OpenAI API key", type="password")
    if openai_api_key:
        openai.api_key = openai_api_key
        st.success("API key entered successfully.")
    else:
        st.warning("Please enter your OpenAI API key.")
        return

    # User input text
    text_input = st.text_area("Enter text to convert into code")

    # Language selection
    language = st.selectbox("Select programming language", ["Python", "R", "JavaScript", "Java", "C", "C++", "Go"])

    # Generate code on button click
    if st.button("Generate Code"):
        # Call OpenAI API to generate code
        prompt = f"Convert the following text into {language} code:\n\n{text_input}\n\nCode:"
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=2000,
            temperature=0.7,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0,
            n=1,
            stop=None
        )
        generated_code = response.choices[0].text.strip()

        # Display generated code
        st.code(generated_code, language=language.lower())

        # Clear OpenAI API key from memory
        openai.api_key = None
        openai_api_key = None

if __name__ == '__main__':
    main()