import json

def save_responses(time, state_values, control_inputs, filename):
    data = {
        "time": time.tolist(),
        "state_values": [state.tolist() for state in state_values],
        "control_inputs": control_inputs
    }
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
