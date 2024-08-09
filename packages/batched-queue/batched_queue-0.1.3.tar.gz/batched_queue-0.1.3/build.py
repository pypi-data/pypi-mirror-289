import os
from pathlib import Path
from typing import Any

from setuptools import Extension

root = Path(__file__).parent

IS_DEBUG = os.getenv("EXT_BUILD_DEBUG", False)
print("Build File Imported")

debug_macros = []
debug_cythonize_kw: dict[str, Any] = {"force": True}
debug_include_path = []

if IS_DEBUG:
    print("Extension IS_DEBUG=True!")
    # Adding cython line trace for coverage report
    debug_macros += ("CYTHON_TRACE_NOGIL", 1), ("CYTHON_TRACE", 1)
    # Adding upper directory for supporting code coverage when running tests
    # inside the cython package
    debug_include_path += [".."]
    # Some extra info for cython compilator
    debug_cythonize_kw.update(
        {
            "gdb_debug": True,
            "force": True,
            "annotate": True,
            "compiler_directives": {"linetrace": True, "profile": True, "binding": True},
        }
    )

extensions = [
    Extension(
        "*",
        [
            str(file.relative_to(root))
            for file in Path(root, "src").rglob("*.pyx")
            if file.name != "__init__.py"
        ],
        define_macros=debug_macros,
    ),
]
try:
    from Cython.Build import cythonize
except ImportError:
    # Got to provide this function. Otherwise, poetry will fail
    def build(setup_kwargs):
        print("Build without Cython")


# Cython is installed. Compile
else:
    # This function will be executed in setup.py:
    def build(setup_kwargs):
        print("Build with Cython")
        # Build
        setup_kwargs.update(
            {
                "ext_modules": cythonize(extensions, language_level="3", **debug_cythonize_kw),
            }
        )
