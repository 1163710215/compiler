class Node:
    offset = 0
    type = ''
    t = ''
    w = ''
    val = ''
    width = 0
    addr = ''
    nextlist = []
    truelist = []
    falselist = []
    quad = 0

    def __init__(self, width):
        self.width = width
