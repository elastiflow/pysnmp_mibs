# SNMP MIB module (ENDACE-ERFSTREAM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/endace_18418/ENDACE-ERFSTREAM-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 30 15:13:01 2025
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

(endace,) = mibBuilder.importSymbols(
    "ENDACE-MIB",
    "endace")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

endaceErfstreamMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 18418, 12)
)
if mibBuilder.loadTexts:
    endaceErfstreamMIB.setRevisions(
        ("2012-09-24 05:56",
         "2012-05-04 00:24")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class PipeIndex(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "x"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class VisionDBIndex(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "x"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class VisionDBVersionIndex(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



# MIB Managed Objects in the order of their OIDs

_ErfstreamVariables_ObjectIdentity = ObjectIdentity
erfstreamVariables = _ErfstreamVariables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18418, 12, 1)
)
_PipeInfoTable_Object = MibTable
pipeInfoTable = _PipeInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 18418, 12, 1, 1)
)
if mibBuilder.loadTexts:
    pipeInfoTable.setStatus("current")
_PipeInfoTableEntry_Object = MibTableRow
pipeInfoTableEntry = _PipeInfoTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 18418, 12, 1, 1, 1)
)
pipeInfoTableEntry.setIndexNames(
    (0, "ENDACE-ERFSTREAM-MIB", "pipeInfoIndex"),
)
if mibBuilder.loadTexts:
    pipeInfoTableEntry.setStatus("current")
_PipeInfoIndex_Type = PipeIndex
_PipeInfoIndex_Object = MibTableColumn
pipeInfoIndex = _PipeInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 18418, 12, 1, 1, 1, 1),
    _PipeInfoIndex_Type()
)
pipeInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pipeInfoIndex.setStatus("current")


