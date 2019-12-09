from intcode import IntCode
from itertools import permutations

class AmpSystem:
    def __init__(self):
        self.amps = [IntCode() for _ in range(5)]
        for amp in self.amps:
            amp.load_program('input')
        self.cleanState = self.amps[0].dump_memory()

    def _reset(self):
        for amp in self.amps:
            amp.flash_memory(self.cleanState)

    def run_phase(self, a, b, c, d, e):
        self._reset()
        phases = [a,b,c,d,e]
        self.amps[0].run_program(phases[0], 0)
        lastOut = self.amps[0].read_output()
        currentAmp = 1
        while currentAmp != 0:
            self.amps[currentAmp].run_program(phases[currentAmp], lastOut)
            lastOut = self.amps[currentAmp].read_output()
            currentAmp = (currentAmp + 1) % 5
            
        while not self.amps[currentAmp].halted():
            self.amps[currentAmp].push_input(lastOut)
            self.amps[currentAmp].run_program()
            lastOut = self.amps[currentAmp].read_output()
            currentAmp = (currentAmp + 1) % 5

        return lastOut

def main1():
    ampSystem = AmpSystem()
    greatestPhase = (0,1,2,3,4)
    greatestValue = -1
    for phase in permutations([0,1,2,3,4]):
        value = ampSystem.run_phase(*phase)
        if value > greatestValue:
            greatestValue = value
            greatestPhase = phase
    return greatestValue, greatestPhase

def main2():
    ampSystem = AmpSystem()
    greatestPhase = (5,6,7,8,9)
    greatestValue = -1
    for phase in permutations([5,6,7,8,9]):
        value = ampSystem.run_phase(*phase)
        if value > greatestValue:
            greatestValue = value
            greatestPhase = phase
    return greatestValue, greatestPhase

print(main1())
print(main2())

        
