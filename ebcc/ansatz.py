"""Ansatz definition.
"""

import importlib

import numpy as np

from ebcc import METHOD_TYPES, util


named_ansatzes = {
        "CCSD": ("CCSD", "", 0, 0),
        "CCSDT": ("CCSDT", "", 0, 0),
        "CCSD(T)": ("CCSD(T)", "", 0, 0),
        "CC2": ("CC2", "", 0, 0),
        "CC3": ("CC3", "", 0, 0),
        "CCSD-S-1-1": ("CCSD", "S", 1, 1),
        "CCSD-SD-1-1": ("CCSD", "SD", 1, 1),
        "CCSD-SD-1-2": ("CCSD", "SD", 1, 2),
}


class Ansatz:
    """Ansatz class.
    """

    def __init__(
            self,
            fermion_ansatz: str = "CCSD",
            boson_ansatz: str = "",
            fermion_coupling_rank: int = 0,
            boson_coupling_rank: int = 0,
    ):
        self.fermion_ansatz = fermion_ansatz
        self.boson_ansatz = boson_ansatz
        self.fermion_coupling_rank = fermion_coupling_rank
        self.boson_coupling_rank = boson_coupling_rank

    def _get_eqns(self, prefix):
        """Get the module which contains the generated equations for
        the current model.
        """
        name = prefix + self.name.replace("-", "_")
        name = name.replace("(", "_").replace(")", "")
        eqns = importlib.import_module("ebcc.codegen.%s" % name)
        return eqns

    @classmethod
    def from_string(cls, string):
        """Build an Ansatz from a string for the default ansatzes.

        Parameters
        ----------
        input : str
            Input string

        Returns
        -------
        ansatz : Ansatz
            Ansatz object
        """

        if string not in named_ansatzes:
            raise util.ModelNotImplemented(string)

    @property
    def name(self):
        """Get a string with the name of the method.

        Returns
        -------
        name : str
            Name of the method.
        """
        name = self.fermion_ansatz
        if self.boson_ansatz:
            name += "-%s" % self.boson_ansatz
        if self.fermion_coupling_rank or self.boson_coupling_rank:
            name += "-%d" % self.fermion_coupling_rank
            name += "-%d" % self.boson_coupling_rank
        return name

    @property
    def has_perturbative_correction(self):
        """Return a boolean indicating whether the ansatz includes a
        perturbative correction e.g. CCSD(T).

        Returns
        -------
        perturbative : bool
            Boolean indicating if the ansatz is perturbatively
            corrected.
        """
        return any(
                "(" in ansatz and ")" in ansatz
                for ansatz in (self.fermion_ansatz, self.boson_ansatz)
        )

    @property
    def correlated_cluster_ranks(self):
        """Get a list of cluster operator rank numbers for each of
        the fermionic, bosonic, and coupling ansatzes, for the
        correlated space (see space.py).

        Returns
        -------
        ranks : tuple of tuple of int
            Cluster operator ranks for the fermionic, bosonic, and
            coupling ansatzes, for the correlated space.
        """

        ranks = []

        notations = {
                "S": [1], "D": [2], "T": [3], "Q": [4],
                "2": [1, 2], "3": [1, 2, 3], "4": [1, 2, 3, 4],
        }

        for i, op in enumerate([self.fermion_ansatz, self.boson_ansatz]):
            # Remove any perturbative corrections
            while "(" in op:
                start = op.index("(")
                end = op.index(")")
                op = op[:start]
                if (end + 1) < len(op):
                    op += op[end + 1 :]

            # Check in order of longest -> shortest string in case
            # one method name starts with a substring equal to the
            # name of another method
            if i == 0:
                for method_type in sorted(METHOD_TYPES, key=len)[::-1]:
                    if op.startswith(method_type):
                        op = op.lstrip(method_type)
                        break

            # Remove any lower case characters, as these correspond
            # to active space
            op = "".join([char for char in op if char.isupper() or char.isnumeric()])

            # Determine the ranks
            ranks_entry = set()
            for char in op:
                for rank in notations[char]:
                    ranks_entry.add(rank)
            ranks.append(tuple(sorted(list(ranks_entry))))

        # Get the coupling ranks
        for op in [self.fermion_coupling_rank, self.boson_coupling_rank]:
            ranks.append(tuple(range(1, op + 1)))

        return tuple(ranks)

    @property
    def active_cluster_ranks(self):
        """Get a list of cluster operator rank numbers for each of
        the fermionic, bosonic, and coupling ansatzes, for the
        active space (see space.py).

        Returns
        -------
        ranks : tuple of tuple of int
            Cluster operator ranks for the fermionic, bosonic, and
            coupling ansatzes, for the active space.
        """

        ranks = []

        notations = {
                "s": [1], "d": [2], "t": [3], "q": [4],
        }

        for i, op in enumerate([self.fermion_ansatz, self.boson_ansatz]):
            # Remove any perturbative corrections
            while "(" in op:
                start = op.index("(")
                end = op.index(")")
                op = op[:start]
                if (end + 1) < len(op):
                    op += op[end + 1 :]

            # Check in order of longest -> shortest string in case
            # one method name starts with a substring equal to the
            # name of another method
            if i == 0:
                for method_type in sorted(METHOD_TYPES, key=len)[::-1]:
                    if op.startswith(method_type):
                        op = op.lstrip(method_type)
                        break

            # Remove any lower case characters, as these correspond
            # to active space
            op = "".join([char for char in op if char.islower()])

            # Determine the ranks
            ranks_entry = set()
            for char in op:
                for rank in notations[char]:
                    ranks_entry.add(rank)
            ranks.append(tuple(sorted(list(ranks_entry))))

        # Get the coupling ranks
        # FIXME how to handle? if it's ever supported
        ranks.append(tuple())

        return tuple(ranks)

