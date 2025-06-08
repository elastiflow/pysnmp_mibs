# SNMP MIB module (INVEATECH-ADS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/flowmon_39499/INVEATECH-ADS-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 23:03:01 2025
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

inveatechAdsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 39499, 39079, 1)
)
if mibBuilder.loadTexts:
    inveatechAdsMIB.setRevisions(
        ("2013-04-02 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Inveatech_ObjectIdentity = ObjectIdentity
inveatech = _Inveatech_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39499)
)
_Ads_ObjectIdentity = ObjectIdentity
ads = _Ads_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39499, 39079)
)
_Notification_ObjectIdentity = ObjectIdentity
notification = _Notification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39499, 39079, 2)
)
_Datatypes_ObjectIdentity = ObjectIdentity
datatypes = _Datatypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39499, 39079, 3)
)
_Event_ObjectIdentity = ObjectIdentity
event = _Event_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39499, 39079, 3, 1)
)


class _Code_Type(DisplayString):
    """Custom type code based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Code_Type.__name__ = "DisplayString"
_Code_Object = MibScalar
code = _Code_Object(
    (1, 3, 6, 1, 4, 1, 39499, 39079, 3, 1, 1),
    _Code_Type()
)
code.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    code.setStatus("current")


class _Detail_Type(DisplayString):
    """Custom type detail based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4096),
    )


_Detail_Type.__name__ = "DisplayString"
_Detail_Object = MibScalar
detail = _Detail_Object(
    (1, 3, 6, 1, 4, 1, 39499, 39079, 3, 1, 2),
    _Detail_Type()
)
detail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    detail.setStatus("current")


class _EventTimeStamp_Type(DisplayString):
    """Custom type eventTimeStamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EventTimeStamp_Type.__name__ = "DisplayString"
_EventTimeStamp_Object = MibScalar
eventTimeStamp = _EventTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 39499, 39079, 3, 1, 3),
    _EventTimeStamp_Type()
)
eventTimeStamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventTimeStamp.setStatus("current")


class _Source_Type(DisplayString):
    """Custom type source based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_Source_Type.__name__ = "DisplayString"
_Source_Object = MibScalar
source = _Source_Object(
    (1, 3, 6, 1, 4, 1, 39499, 39079, 3, 1, 4),
    _Source_Type()
)
source.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    source.setStatus("current")


class _Priority_Type(Integer32):
    """Custom type priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Priority_Type.__name__ = "Integer32"
_Priority_Object = MibScalar
priority = _Priority_Object(
    (1, 3, 6, 1, 4, 1, 39499, 39079, 3, 1, 5),
    _Priority_Type()
)
priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    priority.setStatus("current")


class _Targets_Type(DisplayString):
    """Custom type targets based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 450),
    )


_Targets_Type.__name__ = "DisplayString"
_Targets_Object = MibScalar
targets = _Targets_Object(
    (1, 3, 6, 1, 4, 1, 39499, 39079, 3, 1, 7),
    _Targets_Type()
)
targets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    targets.setStatus("current")
_EventID_Type = Integer32
_EventID_Object = MibScalar
eventID = _EventID_Object(
    (1, 3, 6, 1, 4, 1, 39499, 39079, 3, 1, 8),
    _EventID_Type()
)
eventID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventID.setStatus("current")
_Batch_ObjectIdentity = ObjectIdentity
batch = _Batch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39499, 39079, 3, 2)
)


class _SourceID_Type(Integer32):
    """Custom type sourceID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_SourceID_Type.__name__ = "Integer32"
_SourceID_Object = MibScalar
sourceID = _SourceID_Object(
    (1, 3, 6, 1, 4, 1, 39499, 39079, 3, 2, 1),
    _SourceID_Type()
)
sourceID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sourceID.setStatus("current")


class _SourceName_Type(DisplayString):
    """Custom type sourceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SourceName_Type.__name__ = "DisplayString"
_SourceName_Object = MibScalar
sourceName = _SourceName_Object(
    (1, 3, 6, 1, 4, 1, 39499, 39079, 3, 2, 2),
    _SourceName_Type()
)
sourceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sourceName.setStatus("current")


class _Flowcount_Type(Integer32):
    """Custom type flowcount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Flowcount_Type.__name__ = "Integer32"
_Flowcount_Object = MibScalar
flowcount = _Flowcount_Object(
    (1, 3, 6, 1, 4, 1, 39499, 39079, 3, 2, 3),
    _Flowcount_Type()
)
flowcount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flowcount.setStatus("current")
if mibBuilder.loadTexts:
    flowcount.setUnits("Flows")


class _ProcessingTime_Type(Integer32):
    """Custom type processingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_ProcessingTime_Type.__name__ = "Integer32"
_ProcessingTime_Object = MibScalar
processingTime = _ProcessingTime_Object(
    (1, 3, 6, 1, 4, 1, 39499, 39079, 3, 2, 4),
    _ProcessingTime_Type()
)
processingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    processingTime.setStatus("current")
if mibBuilder.loadTexts:
    processingTime.setUnits("seconds")


class _StartTime_Type(DisplayString):
    """Custom type startTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_StartTime_Type.__name__ = "DisplayString"
_StartTime_Object = MibScalar
startTime = _StartTime_Object(
    (1, 3, 6, 1, 4, 1, 39499, 39079, 3, 2, 5),
    _StartTime_Type()
)
startTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    startTime.setStatus("current")

# Managed Objects groups


# Notification objects

eventNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 39499, 39079, 2, 1)
)
eventNotif.setObjects(
      *(("INVEATECH-ADS-MIB", "code"),
        ("INVEATECH-ADS-MIB", "detail"),
        ("INVEATECH-ADS-MIB", "eventTimeStamp"),
        ("INVEATECH-ADS-MIB", "source"),
        ("INVEATECH-ADS-MIB", "priority"),
        ("INVEATECH-ADS-MIB", "targets"),
        ("INVEATECH-ADS-MIB", "eventID"))
)
if mibBuilder.loadTexts:
    eventNotif.setStatus(
        "current"
    )

batchNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 39499, 39079, 2, 2)
)
batchNotif.setObjects(
      *(("INVEATECH-ADS-MIB", "sourceID"),
        ("INVEATECH-ADS-MIB", "sourceName"),
        ("INVEATECH-ADS-MIB", "flowcount"),
        ("INVEATECH-ADS-MIB", "startTime"))
)
if mibBuilder.loadTexts:
    batchNotif.setStatus(
        "current"
    )

batchTimeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 39499, 39079, 2, 3)
)
batchTimeNotif.setObjects(
      *(("INVEATECH-ADS-MIB", "sourceID"),
        ("INVEATECH-ADS-MIB", "sourceName"),
        ("INVEATECH-ADS-MIB", "processingTime"),
        ("INVEATECH-ADS-MIB", "startTime"))
)
if mibBuilder.loadTexts:
    batchTimeNotif.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INVEATECH-ADS-MIB",
    **{"inveatech": inveatech,
       "ads": ads,
       "inveatechAdsMIB": inveatechAdsMIB,
       "notification": notification,
       "eventNotif": eventNotif,
       "batchNotif": batchNotif,
       "batchTimeNotif": batchTimeNotif,
       "datatypes": datatypes,
       "event": event,
       "code": code,
       "detail": detail,
       "eventTimeStamp": eventTimeStamp,
       "source": source,
       "priority": priority,
       "targets": targets,
       "eventID": eventID,
       "batch": batch,
       "sourceID": sourceID,
       "sourceName": sourceName,
       "flowcount": flowcount,
       "processingTime": processingTime,
       "startTime": startTime}
)
