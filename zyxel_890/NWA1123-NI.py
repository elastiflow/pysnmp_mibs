# SNMP MIB module (NWA1123-NI) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/zyxel_890/NWA1123-NI.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 10:30:51 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

(DisplayString,
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

nwa1123ni = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Zyxel_ObjectIdentity = ObjectIdentity
zyxel = _Zyxel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890)
)
_NwaSeries_ObjectIdentity = ObjectIdentity
nwaSeries = _NwaSeries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1)
)
_EsMgmt_ObjectIdentity = ObjectIdentity
esMgmt = _EsMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3)
)
_EsSysInfo_ObjectIdentity = ObjectIdentity
esSysInfo = _EsSysInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 1)
)
_SysSwPlatform_Type = DisplayString
_SysSwPlatform_Object = MibScalar
sysSwPlatform = _SysSwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 1, 1),
    _SysSwPlatform_Type()
)
sysSwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSwPlatform.setStatus("current")
_SysSwMajorVersion_Type = DisplayString
_SysSwMajorVersion_Object = MibScalar
sysSwMajorVersion = _SysSwMajorVersion_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 1, 2),
    _SysSwMajorVersion_Type()
)
sysSwMajorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSwMajorVersion.setStatus("current")
_SysSwMinorVersion_Type = DisplayString
_SysSwMinorVersion_Object = MibScalar
sysSwMinorVersion = _SysSwMinorVersion_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 1, 3),
    _SysSwMinorVersion_Type()
)
sysSwMinorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSwMinorVersion.setStatus("current")
_SysSwModel_Type = DisplayString
_SysSwModel_Object = MibScalar
sysSwModel = _SysSwModel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 1, 4),
    _SysSwModel_Type()
)
sysSwModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSwModel.setStatus("current")
_SysSwPatchNumber_Type = DisplayString
_SysSwPatchNumber_Object = MibScalar
sysSwPatchNumber = _SysSwPatchNumber_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 1, 5),
    _SysSwPatchNumber_Type()
)
sysSwPatchNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSwPatchNumber.setStatus("current")
_SysSwVersionString_Type = DisplayString
_SysSwVersionString_Object = MibScalar
sysSwVersionString = _SysSwVersionString_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 1, 6),
    _SysSwVersionString_Type()
)
sysSwVersionString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSwVersionString.setStatus("current")
_SysSwDay_Type = DisplayString
_SysSwDay_Object = MibScalar
sysSwDay = _SysSwDay_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 1, 7),
    _SysSwDay_Type()
)
sysSwDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSwDay.setStatus("current")
_SysSwMonth_Type = DisplayString
_SysSwMonth_Object = MibScalar
sysSwMonth = _SysSwMonth_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 1, 8),
    _SysSwMonth_Type()
)
sysSwMonth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSwMonth.setStatus("current")
_SysSwYear_Type = DisplayString
_SysSwYear_Object = MibScalar
sysSwYear = _SysSwYear_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 1, 9),
    _SysSwYear_Type()
)
sysSwYear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSwYear.setStatus("current")
_SysProductFamily_Type = DisplayString
_SysProductFamily_Object = MibScalar
sysProductFamily = _SysProductFamily_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 1, 10),
    _SysProductFamily_Type()
)
sysProductFamily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysProductFamily.setStatus("current")
_SysProductModel_Type = DisplayString
_SysProductModel_Object = MibScalar
sysProductModel = _SysProductModel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 1, 11),
    _SysProductModel_Type()
)
sysProductModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysProductModel.setStatus("current")
_SysProductSerialNumber_Type = DisplayString
_SysProductSerialNumber_Object = MibScalar
sysProductSerialNumber = _SysProductSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 1, 12),
    _SysProductSerialNumber_Type()
)
sysProductSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysProductSerialNumber.setStatus("current")
_SysHwMajorVersion_Type = DisplayString
_SysHwMajorVersion_Object = MibScalar
sysHwMajorVersion = _SysHwMajorVersion_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 1, 13),
    _SysHwMajorVersion_Type()
)
sysHwMajorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysHwMajorVersion.setStatus("current")
_SysHwMinorVersion_Type = DisplayString
_SysHwMinorVersion_Object = MibScalar
sysHwMinorVersion = _SysHwMinorVersion_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 1, 14),
    _SysHwMinorVersion_Type()
)
sysHwMinorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysHwMinorVersion.setStatus("current")
_SysHwVersionString_Type = DisplayString
_SysHwVersionString_Object = MibScalar
sysHwVersionString = _SysHwVersionString_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 1, 15),
    _SysHwVersionString_Type()
)
sysHwVersionString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysHwVersionString.setStatus("current")


class _SysCountryCode_Type(Integer32):
    """Custom type sysCountryCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(36,
              40,
              124,
              156,
              158,
              208,
              246,
              250,
              276,
              344,
              352,
              356,
              372,
              380,
              392,
              438,
              442,
              528,
              554,
              578,
              620,
              702,
              724,
              752,
              756,
              826,
              840)
        )
    )
    namedValues = NamedValues(
        *(("au", 36),
          ("ai", 40),
          ("ca", 124),
          ("cn", 156),
          ("tw", 158),
          ("dk", 208),
          ("fi", 246),
          ("fr", 250),
          ("de", 276),
          ("hk", 344),
          ("is", 352),
          ("id", 356),
          ("ie", 372),
          ("it", 380),
          ("jp", 392),
          ("li", 438),
          ("lu", 442),
          ("nl", 528),
          ("nz", 554),
          ("no", 578),
          ("pt", 620),
          ("sg", 702),
          ("es", 724),
          ("se", 752),
          ("ch", 756),
          ("uk", 826),
          ("us", 840))
    )


_SysCountryCode_Type.__name__ = "Integer32"
_SysCountryCode_Object = MibScalar
sysCountryCode = _SysCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 1, 16),
    _SysCountryCode_Type()
)
sysCountryCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysCountryCode.setStatus("current")
_SysCurrentDateTime_Type = DisplayString
_SysCurrentDateTime_Object = MibScalar
sysCurrentDateTime = _SysCurrentDateTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 1, 17),
    _SysCurrentDateTime_Type()
)
sysCurrentDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysCurrentDateTime.setStatus("current")
_SysCurrentTime_Type = DisplayString
_SysCurrentTime_Object = MibScalar
sysCurrentTime = _SysCurrentTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 1, 18),
    _SysCurrentTime_Type()
)
sysCurrentTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysCurrentTime.setStatus("current")
_EsSysMgmt_ObjectIdentity = ObjectIdentity
esSysMgmt = _EsSysMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 2)
)


class _SysMgmtReboot_Type(Integer32):
    """Custom type sysMgmtReboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_SysMgmtReboot_Type.__name__ = "Integer32"
_SysMgmtReboot_Object = MibScalar
sysMgmtReboot = _SysMgmtReboot_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 2, 1),
    _SysMgmtReboot_Type()
)
sysMgmtReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMgmtReboot.setStatus("current")
_SysMgmtConfigSave_Type = OctetString
_SysMgmtConfigSave_Object = MibScalar
sysMgmtConfigSave = _SysMgmtConfigSave_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 2, 2),
    _SysMgmtConfigSave_Type()
)
sysMgmtConfigSave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMgmtConfigSave.setStatus("current")


