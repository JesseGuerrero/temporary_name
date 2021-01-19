import vlc
import pafy
from youtubesearchpython import VideosSearch
import random

'''
~~Code resources~~
Youtube URL generation library docs
https://pypi.org/project/youtube-search-python/

Playing Youtube videos usin VLC
https://stackoverflow.com/questions/49354232/how-to-stream-audio-from-a-youtube-url-in-python-without-download
https://stackoverflow.com/questions/56611337/python-vlc-doesnt-plays-and-response-with-the-youtube-video-link
'''

def generateURLYouTubeSearch(searchQuery):
    search = VideosSearch(searchQuery + ' music', limit=20)
    searchIndex = random.randint(0, 19)
    url = search.result()['result'][searchIndex]['link']
    return url

'''
requires libvlc
'''
def playYouTubeAudio(url, player):
    video = pafy.new(url)
    best = video.getbest()
    playurl = best.url

    #To play with video remove no-video
    Media = ins.media_new(playurl, ":no-video")
    Media.get_mrl()
    player.set_media(Media)
    player.play()


#Only runs when you run this file.
if __name__ == '__main__':
    url = generateURLYouTubeSearch(input("insert a search: "))

    ins = vlc.Instance()
    mediaPlayer = ins.media_player_new()
    playYouTubeAudio(url, mediaPlayer)

    command = ''
    while(command != 'yes'):
        command = input("Stop Playing: ")
    mediaPlayer.stop()