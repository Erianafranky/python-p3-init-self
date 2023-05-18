#!/usr/bin/env python3

class Dog:
    def __init__ (self, name, breed="Mutt"):
        self.name = name
        self.breed = breed

luna = Dog("Luna")
luna.breed
#Mutt

bella = Dog("Bella", "Chihuahua")
bella.breed
#chihuahua

