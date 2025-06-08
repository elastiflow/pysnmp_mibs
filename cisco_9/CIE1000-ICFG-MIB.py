# SNMP MIB module (CIE1000-ICFG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CIE1000-ICFG-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 20:26:41 2025
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

(CIE1000DisplayString,) = mibBuilder.importSymbols(
    "CIE1000-TC",
    "CIE1000DisplayString")

(cie1000SwitchMgmt,) = mibBuilder.importSymbols(
    "CISCO-IE1000-MIB",
    "cie1000SwitchMgmt")

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

(DisplayString,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

cie1000IcfgMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 101)
)
if mibBuilder.loadTexts:
    cie1000IcfgMib.setRevisions(
        ("2016-05-09 00:00",
         "2014-10-10 00:00",
         "2014-07-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class CIE1000IcfgConfigStatus(TextualConvention, Integer32):
    status = "current"
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("success", 1),
          ("inProgress", 2),
          ("errOtherInProcessing", 3),
          ("errNoSuchFile", 4),
          ("errSameSrcDst", 5),
          ("errPermissionDenied", 6),
          ("errLoadSrc", 7),
          ("errSaveDst", 8))
    )



class CIE1000IcfgConfigType(TextualConvention, Integer32):
    status = "current"
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
        *(("none", 0),
          ("runningConfig", 1),
          ("startupConfig", 2),
          ("configFile", 3))
    )



class CIE1000IcfgReloadDefault(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("default", 1),
          ("defaultKeepIp", 2))
    )



# MIB Managed Objects in the order of their OIDs

_Cie1000IcfgMibObjects_ObjectIdentity = ObjectIdentity
cie1000IcfgMibObjects = _Cie1000IcfgMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 101, 1)
)
_Cie1000IcfgStatus_ObjectIdentity = ObjectIdentity
cie1000IcfgStatus = _Cie1000IcfgStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 101, 1, 3)
)
_Cie1000IcfgStatusFileStatistics_ObjectIdentity = ObjectIdentity
cie1000IcfgStatusFileStatistics = _Cie1000IcfgStatusFileStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 101, 1, 3, 1)
)
_Cie1000IcfgStatusFileStatisticsNumberOfFiles_Type = Unsigned32
_Cie1000IcfgStatusFileStatisticsNumberOfFiles_Object = MibScalar
cie1000IcfgStatusFileStatisticsNumberOfFiles = _Cie1000IcfgStatusFileStatisticsNumberOfFiles_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 101, 1, 3, 1, 1),
    _Cie1000IcfgStatusFileStatisticsNumberOfFiles_Type()
)
cie1000IcfgStatusFileStatisticsNumberOfFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IcfgStatusFileStatisticsNumberOfFiles.setStatus("current")
_Cie1000IcfgStatusFileStatisticsTotalBytes_Type = Unsigned32
_Cie1000IcfgStatusFileStatisticsTotalBytes_Object = MibScalar
cie1000IcfgStatusFileStatisticsTotalBytes = _Cie1000IcfgStatusFileStatisticsTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 101, 1, 3, 1, 2),
    _Cie1000IcfgStatusFileStatisticsTotalBytes_Type()
)
cie1000IcfgStatusFileStatisticsTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IcfgStatusFileStatisticsTotalBytes.setStatus("current")
_Cie1000IcfgStatusFileStatisticsFlashSizeBytes_Type = Unsigned32
_Cie1000IcfgStatusFileStatisticsFlashSizeBytes_Object = MibScalar
cie1000IcfgStatusFileStatisticsFlashSizeBytes = _Cie1000IcfgStatusFileStatisticsFlashSizeBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 101, 1, 3, 1, 3),
    _Cie1000IcfgStatusFileStatisticsFlashSizeBytes_Type()
)
cie1000IcfgStatusFileStatisticsFlashSizeBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IcfgStatusFileStatisticsFlashSizeBytes.setStatus("current")
_Cie1000IcfgStatusFileStatisticsFlashFreeBytes_Type = Unsigned32
_Cie1000IcfgStatusFileStatisticsFlashFreeBytes_Object = MibScalar
cie1000IcfgStatusFileStatisticsFlashFreeBytes = _Cie1000IcfgStatusFileStatisticsFlashFreeBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 101, 1, 3, 1, 4),
    _Cie1000IcfgStatusFileStatisticsFlashFreeBytes_Type()
)
cie1000IcfgStatusFileStatisticsFlashFreeBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IcfgStatusFileStatisticsFlashFreeBytes.setStatus("current")
_Cie1000IcfgStatusFileTable_Object = MibTable
cie1000IcfgStatusFileTable = _Cie1000IcfgStatusFileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 101, 1, 3, 2)
)
if mibBuilder.loadTexts:
    cie1000IcfgStatusFileTable.setStatus("current")
