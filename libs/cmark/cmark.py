import info
from Package.CMakePackageBase import *


class subinfo(info.infoclass):
    def setTargets(self):
        self.svnTargets['master'] = 'https://github.com/commonmark/cmark'

        # use latest stable version
        self.defaultTarget = '0.30.1'
        self.targets[self.defaultTarget] = "https://github.com/commonmark/cmark/archive/%s.tar.gz" % self.defaultTarget
        self.archiveNames[self.defaultTarget] = 'cmark-%s.tar.gz' % self.defaultTarget
        self.targetInstSrc[self.defaultTarget] = 'cmark-%s' % self.defaultTarget

        # fix clash of bin artifacts and lib artifacs
        self.patchToApply[self.defaultTarget] = ('cmark-0.30.1-20210816.diff', 1)
        self.patchLevel[self.defaultTarget] = 1

        self.targetDigests["0.30.1"] =  (['9609506bd7473e769452488ef981eb53f082011b1ec6c9b6c73ed57062e25ee6'], CraftHash.HashAlgorithm.SHA256)
        self.description = "CommonMark parsing and rendering library and program in C"

    def setDependencies(self):
        self.runtimeDependencies["virtual/base"] = None

class Package(CMakePackageBase):
    def __init__(self, **args):
        CMakePackageBase.__init__(self)
        self.subinfo.options.configure.args += "-DCMARK_TESTS=OFF"

    def postInstall(self):
        # remove API docs here as there is no build option for that
        baseDir = os.path.join(self.installDir(), os.path.relpath(CraftCore.standardDirs.locations.data, CraftCore.standardDirs.craftRoot()))
        shutil.rmtree(os.path.join(baseDir, "man"), ignore_errors=True)
        return True
