# SNMP MIB module (CISCO-SNMP-NOTIFICATION-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-SNMP-NOTIFICATION-EXT-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 00:52:59 2025
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

(snmpNotifyFilterEntry,) = mibBuilder.importSymbols(
    "SNMP-NOTIFICATION-MIB",
    "snmpNotifyFilterEntry")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

ciscoSnmpNotificationExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 408)
)
if mibBuilder.loadTexts:
    ciscoSnmpNotificationExtMIB.setRevisions(
        ("2004-05-12 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CsneMIBNotifs_ObjectIdentity = ObjectIdentity
csneMIBNotifs = _CsneMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 408, 0)
)
_CsneMIBObjects_ObjectIdentity = ObjectIdentity
csneMIBObjects = _CsneMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 408, 1)
)
_CsneNotifyObjects_ObjectIdentity = ObjectIdentity
csneNotifyObjects = _CsneNotifyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 408, 1, 1)
)
_CsneSnmpNotifyFilterTable_Object = MibTable
csneSnmpNotifyFilterTable = _CsneSnmpNotifyFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 408, 1, 1, 1)
)
if mibBuilder.loadTexts:
    csneSnmpNotifyFilterTable.setStatus("current")
_CsneSnmpNotifyFilterEntry_Object = MibTableRow
csneSnmpNotifyFilterEntry = _CsneSnmpNotifyFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 408, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    csneSnmpNotifyFilterEntry.setStatus("current")


class _CsneFilterAdminTimer_Type(Unsigned32):
    """Custom type csneFilterAdminTimer based on Unsigned32"""
    defaultValue = 15


_CsneFilterAdminTimer_Type.__name__ = "Unsigned32"
_CsneFilterAdminTimer_Object = MibTableColumn
csneFilterAdminTimer = _CsneFilterAdminTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 408, 1, 1, 1, 1, 1),
    _CsneFilterAdminTimer_Type()
)
csneFilterAdminTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csneFilterAdminTimer.setStatus("current")
_CsneFilterOperTimer_Type = Unsigned32
_CsneFilterOperTimer_Object = MibTableColumn
csneFilterOperTimer = _CsneFilterOperTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 408, 1, 1, 1, 1, 2),
    _CsneFilterOperTimer_Type()
)
csneFilterOperTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csneFilterOperTimer.setStatus("current")


class _CsneFilterTimerUnit_Type(Integer32):
    """Custom type csneFilterTimerUnit based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("seconds", 1),
          ("minutes", 2),
          ("hours", 3))
    )


_CsneFilterTimerUnit_Type.__name__ = "Integer32"
_CsneFilterTimerUnit_Object = MibTableColumn
csneFilterTimerUnit = _CsneFilterTimerUnit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 408, 1, 1, 1, 1, 3),
    _CsneFilterTimerUnit_Type()
)
csneFilterTimerUnit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csneFilterTimerUnit.setStatus("current")
_CsneMIBConform_ObjectIdentity = ObjectIdentity
csneMIBConform = _CsneMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 408, 2)
)
_CsneMIBCompliances_ObjectIdentity = ObjectIdentity
csneMIBCompliances = _CsneMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 408, 2, 1)
)
_CsneMIBGroups_ObjectIdentity = ObjectIdentity
csneMIBGroups = _CsneMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 408, 2, 2)
)
snmpNotifyFilterEntry.registerAugmentions(
    ("CISCO-SNMP-NOTIFICATION-EXT-MIB",
     "csneSnmpNotifyFilterEntry")
)
csneSnmpNotifyFilterEntry.setIndexNames(*snmpNotifyFilterEntry.getIndexNames())

# Managed Objects groups

csneNotifyFilterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 408, 2, 2, 1)
)
csneNotifyFilterGroup.setObjects(
      *(("CISCO-SNMP-NOTIFICATION-EXT-MIB", "csneFilterOperTimer"),
        ("CISCO-SNMP-NOTIFICATION-EXT-MIB", "csneFilterAdminTimer"),
        ("CISCO-SNMP-NOTIFICATION-EXT-MIB", "csneFilterTimerUnit"))
)
if mibBuilder.loadTexts:
    csneNotifyFilterGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

csneMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 408, 2, 1, 1)
)
csneMIBCompliance.setObjects(
    ("CISCO-SNMP-NOTIFICATION-EXT-MIB", "csneNotifyFilterGroup")
)
if mibBuilder.loadTexts:
    csneMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-SNMP-NOTIFICATION-EXT-MIB",
    **{"ciscoSnmpNotificationExtMIB": ciscoSnmpNotificationExtMIB,
       "csneMIBNotifs": csneMIBNotifs,
       "csneMIBObjects": csneMIBObjects,
       "csneNotifyObjects": csneNotifyObjects,
       "csneSnmpNotifyFilterTable": csneSnmpNotifyFilterTable,
       "csneSnmpNotifyFilterEntry": csneSnmpNotifyFilterEntry,
       "csneFilterAdminTimer": csneFilterAdminTimer,
       "csneFilterOperTimer": csneFilterOperTimer,
       "csneFilterTimerUnit": csneFilterTimerUnit,
       "csneMIBConform": csneMIBConform,
       "csneMIBCompliances": csneMIBCompliances,
       "csneMIBCompliance": csneMIBCompliance,
       "csneMIBGroups": csneMIBGroups,
       "csneNotifyFilterGroup": csneNotifyFilterGroup}
)
