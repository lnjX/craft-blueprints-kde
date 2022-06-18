# -*- coding: utf-8 -*-
# Copyright (c) 2019-2020 by Gilles Caulier <caulier dot gilles at gmail dot com>
# Copyright (c) 2019-2020 by Ben Cooksley <bcooksley at kde dot org>
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE REGENTS AND CONTRIBUTORS ``AS IS'' AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE REGENTS OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
# OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
# OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
# SUCH DAMAGE.

# NOTE: see relevant phabricator entry https://phabricator.kde.org/T12071

import zipfile
import requests
import info

class subinfo(info.infoclass):
    def setTargets(self):
        self.svnTargets["master"] = 'https://anongit.kde.org/digikam.git'
        self.defaultTarget        = "master"
        self.displayName          = "digiKam"
        self.webpage              = "https://www.digikam.org"
        self.description          = "Professional Photo Management with the Power of Open Source"

    def setDependencies(self):

        # For i18n extraction

        if CraftCore.compiler.isWindows:
            self.buildDependencies["dev-utils/subversion"]              = None

        self.runtimeDependencies["virtual/base"]                        = None
        self.buildDependencies["kde/frameworks/extra-cmake-modules"]    = None
        self.buildDependencies["dev-utils/flexbison"]                   = None

        # digiKam mediaPlayer is not yet fully ported to FFMPEG 5 API

        self.runtimeDependencies["libs/ffmpeg"]                         = "4.4"

        self.runtimeDependencies["libs/opencv/opencv"]                  = None
        self.runtimeDependencies["libs/sqlite"]                         = None
        self.runtimeDependencies["libs/x265"]                           = None
        self.runtimeDependencies["libs/tiff"]                           = None

        # do not force boost deps (see: https://phabricator.kde.org/T12071#212690)

        #self.runtimeDependencies["libs/boost/boost-system"]            = "default"
        #self.runtimeDependencies["libs/boost"]                         = None

        self.runtimeDependencies["libs/expat"]                          = None
        self.runtimeDependencies["libs/lcms2"]                          = None
        self.runtimeDependencies["libs/eigen3"]                         = None
        self.runtimeDependencies["libs/exiv2"]                          = None
        self.runtimeDependencies["libs/lensfun"]                        = None
        self.runtimeDependencies["libs/libpng"]                         = None
        self.runtimeDependencies["libs/libxslt"]                        = None
        self.runtimeDependencies["libs/libxml2"]                        = None
        self.runtimeDependencies["libs/openal-soft"]                    = None
        self.runtimeDependencies["libs/pthreads"]                       = None
        self.runtimeDependencies["libs/libjpeg-turbo"]                  = None
        self.runtimeDependencies["libs/qt5/qtbase"]                     = None
        self.runtimeDependencies["libs/qt5/qtsvg"]                      = None
        self.runtimeDependencies["libs/qt5/qtimageformats"]             = None
        self.runtimeDependencies["libs/qt5/qtxmlpatterns"]              = None
        self.runtimeDependencies["libs/libass"]                         = None
        self.runtimeDependencies["libs/libusb"]                         = None

        if CraftCore.compiler.isMinGW():

            # mingw-based builds need this

            self.runtimeDependencies["libs/runtime"]                    = None

            # QtWebEngine do not compile with MinGW

            self.runtimeDependencies["libs/qt5/qtwebkit"]               = None

        else:

            self.runtimeDependencies["libs/qt5/qtwebengine"]            = None

        self.runtimeDependencies["kde/frameworks/tier1/breeze-icons"]   = None
        self.runtimeDependencies["kde/frameworks/tier1/kconfig"]        = None
        self.runtimeDependencies["kde/frameworks/tier1/ki18n"]          = None
        self.runtimeDependencies["kde/frameworks/tier3/kxmlgui"]        = None
        self.runtimeDependencies["kde/frameworks/tier1/kwindowsystem"]  = None
        self.runtimeDependencies["kde/frameworks/tier3/kservice"]       = None
        self.runtimeDependencies["kde/frameworks/tier1/solid"]          = None
        self.runtimeDependencies["kde/frameworks/tier1/kcoreaddons"]    = None
        self.runtimeDependencies["kde/frameworks/tier3/knotifyconfig"]  = None
        self.runtimeDependencies["kde/frameworks/tier3/knotifications"] = None
        self.runtimeDependencies["kde/frameworks/tier3/kiconthemes"]    = None

        # To sync digiKam database with Baloo Plasma desktop search engine (Linux only).

        self.runtimeDependencies["kde/frameworks/tier2/kfilemetadata"]  = None

        # For Panorama export tool.

        self.runtimeDependencies["kde/frameworks/tier1/threadweaver"]   = None

        # For Calendar export plugin.

        self.runtimeDependencies["kde/frameworks/tier1/kcalendarcore"]  = None

        # For some digiKam plugins used to export on web services.

        self.runtimeDependencies['kde/frameworks/tier3/kio']            = None

        # To support more formats in digiKam Qt plugin image loaders.

        self.runtimeDependencies["kde/frameworks/tier1/kimageformats"]  = None

        # Required even if option is disabled in digiKam at compilation stage.

        self.runtimeDependencies["kde/pim/akonadi-contacts"]            = None

        # Install libmarble, plugins and data for geolocation.
        # Marble application will be removed at packaging stage.

        self.runtimeDependencies["kde/applications/marble"]             = None

