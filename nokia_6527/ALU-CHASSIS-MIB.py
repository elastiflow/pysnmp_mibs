# SNMP MIB module (ALU-CHASSIS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_6527/ALU-CHASSIS-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 17:55:46 2025
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

(aluSARConfs,
 aluSARMIBModules,
 aluSARNotifyPrefix,
 aluSARObjs) = mibBuilder.importSymbols(
    "ALU-SAR-GLOBAL-MIB",
    "aluSARConfs",
    "aluSARMIBModules",
    "aluSARNotifyPrefix",
    "aluSARObjs")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")

(TmnxDeviceState,
 TmnxHwIndex,
 TmnxPortAdminStatus,
 TmnxRefInState,
 TmnxSETSRefAlarm,
 TmnxSETSRefQualified,
 TmnxSSMQualityLevel,
 tSyncIfTimingAdmEntry,
 tmnxCardSlotNum,
 tmnxChassisIndex,
 tmnxChassisNotifyHwIndex,
 tmnxCpmCardEntry,
 tmnxHwClass,
 tmnxHwID,
 tmnxHwIndex,
 tmnxMDAEntry,
 tmnxSyncIfTimingEntry,
 tmnxSyncIfTimingNotifyAlarm,
 tmnxSyncIfTimingRef1InUse,
 tmnxSyncIfTimingRef2InUse) = mibBuilder.importSymbols(
    "TIMETRA-CHASSIS-MIB",
    "TmnxDeviceState",
    "TmnxHwIndex",
    "TmnxPortAdminStatus",
    "TmnxRefInState",
    "TmnxSETSRefAlarm",
    "TmnxSETSRefQualified",
    "TmnxSSMQualityLevel",
    "tSyncIfTimingAdmEntry",
    "tmnxCardSlotNum",
    "tmnxChassisIndex",
    "tmnxChassisNotifyHwIndex",
    "tmnxCpmCardEntry",
    "tmnxHwClass",
    "tmnxHwID",
    "tmnxHwIndex",
    "tmnxMDAEntry",
    "tmnxSyncIfTimingEntry",
    "tmnxSyncIfTimingNotifyAlarm",
    "tmnxSyncIfTimingRef1InUse",
    "tmnxSyncIfTimingRef2InUse")

(TNamedItemOrEmpty,
 TPolicyID,
 TmnxActionType) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TNamedItemOrEmpty",
    "TPolicyID",
    "TmnxActionType")


# MODULE-IDENTITY

aluChassisMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    aluChassisMIBModule.setRevisions(
        ("1908-09-17 00:00",
         "1908-01-24 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AluFamType(TextualConvention, Unsigned32):
    status = "current"


class AluExtAlarmState(TextualConvention, Integer32):
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
        *(("extAlarmStateUnknown", 1),
          ("extAlarmNotEquipped", 2),
          ("extAlarmOk", 3),
          ("extAlarmDetected", 4))
    )



class AluExtAlarmEvent(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("extAlarmSuppressed", 1),
          ("extAlarmCritical", 2),
          ("extAlarmMajor", 3),
          ("extAlarmMinor", 4),
          ("extAlarmWarning", 5),
          ("extAlarmIndeterminate", 6))
    )



class AluPlatformHwClass(TextualConvention, Integer32):
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
        *(("notApplicable", 0),
          ("fam", 1),
          ("extAlarmInput", 2))
    )



class AluHwBgDiagsState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("unknown", 1),
          ("ok", 2),
          ("faultDetected", 3),
          ("criticalFaultDetected", 4))
    )



class AluSETSRefSource(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("reference1", 1),
          ("reference2", 2),
          ("bits", 3),
          ("external", 5),
          ("noReference", 6))
    )



class AluExternalIfType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("two-mhz-square", 1),
          ("five-mhz-sine", 2),
          ("ten-mhz-sine", 3))
    )



class AluExternalInputImpedanceType(TextualConvention, Integer32):
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
        *(("high-impedance", 0),
          ("seventyfive-ohm", 1),
          ("fifty-ohm", 2))
    )



class AluSyncIfTimingIeee1588PtpType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("boundary", 1),
          ("ordinary", 2),
          ("end-to-end-transparent", 3),
          ("peer-to-peer-transparent", 4),
          ("management-node", 5))
    )



# MIB Managed Objects in the order of their OIDs

_AluHwConformance_ObjectIdentity = ObjectIdentity
aluHwConformance = _AluHwConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2)
)
_AluChassisConformance_ObjectIdentity = ObjectIdentity
aluChassisConformance = _AluChassisConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 1)
)
_AluChassisCompliances_ObjectIdentity = ObjectIdentity
aluChassisCompliances = _AluChassisCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 1, 1)
)
_AluChassisGroups_ObjectIdentity = ObjectIdentity
aluChassisGroups = _AluChassisGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 1, 2)
)
_AluSetsMIBConformance_ObjectIdentity = ObjectIdentity
aluSetsMIBConformance = _AluSetsMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 4)
)
_AluHwObjs_ObjectIdentity = ObjectIdentity
aluHwObjs = _AluHwObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2)
)
_AluChassisObjs_ObjectIdentity = ObjectIdentity
aluChassisObjs = _AluChassisObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1)
)
_AluFamTable_Object = MibTable
aluFamTable = _AluFamTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    aluFamTable.setStatus("current")
_AluFamEntry_Object = MibTableRow
aluFamEntry = _AluFamEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 1, 1)
)
aluFamEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "ALU-CHASSIS-MIB", "aluFamIndex"),
)
if mibBuilder.loadTexts:
    aluFamEntry.setStatus("current")


class _AluFamIndex_Type(Unsigned32):
    """Custom type aluFamIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_AluFamIndex_Type.__name__ = "Unsigned32"
_AluFamIndex_Object = MibTableColumn
aluFamIndex = _AluFamIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 1, 1, 1),
    _AluFamIndex_Type()
)
aluFamIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluFamIndex.setStatus("current")
_AluFamOperStatus_Type = TmnxDeviceState
_AluFamOperStatus_Object = MibTableColumn
aluFamOperStatus = _AluFamOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 1, 1, 2),
    _AluFamOperStatus_Type()
)
aluFamOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluFamOperStatus.setStatus("current")
_AluFamHwIndex_Type = TmnxHwIndex
_AluFamHwIndex_Object = MibTableColumn
aluFamHwIndex = _AluFamHwIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 1, 1, 3),
    _AluFamHwIndex_Type()
)
aluFamHwIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluFamHwIndex.setStatus("current")
_AluFamEquippedType_Type = AluFamType
_AluFamEquippedType_Object = MibTableColumn
aluFamEquippedType = _AluFamEquippedType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 1, 1, 4),
    _AluFamEquippedType_Type()
)
aluFamEquippedType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluFamEquippedType.setStatus("current")
_AluChassisExtAlarmTable_Object = MibTable
aluChassisExtAlarmTable = _AluChassisExtAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 2)
)
if mibBuilder.loadTexts:
    aluChassisExtAlarmTable.setStatus("current")
_AluChassisExtAlarmEntry_Object = MibTableRow
aluChassisExtAlarmEntry = _AluChassisExtAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 2, 1)
)
aluChassisExtAlarmEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "ALU-CHASSIS-MIB", "aluChassisExtAlarmIndex"),
)
if mibBuilder.loadTexts:
    aluChassisExtAlarmEntry.setStatus("current")


class _AluChassisExtAlarmIndex_Type(Unsigned32):
    """Custom type aluChassisExtAlarmIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_AluChassisExtAlarmIndex_Type.__name__ = "Unsigned32"
_AluChassisExtAlarmIndex_Object = MibTableColumn
aluChassisExtAlarmIndex = _AluChassisExtAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 2, 1, 1),
    _AluChassisExtAlarmIndex_Type()
)
aluChassisExtAlarmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluChassisExtAlarmIndex.setStatus("current")
_AluChassisExtAlarmState_Type = AluExtAlarmState
_AluChassisExtAlarmState_Object = MibTableColumn
aluChassisExtAlarmState = _AluChassisExtAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 2, 1, 2),
    _AluChassisExtAlarmState_Type()
)
aluChassisExtAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluChassisExtAlarmState.setStatus("current")
_AluChassisExtAlarmEvent_Type = AluExtAlarmEvent
_AluChassisExtAlarmEvent_Object = MibTableColumn
aluChassisExtAlarmEvent = _AluChassisExtAlarmEvent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 2, 1, 3),
    _AluChassisExtAlarmEvent_Type()
)
aluChassisExtAlarmEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluChassisExtAlarmEvent.setStatus("current")


class _AluChassisExtAlarmPin_Type(Unsigned32):
    """Custom type aluChassisExtAlarmPin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_AluChassisExtAlarmPin_Type.__name__ = "Unsigned32"
_AluChassisExtAlarmPin_Object = MibTableColumn
aluChassisExtAlarmPin = _AluChassisExtAlarmPin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 2, 1, 4),
    _AluChassisExtAlarmPin_Type()
)
aluChassisExtAlarmPin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluChassisExtAlarmPin.setStatus("current")
_AluExtTmnxHwTable_Object = MibTable
aluExtTmnxHwTable = _AluExtTmnxHwTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 3)
)
if mibBuilder.loadTexts:
    aluExtTmnxHwTable.setStatus("current")
_AluExtTmnxHwEntry_Object = MibTableRow
aluExtTmnxHwEntry = _AluExtTmnxHwEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 3, 1)
)
aluExtTmnxHwEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxHwIndex"),
)
if mibBuilder.loadTexts:
    aluExtTmnxHwEntry.setStatus("current")
_AluExtPlatformHwClass_Type = AluPlatformHwClass
_AluExtPlatformHwClass_Object = MibTableColumn
aluExtPlatformHwClass = _AluExtPlatformHwClass_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 3, 1, 1),
    _AluExtPlatformHwClass_Type()
)
aluExtPlatformHwClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluExtPlatformHwClass.setStatus("current")


class _AluExtHwBgDiagsState_Type(AluHwBgDiagsState):
    """Custom type aluExtHwBgDiagsState based on AluHwBgDiagsState"""
    defaultValue = 1


_AluExtHwBgDiagsState_Type.__name__ = "AluHwBgDiagsState"
_AluExtHwBgDiagsState_Object = MibTableColumn
aluExtHwBgDiagsState = _AluExtHwBgDiagsState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 3, 1, 2),
    _AluExtHwBgDiagsState_Type()
)
aluExtHwBgDiagsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluExtHwBgDiagsState.setStatus("current")
_AluExtHwBgDiagsFaultReason_Type = DisplayString
_AluExtHwBgDiagsFaultReason_Object = MibTableColumn
aluExtHwBgDiagsFaultReason = _AluExtHwBgDiagsFaultReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 3, 1, 3),
    _AluExtHwBgDiagsFaultReason_Type()
)
aluExtHwBgDiagsFaultReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluExtHwBgDiagsFaultReason.setStatus("current")
_AluExtHwMfgVariant_Type = DisplayString
_AluExtHwMfgVariant_Object = MibTableColumn
aluExtHwMfgVariant = _AluExtHwMfgVariant_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 3, 1, 4),
    _AluExtHwMfgVariant_Type()
)
aluExtHwMfgVariant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluExtHwMfgVariant.setStatus("current")
_AluExtTmnxMDATable_Object = MibTable
aluExtTmnxMDATable = _AluExtTmnxMDATable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 4)
)
if mibBuilder.loadTexts:
    aluExtTmnxMDATable.setStatus("current")
_AluExtTmnxMDAEntry_Object = MibTableRow
aluExtTmnxMDAEntry = _AluExtTmnxMDAEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 4, 1)
)
if mibBuilder.loadTexts:
    aluExtTmnxMDAEntry.setStatus("current")


class _AluExtTmnxMDANetworkIngFabricPolicy_Type(TPolicyID):
    """Custom type aluExtTmnxMDANetworkIngFabricPolicy based on TPolicyID"""
    defaultValue = 1

    subtypeSpec = TPolicyID.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_AluExtTmnxMDANetworkIngFabricPolicy_Type.__name__ = "TPolicyID"
_AluExtTmnxMDANetworkIngFabricPolicy_Object = MibTableColumn
aluExtTmnxMDANetworkIngFabricPolicy = _AluExtTmnxMDANetworkIngFabricPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 4, 1, 1),
    _AluExtTmnxMDANetworkIngFabricPolicy_Type()
)
aluExtTmnxMDANetworkIngFabricPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluExtTmnxMDANetworkIngFabricPolicy.setStatus("current")


class _AluExtTmnxMDAAccessIngFabricPolicy_Type(TPolicyID):
    """Custom type aluExtTmnxMDAAccessIngFabricPolicy based on TPolicyID"""
    defaultValue = 1

    subtypeSpec = TPolicyID.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_AluExtTmnxMDAAccessIngFabricPolicy_Type.__name__ = "TPolicyID"
_AluExtTmnxMDAAccessIngFabricPolicy_Object = MibTableColumn
aluExtTmnxMDAAccessIngFabricPolicy = _AluExtTmnxMDAAccessIngFabricPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 4, 1, 2),
    _AluExtTmnxMDAAccessIngFabricPolicy_Type()
)
aluExtTmnxMDAAccessIngFabricPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluExtTmnxMDAAccessIngFabricPolicy.setStatus("current")


class _AluExtTmnxMDAFabricStatsEnabled_Type(TruthValue):
    """Custom type aluExtTmnxMDAFabricStatsEnabled based on TruthValue"""
    defaultValue = 2


_AluExtTmnxMDAFabricStatsEnabled_Type.__name__ = "TruthValue"
_AluExtTmnxMDAFabricStatsEnabled_Object = MibTableColumn
aluExtTmnxMDAFabricStatsEnabled = _AluExtTmnxMDAFabricStatsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 4, 1, 3),
    _AluExtTmnxMDAFabricStatsEnabled_Type()
)
aluExtTmnxMDAFabricStatsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluExtTmnxMDAFabricStatsEnabled.setStatus("current")


class _AluExtTmnxMDAVoiceCompandingLaw_Type(Integer32):
    """Custom type aluExtTmnxMDAVoiceCompandingLaw based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("aLaw", 1),
          ("muLaw", 2))
    )


