# SNMP MIB module (ME1200-ICFG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/ME1200-ICFG-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 09:05:30 2025
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

(me1200SwitchMgmt,) = mibBuilder.importSymbols(
    "CISCOME1200-MIB",
    "me1200SwitchMgmt")

(ME1200DisplayString,) = mibBuilder.importSymbols(
    "ME1200-TC",
    "ME1200DisplayString")

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

me1200IcfgMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 101)
)
if mibBuilder.loadTexts:
    me1200IcfgMIB.setRevisions(
        ("2014-02-18 00:00",
         "2014-01-29 00:00",
         "2014-01-09 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ME1200ConfigStatus(TextualConvention, Integer32):
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



class ME1200ReloadDefault(TextualConvention, Integer32):
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



class ME1200ConfigType(TextualConvention, Integer32):
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



# MIB Managed Objects in the order of their OIDs

_Me1200IcfgMIBObjects_ObjectIdentity = ObjectIdentity
me1200IcfgMIBObjects = _Me1200IcfgMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 101, 1)
)
_Me1200IcfgStatus_ObjectIdentity = ObjectIdentity
me1200IcfgStatus = _Me1200IcfgStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 101, 1, 3)
)
_Me1200IcfgStatusFileStatistics_ObjectIdentity = ObjectIdentity
me1200IcfgStatusFileStatistics = _Me1200IcfgStatusFileStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 101, 1, 3, 1)
)
_Me1200IcfgStatusFileStatisticsNumberOfFiles_Type = Unsigned32
_Me1200IcfgStatusFileStatisticsNumberOfFiles_Object = MibScalar
me1200IcfgStatusFileStatisticsNumberOfFiles = _Me1200IcfgStatusFileStatisticsNumberOfFiles_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 101, 1, 3, 1, 1),
    _Me1200IcfgStatusFileStatisticsNumberOfFiles_Type()
)
me1200IcfgStatusFileStatisticsNumberOfFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IcfgStatusFileStatisticsNumberOfFiles.setStatus("current")
_Me1200IcfgStatusFileStatisticsTotalBytes_Type = Unsigned32
_Me1200IcfgStatusFileStatisticsTotalBytes_Object = MibScalar
me1200IcfgStatusFileStatisticsTotalBytes = _Me1200IcfgStatusFileStatisticsTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 101, 1, 3, 1, 2),
    _Me1200IcfgStatusFileStatisticsTotalBytes_Type()
)
me1200IcfgStatusFileStatisticsTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IcfgStatusFileStatisticsTotalBytes.setStatus("current")
_Me1200IcfgStatusFileTable_Object = MibTable
me1200IcfgStatusFileTable = _Me1200IcfgStatusFileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 101, 1, 3, 2)
)
if mibBuilder.loadTexts:
    me1200IcfgStatusFileTable.setStatus("current")
_Me1200IcfgStatusFileEntry_Object = MibTableRow
me1200IcfgStatusFileEntry = _Me1200IcfgStatusFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 101, 1, 3, 2, 1)
)
me1200IcfgStatusFileEntry.setIndexNames(
    (0, "ME1200-ICFG-MIB", "me1200IcfgStatusFileFileNo"),
)
if mibBuilder.loadTexts:
    me1200IcfgStatusFileEntry.setStatus("current")


class _Me1200IcfgStatusFileFileNo_Type(Integer32):
    """Custom type me1200IcfgStatusFileFileNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Me1200IcfgStatusFileFileNo_Type.__name__ = "Integer32"
_Me1200IcfgStatusFileFileNo_Object = MibTableColumn
me1200IcfgStatusFileFileNo = _Me1200IcfgStatusFileFileNo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 101, 1, 3, 2, 1, 1),
    _Me1200IcfgStatusFileFileNo_Type()
)
me1200IcfgStatusFileFileNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200IcfgStatusFileFileNo.setStatus("current")


class _Me1200IcfgStatusFileFileName_Type(ME1200DisplayString):
    """Custom type me1200IcfgStatusFileFileName based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Me1200IcfgStatusFileFileName_Type.__name__ = "ME1200DisplayString"
