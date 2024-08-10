# thapar-102218071-topsis

## Description

`thapar-102218071-topsis` is a Python package that implements the TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution) method. This method is used for ranking and decision-making tasks. The package allows users to apply TOPSIS on datasets with multiple criteria, providing a score and rank for each alternative.

## Installation

You can install the package via pip:

```bash
pip install thapar-102218071-topsis

## Command Line Usage

python -m my_topsis_package.__main__ <InputDataFile> <Weights> <Impacts> <ResultFileName>
eg 
>python -m my_topsis_package.__main__ 102218071.csv "1,1,1,1,1" "+,+,+,+,+" st.csv