import pygame
import exifread


from magic_lantern import screen

_photoCache: dict = {}


def createPhoto(path: str, interval: int):
    if path not in _photoCache:
        photo = Photo(path, interval)
        _photoCache[path] = photo
    return _photoCache[path]


def getPhoto(path: str):
    return _photoCache[path]


class PhotoException(Exception):
    def __init__(self, filename):
        self.filename = filename


class Photo:
    def __init__(self, filename, interval) -> None:
        self.filename = filename
        self.x = 0
        self.y = 0
        self.interval = interval
        self.imageLoaded = False

    def loadImage(self):
        # Load the image
        try:
            image = pygame.image.load(self.filename)
        except:
            raise PhotoException(self.filename)

        # Get the boundary rectangle
        imageRect = pygame.Rect((0, 0), image.get_size())

        # Fit the rectangle to the screen
        imageFit = imageRect.fit(screen.rect())

        self.x = imageFit.x
        self.y = imageFit.y

        # Scale the image to the rectangle
        scaledImage = pygame.transform.smoothscale(
            image.convert(), imageFit.size
        )  # call convert to upscale any 8-bit images

        self.surface = scaledImage.convert()

        with open(self.filename, "rb") as file_handle:
            # Return Exif tags
            tags = exifread.process_file(file_handle)

        if "EXIF DateTimeOriginal" in tags:
            self.datetime = tags["EXIF DateTimeOriginal"]
        else:
            self.datetime = ""
        self.imageLoaded = True

    def coordinates(self):
        if not self.imageLoaded:
            self.loadImage()
        return (self.x, self.y)

    def getSurface(self):
        if not self.imageLoaded:
            self.loadImage()
        return self.surface