class _SysMgmtRestoreDefaultConfig_Type(Integer32):
    """Custom type sysMgmtRestoreDefaultConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("running", 0),
          ("restore", 1))
    )


_SysMgmtRestoreDefaultConfig_Type.__name__ = "Integer32"
_SysMgmtRestoreDefaultConfig_Object = MibScalar
sysMgmtRestoreDefaultConfig = _SysMgmtRestoreDefaultConfig_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 2, 3),
    _SysMgmtRestoreDefaultConfig_Type()
)
sysMgmtRestoreDefaultConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMgmtRestoreDefaultConfig.setStatus("current")


class _SysMgmtCPUUsage_Type(DisplayString):
    """Custom type sysMgmtCPUUsage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_SysMgmtCPUUsage_Type.__name__ = "DisplayString"
_SysMgmtCPUUsage_Object = MibScalar
sysMgmtCPUUsage = _SysMgmtCPUUsage_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 2, 4),
    _SysMgmtCPUUsage_Type()
)
sysMgmtCPUUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMgmtCPUUsage.setStatus("current")


class _SysMgmtMemUsage_Type(DisplayString):
    """Custom type sysMgmtMemUsage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_SysMgmtMemUsage_Type.__name__ = "DisplayString"
_SysMgmtMemUsage_Object = MibScalar
sysMgmtMemUsage = _SysMgmtMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 2, 5),
    _SysMgmtMemUsage_Type()
)
sysMgmtMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMgmtMemUsage.setStatus("current")


class _SysMgmtFlashUsage_Type(DisplayString):
    """Custom type sysMgmtFlashUsage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_SysMgmtFlashUsage_Type.__name__ = "DisplayString"
_SysMgmtFlashUsage_Object = MibScalar
sysMgmtFlashUsage = _SysMgmtFlashUsage_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 2, 6),
    _SysMgmtFlashUsage_Type()
)
sysMgmtFlashUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMgmtFlashUsage.setStatus("current")


class _SysMgmtVLANControl_Type(Integer32):
    """Custom type sysMgmtVLANControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_SysMgmtVLANControl_Type.__name__ = "Integer32"
_SysMgmtVLANControl_Object = MibScalar
sysMgmtVLANControl = _SysMgmtVLANControl_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 2, 13),
    _SysMgmtVLANControl_Type()
)
sysMgmtVLANControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMgmtVLANControl.setStatus("current")


class _SysMgmtVLANID_Type(Integer32):
    """Custom type sysMgmtVLANID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_SysMgmtVLANID_Type.__name__ = "Integer32"
_SysMgmtVLANID_Object = MibScalar
sysMgmtVLANID = _SysMgmtVLANID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 2, 14),
    _SysMgmtVLANID_Type()
)
sysMgmtVLANID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMgmtVLANID.setStatus("current")


class _Sys8021QControl_Type(Integer32):
    """Custom type sys8021QControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_Sys8021QControl_Type.__name__ = "Integer32"
_Sys8021QControl_Object = MibScalar
sys8021QControl = _Sys8021QControl_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 2, 15),
    _Sys8021QControl_Type()
)
sys8021QControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sys8021QControl.setStatus("current")
_DevGatewayIPAddr_Type = IpAddress
_DevGatewayIPAddr_Object = MibScalar
devGatewayIPAddr = _DevGatewayIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 2, 17),
    _DevGatewayIPAddr_Type()
)
devGatewayIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devGatewayIPAddr.setStatus("current")
_AdminPassword_Type = DisplayString
_AdminPassword_Object = MibScalar
adminPassword = _AdminPassword_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 2, 18),
    _AdminPassword_Type()
)
adminPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminPassword.setStatus("current")
_EsWireless_ObjectIdentity = ObjectIdentity
esWireless = _EsWireless_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5)
)
_WlanRadioTable_Object = MibTable
wlanRadioTable = _WlanRadioTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 1)
)
if mibBuilder.loadTexts:
    wlanRadioTable.setStatus("current")
_WlanRadioEntry_Object = MibTableRow
wlanRadioEntry = _WlanRadioEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 1, 1)
)
wlanRadioEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    wlanRadioEntry.setStatus("current")


class _WlanCurrentChannel_Type(Integer32):
    """Custom type wlanCurrentChannel based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("channel1", 1),
          ("channel2", 2),
          ("channel3", 3),
          ("channel4", 4),
          ("channel5", 5),
          ("channel6", 6),
          ("channel7", 7),
          ("channel8", 8),
          ("channel9", 9),
          ("channel10", 10),
          ("channel11", 11),
          ("channel12", 12),
          ("channel13", 13))
    )


_WlanCurrentChannel_Type.__name__ = "Integer32"
_WlanCurrentChannel_Object = MibTableColumn
wlanCurrentChannel = _WlanCurrentChannel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 1, 1, 1),
    _WlanCurrentChannel_Type()
)
wlanCurrentChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanCurrentChannel.setStatus("current")


class _WlanStationCount_Type(Integer32):
    """Custom type wlanStationCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_WlanStationCount_Type.__name__ = "Integer32"
_WlanStationCount_Object = MibTableColumn
wlanStationCount = _WlanStationCount_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 1, 1, 2),
    _WlanStationCount_Type()
)
wlanStationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStationCount.setStatus("current")


class _WlanSupportedChannel_Type(DisplayString):
    """Custom type wlanSupportedChannel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlanSupportedChannel_Type.__name__ = "DisplayString"
_WlanSupportedChannel_Object = MibTableColumn
wlanSupportedChannel = _WlanSupportedChannel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 1, 1, 3),
    _WlanSupportedChannel_Type()
)
wlanSupportedChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanSupportedChannel.setStatus("current")
_WlanSupportedRate_Type = DisplayString
_WlanSupportedRate_Object = MibTableColumn
wlanSupportedRate = _WlanSupportedRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 1, 1, 4),
    _WlanSupportedRate_Type()
)
wlanSupportedRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanSupportedRate.setStatus("current")


class _WlanMode_Type(Integer32):
    """Custom type wlanMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("dot11bg", 0),
          ("dot11bgn", 8),
          ("dot11n", 9))
    )


_WlanMode_Type.__name__ = "Integer32"
_WlanMode_Object = MibTableColumn
wlanMode = _WlanMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 1, 1, 5),
    _WlanMode_Type()
)
wlanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanMode.setStatus("current")


class _WlanChannel_Type(Integer32):
    """Custom type wlanChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14),
    )


_WlanChannel_Type.__name__ = "Integer32"
_WlanChannel_Object = MibTableColumn
wlanChannel = _WlanChannel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 1, 1, 6),
    _WlanChannel_Type()
)
wlanChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanChannel.setStatus("current")


class _WlanTxPower_Type(Integer32):
    """Custom type wlanTxPower based on Integer32"""
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
        *(("full", 0),
          ("half", 1),
          ("quarter", 2),
          ("eighth", 3),
          ("min", 4))
    )


_WlanTxPower_Type.__name__ = "Integer32"
_WlanTxPower_Object = MibTableColumn
wlanTxPower = _WlanTxPower_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 1, 1, 7),
    _WlanTxPower_Type()
)
wlanTxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanTxPower.setStatus("current")


