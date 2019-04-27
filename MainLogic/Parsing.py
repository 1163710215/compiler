from treelib import Tree, Node

from MainLogic import Node

index = 0
seq = 0
orders = []
instance = 0
offset = 0
my_type = ''
width = 0
t = ''
w = ''
q = []
symbolTable = []
H1 = Node
I1 = Node
T = Node
path = 'txts/orders.txt'
symbolPath = 'txts/symbol_table.txt'


def p1(nodes, tree, node, tokens):
    node1 = tree.create_node('P', node.identifier + ',' + 'P', parent=node.identifier, data=Node.Node(0))

    nodes.append(node1)
    get_next(nodes, node, tree, tokens)
    return


def p2(nodes, tree, node, tokens):
    node1 = tree.create_node('D', node.identifier + ',' + 'D', parent=node.identifier, data=Node.Node(0))
    node2 = tree.create_node('P', node.identifier + ',' + 'P', parent=node.identifier, data=Node.Node(0))

    global offset
    offset = 0
    nodes.append(node1)
    get_next(nodes, node, tree, tokens)
    nodes.append(node2)
    get_next(nodes, node, tree, tokens)
    return


def p3(nodes, tree, node, tokens):
    node1 = tree.create_node('S', node.identifier + ',' + 'S', parent=node.identifier, data=Node.Node(0))
    node2 = tree.create_node('P', node.identifier + ',' + 'P', parent=node.identifier, data=Node.Node(0))

    nodes.append(node1)
    get_next(nodes, node, tree, tokens)
    nodes.append(node2)
    get_next(nodes, node, tree, tokens)
    return


def p4(nodes, tree, node, tokens):
    return


def p5(nodes, tree, node, tokens):
    node1 = tree.create_node('proc', node.identifier + ',' + 'proc', parent=node.identifier, data=Node.Node(0))
    node2 = tree.create_node('X', node.identifier + ',' + 'X', parent=node.identifier, data=Node.Node(0))
    node3 = tree.create_node('id', node.identifier + ',' + 'id', parent=node.identifier, data=Node.Node(0))
    node4 = tree.create_node('(', node.identifier + ',' + '(', parent=node.identifier, data=Node.Node(0))
    node5 = tree.create_node('M', node.identifier + ',' + 'M', parent=node.identifier, data=Node.Node(0))
    node6 = tree.create_node(')', node.identifier + ',' + ')', parent=node.identifier, data=Node.Node(0))
    node7 = tree.create_node('{', node.identifier + ',' + '{', parent=node.identifier, data=Node.Node(0))
    node8 = tree.create_node('P', node.identifier + ',' + 'P', parent=node.identifier, data=Node.Node(0))
    node9 = tree.create_node('}', node.identifier + ',' + '}', parent=node.identifier, data=Node.Node(0))

    nodes.append(node1)
    get_next(nodes, node, tree, tokens)
    nodes.append(node2)
    get_next(nodes, node, tree, tokens)
    nodes.append(node3)
    get_next(nodes, node, tree, tokens)

    global my_type
    my_type = 'proc'
    enter(tree.get_node(node3.identifier).data.val, my_type, offset)

    nodes.append(node4)
    get_next(nodes, node, tree, tokens)
    nodes.append(node5)
    get_next(nodes, node, tree, tokens)
    nodes.append(node6)
    get_next(nodes, node, tree, tokens)
    nodes.append(node7)
    get_next(nodes, node, tree, tokens)
    nodes.append(node8)
    get_next(nodes, node, tree, tokens)
    nodes.append(node9)
    get_next(nodes, node, tree, tokens)
    return


def p6(nodes, tree, node, tokens):
    node1 = tree.create_node('T', node.identifier + ',' + 'T', parent=node.identifier, data=Node.Node(0))
    node2 = tree.create_node('id', node.identifier + ',' + 'id', parent=node.identifier, data=Node.Node(0))
    node3 = tree.create_node('A', node.identifier + ',' + 'A', parent=node.identifier, data=Node.Node(0))
    node4 = tree.create_node(';', node.identifier + ',' + ';', parent=node.identifier, data=Node.Node(0))

    nodes.append(node1)
    get_next(nodes, node, tree, tokens)
    global offset, H1, T
    T = node1
    nodes.append(node2)
    get_next(nodes, node, tree, tokens)

    enter(tree.get_node(node2.identifier).data.val, tree.get_node(node1.identifier).data.type, offset)
    offset += tree.get_node(node1.identifier).data.width
    H1 = tree.get_node(node2.identifier)
    nodes.append(node3)
    get_next(nodes, node, tree, tokens)
    nodes.append(node4)
    get_next(nodes, node, tree, tokens)
    return


def p7(nodes, tree, node, tokens):
    node1 = tree.create_node('record', node.identifier + ',' + 'record', parent=node.identifier, data=Node.Node(0))
    node2 = tree.create_node('id', node.identifier + ',' + 'id', parent=node.identifier, data=Node.Node(0))
    node3 = tree.create_node('{', node.identifier + ',' + '{', parent=node.identifier, data=Node.Node(0))
    node4 = tree.create_node('P', node.identifier + ',' + 'P', parent=node.identifier, data=Node.Node(0))
    node5 = tree.create_node('}', node.identifier + ',' + '}', parent=node.identifier, data=Node.Node(0))

    nodes.append(node1)
    get_next(nodes, node, tree, tokens)
    nodes.append(node2)
    get_next(nodes, node, tree, tokens)
    global my_type
    my_type = 'record'
    enter(tree.get_node(node2.identifier).data.val, my_type, offset)

    nodes.append(node3)
    get_next(nodes, node, tree, tokens)
    nodes.append(node4)
    get_next(nodes, node, tree, tokens)
    nodes.append(node5)
    get_next(nodes, node, tree, tokens)
    return


def p8(nodes, tree, node, tokens):
    node1 = tree.create_node('=', node.identifier + ',' + '=', parent=node.identifier, data=Node.Node(0))
    node2 = tree.create_node('F', node.identifier + ',' + 'F', parent=node.identifier, data=Node.Node(0))
    node3 = tree.create_node('A', node.identifier + ',' + 'A', parent=node.identifier, data=Node.Node(0))
    nodes.append(node1)
    get_next(nodes, node, tree, tokens)
    nodes.append(node2)
    get_next(nodes, node, tree, tokens)
    nodes.append(node3)
    get_next(nodes, node, tree, tokens)
    global H1
    gen('=', tree.get_node(node2.identifier).data.addr, '_', H1.data.val)
    return


def p9(nodes, tree, node, tokens):
    return


def p10(nodes, tree, node, tokens):
    node1 = tree.create_node(',', node.identifier + ',' + ',', parent=node.identifier, data=Node.Node(0))
    node2 = tree.create_node('id', node.identifier + ',' + 'id', parent=node.identifier, data=Node.Node(0))
    node3 = tree.create_node('A', node.identifier + ',' + 'A', parent=node.identifier, data=Node.Node(0))

    nodes.append(node1)
    get_next(nodes, node, tree, tokens)
    nodes.append(node2)
    get_next(nodes, node, tree, tokens)

    global offset, T
    enter(tree.get_node(node2.identifier).data.val, T.data.type, offset)

    offset += 4
    # tree.get_node(
    # tree.get_node(node.identifier).parent.identifier + ',T').data.width
    nodes.append(node3)
    get_next(nodes, node, tree, tokens)
    return


