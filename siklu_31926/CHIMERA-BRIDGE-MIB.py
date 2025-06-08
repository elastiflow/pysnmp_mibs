# SNMP MIB module (CHIMERA-BRIDGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/siklu_31926/CHIMERA-BRIDGE-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 11:57:26 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



class AlarmSeverity(TextualConvention, Integer32):
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
        *(("critical", 1),
          ("major", 2),
          ("minor", 3),
          ("warning", 4),
          ("no-alarm", 5))
    )



class AlarmType(TextualConvention, Integer32):
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
        *(("link-down", 1),
          ("temperature-high", 2),
          ("synthesizer-unlock", 3),
          ("pow-low", 4),
          ("cfm-mep-error", 5))
    )



# MIB Managed Objects in the order of their OIDs

_RadioBridgeRoot_ObjectIdentity = ObjectIdentity
radioBridgeRoot = _RadioBridgeRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31926)
)
_RadioBridgeSystem_ObjectIdentity = ObjectIdentity
radioBridgeSystem = _RadioBridgeSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31926, 1)
)
_RbSysVoltage_Type = Integer32
_RbSysVoltage_Object = MibScalar
rbSysVoltage = _RbSysVoltage_Object(
    (1, 3, 6, 1, 4, 1, 31926, 1, 1),
    _RbSysVoltage_Type()
)
rbSysVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSysVoltage.setStatus("current")
_RbSysTemperature_Type = Integer32
_RbSysTemperature_Object = MibScalar
rbSysTemperature = _RbSysTemperature_Object(
    (1, 3, 6, 1, 4, 1, 31926, 1, 2),
    _RbSysTemperature_Type()
)
rbSysTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSysTemperature.setStatus("current")
_RbSystemUpAbsoluteTime_Type = Counter64
_RbSystemUpAbsoluteTime_Object = MibScalar
rbSystemUpAbsoluteTime = _RbSystemUpAbsoluteTime_Object(
    (1, 3, 6, 1, 4, 1, 31926, 1, 11),
    _RbSystemUpAbsoluteTime_Type()
)
rbSystemUpAbsoluteTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSystemUpAbsoluteTime.setStatus("current")
_RadioBridgeRf_ObjectIdentity = ObjectIdentity
radioBridgeRf = _RadioBridgeRf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31926, 2)
)
_RbRfTable_Object = MibTable
rbRfTable = _RbRfTable_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 1)
)
if mibBuilder.loadTexts:
    rbRfTable.setStatus("current")
_RbRfEntry_Object = MibTableRow
rbRfEntry = _RbRfEntry_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 1, 1)
)
rbRfEntry.setIndexNames(
    (0, "CHIMERA-BRIDGE-MIB", "rfIndex"),
)
if mibBuilder.loadTexts:
    rbRfEntry.setStatus("current")
_RfIndex_Type = Integer32
_RfIndex_Object = MibTableColumn
rfIndex = _RfIndex_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 1, 1, 1),
    _RfIndex_Type()
)
rfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rfIndex.setStatus("current")


class _RfChannelWidth_Type(Integer32):
    """Custom type rfChannelWidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("rfWidth2000", 1)
    )


_RfChannelWidth_Type.__name__ = "Integer32"
_RfChannelWidth_Object = MibTableColumn
rfChannelWidth = _RfChannelWidth_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 1, 1, 2),
    _RfChannelWidth_Type()
)
rfChannelWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfChannelWidth.setStatus("current")
_RfRxFrequency_Type = Integer32
_RfRxFrequency_Object = MibTableColumn
rfRxFrequency = _RfRxFrequency_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 1, 1, 3),
    _RfRxFrequency_Type()
)
rfRxFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfRxFrequency.setStatus("current")
_RfTxFrequency_Type = Integer32
_RfTxFrequency_Object = MibTableColumn
rfTxFrequency = _RfTxFrequency_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 1, 1, 4),
    _RfTxFrequency_Type()
)
rfTxFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfTxFrequency.setStatus("current")


class _RfModulationType_Type(Integer32):
    """Custom type rfModulationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("rfModulationBPSK", 1),
          ("rfModulationQPSK", 2),
          ("rfModulation8PSK", 3),
          ("rfModulationQAM-16", 4),
          ("rfModulationQAM-32", 5),
          ("rfModulationQAM-64", 6),
          ("rfModulationQAM-128", 7),
          ("rfModulationQAM-256", 8),
          ("rfModulationQAM-512", 9),
          ("rfModulationQAM-1024", 10))
    )


