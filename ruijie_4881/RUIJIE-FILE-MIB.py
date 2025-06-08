# SNMP MIB module (RUIJIE-FILE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-FILE-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 11:04:21 2025
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

(ruijieMgmt,) = mibBuilder.importSymbols(
    "RUIJIE-SMI",
    "ruijieMgmt")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ruijieFileMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 11)
)
if mibBuilder.loadTexts:
    ruijieFileMIB.setRevisions(
        ("2002-03-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieFileMIBTraps_ObjectIdentity = ObjectIdentity
ruijieFileMIBTraps = _RuijieFileMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 11, 0)
)
_RuijieFileMIBObjects_ObjectIdentity = ObjectIdentity
ruijieFileMIBObjects = _RuijieFileMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 11, 1)
)
_RuijieFileTransTable_Object = MibTable
ruijieFileTransTable = _RuijieFileTransTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 11, 1, 1)
)
if mibBuilder.loadTexts:
    ruijieFileTransTable.setStatus("current")
_RuijieFileTransEntry_Object = MibTableRow
ruijieFileTransEntry = _RuijieFileTransEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 11, 1, 1, 1)
)
ruijieFileTransEntry.setIndexNames(
    (0, "RUIJIE-FILE-MIB", "ruijieFileTransIndex"),
)
if mibBuilder.loadTexts:
    ruijieFileTransEntry.setStatus("current")
_RuijieFileTransIndex_Type = Integer32
_RuijieFileTransIndex_Object = MibTableColumn
ruijieFileTransIndex = _RuijieFileTransIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 11, 1, 1, 1, 1),
    _RuijieFileTransIndex_Type()
)
ruijieFileTransIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFileTransIndex.setStatus("current")


class _RuijieFileTransMeans_Type(Integer32):
    """Custom type ruijieFileTransMeans based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tftp", 1),
          ("xmodem", 2),
          ("other", 3))
    )


_RuijieFileTransMeans_Type.__name__ = "Integer32"
_RuijieFileTransMeans_Object = MibTableColumn
ruijieFileTransMeans = _RuijieFileTransMeans_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 11, 1, 1, 1, 2),
    _RuijieFileTransMeans_Type()
)
ruijieFileTransMeans.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieFileTransMeans.setStatus("current")


class _RuijieFileTransOperType_Type(Integer32):
    """Custom type ruijieFileTransOperType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("upload", 1),
          ("download", 2),
          ("synchronize", 3))
    )


_RuijieFileTransOperType_Type.__name__ = "Integer32"
_RuijieFileTransOperType_Object = MibTableColumn
ruijieFileTransOperType = _RuijieFileTransOperType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 11, 1, 1, 1, 3),
    _RuijieFileTransOperType_Type()
)
ruijieFileTransOperType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieFileTransOperType.setStatus("current")
_RuijieFileTransSrcFileName_Type = DisplayString
_RuijieFileTransSrcFileName_Object = MibTableColumn
ruijieFileTransSrcFileName = _RuijieFileTransSrcFileName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 11, 1, 1, 1, 4),
    _RuijieFileTransSrcFileName_Type()
)
ruijieFileTransSrcFileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieFileTransSrcFileName.setStatus("current")
_RuijieFileTransDescFileName_Type = DisplayString
_RuijieFileTransDescFileName_Object = MibTableColumn
ruijieFileTransDescFileName = _RuijieFileTransDescFileName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 11, 1, 1, 1, 5),
    _RuijieFileTransDescFileName_Type()
)
ruijieFileTransDescFileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieFileTransDescFileName.setStatus("current")
_RuijieFileTransServerAddr_Type = IpAddress
_RuijieFileTransServerAddr_Object = MibTableColumn
ruijieFileTransServerAddr = _RuijieFileTransServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 11, 1, 1, 1, 6),
    _RuijieFileTransServerAddr_Type()
)
ruijieFileTransServerAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieFileTransServerAddr.setStatus("current")


class _RuijieFileTransResult_Type(Integer32):
    """Custom type ruijieFileTransResult based on Integer32"""
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
        *(("success", 1),
          ("failure", 2),
          ("parametersIllegel", 3),
          ("timeout", 4))
    )


_RuijieFileTransResult_Type.__name__ = "Integer32"
_RuijieFileTransResult_Object = MibTableColumn
ruijieFileTransResult = _RuijieFileTransResult_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 11, 1, 1, 1, 7),
    _RuijieFileTransResult_Type()
)
ruijieFileTransResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFileTransResult.setStatus("current")
_RuijieFileTransComplete_Type = TruthValue
_RuijieFileTransComplete_Object = MibTableColumn
ruijieFileTransComplete = _RuijieFileTransComplete_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 11, 1, 1, 1, 8),
    _RuijieFileTransComplete_Type()
)
ruijieFileTransComplete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFileTransComplete.setStatus("current")
_RuijieFileTransDataLength_Type = Gauge32
_RuijieFileTransDataLength_Object = MibTableColumn
ruijieFileTransDataLength = _RuijieFileTransDataLength_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 11, 1, 1, 1, 9),
    _RuijieFileTransDataLength_Type()
)
ruijieFileTransDataLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFileTransDataLength.setStatus("current")
_RuijieFileTransEntryStatus_Type = RowStatus
_RuijieFileTransEntryStatus_Object = MibTableColumn
ruijieFileTransEntryStatus = _RuijieFileTransEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 11, 1, 1, 1, 10),
    _RuijieFileTransEntryStatus_Type()
)
ruijieFileTransEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieFileTransEntryStatus.setStatus("current")


