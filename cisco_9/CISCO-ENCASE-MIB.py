# SNMP MIB module (CISCO-ENCASE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-ENCASE-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:11:57 2025
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

(EncaseAppName,) = mibBuilder.importSymbols(
    "CISCO-ENCASE-APP-NAME-MIB",
    "EncaseAppName")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(Unsigned32,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "Unsigned32")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoEncaseMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 143)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class EncaseConnMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("other", 2),
          ("telnet", 3),
          ("console", 4),
          ("snmp", 5),
          ("periodicScan", 6))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoEncaseMIBObjects_ObjectIdentity = ObjectIdentity
ciscoEncaseMIBObjects = _CiscoEncaseMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 143, 1)
)
_EncaseBasic_ObjectIdentity = ObjectIdentity
encaseBasic = _EncaseBasic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 143, 1, 1)
)


class _EncaseNotifiesEnabled_Type(TruthValue):
    """Custom type encaseNotifiesEnabled based on TruthValue"""
    defaultValue = 2


_EncaseNotifiesEnabled_Type.__name__ = "TruthValue"
_EncaseNotifiesEnabled_Object = MibScalar
encaseNotifiesEnabled = _EncaseNotifiesEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 143, 1, 1, 1),
    _EncaseNotifiesEnabled_Type()
)
encaseNotifiesEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    encaseNotifiesEnabled.setStatus("current")
_EncaseHistory_ObjectIdentity = ObjectIdentity
encaseHistory = _EncaseHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 143, 1, 2)
)


class _EncaseHistTableMaxLength_Type(Integer32):
    """Custom type encaseHistTableMaxLength based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_EncaseHistTableMaxLength_Type.__name__ = "Integer32"
_EncaseHistTableMaxLength_Object = MibScalar
encaseHistTableMaxLength = _EncaseHistTableMaxLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 143, 1, 2, 1),
    _EncaseHistTableMaxLength_Type()
)
encaseHistTableMaxLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    encaseHistTableMaxLength.setStatus("current")
if mibBuilder.loadTexts:
    encaseHistTableMaxLength.setUnits("entries")
_EncaseHistIndexLast_Type = Unsigned32
_EncaseHistIndexLast_Object = MibScalar
encaseHistIndexLast = _EncaseHistIndexLast_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 143, 1, 2, 2),
    _EncaseHistIndexLast_Type()
)
encaseHistIndexLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encaseHistIndexLast.setStatus("current")
_EncaseHistoryTable_Object = MibTable
encaseHistoryTable = _EncaseHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 143, 1, 2, 3)
)
if mibBuilder.loadTexts:
    encaseHistoryTable.setStatus("current")
_EncaseHistoryEntry_Object = MibTableRow
encaseHistoryEntry = _EncaseHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 143, 1, 2, 3, 1)
)
encaseHistoryEntry.setIndexNames(
    (0, "CISCO-ENCASE-MIB", "encaseHistIndex"),
)
if mibBuilder.loadTexts:
    encaseHistoryEntry.setStatus("current")
_EncaseHistIndex_Type = Unsigned32
_EncaseHistIndex_Object = MibTableColumn
encaseHistIndex = _EncaseHistIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 143, 1, 2, 3, 1, 1),
    _EncaseHistIndex_Type()
)
encaseHistIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    encaseHistIndex.setStatus("current")
_EncaseHistAppName_Type = EncaseAppName
_EncaseHistAppName_Object = MibTableColumn
encaseHistAppName = _EncaseHistAppName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 143, 1, 2, 3, 1, 2),
    _EncaseHistAppName_Type()
)
encaseHistAppName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encaseHistAppName.setStatus("current")
_EncaseHistConnectionMode_Type = EncaseConnMode
_EncaseHistConnectionMode_Object = MibTableColumn
encaseHistConnectionMode = _EncaseHistConnectionMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 143, 1, 2, 3, 1, 3),
    _EncaseHistConnectionMode_Type()
)
encaseHistConnectionMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encaseHistConnectionMode.setStatus("current")
_EncaseHistCreationTime_Type = DateAndTime
_EncaseHistCreationTime_Object = MibTableColumn
encaseHistCreationTime = _EncaseHistCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 143, 1, 2, 3, 1, 4),
    _EncaseHistCreationTime_Type()
)
encaseHistCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encaseHistCreationTime.setStatus("current")


class _EncaseHistDeviceName_Type(SnmpAdminString):
    """Custom type encaseHistDeviceName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EncaseHistDeviceName_Type.__name__ = "SnmpAdminString"
