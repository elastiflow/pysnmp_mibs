# SNMP MIB module (DIGI-POWER-TRAPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/digi_332/DIGI-POWER-TRAPS-MIB.mib
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

(digiPowerTraps,) = mibBuilder.importSymbols(
    "DIGI-SMI",
    "digiPowerTraps")

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

_PowerIndex_Type = Integer32
_PowerIndex_Object = MibScalar
powerIndex = _PowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 14, 23, 11),
    _PowerIndex_Type()
)
powerIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    powerIndex.setStatus("mandatory")
_PowerDescription_Type = DisplayString
_PowerDescription_Object = MibScalar
powerDescription = _PowerDescription_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 14, 23, 12),
    _PowerDescription_Type()
)
powerDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    powerDescription.setStatus("mandatory")

# Managed Objects groups


# Notification objects

powerOnAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 332, 10, 14, 23, 0, 1)
)
powerOnAlarm.setObjects(
      *(("DIGI-POWER-TRAPS-MIB", "powerIndex"),
        ("DIGI-POWER-TRAPS-MIB", "powerDescription"))
)
if mibBuilder.loadTexts:
    powerOnAlarm.setStatus(
        ""
    )

powerOffAlart = NotificationType(
    (1, 3, 6, 1, 4, 1, 332, 10, 14, 23, 0, 2)
)
powerOffAlart.setObjects(
      *(("DIGI-POWER-TRAPS-MIB", "powerIndex"),
        ("DIGI-POWER-TRAPS-MIB", "powerDescription"))
)
if mibBuilder.loadTexts:
    powerOffAlart.setStatus(
        ""
    )

powerOnAlarmNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 332, 10, 14, 23, 1)
)
powerOnAlarmNotification.setObjects(
      *(("DIGI-POWER-TRAPS-MIB", "powerIndex"),
        ("DIGI-POWER-TRAPS-MIB", "powerDescription"))
)
if mibBuilder.loadTexts:
    powerOnAlarmNotification.setStatus(
        "current"
    )

powerOffAlartNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 332, 10, 14, 23, 2)
)
powerOffAlartNotification.setObjects(
      *(("DIGI-POWER-TRAPS-MIB", "powerIndex"),
        ("DIGI-POWER-TRAPS-MIB", "powerDescription"))
)
if mibBuilder.loadTexts:
    powerOffAlartNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DIGI-POWER-TRAPS-MIB",
    **{"DisplayString": DisplayString,
       "powerOnAlarm": powerOnAlarm,
       "powerOffAlart": powerOffAlart,
       "powerOnAlarmNotification": powerOnAlarmNotification,
       "powerOffAlartNotification": powerOffAlartNotification,
       "powerIndex": powerIndex,
       "powerDescription": powerDescription}
)
