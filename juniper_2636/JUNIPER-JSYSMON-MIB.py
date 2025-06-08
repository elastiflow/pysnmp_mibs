# SNMP MIB module (JUNIPER-JSYSMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/juniper_2636/JUNIPER-JSYSMON-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 30 16:49:54 2025
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

(jnxjSysmonMibRoot,
 jnxjSysmonNotifications) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxjSysmonMibRoot",
    "jnxjSysmonNotifications")

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

jnxjSysmon = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 90, 1)
)
if mibBuilder.loadTexts:
    jnxjSysmon.setRevisions(
        ("2019-10-23 09:24",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxjSysmonNotifyVars_ObjectIdentity = ObjectIdentity
jnxjSysmonNotifyVars = _JnxjSysmonNotifyVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 90, 1, 1)
)
if mibBuilder.loadTexts:
    jnxjSysmonNotifyVars.setStatus("current")
_JnxjSysmonTable_Object = MibTable
jnxjSysmonTable = _JnxjSysmonTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 90, 1, 1, 1)
)
if mibBuilder.loadTexts:
    jnxjSysmonTable.setStatus("current")
_JnxjSysmonEntry_Object = MibTableRow
jnxjSysmonEntry = _JnxjSysmonEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 90, 1, 1, 1, 1)
)
jnxjSysmonEntry.setIndexNames(
    (0, "JUNIPER-JSYSMON-MIB", "jnxjSysmonId"),
)
if mibBuilder.loadTexts:
    jnxjSysmonEntry.setStatus("current")
_JnxjSysmonId_Type = Unsigned32
_JnxjSysmonId_Object = MibTableColumn
jnxjSysmonId = _JnxjSysmonId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 90, 1, 1, 1, 1, 1),
    _JnxjSysmonId_Type()
)
jnxjSysmonId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxjSysmonId.setStatus("current")
_JnxjSysmonEventType_Type = DisplayString
_JnxjSysmonEventType_Object = MibTableColumn
jnxjSysmonEventType = _JnxjSysmonEventType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 90, 1, 1, 1, 1, 2),
    _JnxjSysmonEventType_Type()
)
jnxjSysmonEventType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxjSysmonEventType.setStatus("current")
_JnxjSysmonTimestamp_Type = DateAndTime
_JnxjSysmonTimestamp_Object = MibTableColumn
jnxjSysmonTimestamp = _JnxjSysmonTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 90, 1, 1, 1, 1, 3),
    _JnxjSysmonTimestamp_Type()
)
jnxjSysmonTimestamp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxjSysmonTimestamp.setStatus("current")
_JnxjSysmonEventName_Type = DisplayString
_JnxjSysmonEventName_Object = MibTableColumn
jnxjSysmonEventName = _JnxjSysmonEventName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 90, 1, 1, 1, 1, 5),
    _JnxjSysmonEventName_Type()
)
jnxjSysmonEventName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxjSysmonEventName.setStatus("current")
_JnxjSysmonResource_Type = DisplayString
_JnxjSysmonResource_Object = MibTableColumn
jnxjSysmonResource = _JnxjSysmonResource_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 90, 1, 1, 1, 1, 6),
    _JnxjSysmonResource_Type()
)
jnxjSysmonResource.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxjSysmonResource.setStatus("current")
_JnxjSysmonMessage_Type = OctetString
_JnxjSysmonMessage_Object = MibTableColumn
jnxjSysmonMessage = _JnxjSysmonMessage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 90, 1, 1, 1, 1, 7),
    _JnxjSysmonMessage_Type()
)
jnxjSysmonMessage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxjSysmonMessage.setStatus("current")
_JnxjSysmonNotificationPrefix_ObjectIdentity = ObjectIdentity
jnxjSysmonNotificationPrefix = _JnxjSysmonNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 4, 31, 0)
)
if mibBuilder.loadTexts:
    jnxjSysmonNotificationPrefix.setStatus("current")

# Managed Objects groups


# Notification objects

jnxjSysmonTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 31, 0, 1)
)
jnxjSysmonTrap.setObjects(
      *(("JUNIPER-JSYSMON-MIB", "jnxjSysmonEventType"),
        ("JUNIPER-JSYSMON-MIB", "jnxjSysmonTimestamp"),
        ("JUNIPER-JSYSMON-MIB", "jnxjSysmonEventName"),
        ("JUNIPER-JSYSMON-MIB", "jnxjSysmonResource"),
        ("JUNIPER-JSYSMON-MIB", "jnxjSysmonMessage"))
)
if mibBuilder.loadTexts:
    jnxjSysmonTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-JSYSMON-MIB",
    **{"jnxjSysmon": jnxjSysmon,
       "jnxjSysmonNotifyVars": jnxjSysmonNotifyVars,
       "jnxjSysmonTable": jnxjSysmonTable,
       "jnxjSysmonEntry": jnxjSysmonEntry,
       "jnxjSysmonId": jnxjSysmonId,
       "jnxjSysmonEventType": jnxjSysmonEventType,
       "jnxjSysmonTimestamp": jnxjSysmonTimestamp,
       "jnxjSysmonEventName": jnxjSysmonEventName,
       "jnxjSysmonResource": jnxjSysmonResource,
       "jnxjSysmonMessage": jnxjSysmonMessage,
       "jnxjSysmonNotificationPrefix": jnxjSysmonNotificationPrefix,
       "jnxjSysmonTrap": jnxjSysmonTrap}
)
