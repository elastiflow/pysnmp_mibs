# SNMP MIB module (NDS-DTH3-SYSTEM) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/news_digital_1855/NDS-DTH3-SYSTEM.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 11:44:39 2025
# On host e-ws1-mac.muc.elastiflow.net platform Darwin version 24.3.0 by user rob
# Using Python version 3.13.3 (main, Apr  8 2025, 13:54:08) [Clang 16.0.0 (clang-1600.0.26.6)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ndsDTH3Encoder = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1855, 1, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SystemEnc_ObjectIdentity = ObjectIdentity
systemEnc = _SystemEnc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1)
)


class _SystemSerialNumber_Type(Integer32):
    """Custom type systemSerialNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SystemSerialNumber_Type.__name__ = "Integer32"
_SystemSerialNumber_Object = MibScalar
systemSerialNumber = _SystemSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 1),
    _SystemSerialNumber_Type()
)
systemSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSerialNumber.setStatus("current")


class _SystemHardwareRelease_Type(DisplayString):
    """Custom type systemHardwareRelease based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_SystemHardwareRelease_Type.__name__ = "DisplayString"
_SystemHardwareRelease_Object = MibScalar
systemHardwareRelease = _SystemHardwareRelease_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 2),
    _SystemHardwareRelease_Type()
)
systemHardwareRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemHardwareRelease.setStatus("current")


class _SystemSoftwareRelease_Type(DisplayString):
    """Custom type systemSoftwareRelease based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_SystemSoftwareRelease_Type.__name__ = "DisplayString"
_SystemSoftwareRelease_Object = MibScalar
systemSoftwareRelease = _SystemSoftwareRelease_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 3),
    _SystemSoftwareRelease_Type()
)
systemSoftwareRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSoftwareRelease.setStatus("current")


class _SystemFirmwareRelease_Type(DisplayString):
    """Custom type systemFirmwareRelease based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_SystemFirmwareRelease_Type.__name__ = "DisplayString"
_SystemFirmwareRelease_Object = MibScalar
systemFirmwareRelease = _SystemFirmwareRelease_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 4),
    _SystemFirmwareRelease_Type()
)
systemFirmwareRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemFirmwareRelease.setStatus("current")


class _SystemBuildStandard_Type(DisplayString):
    """Custom type systemBuildStandard based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_SystemBuildStandard_Type.__name__ = "DisplayString"
_SystemBuildStandard_Object = MibScalar
systemBuildStandard = _SystemBuildStandard_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 5),
    _SystemBuildStandard_Type()
)
systemBuildStandard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemBuildStandard.setStatus("current")
_SystemTimeDate_Type = DateAndTime
_SystemTimeDate_Object = MibScalar
systemTimeDate = _SystemTimeDate_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 6),
    _SystemTimeDate_Type()
)
systemTimeDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemTimeDate.setStatus("current")
_SystemnextTimeDate_Type = DateAndTime
_SystemnextTimeDate_Object = MibScalar
systemnextTimeDate = _SystemnextTimeDate_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 7),
    _SystemnextTimeDate_Type()
)
systemnextTimeDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemnextTimeDate.setStatus("current")


class _SystemTimeSwitch_Type(Integer32):
    """Custom type systemTimeSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("timeDate", 0),
          ("timeCode", 1))
    )


_SystemTimeSwitch_Type.__name__ = "Integer32"
_SystemTimeSwitch_Object = MibScalar
systemTimeSwitch = _SystemTimeSwitch_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 8),
    _SystemTimeSwitch_Type()
)
systemTimeSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemTimeSwitch.setStatus("current")


class _SystemServiceLevel_Type(Integer32):
    """Custom type systemServiceLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("onLine", 0),
          ("reserve", 1),
          ("outofService", 2))
    )


_SystemServiceLevel_Type.__name__ = "Integer32"
_SystemServiceLevel_Object = MibScalar
systemServiceLevel = _SystemServiceLevel_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 9),
    _SystemServiceLevel_Type()
)
systemServiceLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemServiceLevel.setStatus("current")
_ModuleTable_Object = MibTable
moduleTable = _ModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 10)
)
if mibBuilder.loadTexts:
    moduleTable.setStatus("current")
_ModuleEntry_Object = MibTableRow
moduleEntry = _ModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 10, 1)
)
moduleEntry.setIndexNames(
    (0, "NDS-DTH3-SYSTEM", "moduleIndex"),
)
if mibBuilder.loadTexts:
    moduleEntry.setStatus("current")


class _ModuleIndex_Type(Integer32):
    """Custom type moduleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("optionModule1", 1),
          ("optionModule2", 2),
          ("optionModule3", 3),
          ("optionModule4", 4),
          ("optionModule5", 5),
          ("optionModule6", 6),
          ("bissOptionCard", 7))
    )


_ModuleIndex_Type.__name__ = "Integer32"
_ModuleIndex_Object = MibTableColumn
moduleIndex = _ModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 10, 1, 1),
    _ModuleIndex_Type()
)
moduleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleIndex.setStatus("current")


class _ModuleType_Type(Integer32):
    """Custom type moduleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("notdefined", 0),
          ("version1", 1),
          ("version2", 2),
          ("version3", 3),
          ("version4", 4),
          ("version5", 5),
          ("version6", 6),
          ("version7", 7),
          ("version8", 8),
          ("version9", 9),
          ("version10", 10))
    )


_ModuleType_Type.__name__ = "Integer32"
_ModuleType_Object = MibTableColumn
moduleType = _ModuleType_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 10, 1, 2),
    _ModuleType_Type()
)
moduleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleType.setStatus("current")


class _ModuleId_Type(Integer32):
    """Custom type moduleId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3,
              4,
              5,
              6,
              7,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              33,
              34,
              37,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("videoE4", 2),
          ("videoHybrid", 3),
          ("videoHD", 4),
          ("video-audio-SD-ICE", 5),
          ("videoPreProcessor", 6),
          ("video-audio-HD-ICE", 7),
          ("audioMPEG2Musicam", 16),
          ("audioDolbyDigitalAC-3", 17),
          ("audioDolbySurround", 18),
          ("audio-AC-3-Pass-Thru", 19),
          ("audioLinearPCM-DolbyE", 20),
          ("audioTBD21", 21),
          ("audioTBD22", 22),
          ("audioTBD23", 23),
          ("audioTBD24", 24),
          ("audioTBD25", 25),
          ("audioS13167-24dB", 26),
          ("audioTBD27", 27),
          ("audioTBD28", 28),
          ("audioTBD29", 29),
          ("audioS11976-18dB", 30),
          ("audioS8482", 31),
          ("analogueVideoInput", 33),
          ("dataModule", 34),
          ("internalQPSKModulator", 37),
          ("iRD", 39),
          ("rAS1", 40),
          ("bISS", 41),
          ("oFDM-Modulator-Voyager", 42),
          ("aTM", 43),
          ("remux", 44),
          ("sSIandASIOutput", 45),
          ("dVCPro", 46),
          ("dataPreEncodedRS422", 47),
          ("satMod3", 48),
          ("oFDM-IFCard-DENG", 49),
          ("oFDM-Modulator-DENG", 50),
          ("audioXLR", 51),
          ("satMod3-IFCard", 52),
          ("oFDM-UpConverter", 53),
          ("dataRS422", 54),
          ("dataRS232", 55),
          ("iPStreamer", 56),
          ("decoderWithDemodulator", 57),
          ("demodulator", 58),
          ("combinedOFDMandIF", 59),
          ("g703", 60),
          ("vocality", 61),
          ("netCueAudioSwitch", 62),
          ("opticalASI", 63))
    )


