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

    # Merge sort algorithm
    def merge_sort():
        n = len(data)
        if (n > 1):
            mid = n // 2
            left_half = data[:mid]
            right_half = data[mid:]
            
            merge_sort(left_half)
            merge_sort(right_half)
            merge(data, left_half, right_half)
            yield data
        
    def merge(data, left_half, right_half):
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                data[k] = left_half[i]
                i += 1
            else:
                data[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            data[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            data[k] = right_half[j]
            j += 1
            k += 1
   
    # Function to update animation speed
    def update_speed(val):
        ani.event_source.interval = val

    # Create a slider for adjusting animation speed
    ax_speed = plt.axes([0.1, 0.02, 0.8, 0.03])
    speed_slider = plt.Slider(ax=ax_speed, label='Speed', valmin=100, valmax=1000, valinit=500, valstep=100)
    speed_slider.on_changed(update_speed)

    # Set title for the window
    plt.title('Merge Sort Visualization')

    # Create animation
    ani = animation.FuncAnimation(fig, func=update_fig, fargs=(bar_rects, iteration), frames=merge_sort, repeat=False, interval=500)
    plt.show()

# Example usage
data = [random.randint(1, 100) for _ in range(10)]
bubble_sort_visualization(data)