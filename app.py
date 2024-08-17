import streamlit as st

st.write('test ok')
# URL of the image from your GitHub repository
image_url = 'https://github.com/samberubz/mtl.slopes/blob/main/Capture1.png'

# Display the image in Streamlit
st.image(image_url, caption='My Image from GitHub', use_column_width=True)

