from youtube_search import YoutubeSearch
import datetime
url = input("Enter Name: ")

results = YoutubeSearch(url, max_results=1).to_dict()

print(results)

commafy = lambda num: f"{num:,}"


print(commafy(123456789222))


def time_(seconds):
	duration = str(datetime.timedelta(seconds=seconds))
	if not duration.startswith("0"):
		return duration
	return duration[2:]


def time_(seconds):
	duration = str(datetime).timedelta(seconds=seconds)
	if not duration.startswith("0"):
		return duration

	temp = duration.split(":")
	minutes = f"{temp[1]}:{temp[2]}"
	return minutes

print(time_(226))	

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


import os
import youtube_dl


with youtube_dl.YoutubeDL(ydl_opts) as ydl:
	meta = ydl.extract_info(url, download=True)
	formats = meta.get('formats', [meta])

get_formats = [f['format'].split(" ")[3][1:-1] for f in formats if f['format'][0] == "1"][1:]

resolutions = list(dict.fromkeys(get_formats))

for f in formats:
	fmts = []
	if f['format'] == "1":
		fmts.append(f['format'].split(" ")[0])



youtube_dl.utils.DownloadError



print(resolutions)

options = {
	"format" : get_formats[-1],
}

with youtube_dl.YoutubeDL(options) as ydl:
	ydl.download([url])


# print(get_formats)

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

audio_folder = "songs"
ydl_opts = {
	'format': 'bestaudio/best',
	'postprocessors': [{
		'key': 'FFmpegExtractAudio',
		'preferredcodec': 'mp3',
		'preferredquality': '360',
	}],
}
# URLS.objects.create(user=request.user, url=f'http://www.youtube.com/watch?v={pk}')


with youtube_dl.YoutubeDL(ydl_opts) as ydl:
	ydl.download(['https://www.youtube.com/watch?v=dVvlmpo5g9k'], download=False)


with youtube_dl.YoutubeDL(ydl_opts) as ydl:
	meta = ydl.extract_info("https://www.youtube.com/watch?v=dVvlmpo5g9k&list=RDdVvlmpo5g9k", download=False)


# info = {'views': meta['view_count'],
# 			'likes': meta['like_count'],
# 			'dislikes': meta['dislike_count'],
# 			'duration': meta['duration'],
# 			'title': meta['title'],
			# }
print(meta)



# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$




audio_folder = "songs"

ydl_opts = {
	'postprocessors': [{
		'key': 'FFmpegExtractAudio',
		'preferredcodec': 'mp4',
		'preferredquality': '192',
	}],
}


if not os.path.exists(audio_folder):
	os.mkdir(audio_folder)
os.chdir(audio_folder)

ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
	ydl.download(["https://www.youtube.com/watch?v=Gfz2Xe3hGbs&list=RDEMxoLg15gGb7rZWyyuKi3lmA"])
	results = ydl.extract_info(url, download=False)

for dict_ in results["entries"]:
	for key, value in dict_.items():
		if key == "playlist":
			print(value)
url = "https://www.youtube.com/watch?v=56reWK8S7RY&list=PL7S2hDr47XdUpt-NN2zFjRymmy9iACGFi"	
from pytube import Playlist

playlist = Playlist(url)

print(playlist)
# Loop through all videos in the playlist and download them
for video in playlist.videos:
    video.streams.first().download()

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

import pytube
from pytube import YouTube, Playlist
pl = Playlist("https://www.youtube.com/watch?v=SlPhMPnQ58k&list=PL4o29bINVT4EG_y-k5jGoOu3-Am8Nvi10")
pl.populate_video_urls()  # fills the pl.video_urls with all links from the playlist
urls = pl.video_urls

for url in urls:
	vid_title = YouTube(url).title  # here's what you want
	print(vid_title)   



from pytube import Playlist


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

import threading
import datetime


starting_time = datetime.datetime.now()
print(f"Starting Time: {starting_time.strftime('%m/%d/%Y, %H:%M:%S')}")


threading_list = []

x = threading.Thread(target=download_images, args=("images.json",))
x.start()

play_list = Playlist("https://www.youtube.com/playlist?list=PL4o29bINVT4EG_y-k5jGoOu3-Am8Nvi10")
print(len(play_list))

