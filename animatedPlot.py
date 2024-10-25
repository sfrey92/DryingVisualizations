import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def main():
    # Import the data from the data directory and name the dataframe after the characteristic particle diameter in the file
    df_1 = pd.read_csv('data/1x50bin_0.021m 1.csv')

    # Rename all columns, except for the first and last, to the corresponding particle position
    # The second column should be named h2o_mf_bin1, the third h2o_mf_bin2, and so on
    column_names = ['time'] + [f'h2o_mf_bin{i}' for i in range(1, df_1.shape[1] - 1)] + ['Temp']
    df_1.columns = column_names

    # Create a tkinter window
    root = tk.Tk()
    root.title("3D Animation with Speed Control")

    # Plot the h2o_mf for each position as a function of time in a 3D plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Initialize the plot
    lines = []
    for i in range(1, df_1.shape[1] - 1):
        line, = ax.plot([], [], zs=i, zdir='y')
        lines.append(line)

    # Set the axes labels
    ax.set_xlabel('Time')
    ax.set_ylabel('Position')
    ax.set_zlabel('h2o_mf')

    # Set the axes limits
    ax.set_xlim(df_1['time'].min(), df_1['time'].max())
    ax.set_ylim(1, df_1.shape[1] - 1)
    ax.set_zlim(df_1.iloc[:, 1:-1].min().min(), df_1.iloc[:, 1:-1].max().max())

    # Animation function
    def update(frame):
        for i, line in enumerate(lines):
            line.set_data(df_1['time'][:frame], [i+1]*frame)
            line.set_3d_properties(df_1[f'h2o_mf_bin{i+1}'][:frame])
        return lines

    # Create the animation and assign it to a variable
    ani = FuncAnimation(fig, update, frames=len(df_1), interval=50, blit=False)

    # Create a canvas to display the plot
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    # Create a slider to control the speed of the animation
    speed_slider = tk.Scale(root, from_=1, to=1000, orient=tk.HORIZONTAL, label="Speed", length=400)
    speed_slider.set(50)
    speed_slider.pack(side=tk.BOTTOM)

    # Function to update the animation speed
    def update_speed(val):
        interval = int(val)
        print(f"Updating interval to: {interval} ms")
        ani.event_source.interval = interval

    # Attach the update function to the slider
    speed_slider.config(command=update_speed)

    # Start the tkinter main loop
    root.mainloop()

if __name__ == "__main__":
    main()