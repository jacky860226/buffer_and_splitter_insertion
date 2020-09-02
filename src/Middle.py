import Raw
import default_cell_library
import BufferAndSplitterInsertionSolver


class Wire:
    def __init__(self, name: str):
        self.name = name
        self.input = []
        self.output = None
        self.connects = []

class Middle:
    def __init__(self, rawModule: Raw.Module):
        self.rawModule = rawModule
        self.ori_jj = 0
        self.buffer_cnt = 0
        self.splitter_cnt = 0
        self.wireDict = dict()
        rawModule.input.add("1'b0")
        rawModule.input.add("1'b1")
        for w in rawModule.input:
            self.wireDict[w] = Wire(w)
        for w in rawModule.output:
            self.wireDict[w] = Wire(w)
            virtualOut = Raw.SubModule("JinkelaOut", "jinkela_out_" + w)
            virtualOut.ioDict["out"] = w
            rawModule.subModuleList.add(virtualOut)
        for w in rawModule.wire:
            self.wireDict[w] = Wire(w)
        self.library = default_cell_library.Library()
        for sm in rawModule.subModuleList:
            if sm.masterName != "JinkelaOut":
                self.ori_jj += self.library.get(sm.masterName).gate_count
            if sm.masterName in self.library.bufferNames:
                self.wireDict[sm.ioDict[self.library.get(
                    sm.masterName)._input]].input.append(sm)
                self.wireDict[sm.ioDict[self.library.get(
                    sm.masterName)._output]].output = sm
            elif sm.masterName in self.library.splitterNames:
                self.wireDict[sm.ioDict[self.library.get(
                    sm.masterName)._input]].input.append(sm)
                for outs in self.library.get(sm.masterName)._outputs:
                    self.wireDict[sm.ioDict[outs]].output = sm
            else:
                if sm.masterName != "JinkelaOut":
                    for ins in self.library.get(sm.masterName)._inputs:
                        self.wireDict[sm.ioDict[ins]].input.append(sm)
                    self.wireDict[sm.ioDict[self.library.get(
                        sm.masterName)._output]].output = sm
                else:
                    self.wireDict[sm.ioDict["out"]].input.append(sm)
        for w in rawModule.input:
            self.dfsCall(self.wireDict[w], self.wireDict[w])
        for sm in rawModule.subModuleList:
            if not sm.masterName in self.library.bufferNames and not sm.masterName in self.library.splitterNames:
                if sm.masterName != "JinkelaOut":
                    w = sm.ioDict[self.library.get(sm.masterName)._output]
                    self.dfsCall(self.wireDict[w], self.wireDict[w])
        for w in self.wireDict:
            if len(self.wireDict[w].connects) > 0:
                self.wireDict[w].connects.sort(key=lambda x: x[0])
        
        delete = []
        for sm in rawModule.subModuleList:
            if sm.masterName in self.library.bufferNames or sm.masterName in self.library.splitterNames:
                delete.append(sm)
        for sm in delete:
            rawModule.subModuleList.remove(sm)

    def dfsCall(self, outputWire, curWire, level=0):
        for sm in curWire.input:
            if sm.masterName in self.library.bufferNames:
                self.buffer_cnt += 1
                nextWire = self.wireDict[sm.ioDict[self.library.get(
                    sm.masterName)._output]]
                self.dfsCall(outputWire, nextWire, level + 1)
            elif sm.masterName in self.library.splitterNames:
                self.splitter_cnt += 1
                for outs in self.library.get(sm.masterName)._outputs:
                    nextWire = self.wireDict[sm.ioDict[outs]]
                    self.dfsCall(outputWire, nextWire, level + 1)
            else:
                pin = None
                for k, v in sm.ioDict.items():
                    if v == curWire.name:
                        pin = k
                assert(pin is not None)
                outputWire.connects.append((level, sm, pin))

    def printConnect(self):
        for w in self.wireDict:
            if len(self.wireDict[w].connects) > 0:
                print(w, self.wireDict[w].connects)
    
    def recursiveInsert(self, connects, parentWire, node):
        if not isinstance(node, list): # leaf
            sm = connects[node][1]
            pin = connects[node][2]
            sm.ioDict[pin] = parentWire.name
        else:
            if len(node) == 1: # buffer
                bfr = self.library.get_buffer()
                newBuffer = Raw.SubModule(bfr.name, "new_Jinkela_buffer_" + str(self.new_buffer_cnt))
                self.new_buffer_cnt += 1
                newBuffer.ioDict[bfr._input] = parentWire.name
                newWire = Wire("new_Jinkela_wire_" + str(self.new_wire_cnt))
                self.new_wire_cnt += 1
                newBuffer.ioDict[bfr._output] = newWire.name
                self.recursiveInsert(connects, newWire, node[0])
                self.rawModule.subModuleList.add(newBuffer)
            else: # splitter
                spli = self.library.get_splitter(len(node))
                newSplitter = Raw.SubModule(spli.name, "new_Jinkela_splitter_" + str(self.new_splitter_cnt))
                self.new_splitter_cnt += 1
                newSplitter.ioDict[spli._input] = parentWire.name
                childCnt = 0
                for out in spli._outputs:
                    newWire = Wire("new_Jinkela_wire_" + str(self.new_wire_cnt))
                    self.new_wire_cnt += 1
                    newSplitter.ioDict[out] = newWire.name
                    self.recursiveInsert(connects, newWire, node[childCnt])
                    childCnt += 1
                self.rawModule.subModuleList.add(newSplitter)
    
    def BufferAndSplitterInsertion(self):
        self.new_wire_cnt = 0
        self.new_buffer_cnt = 0
        self.new_splitter_cnt = 0
        solver = BufferAndSplitterInsertionSolver.DP_Solver()
        for w in self.wireDict:
            if len(self.wireDict[w].connects) > 0:
                S = []
                for l, k, q in self.wireDict[w].connects:
                    S.append(l)
                res = solver.solve(S, self.library.max_fan_out)
                tree = res[1]
                assert(res[0][1] == 0)
                self.recursiveInsert(self.wireDict[w].connects, self.wireDict[w], tree)
        self.rawModule.wire = set()
        for sm in self.rawModule.subModuleList:
            for k, v in sm.ioDict.items():
                self.rawModule.wire.add(v)
