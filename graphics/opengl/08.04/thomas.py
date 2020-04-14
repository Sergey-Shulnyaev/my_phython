from math import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# Процедура инициализации
def init():
	glEnable(GL_DEPTH_TEST)
	glClearColor(0.8, 0.8, 0.8, 1.0) # Белый цвет для первоначальной закраски
	gluOrtho2D(-2.0, 2.0, -2.0, 2.0) # Определяем границы рисования по горизонтали и вертикали
	global anglex, angley, anglez, filled, measure
	anglex = 0
	angley = 0
	anglez = 0
	filled = 0
	measure = 1

# Процедура обработки обычных клавиш
def keyboardkeys(key, x, y):
	global anglex, angley, anglez, filled, measure
	if key == b'\x1b':
		sys.exit(0)
	if key == b'w':
		anglex += 5
	if key == b's':
		anglex -= 5
	if key == b'q':
		angley += 5
	if key == b'e':
		angley -= 5
	if key == b'a':
		anglez += 5
	if key == b'd':
		anglez -= 5
	if key == b'=':
		measure += 0.01
	if key == b'-':
		measure -= 0.01	
	if key == b' ':
		filled = 1 - filled
	glutPostRedisplay()         # Вызываем процедуру перерисовки

def cilinder():
	R = 0.5

	glBegin(GL_TRIANGLE_FAN)

	glVertex3d( 0,  0, -0.5)
	for i in range(21):
		glVertex3d(R * cos(2*pi*i/20), \
			R * sin(2*pi*i/20), -0.5)

	glEnd()

	glBegin(GL_QUAD_STRIP)

	for i in range(21):
		glVertex3d(R * cos(2*pi*i/20), \
			R * sin(2*pi*i/20), -0.5)
		glVertex3d(R * cos(2*pi*i/20), \
			R * sin(2*pi*i/20), 0.5)

	glEnd()

	glBegin(GL_TRIANGLE_FAN)

	glVertex3d( 0,  0, 0.5)
	for i in range(21):
		glVertex3d(R * cos(2*pi*i/20), \
			R * sin(2*pi*i/20), 0.5)

	glEnd()

def conus():
	R = 0.5

	glBegin(GL_TRIANGLE_FAN)

	glVertex3d( 0,  0, -0.5)
	for i in range(21):
		glVertex3d(R * cos(2*pi*i/20), \
			R * sin(2*pi*i/20), -0.5)

	glEnd()

	glBegin(GL_TRIANGLE_FAN)

	glVertex3d( 0,  0, 0.5)
	for i in range(21):
		glVertex3d(R * cos(2*pi*i/20), \
			R * sin(2*pi*i/20), -0.5)

	glEnd()

def sphere():
	R = 0.5

	for j in range(-9,9):
		glBegin(GL_QUAD_STRIP)

		for i in range(21):
			glVertex3d(R * cos(pi*j/18) * cos(2*pi*i/20), \
				R * cos(pi*j/18) * sin(2*pi*i/20), \
				R * sin(pi*j/18))
			glVertex3d(R * cos(pi*(j+1)/18) * cos(2*pi*i/20), \
				R * cos(pi*(j+1)/18) * sin(2*pi*i/20), \
				R * sin(pi*(j+1)/18))

		glEnd()

def thor():
	R = 0.5
	R2 = R * 0.3

	for i in range(20):
		glBegin(GL_QUAD_STRIP)

		for j in range(21):
			glVertex3d((R + R2 * cos(2*pi*j/20)) * cos(2*pi*i/20), \
				(R + R2 * cos(2*pi*j/20)) * sin(2*pi*i/20), \
				R2 * sin(2*pi*j/20))
			glVertex3d((R + R2 * cos(2*pi*j/20)) * cos(2*pi*(i+1)/20), \
				(R + R2 * cos(2*pi*j/20)) * sin(2*pi*(i+1)/20), \
				R2 * sin(2*pi*j/20))

		glEnd()

