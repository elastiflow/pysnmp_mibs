# SNMP MIB module (CENTILE-ALARM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/centile_29844/CENTILE-ALARM-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 10:32:22 2025
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

(centileMIB,) = mibBuilder.importSymbols(
    "CENTILE-MIB",
    "centileMIB")

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
 NotificationType,
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
    "NotificationType",
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

centileAlarmTrapMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 29844, 6)
)
if mibBuilder.loadTexts:
    centileAlarmTrapMIB.setRevisions(
        ("2011-04-19 16:21",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CentileAlarmObjects_ObjectIdentity = ObjectIdentity
centileAlarmObjects = _CentileAlarmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29844, 6, 1)
)
_CentileAlarmEvents_ObjectIdentity = ObjectIdentity
centileAlarmEvents = _CentileAlarmEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29844, 6, 2)
)
_CentileAlarmConf_ObjectIdentity = ObjectIdentity
centileAlarmConf = _CentileAlarmConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29844, 6, 3)
)
_CentileAlarmGroups_ObjectIdentity = ObjectIdentity
centileAlarmGroups = _CentileAlarmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29844, 6, 3, 1)
)
_CentileAlarmCompls_ObjectIdentity = ObjectIdentity
centileAlarmCompls = _CentileAlarmCompls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29844, 6, 3, 2)
)
_CentileAlarmLogTime_Type = OctetString
_CentileAlarmLogTime_Object = MibScalar
centileAlarmLogTime = _CentileAlarmLogTime_Object(
    (1, 3, 6, 1, 4, 1, 29844, 6, 5),
    _CentileAlarmLogTime_Type()
)
centileAlarmLogTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    centileAlarmLogTime.setStatus("current")
_CentileAlarmElapsedTime_Type = OctetString
_CentileAlarmElapsedTime_Object = MibScalar
centileAlarmElapsedTime = _CentileAlarmElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 29844, 6, 6),
    _CentileAlarmElapsedTime_Type()
)
centileAlarmElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    centileAlarmElapsedTime.setStatus("current")


