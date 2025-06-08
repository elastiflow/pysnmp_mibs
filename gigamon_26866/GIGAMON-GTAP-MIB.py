# SNMP MIB module (GIGAMON-GTAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/gigamon_26866/GIGAMON-GTAP-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 23:14:46 2025
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

(sysLocation,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysLocation")

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

gigamonSnmp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 26866)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_GigamonSnmpNotifications_ObjectIdentity = ObjectIdentity
gigamonSnmpNotifications = _GigamonSnmpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26866, 1)
)
_GigamonGtap_ObjectIdentity = ObjectIdentity
gigamonGtap = _GigamonGtap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26866, 1, 3)
)
_GigamonGtapNotificationObjects_ObjectIdentity = ObjectIdentity
gigamonGtapNotificationObjects = _GigamonGtapNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26866, 1, 4)
)


class _GigamonGtapNotifLevel_Type(Integer32):
    """Custom type gigamonGtapNotifLevel based on Integer32"""
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
        *(("information", 1),
          ("minor", 2),
          ("major", 3),
          ("critical", 4))
    )


_GigamonGtapNotifLevel_Type.__name__ = "Integer32"
_GigamonGtapNotifLevel_Object = MibScalar
gigamonGtapNotifLevel = _GigamonGtapNotifLevel_Object(
    (1, 3, 6, 1, 4, 1, 26866, 1, 4, 1),
    _GigamonGtapNotifLevel_Type()
)
gigamonGtapNotifLevel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gigamonGtapNotifLevel.setStatus("current")
_GigamonTapNotifDescription_Type = OctetString
_GigamonTapNotifDescription_Object = MibScalar
gigamonTapNotifDescription = _GigamonTapNotifDescription_Object(
    (1, 3, 6, 1, 4, 1, 26866, 1, 4, 2),
    _GigamonTapNotifDescription_Type()
)
gigamonTapNotifDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gigamonTapNotifDescription.setStatus("current")
_GigamonGtapNotifPortName_Type = OctetString
_GigamonGtapNotifPortName_Object = MibScalar
gigamonGtapNotifPortName = _GigamonGtapNotifPortName_Object(
    (1, 3, 6, 1, 4, 1, 26866, 1, 4, 3),
    _GigamonGtapNotifPortName_Type()
)
gigamonGtapNotifPortName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gigamonGtapNotifPortName.setStatus("current")


class _GigamonGtapNotifPortLinkStatus_Type(Integer32):
    """Custom type gigamonGtapNotifPortLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )


_GigamonGtapNotifPortLinkStatus_Type.__name__ = "Integer32"
_GigamonGtapNotifPortLinkStatus_Object = MibScalar
gigamonGtapNotifPortLinkStatus = _GigamonGtapNotifPortLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 26866, 1, 4, 4),
    _GigamonGtapNotifPortLinkStatus_Type()
)
gigamonGtapNotifPortLinkStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gigamonGtapNotifPortLinkStatus.setStatus("current")


class _GigamonGtapNotifPowerStatus_Type(Integer32):
    """Custom type gigamonGtapNotifPowerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("failure", -1),
          ("abnormal", 0),
          ("normal", 1))
    )


_GigamonGtapNotifPowerStatus_Type.__name__ = "Integer32"
_GigamonGtapNotifPowerStatus_Object = MibScalar
gigamonGtapNotifPowerStatus = _GigamonGtapNotifPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 26866, 1, 4, 5),
    _GigamonGtapNotifPowerStatus_Type()
)
gigamonGtapNotifPowerStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gigamonGtapNotifPowerStatus.setStatus("current")


class _GigamonGtapNotifFanStatus_Type(Integer32):
    """Custom type gigamonGtapNotifFanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("failure", -1),
          ("abnormal", 0),
          ("normal", 1))
    )


_GigamonGtapNotifFanStatus_Type.__name__ = "Integer32"
_GigamonGtapNotifFanStatus_Object = MibScalar
gigamonGtapNotifFanStatus = _GigamonGtapNotifFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 26866, 1, 4, 6),
    _GigamonGtapNotifFanStatus_Type()
)
gigamonGtapNotifFanStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gigamonGtapNotifFanStatus.setStatus("current")


class _GigamonGtapBatteryLevel_Type(Integer32):
    """Custom type gigamonGtapBatteryLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("batteryChargeComplete", 0),
          ("downBelow75", 1),
          ("downBelow50", 2),
          ("downBelow25", 3),
          ("shutDownSystem", 4))
    )


