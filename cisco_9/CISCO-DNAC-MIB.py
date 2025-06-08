# SNMP MIB module (CISCO-DNAC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-DNAC-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:05:18 2025
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

ciscoDnacMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 867)
)
if mibBuilder.loadTexts:
    ciscoDnacMIB.setRevisions(
        ("2019-08-15 00:00",
         "2019-08-13 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoDnacMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoDnacMIBNotifs = _CiscoDnacMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 867, 0)
)
_CiscoDnacMIBObjects_ObjectIdentity = ObjectIdentity
ciscoDnacMIBObjects = _CiscoDnacMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 867, 1)
)
_CDnacAlarms_ObjectIdentity = ObjectIdentity
cDnacAlarms = _CDnacAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 867, 1, 1)
)


class _CDnacAlarmsMax_Type(Unsigned32):
    """Custom type cDnacAlarmsMax based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CDnacAlarmsMax_Type.__name__ = "Unsigned32"
_CDnacAlarmsMax_Object = MibScalar
cDnacAlarmsMax = _CDnacAlarmsMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 867, 1, 1, 1),
    _CDnacAlarmsMax_Type()
)
cDnacAlarmsMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cDnacAlarmsMax.setStatus("current")
_CDnacAlarmsTable_Object = MibTable
cDnacAlarmsTable = _CDnacAlarmsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 867, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cDnacAlarmsTable.setStatus("current")
_CDnacAlarmEntry_Object = MibTableRow
cDnacAlarmEntry = _CDnacAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 867, 1, 1, 2, 1)
)
cDnacAlarmEntry.setIndexNames(
    (0, "CISCO-DNAC-MIB", "cDnacIndex"),
)
if mibBuilder.loadTexts:
    cDnacAlarmEntry.setStatus("current")


class _CDnacIndex_Type(Unsigned32):
    """Custom type cDnacIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CDnacIndex_Type.__name__ = "Unsigned32"
_CDnacIndex_Object = MibTableColumn
cDnacIndex = _CDnacIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 867, 1, 1, 2, 1, 1),
    _CDnacIndex_Type()
)
cDnacIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cDnacIndex.setStatus("current")
_CDnacInstanceID_Type = SnmpAdminString
_CDnacInstanceID_Object = MibTableColumn
cDnacInstanceID = _CDnacInstanceID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 867, 1, 1, 2, 1, 2),
    _CDnacInstanceID_Type()
)
cDnacInstanceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnacInstanceID.setStatus("current")
_CDnacEventID_Type = SnmpAdminString
_CDnacEventID_Object = MibTableColumn
cDnacEventID = _CDnacEventID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 867, 1, 1, 2, 1, 3),
    _CDnacEventID_Type()
)
cDnacEventID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnacEventID.setStatus("current")
_CDnacName_Type = SnmpAdminString
_CDnacName_Object = MibTableColumn
cDnacName = _CDnacName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 867, 1, 1, 2, 1, 4),
    _CDnacName_Type()
)
cDnacName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnacName.setStatus("current")
_CDnacDescription_Type = SnmpAdminString
_CDnacDescription_Object = MibTableColumn
cDnacDescription = _CDnacDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 867, 1, 1, 2, 1, 5),
    _CDnacDescription_Type()
)
cDnacDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnacDescription.setStatus("current")
_CDnacTags_Type = SnmpAdminString
_CDnacTags_Object = MibTableColumn
cDnacTags = _CDnacTags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 867, 1, 1, 2, 1, 6),
    _CDnacTags_Type()
)
cDnacTags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnacTags.setStatus("current")
_CDnacVersion_Type = SnmpAdminString
_CDnacVersion_Object = MibTableColumn
cDnacVersion = _CDnacVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 867, 1, 1, 2, 1, 7),
    _CDnacVersion_Type()
)
cDnacVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnacVersion.setStatus("current")
_CDnacTimestamp_Type = TimeStamp
_CDnacTimestamp_Object = MibTableColumn
cDnacTimestamp = _CDnacTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 867, 1, 1, 2, 1, 8),
    _CDnacTimestamp_Type()
)
cDnacTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnacTimestamp.setStatus("current")
_CDnacDomain_Type = SnmpAdminString
_CDnacDomain_Object = MibTableColumn
cDnacDomain = _CDnacDomain_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 867, 1, 1, 2, 1, 9),
    _CDnacDomain_Type()
)
cDnacDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnacDomain.setStatus("current")
_CDnacSubDomain_Type = SnmpAdminString
_CDnacSubDomain_Object = MibTableColumn
cDnacSubDomain = _CDnacSubDomain_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 867, 1, 1, 2, 1, 10),
    _CDnacSubDomain_Type()
)
cDnacSubDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnacSubDomain.setStatus("current")
_CDnacCategory_Type = SnmpAdminString
_CDnacCategory_Object = MibTableColumn
cDnacCategory = _CDnacCategory_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 867, 1, 1, 2, 1, 11),
    _CDnacCategory_Type()
)
cDnacCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnacCategory.setStatus("current")


