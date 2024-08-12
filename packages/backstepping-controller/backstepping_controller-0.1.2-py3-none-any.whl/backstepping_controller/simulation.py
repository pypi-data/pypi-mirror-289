import numpy as np
import json
import sympy as sp

def simulate_system(final_control_law, states, gains, initial_conditions, time, state_equations, params_subs, refs=None, save_path=None, plot=True, print_law=False):
    # Substitute the gains and parameters with their numerical values
    final_control_law_num = final_control_law.subs(params_subs)

    # Convert the control law to a numerical function
    control_law_func = sp.lambdify(states, final_control_law_num)

    # Simulation parameters
    dt = time[1] - time[0]
    num_states = len(states)

    # Initialize state values
    state_values = [np.array([float(ic)]) for ic in initial_conditions]

    # Initialize reference values if provided
    if refs is not None:
        refs_values = [np.interp(time, time, ref) for ref in refs]
    else:
        refs_values = [np.zeros_like(time) for _ in states]

    # Initialize control inputs
    control_inputs = []

    # Simulation loop
    for t in time[1:]:
        current_values = [float(state[-1]) for state in state_values]
        current_refs = [ref[np.where(time == t)[0][0]] for ref in refs_values]

        # Compute the control input
        u_curr = control_law_func(*current_values)
        control_inputs.append(u_curr)

        # Update the system using Euler's method
        next_values = []
        for i in range(num_states):
            # Substitute the gains and parameters into state equations
            state_eq_num = state_equations[i].subs(params_subs)
            # Create a numerical function for the state equations
            state_dot_func = sp.lambdify(tuple(states) + (sp.Symbol('u'),), state_eq_num)
            state_dot = state_dot_func(*current_values, u_curr)
            
            # Ensure state_dot is fully evaluated
            state_dot = float(state_dot)
            
            next_values.append(current_values[i] + state_dot * dt)

        # Store the next state values
        for i in range(num_states):
            state_values[i] = np.append(state_values[i], next_values[i])

    if plot:
        plot_responses(time, state_values, control_inputs, refs=refs_values)

    if save_path:
        save_responses(save_path, time, state_values, control_inputs)

    if print_law:
        print(f"Final Control Law: {final_control_law}")

    return state_values, control_inputs
