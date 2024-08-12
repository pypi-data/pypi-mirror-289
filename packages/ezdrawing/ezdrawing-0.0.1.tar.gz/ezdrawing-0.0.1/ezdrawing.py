import math
import pygame

def validateInitialized():
    global initialized
    if not initialized:
        raise Exception("ezdrawing is not initialized. Call init() to initialize")

def validateIntegerInRange(integer, integerName = "integer", low = None, high = None):
    if type(integer) != int:
        raise Exception(f"{integerName} is not an integer (it is {type(integer)})")
    if low != None and high != None:
        if integer < low or integer > high:
            raise Exception(f"{integerName} is outside the range {low}-{high} (it is {integer})")
    elif low != None:
        if integer < low:
            raise Exception(f"{integerName} is less than {low} (it is {integer})")
    elif high != None:
        if integer > high:
            raise Exception(f"{integerName} is more than {high} (it is {integer})")

def validateColor(color, name = "color"):
    if type(color) != tuple:
        raise Exception(f"{name} is not a tuple (it is {type(color)})")
    if len(color) != 3:
        raise Exception(f"{name} is not a tuple of 3 values (has {len(color)} values)")
    for i in range(3):
        validateIntegerInRange(color[i], f"{name}[{i}]", 0, 255)

def validatePositionOrSize(pos, name = "pos"):
    if type(pos) != tuple:
        raise Exception(f"{name} is not a tuple (it is {type(pos)})")
    if len(pos) != 2:
        raise Exception(f"{pos} is not a tuple of 2 values (has {len(pos)} values)")
    for i in range(2):
        validateIntegerInRange(pos[i], f"{name}[{i}]")

def validateRect(topLeft, bottomRight, topLeftName = "topLeft", bottomRightName = "bottomRight"):
    validatePositionOrSize(topLeft, topLeftName)
    validatePositionOrSize(bottomRight, bottomRightName)
    if(topLeft[0] > bottomRight[0]):
        raise Exception(f"{topLeftName} is to the right of {bottomRightName} (x={topLeft[0]} vs x={bottomRight[0]})")
    if(topLeft[1] > bottomRight[1]):
        raise Exception(f"{topLeftName} is below of {bottomRightName} (y={topLeft[1]} vs y={bottomRight[1]})")

def validateString(string, name = "string"):
    if type(string) != str:
        raise Exception(f"{name} is not a string (it is {type(string)})")

def validateFont(fontName, name = "fontName"):
    validateString(fontName, name)
    if not fontName in pygame.font.get_fonts():
        raise Exception(f"{name} ({fontName}) was not found in the system fonts. Valid fonts can be found with pygame.font.get_fonts()")

canUndo_ = False
def canUndo():
    global canUndo_
    return canUndo_

def updateOldWindow():
    global canUndo_, window, windowSurfaceOld
    windowSurfaceOld.blit(window, (0, 0))
    canUndo_ = True
    
def undo():
    global canUndo_
    global window, windowSurfaceOld
    window.blit(windowSurfaceOld, (0, 0))
    canUndo_ = False

def drawRect(color, topLeft, bottomRight):
    global window
    validateColor(color)
    validateRect(topLeft, bottomRight)
    
    updateOldWindow()
    
    pygame.draw.rect(window, color, (*topLeft, *bottomRight))

def drawEllipse(color, topLeft, bottomRight):
    global window
    validateColor(color)
    validateRect(topLeft, bottomRight)
    
    updateOldWindow()
    
    pygame.draw.ellipse(window, color, (*topLeft, *bottomRight))

