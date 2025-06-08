# SNMP MIB module (GenGET-LTE-PM-ALARM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/gencore_32601/GenGET-LTE-PM-ALARM-MI.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 23:08:41 2025
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

genesis = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 32601)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_GenGET_ObjectIdentity = ObjectIdentity
GenGET = _GenGET_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32601, 1)
)
_LTE_ObjectIdentity = ObjectIdentity
LTE = _LTE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32601, 1, 2)
)
_Alarm_ObjectIdentity = ObjectIdentity
Alarm = _Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32601, 1, 2, 3)
)
_PmAlarmMIB_ObjectIdentity = ObjectIdentity
pmAlarmMIB = _PmAlarmMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32601, 1, 2, 3, 1)
)
_PmAlarmMIBV2_ObjectIdentity = ObjectIdentity
pmAlarmMIBV2 = _PmAlarmMIBV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32601, 1, 2, 3, 1, 0)
)
_PmAlarmObjects_ObjectIdentity = ObjectIdentity
pmAlarmObjects = _PmAlarmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32601, 1, 2, 3, 1, 1)
)
_PmAlarmTableObjects_ObjectIdentity = ObjectIdentity
pmAlarmTableObjects = _PmAlarmTableObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32601, 1, 2, 3, 1, 1, 1)
)
_PmAlarmTable_Object = MibTable
pmAlarmTable = _PmAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 32601, 1, 2, 3, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    pmAlarmTable.setStatus("mandatory")
_PmAlarmTableEntry_Object = MibTableRow
pmAlarmTableEntry = _PmAlarmTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 32601, 1, 2, 3, 1, 1, 1, 1, 1)
)
pmAlarmTableEntry.setIndexNames(
    (0, "GenGET-LTE-PM-ALARM-MIB", "pmalAlarmId"),
)
if mibBuilder.loadTexts:
    pmAlarmTableEntry.setStatus("mandatory")
_PmalAlarmId_Type = Integer32
_PmalAlarmId_Object = MibTableColumn
pmalAlarmId = _PmalAlarmId_Object(
    (1, 3, 6, 1, 4, 1, 32601, 1, 2, 3, 1, 1, 1, 1, 1, 1),
    _PmalAlarmId_Type()
)
pmalAlarmId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmalAlarmId.setStatus("mandatory")
_PmalAlarmSpecificProblem_Type = DisplayString
_PmalAlarmSpecificProblem_Object = MibTableColumn
pmalAlarmSpecificProblem = _PmalAlarmSpecificProblem_Object(
    (1, 3, 6, 1, 4, 1, 32601, 1, 2, 3, 1, 1, 1, 1, 1, 2),
    _PmalAlarmSpecificProblem_Type()
)
pmalAlarmSpecificProblem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmalAlarmSpecificProblem.setStatus("mandatory")
_PmalAlarmProbableCause_Type = DisplayString
_PmalAlarmProbableCause_Object = MibTableColumn
pmalAlarmProbableCause = _PmalAlarmProbableCause_Object(
    (1, 3, 6, 1, 4, 1, 32601, 1, 2, 3, 1, 1, 1, 1, 1, 3),
    _PmalAlarmProbableCause_Type()
)
pmalAlarmProbableCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmalAlarmProbableCause.setStatus("mandatory")
_PmalAlarmDateAndTime_Type = DisplayString
_PmalAlarmDateAndTime_Object = MibTableColumn
pmalAlarmDateAndTime = _PmalAlarmDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 32601, 1, 2, 3, 1, 1, 1, 1, 1, 4),
    _PmalAlarmDateAndTime_Type()
)
pmalAlarmDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmalAlarmDateAndTime.setStatus("mandatory")
_PmalAlarmPerceivedSeverity_Type = DisplayString
_PmalAlarmPerceivedSeverity_Object = MibTableColumn
pmalAlarmPerceivedSeverity = _PmalAlarmPerceivedSeverity_Object(
    (1, 3, 6, 1, 4, 1, 32601, 1, 2, 3, 1, 1, 1, 1, 1, 5),
    _PmalAlarmPerceivedSeverity_Type()
)
pmalAlarmPerceivedSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmalAlarmPerceivedSeverity.setStatus("mandatory")
_PmalAlarmAdditionalText_Type = DisplayString
_PmalAlarmAdditionalText_Object = MibTableColumn
pmalAlarmAdditionalText = _PmalAlarmAdditionalText_Object(
    (1, 3, 6, 1, 4, 1, 32601, 1, 2, 3, 1, 1, 1, 1, 1, 6),
    _PmalAlarmAdditionalText_Type()
)
pmalAlarmAdditionalText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmalAlarmAdditionalText.setStatus("current")
_PmalAlarmEventType_Type = DisplayString
_PmalAlarmEventType_Object = MibTableColumn
pmalAlarmEventType = _PmalAlarmEventType_Object(
    (1, 3, 6, 1, 4, 1, 32601, 1, 2, 3, 1, 1, 1, 1, 1, 7),
    _PmalAlarmEventType_Type()
)
pmalAlarmEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmalAlarmEventType.setStatus("mandatory")
_PmalAlarmManagedResource_Type = DisplayString
_PmalAlarmManagedResource_Object = MibTableColumn
pmalAlarmManagedResource = _PmalAlarmManagedResource_Object(
    (1, 3, 6, 1, 4, 1, 32601, 1, 2, 3, 1, 1, 1, 1, 1, 8),
    _PmalAlarmManagedResource_Type()
)
pmalAlarmManagedResource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmalAlarmManagedResource.setStatus("mandatory")
_PmalAlarmManagedObject_Type = DisplayString
_PmalAlarmManagedObject_Object = MibTableColumn
pmalAlarmManagedObject = _PmalAlarmManagedObject_Object(
    (1, 3, 6, 1, 4, 1, 32601, 1, 2, 3, 1, 1, 1, 1, 1, 9),
    _PmalAlarmManagedObject_Type()
)
pmalAlarmManagedObject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmalAlarmManagedObject.setStatus("mandatory")

