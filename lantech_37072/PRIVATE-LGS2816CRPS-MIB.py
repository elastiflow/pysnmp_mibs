# SNMP MIB module (PRIVATE-LGS2816CRPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/lantech_37072/PRIVATE-LGS2816CRPS-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 11:14:09 2025
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

(MacAddress,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "MacAddress")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

private = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 37072)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Switch_ObjectIdentity = ObjectIdentity
switch = _Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2)
)
_Lgs2816crpsProductID_ObjectIdentity = ObjectIdentity
lgs2816crpsProductID = _Lgs2816crpsProductID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47)
)
_Lgs2816crpsProduces_ObjectIdentity = ObjectIdentity
lgs2816crpsProduces = _Lgs2816crpsProduces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1)
)
_Lgs2816crpsSystem_ObjectIdentity = ObjectIdentity
lgs2816crpsSystem = _Lgs2816crpsSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 1)
)
_Lgs2816crpsCommonSys_ObjectIdentity = ObjectIdentity
lgs2816crpsCommonSys = _Lgs2816crpsCommonSys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 1, 1)
)


class _Lgs2816crpsReboot_Type(Integer32):
    """Custom type lgs2816crpsReboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2816crpsReboot_Type.__name__ = "Integer32"
_Lgs2816crpsReboot_Object = MibScalar
lgs2816crpsReboot = _Lgs2816crpsReboot_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 1, 1, 1),
    _Lgs2816crpsReboot_Type()
)
lgs2816crpsReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsReboot.setStatus("current")
_Lgs2816crpsBiosVsersion_Type = DisplayString
_Lgs2816crpsBiosVsersion_Object = MibScalar
lgs2816crpsBiosVsersion = _Lgs2816crpsBiosVsersion_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 1, 1, 2),
    _Lgs2816crpsBiosVsersion_Type()
)
lgs2816crpsBiosVsersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsBiosVsersion.setStatus("current")
_Lgs2816crpsFirmwareVersion_Type = DisplayString
_Lgs2816crpsFirmwareVersion_Object = MibScalar
lgs2816crpsFirmwareVersion = _Lgs2816crpsFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 1, 1, 3),
    _Lgs2816crpsFirmwareVersion_Type()
)
lgs2816crpsFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsFirmwareVersion.setStatus("current")
_Lgs2816crpsHardwareVersion_Type = DisplayString
_Lgs2816crpsHardwareVersion_Object = MibScalar
lgs2816crpsHardwareVersion = _Lgs2816crpsHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 1, 1, 4),
    _Lgs2816crpsHardwareVersion_Type()
)
lgs2816crpsHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsHardwareVersion.setStatus("current")
_Lgs2816crpsMechanicalVersion_Type = DisplayString
_Lgs2816crpsMechanicalVersion_Object = MibScalar
lgs2816crpsMechanicalVersion = _Lgs2816crpsMechanicalVersion_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 1, 1, 5),
    _Lgs2816crpsMechanicalVersion_Type()
)
lgs2816crpsMechanicalVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsMechanicalVersion.setStatus("current")
_Lgs2816crpsSerialNumber_Type = DisplayString
_Lgs2816crpsSerialNumber_Object = MibScalar
lgs2816crpsSerialNumber = _Lgs2816crpsSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 1, 1, 6),
    _Lgs2816crpsSerialNumber_Type()
)
lgs2816crpsSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsSerialNumber.setStatus("current")
_Lgs2816crpsHostMacAddress_Type = DisplayString
_Lgs2816crpsHostMacAddress_Object = MibScalar
lgs2816crpsHostMacAddress = _Lgs2816crpsHostMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 1, 1, 7),
    _Lgs2816crpsHostMacAddress_Type()
)
lgs2816crpsHostMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsHostMacAddress.setStatus("current")
_Lgs2816crpsDevicePort_Type = DisplayString
_Lgs2816crpsDevicePort_Object = MibScalar
lgs2816crpsDevicePort = _Lgs2816crpsDevicePort_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 1, 1, 8),
    _Lgs2816crpsDevicePort_Type()
)
lgs2816crpsDevicePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsDevicePort.setStatus("current")
_Lgs2816crpsRamSize_Type = DisplayString
_Lgs2816crpsRamSize_Object = MibScalar
lgs2816crpsRamSize = _Lgs2816crpsRamSize_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 1, 1, 9),
    _Lgs2816crpsRamSize_Type()
)
lgs2816crpsRamSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsRamSize.setStatus("current")
_Lgs2816crpsFlashSize_Type = DisplayString
_Lgs2816crpsFlashSize_Object = MibScalar
lgs2816crpsFlashSize = _Lgs2816crpsFlashSize_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 1, 1, 10),
    _Lgs2816crpsFlashSize_Type()
)
lgs2816crpsFlashSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsFlashSize.setStatus("current")
_Lgs2816crpsDeviceName_Type = DisplayString
_Lgs2816crpsDeviceName_Object = MibScalar
lgs2816crpsDeviceName = _Lgs2816crpsDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 1, 1, 11),
    _Lgs2816crpsDeviceName_Type()
)
lgs2816crpsDeviceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsDeviceName.setStatus("current")
_Lgs2816crpsSystemDescription_Type = DisplayString
_Lgs2816crpsSystemDescription_Object = MibScalar
lgs2816crpsSystemDescription = _Lgs2816crpsSystemDescription_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 1, 1, 12),
    _Lgs2816crpsSystemDescription_Type()
)
lgs2816crpsSystemDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsSystemDescription.setStatus("current")
_Lgs2816crpsCpuLoad_Type = DisplayString
_Lgs2816crpsCpuLoad_Object = MibScalar
lgs2816crpsCpuLoad = _Lgs2816crpsCpuLoad_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 1, 1, 13),
    _Lgs2816crpsCpuLoad_Type()
)
lgs2816crpsCpuLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsCpuLoad.setStatus("current")
_Lgs2816crpsIP_ObjectIdentity = ObjectIdentity
lgs2816crpsIP = _Lgs2816crpsIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 1, 2)
)


class _Lgs2816crpsDhcpSetting_Type(Integer32):
    """Custom type lgs2816crpsDhcpSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2816crpsDhcpSetting_Type.__name__ = "Integer32"
_Lgs2816crpsDhcpSetting_Object = MibScalar
lgs2816crpsDhcpSetting = _Lgs2816crpsDhcpSetting_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 1, 2, 1),
    _Lgs2816crpsDhcpSetting_Type()
)
lgs2816crpsDhcpSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsDhcpSetting.setStatus("current")
_Lgs2816crpsIPAddress_Type = IpAddress
_Lgs2816crpsIPAddress_Object = MibScalar
lgs2816crpsIPAddress = _Lgs2816crpsIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 1, 2, 2),
    _Lgs2816crpsIPAddress_Type()
)
lgs2816crpsIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsIPAddress.setStatus("current")
_Lgs2816crpsNetMask_Type = IpAddress
_Lgs2816crpsNetMask_Object = MibScalar
lgs2816crpsNetMask = _Lgs2816crpsNetMask_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 1, 2, 3),
    _Lgs2816crpsNetMask_Type()
)
lgs2816crpsNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsNetMask.setStatus("current")
_Lgs2816crpsDefaultGateway_Type = IpAddress
_Lgs2816crpsDefaultGateway_Object = MibScalar
lgs2816crpsDefaultGateway = _Lgs2816crpsDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 1, 2, 4),
    _Lgs2816crpsDefaultGateway_Type()
)
lgs2816crpsDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsDefaultGateway.setStatus("current")


class _Lgs2816crpsDnsConf_Type(Integer32):
    """Custom type lgs2816crpsDnsConf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2816crpsDnsConf_Type.__name__ = "Integer32"
_Lgs2816crpsDnsConf_Object = MibScalar
lgs2816crpsDnsConf = _Lgs2816crpsDnsConf_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 1, 2, 5),
    _Lgs2816crpsDnsConf_Type()
)
lgs2816crpsDnsConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsDnsConf.setStatus("current")


class _Lgs2816crpsDnsState_Type(Integer32):
    """Custom type lgs2816crpsDnsState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2816crpsDnsState_Type.__name__ = "Integer32"
_Lgs2816crpsDnsState_Object = MibScalar
lgs2816crpsDnsState = _Lgs2816crpsDnsState_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 1, 2, 6),
    _Lgs2816crpsDnsState_Type()
)
lgs2816crpsDnsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsDnsState.setStatus("current")
_Lgs2816crpsDnsServer_Type = IpAddress
_Lgs2816crpsDnsServer_Object = MibScalar
lgs2816crpsDnsServer = _Lgs2816crpsDnsServer_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 1, 2, 7),
    _Lgs2816crpsDnsServer_Type()
)
lgs2816crpsDnsServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsDnsServer.setStatus("current")
_Lgs2816crpsTime_ObjectIdentity = ObjectIdentity
lgs2816crpsTime = _Lgs2816crpsTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 1, 3)
)
_Lgs2816crpsSystemCurrentTime_Type = DisplayString
_Lgs2816crpsSystemCurrentTime_Object = MibScalar
lgs2816crpsSystemCurrentTime = _Lgs2816crpsSystemCurrentTime_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 1, 3, 1),
    _Lgs2816crpsSystemCurrentTime_Type()
)
lgs2816crpsSystemCurrentTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsSystemCurrentTime.setStatus("current")
_Lgs2816crpsManualTimeSetting_Type = DisplayString
_Lgs2816crpsManualTimeSetting_Object = MibScalar
lgs2816crpsManualTimeSetting = _Lgs2816crpsManualTimeSetting_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 1, 3, 2),
    _Lgs2816crpsManualTimeSetting_Type()
)
lgs2816crpsManualTimeSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsManualTimeSetting.setStatus("current")
_Lgs2816crpsNTPServer_Type = DisplayString
_Lgs2816crpsNTPServer_Object = MibScalar
lgs2816crpsNTPServer = _Lgs2816crpsNTPServer_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 1, 3, 3),
    _Lgs2816crpsNTPServer_Type()
)
lgs2816crpsNTPServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsNTPServer.setStatus("current")


class _Lgs2816crpsNTPTimeZone_Type(Integer32):
    """Custom type lgs2816crpsNTPTimeZone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-12, 13),
    )


_Lgs2816crpsNTPTimeZone_Type.__name__ = "Integer32"
_Lgs2816crpsNTPTimeZone_Object = MibScalar
lgs2816crpsNTPTimeZone = _Lgs2816crpsNTPTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 1, 3, 4),
    _Lgs2816crpsNTPTimeZone_Type()
)
lgs2816crpsNTPTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsNTPTimeZone.setStatus("current")


class _Lgs2816crpsNTPTimeSync_Type(Integer32):
    """Custom type lgs2816crpsNTPTimeSync based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2816crpsNTPTimeSync_Type.__name__ = "Integer32"
_Lgs2816crpsNTPTimeSync_Object = MibScalar
lgs2816crpsNTPTimeSync = _Lgs2816crpsNTPTimeSync_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 1, 3, 5),
    _Lgs2816crpsNTPTimeSync_Type()
)
lgs2816crpsNTPTimeSync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsNTPTimeSync.setStatus("current")


class _Lgs2816crpsDaylightSavingTime_Type(Integer32):
    """Custom type lgs2816crpsDaylightSavingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-5, 5),
    )


_Lgs2816crpsDaylightSavingTime_Type.__name__ = "Integer32"
_Lgs2816crpsDaylightSavingTime_Object = MibScalar
lgs2816crpsDaylightSavingTime = _Lgs2816crpsDaylightSavingTime_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 1, 3, 6),
    _Lgs2816crpsDaylightSavingTime_Type()
)
lgs2816crpsDaylightSavingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsDaylightSavingTime.setStatus("current")
_Lgs2816crpsDaylightStartTime_Type = DisplayString
_Lgs2816crpsDaylightStartTime_Object = MibScalar
lgs2816crpsDaylightStartTime = _Lgs2816crpsDaylightStartTime_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 1, 3, 7),
    _Lgs2816crpsDaylightStartTime_Type()
)
lgs2816crpsDaylightStartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsDaylightStartTime.setStatus("current")
_Lgs2816crpsDaylightEndTime_Type = DisplayString
_Lgs2816crpsDaylightEndTime_Object = MibScalar
lgs2816crpsDaylightEndTime = _Lgs2816crpsDaylightEndTime_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 1, 3, 8),
    _Lgs2816crpsDaylightEndTime_Type()
)
lgs2816crpsDaylightEndTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsDaylightEndTime.setStatus("current")
_Lgs2816crpsAccount_ObjectIdentity = ObjectIdentity
lgs2816crpsAccount = _Lgs2816crpsAccount_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 1, 4)
)


class _Lgs2816crpsAccountNumber_Type(Integer32):
    """Custom type lgs2816crpsAccountNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Lgs2816crpsAccountNumber_Type.__name__ = "Integer32"
_Lgs2816crpsAccountNumber_Object = MibScalar
lgs2816crpsAccountNumber = _Lgs2816crpsAccountNumber_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 1, 4, 1),
    _Lgs2816crpsAccountNumber_Type()
)
lgs2816crpsAccountNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsAccountNumber.setStatus("current")
_Lgs2816crpsAccountTable_Object = MibTable
lgs2816crpsAccountTable = _Lgs2816crpsAccountTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 1, 4, 2)
)
if mibBuilder.loadTexts:
    lgs2816crpsAccountTable.setStatus("current")
_Lgs2816crpsAccountEntry_Object = MibTableRow
lgs2816crpsAccountEntry = _Lgs2816crpsAccountEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 1, 4, 2, 1)
)
lgs2816crpsAccountEntry.setIndexNames(
    (0, "PRIVATE-LGS2816CRPS-MIB", "lgs2816crpsAccountIndex"),
)
if mibBuilder.loadTexts:
    lgs2816crpsAccountEntry.setStatus("current")


class _Lgs2816crpsAccountIndex_Type(Integer32):
    """Custom type lgs2816crpsAccountIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Lgs2816crpsAccountIndex_Type.__name__ = "Integer32"
_Lgs2816crpsAccountIndex_Object = MibTableColumn
lgs2816crpsAccountIndex = _Lgs2816crpsAccountIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 1, 4, 2, 1, 1),
    _Lgs2816crpsAccountIndex_Type()
)
lgs2816crpsAccountIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsAccountIndex.setStatus("current")
_Lgs2816crpsAccountAuthorization_Type = DisplayString
_Lgs2816crpsAccountAuthorization_Object = MibTableColumn
lgs2816crpsAccountAuthorization = _Lgs2816crpsAccountAuthorization_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 1, 4, 2, 1, 2),
    _Lgs2816crpsAccountAuthorization_Type()
)
lgs2816crpsAccountAuthorization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsAccountAuthorization.setStatus("current")
_Lgs2816crpsAccountName_Type = DisplayString
_Lgs2816crpsAccountName_Object = MibTableColumn
lgs2816crpsAccountName = _Lgs2816crpsAccountName_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 1, 4, 2, 1, 3),
    _Lgs2816crpsAccountName_Type()
)
lgs2816crpsAccountName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsAccountName.setStatus("current")
_Lgs2816crpsAccountPassword_Type = DisplayString
_Lgs2816crpsAccountPassword_Object = MibTableColumn
lgs2816crpsAccountPassword = _Lgs2816crpsAccountPassword_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 1, 4, 2, 1, 4),
    _Lgs2816crpsAccountPassword_Type()
)
lgs2816crpsAccountPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsAccountPassword.setStatus("current")


class _Lgs2816crpsAccountAddAuthorization_Type(Integer32):
    """Custom type lgs2816crpsAccountAddAuthorization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Lgs2816crpsAccountAddAuthorization_Type.__name__ = "Integer32"
_Lgs2816crpsAccountAddAuthorization_Object = MibScalar
lgs2816crpsAccountAddAuthorization = _Lgs2816crpsAccountAddAuthorization_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 1, 4, 3),
    _Lgs2816crpsAccountAddAuthorization_Type()
)
lgs2816crpsAccountAddAuthorization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsAccountAddAuthorization.setStatus("current")
_Lgs2816crpsAccountAddName_Type = DisplayString
_Lgs2816crpsAccountAddName_Object = MibScalar
lgs2816crpsAccountAddName = _Lgs2816crpsAccountAddName_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 1, 4, 4),
    _Lgs2816crpsAccountAddName_Type()
)
lgs2816crpsAccountAddName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsAccountAddName.setStatus("current")
_Lgs2816crpsAccountAddPassword_Type = DisplayString
_Lgs2816crpsAccountAddPassword_Object = MibScalar
lgs2816crpsAccountAddPassword = _Lgs2816crpsAccountAddPassword_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 1, 4, 5),
    _Lgs2816crpsAccountAddPassword_Type()
)
lgs2816crpsAccountAddPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsAccountAddPassword.setStatus("current")


class _Lgs2816crpsDoAccountAdd_Type(Integer32):
    """Custom type lgs2816crpsDoAccountAdd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2816crpsDoAccountAdd_Type.__name__ = "Integer32"
_Lgs2816crpsDoAccountAdd_Object = MibScalar
lgs2816crpsDoAccountAdd = _Lgs2816crpsDoAccountAdd_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 1, 4, 6),
    _Lgs2816crpsDoAccountAdd_Type()
)
lgs2816crpsDoAccountAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsDoAccountAdd.setStatus("current")


class _Lgs2816crpsAccountDel_Type(Integer32):
    """Custom type lgs2816crpsAccountDel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 5),
    )


_Lgs2816crpsAccountDel_Type.__name__ = "Integer32"
_Lgs2816crpsAccountDel_Object = MibScalar
lgs2816crpsAccountDel = _Lgs2816crpsAccountDel_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 1, 4, 7),
    _Lgs2816crpsAccountDel_Type()
)
lgs2816crpsAccountDel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsAccountDel.setStatus("current")
_Lgs2816crpsVsm_ObjectIdentity = ObjectIdentity
lgs2816crpsVsm = _Lgs2816crpsVsm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 1, 5)
)


class _Lgs2816crpsVsmState_Type(Integer32):
    """Custom type lgs2816crpsVsmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2816crpsVsmState_Type.__name__ = "Integer32"
_Lgs2816crpsVsmState_Object = MibScalar
lgs2816crpsVsmState = _Lgs2816crpsVsmState_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 1, 5, 1),
    _Lgs2816crpsVsmState_Type()
)
lgs2816crpsVsmState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsVsmState.setStatus("current")


class _Lgs2816crpsVsmRole_Type(Integer32):
    """Custom type lgs2816crpsVsmRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2816crpsVsmRole_Type.__name__ = "Integer32"
_Lgs2816crpsVsmRole_Object = MibScalar
lgs2816crpsVsmRole = _Lgs2816crpsVsmRole_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 1, 5, 2),
    _Lgs2816crpsVsmRole_Type()
)
lgs2816crpsVsmRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsVsmRole.setStatus("current")
_Lgs2816crpsVsmGroupid_Type = DisplayString
_Lgs2816crpsVsmGroupid_Object = MibScalar
lgs2816crpsVsmGroupid = _Lgs2816crpsVsmGroupid_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 1, 5, 3),
    _Lgs2816crpsVsmGroupid_Type()
)
lgs2816crpsVsmGroupid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsVsmGroupid.setStatus("current")
_Lgs2816crpsExternalPower_ObjectIdentity = ObjectIdentity
lgs2816crpsExternalPower = _Lgs2816crpsExternalPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 1, 6)
)


class _Lgs2816crpsExternalPowerExist_Type(Integer32):
    """Custom type lgs2816crpsExternalPowerExist based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2816crpsExternalPowerExist_Type.__name__ = "Integer32"
_Lgs2816crpsExternalPowerExist_Object = MibScalar
lgs2816crpsExternalPowerExist = _Lgs2816crpsExternalPowerExist_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 1, 6, 1),
    _Lgs2816crpsExternalPowerExist_Type()
)
lgs2816crpsExternalPowerExist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsExternalPowerExist.setStatus("current")
_Lgs2816crpsExternalPowerInfo_ObjectIdentity = ObjectIdentity
lgs2816crpsExternalPowerInfo = _Lgs2816crpsExternalPowerInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 1, 6, 2)
)
_Lgs2816crpsExternalPowerModel_Type = DisplayString
_Lgs2816crpsExternalPowerModel_Object = MibScalar
lgs2816crpsExternalPowerModel = _Lgs2816crpsExternalPowerModel_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 1, 6, 2, 1),
    _Lgs2816crpsExternalPowerModel_Type()
)
lgs2816crpsExternalPowerModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsExternalPowerModel.setStatus("current")
_Lgs2816crpsExternalPowerHard_Type = DisplayString
_Lgs2816crpsExternalPowerHard_Object = MibScalar
lgs2816crpsExternalPowerHard = _Lgs2816crpsExternalPowerHard_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 1, 6, 2, 2),
    _Lgs2816crpsExternalPowerHard_Type()
)
lgs2816crpsExternalPowerHard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsExternalPowerHard.setStatus("current")
_Lgs2816crpsExternalPowerMech_Type = DisplayString
_Lgs2816crpsExternalPowerMech_Object = MibScalar
lgs2816crpsExternalPowerMech = _Lgs2816crpsExternalPowerMech_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 1, 6, 2, 3),
    _Lgs2816crpsExternalPowerMech_Type()
)
lgs2816crpsExternalPowerMech.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsExternalPowerMech.setStatus("current")
_Lgs2816crpsExternalPowerSerial_Type = DisplayString
_Lgs2816crpsExternalPowerSerial_Object = MibScalar
lgs2816crpsExternalPowerSerial = _Lgs2816crpsExternalPowerSerial_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 1, 6, 2, 4),
    _Lgs2816crpsExternalPowerSerial_Type()
)
lgs2816crpsExternalPowerSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsExternalPowerSerial.setStatus("current")
_Lgs2816crpsExternalPowerTemp_Type = DisplayString
_Lgs2816crpsExternalPowerTemp_Object = MibScalar
lgs2816crpsExternalPowerTemp = _Lgs2816crpsExternalPowerTemp_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 1, 6, 2, 5),
    _Lgs2816crpsExternalPowerTemp_Type()
)
lgs2816crpsExternalPowerTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsExternalPowerTemp.setStatus("current")
_Lgs2816crpsExternalPowerFan_Type = DisplayString
_Lgs2816crpsExternalPowerFan_Object = MibScalar
lgs2816crpsExternalPowerFan = _Lgs2816crpsExternalPowerFan_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 1, 6, 2, 6),
    _Lgs2816crpsExternalPowerFan_Type()
)
lgs2816crpsExternalPowerFan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsExternalPowerFan.setStatus("current")
_Lgs2816crpsExternalPowerVoltage_Type = DisplayString
_Lgs2816crpsExternalPowerVoltage_Object = MibScalar
lgs2816crpsExternalPowerVoltage = _Lgs2816crpsExternalPowerVoltage_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 1, 6, 2, 7),
    _Lgs2816crpsExternalPowerVoltage_Type()
)
lgs2816crpsExternalPowerVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsExternalPowerVoltage.setStatus("current")
_Lgs2816crpsExternalPowerModuleTable_Object = MibTable
lgs2816crpsExternalPowerModuleTable = _Lgs2816crpsExternalPowerModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 1, 6, 3)
)
if mibBuilder.loadTexts:
    lgs2816crpsExternalPowerModuleTable.setStatus("current")
_Lgs2816crpsExternalPowerModuleEntry_Object = MibTableRow
lgs2816crpsExternalPowerModuleEntry = _Lgs2816crpsExternalPowerModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 1, 6, 3, 1)
)
lgs2816crpsExternalPowerModuleEntry.setIndexNames(
    (0, "PRIVATE-LGS2816CRPS-MIB", "lgs2816crpsPowerModuleIndex"),
)
if mibBuilder.loadTexts:
    lgs2816crpsExternalPowerModuleEntry.setStatus("current")


class _Lgs2816crpsPowerModuleIndex_Type(Integer32):
    """Custom type lgs2816crpsPowerModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_Lgs2816crpsPowerModuleIndex_Type.__name__ = "Integer32"
_Lgs2816crpsPowerModuleIndex_Object = MibTableColumn
lgs2816crpsPowerModuleIndex = _Lgs2816crpsPowerModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 1, 6, 3, 1, 1),
    _Lgs2816crpsPowerModuleIndex_Type()
)
lgs2816crpsPowerModuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgs2816crpsPowerModuleIndex.setStatus("current")
_Lgs2816crpsPowerModuleName_Type = DisplayString
_Lgs2816crpsPowerModuleName_Object = MibTableColumn
lgs2816crpsPowerModuleName = _Lgs2816crpsPowerModuleName_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 1, 6, 3, 1, 2),
    _Lgs2816crpsPowerModuleName_Type()
)
lgs2816crpsPowerModuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsPowerModuleName.setStatus("current")
_Lgs2816crpsPowerModuleType_Type = DisplayString
_Lgs2816crpsPowerModuleType_Object = MibTableColumn
lgs2816crpsPowerModuleType = _Lgs2816crpsPowerModuleType_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 1, 6, 3, 1, 3),
    _Lgs2816crpsPowerModuleType_Type()
)
lgs2816crpsPowerModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsPowerModuleType.setStatus("current")
_Lgs2816crpsPowerModuleSerial_Type = DisplayString
_Lgs2816crpsPowerModuleSerial_Object = MibTableColumn
lgs2816crpsPowerModuleSerial = _Lgs2816crpsPowerModuleSerial_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 1, 6, 3, 1, 4),
    _Lgs2816crpsPowerModuleSerial_Type()
)
lgs2816crpsPowerModuleSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsPowerModuleSerial.setStatus("current")
_Lgs2816crpsPowerModuleHard_Type = DisplayString
_Lgs2816crpsPowerModuleHard_Object = MibTableColumn
lgs2816crpsPowerModuleHard = _Lgs2816crpsPowerModuleHard_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 1, 6, 3, 1, 5),
    _Lgs2816crpsPowerModuleHard_Type()
)
lgs2816crpsPowerModuleHard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsPowerModuleHard.setStatus("current")
_Lgs2816crpsPowerModuleMech_Type = DisplayString
_Lgs2816crpsPowerModuleMech_Object = MibTableColumn
lgs2816crpsPowerModuleMech = _Lgs2816crpsPowerModuleMech_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 1, 6, 3, 1, 6),
    _Lgs2816crpsPowerModuleMech_Type()
)
lgs2816crpsPowerModuleMech.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsPowerModuleMech.setStatus("current")
_Lgs2816crpsPowerModuleVolt_Type = DisplayString
_Lgs2816crpsPowerModuleVolt_Object = MibTableColumn
lgs2816crpsPowerModuleVolt = _Lgs2816crpsPowerModuleVolt_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 1, 6, 3, 1, 7),
    _Lgs2816crpsPowerModuleVolt_Type()
)
lgs2816crpsPowerModuleVolt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsPowerModuleVolt.setStatus("current")
_Lgs2816crpsPowerModuleCurrent_Type = DisplayString
_Lgs2816crpsPowerModuleCurrent_Object = MibTableColumn
lgs2816crpsPowerModuleCurrent = _Lgs2816crpsPowerModuleCurrent_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 1, 6, 3, 1, 8),
    _Lgs2816crpsPowerModuleCurrent_Type()
)
lgs2816crpsPowerModuleCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsPowerModuleCurrent.setStatus("current")
_Lgs2816crpsPowerModuleMaxPwr_Type = DisplayString
_Lgs2816crpsPowerModuleMaxPwr_Object = MibTableColumn
lgs2816crpsPowerModuleMaxPwr = _Lgs2816crpsPowerModuleMaxPwr_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 1, 6, 3, 1, 9),
    _Lgs2816crpsPowerModuleMaxPwr_Type()
)
lgs2816crpsPowerModuleMaxPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsPowerModuleMaxPwr.setStatus("current")
_Lgs2816crpsTrapHost_ObjectIdentity = ObjectIdentity
lgs2816crpsTrapHost = _Lgs2816crpsTrapHost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 2)
)
_Lgs2816crpsTrapHostTable_Object = MibTable
lgs2816crpsTrapHostTable = _Lgs2816crpsTrapHostTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 2, 1)
)
if mibBuilder.loadTexts:
    lgs2816crpsTrapHostTable.setStatus("current")
_Lgs2816crpsTrapHostEntry_Object = MibTableRow
lgs2816crpsTrapHostEntry = _Lgs2816crpsTrapHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 2, 1, 1)
)
lgs2816crpsTrapHostEntry.setIndexNames(
    (0, "PRIVATE-LGS2816CRPS-MIB", "lgs2816crpsTrapHostIndex"),
)
if mibBuilder.loadTexts:
    lgs2816crpsTrapHostEntry.setStatus("current")


class _Lgs2816crpsTrapHostIndex_Type(Integer32):
    """Custom type lgs2816crpsTrapHostIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_Lgs2816crpsTrapHostIndex_Type.__name__ = "Integer32"
_Lgs2816crpsTrapHostIndex_Object = MibTableColumn
lgs2816crpsTrapHostIndex = _Lgs2816crpsTrapHostIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 2, 1, 1, 1),
    _Lgs2816crpsTrapHostIndex_Type()
)
lgs2816crpsTrapHostIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsTrapHostIndex.setStatus("current")


class _Lgs2816crpsTrapHostVersion_Type(Integer32):
    """Custom type lgs2816crpsTrapHostVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Lgs2816crpsTrapHostVersion_Type.__name__ = "Integer32"
_Lgs2816crpsTrapHostVersion_Object = MibTableColumn
lgs2816crpsTrapHostVersion = _Lgs2816crpsTrapHostVersion_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 2, 1, 1, 2),
    _Lgs2816crpsTrapHostVersion_Type()
)
lgs2816crpsTrapHostVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsTrapHostVersion.setStatus("current")
_Lgs2816crpsTrapHostIP_Type = DisplayString
_Lgs2816crpsTrapHostIP_Object = MibTableColumn
lgs2816crpsTrapHostIP = _Lgs2816crpsTrapHostIP_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 2, 1, 1, 3),
    _Lgs2816crpsTrapHostIP_Type()
)
lgs2816crpsTrapHostIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsTrapHostIP.setStatus("current")


class _Lgs2816crpsTrapHostPort_Type(Integer32):
    """Custom type lgs2816crpsTrapHostPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Lgs2816crpsTrapHostPort_Type.__name__ = "Integer32"
_Lgs2816crpsTrapHostPort_Object = MibTableColumn
lgs2816crpsTrapHostPort = _Lgs2816crpsTrapHostPort_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 2, 1, 1, 4),
    _Lgs2816crpsTrapHostPort_Type()
)
lgs2816crpsTrapHostPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsTrapHostPort.setStatus("current")
_Lgs2816crpsTrapHostCommunity_Type = DisplayString
_Lgs2816crpsTrapHostCommunity_Object = MibTableColumn
lgs2816crpsTrapHostCommunity = _Lgs2816crpsTrapHostCommunity_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 2, 1, 1, 5),
    _Lgs2816crpsTrapHostCommunity_Type()
)
lgs2816crpsTrapHostCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsTrapHostCommunity.setStatus("current")


class _Lgs2816crpsTrapHostSecurityLevel_Type(Integer32):
    """Custom type lgs2816crpsTrapHostSecurityLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Lgs2816crpsTrapHostSecurityLevel_Type.__name__ = "Integer32"
_Lgs2816crpsTrapHostSecurityLevel_Object = MibTableColumn
lgs2816crpsTrapHostSecurityLevel = _Lgs2816crpsTrapHostSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 2, 1, 1, 6),
    _Lgs2816crpsTrapHostSecurityLevel_Type()
)
lgs2816crpsTrapHostSecurityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsTrapHostSecurityLevel.setStatus("current")
_Lgs2816crpsTrapHostAuthPtc_Type = DisplayString
_Lgs2816crpsTrapHostAuthPtc_Object = MibTableColumn
lgs2816crpsTrapHostAuthPtc = _Lgs2816crpsTrapHostAuthPtc_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 2, 1, 1, 7),
    _Lgs2816crpsTrapHostAuthPtc_Type()
)
lgs2816crpsTrapHostAuthPtc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsTrapHostAuthPtc.setStatus("current")
_Lgs2816crpsTrapHostAuthPassword_Type = DisplayString
_Lgs2816crpsTrapHostAuthPassword_Object = MibTableColumn
lgs2816crpsTrapHostAuthPassword = _Lgs2816crpsTrapHostAuthPassword_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 2, 1, 1, 8),
    _Lgs2816crpsTrapHostAuthPassword_Type()
)
lgs2816crpsTrapHostAuthPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsTrapHostAuthPassword.setStatus("current")
_Lgs2816crpsTrapHostPrivPtc_Type = DisplayString
_Lgs2816crpsTrapHostPrivPtc_Object = MibTableColumn
lgs2816crpsTrapHostPrivPtc = _Lgs2816crpsTrapHostPrivPtc_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 2, 1, 1, 9),
    _Lgs2816crpsTrapHostPrivPtc_Type()
)
lgs2816crpsTrapHostPrivPtc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsTrapHostPrivPtc.setStatus("current")
_Lgs2816crpsTrapHostPrivPassword_Type = DisplayString
_Lgs2816crpsTrapHostPrivPassword_Object = MibTableColumn
lgs2816crpsTrapHostPrivPassword = _Lgs2816crpsTrapHostPrivPassword_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 2, 1, 1, 10),
    _Lgs2816crpsTrapHostPrivPassword_Type()
)
lgs2816crpsTrapHostPrivPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsTrapHostPrivPassword.setStatus("current")


class _Lgs2816crpsTrapHostCurrentMode_Type(Integer32):
    """Custom type lgs2816crpsTrapHostCurrentMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Lgs2816crpsTrapHostCurrentMode_Type.__name__ = "Integer32"
_Lgs2816crpsTrapHostCurrentMode_Object = MibTableColumn
lgs2816crpsTrapHostCurrentMode = _Lgs2816crpsTrapHostCurrentMode_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 2, 1, 1, 11),
    _Lgs2816crpsTrapHostCurrentMode_Type()
)
lgs2816crpsTrapHostCurrentMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsTrapHostCurrentMode.setStatus("current")
_Lgs2816crpsAlarm_ObjectIdentity = ObjectIdentity
lgs2816crpsAlarm = _Lgs2816crpsAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 3)
)
_Lgs2816crpsEvent_ObjectIdentity = ObjectIdentity
lgs2816crpsEvent = _Lgs2816crpsEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 3, 1)
)


class _Lgs2816crpsEventNumber_Type(Integer32):
    """Custom type lgs2816crpsEventNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Lgs2816crpsEventNumber_Type.__name__ = "Integer32"
_Lgs2816crpsEventNumber_Object = MibScalar
lgs2816crpsEventNumber = _Lgs2816crpsEventNumber_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 3, 1, 1),
    _Lgs2816crpsEventNumber_Type()
)
lgs2816crpsEventNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsEventNumber.setStatus("current")
_Lgs2816crpsEventTable_Object = MibTable
lgs2816crpsEventTable = _Lgs2816crpsEventTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    lgs2816crpsEventTable.setStatus("current")
_Lgs2816crpsEventEntry_Object = MibTableRow
lgs2816crpsEventEntry = _Lgs2816crpsEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 3, 1, 2, 1)
)
lgs2816crpsEventEntry.setIndexNames(
    (0, "PRIVATE-LGS2816CRPS-MIB", "lgs2816crpsEventIndex"),
)
if mibBuilder.loadTexts:
    lgs2816crpsEventEntry.setStatus("current")


class _Lgs2816crpsEventIndex_Type(Integer32):
    """Custom type lgs2816crpsEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Lgs2816crpsEventIndex_Type.__name__ = "Integer32"
_Lgs2816crpsEventIndex_Object = MibTableColumn
lgs2816crpsEventIndex = _Lgs2816crpsEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 3, 1, 2, 1, 1),
    _Lgs2816crpsEventIndex_Type()
)
lgs2816crpsEventIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsEventIndex.setStatus("current")
_Lgs2816crpsEventName_Type = DisplayString
_Lgs2816crpsEventName_Object = MibTableColumn
lgs2816crpsEventName = _Lgs2816crpsEventName_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 3, 1, 2, 1, 2),
    _Lgs2816crpsEventName_Type()
)
lgs2816crpsEventName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsEventName.setStatus("current")


class _Lgs2816crpsEventSendEmail_Type(Integer32):
    """Custom type lgs2816crpsEventSendEmail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2816crpsEventSendEmail_Type.__name__ = "Integer32"
_Lgs2816crpsEventSendEmail_Object = MibTableColumn
lgs2816crpsEventSendEmail = _Lgs2816crpsEventSendEmail_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 3, 1, 2, 1, 3),
    _Lgs2816crpsEventSendEmail_Type()
)
lgs2816crpsEventSendEmail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsEventSendEmail.setStatus("current")


class _Lgs2816crpsEventSendTrap_Type(Integer32):
    """Custom type lgs2816crpsEventSendTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2816crpsEventSendTrap_Type.__name__ = "Integer32"
_Lgs2816crpsEventSendTrap_Object = MibTableColumn
lgs2816crpsEventSendTrap = _Lgs2816crpsEventSendTrap_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 3, 1, 2, 1, 4),
    _Lgs2816crpsEventSendTrap_Type()
)
lgs2816crpsEventSendTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsEventSendTrap.setStatus("current")
_Lgs2816crpsEmail_ObjectIdentity = ObjectIdentity
lgs2816crpsEmail = _Lgs2816crpsEmail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 3, 2)
)
_Lgs2816crpsEmailServer_Type = DisplayString
_Lgs2816crpsEmailServer_Object = MibScalar
lgs2816crpsEmailServer = _Lgs2816crpsEmailServer_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 3, 2, 1),
    _Lgs2816crpsEmailServer_Type()
)
lgs2816crpsEmailServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsEmailServer.setStatus("current")
_Lgs2816crpsEmailUsername_Type = DisplayString
_Lgs2816crpsEmailUsername_Object = MibScalar
lgs2816crpsEmailUsername = _Lgs2816crpsEmailUsername_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 3, 2, 2),
    _Lgs2816crpsEmailUsername_Type()
)
lgs2816crpsEmailUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsEmailUsername.setStatus("current")
_Lgs2816crpsEmailPassword_Type = DisplayString
_Lgs2816crpsEmailPassword_Object = MibScalar
lgs2816crpsEmailPassword = _Lgs2816crpsEmailPassword_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 3, 2, 3),
    _Lgs2816crpsEmailPassword_Type()
)
lgs2816crpsEmailPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsEmailPassword.setStatus("current")
_Lgs2816crpsEmailSender_Type = DisplayString
_Lgs2816crpsEmailSender_Object = MibScalar
lgs2816crpsEmailSender = _Lgs2816crpsEmailSender_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 3, 2, 4),
    _Lgs2816crpsEmailSender_Type()
)
lgs2816crpsEmailSender.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsEmailSender.setStatus("current")
_Lgs2816crpsEmailReturnPath_Type = DisplayString
_Lgs2816crpsEmailReturnPath_Object = MibScalar
lgs2816crpsEmailReturnPath = _Lgs2816crpsEmailReturnPath_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 3, 2, 5),
    _Lgs2816crpsEmailReturnPath_Type()
)
lgs2816crpsEmailReturnPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsEmailReturnPath.setStatus("current")


class _Lgs2816crpsEmailUserNumber_Type(Integer32):
    """Custom type lgs2816crpsEmailUserNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_Lgs2816crpsEmailUserNumber_Type.__name__ = "Integer32"
_Lgs2816crpsEmailUserNumber_Object = MibScalar
lgs2816crpsEmailUserNumber = _Lgs2816crpsEmailUserNumber_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 3, 2, 6),
    _Lgs2816crpsEmailUserNumber_Type()
)
lgs2816crpsEmailUserNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsEmailUserNumber.setStatus("current")
_Lgs2816crpsEmailUserTable_Object = MibTable
lgs2816crpsEmailUserTable = _Lgs2816crpsEmailUserTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 3, 2, 7)
)
if mibBuilder.loadTexts:
    lgs2816crpsEmailUserTable.setStatus("current")
_Lgs2816crpsEmailUserEntry_Object = MibTableRow
lgs2816crpsEmailUserEntry = _Lgs2816crpsEmailUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 3, 2, 7, 1)
)
lgs2816crpsEmailUserEntry.setIndexNames(
    (0, "PRIVATE-LGS2816CRPS-MIB", "lgs2816crpsEmailUserIndex"),
)
if mibBuilder.loadTexts:
    lgs2816crpsEmailUserEntry.setStatus("current")


class _Lgs2816crpsEmailUserIndex_Type(Integer32):
    """Custom type lgs2816crpsEmailUserIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_Lgs2816crpsEmailUserIndex_Type.__name__ = "Integer32"
_Lgs2816crpsEmailUserIndex_Object = MibTableColumn
lgs2816crpsEmailUserIndex = _Lgs2816crpsEmailUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 3, 2, 7, 1, 1),
    _Lgs2816crpsEmailUserIndex_Type()
)
lgs2816crpsEmailUserIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsEmailUserIndex.setStatus("current")
_Lgs2816crpsEmailUserAddress_Type = DisplayString
_Lgs2816crpsEmailUserAddress_Object = MibTableColumn
lgs2816crpsEmailUserAddress = _Lgs2816crpsEmailUserAddress_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 3, 2, 7, 1, 2),
    _Lgs2816crpsEmailUserAddress_Type()
)
lgs2816crpsEmailUserAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsEmailUserAddress.setStatus("current")
_Lgs2816crpsConfiguration_ObjectIdentity = ObjectIdentity
lgs2816crpsConfiguration = _Lgs2816crpsConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 5)
)
_Lgs2816crpsSaveRestore_ObjectIdentity = ObjectIdentity
lgs2816crpsSaveRestore = _Lgs2816crpsSaveRestore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 5, 1)
)


class _Lgs2816crpsSaveStart_Type(Integer32):
    """Custom type lgs2816crpsSaveStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2816crpsSaveStart_Type.__name__ = "Integer32"
_Lgs2816crpsSaveStart_Object = MibScalar
lgs2816crpsSaveStart = _Lgs2816crpsSaveStart_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 5, 1, 1),
    _Lgs2816crpsSaveStart_Type()
)
lgs2816crpsSaveStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsSaveStart.setStatus("current")


class _Lgs2816crpsSaveUser_Type(Integer32):
    """Custom type lgs2816crpsSaveUser based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2816crpsSaveUser_Type.__name__ = "Integer32"
_Lgs2816crpsSaveUser_Object = MibScalar
lgs2816crpsSaveUser = _Lgs2816crpsSaveUser_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 5, 1, 2),
    _Lgs2816crpsSaveUser_Type()
)
lgs2816crpsSaveUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsSaveUser.setStatus("current")


class _Lgs2816crpsRestoreDefault_Type(Integer32):
    """Custom type lgs2816crpsRestoreDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_Lgs2816crpsRestoreDefault_Type.__name__ = "Integer32"
_Lgs2816crpsRestoreDefault_Object = MibScalar
lgs2816crpsRestoreDefault = _Lgs2816crpsRestoreDefault_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 5, 1, 3),
    _Lgs2816crpsRestoreDefault_Type()
)
lgs2816crpsRestoreDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsRestoreDefault.setStatus("current")


class _Lgs2816crpsRestoreUser_Type(Integer32):
    """Custom type lgs2816crpsRestoreUser based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2816crpsRestoreUser_Type.__name__ = "Integer32"
_Lgs2816crpsRestoreUser_Object = MibScalar
lgs2816crpsRestoreUser = _Lgs2816crpsRestoreUser_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 5, 1, 4),
    _Lgs2816crpsRestoreUser_Type()
)
lgs2816crpsRestoreUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsRestoreUser.setStatus("current")
_Lgs2816crpsConfigFile_ObjectIdentity = ObjectIdentity
lgs2816crpsConfigFile = _Lgs2816crpsConfigFile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 5, 2)
)
_Lgs2816crpsExportIpAddress_Type = IpAddress
_Lgs2816crpsExportIpAddress_Object = MibScalar
lgs2816crpsExportIpAddress = _Lgs2816crpsExportIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 5, 2, 1),
    _Lgs2816crpsExportIpAddress_Type()
)
lgs2816crpsExportIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsExportIpAddress.setStatus("current")


class _Lgs2816crpsDoExportConfig_Type(Integer32):
    """Custom type lgs2816crpsDoExportConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_Lgs2816crpsDoExportConfig_Type.__name__ = "Integer32"
_Lgs2816crpsDoExportConfig_Object = MibScalar
lgs2816crpsDoExportConfig = _Lgs2816crpsDoExportConfig_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 5, 2, 2),
    _Lgs2816crpsDoExportConfig_Type()
)
lgs2816crpsDoExportConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsDoExportConfig.setStatus("current")
_Lgs2816crpsImportIpAddress_Type = IpAddress
_Lgs2816crpsImportIpAddress_Object = MibScalar
lgs2816crpsImportIpAddress = _Lgs2816crpsImportIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 5, 2, 3),
    _Lgs2816crpsImportIpAddress_Type()
)
lgs2816crpsImportIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsImportIpAddress.setStatus("current")
_Lgs2816crpsImportConfigName_Type = DisplayString
_Lgs2816crpsImportConfigName_Object = MibScalar
lgs2816crpsImportConfigName = _Lgs2816crpsImportConfigName_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 5, 2, 4),
    _Lgs2816crpsImportConfigName_Type()
)
lgs2816crpsImportConfigName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsImportConfigName.setStatus("current")


class _Lgs2816crpsDoImportConfig_Type(Integer32):
    """Custom type lgs2816crpsDoImportConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_Lgs2816crpsDoImportConfig_Type.__name__ = "Integer32"
_Lgs2816crpsDoImportConfig_Object = MibScalar
lgs2816crpsDoImportConfig = _Lgs2816crpsDoImportConfig_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 5, 2, 5),
    _Lgs2816crpsDoImportConfig_Type()
)
lgs2816crpsDoImportConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsDoImportConfig.setStatus("current")
_Lgs2816crpsLog_ObjectIdentity = ObjectIdentity
lgs2816crpsLog = _Lgs2816crpsLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 7)
)


class _Lgs2816crpsClearLog_Type(Integer32):
    """Custom type lgs2816crpsClearLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2816crpsClearLog_Type.__name__ = "Integer32"
_Lgs2816crpsClearLog_Object = MibScalar
lgs2816crpsClearLog = _Lgs2816crpsClearLog_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 7, 1),
    _Lgs2816crpsClearLog_Type()
)
lgs2816crpsClearLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsClearLog.setStatus("current")


class _Lgs2816crpsLogNumber_Type(Integer32):
    """Custom type lgs2816crpsLogNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_Lgs2816crpsLogNumber_Type.__name__ = "Integer32"
_Lgs2816crpsLogNumber_Object = MibScalar
lgs2816crpsLogNumber = _Lgs2816crpsLogNumber_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 7, 4),
    _Lgs2816crpsLogNumber_Type()
)
lgs2816crpsLogNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsLogNumber.setStatus("current")
_Lgs2816crpsLogTable_Object = MibTable
lgs2816crpsLogTable = _Lgs2816crpsLogTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 7, 5)
)
if mibBuilder.loadTexts:
    lgs2816crpsLogTable.setStatus("current")
_Lgs2816crpsLogEntry_Object = MibTableRow
lgs2816crpsLogEntry = _Lgs2816crpsLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 7, 5, 1)
)
lgs2816crpsLogEntry.setIndexNames(
    (0, "PRIVATE-LGS2816CRPS-MIB", "lgs2816crpsLogIndex"),
)
if mibBuilder.loadTexts:
    lgs2816crpsLogEntry.setStatus("current")


class _Lgs2816crpsLogIndex_Type(Integer32):
    """Custom type lgs2816crpsLogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_Lgs2816crpsLogIndex_Type.__name__ = "Integer32"
_Lgs2816crpsLogIndex_Object = MibTableColumn
lgs2816crpsLogIndex = _Lgs2816crpsLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 7, 5, 1, 1),
    _Lgs2816crpsLogIndex_Type()
)
lgs2816crpsLogIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgs2816crpsLogIndex.setStatus("current")
_Lgs2816crpsLogEvent_Type = DisplayString
_Lgs2816crpsLogEvent_Object = MibTableColumn
lgs2816crpsLogEvent = _Lgs2816crpsLogEvent_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 7, 5, 1, 2),
    _Lgs2816crpsLogEvent_Type()
)
lgs2816crpsLogEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsLogEvent.setStatus("current")
_Lgs2816crpsFirmware_ObjectIdentity = ObjectIdentity
lgs2816crpsFirmware = _Lgs2816crpsFirmware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 8)
)
_Lgs2816crpsFirmwareIpAddress_Type = IpAddress
_Lgs2816crpsFirmwareIpAddress_Object = MibScalar
lgs2816crpsFirmwareIpAddress = _Lgs2816crpsFirmwareIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 8, 1),
    _Lgs2816crpsFirmwareIpAddress_Type()
)
lgs2816crpsFirmwareIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsFirmwareIpAddress.setStatus("current")
_Lgs2816crpsFirmwareFileName_Type = DisplayString
_Lgs2816crpsFirmwareFileName_Object = MibScalar
lgs2816crpsFirmwareFileName = _Lgs2816crpsFirmwareFileName_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 8, 2),
    _Lgs2816crpsFirmwareFileName_Type()
)
lgs2816crpsFirmwareFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsFirmwareFileName.setStatus("current")


class _Lgs2816crpsDoFirmwareUpgrade_Type(Integer32):
    """Custom type lgs2816crpsDoFirmwareUpgrade based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2816crpsDoFirmwareUpgrade_Type.__name__ = "Integer32"
_Lgs2816crpsDoFirmwareUpgrade_Object = MibScalar
lgs2816crpsDoFirmwareUpgrade = _Lgs2816crpsDoFirmwareUpgrade_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 8, 3),
    _Lgs2816crpsDoFirmwareUpgrade_Type()
)
lgs2816crpsDoFirmwareUpgrade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsDoFirmwareUpgrade.setStatus("current")
_Lgs2816crpsPort_ObjectIdentity = ObjectIdentity
lgs2816crpsPort = _Lgs2816crpsPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 9)
)
_Lgs2816crpsPortStatus_ObjectIdentity = ObjectIdentity
lgs2816crpsPortStatus = _Lgs2816crpsPortStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 9, 1)
)


class _Lgs2816crpsPortStatusNumber_Type(Integer32):
    """Custom type lgs2816crpsPortStatusNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Lgs2816crpsPortStatusNumber_Type.__name__ = "Integer32"
_Lgs2816crpsPortStatusNumber_Object = MibScalar
lgs2816crpsPortStatusNumber = _Lgs2816crpsPortStatusNumber_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 9, 1, 1),
    _Lgs2816crpsPortStatusNumber_Type()
)
lgs2816crpsPortStatusNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsPortStatusNumber.setStatus("current")
_Lgs2816crpsPortStatusTable_Object = MibTable
lgs2816crpsPortStatusTable = _Lgs2816crpsPortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 9, 1, 2)
)
if mibBuilder.loadTexts:
    lgs2816crpsPortStatusTable.setStatus("current")
_Lgs2816crpsPortStatusEntry_Object = MibTableRow
lgs2816crpsPortStatusEntry = _Lgs2816crpsPortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 9, 1, 2, 1)
)
lgs2816crpsPortStatusEntry.setIndexNames(
    (0, "PRIVATE-LGS2816CRPS-MIB", "lgs2816crpsPortStatusIndex"),
)
if mibBuilder.loadTexts:
    lgs2816crpsPortStatusEntry.setStatus("current")


class _Lgs2816crpsPortStatusIndex_Type(Integer32):
    """Custom type lgs2816crpsPortStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Lgs2816crpsPortStatusIndex_Type.__name__ = "Integer32"
_Lgs2816crpsPortStatusIndex_Object = MibTableColumn
lgs2816crpsPortStatusIndex = _Lgs2816crpsPortStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 9, 1, 2, 1, 1),
    _Lgs2816crpsPortStatusIndex_Type()
)
lgs2816crpsPortStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsPortStatusIndex.setStatus("current")
_Lgs2816crpsPortStatusMedia_Type = DisplayString
_Lgs2816crpsPortStatusMedia_Object = MibTableColumn
lgs2816crpsPortStatusMedia = _Lgs2816crpsPortStatusMedia_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 9, 1, 2, 1, 2),
    _Lgs2816crpsPortStatusMedia_Type()
)
lgs2816crpsPortStatusMedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsPortStatusMedia.setStatus("current")
_Lgs2816crpsPortStatusPortState_Type = DisplayString
_Lgs2816crpsPortStatusPortState_Object = MibTableColumn
lgs2816crpsPortStatusPortState = _Lgs2816crpsPortStatusPortState_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 9, 1, 2, 1, 3),
    _Lgs2816crpsPortStatusPortState_Type()
)
lgs2816crpsPortStatusPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsPortStatusPortState.setStatus("current")
_Lgs2816crpsPortStatusLink_Type = DisplayString
_Lgs2816crpsPortStatusLink_Object = MibTableColumn
lgs2816crpsPortStatusLink = _Lgs2816crpsPortStatusLink_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 9, 1, 2, 1, 4),
    _Lgs2816crpsPortStatusLink_Type()
)
lgs2816crpsPortStatusLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsPortStatusLink.setStatus("current")
_Lgs2816crpsPortStatusAutoNego_Type = DisplayString
_Lgs2816crpsPortStatusAutoNego_Object = MibTableColumn
lgs2816crpsPortStatusAutoNego = _Lgs2816crpsPortStatusAutoNego_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 9, 1, 2, 1, 5),
    _Lgs2816crpsPortStatusAutoNego_Type()
)
lgs2816crpsPortStatusAutoNego.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsPortStatusAutoNego.setStatus("current")
_Lgs2816crpsPortStatusSpdDpx_Type = DisplayString
_Lgs2816crpsPortStatusSpdDpx_Object = MibTableColumn
lgs2816crpsPortStatusSpdDpx = _Lgs2816crpsPortStatusSpdDpx_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 9, 1, 2, 1, 6),
    _Lgs2816crpsPortStatusSpdDpx_Type()
)
lgs2816crpsPortStatusSpdDpx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsPortStatusSpdDpx.setStatus("current")
_Lgs2816crpsPortStatusFlwCtrlRx_Type = DisplayString
_Lgs2816crpsPortStatusFlwCtrlRx_Object = MibTableColumn
lgs2816crpsPortStatusFlwCtrlRx = _Lgs2816crpsPortStatusFlwCtrlRx_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 9, 1, 2, 1, 7),
    _Lgs2816crpsPortStatusFlwCtrlRx_Type()
)
lgs2816crpsPortStatusFlwCtrlRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsPortStatusFlwCtrlRx.setStatus("current")
_Lgs2816crpsPortStatusFlwCtrlTx_Type = DisplayString
_Lgs2816crpsPortStatusFlwCtrlTx_Object = MibTableColumn
lgs2816crpsPortStatusFlwCtrlTx = _Lgs2816crpsPortStatusFlwCtrlTx_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 9, 1, 2, 1, 8),
    _Lgs2816crpsPortStatusFlwCtrlTx_Type()
)
lgs2816crpsPortStatusFlwCtrlTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsPortStatusFlwCtrlTx.setStatus("current")
_Lgs2816crpsPortStatuDescription_Type = DisplayString
_Lgs2816crpsPortStatuDescription_Object = MibTableColumn
lgs2816crpsPortStatuDescription = _Lgs2816crpsPortStatuDescription_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 9, 1, 2, 1, 9),
    _Lgs2816crpsPortStatuDescription_Type()
)
lgs2816crpsPortStatuDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsPortStatuDescription.setStatus("current")
_Lgs2816crpsPortConf_ObjectIdentity = ObjectIdentity
lgs2816crpsPortConf = _Lgs2816crpsPortConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 9, 2)
)


class _Lgs2816crpsPortConfNumber_Type(Integer32):
    """Custom type lgs2816crpsPortConfNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Lgs2816crpsPortConfNumber_Type.__name__ = "Integer32"
_Lgs2816crpsPortConfNumber_Object = MibScalar
lgs2816crpsPortConfNumber = _Lgs2816crpsPortConfNumber_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 9, 2, 1),
    _Lgs2816crpsPortConfNumber_Type()
)
lgs2816crpsPortConfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsPortConfNumber.setStatus("current")
_Lgs2816crpsPortConfTable_Object = MibTable
lgs2816crpsPortConfTable = _Lgs2816crpsPortConfTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 9, 2, 2)
)
if mibBuilder.loadTexts:
    lgs2816crpsPortConfTable.setStatus("current")
_Lgs2816crpsPortConfEntry_Object = MibTableRow
lgs2816crpsPortConfEntry = _Lgs2816crpsPortConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 9, 2, 2, 1)
)
lgs2816crpsPortConfEntry.setIndexNames(
    (0, "PRIVATE-LGS2816CRPS-MIB", "lgs2816crpsPortConfIndex"),
)
if mibBuilder.loadTexts:
    lgs2816crpsPortConfEntry.setStatus("current")


class _Lgs2816crpsPortConfIndex_Type(Integer32):
    """Custom type lgs2816crpsPortConfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Lgs2816crpsPortConfIndex_Type.__name__ = "Integer32"
_Lgs2816crpsPortConfIndex_Object = MibTableColumn
lgs2816crpsPortConfIndex = _Lgs2816crpsPortConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 9, 2, 2, 1, 1),
    _Lgs2816crpsPortConfIndex_Type()
)
lgs2816crpsPortConfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsPortConfIndex.setStatus("current")


class _Lgs2816crpsPortConfPortState_Type(Integer32):
    """Custom type lgs2816crpsPortConfPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2816crpsPortConfPortState_Type.__name__ = "Integer32"
_Lgs2816crpsPortConfPortState_Object = MibTableColumn
lgs2816crpsPortConfPortState = _Lgs2816crpsPortConfPortState_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 9, 2, 2, 1, 2),
    _Lgs2816crpsPortConfPortState_Type()
)
lgs2816crpsPortConfPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsPortConfPortState.setStatus("current")


class _Lgs2816crpsPortConfTPSpdDpx_Type(Integer32):
    """Custom type lgs2816crpsPortConfTPSpdDpx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_Lgs2816crpsPortConfTPSpdDpx_Type.__name__ = "Integer32"
_Lgs2816crpsPortConfTPSpdDpx_Object = MibTableColumn
lgs2816crpsPortConfTPSpdDpx = _Lgs2816crpsPortConfTPSpdDpx_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 9, 2, 2, 1, 3),
    _Lgs2816crpsPortConfTPSpdDpx_Type()
)
lgs2816crpsPortConfTPSpdDpx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsPortConfTPSpdDpx.setStatus("current")


class _Lgs2816crpsPortConfSFPSpdDpx_Type(Integer32):
    """Custom type lgs2816crpsPortConfSFPSpdDpx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(4, 4),
        ValueRangeConstraint(5, 5),
    )


_Lgs2816crpsPortConfSFPSpdDpx_Type.__name__ = "Integer32"
_Lgs2816crpsPortConfSFPSpdDpx_Object = MibTableColumn
lgs2816crpsPortConfSFPSpdDpx = _Lgs2816crpsPortConfSFPSpdDpx_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 9, 2, 2, 1, 4),
    _Lgs2816crpsPortConfSFPSpdDpx_Type()
)
lgs2816crpsPortConfSFPSpdDpx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsPortConfSFPSpdDpx.setStatus("current")


class _Lgs2816crpsPortConfFlwCtrl_Type(Integer32):
    """Custom type lgs2816crpsPortConfFlwCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2816crpsPortConfFlwCtrl_Type.__name__ = "Integer32"
_Lgs2816crpsPortConfFlwCtrl_Object = MibTableColumn
lgs2816crpsPortConfFlwCtrl = _Lgs2816crpsPortConfFlwCtrl_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 9, 2, 2, 1, 5),
    _Lgs2816crpsPortConfFlwCtrl_Type()
)
lgs2816crpsPortConfFlwCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsPortConfFlwCtrl.setStatus("current")


class _Lgs2816crpsPortConfExcessiveCollisionMode_Type(Integer32):
    """Custom type lgs2816crpsPortConfExcessiveCollisionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2816crpsPortConfExcessiveCollisionMode_Type.__name__ = "Integer32"
_Lgs2816crpsPortConfExcessiveCollisionMode_Object = MibTableColumn
lgs2816crpsPortConfExcessiveCollisionMode = _Lgs2816crpsPortConfExcessiveCollisionMode_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 9, 2, 2, 1, 6),
    _Lgs2816crpsPortConfExcessiveCollisionMode_Type()
)
lgs2816crpsPortConfExcessiveCollisionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsPortConfExcessiveCollisionMode.setStatus("current")
_Lgs2816crpsPortConfDescription_Type = DisplayString
_Lgs2816crpsPortConfDescription_Object = MibTableColumn
lgs2816crpsPortConfDescription = _Lgs2816crpsPortConfDescription_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 9, 2, 2, 1, 7),
    _Lgs2816crpsPortConfDescription_Type()
)
lgs2816crpsPortConfDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsPortConfDescription.setStatus("current")


class _Lgs2816crpsPortConfPowerSaving_Type(Integer32):
    """Custom type lgs2816crpsPortConfPowerSaving based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2816crpsPortConfPowerSaving_Type.__name__ = "Integer32"
_Lgs2816crpsPortConfPowerSaving_Object = MibTableColumn
lgs2816crpsPortConfPowerSaving = _Lgs2816crpsPortConfPowerSaving_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 9, 2, 2, 1, 8),
    _Lgs2816crpsPortConfPowerSaving_Type()
)
lgs2816crpsPortConfPowerSaving.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsPortConfPowerSaving.setStatus("current")
_Lgs2816crpsSFPInfo_ObjectIdentity = ObjectIdentity
lgs2816crpsSFPInfo = _Lgs2816crpsSFPInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 9, 3)
)


class _Lgs2816crpsSFPInfoNumber_Type(Integer32):
    """Custom type lgs2816crpsSFPInfoNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Lgs2816crpsSFPInfoNumber_Type.__name__ = "Integer32"
_Lgs2816crpsSFPInfoNumber_Object = MibScalar
lgs2816crpsSFPInfoNumber = _Lgs2816crpsSFPInfoNumber_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 9, 3, 1),
    _Lgs2816crpsSFPInfoNumber_Type()
)
lgs2816crpsSFPInfoNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsSFPInfoNumber.setStatus("current")
_Lgs2816crpsSFPInfoTable_Object = MibTable
lgs2816crpsSFPInfoTable = _Lgs2816crpsSFPInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 9, 3, 2)
)
if mibBuilder.loadTexts:
    lgs2816crpsSFPInfoTable.setStatus("current")
_Lgs2816crpsSFPInfoEntry_Object = MibTableRow
lgs2816crpsSFPInfoEntry = _Lgs2816crpsSFPInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 9, 3, 2, 1)
)
lgs2816crpsSFPInfoEntry.setIndexNames(
    (0, "PRIVATE-LGS2816CRPS-MIB", "lgs2816crpsSFPInfoIndex"),
)
if mibBuilder.loadTexts:
    lgs2816crpsSFPInfoEntry.setStatus("current")


class _Lgs2816crpsSFPInfoIndex_Type(Integer32):
    """Custom type lgs2816crpsSFPInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Lgs2816crpsSFPInfoIndex_Type.__name__ = "Integer32"
_Lgs2816crpsSFPInfoIndex_Object = MibTableColumn
lgs2816crpsSFPInfoIndex = _Lgs2816crpsSFPInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 9, 3, 2, 1, 1),
    _Lgs2816crpsSFPInfoIndex_Type()
)
lgs2816crpsSFPInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsSFPInfoIndex.setStatus("current")
_Lgs2816crpsSFPConnectorType_Type = DisplayString
_Lgs2816crpsSFPConnectorType_Object = MibTableColumn
lgs2816crpsSFPConnectorType = _Lgs2816crpsSFPConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 9, 3, 2, 1, 2),
    _Lgs2816crpsSFPConnectorType_Type()
)
lgs2816crpsSFPConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsSFPConnectorType.setStatus("current")
_Lgs2816crpsSFPFiberType_Type = DisplayString
_Lgs2816crpsSFPFiberType_Object = MibTableColumn
lgs2816crpsSFPFiberType = _Lgs2816crpsSFPFiberType_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 9, 3, 2, 1, 3),
    _Lgs2816crpsSFPFiberType_Type()
)
lgs2816crpsSFPFiberType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsSFPFiberType.setStatus("current")
_Lgs2816crpsSFPWavelength_Type = DisplayString
_Lgs2816crpsSFPWavelength_Object = MibTableColumn
lgs2816crpsSFPWavelength = _Lgs2816crpsSFPWavelength_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 9, 3, 2, 1, 4),
    _Lgs2816crpsSFPWavelength_Type()
)
lgs2816crpsSFPWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsSFPWavelength.setStatus("current")
_Lgs2816crpsSFPBaudRate_Type = DisplayString
_Lgs2816crpsSFPBaudRate_Object = MibTableColumn
lgs2816crpsSFPBaudRate = _Lgs2816crpsSFPBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 9, 3, 2, 1, 5),
    _Lgs2816crpsSFPBaudRate_Type()
)
lgs2816crpsSFPBaudRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsSFPBaudRate.setStatus("current")
_Lgs2816crpsSFPVendorOUI_Type = DisplayString
_Lgs2816crpsSFPVendorOUI_Object = MibTableColumn
lgs2816crpsSFPVendorOUI = _Lgs2816crpsSFPVendorOUI_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 9, 3, 2, 1, 6),
    _Lgs2816crpsSFPVendorOUI_Type()
)
lgs2816crpsSFPVendorOUI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsSFPVendorOUI.setStatus("current")
_Lgs2816crpsSFPVendorName_Type = DisplayString
_Lgs2816crpsSFPVendorName_Object = MibTableColumn
lgs2816crpsSFPVendorName = _Lgs2816crpsSFPVendorName_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 9, 3, 2, 1, 7),
    _Lgs2816crpsSFPVendorName_Type()
)
lgs2816crpsSFPVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsSFPVendorName.setStatus("current")
_Lgs2816crpsSFPVendorPN_Type = DisplayString
_Lgs2816crpsSFPVendorPN_Object = MibTableColumn
lgs2816crpsSFPVendorPN = _Lgs2816crpsSFPVendorPN_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 9, 3, 2, 1, 8),
    _Lgs2816crpsSFPVendorPN_Type()
)
lgs2816crpsSFPVendorPN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsSFPVendorPN.setStatus("current")
_Lgs2816crpsSFPVendorRev_Type = DisplayString
_Lgs2816crpsSFPVendorRev_Object = MibTableColumn
lgs2816crpsSFPVendorRev = _Lgs2816crpsSFPVendorRev_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 9, 3, 2, 1, 9),
    _Lgs2816crpsSFPVendorRev_Type()
)
lgs2816crpsSFPVendorRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsSFPVendorRev.setStatus("current")
_Lgs2816crpsSFPVendorSN_Type = DisplayString
_Lgs2816crpsSFPVendorSN_Object = MibTableColumn
lgs2816crpsSFPVendorSN = _Lgs2816crpsSFPVendorSN_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 9, 3, 2, 1, 10),
    _Lgs2816crpsSFPVendorSN_Type()
)
lgs2816crpsSFPVendorSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsSFPVendorSN.setStatus("current")
_Lgs2816crpsSFPDateCode_Type = DisplayString
_Lgs2816crpsSFPDateCode_Object = MibTableColumn
lgs2816crpsSFPDateCode = _Lgs2816crpsSFPDateCode_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 9, 3, 2, 1, 11),
    _Lgs2816crpsSFPDateCode_Type()
)
lgs2816crpsSFPDateCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsSFPDateCode.setStatus("current")
_Lgs2816crpsSFPTemperature_Type = DisplayString
_Lgs2816crpsSFPTemperature_Object = MibTableColumn
lgs2816crpsSFPTemperature = _Lgs2816crpsSFPTemperature_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 9, 3, 2, 1, 12),
    _Lgs2816crpsSFPTemperature_Type()
)
lgs2816crpsSFPTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsSFPTemperature.setStatus("current")
_Lgs2816crpsSFPVcc_Type = DisplayString
_Lgs2816crpsSFPVcc_Object = MibTableColumn
lgs2816crpsSFPVcc = _Lgs2816crpsSFPVcc_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 9, 3, 2, 1, 13),
    _Lgs2816crpsSFPVcc_Type()
)
lgs2816crpsSFPVcc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsSFPVcc.setStatus("current")
_Lgs2816crpsSFPTxBias_Type = DisplayString
_Lgs2816crpsSFPTxBias_Object = MibTableColumn
lgs2816crpsSFPTxBias = _Lgs2816crpsSFPTxBias_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 9, 3, 2, 1, 14),
    _Lgs2816crpsSFPTxBias_Type()
)
lgs2816crpsSFPTxBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsSFPTxBias.setStatus("current")
_Lgs2816crpsSFPTxPWR_Type = DisplayString
_Lgs2816crpsSFPTxPWR_Object = MibTableColumn
lgs2816crpsSFPTxPWR = _Lgs2816crpsSFPTxPWR_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 9, 3, 2, 1, 15),
    _Lgs2816crpsSFPTxPWR_Type()
)
lgs2816crpsSFPTxPWR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsSFPTxPWR.setStatus("current")
_Lgs2816crpsSFPRxPWR_Type = DisplayString
_Lgs2816crpsSFPRxPWR_Object = MibTableColumn
lgs2816crpsSFPRxPWR = _Lgs2816crpsSFPRxPWR_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 9, 3, 2, 1, 16),
    _Lgs2816crpsSFPRxPWR_Type()
)
lgs2816crpsSFPRxPWR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsSFPRxPWR.setStatus("current")
_Lgs2816crpsMirror_ObjectIdentity = ObjectIdentity
lgs2816crpsMirror = _Lgs2816crpsMirror_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 10)
)


class _Lgs2816crpsMirroringPort_Type(Integer32):
    """Custom type lgs2816crpsMirroringPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Lgs2816crpsMirroringPort_Type.__name__ = "Integer32"
_Lgs2816crpsMirroringPort_Object = MibScalar
lgs2816crpsMirroringPort = _Lgs2816crpsMirroringPort_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 10, 1),
    _Lgs2816crpsMirroringPort_Type()
)
lgs2816crpsMirroringPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsMirroringPort.setStatus("current")
_Lgs2816crpsMirroredPortsTable_Object = MibTable
lgs2816crpsMirroredPortsTable = _Lgs2816crpsMirroredPortsTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 10, 2)
)
if mibBuilder.loadTexts:
    lgs2816crpsMirroredPortsTable.setStatus("current")
_Lgs2816crpsMirroredPortsEntry_Object = MibTableRow
lgs2816crpsMirroredPortsEntry = _Lgs2816crpsMirroredPortsEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 10, 2, 1)
)
lgs2816crpsMirroredPortsEntry.setIndexNames(
    (0, "PRIVATE-LGS2816CRPS-MIB", "lgs2816crpsMirroredPortIndex"),
)
if mibBuilder.loadTexts:
    lgs2816crpsMirroredPortsEntry.setStatus("current")


class _Lgs2816crpsMirroredPortIndex_Type(Integer32):
    """Custom type lgs2816crpsMirroredPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Lgs2816crpsMirroredPortIndex_Type.__name__ = "Integer32"
_Lgs2816crpsMirroredPortIndex_Object = MibTableColumn
lgs2816crpsMirroredPortIndex = _Lgs2816crpsMirroredPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 10, 2, 1, 1),
    _Lgs2816crpsMirroredPortIndex_Type()
)
lgs2816crpsMirroredPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsMirroredPortIndex.setStatus("current")


class _Lgs2816crpsMirroredPortSrouceEnable_Type(Integer32):
    """Custom type lgs2816crpsMirroredPortSrouceEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2816crpsMirroredPortSrouceEnable_Type.__name__ = "Integer32"
_Lgs2816crpsMirroredPortSrouceEnable_Object = MibTableColumn
lgs2816crpsMirroredPortSrouceEnable = _Lgs2816crpsMirroredPortSrouceEnable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 10, 2, 1, 2),
    _Lgs2816crpsMirroredPortSrouceEnable_Type()
)
lgs2816crpsMirroredPortSrouceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsMirroredPortSrouceEnable.setStatus("current")


class _Lgs2816crpsMirroredPortDestinationEnable_Type(Integer32):
    """Custom type lgs2816crpsMirroredPortDestinationEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2816crpsMirroredPortDestinationEnable_Type.__name__ = "Integer32"
_Lgs2816crpsMirroredPortDestinationEnable_Object = MibTableColumn
lgs2816crpsMirroredPortDestinationEnable = _Lgs2816crpsMirroredPortDestinationEnable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 10, 2, 1, 3),
    _Lgs2816crpsMirroredPortDestinationEnable_Type()
)
lgs2816crpsMirroredPortDestinationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsMirroredPortDestinationEnable.setStatus("current")
_Lgs2816crpsMaxPktLen_ObjectIdentity = ObjectIdentity
lgs2816crpsMaxPktLen = _Lgs2816crpsMaxPktLen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 11)
)


class _Lgs2816crpsMaxPktLenPortNumber_Type(Integer32):
    """Custom type lgs2816crpsMaxPktLenPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Lgs2816crpsMaxPktLenPortNumber_Type.__name__ = "Integer32"
_Lgs2816crpsMaxPktLenPortNumber_Object = MibScalar
lgs2816crpsMaxPktLenPortNumber = _Lgs2816crpsMaxPktLenPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 11, 1),
    _Lgs2816crpsMaxPktLenPortNumber_Type()
)
lgs2816crpsMaxPktLenPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsMaxPktLenPortNumber.setStatus("current")
_Lgs2816crpsMaxPktLenConfTable_Object = MibTable
lgs2816crpsMaxPktLenConfTable = _Lgs2816crpsMaxPktLenConfTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 11, 2)
)
if mibBuilder.loadTexts:
    lgs2816crpsMaxPktLenConfTable.setStatus("current")
_Lgs2816crpsMaxPktLenConfEntry_Object = MibTableRow
lgs2816crpsMaxPktLenConfEntry = _Lgs2816crpsMaxPktLenConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 11, 2, 1)
)
lgs2816crpsMaxPktLenConfEntry.setIndexNames(
    (0, "PRIVATE-LGS2816CRPS-MIB", "lgs2816crpsMaxPktLenConfIndex"),
)
if mibBuilder.loadTexts:
    lgs2816crpsMaxPktLenConfEntry.setStatus("current")


class _Lgs2816crpsMaxPktLenConfIndex_Type(Integer32):
    """Custom type lgs2816crpsMaxPktLenConfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Lgs2816crpsMaxPktLenConfIndex_Type.__name__ = "Integer32"
_Lgs2816crpsMaxPktLenConfIndex_Object = MibTableColumn
lgs2816crpsMaxPktLenConfIndex = _Lgs2816crpsMaxPktLenConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 11, 2, 1, 1),
    _Lgs2816crpsMaxPktLenConfIndex_Type()
)
lgs2816crpsMaxPktLenConfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsMaxPktLenConfIndex.setStatus("current")


class _Lgs2816crpsMaxPktLenConfSetting_Type(Integer32):
    """Custom type lgs2816crpsMaxPktLenConfSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1518, 9600),
    )


_Lgs2816crpsMaxPktLenConfSetting_Type.__name__ = "Integer32"
_Lgs2816crpsMaxPktLenConfSetting_Object = MibTableColumn
lgs2816crpsMaxPktLenConfSetting = _Lgs2816crpsMaxPktLenConfSetting_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 11, 2, 1, 2),
    _Lgs2816crpsMaxPktLenConfSetting_Type()
)
lgs2816crpsMaxPktLenConfSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsMaxPktLenConfSetting.setStatus("current")
_Lgs2816crpsLoopDetectedConf_ObjectIdentity = ObjectIdentity
lgs2816crpsLoopDetectedConf = _Lgs2816crpsLoopDetectedConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 12)
)


class _Lgs2816crpsLoopDetectedNumber_Type(Integer32):
    """Custom type lgs2816crpsLoopDetectedNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Lgs2816crpsLoopDetectedNumber_Type.__name__ = "Integer32"
_Lgs2816crpsLoopDetectedNumber_Object = MibScalar
lgs2816crpsLoopDetectedNumber = _Lgs2816crpsLoopDetectedNumber_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 12, 1),
    _Lgs2816crpsLoopDetectedNumber_Type()
)
lgs2816crpsLoopDetectedNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsLoopDetectedNumber.setStatus("current")
_Lgs2816crpsLoopDetectedTable_Object = MibTable
lgs2816crpsLoopDetectedTable = _Lgs2816crpsLoopDetectedTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 12, 2)
)
if mibBuilder.loadTexts:
    lgs2816crpsLoopDetectedTable.setStatus("current")
_Lgs2816crpsLoopDetectedEntry_Object = MibTableRow
lgs2816crpsLoopDetectedEntry = _Lgs2816crpsLoopDetectedEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 12, 2, 1)
)
lgs2816crpsLoopDetectedEntry.setIndexNames(
    (0, "PRIVATE-LGS2816CRPS-MIB", "lgs2816crpsLoopDetectedfIndex"),
)
if mibBuilder.loadTexts:
    lgs2816crpsLoopDetectedEntry.setStatus("current")


class _Lgs2816crpsLoopDetectedfIndex_Type(Integer32):
    """Custom type lgs2816crpsLoopDetectedfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Lgs2816crpsLoopDetectedfIndex_Type.__name__ = "Integer32"
_Lgs2816crpsLoopDetectedfIndex_Object = MibTableColumn
lgs2816crpsLoopDetectedfIndex = _Lgs2816crpsLoopDetectedfIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 12, 2, 1, 1),
    _Lgs2816crpsLoopDetectedfIndex_Type()
)
lgs2816crpsLoopDetectedfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsLoopDetectedfIndex.setStatus("current")


class _Lgs2816crpsLoopDetectedPort_Type(Integer32):
    """Custom type lgs2816crpsLoopDetectedPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2816crpsLoopDetectedPort_Type.__name__ = "Integer32"
_Lgs2816crpsLoopDetectedPort_Object = MibTableColumn
lgs2816crpsLoopDetectedPort = _Lgs2816crpsLoopDetectedPort_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 12, 2, 1, 2),
    _Lgs2816crpsLoopDetectedPort_Type()
)
lgs2816crpsLoopDetectedPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsLoopDetectedPort.setStatus("current")


class _Lgs2816crpsLoopDetectedLockedPort_Type(Integer32):
    """Custom type lgs2816crpsLoopDetectedLockedPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2816crpsLoopDetectedLockedPort_Type.__name__ = "Integer32"
_Lgs2816crpsLoopDetectedLockedPort_Object = MibTableColumn
lgs2816crpsLoopDetectedLockedPort = _Lgs2816crpsLoopDetectedLockedPort_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 12, 2, 1, 3),
    _Lgs2816crpsLoopDetectedLockedPort_Type()
)
lgs2816crpsLoopDetectedLockedPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsLoopDetectedLockedPort.setStatus("current")
_Lgs2816crpsManagementPolicy_ObjectIdentity = ObjectIdentity
lgs2816crpsManagementPolicy = _Lgs2816crpsManagementPolicy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 13)
)


class _Lgs2816crpsManagementSecurityNumber_Type(Integer32):
    """Custom type lgs2816crpsManagementSecurityNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_Lgs2816crpsManagementSecurityNumber_Type.__name__ = "Integer32"
_Lgs2816crpsManagementSecurityNumber_Object = MibScalar
lgs2816crpsManagementSecurityNumber = _Lgs2816crpsManagementSecurityNumber_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 13, 1),
    _Lgs2816crpsManagementSecurityNumber_Type()
)
lgs2816crpsManagementSecurityNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsManagementSecurityNumber.setStatus("current")


class _Lgs2816crpsManagementSecurityEntryCreate_Type(Integer32):
    """Custom type lgs2816crpsManagementSecurityEntryCreate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_Lgs2816crpsManagementSecurityEntryCreate_Type.__name__ = "Integer32"
_Lgs2816crpsManagementSecurityEntryCreate_Object = MibScalar
lgs2816crpsManagementSecurityEntryCreate = _Lgs2816crpsManagementSecurityEntryCreate_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 13, 2),
    _Lgs2816crpsManagementSecurityEntryCreate_Type()
)
lgs2816crpsManagementSecurityEntryCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsManagementSecurityEntryCreate.setStatus("current")
_Lgs2816crpsManagementSecurityTable_Object = MibTable
lgs2816crpsManagementSecurityTable = _Lgs2816crpsManagementSecurityTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 13, 3)
)
if mibBuilder.loadTexts:
    lgs2816crpsManagementSecurityTable.setStatus("current")
_Lgs2816crpsManagementSecurityEntry_Object = MibTableRow
lgs2816crpsManagementSecurityEntry = _Lgs2816crpsManagementSecurityEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 13, 3, 1)
)
lgs2816crpsManagementSecurityEntry.setIndexNames(
    (0, "PRIVATE-LGS2816CRPS-MIB", "lgs2816crpsManagementSecurityIndex"),
)
if mibBuilder.loadTexts:
    lgs2816crpsManagementSecurityEntry.setStatus("current")


class _Lgs2816crpsManagementSecurityIndex_Type(Integer32):
    """Custom type lgs2816crpsManagementSecurityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Lgs2816crpsManagementSecurityIndex_Type.__name__ = "Integer32"
_Lgs2816crpsManagementSecurityIndex_Object = MibTableColumn
lgs2816crpsManagementSecurityIndex = _Lgs2816crpsManagementSecurityIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 13, 3, 1, 1),
    _Lgs2816crpsManagementSecurityIndex_Type()
)
lgs2816crpsManagementSecurityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsManagementSecurityIndex.setStatus("current")
_Lgs2816crpsManagementSecurityName_Type = DisplayString
_Lgs2816crpsManagementSecurityName_Object = MibTableColumn
lgs2816crpsManagementSecurityName = _Lgs2816crpsManagementSecurityName_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 13, 3, 1, 2),
    _Lgs2816crpsManagementSecurityName_Type()
)
lgs2816crpsManagementSecurityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsManagementSecurityName.setStatus("current")
_Lgs2816crpsManagementSecurityIpRange_Type = DisplayString
_Lgs2816crpsManagementSecurityIpRange_Object = MibTableColumn
lgs2816crpsManagementSecurityIpRange = _Lgs2816crpsManagementSecurityIpRange_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 13, 3, 1, 3),
    _Lgs2816crpsManagementSecurityIpRange_Type()
)
lgs2816crpsManagementSecurityIpRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsManagementSecurityIpRange.setStatus("current")
_Lgs2816crpsManagementSecurityIncomigPort_Type = DisplayString
_Lgs2816crpsManagementSecurityIncomigPort_Object = MibTableColumn
lgs2816crpsManagementSecurityIncomigPort = _Lgs2816crpsManagementSecurityIncomigPort_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 13, 3, 1, 4),
    _Lgs2816crpsManagementSecurityIncomigPort_Type()
)
lgs2816crpsManagementSecurityIncomigPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsManagementSecurityIncomigPort.setStatus("current")
_Lgs2816crpsManagementSecurityAccessType_Type = DisplayString
_Lgs2816crpsManagementSecurityAccessType_Object = MibTableColumn
lgs2816crpsManagementSecurityAccessType = _Lgs2816crpsManagementSecurityAccessType_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 13, 3, 1, 5),
    _Lgs2816crpsManagementSecurityAccessType_Type()
)
lgs2816crpsManagementSecurityAccessType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsManagementSecurityAccessType.setStatus("current")


class _Lgs2816crpsManagementSecurityAction_Type(Integer32):
    """Custom type lgs2816crpsManagementSecurityAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2816crpsManagementSecurityAction_Type.__name__ = "Integer32"
_Lgs2816crpsManagementSecurityAction_Object = MibTableColumn
lgs2816crpsManagementSecurityAction = _Lgs2816crpsManagementSecurityAction_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 13, 3, 1, 6),
    _Lgs2816crpsManagementSecurityAction_Type()
)
lgs2816crpsManagementSecurityAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsManagementSecurityAction.setStatus("current")


class _Lgs2816crpsManagementSecurityEntryAction_Type(Integer32):
    """Custom type lgs2816crpsManagementSecurityEntryAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Lgs2816crpsManagementSecurityEntryAction_Type.__name__ = "Integer32"
_Lgs2816crpsManagementSecurityEntryAction_Object = MibTableColumn
lgs2816crpsManagementSecurityEntryAction = _Lgs2816crpsManagementSecurityEntryAction_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 13, 3, 1, 7),
    _Lgs2816crpsManagementSecurityEntryAction_Type()
)
lgs2816crpsManagementSecurityEntryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsManagementSecurityEntryAction.setStatus("current")
_Lgs2816crpsVLAN_ObjectIdentity = ObjectIdentity
lgs2816crpsVLAN = _Lgs2816crpsVLAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 14)
)
_Lgs2816crpsVlanConf_ObjectIdentity = ObjectIdentity
lgs2816crpsVlanConf = _Lgs2816crpsVlanConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 14, 1)
)


class _Lgs2816crpsVlanMode_Type(Integer32):
    """Custom type lgs2816crpsVlanMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2816crpsVlanMode_Type.__name__ = "Integer32"
_Lgs2816crpsVlanMode_Object = MibScalar
lgs2816crpsVlanMode = _Lgs2816crpsVlanMode_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 14, 1, 1),
    _Lgs2816crpsVlanMode_Type()
)
lgs2816crpsVlanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsVlanMode.setStatus("current")


class _Lgs2816crpsManagementVlan_Type(Integer32):
    """Custom type lgs2816crpsManagementVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Lgs2816crpsManagementVlan_Type.__name__ = "Integer32"
_Lgs2816crpsManagementVlan_Object = MibScalar
lgs2816crpsManagementVlan = _Lgs2816crpsManagementVlan_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 14, 1, 2),
    _Lgs2816crpsManagementVlan_Type()
)
lgs2816crpsManagementVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsManagementVlan.setStatus("current")
_Lgs2816crpsPortIsolation_Type = DisplayString
_Lgs2816crpsPortIsolation_Object = MibScalar
lgs2816crpsPortIsolation = _Lgs2816crpsPortIsolation_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 14, 1, 3),
    _Lgs2816crpsPortIsolation_Type()
)
lgs2816crpsPortIsolation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsPortIsolation.setStatus("current")


class _Lgs2816crpsTagIdentifier_Type(Integer32):
    """Custom type lgs2816crpsTagIdentifier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2816crpsTagIdentifier_Type.__name__ = "Integer32"
_Lgs2816crpsTagIdentifier_Object = MibScalar
lgs2816crpsTagIdentifier = _Lgs2816crpsTagIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 14, 1, 4),
    _Lgs2816crpsTagIdentifier_Type()
)
lgs2816crpsTagIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsTagIdentifier.setStatus("current")
_Lgs2816crpsTagBaseVlanGroup_ObjectIdentity = ObjectIdentity
lgs2816crpsTagBaseVlanGroup = _Lgs2816crpsTagBaseVlanGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 14, 2)
)


class _Lgs2816crpsTagBaseVlanNumber_Type(Integer32):
    """Custom type lgs2816crpsTagBaseVlanNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Lgs2816crpsTagBaseVlanNumber_Type.__name__ = "Integer32"
_Lgs2816crpsTagBaseVlanNumber_Object = MibScalar
lgs2816crpsTagBaseVlanNumber = _Lgs2816crpsTagBaseVlanNumber_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 14, 2, 1),
    _Lgs2816crpsTagBaseVlanNumber_Type()
)
lgs2816crpsTagBaseVlanNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsTagBaseVlanNumber.setStatus("current")


class _Lgs2816crpsTagBaseVlanGroupEntryCreate_Type(Integer32):
    """Custom type lgs2816crpsTagBaseVlanGroupEntryCreate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Lgs2816crpsTagBaseVlanGroupEntryCreate_Type.__name__ = "Integer32"
_Lgs2816crpsTagBaseVlanGroupEntryCreate_Object = MibScalar
lgs2816crpsTagBaseVlanGroupEntryCreate = _Lgs2816crpsTagBaseVlanGroupEntryCreate_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 14, 2, 2),
    _Lgs2816crpsTagBaseVlanGroupEntryCreate_Type()
)
lgs2816crpsTagBaseVlanGroupEntryCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsTagBaseVlanGroupEntryCreate.setStatus("current")
_Lgs2816crpsTagBaseVlanGroupTable_Object = MibTable
lgs2816crpsTagBaseVlanGroupTable = _Lgs2816crpsTagBaseVlanGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 14, 2, 3)
)
if mibBuilder.loadTexts:
    lgs2816crpsTagBaseVlanGroupTable.setStatus("current")
_Lgs2816crpsTagBaseVlanGroupEntry_Object = MibTableRow
lgs2816crpsTagBaseVlanGroupEntry = _Lgs2816crpsTagBaseVlanGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 14, 2, 3, 1)
)
lgs2816crpsTagBaseVlanGroupEntry.setIndexNames(
    (0, "PRIVATE-LGS2816CRPS-MIB", "lgs2816crpsTagBaseVlanVid"),
)
if mibBuilder.loadTexts:
    lgs2816crpsTagBaseVlanGroupEntry.setStatus("current")


class _Lgs2816crpsTagBaseVlanVid_Type(Integer32):
    """Custom type lgs2816crpsTagBaseVlanVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Lgs2816crpsTagBaseVlanVid_Type.__name__ = "Integer32"
_Lgs2816crpsTagBaseVlanVid_Object = MibTableColumn
lgs2816crpsTagBaseVlanVid = _Lgs2816crpsTagBaseVlanVid_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 14, 2, 3, 1, 1),
    _Lgs2816crpsTagBaseVlanVid_Type()
)
lgs2816crpsTagBaseVlanVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgs2816crpsTagBaseVlanVid.setStatus("current")
_Lgs2816crpsTagBaseVlanName_Type = DisplayString
_Lgs2816crpsTagBaseVlanName_Object = MibTableColumn
lgs2816crpsTagBaseVlanName = _Lgs2816crpsTagBaseVlanName_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 14, 2, 3, 1, 2),
    _Lgs2816crpsTagBaseVlanName_Type()
)
lgs2816crpsTagBaseVlanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsTagBaseVlanName.setStatus("current")


class _Lgs2816crpsTagBaseVlanIgmpProxy_Type(Integer32):
    """Custom type lgs2816crpsTagBaseVlanIgmpProxy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2816crpsTagBaseVlanIgmpProxy_Type.__name__ = "Integer32"
_Lgs2816crpsTagBaseVlanIgmpProxy_Object = MibTableColumn
lgs2816crpsTagBaseVlanIgmpProxy = _Lgs2816crpsTagBaseVlanIgmpProxy_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 14, 2, 3, 1, 3),
    _Lgs2816crpsTagBaseVlanIgmpProxy_Type()
)
lgs2816crpsTagBaseVlanIgmpProxy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsTagBaseVlanIgmpProxy.setStatus("current")


class _Lgs2816crpsTagBaseVlanPrivateVlan_Type(Integer32):
    """Custom type lgs2816crpsTagBaseVlanPrivateVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2816crpsTagBaseVlanPrivateVlan_Type.__name__ = "Integer32"
_Lgs2816crpsTagBaseVlanPrivateVlan_Object = MibTableColumn
lgs2816crpsTagBaseVlanPrivateVlan = _Lgs2816crpsTagBaseVlanPrivateVlan_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 14, 2, 3, 1, 4),
    _Lgs2816crpsTagBaseVlanPrivateVlan_Type()
)
lgs2816crpsTagBaseVlanPrivateVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsTagBaseVlanPrivateVlan.setStatus("current")


class _Lgs2816crpsTagBaseVlanGvrp_Type(Integer32):
    """Custom type lgs2816crpsTagBaseVlanGvrp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2816crpsTagBaseVlanGvrp_Type.__name__ = "Integer32"
_Lgs2816crpsTagBaseVlanGvrp_Object = MibTableColumn
lgs2816crpsTagBaseVlanGvrp = _Lgs2816crpsTagBaseVlanGvrp_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 14, 2, 3, 1, 5),
    _Lgs2816crpsTagBaseVlanGvrp_Type()
)
lgs2816crpsTagBaseVlanGvrp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsTagBaseVlanGvrp.setStatus("current")
_Lgs2816crpsTagBaseVlanMemberPort_Type = DisplayString
_Lgs2816crpsTagBaseVlanMemberPort_Object = MibTableColumn
lgs2816crpsTagBaseVlanMemberPort = _Lgs2816crpsTagBaseVlanMemberPort_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 14, 2, 3, 1, 6),
    _Lgs2816crpsTagBaseVlanMemberPort_Type()
)
lgs2816crpsTagBaseVlanMemberPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsTagBaseVlanMemberPort.setStatus("current")


class _Lgs2816crpsTagBaseVlanEntryAction_Type(Integer32):
    """Custom type lgs2816crpsTagBaseVlanEntryAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Lgs2816crpsTagBaseVlanEntryAction_Type.__name__ = "Integer32"
_Lgs2816crpsTagBaseVlanEntryAction_Object = MibTableColumn
lgs2816crpsTagBaseVlanEntryAction = _Lgs2816crpsTagBaseVlanEntryAction_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 14, 2, 3, 1, 7),
    _Lgs2816crpsTagBaseVlanEntryAction_Type()
)
lgs2816crpsTagBaseVlanEntryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsTagBaseVlanEntryAction.setStatus("current")
_Lgs2816crpsVlanPortConfTable_Object = MibTable
lgs2816crpsVlanPortConfTable = _Lgs2816crpsVlanPortConfTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 14, 3)
)
if mibBuilder.loadTexts:
    lgs2816crpsVlanPortConfTable.setStatus("current")
_Lgs2816crpsVlanPortConfEntry_Object = MibTableRow
lgs2816crpsVlanPortConfEntry = _Lgs2816crpsVlanPortConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 14, 3, 1)
)
lgs2816crpsVlanPortConfEntry.setIndexNames(
    (0, "PRIVATE-LGS2816CRPS-MIB", "lgs2816crpsVlanPortConfIndex"),
)
if mibBuilder.loadTexts:
    lgs2816crpsVlanPortConfEntry.setStatus("current")


class _Lgs2816crpsVlanPortConfIndex_Type(Integer32):
    """Custom type lgs2816crpsVlanPortConfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Lgs2816crpsVlanPortConfIndex_Type.__name__ = "Integer32"
_Lgs2816crpsVlanPortConfIndex_Object = MibTableColumn
lgs2816crpsVlanPortConfIndex = _Lgs2816crpsVlanPortConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 14, 3, 1, 1),
    _Lgs2816crpsVlanPortConfIndex_Type()
)
lgs2816crpsVlanPortConfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgs2816crpsVlanPortConfIndex.setStatus("current")


class _Lgs2816crpsVlanPortConfVlanAware_Type(Integer32):
    """Custom type lgs2816crpsVlanPortConfVlanAware based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2816crpsVlanPortConfVlanAware_Type.__name__ = "Integer32"
_Lgs2816crpsVlanPortConfVlanAware_Object = MibTableColumn
lgs2816crpsVlanPortConfVlanAware = _Lgs2816crpsVlanPortConfVlanAware_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 14, 3, 1, 2),
    _Lgs2816crpsVlanPortConfVlanAware_Type()
)
lgs2816crpsVlanPortConfVlanAware.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsVlanPortConfVlanAware.setStatus("current")


class _Lgs2816crpsVlanPortConfIngressFiltering_Type(Integer32):
    """Custom type lgs2816crpsVlanPortConfIngressFiltering based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2816crpsVlanPortConfIngressFiltering_Type.__name__ = "Integer32"
_Lgs2816crpsVlanPortConfIngressFiltering_Object = MibTableColumn
lgs2816crpsVlanPortConfIngressFiltering = _Lgs2816crpsVlanPortConfIngressFiltering_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 14, 3, 1, 3),
    _Lgs2816crpsVlanPortConfIngressFiltering_Type()
)
lgs2816crpsVlanPortConfIngressFiltering.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsVlanPortConfIngressFiltering.setStatus("current")


class _Lgs2816crpsVlanPortConfFrameType_Type(Integer32):
    """Custom type lgs2816crpsVlanPortConfFrameType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2816crpsVlanPortConfFrameType_Type.__name__ = "Integer32"
_Lgs2816crpsVlanPortConfFrameType_Object = MibTableColumn
lgs2816crpsVlanPortConfFrameType = _Lgs2816crpsVlanPortConfFrameType_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 14, 3, 1, 4),
    _Lgs2816crpsVlanPortConfFrameType_Type()
)
lgs2816crpsVlanPortConfFrameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsVlanPortConfFrameType.setStatus("current")


class _Lgs2816crpsVlanPortConfPvid_Type(Integer32):
    """Custom type lgs2816crpsVlanPortConfPvid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Lgs2816crpsVlanPortConfPvid_Type.__name__ = "Integer32"
_Lgs2816crpsVlanPortConfPvid_Object = MibTableColumn
lgs2816crpsVlanPortConfPvid = _Lgs2816crpsVlanPortConfPvid_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 14, 3, 1, 5),
    _Lgs2816crpsVlanPortConfPvid_Type()
)
lgs2816crpsVlanPortConfPvid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsVlanPortConfPvid.setStatus("current")


class _Lgs2816crpsVlanPortConfRole_Type(Integer32):
    """Custom type lgs2816crpsVlanPortConfRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Lgs2816crpsVlanPortConfRole_Type.__name__ = "Integer32"
_Lgs2816crpsVlanPortConfRole_Object = MibTableColumn
lgs2816crpsVlanPortConfRole = _Lgs2816crpsVlanPortConfRole_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 14, 3, 1, 6),
    _Lgs2816crpsVlanPortConfRole_Type()
)
lgs2816crpsVlanPortConfRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsVlanPortConfRole.setStatus("current")


class _Lgs2816crpsVlanPortConfUntagVid_Type(Integer32):
    """Custom type lgs2816crpsVlanPortConfUntagVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Lgs2816crpsVlanPortConfUntagVid_Type.__name__ = "Integer32"
_Lgs2816crpsVlanPortConfUntagVid_Object = MibTableColumn
lgs2816crpsVlanPortConfUntagVid = _Lgs2816crpsVlanPortConfUntagVid_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 14, 3, 1, 7),
    _Lgs2816crpsVlanPortConfUntagVid_Type()
)
lgs2816crpsVlanPortConfUntagVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsVlanPortConfUntagVid.setStatus("current")


class _Lgs2816crpsVlanPortConfDoubleTag_Type(Integer32):
    """Custom type lgs2816crpsVlanPortConfDoubleTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Lgs2816crpsVlanPortConfDoubleTag_Type.__name__ = "Integer32"
_Lgs2816crpsVlanPortConfDoubleTag_Object = MibTableColumn
lgs2816crpsVlanPortConfDoubleTag = _Lgs2816crpsVlanPortConfDoubleTag_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 14, 3, 1, 8),
    _Lgs2816crpsVlanPortConfDoubleTag_Type()
)
lgs2816crpsVlanPortConfDoubleTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsVlanPortConfDoubleTag.setStatus("current")
_Lgs2816crpsPortBaseVlanGroup_ObjectIdentity = ObjectIdentity
lgs2816crpsPortBaseVlanGroup = _Lgs2816crpsPortBaseVlanGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 14, 4)
)


class _Lgs2816crpsPortBaseVlanNumber_Type(Integer32):
    """Custom type lgs2816crpsPortBaseVlanNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Lgs2816crpsPortBaseVlanNumber_Type.__name__ = "Integer32"
_Lgs2816crpsPortBaseVlanNumber_Object = MibScalar
lgs2816crpsPortBaseVlanNumber = _Lgs2816crpsPortBaseVlanNumber_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 14, 4, 1),
    _Lgs2816crpsPortBaseVlanNumber_Type()
)
lgs2816crpsPortBaseVlanNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsPortBaseVlanNumber.setStatus("current")


class _Lgs2816crpsPortBaseVlanGroupEntryCreate_Type(Integer32):
    """Custom type lgs2816crpsPortBaseVlanGroupEntryCreate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_Lgs2816crpsPortBaseVlanGroupEntryCreate_Type.__name__ = "Integer32"
_Lgs2816crpsPortBaseVlanGroupEntryCreate_Object = MibScalar
lgs2816crpsPortBaseVlanGroupEntryCreate = _Lgs2816crpsPortBaseVlanGroupEntryCreate_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 14, 4, 2),
    _Lgs2816crpsPortBaseVlanGroupEntryCreate_Type()
)
lgs2816crpsPortBaseVlanGroupEntryCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsPortBaseVlanGroupEntryCreate.setStatus("current")
_Lgs2816crpsPortBaseVlanGroupTable_Object = MibTable
lgs2816crpsPortBaseVlanGroupTable = _Lgs2816crpsPortBaseVlanGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 14, 4, 3)
)
if mibBuilder.loadTexts:
    lgs2816crpsPortBaseVlanGroupTable.setStatus("current")
_Lgs2816crpsPortBaseVlanGroupEntry_Object = MibTableRow
lgs2816crpsPortBaseVlanGroupEntry = _Lgs2816crpsPortBaseVlanGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 14, 4, 3, 1)
)
lgs2816crpsPortBaseVlanGroupEntry.setIndexNames(
    (0, "PRIVATE-LGS2816CRPS-MIB", "lgs2816crpsPortBaseVlanGroupIndex"),
)
if mibBuilder.loadTexts:
    lgs2816crpsPortBaseVlanGroupEntry.setStatus("current")


class _Lgs2816crpsPortBaseVlanGroupIndex_Type(Integer32):
    """Custom type lgs2816crpsPortBaseVlanGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Lgs2816crpsPortBaseVlanGroupIndex_Type.__name__ = "Integer32"
_Lgs2816crpsPortBaseVlanGroupIndex_Object = MibTableColumn
lgs2816crpsPortBaseVlanGroupIndex = _Lgs2816crpsPortBaseVlanGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 14, 4, 3, 1, 1),
    _Lgs2816crpsPortBaseVlanGroupIndex_Type()
)
lgs2816crpsPortBaseVlanGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgs2816crpsPortBaseVlanGroupIndex.setStatus("current")
_Lgs2816crpsPortBaseVlanGroupName_Type = DisplayString
_Lgs2816crpsPortBaseVlanGroupName_Object = MibTableColumn
lgs2816crpsPortBaseVlanGroupName = _Lgs2816crpsPortBaseVlanGroupName_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 14, 4, 3, 1, 2),
    _Lgs2816crpsPortBaseVlanGroupName_Type()
)
lgs2816crpsPortBaseVlanGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsPortBaseVlanGroupName.setStatus("current")
_Lgs2816crpsPortBaseVlanGroupMembers_Type = DisplayString
_Lgs2816crpsPortBaseVlanGroupMembers_Object = MibTableColumn
lgs2816crpsPortBaseVlanGroupMembers = _Lgs2816crpsPortBaseVlanGroupMembers_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 14, 4, 3, 1, 3),
    _Lgs2816crpsPortBaseVlanGroupMembers_Type()
)
lgs2816crpsPortBaseVlanGroupMembers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsPortBaseVlanGroupMembers.setStatus("current")


class _Lgs2816crpsPortBaseVlanGroupEntryAction_Type(Integer32):
    """Custom type lgs2816crpsPortBaseVlanGroupEntryAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Lgs2816crpsPortBaseVlanGroupEntryAction_Type.__name__ = "Integer32"
_Lgs2816crpsPortBaseVlanGroupEntryAction_Object = MibTableColumn
lgs2816crpsPortBaseVlanGroupEntryAction = _Lgs2816crpsPortBaseVlanGroupEntryAction_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 14, 4, 3, 1, 4),
    _Lgs2816crpsPortBaseVlanGroupEntryAction_Type()
)
lgs2816crpsPortBaseVlanGroupEntryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsPortBaseVlanGroupEntryAction.setStatus("current")
_Lgs2816crpsMacTableInfo_ObjectIdentity = ObjectIdentity
lgs2816crpsMacTableInfo = _Lgs2816crpsMacTableInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 15)
)
_Lgs2816crpsMacTableConf_ObjectIdentity = ObjectIdentity
lgs2816crpsMacTableConf = _Lgs2816crpsMacTableConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 15, 1)
)


class _Lgs2816crpsMacAgeTime_Type(Integer32):
    """Custom type lgs2816crpsMacAgeTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000000),
    )


_Lgs2816crpsMacAgeTime_Type.__name__ = "Integer32"
_Lgs2816crpsMacAgeTime_Object = MibScalar
lgs2816crpsMacAgeTime = _Lgs2816crpsMacAgeTime_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 15, 1, 1),
    _Lgs2816crpsMacAgeTime_Type()
)
lgs2816crpsMacAgeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsMacAgeTime.setStatus("current")
_Lgs2816crpsMacTableLearningConfTable_Object = MibTable
lgs2816crpsMacTableLearningConfTable = _Lgs2816crpsMacTableLearningConfTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 15, 1, 2)
)
if mibBuilder.loadTexts:
    lgs2816crpsMacTableLearningConfTable.setStatus("current")
_Lgs2816crpsMacTableLearningConfEntry_Object = MibTableRow
lgs2816crpsMacTableLearningConfEntry = _Lgs2816crpsMacTableLearningConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 15, 1, 2, 1)
)
lgs2816crpsMacTableLearningConfEntry.setIndexNames(
    (0, "PRIVATE-LGS2816CRPS-MIB", "lgs2816crpsMacTableLearningConfIndex"),
)
if mibBuilder.loadTexts:
    lgs2816crpsMacTableLearningConfEntry.setStatus("current")


class _Lgs2816crpsMacTableLearningConfIndex_Type(Integer32):
    """Custom type lgs2816crpsMacTableLearningConfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Lgs2816crpsMacTableLearningConfIndex_Type.__name__ = "Integer32"
_Lgs2816crpsMacTableLearningConfIndex_Object = MibTableColumn
lgs2816crpsMacTableLearningConfIndex = _Lgs2816crpsMacTableLearningConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 15, 1, 2, 1, 1),
    _Lgs2816crpsMacTableLearningConfIndex_Type()
)
lgs2816crpsMacTableLearningConfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgs2816crpsMacTableLearningConfIndex.setStatus("current")


class _Lgs2816crpsMacTableLearningConfstate_Type(Integer32):
    """Custom type lgs2816crpsMacTableLearningConfstate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_Lgs2816crpsMacTableLearningConfstate_Type.__name__ = "Integer32"
_Lgs2816crpsMacTableLearningConfstate_Object = MibTableColumn
lgs2816crpsMacTableLearningConfstate = _Lgs2816crpsMacTableLearningConfstate_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 15, 1, 2, 1, 2),
    _Lgs2816crpsMacTableLearningConfstate_Type()
)
lgs2816crpsMacTableLearningConfstate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsMacTableLearningConfstate.setStatus("current")
_Lgs2816crpsMacTableStaticFilter_ObjectIdentity = ObjectIdentity
lgs2816crpsMacTableStaticFilter = _Lgs2816crpsMacTableStaticFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 15, 2)
)


class _Lgs2816crpsMacTableStaticFilterNumber_Type(Integer32):
    """Custom type lgs2816crpsMacTableStaticFilterNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 512),
    )


_Lgs2816crpsMacTableStaticFilterNumber_Type.__name__ = "Integer32"
_Lgs2816crpsMacTableStaticFilterNumber_Object = MibScalar
lgs2816crpsMacTableStaticFilterNumber = _Lgs2816crpsMacTableStaticFilterNumber_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 15, 2, 1),
    _Lgs2816crpsMacTableStaticFilterNumber_Type()
)
lgs2816crpsMacTableStaticFilterNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsMacTableStaticFilterNumber.setStatus("current")


class _Lgs2816crpsMacTableStaticFilterEntryCreate_Type(Integer32):
    """Custom type lgs2816crpsMacTableStaticFilterEntryCreate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 512),
    )


_Lgs2816crpsMacTableStaticFilterEntryCreate_Type.__name__ = "Integer32"
_Lgs2816crpsMacTableStaticFilterEntryCreate_Object = MibScalar
lgs2816crpsMacTableStaticFilterEntryCreate = _Lgs2816crpsMacTableStaticFilterEntryCreate_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 15, 2, 2),
    _Lgs2816crpsMacTableStaticFilterEntryCreate_Type()
)
lgs2816crpsMacTableStaticFilterEntryCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsMacTableStaticFilterEntryCreate.setStatus("current")
_Lgs2816crpsMacTableStaticFilterTable_Object = MibTable
lgs2816crpsMacTableStaticFilterTable = _Lgs2816crpsMacTableStaticFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 15, 2, 3)
)
if mibBuilder.loadTexts:
    lgs2816crpsMacTableStaticFilterTable.setStatus("current")
_Lgs2816crpsMacTableStaticFilterEntry_Object = MibTableRow
lgs2816crpsMacTableStaticFilterEntry = _Lgs2816crpsMacTableStaticFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 15, 2, 3, 1)
)
lgs2816crpsMacTableStaticFilterEntry.setIndexNames(
    (0, "PRIVATE-LGS2816CRPS-MIB", "lgs2816crpsMacTableStaticFilterIndex"),
)
if mibBuilder.loadTexts:
    lgs2816crpsMacTableStaticFilterEntry.setStatus("current")


class _Lgs2816crpsMacTableStaticFilterIndex_Type(Integer32):
    """Custom type lgs2816crpsMacTableStaticFilterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_Lgs2816crpsMacTableStaticFilterIndex_Type.__name__ = "Integer32"
_Lgs2816crpsMacTableStaticFilterIndex_Object = MibTableColumn
lgs2816crpsMacTableStaticFilterIndex = _Lgs2816crpsMacTableStaticFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 15, 2, 3, 1, 1),
    _Lgs2816crpsMacTableStaticFilterIndex_Type()
)
lgs2816crpsMacTableStaticFilterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgs2816crpsMacTableStaticFilterIndex.setStatus("current")
_Lgs2816crpsMacTableStaticFilterMac_Type = DisplayString
_Lgs2816crpsMacTableStaticFilterMac_Object = MibTableColumn
lgs2816crpsMacTableStaticFilterMac = _Lgs2816crpsMacTableStaticFilterMac_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 15, 2, 3, 1, 2),
    _Lgs2816crpsMacTableStaticFilterMac_Type()
)
lgs2816crpsMacTableStaticFilterMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsMacTableStaticFilterMac.setStatus("current")


class _Lgs2816crpsMacTableStaticFilterVid_Type(Integer32):
    """Custom type lgs2816crpsMacTableStaticFilterVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Lgs2816crpsMacTableStaticFilterVid_Type.__name__ = "Integer32"
_Lgs2816crpsMacTableStaticFilterVid_Object = MibTableColumn
lgs2816crpsMacTableStaticFilterVid = _Lgs2816crpsMacTableStaticFilterVid_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 15, 2, 3, 1, 3),
    _Lgs2816crpsMacTableStaticFilterVid_Type()
)
lgs2816crpsMacTableStaticFilterVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsMacTableStaticFilterVid.setStatus("current")
_Lgs2816crpsMacTableStaticFilterAlias_Type = DisplayString
_Lgs2816crpsMacTableStaticFilterAlias_Object = MibTableColumn
lgs2816crpsMacTableStaticFilterAlias = _Lgs2816crpsMacTableStaticFilterAlias_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 15, 2, 3, 1, 4),
    _Lgs2816crpsMacTableStaticFilterAlias_Type()
)
lgs2816crpsMacTableStaticFilterAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsMacTableStaticFilterAlias.setStatus("current")


class _Lgs2816crpsMacTableStaticFilterEntryAction_Type(Integer32):
    """Custom type lgs2816crpsMacTableStaticFilterEntryAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Lgs2816crpsMacTableStaticFilterEntryAction_Type.__name__ = "Integer32"
_Lgs2816crpsMacTableStaticFilterEntryAction_Object = MibTableColumn
lgs2816crpsMacTableStaticFilterEntryAction = _Lgs2816crpsMacTableStaticFilterEntryAction_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 15, 2, 3, 1, 5),
    _Lgs2816crpsMacTableStaticFilterEntryAction_Type()
)
lgs2816crpsMacTableStaticFilterEntryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsMacTableStaticFilterEntryAction.setStatus("current")
_Lgs2816crpsMacTableStaticForward_ObjectIdentity = ObjectIdentity
lgs2816crpsMacTableStaticForward = _Lgs2816crpsMacTableStaticForward_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 15, 3)
)


class _Lgs2816crpsMacTableStaticForwardNumber_Type(Integer32):
    """Custom type lgs2816crpsMacTableStaticForwardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 512),
    )


_Lgs2816crpsMacTableStaticForwardNumber_Type.__name__ = "Integer32"
_Lgs2816crpsMacTableStaticForwardNumber_Object = MibScalar
lgs2816crpsMacTableStaticForwardNumber = _Lgs2816crpsMacTableStaticForwardNumber_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 15, 3, 1),
    _Lgs2816crpsMacTableStaticForwardNumber_Type()
)
lgs2816crpsMacTableStaticForwardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsMacTableStaticForwardNumber.setStatus("current")


class _Lgs2816crpsMacTableStaticForwardEntryCreate_Type(Integer32):
    """Custom type lgs2816crpsMacTableStaticForwardEntryCreate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 512),
    )


_Lgs2816crpsMacTableStaticForwardEntryCreate_Type.__name__ = "Integer32"
_Lgs2816crpsMacTableStaticForwardEntryCreate_Object = MibScalar
lgs2816crpsMacTableStaticForwardEntryCreate = _Lgs2816crpsMacTableStaticForwardEntryCreate_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 15, 3, 2),
    _Lgs2816crpsMacTableStaticForwardEntryCreate_Type()
)
lgs2816crpsMacTableStaticForwardEntryCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsMacTableStaticForwardEntryCreate.setStatus("current")
_Lgs2816crpsMacTableStaticForwardTable_Object = MibTable
lgs2816crpsMacTableStaticForwardTable = _Lgs2816crpsMacTableStaticForwardTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 15, 3, 3)
)
if mibBuilder.loadTexts:
    lgs2816crpsMacTableStaticForwardTable.setStatus("current")
_Lgs2816crpsMacTableStaticForwardEntry_Object = MibTableRow
lgs2816crpsMacTableStaticForwardEntry = _Lgs2816crpsMacTableStaticForwardEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 15, 3, 3, 1)
)
lgs2816crpsMacTableStaticForwardEntry.setIndexNames(
    (0, "PRIVATE-LGS2816CRPS-MIB", "lgs2816crpsMacTableStaticForwardIndex"),
)
if mibBuilder.loadTexts:
    lgs2816crpsMacTableStaticForwardEntry.setStatus("current")


class _Lgs2816crpsMacTableStaticForwardIndex_Type(Integer32):
    """Custom type lgs2816crpsMacTableStaticForwardIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_Lgs2816crpsMacTableStaticForwardIndex_Type.__name__ = "Integer32"
_Lgs2816crpsMacTableStaticForwardIndex_Object = MibTableColumn
lgs2816crpsMacTableStaticForwardIndex = _Lgs2816crpsMacTableStaticForwardIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 15, 3, 3, 1, 1),
    _Lgs2816crpsMacTableStaticForwardIndex_Type()
)
lgs2816crpsMacTableStaticForwardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgs2816crpsMacTableStaticForwardIndex.setStatus("current")
_Lgs2816crpsMacTableStaticForwardMac_Type = DisplayString
_Lgs2816crpsMacTableStaticForwardMac_Object = MibTableColumn
lgs2816crpsMacTableStaticForwardMac = _Lgs2816crpsMacTableStaticForwardMac_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 15, 3, 3, 1, 2),
    _Lgs2816crpsMacTableStaticForwardMac_Type()
)
lgs2816crpsMacTableStaticForwardMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsMacTableStaticForwardMac.setStatus("current")


class _Lgs2816crpsMacTableStaticForwardPort_Type(Integer32):
    """Custom type lgs2816crpsMacTableStaticForwardPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Lgs2816crpsMacTableStaticForwardPort_Type.__name__ = "Integer32"
_Lgs2816crpsMacTableStaticForwardPort_Object = MibTableColumn
lgs2816crpsMacTableStaticForwardPort = _Lgs2816crpsMacTableStaticForwardPort_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 15, 3, 3, 1, 3),
    _Lgs2816crpsMacTableStaticForwardPort_Type()
)
lgs2816crpsMacTableStaticForwardPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsMacTableStaticForwardPort.setStatus("current")


class _Lgs2816crpsMacTableStaticForwardVid_Type(Integer32):
    """Custom type lgs2816crpsMacTableStaticForwardVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Lgs2816crpsMacTableStaticForwardVid_Type.__name__ = "Integer32"
_Lgs2816crpsMacTableStaticForwardVid_Object = MibTableColumn
lgs2816crpsMacTableStaticForwardVid = _Lgs2816crpsMacTableStaticForwardVid_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 15, 3, 3, 1, 4),
    _Lgs2816crpsMacTableStaticForwardVid_Type()
)
lgs2816crpsMacTableStaticForwardVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsMacTableStaticForwardVid.setStatus("current")
_Lgs2816crpsMacTableStaticForwardAlias_Type = DisplayString
_Lgs2816crpsMacTableStaticForwardAlias_Object = MibTableColumn
lgs2816crpsMacTableStaticForwardAlias = _Lgs2816crpsMacTableStaticForwardAlias_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 15, 3, 3, 1, 5),
    _Lgs2816crpsMacTableStaticForwardAlias_Type()
)
lgs2816crpsMacTableStaticForwardAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsMacTableStaticForwardAlias.setStatus("current")


class _Lgs2816crpsMacTableStaticForwardEntryAction_Type(Integer32):
    """Custom type lgs2816crpsMacTableStaticForwardEntryAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Lgs2816crpsMacTableStaticForwardEntryAction_Type.__name__ = "Integer32"
_Lgs2816crpsMacTableStaticForwardEntryAction_Object = MibTableColumn
lgs2816crpsMacTableStaticForwardEntryAction = _Lgs2816crpsMacTableStaticForwardEntryAction_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 15, 3, 3, 1, 6),
    _Lgs2816crpsMacTableStaticForwardEntryAction_Type()
)
lgs2816crpsMacTableStaticForwardEntryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsMacTableStaticForwardEntryAction.setStatus("current")
_Lgs2816crpsMacAlias_ObjectIdentity = ObjectIdentity
lgs2816crpsMacAlias = _Lgs2816crpsMacAlias_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 15, 4)
)


class _Lgs2816crpsMacAliasNumber_Type(Integer32):
    """Custom type lgs2816crpsMacAliasNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_Lgs2816crpsMacAliasNumber_Type.__name__ = "Integer32"
_Lgs2816crpsMacAliasNumber_Object = MibScalar
lgs2816crpsMacAliasNumber = _Lgs2816crpsMacAliasNumber_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 15, 4, 1),
    _Lgs2816crpsMacAliasNumber_Type()
)
lgs2816crpsMacAliasNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsMacAliasNumber.setStatus("current")


class _Lgs2816crpsMacAliasEntryCreate_Type(Integer32):
    """Custom type lgs2816crpsMacAliasEntryCreate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_Lgs2816crpsMacAliasEntryCreate_Type.__name__ = "Integer32"
_Lgs2816crpsMacAliasEntryCreate_Object = MibScalar
lgs2816crpsMacAliasEntryCreate = _Lgs2816crpsMacAliasEntryCreate_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 15, 4, 2),
    _Lgs2816crpsMacAliasEntryCreate_Type()
)
lgs2816crpsMacAliasEntryCreate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsMacAliasEntryCreate.setStatus("current")
_Lgs2816crpsMacAliasTable_Object = MibTable
lgs2816crpsMacAliasTable = _Lgs2816crpsMacAliasTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 15, 4, 3)
)
if mibBuilder.loadTexts:
    lgs2816crpsMacAliasTable.setStatus("current")
_Lgs2816crpsMacAliasEntry_Object = MibTableRow
lgs2816crpsMacAliasEntry = _Lgs2816crpsMacAliasEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 15, 4, 3, 1)
)
lgs2816crpsMacAliasEntry.setIndexNames(
    (0, "PRIVATE-LGS2816CRPS-MIB", "lgs2816crpsMacAliasIndex"),
)
if mibBuilder.loadTexts:
    lgs2816crpsMacAliasEntry.setStatus("current")


class _Lgs2816crpsMacAliasIndex_Type(Integer32):
    """Custom type lgs2816crpsMacAliasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_Lgs2816crpsMacAliasIndex_Type.__name__ = "Integer32"
_Lgs2816crpsMacAliasIndex_Object = MibTableColumn
lgs2816crpsMacAliasIndex = _Lgs2816crpsMacAliasIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 15, 4, 3, 1, 1),
    _Lgs2816crpsMacAliasIndex_Type()
)
lgs2816crpsMacAliasIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgs2816crpsMacAliasIndex.setStatus("current")
_Lgs2816crpsAliasMac_Type = DisplayString
_Lgs2816crpsAliasMac_Object = MibTableColumn
lgs2816crpsAliasMac = _Lgs2816crpsAliasMac_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 15, 4, 3, 1, 2),
    _Lgs2816crpsAliasMac_Type()
)
lgs2816crpsAliasMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsAliasMac.setStatus("current")
_Lgs2816crpsAliasName_Type = DisplayString
_Lgs2816crpsAliasName_Object = MibTableColumn
lgs2816crpsAliasName = _Lgs2816crpsAliasName_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 15, 4, 3, 1, 3),
    _Lgs2816crpsAliasName_Type()
)
lgs2816crpsAliasName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsAliasName.setStatus("current")


class _Lgs2816crpsMacAliasEntryAction_Type(Integer32):
    """Custom type lgs2816crpsMacAliasEntryAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Lgs2816crpsMacAliasEntryAction_Type.__name__ = "Integer32"
_Lgs2816crpsMacAliasEntryAction_Object = MibTableColumn
lgs2816crpsMacAliasEntryAction = _Lgs2816crpsMacAliasEntryAction_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 15, 4, 3, 1, 4),
    _Lgs2816crpsMacAliasEntryAction_Type()
)
lgs2816crpsMacAliasEntryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsMacAliasEntryAction.setStatus("current")
_Lgs2816crpsGVRPInfo_ObjectIdentity = ObjectIdentity
lgs2816crpsGVRPInfo = _Lgs2816crpsGVRPInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 16)
)
_Lgs2816crpsGvrpConf_ObjectIdentity = ObjectIdentity
lgs2816crpsGvrpConf = _Lgs2816crpsGvrpConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 16, 1)
)


class _Lgs2816crpsGvrpConfState_Type(Integer32):
    """Custom type lgs2816crpsGvrpConfState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2816crpsGvrpConfState_Type.__name__ = "Integer32"
_Lgs2816crpsGvrpConfState_Object = MibScalar
lgs2816crpsGvrpConfState = _Lgs2816crpsGvrpConfState_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 16, 1, 1),
    _Lgs2816crpsGvrpConfState_Type()
)
lgs2816crpsGvrpConfState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsGvrpConfState.setStatus("current")
_Lgs2816crpsGvrpConfTable_Object = MibTable
lgs2816crpsGvrpConfTable = _Lgs2816crpsGvrpConfTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 16, 1, 2)
)
if mibBuilder.loadTexts:
    lgs2816crpsGvrpConfTable.setStatus("current")
_Lgs2816crpsGvrpConfEntry_Object = MibTableRow
lgs2816crpsGvrpConfEntry = _Lgs2816crpsGvrpConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 16, 1, 2, 1)
)
lgs2816crpsGvrpConfEntry.setIndexNames(
    (0, "PRIVATE-LGS2816CRPS-MIB", "lgs2816crpsGvrpConfIndex"),
)
if mibBuilder.loadTexts:
    lgs2816crpsGvrpConfEntry.setStatus("current")


class _Lgs2816crpsGvrpConfIndex_Type(Integer32):
    """Custom type lgs2816crpsGvrpConfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Lgs2816crpsGvrpConfIndex_Type.__name__ = "Integer32"
_Lgs2816crpsGvrpConfIndex_Object = MibTableColumn
lgs2816crpsGvrpConfIndex = _Lgs2816crpsGvrpConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 16, 1, 2, 1, 1),
    _Lgs2816crpsGvrpConfIndex_Type()
)
lgs2816crpsGvrpConfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgs2816crpsGvrpConfIndex.setStatus("current")


class _Lgs2816crpsGvrpConfJoinTime_Type(Integer32):
    """Custom type lgs2816crpsGvrpConfJoinTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 100),
    )


_Lgs2816crpsGvrpConfJoinTime_Type.__name__ = "Integer32"
_Lgs2816crpsGvrpConfJoinTime_Object = MibTableColumn
lgs2816crpsGvrpConfJoinTime = _Lgs2816crpsGvrpConfJoinTime_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 16, 1, 2, 1, 2),
    _Lgs2816crpsGvrpConfJoinTime_Type()
)
lgs2816crpsGvrpConfJoinTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsGvrpConfJoinTime.setStatus("current")


class _Lgs2816crpsGvrpConfLeaveTime_Type(Integer32):
    """Custom type lgs2816crpsGvrpConfLeaveTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 300),
    )


_Lgs2816crpsGvrpConfLeaveTime_Type.__name__ = "Integer32"
_Lgs2816crpsGvrpConfLeaveTime_Object = MibTableColumn
lgs2816crpsGvrpConfLeaveTime = _Lgs2816crpsGvrpConfLeaveTime_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 16, 1, 2, 1, 3),
    _Lgs2816crpsGvrpConfLeaveTime_Type()
)
lgs2816crpsGvrpConfLeaveTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsGvrpConfLeaveTime.setStatus("current")


class _Lgs2816crpsGvrpConfLeaveAllTime_Type(Integer32):
    """Custom type lgs2816crpsGvrpConfLeaveAllTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 5000),
    )


_Lgs2816crpsGvrpConfLeaveAllTime_Type.__name__ = "Integer32"
_Lgs2816crpsGvrpConfLeaveAllTime_Object = MibTableColumn
lgs2816crpsGvrpConfLeaveAllTime = _Lgs2816crpsGvrpConfLeaveAllTime_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 16, 1, 2, 1, 4),
    _Lgs2816crpsGvrpConfLeaveAllTime_Type()
)
lgs2816crpsGvrpConfLeaveAllTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsGvrpConfLeaveAllTime.setStatus("current")


class _Lgs2816crpsGvrpConfDefaultAppMode_Type(Integer32):
    """Custom type lgs2816crpsGvrpConfDefaultAppMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2816crpsGvrpConfDefaultAppMode_Type.__name__ = "Integer32"
_Lgs2816crpsGvrpConfDefaultAppMode_Object = MibTableColumn
lgs2816crpsGvrpConfDefaultAppMode = _Lgs2816crpsGvrpConfDefaultAppMode_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 16, 1, 2, 1, 5),
    _Lgs2816crpsGvrpConfDefaultAppMode_Type()
)
lgs2816crpsGvrpConfDefaultAppMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsGvrpConfDefaultAppMode.setStatus("current")


class _Lgs2816crpsGvrpConfDefaultRegMode_Type(Integer32):
    """Custom type lgs2816crpsGvrpConfDefaultRegMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_Lgs2816crpsGvrpConfDefaultRegMode_Type.__name__ = "Integer32"
_Lgs2816crpsGvrpConfDefaultRegMode_Object = MibTableColumn
lgs2816crpsGvrpConfDefaultRegMode = _Lgs2816crpsGvrpConfDefaultRegMode_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 16, 1, 2, 1, 6),
    _Lgs2816crpsGvrpConfDefaultRegMode_Type()
)
lgs2816crpsGvrpConfDefaultRegMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsGvrpConfDefaultRegMode.setStatus("current")


class _Lgs2816crpsGvrpConfRestrictedMode_Type(Integer32):
    """Custom type lgs2816crpsGvrpConfRestrictedMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2816crpsGvrpConfRestrictedMode_Type.__name__ = "Integer32"
_Lgs2816crpsGvrpConfRestrictedMode_Object = MibTableColumn
lgs2816crpsGvrpConfRestrictedMode = _Lgs2816crpsGvrpConfRestrictedMode_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 16, 1, 2, 1, 7),
    _Lgs2816crpsGvrpConfRestrictedMode_Type()
)
lgs2816crpsGvrpConfRestrictedMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsGvrpConfRestrictedMode.setStatus("current")
_Lgs2816crpsGvrpCounter_ObjectIdentity = ObjectIdentity
lgs2816crpsGvrpCounter = _Lgs2816crpsGvrpCounter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 16, 2)
)
_Lgs2816crpsGvrpCounterTable_Object = MibTable
lgs2816crpsGvrpCounterTable = _Lgs2816crpsGvrpCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 16, 2, 1)
)
if mibBuilder.loadTexts:
    lgs2816crpsGvrpCounterTable.setStatus("current")
_Lgs2816crpsGvrpCounterEntry_Object = MibTableRow
lgs2816crpsGvrpCounterEntry = _Lgs2816crpsGvrpCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 16, 2, 1, 1)
)
lgs2816crpsGvrpCounterEntry.setIndexNames(
    (0, "PRIVATE-LGS2816CRPS-MIB", "lgs2816crpsGvrpCounterIndex"),
)
if mibBuilder.loadTexts:
    lgs2816crpsGvrpCounterEntry.setStatus("current")


class _Lgs2816crpsGvrpCounterIndex_Type(Integer32):
    """Custom type lgs2816crpsGvrpCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Lgs2816crpsGvrpCounterIndex_Type.__name__ = "Integer32"
_Lgs2816crpsGvrpCounterIndex_Object = MibTableColumn
lgs2816crpsGvrpCounterIndex = _Lgs2816crpsGvrpCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 16, 2, 1, 1, 1),
    _Lgs2816crpsGvrpCounterIndex_Type()
)
lgs2816crpsGvrpCounterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgs2816crpsGvrpCounterIndex.setStatus("current")
_Lgs2816crpsGvrpCounterRxTotalGvrpPkts_Type = Counter32
_Lgs2816crpsGvrpCounterRxTotalGvrpPkts_Object = MibTableColumn
lgs2816crpsGvrpCounterRxTotalGvrpPkts = _Lgs2816crpsGvrpCounterRxTotalGvrpPkts_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 16, 2, 1, 1, 2),
    _Lgs2816crpsGvrpCounterRxTotalGvrpPkts_Type()
)
lgs2816crpsGvrpCounterRxTotalGvrpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsGvrpCounterRxTotalGvrpPkts.setStatus("current")
_Lgs2816crpsGvrpCounterRxInvalidGvrpPkts_Type = Counter32
_Lgs2816crpsGvrpCounterRxInvalidGvrpPkts_Object = MibTableColumn
lgs2816crpsGvrpCounterRxInvalidGvrpPkts = _Lgs2816crpsGvrpCounterRxInvalidGvrpPkts_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 16, 2, 1, 1, 3),
    _Lgs2816crpsGvrpCounterRxInvalidGvrpPkts_Type()
)
lgs2816crpsGvrpCounterRxInvalidGvrpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsGvrpCounterRxInvalidGvrpPkts.setStatus("current")
_Lgs2816crpsGvrpCounterRxLeaveAllMsg_Type = Counter32
_Lgs2816crpsGvrpCounterRxLeaveAllMsg_Object = MibTableColumn
lgs2816crpsGvrpCounterRxLeaveAllMsg = _Lgs2816crpsGvrpCounterRxLeaveAllMsg_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 16, 2, 1, 1, 4),
    _Lgs2816crpsGvrpCounterRxLeaveAllMsg_Type()
)
lgs2816crpsGvrpCounterRxLeaveAllMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsGvrpCounterRxLeaveAllMsg.setStatus("current")
_Lgs2816crpsGvrpCounterRxJoinEmptyMsg_Type = Counter32
_Lgs2816crpsGvrpCounterRxJoinEmptyMsg_Object = MibTableColumn
lgs2816crpsGvrpCounterRxJoinEmptyMsg = _Lgs2816crpsGvrpCounterRxJoinEmptyMsg_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 16, 2, 1, 1, 5),
    _Lgs2816crpsGvrpCounterRxJoinEmptyMsg_Type()
)
lgs2816crpsGvrpCounterRxJoinEmptyMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsGvrpCounterRxJoinEmptyMsg.setStatus("current")
_Lgs2816crpsGvrpCounterRxJoinInMsg_Type = Counter32
_Lgs2816crpsGvrpCounterRxJoinInMsg_Object = MibTableColumn
lgs2816crpsGvrpCounterRxJoinInMsg = _Lgs2816crpsGvrpCounterRxJoinInMsg_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 16, 2, 1, 1, 6),
    _Lgs2816crpsGvrpCounterRxJoinInMsg_Type()
)
lgs2816crpsGvrpCounterRxJoinInMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsGvrpCounterRxJoinInMsg.setStatus("current")
_Lgs2816crpsGvrpCounterRxLeaveEmptyMsg_Type = Counter32
_Lgs2816crpsGvrpCounterRxLeaveEmptyMsg_Object = MibTableColumn
lgs2816crpsGvrpCounterRxLeaveEmptyMsg = _Lgs2816crpsGvrpCounterRxLeaveEmptyMsg_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 16, 2, 1, 1, 7),
    _Lgs2816crpsGvrpCounterRxLeaveEmptyMsg_Type()
)
lgs2816crpsGvrpCounterRxLeaveEmptyMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsGvrpCounterRxLeaveEmptyMsg.setStatus("current")
_Lgs2816crpsGvrpCounterRxEmptyMsg_Type = Counter32
_Lgs2816crpsGvrpCounterRxEmptyMsg_Object = MibTableColumn
lgs2816crpsGvrpCounterRxEmptyMsg = _Lgs2816crpsGvrpCounterRxEmptyMsg_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 16, 2, 1, 1, 8),
    _Lgs2816crpsGvrpCounterRxEmptyMsg_Type()
)
lgs2816crpsGvrpCounterRxEmptyMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsGvrpCounterRxEmptyMsg.setStatus("current")
_Lgs2816crpsGvrpCounterTxTotalGvrpPkts_Type = Counter32
_Lgs2816crpsGvrpCounterTxTotalGvrpPkts_Object = MibTableColumn
lgs2816crpsGvrpCounterTxTotalGvrpPkts = _Lgs2816crpsGvrpCounterTxTotalGvrpPkts_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 16, 2, 1, 1, 9),
    _Lgs2816crpsGvrpCounterTxTotalGvrpPkts_Type()
)
lgs2816crpsGvrpCounterTxTotalGvrpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsGvrpCounterTxTotalGvrpPkts.setStatus("current")
_Lgs2816crpsGvrpCounterTxLeaveAllMsg_Type = Counter32
_Lgs2816crpsGvrpCounterTxLeaveAllMsg_Object = MibTableColumn
lgs2816crpsGvrpCounterTxLeaveAllMsg = _Lgs2816crpsGvrpCounterTxLeaveAllMsg_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 16, 2, 1, 1, 10),
    _Lgs2816crpsGvrpCounterTxLeaveAllMsg_Type()
)
lgs2816crpsGvrpCounterTxLeaveAllMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsGvrpCounterTxLeaveAllMsg.setStatus("current")
_Lgs2816crpsGvrpCounterTxJoinEmptyMsg_Type = Counter32
_Lgs2816crpsGvrpCounterTxJoinEmptyMsg_Object = MibTableColumn
lgs2816crpsGvrpCounterTxJoinEmptyMsg = _Lgs2816crpsGvrpCounterTxJoinEmptyMsg_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 16, 2, 1, 1, 11),
    _Lgs2816crpsGvrpCounterTxJoinEmptyMsg_Type()
)
lgs2816crpsGvrpCounterTxJoinEmptyMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsGvrpCounterTxJoinEmptyMsg.setStatus("current")
_Lgs2816crpsGvrpCounterTxJoinInMsg_Type = Counter32
_Lgs2816crpsGvrpCounterTxJoinInMsg_Object = MibTableColumn
lgs2816crpsGvrpCounterTxJoinInMsg = _Lgs2816crpsGvrpCounterTxJoinInMsg_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 16, 2, 1, 1, 12),
    _Lgs2816crpsGvrpCounterTxJoinInMsg_Type()
)
lgs2816crpsGvrpCounterTxJoinInMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsGvrpCounterTxJoinInMsg.setStatus("current")
_Lgs2816crpsGvrpCounterTxLeaveEmptyMsg_Type = Counter32
_Lgs2816crpsGvrpCounterTxLeaveEmptyMsg_Object = MibTableColumn
lgs2816crpsGvrpCounterTxLeaveEmptyMsg = _Lgs2816crpsGvrpCounterTxLeaveEmptyMsg_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 16, 2, 1, 1, 13),
    _Lgs2816crpsGvrpCounterTxLeaveEmptyMsg_Type()
)
lgs2816crpsGvrpCounterTxLeaveEmptyMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsGvrpCounterTxLeaveEmptyMsg.setStatus("current")
_Lgs2816crpsGvrpCounterTxEmptyMsg_Type = Counter32
_Lgs2816crpsGvrpCounterTxEmptyMsg_Object = MibTableColumn
lgs2816crpsGvrpCounterTxEmptyMsg = _Lgs2816crpsGvrpCounterTxEmptyMsg_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 16, 2, 1, 1, 14),
    _Lgs2816crpsGvrpCounterTxEmptyMsg_Type()
)
lgs2816crpsGvrpCounterTxEmptyMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsGvrpCounterTxEmptyMsg.setStatus("current")
_Lgs2816crpsGvrpGroup_ObjectIdentity = ObjectIdentity
lgs2816crpsGvrpGroup = _Lgs2816crpsGvrpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 16, 3)
)


class _Lgs2816crpsGvrpGroupNumber_Type(Integer32):
    """Custom type lgs2816crpsGvrpGroupNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Lgs2816crpsGvrpGroupNumber_Type.__name__ = "Integer32"
_Lgs2816crpsGvrpGroupNumber_Object = MibScalar
lgs2816crpsGvrpGroupNumber = _Lgs2816crpsGvrpGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 16, 3, 1),
    _Lgs2816crpsGvrpGroupNumber_Type()
)
lgs2816crpsGvrpGroupNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsGvrpGroupNumber.setStatus("current")
_Lgs2816crpsGvrpGroupTable_Object = MibTable
lgs2816crpsGvrpGroupTable = _Lgs2816crpsGvrpGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 16, 3, 2)
)
if mibBuilder.loadTexts:
    lgs2816crpsGvrpGroupTable.setStatus("current")
_Lgs2816crpsGvrpGroupEntry_Object = MibTableRow
lgs2816crpsGvrpGroupEntry = _Lgs2816crpsGvrpGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 16, 3, 2, 1)
)
lgs2816crpsGvrpGroupEntry.setIndexNames(
    (0, "PRIVATE-LGS2816CRPS-MIB", "lgs2816crpsGvrpGroupId"),
)
if mibBuilder.loadTexts:
    lgs2816crpsGvrpGroupEntry.setStatus("current")


class _Lgs2816crpsGvrpGroupId_Type(Integer32):
    """Custom type lgs2816crpsGvrpGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Lgs2816crpsGvrpGroupId_Type.__name__ = "Integer32"
_Lgs2816crpsGvrpGroupId_Object = MibTableColumn
lgs2816crpsGvrpGroupId = _Lgs2816crpsGvrpGroupId_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 16, 3, 2, 1, 1),
    _Lgs2816crpsGvrpGroupId_Type()
)
lgs2816crpsGvrpGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsGvrpGroupId.setStatus("current")


class _Lgs2816crpsGvrpGroupVid_Type(Integer32):
    """Custom type lgs2816crpsGvrpGroupVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Lgs2816crpsGvrpGroupVid_Type.__name__ = "Integer32"
_Lgs2816crpsGvrpGroupVid_Object = MibTableColumn
lgs2816crpsGvrpGroupVid = _Lgs2816crpsGvrpGroupVid_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 16, 3, 2, 1, 2),
    _Lgs2816crpsGvrpGroupVid_Type()
)
lgs2816crpsGvrpGroupVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsGvrpGroupVid.setStatus("current")
_Lgs2816crpsGvrpGroupMemberPort_Type = DisplayString
_Lgs2816crpsGvrpGroupMemberPort_Object = MibTableColumn
lgs2816crpsGvrpGroupMemberPort = _Lgs2816crpsGvrpGroupMemberPort_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 16, 3, 2, 1, 3),
    _Lgs2816crpsGvrpGroupMemberPort_Type()
)
lgs2816crpsGvrpGroupMemberPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsGvrpGroupMemberPort.setStatus("current")
_Lgs2816crpsGvrpGroupAdministrativeCtrlTable_Object = MibTable
lgs2816crpsGvrpGroupAdministrativeCtrlTable = _Lgs2816crpsGvrpGroupAdministrativeCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 16, 3, 3)
)
if mibBuilder.loadTexts:
    lgs2816crpsGvrpGroupAdministrativeCtrlTable.setStatus("current")
_Lgs2816crpsGvrpGroupAdministrativeCtrlEntry_Object = MibTableRow
lgs2816crpsGvrpGroupAdministrativeCtrlEntry = _Lgs2816crpsGvrpGroupAdministrativeCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 16, 3, 3, 1)
)
lgs2816crpsGvrpGroupAdministrativeCtrlEntry.setIndexNames(
    (0, "PRIVATE-LGS2816CRPS-MIB", "lgs2816crpsGvrpGroupAdministrativeCtrlVid"),
    (0, "PRIVATE-LGS2816CRPS-MIB", "lgs2816crpsGvrpGroupAdministrativeCtrlPort"),
)
if mibBuilder.loadTexts:
    lgs2816crpsGvrpGroupAdministrativeCtrlEntry.setStatus("current")


class _Lgs2816crpsGvrpGroupAdministrativeCtrlVid_Type(Integer32):
    """Custom type lgs2816crpsGvrpGroupAdministrativeCtrlVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Lgs2816crpsGvrpGroupAdministrativeCtrlVid_Type.__name__ = "Integer32"
_Lgs2816crpsGvrpGroupAdministrativeCtrlVid_Object = MibTableColumn
lgs2816crpsGvrpGroupAdministrativeCtrlVid = _Lgs2816crpsGvrpGroupAdministrativeCtrlVid_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 16, 3, 3, 1, 1),
    _Lgs2816crpsGvrpGroupAdministrativeCtrlVid_Type()
)
lgs2816crpsGvrpGroupAdministrativeCtrlVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsGvrpGroupAdministrativeCtrlVid.setStatus("current")


class _Lgs2816crpsGvrpGroupAdministrativeCtrlPort_Type(Integer32):
    """Custom type lgs2816crpsGvrpGroupAdministrativeCtrlPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Lgs2816crpsGvrpGroupAdministrativeCtrlPort_Type.__name__ = "Integer32"
_Lgs2816crpsGvrpGroupAdministrativeCtrlPort_Object = MibTableColumn
lgs2816crpsGvrpGroupAdministrativeCtrlPort = _Lgs2816crpsGvrpGroupAdministrativeCtrlPort_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 16, 3, 3, 1, 2),
    _Lgs2816crpsGvrpGroupAdministrativeCtrlPort_Type()
)
lgs2816crpsGvrpGroupAdministrativeCtrlPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsGvrpGroupAdministrativeCtrlPort.setStatus("current")


class _Lgs2816crpsGvrpGroupAdministrativeCtrlApp_Type(Integer32):
    """Custom type lgs2816crpsGvrpGroupAdministrativeCtrlApp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2816crpsGvrpGroupAdministrativeCtrlApp_Type.__name__ = "Integer32"
_Lgs2816crpsGvrpGroupAdministrativeCtrlApp_Object = MibTableColumn
lgs2816crpsGvrpGroupAdministrativeCtrlApp = _Lgs2816crpsGvrpGroupAdministrativeCtrlApp_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 16, 3, 3, 1, 3),
    _Lgs2816crpsGvrpGroupAdministrativeCtrlApp_Type()
)
lgs2816crpsGvrpGroupAdministrativeCtrlApp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsGvrpGroupAdministrativeCtrlApp.setStatus("current")


class _Lgs2816crpsGvrpGroupAdministrativeCtrlReg_Type(Integer32):
    """Custom type lgs2816crpsGvrpGroupAdministrativeCtrlReg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Lgs2816crpsGvrpGroupAdministrativeCtrlReg_Type.__name__ = "Integer32"
_Lgs2816crpsGvrpGroupAdministrativeCtrlReg_Object = MibTableColumn
lgs2816crpsGvrpGroupAdministrativeCtrlReg = _Lgs2816crpsGvrpGroupAdministrativeCtrlReg_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 16, 3, 3, 1, 4),
    _Lgs2816crpsGvrpGroupAdministrativeCtrlReg_Type()
)
lgs2816crpsGvrpGroupAdministrativeCtrlReg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsGvrpGroupAdministrativeCtrlReg.setStatus("current")
_Lgs2816crpsQosInfo_ObjectIdentity = ObjectIdentity
lgs2816crpsQosInfo = _Lgs2816crpsQosInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 17)
)
_Lgs2816crpsQosPortConf_ObjectIdentity = ObjectIdentity
lgs2816crpsQosPortConf = _Lgs2816crpsQosPortConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 17, 1)
)


class _Lgs2816crpsQosNumOfClasses_Type(Integer32):
    """Custom type lgs2816crpsQosNumOfClasses based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(4, 4),
    )


_Lgs2816crpsQosNumOfClasses_Type.__name__ = "Integer32"
_Lgs2816crpsQosNumOfClasses_Object = MibScalar
lgs2816crpsQosNumOfClasses = _Lgs2816crpsQosNumOfClasses_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 17, 1, 1),
    _Lgs2816crpsQosNumOfClasses_Type()
)
lgs2816crpsQosNumOfClasses.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsQosNumOfClasses.setStatus("current")
_Lgs2816crpsQosPortConfTable_Object = MibTable
lgs2816crpsQosPortConfTable = _Lgs2816crpsQosPortConfTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 17, 1, 2)
)
if mibBuilder.loadTexts:
    lgs2816crpsQosPortConfTable.setStatus("current")
_Lgs2816crpsQosPortConfEntry_Object = MibTableRow
lgs2816crpsQosPortConfEntry = _Lgs2816crpsQosPortConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 17, 1, 2, 1)
)
lgs2816crpsQosPortConfEntry.setIndexNames(
    (0, "PRIVATE-LGS2816CRPS-MIB", "lgs2816crpsQosPortConfIndex"),
)
if mibBuilder.loadTexts:
    lgs2816crpsQosPortConfEntry.setStatus("current")


class _Lgs2816crpsQosPortConfIndex_Type(Integer32):
    """Custom type lgs2816crpsQosPortConfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Lgs2816crpsQosPortConfIndex_Type.__name__ = "Integer32"
_Lgs2816crpsQosPortConfIndex_Object = MibTableColumn
lgs2816crpsQosPortConfIndex = _Lgs2816crpsQosPortConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 17, 1, 2, 1, 1),
    _Lgs2816crpsQosPortConfIndex_Type()
)
lgs2816crpsQosPortConfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgs2816crpsQosPortConfIndex.setStatus("current")


class _Lgs2816crpsQosPortConfDefaultClasses_Type(Integer32):
    """Custom type lgs2816crpsQosPortConfDefaultClasses based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Lgs2816crpsQosPortConfDefaultClasses_Type.__name__ = "Integer32"
_Lgs2816crpsQosPortConfDefaultClasses_Object = MibTableColumn
lgs2816crpsQosPortConfDefaultClasses = _Lgs2816crpsQosPortConfDefaultClasses_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 17, 1, 2, 1, 2),
    _Lgs2816crpsQosPortConfDefaultClasses_Type()
)
lgs2816crpsQosPortConfDefaultClasses.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsQosPortConfDefaultClasses.setStatus("current")


class _Lgs2816crpsQosPortConfQCL_Type(Integer32):
    """Custom type lgs2816crpsQosPortConfQCL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Lgs2816crpsQosPortConfQCL_Type.__name__ = "Integer32"
_Lgs2816crpsQosPortConfQCL_Object = MibTableColumn
lgs2816crpsQosPortConfQCL = _Lgs2816crpsQosPortConfQCL_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 17, 1, 2, 1, 3),
    _Lgs2816crpsQosPortConfQCL_Type()
)
lgs2816crpsQosPortConfQCL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsQosPortConfQCL.setStatus("current")


class _Lgs2816crpsQosPortConfUserPriority_Type(Integer32):
    """Custom type lgs2816crpsQosPortConfUserPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Lgs2816crpsQosPortConfUserPriority_Type.__name__ = "Integer32"
_Lgs2816crpsQosPortConfUserPriority_Object = MibTableColumn
lgs2816crpsQosPortConfUserPriority = _Lgs2816crpsQosPortConfUserPriority_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 17, 1, 2, 1, 4),
    _Lgs2816crpsQosPortConfUserPriority_Type()
)
lgs2816crpsQosPortConfUserPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsQosPortConfUserPriority.setStatus("current")


class _Lgs2816crpsQosPortConfQueuingMode_Type(Integer32):
    """Custom type lgs2816crpsQosPortConfQueuingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2816crpsQosPortConfQueuingMode_Type.__name__ = "Integer32"
_Lgs2816crpsQosPortConfQueuingMode_Object = MibTableColumn
lgs2816crpsQosPortConfQueuingMode = _Lgs2816crpsQosPortConfQueuingMode_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 17, 1, 2, 1, 5),
    _Lgs2816crpsQosPortConfQueuingMode_Type()
)
lgs2816crpsQosPortConfQueuingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsQosPortConfQueuingMode.setStatus("current")


class _Lgs2816crpsQosPortConfQueueWeightedLow_Type(Integer32):
    """Custom type lgs2816crpsQosPortConfQueueWeightedLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(4, 4),
        ValueRangeConstraint(8, 8),
    )


_Lgs2816crpsQosPortConfQueueWeightedLow_Type.__name__ = "Integer32"
_Lgs2816crpsQosPortConfQueueWeightedLow_Object = MibTableColumn
lgs2816crpsQosPortConfQueueWeightedLow = _Lgs2816crpsQosPortConfQueueWeightedLow_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 17, 1, 2, 1, 6),
    _Lgs2816crpsQosPortConfQueueWeightedLow_Type()
)
lgs2816crpsQosPortConfQueueWeightedLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsQosPortConfQueueWeightedLow.setStatus("current")


class _Lgs2816crpsQosPortConfQueueWeightedNormal_Type(Integer32):
    """Custom type lgs2816crpsQosPortConfQueueWeightedNormal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(4, 4),
        ValueRangeConstraint(8, 8),
    )


_Lgs2816crpsQosPortConfQueueWeightedNormal_Type.__name__ = "Integer32"
_Lgs2816crpsQosPortConfQueueWeightedNormal_Object = MibTableColumn
lgs2816crpsQosPortConfQueueWeightedNormal = _Lgs2816crpsQosPortConfQueueWeightedNormal_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 17, 1, 2, 1, 7),
    _Lgs2816crpsQosPortConfQueueWeightedNormal_Type()
)
lgs2816crpsQosPortConfQueueWeightedNormal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsQosPortConfQueueWeightedNormal.setStatus("current")


class _Lgs2816crpsQosPortConfQueueWeightedMedium_Type(Integer32):
    """Custom type lgs2816crpsQosPortConfQueueWeightedMedium based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(4, 4),
        ValueRangeConstraint(8, 8),
    )


_Lgs2816crpsQosPortConfQueueWeightedMedium_Type.__name__ = "Integer32"
_Lgs2816crpsQosPortConfQueueWeightedMedium_Object = MibTableColumn
lgs2816crpsQosPortConfQueueWeightedMedium = _Lgs2816crpsQosPortConfQueueWeightedMedium_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 17, 1, 2, 1, 8),
    _Lgs2816crpsQosPortConfQueueWeightedMedium_Type()
)
lgs2816crpsQosPortConfQueueWeightedMedium.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsQosPortConfQueueWeightedMedium.setStatus("current")


class _Lgs2816crpsQosPortConfQueueWeightedHigh_Type(Integer32):
    """Custom type lgs2816crpsQosPortConfQueueWeightedHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(4, 4),
        ValueRangeConstraint(8, 8),
    )


_Lgs2816crpsQosPortConfQueueWeightedHigh_Type.__name__ = "Integer32"
_Lgs2816crpsQosPortConfQueueWeightedHigh_Object = MibTableColumn
lgs2816crpsQosPortConfQueueWeightedHigh = _Lgs2816crpsQosPortConfQueueWeightedHigh_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 17, 1, 2, 1, 9),
    _Lgs2816crpsQosPortConfQueueWeightedHigh_Type()
)
lgs2816crpsQosPortConfQueueWeightedHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsQosPortConfQueueWeightedHigh.setStatus("current")
_Lgs2816crpsQosRateLimiters_ObjectIdentity = ObjectIdentity
lgs2816crpsQosRateLimiters = _Lgs2816crpsQosRateLimiters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 17, 3)
)
_Lgs2816crpsQosRateLimitersTable_Object = MibTable
lgs2816crpsQosRateLimitersTable = _Lgs2816crpsQosRateLimitersTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 17, 3, 1)
)
if mibBuilder.loadTexts:
    lgs2816crpsQosRateLimitersTable.setStatus("current")
_Lgs2816crpsQosRateLimitersEntry_Object = MibTableRow
lgs2816crpsQosRateLimitersEntry = _Lgs2816crpsQosRateLimitersEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 17, 3, 1, 1)
)
lgs2816crpsQosRateLimitersEntry.setIndexNames(
    (0, "PRIVATE-LGS2816CRPS-MIB", "lgs2816crpsQosRateLimitersIndex"),
)
if mibBuilder.loadTexts:
    lgs2816crpsQosRateLimitersEntry.setStatus("current")


class _Lgs2816crpsQosRateLimitersIndex_Type(Integer32):
    """Custom type lgs2816crpsQosRateLimitersIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Lgs2816crpsQosRateLimitersIndex_Type.__name__ = "Integer32"
_Lgs2816crpsQosRateLimitersIndex_Object = MibTableColumn
lgs2816crpsQosRateLimitersIndex = _Lgs2816crpsQosRateLimitersIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 17, 3, 1, 1, 1),
    _Lgs2816crpsQosRateLimitersIndex_Type()
)
lgs2816crpsQosRateLimitersIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgs2816crpsQosRateLimitersIndex.setStatus("current")


class _Lgs2816crpsQosRateLimitersPolicer_Type(Integer32):
    """Custom type lgs2816crpsQosRateLimitersPolicer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2816crpsQosRateLimitersPolicer_Type.__name__ = "Integer32"
_Lgs2816crpsQosRateLimitersPolicer_Object = MibTableColumn
lgs2816crpsQosRateLimitersPolicer = _Lgs2816crpsQosRateLimitersPolicer_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 17, 3, 1, 1, 2),
    _Lgs2816crpsQosRateLimitersPolicer_Type()
)
lgs2816crpsQosRateLimitersPolicer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsQosRateLimitersPolicer.setStatus("current")


class _Lgs2816crpsQosRateLimitersPolicerRate_Type(Integer32):
    """Custom type lgs2816crpsQosRateLimitersPolicerRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000000),
    )


_Lgs2816crpsQosRateLimitersPolicerRate_Type.__name__ = "Integer32"
_Lgs2816crpsQosRateLimitersPolicerRate_Object = MibTableColumn
lgs2816crpsQosRateLimitersPolicerRate = _Lgs2816crpsQosRateLimitersPolicerRate_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 17, 3, 1, 1, 3),
    _Lgs2816crpsQosRateLimitersPolicerRate_Type()
)
lgs2816crpsQosRateLimitersPolicerRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsQosRateLimitersPolicerRate.setStatus("current")


class _Lgs2816crpsQosRateLimitersShaper_Type(Integer32):
    """Custom type lgs2816crpsQosRateLimitersShaper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2816crpsQosRateLimitersShaper_Type.__name__ = "Integer32"
_Lgs2816crpsQosRateLimitersShaper_Object = MibTableColumn
lgs2816crpsQosRateLimitersShaper = _Lgs2816crpsQosRateLimitersShaper_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 17, 3, 1, 1, 4),
    _Lgs2816crpsQosRateLimitersShaper_Type()
)
lgs2816crpsQosRateLimitersShaper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsQosRateLimitersShaper.setStatus("current")


class _Lgs2816crpsQosRateLimitersShaperRate_Type(Integer32):
    """Custom type lgs2816crpsQosRateLimitersShaperRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000000),
    )


_Lgs2816crpsQosRateLimitersShaperRate_Type.__name__ = "Integer32"
_Lgs2816crpsQosRateLimitersShaperRate_Object = MibTableColumn
lgs2816crpsQosRateLimitersShaperRate = _Lgs2816crpsQosRateLimitersShaperRate_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 17, 3, 1, 1, 5),
    _Lgs2816crpsQosRateLimitersShaperRate_Type()
)
lgs2816crpsQosRateLimitersShaperRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsQosRateLimitersShaperRate.setStatus("current")
_Lgs2816crpsQosStormCtrl_ObjectIdentity = ObjectIdentity
lgs2816crpsQosStormCtrl = _Lgs2816crpsQosStormCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 17, 4)
)


class _Lgs2816crpsQosStromCtrlFloodedUnicastStatus_Type(Integer32):
    """Custom type lgs2816crpsQosStromCtrlFloodedUnicastStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2816crpsQosStromCtrlFloodedUnicastStatus_Type.__name__ = "Integer32"
_Lgs2816crpsQosStromCtrlFloodedUnicastStatus_Object = MibScalar
lgs2816crpsQosStromCtrlFloodedUnicastStatus = _Lgs2816crpsQosStromCtrlFloodedUnicastStatus_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 17, 4, 1),
    _Lgs2816crpsQosStromCtrlFloodedUnicastStatus_Type()
)
lgs2816crpsQosStromCtrlFloodedUnicastStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsQosStromCtrlFloodedUnicastStatus.setStatus("current")
_Lgs2816crpsQosStromCtrlFloodedUnicastRate_Type = DisplayString
_Lgs2816crpsQosStromCtrlFloodedUnicastRate_Object = MibScalar
lgs2816crpsQosStromCtrlFloodedUnicastRate = _Lgs2816crpsQosStromCtrlFloodedUnicastRate_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 17, 4, 2),
    _Lgs2816crpsQosStromCtrlFloodedUnicastRate_Type()
)
lgs2816crpsQosStromCtrlFloodedUnicastRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsQosStromCtrlFloodedUnicastRate.setStatus("current")


class _Lgs2816crpsQosStromCtrlMulticastStatus_Type(Integer32):
    """Custom type lgs2816crpsQosStromCtrlMulticastStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2816crpsQosStromCtrlMulticastStatus_Type.__name__ = "Integer32"
_Lgs2816crpsQosStromCtrlMulticastStatus_Object = MibScalar
lgs2816crpsQosStromCtrlMulticastStatus = _Lgs2816crpsQosStromCtrlMulticastStatus_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 17, 4, 3),
    _Lgs2816crpsQosStromCtrlMulticastStatus_Type()
)
lgs2816crpsQosStromCtrlMulticastStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsQosStromCtrlMulticastStatus.setStatus("current")
_Lgs2816crpsQosStromCtrlMulticastRate_Type = DisplayString
_Lgs2816crpsQosStromCtrlMulticastRate_Object = MibScalar
lgs2816crpsQosStromCtrlMulticastRate = _Lgs2816crpsQosStromCtrlMulticastRate_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 17, 4, 4),
    _Lgs2816crpsQosStromCtrlMulticastRate_Type()
)
lgs2816crpsQosStromCtrlMulticastRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsQosStromCtrlMulticastRate.setStatus("current")


class _Lgs2816crpsQosStromCtrlBroadcastStatus_Type(Integer32):
    """Custom type lgs2816crpsQosStromCtrlBroadcastStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2816crpsQosStromCtrlBroadcastStatus_Type.__name__ = "Integer32"
_Lgs2816crpsQosStromCtrlBroadcastStatus_Object = MibScalar
lgs2816crpsQosStromCtrlBroadcastStatus = _Lgs2816crpsQosStromCtrlBroadcastStatus_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 17, 4, 5),
    _Lgs2816crpsQosStromCtrlBroadcastStatus_Type()
)
lgs2816crpsQosStromCtrlBroadcastStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsQosStromCtrlBroadcastStatus.setStatus("current")
_Lgs2816crpsQosStromCtrlBroadcastRate_Type = DisplayString
_Lgs2816crpsQosStromCtrlBroadcastRate_Object = MibScalar
lgs2816crpsQosStromCtrlBroadcastRate = _Lgs2816crpsQosStromCtrlBroadcastRate_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 17, 4, 6),
    _Lgs2816crpsQosStromCtrlBroadcastRate_Type()
)
lgs2816crpsQosStromCtrlBroadcastRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsQosStromCtrlBroadcastRate.setStatus("current")
_Lgs2816crpsQosQCL_ObjectIdentity = ObjectIdentity
lgs2816crpsQosQCL = _Lgs2816crpsQosQCL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 17, 5)
)


class _Lgs2816crpsQosQclCreate_Type(Integer32):
    """Custom type lgs2816crpsQosQclCreate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Lgs2816crpsQosQclCreate_Type.__name__ = "Integer32"
_Lgs2816crpsQosQclCreate_Object = MibScalar
lgs2816crpsQosQclCreate = _Lgs2816crpsQosQclCreate_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 17, 5, 1),
    _Lgs2816crpsQosQclCreate_Type()
)
lgs2816crpsQosQclCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsQosQclCreate.setStatus("current")
_Lgs2816crpsQosQclTable_Object = MibTable
lgs2816crpsQosQclTable = _Lgs2816crpsQosQclTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 17, 5, 2)
)
if mibBuilder.loadTexts:
    lgs2816crpsQosQclTable.setStatus("current")
_Lgs2816crpsQosQclEntry_Object = MibTableRow
lgs2816crpsQosQclEntry = _Lgs2816crpsQosQclEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 17, 5, 2, 1)
)
lgs2816crpsQosQclEntry.setIndexNames(
    (0, "PRIVATE-LGS2816CRPS-MIB", "lgs2816crpsQosQclNo"),
    (0, "PRIVATE-LGS2816CRPS-MIB", "lgs2816crpsQosQclQceListNo"),
)
if mibBuilder.loadTexts:
    lgs2816crpsQosQclEntry.setStatus("current")


class _Lgs2816crpsQosQclNo_Type(Integer32):
    """Custom type lgs2816crpsQosQclNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Lgs2816crpsQosQclNo_Type.__name__ = "Integer32"
_Lgs2816crpsQosQclNo_Object = MibTableColumn
lgs2816crpsQosQclNo = _Lgs2816crpsQosQclNo_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 17, 5, 2, 1, 1),
    _Lgs2816crpsQosQclNo_Type()
)
lgs2816crpsQosQclNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgs2816crpsQosQclNo.setStatus("current")


class _Lgs2816crpsQosQclQceListNo_Type(Integer32):
    """Custom type lgs2816crpsQosQclQceListNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Lgs2816crpsQosQclQceListNo_Type.__name__ = "Integer32"
_Lgs2816crpsQosQclQceListNo_Object = MibTableColumn
lgs2816crpsQosQclQceListNo = _Lgs2816crpsQosQclQceListNo_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 17, 5, 2, 1, 2),
    _Lgs2816crpsQosQclQceListNo_Type()
)
lgs2816crpsQosQclQceListNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgs2816crpsQosQclQceListNo.setStatus("current")


class _Lgs2816crpsQosQclQceMoveTo_Type(Integer32):
    """Custom type lgs2816crpsQosQclQceMoveTo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Lgs2816crpsQosQclQceMoveTo_Type.__name__ = "Integer32"
_Lgs2816crpsQosQclQceMoveTo_Object = MibTableColumn
lgs2816crpsQosQclQceMoveTo = _Lgs2816crpsQosQclQceMoveTo_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 17, 5, 2, 1, 3),
    _Lgs2816crpsQosQclQceMoveTo_Type()
)
lgs2816crpsQosQclQceMoveTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsQosQclQceMoveTo.setStatus("current")


class _Lgs2816crpsQosQclQceType_Type(Integer32):
    """Custom type lgs2816crpsQosQclQceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_Lgs2816crpsQosQclQceType_Type.__name__ = "Integer32"
_Lgs2816crpsQosQclQceType_Object = MibTableColumn
lgs2816crpsQosQclQceType = _Lgs2816crpsQosQclQceType_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 17, 5, 2, 1, 4),
    _Lgs2816crpsQosQclQceType_Type()
)
lgs2816crpsQosQclQceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsQosQclQceType.setStatus("current")
_Lgs2816crpsQosQclQceValue_Type = DisplayString
_Lgs2816crpsQosQclQceValue_Object = MibTableColumn
lgs2816crpsQosQclQceValue = _Lgs2816crpsQosQclQceValue_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 17, 5, 2, 1, 5),
    _Lgs2816crpsQosQclQceValue_Type()
)
lgs2816crpsQosQclQceValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsQosQclQceValue.setStatus("current")
_Lgs2816crpsQosQclQceTrafficClass_Type = DisplayString
_Lgs2816crpsQosQclQceTrafficClass_Object = MibTableColumn
lgs2816crpsQosQclQceTrafficClass = _Lgs2816crpsQosQclQceTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 17, 5, 2, 1, 6),
    _Lgs2816crpsQosQclQceTrafficClass_Type()
)
lgs2816crpsQosQclQceTrafficClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsQosQclQceTrafficClass.setStatus("current")
_Lgs2816crpsQosQclQcePriority0Class_Type = DisplayString
_Lgs2816crpsQosQclQcePriority0Class_Object = MibTableColumn
lgs2816crpsQosQclQcePriority0Class = _Lgs2816crpsQosQclQcePriority0Class_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 17, 5, 2, 1, 7),
    _Lgs2816crpsQosQclQcePriority0Class_Type()
)
lgs2816crpsQosQclQcePriority0Class.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsQosQclQcePriority0Class.setStatus("current")
_Lgs2816crpsQosQclQcePriority1Class_Type = DisplayString
_Lgs2816crpsQosQclQcePriority1Class_Object = MibTableColumn
lgs2816crpsQosQclQcePriority1Class = _Lgs2816crpsQosQclQcePriority1Class_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 17, 5, 2, 1, 8),
    _Lgs2816crpsQosQclQcePriority1Class_Type()
)
lgs2816crpsQosQclQcePriority1Class.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsQosQclQcePriority1Class.setStatus("current")
_Lgs2816crpsQosQclQcePriority2Class_Type = DisplayString
_Lgs2816crpsQosQclQcePriority2Class_Object = MibTableColumn
lgs2816crpsQosQclQcePriority2Class = _Lgs2816crpsQosQclQcePriority2Class_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 17, 5, 2, 1, 9),
    _Lgs2816crpsQosQclQcePriority2Class_Type()
)
lgs2816crpsQosQclQcePriority2Class.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsQosQclQcePriority2Class.setStatus("current")
_Lgs2816crpsQosQclQcePriority3Class_Type = DisplayString
_Lgs2816crpsQosQclQcePriority3Class_Object = MibTableColumn
lgs2816crpsQosQclQcePriority3Class = _Lgs2816crpsQosQclQcePriority3Class_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 17, 5, 2, 1, 10),
    _Lgs2816crpsQosQclQcePriority3Class_Type()
)
lgs2816crpsQosQclQcePriority3Class.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsQosQclQcePriority3Class.setStatus("current")
_Lgs2816crpsQosQclQcePriority4Class_Type = DisplayString
_Lgs2816crpsQosQclQcePriority4Class_Object = MibTableColumn
lgs2816crpsQosQclQcePriority4Class = _Lgs2816crpsQosQclQcePriority4Class_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 17, 5, 2, 1, 11),
    _Lgs2816crpsQosQclQcePriority4Class_Type()
)
lgs2816crpsQosQclQcePriority4Class.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsQosQclQcePriority4Class.setStatus("current")
_Lgs2816crpsQosQclQcePriority5Class_Type = DisplayString
_Lgs2816crpsQosQclQcePriority5Class_Object = MibTableColumn
lgs2816crpsQosQclQcePriority5Class = _Lgs2816crpsQosQclQcePriority5Class_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 17, 5, 2, 1, 12),
    _Lgs2816crpsQosQclQcePriority5Class_Type()
)
lgs2816crpsQosQclQcePriority5Class.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsQosQclQcePriority5Class.setStatus("current")
_Lgs2816crpsQosQclQcePriority6Class_Type = DisplayString
_Lgs2816crpsQosQclQcePriority6Class_Object = MibTableColumn
lgs2816crpsQosQclQcePriority6Class = _Lgs2816crpsQosQclQcePriority6Class_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 17, 5, 2, 1, 13),
    _Lgs2816crpsQosQclQcePriority6Class_Type()
)
lgs2816crpsQosQclQcePriority6Class.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsQosQclQcePriority6Class.setStatus("current")
_Lgs2816crpsQosQclQcePriority7Class_Type = DisplayString
_Lgs2816crpsQosQclQcePriority7Class_Object = MibTableColumn
lgs2816crpsQosQclQcePriority7Class = _Lgs2816crpsQosQclQcePriority7Class_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 17, 5, 2, 1, 14),
    _Lgs2816crpsQosQclQcePriority7Class_Type()
)
lgs2816crpsQosQclQcePriority7Class.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsQosQclQcePriority7Class.setStatus("current")


class _Lgs2816crpsQosQclQceEntryAction_Type(Integer32):
    """Custom type lgs2816crpsQosQclQceEntryAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Lgs2816crpsQosQclQceEntryAction_Type.__name__ = "Integer32"
_Lgs2816crpsQosQclQceEntryAction_Object = MibTableColumn
lgs2816crpsQosQclQceEntryAction = _Lgs2816crpsQosQclQceEntryAction_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 17, 5, 2, 1, 15),
    _Lgs2816crpsQosQclQceEntryAction_Type()
)
lgs2816crpsQosQclQceEntryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsQosQclQceEntryAction.setStatus("current")
_Lgs2816crpsAclInfo_ObjectIdentity = ObjectIdentity
lgs2816crpsAclInfo = _Lgs2816crpsAclInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18)
)
_Lgs2816crpsAclPortsConfTable_Object = MibTable
lgs2816crpsAclPortsConfTable = _Lgs2816crpsAclPortsConfTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 1)
)
if mibBuilder.loadTexts:
    lgs2816crpsAclPortsConfTable.setStatus("current")
_Lgs2816crpsAclPortsConfEntry_Object = MibTableRow
lgs2816crpsAclPortsConfEntry = _Lgs2816crpsAclPortsConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 1, 1)
)
lgs2816crpsAclPortsConfEntry.setIndexNames(
    (0, "PRIVATE-LGS2816CRPS-MIB", "lgs2816crpsAclPortsConfIndex"),
)
if mibBuilder.loadTexts:
    lgs2816crpsAclPortsConfEntry.setStatus("current")


class _Lgs2816crpsAclPortsConfIndex_Type(Integer32):
    """Custom type lgs2816crpsAclPortsConfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Lgs2816crpsAclPortsConfIndex_Type.__name__ = "Integer32"
_Lgs2816crpsAclPortsConfIndex_Object = MibTableColumn
lgs2816crpsAclPortsConfIndex = _Lgs2816crpsAclPortsConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 1, 1, 1),
    _Lgs2816crpsAclPortsConfIndex_Type()
)
lgs2816crpsAclPortsConfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgs2816crpsAclPortsConfIndex.setStatus("current")


class _Lgs2816crpsAclPortsConfPolicyId_Type(Integer32):
    """Custom type lgs2816crpsAclPortsConfPolicyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Lgs2816crpsAclPortsConfPolicyId_Type.__name__ = "Integer32"
_Lgs2816crpsAclPortsConfPolicyId_Object = MibTableColumn
lgs2816crpsAclPortsConfPolicyId = _Lgs2816crpsAclPortsConfPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 1, 1, 2),
    _Lgs2816crpsAclPortsConfPolicyId_Type()
)
lgs2816crpsAclPortsConfPolicyId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsAclPortsConfPolicyId.setStatus("current")


class _Lgs2816crpsAclPortsConfAction_Type(Integer32):
    """Custom type lgs2816crpsAclPortsConfAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2816crpsAclPortsConfAction_Type.__name__ = "Integer32"
_Lgs2816crpsAclPortsConfAction_Object = MibTableColumn
lgs2816crpsAclPortsConfAction = _Lgs2816crpsAclPortsConfAction_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 1, 1, 3),
    _Lgs2816crpsAclPortsConfAction_Type()
)
lgs2816crpsAclPortsConfAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsAclPortsConfAction.setStatus("current")


class _Lgs2816crpsAclPortsConfRateLimiterId_Type(Integer32):
    """Custom type lgs2816crpsAclPortsConfRateLimiterId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_Lgs2816crpsAclPortsConfRateLimiterId_Type.__name__ = "Integer32"
_Lgs2816crpsAclPortsConfRateLimiterId_Object = MibTableColumn
lgs2816crpsAclPortsConfRateLimiterId = _Lgs2816crpsAclPortsConfRateLimiterId_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 1, 1, 4),
    _Lgs2816crpsAclPortsConfRateLimiterId_Type()
)
lgs2816crpsAclPortsConfRateLimiterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsAclPortsConfRateLimiterId.setStatus("current")


class _Lgs2816crpsAclPortsConfPortCopy_Type(Integer32):
    """Custom type lgs2816crpsAclPortsConfPortCopy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_Lgs2816crpsAclPortsConfPortCopy_Type.__name__ = "Integer32"
_Lgs2816crpsAclPortsConfPortCopy_Object = MibTableColumn
lgs2816crpsAclPortsConfPortCopy = _Lgs2816crpsAclPortsConfPortCopy_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 1, 1, 5),
    _Lgs2816crpsAclPortsConfPortCopy_Type()
)
lgs2816crpsAclPortsConfPortCopy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsAclPortsConfPortCopy.setStatus("current")
_Lgs2816crpsAclPortsConfCounter_Type = Counter32
_Lgs2816crpsAclPortsConfCounter_Object = MibTableColumn
lgs2816crpsAclPortsConfCounter = _Lgs2816crpsAclPortsConfCounter_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 1, 1, 6),
    _Lgs2816crpsAclPortsConfCounter_Type()
)
lgs2816crpsAclPortsConfCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsAclPortsConfCounter.setStatus("current")
_Lgs2816crpsAclRateLimiter_ObjectIdentity = ObjectIdentity
lgs2816crpsAclRateLimiter = _Lgs2816crpsAclRateLimiter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 2)
)
_Lgs2816crpsAclRateLimiterTable_Object = MibTable
lgs2816crpsAclRateLimiterTable = _Lgs2816crpsAclRateLimiterTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 2, 1)
)
if mibBuilder.loadTexts:
    lgs2816crpsAclRateLimiterTable.setStatus("current")
_Lgs2816crpsAclRateLimiterEntry_Object = MibTableRow
lgs2816crpsAclRateLimiterEntry = _Lgs2816crpsAclRateLimiterEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 2, 1, 1)
)
lgs2816crpsAclRateLimiterEntry.setIndexNames(
    (0, "PRIVATE-LGS2816CRPS-MIB", "lgs2816crpsAclRateLimiterIndex"),
)
if mibBuilder.loadTexts:
    lgs2816crpsAclRateLimiterEntry.setStatus("current")


class _Lgs2816crpsAclRateLimiterIndex_Type(Integer32):
    """Custom type lgs2816crpsAclRateLimiterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Lgs2816crpsAclRateLimiterIndex_Type.__name__ = "Integer32"
_Lgs2816crpsAclRateLimiterIndex_Object = MibTableColumn
lgs2816crpsAclRateLimiterIndex = _Lgs2816crpsAclRateLimiterIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 2, 1, 1, 1),
    _Lgs2816crpsAclRateLimiterIndex_Type()
)
lgs2816crpsAclRateLimiterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgs2816crpsAclRateLimiterIndex.setStatus("current")
_Lgs2816crpsAclRateLimiterRate_Type = DisplayString
_Lgs2816crpsAclRateLimiterRate_Object = MibTableColumn
lgs2816crpsAclRateLimiterRate = _Lgs2816crpsAclRateLimiterRate_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 2, 1, 1, 2),
    _Lgs2816crpsAclRateLimiterRate_Type()
)
lgs2816crpsAclRateLimiterRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsAclRateLimiterRate.setStatus("current")
_Lgs2816crpsAclInfoViewTable_Object = MibTable
lgs2816crpsAclInfoViewTable = _Lgs2816crpsAclInfoViewTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 3)
)
if mibBuilder.loadTexts:
    lgs2816crpsAclInfoViewTable.setStatus("current")
_Lgs2816crpsAclInfoViewEntry_Object = MibTableRow
lgs2816crpsAclInfoViewEntry = _Lgs2816crpsAclInfoViewEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 3, 1)
)
lgs2816crpsAclInfoViewEntry.setIndexNames(
    (0, "PRIVATE-LGS2816CRPS-MIB", "lgs2816crpsAclInfoViewNo"),
)
if mibBuilder.loadTexts:
    lgs2816crpsAclInfoViewEntry.setStatus("current")


class _Lgs2816crpsAclInfoViewNo_Type(Integer32):
    """Custom type lgs2816crpsAclInfoViewNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_Lgs2816crpsAclInfoViewNo_Type.__name__ = "Integer32"
_Lgs2816crpsAclInfoViewNo_Object = MibTableColumn
lgs2816crpsAclInfoViewNo = _Lgs2816crpsAclInfoViewNo_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 3, 1, 1),
    _Lgs2816crpsAclInfoViewNo_Type()
)
lgs2816crpsAclInfoViewNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgs2816crpsAclInfoViewNo.setStatus("current")
_Lgs2816crpsAceIngressPort_Type = DisplayString
_Lgs2816crpsAceIngressPort_Object = MibTableColumn
lgs2816crpsAceIngressPort = _Lgs2816crpsAceIngressPort_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 3, 1, 2),
    _Lgs2816crpsAceIngressPort_Type()
)
lgs2816crpsAceIngressPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsAceIngressPort.setStatus("current")
_Lgs2816crpsAceFrameType_Type = DisplayString
_Lgs2816crpsAceFrameType_Object = MibTableColumn
lgs2816crpsAceFrameType = _Lgs2816crpsAceFrameType_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 3, 1, 3),
    _Lgs2816crpsAceFrameType_Type()
)
lgs2816crpsAceFrameType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsAceFrameType.setStatus("current")
_Lgs2816crpsAceAction_Type = DisplayString
_Lgs2816crpsAceAction_Object = MibTableColumn
lgs2816crpsAceAction = _Lgs2816crpsAceAction_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 3, 1, 4),
    _Lgs2816crpsAceAction_Type()
)
lgs2816crpsAceAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsAceAction.setStatus("current")
_Lgs2816crpsAceRateLimiter_Type = DisplayString
_Lgs2816crpsAceRateLimiter_Object = MibTableColumn
lgs2816crpsAceRateLimiter = _Lgs2816crpsAceRateLimiter_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 3, 1, 5),
    _Lgs2816crpsAceRateLimiter_Type()
)
lgs2816crpsAceRateLimiter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsAceRateLimiter.setStatus("current")
_Lgs2816crpsAcePortCopy_Type = DisplayString
_Lgs2816crpsAcePortCopy_Object = MibTableColumn
lgs2816crpsAcePortCopy = _Lgs2816crpsAcePortCopy_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 3, 1, 6),
    _Lgs2816crpsAcePortCopy_Type()
)
lgs2816crpsAcePortCopy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsAcePortCopy.setStatus("current")
_Lgs2816crpsAceCounter_Type = Counter32
_Lgs2816crpsAceCounter_Object = MibTableColumn
lgs2816crpsAceCounter = _Lgs2816crpsAceCounter_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 3, 1, 7),
    _Lgs2816crpsAceCounter_Type()
)
lgs2816crpsAceCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsAceCounter.setStatus("current")
_Lgs2816crpsSmacFilter_Type = DisplayString
_Lgs2816crpsSmacFilter_Object = MibTableColumn
lgs2816crpsSmacFilter = _Lgs2816crpsSmacFilter_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 3, 1, 8),
    _Lgs2816crpsSmacFilter_Type()
)
lgs2816crpsSmacFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsSmacFilter.setStatus("current")
_Lgs2816crpsDmacFilter_Type = DisplayString
_Lgs2816crpsDmacFilter_Object = MibTableColumn
lgs2816crpsDmacFilter = _Lgs2816crpsDmacFilter_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 3, 1, 9),
    _Lgs2816crpsDmacFilter_Type()
)
lgs2816crpsDmacFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsDmacFilter.setStatus("current")
_Lgs2816crpsVlanIdFilter_Type = DisplayString
_Lgs2816crpsVlanIdFilter_Object = MibTableColumn
lgs2816crpsVlanIdFilter = _Lgs2816crpsVlanIdFilter_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 3, 1, 10),
    _Lgs2816crpsVlanIdFilter_Type()
)
lgs2816crpsVlanIdFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsVlanIdFilter.setStatus("current")
_Lgs2816crpsVlanTagPriority_Type = DisplayString
_Lgs2816crpsVlanTagPriority_Object = MibTableColumn
lgs2816crpsVlanTagPriority = _Lgs2816crpsVlanTagPriority_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 3, 1, 11),
    _Lgs2816crpsVlanTagPriority_Type()
)
lgs2816crpsVlanTagPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsVlanTagPriority.setStatus("current")
_Lgs2816crpsEtherTypeFilter_Type = DisplayString
_Lgs2816crpsEtherTypeFilter_Object = MibTableColumn
lgs2816crpsEtherTypeFilter = _Lgs2816crpsEtherTypeFilter_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 3, 1, 12),
    _Lgs2816crpsEtherTypeFilter_Type()
)
lgs2816crpsEtherTypeFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsEtherTypeFilter.setStatus("current")
_Lgs2816crpsArpRarp_Type = DisplayString
_Lgs2816crpsArpRarp_Object = MibTableColumn
lgs2816crpsArpRarp = _Lgs2816crpsArpRarp_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 3, 1, 13),
    _Lgs2816crpsArpRarp_Type()
)
lgs2816crpsArpRarp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsArpRarp.setStatus("current")
_Lgs2816crpsArpRequestReply_Type = DisplayString
_Lgs2816crpsArpRequestReply_Object = MibTableColumn
lgs2816crpsArpRequestReply = _Lgs2816crpsArpRequestReply_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 3, 1, 14),
    _Lgs2816crpsArpRequestReply_Type()
)
lgs2816crpsArpRequestReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsArpRequestReply.setStatus("current")
_Lgs2816crpsArpSenderIpFilter_Type = DisplayString
_Lgs2816crpsArpSenderIpFilter_Object = MibTableColumn
lgs2816crpsArpSenderIpFilter = _Lgs2816crpsArpSenderIpFilter_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 3, 1, 15),
    _Lgs2816crpsArpSenderIpFilter_Type()
)
lgs2816crpsArpSenderIpFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsArpSenderIpFilter.setStatus("current")
_Lgs2816crpsArpSenderIpAddress_Type = DisplayString
_Lgs2816crpsArpSenderIpAddress_Object = MibTableColumn
lgs2816crpsArpSenderIpAddress = _Lgs2816crpsArpSenderIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 3, 1, 16),
    _Lgs2816crpsArpSenderIpAddress_Type()
)
lgs2816crpsArpSenderIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsArpSenderIpAddress.setStatus("current")
_Lgs2816crpsArpSenderIpMask_Type = DisplayString
_Lgs2816crpsArpSenderIpMask_Object = MibTableColumn
lgs2816crpsArpSenderIpMask = _Lgs2816crpsArpSenderIpMask_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 3, 1, 17),
    _Lgs2816crpsArpSenderIpMask_Type()
)
lgs2816crpsArpSenderIpMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsArpSenderIpMask.setStatus("current")
_Lgs2816crpsArpTargetIpFilter_Type = DisplayString
_Lgs2816crpsArpTargetIpFilter_Object = MibTableColumn
lgs2816crpsArpTargetIpFilter = _Lgs2816crpsArpTargetIpFilter_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 3, 1, 18),
    _Lgs2816crpsArpTargetIpFilter_Type()
)
lgs2816crpsArpTargetIpFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsArpTargetIpFilter.setStatus("current")
_Lgs2816crpsArpTargetIpAddress_Type = DisplayString
_Lgs2816crpsArpTargetIpAddress_Object = MibTableColumn
lgs2816crpsArpTargetIpAddress = _Lgs2816crpsArpTargetIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 3, 1, 19),
    _Lgs2816crpsArpTargetIpAddress_Type()
)
lgs2816crpsArpTargetIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsArpTargetIpAddress.setStatus("current")
_Lgs2816crpsArpTargetIpMask_Type = DisplayString
_Lgs2816crpsArpTargetIpMask_Object = MibTableColumn
lgs2816crpsArpTargetIpMask = _Lgs2816crpsArpTargetIpMask_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 3, 1, 20),
    _Lgs2816crpsArpTargetIpMask_Type()
)
lgs2816crpsArpTargetIpMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsArpTargetIpMask.setStatus("current")
_Lgs2816crpsArpSmacMatch_Type = DisplayString
_Lgs2816crpsArpSmacMatch_Object = MibTableColumn
lgs2816crpsArpSmacMatch = _Lgs2816crpsArpSmacMatch_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 3, 1, 21),
    _Lgs2816crpsArpSmacMatch_Type()
)
lgs2816crpsArpSmacMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsArpSmacMatch.setStatus("current")
_Lgs2816crpsArpRarpDmacMatch_Type = DisplayString
_Lgs2816crpsArpRarpDmacMatch_Object = MibTableColumn
lgs2816crpsArpRarpDmacMatch = _Lgs2816crpsArpRarpDmacMatch_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 3, 1, 22),
    _Lgs2816crpsArpRarpDmacMatch_Type()
)
lgs2816crpsArpRarpDmacMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsArpRarpDmacMatch.setStatus("current")
_Lgs2816crpsArpIpEthernetLength_Type = DisplayString
_Lgs2816crpsArpIpEthernetLength_Object = MibTableColumn
lgs2816crpsArpIpEthernetLength = _Lgs2816crpsArpIpEthernetLength_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 3, 1, 23),
    _Lgs2816crpsArpIpEthernetLength_Type()
)
lgs2816crpsArpIpEthernetLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsArpIpEthernetLength.setStatus("current")
_Lgs2816crpsArpIp_Type = DisplayString
_Lgs2816crpsArpIp_Object = MibTableColumn
lgs2816crpsArpIp = _Lgs2816crpsArpIp_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 3, 1, 24),
    _Lgs2816crpsArpIp_Type()
)
lgs2816crpsArpIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsArpIp.setStatus("current")
_Lgs2816crpsArpEthernet_Type = DisplayString
_Lgs2816crpsArpEthernet_Object = MibTableColumn
lgs2816crpsArpEthernet = _Lgs2816crpsArpEthernet_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 3, 1, 25),
    _Lgs2816crpsArpEthernet_Type()
)
lgs2816crpsArpEthernet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsArpEthernet.setStatus("current")
_Lgs2816crpsIpProtocolFilter_Type = DisplayString
_Lgs2816crpsIpProtocolFilter_Object = MibTableColumn
lgs2816crpsIpProtocolFilter = _Lgs2816crpsIpProtocolFilter_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 3, 1, 26),
    _Lgs2816crpsIpProtocolFilter_Type()
)
lgs2816crpsIpProtocolFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsIpProtocolFilter.setStatus("current")
_Lgs2816crpsIpProtocolValue_Type = DisplayString
_Lgs2816crpsIpProtocolValue_Object = MibTableColumn
lgs2816crpsIpProtocolValue = _Lgs2816crpsIpProtocolValue_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 3, 1, 27),
    _Lgs2816crpsIpProtocolValue_Type()
)
lgs2816crpsIpProtocolValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsIpProtocolValue.setStatus("current")
_Lgs2816crpsIpTTL_Type = DisplayString
_Lgs2816crpsIpTTL_Object = MibTableColumn
lgs2816crpsIpTTL = _Lgs2816crpsIpTTL_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 3, 1, 28),
    _Lgs2816crpsIpTTL_Type()
)
lgs2816crpsIpTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsIpTTL.setStatus("current")
_Lgs2816crpsIpFragment_Type = DisplayString
_Lgs2816crpsIpFragment_Object = MibTableColumn
lgs2816crpsIpFragment = _Lgs2816crpsIpFragment_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 3, 1, 29),
    _Lgs2816crpsIpFragment_Type()
)
lgs2816crpsIpFragment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsIpFragment.setStatus("current")
_Lgs2816crpsIpOption_Type = DisplayString
_Lgs2816crpsIpOption_Object = MibTableColumn
lgs2816crpsIpOption = _Lgs2816crpsIpOption_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 3, 1, 30),
    _Lgs2816crpsIpOption_Type()
)
lgs2816crpsIpOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsIpOption.setStatus("current")
_Lgs2816crpsSipFilter_Type = DisplayString
_Lgs2816crpsSipFilter_Object = MibTableColumn
lgs2816crpsSipFilter = _Lgs2816crpsSipFilter_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 3, 1, 31),
    _Lgs2816crpsSipFilter_Type()
)
lgs2816crpsSipFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsSipFilter.setStatus("current")
_Lgs2816crpsSipAddress_Type = DisplayString
_Lgs2816crpsSipAddress_Object = MibTableColumn
lgs2816crpsSipAddress = _Lgs2816crpsSipAddress_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 3, 1, 32),
    _Lgs2816crpsSipAddress_Type()
)
lgs2816crpsSipAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsSipAddress.setStatus("current")
_Lgs2816crpsSipMask_Type = DisplayString
_Lgs2816crpsSipMask_Object = MibTableColumn
lgs2816crpsSipMask = _Lgs2816crpsSipMask_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 3, 1, 33),
    _Lgs2816crpsSipMask_Type()
)
lgs2816crpsSipMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsSipMask.setStatus("current")
_Lgs2816crpsDipFilter_Type = DisplayString
_Lgs2816crpsDipFilter_Object = MibTableColumn
lgs2816crpsDipFilter = _Lgs2816crpsDipFilter_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 3, 1, 34),
    _Lgs2816crpsDipFilter_Type()
)
lgs2816crpsDipFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsDipFilter.setStatus("current")
_Lgs2816crpsDipAddress_Type = DisplayString
_Lgs2816crpsDipAddress_Object = MibTableColumn
lgs2816crpsDipAddress = _Lgs2816crpsDipAddress_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 3, 1, 35),
    _Lgs2816crpsDipAddress_Type()
)
lgs2816crpsDipAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsDipAddress.setStatus("current")
_Lgs2816crpsDipMask_Type = DisplayString
_Lgs2816crpsDipMask_Object = MibTableColumn
lgs2816crpsDipMask = _Lgs2816crpsDipMask_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 3, 1, 36),
    _Lgs2816crpsDipMask_Type()
)
lgs2816crpsDipMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsDipMask.setStatus("current")
_Lgs2816crpsIcmpTypeFilter_Type = DisplayString
_Lgs2816crpsIcmpTypeFilter_Object = MibTableColumn
lgs2816crpsIcmpTypeFilter = _Lgs2816crpsIcmpTypeFilter_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 3, 1, 37),
    _Lgs2816crpsIcmpTypeFilter_Type()
)
lgs2816crpsIcmpTypeFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsIcmpTypeFilter.setStatus("current")
_Lgs2816crpsIcmpCodeFilter_Type = DisplayString
_Lgs2816crpsIcmpCodeFilter_Object = MibTableColumn
lgs2816crpsIcmpCodeFilter = _Lgs2816crpsIcmpCodeFilter_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 3, 1, 38),
    _Lgs2816crpsIcmpCodeFilter_Type()
)
lgs2816crpsIcmpCodeFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsIcmpCodeFilter.setStatus("current")
_Lgs2816crpsUdpSourcePortFilter_Type = DisplayString
_Lgs2816crpsUdpSourcePortFilter_Object = MibTableColumn
lgs2816crpsUdpSourcePortFilter = _Lgs2816crpsUdpSourcePortFilter_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 3, 1, 39),
    _Lgs2816crpsUdpSourcePortFilter_Type()
)
lgs2816crpsUdpSourcePortFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsUdpSourcePortFilter.setStatus("current")
_Lgs2816crpsUdpDestPortFilter_Type = DisplayString
_Lgs2816crpsUdpDestPortFilter_Object = MibTableColumn
lgs2816crpsUdpDestPortFilter = _Lgs2816crpsUdpDestPortFilter_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 3, 1, 40),
    _Lgs2816crpsUdpDestPortFilter_Type()
)
lgs2816crpsUdpDestPortFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsUdpDestPortFilter.setStatus("current")
_Lgs2816crpsTcpSourcePortFilter_Type = DisplayString
_Lgs2816crpsTcpSourcePortFilter_Object = MibTableColumn
lgs2816crpsTcpSourcePortFilter = _Lgs2816crpsTcpSourcePortFilter_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 3, 1, 41),
    _Lgs2816crpsTcpSourcePortFilter_Type()
)
lgs2816crpsTcpSourcePortFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsTcpSourcePortFilter.setStatus("current")
_Lgs2816crpsTcpDestPortFilter_Type = DisplayString
_Lgs2816crpsTcpDestPortFilter_Object = MibTableColumn
lgs2816crpsTcpDestPortFilter = _Lgs2816crpsTcpDestPortFilter_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 3, 1, 42),
    _Lgs2816crpsTcpDestPortFilter_Type()
)
lgs2816crpsTcpDestPortFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsTcpDestPortFilter.setStatus("current")
_Lgs2816crpsTcpFIN_Type = DisplayString
_Lgs2816crpsTcpFIN_Object = MibTableColumn
lgs2816crpsTcpFIN = _Lgs2816crpsTcpFIN_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 3, 1, 43),
    _Lgs2816crpsTcpFIN_Type()
)
lgs2816crpsTcpFIN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsTcpFIN.setStatus("current")
_Lgs2816crpsTcpSYN_Type = DisplayString
_Lgs2816crpsTcpSYN_Object = MibTableColumn
lgs2816crpsTcpSYN = _Lgs2816crpsTcpSYN_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 3, 1, 44),
    _Lgs2816crpsTcpSYN_Type()
)
lgs2816crpsTcpSYN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsTcpSYN.setStatus("current")
_Lgs2816crpsTcpRST_Type = DisplayString
_Lgs2816crpsTcpRST_Object = MibTableColumn
lgs2816crpsTcpRST = _Lgs2816crpsTcpRST_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 3, 1, 45),
    _Lgs2816crpsTcpRST_Type()
)
lgs2816crpsTcpRST.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsTcpRST.setStatus("current")
_Lgs2816crpsTcpPSH_Type = DisplayString
_Lgs2816crpsTcpPSH_Object = MibTableColumn
lgs2816crpsTcpPSH = _Lgs2816crpsTcpPSH_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 3, 1, 46),
    _Lgs2816crpsTcpPSH_Type()
)
lgs2816crpsTcpPSH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsTcpPSH.setStatus("current")
_Lgs2816crpsTcpACK_Type = DisplayString
_Lgs2816crpsTcpACK_Object = MibTableColumn
lgs2816crpsTcpACK = _Lgs2816crpsTcpACK_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 3, 1, 47),
    _Lgs2816crpsTcpACK_Type()
)
lgs2816crpsTcpACK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsTcpACK.setStatus("current")
_Lgs2816crpsTcpURG_Type = DisplayString
_Lgs2816crpsTcpURG_Object = MibTableColumn
lgs2816crpsTcpURG = _Lgs2816crpsTcpURG_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 3, 1, 48),
    _Lgs2816crpsTcpURG_Type()
)
lgs2816crpsTcpURG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsTcpURG.setStatus("current")


class _Lgs2816crpsAclInfoEntryAction_Type(Integer32):
    """Custom type lgs2816crpsAclInfoEntryAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Lgs2816crpsAclInfoEntryAction_Type.__name__ = "Integer32"
_Lgs2816crpsAclInfoEntryAction_Object = MibTableColumn
lgs2816crpsAclInfoEntryAction = _Lgs2816crpsAclInfoEntryAction_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 3, 1, 49),
    _Lgs2816crpsAclInfoEntryAction_Type()
)
lgs2816crpsAclInfoEntryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsAclInfoEntryAction.setStatus("current")
_Lgs2816crpsAclInfoConf_ObjectIdentity = ObjectIdentity
lgs2816crpsAclInfoConf = _Lgs2816crpsAclInfoConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 4)
)


class _Lgs2816crpsAceNo_Type(Integer32):
    """Custom type lgs2816crpsAceNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Lgs2816crpsAceNo_Type.__name__ = "Integer32"
_Lgs2816crpsAceNo_Object = MibScalar
lgs2816crpsAceNo = _Lgs2816crpsAceNo_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 4, 1),
    _Lgs2816crpsAceNo_Type()
)
lgs2816crpsAceNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsAceNo.setStatus("current")


class _Lgs2816crpsAceMoveTo_Type(Integer32):
    """Custom type lgs2816crpsAceMoveTo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_Lgs2816crpsAceMoveTo_Type.__name__ = "Integer32"
_Lgs2816crpsAceMoveTo_Object = MibScalar
lgs2816crpsAceMoveTo = _Lgs2816crpsAceMoveTo_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 4, 2),
    _Lgs2816crpsAceMoveTo_Type()
)
lgs2816crpsAceMoveTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsAceMoveTo.setStatus("current")
_Lgs2816crpsAceIngressPortConf_Type = DisplayString
_Lgs2816crpsAceIngressPortConf_Object = MibScalar
lgs2816crpsAceIngressPortConf = _Lgs2816crpsAceIngressPortConf_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 4, 3),
    _Lgs2816crpsAceIngressPortConf_Type()
)
lgs2816crpsAceIngressPortConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsAceIngressPortConf.setStatus("current")


class _Lgs2816crpsAceFrameTypeConf_Type(Integer32):
    """Custom type lgs2816crpsAceFrameTypeConf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Lgs2816crpsAceFrameTypeConf_Type.__name__ = "Integer32"
_Lgs2816crpsAceFrameTypeConf_Object = MibScalar
lgs2816crpsAceFrameTypeConf = _Lgs2816crpsAceFrameTypeConf_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 4, 4),
    _Lgs2816crpsAceFrameTypeConf_Type()
)
lgs2816crpsAceFrameTypeConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsAceFrameTypeConf.setStatus("current")
_Lgs2816crpsAceFrameTypeParameters_ObjectIdentity = ObjectIdentity
lgs2816crpsAceFrameTypeParameters = _Lgs2816crpsAceFrameTypeParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 4, 5)
)
_Lgs2816crpsEthernetTypeFilter_Type = DisplayString
_Lgs2816crpsEthernetTypeFilter_Object = MibScalar
lgs2816crpsEthernetTypeFilter = _Lgs2816crpsEthernetTypeFilter_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 4, 5, 1),
    _Lgs2816crpsEthernetTypeFilter_Type()
)
lgs2816crpsEthernetTypeFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsEthernetTypeFilter.setStatus("current")
_Lgs2816crpsAclArpParameters_ObjectIdentity = ObjectIdentity
lgs2816crpsAclArpParameters = _Lgs2816crpsAclArpParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 4, 5, 2)
)


class _Lgs2816crpsAceArpRarp_Type(Integer32):
    """Custom type lgs2816crpsAceArpRarp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Lgs2816crpsAceArpRarp_Type.__name__ = "Integer32"
_Lgs2816crpsAceArpRarp_Object = MibScalar
lgs2816crpsAceArpRarp = _Lgs2816crpsAceArpRarp_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 4, 5, 2, 1),
    _Lgs2816crpsAceArpRarp_Type()
)
lgs2816crpsAceArpRarp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsAceArpRarp.setStatus("current")


class _Lgs2816crpsAceArpRequestReply_Type(Integer32):
    """Custom type lgs2816crpsAceArpRequestReply based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Lgs2816crpsAceArpRequestReply_Type.__name__ = "Integer32"
_Lgs2816crpsAceArpRequestReply_Object = MibScalar
lgs2816crpsAceArpRequestReply = _Lgs2816crpsAceArpRequestReply_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 4, 5, 2, 2),
    _Lgs2816crpsAceArpRequestReply_Type()
)
lgs2816crpsAceArpRequestReply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsAceArpRequestReply.setStatus("current")


class _Lgs2816crpsAceArpSenderIpFilter_Type(Integer32):
    """Custom type lgs2816crpsAceArpSenderIpFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Lgs2816crpsAceArpSenderIpFilter_Type.__name__ = "Integer32"
_Lgs2816crpsAceArpSenderIpFilter_Object = MibScalar
lgs2816crpsAceArpSenderIpFilter = _Lgs2816crpsAceArpSenderIpFilter_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 4, 5, 2, 3),
    _Lgs2816crpsAceArpSenderIpFilter_Type()
)
lgs2816crpsAceArpSenderIpFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsAceArpSenderIpFilter.setStatus("current")
_Lgs2816crpsAceArpSenderIpAddress_Type = DisplayString
_Lgs2816crpsAceArpSenderIpAddress_Object = MibScalar
lgs2816crpsAceArpSenderIpAddress = _Lgs2816crpsAceArpSenderIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 4, 5, 2, 4),
    _Lgs2816crpsAceArpSenderIpAddress_Type()
)
lgs2816crpsAceArpSenderIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsAceArpSenderIpAddress.setStatus("current")
_Lgs2816crpsAceArpSenderIpMask_Type = DisplayString
_Lgs2816crpsAceArpSenderIpMask_Object = MibScalar
lgs2816crpsAceArpSenderIpMask = _Lgs2816crpsAceArpSenderIpMask_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 4, 5, 2, 5),
    _Lgs2816crpsAceArpSenderIpMask_Type()
)
lgs2816crpsAceArpSenderIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsAceArpSenderIpMask.setStatus("current")


class _Lgs2816crpsAceArpTargetIpFilter_Type(Integer32):
    """Custom type lgs2816crpsAceArpTargetIpFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Lgs2816crpsAceArpTargetIpFilter_Type.__name__ = "Integer32"
_Lgs2816crpsAceArpTargetIpFilter_Object = MibScalar
lgs2816crpsAceArpTargetIpFilter = _Lgs2816crpsAceArpTargetIpFilter_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 4, 5, 2, 6),
    _Lgs2816crpsAceArpTargetIpFilter_Type()
)
lgs2816crpsAceArpTargetIpFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsAceArpTargetIpFilter.setStatus("current")
_Lgs2816crpsAceArpTargetIpAddress_Type = DisplayString
_Lgs2816crpsAceArpTargetIpAddress_Object = MibScalar
lgs2816crpsAceArpTargetIpAddress = _Lgs2816crpsAceArpTargetIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 4, 5, 2, 7),
    _Lgs2816crpsAceArpTargetIpAddress_Type()
)
lgs2816crpsAceArpTargetIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsAceArpTargetIpAddress.setStatus("current")
_Lgs2816crpsAceArpTargetIpMask_Type = DisplayString
_Lgs2816crpsAceArpTargetIpMask_Object = MibScalar
lgs2816crpsAceArpTargetIpMask = _Lgs2816crpsAceArpTargetIpMask_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 4, 5, 2, 8),
    _Lgs2816crpsAceArpTargetIpMask_Type()
)
lgs2816crpsAceArpTargetIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsAceArpTargetIpMask.setStatus("current")
_Lgs2816crpsAceArpSmacMatch_Type = DisplayString
_Lgs2816crpsAceArpSmacMatch_Object = MibScalar
lgs2816crpsAceArpSmacMatch = _Lgs2816crpsAceArpSmacMatch_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 4, 5, 2, 9),
    _Lgs2816crpsAceArpSmacMatch_Type()
)
lgs2816crpsAceArpSmacMatch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsAceArpSmacMatch.setStatus("current")
_Lgs2816crpsAceArpRarpDmacMatch_Type = DisplayString
_Lgs2816crpsAceArpRarpDmacMatch_Object = MibScalar
lgs2816crpsAceArpRarpDmacMatch = _Lgs2816crpsAceArpRarpDmacMatch_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 4, 5, 2, 10),
    _Lgs2816crpsAceArpRarpDmacMatch_Type()
)
lgs2816crpsAceArpRarpDmacMatch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsAceArpRarpDmacMatch.setStatus("current")
_Lgs2816crpsAceArpIpEthernetLength_Type = DisplayString
_Lgs2816crpsAceArpIpEthernetLength_Object = MibScalar
lgs2816crpsAceArpIpEthernetLength = _Lgs2816crpsAceArpIpEthernetLength_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 4, 5, 2, 11),
    _Lgs2816crpsAceArpIpEthernetLength_Type()
)
lgs2816crpsAceArpIpEthernetLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsAceArpIpEthernetLength.setStatus("current")
_Lgs2816crpsAceArpIp_Type = DisplayString
_Lgs2816crpsAceArpIp_Object = MibScalar
lgs2816crpsAceArpIp = _Lgs2816crpsAceArpIp_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 4, 5, 2, 12),
    _Lgs2816crpsAceArpIp_Type()
)
lgs2816crpsAceArpIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsAceArpIp.setStatus("current")
_Lgs2816crpsAceArpEthernet_Type = DisplayString
_Lgs2816crpsAceArpEthernet_Object = MibScalar
lgs2816crpsAceArpEthernet = _Lgs2816crpsAceArpEthernet_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 4, 5, 2, 13),
    _Lgs2816crpsAceArpEthernet_Type()
)
lgs2816crpsAceArpEthernet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsAceArpEthernet.setStatus("current")
_Lgs2816crpsAclIpParameters_ObjectIdentity = ObjectIdentity
lgs2816crpsAclIpParameters = _Lgs2816crpsAclIpParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 4, 5, 3)
)


class _Lgs2816crpsAceIpProtocolFilter_Type(Integer32):
    """Custom type lgs2816crpsAceIpProtocolFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_Lgs2816crpsAceIpProtocolFilter_Type.__name__ = "Integer32"
_Lgs2816crpsAceIpProtocolFilter_Object = MibScalar
lgs2816crpsAceIpProtocolFilter = _Lgs2816crpsAceIpProtocolFilter_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 4, 5, 3, 1),
    _Lgs2816crpsAceIpProtocolFilter_Type()
)
lgs2816crpsAceIpProtocolFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsAceIpProtocolFilter.setStatus("current")
_Lgs2816crpsAceIpProtocolFilterParameters_ObjectIdentity = ObjectIdentity
lgs2816crpsAceIpProtocolFilterParameters = _Lgs2816crpsAceIpProtocolFilterParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 4, 5, 3, 2)
)
_Lgs2816crpsAceIcmpParameters_ObjectIdentity = ObjectIdentity
lgs2816crpsAceIcmpParameters = _Lgs2816crpsAceIcmpParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 4, 5, 3, 2, 1)
)
_Lgs2816crpsAceIcmpTypeFilter_Type = DisplayString
_Lgs2816crpsAceIcmpTypeFilter_Object = MibScalar
lgs2816crpsAceIcmpTypeFilter = _Lgs2816crpsAceIcmpTypeFilter_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 4, 5, 3, 2, 1, 1),
    _Lgs2816crpsAceIcmpTypeFilter_Type()
)
lgs2816crpsAceIcmpTypeFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsAceIcmpTypeFilter.setStatus("current")
_Lgs2816crpsAceIcmpCodeFilter_Type = DisplayString
_Lgs2816crpsAceIcmpCodeFilter_Object = MibScalar
lgs2816crpsAceIcmpCodeFilter = _Lgs2816crpsAceIcmpCodeFilter_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 4, 5, 3, 2, 1, 2),
    _Lgs2816crpsAceIcmpCodeFilter_Type()
)
lgs2816crpsAceIcmpCodeFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsAceIcmpCodeFilter.setStatus("current")
_Lgs2816crpsAceUdpParameters_ObjectIdentity = ObjectIdentity
lgs2816crpsAceUdpParameters = _Lgs2816crpsAceUdpParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 4, 5, 3, 2, 2)
)
_Lgs2816crpsUdpSourcePortFilterConf_Type = DisplayString
_Lgs2816crpsUdpSourcePortFilterConf_Object = MibScalar
lgs2816crpsUdpSourcePortFilterConf = _Lgs2816crpsUdpSourcePortFilterConf_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 4, 5, 3, 2, 2, 1),
    _Lgs2816crpsUdpSourcePortFilterConf_Type()
)
lgs2816crpsUdpSourcePortFilterConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsUdpSourcePortFilterConf.setStatus("current")
_Lgs2816crpsUdpDestPortFilterConf_Type = DisplayString
_Lgs2816crpsUdpDestPortFilterConf_Object = MibScalar
lgs2816crpsUdpDestPortFilterConf = _Lgs2816crpsUdpDestPortFilterConf_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 4, 5, 3, 2, 2, 2),
    _Lgs2816crpsUdpDestPortFilterConf_Type()
)
lgs2816crpsUdpDestPortFilterConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsUdpDestPortFilterConf.setStatus("current")
_Lgs2816crpsAceTcpParameters_ObjectIdentity = ObjectIdentity
lgs2816crpsAceTcpParameters = _Lgs2816crpsAceTcpParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 4, 5, 3, 2, 3)
)
_Lgs2816crpsTcpSourcePortFilterConf_Type = DisplayString
_Lgs2816crpsTcpSourcePortFilterConf_Object = MibScalar
lgs2816crpsTcpSourcePortFilterConf = _Lgs2816crpsTcpSourcePortFilterConf_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 4, 5, 3, 2, 3, 1),
    _Lgs2816crpsTcpSourcePortFilterConf_Type()
)
lgs2816crpsTcpSourcePortFilterConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsTcpSourcePortFilterConf.setStatus("current")
_Lgs2816crpsTcpDestPortFilterConf_Type = DisplayString
_Lgs2816crpsTcpDestPortFilterConf_Object = MibScalar
lgs2816crpsTcpDestPortFilterConf = _Lgs2816crpsTcpDestPortFilterConf_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 4, 5, 3, 2, 3, 2),
    _Lgs2816crpsTcpDestPortFilterConf_Type()
)
lgs2816crpsTcpDestPortFilterConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsTcpDestPortFilterConf.setStatus("current")
_Lgs2816crpsTcpFINConf_Type = DisplayString
_Lgs2816crpsTcpFINConf_Object = MibScalar
lgs2816crpsTcpFINConf = _Lgs2816crpsTcpFINConf_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 4, 5, 3, 2, 3, 3),
    _Lgs2816crpsTcpFINConf_Type()
)
lgs2816crpsTcpFINConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsTcpFINConf.setStatus("current")
_Lgs2816crpsTcpSYNConf_Type = DisplayString
_Lgs2816crpsTcpSYNConf_Object = MibScalar
lgs2816crpsTcpSYNConf = _Lgs2816crpsTcpSYNConf_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 4, 5, 3, 2, 3, 4),
    _Lgs2816crpsTcpSYNConf_Type()
)
lgs2816crpsTcpSYNConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsTcpSYNConf.setStatus("current")
_Lgs2816crpsTcpRSTConf_Type = DisplayString
_Lgs2816crpsTcpRSTConf_Object = MibScalar
lgs2816crpsTcpRSTConf = _Lgs2816crpsTcpRSTConf_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 4, 5, 3, 2, 3, 5),
    _Lgs2816crpsTcpRSTConf_Type()
)
lgs2816crpsTcpRSTConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsTcpRSTConf.setStatus("current")
_Lgs2816crpsTcpPSHConf_Type = DisplayString
_Lgs2816crpsTcpPSHConf_Object = MibScalar
lgs2816crpsTcpPSHConf = _Lgs2816crpsTcpPSHConf_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 4, 5, 3, 2, 3, 6),
    _Lgs2816crpsTcpPSHConf_Type()
)
lgs2816crpsTcpPSHConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsTcpPSHConf.setStatus("current")
_Lgs2816crpsTcpACKConf_Type = DisplayString
_Lgs2816crpsTcpACKConf_Object = MibScalar
lgs2816crpsTcpACKConf = _Lgs2816crpsTcpACKConf_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 4, 5, 3, 2, 3, 7),
    _Lgs2816crpsTcpACKConf_Type()
)
lgs2816crpsTcpACKConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsTcpACKConf.setStatus("current")
_Lgs2816crpsTcpURGConf_Type = DisplayString
_Lgs2816crpsTcpURGConf_Object = MibScalar
lgs2816crpsTcpURGConf = _Lgs2816crpsTcpURGConf_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 4, 5, 3, 2, 3, 8),
    _Lgs2816crpsTcpURGConf_Type()
)
lgs2816crpsTcpURGConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsTcpURGConf.setStatus("current")


class _Lgs2816crpsAceIpProtocolValue_Type(Integer32):
    """Custom type lgs2816crpsAceIpProtocolValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_Lgs2816crpsAceIpProtocolValue_Type.__name__ = "Integer32"
_Lgs2816crpsAceIpProtocolValue_Object = MibScalar
lgs2816crpsAceIpProtocolValue = _Lgs2816crpsAceIpProtocolValue_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 4, 5, 3, 3),
    _Lgs2816crpsAceIpProtocolValue_Type()
)
lgs2816crpsAceIpProtocolValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsAceIpProtocolValue.setStatus("current")
_Lgs2816crpsAceIpTTL_Type = DisplayString
_Lgs2816crpsAceIpTTL_Object = MibScalar
lgs2816crpsAceIpTTL = _Lgs2816crpsAceIpTTL_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 4, 5, 3, 4),
    _Lgs2816crpsAceIpTTL_Type()
)
lgs2816crpsAceIpTTL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsAceIpTTL.setStatus("current")
_Lgs2816crpsAceIpFragment_Type = DisplayString
_Lgs2816crpsAceIpFragment_Object = MibScalar
lgs2816crpsAceIpFragment = _Lgs2816crpsAceIpFragment_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 4, 5, 3, 5),
    _Lgs2816crpsAceIpFragment_Type()
)
lgs2816crpsAceIpFragment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsAceIpFragment.setStatus("current")
_Lgs2816crpsAceIpOption_Type = DisplayString
_Lgs2816crpsAceIpOption_Object = MibScalar
lgs2816crpsAceIpOption = _Lgs2816crpsAceIpOption_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 4, 5, 3, 6),
    _Lgs2816crpsAceIpOption_Type()
)
lgs2816crpsAceIpOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsAceIpOption.setStatus("current")


class _Lgs2816crpsAceSipFilter_Type(Integer32):
    """Custom type lgs2816crpsAceSipFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Lgs2816crpsAceSipFilter_Type.__name__ = "Integer32"
_Lgs2816crpsAceSipFilter_Object = MibScalar
lgs2816crpsAceSipFilter = _Lgs2816crpsAceSipFilter_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 4, 5, 3, 7),
    _Lgs2816crpsAceSipFilter_Type()
)
lgs2816crpsAceSipFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsAceSipFilter.setStatus("current")
_Lgs2816crpsAceSipAddress_Type = DisplayString
_Lgs2816crpsAceSipAddress_Object = MibScalar
lgs2816crpsAceSipAddress = _Lgs2816crpsAceSipAddress_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 4, 5, 3, 8),
    _Lgs2816crpsAceSipAddress_Type()
)
lgs2816crpsAceSipAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsAceSipAddress.setStatus("current")
_Lgs2816crpsAceSipMask_Type = DisplayString
_Lgs2816crpsAceSipMask_Object = MibScalar
lgs2816crpsAceSipMask = _Lgs2816crpsAceSipMask_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 4, 5, 3, 9),
    _Lgs2816crpsAceSipMask_Type()
)
lgs2816crpsAceSipMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsAceSipMask.setStatus("current")


class _Lgs2816crpsAceDipFilter_Type(Integer32):
    """Custom type lgs2816crpsAceDipFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Lgs2816crpsAceDipFilter_Type.__name__ = "Integer32"
_Lgs2816crpsAceDipFilter_Object = MibScalar
lgs2816crpsAceDipFilter = _Lgs2816crpsAceDipFilter_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 4, 5, 3, 10),
    _Lgs2816crpsAceDipFilter_Type()
)
lgs2816crpsAceDipFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsAceDipFilter.setStatus("current")
_Lgs2816crpsAceDipAddress_Type = DisplayString
_Lgs2816crpsAceDipAddress_Object = MibScalar
lgs2816crpsAceDipAddress = _Lgs2816crpsAceDipAddress_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 4, 5, 3, 11),
    _Lgs2816crpsAceDipAddress_Type()
)
lgs2816crpsAceDipAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsAceDipAddress.setStatus("current")
_Lgs2816crpsAceDipMask_Type = DisplayString
_Lgs2816crpsAceDipMask_Object = MibScalar
lgs2816crpsAceDipMask = _Lgs2816crpsAceDipMask_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 4, 5, 3, 12),
    _Lgs2816crpsAceDipMask_Type()
)
lgs2816crpsAceDipMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsAceDipMask.setStatus("current")


class _Lgs2816crpsAceActionConf_Type(Integer32):
    """Custom type lgs2816crpsAceActionConf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2816crpsAceActionConf_Type.__name__ = "Integer32"
_Lgs2816crpsAceActionConf_Object = MibScalar
lgs2816crpsAceActionConf = _Lgs2816crpsAceActionConf_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 4, 6),
    _Lgs2816crpsAceActionConf_Type()
)
lgs2816crpsAceActionConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsAceActionConf.setStatus("current")


class _Lgs2816crpsAceRateLimiterConf_Type(Integer32):
    """Custom type lgs2816crpsAceRateLimiterConf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_Lgs2816crpsAceRateLimiterConf_Type.__name__ = "Integer32"
_Lgs2816crpsAceRateLimiterConf_Object = MibScalar
lgs2816crpsAceRateLimiterConf = _Lgs2816crpsAceRateLimiterConf_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 4, 7),
    _Lgs2816crpsAceRateLimiterConf_Type()
)
lgs2816crpsAceRateLimiterConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsAceRateLimiterConf.setStatus("current")


class _Lgs2816crpsAcePortCopyConf_Type(Integer32):
    """Custom type lgs2816crpsAcePortCopyConf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_Lgs2816crpsAcePortCopyConf_Type.__name__ = "Integer32"
_Lgs2816crpsAcePortCopyConf_Object = MibScalar
lgs2816crpsAcePortCopyConf = _Lgs2816crpsAcePortCopyConf_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 4, 8),
    _Lgs2816crpsAcePortCopyConf_Type()
)
lgs2816crpsAcePortCopyConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsAcePortCopyConf.setStatus("current")
_Lgs2816crpsAceMacParameters_ObjectIdentity = ObjectIdentity
lgs2816crpsAceMacParameters = _Lgs2816crpsAceMacParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 4, 9)
)
_Lgs2816crpsAceSmacFilter_Type = DisplayString
_Lgs2816crpsAceSmacFilter_Object = MibScalar
lgs2816crpsAceSmacFilter = _Lgs2816crpsAceSmacFilter_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 4, 9, 1),
    _Lgs2816crpsAceSmacFilter_Type()
)
lgs2816crpsAceSmacFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsAceSmacFilter.setStatus("current")
_Lgs2816crpsAceDmacFilter_Type = DisplayString
_Lgs2816crpsAceDmacFilter_Object = MibScalar
lgs2816crpsAceDmacFilter = _Lgs2816crpsAceDmacFilter_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 4, 9, 2),
    _Lgs2816crpsAceDmacFilter_Type()
)
lgs2816crpsAceDmacFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsAceDmacFilter.setStatus("current")
_Lgs2816crpsAceVlanParameters_ObjectIdentity = ObjectIdentity
lgs2816crpsAceVlanParameters = _Lgs2816crpsAceVlanParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 4, 10)
)
_Lgs2816crpsAceVlanIdFilter_Type = DisplayString
_Lgs2816crpsAceVlanIdFilter_Object = MibScalar
lgs2816crpsAceVlanIdFilter = _Lgs2816crpsAceVlanIdFilter_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 4, 10, 1),
    _Lgs2816crpsAceVlanIdFilter_Type()
)
lgs2816crpsAceVlanIdFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsAceVlanIdFilter.setStatus("current")
_Lgs2816crpsAceTagPriority_Type = DisplayString
_Lgs2816crpsAceTagPriority_Object = MibScalar
lgs2816crpsAceTagPriority = _Lgs2816crpsAceTagPriority_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 4, 10, 2),
    _Lgs2816crpsAceTagPriority_Type()
)
lgs2816crpsAceTagPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsAceTagPriority.setStatus("current")


class _Lgs2816crpsAceInfoEntryAction_Type(Integer32):
    """Custom type lgs2816crpsAceInfoEntryAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Lgs2816crpsAceInfoEntryAction_Type.__name__ = "Integer32"
_Lgs2816crpsAceInfoEntryAction_Object = MibScalar
lgs2816crpsAceInfoEntryAction = _Lgs2816crpsAceInfoEntryAction_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 18, 4, 11),
    _Lgs2816crpsAceInfoEntryAction_Type()
)
lgs2816crpsAceInfoEntryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsAceInfoEntryAction.setStatus("current")
_Lgs2816crpsIpMacBind_ObjectIdentity = ObjectIdentity
lgs2816crpsIpMacBind = _Lgs2816crpsIpMacBind_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 19)
)
_Lgs2816crpsIpMacBindConf_ObjectIdentity = ObjectIdentity
lgs2816crpsIpMacBindConf = _Lgs2816crpsIpMacBindConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 19, 1)
)


class _Lgs2816crpsIpMacBindstate_Type(Integer32):
    """Custom type lgs2816crpsIpMacBindstate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2816crpsIpMacBindstate_Type.__name__ = "Integer32"
_Lgs2816crpsIpMacBindstate_Object = MibScalar
lgs2816crpsIpMacBindstate = _Lgs2816crpsIpMacBindstate_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 19, 1, 1),
    _Lgs2816crpsIpMacBindstate_Type()
)
lgs2816crpsIpMacBindstate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsIpMacBindstate.setStatus("current")
_Lgs2816crpsIpMacBindTrustPort_Type = DisplayString
_Lgs2816crpsIpMacBindTrustPort_Object = MibScalar
lgs2816crpsIpMacBindTrustPort = _Lgs2816crpsIpMacBindTrustPort_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 19, 1, 2),
    _Lgs2816crpsIpMacBindTrustPort_Type()
)
lgs2816crpsIpMacBindTrustPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsIpMacBindTrustPort.setStatus("current")
_Lgs2816crpsIpMacBindSetting_ObjectIdentity = ObjectIdentity
lgs2816crpsIpMacBindSetting = _Lgs2816crpsIpMacBindSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 19, 2)
)


class _Lgs2816crpsIpMacBindSettingNumber_Type(Integer32):
    """Custom type lgs2816crpsIpMacBindSettingNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_Lgs2816crpsIpMacBindSettingNumber_Type.__name__ = "Integer32"
_Lgs2816crpsIpMacBindSettingNumber_Object = MibScalar
lgs2816crpsIpMacBindSettingNumber = _Lgs2816crpsIpMacBindSettingNumber_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 19, 2, 1),
    _Lgs2816crpsIpMacBindSettingNumber_Type()
)
lgs2816crpsIpMacBindSettingNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsIpMacBindSettingNumber.setStatus("current")


class _Lgs2816crpsIpMacBindSettingEntryCreate_Type(Integer32):
    """Custom type lgs2816crpsIpMacBindSettingEntryCreate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2816crpsIpMacBindSettingEntryCreate_Type.__name__ = "Integer32"
_Lgs2816crpsIpMacBindSettingEntryCreate_Object = MibScalar
lgs2816crpsIpMacBindSettingEntryCreate = _Lgs2816crpsIpMacBindSettingEntryCreate_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 19, 2, 2),
    _Lgs2816crpsIpMacBindSettingEntryCreate_Type()
)
lgs2816crpsIpMacBindSettingEntryCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsIpMacBindSettingEntryCreate.setStatus("current")
_Lgs2816crpsIpMacBindSettingTable_Object = MibTable
lgs2816crpsIpMacBindSettingTable = _Lgs2816crpsIpMacBindSettingTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 19, 2, 3)
)
if mibBuilder.loadTexts:
    lgs2816crpsIpMacBindSettingTable.setStatus("current")
_Lgs2816crpsIpMacBindSettingEntry_Object = MibTableRow
lgs2816crpsIpMacBindSettingEntry = _Lgs2816crpsIpMacBindSettingEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 19, 2, 3, 1)
)
lgs2816crpsIpMacBindSettingEntry.setIndexNames(
    (0, "PRIVATE-LGS2816CRPS-MIB", "lgs2816crpsIpMacBindSettingIndex"),
)
if mibBuilder.loadTexts:
    lgs2816crpsIpMacBindSettingEntry.setStatus("current")


class _Lgs2816crpsIpMacBindSettingIndex_Type(Integer32):
    """Custom type lgs2816crpsIpMacBindSettingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_Lgs2816crpsIpMacBindSettingIndex_Type.__name__ = "Integer32"
_Lgs2816crpsIpMacBindSettingIndex_Object = MibTableColumn
lgs2816crpsIpMacBindSettingIndex = _Lgs2816crpsIpMacBindSettingIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 19, 2, 3, 1, 1),
    _Lgs2816crpsIpMacBindSettingIndex_Type()
)
lgs2816crpsIpMacBindSettingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgs2816crpsIpMacBindSettingIndex.setStatus("current")
_Lgs2816crpsIpMacBindSettingMAC_Type = DisplayString
_Lgs2816crpsIpMacBindSettingMAC_Object = MibTableColumn
lgs2816crpsIpMacBindSettingMAC = _Lgs2816crpsIpMacBindSettingMAC_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 19, 2, 3, 1, 2),
    _Lgs2816crpsIpMacBindSettingMAC_Type()
)
lgs2816crpsIpMacBindSettingMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsIpMacBindSettingMAC.setStatus("current")
_Lgs2816crpsIpMacBindSettingIP_Type = IpAddress
_Lgs2816crpsIpMacBindSettingIP_Object = MibTableColumn
lgs2816crpsIpMacBindSettingIP = _Lgs2816crpsIpMacBindSettingIP_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 19, 2, 3, 1, 3),
    _Lgs2816crpsIpMacBindSettingIP_Type()
)
lgs2816crpsIpMacBindSettingIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsIpMacBindSettingIP.setStatus("current")


class _Lgs2816crpsIpMacBindSettingPort_Type(Integer32):
    """Custom type lgs2816crpsIpMacBindSettingPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Lgs2816crpsIpMacBindSettingPort_Type.__name__ = "Integer32"
_Lgs2816crpsIpMacBindSettingPort_Object = MibTableColumn
lgs2816crpsIpMacBindSettingPort = _Lgs2816crpsIpMacBindSettingPort_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 19, 2, 3, 1, 4),
    _Lgs2816crpsIpMacBindSettingPort_Type()
)
lgs2816crpsIpMacBindSettingPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsIpMacBindSettingPort.setStatus("current")


class _Lgs2816crpsIpMacBindSettingVID_Type(Integer32):
    """Custom type lgs2816crpsIpMacBindSettingVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Lgs2816crpsIpMacBindSettingVID_Type.__name__ = "Integer32"
_Lgs2816crpsIpMacBindSettingVID_Object = MibTableColumn
lgs2816crpsIpMacBindSettingVID = _Lgs2816crpsIpMacBindSettingVID_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 19, 2, 3, 1, 5),
    _Lgs2816crpsIpMacBindSettingVID_Type()
)
lgs2816crpsIpMacBindSettingVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsIpMacBindSettingVID.setStatus("current")


class _Lgs2816crpsIpMacBindSettingEntryAction_Type(Integer32):
    """Custom type lgs2816crpsIpMacBindSettingEntryAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Lgs2816crpsIpMacBindSettingEntryAction_Type.__name__ = "Integer32"
_Lgs2816crpsIpMacBindSettingEntryAction_Object = MibTableColumn
lgs2816crpsIpMacBindSettingEntryAction = _Lgs2816crpsIpMacBindSettingEntryAction_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 19, 2, 3, 1, 6),
    _Lgs2816crpsIpMacBindSettingEntryAction_Type()
)
lgs2816crpsIpMacBindSettingEntryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsIpMacBindSettingEntryAction.setStatus("current")
_Lgs2816crpsTrapEntry_ObjectIdentity = ObjectIdentity
lgs2816crpsTrapEntry = _Lgs2816crpsTrapEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 20)
)
_Lgs2816crpsTrapVariable_ObjectIdentity = ObjectIdentity
lgs2816crpsTrapVariable = _Lgs2816crpsTrapVariable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 21)
)
_Username_Type = DisplayString
_Username_Object = MibScalar
username = _Username_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 21, 1),
    _Username_Type()
)
username.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    username.setStatus("current")


class _GroupId_Type(Integer32):
    """Custom type groupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_GroupId_Type.__name__ = "Integer32"
_GroupId_Object = MibScalar
groupId = _GroupId_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 21, 2),
    _GroupId_Type()
)
groupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupId.setStatus("current")


class _Actorkey_Type(Integer32):
    """Custom type actorkey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Actorkey_Type.__name__ = "Integer32"
_Actorkey_Object = MibScalar
actorkey = _Actorkey_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 21, 3),
    _Actorkey_Type()
)
actorkey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actorkey.setStatus("current")


class _Partnerkey_Type(Integer32):
    """Custom type partnerkey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Partnerkey_Type.__name__ = "Integer32"
_Partnerkey_Object = MibScalar
partnerkey = _Partnerkey_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 21, 4),
    _Partnerkey_Type()
)
partnerkey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partnerkey.setStatus("current")
_Swapto_Type = DisplayString
_Swapto_Object = MibScalar
swapto = _Swapto_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 21, 6),
    _Swapto_Type()
)
swapto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swapto.setStatus("current")
_IpmacIp_Type = DisplayString
_IpmacIp_Object = MibScalar
ipmacIp = _IpmacIp_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 21, 7),
    _IpmacIp_Type()
)
ipmacIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmacIp.setStatus("current")
_IpmacMac_Type = DisplayString
_IpmacMac_Object = MibScalar
ipmacMac = _IpmacMac_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 21, 8),
    _IpmacMac_Type()
)
ipmacMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmacMac.setStatus("current")
_Rp2000eventstatus_Type = DisplayString
_Rp2000eventstatus_Object = MibScalar
rp2000eventstatus = _Rp2000eventstatus_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 21, 10),
    _Rp2000eventstatus_Type()
)
rp2000eventstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rp2000eventstatus.setStatus("current")
_Rp2000eventinfo_Type = DisplayString
_Rp2000eventinfo_Object = MibScalar
rp2000eventinfo = _Rp2000eventinfo_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 21, 11),
    _Rp2000eventinfo_Type()
)
rp2000eventinfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rp2000eventinfo.setStatus("current")
_Lgs2816crpsDot1X_ObjectIdentity = ObjectIdentity
lgs2816crpsDot1X = _Lgs2816crpsDot1X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 23)
)
_Lgs2816crpsDot1XServerConf_ObjectIdentity = ObjectIdentity
lgs2816crpsDot1XServerConf = _Lgs2816crpsDot1XServerConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 23, 1)
)
_Lgs2816crpsDot1XServerConfAuthenticationServerIp_Type = DisplayString
_Lgs2816crpsDot1XServerConfAuthenticationServerIp_Object = MibScalar
lgs2816crpsDot1XServerConfAuthenticationServerIp = _Lgs2816crpsDot1XServerConfAuthenticationServerIp_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 23, 1, 1),
    _Lgs2816crpsDot1XServerConfAuthenticationServerIp_Type()
)
lgs2816crpsDot1XServerConfAuthenticationServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsDot1XServerConfAuthenticationServerIp.setStatus("current")


class _Lgs2816crpsDot1XServerConfAuthenticationUdpPort_Type(Integer32):
    """Custom type lgs2816crpsDot1XServerConfAuthenticationUdpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Lgs2816crpsDot1XServerConfAuthenticationUdpPort_Type.__name__ = "Integer32"
_Lgs2816crpsDot1XServerConfAuthenticationUdpPort_Object = MibScalar
lgs2816crpsDot1XServerConfAuthenticationUdpPort = _Lgs2816crpsDot1XServerConfAuthenticationUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 23, 1, 2),
    _Lgs2816crpsDot1XServerConfAuthenticationUdpPort_Type()
)
lgs2816crpsDot1XServerConfAuthenticationUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsDot1XServerConfAuthenticationUdpPort.setStatus("current")
_Lgs2816crpsDot1XServerConfAuthenticationServerIp2_Type = DisplayString
_Lgs2816crpsDot1XServerConfAuthenticationServerIp2_Object = MibScalar
lgs2816crpsDot1XServerConfAuthenticationServerIp2 = _Lgs2816crpsDot1XServerConfAuthenticationServerIp2_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 23, 1, 3),
    _Lgs2816crpsDot1XServerConfAuthenticationServerIp2_Type()
)
lgs2816crpsDot1XServerConfAuthenticationServerIp2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsDot1XServerConfAuthenticationServerIp2.setStatus("current")


class _Lgs2816crpsDot1XServerConfAuthenticationUdpPort2_Type(Integer32):
    """Custom type lgs2816crpsDot1XServerConfAuthenticationUdpPort2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Lgs2816crpsDot1XServerConfAuthenticationUdpPort2_Type.__name__ = "Integer32"
_Lgs2816crpsDot1XServerConfAuthenticationUdpPort2_Object = MibScalar
lgs2816crpsDot1XServerConfAuthenticationUdpPort2 = _Lgs2816crpsDot1XServerConfAuthenticationUdpPort2_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 23, 1, 4),
    _Lgs2816crpsDot1XServerConfAuthenticationUdpPort2_Type()
)
lgs2816crpsDot1XServerConfAuthenticationUdpPort2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsDot1XServerConfAuthenticationUdpPort2.setStatus("current")
_Lgs2816crpsDot1XServerConfAuthenticationSecretKey_Type = DisplayString
_Lgs2816crpsDot1XServerConfAuthenticationSecretKey_Object = MibScalar
lgs2816crpsDot1XServerConfAuthenticationSecretKey = _Lgs2816crpsDot1XServerConfAuthenticationSecretKey_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 23, 1, 5),
    _Lgs2816crpsDot1XServerConfAuthenticationSecretKey_Type()
)
lgs2816crpsDot1XServerConfAuthenticationSecretKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsDot1XServerConfAuthenticationSecretKey.setStatus("current")
_Lgs2816crpsDot1XServerConfAccountingServerIp_Type = DisplayString
_Lgs2816crpsDot1XServerConfAccountingServerIp_Object = MibScalar
lgs2816crpsDot1XServerConfAccountingServerIp = _Lgs2816crpsDot1XServerConfAccountingServerIp_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 23, 1, 6),
    _Lgs2816crpsDot1XServerConfAccountingServerIp_Type()
)
lgs2816crpsDot1XServerConfAccountingServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsDot1XServerConfAccountingServerIp.setStatus("current")


class _Lgs2816crpsDot1XServerConfAccountingUdpPort_Type(Integer32):
    """Custom type lgs2816crpsDot1XServerConfAccountingUdpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Lgs2816crpsDot1XServerConfAccountingUdpPort_Type.__name__ = "Integer32"
_Lgs2816crpsDot1XServerConfAccountingUdpPort_Object = MibScalar
lgs2816crpsDot1XServerConfAccountingUdpPort = _Lgs2816crpsDot1XServerConfAccountingUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 23, 1, 7),
    _Lgs2816crpsDot1XServerConfAccountingUdpPort_Type()
)
lgs2816crpsDot1XServerConfAccountingUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsDot1XServerConfAccountingUdpPort.setStatus("current")
_Lgs2816crpsDot1XServerConfAccountingServerIp2_Type = DisplayString
_Lgs2816crpsDot1XServerConfAccountingServerIp2_Object = MibScalar
lgs2816crpsDot1XServerConfAccountingServerIp2 = _Lgs2816crpsDot1XServerConfAccountingServerIp2_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 23, 1, 8),
    _Lgs2816crpsDot1XServerConfAccountingServerIp2_Type()
)
lgs2816crpsDot1XServerConfAccountingServerIp2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsDot1XServerConfAccountingServerIp2.setStatus("current")


class _Lgs2816crpsDot1XServerConfAccountingUdpPort2_Type(Integer32):
    """Custom type lgs2816crpsDot1XServerConfAccountingUdpPort2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Lgs2816crpsDot1XServerConfAccountingUdpPort2_Type.__name__ = "Integer32"
_Lgs2816crpsDot1XServerConfAccountingUdpPort2_Object = MibScalar
lgs2816crpsDot1XServerConfAccountingUdpPort2 = _Lgs2816crpsDot1XServerConfAccountingUdpPort2_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 23, 1, 9),
    _Lgs2816crpsDot1XServerConfAccountingUdpPort2_Type()
)
lgs2816crpsDot1XServerConfAccountingUdpPort2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsDot1XServerConfAccountingUdpPort2.setStatus("current")
_Lgs2816crpsDot1XServerConfAccountingSecretKey_Type = DisplayString
_Lgs2816crpsDot1XServerConfAccountingSecretKey_Object = MibScalar
lgs2816crpsDot1XServerConfAccountingSecretKey = _Lgs2816crpsDot1XServerConfAccountingSecretKey_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 23, 1, 10),
    _Lgs2816crpsDot1XServerConfAccountingSecretKey_Type()
)
lgs2816crpsDot1XServerConfAccountingSecretKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsDot1XServerConfAccountingSecretKey.setStatus("current")
_Lgs2816crpsDot1XPortConfTable_Object = MibTable
lgs2816crpsDot1XPortConfTable = _Lgs2816crpsDot1XPortConfTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 23, 2)
)
if mibBuilder.loadTexts:
    lgs2816crpsDot1XPortConfTable.setStatus("current")
_Lgs2816crpsDot1XPortConfEntry_Object = MibTableRow
lgs2816crpsDot1XPortConfEntry = _Lgs2816crpsDot1XPortConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 23, 2, 1)
)
lgs2816crpsDot1XPortConfEntry.setIndexNames(
    (0, "PRIVATE-LGS2816CRPS-MIB", "lgs2816crpsDot1XPort"),
)
if mibBuilder.loadTexts:
    lgs2816crpsDot1XPortConfEntry.setStatus("current")


class _Lgs2816crpsDot1XPort_Type(Integer32):
    """Custom type lgs2816crpsDot1XPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Lgs2816crpsDot1XPort_Type.__name__ = "Integer32"
_Lgs2816crpsDot1XPort_Object = MibTableColumn
lgs2816crpsDot1XPort = _Lgs2816crpsDot1XPort_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 23, 2, 1, 1),
    _Lgs2816crpsDot1XPort_Type()
)
lgs2816crpsDot1XPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsDot1XPort.setStatus("current")


class _Lgs2816crpsDot1XPortMode_Type(Integer32):
    """Custom type lgs2816crpsDot1XPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_Lgs2816crpsDot1XPortMode_Type.__name__ = "Integer32"
_Lgs2816crpsDot1XPortMode_Object = MibTableColumn
lgs2816crpsDot1XPortMode = _Lgs2816crpsDot1XPortMode_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 23, 2, 1, 2),
    _Lgs2816crpsDot1XPortMode_Type()
)
lgs2816crpsDot1XPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsDot1XPortMode.setStatus("current")


class _Lgs2816crpsDot1XPortControl_Type(Integer32):
    """Custom type lgs2816crpsDot1XPortControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Lgs2816crpsDot1XPortControl_Type.__name__ = "Integer32"
_Lgs2816crpsDot1XPortControl_Object = MibTableColumn
lgs2816crpsDot1XPortControl = _Lgs2816crpsDot1XPortControl_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 23, 2, 1, 3),
    _Lgs2816crpsDot1XPortControl_Type()
)
lgs2816crpsDot1XPortControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsDot1XPortControl.setStatus("current")


class _Lgs2816crpsDot1XPortreAuthMax_Type(Integer32):
    """Custom type lgs2816crpsDot1XPortreAuthMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Lgs2816crpsDot1XPortreAuthMax_Type.__name__ = "Integer32"
_Lgs2816crpsDot1XPortreAuthMax_Object = MibTableColumn
lgs2816crpsDot1XPortreAuthMax = _Lgs2816crpsDot1XPortreAuthMax_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 23, 2, 1, 4),
    _Lgs2816crpsDot1XPortreAuthMax_Type()
)
lgs2816crpsDot1XPortreAuthMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsDot1XPortreAuthMax.setStatus("current")


class _Lgs2816crpsDot1XPorttxPeriod_Type(Integer32):
    """Custom type lgs2816crpsDot1XPorttxPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Lgs2816crpsDot1XPorttxPeriod_Type.__name__ = "Integer32"
_Lgs2816crpsDot1XPorttxPeriod_Object = MibTableColumn
lgs2816crpsDot1XPorttxPeriod = _Lgs2816crpsDot1XPorttxPeriod_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 23, 2, 1, 5),
    _Lgs2816crpsDot1XPorttxPeriod_Type()
)
lgs2816crpsDot1XPorttxPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsDot1XPorttxPeriod.setStatus("current")


class _Lgs2816crpsDot1XPortquietPeriod_Type(Integer32):
    """Custom type lgs2816crpsDot1XPortquietPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Lgs2816crpsDot1XPortquietPeriod_Type.__name__ = "Integer32"
_Lgs2816crpsDot1XPortquietPeriod_Object = MibTableColumn
lgs2816crpsDot1XPortquietPeriod = _Lgs2816crpsDot1XPortquietPeriod_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 23, 2, 1, 6),
    _Lgs2816crpsDot1XPortquietPeriod_Type()
)
lgs2816crpsDot1XPortquietPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsDot1XPortquietPeriod.setStatus("current")


class _Lgs2816crpsDot1XPortreAuthEnabled_Type(Integer32):
    """Custom type lgs2816crpsDot1XPortreAuthEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2816crpsDot1XPortreAuthEnabled_Type.__name__ = "Integer32"
_Lgs2816crpsDot1XPortreAuthEnabled_Object = MibTableColumn
lgs2816crpsDot1XPortreAuthEnabled = _Lgs2816crpsDot1XPortreAuthEnabled_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 23, 2, 1, 7),
    _Lgs2816crpsDot1XPortreAuthEnabled_Type()
)
lgs2816crpsDot1XPortreAuthEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsDot1XPortreAuthEnabled.setStatus("current")


class _Lgs2816crpsDot1XPortreAuthPeriod_Type(Integer32):
    """Custom type lgs2816crpsDot1XPortreAuthPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Lgs2816crpsDot1XPortreAuthPeriod_Type.__name__ = "Integer32"
_Lgs2816crpsDot1XPortreAuthPeriod_Object = MibTableColumn
lgs2816crpsDot1XPortreAuthPeriod = _Lgs2816crpsDot1XPortreAuthPeriod_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 23, 2, 1, 8),
    _Lgs2816crpsDot1XPortreAuthPeriod_Type()
)
lgs2816crpsDot1XPortreAuthPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsDot1XPortreAuthPeriod.setStatus("current")


class _Lgs2816crpsDot1XPortmaxReq_Type(Integer32):
    """Custom type lgs2816crpsDot1XPortmaxReq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Lgs2816crpsDot1XPortmaxReq_Type.__name__ = "Integer32"
_Lgs2816crpsDot1XPortmaxReq_Object = MibTableColumn
lgs2816crpsDot1XPortmaxReq = _Lgs2816crpsDot1XPortmaxReq_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 23, 2, 1, 9),
    _Lgs2816crpsDot1XPortmaxReq_Type()
)
lgs2816crpsDot1XPortmaxReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsDot1XPortmaxReq.setStatus("current")


class _Lgs2816crpsDot1XPortsuppTimeout_Type(Integer32):
    """Custom type lgs2816crpsDot1XPortsuppTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Lgs2816crpsDot1XPortsuppTimeout_Type.__name__ = "Integer32"
_Lgs2816crpsDot1XPortsuppTimeout_Object = MibTableColumn
lgs2816crpsDot1XPortsuppTimeout = _Lgs2816crpsDot1XPortsuppTimeout_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 23, 2, 1, 10),
    _Lgs2816crpsDot1XPortsuppTimeout_Type()
)
lgs2816crpsDot1XPortsuppTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsDot1XPortsuppTimeout.setStatus("current")


class _Lgs2816crpsDot1XPortserverTimeout_Type(Integer32):
    """Custom type lgs2816crpsDot1XPortserverTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Lgs2816crpsDot1XPortserverTimeout_Type.__name__ = "Integer32"
_Lgs2816crpsDot1XPortserverTimeout_Object = MibTableColumn
lgs2816crpsDot1XPortserverTimeout = _Lgs2816crpsDot1XPortserverTimeout_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 23, 2, 1, 11),
    _Lgs2816crpsDot1XPortserverTimeout_Type()
)
lgs2816crpsDot1XPortserverTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsDot1XPortserverTimeout.setStatus("current")


class _Lgs2816crpsDot1XPortVlanAssignment_Type(Integer32):
    """Custom type lgs2816crpsDot1XPortVlanAssignment based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Lgs2816crpsDot1XPortVlanAssignment_Type.__name__ = "Integer32"
_Lgs2816crpsDot1XPortVlanAssignment_Object = MibTableColumn
lgs2816crpsDot1XPortVlanAssignment = _Lgs2816crpsDot1XPortVlanAssignment_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 23, 2, 1, 12),
    _Lgs2816crpsDot1XPortVlanAssignment_Type()
)
lgs2816crpsDot1XPortVlanAssignment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsDot1XPortVlanAssignment.setStatus("current")


class _Lgs2816crpsDot1XPortGuestVlan_Type(Integer32):
    """Custom type lgs2816crpsDot1XPortGuestVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Lgs2816crpsDot1XPortGuestVlan_Type.__name__ = "Integer32"
_Lgs2816crpsDot1XPortGuestVlan_Object = MibTableColumn
lgs2816crpsDot1XPortGuestVlan = _Lgs2816crpsDot1XPortGuestVlan_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 23, 2, 1, 13),
    _Lgs2816crpsDot1XPortGuestVlan_Type()
)
lgs2816crpsDot1XPortGuestVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsDot1XPortGuestVlan.setStatus("current")


class _Lgs2816crpsDot1XPortAuthFailedVlan_Type(Integer32):
    """Custom type lgs2816crpsDot1XPortAuthFailedVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Lgs2816crpsDot1XPortAuthFailedVlan_Type.__name__ = "Integer32"
_Lgs2816crpsDot1XPortAuthFailedVlan_Object = MibTableColumn
lgs2816crpsDot1XPortAuthFailedVlan = _Lgs2816crpsDot1XPortAuthFailedVlan_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 23, 2, 1, 14),
    _Lgs2816crpsDot1XPortAuthFailedVlan_Type()
)
lgs2816crpsDot1XPortAuthFailedVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsDot1XPortAuthFailedVlan.setStatus("current")
_Lgs2816crpsDot1XStatusTable_Object = MibTable
lgs2816crpsDot1XStatusTable = _Lgs2816crpsDot1XStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 23, 3)
)
if mibBuilder.loadTexts:
    lgs2816crpsDot1XStatusTable.setStatus("current")
_Lgs2816crpsDot1XStatusEntry_Object = MibTableRow
lgs2816crpsDot1XStatusEntry = _Lgs2816crpsDot1XStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 23, 3, 1)
)
lgs2816crpsDot1XStatusEntry.setIndexNames(
    (0, "PRIVATE-LGS2816CRPS-MIB", "lgs2816crpsDot1XStatusIndex"),
)
if mibBuilder.loadTexts:
    lgs2816crpsDot1XStatusEntry.setStatus("current")


class _Lgs2816crpsDot1XStatusIndex_Type(Integer32):
    """Custom type lgs2816crpsDot1XStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Lgs2816crpsDot1XStatusIndex_Type.__name__ = "Integer32"
_Lgs2816crpsDot1XStatusIndex_Object = MibTableColumn
lgs2816crpsDot1XStatusIndex = _Lgs2816crpsDot1XStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 23, 3, 1, 1),
    _Lgs2816crpsDot1XStatusIndex_Type()
)
lgs2816crpsDot1XStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgs2816crpsDot1XStatusIndex.setStatus("current")
_Lgs2816crpsDot1XStatusMode_Type = DisplayString
_Lgs2816crpsDot1XStatusMode_Object = MibTableColumn
lgs2816crpsDot1XStatusMode = _Lgs2816crpsDot1XStatusMode_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 23, 3, 1, 2),
    _Lgs2816crpsDot1XStatusMode_Type()
)
lgs2816crpsDot1XStatusMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsDot1XStatusMode.setStatus("current")
_Lgs2816crpsDot1XStatusStatus_Type = DisplayString
_Lgs2816crpsDot1XStatusStatus_Object = MibTableColumn
lgs2816crpsDot1XStatusStatus = _Lgs2816crpsDot1XStatusStatus_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 23, 3, 1, 3),
    _Lgs2816crpsDot1XStatusStatus_Type()
)
lgs2816crpsDot1XStatusStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsDot1XStatusStatus.setStatus("current")
_Lgs2816crpsDot1XVlanPolicy_Type = DisplayString
_Lgs2816crpsDot1XVlanPolicy_Object = MibTableColumn
lgs2816crpsDot1XVlanPolicy = _Lgs2816crpsDot1XVlanPolicy_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 23, 3, 1, 4),
    _Lgs2816crpsDot1XVlanPolicy_Type()
)
lgs2816crpsDot1XVlanPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsDot1XVlanPolicy.setStatus("current")
_Lgs2816crpsDot1XStatisticsTable_Object = MibTable
lgs2816crpsDot1XStatisticsTable = _Lgs2816crpsDot1XStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 23, 4)
)
if mibBuilder.loadTexts:
    lgs2816crpsDot1XStatisticsTable.setStatus("current")
_Lgs2816crpsDot1XStatisticsEntry_Object = MibTableRow
lgs2816crpsDot1XStatisticsEntry = _Lgs2816crpsDot1XStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 23, 4, 1)
)
lgs2816crpsDot1XStatisticsEntry.setIndexNames(
    (0, "PRIVATE-LGS2816CRPS-MIB", "lgs2816crpsDot1XStatisticsIndex"),
)
if mibBuilder.loadTexts:
    lgs2816crpsDot1XStatisticsEntry.setStatus("current")


class _Lgs2816crpsDot1XStatisticsIndex_Type(Integer32):
    """Custom type lgs2816crpsDot1XStatisticsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Lgs2816crpsDot1XStatisticsIndex_Type.__name__ = "Integer32"
_Lgs2816crpsDot1XStatisticsIndex_Object = MibTableColumn
lgs2816crpsDot1XStatisticsIndex = _Lgs2816crpsDot1XStatisticsIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 23, 4, 1, 1),
    _Lgs2816crpsDot1XStatisticsIndex_Type()
)
lgs2816crpsDot1XStatisticsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgs2816crpsDot1XStatisticsIndex.setStatus("current")


class _Lgs2816crpsDot1XClearCounter_Type(Integer32):
    """Custom type lgs2816crpsDot1XClearCounter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2816crpsDot1XClearCounter_Type.__name__ = "Integer32"
_Lgs2816crpsDot1XClearCounter_Object = MibTableColumn
lgs2816crpsDot1XClearCounter = _Lgs2816crpsDot1XClearCounter_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 23, 4, 1, 2),
    _Lgs2816crpsDot1XClearCounter_Type()
)
lgs2816crpsDot1XClearCounter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsDot1XClearCounter.setStatus("current")
_Lgs2816crpsDot1XAuthEntersConnecting_Type = Counter32
_Lgs2816crpsDot1XAuthEntersConnecting_Object = MibTableColumn
lgs2816crpsDot1XAuthEntersConnecting = _Lgs2816crpsDot1XAuthEntersConnecting_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 23, 4, 1, 3),
    _Lgs2816crpsDot1XAuthEntersConnecting_Type()
)
lgs2816crpsDot1XAuthEntersConnecting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsDot1XAuthEntersConnecting.setStatus("current")
_Lgs2816crpsDot1XauthEapLogoffsWhileConnecting_Type = Counter32
_Lgs2816crpsDot1XauthEapLogoffsWhileConnecting_Object = MibTableColumn
lgs2816crpsDot1XauthEapLogoffsWhileConnecting = _Lgs2816crpsDot1XauthEapLogoffsWhileConnecting_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 23, 4, 1, 4),
    _Lgs2816crpsDot1XauthEapLogoffsWhileConnecting_Type()
)
lgs2816crpsDot1XauthEapLogoffsWhileConnecting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsDot1XauthEapLogoffsWhileConnecting.setStatus("current")
_Lgs2816crpsDot1XAuthEntersAuthenticating_Type = Counter32
_Lgs2816crpsDot1XAuthEntersAuthenticating_Object = MibTableColumn
lgs2816crpsDot1XAuthEntersAuthenticating = _Lgs2816crpsDot1XAuthEntersAuthenticating_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 23, 4, 1, 5),
    _Lgs2816crpsDot1XAuthEntersAuthenticating_Type()
)
lgs2816crpsDot1XAuthEntersAuthenticating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsDot1XAuthEntersAuthenticating.setStatus("current")
_Lgs2816crpsDot1XAuthAuthSuccessesWhileAuthenticating_Type = Counter32
_Lgs2816crpsDot1XAuthAuthSuccessesWhileAuthenticating_Object = MibTableColumn
lgs2816crpsDot1XAuthAuthSuccessesWhileAuthenticating = _Lgs2816crpsDot1XAuthAuthSuccessesWhileAuthenticating_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 23, 4, 1, 6),
    _Lgs2816crpsDot1XAuthAuthSuccessesWhileAuthenticating_Type()
)
lgs2816crpsDot1XAuthAuthSuccessesWhileAuthenticating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsDot1XAuthAuthSuccessesWhileAuthenticating.setStatus("current")
_Lgs2816crpsDot1XAuthAuthTimeoutsWhileAuthenticating_Type = Counter32
_Lgs2816crpsDot1XAuthAuthTimeoutsWhileAuthenticating_Object = MibTableColumn
lgs2816crpsDot1XAuthAuthTimeoutsWhileAuthenticating = _Lgs2816crpsDot1XAuthAuthTimeoutsWhileAuthenticating_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 23, 4, 1, 7),
    _Lgs2816crpsDot1XAuthAuthTimeoutsWhileAuthenticating_Type()
)
lgs2816crpsDot1XAuthAuthTimeoutsWhileAuthenticating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsDot1XAuthAuthTimeoutsWhileAuthenticating.setStatus("current")
_Lgs2816crpsDot1XAuthAuthFailWhileAuthenticating_Type = Counter32
_Lgs2816crpsDot1XAuthAuthFailWhileAuthenticating_Object = MibTableColumn
lgs2816crpsDot1XAuthAuthFailWhileAuthenticating = _Lgs2816crpsDot1XAuthAuthFailWhileAuthenticating_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 23, 4, 1, 8),
    _Lgs2816crpsDot1XAuthAuthFailWhileAuthenticating_Type()
)
lgs2816crpsDot1XAuthAuthFailWhileAuthenticating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsDot1XAuthAuthFailWhileAuthenticating.setStatus("current")
_Lgs2816crpsDot1XAuthAuthEapStartsWhileAuthenticating_Type = Counter32
_Lgs2816crpsDot1XAuthAuthEapStartsWhileAuthenticating_Object = MibTableColumn
lgs2816crpsDot1XAuthAuthEapStartsWhileAuthenticating = _Lgs2816crpsDot1XAuthAuthEapStartsWhileAuthenticating_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 23, 4, 1, 9),
    _Lgs2816crpsDot1XAuthAuthEapStartsWhileAuthenticating_Type()
)
lgs2816crpsDot1XAuthAuthEapStartsWhileAuthenticating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsDot1XAuthAuthEapStartsWhileAuthenticating.setStatus("current")
_Lgs2816crpsDot1XAuthAuthEapLogoffWhileAuthenticating_Type = Counter32
_Lgs2816crpsDot1XAuthAuthEapLogoffWhileAuthenticating_Object = MibTableColumn
lgs2816crpsDot1XAuthAuthEapLogoffWhileAuthenticating = _Lgs2816crpsDot1XAuthAuthEapLogoffWhileAuthenticating_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 23, 4, 1, 10),
    _Lgs2816crpsDot1XAuthAuthEapLogoffWhileAuthenticating_Type()
)
lgs2816crpsDot1XAuthAuthEapLogoffWhileAuthenticating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsDot1XAuthAuthEapLogoffWhileAuthenticating.setStatus("current")
_Lgs2816crpsDot1XAuthAuthReauthsWhileAuthenticated_Type = Counter32
_Lgs2816crpsDot1XAuthAuthReauthsWhileAuthenticated_Object = MibTableColumn
lgs2816crpsDot1XAuthAuthReauthsWhileAuthenticated = _Lgs2816crpsDot1XAuthAuthReauthsWhileAuthenticated_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 23, 4, 1, 11),
    _Lgs2816crpsDot1XAuthAuthReauthsWhileAuthenticated_Type()
)
lgs2816crpsDot1XAuthAuthReauthsWhileAuthenticated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsDot1XAuthAuthReauthsWhileAuthenticated.setStatus("current")
_Lgs2816crpsDot1XAuthAuthEapStartsWhileAuthenticated_Type = Counter32
_Lgs2816crpsDot1XAuthAuthEapStartsWhileAuthenticated_Object = MibTableColumn
lgs2816crpsDot1XAuthAuthEapStartsWhileAuthenticated = _Lgs2816crpsDot1XAuthAuthEapStartsWhileAuthenticated_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 23, 4, 1, 12),
    _Lgs2816crpsDot1XAuthAuthEapStartsWhileAuthenticated_Type()
)
lgs2816crpsDot1XAuthAuthEapStartsWhileAuthenticated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsDot1XAuthAuthEapStartsWhileAuthenticated.setStatus("current")
_Lgs2816crpsDot1XAuthAuthEapLogoffWhileAuthenticated_Type = Counter32
_Lgs2816crpsDot1XAuthAuthEapLogoffWhileAuthenticated_Object = MibTableColumn
lgs2816crpsDot1XAuthAuthEapLogoffWhileAuthenticated = _Lgs2816crpsDot1XAuthAuthEapLogoffWhileAuthenticated_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 23, 4, 1, 13),
    _Lgs2816crpsDot1XAuthAuthEapLogoffWhileAuthenticated_Type()
)
lgs2816crpsDot1XAuthAuthEapLogoffWhileAuthenticated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsDot1XAuthAuthEapLogoffWhileAuthenticated.setStatus("current")
_Lgs2816crpsDot1XBackendResponses_Type = Counter32
_Lgs2816crpsDot1XBackendResponses_Object = MibTableColumn
lgs2816crpsDot1XBackendResponses = _Lgs2816crpsDot1XBackendResponses_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 23, 4, 1, 14),
    _Lgs2816crpsDot1XBackendResponses_Type()
)
lgs2816crpsDot1XBackendResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsDot1XBackendResponses.setStatus("current")
_Lgs2816crpsDot1XBackendAccessChallenges_Type = Counter32
_Lgs2816crpsDot1XBackendAccessChallenges_Object = MibTableColumn
lgs2816crpsDot1XBackendAccessChallenges = _Lgs2816crpsDot1XBackendAccessChallenges_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 23, 4, 1, 15),
    _Lgs2816crpsDot1XBackendAccessChallenges_Type()
)
lgs2816crpsDot1XBackendAccessChallenges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsDot1XBackendAccessChallenges.setStatus("current")
_Lgs2816crpsDot1XBackendOtherRequestsToSupplicant_Type = Counter32
_Lgs2816crpsDot1XBackendOtherRequestsToSupplicant_Object = MibTableColumn
lgs2816crpsDot1XBackendOtherRequestsToSupplicant = _Lgs2816crpsDot1XBackendOtherRequestsToSupplicant_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 23, 4, 1, 16),
    _Lgs2816crpsDot1XBackendOtherRequestsToSupplicant_Type()
)
lgs2816crpsDot1XBackendOtherRequestsToSupplicant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsDot1XBackendOtherRequestsToSupplicant.setStatus("current")
_Lgs2816crpsDot1XBackendAuthSuccesses_Type = Counter32
_Lgs2816crpsDot1XBackendAuthSuccesses_Object = MibTableColumn
lgs2816crpsDot1XBackendAuthSuccesses = _Lgs2816crpsDot1XBackendAuthSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 23, 4, 1, 17),
    _Lgs2816crpsDot1XBackendAuthSuccesses_Type()
)
lgs2816crpsDot1XBackendAuthSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsDot1XBackendAuthSuccesses.setStatus("current")
_Lgs2816crpsDot1XBackendAuthFails_Type = Counter32
_Lgs2816crpsDot1XBackendAuthFails_Object = MibTableColumn
lgs2816crpsDot1XBackendAuthFails = _Lgs2816crpsDot1XBackendAuthFails_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 23, 4, 1, 18),
    _Lgs2816crpsDot1XBackendAuthFails_Type()
)
lgs2816crpsDot1XBackendAuthFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsDot1XBackendAuthFails.setStatus("current")
_Lgs2816crpsDot1XAuthEapolFramesRx_Type = Counter32
_Lgs2816crpsDot1XAuthEapolFramesRx_Object = MibTableColumn
lgs2816crpsDot1XAuthEapolFramesRx = _Lgs2816crpsDot1XAuthEapolFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 23, 4, 1, 19),
    _Lgs2816crpsDot1XAuthEapolFramesRx_Type()
)
lgs2816crpsDot1XAuthEapolFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsDot1XAuthEapolFramesRx.setStatus("current")
_Lgs2816crpsDot1XAuthEapolFramesTx_Type = Counter32
_Lgs2816crpsDot1XAuthEapolFramesTx_Object = MibTableColumn
lgs2816crpsDot1XAuthEapolFramesTx = _Lgs2816crpsDot1XAuthEapolFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 23, 4, 1, 20),
    _Lgs2816crpsDot1XAuthEapolFramesTx_Type()
)
lgs2816crpsDot1XAuthEapolFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsDot1XAuthEapolFramesTx.setStatus("current")
_Lgs2816crpsDot1XAuthEapolStartFramesRx_Type = Counter32
_Lgs2816crpsDot1XAuthEapolStartFramesRx_Object = MibTableColumn
lgs2816crpsDot1XAuthEapolStartFramesRx = _Lgs2816crpsDot1XAuthEapolStartFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 23, 4, 1, 21),
    _Lgs2816crpsDot1XAuthEapolStartFramesRx_Type()
)
lgs2816crpsDot1XAuthEapolStartFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsDot1XAuthEapolStartFramesRx.setStatus("current")
_Lgs2816crpsDot1XAuthEapolLogoffFramesRx_Type = Counter32
_Lgs2816crpsDot1XAuthEapolLogoffFramesRx_Object = MibTableColumn
lgs2816crpsDot1XAuthEapolLogoffFramesRx = _Lgs2816crpsDot1XAuthEapolLogoffFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 23, 4, 1, 22),
    _Lgs2816crpsDot1XAuthEapolLogoffFramesRx_Type()
)
lgs2816crpsDot1XAuthEapolLogoffFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsDot1XAuthEapolLogoffFramesRx.setStatus("current")
_Lgs2816crpsDot1XAuthEapolRespIdFramesRx_Type = Counter32
_Lgs2816crpsDot1XAuthEapolRespIdFramesRx_Object = MibTableColumn
lgs2816crpsDot1XAuthEapolRespIdFramesRx = _Lgs2816crpsDot1XAuthEapolRespIdFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 23, 4, 1, 23),
    _Lgs2816crpsDot1XAuthEapolRespIdFramesRx_Type()
)
lgs2816crpsDot1XAuthEapolRespIdFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsDot1XAuthEapolRespIdFramesRx.setStatus("current")
_Lgs2816crpsDot1XAuthEapolRespFramesRx_Type = Counter32
_Lgs2816crpsDot1XAuthEapolRespFramesRx_Object = MibTableColumn
lgs2816crpsDot1XAuthEapolRespFramesRx = _Lgs2816crpsDot1XAuthEapolRespFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 23, 4, 1, 24),
    _Lgs2816crpsDot1XAuthEapolRespFramesRx_Type()
)
lgs2816crpsDot1XAuthEapolRespFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsDot1XAuthEapolRespFramesRx.setStatus("current")
_Lgs2816crpsDot1XAuthEapolReqIdFramesTx_Type = Counter32
_Lgs2816crpsDot1XAuthEapolReqIdFramesTx_Object = MibTableColumn
lgs2816crpsDot1XAuthEapolReqIdFramesTx = _Lgs2816crpsDot1XAuthEapolReqIdFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 23, 4, 1, 25),
    _Lgs2816crpsDot1XAuthEapolReqIdFramesTx_Type()
)
lgs2816crpsDot1XAuthEapolReqIdFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsDot1XAuthEapolReqIdFramesTx.setStatus("current")
_Lgs2816crpsDot1XAuthEapolReqFramesTx_Type = Counter32
_Lgs2816crpsDot1XAuthEapolReqFramesTx_Object = MibTableColumn
lgs2816crpsDot1XAuthEapolReqFramesTx = _Lgs2816crpsDot1XAuthEapolReqFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 23, 4, 1, 26),
    _Lgs2816crpsDot1XAuthEapolReqFramesTx_Type()
)
lgs2816crpsDot1XAuthEapolReqFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsDot1XAuthEapolReqFramesTx.setStatus("current")
_Lgs2816crpsDot1XAuthInvalidEapolFramesRx_Type = Counter32
_Lgs2816crpsDot1XAuthInvalidEapolFramesRx_Object = MibTableColumn
lgs2816crpsDot1XAuthInvalidEapolFramesRx = _Lgs2816crpsDot1XAuthInvalidEapolFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 23, 4, 1, 27),
    _Lgs2816crpsDot1XAuthInvalidEapolFramesRx_Type()
)
lgs2816crpsDot1XAuthInvalidEapolFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsDot1XAuthInvalidEapolFramesRx.setStatus("current")
_Lgs2816crpsDot1XAuthEapLengthErrorFramesRx_Type = Counter32
_Lgs2816crpsDot1XAuthEapLengthErrorFramesRx_Object = MibTableColumn
lgs2816crpsDot1XAuthEapLengthErrorFramesRx = _Lgs2816crpsDot1XAuthEapLengthErrorFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 23, 4, 1, 28),
    _Lgs2816crpsDot1XAuthEapLengthErrorFramesRx_Type()
)
lgs2816crpsDot1XAuthEapLengthErrorFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsDot1XAuthEapLengthErrorFramesRx.setStatus("current")
_Lgs2816crpsDot1XAuthLastEapolFrameVersion_Type = Counter32
_Lgs2816crpsDot1XAuthLastEapolFrameVersion_Object = MibTableColumn
lgs2816crpsDot1XAuthLastEapolFrameVersion = _Lgs2816crpsDot1XAuthLastEapolFrameVersion_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 23, 4, 1, 29),
    _Lgs2816crpsDot1XAuthLastEapolFrameVersion_Type()
)
lgs2816crpsDot1XAuthLastEapolFrameVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsDot1XAuthLastEapolFrameVersion.setStatus("current")
_Lgs2816crpsDot1XAuthLastEapolFrameSource_Type = DisplayString
_Lgs2816crpsDot1XAuthLastEapolFrameSource_Object = MibTableColumn
lgs2816crpsDot1XAuthLastEapolFrameSource = _Lgs2816crpsDot1XAuthLastEapolFrameSource_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 23, 4, 1, 30),
    _Lgs2816crpsDot1XAuthLastEapolFrameSource_Type()
)
lgs2816crpsDot1XAuthLastEapolFrameSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsDot1XAuthLastEapolFrameSource.setStatus("current")
_Lgs2816crpsTrunkInfo_ObjectIdentity = ObjectIdentity
lgs2816crpsTrunkInfo = _Lgs2816crpsTrunkInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 24)
)
_Lgs2816crpsTrunkPort_ObjectIdentity = ObjectIdentity
lgs2816crpsTrunkPort = _Lgs2816crpsTrunkPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 24, 1)
)
_Lgs2816crpsTrunkPortTable_Object = MibTable
lgs2816crpsTrunkPortTable = _Lgs2816crpsTrunkPortTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 24, 1, 1)
)
if mibBuilder.loadTexts:
    lgs2816crpsTrunkPortTable.setStatus("current")
_Lgs2816crpsTrunkPortEntry_Object = MibTableRow
lgs2816crpsTrunkPortEntry = _Lgs2816crpsTrunkPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 24, 1, 1, 1)
)
lgs2816crpsTrunkPortEntry.setIndexNames(
    (0, "PRIVATE-LGS2816CRPS-MIB", "lgs2816crpsTrunkPortIndex"),
)
if mibBuilder.loadTexts:
    lgs2816crpsTrunkPortEntry.setStatus("current")


class _Lgs2816crpsTrunkPortIndex_Type(Integer32):
    """Custom type lgs2816crpsTrunkPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Lgs2816crpsTrunkPortIndex_Type.__name__ = "Integer32"
_Lgs2816crpsTrunkPortIndex_Object = MibTableColumn
lgs2816crpsTrunkPortIndex = _Lgs2816crpsTrunkPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 24, 1, 1, 1, 1),
    _Lgs2816crpsTrunkPortIndex_Type()
)
lgs2816crpsTrunkPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgs2816crpsTrunkPortIndex.setStatus("current")


class _Lgs2816crpsTrunkPortMethod_Type(Integer32):
    """Custom type lgs2816crpsTrunkPortMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Lgs2816crpsTrunkPortMethod_Type.__name__ = "Integer32"
_Lgs2816crpsTrunkPortMethod_Object = MibTableColumn
lgs2816crpsTrunkPortMethod = _Lgs2816crpsTrunkPortMethod_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 24, 1, 1, 1, 2),
    _Lgs2816crpsTrunkPortMethod_Type()
)
lgs2816crpsTrunkPortMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsTrunkPortMethod.setStatus("current")


class _Lgs2816crpsTrunkPortGroup_Type(Integer32):
    """Custom type lgs2816crpsTrunkPortGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_Lgs2816crpsTrunkPortGroup_Type.__name__ = "Integer32"
_Lgs2816crpsTrunkPortGroup_Object = MibTableColumn
lgs2816crpsTrunkPortGroup = _Lgs2816crpsTrunkPortGroup_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 24, 1, 1, 1, 3),
    _Lgs2816crpsTrunkPortGroup_Type()
)
lgs2816crpsTrunkPortGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsTrunkPortGroup.setStatus("current")


class _Lgs2816crpsTrunkPortActiveLacp_Type(Integer32):
    """Custom type lgs2816crpsTrunkPortActiveLacp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2816crpsTrunkPortActiveLacp_Type.__name__ = "Integer32"
_Lgs2816crpsTrunkPortActiveLacp_Object = MibTableColumn
lgs2816crpsTrunkPortActiveLacp = _Lgs2816crpsTrunkPortActiveLacp_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 24, 1, 1, 1, 4),
    _Lgs2816crpsTrunkPortActiveLacp_Type()
)
lgs2816crpsTrunkPortActiveLacp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsTrunkPortActiveLacp.setStatus("current")


class _Lgs2816crpsTrunkPortAggtr_Type(Integer32):
    """Custom type lgs2816crpsTrunkPortAggtr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Lgs2816crpsTrunkPortAggtr_Type.__name__ = "Integer32"
_Lgs2816crpsTrunkPortAggtr_Object = MibTableColumn
lgs2816crpsTrunkPortAggtr = _Lgs2816crpsTrunkPortAggtr_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 24, 1, 1, 1, 5),
    _Lgs2816crpsTrunkPortAggtr_Type()
)
lgs2816crpsTrunkPortAggtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsTrunkPortAggtr.setStatus("current")


class _Lgs2816crpsTrunkPortStatus_Type(Integer32):
    """Custom type lgs2816crpsTrunkPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2816crpsTrunkPortStatus_Type.__name__ = "Integer32"
_Lgs2816crpsTrunkPortStatus_Object = MibTableColumn
lgs2816crpsTrunkPortStatus = _Lgs2816crpsTrunkPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 24, 1, 1, 1, 6),
    _Lgs2816crpsTrunkPortStatus_Type()
)
lgs2816crpsTrunkPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsTrunkPortStatus.setStatus("current")


class _Lgs2816crpsTrunkPortCurrentMode_Type(Integer32):
    """Custom type lgs2816crpsTrunkPortCurrentMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Lgs2816crpsTrunkPortCurrentMode_Type.__name__ = "Integer32"
_Lgs2816crpsTrunkPortCurrentMode_Object = MibTableColumn
lgs2816crpsTrunkPortCurrentMode = _Lgs2816crpsTrunkPortCurrentMode_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 24, 1, 1, 1, 7),
    _Lgs2816crpsTrunkPortCurrentMode_Type()
)
lgs2816crpsTrunkPortCurrentMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsTrunkPortCurrentMode.setStatus("current")
_Lgs2816crpsAggregatorView_ObjectIdentity = ObjectIdentity
lgs2816crpsAggregatorView = _Lgs2816crpsAggregatorView_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 24, 2)
)
_Lgs2816crpsAggregatorViewTable_Object = MibTable
lgs2816crpsAggregatorViewTable = _Lgs2816crpsAggregatorViewTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 24, 2, 1)
)
if mibBuilder.loadTexts:
    lgs2816crpsAggregatorViewTable.setStatus("current")
_Lgs2816crpsAggregatorViewEntry_Object = MibTableRow
lgs2816crpsAggregatorViewEntry = _Lgs2816crpsAggregatorViewEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 24, 2, 1, 1)
)
lgs2816crpsAggregatorViewEntry.setIndexNames(
    (0, "PRIVATE-LGS2816CRPS-MIB", "lgs2816crpsAggregatorViewIndex"),
)
if mibBuilder.loadTexts:
    lgs2816crpsAggregatorViewEntry.setStatus("current")


class _Lgs2816crpsAggregatorViewIndex_Type(Integer32):
    """Custom type lgs2816crpsAggregatorViewIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Lgs2816crpsAggregatorViewIndex_Type.__name__ = "Integer32"
_Lgs2816crpsAggregatorViewIndex_Object = MibTableColumn
lgs2816crpsAggregatorViewIndex = _Lgs2816crpsAggregatorViewIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 24, 2, 1, 1, 1),
    _Lgs2816crpsAggregatorViewIndex_Type()
)
lgs2816crpsAggregatorViewIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgs2816crpsAggregatorViewIndex.setStatus("current")


class _Lgs2816crpsAggregatorViewMethod_Type(Integer32):
    """Custom type lgs2816crpsAggregatorViewMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Lgs2816crpsAggregatorViewMethod_Type.__name__ = "Integer32"
_Lgs2816crpsAggregatorViewMethod_Object = MibTableColumn
lgs2816crpsAggregatorViewMethod = _Lgs2816crpsAggregatorViewMethod_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 24, 2, 1, 1, 2),
    _Lgs2816crpsAggregatorViewMethod_Type()
)
lgs2816crpsAggregatorViewMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsAggregatorViewMethod.setStatus("current")
_Lgs2816crpsAggregatorViewMemberPorts_Type = DisplayString
_Lgs2816crpsAggregatorViewMemberPorts_Object = MibTableColumn
lgs2816crpsAggregatorViewMemberPorts = _Lgs2816crpsAggregatorViewMemberPorts_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 24, 2, 1, 1, 3),
    _Lgs2816crpsAggregatorViewMemberPorts_Type()
)
lgs2816crpsAggregatorViewMemberPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsAggregatorViewMemberPorts.setStatus("current")
_Lgs2816crpsAggregatorViewReadyPorts_Type = DisplayString
_Lgs2816crpsAggregatorViewReadyPorts_Object = MibTableColumn
lgs2816crpsAggregatorViewReadyPorts = _Lgs2816crpsAggregatorViewReadyPorts_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 24, 2, 1, 1, 4),
    _Lgs2816crpsAggregatorViewReadyPorts_Type()
)
lgs2816crpsAggregatorViewReadyPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsAggregatorViewReadyPorts.setStatus("current")


class _Lgs2816crpsLacpSystemPriority_Type(Integer32):
    """Custom type lgs2816crpsLacpSystemPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Lgs2816crpsLacpSystemPriority_Type.__name__ = "Integer32"
_Lgs2816crpsLacpSystemPriority_Object = MibScalar
lgs2816crpsLacpSystemPriority = _Lgs2816crpsLacpSystemPriority_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 24, 3),
    _Lgs2816crpsLacpSystemPriority_Type()
)
lgs2816crpsLacpSystemPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsLacpSystemPriority.setStatus("current")
_Lgs2816crpsAggregationHashMode_ObjectIdentity = ObjectIdentity
lgs2816crpsAggregationHashMode = _Lgs2816crpsAggregationHashMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 24, 4)
)


class _Lgs2816crpsHashCodeSourceMacAddress_Type(Integer32):
    """Custom type lgs2816crpsHashCodeSourceMacAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2816crpsHashCodeSourceMacAddress_Type.__name__ = "Integer32"
_Lgs2816crpsHashCodeSourceMacAddress_Object = MibScalar
lgs2816crpsHashCodeSourceMacAddress = _Lgs2816crpsHashCodeSourceMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 24, 4, 1),
    _Lgs2816crpsHashCodeSourceMacAddress_Type()
)
lgs2816crpsHashCodeSourceMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsHashCodeSourceMacAddress.setStatus("current")


class _Lgs2816crpsHashCodeDestinationMacAddress_Type(Integer32):
    """Custom type lgs2816crpsHashCodeDestinationMacAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2816crpsHashCodeDestinationMacAddress_Type.__name__ = "Integer32"
_Lgs2816crpsHashCodeDestinationMacAddress_Object = MibScalar
lgs2816crpsHashCodeDestinationMacAddress = _Lgs2816crpsHashCodeDestinationMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 24, 4, 2),
    _Lgs2816crpsHashCodeDestinationMacAddress_Type()
)
lgs2816crpsHashCodeDestinationMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsHashCodeDestinationMacAddress.setStatus("current")


class _Lgs2816crpsHashCodeIpAddress_Type(Integer32):
    """Custom type lgs2816crpsHashCodeIpAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2816crpsHashCodeIpAddress_Type.__name__ = "Integer32"
_Lgs2816crpsHashCodeIpAddress_Object = MibScalar
lgs2816crpsHashCodeIpAddress = _Lgs2816crpsHashCodeIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 24, 4, 3),
    _Lgs2816crpsHashCodeIpAddress_Type()
)
lgs2816crpsHashCodeIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsHashCodeIpAddress.setStatus("current")


class _Lgs2816crpsHashCodeTcpUdpPortNumber_Type(Integer32):
    """Custom type lgs2816crpsHashCodeTcpUdpPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2816crpsHashCodeTcpUdpPortNumber_Type.__name__ = "Integer32"
_Lgs2816crpsHashCodeTcpUdpPortNumber_Object = MibScalar
lgs2816crpsHashCodeTcpUdpPortNumber = _Lgs2816crpsHashCodeTcpUdpPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 24, 4, 4),
    _Lgs2816crpsHashCodeTcpUdpPortNumber_Type()
)
lgs2816crpsHashCodeTcpUdpPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsHashCodeTcpUdpPortNumber.setStatus("current")
_Lgs2816crpsMulticastInfo_ObjectIdentity = ObjectIdentity
lgs2816crpsMulticastInfo = _Lgs2816crpsMulticastInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 25)
)


class _Lgs2816crpsIGMPMode_Type(Integer32):
    """Custom type lgs2816crpsIGMPMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_Lgs2816crpsIGMPMode_Type.__name__ = "Integer32"
_Lgs2816crpsIGMPMode_Object = MibScalar
lgs2816crpsIGMPMode = _Lgs2816crpsIGMPMode_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 25, 1),
    _Lgs2816crpsIGMPMode_Type()
)
lgs2816crpsIGMPMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsIGMPMode.setStatus("current")
_Lgs2816crpsIGMPGroupAllowConf_ObjectIdentity = ObjectIdentity
lgs2816crpsIGMPGroupAllowConf = _Lgs2816crpsIGMPGroupAllowConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 25, 2)
)


class _Lgs2816crpsIGMPGroupAllowNumber_Type(Integer32):
    """Custom type lgs2816crpsIGMPGroupAllowNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Lgs2816crpsIGMPGroupAllowNumber_Type.__name__ = "Integer32"
_Lgs2816crpsIGMPGroupAllowNumber_Object = MibScalar
lgs2816crpsIGMPGroupAllowNumber = _Lgs2816crpsIGMPGroupAllowNumber_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 25, 2, 1),
    _Lgs2816crpsIGMPGroupAllowNumber_Type()
)
lgs2816crpsIGMPGroupAllowNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsIGMPGroupAllowNumber.setStatus("current")


class _Lgs2816crpsIGMPGroupAllowEntryCreate_Type(Integer32):
    """Custom type lgs2816crpsIGMPGroupAllowEntryCreate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Lgs2816crpsIGMPGroupAllowEntryCreate_Type.__name__ = "Integer32"
_Lgs2816crpsIGMPGroupAllowEntryCreate_Object = MibScalar
lgs2816crpsIGMPGroupAllowEntryCreate = _Lgs2816crpsIGMPGroupAllowEntryCreate_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 25, 2, 2),
    _Lgs2816crpsIGMPGroupAllowEntryCreate_Type()
)
lgs2816crpsIGMPGroupAllowEntryCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsIGMPGroupAllowEntryCreate.setStatus("current")
_Lgs2816crpsIGMPGroupAllowTable_Object = MibTable
lgs2816crpsIGMPGroupAllowTable = _Lgs2816crpsIGMPGroupAllowTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 25, 2, 3)
)
if mibBuilder.loadTexts:
    lgs2816crpsIGMPGroupAllowTable.setStatus("current")
_Lgs2816crpsIGMPGroupAllowEntry_Object = MibTableRow
lgs2816crpsIGMPGroupAllowEntry = _Lgs2816crpsIGMPGroupAllowEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 25, 2, 3, 1)
)
lgs2816crpsIGMPGroupAllowEntry.setIndexNames(
    (0, "PRIVATE-LGS2816CRPS-MIB", "lgs2816crpsIGMPGroupAllowNo"),
)
if mibBuilder.loadTexts:
    lgs2816crpsIGMPGroupAllowEntry.setStatus("current")


class _Lgs2816crpsIGMPGroupAllowNo_Type(Integer32):
    """Custom type lgs2816crpsIGMPGroupAllowNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Lgs2816crpsIGMPGroupAllowNo_Type.__name__ = "Integer32"
_Lgs2816crpsIGMPGroupAllowNo_Object = MibTableColumn
lgs2816crpsIGMPGroupAllowNo = _Lgs2816crpsIGMPGroupAllowNo_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 25, 2, 3, 1, 1),
    _Lgs2816crpsIGMPGroupAllowNo_Type()
)
lgs2816crpsIGMPGroupAllowNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgs2816crpsIGMPGroupAllowNo.setStatus("current")


class _Lgs2816crpsIGMPGroupAllowVid_Type(Integer32):
    """Custom type lgs2816crpsIGMPGroupAllowVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Lgs2816crpsIGMPGroupAllowVid_Type.__name__ = "Integer32"
_Lgs2816crpsIGMPGroupAllowVid_Object = MibTableColumn
lgs2816crpsIGMPGroupAllowVid = _Lgs2816crpsIGMPGroupAllowVid_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 25, 2, 3, 1, 2),
    _Lgs2816crpsIGMPGroupAllowVid_Type()
)
lgs2816crpsIGMPGroupAllowVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsIGMPGroupAllowVid.setStatus("current")
_Lgs2816crpsIGMPGroupAllowStartAddress_Type = DisplayString
_Lgs2816crpsIGMPGroupAllowStartAddress_Object = MibTableColumn
lgs2816crpsIGMPGroupAllowStartAddress = _Lgs2816crpsIGMPGroupAllowStartAddress_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 25, 2, 3, 1, 3),
    _Lgs2816crpsIGMPGroupAllowStartAddress_Type()
)
lgs2816crpsIGMPGroupAllowStartAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsIGMPGroupAllowStartAddress.setStatus("current")
_Lgs2816crpsIGMPGroupAllowEndAddress_Type = DisplayString
_Lgs2816crpsIGMPGroupAllowEndAddress_Object = MibTableColumn
lgs2816crpsIGMPGroupAllowEndAddress = _Lgs2816crpsIGMPGroupAllowEndAddress_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 25, 2, 3, 1, 4),
    _Lgs2816crpsIGMPGroupAllowEndAddress_Type()
)
lgs2816crpsIGMPGroupAllowEndAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsIGMPGroupAllowEndAddress.setStatus("current")


class _Lgs2816crpsIGMPGroupAllowEntryAction_Type(Integer32):
    """Custom type lgs2816crpsIGMPGroupAllowEntryAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Lgs2816crpsIGMPGroupAllowEntryAction_Type.__name__ = "Integer32"
_Lgs2816crpsIGMPGroupAllowEntryAction_Object = MibTableColumn
lgs2816crpsIGMPGroupAllowEntryAction = _Lgs2816crpsIGMPGroupAllowEntryAction_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 25, 2, 3, 1, 5),
    _Lgs2816crpsIGMPGroupAllowEntryAction_Type()
)
lgs2816crpsIGMPGroupAllowEntryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsIGMPGroupAllowEntryAction.setStatus("current")
_Lgs2816crpsIGMPProxy_ObjectIdentity = ObjectIdentity
lgs2816crpsIGMPProxy = _Lgs2816crpsIGMPProxy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 25, 3)
)


class _Lgs2816crpsIgmpProxyConfGeneralQueryInterval_Type(Integer32):
    """Custom type lgs2816crpsIgmpProxyConfGeneralQueryInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_Lgs2816crpsIgmpProxyConfGeneralQueryInterval_Type.__name__ = "Integer32"
_Lgs2816crpsIgmpProxyConfGeneralQueryInterval_Object = MibScalar
lgs2816crpsIgmpProxyConfGeneralQueryInterval = _Lgs2816crpsIgmpProxyConfGeneralQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 25, 3, 1),
    _Lgs2816crpsIgmpProxyConfGeneralQueryInterval_Type()
)
lgs2816crpsIgmpProxyConfGeneralQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsIgmpProxyConfGeneralQueryInterval.setStatus("current")


class _Lgs2816crpsIgmpProxyConfGeneralQueryRepTimeout_Type(Integer32):
    """Custom type lgs2816crpsIgmpProxyConfGeneralQueryRepTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 25),
    )


_Lgs2816crpsIgmpProxyConfGeneralQueryRepTimeout_Type.__name__ = "Integer32"
_Lgs2816crpsIgmpProxyConfGeneralQueryRepTimeout_Object = MibScalar
lgs2816crpsIgmpProxyConfGeneralQueryRepTimeout = _Lgs2816crpsIgmpProxyConfGeneralQueryRepTimeout_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 25, 3, 2),
    _Lgs2816crpsIgmpProxyConfGeneralQueryRepTimeout_Type()
)
lgs2816crpsIgmpProxyConfGeneralQueryRepTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsIgmpProxyConfGeneralQueryRepTimeout.setStatus("current")


class _Lgs2816crpsIgmpProxyConfGeneralQueryMaxRepTime_Type(Integer32):
    """Custom type lgs2816crpsIgmpProxyConfGeneralQueryMaxRepTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 25),
    )


_Lgs2816crpsIgmpProxyConfGeneralQueryMaxRepTime_Type.__name__ = "Integer32"
_Lgs2816crpsIgmpProxyConfGeneralQueryMaxRepTime_Object = MibScalar
lgs2816crpsIgmpProxyConfGeneralQueryMaxRepTime = _Lgs2816crpsIgmpProxyConfGeneralQueryMaxRepTime_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 25, 3, 3),
    _Lgs2816crpsIgmpProxyConfGeneralQueryMaxRepTime_Type()
)
lgs2816crpsIgmpProxyConfGeneralQueryMaxRepTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsIgmpProxyConfGeneralQueryMaxRepTime.setStatus("current")


class _Lgs2816crpsIgmpProxyConfLastMemberQueryCount_Type(Integer32):
    """Custom type lgs2816crpsIgmpProxyConfLastMemberQueryCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Lgs2816crpsIgmpProxyConfLastMemberQueryCount_Type.__name__ = "Integer32"
_Lgs2816crpsIgmpProxyConfLastMemberQueryCount_Object = MibScalar
lgs2816crpsIgmpProxyConfLastMemberQueryCount = _Lgs2816crpsIgmpProxyConfLastMemberQueryCount_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 25, 3, 4),
    _Lgs2816crpsIgmpProxyConfLastMemberQueryCount_Type()
)
lgs2816crpsIgmpProxyConfLastMemberQueryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsIgmpProxyConfLastMemberQueryCount.setStatus("current")


class _Lgs2816crpsIgmpProxyConfLastMemberQueryInterval_Type(Integer32):
    """Custom type lgs2816crpsIgmpProxyConfLastMemberQueryInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 25),
    )


_Lgs2816crpsIgmpProxyConfLastMemberQueryInterval_Type.__name__ = "Integer32"
_Lgs2816crpsIgmpProxyConfLastMemberQueryInterval_Object = MibScalar
lgs2816crpsIgmpProxyConfLastMemberQueryInterval = _Lgs2816crpsIgmpProxyConfLastMemberQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 25, 3, 5),
    _Lgs2816crpsIgmpProxyConfLastMemberQueryInterval_Type()
)
lgs2816crpsIgmpProxyConfLastMemberQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsIgmpProxyConfLastMemberQueryInterval.setStatus("current")


class _Lgs2816crpsIgmpProxyConfLastMemberQueryMaxRepTime_Type(Integer32):
    """Custom type lgs2816crpsIgmpProxyConfLastMemberQueryMaxRepTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 25),
    )


_Lgs2816crpsIgmpProxyConfLastMemberQueryMaxRepTime_Type.__name__ = "Integer32"
_Lgs2816crpsIgmpProxyConfLastMemberQueryMaxRepTime_Object = MibScalar
lgs2816crpsIgmpProxyConfLastMemberQueryMaxRepTime = _Lgs2816crpsIgmpProxyConfLastMemberQueryMaxRepTime_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 25, 3, 6),
    _Lgs2816crpsIgmpProxyConfLastMemberQueryMaxRepTime_Type()
)
lgs2816crpsIgmpProxyConfLastMemberQueryMaxRepTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsIgmpProxyConfLastMemberQueryMaxRepTime.setStatus("current")
_Lgs2816crpsIgmpProxyConfRouterPorts_Type = DisplayString
_Lgs2816crpsIgmpProxyConfRouterPorts_Object = MibScalar
lgs2816crpsIgmpProxyConfRouterPorts = _Lgs2816crpsIgmpProxyConfRouterPorts_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 25, 3, 7),
    _Lgs2816crpsIgmpProxyConfRouterPorts_Type()
)
lgs2816crpsIgmpProxyConfRouterPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsIgmpProxyConfRouterPorts.setStatus("current")


class _Lgs2816crpsIgmpProxyGroupMembershipNumber_Type(Integer32):
    """Custom type lgs2816crpsIgmpProxyGroupMembershipNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_Lgs2816crpsIgmpProxyGroupMembershipNumber_Type.__name__ = "Integer32"
_Lgs2816crpsIgmpProxyGroupMembershipNumber_Object = MibScalar
lgs2816crpsIgmpProxyGroupMembershipNumber = _Lgs2816crpsIgmpProxyGroupMembershipNumber_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 25, 3, 8),
    _Lgs2816crpsIgmpProxyGroupMembershipNumber_Type()
)
lgs2816crpsIgmpProxyGroupMembershipNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsIgmpProxyGroupMembershipNumber.setStatus("current")
_Lgs2816crpsIgmpProxyGroupMembershipTable_Object = MibTable
lgs2816crpsIgmpProxyGroupMembershipTable = _Lgs2816crpsIgmpProxyGroupMembershipTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 25, 3, 9)
)
if mibBuilder.loadTexts:
    lgs2816crpsIgmpProxyGroupMembershipTable.setStatus("current")
_Lgs2816crpsIgmpProxyGroupMembershipEntry_Object = MibTableRow
lgs2816crpsIgmpProxyGroupMembershipEntry = _Lgs2816crpsIgmpProxyGroupMembershipEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 25, 3, 9, 1)
)
lgs2816crpsIgmpProxyGroupMembershipEntry.setIndexNames(
    (0, "PRIVATE-LGS2816CRPS-MIB", "lgs2816crpsIgmpProxyGroupNo"),
)
if mibBuilder.loadTexts:
    lgs2816crpsIgmpProxyGroupMembershipEntry.setStatus("current")


class _Lgs2816crpsIgmpProxyGroupNo_Type(Integer32):
    """Custom type lgs2816crpsIgmpProxyGroupNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_Lgs2816crpsIgmpProxyGroupNo_Type.__name__ = "Integer32"
_Lgs2816crpsIgmpProxyGroupNo_Object = MibTableColumn
lgs2816crpsIgmpProxyGroupNo = _Lgs2816crpsIgmpProxyGroupNo_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 25, 3, 9, 1, 1),
    _Lgs2816crpsIgmpProxyGroupNo_Type()
)
lgs2816crpsIgmpProxyGroupNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgs2816crpsIgmpProxyGroupNo.setStatus("current")
_Lgs2816crpsIgmpProxyGroupAddress_Type = DisplayString
_Lgs2816crpsIgmpProxyGroupAddress_Object = MibTableColumn
lgs2816crpsIgmpProxyGroupAddress = _Lgs2816crpsIgmpProxyGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 25, 3, 9, 1, 2),
    _Lgs2816crpsIgmpProxyGroupAddress_Type()
)
lgs2816crpsIgmpProxyGroupAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsIgmpProxyGroupAddress.setStatus("current")


class _Lgs2816crpsIgmpProxyGroupVLANId_Type(Integer32):
    """Custom type lgs2816crpsIgmpProxyGroupVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Lgs2816crpsIgmpProxyGroupVLANId_Type.__name__ = "Integer32"
_Lgs2816crpsIgmpProxyGroupVLANId_Object = MibTableColumn
lgs2816crpsIgmpProxyGroupVLANId = _Lgs2816crpsIgmpProxyGroupVLANId_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 25, 3, 9, 1, 3),
    _Lgs2816crpsIgmpProxyGroupVLANId_Type()
)
lgs2816crpsIgmpProxyGroupVLANId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsIgmpProxyGroupVLANId.setStatus("current")
_Lgs2816crpsIgmpProxyGroupPortMembers_Type = DisplayString
_Lgs2816crpsIgmpProxyGroupPortMembers_Object = MibTableColumn
lgs2816crpsIgmpProxyGroupPortMembers = _Lgs2816crpsIgmpProxyGroupPortMembers_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 25, 3, 9, 1, 4),
    _Lgs2816crpsIgmpProxyGroupPortMembers_Type()
)
lgs2816crpsIgmpProxyGroupPortMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsIgmpProxyGroupPortMembers.setStatus("current")
_Lgs2816crpsIGMPSnooping_ObjectIdentity = ObjectIdentity
lgs2816crpsIGMPSnooping = _Lgs2816crpsIGMPSnooping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 25, 4)
)


class _Lgs2816crpsIgmpSnoopingConfHostTimeout_Type(Integer32):
    """Custom type lgs2816crpsIgmpSnoopingConfHostTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Lgs2816crpsIgmpSnoopingConfHostTimeout_Type.__name__ = "Integer32"
_Lgs2816crpsIgmpSnoopingConfHostTimeout_Object = MibScalar
lgs2816crpsIgmpSnoopingConfHostTimeout = _Lgs2816crpsIgmpSnoopingConfHostTimeout_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 25, 4, 1),
    _Lgs2816crpsIgmpSnoopingConfHostTimeout_Type()
)
lgs2816crpsIgmpSnoopingConfHostTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsIgmpSnoopingConfHostTimeout.setStatus("current")
_Lgs2816crpsIgmpSnoopingConfFastLeave_Type = DisplayString
_Lgs2816crpsIgmpSnoopingConfFastLeave_Object = MibScalar
lgs2816crpsIgmpSnoopingConfFastLeave = _Lgs2816crpsIgmpSnoopingConfFastLeave_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 25, 4, 2),
    _Lgs2816crpsIgmpSnoopingConfFastLeave_Type()
)
lgs2816crpsIgmpSnoopingConfFastLeave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsIgmpSnoopingConfFastLeave.setStatus("current")
_Lgs2816crpsIgmpSnoopingConfRouterPorts_Type = DisplayString
_Lgs2816crpsIgmpSnoopingConfRouterPorts_Object = MibScalar
lgs2816crpsIgmpSnoopingConfRouterPorts = _Lgs2816crpsIgmpSnoopingConfRouterPorts_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 25, 4, 3),
    _Lgs2816crpsIgmpSnoopingConfRouterPorts_Type()
)
lgs2816crpsIgmpSnoopingConfRouterPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsIgmpSnoopingConfRouterPorts.setStatus("current")


class _Lgs2816crpsIgmpSnoopingGroupMembershipNumber_Type(Integer32):
    """Custom type lgs2816crpsIgmpSnoopingGroupMembershipNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_Lgs2816crpsIgmpSnoopingGroupMembershipNumber_Type.__name__ = "Integer32"
_Lgs2816crpsIgmpSnoopingGroupMembershipNumber_Object = MibScalar
lgs2816crpsIgmpSnoopingGroupMembershipNumber = _Lgs2816crpsIgmpSnoopingGroupMembershipNumber_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 25, 4, 4),
    _Lgs2816crpsIgmpSnoopingGroupMembershipNumber_Type()
)
lgs2816crpsIgmpSnoopingGroupMembershipNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsIgmpSnoopingGroupMembershipNumber.setStatus("current")
_Lgs2816crpsIgmpSnoopingGroupMembershipTable_Object = MibTable
lgs2816crpsIgmpSnoopingGroupMembershipTable = _Lgs2816crpsIgmpSnoopingGroupMembershipTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 25, 4, 5)
)
if mibBuilder.loadTexts:
    lgs2816crpsIgmpSnoopingGroupMembershipTable.setStatus("current")
_Lgs2816crpsIgmpSnoopingGroupMembershipEntry_Object = MibTableRow
lgs2816crpsIgmpSnoopingGroupMembershipEntry = _Lgs2816crpsIgmpSnoopingGroupMembershipEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 25, 4, 5, 1)
)
lgs2816crpsIgmpSnoopingGroupMembershipEntry.setIndexNames(
    (0, "PRIVATE-LGS2816CRPS-MIB", "lgs2816crpsIgmpSnoopingGroupNo"),
)
if mibBuilder.loadTexts:
    lgs2816crpsIgmpSnoopingGroupMembershipEntry.setStatus("current")


class _Lgs2816crpsIgmpSnoopingGroupNo_Type(Integer32):
    """Custom type lgs2816crpsIgmpSnoopingGroupNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_Lgs2816crpsIgmpSnoopingGroupNo_Type.__name__ = "Integer32"
_Lgs2816crpsIgmpSnoopingGroupNo_Object = MibTableColumn
lgs2816crpsIgmpSnoopingGroupNo = _Lgs2816crpsIgmpSnoopingGroupNo_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 25, 4, 5, 1, 1),
    _Lgs2816crpsIgmpSnoopingGroupNo_Type()
)
lgs2816crpsIgmpSnoopingGroupNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgs2816crpsIgmpSnoopingGroupNo.setStatus("current")
_Lgs2816crpsIgmpSnoopingGroupAddress_Type = DisplayString
_Lgs2816crpsIgmpSnoopingGroupAddress_Object = MibTableColumn
lgs2816crpsIgmpSnoopingGroupAddress = _Lgs2816crpsIgmpSnoopingGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 25, 4, 5, 1, 2),
    _Lgs2816crpsIgmpSnoopingGroupAddress_Type()
)
lgs2816crpsIgmpSnoopingGroupAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsIgmpSnoopingGroupAddress.setStatus("current")


class _Lgs2816crpsIgmpSnoopingGroupVLANId_Type(Integer32):
    """Custom type lgs2816crpsIgmpSnoopingGroupVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Lgs2816crpsIgmpSnoopingGroupVLANId_Type.__name__ = "Integer32"
_Lgs2816crpsIgmpSnoopingGroupVLANId_Object = MibTableColumn
lgs2816crpsIgmpSnoopingGroupVLANId = _Lgs2816crpsIgmpSnoopingGroupVLANId_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 25, 4, 5, 1, 3),
    _Lgs2816crpsIgmpSnoopingGroupVLANId_Type()
)
lgs2816crpsIgmpSnoopingGroupVLANId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsIgmpSnoopingGroupVLANId.setStatus("current")
_Lgs2816crpsIgmpSnoopingGroupPortMembers_Type = DisplayString
_Lgs2816crpsIgmpSnoopingGroupPortMembers_Object = MibTableColumn
lgs2816crpsIgmpSnoopingGroupPortMembers = _Lgs2816crpsIgmpSnoopingGroupPortMembers_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 25, 4, 5, 1, 4),
    _Lgs2816crpsIgmpSnoopingGroupPortMembers_Type()
)
lgs2816crpsIgmpSnoopingGroupPortMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsIgmpSnoopingGroupPortMembers.setStatus("current")
_Lgs2816crpsMVR_ObjectIdentity = ObjectIdentity
lgs2816crpsMVR = _Lgs2816crpsMVR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 25, 5)
)


class _Lgs2816crpsMVRMode_Type(Integer32):
    """Custom type lgs2816crpsMVRMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2816crpsMVRMode_Type.__name__ = "Integer32"
_Lgs2816crpsMVRMode_Object = MibScalar
lgs2816crpsMVRMode = _Lgs2816crpsMVRMode_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 25, 5, 1),
    _Lgs2816crpsMVRMode_Type()
)
lgs2816crpsMVRMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsMVRMode.setStatus("current")


class _Lgs2816crpsMVRConfHostTimeout_Type(Integer32):
    """Custom type lgs2816crpsMVRConfHostTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Lgs2816crpsMVRConfHostTimeout_Type.__name__ = "Integer32"
_Lgs2816crpsMVRConfHostTimeout_Object = MibScalar
lgs2816crpsMVRConfHostTimeout = _Lgs2816crpsMVRConfHostTimeout_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 25, 5, 2),
    _Lgs2816crpsMVRConfHostTimeout_Type()
)
lgs2816crpsMVRConfHostTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsMVRConfHostTimeout.setStatus("current")
_Lgs2816crpsMVRConfFastLeave_Type = DisplayString
_Lgs2816crpsMVRConfFastLeave_Object = MibScalar
lgs2816crpsMVRConfFastLeave = _Lgs2816crpsMVRConfFastLeave_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 25, 5, 3),
    _Lgs2816crpsMVRConfFastLeave_Type()
)
lgs2816crpsMVRConfFastLeave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsMVRConfFastLeave.setStatus("current")
_Lgs2816crpsMVIDConf_ObjectIdentity = ObjectIdentity
lgs2816crpsMVIDConf = _Lgs2816crpsMVIDConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 25, 5, 4)
)


class _Lgs2816crpsMVIDNumber_Type(Integer32):
    """Custom type lgs2816crpsMVIDNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Lgs2816crpsMVIDNumber_Type.__name__ = "Integer32"
_Lgs2816crpsMVIDNumber_Object = MibScalar
lgs2816crpsMVIDNumber = _Lgs2816crpsMVIDNumber_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 25, 5, 4, 1),
    _Lgs2816crpsMVIDNumber_Type()
)
lgs2816crpsMVIDNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsMVIDNumber.setStatus("current")


class _Lgs2816crpsMVIDEntryCreate_Type(Integer32):
    """Custom type lgs2816crpsMVIDEntryCreate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Lgs2816crpsMVIDEntryCreate_Type.__name__ = "Integer32"
_Lgs2816crpsMVIDEntryCreate_Object = MibScalar
lgs2816crpsMVIDEntryCreate = _Lgs2816crpsMVIDEntryCreate_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 25, 5, 4, 2),
    _Lgs2816crpsMVIDEntryCreate_Type()
)
lgs2816crpsMVIDEntryCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsMVIDEntryCreate.setStatus("current")
_Lgs2816crpsMVIDGroupTable_Object = MibTable
lgs2816crpsMVIDGroupTable = _Lgs2816crpsMVIDGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 25, 5, 4, 3)
)
if mibBuilder.loadTexts:
    lgs2816crpsMVIDGroupTable.setStatus("current")
_Lgs2816crpsMVIDGroupEntry_Object = MibTableRow
lgs2816crpsMVIDGroupEntry = _Lgs2816crpsMVIDGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 25, 5, 4, 3, 1)
)
lgs2816crpsMVIDGroupEntry.setIndexNames(
    (0, "PRIVATE-LGS2816CRPS-MIB", "lgs2816crpsMVID"),
)
if mibBuilder.loadTexts:
    lgs2816crpsMVIDGroupEntry.setStatus("current")


class _Lgs2816crpsMVID_Type(Integer32):
    """Custom type lgs2816crpsMVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Lgs2816crpsMVID_Type.__name__ = "Integer32"
_Lgs2816crpsMVID_Object = MibTableColumn
lgs2816crpsMVID = _Lgs2816crpsMVID_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 25, 5, 4, 3, 1, 1),
    _Lgs2816crpsMVID_Type()
)
lgs2816crpsMVID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgs2816crpsMVID.setStatus("current")
_Lgs2816crpsMVIDMemberPort_Type = DisplayString
_Lgs2816crpsMVIDMemberPort_Object = MibTableColumn
lgs2816crpsMVIDMemberPort = _Lgs2816crpsMVIDMemberPort_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 25, 5, 4, 3, 1, 2),
    _Lgs2816crpsMVIDMemberPort_Type()
)
lgs2816crpsMVIDMemberPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsMVIDMemberPort.setStatus("current")
_Lgs2816crpsMVIDRouterPorts_Type = DisplayString
_Lgs2816crpsMVIDRouterPorts_Object = MibTableColumn
lgs2816crpsMVIDRouterPorts = _Lgs2816crpsMVIDRouterPorts_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 25, 5, 4, 3, 1, 3),
    _Lgs2816crpsMVIDRouterPorts_Type()
)
lgs2816crpsMVIDRouterPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsMVIDRouterPorts.setStatus("current")


class _Lgs2816crpsMVIDEntryAction_Type(Integer32):
    """Custom type lgs2816crpsMVIDEntryAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Lgs2816crpsMVIDEntryAction_Type.__name__ = "Integer32"
_Lgs2816crpsMVIDEntryAction_Object = MibTableColumn
lgs2816crpsMVIDEntryAction = _Lgs2816crpsMVIDEntryAction_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 25, 5, 4, 3, 1, 4),
    _Lgs2816crpsMVIDEntryAction_Type()
)
lgs2816crpsMVIDEntryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsMVIDEntryAction.setStatus("current")
_Lgs2816crpsMVIDGroupAllowConf_ObjectIdentity = ObjectIdentity
lgs2816crpsMVIDGroupAllowConf = _Lgs2816crpsMVIDGroupAllowConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 25, 5, 5)
)


class _Lgs2816crpsMVIDGroupAllowNumber_Type(Integer32):
    """Custom type lgs2816crpsMVIDGroupAllowNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Lgs2816crpsMVIDGroupAllowNumber_Type.__name__ = "Integer32"
_Lgs2816crpsMVIDGroupAllowNumber_Object = MibScalar
lgs2816crpsMVIDGroupAllowNumber = _Lgs2816crpsMVIDGroupAllowNumber_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 25, 5, 5, 1),
    _Lgs2816crpsMVIDGroupAllowNumber_Type()
)
lgs2816crpsMVIDGroupAllowNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsMVIDGroupAllowNumber.setStatus("current")


class _Lgs2816crpsMVIDGroupAllowEntryCreate_Type(Integer32):
    """Custom type lgs2816crpsMVIDGroupAllowEntryCreate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Lgs2816crpsMVIDGroupAllowEntryCreate_Type.__name__ = "Integer32"
_Lgs2816crpsMVIDGroupAllowEntryCreate_Object = MibScalar
lgs2816crpsMVIDGroupAllowEntryCreate = _Lgs2816crpsMVIDGroupAllowEntryCreate_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 25, 5, 5, 2),
    _Lgs2816crpsMVIDGroupAllowEntryCreate_Type()
)
lgs2816crpsMVIDGroupAllowEntryCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsMVIDGroupAllowEntryCreate.setStatus("current")
_Lgs2816crpsMVIDGroupAllowTable_Object = MibTable
lgs2816crpsMVIDGroupAllowTable = _Lgs2816crpsMVIDGroupAllowTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 25, 5, 5, 3)
)
if mibBuilder.loadTexts:
    lgs2816crpsMVIDGroupAllowTable.setStatus("current")
_Lgs2816crpsMVIDGroupAllowEntry_Object = MibTableRow
lgs2816crpsMVIDGroupAllowEntry = _Lgs2816crpsMVIDGroupAllowEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 25, 5, 5, 3, 1)
)
lgs2816crpsMVIDGroupAllowEntry.setIndexNames(
    (0, "PRIVATE-LGS2816CRPS-MIB", "lgs2816crpsMVIDGroupAllowNo"),
)
if mibBuilder.loadTexts:
    lgs2816crpsMVIDGroupAllowEntry.setStatus("current")


class _Lgs2816crpsMVIDGroupAllowNo_Type(Integer32):
    """Custom type lgs2816crpsMVIDGroupAllowNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Lgs2816crpsMVIDGroupAllowNo_Type.__name__ = "Integer32"
_Lgs2816crpsMVIDGroupAllowNo_Object = MibTableColumn
lgs2816crpsMVIDGroupAllowNo = _Lgs2816crpsMVIDGroupAllowNo_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 25, 5, 5, 3, 1, 1),
    _Lgs2816crpsMVIDGroupAllowNo_Type()
)
lgs2816crpsMVIDGroupAllowNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgs2816crpsMVIDGroupAllowNo.setStatus("current")


class _Lgs2816crpsMVIDGroupAllowMvid_Type(Integer32):
    """Custom type lgs2816crpsMVIDGroupAllowMvid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Lgs2816crpsMVIDGroupAllowMvid_Type.__name__ = "Integer32"
_Lgs2816crpsMVIDGroupAllowMvid_Object = MibTableColumn
lgs2816crpsMVIDGroupAllowMvid = _Lgs2816crpsMVIDGroupAllowMvid_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 25, 5, 5, 3, 1, 2),
    _Lgs2816crpsMVIDGroupAllowMvid_Type()
)
lgs2816crpsMVIDGroupAllowMvid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsMVIDGroupAllowMvid.setStatus("current")
_Lgs2816crpsMVIDGroupAllowStartAddress_Type = DisplayString
_Lgs2816crpsMVIDGroupAllowStartAddress_Object = MibTableColumn
lgs2816crpsMVIDGroupAllowStartAddress = _Lgs2816crpsMVIDGroupAllowStartAddress_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 25, 5, 5, 3, 1, 3),
    _Lgs2816crpsMVIDGroupAllowStartAddress_Type()
)
lgs2816crpsMVIDGroupAllowStartAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsMVIDGroupAllowStartAddress.setStatus("current")
_Lgs2816crpsMVIDGroupAllowEndAddress_Type = DisplayString
_Lgs2816crpsMVIDGroupAllowEndAddress_Object = MibTableColumn
lgs2816crpsMVIDGroupAllowEndAddress = _Lgs2816crpsMVIDGroupAllowEndAddress_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 25, 5, 5, 3, 1, 4),
    _Lgs2816crpsMVIDGroupAllowEndAddress_Type()
)
lgs2816crpsMVIDGroupAllowEndAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsMVIDGroupAllowEndAddress.setStatus("current")


class _Lgs2816crpsMVIDGroupAllowEntryAction_Type(Integer32):
    """Custom type lgs2816crpsMVIDGroupAllowEntryAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Lgs2816crpsMVIDGroupAllowEntryAction_Type.__name__ = "Integer32"
_Lgs2816crpsMVIDGroupAllowEntryAction_Object = MibTableColumn
lgs2816crpsMVIDGroupAllowEntryAction = _Lgs2816crpsMVIDGroupAllowEntryAction_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 25, 5, 5, 3, 1, 5),
    _Lgs2816crpsMVIDGroupAllowEntryAction_Type()
)
lgs2816crpsMVIDGroupAllowEntryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsMVIDGroupAllowEntryAction.setStatus("current")


class _Lgs2816crpsMVRGroupMembershipNumber_Type(Integer32):
    """Custom type lgs2816crpsMVRGroupMembershipNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_Lgs2816crpsMVRGroupMembershipNumber_Type.__name__ = "Integer32"
_Lgs2816crpsMVRGroupMembershipNumber_Object = MibScalar
lgs2816crpsMVRGroupMembershipNumber = _Lgs2816crpsMVRGroupMembershipNumber_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 25, 5, 6),
    _Lgs2816crpsMVRGroupMembershipNumber_Type()
)
lgs2816crpsMVRGroupMembershipNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsMVRGroupMembershipNumber.setStatus("current")
_Lgs2816crpsMVRGroupMembershipTable_Object = MibTable
lgs2816crpsMVRGroupMembershipTable = _Lgs2816crpsMVRGroupMembershipTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 25, 5, 7)
)
if mibBuilder.loadTexts:
    lgs2816crpsMVRGroupMembershipTable.setStatus("current")
_Lgs2816crpsMVRGroupMembershipEntry_Object = MibTableRow
lgs2816crpsMVRGroupMembershipEntry = _Lgs2816crpsMVRGroupMembershipEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 25, 5, 7, 1)
)
lgs2816crpsMVRGroupMembershipEntry.setIndexNames(
    (0, "PRIVATE-LGS2816CRPS-MIB", "lgs2816crpsMVRGroupNo"),
)
if mibBuilder.loadTexts:
    lgs2816crpsMVRGroupMembershipEntry.setStatus("current")


class _Lgs2816crpsMVRGroupNo_Type(Integer32):
    """Custom type lgs2816crpsMVRGroupNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_Lgs2816crpsMVRGroupNo_Type.__name__ = "Integer32"
_Lgs2816crpsMVRGroupNo_Object = MibTableColumn
lgs2816crpsMVRGroupNo = _Lgs2816crpsMVRGroupNo_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 25, 5, 7, 1, 1),
    _Lgs2816crpsMVRGroupNo_Type()
)
lgs2816crpsMVRGroupNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgs2816crpsMVRGroupNo.setStatus("current")
_Lgs2816crpsMVRGroupAddress_Type = DisplayString
_Lgs2816crpsMVRGroupAddress_Object = MibTableColumn
lgs2816crpsMVRGroupAddress = _Lgs2816crpsMVRGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 25, 5, 7, 1, 2),
    _Lgs2816crpsMVRGroupAddress_Type()
)
lgs2816crpsMVRGroupAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsMVRGroupAddress.setStatus("current")


class _Lgs2816crpsMVRGroupVLANId_Type(Integer32):
    """Custom type lgs2816crpsMVRGroupVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Lgs2816crpsMVRGroupVLANId_Type.__name__ = "Integer32"
_Lgs2816crpsMVRGroupVLANId_Object = MibTableColumn
lgs2816crpsMVRGroupVLANId = _Lgs2816crpsMVRGroupVLANId_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 25, 5, 7, 1, 3),
    _Lgs2816crpsMVRGroupVLANId_Type()
)
lgs2816crpsMVRGroupVLANId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsMVRGroupVLANId.setStatus("current")
_Lgs2816crpsMVRGroupPortMembers_Type = DisplayString
_Lgs2816crpsMVRGroupPortMembers_Object = MibTableColumn
lgs2816crpsMVRGroupPortMembers = _Lgs2816crpsMVRGroupPortMembers_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 25, 5, 7, 1, 4),
    _Lgs2816crpsMVRGroupPortMembers_Type()
)
lgs2816crpsMVRGroupPortMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsMVRGroupPortMembers.setStatus("current")
_Lgs2816crpsDhcpSnooping_ObjectIdentity = ObjectIdentity
lgs2816crpsDhcpSnooping = _Lgs2816crpsDhcpSnooping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 26)
)


class _Lgs2816crpsDhcpSnoopingState_Type(Integer32):
    """Custom type lgs2816crpsDhcpSnoopingState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2816crpsDhcpSnoopingState_Type.__name__ = "Integer32"
_Lgs2816crpsDhcpSnoopingState_Object = MibScalar
lgs2816crpsDhcpSnoopingState = _Lgs2816crpsDhcpSnoopingState_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 26, 1),
    _Lgs2816crpsDhcpSnoopingState_Type()
)
lgs2816crpsDhcpSnoopingState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsDhcpSnoopingState.setStatus("current")
_Lgs2816crpsDhcpSnoopingInfo_ObjectIdentity = ObjectIdentity
lgs2816crpsDhcpSnoopingInfo = _Lgs2816crpsDhcpSnoopingInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 26, 2)
)


class _Lgs2816crpsDhcpSnoopingCreate_Type(Integer32):
    """Custom type lgs2816crpsDhcpSnoopingCreate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2816crpsDhcpSnoopingCreate_Type.__name__ = "Integer32"
_Lgs2816crpsDhcpSnoopingCreate_Object = MibScalar
lgs2816crpsDhcpSnoopingCreate = _Lgs2816crpsDhcpSnoopingCreate_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 26, 2, 1),
    _Lgs2816crpsDhcpSnoopingCreate_Type()
)
lgs2816crpsDhcpSnoopingCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsDhcpSnoopingCreate.setStatus("current")
_Lgs2816crpsDhcpSnoopingTable_Object = MibTable
lgs2816crpsDhcpSnoopingTable = _Lgs2816crpsDhcpSnoopingTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 26, 2, 2)
)
if mibBuilder.loadTexts:
    lgs2816crpsDhcpSnoopingTable.setStatus("current")
_Lgs2816crpsDhcpSnoopingEntry_Object = MibTableRow
lgs2816crpsDhcpSnoopingEntry = _Lgs2816crpsDhcpSnoopingEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 26, 2, 2, 1)
)
lgs2816crpsDhcpSnoopingEntry.setIndexNames(
    (0, "PRIVATE-LGS2816CRPS-MIB", "lgs2816crpsDhcpSnoopingIndex"),
)
if mibBuilder.loadTexts:
    lgs2816crpsDhcpSnoopingEntry.setStatus("current")


class _Lgs2816crpsDhcpSnoopingIndex_Type(Integer32):
    """Custom type lgs2816crpsDhcpSnoopingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Lgs2816crpsDhcpSnoopingIndex_Type.__name__ = "Integer32"
_Lgs2816crpsDhcpSnoopingIndex_Object = MibTableColumn
lgs2816crpsDhcpSnoopingIndex = _Lgs2816crpsDhcpSnoopingIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 26, 2, 2, 1, 1),
    _Lgs2816crpsDhcpSnoopingIndex_Type()
)
lgs2816crpsDhcpSnoopingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgs2816crpsDhcpSnoopingIndex.setStatus("current")


class _Lgs2816crpsDhcpSnoopingVID_Type(Integer32):
    """Custom type lgs2816crpsDhcpSnoopingVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Lgs2816crpsDhcpSnoopingVID_Type.__name__ = "Integer32"
_Lgs2816crpsDhcpSnoopingVID_Object = MibTableColumn
lgs2816crpsDhcpSnoopingVID = _Lgs2816crpsDhcpSnoopingVID_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 26, 2, 2, 1, 2),
    _Lgs2816crpsDhcpSnoopingVID_Type()
)
lgs2816crpsDhcpSnoopingVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsDhcpSnoopingVID.setStatus("current")


class _Lgs2816crpsDhcpSnoopingTrustPort1_Type(Integer32):
    """Custom type lgs2816crpsDhcpSnoopingTrustPort1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_Lgs2816crpsDhcpSnoopingTrustPort1_Type.__name__ = "Integer32"
_Lgs2816crpsDhcpSnoopingTrustPort1_Object = MibTableColumn
lgs2816crpsDhcpSnoopingTrustPort1 = _Lgs2816crpsDhcpSnoopingTrustPort1_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 26, 2, 2, 1, 3),
    _Lgs2816crpsDhcpSnoopingTrustPort1_Type()
)
lgs2816crpsDhcpSnoopingTrustPort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsDhcpSnoopingTrustPort1.setStatus("current")


class _Lgs2816crpsDhcpSnoopingTrustPort2_Type(Integer32):
    """Custom type lgs2816crpsDhcpSnoopingTrustPort2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_Lgs2816crpsDhcpSnoopingTrustPort2_Type.__name__ = "Integer32"
_Lgs2816crpsDhcpSnoopingTrustPort2_Object = MibTableColumn
lgs2816crpsDhcpSnoopingTrustPort2 = _Lgs2816crpsDhcpSnoopingTrustPort2_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 26, 2, 2, 1, 4),
    _Lgs2816crpsDhcpSnoopingTrustPort2_Type()
)
lgs2816crpsDhcpSnoopingTrustPort2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsDhcpSnoopingTrustPort2.setStatus("current")
_Lgs2816crpsDhcpSnoopingServerIP_Type = IpAddress
_Lgs2816crpsDhcpSnoopingServerIP_Object = MibTableColumn
lgs2816crpsDhcpSnoopingServerIP = _Lgs2816crpsDhcpSnoopingServerIP_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 26, 2, 2, 1, 5),
    _Lgs2816crpsDhcpSnoopingServerIP_Type()
)
lgs2816crpsDhcpSnoopingServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsDhcpSnoopingServerIP.setStatus("current")


class _Lgs2816crpsDhcpSnoopingOption82_Type(Integer32):
    """Custom type lgs2816crpsDhcpSnoopingOption82 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2816crpsDhcpSnoopingOption82_Type.__name__ = "Integer32"
_Lgs2816crpsDhcpSnoopingOption82_Object = MibTableColumn
lgs2816crpsDhcpSnoopingOption82 = _Lgs2816crpsDhcpSnoopingOption82_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 26, 2, 2, 1, 6),
    _Lgs2816crpsDhcpSnoopingOption82_Type()
)
lgs2816crpsDhcpSnoopingOption82.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsDhcpSnoopingOption82.setStatus("current")


class _Lgs2816crpsDhcpSnoopingAction_Type(Integer32):
    """Custom type lgs2816crpsDhcpSnoopingAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Lgs2816crpsDhcpSnoopingAction_Type.__name__ = "Integer32"
_Lgs2816crpsDhcpSnoopingAction_Object = MibTableColumn
lgs2816crpsDhcpSnoopingAction = _Lgs2816crpsDhcpSnoopingAction_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 26, 2, 2, 1, 7),
    _Lgs2816crpsDhcpSnoopingAction_Type()
)
lgs2816crpsDhcpSnoopingAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsDhcpSnoopingAction.setStatus("current")


class _Lgs2816crpsDhcpSnoopingEntryAction_Type(Integer32):
    """Custom type lgs2816crpsDhcpSnoopingEntryAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Lgs2816crpsDhcpSnoopingEntryAction_Type.__name__ = "Integer32"
_Lgs2816crpsDhcpSnoopingEntryAction_Object = MibTableColumn
lgs2816crpsDhcpSnoopingEntryAction = _Lgs2816crpsDhcpSnoopingEntryAction_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 26, 2, 2, 1, 8),
    _Lgs2816crpsDhcpSnoopingEntryAction_Type()
)
lgs2816crpsDhcpSnoopingEntryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsDhcpSnoopingEntryAction.setStatus("current")
_Lgs2816crpsDhcpSnoopingDefaultData_ObjectIdentity = ObjectIdentity
lgs2816crpsDhcpSnoopingDefaultData = _Lgs2816crpsDhcpSnoopingDefaultData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 26, 2, 3)
)


class _Lgs2816crpsDhcpSnoopingDefaultVID_Type(Integer32):
    """Custom type lgs2816crpsDhcpSnoopingDefaultVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Lgs2816crpsDhcpSnoopingDefaultVID_Type.__name__ = "Integer32"
_Lgs2816crpsDhcpSnoopingDefaultVID_Object = MibScalar
lgs2816crpsDhcpSnoopingDefaultVID = _Lgs2816crpsDhcpSnoopingDefaultVID_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 26, 2, 3, 1),
    _Lgs2816crpsDhcpSnoopingDefaultVID_Type()
)
lgs2816crpsDhcpSnoopingDefaultVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsDhcpSnoopingDefaultVID.setStatus("current")


class _Lgs2816crpsDhcpSnoopingDefaultTrustPort1_Type(Integer32):
    """Custom type lgs2816crpsDhcpSnoopingDefaultTrustPort1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_Lgs2816crpsDhcpSnoopingDefaultTrustPort1_Type.__name__ = "Integer32"
_Lgs2816crpsDhcpSnoopingDefaultTrustPort1_Object = MibScalar
lgs2816crpsDhcpSnoopingDefaultTrustPort1 = _Lgs2816crpsDhcpSnoopingDefaultTrustPort1_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 26, 2, 3, 2),
    _Lgs2816crpsDhcpSnoopingDefaultTrustPort1_Type()
)
lgs2816crpsDhcpSnoopingDefaultTrustPort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsDhcpSnoopingDefaultTrustPort1.setStatus("current")


class _Lgs2816crpsDhcpSnoopingDefaultTrustPort2_Type(Integer32):
    """Custom type lgs2816crpsDhcpSnoopingDefaultTrustPort2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_Lgs2816crpsDhcpSnoopingDefaultTrustPort2_Type.__name__ = "Integer32"
_Lgs2816crpsDhcpSnoopingDefaultTrustPort2_Object = MibScalar
lgs2816crpsDhcpSnoopingDefaultTrustPort2 = _Lgs2816crpsDhcpSnoopingDefaultTrustPort2_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 26, 2, 3, 3),
    _Lgs2816crpsDhcpSnoopingDefaultTrustPort2_Type()
)
lgs2816crpsDhcpSnoopingDefaultTrustPort2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsDhcpSnoopingDefaultTrustPort2.setStatus("current")
_Lgs2816crpsDhcpSnoopingDefaultServerIP_Type = IpAddress
_Lgs2816crpsDhcpSnoopingDefaultServerIP_Object = MibScalar
lgs2816crpsDhcpSnoopingDefaultServerIP = _Lgs2816crpsDhcpSnoopingDefaultServerIP_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 26, 2, 3, 4),
    _Lgs2816crpsDhcpSnoopingDefaultServerIP_Type()
)
lgs2816crpsDhcpSnoopingDefaultServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsDhcpSnoopingDefaultServerIP.setStatus("current")


class _Lgs2816crpsDhcpSnoopingDefaultOption82_Type(Integer32):
    """Custom type lgs2816crpsDhcpSnoopingDefaultOption82 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Lgs2816crpsDhcpSnoopingDefaultOption82_Type.__name__ = "Integer32"
_Lgs2816crpsDhcpSnoopingDefaultOption82_Object = MibScalar
lgs2816crpsDhcpSnoopingDefaultOption82 = _Lgs2816crpsDhcpSnoopingDefaultOption82_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 26, 2, 3, 5),
    _Lgs2816crpsDhcpSnoopingDefaultOption82_Type()
)
lgs2816crpsDhcpSnoopingDefaultOption82.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsDhcpSnoopingDefaultOption82.setStatus("current")


class _Lgs2816crpsDhcpSnoopingDefaultAction_Type(Integer32):
    """Custom type lgs2816crpsDhcpSnoopingDefaultAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Lgs2816crpsDhcpSnoopingDefaultAction_Type.__name__ = "Integer32"
_Lgs2816crpsDhcpSnoopingDefaultAction_Object = MibScalar
lgs2816crpsDhcpSnoopingDefaultAction = _Lgs2816crpsDhcpSnoopingDefaultAction_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 26, 2, 3, 6),
    _Lgs2816crpsDhcpSnoopingDefaultAction_Type()
)
lgs2816crpsDhcpSnoopingDefaultAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsDhcpSnoopingDefaultAction.setStatus("current")


class _Lgs2816crpsDhcpSnoopingDefaultEntryAction_Type(Integer32):
    """Custom type lgs2816crpsDhcpSnoopingDefaultEntryAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Lgs2816crpsDhcpSnoopingDefaultEntryAction_Type.__name__ = "Integer32"
_Lgs2816crpsDhcpSnoopingDefaultEntryAction_Object = MibScalar
lgs2816crpsDhcpSnoopingDefaultEntryAction = _Lgs2816crpsDhcpSnoopingDefaultEntryAction_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 26, 2, 3, 7),
    _Lgs2816crpsDhcpSnoopingDefaultEntryAction_Type()
)
lgs2816crpsDhcpSnoopingDefaultEntryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgs2816crpsDhcpSnoopingDefaultEntryAction.setStatus("current")
_Lgs2816crpsDhcpSnoopingClientTable_Object = MibTable
lgs2816crpsDhcpSnoopingClientTable = _Lgs2816crpsDhcpSnoopingClientTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 26, 3)
)
if mibBuilder.loadTexts:
    lgs2816crpsDhcpSnoopingClientTable.setStatus("current")
_Lgs2816crpsDhcpSnoopingClientEntry_Object = MibTableRow
lgs2816crpsDhcpSnoopingClientEntry = _Lgs2816crpsDhcpSnoopingClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 26, 3, 1)
)
lgs2816crpsDhcpSnoopingClientEntry.setIndexNames(
    (0, "PRIVATE-LGS2816CRPS-MIB", "lgs2816crpsDhcpSnoopingClientIndex"),
)
if mibBuilder.loadTexts:
    lgs2816crpsDhcpSnoopingClientEntry.setStatus("current")


class _Lgs2816crpsDhcpSnoopingClientIndex_Type(Integer32):
    """Custom type lgs2816crpsDhcpSnoopingClientIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_Lgs2816crpsDhcpSnoopingClientIndex_Type.__name__ = "Integer32"
_Lgs2816crpsDhcpSnoopingClientIndex_Object = MibTableColumn
lgs2816crpsDhcpSnoopingClientIndex = _Lgs2816crpsDhcpSnoopingClientIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 26, 3, 1, 1),
    _Lgs2816crpsDhcpSnoopingClientIndex_Type()
)
lgs2816crpsDhcpSnoopingClientIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgs2816crpsDhcpSnoopingClientIndex.setStatus("current")
_Lgs2816crpsDhcpSnoopingClientMac_Type = DisplayString
_Lgs2816crpsDhcpSnoopingClientMac_Object = MibTableColumn
lgs2816crpsDhcpSnoopingClientMac = _Lgs2816crpsDhcpSnoopingClientMac_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 26, 3, 1, 2),
    _Lgs2816crpsDhcpSnoopingClientMac_Type()
)
lgs2816crpsDhcpSnoopingClientMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsDhcpSnoopingClientMac.setStatus("current")


class _Lgs2816crpsDhcpSnoopingClientVID_Type(Integer32):
    """Custom type lgs2816crpsDhcpSnoopingClientVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Lgs2816crpsDhcpSnoopingClientVID_Type.__name__ = "Integer32"
_Lgs2816crpsDhcpSnoopingClientVID_Object = MibTableColumn
lgs2816crpsDhcpSnoopingClientVID = _Lgs2816crpsDhcpSnoopingClientVID_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 26, 3, 1, 3),
    _Lgs2816crpsDhcpSnoopingClientVID_Type()
)
lgs2816crpsDhcpSnoopingClientVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsDhcpSnoopingClientVID.setStatus("current")


class _Lgs2816crpsDhcpSnoopingClientPort_Type(Integer32):
    """Custom type lgs2816crpsDhcpSnoopingClientPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Lgs2816crpsDhcpSnoopingClientPort_Type.__name__ = "Integer32"
_Lgs2816crpsDhcpSnoopingClientPort_Object = MibTableColumn
lgs2816crpsDhcpSnoopingClientPort = _Lgs2816crpsDhcpSnoopingClientPort_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 26, 3, 1, 4),
    _Lgs2816crpsDhcpSnoopingClientPort_Type()
)
lgs2816crpsDhcpSnoopingClientPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsDhcpSnoopingClientPort.setStatus("current")
_Lgs2816crpsDhcpSnoopingClientIP_Type = IpAddress
_Lgs2816crpsDhcpSnoopingClientIP_Object = MibTableColumn
lgs2816crpsDhcpSnoopingClientIP = _Lgs2816crpsDhcpSnoopingClientIP_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 26, 3, 1, 5),
    _Lgs2816crpsDhcpSnoopingClientIP_Type()
)
lgs2816crpsDhcpSnoopingClientIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsDhcpSnoopingClientIP.setStatus("current")
_Lgs2816crpsDhcpSnoopingClientLease_Type = DisplayString
_Lgs2816crpsDhcpSnoopingClientLease_Object = MibTableColumn
lgs2816crpsDhcpSnoopingClientLease = _Lgs2816crpsDhcpSnoopingClientLease_Object(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 26, 3, 1, 6),
    _Lgs2816crpsDhcpSnoopingClientLease_Type()
)
lgs2816crpsDhcpSnoopingClientLease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgs2816crpsDhcpSnoopingClientLease.setStatus("current")

# Managed Objects groups


# Notification objects

lgs2816crpsUserLogin = NotificationType(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 20, 1)
)
lgs2816crpsUserLogin.setObjects(
    ("PRIVATE-LGS2816CRPS-MIB", "username")
)
if mibBuilder.loadTexts:
    lgs2816crpsUserLogin.setStatus(
        "current"
    )

lgs2816crpsUserLogout = NotificationType(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 20, 2)
)
lgs2816crpsUserLogout.setObjects(
    ("PRIVATE-LGS2816CRPS-MIB", "username")
)
if mibBuilder.loadTexts:
    lgs2816crpsUserLogout.setStatus(
        "current"
    )

lgs2816crpsModuleInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 20, 3)
)
lgs2816crpsModuleInserted.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    lgs2816crpsModuleInserted.setStatus(
        "current"
    )

lgs2816crpsModuleRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 20, 4)
)
lgs2816crpsModuleRemoved.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    lgs2816crpsModuleRemoved.setStatus(
        "current"
    )

lgs2816crpsDualMediaSwapped = NotificationType(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 20, 5)
)
lgs2816crpsDualMediaSwapped.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("PRIVATE-LGS2816CRPS-MIB", "swapto"))
)
if mibBuilder.loadTexts:
    lgs2816crpsDualMediaSwapped.setStatus(
        "current"
    )

lgs2816crpsLoopDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 20, 6)
)
lgs2816crpsLoopDetected.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    lgs2816crpsLoopDetected.setStatus(
        "current"
    )

lgs2816crpsStpStateDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 20, 7)
)
if mibBuilder.loadTexts:
    lgs2816crpsStpStateDisabled.setStatus(
        "current"
    )

lgs2816crpsStpStateEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 20, 8)
)
if mibBuilder.loadTexts:
    lgs2816crpsStpStateEnabled.setStatus(
        "current"
    )

lgs2816crpsStpTopologyChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 20, 9)
)
lgs2816crpsStpTopologyChanged.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    lgs2816crpsStpTopologyChanged.setStatus(
        "current"
    )

lgs2816crpsLacpStateDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 20, 10)
)
lgs2816crpsLacpStateDisabled.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("PRIVATE-LGS2816CRPS-MIB", "groupId"))
)
if mibBuilder.loadTexts:
    lgs2816crpsLacpStateDisabled.setStatus(
        "current"
    )

lgs2816crpsLacpStateEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 20, 11)
)
lgs2816crpsLacpStateEnabled.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("PRIVATE-LGS2816CRPS-MIB", "groupId"))
)
if mibBuilder.loadTexts:
    lgs2816crpsLacpStateEnabled.setStatus(
        "current"
    )

lgs2816crpsLacpPortAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 20, 12)
)
lgs2816crpsLacpPortAdded.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("PRIVATE-LGS2816CRPS-MIB", "actorkey"),
        ("PRIVATE-LGS2816CRPS-MIB", "partnerkey"))
)
if mibBuilder.loadTexts:
    lgs2816crpsLacpPortAdded.setStatus(
        "current"
    )

lgs2816crpsLacpPortTrunkFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 20, 13)
)
lgs2816crpsLacpPortTrunkFailure.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("PRIVATE-LGS2816CRPS-MIB", "actorkey"),
        ("PRIVATE-LGS2816CRPS-MIB", "partnerkey"))
)
if mibBuilder.loadTexts:
    lgs2816crpsLacpPortTrunkFailure.setStatus(
        "current"
    )

lgs2816crpsGvrpStateDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 20, 14)
)
if mibBuilder.loadTexts:
    lgs2816crpsGvrpStateDisabled.setStatus(
        "current"
    )

lgs2816crpsGvrpStateEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 20, 15)
)
if mibBuilder.loadTexts:
    lgs2816crpsGvrpStateEnabled.setStatus(
        "current"
    )

lgs2816crpsVlanPortBaseEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 20, 17)
)
if mibBuilder.loadTexts:
    lgs2816crpsVlanPortBaseEnabled.setStatus(
        "current"
    )

lgs2816crpsVlanTagBaseEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 20, 18)
)
if mibBuilder.loadTexts:
    lgs2816crpsVlanTagBaseEnabled.setStatus(
        "current"
    )

lgs2816crpsIpmbStateEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 20, 19)
)
if mibBuilder.loadTexts:
    lgs2816crpsIpmbStateEnabled.setStatus(
        "current"
    )

lgs2816crpsIpmbStateDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 20, 20)
)
if mibBuilder.loadTexts:
    lgs2816crpsIpmbStateDisabled.setStatus(
        "current"
    )

lgs2816crpsIpmbEntryFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 20, 21)
)
lgs2816crpsIpmbEntryFailure.setObjects(
      *(("PRIVATE-LGS2816CRPS-MIB", "ipmacIp"),
        ("PRIVATE-LGS2816CRPS-MIB", "ipmacMac"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    lgs2816crpsIpmbEntryFailure.setStatus(
        "current"
    )

lgs2816crpsRP2000TempEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 20, 26)
)
lgs2816crpsRP2000TempEvent.setObjects(
      *(("PRIVATE-LGS2816CRPS-MIB", "rp2000eventstatus"),
        ("PRIVATE-LGS2816CRPS-MIB", "rp2000eventinfo"))
)
if mibBuilder.loadTexts:
    lgs2816crpsRP2000TempEvent.setStatus(
        "current"
    )

lgs2816crpsRP2000FanEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 20, 27)
)
lgs2816crpsRP2000FanEvent.setObjects(
      *(("PRIVATE-LGS2816CRPS-MIB", "rp2000eventstatus"),
        ("PRIVATE-LGS2816CRPS-MIB", "rp2000eventinfo"))
)
if mibBuilder.loadTexts:
    lgs2816crpsRP2000FanEvent.setStatus(
        "current"
    )

lgs2816crpsRP2000VoltEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 20, 28)
)
lgs2816crpsRP2000VoltEvent.setObjects(
      *(("PRIVATE-LGS2816CRPS-MIB", "rp2000eventstatus"),
        ("PRIVATE-LGS2816CRPS-MIB", "rp2000eventinfo"))
)
if mibBuilder.loadTexts:
    lgs2816crpsRP2000VoltEvent.setStatus(
        "current"
    )

lgs2816crpsRP2000PwrEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 37072, 2, 47, 1, 20, 29)
)
lgs2816crpsRP2000PwrEvent.setObjects(
      *(("PRIVATE-LGS2816CRPS-MIB", "rp2000eventstatus"),
        ("PRIVATE-LGS2816CRPS-MIB", "rp2000eventinfo"))
)
if mibBuilder.loadTexts:
    lgs2816crpsRP2000PwrEvent.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PRIVATE-LGS2816CRPS-MIB",
    **{"private": private,
       "switch": switch,
       "lgs2816crpsProductID": lgs2816crpsProductID,
       "lgs2816crpsProduces": lgs2816crpsProduces,
       "lgs2816crpsSystem": lgs2816crpsSystem,
       "lgs2816crpsCommonSys": lgs2816crpsCommonSys,
       "lgs2816crpsReboot": lgs2816crpsReboot,
       "lgs2816crpsBiosVsersion": lgs2816crpsBiosVsersion,
       "lgs2816crpsFirmwareVersion": lgs2816crpsFirmwareVersion,
       "lgs2816crpsHardwareVersion": lgs2816crpsHardwareVersion,
       "lgs2816crpsMechanicalVersion": lgs2816crpsMechanicalVersion,
       "lgs2816crpsSerialNumber": lgs2816crpsSerialNumber,
       "lgs2816crpsHostMacAddress": lgs2816crpsHostMacAddress,
       "lgs2816crpsDevicePort": lgs2816crpsDevicePort,
       "lgs2816crpsRamSize": lgs2816crpsRamSize,
       "lgs2816crpsFlashSize": lgs2816crpsFlashSize,
       "lgs2816crpsDeviceName": lgs2816crpsDeviceName,
       "lgs2816crpsSystemDescription": lgs2816crpsSystemDescription,
       "lgs2816crpsCpuLoad": lgs2816crpsCpuLoad,
       "lgs2816crpsIP": lgs2816crpsIP,
       "lgs2816crpsDhcpSetting": lgs2816crpsDhcpSetting,
       "lgs2816crpsIPAddress": lgs2816crpsIPAddress,
       "lgs2816crpsNetMask": lgs2816crpsNetMask,
       "lgs2816crpsDefaultGateway": lgs2816crpsDefaultGateway,
       "lgs2816crpsDnsConf": lgs2816crpsDnsConf,
       "lgs2816crpsDnsState": lgs2816crpsDnsState,
       "lgs2816crpsDnsServer": lgs2816crpsDnsServer,
       "lgs2816crpsTime": lgs2816crpsTime,
       "lgs2816crpsSystemCurrentTime": lgs2816crpsSystemCurrentTime,
       "lgs2816crpsManualTimeSetting": lgs2816crpsManualTimeSetting,
       "lgs2816crpsNTPServer": lgs2816crpsNTPServer,
       "lgs2816crpsNTPTimeZone": lgs2816crpsNTPTimeZone,
       "lgs2816crpsNTPTimeSync": lgs2816crpsNTPTimeSync,
       "lgs2816crpsDaylightSavingTime": lgs2816crpsDaylightSavingTime,
       "lgs2816crpsDaylightStartTime": lgs2816crpsDaylightStartTime,
       "lgs2816crpsDaylightEndTime": lgs2816crpsDaylightEndTime,
       "lgs2816crpsAccount": lgs2816crpsAccount,
       "lgs2816crpsAccountNumber": lgs2816crpsAccountNumber,
       "lgs2816crpsAccountTable": lgs2816crpsAccountTable,
       "lgs2816crpsAccountEntry": lgs2816crpsAccountEntry,
       "lgs2816crpsAccountIndex": lgs2816crpsAccountIndex,
       "lgs2816crpsAccountAuthorization": lgs2816crpsAccountAuthorization,
       "lgs2816crpsAccountName": lgs2816crpsAccountName,
       "lgs2816crpsAccountPassword": lgs2816crpsAccountPassword,
       "lgs2816crpsAccountAddAuthorization": lgs2816crpsAccountAddAuthorization,
       "lgs2816crpsAccountAddName": lgs2816crpsAccountAddName,
       "lgs2816crpsAccountAddPassword": lgs2816crpsAccountAddPassword,
       "lgs2816crpsDoAccountAdd": lgs2816crpsDoAccountAdd,
       "lgs2816crpsAccountDel": lgs2816crpsAccountDel,
       "lgs2816crpsVsm": lgs2816crpsVsm,
       "lgs2816crpsVsmState": lgs2816crpsVsmState,
       "lgs2816crpsVsmRole": lgs2816crpsVsmRole,
       "lgs2816crpsVsmGroupid": lgs2816crpsVsmGroupid,
       "lgs2816crpsExternalPower": lgs2816crpsExternalPower,
       "lgs2816crpsExternalPowerExist": lgs2816crpsExternalPowerExist,
       "lgs2816crpsExternalPowerInfo": lgs2816crpsExternalPowerInfo,
       "lgs2816crpsExternalPowerModel": lgs2816crpsExternalPowerModel,
       "lgs2816crpsExternalPowerHard": lgs2816crpsExternalPowerHard,
       "lgs2816crpsExternalPowerMech": lgs2816crpsExternalPowerMech,
       "lgs2816crpsExternalPowerSerial": lgs2816crpsExternalPowerSerial,
       "lgs2816crpsExternalPowerTemp": lgs2816crpsExternalPowerTemp,
       "lgs2816crpsExternalPowerFan": lgs2816crpsExternalPowerFan,
       "lgs2816crpsExternalPowerVoltage": lgs2816crpsExternalPowerVoltage,
       "lgs2816crpsExternalPowerModuleTable": lgs2816crpsExternalPowerModuleTable,
       "lgs2816crpsExternalPowerModuleEntry": lgs2816crpsExternalPowerModuleEntry,
       "lgs2816crpsPowerModuleIndex": lgs2816crpsPowerModuleIndex,
       "lgs2816crpsPowerModuleName": lgs2816crpsPowerModuleName,
       "lgs2816crpsPowerModuleType": lgs2816crpsPowerModuleType,
       "lgs2816crpsPowerModuleSerial": lgs2816crpsPowerModuleSerial,
       "lgs2816crpsPowerModuleHard": lgs2816crpsPowerModuleHard,
       "lgs2816crpsPowerModuleMech": lgs2816crpsPowerModuleMech,
       "lgs2816crpsPowerModuleVolt": lgs2816crpsPowerModuleVolt,
       "lgs2816crpsPowerModuleCurrent": lgs2816crpsPowerModuleCurrent,
       "lgs2816crpsPowerModuleMaxPwr": lgs2816crpsPowerModuleMaxPwr,
       "lgs2816crpsTrapHost": lgs2816crpsTrapHost,
       "lgs2816crpsTrapHostTable": lgs2816crpsTrapHostTable,
       "lgs2816crpsTrapHostEntry": lgs2816crpsTrapHostEntry,
       "lgs2816crpsTrapHostIndex": lgs2816crpsTrapHostIndex,
       "lgs2816crpsTrapHostVersion": lgs2816crpsTrapHostVersion,
       "lgs2816crpsTrapHostIP": lgs2816crpsTrapHostIP,
       "lgs2816crpsTrapHostPort": lgs2816crpsTrapHostPort,
       "lgs2816crpsTrapHostCommunity": lgs2816crpsTrapHostCommunity,
       "lgs2816crpsTrapHostSecurityLevel": lgs2816crpsTrapHostSecurityLevel,
       "lgs2816crpsTrapHostAuthPtc": lgs2816crpsTrapHostAuthPtc,
       "lgs2816crpsTrapHostAuthPassword": lgs2816crpsTrapHostAuthPassword,
       "lgs2816crpsTrapHostPrivPtc": lgs2816crpsTrapHostPrivPtc,
       "lgs2816crpsTrapHostPrivPassword": lgs2816crpsTrapHostPrivPassword,
       "lgs2816crpsTrapHostCurrentMode": lgs2816crpsTrapHostCurrentMode,
       "lgs2816crpsAlarm": lgs2816crpsAlarm,
       "lgs2816crpsEvent": lgs2816crpsEvent,
       "lgs2816crpsEventNumber": lgs2816crpsEventNumber,
       "lgs2816crpsEventTable": lgs2816crpsEventTable,
       "lgs2816crpsEventEntry": lgs2816crpsEventEntry,
       "lgs2816crpsEventIndex": lgs2816crpsEventIndex,
       "lgs2816crpsEventName": lgs2816crpsEventName,
       "lgs2816crpsEventSendEmail": lgs2816crpsEventSendEmail,
       "lgs2816crpsEventSendTrap": lgs2816crpsEventSendTrap,
       "lgs2816crpsEmail": lgs2816crpsEmail,
       "lgs2816crpsEmailServer": lgs2816crpsEmailServer,
       "lgs2816crpsEmailUsername": lgs2816crpsEmailUsername,
       "lgs2816crpsEmailPassword": lgs2816crpsEmailPassword,
       "lgs2816crpsEmailSender": lgs2816crpsEmailSender,
       "lgs2816crpsEmailReturnPath": lgs2816crpsEmailReturnPath,
       "lgs2816crpsEmailUserNumber": lgs2816crpsEmailUserNumber,
       "lgs2816crpsEmailUserTable": lgs2816crpsEmailUserTable,
       "lgs2816crpsEmailUserEntry": lgs2816crpsEmailUserEntry,
       "lgs2816crpsEmailUserIndex": lgs2816crpsEmailUserIndex,
       "lgs2816crpsEmailUserAddress": lgs2816crpsEmailUserAddress,
       "lgs2816crpsConfiguration": lgs2816crpsConfiguration,
       "lgs2816crpsSaveRestore": lgs2816crpsSaveRestore,
       "lgs2816crpsSaveStart": lgs2816crpsSaveStart,
       "lgs2816crpsSaveUser": lgs2816crpsSaveUser,
       "lgs2816crpsRestoreDefault": lgs2816crpsRestoreDefault,
       "lgs2816crpsRestoreUser": lgs2816crpsRestoreUser,
       "lgs2816crpsConfigFile": lgs2816crpsConfigFile,
       "lgs2816crpsExportIpAddress": lgs2816crpsExportIpAddress,
       "lgs2816crpsDoExportConfig": lgs2816crpsDoExportConfig,
       "lgs2816crpsImportIpAddress": lgs2816crpsImportIpAddress,
       "lgs2816crpsImportConfigName": lgs2816crpsImportConfigName,
       "lgs2816crpsDoImportConfig": lgs2816crpsDoImportConfig,
       "lgs2816crpsLog": lgs2816crpsLog,
       "lgs2816crpsClearLog": lgs2816crpsClearLog,
       "lgs2816crpsLogNumber": lgs2816crpsLogNumber,
       "lgs2816crpsLogTable": lgs2816crpsLogTable,
       "lgs2816crpsLogEntry": lgs2816crpsLogEntry,
       "lgs2816crpsLogIndex": lgs2816crpsLogIndex,
       "lgs2816crpsLogEvent": lgs2816crpsLogEvent,
       "lgs2816crpsFirmware": lgs2816crpsFirmware,
       "lgs2816crpsFirmwareIpAddress": lgs2816crpsFirmwareIpAddress,
       "lgs2816crpsFirmwareFileName": lgs2816crpsFirmwareFileName,
       "lgs2816crpsDoFirmwareUpgrade": lgs2816crpsDoFirmwareUpgrade,
       "lgs2816crpsPort": lgs2816crpsPort,
       "lgs2816crpsPortStatus": lgs2816crpsPortStatus,
       "lgs2816crpsPortStatusNumber": lgs2816crpsPortStatusNumber,
       "lgs2816crpsPortStatusTable": lgs2816crpsPortStatusTable,
       "lgs2816crpsPortStatusEntry": lgs2816crpsPortStatusEntry,
       "lgs2816crpsPortStatusIndex": lgs2816crpsPortStatusIndex,
       "lgs2816crpsPortStatusMedia": lgs2816crpsPortStatusMedia,
       "lgs2816crpsPortStatusPortState": lgs2816crpsPortStatusPortState,
       "lgs2816crpsPortStatusLink": lgs2816crpsPortStatusLink,
       "lgs2816crpsPortStatusAutoNego": lgs2816crpsPortStatusAutoNego,
       "lgs2816crpsPortStatusSpdDpx": lgs2816crpsPortStatusSpdDpx,
       "lgs2816crpsPortStatusFlwCtrlRx": lgs2816crpsPortStatusFlwCtrlRx,
       "lgs2816crpsPortStatusFlwCtrlTx": lgs2816crpsPortStatusFlwCtrlTx,
       "lgs2816crpsPortStatuDescription": lgs2816crpsPortStatuDescription,
       "lgs2816crpsPortConf": lgs2816crpsPortConf,
       "lgs2816crpsPortConfNumber": lgs2816crpsPortConfNumber,
       "lgs2816crpsPortConfTable": lgs2816crpsPortConfTable,
       "lgs2816crpsPortConfEntry": lgs2816crpsPortConfEntry,
       "lgs2816crpsPortConfIndex": lgs2816crpsPortConfIndex,
       "lgs2816crpsPortConfPortState": lgs2816crpsPortConfPortState,
       "lgs2816crpsPortConfTPSpdDpx": lgs2816crpsPortConfTPSpdDpx,
       "lgs2816crpsPortConfSFPSpdDpx": lgs2816crpsPortConfSFPSpdDpx,
       "lgs2816crpsPortConfFlwCtrl": lgs2816crpsPortConfFlwCtrl,
       "lgs2816crpsPortConfExcessiveCollisionMode": lgs2816crpsPortConfExcessiveCollisionMode,
       "lgs2816crpsPortConfDescription": lgs2816crpsPortConfDescription,
       "lgs2816crpsPortConfPowerSaving": lgs2816crpsPortConfPowerSaving,
       "lgs2816crpsSFPInfo": lgs2816crpsSFPInfo,
       "lgs2816crpsSFPInfoNumber": lgs2816crpsSFPInfoNumber,
       "lgs2816crpsSFPInfoTable": lgs2816crpsSFPInfoTable,
       "lgs2816crpsSFPInfoEntry": lgs2816crpsSFPInfoEntry,
       "lgs2816crpsSFPInfoIndex": lgs2816crpsSFPInfoIndex,
       "lgs2816crpsSFPConnectorType": lgs2816crpsSFPConnectorType,
       "lgs2816crpsSFPFiberType": lgs2816crpsSFPFiberType,
       "lgs2816crpsSFPWavelength": lgs2816crpsSFPWavelength,
       "lgs2816crpsSFPBaudRate": lgs2816crpsSFPBaudRate,
       "lgs2816crpsSFPVendorOUI": lgs2816crpsSFPVendorOUI,
       "lgs2816crpsSFPVendorName": lgs2816crpsSFPVendorName,
       "lgs2816crpsSFPVendorPN": lgs2816crpsSFPVendorPN,
       "lgs2816crpsSFPVendorRev": lgs2816crpsSFPVendorRev,
       "lgs2816crpsSFPVendorSN": lgs2816crpsSFPVendorSN,
       "lgs2816crpsSFPDateCode": lgs2816crpsSFPDateCode,
       "lgs2816crpsSFPTemperature": lgs2816crpsSFPTemperature,
       "lgs2816crpsSFPVcc": lgs2816crpsSFPVcc,
       "lgs2816crpsSFPTxBias": lgs2816crpsSFPTxBias,
       "lgs2816crpsSFPTxPWR": lgs2816crpsSFPTxPWR,
       "lgs2816crpsSFPRxPWR": lgs2816crpsSFPRxPWR,
       "lgs2816crpsMirror": lgs2816crpsMirror,
       "lgs2816crpsMirroringPort": lgs2816crpsMirroringPort,
       "lgs2816crpsMirroredPortsTable": lgs2816crpsMirroredPortsTable,
       "lgs2816crpsMirroredPortsEntry": lgs2816crpsMirroredPortsEntry,
       "lgs2816crpsMirroredPortIndex": lgs2816crpsMirroredPortIndex,
       "lgs2816crpsMirroredPortSrouceEnable": lgs2816crpsMirroredPortSrouceEnable,
       "lgs2816crpsMirroredPortDestinationEnable": lgs2816crpsMirroredPortDestinationEnable,
       "lgs2816crpsMaxPktLen": lgs2816crpsMaxPktLen,
       "lgs2816crpsMaxPktLenPortNumber": lgs2816crpsMaxPktLenPortNumber,
       "lgs2816crpsMaxPktLenConfTable": lgs2816crpsMaxPktLenConfTable,
       "lgs2816crpsMaxPktLenConfEntry": lgs2816crpsMaxPktLenConfEntry,
       "lgs2816crpsMaxPktLenConfIndex": lgs2816crpsMaxPktLenConfIndex,
       "lgs2816crpsMaxPktLenConfSetting": lgs2816crpsMaxPktLenConfSetting,
       "lgs2816crpsLoopDetectedConf": lgs2816crpsLoopDetectedConf,
       "lgs2816crpsLoopDetectedNumber": lgs2816crpsLoopDetectedNumber,
       "lgs2816crpsLoopDetectedTable": lgs2816crpsLoopDetectedTable,
       "lgs2816crpsLoopDetectedEntry": lgs2816crpsLoopDetectedEntry,
       "lgs2816crpsLoopDetectedfIndex": lgs2816crpsLoopDetectedfIndex,
       "lgs2816crpsLoopDetectedPort": lgs2816crpsLoopDetectedPort,
       "lgs2816crpsLoopDetectedLockedPort": lgs2816crpsLoopDetectedLockedPort,
       "lgs2816crpsManagementPolicy": lgs2816crpsManagementPolicy,
       "lgs2816crpsManagementSecurityNumber": lgs2816crpsManagementSecurityNumber,
       "lgs2816crpsManagementSecurityEntryCreate": lgs2816crpsManagementSecurityEntryCreate,
       "lgs2816crpsManagementSecurityTable": lgs2816crpsManagementSecurityTable,
       "lgs2816crpsManagementSecurityEntry": lgs2816crpsManagementSecurityEntry,
       "lgs2816crpsManagementSecurityIndex": lgs2816crpsManagementSecurityIndex,
       "lgs2816crpsManagementSecurityName": lgs2816crpsManagementSecurityName,
       "lgs2816crpsManagementSecurityIpRange": lgs2816crpsManagementSecurityIpRange,
       "lgs2816crpsManagementSecurityIncomigPort": lgs2816crpsManagementSecurityIncomigPort,
       "lgs2816crpsManagementSecurityAccessType": lgs2816crpsManagementSecurityAccessType,
       "lgs2816crpsManagementSecurityAction": lgs2816crpsManagementSecurityAction,
       "lgs2816crpsManagementSecurityEntryAction": lgs2816crpsManagementSecurityEntryAction,
       "lgs2816crpsVLAN": lgs2816crpsVLAN,
       "lgs2816crpsVlanConf": lgs2816crpsVlanConf,
       "lgs2816crpsVlanMode": lgs2816crpsVlanMode,
       "lgs2816crpsManagementVlan": lgs2816crpsManagementVlan,
       "lgs2816crpsPortIsolation": lgs2816crpsPortIsolation,
       "lgs2816crpsTagIdentifier": lgs2816crpsTagIdentifier,
       "lgs2816crpsTagBaseVlanGroup": lgs2816crpsTagBaseVlanGroup,
       "lgs2816crpsTagBaseVlanNumber": lgs2816crpsTagBaseVlanNumber,
       "lgs2816crpsTagBaseVlanGroupEntryCreate": lgs2816crpsTagBaseVlanGroupEntryCreate,
       "lgs2816crpsTagBaseVlanGroupTable": lgs2816crpsTagBaseVlanGroupTable,
       "lgs2816crpsTagBaseVlanGroupEntry": lgs2816crpsTagBaseVlanGroupEntry,
       "lgs2816crpsTagBaseVlanVid": lgs2816crpsTagBaseVlanVid,
       "lgs2816crpsTagBaseVlanName": lgs2816crpsTagBaseVlanName,
       "lgs2816crpsTagBaseVlanIgmpProxy": lgs2816crpsTagBaseVlanIgmpProxy,
       "lgs2816crpsTagBaseVlanPrivateVlan": lgs2816crpsTagBaseVlanPrivateVlan,
       "lgs2816crpsTagBaseVlanGvrp": lgs2816crpsTagBaseVlanGvrp,
       "lgs2816crpsTagBaseVlanMemberPort": lgs2816crpsTagBaseVlanMemberPort,
       "lgs2816crpsTagBaseVlanEntryAction": lgs2816crpsTagBaseVlanEntryAction,
       "lgs2816crpsVlanPortConfTable": lgs2816crpsVlanPortConfTable,
       "lgs2816crpsVlanPortConfEntry": lgs2816crpsVlanPortConfEntry,
       "lgs2816crpsVlanPortConfIndex": lgs2816crpsVlanPortConfIndex,
       "lgs2816crpsVlanPortConfVlanAware": lgs2816crpsVlanPortConfVlanAware,
       "lgs2816crpsVlanPortConfIngressFiltering": lgs2816crpsVlanPortConfIngressFiltering,
       "lgs2816crpsVlanPortConfFrameType": lgs2816crpsVlanPortConfFrameType,
       "lgs2816crpsVlanPortConfPvid": lgs2816crpsVlanPortConfPvid,
       "lgs2816crpsVlanPortConfRole": lgs2816crpsVlanPortConfRole,
       "lgs2816crpsVlanPortConfUntagVid": lgs2816crpsVlanPortConfUntagVid,
       "lgs2816crpsVlanPortConfDoubleTag": lgs2816crpsVlanPortConfDoubleTag,
       "lgs2816crpsPortBaseVlanGroup": lgs2816crpsPortBaseVlanGroup,
       "lgs2816crpsPortBaseVlanNumber": lgs2816crpsPortBaseVlanNumber,
       "lgs2816crpsPortBaseVlanGroupEntryCreate": lgs2816crpsPortBaseVlanGroupEntryCreate,
       "lgs2816crpsPortBaseVlanGroupTable": lgs2816crpsPortBaseVlanGroupTable,
       "lgs2816crpsPortBaseVlanGroupEntry": lgs2816crpsPortBaseVlanGroupEntry,
       "lgs2816crpsPortBaseVlanGroupIndex": lgs2816crpsPortBaseVlanGroupIndex,
       "lgs2816crpsPortBaseVlanGroupName": lgs2816crpsPortBaseVlanGroupName,
       "lgs2816crpsPortBaseVlanGroupMembers": lgs2816crpsPortBaseVlanGroupMembers,
       "lgs2816crpsPortBaseVlanGroupEntryAction": lgs2816crpsPortBaseVlanGroupEntryAction,
       "lgs2816crpsMacTableInfo": lgs2816crpsMacTableInfo,
       "lgs2816crpsMacTableConf": lgs2816crpsMacTableConf,
       "lgs2816crpsMacAgeTime": lgs2816crpsMacAgeTime,
       "lgs2816crpsMacTableLearningConfTable": lgs2816crpsMacTableLearningConfTable,
       "lgs2816crpsMacTableLearningConfEntry": lgs2816crpsMacTableLearningConfEntry,
       "lgs2816crpsMacTableLearningConfIndex": lgs2816crpsMacTableLearningConfIndex,
       "lgs2816crpsMacTableLearningConfstate": lgs2816crpsMacTableLearningConfstate,
       "lgs2816crpsMacTableStaticFilter": lgs2816crpsMacTableStaticFilter,
       "lgs2816crpsMacTableStaticFilterNumber": lgs2816crpsMacTableStaticFilterNumber,
       "lgs2816crpsMacTableStaticFilterEntryCreate": lgs2816crpsMacTableStaticFilterEntryCreate,
       "lgs2816crpsMacTableStaticFilterTable": lgs2816crpsMacTableStaticFilterTable,
       "lgs2816crpsMacTableStaticFilterEntry": lgs2816crpsMacTableStaticFilterEntry,
       "lgs2816crpsMacTableStaticFilterIndex": lgs2816crpsMacTableStaticFilterIndex,
       "lgs2816crpsMacTableStaticFilterMac": lgs2816crpsMacTableStaticFilterMac,
       "lgs2816crpsMacTableStaticFilterVid": lgs2816crpsMacTableStaticFilterVid,
       "lgs2816crpsMacTableStaticFilterAlias": lgs2816crpsMacTableStaticFilterAlias,
       "lgs2816crpsMacTableStaticFilterEntryAction": lgs2816crpsMacTableStaticFilterEntryAction,
       "lgs2816crpsMacTableStaticForward": lgs2816crpsMacTableStaticForward,
       "lgs2816crpsMacTableStaticForwardNumber": lgs2816crpsMacTableStaticForwardNumber,
       "lgs2816crpsMacTableStaticForwardEntryCreate": lgs2816crpsMacTableStaticForwardEntryCreate,
       "lgs2816crpsMacTableStaticForwardTable": lgs2816crpsMacTableStaticForwardTable,
       "lgs2816crpsMacTableStaticForwardEntry": lgs2816crpsMacTableStaticForwardEntry,
       "lgs2816crpsMacTableStaticForwardIndex": lgs2816crpsMacTableStaticForwardIndex,
       "lgs2816crpsMacTableStaticForwardMac": lgs2816crpsMacTableStaticForwardMac,
       "lgs2816crpsMacTableStaticForwardPort": lgs2816crpsMacTableStaticForwardPort,
       "lgs2816crpsMacTableStaticForwardVid": lgs2816crpsMacTableStaticForwardVid,
       "lgs2816crpsMacTableStaticForwardAlias": lgs2816crpsMacTableStaticForwardAlias,
       "lgs2816crpsMacTableStaticForwardEntryAction": lgs2816crpsMacTableStaticForwardEntryAction,
       "lgs2816crpsMacAlias": lgs2816crpsMacAlias,
       "lgs2816crpsMacAliasNumber": lgs2816crpsMacAliasNumber,
       "lgs2816crpsMacAliasEntryCreate": lgs2816crpsMacAliasEntryCreate,
       "lgs2816crpsMacAliasTable": lgs2816crpsMacAliasTable,
       "lgs2816crpsMacAliasEntry": lgs2816crpsMacAliasEntry,
       "lgs2816crpsMacAliasIndex": lgs2816crpsMacAliasIndex,
       "lgs2816crpsAliasMac": lgs2816crpsAliasMac,
       "lgs2816crpsAliasName": lgs2816crpsAliasName,
       "lgs2816crpsMacAliasEntryAction": lgs2816crpsMacAliasEntryAction,
       "lgs2816crpsGVRPInfo": lgs2816crpsGVRPInfo,
       "lgs2816crpsGvrpConf": lgs2816crpsGvrpConf,
       "lgs2816crpsGvrpConfState": lgs2816crpsGvrpConfState,
       "lgs2816crpsGvrpConfTable": lgs2816crpsGvrpConfTable,
       "lgs2816crpsGvrpConfEntry": lgs2816crpsGvrpConfEntry,
       "lgs2816crpsGvrpConfIndex": lgs2816crpsGvrpConfIndex,
       "lgs2816crpsGvrpConfJoinTime": lgs2816crpsGvrpConfJoinTime,
       "lgs2816crpsGvrpConfLeaveTime": lgs2816crpsGvrpConfLeaveTime,
       "lgs2816crpsGvrpConfLeaveAllTime": lgs2816crpsGvrpConfLeaveAllTime,
       "lgs2816crpsGvrpConfDefaultAppMode": lgs2816crpsGvrpConfDefaultAppMode,
       "lgs2816crpsGvrpConfDefaultRegMode": lgs2816crpsGvrpConfDefaultRegMode,
       "lgs2816crpsGvrpConfRestrictedMode": lgs2816crpsGvrpConfRestrictedMode,
       "lgs2816crpsGvrpCounter": lgs2816crpsGvrpCounter,
       "lgs2816crpsGvrpCounterTable": lgs2816crpsGvrpCounterTable,
       "lgs2816crpsGvrpCounterEntry": lgs2816crpsGvrpCounterEntry,
       "lgs2816crpsGvrpCounterIndex": lgs2816crpsGvrpCounterIndex,
       "lgs2816crpsGvrpCounterRxTotalGvrpPkts": lgs2816crpsGvrpCounterRxTotalGvrpPkts,
       "lgs2816crpsGvrpCounterRxInvalidGvrpPkts": lgs2816crpsGvrpCounterRxInvalidGvrpPkts,
       "lgs2816crpsGvrpCounterRxLeaveAllMsg": lgs2816crpsGvrpCounterRxLeaveAllMsg,
       "lgs2816crpsGvrpCounterRxJoinEmptyMsg": lgs2816crpsGvrpCounterRxJoinEmptyMsg,
       "lgs2816crpsGvrpCounterRxJoinInMsg": lgs2816crpsGvrpCounterRxJoinInMsg,
       "lgs2816crpsGvrpCounterRxLeaveEmptyMsg": lgs2816crpsGvrpCounterRxLeaveEmptyMsg,
       "lgs2816crpsGvrpCounterRxEmptyMsg": lgs2816crpsGvrpCounterRxEmptyMsg,
       "lgs2816crpsGvrpCounterTxTotalGvrpPkts": lgs2816crpsGvrpCounterTxTotalGvrpPkts,
       "lgs2816crpsGvrpCounterTxLeaveAllMsg": lgs2816crpsGvrpCounterTxLeaveAllMsg,
       "lgs2816crpsGvrpCounterTxJoinEmptyMsg": lgs2816crpsGvrpCounterTxJoinEmptyMsg,
       "lgs2816crpsGvrpCounterTxJoinInMsg": lgs2816crpsGvrpCounterTxJoinInMsg,
       "lgs2816crpsGvrpCounterTxLeaveEmptyMsg": lgs2816crpsGvrpCounterTxLeaveEmptyMsg,
       "lgs2816crpsGvrpCounterTxEmptyMsg": lgs2816crpsGvrpCounterTxEmptyMsg,
       "lgs2816crpsGvrpGroup": lgs2816crpsGvrpGroup,
       "lgs2816crpsGvrpGroupNumber": lgs2816crpsGvrpGroupNumber,
       "lgs2816crpsGvrpGroupTable": lgs2816crpsGvrpGroupTable,
       "lgs2816crpsGvrpGroupEntry": lgs2816crpsGvrpGroupEntry,
       "lgs2816crpsGvrpGroupId": lgs2816crpsGvrpGroupId,
       "lgs2816crpsGvrpGroupVid": lgs2816crpsGvrpGroupVid,
       "lgs2816crpsGvrpGroupMemberPort": lgs2816crpsGvrpGroupMemberPort,
       "lgs2816crpsGvrpGroupAdministrativeCtrlTable": lgs2816crpsGvrpGroupAdministrativeCtrlTable,
       "lgs2816crpsGvrpGroupAdministrativeCtrlEntry": lgs2816crpsGvrpGroupAdministrativeCtrlEntry,
       "lgs2816crpsGvrpGroupAdministrativeCtrlVid": lgs2816crpsGvrpGroupAdministrativeCtrlVid,
       "lgs2816crpsGvrpGroupAdministrativeCtrlPort": lgs2816crpsGvrpGroupAdministrativeCtrlPort,
       "lgs2816crpsGvrpGroupAdministrativeCtrlApp": lgs2816crpsGvrpGroupAdministrativeCtrlApp,
       "lgs2816crpsGvrpGroupAdministrativeCtrlReg": lgs2816crpsGvrpGroupAdministrativeCtrlReg,
       "lgs2816crpsQosInfo": lgs2816crpsQosInfo,
       "lgs2816crpsQosPortConf": lgs2816crpsQosPortConf,
       "lgs2816crpsQosNumOfClasses": lgs2816crpsQosNumOfClasses,
       "lgs2816crpsQosPortConfTable": lgs2816crpsQosPortConfTable,
       "lgs2816crpsQosPortConfEntry": lgs2816crpsQosPortConfEntry,
       "lgs2816crpsQosPortConfIndex": lgs2816crpsQosPortConfIndex,
       "lgs2816crpsQosPortConfDefaultClasses": lgs2816crpsQosPortConfDefaultClasses,
       "lgs2816crpsQosPortConfQCL": lgs2816crpsQosPortConfQCL,
       "lgs2816crpsQosPortConfUserPriority": lgs2816crpsQosPortConfUserPriority,
       "lgs2816crpsQosPortConfQueuingMode": lgs2816crpsQosPortConfQueuingMode,
       "lgs2816crpsQosPortConfQueueWeightedLow": lgs2816crpsQosPortConfQueueWeightedLow,
       "lgs2816crpsQosPortConfQueueWeightedNormal": lgs2816crpsQosPortConfQueueWeightedNormal,
       "lgs2816crpsQosPortConfQueueWeightedMedium": lgs2816crpsQosPortConfQueueWeightedMedium,
       "lgs2816crpsQosPortConfQueueWeightedHigh": lgs2816crpsQosPortConfQueueWeightedHigh,
       "lgs2816crpsQosRateLimiters": lgs2816crpsQosRateLimiters,
       "lgs2816crpsQosRateLimitersTable": lgs2816crpsQosRateLimitersTable,
       "lgs2816crpsQosRateLimitersEntry": lgs2816crpsQosRateLimitersEntry,
       "lgs2816crpsQosRateLimitersIndex": lgs2816crpsQosRateLimitersIndex,
       "lgs2816crpsQosRateLimitersPolicer": lgs2816crpsQosRateLimitersPolicer,
       "lgs2816crpsQosRateLimitersPolicerRate": lgs2816crpsQosRateLimitersPolicerRate,
       "lgs2816crpsQosRateLimitersShaper": lgs2816crpsQosRateLimitersShaper,
       "lgs2816crpsQosRateLimitersShaperRate": lgs2816crpsQosRateLimitersShaperRate,
       "lgs2816crpsQosStormCtrl": lgs2816crpsQosStormCtrl,
       "lgs2816crpsQosStromCtrlFloodedUnicastStatus": lgs2816crpsQosStromCtrlFloodedUnicastStatus,
       "lgs2816crpsQosStromCtrlFloodedUnicastRate": lgs2816crpsQosStromCtrlFloodedUnicastRate,
       "lgs2816crpsQosStromCtrlMulticastStatus": lgs2816crpsQosStromCtrlMulticastStatus,
       "lgs2816crpsQosStromCtrlMulticastRate": lgs2816crpsQosStromCtrlMulticastRate,
       "lgs2816crpsQosStromCtrlBroadcastStatus": lgs2816crpsQosStromCtrlBroadcastStatus,
       "lgs2816crpsQosStromCtrlBroadcastRate": lgs2816crpsQosStromCtrlBroadcastRate,
       "lgs2816crpsQosQCL": lgs2816crpsQosQCL,
       "lgs2816crpsQosQclCreate": lgs2816crpsQosQclCreate,
       "lgs2816crpsQosQclTable": lgs2816crpsQosQclTable,
       "lgs2816crpsQosQclEntry": lgs2816crpsQosQclEntry,
       "lgs2816crpsQosQclNo": lgs2816crpsQosQclNo,
       "lgs2816crpsQosQclQceListNo": lgs2816crpsQosQclQceListNo,
       "lgs2816crpsQosQclQceMoveTo": lgs2816crpsQosQclQceMoveTo,
       "lgs2816crpsQosQclQceType": lgs2816crpsQosQclQceType,
       "lgs2816crpsQosQclQceValue": lgs2816crpsQosQclQceValue,
       "lgs2816crpsQosQclQceTrafficClass": lgs2816crpsQosQclQceTrafficClass,
       "lgs2816crpsQosQclQcePriority0Class": lgs2816crpsQosQclQcePriority0Class,
       "lgs2816crpsQosQclQcePriority1Class": lgs2816crpsQosQclQcePriority1Class,
       "lgs2816crpsQosQclQcePriority2Class": lgs2816crpsQosQclQcePriority2Class,
       "lgs2816crpsQosQclQcePriority3Class": lgs2816crpsQosQclQcePriority3Class,
       "lgs2816crpsQosQclQcePriority4Class": lgs2816crpsQosQclQcePriority4Class,
       "lgs2816crpsQosQclQcePriority5Class": lgs2816crpsQosQclQcePriority5Class,
       "lgs2816crpsQosQclQcePriority6Class": lgs2816crpsQosQclQcePriority6Class,
       "lgs2816crpsQosQclQcePriority7Class": lgs2816crpsQosQclQcePriority7Class,
       "lgs2816crpsQosQclQceEntryAction": lgs2816crpsQosQclQceEntryAction,
       "lgs2816crpsAclInfo": lgs2816crpsAclInfo,
       "lgs2816crpsAclPortsConfTable": lgs2816crpsAclPortsConfTable,
       "lgs2816crpsAclPortsConfEntry": lgs2816crpsAclPortsConfEntry,
       "lgs2816crpsAclPortsConfIndex": lgs2816crpsAclPortsConfIndex,
       "lgs2816crpsAclPortsConfPolicyId": lgs2816crpsAclPortsConfPolicyId,
       "lgs2816crpsAclPortsConfAction": lgs2816crpsAclPortsConfAction,
       "lgs2816crpsAclPortsConfRateLimiterId": lgs2816crpsAclPortsConfRateLimiterId,
       "lgs2816crpsAclPortsConfPortCopy": lgs2816crpsAclPortsConfPortCopy,
       "lgs2816crpsAclPortsConfCounter": lgs2816crpsAclPortsConfCounter,
       "lgs2816crpsAclRateLimiter": lgs2816crpsAclRateLimiter,
       "lgs2816crpsAclRateLimiterTable": lgs2816crpsAclRateLimiterTable,
       "lgs2816crpsAclRateLimiterEntry": lgs2816crpsAclRateLimiterEntry,
       "lgs2816crpsAclRateLimiterIndex": lgs2816crpsAclRateLimiterIndex,
       "lgs2816crpsAclRateLimiterRate": lgs2816crpsAclRateLimiterRate,
       "lgs2816crpsAclInfoViewTable": lgs2816crpsAclInfoViewTable,
       "lgs2816crpsAclInfoViewEntry": lgs2816crpsAclInfoViewEntry,
       "lgs2816crpsAclInfoViewNo": lgs2816crpsAclInfoViewNo,
       "lgs2816crpsAceIngressPort": lgs2816crpsAceIngressPort,
       "lgs2816crpsAceFrameType": lgs2816crpsAceFrameType,
       "lgs2816crpsAceAction": lgs2816crpsAceAction,
       "lgs2816crpsAceRateLimiter": lgs2816crpsAceRateLimiter,
       "lgs2816crpsAcePortCopy": lgs2816crpsAcePortCopy,
       "lgs2816crpsAceCounter": lgs2816crpsAceCounter,
       "lgs2816crpsSmacFilter": lgs2816crpsSmacFilter,
       "lgs2816crpsDmacFilter": lgs2816crpsDmacFilter,
       "lgs2816crpsVlanIdFilter": lgs2816crpsVlanIdFilter,
       "lgs2816crpsVlanTagPriority": lgs2816crpsVlanTagPriority,
       "lgs2816crpsEtherTypeFilter": lgs2816crpsEtherTypeFilter,
       "lgs2816crpsArpRarp": lgs2816crpsArpRarp,
       "lgs2816crpsArpRequestReply": lgs2816crpsArpRequestReply,
       "lgs2816crpsArpSenderIpFilter": lgs2816crpsArpSenderIpFilter,
       "lgs2816crpsArpSenderIpAddress": lgs2816crpsArpSenderIpAddress,
       "lgs2816crpsArpSenderIpMask": lgs2816crpsArpSenderIpMask,
       "lgs2816crpsArpTargetIpFilter": lgs2816crpsArpTargetIpFilter,
       "lgs2816crpsArpTargetIpAddress": lgs2816crpsArpTargetIpAddress,
       "lgs2816crpsArpTargetIpMask": lgs2816crpsArpTargetIpMask,
       "lgs2816crpsArpSmacMatch": lgs2816crpsArpSmacMatch,
       "lgs2816crpsArpRarpDmacMatch": lgs2816crpsArpRarpDmacMatch,
       "lgs2816crpsArpIpEthernetLength": lgs2816crpsArpIpEthernetLength,
       "lgs2816crpsArpIp": lgs2816crpsArpIp,
       "lgs2816crpsArpEthernet": lgs2816crpsArpEthernet,
       "lgs2816crpsIpProtocolFilter": lgs2816crpsIpProtocolFilter,
       "lgs2816crpsIpProtocolValue": lgs2816crpsIpProtocolValue,
       "lgs2816crpsIpTTL": lgs2816crpsIpTTL,
       "lgs2816crpsIpFragment": lgs2816crpsIpFragment,
       "lgs2816crpsIpOption": lgs2816crpsIpOption,
       "lgs2816crpsSipFilter": lgs2816crpsSipFilter,
       "lgs2816crpsSipAddress": lgs2816crpsSipAddress,
       "lgs2816crpsSipMask": lgs2816crpsSipMask,
       "lgs2816crpsDipFilter": lgs2816crpsDipFilter,
       "lgs2816crpsDipAddress": lgs2816crpsDipAddress,
       "lgs2816crpsDipMask": lgs2816crpsDipMask,
       "lgs2816crpsIcmpTypeFilter": lgs2816crpsIcmpTypeFilter,
       "lgs2816crpsIcmpCodeFilter": lgs2816crpsIcmpCodeFilter,
       "lgs2816crpsUdpSourcePortFilter": lgs2816crpsUdpSourcePortFilter,
       "lgs2816crpsUdpDestPortFilter": lgs2816crpsUdpDestPortFilter,
       "lgs2816crpsTcpSourcePortFilter": lgs2816crpsTcpSourcePortFilter,
       "lgs2816crpsTcpDestPortFilter": lgs2816crpsTcpDestPortFilter,
       "lgs2816crpsTcpFIN": lgs2816crpsTcpFIN,
       "lgs2816crpsTcpSYN": lgs2816crpsTcpSYN,
       "lgs2816crpsTcpRST": lgs2816crpsTcpRST,
       "lgs2816crpsTcpPSH": lgs2816crpsTcpPSH,
       "lgs2816crpsTcpACK": lgs2816crpsTcpACK,
       "lgs2816crpsTcpURG": lgs2816crpsTcpURG,
       "lgs2816crpsAclInfoEntryAction": lgs2816crpsAclInfoEntryAction,
       "lgs2816crpsAclInfoConf": lgs2816crpsAclInfoConf,
       "lgs2816crpsAceNo": lgs2816crpsAceNo,
       "lgs2816crpsAceMoveTo": lgs2816crpsAceMoveTo,
       "lgs2816crpsAceIngressPortConf": lgs2816crpsAceIngressPortConf,
       "lgs2816crpsAceFrameTypeConf": lgs2816crpsAceFrameTypeConf,
       "lgs2816crpsAceFrameTypeParameters": lgs2816crpsAceFrameTypeParameters,
       "lgs2816crpsEthernetTypeFilter": lgs2816crpsEthernetTypeFilter,
       "lgs2816crpsAclArpParameters": lgs2816crpsAclArpParameters,
       "lgs2816crpsAceArpRarp": lgs2816crpsAceArpRarp,
       "lgs2816crpsAceArpRequestReply": lgs2816crpsAceArpRequestReply,
       "lgs2816crpsAceArpSenderIpFilter": lgs2816crpsAceArpSenderIpFilter,
       "lgs2816crpsAceArpSenderIpAddress": lgs2816crpsAceArpSenderIpAddress,
       "lgs2816crpsAceArpSenderIpMask": lgs2816crpsAceArpSenderIpMask,
       "lgs2816crpsAceArpTargetIpFilter": lgs2816crpsAceArpTargetIpFilter,
       "lgs2816crpsAceArpTargetIpAddress": lgs2816crpsAceArpTargetIpAddress,
       "lgs2816crpsAceArpTargetIpMask": lgs2816crpsAceArpTargetIpMask,
       "lgs2816crpsAceArpSmacMatch": lgs2816crpsAceArpSmacMatch,
       "lgs2816crpsAceArpRarpDmacMatch": lgs2816crpsAceArpRarpDmacMatch,
       "lgs2816crpsAceArpIpEthernetLength": lgs2816crpsAceArpIpEthernetLength,
       "lgs2816crpsAceArpIp": lgs2816crpsAceArpIp,
       "lgs2816crpsAceArpEthernet": lgs2816crpsAceArpEthernet,
       "lgs2816crpsAclIpParameters": lgs2816crpsAclIpParameters,
       "lgs2816crpsAceIpProtocolFilter": lgs2816crpsAceIpProtocolFilter,
       "lgs2816crpsAceIpProtocolFilterParameters": lgs2816crpsAceIpProtocolFilterParameters,
       "lgs2816crpsAceIcmpParameters": lgs2816crpsAceIcmpParameters,
       "lgs2816crpsAceIcmpTypeFilter": lgs2816crpsAceIcmpTypeFilter,
       "lgs2816crpsAceIcmpCodeFilter": lgs2816crpsAceIcmpCodeFilter,
       "lgs2816crpsAceUdpParameters": lgs2816crpsAceUdpParameters,
       "lgs2816crpsUdpSourcePortFilterConf": lgs2816crpsUdpSourcePortFilterConf,
       "lgs2816crpsUdpDestPortFilterConf": lgs2816crpsUdpDestPortFilterConf,
       "lgs2816crpsAceTcpParameters": lgs2816crpsAceTcpParameters,
       "lgs2816crpsTcpSourcePortFilterConf": lgs2816crpsTcpSourcePortFilterConf,
       "lgs2816crpsTcpDestPortFilterConf": lgs2816crpsTcpDestPortFilterConf,
       "lgs2816crpsTcpFINConf": lgs2816crpsTcpFINConf,
       "lgs2816crpsTcpSYNConf": lgs2816crpsTcpSYNConf,
       "lgs2816crpsTcpRSTConf": lgs2816crpsTcpRSTConf,
       "lgs2816crpsTcpPSHConf": lgs2816crpsTcpPSHConf,
       "lgs2816crpsTcpACKConf": lgs2816crpsTcpACKConf,
       "lgs2816crpsTcpURGConf": lgs2816crpsTcpURGConf,
       "lgs2816crpsAceIpProtocolValue": lgs2816crpsAceIpProtocolValue,
       "lgs2816crpsAceIpTTL": lgs2816crpsAceIpTTL,
       "lgs2816crpsAceIpFragment": lgs2816crpsAceIpFragment,
       "lgs2816crpsAceIpOption": lgs2816crpsAceIpOption,
       "lgs2816crpsAceSipFilter": lgs2816crpsAceSipFilter,
       "lgs2816crpsAceSipAddress": lgs2816crpsAceSipAddress,
       "lgs2816crpsAceSipMask": lgs2816crpsAceSipMask,
       "lgs2816crpsAceDipFilter": lgs2816crpsAceDipFilter,
       "lgs2816crpsAceDipAddress": lgs2816crpsAceDipAddress,
       "lgs2816crpsAceDipMask": lgs2816crpsAceDipMask,
       "lgs2816crpsAceActionConf": lgs2816crpsAceActionConf,
       "lgs2816crpsAceRateLimiterConf": lgs2816crpsAceRateLimiterConf,
       "lgs2816crpsAcePortCopyConf": lgs2816crpsAcePortCopyConf,
       "lgs2816crpsAceMacParameters": lgs2816crpsAceMacParameters,
       "lgs2816crpsAceSmacFilter": lgs2816crpsAceSmacFilter,
       "lgs2816crpsAceDmacFilter": lgs2816crpsAceDmacFilter,
       "lgs2816crpsAceVlanParameters": lgs2816crpsAceVlanParameters,
       "lgs2816crpsAceVlanIdFilter": lgs2816crpsAceVlanIdFilter,
       "lgs2816crpsAceTagPriority": lgs2816crpsAceTagPriority,
       "lgs2816crpsAceInfoEntryAction": lgs2816crpsAceInfoEntryAction,
       "lgs2816crpsIpMacBind": lgs2816crpsIpMacBind,
       "lgs2816crpsIpMacBindConf": lgs2816crpsIpMacBindConf,
       "lgs2816crpsIpMacBindstate": lgs2816crpsIpMacBindstate,
       "lgs2816crpsIpMacBindTrustPort": lgs2816crpsIpMacBindTrustPort,
       "lgs2816crpsIpMacBindSetting": lgs2816crpsIpMacBindSetting,
       "lgs2816crpsIpMacBindSettingNumber": lgs2816crpsIpMacBindSettingNumber,
       "lgs2816crpsIpMacBindSettingEntryCreate": lgs2816crpsIpMacBindSettingEntryCreate,
       "lgs2816crpsIpMacBindSettingTable": lgs2816crpsIpMacBindSettingTable,
       "lgs2816crpsIpMacBindSettingEntry": lgs2816crpsIpMacBindSettingEntry,
       "lgs2816crpsIpMacBindSettingIndex": lgs2816crpsIpMacBindSettingIndex,
       "lgs2816crpsIpMacBindSettingMAC": lgs2816crpsIpMacBindSettingMAC,
       "lgs2816crpsIpMacBindSettingIP": lgs2816crpsIpMacBindSettingIP,
       "lgs2816crpsIpMacBindSettingPort": lgs2816crpsIpMacBindSettingPort,
       "lgs2816crpsIpMacBindSettingVID": lgs2816crpsIpMacBindSettingVID,
       "lgs2816crpsIpMacBindSettingEntryAction": lgs2816crpsIpMacBindSettingEntryAction,
       "lgs2816crpsTrapEntry": lgs2816crpsTrapEntry,
       "lgs2816crpsUserLogin": lgs2816crpsUserLogin,
       "lgs2816crpsUserLogout": lgs2816crpsUserLogout,
       "lgs2816crpsModuleInserted": lgs2816crpsModuleInserted,
       "lgs2816crpsModuleRemoved": lgs2816crpsModuleRemoved,
       "lgs2816crpsDualMediaSwapped": lgs2816crpsDualMediaSwapped,
       "lgs2816crpsLoopDetected": lgs2816crpsLoopDetected,
       "lgs2816crpsStpStateDisabled": lgs2816crpsStpStateDisabled,
       "lgs2816crpsStpStateEnabled": lgs2816crpsStpStateEnabled,
       "lgs2816crpsStpTopologyChanged": lgs2816crpsStpTopologyChanged,
       "lgs2816crpsLacpStateDisabled": lgs2816crpsLacpStateDisabled,
       "lgs2816crpsLacpStateEnabled": lgs2816crpsLacpStateEnabled,
       "lgs2816crpsLacpPortAdded": lgs2816crpsLacpPortAdded,
       "lgs2816crpsLacpPortTrunkFailure": lgs2816crpsLacpPortTrunkFailure,
       "lgs2816crpsGvrpStateDisabled": lgs2816crpsGvrpStateDisabled,
       "lgs2816crpsGvrpStateEnabled": lgs2816crpsGvrpStateEnabled,
       "lgs2816crpsVlanPortBaseEnabled": lgs2816crpsVlanPortBaseEnabled,
       "lgs2816crpsVlanTagBaseEnabled": lgs2816crpsVlanTagBaseEnabled,
       "lgs2816crpsIpmbStateEnabled": lgs2816crpsIpmbStateEnabled,
       "lgs2816crpsIpmbStateDisabled": lgs2816crpsIpmbStateDisabled,
       "lgs2816crpsIpmbEntryFailure": lgs2816crpsIpmbEntryFailure,
       "lgs2816crpsRP2000TempEvent": lgs2816crpsRP2000TempEvent,
       "lgs2816crpsRP2000FanEvent": lgs2816crpsRP2000FanEvent,
       "lgs2816crpsRP2000VoltEvent": lgs2816crpsRP2000VoltEvent,
       "lgs2816crpsRP2000PwrEvent": lgs2816crpsRP2000PwrEvent,
       "lgs2816crpsTrapVariable": lgs2816crpsTrapVariable,
       "username": username,
       "groupId": groupId,
       "actorkey": actorkey,
       "partnerkey": partnerkey,
       "swapto": swapto,
       "ipmacIp": ipmacIp,
       "ipmacMac": ipmacMac,
       "rp2000eventstatus": rp2000eventstatus,
       "rp2000eventinfo": rp2000eventinfo,
       "lgs2816crpsDot1X": lgs2816crpsDot1X,
       "lgs2816crpsDot1XServerConf": lgs2816crpsDot1XServerConf,
       "lgs2816crpsDot1XServerConfAuthenticationServerIp": lgs2816crpsDot1XServerConfAuthenticationServerIp,
       "lgs2816crpsDot1XServerConfAuthenticationUdpPort": lgs2816crpsDot1XServerConfAuthenticationUdpPort,
       "lgs2816crpsDot1XServerConfAuthenticationServerIp2": lgs2816crpsDot1XServerConfAuthenticationServerIp2,
       "lgs2816crpsDot1XServerConfAuthenticationUdpPort2": lgs2816crpsDot1XServerConfAuthenticationUdpPort2,
       "lgs2816crpsDot1XServerConfAuthenticationSecretKey": lgs2816crpsDot1XServerConfAuthenticationSecretKey,
       "lgs2816crpsDot1XServerConfAccountingServerIp": lgs2816crpsDot1XServerConfAccountingServerIp,
       "lgs2816crpsDot1XServerConfAccountingUdpPort": lgs2816crpsDot1XServerConfAccountingUdpPort,
       "lgs2816crpsDot1XServerConfAccountingServerIp2": lgs2816crpsDot1XServerConfAccountingServerIp2,
       "lgs2816crpsDot1XServerConfAccountingUdpPort2": lgs2816crpsDot1XServerConfAccountingUdpPort2,
       "lgs2816crpsDot1XServerConfAccountingSecretKey": lgs2816crpsDot1XServerConfAccountingSecretKey,
       "lgs2816crpsDot1XPortConfTable": lgs2816crpsDot1XPortConfTable,
       "lgs2816crpsDot1XPortConfEntry": lgs2816crpsDot1XPortConfEntry,
       "lgs2816crpsDot1XPort": lgs2816crpsDot1XPort,
       "lgs2816crpsDot1XPortMode": lgs2816crpsDot1XPortMode,
       "lgs2816crpsDot1XPortControl": lgs2816crpsDot1XPortControl,
       "lgs2816crpsDot1XPortreAuthMax": lgs2816crpsDot1XPortreAuthMax,
       "lgs2816crpsDot1XPorttxPeriod": lgs2816crpsDot1XPorttxPeriod,
       "lgs2816crpsDot1XPortquietPeriod": lgs2816crpsDot1XPortquietPeriod,
       "lgs2816crpsDot1XPortreAuthEnabled": lgs2816crpsDot1XPortreAuthEnabled,
       "lgs2816crpsDot1XPortreAuthPeriod": lgs2816crpsDot1XPortreAuthPeriod,
       "lgs2816crpsDot1XPortmaxReq": lgs2816crpsDot1XPortmaxReq,
       "lgs2816crpsDot1XPortsuppTimeout": lgs2816crpsDot1XPortsuppTimeout,
       "lgs2816crpsDot1XPortserverTimeout": lgs2816crpsDot1XPortserverTimeout,
       "lgs2816crpsDot1XPortVlanAssignment": lgs2816crpsDot1XPortVlanAssignment,
       "lgs2816crpsDot1XPortGuestVlan": lgs2816crpsDot1XPortGuestVlan,
       "lgs2816crpsDot1XPortAuthFailedVlan": lgs2816crpsDot1XPortAuthFailedVlan,
       "lgs2816crpsDot1XStatusTable": lgs2816crpsDot1XStatusTable,
       "lgs2816crpsDot1XStatusEntry": lgs2816crpsDot1XStatusEntry,
       "lgs2816crpsDot1XStatusIndex": lgs2816crpsDot1XStatusIndex,
       "lgs2816crpsDot1XStatusMode": lgs2816crpsDot1XStatusMode,
       "lgs2816crpsDot1XStatusStatus": lgs2816crpsDot1XStatusStatus,
       "lgs2816crpsDot1XVlanPolicy": lgs2816crpsDot1XVlanPolicy,
       "lgs2816crpsDot1XStatisticsTable": lgs2816crpsDot1XStatisticsTable,
       "lgs2816crpsDot1XStatisticsEntry": lgs2816crpsDot1XStatisticsEntry,
       "lgs2816crpsDot1XStatisticsIndex": lgs2816crpsDot1XStatisticsIndex,
       "lgs2816crpsDot1XClearCounter": lgs2816crpsDot1XClearCounter,
       "lgs2816crpsDot1XAuthEntersConnecting": lgs2816crpsDot1XAuthEntersConnecting,
       "lgs2816crpsDot1XauthEapLogoffsWhileConnecting": lgs2816crpsDot1XauthEapLogoffsWhileConnecting,
       "lgs2816crpsDot1XAuthEntersAuthenticating": lgs2816crpsDot1XAuthEntersAuthenticating,
       "lgs2816crpsDot1XAuthAuthSuccessesWhileAuthenticating": lgs2816crpsDot1XAuthAuthSuccessesWhileAuthenticating,
       "lgs2816crpsDot1XAuthAuthTimeoutsWhileAuthenticating": lgs2816crpsDot1XAuthAuthTimeoutsWhileAuthenticating,
       "lgs2816crpsDot1XAuthAuthFailWhileAuthenticating": lgs2816crpsDot1XAuthAuthFailWhileAuthenticating,
       "lgs2816crpsDot1XAuthAuthEapStartsWhileAuthenticating": lgs2816crpsDot1XAuthAuthEapStartsWhileAuthenticating,
       "lgs2816crpsDot1XAuthAuthEapLogoffWhileAuthenticating": lgs2816crpsDot1XAuthAuthEapLogoffWhileAuthenticating,
       "lgs2816crpsDot1XAuthAuthReauthsWhileAuthenticated": lgs2816crpsDot1XAuthAuthReauthsWhileAuthenticated,
       "lgs2816crpsDot1XAuthAuthEapStartsWhileAuthenticated": lgs2816crpsDot1XAuthAuthEapStartsWhileAuthenticated,
       "lgs2816crpsDot1XAuthAuthEapLogoffWhileAuthenticated": lgs2816crpsDot1XAuthAuthEapLogoffWhileAuthenticated,
       "lgs2816crpsDot1XBackendResponses": lgs2816crpsDot1XBackendResponses,
       "lgs2816crpsDot1XBackendAccessChallenges": lgs2816crpsDot1XBackendAccessChallenges,
       "lgs2816crpsDot1XBackendOtherRequestsToSupplicant": lgs2816crpsDot1XBackendOtherRequestsToSupplicant,
       "lgs2816crpsDot1XBackendAuthSuccesses": lgs2816crpsDot1XBackendAuthSuccesses,
       "lgs2816crpsDot1XBackendAuthFails": lgs2816crpsDot1XBackendAuthFails,
       "lgs2816crpsDot1XAuthEapolFramesRx": lgs2816crpsDot1XAuthEapolFramesRx,
       "lgs2816crpsDot1XAuthEapolFramesTx": lgs2816crpsDot1XAuthEapolFramesTx,
       "lgs2816crpsDot1XAuthEapolStartFramesRx": lgs2816crpsDot1XAuthEapolStartFramesRx,
       "lgs2816crpsDot1XAuthEapolLogoffFramesRx": lgs2816crpsDot1XAuthEapolLogoffFramesRx,
       "lgs2816crpsDot1XAuthEapolRespIdFramesRx": lgs2816crpsDot1XAuthEapolRespIdFramesRx,
       "lgs2816crpsDot1XAuthEapolRespFramesRx": lgs2816crpsDot1XAuthEapolRespFramesRx,
       "lgs2816crpsDot1XAuthEapolReqIdFramesTx": lgs2816crpsDot1XAuthEapolReqIdFramesTx,
       "lgs2816crpsDot1XAuthEapolReqFramesTx": lgs2816crpsDot1XAuthEapolReqFramesTx,
       "lgs2816crpsDot1XAuthInvalidEapolFramesRx": lgs2816crpsDot1XAuthInvalidEapolFramesRx,
       "lgs2816crpsDot1XAuthEapLengthErrorFramesRx": lgs2816crpsDot1XAuthEapLengthErrorFramesRx,
       "lgs2816crpsDot1XAuthLastEapolFrameVersion": lgs2816crpsDot1XAuthLastEapolFrameVersion,
       "lgs2816crpsDot1XAuthLastEapolFrameSource": lgs2816crpsDot1XAuthLastEapolFrameSource,
       "lgs2816crpsTrunkInfo": lgs2816crpsTrunkInfo,
       "lgs2816crpsTrunkPort": lgs2816crpsTrunkPort,
       "lgs2816crpsTrunkPortTable": lgs2816crpsTrunkPortTable,
       "lgs2816crpsTrunkPortEntry": lgs2816crpsTrunkPortEntry,
       "lgs2816crpsTrunkPortIndex": lgs2816crpsTrunkPortIndex,
       "lgs2816crpsTrunkPortMethod": lgs2816crpsTrunkPortMethod,
       "lgs2816crpsTrunkPortGroup": lgs2816crpsTrunkPortGroup,
       "lgs2816crpsTrunkPortActiveLacp": lgs2816crpsTrunkPortActiveLacp,
       "lgs2816crpsTrunkPortAggtr": lgs2816crpsTrunkPortAggtr,
       "lgs2816crpsTrunkPortStatus": lgs2816crpsTrunkPortStatus,
       "lgs2816crpsTrunkPortCurrentMode": lgs2816crpsTrunkPortCurrentMode,
       "lgs2816crpsAggregatorView": lgs2816crpsAggregatorView,
       "lgs2816crpsAggregatorViewTable": lgs2816crpsAggregatorViewTable,
       "lgs2816crpsAggregatorViewEntry": lgs2816crpsAggregatorViewEntry,
       "lgs2816crpsAggregatorViewIndex": lgs2816crpsAggregatorViewIndex,
       "lgs2816crpsAggregatorViewMethod": lgs2816crpsAggregatorViewMethod,
       "lgs2816crpsAggregatorViewMemberPorts": lgs2816crpsAggregatorViewMemberPorts,
       "lgs2816crpsAggregatorViewReadyPorts": lgs2816crpsAggregatorViewReadyPorts,
       "lgs2816crpsLacpSystemPriority": lgs2816crpsLacpSystemPriority,
       "lgs2816crpsAggregationHashMode": lgs2816crpsAggregationHashMode,
       "lgs2816crpsHashCodeSourceMacAddress": lgs2816crpsHashCodeSourceMacAddress,
       "lgs2816crpsHashCodeDestinationMacAddress": lgs2816crpsHashCodeDestinationMacAddress,
       "lgs2816crpsHashCodeIpAddress": lgs2816crpsHashCodeIpAddress,
       "lgs2816crpsHashCodeTcpUdpPortNumber": lgs2816crpsHashCodeTcpUdpPortNumber,
       "lgs2816crpsMulticastInfo": lgs2816crpsMulticastInfo,
       "lgs2816crpsIGMPMode": lgs2816crpsIGMPMode,
       "lgs2816crpsIGMPGroupAllowConf": lgs2816crpsIGMPGroupAllowConf,
       "lgs2816crpsIGMPGroupAllowNumber": lgs2816crpsIGMPGroupAllowNumber,
       "lgs2816crpsIGMPGroupAllowEntryCreate": lgs2816crpsIGMPGroupAllowEntryCreate,
       "lgs2816crpsIGMPGroupAllowTable": lgs2816crpsIGMPGroupAllowTable,
       "lgs2816crpsIGMPGroupAllowEntry": lgs2816crpsIGMPGroupAllowEntry,
       "lgs2816crpsIGMPGroupAllowNo": lgs2816crpsIGMPGroupAllowNo,
       "lgs2816crpsIGMPGroupAllowVid": lgs2816crpsIGMPGroupAllowVid,
       "lgs2816crpsIGMPGroupAllowStartAddress": lgs2816crpsIGMPGroupAllowStartAddress,
       "lgs2816crpsIGMPGroupAllowEndAddress": lgs2816crpsIGMPGroupAllowEndAddress,
       "lgs2816crpsIGMPGroupAllowEntryAction": lgs2816crpsIGMPGroupAllowEntryAction,
       "lgs2816crpsIGMPProxy": lgs2816crpsIGMPProxy,
       "lgs2816crpsIgmpProxyConfGeneralQueryInterval": lgs2816crpsIgmpProxyConfGeneralQueryInterval,
       "lgs2816crpsIgmpProxyConfGeneralQueryRepTimeout": lgs2816crpsIgmpProxyConfGeneralQueryRepTimeout,
       "lgs2816crpsIgmpProxyConfGeneralQueryMaxRepTime": lgs2816crpsIgmpProxyConfGeneralQueryMaxRepTime,
       "lgs2816crpsIgmpProxyConfLastMemberQueryCount": lgs2816crpsIgmpProxyConfLastMemberQueryCount,
       "lgs2816crpsIgmpProxyConfLastMemberQueryInterval": lgs2816crpsIgmpProxyConfLastMemberQueryInterval,
       "lgs2816crpsIgmpProxyConfLastMemberQueryMaxRepTime": lgs2816crpsIgmpProxyConfLastMemberQueryMaxRepTime,
       "lgs2816crpsIgmpProxyConfRouterPorts": lgs2816crpsIgmpProxyConfRouterPorts,
       "lgs2816crpsIgmpProxyGroupMembershipNumber": lgs2816crpsIgmpProxyGroupMembershipNumber,
       "lgs2816crpsIgmpProxyGroupMembershipTable": lgs2816crpsIgmpProxyGroupMembershipTable,
       "lgs2816crpsIgmpProxyGroupMembershipEntry": lgs2816crpsIgmpProxyGroupMembershipEntry,
       "lgs2816crpsIgmpProxyGroupNo": lgs2816crpsIgmpProxyGroupNo,
       "lgs2816crpsIgmpProxyGroupAddress": lgs2816crpsIgmpProxyGroupAddress,
       "lgs2816crpsIgmpProxyGroupVLANId": lgs2816crpsIgmpProxyGroupVLANId,
       "lgs2816crpsIgmpProxyGroupPortMembers": lgs2816crpsIgmpProxyGroupPortMembers,
       "lgs2816crpsIGMPSnooping": lgs2816crpsIGMPSnooping,
       "lgs2816crpsIgmpSnoopingConfHostTimeout": lgs2816crpsIgmpSnoopingConfHostTimeout,
       "lgs2816crpsIgmpSnoopingConfFastLeave": lgs2816crpsIgmpSnoopingConfFastLeave,
       "lgs2816crpsIgmpSnoopingConfRouterPorts": lgs2816crpsIgmpSnoopingConfRouterPorts,
       "lgs2816crpsIgmpSnoopingGroupMembershipNumber": lgs2816crpsIgmpSnoopingGroupMembershipNumber,
       "lgs2816crpsIgmpSnoopingGroupMembershipTable": lgs2816crpsIgmpSnoopingGroupMembershipTable,
       "lgs2816crpsIgmpSnoopingGroupMembershipEntry": lgs2816crpsIgmpSnoopingGroupMembershipEntry,
       "lgs2816crpsIgmpSnoopingGroupNo": lgs2816crpsIgmpSnoopingGroupNo,
       "lgs2816crpsIgmpSnoopingGroupAddress": lgs2816crpsIgmpSnoopingGroupAddress,
       "lgs2816crpsIgmpSnoopingGroupVLANId": lgs2816crpsIgmpSnoopingGroupVLANId,
       "lgs2816crpsIgmpSnoopingGroupPortMembers": lgs2816crpsIgmpSnoopingGroupPortMembers,
       "lgs2816crpsMVR": lgs2816crpsMVR,
       "lgs2816crpsMVRMode": lgs2816crpsMVRMode,
       "lgs2816crpsMVRConfHostTimeout": lgs2816crpsMVRConfHostTimeout,
       "lgs2816crpsMVRConfFastLeave": lgs2816crpsMVRConfFastLeave,
       "lgs2816crpsMVIDConf": lgs2816crpsMVIDConf,
       "lgs2816crpsMVIDNumber": lgs2816crpsMVIDNumber,
       "lgs2816crpsMVIDEntryCreate": lgs2816crpsMVIDEntryCreate,
       "lgs2816crpsMVIDGroupTable": lgs2816crpsMVIDGroupTable,
       "lgs2816crpsMVIDGroupEntry": lgs2816crpsMVIDGroupEntry,
       "lgs2816crpsMVID": lgs2816crpsMVID,
       "lgs2816crpsMVIDMemberPort": lgs2816crpsMVIDMemberPort,
       "lgs2816crpsMVIDRouterPorts": lgs2816crpsMVIDRouterPorts,
       "lgs2816crpsMVIDEntryAction": lgs2816crpsMVIDEntryAction,
       "lgs2816crpsMVIDGroupAllowConf": lgs2816crpsMVIDGroupAllowConf,
       "lgs2816crpsMVIDGroupAllowNumber": lgs2816crpsMVIDGroupAllowNumber,
       "lgs2816crpsMVIDGroupAllowEntryCreate": lgs2816crpsMVIDGroupAllowEntryCreate,
       "lgs2816crpsMVIDGroupAllowTable": lgs2816crpsMVIDGroupAllowTable,
       "lgs2816crpsMVIDGroupAllowEntry": lgs2816crpsMVIDGroupAllowEntry,
       "lgs2816crpsMVIDGroupAllowNo": lgs2816crpsMVIDGroupAllowNo,
       "lgs2816crpsMVIDGroupAllowMvid": lgs2816crpsMVIDGroupAllowMvid,
       "lgs2816crpsMVIDGroupAllowStartAddress": lgs2816crpsMVIDGroupAllowStartAddress,
       "lgs2816crpsMVIDGroupAllowEndAddress": lgs2816crpsMVIDGroupAllowEndAddress,
       "lgs2816crpsMVIDGroupAllowEntryAction": lgs2816crpsMVIDGroupAllowEntryAction,
       "lgs2816crpsMVRGroupMembershipNumber": lgs2816crpsMVRGroupMembershipNumber,
       "lgs2816crpsMVRGroupMembershipTable": lgs2816crpsMVRGroupMembershipTable,
       "lgs2816crpsMVRGroupMembershipEntry": lgs2816crpsMVRGroupMembershipEntry,
       "lgs2816crpsMVRGroupNo": lgs2816crpsMVRGroupNo,
       "lgs2816crpsMVRGroupAddress": lgs2816crpsMVRGroupAddress,
       "lgs2816crpsMVRGroupVLANId": lgs2816crpsMVRGroupVLANId,
       "lgs2816crpsMVRGroupPortMembers": lgs2816crpsMVRGroupPortMembers,
       "lgs2816crpsDhcpSnooping": lgs2816crpsDhcpSnooping,
       "lgs2816crpsDhcpSnoopingState": lgs2816crpsDhcpSnoopingState,
       "lgs2816crpsDhcpSnoopingInfo": lgs2816crpsDhcpSnoopingInfo,
       "lgs2816crpsDhcpSnoopingCreate": lgs2816crpsDhcpSnoopingCreate,
       "lgs2816crpsDhcpSnoopingTable": lgs2816crpsDhcpSnoopingTable,
       "lgs2816crpsDhcpSnoopingEntry": lgs2816crpsDhcpSnoopingEntry,
       "lgs2816crpsDhcpSnoopingIndex": lgs2816crpsDhcpSnoopingIndex,
       "lgs2816crpsDhcpSnoopingVID": lgs2816crpsDhcpSnoopingVID,
       "lgs2816crpsDhcpSnoopingTrustPort1": lgs2816crpsDhcpSnoopingTrustPort1,
       "lgs2816crpsDhcpSnoopingTrustPort2": lgs2816crpsDhcpSnoopingTrustPort2,
       "lgs2816crpsDhcpSnoopingServerIP": lgs2816crpsDhcpSnoopingServerIP,
       "lgs2816crpsDhcpSnoopingOption82": lgs2816crpsDhcpSnoopingOption82,
       "lgs2816crpsDhcpSnoopingAction": lgs2816crpsDhcpSnoopingAction,
       "lgs2816crpsDhcpSnoopingEntryAction": lgs2816crpsDhcpSnoopingEntryAction,
       "lgs2816crpsDhcpSnoopingDefaultData": lgs2816crpsDhcpSnoopingDefaultData,
       "lgs2816crpsDhcpSnoopingDefaultVID": lgs2816crpsDhcpSnoopingDefaultVID,
       "lgs2816crpsDhcpSnoopingDefaultTrustPort1": lgs2816crpsDhcpSnoopingDefaultTrustPort1,
       "lgs2816crpsDhcpSnoopingDefaultTrustPort2": lgs2816crpsDhcpSnoopingDefaultTrustPort2,
       "lgs2816crpsDhcpSnoopingDefaultServerIP": lgs2816crpsDhcpSnoopingDefaultServerIP,
       "lgs2816crpsDhcpSnoopingDefaultOption82": lgs2816crpsDhcpSnoopingDefaultOption82,
       "lgs2816crpsDhcpSnoopingDefaultAction": lgs2816crpsDhcpSnoopingDefaultAction,
       "lgs2816crpsDhcpSnoopingDefaultEntryAction": lgs2816crpsDhcpSnoopingDefaultEntryAction,
       "lgs2816crpsDhcpSnoopingClientTable": lgs2816crpsDhcpSnoopingClientTable,
       "lgs2816crpsDhcpSnoopingClientEntry": lgs2816crpsDhcpSnoopingClientEntry,
       "lgs2816crpsDhcpSnoopingClientIndex": lgs2816crpsDhcpSnoopingClientIndex,
       "lgs2816crpsDhcpSnoopingClientMac": lgs2816crpsDhcpSnoopingClientMac,
       "lgs2816crpsDhcpSnoopingClientVID": lgs2816crpsDhcpSnoopingClientVID,
       "lgs2816crpsDhcpSnoopingClientPort": lgs2816crpsDhcpSnoopingClientPort,
       "lgs2816crpsDhcpSnoopingClientIP": lgs2816crpsDhcpSnoopingClientIP,
       "lgs2816crpsDhcpSnoopingClientLease": lgs2816crpsDhcpSnoopingClientLease}
)