def drawLine(color, pointA, pointB, width):
    global window
    validateColor(color)
    validatePositionOrSize(pointA, "pointA")
    validatePositionOrSize(pointB, "pointB")
    validateIntegerInRange(width, "width", 0)
    
    updateOldWindow()
    
    if pointA == pointB: #avoid division by 0 by just not drawing anything
        return

    offset = (pointB[0] - pointA[0], pointB[1] - pointA[1]) #vector from pointA to pointB
    offset = (-offset[1], offset[0]) #rotate 90 degrees
    len = (offset[0] ** 2 + offset[1] ** 2) ** 0.5
    offset = ((offset[0] * width) / (len * 2), 
            (offset[1] * width) / (len * 2)) #normalize and multiply by width / 2
    offset1AbsCeil = (math.ceil(abs(offset[0])), math.ceil(abs(offset[1]))) #make sure to round away from 0 so you never have width 0
    offset = (offset1AbsCeil[0] if offset[0] > 0 else -offset1AbsCeil[0],
            offset1AbsCeil[1] if offset[1] > 0 else -offset1AbsCeil[1]) #get sign back
    pygame.draw.polygon(window, color, [(pointA[0] + offset[0], pointA[1] + offset[1]),
                                        (pointB[0] + offset[0], pointB[1] + offset[1]),
                                        (pointB[0] - offset[0], pointB[1] - offset[1]),
                                        (pointA[0] - offset[0], pointA[1] - offset[1])]) #get the 4 points of the line and draw

def drawText(text, fontName, size, position, color):
    global window
    validateString(text, "text")
    validateFont(fontName, "fontName")
    validateIntegerInRange(size, "size", 1)
    validatePositionOrSize(position, "position")
    validateColor(color, "color")
    
    updateOldWindow()
    
    font = pygame.font.SysFont(fontName, size)
    surface = font.render(text, False, color)
    window.blit(surface, position)  

#input/event handling stuff
def handleEvents():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            handleQuitEvent(event)
        elif event.type in [pygame.KEYDOWN, pygame.KEYUP]:
            handleKeyButtonEvent(event)
        elif event.type == pygame.MOUSEMOTION:
            handleMouseMotion(event)
        elif event.type in [pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP]:
            handleMouseButtonEvent(event)

shouldQuit_ = False
def handleQuitEvent(event):
    global shouldQuit_
    shouldQuit_ = True

def shouldQuit():
    global shouldQuit_
    handleEvents()
    return shouldQuit_

pressedKeyEvents = []
def handleKeyButtonEvent(event):
    global pressedKeyEvents
    i = 0
    while i < len(pressedKeyEvents):
        if event.key == pressedKeyEvents[i].key:
            pressedKeyEvents.pop(i)
            i -= 1
        i += 1
    if event.type == pygame.KEYDOWN:
        pressedKeyEvents.append(event) #add it so it's the latest (as it should be)

def getPressedKeys():
    global pressedKeyEvents
    handleEvents()
    keyStrings = []
    for event in pressedKeyEvents:
        keyStrings.append(pygame.key.name(event.key))
    return keyStrings

