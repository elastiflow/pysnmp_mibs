# SNMP MIB module (CISCO-UNIFIED-COMPUTING-CONFORM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-UNIFIED-COMPUTING-CONFORM-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 08:58:45 2025
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

(cucsFaultAffectedObjectDn,
 cucsFaultAffectedObjectId,
 cucsFaultCode,
 cucsFaultCreationTime,
 cucsFaultDescription,
 cucsFaultLastModificationTime,
 cucsFaultOccur,
 cucsFaultProbableCause,
 cucsFaultSeverity,
 cucsFaultType) = mibBuilder.importSymbols(
    "CISCO-UNIFIED-COMPUTING-FAULT-MIB",
    "cucsFaultAffectedObjectDn",
    "cucsFaultAffectedObjectId",
    "cucsFaultCode",
    "cucsFaultCreationTime",
    "cucsFaultDescription",
    "cucsFaultLastModificationTime",
    "cucsFaultOccur",
    "cucsFaultProbableCause",
    "cucsFaultSeverity",
    "cucsFaultType")

(ciscoUnifiedComputingMIB,
 ciscoUnifiedComputingMIBObjects) = mibBuilder.importSymbols(
    "CISCO-UNIFIED-COMPUTING-MIB",
    "ciscoUnifiedComputingMIB",
    "ciscoUnifiedComputingMIBObjects")

(cucsFaultActiveNotif,
 cucsFaultClearNotif) = mibBuilder.importSymbols(
    "CISCO-UNIFIED-COMPUTING-NOTIFS-MIB",
    "cucsFaultActiveNotif",
    "cucsFaultClearNotif")

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

ciscoUnifiedComputingMIBConform = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 2)
)
if mibBuilder.loadTexts:
    ciscoUnifiedComputingMIBConform.setRevisions(
        ("2010-01-29 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CucsFaultMIBConform_ObjectIdentity = ObjectIdentity
cucsFaultMIBConform = _CucsFaultMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 2, 1)
)
_CucsFaultMIBCompliances_ObjectIdentity = ObjectIdentity
cucsFaultMIBCompliances = _CucsFaultMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 2, 1, 1)
)
_CucsFaultMIBGroups_ObjectIdentity = ObjectIdentity
cucsFaultMIBGroups = _CucsFaultMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 2, 1, 2)
)

# Managed Objects groups

cucsFaultsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 2, 1, 2, 1)
)
cucsFaultsGroup.setObjects(
      *(("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultDescription"),
        ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultAffectedObjectId"),
        ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultAffectedObjectDn"),
        ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultCreationTime"),
        ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultLastModificationTime"),
        ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultCode"),
        ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultType"),
        ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultProbableCause"),
        ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultSeverity"),
        ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultOccur"))
)
if mibBuilder.loadTexts:
    cucsFaultsGroup.setStatus("current")


# Notification objects


# Notifications groups

cucsFaultsNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 2, 1, 2, 2)
)
cucsFaultsNotifGroup.setObjects(
      *(("CISCO-UNIFIED-COMPUTING-NOTIFS-MIB", "cucsFaultActiveNotif"),
        ("CISCO-UNIFIED-COMPUTING-NOTIFS-MIB", "cucsFaultClearNotif"))
)
if mibBuilder.loadTexts:
    cucsFaultsNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cucsFaultMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 2, 1, 1, 1)
)
cucsFaultMIBCompliance.setObjects(
      *(("CISCO-UNIFIED-COMPUTING-CONFORM-MIB", "cucsFaultsNotifGroup"),
        ("CISCO-UNIFIED-COMPUTING-CONFORM-MIB", "cucsFaultsGroup"))
)
if mibBuilder.loadTexts:
    cucsFaultMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-UNIFIED-COMPUTING-CONFORM-MIB",
    **{"ciscoUnifiedComputingMIBConform": ciscoUnifiedComputingMIBConform,
       "cucsFaultMIBConform": cucsFaultMIBConform,
       "cucsFaultMIBCompliances": cucsFaultMIBCompliances,
       "cucsFaultMIBCompliance": cucsFaultMIBCompliance,
       "cucsFaultMIBGroups": cucsFaultMIBGroups,
       "cucsFaultsGroup": cucsFaultsGroup,
       "cucsFaultsNotifGroup": cucsFaultsNotifGroup}
)
