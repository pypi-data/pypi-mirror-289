from typing import Any, Dict

from setuptools_cpp import CMakeExtension, ExtensionBuilder, Pybind11Extension

ext_modules = [
    CMakeExtension(f"socom._multinet", sourcedir=""),
]

def build(setup_kwargs: Dict[str, Any]) -> None:
    setup_kwargs.update(
        {
            "ext_modules": ext_modules,
            "cmdclass": dict(build_ext=ExtensionBuilder),
            "zip_safe": False,
        }
    )
