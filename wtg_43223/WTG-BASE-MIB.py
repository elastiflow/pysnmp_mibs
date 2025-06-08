# SNMP MIB module (WTG-BASE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/wtg_43223/WTG-BASE-MIB.mib
# Produced by pysmi-1.6.1 at Thu Jun  5 22:06:24 2025
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

(DisplayString,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

wtgRegMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43223)
)
if mibBuilder.loadTexts:
    wtgRegMIB.setRevisions(
        ("2020-05-15 08:25",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WtgObjects_ObjectIdentity = ObjectIdentity
wtgObjects = _WtgObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43223, 1)
)
_WtgBTSAlarms_ObjectIdentity = ObjectIdentity
wtgBTSAlarms = _WtgBTSAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43223, 1, 1)
)
_WtgBTSCh0Alarms_ObjectIdentity = ObjectIdentity
wtgBTSCh0Alarms = _WtgBTSCh0Alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43223, 1, 1, 1)
)


class _WtgBTSCh0UnderPwr_Type(TruthValue):
    """Custom type wtgBTSCh0UnderPwr based on TruthValue"""
    defaultValue = 2


_WtgBTSCh0UnderPwr_Type.__name__ = "TruthValue"
_WtgBTSCh0UnderPwr_Object = MibScalar
wtgBTSCh0UnderPwr = _WtgBTSCh0UnderPwr_Object(
    (1, 3, 6, 1, 4, 1, 43223, 1, 1, 1, 1),
    _WtgBTSCh0UnderPwr_Type()
)
wtgBTSCh0UnderPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtgBTSCh0UnderPwr.setStatus("current")


class _WtgBTSCh0OverPwr_Type(TruthValue):
    """Custom type wtgBTSCh0OverPwr based on TruthValue"""
    defaultValue = 2


_WtgBTSCh0OverPwr_Type.__name__ = "TruthValue"
_WtgBTSCh0OverPwr_Object = MibScalar
wtgBTSCh0OverPwr = _WtgBTSCh0OverPwr_Object(
    (1, 3, 6, 1, 4, 1, 43223, 1, 1, 1, 2),
    _WtgBTSCh0OverPwr_Type()
)
wtgBTSCh0OverPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtgBTSCh0OverPwr.setStatus("current")
_WtgBTSCh0InputPwr_Type = Integer32
_WtgBTSCh0InputPwr_Object = MibScalar
wtgBTSCh0InputPwr = _WtgBTSCh0InputPwr_Object(
    (1, 3, 6, 1, 4, 1, 43223, 1, 1, 1, 3),
    _WtgBTSCh0InputPwr_Type()
)
wtgBTSCh0InputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtgBTSCh0InputPwr.setStatus("current")


class _WtgGWThruPort_Type(TruthValue):
    """Custom type wtgGWThruPort based on TruthValue"""
    defaultValue = 2


_WtgGWThruPort_Type.__name__ = "TruthValue"
_WtgGWThruPort_Object = MibScalar
wtgGWThruPort = _WtgGWThruPort_Object(
    (1, 3, 6, 1, 4, 1, 43223, 1, 1, 2),
    _WtgGWThruPort_Type()
)
wtgGWThruPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtgGWThruPort.setStatus("current")


class _WtgGWAlarmStatus_Type(TruthValue):
    """Custom type wtgGWAlarmStatus based on TruthValue"""
    defaultValue = 2


_WtgGWAlarmStatus_Type.__name__ = "TruthValue"
_WtgGWAlarmStatus_Object = MibScalar
wtgGWAlarmStatus = _WtgGWAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 43223, 1, 1, 3),
    _WtgGWAlarmStatus_Type()
)
wtgGWAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtgGWAlarmStatus.setStatus("current")


class _WtgGWTemp_Type(Integer32):
    """Custom type wtgGWTemp based on Integer32"""
    defaultValue = 0


_WtgGWTemp_Type.__name__ = "Integer32"
_WtgGWTemp_Object = MibScalar
wtgGWTemp = _WtgGWTemp_Object(
    (1, 3, 6, 1, 4, 1, 43223, 1, 1, 4),
    _WtgGWTemp_Type()
)
wtgGWTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtgGWTemp.setStatus("current")
_WtgSCPLsTable_Object = MibTable
wtgSCPLsTable = _WtgSCPLsTable_Object(
    (1, 3, 6, 1, 4, 1, 43223, 1, 2)
)
if mibBuilder.loadTexts:
    wtgSCPLsTable.setStatus("current")
