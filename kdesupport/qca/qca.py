import info


class subinfo(info.infoclass):
    def setDependencies(self):
        self.runtimeDependencies["virtual/base"] = None
        if self.options.dynamic.buildWithQt6:
            self.runtimeDependencies["libs/qt6/qtbase"] = None
        else:
            self.runtimeDependencies["libs/qt5/qtbase"] = None
        self.runtimeDependencies["libs/openssl"] = None

        # gcrypt currently fails to build for android
        if not CraftCore.compiler.isAndroid:
            self.runtimeDependencies["libs/gcrypt"] = None

        # cyrus-sasl currently fails to build with mingw / for android
        if not CraftCore.compiler.isMinGW():
            self.runtimeDependencies["libs/cyrus-sasl"] = None

    def setTargets(self):
        self.description = "Qt Cryptographic Architecture (QCA)"

        self.svnTargets["master"] = "https://anongit.kde.org/qca.git"

        for ver in ["2.3.5"]:
            self.targets[ver] = f"https://download.kde.org/stable/qca/{ver}/qca-{ver}.tar.xz"
            self.targetDigestUrls[ver] = f"https://download.kde.org/stable/qca/{ver}/qca-{ver}.tar.xz.sha256"
            self.targetInstSrc[ver] = f"qca-{ver}"

        # latest stable version
        self.defaultTarget = "2.3.5"

    def registerOptions(self):
        self.options.dynamic.registerOption("buildWithQt6", False)

from Package.CMakePackageBase import *


class Package(CMakePackageBase):
    def __init__(self, **args):
        CMakePackageBase.__init__(self)
        # the cmake config is not relocatable
        self.subinfo.options.package.disableBinaryCache = True

        # tests fail to build with missing openssl header
        self.subinfo.options.configure.args = "-DBUILD_TESTS=OFF "

        if self.subinfo.options.dynamic.buildWithQt6:
            self.subinfo.options.configure.args += "-DBUILD_WITH_QT6=ON "
