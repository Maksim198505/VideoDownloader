import requests
import pytube


link = input("Enter the link of video you want to download: ")


def download_file(url):
    local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter
    r = requests.get(url, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)
                # f.flush() commented by recommendation from J.F.Sebastian
    return local_filename


def download_video(url):
    youtube = pytube.YouTube(url)
    video = youtube.streams.get_highest_resolution()
    print(video.title)
    print("Downloading...")
    video.download()
    print("Download completed!!")


def main_download():
    if "youtube" in link:
        download_video(link)
    else:
        download_file(link)


main_download()
