import info


class subinfo(info.infoclass):
    def registerOptions(self):
        self.parent.package.categoryInfo.platforms = CraftCore.compiler.Platforms.NotWindows & CraftCore.compiler.Platforms.NotAndroid

    def setTargets(self):
        self.versionInfo.setDefaultValues()

        self.description = "KGlobalAccel"

    def setDependencies(self):
        self.buildDependencies["virtual/base"] = None
        self.buildDependencies["kde/frameworks/extra-cmake-modules"] = None
        self.runtimeDependencies["kde/frameworks/tier1/kconfig"] = None
        self.runtimeDependencies["kde/frameworks/tier1/kcoreaddons"] = None
        self.runtimeDependencies["kde/frameworks/tier2/kcrash"] = None
        self.runtimeDependencies["kde/frameworks/tier1/kdbusaddons"] = None
        self.runtimeDependencies["kde/frameworks/tier1/ki18n"] = None
        self.runtimeDependencies["kde/frameworks/tier3/kservice"] = None
        self.runtimeDependencies["kde/frameworks/tier1/kwindowsystem"] = None


from Package.CMakePackageBase import *


class Package(CMakePackageBase):
    def __init__(self):
        CMakePackageBase.__init__(self)
