import os
import subprocess
import sys
from setuptools import setup, find_packages
from setuptools.command.install import install

class PostInstallCommand(install):
    def run(self):
        install.run(self)
        self.install_rust()
        self.install_agg()

    def install_rust(self):
        home = os.path.expanduser("~")
        rustup_init = os.path.join(home, "rustup-init")
        
        # Download rustup-init
        subprocess.check_call([
            "curl", "--proto", "=https", "--tlsv1.2", "-sSf",
            "https://sh.rustup.rs", "-o", rustup_init
        ])
        
        # Make rustup-init executable
        os.chmod(rustup_init, 0o755)
        
        # Run rustup-init with user-level installation
        subprocess.check_call([
            rustup_init, "-y", 
            "--no-modify-path",
            "--default-toolchain", "stable"
        ])
        
        # Clean up
        os.remove(rustup_init)
        
        # Update PATH for the current process
        os.environ["PATH"] = f"{home}/.cargo/bin:{os.environ['PATH']}"
        
        # Source cargo environment
        if sys.platform != "win32":
            cargo_env = os.path.join(home, ".cargo", "env")
            subprocess.check_call(f"source {cargo_env}", shell=True, executable="/bin/bash")

    def install_agg(self):
        subprocess.check_call([
            os.path.expanduser("~/.cargo/bin/cargo"),
            "install", "--git", "https://github.com/asciinema/agg"
        ])

setup(
    name="r-a-installer",
    version="0.1",
    packages=find_packages(),
    cmdclass={
        'install': PostInstallCommand,
    },
    # other setup parameters...
)