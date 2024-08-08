from unittest import IsolatedAsyncioTestCase as AsyncCase
from src.bazpy.testing.testbase import TestBase


class TestBaseAsync(TestBase, AsyncCase): ...