def p11(nodes, tree, node, tokens):
    node1 = tree.create_node('X', node.identifier + ',' + 'X', parent=node.identifier, data=Node.Node(0))
    node2 = tree.create_node('id', node.identifier + ',' + 'id', parent=node.identifier, data=Node.Node(0))
    node3 = tree.create_node('M-', node.identifier + ',' + 'M-', parent=node.identifier, data=Node.Node(0))

    nodes.append(node1)
    get_next(nodes, node, tree, tokens)
    nodes.append(node2)
    get_next(nodes, node, tree, tokens)

    global offset
    enter(tree.get_node(node2.identifier).data.val, tree.get_node(node1.identifier).data.type, offset)

    offset += tree.get_node(node1.identifier).data.offset
    nodes.append(node3)
    get_next(nodes, node, tree, tokens)
    return


def p12(nodes, tree, node, tokens):
    node1 = tree.create_node(',', node.identifier + ',' + ',', parent=node.identifier, data=Node.Node(0))
    node2 = tree.create_node('X', node.identifier + ',' + 'X', parent=node.identifier, data=Node.Node(0))
    node3 = tree.create_node('id', node.identifier + ',' + 'id', parent=node.identifier, data=Node.Node(0))
    node4 = tree.create_node('M-', node.identifier + ',' + 'M-', parent=node.identifier, data=Node.Node(0))

    nodes.append(node1)
    get_next(nodes, node, tree, tokens)
    nodes.append(node2)
    get_next(nodes, node, tree, tokens)
    nodes.append(node3)
    get_next(nodes, node, tree, tokens)
    enter(tree.get_node(node3.identifier).data.val, tree.get_node(node2.identifier).data.type, offset)

    nodes.append(node4)
    get_next(nodes, node, tree, tokens)
    return


def p13(nodes, tree, node, tokens):
    return


def p14(nodes, tree, node, tokens):
    node1 = tree.create_node('X', node.identifier + ',' + 'X', parent=node.identifier, data=Node.Node(0))
    node2 = tree.create_node('C', node.identifier + ',' + 'C', parent=node.identifier, data=Node.Node(0))

    nodes.append(node1)
    get_next(nodes, node, tree, tokens)
    global t, w
    t = tree.get_node(node1.identifier).data.type
    w = tree.get_node(node1.identifier).data.width

    nodes.append(node2)
    get_next(nodes, node, tree, tokens)
    tree.get_node(node.identifier).data.type = tree.get_node(node2.identifier).data.type
    tree.get_node(node.identifier).data.width = tree.get_node(node2.identifier).data.width

    return


def p15(nodes, tree, node, tokens):
    node1 = tree.create_node('int', node.identifier + ',' + 'int', parent=node.identifier, data=Node.Node(0))

    nodes.append(node1)
    get_next(nodes, node, tree, tokens)
    tree.get_node(node.identifier).data.type = 'int'
    tree.get_node(node.identifier).data.width = 4

    return


def p16(nodes, tree, node, tokens):
    node1 = tree.create_node('float', node.identifier + ',' + 'float', parent=node.identifier, data=Node.Node(0))

    nodes.append(node1)
    get_next(nodes, node, tree, tokens)
    tree.get_node(node.identifier).data.type = 'float'
    tree.get_node(node.identifier).data.width = 8
    return


def p17(nodes, tree, node, tokens):
    node1 = tree.create_node('char', node.identifier + ',' + 'char', parent=node.identifier, data=Node.Node(0))

    nodes.append(node1)
    get_next(nodes, node, tree, tokens)
    tree.get_node(node.identifier).data.type = 'char'
    tree.get_node(node.identifier).data.width = 1
    return


def p18(nodes, tree, node, tokens):
    node1 = tree.create_node('[', node.identifier + ',' + '[', parent=node.identifier, data=Node.Node(0))
    node2 = tree.create_node('digit', node.identifier + ',' + 'digit', parent=node.identifier, data=Node.Node(0))
    node3 = tree.create_node(']', node.identifier + ',' + ']', parent=node.identifier, data=Node.Node(0))
    node4 = tree.create_node('C', node.identifier + ',' + 'C', parent=node.identifier, data=Node.Node(0))

    nodes.append(node1)
    get_next(nodes, node, tree, tokens)
    nodes.append(node2)
    get_next(nodes, node, tree, tokens)
    nodes.append(node3)
    get_next(nodes, node, tree, tokens)
    nodes.append(node4)
    get_next(nodes, node, tree, tokens)
    tree.get_node(node.identifier).data.type = 'array(' + tree.get_node(
        node2.identifier).data.val + ',' + tree.get_node(node4.identifier).data.type + ')'
    tree.get_node(node.identifier).data.width = int(tree.get_node(node2.identifier).data.val) * int(tree.get_node(
        node4.identifier).data.width)
    return


def p19(nodes, tree, node, tokens):
    tree.get_node(node.identifier).data.type = t
    tree.get_node(node.identifier).data.width = w

    return


def p20(nodes, tree, node, tokens):
    node1 = tree.create_node('L', node.identifier + ',' + 'L', parent=node.identifier, data=Node.Node(0))
    node2 = tree.create_node('=', node.identifier + ',' + '=', parent=node.identifier, data=Node.Node(0))
    node3 = tree.create_node('E', node.identifier + ',' + 'E', parent=node.identifier, data=Node.Node(0))
    node4 = tree.create_node(';', node.identifier + ',' + ';', parent=node.identifier, data=Node.Node(0))

    nodes.append(node1)
    get_next(nodes, node, tree, tokens)
    nodes.append(node2)
    get_next(nodes, node, tree, tokens)
    nodes.append(node3)
    get_next(nodes, node, tree, tokens)
    nodes.append(node4)
    get_next(nodes, node, tree, tokens)
    gen('=', tree.get_node(node3.identifier).data.addr, '_', tree.get_node(node1.identifier).data.addr)
    return


