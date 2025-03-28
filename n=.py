import streamlit as st

# --- Section 1: Inverse Pattern Generator ---
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

# --- Section 2: Collatz Branch Path Generator ---
def generate_branch_path(start, steps):
    """
    Traces a Collatz branch for a set number of steps,
    printing each number and its relationship to the previous one.
    Marks (3n + 1) cases where applicable.
    """
    path = [start]
    output = []

    for _ in range(steps):
        current = path[-1]
        next_val = None

        if current % 2 == 0:
            next_val = current // 2
            line = f"{current} = ({current * 2} / 2)"
        else:
            raw = 3 * current + 1
            divs = 0
            temp = raw
            while temp % 2 == 0:
                temp //= 2
                divs += 1
            next_val = temp

            if (next_val * 3 + 1) == (3 * current + 1):
                line = f"{current} = ({(3 * current + 1)} / {2 ** divs}) = ({next_val} x 3 + 1)"
            else:
                line = f"{current} = ({(3 * current + 1)} / {2 ** divs})"

        output.append(line)
        path.append(next_val)

    return output

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

# --- Section 2: Collatz Branch Viewer ---
st.header("2. Collatz Branch Viewer")
with st.form("branch_form"):
    start = st.number_input("Starting number", min_value=1, value=1)
    steps = st.number_input("Steps to trace", min_value=1, value=20)
    branch_submit = st.form_submit_button("Trace Collatz Branch")

if branch_submit:
    branch = generate_branch_path(start, steps)
    st.text_area("Collatz Branch Output", "\n".join(branch), height=steps * 20)
