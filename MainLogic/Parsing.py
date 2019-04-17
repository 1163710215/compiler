from treelib import Tree

index = 0


def p1(nodes, tree, node):
    node1 = tree.create_node('P', node.identifier + ',' + 'P', parent=node.identifier)
    nodes.append(node1)
    return


def p2(nodes, tree, node):
    node1 = tree.create_node('D', node.identifier + ',' + 'D', parent=node.identifier)
    node2 = tree.create_node('P', node.identifier + ',' + 'P', parent=node.identifier)

    nodes.append(node2)
    nodes.append(node1)
    return


def p3(nodes, tree, node):
    node1 = tree.create_node('S', node.identifier + ',' + 'S', parent=node.identifier)
    node2 = tree.create_node('P', node.identifier + ',' + 'P', parent=node.identifier)

    nodes.append(node2)
    nodes.append(node1)
    return


def p4(nodes, tree, node):
    return


def p5(nodes, tree, node):
    node1 = tree.create_node('proc', node.identifier + ',' + 'proc', parent=node.identifier)
    node2 = tree.create_node('X', node.identifier + ',' + 'X', parent=node.identifier)
    node3 = tree.create_node('id', node.identifier + ',' + 'id', parent=node.identifier)
    node4 = tree.create_node('(', node.identifier + ',' + '(', parent=node.identifier)
    node5 = tree.create_node('M', node.identifier + ',' + 'M', parent=node.identifier)
    node6 = tree.create_node(')', node.identifier + ',' + ')', parent=node.identifier)
    node7 = tree.create_node('{', node.identifier + ',' + '{', parent=node.identifier)
    node8 = tree.create_node('P', node.identifier + ',' + 'P', parent=node.identifier)
    node9 = tree.create_node('}', node.identifier + ',' + '}', parent=node.identifier)

    nodes.append(node9)
    nodes.append(node8)
    nodes.append(node7)
    nodes.append(node6)
    nodes.append(node5)
    nodes.append(node4)
    nodes.append(node3)
    nodes.append(node2)
    nodes.append(node1)
    return


def p6(nodes, tree, node):
    node1 = tree.create_node('T', node.identifier + ',' + 'T', parent=node.identifier)
    node2 = tree.create_node('id', node.identifier + ',' + 'id', parent=node.identifier)
    node3 = tree.create_node('A', node.identifier + ',' + 'A', parent=node.identifier)
    node4 = tree.create_node(';', node.identifier + ',' + ';', parent=node.identifier)

    nodes.append(node4)
    nodes.append(node3)
    nodes.append(node2)
    nodes.append(node1)
    return


def p7(nodes, tree, node):
    node1 = tree.create_node('record', node.identifier + ',' + 'record', parent=node.identifier)
    node2 = tree.create_node('id', node.identifier + ',' + 'id', parent=node.identifier)
    node3 = tree.create_node('{', node.identifier + ',' + '{', parent=node.identifier)
    node4 = tree.create_node('P', node.identifier + ',' + 'P', parent=node.identifier)
    node5 = tree.create_node('}', node.identifier + ',' + '}', parent=node.identifier)

    nodes.append(node5)
    nodes.append(node4)
    nodes.append(node3)
    nodes.append(node2)
    nodes.append(node1)
    return


def p8(nodes, tree, node):
    node1 = tree.create_node('=', node.identifier + ',' + '=', parent=node.identifier)
    node2 = tree.create_node('F', node.identifier + ',' + 'F', parent=node.identifier)
    node3 = tree.create_node('A', node.identifier + ',' + 'A', parent=node.identifier)

    nodes.append(node3)

    nodes.append(node2)
    nodes.append(node1)
    return


def p9(nodes, tree, node):
    return


def p10(nodes, tree, node):
    node1 = tree.create_node(',', node.identifier + ',' + ',', parent=node.identifier)
    node2 = tree.create_node('id', node.identifier + ',' + 'id', parent=node.identifier)
    node3 = tree.create_node('A', node.identifier + ',' + 'A', parent=node.identifier)

    nodes.append(node3)
    nodes.append(node2)
    nodes.append(node1)
    return


def p11(nodes, tree, node):
    node1 = tree.create_node('X', node.identifier + ',' + 'X', parent=node.identifier)
    node2 = tree.create_node('id', node.identifier + ',' + 'id', parent=node.identifier)
    node3 = tree.create_node('M-', node.identifier + ',' + 'M-', parent=node.identifier)

    nodes.append(node3)
    nodes.append(node2)
    nodes.append(node1)
    return


