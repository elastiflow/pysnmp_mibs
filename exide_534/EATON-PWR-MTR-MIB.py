# SNMP MIB module (EATON-PWR-MTR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/exide_534/EATON-PWR-MTR-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 22:56:03 2025
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

(NonNegativeInteger,
 PositiveInteger,
 powerChain) = mibBuilder.importSymbols(
    "EATON-OIDS",
    "NonNegativeInteger",
    "PositiveInteger",
    "powerChain")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

pwrMeterMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 534, 8, 3)
)
if mibBuilder.loadTexts:
    pwrMeterMIB.setRevisions(
        ("2009-07-14 00:00",
         "2008-04-09 00:00",
         "2008-03-17 00:00",
         "2007-12-03 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class EatonPowerQualityIndex(TextualConvention, Integer32):
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
        *(("normal", 1),
          ("caution", 2),
          ("alert", 3),
          ("unknown", 4))
    )



class PowerFactorInteger(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )



# MIB Managed Objects in the order of their OIDs

_PwrMeterMIBObjects_ObjectIdentity = ObjectIdentity
pwrMeterMIBObjects = _PwrMeterMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 8, 3, 1)
)
_MtrPowerQualityMeasures_ObjectIdentity = ObjectIdentity
mtrPowerQualityMeasures = _MtrPowerQualityMeasures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 8, 3, 1, 1)
)
_MtrPowerQualityMeasuresTable_Object = MibTable
mtrPowerQualityMeasuresTable = _MtrPowerQualityMeasuresTable_Object(
    (1, 3, 6, 1, 4, 1, 534, 8, 3, 1, 1, 1)
)
if mibBuilder.loadTexts:
    mtrPowerQualityMeasuresTable.setStatus("current")
_MtrPowerQualityMeasuresEntry_Object = MibTableRow
mtrPowerQualityMeasuresEntry = _MtrPowerQualityMeasuresEntry_Object(
    (1, 3, 6, 1, 4, 1, 534, 8, 3, 1, 1, 1, 1)
)
mtrPowerQualityMeasuresEntry.setIndexNames(
    (0, "EATON-PWR-MTR-MIB", "powerMeterIndex"),
)
if mibBuilder.loadTexts:
    mtrPowerQualityMeasuresEntry.setStatus("current")
_PowerMeterIndex_Type = PositiveInteger
_PowerMeterIndex_Object = MibTableColumn
powerMeterIndex = _PowerMeterIndex_Object(
    (1, 3, 6, 1, 4, 1, 534, 8, 3, 1, 1, 1, 1, 1),
    _PowerMeterIndex_Type()
)
powerMeterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    powerMeterIndex.setStatus("current")
_MtrPresentPowerQualityIndex_Type = EatonPowerQualityIndex
_MtrPresentPowerQualityIndex_Object = MibTableColumn
mtrPresentPowerQualityIndex = _MtrPresentPowerQualityIndex_Object(
    (1, 3, 6, 1, 4, 1, 534, 8, 3, 1, 1, 1, 1, 2),
    _MtrPresentPowerQualityIndex_Type()
)
mtrPresentPowerQualityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtrPresentPowerQualityIndex.setStatus("current")
_Mtr24hourPowerQualityIndex_Type = EatonPowerQualityIndex
_Mtr24hourPowerQualityIndex_Object = MibTableColumn
mtr24hourPowerQualityIndex = _Mtr24hourPowerQualityIndex_Object(
    (1, 3, 6, 1, 4, 1, 534, 8, 3, 1, 1, 1, 1, 3),
    _Mtr24hourPowerQualityIndex_Type()
)
mtr24hourPowerQualityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtr24hourPowerQualityIndex.setStatus("current")
_MtrPQVoltageTHD_Type = NonNegativeInteger
_MtrPQVoltageTHD_Object = MibTableColumn
mtrPQVoltageTHD = _MtrPQVoltageTHD_Object(
    (1, 3, 6, 1, 4, 1, 534, 8, 3, 1, 1, 1, 1, 4),
    _MtrPQVoltageTHD_Type()
)
mtrPQVoltageTHD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtrPQVoltageTHD.setStatus("current")
if mibBuilder.loadTexts:
    mtrPQVoltageTHD.setUnits("percent x100")
_MtrPQCurrentTDD_Type = NonNegativeInteger
_MtrPQCurrentTDD_Object = MibTableColumn
mtrPQCurrentTDD = _MtrPQCurrentTDD_Object(
    (1, 3, 6, 1, 4, 1, 534, 8, 3, 1, 1, 1, 1, 5),
    _MtrPQCurrentTDD_Type()
)
mtrPQCurrentTDD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtrPQCurrentTDD.setStatus("current")
if mibBuilder.loadTexts:
    mtrPQCurrentTDD.setUnits("percent x100")
_MtrPQLastSagSurgeReset_Type = DisplayString
_MtrPQLastSagSurgeReset_Object = MibTableColumn
mtrPQLastSagSurgeReset = _MtrPQLastSagSurgeReset_Object(
    (1, 3, 6, 1, 4, 1, 534, 8, 3, 1, 1, 1, 1, 6),
    _MtrPQLastSagSurgeReset_Type()
)
mtrPQLastSagSurgeReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtrPQLastSagSurgeReset.setStatus("current")
_MtrPQSagSurgeTable_Object = MibTable
mtrPQSagSurgeTable = _MtrPQSagSurgeTable_Object(
    (1, 3, 6, 1, 4, 1, 534, 8, 3, 1, 1, 2)
)
if mibBuilder.loadTexts:
    mtrPQSagSurgeTable.setStatus("current")
_MtrPQSagSurgeEntry_Object = MibTableRow
mtrPQSagSurgeEntry = _MtrPQSagSurgeEntry_Object(
    (1, 3, 6, 1, 4, 1, 534, 8, 3, 1, 1, 2, 1)
)
mtrPQSagSurgeEntry.setIndexNames(
    (0, "EATON-PWR-MTR-MIB", "powerMeterIndex"),
    (0, "EATON-PWR-MTR-MIB", "mtrPQSagSurgeIndex"),
)
if mibBuilder.loadTexts:
    mtrPQSagSurgeEntry.setStatus("current")
