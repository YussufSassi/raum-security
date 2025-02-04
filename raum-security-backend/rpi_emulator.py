from random import randint


class RpiEmulator:
    red_light = False
    yellow_light = False
    green_light = False

    def __init__(self):
        pass

    def toggle_light(self, color: str):
        if color == "red":
            self.red_light = not self.red_light
        elif color == "yellow":
            self.yellow_light = not self.yellow_light
        elif color == "green":
            self.green_light = not self.green_light

    def read_card(self, should_succeed: bool):
        if should_succeed:
            return "1234567890"
        else:
            return None

    def observe_movement(self, should_have_movement: bool):
        return should_have_movement

    def ring_alarm(self, should_ring_alarm: bool):
        self.toggle_light("red")


rpi_emulator = RpiEmulator()
