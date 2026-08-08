import math

def gradient_direction_magnitude(gradient: list) -> dict:
    # Calculate magnitude
    magnitude = math.sqrt(sum(i ** 2 for i in gradient))

    # Zero gradient
    if magnitude == 0:
        return {
            "magnitude": 0.0,
            "direction": [0.0 for i in gradient],
            "descent_direction": [0.0 for i in gradient]
        }

    # Unit vector
    direction = [i / magnitude for i in gradient]

    # Opposite direction
    descent_direction = [-i for i in direction]

    return {
        "magnitude": magnitude,
        "direction": direction,
        "descent_direction": descent_direction
    }
