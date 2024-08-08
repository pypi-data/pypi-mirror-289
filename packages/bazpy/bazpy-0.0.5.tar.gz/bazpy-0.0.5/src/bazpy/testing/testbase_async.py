from unittest import IsolatedAsyncioTestCase as AsyncCase
from .testbase import TestBase


class TestBaseAsync(TestBase, AsyncCase): ...
