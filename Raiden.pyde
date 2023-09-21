def setup():
    global RaidenX, RaidenY, RaidenW, RaidenH
    global EnemyX, EnemyY, EnemyW, EnemyH
    global missileX, missileY, missileW, missileH
    global bgY
    global bg, Explosion
    global Raiden, Enemy, missile
    global stageNum, EnemyNum
    global dx, dy, missileVelocity
    global fireOn, enemyGone
    global explosionX, explosionY, explosionW, explosionH
    global score
    global Boss, BossX, BossY, BossW, BossH
    global bx, by
    global startTime
    
    size(1000,1000)
    
    bg = loadImage("space.jpg")
    Raiden = loadImage("Raiden.png")
    missile = loadImage("missile.png")
    Explosion = loadImage("explosion.png")
    Boss = loadImage("boss.png")

    BossW = 250
    BossH = 300
    BossX = random(0, width - BossW)
    BossY = random(0, height - BossH)
    
    missileX = -100
    missileY = -100
    missileW = 20
    missileH = 65
    missileVelocity = 100
    
    RaidenW = 80
    RaidenH = 120
    RaidenX = 460
    RaidenY = 500
    
    Enemy = []
    EnemyX = []
    EnemyY = []
    explosionX = []
    explosionY = []
    dx = []
    dy = []
    enemyGone = []
    
    EnemyW = 50
    EnemyH = 60
    
    bx = random(-10,10)
    by = random(15,16)
    
    explosionW = 70
    explosionH = 80
    
    fireOn = 0

    score = 0
    
    bgY = 0
    
    stageNum = 0
    
    EnemyNum = 5
    
    startTime = 0
    
    for i in range(EnemyNum):
        EnemyX.append(random(0,width - RaidenW))
        EnemyY.append(random(0,height/3 - RaidenH))
        Enemy.append(loadImage('enemy' + str(i) + '.png'))
        dx.append(random(-7,7))
        dy.append(random(6,7))
        explosionX.append(-100)
        explosionY.append(-100)
        enemyGone.append(False)

def draw():
    if stageNum == 0:
        drawWelcome()
    if stageNum == 1:
        drawGameplay()
    if stageNum == 2:
        drawGameplay2()
    if stageNum == 3:
        drawFail()
    if stageNum == 4:
        drawWin()
    
def drawWelcome():
    image(bg,0,0)
        
    image(Raiden,RaidenX,RaidenY,RaidenW,RaidenH)
    
    textSize(37)
    fill(255)
    text("Press Raiden to start...", 270, 450)
    text("Instructions: Press left button to shoot missiles.", 10, 50)
    text("Move your mouse to move Raiden.", 245, 85)
    text("One enermy jet values 1 scores.", 245, 120)
    text("Try to get more scores.", 245, 155)
    text("Avoid hitting the enemies and their dead", 245, 190)
    text("bodies.", 245, 225)
    
