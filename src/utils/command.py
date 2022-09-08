import os
import subprocess


class CommandUtils:

    @staticmethod
    def run_command(command: list, flatpak_spawn: bool = None, output: bool = False, decode: bool = True):
        """
        Keep flatpak_spawn as None to automatically assume its value based on
        whether the app is running in a flatpak or not. Set it to True or False
        to override this behavior.
        """
        if flatpak_spawn is None and "FLATPAK_ID" in os.environ:
            flatpak_spawn = True

        if flatpak_spawn:
            command = ["flatpak-spawn", "--host"] + command
            
        if output:
            res = subprocess.check_output(command)
            if decode:
                res = res.decode("utf-8").strip()
            return res

        return subprocess.Popen(command, stdout=subprocess.PIPE)

    @staticmethod
    def check_output(command: list, flatpak_spawn: bool = None, decode: bool = True):
        """Just a wrapper for convenience"""
        return CommandUtils.run_command(command, flatpak_spawn, output=True, decode=decode)