class _CDnacType_Type(SnmpAdminString):
    """Custom type cDnacType based on SnmpAdminString"""
    defaultValue = OctetString("SYSTEM")


_CDnacType_Type.__name__ = "SnmpAdminString"
_CDnacType_Object = MibTableColumn
cDnacType = _CDnacType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 867, 1, 1, 2, 1, 12),
    _CDnacType_Type()
)
cDnacType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnacType.setStatus("current")


class _CDnacSeverity_Type(Integer32):
    """Custom type cDnacSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_CDnacSeverity_Type.__name__ = "Integer32"
_CDnacSeverity_Object = MibTableColumn
cDnacSeverity = _CDnacSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 867, 1, 1, 2, 1, 13),
    _CDnacSeverity_Type()
)
cDnacSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnacSeverity.setStatus("current")
_CDnacSource_Type = SnmpAdminString
_CDnacSource_Object = MibTableColumn
cDnacSource = _CDnacSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 867, 1, 1, 2, 1, 14),
    _CDnacSource_Type()
)
cDnacSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnacSource.setStatus("current")


class _CDnacUserMessage_Type(OctetString):
    """Custom type cDnacUserMessage based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8192),
    )


_CDnacUserMessage_Type.__name__ = "OctetString"
_CDnacUserMessage_Object = MibTableColumn
cDnacUserMessage = _CDnacUserMessage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 867, 1, 1, 2, 1, 15),
    _CDnacUserMessage_Type()
)
cDnacUserMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnacUserMessage.setStatus("current")
_CiscoDnacMIBConform_ObjectIdentity = ObjectIdentity
ciscoDnacMIBConform = _CiscoDnacMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 867, 2)
)
_CiscoDnacMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoDnacMIBCompliances = _CiscoDnacMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 867, 2, 1)
)
_CiscoDnacMIBGroups_ObjectIdentity = ObjectIdentity
ciscoDnacMIBGroups = _CiscoDnacMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 867, 2, 2)
)

# Managed Objects groups

ciscoDnacObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 867, 2, 2, 1)
)
ciscoDnacObjectGroup.setObjects(
      *(("CISCO-DNAC-MIB", "cDnacInstanceID"),
        ("CISCO-DNAC-MIB", "cDnacEventID"),
        ("CISCO-DNAC-MIB", "cDnacName"),
        ("CISCO-DNAC-MIB", "cDnacDescription"),
        ("CISCO-DNAC-MIB", "cDnacTags"),
        ("CISCO-DNAC-MIB", "cDnacVersion"),
        ("CISCO-DNAC-MIB", "cDnacTimestamp"),
        ("CISCO-DNAC-MIB", "cDnacDomain"),
        ("CISCO-DNAC-MIB", "cDnacSubDomain"),
        ("CISCO-DNAC-MIB", "cDnacCategory"),
        ("CISCO-DNAC-MIB", "cDnacType"),
        ("CISCO-DNAC-MIB", "cDnacSeverity"),
        ("CISCO-DNAC-MIB", "cDnacSource"),
        ("CISCO-DNAC-MIB", "cDnacUserMessage"))
)
if mibBuilder.loadTexts:
    ciscoDnacObjectGroup.setStatus("current")


