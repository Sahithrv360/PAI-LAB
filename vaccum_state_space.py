def travel_room(start):
    visited = set()
    stack = [start]

    print('Cleaninig Room : ',start)

    while stack:
        current = stack.pop()
        
        if current not in visited:
            visited.add(current)
            print("\nEntering Room:", current)

            for neighbour,status in room[current]:
                if status == 1:
                    print("Room", neighbour, "is Dirty → Cleaning...")
                    status = 0
                    print("Room", neighbour, "Cleaned")
                else :
                    print("Room", neighbour, "is already cleane")
            
                stack.append(neighbour)
    
    print("\nAll reachable rooms checked.")

room  = {
    'A' : [('B',1),('C',0),('D',1)],
    'B' : [('D',1)],
    'C' : [('A',0),('D',1),('E',1)],
    'D' : [('A',0),('C',0),('E',1)],
    'E' : [('C',0),('D',1)]
}

travel_room('A')

