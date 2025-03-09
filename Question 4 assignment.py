class Dog:
    def make_sound(self):
        return "Woof!"


class Cat:
    def make_sound(self):
        return "Meow!"


def process_sound(sound_object):
    """
    Processes a sound object by calling its make_sound() method.

    Args:
        sound_object: An object with a make_sound() method.

    Returns:
        The sound produced by the object.  Returns an error message if the object
        doesn't have a make_sound() method.
    """
    try:
        sound = sound_object.make_sound()
        print(f"The animal says: {sound}")
        return sound
    except AttributeError:
        return "Error: Object does not have a make_sound() method."


# Example usage
dog = Dog()
cat = Cat()

process_sound(dog)  # Output: The animal says: Woof!
process_sound(cat)  # Output: The animal says: Meow!


# Example of error handling
class Bird:
    def fly(self):
        return "I'm flying!"


bird = Bird()
process_sound(bird)  # Output: Error: Object does not have a make_sound() method.
