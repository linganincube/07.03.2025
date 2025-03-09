from abc import ABC, abstractmethod

# Abstract Base Class (ABC) for FileHandler
class FileHandler(ABC):
    @abstractmethod
    def read(self):
        """Abstract method to read a file."""
        pass

    @abstractmethod
    def write(self, data):
        """Abstract method to write data to a file."""
        pass

# Concrete class for handling text files
class TextFileHandler(FileHandler):
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        """Reads the contents of a text file."""
        with open(self.filename, 'r') as file:
            return file.read()

    def write(self, data):
        """Writes data to a text file."""
        with open(self.filename, 'w') as file:
            file.write(data)

# Concrete class for handling binary files
class BinaryFileHandler(FileHandler):
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        """Reads the contents of a binary file."""
        with open(self.filename, 'rb') as file:
            return file.read()

    def write(self, data):
        """Writes data to a binary file."""
        with open(self.filename, 'wb') as file:
            file.write(data)

# Example usage
if __name__ == "__main__":
    # Text file example
    text_handler = TextFileHandler("example.txt")
    text_handler.write("Hello, this is a text file!")
    print("Text file content:", text_handler.read())

    # Binary file example
    binary_handler = BinaryFileHandler("example.bin")
    binary_handler.write(b"Hello, this is a binary file!")
    print("Binary file content:", binary_handler.read())