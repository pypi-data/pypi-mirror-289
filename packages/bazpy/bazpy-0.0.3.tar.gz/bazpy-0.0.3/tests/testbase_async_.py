from src.bazpy.testing.testbase_async import TestBaseAsync


class Test_TestBaseAsync(TestBaseAsync):
    def test_inherits_basic_stuff(self):
        self.assertIsInstance(self.few, int)
        self.assertIsInstance(self.some, int)
        self.assertIsInstance(self.many, int)
