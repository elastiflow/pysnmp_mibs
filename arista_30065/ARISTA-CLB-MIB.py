# SNMP MIB module (ARISTA-CLB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/arista_30065/ARISTA-CLB-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 30 16:46:35 2025
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

(aristaMibs,) = mibBuilder.importSymbols(
    "ARISTA-SMI-MIB",
    "aristaMibs")

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
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

aristaClbMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 36)
)
if mibBuilder.loadTexts:
    aristaClbMIB.setRevisions(
        ("2024-05-20 00:00",
         "2024-04-30 00:00",
         "2024-03-19 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AristaClbPortGroupShortName(TextualConvention, OctetString):
    status = "current"
    displayHint = "100t"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )



# MIB Managed Objects in the order of their OIDs

_AristaClbMibNotifications_ObjectIdentity = ObjectIdentity
aristaClbMibNotifications = _AristaClbMibNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 36, 0)
)
_AristaClbMibObjects_ObjectIdentity = ObjectIdentity
aristaClbMibObjects = _AristaClbMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 36, 1)
)
_AristaClbPortGroupTable_Object = MibTable
aristaClbPortGroupTable = _AristaClbPortGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 36, 1, 1)
)
if mibBuilder.loadTexts:
    aristaClbPortGroupTable.setStatus("current")
_AristaClbPortGroupEntry_Object = MibTableRow
aristaClbPortGroupEntry = _AristaClbPortGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 36, 1, 1, 1)
)
aristaClbPortGroupEntry.setIndexNames(
    (0, "ARISTA-CLB-MIB", "aristaClbPortGroupIndex"),
)
if mibBuilder.loadTexts:
    aristaClbPortGroupEntry.setStatus("current")
