from intcode import IntCode


def main1():
    interpreter = IntCode()
    interpreter.load_program('input')
    return interpreter.run_program(1)

def main2():
    interpreter = IntCode()
    interpreter.load_program('input')
    return interpreter.run_program(5)

print(main1())
print(main2())
