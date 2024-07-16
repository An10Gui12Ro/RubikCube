from NodeCubeBits import Cube
from CubeMovementsBits import Cube_movements
from queue import PriorityQueue
from copy import deepcopy
import time #REPORTE 1

class Heuristics:
    @staticmethod
    #This heuristic calculates the distance between the corners (and edges) and the right position where they need to be
    def manhattan_distance_3d(node):
        def __get_bits(face, gb, lb):
            if lb > gb or gb < lb:
                return 0

            mask = ((2 ** (gb + 1) - 1) >> lb) << lb

            return (face & mask) >> lb 
    
        distance = 0
        tuple_of_corners_colors = [('013',1,3,3), ('014',3,3,3), ('023',1,1,3), ('024',3,1,3), ('145',3,3,1), ('135',1,3,1), ('245',3,1,1), ('235'),1,1,1]
        tuple_of_corners = [(''.join(sorted(str(__get_bits(node.cube[0],2,0)) + str(__get_bits(node.cube[1],20,18)) + str(__get_bits(node.cube[3],8,6)))), 1, 3, 3),
                            (''.join(sorted(str(__get_bits(node.cube[0],8,6)) + str(__get_bits(node.cube[1],26,24)) + str(__get_bits(node.cube[4],2,0)))), 3, 3, 3),
                            (''.join(sorted(str(__get_bits(node.cube[0],20,18)) + str(__get_bits(node.cube[2],2,0)) + str(__get_bits(node.cube[3],26,24)))), 1, 1, 3),
                            (''.join(sorted(str(__get_bits(node.cube[0],26,24)) + str(__get_bits(node.cube[2],8,6)) + str(__get_bits(node.cube[4],20,18)))), 3, 1, 3),
                            (''.join(sorted(str(__get_bits(node.cube[5],2,0)) + str(__get_bits(node.cube[1],8,6)) + str(__get_bits(node.cube[4],8,6)))), 3, 3, 1),
                            (''.join(sorted(str(__get_bits(node.cube[5],8,6)) + str(__get_bits(node.cube[1],2,0)) + str(__get_bits(node.cube[3],2,0)))), 1, 3, 1),
                            (''.join(sorted(str(__get_bits(node.cube[5],20,18)) + str(__get_bits(node.cube[2],26,24)) + str(__get_bits(node.cube[4],26,24)))), 3, 1, 1),
                            (''.join(sorted(str(__get_bits(node.cube[5],26,24)) + str(__get_bits(node.cube[2],20,18)) + str(__get_bits(node.cube[3],20,18)))), 1, 1, 1)]
        for i in range(8):
            for j in range(8):
                if tuple_of_corners[i][0] == tuple_of_corners_colors[j][0]:
                    distance += abs(tuple_of_corners[i][1]-tuple_of_corners_colors[j][1])+abs(tuple_of_corners[i][2]-tuple_of_corners_colors[j][2])+abs(tuple_of_corners[i][3]-tuple_of_corners_colors[j][3])

        tuple_of_edges_colors = [('01',2,3,3), ('14',3,3,2), ('15',2,3,1), ('13',1,3,2), ('03',1,2,3), ('04',3,2,3), ('45',3,2,1), ('35',1,2,1),
                                 ('02',2,1,3), ('24',3,1,2), ('25',2,1,1), ('23',1,1,2)]
        tuple_of_edges = [(''.join(sorted(str(__get_bits(node.cube[0],5,3)) + str(__get_bits(node.cube[1],23,21)))), 2, 3, 3),
                            (''.join(sorted(str(__get_bits(node.cube[4],5,3)) + str(__get_bits(node.cube[1],17,15)))), 3, 3, 2),
                            (''.join(sorted(str(__get_bits(node.cube[5],5,3)) + str(__get_bits(node.cube[1],5,3)))), 2, 3, 1),
                            (''.join(sorted(str(__get_bits(node.cube[3],5,3)) + str(__get_bits(node.cube[1],11,9)))), 1, 3, 2),
                            (''.join(sorted(str(__get_bits(node.cube[0],11,9)) + str(__get_bits(node.cube[3],17,15)))), 1, 2, 3),
                            (''.join(sorted(str(__get_bits(node.cube[0],17,15)) + str(__get_bits(node.cube[4],11,9)))), 3, 2, 3),
                            (''.join(sorted(str(__get_bits(node.cube[5],11,9)) + str(__get_bits(node.cube[4],17,15)))), 3, 2, 1),
                            (''.join(sorted(str(__get_bits(node.cube[5],17,15)) + str(__get_bits(node.cube[3],11,9)))), 1, 2, 1),
                            (''.join(sorted(str(__get_bits(node.cube[0],23,21)) + str(__get_bits(node.cube[2],5,3)))), 2, 1, 3),
                            (''.join(sorted(str(__get_bits(node.cube[4],23,21)) + str(__get_bits(node.cube[2],17,15)))), 3, 1, 2),
                            (''.join(sorted(str(__get_bits(node.cube[5],23,21)) + str(__get_bits(node.cube[2],23,21)))), 2, 1, 1),
                            (''.join(sorted(str(__get_bits(node.cube[3],23,21)) + str(__get_bits(node.cube[2],11,9)))), 1, 1, 2)]
        for i in range(12):
            for j in range(12):
                if tuple_of_edges[i][0] == tuple_of_edges_colors[j][0]:
                    distance += abs(tuple_of_edges[i][1]-tuple_of_edges_colors[j][1])+abs(tuple_of_edges[i][2]-tuple_of_edges_colors[j][2])+abs(tuple_of_edges[i][3]-tuple_of_edges_colors[j][3])

        return (distance/8)

    #c_e_2
    @staticmethod
    def intento_1(node):
        sum = 0
        def __get_bits(face, gb, lb):
            if lb > gb or gb < lb:
                return 0

            mask = ((2 ** (gb + 1) - 1) >> lb) << lb

            return (face & mask) >> lb
        c_0 = __get_bits(node.cube[0], 14, 12)
        c_1 = __get_bits(node.cube[1], 14, 12)
        c_2 = __get_bits(node.cube[2], 14, 12)
        c_3 = __get_bits(node.cube[3], 14, 12)
        c_4 = __get_bits(node.cube[4], 14, 12)
        c_5 = __get_bits(node.cube[5], 14, 12)

        if __get_bits(node.cube[0],2,0) != c_0 or __get_bits(node.cube[1],20,18) != c_1 or __get_bits(node.cube[3],8,6) != c_3:
            sum += 1
        if __get_bits(node.cube[0],8,6) != c_0 or __get_bits(node.cube[1],26,24) != c_1 or __get_bits(node.cube[4],2,0) != c_4:
            sum += 1
        if __get_bits(node.cube[0],20,18) != c_0 or __get_bits(node.cube[3],26,24) != c_3 or __get_bits(node.cube[2],2,0) != c_2:
            sum += 1
        if __get_bits(node.cube[0],26,24) != c_0 or __get_bits(node.cube[4],20,18) != c_4 or __get_bits(node.cube[2],8,6) != c_2:
            sum += 1
        if __get_bits(node.cube[5],2,0) != c_5 or __get_bits(node.cube[4],8,6) != c_4 or __get_bits(node.cube[1],8,6) != c_1:
            sum += 1
        if __get_bits(node.cube[5],8,6) != c_5 or __get_bits(node.cube[3],2,0) != c_3 or __get_bits(node.cube[1],2,0) != c_1:
            sum += 1
        if __get_bits(node.cube[5],20,18) != c_5 or __get_bits(node.cube[4],26,24) != c_4 or __get_bits(node.cube[2],26,24) != c_2:
            sum += 1
        if __get_bits(node.cube[5],26,24) != c_5 or __get_bits(node.cube[3],20,18) != c_3 or __get_bits(node.cube[2],20,18) != c_2:
            sum += 1
        if __get_bits(node.cube[0],5,3) != c_0 or __get_bits(node.cube[1],23,21) != c_1:
            sum += 1
        if __get_bits(node.cube[4],5,3) != c_4 or __get_bits(node.cube[1],17,15) != c_1:
            sum += 1
        if __get_bits(node.cube[5],5,3) != c_5 or __get_bits(node.cube[1],5,3) != c_1:
            sum += 1
        if __get_bits(node.cube[3],5,3) != c_3 or __get_bits(node.cube[1],11,9) != c_1:
            sum += 1
        if __get_bits(node.cube[0],11,9) != c_0 or __get_bits(node.cube[3],17,15) != c_3:
            sum += 1
        if __get_bits(node.cube[0],17,15) != c_0 or __get_bits(node.cube[4],11,9) != c_4:
            sum += 1
        if __get_bits(node.cube[5],11,9) != c_5 or __get_bits(node.cube[4],17,15) != c_4:
            sum += 1
        if __get_bits(node.cube[5],17,15) != c_5 or __get_bits(node.cube[3],11,9) != c_3:
            sum += 1
        if __get_bits(node.cube[0],23,21) != c_0 or __get_bits(node.cube[2],5,3) != c_2:
            sum += 1
        if __get_bits(node.cube[4],23,21) != c_4 or __get_bits(node.cube[2],17,15) != c_2:
            sum += 1
        if __get_bits(node.cube[5],23,21) != c_5 or __get_bits(node.cube[2],23,21) != c_2:
            sum += 1
        if __get_bits(node.cube[3],23,21) != c_3 or __get_bits(node.cube[2],11,9) != c_2:
            sum += 1
        return sum

    #c_2
    @staticmethod
    def intento_2(node):
        sum = 0
        def __get_bits(face, gb, lb):
            if lb > gb or gb < lb:
                return 0

            mask = ((2 ** (gb + 1) - 1) >> lb) << lb

            return (face & mask) >> lb
        c_0 = __get_bits(node.cube[0], 14, 12)
        c_1 = __get_bits(node.cube[1], 14, 12)
        c_2 = __get_bits(node.cube[2], 14, 12)
        c_3 = __get_bits(node.cube[3], 14, 12)
        c_4 = __get_bits(node.cube[4], 14, 12)
        c_5 = __get_bits(node.cube[5], 14, 12)

        if __get_bits(node.cube[0],2,0) != c_0 or __get_bits(node.cube[1],20,18) != c_1 or __get_bits(node.cube[3],8,6) != c_3:
            sum += 1
        if __get_bits(node.cube[0],8,6) != c_0 or __get_bits(node.cube[1],26,24) != c_1 or __get_bits(node.cube[4],2,0) != c_4:
            sum += 1
        if __get_bits(node.cube[0],20,18) != c_0 or __get_bits(node.cube[3],26,24) != c_3 or __get_bits(node.cube[2],2,0) != c_2:
            sum += 1
        if __get_bits(node.cube[0],26,24) != c_0 or __get_bits(node.cube[4],20,18) != c_4 or __get_bits(node.cube[2],8,6) != c_2:
            sum += 1
        if __get_bits(node.cube[5],2,0) != c_5 or __get_bits(node.cube[4],8,6) != c_4 or __get_bits(node.cube[1],8,6) != c_1:
            sum += 1
        if __get_bits(node.cube[5],8,6) != c_5 or __get_bits(node.cube[3],2,0) != c_3 or __get_bits(node.cube[1],2,0) != c_1:
            sum += 1
        if __get_bits(node.cube[5],20,18) != c_5 or __get_bits(node.cube[4],26,24) != c_4 or __get_bits(node.cube[2],26,24) != c_2:
            sum += 1
        if __get_bits(node.cube[5],26,24) != c_5 or __get_bits(node.cube[3],20,18) != c_3 or __get_bits(node.cube[2],20,18) != c_2:
            sum += 1
        return sum

    #e_2
    @staticmethod
    def intento_3(node):
        sum = 0
        def __get_bits(face, gb, lb):
            if lb > gb or gb < lb:
                return 0

            mask = ((2 ** (gb + 1) - 1) >> lb) << lb

            return (face & mask) >> lb
        c_0 = __get_bits(node.cube[0], 14, 12)
        c_1 = __get_bits(node.cube[1], 14, 12)
        c_2 = __get_bits(node.cube[2], 14, 12)
        c_3 = __get_bits(node.cube[3], 14, 12)
        c_4 = __get_bits(node.cube[4], 14, 12)
        c_5 = __get_bits(node.cube[5], 14, 12)

        if __get_bits(node.cube[0],5,3) != c_0 or __get_bits(node.cube[1],23,21) != c_1:
            sum += 1
        if __get_bits(node.cube[4],5,3) != c_4 or __get_bits(node.cube[1],17,15) != c_1:
            sum += 1
        if __get_bits(node.cube[5],5,3) != c_5 or __get_bits(node.cube[1],5,3) != c_1:
            sum += 1
        if __get_bits(node.cube[3],5,3) != c_3 or __get_bits(node.cube[1],11,9) != c_1:
            sum += 1
        if __get_bits(node.cube[0],11,9) != c_0 or __get_bits(node.cube[3],17,15) != c_3:
            sum += 1
        if __get_bits(node.cube[0],17,15) != c_0 or __get_bits(node.cube[4],11,9) != c_4:
            sum += 1
        if __get_bits(node.cube[5],11,9) != c_5 or __get_bits(node.cube[4],17,15) != c_4:
            sum += 1
        if __get_bits(node.cube[5],17,15) != c_5 or __get_bits(node.cube[3],11,9) != c_3:
            sum += 1
        if __get_bits(node.cube[0],23,21) != c_0 or __get_bits(node.cube[2],5,3) != c_2:
            sum += 1
        if __get_bits(node.cube[4],23,21) != c_4 or __get_bits(node.cube[2],17,15) != c_2:
            sum += 1
        if __get_bits(node.cube[5],23,21) != c_5 or __get_bits(node.cube[2],23,21) != c_2:
            sum += 1
        if __get_bits(node.cube[3],23,21) != c_3 or __get_bits(node.cube[2],11,9) != c_2:
            sum += 1
        return sum
    
    #e
    @staticmethod
    def intento_4(node):
        sum = 0
        def __get_bits(face, gb, lb):
            if lb > gb or gb < lb:
                return 0

            mask = ((2 ** (gb + 1) - 1) >> lb) << lb

            return (face & mask) >> lb
        
        for k in range(6):
            if __get_bits(node.cube[k],5,3) != __get_bits(node.cube[k],14,12):
                sum += 1
            if __get_bits(node.cube[k],11,9) != __get_bits(node.cube[k],14,12):
                sum += 1
            if __get_bits(node.cube[k],17,15) != __get_bits(node.cube[k],14,12):
                sum += 1
            if __get_bits(node.cube[k],23,21) != __get_bits(node.cube[k],14,12):
                sum += 1
        return sum

    #c
    @staticmethod
    def intento_5(node):
        def __get_bits(face, gb, lb):
            if lb > gb or gb < lb:
                return 0

            mask = ((2 ** (gb + 1) - 1) >> lb) << lb

            return (face & mask) >> lb
        sum = 0
        for k in range(6):
            if __get_bits(node.cube[k],2,0) != __get_bits(node.cube[k],14,12):
                sum += 1
            if __get_bits(node.cube[k],8,6) != __get_bits(node.cube[k],14,12):
                sum += 1
            if __get_bits(node.cube[k],20,18) != __get_bits(node.cube[k],14,12):
                sum += 1
            if __get_bits(node.cube[k],26,24) != __get_bits(node.cube[k],14,12):
                sum += 1
        return sum

    #c_e
    @staticmethod
    def intento_6(node):
        def __get_bits(face, gb, lb):
            if lb > gb or gb < lb:
                return 0

            mask = ((2 ** (gb + 1) - 1) >> lb) << lb

            return (face & mask) >> lb
        sum = 0
        for k in range(6):
            center_bits = __get_bits(node.cube[k],14,12)
            gb = 2
            lb = 0
            for _ in range(9):
                if __get_bits(node.cube[k],gb,lb) != center_bits:
                    sum += 1
                gb += 3
                lb += 3
        return sum

    #f
    @staticmethod
    def intento_7(node):
        def __get_bits(face, gb, lb):
            if lb > gb or gb < lb:
                return 0

            mask = ((2 ** (gb + 1) - 1) >> lb) << lb

            return (face & mask) >> lb
        
        minimum = 54
        move_12 = ['R', 'r', #Right
                    'L', 'l', #Left
                    'U', 'u', #Up
                    'N', 'n', #Down
                    'F', 'f', #Front
                    'D', 'd'] #Back
        for q in range(len(move_12)):
            sum = 0
            obj1 = Cube_movements(deepcopy(node.cube))
            new_cube = obj1.Movements(move_12[q])
            for k in range(6):
                center_bits = __get_bits(new_cube[k],14,12)
                gb = 2
                lb = 0
                for _ in range(9):
                    if __get_bits(new_cube[k],gb,lb) != center_bits:
                        sum += 1
                    gb += 3
                    lb += 3
            minimum = min(sum, minimum)
        return minimum