class _WlanRadioActivate_Type(Integer32):
    """Custom type wlanRadioActivate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_WlanRadioActivate_Type.__name__ = "Integer32"
_WlanRadioActivate_Object = MibTableColumn
wlanRadioActivate = _WlanRadioActivate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 1, 1, 8),
    _WlanRadioActivate_Type()
)
wlanRadioActivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanRadioActivate.setStatus("current")


class _WlanOperationMode_Type(Integer32):
    """Custom type wlanOperationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              4,
              5,
              8)
        )
    )
    namedValues = NamedValues(
        *(("modeMultiSSID", 0),
          ("modeWirelessClient", 1),
          ("modeBridge", 4),
          ("modeApRepeater", 5),
          ("modeAccessPoint", 8))
    )


_WlanOperationMode_Type.__name__ = "Integer32"
_WlanOperationMode_Object = MibTableColumn
wlanOperationMode = _WlanOperationMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 1, 1, 9),
    _WlanOperationMode_Type()
)
wlanOperationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanOperationMode.setStatus("current")


class _WlanChannelWidth_Type(Integer32):
    """Custom type wlanChannelWidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("twoPointFourGHz", 1),
          ("fiveGHz", 2))
    )


_WlanChannelWidth_Type.__name__ = "Integer32"
_WlanChannelWidth_Object = MibTableColumn
wlanChannelWidth = _WlanChannelWidth_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 1, 1, 11),
    _WlanChannelWidth_Type()
)
wlanChannelWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanChannelWidth.setStatus("current")


class _WlanAPSSIDProfileIndex_Type(Integer32):
    """Custom type wlanAPSSIDProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_WlanAPSSIDProfileIndex_Type.__name__ = "Integer32"
_WlanAPSSIDProfileIndex_Object = MibTableColumn
wlanAPSSIDProfileIndex = _WlanAPSSIDProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 1, 1, 19),
    _WlanAPSSIDProfileIndex_Type()
)
wlanAPSSIDProfileIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanAPSSIDProfileIndex.setStatus("current")
_WlanStationTable_Object = MibTable
wlanStationTable = _WlanStationTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 2)
)
if mibBuilder.loadTexts:
    wlanStationTable.setStatus("current")
_WlanStationEntry_Object = MibTableRow
wlanStationEntry = _WlanStationEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 2, 1)
)
wlanStationEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    wlanStationEntry.setStatus("current")


class _StationIndex_Type(Integer32):
    """Custom type stationIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_StationIndex_Type.__name__ = "Integer32"
_StationIndex_Object = MibTableColumn
stationIndex = _StationIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 2, 1, 1),
    _StationIndex_Type()
)
stationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stationIndex.setStatus("current")
_StationMacAddress_Type = MacAddress
_StationMacAddress_Object = MibTableColumn
stationMacAddress = _StationMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 2, 1, 2),
    _StationMacAddress_Type()
)
stationMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stationMacAddress.setStatus("current")
_StationAssociatedTime_Type = DisplayString
_StationAssociatedTime_Object = MibTableColumn
stationAssociatedTime = _StationAssociatedTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 2, 1, 3),
    _StationAssociatedTime_Type()
)
stationAssociatedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stationAssociatedTime.setStatus("current")
_StationSSID_Type = DisplayString
_StationSSID_Object = MibTableColumn
stationSSID = _StationSSID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 2, 1, 4),
    _StationSSID_Type()
)
stationSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stationSSID.setStatus("current")
_StationSignalRSSI_Type = Integer32
_StationSignalRSSI_Object = MibTableColumn
stationSignalRSSI = _StationSignalRSSI_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 2, 1, 5),
    _StationSignalRSSI_Type()
)
stationSignalRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stationSignalRSSI.setStatus("current")
_StationIPAddr_Type = IpAddress
_StationIPAddr_Object = MibTableColumn
stationIPAddr = _StationIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 2, 1, 6),
    _StationIPAddr_Type()
)
stationIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stationIPAddr.setStatus("current")
_StationCurrentDataRate_Type = DisplayString
_StationCurrentDataRate_Object = MibTableColumn
stationCurrentDataRate = _StationCurrentDataRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 2, 1, 7),
    _StationCurrentDataRate_Type()
)
stationCurrentDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stationCurrentDataRate.setStatus("current")
_StationInOctet_Type = Integer32
_StationInOctet_Object = MibTableColumn
stationInOctet = _StationInOctet_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 2, 1, 8),
    _StationInOctet_Type()
)
stationInOctet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stationInOctet.setStatus("current")
_StationOutOctet_Type = Integer32
_StationOutOctet_Object = MibTableColumn
stationOutOctet = _StationOutOctet_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 2, 1, 9),
    _StationOutOctet_Type()
)
stationOutOctet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stationOutOctet.setStatus("current")
_StationTxPkt_Type = Integer32
_StationTxPkt_Object = MibTableColumn
stationTxPkt = _StationTxPkt_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 2, 1, 10),
    _StationTxPkt_Type()
)
stationTxPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stationTxPkt.setStatus("current")
_StationRxPkt_Type = Integer32
_StationRxPkt_Object = MibTableColumn
stationRxPkt = _StationRxPkt_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 2, 1, 11),
    _StationRxPkt_Type()
)
stationRxPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stationRxPkt.setStatus("current")
_WlanStatisticTable_Object = MibTable
wlanStatisticTable = _WlanStatisticTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 3)
)
if mibBuilder.loadTexts:
    wlanStatisticTable.setStatus("current")
_WlanStatisticEntry_Object = MibTableRow
wlanStatisticEntry = _WlanStatisticEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 3, 1)
)
wlanStatisticEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    wlanStatisticEntry.setStatus("current")
_Dot11FailedCount_Type = Counter64
_Dot11FailedCount_Object = MibTableColumn
dot11FailedCount = _Dot11FailedCount_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 3, 1, 1),
    _Dot11FailedCount_Type()
)
dot11FailedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11FailedCount.setStatus("current")
_Dot11RetryCount_Type = Counter64
_Dot11RetryCount_Object = MibTableColumn
dot11RetryCount = _Dot11RetryCount_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 3, 1, 2),
    _Dot11RetryCount_Type()
)
dot11RetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11RetryCount.setStatus("current")
_Dot11ACKFailureCount_Type = Counter64
_Dot11ACKFailureCount_Object = MibTableColumn
dot11ACKFailureCount = _Dot11ACKFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 3, 1, 3),
    _Dot11ACKFailureCount_Type()
)
dot11ACKFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ACKFailureCount.setStatus("current")
_Dot11ReceivedFragmentCount_Type = Counter64
_Dot11ReceivedFragmentCount_Object = MibTableColumn
dot11ReceivedFragmentCount = _Dot11ReceivedFragmentCount_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 3, 1, 4),
    _Dot11ReceivedFragmentCount_Type()
)
dot11ReceivedFragmentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ReceivedFragmentCount.setStatus("current")
_Dot11TransmittedFrameCount_Type = Counter64
_Dot11TransmittedFrameCount_Object = MibTableColumn
dot11TransmittedFrameCount = _Dot11TransmittedFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 3, 1, 5),
    _Dot11TransmittedFrameCount_Type()
)
dot11TransmittedFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11TransmittedFrameCount.setStatus("current")
_Dot11ReceivedPktCount_Type = Counter64
_Dot11ReceivedPktCount_Object = MibTableColumn
dot11ReceivedPktCount = _Dot11ReceivedPktCount_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 3, 1, 6),
    _Dot11ReceivedPktCount_Type()
)
dot11ReceivedPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ReceivedPktCount.setStatus("current")
_Dot11TransmittedPktCount_Type = Counter64
_Dot11TransmittedPktCount_Object = MibTableColumn
dot11TransmittedPktCount = _Dot11TransmittedPktCount_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 3, 1, 7),
    _Dot11TransmittedPktCount_Type()
)
dot11TransmittedPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11TransmittedPktCount.setStatus("current")
_WlanTraps_ObjectIdentity = ObjectIdentity
wlanTraps = _WlanTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 4)
)
_WlanTrapsControl_ObjectIdentity = ObjectIdentity
wlanTrapsControl = _WlanTrapsControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 4, 1)
)


class _TrapWirelessControl_Type(Integer32):
    """Custom type trapWirelessControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_TrapWirelessControl_Type.__name__ = "Integer32"
