import streamlit as st
import pandas as pd

st.title("Multiplication Table Generator")

# Take user input
num = st.number_input("Enter a number:", min_value=1, step=1)

# Generate table when input is provided
if num:
    table = pd.DataFrame({
        "Multiplier": list(range(1, 11)),
        "Result": [num * i for i in range(1, 11)]
    })
    
    st.write(f"### Multiplication Table of {num}")
    st.table(table)

# if __name__=='__main__':
#     app.run(host="0.0.0.0", debug=True)