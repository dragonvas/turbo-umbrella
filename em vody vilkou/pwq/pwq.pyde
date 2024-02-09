def collideCircleCircle(x,y,d,x2,y2,d2):
    if dist(x,y,x2,y2) <=(d/2)+(d2/2):
        return True
    else:
        return False
    
    
def setup():
    size(1000,1000)
def draw():
    background(123,234,0)
    if collideCircleCircle(0,200,100,mouseX,mouseY,100) or collideCircleCircle(200,200,100,mouseX,mouseY,100) or collideCircleCircle(400,200,100,mouseX,mouseY,100) or collideCircleCircle(600,200,100,mouseX,mouseY,100) or collideCircleCircle(800,200,100,mouseX,mouseY,100) or collideCircleCircle(100,200,100,mouseX,mouseY,100) or collideCircleCircle(300,200,100,mouseX,mouseY,100) or collideCircleCircle(500,200,100,mouseX,mouseY,100) or collideCircleCircle(700,200,100,mouseX,mouseY,100):
        fill(255,0,0)
    else:
        fill(255)
    ellipse(0,200,100,100)
    ellipse(200,200,100,100)
    ellipse(400,200,100,100)
    ellipse(800,200,100,100)
    ellipse(600,200,100,100)
    ellipse(100,200,100,100)
    ellipse(300,200,100,100)
    ellipse(500,200,100,100)
    ellipse(700,200,100,100)
    ellipse(0,200,100,100)
    ellipse(0,200,100,100)
    ellipse(0,200,100,100)
    ellipse(0,200,100,100)
    ellipse(0,200,100,100)
    ellipse(0,200,100,100)
    ellipse(0,200,100,100)
    ellipse(0,200,100,100)
    ellipse(0,200,100,100)
    ellipse(0,200,100,100)
    ellipse(0,200,100,100)
    ellipse(0,200,100,100)
    ellipse(0,200,100,100)
    ellipse(0,200,100,100)
    ellipse(0,200,100,100)
    ellipse(0,200,100,100)
    ellipse(0,200,100,100)
    ellipse(0,200,100,100)
    ellipse(0,200,100,100)
    ellipse(0,200,100,100)
    ellipse(0,200,100,100)
    ellipse(0,200,100,100)
    ellipse(0,200,100,100)
    ellipse(0,200,100,100)
    ellipse(0,200,100,100)
    ellipse(mouseX,mouseY,100,100)
    
