# SNMP MIB module (CISCO-LWAPP-DOWNLOAD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-LWAPP-DOWNLOAD-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:55:04 2025
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

(cLApSysMacAddress,
 ciscoLwappApMIB) = mibBuilder.importSymbols(
    "CISCO-LWAPP-AP-MIB",
    "cLApSysMacAddress",
    "ciscoLwappApMIB")

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
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TruthValue")


# MODULE-IDENTITY

ciscoLwappDownloadMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 4)
)
if mibBuilder.loadTexts:
    ciscoLwappDownloadMIB.setRevisions(
        ("2017-05-23 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoLwappDownloadMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoLwappDownloadMIBNotifs = _CiscoLwappDownloadMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 4, 0)
)
_CiscoLwappDownloadMIBObjects_ObjectIdentity = ObjectIdentity
ciscoLwappDownloadMIBObjects = _CiscoLwappDownloadMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 4, 1)
)
_CiscoLwappDLApBoot_ObjectIdentity = ObjectIdentity
ciscoLwappDLApBoot = _CiscoLwappDLApBoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 4, 1, 1)
)
_ClDLApBootTable_Object = MibTable
clDLApBootTable = _ClDLApBootTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 4, 1, 1, 1)
)
if mibBuilder.loadTexts:
    clDLApBootTable.setStatus("current")
_CldlApBootEntry_Object = MibTableRow
cldlApBootEntry = _CldlApBootEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 4, 1, 1, 1, 1)
)
cldlApBootEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
)
if mibBuilder.loadTexts:
    cldlApBootEntry.setStatus("current")
_CldlAPName_Type = SnmpAdminString
_CldlAPName_Object = MibTableColumn
cldlAPName = _CldlAPName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 4, 1, 1, 1, 1, 1),
    _CldlAPName_Type()
)
cldlAPName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldlAPName.setStatus("current")
_CldlAPPrimaryVersion_Type = SnmpAdminString
_CldlAPPrimaryVersion_Object = MibTableColumn
cldlAPPrimaryVersion = _CldlAPPrimaryVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 4, 1, 1, 1, 1, 2),
    _CldlAPPrimaryVersion_Type()
)
cldlAPPrimaryVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldlAPPrimaryVersion.setStatus("current")
_CldlAPBackupVersion_Type = SnmpAdminString
_CldlAPBackupVersion_Object = MibTableColumn
cldlAPBackupVersion = _CldlAPBackupVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 4, 1, 1, 1, 1, 3),
    _CldlAPBackupVersion_Type()
)
cldlAPBackupVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldlAPBackupVersion.setStatus("current")


class _CldlAPSwapImage_Type(TruthValue):
    """Custom type cldlAPSwapImage based on TruthValue"""
    defaultValue = 2


_CldlAPSwapImage_Type.__name__ = "TruthValue"
_CldlAPSwapImage_Object = MibTableColumn
cldlAPSwapImage = _CldlAPSwapImage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 4, 1, 1, 1, 1, 4),
    _CldlAPSwapImage_Type()
)
cldlAPSwapImage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cldlAPSwapImage.setStatus("current")


class _CldlAPDownloadImage_Type(Integer32):
    """Custom type cldlAPDownloadImage based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("backup", 2),
          ("abort", 3))
    )


_CldlAPDownloadImage_Type.__name__ = "Integer32"
_CldlAPDownloadImage_Object = MibTableColumn
cldlAPDownloadImage = _CldlAPDownloadImage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 4, 1, 1, 1, 1, 5),
    _CldlAPDownloadImage_Type()
)
cldlAPDownloadImage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cldlAPDownloadImage.setStatus("current")
_CldlPreDownloadVersion_Type = SnmpAdminString
_CldlPreDownloadVersion_Object = MibTableColumn
cldlPreDownloadVersion = _CldlPreDownloadVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 4, 1, 1, 1, 1, 6),
    _CldlPreDownloadVersion_Type()
)
cldlPreDownloadVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldlPreDownloadVersion.setStatus("current")


class _CldlPreDownloadStatus_Type(Integer32):
    """Custom type cldlPreDownloadStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("intiated", 2),
          ("preDownloading", 3),
          ("completed", 4),
          ("failed", 5),
          ("notSupported", 6))
    )


