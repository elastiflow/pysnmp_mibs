# SNMP MIB module (BBRIGHT-ENTERPRISE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/bbright_45201/BBRIGHT-ENTERPRISE-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 09:42:06 2025
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

bbright = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 45201)
)
if mibBuilder.loadTexts:
    bbright.setRevisions(
        ("2017-09-19 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AlarmStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alarmOff", 1),
          ("alarmOn", 2),
          ("alarmDisabled", 3))
    )



class Criticity(TextualConvention, Integer32):
    status = "current"
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
        *(("noLog", 0),
          ("info", 1),
          ("warning", 2),
          ("critical", 3))
    )



class ChannelType(TextualConvention, Integer32):
    status = "current"
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
        *(("pip", 1),
          ("sd", 2),
          ("hd", 3),
          ("uhd", 4))
    )



# MIB Managed Objects in the order of their OIDs

_Product_ObjectIdentity = ObjectIdentity
product = _Product_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45201, 1)
)


class _LocalName_Type(DisplayString):
    """Custom type localName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_LocalName_Type.__name__ = "DisplayString"
_LocalName_Object = MibScalar
localName = _LocalName_Object(
    (1, 3, 6, 1, 4, 1, 45201, 1, 1),
    _LocalName_Type()
)
localName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localName.setStatus("current")


class _Name_Type(DisplayString):
    """Custom type name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Name_Type.__name__ = "DisplayString"
_Name_Object = MibScalar
name = _Name_Object(
    (1, 3, 6, 1, 4, 1, 45201, 1, 1),
    _Name_Type()
)
name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    name.setStatus("current")


class _Description_Type(DisplayString):
    """Custom type description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_Description_Type.__name__ = "DisplayString"
_Description_Object = MibScalar
description = _Description_Object(
    (1, 3, 6, 1, 4, 1, 45201, 1, 2),
    _Description_Type()
)
description.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    description.setStatus("current")


class _SerialNumber_Type(DisplayString):
    """Custom type serialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )
    fixed_length = 20


_SerialNumber_Type.__name__ = "DisplayString"
_SerialNumber_Object = MibScalar
serialNumber = _SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 45201, 1, 3),
    _SerialNumber_Type()
)
serialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialNumber.setStatus("current")


class _FirmwareVersion_Type(DisplayString):
    """Custom type firmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FirmwareVersion_Type.__name__ = "DisplayString"
_FirmwareVersion_Object = MibScalar
firmwareVersion = _FirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 45201, 1, 4),
    _FirmwareVersion_Type()
)
firmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareVersion.setStatus("current")


class _MibVersion_Type(DisplayString):
    """Custom type mibVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_MibVersion_Type.__name__ = "DisplayString"
_MibVersion_Object = MibScalar
mibVersion = _MibVersion_Object(
    (1, 3, 6, 1, 4, 1, 45201, 1, 5),
    _MibVersion_Type()
)
mibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibVersion.setStatus("current")
_Channels_ObjectIdentity = ObjectIdentity
channels = _Channels_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45201, 2)
)


class _ActiveChannels_Type(Unsigned32):
    """Custom type activeChannels based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ActiveChannels_Type.__name__ = "Unsigned32"
_ActiveChannels_Object = MibScalar
activeChannels = _ActiveChannels_Object(
    (1, 3, 6, 1, 4, 1, 45201, 2, 1),
    _ActiveChannels_Type()
)
activeChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeChannels.setStatus("current")
_ActiveChannelsState_Type = AlarmStatus
_ActiveChannelsState_Object = MibScalar
activeChannelsState = _ActiveChannelsState_Object(
    (1, 3, 6, 1, 4, 1, 45201, 2, 2),
    _ActiveChannelsState_Type()
)
activeChannelsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeChannelsState.setStatus("current")
_ActiveChannelTable_Object = MibTable
activeChannelTable = _ActiveChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 45201, 2, 3)
)
if mibBuilder.loadTexts:
    activeChannelTable.setStatus("current")
_ActiveChannelEntry_Object = MibTableRow
activeChannelEntry = _ActiveChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 45201, 2, 3, 1)
)
activeChannelEntry.setIndexNames(
    (0, "BBRIGHT-ENTERPRISE-MIB", "activeChannelId"),
)
if mibBuilder.loadTexts:
    activeChannelEntry.setStatus("current")


class _ActiveChannelId_Type(DisplayString):
    """Custom type activeChannelId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 200),
    )


