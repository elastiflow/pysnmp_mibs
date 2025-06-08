# SNMP MIB module (RUIJIE-RLDP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-RLDP-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 11:02:06 2025
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

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

(ruijieMgmt,) = mibBuilder.importSymbols(
    "RUIJIE-SMI",
    "ruijieMgmt")

(IfIndex,) = mibBuilder.importSymbols(
    "RUIJIE-TC",
    "IfIndex")

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

ruijieRldpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 162)
)
if mibBuilder.loadTexts:
    ruijieRldpMIB.setRevisions(
        ("2019-09-17 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieRldpMIBObjects_ObjectIdentity = ObjectIdentity
ruijieRldpMIBObjects = _RuijieRldpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 162, 1)
)
_RuijieRldpLoopTable_Object = MibTable
ruijieRldpLoopTable = _RuijieRldpLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 162, 1, 1)
)
if mibBuilder.loadTexts:
    ruijieRldpLoopTable.setStatus("current")
_RuijieRldpLoopEntry_Object = MibTableRow
ruijieRldpLoopEntry = _RuijieRldpLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 162, 1, 1, 1)
)
ruijieRldpLoopEntry.setIndexNames(
    (0, "RUIJIE-RLDP-MIB", "ruijieRldpLoopIfIndex"),
)
if mibBuilder.loadTexts:
    ruijieRldpLoopEntry.setStatus("current")
_RuijieRldpLoopIfIndex_Type = IfIndex
_RuijieRldpLoopIfIndex_Object = MibTableColumn
ruijieRldpLoopIfIndex = _RuijieRldpLoopIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 162, 1, 1, 1, 1),
    _RuijieRldpLoopIfIndex_Type()
)
ruijieRldpLoopIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRldpLoopIfIndex.setStatus("current")
_RuijieRldpLoopVlan_Type = Integer32
_RuijieRldpLoopVlan_Object = MibTableColumn
ruijieRldpLoopVlan = _RuijieRldpLoopVlan_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 162, 1, 1, 1, 2),
    _RuijieRldpLoopVlan_Type()
)
ruijieRldpLoopVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRldpLoopVlan.setStatus("current")


class _RuijieRldpLoopState_Type(Integer32):
    """Custom type ruijieRldpLoopState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("error", 2))
    )


_RuijieRldpLoopState_Type.__name__ = "Integer32"
_RuijieRldpLoopState_Object = MibTableColumn
ruijieRldpLoopState = _RuijieRldpLoopState_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 162, 1, 1, 1, 3),
    _RuijieRldpLoopState_Type()
)
ruijieRldpLoopState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRldpLoopState.setStatus("current")


class _RuijieRldpLoopAction_Type(Integer32):
    """Custom type ruijieRldpLoopAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("warning", 1),
          ("block", 2),
          ("shutdown-port", 3),
          ("shutdown-svi", 4),
          ("isolate-vlan", 5))
    )


_RuijieRldpLoopAction_Type.__name__ = "Integer32"
_RuijieRldpLoopAction_Object = MibTableColumn
ruijieRldpLoopAction = _RuijieRldpLoopAction_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 162, 1, 1, 1, 4),
    _RuijieRldpLoopAction_Type()
)
ruijieRldpLoopAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRldpLoopAction.setStatus("current")
_RuijieRldpVlanLoopTable_Object = MibTable
ruijieRldpVlanLoopTable = _RuijieRldpVlanLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 162, 1, 2)
)
if mibBuilder.loadTexts:
    ruijieRldpVlanLoopTable.setStatus("current")
_RuijieRldpVlanLoopEntry_Object = MibTableRow
ruijieRldpVlanLoopEntry = _RuijieRldpVlanLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 162, 1, 2, 1)
)
ruijieRldpVlanLoopEntry.setIndexNames(
    (0, "RUIJIE-RLDP-MIB", "ruijieRldpVlanLoopIfIndex"),
    (0, "RUIJIE-RLDP-MIB", "ruijieRldpVlanLoopVlan"),
)
if mibBuilder.loadTexts:
    ruijieRldpVlanLoopEntry.setStatus("current")
