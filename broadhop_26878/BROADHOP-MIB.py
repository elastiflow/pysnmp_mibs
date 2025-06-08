# SNMP MIB module (BROADHOP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/broadhop_26878/BROADHOP-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 00:18:03 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

broadhop = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 26878)
)
if mibBuilder.loadTexts:
    broadhop.setRevisions(
        ("2012-07-05 00:00",
         "2012-01-27 00:00",
         "2009-06-21 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BroadhopCommon_ObjectIdentity = ObjectIdentity
broadhopCommon = _BroadhopCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26878, 100)
)
_BroadhopCommonNotificationsGroup_ObjectIdentity = ObjectIdentity
broadhopCommonNotificationsGroup = _BroadhopCommonNotificationsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26878, 100, 1)
)
_BroadhopNotificationParameters_ObjectIdentity = ObjectIdentity
broadhopNotificationParameters = _BroadhopNotificationParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26878, 100, 1, 1)
)
_BroadhopAlarmDeviceName_Type = DisplayString
_BroadhopAlarmDeviceName_Object = MibScalar
broadhopAlarmDeviceName = _BroadhopAlarmDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 26878, 100, 1, 1, 1),
    _BroadhopAlarmDeviceName_Type()
)
broadhopAlarmDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    broadhopAlarmDeviceName.setStatus("deprecated")


class _BroadhopAlarmErrorNumber_Type(Integer32):
    """Custom type broadhopAlarmErrorNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_BroadhopAlarmErrorNumber_Type.__name__ = "Integer32"
_BroadhopAlarmErrorNumber_Object = MibScalar
broadhopAlarmErrorNumber = _BroadhopAlarmErrorNumber_Object(
    (1, 3, 6, 1, 4, 1, 26878, 100, 1, 1, 2),
    _BroadhopAlarmErrorNumber_Type()
)
broadhopAlarmErrorNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    broadhopAlarmErrorNumber.setStatus("deprecated")
_BroadhopAlarmErrorText_Type = DisplayString
_BroadhopAlarmErrorText_Object = MibScalar
broadhopAlarmErrorText = _BroadhopAlarmErrorText_Object(
    (1, 3, 6, 1, 4, 1, 26878, 100, 1, 1, 3),
    _BroadhopAlarmErrorText_Type()
)
broadhopAlarmErrorText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    broadhopAlarmErrorText.setStatus("deprecated")
_BroadhopAlarmDateAndTime_Type = DisplayString
_BroadhopAlarmDateAndTime_Object = MibScalar
broadhopAlarmDateAndTime = _BroadhopAlarmDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 26878, 100, 1, 1, 4),
    _BroadhopAlarmDateAndTime_Type()
)
broadhopAlarmDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    broadhopAlarmDateAndTime.setStatus("deprecated")
_BroadhopAlarmProbableCause_Type = DisplayString
_BroadhopAlarmProbableCause_Object = MibScalar
broadhopAlarmProbableCause = _BroadhopAlarmProbableCause_Object(
    (1, 3, 6, 1, 4, 1, 26878, 100, 1, 1, 5),
    _BroadhopAlarmProbableCause_Type()
)
broadhopAlarmProbableCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    broadhopAlarmProbableCause.setStatus("deprecated")
_BroadhopAlarmAdditionalInfo_Type = DisplayString
_BroadhopAlarmAdditionalInfo_Object = MibScalar
broadhopAlarmAdditionalInfo = _BroadhopAlarmAdditionalInfo_Object(
    (1, 3, 6, 1, 4, 1, 26878, 100, 1, 1, 6),
    _BroadhopAlarmAdditionalInfo_Type()
)
broadhopAlarmAdditionalInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    broadhopAlarmAdditionalInfo.setStatus("deprecated")
_BroadhopComponentName_Type = DisplayString
_BroadhopComponentName_Object = MibScalar
broadhopComponentName = _BroadhopComponentName_Object(
    (1, 3, 6, 1, 4, 1, 26878, 100, 1, 1, 7),
    _BroadhopComponentName_Type()
)
broadhopComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    broadhopComponentName.setStatus("current")
_BroadhopComponentTime_Type = DisplayString
_BroadhopComponentTime_Object = MibScalar
broadhopComponentTime = _BroadhopComponentTime_Object(
    (1, 3, 6, 1, 4, 1, 26878, 100, 1, 1, 8),
    _BroadhopComponentTime_Type()
)
broadhopComponentTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    broadhopComponentTime.setStatus("current")
_BroadhopComponentNotificationName_Type = DisplayString
_BroadhopComponentNotificationName_Object = MibScalar
broadhopComponentNotificationName = _BroadhopComponentNotificationName_Object(
    (1, 3, 6, 1, 4, 1, 26878, 100, 1, 1, 9),
    _BroadhopComponentNotificationName_Type()
)
broadhopComponentNotificationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    broadhopComponentNotificationName.setStatus("current")
_BroadhopComponentAdditionalInfo_Type = DisplayString
_BroadhopComponentAdditionalInfo_Object = MibScalar
broadhopComponentAdditionalInfo = _BroadhopComponentAdditionalInfo_Object(
    (1, 3, 6, 1, 4, 1, 26878, 100, 1, 1, 10),
    _BroadhopComponentAdditionalInfo_Type()
)
broadhopComponentAdditionalInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    broadhopComponentAdditionalInfo.setStatus("current")
_BroadhopNotificationPrefix_ObjectIdentity = ObjectIdentity
broadhopNotificationPrefix = _BroadhopNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26878, 100, 1, 2)
)
_BroadhopNotifications_ObjectIdentity = ObjectIdentity
broadhopNotifications = _BroadhopNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26878, 100, 1, 2, 0)
)


class _BroadhopNotificationFacility_Type(Integer32):
    """Custom type broadhopNotificationFacility based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("hardware", 0),
          ("network", 1),
          ("virtualization", 2),
          ("operatingsystem", 3),
          ("application", 4),
          ("process", 5),
          ("none", 6))
    )


