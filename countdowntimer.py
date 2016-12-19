from time import localtime, sleep

def timer(t):
    while t:
        mins,secs = divmod(t,60)
        print("t =",t)
        print(mins,secs)
        lights=[]
        if t>=60:
            if mins>=128:
                lights.append("green")
                mins=mins-128
            else:
                lights.append(0)
            if mins>=64:
                lights.append("green")
                mins=mins-64
            else:
                lights.append(0)
            if mins>=32:
                lights.append("green")
                mins=mins-32
            else:
                lights.append(0)
            if mins>=16:
                lights.append("green")
                mins=mins-16
            else:
                lights.append(0)
            if mins>=8:
                lights.append("green")
                mins=mins-8
            else:
                lights.append(0)
            if mins>=4:
                lights.append("green")
                mins=mins-4
            else:
                lights.append(0)
            if mins>=2:
                lights.append("green")
                mins=mins-2
            else:
                lights.append(0)
            if mins>=1:
                lights.append("green")
                mins=mins-1
            else:
                lights.append(0)
            print(lights)
        elif t>8:
            if secs>=128:
                lights.append("amber")
                secs=secs-128
            else:
                lights.append(0)
            if secs>=64:
                lights.append("amber")
                secs=secs-64
            else:
                lights.append(0)
            if secs>=32:
                lights.append("amber")
                secs=secs-32
            else:
                lights.append(0)
            if secs>=16:
                lights.append("amber")
                secs=secs-16
            else:
                lights.append(0)
            if secs>=8:
                lights.append("amber")
                secs=secs-8
            else:
                lights.append(0)
            if secs>=4:
                lights.append("amber")
                secs=secs-4
            else:
                lights.append(0)
            if secs>=2:
                lights.append("amber")
                secs=secs-2
            else:
                lights.append(0)
            if secs>=1:
                lights.append("amber")
                secs=secs-1
            else:
                lights.append(0)
            print(lights)
        elif t>=1:
            for i in range(8,0,-1):
                if i>t:
                    lights.append(0)
                else:
                    lights.append("red")
            print(lights)
        t-=1
        sleep(1)

count=int(input("Enter the seconds: "))
timer(count)
    
