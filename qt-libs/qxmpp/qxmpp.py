# -*- coding: utf-8 -*-
import info
from Package.CMakePackageBase import *


class subinfo(info.infoclass):
    def setDependencies(self):
        self.runtimeDependencies["virtual/base"] = None
        self.runtimeDependencies["libs/qt5/qtbase"] = None
        self.buildDependencies["libs/qt5/qttools"] = None

    def setTargets(self):
        self.svnTargets['master'] = 'https://github.com/qxmpp-project/qxmpp.git'
        for ver in ["0.9.3", "1.0.0"]:
            self.targets[ver] = "https://github.com/qxmpp-project/qxmpp/archive/v%s.tar.gz" % ver
            self.archiveNames[ver] = "qxmpp-v%s.tar.gz" % ver
            self.targetInstSrc[ver] = 'qxmpp-%s' % ver
        self.targetDigests['0.9.3'] = (
            ['13f5162a1df720702c6ae15a476a4cb8ea3e57d861a992c4de9147909765e6de'], CraftHash.HashAlgorithm.SHA256)
        self.targetDigests['1.0.0'] = (
            ['bf62ac8d0b5741b3cb07ea92780b279d5c34d000dc7401d6c20a9b77865a5c1e'], CraftHash.HashAlgorithm.SHA256)
        self.defaultTarget = '1.0.0'


class Package(CMakePackageBase):
    def __init__(self, **args):
        CMakePackageBase.__init__(self)

        self.subinfo.options.configure.args = "-DBUILD_EXAMPLES=OFF -DBUILD_TESTS=OFF"
