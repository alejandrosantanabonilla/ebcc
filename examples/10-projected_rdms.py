''' Compute RDM and energy contributions for the CCSD model from a subspace.
    This is done in two ways:
        o Democratic partitioning of the full density matrix
        o Projection of the T/L amplitudes in the construction of the individual density matrices.

    Since these are both done on the exact full system CCSD solution (which can be thought of as a
    complete bath space), they should both be trivially exact, and should only differ once the 
    solutions differ for the different subspaces (in which case the projected approach is likely 
    to be more accurate.

    The partitioning of the full system into 'clusters' in this case is just achieved via randomly
    splitting the occupied and virtual states into disjoint orthogonal orbitals. Note that for the
    projection of the T/L amplitudes, we only want to provide a projector onto the *occupied*
    space of each cluster, as opposed to democratic partitioning, which requires a fragmentation and
    projection of the full (occ+virt) orbital space.

    Note that the projected case can also be performed for the energy, and will be done to ensure consistency.'''

import numpy as np
import pyscf
import scipy.stats
from pyscf import ao2mo, scf
from pyscf import cc as pyscf_cc
from ebcc import ebccsd, utils

mol = pyscf.M(
    atom = 'H 0 0 0; F 0 0 1.1',
    basis = 'cc-pvdz')
# There is a small amount of symmetry breaking in this system.
mf = mol.UHF().run()

# Set up cc object and run kernel for T-amplitude optimization (no bosons)
cc = ebccsd.EBCCSD.fromUHFobj(mf, options={'tthresh': 1e-11, 'diis space': 12}, autogen_code=True)
ecorr = cc.kernel()
print('EBCCSD correlation energy', cc.e_corr)

# Solve lambda equations
cc.solve_lambda()

# Make subspaces.
nocc = cc.no
nvir = cc.nv
# Create occupied subspace sizes (note these can be zero or odd). 
# Generate number of occ and vir orbitals in each cluster via multinomial distribution
nclust = 5 
occ_clust_size = np.random.multinomial(nocc, np.ones(nclust)/nclust, size=1)[0]
vir_clust_size = np.random.multinomial(nvir, np.ones(nclust)/nclust, size=1)[0]
assert(sum(occ_clust_size)==nocc)
assert(sum(vir_clust_size)==nvir)
# Find arbitrary orthogonal occupied and virtual 'orbitals' in each cluster
occ_rep = scipy.stats.ortho_group.rvs(nocc) # These are the representation of the total orbitals
vir_rep = scipy.stats.ortho_group.rvs(nvir)
# The total orbital space of each cluster, defined by a set of occupied and virtual (non-canonical) orthogonal orbitals represented in the full canonical basis
clust_orbs = [] 
# Projectors of each cluster into its occupied space (in the representation of the canonical occupied orbitals)
occ_projs = []
# Total projectors of each cluster (in the representation of all canonical orbitals, occ+vir)
tot_projs = []
print('occupied cluster sizes: ',occ_clust_size)
print('virtual cluster sizes: ',vir_clust_size)
for i in range(nclust):
    occ_start_ind = np.sum(occ_clust_size[:i])
    vir_start_ind = np.sum(vir_clust_size[:i])
    # Find the cluster occupied orbitals (in the space of all canonical orbitals), noting that they will have no weight on virtuals
    clust_occ_orbs = np.vstack((occ_rep[:, occ_start_ind:occ_start_ind+occ_clust_size[i]], np.zeros((nvir, occ_clust_size[i])) ))
    clust_vir_orbs = np.vstack((np.zeros((nocc, vir_clust_size[i])), vir_rep[:, vir_start_ind:vir_start_ind+vir_clust_size[i]] ))
    clust_orbs.append(np.hstack((clust_occ_orbs, clust_vir_orbs)))
    assert(clust_orbs[-1].shape == (nocc+nvir, occ_clust_size[i]+vir_clust_size[i]))
    assert(np.isclose(np.trace(np.dot(clust_orbs[-1], clust_orbs[-1].T)), occ_clust_size[i]+vir_clust_size[i]))

    # Create a projector (in the canonical occupied representation) into the occupied space of this cluster
    occ_projs.append(np.dot(occ_rep[:, occ_start_ind:occ_start_ind+occ_clust_size[i]], occ_rep[:, occ_start_ind:occ_start_ind+occ_clust_size[i]].T))
    assert(occ_projs[-1].shape == (nocc,nocc))
    assert(np.isclose(np.trace(occ_projs[-1]), occ_clust_size[i]))
    # Create a total space projector (in the full canonical representation) into the full space of this cluster
    tot_projs.append(np.dot(clust_orbs[-1], clust_orbs[-1].T))
    assert(tot_projs[-1].shape == (nocc+nvir, nocc+nvir))
    assert(np.isclose(np.trace(tot_projs[-1]), occ_clust_size[i]+vir_clust_size[i]))
