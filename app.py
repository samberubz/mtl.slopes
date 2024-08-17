import streamlit as st

# Set the page configuration to wide mode
st.set_page_config(layout="wide")


# URL of the image from your GitHub repository
image1_url = 'https://raw.githubusercontent.com/samberubz/mtl.slopes/main/Capture1.png'
image2_url = 'https://raw.githubusercontent.com/samberubz/mtl.slopes/main/Capture2.png'
# Display the image in Streamlit
st.image(image1_url, use_column_width=True)
# Custom HTML and CSS for the rectangle with a purple border, transparent background,
# and text color that adapts to the user's theme
st.markdown(
    """
    <style>
    .custom-box {
        background-color: transparent;
        border: 2px solid #d4a5ff;
        border-radius: 15px;
        padding: 20px;
        margin: 20px 0;
    }
    </style>
    <div class="custom-box">
        <strong>Hey! This is an app designed for all of you skiers! 🎿</strong><br><br>
        <em>*That includes casual gliders, bunny hill specialists, downhill experts, etc. ☃️</em>
    </div>
    """,
    unsafe_allow_html=True
)
st.write('This app gathers ski conditions from three well-known stations located within a 2-hour drive from Montreal Montreal \n'
         'making it your perfect single-stop destination before hitting the slopes). 🚗 \n'
         'Look, I summarized the main points for you below. 🏔️')
st.write('©2024, Samuel Bérubé, P.Eng., M.A.Sc.')

# Display the image in Streamlit
st.image(image2_url, use_column_width=True)