_ModuleId_Type.__name__ = "Integer32"
_ModuleId_Object = MibTableColumn
moduleId = _ModuleId_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 10, 1, 3),
    _ModuleId_Type()
)
moduleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleId.setStatus("current")
_SystemTable_Object = MibTable
systemTable = _SystemTable_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 11)
)
if mibBuilder.loadTexts:
    systemTable.setStatus("current")
_SystemEntry_Object = MibTableRow
systemEntry = _SystemEntry_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 11, 1)
)
systemEntry.setIndexNames(
    (0, "NDS-DTH3-SYSTEM", "systemCurrentNextIndex"),
)
if mibBuilder.loadTexts:
    systemEntry.setStatus("current")


class _SystemCurrentNextIndex_Type(Integer32):
    """Custom type systemCurrentNextIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("index-current", 1),
          ("index-next", 2))
    )


_SystemCurrentNextIndex_Type.__name__ = "Integer32"
_SystemCurrentNextIndex_Object = MibTableColumn
systemCurrentNextIndex = _SystemCurrentNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 11, 1, 1),
    _SystemCurrentNextIndex_Type()
)
systemCurrentNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemCurrentNextIndex.setStatus("current")


class _SystemSplicing_Type(Integer32):
    """Custom type systemSplicing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_SystemSplicing_Type.__name__ = "Integer32"
_SystemSplicing_Object = MibTableColumn
systemSplicing = _SystemSplicing_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 11, 1, 2),
    _SystemSplicing_Type()
)
systemSplicing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemSplicing.setStatus("current")


class _SystemClockSource_Type(Integer32):
    """Custom type systemClockSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 0),
          ("video", 1),
          ("hsync", 2))
    )


_SystemClockSource_Type.__name__ = "Integer32"
_SystemClockSource_Object = MibTableColumn
systemClockSource = _SystemClockSource_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 11, 1, 3),
    _SystemClockSource_Type()
)
systemClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemClockSource.setStatus("current")


class _SystemNetworkName_Type(DisplayString):
    """Custom type systemNetworkName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_SystemNetworkName_Type.__name__ = "DisplayString"
_SystemNetworkName_Object = MibTableColumn
systemNetworkName = _SystemNetworkName_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 11, 1, 4),
    _SystemNetworkName_Type()
)
systemNetworkName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemNetworkName.setStatus("current")


class _SystemServiceName_Type(DisplayString):
    """Custom type systemServiceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_SystemServiceName_Type.__name__ = "DisplayString"
_SystemServiceName_Object = MibTableColumn
systemServiceName = _SystemServiceName_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 11, 1, 5),
    _SystemServiceName_Type()
)
systemServiceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemServiceName.setStatus("current")


class _SystemNetworkID_Type(Integer32):
    """Custom type systemNetworkID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SystemNetworkID_Type.__name__ = "Integer32"
_SystemNetworkID_Object = MibTableColumn
systemNetworkID = _SystemNetworkID_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 11, 1, 6),
    _SystemNetworkID_Type()
)
systemNetworkID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemNetworkID.setStatus("current")


class _SystemServiceID_Type(Integer32):
    """Custom type systemServiceID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SystemServiceID_Type.__name__ = "Integer32"
_SystemServiceID_Object = MibTableColumn
systemServiceID = _SystemServiceID_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 11, 1, 7),
    _SystemServiceID_Type()
)
systemServiceID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemServiceID.setStatus("current")


class _SystemTSID_Type(Integer32):
    """Custom type systemTSID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SystemTSID_Type.__name__ = "Integer32"
_SystemTSID_Object = MibTableColumn
systemTSID = _SystemTSID_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 11, 1, 8),
    _SystemTSID_Type()
)
systemTSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemTSID.setStatus("current")


class _SystemSIInformation_Type(Integer32):
    """Custom type systemSIInformation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1),
          ("onNoEIT", 2),
          ("onPAT-PMT-CAT-only", 3),
          ("onPAT-PMT-only", 4),
          ("onPSIP", 5),
          ("onExtPSIP", 6),
          ("onExtPSIPPSI", 7))
    )


_SystemSIInformation_Type.__name__ = "Integer32"
_SystemSIInformation_Object = MibTableColumn
systemSIInformation = _SystemSIInformation_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 11, 1, 9),
    _SystemSIInformation_Type()
)
systemSIInformation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemSIInformation.setStatus("current")
_SystemDONOTUSEReflexIPAddress_Type = IpAddress
_SystemDONOTUSEReflexIPAddress_Object = MibTableColumn
systemDONOTUSEReflexIPAddress = _SystemDONOTUSEReflexIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 11, 1, 10),
    _SystemDONOTUSEReflexIPAddress_Type()
)
systemDONOTUSEReflexIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemDONOTUSEReflexIPAddress.setStatus("current")


class _SystemDONOTUSEReflexUDPPort_Type(Integer32):
    """Custom type systemDONOTUSEReflexUDPPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SystemDONOTUSEReflexUDPPort_Type.__name__ = "Integer32"
_SystemDONOTUSEReflexUDPPort_Object = MibTableColumn
systemDONOTUSEReflexUDPPort = _SystemDONOTUSEReflexUDPPort_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 11, 1, 11),
    _SystemDONOTUSEReflexUDPPort_Type()
)
systemDONOTUSEReflexUDPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemDONOTUSEReflexUDPPort.setStatus("current")


class _SystemEncoderNumber_Type(Integer32):
    """Custom type systemEncoderNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SystemEncoderNumber_Type.__name__ = "Integer32"
_SystemEncoderNumber_Object = MibTableColumn
systemEncoderNumber = _SystemEncoderNumber_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 11, 1, 12),
    _SystemEncoderNumber_Type()
)
systemEncoderNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemEncoderNumber.setStatus("current")


class _SystemLCDMode_Type(Integer32):
    """Custom type systemLCDMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("encoderControl", 0),
          ("textRemote", 1),
          ("textRemoteClearScreen", 2),
          ("graphicsRemote", 3),
          ("graphicsRemoteClearScreen", 4))
    )


