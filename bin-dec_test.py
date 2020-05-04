import unittest
import bin_dec_converter

class MyTestCase(unittest.TestCase):
    def test_bin2dec(self):
        self.assertEqual(bin_dec_converter.bin2dec('10101'), int(0b10101))
        self.assertEqual(bin_dec_converter.bin2dec('10101010101'), int(0b10101010101))
        self.assertEqual(bin_dec_converter.bin2dec('11111111'), int(0b11111111))
        self.assertEqual(bin_dec_converter.bin2dec('00111'), int(0b00111))
        self.assertEqual(bin_dec_converter.bin2dec('11111110000'), int(0b11111110000))
        self.assertEqual(bin_dec_converter.bin2dec('0101010'), int(0b0101010))
        self.assertEqual(bin_dec_converter.bin2dec('11111111111111111'), int(0b11111111111111111))
        self.assertEqual(bin_dec_converter.bin2dec('0'), int(0b0))

    def test_dec2bin(self):
        self.assertEqual(bin_dec_converter.dec2bin(999999),   bin(999999)[2:])
        self.assertEqual(bin_dec_converter.dec2bin('00001'),  bin(1)[2:])
        self.assertEqual(bin_dec_converter.dec2bin(1234789),  bin(1234789)[2:])
        self.assertEqual(bin_dec_converter.dec2bin(0),        0)
        #self.assertEqual(bin_dec_converter.dec2bin(-3829),    bin(-3829)[2:])
        self.assertEqual(bin_dec_converter.dec2bin(8702),     bin(8702)[2:])

    def test_hex2dec(self):
        self.assertEqual(bin_dec_converter.hex2dec('deadbeef'),   0xdeadbeef)
        self.assertEqual(bin_dec_converter.hex2dec('DEADBEEF'),   0xDEADBEEF)
        self.assertEqual(bin_dec_converter.hex2dec(0),              0x0)
        self.assertEqual(bin_dec_converter.hex2dec('F00FBABE'),   0xF00FBABE)
        self.assertEqual(bin_dec_converter.hex2dec(12345),      0x12345)
        self.assertEqual(bin_dec_converter.hex2dec(999999),     0x999999)

if __name__ == '__main__':
    unittest.main()
