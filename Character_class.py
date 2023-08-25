class Character:
  def __init__(self, posX, posY, health, stamina, isInAir, W, H, skin):
    self.centerx = posX
    self.centery = posY
    self.W = W
    self.H = H
    self.health = health
    self.stamina = stamina
    self.isInAir = isInAir
    self.skin = skin