_SystemLCDMode_Type.__name__ = "Integer32"
_SystemLCDMode_Object = MibTableColumn
systemLCDMode = _SystemLCDMode_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 11, 1, 13),
    _SystemLCDMode_Type()
)
systemLCDMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemLCDMode.setStatus("current")


class _SystemFailRelay_Type(Integer32):
    """Custom type systemFailRelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("encoderControl", 0),
          ("offRemote", 1),
          ("onRemote", 2))
    )


_SystemFailRelay_Type.__name__ = "Integer32"
_SystemFailRelay_Object = MibTableColumn
systemFailRelay = _SystemFailRelay_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 11, 1, 14),
    _SystemFailRelay_Type()
)
systemFailRelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemFailRelay.setStatus("current")


class _SystemAlarmRelay_Type(Integer32):
    """Custom type systemAlarmRelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("encoderControl", 0),
          ("offRemote", 1),
          ("onRemote", 2))
    )


_SystemAlarmRelay_Type.__name__ = "Integer32"
_SystemAlarmRelay_Object = MibTableColumn
systemAlarmRelay = _SystemAlarmRelay_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 11, 1, 15),
    _SystemAlarmRelay_Type()
)
systemAlarmRelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemAlarmRelay.setStatus("current")


class _SystemPMTPID_Type(Integer32):
    """Custom type systemPMTPID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8190),
    )


_SystemPMTPID_Type.__name__ = "Integer32"
_SystemPMTPID_Object = MibTableColumn
systemPMTPID = _SystemPMTPID_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 11, 1, 16),
    _SystemPMTPID_Type()
)
systemPMTPID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemPMTPID.setStatus("current")


class _SystemServiceProvider_Type(DisplayString):
    """Custom type systemServiceProvider based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_SystemServiceProvider_Type.__name__ = "DisplayString"
_SystemServiceProvider_Object = MibTableColumn
systemServiceProvider = _SystemServiceProvider_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 11, 1, 17),
    _SystemServiceProvider_Type()
)
systemServiceProvider.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemServiceProvider.setStatus("current")


class _SystemAC3AudioDescriptor_Type(Integer32):
    """Custom type systemAC3AudioDescriptor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("atsc-and-dvb", 0),
          ("dvb-only", 1),
          ("atsc-only", 2))
    )


_SystemAC3AudioDescriptor_Type.__name__ = "Integer32"
_SystemAC3AudioDescriptor_Object = MibTableColumn
systemAC3AudioDescriptor = _SystemAC3AudioDescriptor_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 11, 1, 18),
    _SystemAC3AudioDescriptor_Type()
)
systemAC3AudioDescriptor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemAC3AudioDescriptor.setStatus("current")


class _SystemDVBServiceType_Type(Integer32):
    """Custom type systemDVBServiceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("digital-television-service", 0),
          ("digital-radio-service", 1),
          ("teletext-service", 2),
          ("data-broadcast-service", 3))
    )


_SystemDVBServiceType_Type.__name__ = "Integer32"
_SystemDVBServiceType_Object = MibTableColumn
systemDVBServiceType = _SystemDVBServiceType_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 11, 1, 19),
    _SystemDVBServiceType_Type()
)
systemDVBServiceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemDVBServiceType.setStatus("current")


class _SystemATSCServiceType_Type(Integer32):
    """Custom type systemATSCServiceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("analog-television", 0),
          ("atsc-digital-television", 1),
          ("atsc-audio-only", 2),
          ("atsc-data-broadcast-service", 3))
    )


_SystemATSCServiceType_Type.__name__ = "Integer32"
_SystemATSCServiceType_Object = MibTableColumn
systemATSCServiceType = _SystemATSCServiceType_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 11, 1, 20),
    _SystemATSCServiceType_Type()
)
systemATSCServiceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemATSCServiceType.setStatus("current")


class _SystemATSCProgramNumber_Type(Integer32):
    """Custom type systemATSCProgramNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SystemATSCProgramNumber_Type.__name__ = "Integer32"
_SystemATSCProgramNumber_Object = MibTableColumn
systemATSCProgramNumber = _SystemATSCProgramNumber_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 11, 1, 21),
    _SystemATSCProgramNumber_Type()
)
systemATSCProgramNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemATSCProgramNumber.setStatus("current")


class _SystemATSCProgramParadigm_Type(Integer32):
    """Custom type systemATSCProgramParadigm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_SystemATSCProgramParadigm_Type.__name__ = "Integer32"
_SystemATSCProgramParadigm_Object = MibTableColumn
systemATSCProgramParadigm = _SystemATSCProgramParadigm_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 11, 1, 22),
    _SystemATSCProgramParadigm_Type()
)
systemATSCProgramParadigm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemATSCProgramParadigm.setStatus("current")


class _SystemDVBStreamIdentifier_Type(Integer32):
    """Custom type systemDVBStreamIdentifier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_SystemDVBStreamIdentifier_Type.__name__ = "Integer32"
_SystemDVBStreamIdentifier_Object = MibTableColumn
systemDVBStreamIdentifier = _SystemDVBStreamIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 11, 1, 23),
    _SystemDVBStreamIdentifier_Type()
)
systemDVBStreamIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemDVBStreamIdentifier.setStatus("current")


class _SystemPSIPExternalSource_Type(Integer32):
    """Custom type systemPSIPExternalSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("remux-PSIP-Input-1", 1),
          ("remux-PSIP-Input-2", 2),
          ("remux-PSIP-Input-3", 3))
    )


_SystemPSIPExternalSource_Type.__name__ = "Integer32"
_SystemPSIPExternalSource_Object = MibTableColumn
systemPSIPExternalSource = _SystemPSIPExternalSource_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 11, 1, 24),
    _SystemPSIPExternalSource_Type()
)
systemPSIPExternalSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemPSIPExternalSource.setStatus("current")


class _SystemPSIPMinPID_Type(Integer32):
    """Custom type systemPSIPMinPID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8190),
    )


_SystemPSIPMinPID_Type.__name__ = "Integer32"
_SystemPSIPMinPID_Object = MibTableColumn
systemPSIPMinPID = _SystemPSIPMinPID_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 11, 1, 25),
    _SystemPSIPMinPID_Type()
)
systemPSIPMinPID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemPSIPMinPID.setStatus("current")


