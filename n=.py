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
lines_to_display = st.number_input("How many lines to show in the output window", min_value=1, value=20)

if st.button("Generate"):
    result = generate_inverse_pattern(limit, w, y, z)
    result_str = "\n".join(result[:lines_to_display])

    st.text_area("Output", result_str, height=300)
