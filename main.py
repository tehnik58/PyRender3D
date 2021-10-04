import pygame as r_tool

class Render:
    def __init__(self):
        r_tool.init()
        self.RES = self.WIDTH, self.HEIGHT = 1200, 720
        self.H_WIDTH ,self.H_HEIGHT = self.WIDTH // 2, self.HEIGHT // 2
        self.FPS = 60
        self.screen = r_tool.display.set_mode(self.RES)
        self.clock = r_tool.time.Clock()

    def draw(self):
        self.screen.fill(r_tool.Color('darkgreen'))
    
    def run(self):
        while True:
            self.draw()
            [exit() for i in r_tool.event.get() if i.type == r_tool.QUIT]
            r_tool.display.set_caption(str(self.clock.get_fps()))
            r_tool.display.flip()
            self.clock.tick(self.FPS)

if __name__ == '__main__':
    app = Render()
    app.run()