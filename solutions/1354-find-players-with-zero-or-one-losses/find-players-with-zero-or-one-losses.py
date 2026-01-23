class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        from collections import defaultdict
        
        losses = defaultdict(int)
        players = set()
        for winner, loser in matches:
            players.add(winner)
            players.add(loser)
            losses[loser] += 1
        
        no_loss = []
        one_loss = []
        
        for player in sorted(players):
            loss_count = losses[player]
            if loss_count == 0:
                no_loss.append(player)
            elif loss_count == 1:
                one_loss.append(player)
        
        return [no_loss, one_loss]