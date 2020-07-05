winners = ['Alice Munro', 'Alvin E. Roth', 'Kazuo Ishiguro', 'Malala Yousafzai', 'Rainer Weiss', 'Youyou Tu']
z_winners=[]
winners.sort(reverse=True)
for x in range(len(winners)):
    z_winners.append(winners[x])

print(z_winners)