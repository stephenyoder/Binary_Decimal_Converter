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

    def test_isBinary(self):
        self.assertFalse(bin_dec_converter.isBinary('abcdef'))
        self.assertFalse(bin_dec_converter.isBinary('101fja'))
        self.assertFalse(bin_dec_converter.isBinary('#@104700'))
        self.assertTrue(bin_dec_converter.isBinary('101010101'))
        self.assertTrue(bin_dec_converter.isBinary('000001111'))
        self.assertTrue(bin_dec_converter.isBinary('111110000'))
        self.assertFalse(bin_dec_converter.isBinary('1010101a'))
        self.assertFalse(bin_dec_converter.isBinary('a101010101'))
        self.assertFalse(bin_dec_converter.isBinary(''))
        self.assertFalse(bin_dec_converter.isBinary('-$#@'))

    def test_isDecimal(self):
        self.assertFalse(bin_dec_converter.isDecimal('abcd'))
        self.assertFalse(bin_dec_converter.isDecimal('101fja'))
        self.assertFalse(bin_dec_converter.isDecimal('#@104700'))
        self.assertTrue(bin_dec_converter.isDecimal('101010101'))
        self.assertTrue(bin_dec_converter.isDecimal('0123456789'))
        self.assertTrue(bin_dec_converter.isDecimal('111110000'))
        self.assertFalse(bin_dec_converter.isDecimal('-10101'))
        self.assertFalse(bin_dec_converter.isDecimal('a101010101'))
        self.assertFalse(bin_dec_converter.isDecimal(''))
        self.assertFalse(bin_dec_converter.isDecimal('$#@'))
        self.assertFalse(bin_dec_converter.isDecimal('0.342'))
        self.assertFalse(bin_dec_converter.isDecimal('-0.342'))

    def test_is_hex(self):
        self.assertTrue(bin_dec_converter.is_hex('abcd'))
        self.assertFalse(bin_dec_converter.is_hex('101fja'))
        self.assertFalse(bin_dec_converter.is_hex('#@104700'))
        self.assertTrue(bin_dec_converter.is_hex('101010101'))
        self.assertTrue(bin_dec_converter.is_hex('0123456789'))
        self.assertTrue(bin_dec_converter.is_hex('111110000'))
        self.assertTrue(bin_dec_converter.is_hex('abcdef1234567890'))
        self.assertFalse(bin_dec_converter.is_hex('abcdefg1234570'))
        self.assertTrue(bin_dec_converter.is_hex('f00fbabe'))
        self.assertFalse(bin_dec_converter.is_hex('-10101'))
        self.assertTrue(bin_dec_converter.is_hex('deadbeef'))
        self.assertFalse(bin_dec_converter.is_hex(''))
        self.assertFalse(bin_dec_converter.is_hex('$#@'))
        self.assertFalse(bin_dec_converter.is_hex('0.342'))
        self.assertFalse(bin_dec_converter.is_hex('-0.342'))
        self.assertFalse(bin_dec_converter.is_hex('-f00fbabe'))


if __name__ == '__main__':
    unittest.main()
