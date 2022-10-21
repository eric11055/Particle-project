import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation 

num_particles = 3

m = 1
Cq_squared = 0.01
delta_t = 0.005

# positions = np.random.random(size=(num_particles, 2)) # n particles with random starting positions x,y between 0 and 1 
positions = np.array([
    [0.552, 0.433],
    [0.223, 0.887],
    [0.666, 0.111]
])

print("Particle Positions (x and y)")
print(positions)
print()
velocities = np.random.random(size=(num_particles, 2))


def step():
    global positions, velocities, delta_t
    global positions
    global delta_t
    accels = np.zeros((num_particles, 2))
    for i in range(num_particles):
        for j in range(i+1, num_particles):
            r = positions[i] - positions[j] #r is vector from particle j to i (Force direction for particle i )
            
            
            r_length = np.linalg.norm(r)
            
            
            force = Cq_squared * r / r_length ** 3
            accels[i] += force / m
            accels[j] -= force / m #the Force direction is opposite

            
    

    velocities += accels * delta_t
    # positions += accels * delta_t
    boundary = np.transpose((positions>1).nonzero())
    
                    #rows of boundary
    # for x in range(np.shape(boundary)[0]):

    print(boundary)


    #     if positio
    #     velocities[:, 0] *= -1
    # if positions[:, 0] < 0:
    #     velocities[:, 0] *= -1
    
    # if positions[:, 1] > 1:
    #     velocities[:, 1] *= -1
    # if positions[:, 1] < 0:
    #     velocities[:, 1] *= -1

    positions += velocities * delta_t
    



fig = plt.figure(figsize=(1, 1))
# ax = fig.add_subplot(autoscale_on=False, xlim=(0, 1), ylim=(0, 1))
# line = ax.plot(*positions, 'o', lw=2)
ax = plt.axes(xlim=(0,1),ylim=(0,1))
scatter=ax.scatter(positions[:, 0], positions[:, 1])





def animate(i):
    global scatter
    step()
    scatter.set_offsets(positions)
    return scatter

ani = FuncAnimation(fig, animate, interval=5)

plt.show()

