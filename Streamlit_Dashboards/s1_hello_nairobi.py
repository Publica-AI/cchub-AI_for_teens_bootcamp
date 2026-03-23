%%writefile s1_hello_nairobi.py
# Example 1: Your very first Streamlit app — Hello Nairobi!
# Run this with: streamlit run s1_hello_nairobi.py

import streamlit as st   # import the streamlit library (always use alias 'st')

# st.title() displays a large heading at the top of the page
st.title("🌍 Habari Nairobi!")

# st.write() is the Swiss army knife of Streamlit — it can display
# text, numbers, dataframes, charts, and more
st.write("Welcome to our first Streamlit app!")
st.write("Streamlit makes it easy to build interactive web apps using Python.")

# st.markdown() lets you use markdown formatting (bold, italic, bullet points)
st.markdown("""
### Why Streamlit is awesome:
- ✅ No HTML or CSS needed
- ✅ Works with pandas, matplotlib, and plotly
- ✅ Free and open source
- ✅ Used by companies like KCB, Safaricom data teams, and many more!
""")

# st.success() shows a green success box — great for positive messages
st.success("App is running successfully! Sawa sawa! 🎉")