from Package.CMakePackageBase import *

class Package(CMakePackageBase):
    def __init__(self):
        CMakePackageBase.__init__(self)

        if CraftCore.compiler.isMSVC():
            self.subinfo.options.configure.args  =  " -DENABLE_KFILEMETADATASUPPORT=OFF"
            self.subinfo.options.configure.args += f" -DENABLE_AKONADICONTACTSUPPORT=OFF"
            self.subinfo.options.configure.args += f" -DENABLE_MEDIAPLAYER=ON"
            self.subinfo.options.configure.args += f" -DENABLE_DBUS=OFF"
            self.subinfo.options.configure.args += f" -DENABLE_QWEBENGINE=ON"
            self.subinfo.options.configure.args += f" -DENABLE_MYSQLSUPPORT=OFF"
            self.subinfo.options.configure.args += f" -DENABLE_INTERNALMYSQL=OFF"
            self.subinfo.options.configure.args += f" -DENABLE_DIGIKAM_MODELTEST=OFF"
            self.subinfo.options.configure.args += f" -DENABLE_DRMINGW=OFF"
            self.subinfo.options.configure.args += f" -DENABLE_MINGW_HARDENING_LINKER=OFF"
            self.subinfo.options.configure.args += f" -DBUILD_TESTING=OFF"
            self.subinfo.options.configure.args += f" -DDIGIKAMSC_CHECKOUT_PO=ON"
            self.subinfo.options.configure.args += f" -DDIGIKAMSC_CHECKOUT_DOC=OFF"
            self.subinfo.options.configure.args += f" -DDIGIKAMSC_COMPILE_PO=ON"
            self.subinfo.options.configure.args += f" -DDIGIKAMSC_COMPILE_DOC=OFF"
            self.subinfo.options.configure.args += f" -DDIGIKAMSC_COMPILE_DIGIKAM=ON"

        if CraftCore.compiler.isMinGW():
            self.subinfo.options.configure.args  =  " -DENABLE_KFILEMETADATASUPPORT=OFF"
            self.subinfo.options.configure.args += f" -DENABLE_AKONADICONTACTSUPPORT=OFF"
            self.subinfo.options.configure.args += f" -DENABLE_MEDIAPLAYER=ON"
            self.subinfo.options.configure.args += f" -DENABLE_DBUS=OFF"
            self.subinfo.options.configure.args += f" -DENABLE_QWEBENGINE=OFF"
            self.subinfo.options.configure.args += f" -DENABLE_MYSQLSUPPORT=OFF"
            self.subinfo.options.configure.args += f" -DENABLE_INTERNALMYSQL=OFF"
            self.subinfo.options.configure.args += f" -DENABLE_DIGIKAM_MODELTEST=OFF"
            self.subinfo.options.configure.args += f" -DENABLE_DRMINGW=ON"
            self.subinfo.options.configure.args += f" -DENABLE_MINGW_HARDENING_LINKER=ON"
            self.subinfo.options.configure.args += f" -DBUILD_TESTING=OFF"
            self.subinfo.options.configure.args += f" -DDIGIKAMSC_CHECKOUT_PO=ON"
            self.subinfo.options.configure.args += f" -DDIGIKAMSC_CHECKOUT_DOC=OFF"
            self.subinfo.options.configure.args += f" -DDIGIKAMSC_COMPILE_PO=ON"
            self.subinfo.options.configure.args += f" -DDIGIKAMSC_COMPILE_DOC=OFF"
            self.subinfo.options.configure.args += f" -DDIGIKAMSC_COMPILE_DIGIKAM=ON"

        if CraftCore.compiler.isMacOS:
            self.subinfo.options.configure.args  =  " -DENABLE_KFILEMETADATASUPPORT=OFF"
            self.subinfo.options.configure.args += f" -DENABLE_AKONADICONTACTSUPPORT=OFF"
            self.subinfo.options.configure.args += f" -DENABLE_MEDIAPLAYER=ON"
            self.subinfo.options.configure.args += f" -DENABLE_DBUS=OFF"
            self.subinfo.options.configure.args += f" -DENABLE_QWEBENGINE=ON"
            self.subinfo.options.configure.args += f" -DENABLE_MYSQLSUPPORT=OFF"
            self.subinfo.options.configure.args += f" -DENABLE_INTERNALMYSQL=OFF"
            self.subinfo.options.configure.args += f" -DENABLE_DIGIKAM_MODELTEST=OFF"
            self.subinfo.options.configure.args += f" -DENABLE_DRMINGW=OFF"
            self.subinfo.options.configure.args += f" -DENABLE_MINGW_HARDENING_LINKER=OFF"
            self.subinfo.options.configure.args += f" -DBUILD_TESTING=OFF"
            self.subinfo.options.configure.args += f" -DDIGIKAMSC_CHECKOUT_PO=ON"
            self.subinfo.options.configure.args += f" -DDIGIKAMSC_CHECKOUT_DOC=OFF"
            self.subinfo.options.configure.args += f" -DDIGIKAMSC_COMPILE_PO=ON"
            self.subinfo.options.configure.args += f" -DDIGIKAMSC_COMPILE_DOC=OFF"
            self.subinfo.options.configure.args += f" -DDIGIKAMSC_COMPILE_DIGIKAM=ON"

    def createPackage(self):
        self.defines["productname"] = "digiKam"
        self.defines["website"]     = "https://www.digikam.org"
        self.defines["company"]     = "digiKam.org"
        self.defines["license"]     = os.path.join(self.sourceDir(), "COPYING")

        # Windows-only, mac is handled implicitly

        self.defines["executable"]  = "bin\\digikam.exe"

        # Windows-only (order is important)

        self.defines["icon"]        = os.path.join(self.packageDir(), "avplayer.ico")
        self.defines["icon"]        = os.path.join(self.packageDir(), "showfoto.ico")
        self.defines["icon"]        = os.path.join(self.packageDir(), "digikam.ico")

        # Windows-only

        self.defines["shortcuts"]   = [ {
                                            "name"        : "digiKam",
                                            "target"      : "bin/digikam.exe",
                                            "description" : self.subinfo.description,
                                            "icon"        : "$INSTDIR\\digikam.ico"
                                        },
                                        {
                                            "name"        : "Showfoto",
                                            "target"      : "bin/showfoto.exe",
                                            "description" : "digiKam stand alone Image Editor",
                                            "icon"        : "$INSTDIR\\showfoto.ico"
                                        },
                                        {
                                            "name"        : "AVPlayer",
                                            "target"      : "bin/avplayer.exe",
                                            "description" : "digiKam stand alone Media Player",
                                            "icon"        : "$INSTDIR\\avplayer.ico"
                                        }
                                      ]

        self.blacklist_file.append(os.path.join(self.packageDir(), 'blacklist.txt'))
        if CraftCore.compiler.isMacOS:
            self.blacklist_file.append(os.path.join(self.packageDir(), 'blacklist_mac.txt'))

        self.ignoredPackages.append("binary/mysql")

        return TypePackager.createPackage(self)

    def preArchive(self):
        if CraftCore.compiler.isMSVC():

            # Manage files under Windows bundle:

            # remove setup_vars_opencv4.cmd               (blacklist.txt)
            # remove Marble LICENSE                       (blacklist.txt)

            # See bug #455232:
            # - move astro.dll to digiKam/bin/
            # - move marbledeclarative.dll to digiKam/bin/
            # - move marblewidget-qt5.dll to digiKam/bin/
            # - move data/ to digiKam/data
            # - remove marble-qt.exe                      (blacklist.txt)

            archiveDir = self.archiveDir()
            binPath    = os.path.join(archiveDir,    "bin")

            if not utils.moveFile(os.path.join(archiveDir,  "astro.dll"),
                                  os.path.join(binPath,     "astro.dll")):
                print("Could not move astro.dll file")

            if not utils.moveFile(os.path.join(archiveDir,  "marbledeclarative.dll"),
                                  os.path.join(binPath,     "marbledeclarative.dll")):
                print("Could not move marbledeclarative.dll file")

            if not utils.moveFile(os.path.join(archiveDir,  "marblewidget-qt5.dll"),
                                  os.path.join(binPath,     "marblewidget-qt5.dll")):
                print("Could not move marblewidget-qt5.dll file")

            if not utils.mergeTree(os.path.join(archiveDir, "data"),
                                   os.path.join(binPath,    "data")):
                print("Could not move Marble data dir")

            # Move translations/ to bin/translations/

            if not utils.moveFile(os.path.join(archiveDir,  "translations"),
                                  os.path.join(binPath,     "translations")):
                print("Could not move Qt translations dir")

            # Move digiKam plugins from bin/digikam/ to bin/plugins/digikam/

            pluginsPath = os.path.join(archiveDir,   "bin", "plugins")
            utils.createDir(pluginsPath)

            if not utils.moveFile(os.path.join(archiveDir,  "bin", "digikam"),
                                  os.path.join(pluginsPath, "digikam")):
                print("Could not move digiKam plugins dir")

            # Move bin/*marble_plugins*.dll to bin/plugins/

            pluginsLst = [
                "AnnotatePlugin.dll",
                "AprsPlugin.dll",
                "AtmospherePlugin.dll",
                "CachePlugin.dll",
                "CompassFloatItem.dll",
                "CrosshairsPlugin.dll",
                "CycleStreetsPlugin.dll",
                "EarthquakePlugin.dll",
                "EclipsesPlugin.dll",
                "ElevationProfileFloatItem.dll",
                "ElevationProfileMarker.dll",
                "FlightGearPositionProviderPlugin.dll",
                "FoursquarePlugin.dll",
                "GeoUriPlugin.dll",
                "GosmoreReverseGeocodingPlugin.dll",
                "GosmoreRoutingPlugin.dll",
                "GpsbabelPlugin.dll",
                "GpsInfo.dll",
                "GpxPlugin.dll",
                "GraticulePlugin.dll",
                "HostipPlugin.dll",
                "JsonPlugin.dll",
                "KmlPlugin.dll",
                "LatLonPlugin.dll",
                "License.dll",
                "LocalDatabasePlugin.dll",
                "LocalOsmSearchPlugin.dll",
                "MapQuestPlugin.dll",
                "MapScaleFloatItem.dll",
                "MeasureTool.dll",
                "MonavPlugin.dll",
                "NavigationFloatItem.dll",
                "NominatimReverseGeocodingPlugin.dll",
                "NominatimSearchPlugin.dll",
                "NotesPlugin.dll",
                "OpenLocationCodeSearchPlugin.dll",
                "OpenRouteServicePlugin.dll",
                "OsmPlugin.dll",
                "OSRMPlugin.dll",
                "OverviewMap.dll",
                "Pn2Plugin.dll",
                "PntPlugin.dll",
                "PositionMarker.dll",
                "PostalCode.dll",
                "ProgressFloatItem.dll",
                "ProgressFloatItem.dll",
                "RoutingPlugin.dll",
                "RoutinoPlugin.dll",
                "SatellitesPlugin.dll",
                "Speedometer.dll",
                "StarsPlugin.dll",
                "SunPlugin.dll",
                "YoursPlugin.dll",
            ]

            for dll in pluginsLst:
                if not utils.moveFile(os.path.join(binPath,     dll),
                                      os.path.join(pluginsPath, dll)):
                    print("Could not move Marble plugin " + dll)

            # Download exiftool.exe in the bundle

            url     = 'https://exiftool.org/exiftool-12.42.zip'
            archive = requests.get(url)
            open(os.path.join(binPath, "exiftool.zip"), 'wb').write(archive.content)
            with zipfile.ZipFile(os.path.join(binPath, "exiftool.zip"), "r") as zip_ref:
                zip_ref.extractall(binPath)
            utils.moveFile(os.path.join(binPath, "exiftool(-k).exe"),
                           os.path.join(binPath, "exiftool.exe"))
            utils.deleteFile(os.path.join(binPath, "exiftool.zip"))


        return True