_AristaClbPortGroupIndex_Type = AristaClbPortGroupShortName
_AristaClbPortGroupIndex_Object = MibTableColumn
aristaClbPortGroupIndex = _AristaClbPortGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 36, 1, 1, 1, 1),
    _AristaClbPortGroupIndex_Type()
)
aristaClbPortGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aristaClbPortGroupIndex.setStatus("current")
_AristaClbPortGroupLearnedFlows_Type = Gauge32
_AristaClbPortGroupLearnedFlows_Object = MibTableColumn
aristaClbPortGroupLearnedFlows = _AristaClbPortGroupLearnedFlows_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 36, 1, 1, 1, 2),
    _AristaClbPortGroupLearnedFlows_Type()
)
aristaClbPortGroupLearnedFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaClbPortGroupLearnedFlows.setStatus("current")
_AristaClbPortGroupAllocatedFlows_Type = Gauge32
_AristaClbPortGroupAllocatedFlows_Object = MibTableColumn
aristaClbPortGroupAllocatedFlows = _AristaClbPortGroupAllocatedFlows_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 36, 1, 1, 1, 3),
    _AristaClbPortGroupAllocatedFlows_Type()
)
aristaClbPortGroupAllocatedFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaClbPortGroupAllocatedFlows.setStatus("current")
_AristaClbPortGroupUnallocatedFlows_Type = Gauge32
_AristaClbPortGroupUnallocatedFlows_Object = MibTableColumn
aristaClbPortGroupUnallocatedFlows = _AristaClbPortGroupUnallocatedFlows_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 36, 1, 1, 1, 4),
    _AristaClbPortGroupUnallocatedFlows_Type()
)
aristaClbPortGroupUnallocatedFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaClbPortGroupUnallocatedFlows.setStatus("current")
_AristaClbPortGroupAllocatedFlowLimit_Type = Integer32
_AristaClbPortGroupAllocatedFlowLimit_Object = MibTableColumn
aristaClbPortGroupAllocatedFlowLimit = _AristaClbPortGroupAllocatedFlowLimit_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 36, 1, 1, 1, 5),
    _AristaClbPortGroupAllocatedFlowLimit_Type()
)
aristaClbPortGroupAllocatedFlowLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaClbPortGroupAllocatedFlowLimit.setStatus("current")
_AristaClbPortGroupUnmatchedNormalBytes_Type = Counter64
_AristaClbPortGroupUnmatchedNormalBytes_Object = MibTableColumn
aristaClbPortGroupUnmatchedNormalBytes = _AristaClbPortGroupUnmatchedNormalBytes_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 36, 1, 1, 1, 6),
    _AristaClbPortGroupUnmatchedNormalBytes_Type()
)
aristaClbPortGroupUnmatchedNormalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaClbPortGroupUnmatchedNormalBytes.setStatus("current")
_AristaClbPortGroupUnmatchedNormalPackets_Type = Counter64
_AristaClbPortGroupUnmatchedNormalPackets_Object = MibTableColumn
aristaClbPortGroupUnmatchedNormalPackets = _AristaClbPortGroupUnmatchedNormalPackets_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 36, 1, 1, 1, 7),
    _AristaClbPortGroupUnmatchedNormalPackets_Type()
)
aristaClbPortGroupUnmatchedNormalPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaClbPortGroupUnmatchedNormalPackets.setStatus("current")
_AristaClbPortGroupUnmatchedOverflowBytes_Type = Counter64
_AristaClbPortGroupUnmatchedOverflowBytes_Object = MibTableColumn
aristaClbPortGroupUnmatchedOverflowBytes = _AristaClbPortGroupUnmatchedOverflowBytes_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 36, 1, 1, 1, 8),
    _AristaClbPortGroupUnmatchedOverflowBytes_Type()
)
aristaClbPortGroupUnmatchedOverflowBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaClbPortGroupUnmatchedOverflowBytes.setStatus("current")
_AristaClbPortGroupUnmatchedOverflowPackets_Type = Counter64
_AristaClbPortGroupUnmatchedOverflowPackets_Object = MibTableColumn
aristaClbPortGroupUnmatchedOverflowPackets = _AristaClbPortGroupUnmatchedOverflowPackets_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 36, 1, 1, 1, 9),
    _AristaClbPortGroupUnmatchedOverflowPackets_Type()
)
aristaClbPortGroupUnmatchedOverflowPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaClbPortGroupUnmatchedOverflowPackets.setStatus("current")
_AristaClbPortGroupDiscontinuityTime_Type = TimeStamp
_AristaClbPortGroupDiscontinuityTime_Object = MibTableColumn
aristaClbPortGroupDiscontinuityTime = _AristaClbPortGroupDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 36, 1, 1, 1, 10),
    _AristaClbPortGroupDiscontinuityTime_Type()
)
aristaClbPortGroupDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaClbPortGroupDiscontinuityTime.setStatus("current")
_AristaClbPortGroupAllocatedFlowThreshold_Type = Integer32
_AristaClbPortGroupAllocatedFlowThreshold_Object = MibTableColumn
aristaClbPortGroupAllocatedFlowThreshold = _AristaClbPortGroupAllocatedFlowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 36, 1, 1, 1, 11),
    _AristaClbPortGroupAllocatedFlowThreshold_Type()
)
aristaClbPortGroupAllocatedFlowThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaClbPortGroupAllocatedFlowThreshold.setStatus("current")
_AristaClbPortGroupNameMappingTable_Object = MibTable
aristaClbPortGroupNameMappingTable = _AristaClbPortGroupNameMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 36, 1, 2)
)
if mibBuilder.loadTexts:
    aristaClbPortGroupNameMappingTable.setStatus("current")
_AristaClbPortGroupNameMappingEntry_Object = MibTableRow
aristaClbPortGroupNameMappingEntry = _AristaClbPortGroupNameMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 36, 1, 2, 1)
)
aristaClbPortGroupNameMappingEntry.setIndexNames(
    (0, "ARISTA-CLB-MIB", "aristaClbPortGroupIndex"),
)
if mibBuilder.loadTexts:
    aristaClbPortGroupNameMappingEntry.setStatus("current")
_AristaClbPortGroupNameMappingFullName_Type = OctetString
_AristaClbPortGroupNameMappingFullName_Object = MibTableColumn
aristaClbPortGroupNameMappingFullName = _AristaClbPortGroupNameMappingFullName_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 36, 1, 2, 1, 1),
    _AristaClbPortGroupNameMappingFullName_Type()
)
aristaClbPortGroupNameMappingFullName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaClbPortGroupNameMappingFullName.setStatus("current")
_AristaClbDestinationInterfaceTable_Object = MibTable
aristaClbDestinationInterfaceTable = _AristaClbDestinationInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 36, 1, 3)
)
if mibBuilder.loadTexts:
    aristaClbDestinationInterfaceTable.setStatus("current")