_Me1200IcfgStatusFileFileName_Object = MibTableColumn
me1200IcfgStatusFileFileName = _Me1200IcfgStatusFileFileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 101, 1, 3, 2, 1, 2),
    _Me1200IcfgStatusFileFileName_Type()
)
me1200IcfgStatusFileFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IcfgStatusFileFileName.setStatus("current")
_Me1200IcfgStatusFileBytes_Type = Unsigned32
_Me1200IcfgStatusFileBytes_Object = MibTableColumn
me1200IcfgStatusFileBytes = _Me1200IcfgStatusFileBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 101, 1, 3, 2, 1, 3),
    _Me1200IcfgStatusFileBytes_Type()
)
me1200IcfgStatusFileBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IcfgStatusFileBytes.setStatus("current")


class _Me1200IcfgStatusFileModifiedTime_Type(ME1200DisplayString):
    """Custom type me1200IcfgStatusFileModifiedTime based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 39),
    )


_Me1200IcfgStatusFileModifiedTime_Type.__name__ = "ME1200DisplayString"
_Me1200IcfgStatusFileModifiedTime_Object = MibTableColumn
me1200IcfgStatusFileModifiedTime = _Me1200IcfgStatusFileModifiedTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 101, 1, 3, 2, 1, 4),
    _Me1200IcfgStatusFileModifiedTime_Type()
)
me1200IcfgStatusFileModifiedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IcfgStatusFileModifiedTime.setStatus("current")


class _Me1200IcfgStatusFileAttribute_Type(ME1200DisplayString):
    """Custom type me1200IcfgStatusFileAttribute based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Me1200IcfgStatusFileAttribute_Type.__name__ = "ME1200DisplayString"
_Me1200IcfgStatusFileAttribute_Object = MibTableColumn
me1200IcfgStatusFileAttribute = _Me1200IcfgStatusFileAttribute_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 101, 1, 3, 2, 1, 5),
    _Me1200IcfgStatusFileAttribute_Type()
)
me1200IcfgStatusFileAttribute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IcfgStatusFileAttribute.setStatus("current")
_Me1200IcfgStatusCopyConfig_ObjectIdentity = ObjectIdentity
me1200IcfgStatusCopyConfig = _Me1200IcfgStatusCopyConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 101, 1, 3, 3)
)
_Me1200IcfgStatusCopyConfigStatus_Type = ME1200ConfigStatus
_Me1200IcfgStatusCopyConfigStatus_Object = MibScalar
me1200IcfgStatusCopyConfigStatus = _Me1200IcfgStatusCopyConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 101, 1, 3, 3, 1),
    _Me1200IcfgStatusCopyConfigStatus_Type()
)
me1200IcfgStatusCopyConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IcfgStatusCopyConfigStatus.setStatus("current")
_Me1200IcfgControl_ObjectIdentity = ObjectIdentity
me1200IcfgControl = _Me1200IcfgControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 101, 1, 4)
)
_Me1200IcfgControlGlobals_ObjectIdentity = ObjectIdentity
me1200IcfgControlGlobals = _Me1200IcfgControlGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 101, 1, 4, 1)
)
_Me1200IcfgControlGlobalsReloadDefault_Type = ME1200ReloadDefault
_Me1200IcfgControlGlobalsReloadDefault_Object = MibScalar
me1200IcfgControlGlobalsReloadDefault = _Me1200IcfgControlGlobalsReloadDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 101, 1, 4, 1, 1),
    _Me1200IcfgControlGlobalsReloadDefault_Type()
)
me1200IcfgControlGlobalsReloadDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IcfgControlGlobalsReloadDefault.setStatus("current")


