# -*- coding: utf-8 -*-
import info

class subinfo(info.infoclass):
    def setTargets(self):
        for ver in ['0.1.3']:
            self.targets[ver] = 'https://gitea.nouspiro.space/nou/libXISF/archive/v%s.tar.gz' % ver
            self.archiveNames[ver] = "libxisf-%s.tar.gz" % ver
            self.targetInstSrc[ver] = 'libxisf'
        self.description = 'A C++ library that can read and write XISF files produced by PixInsight.'
        self.defaultTarget = '0.1.3'

    def setDependencies(self):
        self.buildDependencies["dev-utils/pkg-config"] = None
        self.runtimeDependencies["virtual/base"] = None
        self.runtimeDependencies["libs/qt5/qtbase"] = None
        
from Package.CMakePackageBase import *

class Package(CMakePackageBase):
    def __init__(self, **args):
        CMakePackageBase.__init__(self)
        root = str(CraftCore.standardDirs.craftRoot())
        craftLibDir = os.path.join(root,  'lib')
        self.subinfo.options.configure.args = "-DCMAKE_MACOSX_RPATH=1 -DCMAKE_INSTALL_RPATH=" + craftLibDir

