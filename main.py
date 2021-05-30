from gui import dw_gui
from download_manager.dw_manager import DownloadManager

dwmanager = DownloadManager()


def main():
    global dwmanager
    dwmanager.start()
    dw_gui.vp_start_gui()


if __name__ == '__main__':
    main()