_TrapWirelessControl_Object = MibScalar
trapWirelessControl = _TrapWirelessControl_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 4, 1, 1),
    _TrapWirelessControl_Type()
)
trapWirelessControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapWirelessControl.setStatus("current")
_WlanChannelUsageTable_Object = MibTable
wlanChannelUsageTable = _WlanChannelUsageTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 5)
)
if mibBuilder.loadTexts:
    wlanChannelUsageTable.setStatus("current")
_WlanChannelUsageEntry_Object = MibTableRow
wlanChannelUsageEntry = _WlanChannelUsageEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 5, 1)
)
wlanChannelUsageEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    wlanChannelUsageEntry.setStatus("current")
_WlanAPIndex_Type = Integer32
_WlanAPIndex_Object = MibTableColumn
wlanAPIndex = _WlanAPIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 5, 1, 1),
    _WlanAPIndex_Type()
)
wlanAPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPIndex.setStatus("current")
_WlanAPSSID_Type = DisplayString
_WlanAPSSID_Object = MibTableColumn
wlanAPSSID = _WlanAPSSID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 5, 1, 2),
    _WlanAPSSID_Type()
)
wlanAPSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPSSID.setStatus("current")
_WlanAPChannel_Type = Integer32
_WlanAPChannel_Object = MibTableColumn
wlanAPChannel = _WlanAPChannel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 5, 1, 3),
    _WlanAPChannel_Type()
)
wlanAPChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPChannel.setStatus("current")
_WlanAPMacAddress_Type = MacAddress
_WlanAPMacAddress_Object = MibTableColumn
wlanAPMacAddress = _WlanAPMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 5, 1, 4),
    _WlanAPMacAddress_Type()
)
wlanAPMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPMacAddress.setStatus("current")


class _WlanAPRadioMode_Type(Integer32):
    """Custom type wlanAPRadioMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              8)
        )
    )
    namedValues = NamedValues(
        *(("dot11bg", 0),
          ("dot11bgn", 8))
    )


_WlanAPRadioMode_Type.__name__ = "Integer32"
_WlanAPRadioMode_Object = MibTableColumn
wlanAPRadioMode = _WlanAPRadioMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 5, 1, 5),
    _WlanAPRadioMode_Type()
)
wlanAPRadioMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPRadioMode.setStatus("current")
_WlanAPSignal_Type = Integer32
_WlanAPSignal_Object = MibTableColumn
wlanAPSignal = _WlanAPSignal_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 5, 1, 6),
    _WlanAPSignal_Type()
)
wlanAPSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPSignal.setStatus("current")
_WlanAPSecurity_Type = DisplayString
_WlanAPSecurity_Object = MibTableColumn
wlanAPSecurity = _WlanAPSecurity_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 5, 1, 7),
    _WlanAPSecurity_Type()
)
wlanAPSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPSecurity.setStatus("current")
_WlanMultiVAPTable_Object = MibTable
wlanMultiVAPTable = _WlanMultiVAPTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 6)
)
if mibBuilder.loadTexts:
    wlanMultiVAPTable.setStatus("current")
_WlanVAPEntry_Object = MibTableRow
wlanVAPEntry = _WlanVAPEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 6, 1)
)
wlanVAPEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    wlanVAPEntry.setStatus("current")


class _WlanVAPActivate_Type(Integer32):
    """Custom type wlanVAPActivate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_WlanVAPActivate_Type.__name__ = "Integer32"
_WlanVAPActivate_Object = MibTableColumn
wlanVAPActivate = _WlanVAPActivate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 6, 1, 1),
    _WlanVAPActivate_Type()
)
wlanVAPActivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanVAPActivate.setStatus("current")


class _WlanVAPSSIDProfileIndex_Type(Integer32):
    """Custom type wlanVAPSSIDProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_WlanVAPSSIDProfileIndex_Type.__name__ = "Integer32"
_WlanVAPSSIDProfileIndex_Object = MibTableColumn
wlanVAPSSIDProfileIndex = _WlanVAPSSIDProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 6, 1, 2),
    _WlanVAPSSIDProfileIndex_Type()
)
wlanVAPSSIDProfileIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanVAPSSIDProfileIndex.setStatus("current")


class _WlanVAPVLANTag_Type(Integer32):
    """Custom type wlanVAPVLANTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_WlanVAPVLANTag_Type.__name__ = "Integer32"
_WlanVAPVLANTag_Object = MibTableColumn
wlanVAPVLANTag = _WlanVAPVLANTag_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 6, 1, 3),
    _WlanVAPVLANTag_Type()
)
wlanVAPVLANTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanVAPVLANTag.setStatus("current")


class _WlanVAPVLANID_Type(Integer32):
    """Custom type wlanVAPVLANID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_WlanVAPVLANID_Type.__name__ = "Integer32"
_WlanVAPVLANID_Object = MibTableColumn
wlanVAPVLANID = _WlanVAPVLANID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 6, 1, 4),
    _WlanVAPVLANID_Type()
)
wlanVAPVLANID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanVAPVLANID.setStatus("current")


class _WlanVAPVLANQoS_Type(Integer32):
    """Custom type wlanVAPVLANQoS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_WlanVAPVLANQoS_Type.__name__ = "Integer32"
_WlanVAPVLANQoS_Object = MibTableColumn
wlanVAPVLANQoS = _WlanVAPVLANQoS_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 6, 1, 5),
    _WlanVAPVLANQoS_Type()
)
wlanVAPVLANQoS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanVAPVLANQoS.setStatus("current")
_WlanMSSIDProfileControlTable_Object = MibTable
wlanMSSIDProfileControlTable = _WlanMSSIDProfileControlTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 7)
)
if mibBuilder.loadTexts:
    wlanMSSIDProfileControlTable.setStatus("current")
_WlanMSSIDProfileControlEntry_Object = MibTableRow
wlanMSSIDProfileControlEntry = _WlanMSSIDProfileControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 7, 1)
)
wlanMSSIDProfileControlEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    wlanMSSIDProfileControlEntry.setStatus("current")
_WlanSSIDProfileName_Type = DisplayString
_WlanSSIDProfileName_Object = MibTableColumn
wlanSSIDProfileName = _WlanSSIDProfileName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 7, 1, 1),
    _WlanSSIDProfileName_Type()
)
wlanSSIDProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanSSIDProfileName.setStatus("current")
_WlanSSID_Type = DisplayString
_WlanSSID_Object = MibTableColumn
wlanSSID = _WlanSSID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 7, 1, 2),
    _WlanSSID_Type()
)
wlanSSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanSSID.setStatus("current")