_BroadhopNotificationFacility_Type.__name__ = "Integer32"
_BroadhopNotificationFacility_Object = MibScalar
broadhopNotificationFacility = _BroadhopNotificationFacility_Object(
    (1, 3, 6, 1, 4, 1, 26878, 100, 1, 3),
    _BroadhopNotificationFacility_Type()
)
broadhopNotificationFacility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    broadhopNotificationFacility.setStatus("current")


class _BroadhopNotificationSeverity_Type(Integer32):
    """Custom type broadhopNotificationSeverity based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("emergency", 0),
          ("alert", 1),
          ("critical", 2),
          ("error", 3),
          ("warning", 4),
          ("notice", 5),
          ("info", 6),
          ("debug", 7),
          ("none", 8),
          ("clear", 9))
    )


_BroadhopNotificationSeverity_Type.__name__ = "Integer32"
_BroadhopNotificationSeverity_Object = MibScalar
broadhopNotificationSeverity = _BroadhopNotificationSeverity_Object(
    (1, 3, 6, 1, 4, 1, 26878, 100, 1, 4),
    _BroadhopNotificationSeverity_Type()
)
broadhopNotificationSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    broadhopNotificationSeverity.setStatus("current")
_BroadhopProducts_ObjectIdentity = ObjectIdentity
broadhopProducts = _BroadhopProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26878, 200)
)

# Managed Objects groups


# Notification objects

broadhopCriticalAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 26878, 100, 1, 2, 0, 1)
)
broadhopCriticalAlarm.setObjects(
      *(("BROADHOP-MIB", "broadhopAlarmDeviceName"),
        ("BROADHOP-MIB", "broadhopAlarmErrorNumber"),
        ("BROADHOP-MIB", "broadhopAlarmErrorText"),
        ("BROADHOP-MIB", "broadhopAlarmDateAndTime"),
        ("BROADHOP-MIB", "broadhopAlarmProbableCause"),
        ("BROADHOP-MIB", "broadhopAlarmAdditionalInfo"))
)
if mibBuilder.loadTexts:
    broadhopCriticalAlarm.setStatus(
        "deprecated"
    )

broadhopMajorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 26878, 100, 1, 2, 0, 2)
)
broadhopMajorAlarm.setObjects(
      *(("BROADHOP-MIB", "broadhopAlarmDeviceName"),
        ("BROADHOP-MIB", "broadhopAlarmErrorNumber"),
        ("BROADHOP-MIB", "broadhopAlarmErrorText"),
        ("BROADHOP-MIB", "broadhopAlarmDateAndTime"),
        ("BROADHOP-MIB", "broadhopAlarmProbableCause"),
        ("BROADHOP-MIB", "broadhopAlarmAdditionalInfo"))
)
if mibBuilder.loadTexts:
    broadhopMajorAlarm.setStatus(
        "deprecated"
    )

broadhopMinorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 26878, 100, 1, 2, 0, 3)
)
broadhopMinorAlarm.setObjects(
      *(("BROADHOP-MIB", "broadhopAlarmDeviceName"),
        ("BROADHOP-MIB", "broadhopAlarmErrorNumber"),
        ("BROADHOP-MIB", "broadhopAlarmErrorText"),
        ("BROADHOP-MIB", "broadhopAlarmDateAndTime"),
        ("BROADHOP-MIB", "broadhopAlarmProbableCause"),
        ("BROADHOP-MIB", "broadhopAlarmAdditionalInfo"))
)
if mibBuilder.loadTexts:
    broadhopMinorAlarm.setStatus(
        "deprecated"
    )

broadhopWarningAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 26878, 100, 1, 2, 0, 4)
)
broadhopWarningAlarm.setObjects(
      *(("BROADHOP-MIB", "broadhopAlarmDeviceName"),
        ("BROADHOP-MIB", "broadhopAlarmErrorNumber"),
        ("BROADHOP-MIB", "broadhopAlarmErrorText"),
        ("BROADHOP-MIB", "broadhopAlarmDateAndTime"),
        ("BROADHOP-MIB", "broadhopAlarmProbableCause"),
        ("BROADHOP-MIB", "broadhopAlarmAdditionalInfo"))
)
if mibBuilder.loadTexts:
    broadhopWarningAlarm.setStatus(
        "deprecated"
    )

broadhopIndeterminateAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 26878, 100, 1, 2, 0, 5)
)
broadhopIndeterminateAlarm.setObjects(
      *(("BROADHOP-MIB", "broadhopAlarmDeviceName"),
        ("BROADHOP-MIB", "broadhopAlarmErrorNumber"),
        ("BROADHOP-MIB", "broadhopAlarmErrorText"),
        ("BROADHOP-MIB", "broadhopAlarmDateAndTime"),
        ("BROADHOP-MIB", "broadhopAlarmProbableCause"),
        ("BROADHOP-MIB", "broadhopAlarmAdditionalInfo"))
)
if mibBuilder.loadTexts:
    broadhopIndeterminateAlarm.setStatus(
        "deprecated"
    )

broadhopNormalAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 26878, 100, 1, 2, 0, 6)
)
broadhopNormalAlarm.setObjects(
      *(("BROADHOP-MIB", "broadhopAlarmDeviceName"),
        ("BROADHOP-MIB", "broadhopAlarmErrorNumber"),
        ("BROADHOP-MIB", "broadhopAlarmErrorText"),
        ("BROADHOP-MIB", "broadhopAlarmDateAndTime"),
        ("BROADHOP-MIB", "broadhopAlarmProbableCause"),
        ("BROADHOP-MIB", "broadhopAlarmAdditionalInfo"))
)
if mibBuilder.loadTexts:
    broadhopNormalAlarm.setStatus(
        "deprecated"
    )

broadhopClearAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 26878, 100, 1, 2, 0, 7)
)
broadhopClearAlarm.setObjects(
      *(("BROADHOP-MIB", "broadhopAlarmDeviceName"),
        ("BROADHOP-MIB", "broadhopAlarmErrorNumber"),
        ("BROADHOP-MIB", "broadhopAlarmErrorText"),
        ("BROADHOP-MIB", "broadhopAlarmDateAndTime"),
        ("BROADHOP-MIB", "broadhopAlarmProbableCause"),
        ("BROADHOP-MIB", "broadhopAlarmAdditionalInfo"))
)
if mibBuilder.loadTexts:
    broadhopClearAlarm.setStatus(
        "deprecated"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BROADHOP-MIB",
    **{"broadhop": broadhop,
       "broadhopCommon": broadhopCommon,
       "broadhopCommonNotificationsGroup": broadhopCommonNotificationsGroup,
       "broadhopNotificationParameters": broadhopNotificationParameters,
       "broadhopAlarmDeviceName": broadhopAlarmDeviceName,
       "broadhopAlarmErrorNumber": broadhopAlarmErrorNumber,
       "broadhopAlarmErrorText": broadhopAlarmErrorText,
       "broadhopAlarmDateAndTime": broadhopAlarmDateAndTime,
       "broadhopAlarmProbableCause": broadhopAlarmProbableCause,
       "broadhopAlarmAdditionalInfo": broadhopAlarmAdditionalInfo,
       "broadhopComponentName": broadhopComponentName,
       "broadhopComponentTime": broadhopComponentTime,
       "broadhopComponentNotificationName": broadhopComponentNotificationName,
       "broadhopComponentAdditionalInfo": broadhopComponentAdditionalInfo,
       "broadhopNotificationPrefix": broadhopNotificationPrefix,
       "broadhopNotifications": broadhopNotifications,
       "broadhopCriticalAlarm": broadhopCriticalAlarm,
       "broadhopMajorAlarm": broadhopMajorAlarm,
       "broadhopMinorAlarm": broadhopMinorAlarm,
       "broadhopWarningAlarm": broadhopWarningAlarm,
       "broadhopIndeterminateAlarm": broadhopIndeterminateAlarm,
       "broadhopNormalAlarm": broadhopNormalAlarm,
       "broadhopClearAlarm": broadhopClearAlarm,
       "broadhopNotificationFacility": broadhopNotificationFacility,
       "broadhopNotificationSeverity": broadhopNotificationSeverity,
       "broadhopProducts": broadhopProducts}
)
