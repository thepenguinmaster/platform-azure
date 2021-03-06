[06.12.2019]
* Fix Mediatek SDK - printf()
* Add M4F FreeRTOS - last version
* [Example M4F MTK_FreeRTOS](https://github.com/Wiz-IO/platform-azure/tree/master/Examples/MTK_FreeRTOS)

[02.12.2019]
* Add new framework for M4: [mediatek](https://github.com/MediaTek-Labs/mt3620_m4_software)

[14.10.2019]
* Fix all builders
* Add Sysroot 3+Beta1909
* azspere form SDK 3
* Support installed Microsoft SDK

[10.10.2019]
* Workaround beta upload (fixed in 2.x.x)

[04.10.2019]
* Python 2/3 fix print()
* Wiring baremetal add all gpio blocks

[26.09.2019]
* Add Linux [Experimental mode](https://github.com/Wiz-IO/platform-azure/wiki/Arduino-INI-file#experimental-mode) for libc and libwolfssl
* Add search path for user project/lib so
* Add some examples
* Fix Arduino waitWifi()
* Default delete all applications

[20.09.2019]
* Add Arduino [Experimental mode](https://github.com/Wiz-IO/platform-azure/wiki/Arduino-INI-file#experimental-mode) for libc and libwolfssl
* Add Arduino lib ClientSecure ( need Experimental mode )

[10.09.2019]
* Serial.redirect(stderr); // LogDebug() can be used

[05.09.2019]
* Fix copy-packed images
* Fix C++ includes ( Junxiao Shi )

[02.09.2019]
* Add Arduino get utc()
* Add Library Generate SAS token
* Fix millis() zero from beginning

[31.08.2019]
* Fix times ( Junxiao Shi )
* Fix Wire ( Junxiao Shi )

[28.08.2019]
* Serial.available()
* Client.available()

[26.08.2019]
* ComponentID (GUID) once
* platformio.ini - delete current or all applications
* Try use installed SDK if exist

[22.08.2019]
* [Image packer](https://github.com/Wiz-IO/platform-azure/blob/07d94266b7e44426c8f37778d8c5164b10d92449/builder/frameworks/common.py#L56) must be work fine
* [Arduino Serial and Serial1](https://github.com/Wiz-IO/framework-azure/blob/783b1effeee9e36aececdbb03b1dfdd376c816be/arduino/core/HardwareSerial.cpp#L55) - receive - there is not allowed ioctl() for Serial.Available() and .peek ... I did "fake" ringbuffer
* I found way to use installed Microsoft SDK (for those who have it) - [will update soon](https://github.com/Wiz-IO/platform-azure/blob/b2222658ca657c9c70001924e720417a64a719f0/builder/frameworks/common.py#L126)