class _SystemPSIPMaxPID_Type(Integer32):
    """Custom type systemPSIPMaxPID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8190),
    )


_SystemPSIPMaxPID_Type.__name__ = "Integer32"
_SystemPSIPMaxPID_Object = MibTableColumn
systemPSIPMaxPID = _SystemPSIPMaxPID_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 11, 1, 26),
    _SystemPSIPMaxPID_Type()
)
systemPSIPMaxPID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemPSIPMaxPID.setStatus("current")


class _SystemBroadcastFlag_Type(Integer32):
    """Custom type systemBroadcastFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_SystemBroadcastFlag_Type.__name__ = "Integer32"
_SystemBroadcastFlag_Object = MibTableColumn
systemBroadcastFlag = _SystemBroadcastFlag_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 11, 1, 27),
    _SystemBroadcastFlag_Type()
)
systemBroadcastFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemBroadcastFlag.setStatus("current")
_SystemLCDTable_Object = MibTable
systemLCDTable = _SystemLCDTable_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 12)
)
if mibBuilder.loadTexts:
    systemLCDTable.setStatus("current")
_SystemLCDEntry_Object = MibTableRow
systemLCDEntry = _SystemLCDEntry_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 12, 1)
)
systemLCDEntry.setIndexNames(
    (0, "NDS-DTH3-SYSTEM", "systemLCDCurrentNextIndex"),
    (0, "NDS-DTH3-SYSTEM", "systemLCDLine"),
)
if mibBuilder.loadTexts:
    systemLCDEntry.setStatus("current")


class _SystemLCDCurrentNextIndex_Type(Integer32):
    """Custom type systemLCDCurrentNextIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("index-current", 1),
          ("index-next", 2))
    )


_SystemLCDCurrentNextIndex_Type.__name__ = "Integer32"
_SystemLCDCurrentNextIndex_Object = MibTableColumn
systemLCDCurrentNextIndex = _SystemLCDCurrentNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 12, 1, 1),
    _SystemLCDCurrentNextIndex_Type()
)
systemLCDCurrentNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemLCDCurrentNextIndex.setStatus("current")


class _SystemLCDLine_Type(Integer32):
    """Custom type systemLCDLine based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("line1", 1),
          ("line2", 2),
          ("line3", 3),
          ("line4", 4),
          ("line5", 5),
          ("line6", 6),
          ("line7", 7),
          ("line8", 8))
    )


_SystemLCDLine_Type.__name__ = "Integer32"
_SystemLCDLine_Object = MibTableColumn
systemLCDLine = _SystemLCDLine_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 12, 1, 2),
    _SystemLCDLine_Type()
)
systemLCDLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemLCDLine.setStatus("current")


class _SystemLCDText_Type(DisplayString):
    """Custom type systemLCDText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_SystemLCDText_Type.__name__ = "DisplayString"
_SystemLCDText_Object = MibTableColumn
systemLCDText = _SystemLCDText_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 12, 1, 3),
    _SystemLCDText_Type()
)
systemLCDText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemLCDText.setStatus("current")


class _SystemTemperature_Type(Integer32):
    """Custom type systemTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 200),
    )


_SystemTemperature_Type.__name__ = "Integer32"
_SystemTemperature_Object = MibScalar
systemTemperature = _SystemTemperature_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 13),
    _SystemTemperature_Type()
)
systemTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemTemperature.setStatus("current")


class _SystemVoltage_Type(Integer32):
    """Custom type systemVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_SystemVoltage_Type.__name__ = "Integer32"
_SystemVoltage_Object = MibScalar
systemVoltage = _SystemVoltage_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 14),
    _SystemVoltage_Type()
)
systemVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemVoltage.setStatus("current")


class _SystemFans_Type(Integer32):
    """Custom type systemFans based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("half-on", 1),
          ("on", 3))
    )


_SystemFans_Type.__name__ = "Integer32"
_SystemFans_Object = MibScalar
systemFans = _SystemFans_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 15),
    _SystemFans_Type()
)
systemFans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemFans.setStatus("current")


class _SystemType_Type(Integer32):
    """Custom type systemType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("local", 0),
          ("external-snmp", 1),
          ("not-used-1", 2),
          ("not-used-2", 3),
          ("mem-nCC", 4))
    )


_SystemType_Type.__name__ = "Integer32"
_SystemType_Object = MibScalar
systemType = _SystemType_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 16),
    _SystemType_Type()
)
systemType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemType.setStatus("current")


class _SystemModelNo_Type(Integer32):
    """Custom type systemModelNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              100)
        )
    )
    namedValues = NamedValues(
        *(("e5210", 0),
          ("e5410", 1),
          ("e5420", 2),
          ("e5610", 3),
          ("e5424", 4),
          ("e5428", 5),
          ("e5820", 6),
          ("e6100", 7),
          ("e5710", 8),
          ("e5714", 9),
          ("e5720", 10),
          ("e5740", 11),
          ("e5744", 12),
          ("e5748", 13),
          ("e5750", 14),
          ("e5760", 15),
          ("e5715", 16),
          ("e5780", 17),
          ("en5920", 18),
          ("e5770", 19),
          ("e5784", 20),
          ("e5745", 21),
          ("e5775", 22),
          ("en5930", 23),
          ("e5782", 24),
          ("e5788", 25),
          ("en5980", 26),
          ("en5990", 27),
          ("unknown", 100))
    )


_SystemModelNo_Type.__name__ = "Integer32"
_SystemModelNo_Object = MibScalar
systemModelNo = _SystemModelNo_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 17),
    _SystemModelNo_Type()
)
systemModelNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemModelNo.setStatus("current")


class _SystemSyntax_Type(Integer32):
    """Custom type systemSyntax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dVB", 0),
          ("aTSC", 1),
          ("dSS", 2))
    )


_SystemSyntax_Type.__name__ = "Integer32"
_SystemSyntax_Object = MibScalar
systemSyntax = _SystemSyntax_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 18),
    _SystemSyntax_Type()
)
systemSyntax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemSyntax.setStatus("current")


class _SystemControlMode_Type(Integer32):
    """Custom type systemControlMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("encodeMode", 0),
          ("testMode", 1),
          ("downloadMode", 2))
    )


_SystemControlMode_Type.__name__ = "Integer32"
_SystemControlMode_Object = MibScalar
systemControlMode = _SystemControlMode_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 19),
    _SystemControlMode_Type()
)
systemControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemControlMode.setStatus("current")


class _SystemStoreActiveConfig_Type(Integer32):
    """Custom type systemStoreActiveConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_SystemStoreActiveConfig_Type.__name__ = "Integer32"
_SystemStoreActiveConfig_Object = MibScalar
systemStoreActiveConfig = _SystemStoreActiveConfig_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 20),
    _SystemStoreActiveConfig_Type()
)
systemStoreActiveConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemStoreActiveConfig.setStatus("current")


class _SystemStartTest_Type(Integer32):
    """Custom type systemStartTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SystemStartTest_Type.__name__ = "Integer32"