def p21(nodes, tree, node, tokens):
    node1 = tree.create_node('if', node.identifier + ',' + 'if', parent=node.identifier, data=Node.Node(0))
    node2 = tree.create_node('B', node.identifier + ',' + 'B', parent=node.identifier, data=Node.Node(0))
    node3 = tree.create_node('then', node.identifier + ',' + 'then', parent=node.identifier, data=Node.Node(0))
    node4 = tree.create_node('M1', node.identifier + ',' + 'M1', parent=node.identifier, data=Node.Node(0))
    node5 = tree.create_node('S', node.identifier + ',' + 'S1', parent=node.identifier, data=Node.Node(0))
    node7 = tree.create_node('else', node.identifier + ',' + 'else', parent=node.identifier, data=Node.Node(0))
    node8 = tree.create_node('M2', node.identifier + ',' + 'M2', parent=node.identifier, data=Node.Node(0))
    node9 = tree.create_node('S', node.identifier + ',' + 'S2', parent=node.identifier, data=Node.Node(0))

    nodes.append(node1)
    get_next(nodes, node, tree, tokens)
    nodes.append(node2)
    get_next(nodes, node, tree, tokens)
    nodes.append(node3)
    get_next(nodes, node, tree, tokens)
    nodes.append(node4)
    get_next(nodes, node, tree, tokens)

    nodes.append(node5)
    get_next(nodes, node, tree, tokens)
    local_seq = seq
    gen('j', '_', '_', '_')
    nodes.append(node7)
    get_next(nodes, node, tree, tokens)

    nodes.append(node8)
    get_next(nodes, node, tree, tokens)
    nodes.append(node9)
    get_next(nodes, node, tree, tokens)
    back_patch([local_seq], seq)

    back_patch(tree.get_node(node2.identifier).data.truelist, tree.get_node(node4.identifier).data.quad)
    back_patch(tree.get_node(node2.identifier).data.falselist, tree.get_node(node8.identifier).data.quad)
    tree.get_node(node5.identifier).data.nextlist = tree.get_node(node5.identifier).data.nextlist + tree.get_node(
        node9.identifier).data.nextlist

    return


def p22(nodes, tree, node, tokens):
    node1 = tree.create_node('while', node.identifier + ',' + 'while', parent=node.identifier, data=Node.Node(0))
    node2 = tree.create_node('M1', node.identifier + ',' + 'M1', parent=node.identifier, data=Node.Node(0))
    node3 = tree.create_node('B', node.identifier + ',' + 'B', parent=node.identifier, data=Node.Node(0))
    node4 = tree.create_node('do', node.identifier + ',' + 'do', parent=node.identifier, data=Node.Node(0))
    node5 = tree.create_node('{', node.identifier + ',' + '{', parent=node.identifier, data=Node.Node(0))

    node6 = tree.create_node('M2', node.identifier + ',' + 'M2', parent=node.identifier, data=Node.Node(0))
    node7 = tree.create_node('S', node.identifier + ',' + 'S', parent=node.identifier, data=Node.Node(0))
    node8 = tree.create_node('}', node.identifier + ',' + '}', parent=node.identifier, data=Node.Node(0))

    nodes.append(node1)
    get_next(nodes, node, tree, tokens)
    nodes.append(node2)
    get_next(nodes, node, tree, tokens)
    nodes.append(node3)
    get_next(nodes, node, tree, tokens)
    nodes.append(node4)
    get_next(nodes, node, tree, tokens)
    nodes.append(node5)
    get_next(nodes, node, tree, tokens)
    nodes.append(node6)
    get_next(nodes, node, tree, tokens)
    nodes.append(node7)
    get_next(nodes, node, tree, tokens)
    nodes.append(node8)
    get_next(nodes, node, tree, tokens)

    back_patch(tree.get_node(node7.identifier).data.nextlist, tree.get_node(node2.identifier).data.quad)
    back_patch(tree.get_node(node3.identifier).data.truelist, tree.get_node(node6.identifier).data.quad)
    tree.get_node(node.identifier).data.nextlist = tree.get_node(node3.identifier).data.falselist
    gen('j', '_', '_', tree.get_node(node2.identifier).data.quad)
    return


# 实现函数
def p23(nodes, tree, node, tokens):
    node1 = tree.create_node('call', node.identifier + ',' + 'call', parent=node.identifier, data=Node.Node(0))
    node2 = tree.create_node('id', node.identifier + ',' + 'id', parent=node.identifier, data=Node.Node(0))
    node3 = tree.create_node('(', node.identifier + ',' + '(', parent=node.identifier, data=Node.Node(0))
    node4 = tree.create_node('Elist', node.identifier + ',' + 'Elist', parent=node.identifier, data=Node.Node(0))
    node5 = tree.create_node(')', node.identifier + ',' + ')', parent=node.identifier, data=Node.Node(0))
    node6 = tree.create_node(';', node.identifier + ',' + ';', parent=node.identifier, data=Node.Node(0))

    nodes.append(node1)
    get_next(nodes, node, tree, tokens)
    nodes.append(node2)
    get_next(nodes, node, tree, tokens)
    nodes.append(node3)
    get_next(nodes, node, tree, tokens)
    nodes.append(node4)
    get_next(nodes, node, tree, tokens)
    nodes.append(node5)
    get_next(nodes, node, tree, tokens)
    nodes.append(node6)
    get_next(nodes, node, tree, tokens)

    n = 0
    global q
    for t in q:
        gen('param', '_', '_', t)
        n += 1
    gen('call', n, '_', tree.get_node(node2.identifier).data.addr)

    return


def p24(nodes, tree, node, tokens):
    node1 = tree.create_node('return', node.identifier + ',' + 'return', parent=node.identifier, data=Node.Node(0))
    node2 = tree.create_node('E', node.identifier + ',' + 'E', parent=node.identifier, data=Node.Node(0))
    node3 = tree.create_node(';', node.identifier + ',' + ';', parent=node.identifier, data=Node.Node(0))

    nodes.append(node1)
    get_next(nodes, node, tree, tokens)
    nodes.append(node2)
    get_next(nodes, node, tree, tokens)
    nodes.append(node3)
    get_next(nodes, node, tree, tokens)
    gen('return', '_', '_', tree.get_node(node2.identifier).data.addr)
    return


# ...
def p25(nodes, tree, node, tokens):
    node1 = tree.create_node('switch', node.identifier + ',' + 'switch', parent=node.identifier, data=Node.Node(0))
    node2 = tree.create_node('(', node.identifier + ',' + '(', parent=node.identifier, data=Node.Node(0))
    node3 = tree.create_node('id', node.identifier + ',' + 'id', parent=node.identifier, data=Node.Node(0))
    node4 = tree.create_node(')', node.identifier + ',' + ')', parent=node.identifier, data=Node.Node(0))
    node5 = tree.create_node('{', node.identifier + ',' + '{', parent=node.identifier, data=Node.Node(0))
    node6 = tree.create_node('N', node.identifier + ',' + 'N', parent=node.identifier, data=Node.Node(0))
    node7 = tree.create_node('default', node.identifier + ',' + 'default', parent=node.identifier, data=Node.Node(0))
    node8 = tree.create_node(':', node.identifier + ',' + ':', parent=node.identifier, data=Node.Node(0))
    node9 = tree.create_node('S', node.identifier + ',' + 'S', parent=node.identifier, data=Node.Node(0))
    node10 = tree.create_node('}', node.identifier + ',' + '}', parent=node.identifier, data=Node.Node(0))

    nodes.append(node1)
    get_next(nodes, node, tree, tokens)
    nodes.append(node2)
    get_next(nodes, node, tree, tokens)
    nodes.append(node3)
    get_next(nodes, node, tree, tokens)
    nodes.append(node4)
    get_next(nodes, node, tree, tokens)
    nodes.append(node5)
    get_next(nodes, node, tree, tokens)
    nodes.append(node6)
    get_next(nodes, node, tree, tokens)
    nodes.append(node7)
    get_next(nodes, node, tree, tokens)
    nodes.append(node8)
    get_next(nodes, node, tree, tokens)

    # label()
    nodes.append(node9)
    get_next(nodes, node, tree, tokens)

    nodes.append(node10)
    get_next(nodes, node, tree, tokens)
    return