_RfModulationType_Type.__name__ = "Integer32"
_RfModulationType_Object = MibTableColumn
rfModulationType = _RfModulationType_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 1, 1, 4),
    _RfModulationType_Type()
)
rfModulationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfModulationType.setStatus("current")
_RfInPower_Type = Integer32
_RfInPower_Object = MibTableColumn
rfInPower = _RfInPower_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 1, 1, 5),
    _RfInPower_Type()
)
rfInPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfInPower.setStatus("current")
_RfMseNormalized_Type = Integer32
_RfMseNormalized_Object = MibTableColumn
rfMseNormalized = _RfMseNormalized_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 1, 1, 6),
    _RfMseNormalized_Type()
)
rfMseNormalized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfMseNormalized.setStatus("current")
_RfRxBer_Type = Integer32
_RfRxBer_Object = MibTableColumn
rfRxBer = _RfRxBer_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 1, 1, 7),
    _RfRxBer_Type()
)
rfRxBer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfRxBer.setStatus("current")
_RfAverageRssi_Type = Integer32
_RfAverageRssi_Object = MibTableColumn
rfAverageRssi = _RfAverageRssi_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 1, 1, 8),
    _RfAverageRssi_Type()
)
rfAverageRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfAverageRssi.setStatus("current")


class _RfRxSynthLock_Type(Integer32):
    """Custom type rfRxSynthLock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("rxSynthUnlock", 0),
          ("rxSynthLock", 1))
    )


_RfRxSynthLock_Type.__name__ = "Integer32"
_RfRxSynthLock_Object = MibTableColumn
rfRxSynthLock = _RfRxSynthLock_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 1, 1, 9),
    _RfRxSynthLock_Type()
)
rfRxSynthLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfRxSynthLock.setStatus("current")
_RfTemperature_Type = Integer32
_RfTemperature_Object = MibTableColumn
rfTemperature = _RfTemperature_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 1, 1, 10),
    _RfTemperature_Type()
)
rfTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfTemperature.setStatus("current")
_RadioBridgeTraps_ObjectIdentity = ObjectIdentity
radioBridgeTraps = _RadioBridgeTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31926, 3)
)
_RadioBridgeAlarms_ObjectIdentity = ObjectIdentity
radioBridgeAlarms = _RadioBridgeAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31926, 11)
)
_RbAlarmsCommon_ObjectIdentity = ObjectIdentity
rbAlarmsCommon = _RbAlarmsCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31926, 11, 1)
)
_RbCurrentAlarmChangeCounter_Type = Integer32
_RbCurrentAlarmChangeCounter_Object = MibScalar
rbCurrentAlarmChangeCounter = _RbCurrentAlarmChangeCounter_Object(
    (1, 3, 6, 1, 4, 1, 31926, 11, 1, 1),
    _RbCurrentAlarmChangeCounter_Type()
)
rbCurrentAlarmChangeCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbCurrentAlarmChangeCounter.setStatus("current")
_RbCurrentAlarmMostSevere_Type = AlarmSeverity
_RbCurrentAlarmMostSevere_Object = MibScalar
rbCurrentAlarmMostSevere = _RbCurrentAlarmMostSevere_Object(
    (1, 3, 6, 1, 4, 1, 31926, 11, 1, 2),
    _RbCurrentAlarmMostSevere_Type()
)
rbCurrentAlarmMostSevere.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbCurrentAlarmMostSevere.setStatus("current")
_RbCurrentAlarmLastIndex_Type = Integer32
_RbCurrentAlarmLastIndex_Object = MibScalar
rbCurrentAlarmLastIndex = _RbCurrentAlarmLastIndex_Object(
    (1, 3, 6, 1, 4, 1, 31926, 11, 1, 3),
    _RbCurrentAlarmLastIndex_Type()
)
rbCurrentAlarmLastIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbCurrentAlarmLastIndex.setStatus("current")


class _RbCurrentAlarmLastTrapType_Type(Integer32):
    """Custom type rbCurrentAlarmLastTrapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarm-up", 1),
          ("alarm-down", 2))
    )


_RbCurrentAlarmLastTrapType_Type.__name__ = "Integer32"
_RbCurrentAlarmLastTrapType_Object = MibScalar
rbCurrentAlarmLastTrapType = _RbCurrentAlarmLastTrapType_Object(
    (1, 3, 6, 1, 4, 1, 31926, 11, 1, 4),
    _RbCurrentAlarmLastTrapType_Type()
)
rbCurrentAlarmLastTrapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbCurrentAlarmLastTrapType.setStatus("current")
_RbCurrentAlarmTable_Object = MibTable
rbCurrentAlarmTable = _RbCurrentAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 31926, 11, 2)
)
if mibBuilder.loadTexts:
    rbCurrentAlarmTable.setStatus("current")
