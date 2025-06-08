# SNMP MIB module (JUNIPER-ALARM-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/juniper_2636/JUNIPER-ALARM-EXT-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 30 16:48:42 2025
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

(alarmClearEntry,) = mibBuilder.importSymbols(
    "ALARM-MIB",
    "alarmClearEntry")

(jnxAlarmExtMibRoot,
 jnxMibs) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxAlarmExtMibRoot",
    "jnxMibs")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

jnxAlarmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 72, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxAlarmObjects_ObjectIdentity = ObjectIdentity
jnxAlarmObjects = _JnxAlarmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 72, 1, 1)
)
_JnxAlarmClearTable_Object = MibTable
jnxAlarmClearTable = _JnxAlarmClearTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 72, 1, 1, 1)
)
if mibBuilder.loadTexts:
    jnxAlarmClearTable.setStatus("current")
_JnxAlarmClearEntry_Object = MibTableRow
jnxAlarmClearEntry = _JnxAlarmClearEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 72, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    jnxAlarmClearEntry.setStatus("current")
_JnxAlarmClearActiveDateAndTime_Type = DateAndTime
_JnxAlarmClearActiveDateAndTime_Object = MibTableColumn
jnxAlarmClearActiveDateAndTime = _JnxAlarmClearActiveDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 72, 1, 1, 1, 1, 1),
    _JnxAlarmClearActiveDateAndTime_Type()
)
jnxAlarmClearActiveDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAlarmClearActiveDateAndTime.setStatus("current")
alarmClearEntry.registerAugmentions(
    ("JUNIPER-ALARM-EXT-MIB",
     "jnxAlarmClearEntry")
)
jnxAlarmClearEntry.setIndexNames(*alarmClearEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-ALARM-EXT-MIB",
    **{"jnxAlarmMIB": jnxAlarmMIB,
       "jnxAlarmObjects": jnxAlarmObjects,
       "jnxAlarmClearTable": jnxAlarmClearTable,
       "jnxAlarmClearEntry": jnxAlarmClearEntry,
       "jnxAlarmClearActiveDateAndTime": jnxAlarmClearActiveDateAndTime}
)
