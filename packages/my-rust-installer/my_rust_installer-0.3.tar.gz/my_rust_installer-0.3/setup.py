import os
import subprocess
import sys
from setuptools import setup, find_packages
from setuptools.command.install import install

class CustomInstallCommand(install):
    def run(self):
        try:
            self.install_rust_and_agg()
        except Exception as e:
            print(f"Error during installation: {e}", file=sys.stderr)
            raise
        install.run(self)

    def install_rust_and_agg(self):
        def run_command(command):
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            stdout, stderr = process.communicate()
            if process.returncode != 0:
                raise Exception(f"Error executing command: {command}\nError message: {stderr.decode('utf-8')}")
            return stdout.decode('utf-8')

        home_dir = os.path.expanduser("~")
        cargo_bin = os.path.join(home_dir, ".cargo", "bin")

        print("Installing Rust...")
        run_command(f"curl https://sh.rustup.rs -sSf | sh -s -- -y --no-modify-path")
        
        print("Updating PATH...")
        os.environ["PATH"] = f"{cargo_bin}:{os.environ['PATH']}"
        
        # Determine the user's shell and corresponding config file
        shell = os.environ.get("SHELL", "").split("/")[-1]
        if shell == "bash":
            config_file = os.path.join(home_dir, ".bashrc")
        elif shell == "zsh":
            config_file = os.path.join(home_dir, ".zshrc")
        else:
            config_file = os.path.join(home_dir, ".profile")
        
        # Append PATH update to the shell config file
        with open(config_file, "a") as f:
            f.write(f'\nexport PATH="{cargo_bin}:$PATH"\n')
        
        print("Installing agg...")
        run_command(f"{cargo_bin}/cargo install --git https://github.com/asciinema/agg")
        
        print("Verifying installation...")
        cargo_version = run_command(f"{cargo_bin}/cargo --version")
        agg_version = run_command(f"{cargo_bin}/agg --version")
        
        print(f"Cargo installed: {cargo_version}")
        print(f"agg installed: {agg_version}")

        print("Rust and agg installed successfully!")
        print(f"Please restart your shell or run 'source {config_file}' to update your PATH.")

setup(
    name="my_rust_installer",
    version="0.3",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],
    author="Your Name",
    author_email="your.email@example.com",
    description="A package to install Rust and agg for a non-root user",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/my_rust_installer",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    cmdclass={
        'install': CustomInstallCommand,
    },
)