class _WlanSSIDProfileSecIndex_Type(Integer32):
    """Custom type wlanSSIDProfileSecIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_WlanSSIDProfileSecIndex_Type.__name__ = "Integer32"
_WlanSSIDProfileSecIndex_Object = MibTableColumn
wlanSSIDProfileSecIndex = _WlanSSIDProfileSecIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 7, 1, 3),
    _WlanSSIDProfileSecIndex_Type()
)
wlanSSIDProfileSecIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanSSIDProfileSecIndex.setStatus("current")


class _WlanSSIDProfileRadiusIndex_Type(Integer32):
    """Custom type wlanSSIDProfileRadiusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_WlanSSIDProfileRadiusIndex_Type.__name__ = "Integer32"
_WlanSSIDProfileRadiusIndex_Object = MibTableColumn
wlanSSIDProfileRadiusIndex = _WlanSSIDProfileRadiusIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 7, 1, 4),
    _WlanSSIDProfileRadiusIndex_Type()
)
wlanSSIDProfileRadiusIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanSSIDProfileRadiusIndex.setStatus("current")


class _WlanSSIDProfileMACFilterIndex_Type(Integer32):
    """Custom type wlanSSIDProfileMACFilterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_WlanSSIDProfileMACFilterIndex_Type.__name__ = "Integer32"
_WlanSSIDProfileMACFilterIndex_Object = MibTableColumn
wlanSSIDProfileMACFilterIndex = _WlanSSIDProfileMACFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 7, 1, 5),
    _WlanSSIDProfileMACFilterIndex_Type()
)
wlanSSIDProfileMACFilterIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanSSIDProfileMACFilterIndex.setStatus("current")


class _WlanSSIDProfileQoSIndex_Type(Integer32):
    """Custom type wlanSSIDProfileQoSIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("bestEffort", 0),
          ("backGround", 1),
          ("video", 2),
          ("voice", 3),
          ("wmm", 4),
          ("none", 255))
    )


_WlanSSIDProfileQoSIndex_Type.__name__ = "Integer32"
_WlanSSIDProfileQoSIndex_Object = MibTableColumn
wlanSSIDProfileQoSIndex = _WlanSSIDProfileQoSIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 7, 1, 6),
    _WlanSSIDProfileQoSIndex_Type()
)
wlanSSIDProfileQoSIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanSSIDProfileQoSIndex.setStatus("current")


class _WlanSSIDProfileAllowSTACount_Type(Integer32):
    """Custom type wlanSSIDProfileAllowSTACount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_WlanSSIDProfileAllowSTACount_Type.__name__ = "Integer32"
_WlanSSIDProfileAllowSTACount_Object = MibTableColumn
wlanSSIDProfileAllowSTACount = _WlanSSIDProfileAllowSTACount_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 7, 1, 7),
    _WlanSSIDProfileAllowSTACount_Type()
)
wlanSSIDProfileAllowSTACount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanSSIDProfileAllowSTACount.setStatus("current")


class _WlanSSIDProfileHiddenSSID_Type(Integer32):
    """Custom type wlanSSIDProfileHiddenSSID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("broadcast", 0),
          ("hidden", 1))
    )


_WlanSSIDProfileHiddenSSID_Type.__name__ = "Integer32"
_WlanSSIDProfileHiddenSSID_Object = MibTableColumn
wlanSSIDProfileHiddenSSID = _WlanSSIDProfileHiddenSSID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 7, 1, 8),
    _WlanSSIDProfileHiddenSSID_Type()
)
wlanSSIDProfileHiddenSSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanSSIDProfileHiddenSSID.setStatus("current")


class _WlanSSIDProfileIntraBSSBlock_Type(Integer32):
    """Custom type wlanSSIDProfileIntraBSSBlock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_WlanSSIDProfileIntraBSSBlock_Type.__name__ = "Integer32"
_WlanSSIDProfileIntraBSSBlock_Object = MibTableColumn
wlanSSIDProfileIntraBSSBlock = _WlanSSIDProfileIntraBSSBlock_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 7, 1, 9),
    _WlanSSIDProfileIntraBSSBlock_Type()
)
wlanSSIDProfileIntraBSSBlock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanSSIDProfileIntraBSSBlock.setStatus("current")
_WlanSecurityProfileControlTable_Object = MibTable
wlanSecurityProfileControlTable = _WlanSecurityProfileControlTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 8)
)
if mibBuilder.loadTexts:
    wlanSecurityProfileControlTable.setStatus("current")
_WlanSecurityProfileControlEntry_Object = MibTableRow
wlanSecurityProfileControlEntry = _WlanSecurityProfileControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 8, 1)
)
wlanSecurityProfileControlEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    wlanSecurityProfileControlEntry.setStatus("current")


class _WlanSecMode_Type(Integer32):
    """Custom type wlanSecMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              8,
              12,
              16,
              32,
              48)
        )
    )
    namedValues = NamedValues(
        *(("modeOpenSystem", 0),
          ("modeSharedKey", 1),
          ("mode8021x", 2),
          ("modeWpaWith8021x", 4),
          ("modeWpa2With8021x", 8),
          ("modeWpaWpa2With8021x", 12),
          ("modeWpaPsk", 16),
          ("modeWpa2Psk", 32),
          ("modeWpaWpa2Psk", 48))
    )


_WlanSecMode_Type.__name__ = "Integer32"
_WlanSecMode_Object = MibTableColumn
wlanSecMode = _WlanSecMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 8, 1, 1),
    _WlanSecMode_Type()
)
wlanSecMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanSecMode.setStatus("current")


class _WlanWPAGroupKeyRekey_Type(Integer32):
    """Custom type wlanWPAGroupKeyRekey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 3600),
    )


_WlanWPAGroupKeyRekey_Type.__name__ = "Integer32"
_WlanWPAGroupKeyRekey_Object = MibTableColumn
wlanWPAGroupKeyRekey = _WlanWPAGroupKeyRekey_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 8, 1, 2),
    _WlanWPAGroupKeyRekey_Type()
)
wlanWPAGroupKeyRekey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanWPAGroupKeyRekey.setStatus("current")
_WlanWPAPreSharedKey_Type = DisplayString
_WlanWPAPreSharedKey_Object = MibTableColumn
wlanWPAPreSharedKey = _WlanWPAPreSharedKey_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 8, 1, 3),
    _WlanWPAPreSharedKey_Type()
)
wlanWPAPreSharedKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanWPAPreSharedKey.setStatus("current")


class _WlanWEPEncryption_Type(Integer32):
    """Custom type wlanWEPEncryption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              40,
              104,
              128,
              250)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("mode64hex", 40),
          ("mode128hex", 104),
          ("mode152hex", 128),
          ("dynamic", 250))
    )


_WlanWEPEncryption_Type.__name__ = "Integer32"
_WlanWEPEncryption_Object = MibTableColumn
wlanWEPEncryption = _WlanWEPEncryption_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 8, 1, 4),
    _WlanWEPEncryption_Type()
)
wlanWEPEncryption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanWEPEncryption.setStatus("current")