class _PipeName_Type(DisplayString):
    """Custom type pipeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PipeName_Type.__name__ = "DisplayString"
_PipeName_Object = MibTableColumn
pipeName = _PipeName_Object(
    (1, 3, 6, 1, 4, 1, 18418, 12, 1, 1, 1, 2),
    _PipeName_Type()
)
pipeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pipeName.setStatus("current")
_PipeStatusTable_Object = MibTable
pipeStatusTable = _PipeStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 18418, 12, 1, 2)
)
if mibBuilder.loadTexts:
    pipeStatusTable.setStatus("current")
_PipeStatusTableEntry_Object = MibTableRow
pipeStatusTableEntry = _PipeStatusTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 18418, 12, 1, 2, 1)
)
pipeStatusTableEntry.setIndexNames(
    (0, "ENDACE-ERFSTREAM-MIB", "pipeStatusIndex"),
)
if mibBuilder.loadTexts:
    pipeStatusTableEntry.setStatus("current")
_PipeStatusIndex_Type = PipeIndex
_PipeStatusIndex_Object = MibTableColumn
pipeStatusIndex = _PipeStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 18418, 12, 1, 2, 1, 1),
    _PipeStatusIndex_Type()
)
pipeStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pipeStatusIndex.setStatus("current")
_PipeInputPackets_Type = Counter64
_PipeInputPackets_Object = MibTableColumn
pipeInputPackets = _PipeInputPackets_Object(
    (1, 3, 6, 1, 4, 1, 18418, 12, 1, 2, 1, 2),
    _PipeInputPackets_Type()
)
pipeInputPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pipeInputPackets.setStatus("current")
_PipeInputBytes_Type = Counter64
_PipeInputBytes_Object = MibTableColumn
pipeInputBytes = _PipeInputBytes_Object(
    (1, 3, 6, 1, 4, 1, 18418, 12, 1, 2, 1, 3),
    _PipeInputBytes_Type()
)
pipeInputBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pipeInputBytes.setStatus("current")
_PipeOutputPackets_Type = Counter64
_PipeOutputPackets_Object = MibTableColumn
pipeOutputPackets = _PipeOutputPackets_Object(
    (1, 3, 6, 1, 4, 1, 18418, 12, 1, 2, 1, 4),
    _PipeOutputPackets_Type()
)
pipeOutputPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pipeOutputPackets.setStatus("current")
_PipeOutputBytes_Type = Counter64
_PipeOutputBytes_Object = MibTableColumn
pipeOutputBytes = _PipeOutputBytes_Object(
    (1, 3, 6, 1, 4, 1, 18418, 12, 1, 2, 1, 5),
    _PipeOutputBytes_Type()
)
pipeOutputBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pipeOutputBytes.setStatus("current")
_PipeDroppedPackets_Type = Counter64
_PipeDroppedPackets_Object = MibTableColumn
pipeDroppedPackets = _PipeDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 18418, 12, 1, 2, 1, 6),
    _PipeDroppedPackets_Type()
)
pipeDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pipeDroppedPackets.setStatus("current")
_PipeDroppedBytes_Type = Counter64
_PipeDroppedBytes_Object = MibTableColumn
pipeDroppedBytes = _PipeDroppedBytes_Object(
    (1, 3, 6, 1, 4, 1, 18418, 12, 1, 2, 1, 7),
    _PipeDroppedBytes_Type()
)
pipeDroppedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pipeDroppedBytes.setStatus("current")
_PilotDroppedPackets_Type = Counter64
_PilotDroppedPackets_Object = MibTableColumn
pilotDroppedPackets = _PilotDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 18418, 12, 1, 2, 1, 8),
    _PilotDroppedPackets_Type()
)
pilotDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pilotDroppedPackets.setStatus("current")
_PilotDroppedBytes_Type = Counter64
_PilotDroppedBytes_Object = MibTableColumn
pilotDroppedBytes = _PilotDroppedBytes_Object(
    (1, 3, 6, 1, 4, 1, 18418, 12, 1, 2, 1, 9),
    _PilotDroppedBytes_Type()
)
pilotDroppedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pilotDroppedBytes.setStatus("current")
_VisionDroppedRecords_Type = Counter64
_VisionDroppedRecords_Object = MibTableColumn
visionDroppedRecords = _VisionDroppedRecords_Object(
    (1, 3, 6, 1, 4, 1, 18418, 12, 1, 2, 1, 10),
    _VisionDroppedRecords_Type()
)
visionDroppedRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    visionDroppedRecords.setStatus("current")
_PipeCurrentFlows_Type = Counter64
_PipeCurrentFlows_Object = MibTableColumn
pipeCurrentFlows = _PipeCurrentFlows_Object(
    (1, 3, 6, 1, 4, 1, 18418, 12, 1, 2, 1, 11),
    _PipeCurrentFlows_Type()
)
pipeCurrentFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pipeCurrentFlows.setStatus("current")
_VisionDBStatusTable_Object = MibTable
visionDBStatusTable = _VisionDBStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 18418, 12, 1, 3)
)
if mibBuilder.loadTexts:
    visionDBStatusTable.setStatus("current")
_VisionDBStatusTableEntry_Object = MibTableRow
visionDBStatusTableEntry = _VisionDBStatusTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 18418, 12, 1, 3, 1)
)
visionDBStatusTableEntry.setIndexNames(
    (0, "ENDACE-ERFSTREAM-MIB", "visionDBStatusVersionIndex"),
    (0, "ENDACE-ERFSTREAM-MIB", "visionDBStatusIndex"),
)
if mibBuilder.loadTexts:
    visionDBStatusTableEntry.setStatus("current")
_VisionDBStatusVersionIndex_Type = VisionDBVersionIndex
_VisionDBStatusVersionIndex_Object = MibTableColumn
visionDBStatusVersionIndex = _VisionDBStatusVersionIndex_Object(
    (1, 3, 6, 1, 4, 1, 18418, 12, 1, 3, 1, 1),
    _VisionDBStatusVersionIndex_Type()
)
visionDBStatusVersionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    visionDBStatusVersionIndex.setStatus("current")
_VisionDBStatusIndex_Type = VisionDBIndex
_VisionDBStatusIndex_Object = MibTableColumn
visionDBStatusIndex = _VisionDBStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 18418, 12, 1, 3, 1, 2),
    _VisionDBStatusIndex_Type()
)
visionDBStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    visionDBStatusIndex.setStatus("current")


class _VisionDBRotfileName_Type(DisplayString):
    """Custom type visionDBRotfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VisionDBRotfileName_Type.__name__ = "DisplayString"
_VisionDBRotfileName_Object = MibTableColumn
visionDBRotfileName = _VisionDBRotfileName_Object(
    (1, 3, 6, 1, 4, 1, 18418, 12, 1, 3, 1, 3),
    _VisionDBRotfileName_Type()
)
visionDBRotfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    visionDBRotfileName.setStatus("current")
_VisionDBUsage_Type = Counter32
_VisionDBUsage_Object = MibTableColumn
visionDBUsage = _VisionDBUsage_Object(
    (1, 3, 6, 1, 4, 1, 18418, 12, 1, 3, 1, 4),
    _VisionDBUsage_Type()
)
visionDBUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    visionDBUsage.setStatus("current")
_EventTraps_ObjectIdentity = ObjectIdentity
eventTraps = _EventTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18418, 12, 2)
)
_ErfstreamNotificationPrefix_ObjectIdentity = ObjectIdentity
erfstreamNotificationPrefix = _ErfstreamNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18418, 12, 2, 0)
)
_ErfstreamConf_ObjectIdentity = ObjectIdentity
erfstreamConf = _ErfstreamConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18418, 12, 3)
)
_ErfstreamGroups_ObjectIdentity = ObjectIdentity
erfstreamGroups = _ErfstreamGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18418, 12, 3, 1)
)