_CldlPreDownloadStatus_Type.__name__ = "Integer32"
_CldlPreDownloadStatus_Object = MibTableColumn
cldlPreDownloadStatus = _CldlPreDownloadStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 4, 1, 1, 1, 1, 7),
    _CldlPreDownloadStatus_Type()
)
cldlPreDownloadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldlPreDownloadStatus.setStatus("current")
_CldlPreDownloadNextRetryTime_Type = TimeInterval
_CldlPreDownloadNextRetryTime_Object = MibTableColumn
cldlPreDownloadNextRetryTime = _CldlPreDownloadNextRetryTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 4, 1, 1, 1, 1, 8),
    _CldlPreDownloadNextRetryTime_Type()
)
cldlPreDownloadNextRetryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldlPreDownloadNextRetryTime.setStatus("current")
if mibBuilder.loadTexts:
    cldlPreDownloadNextRetryTime.setUnits("seconds")
_CldlPreDownloadRetryCount_Type = Unsigned32
_CldlPreDownloadRetryCount_Object = MibTableColumn
cldlPreDownloadRetryCount = _CldlPreDownloadRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 4, 1, 1, 1, 1, 9),
    _CldlPreDownloadRetryCount_Type()
)
cldlPreDownloadRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldlPreDownloadRetryCount.setStatus("current")


class _CldlPredownloadImageUpgradeRole_Type(Integer32):
    """Custom type cldlPredownloadImageUpgradeRole based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("masterCentral", 1),
          ("masterLocal", 2),
          ("slaveCentral", 3),
          ("slaveLocal", 4),
          ("unknown", 5))
    )


_CldlPredownloadImageUpgradeRole_Type.__name__ = "Integer32"
_CldlPredownloadImageUpgradeRole_Object = MibTableColumn
cldlPredownloadImageUpgradeRole = _CldlPredownloadImageUpgradeRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 4, 1, 1, 1, 1, 10),
    _CldlPredownloadImageUpgradeRole_Type()
)
cldlPredownloadImageUpgradeRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldlPredownloadImageUpgradeRole.setStatus("current")
_CldlAPSoftwareName_Type = SnmpAdminString
_CldlAPSoftwareName_Object = MibTableColumn
cldlAPSoftwareName = _CldlAPSoftwareName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 4, 1, 1, 1, 1, 11),
    _CldlAPSoftwareName_Type()
)
cldlAPSoftwareName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldlAPSoftwareName.setStatus("current")
_CiscoLwappDLReset_ObjectIdentity = ObjectIdentity
ciscoLwappDLReset = _CiscoLwappDLReset_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 4, 1, 2)
)
_ClDLResetTable_Object = MibTable
clDLResetTable = _ClDLResetTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 4, 1, 2, 1)
)
if mibBuilder.loadTexts:
    clDLResetTable.setStatus("current")
_CldlResetEntry_Object = MibTableRow
cldlResetEntry = _CldlResetEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 4, 1, 2, 1, 1)
)
cldlResetEntry.setIndexNames(
    (0, "CISCO-LWAPP-DOWNLOAD-MIB", "cldlResetIndex"),
)
if mibBuilder.loadTexts:
    cldlResetEntry.setStatus("current")
_CldlResetIndex_Type = Unsigned32
_CldlResetIndex_Object = MibTableColumn
cldlResetIndex = _CldlResetIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 4, 1, 2, 1, 1, 1),
    _CldlResetIndex_Type()
)
cldlResetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cldlResetIndex.setStatus("current")
_CldlResetDateAndTime_Type = DateAndTime
_CldlResetDateAndTime_Object = MibTableColumn
cldlResetDateAndTime = _CldlResetDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 4, 1, 2, 1, 1, 2),
    _CldlResetDateAndTime_Type()
)
cldlResetDateAndTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cldlResetDateAndTime.setStatus("current")


class _CldlResetSwapImage_Type(TruthValue):
    """Custom type cldlResetSwapImage based on TruthValue"""
    defaultValue = 2


_CldlResetSwapImage_Type.__name__ = "TruthValue"
_CldlResetSwapImage_Object = MibTableColumn
cldlResetSwapImage = _CldlResetSwapImage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 4, 1, 2, 1, 1, 3),
    _CldlResetSwapImage_Type()
)
cldlResetSwapImage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cldlResetSwapImage.setStatus("current")


class _CldlResetAP_Type(TruthValue):
    """Custom type cldlResetAP based on TruthValue"""
    defaultValue = 2


_CldlResetAP_Type.__name__ = "TruthValue"
_CldlResetAP_Object = MibTableColumn
cldlResetAP = _CldlResetAP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 4, 1, 2, 1, 1, 4),
    _CldlResetAP_Type()
)
cldlResetAP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cldlResetAP.setStatus("current")
_CldlResetRowStatus_Type = RowStatus
_CldlResetRowStatus_Object = MibTableColumn
cldlResetRowStatus = _CldlResetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 4, 1, 2, 1, 1, 5),
    _CldlResetRowStatus_Type()
)
cldlResetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cldlResetRowStatus.setStatus("current")


class _CldlResetSaveConfig_Type(TruthValue):
    """Custom type cldlResetSaveConfig based on TruthValue"""
    defaultValue = 1


_CldlResetSaveConfig_Type.__name__ = "TruthValue"
_CldlResetSaveConfig_Object = MibTableColumn
cldlResetSaveConfig = _CldlResetSaveConfig_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 4, 1, 2, 1, 1, 6),
    _CldlResetSaveConfig_Type()
)
cldlResetSaveConfig.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cldlResetSaveConfig.setStatus("current")


class _CldlResetAlertTime_Type(Unsigned32):
    """Custom type cldlResetAlertTime based on Unsigned32"""
    defaultValue = 0


_CldlResetAlertTime_Type.__name__ = "Unsigned32"
_CldlResetAlertTime_Object = MibTableColumn
cldlResetAlertTime = _CldlResetAlertTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 4, 1, 2, 1, 1, 7),
    _CldlResetAlertTime_Type()
)
cldlResetAlertTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cldlResetAlertTime.setStatus("current")
if mibBuilder.loadTexts:
    cldlResetAlertTime.setUnits("seconds")


class _CldlResetBootImage_Type(Integer32):
    """Custom type cldlResetBootImage based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("backup", 2))
    )


