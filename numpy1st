import numpy as np

def reward_function(params):
    # Read input parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    all_wheels_on_track = params['all_wheels_on_track']
    steering_angle = abs(params['steering_angle'])
    speed = params['speed']
    progress = params['progress']
    waypoints = params['waypoints']
    closest_waypoints = params['closest_waypoints']
    heading = params['heading']
    steps = params['steps']

    # Set the reward base on the progress made
    reward = progress

    # Penalize if the car goes off track
    if not all_wheels_on_track:
        reward = 1e-3

    # Penalize if the car is too far from the center
    if distance_from_center > track_width/2:
        reward = 1e-3

    # Reward high speed
    reward += speed*0.5

    # Reward the car for staying close to the center of the track
    reward += (1 - distance_from_center/(track_width/2))*0.5

    # Reward for steering angle
    reward += (steering_angle - (15*np.pi/180))*0.5

    # Penalize for too many steps
    if steps > 100:
        reward = 1e-3

    return float(reward)
