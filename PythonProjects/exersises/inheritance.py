def main():
    class Animal:
        def __init__(self,habitat):
            self.habitat = habitat

        def habitats(self):
            print(self.habitat)
        @staticmethod
        def sounds():
            print("SOME ANIMAL SOUND")


    class Dog(Animal):
        def __init__(self):
            super().__init__("Kennel")

        @staticmethod
        def sounds():
            print("Woof Woof!")

    shep = Dog()
    shep.habitats()
    shep.sounds()

if __name__ == "__main__":
    main()