import matplotlib.pyplot as plt
import numpy as np
import paths
from astropy.stats import histogram

# Generate some data
random_numbers = np.concatenate((np.random.normal(0, 1, 1000),
                                 np.random.normal(10, 1, 1000)))

# Plot and save
fig, ax = plt.subplots()
bin_type = ['knuth','scott','freedman','blocks']
for bt in bin_type:
    h, bins = histogram(random_numbers, bins=bt)
    ax.hist(random_numbers, bins=bins, label=bt, alpha=0.8)
ax.legend()
fig.savefig(paths.figures / "different_hist_bin_type.pdf", bbox_inches="tight", dpi=300)