def p12(nodes, tree, node):
    node1 = tree.create_node(',', node.identifier + ',' + ',', parent=node.identifier)
    node2 = tree.create_node('X', node.identifier + ',' + 'X', parent=node.identifier)
    node3 = tree.create_node('id', node.identifier + ',' + 'id', parent=node.identifier)
    node4 = tree.create_node('M-', node.identifier + ',' + 'M-', parent=node.identifier)

    nodes.append(node4)
    nodes.append(node3)
    nodes.append(node2)
    nodes.append(node1)
    return


def p13(nodes, tree, node):
    return


def p14(nodes, tree, node):
    node1 = tree.create_node('X', node.identifier + ',' + 'X', parent=node.identifier)
    node2 = tree.create_node('C', node.identifier + ',' + 'C', parent=node.identifier)

    nodes.append(node2)
    nodes.append(node1)
    return


def p15(nodes, tree, node):
    node1 = tree.create_node('int', node.identifier + ',' + 'int', parent=node.identifier)

    nodes.append(node1)
    return


def p16(nodes, tree, node):
    node1 = tree.create_node('float', node.identifier + ',' + 'float', parent=node.identifier)

    nodes.append(node1)
    return


def p17(nodes, tree, node):
    node1 = tree.create_node('char', node.identifier + ',' + 'char', parent=node.identifier)

    nodes.append(node1)
    return


def p18(nodes, tree, node):
    node1 = tree.create_node('[', node.identifier + ',' + '[', parent=node.identifier)
    node2 = tree.create_node('digit', node.identifier + ',' + 'digit', parent=node.identifier)
    node3 = tree.create_node(']', node.identifier + ',' + ']', parent=node.identifier)
    node4 = tree.create_node('C', node.identifier + ',' + 'C', parent=node.identifier)

    nodes.append(node4)
    nodes.append(node3)
    nodes.append(node2)
    nodes.append(node1)
    return


def p19(nodes, tree, node):
    return


def p20(nodes, tree, node):
    node1 = tree.create_node('L', node.identifier + ',' + 'L', parent=node.identifier)
    node2 = tree.create_node('=', node.identifier + ',' + '=', parent=node.identifier)
    node3 = tree.create_node('E', node.identifier + ',' + 'E', parent=node.identifier)
    node4 = tree.create_node(';', node.identifier + ',' + ';', parent=node.identifier)

    nodes.append(node4)
    nodes.append(node3)
    nodes.append(node2)
    nodes.append(node1)
    return


def p21(nodes, tree, node):
    node1 = tree.create_node('if', node.identifier + ',' + 'if', parent=node.identifier)
    node2 = tree.create_node('B', node.identifier + ',' + 'B', parent=node.identifier)
    node3 = tree.create_node('then', node.identifier + ',' + 'then', parent=node.identifier)
    node4 = tree.create_node('S', node.identifier + ',' + 'S1', parent=node.identifier)
    node5 = tree.create_node('else', node.identifier + ',' + 'else', parent=node.identifier)
    node6 = tree.create_node('S', node.identifier + ',' + 'S2', parent=node.identifier)

    nodes.append(node6)
    nodes.append(node5)
    nodes.append(node4)
    nodes.append(node3)
    nodes.append(node2)
    nodes.append(node1)
    return


def p22(nodes, tree, node):
    node1 = tree.create_node('while', node.identifier + ',' + 'while', parent=node.identifier)
    node2 = tree.create_node('B', node.identifier + ',' + 'B', parent=node.identifier)
    node3 = tree.create_node('do', node.identifier + ',' + 'do', parent=node.identifier)
    node4 = tree.create_node('S', node.identifier + ',' + 'S', parent=node.identifier)

    nodes.append(node4)
    nodes.append(node3)
    nodes.append(node2)
    nodes.append(node1)
    return


