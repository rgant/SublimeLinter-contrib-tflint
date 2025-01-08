"""
Subclass to call tflint for linting Terraform HCL files

Copied from [patrickrgaffney/SublimeLinter-contrib-terraform](https://github.com/patrickrgaffney/SublimeLinter-contrib-terraform/blob/849c67ef08c2ef9ace1b3b0455919b4b9220698b/linter.py#L9)
"""
import json
import logging

from SublimeLinter.lint import Linter, LintMatch

logger = logging.getLogger('SublimeLinter.plugin.tflint')

class TerraformLinter(Linter):
    """Subclass to call tflint for linting Terraform HCL files"""
    # The executable plus all arguments used to lint. The $file_path
    # will be set by super(), and will be the folder path of the file
    # currently in the active view. The "validate" command only operates
    # on directories (modules), so it's provided here to avoid the
    # command attempting to guess what directory we are at.
    cmd = ('tflint', '--format=json', '--chdir=${file_path}')

    # The tflint command uses a one-based reporting for line and column numbers.
    line_col_base = (1, 1)

    # A dict of defaults for the linter’s settings.
    defaults = {
        'selector': 'source.terraform'
    }

    # Turn off stdin. The validate command requires a directory.
    template_suffix = '-'

    def find_errors(self, output):
        """
        Override the find_errors() output so that we can parse the JSON
        output directly instead of using a multiline regex to walk
        through it.
        """
        data = {}
        try:
            data = json.loads(output)
        except Exception as e:
            logger.error(e)
            self.notify_failure()

        # If there are no errors, return to stop iteration,
        # then yield to turn this function into a generator.
        if not data["issues"] and not data["errors"]:
            return

        # Iterate through the issues, yielding LintMatchs.
        for issue in data['issues']:
            message = issue['message']
            severity = issue["rule"]["severity"]
            line = issue["range"]["start"]["line"] - self.line_col_base[0]
            col = issue["range"]["start"]["column"] - self.line_col_base[1]
            filename = issue["range"]["filename"]

            yield LintMatch(
              filename=filename,
              line=line,
              col=col,
              error_type=severity,
              message=message,
            )

        # Iterate through the errors, yielding LintMatchs.
        for error in data['errors']:
            line, col = 0, 0
            filename = self.context.get("file_name")
            message = "Error"
            severity = error["severity"]

            # Catch the specific error for unsatisfied plugin
            # requirements. The "detail" key is rather long.
            # If a "detail" key was given, we also use that.
            if "summary" in error:
                message = f'{error["summary"]}: {error["message"]}'.replace("\n", " ")
            else:
                message = error['message'].replace("\n", " ")

            # If the error or warning occured on the entire file,
            # there won't be a "range" key, so we use the defaults.
            if "range" in error:
                line = error["range"]["start"]["line"] - self.line_col_base[0]
                col = error["range"]["start"]["column"] - self.line_col_base[1]

                # Only the basename is provided in "filename".
                filename = error["range"]["filename"]

            yield LintMatch(
              filename=filename,
              line=line,
              col=col,
              error_type=severity,
              message=message,
            )
