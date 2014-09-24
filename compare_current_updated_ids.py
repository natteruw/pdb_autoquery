current_list = [i.strip().split() for i in open("current_id_lists/D6_ids_001.list").readlines()]
updated_list = [i.strip().split() for i in open("updated_temp_id_lists/tempD6").readlines()]

def diff(current_list, updated_list):
	a = set(current_list).union(set(updated_list))
	b = set(current_list).intersection(set(updated_list))
	print list(a - b)