def p23(nodes, tree, node):
    node1 = tree.create_node('call', node.identifier + ',' + 'call', parent=node.identifier)
    node2 = tree.create_node('id', node.identifier + ',' + 'id', parent=node.identifier)
    node3 = tree.create_node('(', node.identifier + ',' + '(', parent=node.identifier)
    node4 = tree.create_node('Elist', node.identifier + ',' + 'Elist', parent=node.identifier)
    node5 = tree.create_node(')', node.identifier + ',' + ')', parent=node.identifier)
    node6 = tree.create_node(';', node.identifier + ',' + ';', parent=node.identifier)

    nodes.append(node6)
    nodes.append(node5)
    nodes.append(node4)
    nodes.append(node3)
    nodes.append(node2)
    nodes.append(node1)
    return


def p24(nodes, tree, node):
    node1 = tree.create_node('return', node.identifier + ',' + 'return', parent=node.identifier)
    node2 = tree.create_node('E', node.identifier + ',' + 'E', parent=node.identifier)
    node3 = tree.create_node(';', node.identifier + ',' + ';', parent=node.identifier)

    nodes.append(node3)
    nodes.append(node2)
    nodes.append(node1)
    return


def p25(nodes, tree, node):
    node1 = tree.create_node('switch', node.identifier + ',' + 'switch', parent=node.identifier)
    node2 = tree.create_node('(', node.identifier + ',' + '(', parent=node.identifier)
    node3 = tree.create_node('id', node.identifier + ',' + 'id', parent=node.identifier)
    node4 = tree.create_node(')', node.identifier + ',' + ')', parent=node.identifier)
    node5 = tree.create_node('{', node.identifier + ',' + '{', parent=node.identifier)
    node6 = tree.create_node('N', node.identifier + ',' + 'N', parent=node.identifier)
    node7 = tree.create_node('default', node.identifier + ',' + 'default', parent=node.identifier)
    node8 = tree.create_node(':', node.identifier + ',' + ':', parent=node.identifier)
    node9 = tree.create_node('S', node.identifier + ',' + 'S', parent=node.identifier)
    node10 = tree.create_node('}', node.identifier + ',' + '}', parent=node.identifier)

    nodes.append(node10)
    nodes.append(node9)
    nodes.append(node8)
    nodes.append(node7)
    nodes.append(node6)
    nodes.append(node5)
    nodes.append(node4)
    nodes.append(node3)
    nodes.append(node2)
    nodes.append(node1)
    return


def p26(nodes, tree, node):
    node1 = tree.create_node('for', node.identifier + ',' + 'for', parent=node.identifier)
    node2 = tree.create_node('(', node.identifier + ',' + '(', parent=node.identifier)
    node3 = tree.create_node('S', node.identifier + ',' + 'S1', parent=node.identifier)
    node4 = tree.create_node('B', node.identifier + ',' + 'B', parent=node.identifier)
    node5 = tree.create_node(';', node.identifier + ',' + ';', parent=node.identifier)
    node6 = tree.create_node('id', node.identifier + ',' + 'id', parent=node.identifier)
    node7 = tree.create_node('V', node.identifier + ',' + 'V', parent=node.identifier)
    node8 = tree.create_node(')', node.identifier + ',' + ')', parent=node.identifier)
    node9 = tree.create_node('{', node.identifier + ',' + '{', parent=node.identifier)
    node10 = tree.create_node('S', node.identifier + ',' + 'S2', parent=node.identifier)
    node11 = tree.create_node('}', node.identifier + ',' + '}', parent=node.identifier)

    nodes.append(node11)
    nodes.append(node10)
    nodes.append(node9)
    nodes.append(node8)
    nodes.append(node7)
    nodes.append(node6)
    nodes.append(node5)
    nodes.append(node4)
    nodes.append(node3)
    nodes.append(node2)
    nodes.append(node1)
    return


def p27(nodes, tree, node):
    node1 = tree.create_node('++', node.identifier + ',' + '++', parent=node.identifier)

    nodes.append(node1)
    return


def p28(nodes, tree, node):
    node1 = tree.create_node('--', node.identifier + ',' + '--', parent=node.identifier)

    nodes.append(node1)
    return


def p29(nodes, tree, node):
    node1 = tree.create_node('case', node.identifier + ',' + 'case', parent=node.identifier)
    node2 = tree.create_node('digit', node.identifier + ',' + 'digit', parent=node.identifier)
    node3 = tree.create_node(':', node.identifier + ',' + ':', parent=node.identifier)
    node4 = tree.create_node('S', node.identifier + ',' + 'S', parent=node.identifier)
    node5 = tree.create_node('N', node.identifier + ',' + 'N', parent=node.identifier)

    nodes.append(node5)
    nodes.append(node4)
    nodes.append(node3)
    nodes.append(node2)
    nodes.append(node1)
    return


