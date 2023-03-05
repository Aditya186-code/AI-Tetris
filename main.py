from ISMCTS import ISMCTS
from tetris import Tetris

env = Tetris()
env.render()
game_over = False

render = True
while(not game_over):



    best_move = ISMCTS(env, 500)
    
    reward, game_over = env.play(best_move[0], best_move[1], render)
    # game_over = True
    env._new_round()
    # print(best_move)
    
