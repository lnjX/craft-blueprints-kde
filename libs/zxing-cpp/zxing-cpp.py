# -*- coding: utf-8 -*-
import info
from Package.CMakePackageBase import *


class subinfo(info.infoclass):
    def setDependencies(self):
        #self.runtimeDependencies["virtual/base"] = None
        #self.runtimeDependencies["libs/qt5/qtbase"] = None
        #self.buildDependencies["libs/qt5/qttools"] = None
        pass

    def setTargets(self):
        self.svnTargets['master'] = 'https://github.com/nu-book/zxing-cpp.git'
        for ver in ["1.0.7"]:
            self.targets[ver] = "https://github.com/nu-book/zxing-cpp/archive/v%s.tar.gz" % ver
            self.archiveNames[ver] = "zxing-cpp-v%s.tar.gz" % ver
            self.targetInstSrc[ver] = 'zxing-cpp-%s' % ver
        self.targetDigests['1.0.7'] = (
            ['b6eacc2ca25fcf7d2ceb07900eae1f6bdef8a349c9d373df3b8481116355afbb'], CraftHash.HashAlgorithm.SHA256)
        self.defaultTarget = '1.0.7'


class Package(CMakePackageBase):
    def __init__(self, **args):
        CMakePackageBase.__init__(self)

