# SNMP MIB module (IF-CAP-STACK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/Standards/IETF/IF-CAP-STACK-MIB.mib
# Produced by pysmi-1.5.11 at Wed May 21 14:36:15 2025
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

(ifInvStackGroup,) = mibBuilder.importSymbols(
    "IF-INVERTED-STACK-MIB",
    "ifInvStackGroup")

(ifStackGroup2,
 ifStackHigherLayer,
 ifStackLowerLayer) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifStackGroup2",
    "ifStackHigherLayer",
    "ifStackLowerLayer")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

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

ifCapStackMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 166)
)
if mibBuilder.loadTexts:
    ifCapStackMIB.setRevisions(
        ("2007-11-07 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IfCapStackObjects_ObjectIdentity = ObjectIdentity
ifCapStackObjects = _IfCapStackObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 166, 1)
)
_IfCapStackTable_Object = MibTable
ifCapStackTable = _IfCapStackTable_Object(
    (1, 3, 6, 1, 2, 1, 166, 1, 1)
)
if mibBuilder.loadTexts:
    ifCapStackTable.setStatus("current")
_IfCapStackEntry_Object = MibTableRow
ifCapStackEntry = _IfCapStackEntry_Object(
    (1, 3, 6, 1, 2, 1, 166, 1, 1, 1)
)
ifCapStackEntry.setIndexNames(
    (0, "IF-MIB", "ifStackHigherLayer"),
    (0, "IF-MIB", "ifStackLowerLayer"),
)
if mibBuilder.loadTexts:
    ifCapStackEntry.setStatus("current")
_IfCapStackStatus_Type = TruthValue
_IfCapStackStatus_Object = MibTableColumn
ifCapStackStatus = _IfCapStackStatus_Object(
    (1, 3, 6, 1, 2, 1, 166, 1, 1, 1, 1),
    _IfCapStackStatus_Type()
)
ifCapStackStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifCapStackStatus.setStatus("current")
_IfInvCapStackTable_Object = MibTable
ifInvCapStackTable = _IfInvCapStackTable_Object(
    (1, 3, 6, 1, 2, 1, 166, 1, 2)
)
if mibBuilder.loadTexts:
    ifInvCapStackTable.setStatus("current")
_IfInvCapStackEntry_Object = MibTableRow
ifInvCapStackEntry = _IfInvCapStackEntry_Object(
    (1, 3, 6, 1, 2, 1, 166, 1, 2, 1)
)
ifInvCapStackEntry.setIndexNames(
    (0, "IF-MIB", "ifStackLowerLayer"),
    (0, "IF-MIB", "ifStackHigherLayer"),
)
if mibBuilder.loadTexts:
    ifInvCapStackEntry.setStatus("current")
_IfInvCapStackStatus_Type = TruthValue
_IfInvCapStackStatus_Object = MibTableColumn
ifInvCapStackStatus = _IfInvCapStackStatus_Object(
    (1, 3, 6, 1, 2, 1, 166, 1, 2, 1, 1),
    _IfInvCapStackStatus_Type()
)
ifInvCapStackStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifInvCapStackStatus.setStatus("current")
_IfCapStackConformance_ObjectIdentity = ObjectIdentity
ifCapStackConformance = _IfCapStackConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 166, 2)
)
_IfCapStackGroups_ObjectIdentity = ObjectIdentity
ifCapStackGroups = _IfCapStackGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 166, 2, 1)
)
_IfCapStackCompliances_ObjectIdentity = ObjectIdentity
ifCapStackCompliances = _IfCapStackCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 166, 2, 2)
)

# Managed Objects groups

ifCapStackGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 166, 2, 1, 1)
)
ifCapStackGroup.setObjects(
      *(("IF-CAP-STACK-MIB", "ifCapStackStatus"),
        ("IF-CAP-STACK-MIB", "ifInvCapStackStatus"))
)
if mibBuilder.loadTexts:
    ifCapStackGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ifCapStackCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 166, 2, 2, 1)
)
ifCapStackCompliance.setObjects(
      *(("IF-CAP-STACK-MIB", "ifCapStackGroup"),
        ("IF-MIB", "ifStackGroup2"),
        ("IF-INVERTED-STACK-MIB", "ifInvStackGroup"))
)
if mibBuilder.loadTexts:
    ifCapStackCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IF-CAP-STACK-MIB",
    **{"ifCapStackMIB": ifCapStackMIB,
       "ifCapStackObjects": ifCapStackObjects,
       "ifCapStackTable": ifCapStackTable,
       "ifCapStackEntry": ifCapStackEntry,
       "ifCapStackStatus": ifCapStackStatus,
       "ifInvCapStackTable": ifInvCapStackTable,
       "ifInvCapStackEntry": ifInvCapStackEntry,
       "ifInvCapStackStatus": ifInvCapStackStatus,
       "ifCapStackConformance": ifCapStackConformance,
       "ifCapStackGroups": ifCapStackGroups,
       "ifCapStackGroup": ifCapStackGroup,
       "ifCapStackCompliances": ifCapStackCompliances,
       "ifCapStackCompliance": ifCapStackCompliance}
)
