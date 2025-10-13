import pennylane as qml
from pennylane import numpy as np

# Step 1: Quantum device (simulator)
dev = qml.device("default.qubit", wires=2)

# Step 2: Quantum circuit
@qml.qnode(dev)
def circuit(weights):
    qml.RY(weights[0], wires=0)
    qml.RY(weights[1], wires=1)
    qml.CNOT(wires=[0, 1])
    return qml.expval(qml.PauliZ(1))

# Step 3: Try different angles
angles = np.linspace(0, np.pi, 10)
outputs = [circuit([a, a]) for a in angles]

print("Quantum circuit outputs:")
print(outputs)

# Step 4: Visualize It (optional)
import matplotlib.pyplot as plt
plt.plot(angles, outputs)
plt.xlabel("Rotation Angle (radians)")
plt.ylabel("Output Expectation")
plt.title("Quantum Learning Curve")
plt.show()