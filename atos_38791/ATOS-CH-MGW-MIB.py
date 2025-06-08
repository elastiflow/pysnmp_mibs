# SNMP MIB module (ATOS-CH-MGW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/atos_38791/ATOS-CH-MGW-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 09:39:53 2025
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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

mgwMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 38791, 1, 5, 1)
)
if mibBuilder.loadTexts:
    mgwMIB.setRevisions(
        ("2000-01-01 01:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class MgwAlarmKey(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("influxDbConnectionLost", 1),
          ("brokerConnectionLost", 2),
          ("alarm3", 3),
          ("alarm4", 4),
          ("alarm5", 5))
    )



class MgwAlarmSeveriiity(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("minor", 4),
          ("major", 5),
          ("critical", 6))
    )



class MgwTimeslotState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bookedTimeslot", 0),
          ("timeslotInUse", 1),
          ("timeslotFree", 2))
    )



# MIB Managed Objects in the order of their OIDs

_Atos_ObjectIdentity = ObjectIdentity
atos = _Atos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38791)
)
if mibBuilder.loadTexts:
    atos.setStatus("current")
_Ch_ObjectIdentity = ObjectIdentity
ch = _Ch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38791, 1)
)
if mibBuilder.loadTexts:
    ch.setStatus("current")
_Mgw_ObjectIdentity = ObjectIdentity
mgw = _Mgw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38791, 1, 5)
)
if mibBuilder.loadTexts:
    mgw.setStatus("current")
_MgwAlarms_ObjectIdentity = ObjectIdentity
mgwAlarms = _MgwAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38791, 1, 5, 1, 1)
)
if mibBuilder.loadTexts:
    mgwAlarms.setStatus("current")
_MgwActiveAlarmsCount_Type = Integer32
_MgwActiveAlarmsCount_Object = MibScalar
mgwActiveAlarmsCount = _MgwActiveAlarmsCount_Object(
    (1, 3, 6, 1, 4, 1, 38791, 1, 5, 1, 1, 1),
    _MgwActiveAlarmsCount_Type()
)
mgwActiveAlarmsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwActiveAlarmsCount.setStatus("current")
_MgwAlarmsTable_Object = MibTable
mgwAlarmsTable = _MgwAlarmsTable_Object(
    (1, 3, 6, 1, 4, 1, 38791, 1, 5, 1, 1, 2)
)
if mibBuilder.loadTexts:
    mgwAlarmsTable.setStatus("current")
_MgwAlarmsEntry_Object = MibTableRow
mgwAlarmsEntry = _MgwAlarmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 38791, 1, 5, 1, 1, 2, 1)
)
mgwAlarmsEntry.setIndexNames(
    (0, "ATOS-CH-MGW-MIB", "mgwAlarmIdx"),
)
if mibBuilder.loadTexts:
    mgwAlarmsEntry.setStatus("current")
