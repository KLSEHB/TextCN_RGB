We propose a general framework for using complex network metrics and convolutional neural networks to detect software vulnerabilities, named TextCN-RGB. To evaluate TextCN-RGB, we construct a dataset of program functions labeled as vulnerable or non-vulnerable, and transform each function into a program dependence graph (PDG).

At a high level, each node in the PDG corresponds to a statement or operation in the program. To capture the structural and semantic properties of the code, we apply K-shell decomposition, degree centrality, and the HITS algorithm to analyze the importance and influence of each node. The resulting metric values are combined into a three-dimensional representation, which is then converted into an image suitable for convolutional neural network (CNN) training.

Our dataset focuses on real-world C/C++ programs containing vulnerable and non-vulnerable functions. Each function is represented as a PDG-based image, forming a labeled dataset for supervised learning. In total, the dataset consists of X vulnerable functions and Y non-vulnerable functions.

Four types of vulnerability-related patterns are considered:

Control dependence nodes: capturing vulnerabilities related to improper control flow and condition checks.

Data dependence nodes: capturing vulnerabilities related to variable use, improper validation, and unsafe data propagation.

Structural centrality: vulnerabilities that arise from highly connected nodes (e.g., improper pointer or array usage in critical positions).

Semantic influence nodes: vulnerabilities that emerge due to critical operations identified by HITS authority/hub scores (e.g., unsafe API or library interactions).



Our approach consists of five main steps: first, CodeScript\_new.py is executed to perform program slicing; second, joern\_graph\_gen.py is used to generate program dependence graphs (.dot files); third, ImageGeneration.py applies complex network metrics, including K-shell decomposition, degree centrality, and the HITS algorithm, to convert the PDGs into images; fourth, split\_train\_test.py is employed to divide the data into training and testing sets; finally, classification.py is used to train the convolutional neural network and perform vulnerability classification.