_AristaClbDestinationInterfaceEntry_Object = MibTableRow
aristaClbDestinationInterfaceEntry = _AristaClbDestinationInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 36, 1, 3, 1)
)
aristaClbDestinationInterfaceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    aristaClbDestinationInterfaceEntry.setStatus("current")
_AristaClbDestinationInterfaceActiveFlows_Type = Gauge32
_AristaClbDestinationInterfaceActiveFlows_Object = MibTableColumn
aristaClbDestinationInterfaceActiveFlows = _AristaClbDestinationInterfaceActiveFlows_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 36, 1, 3, 1, 1),
    _AristaClbDestinationInterfaceActiveFlows_Type()
)
aristaClbDestinationInterfaceActiveFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaClbDestinationInterfaceActiveFlows.setStatus("current")


class _AristaClbStatus_Type(Integer32):
    """Custom type aristaClbStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("monitor", 1),
          ("enabled", 2))
    )


_AristaClbStatus_Type.__name__ = "Integer32"
_AristaClbStatus_Object = MibScalar
aristaClbStatus = _AristaClbStatus_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 36, 1, 4),
    _AristaClbStatus_Type()
)
aristaClbStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaClbStatus.setStatus("current")
_AristaClbTotalAllocatedFlows_Type = Gauge32
_AristaClbTotalAllocatedFlows_Object = MibScalar
aristaClbTotalAllocatedFlows = _AristaClbTotalAllocatedFlows_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 36, 1, 5),
    _AristaClbTotalAllocatedFlows_Type()
)
aristaClbTotalAllocatedFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaClbTotalAllocatedFlows.setStatus("current")
_AristaClbTotalUnallocatedFlows_Type = Gauge32
_AristaClbTotalUnallocatedFlows_Object = MibScalar
aristaClbTotalUnallocatedFlows = _AristaClbTotalUnallocatedFlows_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 36, 1, 6),
    _AristaClbTotalUnallocatedFlows_Type()
)
aristaClbTotalUnallocatedFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaClbTotalUnallocatedFlows.setStatus("current")
_AristaClbTotalLearnedFlows_Type = Gauge32
_AristaClbTotalLearnedFlows_Object = MibScalar
aristaClbTotalLearnedFlows = _AristaClbTotalLearnedFlows_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 36, 1, 7),
    _AristaClbTotalLearnedFlows_Type()
)
aristaClbTotalLearnedFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaClbTotalLearnedFlows.setStatus("current")
_AristaClbMibConformance_ObjectIdentity = ObjectIdentity
aristaClbMibConformance = _AristaClbMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 36, 2)
)
_AristaClbMibCompliances_ObjectIdentity = ObjectIdentity
aristaClbMibCompliances = _AristaClbMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 36, 2, 1)
)
_AristaClbMibGroups_ObjectIdentity = ObjectIdentity
aristaClbMibGroups = _AristaClbMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 36, 2, 2)
)

# Managed Objects groups

aristaClbMibGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30065, 3, 36, 2, 2, 1)
)
aristaClbMibGroup.setObjects(
      *(("ARISTA-CLB-MIB", "aristaClbPortGroupLearnedFlows"),
        ("ARISTA-CLB-MIB", "aristaClbPortGroupAllocatedFlows"),
        ("ARISTA-CLB-MIB", "aristaClbPortGroupUnallocatedFlows"),
        ("ARISTA-CLB-MIB", "aristaClbPortGroupAllocatedFlowLimit"),
        ("ARISTA-CLB-MIB", "aristaClbPortGroupUnmatchedNormalBytes"),
        ("ARISTA-CLB-MIB", "aristaClbPortGroupUnmatchedNormalPackets"),
        ("ARISTA-CLB-MIB", "aristaClbPortGroupUnmatchedOverflowBytes"),
        ("ARISTA-CLB-MIB", "aristaClbPortGroupUnmatchedOverflowPackets"),
        ("ARISTA-CLB-MIB", "aristaClbPortGroupDiscontinuityTime"),
        ("ARISTA-CLB-MIB", "aristaClbPortGroupNameMappingFullName"),
        ("ARISTA-CLB-MIB", "aristaClbDestinationInterfaceActiveFlows"),
        ("ARISTA-CLB-MIB", "aristaClbPortGroupAllocatedFlowThreshold"),
        ("ARISTA-CLB-MIB", "aristaClbStatus"),
        ("ARISTA-CLB-MIB", "aristaClbTotalAllocatedFlows"),
        ("ARISTA-CLB-MIB", "aristaClbTotalUnallocatedFlows"),
        ("ARISTA-CLB-MIB", "aristaClbTotalLearnedFlows"))
)
if mibBuilder.loadTexts:
    aristaClbMibGroup.setStatus("current")


# Notification objects

aristaClbPortGroupAllocatedFlowAtOrAboveThresholdWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 30065, 3, 36, 0, 1)
)
aristaClbPortGroupAllocatedFlowAtOrAboveThresholdWarning.setObjects(
      *(("ARISTA-CLB-MIB", "aristaClbPortGroupNameMappingFullName"),
        ("ARISTA-CLB-MIB", "aristaClbPortGroupAllocatedFlows"),
        ("ARISTA-CLB-MIB", "aristaClbPortGroupUnallocatedFlows"),
        ("ARISTA-CLB-MIB", "aristaClbPortGroupLearnedFlows"),
        ("ARISTA-CLB-MIB", "aristaClbPortGroupAllocatedFlowThreshold"))
)
if mibBuilder.loadTexts:
    aristaClbPortGroupAllocatedFlowAtOrAboveThresholdWarning.setStatus(
        "current"
    )

aristaClbPortGroupAllocatedFlowBelowThresholdWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 30065, 3, 36, 0, 2)
)
aristaClbPortGroupAllocatedFlowBelowThresholdWarning.setObjects(
      *(("ARISTA-CLB-MIB", "aristaClbPortGroupNameMappingFullName"),
        ("ARISTA-CLB-MIB", "aristaClbPortGroupAllocatedFlows"),
        ("ARISTA-CLB-MIB", "aristaClbPortGroupUnallocatedFlows"),
        ("ARISTA-CLB-MIB", "aristaClbPortGroupLearnedFlows"),
        ("ARISTA-CLB-MIB", "aristaClbPortGroupAllocatedFlowThreshold"))
)
if mibBuilder.loadTexts:
    aristaClbPortGroupAllocatedFlowBelowThresholdWarning.setStatus(
        "current"
    )

aristaClbPortGroupAllocatedFlowAtOrAboveLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 30065, 3, 36, 0, 3)
)
aristaClbPortGroupAllocatedFlowAtOrAboveLimit.setObjects(
      *(("ARISTA-CLB-MIB", "aristaClbPortGroupNameMappingFullName"),
        ("ARISTA-CLB-MIB", "aristaClbPortGroupAllocatedFlows"),
        ("ARISTA-CLB-MIB", "aristaClbPortGroupUnallocatedFlows"),
        ("ARISTA-CLB-MIB", "aristaClbPortGroupLearnedFlows"),
        ("ARISTA-CLB-MIB", "aristaClbPortGroupAllocatedFlowLimit"))
)
if mibBuilder.loadTexts:
    aristaClbPortGroupAllocatedFlowAtOrAboveLimit.setStatus(
        "current"
    )

aristaClbPortGroupAllocatedFlowBelowLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 30065, 3, 36, 0, 4)
)
aristaClbPortGroupAllocatedFlowBelowLimit.setObjects(
      *(("ARISTA-CLB-MIB", "aristaClbPortGroupNameMappingFullName"),
        ("ARISTA-CLB-MIB", "aristaClbPortGroupAllocatedFlows"),
        ("ARISTA-CLB-MIB", "aristaClbPortGroupUnallocatedFlows"),
        ("ARISTA-CLB-MIB", "aristaClbPortGroupLearnedFlows"),
        ("ARISTA-CLB-MIB", "aristaClbPortGroupAllocatedFlowLimit"))
)
if mibBuilder.loadTexts:
    aristaClbPortGroupAllocatedFlowBelowLimit.setStatus(
        "current"
    )


# Notifications groups

aristaClbNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 30065, 3, 36, 2, 2, 2)
)
aristaClbNotificationGroup.setObjects(
      *(("ARISTA-CLB-MIB", "aristaClbPortGroupAllocatedFlowAtOrAboveThresholdWarning"),
        ("ARISTA-CLB-MIB", "aristaClbPortGroupAllocatedFlowBelowThresholdWarning"),
        ("ARISTA-CLB-MIB", "aristaClbPortGroupAllocatedFlowAtOrAboveLimit"),
        ("ARISTA-CLB-MIB", "aristaClbPortGroupAllocatedFlowBelowLimit"))
)
if mibBuilder.loadTexts:
    aristaClbNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

aristaClbMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 30065, 3, 36, 2, 1, 1)
)
aristaClbMibCompliance.setObjects(
      *(("ARISTA-CLB-MIB", "aristaClbMibGroup"),
        ("ARISTA-CLB-MIB", "aristaClbNotificationGroup"))
)
if mibBuilder.loadTexts:
    aristaClbMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARISTA-CLB-MIB",
    **{"AristaClbPortGroupShortName": AristaClbPortGroupShortName,
       "aristaClbMIB": aristaClbMIB,
       "aristaClbMibNotifications": aristaClbMibNotifications,
       "aristaClbPortGroupAllocatedFlowAtOrAboveThresholdWarning": aristaClbPortGroupAllocatedFlowAtOrAboveThresholdWarning,
       "aristaClbPortGroupAllocatedFlowBelowThresholdWarning": aristaClbPortGroupAllocatedFlowBelowThresholdWarning,
       "aristaClbPortGroupAllocatedFlowAtOrAboveLimit": aristaClbPortGroupAllocatedFlowAtOrAboveLimit,
       "aristaClbPortGroupAllocatedFlowBelowLimit": aristaClbPortGroupAllocatedFlowBelowLimit,
       "aristaClbMibObjects": aristaClbMibObjects,
       "aristaClbPortGroupTable": aristaClbPortGroupTable,
       "aristaClbPortGroupEntry": aristaClbPortGroupEntry,
       "aristaClbPortGroupIndex": aristaClbPortGroupIndex,
       "aristaClbPortGroupLearnedFlows": aristaClbPortGroupLearnedFlows,
       "aristaClbPortGroupAllocatedFlows": aristaClbPortGroupAllocatedFlows,
       "aristaClbPortGroupUnallocatedFlows": aristaClbPortGroupUnallocatedFlows,
       "aristaClbPortGroupAllocatedFlowLimit": aristaClbPortGroupAllocatedFlowLimit,
       "aristaClbPortGroupUnmatchedNormalBytes": aristaClbPortGroupUnmatchedNormalBytes,
       "aristaClbPortGroupUnmatchedNormalPackets": aristaClbPortGroupUnmatchedNormalPackets,
       "aristaClbPortGroupUnmatchedOverflowBytes": aristaClbPortGroupUnmatchedOverflowBytes,
       "aristaClbPortGroupUnmatchedOverflowPackets": aristaClbPortGroupUnmatchedOverflowPackets,
       "aristaClbPortGroupDiscontinuityTime": aristaClbPortGroupDiscontinuityTime,
       "aristaClbPortGroupAllocatedFlowThreshold": aristaClbPortGroupAllocatedFlowThreshold,
       "aristaClbPortGroupNameMappingTable": aristaClbPortGroupNameMappingTable,
       "aristaClbPortGroupNameMappingEntry": aristaClbPortGroupNameMappingEntry,
       "aristaClbPortGroupNameMappingFullName": aristaClbPortGroupNameMappingFullName,
       "aristaClbDestinationInterfaceTable": aristaClbDestinationInterfaceTable,
       "aristaClbDestinationInterfaceEntry": aristaClbDestinationInterfaceEntry,
       "aristaClbDestinationInterfaceActiveFlows": aristaClbDestinationInterfaceActiveFlows,
       "aristaClbStatus": aristaClbStatus,
       "aristaClbTotalAllocatedFlows": aristaClbTotalAllocatedFlows,
       "aristaClbTotalUnallocatedFlows": aristaClbTotalUnallocatedFlows,
       "aristaClbTotalLearnedFlows": aristaClbTotalLearnedFlows,
       "aristaClbMibConformance": aristaClbMibConformance,
       "aristaClbMibCompliances": aristaClbMibCompliances,
       "aristaClbMibCompliance": aristaClbMibCompliance,
       "aristaClbMibGroups": aristaClbMibGroups,
       "aristaClbMibGroup": aristaClbMibGroup,
       "aristaClbNotificationGroup": aristaClbNotificationGroup}
)
