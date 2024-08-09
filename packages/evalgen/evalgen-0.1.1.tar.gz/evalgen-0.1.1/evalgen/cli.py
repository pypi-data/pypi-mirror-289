import os
import sys
import traceback
import importlib
import inspect

import click
import yaml

from .access import *
from .specification import *
from .lib import *


def load_modules_from_config(config_path):
    """
    Load Python modules from paths specified in a YAML configuration file.
    """
    try:

        if config_path is None:
            # Nothing to do
            return

        if not os.path.exists(config_path):
            return
        
        with open(config_path, 'r') as file:
            config = yaml.safe_load(file)
            
            module_paths = config.get('module_paths', [])
            for path in module_paths:
                if path not in sys.path:
                    sys.path.append(path)

            return config
    except Exception as e:
        traceback.print_exc()
        print(f"Failed to load modules from config: {str(e)}")


def load_subclass(module_name, defaultclass, baseclass):
    """
    Load the subclass of Specification from the specified module.
    """

    if module_name is None:
        return defaultclass
    
    module = importlib.import_module(module_name)
    print(module)
    subclasses = []
    for name, obj in inspect.getmembers(module, inspect.isclass):
        if issubclass(obj, baseclass) and obj is not baseclass:
            subclasses.append(obj)
    if not subclasses:
        raise ValueError("No subclass of Specification found in the module.")
    return subclasses[0]  # Assuming there's only one subclass and returning it


@click.group()
@click.option(
    '--config',
    default='evalgen.yaml',
    help='Path to the configuration YAML file containing module paths'
)
def main(config):
    """
    EvalGen CLI: A command-line interface for generating and applying
    data transformation specifications.
    """
    config = load_modules_from_config(config)

@main.command()
@click.option(
    '--loader-class',
    help='Full path to the loader class (e.g., package.module.ClassName)'
)
@click.option(
    '--loader-param',
    help='Parameter for the loader class (e.g., path to the data source)'
)
@click.option(
    '--output-file',
    help='Path to the output Python file for the specification'
)
def generate_spec(loader_class, loader_param, output_file):
    """
    Generate a specification by interacting with the user to select
    columns and transformations.
    """
    try:
        if loader_class is not None:
            sourceclass = load_subclass(loader_class,
                                        defaultclass=StandardDataSourceLoader,
                                        baseclass=DataSourceLoader)
            instance = sourceclass(loader_param)
        else:
            instance = StandardDataSourceLoader(loader_param)

        # Double check if all is well..
        instance.validate()
        
        df = instance.load()
        generate_specification(df, output_file)
    except Exception as e:
        traceback.print_exc()
        print(f"An error occurred: {str(e)}")


@main.command()
@click.option(
    '--loader-class',
    help='Full path to the loader class (e.g., package.module.ClassName)'
)
@click.option(
    '--spec-class',
    required=False,
    help='Full path to the loader class (e.g., package.module.ClassName)'
)
@click.option(
    '--loader-param',
    required=True,
    help='Parameter for the loader class (e.g., path to the data source)'
)
@click.option(
    '--output-file',
    help='Path to the output JSON file'
)
def apply_spec(loader_class, spec_class, loader_param, output_file):
    """Apply a specification to transform data."""
    try:

        sourceclass = load_subclass(loader_class,
                                    defaultclass=StandardDataSourceLoader,
                                    baseclass=DataSourceLoader)
        instance = sourceclass(loader_param)
        df = instance.load()
        
        specclass = load_subclass(spec_class,
                                  defaultclass=Specification,
                                  baseclass=Specification)
        instance = specclass()
        
        transformed_df = apply_specification(df, instance)

        if output_file is not None:
            transformed_df.to_json(output_file, orient='records', lines=True)
            print(f"Data successfully transformed and saved to {output_file}")
        else:
            print(transformed_df.to_json(orient='records', lines=True))

    except Exception as e:
        traceback.print_exc()
        print(f"An error occurred: {str(e)}")


@main.command()
@click.option(
    "--output-file",
    type=click.Path(),
    default=None,
    help='Path to the output file for the sample YAML configuration.'
)
def sample_config(output_file):
    """
    Generate a sample YAML configuration.
    """
    sample_yaml = {
        'module_paths': [
            '/path/to/your/modules',
            '/another/path/to/modules'
        ]
    }
    yaml_content = yaml.dump(sample_yaml, default_flow_style=False)
    if output_file:
        with open(output_file, 'w') as file:
            file.write(yaml_content)
        print(f"Sample YAML configuration written to {output_file}")
    else:
        print("Sample YAML configuration:\n", file=sys.stderr)
        print(yaml_content)


if __name__ == '__main__':
    main()
