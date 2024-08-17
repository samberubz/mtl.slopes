import streamlit as st
import streamlit.components.v1 as components

# Set the page configuration to wide mode
st.set_page_config(layout="wide")

# Define the HTML content as a string
html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>My App</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            overflow: hidden;
        }
        img {
            max-width: 100%;
            height: auto;
        }
    </style>
</head>
<body>
    <img src="https://raw.githubusercontent.com/samberubz/mtl.slopes/main/Capture1.png" alt="Image">
</body>
</html>
"""

# Display the HTML content in Streamlit
components.html(html_content, height=600)

# URL of the image from your GitHub repository
image1_url = 'https://raw.githubusercontent.com/samberubz/mtl.slopes/main/Capture1.png'
image2_url = 'https://raw.githubusercontent.com/samberubz/mtl.slopes/main/Capture2.png'
# Display the image in Streamlit
st.image(image1_url, use_column_width=True)

st.write('**Hey!**')
st.write('©2024, Samuel Bérubé, P.Eng., M.A.Sc.')

# Display the image in Streamlit
st.image(image2_url, use_column_width=True)

