# SNMP MIB module (ZYXEL-EXTERNAL-ALARM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/zyxel_890/ZYXEL-EXTERNAL-ALARM-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 10:07:44 2025
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

(esMgmt,) = mibBuilder.importSymbols(
    "ZYXEL-ES-SMI",
    "esMgmt")


# MODULE-IDENTITY

zyxelExternalAlarm = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 25)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelExternalAlarmTrapInfoObjects_ObjectIdentity = ObjectIdentity
zyxelExternalAlarmTrapInfoObjects = _ZyxelExternalAlarmTrapInfoObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 25, 1)
)
_ZyExternalAlarmTrapAlarmId_Type = Integer32
_ZyExternalAlarmTrapAlarmId_Object = MibScalar
zyExternalAlarmTrapAlarmId = _ZyExternalAlarmTrapAlarmId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 25, 1, 1),
    _ZyExternalAlarmTrapAlarmId_Type()
)
zyExternalAlarmTrapAlarmId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyExternalAlarmTrapAlarmId.setStatus("current")
_ZyxelExternalAlarmNotifications_ObjectIdentity = ObjectIdentity
zyxelExternalAlarmNotifications = _ZyxelExternalAlarmNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 25, 2)
)

# Managed Objects groups


# Notification objects

zyExternalAlarmDetect = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 25, 2, 1)
)
zyExternalAlarmDetect.setObjects(
    ("ZYXEL-EXTERNAL-ALARM-MIB", "zyExternalAlarmTrapAlarmId")
)
if mibBuilder.loadTexts:
    zyExternalAlarmDetect.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-EXTERNAL-ALARM-MIB",
    **{"zyxelExternalAlarm": zyxelExternalAlarm,
       "zyxelExternalAlarmTrapInfoObjects": zyxelExternalAlarmTrapInfoObjects,
       "zyExternalAlarmTrapAlarmId": zyExternalAlarmTrapAlarmId,
       "zyxelExternalAlarmNotifications": zyxelExternalAlarmNotifications,
       "zyExternalAlarmDetect": zyExternalAlarmDetect}
)
