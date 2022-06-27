# -*- coding: utf-8 -*-
import info


class subinfo(info.infoclass):
    def setTargets(self):
        self.versionInfo.setDefaultValues()
        self.patchLevel["5.15.2"] = 2
        self.patchToApply["5.15.5"] = [(".qt-5.15.5-kde", 1)]
        if CraftCore.compiler.isAndroid:
            self.patchToApply["5.15.2"] = [ ("optional-widget-dependency.diff", 1) ]
            self.patchToApply["5.15.5"] = [ ("optional-widget-dependency.diff", 1) ]
        self.patchLevel["5.15.5"] = 1

    def setDependencies(self):
        self.runtimeDependencies["libs/qt5/qtbase"] = None
        self.runtimeDependencies["libs/qt5/qtdeclarative"] = None


from Package.Qt5CorePackageBase import *


class QtPackage(Qt5CorePackageBase):
    def __init__(self, **args):
        Qt5CorePackageBase.__init__(self)


class Package(Qt5CoreSdkPackageBase):
    def __init__(self):
        Qt5CoreSdkPackageBase.__init__(self, classA=QtPackage)
