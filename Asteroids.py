# import the pygame module, so you can use it
import pygame
from pygame.locals import *

import numpy as np
# define a main function
def main():
     
    # initialize the pygame module
    pygame.init()
    # Caption
    
    pygame.display.set_caption("Asteroids")
     
    # create a surface on screen
    size=(800,600)
    screen = pygame.display.set_mode(size)
    
    # colors
    black=(0,0,0)
    white=(255,255,255)
    weirdcolor=(145,50,69)
    green=(0,255,56)
    red=(255,5,50)
    # define a variable to control the main loop
    running = False
    loser=False
    # make the ship
    Ship=pygame.image.load("Ship.png")
    # create different orientations for the ship (left, right, up, down)
    Shipdown=pygame.transform.rotate(Ship,90)
    Shipup=pygame.transform.rotate(Ship,-90)
    Shipright=pygame.transform.rotate(Ship,180)
    Shipa=Ship
    # initial ship coordinates and ship speed
    x,y=400,300
    speed=0.65
    # make the bullet
    Bolt=pygame.image.load("Bolt.png")
    Bolt2=pygame.transform.rotate(Bolt,90)
    # variable to determine the orientation of the ship when the bullet is fired
    which=0
    # set to hold the data for each bullet
    bullets=[]
    # create the asteroids
    Asteroid=pygame.image.load("AsteroidLarge.png")
    spawnspeed=300 # controls how fast the asteroids spawn
    asteroids=[] # empty set to hold data for each asteroid
    # parameters to determine how fast asteroids spawn
    asteroidcounter=0
    asteroidcounterspeed=1
    # text on screen
    message='Score: '
    messagenew=message
    # define different text sizes
    font=pygame.font.Font('freesansbold.ttf',32)
    font2=pygame.font.Font('freesansbold.ttf',24)
    font3=pygame.font.Font('freesansbold.ttf',16)
    font4=pygame.font.Font('freesansbold.ttf',48)
    score=0
    # title screen
    titlescreen=True
    while titlescreen:
        screen.fill(black) # make a black screen
        # create title
        titletext=font4.render('ASTEROIDS',True,red)
        titletextRect=titletext.get_rect()
        titletextRect.center=(400,200)
        screen.blit(titletext,titletextRect)
        # create instructions on how to start the game
        instructions=font2.render('Press ENTER to play, or ESCAPE to quit!',True,white)
        instructionsRect=instructions.get_rect()
        instructionsRect.center=(400,300)
        screen.blit(instructions,instructionsRect)
        # create instructions for how to play the game
        helptext=font3.render('Use WASD to move, the arrow keys to turn, and SPACEBAR to shoot!',True,white)
        helptextRect=helptext.get_rect()
        helptextRect.center=(400,500)
        screen.blit(helptext,helptextRect)
        pygame.display.flip() # display the text
        # take keyboard inputs and determine whether to quit or start the game
        for event in pygame.event.get():
            if event.type==KEYDOWN:
                if event.key==K_ESCAPE:
                    titlescreen=False
                elif event.key==K_RETURN:
                    titlescreen=False
                    running=True
    # main loop
    while running:
        # counter to determine when to spawn an asteroid
        asteroidcounter=asteroidcounter+asteroidcounterspeed
        # when it is time to spawn an asteroid, give it a random side and speed (e.g. left side)
        if asteroidcounter>=spawnspeed:
            side=np.random.randint(1,5)
            direction=np.random.randint(1,5)
            speedx=np.random.uniform(0.1,0.5)
            speedy=np.random.uniform(0.1,0.5)
            if side==1:
                asteroids.append([0,np.random.randint(600),direction,speedx,speedy])
            elif side==2:
                asteroids.append([np.random.randint(800),0,direction,speedx,speedy])
            elif side==3:
                asteroids.append([750,np.random.randint(600),direction,speedx,speedy])
            elif side==4:
                asteroids.append([np.random.randint(800),550,direction,speedx,speedy])
            asteroidcounter=0 # reset the counter
        # allow user to move the ship by holding down WASD
        keys=pygame.key.get_pressed()
        if keys[K_w]:
            y=y-speed
        elif keys[K_s]:
            y=y+speed
        elif keys[K_a]:
            x=x-speed
        elif keys[K_d]:
            x=x+speed
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
            # allow user to turn if using arrow keys, shoot by pressing space, or quit by pressing escape
            elif event.type==KEYDOWN:
                if event.key==K_ESCAPE:
                    running=False
                elif event.key==K_UP:
                    Shipa=Shipup
                    which=2 # which is the variable that describes the direction of the ship
                elif event.key==K_DOWN:
                    Shipa=Shipdown
                    which=3
                elif event.key==K_RIGHT:
                    Shipa=Shipright
                    which=1
                elif event.key==K_LEFT:
                    Shipa=Ship
                    which=0
                elif event.key==K_SPACE:
                    # determine which way the bullet should be oriented based on the direction of the ship
                    if which==0:
                        bullets.append([x,y+26,which])
                    elif which==1:
                        bullets.append([x+36,y+26,which])
                    elif which==2:
                        bullets.append([x+26,y,which])
                    elif which==3:
                        bullets.append([x+26,y+36,which])
        screen.fill(weirdcolor) # fill the screen with a red color as the background
        # display the score
        text=font.render(messagenew,True,white)
        textRect=text.get_rect()
        textRect.center=(85,18)
        screen.blit(text,textRect)
        # display the ship at position x,y (x and y are changed by pressing WASD)
        screen.blit(Shipa,(x,y))
        # change the position of each asteroid based off its original randomly generated parameters
        if len(asteroids)>0:
            for i in range(len(asteroids)):
                if asteroids[i][2]==1:
                    asteroids[i][0]=asteroids[i][0]-asteroids[i][3]
                    asteroids[i][1]=asteroids[i][1]-asteroids[i][4]
                    screen.blit(Asteroid,(asteroids[i][0],asteroids[i][1]))
                elif asteroids[i][2]==2:
                    asteroids[i][0]=asteroids[i][0]+asteroids[i][3]
                    asteroids[i][1]=asteroids[i][1]+asteroids[i][4]
                    screen.blit(Asteroid,(asteroids[i][0],asteroids[i][1]))
                elif asteroids[i][2]==3:
                    asteroids[i][1]=asteroids[i][1]-asteroids[i][4]
                    asteroids[i][0]=asteroids[i][0]+asteroids[i][3]
                    screen.blit(Asteroid,(asteroids[i][0],asteroids[i][1]))
                elif asteroids[i][2]==4:
                    asteroids[i][1]=asteroids[i][1]+asteroids[i][4]
                    asteroids[i][0]=asteroids[i][0]-asteroids[i][3]
                    screen.blit(Asteroid,(asteroids[i][0],asteroids[i][1]))
        i=0
        j=0
        looplength=len(bullets)
        looplength2=len(asteroids)
        # change the position of each bullet based on the original ship orientation
        while i<looplength:
                if bullets[i][2]==0:
                    bullets[i][0]=bullets[i][0]-1
                    screen.blit(Bolt,(bullets[i][0],bullets[i][1]))
                elif bullets[i][2]==2:
                    bullets[i][1]=bullets[i][1]-1
                    screen.blit(Bolt2,(bullets[i][0],bullets[i][1]))
                elif bullets[i][2]==3:
                    bullets[i][1]=bullets[i][1]+1
                    screen.blit(Bolt2,(bullets[i][0],bullets[i][1]))
                elif bullets[i][2]==1:
                    bullets[i][0]=bullets[i][0]+1
                    screen.blit(Bolt,(bullets[i][0],bullets[i][1]))
                j=0
                looplength2=len(asteroids)
                # check to see if a bullet has hit an asteroid
                while j<looplength2:
                    if abs(bullets[i][0]-(asteroids[j][0]+20))<20 and abs(bullets[i][1]-(asteroids[j][1]+20))<20:
                        del asteroids[j] # Destroy an asteroid if it is hit by a bullet
                        score=score+1 # Score goes up with every asteroid destroyed this way
                    j=j+1
                    looplength2=len(asteroids)
                i=i+1
                looplength=len(bullets)
        # get rid of any bullets that are outside the range of the screen
        looplength=len(bullets)
        i=0
        while i<looplength:
            if bullets[i][0]>800 or bullets[i][0]<0 or bullets[i][1]>600 or bullets[i][1]<0:
                del bullets[i]
            i=i+1
            looplength=len(bullets)
        # get rid of any asteroids that are outside the range of the screen
        looplength=len(asteroids)
        i=0
        while i<looplength:
            if asteroids[i][0]>800 or asteroids[i][0]<0 or asteroids[i][1]>600 or asteroids[i][1]<0:
                del asteroids[i]
            i=i+1
            looplength=len(asteroids)
        # change the displayed score based on how many asteroids have been destroyed
        scorestr=str(score)
        messagenew=message+scorestr
        # check to see if the user's ship has been hit by an asteroid
        for j in range(len(asteroids)):
            if abs(x-(asteroids[j][0]))<20 and abs(y-(asteroids[j][1]))<20:
                loser=True
        # if the user is hit, go to an end screen:
        while loser:
            screen.fill(black) # black screen
            # Let the user know that they lost
            endtext=font4.render('You lost!',True,white)
            endtextRect=endtext.get_rect()
            endtextRect.center=(400,200)
            screen.blit(endtext,endtextRect)
            # display the user's final score
            finalscore=font.render(messagenew,True,green)
            finalscoreRect=finalscore.get_rect()
            finalscoreRect.center=(400,250)
            screen.blit(finalscore,finalscoreRect)
            # provide text instructions on how to quit the game or play again
            helptext=font2.render('Hit ESACPE to quit, or hit ENTER to play again!',True,white)
            helptextRect=helptext.get_rect()
            helptextRect.center=(400,300)
            screen.blit(helptext,helptextRect)
            pygame.display.flip()
            # quit the game or restart based on user key inputs
            for event in pygame.event.get():
                if event.type==KEYDOWN:
                    if event.key==K_ESCAPE: # quit the game if the user hits ESCAPE
                        loser=False
                        running=False
                    elif event.key==K_RETURN: # restart the game if ENTER is hit; reset all the variables
                        loser=False
                        Shipa=Ship
                        x,y=400,300
                        which=0
                        bullets=[]
                        asteroids=[]
                        asteroidcounter=0
                        asteroidcounterspeed=1
                        message='Score: '
                        messagenew=message
                        font=pygame.font.Font('freesansbold.ttf',32)
                        text=font.render(messagenew,True,white)
                        textRect=text.get_rect()
                        textRect.center=(51,18)
                        score=0
        asteroidcounterspeed=asteroidcounterspeed+0.0001 # increase the speed at which asteroids spawn over time
        pygame.display.flip() # the command that actually displays all the text, the ship, asteroids, etc.
        
# run the main function only if this module is executed as the main script
if __name__=="__main__":
    # call the main function
    main()
    
    pygame.quit()