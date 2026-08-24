#!/usr/bin/python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import shutil
import sys
import urllib.request

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""


def read_urls(filename, puzzle):
    """Returns a list of the puzzle urls from the given log file,
    extracting the hostname from the filename itself.
    Screens out duplicate urls and returns the urls sorted into
    increasing order."""
    # +++your code here+++
    if puzzle == "animal":
        with open(filename) as f:
            result = []
            for line in f:
                match = re.search(r'/edu/languages/google-python-class/images/puzzle/a-\w\w\w\w\.jpg', line)
                if match:
                    result.append("https://code.google.com" + match.group())
        return sorted(list(set(result)))
    else:
        with open(filename) as f:
            result = {}
            for line in f:
                match = re.search(r'/edu/languages/google-python-class/images/puzzle/p-\w\w\w\w-(\w\w\w\w)\.jpg', line)
                if match:
                    print("match found")
                    result[match.group(1)] = "https://code.google.com" + match.group()
            sorted_result = dict(sorted(result.items()))
            print(sorted_result)
        return list(sorted_result.values())


def download_images(img_urls, dest_dir):
    """Given the urls already in the correct order, downloads
    each image into the given directory.
    Gives the images local filenames img0, img1, and so on.
    Creates an index.html in the directory
    with an img tag to show each local image file.
    Creates the directory if necessary.
    """
    # +++your code here+++
    # delete old folder and make a new one
    if os.path.exists(dest_dir):
        print(dest_dir)
        print("Removing existing output directory...")
        shutil.rmtree(dest_dir)
    if not os.path.exists(dest_dir):
        print(dest_dir)
        print("Creating output directory...")
        os.mkdir(dest_dir)

    # download all the images and create html file
    with open("index.html", "w") as f:
        f.write("<html>\n<body>\n")
        count = 1
        for url in img_urls:
            urllib.request.urlretrieve(url, f"./animal_images/animal_img_{count}.jpg")
            f.write(f'<img src="./animal_images/animal_img_{count}.jpg">')
            count += 1
        f.write("</body>\n</html>")


def main():
    download_images(read_urls("place_code.google.com", "place"), "./animal_images")

if __name__ == '__main__':
    main()
