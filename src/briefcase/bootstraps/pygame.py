from briefcase.bootstraps.base import BaseGuiBootstrap


class PygameGuiBootstrap(BaseGuiBootstrap):
    def app_source(self):
        return """\
import importlib.metadata
import os
import sys

import pygame


SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
WHITE = (255, 255, 255)


def main():
    # Linux desktop environments use app's .desktop file to integrate the app
    # to their application menus. The .desktop file of this app will include
    # StartupWMClass key, set to app's formal name, which helps associate
    # app's windows to its menu item.
    #
    # For association to work any windows of the app must have WMCLASS
    # property set to match the value set in app's desktop file. For PPB this
    # is set using environment variable.

    # Find the name of the module that was used to start the app
    app_module = sys.modules["__main__"].__package__
    # Retrieve the app's metadata
    metadata = importlib.metadata.metadata(app_module)

    os.environ["SDL_VIDEO_X11_WMCLASS"] = metadata["Formal-Name"]

    pygame.init()
    pygame.display.set_caption(metadata["Formal-Name"])
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

        screen.fill(WHITE)
        pygame.display.flip()

    pygame.quit()
"""

    def pyproject_requires(self):
        return """
    "pygame~=2.2",
"""

    def pyproject_test_requires(self):
        return """
{%- if cookiecutter.test_framework == "pytest" %}
    "pytest",
{%- endif %}
"""

    def pyproject_table_macOS(self):
        return """
universal_build = true
requires = [
    "std-nslog~=1.0.0",
]
"""

    def pyproject_table_linux(self):
        return """
requires = [
]
"""

    def pyproject_table_linux_system_debian(self):
        return """
system_requires = [
]

system_runtime_requires = [
]
"""

    def pyproject_table_linux_system_rhel(self):
        return """
system_requires = [
]

system_runtime_requires = [
]
"""

    def pyproject_table_linux_system_suse(self):
        return """
system_requires = [
]

system_runtime_requires = [
]
"""

    def pyproject_table_linux_system_arch(self):
        return """
system_requires = [
]

system_runtime_requires = [
]
"""

    def pyproject_table_linux_appimage(self):
        return """
manylinux = "manylinux2014"

system_requires = [
]

linuxdeploy_plugins = [
]
"""

    def pyproject_table_linux_flatpak(self):
        return """
flatpak_runtime = "org.freedesktop.Platform"
flatpak_runtime_version = "22.08"
flatpak_sdk = "org.freedesktop.Sdk"
"""

    def pyproject_table_windows(self):
        return """
requires = [
]
"""

    def pyproject_table_iOS(self):
        return """
supported = false
"""

    def pyproject_table_android(self):
        return """
supported = false
"""

    def pyproject_table_web(self):
        return """
supported = false
"""