def p30(nodes, tree, node):
    return


def p31(nodes, tree, node):
    node1 = tree.create_node('G', node.identifier + ',' + 'G', parent=node.identifier)
    node2 = tree.create_node('E-', node.identifier + ',' + 'E-', parent=node.identifier)

    nodes.append(node2)
    nodes.append(node1)
    return


def p32(nodes, tree, node):
    node1 = tree.create_node('+', node.identifier + ',' + '+', parent=node.identifier)
    node2 = tree.create_node('G', node.identifier + ',' + 'G', parent=node.identifier)
    node3 = tree.create_node('E-', node.identifier + ',' + 'E-', parent=node.identifier)

    nodes.append(node3)
    nodes.append(node2)
    nodes.append(node1)
    return


def p33(nodes, tree, node):
    return


def p34(nodes, tree, node):
    node1 = tree.create_node('F', node.identifier + ',' + 'F', parent=node.identifier)
    node2 = tree.create_node('G-', node.identifier + ',' + 'G-', parent=node.identifier)

    nodes.append(node2)
    nodes.append(node1)
    return


def p35(nodes, tree, node):
    node1 = tree.create_node('*', node.identifier + ',' + '*', parent=node.identifier)
    node2 = tree.create_node('F', node.identifier + ',' + 'F', parent=node.identifier)
    node3 = tree.create_node('G-', node.identifier + ',' + 'G-', parent=node.identifier)

    nodes.append(node3)
    nodes.append(node2)
    nodes.append(node1)
    return


def p36(nodes, tree, node):
    return


def p37(nodes, tree, node):
    node1 = tree.create_node('(', node.identifier + ',' + '(', parent=node.identifier)
    node2 = tree.create_node('E', node.identifier + ',' + 'E', parent=node.identifier)

    node3 = tree.create_node(')', node.identifier + ',' + ')', parent=node.identifier)

    nodes.append(node3)
    nodes.append(node2)
    nodes.append(node1)
    return


def p38(nodes, tree, node):
    node1 = tree.create_node('digit', node.identifier + ',' + 'digit', parent=node.identifier)

    nodes.append(node1)
    return


def p39(nodes, tree, node):
    node1 = tree.create_node('char', node.identifier + ',' + 'char', parent=node.identifier)

    nodes.append(node1)
    return


def p40(nodes, tree, node):
    node1 = tree.create_node('id', node.identifier + ',' + 'id', parent=node.identifier)

    nodes.append(node1)
    return


def p41(nodes, tree, node):
    node1 = tree.create_node('id', node.identifier + ',' + 'id', parent=node.identifier)
    node2 = tree.create_node('L-', node.identifier + ',' + 'L-', parent=node.identifier)

    nodes.append(node2)
    nodes.append(node1)
    return


def p42(nodes, tree, node):
    node1 = tree.create_node('[', node.identifier + ',' + '[', parent=node.identifier)
    node2 = tree.create_node('digit', node.identifier + ',' + 'digit', parent=node.identifier)
    node3 = tree.create_node(']', node.identifier + ',' + ']', parent=node.identifier)
    node4 = tree.create_node('L-', node.identifier + ',' + 'L-', parent=node.identifier)

    nodes.append(node4)
    nodes.append(node3)
    nodes.append(node2)
    nodes.append(node1)
    return


def p43(nodes, tree, node):
    return


def p44(nodes, tree, node):
    node1 = tree.create_node('H', node.identifier + ',' + 'H', parent=node.identifier)
    node2 = tree.create_node('B-', node.identifier + ',' + 'B-', parent=node.identifier)

    nodes.append(node2)
    nodes.append(node1)
    return


def p45(nodes, tree, node):
    node1 = tree.create_node('or', node.identifier + ',' + 'or', parent=node.identifier)
    node2 = tree.create_node('H', node.identifier + ',' + 'H', parent=node.identifier)
    node3 = tree.create_node('B-', node.identifier + ',' + 'B-', parent=node.identifier)

    nodes.append(node3)
    nodes.append(node2)
    nodes.append(node1)
    return


def p46(nodes, tree, node):
    return


def p47(nodes, tree, node):
    node1 = tree.create_node('I', node.identifier + ',' + 'I', parent=node.identifier)
    node2 = tree.create_node('H-', node.identifier + ',' + 'H-', parent=node.identifier)

    nodes.append(node2)
    nodes.append(node1)
    return


