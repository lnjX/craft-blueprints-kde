# -*- coding: utf-8 -*-
import info
from Package.AutoToolsPackageBase import AutoToolsPackageBase
from Package.CMakePackageBase import *


class subinfo(info.infoclass):
    def setTargets(self):
        for ver in ['1.5.0']:
            tag = ver
            if ver == "1.5.0":
                tag = "1.5"
            self.targets[ver] = f"https://github.com/libunwind/libunwind/releases/download/v{tag}/libunwind-{ver}.tar.gz"
            self.targetInstSrc[ver] = f"libunwind-{ver}"
            self.patchLevel[ver] = 0

        self.targetDigests['1.5.0'] = (['1df20ca7a8cee2f2e61294fa9b677e88fec52e9d5a329f88d05c2671c69fa462f6c18808c97ca9ff664ef57292537a844f00b18d142b1938c9da701ca95a4bab'], CraftHash.HashAlgorithm.SHA512)

        self.description = 'The primary goal of this project is to define a portable and efficient C programming interface (API) to determine the call-chain of a program.'
        self.defaultTarget = '1.5.0'

    def setDependencies(self):
        self.runtimeDependencies["virtual/base"] = None

class Package(AutoToolsPackageBase):
    def __init__(self, **args):
        AutoToolsPackageBase.__init__(self)
        self.subinfo.options.configure.autoreconf = False
        self.platform = ""