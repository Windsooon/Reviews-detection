import matplotlib.pyplot as plt
import numpy as np

# Fixing random state for reproducibility
np.random.seed(19680801)


plt.rcdefaults()
fig, ax = plt.subplots()

# Example data
scores = ('Accuracy score', 'Precision score', 'Recall score', 'F1 score')
y_pos = np.arange(len(scores))

performance = [0.76, 0.69, 0.91, 0.79]

ax.barh(y_pos, performance, align='center')
ax.set_yticks(y_pos)
ax.set_yticklabels(scores)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Performance')
ax.set_title('Hybrid')

plt.show()
