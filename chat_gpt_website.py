import streamlit as st

def main():
    # Set page layout
    st.set_page_config(layout="wide")

    # Sidebar (left empty space for advertising)
    left_sidebar = st.sidebar.empty()

    # Main content (information regarding LLMs)
    st.title("How to Make Money with ChatGPT")
    st.write("Welcome to the 'How to Make Money with ChatGPT' section!")
    st.write("Here you can find valuable information on monetizing ChatGPT.")

    # Add your content on monetizing ChatGPT here
    st.write("Step 1: ...")
    st.write("Step 2: ...")
    st.write("Step 3: ...")

    # Sidebar (right empty space for advertising)
    right_sidebar = st.sidebar.empty()

    # Insert the AdSense ad code
    ad_code = """
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-4777786136450145"
     crossorigin="anonymous"></script>
    """
    st.components.v1.html(ad_code, height=250)

    # Custom CSS to hide the GitHub logo
    custom_css = """
    <style>
    #MainMenu {
        visibility: hidden;
    }
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
