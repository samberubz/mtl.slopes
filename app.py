import streamlit as st

# Set the page configuration to wide mode
# st.set_page_config(layout="wide")
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
        <strong>Hey Skiers! This app was designed for you! 🎿</strong><br>
        <em>"you" includes: casual gliders, bunny hill specialists, downhill experts, etc. ☃️</em>
    </div>
    """,
    unsafe_allow_html=True
)
st.write('This app gathers ski conditions from three well-known stations located within a 2-hour drive from Montreal \n'
         '(making it your perfect single-stop destination before hitting the slopes). 🚗🏔️')
# ----------------------------------------------------------------------------------------------------------------------
st.title('SECTION A - Summary')

st.markdown(
    """
    <style>
    table {
        width: 100%;
        border-collapse: collapse;
    }
    th, td {
        border: 1px solid #d4a5ff;
        padding: 8px;
        text-align: center;
    }
    th {
        background-color: #d4a5ff;
    }
    </style>
    <table>
        <thead>
            <tr>
                <th></th>
                <th>Tremblant</th>
                <th>Orford</th>
                <th>Sutton</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Current Weather</td>
                <td></td>
                <td></td>
                <td></td>
            </tr>
            <tr>
                <td>Snow (last 24h)</td>
                <td></td>
                <td></td>
                <td></td>
            </tr>
            <tr>
                <td>Snow (last 48h)</td>
                <td></td>
                <td></td>
                <td></td>
            </tr>
            <tr>
                <td>Snow (last 7d)</td>
                <td></td>
                <td></td>
                <td></td>
            </tr>
            <tr>
                <td>Snow (season total)</td>
                <td></td>
                <td></td>
                <td></td>
            </tr>
            <tr>
                <td>Total Slopes</td>
                <td></td>
                <td></td>
                <td></td>
            </tr>
            <tr>
                <td>Open Slopes (g/b/d/dd)</td>
                <td></td>
                <td></td>
                <td></td>
            </tr>
        </tbody>
    </table>
    """,
    unsafe_allow_html=True
)

st.title('SECTION B - Webcams')

st.title('SECTION C - Forecasts')

# Display the image in Streamlit
st.image(image2_url, use_column_width=True)
st.write('©2024, Samuel Bérubé, P.Eng., M.A.Sc.')

