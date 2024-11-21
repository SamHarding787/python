class Television:
    # Default Numbers (DO NOT CHANGE)
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        """Initializes the TV. Uses default values."""
        self._status = False
        self._muted = False
        self._volume = self.MIN_VOLUME
        self._channel = self.MIN_CHANNEL

    def power(self):
        """Changes whether the TV is on or not."""
        self._status = not self._status

    def mute(self):
        """Toggles the mute status of the TV."""
        if self._status:
            self._muted = not self._muted

    def channel_up(self):
        """Changes the channel up by 1."""
        if self._status:
            self._channel = (self._channel + 1) % (self.MAX_CHANNEL + 1)

    def channel_down(self):
        """Changes the channel down by 1."""
        if self._status:
            self._channel = (self._channel - 1) % (self.MAX_CHANNEL + 1)

    def volume_up(self):
        """Increases the volume by 1."""
        if self._status:
            if self._muted:
                self._muted = False
            if self._volume < self.MAX_VOLUME:
                self._volume += 1

    def volume_down(self):
        """Decreases the volume by 1."""
        if self._status:
            if self._muted:
                self._muted = False
            if self._volume > self.MIN_VOLUME:
                self._volume -= 1

    def __str__(self):
        """Gives the print statement for the current TV status."""
        status = "True" if self._status else "False"
        volume = 0 if self._muted else self._volume
        return f"Power = {status}, Channel = {self._channel}, Volume = {volume}"
