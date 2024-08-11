import re
from typing import Literal

from mutagen.mp4 import MP4, MP4Cover

from unigen.types.audio_metadata import MediaInfo
from unigen.types.picture import Picture
from unigen.wrapper.audio_manager import IAudioManager, non_custom_tags
from unigen.wrapper.utils import (
    cleanDate,
    convertStringToNumber,
    extractYearFromDate,
    getFirstElement,
    toList,
)


class MP4Wrapper(IAudioManager):
    def __init__(self, file_path: str, extension: Literal[".m4a"]):
        extension_handlers = {".m4a": MP4}
        self.extension = extension.lower()
        self.audio = extension_handlers[extension](file_path)
        self.file_path = file_path

    def getFilePath(self):
        return self.file_path

    def setTitle(self, newTitle):
        self.audio["\xa9nam"] = newTitle

    def setAlbum(self, newAlbum):
        self.audio["\xa9alb"] = newAlbum

    def setDiscNumbers(self, discNumber, totalDiscs):
        self.audio["disk"] = [(discNumber, totalDiscs)]

    def setTrackNumbers(self, trackNumber, totalTracks):
        self.audio["trkn"] = [(trackNumber, totalTracks)]

    def setComment(self, comment):
        self.audio["\xa9cmt"] = comment

    # There is no way to set cover of a certain type here :( We can put multiple covers but it becomes messy without identifiers for cover type
    def setPictureOfType(self, imageData, pictureType):
        cover = MP4Cover(imageData, imageformat=MP4Cover.FORMAT_JPEG)
        self.audio["covr"] = [cover]

    def hasPictureOfType(self, pictureType):
        return "covr" in self.audio and self.audio["covr"][0].imageformat == MP4Cover.FORMAT_JPEG

    def deletePictureOfType(self, pictureType):
        if "covr" in self.audio:
            del self.audio["covr"]
            return True
        return False

    def setDate(self, date):
        self.audio["\xa9day"] = [cleanDate(date)]
        self.audio["\xa9year"] = [extractYearFromDate(date)]

    def setCustomTag(self, key, value):
        newKey = f"----:com.apple.iTunes:{key}"
        value = [v.encode("utf-8") for v in value]
        self.audio[newKey] = value

    def setCatalog(self, value):
        self.setCustomTag("CATALOGNUMBER", value)
        self.setCustomTag("CATALOG", value)

    def setBarcode(self, value):
        self.setCustomTag("barcode", value)

    def setDiscName(self, value):
        self.setCustomTag("DISCSUBTITLE", value)

    def getTitle(self):
        return toList(self.audio.get("\xa9nam"))

    def getAlbum(self):
        return toList(self.audio.get("\xa9alb"))

    def getArtist(self):
        return toList(self.audio.get("\xa9ART"))

    def getAlbumArtist(self):
        return toList(self.audio.get("aART"))

    def getDiscNumber(self):
        disk = getFirstElement(self.audio.get("disk"))
        return convertStringToNumber(disk[0]) if disk else None

    def getTotalDiscs(self):
        disk = getFirstElement(self.audio.get("disk"))
        return convertStringToNumber(disk[1]) if disk else None

    def getTrackNumber(self):
        trkn = getFirstElement(self.audio.get("trkn"))
        return convertStringToNumber(trkn[0]) if trkn else None

    def getTotalTracks(self):
        trkn = getFirstElement(self.audio.get("trkn"))
        return convertStringToNumber(trkn[1]) if trkn else None

    def getComment(self):
        return toList(self.audio.get("\xa9cmt"))

    def getDate(self):
        date = self.audio.get("\xa9day")
        return cleanDate(date[0]) if date else None

    def getCustomTag(self, key):
        newKey = f"----:com.apple.iTunes:{key}"
        value = self.audio.get(newKey, None)
        if not value:
            return []
        value = [v.decode("utf-8") for v in value]
        return value

    def getAllCustomTags(self):
        custom_tags: dict[str, list[str]] = {}
        pattern = r"----:com\.apple\.iTunes:(.*)"
        for key, value in self.audio.items():
            match = re.search(pattern, key)
            if match:
                tag_key = match.group(1)
                if tag_key.lower() not in non_custom_tags:
                    tag_value = [v.decode("utf-8") for v in toList(value)]
                    custom_tags[tag_key] = tag_value

        return custom_tags

    def getCatalog(self):
        return self._searchMultiCustomTags(["CATALOGNUMBER", "CATALOG", "LABELNO"])

    def getBarcode(self):
        return self._searchMultiCustomTags(["barcode", "BARCODE"])

    def getDiscName(self):
        return self._searchMultiCustomTags(["DISCSUBTITLE", "DISCNAME"])

    def getAllPictures(self):
        pictures: list[Picture] = []
        if "covr" in self.audio and self.audio["covr"][0].imageformat == MP4Cover.FORMAT_JPEG:
            pictures.append(Picture(picture_type=3, data=bytes(self.audio["covr"][0])))
        return pictures

    def getMediaInfo(self) -> MediaInfo:
        info = self.audio.info
        return MediaInfo(
            sample_rate=info.sample_rate if hasattr(info, "sample_rate") else None,
            channels=info.channels if hasattr(info, "channels") else None,
            bits_per_sample=info.bits_per_sample if hasattr(info, "bits_per_sample") else None,
            bitrate=info.bitrate if hasattr(info, "bitrate") else None,
            codec=info.codec if hasattr(info, "codec") else None,
        )

    def printInfo(self):
        return self.audio.pprint()

    def save(self):
        self.audio.save()

    def clearTags(self):
        self.audio.delete()

    def _searchMultiCustomTags(self, possibleFields: list[str]) -> list[str]:
        for field in possibleFields:
            ans = self.getCustomTag(field)
            if ans:
                return ans
        return []
