# import the os module to work with file paths
import os

# get the current working directory
cwd = os.getcwd()

# create the relative file path to the files
cnf_file_path = os.path.join(cwd, "test", "uf20-01.cnf")
txt_file_path = os.path.join(cwd, "test", "uf20-01.txt")

def convert_to_txt(cnf_file_path, txt_file_path):
    with open(r"{}".format(cnf_file_path), 'r') as cnf_file:
        with open(r"{}".format(txt_file_path), 'w') as txt_file:
            for line in cnf_file:
                txt_file.write(line)


convert_to_txt(cnf_file_path, txt_file_path)

# extract useful data from the input file
def extract_clauses(file_path):
    with open(file_path, 'r') as file:
        start_of_file = True
        problem_line_found = False
        clauses = []
        for line in file:
            if start_of_file and line.startswith("c"):
                continue
            elif line.startswith("p cnf"):
                problem_line_found = True
                start_of_file = False
                variables, clauses_count = map(int, line.strip().split()[2:4])
                continue
            else:
                start_of_file = False
                clause = line.strip().split()
                if clause and clause[-1] == "0":
                    clauses.append([x for x in clause[:-1] if x != ''])
        if not problem_line_found:
            raise Exception("Problem line not found.")
    return variables, clauses_count, clauses


variables, clauses_count, clauses = extract_clauses(txt_file_path)
print("Number of variables:", variables)
print("Number of clauses:", clauses_count)
print("Clauses:", clauses)
print("Size of clauses list:", len(clauses))

# eliminate_empty_lists
def eliminate_empty_lists(clauses):
    return [lst for lst in clauses if lst]

clauses = eliminate_empty_lists(clauses)
print("Size of clauses list after removing empty clauses:", len(clauses))

print("Final Clauses:", clauses)