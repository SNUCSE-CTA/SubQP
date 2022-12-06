# SubgraphQueryProcessing
Subgraph Query Processing. Handles multiple data graphs given as (name, path) pairs. 

VEQ-S [1] is internally invoked to solve the problem. 

## Environment
This program requires VEQ executable file. 

## Installation
```sh
git clone https://github.com/SNUCSE-CTA/SubgraphQueryProcessing
```

## Usage
```sh
python SubgraphQueryProcessing.py <VEQ binary path> <Graph list path> <Query graph path>
```

Graph list file contains name and path for multiple data graphs;
```text
name1 path1
name2 path2
...
```

Query graph path must be a path to GFU file. 

## License
Distributed under Apache License 2.0. See LICENSE for more information.

## Reference
[1] Hyunjoon Kim, Yunyoung Choi, Kunsoo Park, Xuemin Lin, Seok-Hee Hong, and Wook-Shin Han. 2021. Versatile Equivalences: Speeding up Subgraph Query Processing and Subgraph Matching. In Proceedings of the 2021 International Conference on Management of Data (SIGMOD '21). Association for Computing Machinery, New York, NY, USA, 925–937. https://doi.org/10.1145/3448016.3457265