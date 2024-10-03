class television:

    def __init__(self):
        self.is_on = False
        self.channel = 1
        self.volume = 0

    def turn_off(self):
        self.is_on = False

    def turn_on(self):
        self.is_on = True

    def tv_is_on(self):
        return self.is_on

    def increase_volume(self):
        try:
            if self.volume < 100:
                self.volume += 1
        except ValueError:
            print('Volume must be between 1 and 100')

    def decrease_volume(self):
        if 100 >= self.volume > 0:
            self.volume -= 1

    def channel_up(self):
        if self.channel < 10:
            self.channel += 1

    def channel_down(self):
        if 10 >= self.channel > 1:
            self.channel -= 1

    def get_volume(self):
        return self.volume

    def get_channel(self):
        return self.channel