def cube():
	glBegin(GL_QUADS)

	glVertex3d( 0.5,  0.5, 0.5)
	glVertex3d(-0.5,  0.5, 0.5)
	glVertex3d(-0.5, -0.5, 0.5)
	glVertex3d( 0.5, -0.5, 0.5)
	
	glVertex3d( 0.5,  0.5,-0.5)
	glVertex3d(-0.5,  0.5,-0.5)
	glVertex3d(-0.5, -0.5,-0.5)
	glVertex3d( 0.5, -0.5,-0.5)
	
	glVertex3d( 0.5,  0.5, 0.5)
	glVertex3d( 0.5,  0.5,-0.5)
	glVertex3d( 0.5, -0.5,-0.5)
	glVertex3d( 0.5, -0.5, 0.5)

	glVertex3d(-0.5,  0.5, 0.5)
	glVertex3d(-0.5,  0.5,-0.5)
	glVertex3d(-0.5, -0.5,-0.5)
	glVertex3d(-0.5, -0.5, 0.5)

	glVertex3d( 0.5,  0.5, 0.5)
	glVertex3d( 0.5,  0.5,-0.5)
	glVertex3d(-0.5,  0.5,-0.5)
	glVertex3d(-0.5,  0.5, 0.5)

	glVertex3d( 0.5, -0.5, 0.5)
	glVertex3d( 0.5, -0.5,-0.5)
	glVertex3d(-0.5, -0.5,-0.5)
	glVertex3d(-0.5, -0.5, 0.5)

	glEnd()

