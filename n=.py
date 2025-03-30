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

# --- Collatz Branch Tracer (correct 3n+1 logic, all /2 steps shown) ---
def generate_inverse_branch(x, w, y, z):
    steps = []
    while x != 1:
        v = x * w
        line = f"{x} = ({v} / {w})"
        
        if x % 2 == 0:
            if y != 0 and (x - z) % y == 0:
                a = (x - z) // y
                line += f" = ({a} x {y} + {z})"
            x = x // 2
        else:
            a = x * y + z
            line += f" = ({a} x {y} + {z})"
            x = a
        
        steps.append(line)

    steps.append("1")
    return steps

# --- Streamlit UI Setup ---
st.set_page_config(page_title="Collatz + Pattern Tools", layout="centered")
st.title("Collatz + Inverse Pattern Tools")

# --- Section 1: Inverse Pattern Generator ---
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

# --- Section 2: Full Collatz Branch Viewer ---
st.header("2. Collatz Branch (Full Trace to 1)")
with st.form("branch_form"):
    w = st.number_input("W (Multiplier, usually 2)", value=2, key="w_branch")
    y = st.number_input("Y (Divisor Check, usually 3)", value=3, key="y_branch")
    z = st.number_input("Z (Offset, usually 1)", value=1, key="z_branch")
    start = st.number_input("Starting number", min_value=1, value=7)
    branch_submit = st.form_submit_button("Generate Collatz Branch")

if branch_submit:
    output_text = "\n".join(branch)
st.text_area("Collatz Branch Output", output_text, height=min(len(branch), 50) * 20 if branch else 200)
