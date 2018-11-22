{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}
# {{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description }}

This paragraph should contain a high-level description of the package, with a
brief overview of its features and limitations.

{% if is_open_source %}
* Free software: {{ cookiecutter.open_source_license }}
* Documentation: [https://{{ cookiecutter.github_username }}.github.io/{{ cookiecutter.project_slug }}]
{% endif %}

## Readiness

The author of this package is in the process of setting up this
package for optimal usability. The following has already been completed:

- [ ] Documentation
    - A package description has been written in the README
    - Documentation has been generated using `make docs`, committed,
        and pushed to GitHub.
	- GitHub pages have been setup in the project settings
	  with the "source" set to "master branch /docs folder".
- [ ] An initial release
	- In `CHANGELOG.md`, a release date has been added to v0.1.0 (change the YYYY-MM-DD).
	- The release has been marked a release on GitHub.
	- For more info, see the [Software Release Guide](https://cicwi.github.io/software-guidelines/software-release-guide).
- [ ] A conda package
	- Required packages have been added to `setup.py`, for instance,
	  ```
	  requirements = [ ]
	  ```
	  Has been replaced by
	  ```
	  requirements = [
	      'sacred>=0.7.2'
      ]
      ```
	- All "conda channels" that are required for building and
      installing the package have been added to the
      `Makefile`. Specifically, replace
	  ```
      conda_package: install_dev
      	conda build conda/
      ```
	  by
	  ```
      conda_package: install_dev
      	conda build conda/ -c some-channel -c some-other-channel
      ```
    - Conda packages have been built successfully with `make conda_package`.
	- These conda packages have been uploaded to [Anaconda](https://anaconda.org).
	- The installation instructions (below) have been updated.

## Getting Started

It takes a few steps to setup {{ cookiecutter.project_name }} on your
machine. We recommend installing
[Anaconda package manager](https://www.anaconda.com/download/) for
Python 3.

### Installing with conda

Simply install with:
```
conda install -c cicwi {{ cookiecutter.project_slug }}
```

### Installing from source

To install {{ cookiecutter.project_name }}, simply clone this GitHub
project. Go to the cloned directory and run PIP installer:
```
git clone https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug}}.git
cd {{ cookiecutter.project_slug }}
pip install -e .
```

### Running the examples

To learn more about the functionality of the package check out our
examples folder.

## Authors and contributors

* **{{ cookiecutter.full_name }} ** - *Initial work*

See also the list of [contributors](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/contributors) who participated in this project.

## How to contribute

Contributions are always welcome. Please submit pull requests against the `master` branch.

If you have any issues, questions, or remarks, then please open an issue on GitHub.

## License

This project is licensed under the {{ cookiecutter.open_source_license }} - see the [LICENSE.md](LICENSE.md) file for details.
