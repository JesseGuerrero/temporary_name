import pyglet

width = 500
height = 500

window = pyglet.window.Window(width, height, "Video Player")

Path = "Oklahoma.mp4"

player = pyglet.media.Player()

source = pyglet.media.StreamingSource()

MediaLoad = pyglet.media.load(Path)

player.queue(MediaLoad)

player.play()

@window.event
def on_draw():
    window.clear()
    if player.source and player.source.video_format:
        player.get_texture().blit(0, 0)

pyglet.app.run()
