# SNMP MIB module (BELAIR-RSTP) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ericsson_15768/BELAIR-RSTP.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 16:08:43 2025
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

(belairProtocols,) = mibBuilder.importSymbols(
    "BELAIR-SMI",
    "belairProtocols")

(BelAirAdminState,) = mibBuilder.importSymbols(
    "BELAIR-TC",
    "BelAirAdminState")

(BridgeId,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "BridgeId")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

belairRstpMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 5, 2)
)
if mibBuilder.loadTexts:
    belairRstpMib.setRevisions(
        ("2008-11-26 22:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BelairRstpObjects_ObjectIdentity = ObjectIdentity
belairRstpObjects = _BelairRstpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 5, 2, 1)
)
_BaRstpPortIfTable_Object = MibTable
baRstpPortIfTable = _BaRstpPortIfTable_Object(
    (1, 3, 6, 1, 4, 1, 15768, 5, 2, 1, 1)
)
if mibBuilder.loadTexts:
    baRstpPortIfTable.setStatus("current")
_BaRstpPortIfEntry_Object = MibTableRow
baRstpPortIfEntry = _BaRstpPortIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 15768, 5, 2, 1, 1, 1)
)
baRstpPortIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    baRstpPortIfEntry.setStatus("current")


class _BaRstpPortPriority_Type(Integer32):
    """Custom type baRstpPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BaRstpPortPriority_Type.__name__ = "Integer32"
_BaRstpPortPriority_Object = MibTableColumn
baRstpPortPriority = _BaRstpPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 15768, 5, 2, 1, 1, 1, 1),
    _BaRstpPortPriority_Type()
)
baRstpPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    baRstpPortPriority.setStatus("current")


class _BaRstpPortState_Type(Integer32):
    """Custom type baRstpPortState based on Integer32"""
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
        *(("disabled", 1),
          ("blocking", 2),
          ("listening", 3),
          ("learning", 4),
          ("forwarding", 5),
          ("broken", 6))
    )


_BaRstpPortState_Type.__name__ = "Integer32"
_BaRstpPortState_Object = MibTableColumn
baRstpPortState = _BaRstpPortState_Object(
    (1, 3, 6, 1, 4, 1, 15768, 5, 2, 1, 1, 1, 2),
    _BaRstpPortState_Type()
)
baRstpPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baRstpPortState.setStatus("current")
_BaRstpPortEnable_Type = BelAirAdminState
_BaRstpPortEnable_Object = MibTableColumn
baRstpPortEnable = _BaRstpPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 15768, 5, 2, 1, 1, 1, 3),
    _BaRstpPortEnable_Type()
)
baRstpPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    baRstpPortEnable.setStatus("current")


class _BaRstpPortPathCost_Type(Integer32):
    """Custom type baRstpPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200000000),
    )


_BaRstpPortPathCost_Type.__name__ = "Integer32"
_BaRstpPortPathCost_Object = MibTableColumn
baRstpPortPathCost = _BaRstpPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 15768, 5, 2, 1, 1, 1, 4),
    _BaRstpPortPathCost_Type()
)
baRstpPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    baRstpPortPathCost.setStatus("current")
_BaRstpPortDesignatedRoot_Type = BridgeId
_BaRstpPortDesignatedRoot_Object = MibTableColumn
baRstpPortDesignatedRoot = _BaRstpPortDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 15768, 5, 2, 1, 1, 1, 5),
    _BaRstpPortDesignatedRoot_Type()
)
baRstpPortDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baRstpPortDesignatedRoot.setStatus("current")
_BaRstpPortDesignatedCost_Type = Integer32
_BaRstpPortDesignatedCost_Object = MibTableColumn
baRstpPortDesignatedCost = _BaRstpPortDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 15768, 5, 2, 1, 1, 1, 6),
    _BaRstpPortDesignatedCost_Type()
)
baRstpPortDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baRstpPortDesignatedCost.setStatus("current")
_BaRstpPortDesignatedBridge_Type = BridgeId
_BaRstpPortDesignatedBridge_Object = MibTableColumn
baRstpPortDesignatedBridge = _BaRstpPortDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 15768, 5, 2, 1, 1, 1, 7),
    _BaRstpPortDesignatedBridge_Type()
)
baRstpPortDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baRstpPortDesignatedBridge.setStatus("current")


