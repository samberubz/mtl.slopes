import streamlit as st

# Set the page configuration to wide mode
st.set_page_config(layout="wide")
# URL of the image from your GitHub repository
image_url = 'https://raw.githubusercontent.com/samberubz/mtl.slopes/main/Capture1.png'
# Display the image in Streamlit
st.image(image_url, caption='© S. Bérubé, 2024', use_column_width=True)

st.write('**Hey!**')

