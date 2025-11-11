"""
COMP 163 - Project 2: Character Abilities Showcase
Name: Sydney Brown
Date: 11/8/2025

AI Usage: [Document any AI assistance used]
Example: AI helped with inheritance structure and method overriding concepts
"""

# ============================================================================
# PROVIDED BATTLE SYSTEM (DO NOT MODIFY)
# ============================================================================
import random
class SimpleBattle:
    """
    Simple battle system provided for you to test your characters.
    DO NOT MODIFY THIS CLASS - just use it to test your character implementations.
    """
    
    def __init__(self, character1, character2):
        self.char1 = character1
        self.char2 = character2
    
    def fight(self):
        """Simulates a simple battle between two characters"""
        print(f"\n=== BATTLE: {self.char1.name} vs {self.char2.name} ===")
        
        # Show starting stats
        print("\nStarting Stats:")
        self.char1.display_stats()
        self.char2.display_stats()
        
        print(f"\n--- Round 1 ---")
        print(f"{self.char1.name} attacks:")
        self.char1.attack(self.char2)
        
        if self.char2.health > 0:
            print(f"\n{self.char2.name} attacks:")
            self.char2.attack(self.char1)
        
        print(f"\n--- Battle Results ---")
        self.char1.display_stats()
        self.char2.display_stats()
        
        if self.char1.health > self.char2.health:
            print(f"🏆 {self.char1.name} wins!")
        elif self.char2.health > self.char1.health:
            print(f"🏆 {self.char2.name} wins!")
        else:
            print("🤝 It's a tie!")

# ============================================================================
# YOUR CLASSES TO IMPLEMENT (6 CLASSES TOTAL)
# ============================================================================

class Character:
    """
    Base class for all character types.
    Stores the core stats (name, health, strength, magic) and
    provides universal functions that all characters share.
    """
    
    def __init__(self, name, health, strength, magic):
        """ Initializes a basic character with the essential stats. Every character in the game has these four values. """
        self.name = name
        self.health = health
        self.strength = strength
        self.magic = magic
        
    def attack(self, target):
        """
        Basic attack method that all characters can use.
        1. Calculate damage based on strength
        2. Apply damage to the target
        3. Print what happened
        """
        damage = self.strength
        print(f"{self.name} attacks {target.name} for {damage} damage!")
        target.take_damage(damage)
        
    def take_damage(self, damage):
        """
        Reduces this character's health by the damage amount.
        Health should never go below 0.
        Returns the actual damage dealt (useful for logs/feedback).
        """
        damage_taken = damage
        self.health -= damage
        if self.health < 0:
            # If health went below zero, the actual damage taken is less
            damage_taken = damage + self.health # health is negative here, so adding it reduces damage
            self.health = 0
        return damage_taken
        
    def display_stats(self):
        """
        Prints the character's current stats in a nice format. Used to show character information before and after battles.
        """
        print(f"--- {self.name} ---")
        print(f"Health:    {self.health}")
        print(f"Strength: {self.strength}")
        print(f"Magic:    {self.magic}")

class Player(Character):
    """
    Base class for player characters.
    Inherits from Character and adds player-specific features (Class, Level, XP, Weapon).
    """
    
    def __init__(self, name, character_class, health, strength, magic, weapon=None):
        """
        Initialize a player character, including their equipped weapon (Composition).
        """
        super().__init__(name, health, strength, magic)
        self.character_class = character_class
        
        # Composition: Player HAS a Weapon object
        self.weapon = weapon
        
        # Optional but recommended attributes
        self.level = 1
        self.experience = 0
        
    def display_stats(self):
        """
        Override the parent's display_stats to show additional player info, including the weapon.
        """
        super().display_stats()  # Shows name, health, strength, magic
        print(f"Class:     {self.character_class}")
        
        # Display weapon information
        if self.weapon:
             print(f"Weapon:    {self.weapon.name} (+{self.weapon.damage_bonus} DMG)")
        else:
             print(f"Weapon:    Unarmed")

        print(f"Level:     {self.level}")
        print(f"XP:        {self.experience}")

class Warrior(Player):
    """
    Warrior class - strong physical fighter.
    Inherits from Player.
    """
    
    def __init__(self, name, weapon=None):
        """
        Create a warrior with appropriate stats, passing the weapon to the Player constructor.
        Warriors should have: high health, high strength, low magic
        """
        super().__init__(name, "Warrior", health=120, strength=15, magic=5, weapon=weapon)
        
    def attack(self, target):
        """
        Override the basic attack. Warrior attack = Strength + 5 + Weapon Bonus.
        """
        # Base damage calculation
        damage = self.strength + 5
        
        # Add weapon bonus if equipped
        weapon_name = "fists"
        if self.weapon:
            damage += self.weapon.damage_bonus
            weapon_name = self.weapon.name

        print(f"{self.name} performs a mighty strike with their {weapon_name} on {target.name} for {damage} damage!")
        target.take_damage(damage)
        
    def power_strike(self, target):
        """
        Special warrior ability - a powerful attack that does extra damage.
        """
        damage = self.strength + 10
        if self.weapon:
             damage += self.weapon.damage_bonus # Power Strike also benefits from the weapon

        print(f"{self.name} uses POWER STRIKE on {target.name} for {damage} damage!!")
        target.take_damage(damage)

