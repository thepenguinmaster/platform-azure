# WizIO 2019 Georgi Angelov
#   http://www.wizio.eu/
#   https://github.com/Wiz-IO/platform-azure

from os.path import join
from common import *
from SCons.Script import Builder

def dev_init(env, platform):
    dev_create_template(env, [ "app_manifest.json" ])
    dev_initialize(env, False)     
    env.Append(
        CPPDEFINES = [ "_POSIX_C_SOURCE", "{}=200".format(platform.upper()) ],        
        CPPPATH = [ 
            join(env.framework_dir,  platform, platform),
            join(env.framework_dir,  platform, "core"),
            join(env.framework_dir,  platform, "variants", env.BoardConfig().get("build.variant")),            
            join(env.sysroot_dir, "usr", "include"),   
            join("$PROJECT_DIR", "src"),     
            join("$PROJECT_DIR", "lib"),
            join("$PROJECT_DIR", "include")         
        ],        
        CFLAGS = [ 
            "-O0",
            "-std=c11", 
            "--sysroot=" + env.sysroot_dir,
            "-fno-omit-frame-pointer", 
            "-fno-strict-aliasing",  
            "-Wall",    
            "-fno-exceptions",                                                
        ],  
        CXXFLAGS = [    
            "-O0",                            
            "-fno-rtti",
            "-fno-exceptions", 
            "-fno-non-call-exceptions",
            "-fno-use-cxa-atexit",
            "-fno-threadsafe-statics",
        ],  
        CCFLAGS = [ env.cortex ],                     
        LINKFLAGS = [ 
            env.cortex,  
            "--sysroot=" + env.sysroot_dir,
            "-B", env.toolchain_dir,
            "-nodefaultlibs",
            "-Wl,--no-undefined", 
        ], 
        LIBSOURCE_DIRS = [ join(env.framework_dir, platform, "libraries"), ], 
        LIBPATH = [ join("$PROJECT_DIR", "lib") ], # -L
        LIBS = [ "c", "gcc_s", "applibs", "azureiot", "curl" ],               
        BUILDERS = dict( PackImage = Builder( 
                action = env.VerboseAction(dev_image_pack, " "),
                suffix = ".bin"
            )  
        ), 
        UPLOADCMD = dev_image_upload
    )
    dev_experimental_mode(env)
    libs = []   
    #ARDUINO  
    libs.append(
        env.BuildLibrary(
            join("$BUILD_DIR", "_" + platform),
            join(env.framework_dir, platform, platform),
    ))     
    libs.append(
        env.BuildLibrary(
            join("$BUILD_DIR", "_core"),
            join(env.framework_dir, platform, "core"),
    ))    
    libs.append(
        env.BuildLibrary(
            join("$BUILD_DIR", "_variant"),
            join(env.framework_dir, platform, "variants", env.BoardConfig().get("build.variant")),
    ))  
    #USER     
    libs.append(
        env.BuildLibrary(
            join("$BUILD_DIR", "_custom"),
            join("$PROJECT_DIR", "lib"),
    ))         
    env.Append(LIBS = libs)




    
