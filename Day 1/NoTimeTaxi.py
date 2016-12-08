puzzle_input = ['R4', 'R3', 'R5', 'L3', 'L5', 'R2', 'L2', 'R5', 'L2', 'R5', 'R5',
                'R5', 'R1', 'R3', 'L2', 'L2', 'L1', 'R5', 'L3', 'R1', 'L2', 'R1',
                'L3', 'L5', 'L1', 'R3', 'L4', 'R2', 'R4', 'L3', 'L1', 'R4', 'L4', 
                'R3', 'L5', 'L3', 'R188', 'R4', 'L1', 'R48', 'L5', 'R4', 'R71', 
                'R3', 'L2', 'R188', 'L3', 'R2', 'L3', 'R3', 'L5', 'L1', 'R1', 
                'L2', 'L4', 'L2', 'R5', 'L3', 'R3', 'R3', 'R4', 'L3', 'L4', 'R5', 
                'L4', 'L4', 'R3', 'R4', 'L4', 'R1', 'L3', 'L1', 'L1', 'R4', 'R1', 
                'L4', 'R1', 'L1', 'L3', 'R2', 'L2', 'R2', 'L1', 'R5', 'R3', 'R4', 
                'L5', 'R2', 'R5', 'L5', 'R1', 'R2', 'L1', 'L3', 'R3', 'R1', 'R3', 
                'L4', 'R4', 'L4', 'L1', 'R1', 'L2', 'L2', 'L4', 'R1', 'L3', 'R4', 
                'L2', 'R3', 'L1', 'L5', 'R4', 'R5', 'R2', 'R5', 'R1', 'R5', 'R1', 
                'R3', 'L3', 'L2', 'L2', 'L5', 'R2', 'L2', 'R5', 'R5', 'L2', 'R3', 
                'L5', 'R5', 'L2', 'R4', 'R2', 'L1', 'R3', 'L5', 'R3', 'R2', 'R5', 
                'L1', 'R3', 'L2', 'R2', 'R1']

blocks = {'x': 0,
          'y': 0,
          'z': 0 
         }

direction = {0 : ('x', 1),
             1 : ('y', 1),
             2 : ('x', -1),
             3 : ('y', -1)}


for i in puzzle_input:
    if i[0] == "R":
        if blocks['z'] == 3:
            blocks['z'] = 0
        else:
            blocks['z'] += 1
    if i[0] == "L":
        if blocks['z'] == 0:
            blocks['z'] = 3
        else:
            blocks['z'] += -1
    for x in range(int(i[1:])):
        print(blocks)
        blocks[direction[blocks['z']][0]] += direction[blocks['z']][1]

distance = abs(blocks['x']) + abs(blocks['y'])

print("Easter Bunny HQ is {} blocks away".format(distance))
