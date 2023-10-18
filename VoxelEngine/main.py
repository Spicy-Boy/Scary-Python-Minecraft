from settings import *
import moderngl as mgl
import pygame as pg
import sys

class VoxelEngine:
    
    def __init__(self):
        #some initial pygame settings, I don't know the difference so following some defaults
        pg.init()
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)
        pg.display.gl_set_attribute(pg.GL_DEPTH_SIZE, 24) #24 bits
        
        pg.display.set_mode(WIN_RES, flags=pg.OPENGL | pg.DOUBLEBUF)
        self.ctx = mgl.create_context()
        
        self.ctx.enable(flags = mgl.DEPTH_TEST | mgl.CULL_FACE | mgl.BLEND)
        self.ctx.gc_mode = 'auto' #automatic garbage collection for unused objects
        
        self.clock = pg.time.Clock()
        self.delta_time = 0
        self.time = 0
        
        self.is_running = True #used in the run() method to drive the main loop
        
        
    def update(self):
        self.delta_time = self.clock.tick() #ticks up every time the game updates
        self.time = pg.time.get_ticks() * 0.001
        pg.display.set_caption(f'{self.clock.get_fps() : .0f}') #displays frame rate in the window title
    
    def render(self):
        self.ctx.clear(color=BG_COLOR) #clears the previous frame
        pg.display.flip() #displays a new frame
    
    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE): #watches for closing the window OR hitting escape
                self.is_running = False
        
    def run(self):
        while self.is_running:  #MAIN LOOP!!!
            self.handle_events()
            self.update()
            self.render()
        pg.quit()
        sys.exit()
    
if __name__ == '__main__':
    app = VoxelEngine()
    app.run()