# Процедура рисования
def draw(*args, **kwargs):
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # Очищаем экран и заливаем текущим цветом фона
	glLoadIdentity()
	global anglex, angley, anglez, filled, measure
	glRotated(anglex,1,0,0)
	glRotated(angley,0,1,0)
	glRotated(anglez,0,0,1)
	glScaled(measure, measure, measure)
	glRotated(-105,1,0,0)
	if filled == 1:
		glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
	else:
		glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)

	glPushMatrix()
	glColor3f(1, 0, 0)
	glRotated(90, 1, 0, 0)
	glScaled(0.5, 0.5, 1.2)
	cilinder()
	glPopMatrix()

        #поперечные для колёс
	#переднее
	glPushMatrix()
	glColor3f(0, 0.5, 0)
	glTranslated(0, 0.4, -0.3)
	glRotated(90, 0, 1, 0)
	glScaled(0.1, 0.1, 0.8)
	cilinder()
	glPopMatrix()
        #заднее
	glPushMatrix()
	glColor3f(0, 0.5, 0)
	glTranslated(0, -0.25, -0.3)
	glRotated(90, 0, 1, 0)
	glScaled(0.1, 0.1, 0.8)
	cilinder()
	glPopMatrix()

        #колёсики
	#переднее
	glPushMatrix()
	glColor3f(0.5, 0.5, 1)
	glTranslated(0.4, 0.4, -0.3)
	glRotated(90, 0, 1, 0)
	glScaled(0.1, 0.1, 0.1)
	sphere()
	glPopMatrix()
	
	glPushMatrix()
	glColor3f(0.5, 0.5, 1)
	glTranslated(-0.4, 0.4, -0.3)
	glRotated(90, 0, 1, 0)
	glScaled(0.1, 0.1, 0.1)
	sphere()
	glPopMatrix()
	
	glPushMatrix()
	glColor3f(0.3, 0, 0.6)
	glTranslated(-0.38, 0.4, -0.3)
	glRotated(90, 0, 1, 0)
	glScaled(0.3, 0.3, 0.05)
	cilinder()
	glPopMatrix()

	glPushMatrix()
	glColor3f(0.3, 0, 0.6)
	glTranslated(0.38, 0.4, -0.3)
	glRotated(90, 0, 1, 0)
	glScaled(0.3, 0.3, 0.05)
	cilinder()
	glPopMatrix()
	

	#заднее
	glPushMatrix()
	glColor3f(0.5, 0.5, 1)
	glTranslated(0.4, -0.25, -0.3)
	glRotated(90, 0, 1, 0)
	glScaled(0.1, 0.1, 0.1)
	sphere()
	glPopMatrix()

	glPushMatrix()
	glColor3f(0.5, 0.5, 1)
	glTranslated(-0.4, -0.25, -0.3)
	glRotated(90, 0, 1, 0)
	glScaled(0.1, 0.1, 0.1)
	sphere()
	glPopMatrix()
	
	glPushMatrix()
	glColor3f(0.3, 0, 0.6)
	glTranslated(0.38, -0.25, -0.3)
	glRotated(90, 0, 1, 0)
	glScaled(0.3, 0.3, 0.05)
	cilinder()
	glPopMatrix()
	
	glPushMatrix()
	glColor3f(0.3, 0, 0.6)
	glTranslated(-0.38, -0.25, -0.3)
	glRotated(90, 0, 1, 0)
	glScaled(0.3, 0.3, 0.05)
	cilinder()
	glPopMatrix()

	#корпус
	glPushMatrix()
	glColor3f(1, 1, 0)
	glTranslated(0, -0.7, 0.4)
	cube()
	glPopMatrix()

        #передняя штука
	glPushMatrix()
	glColor3f(0.5, 1, 0)
	glRotated(90, 1, 0, 0)
	glTranslated(0, 0, -0.75)
	glScaled(0.5, 0.5, -0.3)
	conus()
	glPopMatrix()

	#труба

	glPushMatrix()
	glColor3f(0, 0, 1)
	glTranslated(0, 0.30, 0.4)
	#glRotated(90, 0, 1, 0)
	glScaled(0.25, 0.25, 0.35)
	cilinder()
	glPopMatrix()

	glPushMatrix()
	glColor3f(1, 0.5, 0)
	glTranslated(0, 0.30, 0.62)
	#glRotated(90, 0, 1, 0)
	glScaled(0.35, 0.35, 0.1)
	cilinder()
	glPopMatrix()

        #дым
	glPushMatrix()
	glColor3f(0.3, 0.3, 0.3)
	glTranslated(0, 0.30, 0.72)
	#glRotated(90, 0, 1, 0)
	glScaled(0.25, 0.25, 0.25)
	thor()
	glPopMatrix()

	glPushMatrix()
	glColor3f(0.5, 0.5, 0.5)
	glTranslated(0, 0.30, 0.82)
	#glRotated(90, 0, 1, 0)
	glScaled(0.35, 0.35, 0.25)
	thor()
	glPopMatrix()
	
	glPushMatrix()
	glColor3f(0.7, 0.7, 0.7)
	glTranslated(0, 0.30, 0.92)
	#glRotated(90, 0, 1, 0)
	glScaled(0.45, 0.45, 0.25)
	thor()
	glPopMatrix()

	glPushMatrix()
	glColor3f(0.9, 0.9, 0.9)
	glTranslated(0, 0.30, 1.02)
	#glRotated(90, 0, 1, 0)
	glScaled(0.55, 0.55, 0.25)
	thor()
	glPopMatrix()

        #фонарик
	glPushMatrix()
	glColor3f(0.5, 0, 0)
	glTranslated(0, 0.55, 0.3)
	glScaled(0.1, 0.1, 0.1)
	cube()
	glPopMatrix()

	glPushMatrix()
	glColor3f(1, 1, 1)
	glTranslated(0, 0.6, 0.3)
	glRotated(90, 1, 0, 0)
	glScaled(0.1, 0.1, 0.1)
	conus()
	glPopMatrix()
	

	
	glutSwapBuffers()           # Меняем буферы
	glutPostRedisplay()         # Вызываем процедуру перерисовки

glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(600, 600)
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
