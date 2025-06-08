# SNMP MIB module (CISCO-FIREPOWER-AP-NOTIFS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-AP-NOTIFS-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:17:14 2025
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

(cfprApFaultInstAffectedObjectDn,
 cfprApFaultInstAffectedObjectId,
 cfprApFaultInstCause,
 cfprApFaultInstCode,
 cfprApFaultInstCreated,
 cfprApFaultInstDescr,
 cfprApFaultInstId,
 cfprApFaultInstInstanceId,
 cfprApFaultInstLastTransition,
 cfprApFaultInstOccur,
 cfprApFaultInstSeverity,
 cfprApFaultInstType) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-AP-FAULT-MIB",
    "cfprApFaultInstAffectedObjectDn",
    "cfprApFaultInstAffectedObjectId",
    "cfprApFaultInstCause",
    "cfprApFaultInstCode",
    "cfprApFaultInstCreated",
    "cfprApFaultInstDescr",
    "cfprApFaultInstId",
    "cfprApFaultInstInstanceId",
    "cfprApFaultInstLastTransition",
    "cfprApFaultInstOccur",
    "cfprApFaultInstSeverity",
    "cfprApFaultInstType")

(ciscoFirepowerApMIB,) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-AP-MIB",
    "ciscoFirepowerApMIB")

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

ciscoFirepowerApMIBNotifs = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 0)
)
if mibBuilder.loadTexts:
    ciscoFirepowerApMIBNotifs.setRevisions(
        ("2010-01-29 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects

cfprApFaultActiveNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 0, 1)
)
cfprApFaultActiveNotif.setObjects(
      *(("CISCO-FIREPOWER-AP-FAULT-MIB", "cfprApFaultInstInstanceId"),
        ("CISCO-FIREPOWER-AP-FAULT-MIB", "cfprApFaultInstDescr"),
        ("CISCO-FIREPOWER-AP-FAULT-MIB", "cfprApFaultInstAffectedObjectId"),
        ("CISCO-FIREPOWER-AP-FAULT-MIB", "cfprApFaultInstAffectedObjectDn"),
        ("CISCO-FIREPOWER-AP-FAULT-MIB", "cfprApFaultInstCreated"),
        ("CISCO-FIREPOWER-AP-FAULT-MIB", "cfprApFaultInstLastTransition"),
        ("CISCO-FIREPOWER-AP-FAULT-MIB", "cfprApFaultInstCode"),
        ("CISCO-FIREPOWER-AP-FAULT-MIB", "cfprApFaultInstType"),
        ("CISCO-FIREPOWER-AP-FAULT-MIB", "cfprApFaultInstCause"),
        ("CISCO-FIREPOWER-AP-FAULT-MIB", "cfprApFaultInstSeverity"),
        ("CISCO-FIREPOWER-AP-FAULT-MIB", "cfprApFaultInstOccur"),
        ("CISCO-FIREPOWER-AP-FAULT-MIB", "cfprApFaultInstId"))
)
if mibBuilder.loadTexts:
    cfprApFaultActiveNotif.setStatus(
        "current"
    )

cfprApFaultClearNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 0, 2)
)
cfprApFaultClearNotif.setObjects(
      *(("CISCO-FIREPOWER-AP-FAULT-MIB", "cfprApFaultInstInstanceId"),
        ("CISCO-FIREPOWER-AP-FAULT-MIB", "cfprApFaultInstDescr"),
        ("CISCO-FIREPOWER-AP-FAULT-MIB", "cfprApFaultInstAffectedObjectId"),
        ("CISCO-FIREPOWER-AP-FAULT-MIB", "cfprApFaultInstAffectedObjectDn"),
        ("CISCO-FIREPOWER-AP-FAULT-MIB", "cfprApFaultInstCreated"),
        ("CISCO-FIREPOWER-AP-FAULT-MIB", "cfprApFaultInstLastTransition"),
        ("CISCO-FIREPOWER-AP-FAULT-MIB", "cfprApFaultInstCode"),
        ("CISCO-FIREPOWER-AP-FAULT-MIB", "cfprApFaultInstType"),
        ("CISCO-FIREPOWER-AP-FAULT-MIB", "cfprApFaultInstCause"),
        ("CISCO-FIREPOWER-AP-FAULT-MIB", "cfprApFaultInstSeverity"),
        ("CISCO-FIREPOWER-AP-FAULT-MIB", "cfprApFaultInstOccur"),
        ("CISCO-FIREPOWER-AP-FAULT-MIB", "cfprApFaultInstId"))
)
if mibBuilder.loadTexts:
    cfprApFaultClearNotif.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-AP-NOTIFS-MIB",
    **{"ciscoFirepowerApMIBNotifs": ciscoFirepowerApMIBNotifs,
       "cfprApFaultActiveNotif": cfprApFaultActiveNotif,
       "cfprApFaultClearNotif": cfprApFaultClearNotif}
)
