# SNMP MIB module (IEEE8021-MVRPX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/IEEE/IEEE8021-MVRPX-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 18:12:28 2025
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

(ieee8021BridgeBasePortEntry,) = mibBuilder.importSymbols(
    "IEEE8021-BRIDGE-MIB",
    "ieee8021BridgeBasePortEntry")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(systemGroup,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "systemGroup")

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

ieee8021MvrpxMib = ModuleIdentity(
    (1, 3, 111, 2, 802, 1, 1, 22)
)
if mibBuilder.loadTexts:
    ieee8021MvrpxMib.setRevisions(
        ("2021-03-05 00:00",
         "2018-07-01 00:00",
         "2014-12-15 00:00",
         "2011-04-05 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ieee8021MvrpxMIBObjects_ObjectIdentity = ObjectIdentity
ieee8021MvrpxMIBObjects = _Ieee8021MvrpxMIBObjects_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 22, 1)
)
_Ieee8021MvrpxPortTable_Object = MibTable
ieee8021MvrpxPortTable = _Ieee8021MvrpxPortTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 22, 1, 1)
)
if mibBuilder.loadTexts:
    ieee8021MvrpxPortTable.setStatus("current")
_Ieee8021MvrpxPortEntry_Object = MibTableRow
ieee8021MvrpxPortEntry = _Ieee8021MvrpxPortEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 22, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ieee8021MvrpxPortEntry.setStatus("current")


class _Ieee8021MvrpxPortNewOnly_Type(TruthValue):
    """Custom type ieee8021MvrpxPortNewOnly based on TruthValue"""
    defaultValue = 2


_Ieee8021MvrpxPortNewOnly_Type.__name__ = "TruthValue"
_Ieee8021MvrpxPortNewOnly_Object = MibTableColumn
ieee8021MvrpxPortNewOnly = _Ieee8021MvrpxPortNewOnly_Object(
    (1, 3, 111, 2, 802, 1, 1, 22, 1, 1, 1, 1),
    _Ieee8021MvrpxPortNewOnly_Type()
)
ieee8021MvrpxPortNewOnly.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021MvrpxPortNewOnly.setStatus("current")


class _Ieee8021MvrpxPortMvrpNewPropagated_Type(TruthValue):
    """Custom type ieee8021MvrpxPortMvrpNewPropagated based on TruthValue"""
    defaultValue = 2


_Ieee8021MvrpxPortMvrpNewPropagated_Type.__name__ = "TruthValue"
_Ieee8021MvrpxPortMvrpNewPropagated_Object = MibTableColumn
ieee8021MvrpxPortMvrpNewPropagated = _Ieee8021MvrpxPortMvrpNewPropagated_Object(
    (1, 3, 111, 2, 802, 1, 1, 22, 1, 1, 1, 2),
    _Ieee8021MvrpxPortMvrpNewPropagated_Type()
)
ieee8021MvrpxPortMvrpNewPropagated.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021MvrpxPortMvrpNewPropagated.setStatus("current")


class _Ieee8021MvrpxPortXmitZero_Type(TruthValue):
    """Custom type ieee8021MvrpxPortXmitZero based on TruthValue"""
    defaultValue = 2


_Ieee8021MvrpxPortXmitZero_Type.__name__ = "TruthValue"
_Ieee8021MvrpxPortXmitZero_Object = MibTableColumn
ieee8021MvrpxPortXmitZero = _Ieee8021MvrpxPortXmitZero_Object(
    (1, 3, 111, 2, 802, 1, 1, 22, 1, 1, 1, 3),
    _Ieee8021MvrpxPortXmitZero_Type()
)
ieee8021MvrpxPortXmitZero.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021MvrpxPortXmitZero.setStatus("current")
_Ieee8021MvrpxConformance_ObjectIdentity = ObjectIdentity
ieee8021MvrpxConformance = _Ieee8021MvrpxConformance_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 22, 2)
)
_Ieee8021MvrpxCompliances_ObjectIdentity = ObjectIdentity
ieee8021MvrpxCompliances = _Ieee8021MvrpxCompliances_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 22, 2, 1)
)
_Ieee8021MvrpxGroups_ObjectIdentity = ObjectIdentity
ieee8021MvrpxGroups = _Ieee8021MvrpxGroups_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 22, 2, 2)
)
ieee8021BridgeBasePortEntry.registerAugmentions(
    ("IEEE8021-MVRPX-MIB",
     "ieee8021MvrpxPortEntry")
)
ieee8021MvrpxPortEntry.setIndexNames(*ieee8021BridgeBasePortEntry.getIndexNames())

# Managed Objects groups

ieee8021MvrpxReqdGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 22, 2, 2, 1)
)
ieee8021MvrpxReqdGroup.setObjects(
      *(("IEEE8021-MVRPX-MIB", "ieee8021MvrpxPortNewOnly"),
        ("IEEE8021-MVRPX-MIB", "ieee8021MvrpxPortMvrpNewPropagated"),
        ("IEEE8021-MVRPX-MIB", "ieee8021MvrpxPortXmitZero"))
)
if mibBuilder.loadTexts:
    ieee8021MvrpxReqdGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ieee8021MvrpxCompliance = ModuleCompliance(
    (1, 3, 111, 2, 802, 1, 1, 22, 2, 1, 1)
)
ieee8021MvrpxCompliance.setObjects(
      *(("SNMPv2-MIB", "systemGroup"),
        ("IEEE8021-MVRPX-MIB", "ieee8021MvrpxReqdGroup"))
)
if mibBuilder.loadTexts:
    ieee8021MvrpxCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IEEE8021-MVRPX-MIB",
    **{"ieee8021MvrpxMib": ieee8021MvrpxMib,
       "ieee8021MvrpxMIBObjects": ieee8021MvrpxMIBObjects,
       "ieee8021MvrpxPortTable": ieee8021MvrpxPortTable,
       "ieee8021MvrpxPortEntry": ieee8021MvrpxPortEntry,
       "ieee8021MvrpxPortNewOnly": ieee8021MvrpxPortNewOnly,
       "ieee8021MvrpxPortMvrpNewPropagated": ieee8021MvrpxPortMvrpNewPropagated,
       "ieee8021MvrpxPortXmitZero": ieee8021MvrpxPortXmitZero,
       "ieee8021MvrpxConformance": ieee8021MvrpxConformance,
       "ieee8021MvrpxCompliances": ieee8021MvrpxCompliances,
       "ieee8021MvrpxCompliance": ieee8021MvrpxCompliance,
       "ieee8021MvrpxGroups": ieee8021MvrpxGroups,
       "ieee8021MvrpxReqdGroup": ieee8021MvrpxReqdGroup}
)
