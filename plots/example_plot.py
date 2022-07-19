import proposal as pp

import matplotlib.pyplot as plt
import numpy as np

# read properties from config file
particle = pp.particle.MuMinusDef()
prop = pp.Propagator(particle, "config.json")

# define initial particle state
init_state = pp.particle.ParticleState()
init_state.position = pp.Cartesian3D(0, 0, 0)
init_state.direction = pp.Cartesian3D(0, 0, 1)
init_state.energy = 1e9 # MeV

# propagation
prop_distances = []
for i in range(10000):
    output = prop.propagate(init_state, 
                            max_distance = 1e5) # cm
    E_f = output.final_state().energy
    prop_distances.append(E_f)


bins = np.geomspace(min(prop_distances), max(prop_distances), 50)
plt.xscale('log')
plt.yscale('log')
plt.grid()
plt.hist(prop_distances, bins=bins)
plt.xlabel('propagated_distance / cm')
plt.ylabel('# particles')
plt.tight_layout()
plt.savefig("example_output.pdf", dpi=300)