class _WlanWEPKeyIndex_Type(Integer32):
    """Custom type wlanWEPKeyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("key1", 1),
          ("key2", 2),
          ("key3", 3),
          ("key4", 4))
    )


_WlanWEPKeyIndex_Type.__name__ = "Integer32"
_WlanWEPKeyIndex_Object = MibTableColumn
wlanWEPKeyIndex = _WlanWEPKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 8, 1, 6),
    _WlanWEPKeyIndex_Type()
)
wlanWEPKeyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanWEPKeyIndex.setStatus("current")
_WlanWEPKey1_Type = DisplayString
_WlanWEPKey1_Object = MibTableColumn
wlanWEPKey1 = _WlanWEPKey1_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 8, 1, 7),
    _WlanWEPKey1_Type()
)
wlanWEPKey1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanWEPKey1.setStatus("current")
_WlanWEPKey2_Type = DisplayString
_WlanWEPKey2_Object = MibTableColumn
wlanWEPKey2 = _WlanWEPKey2_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 8, 1, 8),
    _WlanWEPKey2_Type()
)
wlanWEPKey2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanWEPKey2.setStatus("current")
_WlanWEPKey3_Type = DisplayString
_WlanWEPKey3_Object = MibTableColumn
wlanWEPKey3 = _WlanWEPKey3_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 8, 1, 9),
    _WlanWEPKey3_Type()
)
wlanWEPKey3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanWEPKey3.setStatus("current")
_WlanWEPKey4_Type = DisplayString
_WlanWEPKey4_Object = MibTableColumn
wlanWEPKey4 = _WlanWEPKey4_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 8, 1, 10),
    _WlanWEPKey4_Type()
)
wlanWEPKey4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanWEPKey4.setStatus("current")


class _WlanWEPAuthMethod_Type(Integer32):
    """Custom type wlanWEPAuthMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(13,
              17,
              21,
              25)
        )
    )
    namedValues = NamedValues(
        *(("tls", 13),
          ("leap", 17),
          ("ttls", 21),
          ("peap", 25))
    )


_WlanWEPAuthMethod_Type.__name__ = "Integer32"
_WlanWEPAuthMethod_Object = MibTableColumn
wlanWEPAuthMethod = _WlanWEPAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 8, 1, 11),
    _WlanWEPAuthMethod_Type()
)
wlanWEPAuthMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanWEPAuthMethod.setStatus("current")
_WlanSecProfileName_Type = DisplayString
_WlanSecProfileName_Object = MibTableColumn
wlanSecProfileName = _WlanSecProfileName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 8, 1, 12),
    _WlanSecProfileName_Type()
)
wlanSecProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanSecProfileName.setStatus("current")


class _Wlan8021xReauthTime_Type(Integer32):
    """Custom type wlan8021xReauthTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 3600),
    )


_Wlan8021xReauthTime_Type.__name__ = "Integer32"
_Wlan8021xReauthTime_Object = MibTableColumn
wlan8021xReauthTime = _Wlan8021xReauthTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 8, 1, 13),
    _Wlan8021xReauthTime_Type()
)
wlan8021xReauthTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan8021xReauthTime.setStatus("current")


class _Wlan8021xGroupKeyRekeyControl_Type(Integer32):
    """Custom type wlan8021xGroupKeyRekeyControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_Wlan8021xGroupKeyRekeyControl_Type.__name__ = "Integer32"
_Wlan8021xGroupKeyRekeyControl_Object = MibTableColumn
wlan8021xGroupKeyRekeyControl = _Wlan8021xGroupKeyRekeyControl_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 8, 1, 14),
    _Wlan8021xGroupKeyRekeyControl_Type()
)
wlan8021xGroupKeyRekeyControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan8021xGroupKeyRekeyControl.setStatus("current")
_WlanRadiusProfileControlTable_Object = MibTable
wlanRadiusProfileControlTable = _WlanRadiusProfileControlTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 9)
)
if mibBuilder.loadTexts:
    wlanRadiusProfileControlTable.setStatus("current")
_WlanRadiusProfileControlEntry_Object = MibTableRow
wlanRadiusProfileControlEntry = _WlanRadiusProfileControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 9, 1)
)
wlanRadiusProfileControlEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    wlanRadiusProfileControlEntry.setStatus("current")
_WlanRadiusProfileName_Type = DisplayString
_WlanRadiusProfileName_Object = MibTableColumn
wlanRadiusProfileName = _WlanRadiusProfileName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 9, 1, 1),
    _WlanRadiusProfileName_Type()
)
wlanRadiusProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanRadiusProfileName.setStatus("current")
_WlanRadiusNASIdentifier_Type = DisplayString
_WlanRadiusNASIdentifier_Object = MibTableColumn
wlanRadiusNASIdentifier = _WlanRadiusNASIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 9, 1, 2),
    _WlanRadiusNASIdentifier_Type()
)
wlanRadiusNASIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanRadiusNASIdentifier.setStatus("current")


class _WlanRadiusPrimaryAcitvate_Type(Integer32):
    """Custom type wlanRadiusPrimaryAcitvate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_WlanRadiusPrimaryAcitvate_Type.__name__ = "Integer32"
_WlanRadiusPrimaryAcitvate_Object = MibTableColumn
wlanRadiusPrimaryAcitvate = _WlanRadiusPrimaryAcitvate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 9, 1, 3),
    _WlanRadiusPrimaryAcitvate_Type()
)
wlanRadiusPrimaryAcitvate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanRadiusPrimaryAcitvate.setStatus("current")
_WlanRadiusPriSrvIPAddr_Type = IpAddress
_WlanRadiusPriSrvIPAddr_Object = MibTableColumn
wlanRadiusPriSrvIPAddr = _WlanRadiusPriSrvIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 9, 1, 4),
    _WlanRadiusPriSrvIPAddr_Type()
)
wlanRadiusPriSrvIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanRadiusPriSrvIPAddr.setStatus("current")
_WlanRadiusPriSrvPort_Type = Integer32
_WlanRadiusPriSrvPort_Object = MibTableColumn
wlanRadiusPriSrvPort = _WlanRadiusPriSrvPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 9, 1, 5),
    _WlanRadiusPriSrvPort_Type()
)
wlanRadiusPriSrvPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanRadiusPriSrvPort.setStatus("current")
_WlanRadiusPriShareSecret_Type = DisplayString
_WlanRadiusPriShareSecret_Object = MibTableColumn
wlanRadiusPriShareSecret = _WlanRadiusPriShareSecret_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 9, 1, 6),
    _WlanRadiusPriShareSecret_Type()
)
wlanRadiusPriShareSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanRadiusPriShareSecret.setStatus("current")


class _WlanRadiusPriACCAcitvate_Type(Integer32):
    """Custom type wlanRadiusPriACCAcitvate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_WlanRadiusPriACCAcitvate_Type.__name__ = "Integer32"
_WlanRadiusPriACCAcitvate_Object = MibTableColumn
wlanRadiusPriACCAcitvate = _WlanRadiusPriACCAcitvate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 9, 1, 7),
    _WlanRadiusPriACCAcitvate_Type()
)
wlanRadiusPriACCAcitvate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanRadiusPriACCAcitvate.setStatus("current")
_WlanRadiusPriACCSrvIPAddr_Type = IpAddress
_WlanRadiusPriACCSrvIPAddr_Object = MibTableColumn
wlanRadiusPriACCSrvIPAddr = _WlanRadiusPriACCSrvIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 9, 1, 8),
    _WlanRadiusPriACCSrvIPAddr_Type()
)
wlanRadiusPriACCSrvIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanRadiusPriACCSrvIPAddr.setStatus("current")
_WlanRadiusPriACCSrvPort_Type = Integer32
_WlanRadiusPriACCSrvPort_Object = MibTableColumn
wlanRadiusPriACCSrvPort = _WlanRadiusPriACCSrvPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 9, 1, 9),
    _WlanRadiusPriACCSrvPort_Type()
)
wlanRadiusPriACCSrvPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanRadiusPriACCSrvPort.setStatus("current")
_WlanRadiusPriACCShareSecret_Type = DisplayString
_WlanRadiusPriACCShareSecret_Object = MibTableColumn
wlanRadiusPriACCShareSecret = _WlanRadiusPriACCShareSecret_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 9, 1, 10),
    _WlanRadiusPriACCShareSecret_Type()
)
wlanRadiusPriACCShareSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanRadiusPriACCShareSecret.setStatus("current")


