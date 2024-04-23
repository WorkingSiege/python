import unittest
from television import Television

class TeleTest(unittest.TestCase):
    def setUp(self):
        self.tv = Television()

    def test_init(self):
        self.assertFalse(self.tv.status)
        self.assertEqual(self.tv.volume, Television.MIN_VOLUME)
        self.assertEqual(self.tv.channel, Television.MIN_CHANNEL)

    def testPower(self):
        self.tv.power()
        self.assertTrue(self.tv.status)
        self.tv.power()
        self.assertFalse(self.tv.status)

    def testMute(self):
        self.tv.power()
        self.tv.volume_up()
        self.tv.mute()
        self.assertEqual(self.tv.muted, True)
        self.tv.mute()
        self.assertEqual(self.tv.muted, False)

    def testChUp(self):
        self.tv.channel_up()
        self.assertEqual(self.tv.channel, Television.MIN_CHANNEL)
        self.tv.power()
        self.tv.channel_up()
        self.assertEqual(self.tv.channel, Television.MIN_CHANNEL + 1)
        for i in range(Television.MAX_CHANNEL - Television.MIN_CHANNEL):
            self.tv.channel_up()
        self.assertEqual(self.tv.channel, Television.MIN_CHANNEL)

    def testChDw(self):
        self.tv.channel_down()
        self.assertEqual(self.tv.channel, Television.MIN_CHANNEL)
        self.tv.power()
        self.tv.channel_down()
        self.assertEqual(self.tv.channel, Television.MIN_CHANNEL - 1)
        for _ in range(Television.MAX_CHANNEL - Television.MIN_CHANNEL + 1):
            self.tv.channel_down()
        self.assertEqual(self.tv.channel, Television.MAX_CHANNEL)

    def testVolUp(self):
        self.tv.volume_up()
        self.assertEqual(self.tv.volume, Television.MIN_VOLUME)
        self.tv.power()
        self.tv.volume_up()
        self.assertEqual(self.tv.volume, Television.MIN_VOLUME + 1)
        self.tv.mute()
        self.tv.volume_up()
        self.assertEqual(self.tv.volume, Television.MIN_VOLUME + 2)
        for i in range(Television.MAX_VOLUME - Television.MIN_VOLUME + 1):
            self.tv.volume_up()
        self.assertEqual(self.tv.volume, Television.MAX_VOLUME)

    def testVolDw(self):
        self.tv.volume_down()
        self.assertEqual(self.tv.volume, Television.MIN_VOLUME)
        self.tv.power()
        self.tv.volume_up()
        self.tv.volume_down()
        self.assertEqual(self.tv.volume, Television.MAX_VOLUME - 1)
        self.tv.mute()
        self.tv.volume_down()
        self.assertEqual(self.tv.volume, Television.MIN_VOLUME)
        for _ in range(Television.MAX_VOLUME - Television.MIN_VOLUME + 1):
            self.tv.volume_down()
        self.assertEqual(self.tv.volume, Television.MIN_VOLUME)

if __name__ == "__main__":
    unittest.main()

