'''
    Simple M4A to MP3 convertion
'''
import os
from pydub import AudioSegment
from pydub.utils import mediainfo

# function to handle song convertion and saving
def convert_to_mp3(song_path, destination_dir):
    '''
        Receives the song path and converts the song to MP3 format
    '''
    song = AudioSegment.from_file(song_path) # returns an object
    tags = mediainfo(song_path).get('TAG', None) # dict of tags

    for k in tags:
        tags[k] = tags[k].encode('utf8')
    title = tags['title'] + ".mp3"

    song.export("{0}/{1}".format(destination_dir, title),\
                format="mp3",\
                tags=tags,\
                bitrate="320k")

print "------------------------------"
print "--Convertion Started started--"
print "------------------------------"

destination_dir = str(raw_input('Enter Folder Name:'))
if not os.path.exists(destination_dir):
        os.mkdir(destination_dir)

for cdir, subdirs, files in os.walk('.'):
    for f in files:
        if f.lower().endswith('m4a'):
            convert_to_mp3(f, destination_dir)
            print f, "converted\n"

print "-----------------------------"
print "------Convertion ended.------"
print "-----------------------------"
