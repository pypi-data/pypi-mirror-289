import os
import sys
import json
import click
from tabulate import tabulate
from ..llm import generate_transformation_code

__all__ = [
    'Specification',
    'generate_specification',
    'apply_specification'
]

class Specification:
    """
    Class to represent a data transformation specification.

    Attributes:
    - columns (list): List of column names.
    - transformation (str): Description of the transformation.
    - code_snippet (str): Code snippet to apply the transformation.
    """
    def __init__(self, config={}):
        self.config = {}
        self.code_snippet = """
transformed_df = df
        """

    def transform(self, df):
        """
        Apply the transformation to the DataFrame.

        Parameters:
        - df (DataFrame): Input pandas DataFrame.

        Returns:
        - DataFrame: Transformed pandas DataFrame.
        """
        # Execute the transformation code snippet
        local_vars = {'df': df}
        exec(self.code_snippet, globals(), local_vars)
        return local_vars.get('transformed_df', df)


def generate_specification(df, query_params):
    """
    Generate a data transformation specification interactively and save it to a Python file.

    Parameters:
    - df (DataFrame): Input pandas DataFrame.
    - output_file (str): Path to the output Python file.
    - query_params (dict): Query params to replay
    """

    print("Available data:")
    data = [{
        "column": c,
        "type": df[c].dtype,
        "sample": [str(x)[:20] for x in df[c].sample(3, replace=True).values]
    } for c in df.columns]
    print(tabulate(data))

    context = "The input is a table with the following columns:\n"
    for d in data:
        d['sample'] = "; ".join(d['sample'])
        context += f"%(column)s: type = %(type)s , sample = %(sample)s\n" % d

    inputs = []
    print("Describe the transformation you want to apply")
    while True:
        line = input()
        if line == '':
            break
        inputs.append(line)
    transformation = "\n".join(inputs)

    template = """
from evalgen import Specification

class GeneratedSpecification(Specification):

    def get_query_params(self):
        '''
        Query parameters used to select data
        '''
        return %(query_params)s

    def transform(self, df):
        {code_snippet}
        return transformed_df

    """ % {
        "query_params": json.dumps(query_params)
    }

    print("Context is", context)
    print("Template is", template)

    code = generate_transformation_code(context,
                                        transformation,
                                        template)

    return code

def apply_specification(df, spec):
    """
    Apply a specification to transform a DataFrame.

    Parameters:
    - df (DataFrame): Input pandas DataFrame.
    - spec_file (class): Path to the specification Python file.

    Returns:
    - DataFrame: Transformed pandas DataFrame.
    """

    assert isinstance(spec, Specification)

    # Apply the transformation
    transformed_df = spec.transform(df)

    return transformed_df
