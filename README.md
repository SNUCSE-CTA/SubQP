# SubQP
SubQP. Handles multiple data graphs given as (name, path) pairs. 

VEQ_S [1, 2] is internally used to solve the problem. 

## Environment
SubQP requires python3 running on a machine with 64 bit CentOS Linux.

## Installation
```sh
git clone https://github.com/SNUCSE-CTA/SubQP
```

## Usage
```sh
python3 SubQP.py <Graph list path> <Query graph path>
```

Graph list file contains name and path for multiple data graphs;
```text
name1 path1
name2 path2
...
```

Query graph path must be a path to GFU file. 

## Output
Outputs list of [name] of graphs which contains the specified query as subgraphs.

## License
Distributed under Apache License 2.0. See LICENSE for more information.

## Reference
[1] Hyunjoon Kim, Yunyoung Choi, Kunsoo Park, Xuemin Lin, Seok-Hee Hong, and Wook-Shin Han. 2021. Versatile Equivalences: Speeding up Subgraph Query Processing and Subgraph Matching. In Proceedings of the 2021 International Conference on Management of Data (SIGMOD '21). Association for Computing Machinery, New York, NY, USA, 925–937. https://doi.org/10.1145/3448016.3457265

[2] Hyunjoon Kim, Yunyoung Choi, Kunsoo Park, Xuemin Lin, Seok-Hee Hong, and Wook-Shin Han. Fast subgraph query processing and subgraph matching via static and dynamic equivalences. The VLDB Journal (2022). https://doi.org/10.1007/s00778-022-00749-x
