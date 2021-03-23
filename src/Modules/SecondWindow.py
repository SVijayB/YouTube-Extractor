from pytube import YouTube
from pytube import Playlist
from tkinter import *


class SecondWindow:
    def __init__(
        self, downloadWindow, youtubeEntry, folderName, choice, playlistChoice
    ):
        self.downloadWindow = downloadWindow
        self.downloadWindow.state("zoomed")
        self.downloadWindow.grid_rowconfigure(0, weight=0)
        self.downloadWindow.grid_columnconfigure(0, weight=1)
        self.youtubeEntry = youtubeEntry
        self.folderName = folderName
        self.choice = choice
        self.playlistChoice = playlistChoice

        self.yt = YouTube(self.youtubeEntry)

        if self.playlistChoice == "1":
            self.PL = Playlist(self.youtubeEntry)
            self.batchDownload()
        else:
            if self.choice == "1":
                self.stream = self.yt.streams.first()
                self.downloadFile()

            elif self.choice == "2":
                self.stream = self.yt.streams.filter(only_audio=True).first()
                self.downloadFile()

        self.loading = Label(
            self.downloadWindow,
            text="Download Completed\nThanks For Using YouTube Extractor",
            font=("Small Fonts", 40),
        )
        self.loading.grid(pady=(100, 0))
        downloadWindow.protocol("WM_DELETE_WINDOW", self.closing)
        downloadWindow.mainloop()

    def downloadFile(self):
        print(
            "\nYour File Is Being Downloaded...\nWe will notify you once the download is completed."
        )
        print("Thank you For Using YouTube Extractor")
        self.stream.download(self.folderName)

    def batchDownload(self):
        print(
            "\nYour Files Are Being Downloaded...\nWe will notify you once the download is completed."
        )
        print("Thank you For Using YouTube Extractor")
        if self.choice == "1":
            for video in self.PL.videos:
                video.streams.first().download(self.folderName)
        elif self.choice == "2":
            for video in self.PL.videos:
                video.streams.filter(only_audio=True).first().download(self.folderName)

    def closing(self):
        sys.exit(0)