def getPossibleKeys():
    possibleKeys = [pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, 
                    pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9, 
                    pygame.K_AC_BACK, pygame.K_AMPERSAND, pygame.K_ASTERISK, pygame.K_AT, 
                    pygame.K_BACKQUOTE, pygame.K_BACKSLASH, pygame.K_BACKSPACE, pygame.K_BREAK, 
                    pygame.K_CAPSLOCK, pygame.K_CARET, pygame.K_CLEAR, pygame.K_COLON, 
                    pygame.K_COMMA, pygame.K_CURRENCYSUBUNIT, pygame.K_CURRENCYUNIT, 
                    pygame.K_DELETE, pygame.K_DOLLAR, pygame.K_DOWN, pygame.K_END, 
                    pygame.K_EQUALS, pygame.K_ESCAPE, pygame.K_EURO, pygame.K_EXCLAIM, 
                    pygame.K_F1, pygame.K_F10, pygame.K_F11, pygame.K_F12, pygame.K_F13, 
                    pygame.K_F14, pygame.K_F15, pygame.K_F2, pygame.K_F3, pygame.K_F4, 
                    pygame.K_F5, pygame.K_F6, pygame.K_F7, pygame.K_F8, pygame.K_F9, 
                    pygame.K_GREATER, pygame.K_HASH, pygame.K_HELP, pygame.K_HOME, 
                    pygame.K_INSERT, pygame.K_KP0, pygame.K_KP1, pygame.K_KP2, pygame.K_KP3, 
                    pygame.K_KP4, pygame.K_KP5, pygame.K_KP6, pygame.K_KP7, pygame.K_KP8, 
                    pygame.K_KP9, pygame.K_KP_0, pygame.K_KP_1, pygame.K_KP_2, pygame.K_KP_3, 
                    pygame.K_KP_4, pygame.K_KP_5, pygame.K_KP_6, pygame.K_KP_7, pygame.K_KP_8, 
                    pygame.K_KP_9, pygame.K_KP_DIVIDE, pygame.K_KP_ENTER, pygame.K_KP_EQUALS, 
                    pygame.K_KP_MINUS, pygame.K_KP_MULTIPLY, pygame.K_KP_PERIOD, pygame.K_KP_PLUS, 
                    pygame.K_LALT, pygame.K_LCTRL, pygame.K_LEFT, pygame.K_LEFTBRACKET, 
                    pygame.K_LEFTPAREN, pygame.K_LESS, pygame.K_LGUI, pygame.K_LMETA, 
                    pygame.K_LSHIFT, pygame.K_LSUPER, pygame.K_MENU, pygame.K_MINUS, 
                    pygame.K_MODE, pygame.K_NUMLOCK, pygame.K_NUMLOCKCLEAR, pygame.K_PAGEDOWN, 
                    pygame.K_PAGEUP, pygame.K_PAUSE, pygame.K_PERCENT, pygame.K_PERIOD, 
                    pygame.K_PLUS, pygame.K_POWER, pygame.K_PRINT, pygame.K_PRINTSCREEN, 
                    pygame.K_QUESTION, pygame.K_QUOTE, pygame.K_QUOTEDBL, pygame.K_RALT, 
                    pygame.K_RCTRL, pygame.K_RETURN, pygame.K_RGUI, pygame.K_RIGHT, 
                    pygame.K_RIGHTBRACKET, pygame.K_RIGHTPAREN, pygame.K_RMETA, pygame.K_RSHIFT, 
                    pygame.K_RSUPER, pygame.K_SCROLLLOCK, pygame.K_SCROLLOCK, pygame.K_SEMICOLON, 
                    pygame.K_SLASH, pygame.K_SPACE, pygame.K_SYSREQ, pygame.K_TAB, pygame.K_UNDERSCORE, 
                    pygame.K_UNKNOWN, pygame.K_UP, pygame.K_a, pygame.K_b, pygame.K_c, 
                    pygame.K_d, pygame.K_e, pygame.K_f, pygame.K_g, pygame.K_h, 
                    pygame.K_i, pygame.K_j, pygame.K_k, pygame.K_l, pygame.K_m, 
                    pygame.K_n, pygame.K_o, pygame.K_p, pygame.K_q, pygame.K_r, 
                    pygame.K_s, pygame.K_t, pygame.K_u, pygame.K_v, pygame.K_w, 
                    pygame.K_x, pygame.K_y, pygame.K_z]
    return [pygame.key.name(key) for key in possibleKeys]

mousePos = (0, 0)
def handleMouseMotion(event):
    global mousePos
    mousePos = (int(event.pos[0]), int(event.pos[1]))

def getMousePos():
    global mousePos
    handleEvents()
    return mousePos

pressedMouseButtonEvents = []
def handleMouseButtonEvent(event):
    global pressedMouseButtonEvents
    i = 0
    while i < len(pressedMouseButtonEvents):
        if event.button == pressedMouseButtonEvents[i].button:
            pressedMouseButtonEvents.pop(i)
            i -= 1
        i += 1
    if event.type == pygame.MOUSEBUTTONDOWN:
        pressedMouseButtonEvents.append(event) #add it so it's the latest (as it should be)

def getPressedMouseButtons():
    global pressedMouseButtonEvents
    handleEvents()
    buttons = []
    for event in pressedMouseButtonEvents:
        buttons.append(event.button)
    return buttons

window = None
windowSurfaceOld = None
initialized = False
def openWindow(windowSize):
    validatePositionOrSize(windowSize, "windowSize")
    for i in range(2):
        validateIntegerInRange(windowSize[i], f"windowSize[{i}]", 1)
    
    global window, windowSurfaceOld, initialized
    pygame.init()

    window = pygame.display.set_mode(windowSize)
    window.fill((255, 255, 255))

    windowSurfaceOld = pygame.Surface(windowSize)
    updateOldWindow()

    pygame.display.flip()
    
    initialized = True

def update():
    pygame.display.flip()

def quit():
    pygame.quit()