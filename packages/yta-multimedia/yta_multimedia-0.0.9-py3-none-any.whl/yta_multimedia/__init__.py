from video.generation.google import GoogleSearch

def test():
    GoogleSearch().generate().write_videofile('test.mp4')

test()