_Cie1000IcfgStatusFileEntry_Object = MibTableRow
cie1000IcfgStatusFileEntry = _Cie1000IcfgStatusFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 101, 1, 3, 2, 1)
)
cie1000IcfgStatusFileEntry.setIndexNames(
    (0, "CIE1000-ICFG-MIB", "cie1000IcfgStatusFileFileNo"),
)
if mibBuilder.loadTexts:
    cie1000IcfgStatusFileEntry.setStatus("current")


class _Cie1000IcfgStatusFileFileNo_Type(Integer32):
    """Custom type cie1000IcfgStatusFileFileNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cie1000IcfgStatusFileFileNo_Type.__name__ = "Integer32"
_Cie1000IcfgStatusFileFileNo_Object = MibTableColumn
cie1000IcfgStatusFileFileNo = _Cie1000IcfgStatusFileFileNo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 101, 1, 3, 2, 1, 1),
    _Cie1000IcfgStatusFileFileNo_Type()
)
cie1000IcfgStatusFileFileNo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000IcfgStatusFileFileNo.setStatus("current")


class _Cie1000IcfgStatusFileFileName_Type(CIE1000DisplayString):
    """Custom type cie1000IcfgStatusFileFileName based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Cie1000IcfgStatusFileFileName_Type.__name__ = "CIE1000DisplayString"
_Cie1000IcfgStatusFileFileName_Object = MibTableColumn
cie1000IcfgStatusFileFileName = _Cie1000IcfgStatusFileFileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 101, 1, 3, 2, 1, 2),
    _Cie1000IcfgStatusFileFileName_Type()
)
cie1000IcfgStatusFileFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IcfgStatusFileFileName.setStatus("current")
_Cie1000IcfgStatusFileBytes_Type = Unsigned32
_Cie1000IcfgStatusFileBytes_Object = MibTableColumn
cie1000IcfgStatusFileBytes = _Cie1000IcfgStatusFileBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 101, 1, 3, 2, 1, 3),
    _Cie1000IcfgStatusFileBytes_Type()
)
cie1000IcfgStatusFileBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IcfgStatusFileBytes.setStatus("current")


class _Cie1000IcfgStatusFileModifiedTime_Type(CIE1000DisplayString):
    """Custom type cie1000IcfgStatusFileModifiedTime based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 39),
    )


_Cie1000IcfgStatusFileModifiedTime_Type.__name__ = "CIE1000DisplayString"
_Cie1000IcfgStatusFileModifiedTime_Object = MibTableColumn
cie1000IcfgStatusFileModifiedTime = _Cie1000IcfgStatusFileModifiedTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 101, 1, 3, 2, 1, 4),
    _Cie1000IcfgStatusFileModifiedTime_Type()
)
cie1000IcfgStatusFileModifiedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IcfgStatusFileModifiedTime.setStatus("current")


class _Cie1000IcfgStatusFileAttribute_Type(CIE1000DisplayString):
    """Custom type cie1000IcfgStatusFileAttribute based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Cie1000IcfgStatusFileAttribute_Type.__name__ = "CIE1000DisplayString"