_SystemStartTest_Object = MibScalar
systemStartTest = _SystemStartTest_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 21),
    _SystemStartTest_Type()
)
systemStartTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemStartTest.setStatus("current")
_StartupTestTable_Object = MibTable
startupTestTable = _StartupTestTable_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 22)
)
if mibBuilder.loadTexts:
    startupTestTable.setStatus("current")
_StartupTestEntry_Object = MibTableRow
startupTestEntry = _StartupTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 22, 1)
)
startupTestEntry.setIndexNames(
    (0, "NDS-DTH3-SYSTEM", "startupTestIndex"),
)
if mibBuilder.loadTexts:
    startupTestEntry.setStatus("current")


class _StartupTestIndex_Type(Integer32):
    """Custom type startupTestIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_StartupTestIndex_Type.__name__ = "Integer32"
_StartupTestIndex_Object = MibTableColumn
startupTestIndex = _StartupTestIndex_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 22, 1, 1),
    _StartupTestIndex_Type()
)
startupTestIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    startupTestIndex.setStatus("current")


class _StartupTestExec_Type(Integer32):
    """Custom type startupTestExec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("stop", 0),
          ("start", 1))
    )


_StartupTestExec_Type.__name__ = "Integer32"
_StartupTestExec_Object = MibTableColumn
startupTestExec = _StartupTestExec_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 22, 1, 2),
    _StartupTestExec_Type()
)
startupTestExec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    startupTestExec.setStatus("current")


class _StartupTestResult_Type(Integer32):
    """Custom type startupTestResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_StartupTestResult_Type.__name__ = "Integer32"
_StartupTestResult_Object = MibTableColumn
startupTestResult = _StartupTestResult_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 22, 1, 3),
    _StartupTestResult_Type()
)
startupTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    startupTestResult.setStatus("current")
_StartupTestName_Type = DisplayString
_StartupTestName_Object = MibTableColumn
startupTestName = _StartupTestName_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 22, 1, 4),
    _StartupTestName_Type()
)
startupTestName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    startupTestName.setStatus("current")
_StdTestTable_Object = MibTable
stdTestTable = _StdTestTable_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 23)
)
if mibBuilder.loadTexts:
    stdTestTable.setStatus("current")
_StdTestEntry_Object = MibTableRow
stdTestEntry = _StdTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 23, 1)
)
stdTestEntry.setIndexNames(
    (0, "NDS-DTH3-SYSTEM", "stdTestIndex"),
)
if mibBuilder.loadTexts:
    stdTestEntry.setStatus("current")


class _StdTestIndex_Type(Integer32):
    """Custom type stdTestIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_StdTestIndex_Type.__name__ = "Integer32"
_StdTestIndex_Object = MibTableColumn
stdTestIndex = _StdTestIndex_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 23, 1, 1),
    _StdTestIndex_Type()
)
stdTestIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stdTestIndex.setStatus("current")


class _StdTestExec_Type(Integer32):
    """Custom type stdTestExec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("stop", 0),
          ("start", 1))
    )


_StdTestExec_Type.__name__ = "Integer32"
_StdTestExec_Object = MibTableColumn
stdTestExec = _StdTestExec_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 23, 1, 2),
    _StdTestExec_Type()
)
stdTestExec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stdTestExec.setStatus("current")


class _StdTestResult_Type(Integer32):
    """Custom type stdTestResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_StdTestResult_Type.__name__ = "Integer32"
_StdTestResult_Object = MibTableColumn
stdTestResult = _StdTestResult_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 23, 1, 3),
    _StdTestResult_Type()
)
stdTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stdTestResult.setStatus("current")
_StdTestName_Type = DisplayString
_StdTestName_Object = MibTableColumn
stdTestName = _StdTestName_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 23, 1, 4),
    _StdTestName_Type()
)
stdTestName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stdTestName.setStatus("current")


class _SystemBuildDate_Type(DisplayString):
    """Custom type systemBuildDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_SystemBuildDate_Type.__name__ = "DisplayString"
_SystemBuildDate_Object = MibScalar
systemBuildDate = _SystemBuildDate_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 24),
    _SystemBuildDate_Type()
)
systemBuildDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemBuildDate.setStatus("current")


class _SystemModelDescription_Type(DisplayString):
    """Custom type systemModelDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_SystemModelDescription_Type.__name__ = "DisplayString"
_SystemModelDescription_Object = MibScalar
systemModelDescription = _SystemModelDescription_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 25),
    _SystemModelDescription_Type()
)
systemModelDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemModelDescription.setStatus("current")
_LicenceTable_Object = MibTable
licenceTable = _LicenceTable_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 26)
)
if mibBuilder.loadTexts:
    licenceTable.setStatus("current")
_LicenceEntry_Object = MibTableRow
licenceEntry = _LicenceEntry_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 26, 1)
)
licenceEntry.setIndexNames(
    (0, "NDS-DTH3-SYSTEM", "licenceIndex"),
)
if mibBuilder.loadTexts:
    licenceEntry.setStatus("current")


class _LicenceIndex_Type(Integer32):
    """Custom type licenceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_LicenceIndex_Type.__name__ = "Integer32"
_LicenceIndex_Object = MibTableColumn
licenceIndex = _LicenceIndex_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 26, 1, 1),
    _LicenceIndex_Type()
)
licenceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenceIndex.setStatus("current")
_LicenceDescription_Type = DisplayString
_LicenceDescription_Object = MibTableColumn
licenceDescription = _LicenceDescription_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 26, 1, 2),
    _LicenceDescription_Type()
)
licenceDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenceDescription.setStatus("current")


class _LicenceId_Type(Integer32):
    """Custom type licenceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45)
        )
    )
    namedValues = NamedValues(
        *(("not-enabled", 0),
          ("dolby-digital-AC-3", 1),
          ("video422P-at-ML", 2),
          ("reflex", 3),
          ("noise-reduction", 4),
          ("advanced-VBI", 5),
          ("performance-upgrade", 6),
          ("motherboard-data-input", 7),
          ("composite-video-In", 8),
          ("ras", 9),
          ("sat-mod3", 10),
          ("mod16QAM", 11),
          ("atm", 12),
          ("unassigned-13", 13),
          ("ofdm", 14),
          ("remux", 15),
          ("psip-insertion", 16),
          ("biss", 17),
          ("vbi-in-picture", 18),
          ("mod8PSK", 19),
          ("auto-concatenation", 20),
          ("demod-16QAM", 21),
          ("hd-Noise-reduction", 22),
          ("hd-Upconversion", 23),
          ("low-Symbol-Rate", 24),
          ("video-SDI-input", 25),
          ("audio-2-Stereo-Pairs", 26),
          ("e5705", 27),
          ("hd-ATSC", 28),
          ("hd-DVB", 29),
          ("hd-vbr-reflex", 30),
          ("hd-422", 31),
          ("hd-Down-Conversion", 32),
          ("hd-Up-Down-Simulcast", 33),
          ("hd-Improved", 34),
          ("scte-35-Splice-Points", 35),
          ("dts-Audio", 36),
          ("stream-Event", 37),
          ("dual-WMV9-MPEG2", 38),
          ("motion-compensated-noise-reduction", 39),
          ("hd-Auto-Concatenation", 40),
          ("nabts-Gemstar", 41),
          ("wm9-Multicast", 42),
          ("wm9-Digital-Rights-Management", 43),
          ("wm-Advanced", 44),
          ("wm-ASI-VC9", 45))
    )


