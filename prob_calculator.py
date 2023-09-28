import copy
import random


class Hat:
    """A hat containing balls of different colors."""

    def __init__(self, **kwargs):
        """Initializes a hat with the specified number of balls of each color.

        Args:
            **kwargs: A dictionary mapping ball colors to the number of balls of that color.
        """

        self.contents = []
        for color, count in kwargs.items():
            for _ in range(count):
                self.contents.append(color)

    def draw(self, num_balls_drawn):
        """Draws `num_balls_drawn` balls from the hat without replacement.

        Args:
            num_balls_drawn: The number of balls to draw.

        Returns:
            A list of the drawn balls, as strings.
        """

        drawn_balls = []
        for _ in range(num_balls_drawn):
            if self.contents:
                ball_drawn = random.choice(self.contents)
                drawn_balls.append(ball_drawn)
                self.contents.remove(ball_drawn)
            else:
                break
        return drawn_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    """Runs a Monte Carlo simulation to estimate the probability of success for a given experiment.

    Args:
        hat: A `Hat` object.
        expected_balls: A dictionary mapping ball colors to the number of balls of that color that must be drawn in order for the experiment to be considered a success.
        num_balls_drawn: The number of balls to draw from the hat on each trial.
        num_experiments: The number of times to repeat the experiment.

    Returns:
        The probability of success, which is calculated by dividing the number of successful experiments by the total number of experiments.
    """

    # Create a deep copy of the hat so that we don't modify the original hat.
    hat_copy = copy.deepcopy(hat)

    # Initialize the number of successful experiments.
    num_successful_experiments = 0

    # Repeat the experiment `num_experiments` times.
    for i in range(num_experiments):

        # Draw `num_balls_drawn` balls from the hat.
        drawn_balls = hat_copy.draw(num_balls_drawn)

        # Check to see if the drawn balls match the `expected_balls` dictionary.
        success = True
        for color, expected_count in expected_balls.items():
            if drawn_balls.count(color) < expected_count:
                success = False
                break

        # If the experiment was a success, increment the number of successful experiments.
        if success:
            num_successful_experiments += 1

    # Calculate the probability of success.
    probability_of_success = num_successful_experiments / num_experiments

    return probability_of_success
