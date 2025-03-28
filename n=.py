import streamlit as st

def generate_inverse_pattern(limit, w, y, z):
    output = []

    for x in range(1, limit + 1):
        v = x * w
        line = f"{x} = ({v} / {w})"

        if x % 2 == 0:
            if y != 0 and (x - z) % y == 0:
                a = (x - z) // y
                line += f" = ({a} • {y} + {z})"

        output.append(line)

    return output

# Streamlit interface
st.title("Inverse Pattern Generator")

limit = st.number_input("Limit", min_value=1, value=100)
w = st.number_input("W (default 2)", value=2)
y = st.number_input("Y (default 3)", value=3)
z = st.number_input("Z (default 1)", value=1)

line_window = st.slider("Visible Lines in Output Window", min_value=5, max_value=30, value=10)

if st.button("Generate"):
    result = generate_inverse_pattern(limit, w, y, z)
    output_text = "\n".join(result)
    st.text_area("Output", output_text, height=line_window * 20, max_chars=None)
