from math import *

class Node:
    def __init__(self, move = None, parent = None):
        self.move = move
        self.parentNode = parent
        self.childNodes = []
        self.wins = 0
        self.visits = 0
        self.avails = 1

    def GetUntriedMoves(self, legalMoves):
        triedMoves = [child.move for child in self.childNodes]
        return [move for move in legalMoves if move not in triedMoves]

    
    def AddChild(self, m):
        n = Node(move = m, parent = self)
        self.childNodes.append(n)

        return n

    def Update(self, terminalState, reward):
        self.visits += 1
        
        #as per reward update wins
        # if reward:
        #     self.wins += 0
        # else:
        #     self.wins += 0
        self.wins += reward

    def UCBSelectedChild(self, legalMoves,exploration = 1.414):
        legalChildren = [child for child in self.childNodes if child.move in legalMoves]

        s = max(legalChildren, key = lambda c : float(c.wins) / float(c.visits) + exploration * sqrt(log(c.avails) / float(c.visits)))

        for child in legalChildren:
            child.avails += 1
        

        return s