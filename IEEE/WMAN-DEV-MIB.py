# SNMP MIB module (WMAN-DEV-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/IEEE/WMAN-DEV-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 18:18:43 2025
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
    "iso")

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

wmanDevMib = ModuleIdentity(
    (1, 0, 8802, 16, 1)
)
if mibBuilder.loadTexts:
    wmanDevMib.setRevisions(
        ("2005-08-02 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class WmanDevEventSeverity(TextualConvention, Integer32):
    status = "current"
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
        *(("emergency", 1),
          ("alert", 2),
          ("critical", 3),
          ("error", 4),
          ("warning", 5),
          ("notice", 6),
          ("informational", 7),
          ("debug", 8))
    )



# MIB Managed Objects in the order of their OIDs

_WmanDevMibObjects_ObjectIdentity = ObjectIdentity
wmanDevMibObjects = _WmanDevMibObjects_ObjectIdentity(
    (1, 0, 8802, 16, 1, 1)
)
_WmanDevBsObjects_ObjectIdentity = ObjectIdentity
wmanDevBsObjects = _WmanDevBsObjects_ObjectIdentity(
    (1, 0, 8802, 16, 1, 1, 1)
)
_WmanDevBsSoftwareUpgradeTable_Object = MibTable
wmanDevBsSoftwareUpgradeTable = _WmanDevBsSoftwareUpgradeTable_Object(
    (1, 0, 8802, 16, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    wmanDevBsSoftwareUpgradeTable.setStatus("current")
_WmanDevBsSoftwareUpgradeEntry_Object = MibTableRow
wmanDevBsSoftwareUpgradeEntry = _WmanDevBsSoftwareUpgradeEntry_Object(
    (1, 0, 8802, 16, 1, 1, 1, 1, 1)
)
wmanDevBsSoftwareUpgradeEntry.setIndexNames(
    (0, "WMAN-DEV-MIB", "wmanDevBsDeviceIndex"),
)
if mibBuilder.loadTexts:
    wmanDevBsSoftwareUpgradeEntry.setStatus("current")


class _WmanDevBsDeviceIndex_Type(Integer32):
    """Custom type wmanDevBsDeviceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_WmanDevBsDeviceIndex_Type.__name__ = "Integer32"
_WmanDevBsDeviceIndex_Object = MibTableColumn
wmanDevBsDeviceIndex = _WmanDevBsDeviceIndex_Object(
    (1, 0, 8802, 16, 1, 1, 1, 1, 1, 1),
    _WmanDevBsDeviceIndex_Type()
)
wmanDevBsDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wmanDevBsDeviceIndex.setStatus("current")


class _WmanDevBsVendorId_Type(OctetString):
    """Custom type wmanDevBsVendorId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 256),
    )


_WmanDevBsVendorId_Type.__name__ = "OctetString"
_WmanDevBsVendorId_Object = MibTableColumn
wmanDevBsVendorId = _WmanDevBsVendorId_Object(
    (1, 0, 8802, 16, 1, 1, 1, 1, 1, 2),
    _WmanDevBsVendorId_Type()
)
wmanDevBsVendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanDevBsVendorId.setStatus("current")


class _WmanDevBsHwId_Type(OctetString):
    """Custom type wmanDevBsHwId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 256),
    )


_WmanDevBsHwId_Type.__name__ = "OctetString"
_WmanDevBsHwId_Object = MibTableColumn
wmanDevBsHwId = _WmanDevBsHwId_Object(
    (1, 0, 8802, 16, 1, 1, 1, 1, 1, 3),
    _WmanDevBsHwId_Type()
)
wmanDevBsHwId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanDevBsHwId.setStatus("current")


class _WmanDevBsCurrentSwVersion_Type(OctetString):
    """Custom type wmanDevBsCurrentSwVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 256),
    )


_WmanDevBsCurrentSwVersion_Type.__name__ = "OctetString"
_WmanDevBsCurrentSwVersion_Object = MibTableColumn
wmanDevBsCurrentSwVersion = _WmanDevBsCurrentSwVersion_Object(
    (1, 0, 8802, 16, 1, 1, 1, 1, 1, 4),
    _WmanDevBsCurrentSwVersion_Type()
)
wmanDevBsCurrentSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanDevBsCurrentSwVersion.setStatus("current")


class _WmanDevBsDownloadSwVersion_Type(OctetString):
    """Custom type wmanDevBsDownloadSwVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 256),
    )


_WmanDevBsDownloadSwVersion_Type.__name__ = "OctetString"
_WmanDevBsDownloadSwVersion_Object = MibTableColumn
wmanDevBsDownloadSwVersion = _WmanDevBsDownloadSwVersion_Object(
    (1, 0, 8802, 16, 1, 1, 1, 1, 1, 5),
    _WmanDevBsDownloadSwVersion_Type()
)
wmanDevBsDownloadSwVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanDevBsDownloadSwVersion.setStatus("current")


class _WmanDevBsUpgradeFileName_Type(OctetString):
    """Custom type wmanDevBsUpgradeFileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 256),
    )


_WmanDevBsUpgradeFileName_Type.__name__ = "OctetString"
_WmanDevBsUpgradeFileName_Object = MibTableColumn
wmanDevBsUpgradeFileName = _WmanDevBsUpgradeFileName_Object(
    (1, 0, 8802, 16, 1, 1, 1, 1, 1, 6),
    _WmanDevBsUpgradeFileName_Type()
)
wmanDevBsUpgradeFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanDevBsUpgradeFileName.setStatus("current")


class _WmanDevBsSoftwareUpgradeAdminState_Type(Integer32):
    """Custom type wmanDevBsSoftwareUpgradeAdminState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("null", 0),
          ("download", 1),
          ("activate", 2))
    )


_WmanDevBsSoftwareUpgradeAdminState_Type.__name__ = "Integer32"
_WmanDevBsSoftwareUpgradeAdminState_Object = MibTableColumn
wmanDevBsSoftwareUpgradeAdminState = _WmanDevBsSoftwareUpgradeAdminState_Object(
    (1, 0, 8802, 16, 1, 1, 1, 1, 1, 7),
    _WmanDevBsSoftwareUpgradeAdminState_Type()
)
wmanDevBsSoftwareUpgradeAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanDevBsSoftwareUpgradeAdminState.setStatus("current")


class _WmanDevBsDownloadSwProgress_Type(Integer32):
    """Custom type wmanDevBsDownloadSwProgress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_WmanDevBsDownloadSwProgress_Type.__name__ = "Integer32"
_WmanDevBsDownloadSwProgress_Object = MibTableColumn
wmanDevBsDownloadSwProgress = _WmanDevBsDownloadSwProgress_Object(
    (1, 0, 8802, 16, 1, 1, 1, 1, 1, 8),
    _WmanDevBsDownloadSwProgress_Type()
)
wmanDevBsDownloadSwProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanDevBsDownloadSwProgress.setStatus("current")
if mibBuilder.loadTexts:
    wmanDevBsDownloadSwProgress.setUnits("%")
