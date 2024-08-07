"""
Helper for OS functions.

Supports windows and linux

"""
# is_admin
# run_as_admin
import ctypes
import os
import pathlib
import platform
import sys

from loguru import logger as LOGGER

import dt_tools.logger.logging_helper as lh
# from dt_tools.console.console_helper import ConsoleInputHelper as InputHelper

class OSHelper():
    """
    Helper class for OS functions.
    
    Supports windows and linux

    Features:
        - OS/hardware detection (Windows/Linux/RaspberryPI)
        - Process detection (running in fg/bg)
        - Is executable in the path?
        - Is process running with admin/root permisssions?
        
        Windowws:
        - is_admin
        - elevate to admin

        Linux:
        - is_root

    Raises:
        OSError: On un-supported OS

    Examples::
        from dt_tools.os.os_helper import OSHelper

        print(f'Is Windows: {OSHelper.is_windows()})
        print(f'Is Linux  : {OSHelper.is_linux()})
        print(f'Is RPi    : {OSHelper.is_raspberrypi()})
        
    """
    @staticmethod
    def is_windows() -> bool:
        """Return True if running in windows else False"""
        return platform.system() == "Windows"
    
    @staticmethod
    def is_linux() -> bool:
        """Return True if running in linux else False"""
        return platform.system() == "Linux"

    @staticmethod
    def is_raspberrypi() -> bool:
        """
        Check if hardware is a Raspberry PI

        Returns:
            True if Raspberry PI else False
        """
        if not OSHelper.is_linux():
            return False
        buffer = []
        with open('/proc/cpuinfo','r') as fh:
            buffer = fh.readlines()
        token = [x for x in buffer if x.startswith('Hardware')]
        hw = token[0].split(":")[1].strip()
        if hw.startswith("BCM"):
            return True
        return False

    @staticmethod
    def is_running_in_foreground():
        """
        Check if process is running in foreground

        Returns:
            True if running in foreground else False
        """
        try:
            if os.getpgrp() == os.tcgetpgrp(sys.stdout.fileno()):
                return True     # is foreground
            return False        # is background
        except AttributeError:
            # Fall back, looks like os.getpgrp() is not available
            return sys.stdout.isatty()
        except OSError:
            return True         # is as a daemon       

    @staticmethod
    def is_running_in_background():
        """
        Check if process is running in background (or as a daemon)

        Returns:
            True if running in background else False
        """
        # return not cls.is_running_in_foreground()
        return not OSHelper.is_running_in_foreground()

    @staticmethod
    def is_executable_available(name: str) -> str:
        """
        Is executable in system path?

        Arguments:
            name: Name of executable.

        Returns:
            Fully qualified executable path if found, else None
        """
        if OSHelper.is_windows():
            sep = ';'
        else:
            sep = ':'
        PATH = os.getenv('PATH')
        exe = None
        for dir in PATH.split(sep):
            exe = pathlib.Path(dir) / name
            if exe.exists():
                break
            if OSHelper.is_windows():
                exe = pathlib.Path(dir) / f'{name}.exe'
                if exe.exists():
                    break
                exe = pathlib.Path(dir) / f'{name}.com'
                if exe.exists():
                    break
        return exe

    @staticmethod
    def is_windows_admin():
        """
        Is process running as Windows Admin

        Returns:
            True if Admin privileges in effect else False
        """
        if OSHelper.is_windows():
            try:
                return ctypes.windll.shell32.IsUserAnAdmin()
            except Exception as ex:
                LOGGER.warning(f'On Windows, but cant check Admin privileges: {repr(ex)}')
                return False            
        
        return False

    @staticmethod
    def is_linux_root():
        """
        Is process running as root?

        Returns:
            True if root else False
        """
        return os.geteuid() == 0
    
    @staticmethod
    def is_god(cls):
        """
        Is process running elevated.

        For windows: admin permissions
        For linux:   root user
        
        Returns:
            True if admin/root else False
        """
        if OSHelper.is_windows:
            return OSHelper.is_windows_admin()
        return OSHelper.is_linux_root()
    
    @staticmethod
    def elevate_to_admin():
        """
        Elevate priviliges to Windows Admin

        User will be presented with a prompt which must be ACK'd for elevation.

        Raises:
            OSError: If not running on Windows.
        """
        
        if not OSHelper.is_windows():
            raise OSError('run_as_admin is ONLY available in Windows')

        if not OSHelper.is_windows_admin():
            # Re-run the program with admin rights
            LOGGER.debug(f'Run Elevated - sys.executable: {sys.executable}   args: {sys.argv}')
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

    
if __name__ == "__main__":
    lh.configure_logger(log_format=lh.DEFAULT_CONSOLE_LOGFMT)
    if OSHelper.is_linux():
        LOGGER.info('Running on Linux')
    if OSHelper.is_raspberrypi():
        LOGGER.info('Running on Raspberry Pi')
    
    LOGGER.info(f'gitx: {OSHelper.is_executable_available("gitx")}')
    LOGGER.info(f'git:  {OSHelper.is_executable_available("git")}')
    if OSHelper.is_windows():
        LOGGER.info('Running on Windows')
        if OSHelper.is_windows_admin():
            LOGGER.info('Windows admin privileges in effect')
            InputHelper.get_input_with_timeout("Press ENTER key", timeout_secs=20)
        else:
            LOGGER.info('Elevate privileges')
            OSHelper.elevate_to_admin()
            LOGGER.info('Shelled as admin')
            InputHelper.wait_with_bypass(2)
