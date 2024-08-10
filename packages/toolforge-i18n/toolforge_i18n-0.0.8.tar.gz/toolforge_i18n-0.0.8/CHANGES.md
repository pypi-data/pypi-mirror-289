# Changelog

## Pre-0.1.0 phase

Prior to the 0.1.0 release, toolforge_i18n is not ready for general use yet.
The following notes only give an overview of what changed,
and there are no migration instructions,
as nobody other than the author should be using these versions of the library.

### 0.0.8 (2024-08-10)

Add Sphinx-built docs, hopefully to be published on Read the Docs.

### 0.0.7 (2024-08-05)

Move Flask-related dependencies to `Flask` extra (which most tools should use).

### 0.0.6 (2024-07-31)

Re-export all members from `toolforge_i18n` (i.e. `__init__.py`)
and make all other modules internal.

### 0.0.5 (2024-07-21)

Republish of 0.0.3 / 0.0.4 with no user-visible changes.

### 0.0.4 (2024-07-21)

Republish of 0.0.3 with no user-visible changes.
Failed to publish to PyPI.

### 0.0.3 (2024-07-21)

Check translations on load by default,
rather than relying on tool developers always running `pytest`.
Failed to publish to PyPI.

### 0.0.2 (2024-07-07)

Improved translation tests,
automatically registering them with a pytest plugin
and showing nicer assertion messages.

### 0.0.1 (2024-06-04)

Initial release.