# Managed Objects groups

pipeAttributes = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 18418, 12, 3, 1, 1)
)
pipeAttributes.setObjects(
    ("ENDACE-ERFSTREAM-MIB", "pipeName")
)
if mibBuilder.loadTexts:
    pipeAttributes.setStatus("current")

pipeStatus = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 18418, 12, 3, 1, 2)
)
pipeStatus.setObjects(
      *(("ENDACE-ERFSTREAM-MIB", "pilotDroppedBytes"),
        ("ENDACE-ERFSTREAM-MIB", "pilotDroppedPackets"),
        ("ENDACE-ERFSTREAM-MIB", "pipeCurrentFlows"),
        ("ENDACE-ERFSTREAM-MIB", "pipeDroppedBytes"),
        ("ENDACE-ERFSTREAM-MIB", "pipeDroppedPackets"),
        ("ENDACE-ERFSTREAM-MIB", "pipeInputBytes"),
        ("ENDACE-ERFSTREAM-MIB", "pipeInputPackets"),
        ("ENDACE-ERFSTREAM-MIB", "pipeOutputBytes"),
        ("ENDACE-ERFSTREAM-MIB", "pipeOutputPackets"))
)
if mibBuilder.loadTexts:
    pipeStatus.setStatus("current")

visionAttributes = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 18418, 12, 3, 1, 5)
)
visionAttributes.setObjects(
      *(("ENDACE-ERFSTREAM-MIB", "visionDBRotfileName"),
        ("ENDACE-ERFSTREAM-MIB", "visionDBUsage"),
        ("ENDACE-ERFSTREAM-MIB", "visionDroppedRecords"))
)
if mibBuilder.loadTexts:
    visionAttributes.setStatus("current")


# Notification objects

pipeDropFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 12, 2, 0, 1)
)
pipeDropFault.setObjects(
    ("ENDACE-ERFSTREAM-MIB", "pipeName")
)
if mibBuilder.loadTexts:
    pipeDropFault.setStatus(
        "current"
    )

pipeDropNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 12, 2, 0, 2)
)
pipeDropNormal.setObjects(
    ("ENDACE-ERFSTREAM-MIB", "pipeName")
)
if mibBuilder.loadTexts:
    pipeDropNormal.setStatus(
        "current"
    )

pilotDropFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 12, 2, 0, 3)
)
pilotDropFault.setObjects(
    ("ENDACE-ERFSTREAM-MIB", "pipeName")
)
if mibBuilder.loadTexts:
    pilotDropFault.setStatus(
        "current"
    )

pilotDropNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 12, 2, 0, 4)
)
pilotDropNormal.setObjects(
    ("ENDACE-ERFSTREAM-MIB", "pipeName")
)
if mibBuilder.loadTexts:
    pilotDropNormal.setStatus(
        "current"
    )

visionDropFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 12, 2, 0, 5)
)
visionDropFault.setObjects(
    ("ENDACE-ERFSTREAM-MIB", "pipeName")
)
if mibBuilder.loadTexts:
    visionDropFault.setStatus(
        "current"
    )

visionDropNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 12, 2, 0, 6)
)
visionDropNormal.setObjects(
    ("ENDACE-ERFSTREAM-MIB", "pipeName")
)
if mibBuilder.loadTexts:
    visionDropNormal.setStatus(
        "current"
    )

visionMetadataDBFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 12, 2, 0, 7)
)
visionMetadataDBFull.setObjects(
    ("ENDACE-ERFSTREAM-MIB", "visionDBRotfileName")
)
if mibBuilder.loadTexts:
    visionMetadataDBFull.setStatus(
        "current"
    )

visionMetadataDBThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 12, 2, 0, 8)
)
visionMetadataDBThreshold.setObjects(
    ("ENDACE-ERFSTREAM-MIB", "visionDBRotfileName")
)
if mibBuilder.loadTexts:
    visionMetadataDBThreshold.setStatus(
        "current"
    )

visionMetadataDBNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 12, 2, 0, 9)
)
visionMetadataDBNormal.setObjects(
    ("ENDACE-ERFSTREAM-MIB", "visionDBRotfileName")
)
if mibBuilder.loadTexts:
    visionMetadataDBNormal.setStatus(
        "current"
    )

visionMetadataDBBelowFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 12, 2, 0, 10)
)
visionMetadataDBBelowFull.setObjects(
    ("ENDACE-ERFSTREAM-MIB", "visionDBRotfileName")
)
if mibBuilder.loadTexts:
    visionMetadataDBBelowFull.setStatus(
        "current"
    )


# Notifications groups

pipeEvents = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 18418, 12, 3, 1, 3)
)
pipeEvents.setObjects(
      *(("ENDACE-ERFSTREAM-MIB", "pipeDropFault"),
        ("ENDACE-ERFSTREAM-MIB", "pipeDropNormal"),
        ("ENDACE-ERFSTREAM-MIB", "pilotDropFault"),
        ("ENDACE-ERFSTREAM-MIB", "pilotDropNormal"),
        ("ENDACE-ERFSTREAM-MIB", "visionDropFault"),
        ("ENDACE-ERFSTREAM-MIB", "visionDropNormal"))
)
if mibBuilder.loadTexts:
    pipeEvents.setStatus(
        "current"
    )

visionEvents = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 18418, 12, 3, 1, 4)
)
visionEvents.setObjects(
      *(("ENDACE-ERFSTREAM-MIB", "visionMetadataDBFull"),
        ("ENDACE-ERFSTREAM-MIB", "visionMetadataDBThreshold"),
        ("ENDACE-ERFSTREAM-MIB", "visionMetadataDBNormal"),
        ("ENDACE-ERFSTREAM-MIB", "visionMetadataDBBelowFull"))
)
if mibBuilder.loadTexts:
    visionEvents.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENDACE-ERFSTREAM-MIB",
    **{"PipeIndex": PipeIndex,
       "VisionDBIndex": VisionDBIndex,
       "VisionDBVersionIndex": VisionDBVersionIndex,
       "endaceErfstreamMIB": endaceErfstreamMIB,
       "erfstreamVariables": erfstreamVariables,
       "pipeInfoTable": pipeInfoTable,
       "pipeInfoTableEntry": pipeInfoTableEntry,
       "pipeInfoIndex": pipeInfoIndex,
       "pipeName": pipeName,
       "pipeStatusTable": pipeStatusTable,
       "pipeStatusTableEntry": pipeStatusTableEntry,
       "pipeStatusIndex": pipeStatusIndex,
       "pipeInputPackets": pipeInputPackets,
       "pipeInputBytes": pipeInputBytes,
       "pipeOutputPackets": pipeOutputPackets,
       "pipeOutputBytes": pipeOutputBytes,
       "pipeDroppedPackets": pipeDroppedPackets,
       "pipeDroppedBytes": pipeDroppedBytes,
       "pilotDroppedPackets": pilotDroppedPackets,
       "pilotDroppedBytes": pilotDroppedBytes,
       "visionDroppedRecords": visionDroppedRecords,
       "pipeCurrentFlows": pipeCurrentFlows,
       "visionDBStatusTable": visionDBStatusTable,
       "visionDBStatusTableEntry": visionDBStatusTableEntry,
       "visionDBStatusVersionIndex": visionDBStatusVersionIndex,
       "visionDBStatusIndex": visionDBStatusIndex,
       "visionDBRotfileName": visionDBRotfileName,
       "visionDBUsage": visionDBUsage,
       "eventTraps": eventTraps,
       "erfstreamNotificationPrefix": erfstreamNotificationPrefix,
       "pipeDropFault": pipeDropFault,
       "pipeDropNormal": pipeDropNormal,
       "pilotDropFault": pilotDropFault,
       "pilotDropNormal": pilotDropNormal,
       "visionDropFault": visionDropFault,
       "visionDropNormal": visionDropNormal,
       "visionMetadataDBFull": visionMetadataDBFull,
       "visionMetadataDBThreshold": visionMetadataDBThreshold,
       "visionMetadataDBNormal": visionMetadataDBNormal,
       "visionMetadataDBBelowFull": visionMetadataDBBelowFull,
       "erfstreamConf": erfstreamConf,
       "erfstreamGroups": erfstreamGroups,
       "pipeAttributes": pipeAttributes,
       "pipeStatus": pipeStatus,
       "pipeEvents": pipeEvents,
       "visionEvents": visionEvents,
       "visionAttributes": visionAttributes}
)
