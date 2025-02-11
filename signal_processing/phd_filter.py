# signal_processing/phd_filter.py

import numpy as np

# Constants for the filter
NUM_PARTICLES = 500
SURVIVAL_PROB = 0.95
DETECTION_PROB = 0.9
BIRTH_RATE = 0.1
CLUTTER_RATE = 10
STATE_SPACE = (0, 100)

def simulate_measurements(true_positions, detection_prob=DETECTION_PROB, clutter_rate=CLUTTER_RATE, state_space=STATE_SPACE):
    """
    Simulate measurements based on true positions, including missed detections and clutter.
    """
    measurements = []
    for pos in true_positions:
        if np.random.rand() < detection_prob:
            measurements.append(pos + np.random.randn() * 1.0)
    num_clutter = np.random.poisson(clutter_rate)
    measurements.extend(np.random.uniform(state_space[0], state_space[1], num_clutter))
    return measurements

def phd_filter(particles, weights, measurements):
    """
    Apply one update cycle of a PHD filter.
    
    Parameters:
        particles (np.ndarray): Array of particle positions.
        weights (np.ndarray): Array of particle weights.
        measurements (list): List of current measurements.
    
    Returns:
        tuple: Updated (particles, weights)
    """
    # Predict step: random walk (motion model)
    particles += np.random.randn(len(particles)) * 1.0
    weights *= SURVIVAL_PROB

    # Birth step: add new particles
    num_births = np.random.poisson(BIRTH_RATE * len(particles))
    if num_births > 0:
        birth_particles = np.random.uniform(STATE_SPACE[0], STATE_SPACE[1], num_births)
        particles = np.concatenate((particles, birth_particles))
        weights = np.concatenate((weights, np.full(num_births, 1.0/len(particles))))

    # Update step: adjust weights based on measurements
    for measurement in measurements:
        likelihood = np.exp(-0.5 * ((particles - measurement) ** 2))
        weights += DETECTION_PROB * likelihood

    # Normalize and resample
    weights /= np.sum(weights)
    indices = np.random.choice(len(particles), size=NUM_PARTICLES, p=weights)
    particles = particles[indices]
    weights = np.full(NUM_PARTICLES, 1.0 / NUM_PARTICLES)
    return particles, weights
