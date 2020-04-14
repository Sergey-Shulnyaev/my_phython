from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# Процедура инициализации
def init():
	glEnable(GL_DEPTH_TEST)
	glClearColor(0.5, 0.5, 0.5, 1.0) # Серый цвет для первоначальной закраски
	gluOrtho2D(-1.0, 1.0, -1.0, 1.0) # Определяем границы рисования по горизонтали и вертикали

# Процедура обработки обычных клавиш
def keyboardkeys(key, x, y):
	if key == b'\x1b':
		sys.exit(0)
	glutPostRedisplay()         # Вызываем процедуру перерисовки

def cube(center, half):
        v1 = (center[0] - half, center[1] - half, center[2] - half) #v2 v4 v5
        v2 = (center[0] + half, center[1] - half, center[2] - half)#v1 v3 v6
        v3 = (center[0] + half, center[1] + half, center[2] - half)#v2 v4 v7 
        v4 = (center[0] - half, center[1] + half, center[2] - half)# v1 v3 v8
        v5 = (center[0] - half, center[1] - half, center[2] + half)# v1 v6 v8
        v6 = (center[0] + half, center[1] - half, center[2] + half)#v5 v7 v2
        v7 = (center[0] + half, center[1] + half, center[2] + half)#v6 v8 v3
        v8 = (center[0] - half, center[1] + half, center[2] + half)#v5 v7 v4

        glColor3f(1, 0, 0)
        glVertex3d(v1[0], v1[1], v1[2])
        glVertex3d(v2[0], v2[1], v2[2])
        glVertex3d(v3[0], v3[1], v3[2])
        glVertex3d(v4[0], v4[1], v4[2])

        glColor3f(0, 1, 0)
        glVertex3d(v1[0], v1[1], v1[2])
        glVertex3d(v5[0], v5[1], v5[2])
        glVertex3d(v6[0], v6[1], v6[2])
        glVertex3d(v2[0], v2[1], v2[2])

        glColor3f(0, 0, 1)
        glVertex3d(v2[0], v2[1], v2[2])
        glVertex3d(v6[0], v6[1], v6[2])
        glVertex3d(v7[0], v7[1], v7[2])
        glVertex3d(v3[0], v3[1], v3[2])

        glColor3f(0, 1, 1)
        glVertex3d(v3[0], v3[1], v3[2])
        glVertex3d(v7[0], v7[1], v7[2])
        glVertex3d(v8[0], v8[1], v8[2])
        glVertex3d(v4[0], v4[1], v4[2])

        glColor3f(1, 0, 1)
        glVertex3d(v1[0], v1[1], v1[2])
        glVertex3d(v5[0], v5[1], v5[2])
        glVertex3d(v8[0], v8[1], v8[2])
        glVertex3d(v4[0], v4[1], v4[2])

        glColor3f(1, 1, 0)
        glVertex3d(v5[0], v5[1], v5[2])
        glVertex3d(v6[0], v6[1], v6[2])
        glVertex3d(v7[0], v7[1], v7[2])
        glVertex3d(v8[0], v8[1], v8[2])

# Процедура рисования
def draw(*args, **kwargs):
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # Очищаем экран и заливаем текущим цветом фона
	glRotated(0.125,1,1,1)

	glBegin(GL_QUADS)
	cube((0.5,0.5,0.5), 0.1)
	cube((-0.5,0.5,0.5), 0.1)
	cube((-0.5,-0.5,0.5), 0.1)
	cube((0.5,-0.5,0.5), 0.1)
	cube((0.5,0.5,-0.5), 0.1)
	cube((-0.5,0.5,-0.5), 0.1)
	cube((-0.5,-0.5,-0.5), 0.1)
	cube((0.5,-0.5,-0.5), 0.1)
	
	glEnd()

	glutSwapBuffers()           # Меняем буферы
	glutPostRedisplay()         # Вызываем процедуру перерисовки

glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(800, 600)
glutInitWindowPosition(50, 50)
glutInit(sys.argv)
glutCreateWindow(b"OpenGL Second Program!")
# Определяем процедуру, отвечающую за рисование
glutDisplayFunc(draw)
# Определяем процедуру, отвечающую за обработку обычных клавиш
glutKeyboardFunc(keyboardkeys)
# Вызываем нашу функцию инициализации
init()
glutMainLoop()
