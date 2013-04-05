import pygame
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480), pygame.NOFRAME)
    clock = pygame.time.Clock()
    pygame.display.set_caption("Color!")
    pygame.mixer.music.load('bg_music.mp3')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.7)
    
    radius = 15
    x = 0
    y = 0
    mode = 'blue'
    points = []
    
    while True:
        
        pressed = pygame.key.get_pressed()
        
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            
            # determin if X was clicked, or Ctrl+W or Alt+F4 was used 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
            
                # determine if a letter key was pressed 
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
                elif event.key == pygame.K_y:
                    mode = 'yellow'
                elif event.key == pygame.K_p:
                    mode = 'purple'
                elif event.key == pygame.K_s:
                    pygame.image.save(screen, 'Color! save.jpeg')
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # left click grows radius 
                    radius = min(200, radius + 1)
                elif event.button == 3: # right click shrinks radius 
                    radius = max(1, radius - 1)
            
            if event.type == pygame.MOUSEMOTION:
                # if mouse moved, add point to list 
                position = event.pos
                points = points + [position]
                points = points[-256:]
                
        screen.fill((0, 0, 0))
        
        # draw all points 
        i = 0
        while i < len(points) - 1:
            drawLineBetween(screen, i, points[i], points[i + 1], radius, mode)
            i += 1
        
        pygame.display.flip()
        
        clock.tick(60)

def drawLineBetween(screen, index, start, end, width, color_mode):  
    if color_mode == 'blue':
        color = ( 0, 0, 255)
    elif color_mode == 'red':
        color = ( 255, 0, 0)
    elif color_mode == 'green':
        color = ( 0, 255, 0)
    elif color_mode == 'yellow':
        color = ( 255, 255, 0)
    elif color_mode == 'purple':
        color = ( 255, 0, 255)
        
    
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in xrange(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = aprogress * start[0] + progress * end[0]
        y = aprogress * start[1] + progress * end[1]
        pygame.draw.circle(screen, color, (x, y), width)

main()
