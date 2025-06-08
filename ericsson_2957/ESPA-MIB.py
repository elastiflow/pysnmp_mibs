# SNMP MIB module (ESPA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ericsson_2957/ESPA-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 16:13:12 2025
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ericsson_ObjectIdentity = ObjectIdentity
ericsson = _Ericsson_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2957)
)
_Espa_ObjectIdentity = ObjectIdentity
espa = _Espa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2957, 8757)
)
_AlarmNotificationProfile_ObjectIdentity = ObjectIdentity
alarmNotificationProfile = _AlarmNotificationProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2957, 8757, 1)
)
_ObjectOfReference_Type = OctetString
_ObjectOfReference_Object = MibScalar
objectOfReference = _ObjectOfReference_Object(
    (1, 3, 6, 1, 4, 1, 2957, 8757, 2),
    _ObjectOfReference_Type()
)
objectOfReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    objectOfReference.setStatus("current")
_EventTime_Type = Integer32
_EventTime_Object = MibScalar
eventTime = _EventTime_Object(
    (1, 3, 6, 1, 4, 1, 2957, 8757, 3),
    _EventTime_Type()
)
eventTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventTime.setStatus("current")
_EventType_Type = OctetString
_EventType_Object = MibScalar
eventType = _EventType_Object(
    (1, 3, 6, 1, 4, 1, 2957, 8757, 4),
    _EventType_Type()
)
eventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventType.setStatus("current")
_PerceivedSeverity_Type = OctetString
_PerceivedSeverity_Object = MibScalar
perceivedSeverity = _PerceivedSeverity_Object(
    (1, 3, 6, 1, 4, 1, 2957, 8757, 5),
    _PerceivedSeverity_Type()
)
perceivedSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perceivedSeverity.setStatus("current")
_ThresholdInformation_Type = OctetString
_ThresholdInformation_Object = MibScalar
thresholdInformation = _ThresholdInformation_Object(
    (1, 3, 6, 1, 4, 1, 2957, 8757, 6),
    _ThresholdInformation_Type()
)
thresholdInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thresholdInformation.setStatus("current")
_Description_Type = OctetString
_Description_Object = MibScalar
description = _Description_Object(
    (1, 3, 6, 1, 4, 1, 2957, 8757, 7),
    _Description_Type()
)
description.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    description.setStatus("current")

# Managed Objects groups


# Notification objects

alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2957, 8757, 1, 1)
)
alarm.setObjects(
      *(("ESPA-MIB", "ObjectOfReference"),
        ("ESPA-MIB", "EventTime"),
        ("ESPA-MIB", "EventType"),
        ("ESPA-MIB", "PerceivedSeverity"),
        ("ESPA-MIB", "ThresholdInformation"),
        ("ESPA-MIB", "Description"))
)
if mibBuilder.loadTexts:
    alarm.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ESPA-MIB",
    **{"ericsson": ericsson,
       "espa": espa,
       "alarmNotificationProfile": alarmNotificationProfile,
       "alarm": alarm,
       "objectOfReference": objectOfReference,
       "eventTime": eventTime,
       "eventType": eventType,
       "perceivedSeverity": perceivedSeverity,
       "thresholdInformation": thresholdInformation,
       "description": description}
)
