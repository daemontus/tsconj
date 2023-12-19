import tsconj
from sys import argv

max_solutions = int(argv[1])
model_path = argv[2]

spaces = tsconj.compute_trap_spaces(
	model_path, 
	max_output=max_solutions, 
	method="conj", 
	computation="max"
)

for space in spaces:
	print("".join(space))
