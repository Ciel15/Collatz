def generate_inverse_pattern(limit=141, w=None, y=None, z=None):
    for x in range(1, limit + 1):
        # Default fallback values
        w_val = w if w is not None else 2
        y_val = y if y is not None else 3
        z_val = z if z is not None else 1

        # Always compute v = x * w
        v = x * w_val
        line = f"{x} = ({v} / {w_val})"

        if x % 2 == 0:
            # Try a • y + z form only for even x
            if y_val != 0 and (x - z_val) % y_val == 0:
                a = (x - z_val) // y_val
                line += f" = ({a} • {y_val} + {z_val})"
            else:
                line += ""

        print(line)

# Run
generate_inverse_pattern(limit=100, w=2, y=3, z=1)