class _RuijieFileTransServerAddr6_Type(OctetString):
    """Custom type ruijieFileTransServerAddr6 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_RuijieFileTransServerAddr6_Type.__name__ = "OctetString"
_RuijieFileTransServerAddr6_Object = MibTableColumn
ruijieFileTransServerAddr6 = _RuijieFileTransServerAddr6_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 11, 1, 1, 1, 11),
    _RuijieFileTransServerAddr6_Type()
)
ruijieFileTransServerAddr6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieFileTransServerAddr6.setStatus("current")
_RuijieFileTransUserName_Type = DisplayString
_RuijieFileTransUserName_Object = MibTableColumn
ruijieFileTransUserName = _RuijieFileTransUserName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 11, 1, 1, 1, 12),
    _RuijieFileTransUserName_Type()
)
ruijieFileTransUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieFileTransUserName.setStatus("current")
_RuijieFileTransPassWord_Type = DisplayString
_RuijieFileTransPassWord_Object = MibTableColumn
ruijieFileTransPassWord = _RuijieFileTransPassWord_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 11, 1, 1, 1, 13),
    _RuijieFileTransPassWord_Type()
)
ruijieFileTransPassWord.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieFileTransPassWord.setStatus("current")
_RuijieFileTransFailedReason_Type = DisplayString
_RuijieFileTransFailedReason_Object = MibTableColumn
ruijieFileTransFailedReason = _RuijieFileTransFailedReason_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 11, 1, 1, 1, 14),
    _RuijieFileTransFailedReason_Type()
)
ruijieFileTransFailedReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFileTransFailedReason.setStatus("current")


class _RuijieFileTransFileType_Type(Integer32):
    """Custom type ruijieFileTransFileType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("software-version-file", 1),
          ("config-file", 2),
          ("log-file", 3))
    )


_RuijieFileTransFileType_Type.__name__ = "Integer32"
_RuijieFileTransFileType_Object = MibTableColumn
ruijieFileTransFileType = _RuijieFileTransFileType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 11, 1, 1, 1, 15),
    _RuijieFileTransFileType_Type()
)
ruijieFileTransFileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieFileTransFileType.setStatus("current")
_RuijieFileTransServerPort_Type = Integer32
_RuijieFileTransServerPort_Object = MibTableColumn
ruijieFileTransServerPort = _RuijieFileTransServerPort_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 11, 1, 1, 1, 16),
    _RuijieFileTransServerPort_Type()
)
ruijieFileTransServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieFileTransServerPort.setStatus("current")