_MtrPQSagSurgeIndex_Type = PositiveInteger
_MtrPQSagSurgeIndex_Object = MibTableColumn
mtrPQSagSurgeIndex = _MtrPQSagSurgeIndex_Object(
    (1, 3, 6, 1, 4, 1, 534, 8, 3, 1, 1, 2, 1, 1),
    _MtrPQSagSurgeIndex_Type()
)
mtrPQSagSurgeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mtrPQSagSurgeIndex.setStatus("current")


class _MtrPQSagSurgeLevel_Type(DisplayString):
    """Custom type mtrPQSagSurgeLevel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_MtrPQSagSurgeLevel_Type.__name__ = "DisplayString"
_MtrPQSagSurgeLevel_Object = MibTableColumn
mtrPQSagSurgeLevel = _MtrPQSagSurgeLevel_Object(
    (1, 3, 6, 1, 4, 1, 534, 8, 3, 1, 1, 2, 1, 2),
    _MtrPQSagSurgeLevel_Type()
)
mtrPQSagSurgeLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtrPQSagSurgeLevel.setStatus("current")
_MtrPQSagCount_Type = NonNegativeInteger
_MtrPQSagCount_Object = MibTableColumn
mtrPQSagCount = _MtrPQSagCount_Object(
    (1, 3, 6, 1, 4, 1, 534, 8, 3, 1, 1, 2, 1, 3),
    _MtrPQSagCount_Type()
)
mtrPQSagCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtrPQSagCount.setStatus("current")
_MtrPQSurgeCount_Type = NonNegativeInteger
_MtrPQSurgeCount_Object = MibTableColumn
mtrPQSurgeCount = _MtrPQSurgeCount_Object(
    (1, 3, 6, 1, 4, 1, 534, 8, 3, 1, 1, 2, 1, 4),
    _MtrPQSurgeCount_Type()
)
mtrPQSurgeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtrPQSurgeCount.setStatus("current")
_PwrMeterRealTimeMeasures_ObjectIdentity = ObjectIdentity
pwrMeterRealTimeMeasures = _PwrMeterRealTimeMeasures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 8, 3, 1, 2)
)
_PwrMeterRtMeasuresTable_Object = MibTable
pwrMeterRtMeasuresTable = _PwrMeterRtMeasuresTable_Object(
    (1, 3, 6, 1, 4, 1, 534, 8, 3, 1, 2, 1)
)
if mibBuilder.loadTexts:
    pwrMeterRtMeasuresTable.setStatus("current")
_PwrMeterRtMeasuresEntry_Object = MibTableRow
pwrMeterRtMeasuresEntry = _PwrMeterRtMeasuresEntry_Object(
    (1, 3, 6, 1, 4, 1, 534, 8, 3, 1, 2, 1, 1)
)
pwrMeterRtMeasuresEntry.setIndexNames(
    (0, "EATON-PWR-MTR-MIB", "powerMeterIndex"),
)
if mibBuilder.loadTexts:
    pwrMeterRtMeasuresEntry.setStatus("current")
_PwrMtrRtNeutralCurrent_Type = NonNegativeInteger
_PwrMtrRtNeutralCurrent_Object = MibTableColumn
pwrMtrRtNeutralCurrent = _PwrMtrRtNeutralCurrent_Object(
    (1, 3, 6, 1, 4, 1, 534, 8, 3, 1, 2, 1, 1, 2),
    _PwrMtrRtNeutralCurrent_Type()
)
pwrMtrRtNeutralCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrMtrRtNeutralCurrent.setStatus("current")
if mibBuilder.loadTexts:
    pwrMtrRtNeutralCurrent.setUnits("0.1 Amps RMS")
_PwrMtrRtGroundCurrent_Type = NonNegativeInteger
_PwrMtrRtGroundCurrent_Object = MibTableColumn
pwrMtrRtGroundCurrent = _PwrMtrRtGroundCurrent_Object(
    (1, 3, 6, 1, 4, 1, 534, 8, 3, 1, 2, 1, 1, 3),
    _PwrMtrRtGroundCurrent_Type()
)
pwrMtrRtGroundCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrMtrRtGroundCurrent.setStatus("current")
if mibBuilder.loadTexts:
    pwrMtrRtGroundCurrent.setUnits("milli-Amps RMS")
_PwrMtrRtTotalWatts_Type = Integer32
_PwrMtrRtTotalWatts_Object = MibTableColumn
pwrMtrRtTotalWatts = _PwrMtrRtTotalWatts_Object(
    (1, 3, 6, 1, 4, 1, 534, 8, 3, 1, 2, 1, 1, 4),
    _PwrMtrRtTotalWatts_Type()
)
pwrMtrRtTotalWatts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrMtrRtTotalWatts.setStatus("current")
if mibBuilder.loadTexts:
    pwrMtrRtTotalWatts.setUnits("watts")
_PwrMtrRtTotalVA_Type = NonNegativeInteger
_PwrMtrRtTotalVA_Object = MibTableColumn
pwrMtrRtTotalVA = _PwrMtrRtTotalVA_Object(
    (1, 3, 6, 1, 4, 1, 534, 8, 3, 1, 2, 1, 1, 5),
    _PwrMtrRtTotalVA_Type()
)
pwrMtrRtTotalVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrMtrRtTotalVA.setStatus("current")
if mibBuilder.loadTexts:
    pwrMtrRtTotalVA.setUnits("VA")
_PwrMtrRtTotalVAR_Type = Integer32
_PwrMtrRtTotalVAR_Object = MibTableColumn
pwrMtrRtTotalVAR = _PwrMtrRtTotalVAR_Object(
    (1, 3, 6, 1, 4, 1, 534, 8, 3, 1, 2, 1, 1, 6),
    _PwrMtrRtTotalVAR_Type()
)
pwrMtrRtTotalVAR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrMtrRtTotalVAR.setStatus("current")
if mibBuilder.loadTexts:
    pwrMtrRtTotalVAR.setUnits("var")
_PwrMtrRtPowerFactor_Type = PowerFactorInteger
_PwrMtrRtPowerFactor_Object = MibTableColumn
pwrMtrRtPowerFactor = _PwrMtrRtPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 534, 8, 3, 1, 2, 1, 1, 7),
    _PwrMtrRtPowerFactor_Type()
)
pwrMtrRtPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrMtrRtPowerFactor.setStatus("current")
if mibBuilder.loadTexts:
    pwrMtrRtPowerFactor.setUnits("PF x100")
_PwrMtrRtFrequency_Type = NonNegativeInteger
_PwrMtrRtFrequency_Object = MibTableColumn
pwrMtrRtFrequency = _PwrMtrRtFrequency_Object(
    (1, 3, 6, 1, 4, 1, 534, 8, 3, 1, 2, 1, 1, 8),
    _PwrMtrRtFrequency_Type()
)
pwrMtrRtFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrMtrRtFrequency.setStatus("current")
if mibBuilder.loadTexts:
    pwrMtrRtFrequency.setUnits("0.01 Hertz")
_PwrMtrRtBtuPerHour_Type = NonNegativeInteger
_PwrMtrRtBtuPerHour_Object = MibTableColumn
pwrMtrRtBtuPerHour = _PwrMtrRtBtuPerHour_Object(
    (1, 3, 6, 1, 4, 1, 534, 8, 3, 1, 2, 1, 1, 9),
    _PwrMtrRtBtuPerHour_Type()
)
pwrMtrRtBtuPerHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrMtrRtBtuPerHour.setStatus("current")
if mibBuilder.loadTexts:
    pwrMtrRtBtuPerHour.setUnits("BTU/hr")
_PwrMeterRtPhaseMeasuresTable_Object = MibTable
pwrMeterRtPhaseMeasuresTable = _PwrMeterRtPhaseMeasuresTable_Object(
    (1, 3, 6, 1, 4, 1, 534, 8, 3, 1, 2, 2)
)
if mibBuilder.loadTexts:
    pwrMeterRtPhaseMeasuresTable.setStatus("current")
_PwrMeterRtPhaseMeasuresEntry_Object = MibTableRow
pwrMeterRtPhaseMeasuresEntry = _PwrMeterRtPhaseMeasuresEntry_Object(
    (1, 3, 6, 1, 4, 1, 534, 8, 3, 1, 2, 2, 1)
)
pwrMeterRtPhaseMeasuresEntry.setIndexNames(
    (0, "EATON-PWR-MTR-MIB", "powerMeterIndex"),
    (0, "EATON-PWR-MTR-MIB", "pwrMtrPhaseIndex"),
)
if mibBuilder.loadTexts:
    pwrMeterRtPhaseMeasuresEntry.setStatus("current")
_PwrMtrPhaseIndex_Type = PositiveInteger
_PwrMtrPhaseIndex_Object = MibTableColumn
pwrMtrPhaseIndex = _PwrMtrPhaseIndex_Object(
    (1, 3, 6, 1, 4, 1, 534, 8, 3, 1, 2, 2, 1, 1),
    _PwrMtrPhaseIndex_Type()
)
pwrMtrPhaseIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pwrMtrPhaseIndex.setStatus("current")
_PwrMtrRtPhaseVoltageLL_Type = NonNegativeInteger
_PwrMtrRtPhaseVoltageLL_Object = MibTableColumn
pwrMtrRtPhaseVoltageLL = _PwrMtrRtPhaseVoltageLL_Object(
    (1, 3, 6, 1, 4, 1, 534, 8, 3, 1, 2, 2, 1, 2),
    _PwrMtrRtPhaseVoltageLL_Type()
)
pwrMtrRtPhaseVoltageLL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrMtrRtPhaseVoltageLL.setStatus("current")
if mibBuilder.loadTexts:
    pwrMtrRtPhaseVoltageLL.setUnits("Volts")
_PwrMtrRtPhaseVoltageLN_Type = NonNegativeInteger
_PwrMtrRtPhaseVoltageLN_Object = MibTableColumn
pwrMtrRtPhaseVoltageLN = _PwrMtrRtPhaseVoltageLN_Object(
    (1, 3, 6, 1, 4, 1, 534, 8, 3, 1, 2, 2, 1, 3),
    _PwrMtrRtPhaseVoltageLN_Type()
)
pwrMtrRtPhaseVoltageLN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrMtrRtPhaseVoltageLN.setStatus("current")
if mibBuilder.loadTexts:
    pwrMtrRtPhaseVoltageLN.setUnits("Volts")
_PwrMtrRtPhaseCurrent_Type = NonNegativeInteger
_PwrMtrRtPhaseCurrent_Object = MibTableColumn
pwrMtrRtPhaseCurrent = _PwrMtrRtPhaseCurrent_Object(
    (1, 3, 6, 1, 4, 1, 534, 8, 3, 1, 2, 2, 1, 4),
    _PwrMtrRtPhaseCurrent_Type()
)
pwrMtrRtPhaseCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrMtrRtPhaseCurrent.setStatus("current")
if mibBuilder.loadTexts:
    pwrMtrRtPhaseCurrent.setUnits("0.1 Amps RMS")
_PwrMtrRtPhaseWatts_Type = NonNegativeInteger
_PwrMtrRtPhaseWatts_Object = MibTableColumn
pwrMtrRtPhaseWatts = _PwrMtrRtPhaseWatts_Object(
    (1, 3, 6, 1, 4, 1, 534, 8, 3, 1, 2, 2, 1, 5),
    _PwrMtrRtPhaseWatts_Type()
)
pwrMtrRtPhaseWatts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrMtrRtPhaseWatts.setStatus("current")
if mibBuilder.loadTexts:
    pwrMtrRtPhaseWatts.setUnits("watts")
_PwrMtrRtPhaseVA_Type = NonNegativeInteger
_PwrMtrRtPhaseVA_Object = MibTableColumn
pwrMtrRtPhaseVA = _PwrMtrRtPhaseVA_Object(
    (1, 3, 6, 1, 4, 1, 534, 8, 3, 1, 2, 2, 1, 6),
    _PwrMtrRtPhaseVA_Type()
)
pwrMtrRtPhaseVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrMtrRtPhaseVA.setStatus("current")
if mibBuilder.loadTexts:
    pwrMtrRtPhaseVA.setUnits("VA")
_PwrMtrRtPhaseVAR_Type = NonNegativeInteger
_PwrMtrRtPhaseVAR_Object = MibTableColumn
pwrMtrRtPhaseVAR = _PwrMtrRtPhaseVAR_Object(
    (1, 3, 6, 1, 4, 1, 534, 8, 3, 1, 2, 2, 1, 7),
    _PwrMtrRtPhaseVAR_Type()
)
pwrMtrRtPhaseVAR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrMtrRtPhaseVAR.setStatus("current")
if mibBuilder.loadTexts:
    pwrMtrRtPhaseVAR.setUnits("var")
_PwrMtrRtPhasePowerFactor_Type = PowerFactorInteger
_PwrMtrRtPhasePowerFactor_Object = MibTableColumn
pwrMtrRtPhasePowerFactor = _PwrMtrRtPhasePowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 534, 8, 3, 1, 2, 2, 1, 8),
    _PwrMtrRtPhasePowerFactor_Type()
)
pwrMtrRtPhasePowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrMtrRtPhasePowerFactor.setStatus("current")
if mibBuilder.loadTexts:
    pwrMtrRtPhasePowerFactor.setUnits("PF x100")
_PwrMeterMinAvgMax_ObjectIdentity = ObjectIdentity
pwrMeterMinAvgMax = _PwrMeterMinAvgMax_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 8, 3, 1, 3)
)
_PwrMeterMinAvgMaxTable_Object = MibTable
pwrMeterMinAvgMaxTable = _PwrMeterMinAvgMaxTable_Object(
    (1, 3, 6, 1, 4, 1, 534, 8, 3, 1, 3, 1)
)
if mibBuilder.loadTexts:
    pwrMeterMinAvgMaxTable.setStatus("current")
_PwrMeterMinAvgMaxEntry_Object = MibTableRow
pwrMeterMinAvgMaxEntry = _PwrMeterMinAvgMaxEntry_Object(
    (1, 3, 6, 1, 4, 1, 534, 8, 3, 1, 3, 1, 1)
)
pwrMeterMinAvgMaxEntry.setIndexNames(
    (0, "EATON-PWR-MTR-MIB", "powerMeterIndex"),
    (0, "EATON-PWR-MTR-MIB", "pwrMtrMinAvgMaxIndexTag"),
)
if mibBuilder.loadTexts:
    pwrMeterMinAvgMaxEntry.setStatus("current")


class _PwrMtrMinAvgMaxIndexTag_Type(SnmpAdminString):
    """Custom type pwrMtrMinAvgMaxIndexTag based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_PwrMtrMinAvgMaxIndexTag_Type.__name__ = "SnmpAdminString"
