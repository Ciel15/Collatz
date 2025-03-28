import streamlit as st

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

# Streamlit interface
st.title("Cardinal ((xy)+1) Generator")

limit = st.number_input("Limit", min_value=1, value=100)
w = st.number_input("W (Collatz: 2)", value=2)
y = st.number_input("Y (Collatz: 3)", value=3)
z = st.number_input("Z (Collatz: 1)", value=1)

line_window = st.slider("Visible Lines for Output Window", min_value=25, max_value=100, value=50)

if st.button("Generate"):
    result = generate_inverse_pattern(limit, w, y, z)
    output_text = "\n".join(result)
    st.text_area("x = (x / w) = (x x y + z) Output:", output_text, height=line_window * 20, max_chars=None)

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
    """
    Returns all possible odd n such that T(n) = target.
    Reverse solving (3n + 1)/2^k = target for some k ≥ 1.
    """
    results = []
    for k in range(1, 100):  # Reasonable range for k
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
    """
    Explore backwards from a number using reverse_T, tracing possible predecessors.
    Returns a tree of paths (as nested lists).
    """
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

# Example Usage
if __name__ == "__main__":
    # Forward trace from 3 (T-style path)
    print("Forward T path from 3:")
    print(trace_forward(3, 10))

    # Backward trace to 1 (finding n such that T(n) = 1)
    print("\nReverse T path to 1:")
    paths_to_1 = trace_backward(1, 5)
    for path in paths_to_1:
        print(path)