_ActiveChannelId_Type.__name__ = "DisplayString"
_ActiveChannelId_Object = MibTableColumn
activeChannelId = _ActiveChannelId_Object(
    (1, 3, 6, 1, 4, 1, 45201, 2, 3, 1, 1),
    _ActiveChannelId_Type()
)
activeChannelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeChannelId.setStatus("current")


class _ActiveChannelName_Type(DisplayString):
    """Custom type activeChannelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 200),
    )


_ActiveChannelName_Type.__name__ = "DisplayString"
_ActiveChannelName_Object = MibTableColumn
activeChannelName = _ActiveChannelName_Object(
    (1, 3, 6, 1, 4, 1, 45201, 2, 3, 1, 2),
    _ActiveChannelName_Type()
)
activeChannelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeChannelName.setStatus("current")
_ActiveChannelType_Type = ChannelType
_ActiveChannelType_Object = MibTableColumn
activeChannelType = _ActiveChannelType_Object(
    (1, 3, 6, 1, 4, 1, 45201, 2, 3, 1, 3),
    _ActiveChannelType_Type()
)
activeChannelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeChannelType.setStatus("current")
_AlarmsLogs_ObjectIdentity = ObjectIdentity
alarmsLogs = _AlarmsLogs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45201, 2, 3, 1, 4)
)
_ActiveAlarmState_Type = Criticity
_ActiveAlarmState_Object = MibScalar
activeAlarmState = _ActiveAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 45201, 2, 3, 1, 4, 1),
    _ActiveAlarmState_Type()
)
activeAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeAlarmState.setStatus("current")
_Alarms_ObjectIdentity = ObjectIdentity
alarms = _Alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45201, 2, 3, 1, 4, 2)
)
if mibBuilder.loadTexts:
    alarms.setStatus("current")


class _ActiveAlarmCount_Type(Unsigned32):
    """Custom type activeAlarmCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ActiveAlarmCount_Type.__name__ = "Unsigned32"
_ActiveAlarmCount_Object = MibScalar
activeAlarmCount = _ActiveAlarmCount_Object(
    (1, 3, 6, 1, 4, 1, 45201, 2, 3, 1, 4, 2, 1),
    _ActiveAlarmCount_Type()
)
activeAlarmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeAlarmCount.setStatus("current")
_ActiveAlarmTable_Object = MibTable
activeAlarmTable = _ActiveAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 45201, 2, 3, 1, 4, 2, 2)
)
if mibBuilder.loadTexts:
    activeAlarmTable.setStatus("current")
_ActiveAlarmEntry_Object = MibTableRow
activeAlarmEntry = _ActiveAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 45201, 2, 3, 1, 4, 2, 2, 1)
)
activeAlarmEntry.setIndexNames(
    (0, "BBRIGHT-ENTERPRISE-MIB", "activeAlarmId"),
)
if mibBuilder.loadTexts:
    activeAlarmEntry.setStatus("current")
_ActiveAlarmId_Type = Unsigned32
_ActiveAlarmId_Object = MibTableColumn
activeAlarmId = _ActiveAlarmId_Object(
    (1, 3, 6, 1, 4, 1, 45201, 2, 3, 1, 4, 2, 2, 1, 1),
    _ActiveAlarmId_Type()
)
activeAlarmId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeAlarmId.setStatus("current")


class _ActiveAlarmName_Type(DisplayString):
    """Custom type activeAlarmName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 200),
    )


_ActiveAlarmName_Type.__name__ = "DisplayString"
_ActiveAlarmName_Object = MibTableColumn
activeAlarmName = _ActiveAlarmName_Object(
    (1, 3, 6, 1, 4, 1, 45201, 2, 3, 1, 4, 2, 2, 1, 2),
    _ActiveAlarmName_Type()
)
activeAlarmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeAlarmName.setStatus("current")
_ActiveAlarmStatus_Type = AlarmStatus
_ActiveAlarmStatus_Object = MibTableColumn
activeAlarmStatus = _ActiveAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 45201, 2, 3, 1, 4, 2, 2, 1, 3),
    _ActiveAlarmStatus_Type()
)
activeAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeAlarmStatus.setStatus("current")


class _ActiveAlarmTime_Type(DisplayString):
    """Custom type activeAlarmTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ActiveAlarmTime_Type.__name__ = "DisplayString"
