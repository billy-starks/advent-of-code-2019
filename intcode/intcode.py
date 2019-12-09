class IntCode:
    def __init__(self):
        self.memory = []
    
    def load_program(self, input):
        with open(input, 'r') as file:
            data = file.read()
            data = data.strip()
            data = data.split(',')
            self.memory = data

    def run_program(self, optionalInput = None):
        pos = 0
        userInput = None if optionalInput is None else optionalInput
        programOutput = None
        while True:
            opcode, p1mode, p2mode, p3mode  = self. _process_instruction(self.memory[pos])
            
            if opcode == 1: # Add p1, p2, a1
                param1, param2 = self._get_values(pos+1, 2, p1mode, p2mode)
                value = param1 + param2
                self._store_value_at_address(pos+3, value)
                pos += 4
                
            elif opcode == 2: # Multiply p1, p2, a1
                param1, param2 = self._get_values(pos+1, 2, p1mode, p2mode)
                value = param1 * param2
                self._store_value_at_address(pos+3, value)
                pos += 4

            elif opcode == 3: # StoreInput a1
                address = int(self.memory[pos+1])
                self.memory[address] = str(userInput)
                pos += 2

            elif opcode == 4: # WriteOutput a1
                param = self._get_values(pos+1, 1, p1mode)[0]
                programOutput = param
                pos += 2

            elif opcode == 5: #JumpIfTrue b1 p1
                check, ip = self._get_values(pos+1, 2, p1mode, p2mode)
                if check != 0:
                    pos = ip
                else:
                    pos += 3

            elif opcode == 6: #JumpIfFalse b1 p1
                check, ip = self._get_values(pos+1, 2, p1mode, p2mode)
                if check == 0:
                    pos = ip
                else:
                    pos += 3

            elif opcode == 7: #LessThan p1 p2 a1
                param1, param2 = self._get_values(pos+1, 2, p1mode, p2mode)
                address = int(self.memory[pos+3])
                if param1 < param2:
                    self.memory[address] = '1'
                else:
                    self.memory[address] = '0'
                pos += 4

            elif opcode == 8: #Equals p1 p2 a1
                param1, param2 = self._get_values(pos+1, 2, p1mode, p2mode)
                address = int(self.memory[pos+3])
                if param1 == param2:
                    self.memory[address] = '1'
                else:
                    self.memory[address] = '0'
                pos += 4
                
            elif opcode == 99:
                break
            
            else:
                raise Exception("Invalid Opcode {} at {}".format(opcode, pos))
        return programOutput

    def dump_memory(self):
        return self.memory
                
    def _process_instruction(self, instruction):
        opcode = int(instruction[-2:])
        param1mode = int(instruction[-3]) if len(instruction) >= 3 else 0
        param2mode = int(instruction[-4]) if len(instruction) >= 4 else 0
        param3mode = int(instruction[-5]) if len(instruction) >= 5 else 0
        return opcode, param1mode, param2mode, param3mode

    def _get_values(self, position, numArgs, *paramModes):
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
