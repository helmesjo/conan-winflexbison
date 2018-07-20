#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, CMake, tools
from conans.errors import ConanException
import os


class LibnameConan(ConanFile):
    name = "winflexbison"
    version = "2.5.14"
    description =   "Win flex-bison is a windows port of \
                    the Flex (the fast lexical analyser) and \
                    Bison (GNU parser generator)."
                    
    url = "https://github.com/helmesjo/conan-winflexbison"
    homepage = "https://sourceforge.net/projects/winflexbison/"
    author = "helmesjo <helmesjo@gmail.com>"
    license = "GPLv3"
    exports = ["LICENSE.md"]
    exports_sources = ["CMakeLists.txt"]

    generators = "cmake"
    settings = "os", "arch", "compiler", "build_type"
    options = {}
    default_options = ""
    requires = ()

    source_subfolder = "source_subfolder"
    build_subfolder = "build_subfolder"

    def config_options(self):
        if self.settings.os == 'Windows':
            del self.options.fPIC
            version = float(self.settings.compiler.version.value)
            if version <= 12.0:
                self.deps_cpp_info.defines.append("snprintf=_snprintf") # "snprintf" not available in older VS (<= VS 2013)
        else:
            raise ConanException("{} is only supported on Windows.".format(self.name))

    def source(self):
        source_url = "https://github.com/lexxmark/winflexbison"
        tools.get("{0}/archive/v{1}.tar.gz".format(source_url, self.version))
        extracted_dir = self.name + "-" + self.version

        # Rename to "source_subfolder" is a convention to simplify later steps
        os.rename(extracted_dir, self.source_subfolder)

    def configure_cmake(self):
        cmake = CMake(self, set_cmake_flags=True)
        cmake.configure(build_folder=self.build_subfolder)
        return cmake

    def build(self):
        cmake = self.configure_cmake()
        cmake.build()

    def package(self):
        self.copy(pattern="flex/src/COPYING", dst="licenses/flex", src=self.source_subfolder, keep_path=False)
        self.copy(pattern="bison/src/COPYING", dst="licenses/bison", src=self.source_subfolder, keep_path=False)

        bison_folder = os.path.join(self.source_subfolder, "bison")
        self.copy(pattern="data/*", dst="bin", src=bison_folder, keep_path=True)
        self.copy(pattern="*win_flex.exe", dst="bin", keep_path=False)
        self.copy(pattern="*win_bison.exe", dst="bin", keep_path=False)

        with tools.chdir(os.path.join(self.package_folder, "bin")):
            os.rename('win_flex.exe', 'flex.exe')
            os.rename('win_bison.exe', 'bison.exe')

    def package_info(self):
        self.env_info.path.append(os.path.join(self.package_folder, "bin"))
        self.env_info.path.append(os.path.join(self.package_folder, "include"))