# Managed Objects groups


# Notification objects

pmAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 32601, 1, 2, 3, 1, 0, 1)
)
pmAlarm.setObjects(
      *(("GenGET-LTE-PM-ALARM-MIB", "pmalAlarmId"),
        ("GenGET-LTE-PM-ALARM-MIB", "pmalAlarmSpecificProblem"),
        ("GenGET-LTE-PM-ALARM-MIB", "pmalAlarmProbableCause"),
        ("GenGET-LTE-PM-ALARM-MIB", "pmalAlarmDateAndTime"),
        ("GenGET-LTE-PM-ALARM-MIB", "pmalAlarmPerceivedSeverity"),
        ("GenGET-LTE-PM-ALARM-MIB", "pmalAlarmAdditionalText"),
        ("GenGET-LTE-PM-ALARM-MIB", "pmalAlarmEventType"),
        ("GenGET-LTE-PM-ALARM-MIB", "pmalAlarmManagedResource"),
        ("GenGET-LTE-PM-ALARM-MIB", "pmalAlarmManagedObject"))
)
if mibBuilder.loadTexts:
    pmAlarm.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GenGET-LTE-PM-ALARM-MIB",
    **{"genesis": genesis,
       "GenGET": GenGET,
       "LTE": LTE,
       "Alarm": Alarm,
       "pmAlarmMIB": pmAlarmMIB,
       "pmAlarmMIBV2": pmAlarmMIBV2,
       "pmAlarm": pmAlarm,
       "pmAlarmObjects": pmAlarmObjects,
       "pmAlarmTableObjects": pmAlarmTableObjects,
       "pmAlarmTable": pmAlarmTable,
       "pmAlarmTableEntry": pmAlarmTableEntry,
       "pmalAlarmId": pmalAlarmId,
       "pmalAlarmSpecificProblem": pmalAlarmSpecificProblem,
       "pmalAlarmProbableCause": pmalAlarmProbableCause,
       "pmalAlarmDateAndTime": pmalAlarmDateAndTime,
       "pmalAlarmPerceivedSeverity": pmalAlarmPerceivedSeverity,
       "pmalAlarmAdditionalText": pmalAlarmAdditionalText,
       "pmalAlarmEventType": pmalAlarmEventType,
       "pmalAlarmManagedResource": pmalAlarmManagedResource,
       "pmalAlarmManagedObject": pmalAlarmManagedObject}
)
