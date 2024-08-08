from src.bazpy.testing.testbase import TestBase


class TestBase_(TestBase):
    def test_has_basic_stuff(self):
        self.assertIsInstance(self.few, int)
        self.assertIsInstance(self.some, int)
        self.assertIsInstance(self.many, int)

    assertLen_cases = [
        (False, [], -1),
        (True, [], 0),
        (False, [], 1),
    ]

    def test_assertLen(self):
        for should, input, expect in self.assertLen_cases:
            with self.subTest():
                if should:
                    self.assertLen(input, expect)
                else:
                    self.assertFails(self.assertLen, input, expect)

    assertBetween_cases = [
        (False, 0.3, 1, 2.5),
        (True, 1.3, 1, 2.5),
        (False, 2.51, 1, 2.5),
    ]

    def test_assertLen(self):
        for should, value, lower, upper in self.assertBetween_cases:
            with self.subTest():
                if should:
                    self.assertBetween(value, lower, upper)
                else:
                    self.assertFails(self.assertBetween, value, lower, upper)
