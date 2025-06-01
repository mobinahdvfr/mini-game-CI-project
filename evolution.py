from player import Player
import numpy as np
from config import CONFIG
import random
import copy


class Evolution():

    def __init__(self, mode):
        self.mode = mode

    # calculate fitness of players
    def calculate_fitness(self, players, delta_xs):
        for i, p in enumerate(players):
            p.fitness = delta_xs[i]

    def mutate(self, children, p=0.3):
        u = 0
        sigma = 1
        for child in children:
            for weight1 in child.nn.w1:
                if random.random() < p:
                    weight1 += np.random.normal(u, sigma)
            for weight2 in child.nn.w2:
                if random.random() < p:
                    weight2 += np.random.normal(u, sigma)
            for bias1 in child.nn.b1:
                if random.random() < p:
                    bias1 += np.random.normal(u, sigma)
            for bias2 in child.nn.b2:
                if random.random() < p:
                    bias2 += np.random.normal(u, sigma)
        # TODO
        # child: an object of class `Player`
        pass


    def generate_new_population(self, num_players, prev_players=None):

        # in first generation, we create random players
        if prev_players is None:
            return [Player(self.mode) for _ in range(num_players)]

        else:       # making the difference bigger
            fitness_weights = [prev_players[j].fitness ** 4 for j in range(num_players)]
            # random parents    more probability for more fitness
            parents = random.choices(prev_players, weights=fitness_weights, k=num_players)

            children = []
            for p in parents:
                child = copy.deepcopy(p)
                children.append(child)
            self.mutate(children)
            # return children

            # TODO
            # num_players example: 150
            # prev_players: an array of `Player` objects

            # TODO (additional): a selection method other than `fitness proportionate`
            # TODO (additional): implementing crossover

            children2 = []
            for i in range(num_players):
                p1, p2 = random.choices(prev_players, weights=fitness_weights, k=2)
                # w1, b1 from p1 and w2, b2 from p2
                child = copy.deepcopy(p1)
                child.nn.w2 = p2.nn.w2
                child.nn.b2 = p2.nn.b2
                children2.append(child)
            self.mutate(children2)
            return children


    def next_population_selection(self, players, num_players):

            # TODO
            # num_players example: 100
            # players: an array of `Player` objects

            # sort by fitness
            players.sort(key=lambda x: x.fitness, reverse=True)


            # TODO (additional): a selection method other than `top-k`
            # fitness_weights = [players[j].fitness ** 4 for j in range(num_players)]
            # new_player = random.choices(players, weights=fitness_weights, k=num_players)

            # TODO (additional): plotting

            return players[: num_players]
