import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

# Function to visualize bubble sort
def bubble_sort_visualization(data):
    n = len(data)
    fig, ax = plt.subplots()
    # ax.set_title('Bubble Sort Visualization')
    bar_rects = ax.bar(range(len(data)), data, align="edge")
    iteration = [0]

    # Update function for animation
    def update_fig(data, rects, iteration):
        for rect, val in zip(rects, data):
            rect.set_height(val)
        iteration[0] += 1
        ax.set_title(f'Iteration {iteration[0]}')

    # Quicksort algorithm
    def quicksort():
        if len(data) <= 1:
            sorted_arr = data
        else:
            pivot = data[len(data) // 2]
            left = [x for x in data if x < pivot]
            middle = [x for x in data if x == pivot]
            right = [x for x in data if x > pivot]
            
            sorted_arr = quicksort(left) + middle + quicksort(right)
    
    # Function to update animation speed
    def update_speed(val):
        ani.event_source.interval = val

    # Create a slider for adjusting animation speed
    ax_speed = plt.axes([0.1, 0.02, 0.8, 0.03])
    speed_slider = plt.Slider(ax=ax_speed, label='Speed', valmin=100, valmax=1000, valinit=500, valstep=100)
    speed_slider.on_changed(update_speed)

    # Set title for the window
    plt.title('Quicksort Visualization')

    # Create animation
    ani = animation.FuncAnimation(fig, func=update_fig, fargs=(bar_rects, iteration), frames=quicksort, repeat=False, interval=500)
    plt.show()

# Example usage
data = [random.randint(1, 100) for _ in range(10)]
bubble_sort_visualization(data)