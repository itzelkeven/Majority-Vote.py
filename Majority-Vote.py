# Kevin Ramos
# CSCI128 - Section E
# Python-MajorityVote
votes = input().split()
al = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
winning_vote = "" 
amount_win = 0
for vote in al:
    count = votes.count(vote)
    if count > len(votes)/2 and count > amount_win:
        amount_win = count
        winning_vote = vote
print(winning_vote)
