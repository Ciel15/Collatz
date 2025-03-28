import streamlit as st

# --- Inverse Pattern Generator ---
def generate_inverse_pattern(limit, w, y, z):
    output = []

    for x in range(1, limit + 1):
        v = x * w
        line = f"{x} = ({v} / {w})"

        if x % 2 == 0:
            if y != 0 and (x - z) % y == 0:
                a = (x - z) // y
                line += f" = ({a} x {y} + {z})"

        output.append(line)

    return output

# --- Streamlit UI ---
st.set_page_config(page_title="Inverse Pattern Generator", layout="centered")
st.title("1. Inverse Pattern Generator")

with st.form("pattern_form"):
    limit = st.number_input("Limit", min_value=1, value=100)
    w = st.number_input("W (Multiplier, usually 2)", value=2)
    y = st.number_input("Y (Divisor Check, usually 3)", value=3)
    z = st.number_input("Z (Offset, usually 1)", value=1)
    line_window = st.slider("Visible Lines", min_value=10, max_value=100, value=30)
    submitted_pattern = st.form_submit_button("Generate Pattern")

if submitted_pattern:
    pattern = generate_inverse_pattern(limit, w, y, z)
    st.text_area("Generated Pattern", "\n".join(pattern), height=line_window * 20)
