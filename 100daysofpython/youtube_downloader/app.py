from pytube import YouTube, Playlist, exceptions
import os

if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

print("%"*95)
print("\t"*4, "PYTHON YOUTUBE DOWNLOADER")
print("%"*95, "\n")


url = input('Enter URL: ')


def get_video_info(func):
    def inner(url):
        try:
            yt = YouTube(url)
            title = yt.title
            views = yt.views
            length = yt.length
            author = yt.author
            context = {
                "title": title,
                "author": author,
                "views": views,
                "length": length,
            }

            print(f"\nTitle: {context['title']}")
            print(f"Author: {context['author']}")
            print(f"Views: {context['views']}")
            print(f"Length: {round(context['length']/60,2)} minutes\n")

        except exceptions.PytubeError as e:
            exit(f"Oops!, {e}")
        return func(url)
    return inner


@get_video_info
def download_audio(url):
    print("Downloading...")
    _ = YouTube(url).streams.get_audio_only().download('music/')
    print("Finished Downloading")


def download_playlists(url):
    try:
        pl = Playlist(url)
        print("Total videos:", len(pl))
        for audio in pl.videos:
            audio.streams.get_audio_only().download()
            print("Downloading", audio.title)
    except exceptions.PytubeError as e:
        exit(f"Oops!, {e}")


try:
    download_playlists(url)
except KeyError:
    download_audio(url)
