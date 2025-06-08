# SNMP MIB module (CISCO-NETINT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-NETINT-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 00:13:23 2025
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

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

ciscoNetintMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 490)
)
if mibBuilder.loadTexts:
    ciscoNetintMIB.setRevisions(
        ("2005-09-26 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoNetintMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoNetintMIBNotifs = _CiscoNetintMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 490, 0)
)
_CiscoNetintMIBObjects_ObjectIdentity = ObjectIdentity
ciscoNetintMIBObjects = _CiscoNetintMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 490, 1)
)
_CniThrottle_ObjectIdentity = ObjectIdentity
cniThrottle = _CniThrottle_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 490, 1, 1)
)
_CniThrottleTable_Object = MibTable
cniThrottleTable = _CniThrottleTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 490, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cniThrottleTable.setStatus("current")
_CniThrottleEntry_Object = MibTableRow
cniThrottleEntry = _CniThrottleEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 490, 1, 1, 1, 1)
)
cniThrottleEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    cniThrottleEntry.setStatus("current")
_CniThrottleCount_Type = Counter32
_CniThrottleCount_Object = MibTableColumn
cniThrottleCount = _CniThrottleCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 490, 1, 1, 1, 1, 1),
    _CniThrottleCount_Type()
)
cniThrottleCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cniThrottleCount.setStatus("current")
_CiscoNetintMIBConformance_ObjectIdentity = ObjectIdentity
ciscoNetintMIBConformance = _CiscoNetintMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 490, 2)
)
_CiscoNetintMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoNetintMIBCompliances = _CiscoNetintMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 490, 2, 1)
)
_CiscoNetintMIBGroups_ObjectIdentity = ObjectIdentity
ciscoNetintMIBGroups = _CiscoNetintMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 490, 2, 2)
)

# Managed Objects groups

ciscoThrottleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 490, 2, 2, 1)
)
ciscoThrottleGroup.setObjects(
    ("CISCO-NETINT-MIB", "cniThrottleCount")
)
if mibBuilder.loadTexts:
    ciscoThrottleGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoNetintMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 490, 2, 1, 1)
)
ciscoNetintMIBCompliance.setObjects(
    ("CISCO-NETINT-MIB", "ciscoThrottleGroup")
)
if mibBuilder.loadTexts:
    ciscoNetintMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-NETINT-MIB",
    **{"ciscoNetintMIB": ciscoNetintMIB,
       "ciscoNetintMIBNotifs": ciscoNetintMIBNotifs,
       "ciscoNetintMIBObjects": ciscoNetintMIBObjects,
       "cniThrottle": cniThrottle,
       "cniThrottleTable": cniThrottleTable,
       "cniThrottleEntry": cniThrottleEntry,
       "cniThrottleCount": cniThrottleCount,
       "ciscoNetintMIBConformance": ciscoNetintMIBConformance,
       "ciscoNetintMIBCompliances": ciscoNetintMIBCompliances,
       "ciscoNetintMIBCompliance": ciscoNetintMIBCompliance,
       "ciscoNetintMIBGroups": ciscoNetintMIBGroups,
       "ciscoThrottleGroup": ciscoThrottleGroup}
)
