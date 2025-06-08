# SNMP MIB module (CISCO-FIREPOWER-NOTIFS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-NOTIFS-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:24:12 2025
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

(cfprFaultInstAffectedObjectDn,
 cfprFaultInstAffectedObjectId,
 cfprFaultInstCause,
 cfprFaultInstCode,
 cfprFaultInstCreated,
 cfprFaultInstDescr,
 cfprFaultInstId,
 cfprFaultInstInstanceId,
 cfprFaultInstLastTransition,
 cfprFaultInstOccur,
 cfprFaultInstSeverity,
 cfprFaultInstType) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-FAULT-MIB",
    "cfprFaultInstAffectedObjectDn",
    "cfprFaultInstAffectedObjectId",
    "cfprFaultInstCause",
    "cfprFaultInstCode",
    "cfprFaultInstCreated",
    "cfprFaultInstDescr",
    "cfprFaultInstId",
    "cfprFaultInstInstanceId",
    "cfprFaultInstLastTransition",
    "cfprFaultInstOccur",
    "cfprFaultInstSeverity",
    "cfprFaultInstType")

(ciscoFirepowerMIB,) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-MIB",
    "ciscoFirepowerMIB")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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

ciscoFirepowerMIBNotifs = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 0)
)
if mibBuilder.loadTexts:
    ciscoFirepowerMIBNotifs.setRevisions(
        ("2010-01-29 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects

cfprFaultActiveNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 0, 1)
)
cfprFaultActiveNotif.setObjects(
      *(("CISCO-FIREPOWER-FAULT-MIB", "cfprFaultInstInstanceId"),
        ("CISCO-FIREPOWER-FAULT-MIB", "cfprFaultInstDescr"),
        ("CISCO-FIREPOWER-FAULT-MIB", "cfprFaultInstAffectedObjectId"),
        ("CISCO-FIREPOWER-FAULT-MIB", "cfprFaultInstAffectedObjectDn"),
        ("CISCO-FIREPOWER-FAULT-MIB", "cfprFaultInstCreated"),
        ("CISCO-FIREPOWER-FAULT-MIB", "cfprFaultInstLastTransition"),
        ("CISCO-FIREPOWER-FAULT-MIB", "cfprFaultInstCode"),
        ("CISCO-FIREPOWER-FAULT-MIB", "cfprFaultInstType"),
        ("CISCO-FIREPOWER-FAULT-MIB", "cfprFaultInstCause"),
        ("CISCO-FIREPOWER-FAULT-MIB", "cfprFaultInstSeverity"),
        ("CISCO-FIREPOWER-FAULT-MIB", "cfprFaultInstOccur"),
        ("CISCO-FIREPOWER-FAULT-MIB", "cfprFaultInstId"))
)
if mibBuilder.loadTexts:
    cfprFaultActiveNotif.setStatus(
        "current"
    )

cfprFaultClearNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 0, 2)
)
cfprFaultClearNotif.setObjects(
      *(("CISCO-FIREPOWER-FAULT-MIB", "cfprFaultInstInstanceId"),
        ("CISCO-FIREPOWER-FAULT-MIB", "cfprFaultInstDescr"),
        ("CISCO-FIREPOWER-FAULT-MIB", "cfprFaultInstAffectedObjectId"),
        ("CISCO-FIREPOWER-FAULT-MIB", "cfprFaultInstAffectedObjectDn"),
        ("CISCO-FIREPOWER-FAULT-MIB", "cfprFaultInstCreated"),
        ("CISCO-FIREPOWER-FAULT-MIB", "cfprFaultInstLastTransition"),
        ("CISCO-FIREPOWER-FAULT-MIB", "cfprFaultInstCode"),
        ("CISCO-FIREPOWER-FAULT-MIB", "cfprFaultInstType"),
        ("CISCO-FIREPOWER-FAULT-MIB", "cfprFaultInstCause"),
        ("CISCO-FIREPOWER-FAULT-MIB", "cfprFaultInstSeverity"),
        ("CISCO-FIREPOWER-FAULT-MIB", "cfprFaultInstOccur"),
        ("CISCO-FIREPOWER-FAULT-MIB", "cfprFaultInstId"))
)
if mibBuilder.loadTexts:
    cfprFaultClearNotif.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-NOTIFS-MIB",
    **{"ciscoFirepowerMIBNotifs": ciscoFirepowerMIBNotifs,
       "cfprFaultActiveNotif": cfprFaultActiveNotif,
       "cfprFaultClearNotif": cfprFaultClearNotif}
)
