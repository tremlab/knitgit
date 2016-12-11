


def create_sweater_pattern(instructions_list): #pass a file name?
	with open("sweater_pattern.txt", mode = 'w') as sweater_txt:  #ideally, let user name the file? not practical?
		sweater_txt.write("knitgit by tremlab: THE ROUNDABOUT 2016\n\n\n")

		for section in instructions_list:
			sweater_txt.write(section)

	####above creates separate text file

	##below return something fro HTML????

	