_PwrMtrMinAvgMaxIndexTag_Object = MibTableColumn
pwrMtrMinAvgMaxIndexTag = _PwrMtrMinAvgMaxIndexTag_Object(
    (1, 3, 6, 1, 4, 1, 534, 8, 3, 1, 3, 1, 1, 1),
    _PwrMtrMinAvgMaxIndexTag_Type()
)
pwrMtrMinAvgMaxIndexTag.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pwrMtrMinAvgMaxIndexTag.setStatus("current")
_PwrMtrMinAvgMaxVoltageLN_Type = NonNegativeInteger
_PwrMtrMinAvgMaxVoltageLN_Object = MibTableColumn
pwrMtrMinAvgMaxVoltageLN = _PwrMtrMinAvgMaxVoltageLN_Object(
    (1, 3, 6, 1, 4, 1, 534, 8, 3, 1, 3, 1, 1, 2),
    _PwrMtrMinAvgMaxVoltageLN_Type()
)
pwrMtrMinAvgMaxVoltageLN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrMtrMinAvgMaxVoltageLN.setStatus("current")
if mibBuilder.loadTexts:
    pwrMtrMinAvgMaxVoltageLN.setUnits("Volts")
_PwrMtrMinAvgMaxLineCurrent_Type = NonNegativeInteger
_PwrMtrMinAvgMaxLineCurrent_Object = MibTableColumn
pwrMtrMinAvgMaxLineCurrent = _PwrMtrMinAvgMaxLineCurrent_Object(
    (1, 3, 6, 1, 4, 1, 534, 8, 3, 1, 3, 1, 1, 3),
    _PwrMtrMinAvgMaxLineCurrent_Type()
)
pwrMtrMinAvgMaxLineCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrMtrMinAvgMaxLineCurrent.setStatus("current")
if mibBuilder.loadTexts:
    pwrMtrMinAvgMaxLineCurrent.setUnits("0.1 Amps RMS")
