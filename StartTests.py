import unittest
from start import ProducerThread

if __name__ == '__main__':
    unittest.main()

class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self._pokus = ProducerThread.process2('The widget')

    def tearDown(self):
        self._pokus.dispose()
        self._pokus = None

    def test_process(self):
        self.assertEqual(self, self._pokus, 'The widget', 'aaa')
