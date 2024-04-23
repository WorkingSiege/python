class Television:

  MIN_VOLUME = 0
  MAX_VOLUME = 2
  MIN_CHANNEL = 0
  MAX_CHANNEL = 3

    #docstring
  def __init__(self):        
    self.status = False
    self.muted = False
    self.volume = self.MIN_VOLUME
    self.channel = self.MIN_CHANNEL

   #docstring
  def power(self):
    self.status = not self.status
      
   #docstring      
  def mute(self):
    if self.status:
      self.muted = not self.muted

   #docstring
  def channel_up(self):
    if self.status:
      if self.channel < self.MAX_CHANNEL:
        self.channel += 1
      else:
        self.channel = self.MIN_CHANNEL

   #docstring
  def channel_down(self):
    if self.status:
      if self.channel > self.MIN_CHANNEL:
        self.channel -= 1
      else:
        self.channel = self.MAX_CHANNEL        

   #docstring  
  def volume_up(self):
    if self.status:
      if self.muted:
        self.muted = False
      if self.volume < self.MAX_VOLUME:
        self.volume += 1

   #docstring  
  def volume_down(self):
    if self.status:
      if self.muted:
        self.muted = False
      if self.volume > self.MIN_VOLUME:
        self.volume -= 1
  
  def __str__(self):
    if self.muted:
      volume_str = "0"
    else:
      volume_str = str(self.volume)
    return (
            f"Power: {self.status}\n"
            f"Channel: {self.channel}\n"
            f"Volume: {volume_str}\n"
        )