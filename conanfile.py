from conans import ConanFile, CMake, tools
import os


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
    build_policy = "missing"

    def source(self):
        git = tools.Git(folder="simple-binary-encoding")
        git.clone("https://github.com/real-logic/simple-binary-encoding.git", SbeConan.version)

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="simple-binary-encoding")
        cmake.build()

    def package(self):
        self.copy("*.h", src=os.path.join("simple-binary-encoding","sbe-tool","src","main","cpp","otf"), dst="include/otf")
        self.copy("*.jar", src=os.path.join("simple-binary-encoding","sbe-all","build","libs"), dst="bin")

    def package_info(self):
        bin_path = os.path.join(self.package_folder, "bin")
        self.output.info("Appending PATH environment variable: %s" % bin_path)
        self.env_info.PATH.append(bin_path)

        self.user_info.sbe_jar = os.path.join(self.package_folder, "bin", "sbe-all-1.26.0.jar").replace("\\","/")

