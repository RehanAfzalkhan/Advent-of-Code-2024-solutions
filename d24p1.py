from collections import defaultdict
import re

# Read input from file
def read_input(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip().split('\n')

# Perform logic gate operations
def apply_gate(gate, a, b):
    if gate == 'AND':
        return a & b
    elif gate == 'OR':
        return a | b
    elif gate == 'XOR':
        return a ^ b
    return None

# Simulate the circuit
def simulate_circuit(lines):
    wire_values = {}
    gate_operations = []
    
    # Parse input
    for line in lines:
        if ':' in line:
            wire, value = line.split(': ')
            wire_values[wire] = int(value)
        else:
            gate_operations.append(line)
    
    # Process gates until all outputs are computed
    while gate_operations:
        remaining_operations = []
        for operation in gate_operations:
            match = re.match(r'(.+) (AND|OR|XOR) (.+) -> (.+)', operation)
            if match:
                a, gate, b, output = match.groups()
                if a in wire_values and b in wire_values:
                    wire_values[output] = apply_gate(gate, wire_values[a], wire_values[b])
                else:
                    remaining_operations.append(operation)
        gate_operations = remaining_operations
    
    # Collect and sort output wires starting with 'z'
    output_bits = []
    for wire, value in wire_values.items():
        if wire.startswith('z'):
            output_bits.append((wire, value))
    
    output_bits.sort()  # Sort to ensure correct binary order (z00, z01, ...)
    
    # Construct binary output
    binary_result = ''.join(str(bit[1]) for bit in output_bits[::-1])
    return int(binary_result, 2)

if __name__ == "__main__":
    input_lines = read_input("inputs/d24input.txt")
    result = simulate_circuit(input_lines)
    print("Output (Decimal):", result)