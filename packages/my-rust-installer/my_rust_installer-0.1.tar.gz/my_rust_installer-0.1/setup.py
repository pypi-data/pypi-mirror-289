import os
import subprocess
import shlex
from setuptools import setup, find_packages
from setuptools.command.install import install


class CustomInstallCommand(install):
    def run(self):
        self.install_rust_and_agg()
        install.run(self)

    def install_rust_and_agg(self):
        def run_command(command):
            process = subprocess.Popen(
                command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True
            )
            stdout, stderr = process.communicate()
            if process.returncode != 0:
                print(f"Error executing command: {command}")
                print(f"Error message: {stderr.decode('utf-8')}")
                return False
            return True

        # Install Rust
        if not run_command("curl https://sh.rustup.rs -sSf | sh -s -- -y"):
            raise Exception("Failed to install Rust")

        # Source the cargo environment
        cargo_env = os.path.expanduser("~/.cargo/env")
        if os.path.exists(cargo_env):
            with open(cargo_env, "r") as f:
                env_vars = {}
                for line in f:
                    if line.startswith("export "):
                        key, value = line.replace("export ", "").strip().split("=", 1)
                        env_vars[key] = shlex.split(value)[
                            0
                        ]  # Remove quotes if present

            # Update environment variables
            os.environ.update(env_vars)

        # Update PATH to include cargo binary directory
        os.environ["PATH"] = (
            f"{os.path.expanduser('~/.cargo/bin')}:{os.environ['PATH']}"
        )

        # Install agg
        if not run_command("cargo install --git https://github.com/asciinema/agg"):
            raise Exception("Failed to install agg")

        print("Rust and agg installed successfully!")


setup(
    name="my_rust_installer",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],
    author="Your Name",
    author_email="your.email@example.com",
    description="A package to install Rust and agg",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/my_rust_installer",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    cmdclass={
        "install": CustomInstallCommand,
    },
)
