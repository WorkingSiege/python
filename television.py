class Television:

  MIN_VOLUME = 0
  MAX_VOLUME = 2
  MIN_CHANNEL = 0
  MAX_CHANNEL = 3

  def __init__(self):        
    self.__status = False
    self.__muted = False
    self.__volume = self.MIN_VOLUME
    self.__channel = self.MIN_CHANNEL

    """
    Initialize a Television object.

    Attributes:
        __status (bool): The power status of the television.
        __muted (bool): Whether the television is muted.
        __volume (int): The current volume level.
        __channel (int): The current channel.
    """
  def power(self):
    """Toggle the power status of the television."""
    self.__status = not self.__status
        
  def mute(self):
    """Toggle the mute status of the television if it's powered on."""
    if self.__status:
      self.__muted = not self.__muted

  def channel_up(self):
    """Switch to the next channel if the television is powered on."""
    if self.__status:
      if self.__channel < self.MAX_CHANNEL:
        self.__channel += 1
      else:
        self.__channel = self.MIN_CHANNEL

  def channel_down(self):
    """Switch to the previous channel if the television is powered on."""
    if self.__status:
      if self.__channel > self.MIN_CHANNEL:
        self.__channel -= 1
      else:
        self.__channel = self.MAX_CHANNEL        

  def volume_up(self):
    """Increase the volume by one level if the television is powered on and not muted."""
    if self.__status:
      if self.__muted:
        self.__muted = False
      if self.__volume < self.MAX_VOLUME:
        self.__volume += 1

  def volume_down(self):
    """Decrease the volume by one level if the television is powered on and not muted."""
    if self.__status:
      if self.__muted:
        self.__muted = False
      if self.__volume > self.MIN_VOLUME:
        self.__volume -= 1
  
  def __str__(self):
    if self.__muted:
      volume_str = "0"
    else:
      volume_str = str(self.__volume)
    return (
            f"Power = {self.__status}, " f"Channel = {self.__channel}, " f"Volume = {volume_str}"
        )