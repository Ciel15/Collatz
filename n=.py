import streamlit as st

#1
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

#2
def generate_inverse_branch(x, w, y, z):
    steps = []

    line = f"{x} = ({x * w} / {w})"
    if y != 0 and (x - z) % y == 0:
        a = (x - z) // y
        if a != 0:
            line += f" = ({a} x {y} + {z})"
    steps.append(line)

    if x % 2 == 0:
        x = x // 2
    else:
        x = 3 * x + 1

    while x != 1:
        line = f"{x} = ({x * w} / {w})"
        if y != 0 and (x - z) % y == 0:
            a = (x - z) // y
            if a != 0:
                line += f" = ({a} x {y} + {z})"
        steps.append(line)

        if x % 2 == 0:
            x = x // 2
        else:
            x = 3 * x + 1

    steps.append(f"1 = ({1 * w} / {w})")  # only this format for 1
    return steps

#3
def generate_pattern(start, step, count):
    return [start + i * step for i in range(count)]

#1
st.set_page_config(page_title="Collatz + Pattern Tools", layout="centered")
st.title("Collatz + Inverse Pattern Tools")

st.header("1. Inverse Pattern Generator")
with st.form("pattern_form"):
    limit = st.number_input("Limit", min_value=1, value=100)
    w = st.number_input("W (Multiplier, usually 2)", value=2)
    y = st.number_input("Y (Divisor Check, usually 3)", value=3)
    z = st.number_input("Z (Offset, usually 1)", value=1)
    line_window = st.slider("Visible Lines (Height)", min_value=10, max_value=100, value=30)
    submitted_pattern = st.form_submit_button("Generate Pattern")

if submitted_pattern:
    pattern = generate_inverse_pattern(limit, w, y, z)
    st.text_area("Generated Pattern", "\n".join(pattern), height=line_window * 20)

#2
st.header("2. Collatz Branch (Full Trace to 1)")

with st.form("branch_form"):
    w = st.number_input("W (Multiplier, usually 2)", value=2, key="w_branch")
    y = st.number_input("Y (Divisor Check, usually 3)", value=3, key="y_branch")
    z = st.number_input("Z (Offset, usually 1)", value=1, key="z_branch")
    start = st.number_input("Starting number", min_value=1, value=7)
    branch_submit = st.form_submit_button("Generate Collatz Branch")

if branch_submit:
    steps = generate_inverse_branch(start, w, y, z)
    output_text = "\n".join(str(step) for step in steps)
    height_value = max(200, min(len(steps), 50) * 20)
    st.text_area("Collatz Branch Output", output_text, height=height_value)

#3
st.title("f(n) = m x n + o")

start = st.number_input("Enter starting number:", value=1)
step = st.number_input("Enter step size:", value=10)
count = st.number_input("How many steps:", value=23)

if st.button("Generate"):
    pattern = generate_pattern(start, step, count)
    st.write("Generated Pattern:")
    st.write(pattern)
