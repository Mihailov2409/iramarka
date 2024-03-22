from kivy.app import App
from kivy.uix.video import Video
from kivy.uix.widget import Widget


class VideoWindow(App):
    def build(self):
        # start playing the video at creation
        video.volume = 0
        return video


if __name__ == "__main__":
    window = VideoWindow()
    window.run()
