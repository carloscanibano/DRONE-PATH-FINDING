## V2.2
## Javier Huertas (2017-18)
## Alejandro Cervantes (2017-18)
## Based on code from:
## Daniel Borrajo (2016-17)
## To be used with python2.7
## Open source. Distributed as-is

import pygame
import os.path
import re
import random

# Define some colors
white    = ( 255, 255, 255)
green    = (   0, 255,   0)
red      = ( 255,   0,   0)
blue      = ( 70,   70,   255)
myred    = ( 230,   30, 70)
black    = (   0,   0,   0)
background = black
disp     = (0, 0)

def create_map (configuration, state, tracep):
    if tracep:
        print("Creating map")
        
    basicTile=configuration['basicTile']
#    basicMapData= [configuration['maptiles'][basicTile]['id'],0,dict(configuration['maptiles'][basicTile]['attributes'])  ]
    basicMapConf= configuration['maptiles'][basicTile]
        
#    mapa = [[[configuration['maptiles']['empty']['id']] for x in range(configuration['map_size'][1])] for y in range(configuration['map_size'][0])]
    mapa = [ [ [ basicMapConf['id'],0,
                 dict(basicMapConf['attributes'])]
               for x in range(configuration['map_size'][1])
             ] 
            for y in range(configuration['map_size'][0])]
    
    # state['prev_pos'] is the initial location of the agent
    # When creating the map we explicitly set a tile of the agentBaseTile type for this location in the configuration file
#    mapa[state['prev_pos'][0]][state['prev_pos'][1]] = [configuration['maptiles']['agent']['id']]

    # Establish one base with the agent (others will be void)
    agentBaseTile= configuration['agentBaseTile']
    agentBaseMapData= [ configuration['maptiles'][agentBaseTile]['id'],0,dict(configuration['maptiles'][agentBaseTile]['attributes'])]
    mapa[state['prev_pos'][0]][state['prev_pos'][1]]=agentBaseMapData

    agentType=configuration['agentType']
    mapa[state['prev_pos'][0]][state['prev_pos'][1]][2]['agent']=agentType
    
    for tilekey, tiledict in configuration['maptiles'].iteritems():
        if 'num' in tiledict:
            mapa = fill_map(configuration, mapa, tiledict)
            
    return mapa

def fill_map(configuration,mapa,attribute):
    # Create walls
    basicTile=configuration['basicTile']
    
    for i in range(0,attribute['num']):
        a = random.randrange(0,configuration['map_size'][0])
        b = random.randrange(0,configuration['map_size'][1])
        while not(mapa[a][b][0] == configuration['maptiles'][basicTile]['id']):
            a = random.randrange(0,configuration['map_size'][0])
            b = random.randrange(0,configuration['map_size'][1])
        if 'attributes' in attribute.keys():
            tileAttributes = dict(attribute['attributes'])
        else:
            tileAttributes = None
            
        mapa[a][b] = [attribute['id'],i,tileAttributes]
    return mapa

def print_map(mapa, configuration, images, screen, state, tile_size, fsm_state, tracep ,show_text="Insert text here"):
    basicTile=configuration['basicTile']
    if tracep:
        print("Printing map")
    screen.fill(background)
    #pygame.display.set_caption("Points: "+str(state['points'])+" Eats: "+str(state['eats'])+" Knives: "+str(state['knives'])+
    #                           " Bad Eats: "+str(state['bad_eats'])+" Moves: "+str(state['moves'])+" State: "+fsm_state)
    for i in range(0,configuration['map_size'][0]):
        for j in range (0,configuration['map_size'][1]):
            if mapa[i][j][0] == configuration['maptiles'][basicTile]['id']:
                d = [0, 0]
            else:
                d = disp

            rect = pygame.Rect((i * tile_size + d[0], (configuration['map_size'][1] - j - 1) * tile_size + d[1], 1, 1))
            #screen.blit(configuration['maptiles']['empty']['img'], rect)
            #if mapa[i][j][0] == configuration['goal']['id']:
            #    image = configuration['goal']['img']
            #else:
            if mapa[i][j][2]['agent'] is not None:
                image = images[mapa[i][j][2]['agent']]
            else:
                for tilekey, tiledict in configuration['maptiles'].iteritems():
                    if tiledict['id'] == mapa[i][j][0]:
                        image = images[tilekey]
            
            screen.blit(image, rect)
    if tracep:
        s = printable_map(mapa, configuration, True)
        print(s)
    #rect1 = pygame.Rect((0, configuration['map_size'][1] * tile_size, 1, 1))
    #font = pygame.font.SysFont(pygame.font.get_fonts()[6], 30)
    font = pygame.font.Font(None, 24)
    if state['inPause']:
        if state['step']:
                controlText="**** STEP MODE - PRESS 'S' TO STEP [SPACE: CONTINUE] ****"
        else:
                controlText="**** PAUSED - PRESS SPACE TO CONTINUE ['S' STEP] ****"
        controlColor=red
    else:
        controlText="**** RUNNING - FOLLOWING PLAN [SPACE: PAUSE] [S: STEP] ****"
        controlColor=blue
        
    rect1 = pygame.Rect((0, configuration['map_size'][1] * tile_size, 1, 1))
    rect2 = pygame.Rect((0, configuration['map_size'][1] * tile_size + 30, 1, 1))

    text1 = font.render(controlText,1,controlColor)
    screen.blit(text1, rect1)
    
    l=1
    
    if configuration['showState']:
        for show_line in show_text.split('\n'):
            rect2 = pygame.Rect((0, configuration['map_size'][1] * tile_size + 18*l, 1, 1))
            text2 = font.render(show_line,1,green)
            screen.blit(text2, rect2)
            l += 1
    #screen.blit(text1, rect1)
    #screen.blit(text2, rect2)
    pygame.display.flip()