class _WlanRadiusBUAcitvate_Type(Integer32):
    """Custom type wlanRadiusBUAcitvate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_WlanRadiusBUAcitvate_Type.__name__ = "Integer32"
_WlanRadiusBUAcitvate_Object = MibTableColumn
wlanRadiusBUAcitvate = _WlanRadiusBUAcitvate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 9, 1, 11),
    _WlanRadiusBUAcitvate_Type()
)
wlanRadiusBUAcitvate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanRadiusBUAcitvate.setStatus("current")
_WlanRadiusBUSrvIPAddr_Type = IpAddress
_WlanRadiusBUSrvIPAddr_Object = MibTableColumn
wlanRadiusBUSrvIPAddr = _WlanRadiusBUSrvIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 9, 1, 12),
    _WlanRadiusBUSrvIPAddr_Type()
)
wlanRadiusBUSrvIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanRadiusBUSrvIPAddr.setStatus("current")
_WlanRadiusBUSrvPort_Type = Integer32
_WlanRadiusBUSrvPort_Object = MibTableColumn
wlanRadiusBUSrvPort = _WlanRadiusBUSrvPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 9, 1, 13),
    _WlanRadiusBUSrvPort_Type()
)
wlanRadiusBUSrvPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanRadiusBUSrvPort.setStatus("current")
_WlanRadiusBUShareSecret_Type = DisplayString
_WlanRadiusBUShareSecret_Object = MibTableColumn
wlanRadiusBUShareSecret = _WlanRadiusBUShareSecret_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 9, 1, 14),
    _WlanRadiusBUShareSecret_Type()
)
wlanRadiusBUShareSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanRadiusBUShareSecret.setStatus("current")


class _WlanRadiusBUACCAcitvate_Type(Integer32):
    """Custom type wlanRadiusBUACCAcitvate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_WlanRadiusBUACCAcitvate_Type.__name__ = "Integer32"
_WlanRadiusBUACCAcitvate_Object = MibTableColumn
wlanRadiusBUACCAcitvate = _WlanRadiusBUACCAcitvate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 9, 1, 15),
    _WlanRadiusBUACCAcitvate_Type()
)
wlanRadiusBUACCAcitvate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanRadiusBUACCAcitvate.setStatus("current")
_WlanRadiusBUACCSrvIPAddr_Type = IpAddress
_WlanRadiusBUACCSrvIPAddr_Object = MibTableColumn
wlanRadiusBUACCSrvIPAddr = _WlanRadiusBUACCSrvIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 9, 1, 16),
    _WlanRadiusBUACCSrvIPAddr_Type()
)
wlanRadiusBUACCSrvIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanRadiusBUACCSrvIPAddr.setStatus("current")
_WlanRadiusBUACCSrvPort_Type = Integer32
_WlanRadiusBUACCSrvPort_Object = MibTableColumn
wlanRadiusBUACCSrvPort = _WlanRadiusBUACCSrvPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 9, 1, 17),
    _WlanRadiusBUACCSrvPort_Type()
)
wlanRadiusBUACCSrvPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanRadiusBUACCSrvPort.setStatus("current")
_WlanRadiusBUACCShareSecret_Type = DisplayString
_WlanRadiusBUACCShareSecret_Object = MibTableColumn
wlanRadiusBUACCShareSecret = _WlanRadiusBUACCShareSecret_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 9, 1, 18),
    _WlanRadiusBUACCShareSecret_Type()
)
wlanRadiusBUACCShareSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanRadiusBUACCShareSecret.setStatus("current")
_WlanMACFilterProfileControlTable_Object = MibTable
wlanMACFilterProfileControlTable = _WlanMACFilterProfileControlTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 10)
)
if mibBuilder.loadTexts:
    wlanMACFilterProfileControlTable.setStatus("current")
_WlanMACFilterProfileControlEntry_Object = MibTableRow
wlanMACFilterProfileControlEntry = _WlanMACFilterProfileControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 10, 1)
)
wlanMACFilterProfileControlEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    wlanMACFilterProfileControlEntry.setStatus("current")
_WlanMACFilterProfileName_Type = DisplayString
_WlanMACFilterProfileName_Object = MibTableColumn
wlanMACFilterProfileName = _WlanMACFilterProfileName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 10, 1, 1),
    _WlanMACFilterProfileName_Type()
)
wlanMACFilterProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanMACFilterProfileName.setStatus("current")