_AluExtTmnxMDAVoiceCompandingLaw_Type.__name__ = "Integer32"
_AluExtTmnxMDAVoiceCompandingLaw_Object = MibTableColumn
aluExtTmnxMDAVoiceCompandingLaw = _AluExtTmnxMDAVoiceCompandingLaw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 4, 1, 4),
    _AluExtTmnxMDAVoiceCompandingLaw_Type()
)
aluExtTmnxMDAVoiceCompandingLaw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluExtTmnxMDAVoiceCompandingLaw.setStatus("current")


class _AluExtTmnxMDAVoiceSignalingType_Type(Integer32):
    """Custom type aluExtTmnxMDAVoiceSignalingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("typeI", 1),
          ("typeII", 2),
          ("typeIII", 3),
          ("typeIV", 4),
          ("typeV", 5))
    )


_AluExtTmnxMDAVoiceSignalingType_Type.__name__ = "Integer32"
_AluExtTmnxMDAVoiceSignalingType_Object = MibTableColumn
aluExtTmnxMDAVoiceSignalingType = _AluExtTmnxMDAVoiceSignalingType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 4, 1, 5),
    _AluExtTmnxMDAVoiceSignalingType_Type()
)
aluExtTmnxMDAVoiceSignalingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluExtTmnxMDAVoiceSignalingType.setStatus("current")
_AluExtTmnxMDANumOfDigitalAlarmInputs_Type = Integer32
_AluExtTmnxMDANumOfDigitalAlarmInputs_Object = MibTableColumn
aluExtTmnxMDANumOfDigitalAlarmInputs = _AluExtTmnxMDANumOfDigitalAlarmInputs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 4, 1, 6),
    _AluExtTmnxMDANumOfDigitalAlarmInputs_Type()
)
aluExtTmnxMDANumOfDigitalAlarmInputs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluExtTmnxMDANumOfDigitalAlarmInputs.setStatus("current")
_AluExtTmnxMDANumOfAnalogAlarmInputs_Type = Integer32
_AluExtTmnxMDANumOfAnalogAlarmInputs_Object = MibTableColumn
aluExtTmnxMDANumOfAnalogAlarmInputs = _AluExtTmnxMDANumOfAnalogAlarmInputs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 4, 1, 7),
    _AluExtTmnxMDANumOfAnalogAlarmInputs_Type()
)
aluExtTmnxMDANumOfAnalogAlarmInputs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluExtTmnxMDANumOfAnalogAlarmInputs.setStatus("current")
_AluExtTmnxMDANumOfDigitalOutputRelays_Type = Integer32
_AluExtTmnxMDANumOfDigitalOutputRelays_Object = MibTableColumn
aluExtTmnxMDANumOfDigitalOutputRelays = _AluExtTmnxMDANumOfDigitalOutputRelays_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 4, 1, 8),
    _AluExtTmnxMDANumOfDigitalOutputRelays_Type()
)
aluExtTmnxMDANumOfDigitalOutputRelays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluExtTmnxMDANumOfDigitalOutputRelays.setStatus("current")


class _AluExtTmnxMDACapabilityMode_Type(Integer32):
    """Custom type aluExtTmnxMDACapabilityMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("modeA", 1),
          ("modeB", 2),
          ("modeC", 3))
    )


_AluExtTmnxMDACapabilityMode_Type.__name__ = "Integer32"
_AluExtTmnxMDACapabilityMode_Object = MibTableColumn
aluExtTmnxMDACapabilityMode = _AluExtTmnxMDACapabilityMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 4, 1, 9),
    _AluExtTmnxMDACapabilityMode_Type()
)
aluExtTmnxMDACapabilityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluExtTmnxMDACapabilityMode.setStatus("current")
_AluFabricDeviceStatsTable_Object = MibTable
aluFabricDeviceStatsTable = _AluFabricDeviceStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 5)
)
if mibBuilder.loadTexts:
    aluFabricDeviceStatsTable.setStatus("current")
_AluFabricDeviceStatsEntry_Object = MibTableRow
aluFabricDeviceStatsEntry = _AluFabricDeviceStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 5, 1)
)
aluFabricDeviceStatsEntry.setIndexNames(
    (0, "ALU-CHASSIS-MIB", "aluFabricDeviceStatsIndex"),
)
if mibBuilder.loadTexts:
    aluFabricDeviceStatsEntry.setStatus("current")
_AluFabricDeviceStatsIndex_Type = Unsigned32
_AluFabricDeviceStatsIndex_Object = MibTableColumn
aluFabricDeviceStatsIndex = _AluFabricDeviceStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 5, 1, 1),
    _AluFabricDeviceStatsIndex_Type()
)
aluFabricDeviceStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluFabricDeviceStatsIndex.setStatus("current")
_AluFabricDeviceStatsFwdPkts_Type = Counter64
_AluFabricDeviceStatsFwdPkts_Object = MibTableColumn
aluFabricDeviceStatsFwdPkts = _AluFabricDeviceStatsFwdPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 5, 1, 2),
    _AluFabricDeviceStatsFwdPkts_Type()
)
aluFabricDeviceStatsFwdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluFabricDeviceStatsFwdPkts.setStatus("current")
_AluFabricDeviceStatsDroPkts_Type = Counter64
_AluFabricDeviceStatsDroPkts_Object = MibTableColumn
aluFabricDeviceStatsDroPkts = _AluFabricDeviceStatsDroPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 5, 1, 3),
    _AluFabricDeviceStatsDroPkts_Type()
)
aluFabricDeviceStatsDroPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluFabricDeviceStatsDroPkts.setStatus("current")
_AluFabricDeviceStatsFwdOcts_Type = Counter64
_AluFabricDeviceStatsFwdOcts_Object = MibTableColumn
aluFabricDeviceStatsFwdOcts = _AluFabricDeviceStatsFwdOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 5, 1, 4),
    _AluFabricDeviceStatsFwdOcts_Type()
)
aluFabricDeviceStatsFwdOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluFabricDeviceStatsFwdOcts.setStatus("current")
_AluFabricDeviceStatsUcastFwdPkts_Type = Counter64
_AluFabricDeviceStatsUcastFwdPkts_Object = MibTableColumn
aluFabricDeviceStatsUcastFwdPkts = _AluFabricDeviceStatsUcastFwdPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 5, 1, 5),
    _AluFabricDeviceStatsUcastFwdPkts_Type()
)
aluFabricDeviceStatsUcastFwdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluFabricDeviceStatsUcastFwdPkts.setStatus("current")
_AluFabricDeviceStatsMcastFwdPkts_Type = Counter64
_AluFabricDeviceStatsMcastFwdPkts_Object = MibTableColumn
aluFabricDeviceStatsMcastFwdPkts = _AluFabricDeviceStatsMcastFwdPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 5, 1, 6),
    _AluFabricDeviceStatsMcastFwdPkts_Type()
)
aluFabricDeviceStatsMcastFwdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluFabricDeviceStatsMcastFwdPkts.setStatus("current")
_AluFabricDeviceStatsDroOcts_Type = Counter64
_AluFabricDeviceStatsDroOcts_Object = MibTableColumn
aluFabricDeviceStatsDroOcts = _AluFabricDeviceStatsDroOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 5, 1, 7),
    _AluFabricDeviceStatsDroOcts_Type()
)
aluFabricDeviceStatsDroOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluFabricDeviceStatsDroOcts.setStatus("current")
_AluFabricDeviceStatsMdaDroEvents_Type = Counter64
_AluFabricDeviceStatsMdaDroEvents_Object = MibTableColumn
aluFabricDeviceStatsMdaDroEvents = _AluFabricDeviceStatsMdaDroEvents_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 5, 1, 8),
    _AluFabricDeviceStatsMdaDroEvents_Type()
)
aluFabricDeviceStatsMdaDroEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluFabricDeviceStatsMdaDroEvents.setStatus("current")
_AluSourceMDAStatsTable_Object = MibTable
aluSourceMDAStatsTable = _AluSourceMDAStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 6)
)
if mibBuilder.loadTexts:
    aluSourceMDAStatsTable.setStatus("current")
_AluSourceMDAStatsEntry_Object = MibTableRow
aluSourceMDAStatsEntry = _AluSourceMDAStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 6, 1)
)
aluSourceMDAStatsEntry.setIndexNames(
    (0, "ALU-CHASSIS-MIB", "aluSourceMDASrcMdaId"),
    (0, "ALU-CHASSIS-MIB", "aluSourceMDADestMdaId"),
)
if mibBuilder.loadTexts:
    aluSourceMDAStatsEntry.setStatus("current")