_WmanDevBsSoftwareUpgradeTimeStamp_Type = DateAndTime
_WmanDevBsSoftwareUpgradeTimeStamp_Object = MibTableColumn
wmanDevBsSoftwareUpgradeTimeStamp = _WmanDevBsSoftwareUpgradeTimeStamp_Object(
    (1, 0, 8802, 16, 1, 1, 1, 1, 1, 9),
    _WmanDevBsSoftwareUpgradeTimeStamp_Type()
)
wmanDevBsSoftwareUpgradeTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanDevBsSoftwareUpgradeTimeStamp.setStatus("current")
_WmanDevBsNotification_ObjectIdentity = ObjectIdentity
wmanDevBsNotification = _WmanDevBsNotification_ObjectIdentity(
    (1, 0, 8802, 16, 1, 1, 1, 2)
)
_WmanDevBsTrapControl_ObjectIdentity = ObjectIdentity
wmanDevBsTrapControl = _WmanDevBsTrapControl_ObjectIdentity(
    (1, 0, 8802, 16, 1, 1, 1, 2, 1)
)


class _WmanDevBsTrapControlRegister_Type(Bits):
    """Custom type wmanDevBsTrapControlRegister based on Bits"""
    namedValues = NamedValues(
        *(("wmanDevBsEvent", 0),
          ("wmanDevBsLogBuffExceedThresholdTrapControl", 1))
    )

