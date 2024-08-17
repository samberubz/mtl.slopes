import streamlit as st

# Set the page configuration to wide mode
st.set_page_config(layout="wide", base="dark")


# URL of the image from your GitHub repository
image1_url = 'https://raw.githubusercontent.com/samberubz/mtl.slopes/main/Capture1.png'
image2_url = 'https://raw.githubusercontent.com/samberubz/mtl.slopes/main/Capture2.png'
# Display the image in Streamlit
st.image(image1_url, use_column_width=True)
# Custom HTML and CSS for the purple rectangle with rounded corners
st.markdown(
    """
    <div style="
        background-color: #d4a5ff; 
        border-radius: 15px; 
        padding: 20px; 
        margin: 20px 0;
        color: #4b0082;
        box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.1);
    ">
        <strong>Hey! This is an app designed for all of you skiers! :skier:</strong><br><br>
        <em>That includes casual gliders, bunny hill specialists, downhill experts, etc. :snowman:</em><br><br>
        It gathers ski conditions from three well-known stations located within a 2-hour drive from Montreal 
        (making it your perfect single-stop destination before hitting the slopes). :car: <br><br>
        Look, I summarized the main points for you below. :snow_capped_mountain:
    </div>
    """,
    unsafe_allow_html=True
)

st.write('©2024, Samuel Bérubé, P.Eng., M.A.Sc.')

# Display the image in Streamlit
st.image(image2_url, use_column_width=True)