_AluSourceMDASrcMdaId_Type = Unsigned32
_AluSourceMDASrcMdaId_Object = MibTableColumn
aluSourceMDASrcMdaId = _AluSourceMDASrcMdaId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 6, 1, 1),
    _AluSourceMDASrcMdaId_Type()
)
aluSourceMDASrcMdaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluSourceMDASrcMdaId.setStatus("current")
_AluSourceMDADestMdaId_Type = Unsigned32
_AluSourceMDADestMdaId_Object = MibTableColumn
aluSourceMDADestMdaId = _AluSourceMDADestMdaId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 6, 1, 2),
    _AluSourceMDADestMdaId_Type()
)
aluSourceMDADestMdaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluSourceMDADestMdaId.setStatus("current")
_AluSourceMDAStatsFwdInProfPkts_Type = Counter64
_AluSourceMDAStatsFwdInProfPkts_Object = MibTableColumn
aluSourceMDAStatsFwdInProfPkts = _AluSourceMDAStatsFwdInProfPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 6, 1, 3),
    _AluSourceMDAStatsFwdInProfPkts_Type()
)
aluSourceMDAStatsFwdInProfPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSourceMDAStatsFwdInProfPkts.setStatus("current")
_AluSourceMDAStatsFwdOutProfPkts_Type = Counter64
_AluSourceMDAStatsFwdOutProfPkts_Object = MibTableColumn
aluSourceMDAStatsFwdOutProfPkts = _AluSourceMDAStatsFwdOutProfPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 6, 1, 4),
    _AluSourceMDAStatsFwdOutProfPkts_Type()
)
aluSourceMDAStatsFwdOutProfPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSourceMDAStatsFwdOutProfPkts.setStatus("current")
_AluSourceMDAStatsFwdInProfOcts_Type = Counter64
_AluSourceMDAStatsFwdInProfOcts_Object = MibTableColumn
aluSourceMDAStatsFwdInProfOcts = _AluSourceMDAStatsFwdInProfOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 6, 1, 5),
    _AluSourceMDAStatsFwdInProfOcts_Type()
)
aluSourceMDAStatsFwdInProfOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSourceMDAStatsFwdInProfOcts.setStatus("current")
_AluSourceMDAStatsFwdOutProfOcts_Type = Counter64
_AluSourceMDAStatsFwdOutProfOcts_Object = MibTableColumn
aluSourceMDAStatsFwdOutProfOcts = _AluSourceMDAStatsFwdOutProfOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 6, 1, 6),
    _AluSourceMDAStatsFwdOutProfOcts_Type()
)
aluSourceMDAStatsFwdOutProfOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSourceMDAStatsFwdOutProfOcts.setStatus("current")
_AluSourceMDAStatsDroInProfPkts_Type = Counter64
_AluSourceMDAStatsDroInProfPkts_Object = MibTableColumn
aluSourceMDAStatsDroInProfPkts = _AluSourceMDAStatsDroInProfPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 6, 1, 7),
    _AluSourceMDAStatsDroInProfPkts_Type()
)
aluSourceMDAStatsDroInProfPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSourceMDAStatsDroInProfPkts.setStatus("current")
_AluSourceMDAStatsDroOutProfPkts_Type = Counter64
_AluSourceMDAStatsDroOutProfPkts_Object = MibTableColumn
aluSourceMDAStatsDroOutProfPkts = _AluSourceMDAStatsDroOutProfPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 6, 1, 8),
    _AluSourceMDAStatsDroOutProfPkts_Type()
)
aluSourceMDAStatsDroOutProfPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSourceMDAStatsDroOutProfPkts.setStatus("current")
_AluSourceMDAStatsDroInProfOcts_Type = Counter64
_AluSourceMDAStatsDroInProfOcts_Object = MibTableColumn
aluSourceMDAStatsDroInProfOcts = _AluSourceMDAStatsDroInProfOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 6, 1, 9),
    _AluSourceMDAStatsDroInProfOcts_Type()
)
aluSourceMDAStatsDroInProfOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSourceMDAStatsDroInProfOcts.setStatus("current")
_AluSourceMDAStatsDroOutProfOcts_Type = Counter64
_AluSourceMDAStatsDroOutProfOcts_Object = MibTableColumn
aluSourceMDAStatsDroOutProfOcts = _AluSourceMDAStatsDroOutProfOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 6, 1, 10),
    _AluSourceMDAStatsDroOutProfOcts_Type()
)
aluSourceMDAStatsDroOutProfOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSourceMDAStatsDroOutProfOcts.setStatus("current")
_AluSourceMDAStatsAccessFwdInProfPkts_Type = Counter64
_AluSourceMDAStatsAccessFwdInProfPkts_Object = MibTableColumn
aluSourceMDAStatsAccessFwdInProfPkts = _AluSourceMDAStatsAccessFwdInProfPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 6, 1, 11),
    _AluSourceMDAStatsAccessFwdInProfPkts_Type()
)
aluSourceMDAStatsAccessFwdInProfPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSourceMDAStatsAccessFwdInProfPkts.setStatus("current")
_AluSourceMDAStatsAccessFwdOutProfPkts_Type = Counter64
_AluSourceMDAStatsAccessFwdOutProfPkts_Object = MibTableColumn
aluSourceMDAStatsAccessFwdOutProfPkts = _AluSourceMDAStatsAccessFwdOutProfPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 6, 1, 12),
    _AluSourceMDAStatsAccessFwdOutProfPkts_Type()
)
aluSourceMDAStatsAccessFwdOutProfPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSourceMDAStatsAccessFwdOutProfPkts.setStatus("current")
_AluSourceMDAStatsAccessFwdInProfOcts_Type = Counter64
_AluSourceMDAStatsAccessFwdInProfOcts_Object = MibTableColumn
aluSourceMDAStatsAccessFwdInProfOcts = _AluSourceMDAStatsAccessFwdInProfOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 6, 1, 13),
    _AluSourceMDAStatsAccessFwdInProfOcts_Type()
)
aluSourceMDAStatsAccessFwdInProfOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSourceMDAStatsAccessFwdInProfOcts.setStatus("current")
_AluSourceMDAStatsAccessFwdOutProfOcts_Type = Counter64
_AluSourceMDAStatsAccessFwdOutProfOcts_Object = MibTableColumn
aluSourceMDAStatsAccessFwdOutProfOcts = _AluSourceMDAStatsAccessFwdOutProfOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 6, 1, 14),
    _AluSourceMDAStatsAccessFwdOutProfOcts_Type()
)
aluSourceMDAStatsAccessFwdOutProfOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSourceMDAStatsAccessFwdOutProfOcts.setStatus("current")
_AluSourceMDAStatsAccessDroPkts_Type = Counter64
_AluSourceMDAStatsAccessDroPkts_Object = MibTableColumn
aluSourceMDAStatsAccessDroPkts = _AluSourceMDAStatsAccessDroPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 6, 1, 15),
    _AluSourceMDAStatsAccessDroPkts_Type()
)
aluSourceMDAStatsAccessDroPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSourceMDAStatsAccessDroPkts.setStatus("current")
_AluSourceMDAStatsAccessDroOcts_Type = Counter64
_AluSourceMDAStatsAccessDroOcts_Object = MibTableColumn
aluSourceMDAStatsAccessDroOcts = _AluSourceMDAStatsAccessDroOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 6, 1, 16),
    _AluSourceMDAStatsAccessDroOcts_Type()
)
aluSourceMDAStatsAccessDroOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSourceMDAStatsAccessDroOcts.setStatus("current")
_AluDestMDAStatsTable_Object = MibTable
aluDestMDAStatsTable = _AluDestMDAStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 7)
)
if mibBuilder.loadTexts:
    aluDestMDAStatsTable.setStatus("current")
_AluDestMDAStatsEntry_Object = MibTableRow
aluDestMDAStatsEntry = _AluDestMDAStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 7, 1)
)
aluDestMDAStatsEntry.setIndexNames(
    (0, "ALU-CHASSIS-MIB", "aluDestMDADestMdaId"),
    (0, "ALU-CHASSIS-MIB", "aluDestMDASrcMdaId"),
)
if mibBuilder.loadTexts:
    aluDestMDAStatsEntry.setStatus("current")
_AluDestMDADestMdaId_Type = Unsigned32
_AluDestMDADestMdaId_Object = MibTableColumn
aluDestMDADestMdaId = _AluDestMDADestMdaId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 7, 1, 1),
    _AluDestMDADestMdaId_Type()
)
aluDestMDADestMdaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluDestMDADestMdaId.setStatus("current")
_AluDestMDASrcMdaId_Type = Unsigned32
_AluDestMDASrcMdaId_Object = MibTableColumn
aluDestMDASrcMdaId = _AluDestMDASrcMdaId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 7, 1, 2),
    _AluDestMDASrcMdaId_Type()
)
aluDestMDASrcMdaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluDestMDASrcMdaId.setStatus("current")
_AluDestMDAStatsFwdInProfPkts_Type = Counter64
_AluDestMDAStatsFwdInProfPkts_Object = MibTableColumn
aluDestMDAStatsFwdInProfPkts = _AluDestMDAStatsFwdInProfPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 7, 1, 3),
    _AluDestMDAStatsFwdInProfPkts_Type()
)
aluDestMDAStatsFwdInProfPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluDestMDAStatsFwdInProfPkts.setStatus("current")
_AluDestMDAStatsFwdOutProfPkts_Type = Counter64
_AluDestMDAStatsFwdOutProfPkts_Object = MibTableColumn
aluDestMDAStatsFwdOutProfPkts = _AluDestMDAStatsFwdOutProfPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 7, 1, 4),
    _AluDestMDAStatsFwdOutProfPkts_Type()
)
aluDestMDAStatsFwdOutProfPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluDestMDAStatsFwdOutProfPkts.setStatus("current")
_AluDestMDAStatsFwdInProfOcts_Type = Counter64
_AluDestMDAStatsFwdInProfOcts_Object = MibTableColumn
aluDestMDAStatsFwdInProfOcts = _AluDestMDAStatsFwdInProfOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 7, 1, 5),
    _AluDestMDAStatsFwdInProfOcts_Type()
)
aluDestMDAStatsFwdInProfOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluDestMDAStatsFwdInProfOcts.setStatus("current")
_AluDestMDAStatsFwdOutProfOcts_Type = Counter64
_AluDestMDAStatsFwdOutProfOcts_Object = MibTableColumn
aluDestMDAStatsFwdOutProfOcts = _AluDestMDAStatsFwdOutProfOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 7, 1, 6),
    _AluDestMDAStatsFwdOutProfOcts_Type()
)
aluDestMDAStatsFwdOutProfOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluDestMDAStatsFwdOutProfOcts.setStatus("current")
_AluDestMDAStatsDroInProfPkts_Type = Counter64
_AluDestMDAStatsDroInProfPkts_Object = MibTableColumn
aluDestMDAStatsDroInProfPkts = _AluDestMDAStatsDroInProfPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 7, 1, 7),
    _AluDestMDAStatsDroInProfPkts_Type()
)
aluDestMDAStatsDroInProfPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluDestMDAStatsDroInProfPkts.setStatus("current")
_AluDestMDAStatsDroOutProfPkts_Type = Counter64
_AluDestMDAStatsDroOutProfPkts_Object = MibTableColumn
aluDestMDAStatsDroOutProfPkts = _AluDestMDAStatsDroOutProfPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 7, 1, 8),
    _AluDestMDAStatsDroOutProfPkts_Type()
)
aluDestMDAStatsDroOutProfPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluDestMDAStatsDroOutProfPkts.setStatus("current")
_AluDestMDAStatsDroInProfOcts_Type = Counter64
_AluDestMDAStatsDroInProfOcts_Object = MibTableColumn
aluDestMDAStatsDroInProfOcts = _AluDestMDAStatsDroInProfOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 7, 1, 9),
    _AluDestMDAStatsDroInProfOcts_Type()
)
aluDestMDAStatsDroInProfOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluDestMDAStatsDroInProfOcts.setStatus("current")
_AluDestMDAStatsDroOutProfOcts_Type = Counter64
_AluDestMDAStatsDroOutProfOcts_Object = MibTableColumn
aluDestMDAStatsDroOutProfOcts = _AluDestMDAStatsDroOutProfOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 7, 1, 10),
    _AluDestMDAStatsDroOutProfOcts_Type()
)
aluDestMDAStatsDroOutProfOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluDestMDAStatsDroOutProfOcts.setStatus("current")
_AluDestMDAStatsAccessFwdInProfPkts_Type = Counter64
_AluDestMDAStatsAccessFwdInProfPkts_Object = MibTableColumn
aluDestMDAStatsAccessFwdInProfPkts = _AluDestMDAStatsAccessFwdInProfPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 7, 1, 11),
    _AluDestMDAStatsAccessFwdInProfPkts_Type()
)
aluDestMDAStatsAccessFwdInProfPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluDestMDAStatsAccessFwdInProfPkts.setStatus("current")
_AluDestMDAStatsAccessFwdOutProfPkts_Type = Counter64
_AluDestMDAStatsAccessFwdOutProfPkts_Object = MibTableColumn
aluDestMDAStatsAccessFwdOutProfPkts = _AluDestMDAStatsAccessFwdOutProfPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 7, 1, 12),
    _AluDestMDAStatsAccessFwdOutProfPkts_Type()
)
aluDestMDAStatsAccessFwdOutProfPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluDestMDAStatsAccessFwdOutProfPkts.setStatus("current")
_AluDestMDAStatsAccessFwdInProfOcts_Type = Counter64
_AluDestMDAStatsAccessFwdInProfOcts_Object = MibTableColumn
aluDestMDAStatsAccessFwdInProfOcts = _AluDestMDAStatsAccessFwdInProfOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 7, 1, 13),
    _AluDestMDAStatsAccessFwdInProfOcts_Type()
)
aluDestMDAStatsAccessFwdInProfOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluDestMDAStatsAccessFwdInProfOcts.setStatus("current")
_AluDestMDAStatsAccessFwdOutProfOcts_Type = Counter64
_AluDestMDAStatsAccessFwdOutProfOcts_Object = MibTableColumn
aluDestMDAStatsAccessFwdOutProfOcts = _AluDestMDAStatsAccessFwdOutProfOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 7, 1, 14),
    _AluDestMDAStatsAccessFwdOutProfOcts_Type()
)
aluDestMDAStatsAccessFwdOutProfOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluDestMDAStatsAccessFwdOutProfOcts.setStatus("current")
_AluDestMDAStatsAccessDroPkts_Type = Counter64
_AluDestMDAStatsAccessDroPkts_Object = MibTableColumn
aluDestMDAStatsAccessDroPkts = _AluDestMDAStatsAccessDroPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 7, 1, 15),
    _AluDestMDAStatsAccessDroPkts_Type()
)
aluDestMDAStatsAccessDroPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluDestMDAStatsAccessDroPkts.setStatus("current")
_AluDestMDAStatsAccessDroOcts_Type = Counter64
_AluDestMDAStatsAccessDroOcts_Object = MibTableColumn
aluDestMDAStatsAccessDroOcts = _AluDestMDAStatsAccessDroOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 7, 1, 16),
    _AluDestMDAStatsAccessDroOcts_Type()
)
aluDestMDAStatsAccessDroOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluDestMDAStatsAccessDroOcts.setStatus("current")
_AluCardObjs_ObjectIdentity = ObjectIdentity
aluCardObjs = _AluCardObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 3)
)
_AluExtTmnxCpmCardTable_Object = MibTable
aluExtTmnxCpmCardTable = _AluExtTmnxCpmCardTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 3, 1)
)
if mibBuilder.loadTexts:
    aluExtTmnxCpmCardTable.setStatus("current")
