from conans import ConanFile, CMake, tools


class SbeConan(ConanFile):
    name = "sbe"
    version = "1.26.0"
    license = "Apache License, Version 2.0"
    url = "https://github.com/real-logic/simple-binary-encoding"
    description = "Simple Binary Encoding (SBE) - High Performance Message Codec"
    topics = ("codec", "java", "c-plus-plus", "encoder-decoder")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"

    def source(self):
        git = tools.Git(folder="simple-binary-encoding")
        git.clone("https://github.com/real-logic/simple-binary-encoding.git", SbeConan.version)

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="simple-binary-encoding")
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include/otf", src="simple-binary-encoding/sbe-tool/src/main/cpp/otf")
        self.copy("*.jar", dst="bin", src="simple-binary-encoding/sbe-all/build", keep_path=False)
