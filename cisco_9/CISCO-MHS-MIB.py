# SNMP MIB module (CISCO-MHS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-MHS-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 00:12:03 2025
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

ciscoMhsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoMhsMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoMhsMIBNotifs = _CiscoMhsMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 0)
)
_CiscoMhsMIBObjects_ObjectIdentity = ObjectIdentity
ciscoMhsMIBObjects = _CiscoMhsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1)
)
_CiscoMhsDeviceID_Type = OctetString
_CiscoMhsDeviceID_Object = MibScalar
ciscoMhsDeviceID = _CiscoMhsDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1),
    _CiscoMhsDeviceID_Type()
)
ciscoMhsDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoMhsDeviceID.setStatus("current")
_CiscoMhsStatusName_Type = OctetString
_CiscoMhsStatusName_Object = MibScalar
ciscoMhsStatusName = _CiscoMhsStatusName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 2),
    _CiscoMhsStatusName_Type()
)
ciscoMhsStatusName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoMhsStatusName.setStatus("current")
_CiscoMhsStatusValue_Type = OctetString
_CiscoMhsStatusValue_Object = MibScalar
ciscoMhsStatusValue = _CiscoMhsStatusValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 3),
    _CiscoMhsStatusValue_Type()
)
ciscoMhsStatusValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoMhsStatusValue.setStatus("current")


class _CiscoMhsServerType_Type(Integer32):
    """Custom type ciscoMhsServerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("cmhs", 1),
          ("other", 2),
          ("upload", 3),
          ("watchdog", 4))
    )


_CiscoMhsServerType_Type.__name__ = "Integer32"
_CiscoMhsServerType_Object = MibScalar
ciscoMhsServerType = _CiscoMhsServerType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 4),
    _CiscoMhsServerType_Type()
)
ciscoMhsServerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoMhsServerType.setStatus("current")
_CiscoMhsServerName_Type = OctetString
_CiscoMhsServerName_Object = MibScalar
ciscoMhsServerName = _CiscoMhsServerName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 5),
    _CiscoMhsServerName_Type()
)
ciscoMhsServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoMhsServerName.setStatus("current")


class _CiscoMhsInterfaceType_Type(Integer32):
    """Custom type ciscoMhsInterfaceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("wireline", 1),
          ("three-g", 2),
          ("all", 3))
    )


_CiscoMhsInterfaceType_Type.__name__ = "Integer32"
_CiscoMhsInterfaceType_Object = MibScalar
ciscoMhsInterfaceType = _CiscoMhsInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 6),
    _CiscoMhsInterfaceType_Type()
)
ciscoMhsInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoMhsInterfaceType.setStatus("current")
_CiscoMhsDeviceAddressType_Type = InetAddressType
_CiscoMhsDeviceAddressType_Object = MibScalar
ciscoMhsDeviceAddressType = _CiscoMhsDeviceAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 7),
    _CiscoMhsDeviceAddressType_Type()
)
ciscoMhsDeviceAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoMhsDeviceAddressType.setStatus("current")
_CiscoMhsDeviceAddress_Type = InetAddress
_CiscoMhsDeviceAddress_Object = MibScalar
ciscoMhsDeviceAddress = _CiscoMhsDeviceAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 8),
    _CiscoMhsDeviceAddress_Type()
)
ciscoMhsDeviceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoMhsDeviceAddress.setStatus("current")
_CiscoMhsServerAddressType_Type = InetAddressType
_CiscoMhsServerAddressType_Object = MibScalar
ciscoMhsServerAddressType = _CiscoMhsServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 9),
    _CiscoMhsServerAddressType_Type()
)
ciscoMhsServerAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoMhsServerAddressType.setStatus("current")
_CiscoMhsServerAddress_Type = InetAddress
_CiscoMhsServerAddress_Object = MibScalar
ciscoMhsServerAddress = _CiscoMhsServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 10),
    _CiscoMhsServerAddress_Type()
)
ciscoMhsServerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoMhsServerAddress.setStatus("current")