_PwrMtrMinAvgMaxNeutralCurrent_Type = NonNegativeInteger
_PwrMtrMinAvgMaxNeutralCurrent_Object = MibTableColumn
pwrMtrMinAvgMaxNeutralCurrent = _PwrMtrMinAvgMaxNeutralCurrent_Object(
    (1, 3, 6, 1, 4, 1, 534, 8, 3, 1, 3, 1, 1, 4),
    _PwrMtrMinAvgMaxNeutralCurrent_Type()
)
pwrMtrMinAvgMaxNeutralCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrMtrMinAvgMaxNeutralCurrent.setStatus("current")
if mibBuilder.loadTexts:
    pwrMtrMinAvgMaxNeutralCurrent.setUnits("0.1 Amps RMS")
_PwrMtrMinAvgMaxFrequency_Type = NonNegativeInteger
_PwrMtrMinAvgMaxFrequency_Object = MibTableColumn
pwrMtrMinAvgMaxFrequency = _PwrMtrMinAvgMaxFrequency_Object(
    (1, 3, 6, 1, 4, 1, 534, 8, 3, 1, 3, 1, 1, 5),
    _PwrMtrMinAvgMaxFrequency_Type()
)
pwrMtrMinAvgMaxFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrMtrMinAvgMaxFrequency.setStatus("current")
if mibBuilder.loadTexts:
    pwrMtrMinAvgMaxFrequency.setUnits("0.01 Hertz")
_PwrMtrMinAvgMaxPowerFactor_Type = PowerFactorInteger
_PwrMtrMinAvgMaxPowerFactor_Object = MibTableColumn
pwrMtrMinAvgMaxPowerFactor = _PwrMtrMinAvgMaxPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 534, 8, 3, 1, 3, 1, 1, 6),
    _PwrMtrMinAvgMaxPowerFactor_Type()
)
pwrMtrMinAvgMaxPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrMtrMinAvgMaxPowerFactor.setStatus("current")
if mibBuilder.loadTexts:
    pwrMtrMinAvgMaxPowerFactor.setUnits("PF x100")
_PwrMeterEnergyMeasures_ObjectIdentity = ObjectIdentity
pwrMeterEnergyMeasures = _PwrMeterEnergyMeasures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 8, 3, 1, 4)
)
_PwrMeterEnergyMeasuresTable_Object = MibTable
pwrMeterEnergyMeasuresTable = _PwrMeterEnergyMeasuresTable_Object(
    (1, 3, 6, 1, 4, 1, 534, 8, 3, 1, 4, 1)
)
if mibBuilder.loadTexts:
    pwrMeterEnergyMeasuresTable.setStatus("current")