# ...
def p26(nodes, tree, node, tokens):
    node1 = tree.create_node('for', node.identifier + ',' + 'for', parent=node.identifier, data=Node.Node(0))
    node2 = tree.create_node('(', node.identifier + ',' + '(', parent=node.identifier, data=Node.Node(0))
    node3 = tree.create_node('S', node.identifier + ',' + 'S1', parent=node.identifier, data=Node.Node(0))
    node4 = tree.create_node('B', node.identifier + ',' + 'B', parent=node.identifier, data=Node.Node(0))
    node5 = tree.create_node(';', node.identifier + ',' + ';', parent=node.identifier, data=Node.Node(0))
    node6 = tree.create_node('id', node.identifier + ',' + 'id', parent=node.identifier, data=Node.Node(0))
    node7 = tree.create_node('V', node.identifier + ',' + 'V', parent=node.identifier, data=Node.Node(0))
    node8 = tree.create_node(')', node.identifier + ',' + ')', parent=node.identifier, data=Node.Node(0))
    node9 = tree.create_node('{', node.identifier + ',' + '{', parent=node.identifier, data=Node.Node(0))
    node10 = tree.create_node('S', node.identifier + ',' + 'S2', parent=node.identifier, data=Node.Node(0))
    node11 = tree.create_node('}', node.identifier + ',' + '}', parent=node.identifier, data=Node.Node(0))

    nodes.append(node1)
    get_next(nodes, node, tree, tokens)
    nodes.append(node2)
    get_next(nodes, node, tree, tokens)
    nodes.append(node3)
    get_next(nodes, node, tree, tokens)
    nodes.append(node4)
    get_next(nodes, node, tree, tokens)
    nodes.append(node5)
    get_next(nodes, node, tree, tokens)
    nodes.append(node6)
    get_next(nodes, node, tree, tokens)
    nodes.append(node7)
    get_next(nodes, node, tree, tokens)
    nodes.append(node8)
    get_next(nodes, node, tree, tokens)
    nodes.append(node9)
    get_next(nodes, node, tree, tokens)
    nodes.append(node10)
    get_next(nodes, node, tree, tokens)
    nodes.append(node11)
    get_next(nodes, node, tree, tokens)
    return


def p27(nodes, tree, node, tokens):
    node1 = tree.create_node('++', node.identifier + ',' + '++', parent=node.identifier, data=Node.Node(0))

    nodes.append(node1)
    get_next(nodes, node, tree, tokens)
    return


def p28(nodes, tree, node, tokens):
    node1 = tree.create_node('--', node.identifier + ',' + '--', parent=node.identifier, data=Node.Node(0))

    nodes.append(node1)
    return


def p29(nodes, tree, node, tokens):
    node1 = tree.create_node('case', node.identifier + ',' + 'case', parent=node.identifier, data=Node.Node(0))
    node2 = tree.create_node('digit', node.identifier + ',' + 'digit', parent=node.identifier, data=Node.Node(0))
    node3 = tree.create_node(':', node.identifier + ',' + ':', parent=node.identifier, data=Node.Node(0))
    node4 = tree.create_node('S', node.identifier + ',' + 'S', parent=node.identifier, data=Node.Node(0))
    node5 = tree.create_node('N', node.identifier + ',' + 'N', parent=node.identifier, data=Node.Node(0))

    nodes.append(node1)
    get_next(nodes, node, tree, tokens)
    nodes.append(node2)
    get_next(nodes, node, tree, tokens)
    nodes.append(node3)
    get_next(nodes, node, tree, tokens)
    nodes.append(node4)
    get_next(nodes, node, tree, tokens)
    nodes.append(node5)
    get_next(nodes, node, tree, tokens)
    return


def p30(nodes, tree, node, tokens):
    tree.get_node(node.identifier).data.nextlist = [seq]
    gen('j', '_', '_', '_')
    return


def p31(nodes, tree, node, tokens):
    node1 = tree.create_node('G', node.identifier + ',' + 'G', parent=node.identifier, data=Node.Node(0))
    node2 = tree.create_node('E-', node.identifier + ',' + 'E-', parent=node.identifier, data=Node.Node(0))

    nodes.append(node1)
    get_next(nodes, node, tree, tokens)
    nodes.append(node2)
    get_next(nodes, node, tree, tokens)
    if tree.get_node(node2.identifier).data.addr == '':
        tree.get_node(node.identifier).data.addr = tree.get_node(node1.identifier).data.addr
        tree.get_node(node.identifier).data.val = tree.get_node(node1.identifier).data.val
        pass
    else:
        tree.get_node(node.identifier).data.addr = new_temp()
        gen('+', tree.get_node(node1.identifier).data.addr, tree.get_node(node2.identifier).data.addr,
            tree.get_node(node.identifier).data.addr)
    return


def p32(nodes, tree, node, tokens):
    node1 = tree.create_node('+', node.identifier + ',' + '+', parent=node.identifier, data=Node.Node(0))
    node2 = tree.create_node('G', node.identifier + ',' + 'G', parent=node.identifier, data=Node.Node(0))
    node3 = tree.create_node('E-', node.identifier + ',' + 'E-', parent=node.identifier, data=Node.Node(0))

    nodes.append(node1)
    get_next(nodes, node, tree, tokens)
    nodes.append(node2)
    get_next(nodes, node, tree, tokens)
    nodes.append(node3)
    get_next(nodes, node, tree, tokens)
    tree.get_node(node.identifier).data.addr = tree.get_node(node2.identifier).data.addr
    return


def p33(nodes, tree, node, tokens):
    return


def p34(nodes, tree, node, tokens):
    node1 = tree.create_node('F', node.identifier + ',' + 'F', parent=node.identifier, data=Node.Node(0))
    node2 = tree.create_node('G-', node.identifier + ',' + 'G-', parent=node.identifier, data=Node.Node(0))

    nodes.append(node1)
    get_next(nodes, node, tree, tokens)
    nodes.append(node2)
    get_next(nodes, node, tree, tokens)

    if tree.get_node(node2.identifier).data.addr == '':
        tree.get_node(node.identifier).data.addr = tree.get_node(node1.identifier).data.addr
        tree.get_node(node.identifier).data.val = tree.get_node(node1.identifier).data.val
        pass
    else:
        tree.get_node(node.identifier).data.addr = new_temp()
        gen('*', tree.get_node(node1.identifier).data.addr, tree.get_node(node2.identifier).data.addr,
            tree.get_node(node.identifier).data.addr)
    return


def p35(nodes, tree, node, tokens):
    node1 = tree.create_node('*', node.identifier + ',' + '*', parent=node.identifier, data=Node.Node(0))
    node2 = tree.create_node('F', node.identifier + ',' + 'F', parent=node.identifier, data=Node.Node(0))
    node3 = tree.create_node('G-', node.identifier + ',' + 'G-', parent=node.identifier, data=Node.Node(0))

    nodes.append(node1)
    get_next(nodes, node, tree, tokens)
    nodes.append(node2)
    get_next(nodes, node, tree, tokens)
    nodes.append(node3)
    get_next(nodes, node, tree, tokens)
    tree.get_node(node.identifier).data.addr = tree.get_node(node2.identifier).data.addr
    return


