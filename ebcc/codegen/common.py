import numpy as np
from timeit import default_timer as timer
from qwick import codegen

PYTHON_HEADER = """# Code generated by qwick.

import numpy as np
from pyscf import lib
from types import SimpleNamespace
from ebcc.codegen import common

"""

PYTHON_FOOTER = ""

LATEX_HEADER = r"""\documentclass{article}

\begin{document}

\title{Equations generated by {\tt qwick}.}
\maketitle

"""

LATEX_FOOTER = r"""

\end{document}"""


class FilePrinter:
    def __init__(self, name):
        self.python_file = open("%s.py" % name, "w")
        self.latex_file = open("%s.tex" % name, "w")

    def __enter__(self):
        # Initialise the Python file:
        self.python_file.write(PYTHON_HEADER)
        # Initialise the LaTeX file:
        self.latex_file.write(LATEX_HEADER)
        return self

    def __exit__(self, *args, **kwargs):
        # Exit the python file:
        self.python_file.write(PYTHON_FOOTER)
        self.python_file.close()
        # Exit the LaTeX file:
        self.latex_file.write(LATEX_FOOTER)
        self.latex_file.close()


class FunctionPrinter:
    def __init__(self, file_printer, name, args, res, remove_f_diagonal=False, timer=None):
        self.file_printer = file_printer
        self.name = name
        self.args = args
        self.res = res
        self.remove_f_diagonal = remove_f_diagonal
        self.timer = timer

    def write_python(self, string, comment=None):
        if comment:
            self.file_printer.python_file.write("    # %s\n" % comment)
        self.file_printer.python_file.write(string)
        self.file_printer.python_file.write("\n")
        self.file_printer.python_file.flush()

    def write_latex(self, string, comment=None):
        if comment:
            self.file_printer.latex_file.write(comment + ":\n\n")
        self.file_printer.latex_file.write("$$" + string + "$$")
        self.file_printer.latex_file.write("\n\n")
        self.file_printer.latex_file.flush()

    def __enter__(self):
        # Initialise python function
        self.write_python("def %s(%s, **kwargs):" % (
            self.name, ", ".join(["%s=None" % arg for arg in self.args])
        ))
        if self.remove_f_diagonal:
            self.write_python(
                    "    # Remove diagonal from Fock:\n"
                    "    f = SimpleNamespace(\n"
                    "        oo=f.oo-np.diag(np.diag(f.oo)),\n"
                    "        ov=f.ov,\n"
                    "        vo=f.vo,\n"
                    "        vv=f.vv-np.diag(np.diag(f.vv)),\n"
                    "    )\n"
            )
        return self

    def __exit__(self, *args, **kwargs):
        # Return from python function
        res_dict = "{" + ", ".join(["\"%s\": %s" % (v, v) for v in self.res]) + "}"
        self.write_python("    return %s\n" % res_dict)
        if self.timer is not None:
            print("Time for %s: %.5f s" % (self.name, self.timer()))


class Stopwatch:
    def __init__(self):
        self._t0 = timer()
        self._t = timer()

    def split(self):
        t = timer() - self._t0
        return t

    def lap(self):
        t = timer() - self._t
        self._t = timer()
        return t

    def reset(self):
        self.__init__()
        return self

    __call__ = lap


ov_2e = ["oooo", "ooov", "oovo", "ovoo", "vooo", "oovv", "ovov", "ovvo", "voov", "vovo", "vvoo", "ovvv", "vovv", "vvov", "vvvo", "vvvv"]
ov_1e = ["oo", "ov", "vo", "vv"]

def pack_2e(*args):
    # args should be in the order of ov_2e

    assert len(args) == len(ov_2e)

    nocc = args[0].shape[0]
    nvir = args[-1].shape[-1]
    occ = slice(None, nocc)
    vir = slice(nocc, None)
    out = np.zeros((nocc+nvir,) * 4)

    for key, arg in zip(ov_2e, args):
        slices = [occ if x == "o" else vir for x in key]
        out[tuple(slices)] = arg

    return out
