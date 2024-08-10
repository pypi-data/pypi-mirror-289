"""Unix implementation of userfolders.

Your application should not use this directly; "import userfolders" will
automatically select the correct implementation for the current platform.
"""

import os
import shutil
import subprocess
from enum import StrEnum

# Paths within a user's home directory are, to my knowledge, not as
# standardized on Unix as they are on Windows. The paths returned by this
# module are based on the following references, in order of preference:
#
#  1. Published standards like the XDG Base Directory Specification [1].
#
#  2. De facto standards used by major applications. These are generally
#     safe to use regardless of the operating system distribution. For
#     example, the Desktop and Downloads directories are widely used by
#     major desktop environments and web browsers, respectively.
#
#  3. Other paths commonly found on major operating system distributions.
#     These are not guaranteed to exist on all systems, but are used widely
#     enough that users would reasonably expect us to return them if they
#     exist. For example, many Linux distributions now create Documents,
#     Pictures, Music, and Video folders similar to those found on Windows.
#
# The userfolders module was originally designed from a Windows-centric
# perspective. Because of the many differences between the two systems,
# there are some Windows paths that do not have a direct equivalent on
# Unix, and vice versa. In these cases, userfolders attempts to return the
# nearest functional equivalent, but it is up to the user to ensure their
# application is using the appropriate path for what it seeks to do.
#
# If you know of other applicable standards, or better equivalents than
# the ones used here, please feel free to submit a patch.
#
# References:
# [1] https://specifications.freedesktop.org/basedir-spec/latest/
# [2] https://manpages.org/xdg-user-dir


class _XdgUserDirs(StrEnum):
    """All valid XDG user dirs accessible via the xdg-user-dir command"""

    DESKTOP = "DESKTOP"
    DOWNLOAD = "DOWNLOAD"
    TEMPLATES = "TEMPLATES"
    PUBLICSHARE = "PUBLICSHARE"
    DOCUMENTS = "DOCUMENTS"
    MUSIC = "MUSIC"
    PICTURES = "PICTURES"
    VIDEOS = "VIDEOS"

    def __repr__(self):
        return f"<{self.__class__.__name__}.{self._name_}>"


def _xdg_user_dir_or_default(requested_folder: _XdgUserDirs, default_value: str) -> str:
    default = os.path.expanduser(default_value)
    xdg_user_dirs_path = shutil.which("xdg-user-dir")
    if not xdg_user_dirs_path:
        return default
    out = subprocess.run(
        [xdg_user_dirs_path, str(requested_folder)], capture_output=True, text=True
    ).stdout.rstrip("\n")
    if not out:
        return default
    return out


def _env_or_default(env_name: str, default_value: str) -> str:
    """Return $env_name if specified, otherwise default_value."""

    if env_name:
        value = os.getenv(env_name)
    else:
        value = None

    if value:
        return value
    else:
        return os.path.expanduser(default_value)


def get_appdata() -> str:
    """Return the current user's roaming Application Data folder."""
    # Standardized in the XDG Base Directory Specification
    return _env_or_default("XDG_DATA_HOME", "~/.local/share")


def get_desktop() -> str:
    """Return the current user's Desktop folder."""
    return _xdg_user_dir_or_default(_XdgUserDirs.DESKTOP, "~/Desktop")


def get_downloads() -> str:
    """Return the current user's Downloads folder."""
    return _xdg_user_dir_or_default(_XdgUserDirs.DOWNLOAD, "~/Downloads")


def get_local_appdata() -> str:
    """Return the current user's local Application Data folder."""
    return _env_or_default("XDG_CONFIG_HOME", "~/.local/share")


def get_my_documents() -> str:
    """Return the current user's My Documents folder."""
    return _xdg_user_dir_or_default(_XdgUserDirs.DOCUMENTS, "~/Documents")


def get_my_music():
    """Return the current user's My Music folder."""
    return _xdg_user_dir_or_default(_XdgUserDirs.MUSIC, "~/Music")


def get_my_pictures():
    """Return the current user's My Pictures folder."""
    return _xdg_user_dir_or_default(_XdgUserDirs.PICTURES, "~/Pictures")


def get_my_videos():
    """Return the current user's My Videos folder."""
    return _xdg_user_dir_or_default(_XdgUserDirs.VIDEOS, "~/Videos")


def get_profile():
    """Return the current user's profile folder."""
    return os.path.expanduser("~")
