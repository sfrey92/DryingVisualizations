import matplotlib.pylab as plot
import numpy as np
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

h = 3                           #define nth harmonic
kval = np.pi*h/100              #wave vector from nth harmonic (1/cm)
mu = 0.001                      #linear string mass density (g/cm)
g = 980                         #gravitational acceleration (cm/s/s)
N = 50                          #number of lead shot pellets
m = N*0.01216                   #total mass of lead shot pellets (g)
A = 0.15                        #wave amplitude
omega = 120                     #angular wave frequency
k1 = omega*np.sqrt(mu/(m*g))    #wave vector for initial wave (1/cm)
k2 = k1*k1/kval                 #wave vector for 'reflected' wave (1/cm)

fig = plot.Figure()

x = np.linspace(0,100,500)

def animate(i):
    line.set_ydata(A*np.sin(k1*x+omega*i) + A*np.sin(k2*x - omega*i))
    return line,

main = tk.Tk()

#background text
intro = tk.Label(main,text='Add lead shot to produce a standing wave.').grid(column=0,row=0)

canvas = FigureCanvasTkAgg(fig, master=main)
canvas.get_tk_widget().grid(column=0,row=1)

ax = fig.add_subplot(111)
ax.set_xlim(0,100)
ax.set_ylim(-2,2)

line, = ax.plot(x, A*np.sin(k1*x) + A*np.sin(k2*x))
anim = animation.FuncAnimation(fig, animate, interval=50, blit=False)

horizontal = tk.Scale(main, from_=1, to=1000, length=400, orient='horizontal').grid(column=0,row=2)

main.mainloop()