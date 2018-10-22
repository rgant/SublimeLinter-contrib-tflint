SublimeLinter-contrib-tflint
================================

[![Build Status](https://travis-ci.org/mcw0933/SublimeLinter-contrib-tflint.svg?branch=master)](https://travis-ci.org/mcw0933/SublimeLinter-contrib-tflint)

This linter plugin for [SublimeLinter](https://github.com/SublimeLinter/SublimeLinter) provides an interface to [tflint](https://github.com/wata727/tflint). It will be used with Terraform HCL files that have the `source.terraform` syntax.  You may need to install a Terraform syntax package to Sublime to use it.

## Installation
SublimeLinter must be installed in order to use this plugin.

Please use [Package Control](https://packagecontrol.io) to install the linter plugin.

Before installing this plugin, you must ensure that `tflint` is installed on your system.  Follow the instructions in the [tflint README](https://github.com/wata727/tflint/blob/master/README.md)

In order for `tflint` to be executed by SublimeLinter, you must ensure that its path is available to SublimeLinter. The docs cover [troubleshooting PATH configuration](http://sublimelinter.readthedocs.io/en/latest/troubleshooting.html#finding-a-linter-executable).

## Settings
- SublimeLinter settings: http://sublimelinter.readthedocs.org/en/latest/settings.html
- Linter settings: http://sublimelinter.readthedocs.org/en/latest/linter_settings.html
