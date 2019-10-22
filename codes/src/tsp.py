import math

import numpy as np

x = [64, 94, 56, 54, 98, 82, 18, 0, 12, 42, 9, 54, 69, 29, 65, 75, 18, 16, 95, 8]
y = [41, 77, 36, 33, 20, 83, 25, 47, 1, 60, 86, 11, 34, 98, 18, 31, 97, 2, 25, 74]


class TSP(object):
    allnum = 1
    crossrate = 0.1
    changerate = 0.1
    citynum = 20
    pop = np.array([])
    best_dist = 10000000000
    best_one = 99
    dist = []
    fitness = []

    def __init__(self, allnum, crossrate, changerate):
        self.allnum = allnum
        self.crossrate = crossrate
        self.changerate = changerate
        self.best_one = 0
        self.best_dist = 1000000000
        self.dist = []
        self.fitness = []
        self.pop = np.array([])
        for i in range(int(self.allnum)):
            self.dist.append(0)
            self.fitness.append(0)

    def Print(self):
        print(self.pop[self.best_one])

    def crate_pop(self, size):
        pop = []
        tem = []
        for i in range(int(self.citynum)):
            tem.append(i)
        for i in range(int(size)):
            gene = tem
            np.random.shuffle(gene)
            tem = gene
            #   print(tem)
            pop.append([])
            for j in gene:
                pop[i].append(j)
        return np.array(pop)

    def set(self):
        self.pop = self.crate_pop(self.allnum)

    @staticmethod
    def get_dist(a, b, c, d):
        return math.sqrt((b - a) * (b - a) + (d - c) * (d - c))

    def get_gendist(self, gen):
        dist = 0
        for i in range(self.citynum):
            dist += self.get_dist(x[gen[i]], x[gen[i - 1]], y[gen[i]], y[gen[i - 1]])
        return dist

    def sum(self):
        flag = 0
        for i in range(int(self.allnum)):
            dist = self.get_gendist(self.pop[i])
            self.dist[i] = dist
            if dist < self.best_dist:
                self.best_dist = dist
                self.best_one = i
                flag = 1
        for i in range(int(self.allnum)):
            self.fitness[i] = int(self.best_dist / self.dist[i])
        w = np.argmin(self.fitness)
        w = int(w)
        # print(w)
        if flag == 0:
            self.pop[w] = self.pop[self.best_one]
            self.dist[w] = self.dist[self.best_one]
            self.fitness[w] = self.fitness[self.best_one]

    def play(self, parent1, parent2):
        if np.random.rand() > float(self.crossrate):
            return parent1
        index1 = np.random.randint(0, int(self.citynum) - 1)
        index2 = np.random.randint(index1, int(self.citynum) - 1)
        tem = parent2[index1:index2]
        newgene = []
        glen = 0
        for i in parent2:
            if glen == index1:
                newgene.extend(tem)
            if i not in tem:
                newgene.append(i)
            glen += 1
        newgene = np.array(newgene)
        return newgene

    @staticmethod
    def reverse(gene, i, j):
        while i < j:
            k = gene[i]
            gene[i] = gene[j]
            gene[j] = k
            i += 1
            j -= 1
        return gene

    def change(self, gene):
        if np.random.rand() > float(self.changerate):
            return gene
        index1 = np.random.randint(0, int(self.citynum) - 1)
        index2 = np.random.randint(index1, int(self.citynum) - 1)
        # print(index1,index2)
        newgene = self.reverse(gene, index1, index2)
        return newgene

    def select(self, pop):
        av = np.median(self.fitness, axis=0)
        for i in range(int(self.allnum)):
            if self.fitness[i] < av and i != self.best_one:
                pi = self.change(self.pop[i])
                pop[i] = np.copy(pi)
        return pop

    @staticmethod
    def exchange(gen, i, j):
        neogene = np.copy(gen)
        a = neogene[i]
        neogene[i] = neogene[j]
        neogene[j] = a
        return neogene

    def EO(self, best):
        maxgen = np.copy(self.pop[best])
        for i in range(self.citynum):
            j = i + 1
            while j < self.citynum:
                gen = self.exchange(maxgen, i, j)
                d1 = self.get_gendist(gen)
                d = self.get_gendist(maxgen)
                if d1 < d:
                    maxgen = np.copy(gen)
                j += 1
        return maxgen

    def evolution(self, cishu):
        result = []
        dist = []
        self.sum()
        for i in range(int(cishu)):
            for j in range(int(self.allnum)):
                r = np.random.randint(0, int(self.allnum) - 1)
                if r != j and j != self.best_one:
                    self.pop[j] = self.play(self.pop[j], self.pop[r])
                    self.pop[j] = self.change(self.pop[j])
            self.pop = self.select(self.pop)
            self.EO(self.best_one)
            self.sum()
            result.append([])
            for j in self.pop[self.best_one]:
                result[i].append(j)
            dist.append(self.best_dist)
            # self.Print()
        return result, dist