class _BaRstpPortDesignatedPort_Type(OctetString):
    """Custom type baRstpPortDesignatedPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_BaRstpPortDesignatedPort_Type.__name__ = "OctetString"
_BaRstpPortDesignatedPort_Object = MibTableColumn
baRstpPortDesignatedPort = _BaRstpPortDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 15768, 5, 2, 1, 1, 1, 8),
    _BaRstpPortDesignatedPort_Type()
)
baRstpPortDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baRstpPortDesignatedPort.setStatus("current")
_BaRstpPortForwardTransitions_Type = Integer32
_BaRstpPortForwardTransitions_Object = MibTableColumn
baRstpPortForwardTransitions = _BaRstpPortForwardTransitions_Object(
    (1, 3, 6, 1, 4, 1, 15768, 5, 2, 1, 1, 1, 9),
    _BaRstpPortForwardTransitions_Type()
)
baRstpPortForwardTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baRstpPortForwardTransitions.setStatus("current")
_BaRstpPortProtocolMigration_Type = TruthValue
_BaRstpPortProtocolMigration_Object = MibTableColumn
baRstpPortProtocolMigration = _BaRstpPortProtocolMigration_Object(
    (1, 3, 6, 1, 4, 1, 15768, 5, 2, 1, 1, 1, 10),
    _BaRstpPortProtocolMigration_Type()
)
baRstpPortProtocolMigration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    baRstpPortProtocolMigration.setStatus("current")
_BaRstpPortAdminEdgePort_Type = TruthValue
_BaRstpPortAdminEdgePort_Object = MibTableColumn
baRstpPortAdminEdgePort = _BaRstpPortAdminEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 15768, 5, 2, 1, 1, 1, 11),
    _BaRstpPortAdminEdgePort_Type()
)
baRstpPortAdminEdgePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    baRstpPortAdminEdgePort.setStatus("current")
_BaRstpPortOperEdgePort_Type = TruthValue
_BaRstpPortOperEdgePort_Object = MibTableColumn
baRstpPortOperEdgePort = _BaRstpPortOperEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 15768, 5, 2, 1, 1, 1, 12),
    _BaRstpPortOperEdgePort_Type()
)
baRstpPortOperEdgePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baRstpPortOperEdgePort.setStatus("current")


class _BaRstpPortAdminPointToPoint_Type(Integer32):
    """Custom type baRstpPortAdminPointToPoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forceTrue", 0),
          ("forceFalse", 1),
          ("auto", 2))
    )


_BaRstpPortAdminPointToPoint_Type.__name__ = "Integer32"
_BaRstpPortAdminPointToPoint_Object = MibTableColumn
baRstpPortAdminPointToPoint = _BaRstpPortAdminPointToPoint_Object(
    (1, 3, 6, 1, 4, 1, 15768, 5, 2, 1, 1, 1, 13),
    _BaRstpPortAdminPointToPoint_Type()
)
baRstpPortAdminPointToPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    baRstpPortAdminPointToPoint.setStatus("current")
_BaRstpPortOperPointToPoint_Type = TruthValue
_BaRstpPortOperPointToPoint_Object = MibTableColumn
baRstpPortOperPointToPoint = _BaRstpPortOperPointToPoint_Object(
    (1, 3, 6, 1, 4, 1, 15768, 5, 2, 1, 1, 1, 14),
    _BaRstpPortOperPointToPoint_Type()
)
baRstpPortOperPointToPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baRstpPortOperPointToPoint.setStatus("current")
_BaRstpCostConfigTable_Object = MibTable
baRstpCostConfigTable = _BaRstpCostConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 15768, 5, 2, 1, 2)
)
if mibBuilder.loadTexts:
    baRstpCostConfigTable.setStatus("current")
_BaRstpCostConfigEntry_Object = MibTableRow
baRstpCostConfigEntry = _BaRstpCostConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 15768, 5, 2, 1, 2, 1)
)
baRstpCostConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    baRstpCostConfigEntry.setStatus("current")
_BaRstpDynamicCost_Type = TruthValue
_BaRstpDynamicCost_Object = MibTableColumn
baRstpDynamicCost = _BaRstpDynamicCost_Object(
    (1, 3, 6, 1, 4, 1, 15768, 5, 2, 1, 2, 1, 1),
    _BaRstpDynamicCost_Type()
)
baRstpDynamicCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    baRstpDynamicCost.setStatus("current")


class _BaRstpBaseCost_Type(Integer32):
    """Custom type baRstpBaseCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200000000),
    )


_BaRstpBaseCost_Type.__name__ = "Integer32"
_BaRstpBaseCost_Object = MibTableColumn
baRstpBaseCost = _BaRstpBaseCost_Object(
    (1, 3, 6, 1, 4, 1, 15768, 5, 2, 1, 2, 1, 2),
    _BaRstpBaseCost_Type()
)
baRstpBaseCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    baRstpBaseCost.setStatus("current")


class _BaRstpBasePriority_Type(Integer32):
    """Custom type baRstpBasePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BaRstpBasePriority_Type.__name__ = "Integer32"
