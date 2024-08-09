import os
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import requests

__all__ = [
    'generate_transformation_code'
]
def access_openai():
    """
    Access the OpenAI API using the API key from environment variables.

    Returns:
    - OpenAI: Instance of the OpenAI class.

    Raises:
    - ValueError: If the OPENAI_API_KEY is not found in environment variables.
    """
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise ValueError("OPENAI_API_KEY not found in environment variables")
    
    llm = OpenAI(api_key=api_key)
    return llm

def access_perplexity():
    """
    Access the Perplexity API using the API key from environment variables.

    Returns:
    - function: A function to make requests to the Perplexity API.

    Raises:
    - ValueError: If the PPLX_API_KEY is not found in environment variables.
    """
    api_key = os.getenv('PPLX_API_KEY')
    if not api_key:
        raise ValueError("PPLX_API_KEY not found in environment variables")
    
    def call_perplexity(model, messages):
        url = "https://api.perplexity.ai/chat/completions"
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "model": model,
            "messages": messages
        }
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()
    
    return call_perplexity

def generate_transformation_code(columns, transformation,
                                 template,
                                 use_perplexity=False):
    """
    Generate a Python class definition for transforming data.

    Parameters:
    - columns (list): List of column names to include.
    - transformation (str): Description of the transformation.
    - use_perplexity (bool): Whether to use Perplexity API instead of OpenAI.

    Returns:
    - str: Class definition as a string.
    """

    if use_perplexity:
        call_perplexity = access_perplexity()
        model = "pplx-7b-online"  # Example model name
        messages = [
            {"role": "system", "content": "Generate a Python code snippet."},
            {"role": "user", "content": f"The columns to include are: {columns}. The transformation to apply is: {transformation}. Apply the code snippet to this code template and format the output: {template}"}
        ]
        response = call_perplexity(model, messages)
        code_snippet = response['choices'][0]['message']['content']
    else:
        llm = access_openai()
        prompt = PromptTemplate(
            input_variables=["columns", "transformation", "template"],
            template=(
                "Generate a Python code snippet that transforms a DataFrame. "
                "The columns to include are: {columns}. \n"
                "The transformation to apply is: {transformation}. \n"
                "Update the following code template with the columns and code snippet and format the output: {template}\n"
                "Provide only final output python code"
            )
        )
        chain = LLMChain(llm=llm, prompt=prompt)
        code_snippet = chain.run(columns=columns, transformation=transformation, template=template)
        
    return code_snippet
