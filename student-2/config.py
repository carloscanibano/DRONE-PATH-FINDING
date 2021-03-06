## v2.2
## Javier Huertas (2017-18)
## Alejandro Cervantes (2017-18)
## To be used with python2.7
## Open source. Distributed as-is
#Cambiar apartado 'type' por cualquier otro para que lea un mapa aleatorio
#por ejemplo 'read'
#Disenar mapas aleatorios o mapas a mano. Probar con todos los algoritmos
#disponibles por lo menos tres mapas diferentes. 9 experimentos en total
configuration = {
"text_size": 150,
"tile_size": 50,
"type": "random",
"seed": 222,
"file": "./map.txt",
"map_size": [7, 3],
"delay": 0.1,
"showState": True,
"debugMap": True,
"debug": False,
"save": False,
"hazards": False,
"basicTile": "desert",
"agentInit":  [1, 1],
"agentBaseTile": "drone-base",
"agentType": "drone",
"agentMarker": "A",
"battery": 100,
"agentTiles": {
       "drone":"game/graphics/agents/dronPlain100.png"
     },
"maptiles": {
    "desert": {
        "img": "game/graphics/terrains/desert100.png",
        "id":  "desert",
        "marker": 'D',
        "attributes":
             {
                "agent":None,
                "cost":6
             }
        },
    "desert-traversed": {
        "img": "game/graphics/terrains/desertTraversed100.png",
        "id":  "desert-traversed",
        "marker": 'd',
        "attributes":
             {
                "agent":None,
                "cost":6
             }
        },
    "plains": {
        "img": "game/graphics/terrains/plains100.png",
        "id":  "plains",
        "marker": 'P',
        "num": 0,
        "attributes":
             {
                "agent":None,
                "cost":5
             }
        },
    "plains-traversed": {
        "img": "game/graphics/terrains/plainsTraversed100.png",
        "id":  "plains-traversed",
        "marker": 'p',
        "num": 0,
        "attributes":
             {
                "agent":None,
                "cost":5
             }
        },
    "hills": {
        "img": "game/graphics/terrains/hills100.png",
        "id":  "hills",
        "marker": 'H',
        "num": 0,
        "attributes":
             {
                "agent":None,
                "cost":4
             }
        },
    "hills-traversed": {
        "img": "game/graphics/terrains/hillsTraversed100.png",
        "id":  "hills-traversed",
        "marker": 'h',
        "num": 0,
        "attributes":
             {
                "agent":None,
                "cost":4
             }
        },
    "forest": {
        "img": "game/graphics/terrains/forest100.png",
        "id":  "forest",
        "marker": 'F',
        "num": 5,
        "attributes":
             {
                "agent":None,
                "cost":7
             }
        },
    "forest-traversed": {
        "img": "game/graphics/terrains/forestTraversed100.png",
        "id":  "forest-traversed",
        "marker": 'f',
        "num": 0,
        "attributes":
             {
                "agent":None,
                "cost":7
             }
        },
    "sea": {
        "img": "game/graphics/terrains/sea100.png",
        "id":  "sea",
        "marker": 'S',
        "num": 1,
        "attributes":
            {
                "agent":None,
                "water":True
            }
        },
    "sea-traversed": {
        "img": "game/graphics/terrains/seaTraversed100.png",
        "id":  "sea-traversed",
        "marker": 's',
        "num": 0,
        "attributes":
             {"agent":None}
        },
    "goal": {
        "img": "game/graphics/locations/camera100.png",
        "id":  "goal",
        "marker": 'G',
        "num": 4,
        "attributes":
            {
                "agent":None,
                "isGoal":True,
                "cost":0
            }
        },
    "goal-traversed": {
        "img": "game/graphics/locations/cameraTraversed100.png",
        "id":  "goal-traversed",
        "marker": 'G',
        "num": 0,
        "attributes":
            {
                "agent":None,
                "visited-goal":True,
                "cost": 0
            }
        },
    "drone-base": {
        "img": "game/graphics/locations/droneBase100.png",
        "id":  "drone-base",
        "marker": 'B',
        "num": 0,
        "attributes":
             {
                "agent":None,
                "cost":2
             }
        },
    "drone-base-traversed": {
        "img": "game/graphics/locations/droneBaseTraversed100.png",
        "id":  "drone-base-traversed",
        "marker": 'b',
        "num": 0,
        "attributes":
            {
                "agent":None,
                "cost":2
            }
        },
    "drone-battery:": {
        "img": "game/graphics/locations/droneBattery100.png",
        "id": "drone-battery",
        "marker": 'D',
        "num": 1,
        "attributes":
            {
                "agent":None,
                "cost":3,
                "charge":True
            }
        },
    "drone-battery-traversed:": {
        "img": "game/graphics/locations/droneBatteryTraversed100.png",
        "id": "drone-battery-traversed",
        "marker": 'd',
        "num": 0,
        "attributes":
            {
                "agent":None,
                "cost":1,
                "charge":True
            }
        }
    }
}
