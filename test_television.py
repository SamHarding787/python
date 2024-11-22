from television import Television
import unittest

class Test_Television(unittest.TestCase):

    def test_init(self):
        """Testing the init"""
        tv = Television()
        self.assertFalse(tv._status, "TV should start off.")
        self.assertFalse(tv._muted, "TV should start unmuted.")
        self.assertEqual(tv._volume, Television.MIN_VOLUME, "Volume should start at minimum.")
        self.assertEqual(tv._channel, Television.MIN_CHANNEL, "Channel should start at minimum.")

    def test_power(self):
        """Testing power"""
        tv = Television()
        tv.power()
        self.assertTrue(tv._status, "TV should be on after calling power.")
        tv.power()
        self.assertFalse(tv._status, "TV should be off after calling power again.")

    def test_channel_up(self):
        """Testing channel_up"""
        tv = Television()
        tv.power()  # Turn on the TV
        tv.channel_up()
        self.assertEqual(tv._channel, 1, "Channel should increment by 1.")
        tv._channel = Television.MAX_CHANNEL
        tv.channel_up()
        self.assertEqual(tv._channel, Television.MIN_CHANNEL, "Channel should wrap to minimum.")

    def test_channel_down(self):
        """Testing channel_down"""
        tv = Television()
        tv.power()  # Turn on the TV
        tv.channel_down()
        self.assertEqual(tv._channel, Television.MAX_CHANNEL, "Channel should wrap to maximum.")
        tv._channel = 1
        tv.channel_down()
        self.assertEqual(tv._channel, 0, "Channel should decrement by 1.")

    def test_volume_up(self):
        """Testing volume_up"""
        tv = Television()
        tv.power()  # Turn on the TV
        tv.volume_up()
        self.assertEqual(tv._volume, 1, "Volume should increment by 1.")
        tv._volume = Television.MAX_VOLUME
        tv.volume_up()
        self.assertEqual(tv._volume, Television.MAX_VOLUME, "Volume should stay at maximum.")

    def test_volume_down(self):
        """Testing volume_down"""
        tv = Television()
        tv.power()  # Turn on the TV
        tv.volume_down()
        self.assertEqual(tv._volume, Television.MIN_VOLUME, "Volume should stay at minimum.")
        tv._volume = 1
        tv.volume_down()
        self.assertEqual(tv._volume, 0, "Volume should decrement by 1.")