_WtgSCPLsEntry_Object = MibTableRow
wtgSCPLsEntry = _WtgSCPLsEntry_Object(
    (1, 3, 6, 1, 4, 1, 43223, 1, 2, 1)
)
wtgSCPLsEntry.setIndexNames(
    (0, "WTG-BASE-MIB", "wtgSCPLID"),
)
if mibBuilder.loadTexts:
    wtgSCPLsEntry.setStatus("current")


class _WtgSCPLID_Type(Integer32):
    """Custom type wtgSCPLID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_WtgSCPLID_Type.__name__ = "Integer32"
_WtgSCPLID_Object = MibTableColumn
wtgSCPLID = _WtgSCPLID_Object(
    (1, 3, 6, 1, 4, 1, 43223, 1, 2, 1, 1),
    _WtgSCPLID_Type()
)
wtgSCPLID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtgSCPLID.setStatus("current")


class _WtgSCPLLocation_Type(OctetString):
    """Custom type wtgSCPLLocation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WtgSCPLLocation_Type.__name__ = "OctetString"
_WtgSCPLLocation_Object = MibTableColumn
wtgSCPLLocation = _WtgSCPLLocation_Object(
    (1, 3, 6, 1, 4, 1, 43223, 1, 2, 1, 2),
    _WtgSCPLLocation_Type()
)
wtgSCPLLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtgSCPLLocation.setStatus("current")


class _WtgSCPLMacAddr_Type(OctetString):
    """Custom type wtgSCPLMacAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WtgSCPLMacAddr_Type.__name__ = "OctetString"
_WtgSCPLMacAddr_Object = MibTableColumn
wtgSCPLMacAddr = _WtgSCPLMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 43223, 1, 2, 1, 3),
    _WtgSCPLMacAddr_Type()
)
wtgSCPLMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtgSCPLMacAddr.setStatus("current")


class _WtgSCPLNotActive_Type(TruthValue):
    """Custom type wtgSCPLNotActive based on TruthValue"""
    defaultValue = 2


_WtgSCPLNotActive_Type.__name__ = "TruthValue"
_WtgSCPLNotActive_Object = MibTableColumn
wtgSCPLNotActive = _WtgSCPLNotActive_Object(
    (1, 3, 6, 1, 4, 1, 43223, 1, 2, 1, 4),
    _WtgSCPLNotActive_Type()
)
wtgSCPLNotActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtgSCPLNotActive.setStatus("current")


class _WtgSCPLAntenna_Type(TruthValue):
    """Custom type wtgSCPLAntenna based on TruthValue"""
    defaultValue = 2


_WtgSCPLAntenna_Type.__name__ = "TruthValue"
_WtgSCPLAntenna_Object = MibTableColumn
wtgSCPLAntenna = _WtgSCPLAntenna_Object(
    (1, 3, 6, 1, 4, 1, 43223, 1, 2, 1, 5),
    _WtgSCPLAntenna_Type()
)
wtgSCPLAntenna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtgSCPLAntenna.setStatus("current")
_WtgSCPLThruPort_Type = TruthValue
_WtgSCPLThruPort_Object = MibTableColumn
wtgSCPLThruPort = _WtgSCPLThruPort_Object(
    (1, 3, 6, 1, 4, 1, 43223, 1, 2, 1, 6),
    _WtgSCPLThruPort_Type()
)
wtgSCPLThruPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtgSCPLThruPort.setStatus("current")
_WtgSCPLForward_Type = TruthValue
_WtgSCPLForward_Object = MibTableColumn
wtgSCPLForward = _WtgSCPLForward_Object(
    (1, 3, 6, 1, 4, 1, 43223, 1, 2, 1, 7),
    _WtgSCPLForward_Type()
)
wtgSCPLForward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtgSCPLForward.setStatus("current")
_WtgSCPLAlarmStatus_Type = TruthValue
_WtgSCPLAlarmStatus_Object = MibTableColumn
wtgSCPLAlarmStatus = _WtgSCPLAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 43223, 1, 2, 1, 8),
    _WtgSCPLAlarmStatus_Type()
)
wtgSCPLAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtgSCPLAlarmStatus.setStatus("current")
_WtgSCPLRSSI_Type = Integer32
_WtgSCPLRSSI_Object = MibTableColumn
wtgSCPLRSSI = _WtgSCPLRSSI_Object(
    (1, 3, 6, 1, 4, 1, 43223, 1, 2, 1, 9),
    _WtgSCPLRSSI_Type()
)
wtgSCPLRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtgSCPLRSSI.setStatus("current")


class _WtgSCPLLastRecorded_Type(OctetString):
    """Custom type wtgSCPLLastRecorded based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WtgSCPLLastRecorded_Type.__name__ = "OctetString"