_WmanDevBsTrapControlRegister_Type.__name__ = "Bits"
_WmanDevBsTrapControlRegister_Object = MibScalar
wmanDevBsTrapControlRegister = _WmanDevBsTrapControlRegister_Object(
    (1, 0, 8802, 16, 1, 1, 1, 2, 1, 1),
    _WmanDevBsTrapControlRegister_Type()
)
wmanDevBsTrapControlRegister.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanDevBsTrapControlRegister.setStatus("current")
_WmanDevBsTrapDefinition_ObjectIdentity = ObjectIdentity
wmanDevBsTrapDefinition = _WmanDevBsTrapDefinition_ObjectIdentity(
    (1, 0, 8802, 16, 1, 1, 1, 2, 2)
)
_WmanDevBsTrapPrefix_ObjectIdentity = ObjectIdentity
wmanDevBsTrapPrefix = _WmanDevBsTrapPrefix_ObjectIdentity(
    (1, 0, 8802, 16, 1, 1, 1, 2, 2, 0)
)
_WmanDevSsObjects_ObjectIdentity = ObjectIdentity
wmanDevSsObjects = _WmanDevSsObjects_ObjectIdentity(
    (1, 0, 8802, 16, 1, 1, 2)
)
_WmanDevSsConfigFileEncodingTable_Object = MibTable
wmanDevSsConfigFileEncodingTable = _WmanDevSsConfigFileEncodingTable_Object(
    (1, 0, 8802, 16, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    wmanDevSsConfigFileEncodingTable.setStatus("current")
_WmanDevSsConfigFileEncodingEntry_Object = MibTableRow
wmanDevSsConfigFileEncodingEntry = _WmanDevSsConfigFileEncodingEntry_Object(
    (1, 0, 8802, 16, 1, 1, 2, 1, 1)
)
wmanDevSsConfigFileEncodingEntry.setIndexNames(
    (0, "WMAN-DEV-MIB", "wmanDevSsDeviceIndex"),
)
if mibBuilder.loadTexts:
    wmanDevSsConfigFileEncodingEntry.setStatus("current")


class _WmanDevSsDeviceIndex_Type(Integer32):
    """Custom type wmanDevSsDeviceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_WmanDevSsDeviceIndex_Type.__name__ = "Integer32"
_WmanDevSsDeviceIndex_Object = MibTableColumn
wmanDevSsDeviceIndex = _WmanDevSsDeviceIndex_Object(
    (1, 0, 8802, 16, 1, 1, 2, 1, 1, 1),
    _WmanDevSsDeviceIndex_Type()
)
wmanDevSsDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wmanDevSsDeviceIndex.setStatus("current")


class _WmanDevSsMicConfigSetting_Type(OctetString):
    """Custom type wmanDevSsMicConfigSetting based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )
    fixedLength = 20


_WmanDevSsMicConfigSetting_Type.__name__ = "OctetString"
_WmanDevSsMicConfigSetting_Object = MibTableColumn
wmanDevSsMicConfigSetting = _WmanDevSsMicConfigSetting_Object(
    (1, 0, 8802, 16, 1, 1, 2, 1, 1, 2),
    _WmanDevSsMicConfigSetting_Type()
)
wmanDevSsMicConfigSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanDevSsMicConfigSetting.setStatus("current")


class _WmanDevSsVendorId_Type(OctetString):
    """Custom type wmanDevSsVendorId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixedLength = 3


_WmanDevSsVendorId_Type.__name__ = "OctetString"
_WmanDevSsVendorId_Object = MibTableColumn
wmanDevSsVendorId = _WmanDevSsVendorId_Object(
    (1, 0, 8802, 16, 1, 1, 2, 1, 1, 3),
    _WmanDevSsVendorId_Type()
)
wmanDevSsVendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanDevSsVendorId.setStatus("current")


class _WmanDevSsHwId_Type(OctetString):
    """Custom type wmanDevSsHwId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_WmanDevSsHwId_Type.__name__ = "OctetString"
_WmanDevSsHwId_Object = MibTableColumn
wmanDevSsHwId = _WmanDevSsHwId_Object(
    (1, 0, 8802, 16, 1, 1, 2, 1, 1, 4),
    _WmanDevSsHwId_Type()
)
wmanDevSsHwId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanDevSsHwId.setStatus("current")


class _WmanDevSsSwVersion_Type(OctetString):
    """Custom type wmanDevSsSwVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_WmanDevSsSwVersion_Type.__name__ = "OctetString"
_WmanDevSsSwVersion_Object = MibTableColumn
wmanDevSsSwVersion = _WmanDevSsSwVersion_Object(
    (1, 0, 8802, 16, 1, 1, 2, 1, 1, 5),
    _WmanDevSsSwVersion_Type()
)
wmanDevSsSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanDevSsSwVersion.setStatus("current")


class _WmanDevSsUpgradeFileName_Type(OctetString):
    """Custom type wmanDevSsUpgradeFileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_WmanDevSsUpgradeFileName_Type.__name__ = "OctetString"
_WmanDevSsUpgradeFileName_Object = MibTableColumn
wmanDevSsUpgradeFileName = _WmanDevSsUpgradeFileName_Object(
    (1, 0, 8802, 16, 1, 1, 2, 1, 1, 6),
    _WmanDevSsUpgradeFileName_Type()
)
wmanDevSsUpgradeFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanDevSsUpgradeFileName.setStatus("current")
_WmanDevSsSwUpgradeTftpServer_Type = InetAddress
_WmanDevSsSwUpgradeTftpServer_Object = MibTableColumn
wmanDevSsSwUpgradeTftpServer = _WmanDevSsSwUpgradeTftpServer_Object(
    (1, 0, 8802, 16, 1, 1, 2, 1, 1, 7),
    _WmanDevSsSwUpgradeTftpServer_Type()
)
wmanDevSsSwUpgradeTftpServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanDevSsSwUpgradeTftpServer.setStatus("current")
_WmanDevSsTftpServerTimeStamp_Type = DateAndTime
_WmanDevSsTftpServerTimeStamp_Object = MibTableColumn
wmanDevSsTftpServerTimeStamp = _WmanDevSsTftpServerTimeStamp_Object(
    (1, 0, 8802, 16, 1, 1, 2, 1, 1, 8),
    _WmanDevSsTftpServerTimeStamp_Type()
)
wmanDevSsTftpServerTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanDevSsTftpServerTimeStamp.setStatus("current")
_WmanDevSsNotification_ObjectIdentity = ObjectIdentity
wmanDevSsNotification = _WmanDevSsNotification_ObjectIdentity(
    (1, 0, 8802, 16, 1, 1, 2, 2)
)
_WmanDevSsTrapControl_ObjectIdentity = ObjectIdentity
wmanDevSsTrapControl = _WmanDevSsTrapControl_ObjectIdentity(
    (1, 0, 8802, 16, 1, 1, 2, 2, 1)
)


class _WmanDevSsTrapControlRegister_Type(Bits):
    """Custom type wmanDevSsTrapControlRegister based on Bits"""
    namedValues = NamedValues(
        *(("wmanDevSsEventTrapControl", 0),
          ("wmanDevSsLogBuffExceedThresholdTrapControl", 1))
    )

_WmanDevSsTrapControlRegister_Type.__name__ = "Bits"
_WmanDevSsTrapControlRegister_Object = MibScalar
wmanDevSsTrapControlRegister = _WmanDevSsTrapControlRegister_Object(
    (1, 0, 8802, 16, 1, 1, 2, 2, 1, 1),
    _WmanDevSsTrapControlRegister_Type()
)
wmanDevSsTrapControlRegister.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanDevSsTrapControlRegister.setStatus("current")
_WmanDevSsTrapDefinitions_ObjectIdentity = ObjectIdentity
wmanDevSsTrapDefinitions = _WmanDevSsTrapDefinitions_ObjectIdentity(
    (1, 0, 8802, 16, 1, 1, 2, 2, 2)
)
_WmanDevSsTrapPrefix_ObjectIdentity = ObjectIdentity
wmanDevSsTrapPrefix = _WmanDevSsTrapPrefix_ObjectIdentity(
    (1, 0, 8802, 16, 1, 1, 2, 2, 2, 0)
)
_WmanDevCommonObjects_ObjectIdentity = ObjectIdentity
wmanDevCommonObjects = _WmanDevCommonObjects_ObjectIdentity(
    (1, 0, 8802, 16, 1, 1, 3)
)
_WmanDevCmnEventLog_ObjectIdentity = ObjectIdentity
wmanDevCmnEventLog = _WmanDevCmnEventLog_ObjectIdentity(
    (1, 0, 8802, 16, 1, 1, 3, 1)
)
_WmanDevCmnEventLogConfigTable_Object = MibTable
wmanDevCmnEventLogConfigTable = _WmanDevCmnEventLogConfigTable_Object(
    (1, 0, 8802, 16, 1, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    wmanDevCmnEventLogConfigTable.setStatus("current")
_WmanDevCmnEventLogConfigEntry_Object = MibTableRow
wmanDevCmnEventLogConfigEntry = _WmanDevCmnEventLogConfigEntry_Object(
    (1, 0, 8802, 16, 1, 1, 3, 1, 1, 1)
)
wmanDevCmnEventLogConfigEntry.setIndexNames(
    (0, "WMAN-DEV-MIB", "wmanDevCmnDeviceIndex"),
)
if mibBuilder.loadTexts:
    wmanDevCmnEventLogConfigEntry.setStatus("current")


class _WmanDevCmnDeviceIndex_Type(Integer32):
    """Custom type wmanDevCmnDeviceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_WmanDevCmnDeviceIndex_Type.__name__ = "Integer32"
_WmanDevCmnDeviceIndex_Object = MibTableColumn
wmanDevCmnDeviceIndex = _WmanDevCmnDeviceIndex_Object(
    (1, 0, 8802, 16, 1, 1, 3, 1, 1, 1, 1),
    _WmanDevCmnDeviceIndex_Type()
)
wmanDevCmnDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanDevCmnDeviceIndex.setStatus("current")


class _WmanDevCmnEventLogEntryLimit_Type(Integer32):
    """Custom type wmanDevCmnEventLogEntryLimit based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_WmanDevCmnEventLogEntryLimit_Type.__name__ = "Integer32"
_WmanDevCmnEventLogEntryLimit_Object = MibTableColumn
wmanDevCmnEventLogEntryLimit = _WmanDevCmnEventLogEntryLimit_Object(
    (1, 0, 8802, 16, 1, 1, 3, 1, 1, 1, 2),
    _WmanDevCmnEventLogEntryLimit_Type()
)
wmanDevCmnEventLogEntryLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanDevCmnEventLogEntryLimit.setStatus("current")


class _WmanDevCmnEventLifeTimeLimit_Type(Integer32):
    """Custom type wmanDevCmnEventLifeTimeLimit based on Integer32"""
    defaultValue = 1440

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_WmanDevCmnEventLifeTimeLimit_Type.__name__ = "Integer32"
_WmanDevCmnEventLifeTimeLimit_Object = MibTableColumn
wmanDevCmnEventLifeTimeLimit = _WmanDevCmnEventLifeTimeLimit_Object(
    (1, 0, 8802, 16, 1, 1, 3, 1, 1, 1, 3),
    _WmanDevCmnEventLifeTimeLimit_Type()
)
wmanDevCmnEventLifeTimeLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanDevCmnEventLifeTimeLimit.setStatus("current")
if mibBuilder.loadTexts:
    wmanDevCmnEventLifeTimeLimit.setUnits("minutes")


class _WmanDevCmnEventLogEntryLimitPerEventId_Type(Integer32):
    """Custom type wmanDevCmnEventLogEntryLimitPerEventId based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_WmanDevCmnEventLogEntryLimitPerEventId_Type.__name__ = "Integer32"
_WmanDevCmnEventLogEntryLimitPerEventId_Object = MibTableColumn
wmanDevCmnEventLogEntryLimitPerEventId = _WmanDevCmnEventLogEntryLimitPerEventId_Object(
    (1, 0, 8802, 16, 1, 1, 3, 1, 1, 1, 4),
    _WmanDevCmnEventLogEntryLimitPerEventId_Type()
)
wmanDevCmnEventLogEntryLimitPerEventId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanDevCmnEventLogEntryLimitPerEventId.setStatus("current")


class _WmanDevCmnEventLogSeverityThreshold_Type(WmanDevEventSeverity):
    """Custom type wmanDevCmnEventLogSeverityThreshold based on WmanDevEventSeverity"""
    defaultValue = 5


_WmanDevCmnEventLogSeverityThreshold_Type.__name__ = "WmanDevEventSeverity"
_WmanDevCmnEventLogSeverityThreshold_Object = MibTableColumn
wmanDevCmnEventLogSeverityThreshold = _WmanDevCmnEventLogSeverityThreshold_Object(
    (1, 0, 8802, 16, 1, 1, 3, 1, 1, 1, 5),
    _WmanDevCmnEventLogSeverityThreshold_Type()
)
wmanDevCmnEventLogSeverityThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanDevCmnEventLogSeverityThreshold.setStatus("current")


class _WmanDevCmnEventLogWrapAroundBuffEnable_Type(TruthValue):
    """Custom type wmanDevCmnEventLogWrapAroundBuffEnable based on TruthValue"""
    defaultValue = 1


_WmanDevCmnEventLogWrapAroundBuffEnable_Type.__name__ = "TruthValue"
_WmanDevCmnEventLogWrapAroundBuffEnable_Object = MibTableColumn
wmanDevCmnEventLogWrapAroundBuffEnable = _WmanDevCmnEventLogWrapAroundBuffEnable_Object(
    (1, 0, 8802, 16, 1, 1, 3, 1, 1, 1, 6),
    _WmanDevCmnEventLogWrapAroundBuffEnable_Type()
)
wmanDevCmnEventLogWrapAroundBuffEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanDevCmnEventLogWrapAroundBuffEnable.setStatus("current")


class _WmanDevCmnEventLogLatestEvent_Type(Unsigned32):
    """Custom type wmanDevCmnEventLogLatestEvent based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_WmanDevCmnEventLogLatestEvent_Type.__name__ = "Unsigned32"
_WmanDevCmnEventLogLatestEvent_Object = MibTableColumn
wmanDevCmnEventLogLatestEvent = _WmanDevCmnEventLogLatestEvent_Object(
    (1, 0, 8802, 16, 1, 1, 3, 1, 1, 1, 7),
    _WmanDevCmnEventLogLatestEvent_Type()
)
wmanDevCmnEventLogLatestEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanDevCmnEventLogLatestEvent.setStatus("current")
_WmanDevCmnEventLogPersistenceSupported_Type = TruthValue
_WmanDevCmnEventLogPersistenceSupported_Object = MibTableColumn
wmanDevCmnEventLogPersistenceSupported = _WmanDevCmnEventLogPersistenceSupported_Object(
    (1, 0, 8802, 16, 1, 1, 3, 1, 1, 1, 8),
    _WmanDevCmnEventLogPersistenceSupported_Type()
)
wmanDevCmnEventLogPersistenceSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanDevCmnEventLogPersistenceSupported.setStatus("current")


class _WmanDevCmnEventLogResidualBuffThreshold_Type(Integer32):
    """Custom type wmanDevCmnEventLogResidualBuffThreshold based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_WmanDevCmnEventLogResidualBuffThreshold_Type.__name__ = "Integer32"
_WmanDevCmnEventLogResidualBuffThreshold_Object = MibTableColumn
wmanDevCmnEventLogResidualBuffThreshold = _WmanDevCmnEventLogResidualBuffThreshold_Object(
    (1, 0, 8802, 16, 1, 1, 3, 1, 1, 1, 9),
    _WmanDevCmnEventLogResidualBuffThreshold_Type()
)
wmanDevCmnEventLogResidualBuffThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanDevCmnEventLogResidualBuffThreshold.setStatus("current")
_WmanDevCmnEventTable_Object = MibTable
wmanDevCmnEventTable = _WmanDevCmnEventTable_Object(
    (1, 0, 8802, 16, 1, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    wmanDevCmnEventTable.setStatus("current")
_WmanDevCmnEventEntry_Object = MibTableRow
wmanDevCmnEventEntry = _WmanDevCmnEventEntry_Object(
    (1, 0, 8802, 16, 1, 1, 3, 1, 2, 1)
)
wmanDevCmnEventEntry.setIndexNames(
    (0, "WMAN-DEV-MIB", "wmanDevCmnDeviceIndex"),
    (0, "WMAN-DEV-MIB", "wmanDevCmnEventIdentifier"),
)
if mibBuilder.loadTexts:
    wmanDevCmnEventEntry.setStatus("current")


class _WmanDevCmnEventIdentifier_Type(Integer32):
    """Custom type wmanDevCmnEventIdentifier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100000),
    )


_WmanDevCmnEventIdentifier_Type.__name__ = "Integer32"
_WmanDevCmnEventIdentifier_Object = MibTableColumn
wmanDevCmnEventIdentifier = _WmanDevCmnEventIdentifier_Object(
    (1, 0, 8802, 16, 1, 1, 3, 1, 2, 1, 1),
    _WmanDevCmnEventIdentifier_Type()
)
wmanDevCmnEventIdentifier.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wmanDevCmnEventIdentifier.setStatus("current")
_WmanDevCmnEventDescription_Type = SnmpAdminString
_WmanDevCmnEventDescription_Object = MibTableColumn
wmanDevCmnEventDescription = _WmanDevCmnEventDescription_Object(
    (1, 0, 8802, 16, 1, 1, 3, 1, 2, 1, 2),
    _WmanDevCmnEventDescription_Type()
)
wmanDevCmnEventDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanDevCmnEventDescription.setStatus("current")
_WmanDevCmnEventSeverity_Type = WmanDevEventSeverity
_WmanDevCmnEventSeverity_Object = MibTableColumn
wmanDevCmnEventSeverity = _WmanDevCmnEventSeverity_Object(
    (1, 0, 8802, 16, 1, 1, 3, 1, 2, 1, 3),
    _WmanDevCmnEventSeverity_Type()
)
wmanDevCmnEventSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanDevCmnEventSeverity.setStatus("current")


class _WmanDevCmnEventNotification_Type(TruthValue):
    """Custom type wmanDevCmnEventNotification based on TruthValue"""
    defaultValue = 2


_WmanDevCmnEventNotification_Type.__name__ = "TruthValue"
_WmanDevCmnEventNotification_Object = MibTableColumn
wmanDevCmnEventNotification = _WmanDevCmnEventNotification_Object(
    (1, 0, 8802, 16, 1, 1, 3, 1, 2, 1, 4),
    _WmanDevCmnEventNotification_Type()
)
wmanDevCmnEventNotification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanDevCmnEventNotification.setStatus("current")
_WmanDevCmnEventNotificationOid_Type = ObjectIdentifier
_WmanDevCmnEventNotificationOid_Object = MibTableColumn
wmanDevCmnEventNotificationOid = _WmanDevCmnEventNotificationOid_Object(
    (1, 0, 8802, 16, 1, 1, 3, 1, 2, 1, 5),
    _WmanDevCmnEventNotificationOid_Type()
)
wmanDevCmnEventNotificationOid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanDevCmnEventNotificationOid.setStatus("current")
_WmanDevCmnEventLogTable_Object = MibTable
wmanDevCmnEventLogTable = _WmanDevCmnEventLogTable_Object(
    (1, 0, 8802, 16, 1, 1, 3, 1, 3)
)
if mibBuilder.loadTexts:
    wmanDevCmnEventLogTable.setStatus("current")
_WmanDevCmnEventLogEntry_Object = MibTableRow
wmanDevCmnEventLogEntry = _WmanDevCmnEventLogEntry_Object(
    (1, 0, 8802, 16, 1, 1, 3, 1, 3, 1)
)
wmanDevCmnEventLogEntry.setIndexNames(
    (0, "WMAN-DEV-MIB", "wmanDevCmnDeviceIndex"),
    (0, "WMAN-DEV-MIB", "wmanDevCmnEventLogIndex"),
)
if mibBuilder.loadTexts:
    wmanDevCmnEventLogEntry.setStatus("current")


class _WmanDevCmnEventLogIndex_Type(Unsigned32):
    """Custom type wmanDevCmnEventLogIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_WmanDevCmnEventLogIndex_Type.__name__ = "Unsigned32"
_WmanDevCmnEventLogIndex_Object = MibTableColumn
wmanDevCmnEventLogIndex = _WmanDevCmnEventLogIndex_Object(
    (1, 0, 8802, 16, 1, 1, 3, 1, 3, 1, 1),
    _WmanDevCmnEventLogIndex_Type()
)
wmanDevCmnEventLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanDevCmnEventLogIndex.setStatus("current")


class _WmanDevCmnEventId_Type(Integer32):
    """Custom type wmanDevCmnEventId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100000),
    )


