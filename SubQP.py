import os, sys
from subprocess import Popen, PIPE


def generate_args(binary, *params):
    arguments = [binary]
    arguments.extend(list(params))
    return arguments


def execute_binary(args):
    cmd = ' '.join(args)
    process = Popen(cmd, shell=True, stdout=PIPE, stderr=sys.stderr)
    (std_output, std_error) = process.communicate()
    process.wait()
    rc = process.returncode
    return rc, std_output, std_error


def merge_gfu_graphs(graph_list):
    file_list = list(map(
        lambda x : x.strip().split(),
        open(graph_list).readlines()
    ))
    merged_data = []
    name_list = []
    for i, (name, file_path) in enumerate(file_list):
        name_list.append(name)
        with open(file_path, 'r') as f:
            _ = f.readline()

            merged_data.append(f"#{i}")
            num_vertices = int(f.readline().strip())
            merged_data.append(str(num_vertices))

            for i in range(num_vertices):
                vertex_label = int(f.readline().strip())
                merged_data.append(str(vertex_label))

            merged_data.append(f.readline().strip())
            num_edges = int(merged_data[-1])

            for i in range(num_edges):
                _inp = f.readline().strip()
                merged_data.append(_inp)
                edge = tuple(map(int, _inp.split()))
            
    return name_list, "\n".join(merged_data)

if __name__ == "__main__":
    graph_list = sys.argv[1]
    query_graph = sys.argv[2]
    name_list, merged_gfu = (merge_gfu_graphs(graph_list))

    temp_data_path_ = "./tmp_input.gfu"
    temporary_file_ = open(temp_data_path_, 'w')
    temporary_file_.write(merged_gfu)
    temporary_file_.close()

    veq_output_path = "./search-result.txt"
    execution_args = generate_args("./lib/VEQ_S", '-dg', temp_data_path_, '-qg', query_graph, '-o', veq_output_path)
    (rc, std_output, std_error) = execute_binary(execution_args)
    # std_output = str(std_output, encoding='utf-8')
    # std_output_list = std_output.split('\n')
    if rc != 0:
        print("Error occured")
        exit(1)

    found_in = list(map(
        lambda x : name_list[int(x.strip())],
        open(veq_output_path).readlines()
    ))
    print(f"Found in :", *found_in)
