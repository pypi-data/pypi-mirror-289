import os
import pathlib
import random
import logging as log

from magic_lantern.photo import createPhoto, getPhoto, Photo
from magic_lantern import config
from magic_lantern.config import Order
from magic_lantern import pdf


class Album:
    def __init__(self, order: Order, path: pathlib.Path, weight: int, interval: int):
        self._order = order
        self._path = path

        if weight:
            self.weight = weight
        else:
            self.weight = config.weight
        if interval:
            self.interval = interval
        else:
            self.interval = config.interval

        self._photoFileList = []
        self._photoIndex = 0
        self._photoCount = 0
        # Walk through the source directory and its subdirectories
        for root, dirs, files in os.walk(path):
            dirs[:] = [d for d in dirs if d not in config.exclude]
            log.info(f"In {root}")
            for f in files:
                if f.lower().endswith(".pdf"):
                    log.info(f"{f}  PDF file")
                    for pdfPageImageFile in pdf.convert(root, f):
                        createPhoto(pdfPageImageFile, self.interval)
                        self._photoFileList.append(pdfPageImageFile)
                    continue

                # Filter out files with unknown extensions
                if f.lower().endswith((".png", ".jpg", ".jpeg")):
                    imageFile = os.path.join(root, f)
                    createPhoto(imageFile, self.interval)
                    self._photoFileList.append(imageFile)
                    continue

                log.warning(f"{f}  Unknown file type")

        # Shuffle or sort the list of photos
        if self._order == Order.RANDOM:
            random.shuffle(self._photoFileList)
        # else:
        #     self._photoFileList.sort()

        # Update the photo count
        self._photoCount = len(self._photoFileList)

    def getNextPhoto(self):
        if self._photoIndex >= self._photoCount:
            self._photoIndex = 0
            if self._order == Order.ATOMIC:
                return None  # We've reached the end; signal caller
        photo = getPhoto(self._photoFileList[self._photoIndex])
        self._photoIndex += 1
        return photo
