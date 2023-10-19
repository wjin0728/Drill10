world = [[], [], []]


def add_object(obj, depth):
    world[depth].append(obj)

def add_objects(obj, depth = 0):
    world[depth]+=obj


def remove_object(obj):
    for layer in world:
        if obj in layer:
            layer.remove(obj)
            return
    raise ValueError("와~ 버그 보소?")


def Update():
    for layer in world:
        for obj in layer:
            obj.update()


def Render():
    for layer in world:
        for obj in layer:
            obj.draw()

