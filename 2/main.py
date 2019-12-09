def load_program(input):
    with open(input, 'r') as file:
        data = file.read()
        data = data.strip()
        data = data.split(',')
        return data

def run_program(program):
    pos = 0
    while True:
        opcode = program[pos]

        if opcode == '1':
            pos1, pos2, pos3 = int(program[pos+1]), int(program[pos+2]), int(program[pos+3])
            value = int(program[pos1]) + int(program[pos2])
            program[pos3] = value

        elif opcode == '2':
            pos1, pos2, pos3 = int(program[pos+1]), int(program[pos+2]), int(program[pos+3])
            value = int(program[pos1]) * int(program[pos2])
            program[pos3] = value

        elif opcode == '99':
            return program

        else:
            raise Exception("Invalid Opcode {} at {}".format(opcode, pos))

        pos += 4

def main1():
    program = load_program('input')
    program[1] = '12'
    program[2] = '2'
    program = run_program(program)
    return program[0]

def try_with_input(program, noun, verb):
    memory = program[::]
    memory[1] = noun
    memory[2] = verb
    return int(run_program(memory)[0])

def main2():
    program = load_program('input')
    for noun in range(100):
        for verb in range(100):
            value = try_with_input(program, noun, verb)
            if value == 19690720:
                return (noun, verb)

print(main1())
print(main2())
            
