import random

class Tank:
    def __init__(self):
        self.x, self.y = 6, 6
        self.directions = ["^", ">", "v", "<"]
        self.direction_values = ["North", "East", "South", "West"]
        self.direction_index = 0
        self.target_hits = 0
        self.shots = {"^": 0, ">": 0, "v": 0, "<": 0}
        self.map_size = 12
        self.target_x, self.target_y  = self.generate_target()

    def generate_target(self):
        x_target, y_target = random.randint(0, self.map_size - 1), random.randint(0, self.map_size - 1)
        if (x_target, y_target) == (self.x, self.y):
            return self.generate_target()
        return x_target, y_target

    def create_map(self):
        game_map = [["." for _ in range(self.map_size)] for _ in range(self.map_size)]
        game_map[self.x][self.y] = self.directions[self.direction_index]
        game_map[self.target_x][self.target_y] = "O"
        for row in game_map:
            print(" ".join(row))

    def move_forward(self):
        if self.x > 0:
            self.x -= 1
            print("Tank moved forward")
        else:
            print("Reached the map edge, cant move forward!!!")
        self.create_map()

    def move_backward(self):
        if self.x < self.map_size - 1:
            self.x += 1
            print("Tank moved backward")
        else:
            print("Reached the map edge, cant move backwards!!!")
        self.create_map()

    def move_left(self):
        if self.y > 0:
            self.y -= 1
            print("Tank moved left")
        else:

            print("Reached the map edge, cant move to the left!!!")
        self.create_map()

    def move_right(self):
        if self.y < self.map_size - 1:
            self.y += 1
            print("Tank moved right")
        else:
            print("Reached the map edge, cant move to the right!!!")
        self.create_map()

    def turn_left(self):
        self.direction_index = (self.direction_index - 1) % 4
        print("Tank turned left")
        self.create_map()

    def turn_right(self):
        self.direction_index = (self.direction_index + 1) % 4
        print("Tank turned right")
        self.create_map()

    def shoot(self):
        directions = self.directions[self.direction_index]
        self.shots[directions] += 1
        print(f"Tank shot at {directions}")
        if self.direction_index == 0:
            if self.x > self.target_x and self.y == self.target_y:
                print("Target was hit")
                self.target_x, self.target_y = self.generate_target()
                self.create_map()
                self.target_hits += 1
            else:
                print("Shot missed")
                self.create_map()

        if self.direction_index == 1:
            if self.x == self.target_x and self.y < self.target_y:
                print("Target was hit")
                self.target_x, self.target_y = self.generate_target()
                self.create_map()
                self.target_hits += 1
            else:
                print("Shot missed")
                self.create_map()

        if self.direction_index == 2:
            if self.x < self.target_x and self.y == self.target_y:
                print("Target was hit")
                self.target_x, self.target_y = self.generate_target()
                self.create_map()
                self.target_hits += 1
            else:
                print("Shot missed")
                self.create_map()

        if self.direction_index == 3:
            if self.x == self.target_x and self.y > self.target_y:
                print("Target was hit")
                self.target_x, self.target_y = self.generate_target()
                self.create_map()
                self.target_hits += 1
            else:
                print("Shot missed")
                self.create_map()

    def info(self):
        direction_symbol = self.directions[self.direction_index]
        direction_name = self.direction_values[self.direction_index]
        print("\nTank information:")
        print(f"Current direction: {direction_name}, {direction_symbol}")
        print(f"Tank coordination: ({self.x}, {self.y})")
        print(f"Bulls eyes! = {self.target_hits}")
        print(f"Target coordination: ({self.target_x}, {self.target_y})")
        print(f"Total shots: {sum(self.shots.values())}")
        for k, v in self.shots.items():
            print(f"  - {k}: {v} shots")
        self.create_map()


def menu():
    tank = Tank()
    tank.create_map()
    while True:
        print("\nMenu:")
        print("Key 1 : Tank moves forward")
        print("Key 2 : Tank moves backward")
        print("Key 3 : Tank moves left")
        print("Key 4 : Tank moves right")
        print("Key 5 : Tank will turn left")
        print("Key 6 : Tank will turn right")
        print("Key 0 : Tank will shoot")
        print("Key 8 : Information")
        print("Key 9 : Exit the game")
        user_choice = input("Choose 1 option from above: ")

        if user_choice == "w":
            tank.move_forward()
        elif user_choice == "s":
            tank.move_backward()
        elif user_choice == "a":
            tank.move_left()
        elif user_choice == "d":
            tank.move_right()
        elif user_choice == "q":
            tank.turn_left()
        elif user_choice == "e":
            tank.turn_right()
        elif user_choice == "0":
            tank.shoot()
        elif user_choice == "8":
            tank.info()
        elif user_choice == "9":
            print("You have left the game.")
            break
        else:
            print("Only choices from above are allowed!")

menu()