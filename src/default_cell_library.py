from cell import Cell, Buffer, Splitter


class Library:
    def __init__(self, default_library: bool = True):
        self._lib = dict()
        self._mapping = dict()
        self._bfr = None
        self._splitters = dict()
        if default_library:
            self._load_deault_library()
            for item in self._lib.values():
                if isinstance(item, Cell):
                    self._mapping[item.truth_value()] = item

    def __getitem__(self, item):
        return self._lib.get(item)

    @property
    def max_fan_out(self):
        return max(self._splitters.keys())

    def get(self, item):
        return self._lib.get(item)

    def get_buffer(self):
        return self._bfr

    def get_splitter(self, fan_out: int):
        return self._splitters.get(fan_out)

    def get_mapping(self, truth: int):
        return self._mapping.get(truth)

    def _load_deault_library(self):
        self.bufferNames = {"bfr"}
        self.splitterNames = {"spl2", "spl3L", "spl4L"}
        self._lib["inv"] = Cell("inv", ["din", "dout"], ["din"], "dout", 1, 2, 1)
        self._lib["bfr"] = Buffer("bfr", ["din", "dout"], "din", "dout", 2, 1)
        self._lib["and_bb"] = Cell("and_bb", ["a", "b", "c"], ["a", "b"], "c", 8, 6, 1)
        self._lib["and_bi"] = Cell("and_bi", ["a", "b", "c"], ["a", "b"], "c", 2, 6, 1)
        self._lib["and_ib"] = Cell("and_ib", ["a", "b", "c"], ["a", "b"], "c", 4, 6, 1)
        self._lib["and_ii"] = Cell("and_ii", ["a", "b", "c"], ["a", "b"], "c", 1, 6, 1)
        self._lib["or_bb"] = Cell("or_bb", ["a", "b", "c"], ["a", "b"], "c", 14, 6, 1)
        self._lib["or_bi"] = Cell("or_bi", ["a", "b", "c"], ["a", "b"], "c", 11, 6, 1)
        self._lib["or_ib"] = Cell("or_ib", ["a", "b", "c"], ["a", "b"], "c", 13, 6, 1)
        self._lib["or_ii"] = Cell("or_ii", ["a", "b", "c"], ["a", "b"], "c", 7, 6, 1)
        self._lib["maj_bbb"] = Cell("maj_bbb", ["a", "b", "c", "d"], ["a", "b", "c"], "d", 232, 6, 1)
        self._lib["maj_bbi"] = Cell("maj_bbi", ["a", "b", "c", "d"], ["a", "b", "c"], "d", 142, 6, 1)
        self._lib["maj_bib"] = Cell("maj_bib", ["a", "b", "c", "d"], ["a", "b", "c"], "d", 178, 6, 1)
        self._lib["maj_ibb"] = Cell("maj_ibb", ["a", "b", "c", "d"], ["a", "b", "c"], "d", 212, 6, 1)
        self._lib["maj_iii"] = Cell("maj_iii", ["a", "b", "c", "d"], ["a", "b", "c"], "d", 23, 6, 1)
        self._lib["maj_bii"] = Cell("maj_bii", ["a", "b", "c", "d"], ["a", "b", "c"], "d", 43, 6, 1)
        self._lib["maj_iib"] = Cell("maj_iib", ["a", "b", "c", "d"], ["a", "b", "c"], "d", 113, 6, 1)
        self._lib["maj_ibi"] = Cell("maj_ibi", ["a", "b", "c", "d"], ["a", "b", "c"], "d", 77, 6, 1)
        self._lib["spl2"] = Splitter("spl2", ["a", "b", "c"], "a", {"b", "c"}, 2, 1)
        self._lib["spl3L"] = Splitter("spl3L", ["a", "b", "c", "d"], "a", {"b", "c", "d"}, 2, 1)
        self._lib["spl4L"] = Splitter("spl4L", ["a", "b", "c", "d", "e"], "a", {"b", "c", "d", "e"}, 2, 1)
        self._bfr = self._lib["bfr"]
        self._splitters = {2: self._lib["spl2"], 3: self._lib["spl3L"], 4: self._lib["spl4L"]}