def p48(nodes, tree, node):
    node1 = tree.create_node('and', node.identifier + ',' + 'and', parent=node.identifier)
    node2 = tree.create_node('I', node.identifier + ',' + 'I', parent=node.identifier)
    node3 = tree.create_node('H-', node.identifier + ',' + 'H-', parent=node.identifier)

    nodes.append(node3)
    nodes.append(node2)
    nodes.append(node1)
    return


def p49(nodes, tree, node):
    return


def p50(nodes, tree, node):
    node1 = tree.create_node('not', node.identifier + ',' + 'not', parent=node.identifier)
    node2 = tree.create_node('B', node.identifier + ',' + 'B', parent=node.identifier)

    nodes.append(node2)
    nodes.append(node1)
    return


def p51(nodes, tree, node):
    node1 = tree.create_node('(', node.identifier + ',' + '(', parent=node.identifier)
    node2 = tree.create_node('B', node.identifier + ',' + 'B', parent=node.identifier)
    node3 = tree.create_node(')', node.identifier + ',' + ')', parent=node.identifier)

    nodes.append(node3)
    nodes.append(node2)
    nodes.append(node1)
    return


def p52(nodes, tree, node):
    node1 = tree.create_node('E', node.identifier + ',' + 'E1', parent=node.identifier)
    node2 = tree.create_node('relop', node.identifier + ',' + 'relop', parent=node.identifier)
    node3 = tree.create_node('E', node.identifier + ',' + 'E2', parent=node.identifier)

    nodes.append(node3)
    nodes.append(node2)
    nodes.append(node1)
    return


def p53(nodes, tree, node):
    node1 = tree.create_node('true', node.identifier + ',' + 'true', parent=node.identifier)

    nodes.append(node1)
    return


def p54(nodes, tree, node):
    node1 = tree.create_node('false', node.identifier + ',' + 'false', parent=node.identifier)

    nodes.append(node1)
    return


def p55(nodes, tree, node):
    node1 = tree.create_node('<', node.identifier + ',' + '<', parent=node.identifier)

    nodes.append(node1)
    return


def p56(nodes, tree, node):
    node1 = tree.create_node('<=', node.identifier + ',' + '<=', parent=node.identifier)

    nodes.append(node1)
    return


def p57(nodes, tree, node):
    node1 = tree.create_node('==', node.identifier + ',' + '==', parent=node.identifier)

    nodes.append(node1)
    return


def p58(nodes, tree, node):
    node1 = tree.create_node('!=', node.identifier + ',' + '!=', parent=node.identifier)

    nodes.append(node1)
    return


def p59(nodes, tree, node):
    node1 = tree.create_node('>', node.identifier + ',' + '>', parent=node.identifier)

    nodes.append(node1)
    return


def p60(nodes, tree, node):
    node1 = tree.create_node('>=', node.identifier + ',' + '>=', parent=node.identifier)

    nodes.append(node1)
    return


def p61(nodes, tree, node):
    node1 = tree.create_node('E', node.identifier + ',' + 'E', parent=node.identifier)
    node2 = tree.create_node('Elist-', node.identifier + ',' + 'Elist-', parent=node.identifier)

    nodes.append(node2)
    nodes.append(node1)
    return


def p62(nodes, tree, node):
    node1 = tree.create_node(',', node.identifier + ',' + ',', parent=node.identifier)
    node2 = tree.create_node('E', node.identifier + ',' + 'E', parent=node.identifier)
    node3 = tree.create_node('Elist-', node.identifier + ',' + 'Elist-', parent=node.identifier)

    nodes.append(node3)
    nodes.append(node2)
    nodes.append(node1)
    return


def p63(nodes, tree, node):
    return


