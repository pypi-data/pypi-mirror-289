import matplotlib.pyplot as plt

def plot_responses(time, state_values, control_inputs):
    # Plot states
    plt.figure(figsize=(12, 8))
    for i, state in enumerate(state_values):
        plt.plot(time, state, label=f'State {i+1}')
    plt.xlabel('Time [s]')
    plt.ylabel('States')
    plt.legend()
    plt.title('System States Over Time')
    plt.grid(True)
    plt.show()
    
    # Plot control inputs
    plt.figure(figsize=(12, 6))
    plt.plot(time[:-1], control_inputs, label='Control Input')
    plt.xlabel('Time [s]')
    plt.ylabel('Control Input')
    plt.legend()
    plt.title('Control Input Over Time')
    plt.grid(True)
    plt.show()

