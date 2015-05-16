========
sgeparse
========

Simple python module for parsing the output of SGE qstat. There is only one top level function: ``get_jobs`` which returns a list of dictionaries of currently queued (running or waiting) jobs.

------------
Requirements
------------

The only requirements are Python version 2.7+ or 3.3+. All code uses the standard library. The binary ``qstat`` must be available and in your ``$PATH``.

-------
Example
-------

::

    >>> from sgeparse import get_jobs
    >>> jobs = get_jobs()
    >>> # => {"name": "jobname", "owner": "me", ... }

The user argument can be used to specify which user to query:

::

    >>> from sgeparse import get_jobs
    >>> jobs = get_jobs(user='nobody')
    >>> # => {"name": "jobname", "owner": "nobody", ... }

--------------
Available keys
--------------

- ``job_number``
- ``priority``
- ``name``
- ``owner``
- ``state``
- ``start_time``
- ``queue``
- ``host``
- ``slots``
