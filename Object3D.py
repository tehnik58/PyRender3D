import pygame as r_tool
import matrix_func
import numpy as np
from Camera import*

class Object3D():
    def __init__(self, render):
        self.render = render
        self.vertexes = np.array([(0, 0, 0, 1), (0, 1 ,0 ,1), (1, 1, 0, 1), (1, 0, 0, 1),
        (0, 0, 1, 1),(0, 1, 1, 1), (1, 1, 1, 1), (1, 0, 1, 1)])
        self.faces = np.array([(0, 1, 2, 3), (1, 2, 6, 5), (0, 1, 5, 4), (3, 2, 6, 7)])

    def draw(self):
        self.screen_projection()

    def screen_projection(self):
        vertexes = self.vertexes @ self.render.camera.camera_matrix()
        vertexes = vertexes @ self.render.projection.projection_matrix
        vertexes /= vertexes[:, -1].reshape(-1, 1)
        vertexes[(vertexes > 2) | (vertexes < -2)] = 0
        vertexes = vertexes @ self.render.projection.to_screen_matrix
        vertexes = vertexes[:, :2]

        for face in self.faces:
            polygon = vertexes[face]
            if not np.any((polygon == self.render.H_WIDTH) | (polygon == self.render.H_HEIGHT)):
                r_tool.drow.polygon(self.render.screen, r_tool.Color('orange'), polygon, 3)
                
        for vertex in self.vertexes:
            if not np.any((vertex == self.render.H_WIDTH) | (vertex == self.render.H_HEIGHT)):
                r_tool.drow.circle(self.render.screen, r_tool.Color('white'), polygon, 6)

    def translate(self, pos):
        self.vertexes = self.vertexes @ matrix_func.translate(pos)
    
    def scale(self, scale_to):
        self.vertexes = self.vertexes @ matrix_func.scale(scale_to)
    
    def rotation_x(self, a_x):
        self.vertexes = self.vertexes @ matrix_func.rotation_x(a_x)
    
    def rotation_y(self, a_y):
        self.vertexes = self.vertexes @ matrix_func.rotation_y(a_y)
    
    def rotation_z(self, a_z):
        self.vertexes = self.vertexes @ matrix_func.rotation_z(a_z)