_RuijieRldpVlanLoopIfIndex_Type = IfIndex
_RuijieRldpVlanLoopIfIndex_Object = MibTableColumn
ruijieRldpVlanLoopIfIndex = _RuijieRldpVlanLoopIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 162, 1, 2, 1, 1),
    _RuijieRldpVlanLoopIfIndex_Type()
)
ruijieRldpVlanLoopIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRldpVlanLoopIfIndex.setStatus("current")
_RuijieRldpVlanLoopVlan_Type = VlanId
_RuijieRldpVlanLoopVlan_Object = MibTableColumn
ruijieRldpVlanLoopVlan = _RuijieRldpVlanLoopVlan_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 162, 1, 2, 1, 2),
    _RuijieRldpVlanLoopVlan_Type()
)
ruijieRldpVlanLoopVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRldpVlanLoopVlan.setStatus("current")


class _RuijieRldpVlanLoopState_Type(Integer32):
    """Custom type ruijieRldpVlanLoopState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("error", 2))
    )


_RuijieRldpVlanLoopState_Type.__name__ = "Integer32"
_RuijieRldpVlanLoopState_Object = MibTableColumn
ruijieRldpVlanLoopState = _RuijieRldpVlanLoopState_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 162, 1, 2, 1, 3),
    _RuijieRldpVlanLoopState_Type()
)
ruijieRldpVlanLoopState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRldpVlanLoopState.setStatus("current")


class _RuijieRldpVlanLoopAction_Type(Integer32):
    """Custom type ruijieRldpVlanLoopAction based on Integer32"""
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
        *(("warning", 1),
          ("block", 2),
          ("shutdown-port", 3),
          ("shutdown-svi", 4),
          ("isolate-vlan", 5))
    )


_RuijieRldpVlanLoopAction_Type.__name__ = "Integer32"
_RuijieRldpVlanLoopAction_Object = MibTableColumn
ruijieRldpVlanLoopAction = _RuijieRldpVlanLoopAction_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 162, 1, 2, 1, 4),
    _RuijieRldpVlanLoopAction_Type()
)
ruijieRldpVlanLoopAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRldpVlanLoopAction.setStatus("current")
_RuijieRldpTraps_ObjectIdentity = ObjectIdentity
ruijieRldpTraps = _RuijieRldpTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 162, 2)
)
_RuijieRldpMIBConformance_ObjectIdentity = ObjectIdentity
ruijieRldpMIBConformance = _RuijieRldpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 162, 3)
)
_RuijieRldpMIBCompliances_ObjectIdentity = ObjectIdentity
ruijieRldpMIBCompliances = _RuijieRldpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 162, 3, 1)
)
_RuijieRldpMIBGroups_ObjectIdentity = ObjectIdentity
ruijieRldpMIBGroups = _RuijieRldpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 162, 3, 2)
)

# Managed Objects groups

ruijieRldpLoopMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 162, 3, 2, 1)
)
ruijieRldpLoopMIBGroup.setObjects(
      *(("RUIJIE-RLDP-MIB", "ruijieRldpLoopIfIndex"),
        ("RUIJIE-RLDP-MIB", "ruijieRldpLoopVlan"),
        ("RUIJIE-RLDP-MIB", "ruijieRldpLoopState"),
        ("RUIJIE-RLDP-MIB", "ruijieRldpLoopAction"))
)
if mibBuilder.loadTexts:
    ruijieRldpLoopMIBGroup.setStatus("current")

ruijieRldpVlanLoopMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 162, 3, 2, 2)
)
ruijieRldpVlanLoopMIBGroup.setObjects(
      *(("RUIJIE-RLDP-MIB", "ruijieRldpVlanLoopIfIndex"),
        ("RUIJIE-RLDP-MIB", "ruijieRldpVlanLoopVlan"),
        ("RUIJIE-RLDP-MIB", "ruijieRldpVlanLoopState"),
        ("RUIJIE-RLDP-MIB", "ruijieRldpVlanLoopAction"))
)
if mibBuilder.loadTexts:
    ruijieRldpVlanLoopMIBGroup.setStatus("current")


# Notification objects

rldpLoopStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 162, 2, 1)
)
rldpLoopStateChange.setObjects(
      *(("RUIJIE-RLDP-MIB", "ruijieRldpLoopIfIndex"),
        ("RUIJIE-RLDP-MIB", "ruijieRldpLoopVlan"),
        ("RUIJIE-RLDP-MIB", "ruijieRldpLoopState"),
        ("RUIJIE-RLDP-MIB", "ruijieRldpLoopAction"))
)
if mibBuilder.loadTexts:
    rldpLoopStateChange.setStatus(
        "current"
    )

rldpVlanLoopStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 162, 2, 2)
)
rldpVlanLoopStateChange.setObjects(
      *(("RUIJIE-RLDP-MIB", "ruijieRldpVlanLoopIfIndex"),
        ("RUIJIE-RLDP-MIB", "ruijieRldpVlanLoopVlan"),
        ("RUIJIE-RLDP-MIB", "ruijieRldpVlanLoopState"),
        ("RUIJIE-RLDP-MIB", "ruijieRldpVlanLoopAction"))
)
if mibBuilder.loadTexts:
    rldpVlanLoopStateChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

ruijieRldpMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 162, 3, 1, 1)
)
ruijieRldpMIBCompliance.setObjects(
      *(("RUIJIE-RLDP-MIB", "ruijieRldpLoopMIBGroup"),
        ("RUIJIE-RLDP-MIB", "ruijieRldpVlanLoopMIBGroup"))
)
if mibBuilder.loadTexts:
    ruijieRldpMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-RLDP-MIB",
    **{"ruijieRldpMIB": ruijieRldpMIB,
       "ruijieRldpMIBObjects": ruijieRldpMIBObjects,
       "ruijieRldpLoopTable": ruijieRldpLoopTable,
       "ruijieRldpLoopEntry": ruijieRldpLoopEntry,
       "ruijieRldpLoopIfIndex": ruijieRldpLoopIfIndex,
       "ruijieRldpLoopVlan": ruijieRldpLoopVlan,
       "ruijieRldpLoopState": ruijieRldpLoopState,
       "ruijieRldpLoopAction": ruijieRldpLoopAction,
       "ruijieRldpVlanLoopTable": ruijieRldpVlanLoopTable,
       "ruijieRldpVlanLoopEntry": ruijieRldpVlanLoopEntry,
       "ruijieRldpVlanLoopIfIndex": ruijieRldpVlanLoopIfIndex,
       "ruijieRldpVlanLoopVlan": ruijieRldpVlanLoopVlan,
       "ruijieRldpVlanLoopState": ruijieRldpVlanLoopState,
       "ruijieRldpVlanLoopAction": ruijieRldpVlanLoopAction,
       "ruijieRldpTraps": ruijieRldpTraps,
       "rldpLoopStateChange": rldpLoopStateChange,
       "rldpVlanLoopStateChange": rldpVlanLoopStateChange,
       "ruijieRldpMIBConformance": ruijieRldpMIBConformance,
       "ruijieRldpMIBCompliances": ruijieRldpMIBCompliances,
       "ruijieRldpMIBCompliance": ruijieRldpMIBCompliance,
       "ruijieRldpMIBGroups": ruijieRldpMIBGroups,
       "ruijieRldpLoopMIBGroup": ruijieRldpLoopMIBGroup,
       "ruijieRldpVlanLoopMIBGroup": ruijieRldpVlanLoopMIBGroup}
)