_MgwAlarmIdx_Type = Unsigned32
_MgwAlarmIdx_Object = MibTableColumn
mgwAlarmIdx = _MgwAlarmIdx_Object(
    (1, 3, 6, 1, 4, 1, 38791, 1, 5, 1, 1, 2, 1, 1),
    _MgwAlarmIdx_Type()
)
mgwAlarmIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgwAlarmIdx.setStatus("current")
_MgwAlarmKey_Type = MgwAlarmKey
_MgwAlarmKey_Object = MibTableColumn
mgwAlarmKey = _MgwAlarmKey_Object(
    (1, 3, 6, 1, 4, 1, 38791, 1, 5, 1, 1, 2, 1, 2),
    _MgwAlarmKey_Type()
)
mgwAlarmKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwAlarmKey.setStatus("current")
_MgwAlarmSeveriiity_Type = MgwAlarmSeveriiity
_MgwAlarmSeveriiity_Object = MibTableColumn
mgwAlarmSeveriiity = _MgwAlarmSeveriiity_Object(
    (1, 3, 6, 1, 4, 1, 38791, 1, 5, 1, 1, 2, 1, 3),
    _MgwAlarmSeveriiity_Type()
)
mgwAlarmSeveriiity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwAlarmSeveriiity.setStatus("current")
_MgwTimestamp_Type = DateAndTime
_MgwTimestamp_Object = MibTableColumn
mgwTimestamp = _MgwTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 38791, 1, 5, 1, 1, 2, 1, 4),
    _MgwTimestamp_Type()
)
mgwTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwTimestamp.setStatus("current")
_MgwAlarmIsCleared_Type = TruthValue
_MgwAlarmIsCleared_Object = MibTableColumn
mgwAlarmIsCleared = _MgwAlarmIsCleared_Object(
    (1, 3, 6, 1, 4, 1, 38791, 1, 5, 1, 1, 2, 1, 5),
    _MgwAlarmIsCleared_Type()
)
mgwAlarmIsCleared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwAlarmIsCleared.setStatus("current")
_MgwStateChangeCause_Type = DisplayString
_MgwStateChangeCause_Object = MibTableColumn
mgwStateChangeCause = _MgwStateChangeCause_Object(
    (1, 3, 6, 1, 4, 1, 38791, 1, 5, 1, 1, 2, 1, 6),
    _MgwStateChangeCause_Type()
)
mgwStateChangeCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwStateChangeCause.setStatus("current")
_MgwValue_Type = DisplayString
_MgwValue_Object = MibTableColumn
mgwValue = _MgwValue_Object(
    (1, 3, 6, 1, 4, 1, 38791, 1, 5, 1, 1, 2, 1, 7),
    _MgwValue_Type()
)
mgwValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwValue.setStatus("current")
_MgwValueThreshold_Type = DisplayString
_MgwValueThreshold_Object = MibTableColumn
mgwValueThreshold = _MgwValueThreshold_Object(
    (1, 3, 6, 1, 4, 1, 38791, 1, 5, 1, 1, 2, 1, 8),
    _MgwValueThreshold_Type()
)
mgwValueThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwValueThreshold.setStatus("current")
_MgwValueDescription_Type = DisplayString
_MgwValueDescription_Object = MibTableColumn
mgwValueDescription = _MgwValueDescription_Object(
    (1, 3, 6, 1, 4, 1, 38791, 1, 5, 1, 1, 2, 1, 9),
    _MgwValueDescription_Type()
)
mgwValueDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwValueDescription.setStatus("current")
_MgwScalars_ObjectIdentity = ObjectIdentity
mgwScalars = _MgwScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38791, 1, 5, 1, 2)
)
if mibBuilder.loadTexts:
    mgwScalars.setStatus("current")
