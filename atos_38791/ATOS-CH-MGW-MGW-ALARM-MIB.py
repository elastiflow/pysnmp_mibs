# SNMP MIB module (ATOS-CH-MGW-MGW-ALARM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/atos_38791/ATOS-CH-MGW-MGW-ALARM-MIB.mib
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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

mgwMgwAlarmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 38791, 1, 4, 1)
)
if mibBuilder.loadTexts:
    mgwMgwAlarmMIB.setRevisions(
        ("2017-03-15 12:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class MgwAlarmSeverity(TextualConvention, Integer32):
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



class MgwConnectionState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("nok", 2),
          ("idle", 3),
          ("unknown", 255))
    )



class MgwNullableBoolean(TextualConvention, Integer32):
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
        *(("null", 0),
          ("true", 1),
          ("false", 2))
    )



class MgwAlarmType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(48201,
              48301,
              48302)
        )
    )
    namedValues = NamedValues(
        *(("sproServiceIsNotRunning", 48201),
          ("sproDbIsNotConnected", 48301),
          ("sproDbReplicationIsNotRunning", 48302))
    )



# MIB Managed Objects in the order of their OIDs

_Atos_ObjectIdentity = ObjectIdentity
atos = _Atos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38791)
)
_Ch_ObjectIdentity = ObjectIdentity
ch = _Ch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38791, 1)
)
_Mgw_ObjectIdentity = ObjectIdentity
mgw = _Mgw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38791, 1, 4)
)
_MgwAlarms_ObjectIdentity = ObjectIdentity
mgwAlarms = _MgwAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38791, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    mgwAlarms.setStatus("current")
_MgwNrAlarms_Type = Unsigned32
_MgwNrAlarms_Object = MibScalar
mgwNrAlarms = _MgwNrAlarms_Object(
    (1, 3, 6, 1, 4, 1, 38791, 1, 4, 1, 1, 1),
    _MgwNrAlarms_Type()
)
mgwNrAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwNrAlarms.setStatus("current")
_MgwAlarmTable_Object = MibTable
mgwAlarmTable = _MgwAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 38791, 1, 4, 1, 1, 2)
)
if mibBuilder.loadTexts:
    mgwAlarmTable.setStatus("current")
_MgwAlarmEntry_Object = MibTableRow
mgwAlarmEntry = _MgwAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 38791, 1, 4, 1, 1, 2, 1)
)
mgwAlarmEntry.setIndexNames(
    (0, "ATOS-CH-MGW-MGW-ALARM-MIB", "mgwAlarmIdx"),
)
if mibBuilder.loadTexts:
    mgwAlarmEntry.setStatus("current")
_MgwAlarmIdx_Type = Unsigned32
_MgwAlarmIdx_Object = MibTableColumn
mgwAlarmIdx = _MgwAlarmIdx_Object(
    (1, 3, 6, 1, 4, 1, 38791, 1, 4, 1, 1, 2, 1, 1),
    _MgwAlarmIdx_Type()
)
mgwAlarmIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgwAlarmIdx.setStatus("current")
_MgwAlarmType_Type = MgwAlarmType
_MgwAlarmType_Object = MibTableColumn
mgwAlarmType = _MgwAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 38791, 1, 4, 1, 1, 2, 1, 2),
    _MgwAlarmType_Type()
)
mgwAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwAlarmType.setStatus("current")
_MgwAlarmSeverity_Type = MgwAlarmSeverity
_MgwAlarmSeverity_Object = MibTableColumn
mgwAlarmSeverity = _MgwAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 38791, 1, 4, 1, 1, 2, 1, 3),
    _MgwAlarmSeverity_Type()
)
mgwAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwAlarmSeverity.setStatus("current")
_MgwAlarmBeginDateTime_Type = DateAndTime
_MgwAlarmBeginDateTime_Object = MibTableColumn
mgwAlarmBeginDateTime = _MgwAlarmBeginDateTime_Object(
    (1, 3, 6, 1, 4, 1, 38791, 1, 4, 1, 1, 2, 1, 4),
    _MgwAlarmBeginDateTime_Type()
)
mgwAlarmBeginDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwAlarmBeginDateTime.setStatus("current")
_MgwAlarmIsFlapping_Type = TruthValue
_MgwAlarmIsFlapping_Object = MibTableColumn
mgwAlarmIsFlapping = _MgwAlarmIsFlapping_Object(
    (1, 3, 6, 1, 4, 1, 38791, 1, 4, 1, 1, 2, 1, 5),
    _MgwAlarmIsFlapping_Type()
)
mgwAlarmIsFlapping.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwAlarmIsFlapping.setStatus("current")
_MgwAlarmParam1_Type = DisplayString
_MgwAlarmParam1_Object = MibTableColumn
mgwAlarmParam1 = _MgwAlarmParam1_Object(
    (1, 3, 6, 1, 4, 1, 38791, 1, 4, 1, 1, 2, 1, 6),
    _MgwAlarmParam1_Type()
)
mgwAlarmParam1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwAlarmParam1.setStatus("current")
_MgwAlarmParam2_Type = DisplayString
_MgwAlarmParam2_Object = MibTableColumn
mgwAlarmParam2 = _MgwAlarmParam2_Object(
    (1, 3, 6, 1, 4, 1, 38791, 1, 4, 1, 1, 2, 1, 7),
    _MgwAlarmParam2_Type()
)
mgwAlarmParam2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwAlarmParam2.setStatus("current")
_MgwAlarmParam3_Type = DisplayString
_MgwAlarmParam3_Object = MibTableColumn
mgwAlarmParam3 = _MgwAlarmParam3_Object(
    (1, 3, 6, 1, 4, 1, 38791, 1, 4, 1, 1, 2, 1, 8),
    _MgwAlarmParam3_Type()
)
mgwAlarmParam3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwAlarmParam3.setStatus("current")
_MgwAlarmParam4_Type = DisplayString
_MgwAlarmParam4_Object = MibTableColumn
mgwAlarmParam4 = _MgwAlarmParam4_Object(
    (1, 3, 6, 1, 4, 1, 38791, 1, 4, 1, 1, 2, 1, 9),
    _MgwAlarmParam4_Type()
)
mgwAlarmParam4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwAlarmParam4.setStatus("current")
_MgwAlarmMIBConformance_ObjectIdentity = ObjectIdentity
mgwAlarmMIBConformance = _MgwAlarmMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38791, 1, 4, 1, 100)
)
if mibBuilder.loadTexts:
    mgwAlarmMIBConformance.setStatus("current")
