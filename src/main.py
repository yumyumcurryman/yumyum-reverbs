import eyed3
import os

directory = '/Users/yumyumcurryman/Documents/Personal/Music/yumyum-reverbs-'

def getNameAndArtist(filename):
    filename = filename[0:-4]
    return filename.split(' - ')

def setSongData(data, filename):
    audiofile = eyed3.load(os.path.join(directory, filename))
    if audiofile.tag.title != data[0]:
        print("Processing ", data)
        audiofile.tag.title = data[0]
        audiofile.tag.artist = data[1]
        audiofile.tag.images.set(3, open('cover.jpg', 'rb').read(), 'image/jpeg')
        audiofile.tag.album = "YumYum Reverbs™"
        audiofile.tag.save()


for filename in os.listdir(directory):
    if filename.endswith(".mp3"):
        songData = getNameAndArtist(filename)
        if len(songData) > 1:
            setSongData(getNameAndArtist(filename), filename)