_PwrMeterEnergyMeasuresEntry_Object = MibTableRow
pwrMeterEnergyMeasuresEntry = _PwrMeterEnergyMeasuresEntry_Object(
    (1, 3, 6, 1, 4, 1, 534, 8, 3, 1, 4, 1, 1)
)
pwrMeterEnergyMeasuresEntry.setIndexNames(
    (0, "EATON-PWR-MTR-MIB", "powerMeterIndex"),
)
if mibBuilder.loadTexts:
    pwrMeterEnergyMeasuresEntry.setStatus("current")
_PwrMtrEnergyKiloWattHours_Type = Integer32
_PwrMtrEnergyKiloWattHours_Object = MibTableColumn
pwrMtrEnergyKiloWattHours = _PwrMtrEnergyKiloWattHours_Object(
    (1, 3, 6, 1, 4, 1, 534, 8, 3, 1, 4, 1, 1, 1),
    _PwrMtrEnergyKiloWattHours_Type()
)
pwrMtrEnergyKiloWattHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrMtrEnergyKiloWattHours.setStatus("current")
if mibBuilder.loadTexts:
    pwrMtrEnergyKiloWattHours.setUnits("kWh")
_PwrMtrEnergyKiloVAHours_Type = NonNegativeInteger
_PwrMtrEnergyKiloVAHours_Object = MibTableColumn
pwrMtrEnergyKiloVAHours = _PwrMtrEnergyKiloVAHours_Object(
    (1, 3, 6, 1, 4, 1, 534, 8, 3, 1, 4, 1, 1, 2),
    _PwrMtrEnergyKiloVAHours_Type()
)
pwrMtrEnergyKiloVAHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrMtrEnergyKiloVAHours.setStatus("current")
if mibBuilder.loadTexts:
    pwrMtrEnergyKiloVAHours.setUnits("kVAh")
_PwrMtrEnergyKiloVARHours_Type = Integer32
_PwrMtrEnergyKiloVARHours_Object = MibTableColumn
pwrMtrEnergyKiloVARHours = _PwrMtrEnergyKiloVARHours_Object(
    (1, 3, 6, 1, 4, 1, 534, 8, 3, 1, 4, 1, 1, 3),
    _PwrMtrEnergyKiloVARHours_Type()
)
pwrMtrEnergyKiloVARHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrMtrEnergyKiloVARHours.setStatus("current")
if mibBuilder.loadTexts:
    pwrMtrEnergyKiloVARHours.setUnits("kvarh")
_PwrMtrLastEnergyReset_Type = DisplayString
_PwrMtrLastEnergyReset_Object = MibTableColumn
pwrMtrLastEnergyReset = _PwrMtrLastEnergyReset_Object(
    (1, 3, 6, 1, 4, 1, 534, 8, 3, 1, 4, 1, 1, 4),
    _PwrMtrLastEnergyReset_Type()
)
pwrMtrLastEnergyReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrMtrLastEnergyReset.setStatus("current")
_PwrMeterDemandMeasures_ObjectIdentity = ObjectIdentity
pwrMeterDemandMeasures = _PwrMeterDemandMeasures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 8, 3, 1, 5)
)
_PwrMeterDemandMeasuresTable_Object = MibTable
pwrMeterDemandMeasuresTable = _PwrMeterDemandMeasuresTable_Object(
    (1, 3, 6, 1, 4, 1, 534, 8, 3, 1, 5, 1)
)
if mibBuilder.loadTexts:
    pwrMeterDemandMeasuresTable.setStatus("current")
_PwrMeterDemandMeasuresEntry_Object = MibTableRow
pwrMeterDemandMeasuresEntry = _PwrMeterDemandMeasuresEntry_Object(
    (1, 3, 6, 1, 4, 1, 534, 8, 3, 1, 5, 1, 1)
)
pwrMeterDemandMeasuresEntry.setIndexNames(
    (0, "EATON-PWR-MTR-MIB", "powerMeterIndex"),
)
if mibBuilder.loadTexts:
    pwrMeterDemandMeasuresEntry.setStatus("current")


class _PwrMtrDemandIntervalType_Type(Integer32):
    """Custom type pwrMtrDemandIntervalType based on Integer32"""
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
        *(("fixed", 1),
          ("sliding", 2),
          ("sync", 3),
          ("unknown", 4))
    )


_PwrMtrDemandIntervalType_Type.__name__ = "Integer32"
_PwrMtrDemandIntervalType_Object = MibTableColumn
pwrMtrDemandIntervalType = _PwrMtrDemandIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 534, 8, 3, 1, 5, 1, 1, 1),
    _PwrMtrDemandIntervalType_Type()
)
pwrMtrDemandIntervalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrMtrDemandIntervalType.setStatus("current")
_PwrMtrDemandInterval_Type = NonNegativeInteger
_PwrMtrDemandInterval_Object = MibTableColumn
pwrMtrDemandInterval = _PwrMtrDemandInterval_Object(
    (1, 3, 6, 1, 4, 1, 534, 8, 3, 1, 5, 1, 1, 2),
    _PwrMtrDemandInterval_Type()
)
pwrMtrDemandInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrMtrDemandInterval.setStatus("current")
if mibBuilder.loadTexts:
    pwrMtrDemandInterval.setUnits("minutes")
_PwrMtrDemandSubinterval_Type = NonNegativeInteger
_PwrMtrDemandSubinterval_Object = MibTableColumn
pwrMtrDemandSubinterval = _PwrMtrDemandSubinterval_Object(
    (1, 3, 6, 1, 4, 1, 534, 8, 3, 1, 5, 1, 1, 3),
    _PwrMtrDemandSubinterval_Type()
)
pwrMtrDemandSubinterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrMtrDemandSubinterval.setStatus("current")
if mibBuilder.loadTexts:
    pwrMtrDemandSubinterval.setUnits("minutes")