_Cie1000IcfgStatusFileAttribute_Object = MibTableColumn
cie1000IcfgStatusFileAttribute = _Cie1000IcfgStatusFileAttribute_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 101, 1, 3, 2, 1, 5),
    _Cie1000IcfgStatusFileAttribute_Type()
)
cie1000IcfgStatusFileAttribute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IcfgStatusFileAttribute.setStatus("current")
_Cie1000IcfgStatusCopyConfig_ObjectIdentity = ObjectIdentity
cie1000IcfgStatusCopyConfig = _Cie1000IcfgStatusCopyConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 101, 1, 3, 3)
)
_Cie1000IcfgStatusCopyConfigStatus_Type = CIE1000IcfgConfigStatus
_Cie1000IcfgStatusCopyConfigStatus_Object = MibScalar
cie1000IcfgStatusCopyConfigStatus = _Cie1000IcfgStatusCopyConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 101, 1, 3, 3, 1),
    _Cie1000IcfgStatusCopyConfigStatus_Type()
)
cie1000IcfgStatusCopyConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IcfgStatusCopyConfigStatus.setStatus("current")
_Cie1000IcfgControl_ObjectIdentity = ObjectIdentity
cie1000IcfgControl = _Cie1000IcfgControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 101, 1, 4)
)
_Cie1000IcfgControlGlobals_ObjectIdentity = ObjectIdentity
cie1000IcfgControlGlobals = _Cie1000IcfgControlGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 101, 1, 4, 1)
)
_Cie1000IcfgControlGlobalsReloadDefault_Type = CIE1000IcfgReloadDefault
_Cie1000IcfgControlGlobalsReloadDefault_Object = MibScalar
cie1000IcfgControlGlobalsReloadDefault = _Cie1000IcfgControlGlobalsReloadDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 101, 1, 4, 1, 1),
    _Cie1000IcfgControlGlobalsReloadDefault_Type()
)
cie1000IcfgControlGlobalsReloadDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IcfgControlGlobalsReloadDefault.setStatus("current")


class _Cie1000IcfgControlGlobalsDeleteFile_Type(CIE1000DisplayString):
    """Custom type cie1000IcfgControlGlobalsDeleteFile based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Cie1000IcfgControlGlobalsDeleteFile_Type.__name__ = "CIE1000DisplayString"
_Cie1000IcfgControlGlobalsDeleteFile_Object = MibScalar
cie1000IcfgControlGlobalsDeleteFile = _Cie1000IcfgControlGlobalsDeleteFile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 101, 1, 4, 1, 2),
    _Cie1000IcfgControlGlobalsDeleteFile_Type()
)
cie1000IcfgControlGlobalsDeleteFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IcfgControlGlobalsDeleteFile.setStatus("current")
_Cie1000IcfgControlCopyConfig_ObjectIdentity = ObjectIdentity
cie1000IcfgControlCopyConfig = _Cie1000IcfgControlCopyConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 101, 1, 4, 2)
)
_Cie1000IcfgControlCopyConfigCopy_Type = TruthValue
_Cie1000IcfgControlCopyConfigCopy_Object = MibScalar
cie1000IcfgControlCopyConfigCopy = _Cie1000IcfgControlCopyConfigCopy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 101, 1, 4, 2, 1),
    _Cie1000IcfgControlCopyConfigCopy_Type()
)
cie1000IcfgControlCopyConfigCopy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IcfgControlCopyConfigCopy.setStatus("current")
_Cie1000IcfgControlCopyConfigSourceConfigType_Type = CIE1000IcfgConfigType
_Cie1000IcfgControlCopyConfigSourceConfigType_Object = MibScalar
cie1000IcfgControlCopyConfigSourceConfigType = _Cie1000IcfgControlCopyConfigSourceConfigType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 101, 1, 4, 2, 2),
    _Cie1000IcfgControlCopyConfigSourceConfigType_Type()
)
cie1000IcfgControlCopyConfigSourceConfigType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IcfgControlCopyConfigSourceConfigType.setStatus("current")


class _Cie1000IcfgControlCopyConfigSourceConfigFile_Type(CIE1000DisplayString):
    """Custom type cie1000IcfgControlCopyConfigSourceConfigFile based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Cie1000IcfgControlCopyConfigSourceConfigFile_Type.__name__ = "CIE1000DisplayString"
