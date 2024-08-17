import streamlit as st

# Set the page configuration to wide mode
st.set_page_config(layout="wide")
# URL of the image from your GitHub repository
image_url = 'https://raw.githubusercontent.com/samberubz/mtl.slopes/main/Capture1.png'
# Display the image in Streamlit
st.image(image_url, use_column_width=True)

st.write('**Hey!**')
st.write('© S. Bérubé, 2024')