_RbCurrentAlarmEntry_Object = MibTableRow
rbCurrentAlarmEntry = _RbCurrentAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 31926, 11, 2, 1)
)
rbCurrentAlarmEntry.setIndexNames(
    (0, "CHIMERA-BRIDGE-MIB", "rbCurrentAlarmIndex"),
)
if mibBuilder.loadTexts:
    rbCurrentAlarmEntry.setStatus("current")
_RbCurrentAlarmIndex_Type = Integer32
_RbCurrentAlarmIndex_Object = MibTableColumn
rbCurrentAlarmIndex = _RbCurrentAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 31926, 11, 2, 1, 1),
    _RbCurrentAlarmIndex_Type()
)
rbCurrentAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbCurrentAlarmIndex.setStatus("current")
_RbCurrentAlarmType_Type = AlarmType
_RbCurrentAlarmType_Object = MibTableColumn
rbCurrentAlarmType = _RbCurrentAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 31926, 11, 2, 1, 2),
    _RbCurrentAlarmType_Type()
)
rbCurrentAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbCurrentAlarmType.setStatus("current")
_RbCurrentAlarmTypeName_Type = DisplayString
_RbCurrentAlarmTypeName_Object = MibTableColumn
rbCurrentAlarmTypeName = _RbCurrentAlarmTypeName_Object(
    (1, 3, 6, 1, 4, 1, 31926, 11, 2, 1, 3),
    _RbCurrentAlarmTypeName_Type()
)
rbCurrentAlarmTypeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbCurrentAlarmTypeName.setStatus("current")
_RbCurrentAlarmSource_Type = DisplayString
_RbCurrentAlarmSource_Object = MibTableColumn
rbCurrentAlarmSource = _RbCurrentAlarmSource_Object(
    (1, 3, 6, 1, 4, 1, 31926, 11, 2, 1, 4),
    _RbCurrentAlarmSource_Type()
)
rbCurrentAlarmSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbCurrentAlarmSource.setStatus("current")
_RbCurrentAlarmSeverity_Type = AlarmSeverity
_RbCurrentAlarmSeverity_Object = MibTableColumn
rbCurrentAlarmSeverity = _RbCurrentAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 31926, 11, 2, 1, 5),
    _RbCurrentAlarmSeverity_Type()
)
rbCurrentAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbCurrentAlarmSeverity.setStatus("current")
_RbCurrentAlarmRaisedTime_Type = TimeTicks
_RbCurrentAlarmRaisedTime_Object = MibTableColumn
rbCurrentAlarmRaisedTime = _RbCurrentAlarmRaisedTime_Object(
    (1, 3, 6, 1, 4, 1, 31926, 11, 2, 1, 6),
    _RbCurrentAlarmRaisedTime_Type()
)
rbCurrentAlarmRaisedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbCurrentAlarmRaisedTime.setStatus("current")
_RbCurrentAlarmDesc_Type = DisplayString
_RbCurrentAlarmDesc_Object = MibTableColumn
rbCurrentAlarmDesc = _RbCurrentAlarmDesc_Object(
    (1, 3, 6, 1, 4, 1, 31926, 11, 2, 1, 7),
    _RbCurrentAlarmDesc_Type()
)
rbCurrentAlarmDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbCurrentAlarmDesc.setStatus("current")
_RbCurrentAlarmCause_Type = DisplayString
_RbCurrentAlarmCause_Object = MibTableColumn
rbCurrentAlarmCause = _RbCurrentAlarmCause_Object(
    (1, 3, 6, 1, 4, 1, 31926, 11, 2, 1, 8),
    _RbCurrentAlarmCause_Type()
)
rbCurrentAlarmCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbCurrentAlarmCause.setStatus("current")
_RbCurrentAlarmAction_Type = DisplayString
_RbCurrentAlarmAction_Object = MibTableColumn
rbCurrentAlarmAction = _RbCurrentAlarmAction_Object(
    (1, 3, 6, 1, 4, 1, 31926, 11, 2, 1, 9),
    _RbCurrentAlarmAction_Type()
)
rbCurrentAlarmAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbCurrentAlarmAction.setStatus("current")
_RbCurrentAlarmIfIndex_Type = Integer32
_RbCurrentAlarmIfIndex_Object = MibTableColumn
rbCurrentAlarmIfIndex = _RbCurrentAlarmIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 31926, 11, 2, 1, 10),
    _RbCurrentAlarmIfIndex_Type()
)
rbCurrentAlarmIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbCurrentAlarmIfIndex.setStatus("current")

# Managed Objects groups


# Notification objects

trapModulationChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 31926, 3, 1)
)
trapModulationChange.setObjects(
      *(("CHIMERA-BRIDGE-MIB", "rfModulationType"),
        ("CHIMERA-BRIDGE-MIB", "rfNumOfSubchannels"),
        ("CHIMERA-BRIDGE-MIB", "rfNumOfRepetitions"),
        ("CHIMERA-BRIDGE-MIB", "rfFecRate"))
)
if mibBuilder.loadTexts:
    trapModulationChange.setStatus(
        "current"
    )

trapTemperatureHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 31926, 3, 2)
)
if mibBuilder.loadTexts:
    trapTemperatureHigh.setStatus(
        "current"
    )

trapTemperatureNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 31926, 3, 3)
)
if mibBuilder.loadTexts:
    trapTemperatureNormal.setStatus(
        "current"
    )

trapSyntehesizerUnlock = NotificationType(
    (1, 3, 6, 1, 4, 1, 31926, 3, 7)
)
if mibBuilder.loadTexts:
    trapSyntehesizerUnlock.setStatus(
        "current"
    )

trapSyntehesizerLock = NotificationType(
    (1, 3, 6, 1, 4, 1, 31926, 3, 8)
)
if mibBuilder.loadTexts:
    trapSyntehesizerLock.setStatus(
        "current"
    )

trapBerNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 31926, 3, 8)
)
if mibBuilder.loadTexts:
    trapBerNormal.setStatus(
        "current"
    )

trapBerHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 31926, 3, 8)
)
if mibBuilder.loadTexts:
    trapBerHigh.setStatus(
        "current"
    )

trapSfpNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 31926, 3, 8)
)
if mibBuilder.loadTexts:
    trapSfpNormal.setStatus(
        "current"
    )

trapSfpFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 31926, 3, 8)
)
if mibBuilder.loadTexts:
    trapSfpFault.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CHIMERA-BRIDGE-MIB",
    **{"AlarmSeverity": AlarmSeverity,
       "AlarmType": AlarmType,
       "radioBridgeRoot": radioBridgeRoot,
       "radioBridgeSystem": radioBridgeSystem,
       "rbSysVoltage": rbSysVoltage,
       "rbSysTemperature": rbSysTemperature,
       "rbSystemUpAbsoluteTime": rbSystemUpAbsoluteTime,
       "radioBridgeRf": radioBridgeRf,
       "rbRfTable": rbRfTable,
       "rbRfEntry": rbRfEntry,
       "rfIndex": rfIndex,
       "rfChannelWidth": rfChannelWidth,
       "rfRxFrequency": rfRxFrequency,
       "rfTxFrequency": rfTxFrequency,
       "rfModulationType": rfModulationType,
       "rfInPower": rfInPower,
       "rfMseNormalized": rfMseNormalized,
       "rfRxBer": rfRxBer,
       "rfAverageRssi": rfAverageRssi,
       "rfRxSynthLock": rfRxSynthLock,
       "rfTemperature": rfTemperature,
       "radioBridgeTraps": radioBridgeTraps,
       "trapModulationChange": trapModulationChange,
       "trapTemperatureHigh": trapTemperatureHigh,
       "trapTemperatureNormal": trapTemperatureNormal,
       "trapSyntehesizerUnlock": trapSyntehesizerUnlock,
       "trapSyntehesizerLock": trapSyntehesizerLock,
       "trapBerNormal": trapBerNormal,
       "trapBerHigh": trapBerHigh,
       "trapSfpNormal": trapSfpNormal,
       "trapSfpFault": trapSfpFault,
       "radioBridgeAlarms": radioBridgeAlarms,
       "rbAlarmsCommon": rbAlarmsCommon,
       "rbCurrentAlarmChangeCounter": rbCurrentAlarmChangeCounter,
       "rbCurrentAlarmMostSevere": rbCurrentAlarmMostSevere,
       "rbCurrentAlarmLastIndex": rbCurrentAlarmLastIndex,
       "rbCurrentAlarmLastTrapType": rbCurrentAlarmLastTrapType,
       "rbCurrentAlarmTable": rbCurrentAlarmTable,
       "rbCurrentAlarmEntry": rbCurrentAlarmEntry,
       "rbCurrentAlarmIndex": rbCurrentAlarmIndex,
       "rbCurrentAlarmType": rbCurrentAlarmType,
       "rbCurrentAlarmTypeName": rbCurrentAlarmTypeName,
       "rbCurrentAlarmSource": rbCurrentAlarmSource,
       "rbCurrentAlarmSeverity": rbCurrentAlarmSeverity,
       "rbCurrentAlarmRaisedTime": rbCurrentAlarmRaisedTime,
       "rbCurrentAlarmDesc": rbCurrentAlarmDesc,
       "rbCurrentAlarmCause": rbCurrentAlarmCause,
       "rbCurrentAlarmAction": rbCurrentAlarmAction,
       "rbCurrentAlarmIfIndex": rbCurrentAlarmIfIndex}
)
