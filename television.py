class Television:
    # Default Numbers (DO NOT CHANGE)
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        """Initializes the TV. Uses default values."""
        self.__status = False
        self.__muted = False
        self.__volume = self.MIN_VOLUME
        self.__channel = self.MIN_CHANNEL

    def power(self): # Turns the tv off and on
        """Changes whether the TV is on or not."""
        self.__status = not self.__status  # Flips what is happening

    def mute(self): # Mutes the TV
        """Toggles the mute status of the TV."""
        if self.__status:  # Checks if the tv is on
            self.__muted = not self.__muted # Flips what is happening

    def channel_up(self): # Turns the channel up by 1
        """Changes the channel up by 1."""
        if self.__status: # Checks if the tv is on
            self.__channel = (self.__channel + 1) % (self.MAX_CHANNEL + 1) # Basically adds one to total

    def channel_down(self): # Turns the channel down by 1
        """Changes the channel down by 1."""
        if self.__status: # Checks if the tv is on
            self.__channel = (self.__channel - 1) % (self.MAX_CHANNEL + 1) # Decreases total by one

    def volume_up(self): # Turns the volume up by 1
        """Increases the volume by 1."""
        if self.__status: # Checks if the tv is on
            if self.__muted: # Checks to see if its muted
                self.__muted = False
            if self.__volume < self.MAX_VOLUME:  # Basically adds one to total
                self.__volume += 1

    def volume_down(self): # Turns the volume down by 1
        """Decreases the volume by 1."""
        if self.__status: # Checks if the tv is on
            if self.__muted: # Checks to see if its muted
                self.__muted = False
            if self.__volume > self.MIN_VOLUME:  # Decreases total by one
                self.__volume -= 1

    def __str__(self):
        """Gives the print statement for the current TV status."""
        status = "True" if self.__status else "False"
        volume = 0 if self.__muted else self.__volume
        return f"Power = {status}, Channel = {self.__channel}, Volume = {volume}"
