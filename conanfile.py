from conan import ConanFile
from conan.tools.cmake import CMakeDeps, CMakeToolchain

class LightMaker(ConanFile):
    settings = "os", "build_type"

    def requirements(self):
        self.requires("ada/2.9.1")
        self.requires("boost/1.83.0")
        self.requires("protobuf/3.21.12")
        self.requires("ffmpeg/6.1.1")
        self.requires("mozjpeg/4.1.5")
        self.requires("openal/1.21.1")
        self.requires("sqlite3/3.43.0")
        self.requires("gtest/1.15.0")
        self.requires("zlib/1.3.1")
        self.requires("openssl/3.3.1")
        self.requires("openh264/2.4.1")
        self.requires("libvpx/1.14.1")
        self.requires("opus/1.3.1")

    def generate(self):
        tc = CMakeToolchain(self)
        tc.user_presets_path = False
        tc.generate()
        cd = CMakeDeps(self)
        cd.generate()