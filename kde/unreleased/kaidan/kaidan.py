import info


class subinfo(info.infoclass):
    def setTargets(self):
        self.description = "A simple, user-friendly Jabber/XMPP client for every device!"
        self.displayName = "Kaidan"

        self.svnTargets['master'] = 'https://anongit.kde.org/kaidan.git'
        for ver in ["0.4.1"]:
            self.targets[ver] = "https://download.kde.org/stable/kaidan/{}/kaidan-{}.tar.xz".format(ver, ver)
            self.archiveNames[ver] = "kaidan-v{}.tar.xz".format(ver)
            self.targetInstSrc[ver] = "kaidan-{}".format(ver)
        self.targetDigests['0.4.1'] = (
            ['a9660e2b9c9d9ac6802f7de9a8e1d29a6d552beffcafca27231682bf1038e03c'], CraftHash.HashAlgorithm.SHA256)
        self.defaultTarget = '0.4.1'

    def setDependencies(self):
        self.runtimeDependencies["libs/qt5/qtbase"] = None
        self.runtimeDependencies["libs/qt5/qtdeclarative"] = None
        self.runtimeDependencies["libs/qt5/qtmultimedia"] = None
        self.runtimeDependencies["libs/qt5/qtsvg"] = None
        self.runtimeDependencies["libs/zxing-cpp"] = None
        self.runtimeDependencies["qt-libs/qxmpp"] = None
        self.runtimeDependencies["kde/frameworks/tier1/kirigami"] = None

from Package.CMakePackageBase import *


class Package(CMakePackageBase):
    def __init__(self):
        CMakePackageBase.__init__(self)

    def createPackage(self):
        self.defines["executable"] = r"bin\kaidan.exe"

        # okular icons
        #self.defines["icon"] = os.path.join(self.packageDir(), "okular.ico")
        #self.defines["icon_png"] = os.path.join(self.packageDir(), ".assets", "150-apps-okular.png")
        #self.defines["icon_png_44"] = os.path.join(self.packageDir(), ".assets", "44-apps-okular.png")

        # this requires an 310x150 variant in addition!
        #self.defines["icon_png_310x310"] = os.path.join(self.packageDir(), ".assets", "310-apps-okular.png")

        return TypePackager.createPackage(self)