class _WlanMACFilterACLMode_Type(Integer32):
    """Custom type wlanMACFilterACLMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("allow", 1),
          ("deny", 2))
    )


_WlanMACFilterACLMode_Type.__name__ = "Integer32"
_WlanMACFilterACLMode_Object = MibTableColumn
wlanMACFilterACLMode = _WlanMACFilterACLMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 5, 10, 1, 2),
    _WlanMACFilterACLMode_Type()
)
wlanMACFilterACLMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanMACFilterACLMode.setStatus("current")
_EsProductSpecific_ObjectIdentity = ObjectIdentity
esProductSpecific = _EsProductSpecific_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 4)
)
_EsProWLAN_ObjectIdentity = ObjectIdentity
esProWLAN = _EsProWLAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 4, 1)
)
_SysMgmt_ObjectIdentity = ObjectIdentity
sysMgmt = _SysMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 4, 1, 1)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NWA1123-NI",
    **{"zyxel": zyxel,
       "nwaSeries": nwaSeries,
       "nwa1123ni": nwa1123ni,
       "esMgmt": esMgmt,
       "esSysInfo": esSysInfo,
       "sysSwPlatform": sysSwPlatform,
       "sysSwMajorVersion": sysSwMajorVersion,
       "sysSwMinorVersion": sysSwMinorVersion,
       "sysSwModel": sysSwModel,
       "sysSwPatchNumber": sysSwPatchNumber,
       "sysSwVersionString": sysSwVersionString,
       "sysSwDay": sysSwDay,
       "sysSwMonth": sysSwMonth,
       "sysSwYear": sysSwYear,
       "sysProductFamily": sysProductFamily,
       "sysProductModel": sysProductModel,
       "sysProductSerialNumber": sysProductSerialNumber,
       "sysHwMajorVersion": sysHwMajorVersion,
       "sysHwMinorVersion": sysHwMinorVersion,
       "sysHwVersionString": sysHwVersionString,
       "sysCountryCode": sysCountryCode,
       "sysCurrentDateTime": sysCurrentDateTime,
       "sysCurrentTime": sysCurrentTime,
       "esSysMgmt": esSysMgmt,
       "sysMgmtReboot": sysMgmtReboot,
       "sysMgmtConfigSave": sysMgmtConfigSave,
       "sysMgmtRestoreDefaultConfig": sysMgmtRestoreDefaultConfig,
       "sysMgmtCPUUsage": sysMgmtCPUUsage,
       "sysMgmtMemUsage": sysMgmtMemUsage,
       "sysMgmtFlashUsage": sysMgmtFlashUsage,
       "sysMgmtVLANControl": sysMgmtVLANControl,
       "sysMgmtVLANID": sysMgmtVLANID,
       "sys8021QControl": sys8021QControl,
       "devGatewayIPAddr": devGatewayIPAddr,
       "adminPassword": adminPassword,
       "esWireless": esWireless,
       "wlanRadioTable": wlanRadioTable,
       "wlanRadioEntry": wlanRadioEntry,
       "wlanCurrentChannel": wlanCurrentChannel,
       "wlanStationCount": wlanStationCount,
       "wlanSupportedChannel": wlanSupportedChannel,
       "wlanSupportedRate": wlanSupportedRate,
       "wlanMode": wlanMode,
       "wlanChannel": wlanChannel,
       "wlanTxPower": wlanTxPower,
       "wlanRadioActivate": wlanRadioActivate,
       "wlanOperationMode": wlanOperationMode,
       "wlanChannelWidth": wlanChannelWidth,
       "wlanAPSSIDProfileIndex": wlanAPSSIDProfileIndex,
       "wlanStationTable": wlanStationTable,
       "wlanStationEntry": wlanStationEntry,
       "stationIndex": stationIndex,
       "stationMacAddress": stationMacAddress,
       "stationAssociatedTime": stationAssociatedTime,
       "stationSSID": stationSSID,
       "stationSignalRSSI": stationSignalRSSI,
       "stationIPAddr": stationIPAddr,
       "stationCurrentDataRate": stationCurrentDataRate,
       "stationInOctet": stationInOctet,
       "stationOutOctet": stationOutOctet,
       "stationTxPkt": stationTxPkt,
       "stationRxPkt": stationRxPkt,
       "wlanStatisticTable": wlanStatisticTable,
       "wlanStatisticEntry": wlanStatisticEntry,
       "dot11FailedCount": dot11FailedCount,
       "dot11RetryCount": dot11RetryCount,
       "dot11ACKFailureCount": dot11ACKFailureCount,
       "dot11ReceivedFragmentCount": dot11ReceivedFragmentCount,
       "dot11TransmittedFrameCount": dot11TransmittedFrameCount,
       "dot11ReceivedPktCount": dot11ReceivedPktCount,
       "dot11TransmittedPktCount": dot11TransmittedPktCount,
       "wlanTraps": wlanTraps,
       "wlanTrapsControl": wlanTrapsControl,
       "trapWirelessControl": trapWirelessControl,
       "wlanChannelUsageTable": wlanChannelUsageTable,
       "wlanChannelUsageEntry": wlanChannelUsageEntry,
       "wlanAPIndex": wlanAPIndex,
       "wlanAPSSID": wlanAPSSID,
       "wlanAPChannel": wlanAPChannel,
       "wlanAPMacAddress": wlanAPMacAddress,
       "wlanAPRadioMode": wlanAPRadioMode,
       "wlanAPSignal": wlanAPSignal,
       "wlanAPSecurity": wlanAPSecurity,
       "wlanMultiVAPTable": wlanMultiVAPTable,
       "wlanVAPEntry": wlanVAPEntry,
       "wlanVAPActivate": wlanVAPActivate,
       "wlanVAPSSIDProfileIndex": wlanVAPSSIDProfileIndex,
       "wlanVAPVLANTag": wlanVAPVLANTag,
       "wlanVAPVLANID": wlanVAPVLANID,
       "wlanVAPVLANQoS": wlanVAPVLANQoS,
       "wlanMSSIDProfileControlTable": wlanMSSIDProfileControlTable,
       "wlanMSSIDProfileControlEntry": wlanMSSIDProfileControlEntry,
       "wlanSSIDProfileName": wlanSSIDProfileName,
       "wlanSSID": wlanSSID,
       "wlanSSIDProfileSecIndex": wlanSSIDProfileSecIndex,
       "wlanSSIDProfileRadiusIndex": wlanSSIDProfileRadiusIndex,
       "wlanSSIDProfileMACFilterIndex": wlanSSIDProfileMACFilterIndex,
       "wlanSSIDProfileQoSIndex": wlanSSIDProfileQoSIndex,
       "wlanSSIDProfileAllowSTACount": wlanSSIDProfileAllowSTACount,
       "wlanSSIDProfileHiddenSSID": wlanSSIDProfileHiddenSSID,
       "wlanSSIDProfileIntraBSSBlock": wlanSSIDProfileIntraBSSBlock,
       "wlanSecurityProfileControlTable": wlanSecurityProfileControlTable,
       "wlanSecurityProfileControlEntry": wlanSecurityProfileControlEntry,
       "wlanSecMode": wlanSecMode,
       "wlanWPAGroupKeyRekey": wlanWPAGroupKeyRekey,
       "wlanWPAPreSharedKey": wlanWPAPreSharedKey,
       "wlanWEPEncryption": wlanWEPEncryption,
       "wlanWEPKeyIndex": wlanWEPKeyIndex,
       "wlanWEPKey1": wlanWEPKey1,
       "wlanWEPKey2": wlanWEPKey2,
       "wlanWEPKey3": wlanWEPKey3,
       "wlanWEPKey4": wlanWEPKey4,
       "wlanWEPAuthMethod": wlanWEPAuthMethod,
       "wlanSecProfileName": wlanSecProfileName,
       "wlan8021xReauthTime": wlan8021xReauthTime,
       "wlan8021xGroupKeyRekeyControl": wlan8021xGroupKeyRekeyControl,
       "wlanRadiusProfileControlTable": wlanRadiusProfileControlTable,
       "wlanRadiusProfileControlEntry": wlanRadiusProfileControlEntry,
       "wlanRadiusProfileName": wlanRadiusProfileName,
       "wlanRadiusNASIdentifier": wlanRadiusNASIdentifier,
       "wlanRadiusPrimaryAcitvate": wlanRadiusPrimaryAcitvate,
       "wlanRadiusPriSrvIPAddr": wlanRadiusPriSrvIPAddr,
       "wlanRadiusPriSrvPort": wlanRadiusPriSrvPort,
       "wlanRadiusPriShareSecret": wlanRadiusPriShareSecret,
       "wlanRadiusPriACCAcitvate": wlanRadiusPriACCAcitvate,
       "wlanRadiusPriACCSrvIPAddr": wlanRadiusPriACCSrvIPAddr,
       "wlanRadiusPriACCSrvPort": wlanRadiusPriACCSrvPort,
       "wlanRadiusPriACCShareSecret": wlanRadiusPriACCShareSecret,
       "wlanRadiusBUAcitvate": wlanRadiusBUAcitvate,
       "wlanRadiusBUSrvIPAddr": wlanRadiusBUSrvIPAddr,
       "wlanRadiusBUSrvPort": wlanRadiusBUSrvPort,
       "wlanRadiusBUShareSecret": wlanRadiusBUShareSecret,
       "wlanRadiusBUACCAcitvate": wlanRadiusBUACCAcitvate,
       "wlanRadiusBUACCSrvIPAddr": wlanRadiusBUACCSrvIPAddr,
       "wlanRadiusBUACCSrvPort": wlanRadiusBUACCSrvPort,
       "wlanRadiusBUACCShareSecret": wlanRadiusBUACCShareSecret,
       "wlanMACFilterProfileControlTable": wlanMACFilterProfileControlTable,
       "wlanMACFilterProfileControlEntry": wlanMACFilterProfileControlEntry,
       "wlanMACFilterProfileName": wlanMACFilterProfileName,
       "wlanMACFilterACLMode": wlanMACFilterACLMode,
       "esProductSpecific": esProductSpecific,
       "esProWLAN": esProWLAN,
       "sysMgmt": sysMgmt}
)