def p36(nodes, tree, node, tokens):
    return


def p37(nodes, tree, node, tokens):
    node1 = tree.create_node('(', node.identifier + ',' + '(', parent=node.identifier, data=Node.Node(0))
    node2 = tree.create_node('E', node.identifier + ',' + 'E', parent=node.identifier, data=Node.Node(0))

    node3 = tree.create_node(')', node.identifier + ',' + ')', parent=node.identifier, data=Node.Node(0))

    nodes.append(node1)
    get_next(nodes, node, tree, tokens)
    nodes.append(node2)
    get_next(nodes, node, tree, tokens)
    nodes.append(node3)
    get_next(nodes, node, tree, tokens)
    tree.get_node(node.identifier).data.addr = tree.get_node(node2.identifier).data.addr
    return


def p38(nodes, tree, node, tokens):
    node1 = tree.create_node('digit', node.identifier + ',' + 'digit', parent=node.identifier, data=Node.Node(0))

    nodes.append(node1)
    get_next(nodes, node, tree, tokens)
    tree.get_node(node.identifier).data.val = tree.get_node(node1.identifier).data.val
    tree.get_node(node.identifier).data.addr = tree.get_node(node1.identifier).data.addr
    return


def p39(nodes, tree, node, tokens):
    node1 = tree.create_node('char', node.identifier + ',' + 'char', parent=node.identifier, data=Node.Node(0))

    nodes.append(node1, tokens)
    get_next(nodes, node, tree, tokens)
    tree.get_node(node.identifier).data.val = tree.get_node(node1.identifier).data.val
    tree.get_node(node.identifier).data.addr = tree.get_node(node1.identifier).data.addr

    return


def p40(nodes, tree, node, tokens):
    node1 = tree.create_node('id', node.identifier + ',' + 'id', parent=node.identifier, data=Node.Node(0))

    nodes.append(node1)
    get_next(nodes, node, tree, tokens)
    addr = tree.get_node(node1.identifier).data.addr
    val = tree.get_node(node1.identifier).data.val
    tree.get_node(node.identifier).data.val = val
    tree.get_node(node.identifier).data.addr = addr

    flag = False
    global symbolTable
    for s in symbolTable:
        try:
            if s[0] == val:
                flag = True
                break
        except IndexError:
            print(s)
    if not flag:
        print('未声明 ' + str(val))
    return


def p41(nodes, tree, node, tokens):
    node1 = tree.create_node('id', node.identifier + ',' + 'id', parent=node.identifier, data=Node.Node(0))
    node2 = tree.create_node('L-', node.identifier + ',' + 'L-', parent=node.identifier, data=Node.Node(0))

    nodes.append(node1)

    get_next(nodes, node, tree, tokens)
    nodes.append(node2)
    get_next(nodes, node, tree, tokens)
    addr = tree.get_node(node1.identifier).data.addr
    val = tree.get_node(node1.identifier).data.val
    tree.get_node(node.identifier).data.val = val + tree.get_node(node2.identifier).data.val
    tree.get_node(node.identifier).data.addr = addr + tree.get_node(node2.identifier).data.addr

    flag = False
    global symbolTable
    for s in symbolTable:
        try:
            if s[0] == val:
                flag = True
                break
        except IndexError:
            print(s)

    if not flag:
        print('未声明 ' + str(val))
    return


def p42(nodes, tree, node, tokens):
    node1 = tree.create_node('[', node.identifier + ',' + '[', parent=node.identifier, data=Node.Node(0))
    node2 = tree.create_node('digit', node.identifier + ',' + 'digit', parent=node.identifier, data=Node.Node(0))
    node3 = tree.create_node(']', node.identifier + ',' + ']', parent=node.identifier, data=Node.Node(0))
    node4 = tree.create_node('L-', node.identifier + ',' + 'L-', parent=node.identifier, data=Node.Node(0))

    nodes.append(node1)
    get_next(nodes, node, tree, tokens)
    nodes.append(node2)
    get_next(nodes, node, tree, tokens)
    nodes.append(node3)
    get_next(nodes, node, tree, tokens)
    nodes.append(node4)
    get_next(nodes, node, tree, tokens)
    tree.get_node(node.identifier).data.addr = '[' + tree.get_node(
        node2.identifier).data.addr + ']' + tree.get_node(node4.identifier).data.addr

    return


def p43(nodes, tree, node, tokens):
    return


def p44(nodes, tree, node, tokens):
    node1 = tree.create_node('H', node.identifier + ',' + 'H', parent=node.identifier, data=Node.Node(0))
    node2 = tree.create_node('B-', node.identifier + ',' + 'B-', parent=node.identifier, data=Node.Node(0))

    nodes.append(node1)
    get_next(nodes, node, tree, tokens)
    global H1
    H1 = tree.get_node(node1.identifier)
    nodes.append(node2)
    get_next(nodes, node, tree, tokens)

    tree.get_node(node.identifier).data.truelist = tree.get_node(node2.identifier).data.truelist
    tree.get_node(node.identifier).data.falselist = tree.get_node(node2.identifier).data.falselist

    return


def p45(nodes, tree, node, tokens):
    node1 = tree.create_node('or', node.identifier + ',' + 'or', parent=node.identifier, data=Node.Node(0))
    node2 = tree.create_node('M1', node.identifier + ',' + 'M1', parent=node.identifier, data=Node.Node(0))

    node3 = tree.create_node('H', node.identifier + ',' + 'H', parent=node.identifier, data=Node.Node(0))
    node4 = tree.create_node('B-', node.identifier + ',' + 'B-', parent=node.identifier, data=Node.Node(0))

    nodes.append(node1)
    get_next(nodes, node, tree, tokens)
    nodes.append(node2)
    get_next(nodes, node, tree, tokens)
    nodes.append(node3)
    get_next(nodes, node, tree, tokens)
    nodes.append(node4)
    get_next(nodes, node, tree, tokens)

    global H1
    back_patch(H1.falselist, tree.get_node(node2.identifier).data.quad)
    tree.get_node(node.identifier).data.truelist = H1.truelist + tree.get_node(node3.identifier).data.truelist
    tree.get_node(node.identifier).data.falselist = tree.get_node(node3.identifier).data.falselist

    return


def p46(nodes, tree, node, tokens):
    tree.get_node(node.identifier).data.quad = seq
    global H1
    try:
        tree.get_node(node.identifier).data.truelist = H1.data.truelist
        tree.get_node(node.identifier).data.falselist = H1.data.falselist
    except AttributeError:
        print()
    return


