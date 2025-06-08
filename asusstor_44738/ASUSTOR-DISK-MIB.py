# SNMP MIB module (ASUSTOR-DISK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/asusstor_44738/ASUSTOR-DISK-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 30 16:41:54 2025
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Asustor_ObjectIdentity = ObjectIdentity
asustor = _Asustor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44738)
)
_AsustorDisk_ObjectIdentity = ObjectIdentity
asustorDisk = _AsustorDisk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44738, 4)
)
_DiskTable_Object = MibTable
diskTable = _DiskTable_Object(
    (1, 3, 6, 1, 4, 1, 44738, 4, 1)
)
if mibBuilder.loadTexts:
    diskTable.setStatus("current")
_DiskEntry_Object = MibTableRow
diskEntry = _DiskEntry_Object(
    (1, 3, 6, 1, 4, 1, 44738, 4, 1, 1)
)
diskEntry.setIndexNames(
    (0, "ASUSTOR-DISK-MIB", "diskIndex"),
)
if mibBuilder.loadTexts:
    diskEntry.setStatus("current")


class _DiskIndex_Type(Integer32):
    """Custom type diskIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DiskIndex_Type.__name__ = "Integer32"
_DiskIndex_Object = MibTableColumn
diskIndex = _DiskIndex_Object(
    (1, 3, 6, 1, 4, 1, 44738, 4, 1, 1, 1),
    _DiskIndex_Type()
)
diskIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    diskIndex.setStatus("current")
_DiskID_Type = OctetString
_DiskID_Object = MibTableColumn
diskID = _DiskID_Object(
    (1, 3, 6, 1, 4, 1, 44738, 4, 1, 1, 2),
    _DiskID_Type()
)
diskID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskID.setStatus("current")
_DiskModel_Type = OctetString
_DiskModel_Object = MibTableColumn
diskModel = _DiskModel_Object(
    (1, 3, 6, 1, 4, 1, 44738, 4, 1, 1, 3),
    _DiskModel_Type()
)
diskModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskModel.setStatus("current")
_DiskType_Type = OctetString
_DiskType_Object = MibTableColumn
diskType = _DiskType_Object(
    (1, 3, 6, 1, 4, 1, 44738, 4, 1, 1, 4),
    _DiskType_Type()
)
diskType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskType.setStatus("current")
_DiskStatus_Type = OctetString
_DiskStatus_Object = MibTableColumn
diskStatus = _DiskStatus_Object(
    (1, 3, 6, 1, 4, 1, 44738, 4, 1, 1, 5),
    _DiskStatus_Type()
)
diskStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskStatus.setStatus("current")
_DiskTemperature_Type = Integer32
_DiskTemperature_Object = MibTableColumn
diskTemperature = _DiskTemperature_Object(
    (1, 3, 6, 1, 4, 1, 44738, 4, 1, 1, 6),
    _DiskTemperature_Type()
)
diskTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskTemperature.setStatus("current")
_DiskSize_Type = Integer32
_DiskSize_Object = MibTableColumn
diskSize = _DiskSize_Object(
    (1, 3, 6, 1, 4, 1, 44738, 4, 1, 1, 7),
    _DiskSize_Type()
)
diskSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskSize.setStatus("current")
_DiskSmartInfo_Type = OctetString
_DiskSmartInfo_Object = MibTableColumn
diskSmartInfo = _DiskSmartInfo_Object(
    (1, 3, 6, 1, 4, 1, 44738, 4, 1, 1, 8),
    _DiskSmartInfo_Type()
)
diskSmartInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskSmartInfo.setStatus("current")
_DiskConformance_ObjectIdentity = ObjectIdentity
diskConformance = _DiskConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44738, 4, 2)
)
_DiskCompliances_ObjectIdentity = ObjectIdentity
diskCompliances = _DiskCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44738, 4, 2, 1)
)
_DiskGroups_ObjectIdentity = ObjectIdentity
diskGroups = _DiskGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44738, 4, 2, 2)
)
_AsustorVolume_ObjectIdentity = ObjectIdentity
asustorVolume = _AsustorVolume_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44738, 5)
)
_VolumeTable_Object = MibTable
volumeTable = _VolumeTable_Object(
    (1, 3, 6, 1, 4, 1, 44738, 5, 1)
)
if mibBuilder.loadTexts:
    volumeTable.setStatus("current")
_VolumeEntry_Object = MibTableRow
volumeEntry = _VolumeEntry_Object(
    (1, 3, 6, 1, 4, 1, 44738, 5, 1, 1)
)
volumeEntry.setIndexNames(
    (0, "ASUSTOR-DISK-MIB", "volumeIndex"),
)
if mibBuilder.loadTexts:
    volumeEntry.setStatus("current")


class _VolumeIndex_Type(Integer32):
    """Custom type volumeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_VolumeIndex_Type.__name__ = "Integer32"
