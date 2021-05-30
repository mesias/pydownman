import multiprocessing as mp
from multiprocessing import Queue


def start_process(dw_manager):
    print('Starting the download main loop')
    dw_manager.start_loop()


class DownloadManager:
    def __init__(self, url_queue=Queue(), info_queue=Queue(1)):
        self.url_queue = url_queue
        self.info_queue = info_queue
        self.downloads = []
        self.process = None

    def start(self):
        print('Starting the download manager process')
        self.process = mp.Process(target=start_process, args=(self,))
        self.process.start()

    def start_loop(self):
        while True:
            url = self.url_queue.get()
            if url is None:
                break
            print(f'New Download: {url}')