def p47(nodes, tree, node, tokens):
    node1 = tree.create_node('I', node.identifier + ',' + 'I', parent=node.identifier, data=Node.Node(0))
    node2 = tree.create_node('H-', node.identifier + ',' + 'H-', parent=node.identifier, data=Node.Node(0))

    nodes.append(node1)
    get_next(nodes, node, tree, tokens)
    global I1
    I1 = tree.get_node(node1.identifier)
    nodes.append(node2)
    get_next(nodes, node, tree, tokens)

    tree.get_node(node.identifier).data.truelist = tree.get_node(node2.identifier).data.truelist
    tree.get_node(node.identifier).data.falselist = tree.get_node(node2.identifier).data.falselist
    return


def p48(nodes, tree, node, tokens):
    node1 = tree.create_node('and', node.identifier + ',' + 'and', parent=node.identifier, data=Node.Node(0))
    node2 = tree.create_node('M1', node.identifier + ',' + 'M1', parent=node.identifier, data=Node.Node(0))

    node3 = tree.create_node('I', node.identifier + ',' + 'I', parent=node.identifier, data=Node.Node(0))
    node4 = tree.create_node('H-', node.identifier + ',' + 'H-', parent=node.identifier, data=Node.Node(0))

    nodes.append(node1)
    get_next(nodes, node, tree, tokens)
    nodes.append(node2)
    get_next(nodes, node, tree, tokens)
    nodes.append(node3)
    get_next(nodes, node, tree, tokens)
    nodes.append(node4)
    get_next(nodes, node, tree, tokens)

    global I1
    back_patch(I1.truelist, tree.get_node(node2.identifier).data.quad)
    tree.get_node(node.identifier).data.truelist = tree.get_node(node3.identifier).data.truelist
    tree.get_node(node.identifier).data.falselist = I1.falselist + tree.get_node(node3.identifier).data.falselist

    return


def p49(nodes, tree, node, tokens):
    tree.get_node(node.identifier).data.quad = seq
    global I1
    try:
        tree.get_node(node.identifier).data.truelist = I1.data.truelist
        tree.get_node(node.identifier).data.falselist = I1.data.falselist
    except AttributeError:
        print()
    return


def p50(nodes, tree, node, tokens):
    node1 = tree.create_node('not', node.identifier + ',' + 'not', parent=node.identifier, data=Node.Node(0))
    node2 = tree.create_node('B', node.identifier + ',' + 'B', parent=node.identifier, data=Node.Node(0))

    nodes.append(node1)
    get_next(nodes, node, tree, tokens)
    nodes.append(node2)
    get_next(nodes, node, tree, tokens)
    tree.get_node(node.identifier).data.truelist = tree.get_node(node2.identifier).data.falselist
    tree.get_node(node.identifier).data.falselist = tree.get_node(node2.identifier).data.truelist

    return


def p51(nodes, tree, node, tokens):
    node1 = tree.create_node('(', node.identifier + ',' + '(', parent=node.identifier, data=Node.Node(0))
    node2 = tree.create_node('B', node.identifier + ',' + 'B', parent=node.identifier, data=Node.Node(0))
    node3 = tree.create_node(')', node.identifier + ',' + ')', parent=node.identifier, data=Node.Node(0))

    nodes.append(node1)
    get_next(nodes, node, tree, tokens)
    nodes.append(node2)
    get_next(nodes, node, tree, tokens)
    nodes.append(node3)
    get_next(nodes, node, tree, tokens)
    tree.get_node(node.identifier).data.truelist = tree.get_node(node2.identifier).data.truelist
    tree.get_node(node.identifier).data.falselist = tree.get_node(node2.identifier).data.falselist

    return


def p52(nodes, tree, node, tokens):
    node1 = tree.create_node('E', node.identifier + ',' + 'E1', parent=node.identifier, data=Node.Node(0))
    node2 = tree.create_node('relop', node.identifier + ',' + 'relop', parent=node.identifier, data=Node.Node(0))
    node3 = tree.create_node('E', node.identifier + ',' + 'E2', parent=node.identifier, data=Node.Node(0))

    nodes.append(node1)
    get_next(nodes, node, tree, tokens)
    nodes.append(node2)
    get_next(nodes, node, tree, tokens)
    nodes.append(node3)
    get_next(nodes, node, tree, tokens)
    global seq
    tree.get_node(node.identifier).data.truelist = [seq]
    tree.get_node(node.identifier).data.falselist = [seq + 1]
    gen('j' + tree.get_node(node2.identifier).data.val, tree.get_node(node1.identifier).data.addr,
        tree.get_node(node3.identifier).data.addr, '_')
    gen('j', '_', '_', '_')
    return


def p53(nodes, tree, node, tokens):
    node1 = tree.create_node('true', node.identifier + ',' + 'true', parent=node.identifier, data=Node.Node(0))

    nodes.append(node1)
    get_next(nodes, node, tree, tokens)
    tree.get_node(node.identifier).data.truelist = [seq + 1]
    gen('j', '_', '_', '_')

    return


def p54(nodes, tree, node, tokens):
    node1 = tree.create_node('false', node.identifier + ',' + 'false', parent=node.identifier, data=Node.Node(0))

    nodes.append(node1)
    get_next(nodes, node, tree, tokens)
    tree.get_node(node.identifier).data.falselist = [seq + 1]
    gen('j', '_', '_', '_')

    return


def p55(nodes, tree, node, tokens):
    node1 = tree.create_node('<', node.identifier + ',' + '<', parent=node.identifier, data=Node.Node(0))

    nodes.append(node1)
    get_next(nodes, node, tree, tokens)
    tree.get_node(node.identifier).data.val = '<'
    return


def p56(nodes, tree, node, tokens):
    node1 = tree.create_node('<=', node.identifier + ',' + '<=', parent=node.identifier, data=Node.Node(0))

    nodes.append(node1)
    get_next(nodes, node, tree, tokens)
    tree.get_node(node.identifier).data.val = '<='
    return


def p57(nodes, tree, node, tokens):
    node1 = tree.create_node('==', node.identifier + ',' + '==', parent=node.identifier, data=Node.Node(0))

    nodes.append(node1)
    get_next(nodes, node, tree, tokens)
    tree.get_node(node.identifier).data.val = '='
    return


def p58(nodes, tree, node, tokens):
    node1 = tree.create_node('!=', node.identifier + ',' + '!=', parent=node.identifier, data=Node.Node(0))

    nodes.append(node1)
    get_next(nodes, node, tree, tokens)
    tree.get_node(node.identifier).data.val = '!='
    return


def p59(nodes, tree, node, tokens):
    node1 = tree.create_node('>', node.identifier + ',' + '>', parent=node.identifier, data=Node.Node(0))

    nodes.append(node1)
    get_next(nodes, node, tree, tokens)
    tree.get_node(node.identifier).data.val = '>'
    return


def p60(nodes, tree, node, tokens):
    node1 = tree.create_node('>=', node.identifier + ',' + '>=', parent=node.identifier, data=Node.Node(0))

    nodes.append(node1)
    get_next(nodes, node, tree, tokens)
    tree.get_node(node.identifier).data.val = '>='
    return


