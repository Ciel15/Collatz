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

# --- Reduced Collatz T(n) Function ---
def T(n):
    if n % 2 == 0:
        raise ValueError("T(n) is only defined for odd integers.")
    result = 3 * n + 1
    while result % 2 == 0:
        result //= 2
    return result

# --- Reverse Collatz (odd-only) ---
def reverse_T(target, max_k=40):
    results = []
    for k in range(1, max_k + 1):
        candidate = target * (2 ** k) - 1
        if candidate % 3 == 0:
            n = candidate // 3
            if n % 2 == 1 and n > 0:
                results.append(n)
    return results

# --- Trace Forward Path ---
def trace_forward(start, steps):
    path = [start]
    current = start
    for _ in range(steps):
        current = T(current)
        path.append(current)
    return path

# --- Trace Backward Paths ---
def trace_backward(target, depth, max_k=40):
    def helper(n, d):
        if d == 0:
            return [[n]]
        branches = reverse_T(n, max_k)
        paths = []
        for prev in branches:
            for path in helper(prev, d - 1):
                paths.append(path + [n])
        return paths
    return helper(target, depth)

# --- Streamlit UI ---
st.set_page_config(page_title="Collatz & Pattern Explorer", layout="centered")
st.title("Collatz + Inverse Pattern Explorer")

# --- Section 1: Inverse Pattern Generator ---
st.header("1. Inverse Pattern Generator")
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

# --- Section 2: Forward T(n) Collatz ---
st.header("2. Forward Collatz (Reduced T Path)")
with st.form("forward_form"):
    forward_n = st.number_input("Starting odd number", min_value=1, value=3, step=2)
    forward_steps = st.number_input("Steps to trace forward", min_value=1, value=10)
    submitted_forward = st.form_submit_button("Trace Forward")

if submitted_forward:
    try:
        forward_path = trace_forward(forward_n, forward_steps)
        st.text_area("T(n) Forward Path", " → ".join(str(n) for n in forward_path), height=150)
    except ValueError as e:
        st.error(str(e))

# --- Section 3: Reverse T(n) Collatz ---
st.header("3. Reverse Collatz T(n) Path Finder")
with st.form("reverse_form"):
    reverse_target = st.number_input("Target odd number (trace backward)", min_value=1, value=1, step=2)
    reverse_depth = st.number_input("Depth (levels backward)", min_value=1, value=5)
    max_k = st.slider("Max exponent k (controls speed & accuracy)", min_value=1, max_value=60, value=30)
    submitted_reverse = st.form_submit_button("Trace Reverse")

if submitted_reverse:
    with st.spinner("Tracing reverse paths..."):
        reverse_paths = trace_backward(reverse_target, reverse_depth, max_k)
        if reverse_paths:
            output = "\n".join(" → ".join(str(n) for n in path) for path in reverse_paths)
            st.text_area("Reverse T(n) Paths", output, height=300)
        else:
            st.warning("No reverse paths found.")