_Cie1000IcfgControlCopyConfigSourceConfigFile_Object = MibScalar
cie1000IcfgControlCopyConfigSourceConfigFile = _Cie1000IcfgControlCopyConfigSourceConfigFile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 101, 1, 4, 2, 3),
    _Cie1000IcfgControlCopyConfigSourceConfigFile_Type()
)
cie1000IcfgControlCopyConfigSourceConfigFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IcfgControlCopyConfigSourceConfigFile.setStatus("current")
_Cie1000IcfgControlCopyConfigDestinationConfigType_Type = CIE1000IcfgConfigType
_Cie1000IcfgControlCopyConfigDestinationConfigType_Object = MibScalar
cie1000IcfgControlCopyConfigDestinationConfigType = _Cie1000IcfgControlCopyConfigDestinationConfigType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 101, 1, 4, 2, 4),
    _Cie1000IcfgControlCopyConfigDestinationConfigType_Type()
)
cie1000IcfgControlCopyConfigDestinationConfigType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IcfgControlCopyConfigDestinationConfigType.setStatus("current")


class _Cie1000IcfgControlCopyConfigDestinationConfigFile_Type(CIE1000DisplayString):
    """Custom type cie1000IcfgControlCopyConfigDestinationConfigFile based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Cie1000IcfgControlCopyConfigDestinationConfigFile_Type.__name__ = "CIE1000DisplayString"
_Cie1000IcfgControlCopyConfigDestinationConfigFile_Object = MibScalar
cie1000IcfgControlCopyConfigDestinationConfigFile = _Cie1000IcfgControlCopyConfigDestinationConfigFile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 101, 1, 4, 2, 5),
    _Cie1000IcfgControlCopyConfigDestinationConfigFile_Type()
)
cie1000IcfgControlCopyConfigDestinationConfigFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IcfgControlCopyConfigDestinationConfigFile.setStatus("current")
_Cie1000IcfgControlCopyConfigMerge_Type = TruthValue
_Cie1000IcfgControlCopyConfigMerge_Object = MibScalar
cie1000IcfgControlCopyConfigMerge = _Cie1000IcfgControlCopyConfigMerge_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 101, 1, 4, 2, 6),
    _Cie1000IcfgControlCopyConfigMerge_Type()
)
cie1000IcfgControlCopyConfigMerge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IcfgControlCopyConfigMerge.setStatus("current")
_Cie1000IcfgMibConformance_ObjectIdentity = ObjectIdentity
cie1000IcfgMibConformance = _Cie1000IcfgMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 101, 2)
)
_Cie1000IcfgMibCompliances_ObjectIdentity = ObjectIdentity
cie1000IcfgMibCompliances = _Cie1000IcfgMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 101, 2, 1)
)
_Cie1000IcfgMibGroups_ObjectIdentity = ObjectIdentity
cie1000IcfgMibGroups = _Cie1000IcfgMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 101, 2, 2)
)

# Managed Objects groups

cie1000IcfgStatusFileStatisticsInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 101, 2, 2, 1)
)
cie1000IcfgStatusFileStatisticsInfoGroup.setObjects(
      *(("CIE1000-ICFG-MIB", "cie1000IcfgStatusFileStatisticsNumberOfFiles"),
        ("CIE1000-ICFG-MIB", "cie1000IcfgStatusFileStatisticsTotalBytes"),
        ("CIE1000-ICFG-MIB", "cie1000IcfgStatusFileStatisticsFlashSizeBytes"),
        ("CIE1000-ICFG-MIB", "cie1000IcfgStatusFileStatisticsFlashFreeBytes"))
)
if mibBuilder.loadTexts:
    cie1000IcfgStatusFileStatisticsInfoGroup.setStatus("current")

cie1000IcfgStatusFileTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 101, 2, 2, 2)
)
cie1000IcfgStatusFileTableInfoGroup.setObjects(
      *(("CIE1000-ICFG-MIB", "cie1000IcfgStatusFileFileNo"),
        ("CIE1000-ICFG-MIB", "cie1000IcfgStatusFileFileName"),
        ("CIE1000-ICFG-MIB", "cie1000IcfgStatusFileBytes"),
        ("CIE1000-ICFG-MIB", "cie1000IcfgStatusFileModifiedTime"),
        ("CIE1000-ICFG-MIB", "cie1000IcfgStatusFileAttribute"))
)
if mibBuilder.loadTexts:
    cie1000IcfgStatusFileTableInfoGroup.setStatus("current")

cie1000IcfgStatusCopyConfigInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 101, 2, 2, 3)
)
cie1000IcfgStatusCopyConfigInfoGroup.setObjects(
    ("CIE1000-ICFG-MIB", "cie1000IcfgStatusCopyConfigStatus")
)
if mibBuilder.loadTexts:
    cie1000IcfgStatusCopyConfigInfoGroup.setStatus("current")

cie1000IcfgControlGlobalsInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 101, 2, 2, 4)
)
cie1000IcfgControlGlobalsInfoGroup.setObjects(
      *(("CIE1000-ICFG-MIB", "cie1000IcfgControlGlobalsReloadDefault"),
        ("CIE1000-ICFG-MIB", "cie1000IcfgControlGlobalsDeleteFile"))
)
if mibBuilder.loadTexts:
    cie1000IcfgControlGlobalsInfoGroup.setStatus("current")

cie1000IcfgControlCopyConfigInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 101, 2, 2, 5)
)
cie1000IcfgControlCopyConfigInfoGroup.setObjects(
      *(("CIE1000-ICFG-MIB", "cie1000IcfgControlCopyConfigCopy"),
        ("CIE1000-ICFG-MIB", "cie1000IcfgControlCopyConfigSourceConfigType"),
        ("CIE1000-ICFG-MIB", "cie1000IcfgControlCopyConfigSourceConfigFile"),
        ("CIE1000-ICFG-MIB", "cie1000IcfgControlCopyConfigDestinationConfigType"),
        ("CIE1000-ICFG-MIB", "cie1000IcfgControlCopyConfigDestinationConfigFile"),
        ("CIE1000-ICFG-MIB", "cie1000IcfgControlCopyConfigMerge"))
)
if mibBuilder.loadTexts:
    cie1000IcfgControlCopyConfigInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cie1000IcfgMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 101, 2, 1, 1)
)
cie1000IcfgMibCompliance.setObjects(
      *(("CIE1000-ICFG-MIB", "cie1000IcfgStatusFileStatisticsInfoGroup"),
        ("CIE1000-ICFG-MIB", "cie1000IcfgStatusFileTableInfoGroup"),
        ("CIE1000-ICFG-MIB", "cie1000IcfgStatusCopyConfigInfoGroup"),
        ("CIE1000-ICFG-MIB", "cie1000IcfgControlGlobalsInfoGroup"),
        ("CIE1000-ICFG-MIB", "cie1000IcfgControlCopyConfigInfoGroup"))
)
if mibBuilder.loadTexts:
    cie1000IcfgMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIE1000-ICFG-MIB",
    **{"CIE1000IcfgConfigStatus": CIE1000IcfgConfigStatus,
       "CIE1000IcfgConfigType": CIE1000IcfgConfigType,
       "CIE1000IcfgReloadDefault": CIE1000IcfgReloadDefault,
       "cie1000IcfgMib": cie1000IcfgMib,
       "cie1000IcfgMibObjects": cie1000IcfgMibObjects,
       "cie1000IcfgStatus": cie1000IcfgStatus,
       "cie1000IcfgStatusFileStatistics": cie1000IcfgStatusFileStatistics,
       "cie1000IcfgStatusFileStatisticsNumberOfFiles": cie1000IcfgStatusFileStatisticsNumberOfFiles,
       "cie1000IcfgStatusFileStatisticsTotalBytes": cie1000IcfgStatusFileStatisticsTotalBytes,
       "cie1000IcfgStatusFileStatisticsFlashSizeBytes": cie1000IcfgStatusFileStatisticsFlashSizeBytes,
       "cie1000IcfgStatusFileStatisticsFlashFreeBytes": cie1000IcfgStatusFileStatisticsFlashFreeBytes,
       "cie1000IcfgStatusFileTable": cie1000IcfgStatusFileTable,
       "cie1000IcfgStatusFileEntry": cie1000IcfgStatusFileEntry,
       "cie1000IcfgStatusFileFileNo": cie1000IcfgStatusFileFileNo,
       "cie1000IcfgStatusFileFileName": cie1000IcfgStatusFileFileName,
       "cie1000IcfgStatusFileBytes": cie1000IcfgStatusFileBytes,
       "cie1000IcfgStatusFileModifiedTime": cie1000IcfgStatusFileModifiedTime,
       "cie1000IcfgStatusFileAttribute": cie1000IcfgStatusFileAttribute,
       "cie1000IcfgStatusCopyConfig": cie1000IcfgStatusCopyConfig,
       "cie1000IcfgStatusCopyConfigStatus": cie1000IcfgStatusCopyConfigStatus,
       "cie1000IcfgControl": cie1000IcfgControl,
       "cie1000IcfgControlGlobals": cie1000IcfgControlGlobals,
       "cie1000IcfgControlGlobalsReloadDefault": cie1000IcfgControlGlobalsReloadDefault,
       "cie1000IcfgControlGlobalsDeleteFile": cie1000IcfgControlGlobalsDeleteFile,
       "cie1000IcfgControlCopyConfig": cie1000IcfgControlCopyConfig,
       "cie1000IcfgControlCopyConfigCopy": cie1000IcfgControlCopyConfigCopy,
       "cie1000IcfgControlCopyConfigSourceConfigType": cie1000IcfgControlCopyConfigSourceConfigType,
       "cie1000IcfgControlCopyConfigSourceConfigFile": cie1000IcfgControlCopyConfigSourceConfigFile,
       "cie1000IcfgControlCopyConfigDestinationConfigType": cie1000IcfgControlCopyConfigDestinationConfigType,
       "cie1000IcfgControlCopyConfigDestinationConfigFile": cie1000IcfgControlCopyConfigDestinationConfigFile,
       "cie1000IcfgControlCopyConfigMerge": cie1000IcfgControlCopyConfigMerge,
       "cie1000IcfgMibConformance": cie1000IcfgMibConformance,
       "cie1000IcfgMibCompliances": cie1000IcfgMibCompliances,
       "cie1000IcfgMibCompliance": cie1000IcfgMibCompliance,
       "cie1000IcfgMibGroups": cie1000IcfgMibGroups,
       "cie1000IcfgStatusFileStatisticsInfoGroup": cie1000IcfgStatusFileStatisticsInfoGroup,
       "cie1000IcfgStatusFileTableInfoGroup": cie1000IcfgStatusFileTableInfoGroup,
       "cie1000IcfgStatusCopyConfigInfoGroup": cie1000IcfgStatusCopyConfigInfoGroup,
       "cie1000IcfgControlGlobalsInfoGroup": cie1000IcfgControlGlobalsInfoGroup,
       "cie1000IcfgControlCopyConfigInfoGroup": cie1000IcfgControlCopyConfigInfoGroup}
)
