from StringIO import StringIO
from unittest import TestCase

from yorke import RandomPad, Xor


class TestXor(TestCase):

    def test_strings(self):
        str1 = '\xff\xfe\xfb'
        str2 = '\xfb\xfe\xff'
        xord = Xor.strings(str1, str2)
        self.assertEqual(xord, [4, 0, 4])

    def test_bytestreams(self):
        stream1 = iter(map(ord, '\xff\xfe\xfb'))
        stream2 = iter(map(ord, '\xfb\xfe\xff'))
        xord = Xor.bytestreams(stream1, stream2)
        self.assertEqual(Xor.str(xord), '\x04\x00\x04')

    def test_files(self):
        fd1 = StringIO('\xff\xfe\xfb')
        fd2 = StringIO('\xfb\xfe\xff')
        xord = Xor.files(fd1, fd2)
        self.assertEqual(list(xord), [4, 0, 4])

    def test_byte_list_to_string(self):
        self.assertEqual(
            Xor.byte_list_to_string([68, 51, 52, 68, 66, 69, 69, 70]),
            'D34DBEEF'
        )

    def test_str_alias(self):
        self.assertEqual(Xor.str, Xor.byte_list_to_string)


class TestRandomPad(TestCase):

    def test_encrypt(self):
        rp = RandomPad()
        self.assertEqual(rp.key_bytes, [])
        self.assertEqual(rp.cipher_bytes, [])

        plain = 'More secret than top secret'
        self.assertEqual(rp, rp.encrypt_string(plain))
        self.assertEqual(
            rp.cipher_bytes,
            [ord(c) ^ b for c, b in zip(plain, rp.key_bytes)]
        )
        self.assertEqual(rp.key_text, ''.join(map(chr, rp.key_bytes)))
        self.assertEqual(rp.cipher_text, ''.join(map(chr, rp.cipher_bytes)))
        self.assertEqual(
            Xor.str(Xor.strings(rp.key_text, rp.cipher_text)),
            plain
        )