_GigamonGtapBatteryLevel_Type.__name__ = "Integer32"
_GigamonGtapBatteryLevel_Object = MibScalar
gigamonGtapBatteryLevel = _GigamonGtapBatteryLevel_Object(
    (1, 3, 6, 1, 4, 1, 26866, 1, 4, 7),
    _GigamonGtapBatteryLevel_Type()
)
gigamonGtapBatteryLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigamonGtapBatteryLevel.setStatus("current")


class _GigamonGtapPortLinkSpeed_Type(Integer32):
    """Custom type gigamonGtapPortLinkSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("notApply", 0),
          ("speed10", 1),
          ("speed100", 2),
          ("speed1000", 3),
          ("speed10000", 4))
    )


_GigamonGtapPortLinkSpeed_Type.__name__ = "Integer32"
_GigamonGtapPortLinkSpeed_Object = MibScalar
gigamonGtapPortLinkSpeed = _GigamonGtapPortLinkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 26866, 1, 4, 8),
    _GigamonGtapPortLinkSpeed_Type()
)
gigamonGtapPortLinkSpeed.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gigamonGtapPortLinkSpeed.setStatus("current")


class _GigamonGtapPowerSource_Type(Integer32):
    """Custom type gigamonGtapPowerSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mainPower", 0),
          ("poe", 1),
          ("power48V", 2),
          ("battery", 3))
    )


_GigamonGtapPowerSource_Type.__name__ = "Integer32"
_GigamonGtapPowerSource_Object = MibScalar
gigamonGtapPowerSource = _GigamonGtapPowerSource_Object(
    (1, 3, 6, 1, 4, 1, 26866, 1, 4, 9),
    _GigamonGtapPowerSource_Type()
)
gigamonGtapPowerSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigamonGtapPowerSource.setStatus("current")


