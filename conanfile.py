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
    # Indicates License type of the packaged library
    license = "MIT"

    # Packages the license for the conanfile.py
    exports = ["LICENSE.md"]

    # Remove following lines if the target lib does not use cmake.
    exports_sources = ["CMakeLists.txt"]
    generators = "cmake"

    # Options may need to change depending on the packaged library.
    settings = "os", "arch", "compiler", "build_type"
    options = {}
    default_options = ""

    # Custom attributes for Bincrafters recipe conventions
    source_subfolder = "source_subfolder"
    build_subfolder = "build_subfolder"

    # Use version ranges for dependencies unless there's a reason not to
    # Update 2/9/18 - Per conan team, ranges are slow to resolve.
    # So, with libs like zlib, updates are very rare, so we now use static version


    requires = ()

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

        #Rename to "source_subfolder" is a convention to simplify later steps
        os.rename(extracted_dir, self.source_subfolder)

    def configure_cmake(self):
        cmake = CMake(self, set_cmake_flags=True)
        cmake.configure(build_folder=self.build_subfolder)
        return cmake

    def build(self):
        cmake = self.configure_cmake()
        cmake.build()

    def package(self):
        self.copy(pattern="LICENSE", dst="licenses", src=self.source_subfolder)

        bison_folder = os.path.join(self.source_subfolder, "bison")
        self.copy(pattern="data/*", dst="bin", src=bison_folder)
        self.copy(pattern="*.exe", dst="bin", keep_path=False)
        self.copy(pattern="*.h", dst="include", keep_path=False)

    def package_info(self):
        self.env_info.path.append(os.path.join(self.package_folder, "bin"))
        self.env_info.path.append(os.path.join(self.package_folder, "include"))