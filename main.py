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
#variable definition
Pr= 15.0 #in MW that's the rated or maximum power of the turbine
WSin=3.0 # in m/s where the rotor starts to spin
WSrp=11.0 #in m/s where the wind speed is sufficient to reach rated power (15MW)
WSout = 25.0 #in m/s turbine switch off at the wind speed because the wind speed is too strong.
r = 118.0 # let s assume a 236m rotor diameter with r is the radius. 
A = pi() * (r**2) #rotor swept area
Cp = 0.45

# the ".0" behind each number is to indicate the value is a float number


x = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0, 21.0, 22.0, 23.0, 24.0, 25.0, 26.0]
# x is the list of the wind speed in m/s from 0 to 26m/s where the power should work between 3 and 25m/s
y = P 

"""
In theory we should have 3 functions:
- one for Power P = 0 meaning where WS<WSin or WS>WSout
- one for Power P= g(v)*Pr wich is the ramp up of the power curve between WSin and WSrp (rp as rated power)
- one for Power Prated for WSrp<WS<WSout
"""
def add_two(x, y):
  #calculate power between WSin and WSrp
  return P= 0.5* A * Cp * x**3
"""
Docstring here.
"""
if x < WSin or x > WS out: 
    P= 0
elif x >= WSin and x < WSrp
    P= (x**3/WSrp**3) * Pr
else x =>WSrp and x <= WSout
    P = Pr
 return y
print ("The power P for the Wind Speed given is" y) 

#plot(x, P) 
"""
# Add comment if needed.
result = x + y # Add comment if needed.
return result
if __name__ == '__main__':
# Write the main script to use the function here:
x = 1
y = 1
# Add comments to explain if needed.
z = add_two(x, y)
print(f'x + y = {z}') # Add comment when needed
"""
"""
The result should be the power curve as a plot. 

"""