_WmanDevCmnEventId_Type.__name__ = "Integer32"
_WmanDevCmnEventId_Object = MibTableColumn
wmanDevCmnEventId = _WmanDevCmnEventId_Object(
    (1, 0, 8802, 16, 1, 1, 3, 1, 3, 1, 2),
    _WmanDevCmnEventId_Type()
)
wmanDevCmnEventId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanDevCmnEventId.setStatus("current")
_WmanDevCmnEventLoggedTime_Type = TimeStamp
_WmanDevCmnEventLoggedTime_Object = MibTableColumn
wmanDevCmnEventLoggedTime = _WmanDevCmnEventLoggedTime_Object(
    (1, 0, 8802, 16, 1, 1, 3, 1, 3, 1, 3),
    _WmanDevCmnEventLoggedTime_Type()
)
wmanDevCmnEventLoggedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanDevCmnEventLoggedTime.setStatus("current")
_WmanDevCmnEventLogDescription_Type = SnmpAdminString
_WmanDevCmnEventLogDescription_Object = MibTableColumn
wmanDevCmnEventLogDescription = _WmanDevCmnEventLogDescription_Object(
    (1, 0, 8802, 16, 1, 1, 3, 1, 3, 1, 4),
    _WmanDevCmnEventLogDescription_Type()
)
wmanDevCmnEventLogDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanDevCmnEventLogDescription.setStatus("current")
_WmanDevCmnEventLogSeverity_Type = WmanDevEventSeverity
_WmanDevCmnEventLogSeverity_Object = MibTableColumn
wmanDevCmnEventLogSeverity = _WmanDevCmnEventLogSeverity_Object(
    (1, 0, 8802, 16, 1, 1, 3, 1, 3, 1, 5),
    _WmanDevCmnEventLogSeverity_Type()
)
wmanDevCmnEventLogSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanDevCmnEventLogSeverity.setStatus("current")
_WmanDevCmnSnmpAgent_ObjectIdentity = ObjectIdentity
wmanDevCmnSnmpAgent = _WmanDevCmnSnmpAgent_ObjectIdentity(
    (1, 0, 8802, 16, 1, 1, 3, 2)
)
_WmanDevCmnSnmpV1V2TrapDestTable_Object = MibTable
wmanDevCmnSnmpV1V2TrapDestTable = _WmanDevCmnSnmpV1V2TrapDestTable_Object(
    (1, 0, 8802, 16, 1, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    wmanDevCmnSnmpV1V2TrapDestTable.setStatus("current")
_WmanDevCmnSnmpV1V2TrapDestEntry_Object = MibTableRow
wmanDevCmnSnmpV1V2TrapDestEntry = _WmanDevCmnSnmpV1V2TrapDestEntry_Object(
    (1, 0, 8802, 16, 1, 1, 3, 2, 1, 1)
)
wmanDevCmnSnmpV1V2TrapDestEntry.setIndexNames(
    (0, "WMAN-DEV-MIB", "wmanDevCmnSnmpV1V2TrapDestIndex"),
)
if mibBuilder.loadTexts:
    wmanDevCmnSnmpV1V2TrapDestEntry.setStatus("current")


class _WmanDevCmnSnmpV1V2TrapDestIndex_Type(Integer32):
    """Custom type wmanDevCmnSnmpV1V2TrapDestIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_WmanDevCmnSnmpV1V2TrapDestIndex_Type.__name__ = "Integer32"
_WmanDevCmnSnmpV1V2TrapDestIndex_Object = MibTableColumn
wmanDevCmnSnmpV1V2TrapDestIndex = _WmanDevCmnSnmpV1V2TrapDestIndex_Object(
    (1, 0, 8802, 16, 1, 1, 3, 2, 1, 1, 1),
    _WmanDevCmnSnmpV1V2TrapDestIndex_Type()
)
wmanDevCmnSnmpV1V2TrapDestIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wmanDevCmnSnmpV1V2TrapDestIndex.setStatus("current")
_WmanDevCmnSnmpV1V2TrapDestIpAddrType_Type = InetAddressType
_WmanDevCmnSnmpV1V2TrapDestIpAddrType_Object = MibTableColumn
wmanDevCmnSnmpV1V2TrapDestIpAddrType = _WmanDevCmnSnmpV1V2TrapDestIpAddrType_Object(
    (1, 0, 8802, 16, 1, 1, 3, 2, 1, 1, 2),
    _WmanDevCmnSnmpV1V2TrapDestIpAddrType_Type()
)
wmanDevCmnSnmpV1V2TrapDestIpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanDevCmnSnmpV1V2TrapDestIpAddrType.setStatus("current")
_WmanDevCmnSnmpV1V2TrapDestIpAddr_Type = InetAddress
_WmanDevCmnSnmpV1V2TrapDestIpAddr_Object = MibTableColumn
wmanDevCmnSnmpV1V2TrapDestIpAddr = _WmanDevCmnSnmpV1V2TrapDestIpAddr_Object(
    (1, 0, 8802, 16, 1, 1, 3, 2, 1, 1, 3),
    _WmanDevCmnSnmpV1V2TrapDestIpAddr_Type()
)
wmanDevCmnSnmpV1V2TrapDestIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanDevCmnSnmpV1V2TrapDestIpAddr.setStatus("current")


class _WmanDevCmnSnmpV1V2TrapDestPort_Type(Integer32):
    """Custom type wmanDevCmnSnmpV1V2TrapDestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanDevCmnSnmpV1V2TrapDestPort_Type.__name__ = "Integer32"
_WmanDevCmnSnmpV1V2TrapDestPort_Object = MibTableColumn
wmanDevCmnSnmpV1V2TrapDestPort = _WmanDevCmnSnmpV1V2TrapDestPort_Object(
    (1, 0, 8802, 16, 1, 1, 3, 2, 1, 1, 4),
    _WmanDevCmnSnmpV1V2TrapDestPort_Type()
)
wmanDevCmnSnmpV1V2TrapDestPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanDevCmnSnmpV1V2TrapDestPort.setStatus("current")
_WmanDevCmnSnmpV1V2TrapDestRowStatus_Type = RowStatus
_WmanDevCmnSnmpV1V2TrapDestRowStatus_Object = MibTableColumn
wmanDevCmnSnmpV1V2TrapDestRowStatus = _WmanDevCmnSnmpV1V2TrapDestRowStatus_Object(
    (1, 0, 8802, 16, 1, 1, 3, 2, 1, 1, 5),
    _WmanDevCmnSnmpV1V2TrapDestRowStatus_Type()
)
wmanDevCmnSnmpV1V2TrapDestRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanDevCmnSnmpV1V2TrapDestRowStatus.setStatus("current")
_WmanDevCmnDeviceConfig_ObjectIdentity = ObjectIdentity
wmanDevCmnDeviceConfig = _WmanDevCmnDeviceConfig_ObjectIdentity(
    (1, 0, 8802, 16, 1, 1, 3, 3)
)


class _WmanDevCmnResetDevice_Type(Integer32):
    """Custom type wmanDevCmnResetDevice based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("actionResetDeviceNoAction", 0),
          ("actionResetDevice", 1))
    )


_WmanDevCmnResetDevice_Type.__name__ = "Integer32"
_WmanDevCmnResetDevice_Object = MibScalar
wmanDevCmnResetDevice = _WmanDevCmnResetDevice_Object(
    (1, 0, 8802, 16, 1, 1, 3, 3, 1),
    _WmanDevCmnResetDevice_Type()
)
wmanDevCmnResetDevice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanDevCmnResetDevice.setStatus("current")
_WmanDevMibConformance_ObjectIdentity = ObjectIdentity
wmanDevMibConformance = _WmanDevMibConformance_ObjectIdentity(
    (1, 0, 8802, 16, 1, 2)
)
_WmanDevMibGroups_ObjectIdentity = ObjectIdentity
wmanDevMibGroups = _WmanDevMibGroups_ObjectIdentity(
    (1, 0, 8802, 16, 1, 2, 1)
)
_WmanDevMibCompliances_ObjectIdentity = ObjectIdentity
wmanDevMibCompliances = _WmanDevMibCompliances_ObjectIdentity(
    (1, 0, 8802, 16, 1, 2, 2)
)

# Managed Objects groups

wmanDevMibBsGroup = ObjectGroup(
    (1, 0, 8802, 16, 1, 2, 1, 1)
)
wmanDevMibBsGroup.setObjects(
    ("WMAN-DEV-MIB", "wmanDevBsTrapControlRegister")
)
if mibBuilder.loadTexts:
    wmanDevMibBsGroup.setStatus("current")

wmanDevMibBsSwUpgradeGroup = ObjectGroup(
    (1, 0, 8802, 16, 1, 2, 1, 2)
)
wmanDevMibBsSwUpgradeGroup.setObjects(
      *(("WMAN-DEV-MIB", "wmanDevBsVendorId"),
        ("WMAN-DEV-MIB", "wmanDevBsHwId"),
        ("WMAN-DEV-MIB", "wmanDevBsCurrentSwVersion"),
        ("WMAN-DEV-MIB", "wmanDevBsDownloadSwVersion"),
        ("WMAN-DEV-MIB", "wmanDevBsUpgradeFileName"),
        ("WMAN-DEV-MIB", "wmanDevBsSoftwareUpgradeAdminState"),
        ("WMAN-DEV-MIB", "wmanDevBsDownloadSwProgress"),
        ("WMAN-DEV-MIB", "wmanDevBsSoftwareUpgradeTimeStamp"))
)
if mibBuilder.loadTexts:
    wmanDevMibBsSwUpgradeGroup.setStatus("current")

wmanDevMibSsGroup = ObjectGroup(
    (1, 0, 8802, 16, 1, 2, 1, 3)
)
wmanDevMibSsGroup.setObjects(
      *(("WMAN-DEV-MIB", "wmanDevSsMicConfigSetting"),
        ("WMAN-DEV-MIB", "wmanDevSsVendorId"),
        ("WMAN-DEV-MIB", "wmanDevSsHwId"),
        ("WMAN-DEV-MIB", "wmanDevSsSwVersion"),
        ("WMAN-DEV-MIB", "wmanDevSsUpgradeFileName"),
        ("WMAN-DEV-MIB", "wmanDevSsSwUpgradeTftpServer"),
        ("WMAN-DEV-MIB", "wmanDevSsTftpServerTimeStamp"),
        ("WMAN-DEV-MIB", "wmanDevSsTrapControlRegister"))
)
if mibBuilder.loadTexts:
    wmanDevMibSsGroup.setStatus("current")

wmanDevMibCmnGroup = ObjectGroup(
    (1, 0, 8802, 16, 1, 2, 1, 4)
)
wmanDevMibCmnGroup.setObjects(
      *(("WMAN-DEV-MIB", "wmanDevCmnSnmpV1V2TrapDestIpAddrType"),
        ("WMAN-DEV-MIB", "wmanDevCmnSnmpV1V2TrapDestIpAddr"),
        ("WMAN-DEV-MIB", "wmanDevCmnSnmpV1V2TrapDestPort"),
        ("WMAN-DEV-MIB", "wmanDevCmnSnmpV1V2TrapDestRowStatus"),
        ("WMAN-DEV-MIB", "wmanDevCmnResetDevice"),
        ("WMAN-DEV-MIB", "wmanDevCmnDeviceIndex"),
        ("WMAN-DEV-MIB", "wmanDevCmnEventLogEntryLimit"),
        ("WMAN-DEV-MIB", "wmanDevCmnEventLifeTimeLimit"),
        ("WMAN-DEV-MIB", "wmanDevCmnEventLogEntryLimitPerEventId"),
        ("WMAN-DEV-MIB", "wmanDevCmnEventLogSeverityThreshold"),
        ("WMAN-DEV-MIB", "wmanDevCmnEventLogWrapAroundBuffEnable"),
        ("WMAN-DEV-MIB", "wmanDevCmnEventLogLatestEvent"),
        ("WMAN-DEV-MIB", "wmanDevCmnEventLogPersistenceSupported"),
        ("WMAN-DEV-MIB", "wmanDevCmnEventLogResidualBuffThreshold"),
        ("WMAN-DEV-MIB", "wmanDevCmnEventDescription"),
        ("WMAN-DEV-MIB", "wmanDevCmnEventSeverity"),
        ("WMAN-DEV-MIB", "wmanDevCmnEventNotification"),
        ("WMAN-DEV-MIB", "wmanDevCmnEventNotificationOid"),
        ("WMAN-DEV-MIB", "wmanDevCmnEventLogIndex"),
        ("WMAN-DEV-MIB", "wmanDevCmnEventId"),
        ("WMAN-DEV-MIB", "wmanDevCmnEventLoggedTime"),
        ("WMAN-DEV-MIB", "wmanDevCmnEventLogDescription"),
        ("WMAN-DEV-MIB", "wmanDevCmnEventLogSeverity"))
)
if mibBuilder.loadTexts:
    wmanDevMibCmnGroup.setStatus("current")


# Notification objects

wmanDevBsEventTrap = NotificationType(
    (1, 0, 8802, 16, 1, 1, 1, 2, 2, 0, 1)
)
wmanDevBsEventTrap.setObjects(
      *(("WMAN-DEV-MIB", "wmanDevCmnEventId"),
        ("WMAN-DEV-MIB", "wmanDevCmnEventLogIndex"),
        ("WMAN-DEV-MIB", "wmanDevCmnEventLoggedTime"),
        ("WMAN-DEV-MIB", "wmanDevCmnEventDescription"),
        ("WMAN-DEV-MIB", "wmanDevCmnEventSeverity"))
)
if mibBuilder.loadTexts:
    wmanDevBsEventTrap.setStatus(
        "current"
    )

wmanDevBsLogBuffExceedThresholdTrap = NotificationType(
    (1, 0, 8802, 16, 1, 1, 1, 2, 2, 0, 2)
)
wmanDevBsLogBuffExceedThresholdTrap.setObjects(
      *(("WMAN-DEV-MIB", "wmanDevCmnEventId"),
        ("WMAN-DEV-MIB", "wmanDevCmnEventLogResidualBuffThreshold"))
)
if mibBuilder.loadTexts:
    wmanDevBsLogBuffExceedThresholdTrap.setStatus(
        "current"
    )

wmanDevSsEventTrap = NotificationType(
    (1, 0, 8802, 16, 1, 1, 2, 2, 2, 0, 1)
)
wmanDevSsEventTrap.setObjects(
      *(("WMAN-DEV-MIB", "wmanDevCmnEventId"),
        ("WMAN-DEV-MIB", "wmanDevCmnEventLogIndex"),
        ("WMAN-DEV-MIB", "wmanDevCmnEventLoggedTime"),
        ("WMAN-DEV-MIB", "wmanDevCmnEventDescription"),
        ("WMAN-DEV-MIB", "wmanDevCmnEventSeverity"))
)
if mibBuilder.loadTexts:
    wmanDevSsEventTrap.setStatus(
        "current"
    )

wmanDevSsLogBufferExceedThresholdTrap = NotificationType(
    (1, 0, 8802, 16, 1, 1, 2, 2, 2, 0, 2)
)
wmanDevSsLogBufferExceedThresholdTrap.setObjects(
      *(("WMAN-DEV-MIB", "wmanDevCmnEventId"),
        ("WMAN-DEV-MIB", "wmanDevCmnEventLogResidualBuffThreshold"))
)
if mibBuilder.loadTexts:
    wmanDevSsLogBufferExceedThresholdTrap.setStatus(
        "current"
    )


# Notifications groups

wmanDevMibBsNotificationGroup = NotificationGroup(
    (1, 0, 8802, 16, 1, 2, 1, 5)
)
wmanDevMibBsNotificationGroup.setObjects(
      *(("WMAN-DEV-MIB", "wmanDevBsEventTrap"),
        ("WMAN-DEV-MIB", "wmanDevBsLogBuffExceedThresholdTrap"))
)
if mibBuilder.loadTexts:
    wmanDevMibBsNotificationGroup.setStatus(
        "current"
    )

wmanDevMibSsNotificationGroup = NotificationGroup(
    (1, 0, 8802, 16, 1, 2, 1, 6)
)
wmanDevMibSsNotificationGroup.setObjects(
      *(("WMAN-DEV-MIB", "wmanDevSsEventTrap"),
        ("WMAN-DEV-MIB", "wmanDevSsLogBufferExceedThresholdTrap"))
)
if mibBuilder.loadTexts:
    wmanDevMibSsNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

wmanDevMibCompliance = ModuleCompliance(
    (1, 0, 8802, 16, 1, 2, 2, 1)
)
wmanDevMibCompliance.setObjects(
      *(("WMAN-DEV-MIB", "wmanDevMibBsGroup"),
        ("WMAN-DEV-MIB", "wmanDevMibBsSwUpgradeGroup"),
        ("WMAN-DEV-MIB", "wmanDevMibSsGroup"),
        ("WMAN-DEV-MIB", "wmanDevMibCmnGroup"),
        ("WMAN-DEV-MIB", "wmanDevMibBsNotificationGroup"),
        ("WMAN-DEV-MIB", "wmanDevMibSsNotificationGroup"))
)
if mibBuilder.loadTexts:
    wmanDevMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WMAN-DEV-MIB",
    **{"WmanDevEventSeverity": WmanDevEventSeverity,
       "wmanDevMib": wmanDevMib,
       "wmanDevMibObjects": wmanDevMibObjects,
       "wmanDevBsObjects": wmanDevBsObjects,
       "wmanDevBsSoftwareUpgradeTable": wmanDevBsSoftwareUpgradeTable,
       "wmanDevBsSoftwareUpgradeEntry": wmanDevBsSoftwareUpgradeEntry,
       "wmanDevBsDeviceIndex": wmanDevBsDeviceIndex,
       "wmanDevBsVendorId": wmanDevBsVendorId,
       "wmanDevBsHwId": wmanDevBsHwId,
       "wmanDevBsCurrentSwVersion": wmanDevBsCurrentSwVersion,
       "wmanDevBsDownloadSwVersion": wmanDevBsDownloadSwVersion,
       "wmanDevBsUpgradeFileName": wmanDevBsUpgradeFileName,
       "wmanDevBsSoftwareUpgradeAdminState": wmanDevBsSoftwareUpgradeAdminState,
       "wmanDevBsDownloadSwProgress": wmanDevBsDownloadSwProgress,
       "wmanDevBsSoftwareUpgradeTimeStamp": wmanDevBsSoftwareUpgradeTimeStamp,
       "wmanDevBsNotification": wmanDevBsNotification,
       "wmanDevBsTrapControl": wmanDevBsTrapControl,
       "wmanDevBsTrapControlRegister": wmanDevBsTrapControlRegister,
       "wmanDevBsTrapDefinition": wmanDevBsTrapDefinition,
       "wmanDevBsTrapPrefix": wmanDevBsTrapPrefix,
       "wmanDevBsEventTrap": wmanDevBsEventTrap,
       "wmanDevBsLogBuffExceedThresholdTrap": wmanDevBsLogBuffExceedThresholdTrap,
       "wmanDevSsObjects": wmanDevSsObjects,
       "wmanDevSsConfigFileEncodingTable": wmanDevSsConfigFileEncodingTable,
       "wmanDevSsConfigFileEncodingEntry": wmanDevSsConfigFileEncodingEntry,
       "wmanDevSsDeviceIndex": wmanDevSsDeviceIndex,
       "wmanDevSsMicConfigSetting": wmanDevSsMicConfigSetting,
       "wmanDevSsVendorId": wmanDevSsVendorId,
       "wmanDevSsHwId": wmanDevSsHwId,
       "wmanDevSsSwVersion": wmanDevSsSwVersion,
       "wmanDevSsUpgradeFileName": wmanDevSsUpgradeFileName,
       "wmanDevSsSwUpgradeTftpServer": wmanDevSsSwUpgradeTftpServer,
       "wmanDevSsTftpServerTimeStamp": wmanDevSsTftpServerTimeStamp,
       "wmanDevSsNotification": wmanDevSsNotification,
       "wmanDevSsTrapControl": wmanDevSsTrapControl,
       "wmanDevSsTrapControlRegister": wmanDevSsTrapControlRegister,
       "wmanDevSsTrapDefinitions": wmanDevSsTrapDefinitions,
       "wmanDevSsTrapPrefix": wmanDevSsTrapPrefix,
       "wmanDevSsEventTrap": wmanDevSsEventTrap,
       "wmanDevSsLogBufferExceedThresholdTrap": wmanDevSsLogBufferExceedThresholdTrap,
       "wmanDevCommonObjects": wmanDevCommonObjects,
       "wmanDevCmnEventLog": wmanDevCmnEventLog,
       "wmanDevCmnEventLogConfigTable": wmanDevCmnEventLogConfigTable,
       "wmanDevCmnEventLogConfigEntry": wmanDevCmnEventLogConfigEntry,
       "wmanDevCmnDeviceIndex": wmanDevCmnDeviceIndex,
       "wmanDevCmnEventLogEntryLimit": wmanDevCmnEventLogEntryLimit,
       "wmanDevCmnEventLifeTimeLimit": wmanDevCmnEventLifeTimeLimit,
       "wmanDevCmnEventLogEntryLimitPerEventId": wmanDevCmnEventLogEntryLimitPerEventId,
       "wmanDevCmnEventLogSeverityThreshold": wmanDevCmnEventLogSeverityThreshold,
       "wmanDevCmnEventLogWrapAroundBuffEnable": wmanDevCmnEventLogWrapAroundBuffEnable,
       "wmanDevCmnEventLogLatestEvent": wmanDevCmnEventLogLatestEvent,
       "wmanDevCmnEventLogPersistenceSupported": wmanDevCmnEventLogPersistenceSupported,
       "wmanDevCmnEventLogResidualBuffThreshold": wmanDevCmnEventLogResidualBuffThreshold,
       "wmanDevCmnEventTable": wmanDevCmnEventTable,
       "wmanDevCmnEventEntry": wmanDevCmnEventEntry,
       "wmanDevCmnEventIdentifier": wmanDevCmnEventIdentifier,
       "wmanDevCmnEventDescription": wmanDevCmnEventDescription,
       "wmanDevCmnEventSeverity": wmanDevCmnEventSeverity,
       "wmanDevCmnEventNotification": wmanDevCmnEventNotification,
       "wmanDevCmnEventNotificationOid": wmanDevCmnEventNotificationOid,
       "wmanDevCmnEventLogTable": wmanDevCmnEventLogTable,
       "wmanDevCmnEventLogEntry": wmanDevCmnEventLogEntry,
       "wmanDevCmnEventLogIndex": wmanDevCmnEventLogIndex,
       "wmanDevCmnEventId": wmanDevCmnEventId,
       "wmanDevCmnEventLoggedTime": wmanDevCmnEventLoggedTime,
       "wmanDevCmnEventLogDescription": wmanDevCmnEventLogDescription,
       "wmanDevCmnEventLogSeverity": wmanDevCmnEventLogSeverity,
       "wmanDevCmnSnmpAgent": wmanDevCmnSnmpAgent,
       "wmanDevCmnSnmpV1V2TrapDestTable": wmanDevCmnSnmpV1V2TrapDestTable,
       "wmanDevCmnSnmpV1V2TrapDestEntry": wmanDevCmnSnmpV1V2TrapDestEntry,
       "wmanDevCmnSnmpV1V2TrapDestIndex": wmanDevCmnSnmpV1V2TrapDestIndex,
       "wmanDevCmnSnmpV1V2TrapDestIpAddrType": wmanDevCmnSnmpV1V2TrapDestIpAddrType,
       "wmanDevCmnSnmpV1V2TrapDestIpAddr": wmanDevCmnSnmpV1V2TrapDestIpAddr,
       "wmanDevCmnSnmpV1V2TrapDestPort": wmanDevCmnSnmpV1V2TrapDestPort,
       "wmanDevCmnSnmpV1V2TrapDestRowStatus": wmanDevCmnSnmpV1V2TrapDestRowStatus,
       "wmanDevCmnDeviceConfig": wmanDevCmnDeviceConfig,
       "wmanDevCmnResetDevice": wmanDevCmnResetDevice,
       "wmanDevMibConformance": wmanDevMibConformance,
       "wmanDevMibGroups": wmanDevMibGroups,
       "wmanDevMibBsGroup": wmanDevMibBsGroup,
       "wmanDevMibBsSwUpgradeGroup": wmanDevMibBsSwUpgradeGroup,
       "wmanDevMibSsGroup": wmanDevMibSsGroup,
       "wmanDevMibCmnGroup": wmanDevMibCmnGroup,
       "wmanDevMibBsNotificationGroup": wmanDevMibBsNotificationGroup,
       "wmanDevMibSsNotificationGroup": wmanDevMibSsNotificationGroup,
       "wmanDevMibCompliances": wmanDevMibCompliances,
       "wmanDevMibCompliance": wmanDevMibCompliance}
)
