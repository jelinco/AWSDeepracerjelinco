import math

def reward_function(params)
    
    # Read input parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    steering = abs(params['steering_angle'])
    direction_stearing=params['steering_angle']
    speed = params['speed']
    steps = params['steps']
    is_offtrack=params['is_offtrack']
    progress = params['progress']
    all_wheels_on_track = params['all_wheels_on_track']
    x = params['x']
    y = params['y']
    
    
    # Calculate 3 markers that are at varying distances away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width
    
    # Give higher reward if the car is closer to center line and vice versa
    if distance_from_center <= marker_1:
        reward = 1.0
    elif distance_from_center <= marker_2:
        reward = 0.5
    elif distance_from_center <= marker_3:
        reward = 0.1
    elif progress > 0.7
        reward = 2.0
    else:
        reward = 1e-3  # likely crashed/ close to off track
    
    return float(reward):