_AluExtTmnxCpmCardEntry_Object = MibTableRow
aluExtTmnxCpmCardEntry = _AluExtTmnxCpmCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 3, 1, 1)
)
if mibBuilder.loadTexts:
    aluExtTmnxCpmCardEntry.setStatus("current")


class _AluExtCpmCardUpgrade_Type(TmnxActionType):
    """Custom type aluExtCpmCardUpgrade based on TmnxActionType"""
    defaultValue = 2


_AluExtCpmCardUpgrade_Type.__name__ = "TmnxActionType"
_AluExtCpmCardUpgrade_Object = MibTableColumn
aluExtCpmCardUpgrade = _AluExtCpmCardUpgrade_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 3, 1, 1, 1),
    _AluExtCpmCardUpgrade_Type()
)
aluExtCpmCardUpgrade.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluExtCpmCardUpgrade.setStatus("current")
_AluChassisNotificationObjects_ObjectIdentity = ObjectIdentity
aluChassisNotificationObjects = _AluChassisNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 6)
)
_AluChassisNotifyMdaRuntimeStatusContext_Type = DisplayString
_AluChassisNotifyMdaRuntimeStatusContext_Object = MibScalar
aluChassisNotifyMdaRuntimeStatusContext = _AluChassisNotifyMdaRuntimeStatusContext_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 6, 1),
    _AluChassisNotifyMdaRuntimeStatusContext_Type()
)
aluChassisNotifyMdaRuntimeStatusContext.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    aluChassisNotifyMdaRuntimeStatusContext.setStatus("current")
_AluSyncObjs_ObjectIdentity = ObjectIdentity
aluSyncObjs = _AluSyncObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 4)
)
_AluSyncExtensionObjs_ObjectIdentity = ObjectIdentity
aluSyncExtensionObjs = _AluSyncExtensionObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 4, 1)
)
_AluExtIfSyncIfTimingExtensionTable_Object = MibTable
aluExtIfSyncIfTimingExtensionTable = _AluExtIfSyncIfTimingExtensionTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 4, 1, 1)
)
if mibBuilder.loadTexts:
    aluExtIfSyncIfTimingExtensionTable.setStatus("current")
_AluExtIfSyncIfTimingExtensionEntry_Object = MibTableRow
aluExtIfSyncIfTimingExtensionEntry = _AluExtIfSyncIfTimingExtensionEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 4, 1, 1, 1)
)
if mibBuilder.loadTexts:
    aluExtIfSyncIfTimingExtensionEntry.setStatus("current")
_AluSyncIfTimingExternInIfType_Type = AluExternalIfType
_AluSyncIfTimingExternInIfType_Object = MibTableColumn
aluSyncIfTimingExternInIfType = _AluSyncIfTimingExternInIfType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 4, 1, 1, 1, 1),
    _AluSyncIfTimingExternInIfType_Type()
)
aluSyncIfTimingExternInIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSyncIfTimingExternInIfType.setStatus("current")
_AluSyncIfTimingExternInImpedType_Type = AluExternalInputImpedanceType
_AluSyncIfTimingExternInImpedType_Object = MibTableColumn
aluSyncIfTimingExternInImpedType = _AluSyncIfTimingExternInImpedType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 4, 1, 1, 1, 2),
    _AluSyncIfTimingExternInImpedType_Type()
)
aluSyncIfTimingExternInImpedType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSyncIfTimingExternInImpedType.setStatus("current")
_AluSyncIfTimingExternOutIfType_Type = AluExternalIfType
_AluSyncIfTimingExternOutIfType_Object = MibTableColumn
aluSyncIfTimingExternOutIfType = _AluSyncIfTimingExternOutIfType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 4, 1, 1, 1, 3),
    _AluSyncIfTimingExternOutIfType_Type()
)
aluSyncIfTimingExternOutIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSyncIfTimingExternOutIfType.setStatus("current")
_AluSyncIfTimingExternInIfAdminStatus_Type = TmnxPortAdminStatus
_AluSyncIfTimingExternInIfAdminStatus_Object = MibTableColumn
aluSyncIfTimingExternInIfAdminStatus = _AluSyncIfTimingExternInIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 4, 1, 1, 1, 4),
    _AluSyncIfTimingExternInIfAdminStatus_Type()
)
aluSyncIfTimingExternInIfAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSyncIfTimingExternInIfAdminStatus.setStatus("current")
_AluSyncIfTimingExternInIfInUse_Type = TruthValue
_AluSyncIfTimingExternInIfInUse_Object = MibTableColumn
aluSyncIfTimingExternInIfInUse = _AluSyncIfTimingExternInIfInUse_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 4, 1, 1, 1, 5),
    _AluSyncIfTimingExternInIfInUse_Type()
)
aluSyncIfTimingExternInIfInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSyncIfTimingExternInIfInUse.setStatus("current")
_AluSyncIfTimingExternInIfQualified_Type = TmnxSETSRefQualified
_AluSyncIfTimingExternInIfQualified_Object = MibTableColumn
aluSyncIfTimingExternInIfQualified = _AluSyncIfTimingExternInIfQualified_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 4, 1, 1, 1, 6),
    _AluSyncIfTimingExternInIfQualified_Type()
)
aluSyncIfTimingExternInIfQualified.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSyncIfTimingExternInIfQualified.setStatus("current")
_AluSyncIfTimingExternInIfAlarm_Type = TmnxSETSRefAlarm
_AluSyncIfTimingExternInIfAlarm_Object = MibTableColumn
aluSyncIfTimingExternInIfAlarm = _AluSyncIfTimingExternInIfAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 4, 1, 1, 1, 7),
    _AluSyncIfTimingExternInIfAlarm_Type()
)
aluSyncIfTimingExternInIfAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSyncIfTimingExternInIfAlarm.setStatus("current")
_AluSyncIfTimingRef1Ieee1588PtpSrc_Type = TNamedItemOrEmpty
_AluSyncIfTimingRef1Ieee1588PtpSrc_Object = MibTableColumn
aluSyncIfTimingRef1Ieee1588PtpSrc = _AluSyncIfTimingRef1Ieee1588PtpSrc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 4, 1, 1, 1, 8),
    _AluSyncIfTimingRef1Ieee1588PtpSrc_Type()
)
aluSyncIfTimingRef1Ieee1588PtpSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSyncIfTimingRef1Ieee1588PtpSrc.setStatus("obsolete")
_AluSyncIfTimingRef2Ieee1588PtpSrc_Type = TNamedItemOrEmpty
_AluSyncIfTimingRef2Ieee1588PtpSrc_Object = MibTableColumn
aluSyncIfTimingRef2Ieee1588PtpSrc = _AluSyncIfTimingRef2Ieee1588PtpSrc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 4, 1, 1, 1, 9),
    _AluSyncIfTimingRef2Ieee1588PtpSrc_Type()
)
aluSyncIfTimingRef2Ieee1588PtpSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSyncIfTimingRef2Ieee1588PtpSrc.setStatus("obsolete")
_AluSyncIfTimingIeee1588PtpType_Type = AluSyncIfTimingIeee1588PtpType
_AluSyncIfTimingIeee1588PtpType_Object = MibTableColumn
aluSyncIfTimingIeee1588PtpType = _AluSyncIfTimingIeee1588PtpType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 4, 1, 1, 1, 10),
    _AluSyncIfTimingIeee1588PtpType_Type()
)
aluSyncIfTimingIeee1588PtpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSyncIfTimingIeee1588PtpType.setStatus("obsolete")
_AluSyncIfTimingExternInCfgQltyLevel_Type = TmnxSSMQualityLevel
_AluSyncIfTimingExternInCfgQltyLevel_Object = MibTableColumn
aluSyncIfTimingExternInCfgQltyLevel = _AluSyncIfTimingExternInCfgQltyLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 4, 1, 1, 1, 11),
    _AluSyncIfTimingExternInCfgQltyLevel_Type()
)
aluSyncIfTimingExternInCfgQltyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSyncIfTimingExternInCfgQltyLevel.setStatus("current")
_AluSyncIfTimingExternInState_Type = TmnxRefInState
_AluSyncIfTimingExternInState_Object = MibTableColumn
aluSyncIfTimingExternInState = _AluSyncIfTimingExternInState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 4, 1, 1, 1, 12),
    _AluSyncIfTimingExternInState_Type()
)
aluSyncIfTimingExternInState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSyncIfTimingExternInState.setStatus("current")


class _AluSyncIfTimingRef1SrcPtpClock_Type(Unsigned32):
    """Custom type aluSyncIfTimingRef1SrcPtpClock based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_AluSyncIfTimingRef1SrcPtpClock_Type.__name__ = "Unsigned32"
_AluSyncIfTimingRef1SrcPtpClock_Object = MibTableColumn
aluSyncIfTimingRef1SrcPtpClock = _AluSyncIfTimingRef1SrcPtpClock_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 4, 1, 1, 1, 13),
    _AluSyncIfTimingRef1SrcPtpClock_Type()
)
aluSyncIfTimingRef1SrcPtpClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSyncIfTimingRef1SrcPtpClock.setStatus("current")


class _AluSyncIfTimingRef2SrcPtpClock_Type(Unsigned32):
    """Custom type aluSyncIfTimingRef2SrcPtpClock based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_AluSyncIfTimingRef2SrcPtpClock_Type.__name__ = "Unsigned32"
