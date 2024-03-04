import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

# Function to visualize Selection sort
def Selection_sort_visualization(data):
   n = len(data)
   fig, ax = plt.subplots()
   # ax.set_title('Selection Sort Visualization')
   bar_rects = ax.bar(range(len(data)), data, align="edge")
   iteration = [0]

   # Update function for animation
   def update_fig(data, rects, iteration):
       for rect, val in zip(rects, data):
           rect.set_height(val)
       iteration[0] += 1
       ax.set_title(f'Iteration {iteration[0]}')

    # Selection sort algorithm
   def selection_sort():
        n = len(data)
        for i in range(n):
            min_index = i
            for j in range(i+1, n):
                if(data[min_index] > data[j]):
                    min_index = j
            data[i], data[min_index] = data[min_index], data[i]
            yield data

   # Function to update animation speed
   def update_speed(val):
       ani.event_source.interval = val

   # Create a slider for adjusting animation speed
   ax_speed = plt.axes([0.1, 0.02, 0.8, 0.03])
   speed_slider = plt.Slider(ax=ax_speed, label='Speed', valmin=100, valmax=1000, valinit=500, valstep=100)
   speed_slider.on_changed(update_speed)

   # Set title for the window
   plt.title('Selection Sort Visualization')

   # Create animation
   ani = animation.FuncAnimation(fig, func=update_fig, fargs=(bar_rects, iteration), frames=selection_sort, repeat=False, interval=500)
   plt.show()

# Example usage
data = [random.randint(1, 100) for _ in range(100)]
Selection_sort_visualization(data)