[![Download](https://api.bintray.com/packages/helmesjo/public-conan/winflexbison%3Ahelmesjo/images/download.svg) ](https://bintray.com/helmesjo/public-conan/winflexbison%3Ahelmesjo/_latestVersion)
[![Build Status](https://travis-ci.org/helmesjo/conan-winflexbison.svg?branch=stable%2F2.5.14)](https://travis-ci.org/helmesjo/conan-winflexbison)
[![Build status](https://ci.appveyor.com/api/projects/status/github/helmesjo/conan-winflexbison?branch=stable%2F2.5.14&svg=true)](https://ci.appveyor.com/project/helmesjo/conan-winflexbison)

[Conan.io](https://conan.io) package recipe for [*winflexbison*](https://sourceforge.net/projects/winflexbison/).

Win flex-bison is a windows port of                     the Flex (the fast lexical analyser) and                     Bison (GNU parser generator).

The packages generated with this **conanfile** can be found on [Bintray](https://bintray.com/helmesjo/public-conan/winflexbison%3Ahelmesjo).

## For Users: Use this package

### Basic setup

    $ conan install winflexbison/2.5.14@helmesjo/stable

### Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*

    [requires]
    winflexbison/2.5.14@helmesjo/stable

    [generators]
    cmake

Complete the installation of requirements for your project running:

    $ mkdir build && cd build && conan install ..

Note: It is recommended that you run conan install from a build directory and not the root of the project directory.  This is because conan generates *conanbuildinfo* files specific to a single build configuration which by default comes from an autodetected default profile located in ~/.conan/profiles/default .  If you pass different build configuration options to conan install, it will generate different *conanbuildinfo* files.  Thus, they should not be added to the root of the project, nor committed to git.

## For Packagers: Publish this Package

The example below shows the commands used to publish to helmesjo conan repository. To publish to your own conan respository (for example, after forking this git repository), you will need to change the commands below accordingly.

## Build and package

The following command both runs all the steps of the conan file, and publishes the package to the local system cache.  This includes downloading dependencies from "build_requires" and "requires" , and then running the build() method.

    $ conan create helmesjo/stable



## Add Remote

    $ conan remote add helmesjo "https://api.bintray.com/conan/helmesjo/public-conan"

## Upload

    $ conan upload winflexbison/2.5.14@helmesjo/stable --all -r helmesjo


## Conan Recipe License

NOTE: The conan recipe license applies only to the files of this recipe, which can be used to build and package winflexbison.
It does *not* in any way apply or is related to the actual software being packaged.

[MIT](https://github.com/helmesjo/conan-winflexbison/blob/stable/2.5.14/LICENSE)