_ActiveAlarmTime_Object = MibTableColumn
activeAlarmTime = _ActiveAlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 45201, 2, 3, 1, 4, 2, 2, 1, 4),
    _ActiveAlarmTime_Type()
)
activeAlarmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeAlarmTime.setStatus("current")
_ActiveAlarmCriticity_Type = Criticity
_ActiveAlarmCriticity_Object = MibTableColumn
activeAlarmCriticity = _ActiveAlarmCriticity_Object(
    (1, 3, 6, 1, 4, 1, 45201, 2, 3, 1, 4, 2, 2, 1, 5),
    _ActiveAlarmCriticity_Type()
)
activeAlarmCriticity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeAlarmCriticity.setStatus("current")


class _ActiveAlarmText_Type(DisplayString):
    """Custom type activeAlarmText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 200),
    )


_ActiveAlarmText_Type.__name__ = "DisplayString"
_ActiveAlarmText_Object = MibTableColumn
activeAlarmText = _ActiveAlarmText_Object(
    (1, 3, 6, 1, 4, 1, 45201, 2, 3, 1, 4, 2, 2, 1, 6),
    _ActiveAlarmText_Type()
)
activeAlarmText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeAlarmText.setStatus("current")
_Traps_ObjectIdentity = ObjectIdentity
traps = _Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45201, 2, 3, 1, 4, 3)
)
_TrapSequenceNumber_Type = Unsigned32
_TrapSequenceNumber_Object = MibScalar
trapSequenceNumber = _TrapSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 45201, 2, 3, 1, 4, 3, 1, 1),
    _TrapSequenceNumber_Type()
)
trapSequenceNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapSequenceNumber.setStatus("current")
_TrapAlarmId_Type = Unsigned32
_TrapAlarmId_Object = MibScalar
trapAlarmId = _TrapAlarmId_Object(
    (1, 3, 6, 1, 4, 1, 45201, 2, 3, 1, 4, 3, 1, 2),
    _TrapAlarmId_Type()
)
trapAlarmId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapAlarmId.setStatus("current")


class _TrapChannelId_Type(DisplayString):
    """Custom type trapChannelId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 200),
    )


_TrapChannelId_Type.__name__ = "DisplayString"
_TrapChannelId_Object = MibScalar
trapChannelId = _TrapChannelId_Object(
    (1, 3, 6, 1, 4, 1, 45201, 2, 3, 1, 4, 3, 1, 3),
    _TrapChannelId_Type()
)
trapChannelId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapChannelId.setStatus("current")


class _TrapAlarmName_Type(DisplayString):
    """Custom type trapAlarmName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 200),
    )


_TrapAlarmName_Type.__name__ = "DisplayString"
_TrapAlarmName_Object = MibScalar
trapAlarmName = _TrapAlarmName_Object(
    (1, 3, 6, 1, 4, 1, 45201, 2, 3, 1, 4, 3, 1, 4),
    _TrapAlarmName_Type()
)
trapAlarmName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapAlarmName.setStatus("current")
_TrapAlarmStatus_Type = AlarmStatus
_TrapAlarmStatus_Object = MibScalar
trapAlarmStatus = _TrapAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 45201, 2, 3, 1, 4, 3, 1, 5),
    _TrapAlarmStatus_Type()
)
trapAlarmStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapAlarmStatus.setStatus("current")


class _TrapAlarmTime_Type(DisplayString):
    """Custom type trapAlarmTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_TrapAlarmTime_Type.__name__ = "DisplayString"
