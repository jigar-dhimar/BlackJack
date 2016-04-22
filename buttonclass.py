# button.py
# for lab 8 on writing classes
from graphics import *

class Button:

    """A button is a labeled rectangle in a window.
    It is enabled or disabled with the activate()
    and deactivate() methods. The clicked(pt) method
    returns True if and only if the button is enabled and pt is inside it."""

    def __init__(self, win, center, width, height, label):
        """ Creates a rectangular button, eg:
qb = Button(myWin, centerPoint, width, height, 'Quit')"""
        w,h = width*.5, height*.5
        x,y = center.getX(), center.getY()
        self.xmax, self.xmin = x+w, x-w 
        self.ymax, self.ymin = y+h, y-h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1,p2)
        self.rect.setFill('lightgray')
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.active = False 

    def getLabel(self):
        """Returns the label string of this button."""
        return self.label.getText()

    def activate(self):
        """Sets this button to 'active'."""
        self.label.setFill('black') 
        self.rect.setWidth(2)       
        self.active = True          


    def deactivate(self):
        """Sets this button to 'inactive'."""
        self.label.setFill('darkgray')
        self.rect.setWidth(.5)
        self.active = False

    def clicked(self, p):
        """Returns true if button active and Point p is inside"""
        if self.active == True:
            if self.xmin < p.getX() < self.xmax and self.ymin < p.getY() < self.ymax:
                return True

    def undraw(self):
        """Undraws the Rectangle and Label components of the Button"""
        self.rect.undraw()
        self.label.undraw()