_AluSyncIfTimingRef2SrcPtpClock_Object = MibTableColumn
aluSyncIfTimingRef2SrcPtpClock = _AluSyncIfTimingRef2SrcPtpClock_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 4, 1, 1, 1, 14),
    _AluSyncIfTimingRef2SrcPtpClock_Type()
)
aluSyncIfTimingRef2SrcPtpClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSyncIfTimingRef2SrcPtpClock.setStatus("current")
_AluExtIfSyncIfTimingAdmExtensionTable_Object = MibTable
aluExtIfSyncIfTimingAdmExtensionTable = _AluExtIfSyncIfTimingAdmExtensionTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 4, 1, 2)
)
if mibBuilder.loadTexts:
    aluExtIfSyncIfTimingAdmExtensionTable.setStatus("current")
_AluExtIfSyncIfTimingAdmExtensionEntry_Object = MibTableRow
aluExtIfSyncIfTimingAdmExtensionEntry = _AluExtIfSyncIfTimingAdmExtensionEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 4, 1, 2, 1)
)
if mibBuilder.loadTexts:
    aluExtIfSyncIfTimingAdmExtensionEntry.setStatus("current")


class _AluSyncIfTimingAdmExternInIfType_Type(AluExternalIfType):
    """Custom type aluSyncIfTimingAdmExternInIfType based on AluExternalIfType"""
    defaultValue = 1


_AluSyncIfTimingAdmExternInIfType_Type.__name__ = "AluExternalIfType"
_AluSyncIfTimingAdmExternInIfType_Object = MibTableColumn
aluSyncIfTimingAdmExternInIfType = _AluSyncIfTimingAdmExternInIfType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 4, 1, 2, 1, 1),
    _AluSyncIfTimingAdmExternInIfType_Type()
)
aluSyncIfTimingAdmExternInIfType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSyncIfTimingAdmExternInIfType.setStatus("current")


class _AluSyncIfTimingAdmExternInImpedType_Type(AluExternalInputImpedanceType):
    """Custom type aluSyncIfTimingAdmExternInImpedType based on AluExternalInputImpedanceType"""
    defaultValue = 2


_AluSyncIfTimingAdmExternInImpedType_Type.__name__ = "AluExternalInputImpedanceType"
_AluSyncIfTimingAdmExternInImpedType_Object = MibTableColumn
aluSyncIfTimingAdmExternInImpedType = _AluSyncIfTimingAdmExternInImpedType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 4, 1, 2, 1, 2),
    _AluSyncIfTimingAdmExternInImpedType_Type()
)
aluSyncIfTimingAdmExternInImpedType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSyncIfTimingAdmExternInImpedType.setStatus("current")


class _AluSyncIfTimingAdmExternOutIfType_Type(AluExternalIfType):
    """Custom type aluSyncIfTimingAdmExternOutIfType based on AluExternalIfType"""
    defaultValue = 1


_AluSyncIfTimingAdmExternOutIfType_Type.__name__ = "AluExternalIfType"
_AluSyncIfTimingAdmExternOutIfType_Object = MibTableColumn
aluSyncIfTimingAdmExternOutIfType = _AluSyncIfTimingAdmExternOutIfType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 4, 1, 2, 1, 3),
    _AluSyncIfTimingAdmExternOutIfType_Type()
)
aluSyncIfTimingAdmExternOutIfType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSyncIfTimingAdmExternOutIfType.setStatus("current")


class _AluSyncIfTimingAdmExternInIfAdminStatus_Type(TmnxPortAdminStatus):
    """Custom type aluSyncIfTimingAdmExternInIfAdminStatus based on TmnxPortAdminStatus"""
    defaultValue = 3


_AluSyncIfTimingAdmExternInIfAdminStatus_Type.__name__ = "TmnxPortAdminStatus"
_AluSyncIfTimingAdmExternInIfAdminStatus_Object = MibTableColumn
aluSyncIfTimingAdmExternInIfAdminStatus = _AluSyncIfTimingAdmExternInIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 4, 1, 2, 1, 4),
    _AluSyncIfTimingAdmExternInIfAdminStatus_Type()
)
aluSyncIfTimingAdmExternInIfAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSyncIfTimingAdmExternInIfAdminStatus.setStatus("current")


class _AluSyncIfTimingAdmRef1Ieee1588PtpSrc_Type(TNamedItemOrEmpty):
    """Custom type aluSyncIfTimingAdmRef1Ieee1588PtpSrc based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_AluSyncIfTimingAdmRef1Ieee1588PtpSrc_Type.__name__ = "TNamedItemOrEmpty"
_AluSyncIfTimingAdmRef1Ieee1588PtpSrc_Object = MibTableColumn
aluSyncIfTimingAdmRef1Ieee1588PtpSrc = _AluSyncIfTimingAdmRef1Ieee1588PtpSrc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 4, 1, 2, 1, 5),
    _AluSyncIfTimingAdmRef1Ieee1588PtpSrc_Type()
)
aluSyncIfTimingAdmRef1Ieee1588PtpSrc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSyncIfTimingAdmRef1Ieee1588PtpSrc.setStatus("obsolete")


class _AluSyncIfTimingAdmRef2Ieee1588PtpSrc_Type(TNamedItemOrEmpty):
    """Custom type aluSyncIfTimingAdmRef2Ieee1588PtpSrc based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_AluSyncIfTimingAdmRef2Ieee1588PtpSrc_Type.__name__ = "TNamedItemOrEmpty"
_AluSyncIfTimingAdmRef2Ieee1588PtpSrc_Object = MibTableColumn
aluSyncIfTimingAdmRef2Ieee1588PtpSrc = _AluSyncIfTimingAdmRef2Ieee1588PtpSrc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 4, 1, 2, 1, 6),
    _AluSyncIfTimingAdmRef2Ieee1588PtpSrc_Type()
)
aluSyncIfTimingAdmRef2Ieee1588PtpSrc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSyncIfTimingAdmRef2Ieee1588PtpSrc.setStatus("obsolete")


class _AluSyncIfTimingAdmExternInCfgQltyLevel_Type(TmnxSSMQualityLevel):
    """Custom type aluSyncIfTimingAdmExternInCfgQltyLevel based on TmnxSSMQualityLevel"""
    defaultValue = 2


_AluSyncIfTimingAdmExternInCfgQltyLevel_Type.__name__ = "TmnxSSMQualityLevel"
_AluSyncIfTimingAdmExternInCfgQltyLevel_Object = MibTableColumn
aluSyncIfTimingAdmExternInCfgQltyLevel = _AluSyncIfTimingAdmExternInCfgQltyLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 4, 1, 2, 1, 7),
    _AluSyncIfTimingAdmExternInCfgQltyLevel_Type()
)
aluSyncIfTimingAdmExternInCfgQltyLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSyncIfTimingAdmExternInCfgQltyLevel.setStatus("current")


class _AluSyncIfTimingAdmRef1SrcPtpClock_Type(Unsigned32):
    """Custom type aluSyncIfTimingAdmRef1SrcPtpClock based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_AluSyncIfTimingAdmRef1SrcPtpClock_Type.__name__ = "Unsigned32"
_AluSyncIfTimingAdmRef1SrcPtpClock_Object = MibTableColumn
aluSyncIfTimingAdmRef1SrcPtpClock = _AluSyncIfTimingAdmRef1SrcPtpClock_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 4, 1, 2, 1, 8),
    _AluSyncIfTimingAdmRef1SrcPtpClock_Type()
)
aluSyncIfTimingAdmRef1SrcPtpClock.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSyncIfTimingAdmRef1SrcPtpClock.setStatus("current")


class _AluSyncIfTimingAdmRef2SrcPtpClock_Type(Unsigned32):
    """Custom type aluSyncIfTimingAdmRef2SrcPtpClock based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_AluSyncIfTimingAdmRef2SrcPtpClock_Type.__name__ = "Unsigned32"
_AluSyncIfTimingAdmRef2SrcPtpClock_Object = MibTableColumn
aluSyncIfTimingAdmRef2SrcPtpClock = _AluSyncIfTimingAdmRef2SrcPtpClock_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 4, 1, 2, 1, 9),
    _AluSyncIfTimingAdmRef2SrcPtpClock_Type()
)
aluSyncIfTimingAdmRef2SrcPtpClock.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSyncIfTimingAdmRef2SrcPtpClock.setStatus("current")
_AluHwNotification_ObjectIdentity = ObjectIdentity
aluHwNotification = _AluHwNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 2)
)
_AluChassisNotifyPrefix_ObjectIdentity = ObjectIdentity
aluChassisNotifyPrefix = _AluChassisNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 2, 1)
)
_AluChassisNotification_ObjectIdentity = ObjectIdentity
aluChassisNotification = _AluChassisNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 2, 1, 0)
)
_AluSetsNotifyPrefix_ObjectIdentity = ObjectIdentity
aluSetsNotifyPrefix = _AluSetsNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 4)
)
tmnxMDAEntry.registerAugmentions(
    ("ALU-CHASSIS-MIB",
     "aluExtTmnxMDAEntry")
)
aluExtTmnxMDAEntry.setIndexNames(*tmnxMDAEntry.getIndexNames())
tmnxCpmCardEntry.registerAugmentions(
    ("ALU-CHASSIS-MIB",
     "aluExtTmnxCpmCardEntry")
)
aluExtTmnxCpmCardEntry.setIndexNames(*tmnxCpmCardEntry.getIndexNames())
tmnxCpmCardEntry.registerAugmentions(
    ("ALU-CHASSIS-MIB",
     "aluExtIfSyncIfTimingExtensionEntry")
)
aluExtIfSyncIfTimingExtensionEntry.setIndexNames(*tmnxCpmCardEntry.getIndexNames())
tSyncIfTimingAdmEntry.registerAugmentions(
    ("ALU-CHASSIS-MIB",
     "aluExtIfSyncIfTimingAdmExtensionEntry")
)
aluExtIfSyncIfTimingAdmExtensionEntry.setIndexNames(*tSyncIfTimingAdmEntry.getIndexNames())

# Managed Objects groups

aluFamGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 1, 2, 1)
)
aluFamGroup.setObjects(
      *(("ALU-CHASSIS-MIB", "aluFamOperStatus"),
        ("ALU-CHASSIS-MIB", "aluFamHwIndex"),
        ("ALU-CHASSIS-MIB", "aluFamEquippedType"))
)
if mibBuilder.loadTexts:
    aluFamGroup.setStatus("current")

aluExtAlarmsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 1, 2, 2)
)
aluExtAlarmsGroup.setObjects(
      *(("ALU-CHASSIS-MIB", "aluChassisExtAlarmState"),
        ("ALU-CHASSIS-MIB", "aluChassisExtAlarmEvent"),
        ("ALU-CHASSIS-MIB", "aluChassisExtAlarmPin"))
)
if mibBuilder.loadTexts:
    aluExtAlarmsGroup.setStatus("current")

aluPlatformHwClassGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 1, 2, 4)
)
aluPlatformHwClassGroup.setObjects(
    ("ALU-CHASSIS-MIB", "aluExtPlatformHwClass")
)
if mibBuilder.loadTexts:
    aluPlatformHwClassGroup.setStatus("current")

aluHwBgDiagsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 1, 2, 5)
)
aluHwBgDiagsGroup.setObjects(
      *(("ALU-CHASSIS-MIB", "aluExtHwBgDiagsState"),
        ("ALU-CHASSIS-MIB", "aluExtHwBgDiagsFaultReason"))
)
if mibBuilder.loadTexts:
    aluHwBgDiagsGroup.setStatus("current")

aluExternalTimingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 1, 2, 7)
)
aluExternalTimingGroup.setObjects(
      *(("ALU-CHASSIS-MIB", "aluSyncIfTimingExternInIfType"),
        ("ALU-CHASSIS-MIB", "aluSyncIfTimingExternInImpedType"),
        ("ALU-CHASSIS-MIB", "aluSyncIfTimingExternOutIfType"),
        ("ALU-CHASSIS-MIB", "aluSyncIfTimingExternInIfAdminStatus"),
        ("ALU-CHASSIS-MIB", "aluSyncIfTimingExternInIfInUse"),
        ("ALU-CHASSIS-MIB", "aluSyncIfTimingExternInIfQualified"),
        ("ALU-CHASSIS-MIB", "aluSyncIfTimingExternInIfAlarm"),
        ("ALU-CHASSIS-MIB", "aluSyncIfTimingAdmExternInIfType"),
        ("ALU-CHASSIS-MIB", "aluSyncIfTimingAdmExternInImpedType"),
        ("ALU-CHASSIS-MIB", "aluSyncIfTimingAdmExternOutIfType"),
        ("ALU-CHASSIS-MIB", "aluSyncIfTimingAdmExternInIfAdminStatus"))
)
if mibBuilder.loadTexts:
    aluExternalTimingGroup.setStatus("current")

aluExtCpmCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 1, 2, 9)
)
aluExtCpmCardGroup.setObjects(
    ("ALU-CHASSIS-MIB", "aluExtCpmCardUpgrade")
)
if mibBuilder.loadTexts:
    aluExtCpmCardGroup.setStatus("current")

aluExtMDAGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 1, 2, 11)
)
aluExtMDAGroup.setObjects(
      *(("ALU-CHASSIS-MIB", "aluExtTmnxMDANetworkIngFabricPolicy"),
        ("ALU-CHASSIS-MIB", "aluExtTmnxMDAAccessIngFabricPolicy"),
        ("ALU-CHASSIS-MIB", "aluExtTmnxMDAFabricStatsEnabled"),
        ("ALU-CHASSIS-MIB", "aluExtTmnxMDAVoiceCompandingLaw"),
        ("ALU-CHASSIS-MIB", "aluExtTmnxMDAVoiceSignalingType"))
)
if mibBuilder.loadTexts:
    aluExtMDAGroup.setStatus("obsolete")

aluFabricDeviceStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 1, 2, 12)
)
aluFabricDeviceStatsGroup.setObjects(
      *(("ALU-CHASSIS-MIB", "aluFabricDeviceStatsFwdPkts"),
        ("ALU-CHASSIS-MIB", "aluFabricDeviceStatsDroPkts"),
        ("ALU-CHASSIS-MIB", "aluFabricDeviceStatsFwdOcts"))
)
if mibBuilder.loadTexts:
    aluFabricDeviceStatsGroup.setStatus("obsolete")

aluSourceMDAStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 1, 2, 13)
)
aluSourceMDAStatsGroup.setObjects(
      *(("ALU-CHASSIS-MIB", "aluSourceMDAStatsFwdInProfPkts"),
        ("ALU-CHASSIS-MIB", "aluSourceMDAStatsFwdOutProfPkts"),
        ("ALU-CHASSIS-MIB", "aluSourceMDAStatsFwdInProfOcts"),
        ("ALU-CHASSIS-MIB", "aluSourceMDAStatsFwdOutProfOcts"),
        ("ALU-CHASSIS-MIB", "aluSourceMDAStatsDroInProfPkts"),
        ("ALU-CHASSIS-MIB", "aluSourceMDAStatsDroOutProfPkts"),
        ("ALU-CHASSIS-MIB", "aluSourceMDAStatsDroInProfOcts"),
        ("ALU-CHASSIS-MIB", "aluSourceMDAStatsDroOutProfOcts"),
        ("ALU-CHASSIS-MIB", "aluSourceMDAStatsAccessFwdInProfPkts"),
        ("ALU-CHASSIS-MIB", "aluSourceMDAStatsAccessFwdOutProfPkts"),
        ("ALU-CHASSIS-MIB", "aluSourceMDAStatsAccessFwdInProfOcts"),
        ("ALU-CHASSIS-MIB", "aluSourceMDAStatsAccessFwdOutProfOcts"),
        ("ALU-CHASSIS-MIB", "aluSourceMDAStatsAccessDroPkts"),
        ("ALU-CHASSIS-MIB", "aluSourceMDAStatsAccessDroOcts"))
)
if mibBuilder.loadTexts:
    aluSourceMDAStatsGroup.setStatus("current")

aluDestMDAStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 1, 2, 14)
)
aluDestMDAStatsGroup.setObjects(
      *(("ALU-CHASSIS-MIB", "aluDestMDAStatsFwdInProfPkts"),
        ("ALU-CHASSIS-MIB", "aluDestMDAStatsFwdOutProfPkts"),
        ("ALU-CHASSIS-MIB", "aluDestMDAStatsFwdInProfOcts"),
        ("ALU-CHASSIS-MIB", "aluDestMDAStatsFwdOutProfOcts"),
        ("ALU-CHASSIS-MIB", "aluDestMDAStatsDroInProfPkts"),
        ("ALU-CHASSIS-MIB", "aluDestMDAStatsDroOutProfPkts"),
        ("ALU-CHASSIS-MIB", "aluDestMDAStatsDroInProfOcts"),
        ("ALU-CHASSIS-MIB", "aluDestMDAStatsDroOutProfOcts"),
        ("ALU-CHASSIS-MIB", "aluDestMDAStatsAccessFwdInProfPkts"),
        ("ALU-CHASSIS-MIB", "aluDestMDAStatsAccessFwdOutProfPkts"),
        ("ALU-CHASSIS-MIB", "aluDestMDAStatsAccessFwdInProfOcts"),
        ("ALU-CHASSIS-MIB", "aluDestMDAStatsAccessFwdOutProfOcts"),
        ("ALU-CHASSIS-MIB", "aluDestMDAStatsAccessDroPkts"),
        ("ALU-CHASSIS-MIB", "aluDestMDAStatsAccessDroOcts"))
)
if mibBuilder.loadTexts:
    aluDestMDAStatsGroup.setStatus("current")

alu1588PtpTimingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 1, 2, 16)
)
alu1588PtpTimingGroup.setObjects(
      *(("ALU-CHASSIS-MIB", "aluSyncIfTimingIeee1588PtpType"),
        ("ALU-CHASSIS-MIB", "aluSyncIfTimingRef1Ieee1588PtpSrc"),
        ("ALU-CHASSIS-MIB", "aluSyncIfTimingRef2Ieee1588PtpSrc"),
        ("ALU-CHASSIS-MIB", "aluSyncIfTimingAdmRef1Ieee1588PtpSrc"),
        ("ALU-CHASSIS-MIB", "aluSyncIfTimingAdmRef2Ieee1588PtpSrc"))
)
if mibBuilder.loadTexts:
    alu1588PtpTimingGroup.setStatus("obsolete")

aluEqMdaRuntimeNotifyObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 1, 2, 17)
)
aluEqMdaRuntimeNotifyObjsGroup.setObjects(
    ("ALU-CHASSIS-MIB", "aluChassisNotifyMdaRuntimeStatusContext")
)
if mibBuilder.loadTexts:
    aluEqMdaRuntimeNotifyObjsGroup.setStatus("current")

aluQLRefSelectionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 1, 2, 19)
)
aluQLRefSelectionGroup.setObjects(
      *(("ALU-CHASSIS-MIB", "aluSyncIfTimingAdmExternInCfgQltyLevel"),
        ("ALU-CHASSIS-MIB", "aluSyncIfTimingExternInCfgQltyLevel"),
        ("ALU-CHASSIS-MIB", "aluSyncIfTimingExternInState"))
)
if mibBuilder.loadTexts:
    aluQLRefSelectionGroup.setStatus("current")

aluMDAAlarmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 1, 2, 21)
)
aluMDAAlarmGroup.setObjects(
      *(("ALU-CHASSIS-MIB", "aluExtTmnxMDANumOfDigitalAlarmInputs"),
        ("ALU-CHASSIS-MIB", "aluExtTmnxMDANumOfAnalogAlarmInputs"),
        ("ALU-CHASSIS-MIB", "aluExtTmnxMDANumOfDigitalOutputRelays"))
)
if mibBuilder.loadTexts:
    aluMDAAlarmGroup.setStatus("current")

aluFabricDeviceStatsV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 1, 2, 22)
)
aluFabricDeviceStatsV4v0Group.setObjects(
      *(("ALU-CHASSIS-MIB", "aluFabricDeviceStatsFwdPkts"),
        ("ALU-CHASSIS-MIB", "aluFabricDeviceStatsDroPkts"),
        ("ALU-CHASSIS-MIB", "aluFabricDeviceStatsFwdOcts"),
        ("ALU-CHASSIS-MIB", "aluFabricDeviceStatsUcastFwdPkts"),
        ("ALU-CHASSIS-MIB", "aluFabricDeviceStatsMcastFwdPkts"),
        ("ALU-CHASSIS-MIB", "aluFabricDeviceStatsDroOcts"))
)
if mibBuilder.loadTexts:
    aluFabricDeviceStatsV4v0Group.setStatus("current")

alu1588PtpTimingV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 1, 2, 23)
)
alu1588PtpTimingV4v0Group.setObjects(
      *(("ALU-CHASSIS-MIB", "aluSyncIfTimingRef1SrcPtpClock"),
        ("ALU-CHASSIS-MIB", "aluSyncIfTimingRef2SrcPtpClock"),
        ("ALU-CHASSIS-MIB", "aluSyncIfTimingAdmRef1SrcPtpClock"),
        ("ALU-CHASSIS-MIB", "aluSyncIfTimingAdmRef2SrcPtpClock"))
)
if mibBuilder.loadTexts:
    alu1588PtpTimingV4v0Group.setStatus("current")

alu1588PtpTimingObsoleteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 1, 2, 24)
)
alu1588PtpTimingObsoleteGroup.setObjects(
      *(("ALU-CHASSIS-MIB", "aluSyncIfTimingIeee1588PtpType"),
        ("ALU-CHASSIS-MIB", "aluSyncIfTimingRef1Ieee1588PtpSrc"),
        ("ALU-CHASSIS-MIB", "aluSyncIfTimingRef2Ieee1588PtpSrc"),
        ("ALU-CHASSIS-MIB", "aluSyncIfTimingAdmRef1Ieee1588PtpSrc"),
        ("ALU-CHASSIS-MIB", "aluSyncIfTimingAdmRef2Ieee1588PtpSrc"))
)
if mibBuilder.loadTexts:
    alu1588PtpTimingObsoleteGroup.setStatus("current")

aluExtMDAV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 1, 2, 25)
)
aluExtMDAV5v0Group.setObjects(
      *(("ALU-CHASSIS-MIB", "aluExtTmnxMDANetworkIngFabricPolicy"),
        ("ALU-CHASSIS-MIB", "aluExtTmnxMDAAccessIngFabricPolicy"),
        ("ALU-CHASSIS-MIB", "aluExtTmnxMDAFabricStatsEnabled"),
        ("ALU-CHASSIS-MIB", "aluExtTmnxMDAVoiceCompandingLaw"),
        ("ALU-CHASSIS-MIB", "aluExtTmnxMDAVoiceSignalingType"),
        ("ALU-CHASSIS-MIB", "aluExtTmnxMDACapabilityMode"))
)
if mibBuilder.loadTexts:
    aluExtMDAV5v0Group.setStatus("current")

aluMDAEventStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 1, 2, 26)
)
aluMDAEventStatsGroup.setObjects(
    ("ALU-CHASSIS-MIB", "aluFabricDeviceStatsMdaDroEvents")
)
if mibBuilder.loadTexts:
    aluMDAEventStatsGroup.setStatus("current")

aluExtHwMfgVariantGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 1, 2, 27)
)
aluExtHwMfgVariantGroup.setObjects(
    ("ALU-CHASSIS-MIB", "aluExtHwMfgVariant")
)
if mibBuilder.loadTexts:
    aluExtHwMfgVariantGroup.setStatus("current")


# Notification objects

aluEqExtAlarmDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 2, 1, 0, 1)
)
aluEqExtAlarmDetected.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("ALU-CHASSIS-MIB", "aluChassisExtAlarmState"),
        ("ALU-CHASSIS-MIB", "aluChassisExtAlarmEvent"),
        ("ALU-CHASSIS-MIB", "aluChassisExtAlarmPin"))
)
if mibBuilder.loadTexts:
    aluEqExtAlarmDetected.setStatus(
        "current"
    )

aluEqExtAlarmCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 2, 1, 0, 2)
)
aluEqExtAlarmCleared.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("ALU-CHASSIS-MIB", "aluChassisExtAlarmState"),
        ("ALU-CHASSIS-MIB", "aluChassisExtAlarmEvent"),
        ("ALU-CHASSIS-MIB", "aluChassisExtAlarmPin"))
)
if mibBuilder.loadTexts:
    aluEqExtAlarmCleared.setStatus(
        "current"
    )

aluEqBgDiagsFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 2, 1, 0, 3)
)
aluEqBgDiagsFault.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("ALU-CHASSIS-MIB", "aluExtHwBgDiagsState"),
        ("ALU-CHASSIS-MIB", "aluExtHwBgDiagsFaultReason"))
)
if mibBuilder.loadTexts:
    aluEqBgDiagsFault.setStatus(
        "current"
    )

aluEqSyncIfTimingExternAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 2, 1, 0, 4)
)
aluEqSyncIfTimingExternAlarm.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingNotifyAlarm"))
)
if mibBuilder.loadTexts:
    aluEqSyncIfTimingExternAlarm.setStatus(
        "current"
    )

aluEqSyncIfTimingExternAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 2, 1, 0, 5)
)
aluEqSyncIfTimingExternAlarmClear.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingNotifyAlarm"))
)
if mibBuilder.loadTexts:
    aluEqSyncIfTimingExternAlarmClear.setStatus(
        "current"
    )

aluEqFanMinorFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 2, 1, 0, 6)
)
aluEqFanMinorFailure.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"))
)
if mibBuilder.loadTexts:
    aluEqFanMinorFailure.setStatus(
        "current"
    )

aluEqFIBOutOfSynch = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 2, 1, 0, 7)
)
aluEqFIBOutOfSynch.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"))
)
if mibBuilder.loadTexts:
    aluEqFIBOutOfSynch.setStatus(
        "current"
    )

aluEqFIBOutOfSynchClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 2, 1, 0, 8)
)
aluEqFIBOutOfSynchClr.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"))
)
if mibBuilder.loadTexts:
    aluEqFIBOutOfSynchClr.setStatus(
        "current"
    )

aluEqMdaRuntimeStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 2, 1, 0, 9)
)
aluEqMdaRuntimeStatus.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("ALU-CHASSIS-MIB", "aluChassisNotifyMdaRuntimeStatusContext"))
)
if mibBuilder.loadTexts:
    aluEqMdaRuntimeStatus.setStatus(
        "current"
    )

aluSyncIfTimingRefSwitch = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 2, 1, 0, 10)
)
aluSyncIfTimingRefSwitch.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingRef1InUse"),
        ("TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingRef2InUse"),
        ("ALU-CHASSIS-MIB", "aluSyncIfTimingExternInIfInUse"))
)
if mibBuilder.loadTexts:
    aluSyncIfTimingRefSwitch.setStatus(
        "current"
    )


# Notifications groups

aluExtAlarmNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 1, 2, 3)
)
aluExtAlarmNotificationGroup.setObjects(
      *(("ALU-CHASSIS-MIB", "aluEqExtAlarmDetected"),
        ("ALU-CHASSIS-MIB", "aluEqExtAlarmCleared"))
)
if mibBuilder.loadTexts:
    aluExtAlarmNotificationGroup.setStatus(
        "current"
    )

aluHwBgDiagsNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 1, 2, 6)
)
aluHwBgDiagsNotificationGroup.setObjects(
    ("ALU-CHASSIS-MIB", "aluEqBgDiagsFault")
)
if mibBuilder.loadTexts:
    aluHwBgDiagsNotificationGroup.setStatus(
        "current"
    )

aluExternalTimingNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 1, 2, 8)
)
aluExternalTimingNotificationGroup.setObjects(
      *(("ALU-CHASSIS-MIB", "aluEqSyncIfTimingExternAlarm"),
        ("ALU-CHASSIS-MIB", "aluEqSyncIfTimingExternAlarmClear"))
)
if mibBuilder.loadTexts:
    aluExternalTimingNotificationGroup.setStatus(
        "current"
    )

aluEqFanMinorFailGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 1, 2, 10)
)
aluEqFanMinorFailGroup.setObjects(
    ("ALU-CHASSIS-MIB", "aluEqFanMinorFailure")
)
if mibBuilder.loadTexts:
    aluEqFanMinorFailGroup.setStatus(
        "current"
    )

aluEqFIBSynchGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 1, 2, 15)
)
aluEqFIBSynchGroup.setObjects(
      *(("ALU-CHASSIS-MIB", "aluEqFIBOutOfSynch"),
        ("ALU-CHASSIS-MIB", "aluEqFIBOutOfSynchClr"))
)
if mibBuilder.loadTexts:
    aluEqFIBSynchGroup.setStatus(
        "current"
    )

aluEqMdaRuntimeNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 1, 2, 18)
)
aluEqMdaRuntimeNotificationGroup.setObjects(
    ("ALU-CHASSIS-MIB", "aluEqMdaRuntimeStatus")
)
if mibBuilder.loadTexts:
    aluEqMdaRuntimeNotificationGroup.setStatus(
        "current"
    )

aluSyncIfTimingNotifV3v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 1, 2, 20)
)
aluSyncIfTimingNotifV3v0Group.setObjects(
    ("ALU-CHASSIS-MIB", "aluSyncIfTimingRefSwitch")
)
if mibBuilder.loadTexts:
    aluSyncIfTimingNotifV3v0Group.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

aluChassisV1v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 1, 1, 1)
)
aluChassisV1v0Compliance.setObjects(
      *(("ALU-CHASSIS-MIB", "aluFamGroup"),
        ("ALU-CHASSIS-MIB", "aluExtAlarmsGroup"),
        ("ALU-CHASSIS-MIB", "aluExtAlarmNotificationGroup"),
        ("ALU-CHASSIS-MIB", "aluPlatformHwClassGroup"),
        ("ALU-CHASSIS-MIB", "aluHwBgDiagsGroup"),
        ("ALU-CHASSIS-MIB", "aluHwBgDiagsNotificationGroup"),
        ("ALU-CHASSIS-MIB", "aluExternalTimingGroup"),
        ("ALU-CHASSIS-MIB", "aluExternalTimingNotificationGroup"),
        ("ALU-CHASSIS-MIB", "aluExtCpmCardGroup"),
        ("ALU-CHASSIS-MIB", "aluFabricDeviceStatsGroup"),
        ("ALU-CHASSIS-MIB", "aluSourceMDAStatsGroup"),
        ("ALU-CHASSIS-MIB", "aluDestMDAStatsGroup"))
)
if mibBuilder.loadTexts:
    aluChassisV1v0Compliance.setStatus(
        "obsolete"
    )