def switchMode(nodes, node, token, tree):
    global index
    if node.tag == 'Program':
        if token[1][0] in ['proc', 'int', 'float', 'char', 'record', 'id', 'if', 'while', 'call', 'return', 'switch',
                           'for']:
            p1(nodes, tree, node)
        else:
            print("p1 parsing error")
    elif node.tag == 'P':
        if token[1][0] in ['proc', 'int', 'float', 'char', 'record']:
            p2(nodes, tree, node)
        elif token[1][0] in ['id', 'if', 'while', 'call', 'return', 'switch', 'for']:
            p3(nodes, tree, node)
        elif token[1][0] in ['$', '}']:
            p4(nodes, tree, node)
        else:
            print("P parsing error")
    elif node.tag == 'D':
        if token[1][0] in ['proc']:
            p5(nodes, tree, node)
        elif token[1][0] in ['int', 'float', 'char']:
            p6(nodes, tree, node)
        elif token[1][0] in ['record']:
            p7(nodes, tree, node)
        elif token[1][0] == 'id':
            # index += 1
            pass
        else:
            print("D parsing error")
    elif node.tag == 'A':
        if token[1][0] in ['=']:
            p8(nodes, tree, node)
        elif token[1][0] in [';']:
            p9(nodes, tree, node)
        elif token[1][0] in [',']:
            p10(nodes, tree, node)
        else:
            print("A parsing error")
    elif node.tag == 'M':
        if token[1][0] in ['int', 'float', 'char']:
            p11(nodes, tree, node)
        elif token[1][0] == ')':
            # index += 1
            pass
        else:
            print("M parsing error")
    elif node.tag == 'M-':
        if token[1][0] in [',']:
            p12(nodes, tree, node)
        elif token[1][0] in [')']:
            p13(nodes, tree, node)
        else:
            print("M' parsing error")
    elif node.tag == 'T':
        if token[1][0] in ['int', 'float', 'char']:
            p14(nodes, tree, node)
        elif token[1][0] == 'id':
            # index += 1
            pass
        else:
            print("T parsing error")
    elif node.tag == 'X':
        if token[1][0] in ['int']:
            p15(nodes, tree, node)
        elif token[1][0] in ['float']:
            p16(nodes, tree, node)
        elif token[1][0] in ['char']:
            print('sorry! can\'t assign for char')
        elif token[1][0] == 'id':
            # index += 1
            pass
        else:
            print("X parsing error")
    elif node.tag == 'C':
        if token[1][0] in ['[']:
            p18(nodes, tree, node)
        elif token[1][0] in ['id']:
            p19(nodes, tree, node)
        else:
            print("C parsing error")
    elif node.tag == 'S':
        if token[1][0] in ['id']:
            p20(nodes, tree, node)
        elif token[1][0] in ['if']:
            p21(nodes, tree, node)
        elif token[1][0] in ['while']:
            p22(nodes, tree, node)
        elif token[1][0] in ['call']:
            p23(nodes, tree, node)
        elif token[1][0] in ['return']:
            p24(nodes, tree, node)
        elif token[1][0] in ['switch']:
            p25(nodes, tree, node)
        elif token[1][0] in ['for']:
            p26(nodes, tree, node)
        elif token[1][0] == 'proc':
            # index += 1
            pass
        else:
            print("S parsing error")
    elif node.tag == 'V':
        if token[1][0] in ['++']:
            p27(nodes, tree, node)
        elif token[1][0] in ['--']:
            p28(nodes, tree, node)
        elif token[1][0] == ')':
            # index += 1
            pass
        else:
            print("V parsing error")
    elif node.tag == 'N':
        if token[1][0] in ['case']:
            p29(nodes, tree, node)
        elif token[1][0] in ['default']:
            p30(nodes, tree, node)
        else:
            print("N parsing error")
    elif node.tag == 'E':
        if token[1][0] in ['char', 'id', '(', 'digit']:
            p31(nodes, tree, node)
        elif token[1][0] == ';':
            # index += 1
            pass
        else:
            print("E parsing error")
    elif node.tag == 'E-':
        if token[1][0] in ['+']:
            p32(nodes, tree, node)
        elif token[1][0] in [';', ',', ')', '<', '<=', '==', '!=', '>', '>=', 'and', 'or', 'then', 'do']:
            p33(nodes, tree, node)
        else:
            print("E' parsing error")
    elif node.tag == 'G':
        if token[1][0] in ['char', 'id', '(', 'digit']:
            p34(nodes, tree, node)
        elif token[1][0] == '+':
            # index += 1
            pass
        else:
            print("G parsing error")
    elif node.tag == 'G-':
        if token[1][0] in ['*']:
            p35(nodes, tree, node)
        elif token[1][0] in [';', ',', ')', '+', '<', '<=', '==', '!=', '>', '>=', 'and', 'or', 'then', 'do']:
            p36(nodes, tree, node)
        else:
            print("G' parsing error")
    elif node.tag == 'F':
        if token[1][0] in ['(']:
            p37(nodes, tree, node)
        elif token[1][0] in ['digit']:
            p38(nodes, tree, node)
        elif token[1][0] in ['char']:
            p39(nodes, tree, node)
        elif token[1][0] in ['id']:
            p40(nodes, tree, node)
        elif token[1][0] == '=':
            # index += 1
            pass
        else:
            print("F parsing error")
    elif node.tag == 'L':
        if token[1][0] in ['id']:
            p41(nodes, tree, node)
        elif token[1][0] == '=':
            # index += 1
            pass
        else:
            print("L parsing error")
    elif node.tag == 'L-':
        if token[1][0] in ['[']:
            p42(nodes, tree, node)
        elif token[1][0] in ['=']:
            p43(nodes, tree, node)
        else:
            print("L' parsing error")
    elif node.tag == 'B':
        if token[1][0] in ['char', 'id', '(', 'digit', 'not', 'true', 'false']:
            p44(nodes, tree, node)
        elif token[1][0] == 'then':
            # index += 1
            pass
        else:
            print("B parsing error")
    elif node.tag == 'B-':
        if token[1][0] in ['or']:
            p45(nodes, tree, node)
        elif token[1][0] in [';', ')', 'and', 'then', 'do']:
            p46(nodes, tree, node)
        else:
            print("B' parsing error")
    elif node.tag == 'H':
        if token[1][0] in ['char', 'id', '(', 'digit', 'not', 'true', 'false']:
            p47(nodes, tree, node)
        elif token[1][0] == 'or':
            # index += 1
            pass
        else:
            print("H parsing error")
    elif node.tag == 'H-':
        if token[1][0] in ['and']:
            p48(nodes, tree, node)
        elif token[1][0] in [';', ')', 'or', 'then', 'do']:
            p49(nodes, tree, node)
        else:
            print("H' parsing error")
    elif node.tag == 'I':
        if token[1][0] in ['not']:
            p50(nodes, tree, node)
        elif token[1][0] in ['(']:
            p51(nodes, tree, node)
        elif token[1][0] in ['char', 'id', 'digit']:
            p52(nodes, tree, node)
        elif token[1][0] in ['true']:
            p53(nodes, tree, node)
        elif token[1][0] in ['false']:
            p54(nodes, tree, node)
        elif token[1][0] == 'and':
            # index += 1
            pass
        else:
            print("I parsing error")
    elif node.tag == 'relop':
        if token[1][0] in ['<']:
            p55(nodes, tree, node)
        elif token[1][0] in ['<=']:
            p56(nodes, tree, node)
        elif token[1][0] in ['==']:
            p57(nodes, tree, node)
        elif token[1][0] in ['!=']:
            p58(nodes, tree, node)
        elif token[1][0] in ['>']:
            p59(nodes, tree, node)
        elif token[1][0] in ['>=']:
            p60(nodes, tree, node)
        elif token[1][0] == '(':
            # index += 1
            pass
        else:
            print("relop parsing error")
    elif node.tag == 'Elist':
        if token[1][0] in ['char', 'id', '(', 'digit']:
            p61(nodes, tree, node)
        elif token[1][0] == ')':
            # index += 1
            pass
        else:
            print("Elist parsing error")
    elif node.tag == 'Elist-':
        if token[1][0] in [',']:
            p62(nodes, tree, node)
        elif token[1][0] in [')']:
            p63(nodes, tree, node)
        else:
            print("Elist' parsing error")
    else:
        if token[1][0] == node.tag:
            if token[1][0] in ['id', 'digit', 'float', 'char']:
                tree.get_node(node.identifier).data = token[0]
                index += 1
            else:
                index += 1
        elif token[1][0]=='$':
            pass
        else:
            index += 1
            print("error unknown symbol " + token[1][0]+'\t'+token[0])
            print("needs " + node.tag)


def parse(tokens):
    global index
    tree = Tree()
    index = 0
    nodes = []
    node = tree.create_node('Program', 'root')
    # print(node)
    nodes.append(node)
    while len(nodes) > 0:
        node = nodes.pop()
        try:
            token = tokens[index]
        except IndexError:
            token = []
        switchMode(nodes, node, token, tree)

    tree.show(line_type='ascii-em')
    tree.save2file('txts/tree.txt')

    return tree
