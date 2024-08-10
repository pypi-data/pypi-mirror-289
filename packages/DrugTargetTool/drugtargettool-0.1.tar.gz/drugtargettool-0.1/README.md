# DrugTargetTool

DrugTargetTool is a tool for optimizing drug combinations using a genetic algorithm. Targeting the same proteins is crucial for improving treatment efficacy and reducing the likelihood of drug resistance. By simultaneously modulating the same targets, this approach can achieve a more potent therapeutic effect, especially in complex diseases like cancer.

## Methods

DrugTargetTool employs a genetic algorithm to discover optimal drug combinations. By simulating evolutionary processes, the tool efficiently explores potential combinations, evaluating them based on their ability to target key proteins.

## Usage

To use DrugTargetTool, you should have an excel or csv file containing two columns Drug and Target. Import and run:  combination_therapy(file_path = "example.xlsx", num_top_drugs = 5)
## Installation

To install DrugTargetTool, run:

```bash
pip install drugtargettool
