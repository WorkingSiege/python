class Television:

  MIN_VOLUME :int = 0
  MAX_VOLUME :int= 2
  MIN_CHANNEL :int = 0
  MAX_CHANNEL :int= 3

  def __init__(self):     
    """
    Initializes a Television object.

    __status (bool) The power status of the television.
    __muted (bool): Whether the television is muted.
    __volume (int): The current volume level.
    __channel (int): The current channel.
    """   
    self.__status :bool = False
    self.__muted :bool = False
    self.__volume :int = self.MIN_VOLUME
    self.__channel :int = self.MIN_CHANNEL

  def power(self) -> None:
    """Toggle the power status of the television."""
    self.__status = not self.__status
        
  def mute(self) -> None:
    """Toggle the mute status of the television if it's powered on."""
    if self.__status:
      self.__muted = not self.__muted

  def channel_up(self) -> None:
    """Switch to the next channel if the television is powered on."""
    if self.__status:
      if self.__channel < self.MAX_CHANNEL:
        self.__channel += 1
      else:
        self.__channel = self.MIN_CHANNEL

  def channel_down(self) -> None:
    """Switch to the previous channel if the television is powered on."""
    if self.__status:
      if self.__channel > self.MIN_CHANNEL:
        self.__channel -= 1
      else:
        self.__channel = self.MAX_CHANNEL        

  def volume_up(self) -> None:
    """Increase the volume by one level if the television is powered on and not muted."""
    if self.__status:
      if self.__muted:
        self.__muted = False
      if self.__volume < self.MAX_VOLUME:
        self.__volume += 1

  def volume_down(self) -> None:
    """Decrease the volume by one level if the television is powered on and not muted."""
    if self.__status:
      if self.__muted:
        self.__muted = False
      if self.__volume > self.MIN_VOLUME:
        self.__volume -= 1
  
  def __str__(self) -> str:
    """Prints the current Power, Channel, and Volume statuses of the TV.
       If the TV is muted Volume adjustment to 0 is done here.  
    """
    if self.__muted:
      volume_str = "0"
    else:
      volume_str = str(self.__volume)
    return (
            f"Power = {self.__status}, " f"Channel = {self.__channel}, " f"Volume = {volume_str}"
        )