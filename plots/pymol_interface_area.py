from pymol import cmd

# load complex
load 1hmp_tetra_ABBA.pdb

# create objects for alpha1, beta1 and alpha1,beta1 pair of subunits
create chainA, 1hmp_tetra_ABBA and chain A
create chainB, 1hmp_tetra_ABBA and chain B
create chainC, 1hmp_tetra_ABBA and chain C
create chainD, 1hmp_tetra_ABBA and chain D
create chainAB, 1hmp_tetra_ABBA and chain A+B  
create chainCD, 1hmp_tetra_ABBA and chain C+D
create chainAC, 1hmp_tetra_ABBA and chain A+C
create chainBD, 1hmp_tetra_ABBA and chain B+D

# get hydrogens onto everything (NOTE: must have valid valences on e.g. small organic molecules)
h_add

# make sure all atoms including HETATM within an object occlude one another, but ignore solvent
flag ignore, none
flag ignore, solvent

# use solvent-accessible surface with high sampling density
set dot_solvent, 1
set dot_density, 3

# measure the components individually storing the results for later
chainA_area=cmd.get_area("chainA")
chainB_area=cmd.get_area("chainB")
chainC_area=cmd.get_area("chainC")
chainD_area=cmd.get_area("chainD")

# measure the dimers of interface 1 (dimer interface)
dimerAB_area=cmd.get_area("chainAB")
dimerCD_area=cmd.get_area("chainCD")

# measure the dimers of interface 2 (tetramer interface)
dimerAC_area=cmd.get_area("chainAC")
dimerBD_area=cmd.get_area("chainBD")

# now print results and do some maths to get the buried surface
print("Interface AB (dimer): %.3f" % ( (chainA_area+chainB_area-dimerAB_area)/2.0) )
print("Interface CD (dimer): %.3f" % ( (chainC_area+chainD_area-dimerCD_area)/2.0) )
print("Interface AC (tetra): %.3f" % ( (chainA_area+chainC_area-dimerAC_area)/2.0) )
print("Interface BD (tetra): %.3f" % ( (chainB_area+chainD_area-dimerBD_area)/2.0) )