_EncaseHistDeviceName_Object = MibTableColumn
encaseHistDeviceName = _EncaseHistDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 143, 1, 2, 3, 1, 5),
    _EncaseHistDeviceName_Type()
)
encaseHistDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encaseHistDeviceName.setStatus("current")


class _EncaseHistHostName_Type(SnmpAdminString):
    """Custom type encaseHistHostName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EncaseHistHostName_Type.__name__ = "SnmpAdminString"
_EncaseHistHostName_Object = MibTableColumn
encaseHistHostName = _EncaseHistHostName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 143, 1, 2, 3, 1, 6),
    _EncaseHistHostName_Type()
)
encaseHistHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encaseHistHostName.setStatus("current")


class _EncaseHistChangeMessage_Type(SnmpAdminString):
    """Custom type encaseHistChangeMessage based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EncaseHistChangeMessage_Type.__name__ = "SnmpAdminString"
_EncaseHistChangeMessage_Object = MibTableColumn
encaseHistChangeMessage = _EncaseHistChangeMessage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 143, 1, 2, 3, 1, 7),
    _EncaseHistChangeMessage_Type()
)
encaseHistChangeMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encaseHistChangeMessage.setStatus("current")


class _EncaseHistUserName_Type(SnmpAdminString):
    """Custom type encaseHistUserName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EncaseHistUserName_Type.__name__ = "SnmpAdminString"
_EncaseHistUserName_Object = MibTableColumn
encaseHistUserName = _EncaseHistUserName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 143, 1, 2, 3, 1, 8),
    _EncaseHistUserName_Type()
)
encaseHistUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encaseHistUserName.setStatus("current")
_CiscoEncaseMIBNotificationsPrefix_ObjectIdentity = ObjectIdentity
ciscoEncaseMIBNotificationsPrefix = _CiscoEncaseMIBNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 143, 2)
)
_CiscoEncaseMIBNotifications_ObjectIdentity = ObjectIdentity
ciscoEncaseMIBNotifications = _CiscoEncaseMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 143, 2, 0)
)
_CiscoEncaseMIBConformance_ObjectIdentity = ObjectIdentity
ciscoEncaseMIBConformance = _CiscoEncaseMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 143, 3)
)
_CiscoEncaseMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoEncaseMIBCompliances = _CiscoEncaseMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 143, 3, 1)
)
_CiscoEncaseMIBGroups_ObjectIdentity = ObjectIdentity
ciscoEncaseMIBGroups = _CiscoEncaseMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 143, 3, 2)
)

# Managed Objects groups

ciscoEncaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 143, 3, 2, 1)
)
ciscoEncaseGroup.setObjects(
      *(("CISCO-ENCASE-MIB", "encaseHistTableMaxLength"),
        ("CISCO-ENCASE-MIB", "encaseHistIndexLast"),
        ("CISCO-ENCASE-MIB", "encaseHistAppName"),
        ("CISCO-ENCASE-MIB", "encaseHistConnectionMode"),
        ("CISCO-ENCASE-MIB", "encaseHistCreationTime"),
        ("CISCO-ENCASE-MIB", "encaseHistDeviceName"),
        ("CISCO-ENCASE-MIB", "encaseHistHostName"),
        ("CISCO-ENCASE-MIB", "encaseHistChangeMessage"),
        ("CISCO-ENCASE-MIB", "encaseHistUserName"))
)
if mibBuilder.loadTexts:
    ciscoEncaseGroup.setStatus("current")

ciscoEncaseFilterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 143, 3, 2, 2)
)
ciscoEncaseFilterGroup.setObjects(
    ("CISCO-ENCASE-MIB", "encaseNotifiesEnabled")
)
if mibBuilder.loadTexts:
    ciscoEncaseFilterGroup.setStatus("current")


# Notification objects

encaseChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 143, 2, 0, 1)
)
encaseChangeEvent.setObjects(
      *(("CISCO-ENCASE-MIB", "encaseHistAppName"),
        ("CISCO-ENCASE-MIB", "encaseHistConnectionMode"),
        ("CISCO-ENCASE-MIB", "encaseHistCreationTime"),
        ("CISCO-ENCASE-MIB", "encaseHistDeviceName"),
        ("CISCO-ENCASE-MIB", "encaseHistHostName"),
        ("CISCO-ENCASE-MIB", "encaseHistChangeMessage"),
        ("CISCO-ENCASE-MIB", "encaseHistUserName"))
)
if mibBuilder.loadTexts:
    encaseChangeEvent.setStatus(
        "current"
    )


# Notifications groups

ciscoEncaseNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 143, 3, 2, 3)
)
ciscoEncaseNotificationsGroup.setObjects(
    ("CISCO-ENCASE-MIB", "encaseChangeEvent")
)
if mibBuilder.loadTexts:
    ciscoEncaseNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoEncaseMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 143, 3, 1, 1)
)
ciscoEncaseMIBCompliance.setObjects(
      *(("CISCO-ENCASE-MIB", "ciscoEncaseGroup"),
        ("CISCO-ENCASE-MIB", "ciscoEncaseFilterGroup"),
        ("CISCO-ENCASE-MIB", "ciscoEncaseNotificationsGroup"))
)
if mibBuilder.loadTexts:
    ciscoEncaseMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ENCASE-MIB",
    **{"EncaseConnMode": EncaseConnMode,
       "ciscoEncaseMIB": ciscoEncaseMIB,
       "ciscoEncaseMIBObjects": ciscoEncaseMIBObjects,
       "encaseBasic": encaseBasic,
       "encaseNotifiesEnabled": encaseNotifiesEnabled,
       "encaseHistory": encaseHistory,
       "encaseHistTableMaxLength": encaseHistTableMaxLength,
       "encaseHistIndexLast": encaseHistIndexLast,
       "encaseHistoryTable": encaseHistoryTable,
       "encaseHistoryEntry": encaseHistoryEntry,
       "encaseHistIndex": encaseHistIndex,
       "encaseHistAppName": encaseHistAppName,
       "encaseHistConnectionMode": encaseHistConnectionMode,
       "encaseHistCreationTime": encaseHistCreationTime,
       "encaseHistDeviceName": encaseHistDeviceName,
       "encaseHistHostName": encaseHistHostName,
       "encaseHistChangeMessage": encaseHistChangeMessage,
       "encaseHistUserName": encaseHistUserName,
       "ciscoEncaseMIBNotificationsPrefix": ciscoEncaseMIBNotificationsPrefix,
       "ciscoEncaseMIBNotifications": ciscoEncaseMIBNotifications,
       "encaseChangeEvent": encaseChangeEvent,
       "ciscoEncaseMIBConformance": ciscoEncaseMIBConformance,
       "ciscoEncaseMIBCompliances": ciscoEncaseMIBCompliances,
       "ciscoEncaseMIBCompliance": ciscoEncaseMIBCompliance,
       "ciscoEncaseMIBGroups": ciscoEncaseMIBGroups,
       "ciscoEncaseGroup": ciscoEncaseGroup,
       "ciscoEncaseFilterGroup": ciscoEncaseFilterGroup,
       "ciscoEncaseNotificationsGroup": ciscoEncaseNotificationsGroup}
)
