from piglatin import firstvowel, switch, pig, punct
import unittest

class TestMethods(unittest.TestCase):

    def setUp(self):
        pass

    def test_firstvowel(self):
        '''
        testing if the firstvowel index is being returned correctly
        '''
        self.assertEqual(firstvowel('hi'), 1)
        self.assertEqual(firstvowel('hello'), 1)
        self.assertEqual(firstvowel('Awkward'.lower()), 0)
        self.assertEqual(firstvowel('https'), -1)
        self.assertEqual(firstvowel('Psychotic'.lower()), 2)

    def test_switch(self):
        '''
        testing the switching of values
        '''
        self.assertEqual(switch('hey', 'you'), 'youhey')
        self.assertEqual(switch('ping', 'pong'), 'pongping')
        self.assertEqual(switch('123', '456'), '456123')

    def test_pig(self):
        '''
        testing the translation to piglattin
        '''
        self.assertEqual(pig('hey how are you today'), 'eyhay owhay areyay youyay odaytay')
        self.assertEqual(pig('I went To buy: oranges, Mangoes, peache$'), 'IYAY entway Otay uybay: orangesyay, Angoesmay, eachepay$')
        self.assertEqual(pig('phone'), 'onephay')
        self.assertEqual(pig('haPpyeR'), 'appyerhay')

    def test_punct(self):
        '''
        testing punctuations trailing words
        '''
        self.assertEqual(punct(']'), 1)
        self.assertEqual(punct('7'), 0)
        self.assertEqual(punct('A'), 0)

unittest.main()
