import unittest

from tv.television import television


class TestTelevision(unittest.TestCase):
    def test_that_television_exist(self):
        my_tv = television()

    def test_that_television_is_off(self):
        my_tv = television()
        self.assertFalse(my_tv.tv_is_on())

    def test_that_television_is_on(self):
        my_tv = television()
        self.assertEqual(my_tv.tv_is_on(), False)
        my_tv.turn_on()
        self.assertEqual(my_tv.tv_is_on(), True)

    def test_that_Volume_Can_increase(self):
        my_tv = television()
        self.assertEqual(my_tv.tv_is_on(), False)
        my_tv.turn_on()
        self.assertEqual(my_tv.tv_is_on(), True)
        my_tv.increase_volume()
        self.assertEqual(my_tv.get_volume(), 1)

    def test_that_Volume_Can_increase_to_2(self):
        my_tv = television()
        self.assertEqual(my_tv.tv_is_on(), False)
        my_tv.turn_on()
        self.assertEqual(my_tv.tv_is_on(), True)

        my_tv.increase_volume()
        my_tv.increase_volume()
        self.assertEqual(my_tv.get_volume(), 2)

    def test_that_Volume_Can_increase_to_20(self):
        my_tv = television()
        self.assertEqual(my_tv.tv_is_on(), False)
        my_tv.turn_on()
        self.assertEqual(my_tv.tv_is_on(), True)
        for i in range(20):
            my_tv.increase_volume()
        self.assertEqual(my_tv.get_volume(), 20)

    def test_that_Volume_Can_increase_above_100(self):
        my_tv = television()
        self.assertEqual(my_tv.tv_is_on(), False)
        my_tv.turn_on()
        self.assertEqual(my_tv.tv_is_on(), True)
        for i in range(102):
            my_tv.increase_volume()
        self.assertEqual(my_tv.get_volume(), 100)

    def test_that_volume_Can_decrease_from_100_to_99(self):
        my_tv = television()
        self.assertEqual(my_tv.tv_is_on(), False)
        my_tv.turn_on()
        self.assertEqual(my_tv.tv_is_on(), True)
        for i in range(100):
            my_tv.increase_volume()
        self.assertEqual(my_tv.get_volume(), 100)
        my_tv.decrease_volume()
        self.assertEqual(my_tv.get_volume(), 99)

    def test_that_volume_Can_decrease_from_100_to_98(self):
        my_tv = television()
        self.assertEqual(my_tv.tv_is_on(), False)
        my_tv.turn_on()
        self.assertEqual(my_tv.tv_is_on(), True)
        for i in range(100):
            my_tv.increase_volume()
        self.assertEqual(my_tv.get_volume(), 100)
        for i in range(2):
            my_tv.decrease_volume()
        self.assertEqual(my_tv.get_volume(), 98)

    def test_that_volume_can_decrease_from_100_to_30(self):
        my_tv = television()
        self.assertEqual(my_tv.tv_is_on(), False)
        my_tv.turn_on()
        self.assertEqual(my_tv.tv_is_on(), True)
        for i in range(100):
            my_tv.increase_volume()
        self.assertEqual(my_tv.get_volume(), 100)
        for i in range(70):
            my_tv.decrease_volume()
        self.assertEqual(my_tv.get_volume(), 30)

    def test_that_volume_can_decrease_from_100_below_0(self):
        my_tv = television()
        self.assertEqual(my_tv.tv_is_on(), False)
        my_tv.turn_on()
        self.assertEqual(my_tv.tv_is_on(), True)
        for i in range(100):
            my_tv.increase_volume()
        self.assertEqual(my_tv.get_volume(), 100)
        for i in range(102):
            my_tv.decrease_volume()
        self.assertEqual(my_tv.get_volume(), 0)

    def test_to_channel_is_number_one(self):
        my_tv = television()
        self.assertEqual(my_tv.tv_is_on(), False)
        my_tv.turn_on()
        self.assertEqual(my_tv.tv_is_on(), True)
        self.assertEqual(my_tv.get_channel(), 1)

    def test_that_channel_as_changed_to_channel_two(self):
        my_tv = television()
        self.assertEqual(my_tv.tv_is_on(), False)
        my_tv.turn_on()
        self.assertEqual(my_tv.tv_is_on(), True)
        self.assertEqual(my_tv.get_channel(), 1)
        my_tv.channel_up()
        self.assertEqual(my_tv.get_channel(), 2)

    def test_that_channel_as_changed_to_channel_5(self):
        my_tv = television()
        self.assertEqual(my_tv.tv_is_on(), False)
        my_tv.turn_on()
        self.assertEqual(my_tv.tv_is_on(), True)
        self.assertEqual(my_tv.get_channel(), 1)
        for i in range(4):
            my_tv.channel_up()
        self.assertEqual(my_tv.get_channel(), 5)

    def test_that_channel_cant_be_changed_to_beyond_channel_10(self):
        my_tv = television()
        self.assertEqual(my_tv.tv_is_on(), False)
        my_tv.turn_on()
        self.assertEqual(my_tv.tv_is_on(), True)
        self.assertEqual(my_tv.get_channel(), 1)
        for i in range(11):
            my_tv.channel_up()
        self.assertEqual(my_tv.get_channel(), 10)

    def test_that_channel_can_reduce_from_channel_10_to9(self):
        my_tv = television()
        self.assertEqual(my_tv.tv_is_on(), False)
        my_tv.turn_on()
        self.assertEqual(my_tv.tv_is_on(), True)
        self.assertEqual(my_tv.get_channel(), 1)
        for i in range(9):
            my_tv.channel_up()
        self.assertEqual(my_tv.get_channel(), 10)
        my_tv.channel_down()
        self.assertEqual(my_tv.get_channel(), 9)

    def test_that_channel_can_reduce_from_channel_10_to_8(self):
        my_tv = television()
        self.assertEqual(my_tv.tv_is_on(), False)
        my_tv.turn_on()
        self.assertEqual(my_tv.tv_is_on(), True)
        self.assertEqual(my_tv.channel, 1)
        for i in range(9):
            my_tv.channel_up()
        self.assertEqual(my_tv.channel, 10)
        my_tv.channel_down()
        my_tv.channel_down()
        self.assertEqual(my_tv.channel, 8)

    def test_that_channel_cannot_reduce_from_channel_10_below_1(self):
        my_tv = television()
        self.assertEqual(my_tv.tv_is_on(), False)
        my_tv.turn_on()
        self.assertEqual(my_tv.tv_is_on(), True)
        self.assertEqual(my_tv.get_channel(), 1)
        for i in range(9):
            my_tv.channel_up()
        self.assertEqual(my_tv.get_channel(), 10)
        for i in range(12):
            my_tv.channel_down()
        self.assertEqual(my_tv.get_channel(), 1)