class Mage(Player):
    """
    Mage class - magical spellcaster.
    Inherits from Player.
    """
    
    def __init__(self, name, weapon=None):
        """
        Create a mage with appropriate stats, passing the weapon to the Player constructor.
        Mages should have: low health, low strength, high magic
        """
        super().__init__(name, "Mage", health=80, strength=8, magic=20, weapon=weapon)
        
    def attack(self, target):
        """
        Override the basic attack. Mage attack is primarily Magic-based + Weapon Bonus.
        """
        # Base damage calculation: based on magic
        damage = self.magic
        
        # Add weapon bonus (even a staff gives bonus magic power)
        weapon_name = "hands"
        if self.weapon:
            damage += self.weapon.damage_bonus
            weapon_name = self.weapon.name

        print(f"{self.name} casts a magic bolt using their {weapon_name} at {target.name} for {damage} damage!")
        target.take_damage(damage)
        
    def fireball(self, target):
        """
        Special mage ability - a powerful magical attack.
        """
        damage = self.magic + 10
        if self.weapon:
            damage += self.weapon.damage_bonus

        print(f"{self.name} hurls a FIREBALL at {target.name} for {damage} damage!!")
        target.take_damage(damage)

class Rogue(Player):
    """
    Rogue class - quick and sneaky fighter.
    Inherits from Player.
    """
    
    def __init__(self, name, weapon=None):
        """
        Create a rogue with appropriate stats, passing the weapon to the Player constructor.
        Rogues should have: medium health, medium strength, medium magic
        """
        super().__init__(name, "Rogue", health=90, strength=12, magic=10, weapon=weapon)
        
    def attack(self, target):
        """
        Override the basic attack. Rogue has a chance for extra damage (critical hits) + Weapon Bonus.
        """
        damage = self.strength
        
        # Add weapon bonus
        if self.weapon:
            damage += self.weapon.damage_bonus

        if random.randint(1, 10) <= 3:
            # Critical hit: double the total base damage (including weapon)
            damage *= 2
            print(f"{self.name} lands a CRITICAL HIT on {target.name} for {damage} damage!")
        else:
            print(f"{self.name} swiftly attacks {target.name} for {damage} damage.")
        
        target.take_damage(damage)
        
    def sneak_attack(self, target):
        """
        Special rogue ability - guaranteed critical hit (double damage + weapon bonus).
        """
        damage = self.strength
        if self.weapon:
            damage += self.weapon.damage_bonus
            
        damage *= 2 # Guaranteed double damage
        
        print(f"{self.name} performs a SNEAK ATTACK on {target.name} for {damage} damage!!")
        target.take_damage(damage)

class Weapon:
    """
    Weapon class to demonstrate composition.
    Characters can HAVE weapons (composition, not inheritance).
    """
    
    def __init__(self, name, damage_bonus):
        """
        Create a weapon with a name and damage bonus.
        """
        self.name = name
        self.damage_bonus = damage_bonus
        
    def display_info(self):
        """
        Display information about this weapon.
        """
        print(f"Weapon: {self.name} | Damage Bonus: {self.damage_bonus}")

# The AdvancedWeapon class is removed to simplify the solution and focus on required classes.

# ============================================================================
# MAIN PROGRAM FOR TESTING (YOU CAN MODIFY THIS FOR TESTING)
# ============================================================================

if __name__ == "__main__":
    print("=== CHARACTER ABILITIES SHOWCASE ===")
    print("Testing inheritance, polymorphism, and composition")
    print("=" * 50)
    
    # 1. Create Weapons
    sword = Weapon("Iron Sword", 10)
    staff = Weapon("Magic Staff", 15)
    dagger = Weapon("Steel Dagger", 8)

    # 2. Create and equip characters (Composition)
    warrior = Warrior("Sir Galahad", weapon=sword)
    mage = Mage("Merlin", weapon=staff)
    rogue = Rogue("Robin Hood", weapon=dagger)
    
    # Display their stats (now includes weapon info)
    print("\n📊 Character Stats (Equipped):")
    warrior.display_stats()
    mage.display_stats()
    rogue.display_stats()
    
    # Polymorphism test
    print("\n⚔️ Testing Polymorphism (Attacks now include Weapon Bonus):")
    # Health must be reset for each test
    dummy_target = Character("Target Dummy", 1000, 0, 0) 
    
    for character in [warrior, mage, rogue]:
        print(f"\n{character.name} attacks the dummy:")
        character.attack(dummy_target)
        dummy_target.health = 1000  # Reset dummy to high health
    
    # Special abilities
    print("\n✨ Testing Special Abilities (Now include Weapon Bonus):")
    target1 = Character("Enemy1", 50, 0, 0)
    target2 = Character("Enemy2", 50, 0, 0)
    target3 = Character("Enemy3", 50, 0, 0)
    
    warrior.power_strike(target1)
    mage.fireball(target2)
    rogue.sneak_attack(target3)
    
    # Weapon composition info
    print("\n🗡️ Weapon Info:")
    sword.display_info()
    staff.display_info()
    dagger.display_info()
    
    # Battle system test
    print("\n⚔️ Testing Battle System (Warrior vs Mage):")
    # Re-create characters for a fresh battle test
    warrior_battle = Warrior("Sir Lancelot", weapon=Weapon("Greatsword", 12))
    mage_battle = Mage("Gandalf", weapon=Weapon("Oak Staff", 13))

    battle = SimpleBattle(warrior_battle, mage_battle)
    battle.fight()
    
    print("\n✅ Testing complete!")
