import time
import urllib.request
from multiprocessing import Queue
from threading import Thread
import urllib
import re

q = Queue(0) #  it looks like concurent object, no locking is necessary, but I might be wrong, instantiated with 0 wich means infinity


class ProducerThread(Thread):
    # it is automaticaly called when method start is called on instance of this class
    def run(self):
        uris = []
        try:
            file = open('newfile.txt', 'r')
            uris = file.readlines()
        except Exception as ex:  #  I dont know how to determine what kind of exception may happen, 1st link in file is intentionally wrong
            print("something went wrong with the file")
            #  dont know how to terminate the process/thread here
            pass

        self.in_parallel(self.enqueue, uris)  # it will start as many processes as many the links in the list, which is not ok by my opinion, there should be predefined amount of possible threads

    # I don't know ho to make this method kind of private for better encapsulation
    def in_parallel(self, fn, l):
        for i in l:
            Thread(target=fn, args=(i,)).start()

    def enqueue(self, url):
        try:
            link = self.process(url)
            global q  # don't know what this is for?
            q.put(link)
            print('produced')
        except Exception as ex:  # don't know how to work with exceptions properly in python
            print('invalid link or something else happened')
            pass

    def process(self, url):
        req = urllib.request.Request(url)  # it looks like when the link would not be parsed because of the format of an hypelink, then error is thrown
        with urllib.request.urlopen(req) as response:

            '''if response.status_code == 200:
                print('OK')'''  # does not work, don't know why, I would treat issues based on status codes otherwise
            the_page = response.read() #  it returns object, I don't know how to select only markup from that object in python
            return the_page


class ConsumerThread(Thread):
    # it is automaticaly called when method start is called on instance of this class
    def run(self):
        self.dequeue()

    def dequeue(self):
        global q
        while True:
            time.sleep(2)  # just to prove is asynchronous, you can remove it
            the_page = q.get()
            links = self.processlinks(the_page)
            print(links)
            print('consumed')

    def processlinks(self, page):
        a = page.decode(encoding='UTF-8')  # don't know how to extract only markup from that object
        # q.task_done() only exist in different version of the library
        links = re.findall('"((http|ftp)s?://.*?)"', a)  # it searches for hyperlinks
        return links



ProducerThread().start()
ConsumerThread().start()
