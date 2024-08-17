import streamlit as st

st.write('test ok')
# URL of the image from your GitHub repository
image_url = 'https://github.com/samberubz/mtl.slopes/blob/97b66563563410265b8051a2da602d5f398b3f5a/Capture1.png'

# Display the image in Streamlit
st.image(image_url, caption='My Image from GitHub', use_column_width=True)

