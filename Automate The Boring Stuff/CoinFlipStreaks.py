import random

def flip_a_coin():
    streakCount = 0
    for manyTimes in range(10000): # Generate 10.000 lists
        result = []
        for listSize in range(100): # Each list with 100 size
            if (random.randint(0, 1)) == 0: # Flip the Coin
                result.append('H')
            else:
                result.append('T')
        streakCount += find_streaks(result)
    return streakCount

    
def find_streaks(list):
    count = 0
    countStreak = 0
    for x in range(len(list)): 
        try:                            
            if list[x] == list[x + 1]:
                count += 1
            else:
                count = 0
            if count == 5:  # If 5 we got a 6 streak
                count = 0
                countStreak += 1
        except IndexError:  
            return countStreak


numberOfStreaks = flip_a_coin()
print(f'Chance of streak: {numberOfStreaks / 100}%')
    