_TrapAlarmTime_Object = MibScalar
trapAlarmTime = _TrapAlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 45201, 2, 3, 1, 4, 3, 1, 6),
    _TrapAlarmTime_Type()
)
trapAlarmTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapAlarmTime.setStatus("current")
_TrapAlarmCriticity_Type = Criticity
_TrapAlarmCriticity_Object = MibScalar
trapAlarmCriticity = _TrapAlarmCriticity_Object(
    (1, 3, 6, 1, 4, 1, 45201, 2, 3, 1, 4, 3, 1, 7),
    _TrapAlarmCriticity_Type()
)
trapAlarmCriticity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapAlarmCriticity.setStatus("current")


class _TrapAlarmText_Type(DisplayString):
    """Custom type trapAlarmText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 200),
    )


_TrapAlarmText_Type.__name__ = "DisplayString"
_TrapAlarmText_Object = MibScalar
trapAlarmText = _TrapAlarmText_Object(
    (1, 3, 6, 1, 4, 1, 45201, 2, 3, 1, 4, 3, 1, 8),
    _TrapAlarmText_Type()
)
trapAlarmText.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapAlarmText.setStatus("current")
_TrapAlarmCounter_Type = Unsigned32
_TrapAlarmCounter_Object = MibScalar
trapAlarmCounter = _TrapAlarmCounter_Object(
    (1, 3, 6, 1, 4, 1, 45201, 2, 3, 1, 4, 3, 1, 9),
    _TrapAlarmCounter_Type()
)
trapAlarmCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapAlarmCounter.setStatus("current")

# Managed Objects groups


# Notification objects

alarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 45201, 2, 3, 1, 4, 3, 1)
)
alarmTrap.setObjects(
      *(("BBRIGHT-ENTERPRISE-MIB", "trapSequenceNumber"),
        ("BBRIGHT-ENTERPRISE-MIB", "trapChannelId"),
        ("BBRIGHT-ENTERPRISE-MIB", "trapAlarmId"),
        ("BBRIGHT-ENTERPRISE-MIB", "trapAlarmName"),
        ("BBRIGHT-ENTERPRISE-MIB", "trapAlarmStatus"),
        ("BBRIGHT-ENTERPRISE-MIB", "trapAlarmTime"),
        ("BBRIGHT-ENTERPRISE-MIB", "trapAlarmCriticity"),
        ("BBRIGHT-ENTERPRISE-MIB", "trapAlarmText"),
        ("BBRIGHT-ENTERPRISE-MIB", "trapAlarmCounter"))
)
if mibBuilder.loadTexts:
    alarmTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BBRIGHT-ENTERPRISE-MIB",
    **{"AlarmStatus": AlarmStatus,
       "Criticity": Criticity,
       "ChannelType": ChannelType,
       "bbright": bbright,
       "product": product,
       "localName": localName,
       "name": name,
       "description": description,
       "serialNumber": serialNumber,
       "firmwareVersion": firmwareVersion,
       "mibVersion": mibVersion,
       "channels": channels,
       "activeChannels": activeChannels,
       "activeChannelsState": activeChannelsState,
       "activeChannelTable": activeChannelTable,
       "activeChannelEntry": activeChannelEntry,
       "activeChannelId": activeChannelId,
       "activeChannelName": activeChannelName,
       "activeChannelType": activeChannelType,
       "alarmsLogs": alarmsLogs,
       "activeAlarmState": activeAlarmState,
       "alarms": alarms,
       "activeAlarmCount": activeAlarmCount,
       "activeAlarmTable": activeAlarmTable,
       "activeAlarmEntry": activeAlarmEntry,
       "activeAlarmId": activeAlarmId,
       "activeAlarmName": activeAlarmName,
       "activeAlarmStatus": activeAlarmStatus,
       "activeAlarmTime": activeAlarmTime,
       "activeAlarmCriticity": activeAlarmCriticity,
       "activeAlarmText": activeAlarmText,
       "traps": traps,
       "alarmTrap": alarmTrap,
       "trapSequenceNumber": trapSequenceNumber,
       "trapAlarmId": trapAlarmId,
       "trapChannelId": trapChannelId,
       "trapAlarmName": trapAlarmName,
       "trapAlarmStatus": trapAlarmStatus,
       "trapAlarmTime": trapAlarmTime,
       "trapAlarmCriticity": trapAlarmCriticity,
       "trapAlarmText": trapAlarmText,
       "trapAlarmCounter": trapAlarmCounter}
)
