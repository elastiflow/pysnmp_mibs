# SNMP MIB module (VHT-SNMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/vht_46897/VHT-SNMP-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 12:06:48 2025
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

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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
 enterprises,
 experimental,
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
    "enterprises",
    "experimental",
    "iso")

(DisplayString,
 PhysAddress,
 RowStatus,
 StorageType,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention")


# MODULE-IDENTITY

vhtSnmpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 46897)
)
if mibBuilder.loadTexts:
    vhtSnmpMIB.setRevisions(
        ("2005-02-04 00:00",
         "2002-05-09 00:00",
         "2000-06-08 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VhtSnmpNotificationTriggeredBy_Type = OctetString
_VhtSnmpNotificationTriggeredBy_Object = MibScalar
vhtSnmpNotificationTriggeredBy = _VhtSnmpNotificationTriggeredBy_Object(
    (1, 3, 6, 1, 4, 1, 46897, 1),
    _VhtSnmpNotificationTriggeredBy_Type()
)
vhtSnmpNotificationTriggeredBy.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vhtSnmpNotificationTriggeredBy.setStatus("current")


class _VhtSnmpNotificationState_Type(Integer32):
    """Custom type vhtSnmpNotificationState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("start", 0),
          ("complete", 1),
          ("stop", 2),
          ("failure", 3),
          ("lostheartbeat", 4),
          ("lostconnection", 5))
    )


_VhtSnmpNotificationState_Type.__name__ = "Integer32"
_VhtSnmpNotificationState_Object = MibScalar
vhtSnmpNotificationState = _VhtSnmpNotificationState_Object(
    (1, 3, 6, 1, 4, 1, 46897, 2),
    _VhtSnmpNotificationState_Type()
)
vhtSnmpNotificationState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vhtSnmpNotificationState.setStatus("current")
_VhtNetAddressType_Type = InetAddressType
_VhtNetAddressType_Object = MibScalar
vhtNetAddressType = _VhtNetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 46897, 20),
    _VhtNetAddressType_Type()
)
vhtNetAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vhtNetAddressType.setStatus("current")
_VhtNetAddress_Type = InetAddress
_VhtNetAddress_Object = MibScalar
vhtNetAddress = _VhtNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 46897, 21),
    _VhtNetAddress_Type()
)
vhtNetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vhtNetAddress.setStatus("current")
_VhtComponentName_Type = OctetString
_VhtComponentName_Object = MibScalar
vhtComponentName = _VhtComponentName_Object(
    (1, 3, 6, 1, 4, 1, 46897, 22),
    _VhtComponentName_Type()
)
vhtComponentName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vhtComponentName.setStatus("current")

# Managed Objects groups

vhtObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 46897, 100)
)
vhtObjectGroup.setObjects(
      *(("VHT-SNMP-MIB", "vhtSnmpNotificationTriggeredBy"),
        ("VHT-SNMP-MIB", "vhtSnmpNotificationState"),
        ("VHT-SNMP-MIB", "vhtNetAddressType"),
        ("VHT-SNMP-MIB", "vhtNetAddress"))
)
if mibBuilder.loadTexts:
    vhtObjectGroup.setStatus("current")


# Notification objects

vhtSnmpManualFailoverNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 46897, 3)
)
vhtSnmpManualFailoverNotification.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("VHT-SNMP-MIB", "vhtNetAddressType"),
        ("VHT-SNMP-MIB", "vhtNetAddress"),
        ("VHT-SNMP-MIB", "vhtSnmpNotificationState"),
        ("VHT-SNMP-MIB", "vhtSnmpNotificationTriggeredBy"))
)
if mibBuilder.loadTexts:
    vhtSnmpManualFailoverNotification.setStatus(
        "current"
    )

vhtSnmpManualMaintenanceModeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 46897, 4)
)
vhtSnmpManualMaintenanceModeNotification.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("VHT-SNMP-MIB", "vhtNetAddressType"),
        ("VHT-SNMP-MIB", "vhtNetAddress"),
        ("VHT-SNMP-MIB", "vhtSnmpNotificationState"),
        ("VHT-SNMP-MIB", "vhtSnmpNotificationTriggeredBy"))
)
if mibBuilder.loadTexts:
    vhtSnmpManualMaintenanceModeNotification.setStatus(
        "current"
    )

vhtComponentChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 46897, 5)
)
vhtComponentChangeNotification.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("VHT-SNMP-MIB", "vhtNetAddressType"),
        ("VHT-SNMP-MIB", "vhtNetAddress"),
        ("VHT-SNMP-MIB", "vhtComponentName"),
        ("VHT-SNMP-MIB", "vhtSnmpNotificationState"),
        ("VHT-SNMP-MIB", "vhtSnmpNotificationTriggeredBy"))
)
if mibBuilder.loadTexts:
    vhtComponentChangeNotification.setStatus(
        "current"
    )


# Notifications groups

vhtNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 46897, 101)
)
vhtNotificationGroup.setObjects(
      *(("VHT-SNMP-MIB", "vhtSnmpManualFailoverNotification"),
        ("VHT-SNMP-MIB", "vhtSnmpManualMaintenanceModeNotification"))
)
if mibBuilder.loadTexts:
    vhtNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VHT-SNMP-MIB",
    **{"vhtSnmpMIB": vhtSnmpMIB,
       "vhtSnmpNotificationTriggeredBy": vhtSnmpNotificationTriggeredBy,
       "vhtSnmpNotificationState": vhtSnmpNotificationState,
       "vhtSnmpManualFailoverNotification": vhtSnmpManualFailoverNotification,
       "vhtSnmpManualMaintenanceModeNotification": vhtSnmpManualMaintenanceModeNotification,
       "vhtComponentChangeNotification": vhtComponentChangeNotification,
       "vhtNetAddressType": vhtNetAddressType,
       "vhtNetAddress": vhtNetAddress,
       "vhtComponentName": vhtComponentName,
       "vhtObjectGroup": vhtObjectGroup,
       "vhtNotificationGroup": vhtNotificationGroup}
)
