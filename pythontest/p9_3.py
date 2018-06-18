import matplotlib.pyplot as plt
steps = [6543, 7000, 8900, 10789, 3467, 11045, 5095]
labels = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
num_bars = len(steps)
positions = range(1, num_bars+1)
plt.bar(positions, steps, align='center')
plt.yticks(range(2000,12000,2000), range(2000,12000,2000))
plt.xlabel('Steps')
plt.ylabel('Day')
plt.title('Number of steps walked')
plt.grid()
plt.show()
