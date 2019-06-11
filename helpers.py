def invalid_character_in_ifsc(ifsc_code):
	set = {'@','#','$','%','&'}
	for c in set:
		if c in ifsc_code:
			return True
	return False
    