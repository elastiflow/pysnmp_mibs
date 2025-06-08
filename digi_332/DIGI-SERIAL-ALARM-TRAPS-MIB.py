# SNMP MIB module (DIGI-SERIAL-ALARM-TRAPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/digi_332/DIGI-SERIAL-ALARM-TRAPS-MIB.mib
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

(digiSerialAlarmTraps,) = mibBuilder.importSymbols(
    "DIGI-SMI",
    "digiSerialAlarmTraps")

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

_SerialAlarmSubject_Type = DisplayString
_SerialAlarmSubject_Object = MibScalar
serialAlarmSubject = _SerialAlarmSubject_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 14, 19, 11),
    _SerialAlarmSubject_Type()
)
serialAlarmSubject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialAlarmSubject.setStatus("mandatory")

# Managed Objects groups


# Notification objects

serialAlarmDataPattern = NotificationType(
    (1, 3, 6, 1, 4, 1, 332, 10, 14, 19, 0, 1)
)
serialAlarmDataPattern.setObjects(
    ("DIGI-SERIAL-ALARM-TRAPS-MIB", "serialAlarmSubject")
)
if mibBuilder.loadTexts:
    serialAlarmDataPattern.setStatus(
        ""
    )

serialAlarmTransition = NotificationType(
    (1, 3, 6, 1, 4, 1, 332, 10, 14, 19, 0, 2)
)
serialAlarmTransition.setObjects(
    ("DIGI-SERIAL-ALARM-TRAPS-MIB", "serialAlarmSubject")
)
if mibBuilder.loadTexts:
    serialAlarmTransition.setStatus(
        ""
    )

serialAlarmReminder = NotificationType(
    (1, 3, 6, 1, 4, 1, 332, 10, 14, 19, 0, 3)
)
serialAlarmReminder.setObjects(
    ("DIGI-SERIAL-ALARM-TRAPS-MIB", "serialAlarmSubject")
)
if mibBuilder.loadTexts:
    serialAlarmReminder.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DIGI-SERIAL-ALARM-TRAPS-MIB",
    **{"DisplayString": DisplayString,
       "serialAlarmDataPattern": serialAlarmDataPattern,
       "serialAlarmTransition": serialAlarmTransition,
       "serialAlarmReminder": serialAlarmReminder,
       "serialAlarmSubject": serialAlarmSubject}
)