def drawGameplay():
    global bgY
    global RaidenX, RaidenY
    global EnemyX, EnemyY, missileX, missileY, explosionX, explosionY
    global score, stageNum
    
    RaidenX = mouseX - RaidenW/2
    RaidenY = mouseY - RaidenH/2
    
    
    for i in range(0,10000,1):
        image(bg,0,bgY - 650*i, 1000, 1000)
    bgY = bgY + 5
    
    for i in range(EnemyNum):
        image(Enemy[i], EnemyX[i], EnemyY[i], EnemyW, EnemyH)
        EnemyX[i] = EnemyX[i] + dx[i]
        EnemyY[i] = EnemyY[i] + dy[i]
        
        if EnemyX[i] >= width - EnemyW or EnemyX[i] <= 0:
            dx[i] = -dx[i]
            
        if enemyGone[i] == False:
            if EnemyY[i] >= height:
                EnemyX[i] = random(0, width - EnemyW)
                EnemyY[i] = random(-EnemyH, 0)
            
        
        if EnemyY[i] <= 0 - EnemyH:
            EnemyX[i] = random(0, width - EnemyW)
            EnemyY[i] = random(height, height + EnemyY[i])
            
        if (missileX + missileW >= EnemyX[i] and missileX <= EnemyX[i] + EnemyW
            and missileY + missileH >= EnemyY[i] and missileY <= EnemyY[i] + EnemyH) and enemyGone[i] == False:
            dx[i] = 0
            dy[i] = random(15,16)
            score = score + 1
            enemyGone[i] = True
            
        if enemyGone[i] == True:
            image(Explosion, explosionX[i], explosionY[i], explosionW, explosionH)
            explosionX[i] = EnemyX[i]
            explosionY[i] = EnemyY[i]
            if enemyGone[i] == True and explosionY[i] >= height:
                EnemyX[i] = random(0, width - EnemyW)
                EnemyY[i] = random(-EnemyH, 0)
                dx[i] = random(-6,6)
                dy[i] = random(6,7)
                explosionX[i] = 1000
                enemyGone[i] = False
        
        if score >= 10:
            stageNum = 2

        if (RaidenX+RaidenW>EnemyX[i] and RaidenX+RaidenW<EnemyX[i]+EnemyW and RaidenY>EnemyY[i] and RaidenY<EnemyY[i]+EnemyH) or (RaidenX>EnemyX[i] and RaidenX<EnemyX[i]+EnemyW and RaidenY>EnemyY[i] and RaidenY<EnemyY[i]+EnemyH) or (RaidenX+RaidenW>EnemyX[i] and RaidenX+RaidenW<EnemyX[i]+EnemyW and RaidenY+RaidenH>EnemyY[i] and RaidenY+RaidenH<EnemyY[i]+EnemyH) or (RaidenX>EnemyX[i] and RaidenX<EnemyX[i]+EnemyW and RaidenY+RaidenH>EnemyY[i] and RaidenY+RaidenH<EnemyY[i]+EnemyH) and stageNum == 1:
            stageNum = 3
             
             
    image(Raiden, RaidenX, RaidenY, RaidenW, RaidenH)
    
    if fireOn == 1:
        image(missile, missileX - 10, missileY - 50, missileW, missileH)
        missileY = missileY - missileVelocity
        
    textSize(37)
    fill(255)
    text("Score:" + str(score), 10, 50)
    
def drawFail():
    textSize(50)
    fill(255)
    text("You die!", 420, 480)
    text("Press 'R' to continue.", 270, 540)
    if keyPressed:
        if key == "R" or key == "r":
            setup()
    
def drawGameplay2():
    global bgY
    global RaidenX, RaidenY
    global EnemyX, EnemyY, missileX, missileY, explosionX, explosionY
    global score, stageNum
    global BossX, BossY, bx, by
    
    stageNum2Time = millis()
    
    RaidenX = mouseX - RaidenW/2
    RaidenY = mouseY - RaidenH/2
    

    image(bg,0,0, 1000,1000)


    for i in range(0, 10, 1):
        for j in range(0, 10, 1):
            image(Explosion, i*100, j*100, 100, 100)
            
    
    image(Boss, BossX, BossY, BossW, BossH)
    BossX = BossX + bx
    BossY = BossY + by
    
    if BossX >= width - BossW or BossX <= 0:
            bx = -bx
        
            
    if BossY >= height - BossH or BossY <= 0:
            by = -by
    
    image(Raiden, RaidenX, RaidenY, RaidenW, RaidenH)
    
    if missileX + missileW >= BossX and missileX <= BossX + BossW and missileY + missileH >= BossY and missileY<= BossY + BossH:
        score = score + 1
        
    if score >= 100:
        stageNum = 4
        
    
    if RaidenX + RaidenW >= BossX and RaidenX <= BossX + BossW and RaidenY + RaidenH >= BossY and RaidenY <= BossY + BossH:
        stageNum = 3
        
    if fireOn == 1:
        image(missile, missileX - 10, missileY - 50, missileW, missileH)
        missileY = missileY - missileVelocity
    
    textSize(37)
    fill(255)
    text("Score:" + str(score), 10, 50)
    
def drawWin():
    textSize(50)
    fill(255)
    text("You win!", 420, 480)
    text("Press 'R' to continue.", 270, 540)
    if keyPressed:
        if key == "R" or key == "r":
            setup()
    
    
def mousePressed():
    global stageNum, fireOn, missileX, missileY
    if RaidenX <= mouseX <= RaidenX + RaidenW and RaidenY <= mouseY <= RaidenY + RaidenH and stageNum == 0:
        stageNum = 1

    if mousePressed:
        fireOn = 1
        
    if mousePressed:
        missileX = mouseX
        missileY = mouseY
        
        
        
        
        
        
    