_VolumeIndex_Object = MibTableColumn
volumeIndex = _VolumeIndex_Object(
    (1, 3, 6, 1, 4, 1, 44738, 5, 1, 1, 1),
    _VolumeIndex_Type()
)
volumeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    volumeIndex.setStatus("current")
_VolumeName_Type = OctetString
_VolumeName_Object = MibTableColumn
volumeName = _VolumeName_Object(
    (1, 3, 6, 1, 4, 1, 44738, 5, 1, 1, 2),
    _VolumeName_Type()
)
volumeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeName.setStatus("current")
_VolumeLevel_Type = OctetString
_VolumeLevel_Object = MibTableColumn
volumeLevel = _VolumeLevel_Object(
    (1, 3, 6, 1, 4, 1, 44738, 5, 1, 1, 3),
    _VolumeLevel_Type()
)
volumeLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeLevel.setStatus("current")
_VolumeStatus_Type = OctetString
_VolumeStatus_Object = MibTableColumn
volumeStatus = _VolumeStatus_Object(
    (1, 3, 6, 1, 4, 1, 44738, 5, 1, 1, 4),
    _VolumeStatus_Type()
)
volumeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeStatus.setStatus("current")
_VolumeFileSystem_Type = OctetString
_VolumeFileSystem_Object = MibTableColumn
volumeFileSystem = _VolumeFileSystem_Object(
    (1, 3, 6, 1, 4, 1, 44738, 5, 1, 1, 5),
    _VolumeFileSystem_Type()
)
volumeFileSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeFileSystem.setStatus("current")
_VolumeTotalSize_Type = Integer32
_VolumeTotalSize_Object = MibTableColumn
volumeTotalSize = _VolumeTotalSize_Object(
    (1, 3, 6, 1, 4, 1, 44738, 5, 1, 1, 6),
    _VolumeTotalSize_Type()
)
volumeTotalSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeTotalSize.setStatus("current")
_VolumeFreeSize_Type = Integer32
_VolumeFreeSize_Object = MibTableColumn
volumeFreeSize = _VolumeFreeSize_Object(
    (1, 3, 6, 1, 4, 1, 44738, 5, 1, 1, 7),
    _VolumeFreeSize_Type()
)
volumeFreeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeFreeSize.setStatus("current")

# Managed Objects groups

diskGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 44738, 4, 2, 2, 1)
)
diskGroup.setObjects(
      *(("ASUSTOR-DISK-MIB", "diskID"),
        ("ASUSTOR-DISK-MIB", "diskModel"),
        ("ASUSTOR-DISK-MIB", "diskType"),
        ("ASUSTOR-DISK-MIB", "diskStatus"),
        ("ASUSTOR-DISK-MIB", "diskTemperature"))
)
if mibBuilder.loadTexts:
    diskGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

diskCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 44738, 4, 2, 1, 1)
)
diskCompliance.setObjects(
    ("ASUSTOR-DISK-MIB", "diskGroup")
)
if mibBuilder.loadTexts:
    diskCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASUSTOR-DISK-MIB",
    **{"asustor": asustor,
       "asustorDisk": asustorDisk,
       "diskTable": diskTable,
       "diskEntry": diskEntry,
       "diskIndex": diskIndex,
       "diskID": diskID,
       "diskModel": diskModel,
       "diskType": diskType,
       "diskStatus": diskStatus,
       "diskTemperature": diskTemperature,
       "diskSize": diskSize,
       "diskSmartInfo": diskSmartInfo,
       "diskConformance": diskConformance,
       "diskCompliances": diskCompliances,
       "diskCompliance": diskCompliance,
       "diskGroups": diskGroups,
       "diskGroup": diskGroup,
       "asustorVolume": asustorVolume,
       "volumeTable": volumeTable,
       "volumeEntry": volumeEntry,
       "volumeIndex": volumeIndex,
       "volumeName": volumeName,
       "volumeLevel": volumeLevel,
       "volumeStatus": volumeStatus,
       "volumeFileSystem": volumeFileSystem,
       "volumeTotalSize": volumeTotalSize,
       "volumeFreeSize": volumeFreeSize}
)