_CldlResetBootImage_Type.__name__ = "Integer32"
_CldlResetBootImage_Object = MibScalar
cldlResetBootImage = _CldlResetBootImage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 4, 1, 2, 2),
    _CldlResetBootImage_Type()
)
cldlResetBootImage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cldlResetBootImage.setStatus("current")
_CiscoLwappDLRestart_ObjectIdentity = ObjectIdentity
ciscoLwappDLRestart = _CiscoLwappDLRestart_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 4, 1, 3)
)
_ClDLRestartTable_Object = MibTable
clDLRestartTable = _ClDLRestartTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 4, 1, 3, 1)
)
if mibBuilder.loadTexts:
    clDLRestartTable.setStatus("current")
_CldlRestartEntry_Object = MibTableRow
cldlRestartEntry = _CldlRestartEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 4, 1, 3, 1, 1)
)
cldlRestartEntry.setIndexNames(
    (0, "CISCO-LWAPP-DOWNLOAD-MIB", "cldlRestartIndex"),
)
if mibBuilder.loadTexts:
    cldlRestartEntry.setStatus("current")
_CldlRestartIndex_Type = Unsigned32
_CldlRestartIndex_Object = MibTableColumn
cldlRestartIndex = _CldlRestartIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 4, 1, 3, 1, 1, 1),
    _CldlRestartIndex_Type()
)
cldlRestartIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cldlRestartIndex.setStatus("current")
_CldlRestartDateAndTime_Type = DateAndTime
_CldlRestartDateAndTime_Object = MibTableColumn
cldlRestartDateAndTime = _CldlRestartDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 4, 1, 3, 1, 1, 2),
    _CldlRestartDateAndTime_Type()
)
cldlRestartDateAndTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cldlRestartDateAndTime.setStatus("current")


class _CldlRestartAP_Type(TruthValue):
    """Custom type cldlRestartAP based on TruthValue"""
    defaultValue = 2


_CldlRestartAP_Type.__name__ = "TruthValue"
_CldlRestartAP_Object = MibTableColumn
cldlRestartAP = _CldlRestartAP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 4, 1, 3, 1, 1, 3),
    _CldlRestartAP_Type()
)
cldlRestartAP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cldlRestartAP.setStatus("current")
_CldlRestartRowStatus_Type = RowStatus
_CldlRestartRowStatus_Object = MibTableColumn
cldlRestartRowStatus = _CldlRestartRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 4, 1, 3, 1, 1, 4),
    _CldlRestartRowStatus_Type()
)
cldlRestartRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cldlRestartRowStatus.setStatus("current")


class _CldlRestartSaveConfig_Type(TruthValue):
    """Custom type cldlRestartSaveConfig based on TruthValue"""
    defaultValue = 1


_CldlRestartSaveConfig_Type.__name__ = "TruthValue"
_CldlRestartSaveConfig_Object = MibTableColumn
cldlRestartSaveConfig = _CldlRestartSaveConfig_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 4, 1, 3, 1, 1, 5),
    _CldlRestartSaveConfig_Type()
)
cldlRestartSaveConfig.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cldlRestartSaveConfig.setStatus("current")
_CldlRestartAlertTime_Type = Unsigned32
_CldlRestartAlertTime_Object = MibTableColumn
cldlRestartAlertTime = _CldlRestartAlertTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 4, 1, 3, 1, 1, 6),
    _CldlRestartAlertTime_Type()
)
cldlRestartAlertTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cldlRestartAlertTime.setStatus("current")
if mibBuilder.loadTexts:
    cldlRestartAlertTime.setUnits("seconds")
