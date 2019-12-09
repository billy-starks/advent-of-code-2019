class IntCode:
    def __init__(self):
        self.memory = []
        self.userInput = []
        self.programOutput = None
        self.ip = 0
        self.hasHalted = True
    
    def load_program(self, input):
        with open(input, 'r') as file:
            data = file.read()
            data = data.strip()
            data = data.split(',')
            self.memory = data
        self.ip = 0
        self.hasHalted = False

    def run_program(self, *optionalInput):
        self.userInput = self._process_input(optionalInput)
        self.programOutput = None
        while True:
            opcode, p1mode, p2mode, p3mode  = self._process_instruction(self.memory[self.ip])
            
            if opcode == 1: # Add p1, p2, a1
                param1, param2 = self._get_values(2, p1mode, p2mode)
                value = param1 + param2
                self._store_value_at_address(self.ip+3, value)
                self.ip += 4
                
            elif opcode == 2: # Multiply p1, p2, a1
                param1, param2 = self._get_values(2, p1mode, p2mode)
                value = param1 * param2
                self._store_value_at_address(self.ip+3, value)
                self.ip += 4

            elif opcode == 3: # StoreInput a1
                if len(self.userInput) > 0:
                    address = int(self.memory[self.ip+1])
                    self.memory[address] = str(self.userInput.pop(0))
                    self.ip += 2
                else: # Wait for input
                    print("Program paused; waiting for input")
                    return

            elif opcode == 4: # WriteOutput a1
                param = self._get_values(1, p1mode)[0]
                self.programOutput = param
                self.ip += 2

            elif opcode == 5: #JumpIfTrue b1 p1
                check, ip = self._get_values(2, p1mode, p2mode)
                if check != 0:
                    self.ip = ip
                else:
                    self.ip += 3

            elif opcode == 6: #JumpIfFalse b1 p1
                check, ip = self._get_values(2, p1mode, p2mode)
                if check == 0:
                    self.ip = ip
                else:
                    self.ip += 3

            elif opcode == 7: #LessThan p1 p2 a1
                param1, param2 = self._get_values(2, p1mode, p2mode)
                address = int(self.memory[self.ip+3])
                if param1 < param2:
                    self.memory[address] = '1'
                else:
                    self.memory[address] = '0'
                self.ip += 4

            elif opcode == 8: #Equals p1 p2 a1
                param1, param2 = self._get_values(2, p1mode, p2mode)
                address = int(self.memory[self.ip+3])
                if param1 == param2:
                    self.memory[address] = '1'
                else:
                    self.memory[address] = '0'
                self.ip += 4
                
            elif opcode == 99:
                self.hasHalted = True
                break
            
            else:
                raise Exception("Invalid Opcode {} at {}".format(opcode, pos))
        return self.programOutput

    def dump_memory(self):
        return self.memory

    def flash_memory(self, memory):
        self.memory = memory
        self.ip = 0
        self.hasHalted = False

    def push_input(self, newInput):
        self.userInput.append(newInput)

    def read_output(self):
        return self.programOutput

    def halted(self):
        return self.hasHalted
                
    def _process_instruction(self, instruction):
        opcode = int(instruction[-2:])
        param1mode = int(instruction[-3]) if len(instruction) >= 3 else 0
        param2mode = int(instruction[-4]) if len(instruction) >= 4 else 0
        param3mode = int(instruction[-5]) if len(instruction) >= 5 else 0
        return opcode, param1mode, param2mode, param3mode

    def _get_values(self, numArgs, *paramModes):
        position = self.ip + 1
        params = []
        offset = 0
        for _ in range(numArgs):
            param = int(self.memory[position + offset])
            mode = paramModes[offset]
            if mode == 0: #Position mode
                params.append(int(self.memory[param]))
            elif mode == 1: #Immediate mode
                params.append(param)
            offset += 1
        return tuple(params)

    def _store_value_at_address(self, position, value):
        address = int(self.memory[position])
        self.memory[address] = str(value)

    def _process_input(self, userInput):
        if userInput == None or len(userInput) == 0:
            return self.userInput
        return list(userInput)

