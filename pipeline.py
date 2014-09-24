#! /usr/bin/env python

import subprocess

def diff(list_a, list_b):
	new_pdbs = [] 
	for item in list_b:
		if not item in list_a:
			new_pdbs.append(item)
	return new_pdbs

for dihedral_symmetry in range(2,7):
	current_list = [i.strip().lower() for i in open("current_id_lists/D%d_ids_001.list"%dihedral_symmetry).readlines()]
	updated_list = [i.strip().lower() for i in open("updated_temp_id_lists/tempD%d"%dihedral_symmetry).readlines()]

	diff_list = diff(current_list, updated_list)
	
	with open("diff_list_D%d"%dihedral_symmetry,"w") as diff_list_file:
		print>>diff_list_file, "\n".join(diff_list)
	
	subprocess.check_output(['./pipeline_test.sh'],shell=True)
	
	#put outputs from above process into folder for new pdbs
	# based on dihedral symmetry
