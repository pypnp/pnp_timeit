import json
import time
import unittest
import logging
from io import StringIO

from pnp_timeit.pnp_timeit import Pnp_Timeit


class TestClass:
    @Pnp_Timeit.timeit
    def sleep_seconds(self, pi_seconds):
        time.sleep(pi_seconds)
        


class TestPnpTimeit(unittest.TestCase):

    def setUp(self):
        """
        Setup test environment
        """
        self.stream = StringIO()
        self.handler = logging.StreamHandler(self.stream)
        self.log = logging.getLogger(Pnp_Timeit.LOGGER_NAME)
        self.log.setLevel(logging.DEBUG)
        for handler in self.log.handlers: 
            self.log.removeHandler(handler)
        self.log.addHandler(self.handler)


    def __test_pnp_timeit(self, pi_seconds):
        """
        test timeit function, function execute given <pi_seconds> time 
        """
        Pnp_Timeit.enable()

        test_value = pi_seconds
        TestClass().sleep_seconds(test_value)

        time_info = self.stream.getvalue()

        test_seconds = json.loads(time_info).get('time_cost_seconds')
        test_value = int(test_seconds)
        expect_value = pi_seconds
        self.assertEqual(expect_value, test_value)


    def test_pnp_timeit_1_seconds(self):
        """
        test function that execute 1 second
        """
        self.__test_pnp_timeit(1)


    def test_pnp_timeit_3_seconds(self):
        """
        test function that execute 3 seconds
        """
        self.__test_pnp_timeit(3)


    def tearDown(self):
        """
        Tear down test environment
        """
        self.log.removeHandler(self.handler)
        self.handler.close()