class _CiscoMhsAlarmSeverity_Type(Integer32):
    """Custom type ciscoMhsAlarmSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("critical", 1),
          ("major", 2),
          ("minor", 3),
          ("warning", 4),
          ("status", 5),
          ("clear", 6),
          ("informational", 7))
    )


_CiscoMhsAlarmSeverity_Type.__name__ = "Integer32"
_CiscoMhsAlarmSeverity_Object = MibScalar
ciscoMhsAlarmSeverity = _CiscoMhsAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 11),
    _CiscoMhsAlarmSeverity_Type()
)
ciscoMhsAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoMhsAlarmSeverity.setStatus("current")
_CiscoMhsOutageDuration_Type = Unsigned32
_CiscoMhsOutageDuration_Object = MibScalar
ciscoMhsOutageDuration = _CiscoMhsOutageDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 12),
    _CiscoMhsOutageDuration_Type()
)
ciscoMhsOutageDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoMhsOutageDuration.setStatus("current")
_CiscoMhsAlarmDescription_Type = OctetString
_CiscoMhsAlarmDescription_Object = MibScalar
ciscoMhsAlarmDescription = _CiscoMhsAlarmDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 13),
    _CiscoMhsAlarmDescription_Type()
)
ciscoMhsAlarmDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoMhsAlarmDescription.setStatus("current")
_CiscoMhsTimeStamp_Type = TimeStamp
_CiscoMhsTimeStamp_Object = MibScalar
ciscoMhsTimeStamp = _CiscoMhsTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 14),
    _CiscoMhsTimeStamp_Type()
)
ciscoMhsTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoMhsTimeStamp.setStatus("current")
_CiscoMhsMIBConform_ObjectIdentity = ObjectIdentity
ciscoMhsMIBConform = _CiscoMhsMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 2)
)
_CiscoMhsMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoMhsMIBCompliances = _CiscoMhsMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 2, 1)
)
_CiscoMhsMIBGroups_ObjectIdentity = ObjectIdentity
ciscoMhsMIBGroups = _CiscoMhsMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 2, 2)
)

# Managed Objects groups

ciscoMhsMIBMainObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 2, 2, 1)
)
ciscoMhsMIBMainObjectGroup.setObjects(
      *(("CISCO-MHS-MIB", "ciscoMhsDeviceID"),
        ("CISCO-MHS-MIB", "ciscoMhsStatusName"),
        ("CISCO-MHS-MIB", "ciscoMhsStatusValue"),
        ("CISCO-MHS-MIB", "ciscoMhsServerType"),
        ("CISCO-MHS-MIB", "ciscoMhsServerName"),
        ("CISCO-MHS-MIB", "ciscoMhsInterfaceType"),
        ("CISCO-MHS-MIB", "ciscoMhsDeviceAddress"),
        ("CISCO-MHS-MIB", "ciscoMhsServerAddress"),
        ("CISCO-MHS-MIB", "ciscoMhsAlarmSeverity"),
        ("CISCO-MHS-MIB", "ciscoMhsOutageDuration"),
        ("CISCO-MHS-MIB", "ciscoMhsDeviceAddressType"),
        ("CISCO-MHS-MIB", "ciscoMhsServerAddressType"),
        ("CISCO-MHS-MIB", "ciscoMhsAlarmDescription"),
        ("CISCO-MHS-MIB", "ciscoMhsTimeStamp"))
)
if mibBuilder.loadTexts:
    ciscoMhsMIBMainObjectGroup.setStatus("current")


# Notification objects

ciscoMhsHeartbeatLoss = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 0, 1)
)
ciscoMhsHeartbeatLoss.setObjects(
      *(("CISCO-MHS-MIB", "ciscoMhsDeviceID"),
        ("CISCO-MHS-MIB", "ciscoMhsInterfaceType"),
        ("CISCO-MHS-MIB", "ciscoMhsDeviceAddress"),
        ("CISCO-MHS-MIB", "ciscoMhsDeviceAddressType"),
        ("CISCO-MHS-MIB", "ciscoMhsServerAddress"),
        ("CISCO-MHS-MIB", "ciscoMhsServerAddressType"),
        ("CISCO-MHS-MIB", "ciscoMhsAlarmSeverity"),
        ("CISCO-MHS-MIB", "ciscoMhsTimeStamp"))
)
if mibBuilder.loadTexts:
    ciscoMhsHeartbeatLoss.setStatus(
        "current"
    )

ciscoMhsHeartbeatLossClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 0, 2)
)
ciscoMhsHeartbeatLossClear.setObjects(
      *(("CISCO-MHS-MIB", "ciscoMhsDeviceID"),
        ("CISCO-MHS-MIB", "ciscoMhsInterfaceType"),
        ("CISCO-MHS-MIB", "ciscoMhsDeviceAddress"),
        ("CISCO-MHS-MIB", "ciscoMhsDeviceAddressType"),
        ("CISCO-MHS-MIB", "ciscoMhsServerAddress"),
        ("CISCO-MHS-MIB", "ciscoMhsServerAddressType"),
        ("CISCO-MHS-MIB", "ciscoMhsAlarmSeverity"),
        ("CISCO-MHS-MIB", "ciscoMhsOutageDuration"),
        ("CISCO-MHS-MIB", "ciscoMhsTimeStamp"))
)
if mibBuilder.loadTexts:
    ciscoMhsHeartbeatLossClear.setStatus(
        "current"
    )

ciscoMhsStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 0, 3)
)
ciscoMhsStatusChange.setObjects(
      *(("CISCO-MHS-MIB", "ciscoMhsDeviceID"),
        ("CISCO-MHS-MIB", "ciscoMhsStatusName"),
        ("CISCO-MHS-MIB", "ciscoMhsStatusValue"),
        ("CISCO-MHS-MIB", "ciscoMhsInterfaceType"),
        ("CISCO-MHS-MIB", "ciscoMhsDeviceAddress"),
        ("CISCO-MHS-MIB", "ciscoMhsDeviceAddressType"),
        ("CISCO-MHS-MIB", "ciscoMhsServerAddress"),
        ("CISCO-MHS-MIB", "ciscoMhsServerAddressType"),
        ("CISCO-MHS-MIB", "ciscoMhsAlarmSeverity"),
        ("CISCO-MHS-MIB", "ciscoMhsTimeStamp"))
)
if mibBuilder.loadTexts:
    ciscoMhsStatusChange.setStatus(
        "current"
    )

ciscoMhsStatusChangeClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 0, 4)
)
ciscoMhsStatusChangeClear.setObjects(
      *(("CISCO-MHS-MIB", "ciscoMhsDeviceID"),
        ("CISCO-MHS-MIB", "ciscoMhsStatusName"),
        ("CISCO-MHS-MIB", "ciscoMhsStatusValue"),
        ("CISCO-MHS-MIB", "ciscoMhsInterfaceType"),
        ("CISCO-MHS-MIB", "ciscoMhsDeviceAddress"),
        ("CISCO-MHS-MIB", "ciscoMhsDeviceAddressType"),
        ("CISCO-MHS-MIB", "ciscoMhsServerAddress"),
        ("CISCO-MHS-MIB", "ciscoMhsServerAddressType"),
        ("CISCO-MHS-MIB", "ciscoMhsAlarmSeverity"),
        ("CISCO-MHS-MIB", "ciscoMhsTimeStamp"))
)
if mibBuilder.loadTexts:
    ciscoMhsStatusChangeClear.setStatus(
        "current"
    )

ciscoMhsServerAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 0, 5)
)
ciscoMhsServerAlarm.setObjects(
      *(("CISCO-MHS-MIB", "ciscoMhsServerType"),
        ("CISCO-MHS-MIB", "ciscoMhsServerName"),
        ("CISCO-MHS-MIB", "ciscoMhsAlarmDescription"),
        ("CISCO-MHS-MIB", "ciscoMhsAlarmSeverity"),
        ("CISCO-MHS-MIB", "ciscoMhsTimeStamp"))
)
if mibBuilder.loadTexts:
    ciscoMhsServerAlarm.setStatus(
        "current"
    )

ciscoMhsServerAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 0, 6)
)
ciscoMhsServerAlarmClear.setObjects(
      *(("CISCO-MHS-MIB", "ciscoMhsServerType"),
        ("CISCO-MHS-MIB", "ciscoMhsServerName"),
        ("CISCO-MHS-MIB", "ciscoMhsAlarmDescription"),
        ("CISCO-MHS-MIB", "ciscoMhsAlarmSeverity"),
        ("CISCO-MHS-MIB", "ciscoMhsTimeStamp"))
)
if mibBuilder.loadTexts:
    ciscoMhsServerAlarmClear.setStatus(
        "current"
    )


# Notifications groups

ciscoMhsMIBNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 2, 2, 2)
)
ciscoMhsMIBNotificationGroup.setObjects(
      *(("CISCO-MHS-MIB", "ciscoMhsHeartbeatLoss"),
        ("CISCO-MHS-MIB", "ciscoMhsHeartbeatLossClear"),
        ("CISCO-MHS-MIB", "ciscoMhsStatusChange"),
        ("CISCO-MHS-MIB", "ciscoMhsStatusChangeClear"),
        ("CISCO-MHS-MIB", "ciscoMhsServerAlarm"),
        ("CISCO-MHS-MIB", "ciscoMhsServerAlarmClear"))
)
if mibBuilder.loadTexts:
    ciscoMhsMIBNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoMhsMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 2, 1, 1)
)
ciscoMhsMIBCompliance.setObjects(
      *(("CISCO-MHS-MIB", "ciscoMhsMIBMainObjectGroup"),
        ("CISCO-MHS-MIB", "ciscoMhsMIBNotificationGroup"))
)
if mibBuilder.loadTexts:
    ciscoMhsMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-MHS-MIB",
    **{"ciscoMhsMIB": ciscoMhsMIB,
       "ciscoMhsMIBNotifs": ciscoMhsMIBNotifs,
       "ciscoMhsHeartbeatLoss": ciscoMhsHeartbeatLoss,
       "ciscoMhsHeartbeatLossClear": ciscoMhsHeartbeatLossClear,
       "ciscoMhsStatusChange": ciscoMhsStatusChange,
       "ciscoMhsStatusChangeClear": ciscoMhsStatusChangeClear,
       "ciscoMhsServerAlarm": ciscoMhsServerAlarm,
       "ciscoMhsServerAlarmClear": ciscoMhsServerAlarmClear,
       "ciscoMhsMIBObjects": ciscoMhsMIBObjects,
       "ciscoMhsDeviceID": ciscoMhsDeviceID,
       "ciscoMhsStatusName": ciscoMhsStatusName,
       "ciscoMhsStatusValue": ciscoMhsStatusValue,
       "ciscoMhsServerType": ciscoMhsServerType,
       "ciscoMhsServerName": ciscoMhsServerName,
       "ciscoMhsInterfaceType": ciscoMhsInterfaceType,
       "ciscoMhsDeviceAddressType": ciscoMhsDeviceAddressType,
       "ciscoMhsDeviceAddress": ciscoMhsDeviceAddress,
       "ciscoMhsServerAddressType": ciscoMhsServerAddressType,
       "ciscoMhsServerAddress": ciscoMhsServerAddress,
       "ciscoMhsAlarmSeverity": ciscoMhsAlarmSeverity,
       "ciscoMhsOutageDuration": ciscoMhsOutageDuration,
       "ciscoMhsAlarmDescription": ciscoMhsAlarmDescription,
       "ciscoMhsTimeStamp": ciscoMhsTimeStamp,
       "ciscoMhsMIBConform": ciscoMhsMIBConform,
       "ciscoMhsMIBCompliances": ciscoMhsMIBCompliances,
       "ciscoMhsMIBCompliance": ciscoMhsMIBCompliance,
       "ciscoMhsMIBGroups": ciscoMhsMIBGroups,
       "ciscoMhsMIBMainObjectGroup": ciscoMhsMIBMainObjectGroup,
       "ciscoMhsMIBNotificationGroup": ciscoMhsMIBNotificationGroup}
)
