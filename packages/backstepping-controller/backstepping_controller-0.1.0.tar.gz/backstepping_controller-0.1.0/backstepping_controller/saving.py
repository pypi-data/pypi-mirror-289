import json

def save_responses(save_path, time, state_values, control_inputs):
    results = {
        'time': time.tolist(),
        'states': [state.tolist() for state in state_values],
        'control_inputs': control_inputs,
    }
    with open(save_path, 'w') as f:
        json.dump(results, f)
