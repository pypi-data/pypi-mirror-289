import sympy as sp
import numpy as np
from backstepping_controller import generic_backstepping_controller, simulate_system, plot_responses

# Define system dynamics
x1, x2 = sp.symbols('x1 x2')
u = sp.Symbol('u')
gains = {'k1': 2, 'k2': 3}

# Simple system: x1_dot = x2, x2_dot = -x1 + u
state_equations = [x2, -x1 + u]
num_states = 2

# Generate the backstepping control law
control_law, states, gain_symbols = generic_backstepping_controller(num_states, state_equations, 'u', gains)

# Define simulation parameters
initial_conditions = [1, 0]  # Initial conditions for x1 and x2
time = np.linspace(0, 10, 500)  # Time vector
params_subs = {sp.Symbol('k1'): gains['k1'], sp.Symbol('k2'): gains['k2']}

# Simulate the system
state_values, control_inputs = simulate_system(control_law, states, gain_symbols, initial_conditions, time, state_equations, params_subs, plot=False, print_law=True)

# Plot the results (without title parameter)
plot_responses(time, state_values, control_inputs)