print('Created {} disjoint clusters which partition the space'.format(nclust))

# Generate 1 and 2 RDMs, from both autogenerated code and optimized code (for testing accuracy)
dm1 = cc.make_1rdm_f(autogen=False)
dm2 = cc.make_2rdm_f(autogen=False)
dm1_autogen = cc.make_1rdm_f(autogen=True, write=False)
dm2_autogen = cc.make_2rdm_f(autogen=True, write=False)
assert(np.allclose(dm1, dm1_autogen))
assert(np.allclose(dm2, dm2_autogen))

# Create the 'democratically partitioned' density matrices, just by projecting the first index of the total density matrix
# with the complete projector of each cluster, and summing the resulting matrices
dm1_dp = np.zeros_like(dm1)
dm2_dp = np.zeros_like(dm2)
for i in range(nclust):
    dm1_dp += np.dot(tot_projs[i], dm1)
    dm2_dp += np.einsum('pi,ijkl->pjkl',tot_projs[i], dm2)

# Check that democratically partitioned density matrices are exact 
# (since all cluster density matrices are exact, this is just testing the completeness of the projector really)
assert(np.allclose(dm1_dp, dm1))
assert(np.allclose(dm2_dp, dm2))
print('"Democratically partitioned" density matrices exact...')
    
# Test symmetries of full 2RDM
assert(np.allclose(dm2, dm2.transpose(1,0,3,2)))
assert(np.allclose(dm2, -dm2.transpose(2,1,0,3)))
assert(np.allclose(dm2, -dm2.transpose(0,3,2,1)))

# Now, directly construct the projective cluster density matrix contributions, via projection of the occupied T/L amplitudes 
# directly in the DM constructions.
dm1_proj = np.zeros_like(dm1)
dm2_proj = np.zeros_like(dm2)
for i in range(nclust):
    dm1_clustproj = cc.make_1rdm_f(autogen=False, write=False, subspace_proj=occ_projs[i])
    dm2_clustproj = cc.make_2rdm_f(autogen=False, write=False, subspace_proj=occ_projs[i])
    dm1_clustproj_autogen = cc.make_1rdm_f(autogen=True, write=False, subspace_proj=occ_projs[i])
    dm2_clustproj_autogen = cc.make_2rdm_f(autogen=True, write=False, subspace_proj=occ_projs[i])
    assert(np.allclose(dm1_clustproj_autogen, dm1_clustproj))
    assert(np.allclose(dm2_clustproj_autogen, dm2_clustproj))

    # Combine projected DMs of each cluster
    dm1_proj += dm1_clustproj
    dm2_proj += dm2_clustproj
    # Note that each projected cluster density matrix should be physically sensible, and have the correct permutational symmetries
    # for a GHF dm.
    assert(np.allclose(dm1_clustproj, dm1_clustproj.T))
    assert(np.allclose(dm2_clustproj, dm2_clustproj.transpose(1,0,3,2)))
    assert(np.allclose(dm2_clustproj, -dm2_clustproj.transpose(2,1,0,3)))
    assert(np.allclose(dm2_clustproj, -dm2_clustproj.transpose(0,3,2,1)))
    assert(np.allclose(dm2_clustproj_autogen, dm2_clustproj_autogen.transpose(1,0,3,2)))
    assert(np.allclose(dm2_clustproj_autogen, -dm2_clustproj_autogen.transpose(2,1,0,3)))
    assert(np.allclose(dm2_clustproj_autogen, -dm2_clustproj_autogen.transpose(0,3,2,1)))

# Check all projectively occupied partitioned density matrices are exact
assert(np.allclose(dm1_proj, dm1))
assert(np.allclose(dm2_proj, dm2))
print('"Projectively occupied partitioning" of density matrices exact...')

# We can also compute a 'local correlation energy' associated with each cluster via the occupied projection of the T/L amplitudes.
sum_eclust = 0
for i in range(nclust):
    eclust = cc.energy(amps='new', subspace_proj=occ_projs[i])
    print('"Local" energy of cluster {} is {}'.format(i,eclust))
    sum_eclust += eclust
print('Sum of local cluster energies: {}'.format(sum_eclust))
print('Full system correlation energy: {}'.format(cc.e_corr))
if np.isclose(cc.e_corr, sum_eclust):
    print('Sum of cluster energies is same as full system energy!')
assert(np.isclose(cc.e_corr, sum_eclust))