class _Me1200IcfgControlGlobalsDeleteFile_Type(ME1200DisplayString):
    """Custom type me1200IcfgControlGlobalsDeleteFile based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Me1200IcfgControlGlobalsDeleteFile_Type.__name__ = "ME1200DisplayString"
_Me1200IcfgControlGlobalsDeleteFile_Object = MibScalar
me1200IcfgControlGlobalsDeleteFile = _Me1200IcfgControlGlobalsDeleteFile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 101, 1, 4, 1, 2),
    _Me1200IcfgControlGlobalsDeleteFile_Type()
)
me1200IcfgControlGlobalsDeleteFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IcfgControlGlobalsDeleteFile.setStatus("current")
_Me1200IcfgControlCopyConfig_ObjectIdentity = ObjectIdentity
me1200IcfgControlCopyConfig = _Me1200IcfgControlCopyConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 101, 1, 4, 2)
)
_Me1200IcfgControlCopyConfigCopy_Type = TruthValue
_Me1200IcfgControlCopyConfigCopy_Object = MibScalar
me1200IcfgControlCopyConfigCopy = _Me1200IcfgControlCopyConfigCopy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 101, 1, 4, 2, 1),
    _Me1200IcfgControlCopyConfigCopy_Type()
)
me1200IcfgControlCopyConfigCopy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IcfgControlCopyConfigCopy.setStatus("current")
_Me1200IcfgControlCopyConfigSourceConfigType_Type = ME1200ConfigType
_Me1200IcfgControlCopyConfigSourceConfigType_Object = MibScalar
me1200IcfgControlCopyConfigSourceConfigType = _Me1200IcfgControlCopyConfigSourceConfigType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 101, 1, 4, 2, 2),
    _Me1200IcfgControlCopyConfigSourceConfigType_Type()
)
me1200IcfgControlCopyConfigSourceConfigType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IcfgControlCopyConfigSourceConfigType.setStatus("current")


class _Me1200IcfgControlCopyConfigSourceConfigFile_Type(ME1200DisplayString):
    """Custom type me1200IcfgControlCopyConfigSourceConfigFile based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Me1200IcfgControlCopyConfigSourceConfigFile_Type.__name__ = "ME1200DisplayString"
_Me1200IcfgControlCopyConfigSourceConfigFile_Object = MibScalar
me1200IcfgControlCopyConfigSourceConfigFile = _Me1200IcfgControlCopyConfigSourceConfigFile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 101, 1, 4, 2, 3),
    _Me1200IcfgControlCopyConfigSourceConfigFile_Type()
)
me1200IcfgControlCopyConfigSourceConfigFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IcfgControlCopyConfigSourceConfigFile.setStatus("current")
_Me1200IcfgControlCopyConfigDestinationConfigType_Type = ME1200ConfigType
_Me1200IcfgControlCopyConfigDestinationConfigType_Object = MibScalar
me1200IcfgControlCopyConfigDestinationConfigType = _Me1200IcfgControlCopyConfigDestinationConfigType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 101, 1, 4, 2, 4),
    _Me1200IcfgControlCopyConfigDestinationConfigType_Type()
)
me1200IcfgControlCopyConfigDestinationConfigType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IcfgControlCopyConfigDestinationConfigType.setStatus("current")


