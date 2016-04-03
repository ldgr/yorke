

def byte_by_byte(file_descriptor):
    byte = file_descriptor.read(1)
    while byte:
        yield ord(byte)
        byte = file_descriptor.read(1)
    raise StopIteration


def recurrence_relation(mapping):
    def stream_generator(x0, starting_offset=1):
        x = x0
        for _ in xrange(starting_offset):
            x = mapping(x)
        while 1:
            x = mapping(x)
            yield x
    return stream_generator


class Xor(object):

    @classmethod
    def files(cls, left_fd, right_fd):
        left_stream = byte_by_byte(left_fd)
        right_stream = byte_by_byte(right_fd)
        for byte in cls.bytestreams(left_stream, right_stream):
            yield byte

    @classmethod
    def bytestreams(cls, left_stream, right_stream):
        while 1:
            left_byte = left_stream.next()
            right_byte = right_stream.next()
            yield left_byte ^ right_byte

    @classmethod
    def byte_list_to_string(cls, byte_list):
        return ''.join(chr(b) for b in byte_list)

    str = byte_list_to_string