# Notification objects

cDnacAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 867, 0, 1)
)
cDnacAlarm.setObjects(
      *(("CISCO-DNAC-MIB", "cDnacInstanceID"),
        ("CISCO-DNAC-MIB", "cDnacEventID"),
        ("CISCO-DNAC-MIB", "cDnacName"),
        ("CISCO-DNAC-MIB", "cDnacDescription"),
        ("CISCO-DNAC-MIB", "cDnacTags"),
        ("CISCO-DNAC-MIB", "cDnacVersion"),
        ("CISCO-DNAC-MIB", "cDnacTimestamp"),
        ("CISCO-DNAC-MIB", "cDnacDomain"),
        ("CISCO-DNAC-MIB", "cDnacSubDomain"),
        ("CISCO-DNAC-MIB", "cDnacCategory"),
        ("CISCO-DNAC-MIB", "cDnacType"),
        ("CISCO-DNAC-MIB", "cDnacSeverity"),
        ("CISCO-DNAC-MIB", "cDnacSource"),
        ("CISCO-DNAC-MIB", "cDnacUserMessage"))
)
if mibBuilder.loadTexts:
    cDnacAlarm.setStatus(
        "current"
    )


# Notifications groups

ciscoDnacAlarmGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 867, 2, 2, 2)
)
ciscoDnacAlarmGroup.setObjects(
    ("CISCO-DNAC-MIB", "cDnacAlarm")
)
if mibBuilder.loadTexts:
    ciscoDnacAlarmGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoDnacMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 867, 2, 1, 1)
)
ciscoDnacMIBCompliance.setObjects(
      *(("CISCO-DNAC-MIB", "ciscoDnacObjectGroup"),
        ("CISCO-DNAC-MIB", "ciscoDnacAlarmGroup"))
)
if mibBuilder.loadTexts:
    ciscoDnacMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-DNAC-MIB",
    **{"ciscoDnacMIB": ciscoDnacMIB,
       "ciscoDnacMIBNotifs": ciscoDnacMIBNotifs,
       "cDnacAlarm": cDnacAlarm,
       "ciscoDnacMIBObjects": ciscoDnacMIBObjects,
       "cDnacAlarms": cDnacAlarms,
       "cDnacAlarmsMax": cDnacAlarmsMax,
       "cDnacAlarmsTable": cDnacAlarmsTable,
       "cDnacAlarmEntry": cDnacAlarmEntry,
       "cDnacIndex": cDnacIndex,
       "cDnacInstanceID": cDnacInstanceID,
       "cDnacEventID": cDnacEventID,
       "cDnacName": cDnacName,
       "cDnacDescription": cDnacDescription,
       "cDnacTags": cDnacTags,
       "cDnacVersion": cDnacVersion,
       "cDnacTimestamp": cDnacTimestamp,
       "cDnacDomain": cDnacDomain,
       "cDnacSubDomain": cDnacSubDomain,
       "cDnacCategory": cDnacCategory,
       "cDnacType": cDnacType,
       "cDnacSeverity": cDnacSeverity,
       "cDnacSource": cDnacSource,
       "cDnacUserMessage": cDnacUserMessage,
       "ciscoDnacMIBConform": ciscoDnacMIBConform,
       "ciscoDnacMIBCompliances": ciscoDnacMIBCompliances,
       "ciscoDnacMIBCompliance": ciscoDnacMIBCompliance,
       "ciscoDnacMIBGroups": ciscoDnacMIBGroups,
       "ciscoDnacObjectGroup": ciscoDnacObjectGroup,
       "ciscoDnacAlarmGroup": ciscoDnacAlarmGroup}
)
