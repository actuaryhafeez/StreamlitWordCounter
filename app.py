import streamlit as st

# Function to count the words in a string
def count_words(text):
    return len(text.split())

# Streamlit app
def main():
    # Title and description
    st.title("Word Count App")
    st.write("This app counts the number of words in a text input or in a file uploaded by the user.")

    # Text input or file upload option
    option = st.radio(
        "Select input option:",
        ("Text input", "File upload")
    )

    # Initialize text input and file variables
    text_input = ""
    file = None

    # Word count
    if option == "Text input":
        text_input = st.text_input("Enter text:")
        count = count_words(text_input)
    else:
        file = st.file_uploader("Upload a file:")
        if file is not None:
            text = file.read().decode("utf-8")
            count = count_words(text)
        else:
            count = None

    # Show word count
    if count is not None:
        st.write("Word count:", count)


    # Run the app
if __name__ == "__main__":
    main()
