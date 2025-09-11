# Motion Type Identifier Template

 

# Function 1: Convert velocity to m/s

def convert_velocity(v_value, v_unit):

    """

    Convert velocity to meters per second (m/s)

    Supported units: m/s, ft/s, km/s, mi/s

    """

    # TODO: Implement conversion using if-elif-else

    if v_unit == "m/s":
        return v_value
    elif v_unit == "ft/s":
        v_value = 0.3048*v_value
    elif v_unit == "km/s":
        v_value = 1000*v_value
    elif v_unit == "mi/s":
        v_value = 1609.344*v_value
    else:
        print("Error: Unsupported Unit")
        quit()
    return v_value

 

# Function 2: Convert acceleration to m/s²

def convert_acceleration(a_value, a_unit):

    """

    Convert acceleration to meters per second squared (m/s²)

    Supported units: m/s², ft/s², km/s², mi/s²

    """

    # TODO: Implement conversion using if-elif-else

    if a_unit == "m/s²":
        return a_value
    elif a_unit == "ft/s²":
        a_value = 0.3048*a_value
    elif a_unit == "km/s²":
        a_value = 1000*a_value
    elif a_unit == "mi/s²":
        a_value = 1609.344*a_value
    else:
        print("Error: Unsupported Unit")
        quit()
    return a_value

 

# Function 3: Determine motion type

def motion_type(v_si, a_si):

    """

    Determine the type of motion based on velocity and acceleration

    Rules:

    - v > 0 and a = 0 → "Uniform Motion"

    - v > 0 and a > 0 → "Accelerated Motion"

    - v > 0 and a < 0 → "Decelerated Motion"

    - v = 0 → "At Rest"

    """

    # TODO: Implement selection structure to return motion type

    if v_si > 0 and a_si == 0:
        motion = "Uniform Motion"
    elif v_si > 0 and a_si > 0:
        motion = "Accelerated Motion"
    elif v_si > 0 and a_si < 0:
        motion = "Decelerated Motion"
    elif v_si == 0:
        motion = "At Rest"
    elif v_si < 0 and a_si == 0:
        motion = "Uniform Motion"
    elif v_si < 0 and a_si > 0:
        motion = "Decelerated Motion"
    elif v_si < 0 and a_si < 0:
        motion = "Accelerated Motion"
    else:
        print ("Error: Unknown Result")
        quit()
    return motion

 

# --- Main Program ---

 

# Step 1: Input velocity

v_value = float(input("Enter velocity value: "))

v_unit = input("Enter velocity unit (m/s, ft/s, km/s, mi/s): ")

 

# Step 2: Input acceleration

a_value = float(input("Enter acceleration value: "))

a_unit = input("Enter acceleration unit (m/s², ft/s², km/s², mi/s²): ")

 

# Step 3: Convert to SI units

v_si = convert_velocity(v_value, v_unit)      # TODO: Call the conversion function

a_si = convert_acceleration(a_value, a_unit)  # TODO: Call the conversion function

 

# Step 4: Determine motion type

motion = motion_type(v_si, a_si)              # TODO: Call the motion type function

 

# Step 5: Display results

print("\n--- Results ---")

print(f"Velocity = {v_si:.3f} m/s")

print(f"Acceleration = {a_si:.3f} m/s²")


print(f"Motion Type = {motion}")