_LicenceId_Type.__name__ = "Integer32"
_LicenceId_Object = MibTableColumn
licenceId = _LicenceId_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 26, 1, 3),
    _LicenceId_Type()
)
licenceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenceId.setStatus("current")
_LicenceCode_Type = DisplayString
_LicenceCode_Object = MibTableColumn
licenceCode = _LicenceCode_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 26, 1, 4),
    _LicenceCode_Type()
)
licenceCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenceCode.setStatus("current")


class _SystemLoadActiveConfig_Type(Integer32):
    """Custom type systemLoadActiveConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_SystemLoadActiveConfig_Type.__name__ = "Integer32"
_SystemLoadActiveConfig_Object = MibScalar
systemLoadActiveConfig = _SystemLoadActiveConfig_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 27),
    _SystemLoadActiveConfig_Type()
)
systemLoadActiveConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemLoadActiveConfig.setStatus("current")


class _SystemResetOnDownload_Type(Integer32):
    """Custom type systemResetOnDownload based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("do-not-reset", 0),
          ("auto-reset-on-download", 1))
    )


_SystemResetOnDownload_Type.__name__ = "Integer32"
_SystemResetOnDownload_Object = MibScalar
systemResetOnDownload = _SystemResetOnDownload_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 28),
    _SystemResetOnDownload_Type()
)
systemResetOnDownload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemResetOnDownload.setStatus("current")


class _SystemResetEncoder_Type(Integer32):
    """Custom type systemResetEncoder based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no-action", 0),
          ("reset", 1))
    )


_SystemResetEncoder_Type.__name__ = "Integer32"
_SystemResetEncoder_Object = MibScalar
systemResetEncoder = _SystemResetEncoder_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 29),
    _SystemResetEncoder_Type()
)
systemResetEncoder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemResetEncoder.setStatus("current")
_SystemReflexControllerIPAddress_Type = IpAddress
_SystemReflexControllerIPAddress_Object = MibScalar
systemReflexControllerIPAddress = _SystemReflexControllerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 30),
    _SystemReflexControllerIPAddress_Type()
)
systemReflexControllerIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemReflexControllerIPAddress.setStatus("current")


class _SystemReflexConfigPort_Type(Integer32):
    """Custom type systemReflexConfigPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SystemReflexConfigPort_Type.__name__ = "Integer32"
_SystemReflexConfigPort_Object = MibScalar
systemReflexConfigPort = _SystemReflexConfigPort_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 31),
    _SystemReflexConfigPort_Type()
)
systemReflexConfigPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemReflexConfigPort.setStatus("current")


class _SystemReflexOutputPort_Type(Integer32):
    """Custom type systemReflexOutputPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SystemReflexOutputPort_Type.__name__ = "Integer32"
_SystemReflexOutputPort_Object = MibScalar
systemReflexOutputPort = _SystemReflexOutputPort_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 32),
    _SystemReflexOutputPort_Type()
)
systemReflexOutputPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemReflexOutputPort.setStatus("current")


class _SystemReflexEncoderNumber_Type(Integer32):
    """Custom type systemReflexEncoderNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SystemReflexEncoderNumber_Type.__name__ = "Integer32"
_SystemReflexEncoderNumber_Object = MibScalar
systemReflexEncoderNumber = _SystemReflexEncoderNumber_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 33),
    _SystemReflexEncoderNumber_Type()
)
systemReflexEncoderNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemReflexEncoderNumber.setStatus("current")


class _SystemReflexGroup_Type(Integer32):
    """Custom type systemReflexGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SystemReflexGroup_Type.__name__ = "Integer32"
_SystemReflexGroup_Object = MibScalar
systemReflexGroup = _SystemReflexGroup_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 34),
    _SystemReflexGroup_Type()
)
systemReflexGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemReflexGroup.setStatus("current")


class _SystemReflexIndex_Type(Integer32):
    """Custom type systemReflexIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SystemReflexIndex_Type.__name__ = "Integer32"
_SystemReflexIndex_Object = MibScalar
systemReflexIndex = _SystemReflexIndex_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 35),
    _SystemReflexIndex_Type()
)
systemReflexIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemReflexIndex.setStatus("current")


class _SystemFeatureList_Type(OctetString):
    """Custom type systemFeatureList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_SystemFeatureList_Type.__name__ = "OctetString"
_SystemFeatureList_Object = MibScalar
systemFeatureList = _SystemFeatureList_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 36),
    _SystemFeatureList_Type()
)
systemFeatureList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemFeatureList.setStatus("current")


class _SystemSNMPControl_Type(Integer32):
    """Custom type systemSNMPControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no-reply-during-initialisation", 0),
          ("reply-during-initialisation", 1))
    )


_SystemSNMPControl_Type.__name__ = "Integer32"
_SystemSNMPControl_Object = MibScalar
systemSNMPControl = _SystemSNMPControl_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 37),
    _SystemSNMPControl_Type()
)
systemSNMPControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemSNMPControl.setStatus("current")


class _SystemOutputMode_Type(Integer32):
    """Custom type systemOutputMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("asi", 0),
          ("satellite-modulator", 1),
          ("cofdm", 2),
          ("cofdm-and-satellite-modulator", 3),
          ("ip-only", 4))
    )


_SystemOutputMode_Type.__name__ = "Integer32"
_SystemOutputMode_Object = MibScalar
systemOutputMode = _SystemOutputMode_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 38),
    _SystemOutputMode_Type()
)
systemOutputMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemOutputMode.setStatus("current")


class _SystemBoxSerialNo_Type(Integer32):
    """Custom type systemBoxSerialNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SystemBoxSerialNo_Type.__name__ = "Integer32"
_SystemBoxSerialNo_Object = MibScalar
systemBoxSerialNo = _SystemBoxSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 39),
    _SystemBoxSerialNo_Type()
)
systemBoxSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemBoxSerialNo.setStatus("current")