_CiscoLwappDownloadMIBConform_ObjectIdentity = ObjectIdentity
ciscoLwappDownloadMIBConform = _CiscoLwappDownloadMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 4, 2)
)
_CldlMIBCompliances_ObjectIdentity = ObjectIdentity
cldlMIBCompliances = _CldlMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 4, 2, 1)
)
_CldlMIBGroups_ObjectIdentity = ObjectIdentity
cldlMIBGroups = _CldlMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 4, 2, 2)
)

# Managed Objects groups

cldlApGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 4, 2, 2, 1)
)
cldlApGroup.setObjects(
      *(("CISCO-LWAPP-DOWNLOAD-MIB", "cldlAPName"),
        ("CISCO-LWAPP-DOWNLOAD-MIB", "cldlAPPrimaryVersion"),
        ("CISCO-LWAPP-DOWNLOAD-MIB", "cldlAPBackupVersion"),
        ("CISCO-LWAPP-DOWNLOAD-MIB", "cldlAPSwapImage"),
        ("CISCO-LWAPP-DOWNLOAD-MIB", "cldlAPDownloadImage"),
        ("CISCO-LWAPP-DOWNLOAD-MIB", "cldlPreDownloadVersion"),
        ("CISCO-LWAPP-DOWNLOAD-MIB", "cldlPreDownloadStatus"),
        ("CISCO-LWAPP-DOWNLOAD-MIB", "cldlPreDownloadNextRetryTime"),
        ("CISCO-LWAPP-DOWNLOAD-MIB", "cldlPreDownloadRetryCount"),
        ("CISCO-LWAPP-DOWNLOAD-MIB", "cldlPredownloadImageUpgradeRole"),
        ("CISCO-LWAPP-DOWNLOAD-MIB", "cldlAPSoftwareName"))
)
if mibBuilder.loadTexts:
    cldlApGroup.setStatus("current")

cldlResetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 4, 2, 2, 2)
)
cldlResetGroup.setObjects(
      *(("CISCO-LWAPP-DOWNLOAD-MIB", "cldlResetDateAndTime"),
        ("CISCO-LWAPP-DOWNLOAD-MIB", "cldlResetSwapImage"),
        ("CISCO-LWAPP-DOWNLOAD-MIB", "cldlResetAP"),
        ("CISCO-LWAPP-DOWNLOAD-MIB", "cldlResetRowStatus"),
        ("CISCO-LWAPP-DOWNLOAD-MIB", "cldlResetSaveConfig"),
        ("CISCO-LWAPP-DOWNLOAD-MIB", "cldlResetAlertTime"),
        ("CISCO-LWAPP-DOWNLOAD-MIB", "cldlResetDateAndTime"),
        ("CISCO-LWAPP-DOWNLOAD-MIB", "cldlResetSwapImage"),
        ("CISCO-LWAPP-DOWNLOAD-MIB", "cldlResetAP"),
        ("CISCO-LWAPP-DOWNLOAD-MIB", "cldlResetRowStatus"),
        ("CISCO-LWAPP-DOWNLOAD-MIB", "cldlResetSaveConfig"),
        ("CISCO-LWAPP-DOWNLOAD-MIB", "cldlResetBootImage"))
)
if mibBuilder.loadTexts:
    cldlResetGroup.setStatus("current")

cldlRestartGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 4, 2, 2, 3)
)
cldlRestartGroup.setObjects(
      *(("CISCO-LWAPP-DOWNLOAD-MIB", "cldlRestartDateAndTime"),
        ("CISCO-LWAPP-DOWNLOAD-MIB", "cldlRestartAP"),
        ("CISCO-LWAPP-DOWNLOAD-MIB", "cldlRestartRowStatus"),
        ("CISCO-LWAPP-DOWNLOAD-MIB", "cldlRestartSaveConfig"),
        ("CISCO-LWAPP-DOWNLOAD-MIB", "cldlRestartAlertTime"))
)
if mibBuilder.loadTexts:
    cldlRestartGroup.setStatus("current")


# Notification objects

cldlScheduledResetNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 4, 0, 1)
)
cldlScheduledResetNotif.setObjects(
    ("CISCO-LWAPP-DOWNLOAD-MIB", "cldlResetAlertTime")
)
if mibBuilder.loadTexts:
    cldlScheduledResetNotif.setStatus(
        "current"
    )

cldlResetFailedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 4, 0, 2)
)
if mibBuilder.loadTexts:
    cldlResetFailedNotif.setStatus(
        "current"
    )

cldlClearResetNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 4, 0, 3)
)
if mibBuilder.loadTexts:
    cldlClearResetNotif.setStatus(
        "current"
    )


# Notifications groups

cldlNotifsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 4, 2, 2, 4)
)
cldlNotifsGroup.setObjects(
      *(("CISCO-LWAPP-DOWNLOAD-MIB", "cldlScheduledResetNotif"),
        ("CISCO-LWAPP-DOWNLOAD-MIB", "cldlResetFailedNotif"),
        ("CISCO-LWAPP-DOWNLOAD-MIB", "cldlClearResetNotif"))
)
if mibBuilder.loadTexts:
    cldlNotifsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cldlMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 4, 2, 1, 1)
)
cldlMIBCompliance.setObjects(
      *(("CISCO-LWAPP-DOWNLOAD-MIB", "cldlApGroup"),
        ("CISCO-LWAPP-DOWNLOAD-MIB", "cldlResetGroup"),
        ("CISCO-LWAPP-DOWNLOAD-MIB", "cldlNotifsGroup"),
        ("CISCO-LWAPP-DOWNLOAD-MIB", "cldlRestartGroup"))
)
if mibBuilder.loadTexts:
    cldlMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-LWAPP-DOWNLOAD-MIB",
    **{"ciscoLwappDownloadMIB": ciscoLwappDownloadMIB,
       "ciscoLwappDownloadMIBNotifs": ciscoLwappDownloadMIBNotifs,
       "cldlScheduledResetNotif": cldlScheduledResetNotif,
       "cldlResetFailedNotif": cldlResetFailedNotif,
       "cldlClearResetNotif": cldlClearResetNotif,
       "ciscoLwappDownloadMIBObjects": ciscoLwappDownloadMIBObjects,
       "ciscoLwappDLApBoot": ciscoLwappDLApBoot,
       "clDLApBootTable": clDLApBootTable,
       "cldlApBootEntry": cldlApBootEntry,
       "cldlAPName": cldlAPName,
       "cldlAPPrimaryVersion": cldlAPPrimaryVersion,
       "cldlAPBackupVersion": cldlAPBackupVersion,
       "cldlAPSwapImage": cldlAPSwapImage,
       "cldlAPDownloadImage": cldlAPDownloadImage,
       "cldlPreDownloadVersion": cldlPreDownloadVersion,
       "cldlPreDownloadStatus": cldlPreDownloadStatus,
       "cldlPreDownloadNextRetryTime": cldlPreDownloadNextRetryTime,
       "cldlPreDownloadRetryCount": cldlPreDownloadRetryCount,
       "cldlPredownloadImageUpgradeRole": cldlPredownloadImageUpgradeRole,
       "cldlAPSoftwareName": cldlAPSoftwareName,
       "ciscoLwappDLReset": ciscoLwappDLReset,
       "clDLResetTable": clDLResetTable,
       "cldlResetEntry": cldlResetEntry,
       "cldlResetIndex": cldlResetIndex,
       "cldlResetDateAndTime": cldlResetDateAndTime,
       "cldlResetSwapImage": cldlResetSwapImage,
       "cldlResetAP": cldlResetAP,
       "cldlResetRowStatus": cldlResetRowStatus,
       "cldlResetSaveConfig": cldlResetSaveConfig,
       "cldlResetAlertTime": cldlResetAlertTime,
       "cldlResetBootImage": cldlResetBootImage,
       "ciscoLwappDLRestart": ciscoLwappDLRestart,
       "clDLRestartTable": clDLRestartTable,
       "cldlRestartEntry": cldlRestartEntry,
       "cldlRestartIndex": cldlRestartIndex,
       "cldlRestartDateAndTime": cldlRestartDateAndTime,
       "cldlRestartAP": cldlRestartAP,
       "cldlRestartRowStatus": cldlRestartRowStatus,
       "cldlRestartSaveConfig": cldlRestartSaveConfig,
       "cldlRestartAlertTime": cldlRestartAlertTime,
       "ciscoLwappDownloadMIBConform": ciscoLwappDownloadMIBConform,
       "cldlMIBCompliances": cldlMIBCompliances,
       "cldlMIBCompliance": cldlMIBCompliance,
       "cldlMIBGroups": cldlMIBGroups,
       "cldlApGroup": cldlApGroup,
       "cldlResetGroup": cldlResetGroup,
       "cldlRestartGroup": cldlRestartGroup,
       "cldlNotifsGroup": cldlNotifsGroup}
)
