def reflex_vaccum_agent(loc,st):
    while st != [0,0]:
        if st[loc] == 1:
            print('Cleaning Room', 'A' if loc == 0 else 'B')
            print('Cleaned Room')
            st[loc] = 0
        else:
            if loc == 0:
                print('Move A -> B')
                loc = 1
            if loc == 1 :
                print('Move B -> A')
                loc = 0

st = eval(input('Enter in form of [A,B] clean = 0, dirty = 1 :' ))
loc = int(input('Start location A/B : 0/1 = '))

reflex_vaccum_agent(loc,st)
