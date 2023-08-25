class Character:
  def __init__(self, posX, posY, health, stamina, defence, dmg, W, H, skin,  isInAir, isOnIce, isInWater, isFlying, isSprinting, o2):
    self.centerx = posX
    self.centery = posY
    self.W = W
    self.H = H
    self.health = health
    self.stamina = stamina
    self.defence = defence
    self.dmg = dmg
    self.isInAir = isInAir
    self.skin = skin
    self.isOnice = isOnIce
    self.isInWater = isInWater
    self.isFlying = isFlying
    self.isSprinting = isSprinting
    self.o2 = o2
