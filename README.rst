AWS Help!
=========

Utility which adds ``-h`` or ``--help`` capabilities to the AWS Cli.

Usage
-----

* Clone the repository and install the package in editable mode.

.. code-block:: console

    $ git clone git@github.com:xames3/aws_help.git
    $ cd aws_help
    $ pip install -e .

* Setup alias in your .zshrc OR .bashrc file.

.. code-block:: console

    alias aws=aws_help

In Action
---------

.. code-block:: console

    $ aws iam -h
    IAM()                                                                    IAM()


    NAME
        iam -

    DESCRIPTION
        Identity and Access Management (IAM) is a web service for securely con-
        trolling access to Amazon Web Services services. With IAM, you can cen-
        trally manage users, security credentials such as access keys, and per-
        missions that control which Amazon Web  Services  resources  users  and
        applications  can  access. For more information about IAM, see Identity
        and Access Management (IAM) and the Identity and Access Management User
        Guide.