class _SystemPCBTypeNo_Type(DisplayString):
    """Custom type systemPCBTypeNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_SystemPCBTypeNo_Type.__name__ = "DisplayString"
_SystemPCBTypeNo_Object = MibScalar
systemPCBTypeNo = _SystemPCBTypeNo_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 40),
    _SystemPCBTypeNo_Type()
)
systemPCBTypeNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemPCBTypeNo.setStatus("current")


class _SystemPCBIssue_Type(Integer32):
    """Custom type systemPCBIssue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SystemPCBIssue_Type.__name__ = "Integer32"
_SystemPCBIssue_Object = MibScalar
systemPCBIssue = _SystemPCBIssue_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 41),
    _SystemPCBIssue_Type()
)
systemPCBIssue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemPCBIssue.setStatus("current")


class _SystemPCBModStrike_Type(Integer32):
    """Custom type systemPCBModStrike based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SystemPCBModStrike_Type.__name__ = "Integer32"
_SystemPCBModStrike_Object = MibScalar
systemPCBModStrike = _SystemPCBModStrike_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 42),
    _SystemPCBModStrike_Type()
)
systemPCBModStrike.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemPCBModStrike.setStatus("current")


class _SystemBackplaneTypeNo_Type(DisplayString):
    """Custom type systemBackplaneTypeNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_SystemBackplaneTypeNo_Type.__name__ = "DisplayString"
_SystemBackplaneTypeNo_Object = MibScalar
systemBackplaneTypeNo = _SystemBackplaneTypeNo_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 43),
    _SystemBackplaneTypeNo_Type()
)
systemBackplaneTypeNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemBackplaneTypeNo.setStatus("current")


class _SystemBackplanePCBIssue_Type(Integer32):
    """Custom type systemBackplanePCBIssue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SystemBackplanePCBIssue_Type.__name__ = "Integer32"
_SystemBackplanePCBIssue_Object = MibScalar
systemBackplanePCBIssue = _SystemBackplanePCBIssue_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 44),
    _SystemBackplanePCBIssue_Type()
)
systemBackplanePCBIssue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemBackplanePCBIssue.setStatus("current")


class _SystemBackplaneFirmware_Type(DisplayString):
    """Custom type systemBackplaneFirmware based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_SystemBackplaneFirmware_Type.__name__ = "DisplayString"
_SystemBackplaneFirmware_Object = MibScalar
systemBackplaneFirmware = _SystemBackplaneFirmware_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 45),
    _SystemBackplaneFirmware_Type()
)
systemBackplaneFirmware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemBackplaneFirmware.setStatus("current")


class _SystemSABusAddress_Type(Integer32):
    """Custom type systemSABusAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(49, 127),
    )


_SystemSABusAddress_Type.__name__ = "Integer32"
_SystemSABusAddress_Object = MibScalar
systemSABusAddress = _SystemSABusAddress_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 46),
    _SystemSABusAddress_Type()
)
systemSABusAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemSABusAddress.setStatus("current")


class _SystemSABusSerialProtocol_Type(Integer32):
    """Custom type systemSABusSerialProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("rs485", 0),
          ("rs232", 1))
    )


_SystemSABusSerialProtocol_Type.__name__ = "Integer32"
_SystemSABusSerialProtocol_Object = MibScalar
systemSABusSerialProtocol = _SystemSABusSerialProtocol_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 47),
    _SystemSABusSerialProtocol_Type()
)
systemSABusSerialProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemSABusSerialProtocol.setStatus("current")


class _SystemSABusBaudRate_Type(Integer32):
    """Custom type systemSABusBaudRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("baud-1200", 0),
          ("baud-2400", 1),
          ("baud-4800", 2),
          ("baud-9600", 3),
          ("baud-19200", 4),
          ("baud-38400", 5))
    )


_SystemSABusBaudRate_Type.__name__ = "Integer32"
_SystemSABusBaudRate_Object = MibScalar
systemSABusBaudRate = _SystemSABusBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 48),
    _SystemSABusBaudRate_Type()
)
systemSABusBaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemSABusBaudRate.setStatus("current")


class _SystemSABusDataBits_Type(Integer32):
    """Custom type systemSABusDataBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("seven-2-stop-bits", 0),
          ("eight-1-stop-bit", 1))
    )


_SystemSABusDataBits_Type.__name__ = "Integer32"
_SystemSABusDataBits_Object = MibScalar
systemSABusDataBits = _SystemSABusDataBits_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 49),
    _SystemSABusDataBits_Type()
)
systemSABusDataBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemSABusDataBits.setStatus("current")


class _SystemPCRData_Type(Integer32):
    """Custom type systemPCRData based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_SystemPCRData_Type.__name__ = "Integer32"
_SystemPCRData_Object = MibScalar
systemPCRData = _SystemPCRData_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 50),
    _SystemPCRData_Type()
)
systemPCRData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemPCRData.setStatus("current")
_SystemPCRDataIPAddress_Type = IpAddress
_SystemPCRDataIPAddress_Object = MibScalar
systemPCRDataIPAddress = _SystemPCRDataIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 51),
    _SystemPCRDataIPAddress_Type()
)
systemPCRDataIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemPCRDataIPAddress.setStatus("current")


class _SystemPCRDataUDPPort_Type(Integer32):
    """Custom type systemPCRDataUDPPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SystemPCRDataUDPPort_Type.__name__ = "Integer32"
_SystemPCRDataUDPPort_Object = MibScalar
systemPCRDataUDPPort = _SystemPCRDataUDPPort_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 52),
    _SystemPCRDataUDPPort_Type()
)
systemPCRDataUDPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemPCRDataUDPPort.setStatus("current")


class _SystemTrapSendLevel_Type(Integer32):
    """Custom type systemTrapSendLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("all-traps", 0),
          ("fail-and-start-messages", 1),
          ("start-messages-only", 2))
    )


_SystemTrapSendLevel_Type.__name__ = "Integer32"
_SystemTrapSendLevel_Object = MibScalar
systemTrapSendLevel = _SystemTrapSendLevel_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 53),
    _SystemTrapSendLevel_Type()
)
systemTrapSendLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemTrapSendLevel.setStatus("current")


class _SystemActionOnPIDError_Type(Integer32):
    """Custom type systemActionOnPIDError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("auto-correct", 0),
          ("raise-alarm", 1))
    )


_SystemActionOnPIDError_Type.__name__ = "Integer32"
_SystemActionOnPIDError_Object = MibScalar
systemActionOnPIDError = _SystemActionOnPIDError_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 54),
    _SystemActionOnPIDError_Type()
)
systemActionOnPIDError.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemActionOnPIDError.setStatus("current")


