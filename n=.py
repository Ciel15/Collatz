import streamlit as st

def generate_inverse_pattern(limit, w, y, z):
    output = []
    output_for_copy = []

    for x in range(1, limit + 1):
        v = x * w
        line = f"{x} = ({v} / {w})"
        copy_line = f"{x} = ({v} / {w})"

        if x % 2 == 0:
            if y != 0 and (x - z) % y == 0:
                a = (x - z) // y
                line += f" = ({a} • {y} + {z})"
                copy_line += f" = ({a} x {y} + {z})"

        output.append(line)
        output_for_copy.append(copy_line)

    return output, output_for_copy

# Streamlit interface
st.title("Cardinal ((xy)+z) Generator")

limit = st.number_input("Limit", min_value=1, value=100)
w = st.number_input("W (Collatz: 2)", value=2)
y = st.number_input("Y (Collatz: 3)", value=3)
z = st.number_input("Z (Collatz: 1)", value=1)

line_window = st.slider("Visible Lines for Output Window", min_value=25, max_value=100, value=50)

if st.button("Generate"):
    result_display, result_copy = generate_inverse_pattern(limit, w, y, z)
    output_text = "\n".join(result_display)
    output_text_copy = "\n".join(result_copy)

    st.text_area("x = (x / w) = (x • y + z) Output:", output_text, height=line_window * 20, max_chars=None)

    with st.expander("Copy-Friendly Version"):
        st.text_area("Copy This (• becomes 'x'):", output_text_copy, height=line_window * 20, max_chars=None)
        st.download_button("Download as .txt", output_text_copy, file_name="pattern_output.txt")
