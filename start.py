import time
import urllib.request
from multiprocessing import Queue
from threading import Thread
#from urllib.parse import urljoin
import urllib
#import lxml.html
import re

pages = ['http://www.pc.sk', 'http://www.sme.sk'] #zbytocne lebo idem so suboru
q = Queue(0)
pool = multiprocessing.Pool(processes=4)


class ProducerThread(Thread):
    def run(self):
        file = open('newfile.txt', 'r')
        uris = file.readlines()
        for url in uris:
            try:
                req = urllib.request.Request(url)
                with urllib.request.urlopen(req) as response:
                    the_page = response.read()
                    global q
                q.put(the_page)
                print('produced')
                process(req.full_url)
            except Exception as ex:
                pass

            #pool.map(process_url, list_of_urls)

def process():
    print(str)

def process2(str):
    return str+1

class ConsumerThread(Thread):
    def run(self):
        dequeueAndProcess()

def dequeueAndProcess():
    global q
    while True:
        time.sleep(2) #just to prove is asynchronous
        the_page = q.get()
        a = the_page.decode(encoding='UTF-8') # don't know how to extract only markup from that object
        # q.task_done() only in diferent version of the library
        links = re.findall('"((http|ftp)s?://.*?)"', a)
        print(links)
        print('consumed')


ProducerThread().start()
ConsumerThread().start()

class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = ProducerThread()
        self.widget.pr

    def tearDown(self):
        self.widget.dispose()
        self.widget = None

    def test_default_size(self):
        self.assertEqual(self.widget.size(), (50,50), 'incorrect default size')

    def test_resize(self):
        self.widget.resize(100,150)
        self.assertEqual(self.widget.size(), (100,150), 'wrong size after resize')
