import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation 

num_particles = 10
steps_per_frame = 2
m = 1
Cq_squared = 0.02
delta_t = 0.005
fps = 30


max_initial_velocity = 5

height = 5
width = 5

positions = np.random.random(size=(num_particles, 2)) * np.array([width, height]) - np.array([width/2, height/2])# n particles with random starting positions x,y between 0 and 1 
# positions = np.array([
#     [0, 0.5],
#     [1, 0.5]
# ])


# print("Particle Positions (x and y)")
# print(positions)
# print()
def wrapper(lower_bound,upper_bound,size):
    return (upper_bound-lower_bound)*np.random.random(size=size)+lower_bound

velocities = wrapper(-max_initial_velocity,max_initial_velocity,(num_particles,2))
# velocities = np.array([
#     [1, 0],
#     [-1, 1]
# ], dtype='float64')


def step():
    global positions, velocities, delta_t
    global positions
    global delta_t
    accels = np.zeros((num_particles, 2))
    for i in range(num_particles):
        if positions[i,0] > 0.5 * width:
            velocities[i,0] = abs(velocities[i,0]) * -1
        elif  positions[i,0] < -0.5 * width:
            velocities[i,0] = abs(velocities[i,0])
        if positions[i,1] > 0.5 * height:
            velocities[i,1] = abs(velocities[i,1]) * -1
        elif  positions[i,1] < -0.5 * height:
            velocities[i,1] = abs(velocities[i,1])
        for j in range(i+1, num_particles):
            r = positions[i] - positions[j] #r is vector from particle j to i (Force direction for particle i )
            
            r_length = np.linalg.norm(r)
            
            force = Cq_squared * r / r_length ** 3
            accels[i] += force / m
            accels[j] -= force / m #the Force direction is opposite



    velocities += accels * delta_t
    positions += velocities * delta_t
    





fig = plt.figure(figsize=(2.5, 2.5))
ax = plt.axes(xlim=(-0.5 * width , width * 0.5),ylim=(-0.5 * height,height * 0.5))
scatter=ax.scatter(positions[:, 0], positions[:, 1])





def animate(i):
    global scatter, steps_per_frame
    for _ in range(steps_per_frame):
        step()
    scatter.set_offsets(positions)
    return scatter

# given fps find interval
# fps = #frames/1s  interval = # of milliseconds/ frame

interval = 1000/fps

ani = FuncAnimation(fig, animate, interval=interval)

plt.show()