_WtgSCPLLastRecorded_Object = MibTableColumn
wtgSCPLLastRecorded = _WtgSCPLLastRecorded_Object(
    (1, 3, 6, 1, 4, 1, 43223, 1, 2, 1, 10),
    _WtgSCPLLastRecorded_Type()
)
wtgSCPLLastRecorded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtgSCPLLastRecorded.setStatus("current")
_WtgSCPLTemp_Type = Integer32
_WtgSCPLTemp_Object = MibTableColumn
wtgSCPLTemp = _WtgSCPLTemp_Object(
    (1, 3, 6, 1, 4, 1, 43223, 1, 2, 1, 11),
    _WtgSCPLTemp_Type()
)
wtgSCPLTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtgSCPLTemp.setStatus("current")
_WtgEvents_ObjectIdentity = ObjectIdentity
wtgEvents = _WtgEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43223, 2)
)
_WtgConf_ObjectIdentity = ObjectIdentity
wtgConf = _WtgConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43223, 3)
)
_WtgGroups_ObjectIdentity = ObjectIdentity
wtgGroups = _WtgGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43223, 3, 1)
)
_WtgCompliances_ObjectIdentity = ObjectIdentity
wtgCompliances = _WtgCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43223, 3, 2)
)

# Managed Objects groups

wtgBTSGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 43223, 3, 1, 1)
)
wtgBTSGroup.setObjects(
      *(("WTG-BASE-MIB", "wtgBTSCh0UnderPwr"),
        ("WTG-BASE-MIB", "wtgBTSCh0OverPwr"),
        ("WTG-BASE-MIB", "wtgBTSCh0InputPwr"),
        ("WTG-BASE-MIB", "wtgGWThruPort"),
        ("WTG-BASE-MIB", "wtgGWAlarmStatus"),
        ("WTG-BASE-MIB", "wtgGWTemp"))
)
if mibBuilder.loadTexts:
    wtgBTSGroup.setStatus("current")

wtgSCPLGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 43223, 3, 1, 3)
)
wtgSCPLGroup.setObjects(
      *(("WTG-BASE-MIB", "wtgSCPLID"),
        ("WTG-BASE-MIB", "wtgSCPLLocation"),
        ("WTG-BASE-MIB", "wtgSCPLMacAddr"),
        ("WTG-BASE-MIB", "wtgSCPLNotActive"),
        ("WTG-BASE-MIB", "wtgSCPLAntenna"),
        ("WTG-BASE-MIB", "wtgSCPLThruPort"),
        ("WTG-BASE-MIB", "wtgSCPLForward"),
        ("WTG-BASE-MIB", "wtgSCPLAlarmStatus"),
        ("WTG-BASE-MIB", "wtgSCPLRSSI"),
        ("WTG-BASE-MIB", "wtgSCPLLastRecorded"),
        ("WTG-BASE-MIB", "wtgSCPLTemp"))
)
if mibBuilder.loadTexts:
    wtgSCPLGroup.setStatus("current")


# Notification objects

wtgBTSCh0AlarmTrigger = NotificationType(
    (1, 3, 6, 1, 4, 1, 43223, 2, 1)
)
wtgBTSCh0AlarmTrigger.setObjects(
      *(("WTG-BASE-MIB", "wtgBTSCh0UnderPwr"),
        ("WTG-BASE-MIB", "wtgBTSCh0OverPwr"),
        ("WTG-BASE-MIB", "wtgBTSCh0InputPwr"),
        ("WTG-BASE-MIB", "wtgGWThruPort"),
        ("WTG-BASE-MIB", "wtgGWAlarmStatus"),
        ("WTG-BASE-MIB", "wtgGWTemp"))
)
if mibBuilder.loadTexts:
    wtgBTSCh0AlarmTrigger.setStatus(
        "current"
    )

