# SNMP MIB module (DIGI-POWER-MANAGEMENT-TRAPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/digi_332/DIGI-POWER-MANAGEMENT-TRAPS-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 11:54:31 2025
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

(sensorActualCurr,
 sensorActualTemp,
 sensorThreshCurr,
 sensorThreshTemp) = mibBuilder.importSymbols(
    "DIGI-POWER-MANAGEMENT-MIB",
    "sensorActualCurr",
    "sensorActualTemp",
    "sensorThreshCurr",
    "sensorThreshTemp")

(digiPowerManagementTraps,) = mibBuilder.importSymbols(
    "DIGI-SMI",
    "digiPowerManagementTraps")

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
 NotificationType,
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
    "NotificationType",
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


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects

currThreshExc = NotificationType(
    (1, 3, 6, 1, 4, 1, 332, 10, 14, 16, 0, 1)
)
currThreshExc.setObjects(
      *(("DIGI-POWER-MANAGEMENT-MIB", "sensorActualCurr"),
        ("DIGI-POWER-MANAGEMENT-MIB", "sensorThreshCurr"))
)
if mibBuilder.loadTexts:
    currThreshExc.setStatus(
        ""
    )

tempThreshExc = NotificationType(
    (1, 3, 6, 1, 4, 1, 332, 10, 14, 16, 0, 2)
)
tempThreshExc.setObjects(
      *(("DIGI-POWER-MANAGEMENT-MIB", "sensorActualTemp"),
        ("DIGI-POWER-MANAGEMENT-MIB", "sensorThreshTemp"))
)
if mibBuilder.loadTexts:
    tempThreshExc.setStatus(
        ""
    )

currThreshExcNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 332, 10, 14, 16, 1)
)
currThreshExcNotification.setObjects(
      *(("DIGI-POWER-MANAGEMENT-MIB", "sensorActualCurr"),
        ("DIGI-POWER-MANAGEMENT-MIB", "sensorThreshCurr"))
)
if mibBuilder.loadTexts:
    currThreshExcNotification.setStatus(
        "current"
    )

tempThreshExcNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 332, 10, 14, 16, 2)
)
tempThreshExcNotification.setObjects(
      *(("DIGI-POWER-MANAGEMENT-MIB", "sensorActualTemp"),
        ("DIGI-POWER-MANAGEMENT-MIB", "sensorThreshTemp"))
)
if mibBuilder.loadTexts:
    tempThreshExcNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DIGI-POWER-MANAGEMENT-TRAPS-MIB",
    **{"DisplayString": DisplayString,
       "currThreshExc": currThreshExc,
       "tempThreshExc": tempThreshExc,
       "currThreshExcNotification": currThreshExcNotification,
       "tempThreshExcNotification": tempThreshExcNotification}
)
