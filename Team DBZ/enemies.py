class Enemy:
    """Base class for all enemies."""

    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def is_alive(self):
        return self.hp > 0


class Seth(Enemy):
    def __init__(self):
        super().__init__(name="Seth Reed", hp=50, damage=5)