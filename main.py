import math
import matplotlib.pyplot as plt

"""
the goal of the project is to calculate the energy yield in a basic way. with the formula
P = 1/2*Cp*V^3*A
- P= Electrical Power
- Cp= Coefficient performance in theory the maximum is dictate by the betz law (0.593). 
In practice, the value is around 0.48 as maximum for an optimal wind speed
- V is the wind speed arriving to the rotor
- A is the swept area of the rotor. 

The turbine is a 15MW turbine working between 3 and 25m/s reaching rated power at 11m/s
The goal of the script is to calculate the power no matter what is the wind speed. 
As the power is proportial to the wind speed power cube, the cubic interprolation will be used: 
g(v) = WS^3/WSrp^3

"""


# -----------------------------
# Turbine and wind data
# -----------------------------
Pr = 15.0      # rated power in MW
WSin = 3.0     # cut-in wind speed (m/s)
WSrp = 11.0    # rated wind speed (m/s)
WSout = 25.0   # cut-out wind speed (m/s)
r = 118.0      # rotor radius (m)
Cp = 0.45      # power coefficient
rho = 1.225    # air density (kg/m^3)

A = math.pi * r**2  # swept rotor area

# the ".0" behind each number is to indicate the value is a float number

# -----------------------------
# Power calculation
# -----------------------------
def turbine_power(v):
    """
    Calculate turbine output power in MW.
    - Below cut-in (3m/s) or above cut-out (25m/s): 0 MW
    - Between WSin (3m/s) and WSrp (11m/s): cubic increase to rated power
    - Between WSrp (11m/s) and WSout (25m/s): rated power (15MW)
    """
    if v < WSin or v > WSout:
        return 0.0
    elif WSin <= v < WSrp:
        # cubic interpolation to rated power
        return (v / WSrp) ** 3 * Pr
    else:
        # at or above rated speed, keep rated power
        return Pr


def aerodynamic_power(v):
    """
    Optional physical power formula:
    P = 0.5 * Cp * rho * A * v^3
    capped at rated turbine power.
    """
    if v < WSin or v > WSout:
        return 0.0
    p = 0.5 * Cp * rho * A * v**3
    return min(p, Pr)  # power limited by turbine rating


# -----------------------------
# Example usage
# -----------------------------
if __name__ == "__main__":
    speeds = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0,
              11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0,
              20.0, 21.0, 22.0, 23.0, 24.0, 25.0, 26.0]

    print("Wind speed (m/s)   Power (MW)")
    for v in speeds:
        p = turbine_power(v)
        print(f"{v:>15.1f}      {p:>9.2f}")

    # Optional: user input
    user_speed = float(input("\nEnter wind speed in m/s: "))
    print(f"Power at {user_speed} m/s is {turbine_power(user_speed):.2f} MW")

    # -----------------------------
    # Plot the power curve
    # -----------------------------
    x = [i / 10 for i in range(0, 261)]  # 0.0 to 26.0 m/s
    y = [turbine_power(v) for v in x]

    plt.plot(x, y, color="blue", linewidth=2)
    plt.title("Wind Turbine Power Curve")
    plt.xlabel("Wind speed (m/s)")
    plt.ylabel("Power (MW)")
    plt.grid(True)
    plt.show()