_PwrMtrDemandKiloWatts_Type = Integer32
_PwrMtrDemandKiloWatts_Object = MibTableColumn
pwrMtrDemandKiloWatts = _PwrMtrDemandKiloWatts_Object(
    (1, 3, 6, 1, 4, 1, 534, 8, 3, 1, 5, 1, 1, 4),
    _PwrMtrDemandKiloWatts_Type()
)
pwrMtrDemandKiloWatts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrMtrDemandKiloWatts.setStatus("current")
if mibBuilder.loadTexts:
    pwrMtrDemandKiloWatts.setUnits("kilo-watts")
_PwrMtrPeakDemandKiloWatts_Type = Integer32
_PwrMtrPeakDemandKiloWatts_Object = MibTableColumn
pwrMtrPeakDemandKiloWatts = _PwrMtrPeakDemandKiloWatts_Object(
    (1, 3, 6, 1, 4, 1, 534, 8, 3, 1, 5, 1, 1, 5),
    _PwrMtrPeakDemandKiloWatts_Type()
)
pwrMtrPeakDemandKiloWatts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrMtrPeakDemandKiloWatts.setStatus("current")
if mibBuilder.loadTexts:
    pwrMtrPeakDemandKiloWatts.setUnits("kilo-watts")
_PwrMtrDemandKVA_Type = NonNegativeInteger
_PwrMtrDemandKVA_Object = MibTableColumn
pwrMtrDemandKVA = _PwrMtrDemandKVA_Object(
    (1, 3, 6, 1, 4, 1, 534, 8, 3, 1, 5, 1, 1, 6),
    _PwrMtrDemandKVA_Type()
)
pwrMtrDemandKVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrMtrDemandKVA.setStatus("current")
if mibBuilder.loadTexts:
    pwrMtrDemandKVA.setUnits("KVA")
_PwrMtrPeakDemandKVA_Type = NonNegativeInteger
_PwrMtrPeakDemandKVA_Object = MibTableColumn
pwrMtrPeakDemandKVA = _PwrMtrPeakDemandKVA_Object(
    (1, 3, 6, 1, 4, 1, 534, 8, 3, 1, 5, 1, 1, 7),
    _PwrMtrPeakDemandKVA_Type()
)
pwrMtrPeakDemandKVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrMtrPeakDemandKVA.setStatus("current")
if mibBuilder.loadTexts:
    pwrMtrPeakDemandKVA.setUnits("KVA")
_PwrMtrDemandKVAR_Type = Integer32
_PwrMtrDemandKVAR_Object = MibTableColumn
pwrMtrDemandKVAR = _PwrMtrDemandKVAR_Object(
    (1, 3, 6, 1, 4, 1, 534, 8, 3, 1, 5, 1, 1, 8),
    _PwrMtrDemandKVAR_Type()
)
pwrMtrDemandKVAR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrMtrDemandKVAR.setStatus("current")
if mibBuilder.loadTexts:
    pwrMtrDemandKVAR.setUnits("kvar")
_PwrMtrPeakDemandKVAR_Type = Integer32
_PwrMtrPeakDemandKVAR_Object = MibTableColumn
pwrMtrPeakDemandKVAR = _PwrMtrPeakDemandKVAR_Object(
    (1, 3, 6, 1, 4, 1, 534, 8, 3, 1, 5, 1, 1, 9),
    _PwrMtrPeakDemandKVAR_Type()
)
pwrMtrPeakDemandKVAR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrMtrPeakDemandKVAR.setStatus("current")
if mibBuilder.loadTexts:
    pwrMtrPeakDemandKVAR.setUnits("kvar")
_PwrMtrLastPeakDemandReset_Type = DisplayString
_PwrMtrLastPeakDemandReset_Object = MibTableColumn
pwrMtrLastPeakDemandReset = _PwrMtrLastPeakDemandReset_Object(
    (1, 3, 6, 1, 4, 1, 534, 8, 3, 1, 5, 1, 1, 10),
    _PwrMtrLastPeakDemandReset_Type()
)
pwrMtrLastPeakDemandReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrMtrLastPeakDemandReset.setStatus("current")
_PwrMeterConformance_ObjectIdentity = ObjectIdentity
pwrMeterConformance = _PwrMeterConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 8, 3, 2)
)

# Managed Objects groups

mtrPowerQualityMeasuresRow = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 534, 8, 3, 2, 1)
)
mtrPowerQualityMeasuresRow.setObjects(
      *(("EATON-PWR-MTR-MIB", "mtrPresentPowerQualityIndex"),
        ("EATON-PWR-MTR-MIB", "mtr24hourPowerQualityIndex"),
        ("EATON-PWR-MTR-MIB", "mtrPQVoltageTHD"),
        ("EATON-PWR-MTR-MIB", "mtrPQCurrentTDD"),
        ("EATON-PWR-MTR-MIB", "mtrPQLastSagSurgeReset"))
)
if mibBuilder.loadTexts:
    mtrPowerQualityMeasuresRow.setStatus("current")

mtrPQSagSurgeRow = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 534, 8, 3, 2, 2)
)
mtrPQSagSurgeRow.setObjects(
      *(("EATON-PWR-MTR-MIB", "mtrPQSagSurgeLevel"),
        ("EATON-PWR-MTR-MIB", "mtrPQSagCount"),
        ("EATON-PWR-MTR-MIB", "mtrPQSurgeCount"))
)
if mibBuilder.loadTexts:
    mtrPQSagSurgeRow.setStatus("current")

pwrMeterRtMeasuresRow = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 534, 8, 3, 2, 3)
)
pwrMeterRtMeasuresRow.setObjects(
      *(("EATON-PWR-MTR-MIB", "pwrMtrRtNeutralCurrent"),
        ("EATON-PWR-MTR-MIB", "pwrMtrRtGroundCurrent"),
        ("EATON-PWR-MTR-MIB", "pwrMtrRtTotalWatts"),
        ("EATON-PWR-MTR-MIB", "pwrMtrRtTotalVA"),
        ("EATON-PWR-MTR-MIB", "pwrMtrRtTotalVAR"),
        ("EATON-PWR-MTR-MIB", "pwrMtrRtPowerFactor"),
        ("EATON-PWR-MTR-MIB", "pwrMtrRtFrequency"),
        ("EATON-PWR-MTR-MIB", "pwrMtrRtBtuPerHour"))
)
if mibBuilder.loadTexts:
    pwrMeterRtMeasuresRow.setStatus("current")

