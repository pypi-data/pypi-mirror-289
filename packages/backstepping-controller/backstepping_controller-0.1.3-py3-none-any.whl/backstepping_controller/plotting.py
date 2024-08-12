import matplotlib.pyplot as plt

def plot_responses(time, state_values, control_inputs, title="System Response"):
    plt.figure(figsize=(12, 8))
    
    # Plot state variables
    for i, state in enumerate(state_values):
        plt.plot(time, state, label=f'State x{i+1}')
    
    plt.xlabel('Time (s)')
    plt.ylabel('States')
    plt.title(title)
    plt.grid(True)
    plt.legend()
    
    plt.figure(figsize=(12, 8))
    
    # Plot control inputs
    plt.plot(time[:-1], control_inputs, label='Control Input u')
    
    plt.xlabel('Time (s)')
    plt.ylabel('Control Input')
    plt.title(f'{title} - Control Input')
    plt.grid(True)
    plt.legend()
    
    plt.show()