wtgSCPLAlarmTrigger = NotificationType(
    (1, 3, 6, 1, 4, 1, 43223, 2, 2)
)
wtgSCPLAlarmTrigger.setObjects(
      *(("WTG-BASE-MIB", "wtgSCPLID"),
        ("WTG-BASE-MIB", "wtgSCPLLocation"),
        ("WTG-BASE-MIB", "wtgSCPLMacAddr"),
        ("WTG-BASE-MIB", "wtgSCPLNotActive"),
        ("WTG-BASE-MIB", "wtgSCPLAntenna"),
        ("WTG-BASE-MIB", "wtgSCPLThruPort"),
        ("WTG-BASE-MIB", "wtgSCPLForward"),
        ("WTG-BASE-MIB", "wtgSCPLAlarmStatus"),
        ("WTG-BASE-MIB", "wtgSCPLRSSI"),
        ("WTG-BASE-MIB", "wtgSCPLLastRecorded"),
        ("WTG-BASE-MIB", "wtgSCPLTemp"))
)
if mibBuilder.loadTexts:
    wtgSCPLAlarmTrigger.setStatus(
        "current"
    )


# Notifications groups

wtgBTSEvents = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 43223, 3, 1, 2)
)
wtgBTSEvents.setObjects(
    ("WTG-BASE-MIB", "wtgBTSCh0AlarmTrigger")
)
if mibBuilder.loadTexts:
    wtgBTSEvents.setStatus(
        "current"
    )

wtgSCPLEvents = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 43223, 3, 1, 4)
)
wtgSCPLEvents.setObjects(
    ("WTG-BASE-MIB", "wtgSCPLAlarmTrigger")
)
if mibBuilder.loadTexts:
    wtgSCPLEvents.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WTG-BASE-MIB",
    **{"wtgRegMIB": wtgRegMIB,
       "wtgObjects": wtgObjects,
       "wtgBTSAlarms": wtgBTSAlarms,
       "wtgBTSCh0Alarms": wtgBTSCh0Alarms,
       "wtgBTSCh0UnderPwr": wtgBTSCh0UnderPwr,
       "wtgBTSCh0OverPwr": wtgBTSCh0OverPwr,
       "wtgBTSCh0InputPwr": wtgBTSCh0InputPwr,
       "wtgGWThruPort": wtgGWThruPort,
       "wtgGWAlarmStatus": wtgGWAlarmStatus,
       "wtgGWTemp": wtgGWTemp,
       "wtgSCPLsTable": wtgSCPLsTable,
       "wtgSCPLsEntry": wtgSCPLsEntry,
       "wtgSCPLID": wtgSCPLID,
       "wtgSCPLLocation": wtgSCPLLocation,
       "wtgSCPLMacAddr": wtgSCPLMacAddr,
       "wtgSCPLNotActive": wtgSCPLNotActive,
       "wtgSCPLAntenna": wtgSCPLAntenna,
       "wtgSCPLThruPort": wtgSCPLThruPort,
       "wtgSCPLForward": wtgSCPLForward,
       "wtgSCPLAlarmStatus": wtgSCPLAlarmStatus,
       "wtgSCPLRSSI": wtgSCPLRSSI,
       "wtgSCPLLastRecorded": wtgSCPLLastRecorded,
       "wtgSCPLTemp": wtgSCPLTemp,
       "wtgEvents": wtgEvents,
       "wtgBTSCh0AlarmTrigger": wtgBTSCh0AlarmTrigger,
       "wtgSCPLAlarmTrigger": wtgSCPLAlarmTrigger,
       "wtgConf": wtgConf,
       "wtgGroups": wtgGroups,
       "wtgBTSGroup": wtgBTSGroup,
       "wtgBTSEvents": wtgBTSEvents,
       "wtgSCPLGroup": wtgSCPLGroup,
       "wtgSCPLEvents": wtgSCPLEvents,
       "wtgCompliances": wtgCompliances}
)
