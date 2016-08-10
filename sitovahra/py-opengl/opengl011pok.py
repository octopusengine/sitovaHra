import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

# Set up some variables containing the screeen size
colYel = (255,255,0)
colWhi = (255,255,255)
colRed = (255,0,0)
colBlu = (0,0,255)
colSil = (128,128,128)
colBla = (0,0,0)
gcWhi = [(1.0), (1.0), (1.0)]
gcRed = (1.0, 0.0, 0.0)
gcBlu = (0.0, 0.0, 1.0)


verticies = (
    (1, -1, -1), (1, 1, -1), (-1, 1, -1), (-1, -1, -1), (1, -1, 1), (1, 1, 1), (-1, -1, 1), (-1, 1, 1)
    )

edges = (
    (0,1), (0,3), (0,4), (2,1),
    (2,3), (2,7), (6,3), (6,4),
    (6,7), (5,1), (5,4), (5,7)
    )

points = (
    (0,1,1),(20,50,30)
    )


def Point():
    glColor3f(1.0, 1.0, 0.0);
    glBegin(GL_POINTS)
    glVertex3f( 7, 15, 0);
    glVertex3f( 6, 7, 0);
    glVertex3f( 6, 8, 0);
    glEnd()

def Triangle(s):
    glPushMatrix()
    glScalef(s,s,s)
    glBegin(GL_TRIANGLES)
    glVertex3f(-5, -5, 0)
    glVertex3f( 5, -5, 10)
    glVertex3f( 0,  5, 0)
    glEnd()
    glPopMatrix()
    

def Cube0():
    glColor3f(1.0, 1.0, 1.0);
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()
    
def Cube(s):
    glColor3f(1.0, 0.0, 1.0);
    glPushMatrix()
    glTranslatef(s*10,0,0)
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()
    glPopMatrix()


def Line():
    glLineWidth(3.5); 
    glColor3f(0.0, 0.0, 1.0);
    glBegin(GL_LINES);
    glVertex3f(0.0, 0.0, 0.0);
    glVertex3f(15, 0, 0);
    glEnd();



def main():
    ss=0.1
    pygame.init()
    display = (1200,800)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    
    #pygame.draw.rect(display, colRed, (100,100,50,150), 2)
    #pygame.draw.line(display, colYel,(110,90),(110,190),2) 

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0,0.0, -30)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    ss=ss+0.1
                if event.key == pygame.K_RIGHT:
                    ss=ss-0.1

                if event.key == pygame.K_UP:
                    glTranslatef(0,1,0)
                if event.key == pygame.K_DOWN:
                    ss=0

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    glTranslatef(0,0,1.0)

                if event.button == 5:
                    glTranslatef(0,0,-1.0)



        #glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Line()
        Point()
        Triangle(ss)
        #ss=ss+0.001
        #if ss>10:
        #    ss=0.1
        Cube0()
        Cube(ss)
        pygame.display.flip()
        pygame.time.wait(10)


main()
