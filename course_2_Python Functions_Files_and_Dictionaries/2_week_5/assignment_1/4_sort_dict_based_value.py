'''Given the same dictionary, medals, now sort by the medal count. Save the three countries with the highest medal
count to the list, top_three.'''

medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70}
top=sorted(medals.keys(),key=lambda x:medals[x],reverse=1)
top_three=top[:2]