pwrMeterRtPhaseMeasuresRow = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 534, 8, 3, 2, 4)
)
pwrMeterRtPhaseMeasuresRow.setObjects(
      *(("EATON-PWR-MTR-MIB", "pwrMtrRtPhaseVoltageLL"),
        ("EATON-PWR-MTR-MIB", "pwrMtrRtPhaseVoltageLN"),
        ("EATON-PWR-MTR-MIB", "pwrMtrRtPhaseCurrent"),
        ("EATON-PWR-MTR-MIB", "pwrMtrRtPhaseWatts"),
        ("EATON-PWR-MTR-MIB", "pwrMtrRtPhaseVA"),
        ("EATON-PWR-MTR-MIB", "pwrMtrRtPhaseVAR"),
        ("EATON-PWR-MTR-MIB", "pwrMtrRtPhasePowerFactor"))
)
if mibBuilder.loadTexts:
    pwrMeterRtPhaseMeasuresRow.setStatus("current")

pwrMeterMinAvgMaxRow = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 534, 8, 3, 2, 5)
)
pwrMeterMinAvgMaxRow.setObjects(
      *(("EATON-PWR-MTR-MIB", "pwrMtrMinAvgMaxVoltageLN"),
        ("EATON-PWR-MTR-MIB", "pwrMtrMinAvgMaxLineCurrent"),
        ("EATON-PWR-MTR-MIB", "pwrMtrMinAvgMaxNeutralCurrent"),
        ("EATON-PWR-MTR-MIB", "pwrMtrMinAvgMaxFrequency"),
        ("EATON-PWR-MTR-MIB", "pwrMtrMinAvgMaxPowerFactor"))
)
if mibBuilder.loadTexts:
    pwrMeterMinAvgMaxRow.setStatus("current")

pwrMeterEnergyMeasuresRow = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 534, 8, 3, 2, 6)
)
pwrMeterEnergyMeasuresRow.setObjects(
      *(("EATON-PWR-MTR-MIB", "pwrMtrEnergyKiloWattHours"),
        ("EATON-PWR-MTR-MIB", "pwrMtrEnergyKiloVAHours"),
        ("EATON-PWR-MTR-MIB", "pwrMtrEnergyKiloVARHours"),
        ("EATON-PWR-MTR-MIB", "pwrMtrLastEnergyReset"))
)
if mibBuilder.loadTexts:
    pwrMeterEnergyMeasuresRow.setStatus("current")

pwrMeterDemandMeasuresRow = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 534, 8, 3, 2, 7)
)
pwrMeterDemandMeasuresRow.setObjects(
      *(("EATON-PWR-MTR-MIB", "pwrMtrDemandIntervalType"),
        ("EATON-PWR-MTR-MIB", "pwrMtrDemandInterval"),
        ("EATON-PWR-MTR-MIB", "pwrMtrDemandSubinterval"),
        ("EATON-PWR-MTR-MIB", "pwrMtrDemandKiloWatts"),
        ("EATON-PWR-MTR-MIB", "pwrMtrPeakDemandKiloWatts"),
        ("EATON-PWR-MTR-MIB", "pwrMtrDemandKVA"),
        ("EATON-PWR-MTR-MIB", "pwrMtrPeakDemandKVA"),
        ("EATON-PWR-MTR-MIB", "pwrMtrDemandKVAR"),
        ("EATON-PWR-MTR-MIB", "pwrMtrPeakDemandKVAR"),
        ("EATON-PWR-MTR-MIB", "pwrMtrLastPeakDemandReset"))
)
if mibBuilder.loadTexts:
    pwrMeterDemandMeasuresRow.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

mtrPowerQualityMeasuresCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 534, 8, 3, 2, 11)
)
mtrPowerQualityMeasuresCompliance.setObjects(
      *(("EATON-PWR-MTR-MIB", "mtrPowerQualityMeasuresRow"),
        ("EATON-PWR-MTR-MIB", "mtrPQSagSurgeRow"))
)
if mibBuilder.loadTexts:
    mtrPowerQualityMeasuresCompliance.setStatus(
        "current"
    )

pwrMeterRtMeasuresCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 534, 8, 3, 2, 12)
)
pwrMeterRtMeasuresCompliance.setObjects(
      *(("EATON-PWR-MTR-MIB", "pwrMeterRtMeasuresRow"),
        ("EATON-PWR-MTR-MIB", "pwrMeterRtPhaseMeasuresRow"))
)
if mibBuilder.loadTexts:
    pwrMeterRtMeasuresCompliance.setStatus(
        "current"
    )

pwrMeterMinAvgMaxCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 534, 8, 3, 2, 13)
)
pwrMeterMinAvgMaxCompliance.setObjects(
    ("EATON-PWR-MTR-MIB", "pwrMeterMinAvgMaxRow")
)
if mibBuilder.loadTexts:
    pwrMeterMinAvgMaxCompliance.setStatus(
        "current"
    )

pwrMeterEnergyMeasuresCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 534, 8, 3, 2, 14)
)
pwrMeterEnergyMeasuresCompliance.setObjects(
    ("EATON-PWR-MTR-MIB", "pwrMeterEnergyMeasuresRow")
)
if mibBuilder.loadTexts:
    pwrMeterEnergyMeasuresCompliance.setStatus(
        "current"
    )

pwrMeterDemandMeasuresCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 534, 8, 3, 2, 15)
)
pwrMeterDemandMeasuresCompliance.setObjects(
    ("EATON-PWR-MTR-MIB", "pwrMeterDemandMeasuresRow")
)
if mibBuilder.loadTexts:
    pwrMeterDemandMeasuresCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EATON-PWR-MTR-MIB",
    **{"EatonPowerQualityIndex": EatonPowerQualityIndex,
       "PowerFactorInteger": PowerFactorInteger,
       "pwrMeterMIB": pwrMeterMIB,
       "pwrMeterMIBObjects": pwrMeterMIBObjects,
       "mtrPowerQualityMeasures": mtrPowerQualityMeasures,
       "mtrPowerQualityMeasuresTable": mtrPowerQualityMeasuresTable,
       "mtrPowerQualityMeasuresEntry": mtrPowerQualityMeasuresEntry,
       "powerMeterIndex": powerMeterIndex,
       "mtrPresentPowerQualityIndex": mtrPresentPowerQualityIndex,
       "mtr24hourPowerQualityIndex": mtr24hourPowerQualityIndex,
       "mtrPQVoltageTHD": mtrPQVoltageTHD,
       "mtrPQCurrentTDD": mtrPQCurrentTDD,
       "mtrPQLastSagSurgeReset": mtrPQLastSagSurgeReset,
       "mtrPQSagSurgeTable": mtrPQSagSurgeTable,
       "mtrPQSagSurgeEntry": mtrPQSagSurgeEntry,
       "mtrPQSagSurgeIndex": mtrPQSagSurgeIndex,
       "mtrPQSagSurgeLevel": mtrPQSagSurgeLevel,
       "mtrPQSagCount": mtrPQSagCount,
       "mtrPQSurgeCount": mtrPQSurgeCount,
       "pwrMeterRealTimeMeasures": pwrMeterRealTimeMeasures,
       "pwrMeterRtMeasuresTable": pwrMeterRtMeasuresTable,
       "pwrMeterRtMeasuresEntry": pwrMeterRtMeasuresEntry,
       "pwrMtrRtNeutralCurrent": pwrMtrRtNeutralCurrent,
       "pwrMtrRtGroundCurrent": pwrMtrRtGroundCurrent,
       "pwrMtrRtTotalWatts": pwrMtrRtTotalWatts,
       "pwrMtrRtTotalVA": pwrMtrRtTotalVA,
       "pwrMtrRtTotalVAR": pwrMtrRtTotalVAR,
       "pwrMtrRtPowerFactor": pwrMtrRtPowerFactor,
       "pwrMtrRtFrequency": pwrMtrRtFrequency,
       "pwrMtrRtBtuPerHour": pwrMtrRtBtuPerHour,
       "pwrMeterRtPhaseMeasuresTable": pwrMeterRtPhaseMeasuresTable,
       "pwrMeterRtPhaseMeasuresEntry": pwrMeterRtPhaseMeasuresEntry,
       "pwrMtrPhaseIndex": pwrMtrPhaseIndex,
       "pwrMtrRtPhaseVoltageLL": pwrMtrRtPhaseVoltageLL,
       "pwrMtrRtPhaseVoltageLN": pwrMtrRtPhaseVoltageLN,
       "pwrMtrRtPhaseCurrent": pwrMtrRtPhaseCurrent,
       "pwrMtrRtPhaseWatts": pwrMtrRtPhaseWatts,
       "pwrMtrRtPhaseVA": pwrMtrRtPhaseVA,
       "pwrMtrRtPhaseVAR": pwrMtrRtPhaseVAR,
       "pwrMtrRtPhasePowerFactor": pwrMtrRtPhasePowerFactor,
       "pwrMeterMinAvgMax": pwrMeterMinAvgMax,
       "pwrMeterMinAvgMaxTable": pwrMeterMinAvgMaxTable,
       "pwrMeterMinAvgMaxEntry": pwrMeterMinAvgMaxEntry,
       "pwrMtrMinAvgMaxIndexTag": pwrMtrMinAvgMaxIndexTag,
       "pwrMtrMinAvgMaxVoltageLN": pwrMtrMinAvgMaxVoltageLN,
       "pwrMtrMinAvgMaxLineCurrent": pwrMtrMinAvgMaxLineCurrent,
       "pwrMtrMinAvgMaxNeutralCurrent": pwrMtrMinAvgMaxNeutralCurrent,
       "pwrMtrMinAvgMaxFrequency": pwrMtrMinAvgMaxFrequency,
       "pwrMtrMinAvgMaxPowerFactor": pwrMtrMinAvgMaxPowerFactor,
       "pwrMeterEnergyMeasures": pwrMeterEnergyMeasures,
       "pwrMeterEnergyMeasuresTable": pwrMeterEnergyMeasuresTable,
       "pwrMeterEnergyMeasuresEntry": pwrMeterEnergyMeasuresEntry,
       "pwrMtrEnergyKiloWattHours": pwrMtrEnergyKiloWattHours,
       "pwrMtrEnergyKiloVAHours": pwrMtrEnergyKiloVAHours,
       "pwrMtrEnergyKiloVARHours": pwrMtrEnergyKiloVARHours,
       "pwrMtrLastEnergyReset": pwrMtrLastEnergyReset,
       "pwrMeterDemandMeasures": pwrMeterDemandMeasures,
       "pwrMeterDemandMeasuresTable": pwrMeterDemandMeasuresTable,
       "pwrMeterDemandMeasuresEntry": pwrMeterDemandMeasuresEntry,
       "pwrMtrDemandIntervalType": pwrMtrDemandIntervalType,
       "pwrMtrDemandInterval": pwrMtrDemandInterval,
       "pwrMtrDemandSubinterval": pwrMtrDemandSubinterval,
       "pwrMtrDemandKiloWatts": pwrMtrDemandKiloWatts,
       "pwrMtrPeakDemandKiloWatts": pwrMtrPeakDemandKiloWatts,
       "pwrMtrDemandKVA": pwrMtrDemandKVA,
       "pwrMtrPeakDemandKVA": pwrMtrPeakDemandKVA,
       "pwrMtrDemandKVAR": pwrMtrDemandKVAR,
       "pwrMtrPeakDemandKVAR": pwrMtrPeakDemandKVAR,
       "pwrMtrLastPeakDemandReset": pwrMtrLastPeakDemandReset,
       "pwrMeterConformance": pwrMeterConformance,
       "mtrPowerQualityMeasuresRow": mtrPowerQualityMeasuresRow,
       "mtrPQSagSurgeRow": mtrPQSagSurgeRow,
       "pwrMeterRtMeasuresRow": pwrMeterRtMeasuresRow,
       "pwrMeterRtPhaseMeasuresRow": pwrMeterRtPhaseMeasuresRow,
       "pwrMeterMinAvgMaxRow": pwrMeterMinAvgMaxRow,
       "pwrMeterEnergyMeasuresRow": pwrMeterEnergyMeasuresRow,
       "pwrMeterDemandMeasuresRow": pwrMeterDemandMeasuresRow,
       "mtrPowerQualityMeasuresCompliance": mtrPowerQualityMeasuresCompliance,
       "pwrMeterRtMeasuresCompliance": pwrMeterRtMeasuresCompliance,
       "pwrMeterMinAvgMaxCompliance": pwrMeterMinAvgMaxCompliance,
       "pwrMeterEnergyMeasuresCompliance": pwrMeterEnergyMeasuresCompliance,
       "pwrMeterDemandMeasuresCompliance": pwrMeterDemandMeasuresCompliance}
)