class _RuijieFileTransPortType_Type(Integer32):
    """Custom type ruijieFileTransPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("byInterfacePort", 1),
          ("byMgmtPort", 2))
    )


_RuijieFileTransPortType_Type.__name__ = "Integer32"
_RuijieFileTransPortType_Object = MibTableColumn
ruijieFileTransPortType = _RuijieFileTransPortType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 11, 1, 1, 1, 17),
    _RuijieFileTransPortType_Type()
)
ruijieFileTransPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieFileTransPortType.setStatus("current")
_RuijieFileSystemMaxRoom_Type = Integer32
_RuijieFileSystemMaxRoom_Object = MibScalar
ruijieFileSystemMaxRoom = _RuijieFileSystemMaxRoom_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 11, 1, 2),
    _RuijieFileSystemMaxRoom_Type()
)
ruijieFileSystemMaxRoom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFileSystemMaxRoom.setStatus("current")
_RuijieFileSystemAvailableRoom_Type = Integer32
_RuijieFileSystemAvailableRoom_Object = MibScalar
ruijieFileSystemAvailableRoom = _RuijieFileSystemAvailableRoom_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 11, 1, 3),
    _RuijieFileSystemAvailableRoom_Type()
)
ruijieFileSystemAvailableRoom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFileSystemAvailableRoom.setStatus("current")
_RuijieFileMIBConformance_ObjectIdentity = ObjectIdentity
ruijieFileMIBConformance = _RuijieFileMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 11, 2)
)
_RuijieFileMIBCompliances_ObjectIdentity = ObjectIdentity
ruijieFileMIBCompliances = _RuijieFileMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 11, 2, 1)
)
_RuijieFileMIBGroups_ObjectIdentity = ObjectIdentity
ruijieFileMIBGroups = _RuijieFileMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 11, 2, 2)
)

# Managed Objects groups

ruijieFileMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 11, 2, 2, 1)
)
ruijieFileMIBGroup.setObjects(
      *(("RUIJIE-FILE-MIB", "ruijieFileTransIndex"),
        ("RUIJIE-FILE-MIB", "ruijieFileTransOperType"),
        ("RUIJIE-FILE-MIB", "ruijieFileTransSrcFileName"),
        ("RUIJIE-FILE-MIB", "ruijieFileTransDescFileName"),
        ("RUIJIE-FILE-MIB", "ruijieFileTransServerAddr"),
        ("RUIJIE-FILE-MIB", "ruijieFileTransResult"),
        ("RUIJIE-FILE-MIB", "ruijieFileTransComplete"),
        ("RUIJIE-FILE-MIB", "ruijieFileTransDataLength"),
        ("RUIJIE-FILE-MIB", "ruijieFileTransEntryStatus"),
        ("RUIJIE-FILE-MIB", "ruijieFileTransServerAddr6"),
        ("RUIJIE-FILE-MIB", "ruijieFileTransUserName"),
        ("RUIJIE-FILE-MIB", "ruijieFileTransPassWord"),
        ("RUIJIE-FILE-MIB", "ruijieFileTransFailedReason"),
        ("RUIJIE-FILE-MIB", "ruijieFileTransFileType"),
        ("RUIJIE-FILE-MIB", "ruijieFileTransServerPort"),
        ("RUIJIE-FILE-MIB", "ruijieFileTransPortType"),
        ("RUIJIE-FILE-MIB", "ruijieFileSystemMaxRoom"),
        ("RUIJIE-FILE-MIB", "ruijieFileSystemAvailableRoom"))
)
if mibBuilder.loadTexts:
    ruijieFileMIBGroup.setStatus("current")

ruijieFileTransMeansMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 11, 2, 2, 2)
)
ruijieFileTransMeansMIBGroup.setObjects(
    ("RUIJIE-FILE-MIB", "ruijieFileTransMeans")
)
if mibBuilder.loadTexts:
    ruijieFileTransMeansMIBGroup.setStatus("current")


# Notification objects

ruijieFileSystemUpdateFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 11, 0, 1)
)
ruijieFileSystemUpdateFailTrap.setObjects(
    ("RUIJIE-FILE-MIB", "ruijieFileTransFailedReason")
)
if mibBuilder.loadTexts:
    ruijieFileSystemUpdateFailTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

ruijieFileMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 11, 2, 1, 1)
)
ruijieFileMIBCompliance.setObjects(
      *(("RUIJIE-FILE-MIB", "ruijieFileMIBGroup"),
        ("RUIJIE-FILE-MIB", "ruijieFileTransMeansMIBGroup"))
)
if mibBuilder.loadTexts:
    ruijieFileMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-FILE-MIB",
    **{"ruijieFileMIB": ruijieFileMIB,
       "ruijieFileMIBTraps": ruijieFileMIBTraps,
       "ruijieFileSystemUpdateFailTrap": ruijieFileSystemUpdateFailTrap,
       "ruijieFileMIBObjects": ruijieFileMIBObjects,
       "ruijieFileTransTable": ruijieFileTransTable,
       "ruijieFileTransEntry": ruijieFileTransEntry,
       "ruijieFileTransIndex": ruijieFileTransIndex,
       "ruijieFileTransMeans": ruijieFileTransMeans,
       "ruijieFileTransOperType": ruijieFileTransOperType,
       "ruijieFileTransSrcFileName": ruijieFileTransSrcFileName,
       "ruijieFileTransDescFileName": ruijieFileTransDescFileName,
       "ruijieFileTransServerAddr": ruijieFileTransServerAddr,
       "ruijieFileTransResult": ruijieFileTransResult,
       "ruijieFileTransComplete": ruijieFileTransComplete,
       "ruijieFileTransDataLength": ruijieFileTransDataLength,
       "ruijieFileTransEntryStatus": ruijieFileTransEntryStatus,
       "ruijieFileTransServerAddr6": ruijieFileTransServerAddr6,
       "ruijieFileTransUserName": ruijieFileTransUserName,
       "ruijieFileTransPassWord": ruijieFileTransPassWord,
       "ruijieFileTransFailedReason": ruijieFileTransFailedReason,
       "ruijieFileTransFileType": ruijieFileTransFileType,
       "ruijieFileTransServerPort": ruijieFileTransServerPort,
       "ruijieFileTransPortType": ruijieFileTransPortType,
       "ruijieFileSystemMaxRoom": ruijieFileSystemMaxRoom,
       "ruijieFileSystemAvailableRoom": ruijieFileSystemAvailableRoom,
       "ruijieFileMIBConformance": ruijieFileMIBConformance,
       "ruijieFileMIBCompliances": ruijieFileMIBCompliances,
       "ruijieFileMIBCompliance": ruijieFileMIBCompliance,
       "ruijieFileMIBGroups": ruijieFileMIBGroups,
       "ruijieFileMIBGroup": ruijieFileMIBGroup,
       "ruijieFileTransMeansMIBGroup": ruijieFileTransMeansMIBGroup}
)
