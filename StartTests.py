import unittest
from start import ProducerThread
from start import ConsumerThread

if __name__ == '__main__':
    unittest.main()

#  dont know how create a test suite and i dont know why the main application is executed with tests
class MyTest(unittest.TestCase):
    def setUp(self):
        self.pt = ProducerThread()
        self.ct = ConsumerThread()

    def MarkupLengthHigherThanZero(self):
        markup = self.pt.process('http://www.eset.sk')
        self.assertGreater(len(markup.decode(encoding='UTF-8')), 0, "not markup returned")

    def Test(self):
        markup = self.pt.process('http://www.eset.sk')
        links = self.ct.processlinks(markup)
        self.assertEqual(links[0], 'http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd', "no links found")
'''
    def tearDown(self):
        self.pt.dispose()
        self.pt = None

        self.ct.dispose()
        self.pt = None
'''

