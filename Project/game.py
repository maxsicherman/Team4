 ## Melody Simon-says prototype ##
import os
import random
import IMU_main
import medium_mode_DandF as speech
import camera
import IMU_main
import camera
import medium_mode_DandF as speech

modes = ['Keyboard', 'Camera', 'Speech', 'IMU']

class Game:
    def __init__(self, id):
        self.boardH = 2
        self.boardW = 2
        self.board = self.makeBoard(self.boardH, self.boardW)
        self.currPlayer = 0
        self.rolled = False
        self.phase = 'board'
        self.went = False
        self.correct = False
        self.ready = False
        self.id = id
        self.numPlayers = 2
        self.spots = [0 for i in range(self.numPlayers)]
        self.currAnswer = ''
        self.currRoll = 0
        self.currMode = 'Keyboard'
        self.sol = ''
        self.melody = [0]
        self.winner = 0
        


    def makeBoard(self, h, w):
        board = [0 for i in range(w*h)]
        # for i in range(h):
        #     for j in range(w):
        #         board[8*i+j] = random.randint(0, 3)
        return(board)
    

    def newRoll(self, num):
        num = int(num)
        self.currRoll = num
        self.rolled = True
        if self.spots[self.currPlayer] + self.currRoll < len(self.board):
            self.currMode = modes[self.board[self.spots[self.currPlayer] + self.currRoll]]
        else:
            self.currMode = modes[self.board[-1]]
        self.makeSound(self.currMode)
    

    def makeSound(self, mode):
        print(self.currRoll)
        self.sol = ''
        self.melody = [0 for i in range(self.currRoll)]
        for i in range(self.currRoll):
            self.melody[i] = random.randint(0, 6) # 6 is number of sounds
            self.sol += str(self.melody[i])
        if mode == 'Keyboard' or mode == 'IMU':
            relation = [0 for i in range(self.currRoll - 1)]
            for i in range(self.currRoll - 1):
                relation[i] = self.melody[i+1] - self.melody[i]
            self.sol = ''
            for i in range(len(relation)):
                if relation[i] < 0:
                    self.sol += 'v'
                elif relation[i] == 0:
                    self.sol += '>'
                elif relation[i] > 0:
                    self.sol += '^'

        print(self.melody)
        print(self.sol)


    def nextPhase(self, phase):
        if phase == 'board':
            print('dice')
            self.phase = 'dice'

        if phase == 'dice':
            print('turn')
            self.phase = 'turn'
  
        if phase == 'turn':
            print('resetting')
            self.reset()
            self.phase = 'board'
        
        if phase == 'end':
            self.phase = 'end'
        
    def getPhase(self):
        return(self.phase)

    def move(self):
        self.spots[self.currPlayer] += self.currRoll
        if self.spots[self.currPlayer] >= len(self.board):
            self.phase = 'end'
            self.winner = self.currPlayer
        self.correct = False

    def reset(self):
        self.rolled = False
        self.went = False
        self.correct = False
        self.currPlayer = (self.currPlayer+1)%self.numPlayers

    def newGame(self):
        self.rolled = False
        self.went = False
        self.correct = False
        self.currPlayer = 0

    def getP1(self):
        return(self.p1)

    def getP2(self):
        return(self.p2)
    
    def printMelody(self):
        print(self.melody)
        return


    def play(self):
        print(self.currMode)
        if self.currMode == 'Keyboard':
            self.currAnswer = input('^, >, v')
        elif self.currMode == 'IMU':
            self.currAnswer = IMU_main.main()
        elif self.currMode == 'Camera':
            self.currAnswer = camera.camera(self.currRoll)
        elif self.currMode == 'Speech':
            self.currAnswer = speech.speechRecognition()
        return(self.currAnswer)
            

    def check(self, ans):
        if ans == self.sol:
            self.correct = True
            print("Correct!")
        else:
            print("Wrong")
        self.went = True

    def getAns(self, player):
        return(self.answers[player])


    def connected(self):
        return self.ready
    
    def resetWent(self):
        self.went = [False, False]
        self.p1 = False
        self.p2 = False
