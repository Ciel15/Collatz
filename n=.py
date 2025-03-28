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

# --- Reduced Collatz Function T(n) and Utilities ---
def T(n):
    """Returns the next odd number in the reduced Collatz (odd-only) sequence."""
    if n % 2 == 0:
        raise ValueError("T(n) is only defined for odd integers.")
    result = 3 * n + 1
    k = 0
    while result % 2 == 0:
        result //= 2
        k += 1
    return result

def reverse_T(target):
    """Returns all odd n such that T(n) = target."""
    results = []
    for k in range(1, 100):
        candidate = target * (2 ** k) - 1
        if candidate % 3 == 0:
            n = candidate // 3
            if n % 2 == 1 and n > 0:
                results.append((n, k))
    return results

def trace_forward(start, steps):
    path = [start]
    current = start
    for _ in range(steps):
        current = T(current)
        path.append(current)
    return path

def trace_backward(target, depth):
    """Recursively builds all odd-only reverse Collatz paths of given depth."""
    def helper(n, d):
        if d == 0:
            return [[n]]
        branches = reverse_T(n)
        paths = []
        for prev, _ in branches:
            for path in helper(prev, d - 1):
                paths.append(path + [n])
        return paths
    return helper(target, depth)

# --- Streamlit App UI ---
st.set_page_config(page_title="Collatz & Pattern Explorer", layout="centered")
st.title("Collatz + Inverse Pattern Explorer")

# Inverse Pattern Generator
st.header("1. Inverse Pattern Generator")
limit = st.number_input("Limit", min_value=1, value=100)
w = st.number_input("W (Multiplier, usually 2)", value=2)
y = st.number_input("Y (Divisor Check, usually 3)", value=3)
z = st.number_input("Z (Offset, usually 1)", value=1)
line_window = st.slider("Visible Lines (Output Height)", min_value=10, max_value=100, value=30)

if st.button("Generate Pattern"):
    pattern = generate_inverse_pattern(limit, w, y, z)
    st.text_area("Generated Pattern", "\n".join(pattern), height=line_window * 20)

# Forward T(n)
st.header("2. Forward Collatz T(n) Trace")
forward_n = st.number_input("Starting odd number (n)", min_value=1, value=3, step=2)
forward_steps = st.number_input("Number of steps forward", min_value=1, value=10)

if st.button("Trace Forward"):
    try:
        forward_path = trace_forward(forward_n, forward_steps)
        st.text_area("T(n) Forward Path", " → ".join(str(n) for n in forward_path), height=150)
    except ValueError as e:
        st.error(str(e))

# Reverse T(n)
st.header("3. Reverse Collatz T(n) Trace")
reverse_target = st.number_input("Target odd number (to reverse from)", min_value=1, value=1, step=2)
reverse_depth = st.number_input("How far back to trace", min_value=1, value=5)

if st.button("Trace Reverse"):
    reverse_paths = trace_backward(reverse_target, reverse_depth)
    if reverse_paths:
        st.text_area("Reverse Paths", "\n".join(" → ".join(str(n) for n in path) for path in reverse_paths), height=300)
    else:
        st.warning("No reverse paths found.")