def p61(nodes, tree, node, tokens):
    node1 = tree.create_node('E', node.identifier + ',' + 'E', parent=node.identifier, data=Node.Node(0))
    node2 = tree.create_node('Elist-', node.identifier + ',' + 'Elist-', parent=node.identifier, data=Node.Node(0))

    nodes.append(node1)
    get_next(nodes, node, tree, tokens)
    global q
    q = [tree.get_node(node1.identifier).data.addr]
    nodes.append(node2)
    get_next(nodes, node, tree, tokens)
    return


def p62(nodes, tree, node, tokens):
    node1 = tree.create_node(',', node.identifier + ',' + ',', parent=node.identifier, data=Node.Node(0))
    node2 = tree.create_node('E', node.identifier + ',' + 'E', parent=node.identifier, data=Node.Node(0))
    node3 = tree.create_node('Elist-', node.identifier + ',' + 'Elist-', parent=node.identifier, data=Node.Node(0))

    nodes.append(node1)
    get_next(nodes, node, tree, tokens)
    nodes.append(node2)
    get_next(nodes, node, tree, tokens)
    nodes.append(node3)
    get_next(nodes, node, tree, tokens)
    global q
    q.append(tree.get_node(node2.identifier).data.addr)
    return


def p63(nodes, tree, node, tokens):
    return


def switchMode(nodes, node, token, tree, tokens):
    global index, seq
    if node.tag == 'Program':
        if token[1][0] in ['proc', 'int', 'float', 'char', 'record', 'id', 'if', 'while', 'call', 'return', 'switch',
                           'for']:
            p1(nodes, tree, node, tokens)
        else:
            print("p1 parsing error")
    elif node.tag == 'M1':
        tree.get_node(node.identifier).data.quad = seq
    elif node.tag == 'M2':
        tree.get_node(node.identifier).data.quad = seq
    elif node.tag == 'P':
        if token[1][0] in ['proc', 'int', 'float', 'char', 'record']:
            p2(nodes, tree, node, tokens)
        elif token[1][0] in ['id', 'if', 'while', 'call', 'return', 'switch', 'for']:
            p3(nodes, tree, node, tokens)
        elif token[1][0] in ['$', '}']:
            p4(nodes, tree, node, tokens)
        else:
            print("P parsing error")
    elif node.tag == 'D':
        if token[1][0] in ['proc']:
            p5(nodes, tree, node, tokens)
        elif token[1][0] in ['int', 'float', 'char']:
            p6(nodes, tree, node, tokens)
        elif token[1][0] in ['record']:
            p7(nodes, tree, node, tokens)
        elif token[1][0] == 'id':
            # index += 1
            pass
        else:
            print("D parsing error")
    elif node.tag == 'A':
        if token[1][0] in ['=']:
            p8(nodes, tree, node, tokens)
        elif token[1][0] in [';']:
            p9(nodes, tree, node, tokens)
        elif token[1][0] in [',']:
            p10(nodes, tree, node, tokens)
        else:
            print("A parsing error")
    elif node.tag == 'M':
        if token[1][0] in ['int', 'float', 'char']:
            p11(nodes, tree, node, tokens)
        elif token[1][0] == ')':
            # index += 1
            pass
        else:
            print("M parsing error")
    elif node.tag == 'M-':
        if token[1][0] in [',']:
            p12(nodes, tree, node, tokens)
        elif token[1][0] in [')']:
            p13(nodes, tree, node, tokens)
        else:
            print("M' parsing error")
    elif node.tag == 'T':
        if token[1][0] in ['int', 'float', 'char']:
            p14(nodes, tree, node, tokens)
        elif token[1][0] == 'id':
            # index += 1
            pass
        else:
            print("T parsing error")
    elif node.tag == 'X':
        if token[1][0] in ['int']:
            p15(nodes, tree, node, tokens)
        elif token[1][0] in ['float']:
            p16(nodes, tree, node, tokens)
        elif token[1][0] in ['char']:
            print('sorry! can\'t assign for char')
        elif token[1][0] == 'id':
            # index += 1
            pass
        else:
            print("X parsing error")
    elif node.tag == 'C':
        if token[1][0] in ['[']:
            p18(nodes, tree, node, tokens)
        elif token[1][0] in ['id']:
            p19(nodes, tree, node, tokens)
        else:
            print("C parsing error")
    elif node.tag == 'S':
        if token[1][0] in ['id']:
            p20(nodes, tree, node, tokens)
        elif token[1][0] in ['if']:
            p21(nodes, tree, node, tokens)
        elif token[1][0] in ['while']:
            p22(nodes, tree, node, tokens)
        elif token[1][0] in ['call']:
            p23(nodes, tree, node, tokens)
        elif token[1][0] in ['return']:
            p24(nodes, tree, node, tokens)
        elif token[1][0] in ['switch']:
            p25(nodes, tree, node, tokens)
        elif token[1][0] in ['for']:
            p26(nodes, tree, node, tokens)
        elif token[1][0] == 'proc':
            # index += 1
            pass
        else:
            print("S parsing error")
    elif node.tag == 'V':
        if token[1][0] in ['++']:
            p27(nodes, tree, node, tokens)
        elif token[1][0] in ['--']:
            p28(nodes, tree, node, tokens)
        elif token[1][0] == ')':
            # index += 1
            pass
        else:
            print("V parsing error")
    elif node.tag == 'N':
        if token[1][0] in ['case']:
            p29(nodes, tree, node, tokens)
        elif token[1][0] in ['default']:
            p30(nodes, tree, node, tokens)
        else:
            print("N parsing error")
            print(token[1][0])
    elif node.tag == 'E':
        if token[1][0] in ['char', 'id', '(', 'digit']:
            p31(nodes, tree, node, tokens)
        elif token[1][0] == ';':
            # index += 1
            pass
        else:
            print("E parsing error")
    elif node.tag == 'E-':
        if token[1][0] in ['+']:
            p32(nodes, tree, node, tokens)
        elif token[1][0] in [';', ',', ')', '<', '<=', '==', '!=', '>', '>=', 'and', 'or', 'then', 'do']:
            p33(nodes, tree, node, tokens)
        else:
            print("E' parsing error")

            print(token[1][0])
    elif node.tag == 'G':
        if token[1][0] in ['char', 'id', '(', 'digit']:
            p34(nodes, tree, node, tokens)
        elif token[1][0] == '+':
            # index += 1
            pass
        else:
            print("G parsing error")
    elif node.tag == 'G-':
        if token[1][0] in ['*']:
            p35(nodes, tree, node, tokens)
        elif token[1][0] in [';', ',', ')', '+', '<', '<=', '==', '!=', '>', '>=', 'and', 'or', 'then', 'do']:
            p36(nodes, tree, node, tokens)
        else:
            print("G' parsing error")
            print(token[1][0])
    elif node.tag == 'F':
        if token[1][0] in ['(']:
            p37(nodes, tree, node, tokens)
        elif token[1][0] in ['digit']:
            p38(nodes, tree, node, tokens)
        elif token[1][0] in ['char']:
            p39(nodes, tree, node, tokens)
        elif token[1][0] in ['id']:
            p40(nodes, tree, node, tokens)
        elif token[1][0] == '=':
            # index += 1
            pass
        else:
            print("F parsing error")
    elif node.tag == 'L':
        if token[1][0] in ['id']:
            p41(nodes, tree, node, tokens)
        elif token[1][0] == '=':
            # index += 1
            pass
        else:
            print("L parsing error")
    elif node.tag == 'L-':
        if token[1][0] in ['[']:
            p42(nodes, tree, node, tokens)
        elif token[1][0] in ['=']:
            p43(nodes, tree, node, tokens)
        else:
            print("L' parsing error")
    elif node.tag == 'B':
        if token[1][0] in ['char', 'id', '(', 'digit', 'not', 'true', 'false']:
            p44(nodes, tree, node, tokens)
        elif token[1][0] == 'then':
            # index += 1
            pass
        else:
            print("B parsing error")
    elif node.tag == 'B-':
        if token[1][0] in ['or']:
            p45(nodes, tree, node, tokens)
        elif token[1][0] in [';', ')', 'and', 'then', 'do']:
            p46(nodes, tree, node, tokens)
        else:
            print("B' parsing error")
    elif node.tag == 'H':
        if token[1][0] in ['char', 'id', '(', 'digit', 'not', 'true', 'false']:
            p47(nodes, tree, node, tokens)
        elif token[1][0] == 'or':
            # index += 1
            pass
        else:
            print("H parsing error")
    elif node.tag == 'H-':
        if token[1][0] in ['and']:
            p48(nodes, tree, node, tokens)
        elif token[1][0] in [';', ')', 'or', 'then', 'do']:
            p49(nodes, tree, node, tokens)
        else:
            print("H' parsing error")
    elif node.tag == 'I':
        if token[1][0] in ['not']:
            p50(nodes, tree, node, tokens)
        elif token[1][0] in ['(']:
            p51(nodes, tree, node, tokens)
        elif token[1][0] in ['char', 'id', 'digit']:
            p52(nodes, tree, node, tokens)
        elif token[1][0] in ['true']:
            p53(nodes, tree, node, tokens)
        elif token[1][0] in ['false']:
            p54(nodes, tree, node, tokens)
        elif token[1][0] == 'and':
            # index += 1
            pass
        else:
            print("I parsing error")
    elif node.tag == 'relop':
        if token[1][0] in ['<']:
            p55(nodes, tree, node, tokens)
        elif token[1][0] in ['<=']:
            p56(nodes, tree, node, tokens)
        elif token[1][0] in ['==']:
            p57(nodes, tree, node, tokens)
        elif token[1][0] in ['!=']:
            p58(nodes, tree, node, tokens)
        elif token[1][0] in ['>']:
            p59(nodes, tree, node, tokens)
        elif token[1][0] in ['>=']:
            p60(nodes, tree, node, tokens)
        elif token[1][0] == '(':
            # index += 1
            pass
        else:
            print("relop parsing error")
    elif node.tag == 'Elist':
        if token[1][0] in ['char', 'id', '(', 'digit']:
            p61(nodes, tree, node, tokens)
        elif token[1][0] == ')':
            # index += 1
            pass
        else:
            print("Elist parsing error")
    elif node.tag == 'Elist-':
        if token[1][0] in [',']:
            p62(nodes, tree, node, tokens)
        elif token[1][0] in [')']:
            p63(nodes, tree, node, tokens)
        else:
            print("Elist' parsing error")
    else:
        if token[1][0] == node.tag:
            if token[1][0] in ['id', 'digit', 'float', 'char']:

                tree.get_node(node.identifier).data.val = token[0]
                tree.get_node(node.identifier).data.addr = token[0]
                index += 1
            else:
                index += 1
        elif token[1][0] == '$':
            pass
        else:
            index += 1
            print("error unknown symbol " + token[1][0] + '\t' + token[0])
            print("needs " + node.tag)


