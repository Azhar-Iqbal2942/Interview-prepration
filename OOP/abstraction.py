from abc import ABC, abstractmethod


class InvalidOperationError(Exception):
    pass


class Stream(ABC):
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already open ")
        self.opened = True
        print("Stream is Open successfully")

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already closed")
        self.opened = False
        print("Stream is Closed successfully")

    @abstractmethod
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print("Data read from File.")


class NetworkStream(Stream):
    def read(self):
        print("Data read from Network.")


class MemoryStream(Stream):
    def read(self):
        print("Reading data from memory stream.")


stream = MemoryStream()
stream.open()
stream.read()
stream.close()
