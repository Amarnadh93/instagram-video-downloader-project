import yt_dlp
url = input("Enter Instagram Reel/Post URL: ")
ydl_opts = {
    'outtmpl': 'instagram_video.%(ext)s'
}
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
print("Download complete ✅")