def get_next(nodes, node, tree, tokens):
    global index
    if len(nodes) > 0:

        node = nodes.pop()
        try:
            while tokens[index][1][1] == -1:
                index += 1
            token = tokens[index]

        except IndexError:
            token = []
        switchMode(nodes, node, token, tree, tokens)


def gen(symbal, var1, var2, target):
    three_addr = ''
    four_ele = (symbal, var1, var2, target)
    if symbal == '=':
        three_addr = '' + str(target) + symbal + str(var1)
    elif symbal in '*+':
        three_addr = '' + target + '=' + str(var1) + symbal + str(var2)
    elif symbal == 'j>':
        three_addr = 'if ' + str(var1) + '>' + str(var2) + ' goto ' + str(target)
    elif symbal == 'j<':
        three_addr = 'if ' + str(var1) + '<' + str(var2) + ' goto ' + str(target)
    elif symbal == 'j=':
        three_addr = 'if ' + str(var1) + '=' + str(var2) + ' goto ' + str(target)
    elif symbal == 'j':
        three_addr = 'goto ' + str(target)
    elif symbal == 'param':
        three_addr = 'param ' + str(target)
    elif symbal == 'call':
        params = str(var1)

        three_addr = 'call ' + str(target) + ' , ' + params
    elif symbal == 'return':
        three_addr = 'return_' + str(target)
    else:
        print('unknown symbal : ' + symbal)
    if three_addr == '':
        return
    else:
        global seq
        orders.append((seq, three_addr, four_ele))
        seq += 1


def back_patch(truelist, quad):
    global orders
    for i in truelist:
        myindex = len(orders[i][1]) - 1
        s = orders[i][1]
        s = s[0:myindex] + str(quad)
        orders[i] = (i, s, ('j', '_', '_', str(quad)))


def new_temp():
    global instance
    s = 't' + str(instance)
    instance += 1
    return s


def myprint(order):
    ordersFp = open(path, "w", encoding='UTF-8')
    for i in orders:
        c = i[2]
        ordersFp.write("<{0:^5},{1:^20},({2:^3},{3:^3},{4:^3},{5:^3})>\n".format(i[0], i[1], c[0], c[1], c[2], c[3]))
        print("<{0:^5},{1:^20},({2:^3},{3:^3},{4:^3},{5:^3})>".format(i[0], i[1], c[0], c[1], c[2], c[3]))
    symbolFp = open(symbolPath, "w", encoding='UTF-8')
    for i in symbolTable:
        symbolFp.write("|{0:^5}|{1:^30}|{2:^5}|\n".format(i[0], i[1], i[2]))
        print("|{0:^5}|{1:^30}|{2:^5}|".format(i[0], i[1], i[2]))


def enter(name, the_type, the_offset):
    global symbolTable
    symbolTable.append((name, the_type, the_offset))


def parse(tokens):
    global index, orders, symbolTable
    symbolTable = []
    tree = Tree()
    index = 0
    nodes = []
    node = tree.create_node('Program', 'root', data=Node.Node(0))
    # print(node)
    nodes.append(node)
    while len(nodes) > 0:
        node = nodes.pop()
        try:
            while tokens[index][1][1] == -1:
                index += 1
            token = tokens[index]

        except IndexError:
            token = []
        switchMode(nodes, node, token, tree, tokens)

    tree.show(line_type='ascii-em')
    # tree.save2file('txts/tree.txt')

    myprint(orders)

    return tree