class _CentileAlarmID_Type(Integer32):
    """Custom type centileAlarmID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_CentileAlarmID_Type.__name__ = "Integer32"
_CentileAlarmID_Object = MibScalar
centileAlarmID = _CentileAlarmID_Object(
    (1, 3, 6, 1, 4, 1, 29844, 6, 7),
    _CentileAlarmID_Type()
)
centileAlarmID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    centileAlarmID.setStatus("current")
if mibBuilder.loadTexts:
    centileAlarmID.setUnits("alarm ID")
_CentileAlarmSeverity_Type = OctetString
_CentileAlarmSeverity_Object = MibScalar
centileAlarmSeverity = _CentileAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 29844, 6, 8),
    _CentileAlarmSeverity_Type()
)
centileAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    centileAlarmSeverity.setStatus("current")
_CentileAlarmResource_Type = OctetString
_CentileAlarmResource_Object = MibScalar
centileAlarmResource = _CentileAlarmResource_Object(
    (1, 3, 6, 1, 4, 1, 29844, 6, 9),
    _CentileAlarmResource_Type()
)
centileAlarmResource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    centileAlarmResource.setStatus("current")
_CentileAlarmDescription_Type = OctetString
_CentileAlarmDescription_Object = MibScalar
centileAlarmDescription = _CentileAlarmDescription_Object(
    (1, 3, 6, 1, 4, 1, 29844, 6, 10),
    _CentileAlarmDescription_Type()
)
centileAlarmDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    centileAlarmDescription.setStatus("current")
_CentileAlarmCause_Type = OctetString
_CentileAlarmCause_Object = MibScalar
centileAlarmCause = _CentileAlarmCause_Object(
    (1, 3, 6, 1, 4, 1, 29844, 6, 11),
    _CentileAlarmCause_Type()
)
centileAlarmCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    centileAlarmCause.setStatus("current")
_CentileAlarmAction_Type = OctetString
_CentileAlarmAction_Object = MibScalar
centileAlarmAction = _CentileAlarmAction_Object(
    (1, 3, 6, 1, 4, 1, 29844, 6, 12),
    _CentileAlarmAction_Type()
)
centileAlarmAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    centileAlarmAction.setStatus("current")

# Managed Objects groups

centileAlarmBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 29844, 6, 3, 1, 1)
)
centileAlarmBasicGroup.setObjects(
      *(("CENTILE-ALARM-MIB", "centileAlarmLogTime"),
        ("CENTILE-ALARM-MIB", "centileAlarmElapsedTime"),
        ("CENTILE-ALARM-MIB", "centileAlarmID"),
        ("CENTILE-ALARM-MIB", "centileAlarmSeverity"),
        ("CENTILE-ALARM-MIB", "centileAlarmResource"),
        ("CENTILE-ALARM-MIB", "centileAlarmDescription"),
        ("CENTILE-ALARM-MIB", "centileAlarmCause"),
        ("CENTILE-ALARM-MIB", "centileAlarmAction"))
)
if mibBuilder.loadTexts:
    centileAlarmBasicGroup.setStatus("current")


# Notification objects

centileAlarmTrapTypeAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 29844, 6, 0, 20)
)
centileAlarmTrapTypeAlarm.setObjects(
      *(("CENTILE-ALARM-MIB", "centileAlarmLogTime"),
        ("CENTILE-ALARM-MIB", "centileAlarmElapsedTime"),
        ("CENTILE-ALARM-MIB", "centileAlarmID"),
        ("CENTILE-ALARM-MIB", "centileAlarmSeverity"),
        ("CENTILE-ALARM-MIB", "centileAlarmResource"),
        ("CENTILE-ALARM-MIB", "centileAlarmDescription"),
        ("CENTILE-ALARM-MIB", "centileAlarmCause"),
        ("CENTILE-ALARM-MIB", "centileAlarmAction"))
)
if mibBuilder.loadTexts:
    centileAlarmTrapTypeAlarm.setStatus(
        ""
    )

centileAlarmTrapNewAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 29844, 6, 4)
)
centileAlarmTrapNewAlarm.setObjects(
      *(("CENTILE-ALARM-MIB", "centileAlarmLogTime"),
        ("CENTILE-ALARM-MIB", "centileAlarmElapsedTime"),
        ("CENTILE-ALARM-MIB", "centileAlarmID"),
        ("CENTILE-ALARM-MIB", "centileAlarmSeverity"),
        ("CENTILE-ALARM-MIB", "centileAlarmResource"),
        ("CENTILE-ALARM-MIB", "centileAlarmDescription"),
        ("CENTILE-ALARM-MIB", "centileAlarmCause"),
        ("CENTILE-ALARM-MIB", "centileAlarmAction"))
)
if mibBuilder.loadTexts:
    centileAlarmTrapNewAlarm.setStatus(
        "current"
    )


# Notifications groups

centileAlarmBasicEvents = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 29844, 6, 3, 1, 2)
)
centileAlarmBasicEvents.setObjects(
    ("CENTILE-ALARM-MIB", "centileAlarmTrapNewAlarm")
)
if mibBuilder.loadTexts:
    centileAlarmBasicEvents.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CENTILE-ALARM-MIB",
    **{"centileAlarmTrapMIB": centileAlarmTrapMIB,
       "centileAlarmTrapTypeAlarm": centileAlarmTrapTypeAlarm,
       "centileAlarmObjects": centileAlarmObjects,
       "centileAlarmEvents": centileAlarmEvents,
       "centileAlarmConf": centileAlarmConf,
       "centileAlarmGroups": centileAlarmGroups,
       "centileAlarmBasicGroup": centileAlarmBasicGroup,
       "centileAlarmBasicEvents": centileAlarmBasicEvents,
       "centileAlarmCompls": centileAlarmCompls,
       "centileAlarmTrapNewAlarm": centileAlarmTrapNewAlarm,
       "centileAlarmLogTime": centileAlarmLogTime,
       "centileAlarmElapsedTime": centileAlarmElapsedTime,
       "centileAlarmID": centileAlarmID,
       "centileAlarmSeverity": centileAlarmSeverity,
       "centileAlarmResource": centileAlarmResource,
       "centileAlarmDescription": centileAlarmDescription,
       "centileAlarmCause": centileAlarmCause,
       "centileAlarmAction": centileAlarmAction}
)
