#from IPython import get_ipython
#get_ipython().run_line_magic('matplotlib', 'inline')
# Importing standard Qiskit libraries and configuring account
from qiskit import QuantumCircuit, execute, Aer #, IBMQ
from qiskit.compiler import transpile, assemble
#from qiskit.tools.jupyter import *
from qiskit.visualization import *
import numpy as np
# Loading your IBM Q account(s)
# provider = IBMQ.load_account()
circ = QuantumCircuit(4)
circ.h(0)
circ.h(1)
circ.h(2)
circ.h(3)
circ.x(3)
circ.barrier(range(4))
circ.cx(0,3)
circ.cx(1,3)
circ.cx(2,3)
circ.h(0)
circ.h(1)
circ.h(2)
circ.h(3)
circ.draw()

backend = Aer.get_backend('statevector_simulator')
job = execute(circ, backend)
result = job.result()
outputstate = result.get_statevector(circ, decimals=3)
print(outputstate)

plot_state_city(outputstate)
meas = QuantumCircuit(4, 4)
meas.barrier(range(4))
meas.measure(range(4),range(4))
qc = circ+meas
qc.draw()
print(qc)

backend_sim = Aer.get_backend('qasm_simulator')
job_sim = execute(qc, backend_sim, shots=1024)

result_sim = job_sim.result()
counts = result_sim.get_counts(qc)
print(counts)

plot_histogram(counts)

