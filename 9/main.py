from intcode import IntCode

def main1():
    interpreter = IntCode()
    interpreter.load_program('input')
    interpreter.run_program(1)
    return interpreter.read_output()

def main2():
    interpreter = IntCode()
    interpreter.load_program('input')
    interpreter.run_program(2)
    return interpreter.read_output()

print(main1())
print(main2())

