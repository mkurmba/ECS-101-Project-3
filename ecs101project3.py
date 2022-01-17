# initialize variables


from random import randrange

def coinFlip():
    points = 0
    turn=0

    while turn<144:
        turn=turn+1
        flip=randrange(0,2)
        # 0 is tails and 1 is heads

        # if points<0:
        #     choice="quarter"
        if -15<points<=-2 and turn<=30:
            choice="quarter"
        elif -12<points<=-5 and 30<turn<=75:
            choice="quarter"
        elif -25<points<0 and 75<turn<100:
            choice="quarter"
        elif -18 <points <= -2 and 125>turn>=100:
            choice = "quarter"
        elif -10<points<=1 and 137>turn>=125:
            choice="quarter"
        elif points<1 and turn>=137:
            choice="quarter"
        else:
            choice="dime"


        # add up the points
        if flip == 0 and choice=="quarter":
            points=points-2
        if flip == 1 and choice=="quarter":
            points=points+2
        if flip == 0 and choice=="dime":
            points=points-1
        if flip == 1 and choice=="dime":
            points=points+1

        print("turn: ", turn, points)

    return points


if __name__=="__main__":
    wins=0
    losses=0
    for i in range(100):
        points=coinFlip()

        if points>=1:
            wins=wins+1
        else:
            losses=losses+1

    print("wins: ", wins)
    print("losses: ",losses)