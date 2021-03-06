import unittest
import sys

sys.path.insert(1, '../')
from enums.servicetype import ServiceType


class MyTestCase(unittest.TestCase):

    def test_stringToEnum(self):
        enum = ServiceType.translate('drycleaning')
        self.assertEqual(ServiceType.DRYCLEANING, enum)
        enum = ServiceType.translate('DRYCLEANING')
        self.assertEqual(ServiceType.DRYCLEANING, enum)
        try:
            enum = ServiceType.translate('wqeq')
        except ValueError as ve:
            print(ve)
            print('found ve')

    def test_drycleaning(self):
        enum = ServiceType.DRYCLEANING
        self.assertEqual('DRYCLEANING', enum.name)
        self.assertEqual(1, enum.value)

    def test_rx(self):
        enum = ServiceType.RX
        self.assertEqual('RX', enum.name)
        self.assertEqual(2, enum.value)

    def test_coffee(self):
        enum = ServiceType.COFFEE
        self.assertEqual('COFFEE', enum.name)
        self.assertEqual(3, enum.value)

    def test_events(self):
        enum = ServiceType.EVENTS
        self.assertEqual('EVENTS', enum.name)
        self.assertEqual(4, enum.value)


if __name__ == '__main__':
    unittest.main()