aluChassisV4v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 1, 1, 2)
)
aluChassisV4v0Compliance.setObjects(
      *(("ALU-CHASSIS-MIB", "aluFamGroup"),
        ("ALU-CHASSIS-MIB", "aluExtAlarmsGroup"),
        ("ALU-CHASSIS-MIB", "aluExtAlarmNotificationGroup"),
        ("ALU-CHASSIS-MIB", "aluPlatformHwClassGroup"),
        ("ALU-CHASSIS-MIB", "aluHwBgDiagsGroup"),
        ("ALU-CHASSIS-MIB", "aluHwBgDiagsNotificationGroup"),
        ("ALU-CHASSIS-MIB", "aluExternalTimingGroup"),
        ("ALU-CHASSIS-MIB", "aluExternalTimingNotificationGroup"),
        ("ALU-CHASSIS-MIB", "aluExtCpmCardGroup"),
        ("ALU-CHASSIS-MIB", "aluSourceMDAStatsGroup"),
        ("ALU-CHASSIS-MIB", "aluDestMDAStatsGroup"),
        ("ALU-CHASSIS-MIB", "aluEqFIBSynchGroup"),
        ("ALU-CHASSIS-MIB", "aluEqFanMinorFailGroup"),
        ("ALU-CHASSIS-MIB", "aluEqMdaRuntimeNotificationGroup"),
        ("ALU-CHASSIS-MIB", "aluSyncIfTimingNotifV3v0Group"),
        ("ALU-CHASSIS-MIB", "aluFabricDeviceStatsV4v0Group"))
)
if mibBuilder.loadTexts:
    aluChassisV4v0Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALU-CHASSIS-MIB",
    **{"AluFamType": AluFamType,
       "AluExtAlarmState": AluExtAlarmState,
       "AluExtAlarmEvent": AluExtAlarmEvent,
       "AluPlatformHwClass": AluPlatformHwClass,
       "AluHwBgDiagsState": AluHwBgDiagsState,
       "AluSETSRefSource": AluSETSRefSource,
       "AluExternalIfType": AluExternalIfType,
       "AluExternalInputImpedanceType": AluExternalInputImpedanceType,
       "AluSyncIfTimingIeee1588PtpType": AluSyncIfTimingIeee1588PtpType,
       "aluChassisMIBModule": aluChassisMIBModule,
       "aluHwConformance": aluHwConformance,
       "aluChassisConformance": aluChassisConformance,
       "aluChassisCompliances": aluChassisCompliances,
       "aluChassisV1v0Compliance": aluChassisV1v0Compliance,
       "aluChassisV4v0Compliance": aluChassisV4v0Compliance,
       "aluChassisGroups": aluChassisGroups,
       "aluFamGroup": aluFamGroup,
       "aluExtAlarmsGroup": aluExtAlarmsGroup,
       "aluExtAlarmNotificationGroup": aluExtAlarmNotificationGroup,
       "aluPlatformHwClassGroup": aluPlatformHwClassGroup,
       "aluHwBgDiagsGroup": aluHwBgDiagsGroup,
       "aluHwBgDiagsNotificationGroup": aluHwBgDiagsNotificationGroup,
       "aluExternalTimingGroup": aluExternalTimingGroup,
       "aluExternalTimingNotificationGroup": aluExternalTimingNotificationGroup,
       "aluExtCpmCardGroup": aluExtCpmCardGroup,
       "aluEqFanMinorFailGroup": aluEqFanMinorFailGroup,
       "aluExtMDAGroup": aluExtMDAGroup,
       "aluFabricDeviceStatsGroup": aluFabricDeviceStatsGroup,
       "aluSourceMDAStatsGroup": aluSourceMDAStatsGroup,
       "aluDestMDAStatsGroup": aluDestMDAStatsGroup,
       "aluEqFIBSynchGroup": aluEqFIBSynchGroup,
       "alu1588PtpTimingGroup": alu1588PtpTimingGroup,
       "aluEqMdaRuntimeNotifyObjsGroup": aluEqMdaRuntimeNotifyObjsGroup,
       "aluEqMdaRuntimeNotificationGroup": aluEqMdaRuntimeNotificationGroup,
       "aluQLRefSelectionGroup": aluQLRefSelectionGroup,
       "aluSyncIfTimingNotifV3v0Group": aluSyncIfTimingNotifV3v0Group,
       "aluMDAAlarmGroup": aluMDAAlarmGroup,
       "aluFabricDeviceStatsV4v0Group": aluFabricDeviceStatsV4v0Group,
       "alu1588PtpTimingV4v0Group": alu1588PtpTimingV4v0Group,
       "alu1588PtpTimingObsoleteGroup": alu1588PtpTimingObsoleteGroup,
       "aluExtMDAV5v0Group": aluExtMDAV5v0Group,
       "aluMDAEventStatsGroup": aluMDAEventStatsGroup,
       "aluExtHwMfgVariantGroup": aluExtHwMfgVariantGroup,
       "aluSetsMIBConformance": aluSetsMIBConformance,
       "aluHwObjs": aluHwObjs,
       "aluChassisObjs": aluChassisObjs,
       "aluFamTable": aluFamTable,
       "aluFamEntry": aluFamEntry,
       "aluFamIndex": aluFamIndex,
       "aluFamOperStatus": aluFamOperStatus,
       "aluFamHwIndex": aluFamHwIndex,
       "aluFamEquippedType": aluFamEquippedType,
       "aluChassisExtAlarmTable": aluChassisExtAlarmTable,
       "aluChassisExtAlarmEntry": aluChassisExtAlarmEntry,
       "aluChassisExtAlarmIndex": aluChassisExtAlarmIndex,
       "aluChassisExtAlarmState": aluChassisExtAlarmState,
       "aluChassisExtAlarmEvent": aluChassisExtAlarmEvent,
       "aluChassisExtAlarmPin": aluChassisExtAlarmPin,
       "aluExtTmnxHwTable": aluExtTmnxHwTable,
       "aluExtTmnxHwEntry": aluExtTmnxHwEntry,
       "aluExtPlatformHwClass": aluExtPlatformHwClass,
       "aluExtHwBgDiagsState": aluExtHwBgDiagsState,
       "aluExtHwBgDiagsFaultReason": aluExtHwBgDiagsFaultReason,
       "aluExtHwMfgVariant": aluExtHwMfgVariant,
       "aluExtTmnxMDATable": aluExtTmnxMDATable,
       "aluExtTmnxMDAEntry": aluExtTmnxMDAEntry,
       "aluExtTmnxMDANetworkIngFabricPolicy": aluExtTmnxMDANetworkIngFabricPolicy,
       "aluExtTmnxMDAAccessIngFabricPolicy": aluExtTmnxMDAAccessIngFabricPolicy,
       "aluExtTmnxMDAFabricStatsEnabled": aluExtTmnxMDAFabricStatsEnabled,
       "aluExtTmnxMDAVoiceCompandingLaw": aluExtTmnxMDAVoiceCompandingLaw,
       "aluExtTmnxMDAVoiceSignalingType": aluExtTmnxMDAVoiceSignalingType,
       "aluExtTmnxMDANumOfDigitalAlarmInputs": aluExtTmnxMDANumOfDigitalAlarmInputs,
       "aluExtTmnxMDANumOfAnalogAlarmInputs": aluExtTmnxMDANumOfAnalogAlarmInputs,
       "aluExtTmnxMDANumOfDigitalOutputRelays": aluExtTmnxMDANumOfDigitalOutputRelays,
       "aluExtTmnxMDACapabilityMode": aluExtTmnxMDACapabilityMode,
       "aluFabricDeviceStatsTable": aluFabricDeviceStatsTable,
       "aluFabricDeviceStatsEntry": aluFabricDeviceStatsEntry,
       "aluFabricDeviceStatsIndex": aluFabricDeviceStatsIndex,
       "aluFabricDeviceStatsFwdPkts": aluFabricDeviceStatsFwdPkts,
       "aluFabricDeviceStatsDroPkts": aluFabricDeviceStatsDroPkts,
       "aluFabricDeviceStatsFwdOcts": aluFabricDeviceStatsFwdOcts,
       "aluFabricDeviceStatsUcastFwdPkts": aluFabricDeviceStatsUcastFwdPkts,
       "aluFabricDeviceStatsMcastFwdPkts": aluFabricDeviceStatsMcastFwdPkts,
       "aluFabricDeviceStatsDroOcts": aluFabricDeviceStatsDroOcts,
       "aluFabricDeviceStatsMdaDroEvents": aluFabricDeviceStatsMdaDroEvents,
       "aluSourceMDAStatsTable": aluSourceMDAStatsTable,
       "aluSourceMDAStatsEntry": aluSourceMDAStatsEntry,
       "aluSourceMDASrcMdaId": aluSourceMDASrcMdaId,
       "aluSourceMDADestMdaId": aluSourceMDADestMdaId,
       "aluSourceMDAStatsFwdInProfPkts": aluSourceMDAStatsFwdInProfPkts,
       "aluSourceMDAStatsFwdOutProfPkts": aluSourceMDAStatsFwdOutProfPkts,
       "aluSourceMDAStatsFwdInProfOcts": aluSourceMDAStatsFwdInProfOcts,
       "aluSourceMDAStatsFwdOutProfOcts": aluSourceMDAStatsFwdOutProfOcts,
       "aluSourceMDAStatsDroInProfPkts": aluSourceMDAStatsDroInProfPkts,
       "aluSourceMDAStatsDroOutProfPkts": aluSourceMDAStatsDroOutProfPkts,
       "aluSourceMDAStatsDroInProfOcts": aluSourceMDAStatsDroInProfOcts,
       "aluSourceMDAStatsDroOutProfOcts": aluSourceMDAStatsDroOutProfOcts,
       "aluSourceMDAStatsAccessFwdInProfPkts": aluSourceMDAStatsAccessFwdInProfPkts,
       "aluSourceMDAStatsAccessFwdOutProfPkts": aluSourceMDAStatsAccessFwdOutProfPkts,
       "aluSourceMDAStatsAccessFwdInProfOcts": aluSourceMDAStatsAccessFwdInProfOcts,
       "aluSourceMDAStatsAccessFwdOutProfOcts": aluSourceMDAStatsAccessFwdOutProfOcts,
       "aluSourceMDAStatsAccessDroPkts": aluSourceMDAStatsAccessDroPkts,
       "aluSourceMDAStatsAccessDroOcts": aluSourceMDAStatsAccessDroOcts,
       "aluDestMDAStatsTable": aluDestMDAStatsTable,
       "aluDestMDAStatsEntry": aluDestMDAStatsEntry,
       "aluDestMDADestMdaId": aluDestMDADestMdaId,
       "aluDestMDASrcMdaId": aluDestMDASrcMdaId,
       "aluDestMDAStatsFwdInProfPkts": aluDestMDAStatsFwdInProfPkts,
       "aluDestMDAStatsFwdOutProfPkts": aluDestMDAStatsFwdOutProfPkts,
       "aluDestMDAStatsFwdInProfOcts": aluDestMDAStatsFwdInProfOcts,
       "aluDestMDAStatsFwdOutProfOcts": aluDestMDAStatsFwdOutProfOcts,
       "aluDestMDAStatsDroInProfPkts": aluDestMDAStatsDroInProfPkts,
       "aluDestMDAStatsDroOutProfPkts": aluDestMDAStatsDroOutProfPkts,
       "aluDestMDAStatsDroInProfOcts": aluDestMDAStatsDroInProfOcts,
       "aluDestMDAStatsDroOutProfOcts": aluDestMDAStatsDroOutProfOcts,
       "aluDestMDAStatsAccessFwdInProfPkts": aluDestMDAStatsAccessFwdInProfPkts,
       "aluDestMDAStatsAccessFwdOutProfPkts": aluDestMDAStatsAccessFwdOutProfPkts,
       "aluDestMDAStatsAccessFwdInProfOcts": aluDestMDAStatsAccessFwdInProfOcts,
       "aluDestMDAStatsAccessFwdOutProfOcts": aluDestMDAStatsAccessFwdOutProfOcts,
       "aluDestMDAStatsAccessDroPkts": aluDestMDAStatsAccessDroPkts,
       "aluDestMDAStatsAccessDroOcts": aluDestMDAStatsAccessDroOcts,
       "aluCardObjs": aluCardObjs,
       "aluExtTmnxCpmCardTable": aluExtTmnxCpmCardTable,
       "aluExtTmnxCpmCardEntry": aluExtTmnxCpmCardEntry,
       "aluExtCpmCardUpgrade": aluExtCpmCardUpgrade,
       "aluChassisNotificationObjects": aluChassisNotificationObjects,
       "aluChassisNotifyMdaRuntimeStatusContext": aluChassisNotifyMdaRuntimeStatusContext,
       "aluSyncObjs": aluSyncObjs,
       "aluSyncExtensionObjs": aluSyncExtensionObjs,
       "aluExtIfSyncIfTimingExtensionTable": aluExtIfSyncIfTimingExtensionTable,
       "aluExtIfSyncIfTimingExtensionEntry": aluExtIfSyncIfTimingExtensionEntry,
       "aluSyncIfTimingExternInIfType": aluSyncIfTimingExternInIfType,
       "aluSyncIfTimingExternInImpedType": aluSyncIfTimingExternInImpedType,
       "aluSyncIfTimingExternOutIfType": aluSyncIfTimingExternOutIfType,
       "aluSyncIfTimingExternInIfAdminStatus": aluSyncIfTimingExternInIfAdminStatus,
       "aluSyncIfTimingExternInIfInUse": aluSyncIfTimingExternInIfInUse,
       "aluSyncIfTimingExternInIfQualified": aluSyncIfTimingExternInIfQualified,
       "aluSyncIfTimingExternInIfAlarm": aluSyncIfTimingExternInIfAlarm,
       "aluSyncIfTimingRef1Ieee1588PtpSrc": aluSyncIfTimingRef1Ieee1588PtpSrc,
       "aluSyncIfTimingRef2Ieee1588PtpSrc": aluSyncIfTimingRef2Ieee1588PtpSrc,
       "aluSyncIfTimingIeee1588PtpType": aluSyncIfTimingIeee1588PtpType,
       "aluSyncIfTimingExternInCfgQltyLevel": aluSyncIfTimingExternInCfgQltyLevel,
       "aluSyncIfTimingExternInState": aluSyncIfTimingExternInState,
       "aluSyncIfTimingRef1SrcPtpClock": aluSyncIfTimingRef1SrcPtpClock,
       "aluSyncIfTimingRef2SrcPtpClock": aluSyncIfTimingRef2SrcPtpClock,
       "aluExtIfSyncIfTimingAdmExtensionTable": aluExtIfSyncIfTimingAdmExtensionTable,
       "aluExtIfSyncIfTimingAdmExtensionEntry": aluExtIfSyncIfTimingAdmExtensionEntry,
       "aluSyncIfTimingAdmExternInIfType": aluSyncIfTimingAdmExternInIfType,
       "aluSyncIfTimingAdmExternInImpedType": aluSyncIfTimingAdmExternInImpedType,
       "aluSyncIfTimingAdmExternOutIfType": aluSyncIfTimingAdmExternOutIfType,
       "aluSyncIfTimingAdmExternInIfAdminStatus": aluSyncIfTimingAdmExternInIfAdminStatus,
       "aluSyncIfTimingAdmRef1Ieee1588PtpSrc": aluSyncIfTimingAdmRef1Ieee1588PtpSrc,
       "aluSyncIfTimingAdmRef2Ieee1588PtpSrc": aluSyncIfTimingAdmRef2Ieee1588PtpSrc,
       "aluSyncIfTimingAdmExternInCfgQltyLevel": aluSyncIfTimingAdmExternInCfgQltyLevel,
       "aluSyncIfTimingAdmRef1SrcPtpClock": aluSyncIfTimingAdmRef1SrcPtpClock,
       "aluSyncIfTimingAdmRef2SrcPtpClock": aluSyncIfTimingAdmRef2SrcPtpClock,
       "aluHwNotification": aluHwNotification,
       "aluChassisNotifyPrefix": aluChassisNotifyPrefix,
       "aluChassisNotification": aluChassisNotification,
       "aluEqExtAlarmDetected": aluEqExtAlarmDetected,
       "aluEqExtAlarmCleared": aluEqExtAlarmCleared,
       "aluEqBgDiagsFault": aluEqBgDiagsFault,
       "aluEqSyncIfTimingExternAlarm": aluEqSyncIfTimingExternAlarm,
       "aluEqSyncIfTimingExternAlarmClear": aluEqSyncIfTimingExternAlarmClear,
       "aluEqFanMinorFailure": aluEqFanMinorFailure,
       "aluEqFIBOutOfSynch": aluEqFIBOutOfSynch,
       "aluEqFIBOutOfSynchClr": aluEqFIBOutOfSynchClr,
       "aluEqMdaRuntimeStatus": aluEqMdaRuntimeStatus,
       "aluSyncIfTimingRefSwitch": aluSyncIfTimingRefSwitch,
       "aluSetsNotifyPrefix": aluSetsNotifyPrefix}
)
