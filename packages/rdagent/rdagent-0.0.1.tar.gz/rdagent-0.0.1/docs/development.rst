=========================
For Development
=========================

🔧Prepare for development
=========================

- Set up the development environment.

   ```bash
   make dev
   ```

- Run linting and checking.

   ```bash
   make lint
   ```

- Some linting issues can be fixed automatically. We have added a command in the Makefile for easy use.

  ```bash
  make auto-lint
  ```


Code Structure
=========================

.. code-block:: text

    📂 src
    ➥ 📂 <project name>: avoid namespace conflict
      ➥ 📁 core
      ➥ 📁 components/A
      ➥ 📁 components/B
      ➥ 📁 components/C
      ➥ 📁 scenarios/X
      ➥ 📁 scenarios/Y
      ➥ 📂 app
    ➥ 📁 scripts

.. list-table::
   :header-rows: 1

   * - Folder Name
     - Description
   * - 📁 core
     - The core framework of the system. All classes should be abstract and usually can't be used directly.
   * - 📁 component/A
     - Useful components that can be used by others (e.g., scenarios). Many subclasses of core classes are located here.
   * - 📁 scenarios/X
     - Concrete features for specific scenarios (usually built based on components or core). These modules are often unreusable across scenarios.
   * - 📁 app
     - Applications for specific scenarios (usually built based on components or scenarios). Removing any of them does not affect the system's completeness or other scenarios.
   * - 📁 scripts
     - Quick and dirty things. These are candidates for core, components, scenarios, and apps.



Conventions
===========


File Naming Convention
----------------------

.. list-table::
   :header-rows: 1

   * - Name
     - Description
   * - `conf.py`
     - The configuration for the module, app, and project.

<!-- TODO: renaming files -->
