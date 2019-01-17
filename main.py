#Batman Paint.py
#Matthew Liu

#This is a Batman-themed mock paint program that includes a pencil, eraser, brush, spray can,
#fill bucket, color picker, line tool, rectangle tool, ellipse tool, and
#polygon tool. Colors can be picked from the spectrum and different sizes and
#brush tips can be selected. User also has the option to clear canvas, save
#the project, undo, redo, and add stamps.

from math import *
import os
from pygame import *
from random import *
import tkinter
############################## START SCREEN ##############################
os.environ['SDL_VIDEO_WINDOW_POS']='25,75'
window=display.set_mode((1228,690))
init()
font.init()
display.set_caption("Batman Paint")
startfont=font.Font("digital-7.ttf",40)
byfont=font.Font("digital-7.ttf",15)
button1=image.load("images/Button1.png")
button2=image.load("images/Button2.png")
text1=startfont.render("Welcome to Batman Paint",True,(255,255,255))
text2=startfont.render("START",True,(255,255,255))
text3=startfont.render("EXIT",True,(255,255,255))
byline=byfont.render("By: Matthew Liu",True,(50,50,255))
start=image.load("images/Background.png")

startRect=Rect(264,485,250,80)
exitRect=Rect(714,485,250,80)

window.blit(start,(0,0))
window.blit(button2,startRect)
window.blit(button2,exitRect)
window.blit(text1,(614-(text1.get_width()//2),300))
window.blit(text2,(389-(text2.get_width()//2),525-(text2.get_height()//2)))
window.blit(text3,(839-(text3.get_width()//2),525-(text3.get_height()//2)))
window.blit(byline,(1100,650))
starting=True
while starting:
    for evt in event.get():
        if evt.type==QUIT:
            starting=False
            running=False
    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()
    if startRect.collidepoint(mx,my):
        window.blit(button1,startRect)
        window.blit(text2,(389-(text2.get_width()//2),525-(text2.get_height()//2)))
        if mb[0]==1:
            draw.rect(window,(200,0,0),startRect,1)
        if evt.type==MOUSEBUTTONUP:
            starting=False
            running=True
    elif exitRect.collidepoint(mx,my):
        window.blit(button1,exitRect)
        window.blit(text3,(839-(text3.get_width()//2),525-(text3.get_height()//2)))
        if mb[0]==1:
            draw.rect(window,(200,0,0),exitRect,1)
        if evt.type==MOUSEBUTTONUP:
            starting=False
            running=False
    else:
        window.blit(button2,startRect)
        window.blit(button2,exitRect)
        window.blit(text2,(389-(text2.get_width()//2),525-(text2.get_height()//2)))
        window.blit(text3,(839-(text3.get_width()//2),525-(text3.get_height()//2)))
    display.flip()
quit()
############################## PAINT PROGRAM ##############################
if running:
    init()
    mixer.init()
    mixer.music.load("Theme.mp3")
    mixer.music.play(-1)
    os.environ['SDL_VIDEO_WINDOW_POS']='25,75'
    screen=display.set_mode((1225,800))
    display.set_caption("Batman Paint")
    font.init()
    mainfont=font.SysFont("Helvetica",15)
    font1=font.SysFont("Monospace",12)
    font2=font.SysFont("Helvetica",25)
    root=tkinter.Tk()
    root.withdraw()
    ############################## Images ##############################
    background=image.load("images/Background2.png")
    pencilButton=image.load("images/Pencil.png")
    eraserButton=image.load("images/Eraser.png")
    brushButton=image.load("images/Brush.png")
    sprayButton=image.load("images/Spray.png")
    buckButton=image.load("images/Bucket.png")
    pickButton=image.load("images/Picker.png")
    lineButton=image.load("images/Line.png")
    circleButton=image.load("images/Circle.png")
    rectButton=image.load("images/Rectangle.png")
    polyButton=transform.scale(image.load("images/Polygon.png"),(25,25))
    clearButton=transform.scale(image.load("images/Clear.png"),(25,25))
    stampButton=transform.scale(image.load("images/Stamp.png"),(25,25))
    saveButton=transform.scale(image.load("images/Save.png"),(25,25))
    loadButton=transform.scale(image.load("images/Load.png"),(25,25))
    undoButton=transform.scale(image.load("images/Undo.png"),(25,25))
    redoButton=transform.scale(image.load("images/Redo.png"),(25,25))
    spectrum=image.load("images/Spectrum.png")
    brush1=image.load("images/Brush-Circle1.png")
    brush2=image.load("images/Brush-Circle2.png")
    brush3=image.load("images/Brush-Circle3.png")
    brush4=image.load("images/Brush-Square1.png")
    brush5=image.load("images/Brush-Square2.png")
    brush6=image.load("images/Brush-Square3.png")
    brush7=transform.scale(image.load("images/Brush-Diag1.png"),(25,25))
    brush8=transform.scale(image.load("images/Brush-Diag2.png"),(25,25))
    brushes=[brush1,brush2,brush3,brush4,brush5,brush6,brush7,brush8]
    stick1=image.load("images/Logo1.png")
    stick2=image.load("images/Logo2.png")
    stick3=image.load("images/Logo3.png")
    stick4=image.load("images/Logo4.png")
    stick5=image.load("images/Logo5.png")
    stick6=image.load("images/Logo6.png")
    stick7=image.load("images/Logo7.png")
    stick8=image.load("images/Logo8.png")
    stick9=image.load("images/Logo9.png")
    stick10=image.load("images/Logo10.png")
    stick11=image.load("images/Logo11.png")
    stick12=image.load("images/Logo12.png")
    stick13=image.load("images/Logo13.png")
    stick14=image.load("images/Logo14.png")
    stick15=image.load("images/Logo15.png")
    stick16=image.load("images/Logo16.png")
    icon1=transform.scale(stick1,(40,40))
    icon2=transform.scale(stick2,(40,40))
    icon3=transform.scale(stick3,(40,40))
    icon4=transform.scale(stick4,(40,40))
    icon5=transform.scale(stick5,(40,40))
    icon6=transform.scale(stick6,(40,40))
    icon7=transform.scale(stick7,(40,40))
    icon8=transform.scale(stick8,(40,40))
    icon9=transform.scale(stick9,(40,40))
    icon10=transform.scale(stick10,(40,40))
    icon11=transform.scale(stick11,(40,40))
    icon12=transform.scale(stick12,(40,40))
    icon13=transform.scale(stick13,(40,40))
    icon14=transform.scale(stick14,(40,40))
    icon15=transform.scale(stick15,(40,40))
    icon16=transform.scale(stick16,(40,40))
    lines=image.load("images/Lines.png")
    #################################### Buttons #####################################
    screen.blit(background,(0,0))                       #Background
    draw.rect(screen,(255,255,255),(50,50,800,600),0)   #Canvas
    canvasRect=Rect(50,50,800,600)
    draw.rect(screen,(111,111,111),(50,670,800,100),0)  #Info Bar
    draw.rect(screen,(111,111,111),(900,50,290,80),0)   #Tool Bar
    draw.rect(screen,(111,111,111),(900,150,290,45),0)  #Brush Options
    draw.rect(screen,(111,111,111),(900,215,290,100),0) #Circle/Rect/Line/Poly Options
    draw.rect(screen,(111,111,111),(900,335,290,210),0) #Stamps
    for i in range(910,1190,35):                        #Buttons
        draw.rect(screen,(255,255,255),(i,60,25,25),0)
        draw.rect(screen,(255,255,255),(i,95,25,25),0)
    screen.blit(pencilButton,(910,60))                  #Pencil
    pencilRect=Rect(910,60,25,25)
    screen.blit(eraserButton,(910,95))                  #Eraser
    eraserRect=Rect(910,95,25,25)
    screen.blit(brushButton,(948,60))                   #Brush
    brushRect=Rect(945,60,25,25)
    screen.blit(sprayButton,(945,95))                   #Spray Can
    sprayRect=Rect(945,95,25,25)
    screen.blit(buckButton,(981,60))                    #Bucket
    buckRect=Rect(980,60,25,25)
    screen.blit(pickButton,(980,95))                    #Color Picker
    pickRect=Rect(980,95,25,25)
    screen.blit(lineButton,(1015,60))                   #Line 
    lineRect=Rect(1015,60,25,25)
    screen.blit(rectButton,(1015,95))                   #Rect Tool
    rectRect=Rect(1015,95,25,25)
    screen.blit(circleButton,(1050,60))                 #Circle 
    circleRect=Rect(1050,60,25,25)
    screen.blit(polyButton,(1050,95))                   #Polygon 
    polyRect=Rect(1050,95,25,25)
    screen.blit(clearButton,(1085,60))                  #Clear 
    clearRect=Rect(1085,60,25,25)
    screen.blit(stampButton,(1082,95))                  #Stamps
    stampRect=Rect(1085,95,25,25)
    screen.blit(saveButton,(1120,60))                   #Save 
    saveRect=Rect(1120,60,25,25)
    screen.blit(loadButton,(1155,60))                   #Load 
    loadRect=Rect(1155,60,25,25)
    screen.blit(undoButton,(1119,95))                   #Undo 
    undoRect=Rect(1120,95,25,25)
    screen.blit(redoButton,(1155,95))                   #Redo
    redoRect=Rect(1155,95,25,25)
    draw.rect(screen,(111,111,111),(900,572,290,208),0) #Spectrum Frame
    screen.blit(spectrum,(910,582))                     #Spectrum
    specRect=Rect(910,582,270,188)
    #Brushes
    b1Rect=Rect(910,160,25,25)
    b2Rect=Rect(945,160,25,25)
    b3Rect=Rect(980,160,25,25)
    b4Rect=Rect(1015,160,25,25)
    b5Rect=Rect(1050,160,25,25)
    b6Rect=Rect(1084,159,26,26)
    b7Rect=Rect(1120,160,25,25)
    b8Rect=Rect(1155,160,25,25)
    #Lines
    l5Rect=Rect(925,233,240,10)
    l4Rect=Rect(925,247,240,10)
    l3Rect=Rect(925,262,240,10)
    l2Rect=Rect(925,277,240,10)
    l1Rect=Rect(925,291,240,10)
    #Stamps
    icon1Rect=Rect(911,345,40,40)
    icon2Rect=Rect(987,345,40,40)
    icon3Rect=Rect(1063,345,40,40)
    icon4Rect=Rect(1139,345,40,40)
    icon5Rect=Rect(911,395,40,40)
    icon6Rect=Rect(987,395,40,40)
    icon7Rect=Rect(1063,395,40,40)
    icon8Rect=Rect(1139,395,40,40)
    icon9Rect=Rect(911,445,40,40)
    icon10Rect=Rect(987,445,40,40)
    icon11Rect=Rect(1063,445,40,40)
    icon12Rect=Rect(1139,445,40,40)
    icon13Rect=Rect(911,495,40,40)
    icon14Rect=Rect(987,495,40,40)
    icon15Rect=Rect(1063,495,40,40)
    icon16Rect=Rect(1139,495,40,40)
    #Colors
    c1Rect=Rect(800,720,25,25)
    c2Rect=Rect(825,720,25,25)
    c3Rect=Rect(800,745,25,25)
    c4Rect=Rect(825,745,25,25)
    #Size
    slideRect=Rect(763,753,14,10)
    size1Rect=Rect(670,670,90,20)
    size2Rect=Rect(670,690,90,30)
    draw.rect(screen,(255,255,255),(760,670,20,100),0)#Slider box
    draw.rect(screen,0,(769,675,2,90),0)#Slider guideline
    draw.rect(screen,(100,100,255),slideRect,0)#Slider
    draw.rect(screen,(111,111,111),size1Rect,0)#Text: "ADJUST SIZE"
    draw.rect(screen,(111,111,111),size2Rect,0)#Number: size
    #Mouse
    m1Rect=Rect(670,720,90,20)
    m2Rect=Rect(670,740,90,30)
    draw.rect(screen,(111,111,111),m1Rect,0)#Text: "MOUSE"
    draw.rect(screen,(111,111,111),m2Rect,0)#Mouse coordinates
    ################################## VARIABLES ###################################
    info=mainfont.render("ADJUST SIZE",True,(255,0,0))
    screen.blit(info,(670,675))
    info=font2.render("4",True,(255,255,255))
    screen.blit(info,(740,690))
    info=mainfont.render("MOUSE",True,(255,0,0))
    screen.blit(info,(690,725))
    infos=["Pencil: Click and hold to draw free hand lines",
           "Eraser: Click and hold to erase anything",
           "Brush: Click and hold to draw different shaped free hand lines",
           "Spray Can: Click and hold to draw with the effect of spray paint",
           """Bucket: Click to fill shapes or areas""",
           "Color Picker: Click on an object to get its color",
           """Line Tool: Click and hold to draw straight lines""",
           """Rectangle Tool: Click and hold to draw rectangles""",
           """Circle Tool: Click and hold to circles and ellipses""",
           """Polygon Tool: Click to draw a line from point to point.""",
           "Clear: Clears the canvas",
           "Stamps: Opens stamp menu","Save: Saves drawing","Load: Loads an image",
           "Undo: Takes back previous step","Redo: Takes back previous undone step"]
    addinfo=["Press Shift to toggle between horizontal or vertical lines, and free-hand lines.",
             "Shift to toggle between squares and rectangles",
             "Space to toggle between filled and unfilled",
             "Press Shift to toggle between circles and ellipses",
             "Press Enter before clicking the last point.",
             "Press the up and down arrows to adjust the stamp size"]
    info=mainfont.render(infos[0],True,(0,0,0))
    screen.blit(info,(55,675))
    draw.rect(screen,(0),(pencilRect),2)    #Indicates the default tool - pencil
    mxi=0       #mx initial
    myi=0       #my initial
    count=0     #Tracks number of points
    A_trans=50  #Alpha brush transparency
    color=0
    S_size=1.00
    shift=0
    size=4
    stamp=0
    space=0
    undo=0      #Tracks steps
    tip="circle"
    tool="pencil"
    mode = 'draw'
    alpha=False
    enter=False
    hover=False #Tracks user when hovering on a tool
    userQuit=False #When user quits, this variable becomes True
    step=screen.subsurface(canvasRect).copy()
    colors=[color]
    pixels=[]
    undos=[]    #Saves steps
    undos.append(step)
    icons=[icon1,icon2,icon3,icon4,icon5,icon6,icon7,icon8,
           icon9,icon10,icon11,icon12,icon13,icon14,icon15,icon16]
    ################################## Functions #####################################
    def buttonReset():
        pixels=[]
        count=0
        shift=0
        stamp=0
        for i in range(910,1190,35):
            draw.rect(screen,(255,255,255),(i,60,25,25),0)
            draw.rect(screen,(255,255,255),(i,95,25,25),0)
        screen.blit(pencilButton,(910,60))
        screen.blit(eraserButton,(910,95))
        screen.blit(brushButton,(948,60))
        screen.blit(sprayButton,(945,95))
        screen.blit(buckButton,(981,60))
        screen.blit(pickButton,(980,95))
        screen.blit(lineButton,(1015,60))
        screen.blit(rectButton,(1015,95))
        screen.blit(circleButton,(1050,60))
        screen.blit(polyButton,(1050,95))
        screen.blit(clearButton,(1085,60))
        screen.blit(stampButton,(1082,95))
        screen.blit(saveButton,(1120,60))
        screen.blit(loadButton,(1155,60))
        screen.blit(undoButton,(1119,95))
        screen.blit(redoButton,(1155,95))
        draw.rect(screen,(111,111,111),(900,150,290,45),0)
        draw.rect(screen,(111,111,111),(900,215,290,100),0)
        draw.rect(screen,(111,111,111),(900,335,290,215),0)

    def brush():
        for i in range(8):
            draw.rect(screen,(255,255,255),(910+(i*35),160,25,25),0)
            screen.blit(brushes[i],(910+(i*35),160))
        
    def lineWidth():
        screen.blit(lines,(910,225))
    def stamps():
        q=40
        for i in range(4):
            draw.rect(screen,(255,255,255),(911+(i*(q+36)),345,q,q),0)          #Row 1
            screen.blit(icons[i],(911+(i*(q+36)),345))
            draw.rect(screen,(255,255,255),(911+(i*(q+36)),345+(q+10),q,q),0)   #Row 2
            screen.blit(icons[i+4],(911+(i*(q+36)),345+(q+10)))
            draw.rect(screen,(255,255,255),(911+(i*(q+36)),345+(2*(q+10)),q,q),0)#Row 3
            screen.blit(icons[i+8],(911+(i*(q+36)),345+(2*(q+10))))
            draw.rect(screen,(255,255,255),(911+(i*(q+36)),345+(3*(q+10)),q,q),0)#Row 4
            screen.blit(icons[i+12],(911+(i*(q+36)),345+(3*(q+10))))
    #################################################################################
    while running:
        mx,my = mouse.get_pos()
        mb=mouse.get_pressed()
        kp=key.get_pressed()
        ############### EVENT LOOP ###############
        for evt in event.get():
            if evt.type==QUIT:
                mode = 'quit'
            if evt.type==MOUSEBUTTONDOWN:
                if evt.button==1:
                    click=True
                    if count%2==0 and canvasRect.collidepoint(mx,my) and tool=="polygon":
                        pmx1,pmy1=evt.pos
                        count+=1#Number of points
                    elif count%2==1 and canvasRect.collidepoint(mx,my) and tool=="polygon":
                        pmx2,pmy2=evt.pos
                        count+=1
                    mmx,mmy=evt.pos
                preScreen=screen.copy()
            if canvasRect.collidepoint((mx,my)):
                if evt.type==MOUSEBUTTONUP:
                    undo+=1 #Something is drawn, therefore it is added
                    step=screen.subsurface(canvasRect).copy()#to the undo list
                    undos.insert(undo,step)#.insert() b/c the sequence is not affected
                                           #if the user pressed undo/redo
            if specRect.collidepoint(mx,my) and evt.type==MOUSEBUTTONUP:
                if len(colors)<5:
                    colors.append(color)
                if len(colors)>=5:
                    del colors[0]
                    colors.append(color)
            if evt.type==KEYDOWN:
                if evt.key==K_LSHIFT:
                    shift+=1#Becomes even/odd
                if evt.key==K_SPACE:
                    space+=1#Becomes even/odd
                if evt.key==K_RETURN:
                    enter=True
                if evt.key==K_UP:
                    S_size+=0.02
                if evt.key==K_DOWN:
                    S_size-=0.02
        if mode == 'quit':
            preSave=screen.copy()
            #### ASK SAVE WINDOW ####
            text_Font=font.SysFont("Helvetica",20)
            save_Rect  =Rect(400+20, 300+60,80,20)
            nosave_Rect=Rect(400+140,300+60,80,20)
            cancel_Rect=Rect(400+300,300+60,80,20)
            ask_Font   =text_Font.render("Save changes?",True,(0,0,0))
            save_Font  =text_Font.render("Save",         True,(0,0,0))
            nosave_Font=text_Font.render("Don't save",   True,(0,0,0))
            cancel_Font=text_Font.render("Cancel",       True,(0,0,0))
            draw.rect(screen,(255,255,255),(400,300,400,100),0)
            draw.rect(screen,(  0,  0,  0),(400,300,400,100),2)
            draw.rect(screen,(80,120,255),  save_Rect,0)
            draw.rect(screen,(80,120,255),nosave_Rect,0)
            draw.rect(screen,(80,120,255),cancel_Rect,0)
            screen.blit(   ask_Font,(400+20, 300+10))
            screen.blit(  save_Font,(400+43, 300+63))
            screen.blit(nosave_Font,(400+148,300+63))
            screen.blit(cancel_Font,(400+316,300+63))
            if save_Rect.collidepoint((mx,my)):
                draw.rect(screen,(255,0,0),save_Rect,2)
                if evt.type==MOUSEBUTTONUP:
                    save    =True
                    cancel  =False
                    userQuit=False
            if nosave_Rect.collidepoint((mx,my)):
                draw.rect(screen,(255,0,0),nosave_Rect,2)
                if evt.type==MOUSEBUTTONUP:
                    save    =False
                    cancel  =False
                    userQuit=False
            if cancel_Rect.collidepoint((mx,my)):
                draw.rect(screen,(255,0,0),cancel_Rect,2)
                if evt.type==MOUSEBUTTONUP:
                    save    =False
                    cancel  =True
                    userQuit=False
            display.flip()
            if userQuit:
                break
            if not cancel:
                if save:                        
                    save1=filedialog.asksaveasfilename(defaultextension=".png")
                    file1=screen.subsurface(canvasRect).copy()
                    if save1!="":
                        image.save(file1,save1)
                running=False
            if cancel:
                screen.blit(preSave,(0,0))
                mode = 'draw'
        ############
        
        if mode == 'draw':
            ############### MOUSE COORDINATES ###############
            if canvasRect.collidepoint(mx,my):
                xy1=str(mx-50)
                xy2=str(my-50)
                mx1=font1.render(xy1,True,(255,255,255))
                mx2=font1.render(xy2,True,(255,255,255))
                mx3=font1.render("X:",True,(255,255,255))
                mx4=font1.render("Y:",True,(255,255,255))
                draw.rect(screen,(111,111,111),m2Rect,0)#Coordinates
                screen.blit(mx1,(710-mx1.get_width(),745))
                screen.blit(mx2,(755-mx2.get_width(),745))
                screen.blit(mx3,(670,745))
                screen.blit(mx4,(715,745))
            ############### COLOR BOXES ###############
            if tool=="picker":
                try:
                    draw.rect(screen,temp,(800,670,50,50),0)#Box showing current color
                except NameError:
                    temp=color
            else:
                draw.rect(screen,color,(800,670,50,50),0)#Box showing current color
            if len(colors)>=2:
                draw.rect(screen,colors[-2],c1Rect,0)
            if len(colors)>=3:
                draw.rect(screen,colors[-3],c2Rect,0)
            if len(colors)>=4:
                draw.rect(screen,colors[-4],c3Rect,0)
            if len(colors)>=5:
                draw.rect(screen,colors[-5],c4Rect,0)
            ########## BRUSH SIZE ##########
            if slideRect.collidepoint(mx,my) and mb[0]==1:
                draw.rect(screen,(255,255,255),(760,670,20,100),0)#Slider box
                draw.rect(screen,0,(769,675,2,90),0)#Slider guideline
                if my<677:
                    slideRect=Rect(slideRect[0],672,slideRect[2],slideRect[3])
                    draw.rect(screen,(100,100,255),slideRect,0)
                elif my>762:
                    slideRect=Rect(slideRect[0],757,slideRect[2],slideRect[3])
                    draw.rect(screen,(100,100,255),slideRect,0)
                else:
                    slideRect=Rect(slideRect[0],my-5,slideRect[2],slideRect[3])
                    draw.rect(screen,(100,100,255),slideRect,0)
                if slideRect[1]<=672:#Max size is 100
                    size=100
                else:
                    size=int(abs(slideRect[1]-757)/85*100)#Ratio of distance from bottom * 85
            draw.rect(screen,(111,111,111),size2Rect,0)#Box displaying size
            if size<1:
                size=1
                sizenum=font2.render(str(size),True,(255,255,255))
            else:
                sizenum=font2.render(str(size),True,(255,255,255))
            screen.blit(sizenum,(755-sizenum.get_width(),690))
            #############################
            if tool=="polygon" and canvasRect.collidepoint(mx,my):
                if mb[0]==1 and count>=2:#More than 1 point selected
                    draw.line(screen,color,(pmx1,pmy1),(pmx2,pmy2),size)
                    if enter==True:
                        count=0#Stops drawing
                        enter=False
            if pencilRect.collidepoint(mx,my) and mb[0]==1:
                stamp=0
                buttonReset()
                tool="pencil"
                draw.rect(screen,(0),(pencilRect),2)
                draw.rect(screen,(111,111,111),(50,670,600,100),0)
                info=mainfont.render(infos[0],True,(0,0,0))
                screen.blit(info,(55,675))
            if eraserRect.collidepoint(mx,my) and mb[0]==1:
                stamp=0
                buttonReset()
                tool="eraser"
                draw.rect(screen,(0),(eraserRect),2)
                draw.rect(screen,(111,111,111),(50,670,600,100),0)
                info=mainfont.render(infos[1],True,(0,0,0))
                screen.blit(info,(55,675))
            if brushRect.collidepoint(mx,my) and mb[0]==1:
                stamp=0
                buttonReset()
                tool="brush"
                default=True
                draw.rect(screen,(0),(brushRect),2)
                brush()
                draw.rect(screen,(111,111,111),(50,670,600,100),0) 
                info=mainfont.render(infos[2],True,(0,0,0))
                screen.blit(info,(55,675))
                A_text=mainfont.render("ALPHA:",True,(255,0,0))
                screen.blit(A_text,(75,725))
            if sprayRect.collidepoint(mx,my) and mb[0]==1:
                stamp=0
                buttonReset()
                tool="spray"
                draw.rect(screen,(0),(sprayRect),2)
                brush()
                draw.rect(screen,(111,111,111),(50,670,600,100),0)
                info=mainfont.render(infos[3],True,(0,0,0))
                screen.blit(info,(55,675))
            if buckRect.collidepoint(mx,my) and mb[0]==1:
                stamp=0
                buttonReset()
                tool="bucket"
                draw.rect(screen,(0),(buckRect),2)
                draw.rect(screen,(111,111,111),(50,670,600,100),0)
                info=mainfont.render(infos[4],True,(0,0,0))
                screen.blit(info,(55,675))
            if pickRect.collidepoint(mx,my) and mb[0]==1:
                stamp=0
                buttonReset()
                tool="picker"
                draw.rect(screen,(0),(pickRect),2)
                draw.rect(screen,(111,111,111),(50,670,600,100),0)
                info=mainfont.render(infos[5],True,(0,0,0))
                screen.blit(info,(55,675))
            if lineRect.collidepoint(mx,my) and mb[0]==1:
                stamp=0
                buttonReset()
                tool="line"
                draw.rect(screen,(0),(lineRect),2)
                lineWidth()
                draw.rect(screen,(111,111,111),(50,670,600,100),0)
                info=mainfont.render(infos[6],True,(0,0,0))
                screen.blit(info,(55,675))
                info=mainfont.render(addinfo[0],True,(0,0,0))
                screen.blit(info,(55,700))
            if rectRect.collidepoint(mx,my) and mb[0]==1:
                stamp=0
                buttonReset()
                tool="rect"
                draw.rect(screen,(0),(rectRect),2)
                lineWidth()
                draw.rect(screen,(111,111,111),(50,670,600,100),0)
                info=mainfont.render(infos[7],True,(0,0,0))
                screen.blit(info,(55,675))
                info=mainfont.render(addinfo[1],True,(0,0,0))
                screen.blit(info,(55,700))
                info=mainfont.render(addinfo[2],True,(0,0,0))
                screen.blit(info,(55,725))
            if circleRect.collidepoint(mx,my) and mb[0]==1:
                stamp=0
                buttonReset()
                tool="circle"
                draw.rect(screen,(0),(circleRect),2)
                lineWidth()
                draw.rect(screen,(111,111,111),(50,670,600,100),0)
                info=mainfont.render(infos[8],True,(0,0,0))
                screen.blit(info,(55,675))
                info=mainfont.render(addinfo[3],True,(0,0,0))
                screen.blit(info,(55,700))
                info=mainfont.render(addinfo[2],True,(0,0,0))
                screen.blit(info,(55,725))
            if polyRect.collidepoint(mx,my) and mb[0]==1:
                tempRect=(50,670,550,100)
                tempInfo=screen.subsurface(tempRect).copy()
                stamp=0
                buttonReset()
                tool="polygon"
                draw.rect(screen,(0),(polyRect),2)
                lineWidth()
                draw.rect(screen,(111,111,111),(50,670,600,100),0)
                info=mainfont.render(infos[9],True,(0,0,0))
                screen.blit(info,(55,675))
                info=mainfont.render(addinfo[4],True,(0,0,0))
                screen.blit(info,(55,700))
        #####################################################################
            if stampRect.collidepoint(mx,my) and mb[0]==1:
                tool="stamp"
                stamp=0
                buttonReset()
                draw.rect(screen,(0),(stampRect),2)
                stamps()
                draw.rect(screen,(111,111,111),(50,670,600,100),0)
                info=mainfont.render(infos[11],True,(0,0,0))
                screen.blit(info,(55,675))
                info=mainfont.render(addinfo[5],True,(0,0,0))
                screen.blit(info,(55,700))
                S_text1=mainfont.render("STAMP SIZE:",True,(255,0,0))
                screen.blit(S_text1,(55,725))
            if clearRect.collidepoint(mx,my):
                if not hover:
                    tempRect=(50,670,550,100)
                    tempInfo=screen.subsurface(tempRect).copy()#Copies previous text on info bar
                hover=True
                draw.rect(screen,(111,111,111),(50,670,600,100),0)
                info=mainfont.render(infos[10],True,(0,0,0))
                screen.blit(info,(55,675))
                if evt.type==MOUSEBUTTONDOWN:
                    step=screen.subsurface(canvasRect).copy()
                    undos.append(step)
                    undo+=1
                    draw.rect(screen,(0),(clearRect),2)
                    draw.rect(screen,(255,255,255),(canvasRect),0)
                if evt.type==MOUSEBUTTONUP:
                    draw.rect(screen,(255,255,255),(clearRect),0)
                    screen.blit(clearButton,(clearRect))
                    count=0
                    stamp=0
            elif saveRect.collidepoint(mx,my):
                if not hover:
                    tempRect=(50,670,550,100)
                    tempInfo=screen.subsurface(tempRect).copy()
                hover=True
                draw.rect(screen,(111,111,111),(50,670,600,100),0)
                info=mainfont.render(infos[12],True,(0,0,0))
                screen.blit(info,(55,675))
                if evt.type==MOUSEBUTTONDOWN:
                    draw.rect(screen,(0),(saveRect),2)
                    save1=tkinter.filedialog.asksaveasfilename(defaultextension=".png")
                    file1=screen.subsurface(canvasRect).copy()
                    draw.rect(screen,(255,255,255),(saveRect),0)
                    if save1!="":
                        image.save(file1,save1)
                screen.blit(saveButton,(saveRect))
            elif loadRect.collidepoint(mx,my):
                if not hover:
                    tempRect=(50,670,550,100)
                    tempInfo=screen.subsurface(tempRect).copy()
                hover=True
                draw.rect(screen,(111,111,111),(50,670,600,100),0)
                info=mainfont.render(infos[13],True,(0,0,0))
                screen.blit(info,(55,675))
                if evt.type==MOUSEBUTTONDOWN:
                    draw.rect(screen,(0),(loadRect),2)
                    load1=tkinter.filedialog.askopenfilename(filetypes=[("Images","*.png;*.jpeg;*.jpg")])
                    load2=image.load(load1)
                    screen.blit(load2,(50,50))
                    draw.rect(screen,(255,255,255),(saveRect),0)
                screen.blit(saveButton,(saveRect))
            elif undoRect.collidepoint(mx,my):
                if not hover:
                    tempRect=(50,670,550,100)
                    tempInfo=screen.subsurface(tempRect).copy()
                hover=True
                draw.rect(screen,(111,111,111),(50,670,600,100),0)
                info=mainfont.render(infos[14],True,(0,0,0))
                screen.blit(info,(55,675))
                if evt.type==MOUSEBUTTONDOWN:
                    draw.rect(screen,(0),(undoRect),2)
                    if undo<1:
                        screen.blit(undos[undo],(50,50))
                        undo=0
                    else:
                        screen.blit(undos[undo-1],(50,50))#[undo-1] b/c user wants previous step
                        undo-=1#Decreases because the current screen is one less
                    time.wait(200)
                    count==0
                if evt.type==MOUSEBUTTONUP:
                    draw.rect(screen,(255,255,255),(undoRect),0)
                    screen.blit(undoButton,(1119,95))
            elif redoRect.collidepoint(mx,my):
                if not hover:
                    tempRect=(50,670,550,100)
                    tempInfo=screen.subsurface(tempRect).copy()
                hover=True
                draw.rect(screen,(111,111,111),(50,670,600,100),0)
                info=mainfont.render(infos[15],True,(0,0,0))
                screen.blit(info,(55,675))
                if evt.type==MOUSEBUTTONDOWN:
                    draw.rect(screen,(0),(redoRect),2)
                    if undo<len(undos)-1:#if not the last position of the list
                        screen.blit(undos[undo+1],(50,50))# +1 b/c user wants next step
                        undo+=1         #List position increases
                    time.wait(200)
                    count=0
                if evt.type==MOUSEBUTTONUP:
                    draw.rect(screen,(255,255,255),(redoRect),0)
                    screen.blit(redoButton,(redoRect))
            else:
                if hover:
                    screen.blit(tempInfo,(50,670))
                hover=False
            if specRect.collidepoint(mx,my) and mb[0]==1:
                color=screen.get_at((mx,my))
        ############################################################################
            if tool=='brush' or tool=='spray':
                if b1Rect.collidepoint(mx,my) and mb[0]==1:
                    brush()
                    draw.rect(screen,0,b1Rect,2)
                    tip="circle"
                    size=4
                    slideRect=Rect(slideRect[0],753,slideRect[2],slideRect[3])
                    draw.rect(screen,(255,255,255),(760,670,20,100),0)
                    draw.rect(screen,0,(769,675,2,90),0)
                    draw.rect(screen,(100,100,255),slideRect,0)
                if b2Rect.collidepoint(mx,my) and mb[0]==1:
                    brush()
                    draw.rect(screen,0,b2Rect,2)
                    tip="circle"
                    size=8
                    slideRect=Rect(slideRect[0],750,slideRect[2],slideRect[3])
                    draw.rect(screen,(255,255,255),(760,670,20,100),0)
                    draw.rect(screen,0,(769,675,2,90),0)
                    draw.rect(screen,(100,100,255),slideRect,0)
                if b3Rect.collidepoint(mx,my) and mb[0]==1:
                    brush()
                    draw.rect(screen,0,b3Rect,2)
                    tip="circle"
                    size=12
                    slideRect=Rect(slideRect[0],747,slideRect[2],slideRect[3])
                    draw.rect(screen,(255,255,255),(760,670,20,100),0)
                    draw.rect(screen,0,(769,675,2,90),0)
                    draw.rect(screen,(100,100,255),slideRect,0)
                if b4Rect.collidepoint(mx,my) and mb[0]==1:
                    brush()
                    draw.rect(screen,0,b4Rect,2)
                    tip="square"
                    size=4
                    slideRect=Rect(slideRect[0],753,slideRect[2],slideRect[3])
                    draw.rect(screen,(255,255,255),(760,670,20,100),0)
                    draw.rect(screen,0,(769,675,2,90),0)
                    draw.rect(screen,(100,100,255),slideRect,0)
                if b5Rect.collidepoint(mx,my) and mb[0]==1:
                    brush()
                    draw.rect(screen,0,b5Rect,2)
                    tip="square"
                    size=8
                    slideRect=Rect(slideRect[0],750,slideRect[2],slideRect[3])
                    draw.rect(screen,(255,255,255),(760,670,20,100),0)
                    draw.rect(screen,0,(769,675,2,90),0)
                    draw.rect(screen,(100,100,255),slideRect,0)
                if b6Rect.collidepoint(mx,my) and mb[0]==1:
                    brush()
                    draw.rect(screen,0,b6Rect,2)
                    tip="square"
                    size=12
                    slideRect=Rect(slideRect[0],747,slideRect[2],slideRect[3])
                    draw.rect(screen,(255,255,255),(760,670,20,100),0)
                    draw.rect(screen,0,(769,675,2,90),0)
                    draw.rect(screen,(100,100,255),slideRect,0)
                if b7Rect.collidepoint(mx,my) and mb[0]==1:
                    brush()
                    draw.rect(screen,0,b7Rect,2)
                    tip="diag1"
                if b8Rect.collidepoint(mx,my) and mb[0]==1:
                    brush()
                    draw.rect(screen,0,b8Rect,2)
                    tip="diag2"
            if tool=='line' or tool=='circle' or tool=='rect' or tool=='polygon':
                if l1Rect.collidepoint(mx,my) and mb[0]==1:
                    lineWidth()
                    draw.rect(screen,0,(l1Rect),1)
                    size=1
                    slideRect=Rect(slideRect[0],756,slideRect[2],slideRect[3])
                    draw.rect(screen,(255,255,255),(760,670,20,100),0)
                    draw.rect(screen,0,(769,675,2,90),0)
                    draw.rect(screen,(100,100,255),slideRect,0)
                if l2Rect.collidepoint(mx,my) and mb[0]==1:
                    lineWidth()
                    draw.rect(screen,0,(l2Rect),1)
                    size=2
                    slideRect=Rect(slideRect[0],755,slideRect[2],slideRect[3])
                    draw.rect(screen,(255,255,255),(760,670,20,100),0)
                    draw.rect(screen,0,(769,675,2,90),0)
                    draw.rect(screen,(100,100,255),slideRect,0)
                if l3Rect.collidepoint(mx,my) and mb[0]==1:
                    lineWidth()
                    draw.rect(screen,0,(l3Rect),1)
                    size=4
                    slideRect=Rect(slideRect[0],754,slideRect[2],slideRect[3])
                    draw.rect(screen,(255,255,255),(760,670,20,100),0)
                    draw.rect(screen,0,(769,675,2,90),0)
                    draw.rect(screen,(100,100,255),slideRect,0)
                if l4Rect.collidepoint(mx,my) and mb[0]==1:
                    lineWidth()
                    draw.rect(screen,0,(l4Rect),1)
                    size=6
                    slideRect=Rect(slideRect[0],752,slideRect[2],slideRect[3])
                    draw.rect(screen,(255,255,255),(760,670,20,100),0)
                    draw.rect(screen,0,(769,675,2,90),0)
                    draw.rect(screen,(100,100,255),slideRect,0)
                if l5Rect.collidepoint(mx,my) and mb[0]==1:
                    lineWidth()
                    draw.rect(screen,0,(l5Rect),1)
                    size=8
                    slideRect=Rect(slideRect[0],750,slideRect[2],slideRect[3])
                    draw.rect(screen,(255,255,255),(760,670,20,100),0)
                    draw.rect(screen,0,(769,675,2,90),0)
                    draw.rect(screen,(100,100,255),slideRect,0)
            if tool=='stamp':
                if icon1Rect.collidepoint((mx,my)) and mb[0]==1:
                    stamps()
                    draw.rect(screen,0,(icon1Rect),2)
                    stamp=1
                if icon2Rect.collidepoint((mx,my)) and mb[0]==1:
                    stamps()
                    draw.rect(screen,0,(icon2Rect),2)
                    stamp=2
                if icon3Rect.collidepoint((mx,my)) and mb[0]==1:
                    stamps()
                    draw.rect(screen,0,(icon3Rect),2)
                    stamp=3
                if icon4Rect.collidepoint((mx,my)) and mb[0]==1:
                    stamps()
                    draw.rect(screen,0,(icon4Rect),2)
                    stamp=4
                if icon5Rect.collidepoint((mx,my)) and mb[0]==1:
                    stamps()
                    draw.rect(screen,0,(icon5Rect),2)
                    stamp=5
                if icon6Rect.collidepoint((mx,my)) and mb[0]==1:
                    stamps()
                    draw.rect(screen,0,(icon6Rect),2)
                    stamp=6
                if icon7Rect.collidepoint((mx,my)) and mb[0]==1:
                    stamps()
                    draw.rect(screen,0,(icon7Rect),2)
                    stamp=7
                if icon8Rect.collidepoint((mx,my)) and mb[0]==1:
                    stamps()
                    draw.rect(screen,0,(icon8Rect),2)
                    stamp=8
                if icon9Rect.collidepoint((mx,my)) and mb[0]==1:
                    stamps()
                    draw.rect(screen,0,(icon9Rect),2)
                    stamp=9
                if icon10Rect.collidepoint((mx,my)) and mb[0]==1:
                    stamps()
                    draw.rect(screen,0,(icon10Rect),2)
                    stamp=10
                if icon11Rect.collidepoint((mx,my)) and mb[0]==1:
                    stamps()
                    draw.rect(screen,0,(icon11Rect),2)
                    stamp=11
                if icon12Rect.collidepoint((mx,my)) and mb[0]==1:
                    stamps()
                    draw.rect(screen,0,(icon12Rect),2)
                    stamp=12
                if icon13Rect.collidepoint((mx,my)) and mb[0]==1:
                    stamps()
                    draw.rect(screen,0,(icon13Rect),2)
                    stamp=13
                if icon14Rect.collidepoint((mx,my)) and mb[0]==1:
                    stamps()
                    draw.rect(screen,0,(icon14Rect),2)
                    stamp=14
                if icon15Rect.collidepoint((mx,my)) and mb[0]==1:
                    stamps()
                    draw.rect(screen,0,(icon15Rect),2)
                    stamp=15
                if icon16Rect.collidepoint((mx,my)) and mb[0]==1:
                    stamps()
                    draw.rect(screen,0,(icon16Rect),2)
                    stamp=16
        ########################################################################################
            if S_size<=0.10:
                S_size=0.10
            if S_size>=2.50:
                S_size=2.50
            if tool=="stamp" and not hover:
                S_text_size=str(str(int(S_size*100))+"%")
                S_text2=mainfont.render(S_text_size,True,(255,255,255))
                draw.rect(screen,(111,111,111),(54,749,50,20),0)
                screen.blit(S_text2,(55,750))
            if tool=="brush" and not hover:
                A_rect=Rect(80,745,40,15)
                draw.rect(screen,(255,255,255),A_rect,0)
                A_on=mainfont.render("ON",True,(0,255,0))
                A_off=mainfont.render("OFF",True,(255,0,0))
                if alpha:
                    screen.blit(A_on,(89,746))
                elif not alpha:
                    screen.blit(A_off,(86,746))
                if A_rect.collidepoint(mx,my):
                    draw.rect(screen,(255,0,0),A_rect,1)
                    if evt.type==MOUSEBUTTONDOWN:
                        if alpha:
                            alpha=False
                        elif not alpha:
                            alpha=True
                        time.wait(150)
                if default:
                    draw.rect(screen,(255,255,255),(150,743,110,20),0)#Box
                    draw.rect(screen,0,(155,752,100,2),0)#Guide line
                    A_slider=Rect(172,745,10,16)
                    draw.rect(screen,(255,111,111),A_slider,0)
                    default=False
                if A_slider.collidepoint(mx,my) and mb[0]==1:
                    draw.rect(screen,(255,255,255),(150,743,110,20),0)
                    draw.rect(screen,0,(155,752,100,2),0)
                    A_slider=Rect(mx-5,A_slider[1],A_slider[2],A_slider[3])
                    if A_slider[0]<=150:
                        A_slider=Rect(150,A_slider[1],A_slider[2],A_slider[3])
                        draw.rect(screen,(255,111,111),A_slider,0)
                    if A_slider[0]>=250:
                        A_slider=Rect(250,A_slider[1],A_slider[2],A_slider[3])
                        draw.rect(screen,(255,111,111),A_slider,0)
                    else:
                        draw.rect(screen,(255,111,111),A_slider,0)
                    A_trans=int(((A_slider[0]-150)/100)*255)
                A_text1=mainfont.render("TRANSPARENCY:",True,(0,0,255))
                A_text2=mainfont.render(str(A_trans),True,(255,255,255))
                draw.rect(screen,(111,111,111),(149,724,150,16),0)
                screen.blit(A_text1,(150,725))
                screen.blit(A_text2,(160+A_text1.get_width(),725))
            if canvasRect.collidepoint(mx,my):
                screen.set_clip(canvasRect)
                if tool=="pencil" and mb[0]==1:
                    draw.line(screen,color,(mx,my),(mxi,myi),1)
                if tool=="eraser" and mb[0]==1:
                    draw.rect(screen,(255,255,255),(mx-10,my-10,20,20),0)
                    dx=mx-mxi
                    dy=my-myi
                    dist=int(hypot(dx,dy))
                    for i in range(dist):
                        draw.rect(screen,(255,255,255),
                                  ((i*dx//dist)+mxi-10,(i*dy//dist)+myi-10,20,20),0)
                        #Draws rect every point b/w the 2 mouse points
                if tool=="brush" and alpha:
                    A_brush=Surface((size,size)).convert()
                    A_brush.set_alpha(A_trans)
                    if color==0:
                        A_brush.set_colorkey(16581375)
                        A_brush.fill(16581375)
                    else:
                        A_brush.set_colorkey(0)
                        A_brush.fill(0)
                    if mb[0]==1:
                        if tip=="circle":
                            draw.circle(A_brush,color,(size//2,size//2),size//2)
                            screen.blit(A_brush,(mx-size//2,my-size//2))
                        if tip=="square":
                            draw.rect(A_brush,color,(0,0,size,size),0)
                            screen.blit(A_brush,(mx-size//2,my-size//2))
                        if tip=="diag1":
                            draw.line(A_brush,color,(0,size),(size,0),1)
                            screen.blit(A_brush,(mx-size//2,my-size//2))
                        if tip=="diag2":
                            draw.line(screen,color,(size,0),(0,size),1)
                            screen.blit(A_brush,(mx-size//2,my-size//2))
                if tool=="brush" and mb[0]==1 and not alpha:
                    if tip=="circle":
                        draw.circle(screen,color,(mx,my),size//2)
                        dx=mx-mxi
                        dy=my-myi
                        dist=int(hypot(dx,dy))
                        for i in range(dist):
                            draw.circle(screen,color,((i*dx//dist)+mxi,i*dy//dist+myi),size//2)
                            #Draws cirlce b/w points
                    if tip=="square":
                        draw.rect(screen,color,(mx-size//2,my-size//2,size,size),0)
                        dx=mx-mxi
                        dy=my-myi
                        dist=int(hypot(dx,dy))
                        for i in range(dist):
                            draw.rect(screen,color,((i*dx//dist)+mxi-(size//2),
                                                    (i*dy//dist)+myi-(size//2),size,size),0)
                    if tip=="diag1":
                        draw.line(screen,color,(mx-(size//2),
                                                my+(size//2)),(mx+(size//2),my-(size//2)),1)
                        dx=mx-mxi
                        dy=my-myi
                        dist=int(hypot(dx,dy))
                        for i in range(dist):
                            draw.line(screen,color,
                                      ((i*dx//dist)+mxi-(size//2),(i*dy//dist)+myi+(size//2)),
                                  ((i*dx//dist)+mxi+(size//2),(i*dy//dist)+myi-(size//2)),2)
                            #Draws line b/w points
                    if tip=="diag2":
                        draw.line(screen,color,
                                  (mx-(size//2),my-(size//2)),(mx+(size//2),my+(size//2)),1)
                        dx=mx-mxi
                        dy=my-myi
                        dist=int(hypot(dx,dy))
                        for i in range(dist):
                            draw.line(screen,color,((i*dx//dist)+mxi-(size//2)
                                                    ,(i*dy//dist)+myi-(size//2)),
                                  ((i*dx//dist)+mxi+(size//2),(i*dy//dist)+myi+(size//2)),2)
                if tool=="spray" and mb[0]==1:
                    burst=size*2
                    if tip=="circle":
                        for i in range(size**2):
                            sx=randint(mx-burst,mx+burst)#Random point within burst radius
                            sy=randint(my-burst,my+burst)
                            if hypot(mx-sx,my-sy)>burst:#If outside circle don't draw
                                continue
                            else:
                                draw.rect(screen,color,(sx,sy,1,1),1)
                    if tip=="square":
                        for i in range(**2):
                            sx=randint(mx-burst,mx+burst)
                            sy=randint(my-burst,my+burst)
                            draw.rect(screen,color,(sx,sy,1,1),1)
                if tool=="bucket":
                    if evt.type==MOUSEBUTTONUP:
                        pixels=[(mmx,mmy)]
                        oldColor=screen.get_at((mmx,mmy))
                        if oldColor!=color:
                            while len(pixels)>0:
                                if screen.get_at(pixels[0])==oldColor:
                                    screen.set_at(pixels[0],color)
                                    x1=(pixels[0][0]+1,pixels[0][1])#Right
                                    x2=(pixels[0][0]-1,pixels[0][1])#Left
                                    y1=(pixels[0][0],pixels[0][1]+1)#Down
                                    y2=(pixels[0][0],pixels[0][1]-1)#Up
                                    if screen.get_at(x1)==oldColor:
                                        pixels.append(x1)
                                    if screen.get_at(x2)==oldColor:
                                        pixels.append(x2)
                                    if screen.get_at(y1)==oldColor:
                                        pixels.append(y1)
                                    if screen.get_at(y2)==oldColor:
                                        pixels.append(y2)
                                del pixels[0]
                        del pixels
                if tool=="picker":
                    if mb[0]==1:
                        temp=screen.get_at((mx,my))
                    if evt.type==MOUSEBUTTONUP:#Only adds color when mouse is released
                        color=screen.get_at((mx,my))
                        if len(colors)<5:
                            colors.append(color)
                        elif len(color)==5:
                            del colors[0]
                            colors.append(color)
                if tool=="line" and mb[0]==1:
                    screen.blit(preScreen,(0,0))
                    if shift%2==1:#Checks even/odd (see evt.get() loop)
                        if abs(mmx-mx)>abs(mmy-my):#If mx,my is more horizontal
                            draw.line(screen,color,(mmx,mmy),(mx,mmy),size)#Horizontal line
                        elif abs(mmx-mx)<abs(mmy-my):#If mx,my is more vertical
                            draw.line(screen,color,(mmx,mmy),(mmx,my),size)#Vertical line
                    if shift%2==0:
                        draw.line(screen,color,(mmx,mmy),(mx,my),size)
                if tool=="rect" and mb[0]==1:
                    screen.blit(preScreen,(0,0))
                    if space%2==1:#Filled rect
                        if shift%2==0:#Rect
                            draw.rect(screen,color,(mmx,mmy,mx-mmx,my-mmy),0)
                        if shift%2==1:#Square
                            w=mx-mmx#horizontal distance from click point
                            h=my-mmy
                            if (w>1 and h>1) or (w<1 and h<1):#If quandrant I or III
                                draw.rect(screen,color,(mmx,mmy,w,w),0)
                            if (w<1 and h>1) or (w>1 and h<1):#If quandrant II or IV
                                draw.rect(screen,color,(mmx,mmy,w,-w),0)
                    if space%2==0:#Unfilled rect
                        if shift%2==0:
                            draw.rect(screen,color,(mmx,mmy,mx-mmx,my-mmy),size)
                        if shift%2==1:
                            w=mx-mmx
                            h=my-mmy
                            if (w>1 and h>1) or (w<1 and h<1):
                                draw.rect(screen,color,(mmx,mmy,w,w),size)
                            if (w<1 and h>1) or (w>1 and h<1):
                                draw.rect(screen,color,(mmx,mmy,w,-w),size)
                if tool=="circle" and mb[0]==1:
                    screen.blit(preScreen,(0,0))
                    if space%2==1:#Filled
                        w=mx-mmx
                        h=my-mmy
                        if shift%2==1:#Circle
                            try:
                                if (w>1 and h>1) or (w<1 and h<1):#Checks quadrant
                                    elip=Rect(mmx,mmy,w,w)
                                    elip.normalize()
                                if (w<1 and h>1) or (w>1 and h<1):
                                    elip=Rect(mmx,mmy,w,-w)
                                    elip.normalize()
                                draw.ellipse(screen,color,elip,0)
                            except ValueError:
                                pass
                        if shift%2==0:#Ellipse
                            try:
                                elip=Rect(mmx,mmy,w,h)
                                elip.normalize()
                                draw.ellipse(screen,color,elip,0)
                            except ValueError:
                                pass
                    if space%2==0:#Unfilled
                        w=mx-mmx
                        h=my-mmy
                        if shift%2==1:
                            try:
                                if (w>1 and h>1) or (w<1 and h<1):
                                    elip=Rect(mmx,mmy,w,w)
                                    elip.normalize()
                                if (w<1 and h>1) or (w>1 and h<1):
                                    elip=Rect(mmx,mmy,w,-w)
                                    elip.normalize()
                                draw.ellipse(screen,color,elip,size)
                            except ValueError:
                                pass
                        if shift%2==0:
                            try:
                                elip=Rect(mmx,mmy,w,h)
                                elip.normalize()
                                draw.ellipse(screen,color,elip,size)
                            except ValueError:
                                pass
                if tool=="stamp" and stamp==1 and mb[0]==1:
                    S_stick1=transform.scale(stick1,(int(200*S_size),int(75*S_size)))
                    screen.blit(preScreen,(0,0))
                    screen.blit(S_stick1,(mx-S_stick1.get_width()//2,my-S_stick1.get_height()//2))
                if tool=="stamp" and stamp==2 and mb[0]==1:
                    S_stick2=transform.scale(stick2,(int(200*S_size),int(88*S_size)))
                    screen.blit(preScreen,(0,0))
                    screen.blit(S_stick2,(mx-S_stick2.get_width()//2,my-S_stick2.get_height()//2))
                if tool=="stamp" and stamp==3 and mb[0]==1:
                    S_stick3=transform.scale(stick3,(int(200*S_size),int(156*S_size)))
                    screen.blit(preScreen,(0,0))
                    screen.blit(S_stick3,(mx-S_stick3.get_width()//2,my-S_stick3.get_height()//2))
                if tool=="stamp" and stamp==4 and mb[0]==1:
                    S_stick4=transform.scale(stick4,(int(200*S_size),int(82*S_size)))
                    screen.blit(preScreen,(0,0))
                    screen.blit(S_stick4,(mx-S_stick4.get_width()//2,my-S_stick4.get_height()//2))
                if tool=="stamp" and stamp==5 and mb[0]==1:
                    S_stick5=transform.scale(stick5,(int(200*S_size),int(89*S_size)))
                    screen.blit(preScreen,(0,0))
                    screen.blit(S_stick5,(mx-S_stick5.get_width()//2,my-S_stick5.get_height()//2))
                if tool=="stamp" and stamp==6 and mb[0]==1:
                    S_stick6=transform.scale(stick6,(int(200*S_size),int(100*S_size)))
                    screen.blit(preScreen,(0,0))
                    screen.blit(S_stick6,(mx-S_stick6.get_width()//2,my-S_stick6.get_height()//2))
                if tool=="stamp" and stamp==7 and mb[0]==1:
                    S_stick7=transform.scale(stick7,(int(200*S_size),int(200*S_size)))
                    screen.blit(preScreen,(0,0))
                    screen.blit(S_stick7,(mx-S_stick7.get_width()//2,my-S_stick7.get_height()//2))
                if tool=="stamp" and stamp==8 and mb[0]==1:
                    S_stick8=transform.scale(stick8,(int(200*S_size),int(191*S_size)))
                    screen.blit(preScreen,(0,0))
                    screen.blit(S_stick8,(mx-S_stick8.get_width()//2,my-S_stick8.get_height()//2))
                if tool=="stamp" and stamp==9 and mb[0]==1:
                    S_stick9=transform.scale(stick9,(int(200*S_size),int(129*S_size)))
                    screen.blit(preScreen,(0,0))
                    screen.blit(S_stick9,(mx-S_stick9.get_width()//2,my-S_stick9.get_height()//2))
                if tool=="stamp" and stamp==10 and mb[0]==1:
                    S_stick10=transform.scale(stick10,(int(200*S_size),int(420*S_size)))
                    screen.blit(preScreen,(0,0))
                    screen.blit(S_stick10,(mx-S_stick10.get_width()//2,my-S_stick10.get_height()//2))
                if tool=="stamp" and stamp==11 and mb[0]==1:
                    S_stick11=transform.scale(stick11,(int(200*S_size),int(154*S_size)))
                    screen.blit(preScreen,(0,0))
                    screen.blit(S_stick11,(mx-S_stick11.get_width()//2,my-S_stick11.get_height()//2))
                if tool=="stamp" and stamp==12 and mb[0]==1:
                    S_stick12=transform.scale(stick12,(int(305*S_size),int(200*S_size)))
                    screen.blit(preScreen,(0,0))
                    screen.blit(S_stick12,(mx-S_stick12.get_width()//2,my-S_stick12.get_height()//2))
                if tool=="stamp" and stamp==13 and mb[0]==1:
                    S_stick13=transform.scale(stick13,(int(200*S_size),int(234*S_size)))
                    screen.blit(preScreen,(0,0))
                    screen.blit(S_stick13,(mx-S_stick13.get_width()//2,my-S_stick13.get_height()//2))
                if tool=="stamp" and stamp==14 and mb[0]==1:
                    S_stick14=transform.scale(stick14,(int(200*S_size),int(216*S_size)))
                    screen.blit(preScreen,(0,0))
                    screen.blit(S_stick14,(mx-S_stick14.get_width()//2,my-S_stick14.get_height()//2))
                if tool=="stamp" and stamp==15 and mb[0]==1:
                    S_stick15=transform.scale(stick15,(int(200*S_size),int(330*S_size)))
                    screen.blit(preScreen,(0,0))
                    screen.blit(S_stick15,(mx-S_stick15.get_width()//2,my-S_stick15.get_height()//2))
                if tool=="stamp" and stamp==16 and mb[0]==1:
                    S_stick16=transform.scale(stick16,(int(200*S_size),int(267*S_size)))
                    screen.blit(preScreen,(0,0))
                    screen.blit(S_stick16,(mx-S_stick16.get_width()//2,my-S_stick16.get_height()//2))
            mxi=mx
            myi=my
            screen.set_clip(None)
        ##################################################################################
            display.flip()
        quit()

