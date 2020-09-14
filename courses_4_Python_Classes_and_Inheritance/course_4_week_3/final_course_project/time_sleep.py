'''The time.sleep(s) function (from the time module) delays execution of the next line of code for s seconds. You’ll
find that we can build a little suspense during gameplay with some well-placed delays. The game can also be easier
for users to understand if not everything happens instantly '''
import time

for x in range(2, 6):
    print('Sleep {} seconds..'.format(x))
    time.sleep(x) # "Sleep" for x seconds
print('Done!')
