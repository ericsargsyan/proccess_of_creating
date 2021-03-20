from youtubesearchpython import VideosSearch

videosSearch = VideosSearch('iriknajam', limit = 1)

print(videosSearch.result())


print(videosSearch['result'])


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

from youtube_search import YoutubeSearch


results = YoutubeSearch('iriknajam', max_results=2).to_dict()
print(results)
urls = []
image_urls = []

# extract video url and image url

for line in results:
	urls.append(line['url_suffix'])
	image_urls.append(line['thumbnails'][0])




# print(urls)
# print(image_urls)

embedded_urls = []

# embed urls for <iframe>

for url_to_be_embedded in urls:
	embedded_urls.append("https://www.youtube.com" + url_to_be_embedded.replace("watch?v=", "embed/").split("&")[0])

# print(embedded_urls)

context = {
	'embedded_urls': embedded_urls,
	'image_urls': image_urls
}

for i in results:
	print(i['thumbnails'][0])

for i in context['embedded_urls']:
	context['image_urls'][0].strip("\'")

print(context['embedded_urls'][0].strip("\'"))


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


import youtube_dl
from youtube_search import YoutubeSearch
ydl_opts = {a
	"format" : "bestaudio/best",
	'outtmpl': 
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    meta = ydl.extract_info(
        'https://www.youtube.com/watch?v=9bZkp7q19f0', download=True) 

ydl_opts = {
		'format': 'bestaudio/best',
		'postprocessors': [{
			'key': 'FFmpegExtractAudio',
			'preferredcodec': 'mp3',
			'preferredquality': '192',
		}],
	}
	
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		ydl.download(['https://www.youtube.com/watch?v=Gfz2Xe3hGbs&list=RDEMxoLg15gGb7rZWyyuKi3lmA'])




ydl = youtube_dl.YoutubeDL()
with ydl:
    # r = ydl.extract_info("https://www.youtube.com/watch?v=Re_f1UOWyNg&list=RDMM", download=False)  # don't download, much faster
    r = ydl.extract_info("https://www.youtube.com/watch?v=NlwIDxCjL-8", download=False)
# print(r['title'], '\n', r['thumbnail'])
print(r)

ydl_opts ={}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
	result = ydl.extract_info("https://www.youtube.com/watch?v=aaSPmEEzExk", download=False)

print(result)


commafy = lambda num: f"{num:,}"

ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
	meta = ydl.extract_info(f"https://www.youtube.com/watch?v={id}", download=False)

views = commafy(meta['view_count'])
likes = commafy(meta['like_count'])
dislikes = commafy(meta['dislike_count'])
duration = time_(meta['duration'])

info = {'views': views,
		'likes': likes,
		'dislikes': dislikes,
		'duration': duration,
		'title': meta['title'],
		'id': id
		}


urls = []
image_urls = []

for line in results:
	urls.append(line['url_suffix'])
	image_urls.append(line['thumbnails'][0].strip("\'"))

print(info)		



url = "https://www.youtube.com/watch?v=GVbAY0YDVNo" 

results = YoutubeSearch('https://www.youtube.com/watch?v=f-GMYDoTfI0&list=RDf-GMYDoTfI0', max_results=22).to_dict()
print(results)


urls = []
image_urls = []

# extract video url and image url

for line in results:
	urls.append(line['url_suffix'])
	image_urls.append(line['thumbnails'][0].strip("\'"))

"https://www.youtube.com/watch?v=pz7GQ_cENuA&list=RDf-GMYDoTfI0&index=2"
"https://www.youtube.com/watch?v=J5QT4-zqAsM&list=RDf-GMYDoTfI0&index=3"


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


import googleapiclient.discovery

playlist_id = "RDGMEM6ijAnFTG9nX1G-kbWBUCJA"

youtube = googleapiclient.discovery.build("youtube", "v3", developerKey = "AIzaSyCurwIFtb9Mv0VRgWVaNlpQZ_PwwJ326XY")

request = youtube.playlistItems().list(
    part = "snippet",
    playlistId = playlist_id,
    maxResults = 2
)
response = request.execute()

playlist_items = []
while request is not None:
    response = request.execute()
    playlist_items += response["items"]
    request = youtube.playlistItems().list_next(request, response)

print(f"total: {len(playlist_items)}")
print(playlist_items)


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# import gdata.youtube
# import gdata.youtube.service


Dependencies:
- Python==2.7
- gdata==2.0.18
- google-api-python-client==1.2


yt_service = gdata.youtube.service.YouTubeService()
yt_service.ssl = True


# Can be left blank and be set on input
playlist_uri = "http://gdata.youtube.com/feeds/api/playlists/F835FEAB20A328D9"

if playlist_uri == "":
    playlist_uri = str(input("Playlist URI: "))


playlist_songs = []
playlist_video_feed = yt_service.GetYouTubePlaylistVideoFeed(playlist_uri)
for playlist_video_entry in playlist_video_feed.entry:
    playlist_songs.append(playlist_video_entry.title.text)


f = open("playlist.txt", "w")
for entry in playlist_songs:
    f.write(entry + "\n");
f.close()


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$







from youtube_search import YoutubeSearch
from pytube import Playlist
import youtube_dl

results = YoutubeSearch("https://www.youtube.com/watch?v=snsCnP1JhDY&list=RDGMEMQ1dJ7wXfLlqCjwV0xfSNbAVMsnsCnP1JhDY", max_results=50).to_dict()

# print(results)


# playlist = Playlist('https://www.youtube.com/watch?v=58PpYacL-VQ&list=UUd6MoB9NC6uYN2grvUNT-Zg')
# print('Number of videos in playlist: %s' % len(playlist.video_urls))
# playlist.download_all()


ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
	meta = ydl.extract_info("https://www.youtube.com/watch?v=wTgWX_62paE&list=RDGMEMQ1dJ7wXfLlqCjwV0xfSNbAVMsnsCnP1JhDY", download=False)

print(meta)
info = {'title': meta['title']}

print(info)

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


from concurrent.futures import ThreadPoolExecutor
import youtube_dl
import datetime
import threading

url = "https://www.youtube.com/watch?v=gj0Rz-uP4Mk&list=PLDoNWpWHi2nIZ4qPu-GLuuK_3yms09OSz"

def extract_from_playlist(results, item):
	result = []
	for dict_ in results["entries"]:
		for key, value in dict_.items():
			if key == item:
				result.append(value)
	return result


def function(url):
	ydl_opts = {'ignoreerrors': True}
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		results = ydl.extract_info(url, download=False)
		webpage_urls = extract_from_playlist(results, "webpage_url")

starting_time = datetime.datetime.now() # .strftime('%m/%d/%Y, %H:%M:%S')
print(f"Starting Time: {starting_time.strftime('%m/%d/%Y, %H:%M:%S')}")

# with ThreadPoolExecutor(max_workers=222) as executor:
# 	executor.map(function, [url])

threading_list = []

x = threading.Thread(target=function, args=(url,))
x.start()
# function(url)

print(f"Code Execution Time: {(datetime.datetime.today() - starting_time).seconds}")

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


import youtube_dl

def extract_from_playlist(results, item):
	result = []
	for dict_ in results["entries"]:
		for key, value in dict_.items():
			if key == item:
				result.append(value)
	return result


url = "https://www.youtube.com/watch?v=TUVcZfQe-Kw&list=PLNrotoZZ8BaoXT_LJuwEyESQlctWNDCwD"
ydl_opts = {'ignoreerrors': True}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
	results = ydl.extract_info(url, download=False)
	playlist = extract_from_playlist(results, "playlist")
	ydl.download([url])

print(results["entries"][0]["playlist"])


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


from pytube import Playlist, YouTube 


url = 'https://www.youtube.com/watch?v=GfO-3Oir-qM&list=PLvahqwMqN4M0GRkZY8WkLZMb6Z-W7qbLA'

playlist = Playlist(url)


# print(playlist)


print(playlist.title)

print(playlist)
print("respond")
print(playlist)
youtube = pytube.YouTube(url)

print(youtube)
for video in playlist:
	print("For")
	youtube = pytube.YouTube(video)
	print(type(youtube))
	# video.download('/test') 


from youtube_search import YoutubeSearch

url = "Shape of my Heart"

results = YoutubeSearch(url, max_results=25).to_dict()

print(results)
