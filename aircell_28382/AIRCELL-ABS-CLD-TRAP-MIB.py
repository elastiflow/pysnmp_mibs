# SNMP MIB module (AIRCELL-ABS-CLD-TRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/aircell_28382/AIRCELL-ABS-CLD-TRAP-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 09:18:40 2025
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

(absCldOperStatus,
 aircell,
 usbNumber,
 usbSerialNumber,
 usbStatus) = mibBuilder.importSymbols(
    "AIRCELL-ABS-CLD-MIB",
    "absCldOperStatus",
    "aircell",
    "usbNumber",
    "usbSerialNumber",
    "usbStatus")

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

aircellAbsCldTrap = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 28382, 5)
)
if mibBuilder.loadTexts:
    aircellAbsCldTrap.setRevisions(
        ("2009-08-17 14:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CldTrap_ObjectIdentity = ObjectIdentity
cldTrap = _CldTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28382, 5, 1)
)
_CldTrapCompliances_ObjectIdentity = ObjectIdentity
cldTrapCompliances = _CldTrapCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28382, 5, 2)
)
_CldTrapGroups_ObjectIdentity = ObjectIdentity
cldTrapGroups = _CldTrapGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28382, 5, 3)
)

# Managed Objects groups


# Notification objects

absCldPlugInNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 28382, 5, 1, 1)
)
absCldPlugInNotify.setObjects(
      *(("AIRCELL-ABS-CLD-MIB", "usbStatus"),
        ("AIRCELL-ABS-CLD-MIB", "usbNumber"),
        ("AIRCELL-ABS-CLD-MIB", "usbSerialNumber"))
)
if mibBuilder.loadTexts:
    absCldPlugInNotify.setStatus(
        "current"
    )

absCldPlugOutNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 28382, 5, 1, 2)
)
absCldPlugOutNotify.setObjects(
      *(("AIRCELL-ABS-CLD-MIB", "usbStatus"),
        ("AIRCELL-ABS-CLD-MIB", "usbNumber"),
        ("AIRCELL-ABS-CLD-MIB", "usbSerialNumber"))
)
if mibBuilder.loadTexts:
    absCldPlugOutNotify.setStatus(
        "current"
    )

absCldResetNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 28382, 5, 1, 3)
)
absCldResetNotify.setObjects(
    ("AIRCELL-ABS-CLD-MIB", "absCldOperStatus")
)
if mibBuilder.loadTexts:
    absCldResetNotify.setStatus(
        "current"
    )


# Notifications groups

cldNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 28382, 5, 3, 1)
)
cldNotificationGroup.setObjects(
      *(("AIRCELL-ABS-CLD-TRAP-MIB", "absCldPlugInNotify"),
        ("AIRCELL-ABS-CLD-TRAP-MIB", "absCldPlugOutNotify"),
        ("AIRCELL-ABS-CLD-TRAP-MIB", "absCldResetNotify"))
)
if mibBuilder.loadTexts:
    cldNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cldTrapCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 28382, 5, 2, 1)
)
cldTrapCompliance.setObjects(
    ("AIRCELL-ABS-CLD-TRAP-MIB", "cldNotificationGroup")
)
if mibBuilder.loadTexts:
    cldTrapCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AIRCELL-ABS-CLD-TRAP-MIB",
    **{"aircellAbsCldTrap": aircellAbsCldTrap,
       "cldTrap": cldTrap,
       "absCldPlugInNotify": absCldPlugInNotify,
       "absCldPlugOutNotify": absCldPlugOutNotify,
       "absCldResetNotify": absCldResetNotify,
       "cldTrapCompliances": cldTrapCompliances,
       "cldTrapCompliance": cldTrapCompliance,
       "cldTrapGroups": cldTrapGroups,
       "cldNotificationGroup": cldNotificationGroup}
)
