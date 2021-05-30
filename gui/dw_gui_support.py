#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 6.0.1
#  in conjunction with Tcl version 8.6
#    May 27, 2021 04:13:44 PM -03  platform: Linux

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

def set_Tk_var():
    global chkEnterVar
    chkEnterVar = tk.IntVar()


# see: https://stackoverflow.com/a/14824164/926055
def retrieve_url_input():
    return w.txtUrlText.get(1.0, tk.END)


# see: https://stackoverflow.com/a/40425788/926055
def clear_url_input():
    w.txtUrlText.delete(1.0, tk.END)


def init(top, gui, *args, **kwargs):
    global w, top_level, root, dwmgr
    from main import dwmanager
    w = gui
    top_level = top
    root = top
    dwmgr = dwmanager

    # bindings see: https://stackoverflow.com/a/3513906/926055
    w.txtUrlText.bind("<KeyRelease>", binded_txt_keypress)


def binded_txt_keypress(event):
    txt_url = retrieve_url_input()
    if txt_url:
        w.btnDownload.configure(state='enabled')  # enable download button
        if event.keysym in ('KP_Enter', 'Return') and chkEnterVar.get():
            # pressed enter with check Enter enabled, then submit
            print(f'Entered url: {txt_url} key: {event.keysym}')
            enter_url(txt_url)
        else:
            # check if all urls are valid
            if validate_urls(txt_url):
                w.txtUrlText.configure(fg="black")
            else:
                w.txtUrlText.configure(fg="red")

    else:
        w.btnDownload.configure(state='disabled')  # disable download button


def validate_urls(url):
    """
    Return the url list if all are valid

    :param url: URL's separated by NEWLINE
    :return: url list
    """
    if '\n' in url:
        url_list = url.split()
    else:
        url_list = [url, ]

    for url in url_list:
        if not is_valid_url(url):
            print(f'Not Valid url: {url}')
            return []
    return url_list


def enter_url(url):
    valid_urls = validate_urls(url)
    print(f'New Url Added: {valid_urls}')
    sys.stdout.flush()
    if valid_urls:  # if the list is valid
        for url in valid_urls:
            print(f'Sending url to manager: {url}')
            dwmgr.url_queue.put(url)  # send url to manager thru queue
        clear_url_input()  # clears the list !


def cmdAddUrl():
    txt_url = retrieve_url_input()
    if txt_url:
        enter_url(txt_url)


# see: https://stackoverflow.com/a/7995979/926055
def is_valid_url(url):
    import re
    regex = re.compile(
        r'^https?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return url is not None and regex.search(url)


def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import dw_gui
    dw_gui.vp_start_gui()



