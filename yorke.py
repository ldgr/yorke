from random import randint


def byte_by_byte(file_descriptor):
    byte = file_descriptor.read(1)
    while byte:
        yield ord(byte)
        byte = file_descriptor.read(1)
    raise StopIteration


class Xor(object):

    @classmethod
    def strings(cls, left, right):
        return [ord(l) ^ ord(r) for l, r in zip(left, right)]

    @classmethod
    def bytestreams(cls, left_stream, right_stream):
        while 1:
            left_byte = left_stream.next()
            right_byte = right_stream.next()
            yield left_byte ^ right_byte

    @classmethod
    def files(cls, left_fd, right_fd):
        left_stream = byte_by_byte(left_fd)
        right_stream = byte_by_byte(right_fd)
        for byte in cls.bytestreams(left_stream, right_stream):
            yield byte

    @classmethod
    def byte_list_to_string(cls, byte_list):
        return ''.join(chr(b) for b in byte_list)

    str = byte_list_to_string


class RandomPad(object):

    def __init__(self):
        self.key_bytes = []
        self.cipher_bytes = []

    def encrypt_bytes(self, byte_stream):
        for byte in byte_stream:
            random_byte = randint(0, 255)
            self.key_bytes.append(random_byte)
            self.cipher_bytes.append(byte ^ random_byte)
        return self

    def encrypt_string(self, plain_text):
        return self.encrypt_bytes(map(ord, plain_text))

    @property
    def key_text(self):
        return Xor.str(self.key_bytes)

    @property
    def cipher_text(self):
        return Xor.str(self.cipher_bytes)