class World:
    def __init__(self):
        self.directions ={'':'', 'R': "Rotate the right layer clockwise.", 'r': "Rotate the right layer anti-clockwise.",
               'L': "Rotate the left layer clockwise.", 'l':"Rotate the left layer anti-clockwise.",
               'U': "Rotate the top layer clockwise.", 'u':"Rotate the top layer anti-clockwise.",
               'N':"Rotate the bottom layer clockwise.", 'n':"Rotate the bottom layer anti-clockwise.",
               'F': "Rotate the front layer clockwise.", 'f':"Rotate the front layer anti-clockwise.",
               'D': "Rotate the back layer clockwise.", 'd': "Rotate the back layer anti-clockwise."}
        
        #En python es más rápido verificar si un elemento esta en un set que en una lista
        self.visited = set()

        self.movement_12 = ['R', 'r', #Right
                           'L', 'l', #Left
                           'U', 'u', #Up
                           'N', 'n', #Down
                           'F', 'f', #Front
                           'D', 'd'] #Back
        
    def solve_a_star(self, source_cube, target_cube, heuristic):
        pq = PriorityQueue()
        
        source = Cube()
        target = Cube()
        source.cube = source_cube
        target.cube = target_cube

        source.path.append(source)
        pq.put(source)

        while not pq.empty():
            curr_node = pq.get()

            #Check if the cube is already solved
            if curr_node.cube == target.cube:
                """self.print_solution(curr_node)""" #REPORTE 3
                end_time = time.time()#REPORTE 4
                print(end_time - start_time) #REPORTE 5
                return

            #This 'if' is in the case that we already use a node but there are more nodes (with the same cube) in the pq
            # so this 'if' helps to do not use them
            if self.is_visited(curr_node.cube):
                continue
            else:
                self.visited.add(tuple(deepcopy(curr_node.cube)))

                for i in range(len(self.movement_12)):
                    obj = Cube_movements(deepcopy(curr_node.cube))
                    new_cube = obj.Movements(self.movement_12[i])

                    #This 'if' is helps to not create more nodes if we already use them
                    if self.is_visited(new_cube):
                        pass
                    else:
                        new_node = Cube()
                        new_node.distance = curr_node.distance+1
                        new_node.cube = new_cube
                        new_node.move = self.movement_12[i]
                        new_node.path.extend(curr_node.path)
                        new_node.path.append(new_node)
                        new_node.calculate_heuristic(heuristic)
                        pq.put(new_node)

    def is_visited(self, cube):
        tupla = tuple(deepcopy(cube))
        return tupla in self.visited
        
    def print_solution(self, node):
        mask = (2 ** 3) - 1
        for q in range(len(node.path)):
            print("Step: ", q)
            print(self.directions[node.path[q].move])
            aux = [node.path[q].cube[0], node.path[q].cube[1], node.path[q].cube[2], node.path[q].cube[3], node.path[q].cube[4], node.path[q].cube[5]]
            print("   front          top           bottom           left          right          back")
            for _ in range(3):
                print("-----------    -----------    -----------    -----------    ----------     -----------")
                for i in range(6):
                    for _ in range(3):
                        print(aux[i] & mask, end=' | ')
                        aux[i] >>= 3
                    print(end = "   ")
                print()
            print("\n0 = white |  1 = orange  |     2 = red  |   3 = green  |    4 = blue  |    5 = yellow")
            print()
        
        print("Cantidad de pasos: ", len(node.path)-1)

obj1 = World()

t_cube = [0]*6
for k in range(6):
    for _ in range(9):
        t_cube[k] = (t_cube[k] << 3) | k
obj2 = Cube_movements(deepcopy(t_cube))

s_cube = obj2.shuffle(10)

start_time = time.time() #REPORTE 2
obj1.solve_a_star(s_cube, t_cube, Heuristics.manhattan_distance_3d)

#BORRAR LOS 5 REPORTES

#Este se lleva a todos de corbata (me hizo un 10 en 2:59:50)
#El 10 se tarda menos de 10 min