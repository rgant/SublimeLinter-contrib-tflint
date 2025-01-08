"""Subclass to call tflint for linting Terraform HCL files"""
from SublimeLinter.lint import Linter  # or NodeLinter, PythonLinter, ComposerLinter, RubyLinter


class TerraformLinter(Linter):
    """Subclass to call tflint for linting Terraform HCL files"""
    cmd = ('tflint', '--chdir=${file_path}' '--filter=${file}')
    regex = (
        r'^.+?(?:(?P<error>ERROR)|(?P<warning>(?:(WARNING|NOTICE)))):(?P<line>\d+) (?P<message>.+)'
    )
    defaults = {
        'selector': 'source.terraform'
    }
    tempfile_suffix = '-'