def printable_map(mapa, configuration, screenp):
    s = ''
    for j in range (0,configuration['map_size'][1]):
        for i in range(0,configuration['map_size'][0]):
            if screenp:
                y = configuration['map_size'][1] - j - 1
            else: y = j
            
            if mapa[i][y][2]['agent'] == configuration["agentType"]:
                s+= configuration["agentMarker"]
            else:
                for tilekey, tiledict in configuration['maptiles'].iteritems():
                    if mapa[i][y][0] == tiledict['id']:
                        s += tiledict['marker']
        s = s + '\n'
    return s

def read_map(configuration):
    basicTile=configuration['basicTile']
    map_file= configuration['file']
    for tilekey, tiledict in configuration['maptiles'].iteritems():
        if 'num' in tiledict:
            tiledict['num'] = 0
    
    allowed = configuration["agentMarker"]
    for tilekey, tiledict in configuration["maptiles"].iteritems():
        allowed += tiledict['marker']
    
    allowed = "([" + allowed + "]*)\n"
    
    with open(map_file, 'r') as f:
        lines = re.findall(allowed,f.read())
        
    configuration['map_size'][1] = len(lines)
    configuration['map_size'][0] = len(lines[0])

 #   basicMapData=[ configuration['maptiles'][basicTile]['id'],0,configuration['maptiles'][basicTile]['attributes']] 
 #   mapa = [ [ basicMapData for x in range(configuration['map_size'][1])] for y in range(configuration['map_size'][0])]
    
    basicTile=configuration['basicTile']
#    basicMapData= [configuration['maptiles'][basicTile]['id'],0,dict(configuration['maptiles'][basicTile]['attributes'])  ]
    basicMapConf= configuration['maptiles'][basicTile]
        
#    mapa = [[[configuration['maptiles']['empty']['id']] for x in range(configuration['map_size'][1])] for y in range(configuration['map_size'][0])]
    mapa = [ [ [ basicMapConf['id'],0,
                 dict(basicMapConf['attributes'])]
               for x in range(configuration['map_size'][1])
             ] 
            for y in range(configuration['map_size'][0])]
    
#    mapa = [[[configuration['maptiles']['empty']['id']] for x in range(configuration['map_size'][1])] for y in range(configuration['map_size'][0])]
    column = -1
    for line in lines:
        row = -1
        column = column + 1
        for char in line:
            row = row + 1
            if char == configuration["agentMarker"] :
                agentBaseTile=configuration['agentBaseTile']
                tileConf= configuration['maptiles'][agentBaseTile]
                mapa[row][column][2]=dict(tileConf['attributes'])
                mapa[row][column][2]["agent"] = configuration["agentType"]
                mapa[row][column][0] = tileConf["id"]
                configuration["agentInit"] = [row,column]
            else:
                for tilekey, tiledict in configuration['maptiles'].iteritems():
                    if char == tiledict['marker']:
                        mapa[row][column][0] = tiledict['id']
                        # TODO: Revisar el indice
                        if 'num' in tiledict:
                            configuration['maptiles'][tilekey]['num'] += 1
                        mapa[row][column][2]=dict(tiledict['attributes'])
            
#    configuration['max_eats'] = configuration['num_eats']
    return mapa, configuration
