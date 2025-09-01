We propose a general framework for detecting software vulnerabilities by leveraging complex network metrics and convolutional neural networks, named TextCN-RGB. To evaluate TextCN-RGB, we construct a dataset of program functions labeled as vulnerable or non-vulnerable, and transform each function into a Program Dependence Graph (PDG).

At a high level, each node in the PDG corresponds to a statement or operation in the program. To capture the structural and semantic properties of the code, we apply K-shell decomposition, degree centrality, and the HITS algorithm to analyze the importance and influence of each node. The resulting metric values are combined into a three-dimensional representation, which is then converted into an image suitable for convolutional neural network (CNN) training.

Our dataset focuses on real-world C/C++ programs containing vulnerable and non-vulnerable functions. Each function is represented as a PDG-based image, forming a labeled dataset for supervised learning. In total, the dataset consists of X vulnerable functions and Y non-vulnerable functions.

We consider four types of vulnerability-related patterns:

Control dependence nodes: capturing vulnerabilities related to improper control flow and condition checks;

Data dependence nodes: capturing vulnerabilities related to variable use, improper validation, and unsafe data propagation;

Structural centrality: vulnerabilities arising from highly connected nodes (e.g., improper pointer or array usage in critical positions);

Semantic influence nodes: vulnerabilities that emerge due to critical operations identified by HITS authority/hub scores (e.g., unsafe API or library interactions).

Our approach consists of the following steps:

The Code folder is used to extract vulnerability-critical paths. After decompressing the relevant files, CodeScript_new.py is executed to perform program slicing;

The dataset folder contains various datasets, among which the obfuscate folder stores adversarial example datasets;

The py folder includes multiple Python scripts, where joern_graph_gen.py is used to generate Program Dependence Graphs (.dot files);

ImageGeneration.py applies complex network metrics (including K-shell decomposition, degree centrality, and the HITS algorithm) to convert PDGs into images;

split_train_test.py is employed to divide the dataset into training and testing subsets;

Finally, classification.py is executed to train the convolutional neural network and perform vulnerability classification.