class _GigamonGtapNotifPortSignalDetect_Type(Integer32):
    """Custom type gigamonGtapNotifPortSignalDetect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_GigamonGtapNotifPortSignalDetect_Type.__name__ = "Integer32"
_GigamonGtapNotifPortSignalDetect_Object = MibScalar
gigamonGtapNotifPortSignalDetect = _GigamonGtapNotifPortSignalDetect_Object(
    (1, 3, 6, 1, 4, 1, 26866, 1, 4, 10),
    _GigamonGtapNotifPortSignalDetect_Type()
)
gigamonGtapNotifPortSignalDetect.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gigamonGtapNotifPortSignalDetect.setStatus("current")

# Managed Objects groups


# Notification objects

gigamonGtapResetSystemNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 26866, 1, 3, 1)
)
gigamonGtapResetSystemNotification.setObjects(
      *(("GIGAMON-GTAP-MIB", "gigamonGtapNotifLevel"),
        ("GIGAMON-GTAP-MIB", "gigamonTapNotifDescription"))
)
if mibBuilder.loadTexts:
    gigamonGtapResetSystemNotification.setStatus(
        "current"
    )

gigamonGtapPowerChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 26866, 1, 3, 2)
)
gigamonGtapPowerChangeNotification.setObjects(
      *(("GIGAMON-GTAP-MIB", "gigamonGtapNotifLevel"),
        ("GIGAMON-GTAP-MIB", "gigamonGtapNotifPowerStatus"))
)
if mibBuilder.loadTexts:
    gigamonGtapPowerChangeNotification.setStatus(
        "current"
    )

gigamonGtapBatterryLevelChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 26866, 1, 3, 3)
)
gigamonGtapBatterryLevelChangeNotification.setObjects(
      *(("GIGAMON-GTAP-MIB", "gigamonGtapNotifLevel"),
        ("GIGAMON-GTAP-MIB", "gigamonGtapBatteryLevel"))
)
if mibBuilder.loadTexts:
    gigamonGtapBatterryLevelChangeNotification.setStatus(
        "current"
    )

gigamonGtapLinkStatusChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 26866, 1, 3, 4)
)
gigamonGtapLinkStatusChangeNotification.setObjects(
      *(("GIGAMON-GTAP-MIB", "gigamonGtapNotifPortName"),
        ("GIGAMON-GTAP-MIB", "gigamonGtapNotifPortLinkStatus"))
)
if mibBuilder.loadTexts:
    gigamonGtapLinkStatusChangeNotification.setStatus(
        "current"
    )

gigamonGtapLinkSpeedChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 26866, 1, 3, 5)
)
gigamonGtapLinkSpeedChangeNotification.setObjects(
      *(("GIGAMON-GTAP-MIB", "gigamonGtapNotifPortName"),
        ("GIGAMON-GTAP-MIB", "gigamonGtapPortLinkSpeed"))
)
if mibBuilder.loadTexts:
    gigamonGtapLinkSpeedChangeNotification.setStatus(
        "current"
    )

gigamonGtapPowerSourceChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 26866, 1, 3, 6)
)
gigamonGtapPowerSourceChangeNotification.setObjects(
      *(("GIGAMON-GTAP-MIB", "gigamonGtapNotifLevel"),
        ("GIGAMON-GTAP-MIB", "gigamonGtapPowerSource"))
)
if mibBuilder.loadTexts:
    gigamonGtapPowerSourceChangeNotification.setStatus(
        "current"
    )

gigamonGtapFanChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 26866, 1, 3, 7)
)
gigamonGtapFanChangeNotification.setObjects(
      *(("GIGAMON-GTAP-MIB", "gigamonGtapNotifLevel"),
        ("GIGAMON-GTAP-MIB", "gigamonGtapNotifFanStatus"))
)
if mibBuilder.loadTexts:
    gigamonGtapFanChangeNotification.setStatus(
        "current"
    )

gigamonGtapPortSignalDetectNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 26866, 1, 3, 8)
)
gigamonGtapPortSignalDetectNotification.setObjects(
      *(("GIGAMON-GTAP-MIB", "gigamonGtapNotifPortName"),
        ("GIGAMON-GTAP-MIB", "gigamonGtapNotifPortSignalDetect"))
)
if mibBuilder.loadTexts:
    gigamonGtapPortSignalDetectNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GIGAMON-GTAP-MIB",
    **{"gigamonSnmp": gigamonSnmp,
       "gigamonSnmpNotifications": gigamonSnmpNotifications,
       "gigamonGtap": gigamonGtap,
       "gigamonGtapResetSystemNotification": gigamonGtapResetSystemNotification,
       "gigamonGtapPowerChangeNotification": gigamonGtapPowerChangeNotification,
       "gigamonGtapBatterryLevelChangeNotification": gigamonGtapBatterryLevelChangeNotification,
       "gigamonGtapLinkStatusChangeNotification": gigamonGtapLinkStatusChangeNotification,
       "gigamonGtapLinkSpeedChangeNotification": gigamonGtapLinkSpeedChangeNotification,
       "gigamonGtapPowerSourceChangeNotification": gigamonGtapPowerSourceChangeNotification,
       "gigamonGtapFanChangeNotification": gigamonGtapFanChangeNotification,
       "gigamonGtapPortSignalDetectNotification": gigamonGtapPortSignalDetectNotification,
       "gigamonGtapNotificationObjects": gigamonGtapNotificationObjects,
       "gigamonGtapNotifLevel": gigamonGtapNotifLevel,
       "gigamonTapNotifDescription": gigamonTapNotifDescription,
       "gigamonGtapNotifPortName": gigamonGtapNotifPortName,
       "gigamonGtapNotifPortLinkStatus": gigamonGtapNotifPortLinkStatus,
       "gigamonGtapNotifPowerStatus": gigamonGtapNotifPowerStatus,
       "gigamonGtapNotifFanStatus": gigamonGtapNotifFanStatus,
       "gigamonGtapBatteryLevel": gigamonGtapBatteryLevel,
       "gigamonGtapPortLinkSpeed": gigamonGtapPortLinkSpeed,
       "gigamonGtapPowerSource": gigamonGtapPowerSource,
       "gigamonGtapNotifPortSignalDetect": gigamonGtapNotifPortSignalDetect}
)
