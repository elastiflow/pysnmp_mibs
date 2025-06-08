# SNMP MIB module (NOKIA-SUBSCRIBER-MANAGEMENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_28458/NOKIA-SDL-MANAGEMENT-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 30 16:24:52 2025
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

(sysDescr,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysDescr")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

nokia = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 28458)
)
if mibBuilder.loadTexts:
    nokia.setRevisions(
        ("2016-05-03 14:10",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_System_ObjectIdentity = ObjectIdentity
system = _System_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 1)
)
_Snmp_ObjectIdentity = ObjectIdentity
snmp = _Snmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28458, 1)
)
_Subscribermanagement_ObjectIdentity = ObjectIdentity
subscribermanagement = _Subscribermanagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28458, 1, 45)
)
_Sdl_ObjectIdentity = ObjectIdentity
sdl = _Sdl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28458, 1, 45, 1)
)


class _SourceAddress_Type(OctetString):
    """Custom type sourceAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SourceAddress_Type.__name__ = "OctetString"
_SourceAddress_Object = MibScalar
sourceAddress = _SourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 45, 1, 1),
    _SourceAddress_Type()
)
sourceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sourceAddress.setStatus("current")
_AlarmCode_Type = Integer32
_AlarmCode_Object = MibScalar
alarmCode = _AlarmCode_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 45, 1, 2),
    _AlarmCode_Type()
)
alarmCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmCode.setStatus("current")


class _AlarmEventTime_Type(OctetString):
    """Custom type alarmEventTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AlarmEventTime_Type.__name__ = "OctetString"
_AlarmEventTime_Object = MibScalar
alarmEventTime = _AlarmEventTime_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 45, 1, 3),
    _AlarmEventTime_Type()
)
alarmEventTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmEventTime.setStatus("current")


class _AlarmDescription_Type(OctetString):
    """Custom type alarmDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AlarmDescription_Type.__name__ = "OctetString"
_AlarmDescription_Object = MibScalar
alarmDescription = _AlarmDescription_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 45, 1, 4),
    _AlarmDescription_Type()
)
alarmDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmDescription.setStatus("current")


class _AlarmSeverity_Type(OctetString):
    """Custom type alarmSeverity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AlarmSeverity_Type.__name__ = "OctetString"
_AlarmSeverity_Object = MibScalar
alarmSeverity = _AlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 45, 1, 5),
    _AlarmSeverity_Type()
)
alarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmSeverity.setStatus("current")


class _ManagedObject_Type(OctetString):
    """Custom type managedObject based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ManagedObject_Type.__name__ = "OctetString"
_ManagedObject_Object = MibScalar
managedObject = _ManagedObject_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 45, 1, 6),
    _ManagedObject_Type()
)
managedObject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    managedObject.setStatus("current")


class _Hostname_Type(OctetString):
    """Custom type hostname based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hostname_Type.__name__ = "OctetString"
_Hostname_Object = MibScalar
hostname = _Hostname_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 45, 1, 7),
    _Hostname_Type()
)
hostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostname.setStatus("current")


class _Locality_Type(OctetString):
    """Custom type locality based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Locality_Type.__name__ = "OctetString"
_Locality_Object = MibScalar
locality = _Locality_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 45, 1, 8),
    _Locality_Type()
)
locality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locality.setStatus("current")


class _PossibleReasons_Type(OctetString):
    """Custom type possibleReasons based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_PossibleReasons_Type.__name__ = "OctetString"
_PossibleReasons_Object = MibScalar
possibleReasons = _PossibleReasons_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 45, 1, 9),
    _PossibleReasons_Type()
)
possibleReasons.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    possibleReasons.setStatus("current")


class _RepairAction_Type(OctetString):
    """Custom type repairAction based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_RepairAction_Type.__name__ = "OctetString"
_RepairAction_Object = MibScalar
repairAction = _RepairAction_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 45, 1, 10),
    _RepairAction_Type()
)
repairAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    repairAction.setStatus("current")


class _AdditionalText_Type(OctetString):
    """Custom type additionalText based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_AdditionalText_Type.__name__ = "OctetString"
_AdditionalText_Object = MibScalar
additionalText = _AdditionalText_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 45, 1, 11),
    _AdditionalText_Type()
)
additionalText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    additionalText.setStatus("current")


class _AllParameters_Type(OctetString):
    """Custom type allParameters based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AllParameters_Type.__name__ = "OctetString"
_AllParameters_Object = MibScalar
allParameters = _AllParameters_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 45, 1, 12),
    _AllParameters_Type()
)
allParameters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    allParameters.setStatus("current")


class _AlarmUUID_Type(OctetString):
    """Custom type alarmUUID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 36),
    )


_AlarmUUID_Type.__name__ = "OctetString"
_AlarmUUID_Object = MibScalar
alarmUUID = _AlarmUUID_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 45, 1, 13),
    _AlarmUUID_Type()
)
alarmUUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmUUID.setStatus("current")


class _ClearState_Type(OctetString):
    """Custom type clearState based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ClearState_Type.__name__ = "OctetString"
_ClearState_Object = MibScalar
clearState = _ClearState_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 45, 1, 14),
    _ClearState_Type()
)
clearState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clearState.setStatus("current")

# Managed Objects groups


# Notification objects

sdlAlarmNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 28458, 1, 45, 1, 100)
)
sdlAlarmNotification.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("NOKIA-SUBSCRIBER-MANAGEMENT-MIB", "sourceAddress"),
        ("NOKIA-SUBSCRIBER-MANAGEMENT-MIB", "alarmCode"),
        ("NOKIA-SUBSCRIBER-MANAGEMENT-MIB", "alarmEventTime"),
        ("NOKIA-SUBSCRIBER-MANAGEMENT-MIB", "alarmDescription"),
        ("NOKIA-SUBSCRIBER-MANAGEMENT-MIB", "alarmSeverity"),
        ("NOKIA-SUBSCRIBER-MANAGEMENT-MIB", "managedObject"),
        ("NOKIA-SUBSCRIBER-MANAGEMENT-MIB", "hostname"),
        ("NOKIA-SUBSCRIBER-MANAGEMENT-MIB", "locality"),
        ("NOKIA-SUBSCRIBER-MANAGEMENT-MIB", "possibleReasons"),
        ("NOKIA-SUBSCRIBER-MANAGEMENT-MIB", "repairAction"),
        ("NOKIA-SUBSCRIBER-MANAGEMENT-MIB", "additionalText"),
        ("NOKIA-SUBSCRIBER-MANAGEMENT-MIB", "allParameters"),
        ("NOKIA-SUBSCRIBER-MANAGEMENT-MIB", "alarmUUID"))
)
if mibBuilder.loadTexts:
    sdlAlarmNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NOKIA-SUBSCRIBER-MANAGEMENT-MIB",
    **{"system": system,
       "nokia": nokia,
       "snmp": snmp,
       "subscribermanagement": subscribermanagement,
       "sdl": sdl,
       "sourceAddress": sourceAddress,
       "alarmCode": alarmCode,
       "alarmEventTime": alarmEventTime,
       "alarmDescription": alarmDescription,
       "alarmSeverity": alarmSeverity,
       "managedObject": managedObject,
       "hostname": hostname,
       "locality": locality,
       "possibleReasons": possibleReasons,
       "repairAction": repairAction,
       "additionalText": additionalText,
       "allParameters": allParameters,
       "alarmUUID": alarmUUID,
       "clearState": clearState,
       "sdlAlarmNotification": sdlAlarmNotification}
)
