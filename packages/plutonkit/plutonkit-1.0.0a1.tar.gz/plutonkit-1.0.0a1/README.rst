pluton-kit
==========

Create your project from the current selection we had on the lobby, But
in the future we are working to share your ideas with other developer.

|PIP version| |Build Status|

`Site <https://plutonkit.codehyouka.xyz/>`__ \|
`Docs <https://plutonkit.codehyouka.xyz/api>`__ \| `Architecture
lobby <https://github.com/fonipts/pluton-lobby>`__ \|

Introduction
------------

Building from scratch is quite a dauting task. Constructing your
thought, looking for feature and research it will take alot of your time
in figuring what will you do next. Therefore I decided to create
application where you can choose in different framework, either zero or
hero it will help you alot visualize what framework will you choose.

Installation
------------

In your local machine

.. code:: html

   pip install -e .

In using Pip install

.. code:: html

   pip install plutonkit

Why we need another project template
------------------------------------

There are several template generator that is available public
repository, but they lack of user control in favored of there likes. -
to have condition, for feature that you want and available in
architecture. - Custom template that makes this project unique.

Roadmap
-------

Currently we are in alpha phase had not reach 100% test coverage and
some linter(due to feature I am currently in focused) but still
committed to deliver the improvement if the tool.

Available command you can use at your terminal
----------------------------------------------

The commands must in this format ``plutonkit <Command type>`` \|Command
type \| Description\| Example \| \|————- \| ————- \| ————- \|
\|create_project \| Start creating your project in our listed framework
\| ``plutonkit create_project``\ \| \|cmd \| Executing command using
plutonkit. the details of your command can be found at ``command.yaml``
\| ``plutonkit cmd start`` or ``plkcmd start``\ \| \|help \| See
available command for plutonkit \| ``plutonkit help`` \|

.. figure:: resources/pluton-kit-terminal-design.gif?raw=true
   :alt: terminal

   Alt text

How to use the command
----------------------

Structure of your command, should follow this format

in ``command.yaml`` :

.. code:: html

   script:
     {command_name}:
       command:
       - {executed command}
      

For quick command execution, we had a new abbrevation that called
``plkcmd`` instead of ``plutonkit cmd``.

.. |PIP version| image:: https://img.shields.io/badge/plutonkit-0.01alpha0-brightgreen
   :target: https://pypi.org/project/plutonkit/
.. |Build Status| image:: https://github.com/fonipts/pluton-kit/actions/workflows/cicd.yml/badge.svg?branch=main
   :target: https://github.com/fonipts/pluton-kit/actions