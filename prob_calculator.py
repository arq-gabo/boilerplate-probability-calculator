import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **args):
        self.contents = self.balls_list(args)

    # Method for cast a dict to list ej {"red": 2, "blue": 1} -> ["red", "red", "blue"]
    def balls_list(self, balls):
        list_args = []
        for i in balls:
            for _ in range(balls[i]):
                list_args.append(i)
        return list_args
    
    # Method for get num balls random fron de hat
    def draw(self, num_ball_draw):
        draw_list = []
        if num_ball_draw >= len(self.contents):
            draw_list = self.contents
        else:
            for _ in range(num_ball_draw):
                random_idx = random.randint(0, len(self.contents) - 1)
                draw_list.append(self.contents[random_idx])
                del self.contents[random_idx]               
        
        return draw_list

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

    acum = 0

    for _ in range(num_experiments):
        # We deeply copy the elements of the Ball class so as not to affect the elements of the original class
        copy_hat = copy.deepcopy(hat)
        # Apply method for get num random balls
        random_balls = copy_hat.draw(num_balls_drawn)
        # Cast dict expected_balls to list using balls_list method from copy_had copied from Class Hat
        list_expected_balls = copy_hat.balls_list(expected_balls)

        # Loop for delete in list expected balls if the colors in list random balls
        for color_random_ball in random_balls:
            if color_random_ball in list_expected_balls:
                list_expected_balls.remove(color_random_ball)

        # if the list is empty, it is because there are enough balls in list expected balls
        if list_expected_balls == []:
            acum += 1

    # Calculating probabilities
    return acum / num_experiments