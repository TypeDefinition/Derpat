import time

from system import System
from vector2 import Vector2
from mouseController import *

from petStates import PetState

class SnatchMouse(System):
    FOLLOW_SPEED = 10
    MOUSE_CATCH_OFFSET = 10 

    MAX_FOLLOW_TIME_AMT = 5 # after a certain amt of time give up
    MIN_FOLLOW_TIME_AMT = 2 

    MAX_SNATCH_TIME_AMT = 5 # in seconds
    MIN_SNATCH_TIME_AMT = 2

    #pet follows the mouse ard
    def followMouse(self, pet):
        mousePos = getMousePos()

        dir = mousePos.__sub__(pet.pos)
        dir = dir.normalised()

        pet.translate(round(dir.x) * SnatchMouse.FOLLOW_SPEED, round(dir.y) * SnatchMouse.FOLLOW_SPEED)

    #check if pet close enough to grab the mouse
    def checkGetMouse(self, pet):
        dir = getMousePos().__sub__(pet.pos)
        return dir.length() < SnatchMouse.MOUSE_CATCH_OFFSET

    # update snatching the mouse
    def snatchMouseUpdate(self, pet):
        self.followMouse(pet)

        #TODO:: might want to move this part somewhere else like the proper statemachine
        if self.checkGetMouse():
            pet.snatchStartTime = time.time()
            pet.state = PetState.CHASE_MOUSE




    def initTakeMouse(self, pet):
        pet.snatchStartTime = 0
        pet.snatchTime = 0

    #behavior for taking the mouse and running away
    def takeMouse(self, pet):
        #let go of mouse after a while
        if (time.time() > pet.snatchStartTime + SnatchMouse.MAX_SNATCH_TIME_AMT):
            return False

        #set random directions


        setMousePos(pet.pos.x, pet.pos.y) #mouse attached to pet

        #pet.state = PetState.IDLE #TODO:: TEMP CODE REMOVE THIS

        return True
