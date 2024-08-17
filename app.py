import streamlit as st

st.write('## Responsive Layout Example')

# Create two columns
col1, col2 = st.columns([1, 2])

with col1:
    st.image('https://raw.githubusercontent.com/samberubz/mtl.slopes/main/Capture1.png', caption='Image in Column 1', use_column_width=True)

with col2:
    st.write("This is some text next to the image. It will automatically adjust based on the screen size.")

st.write('## End of Example')
st.write('**Hey!**')