_MgwAlarmsConformance_ObjectIdentity = ObjectIdentity
mgwAlarmsConformance = _MgwAlarmsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38791, 1, 4, 1, 100, 1)
)
if mibBuilder.loadTexts:
    mgwAlarmsConformance.setStatus("current")

# Managed Objects groups

mgwAlarmsObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 38791, 1, 4, 1, 100, 1, 1)
)
mgwAlarmsObjectGroup.setObjects(
      *(("ATOS-CH-MGW-MGW-ALARM-MIB", "mgwNrAlarms"),
        ("ATOS-CH-MGW-MGW-ALARM-MIB", "mgwAlarmType"),
        ("ATOS-CH-MGW-MGW-ALARM-MIB", "mgwAlarmSeverity"),
        ("ATOS-CH-MGW-MGW-ALARM-MIB", "mgwAlarmBeginDateTime"),
        ("ATOS-CH-MGW-MGW-ALARM-MIB", "mgwAlarmIsFlapping"),
        ("ATOS-CH-MGW-MGW-ALARM-MIB", "mgwAlarmParam1"),
        ("ATOS-CH-MGW-MGW-ALARM-MIB", "mgwAlarmParam2"),
        ("ATOS-CH-MGW-MGW-ALARM-MIB", "mgwAlarmParam3"),
        ("ATOS-CH-MGW-MGW-ALARM-MIB", "mgwAlarmParam4"))
)
if mibBuilder.loadTexts:
    mgwAlarmsObjectGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ATOS-CH-MGW-MGW-ALARM-MIB",
    **{"MgwAlarmSeverity": MgwAlarmSeverity,
       "MgwConnectionState": MgwConnectionState,
       "MgwNullableBoolean": MgwNullableBoolean,
       "MgwAlarmType": MgwAlarmType,
       "atos": atos,
       "ch": ch,
       "mgw": mgw,
       "mgwMgwAlarmMIB": mgwMgwAlarmMIB,
       "mgwAlarms": mgwAlarms,
       "mgwNrAlarms": mgwNrAlarms,
       "mgwAlarmTable": mgwAlarmTable,
       "mgwAlarmEntry": mgwAlarmEntry,
       "mgwAlarmIdx": mgwAlarmIdx,
       "mgwAlarmType": mgwAlarmType,
       "mgwAlarmSeverity": mgwAlarmSeverity,
       "mgwAlarmBeginDateTime": mgwAlarmBeginDateTime,
       "mgwAlarmIsFlapping": mgwAlarmIsFlapping,
       "mgwAlarmParam1": mgwAlarmParam1,
       "mgwAlarmParam2": mgwAlarmParam2,
       "mgwAlarmParam3": mgwAlarmParam3,
       "mgwAlarmParam4": mgwAlarmParam4,
       "mgwAlarmMIBConformance": mgwAlarmMIBConformance,
       "mgwAlarmsConformance": mgwAlarmsConformance,
       "mgwAlarmsObjectGroup": mgwAlarmsObjectGroup}
)
