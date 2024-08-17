import streamlit as st

# Set the page configuration to wide mode
st.set_page_config(layout="wide")

# URL of the image from your GitHub repository
image1_url = 'https://raw.githubusercontent.com/samberubz/mtl.slopes/main/Capture1.png'
image2_url = 'https://raw.githubusercontent.com/samberubz/mtl.slopes/main/Capture2.png'
# Display the image in Streamlit
st.image(image1_url, use_column_width=True)

st.write('**Hey! This is an app designed for all of you advanced (and not so advanced) skiers!**\n\n'
         'It currently gathers ski conditions from three well-known stations located within a 2-hour drive from Montreal.\n\n'
         'Look, I summarized the main points for you...')
st.write('©2024, Samuel Bérubé, P.Eng., M.A.Sc.')

# Display the image in Streamlit
st.image(image2_url, use_column_width=True)