_MgwMibRevisionTimestamp_Type = DateAndTime
_MgwMibRevisionTimestamp_Object = MibScalar
mgwMibRevisionTimestamp = _MgwMibRevisionTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 38791, 1, 5, 1, 2, 1),
    _MgwMibRevisionTimestamp_Type()
)
mgwMibRevisionTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwMibRevisionTimestamp.setStatus("current")
_MgwResourcesTimeslotStatusCard1Timeslot5_Type = MgwTimeslotState
_MgwResourcesTimeslotStatusCard1Timeslot5_Object = MibScalar
mgwResourcesTimeslotStatusCard1Timeslot5 = _MgwResourcesTimeslotStatusCard1Timeslot5_Object(
    (1, 3, 6, 1, 4, 1, 38791, 1, 5, 1, 2, 2),
    _MgwResourcesTimeslotStatusCard1Timeslot5_Type()
)
mgwResourcesTimeslotStatusCard1Timeslot5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwResourcesTimeslotStatusCard1Timeslot5.setStatus("current")
_MgwSessionsCount_Type = Integer32
_MgwSessionsCount_Object = MibScalar
mgwSessionsCount = _MgwSessionsCount_Object(
    (1, 3, 6, 1, 4, 1, 38791, 1, 5, 1, 2, 3),
    _MgwSessionsCount_Type()
)
mgwSessionsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwSessionsCount.setStatus("current")
_MgwResourcesPcmAdd_Type = Integer32
_MgwResourcesPcmAdd_Object = MibScalar
mgwResourcesPcmAdd = _MgwResourcesPcmAdd_Object(
    (1, 3, 6, 1, 4, 1, 38791, 1, 5, 1, 2, 4),
    _MgwResourcesPcmAdd_Type()
)
mgwResourcesPcmAdd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwResourcesPcmAdd.setStatus("current")
_MgwSessionsStateDuration_Type = TimeTicks
_MgwSessionsStateDuration_Object = MibScalar
mgwSessionsStateDuration = _MgwSessionsStateDuration_Object(
    (1, 3, 6, 1, 4, 1, 38791, 1, 5, 1, 2, 5),
    _MgwSessionsStateDuration_Type()
)
mgwSessionsStateDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwSessionsStateDuration.setStatus("current")
_MgwResponsiveToWatchdog_Type = TruthValue
_MgwResponsiveToWatchdog_Object = MibScalar
mgwResponsiveToWatchdog = _MgwResponsiveToWatchdog_Object(
    (1, 3, 6, 1, 4, 1, 38791, 1, 5, 1, 2, 6),
    _MgwResponsiveToWatchdog_Type()
)
mgwResponsiveToWatchdog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwResponsiveToWatchdog.setStatus("current")
_MgwCardConfigurationId_Type = DisplayString
_MgwCardConfigurationId_Object = MibScalar
mgwCardConfigurationId = _MgwCardConfigurationId_Object(
    (1, 3, 6, 1, 4, 1, 38791, 1, 5, 1, 2, 7),
    _MgwCardConfigurationId_Type()
)
mgwCardConfigurationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwCardConfigurationId.setStatus("current")
_MgwSessionConnectionsCount_Type = Integer32
_MgwSessionConnectionsCount_Object = MibScalar
mgwSessionConnectionsCount = _MgwSessionConnectionsCount_Object(
    (1, 3, 6, 1, 4, 1, 38791, 1, 5, 1, 2, 8),
    _MgwSessionConnectionsCount_Type()
)
mgwSessionConnectionsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwSessionConnectionsCount.setStatus("current")
_MgwCardMappingPcm_Type = Counter32
_MgwCardMappingPcm_Object = MibScalar
mgwCardMappingPcm = _MgwCardMappingPcm_Object(
    (1, 3, 6, 1, 4, 1, 38791, 1, 5, 1, 2, 9),
    _MgwCardMappingPcm_Type()
)
mgwCardMappingPcm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwCardMappingPcm.setStatus("current")
_MgwAlarm_Type = DateAndTime
_MgwAlarm_Object = MibScalar
mgwAlarm = _MgwAlarm_Object(
    (1, 3, 6, 1, 4, 1, 38791, 1, 5, 1, 2, 10),
    _MgwAlarm_Type()
)
mgwAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwAlarm.setStatus("current")
_MgwLog_Type = DisplayString
_MgwLog_Object = MibScalar
mgwLog = _MgwLog_Object(
    (1, 3, 6, 1, 4, 1, 38791, 1, 5, 1, 2, 11),
    _MgwLog_Type()
)
mgwLog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwLog.setStatus("current")
_MgwMIBConformance_ObjectIdentity = ObjectIdentity
mgwMIBConformance = _MgwMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38791, 1, 5, 1, 100)
)
if mibBuilder.loadTexts:
    mgwMIBConformance.setStatus("current")

# Managed Objects groups

mgwObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 38791, 1, 5, 1, 100, 1)
)
mgwObjectGroup.setObjects(
      *(("ATOS-CH-MGW-MIB", "mgwMibRevisionTimestamp"),
        ("ATOS-CH-MGW-MIB", "mgwActiveAlarmsCount"),
        ("ATOS-CH-MGW-MIB", "mgwAlarmKey"),
        ("ATOS-CH-MGW-MIB", "mgwAlarmSeveriiity"),
        ("ATOS-CH-MGW-MIB", "mgwTimestamp"),
        ("ATOS-CH-MGW-MIB", "mgwAlarmIsCleared"),
        ("ATOS-CH-MGW-MIB", "mgwStateChangeCause"),
        ("ATOS-CH-MGW-MIB", "mgwValue"),
        ("ATOS-CH-MGW-MIB", "mgwValueThreshold"),
        ("ATOS-CH-MGW-MIB", "mgwValueDescription"),
        ("ATOS-CH-MGW-MIB", "mgwResourcesTimeslotStatusCard1Timeslot5"),
        ("ATOS-CH-MGW-MIB", "mgwSessionsCount"),
        ("ATOS-CH-MGW-MIB", "mgwResourcesPcmAdd"),
        ("ATOS-CH-MGW-MIB", "mgwSessionsStateDuration"),
        ("ATOS-CH-MGW-MIB", "mgwResponsiveToWatchdog"),
        ("ATOS-CH-MGW-MIB", "mgwCardConfigurationId"),
        ("ATOS-CH-MGW-MIB", "mgwSessionConnectionsCount"),
        ("ATOS-CH-MGW-MIB", "mgwCardMappingPcm"),
        ("ATOS-CH-MGW-MIB", "mgwAlarm"),
        ("ATOS-CH-MGW-MIB", "mgwLog"))
)
if mibBuilder.loadTexts:
    mgwObjectGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

mgwCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 38791, 1, 5, 1, 100, 2)
)
mgwCompliance.setObjects(
    ("ATOS-CH-MGW-MIB", "mgwObjectGroup")
)
if mibBuilder.loadTexts:
    mgwCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ATOS-CH-MGW-MIB",
    **{"MgwAlarmKey": MgwAlarmKey,
       "MgwAlarmSeveriiity": MgwAlarmSeveriiity,
       "MgwTimeslotState": MgwTimeslotState,
       "atos": atos,
       "ch": ch,
       "mgw": mgw,
       "mgwMIB": mgwMIB,
       "mgwAlarms": mgwAlarms,
       "mgwActiveAlarmsCount": mgwActiveAlarmsCount,
       "mgwAlarmsTable": mgwAlarmsTable,
       "mgwAlarmsEntry": mgwAlarmsEntry,
       "mgwAlarmIdx": mgwAlarmIdx,
       "mgwAlarmKey": mgwAlarmKey,
       "mgwAlarmSeveriiity": mgwAlarmSeveriiity,
       "mgwTimestamp": mgwTimestamp,
       "mgwAlarmIsCleared": mgwAlarmIsCleared,
       "mgwStateChangeCause": mgwStateChangeCause,
       "mgwValue": mgwValue,
       "mgwValueThreshold": mgwValueThreshold,
       "mgwValueDescription": mgwValueDescription,
       "mgwScalars": mgwScalars,
       "mgwMibRevisionTimestamp": mgwMibRevisionTimestamp,
       "mgwResourcesTimeslotStatusCard1Timeslot5": mgwResourcesTimeslotStatusCard1Timeslot5,
       "mgwSessionsCount": mgwSessionsCount,
       "mgwResourcesPcmAdd": mgwResourcesPcmAdd,
       "mgwSessionsStateDuration": mgwSessionsStateDuration,
       "mgwResponsiveToWatchdog": mgwResponsiveToWatchdog,
       "mgwCardConfigurationId": mgwCardConfigurationId,
       "mgwSessionConnectionsCount": mgwSessionConnectionsCount,
       "mgwCardMappingPcm": mgwCardMappingPcm,
       "mgwAlarm": mgwAlarm,
       "mgwLog": mgwLog,
       "mgwMIBConformance": mgwMIBConformance,
       "mgwObjectGroup": mgwObjectGroup,
       "mgwCompliance": mgwCompliance}
)