class _SystemMHPContentId_Type(Unsigned32):
    """Custom type systemMHPContentId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SystemMHPContentId_Type.__name__ = "Unsigned32"
_SystemMHPContentId_Object = MibScalar
systemMHPContentId = _SystemMHPContentId_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 55),
    _SystemMHPContentId_Type()
)
systemMHPContentId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemMHPContentId.setStatus("current")


class _SystemReflexExtendedMode_Type(Integer32):
    """Custom type systemReflexExtendedMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_SystemReflexExtendedMode_Type.__name__ = "Integer32"
_SystemReflexExtendedMode_Object = MibScalar
systemReflexExtendedMode = _SystemReflexExtendedMode_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 1, 56),
    _SystemReflexExtendedMode_Type()
)
systemReflexExtendedMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemReflexExtendedMode.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NDS-DTH3-SYSTEM",
    **{"ndsDTH3Encoder": ndsDTH3Encoder,
       "systemEnc": systemEnc,
       "systemSerialNumber": systemSerialNumber,
       "systemHardwareRelease": systemHardwareRelease,
       "systemSoftwareRelease": systemSoftwareRelease,
       "systemFirmwareRelease": systemFirmwareRelease,
       "systemBuildStandard": systemBuildStandard,
       "systemTimeDate": systemTimeDate,
       "systemnextTimeDate": systemnextTimeDate,
       "systemTimeSwitch": systemTimeSwitch,
       "systemServiceLevel": systemServiceLevel,
       "moduleTable": moduleTable,
       "moduleEntry": moduleEntry,
       "moduleIndex": moduleIndex,
       "moduleType": moduleType,
       "moduleId": moduleId,
       "systemTable": systemTable,
       "systemEntry": systemEntry,
       "systemCurrentNextIndex": systemCurrentNextIndex,
       "systemSplicing": systemSplicing,
       "systemClockSource": systemClockSource,
       "systemNetworkName": systemNetworkName,
       "systemServiceName": systemServiceName,
       "systemNetworkID": systemNetworkID,
       "systemServiceID": systemServiceID,
       "systemTSID": systemTSID,
       "systemSIInformation": systemSIInformation,
       "systemDONOTUSEReflexIPAddress": systemDONOTUSEReflexIPAddress,
       "systemDONOTUSEReflexUDPPort": systemDONOTUSEReflexUDPPort,
       "systemEncoderNumber": systemEncoderNumber,
       "systemLCDMode": systemLCDMode,
       "systemFailRelay": systemFailRelay,
       "systemAlarmRelay": systemAlarmRelay,
       "systemPMTPID": systemPMTPID,
       "systemServiceProvider": systemServiceProvider,
       "systemAC3AudioDescriptor": systemAC3AudioDescriptor,
       "systemDVBServiceType": systemDVBServiceType,
       "systemATSCServiceType": systemATSCServiceType,
       "systemATSCProgramNumber": systemATSCProgramNumber,
       "systemATSCProgramParadigm": systemATSCProgramParadigm,
       "systemDVBStreamIdentifier": systemDVBStreamIdentifier,
       "systemPSIPExternalSource": systemPSIPExternalSource,
       "systemPSIPMinPID": systemPSIPMinPID,
       "systemPSIPMaxPID": systemPSIPMaxPID,
       "systemBroadcastFlag": systemBroadcastFlag,
       "systemLCDTable": systemLCDTable,
       "systemLCDEntry": systemLCDEntry,
       "systemLCDCurrentNextIndex": systemLCDCurrentNextIndex,
       "systemLCDLine": systemLCDLine,
       "systemLCDText": systemLCDText,
       "systemTemperature": systemTemperature,
       "systemVoltage": systemVoltage,
       "systemFans": systemFans,
       "systemType": systemType,
       "systemModelNo": systemModelNo,
       "systemSyntax": systemSyntax,
       "systemControlMode": systemControlMode,
       "systemStoreActiveConfig": systemStoreActiveConfig,
       "systemStartTest": systemStartTest,
       "startupTestTable": startupTestTable,
       "startupTestEntry": startupTestEntry,
       "startupTestIndex": startupTestIndex,
       "startupTestExec": startupTestExec,
       "startupTestResult": startupTestResult,
       "startupTestName": startupTestName,
       "stdTestTable": stdTestTable,
       "stdTestEntry": stdTestEntry,
       "stdTestIndex": stdTestIndex,
       "stdTestExec": stdTestExec,
       "stdTestResult": stdTestResult,
       "stdTestName": stdTestName,
       "systemBuildDate": systemBuildDate,
       "systemModelDescription": systemModelDescription,
       "licenceTable": licenceTable,
       "licenceEntry": licenceEntry,
       "licenceIndex": licenceIndex,
       "licenceDescription": licenceDescription,
       "licenceId": licenceId,
       "licenceCode": licenceCode,
       "systemLoadActiveConfig": systemLoadActiveConfig,
       "systemResetOnDownload": systemResetOnDownload,
       "systemResetEncoder": systemResetEncoder,
       "systemReflexControllerIPAddress": systemReflexControllerIPAddress,
       "systemReflexConfigPort": systemReflexConfigPort,
       "systemReflexOutputPort": systemReflexOutputPort,
       "systemReflexEncoderNumber": systemReflexEncoderNumber,
       "systemReflexGroup": systemReflexGroup,
       "systemReflexIndex": systemReflexIndex,
       "systemFeatureList": systemFeatureList,
       "systemSNMPControl": systemSNMPControl,
       "systemOutputMode": systemOutputMode,
       "systemBoxSerialNo": systemBoxSerialNo,
       "systemPCBTypeNo": systemPCBTypeNo,
       "systemPCBIssue": systemPCBIssue,
       "systemPCBModStrike": systemPCBModStrike,
       "systemBackplaneTypeNo": systemBackplaneTypeNo,
       "systemBackplanePCBIssue": systemBackplanePCBIssue,
       "systemBackplaneFirmware": systemBackplaneFirmware,
       "systemSABusAddress": systemSABusAddress,
       "systemSABusSerialProtocol": systemSABusSerialProtocol,
       "systemSABusBaudRate": systemSABusBaudRate,
       "systemSABusDataBits": systemSABusDataBits,
       "systemPCRData": systemPCRData,
       "systemPCRDataIPAddress": systemPCRDataIPAddress,
       "systemPCRDataUDPPort": systemPCRDataUDPPort,
       "systemTrapSendLevel": systemTrapSendLevel,
       "systemActionOnPIDError": systemActionOnPIDError,
       "systemMHPContentId": systemMHPContentId,
       "systemReflexExtendedMode": systemReflexExtendedMode}
)
