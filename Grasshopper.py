from hub import light_matrix, port
import motor_pair

motor_pair.pair(motor_pair.PAIR_1, port.C, port.D)

light_matrix.write('3')
light_matrix.write('2')
light_matrix.write('1')

motor_pair.move_for_time(motor_pair.PAIR_1, 5000, 0, velocity = 500)
