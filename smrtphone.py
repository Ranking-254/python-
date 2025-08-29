# Parent class
class Smartphone:
    def __init__(self, brand, model, battery_level=100):
        self.brand = brand
        self.model = model
        self.__battery_level = battery_level  # private (encapsulation)

    def show_info(self):
        return f"{self.brand} {self.model} | Battery: {self.__battery_level}%"

    def charge(self, amount):
        self.__battery_level = min(100, self.__battery_level + amount)
        return f"Charging... Battery now at {self.__battery_level}%"

    def use(self, amount):
        if self.__battery_level - amount < 0:
            return f"Battery too low! Please charge."
        else:
            self.__battery_level -= amount
            return f"Using phone... Battery now at {self.__battery_level}%"

    # Getter (encapsulation)
    def get_battery_level(self):
        return self.__battery_level


# Child class (Inheritance)
class SmartPhoneWithCamera(Smartphone):
    def __init__(self, brand, model, battery_level=100, camera_megapixels=12):
        super().__init__(brand, model, battery_level)  # inherit parent
        self.camera_megapixels = camera_megapixels

    # Polymorphism: override show_info()
    def show_info(self):
        base_info = super().show_info()
        return f"{base_info} | Camera: {self.camera_megapixels}MP"

    def take_photo(self):
        return f"📸 Photo taken with {self.camera_megapixels}MP camera!"


# Example usage
if __name__ == "__main__":
    phone1 = Smartphone("Samsung", "Galaxy S23", 80)
    phone2 = SmartPhoneWithCamera("Apple", "iPhone 14 Pro", 90, 48)

    print(phone1.show_info())
    print(phone1.use(30))
    print(phone1.charge(20))

    print("\n--- With Camera ---")
    print(phone2.show_info())
    print(phone2.take_photo())
    print(phone2.use(50))
