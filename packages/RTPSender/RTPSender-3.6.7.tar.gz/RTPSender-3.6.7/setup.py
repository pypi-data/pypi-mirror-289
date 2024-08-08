from setuptools import setup, find_packages
from setuptools.command.install import install
import os

class CustomInstallCommand(install):
    """Customized setuptools install command - runs custom script."""
    def run(self):
        install.run(self)
        self.execute_post_install()

    def execute_post_install(self):
        post_install_script = os.path.join(os.path.dirname(__file__), 'custom_install.py')
        if os.path.exists(post_install_script):
            import subprocess
            print("Running custom-install script...")
            subprocess.run([self.distribution.get_command_obj('build').executable, post_install_script])

setup(
    name="RTPSender",
    version="3.6.7",
    author="liushihai02",
    author_email="liushihai02@58.com",
    packages=find_packages(),
    install_requires=[
        'scapy',
        'opencv-python',
        'pydub'
        # Note: Do not include 'av' here as it will be handled separately
    ],
    description="A SDK for sending RTP streams",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    python_requires='>=3.9',
    cmdclass={
        'install': CustomInstallCommand,
    },
)