# for link in play_list:
#     print(link)

name = []

for video in play_list.videos:
    name.append(video.title)
    print(name)


titles = []
for video in play_list.videos:
	titles.append(video.title)

print(title)


def embed_urls(urls):
	embedded_urls = []
	for url_to_be_embedded in urls:
		embedded_urls.append(url_to_be_embedded.replace("watch?v=", "embed/").split("&")[0])
	return embedded_urls


urls_to_send = []

for url_to_be_embedded in urls_history:
	urls_to_send.append(str(url_to_be_embedded))
# with ThreadPoolExecutor(max_workers=222) as executor:
# 	executor.map(function, [url])

embedded_urls = embed_urls(urls_to_send)

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

from pytube import Playlist

def embed_urls(urls):
	embedded_urls = []
	for url_to_be_embedded in urls:
		embedded_urls.append(url_to_be_embedded.replace("watch?v=", "embed/").split("&")[0])
	return embedded_urls

playlist = Playlist("https://www.youtube.com/watch?v=8ejF8Qv6VZk&list=PLRfY4Rc-GWzhdCvSPR7aTV0PJjjiSAGMs")
embedded_urls = embed_urls(playlist)
database = embedded_urls[0]
# titles = []
# for video in playlist.videos:
# 	titles.append(video.title)
# Playlists.objects.create(user=request.user, playlist_url=url)
context = {
	"embedded_urls": embedded_urls
	# "titles": titles
}

print(context)

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

from youtube_search import YoutubeSearch

url = "https://www.youtube.com/watch?v=e-NDXtDUcGQ&list=PLOsKeK_3mXlgEeiFTOJOArqKIr7SX44xO"
results = YoutubeSearch(url, max_results=1).to_dict()
print(results)

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

from youtubesearchpython import *

playlist = Playlist.get('https://www.youtube.com/playlist?list=PLRBp0Fe2GpgmsW46rJyudVFlY6IYjFBIK', mode = ResultMode.json)
print(playlist)
playlistInfo = Playlist.getInfo('https://www.youtube.com/playlist?list=PLRBp0Fe2GpgmsW46rJyudVFlY6IYjFBIK', mode = ResultMode.json)
print(playlistInfo)
playlistVideos = Playlist.getVideos('https://www.youtube.com/playlist?list=PLRBp0Fe2GpgmsW46rJyudVFlY6IYjFBIK')
print(playlistVideos)


# https://www.youtube.com/embed/8ejF8Qv6VZk
# https://www.youtube.com/embed/gppHFr0_lDk
# https://www.youtube.com/embed/8ejF8Qv6VZk

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

from pytube import Playlist

import os

url = "https://www.youtube.com/watch?v=TUVcZfQe-Kw&list=PLNrotoZZ8BaoXT_LJuwEyESQlctWNDCwD"
playlist = Playlist("https://www.youtube.com/watch?v=TUVcZfQe-Kw&list=PLNrotoZZ8BaoXT_LJuwEyESQlctWNDCwD")
os.chdir("test")
# playlist.download_all()
# print(playlist.title)
print(playlist.title)
for video in playlist:
	video.download()

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

from pytube import Playlist
os.chdir("test")
playlist = Playlist('https://www.youtube.com/playlist?list=PL6gx4Cwl9DGCkg2uj3PxUWhMDuTw3VKjM')
print('Number of videos in playlist: %s' % len(playlist.video_urls))
for video_url in playlist.video_urls:
    print(video_url)
playlist.download_all()

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

import youtube_dl

ydl_opts = {}
os.chdir("test")
url = "https://www.youtube.com/watch?v=TUVcZfQe-Kw&list=PLNrotoZZ8BaoXT_LJuwEyESQlctWNDCwD"

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
	meta = ydl.extract_info(url, download=True)
	ydl.download(url)

print(meta)

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

from pytube import Playlist


url = 'https://www.youtube.com/watch?v=GfO-3Oir-qM&list=PLvahqwMqN4M0GRkZY8WkLZMb6Z-W7qbLA'

playlist = Playlist(url)


# print(playlist)

print(type(playlist))

 
for video in playlist.videos:
    video.streams.first().download('/test')

print(playlist.title)
