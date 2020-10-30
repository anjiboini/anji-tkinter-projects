
try:
    from pytube import YouTube
    from pytube import Playlist
except  Exception as e:
    print("Some Modules are missing {}".format(e))

url = "https://www.youtube.com/watch?v=QWqxRchawZY&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=40"
ytd = YouTube(url).streams.first().download()
#print(ytd)
#for x in ytd.streams.all():
  #  print(x)

#ytd = YouTube(url)
#print(ytd.streams.filter(adaptive=True).all())