class _Me1200IcfgControlCopyConfigDestinationConfigFile_Type(ME1200DisplayString):
    """Custom type me1200IcfgControlCopyConfigDestinationConfigFile based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Me1200IcfgControlCopyConfigDestinationConfigFile_Type.__name__ = "ME1200DisplayString"
_Me1200IcfgControlCopyConfigDestinationConfigFile_Object = MibScalar
me1200IcfgControlCopyConfigDestinationConfigFile = _Me1200IcfgControlCopyConfigDestinationConfigFile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 101, 1, 4, 2, 5),
    _Me1200IcfgControlCopyConfigDestinationConfigFile_Type()
)
me1200IcfgControlCopyConfigDestinationConfigFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IcfgControlCopyConfigDestinationConfigFile.setStatus("current")
_Me1200IcfgControlCopyConfigMerge_Type = TruthValue
_Me1200IcfgControlCopyConfigMerge_Object = MibScalar
me1200IcfgControlCopyConfigMerge = _Me1200IcfgControlCopyConfigMerge_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 101, 1, 4, 2, 6),
    _Me1200IcfgControlCopyConfigMerge_Type()
)
me1200IcfgControlCopyConfigMerge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IcfgControlCopyConfigMerge.setStatus("current")
_Me1200IcfgMIBConformance_ObjectIdentity = ObjectIdentity
me1200IcfgMIBConformance = _Me1200IcfgMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 101, 2)
)
_Me1200IcfgMIBCompliances_ObjectIdentity = ObjectIdentity
me1200IcfgMIBCompliances = _Me1200IcfgMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 101, 2, 1)
)
_Me1200IcfgMIBGroups_ObjectIdentity = ObjectIdentity
me1200IcfgMIBGroups = _Me1200IcfgMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 101, 2, 2)
)

# Managed Objects groups

me1200IcfgStatusFileStatisticsInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 101, 2, 2, 1)
)
me1200IcfgStatusFileStatisticsInfoGroup.setObjects(
      *(("ME1200-ICFG-MIB", "me1200IcfgStatusFileStatisticsNumberOfFiles"),
        ("ME1200-ICFG-MIB", "me1200IcfgStatusFileStatisticsTotalBytes"))
)
if mibBuilder.loadTexts:
    me1200IcfgStatusFileStatisticsInfoGroup.setStatus("current")

me1200IcfgStatusFileTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 101, 2, 2, 2)
)
me1200IcfgStatusFileTableInfoGroup.setObjects(
      *(("ME1200-ICFG-MIB", "me1200IcfgStatusFileFileName"),
        ("ME1200-ICFG-MIB", "me1200IcfgStatusFileBytes"),
        ("ME1200-ICFG-MIB", "me1200IcfgStatusFileModifiedTime"),
        ("ME1200-ICFG-MIB", "me1200IcfgStatusFileAttribute"))
)
if mibBuilder.loadTexts:
    me1200IcfgStatusFileTableInfoGroup.setStatus("current")

me1200IcfgStatusCopyConfigInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 101, 2, 2, 3)
)
me1200IcfgStatusCopyConfigInfoGroup.setObjects(
    ("ME1200-ICFG-MIB", "me1200IcfgStatusCopyConfigStatus")
)
if mibBuilder.loadTexts:
    me1200IcfgStatusCopyConfigInfoGroup.setStatus("current")

me1200IcfgControlGlobalsInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 101, 2, 2, 4)
)
me1200IcfgControlGlobalsInfoGroup.setObjects(
      *(("ME1200-ICFG-MIB", "me1200IcfgControlGlobalsReloadDefault"),
        ("ME1200-ICFG-MIB", "me1200IcfgControlGlobalsDeleteFile"))
)
if mibBuilder.loadTexts:
    me1200IcfgControlGlobalsInfoGroup.setStatus("current")

me1200IcfgControlCopyConfigInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 101, 2, 2, 5)
)
me1200IcfgControlCopyConfigInfoGroup.setObjects(
      *(("ME1200-ICFG-MIB", "me1200IcfgControlCopyConfigCopy"),
        ("ME1200-ICFG-MIB", "me1200IcfgControlCopyConfigSourceConfigType"),
        ("ME1200-ICFG-MIB", "me1200IcfgControlCopyConfigSourceConfigFile"),
        ("ME1200-ICFG-MIB", "me1200IcfgControlCopyConfigDestinationConfigType"),
        ("ME1200-ICFG-MIB", "me1200IcfgControlCopyConfigDestinationConfigFile"),
        ("ME1200-ICFG-MIB", "me1200IcfgControlCopyConfigMerge"))
)
if mibBuilder.loadTexts:
    me1200IcfgControlCopyConfigInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

me1200IcfgMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 101, 2, 1, 1)
)
me1200IcfgMIBCompliance.setObjects(
      *(("ME1200-ICFG-MIB", "me1200IcfgStatusFileStatisticsInfoGroup"),
        ("ME1200-ICFG-MIB", "me1200IcfgStatusFileTableInfoGroup"),
        ("ME1200-ICFG-MIB", "me1200IcfgStatusCopyConfigInfoGroup"),
        ("ME1200-ICFG-MIB", "me1200IcfgControlGlobalsInfoGroup"),
        ("ME1200-ICFG-MIB", "me1200IcfgControlCopyConfigInfoGroup"))
)
if mibBuilder.loadTexts:
    me1200IcfgMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ME1200-ICFG-MIB",
    **{"ME1200ConfigStatus": ME1200ConfigStatus,
       "ME1200ReloadDefault": ME1200ReloadDefault,
       "ME1200ConfigType": ME1200ConfigType,
       "me1200IcfgMIB": me1200IcfgMIB,
       "me1200IcfgMIBObjects": me1200IcfgMIBObjects,
       "me1200IcfgStatus": me1200IcfgStatus,
       "me1200IcfgStatusFileStatistics": me1200IcfgStatusFileStatistics,
       "me1200IcfgStatusFileStatisticsNumberOfFiles": me1200IcfgStatusFileStatisticsNumberOfFiles,
       "me1200IcfgStatusFileStatisticsTotalBytes": me1200IcfgStatusFileStatisticsTotalBytes,
       "me1200IcfgStatusFileTable": me1200IcfgStatusFileTable,
       "me1200IcfgStatusFileEntry": me1200IcfgStatusFileEntry,
       "me1200IcfgStatusFileFileNo": me1200IcfgStatusFileFileNo,
       "me1200IcfgStatusFileFileName": me1200IcfgStatusFileFileName,
       "me1200IcfgStatusFileBytes": me1200IcfgStatusFileBytes,
       "me1200IcfgStatusFileModifiedTime": me1200IcfgStatusFileModifiedTime,
       "me1200IcfgStatusFileAttribute": me1200IcfgStatusFileAttribute,
       "me1200IcfgStatusCopyConfig": me1200IcfgStatusCopyConfig,
       "me1200IcfgStatusCopyConfigStatus": me1200IcfgStatusCopyConfigStatus,
       "me1200IcfgControl": me1200IcfgControl,
       "me1200IcfgControlGlobals": me1200IcfgControlGlobals,
       "me1200IcfgControlGlobalsReloadDefault": me1200IcfgControlGlobalsReloadDefault,
       "me1200IcfgControlGlobalsDeleteFile": me1200IcfgControlGlobalsDeleteFile,
       "me1200IcfgControlCopyConfig": me1200IcfgControlCopyConfig,
       "me1200IcfgControlCopyConfigCopy": me1200IcfgControlCopyConfigCopy,
       "me1200IcfgControlCopyConfigSourceConfigType": me1200IcfgControlCopyConfigSourceConfigType,
       "me1200IcfgControlCopyConfigSourceConfigFile": me1200IcfgControlCopyConfigSourceConfigFile,
       "me1200IcfgControlCopyConfigDestinationConfigType": me1200IcfgControlCopyConfigDestinationConfigType,
       "me1200IcfgControlCopyConfigDestinationConfigFile": me1200IcfgControlCopyConfigDestinationConfigFile,
       "me1200IcfgControlCopyConfigMerge": me1200IcfgControlCopyConfigMerge,
       "me1200IcfgMIBConformance": me1200IcfgMIBConformance,
       "me1200IcfgMIBCompliances": me1200IcfgMIBCompliances,
       "me1200IcfgMIBCompliance": me1200IcfgMIBCompliance,
       "me1200IcfgMIBGroups": me1200IcfgMIBGroups,
       "me1200IcfgStatusFileStatisticsInfoGroup": me1200IcfgStatusFileStatisticsInfoGroup,
       "me1200IcfgStatusFileTableInfoGroup": me1200IcfgStatusFileTableInfoGroup,
       "me1200IcfgStatusCopyConfigInfoGroup": me1200IcfgStatusCopyConfigInfoGroup,
       "me1200IcfgControlGlobalsInfoGroup": me1200IcfgControlGlobalsInfoGroup,
       "me1200IcfgControlCopyConfigInfoGroup": me1200IcfgControlCopyConfigInfoGroup}
)
