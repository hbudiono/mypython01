# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# Percobaan
# 

# %%
a = 2
b=5
print(a+10)
print(b)



# %%
from pylab import *
plot([1,2,3])
xlabel('This is a graph')


# %%
import matplotlib.pyplot as plt
import numpy as np

# Fixing random state for reproducibility
np.random.seed(19680801)

# the bar
x = np.random.rand(500) > 0.7

barprops = dict(aspect='auto', cmap='binary', interpolation='nearest')

fig = plt.figure()

# a vertical barcode
ax1 = fig.add_axes([0.1, 0.1, 0.1, 0.8])
ax1.set_axis_off()
ax1.imshow(x.reshape((-1, 1)), **barprops)

# a horizontal barcode
ax2 = fig.add_axes([0.3, 0.4, 0.6, 0.2])
ax2.set_axis_off()
ax2.imshow(x.reshape((1, -1)), **barprops)

plt.show()


# %%
fig, ax = plt.subplots()  # Create a figure containing a single axes.
ax.plot([1, 2, 2, 2], [1, 4, 2, 3])  # Plot some data on the axes.

# %% [markdown]
# This will explain , how we can draw
# 

# %%
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['path.simplify_threshold'] = 1.0

# Setup, and create the data to plot
y = np.random.rand(100000)
y[50000:] *= 2
y[np.logspace(1, np.log10(50000), 400).astype(int)] = -1
mpl.rcParams['path.simplify'] = True

mpl.rcParams['agg.path.chunksize'] = 0
plt.plot(y)
plt.show()

mpl.rcParams['agg.path.chunksize'] = 10000
plt.plot(y)
plt.show()




# %%
a=10
print(a)

# %%
