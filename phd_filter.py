# Probability Hypothesis Density (PH)
import numpy as np
import matplotlib.pyplot as plt

# Parameters
NUM_PARTICLES = 500
SURVIVAL_PROB = 0.95
DETECTION_PROB = 0.9
BIRTH_RATE = 0.1
CLUTTER_RATE = 10
STATE_SPACE = (0, 100)
TIME_STEPS = 10

# Initialize particles
particles = np.random.uniform(STATE_SPACE[0], STATE_SPACE[1], NUM_PARTICLES)
weights = np.full(NUM_PARTICLES, 1.0 / NUM_PARTICLES)

# Simulated true object positions
true_positions = [30, 60]

def simulate_measurements(true_positions):
    measurements = []
    for pos in true_positions:
        if np.random.rand() < DETECTION_PROB:
            measurements.append(pos + np.random.randn() * 1.0)
    # Add clutter
    num_clutter = np.random.poisson(CLUTTER_RATE)
    measurements.extend(np.random.uniform(STATE_SPACE[0], STATE_SPACE[1], num_clutter))
    return measurements

def phd_filter(particles, weights, measurements):
    # Predict step
    particles += np.random.randn(NUM_PARTICLES) * 1.0  # Motion model
    weights *= SURVIVAL_PROB

    # Birth particles
    num_births = np.random.poisson(BIRTH_RATE * NUM_PARTICLES)
    birth_particles = np.random.uniform(STATE_SPACE[0], STATE_SPACE[1], num_births)
    particles = np.concatenate((particles, birth_particles))
    weights = np.concatenate((weights, np.full(num_births, 1.0 / NUM_PARTICLES)))

    # Update step
    for measurement in measurements:
        # Compute importance weights
        likelihood = np.exp(-0.5 * ((particles - measurement) ** 2))
        weights += DETECTION_PROB * likelihood

    # Normalize weights
    weights /= np.sum(weights)

    # Resample particles
    indices = np.random.choice(len(particles), NUM_PARTICLES, p=weights)
    particles = particles[indices]
    weights = np.full(NUM_PARTICLES, 1.0 / NUM_PARTICLES)

    return particles, weights

# Run the filter over multiple time steps
for t in range(TIME_STEPS):
    # Simulate measurements
    measurements = simulate_measurements(true_positions)
    # Update true positions (objects can move)
    true_positions = [pos + np.random.randn() * 0.5 for pos in true_positions]
    # Apply PHD filter
    particles, weights = phd_filter(particles, weights, measurements)

    # Plotting
    plt.figure(figsize=(10, 3))
    plt.scatter(particles, np.zeros_like(particles), alpha=0.5, label='Particles')
    plt.scatter(measurements, np.ones_like(measurements), color='red', marker='x', label='Measurements')
    plt.scatter(true_positions, np.full_like(true_positions, -0.1), color='green', marker='D', label='True Positions')
    plt.legend()
    plt.title(f'Time Step {t+1}')
    plt.xlabel('State Space')
    plt.yticks([])
    plt.show()
