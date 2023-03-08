def reward_function(params):
    # Read input variables
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    all_wheels_on_track = params['all_wheels_on_track']
    speed = params['speed']
    steering = abs(params['steering_angle'])
    
    # Set the speed threshold based on the track width
    if track_width > 0.6:
        speed_threshold = 3.0
    else:
        speed_threshold = 2.5
    
    # Define the reward and penalty values
    reward = 1.0
    penalty = 1e-3
    
    # Penalize if the car goes off-track
    if not all_wheels_on_track:
        reward -= 1.0
    
    # Penalize if the car is too far from the center
    if distance_from_center > 0.0:
        reward -= distance_from_center * penalty
    
    # Penalize if the car is too slow
    if speed < speed_threshold:
        reward *= 0.5
    
    # Penalize if the car is not going straight
    if steering > 10.0:
        reward *= 0.8
    
    return reward
