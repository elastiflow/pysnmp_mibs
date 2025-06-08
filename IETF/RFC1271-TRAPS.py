# SNMP MIB module (RFC1271-TRAPS) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/Standards/IETF/RFC1271-TRAPS.mib
# Produced by pysmi-1.5.11 at Wed May 21 14:58:31 2025
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

(alarmFallingThreshold,
 alarmIndex,
 alarmRisingThreshold,
 alarmSampleType,
 alarmValue,
 alarmVariable,
 channelDescription,
 channelIndex,
 channelMatches,
 rmon) = mibBuilder.importSymbols(
    "RFC1271-MIB",
    "alarmFallingThreshold",
    "alarmIndex",
    "alarmRisingThreshold",
    "alarmSampleType",
    "alarmValue",
    "alarmVariable",
    "channelDescription",
    "channelIndex",
    "channelMatches",
    "rmon")

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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects

risingAlarm = NotificationType(
    (1, 3, 6, 1, 2, 1, 16, 0, 1)
)
risingAlarm.setObjects(
      *(("RFC1271-MIB", "alarmIndex"),
        ("RFC1271-MIB", "alarmVariable"),
        ("RFC1271-MIB", "alarmSampleType"),
        ("RFC1271-MIB", "alarmValue"),
        ("RFC1271-MIB", "alarmRisingThreshold"))
)
if mibBuilder.loadTexts:
    risingAlarm.setStatus(
        ""
    )

fallingAlarm = NotificationType(
    (1, 3, 6, 1, 2, 1, 16, 0, 2)
)
fallingAlarm.setObjects(
      *(("RFC1271-MIB", "alarmIndex"),
        ("RFC1271-MIB", "alarmVariable"),
        ("RFC1271-MIB", "alarmSampleType"),
        ("RFC1271-MIB", "alarmValue"),
        ("RFC1271-MIB", "alarmFallingThreshold"))
)
if mibBuilder.loadTexts:
    fallingAlarm.setStatus(
        ""
    )

packetMatch = NotificationType(
    (1, 3, 6, 1, 2, 1, 16, 0, 3)
)
packetMatch.setObjects(
      *(("RFC1271-MIB", "channelIndex"),
        ("RFC1271-MIB", "channelMatches"),
        ("RFC1271-MIB", "channelDescription"))
)
if mibBuilder.loadTexts:
    packetMatch.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RFC1271-TRAPS",
    **{"risingAlarm": risingAlarm,
       "fallingAlarm": fallingAlarm,
       "packetMatch": packetMatch}
)