_BaRstpBasePriority_Object = MibTableColumn
baRstpBasePriority = _BaRstpBasePriority_Object(
    (1, 3, 6, 1, 4, 1, 15768, 5, 2, 1, 2, 1, 3),
    _BaRstpBasePriority_Type()
)
baRstpBasePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    baRstpBasePriority.setStatus("current")
_BelairRstpTraps_ObjectIdentity = ObjectIdentity
belairRstpTraps = _BelairRstpTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 5, 2, 2)
)
_BelairRstpTrapsV2_ObjectIdentity = ObjectIdentity
belairRstpTrapsV2 = _BelairRstpTrapsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 5, 2, 2, 0)
)
_BelairRstpConformance_ObjectIdentity = ObjectIdentity
belairRstpConformance = _BelairRstpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 5, 2, 3)
)

# Managed Objects groups

baRstpObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15768, 5, 2, 3, 1)
)
baRstpObjectGroup.setObjects(
      *(("BELAIR-RSTP", "baRstpPortPriority"),
        ("BELAIR-RSTP", "baRstpPortEnable"),
        ("BELAIR-RSTP", "baRstpPortPathCost"),
        ("BELAIR-RSTP", "baRstpPortDesignatedRoot"),
        ("BELAIR-RSTP", "baRstpPortDesignatedCost"),
        ("BELAIR-RSTP", "baRstpPortDesignatedBridge"),
        ("BELAIR-RSTP", "baRstpPortDesignatedPort"),
        ("BELAIR-RSTP", "baRstpPortForwardTransitions"),
        ("BELAIR-RSTP", "baRstpDynamicCost"),
        ("BELAIR-RSTP", "baRstpBasePriority"),
        ("BELAIR-RSTP", "baRstpBaseCost"),
        ("BELAIR-RSTP", "baRstpPortProtocolMigration"),
        ("BELAIR-RSTP", "baRstpPortAdminEdgePort"),
        ("BELAIR-RSTP", "baRstpPortOperEdgePort"),
        ("BELAIR-RSTP", "baRstpPortAdminPointToPoint"),
        ("BELAIR-RSTP", "baRstpPortOperPointToPoint"),
        ("BELAIR-RSTP", "baRstpPortState"))
)
if mibBuilder.loadTexts:
    baRstpObjectGroup.setStatus("current")


# Notification objects

baRstpTopologyChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 15768, 5, 2, 2, 0, 1)
)
if mibBuilder.loadTexts:
    baRstpTopologyChanged.setStatus(
        "current"
    )


# Notifications groups

baRstpTrapObjectGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 15768, 5, 2, 3, 2)
)
baRstpTrapObjectGroup.setObjects(
    ("BELAIR-RSTP", "baRstpTopologyChanged")
)
if mibBuilder.loadTexts:
    baRstpTrapObjectGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BELAIR-RSTP",
    **{"belairRstpMib": belairRstpMib,
       "belairRstpObjects": belairRstpObjects,
       "baRstpPortIfTable": baRstpPortIfTable,
       "baRstpPortIfEntry": baRstpPortIfEntry,
       "baRstpPortPriority": baRstpPortPriority,
       "baRstpPortState": baRstpPortState,
       "baRstpPortEnable": baRstpPortEnable,
       "baRstpPortPathCost": baRstpPortPathCost,
       "baRstpPortDesignatedRoot": baRstpPortDesignatedRoot,
       "baRstpPortDesignatedCost": baRstpPortDesignatedCost,
       "baRstpPortDesignatedBridge": baRstpPortDesignatedBridge,
       "baRstpPortDesignatedPort": baRstpPortDesignatedPort,
       "baRstpPortForwardTransitions": baRstpPortForwardTransitions,
       "baRstpPortProtocolMigration": baRstpPortProtocolMigration,
       "baRstpPortAdminEdgePort": baRstpPortAdminEdgePort,
       "baRstpPortOperEdgePort": baRstpPortOperEdgePort,
       "baRstpPortAdminPointToPoint": baRstpPortAdminPointToPoint,
       "baRstpPortOperPointToPoint": baRstpPortOperPointToPoint,
       "baRstpCostConfigTable": baRstpCostConfigTable,
       "baRstpCostConfigEntry": baRstpCostConfigEntry,
       "baRstpDynamicCost": baRstpDynamicCost,
       "baRstpBaseCost": baRstpBaseCost,
       "baRstpBasePriority": baRstpBasePriority,
       "belairRstpTraps": belairRstpTraps,
       "belairRstpTrapsV2": belairRstpTrapsV2,
       "baRstpTopologyChanged": baRstpTopologyChanged,
       "belairRstpConformance": belairRstpConformance,
       "baRstpObjectGroup": baRstpObjectGroup,
       "baRstpTrapObjectGroup": baRstpTrapObjectGroup}
)
