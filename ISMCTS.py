from Node import Node
import random
from copy import deepcopy

def ISMCTS(state, itermax):
    rootnode = Node()

    state1 = deepcopy(state)

    for i in range(itermax):
        node = rootnode

        last_reward = 0

        # Selection
        # print(i)
        state1.reset()
        state1 = deepcopy(state)
        # print(state1.get_next_states(), " --------------- ", i)
        count1 = 0
        while count1 < 2 and node.GetUntriedMoves(state1.get_next_states()) == []:
            # print('a')
            node = node.UCBSelectedChild(state1.get_next_states().keys())
            # print('a')
            # print(node)
            reward, game_over = state1.play(node.move[0], node.move[1])
            state1._new_round()
            count1 += 1
            last_reward = reward


        # Expansion

        untriedMoves = node.GetUntriedMoves(state1.get_next_states())
        # print("Untried moves ",untriedMoves)
        if untriedMoves != []:
            m = random.choice(untriedMoves)
            # print("M is ", m)
            reward, game_over = state1.play(m[0], m[1])
            state1._new_round()
            # print("Reward obtained is ", reward)
            # print("Reward is ", reward)
            last_reward = reward
            node = node.AddChild(m)

        # Simulation
        # print("Reached here")
        # print(random.choice(list(state1.get_next_states().keys())))

        count2 = 0
        while count2 < 2 and state1.get_next_states() != {}:

            random_choice = random.choice(list(state1.get_next_states().keys()))
            # print(random_choice)
            reward, game_over = state1.play(random_choice[0], random_choice[1])
            state1._new_round()
            count2 += 1
            last_reward = reward

        # Backpropagation
        while node != None:
            node.Update(state1, last_reward)
            node = node.parentNode


    return max(rootnode.childNodes, key = lambda c: c.visits).move


