class Solution(object):
    def matchPlayersAndTrainers(self, players, trainers):
        players.sort()
        trainers.sort()
        j = matches = 0
        for i in range(len(trainers)):
            if j < len(players) and players[j] <= trainers[i]:
                j += 1
                matches += 1
        return matches