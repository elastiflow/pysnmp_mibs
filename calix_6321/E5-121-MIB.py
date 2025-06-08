# SNMP MIB module (E5-121-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/calix_6321/E5-121-MIB.mib
# Produced by pysmi-1.6.1 at Tue Jun  3 17:40:54 2025
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

(BridgeId,
 MacAddress,
 Timeout,
 dot1dBasePort) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "BridgeId",
    "MacAddress",
    "Timeout",
    "dot1dBasePort")

(dot1agCfmMaIndex,
 dot1agCfmMdIndex,
 dot1agCfmMepIdentifier) = mibBuilder.importSymbols(
    "IEEE8021-CFM-MIB",
    "dot1agCfmMaIndex",
    "dot1agCfmMdIndex",
    "dot1agCfmMepIdentifier")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(dot1dTrafficClass,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "dot1dTrafficClass")

(PortList,
 VlanIndex,
 dot1qVlanIndex) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList",
    "VlanIndex",
    "dot1qVlanIndex")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CalixNetworks_ObjectIdentity = ObjectIdentity
calixNetworks = _CalixNetworks_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321)
)
_CalixRegistrations_ObjectIdentity = ObjectIdentity
calixRegistrations = _CalixRegistrations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1)
)
_CalixProducts_ObjectIdentity = ObjectIdentity
calixProducts = _CalixProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2)
)
_E5x100_ObjectIdentity = ObjectIdentity
e5x100 = _E5x100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3)
)
_E5x121_ObjectIdentity = ObjectIdentity
e5x121 = _E5x121_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4)
)
_Alarmconf_ObjectIdentity = ObjectIdentity
alarmconf = _Alarmconf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 2)
)
_AlarmOps_Type = Integer32
_AlarmOps_Object = MibScalar
alarmOps = _AlarmOps_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 2, 1),
    _AlarmOps_Type()
)
alarmOps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmOps.setStatus("current")
_AlarmConfTable_Object = MibTable
alarmConfTable = _AlarmConfTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 2, 2)
)
if mibBuilder.loadTexts:
    alarmConfTable.setStatus("current")
_AlarmConfEntry_Object = MibTableRow
alarmConfEntry = _AlarmConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 2, 2, 1)
)
alarmConfEntry.setIndexNames(
    (0, "E5-121-MIB", "alarmConfId"),
)
if mibBuilder.loadTexts:
    alarmConfEntry.setStatus("current")
_AlarmConfId_Type = Integer32
_AlarmConfId_Object = MibTableColumn
alarmConfId = _AlarmConfId_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 2, 2, 1, 1),
    _AlarmConfId_Type()
)
alarmConfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmConfId.setStatus("current")


class _AlarmConfFacility_Type(Integer32):
    """Custom type alarmConfFacility based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("local1", 1),
          ("local2", 2),
          ("local3", 3),
          ("local4", 4),
          ("local5", 5),
          ("local6", 6),
          ("local7", 7))
    )


_AlarmConfFacility_Type.__name__ = "Integer32"
_AlarmConfFacility_Object = MibTableColumn
alarmConfFacility = _AlarmConfFacility_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 2, 2, 1, 2),
    _AlarmConfFacility_Type()
)
alarmConfFacility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmConfFacility.setStatus("current")
_AlarmConfTarget_Type = Integer32
_AlarmConfTarget_Object = MibTableColumn
alarmConfTarget = _AlarmConfTarget_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 2, 2, 1, 3),
    _AlarmConfTarget_Type()
)
alarmConfTarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmConfTarget.setStatus("current")


class _AlarmConfSeverity_Type(Integer32):
    """Custom type alarmConfSeverity based on Integer32"""
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
        *(("critical", 1),
          ("major", 2),
          ("minor", 3),
          ("info", 4))
    )


_AlarmConfSeverity_Type.__name__ = "Integer32"
_AlarmConfSeverity_Object = MibTableColumn
alarmConfSeverity = _AlarmConfSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 2, 2, 1, 4),
    _AlarmConfSeverity_Type()
)
alarmConfSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmConfSeverity.setStatus("current")


class _AlarmConfClearable_Type(Integer32):
    """Custom type alarmConfClearable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clearable", 1),
          ("unclearable", 2))
    )


_AlarmConfClearable_Type.__name__ = "Integer32"
_AlarmConfClearable_Object = MibTableColumn
alarmConfClearable = _AlarmConfClearable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 2, 2, 1, 5),
    _AlarmConfClearable_Type()
)
alarmConfClearable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmConfClearable.setStatus("current")
_AlarmCurrTable_Object = MibTable
alarmCurrTable = _AlarmCurrTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 2, 3)
)
if mibBuilder.loadTexts:
    alarmCurrTable.setStatus("current")
_AlarmCurrEntry_Object = MibTableRow
alarmCurrEntry = _AlarmCurrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 2, 3, 1)
)
alarmCurrEntry.setIndexNames(
    (0, "E5-121-MIB", "alarmCurrIndex"),
)
if mibBuilder.loadTexts:
    alarmCurrEntry.setStatus("current")
_AlarmCurrIndex_Type = Integer32
_AlarmCurrIndex_Object = MibTableColumn
alarmCurrIndex = _AlarmCurrIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 2, 3, 1, 1),
    _AlarmCurrIndex_Type()
)
alarmCurrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmCurrIndex.setStatus("current")
_AlarmCurrOccurTime_Type = TimeTicks
_AlarmCurrOccurTime_Object = MibTableColumn
alarmCurrOccurTime = _AlarmCurrOccurTime_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 2, 3, 1, 2),
    _AlarmCurrOccurTime_Type()
)
alarmCurrOccurTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmCurrOccurTime.setStatus("current")
_AlarmCurrTrapOid_Type = ObjectIdentifier
_AlarmCurrTrapOid_Object = MibTableColumn
alarmCurrTrapOid = _AlarmCurrTrapOid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 2, 3, 1, 3),
    _AlarmCurrTrapOid_Type()
)
alarmCurrTrapOid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmCurrTrapOid.setStatus("current")
_AlarmCurrParam1_Type = Integer32
_AlarmCurrParam1_Object = MibTableColumn
alarmCurrParam1 = _AlarmCurrParam1_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 2, 3, 1, 4),
    _AlarmCurrParam1_Type()
)
alarmCurrParam1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmCurrParam1.setStatus("current")
_AlarmCurrParam2_Type = Integer32
_AlarmCurrParam2_Object = MibTableColumn
alarmCurrParam2 = _AlarmCurrParam2_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 2, 3, 1, 5),
    _AlarmCurrParam2_Type()
)
alarmCurrParam2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmCurrParam2.setStatus("current")
_AlarmCurrParam3_Type = Integer32
_AlarmCurrParam3_Object = MibTableColumn
alarmCurrParam3 = _AlarmCurrParam3_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 2, 3, 1, 6),
    _AlarmCurrParam3_Type()
)
alarmCurrParam3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmCurrParam3.setStatus("current")
_AlarmCurrParam4_Type = Integer32
_AlarmCurrParam4_Object = MibTableColumn
alarmCurrParam4 = _AlarmCurrParam4_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 2, 3, 1, 7),
    _AlarmCurrParam4_Type()
)
alarmCurrParam4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmCurrParam4.setStatus("current")
_AlarmCurrParam5_Type = Integer32
_AlarmCurrParam5_Object = MibTableColumn
alarmCurrParam5 = _AlarmCurrParam5_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 2, 3, 1, 8),
    _AlarmCurrParam5_Type()
)
alarmCurrParam5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmCurrParam5.setStatus("current")
_AlarmCurrParam6_Type = Integer32
_AlarmCurrParam6_Object = MibTableColumn
alarmCurrParam6 = _AlarmCurrParam6_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 2, 3, 1, 9),
    _AlarmCurrParam6_Type()
)
alarmCurrParam6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmCurrParam6.setStatus("current")
_AlarmCurrParam7_Type = Integer32
_AlarmCurrParam7_Object = MibTableColumn
alarmCurrParam7 = _AlarmCurrParam7_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 2, 3, 1, 10),
    _AlarmCurrParam7_Type()
)
alarmCurrParam7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmCurrParam7.setStatus("current")
_AlarmCurrParam8_Type = Integer32
_AlarmCurrParam8_Object = MibTableColumn
alarmCurrParam8 = _AlarmCurrParam8_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 2, 3, 1, 11),
    _AlarmCurrParam8_Type()
)
alarmCurrParam8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmCurrParam8.setStatus("current")
_AlarmCurrTimeDescr_Type = DisplayString
_AlarmCurrTimeDescr_Object = MibTableColumn
alarmCurrTimeDescr = _AlarmCurrTimeDescr_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 2, 3, 1, 12),
    _AlarmCurrTimeDescr_Type()
)
alarmCurrTimeDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmCurrTimeDescr.setStatus("current")


class _AlarmCurrSeverity_Type(Integer32):
    """Custom type alarmCurrSeverity based on Integer32"""
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
        *(("critical", 1),
          ("major", 2),
          ("minor", 3),
          ("info", 4))
    )


_AlarmCurrSeverity_Type.__name__ = "Integer32"
_AlarmCurrSeverity_Object = MibTableColumn
alarmCurrSeverity = _AlarmCurrSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 2, 3, 1, 13),
    _AlarmCurrSeverity_Type()
)
alarmCurrSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmCurrSeverity.setStatus("current")
_AlarmCurrDescr_Type = DisplayString
_AlarmCurrDescr_Object = MibTableColumn
alarmCurrDescr = _AlarmCurrDescr_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 2, 3, 1, 14),
    _AlarmCurrDescr_Type()
)
alarmCurrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmCurrDescr.setStatus("current")
_AlarmSeverityPortTable_Object = MibTable
alarmSeverityPortTable = _AlarmSeverityPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 2, 4)
)
if mibBuilder.loadTexts:
    alarmSeverityPortTable.setStatus("current")
_AlarmSeverityPortEntry_Object = MibTableRow
alarmSeverityPortEntry = _AlarmSeverityPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 2, 4, 1)
)
alarmSeverityPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    alarmSeverityPortEntry.setStatus("current")


class _SeverityThresh_Type(Integer32):
    """Custom type severityThresh based on Integer32"""
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
        *(("critical", 1),
          ("major", 2),
          ("minor", 3),
          ("info", 4))
    )


_SeverityThresh_Type.__name__ = "Integer32"
_SeverityThresh_Object = MibTableColumn
severityThresh = _SeverityThresh_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 2, 4, 1, 1),
    _SeverityThresh_Type()
)
severityThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityThresh.setStatus("current")
_Diagnostic_ObjectIdentity = ObjectIdentity
diagnostic = _Diagnostic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 4)
)
_Selt_ObjectIdentity = ObjectIdentity
selt = _Selt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 4, 3)
)
_SeltTarget_Type = Integer32
_SeltTarget_Object = MibScalar
seltTarget = _SeltTarget_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 4, 3, 1),
    _SeltTarget_Type()
)
seltTarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    seltTarget.setStatus("current")
_SeltOps_Type = Integer32
_SeltOps_Object = MibScalar
seltOps = _SeltOps_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 4, 3, 2),
    _SeltOps_Type()
)
seltOps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    seltOps.setStatus("current")
_SeltStatus_Type = DisplayString
_SeltStatus_Object = MibScalar
seltStatus = _SeltStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 4, 3, 3),
    _SeltStatus_Type()
)
seltStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    seltStatus.setStatus("current")


class _SeltCableType_Type(Integer32):
    """Custom type seltCableType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("awg24", 1),
          ("awg26", 2))
    )


_SeltCableType_Type.__name__ = "Integer32"
_SeltCableType_Object = MibScalar
seltCableType = _SeltCableType_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 4, 3, 4),
    _SeltCableType_Type()
)
seltCableType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    seltCableType.setStatus("current")
_SeltLoopEstimateLengthFt_Type = Integer32
_SeltLoopEstimateLengthFt_Object = MibScalar
seltLoopEstimateLengthFt = _SeltLoopEstimateLengthFt_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 4, 3, 5),
    _SeltLoopEstimateLengthFt_Type()
)
seltLoopEstimateLengthFt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    seltLoopEstimateLengthFt.setStatus("current")
if mibBuilder.loadTexts:
    seltLoopEstimateLengthFt.setUnits("feet")
_SeltLoopEstimateLengthMeter_Type = Integer32
_SeltLoopEstimateLengthMeter_Object = MibScalar
seltLoopEstimateLengthMeter = _SeltLoopEstimateLengthMeter_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 4, 3, 6),
    _SeltLoopEstimateLengthMeter_Type()
)
seltLoopEstimateLengthMeter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    seltLoopEstimateLengthMeter.setStatus("current")
if mibBuilder.loadTexts:
    seltLoopEstimateLengthMeter.setUnits("meter")
_Ldm_ObjectIdentity = ObjectIdentity
ldm = _Ldm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 4, 4)
)
_LdmTarget_Type = Integer32
_LdmTarget_Object = MibScalar
ldmTarget = _LdmTarget_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 4, 4, 1),
    _LdmTarget_Type()
)
ldmTarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ldmTarget.setStatus("current")
_LdmOps_Type = Integer32
_LdmOps_Object = MibScalar
ldmOps = _LdmOps_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 4, 4, 2),
    _LdmOps_Type()
)
ldmOps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ldmOps.setStatus("current")
_LdmStatus_Type = DisplayString
_LdmStatus_Object = MibScalar
ldmStatus = _LdmStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 4, 4, 3),
    _LdmStatus_Type()
)
ldmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldmStatus.setStatus("current")
_LdmXtucLoopAttenuation_Type = Integer32
_LdmXtucLoopAttenuation_Object = MibScalar
ldmXtucLoopAttenuation = _LdmXtucLoopAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 4, 4, 4),
    _LdmXtucLoopAttenuation_Type()
)
ldmXtucLoopAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldmXtucLoopAttenuation.setStatus("current")
if mibBuilder.loadTexts:
    ldmXtucLoopAttenuation.setUnits("tenth dB")
_LdmXtucSignalAttenuation_Type = Integer32
_LdmXtucSignalAttenuation_Object = MibScalar
ldmXtucSignalAttenuation = _LdmXtucSignalAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 4, 4, 5),
    _LdmXtucSignalAttenuation_Type()
)
ldmXtucSignalAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldmXtucSignalAttenuation.setStatus("current")
if mibBuilder.loadTexts:
    ldmXtucSignalAttenuation.setUnits("tenth dB")
_LdmXtucSignalMargin_Type = Integer32
_LdmXtucSignalMargin_Object = MibScalar
ldmXtucSignalMargin = _LdmXtucSignalMargin_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 4, 4, 6),
    _LdmXtucSignalMargin_Type()
)
ldmXtucSignalMargin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldmXtucSignalMargin.setStatus("current")
if mibBuilder.loadTexts:
    ldmXtucSignalMargin.setUnits("tenth dB")
_LdmXtucAggregateTxPower_Type = Integer32
_LdmXtucAggregateTxPower_Object = MibScalar
ldmXtucAggregateTxPower = _LdmXtucAggregateTxPower_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 4, 4, 7),
    _LdmXtucAggregateTxPower_Type()
)
ldmXtucAggregateTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldmXtucAggregateTxPower.setStatus("current")
if mibBuilder.loadTexts:
    ldmXtucAggregateTxPower.setUnits("tenth dB")
_LdmXtucAttainableBitRate_Type = Unsigned32
_LdmXtucAttainableBitRate_Object = MibScalar
ldmXtucAttainableBitRate = _LdmXtucAttainableBitRate_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 4, 4, 8),
    _LdmXtucAttainableBitRate_Type()
)
ldmXtucAttainableBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldmXtucAttainableBitRate.setStatus("current")
if mibBuilder.loadTexts:
    ldmXtucAttainableBitRate.setUnits("bits per second")
_LdmXturLoopAttenuation_Type = Integer32
_LdmXturLoopAttenuation_Object = MibScalar
ldmXturLoopAttenuation = _LdmXturLoopAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 4, 4, 9),
    _LdmXturLoopAttenuation_Type()
)
ldmXturLoopAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldmXturLoopAttenuation.setStatus("current")
if mibBuilder.loadTexts:
    ldmXturLoopAttenuation.setUnits("tenth dB")
_LdmXturSignalAttenuation_Type = Integer32
_LdmXturSignalAttenuation_Object = MibScalar
ldmXturSignalAttenuation = _LdmXturSignalAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 4, 4, 10),
    _LdmXturSignalAttenuation_Type()
)
ldmXturSignalAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldmXturSignalAttenuation.setStatus("current")
if mibBuilder.loadTexts:
    ldmXturSignalAttenuation.setUnits("tenth dB")
_LdmXturSignalMargin_Type = Integer32
_LdmXturSignalMargin_Object = MibScalar
ldmXturSignalMargin = _LdmXturSignalMargin_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 4, 4, 11),
    _LdmXturSignalMargin_Type()
)
ldmXturSignalMargin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldmXturSignalMargin.setStatus("current")
if mibBuilder.loadTexts:
    ldmXturSignalMargin.setUnits("tenth dB")
_LdmXturAggregateTxPower_Type = Integer32
_LdmXturAggregateTxPower_Object = MibScalar
ldmXturAggregateTxPower = _LdmXturAggregateTxPower_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 4, 4, 12),
    _LdmXturAggregateTxPower_Type()
)
ldmXturAggregateTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldmXturAggregateTxPower.setStatus("current")
if mibBuilder.loadTexts:
    ldmXturAggregateTxPower.setUnits("tenth dB")
_LdmXturAttainableBitRate_Type = Unsigned32
_LdmXturAttainableBitRate_Object = MibScalar
ldmXturAttainableBitRate = _LdmXturAttainableBitRate_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 4, 4, 13),
    _LdmXturAttainableBitRate_Type()
)
ldmXturAttainableBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldmXturAttainableBitRate.setStatus("current")
if mibBuilder.loadTexts:
    ldmXturAttainableBitRate.setUnits("bits per second")
_LdmXtucNumOfSubcarriersPerPort_Type = Integer32
_LdmXtucNumOfSubcarriersPerPort_Object = MibScalar
ldmXtucNumOfSubcarriersPerPort = _LdmXtucNumOfSubcarriersPerPort_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 4, 4, 14),
    _LdmXtucNumOfSubcarriersPerPort_Type()
)
ldmXtucNumOfSubcarriersPerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldmXtucNumOfSubcarriersPerPort.setStatus("current")
_LdmXturNumOfSubcarriersPerPort_Type = Integer32
_LdmXturNumOfSubcarriersPerPort_Object = MibScalar
ldmXturNumOfSubcarriersPerPort = _LdmXturNumOfSubcarriersPerPort_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 4, 4, 15),
    _LdmXturNumOfSubcarriersPerPort_Type()
)
ldmXturNumOfSubcarriersPerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldmXturNumOfSubcarriersPerPort.setStatus("current")
_LdmXtucHlinScale_Type = Integer32
_LdmXtucHlinScale_Object = MibScalar
ldmXtucHlinScale = _LdmXtucHlinScale_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 4, 4, 16),
    _LdmXtucHlinScale_Type()
)
ldmXtucHlinScale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldmXtucHlinScale.setStatus("current")
_LdmXtucHlinReal1_Type = OctetString
_LdmXtucHlinReal1_Object = MibScalar
ldmXtucHlinReal1 = _LdmXtucHlinReal1_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 4, 4, 17),
    _LdmXtucHlinReal1_Type()
)
ldmXtucHlinReal1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldmXtucHlinReal1.setStatus("current")
_LdmXtucHlinReal2_Type = OctetString
_LdmXtucHlinReal2_Object = MibScalar
ldmXtucHlinReal2 = _LdmXtucHlinReal2_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 4, 4, 18),
    _LdmXtucHlinReal2_Type()
)
ldmXtucHlinReal2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldmXtucHlinReal2.setStatus("current")
_LdmXtucHlinImage1_Type = OctetString
_LdmXtucHlinImage1_Object = MibScalar
ldmXtucHlinImage1 = _LdmXtucHlinImage1_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 4, 4, 19),
    _LdmXtucHlinImage1_Type()
)
ldmXtucHlinImage1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldmXtucHlinImage1.setStatus("current")
_LdmXtucHlinImage2_Type = OctetString
_LdmXtucHlinImage2_Object = MibScalar
ldmXtucHlinImage2 = _LdmXtucHlinImage2_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 4, 4, 20),
    _LdmXtucHlinImage2_Type()
)
ldmXtucHlinImage2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldmXtucHlinImage2.setStatus("current")
_LdmXtucHlog1_Type = OctetString
_LdmXtucHlog1_Object = MibScalar
ldmXtucHlog1 = _LdmXtucHlog1_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 4, 4, 21),
    _LdmXtucHlog1_Type()
)
ldmXtucHlog1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldmXtucHlog1.setStatus("current")
_LdmXtucHlog2_Type = OctetString
_LdmXtucHlog2_Object = MibScalar
ldmXtucHlog2 = _LdmXtucHlog2_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 4, 4, 22),
    _LdmXtucHlog2_Type()
)
ldmXtucHlog2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldmXtucHlog2.setStatus("current")
_LdmXtucQln1_Type = OctetString
_LdmXtucQln1_Object = MibScalar
ldmXtucQln1 = _LdmXtucQln1_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 4, 4, 23),
    _LdmXtucQln1_Type()
)
ldmXtucQln1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldmXtucQln1.setStatus("current")
_LdmXtucQln2_Type = OctetString
_LdmXtucQln2_Object = MibScalar
ldmXtucQln2 = _LdmXtucQln2_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 4, 4, 24),
    _LdmXtucQln2_Type()
)
ldmXtucQln2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldmXtucQln2.setStatus("current")
_LdmXtucSnr1_Type = OctetString
_LdmXtucSnr1_Object = MibScalar
ldmXtucSnr1 = _LdmXtucSnr1_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 4, 4, 25),
    _LdmXtucSnr1_Type()
)
ldmXtucSnr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldmXtucSnr1.setStatus("current")
_LdmXtucSnr2_Type = OctetString
_LdmXtucSnr2_Object = MibScalar
ldmXtucSnr2 = _LdmXtucSnr2_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 4, 4, 26),
    _LdmXtucSnr2_Type()
)
ldmXtucSnr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldmXtucSnr2.setStatus("current")
_LdmXturHlinScale_Type = Integer32
_LdmXturHlinScale_Object = MibScalar
ldmXturHlinScale = _LdmXturHlinScale_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 4, 4, 27),
    _LdmXturHlinScale_Type()
)
ldmXturHlinScale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldmXturHlinScale.setStatus("current")
_LdmXturHlinReal_Type = OctetString
_LdmXturHlinReal_Object = MibScalar
ldmXturHlinReal = _LdmXturHlinReal_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 4, 4, 28),
    _LdmXturHlinReal_Type()
)
ldmXturHlinReal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldmXturHlinReal.setStatus("current")
_LdmXturHlinImage_Type = OctetString
_LdmXturHlinImage_Object = MibScalar
ldmXturHlinImage = _LdmXturHlinImage_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 4, 4, 29),
    _LdmXturHlinImage_Type()
)
ldmXturHlinImage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldmXturHlinImage.setStatus("current")
_LdmXturHlog_Type = OctetString
_LdmXturHlog_Object = MibScalar
ldmXturHlog = _LdmXturHlog_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 4, 4, 30),
    _LdmXturHlog_Type()
)
ldmXturHlog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldmXturHlog.setStatus("current")
_LdmXturQln_Type = OctetString
_LdmXturQln_Object = MibScalar
ldmXturQln = _LdmXturQln_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 4, 4, 31),
    _LdmXturQln_Type()
)
ldmXturQln.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldmXturQln.setStatus("current")
_LdmXturSnr_Type = OctetString
_LdmXturSnr_Object = MibScalar
ldmXturSnr = _LdmXturSnr_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 4, 4, 32),
    _LdmXturSnr_Type()
)
ldmXturSnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldmXturSnr.setStatus("current")
_LdmXtucHlogGroupFactor_Type = OctetString
_LdmXtucHlogGroupFactor_Object = MibScalar
ldmXtucHlogGroupFactor = _LdmXtucHlogGroupFactor_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 4, 4, 33),
    _LdmXtucHlogGroupFactor_Type()
)
ldmXtucHlogGroupFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldmXtucHlogGroupFactor.setStatus("current")
_LdmXtucQlnGroupFactor_Type = OctetString
_LdmXtucQlnGroupFactor_Object = MibScalar
ldmXtucQlnGroupFactor = _LdmXtucQlnGroupFactor_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 4, 4, 34),
    _LdmXtucQlnGroupFactor_Type()
)
ldmXtucQlnGroupFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldmXtucQlnGroupFactor.setStatus("current")
_LdmXtucSnrGroupFactor_Type = OctetString
_LdmXtucSnrGroupFactor_Object = MibScalar
ldmXtucSnrGroupFactor = _LdmXtucSnrGroupFactor_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 4, 4, 35),
    _LdmXtucSnrGroupFactor_Type()
)
ldmXtucSnrGroupFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldmXtucSnrGroupFactor.setStatus("current")
_LdmXturHlogGroupFactor_Type = OctetString
_LdmXturHlogGroupFactor_Object = MibScalar
ldmXturHlogGroupFactor = _LdmXturHlogGroupFactor_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 4, 4, 36),
    _LdmXturHlogGroupFactor_Type()
)
ldmXturHlogGroupFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldmXturHlogGroupFactor.setStatus("current")
_LdmXturQlnGroupFactor_Type = OctetString
_LdmXturQlnGroupFactor_Object = MibScalar
ldmXturQlnGroupFactor = _LdmXturQlnGroupFactor_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 4, 4, 37),
    _LdmXturQlnGroupFactor_Type()
)
ldmXturQlnGroupFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldmXturQlnGroupFactor.setStatus("current")
_LdmXturSnrGroupFactor_Type = OctetString
_LdmXturSnrGroupFactor_Object = MibScalar
ldmXturSnrGroupFactor = _LdmXturSnrGroupFactor_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 4, 4, 38),
    _LdmXturSnrGroupFactor_Type()
)
ldmXturSnrGroupFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldmXturSnrGroupFactor.setStatus("current")
_Mlt_ObjectIdentity = ObjectIdentity
mlt = _Mlt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 4, 5)
)
_MltTarget_Type = Integer32
_MltTarget_Object = MibScalar
mltTarget = _MltTarget_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 4, 5, 1),
    _MltTarget_Type()
)
mltTarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltTarget.setStatus("current")
_MltOps_Type = Integer32
_MltOps_Object = MibScalar
mltOps = _MltOps_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 4, 5, 2),
    _MltOps_Type()
)
mltOps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltOps.setStatus("current")


class _MltOption_Type(Integer32):
    """Custom type mltOption based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("vac", 2),
          ("vdc", 3),
          ("rload", 4),
          ("riso", 5),
          ("cap", 6),
          ("ren", 7),
          ("ring", 8),
          ("metering", 9))
    )


_MltOption_Type.__name__ = "Integer32"
_MltOption_Object = MibScalar
mltOption = _MltOption_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 4, 5, 3),
    _MltOption_Type()
)
mltOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltOption.setStatus("current")


class _MltForce_Type(Integer32):
    """Custom type mltForce based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("force", 1),
          ("notForce", 2))
    )


_MltForce_Type.__name__ = "Integer32"
_MltForce_Object = MibScalar
mltForce = _MltForce_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 4, 5, 4),
    _MltForce_Type()
)
mltForce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltForce.setStatus("current")
_MltResult_ObjectIdentity = ObjectIdentity
mltResult = _MltResult_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 4, 5, 5)
)
_MltVacTip_Type = Integer32
_MltVacTip_Object = MibScalar
mltVacTip = _MltVacTip_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 4, 5, 5, 1),
    _MltVacTip_Type()
)
mltVacTip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltVacTip.setStatus("current")
if mibBuilder.loadTexts:
    mltVacTip.setUnits("0.1 rms")
_MltVacRing_Type = Integer32
_MltVacRing_Object = MibScalar
mltVacRing = _MltVacRing_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 4, 5, 5, 2),
    _MltVacRing_Type()
)
mltVacRing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltVacRing.setStatus("current")
if mibBuilder.loadTexts:
    mltVacRing.setUnits("0.1 rms")
_MltVacDiff_Type = Integer32
_MltVacDiff_Object = MibScalar
mltVacDiff = _MltVacDiff_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 4, 5, 5, 3),
    _MltVacDiff_Type()
)
mltVacDiff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltVacDiff.setStatus("current")
if mibBuilder.loadTexts:
    mltVacDiff.setUnits("0.1 rms")
_MltVdcTip_Type = Integer32
_MltVdcTip_Object = MibScalar
mltVdcTip = _MltVdcTip_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 4, 5, 5, 4),
    _MltVdcTip_Type()
)
mltVdcTip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltVdcTip.setStatus("current")
if mibBuilder.loadTexts:
    mltVdcTip.setUnits("0.1 volt")
_MltVdcRing_Type = Integer32
_MltVdcRing_Object = MibScalar
mltVdcRing = _MltVdcRing_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 4, 5, 5, 5),
    _MltVdcRing_Type()
)
mltVdcRing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltVdcRing.setStatus("current")
if mibBuilder.loadTexts:
    mltVdcRing.setUnits("0.1 volt")
_MltVdcDiff_Type = Integer32
_MltVdcDiff_Object = MibScalar
mltVdcDiff = _MltVdcDiff_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 4, 5, 5, 6),
    _MltVdcDiff_Type()
)
mltVdcDiff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltVdcDiff.setStatus("current")
if mibBuilder.loadTexts:
    mltVdcDiff.setUnits("0.1 volt")
_MltRLoop_Type = Integer32
_MltRLoop_Object = MibScalar
mltRLoop = _MltRLoop_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 4, 5, 5, 7),
    _MltRLoop_Type()
)
mltRLoop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltRLoop.setStatus("current")
if mibBuilder.loadTexts:
    mltRLoop.setUnits("0.1 ohm")
_MltRtg_Type = Integer32
_MltRtg_Object = MibScalar
mltRtg = _MltRtg_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 4, 5, 5, 8),
    _MltRtg_Type()
)
mltRtg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltRtg.setStatus("current")
if mibBuilder.loadTexts:
    mltRtg.setUnits("0.1 ohm")
_MltRrg_Type = Integer32
_MltRrg_Object = MibScalar
mltRrg = _MltRrg_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 4, 5, 5, 9),
    _MltRrg_Type()
)
mltRrg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltRrg.setStatus("current")
if mibBuilder.loadTexts:
    mltRrg.setUnits("0.1 ohm")
_MltRtr_Type = Integer32
_MltRtr_Object = MibScalar
mltRtr = _MltRtr_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 4, 5, 5, 10),
    _MltRtr_Type()
)
mltRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltRtr.setStatus("current")
if mibBuilder.loadTexts:
    mltRtr.setUnits("0.1 ohm")
_MltCtg_Type = Integer32
_MltCtg_Object = MibScalar
mltCtg = _MltCtg_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 4, 5, 5, 11),
    _MltCtg_Type()
)
mltCtg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltCtg.setStatus("current")
if mibBuilder.loadTexts:
    mltCtg.setUnits("10^-9 F")
_MltCrg_Type = Integer32
_MltCrg_Object = MibScalar
mltCrg = _MltCrg_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 4, 5, 5, 12),
    _MltCrg_Type()
)
mltCrg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltCrg.setStatus("current")
if mibBuilder.loadTexts:
    mltCrg.setUnits("10^-9 F")
_MltCtr_Type = Integer32
_MltCtr_Object = MibScalar
mltCtr = _MltCtr_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 4, 5, 5, 13),
    _MltCtr_Type()
)
mltCtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltCtr.setStatus("current")
if mibBuilder.loadTexts:
    mltCtr.setUnits("10^-9 F")
_MltRen_Type = Integer32
_MltRen_Object = MibScalar
mltRen = _MltRen_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 4, 5, 5, 14),
    _MltRen_Type()
)
mltRen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltRen.setStatus("current")
if mibBuilder.loadTexts:
    mltRen.setUnits("0.1 ren")
_MltVRing_Type = Integer32
_MltVRing_Object = MibScalar
mltVRing = _MltVRing_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 4, 5, 5, 15),
    _MltVRing_Type()
)
mltVRing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltVRing.setStatus("current")
if mibBuilder.loadTexts:
    mltVRing.setUnits("0.1 rms")
_MltVMetering_Type = Integer32
_MltVMetering_Object = MibScalar
mltVMetering = _MltVMetering_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 4, 5, 5, 16),
    _MltVMetering_Type()
)
mltVMetering.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltVMetering.setStatus("current")
if mibBuilder.loadTexts:
    mltVMetering.setUnits("0.1 vpeak")


class _MltDialToneDetected_Type(Integer32):
    """Custom type mltDialToneDetected based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_MltDialToneDetected_Type.__name__ = "Integer32"
_MltDialToneDetected_Object = MibScalar
mltDialToneDetected = _MltDialToneDetected_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 4, 5, 5, 17),
    _MltDialToneDetected_Type()
)
mltDialToneDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltDialToneDetected.setStatus("current")
_MltDetectedDtmfCount_Type = Integer32
_MltDetectedDtmfCount_Object = MibScalar
mltDetectedDtmfCount = _MltDetectedDtmfCount_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 4, 5, 5, 18),
    _MltDetectedDtmfCount_Type()
)
mltDetectedDtmfCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltDetectedDtmfCount.setStatus("current")
_MltDialToneDelay_Type = Integer32
_MltDialToneDelay_Object = MibScalar
mltDialToneDelay = _MltDialToneDelay_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 4, 5, 5, 19),
    _MltDialToneDelay_Type()
)
mltDialToneDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltDialToneDelay.setStatus("current")
if mibBuilder.loadTexts:
    mltDialToneDelay.setUnits("0.001 sec")
_MltRelayTable_Object = MibTable
mltRelayTable = _MltRelayTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 4, 5, 6)
)
if mibBuilder.loadTexts:
    mltRelayTable.setStatus("current")
_MltRelayEntry_Object = MibTableRow
mltRelayEntry = _MltRelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 4, 5, 6, 1)
)
mltRelayEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    mltRelayEntry.setStatus("current")


class _MltRelaySet_Type(Integer32):
    """Custom type mltRelaySet based on Integer32"""
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
        *(("in", 1),
          ("out", 2),
          ("both", 3),
          ("off", 4))
    )


_MltRelaySet_Type.__name__ = "Integer32"
_MltRelaySet_Object = MibTableColumn
mltRelaySet = _MltRelaySet_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 4, 5, 6, 1, 1),
    _MltRelaySet_Type()
)
mltRelaySet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltRelaySet.setStatus("current")
_Multicast_ObjectIdentity = ObjectIdentity
multicast = _Multicast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 7)
)


class _IgmpEnable_Type(Integer32):
    """Custom type igmpEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enableProxy", 1),
          ("enableSnooping", 2),
          ("disable", 3))
    )


_IgmpEnable_Type.__name__ = "Integer32"
_IgmpEnable_Object = MibScalar
igmpEnable = _IgmpEnable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 7, 1),
    _IgmpEnable_Type()
)
igmpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpEnable.setStatus("current")
_McastBandwidth_ObjectIdentity = ObjectIdentity
mcastBandwidth = _McastBandwidth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 7, 4)
)


class _McastDefaultBandwidth_Type(Integer32):
    """Custom type mcastDefaultBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100000),
    )


_McastDefaultBandwidth_Type.__name__ = "Integer32"
_McastDefaultBandwidth_Object = MibScalar
mcastDefaultBandwidth = _McastDefaultBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 7, 4, 1),
    _McastDefaultBandwidth_Type()
)
mcastDefaultBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcastDefaultBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    mcastDefaultBandwidth.setUnits("Kbps")
_MaxNumOfMcastBw_Type = Integer32
_MaxNumOfMcastBw_Object = MibScalar
maxNumOfMcastBw = _MaxNumOfMcastBw_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 7, 4, 2),
    _MaxNumOfMcastBw_Type()
)
maxNumOfMcastBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumOfMcastBw.setStatus("current")
_McastBwTable_Object = MibTable
mcastBwTable = _McastBwTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 7, 4, 3)
)
if mibBuilder.loadTexts:
    mcastBwTable.setStatus("current")
_McastBwEntry_Object = MibTableRow
mcastBwEntry = _McastBwEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 7, 4, 3, 1)
)
mcastBwEntry.setIndexNames(
    (0, "E5-121-MIB", "mcastBwIndex"),
    (0, "E5-121-MIB", "mcastBwStartIp"),
    (0, "E5-121-MIB", "mcastBwEndIp"),
)
if mibBuilder.loadTexts:
    mcastBwEntry.setStatus("current")
_McastBwIndex_Type = Integer32
_McastBwIndex_Object = MibTableColumn
mcastBwIndex = _McastBwIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 7, 4, 3, 1, 1),
    _McastBwIndex_Type()
)
mcastBwIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcastBwIndex.setStatus("current")
_McastBwStartIp_Type = IpAddress
_McastBwStartIp_Object = MibTableColumn
mcastBwStartIp = _McastBwStartIp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 7, 4, 3, 1, 2),
    _McastBwStartIp_Type()
)
mcastBwStartIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcastBwStartIp.setStatus("current")
_McastBwEndIp_Type = IpAddress
_McastBwEndIp_Object = MibTableColumn
mcastBwEndIp = _McastBwEndIp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 7, 4, 3, 1, 3),
    _McastBwEndIp_Type()
)
mcastBwEndIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcastBwEndIp.setStatus("current")
_McastBwBandwidth_Type = Integer32
_McastBwBandwidth_Object = MibTableColumn
mcastBwBandwidth = _McastBwBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 7, 4, 3, 1, 4),
    _McastBwBandwidth_Type()
)
mcastBwBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mcastBwBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    mcastBwBandwidth.setUnits("Kbps")
_McastBwRowStatus_Type = RowStatus
_McastBwRowStatus_Object = MibTableColumn
mcastBwRowStatus = _McastBwRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 7, 4, 3, 1, 5),
    _McastBwRowStatus_Type()
)
mcastBwRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mcastBwRowStatus.setStatus("current")
_McastBwPortTable_Object = MibTable
mcastBwPortTable = _McastBwPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 7, 4, 4)
)
if mibBuilder.loadTexts:
    mcastBwPortTable.setStatus("current")
_McastBwPortEntry_Object = MibTableRow
mcastBwPortEntry = _McastBwPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 7, 4, 4, 1)
)
mcastBwPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    mcastBwPortEntry.setStatus("current")


class _McastBwPortEnable_Type(Integer32):
    """Custom type mcastBwPortEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_McastBwPortEnable_Type.__name__ = "Integer32"
_McastBwPortEnable_Object = MibTableColumn
mcastBwPortEnable = _McastBwPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 7, 4, 4, 1, 1),
    _McastBwPortEnable_Type()
)
mcastBwPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcastBwPortEnable.setStatus("current")
_McastBwPortBandwidth_Type = Integer32
_McastBwPortBandwidth_Object = MibTableColumn
mcastBwPortBandwidth = _McastBwPortBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 7, 4, 4, 1, 2),
    _McastBwPortBandwidth_Type()
)
mcastBwPortBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcastBwPortBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    mcastBwPortBandwidth.setUnits("Kbps")
_IgmpCount_ObjectIdentity = ObjectIdentity
igmpCount = _IgmpCount_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 7, 5)
)
_IgmpCountPortTable_Object = MibTable
igmpCountPortTable = _IgmpCountPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 7, 5, 1)
)
if mibBuilder.loadTexts:
    igmpCountPortTable.setStatus("current")
_IgmpCountPortEntry_Object = MibTableRow
igmpCountPortEntry = _IgmpCountPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 7, 5, 1, 1)
)
igmpCountPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    igmpCountPortEntry.setStatus("current")


class _IgmpCountPortEnable_Type(Integer32):
    """Custom type igmpCountPortEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_IgmpCountPortEnable_Type.__name__ = "Integer32"
_IgmpCountPortEnable_Object = MibTableColumn
igmpCountPortEnable = _IgmpCountPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 7, 5, 1, 1, 1),
    _IgmpCountPortEnable_Type()
)
igmpCountPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpCountPortEnable.setStatus("current")


class _IgmpCountPortLimit_Type(Integer32):
    """Custom type igmpCountPortLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_IgmpCountPortLimit_Type.__name__ = "Integer32"
_IgmpCountPortLimit_Object = MibTableColumn
igmpCountPortLimit = _IgmpCountPortLimit_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 7, 5, 1, 1, 2),
    _IgmpCountPortLimit_Type()
)
igmpCountPortLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpCountPortLimit.setStatus("current")
_Mvlan_ObjectIdentity = ObjectIdentity
mvlan = _Mvlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 7, 6)
)
_MaxNumOfMvlan_Type = Integer32
_MaxNumOfMvlan_Object = MibScalar
maxNumOfMvlan = _MaxNumOfMvlan_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 7, 6, 1),
    _MaxNumOfMvlan_Type()
)
maxNumOfMvlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumOfMvlan.setStatus("current")
_MvlanTable_Object = MibTable
mvlanTable = _MvlanTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 7, 6, 2)
)
if mibBuilder.loadTexts:
    mvlanTable.setStatus("current")
_MvlanEntry_Object = MibTableRow
mvlanEntry = _MvlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 7, 6, 2, 1)
)
mvlanEntry.setIndexNames(
    (0, "E5-121-MIB", "mvlanIndex"),
)
if mibBuilder.loadTexts:
    mvlanEntry.setStatus("current")
_MvlanIndex_Type = VlanIndex
_MvlanIndex_Object = MibTableColumn
mvlanIndex = _MvlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 7, 6, 2, 1, 1),
    _MvlanIndex_Type()
)
mvlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvlanIndex.setStatus("current")


class _MvlanName_Type(DisplayString):
    """Custom type mvlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_MvlanName_Type.__name__ = "DisplayString"
_MvlanName_Object = MibTableColumn
mvlanName = _MvlanName_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 7, 6, 2, 1, 2),
    _MvlanName_Type()
)
mvlanName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mvlanName.setStatus("current")
_MvlanEgressPorts_Type = PortList
_MvlanEgressPorts_Object = MibTableColumn
mvlanEgressPorts = _MvlanEgressPorts_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 7, 6, 2, 1, 3),
    _MvlanEgressPorts_Type()
)
mvlanEgressPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mvlanEgressPorts.setStatus("current")
_MvlanUntaggedPorts_Type = PortList
_MvlanUntaggedPorts_Object = MibTableColumn
mvlanUntaggedPorts = _MvlanUntaggedPorts_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 7, 6, 2, 1, 4),
    _MvlanUntaggedPorts_Type()
)
mvlanUntaggedPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mvlanUntaggedPorts.setStatus("current")
_MvlanRowStatus_Type = RowStatus
_MvlanRowStatus_Object = MibTableColumn
mvlanRowStatus = _MvlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 7, 6, 2, 1, 5),
    _MvlanRowStatus_Type()
)
mvlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mvlanRowStatus.setStatus("current")
_MvlanTranslateTable_Object = MibTable
mvlanTranslateTable = _MvlanTranslateTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 7, 6, 3)
)
if mibBuilder.loadTexts:
    mvlanTranslateTable.setStatus("current")
_MvlanTranslateEntry_Object = MibTableRow
mvlanTranslateEntry = _MvlanTranslateEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 7, 6, 3, 1)
)
mvlanTranslateEntry.setIndexNames(
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
    (0, "E5-121-MIB", "mvlanTranslateIndex"),
)
if mibBuilder.loadTexts:
    mvlanTranslateEntry.setStatus("current")
_MvlanTranslateIndex_Type = Integer32
_MvlanTranslateIndex_Object = MibTableColumn
mvlanTranslateIndex = _MvlanTranslateIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 7, 6, 3, 1, 1),
    _MvlanTranslateIndex_Type()
)
mvlanTranslateIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvlanTranslateIndex.setStatus("current")
_MvlanTranslateStartIp_Type = IpAddress
_MvlanTranslateStartIp_Object = MibTableColumn
mvlanTranslateStartIp = _MvlanTranslateStartIp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 7, 6, 3, 1, 2),
    _MvlanTranslateStartIp_Type()
)
mvlanTranslateStartIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvlanTranslateStartIp.setStatus("current")
_MvlanTranslateEndIp_Type = IpAddress
_MvlanTranslateEndIp_Object = MibTableColumn
mvlanTranslateEndIp = _MvlanTranslateEndIp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 7, 6, 3, 1, 3),
    _MvlanTranslateEndIp_Type()
)
mvlanTranslateEndIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvlanTranslateEndIp.setStatus("current")
_QueryVid_ObjectIdentity = ObjectIdentity
queryVid = _QueryVid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 7, 7)
)
_MaxNumOfQryVid_Type = Integer32
_MaxNumOfQryVid_Object = MibScalar
maxNumOfQryVid = _MaxNumOfQryVid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 7, 7, 1),
    _MaxNumOfQryVid_Type()
)
maxNumOfQryVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumOfQryVid.setStatus("current")
_QryVidConfTable_Object = MibTable
qryVidConfTable = _QryVidConfTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 7, 7, 2)
)
if mibBuilder.loadTexts:
    qryVidConfTable.setStatus("current")
_QryVidConfEntry_Object = MibTableRow
qryVidConfEntry = _QryVidConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 7, 7, 2, 1)
)
qryVidConfEntry.setIndexNames(
    (0, "E5-121-MIB", "qryVid"),
)
if mibBuilder.loadTexts:
    qryVidConfEntry.setStatus("current")
_QryVid_Type = Integer32
_QryVid_Object = MibTableColumn
qryVid = _QryVid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 7, 7, 2, 1, 1),
    _QryVid_Type()
)
qryVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qryVid.setStatus("current")
_QryVidRowStatus_Type = RowStatus
_QryVidRowStatus_Object = MibTableColumn
qryVidRowStatus = _QryVidRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 7, 7, 2, 1, 2),
    _QryVidRowStatus_Type()
)
qryVidRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qryVidRowStatus.setStatus("current")
_QryVidStatusTable_Object = MibTable
qryVidStatusTable = _QryVidStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 7, 7, 3)
)
if mibBuilder.loadTexts:
    qryVidStatusTable.setStatus("current")
_QryVidStatusEntry_Object = MibTableRow
qryVidStatusEntry = _QryVidStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 7, 7, 3, 1)
)
qryVidStatusEntry.setIndexNames(
    (0, "E5-121-MIB", "qryVid"),
)
if mibBuilder.loadTexts:
    qryVidStatusEntry.setStatus("current")


class _QryVidType_Type(Integer32):
    """Custom type qryVidType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("dynamic", 2))
    )


_QryVidType_Type.__name__ = "Integer32"
_QryVidType_Object = MibTableColumn
qryVidType = _QryVidType_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 7, 7, 3, 1, 1),
    _QryVidType_Type()
)
qryVidType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qryVidType.setStatus("current")


class _IgmpVersion_Type(Integer32):
    """Custom type igmpVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("v2", 1),
          ("v3", 2))
    )


_IgmpVersion_Type.__name__ = "Integer32"
_IgmpVersion_Object = MibScalar
igmpVersion = _IgmpVersion_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 7, 9),
    _IgmpVersion_Type()
)
igmpVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpVersion.setStatus("current")


class _IgmpLeaveMode_Type(Integer32):
    """Custom type igmpLeaveMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("immediateLeave", 1),
          ("lastMemberQuery", 2))
    )


_IgmpLeaveMode_Type.__name__ = "Integer32"
_IgmpLeaveMode_Object = MibScalar
igmpLeaveMode = _IgmpLeaveMode_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 7, 10),
    _IgmpLeaveMode_Type()
)
igmpLeaveMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpLeaveMode.setStatus("current")
_IgmpTimer_ObjectIdentity = ObjectIdentity
igmpTimer = _IgmpTimer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 7, 11)
)


class _IgmpQryInterval_Type(Integer32):
    """Custom type igmpQryInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000),
    )


_IgmpQryInterval_Type.__name__ = "Integer32"
_IgmpQryInterval_Object = MibScalar
igmpQryInterval = _IgmpQryInterval_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 7, 11, 1),
    _IgmpQryInterval_Type()
)
igmpQryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpQryInterval.setStatus("current")


class _IgmpRobust_Type(Integer32):
    """Custom type igmpRobust based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_IgmpRobust_Type.__name__ = "Integer32"
_IgmpRobust_Object = MibScalar
igmpRobust = _IgmpRobust_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 7, 11, 2),
    _IgmpRobust_Type()
)
igmpRobust.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpRobust.setStatus("current")


class _IgmpQryRespInterval_Type(Integer32):
    """Custom type igmpQryRespInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_IgmpQryRespInterval_Type.__name__ = "Integer32"
_IgmpQryRespInterval_Object = MibScalar
igmpQryRespInterval = _IgmpQryRespInterval_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 7, 11, 3),
    _IgmpQryRespInterval_Type()
)
igmpQryRespInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpQryRespInterval.setStatus("current")


class _IgmpLastMemQryInterval_Type(Integer32):
    """Custom type igmpLastMemQryInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_IgmpLastMemQryInterval_Type.__name__ = "Integer32"
_IgmpLastMemQryInterval_Object = MibScalar
igmpLastMemQryInterval = _IgmpLastMemQryInterval_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 7, 11, 4),
    _IgmpLastMemQryInterval_Type()
)
igmpLastMemQryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpLastMemQryInterval.setStatus("current")


class _IgmpLastMemQryRobust_Type(Integer32):
    """Custom type igmpLastMemQryRobust based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_IgmpLastMemQryRobust_Type.__name__ = "Integer32"
_IgmpLastMemQryRobust_Object = MibScalar
igmpLastMemQryRobust = _IgmpLastMemQryRobust_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 7, 11, 5),
    _IgmpLastMemQryRobust_Type()
)
igmpLastMemQryRobust.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpLastMemQryRobust.setStatus("current")
_AuditQuery_ObjectIdentity = ObjectIdentity
auditQuery = _AuditQuery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 7, 12)
)


class _AuditQryEnable_Type(Integer32):
    """Custom type auditQryEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AuditQryEnable_Type.__name__ = "Integer32"
_AuditQryEnable_Object = MibScalar
auditQryEnable = _AuditQryEnable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 7, 12, 1),
    _AuditQryEnable_Type()
)
auditQryEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auditQryEnable.setStatus("current")


class _AuditQryInterval_Type(Integer32):
    """Custom type auditQryInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_AuditQryInterval_Type.__name__ = "Integer32"
_AuditQryInterval_Object = MibScalar
auditQryInterval = _AuditQryInterval_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 7, 12, 2),
    _AuditQryInterval_Type()
)
auditQryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auditQryInterval.setStatus("current")


class _AuditQryRobust_Type(Integer32):
    """Custom type auditQryRobust based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_AuditQryRobust_Type.__name__ = "Integer32"
_AuditQryRobust_Object = MibScalar
auditQryRobust = _AuditQryRobust_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 7, 12, 3),
    _AuditQryRobust_Type()
)
auditQryRobust.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auditQryRobust.setStatus("current")
_IgmpProfile_ObjectIdentity = ObjectIdentity
igmpProfile = _IgmpProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 7, 13)
)
_MaxNumberOfIgmpProfiles_Type = Integer32
_MaxNumberOfIgmpProfiles_Object = MibScalar
maxNumberOfIgmpProfiles = _MaxNumberOfIgmpProfiles_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 7, 13, 1),
    _MaxNumberOfIgmpProfiles_Type()
)
maxNumberOfIgmpProfiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumberOfIgmpProfiles.setStatus("current")
_IgmpProfileTable_Object = MibTable
igmpProfileTable = _IgmpProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 7, 13, 2)
)
if mibBuilder.loadTexts:
    igmpProfileTable.setStatus("current")
_IgmpProfileEntry_Object = MibTableRow
igmpProfileEntry = _IgmpProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 7, 13, 2, 1)
)
igmpProfileEntry.setIndexNames(
    (1, "E5-121-MIB", "igmpProfileName"),
)
if mibBuilder.loadTexts:
    igmpProfileEntry.setStatus("current")


class _IgmpProfileName_Type(DisplayString):
    """Custom type igmpProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_IgmpProfileName_Type.__name__ = "DisplayString"
_IgmpProfileName_Object = MibTableColumn
igmpProfileName = _IgmpProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 7, 13, 2, 1, 1),
    _IgmpProfileName_Type()
)
igmpProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpProfileName.setStatus("current")


class _IgmpProfileEnable_Type(Integer32):
    """Custom type igmpProfileEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_IgmpProfileEnable_Type.__name__ = "Integer32"
_IgmpProfileEnable_Object = MibTableColumn
igmpProfileEnable = _IgmpProfileEnable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 7, 13, 2, 1, 2),
    _IgmpProfileEnable_Type()
)
igmpProfileEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpProfileEnable.setStatus("current")


class _IgmpProfileMaxGroup_Type(Integer32):
    """Custom type igmpProfileMaxGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_IgmpProfileMaxGroup_Type.__name__ = "Integer32"
_IgmpProfileMaxGroup_Object = MibTableColumn
igmpProfileMaxGroup = _IgmpProfileMaxGroup_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 7, 13, 2, 1, 3),
    _IgmpProfileMaxGroup_Type()
)
igmpProfileMaxGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpProfileMaxGroup.setStatus("current")
_IgmpProfileRowStatus_Type = RowStatus
_IgmpProfileRowStatus_Object = MibTableColumn
igmpProfileRowStatus = _IgmpProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 7, 13, 2, 1, 4),
    _IgmpProfileRowStatus_Type()
)
igmpProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpProfileRowStatus.setStatus("current")
_IgmpFilterTable_Object = MibTable
igmpFilterTable = _IgmpFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 7, 13, 3)
)
if mibBuilder.loadTexts:
    igmpFilterTable.setStatus("current")
_IgmpFilterEntry_Object = MibTableRow
igmpFilterEntry = _IgmpFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 7, 13, 3, 1)
)
igmpFilterEntry.setIndexNames(
    (0, "E5-121-MIB", "igmpProfileName"),
    (0, "E5-121-MIB", "igmpFilterIndex"),
)
if mibBuilder.loadTexts:
    igmpFilterEntry.setStatus("current")
_IgmpFilterIndex_Type = Integer32
_IgmpFilterIndex_Object = MibTableColumn
igmpFilterIndex = _IgmpFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 7, 13, 3, 1, 1),
    _IgmpFilterIndex_Type()
)
igmpFilterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpFilterIndex.setStatus("current")
_IgmpFilterStartIp_Type = IpAddress
_IgmpFilterStartIp_Object = MibTableColumn
igmpFilterStartIp = _IgmpFilterStartIp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 7, 13, 3, 1, 2),
    _IgmpFilterStartIp_Type()
)
igmpFilterStartIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpFilterStartIp.setStatus("current")
_IgmpFilterEndIp_Type = IpAddress
_IgmpFilterEndIp_Object = MibTableColumn
igmpFilterEndIp = _IgmpFilterEndIp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 7, 13, 3, 1, 3),
    _IgmpFilterEndIp_Type()
)
igmpFilterEndIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpFilterEndIp.setStatus("current")
_IgmpProfilePortTable_Object = MibTable
igmpProfilePortTable = _IgmpProfilePortTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 7, 13, 4)
)
if mibBuilder.loadTexts:
    igmpProfilePortTable.setStatus("current")
_IgmpProfilePortEntry_Object = MibTableRow
igmpProfilePortEntry = _IgmpProfilePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 7, 13, 4, 1)
)
igmpProfilePortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    igmpProfilePortEntry.setStatus("current")


class _IgmpProfilePortProfile_Type(OctetString):
    """Custom type igmpProfilePortProfile based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_IgmpProfilePortProfile_Type.__name__ = "OctetString"
_IgmpProfilePortProfile_Object = MibTableColumn
igmpProfilePortProfile = _IgmpProfilePortProfile_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 7, 13, 4, 1, 1),
    _IgmpProfilePortProfile_Type()
)
igmpProfilePortProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpProfilePortProfile.setStatus("current")
_Port_ObjectIdentity = ObjectIdentity
port = _Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8)
)
_SubrPortTable_Object = MibTable
subrPortTable = _SubrPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 1)
)
if mibBuilder.loadTexts:
    subrPortTable.setStatus("current")
_SubrPortEntry_Object = MibTableRow
subrPortEntry = _SubrPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 1, 1)
)
subrPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    subrPortEntry.setStatus("current")


class _SubrPortName_Type(DisplayString):
    """Custom type subrPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_SubrPortName_Type.__name__ = "DisplayString"
_SubrPortName_Object = MibTableColumn
subrPortName = _SubrPortName_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 1, 1, 1),
    _SubrPortName_Type()
)
subrPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subrPortName.setStatus("current")


class _SubrPortTel_Type(DisplayString):
    """Custom type subrPortTel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_SubrPortTel_Type.__name__ = "DisplayString"
_SubrPortTel_Object = MibTableColumn
subrPortTel = _SubrPortTel_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 1, 1, 2),
    _SubrPortTel_Type()
)
subrPortTel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subrPortTel.setStatus("current")
_VdslPort_ObjectIdentity = ObjectIdentity
vdslPort = _VdslPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 3)
)
_VdslLineConfTable_Object = MibTable
vdslLineConfTable = _VdslLineConfTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 3, 1)
)
if mibBuilder.loadTexts:
    vdslLineConfTable.setStatus("current")
_VdslLineConfEntry_Object = MibTableRow
vdslLineConfEntry = _VdslLineConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 3, 1, 1)
)
vdslLineConfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    vdslLineConfEntry.setStatus("current")


class _VdslLineConfUpbo_Type(Integer32):
    """Custom type vdslLineConfUpbo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_VdslLineConfUpbo_Type.__name__ = "Integer32"
_VdslLineConfUpbo_Object = MibTableColumn
vdslLineConfUpbo = _VdslLineConfUpbo_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 3, 1, 1, 1),
    _VdslLineConfUpbo_Type()
)
vdslLineConfUpbo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdslLineConfUpbo.setStatus("current")


class _VdslLineConfVdslProfile_Type(Integer32):
    """Custom type vdslLineConfVdslProfile based on Integer32"""
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
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18)
        )
    )
    namedValues = NamedValues(
        *(("vdsl8a", 1),
          ("vdsl8b", 2),
          ("vdsl8c", 3),
          ("vdsl8d", 4),
          ("vdsl12a", 5),
          ("vdsl12b", 6),
          ("vdsl17a", 7),
          ("auto", 8),
          ("adsl2plus", 9),
          ("vdsl2", 10),
          ("gdmt", 11),
          ("glite", 12),
          ("adsl2", 13),
          ("t1413", 14),
          ("vdsl2adsl2", 15),
          ("vdsl2gdmt", 16),
          ("vdsl2glite", 17),
          ("vdsl2t1413", 18))
    )


_VdslLineConfVdslProfile_Type.__name__ = "Integer32"
_VdslLineConfVdslProfile_Object = MibTableColumn
vdslLineConfVdslProfile = _VdslLineConfVdslProfile_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 3, 1, 1, 2),
    _VdslLineConfVdslProfile_Type()
)
vdslLineConfVdslProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdslLineConfVdslProfile.setStatus("current")


class _VdslLineConfRfiBand_Type(Integer32):
    """Custom type vdslLineConfRfiBand based on Integer32"""
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
        *(("disable", 1),
          ("ansi", 2),
          ("etsi", 3),
          ("custom", 4))
    )


_VdslLineConfRfiBand_Type.__name__ = "Integer32"
_VdslLineConfRfiBand_Object = MibTableColumn
vdslLineConfRfiBand = _VdslLineConfRfiBand_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 3, 1, 1, 4),
    _VdslLineConfRfiBand_Type()
)
vdslLineConfRfiBand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdslLineConfRfiBand.setStatus("current")
_VdslLineConfIpqosProfile_Type = DisplayString
_VdslLineConfIpqosProfile_Object = MibTableColumn
vdslLineConfIpqosProfile = _VdslLineConfIpqosProfile_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 3, 1, 1, 5),
    _VdslLineConfIpqosProfile_Type()
)
vdslLineConfIpqosProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdslLineConfIpqosProfile.setStatus("current")


class _VdslLineConfVturInp_Type(Integer32):
    """Custom type vdslLineConfVturInp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 160),
    )


_VdslLineConfVturInp_Type.__name__ = "Integer32"
_VdslLineConfVturInp_Object = MibTableColumn
vdslLineConfVturInp = _VdslLineConfVturInp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 3, 1, 1, 6),
    _VdslLineConfVturInp_Type()
)
vdslLineConfVturInp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdslLineConfVturInp.setStatus("current")
if mibBuilder.loadTexts:
    vdslLineConfVturInp.setUnits("0.1 DTM symbol")


class _VdslLineConfVtucInp_Type(Integer32):
    """Custom type vdslLineConfVtucInp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 160),
    )


_VdslLineConfVtucInp_Type.__name__ = "Integer32"
_VdslLineConfVtucInp_Object = MibTableColumn
vdslLineConfVtucInp = _VdslLineConfVtucInp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 3, 1, 1, 7),
    _VdslLineConfVtucInp_Type()
)
vdslLineConfVtucInp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdslLineConfVtucInp.setStatus("current")
if mibBuilder.loadTexts:
    vdslLineConfVtucInp.setUnits("0.1 DTM symbol")
_VdslLineConfOptionMask_Type = Integer32
_VdslLineConfOptionMask_Object = MibTableColumn
vdslLineConfOptionMask = _VdslLineConfOptionMask_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 3, 1, 1, 8),
    _VdslLineConfOptionMask_Type()
)
vdslLineConfOptionMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdslLineConfOptionMask.setStatus("current")


class _VdslLineConfUpboForceLength_Type(Integer32):
    """Custom type vdslLineConfUpboForceLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-5, 1270),
    )


_VdslLineConfUpboForceLength_Type.__name__ = "Integer32"
_VdslLineConfUpboForceLength_Object = MibTableColumn
vdslLineConfUpboForceLength = _VdslLineConfUpboForceLength_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 3, 1, 1, 9),
    _VdslLineConfUpboForceLength_Type()
)
vdslLineConfUpboForceLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdslLineConfUpboForceLength.setStatus("current")
if mibBuilder.loadTexts:
    vdslLineConfUpboForceLength.setUnits("0.1dB")


class _VdslLineConfPsdShape_Type(Integer32):
    """Custom type vdslLineConfPsdShape based on Integer32"""
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
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53)
        )
    )
    namedValues = NamedValues(
        *(("vdsl2aNus0", 1),
          ("vdsl2aEu32", 2),
          ("vdsl2aEu36", 3),
          ("vdsl2aEu40", 4),
          ("vdsl2aEu44", 5),
          ("vdsl2aEu48", 6),
          ("vdsl2aEu52", 7),
          ("vdsl2aEu56", 8),
          ("vdsl2aEu60", 9),
          ("vdsl2aEu64", 10),
          ("vdsl2aEu128", 11),
          ("vdsl1fttexAnsiM1", 12),
          ("vdsl1fttexAnsiM2", 13),
          ("vdsl1fttcabAnsiM1", 14),
          ("vdsl1fttcabAnsiM2", 15),
          ("vdsl1fttexAnsiM1E", 16),
          ("vdsl1fttexAnsiM2E", 17),
          ("vdslFttcabAnsiM1E", 18),
          ("vdslFttcabAnsiM2E", 19),
          ("vdsl2aCt", 20),
          ("vdsl2b8x1", 21),
          ("vdsl2b8x2", 22),
          ("vdsl2b8x3", 23),
          ("vdsl2b8x4", 24),
          ("vdsl2b8x5", 25),
          ("vdsl2b8x6", 26),
          ("vdsl2b8x7", 27),
          ("vdsl2b8x8", 28),
          ("vdsl2b8x9", 29),
          ("vdsl2b8x10", 30),
          ("vdsl2b8x11", 31),
          ("vdsl2b8x12", 32),
          ("vdsl2b8x13", 33),
          ("vdsl2b8x14", 34),
          ("vdsl2b8x15", 35),
          ("vdsl2b8x16", 36),
          ("vdsl2b7x1", 37),
          ("vdsl2b7x2", 38),
          ("vdsl2b7x3", 39),
          ("vdsl2b7x4", 40),
          ("vdsl2b7x5", 41),
          ("vdsl2b7x6", 42),
          ("vdsl2b7x7", 43),
          ("vdsl2b7x8", 44),
          ("vdsl2b7x9", 45),
          ("vdsl2b7x10", 46),
          ("vdsl2btAnfp", 47),
          ("vdsl2c138b", 48),
          ("vdsl2c276b", 49),
          ("vdsl2c138co", 50),
          ("vdsl2c276co", 51),
          ("vdsl2cTcmisdn", 52),
          ("vdsl1QAMCompatible", 53))
    )


_VdslLineConfPsdShape_Type.__name__ = "Integer32"
_VdslLineConfPsdShape_Object = MibTableColumn
vdslLineConfPsdShape = _VdslLineConfPsdShape_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 3, 1, 1, 10),
    _VdslLineConfPsdShape_Type()
)
vdslLineConfPsdShape.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdslLineConfPsdShape.setStatus("current")


class _VdslLineConfDpbo_Type(Integer32):
    """Custom type vdslLineConfDpbo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_VdslLineConfDpbo_Type.__name__ = "Integer32"
_VdslLineConfDpbo_Object = MibTableColumn
vdslLineConfDpbo = _VdslLineConfDpbo_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 3, 1, 1, 11),
    _VdslLineConfDpbo_Type()
)
vdslLineConfDpbo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdslLineConfDpbo.setStatus("current")


class _VdslLineConfDpboParamEsel_Type(Integer32):
    """Custom type vdslLineConfDpboParamEsel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 511),
    )


_VdslLineConfDpboParamEsel_Type.__name__ = "Integer32"
_VdslLineConfDpboParamEsel_Object = MibTableColumn
vdslLineConfDpboParamEsel = _VdslLineConfDpboParamEsel_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 3, 1, 1, 12),
    _VdslLineConfDpboParamEsel_Type()
)
vdslLineConfDpboParamEsel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdslLineConfDpboParamEsel.setStatus("current")
if mibBuilder.loadTexts:
    vdslLineConfDpboParamEsel.setUnits("0.5dB")


class _VdslLineConfDpboParamEscma_Type(Integer32):
    """Custom type vdslLineConfDpboParamEscma based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 640),
    )


_VdslLineConfDpboParamEscma_Type.__name__ = "Integer32"
_VdslLineConfDpboParamEscma_Object = MibTableColumn
vdslLineConfDpboParamEscma = _VdslLineConfDpboParamEscma_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 3, 1, 1, 13),
    _VdslLineConfDpboParamEscma_Type()
)
vdslLineConfDpboParamEscma.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdslLineConfDpboParamEscma.setStatus("current")


class _VdslLineConfDpboParamEscmb_Type(Integer32):
    """Custom type vdslLineConfDpboParamEscmb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 640),
    )


_VdslLineConfDpboParamEscmb_Type.__name__ = "Integer32"
_VdslLineConfDpboParamEscmb_Object = MibTableColumn
vdslLineConfDpboParamEscmb = _VdslLineConfDpboParamEscmb_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 3, 1, 1, 14),
    _VdslLineConfDpboParamEscmb_Type()
)
vdslLineConfDpboParamEscmb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdslLineConfDpboParamEscmb.setStatus("current")


class _VdslLineConfDpboParamEscmc_Type(Integer32):
    """Custom type vdslLineConfDpboParamEscmc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 640),
    )


_VdslLineConfDpboParamEscmc_Type.__name__ = "Integer32"
_VdslLineConfDpboParamEscmc_Object = MibTableColumn
vdslLineConfDpboParamEscmc = _VdslLineConfDpboParamEscmc_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 3, 1, 1, 15),
    _VdslLineConfDpboParamEscmc_Type()
)
vdslLineConfDpboParamEscmc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdslLineConfDpboParamEscmc.setStatus("current")


class _VdslLineConfDpboParamMus_Type(Integer32):
    """Custom type vdslLineConfDpboParamMus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VdslLineConfDpboParamMus_Type.__name__ = "Integer32"
_VdslLineConfDpboParamMus_Object = MibTableColumn
vdslLineConfDpboParamMus = _VdslLineConfDpboParamMus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 3, 1, 1, 16),
    _VdslLineConfDpboParamMus_Type()
)
vdslLineConfDpboParamMus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdslLineConfDpboParamMus.setStatus("current")
if mibBuilder.loadTexts:
    vdslLineConfDpboParamMus.setUnits("-0.5 dBm/Hz")


class _VdslLineConfDpboParamFmin_Type(Integer32):
    """Custom type vdslLineConfDpboParamFmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )


_VdslLineConfDpboParamFmin_Type.__name__ = "Integer32"
_VdslLineConfDpboParamFmin_Object = MibTableColumn
vdslLineConfDpboParamFmin = _VdslLineConfDpboParamFmin_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 3, 1, 1, 17),
    _VdslLineConfDpboParamFmin_Type()
)
vdslLineConfDpboParamFmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdslLineConfDpboParamFmin.setStatus("current")
if mibBuilder.loadTexts:
    vdslLineConfDpboParamFmin.setUnits("4.3125kHz")


class _VdslLineConfDpboParamFmax_Type(Integer32):
    """Custom type vdslLineConfDpboParamFmax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 6956),
    )


_VdslLineConfDpboParamFmax_Type.__name__ = "Integer32"
_VdslLineConfDpboParamFmax_Object = MibTableColumn
vdslLineConfDpboParamFmax = _VdslLineConfDpboParamFmax_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 3, 1, 1, 18),
    _VdslLineConfDpboParamFmax_Type()
)
vdslLineConfDpboParamFmax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdslLineConfDpboParamFmax.setStatus("current")
if mibBuilder.loadTexts:
    vdslLineConfDpboParamFmax.setUnits("4.3125kHz")


class _VdslLineConfDpboParamPsdId_Type(Integer32):
    """Custom type vdslLineConfDpboParamPsdId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("psdCo", 1),
          ("psdFlat", 2),
          ("psdCabAnsi", 3),
          ("psdCabEtsi", 4),
          ("psdExchEtsi", 5),
          ("psdExchAnsi", 6))
    )


_VdslLineConfDpboParamPsdId_Type.__name__ = "Integer32"
_VdslLineConfDpboParamPsdId_Object = MibTableColumn
vdslLineConfDpboParamPsdId = _VdslLineConfDpboParamPsdId_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 3, 1, 1, 19),
    _VdslLineConfDpboParamPsdId_Type()
)
vdslLineConfDpboParamPsdId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdslLineConfDpboParamPsdId.setStatus("current")
_VdslVlan_ObjectIdentity = ObjectIdentity
vdslVlan = _VdslVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 3, 2)
)
_VdslPortConfTable_Object = MibTable
vdslPortConfTable = _VdslPortConfTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 3, 2, 1)
)
if mibBuilder.loadTexts:
    vdslPortConfTable.setStatus("current")
_VdslPortConfEntry_Object = MibTableRow
vdslPortConfEntry = _VdslPortConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 3, 2, 1, 1)
)
vdslPortConfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    vdslPortConfEntry.setStatus("current")


class _VdslPortConfTlsEnable_Type(Integer32):
    """Custom type vdslPortConfTlsEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_VdslPortConfTlsEnable_Type.__name__ = "Integer32"
_VdslPortConfTlsEnable_Object = MibTableColumn
vdslPortConfTlsEnable = _VdslPortConfTlsEnable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 3, 2, 1, 1, 4),
    _VdslPortConfTlsEnable_Type()
)
vdslPortConfTlsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdslPortConfTlsEnable.setStatus("current")
_VdslPortConfTlsVid_Type = VlanIndex
_VdslPortConfTlsVid_Object = MibTableColumn
vdslPortConfTlsVid = _VdslPortConfTlsVid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 3, 2, 1, 1, 5),
    _VdslPortConfTlsVid_Type()
)
vdslPortConfTlsVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdslPortConfTlsVid.setStatus("current")
_VdslPortConfTlsPriority_Type = Integer32
_VdslPortConfTlsPriority_Object = MibTableColumn
vdslPortConfTlsPriority = _VdslPortConfTlsPriority_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 3, 2, 1, 1, 6),
    _VdslPortConfTlsPriority_Type()
)
vdslPortConfTlsPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdslPortConfTlsPriority.setStatus("current")


class _VdslPortConfDtEnable_Type(Integer32):
    """Custom type vdslPortConfDtEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_VdslPortConfDtEnable_Type.__name__ = "Integer32"
_VdslPortConfDtEnable_Object = MibTableColumn
vdslPortConfDtEnable = _VdslPortConfDtEnable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 3, 2, 1, 1, 7),
    _VdslPortConfDtEnable_Type()
)
vdslPortConfDtEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdslPortConfDtEnable.setStatus("current")
_VdslPortConfDtSVid_Type = VlanIndex
_VdslPortConfDtSVid_Object = MibTableColumn
vdslPortConfDtSVid = _VdslPortConfDtSVid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 3, 2, 1, 1, 8),
    _VdslPortConfDtSVid_Type()
)
vdslPortConfDtSVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdslPortConfDtSVid.setStatus("current")
_VdslPortConfDtSPriority_Type = Integer32
_VdslPortConfDtSPriority_Object = MibTableColumn
vdslPortConfDtSPriority = _VdslPortConfDtSPriority_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 3, 2, 1, 1, 9),
    _VdslPortConfDtSPriority_Type()
)
vdslPortConfDtSPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdslPortConfDtSPriority.setStatus("current")
_VdslPortConfDtCVid_Type = VlanIndex
_VdslPortConfDtCVid_Object = MibTableColumn
vdslPortConfDtCVid = _VdslPortConfDtCVid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 3, 2, 1, 1, 10),
    _VdslPortConfDtCVid_Type()
)
vdslPortConfDtCVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdslPortConfDtCVid.setStatus("current")
_VdslPortConfDtCPriority_Type = Integer32
_VdslPortConfDtCPriority_Object = MibTableColumn
vdslPortConfDtCPriority = _VdslPortConfDtCPriority_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 3, 2, 1, 1, 11),
    _VdslPortConfDtCPriority_Type()
)
vdslPortConfDtCPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdslPortConfDtCPriority.setStatus("current")
_VdslPortVlanTranslateTable_Object = MibTable
vdslPortVlanTranslateTable = _VdslPortVlanTranslateTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 3, 2, 2)
)
if mibBuilder.loadTexts:
    vdslPortVlanTranslateTable.setStatus("current")
_VdslPortVlanTranslateEntry_Object = MibTableRow
vdslPortVlanTranslateEntry = _VdslPortVlanTranslateEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 3, 2, 2, 1)
)
vdslPortVlanTranslateEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "E5-121-MIB", "vdslPortVlanTranslateVpi"),
    (0, "E5-121-MIB", "vdslPortVlanTranslateVci"),
    (0, "E5-121-MIB", "vdslPortVlanTranslateCvid"),
)
if mibBuilder.loadTexts:
    vdslPortVlanTranslateEntry.setStatus("current")


class _VdslPortVlanTranslateVpi_Type(Integer32):
    """Custom type vdslPortVlanTranslateVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VdslPortVlanTranslateVpi_Type.__name__ = "Integer32"
_VdslPortVlanTranslateVpi_Object = MibTableColumn
vdslPortVlanTranslateVpi = _VdslPortVlanTranslateVpi_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 3, 2, 2, 1, 1),
    _VdslPortVlanTranslateVpi_Type()
)
vdslPortVlanTranslateVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslPortVlanTranslateVpi.setStatus("current")


class _VdslPortVlanTranslateVci_Type(Integer32):
    """Custom type vdslPortVlanTranslateVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_VdslPortVlanTranslateVci_Type.__name__ = "Integer32"
_VdslPortVlanTranslateVci_Object = MibTableColumn
vdslPortVlanTranslateVci = _VdslPortVlanTranslateVci_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 3, 2, 2, 1, 2),
    _VdslPortVlanTranslateVci_Type()
)
vdslPortVlanTranslateVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslPortVlanTranslateVci.setStatus("current")
_VdslPortVlanTranslateCxvid_Type = VlanIndex
_VdslPortVlanTranslateCxvid_Object = MibTableColumn
vdslPortVlanTranslateCxvid = _VdslPortVlanTranslateCxvid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 3, 2, 2, 1, 3),
    _VdslPortVlanTranslateCxvid_Type()
)
vdslPortVlanTranslateCxvid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslPortVlanTranslateCxvid.setStatus("current")
_VdslPortVlanTranslateCvid_Type = VlanIndex
_VdslPortVlanTranslateCvid_Object = MibTableColumn
vdslPortVlanTranslateCvid = _VdslPortVlanTranslateCvid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 3, 2, 2, 1, 4),
    _VdslPortVlanTranslateCvid_Type()
)
vdslPortVlanTranslateCvid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslPortVlanTranslateCvid.setStatus("current")
_VdslPortVlanTranslateSvid_Type = VlanIndex
_VdslPortVlanTranslateSvid_Object = MibTableColumn
vdslPortVlanTranslateSvid = _VdslPortVlanTranslateSvid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 3, 2, 2, 1, 5),
    _VdslPortVlanTranslateSvid_Type()
)
vdslPortVlanTranslateSvid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslPortVlanTranslateSvid.setStatus("current")


class _VdslPortVlanTranslateDsonly_Type(Integer32):
    """Custom type vdslPortVlanTranslateDsonly based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_VdslPortVlanTranslateDsonly_Type.__name__ = "Integer32"
_VdslPortVlanTranslateDsonly_Object = MibTableColumn
vdslPortVlanTranslateDsonly = _VdslPortVlanTranslateDsonly_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 3, 2, 2, 1, 6),
    _VdslPortVlanTranslateDsonly_Type()
)
vdslPortVlanTranslateDsonly.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslPortVlanTranslateDsonly.setStatus("current")
_VdslPortVlanTranslateRowStatus_Type = RowStatus
_VdslPortVlanTranslateRowStatus_Object = MibTableColumn
vdslPortVlanTranslateRowStatus = _VdslPortVlanTranslateRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 3, 2, 2, 1, 7),
    _VdslPortVlanTranslateRowStatus_Type()
)
vdslPortVlanTranslateRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vdslPortVlanTranslateRowStatus.setStatus("current")
_VdslPortPvlanTable_Object = MibTable
vdslPortPvlanTable = _VdslPortPvlanTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 3, 2, 4)
)
if mibBuilder.loadTexts:
    vdslPortPvlanTable.setStatus("current")
_VdslPortPvlanEntry_Object = MibTableRow
vdslPortPvlanEntry = _VdslPortPvlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 3, 2, 4, 1)
)
vdslPortPvlanEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "E5-121-MIB", "vdslPortPvlanEtype"),
)
if mibBuilder.loadTexts:
    vdslPortPvlanEntry.setStatus("current")
_VdslPortPvlanEtype_Type = Unsigned32
_VdslPortPvlanEtype_Object = MibTableColumn
vdslPortPvlanEtype = _VdslPortPvlanEtype_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 3, 2, 4, 1, 1),
    _VdslPortPvlanEtype_Type()
)
vdslPortPvlanEtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslPortPvlanEtype.setStatus("current")
_VdslPortPvlanVid_Type = VlanIndex
_VdslPortPvlanVid_Object = MibTableColumn
vdslPortPvlanVid = _VdslPortPvlanVid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 3, 2, 4, 1, 2),
    _VdslPortPvlanVid_Type()
)
vdslPortPvlanVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vdslPortPvlanVid.setStatus("current")


class _VdslPortPvlanPriority_Type(Integer32):
    """Custom type vdslPortPvlanPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_VdslPortPvlanPriority_Type.__name__ = "Integer32"
_VdslPortPvlanPriority_Object = MibTableColumn
vdslPortPvlanPriority = _VdslPortPvlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 3, 2, 4, 1, 3),
    _VdslPortPvlanPriority_Type()
)
vdslPortPvlanPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vdslPortPvlanPriority.setStatus("current")
_VdslPortPvlanRowStatus_Type = RowStatus
_VdslPortPvlanRowStatus_Object = MibTableColumn
vdslPortPvlanRowStatus = _VdslPortPvlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 3, 2, 4, 1, 4),
    _VdslPortPvlanRowStatus_Type()
)
vdslPortPvlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vdslPortPvlanRowStatus.setStatus("current")
_VdslRfiCustomTable_Object = MibTable
vdslRfiCustomTable = _VdslRfiCustomTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 3, 3)
)
if mibBuilder.loadTexts:
    vdslRfiCustomTable.setStatus("current")
_VdslRfiCustomEntry_Object = MibTableRow
vdslRfiCustomEntry = _VdslRfiCustomEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 3, 3, 1)
)
vdslRfiCustomEntry.setIndexNames(
    (0, "E5-121-MIB", "vdslRfiCustomIndex"),
)
if mibBuilder.loadTexts:
    vdslRfiCustomEntry.setStatus("current")
_VdslRfiCustomIndex_Type = Integer32
_VdslRfiCustomIndex_Object = MibTableColumn
vdslRfiCustomIndex = _VdslRfiCustomIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 3, 3, 1, 1),
    _VdslRfiCustomIndex_Type()
)
vdslRfiCustomIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslRfiCustomIndex.setStatus("current")
_VdslRfiCustomStartFreq_Type = Integer32
_VdslRfiCustomStartFreq_Object = MibTableColumn
vdslRfiCustomStartFreq = _VdslRfiCustomStartFreq_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 3, 3, 1, 2),
    _VdslRfiCustomStartFreq_Type()
)
vdslRfiCustomStartFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdslRfiCustomStartFreq.setStatus("current")
if mibBuilder.loadTexts:
    vdslRfiCustomStartFreq.setUnits("KHz")
_VdslRfiCustomEndFreq_Type = Integer32
_VdslRfiCustomEndFreq_Object = MibTableColumn
vdslRfiCustomEndFreq = _VdslRfiCustomEndFreq_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 3, 3, 1, 3),
    _VdslRfiCustomEndFreq_Type()
)
vdslRfiCustomEndFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdslRfiCustomEndFreq.setStatus("current")
if mibBuilder.loadTexts:
    vdslRfiCustomEndFreq.setUnits("KHz")


class _VdslRfiCustomEnable_Type(Integer32):
    """Custom type vdslRfiCustomEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_VdslRfiCustomEnable_Type.__name__ = "Integer32"
_VdslRfiCustomEnable_Object = MibTableColumn
vdslRfiCustomEnable = _VdslRfiCustomEnable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 3, 3, 1, 4),
    _VdslRfiCustomEnable_Type()
)
vdslRfiCustomEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdslRfiCustomEnable.setStatus("current")
_VdslLineConfUpboParamTable_Object = MibTable
vdslLineConfUpboParamTable = _VdslLineConfUpboParamTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 3, 4)
)
if mibBuilder.loadTexts:
    vdslLineConfUpboParamTable.setStatus("current")
_VdslLineConfUpboParamEntry_Object = MibTableRow
vdslLineConfUpboParamEntry = _VdslLineConfUpboParamEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 3, 4, 1)
)
vdslLineConfUpboParamEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "E5-121-MIB", "vdslLineConfUpboParamBand"),
)
if mibBuilder.loadTexts:
    vdslLineConfUpboParamEntry.setStatus("current")
_VdslLineConfUpboParamBand_Type = Integer32
_VdslLineConfUpboParamBand_Object = MibTableColumn
vdslLineConfUpboParamBand = _VdslLineConfUpboParamBand_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 3, 4, 1, 1),
    _VdslLineConfUpboParamBand_Type()
)
vdslLineConfUpboParamBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineConfUpboParamBand.setStatus("current")


class _VdslLineConfUpboParamA_Type(Integer32):
    """Custom type vdslLineConfUpboParamA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4000, 8095),
    )


_VdslLineConfUpboParamA_Type.__name__ = "Integer32"
_VdslLineConfUpboParamA_Object = MibTableColumn
vdslLineConfUpboParamA = _VdslLineConfUpboParamA_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 3, 4, 1, 2),
    _VdslLineConfUpboParamA_Type()
)
vdslLineConfUpboParamA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdslLineConfUpboParamA.setStatus("current")
if mibBuilder.loadTexts:
    vdslLineConfUpboParamA.setUnits("0.01 dBm/Hz")


class _VdslLineConfUpboParamB_Type(Integer32):
    """Custom type vdslLineConfUpboParamB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_VdslLineConfUpboParamB_Type.__name__ = "Integer32"
_VdslLineConfUpboParamB_Object = MibTableColumn
vdslLineConfUpboParamB = _VdslLineConfUpboParamB_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 3, 4, 1, 3),
    _VdslLineConfUpboParamB_Type()
)
vdslLineConfUpboParamB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdslLineConfUpboParamB.setStatus("current")
if mibBuilder.loadTexts:
    vdslLineConfUpboParamB.setUnits("0.01 dBm/Hz")
_VdslLineConfDpboTable_Object = MibTable
vdslLineConfDpboTable = _VdslLineConfDpboTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 3, 5)
)
if mibBuilder.loadTexts:
    vdslLineConfDpboTable.setStatus("current")
_VdslLineConfDpboEntry_Object = MibTableRow
vdslLineConfDpboEntry = _VdslLineConfDpboEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 3, 5, 1)
)
vdslLineConfDpboEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "E5-121-MIB", "vdslLineConfDpboIndex"),
)
if mibBuilder.loadTexts:
    vdslLineConfDpboEntry.setStatus("current")
_VdslLineConfDpboIndex_Type = Integer32
_VdslLineConfDpboIndex_Object = MibTableColumn
vdslLineConfDpboIndex = _VdslLineConfDpboIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 3, 5, 1, 1),
    _VdslLineConfDpboIndex_Type()
)
vdslLineConfDpboIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineConfDpboIndex.setStatus("current")


class _VdslLineConfDpboTone_Type(Integer32):
    """Custom type vdslLineConfDpboTone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_VdslLineConfDpboTone_Type.__name__ = "Integer32"
_VdslLineConfDpboTone_Object = MibTableColumn
vdslLineConfDpboTone = _VdslLineConfDpboTone_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 3, 5, 1, 2),
    _VdslLineConfDpboTone_Type()
)
vdslLineConfDpboTone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdslLineConfDpboTone.setStatus("current")


class _VdslLineConfDpboPsd_Type(Integer32):
    """Custom type vdslLineConfDpboPsd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VdslLineConfDpboPsd_Type.__name__ = "Integer32"
_VdslLineConfDpboPsd_Object = MibTableColumn
vdslLineConfDpboPsd = _VdslLineConfDpboPsd_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 3, 5, 1, 3),
    _VdslLineConfDpboPsd_Type()
)
vdslLineConfDpboPsd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdslLineConfDpboPsd.setStatus("current")
if mibBuilder.loadTexts:
    vdslLineConfDpboPsd.setUnits("-0.5dBm/Hz")
_Pvc_ObjectIdentity = ObjectIdentity
pvc = _Pvc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 4)
)
_MaxNumOfPvcs_Type = Integer32
_MaxNumOfPvcs_Object = MibScalar
maxNumOfPvcs = _MaxNumOfPvcs_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 4, 1),
    _MaxNumOfPvcs_Type()
)
maxNumOfPvcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumOfPvcs.setStatus("current")
_PvcTable_Object = MibTable
pvcTable = _PvcTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 4, 2)
)
if mibBuilder.loadTexts:
    pvcTable.setStatus("current")
_PvcEntry_Object = MibTableRow
pvcEntry = _PvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 4, 2, 1)
)
pvcEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "E5-121-MIB", "pvcVpi"),
    (0, "E5-121-MIB", "pvcVci"),
    (0, "E5-121-MIB", "pvcPvid"),
)
if mibBuilder.loadTexts:
    pvcEntry.setStatus("current")


class _PvcVpi_Type(Integer32):
    """Custom type pvcVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PvcVpi_Type.__name__ = "Integer32"
_PvcVpi_Object = MibTableColumn
pvcVpi = _PvcVpi_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 4, 2, 1, 1),
    _PvcVpi_Type()
)
pvcVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcVpi.setStatus("current")


class _PvcVci_Type(Integer32):
    """Custom type pvcVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PvcVci_Type.__name__ = "Integer32"
_PvcVci_Object = MibTableColumn
pvcVci = _PvcVci_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 4, 2, 1, 2),
    _PvcVci_Type()
)
pvcVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcVci.setStatus("current")
_PvcPvid_Type = VlanIndex
_PvcPvid_Object = MibTableColumn
pvcPvid = _PvcPvid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 4, 2, 1, 3),
    _PvcPvid_Type()
)
pvcPvid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcPvid.setStatus("current")


class _PvcPriority_Type(Integer32):
    """Custom type pvcPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PvcPriority_Type.__name__ = "Integer32"
_PvcPriority_Object = MibTableColumn
pvcPriority = _PvcPriority_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 4, 2, 1, 5),
    _PvcPriority_Type()
)
pvcPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvcPriority.setStatus("current")


class _PvcProfile_Type(DisplayString):
    """Custom type pvcProfile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_PvcProfile_Type.__name__ = "DisplayString"
_PvcProfile_Object = MibTableColumn
pvcProfile = _PvcProfile_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 4, 2, 1, 6),
    _PvcProfile_Type()
)
pvcProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvcProfile.setStatus("current")


class _PvcEncap_Type(Integer32):
    """Custom type pvcEncap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("llc", 1),
          ("vc", 2))
    )


_PvcEncap_Type.__name__ = "Integer32"
_PvcEncap_Object = MibTableColumn
pvcEncap = _PvcEncap_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 4, 2, 1, 7),
    _PvcEncap_Type()
)
pvcEncap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvcEncap.setStatus("current")
_PvcRowStatus_Type = RowStatus
_PvcRowStatus_Object = MibTableColumn
pvcRowStatus = _PvcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 4, 2, 1, 8),
    _PvcRowStatus_Type()
)
pvcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvcRowStatus.setStatus("current")
_PvcAcName_Type = DisplayString
_PvcAcName_Object = MibTableColumn
pvcAcName = _PvcAcName_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 4, 2, 1, 11),
    _PvcAcName_Type()
)
pvcAcName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvcAcName.setStatus("current")
_PvcServiceName_Type = DisplayString
_PvcServiceName_Object = MibTableColumn
pvcServiceName = _PvcServiceName_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 4, 2, 1, 12),
    _PvcServiceName_Type()
)
pvcServiceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvcServiceName.setStatus("current")
_PvcHelloTime_Type = Integer32
_PvcHelloTime_Object = MibTableColumn
pvcHelloTime = _PvcHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 4, 2, 1, 13),
    _PvcHelloTime_Type()
)
pvcHelloTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvcHelloTime.setStatus("current")
if mibBuilder.loadTexts:
    pvcHelloTime.setUnits("second")


class _PvcAuto_Type(Integer32):
    """Custom type pvcAuto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_PvcAuto_Type.__name__ = "Integer32"
_PvcAuto_Object = MibTableColumn
pvcAuto = _PvcAuto_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 4, 2, 1, 14),
    _PvcAuto_Type()
)
pvcAuto.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvcAuto.setStatus("current")
_PvcStateTable_Object = MibTable
pvcStateTable = _PvcStateTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 4, 3)
)
if mibBuilder.loadTexts:
    pvcStateTable.setStatus("current")
_PvcStateEntry_Object = MibTableRow
pvcStateEntry = _PvcStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 4, 3, 1)
)
pvcStateEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "E5-121-MIB", "pvcStateVpi"),
    (0, "E5-121-MIB", "pvcStateVci"),
    (0, "E5-121-MIB", "pvcStatePvid"),
)
if mibBuilder.loadTexts:
    pvcStateEntry.setStatus("current")


class _PvcStateVpi_Type(Integer32):
    """Custom type pvcStateVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PvcStateVpi_Type.__name__ = "Integer32"
_PvcStateVpi_Object = MibTableColumn
pvcStateVpi = _PvcStateVpi_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 4, 3, 1, 1),
    _PvcStateVpi_Type()
)
pvcStateVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcStateVpi.setStatus("current")


class _PvcStateVci_Type(Integer32):
    """Custom type pvcStateVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PvcStateVci_Type.__name__ = "Integer32"
_PvcStateVci_Object = MibTableColumn
pvcStateVci = _PvcStateVci_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 4, 3, 1, 2),
    _PvcStateVci_Type()
)
pvcStateVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcStateVci.setStatus("current")
_PvcStatePvid_Type = VlanIndex
_PvcStatePvid_Object = MibTableColumn
pvcStatePvid = _PvcStatePvid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 4, 3, 1, 3),
    _PvcStatePvid_Type()
)
pvcStatePvid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcStatePvid.setStatus("current")


class _PvcStatePriority_Type(Integer32):
    """Custom type pvcStatePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PvcStatePriority_Type.__name__ = "Integer32"
_PvcStatePriority_Object = MibTableColumn
pvcStatePriority = _PvcStatePriority_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 4, 3, 1, 4),
    _PvcStatePriority_Type()
)
pvcStatePriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcStatePriority.setStatus("current")


class _PvcStateChannelType_Type(DisplayString):
    """Custom type pvcStateChannelType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_PvcStateChannelType_Type.__name__ = "DisplayString"
_PvcStateChannelType_Object = MibTableColumn
pvcStateChannelType = _PvcStateChannelType_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 4, 3, 1, 8),
    _PvcStateChannelType_Type()
)
pvcStateChannelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcStateChannelType.setStatus("current")


class _PvcStateEncap_Type(DisplayString):
    """Custom type pvcStateEncap based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_PvcStateEncap_Type.__name__ = "DisplayString"
_PvcStateEncap_Object = MibTableColumn
pvcStateEncap = _PvcStateEncap_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 4, 3, 1, 9),
    _PvcStateEncap_Type()
)
pvcStateEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcStateEncap.setStatus("current")
_Rpvc_ObjectIdentity = ObjectIdentity
rpvc = _Rpvc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 8)
)
_RpvcGatewayTable_Object = MibTable
rpvcGatewayTable = _RpvcGatewayTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 8, 1)
)
if mibBuilder.loadTexts:
    rpvcGatewayTable.setStatus("current")
_RpvcGatewayEntry_Object = MibTableRow
rpvcGatewayEntry = _RpvcGatewayEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 8, 1, 1)
)
rpvcGatewayEntry.setIndexNames(
    (0, "E5-121-MIB", "rpvcGatewayIp"),
)
if mibBuilder.loadTexts:
    rpvcGatewayEntry.setStatus("current")
_RpvcGatewayIp_Type = IpAddress
_RpvcGatewayIp_Object = MibTableColumn
rpvcGatewayIp = _RpvcGatewayIp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 8, 1, 1, 1),
    _RpvcGatewayIp_Type()
)
rpvcGatewayIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpvcGatewayIp.setStatus("current")
_RpvcGatewayVlanId_Type = VlanIndex
_RpvcGatewayVlanId_Object = MibTableColumn
rpvcGatewayVlanId = _RpvcGatewayVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 8, 1, 1, 2),
    _RpvcGatewayVlanId_Type()
)
rpvcGatewayVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rpvcGatewayVlanId.setStatus("current")
_RpvcGatewayRowStatus_Type = RowStatus
_RpvcGatewayRowStatus_Object = MibTableColumn
rpvcGatewayRowStatus = _RpvcGatewayRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 8, 1, 1, 3),
    _RpvcGatewayRowStatus_Type()
)
rpvcGatewayRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rpvcGatewayRowStatus.setStatus("current")
_RpvcGatewayPriority_Type = Integer32
_RpvcGatewayPriority_Object = MibTableColumn
rpvcGatewayPriority = _RpvcGatewayPriority_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 8, 1, 1, 4),
    _RpvcGatewayPriority_Type()
)
rpvcGatewayPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rpvcGatewayPriority.setStatus("current")
_RpvcTable_Object = MibTable
rpvcTable = _RpvcTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 8, 2)
)
if mibBuilder.loadTexts:
    rpvcTable.setStatus("current")
_RpvcEntry_Object = MibTableRow
rpvcEntry = _RpvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 8, 2, 1)
)
rpvcEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "E5-121-MIB", "rpvcVpi"),
    (0, "E5-121-MIB", "rpvcVci"),
    (0, "E5-121-MIB", "rpvcIp"),
    (0, "E5-121-MIB", "rpvcNetmask"),
)
if mibBuilder.loadTexts:
    rpvcEntry.setStatus("current")


class _RpvcVpi_Type(Integer32):
    """Custom type rpvcVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RpvcVpi_Type.__name__ = "Integer32"
_RpvcVpi_Object = MibTableColumn
rpvcVpi = _RpvcVpi_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 8, 2, 1, 1),
    _RpvcVpi_Type()
)
rpvcVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpvcVpi.setStatus("current")


class _RpvcVci_Type(Integer32):
    """Custom type rpvcVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RpvcVci_Type.__name__ = "Integer32"
_RpvcVci_Object = MibTableColumn
rpvcVci = _RpvcVci_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 8, 2, 1, 2),
    _RpvcVci_Type()
)
rpvcVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpvcVci.setStatus("current")


class _RpvcEncap_Type(Integer32):
    """Custom type rpvcEncap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("llc", 1),
          ("vc", 2))
    )


_RpvcEncap_Type.__name__ = "Integer32"
_RpvcEncap_Object = MibTableColumn
rpvcEncap = _RpvcEncap_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 8, 2, 1, 3),
    _RpvcEncap_Type()
)
rpvcEncap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rpvcEncap.setStatus("current")


class _RpvcProfile_Type(DisplayString):
    """Custom type rpvcProfile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_RpvcProfile_Type.__name__ = "DisplayString"
_RpvcProfile_Object = MibTableColumn
rpvcProfile = _RpvcProfile_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 8, 2, 1, 4),
    _RpvcProfile_Type()
)
rpvcProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rpvcProfile.setStatus("current")
_RpvcIp_Type = IpAddress
_RpvcIp_Object = MibTableColumn
rpvcIp = _RpvcIp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 8, 2, 1, 5),
    _RpvcIp_Type()
)
rpvcIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpvcIp.setStatus("current")
_RpvcNetmask_Type = IpAddress
_RpvcNetmask_Object = MibTableColumn
rpvcNetmask = _RpvcNetmask_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 8, 2, 1, 6),
    _RpvcNetmask_Type()
)
rpvcNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpvcNetmask.setStatus("current")
_RpvcGatewayIpAddress_Type = IpAddress
_RpvcGatewayIpAddress_Object = MibTableColumn
rpvcGatewayIpAddress = _RpvcGatewayIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 8, 2, 1, 7),
    _RpvcGatewayIpAddress_Type()
)
rpvcGatewayIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rpvcGatewayIpAddress.setStatus("current")
_RpvcRowStatus_Type = RowStatus
_RpvcRowStatus_Object = MibTableColumn
rpvcRowStatus = _RpvcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 8, 2, 1, 8),
    _RpvcRowStatus_Type()
)
rpvcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rpvcRowStatus.setStatus("current")
_RpvcRouteDomainTable_Object = MibTable
rpvcRouteDomainTable = _RpvcRouteDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 8, 3)
)
if mibBuilder.loadTexts:
    rpvcRouteDomainTable.setStatus("current")
_RpvcRouteDomainEntry_Object = MibTableRow
rpvcRouteDomainEntry = _RpvcRouteDomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 8, 3, 1)
)
rpvcRouteDomainEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "E5-121-MIB", "rpvcRouteDomainVpi"),
    (0, "E5-121-MIB", "rpvcRouteDomainVci"),
    (0, "E5-121-MIB", "rpvcRouteDomainIp"),
    (0, "E5-121-MIB", "rpvcRouteDomainNetmask"),
)
if mibBuilder.loadTexts:
    rpvcRouteDomainEntry.setStatus("current")


class _RpvcRouteDomainVpi_Type(Integer32):
    """Custom type rpvcRouteDomainVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RpvcRouteDomainVpi_Type.__name__ = "Integer32"
_RpvcRouteDomainVpi_Object = MibTableColumn
rpvcRouteDomainVpi = _RpvcRouteDomainVpi_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 8, 3, 1, 1),
    _RpvcRouteDomainVpi_Type()
)
rpvcRouteDomainVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpvcRouteDomainVpi.setStatus("current")


class _RpvcRouteDomainVci_Type(Integer32):
    """Custom type rpvcRouteDomainVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RpvcRouteDomainVci_Type.__name__ = "Integer32"
_RpvcRouteDomainVci_Object = MibTableColumn
rpvcRouteDomainVci = _RpvcRouteDomainVci_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 8, 3, 1, 2),
    _RpvcRouteDomainVci_Type()
)
rpvcRouteDomainVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpvcRouteDomainVci.setStatus("current")
_RpvcRouteDomainIp_Type = IpAddress
_RpvcRouteDomainIp_Object = MibTableColumn
rpvcRouteDomainIp = _RpvcRouteDomainIp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 8, 3, 1, 3),
    _RpvcRouteDomainIp_Type()
)
rpvcRouteDomainIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpvcRouteDomainIp.setStatus("current")
_RpvcRouteDomainNetmask_Type = IpAddress
_RpvcRouteDomainNetmask_Object = MibTableColumn
rpvcRouteDomainNetmask = _RpvcRouteDomainNetmask_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 8, 3, 1, 4),
    _RpvcRouteDomainNetmask_Type()
)
rpvcRouteDomainNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpvcRouteDomainNetmask.setStatus("current")
_RpvcRouteDomainRowStatus_Type = RowStatus
_RpvcRouteDomainRowStatus_Object = MibTableColumn
rpvcRouteDomainRowStatus = _RpvcRouteDomainRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 8, 3, 1, 5),
    _RpvcRouteDomainRowStatus_Type()
)
rpvcRouteDomainRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rpvcRouteDomainRowStatus.setStatus("current")
_RpvcArpAgingTime_Type = Integer32
_RpvcArpAgingTime_Object = MibScalar
rpvcArpAgingTime = _RpvcArpAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 8, 4),
    _RpvcArpAgingTime_Type()
)
rpvcArpAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rpvcArpAgingTime.setStatus("current")


class _RpvcArpFlush_Type(Integer32):
    """Custom type rpvcArpFlush based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("enable", 1)
    )


_RpvcArpFlush_Type.__name__ = "Integer32"
_RpvcArpFlush_Object = MibScalar
rpvcArpFlush = _RpvcArpFlush_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 8, 5),
    _RpvcArpFlush_Type()
)
rpvcArpFlush.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rpvcArpFlush.setStatus("current")
_DsBcastDisableTable_Object = MibTable
dsBcastDisableTable = _DsBcastDisableTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 9)
)
if mibBuilder.loadTexts:
    dsBcastDisableTable.setStatus("current")
_DsBcastDisableEntry_Object = MibTableRow
dsBcastDisableEntry = _DsBcastDisableEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 9, 1)
)
dsBcastDisableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "E5-121-MIB", "dsBcastDisableVlanId"),
)
if mibBuilder.loadTexts:
    dsBcastDisableEntry.setStatus("current")
_DsBcastDisableVlanId_Type = Integer32
_DsBcastDisableVlanId_Object = MibTableColumn
dsBcastDisableVlanId = _DsBcastDisableVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 9, 1, 1),
    _DsBcastDisableVlanId_Type()
)
dsBcastDisableVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsBcastDisableVlanId.setStatus("current")
_DsBcastDisableRowStatus_Type = RowStatus
_DsBcastDisableRowStatus_Object = MibTableColumn
dsBcastDisableRowStatus = _DsBcastDisableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 9, 1, 2),
    _DsBcastDisableRowStatus_Type()
)
dsBcastDisableRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsBcastDisableRowStatus.setStatus("current")
_Paepvc_ObjectIdentity = ObjectIdentity
paepvc = _Paepvc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 10)
)
_PaepvcTable_Object = MibTable
paepvcTable = _PaepvcTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 10, 1)
)
if mibBuilder.loadTexts:
    paepvcTable.setStatus("current")
_PaepvcEntry_Object = MibTableRow
paepvcEntry = _PaepvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 10, 1, 1)
)
paepvcEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "E5-121-MIB", "paepvcVpi"),
    (0, "E5-121-MIB", "paepvcVci"),
    (0, "E5-121-MIB", "paepvcPvid"),
)
if mibBuilder.loadTexts:
    paepvcEntry.setStatus("current")


class _PaepvcVpi_Type(Integer32):
    """Custom type paepvcVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PaepvcVpi_Type.__name__ = "Integer32"
_PaepvcVpi_Object = MibTableColumn
paepvcVpi = _PaepvcVpi_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 10, 1, 1, 1),
    _PaepvcVpi_Type()
)
paepvcVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcVpi.setStatus("current")


class _PaepvcVci_Type(Integer32):
    """Custom type paepvcVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PaepvcVci_Type.__name__ = "Integer32"
_PaepvcVci_Object = MibTableColumn
paepvcVci = _PaepvcVci_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 10, 1, 1, 2),
    _PaepvcVci_Type()
)
paepvcVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcVci.setStatus("current")
_PaepvcPvid_Type = VlanIndex
_PaepvcPvid_Object = MibTableColumn
paepvcPvid = _PaepvcPvid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 10, 1, 1, 3),
    _PaepvcPvid_Type()
)
paepvcPvid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcPvid.setStatus("current")


class _PaepvcEncap_Type(Integer32):
    """Custom type paepvcEncap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("llc", 1),
          ("vc", 2))
    )


_PaepvcEncap_Type.__name__ = "Integer32"
_PaepvcEncap_Object = MibTableColumn
paepvcEncap = _PaepvcEncap_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 10, 1, 1, 4),
    _PaepvcEncap_Type()
)
paepvcEncap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    paepvcEncap.setStatus("current")


class _PaepvcPriority_Type(Integer32):
    """Custom type paepvcPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PaepvcPriority_Type.__name__ = "Integer32"
_PaepvcPriority_Object = MibTableColumn
paepvcPriority = _PaepvcPriority_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 10, 1, 1, 5),
    _PaepvcPriority_Type()
)
paepvcPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    paepvcPriority.setStatus("current")


class _PaepvcProfile_Type(DisplayString):
    """Custom type paepvcProfile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_PaepvcProfile_Type.__name__ = "DisplayString"
_PaepvcProfile_Object = MibTableColumn
paepvcProfile = _PaepvcProfile_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 10, 1, 1, 6),
    _PaepvcProfile_Type()
)
paepvcProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    paepvcProfile.setStatus("current")
_PaepvcAcName_Type = DisplayString
_PaepvcAcName_Object = MibTableColumn
paepvcAcName = _PaepvcAcName_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 10, 1, 1, 7),
    _PaepvcAcName_Type()
)
paepvcAcName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    paepvcAcName.setStatus("current")
_PaepvcServiceName_Type = DisplayString
_PaepvcServiceName_Object = MibTableColumn
paepvcServiceName = _PaepvcServiceName_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 10, 1, 1, 8),
    _PaepvcServiceName_Type()
)
paepvcServiceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    paepvcServiceName.setStatus("current")
_PaepvcHelloTime_Type = Integer32
_PaepvcHelloTime_Object = MibTableColumn
paepvcHelloTime = _PaepvcHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 10, 1, 1, 9),
    _PaepvcHelloTime_Type()
)
paepvcHelloTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    paepvcHelloTime.setStatus("current")
if mibBuilder.loadTexts:
    paepvcHelloTime.setUnits("second")
_PaepvcRowStatus_Type = RowStatus
_PaepvcRowStatus_Object = MibTableColumn
paepvcRowStatus = _PaepvcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 10, 1, 1, 10),
    _PaepvcRowStatus_Type()
)
paepvcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    paepvcRowStatus.setStatus("current")
_PaepvcCvid_Type = VlanIndex
_PaepvcCvid_Object = MibTableColumn
paepvcCvid = _PaepvcCvid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 10, 1, 1, 12),
    _PaepvcCvid_Type()
)
paepvcCvid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    paepvcCvid.setStatus("current")


class _PaepvcCPriority_Type(Integer32):
    """Custom type paepvcCPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PaepvcCPriority_Type.__name__ = "Integer32"
_PaepvcCPriority_Object = MibTableColumn
paepvcCPriority = _PaepvcCPriority_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 10, 1, 1, 13),
    _PaepvcCPriority_Type()
)
paepvcCPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    paepvcCPriority.setStatus("current")
_Tlspvc_ObjectIdentity = ObjectIdentity
tlspvc = _Tlspvc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 11)
)
_TlspvcTable_Object = MibTable
tlspvcTable = _TlspvcTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 11, 1)
)
if mibBuilder.loadTexts:
    tlspvcTable.setStatus("current")
_TlspvcEntry_Object = MibTableRow
tlspvcEntry = _TlspvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 11, 1, 1)
)
tlspvcEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "E5-121-MIB", "tlspvcVpi"),
    (0, "E5-121-MIB", "tlspvcVci"),
    (0, "E5-121-MIB", "tlspvcSvid"),
)
if mibBuilder.loadTexts:
    tlspvcEntry.setStatus("current")


class _TlspvcVpi_Type(Integer32):
    """Custom type tlspvcVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TlspvcVpi_Type.__name__ = "Integer32"
_TlspvcVpi_Object = MibTableColumn
tlspvcVpi = _TlspvcVpi_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 11, 1, 1, 1),
    _TlspvcVpi_Type()
)
tlspvcVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlspvcVpi.setStatus("current")


class _TlspvcVci_Type(Integer32):
    """Custom type tlspvcVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TlspvcVci_Type.__name__ = "Integer32"
_TlspvcVci_Object = MibTableColumn
tlspvcVci = _TlspvcVci_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 11, 1, 1, 2),
    _TlspvcVci_Type()
)
tlspvcVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlspvcVci.setStatus("current")
_TlspvcSvid_Type = VlanIndex
_TlspvcSvid_Object = MibTableColumn
tlspvcSvid = _TlspvcSvid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 11, 1, 1, 3),
    _TlspvcSvid_Type()
)
tlspvcSvid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlspvcSvid.setStatus("current")


class _TlspvcEncap_Type(Integer32):
    """Custom type tlspvcEncap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("llc", 1),
          ("vc", 2))
    )


_TlspvcEncap_Type.__name__ = "Integer32"
_TlspvcEncap_Object = MibTableColumn
tlspvcEncap = _TlspvcEncap_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 11, 1, 1, 4),
    _TlspvcEncap_Type()
)
tlspvcEncap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tlspvcEncap.setStatus("current")


class _TlspvcSpriority_Type(Integer32):
    """Custom type tlspvcSpriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TlspvcSpriority_Type.__name__ = "Integer32"
_TlspvcSpriority_Object = MibTableColumn
tlspvcSpriority = _TlspvcSpriority_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 11, 1, 1, 5),
    _TlspvcSpriority_Type()
)
tlspvcSpriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tlspvcSpriority.setStatus("current")


class _TlspvcProfile_Type(DisplayString):
    """Custom type tlspvcProfile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_TlspvcProfile_Type.__name__ = "DisplayString"
_TlspvcProfile_Object = MibTableColumn
tlspvcProfile = _TlspvcProfile_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 11, 1, 1, 6),
    _TlspvcProfile_Type()
)
tlspvcProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tlspvcProfile.setStatus("current")
_TlspvcRowStatus_Type = RowStatus
_TlspvcRowStatus_Object = MibTableColumn
tlspvcRowStatus = _TlspvcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 11, 1, 1, 7),
    _TlspvcRowStatus_Type()
)
tlspvcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tlspvcRowStatus.setStatus("current")
_Dtpvc_ObjectIdentity = ObjectIdentity
dtpvc = _Dtpvc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 13)
)
_DtpvcTable_Object = MibTable
dtpvcTable = _DtpvcTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 13, 1)
)
if mibBuilder.loadTexts:
    dtpvcTable.setStatus("current")
_DtpvcEntry_Object = MibTableRow
dtpvcEntry = _DtpvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 13, 1, 1)
)
dtpvcEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "E5-121-MIB", "dtpvcVpi"),
    (0, "E5-121-MIB", "dtpvcVci"),
    (0, "E5-121-MIB", "dtpvcSvid"),
)
if mibBuilder.loadTexts:
    dtpvcEntry.setStatus("current")


class _DtpvcVpi_Type(Integer32):
    """Custom type dtpvcVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DtpvcVpi_Type.__name__ = "Integer32"
_DtpvcVpi_Object = MibTableColumn
dtpvcVpi = _DtpvcVpi_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 13, 1, 1, 1),
    _DtpvcVpi_Type()
)
dtpvcVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtpvcVpi.setStatus("current")


class _DtpvcVci_Type(Integer32):
    """Custom type dtpvcVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DtpvcVci_Type.__name__ = "Integer32"
_DtpvcVci_Object = MibTableColumn
dtpvcVci = _DtpvcVci_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 13, 1, 1, 2),
    _DtpvcVci_Type()
)
dtpvcVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtpvcVci.setStatus("current")
_DtpvcSvid_Type = VlanIndex
_DtpvcSvid_Object = MibTableColumn
dtpvcSvid = _DtpvcSvid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 13, 1, 1, 3),
    _DtpvcSvid_Type()
)
dtpvcSvid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtpvcSvid.setStatus("current")


class _DtpvcSpriority_Type(Integer32):
    """Custom type dtpvcSpriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_DtpvcSpriority_Type.__name__ = "Integer32"
_DtpvcSpriority_Object = MibTableColumn
dtpvcSpriority = _DtpvcSpriority_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 13, 1, 1, 4),
    _DtpvcSpriority_Type()
)
dtpvcSpriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dtpvcSpriority.setStatus("current")
_DtpvcCvid_Type = VlanIndex
_DtpvcCvid_Object = MibTableColumn
dtpvcCvid = _DtpvcCvid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 13, 1, 1, 5),
    _DtpvcCvid_Type()
)
dtpvcCvid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dtpvcCvid.setStatus("current")


class _DtpvcCpriority_Type(Integer32):
    """Custom type dtpvcCpriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_DtpvcCpriority_Type.__name__ = "Integer32"
_DtpvcCpriority_Object = MibTableColumn
dtpvcCpriority = _DtpvcCpriority_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 13, 1, 1, 6),
    _DtpvcCpriority_Type()
)
dtpvcCpriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dtpvcCpriority.setStatus("current")


class _DtpvcEncap_Type(Integer32):
    """Custom type dtpvcEncap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("llc", 1),
          ("vc", 2))
    )


_DtpvcEncap_Type.__name__ = "Integer32"
_DtpvcEncap_Object = MibTableColumn
dtpvcEncap = _DtpvcEncap_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 13, 1, 1, 7),
    _DtpvcEncap_Type()
)
dtpvcEncap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dtpvcEncap.setStatus("current")


class _DtpvcProfile_Type(DisplayString):
    """Custom type dtpvcProfile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_DtpvcProfile_Type.__name__ = "DisplayString"
_DtpvcProfile_Object = MibTableColumn
dtpvcProfile = _DtpvcProfile_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 13, 1, 1, 8),
    _DtpvcProfile_Type()
)
dtpvcProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dtpvcProfile.setStatus("current")
_DtpvcRowStatus_Type = RowStatus
_DtpvcRowStatus_Object = MibTableColumn
dtpvcRowStatus = _DtpvcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 13, 1, 1, 9),
    _DtpvcRowStatus_Type()
)
dtpvcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dtpvcRowStatus.setStatus("current")


class _DtpvcSuperChannel_Type(Integer32):
    """Custom type dtpvcSuperChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_DtpvcSuperChannel_Type.__name__ = "Integer32"
_DtpvcSuperChannel_Object = MibTableColumn
dtpvcSuperChannel = _DtpvcSuperChannel_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 13, 1, 1, 10),
    _DtpvcSuperChannel_Type()
)
dtpvcSuperChannel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dtpvcSuperChannel.setStatus("current")
_DtpvcAcName_Type = DisplayString
_DtpvcAcName_Object = MibTableColumn
dtpvcAcName = _DtpvcAcName_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 13, 1, 1, 11),
    _DtpvcAcName_Type()
)
dtpvcAcName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dtpvcAcName.setStatus("current")
_DtpvcServiceName_Type = DisplayString
_DtpvcServiceName_Object = MibTableColumn
dtpvcServiceName = _DtpvcServiceName_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 13, 1, 1, 12),
    _DtpvcServiceName_Type()
)
dtpvcServiceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dtpvcServiceName.setStatus("current")
_DtpvcHelloTime_Type = Integer32
_DtpvcHelloTime_Object = MibTableColumn
dtpvcHelloTime = _DtpvcHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 13, 1, 1, 13),
    _DtpvcHelloTime_Type()
)
dtpvcHelloTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dtpvcHelloTime.setStatus("current")
if mibBuilder.loadTexts:
    dtpvcHelloTime.setUnits("second")


class _DtpvcAuto_Type(Integer32):
    """Custom type dtpvcAuto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_DtpvcAuto_Type.__name__ = "Integer32"
_DtpvcAuto_Object = MibTableColumn
dtpvcAuto = _DtpvcAuto_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 13, 1, 1, 14),
    _DtpvcAuto_Type()
)
dtpvcAuto.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dtpvcAuto.setStatus("current")
_DtpvcStateTable_Object = MibTable
dtpvcStateTable = _DtpvcStateTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 13, 2)
)
if mibBuilder.loadTexts:
    dtpvcStateTable.setStatus("current")
_DtpvcStateEntry_Object = MibTableRow
dtpvcStateEntry = _DtpvcStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 13, 2, 1)
)
dtpvcStateEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "E5-121-MIB", "dtpvcStateVpi"),
    (0, "E5-121-MIB", "dtpvcStateVci"),
    (0, "E5-121-MIB", "dtpvcStateSvid"),
)
if mibBuilder.loadTexts:
    dtpvcStateEntry.setStatus("current")


class _DtpvcStateVpi_Type(Integer32):
    """Custom type dtpvcStateVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DtpvcStateVpi_Type.__name__ = "Integer32"
_DtpvcStateVpi_Object = MibTableColumn
dtpvcStateVpi = _DtpvcStateVpi_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 13, 2, 1, 1),
    _DtpvcStateVpi_Type()
)
dtpvcStateVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtpvcStateVpi.setStatus("current")


class _DtpvcStateVci_Type(Integer32):
    """Custom type dtpvcStateVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DtpvcStateVci_Type.__name__ = "Integer32"
_DtpvcStateVci_Object = MibTableColumn
dtpvcStateVci = _DtpvcStateVci_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 13, 2, 1, 2),
    _DtpvcStateVci_Type()
)
dtpvcStateVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtpvcStateVci.setStatus("current")
_DtpvcStateSvid_Type = VlanIndex
_DtpvcStateSvid_Object = MibTableColumn
dtpvcStateSvid = _DtpvcStateSvid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 13, 2, 1, 3),
    _DtpvcStateSvid_Type()
)
dtpvcStateSvid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtpvcStateSvid.setStatus("current")


class _DtpvcStateSPriority_Type(Integer32):
    """Custom type dtpvcStateSPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_DtpvcStateSPriority_Type.__name__ = "Integer32"
_DtpvcStateSPriority_Object = MibTableColumn
dtpvcStateSPriority = _DtpvcStateSPriority_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 13, 2, 1, 4),
    _DtpvcStateSPriority_Type()
)
dtpvcStateSPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtpvcStateSPriority.setStatus("current")
_DtpvcStateCvid_Type = VlanIndex
_DtpvcStateCvid_Object = MibTableColumn
dtpvcStateCvid = _DtpvcStateCvid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 13, 2, 1, 5),
    _DtpvcStateCvid_Type()
)
dtpvcStateCvid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtpvcStateCvid.setStatus("current")


class _DtpvcStateCPriority_Type(Integer32):
    """Custom type dtpvcStateCPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_DtpvcStateCPriority_Type.__name__ = "Integer32"
_DtpvcStateCPriority_Object = MibTableColumn
dtpvcStateCPriority = _DtpvcStateCPriority_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 13, 2, 1, 6),
    _DtpvcStateCPriority_Type()
)
dtpvcStateCPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtpvcStateCPriority.setStatus("current")


class _DtpvcStateChannelType_Type(DisplayString):
    """Custom type dtpvcStateChannelType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_DtpvcStateChannelType_Type.__name__ = "DisplayString"
_DtpvcStateChannelType_Object = MibTableColumn
dtpvcStateChannelType = _DtpvcStateChannelType_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 13, 2, 1, 8),
    _DtpvcStateChannelType_Type()
)
dtpvcStateChannelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtpvcStateChannelType.setStatus("current")


class _DtpvcStateEncap_Type(DisplayString):
    """Custom type dtpvcStateEncap based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_DtpvcStateEncap_Type.__name__ = "DisplayString"
_DtpvcStateEncap_Object = MibTableColumn
dtpvcStateEncap = _DtpvcStateEncap_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 13, 2, 1, 9),
    _DtpvcStateEncap_Type()
)
dtpvcStateEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtpvcStateEncap.setStatus("current")
_VoipPort_ObjectIdentity = ObjectIdentity
voipPort = _VoipPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 14)
)
_VoipSipLineConfTable_Object = MibTable
voipSipLineConfTable = _VoipSipLineConfTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 14, 1)
)
if mibBuilder.loadTexts:
    voipSipLineConfTable.setStatus("current")
_VoipSipLineConfEntry_Object = MibTableRow
voipSipLineConfEntry = _VoipSipLineConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 14, 1, 1)
)
voipSipLineConfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    voipSipLineConfEntry.setStatus("current")
_VoipSipLineConfSipProfile_Type = OctetString
_VoipSipLineConfSipProfile_Object = MibTableColumn
voipSipLineConfSipProfile = _VoipSipLineConfSipProfile_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 14, 1, 1, 1),
    _VoipSipLineConfSipProfile_Type()
)
voipSipLineConfSipProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipSipLineConfSipProfile.setStatus("current")
_VoipSipLineConfSipCallSvcProfile_Type = OctetString
_VoipSipLineConfSipCallSvcProfile_Object = MibTableColumn
voipSipLineConfSipCallSvcProfile = _VoipSipLineConfSipCallSvcProfile_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 14, 1, 1, 2),
    _VoipSipLineConfSipCallSvcProfile_Type()
)
voipSipLineConfSipCallSvcProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipSipLineConfSipCallSvcProfile.setStatus("current")
_VoipSipLineConfDspProfile_Type = OctetString
_VoipSipLineConfDspProfile_Object = MibTableColumn
voipSipLineConfDspProfile = _VoipSipLineConfDspProfile_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 14, 1, 1, 3),
    _VoipSipLineConfDspProfile_Type()
)
voipSipLineConfDspProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipSipLineConfDspProfile.setStatus("current")
_PortOperations_ObjectIdentity = ObjectIdentity
portOperations = _PortOperations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 14, 2)
)
_VoipPortTarget_Type = OctetString
_VoipPortTarget_Object = MibScalar
voipPortTarget = _VoipPortTarget_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 14, 2, 1),
    _VoipPortTarget_Type()
)
voipPortTarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipPortTarget.setStatus("current")
_VoipPortOps_Type = Integer32
_VoipPortOps_Object = MibScalar
voipPortOps = _VoipPortOps_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 14, 2, 2),
    _VoipPortOps_Type()
)
voipPortOps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipPortOps.setStatus("current")
_VoipPortTelTable_Object = MibTable
voipPortTelTable = _VoipPortTelTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 14, 3)
)
if mibBuilder.loadTexts:
    voipPortTelTable.setStatus("current")
_VoipPortTelEntry_Object = MibTableRow
voipPortTelEntry = _VoipPortTelEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 14, 3, 1)
)
voipPortTelEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    voipPortTelEntry.setStatus("current")


class _VoipPortTel_Type(DisplayString):
    """Custom type voipPortTel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_VoipPortTel_Type.__name__ = "DisplayString"
_VoipPortTel_Object = MibTableColumn
voipPortTel = _VoipPortTel_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 14, 3, 1, 1),
    _VoipPortTel_Type()
)
voipPortTel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipPortTel.setStatus("current")
_VoipH248LineConfTable_Object = MibTable
voipH248LineConfTable = _VoipH248LineConfTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 14, 4)
)
if mibBuilder.loadTexts:
    voipH248LineConfTable.setStatus("current")
_VoipH248LineConfEntry_Object = MibTableRow
voipH248LineConfEntry = _VoipH248LineConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 14, 4, 1)
)
voipH248LineConfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    voipH248LineConfEntry.setStatus("current")
_VoipH248LineConfMgName_Type = OctetString
_VoipH248LineConfMgName_Object = MibTableColumn
voipH248LineConfMgName = _VoipH248LineConfMgName_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 14, 4, 1, 1),
    _VoipH248LineConfMgName_Type()
)
voipH248LineConfMgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipH248LineConfMgName.setStatus("current")
_VoipH248LineConfDspProfile_Type = OctetString
_VoipH248LineConfDspProfile_Object = MibTableColumn
voipH248LineConfDspProfile = _VoipH248LineConfDspProfile_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 14, 4, 1, 2),
    _VoipH248LineConfDspProfile_Type()
)
voipH248LineConfDspProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipH248LineConfDspProfile.setStatus("current")
_VoipH248LineConfVBDProfile_Type = OctetString
_VoipH248LineConfVBDProfile_Object = MibTableColumn
voipH248LineConfVBDProfile = _VoipH248LineConfVBDProfile_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 14, 4, 1, 3),
    _VoipH248LineConfVBDProfile_Type()
)
voipH248LineConfVBDProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipH248LineConfVBDProfile.setStatus("current")
_VoipPortH248TerminationTable_Object = MibTable
voipPortH248TerminationTable = _VoipPortH248TerminationTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 14, 5)
)
if mibBuilder.loadTexts:
    voipPortH248TerminationTable.setStatus("current")
_VoipPortH248TerminationEntry_Object = MibTableRow
voipPortH248TerminationEntry = _VoipPortH248TerminationEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 14, 5, 1)
)
voipPortH248TerminationEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    voipPortH248TerminationEntry.setStatus("current")
_VoipPortH248TermName_Type = OctetString
_VoipPortH248TermName_Object = MibTableColumn
voipPortH248TermName = _VoipPortH248TermName_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 14, 5, 1, 1),
    _VoipPortH248TermName_Type()
)
voipPortH248TermName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipPortH248TermName.setStatus("current")
_VoipPortGainTable_Object = MibTable
voipPortGainTable = _VoipPortGainTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 14, 6)
)
if mibBuilder.loadTexts:
    voipPortGainTable.setStatus("current")
_VoipPortGainEntry_Object = MibTableRow
voipPortGainEntry = _VoipPortGainEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 14, 6, 1)
)
voipPortGainEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    voipPortGainEntry.setStatus("current")
_VoipPortTXGain_Type = Integer32
_VoipPortTXGain_Object = MibTableColumn
voipPortTXGain = _VoipPortTXGain_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 14, 6, 1, 1),
    _VoipPortTXGain_Type()
)
voipPortTXGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipPortTXGain.setStatus("current")
_VoipPortRXGain_Type = Integer32
_VoipPortRXGain_Object = MibTableColumn
voipPortRXGain = _VoipPortRXGain_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 14, 6, 1, 2),
    _VoipPortRXGain_Type()
)
voipPortRXGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipPortRXGain.setStatus("current")
_VoipPortSeizureModeTable_Object = MibTable
voipPortSeizureModeTable = _VoipPortSeizureModeTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 14, 7)
)
if mibBuilder.loadTexts:
    voipPortSeizureModeTable.setStatus("current")
_VoipPortSeizureModeEntry_Object = MibTableRow
voipPortSeizureModeEntry = _VoipPortSeizureModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 14, 7, 1)
)
voipPortSeizureModeEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    voipPortSeizureModeEntry.setStatus("current")


class _VoipPortSeizureMode_Type(Integer32):
    """Custom type voipPortSeizureMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("loopstart", 1),
          ("groundstart", 2))
    )


_VoipPortSeizureMode_Type.__name__ = "Integer32"
_VoipPortSeizureMode_Object = MibTableColumn
voipPortSeizureMode = _VoipPortSeizureMode_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 14, 7, 1, 1),
    _VoipPortSeizureMode_Type()
)
voipPortSeizureMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipPortSeizureMode.setStatus("current")
_VoipPortSipAuthTable_Object = MibTable
voipPortSipAuthTable = _VoipPortSipAuthTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 14, 8)
)
if mibBuilder.loadTexts:
    voipPortSipAuthTable.setStatus("current")
_VoipPortSipAuthEntry_Object = MibTableRow
voipPortSipAuthEntry = _VoipPortSipAuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 14, 8, 1)
)
voipPortSipAuthEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    voipPortSipAuthEntry.setStatus("current")


class _VoipPortSipAuthMode_Type(Integer32):
    """Custom type voipPortSipAuthMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("profile", 1),
          ("line", 2))
    )


_VoipPortSipAuthMode_Type.__name__ = "Integer32"
_VoipPortSipAuthMode_Object = MibTableColumn
voipPortSipAuthMode = _VoipPortSipAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 14, 8, 1, 1),
    _VoipPortSipAuthMode_Type()
)
voipPortSipAuthMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipPortSipAuthMode.setStatus("current")
_VoipPortSipAuthUsername_Type = OctetString
_VoipPortSipAuthUsername_Object = MibTableColumn
voipPortSipAuthUsername = _VoipPortSipAuthUsername_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 14, 8, 1, 2),
    _VoipPortSipAuthUsername_Type()
)
voipPortSipAuthUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipPortSipAuthUsername.setStatus("current")


class _VoipPortSipAuthPasswdOn_Type(Integer32):
    """Custom type voipPortSipAuthPasswdOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_VoipPortSipAuthPasswdOn_Type.__name__ = "Integer32"
_VoipPortSipAuthPasswdOn_Object = MibTableColumn
voipPortSipAuthPasswdOn = _VoipPortSipAuthPasswdOn_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 14, 8, 1, 3),
    _VoipPortSipAuthPasswdOn_Type()
)
voipPortSipAuthPasswdOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipPortSipAuthPasswdOn.setStatus("current")
_VoipPortSipAuthPasswd_Type = OctetString
_VoipPortSipAuthPasswd_Object = MibTableColumn
voipPortSipAuthPasswd = _VoipPortSipAuthPasswd_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 14, 8, 1, 4),
    _VoipPortSipAuthPasswd_Type()
)
voipPortSipAuthPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipPortSipAuthPasswd.setStatus("current")
_VoipPortSipCallsvcTable_Object = MibTable
voipPortSipCallsvcTable = _VoipPortSipCallsvcTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 14, 9)
)
if mibBuilder.loadTexts:
    voipPortSipCallsvcTable.setStatus("current")
_VoipPortSipCallsvcEntry_Object = MibTableRow
voipPortSipCallsvcEntry = _VoipPortSipCallsvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 14, 9, 1)
)
voipPortSipCallsvcEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    voipPortSipCallsvcEntry.setStatus("current")


class _VoipPortSipCallsvcMode_Type(Integer32):
    """Custom type voipPortSipCallsvcMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("profile", 1),
          ("line", 2))
    )


_VoipPortSipCallsvcMode_Type.__name__ = "Integer32"
_VoipPortSipCallsvcMode_Object = MibTableColumn
voipPortSipCallsvcMode = _VoipPortSipCallsvcMode_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 14, 9, 1, 1),
    _VoipPortSipCallsvcMode_Type()
)
voipPortSipCallsvcMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipPortSipCallsvcMode.setStatus("current")
_VoipPortSipCallsvcStateMask_Type = Integer32
_VoipPortSipCallsvcStateMask_Object = MibTableColumn
voipPortSipCallsvcStateMask = _VoipPortSipCallsvcStateMask_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 14, 9, 1, 2),
    _VoipPortSipCallsvcStateMask_Type()
)
voipPortSipCallsvcStateMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipPortSipCallsvcStateMask.setStatus("current")


class _VoipPortSipCallsvcCPCOn_Type(Integer32):
    """Custom type voipPortSipCallsvcCPCOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_VoipPortSipCallsvcCPCOn_Type.__name__ = "Integer32"
_VoipPortSipCallsvcCPCOn_Object = MibTableColumn
voipPortSipCallsvcCPCOn = _VoipPortSipCallsvcCPCOn_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 14, 9, 1, 3),
    _VoipPortSipCallsvcCPCOn_Type()
)
voipPortSipCallsvcCPCOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipPortSipCallsvcCPCOn.setStatus("current")


class _VoipPortSipCallsvcCPCTimeout_Type(Integer32):
    """Custom type voipPortSipCallsvcCPCTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 60),
    )


_VoipPortSipCallsvcCPCTimeout_Type.__name__ = "Integer32"
_VoipPortSipCallsvcCPCTimeout_Object = MibTableColumn
voipPortSipCallsvcCPCTimeout = _VoipPortSipCallsvcCPCTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 14, 9, 1, 4),
    _VoipPortSipCallsvcCPCTimeout_Type()
)
voipPortSipCallsvcCPCTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipPortSipCallsvcCPCTimeout.setStatus("current")
_SnrMgn_ObjectIdentity = ObjectIdentity
snrMgn = _SnrMgn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 15)
)
_SnrMgnTable_Object = MibTable
snrMgnTable = _SnrMgnTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 15, 1)
)
if mibBuilder.loadTexts:
    snrMgnTable.setStatus("current")
_SnrMgnEntry_Object = MibTableRow
snrMgnEntry = _SnrMgnEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 15, 1, 1)
)
snrMgnEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    snrMgnEntry.setStatus("current")


class _SnrMgnMode_Type(Integer32):
    """Custom type snrMgnMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("profile", 0),
          ("line", 1))
    )


_SnrMgnMode_Type.__name__ = "Integer32"
_SnrMgnMode_Object = MibTableColumn
snrMgnMode = _SnrMgnMode_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 15, 1, 1, 1),
    _SnrMgnMode_Type()
)
snrMgnMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snrMgnMode.setStatus("current")


class _SnrMgnUcTarget_Type(Integer32):
    """Custom type snrMgnUcTarget based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 310),
    )


_SnrMgnUcTarget_Type.__name__ = "Integer32"
_SnrMgnUcTarget_Object = MibTableColumn
snrMgnUcTarget = _SnrMgnUcTarget_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 15, 1, 1, 2),
    _SnrMgnUcTarget_Type()
)
snrMgnUcTarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snrMgnUcTarget.setStatus("current")
if mibBuilder.loadTexts:
    snrMgnUcTarget.setUnits("tenth dB")


class _SnrMgnUcMax_Type(Integer32):
    """Custom type snrMgnUcMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 310),
    )


_SnrMgnUcMax_Type.__name__ = "Integer32"
_SnrMgnUcMax_Object = MibTableColumn
snrMgnUcMax = _SnrMgnUcMax_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 15, 1, 1, 3),
    _SnrMgnUcMax_Type()
)
snrMgnUcMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snrMgnUcMax.setStatus("current")
if mibBuilder.loadTexts:
    snrMgnUcMax.setUnits("tenth dB")


class _SnrMgnUcMin_Type(Integer32):
    """Custom type snrMgnUcMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 310),
    )


_SnrMgnUcMin_Type.__name__ = "Integer32"
_SnrMgnUcMin_Object = MibTableColumn
snrMgnUcMin = _SnrMgnUcMin_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 15, 1, 1, 4),
    _SnrMgnUcMin_Type()
)
snrMgnUcMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snrMgnUcMin.setStatus("current")
if mibBuilder.loadTexts:
    snrMgnUcMin.setUnits("tenth dB")


class _SnrMgnUcDownshift_Type(Integer32):
    """Custom type snrMgnUcDownshift based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 310),
    )


_SnrMgnUcDownshift_Type.__name__ = "Integer32"
_SnrMgnUcDownshift_Object = MibTableColumn
snrMgnUcDownshift = _SnrMgnUcDownshift_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 15, 1, 1, 5),
    _SnrMgnUcDownshift_Type()
)
snrMgnUcDownshift.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snrMgnUcDownshift.setStatus("current")
if mibBuilder.loadTexts:
    snrMgnUcDownshift.setUnits("tenth dB")


class _SnrMgnUcUpshift_Type(Integer32):
    """Custom type snrMgnUcUpshift based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 310),
    )


_SnrMgnUcUpshift_Type.__name__ = "Integer32"
_SnrMgnUcUpshift_Object = MibTableColumn
snrMgnUcUpshift = _SnrMgnUcUpshift_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 15, 1, 1, 6),
    _SnrMgnUcUpshift_Type()
)
snrMgnUcUpshift.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snrMgnUcUpshift.setStatus("current")
if mibBuilder.loadTexts:
    snrMgnUcUpshift.setUnits("tenth dB")


class _SnrMgnUrTarget_Type(Integer32):
    """Custom type snrMgnUrTarget based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 310),
    )


_SnrMgnUrTarget_Type.__name__ = "Integer32"
_SnrMgnUrTarget_Object = MibTableColumn
snrMgnUrTarget = _SnrMgnUrTarget_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 15, 1, 1, 7),
    _SnrMgnUrTarget_Type()
)
snrMgnUrTarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snrMgnUrTarget.setStatus("current")
if mibBuilder.loadTexts:
    snrMgnUrTarget.setUnits("tenth dB")


class _SnrMgnUrMax_Type(Integer32):
    """Custom type snrMgnUrMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 310),
    )


_SnrMgnUrMax_Type.__name__ = "Integer32"
_SnrMgnUrMax_Object = MibTableColumn
snrMgnUrMax = _SnrMgnUrMax_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 15, 1, 1, 8),
    _SnrMgnUrMax_Type()
)
snrMgnUrMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snrMgnUrMax.setStatus("current")
if mibBuilder.loadTexts:
    snrMgnUrMax.setUnits("tenth dB")


class _SnrMgnUrMin_Type(Integer32):
    """Custom type snrMgnUrMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 310),
    )


_SnrMgnUrMin_Type.__name__ = "Integer32"
_SnrMgnUrMin_Object = MibTableColumn
snrMgnUrMin = _SnrMgnUrMin_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 15, 1, 1, 9),
    _SnrMgnUrMin_Type()
)
snrMgnUrMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snrMgnUrMin.setStatus("current")
if mibBuilder.loadTexts:
    snrMgnUrMin.setUnits("tenth dB")


class _SnrMgnUrDownshift_Type(Integer32):
    """Custom type snrMgnUrDownshift based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 310),
    )


_SnrMgnUrDownshift_Type.__name__ = "Integer32"
_SnrMgnUrDownshift_Object = MibTableColumn
snrMgnUrDownshift = _SnrMgnUrDownshift_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 15, 1, 1, 10),
    _SnrMgnUrDownshift_Type()
)
snrMgnUrDownshift.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snrMgnUrDownshift.setStatus("current")
if mibBuilder.loadTexts:
    snrMgnUrDownshift.setUnits("tenth dB")


class _SnrMgnUrUpshift_Type(Integer32):
    """Custom type snrMgnUrUpshift based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 310),
    )


_SnrMgnUrUpshift_Type.__name__ = "Integer32"
_SnrMgnUrUpshift_Object = MibTableColumn
snrMgnUrUpshift = _SnrMgnUrUpshift_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 15, 1, 1, 11),
    _SnrMgnUrUpshift_Type()
)
snrMgnUrUpshift.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snrMgnUrUpshift.setStatus("current")
if mibBuilder.loadTexts:
    snrMgnUrUpshift.setUnits("tenth dB")
_DslRate_ObjectIdentity = ObjectIdentity
dslRate = _DslRate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 16)
)
_DslRateTable_Object = MibTable
dslRateTable = _DslRateTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 16, 1)
)
if mibBuilder.loadTexts:
    dslRateTable.setStatus("current")
_DslRateEntry_Object = MibTableRow
dslRateEntry = _DslRateEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 16, 1, 1)
)
dslRateEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dslRateEntry.setStatus("current")


class _DslRateMode_Type(Integer32):
    """Custom type dslRateMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("profile", 0),
          ("line", 1))
    )


_DslRateMode_Type.__name__ = "Integer32"
_DslRateMode_Object = MibTableColumn
dslRateMode = _DslRateMode_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 16, 1, 1, 1),
    _DslRateMode_Type()
)
dslRateMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dslRateMode.setStatus("current")


class _DslRateLatencyMode_Type(Integer32):
    """Custom type dslRateLatencyMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("interleave", 1),
          ("fast", 2))
    )


_DslRateLatencyMode_Type.__name__ = "Integer32"
_DslRateLatencyMode_Object = MibTableColumn
dslRateLatencyMode = _DslRateLatencyMode_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 16, 1, 1, 2),
    _DslRateLatencyMode_Type()
)
dslRateLatencyMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslRateLatencyMode.setStatus("current")


class _DslRateXtucMaxInterleaveDelay_Type(Integer32):
    """Custom type dslRateXtucMaxInterleaveDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DslRateXtucMaxInterleaveDelay_Type.__name__ = "Integer32"
_DslRateXtucMaxInterleaveDelay_Object = MibTableColumn
dslRateXtucMaxInterleaveDelay = _DslRateXtucMaxInterleaveDelay_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 16, 1, 1, 3),
    _DslRateXtucMaxInterleaveDelay_Type()
)
dslRateXtucMaxInterleaveDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dslRateXtucMaxInterleaveDelay.setStatus("current")
if mibBuilder.loadTexts:
    dslRateXtucMaxInterleaveDelay.setUnits("milli-seconds")
_DslRateXtucMaxTxRate_Type = Unsigned32
_DslRateXtucMaxTxRate_Object = MibTableColumn
dslRateXtucMaxTxRate = _DslRateXtucMaxTxRate_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 16, 1, 1, 4),
    _DslRateXtucMaxTxRate_Type()
)
dslRateXtucMaxTxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dslRateXtucMaxTxRate.setStatus("current")
if mibBuilder.loadTexts:
    dslRateXtucMaxTxRate.setUnits("kbps")
_DslRateXtucMinTxRate_Type = Unsigned32
_DslRateXtucMinTxRate_Object = MibTableColumn
dslRateXtucMinTxRate = _DslRateXtucMinTxRate_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 16, 1, 1, 5),
    _DslRateXtucMinTxRate_Type()
)
dslRateXtucMinTxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dslRateXtucMinTxRate.setStatus("current")
if mibBuilder.loadTexts:
    dslRateXtucMinTxRate.setUnits("kbps")


class _DslRateXturMaxInterleaveDelay_Type(Integer32):
    """Custom type dslRateXturMaxInterleaveDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DslRateXturMaxInterleaveDelay_Type.__name__ = "Integer32"
_DslRateXturMaxInterleaveDelay_Object = MibTableColumn
dslRateXturMaxInterleaveDelay = _DslRateXturMaxInterleaveDelay_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 16, 1, 1, 6),
    _DslRateXturMaxInterleaveDelay_Type()
)
dslRateXturMaxInterleaveDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dslRateXturMaxInterleaveDelay.setStatus("current")
if mibBuilder.loadTexts:
    dslRateXturMaxInterleaveDelay.setUnits("milli-seconds")
_DslRateXturMaxTxRate_Type = Unsigned32
_DslRateXturMaxTxRate_Object = MibTableColumn
dslRateXturMaxTxRate = _DslRateXturMaxTxRate_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 16, 1, 1, 7),
    _DslRateXturMaxTxRate_Type()
)
dslRateXturMaxTxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dslRateXturMaxTxRate.setStatus("current")
if mibBuilder.loadTexts:
    dslRateXturMaxTxRate.setUnits("kbps")
_DslRateXturMinTxRate_Type = Unsigned32
_DslRateXturMinTxRate_Object = MibTableColumn
dslRateXturMinTxRate = _DslRateXturMinTxRate_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 16, 1, 1, 8),
    _DslRateXturMinTxRate_Type()
)
dslRateXturMinTxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dslRateXturMinTxRate.setStatus("current")
if mibBuilder.loadTexts:
    dslRateXturMinTxRate.setUnits("kbps")
_Gbond_ObjectIdentity = ObjectIdentity
gbond = _Gbond_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 51)
)
_GbondGroupTable_Object = MibTable
gbondGroupTable = _GbondGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 51, 1)
)
if mibBuilder.loadTexts:
    gbondGroupTable.setStatus("current")
_GbondGroupEntry_Object = MibTableRow
gbondGroupEntry = _GbondGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 51, 1, 1)
)
gbondGroupEntry.setIndexNames(
    (0, "E5-121-MIB", "gbondGroupName"),
)
if mibBuilder.loadTexts:
    gbondGroupEntry.setStatus("current")


class _GbondGroupName_Type(OctetString):
    """Custom type gbondGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_GbondGroupName_Type.__name__ = "OctetString"
_GbondGroupName_Object = MibTableColumn
gbondGroupName = _GbondGroupName_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 51, 1, 1, 1),
    _GbondGroupName_Type()
)
gbondGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gbondGroupName.setStatus("current")
_GbondGroupPorts_Type = OctetString
_GbondGroupPorts_Object = MibTableColumn
gbondGroupPorts = _GbondGroupPorts_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 51, 1, 1, 2),
    _GbondGroupPorts_Type()
)
gbondGroupPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gbondGroupPorts.setStatus("current")
_GbondGroupUpRate_Type = Unsigned32
_GbondGroupUpRate_Object = MibTableColumn
gbondGroupUpRate = _GbondGroupUpRate_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 51, 1, 1, 4),
    _GbondGroupUpRate_Type()
)
gbondGroupUpRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gbondGroupUpRate.setStatus("current")
_GbondGroupDownRate_Type = Unsigned32
_GbondGroupDownRate_Object = MibTableColumn
gbondGroupDownRate = _GbondGroupDownRate_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 51, 1, 1, 5),
    _GbondGroupDownRate_Type()
)
gbondGroupDownRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gbondGroupDownRate.setStatus("current")
_GbondGroupRowStatus_Type = RowStatus
_GbondGroupRowStatus_Object = MibTableColumn
gbondGroupRowStatus = _GbondGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 8, 51, 1, 1, 6),
    _GbondGroupRowStatus_Type()
)
gbondGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gbondGroupRowStatus.setStatus("current")
_Profile_ObjectIdentity = ObjectIdentity
profile = _Profile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9)
)
_SraShiftMarginProfile_ObjectIdentity = ObjectIdentity
sraShiftMarginProfile = _SraShiftMarginProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 1)
)
_SraShiftMarginProfileTable_Object = MibTable
sraShiftMarginProfileTable = _SraShiftMarginProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 1, 1)
)
if mibBuilder.loadTexts:
    sraShiftMarginProfileTable.setStatus("current")
_SraShiftMarginProfileEntry_Object = MibTableRow
sraShiftMarginProfileEntry = _SraShiftMarginProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 1, 1, 1)
)
sraShiftMarginProfileEntry.setIndexNames(
    (0, "E5-121-MIB", "sraShiftMarginProfileName"),
)
if mibBuilder.loadTexts:
    sraShiftMarginProfileEntry.setStatus("current")


class _SraShiftMarginProfileName_Type(DisplayString):
    """Custom type sraShiftMarginProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_SraShiftMarginProfileName_Type.__name__ = "DisplayString"
_SraShiftMarginProfileName_Object = MibTableColumn
sraShiftMarginProfileName = _SraShiftMarginProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 1, 1, 1, 1),
    _SraShiftMarginProfileName_Type()
)
sraShiftMarginProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sraShiftMarginProfileName.setStatus("current")


class _XtucConfDownshiftSnrMgn_Type(Integer32):
    """Custom type xtucConfDownshiftSnrMgn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_XtucConfDownshiftSnrMgn_Type.__name__ = "Integer32"
_XtucConfDownshiftSnrMgn_Object = MibTableColumn
xtucConfDownshiftSnrMgn = _XtucConfDownshiftSnrMgn_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 1, 1, 1, 2),
    _XtucConfDownshiftSnrMgn_Type()
)
xtucConfDownshiftSnrMgn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xtucConfDownshiftSnrMgn.setStatus("current")


class _XtucConfUpshiftSnrMgn_Type(Integer32):
    """Custom type xtucConfUpshiftSnrMgn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_XtucConfUpshiftSnrMgn_Type.__name__ = "Integer32"
_XtucConfUpshiftSnrMgn_Object = MibTableColumn
xtucConfUpshiftSnrMgn = _XtucConfUpshiftSnrMgn_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 1, 1, 1, 3),
    _XtucConfUpshiftSnrMgn_Type()
)
xtucConfUpshiftSnrMgn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xtucConfUpshiftSnrMgn.setStatus("current")


class _XtucConfDownshiftTime_Type(Integer32):
    """Custom type xtucConfDownshiftTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_XtucConfDownshiftTime_Type.__name__ = "Integer32"
_XtucConfDownshiftTime_Object = MibTableColumn
xtucConfDownshiftTime = _XtucConfDownshiftTime_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 1, 1, 1, 4),
    _XtucConfDownshiftTime_Type()
)
xtucConfDownshiftTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xtucConfDownshiftTime.setStatus("current")


class _XtucConfUpshiftTime_Type(Integer32):
    """Custom type xtucConfUpshiftTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_XtucConfUpshiftTime_Type.__name__ = "Integer32"
_XtucConfUpshiftTime_Object = MibTableColumn
xtucConfUpshiftTime = _XtucConfUpshiftTime_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 1, 1, 1, 5),
    _XtucConfUpshiftTime_Type()
)
xtucConfUpshiftTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xtucConfUpshiftTime.setStatus("current")


class _XturConfDownshiftSnrMgn_Type(Integer32):
    """Custom type xturConfDownshiftSnrMgn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_XturConfDownshiftSnrMgn_Type.__name__ = "Integer32"
_XturConfDownshiftSnrMgn_Object = MibTableColumn
xturConfDownshiftSnrMgn = _XturConfDownshiftSnrMgn_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 1, 1, 1, 6),
    _XturConfDownshiftSnrMgn_Type()
)
xturConfDownshiftSnrMgn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xturConfDownshiftSnrMgn.setStatus("current")


class _XturConfUpshiftSnrMgn_Type(Integer32):
    """Custom type xturConfUpshiftSnrMgn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_XturConfUpshiftSnrMgn_Type.__name__ = "Integer32"
_XturConfUpshiftSnrMgn_Object = MibTableColumn
xturConfUpshiftSnrMgn = _XturConfUpshiftSnrMgn_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 1, 1, 1, 7),
    _XturConfUpshiftSnrMgn_Type()
)
xturConfUpshiftSnrMgn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xturConfUpshiftSnrMgn.setStatus("current")


class _XturConfDownshiftTime_Type(Integer32):
    """Custom type xturConfDownshiftTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_XturConfDownshiftTime_Type.__name__ = "Integer32"
_XturConfDownshiftTime_Object = MibTableColumn
xturConfDownshiftTime = _XturConfDownshiftTime_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 1, 1, 1, 8),
    _XturConfDownshiftTime_Type()
)
xturConfDownshiftTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xturConfDownshiftTime.setStatus("current")


class _XturConfUpshiftTime_Type(Integer32):
    """Custom type xturConfUpshiftTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_XturConfUpshiftTime_Type.__name__ = "Integer32"
_XturConfUpshiftTime_Object = MibTableColumn
xturConfUpshiftTime = _XturConfUpshiftTime_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 1, 1, 1, 9),
    _XturConfUpshiftTime_Type()
)
xturConfUpshiftTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xturConfUpshiftTime.setStatus("current")
_SraShiftMarginProfileStatus_Type = RowStatus
_SraShiftMarginProfileStatus_Object = MibTableColumn
sraShiftMarginProfileStatus = _SraShiftMarginProfileStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 1, 1, 1, 10),
    _SraShiftMarginProfileStatus_Type()
)
sraShiftMarginProfileStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sraShiftMarginProfileStatus.setStatus("current")
_VoipProfile_ObjectIdentity = ObjectIdentity
voipProfile = _VoipProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 7)
)
_SipProfile_ObjectIdentity = ObjectIdentity
sipProfile = _SipProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 7, 1)
)
_MaxNumOfSipProfiles_Type = Integer32
_MaxNumOfSipProfiles_Object = MibScalar
maxNumOfSipProfiles = _MaxNumOfSipProfiles_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 7, 1, 1),
    _MaxNumOfSipProfiles_Type()
)
maxNumOfSipProfiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumOfSipProfiles.setStatus("current")
_SipProfileTable_Object = MibTable
sipProfileTable = _SipProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 7, 1, 2)
)
if mibBuilder.loadTexts:
    sipProfileTable.setStatus("current")
_SipProfileEntry_Object = MibTableRow
sipProfileEntry = _SipProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 7, 1, 2, 1)
)
sipProfileEntry.setIndexNames(
    (1, "E5-121-MIB", "sipProfileName"),
)
if mibBuilder.loadTexts:
    sipProfileEntry.setStatus("current")


class _SipProfileName_Type(DisplayString):
    """Custom type sipProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_SipProfileName_Type.__name__ = "DisplayString"
_SipProfileName_Object = MibTableColumn
sipProfileName = _SipProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 7, 1, 2, 1, 1),
    _SipProfileName_Type()
)
sipProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipProfileName.setStatus("current")
_SipProfileSipSvr_Type = OctetString
_SipProfileSipSvr_Object = MibTableColumn
sipProfileSipSvr = _SipProfileSipSvr_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 7, 1, 2, 1, 2),
    _SipProfileSipSvr_Type()
)
sipProfileSipSvr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipProfileSipSvr.setStatus("current")
_SipProfileRegSvr_Type = OctetString
_SipProfileRegSvr_Object = MibTableColumn
sipProfileRegSvr = _SipProfileRegSvr_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 7, 1, 2, 1, 3),
    _SipProfileRegSvr_Type()
)
sipProfileRegSvr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipProfileRegSvr.setStatus("current")
_SipProfileProxySvr_Type = OctetString
_SipProfileProxySvr_Object = MibTableColumn
sipProfileProxySvr = _SipProfileProxySvr_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 7, 1, 2, 1, 4),
    _SipProfileProxySvr_Type()
)
sipProfileProxySvr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipProfileProxySvr.setStatus("current")


class _SipProfileSipPort_Type(Integer32):
    """Custom type sipProfileSipPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1025, 65535),
    )


_SipProfileSipPort_Type.__name__ = "Integer32"
_SipProfileSipPort_Object = MibTableColumn
sipProfileSipPort = _SipProfileSipPort_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 7, 1, 2, 1, 5),
    _SipProfileSipPort_Type()
)
sipProfileSipPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipProfileSipPort.setStatus("current")


class _SipProfileRegSvrPort_Type(Integer32):
    """Custom type sipProfileRegSvrPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1025, 65535),
    )


_SipProfileRegSvrPort_Type.__name__ = "Integer32"
_SipProfileRegSvrPort_Object = MibTableColumn
sipProfileRegSvrPort = _SipProfileRegSvrPort_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 7, 1, 2, 1, 6),
    _SipProfileRegSvrPort_Type()
)
sipProfileRegSvrPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipProfileRegSvrPort.setStatus("current")


class _SipProfileProxySvrPort_Type(Integer32):
    """Custom type sipProfileProxySvrPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1025, 65535),
    )


_SipProfileProxySvrPort_Type.__name__ = "Integer32"
_SipProfileProxySvrPort_Object = MibTableColumn
sipProfileProxySvrPort = _SipProfileProxySvrPort_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 7, 1, 2, 1, 7),
    _SipProfileProxySvrPort_Type()
)
sipProfileProxySvrPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipProfileProxySvrPort.setStatus("current")


class _SipProfileUriType_Type(Integer32):
    """Custom type sipProfileUriType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("useSipUri", 1),
          ("useTelUri", 2))
    )


_SipProfileUriType_Type.__name__ = "Integer32"
_SipProfileUriType_Object = MibTableColumn
sipProfileUriType = _SipProfileUriType_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 7, 1, 2, 1, 8),
    _SipProfileUriType_Type()
)
sipProfileUriType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipProfileUriType.setStatus("current")


class _SipProfilePbit_Type(Integer32):
    """Custom type sipProfilePbit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SipProfilePbit_Type.__name__ = "Integer32"
_SipProfilePbit_Object = MibTableColumn
sipProfilePbit = _SipProfilePbit_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 7, 1, 2, 1, 9),
    _SipProfilePbit_Type()
)
sipProfilePbit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipProfilePbit.setStatus("current")


class _SipProfileDscp_Type(Integer32):
    """Custom type sipProfileDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_SipProfileDscp_Type.__name__ = "Integer32"
_SipProfileDscp_Object = MibTableColumn
sipProfileDscp = _SipProfileDscp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 7, 1, 2, 1, 10),
    _SipProfileDscp_Type()
)
sipProfileDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipProfileDscp.setStatus("current")


class _SipProfileKeepAlive_Type(Integer32):
    """Custom type sipProfileKeepAlive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_SipProfileKeepAlive_Type.__name__ = "Integer32"
_SipProfileKeepAlive_Object = MibTableColumn
sipProfileKeepAlive = _SipProfileKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 7, 1, 2, 1, 11),
    _SipProfileKeepAlive_Type()
)
sipProfileKeepAlive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipProfileKeepAlive.setStatus("current")


class _SipProfileSe_Type(Integer32):
    """Custom type sipProfileSe based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(90, 65535),
    )


_SipProfileSe_Type.__name__ = "Integer32"
_SipProfileSe_Object = MibTableColumn
sipProfileSe = _SipProfileSe_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 7, 1, 2, 1, 12),
    _SipProfileSe_Type()
)
sipProfileSe.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipProfileSe.setStatus("current")
if mibBuilder.loadTexts:
    sipProfileSe.setUnits("second")


class _SipProfilePrack_Type(Integer32):
    """Custom type sipProfilePrack based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_SipProfilePrack_Type.__name__ = "Integer32"
_SipProfilePrack_Object = MibTableColumn
sipProfilePrack = _SipProfilePrack_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 7, 1, 2, 1, 13),
    _SipProfilePrack_Type()
)
sipProfilePrack.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipProfilePrack.setStatus("current")
_SipProfileRowStatus_Type = RowStatus
_SipProfileRowStatus_Object = MibTableColumn
sipProfileRowStatus = _SipProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 7, 1, 2, 1, 14),
    _SipProfileRowStatus_Type()
)
sipProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipProfileRowStatus.setStatus("current")


class _SipProfileRegExpire_Type(Integer32):
    """Custom type sipProfileRegExpire based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(120, 2073600),
    )


_SipProfileRegExpire_Type.__name__ = "Integer32"
_SipProfileRegExpire_Object = MibTableColumn
sipProfileRegExpire = _SipProfileRegExpire_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 7, 1, 2, 1, 15),
    _SipProfileRegExpire_Type()
)
sipProfileRegExpire.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipProfileRegExpire.setStatus("current")
if mibBuilder.loadTexts:
    sipProfileRegExpire.setUnits("second")
_MaxNumOfSipCallSvcProfiles_Type = Integer32
_MaxNumOfSipCallSvcProfiles_Object = MibScalar
maxNumOfSipCallSvcProfiles = _MaxNumOfSipCallSvcProfiles_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 7, 1, 3),
    _MaxNumOfSipCallSvcProfiles_Type()
)
maxNumOfSipCallSvcProfiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumOfSipCallSvcProfiles.setStatus("current")
_SipCallSvcProfileTable_Object = MibTable
sipCallSvcProfileTable = _SipCallSvcProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 7, 1, 4)
)
if mibBuilder.loadTexts:
    sipCallSvcProfileTable.setStatus("current")
_SipCallSvcProfileEntry_Object = MibTableRow
sipCallSvcProfileEntry = _SipCallSvcProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 7, 1, 4, 1)
)
sipCallSvcProfileEntry.setIndexNames(
    (1, "E5-121-MIB", "sipCallSvcProfileName"),
)
if mibBuilder.loadTexts:
    sipCallSvcProfileEntry.setStatus("current")


class _SipCallSvcProfileName_Type(DisplayString):
    """Custom type sipCallSvcProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_SipCallSvcProfileName_Type.__name__ = "DisplayString"
_SipCallSvcProfileName_Object = MibTableColumn
sipCallSvcProfileName = _SipCallSvcProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 7, 1, 4, 1, 1),
    _SipCallSvcProfileName_Type()
)
sipCallSvcProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipCallSvcProfileName.setStatus("current")


class _SipCallSvcProfilePasswdOn_Type(Integer32):
    """Custom type sipCallSvcProfilePasswdOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_SipCallSvcProfilePasswdOn_Type.__name__ = "Integer32"
_SipCallSvcProfilePasswdOn_Object = MibTableColumn
sipCallSvcProfilePasswdOn = _SipCallSvcProfilePasswdOn_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 7, 1, 4, 1, 2),
    _SipCallSvcProfilePasswdOn_Type()
)
sipCallSvcProfilePasswdOn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipCallSvcProfilePasswdOn.setStatus("current")
_SipCallSvcProfilePasswd_Type = OctetString
_SipCallSvcProfilePasswd_Object = MibTableColumn
sipCallSvcProfilePasswd = _SipCallSvcProfilePasswd_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 7, 1, 4, 1, 3),
    _SipCallSvcProfilePasswd_Type()
)
sipCallSvcProfilePasswd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipCallSvcProfilePasswd.setStatus("current")


class _SipCallSvcProfileNumberPlanOn_Type(Integer32):
    """Custom type sipCallSvcProfileNumberPlanOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_SipCallSvcProfileNumberPlanOn_Type.__name__ = "Integer32"
_SipCallSvcProfileNumberPlanOn_Object = MibTableColumn
sipCallSvcProfileNumberPlanOn = _SipCallSvcProfileNumberPlanOn_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 7, 1, 4, 1, 4),
    _SipCallSvcProfileNumberPlanOn_Type()
)
sipCallSvcProfileNumberPlanOn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipCallSvcProfileNumberPlanOn.setStatus("current")
_SipCallSvcProfileNumberPlanCc_Type = OctetString
_SipCallSvcProfileNumberPlanCc_Object = MibTableColumn
sipCallSvcProfileNumberPlanCc = _SipCallSvcProfileNumberPlanCc_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 7, 1, 4, 1, 5),
    _SipCallSvcProfileNumberPlanCc_Type()
)
sipCallSvcProfileNumberPlanCc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipCallSvcProfileNumberPlanCc.setStatus("current")
_SipCallSvcProfileNumberPlanNdc_Type = OctetString
_SipCallSvcProfileNumberPlanNdc_Object = MibTableColumn
sipCallSvcProfileNumberPlanNdc = _SipCallSvcProfileNumberPlanNdc_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 7, 1, 4, 1, 6),
    _SipCallSvcProfileNumberPlanNdc_Type()
)
sipCallSvcProfileNumberPlanNdc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipCallSvcProfileNumberPlanNdc.setStatus("current")
_SipCallSvcProfileNumberPlanTable_Type = OctetString
_SipCallSvcProfileNumberPlanTable_Object = MibTableColumn
sipCallSvcProfileNumberPlanTable = _SipCallSvcProfileNumberPlanTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 7, 1, 4, 1, 7),
    _SipCallSvcProfileNumberPlanTable_Type()
)
sipCallSvcProfileNumberPlanTable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipCallSvcProfileNumberPlanTable.setStatus("current")
_SipCallSvcProfileStateMask_Type = Integer32
_SipCallSvcProfileStateMask_Object = MibTableColumn
sipCallSvcProfileStateMask = _SipCallSvcProfileStateMask_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 7, 1, 4, 1, 8),
    _SipCallSvcProfileStateMask_Type()
)
sipCallSvcProfileStateMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipCallSvcProfileStateMask.setStatus("current")


class _SipCallSvcProfileDtmf_Type(Integer32):
    """Custom type sipCallSvcProfileDtmf based on Integer32"""
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
        *(("bypass", 1),
          ("rfc2833", 2),
          ("rfc2833like", 3),
          ("sipinfo", 4))
    )


_SipCallSvcProfileDtmf_Type.__name__ = "Integer32"
_SipCallSvcProfileDtmf_Object = MibTableColumn
sipCallSvcProfileDtmf = _SipCallSvcProfileDtmf_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 7, 1, 4, 1, 9),
    _SipCallSvcProfileDtmf_Type()
)
sipCallSvcProfileDtmf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipCallSvcProfileDtmf.setStatus("current")


class _SipCallSvcProfileFax_Type(Integer32):
    """Custom type sipCallSvcProfileFax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("g711", 1),
          ("t38", 2))
    )


_SipCallSvcProfileFax_Type.__name__ = "Integer32"
_SipCallSvcProfileFax_Object = MibTableColumn
sipCallSvcProfileFax = _SipCallSvcProfileFax_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 7, 1, 4, 1, 10),
    _SipCallSvcProfileFax_Type()
)
sipCallSvcProfileFax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipCallSvcProfileFax.setStatus("current")
_SipCallSvcProfileRowStatus_Type = RowStatus
_SipCallSvcProfileRowStatus_Object = MibTableColumn
sipCallSvcProfileRowStatus = _SipCallSvcProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 7, 1, 4, 1, 11),
    _SipCallSvcProfileRowStatus_Type()
)
sipCallSvcProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipCallSvcProfileRowStatus.setStatus("current")


class _SipCallSvcProfileFlashType_Type(Integer32):
    """Custom type sipCallSvcProfileFlashType based on Integer32"""
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
        *(("invite", 1),
          ("rfc2833", 2),
          ("rfc2833like", 3),
          ("sipinfo1", 4),
          ("sipinfo2", 5),
          ("sipinfo3", 6),
          ("sipinfo4", 7),
          ("sipinfo5", 8),
          ("sipinfo6", 9),
          ("bypass", 10))
    )


_SipCallSvcProfileFlashType_Type.__name__ = "Integer32"
_SipCallSvcProfileFlashType_Object = MibTableColumn
sipCallSvcProfileFlashType = _SipCallSvcProfileFlashType_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 7, 1, 4, 1, 12),
    _SipCallSvcProfileFlashType_Type()
)
sipCallSvcProfileFlashType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipCallSvcProfileFlashType.setStatus("current")
_SipCallSvcProfileFlashInfo_Type = OctetString
_SipCallSvcProfileFlashInfo_Object = MibTableColumn
sipCallSvcProfileFlashInfo = _SipCallSvcProfileFlashInfo_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 7, 1, 4, 1, 13),
    _SipCallSvcProfileFlashInfo_Type()
)
sipCallSvcProfileFlashInfo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipCallSvcProfileFlashInfo.setStatus("current")


class _SipCallSvcProfileSoftSwitchType_Type(Integer32):
    """Custom type sipCallSvcProfileSoftSwitchType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("metaswitch", 1),
          ("nortel", 2))
    )


_SipCallSvcProfileSoftSwitchType_Type.__name__ = "Integer32"
_SipCallSvcProfileSoftSwitchType_Object = MibTableColumn
sipCallSvcProfileSoftSwitchType = _SipCallSvcProfileSoftSwitchType_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 7, 1, 4, 1, 14),
    _SipCallSvcProfileSoftSwitchType_Type()
)
sipCallSvcProfileSoftSwitchType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipCallSvcProfileSoftSwitchType.setStatus("current")


class _SipCallSvcProfileCPCOn_Type(Integer32):
    """Custom type sipCallSvcProfileCPCOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_SipCallSvcProfileCPCOn_Type.__name__ = "Integer32"
_SipCallSvcProfileCPCOn_Object = MibTableColumn
sipCallSvcProfileCPCOn = _SipCallSvcProfileCPCOn_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 7, 1, 4, 1, 15),
    _SipCallSvcProfileCPCOn_Type()
)
sipCallSvcProfileCPCOn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipCallSvcProfileCPCOn.setStatus("current")


class _SipCallSvcProfileCPCTimeout_Type(Integer32):
    """Custom type sipCallSvcProfileCPCTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 60),
    )


_SipCallSvcProfileCPCTimeout_Type.__name__ = "Integer32"
_SipCallSvcProfileCPCTimeout_Object = MibTableColumn
sipCallSvcProfileCPCTimeout = _SipCallSvcProfileCPCTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 7, 1, 4, 1, 16),
    _SipCallSvcProfileCPCTimeout_Type()
)
sipCallSvcProfileCPCTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipCallSvcProfileCPCTimeout.setStatus("current")
_MaxNumOfDspProfiles_Type = Integer32
_MaxNumOfDspProfiles_Object = MibScalar
maxNumOfDspProfiles = _MaxNumOfDspProfiles_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 7, 2),
    _MaxNumOfDspProfiles_Type()
)
maxNumOfDspProfiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumOfDspProfiles.setStatus("current")
_DspProfileTable_Object = MibTable
dspProfileTable = _DspProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 7, 3)
)
if mibBuilder.loadTexts:
    dspProfileTable.setStatus("current")
_DspProfileEntry_Object = MibTableRow
dspProfileEntry = _DspProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 7, 3, 1)
)
dspProfileEntry.setIndexNames(
    (1, "E5-121-MIB", "dspProfileName"),
)
if mibBuilder.loadTexts:
    dspProfileEntry.setStatus("current")


class _DspProfileName_Type(DisplayString):
    """Custom type dspProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_DspProfileName_Type.__name__ = "DisplayString"
_DspProfileName_Object = MibTableColumn
dspProfileName = _DspProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 7, 3, 1, 1),
    _DspProfileName_Type()
)
dspProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dspProfileName.setStatus("current")
_DspProfileCodec_Type = OctetString
_DspProfileCodec_Object = MibTableColumn
dspProfileCodec = _DspProfileCodec_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 7, 3, 1, 2),
    _DspProfileCodec_Type()
)
dspProfileCodec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dspProfileCodec.setStatus("current")


class _DspProfilePlayBufferMinDelay_Type(Integer32):
    """Custom type dspProfilePlayBufferMinDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 500),
    )


_DspProfilePlayBufferMinDelay_Type.__name__ = "Integer32"
_DspProfilePlayBufferMinDelay_Object = MibTableColumn
dspProfilePlayBufferMinDelay = _DspProfilePlayBufferMinDelay_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 7, 3, 1, 3),
    _DspProfilePlayBufferMinDelay_Type()
)
dspProfilePlayBufferMinDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dspProfilePlayBufferMinDelay.setStatus("current")
if mibBuilder.loadTexts:
    dspProfilePlayBufferMinDelay.setUnits("millisecond")


class _DspProfilePlayBufferMaxDelay_Type(Integer32):
    """Custom type dspProfilePlayBufferMaxDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 500),
    )


_DspProfilePlayBufferMaxDelay_Type.__name__ = "Integer32"
_DspProfilePlayBufferMaxDelay_Object = MibTableColumn
dspProfilePlayBufferMaxDelay = _DspProfilePlayBufferMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 7, 3, 1, 4),
    _DspProfilePlayBufferMaxDelay_Type()
)
dspProfilePlayBufferMaxDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dspProfilePlayBufferMaxDelay.setStatus("current")
if mibBuilder.loadTexts:
    dspProfilePlayBufferMaxDelay.setUnits("millisecond")


class _DspProfileEchoTail_Type(Integer32):
    """Custom type dspProfileEchoTail based on Integer32"""
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
        *(("echotail8", 1),
          ("echotail16", 2),
          ("echotail32", 3),
          ("echotail128", 4))
    )


_DspProfileEchoTail_Type.__name__ = "Integer32"
_DspProfileEchoTail_Object = MibTableColumn
dspProfileEchoTail = _DspProfileEchoTail_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 7, 3, 1, 5),
    _DspProfileEchoTail_Type()
)
dspProfileEchoTail.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dspProfileEchoTail.setStatus("current")
_DspProfileRowStatus_Type = RowStatus
_DspProfileRowStatus_Object = MibTableColumn
dspProfileRowStatus = _DspProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 7, 3, 1, 6),
    _DspProfileRowStatus_Type()
)
dspProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dspProfileRowStatus.setStatus("current")


class _DspProfileG711Vpi_Type(Integer32):
    """Custom type dspProfileG711Vpi based on Integer32"""
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
        *(("g711x10ms", 1),
          ("g711x20ms", 2),
          ("g711x30ms", 3),
          ("g711x40ms", 4))
    )


_DspProfileG711Vpi_Type.__name__ = "Integer32"
_DspProfileG711Vpi_Object = MibTableColumn
dspProfileG711Vpi = _DspProfileG711Vpi_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 7, 3, 1, 7),
    _DspProfileG711Vpi_Type()
)
dspProfileG711Vpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dspProfileG711Vpi.setStatus("current")
if mibBuilder.loadTexts:
    dspProfileG711Vpi.setUnits("millisecond")


class _DspProfileG723Vpi_Type(Integer32):
    """Custom type dspProfileG723Vpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("g723x30ms", 1),
          ("g723x60ms", 2))
    )


_DspProfileG723Vpi_Type.__name__ = "Integer32"
_DspProfileG723Vpi_Object = MibTableColumn
dspProfileG723Vpi = _DspProfileG723Vpi_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 7, 3, 1, 8),
    _DspProfileG723Vpi_Type()
)
dspProfileG723Vpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dspProfileG723Vpi.setStatus("current")
if mibBuilder.loadTexts:
    dspProfileG723Vpi.setUnits("millisecond")


class _DspProfileG726Vpi_Type(Integer32):
    """Custom type dspProfileG726Vpi based on Integer32"""
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
        *(("g726x10ms", 1),
          ("g726x20ms", 2),
          ("g726x30ms", 3),
          ("g726x40ms", 4))
    )


_DspProfileG726Vpi_Type.__name__ = "Integer32"
_DspProfileG726Vpi_Object = MibTableColumn
dspProfileG726Vpi = _DspProfileG726Vpi_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 7, 3, 1, 9),
    _DspProfileG726Vpi_Type()
)
dspProfileG726Vpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dspProfileG726Vpi.setStatus("current")
if mibBuilder.loadTexts:
    dspProfileG726Vpi.setUnits("millisecond")


class _DspProfileG729Vpi_Type(Integer32):
    """Custom type dspProfileG729Vpi based on Integer32"""
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
        *(("g729x10ms", 1),
          ("g729x20ms", 2),
          ("g729x30ms", 3),
          ("g729x40ms", 4),
          ("g729x50ms", 5),
          ("g729x60ms", 6))
    )


_DspProfileG729Vpi_Type.__name__ = "Integer32"
_DspProfileG729Vpi_Object = MibTableColumn
dspProfileG729Vpi = _DspProfileG729Vpi_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 7, 3, 1, 10),
    _DspProfileG729Vpi_Type()
)
dspProfileG729Vpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dspProfileG729Vpi.setStatus("current")
if mibBuilder.loadTexts:
    dspProfileG729Vpi.setUnits("millisecond")
_H248Profile_ObjectIdentity = ObjectIdentity
h248Profile = _H248Profile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 7, 4)
)
_MaxNumOfH248Profiles_Type = Integer32
_MaxNumOfH248Profiles_Object = MibScalar
maxNumOfH248Profiles = _MaxNumOfH248Profiles_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 7, 4, 1),
    _MaxNumOfH248Profiles_Type()
)
maxNumOfH248Profiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumOfH248Profiles.setStatus("current")
_H248ProfileTable_Object = MibTable
h248ProfileTable = _H248ProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 7, 4, 2)
)
if mibBuilder.loadTexts:
    h248ProfileTable.setStatus("current")
_H248ProfileEntry_Object = MibTableRow
h248ProfileEntry = _H248ProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 7, 4, 2, 1)
)
h248ProfileEntry.setIndexNames(
    (1, "E5-121-MIB", "h248ProfileName"),
)
if mibBuilder.loadTexts:
    h248ProfileEntry.setStatus("current")


class _H248ProfileName_Type(DisplayString):
    """Custom type h248ProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_H248ProfileName_Type.__name__ = "DisplayString"
_H248ProfileName_Object = MibTableColumn
h248ProfileName = _H248ProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 7, 4, 2, 1, 1),
    _H248ProfileName_Type()
)
h248ProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h248ProfileName.setStatus("current")
_H248ProfileMgcSvr_Type = OctetString
_H248ProfileMgcSvr_Object = MibTableColumn
h248ProfileMgcSvr = _H248ProfileMgcSvr_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 7, 4, 2, 1, 2),
    _H248ProfileMgcSvr_Type()
)
h248ProfileMgcSvr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h248ProfileMgcSvr.setStatus("current")


class _H248ProfileMgcPort_Type(Integer32):
    """Custom type h248ProfileMgcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1025, 65535),
    )


_H248ProfileMgcPort_Type.__name__ = "Integer32"
_H248ProfileMgcPort_Object = MibTableColumn
h248ProfileMgcPort = _H248ProfileMgcPort_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 7, 4, 2, 1, 3),
    _H248ProfileMgcPort_Type()
)
h248ProfileMgcPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h248ProfileMgcPort.setStatus("current")


class _H248ProfileMgc2On_Type(Integer32):
    """Custom type h248ProfileMgc2On based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_H248ProfileMgc2On_Type.__name__ = "Integer32"
_H248ProfileMgc2On_Object = MibTableColumn
h248ProfileMgc2On = _H248ProfileMgc2On_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 7, 4, 2, 1, 4),
    _H248ProfileMgc2On_Type()
)
h248ProfileMgc2On.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h248ProfileMgc2On.setStatus("current")
_H248ProfileMgc2Svr_Type = OctetString
_H248ProfileMgc2Svr_Object = MibTableColumn
h248ProfileMgc2Svr = _H248ProfileMgc2Svr_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 7, 4, 2, 1, 5),
    _H248ProfileMgc2Svr_Type()
)
h248ProfileMgc2Svr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h248ProfileMgc2Svr.setStatus("current")


class _H248ProfileMgc2Port_Type(Integer32):
    """Custom type h248ProfileMgc2Port based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1025, 65535),
    )


_H248ProfileMgc2Port_Type.__name__ = "Integer32"
_H248ProfileMgc2Port_Object = MibTableColumn
h248ProfileMgc2Port = _H248ProfileMgc2Port_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 7, 4, 2, 1, 6),
    _H248ProfileMgc2Port_Type()
)
h248ProfileMgc2Port.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h248ProfileMgc2Port.setStatus("current")


class _H248ProfileTransport_Type(Integer32):
    """Custom type h248ProfileTransport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("udp", 1),
          ("tcp", 2))
    )


_H248ProfileTransport_Type.__name__ = "Integer32"
_H248ProfileTransport_Object = MibTableColumn
h248ProfileTransport = _H248ProfileTransport_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 7, 4, 2, 1, 7),
    _H248ProfileTransport_Type()
)
h248ProfileTransport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h248ProfileTransport.setStatus("current")


class _H248ProfileEncode_Type(Integer32):
    """Custom type h248ProfileEncode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("longtext", 1),
          ("shorttext", 2))
    )


_H248ProfileEncode_Type.__name__ = "Integer32"
_H248ProfileEncode_Object = MibTableColumn
h248ProfileEncode = _H248ProfileEncode_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 7, 4, 2, 1, 8),
    _H248ProfileEncode_Type()
)
h248ProfileEncode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h248ProfileEncode.setStatus("current")


class _H248ProfilePbit_Type(Integer32):
    """Custom type h248ProfilePbit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_H248ProfilePbit_Type.__name__ = "Integer32"
_H248ProfilePbit_Object = MibTableColumn
h248ProfilePbit = _H248ProfilePbit_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 7, 4, 2, 1, 9),
    _H248ProfilePbit_Type()
)
h248ProfilePbit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h248ProfilePbit.setStatus("current")


class _H248ProfileDscp_Type(Integer32):
    """Custom type h248ProfileDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_H248ProfileDscp_Type.__name__ = "Integer32"
_H248ProfileDscp_Object = MibTableColumn
h248ProfileDscp = _H248ProfileDscp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 7, 4, 2, 1, 10),
    _H248ProfileDscp_Type()
)
h248ProfileDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h248ProfileDscp.setStatus("current")
_H248ProfileRowStatus_Type = RowStatus
_H248ProfileRowStatus_Object = MibTableColumn
h248ProfileRowStatus = _H248ProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 7, 4, 2, 1, 11),
    _H248ProfileRowStatus_Type()
)
h248ProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h248ProfileRowStatus.setStatus("current")


class _H248ProfileVbd_Type(Integer32):
    """Custom type h248ProfileVbd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_H248ProfileVbd_Type.__name__ = "Integer32"
_H248ProfileVbd_Object = MibTableColumn
h248ProfileVbd = _H248ProfileVbd_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 7, 4, 2, 1, 12),
    _H248ProfileVbd_Type()
)
h248ProfileVbd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h248ProfileVbd.setStatus("current")


class _H248ProfileEphemeralPrefix_Type(DisplayString):
    """Custom type h248ProfileEphemeralPrefix based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_H248ProfileEphemeralPrefix_Type.__name__ = "DisplayString"
_H248ProfileEphemeralPrefix_Object = MibTableColumn
h248ProfileEphemeralPrefix = _H248ProfileEphemeralPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 7, 4, 2, 1, 14),
    _H248ProfileEphemeralPrefix_Type()
)
h248ProfileEphemeralPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h248ProfileEphemeralPrefix.setStatus("current")


class _H248ProfileSoftswitch_Type(Integer32):
    """Custom type h248ProfileSoftswitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("metaswitch", 1),
          ("nortelCs1500", 2),
          ("nortelCs2000", 3))
    )


_H248ProfileSoftswitch_Type.__name__ = "Integer32"
_H248ProfileSoftswitch_Object = MibTableColumn
h248ProfileSoftswitch = _H248ProfileSoftswitch_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 7, 4, 2, 1, 15),
    _H248ProfileSoftswitch_Type()
)
h248ProfileSoftswitch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h248ProfileSoftswitch.setStatus("current")


class _H248ProfileForceVer_Type(Integer32):
    """Custom type h248ProfileForceVer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_H248ProfileForceVer_Type.__name__ = "Integer32"
_H248ProfileForceVer_Object = MibTableColumn
h248ProfileForceVer = _H248ProfileForceVer_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 7, 4, 2, 1, 16),
    _H248ProfileForceVer_Type()
)
h248ProfileForceVer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h248ProfileForceVer.setStatus("current")


class _H248ProfileStartRTPPort_Type(Integer32):
    """Custom type h248ProfileStartRTPPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4000, 64000),
    )


_H248ProfileStartRTPPort_Type.__name__ = "Integer32"
_H248ProfileStartRTPPort_Object = MibTableColumn
h248ProfileStartRTPPort = _H248ProfileStartRTPPort_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 7, 4, 2, 1, 17),
    _H248ProfileStartRTPPort_Type()
)
h248ProfileStartRTPPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h248ProfileStartRTPPort.setStatus("current")


class _H248ProfileEndRTPPort_Type(Integer32):
    """Custom type h248ProfileEndRTPPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5000, 65000),
    )


_H248ProfileEndRTPPort_Type.__name__ = "Integer32"
_H248ProfileEndRTPPort_Object = MibTableColumn
h248ProfileEndRTPPort = _H248ProfileEndRTPPort_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 7, 4, 2, 1, 18),
    _H248ProfileEndRTPPort_Type()
)
h248ProfileEndRTPPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h248ProfileEndRTPPort.setStatus("current")
_H248ProfileEphemeralStartNumber_Type = OctetString
_H248ProfileEphemeralStartNumber_Object = MibTableColumn
h248ProfileEphemeralStartNumber = _H248ProfileEphemeralStartNumber_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 7, 4, 2, 1, 19),
    _H248ProfileEphemeralStartNumber_Type()
)
h248ProfileEphemeralStartNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h248ProfileEphemeralStartNumber.setStatus("current")


class _H248ProfileEphemeralSuffixLength_Type(Integer32):
    """Custom type h248ProfileEphemeralSuffixLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_H248ProfileEphemeralSuffixLength_Type.__name__ = "Integer32"
_H248ProfileEphemeralSuffixLength_Object = MibTableColumn
h248ProfileEphemeralSuffixLength = _H248ProfileEphemeralSuffixLength_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 7, 4, 2, 1, 20),
    _H248ProfileEphemeralSuffixLength_Type()
)
h248ProfileEphemeralSuffixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h248ProfileEphemeralSuffixLength.setStatus("current")


class _H248ProfilePhysicalPrefix_Type(DisplayString):
    """Custom type h248ProfilePhysicalPrefix based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_H248ProfilePhysicalPrefix_Type.__name__ = "DisplayString"
_H248ProfilePhysicalPrefix_Object = MibTableColumn
h248ProfilePhysicalPrefix = _H248ProfilePhysicalPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 7, 4, 2, 1, 21),
    _H248ProfilePhysicalPrefix_Type()
)
h248ProfilePhysicalPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h248ProfilePhysicalPrefix.setStatus("current")
_H248ProfilePhysicalStartNumber_Type = OctetString
_H248ProfilePhysicalStartNumber_Object = MibTableColumn
h248ProfilePhysicalStartNumber = _H248ProfilePhysicalStartNumber_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 7, 4, 2, 1, 22),
    _H248ProfilePhysicalStartNumber_Type()
)
h248ProfilePhysicalStartNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h248ProfilePhysicalStartNumber.setStatus("current")


class _H248ProfilePhysicalSuffixLength_Type(Integer32):
    """Custom type h248ProfilePhysicalSuffixLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_H248ProfilePhysicalSuffixLength_Type.__name__ = "Integer32"
_H248ProfilePhysicalSuffixLength_Object = MibTableColumn
h248ProfilePhysicalSuffixLength = _H248ProfilePhysicalSuffixLength_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 7, 4, 2, 1, 23),
    _H248ProfilePhysicalSuffixLength_Type()
)
h248ProfilePhysicalSuffixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h248ProfilePhysicalSuffixLength.setStatus("current")


class _H248ProfileRfc2833Mode_Type(Integer32):
    """Custom type h248ProfileRfc2833Mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("On", 1),
          ("Off", 2))
    )


_H248ProfileRfc2833Mode_Type.__name__ = "Integer32"
_H248ProfileRfc2833Mode_Object = MibTableColumn
h248ProfileRfc2833Mode = _H248ProfileRfc2833Mode_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 7, 4, 2, 1, 24),
    _H248ProfileRfc2833Mode_Type()
)
h248ProfileRfc2833Mode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h248ProfileRfc2833Mode.setStatus("current")


class _H248ProfileRfc2833ModePayloadType_Type(Integer32):
    """Custom type h248ProfileRfc2833ModePayloadType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(96, 127),
    )


_H248ProfileRfc2833ModePayloadType_Type.__name__ = "Integer32"
_H248ProfileRfc2833ModePayloadType_Object = MibTableColumn
h248ProfileRfc2833ModePayloadType = _H248ProfileRfc2833ModePayloadType_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 7, 4, 2, 1, 25),
    _H248ProfileRfc2833ModePayloadType_Type()
)
h248ProfileRfc2833ModePayloadType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h248ProfileRfc2833ModePayloadType.setStatus("current")
_IpqosProfile_ObjectIdentity = ObjectIdentity
ipqosProfile = _IpqosProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 8)
)
_MaxNumOfIpqosProfiles_Type = Integer32
_MaxNumOfIpqosProfiles_Object = MibScalar
maxNumOfIpqosProfiles = _MaxNumOfIpqosProfiles_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 8, 1),
    _MaxNumOfIpqosProfiles_Type()
)
maxNumOfIpqosProfiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumOfIpqosProfiles.setStatus("current")
_IpqosProfileTable_Object = MibTable
ipqosProfileTable = _IpqosProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 8, 2)
)
if mibBuilder.loadTexts:
    ipqosProfileTable.setStatus("current")
_IpqosProfileEntry_Object = MibTableRow
ipqosProfileEntry = _IpqosProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 8, 2, 1)
)
ipqosProfileEntry.setIndexNames(
    (0, "E5-121-MIB", "ipqosProfileName"),
    (0, "E5-121-MIB", "ipqosProfileNumOfQueue"),
)
if mibBuilder.loadTexts:
    ipqosProfileEntry.setStatus("current")


class _IpqosProfileName_Type(DisplayString):
    """Custom type ipqosProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_IpqosProfileName_Type.__name__ = "DisplayString"
_IpqosProfileName_Object = MibTableColumn
ipqosProfileName = _IpqosProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 8, 2, 1, 1),
    _IpqosProfileName_Type()
)
ipqosProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipqosProfileName.setStatus("current")


class _IpqosProfileNumOfQueue_Type(Integer32):
    """Custom type ipqosProfileNumOfQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_IpqosProfileNumOfQueue_Type.__name__ = "Integer32"
_IpqosProfileNumOfQueue_Object = MibTableColumn
ipqosProfileNumOfQueue = _IpqosProfileNumOfQueue_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 8, 2, 1, 2),
    _IpqosProfileNumOfQueue_Type()
)
ipqosProfileNumOfQueue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipqosProfileNumOfQueue.setStatus("current")
_IpqosProfileRowStatus_Type = RowStatus
_IpqosProfileRowStatus_Object = MibTableColumn
ipqosProfileRowStatus = _IpqosProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 8, 2, 1, 3),
    _IpqosProfileRowStatus_Type()
)
ipqosProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipqosProfileRowStatus.setStatus("current")
_IpqosProfileQueueTable_Object = MibTable
ipqosProfileQueueTable = _IpqosProfileQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 8, 3)
)
if mibBuilder.loadTexts:
    ipqosProfileQueueTable.setStatus("current")
_IpqosProfileQueueEntry_Object = MibTableRow
ipqosProfileQueueEntry = _IpqosProfileQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 8, 3, 1)
)
ipqosProfileQueueEntry.setIndexNames(
    (0, "E5-121-MIB", "ipqosProfileName"),
    (0, "E5-121-MIB", "ipqosProfileQueueIndex"),
)
if mibBuilder.loadTexts:
    ipqosProfileQueueEntry.setStatus("current")
_IpqosProfileQueueIndex_Type = Integer32
_IpqosProfileQueueIndex_Object = MibTableColumn
ipqosProfileQueueIndex = _IpqosProfileQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 8, 3, 1, 1),
    _IpqosProfileQueueIndex_Type()
)
ipqosProfileQueueIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipqosProfileQueueIndex.setStatus("current")


class _IpqosProfileQueuePIR_Type(Integer32):
    """Custom type ipqosProfileQueuePIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 131072),
    )


_IpqosProfileQueuePIR_Type.__name__ = "Integer32"
_IpqosProfileQueuePIR_Object = MibTableColumn
ipqosProfileQueuePIR = _IpqosProfileQueuePIR_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 8, 3, 1, 2),
    _IpqosProfileQueuePIR_Type()
)
ipqosProfileQueuePIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipqosProfileQueuePIR.setStatus("current")
if mibBuilder.loadTexts:
    ipqosProfileQueuePIR.setUnits("Kbps")


class _IpqosProfileQueueCIR_Type(Integer32):
    """Custom type ipqosProfileQueueCIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 65536),
    )


_IpqosProfileQueueCIR_Type.__name__ = "Integer32"
_IpqosProfileQueueCIR_Object = MibTableColumn
ipqosProfileQueueCIR = _IpqosProfileQueueCIR_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 8, 3, 1, 3),
    _IpqosProfileQueueCIR_Type()
)
ipqosProfileQueueCIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipqosProfileQueueCIR.setStatus("current")
if mibBuilder.loadTexts:
    ipqosProfileQueueCIR.setUnits("Kbps")


class _IpqosProfileQueuePBS_Type(Integer32):
    """Custom type ipqosProfileQueuePBS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3072, 65536),
    )


_IpqosProfileQueuePBS_Type.__name__ = "Integer32"
_IpqosProfileQueuePBS_Object = MibTableColumn
ipqosProfileQueuePBS = _IpqosProfileQueuePBS_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 8, 3, 1, 4),
    _IpqosProfileQueuePBS_Type()
)
ipqosProfileQueuePBS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipqosProfileQueuePBS.setStatus("current")
if mibBuilder.loadTexts:
    ipqosProfileQueuePBS.setUnits("byte")


class _IpqosProfileQueueCBS_Type(Integer32):
    """Custom type ipqosProfileQueueCBS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3072, 65536),
    )


_IpqosProfileQueueCBS_Type.__name__ = "Integer32"
_IpqosProfileQueueCBS_Object = MibTableColumn
ipqosProfileQueueCBS = _IpqosProfileQueueCBS_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 8, 3, 1, 5),
    _IpqosProfileQueueCBS_Type()
)
ipqosProfileQueueCBS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipqosProfileQueueCBS.setStatus("current")
if mibBuilder.loadTexts:
    ipqosProfileQueueCBS.setUnits("byts")


class _IpqosProfileQueueLevel_Type(Integer32):
    """Custom type ipqosProfileQueueLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_IpqosProfileQueueLevel_Type.__name__ = "Integer32"
_IpqosProfileQueueLevel_Object = MibTableColumn
ipqosProfileQueueLevel = _IpqosProfileQueueLevel_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 8, 3, 1, 6),
    _IpqosProfileQueueLevel_Type()
)
ipqosProfileQueueLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipqosProfileQueueLevel.setStatus("current")
if mibBuilder.loadTexts:
    ipqosProfileQueueLevel.setUnits("byts")


class _IpqosProfileQueueWeight_Type(Integer32):
    """Custom type ipqosProfileQueueWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_IpqosProfileQueueWeight_Type.__name__ = "Integer32"
_IpqosProfileQueueWeight_Object = MibTableColumn
ipqosProfileQueueWeight = _IpqosProfileQueueWeight_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 9, 8, 3, 1, 7),
    _IpqosProfileQueueWeight_Type()
)
ipqosProfileQueueWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipqosProfileQueueWeight.setStatus("current")
if mibBuilder.loadTexts:
    ipqosProfileQueueWeight.setUnits("byts")
_Switch_ObjectIdentity = ObjectIdentity
switch = _Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10)
)
_Dot3ad_ObjectIdentity = ObjectIdentity
dot3ad = _Dot3ad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 6)
)
_Dot3adTable_Object = MibTable
dot3adTable = _Dot3adTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 6, 1)
)
if mibBuilder.loadTexts:
    dot3adTable.setStatus("current")
_Dot3adEntry_Object = MibTableRow
dot3adEntry = _Dot3adEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 6, 1, 1)
)
dot3adEntry.setIndexNames(
    (0, "E5-121-MIB", "dot3adGroupId"),
)
if mibBuilder.loadTexts:
    dot3adEntry.setStatus("current")
_Dot3adGroupId_Type = Integer32
_Dot3adGroupId_Object = MibTableColumn
dot3adGroupId = _Dot3adGroupId_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 6, 1, 1, 1),
    _Dot3adGroupId_Type()
)
dot3adGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adGroupId.setStatus("current")


class _Dot3adEnable_Type(Integer32):
    """Custom type dot3adEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("enableWithLacp", 2),
          ("disable", 3))
    )


_Dot3adEnable_Type.__name__ = "Integer32"
_Dot3adEnable_Object = MibTableColumn
dot3adEnable = _Dot3adEnable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 6, 1, 1, 2),
    _Dot3adEnable_Type()
)
dot3adEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3adEnable.setStatus("current")


class _LacpPriority_Type(Integer32):
    """Custom type lacpPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LacpPriority_Type.__name__ = "Integer32"
_LacpPriority_Object = MibScalar
lacpPriority = _LacpPriority_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 6, 2),
    _LacpPriority_Type()
)
lacpPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lacpPriority.setStatus("current")


class _LacpTimeout_Type(Integer32):
    """Custom type lacpTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("shorttimeout", 1),
          ("longtimeout", 2))
    )


_LacpTimeout_Type.__name__ = "Integer32"
_LacpTimeout_Object = MibScalar
lacpTimeout = _LacpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 6, 3),
    _LacpTimeout_Type()
)
lacpTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lacpTimeout.setStatus("current")
_PortTrunkingTable_Object = MibTable
portTrunkingTable = _PortTrunkingTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 6, 4)
)
if mibBuilder.loadTexts:
    portTrunkingTable.setStatus("current")
_PortTrunkingEntry_Object = MibTableRow
portTrunkingEntry = _PortTrunkingEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 6, 4, 1)
)
portTrunkingEntry.setIndexNames(
    (0, "E5-121-MIB", "portTrunkingGroupId"),
)
if mibBuilder.loadTexts:
    portTrunkingEntry.setStatus("current")
_PortTrunkingGroupId_Type = Integer32
_PortTrunkingGroupId_Object = MibTableColumn
portTrunkingGroupId = _PortTrunkingGroupId_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 6, 4, 1, 1),
    _PortTrunkingGroupId_Type()
)
portTrunkingGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portTrunkingGroupId.setStatus("current")


class _PortTrunkingStatus_Type(Integer32):
    """Custom type portTrunkingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_PortTrunkingStatus_Type.__name__ = "Integer32"
_PortTrunkingStatus_Object = MibTableColumn
portTrunkingStatus = _PortTrunkingStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 6, 4, 1, 2),
    _PortTrunkingStatus_Type()
)
portTrunkingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portTrunkingStatus.setStatus("current")
_PortTrunkingPortList_Type = PortList
_PortTrunkingPortList_Object = MibTableColumn
portTrunkingPortList = _PortTrunkingPortList_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 6, 4, 1, 3),
    _PortTrunkingPortList_Type()
)
portTrunkingPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portTrunkingPortList.setStatus("current")
_Dscp_ObjectIdentity = ObjectIdentity
dscp = _Dscp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 10)
)
_DscpMappingTable_Object = MibTable
dscpMappingTable = _DscpMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 10, 1)
)
if mibBuilder.loadTexts:
    dscpMappingTable.setStatus("current")
_DscpMappingEntry_Object = MibTableRow
dscpMappingEntry = _DscpMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 10, 1, 1)
)
dscpMappingEntry.setIndexNames(
    (0, "E5-121-MIB", "dscpSrcCodePoint"),
)
if mibBuilder.loadTexts:
    dscpMappingEntry.setStatus("current")
_DscpSrcCodePoint_Type = Integer32
_DscpSrcCodePoint_Object = MibTableColumn
dscpSrcCodePoint = _DscpSrcCodePoint_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 10, 1, 1, 1),
    _DscpSrcCodePoint_Type()
)
dscpSrcCodePoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dscpSrcCodePoint.setStatus("current")


class _DscpMapPriority_Type(Integer32):
    """Custom type dscpMapPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_DscpMapPriority_Type.__name__ = "Integer32"
_DscpMapPriority_Object = MibTableColumn
dscpMapPriority = _DscpMapPriority_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 10, 1, 1, 3),
    _DscpMapPriority_Type()
)
dscpMapPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dscpMapPriority.setStatus("current")
_DscpPortTable_Object = MibTable
dscpPortTable = _DscpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 10, 2)
)
if mibBuilder.loadTexts:
    dscpPortTable.setStatus("current")
_DscpPortEntry_Object = MibTableRow
dscpPortEntry = _DscpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 10, 2, 1)
)
dscpPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dscpPortEntry.setStatus("current")


class _DscpStatusEnable_Type(Integer32):
    """Custom type dscpStatusEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_DscpStatusEnable_Type.__name__ = "Integer32"
_DscpStatusEnable_Object = MibTableColumn
dscpStatusEnable = _DscpStatusEnable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 10, 2, 1, 1),
    _DscpStatusEnable_Type()
)
dscpStatusEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dscpStatusEnable.setStatus("current")
_VlanIsolation_ObjectIdentity = ObjectIdentity
vlanIsolation = _VlanIsolation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 12)
)
_VlanIsolationTable_Object = MibTable
vlanIsolationTable = _VlanIsolationTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 12, 1)
)
if mibBuilder.loadTexts:
    vlanIsolationTable.setStatus("current")
_VlanIsolationEntry_Object = MibTableRow
vlanIsolationEntry = _VlanIsolationEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 12, 1, 1)
)
vlanIsolationEntry.setIndexNames(
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
)
if mibBuilder.loadTexts:
    vlanIsolationEntry.setStatus("current")
_VlanIsolationRowStatus_Type = RowStatus
_VlanIsolationRowStatus_Object = MibTableColumn
vlanIsolationRowStatus = _VlanIsolationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 12, 1, 1, 1),
    _VlanIsolationRowStatus_Type()
)
vlanIsolationRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanIsolationRowStatus.setStatus("current")
_EnetMtu_ObjectIdentity = ObjectIdentity
enetMtu = _EnetMtu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 13)
)
_EnetMtuEntry_Type = Integer32
_EnetMtuEntry_Object = MibScalar
enetMtuEntry = _EnetMtuEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 13, 1),
    _EnetMtuEntry_Type()
)
enetMtuEntry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enetMtuEntry.setStatus("current")
_Tpid_ObjectIdentity = ObjectIdentity
tpid = _Tpid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 14)
)
_TpidEntry_Type = Unsigned32
_TpidEntry_Object = MibScalar
tpidEntry = _TpidEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 14, 1),
    _TpidEntry_Type()
)
tpidEntry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpidEntry.setStatus("current")
_Cfm_ObjectIdentity = ObjectIdentity
cfm = _Cfm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 15)
)
_CfmLoopbackPortTable_Object = MibTable
cfmLoopbackPortTable = _CfmLoopbackPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 15, 1)
)
if mibBuilder.loadTexts:
    cfmLoopbackPortTable.setStatus("current")
_CfmLoopbackPortEntry_Object = MibTableRow
cfmLoopbackPortEntry = _CfmLoopbackPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 15, 1, 1)
)
cfmLoopbackPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cfmLoopbackPortEntry.setStatus("current")


class _CfmLoopbackPortState_Type(Integer32):
    """Custom type cfmLoopbackPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_CfmLoopbackPortState_Type.__name__ = "Integer32"
_CfmLoopbackPortState_Object = MibTableColumn
cfmLoopbackPortState = _CfmLoopbackPortState_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 15, 1, 1, 1),
    _CfmLoopbackPortState_Type()
)
cfmLoopbackPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfmLoopbackPortState.setStatus("current")
_CfmMIPTable_Object = MibTable
cfmMIPTable = _CfmMIPTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 15, 2)
)
if mibBuilder.loadTexts:
    cfmMIPTable.setStatus("current")
_CfmMIPEntry_Object = MibTableRow
cfmMIPEntry = _CfmMIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 15, 2, 1)
)
cfmMIPEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "E5-121-MIB", "cfmPort"),
)
if mibBuilder.loadTexts:
    cfmMIPEntry.setStatus("current")
_CfmPort_Type = Integer32
_CfmPort_Object = MibTableColumn
cfmPort = _CfmPort_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 15, 2, 1, 3),
    _CfmPort_Type()
)
cfmPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfmPort.setStatus("current")
_CfmMIPRowStatus_Type = RowStatus
_CfmMIPRowStatus_Object = MibTableColumn
cfmMIPRowStatus = _CfmMIPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 15, 2, 1, 4),
    _CfmMIPRowStatus_Type()
)
cfmMIPRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfmMIPRowStatus.setStatus("current")
_CfmMIPMacAddr_Type = PhysAddress
_CfmMIPMacAddr_Object = MibTableColumn
cfmMIPMacAddr = _CfmMIPMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 15, 2, 1, 5),
    _CfmMIPMacAddr_Type()
)
cfmMIPMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfmMIPMacAddr.setStatus("current")


class _CfmActionEnableStatus_Type(Integer32):
    """Custom type cfmActionEnableStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_CfmActionEnableStatus_Type.__name__ = "Integer32"
_CfmActionEnableStatus_Object = MibScalar
cfmActionEnableStatus = _CfmActionEnableStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 15, 3),
    _CfmActionEnableStatus_Type()
)
cfmActionEnableStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfmActionEnableStatus.setStatus("current")


class _CfmMode_Type(Integer32):
    """Custom type cfmMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mode802Dot1Ag", 1),
          ("modeYDot1731", 2))
    )


_CfmMode_Type.__name__ = "Integer32"
_CfmMode_Object = MibScalar
cfmMode = _CfmMode_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 15, 4),
    _CfmMode_Type()
)
cfmMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfmMode.setStatus("current")


class _CfmLbmTimeout_Type(Integer32):
    """Custom type cfmLbmTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 86400),
    )


_CfmLbmTimeout_Type.__name__ = "Integer32"
_CfmLbmTimeout_Object = MibScalar
cfmLbmTimeout = _CfmLbmTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 15, 5),
    _CfmLbmTimeout_Type()
)
cfmLbmTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfmLbmTimeout.setStatus("current")


class _CfmLbmDataTlvLength_Type(Integer32):
    """Custom type cfmLbmDataTlvLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1400),
    )


_CfmLbmDataTlvLength_Type.__name__ = "Integer32"
_CfmLbmDataTlvLength_Object = MibScalar
cfmLbmDataTlvLength = _CfmLbmDataTlvLength_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 15, 6),
    _CfmLbmDataTlvLength_Type()
)
cfmLbmDataTlvLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfmLbmDataTlvLength.setStatus("current")
_CfmLbrTable_Object = MibTable
cfmLbrTable = _CfmLbrTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 15, 7)
)
if mibBuilder.loadTexts:
    cfmLbrTable.setStatus("current")
_CfmLbrEntry_Object = MibTableRow
cfmLbrEntry = _CfmLbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 15, 7, 1)
)
cfmLbrEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "E5-121-MIB", "cfmLbmIndex"),
    (0, "E5-121-MIB", "cfmLbrIndex"),
)
if mibBuilder.loadTexts:
    cfmLbrEntry.setStatus("current")
_CfmLbmIndex_Type = Integer32
_CfmLbmIndex_Object = MibTableColumn
cfmLbmIndex = _CfmLbmIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 15, 7, 1, 1),
    _CfmLbmIndex_Type()
)
cfmLbmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmLbmIndex.setStatus("current")
_CfmLbrIndex_Type = Integer32
_CfmLbrIndex_Object = MibTableColumn
cfmLbrIndex = _CfmLbrIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 15, 7, 1, 2),
    _CfmLbrIndex_Type()
)
cfmLbrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmLbrIndex.setStatus("current")
_CfmLbrSrcMac_Type = PhysAddress
_CfmLbrSrcMac_Object = MibTableColumn
cfmLbrSrcMac = _CfmLbrSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 15, 7, 1, 3),
    _CfmLbrSrcMac_Type()
)
cfmLbrSrcMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmLbrSrcMac.setStatus("current")


class _CfmLbrStatus_Type(Integer32):
    """Custom type cfmLbrStatus based on Integer32"""
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
        *(("ready", 1),
          ("notready", 2),
          ("xmit", 3),
          ("success", 4),
          ("timeout", 5))
    )


_CfmLbrStatus_Type.__name__ = "Integer32"
_CfmLbrStatus_Object = MibTableColumn
cfmLbrStatus = _CfmLbrStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 15, 7, 1, 4),
    _CfmLbrStatus_Type()
)
cfmLbrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmLbrStatus.setStatus("current")
_CfmLbrRtt_Type = Integer32
_CfmLbrRtt_Object = MibTableColumn
cfmLbrRtt = _CfmLbrRtt_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 15, 7, 1, 5),
    _CfmLbrRtt_Type()
)
cfmLbrRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmLbrRtt.setStatus("current")
_Dhcp_ObjectIdentity = ObjectIdentity
dhcp = _Dhcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 51)
)
_DhcpRelay82Table_Object = MibTable
dhcpRelay82Table = _DhcpRelay82Table_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 51, 2)
)
if mibBuilder.loadTexts:
    dhcpRelay82Table.setStatus("current")
_DhcpRelay82Entry_Object = MibTableRow
dhcpRelay82Entry = _DhcpRelay82Entry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 51, 2, 1)
)
dhcpRelay82Entry.setIndexNames(
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
)
if mibBuilder.loadTexts:
    dhcpRelay82Entry.setStatus("current")
_DhcpRelay82PrimaryServer_Type = IpAddress
_DhcpRelay82PrimaryServer_Object = MibTableColumn
dhcpRelay82PrimaryServer = _DhcpRelay82PrimaryServer_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 51, 2, 1, 1),
    _DhcpRelay82PrimaryServer_Type()
)
dhcpRelay82PrimaryServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelay82PrimaryServer.setStatus("current")
_DhcpRelay82SecondaryServer_Type = IpAddress
_DhcpRelay82SecondaryServer_Object = MibTableColumn
dhcpRelay82SecondaryServer = _DhcpRelay82SecondaryServer_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 51, 2, 1, 2),
    _DhcpRelay82SecondaryServer_Type()
)
dhcpRelay82SecondaryServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelay82SecondaryServer.setStatus("current")


class _DhcpRelay82ActiveServer_Type(Integer32):
    """Custom type dhcpRelay82ActiveServer based on Integer32"""
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
        *(("primary", 1),
          ("secondary", 2),
          ("third", 3),
          ("fourth", 4),
          ("fifth", 5))
    )


_DhcpRelay82ActiveServer_Type.__name__ = "Integer32"
_DhcpRelay82ActiveServer_Object = MibTableColumn
dhcpRelay82ActiveServer = _DhcpRelay82ActiveServer_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 51, 2, 1, 3),
    _DhcpRelay82ActiveServer_Type()
)
dhcpRelay82ActiveServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRelay82ActiveServer.setStatus("current")


class _DhcpRelay82Enable_Type(Integer32):
    """Custom type dhcpRelay82Enable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_DhcpRelay82Enable_Type.__name__ = "Integer32"
_DhcpRelay82Enable_Object = MibTableColumn
dhcpRelay82Enable = _DhcpRelay82Enable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 51, 2, 1, 4),
    _DhcpRelay82Enable_Type()
)
dhcpRelay82Enable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpRelay82Enable.setStatus("current")


class _DhcpRelay82Info_Type(DisplayString):
    """Custom type dhcpRelay82Info based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 23),
    )


_DhcpRelay82Info_Type.__name__ = "DisplayString"
_DhcpRelay82Info_Object = MibTableColumn
dhcpRelay82Info = _DhcpRelay82Info_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 51, 2, 1, 5),
    _DhcpRelay82Info_Type()
)
dhcpRelay82Info.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpRelay82Info.setStatus("current")


class _DhcpRelay82RelayMode_Type(Integer32):
    """Custom type dhcpRelay82RelayMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("all", 2))
    )


_DhcpRelay82RelayMode_Type.__name__ = "Integer32"
_DhcpRelay82RelayMode_Object = MibTableColumn
dhcpRelay82RelayMode = _DhcpRelay82RelayMode_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 51, 2, 1, 6),
    _DhcpRelay82RelayMode_Type()
)
dhcpRelay82RelayMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpRelay82RelayMode.setStatus("current")


class _DhcpRelay82Suboption2Enable_Type(Integer32):
    """Custom type dhcpRelay82Suboption2Enable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_DhcpRelay82Suboption2Enable_Type.__name__ = "Integer32"
_DhcpRelay82Suboption2Enable_Object = MibTableColumn
dhcpRelay82Suboption2Enable = _DhcpRelay82Suboption2Enable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 51, 2, 1, 8),
    _DhcpRelay82Suboption2Enable_Type()
)
dhcpRelay82Suboption2Enable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpRelay82Suboption2Enable.setStatus("current")
_DhcpRelay82Suboption2Info_Type = DisplayString
_DhcpRelay82Suboption2Info_Object = MibTableColumn
dhcpRelay82Suboption2Info = _DhcpRelay82Suboption2Info_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 51, 2, 1, 9),
    _DhcpRelay82Suboption2Info_Type()
)
dhcpRelay82Suboption2Info.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpRelay82Suboption2Info.setStatus("current")


class _DhcpRelay82EntryEnable_Type(Integer32):
    """Custom type dhcpRelay82EntryEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("all", 2),
          ("disable", 3))
    )


_DhcpRelay82EntryEnable_Type.__name__ = "Integer32"
_DhcpRelay82EntryEnable_Object = MibTableColumn
dhcpRelay82EntryEnable = _DhcpRelay82EntryEnable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 51, 2, 1, 10),
    _DhcpRelay82EntryEnable_Type()
)
dhcpRelay82EntryEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpRelay82EntryEnable.setStatus("current")


class _DhcpRelay82EntryOptionMode_Type(Integer32):
    """Custom type dhcpRelay82EntryOptionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("private", 1),
          ("tr101", 2),
          ("customer-remote-id", 3))
    )


_DhcpRelay82EntryOptionMode_Type.__name__ = "Integer32"
_DhcpRelay82EntryOptionMode_Object = MibTableColumn
dhcpRelay82EntryOptionMode = _DhcpRelay82EntryOptionMode_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 51, 2, 1, 11),
    _DhcpRelay82EntryOptionMode_Type()
)
dhcpRelay82EntryOptionMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpRelay82EntryOptionMode.setStatus("current")
_DhcpRelay82VlanIp_Type = IpAddress
_DhcpRelay82VlanIp_Object = MibTableColumn
dhcpRelay82VlanIp = _DhcpRelay82VlanIp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 51, 2, 1, 12),
    _DhcpRelay82VlanIp_Type()
)
dhcpRelay82VlanIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelay82VlanIp.setStatus("current")
_DhcpRelay82VlanMask_Type = Integer32
_DhcpRelay82VlanMask_Object = MibTableColumn
dhcpRelay82VlanMask = _DhcpRelay82VlanMask_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 51, 2, 1, 13),
    _DhcpRelay82VlanMask_Type()
)
dhcpRelay82VlanMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelay82VlanMask.setStatus("current")
_DhcpRelay82VlanGateway_Type = IpAddress
_DhcpRelay82VlanGateway_Object = MibTableColumn
dhcpRelay82VlanGateway = _DhcpRelay82VlanGateway_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 51, 2, 1, 14),
    _DhcpRelay82VlanGateway_Type()
)
dhcpRelay82VlanGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelay82VlanGateway.setStatus("current")
_DhcpRelay82ThirdServer_Type = IpAddress
_DhcpRelay82ThirdServer_Object = MibTableColumn
dhcpRelay82ThirdServer = _DhcpRelay82ThirdServer_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 51, 2, 1, 15),
    _DhcpRelay82ThirdServer_Type()
)
dhcpRelay82ThirdServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelay82ThirdServer.setStatus("current")
_DhcpRelay82FourthServer_Type = IpAddress
_DhcpRelay82FourthServer_Object = MibTableColumn
dhcpRelay82FourthServer = _DhcpRelay82FourthServer_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 51, 2, 1, 16),
    _DhcpRelay82FourthServer_Type()
)
dhcpRelay82FourthServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelay82FourthServer.setStatus("current")
_DhcpRelay82FifthServer_Type = IpAddress
_DhcpRelay82FifthServer_Object = MibTableColumn
dhcpRelay82FifthServer = _DhcpRelay82FifthServer_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 51, 2, 1, 17),
    _DhcpRelay82FifthServer_Type()
)
dhcpRelay82FifthServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelay82FifthServer.setStatus("current")
_DhcpRelay82ServerVid_Type = Integer32
_DhcpRelay82ServerVid_Object = MibTableColumn
dhcpRelay82ServerVid = _DhcpRelay82ServerVid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 51, 2, 1, 18),
    _DhcpRelay82ServerVid_Type()
)
dhcpRelay82ServerVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelay82ServerVid.setStatus("current")
_DhcpRelayTest_ObjectIdentity = ObjectIdentity
dhcpRelayTest = _DhcpRelayTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 51, 8)
)
_DhcpRelayTestVid_Type = Integer32
_DhcpRelayTestVid_Object = MibScalar
dhcpRelayTestVid = _DhcpRelayTestVid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 51, 8, 1),
    _DhcpRelayTestVid_Type()
)
dhcpRelayTestVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelayTestVid.setStatus("current")
_DhcpRelayTestIp_Type = IpAddress
_DhcpRelayTestIp_Object = MibScalar
dhcpRelayTestIp = _DhcpRelayTestIp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 51, 8, 2),
    _DhcpRelayTestIp_Type()
)
dhcpRelayTestIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelayTestIp.setStatus("current")
_DhcpRelayTestOps_Type = Integer32
_DhcpRelayTestOps_Object = MibScalar
dhcpRelayTestOps = _DhcpRelayTestOps_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 51, 8, 3),
    _DhcpRelayTestOps_Type()
)
dhcpRelayTestOps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelayTestOps.setStatus("current")
_DhcpRelayTestStatus_Type = DisplayString
_DhcpRelayTestStatus_Object = MibScalar
dhcpRelayTestStatus = _DhcpRelayTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 51, 8, 4),
    _DhcpRelayTestStatus_Type()
)
dhcpRelayTestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRelayTestStatus.setStatus("current")
_DhcpRelayArp_ObjectIdentity = ObjectIdentity
dhcpRelayArp = _DhcpRelayArp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 51, 9)
)
_DhcpRelayArpShowTable_Object = MibTable
dhcpRelayArpShowTable = _DhcpRelayArpShowTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 51, 9, 1)
)
if mibBuilder.loadTexts:
    dhcpRelayArpShowTable.setStatus("current")
_DhcpRelayArpShowEntry_Object = MibTableRow
dhcpRelayArpShowEntry = _DhcpRelayArpShowEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 51, 9, 1, 1)
)
dhcpRelayArpShowEntry.setIndexNames(
    (0, "E5-121-MIB", "dhcpRelayArpShowVid"),
    (0, "E5-121-MIB", "dhcpRelayArpShowIp"),
)
if mibBuilder.loadTexts:
    dhcpRelayArpShowEntry.setStatus("current")
_DhcpRelayArpShowVid_Type = Integer32
_DhcpRelayArpShowVid_Object = MibTableColumn
dhcpRelayArpShowVid = _DhcpRelayArpShowVid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 51, 9, 1, 1, 1),
    _DhcpRelayArpShowVid_Type()
)
dhcpRelayArpShowVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRelayArpShowVid.setStatus("current")
_DhcpRelayArpShowIp_Type = IpAddress
_DhcpRelayArpShowIp_Object = MibTableColumn
dhcpRelayArpShowIp = _DhcpRelayArpShowIp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 51, 9, 1, 1, 2),
    _DhcpRelayArpShowIp_Type()
)
dhcpRelayArpShowIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRelayArpShowIp.setStatus("current")
_DhcpRelayArpShowMac_Type = PhysAddress
_DhcpRelayArpShowMac_Object = MibTableColumn
dhcpRelayArpShowMac = _DhcpRelayArpShowMac_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 51, 9, 1, 1, 3),
    _DhcpRelayArpShowMac_Type()
)
dhcpRelayArpShowMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRelayArpShowMac.setStatus("current")
_DhcpRelayArpFlushOps_Type = Integer32
_DhcpRelayArpFlushOps_Object = MibScalar
dhcpRelayArpFlushOps = _DhcpRelayArpFlushOps_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 51, 9, 2),
    _DhcpRelayArpFlushOps_Type()
)
dhcpRelayArpFlushOps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelayArpFlushOps.setStatus("current")
_Macfilter_ObjectIdentity = ObjectIdentity
macfilter = _Macfilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 53)
)
_MacFilterPortTable_Object = MibTable
macFilterPortTable = _MacFilterPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 53, 1)
)
if mibBuilder.loadTexts:
    macFilterPortTable.setStatus("current")
_MacFilterPortEntry_Object = MibTableRow
macFilterPortEntry = _MacFilterPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 53, 1, 1)
)
macFilterPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    macFilterPortEntry.setStatus("current")


class _MacFilterPortEnable_Type(Integer32):
    """Custom type macFilterPortEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("enableMacFilter", 1),
          ("enableMacCount", 2),
          ("disable", 4),
          ("enableMacFilterAndMacCount", 5))
    )


_MacFilterPortEnable_Type.__name__ = "Integer32"
_MacFilterPortEnable_Object = MibTableColumn
macFilterPortEnable = _MacFilterPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 53, 1, 1, 1),
    _MacFilterPortEnable_Type()
)
macFilterPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macFilterPortEnable.setStatus("current")


class _MacFilterPortMacCount_Type(Integer32):
    """Custom type macFilterPortMacCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_MacFilterPortMacCount_Type.__name__ = "Integer32"
_MacFilterPortMacCount_Object = MibTableColumn
macFilterPortMacCount = _MacFilterPortMacCount_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 53, 1, 1, 2),
    _MacFilterPortMacCount_Type()
)
macFilterPortMacCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macFilterPortMacCount.setStatus("current")


class _MacFilterPortFilterMode_Type(Integer32):
    """Custom type macFilterPortFilterMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("deny", 2))
    )


_MacFilterPortFilterMode_Type.__name__ = "Integer32"
_MacFilterPortFilterMode_Object = MibTableColumn
macFilterPortFilterMode = _MacFilterPortFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 53, 1, 1, 3),
    _MacFilterPortFilterMode_Type()
)
macFilterPortFilterMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macFilterPortFilterMode.setStatus("current")
_MaxNumOfMacFiltersInSystem_Type = Integer32
_MaxNumOfMacFiltersInSystem_Object = MibScalar
maxNumOfMacFiltersInSystem = _MaxNumOfMacFiltersInSystem_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 53, 2),
    _MaxNumOfMacFiltersInSystem_Type()
)
maxNumOfMacFiltersInSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumOfMacFiltersInSystem.setStatus("current")
_MaxNumOfMacFiltersPerPort_Type = Integer32
_MaxNumOfMacFiltersPerPort_Object = MibScalar
maxNumOfMacFiltersPerPort = _MaxNumOfMacFiltersPerPort_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 53, 3),
    _MaxNumOfMacFiltersPerPort_Type()
)
maxNumOfMacFiltersPerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumOfMacFiltersPerPort.setStatus("current")
_CurrNumOfMacFiltersInSystem_Type = Integer32
_CurrNumOfMacFiltersInSystem_Object = MibScalar
currNumOfMacFiltersInSystem = _CurrNumOfMacFiltersInSystem_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 53, 4),
    _CurrNumOfMacFiltersInSystem_Type()
)
currNumOfMacFiltersInSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currNumOfMacFiltersInSystem.setStatus("current")
_MacFilterTable_Object = MibTable
macFilterTable = _MacFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 53, 5)
)
if mibBuilder.loadTexts:
    macFilterTable.setStatus("current")
_MacFilterEntry_Object = MibTableRow
macFilterEntry = _MacFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 53, 5, 1)
)
macFilterEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "E5-121-MIB", "macFilterAddr"),
)
if mibBuilder.loadTexts:
    macFilterEntry.setStatus("current")
_MacFilterAddr_Type = PhysAddress
_MacFilterAddr_Object = MibTableColumn
macFilterAddr = _MacFilterAddr_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 53, 5, 1, 1),
    _MacFilterAddr_Type()
)
macFilterAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macFilterAddr.setStatus("current")
_MacFilterRowStatus_Type = RowStatus
_MacFilterRowStatus_Object = MibTableColumn
macFilterRowStatus = _MacFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 53, 5, 1, 2),
    _MacFilterRowStatus_Type()
)
macFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    macFilterRowStatus.setStatus("current")
_MacfilterBatchSet_ObjectIdentity = ObjectIdentity
macfilterBatchSet = _MacfilterBatchSet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 53, 6)
)
_MacfilterTarget_Type = OctetString
_MacfilterTarget_Object = MibScalar
macfilterTarget = _MacfilterTarget_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 53, 6, 1),
    _MacfilterTarget_Type()
)
macfilterTarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macfilterTarget.setStatus("current")
_MacfilterOps_Type = Integer32
_MacfilterOps_Object = MibScalar
macfilterOps = _MacfilterOps_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 53, 6, 2),
    _MacfilterOps_Type()
)
macfilterOps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macfilterOps.setStatus("current")


class _MacFilterMacCountForBatchSet_Type(Integer32):
    """Custom type macFilterMacCountForBatchSet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_MacFilterMacCountForBatchSet_Type.__name__ = "Integer32"
_MacFilterMacCountForBatchSet_Object = MibScalar
macFilterMacCountForBatchSet = _MacFilterMacCountForBatchSet_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 53, 6, 3),
    _MacFilterMacCountForBatchSet_Type()
)
macFilterMacCountForBatchSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macFilterMacCountForBatchSet.setStatus("current")
_OuiFilterTable_Object = MibTable
ouiFilterTable = _OuiFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 53, 7)
)
if mibBuilder.loadTexts:
    ouiFilterTable.setStatus("current")
_OuiFilterEntry_Object = MibTableRow
ouiFilterEntry = _OuiFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 53, 7, 1)
)
ouiFilterEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "E5-121-MIB", "ouiFilterAddr"),
)
if mibBuilder.loadTexts:
    ouiFilterEntry.setStatus("current")
_OuiFilterAddr_Type = OctetString
_OuiFilterAddr_Object = MibTableColumn
ouiFilterAddr = _OuiFilterAddr_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 53, 7, 1, 1),
    _OuiFilterAddr_Type()
)
ouiFilterAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ouiFilterAddr.setStatus("current")
_OuiFilterRowStatus_Type = RowStatus
_OuiFilterRowStatus_Object = MibTableColumn
ouiFilterRowStatus = _OuiFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 53, 7, 1, 2),
    _OuiFilterRowStatus_Type()
)
ouiFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ouiFilterRowStatus.setStatus("current")
_MaxNumOfOuiFiltersPerPort_Type = Integer32
_MaxNumOfOuiFiltersPerPort_Object = MibScalar
maxNumOfOuiFiltersPerPort = _MaxNumOfOuiFiltersPerPort_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 53, 8),
    _MaxNumOfOuiFiltersPerPort_Type()
)
maxNumOfOuiFiltersPerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumOfOuiFiltersPerPort.setStatus("current")
_OuiFilterPortTable_Object = MibTable
ouiFilterPortTable = _OuiFilterPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 53, 9)
)
if mibBuilder.loadTexts:
    ouiFilterPortTable.setStatus("current")
_OuiFilterPortEntry_Object = MibTableRow
ouiFilterPortEntry = _OuiFilterPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 53, 9, 1)
)
ouiFilterPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ouiFilterPortEntry.setStatus("current")


class _OuiFilterPortEnable_Type(Integer32):
    """Custom type ouiFilterPortEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enableOuiFilter", 1),
          ("disable", 2))
    )


_OuiFilterPortEnable_Type.__name__ = "Integer32"
_OuiFilterPortEnable_Object = MibTableColumn
ouiFilterPortEnable = _OuiFilterPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 53, 9, 1, 1),
    _OuiFilterPortEnable_Type()
)
ouiFilterPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ouiFilterPortEnable.setStatus("current")


class _OuiFilterPortFilterMode_Type(Integer32):
    """Custom type ouiFilterPortFilterMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("deny", 2))
    )


_OuiFilterPortFilterMode_Type.__name__ = "Integer32"
_OuiFilterPortFilterMode_Object = MibTableColumn
ouiFilterPortFilterMode = _OuiFilterPortFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 53, 9, 1, 2),
    _OuiFilterPortFilterMode_Type()
)
ouiFilterPortFilterMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ouiFilterPortFilterMode.setStatus("current")
_DhcpSnoop_ObjectIdentity = ObjectIdentity
dhcpSnoop = _DhcpSnoop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 55)
)
_DhcpSnoopPortTable_Object = MibTable
dhcpSnoopPortTable = _DhcpSnoopPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 55, 1)
)
if mibBuilder.loadTexts:
    dhcpSnoopPortTable.setStatus("current")
_DhcpSnoopPortEntry_Object = MibTableRow
dhcpSnoopPortEntry = _DhcpSnoopPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 55, 1, 1)
)
dhcpSnoopPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dhcpSnoopPortEntry.setStatus("current")


class _DhcpSnoopEnable_Type(Integer32):
    """Custom type dhcpSnoopEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_DhcpSnoopEnable_Type.__name__ = "Integer32"
_DhcpSnoopEnable_Object = MibTableColumn
dhcpSnoopEnable = _DhcpSnoopEnable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 55, 1, 1, 1),
    _DhcpSnoopEnable_Type()
)
dhcpSnoopEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnoopEnable.setStatus("current")
_DhcpSnoopMaxcnt_Type = Integer32
_DhcpSnoopMaxcnt_Object = MibTableColumn
dhcpSnoopMaxcnt = _DhcpSnoopMaxcnt_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 55, 1, 1, 2),
    _DhcpSnoopMaxcnt_Type()
)
dhcpSnoopMaxcnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnoopMaxcnt.setStatus("current")


class _DhcpSnoopSmacverifyEnable_Type(Integer32):
    """Custom type dhcpSnoopSmacverifyEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_DhcpSnoopSmacverifyEnable_Type.__name__ = "Integer32"
_DhcpSnoopSmacverifyEnable_Object = MibTableColumn
dhcpSnoopSmacverifyEnable = _DhcpSnoopSmacverifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 55, 1, 1, 3),
    _DhcpSnoopSmacverifyEnable_Type()
)
dhcpSnoopSmacverifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnoopSmacverifyEnable.setStatus("current")
_DhcpSnoopTarget_Type = OctetString
_DhcpSnoopTarget_Object = MibScalar
dhcpSnoopTarget = _DhcpSnoopTarget_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 55, 2),
    _DhcpSnoopTarget_Type()
)
dhcpSnoopTarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnoopTarget.setStatus("current")
_DhcpSnoopOps_Type = Integer32
_DhcpSnoopOps_Object = MibScalar
dhcpSnoopOps = _DhcpSnoopOps_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 55, 3),
    _DhcpSnoopOps_Type()
)
dhcpSnoopOps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnoopOps.setStatus("current")
_DhcpStaticTable_Object = MibTable
dhcpStaticTable = _DhcpStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 55, 4)
)
if mibBuilder.loadTexts:
    dhcpStaticTable.setStatus("current")
_DhcpStaticEntry_Object = MibTableRow
dhcpStaticEntry = _DhcpStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 55, 4, 1)
)
dhcpStaticEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "E5-121-MIB", "dhcpStaticIpAddr"),
)
if mibBuilder.loadTexts:
    dhcpStaticEntry.setStatus("current")
_DhcpStaticIpAddr_Type = IpAddress
_DhcpStaticIpAddr_Object = MibTableColumn
dhcpStaticIpAddr = _DhcpStaticIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 55, 4, 1, 1),
    _DhcpStaticIpAddr_Type()
)
dhcpStaticIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpStaticIpAddr.setStatus("current")
_DhcpStaticRowStatus_Type = RowStatus
_DhcpStaticRowStatus_Object = MibTableColumn
dhcpStaticRowStatus = _DhcpStaticRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 55, 4, 1, 2),
    _DhcpStaticRowStatus_Type()
)
dhcpStaticRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpStaticRowStatus.setStatus("current")
_MaxNumOfDhcpStaticIp_Type = Integer32
_MaxNumOfDhcpStaticIp_Object = MibScalar
maxNumOfDhcpStaticIp = _MaxNumOfDhcpStaticIp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 55, 5),
    _MaxNumOfDhcpStaticIp_Type()
)
maxNumOfDhcpStaticIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumOfDhcpStaticIp.setStatus("current")


class _DhcpSnoopMaxcntMode_Type(Integer32):
    """Custom type dhcpSnoopMaxcntMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("replace", 1),
          ("drop", 2))
    )


_DhcpSnoopMaxcntMode_Type.__name__ = "Integer32"
_DhcpSnoopMaxcntMode_Object = MibScalar
dhcpSnoopMaxcntMode = _DhcpSnoopMaxcntMode_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 55, 6),
    _DhcpSnoopMaxcntMode_Type()
)
dhcpSnoopMaxcntMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnoopMaxcntMode.setStatus("current")
_Acl_ObjectIdentity = ObjectIdentity
acl = _Acl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 56)
)
_AclSetTable_Object = MibTable
aclSetTable = _AclSetTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 56, 1)
)
if mibBuilder.loadTexts:
    aclSetTable.setStatus("current")
_AclSetEntry_Object = MibTableRow
aclSetEntry = _AclSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 56, 1, 1)
)
aclSetEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "E5-121-MIB", "aclSetVpi"),
    (0, "E5-121-MIB", "aclSetVci"),
    (0, "E5-121-MIB", "aclSetProfileName"),
)
if mibBuilder.loadTexts:
    aclSetEntry.setStatus("current")
_AclSetVpi_Type = Integer32
_AclSetVpi_Object = MibTableColumn
aclSetVpi = _AclSetVpi_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 56, 1, 1, 1),
    _AclSetVpi_Type()
)
aclSetVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclSetVpi.setStatus("current")
_AclSetVci_Type = Integer32
_AclSetVci_Object = MibTableColumn
aclSetVci = _AclSetVci_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 56, 1, 1, 2),
    _AclSetVci_Type()
)
aclSetVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclSetVci.setStatus("current")
_AclSetProfileName_Type = DisplayString
_AclSetProfileName_Object = MibTableColumn
aclSetProfileName = _AclSetProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 56, 1, 1, 3),
    _AclSetProfileName_Type()
)
aclSetProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclSetProfileName.setStatus("current")
_AclSetRowStatus_Type = RowStatus
_AclSetRowStatus_Object = MibTableColumn
aclSetRowStatus = _AclSetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 56, 1, 1, 4),
    _AclSetRowStatus_Type()
)
aclSetRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclSetRowStatus.setStatus("current")
_AclProfileTable_Object = MibTable
aclProfileTable = _AclProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 56, 2)
)
if mibBuilder.loadTexts:
    aclProfileTable.setStatus("current")
_AclProfileEntry_Object = MibTableRow
aclProfileEntry = _AclProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 56, 2, 1)
)
aclProfileEntry.setIndexNames(
    (0, "E5-121-MIB", "aclProfileRuleName"),
)
if mibBuilder.loadTexts:
    aclProfileEntry.setStatus("current")
_AclProfileRuleName_Type = DisplayString
_AclProfileRuleName_Object = MibTableColumn
aclProfileRuleName = _AclProfileRuleName_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 56, 2, 1, 1),
    _AclProfileRuleName_Type()
)
aclProfileRuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclProfileRuleName.setStatus("current")
_AclProfileRuleNumber_Type = Integer32
_AclProfileRuleNumber_Object = MibTableColumn
aclProfileRuleNumber = _AclProfileRuleNumber_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 56, 2, 1, 2),
    _AclProfileRuleNumber_Type()
)
aclProfileRuleNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileRuleNumber.setStatus("current")
_AclProfileActionNumber_Type = Integer32
_AclProfileActionNumber_Object = MibTableColumn
aclProfileActionNumber = _AclProfileActionNumber_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 56, 2, 1, 3),
    _AclProfileActionNumber_Type()
)
aclProfileActionNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileActionNumber.setStatus("current")
_AclProfileRuleParamMask_Type = Integer32
_AclProfileRuleParamMask_Object = MibTableColumn
aclProfileRuleParamMask = _AclProfileRuleParamMask_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 56, 2, 1, 4),
    _AclProfileRuleParamMask_Type()
)
aclProfileRuleParamMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileRuleParamMask.setStatus("current")


class _AclProfileRuleEtype_Type(Integer32):
    """Custom type aclProfileRuleEtype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AclProfileRuleEtype_Type.__name__ = "Integer32"
_AclProfileRuleEtype_Object = MibTableColumn
aclProfileRuleEtype = _AclProfileRuleEtype_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 56, 2, 1, 5),
    _AclProfileRuleEtype_Type()
)
aclProfileRuleEtype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileRuleEtype.setStatus("current")


class _AclProfileRuleVid_Type(Integer32):
    """Custom type aclProfileRuleVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AclProfileRuleVid_Type.__name__ = "Integer32"
_AclProfileRuleVid_Object = MibTableColumn
aclProfileRuleVid = _AclProfileRuleVid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 56, 2, 1, 6),
    _AclProfileRuleVid_Type()
)
aclProfileRuleVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileRuleVid.setStatus("current")
_AclProfileRuleSmac_Type = PhysAddress
_AclProfileRuleSmac_Object = MibTableColumn
aclProfileRuleSmac = _AclProfileRuleSmac_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 56, 2, 1, 7),
    _AclProfileRuleSmac_Type()
)
aclProfileRuleSmac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileRuleSmac.setStatus("current")
_AclProfileRuleDmac_Type = PhysAddress
_AclProfileRuleDmac_Object = MibTableColumn
aclProfileRuleDmac = _AclProfileRuleDmac_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 56, 2, 1, 8),
    _AclProfileRuleDmac_Type()
)
aclProfileRuleDmac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileRuleDmac.setStatus("current")


class _AclProfileRulePriority_Type(Integer32):
    """Custom type aclProfileRulePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AclProfileRulePriority_Type.__name__ = "Integer32"
_AclProfileRulePriority_Object = MibTableColumn
aclProfileRulePriority = _AclProfileRulePriority_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 56, 2, 1, 9),
    _AclProfileRulePriority_Type()
)
aclProfileRulePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileRulePriority.setStatus("current")


class _AclProfileRuleProtocol_Type(Integer32):
    """Custom type aclProfileRuleProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AclProfileRuleProtocol_Type.__name__ = "Integer32"
_AclProfileRuleProtocol_Object = MibTableColumn
aclProfileRuleProtocol = _AclProfileRuleProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 56, 2, 1, 10),
    _AclProfileRuleProtocol_Type()
)
aclProfileRuleProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileRuleProtocol.setStatus("current")


class _AclProfileActionRate_Type(Integer32):
    """Custom type aclProfileActionRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 65472),
    )


_AclProfileActionRate_Type.__name__ = "Integer32"
_AclProfileActionRate_Object = MibTableColumn
aclProfileActionRate = _AclProfileActionRate_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 56, 2, 1, 21),
    _AclProfileActionRate_Type()
)
aclProfileActionRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileActionRate.setStatus("current")


class _AclProfileActionrvlan_Type(Integer32):
    """Custom type aclProfileActionrvlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AclProfileActionrvlan_Type.__name__ = "Integer32"
_AclProfileActionrvlan_Object = MibTableColumn
aclProfileActionrvlan = _AclProfileActionrvlan_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 56, 2, 1, 22),
    _AclProfileActionrvlan_Type()
)
aclProfileActionrvlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileActionrvlan.setStatus("current")


class _AclProfileActionrpri_Type(Integer32):
    """Custom type aclProfileActionrpri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AclProfileActionrpri_Type.__name__ = "Integer32"
_AclProfileActionrpri_Object = MibTableColumn
aclProfileActionrpri = _AclProfileActionrpri_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 56, 2, 1, 23),
    _AclProfileActionrpri_Type()
)
aclProfileActionrpri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileActionrpri.setStatus("current")
_AclProfileRowStatus_Type = RowStatus
_AclProfileRowStatus_Object = MibTableColumn
aclProfileRowStatus = _AclProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 56, 2, 1, 24),
    _AclProfileRowStatus_Type()
)
aclProfileRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileRowStatus.setStatus("current")
_AclProfileRuleSip_Type = IpAddress
_AclProfileRuleSip_Object = MibTableColumn
aclProfileRuleSip = _AclProfileRuleSip_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 56, 2, 1, 25),
    _AclProfileRuleSip_Type()
)
aclProfileRuleSip.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclProfileRuleSip.setStatus("current")
_AclProfileRuleDip_Type = IpAddress
_AclProfileRuleDip_Object = MibTableColumn
aclProfileRuleDip = _AclProfileRuleDip_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 56, 2, 1, 26),
    _AclProfileRuleDip_Type()
)
aclProfileRuleDip.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclProfileRuleDip.setStatus("current")


class _AclProfileRuleSport_Type(Integer32):
    """Custom type aclProfileRuleSport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AclProfileRuleSport_Type.__name__ = "Integer32"
_AclProfileRuleSport_Object = MibTableColumn
aclProfileRuleSport = _AclProfileRuleSport_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 56, 2, 1, 27),
    _AclProfileRuleSport_Type()
)
aclProfileRuleSport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclProfileRuleSport.setStatus("current")


class _AclProfileRuleDport_Type(Integer32):
    """Custom type aclProfileRuleDport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AclProfileRuleDport_Type.__name__ = "Integer32"
_AclProfileRuleDport_Object = MibTableColumn
aclProfileRuleDport = _AclProfileRuleDport_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 56, 2, 1, 28),
    _AclProfileRuleDport_Type()
)
aclProfileRuleDport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclProfileRuleDport.setStatus("current")
_PppoeAgent_ObjectIdentity = ObjectIdentity
pppoeAgent = _PppoeAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 57)
)
_PppoeAgentTable_Object = MibTable
pppoeAgentTable = _PppoeAgentTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 57, 1)
)
if mibBuilder.loadTexts:
    pppoeAgentTable.setStatus("current")
_PppoeAgentEntry_Object = MibTableRow
pppoeAgentEntry = _PppoeAgentEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 57, 1, 1)
)
pppoeAgentEntry.setIndexNames(
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
)
if mibBuilder.loadTexts:
    pppoeAgentEntry.setStatus("current")


class _PppoeAgentEnable_Type(Integer32):
    """Custom type pppoeAgentEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_PppoeAgentEnable_Type.__name__ = "Integer32"
_PppoeAgentEnable_Object = MibTableColumn
pppoeAgentEnable = _PppoeAgentEnable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 57, 1, 1, 1),
    _PppoeAgentEnable_Type()
)
pppoeAgentEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pppoeAgentEnable.setStatus("current")


class _PppoeAgentInfo_Type(DisplayString):
    """Custom type pppoeAgentInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 23),
    )


_PppoeAgentInfo_Type.__name__ = "DisplayString"
_PppoeAgentInfo_Object = MibTableColumn
pppoeAgentInfo = _PppoeAgentInfo_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 57, 1, 1, 2),
    _PppoeAgentInfo_Type()
)
pppoeAgentInfo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pppoeAgentInfo.setStatus("current")
_PppoeAgentRowStatus_Type = RowStatus
_PppoeAgentRowStatus_Object = MibTableColumn
pppoeAgentRowStatus = _PppoeAgentRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 57, 1, 1, 3),
    _PppoeAgentRowStatus_Type()
)
pppoeAgentRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pppoeAgentRowStatus.setStatus("current")


class _PppoeAgentOptionMode_Type(Integer32):
    """Custom type pppoeAgentOptionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("private", 1),
          ("tr101", 2))
    )


_PppoeAgentOptionMode_Type.__name__ = "Integer32"
_PppoeAgentOptionMode_Object = MibTableColumn
pppoeAgentOptionMode = _PppoeAgentOptionMode_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 57, 1, 1, 4),
    _PppoeAgentOptionMode_Type()
)
pppoeAgentOptionMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pppoeAgentOptionMode.setStatus("current")
_MaxNumOfPppoeAgentConf_Type = Integer32
_MaxNumOfPppoeAgentConf_Object = MibScalar
maxNumOfPppoeAgentConf = _MaxNumOfPppoeAgentConf_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 57, 2),
    _MaxNumOfPppoeAgentConf_Type()
)
maxNumOfPppoeAgentConf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumOfPppoeAgentConf.setStatus("current")
_N1mac_ObjectIdentity = ObjectIdentity
n1mac = _N1mac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 58)
)
_N1macReplaceMac_Type = MacAddress
_N1macReplaceMac_Object = MibScalar
n1macReplaceMac = _N1macReplaceMac_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 58, 1),
    _N1macReplaceMac_Type()
)
n1macReplaceMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    n1macReplaceMac.setStatus("current")
_N1macPortTable_Object = MibTable
n1macPortTable = _N1macPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 58, 2)
)
if mibBuilder.loadTexts:
    n1macPortTable.setStatus("current")
_N1macPortEntry_Object = MibTableRow
n1macPortEntry = _N1macPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 58, 2, 1)
)
n1macPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    n1macPortEntry.setStatus("current")


class _N1macStatusEnable_Type(Integer32):
    """Custom type n1macStatusEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_N1macStatusEnable_Type.__name__ = "Integer32"
_N1macStatusEnable_Object = MibTableColumn
n1macStatusEnable = _N1macStatusEnable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 58, 2, 1, 1),
    _N1macStatusEnable_Type()
)
n1macStatusEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    n1macStatusEnable.setStatus("current")
_Macff_ObjectIdentity = ObjectIdentity
macff = _Macff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 60)
)
_MacFfTable_Object = MibTable
macFfTable = _MacFfTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 60, 1)
)
if mibBuilder.loadTexts:
    macFfTable.setStatus("current")
_MacFfEntry_Object = MibTableRow
macFfEntry = _MacFfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 60, 1, 1)
)
macFfEntry.setIndexNames(
    (0, "E5-121-MIB", "macFfIndex"),
)
if mibBuilder.loadTexts:
    macFfEntry.setStatus("current")
_MacFfIndex_Type = Integer32
_MacFfIndex_Object = MibTableColumn
macFfIndex = _MacFfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 60, 1, 1, 1),
    _MacFfIndex_Type()
)
macFfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macFfIndex.setStatus("current")
_MacFfVid_Type = Integer32
_MacFfVid_Object = MibTableColumn
macFfVid = _MacFfVid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 60, 1, 1, 2),
    _MacFfVid_Type()
)
macFfVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macFfVid.setStatus("current")
_MacFfArIP_Type = IpAddress
_MacFfArIP_Object = MibTableColumn
macFfArIP = _MacFfArIP_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 60, 1, 1, 3),
    _MacFfArIP_Type()
)
macFfArIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macFfArIP.setStatus("current")
_MacFfSrcIP_Type = IpAddress
_MacFfSrcIP_Object = MibTableColumn
macFfSrcIP = _MacFfSrcIP_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 60, 1, 1, 4),
    _MacFfSrcIP_Type()
)
macFfSrcIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macFfSrcIP.setStatus("current")
_MacFfSrcMask_Type = Integer32
_MacFfSrcMask_Object = MibTableColumn
macFfSrcMask = _MacFfSrcMask_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 60, 1, 1, 5),
    _MacFfSrcMask_Type()
)
macFfSrcMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macFfSrcMask.setStatus("current")
_MacFfRowStatus_Type = RowStatus
_MacFfRowStatus_Object = MibTableColumn
macFfRowStatus = _MacFfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 60, 1, 1, 6),
    _MacFfRowStatus_Type()
)
macFfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    macFfRowStatus.setStatus("current")
_MacFfArpFlush_Type = Integer32
_MacFfArpFlush_Object = MibScalar
macFfArpFlush = _MacFfArpFlush_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 60, 3),
    _MacFfArpFlush_Type()
)
macFfArpFlush.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macFfArpFlush.setStatus("current")
_MaxNumOfMacFfVlanInSystem_Type = Integer32
_MaxNumOfMacFfVlanInSystem_Object = MibScalar
maxNumOfMacFfVlanInSystem = _MaxNumOfMacFfVlanInSystem_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 60, 4),
    _MaxNumOfMacFfVlanInSystem_Type()
)
maxNumOfMacFfVlanInSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumOfMacFfVlanInSystem.setStatus("current")
_MacFfVlanTable_Object = MibTable
macFfVlanTable = _MacFfVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 60, 5)
)
if mibBuilder.loadTexts:
    macFfVlanTable.setStatus("current")
_MacFfVlanEntry_Object = MibTableRow
macFfVlanEntry = _MacFfVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 60, 5, 1)
)
macFfVlanEntry.setIndexNames(
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
)
if mibBuilder.loadTexts:
    macFfVlanEntry.setStatus("current")
_MacFfVlanRowstatus_Type = RowStatus
_MacFfVlanRowstatus_Object = MibTableColumn
macFfVlanRowstatus = _MacFfVlanRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 60, 5, 1, 1),
    _MacFfVlanRowstatus_Type()
)
macFfVlanRowstatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    macFfVlanRowstatus.setStatus("current")
_MacFfStaticIPTable_Object = MibTable
macFfStaticIPTable = _MacFfStaticIPTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 60, 6)
)
if mibBuilder.loadTexts:
    macFfStaticIPTable.setStatus("current")
_MacFfStaticIPEntry_Object = MibTableRow
macFfStaticIPEntry = _MacFfStaticIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 60, 6, 1)
)
macFfStaticIPEntry.setIndexNames(
    (0, "E5-121-MIB", "macFfStaticIPPort"),
    (0, "E5-121-MIB", "macFfStaticIPVid"),
    (0, "E5-121-MIB", "macFfstaticIP"),
    (0, "E5-121-MIB", "macFfStaticIPMask"),
)
if mibBuilder.loadTexts:
    macFfStaticIPEntry.setStatus("current")
_MacFfStaticIPPort_Type = Integer32
_MacFfStaticIPPort_Object = MibTableColumn
macFfStaticIPPort = _MacFfStaticIPPort_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 60, 6, 1, 1),
    _MacFfStaticIPPort_Type()
)
macFfStaticIPPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macFfStaticIPPort.setStatus("current")
_MacFfStaticIPVid_Type = Integer32
_MacFfStaticIPVid_Object = MibTableColumn
macFfStaticIPVid = _MacFfStaticIPVid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 60, 6, 1, 2),
    _MacFfStaticIPVid_Type()
)
macFfStaticIPVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macFfStaticIPVid.setStatus("current")
_MacFfstaticIP_Type = IpAddress
_MacFfstaticIP_Object = MibTableColumn
macFfstaticIP = _MacFfstaticIP_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 60, 6, 1, 3),
    _MacFfstaticIP_Type()
)
macFfstaticIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macFfstaticIP.setStatus("current")
_MacFfStaticIPMask_Type = Integer32
_MacFfStaticIPMask_Object = MibTableColumn
macFfStaticIPMask = _MacFfStaticIPMask_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 60, 6, 1, 4),
    _MacFfStaticIPMask_Type()
)
macFfStaticIPMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macFfStaticIPMask.setStatus("current")
_MacFfStaticIPRowStatus_Type = RowStatus
_MacFfStaticIPRowStatus_Object = MibTableColumn
macFfStaticIPRowStatus = _MacFfStaticIPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 60, 6, 1, 5),
    _MacFfStaticIPRowStatus_Type()
)
macFfStaticIPRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    macFfStaticIPRowStatus.setStatus("current")
_MacFfServerMacTable_Object = MibTable
macFfServerMacTable = _MacFfServerMacTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 60, 7)
)
if mibBuilder.loadTexts:
    macFfServerMacTable.setStatus("current")
_MacFfServerMacEntry_Object = MibTableRow
macFfServerMacEntry = _MacFfServerMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 60, 7, 1)
)
macFfServerMacEntry.setIndexNames(
    (0, "E5-121-MIB", "macFfServerMacVid"),
    (0, "E5-121-MIB", "macFfServerMacAddr"),
)
if mibBuilder.loadTexts:
    macFfServerMacEntry.setStatus("current")
_MacFfServerMacVid_Type = Integer32
_MacFfServerMacVid_Object = MibTableColumn
macFfServerMacVid = _MacFfServerMacVid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 60, 7, 1, 1),
    _MacFfServerMacVid_Type()
)
macFfServerMacVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macFfServerMacVid.setStatus("current")
_MacFfServerMacAddr_Type = PhysAddress
_MacFfServerMacAddr_Object = MibTableColumn
macFfServerMacAddr = _MacFfServerMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 60, 7, 1, 2),
    _MacFfServerMacAddr_Type()
)
macFfServerMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macFfServerMacAddr.setStatus("current")
_MacFfServerMacRowStatus_Type = RowStatus
_MacFfServerMacRowStatus_Object = MibTableColumn
macFfServerMacRowStatus = _MacFfServerMacRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 10, 60, 7, 1, 3),
    _MacFfServerMacRowStatus_Type()
)
macFfServerMacRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    macFfServerMacRowStatus.setStatus("current")
_Sys_ObjectIdentity = ObjectIdentity
sys = _Sys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 11)
)
_TimeSetup_ObjectIdentity = ObjectIdentity
timeSetup = _TimeSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 11, 4)
)
_DayLightSaving_ObjectIdentity = ObjectIdentity
dayLightSaving = _DayLightSaving_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 11, 4, 7)
)


class _DayLightSavingAdminStatus_Type(Integer32):
    """Custom type dayLightSavingAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_DayLightSavingAdminStatus_Type.__name__ = "Integer32"
_DayLightSavingAdminStatus_Object = MibScalar
dayLightSavingAdminStatus = _DayLightSavingAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 11, 4, 7, 1),
    _DayLightSavingAdminStatus_Type()
)
dayLightSavingAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dayLightSavingAdminStatus.setStatus("current")
_DayLightSavingStartTime_ObjectIdentity = ObjectIdentity
dayLightSavingStartTime = _DayLightSavingStartTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 11, 4, 7, 2)
)


class _DayLightSavingStartMonth_Type(Integer32):
    """Custom type dayLightSavingStartMonth based on Integer32"""
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
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("Jan", 1),
          ("Feb", 2),
          ("Mar", 3),
          ("Apr", 4),
          ("May", 5),
          ("Jun", 6),
          ("Jul", 7),
          ("Aug", 8),
          ("Sep", 9),
          ("Oct", 10),
          ("Nov", 11),
          ("Dec", 12))
    )


_DayLightSavingStartMonth_Type.__name__ = "Integer32"
_DayLightSavingStartMonth_Object = MibScalar
dayLightSavingStartMonth = _DayLightSavingStartMonth_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 11, 4, 7, 2, 1),
    _DayLightSavingStartMonth_Type()
)
dayLightSavingStartMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dayLightSavingStartMonth.setStatus("current")


class _DayLightSavingStartWeek_Type(Integer32):
    """Custom type dayLightSavingStartWeek based on Integer32"""
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
        *(("First", 1),
          ("Second", 2),
          ("Third", 3),
          ("Fourth", 4),
          ("Last", 5))
    )


_DayLightSavingStartWeek_Type.__name__ = "Integer32"
_DayLightSavingStartWeek_Object = MibScalar
dayLightSavingStartWeek = _DayLightSavingStartWeek_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 11, 4, 7, 2, 2),
    _DayLightSavingStartWeek_Type()
)
dayLightSavingStartWeek.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dayLightSavingStartWeek.setStatus("current")


class _DayLightSavingStartWday_Type(Integer32):
    """Custom type dayLightSavingStartWday based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("Sun", 1),
          ("Mon", 2),
          ("Tus", 3),
          ("Wed", 4),
          ("Thu", 5),
          ("Fri", 6),
          ("Sat", 7))
    )


_DayLightSavingStartWday_Type.__name__ = "Integer32"
_DayLightSavingStartWday_Object = MibScalar
dayLightSavingStartWday = _DayLightSavingStartWday_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 11, 4, 7, 2, 3),
    _DayLightSavingStartWday_Type()
)
dayLightSavingStartWday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dayLightSavingStartWday.setStatus("current")
_DayLightSavingStartHour_Type = Integer32
_DayLightSavingStartHour_Object = MibScalar
dayLightSavingStartHour = _DayLightSavingStartHour_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 11, 4, 7, 2, 4),
    _DayLightSavingStartHour_Type()
)
dayLightSavingStartHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dayLightSavingStartHour.setStatus("current")
_DayLightSavingEndTime_ObjectIdentity = ObjectIdentity
dayLightSavingEndTime = _DayLightSavingEndTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 11, 4, 7, 3)
)


class _DayLightSavingEndMonth_Type(Integer32):
    """Custom type dayLightSavingEndMonth based on Integer32"""
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
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("Jan", 1),
          ("Feb", 2),
          ("Mar", 3),
          ("Apr", 4),
          ("May", 5),
          ("Jun", 6),
          ("Jul", 7),
          ("Aug", 8),
          ("Sep", 9),
          ("Oct", 10),
          ("Nov", 11),
          ("Dec", 12))
    )


_DayLightSavingEndMonth_Type.__name__ = "Integer32"
_DayLightSavingEndMonth_Object = MibScalar
dayLightSavingEndMonth = _DayLightSavingEndMonth_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 11, 4, 7, 3, 1),
    _DayLightSavingEndMonth_Type()
)
dayLightSavingEndMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dayLightSavingEndMonth.setStatus("current")


class _DayLightSavingEndWeek_Type(Integer32):
    """Custom type dayLightSavingEndWeek based on Integer32"""
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
        *(("First", 1),
          ("Second", 2),
          ("Third", 3),
          ("Fourth", 4),
          ("Last", 5))
    )


_DayLightSavingEndWeek_Type.__name__ = "Integer32"
_DayLightSavingEndWeek_Object = MibScalar
dayLightSavingEndWeek = _DayLightSavingEndWeek_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 11, 4, 7, 3, 2),
    _DayLightSavingEndWeek_Type()
)
dayLightSavingEndWeek.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dayLightSavingEndWeek.setStatus("current")


class _DayLightSavingEndWday_Type(Integer32):
    """Custom type dayLightSavingEndWday based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("Sun", 1),
          ("Mon", 2),
          ("Tus", 3),
          ("Wed", 4),
          ("Thu", 5),
          ("Fri", 6),
          ("Sat", 7))
    )


_DayLightSavingEndWday_Type.__name__ = "Integer32"
_DayLightSavingEndWday_Object = MibScalar
dayLightSavingEndWday = _DayLightSavingEndWday_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 11, 4, 7, 3, 3),
    _DayLightSavingEndWday_Type()
)
dayLightSavingEndWday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dayLightSavingEndWday.setStatus("current")
_DayLightSavingEndHour_Type = Integer32
_DayLightSavingEndHour_Object = MibScalar
dayLightSavingEndHour = _DayLightSavingEndHour_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 11, 4, 7, 3, 4),
    _DayLightSavingEndHour_Type()
)
dayLightSavingEndHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dayLightSavingEndHour.setStatus("current")
_AccessCtrl_ObjectIdentity = ObjectIdentity
accessCtrl = _AccessCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 11, 5)
)
_SecuredClientTable_Object = MibTable
securedClientTable = _SecuredClientTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 11, 5, 2)
)
if mibBuilder.loadTexts:
    securedClientTable.setStatus("current")
_SecuredClientEntry_Object = MibTableRow
securedClientEntry = _SecuredClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 11, 5, 2, 1)
)
securedClientEntry.setIndexNames(
    (0, "E5-121-MIB", "securedClientIndex"),
)
if mibBuilder.loadTexts:
    securedClientEntry.setStatus("current")
_SecuredClientIndex_Type = Integer32
_SecuredClientIndex_Object = MibTableColumn
securedClientIndex = _SecuredClientIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 11, 5, 2, 1, 1),
    _SecuredClientIndex_Type()
)
securedClientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securedClientIndex.setStatus("current")
_SecuredClientStartIp_Type = IpAddress
_SecuredClientStartIp_Object = MibTableColumn
securedClientStartIp = _SecuredClientStartIp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 11, 5, 2, 1, 2),
    _SecuredClientStartIp_Type()
)
securedClientStartIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securedClientStartIp.setStatus("current")
_SecuredClientEndIp_Type = IpAddress
_SecuredClientEndIp_Object = MibTableColumn
securedClientEndIp = _SecuredClientEndIp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 11, 5, 2, 1, 3),
    _SecuredClientEndIp_Type()
)
securedClientEndIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securedClientEndIp.setStatus("current")
_SecuredClientService_Type = Integer32
_SecuredClientService_Object = MibTableColumn
securedClientService = _SecuredClientService_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 11, 5, 2, 1, 4),
    _SecuredClientService_Type()
)
securedClientService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securedClientService.setStatus("current")


class _SecuredClientEnable_Type(Integer32):
    """Custom type securedClientEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_SecuredClientEnable_Type.__name__ = "Integer32"
_SecuredClientEnable_Object = MibTableColumn
securedClientEnable = _SecuredClientEnable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 11, 5, 2, 1, 5),
    _SecuredClientEnable_Type()
)
securedClientEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securedClientEnable.setStatus("current")
_ExtAlarm_ObjectIdentity = ObjectIdentity
extAlarm = _ExtAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 11, 8)
)
_ExtAlarmTable_Object = MibTable
extAlarmTable = _ExtAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 11, 8, 1)
)
if mibBuilder.loadTexts:
    extAlarmTable.setStatus("current")
_ExtAlarmEntry_Object = MibTableRow
extAlarmEntry = _ExtAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 11, 8, 1, 1)
)
extAlarmEntry.setIndexNames(
    (0, "E5-121-MIB", "extAlarmIndex"),
)
if mibBuilder.loadTexts:
    extAlarmEntry.setStatus("current")
_ExtAlarmIndex_Type = Integer32
_ExtAlarmIndex_Object = MibTableColumn
extAlarmIndex = _ExtAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 11, 8, 1, 1, 1),
    _ExtAlarmIndex_Type()
)
extAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extAlarmIndex.setStatus("current")


class _ExtAlarmName_Type(DisplayString):
    """Custom type extAlarmName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_ExtAlarmName_Type.__name__ = "DisplayString"
_ExtAlarmName_Object = MibTableColumn
extAlarmName = _ExtAlarmName_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 11, 8, 1, 1, 2),
    _ExtAlarmName_Type()
)
extAlarmName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extAlarmName.setStatus("current")


class _ExtAlarmStatus_Type(DisplayString):
    """Custom type extAlarmStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_ExtAlarmStatus_Type.__name__ = "DisplayString"
_ExtAlarmStatus_Object = MibTableColumn
extAlarmStatus = _ExtAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 11, 8, 1, 1, 3),
    _ExtAlarmStatus_Type()
)
extAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extAlarmStatus.setStatus("current")


class _ExtAlarmTriggeredMode_Type(Integer32):
    """Custom type extAlarmTriggeredMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("closeAlarm", 1),
          ("openAlarm", 2))
    )


_ExtAlarmTriggeredMode_Type.__name__ = "Integer32"
_ExtAlarmTriggeredMode_Object = MibTableColumn
extAlarmTriggeredMode = _ExtAlarmTriggeredMode_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 11, 8, 1, 1, 4),
    _ExtAlarmTriggeredMode_Type()
)
extAlarmTriggeredMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extAlarmTriggeredMode.setStatus("current")
_User_ObjectIdentity = ObjectIdentity
user = _User_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 11, 9)
)


class _UserAuthMode_Type(Integer32):
    """Custom type userAuthMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("radius", 2),
          ("localThenRadius", 3))
    )


_UserAuthMode_Type.__name__ = "Integer32"
_UserAuthMode_Object = MibScalar
userAuthMode = _UserAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 11, 9, 1),
    _UserAuthMode_Type()
)
userAuthMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userAuthMode.setStatus("current")
_UserAuthServerIp_Type = IpAddress
_UserAuthServerIp_Object = MibScalar
userAuthServerIp = _UserAuthServerIp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 11, 9, 2),
    _UserAuthServerIp_Type()
)
userAuthServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userAuthServerIp.setStatus("current")
_UserAuthServerPort_Type = Integer32
_UserAuthServerPort_Object = MibScalar
userAuthServerPort = _UserAuthServerPort_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 11, 9, 3),
    _UserAuthServerPort_Type()
)
userAuthServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userAuthServerPort.setStatus("current")
_UserAuthServerSecret_Type = OctetString
_UserAuthServerSecret_Object = MibScalar
userAuthServerSecret = _UserAuthServerSecret_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 11, 9, 4),
    _UserAuthServerSecret_Type()
)
userAuthServerSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userAuthServerSecret.setStatus("current")
_UserTable_Object = MibTable
userTable = _UserTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 11, 9, 5)
)
if mibBuilder.loadTexts:
    userTable.setStatus("current")
_UserEntry_Object = MibTableRow
userEntry = _UserEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 11, 9, 5, 1)
)
userEntry.setIndexNames(
    (0, "E5-121-MIB", "userName"),
)
if mibBuilder.loadTexts:
    userEntry.setStatus("current")
_UserName_Type = DisplayString
_UserName_Object = MibTableColumn
userName = _UserName_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 11, 9, 5, 1, 1),
    _UserName_Type()
)
userName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userName.setStatus("current")
_UserPassword_Type = DisplayString
_UserPassword_Object = MibTableColumn
userPassword = _UserPassword_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 11, 9, 5, 1, 2),
    _UserPassword_Type()
)
userPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    userPassword.setStatus("current")


class _UserPriviledge_Type(Integer32):
    """Custom type userPriviledge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("middle", 2),
          ("low", 3))
    )


_UserPriviledge_Type.__name__ = "Integer32"
_UserPriviledge_Object = MibTableColumn
userPriviledge = _UserPriviledge_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 11, 9, 5, 1, 3),
    _UserPriviledge_Type()
)
userPriviledge.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    userPriviledge.setStatus("current")
_UserRowStatus_Type = RowStatus
_UserRowStatus_Object = MibTableColumn
userRowStatus = _UserRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 11, 9, 5, 1, 4),
    _UserRowStatus_Type()
)
userRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    userRowStatus.setStatus("current")


class _UserAuthDefaultPriviledge_Type(Integer32):
    """Custom type userAuthDefaultPriviledge based on Integer32"""
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
        *(("high", 1),
          ("middle", 2),
          ("low", 3),
          ("deny", 4))
    )


_UserAuthDefaultPriviledge_Type.__name__ = "Integer32"
_UserAuthDefaultPriviledge_Object = MibScalar
userAuthDefaultPriviledge = _UserAuthDefaultPriviledge_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 11, 9, 6),
    _UserAuthDefaultPriviledge_Type()
)
userAuthDefaultPriviledge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userAuthDefaultPriviledge.setStatus("current")
_UsbCastCtrl_ObjectIdentity = ObjectIdentity
usbCastCtrl = _UsbCastCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 11, 10)
)


class _UsBcastCtrlEnable_Type(Integer32):
    """Custom type usBcastCtrlEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_UsBcastCtrlEnable_Type.__name__ = "Integer32"
_UsBcastCtrlEnable_Object = MibScalar
usBcastCtrlEnable = _UsBcastCtrlEnable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 11, 10, 1),
    _UsBcastCtrlEnable_Type()
)
usBcastCtrlEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usBcastCtrlEnable.setStatus("current")
_UsBcastCtrlRate_Type = Integer32
_UsBcastCtrlRate_Object = MibScalar
usBcastCtrlRate = _UsBcastCtrlRate_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 11, 10, 2),
    _UsBcastCtrlRate_Type()
)
usBcastCtrlRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usBcastCtrlRate.setStatus("current")
if mibBuilder.loadTexts:
    usBcastCtrlRate.setUnits("Kbps")
_DsQos_ObjectIdentity = ObjectIdentity
dsQos = _DsQos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 11, 11)
)


class _DsQosEnableMode_Type(Integer32):
    """Custom type dsQosEnableMode based on Integer32"""
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
        *(("disable", 1),
          ("vlan", 2),
          ("dscp", 3),
          ("ippre", 4))
    )


_DsQosEnableMode_Type.__name__ = "Integer32"
_DsQosEnableMode_Object = MibScalar
dsQosEnableMode = _DsQosEnableMode_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 11, 11, 1),
    _DsQosEnableMode_Type()
)
dsQosEnableMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsQosEnableMode.setStatus("current")


class _DsQosDefaultPri_Type(Integer32):
    """Custom type dsQosDefaultPri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_DsQosDefaultPri_Type.__name__ = "Integer32"
_DsQosDefaultPri_Object = MibScalar
dsQosDefaultPri = _DsQosDefaultPri_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 11, 11, 2),
    _DsQosDefaultPri_Type()
)
dsQosDefaultPri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsQosDefaultPri.setStatus("current")
_DsQoSOverridingTable_Object = MibTable
dsQoSOverridingTable = _DsQoSOverridingTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 11, 11, 3)
)
if mibBuilder.loadTexts:
    dsQoSOverridingTable.setStatus("current")
_DsQoSOverridingEntry_Object = MibTableRow
dsQoSOverridingEntry = _DsQoSOverridingEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 11, 11, 3, 1)
)
dsQoSOverridingEntry.setIndexNames(
    (0, "E5-121-MIB", "dsQosPriority"),
)
if mibBuilder.loadTexts:
    dsQoSOverridingEntry.setStatus("current")


class _DsQosPriority_Type(Integer32):
    """Custom type dsQosPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_DsQosPriority_Type.__name__ = "Integer32"
_DsQosPriority_Object = MibTableColumn
dsQosPriority = _DsQosPriority_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 11, 11, 3, 1, 1),
    _DsQosPriority_Type()
)
dsQosPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsQosPriority.setStatus("current")
_DsQosValueList_Type = DisplayString
_DsQosValueList_Object = MibTableColumn
dsQosValueList = _DsQosValueList_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 11, 11, 3, 1, 2),
    _DsQosValueList_Type()
)
dsQosValueList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsQosValueList.setStatus("current")


class _StdioTimeout_Type(Integer32):
    """Custom type stdioTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_StdioTimeout_Type.__name__ = "Integer32"
_StdioTimeout_Object = MibScalar
stdioTimeout = _StdioTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 11, 12),
    _StdioTimeout_Type()
)
stdioTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stdioTimeout.setStatus("current")


class _IsConfigChanged_Type(Integer32):
    """Custom type isConfigChanged based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_IsConfigChanged_Type.__name__ = "Integer32"
_IsConfigChanged_Object = MibScalar
isConfigChanged = _IsConfigChanged_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 11, 13),
    _IsConfigChanged_Type()
)
isConfigChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isConfigChanged.setStatus("current")
_FwUpgrade_ObjectIdentity = ObjectIdentity
fwUpgrade = _FwUpgrade_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 11, 14)
)
_FwUpgradeVersion_Type = OctetString
_FwUpgradeVersion_Object = MibScalar
fwUpgradeVersion = _FwUpgradeVersion_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 11, 14, 1),
    _FwUpgradeVersion_Type()
)
fwUpgradeVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fwUpgradeVersion.setStatus("current")


class _FwUpgradeCheck_Type(Integer32):
    """Custom type fwUpgradeCheck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_FwUpgradeCheck_Type.__name__ = "Integer32"
_FwUpgradeCheck_Object = MibScalar
fwUpgradeCheck = _FwUpgradeCheck_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 11, 14, 2),
    _FwUpgradeCheck_Type()
)
fwUpgradeCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fwUpgradeCheck.setStatus("current")
_FwUpgradeStatus_Type = DisplayString
_FwUpgradeStatus_Object = MibScalar
fwUpgradeStatus = _FwUpgradeStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 11, 14, 3),
    _FwUpgradeStatus_Type()
)
fwUpgradeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwUpgradeStatus.setStatus("current")
_DelayedReboot_ObjectIdentity = ObjectIdentity
delayedReboot = _DelayedReboot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 11, 15)
)
_DelayedRebootTimer_Type = Integer32
_DelayedRebootTimer_Object = MibScalar
delayedRebootTimer = _DelayedRebootTimer_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 11, 15, 1),
    _DelayedRebootTimer_Type()
)
delayedRebootTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    delayedRebootTimer.setStatus("current")
if mibBuilder.loadTexts:
    delayedRebootTimer.setUnits("sec")
_DelayedRebootRemainingTime_Type = Integer32
_DelayedRebootRemainingTime_Object = MibScalar
delayedRebootRemainingTime = _DelayedRebootRemainingTime_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 11, 15, 2),
    _DelayedRebootRemainingTime_Type()
)
delayedRebootRemainingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayedRebootRemainingTime.setStatus("current")
if mibBuilder.loadTexts:
    delayedRebootRemainingTime.setUnits("sec")


class _DelayedRebootCancel_Type(Integer32):
    """Custom type delayedRebootCancel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("cancel", 1)
    )


_DelayedRebootCancel_Type.__name__ = "Integer32"
_DelayedRebootCancel_Object = MibScalar
delayedRebootCancel = _DelayedRebootCancel_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 11, 15, 3),
    _DelayedRebootCancel_Type()
)
delayedRebootCancel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    delayedRebootCancel.setStatus("current")
_Trap_ObjectIdentity = ObjectIdentity
trap = _Trap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 12)
)
_Statistics_ObjectIdentity = ObjectIdentity
statistics = _Statistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13)
)
_IgmpQueryCntTotal_Type = Counter32
_IgmpQueryCntTotal_Object = MibScalar
igmpQueryCntTotal = _IgmpQueryCntTotal_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 1),
    _IgmpQueryCntTotal_Type()
)
igmpQueryCntTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpQueryCntTotal.setStatus("current")
_IgmpReportCntTotal_Type = Counter32
_IgmpReportCntTotal_Object = MibScalar
igmpReportCntTotal = _IgmpReportCntTotal_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 2),
    _IgmpReportCntTotal_Type()
)
igmpReportCntTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpReportCntTotal.setStatus("current")
_IgmpLeaveCntTotal_Type = Counter32
_IgmpLeaveCntTotal_Object = MibScalar
igmpLeaveCntTotal = _IgmpLeaveCntTotal_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 3),
    _IgmpLeaveCntTotal_Type()
)
igmpLeaveCntTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpLeaveCntTotal.setStatus("current")
_IgmpNumOfActiveGroups_Type = Integer32
_IgmpNumOfActiveGroups_Object = MibScalar
igmpNumOfActiveGroups = _IgmpNumOfActiveGroups_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 4),
    _IgmpNumOfActiveGroups_Type()
)
igmpNumOfActiveGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpNumOfActiveGroups.setStatus("current")
_IgmpGroupTable_Object = MibTable
igmpGroupTable = _IgmpGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 5)
)
if mibBuilder.loadTexts:
    igmpGroupTable.setStatus("current")
_IgmpGroupEntry_Object = MibTableRow
igmpGroupEntry = _IgmpGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 5, 1)
)
igmpGroupEntry.setIndexNames(
    (0, "E5-121-MIB", "igmpGroupIp"),
)
if mibBuilder.loadTexts:
    igmpGroupEntry.setStatus("current")
_IgmpGroupIp_Type = IpAddress
_IgmpGroupIp_Object = MibTableColumn
igmpGroupIp = _IgmpGroupIp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 5, 1, 1),
    _IgmpGroupIp_Type()
)
igmpGroupIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpGroupIp.setStatus("current")
_IgmpGroupvid_Type = Integer32
_IgmpGroupvid_Object = MibTableColumn
igmpGroupvid = _IgmpGroupvid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 5, 1, 2),
    _IgmpGroupvid_Type()
)
igmpGroupvid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpGroupvid.setStatus("current")
_IgmpGroupnumberOfMembers_Type = Integer32
_IgmpGroupnumberOfMembers_Object = MibTableColumn
igmpGroupnumberOfMembers = _IgmpGroupnumberOfMembers_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 5, 1, 3),
    _IgmpGroupnumberOfMembers_Type()
)
igmpGroupnumberOfMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpGroupnumberOfMembers.setStatus("current")
_IgmpGroupMemberPorts_Type = PortList
_IgmpGroupMemberPorts_Object = MibTableColumn
igmpGroupMemberPorts = _IgmpGroupMemberPorts_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 5, 1, 4),
    _IgmpGroupMemberPorts_Type()
)
igmpGroupMemberPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpGroupMemberPorts.setStatus("current")
_IgmpGroupPortTable_Object = MibTable
igmpGroupPortTable = _IgmpGroupPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 6)
)
if mibBuilder.loadTexts:
    igmpGroupPortTable.setStatus("current")
_IgmpGroupPortEntry_Object = MibTableRow
igmpGroupPortEntry = _IgmpGroupPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 6, 1)
)
igmpGroupPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "E5-121-MIB", "igmpGroupPortIp"),
    (0, "E5-121-MIB", "igmpGroupPortvid"),
)
if mibBuilder.loadTexts:
    igmpGroupPortEntry.setStatus("current")
_IgmpGroupPortIp_Type = IpAddress
_IgmpGroupPortIp_Object = MibTableColumn
igmpGroupPortIp = _IgmpGroupPortIp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 6, 1, 1),
    _IgmpGroupPortIp_Type()
)
igmpGroupPortIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpGroupPortIp.setStatus("current")
_IgmpGroupPortvid_Type = Integer32
_IgmpGroupPortvid_Object = MibTableColumn
igmpGroupPortvid = _IgmpGroupPortvid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 6, 1, 2),
    _IgmpGroupPortvid_Type()
)
igmpGroupPortvid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpGroupPortvid.setStatus("current")
_IgmpGroupV2Table_Object = MibTable
igmpGroupV2Table = _IgmpGroupV2Table_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 7)
)
if mibBuilder.loadTexts:
    igmpGroupV2Table.setStatus("current")
_IgmpGroupV2Entry_Object = MibTableRow
igmpGroupV2Entry = _IgmpGroupV2Entry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 7, 1)
)
igmpGroupV2Entry.setIndexNames(
    (0, "E5-121-MIB", "igmpGroupV2Vid"),
    (0, "E5-121-MIB", "igmpGroupV2Ip"),
)
if mibBuilder.loadTexts:
    igmpGroupV2Entry.setStatus("current")
_IgmpGroupV2Vid_Type = VlanIndex
_IgmpGroupV2Vid_Object = MibTableColumn
igmpGroupV2Vid = _IgmpGroupV2Vid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 7, 1, 1),
    _IgmpGroupV2Vid_Type()
)
igmpGroupV2Vid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpGroupV2Vid.setStatus("current")
_IgmpGroupV2Ip_Type = IpAddress
_IgmpGroupV2Ip_Object = MibTableColumn
igmpGroupV2Ip = _IgmpGroupV2Ip_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 7, 1, 2),
    _IgmpGroupV2Ip_Type()
)
igmpGroupV2Ip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpGroupV2Ip.setStatus("current")
_IgmpGroupV2NumOfMembers_Type = Integer32
_IgmpGroupV2NumOfMembers_Object = MibTableColumn
igmpGroupV2NumOfMembers = _IgmpGroupV2NumOfMembers_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 7, 1, 3),
    _IgmpGroupV2NumOfMembers_Type()
)
igmpGroupV2NumOfMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpGroupV2NumOfMembers.setStatus("current")
_IgmpGroupV2MemberPorts_Type = PortList
_IgmpGroupV2MemberPorts_Object = MibTableColumn
igmpGroupV2MemberPorts = _IgmpGroupV2MemberPorts_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 7, 1, 4),
    _IgmpGroupV2MemberPorts_Type()
)
igmpGroupV2MemberPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpGroupV2MemberPorts.setStatus("current")
_IgmpGroupPortV2Table_Object = MibTable
igmpGroupPortV2Table = _IgmpGroupPortV2Table_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 8)
)
if mibBuilder.loadTexts:
    igmpGroupPortV2Table.setStatus("current")
_IgmpGroupPortV2Entry_Object = MibTableRow
igmpGroupPortV2Entry = _IgmpGroupPortV2Entry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 8, 1)
)
igmpGroupPortV2Entry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "E5-121-MIB", "igmpGroupPortV2Vid"),
    (0, "E5-121-MIB", "igmpGroupPortV2Ip"),
    (0, "E5-121-MIB", "igmpGroupPortV2SourceIp"),
)
if mibBuilder.loadTexts:
    igmpGroupPortV2Entry.setStatus("current")
_IgmpGroupPortV2Vid_Type = VlanIndex
_IgmpGroupPortV2Vid_Object = MibTableColumn
igmpGroupPortV2Vid = _IgmpGroupPortV2Vid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 8, 1, 1),
    _IgmpGroupPortV2Vid_Type()
)
igmpGroupPortV2Vid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpGroupPortV2Vid.setStatus("current")
_IgmpGroupPortV2Ip_Type = IpAddress
_IgmpGroupPortV2Ip_Object = MibTableColumn
igmpGroupPortV2Ip = _IgmpGroupPortV2Ip_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 8, 1, 2),
    _IgmpGroupPortV2Ip_Type()
)
igmpGroupPortV2Ip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpGroupPortV2Ip.setStatus("current")
_IgmpGroupPortV2SourceIp_Type = IpAddress
_IgmpGroupPortV2SourceIp_Object = MibTableColumn
igmpGroupPortV2SourceIp = _IgmpGroupPortV2SourceIp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 8, 1, 3),
    _IgmpGroupPortV2SourceIp_Type()
)
igmpGroupPortV2SourceIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpGroupPortV2SourceIp.setStatus("current")
_IgmpPortCtrlPduTable_Object = MibTable
igmpPortCtrlPduTable = _IgmpPortCtrlPduTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 9)
)
if mibBuilder.loadTexts:
    igmpPortCtrlPduTable.setStatus("current")
_IgmpPortCtrlPduEntry_Object = MibTableRow
igmpPortCtrlPduEntry = _IgmpPortCtrlPduEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 9, 1)
)
igmpPortCtrlPduEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    igmpPortCtrlPduEntry.setStatus("current")
_IgmpPortCtrlPduQueryCnt_Type = Counter32
_IgmpPortCtrlPduQueryCnt_Object = MibTableColumn
igmpPortCtrlPduQueryCnt = _IgmpPortCtrlPduQueryCnt_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 9, 1, 1),
    _IgmpPortCtrlPduQueryCnt_Type()
)
igmpPortCtrlPduQueryCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpPortCtrlPduQueryCnt.setStatus("current")
_IgmpPortCtrlPduReportCnt_Type = Counter32
_IgmpPortCtrlPduReportCnt_Object = MibTableColumn
igmpPortCtrlPduReportCnt = _IgmpPortCtrlPduReportCnt_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 9, 1, 2),
    _IgmpPortCtrlPduReportCnt_Type()
)
igmpPortCtrlPduReportCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpPortCtrlPduReportCnt.setStatus("current")
_IgmpPortCtrlPduLeaveCnt_Type = Counter32
_IgmpPortCtrlPduLeaveCnt_Object = MibTableColumn
igmpPortCtrlPduLeaveCnt = _IgmpPortCtrlPduLeaveCnt_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 9, 1, 3),
    _IgmpPortCtrlPduLeaveCnt_Type()
)
igmpPortCtrlPduLeaveCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpPortCtrlPduLeaveCnt.setStatus("current")
_IgmpPortNumOfActiveGroups_Type = Integer32
_IgmpPortNumOfActiveGroups_Object = MibTableColumn
igmpPortNumOfActiveGroups = _IgmpPortNumOfActiveGroups_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 9, 1, 4),
    _IgmpPortNumOfActiveGroups_Type()
)
igmpPortNumOfActiveGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpPortNumOfActiveGroups.setStatus("current")
_IgmpPortCtrlAuditLeaveCnt_Type = Counter32
_IgmpPortCtrlAuditLeaveCnt_Object = MibTableColumn
igmpPortCtrlAuditLeaveCnt = _IgmpPortCtrlAuditLeaveCnt_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 9, 1, 5),
    _IgmpPortCtrlAuditLeaveCnt_Type()
)
igmpPortCtrlAuditLeaveCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpPortCtrlAuditLeaveCnt.setStatus("current")
_DhcpStats_ObjectIdentity = ObjectIdentity
dhcpStats = _DhcpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 11)
)
_DhcpSnoopIpTable_Object = MibTable
dhcpSnoopIpTable = _DhcpSnoopIpTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 11, 1)
)
if mibBuilder.loadTexts:
    dhcpSnoopIpTable.setStatus("current")
_DhcpSnoopIpEntry_Object = MibTableRow
dhcpSnoopIpEntry = _DhcpSnoopIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 11, 1, 1)
)
dhcpSnoopIpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "E5-121-MIB", "dhcpSnoopIp"),
)
if mibBuilder.loadTexts:
    dhcpSnoopIpEntry.setStatus("current")
_DhcpSnoopIp_Type = IpAddress
_DhcpSnoopIp_Object = MibTableColumn
dhcpSnoopIp = _DhcpSnoopIp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 11, 1, 1, 1),
    _DhcpSnoopIp_Type()
)
dhcpSnoopIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnoopIp.setStatus("current")
_DhcpSnoopMac_Type = PhysAddress
_DhcpSnoopMac_Object = MibTableColumn
dhcpSnoopMac = _DhcpSnoopMac_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 11, 1, 1, 2),
    _DhcpSnoopMac_Type()
)
dhcpSnoopMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnoopMac.setStatus("current")
_DhcpSnoopVid_Type = VlanIndex
_DhcpSnoopVid_Object = MibTableColumn
dhcpSnoopVid = _DhcpSnoopVid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 11, 1, 1, 3),
    _DhcpSnoopVid_Type()
)
dhcpSnoopVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnoopVid.setStatus("current")
_DhcpSnoopMask_Type = Integer32
_DhcpSnoopMask_Object = MibTableColumn
dhcpSnoopMask = _DhcpSnoopMask_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 11, 1, 1, 4),
    _DhcpSnoopMask_Type()
)
dhcpSnoopMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnoopMask.setStatus("current")
_DhcpSnoopGateway_Type = IpAddress
_DhcpSnoopGateway_Object = MibTableColumn
dhcpSnoopGateway = _DhcpSnoopGateway_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 11, 1, 1, 5),
    _DhcpSnoopGateway_Type()
)
dhcpSnoopGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnoopGateway.setStatus("current")
_DhcpSnoopRouteMap_Type = OctetString
_DhcpSnoopRouteMap_Object = MibTableColumn
dhcpSnoopRouteMap = _DhcpSnoopRouteMap_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 11, 1, 1, 6),
    _DhcpSnoopRouteMap_Type()
)
dhcpSnoopRouteMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnoopRouteMap.setStatus("current")
_DhcpSnoopCounterTable_Object = MibTable
dhcpSnoopCounterTable = _DhcpSnoopCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 11, 2)
)
if mibBuilder.loadTexts:
    dhcpSnoopCounterTable.setStatus("current")
_DhcpSnoopCounterEntry_Object = MibTableRow
dhcpSnoopCounterEntry = _DhcpSnoopCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 11, 2, 1)
)
dhcpSnoopCounterEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dhcpSnoopCounterEntry.setStatus("current")
_DhcpDiscovery_Type = Counter64
_DhcpDiscovery_Object = MibTableColumn
dhcpDiscovery = _DhcpDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 11, 2, 1, 1),
    _DhcpDiscovery_Type()
)
dhcpDiscovery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpDiscovery.setStatus("current")
_DhcpOffer_Type = Counter64
_DhcpOffer_Object = MibTableColumn
dhcpOffer = _DhcpOffer_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 11, 2, 1, 2),
    _DhcpOffer_Type()
)
dhcpOffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpOffer.setStatus("current")
_DhcpRequest_Type = Counter64
_DhcpRequest_Object = MibTableColumn
dhcpRequest = _DhcpRequest_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 11, 2, 1, 3),
    _DhcpRequest_Type()
)
dhcpRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRequest.setStatus("current")
_DhcpAck_Type = Counter64
_DhcpAck_Object = MibTableColumn
dhcpAck = _DhcpAck_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 11, 2, 1, 4),
    _DhcpAck_Type()
)
dhcpAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpAck.setStatus("current")
_DhcpAckBySnoopFull_Type = Counter64
_DhcpAckBySnoopFull_Object = MibTableColumn
dhcpAckBySnoopFull = _DhcpAckBySnoopFull_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 11, 2, 1, 5),
    _DhcpAckBySnoopFull_Type()
)
dhcpAckBySnoopFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpAckBySnoopFull.setStatus("current")
_DhcpRouteTable_Object = MibTable
dhcpRouteTable = _DhcpRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 11, 3)
)
if mibBuilder.loadTexts:
    dhcpRouteTable.setStatus("current")
_DhcpRouteEntry_Object = MibTableRow
dhcpRouteEntry = _DhcpRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 11, 3, 1)
)
dhcpRouteEntry.setIndexNames(
    (0, "E5-121-MIB", "dhcpRouteIndex"),
)
if mibBuilder.loadTexts:
    dhcpRouteEntry.setStatus("current")


class _DhcpRouteIndex_Type(Integer32):
    """Custom type dhcpRouteIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_DhcpRouteIndex_Type.__name__ = "Integer32"
_DhcpRouteIndex_Object = MibTableColumn
dhcpRouteIndex = _DhcpRouteIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 11, 3, 1, 1),
    _DhcpRouteIndex_Type()
)
dhcpRouteIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRouteIndex.setStatus("current")
_DhcpRouteVid_Type = VlanIndex
_DhcpRouteVid_Object = MibTableColumn
dhcpRouteVid = _DhcpRouteVid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 11, 3, 1, 2),
    _DhcpRouteVid_Type()
)
dhcpRouteVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRouteVid.setStatus("current")
_DhcpRouteIP_Type = IpAddress
_DhcpRouteIP_Object = MibTableColumn
dhcpRouteIP = _DhcpRouteIP_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 11, 3, 1, 3),
    _DhcpRouteIP_Type()
)
dhcpRouteIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRouteIP.setStatus("current")
_DhcpRouteMask_Type = Integer32
_DhcpRouteMask_Object = MibTableColumn
dhcpRouteMask = _DhcpRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 11, 3, 1, 4),
    _DhcpRouteMask_Type()
)
dhcpRouteMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRouteMask.setStatus("current")
_DhcpRouteGwIP_Type = IpAddress
_DhcpRouteGwIP_Object = MibTableColumn
dhcpRouteGwIP = _DhcpRouteGwIP_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 11, 3, 1, 5),
    _DhcpRouteGwIP_Type()
)
dhcpRouteGwIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRouteGwIP.setStatus("current")
_PaepvcStats_ObjectIdentity = ObjectIdentity
paepvcStats = _PaepvcStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 12)
)
_PaepvcSessionTable_Object = MibTable
paepvcSessionTable = _PaepvcSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 12, 1)
)
if mibBuilder.loadTexts:
    paepvcSessionTable.setStatus("current")
_PaepvcSessionEntry_Object = MibTableRow
paepvcSessionEntry = _PaepvcSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 12, 1, 1)
)
paepvcSessionEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "E5-121-MIB", "paepvcSessionVpi"),
    (0, "E5-121-MIB", "paepvcSessionVci"),
)
if mibBuilder.loadTexts:
    paepvcSessionEntry.setStatus("current")
_PaepvcSessionVpi_Type = Integer32
_PaepvcSessionVpi_Object = MibTableColumn
paepvcSessionVpi = _PaepvcSessionVpi_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 12, 1, 1, 1),
    _PaepvcSessionVpi_Type()
)
paepvcSessionVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcSessionVpi.setStatus("current")
_PaepvcSessionVci_Type = Integer32
_PaepvcSessionVci_Object = MibTableColumn
paepvcSessionVci = _PaepvcSessionVci_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 12, 1, 1, 2),
    _PaepvcSessionVci_Type()
)
paepvcSessionVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcSessionVci.setStatus("current")


class _PaepvcSessionState_Type(Integer32):
    """Custom type paepvcSessionState based on Integer32"""
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
        *(("down", 1),
          ("pppoe", 2),
          ("ppp", 3),
          ("up", 4))
    )


_PaepvcSessionState_Type.__name__ = "Integer32"
_PaepvcSessionState_Object = MibTableColumn
paepvcSessionState = _PaepvcSessionState_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 12, 1, 1, 3),
    _PaepvcSessionState_Type()
)
paepvcSessionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcSessionState.setStatus("current")
_PaepvcSessionId_Type = Integer32
_PaepvcSessionId_Object = MibTableColumn
paepvcSessionId = _PaepvcSessionId_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 12, 1, 1, 4),
    _PaepvcSessionId_Type()
)
paepvcSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcSessionId.setStatus("current")
_PaepvcSessionUptime_Type = Unsigned32
_PaepvcSessionUptime_Object = MibTableColumn
paepvcSessionUptime = _PaepvcSessionUptime_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 12, 1, 1, 5),
    _PaepvcSessionUptime_Type()
)
paepvcSessionUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcSessionUptime.setStatus("current")
if mibBuilder.loadTexts:
    paepvcSessionUptime.setUnits("second")
_PaepvcSessionacname_Type = DisplayString
_PaepvcSessionacname_Object = MibTableColumn
paepvcSessionacname = _PaepvcSessionacname_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 12, 1, 1, 6),
    _PaepvcSessionacname_Type()
)
paepvcSessionacname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcSessionacname.setStatus("current")
_PaepvcSessionsrvcname_Type = DisplayString
_PaepvcSessionsrvcname_Object = MibTableColumn
paepvcSessionsrvcname = _PaepvcSessionsrvcname_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 12, 1, 1, 7),
    _PaepvcSessionsrvcname_Type()
)
paepvcSessionsrvcname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcSessionsrvcname.setStatus("current")
_PaepvcCountTable_Object = MibTable
paepvcCountTable = _PaepvcCountTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 12, 2)
)
if mibBuilder.loadTexts:
    paepvcCountTable.setStatus("current")
_PaepvcCountEntry_Object = MibTableRow
paepvcCountEntry = _PaepvcCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 12, 2, 1)
)
paepvcCountEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "E5-121-MIB", "paepvcCountVpi"),
    (0, "E5-121-MIB", "paepvcCountVci"),
)
if mibBuilder.loadTexts:
    paepvcCountEntry.setStatus("current")
_PaepvcCountVpi_Type = Integer32
_PaepvcCountVpi_Object = MibTableColumn
paepvcCountVpi = _PaepvcCountVpi_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 12, 2, 1, 1),
    _PaepvcCountVpi_Type()
)
paepvcCountVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcCountVpi.setStatus("current")
_PaepvcCountVci_Type = Integer32
_PaepvcCountVci_Object = MibTableColumn
paepvcCountVci = _PaepvcCountVci_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 12, 2, 1, 2),
    _PaepvcCountVci_Type()
)
paepvcCountVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcCountVci.setStatus("current")
_PaepvcCountPppLcpCfgReqRx_Type = Unsigned32
_PaepvcCountPppLcpCfgReqRx_Object = MibTableColumn
paepvcCountPppLcpCfgReqRx = _PaepvcCountPppLcpCfgReqRx_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 12, 2, 1, 3),
    _PaepvcCountPppLcpCfgReqRx_Type()
)
paepvcCountPppLcpCfgReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcCountPppLcpCfgReqRx.setStatus("current")
_PaepvcCountPppLcpEchoReqRx_Type = Unsigned32
_PaepvcCountPppLcpEchoReqRx_Object = MibTableColumn
paepvcCountPppLcpEchoReqRx = _PaepvcCountPppLcpEchoReqRx_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 12, 2, 1, 4),
    _PaepvcCountPppLcpEchoReqRx_Type()
)
paepvcCountPppLcpEchoReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcCountPppLcpEchoReqRx.setStatus("current")
_PaepvcCountPppLcpEchoReplyRx_Type = Unsigned32
_PaepvcCountPppLcpEchoReplyRx_Object = MibTableColumn
paepvcCountPppLcpEchoReplyRx = _PaepvcCountPppLcpEchoReplyRx_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 12, 2, 1, 5),
    _PaepvcCountPppLcpEchoReplyRx_Type()
)
paepvcCountPppLcpEchoReplyRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcCountPppLcpEchoReplyRx.setStatus("current")
_PaepvcCountPadiTx_Type = Unsigned32
_PaepvcCountPadiTx_Object = MibTableColumn
paepvcCountPadiTx = _PaepvcCountPadiTx_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 12, 2, 1, 6),
    _PaepvcCountPadiTx_Type()
)
paepvcCountPadiTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcCountPadiTx.setStatus("current")
_PaepvcCountPadoRx_Type = Unsigned32
_PaepvcCountPadoRx_Object = MibTableColumn
paepvcCountPadoRx = _PaepvcCountPadoRx_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 12, 2, 1, 7),
    _PaepvcCountPadoRx_Type()
)
paepvcCountPadoRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcCountPadoRx.setStatus("current")
_PaepvcCountPadrTx_Type = Unsigned32
_PaepvcCountPadrTx_Object = MibTableColumn
paepvcCountPadrTx = _PaepvcCountPadrTx_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 12, 2, 1, 8),
    _PaepvcCountPadrTx_Type()
)
paepvcCountPadrTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcCountPadrTx.setStatus("current")
_PaepvcCountPadsRx_Type = Unsigned32
_PaepvcCountPadsRx_Object = MibTableColumn
paepvcCountPadsRx = _PaepvcCountPadsRx_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 12, 2, 1, 9),
    _PaepvcCountPadsRx_Type()
)
paepvcCountPadsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcCountPadsRx.setStatus("current")
_PaepvcCountPadtTx_Type = Unsigned32
_PaepvcCountPadtTx_Object = MibTableColumn
paepvcCountPadtTx = _PaepvcCountPadtTx_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 12, 2, 1, 10),
    _PaepvcCountPadtTx_Type()
)
paepvcCountPadtTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcCountPadtTx.setStatus("current")
_PaepvcCountPadtRx_Type = Unsigned32
_PaepvcCountPadtRx_Object = MibTableColumn
paepvcCountPadtRx = _PaepvcCountPadtRx_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 12, 2, 1, 11),
    _PaepvcCountPadtRx_Type()
)
paepvcCountPadtRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcCountPadtRx.setStatus("current")
_PaepvcCountSrvcnameErrRx_Type = Unsigned32
_PaepvcCountSrvcnameErrRx_Object = MibTableColumn
paepvcCountSrvcnameErrRx = _PaepvcCountSrvcnameErrRx_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 12, 2, 1, 12),
    _PaepvcCountSrvcnameErrRx_Type()
)
paepvcCountSrvcnameErrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcCountSrvcnameErrRx.setStatus("current")
_PaepvcCountAcSystemErrRx_Type = Unsigned32
_PaepvcCountAcSystemErrRx_Object = MibTableColumn
paepvcCountAcSystemErrRx = _PaepvcCountAcSystemErrRx_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 12, 2, 1, 13),
    _PaepvcCountAcSystemErrRx_Type()
)
paepvcCountAcSystemErrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcCountAcSystemErrRx.setStatus("current")
_PaepvcCountGenericErrTx_Type = Unsigned32
_PaepvcCountGenericErrTx_Object = MibTableColumn
paepvcCountGenericErrTx = _PaepvcCountGenericErrTx_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 12, 2, 1, 14),
    _PaepvcCountGenericErrTx_Type()
)
paepvcCountGenericErrTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcCountGenericErrTx.setStatus("current")
_PaepvcCountGenericErrRx_Type = Unsigned32
_PaepvcCountGenericErrRx_Object = MibTableColumn
paepvcCountGenericErrRx = _PaepvcCountGenericErrRx_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 12, 2, 1, 15),
    _PaepvcCountGenericErrRx_Type()
)
paepvcCountGenericErrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcCountGenericErrRx.setStatus("current")
_MacStats_ObjectIdentity = ObjectIdentity
macStats = _MacStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 13)
)
_MacDisplayTarget_Type = Integer32
_MacDisplayTarget_Object = MibScalar
macDisplayTarget = _MacDisplayTarget_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 13, 1),
    _MacDisplayTarget_Type()
)
macDisplayTarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macDisplayTarget.setStatus("current")
_MacTable_Object = MibTable
macTable = _MacTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 13, 2)
)
if mibBuilder.loadTexts:
    macTable.setStatus("current")
_MacEntry_Object = MibTableRow
macEntry = _MacEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 13, 2, 1)
)
macEntry.setIndexNames(
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
    (0, "E5-121-MIB", "macAddress"),
)
if mibBuilder.loadTexts:
    macEntry.setStatus("current")
_MacAddress_Type = MacAddress
_MacAddress_Object = MibTableColumn
macAddress = _MacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 13, 2, 1, 1),
    _MacAddress_Type()
)
macAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macAddress.setStatus("current")
_MacPort_Type = Integer32
_MacPort_Object = MibTableColumn
macPort = _MacPort_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 13, 2, 1, 2),
    _MacPort_Type()
)
macPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macPort.setStatus("current")


class _MacStatus_Type(Integer32):
    """Custom type macStatus based on Integer32"""
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
        *(("other", 1),
          ("invalid", 2),
          ("learned", 3),
          ("self", 4),
          ("mgmt", 5))
    )


_MacStatus_Type.__name__ = "Integer32"
_MacStatus_Object = MibTableColumn
macStatus = _MacStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 13, 2, 1, 3),
    _MacStatus_Type()
)
macStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macStatus.setStatus("current")
_MacVid_Type = VlanIndex
_MacVid_Object = MibTableColumn
macVid = _MacVid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 13, 2, 1, 4),
    _MacVid_Type()
)
macVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macVid.setStatus("current")
_N1macStats_ObjectIdentity = ObjectIdentity
n1macStats = _N1macStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 15)
)
_N1macTable_Object = MibTable
n1macTable = _N1macTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 15, 1)
)
if mibBuilder.loadTexts:
    n1macTable.setStatus("current")
_N1macEntry_Object = MibTableRow
n1macEntry = _N1macEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 15, 1, 1)
)
n1macEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "E5-121-MIB", "n1macProtoVal"),
)
if mibBuilder.loadTexts:
    n1macEntry.setStatus("current")
_N1macProtoVal_Type = Unsigned32
_N1macProtoVal_Object = MibTableColumn
n1macProtoVal = _N1macProtoVal_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 15, 1, 1, 1),
    _N1macProtoVal_Type()
)
n1macProtoVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    n1macProtoVal.setStatus("current")


class _N1macProtoType_Type(Integer32):
    """Custom type n1macProtoType based on Integer32"""
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
        *(("unknown", 1),
          ("ipoe", 2),
          ("ipoaoe", 3),
          ("pppoe", 4),
          ("pppoaoe", 5))
    )


_N1macProtoType_Type.__name__ = "Integer32"
_N1macProtoType_Object = MibTableColumn
n1macProtoType = _N1macProtoType_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 15, 1, 1, 2),
    _N1macProtoType_Type()
)
n1macProtoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    n1macProtoType.setStatus("current")
_N1macMacAddr_Type = MacAddress
_N1macMacAddr_Object = MibTableColumn
n1macMacAddr = _N1macMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 15, 1, 1, 3),
    _N1macMacAddr_Type()
)
n1macMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    n1macMacAddr.setStatus("current")
_EnetStats_ObjectIdentity = ObjectIdentity
enetStats = _EnetStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 16)
)
_EnetPrimaryPort_Type = Integer32
_EnetPrimaryPort_Object = MibScalar
enetPrimaryPort = _EnetPrimaryPort_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 16, 1),
    _EnetPrimaryPort_Type()
)
enetPrimaryPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enetPrimaryPort.setStatus("current")
_EnetSfpInfoTable_Object = MibTable
enetSfpInfoTable = _EnetSfpInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 16, 2)
)
if mibBuilder.loadTexts:
    enetSfpInfoTable.setStatus("current")
_EnetSfpInfoEntry_Object = MibTableRow
enetSfpInfoEntry = _EnetSfpInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 16, 2, 1)
)
enetSfpInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    enetSfpInfoEntry.setStatus("current")


class _EnetSfpInfoTxpower_Type(Integer32):
    """Custom type enetSfpInfoTxpower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EnetSfpInfoTxpower_Type.__name__ = "Integer32"
_EnetSfpInfoTxpower_Object = MibTableColumn
enetSfpInfoTxpower = _EnetSfpInfoTxpower_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 16, 2, 1, 1),
    _EnetSfpInfoTxpower_Type()
)
enetSfpInfoTxpower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enetSfpInfoTxpower.setStatus("current")
if mibBuilder.loadTexts:
    enetSfpInfoTxpower.setUnits("10^-4 mW")


class _EnetSfpInfoRxpower_Type(Integer32):
    """Custom type enetSfpInfoRxpower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EnetSfpInfoRxpower_Type.__name__ = "Integer32"
_EnetSfpInfoRxpower_Object = MibTableColumn
enetSfpInfoRxpower = _EnetSfpInfoRxpower_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 16, 2, 1, 2),
    _EnetSfpInfoRxpower_Type()
)
enetSfpInfoRxpower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enetSfpInfoRxpower.setStatus("current")
if mibBuilder.loadTexts:
    enetSfpInfoRxpower.setUnits("10^-4 C")


class _EnetSfpInfoTemperature_Type(Integer32):
    """Custom type enetSfpInfoTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1280000, 1280000),
    )


_EnetSfpInfoTemperature_Type.__name__ = "Integer32"
_EnetSfpInfoTemperature_Object = MibTableColumn
enetSfpInfoTemperature = _EnetSfpInfoTemperature_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 16, 2, 1, 3),
    _EnetSfpInfoTemperature_Type()
)
enetSfpInfoTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enetSfpInfoTemperature.setStatus("current")
if mibBuilder.loadTexts:
    enetSfpInfoTemperature.setUnits("10^-4 C")


class _EnetSfpInfoTxBias_Type(Integer32):
    """Custom type enetSfpInfoTxBias based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 131000),
    )


_EnetSfpInfoTxBias_Type.__name__ = "Integer32"
_EnetSfpInfoTxBias_Object = MibTableColumn
enetSfpInfoTxBias = _EnetSfpInfoTxBias_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 16, 2, 1, 4),
    _EnetSfpInfoTxBias_Type()
)
enetSfpInfoTxBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enetSfpInfoTxBias.setStatus("current")
if mibBuilder.loadTexts:
    enetSfpInfoTxBias.setUnits("10^-3 mA")


class _EnetSfpInfoVoltage_Type(Integer32):
    """Custom type enetSfpInfoVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65000),
    )


_EnetSfpInfoVoltage_Type.__name__ = "Integer32"
_EnetSfpInfoVoltage_Object = MibTableColumn
enetSfpInfoVoltage = _EnetSfpInfoVoltage_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 16, 2, 1, 5),
    _EnetSfpInfoVoltage_Type()
)
enetSfpInfoVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enetSfpInfoVoltage.setStatus("current")
if mibBuilder.loadTexts:
    enetSfpInfoVoltage.setUnits("0.1mV")
_VdslStats_ObjectIdentity = ObjectIdentity
vdslStats = _VdslStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 17)
)
_VdslLineStatsTable_Object = MibTable
vdslLineStatsTable = _VdslLineStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 17, 2)
)
if mibBuilder.loadTexts:
    vdslLineStatsTable.setStatus("current")
_VdslLineStatsEntry_Object = MibTableRow
vdslLineStatsEntry = _VdslLineStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 17, 2, 1)
)
vdslLineStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    vdslLineStatsEntry.setStatus("current")
_VdslLineStatsVtucBits1_Type = OctetString
_VdslLineStatsVtucBits1_Object = MibTableColumn
vdslLineStatsVtucBits1 = _VdslLineStatsVtucBits1_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 17, 2, 1, 1),
    _VdslLineStatsVtucBits1_Type()
)
vdslLineStatsVtucBits1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineStatsVtucBits1.setStatus("current")
_VdslLineStatsVtucBits2_Type = OctetString
_VdslLineStatsVtucBits2_Object = MibTableColumn
vdslLineStatsVtucBits2 = _VdslLineStatsVtucBits2_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 17, 2, 1, 2),
    _VdslLineStatsVtucBits2_Type()
)
vdslLineStatsVtucBits2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineStatsVtucBits2.setStatus("current")
_VdslLineStatsVtucBits3_Type = OctetString
_VdslLineStatsVtucBits3_Object = MibTableColumn
vdslLineStatsVtucBits3 = _VdslLineStatsVtucBits3_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 17, 2, 1, 3),
    _VdslLineStatsVtucBits3_Type()
)
vdslLineStatsVtucBits3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineStatsVtucBits3.setStatus("current")
_VdslLineStatsVtucBits4_Type = OctetString
_VdslLineStatsVtucBits4_Object = MibTableColumn
vdslLineStatsVtucBits4 = _VdslLineStatsVtucBits4_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 17, 2, 1, 4),
    _VdslLineStatsVtucBits4_Type()
)
vdslLineStatsVtucBits4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineStatsVtucBits4.setStatus("current")
_VdslLineStatsVturBits1_Type = OctetString
_VdslLineStatsVturBits1_Object = MibTableColumn
vdslLineStatsVturBits1 = _VdslLineStatsVturBits1_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 17, 2, 1, 5),
    _VdslLineStatsVturBits1_Type()
)
vdslLineStatsVturBits1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineStatsVturBits1.setStatus("current")
_VdslLineStatsVturBits2_Type = OctetString
_VdslLineStatsVturBits2_Object = MibTableColumn
vdslLineStatsVturBits2 = _VdslLineStatsVturBits2_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 17, 2, 1, 6),
    _VdslLineStatsVturBits2_Type()
)
vdslLineStatsVturBits2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineStatsVturBits2.setStatus("current")
_VdslLineStatsVturBits3_Type = OctetString
_VdslLineStatsVturBits3_Object = MibTableColumn
vdslLineStatsVturBits3 = _VdslLineStatsVturBits3_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 17, 2, 1, 7),
    _VdslLineStatsVturBits3_Type()
)
vdslLineStatsVturBits3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineStatsVturBits3.setStatus("current")
_VdslLineStatsVturBits4_Type = OctetString
_VdslLineStatsVturBits4_Object = MibTableColumn
vdslLineStatsVturBits4 = _VdslLineStatsVturBits4_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 17, 2, 1, 8),
    _VdslLineStatsVturBits4_Type()
)
vdslLineStatsVturBits4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineStatsVturBits4.setStatus("current")
_VdslLineStatsVtucGain1_Type = OctetString
_VdslLineStatsVtucGain1_Object = MibTableColumn
vdslLineStatsVtucGain1 = _VdslLineStatsVtucGain1_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 17, 2, 1, 9),
    _VdslLineStatsVtucGain1_Type()
)
vdslLineStatsVtucGain1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineStatsVtucGain1.setStatus("current")
_VdslLineStatsVtucGain2_Type = OctetString
_VdslLineStatsVtucGain2_Object = MibTableColumn
vdslLineStatsVtucGain2 = _VdslLineStatsVtucGain2_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 17, 2, 1, 10),
    _VdslLineStatsVtucGain2_Type()
)
vdslLineStatsVtucGain2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineStatsVtucGain2.setStatus("current")
_VdslLineStatsVtucGain3_Type = OctetString
_VdslLineStatsVtucGain3_Object = MibTableColumn
vdslLineStatsVtucGain3 = _VdslLineStatsVtucGain3_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 17, 2, 1, 11),
    _VdslLineStatsVtucGain3_Type()
)
vdslLineStatsVtucGain3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineStatsVtucGain3.setStatus("current")
_VdslLineStatsVtucGain4_Type = OctetString
_VdslLineStatsVtucGain4_Object = MibTableColumn
vdslLineStatsVtucGain4 = _VdslLineStatsVtucGain4_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 17, 2, 1, 12),
    _VdslLineStatsVtucGain4_Type()
)
vdslLineStatsVtucGain4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineStatsVtucGain4.setStatus("current")
_VdslLineStatsVtucGain5_Type = OctetString
_VdslLineStatsVtucGain5_Object = MibTableColumn
vdslLineStatsVtucGain5 = _VdslLineStatsVtucGain5_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 17, 2, 1, 13),
    _VdslLineStatsVtucGain5_Type()
)
vdslLineStatsVtucGain5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineStatsVtucGain5.setStatus("current")
_VdslLineStatsVtucGain6_Type = OctetString
_VdslLineStatsVtucGain6_Object = MibTableColumn
vdslLineStatsVtucGain6 = _VdslLineStatsVtucGain6_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 17, 2, 1, 14),
    _VdslLineStatsVtucGain6_Type()
)
vdslLineStatsVtucGain6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineStatsVtucGain6.setStatus("current")
_VdslLineStatsVtucGain7_Type = OctetString
_VdslLineStatsVtucGain7_Object = MibTableColumn
vdslLineStatsVtucGain7 = _VdslLineStatsVtucGain7_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 17, 2, 1, 15),
    _VdslLineStatsVtucGain7_Type()
)
vdslLineStatsVtucGain7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineStatsVtucGain7.setStatus("current")
_VdslLineStatsVtucGain8_Type = OctetString
_VdslLineStatsVtucGain8_Object = MibTableColumn
vdslLineStatsVtucGain8 = _VdslLineStatsVtucGain8_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 17, 2, 1, 16),
    _VdslLineStatsVtucGain8_Type()
)
vdslLineStatsVtucGain8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineStatsVtucGain8.setStatus("current")
_VdslLineStatsVturGain1_Type = OctetString
_VdslLineStatsVturGain1_Object = MibTableColumn
vdslLineStatsVturGain1 = _VdslLineStatsVturGain1_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 17, 2, 1, 17),
    _VdslLineStatsVturGain1_Type()
)
vdslLineStatsVturGain1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineStatsVturGain1.setStatus("current")
_VdslLineStatsVturGain2_Type = OctetString
_VdslLineStatsVturGain2_Object = MibTableColumn
vdslLineStatsVturGain2 = _VdslLineStatsVturGain2_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 17, 2, 1, 18),
    _VdslLineStatsVturGain2_Type()
)
vdslLineStatsVturGain2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineStatsVturGain2.setStatus("current")
_VdslLineStatsVturGain3_Type = OctetString
_VdslLineStatsVturGain3_Object = MibTableColumn
vdslLineStatsVturGain3 = _VdslLineStatsVturGain3_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 17, 2, 1, 19),
    _VdslLineStatsVturGain3_Type()
)
vdslLineStatsVturGain3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineStatsVturGain3.setStatus("current")
_VdslLineStatsVturGain4_Type = OctetString
_VdslLineStatsVturGain4_Object = MibTableColumn
vdslLineStatsVturGain4 = _VdslLineStatsVturGain4_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 17, 2, 1, 20),
    _VdslLineStatsVturGain4_Type()
)
vdslLineStatsVturGain4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineStatsVturGain4.setStatus("current")
_VdslLineStatsVturGain5_Type = OctetString
_VdslLineStatsVturGain5_Object = MibTableColumn
vdslLineStatsVturGain5 = _VdslLineStatsVturGain5_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 17, 2, 1, 21),
    _VdslLineStatsVturGain5_Type()
)
vdslLineStatsVturGain5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineStatsVturGain5.setStatus("current")
_VdslLineStatsVturGain6_Type = OctetString
_VdslLineStatsVturGain6_Object = MibTableColumn
vdslLineStatsVturGain6 = _VdslLineStatsVturGain6_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 17, 2, 1, 22),
    _VdslLineStatsVturGain6_Type()
)
vdslLineStatsVturGain6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineStatsVturGain6.setStatus("current")
_VdslLineStatsVturGain7_Type = OctetString
_VdslLineStatsVturGain7_Object = MibTableColumn
vdslLineStatsVturGain7 = _VdslLineStatsVturGain7_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 17, 2, 1, 23),
    _VdslLineStatsVturGain7_Type()
)
vdslLineStatsVturGain7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineStatsVturGain7.setStatus("current")
_VdslLineStatsVturGain8_Type = OctetString
_VdslLineStatsVturGain8_Object = MibTableColumn
vdslLineStatsVturGain8 = _VdslLineStatsVturGain8_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 17, 2, 1, 24),
    _VdslLineStatsVturGain8_Type()
)
vdslLineStatsVturGain8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineStatsVturGain8.setStatus("current")
_VdslLineStatsVtucHlog_Type = OctetString
_VdslLineStatsVtucHlog_Object = MibTableColumn
vdslLineStatsVtucHlog = _VdslLineStatsVtucHlog_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 17, 2, 1, 25),
    _VdslLineStatsVtucHlog_Type()
)
vdslLineStatsVtucHlog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineStatsVtucHlog.setStatus("current")
_VdslLineStatsVturHlog_Type = OctetString
_VdslLineStatsVturHlog_Object = MibTableColumn
vdslLineStatsVturHlog = _VdslLineStatsVturHlog_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 17, 2, 1, 26),
    _VdslLineStatsVturHlog_Type()
)
vdslLineStatsVturHlog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineStatsVturHlog.setStatus("current")
_VdslLineStatsVtucQln_Type = OctetString
_VdslLineStatsVtucQln_Object = MibTableColumn
vdslLineStatsVtucQln = _VdslLineStatsVtucQln_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 17, 2, 1, 27),
    _VdslLineStatsVtucQln_Type()
)
vdslLineStatsVtucQln.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineStatsVtucQln.setStatus("current")
_VdslLineStatsVturQln_Type = OctetString
_VdslLineStatsVturQln_Object = MibTableColumn
vdslLineStatsVturQln = _VdslLineStatsVturQln_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 17, 2, 1, 28),
    _VdslLineStatsVturQln_Type()
)
vdslLineStatsVturQln.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineStatsVturQln.setStatus("current")
_VdslLineStatsVtucSnr_Type = OctetString
_VdslLineStatsVtucSnr_Object = MibTableColumn
vdslLineStatsVtucSnr = _VdslLineStatsVtucSnr_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 17, 2, 1, 29),
    _VdslLineStatsVtucSnr_Type()
)
vdslLineStatsVtucSnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineStatsVtucSnr.setStatus("current")
_VdslLineStatsVturSnr_Type = OctetString
_VdslLineStatsVturSnr_Object = MibTableColumn
vdslLineStatsVturSnr = _VdslLineStatsVturSnr_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 17, 2, 1, 30),
    _VdslLineStatsVturSnr_Type()
)
vdslLineStatsVturSnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineStatsVturSnr.setStatus("current")
_VdslLineStatsVtucTssi_Type = OctetString
_VdslLineStatsVtucTssi_Object = MibTableColumn
vdslLineStatsVtucTssi = _VdslLineStatsVtucTssi_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 17, 2, 1, 31),
    _VdslLineStatsVtucTssi_Type()
)
vdslLineStatsVtucTssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineStatsVtucTssi.setStatus("current")
_VdslLineStatsVturTssi_Type = OctetString
_VdslLineStatsVturTssi_Object = MibTableColumn
vdslLineStatsVturTssi = _VdslLineStatsVturTssi_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 17, 2, 1, 32),
    _VdslLineStatsVturTssi_Type()
)
vdslLineStatsVturTssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineStatsVturTssi.setStatus("current")


class _VdslLineStatsProtocol_Type(Integer32):
    """Custom type vdslLineStatsProtocol based on Integer32"""
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
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("vdsl8a", 2),
          ("vdsl8b", 3),
          ("vdsl8c", 4),
          ("vdsl8d", 5),
          ("vdsl12a", 6),
          ("vdsl12b", 7),
          ("vdsl17a", 8),
          ("gdmt", 9),
          ("glite", 10),
          ("adsl2", 11),
          ("adsl2plus", 12),
          ("t1413", 13))
    )


_VdslLineStatsProtocol_Type.__name__ = "Integer32"
_VdslLineStatsProtocol_Object = MibTableColumn
vdslLineStatsProtocol = _VdslLineStatsProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 17, 2, 1, 33),
    _VdslLineStatsProtocol_Type()
)
vdslLineStatsProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineStatsProtocol.setStatus("current")
_VoipStats_ObjectIdentity = ObjectIdentity
voipStats = _VoipStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 18)
)
_VoipLineStatusTable_Object = MibTable
voipLineStatusTable = _VoipLineStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 18, 1)
)
if mibBuilder.loadTexts:
    voipLineStatusTable.setStatus("current")
_VoipLineStatusEntry_Object = MibTableRow
voipLineStatusEntry = _VoipLineStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 18, 1, 1)
)
voipLineStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    voipLineStatusEntry.setStatus("current")


class _VoipLineStatusPhoneStatus_Type(Integer32):
    """Custom type voipLineStatusPhoneStatus based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("onHook", 2),
          ("offHook", 3),
          ("ringing", 4),
          ("powerCutDown", 5),
          ("testing", 6),
          ("fault", 7),
          ("bad", 8),
          ("uninitialized", 9))
    )


_VoipLineStatusPhoneStatus_Type.__name__ = "Integer32"
_VoipLineStatusPhoneStatus_Object = MibTableColumn
voipLineStatusPhoneStatus = _VoipLineStatusPhoneStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 18, 1, 1, 1),
    _VoipLineStatusPhoneStatus_Type()
)
voipLineStatusPhoneStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipLineStatusPhoneStatus.setStatus("current")


class _VoipLineStatusServiceStatus_Type(Integer32):
    """Custom type voipLineStatusServiceStatus based on Integer32"""
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
              10,
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("outOfService", 2),
          ("idle", 3),
          ("waitingForDialing", 4),
          ("dialingOut", 5),
          ("ringing", 6),
          ("conversationCaller", 7),
          ("conversationCallee", 8),
          ("faxModemCaller", 9),
          ("faxModemCallee", 10),
          ("waitingForOnHook", 11),
          ("dialingTimeout", 12),
          ("alertingOffHook", 13),
          ("powerCutDown", 14))
    )


_VoipLineStatusServiceStatus_Type.__name__ = "Integer32"
_VoipLineStatusServiceStatus_Object = MibTableColumn
voipLineStatusServiceStatus = _VoipLineStatusServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 18, 1, 1, 2),
    _VoipLineStatusServiceStatus_Type()
)
voipLineStatusServiceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipLineStatusServiceStatus.setStatus("current")
_VoipLineInfoTable_Object = MibTable
voipLineInfoTable = _VoipLineInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 18, 2)
)
if mibBuilder.loadTexts:
    voipLineInfoTable.setStatus("current")
_VoipLineInfoEntry_Object = MibTableRow
voipLineInfoEntry = _VoipLineInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 18, 2, 1)
)
voipLineInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    voipLineInfoEntry.setStatus("current")
_VoipLineInfoSipLocalUri_Type = OctetString
_VoipLineInfoSipLocalUri_Object = MibTableColumn
voipLineInfoSipLocalUri = _VoipLineInfoSipLocalUri_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 18, 2, 1, 1),
    _VoipLineInfoSipLocalUri_Type()
)
voipLineInfoSipLocalUri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipLineInfoSipLocalUri.setStatus("current")
_VoipLineInfoSipRemoteUri_Type = OctetString
_VoipLineInfoSipRemoteUri_Object = MibTableColumn
voipLineInfoSipRemoteUri = _VoipLineInfoSipRemoteUri_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 18, 2, 1, 2),
    _VoipLineInfoSipRemoteUri_Type()
)
voipLineInfoSipRemoteUri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipLineInfoSipRemoteUri.setStatus("current")
_VoipLineInfoRtpTxCodecType_Type = OctetString
_VoipLineInfoRtpTxCodecType_Object = MibTableColumn
voipLineInfoRtpTxCodecType = _VoipLineInfoRtpTxCodecType_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 18, 2, 1, 3),
    _VoipLineInfoRtpTxCodecType_Type()
)
voipLineInfoRtpTxCodecType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipLineInfoRtpTxCodecType.setStatus("current")
_VoipLineInfoRtpRxCodecType_Type = OctetString
_VoipLineInfoRtpRxCodecType_Object = MibTableColumn
voipLineInfoRtpRxCodecType = _VoipLineInfoRtpRxCodecType_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 18, 2, 1, 4),
    _VoipLineInfoRtpRxCodecType_Type()
)
voipLineInfoRtpRxCodecType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipLineInfoRtpRxCodecType.setStatus("current")
_VoipLineInfoRtpTxPt_Type = Integer32
_VoipLineInfoRtpTxPt_Object = MibTableColumn
voipLineInfoRtpTxPt = _VoipLineInfoRtpTxPt_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 18, 2, 1, 5),
    _VoipLineInfoRtpTxPt_Type()
)
voipLineInfoRtpTxPt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipLineInfoRtpTxPt.setStatus("current")
_VoipLineInfoRtpRxPt_Type = Integer32
_VoipLineInfoRtpRxPt_Object = MibTableColumn
voipLineInfoRtpRxPt = _VoipLineInfoRtpRxPt_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 18, 2, 1, 6),
    _VoipLineInfoRtpRxPt_Type()
)
voipLineInfoRtpRxPt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipLineInfoRtpRxPt.setStatus("current")
_VoipLineInfoRtpLocalIp_Type = IpAddress
_VoipLineInfoRtpLocalIp_Object = MibTableColumn
voipLineInfoRtpLocalIp = _VoipLineInfoRtpLocalIp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 18, 2, 1, 7),
    _VoipLineInfoRtpLocalIp_Type()
)
voipLineInfoRtpLocalIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipLineInfoRtpLocalIp.setStatus("current")
_VoipLineInfoRtpRemoteIp_Type = IpAddress
_VoipLineInfoRtpRemoteIp_Object = MibTableColumn
voipLineInfoRtpRemoteIp = _VoipLineInfoRtpRemoteIp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 18, 2, 1, 8),
    _VoipLineInfoRtpRemoteIp_Type()
)
voipLineInfoRtpRemoteIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipLineInfoRtpRemoteIp.setStatus("current")
_VoipLineInfoRtpLocalPort_Type = Integer32
_VoipLineInfoRtpLocalPort_Object = MibTableColumn
voipLineInfoRtpLocalPort = _VoipLineInfoRtpLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 18, 2, 1, 9),
    _VoipLineInfoRtpLocalPort_Type()
)
voipLineInfoRtpLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipLineInfoRtpLocalPort.setStatus("current")
_VoipLineInfoRtpRemotePort_Type = Integer32
_VoipLineInfoRtpRemotePort_Object = MibTableColumn
voipLineInfoRtpRemotePort = _VoipLineInfoRtpRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 18, 2, 1, 10),
    _VoipLineInfoRtpRemotePort_Type()
)
voipLineInfoRtpRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipLineInfoRtpRemotePort.setStatus("current")
_VoipLineInfoSipLocalUri2_Type = OctetString
_VoipLineInfoSipLocalUri2_Object = MibTableColumn
voipLineInfoSipLocalUri2 = _VoipLineInfoSipLocalUri2_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 18, 2, 1, 11),
    _VoipLineInfoSipLocalUri2_Type()
)
voipLineInfoSipLocalUri2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipLineInfoSipLocalUri2.setStatus("current")
_VoipLineInfoSipRemoteUri2_Type = OctetString
_VoipLineInfoSipRemoteUri2_Object = MibTableColumn
voipLineInfoSipRemoteUri2 = _VoipLineInfoSipRemoteUri2_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 18, 2, 1, 12),
    _VoipLineInfoSipRemoteUri2_Type()
)
voipLineInfoSipRemoteUri2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipLineInfoSipRemoteUri2.setStatus("current")
_VoipLineInfoRtpTxCodecType2_Type = OctetString
_VoipLineInfoRtpTxCodecType2_Object = MibTableColumn
voipLineInfoRtpTxCodecType2 = _VoipLineInfoRtpTxCodecType2_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 18, 2, 1, 13),
    _VoipLineInfoRtpTxCodecType2_Type()
)
voipLineInfoRtpTxCodecType2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipLineInfoRtpTxCodecType2.setStatus("current")
_VoipLineInfoRtpRxCodecType2_Type = OctetString
_VoipLineInfoRtpRxCodecType2_Object = MibTableColumn
voipLineInfoRtpRxCodecType2 = _VoipLineInfoRtpRxCodecType2_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 18, 2, 1, 14),
    _VoipLineInfoRtpRxCodecType2_Type()
)
voipLineInfoRtpRxCodecType2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipLineInfoRtpRxCodecType2.setStatus("current")
_VoipLineInfoRtpTxPt2_Type = Integer32
_VoipLineInfoRtpTxPt2_Object = MibTableColumn
voipLineInfoRtpTxPt2 = _VoipLineInfoRtpTxPt2_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 18, 2, 1, 15),
    _VoipLineInfoRtpTxPt2_Type()
)
voipLineInfoRtpTxPt2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipLineInfoRtpTxPt2.setStatus("current")
_VoipLineInfoRtpRxPt2_Type = Integer32
_VoipLineInfoRtpRxPt2_Object = MibTableColumn
voipLineInfoRtpRxPt2 = _VoipLineInfoRtpRxPt2_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 18, 2, 1, 16),
    _VoipLineInfoRtpRxPt2_Type()
)
voipLineInfoRtpRxPt2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipLineInfoRtpRxPt2.setStatus("current")
_VoipLineInfoRtpLocalIp2_Type = IpAddress
_VoipLineInfoRtpLocalIp2_Object = MibTableColumn
voipLineInfoRtpLocalIp2 = _VoipLineInfoRtpLocalIp2_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 18, 2, 1, 17),
    _VoipLineInfoRtpLocalIp2_Type()
)
voipLineInfoRtpLocalIp2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipLineInfoRtpLocalIp2.setStatus("current")
_VoipLineInfoRtpRemoteIp2_Type = IpAddress
_VoipLineInfoRtpRemoteIp2_Object = MibTableColumn
voipLineInfoRtpRemoteIp2 = _VoipLineInfoRtpRemoteIp2_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 18, 2, 1, 18),
    _VoipLineInfoRtpRemoteIp2_Type()
)
voipLineInfoRtpRemoteIp2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipLineInfoRtpRemoteIp2.setStatus("current")
_VoipLineInfoRtpLocalPort2_Type = Integer32
_VoipLineInfoRtpLocalPort2_Object = MibTableColumn
voipLineInfoRtpLocalPort2 = _VoipLineInfoRtpLocalPort2_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 18, 2, 1, 19),
    _VoipLineInfoRtpLocalPort2_Type()
)
voipLineInfoRtpLocalPort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipLineInfoRtpLocalPort2.setStatus("current")
_VoipLineInfoRtpRemotePort2_Type = Integer32
_VoipLineInfoRtpRemotePort2_Object = MibTableColumn
voipLineInfoRtpRemotePort2 = _VoipLineInfoRtpRemotePort2_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 18, 2, 1, 20),
    _VoipLineInfoRtpRemotePort2_Type()
)
voipLineInfoRtpRemotePort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipLineInfoRtpRemotePort2.setStatus("current")
_VoipH248Status_ObjectIdentity = ObjectIdentity
voipH248Status = _VoipH248Status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 18, 3)
)
_VoipH248StatusMgName_Type = OctetString
_VoipH248StatusMgName_Object = MibScalar
voipH248StatusMgName = _VoipH248StatusMgName_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 18, 3, 1),
    _VoipH248StatusMgName_Type()
)
voipH248StatusMgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipH248StatusMgName.setStatus("current")


class _VoipH248StatusMgStatus_Type(Integer32):
    """Custom type voipH248StatusMgStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("registering", 2),
          ("registered", 3),
          ("unregistering", 4),
          ("unregistered", 5),
          ("disconnected", 6),
          ("disabledByMGC", 7))
    )


_VoipH248StatusMgStatus_Type.__name__ = "Integer32"
_VoipH248StatusMgStatus_Object = MibScalar
voipH248StatusMgStatus = _VoipH248StatusMgStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 18, 3, 2),
    _VoipH248StatusMgStatus_Type()
)
voipH248StatusMgStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipH248StatusMgStatus.setStatus("current")
_VoipActiveCallStat_ObjectIdentity = ObjectIdentity
voipActiveCallStat = _VoipActiveCallStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 18, 4)
)
_VoipActiveCallStatCurrentActiveCalls_Type = Integer32
_VoipActiveCallStatCurrentActiveCalls_Object = MibScalar
voipActiveCallStatCurrentActiveCalls = _VoipActiveCallStatCurrentActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 18, 4, 1),
    _VoipActiveCallStatCurrentActiveCalls_Type()
)
voipActiveCallStatCurrentActiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipActiveCallStatCurrentActiveCalls.setStatus("current")
_VoipActiveCallStatFailAttempts_Type = Integer32
_VoipActiveCallStatFailAttempts_Object = MibScalar
voipActiveCallStatFailAttempts = _VoipActiveCallStatFailAttempts_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 18, 4, 2),
    _VoipActiveCallStatFailAttempts_Type()
)
voipActiveCallStatFailAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipActiveCallStatFailAttempts.setStatus("current")
_VoipActiveCallStatClear_Type = Integer32
_VoipActiveCallStatClear_Object = MibScalar
voipActiveCallStatClear = _VoipActiveCallStatClear_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 18, 4, 3),
    _VoipActiveCallStatClear_Type()
)
voipActiveCallStatClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipActiveCallStatClear.setStatus("current")
_MacffStats_ObjectIdentity = ObjectIdentity
macffStats = _MacffStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 19)
)
_MacFfStatsTable_Object = MibTable
macFfStatsTable = _MacFfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 19, 1)
)
if mibBuilder.loadTexts:
    macFfStatsTable.setStatus("current")
_MacFfStatsEntry_Object = MibTableRow
macFfStatsEntry = _MacFfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 19, 1, 1)
)
macFfStatsEntry.setIndexNames(
    (0, "E5-121-MIB", "macFfStatsIndex"),
)
if mibBuilder.loadTexts:
    macFfStatsEntry.setStatus("current")
_MacFfStatsIndex_Type = Integer32
_MacFfStatsIndex_Object = MibTableColumn
macFfStatsIndex = _MacFfStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 19, 1, 1, 1),
    _MacFfStatsIndex_Type()
)
macFfStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macFfStatsIndex.setStatus("current")
_MacFfStatsVid_Type = VlanIndex
_MacFfStatsVid_Object = MibTableColumn
macFfStatsVid = _MacFfStatsVid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 19, 1, 1, 2),
    _MacFfStatsVid_Type()
)
macFfStatsVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macFfStatsVid.setStatus("current")
_MacFfStatsArIP_Type = IpAddress
_MacFfStatsArIP_Object = MibTableColumn
macFfStatsArIP = _MacFfStatsArIP_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 19, 1, 1, 3),
    _MacFfStatsArIP_Type()
)
macFfStatsArIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macFfStatsArIP.setStatus("current")
_MacFfStatsSrcIP_Type = IpAddress
_MacFfStatsSrcIP_Object = MibTableColumn
macFfStatsSrcIP = _MacFfStatsSrcIP_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 19, 1, 1, 4),
    _MacFfStatsSrcIP_Type()
)
macFfStatsSrcIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macFfStatsSrcIP.setStatus("current")
_MacFfStatsSrcMask_Type = Integer32
_MacFfStatsSrcMask_Object = MibTableColumn
macFfStatsSrcMask = _MacFfStatsSrcMask_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 19, 1, 1, 5),
    _MacFfStatsSrcMask_Type()
)
macFfStatsSrcMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macFfStatsSrcMask.setStatus("current")
_MacFfArpTable_Object = MibTable
macFfArpTable = _MacFfArpTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 19, 2)
)
if mibBuilder.loadTexts:
    macFfArpTable.setStatus("current")
_MacFfArpEntry_Object = MibTableRow
macFfArpEntry = _MacFfArpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 19, 2, 1)
)
macFfArpEntry.setIndexNames(
    (0, "E5-121-MIB", "macFfArpVid"),
    (0, "E5-121-MIB", "macFfArpIP"),
)
if mibBuilder.loadTexts:
    macFfArpEntry.setStatus("current")
_MacFfArpVid_Type = VlanIndex
_MacFfArpVid_Object = MibTableColumn
macFfArpVid = _MacFfArpVid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 19, 2, 1, 1),
    _MacFfArpVid_Type()
)
macFfArpVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macFfArpVid.setStatus("current")
_MacFfArpIP_Type = IpAddress
_MacFfArpIP_Object = MibTableColumn
macFfArpIP = _MacFfArpIP_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 19, 2, 1, 2),
    _MacFfArpIP_Type()
)
macFfArpIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macFfArpIP.setStatus("current")
_MacFfArpPort_Type = Integer32
_MacFfArpPort_Object = MibTableColumn
macFfArpPort = _MacFfArpPort_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 19, 2, 1, 3),
    _MacFfArpPort_Type()
)
macFfArpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macFfArpPort.setStatus("current")
_MacFfArpMac_Type = PhysAddress
_MacFfArpMac_Object = MibTableColumn
macFfArpMac = _MacFfArpMac_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 19, 2, 1, 4),
    _MacFfArpMac_Type()
)
macFfArpMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macFfArpMac.setStatus("current")
_MacFfArpCounterTable_Object = MibTable
macFfArpCounterTable = _MacFfArpCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 19, 3)
)
if mibBuilder.loadTexts:
    macFfArpCounterTable.setStatus("current")
_MacFfArpCounterEntry_Object = MibTableRow
macFfArpCounterEntry = _MacFfArpCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 19, 3, 1)
)
macFfArpCounterEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    macFfArpCounterEntry.setStatus("current")
_MacFfArpCounterRequestTX_Type = Counter32
_MacFfArpCounterRequestTX_Object = MibTableColumn
macFfArpCounterRequestTX = _MacFfArpCounterRequestTX_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 19, 3, 1, 1),
    _MacFfArpCounterRequestTX_Type()
)
macFfArpCounterRequestTX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macFfArpCounterRequestTX.setStatus("current")
_MacFfArpCounterRequestRX_Type = Counter32
_MacFfArpCounterRequestRX_Object = MibTableColumn
macFfArpCounterRequestRX = _MacFfArpCounterRequestRX_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 19, 3, 1, 2),
    _MacFfArpCounterRequestRX_Type()
)
macFfArpCounterRequestRX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macFfArpCounterRequestRX.setStatus("current")
_MacFfArpCounterRequestRXDrop_Type = Counter32
_MacFfArpCounterRequestRXDrop_Object = MibTableColumn
macFfArpCounterRequestRXDrop = _MacFfArpCounterRequestRXDrop_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 19, 3, 1, 3),
    _MacFfArpCounterRequestRXDrop_Type()
)
macFfArpCounterRequestRXDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macFfArpCounterRequestRXDrop.setStatus("current")
_MacFfArpCounterReplyTX_Type = Counter32
_MacFfArpCounterReplyTX_Object = MibTableColumn
macFfArpCounterReplyTX = _MacFfArpCounterReplyTX_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 19, 3, 1, 4),
    _MacFfArpCounterReplyTX_Type()
)
macFfArpCounterReplyTX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macFfArpCounterReplyTX.setStatus("current")
_MacFfArpCounterReplyRX_Type = Counter32
_MacFfArpCounterReplyRX_Object = MibTableColumn
macFfArpCounterReplyRX = _MacFfArpCounterReplyRX_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 19, 3, 1, 5),
    _MacFfArpCounterReplyRX_Type()
)
macFfArpCounterReplyRX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macFfArpCounterReplyRX.setStatus("current")
_MacFfArpCounterReplyRXDrop_Type = Counter32
_MacFfArpCounterReplyRXDrop_Object = MibTableColumn
macFfArpCounterReplyRXDrop = _MacFfArpCounterReplyRXDrop_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 19, 3, 1, 6),
    _MacFfArpCounterReplyRXDrop_Type()
)
macFfArpCounterReplyRXDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macFfArpCounterReplyRXDrop.setStatus("current")
_AdslStats_ObjectIdentity = ObjectIdentity
adslStats = _AdslStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 20)
)
_AdslPortUtilTable_Object = MibTable
adslPortUtilTable = _AdslPortUtilTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 20, 1)
)
if mibBuilder.loadTexts:
    adslPortUtilTable.setStatus("current")
_AdslPortUtilEntry_Object = MibTableRow
adslPortUtilEntry = _AdslPortUtilEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 20, 1, 1)
)
adslPortUtilEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adslPortUtilEntry.setStatus("current")


class _AdslPortUtilTx_Type(Integer32):
    """Custom type adslPortUtilTx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AdslPortUtilTx_Type.__name__ = "Integer32"
_AdslPortUtilTx_Object = MibTableColumn
adslPortUtilTx = _AdslPortUtilTx_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 20, 1, 1, 1),
    _AdslPortUtilTx_Type()
)
adslPortUtilTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslPortUtilTx.setStatus("current")


class _AdslPortUtilRx_Type(Integer32):
    """Custom type adslPortUtilRx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AdslPortUtilRx_Type.__name__ = "Integer32"
_AdslPortUtilRx_Object = MibTableColumn
adslPortUtilRx = _AdslPortUtilRx_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 20, 1, 1, 2),
    _AdslPortUtilRx_Type()
)
adslPortUtilRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslPortUtilRx.setStatus("current")
_AdslStatsXturInp_Type = DisplayString
_AdslStatsXturInp_Object = MibTableColumn
adslStatsXturInp = _AdslStatsXturInp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 20, 1, 1, 3),
    _AdslStatsXturInp_Type()
)
adslStatsXturInp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslStatsXturInp.setStatus("current")
_AdslStatsXtucInp_Type = DisplayString
_AdslStatsXtucInp_Object = MibTableColumn
adslStatsXtucInp = _AdslStatsXtucInp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 13, 20, 1, 1, 4),
    _AdslStatsXtucInp_Type()
)
adslStatsXtucInp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslStatsXtucInp.setStatus("current")
_Clear_ObjectIdentity = ObjectIdentity
clear = _Clear_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 14)
)
_CounterClearTarget_Type = OctetString
_CounterClearTarget_Object = MibScalar
counterClearTarget = _CounterClearTarget_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 14, 1),
    _CounterClearTarget_Type()
)
counterClearTarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    counterClearTarget.setStatus("current")
_CounterClearOps_Type = Integer32
_CounterClearOps_Object = MibScalar
counterClearOps = _CounterClearOps_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 14, 2),
    _CounterClearOps_Type()
)
counterClearOps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    counterClearOps.setStatus("current")


class _CounterClearVpi_Type(Integer32):
    """Custom type counterClearVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CounterClearVpi_Type.__name__ = "Integer32"
_CounterClearVpi_Object = MibScalar
counterClearVpi = _CounterClearVpi_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 14, 3),
    _CounterClearVpi_Type()
)
counterClearVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    counterClearVpi.setStatus("current")


class _CounterClearVci_Type(Integer32):
    """Custom type counterClearVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CounterClearVci_Type.__name__ = "Integer32"
_CounterClearVci_Object = MibScalar
counterClearVci = _CounterClearVci_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 14, 4),
    _CounterClearVci_Type()
)
counterClearVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    counterClearVci.setStatus("current")
_Voip_ObjectIdentity = ObjectIdentity
voip = _Voip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 16)
)
_VoipArp_ObjectIdentity = ObjectIdentity
voipArp = _VoipArp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 16, 1)
)
_VoipArpFlushOps_Type = Integer32
_VoipArpFlushOps_Object = MibScalar
voipArpFlushOps = _VoipArpFlushOps_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 16, 1, 1),
    _VoipArpFlushOps_Type()
)
voipArpFlushOps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipArpFlushOps.setStatus("current")
_VoipArpShowTable_Object = MibTable
voipArpShowTable = _VoipArpShowTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 16, 1, 2)
)
if mibBuilder.loadTexts:
    voipArpShowTable.setStatus("current")
_VoipArpShowEntry_Object = MibTableRow
voipArpShowEntry = _VoipArpShowEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 16, 1, 2, 1)
)
voipArpShowEntry.setIndexNames(
    (0, "E5-121-MIB", "voipArpShowIp"),
)
if mibBuilder.loadTexts:
    voipArpShowEntry.setStatus("current")
_VoipArpShowIp_Type = IpAddress
_VoipArpShowIp_Object = MibTableColumn
voipArpShowIp = _VoipArpShowIp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 16, 1, 2, 1, 1),
    _VoipArpShowIp_Type()
)
voipArpShowIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipArpShowIp.setStatus("current")
_VoipArpShowMac_Type = PhysAddress
_VoipArpShowMac_Object = MibTableColumn
voipArpShowMac = _VoipArpShowMac_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 16, 1, 2, 1, 2),
    _VoipArpShowMac_Type()
)
voipArpShowMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipArpShowMac.setStatus("current")
_VoipSip_ObjectIdentity = ObjectIdentity
voipSip = _VoipSip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 16, 2)
)
_MaxNumOfVoipNumberPlan_Type = Integer32
_MaxNumOfVoipNumberPlan_Object = MibScalar
maxNumOfVoipNumberPlan = _MaxNumOfVoipNumberPlan_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 16, 2, 1),
    _MaxNumOfVoipNumberPlan_Type()
)
maxNumOfVoipNumberPlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumOfVoipNumberPlan.setStatus("current")
_VoipNumberPlanTable_Object = MibTable
voipNumberPlanTable = _VoipNumberPlanTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 16, 2, 2)
)
if mibBuilder.loadTexts:
    voipNumberPlanTable.setStatus("current")
_VoipNumberPlanEntry_Object = MibTableRow
voipNumberPlanEntry = _VoipNumberPlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 16, 2, 2, 1)
)
voipNumberPlanEntry.setIndexNames(
    (0, "E5-121-MIB", "voipNumberPlanName"),
    (0, "E5-121-MIB", "voipNumberPlanIndex"),
)
if mibBuilder.loadTexts:
    voipNumberPlanEntry.setStatus("current")


class _VoipNumberPlanName_Type(DisplayString):
    """Custom type voipNumberPlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_VoipNumberPlanName_Type.__name__ = "DisplayString"
_VoipNumberPlanName_Object = MibTableColumn
voipNumberPlanName = _VoipNumberPlanName_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 16, 2, 2, 1, 1),
    _VoipNumberPlanName_Type()
)
voipNumberPlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipNumberPlanName.setStatus("current")


class _VoipNumberPlanIndex_Type(Integer32):
    """Custom type voipNumberPlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_VoipNumberPlanIndex_Type.__name__ = "Integer32"
_VoipNumberPlanIndex_Object = MibTableColumn
voipNumberPlanIndex = _VoipNumberPlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 16, 2, 2, 1, 2),
    _VoipNumberPlanIndex_Type()
)
voipNumberPlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipNumberPlanIndex.setStatus("current")
_VoipNumberPlanPattern_Type = OctetString
_VoipNumberPlanPattern_Object = MibTableColumn
voipNumberPlanPattern = _VoipNumberPlanPattern_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 16, 2, 2, 1, 3),
    _VoipNumberPlanPattern_Type()
)
voipNumberPlanPattern.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    voipNumberPlanPattern.setStatus("current")
_VoipNumberPlanRule_Type = OctetString
_VoipNumberPlanRule_Object = MibTableColumn
voipNumberPlanRule = _VoipNumberPlanRule_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 16, 2, 2, 1, 4),
    _VoipNumberPlanRule_Type()
)
voipNumberPlanRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    voipNumberPlanRule.setStatus("current")
_VoipNumberPlanRowStatus_Type = RowStatus
_VoipNumberPlanRowStatus_Object = MibTableColumn
voipNumberPlanRowStatus = _VoipNumberPlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 16, 2, 2, 1, 5),
    _VoipNumberPlanRowStatus_Type()
)
voipNumberPlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    voipNumberPlanRowStatus.setStatus("current")
_VoipNumberPlanDftTable_Object = MibTable
voipNumberPlanDftTable = _VoipNumberPlanDftTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 16, 2, 3)
)
if mibBuilder.loadTexts:
    voipNumberPlanDftTable.setStatus("current")
_VoipNumberPlanDftEntry_Object = MibTableRow
voipNumberPlanDftEntry = _VoipNumberPlanDftEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 16, 2, 3, 1)
)
voipNumberPlanDftEntry.setIndexNames(
    (0, "E5-121-MIB", "voipNumberPlanName"),
)
if mibBuilder.loadTexts:
    voipNumberPlanDftEntry.setStatus("current")
_VoipNumberPlanDftRule_Type = OctetString
_VoipNumberPlanDftRule_Object = MibTableColumn
voipNumberPlanDftRule = _VoipNumberPlanDftRule_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 16, 2, 3, 1, 1),
    _VoipNumberPlanDftRule_Type()
)
voipNumberPlanDftRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    voipNumberPlanDftRule.setStatus("current")
_DigitSetup_ObjectIdentity = ObjectIdentity
digitSetup = _DigitSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 16, 2, 4)
)
_TimeoutSetup_ObjectIdentity = ObjectIdentity
timeoutSetup = _TimeoutSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 16, 2, 4, 1)
)


class _InitialTimeout_Type(Integer32):
    """Custom type initialTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_InitialTimeout_Type.__name__ = "Integer32"
_InitialTimeout_Object = MibScalar
initialTimeout = _InitialTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 16, 2, 4, 1, 1),
    _InitialTimeout_Type()
)
initialTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    initialTimeout.setStatus("current")


class _InterDigitTimeout_Type(Integer32):
    """Custom type interDigitTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_InterDigitTimeout_Type.__name__ = "Integer32"
_InterDigitTimeout_Object = MibScalar
interDigitTimeout = _InterDigitTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 16, 2, 4, 1, 2),
    _InterDigitTimeout_Type()
)
interDigitTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interDigitTimeout.setStatus("current")


class _DigitPauseTimeout_Type(Integer32):
    """Custom type digitPauseTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_DigitPauseTimeout_Type.__name__ = "Integer32"
_DigitPauseTimeout_Object = MibScalar
digitPauseTimeout = _DigitPauseTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 16, 2, 4, 1, 3),
    _DigitPauseTimeout_Type()
)
digitPauseTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitPauseTimeout.setStatus("current")


class _MatchingTimeout_Type(Integer32):
    """Custom type matchingTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_MatchingTimeout_Type.__name__ = "Integer32"
_MatchingTimeout_Object = MibScalar
matchingTimeout = _MatchingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 16, 2, 4, 1, 4),
    _MatchingTimeout_Type()
)
matchingTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    matchingTimeout.setStatus("current")
_VoipIp_ObjectIdentity = ObjectIdentity
voipIp = _VoipIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 16, 3)
)
_VoipIpSetIp_Type = IpAddress
_VoipIpSetIp_Object = MibScalar
voipIpSetIp = _VoipIpSetIp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 16, 3, 1),
    _VoipIpSetIp_Type()
)
voipIpSetIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipIpSetIp.setStatus("current")
_VoipIpSetVid_Type = VlanIndex
_VoipIpSetVid_Object = MibScalar
voipIpSetVid = _VoipIpSetVid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 16, 3, 2),
    _VoipIpSetVid_Type()
)
voipIpSetVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipIpSetVid.setStatus("current")


class _VoipIpSetMask_Type(Integer32):
    """Custom type voipIpSetMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_VoipIpSetMask_Type.__name__ = "Integer32"
_VoipIpSetMask_Object = MibScalar
voipIpSetMask = _VoipIpSetMask_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 16, 3, 3),
    _VoipIpSetMask_Type()
)
voipIpSetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipIpSetMask.setStatus("current")


class _VoipIpSetDhcpClientEnable_Type(Integer32):
    """Custom type voipIpSetDhcpClientEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_VoipIpSetDhcpClientEnable_Type.__name__ = "Integer32"
_VoipIpSetDhcpClientEnable_Object = MibScalar
voipIpSetDhcpClientEnable = _VoipIpSetDhcpClientEnable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 16, 3, 4),
    _VoipIpSetDhcpClientEnable_Type()
)
voipIpSetDhcpClientEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipIpSetDhcpClientEnable.setStatus("current")
_VoipIpGateway_Type = IpAddress
_VoipIpGateway_Object = MibScalar
voipIpGateway = _VoipIpGateway_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 16, 3, 5),
    _VoipIpGateway_Type()
)
voipIpGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipIpGateway.setStatus("current")
_VoipDns_ObjectIdentity = ObjectIdentity
voipDns = _VoipDns_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 16, 4)
)
_VoipDnsIp_Type = IpAddress
_VoipDnsIp_Object = MibScalar
voipDnsIp = _VoipDnsIp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 16, 4, 1),
    _VoipDnsIp_Type()
)
voipDnsIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipDnsIp.setStatus("current")
_MaxNumOfVoipRoute_Type = Integer32
_MaxNumOfVoipRoute_Object = MibScalar
maxNumOfVoipRoute = _MaxNumOfVoipRoute_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 16, 7),
    _MaxNumOfVoipRoute_Type()
)
maxNumOfVoipRoute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumOfVoipRoute.setStatus("current")
_VoipRouteTable_Object = MibTable
voipRouteTable = _VoipRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 16, 8)
)
if mibBuilder.loadTexts:
    voipRouteTable.setStatus("current")
_VoipRouteEntry_Object = MibTableRow
voipRouteEntry = _VoipRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 16, 8, 1)
)
voipRouteEntry.setIndexNames(
    (0, "E5-121-MIB", "voipRouteIp"),
    (0, "E5-121-MIB", "voipRouteGateway"),
    (0, "E5-121-MIB", "voipRouteMask"),
)
if mibBuilder.loadTexts:
    voipRouteEntry.setStatus("current")
_VoipRouteIp_Type = IpAddress
_VoipRouteIp_Object = MibTableColumn
voipRouteIp = _VoipRouteIp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 16, 8, 1, 1),
    _VoipRouteIp_Type()
)
voipRouteIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipRouteIp.setStatus("current")
_VoipRouteGateway_Type = IpAddress
_VoipRouteGateway_Object = MibTableColumn
voipRouteGateway = _VoipRouteGateway_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 16, 8, 1, 2),
    _VoipRouteGateway_Type()
)
voipRouteGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipRouteGateway.setStatus("current")


class _VoipRouteMask_Type(Integer32):
    """Custom type voipRouteMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_VoipRouteMask_Type.__name__ = "Integer32"
_VoipRouteMask_Object = MibTableColumn
voipRouteMask = _VoipRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 16, 8, 1, 3),
    _VoipRouteMask_Type()
)
voipRouteMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipRouteMask.setStatus("current")


class _VoipRouteMetric_Type(Integer32):
    """Custom type voipRouteMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_VoipRouteMetric_Type.__name__ = "Integer32"
_VoipRouteMetric_Object = MibTableColumn
voipRouteMetric = _VoipRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 16, 8, 1, 4),
    _VoipRouteMetric_Type()
)
voipRouteMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    voipRouteMetric.setStatus("current")
_VoipRouteRowStatus_Type = RowStatus
_VoipRouteRowStatus_Object = MibTableColumn
voipRouteRowStatus = _VoipRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 16, 8, 1, 5),
    _VoipRouteRowStatus_Type()
)
voipRouteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    voipRouteRowStatus.setStatus("current")


class _VoipCountryCode_Type(Integer32):
    """Custom type voipCountryCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("usa", 1)
    )


_VoipCountryCode_Type.__name__ = "Integer32"
_VoipCountryCode_Object = MibScalar
voipCountryCode = _VoipCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 16, 9),
    _VoipCountryCode_Type()
)
voipCountryCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipCountryCode.setStatus("current")
_VoipH248_ObjectIdentity = ObjectIdentity
voipH248 = _VoipH248_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 16, 10)
)
_MaxNumOfVoipH248MgConf_Type = Integer32
_MaxNumOfVoipH248MgConf_Object = MibScalar
maxNumOfVoipH248MgConf = _MaxNumOfVoipH248MgConf_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 16, 10, 1),
    _MaxNumOfVoipH248MgConf_Type()
)
maxNumOfVoipH248MgConf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumOfVoipH248MgConf.setStatus("current")
_VoipH248MgConf_ObjectIdentity = ObjectIdentity
voipH248MgConf = _VoipH248MgConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 16, 10, 2)
)
_VoipH248MgName_Type = DisplayString
_VoipH248MgName_Object = MibScalar
voipH248MgName = _VoipH248MgName_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 16, 10, 2, 1),
    _VoipH248MgName_Type()
)
voipH248MgName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipH248MgName.setStatus("current")


class _VoipH248MgEnable_Type(Integer32):
    """Custom type voipH248MgEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_VoipH248MgEnable_Type.__name__ = "Integer32"
_VoipH248MgEnable_Object = MibScalar
voipH248MgEnable = _VoipH248MgEnable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 16, 10, 2, 2),
    _VoipH248MgEnable_Type()
)
voipH248MgEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipH248MgEnable.setStatus("current")
_VoipH248MgH248Profile_Type = DisplayString
_VoipH248MgH248Profile_Object = MibScalar
voipH248MgH248Profile = _VoipH248MgH248Profile_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 16, 10, 2, 3),
    _VoipH248MgH248Profile_Type()
)
voipH248MgH248Profile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipH248MgH248Profile.setStatus("current")


class _VoipH248MgPort_Type(Integer32):
    """Custom type voipH248MgPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1025, 65535),
    )


_VoipH248MgPort_Type.__name__ = "Integer32"
_VoipH248MgPort_Object = MibScalar
voipH248MgPort = _VoipH248MgPort_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 16, 10, 2, 4),
    _VoipH248MgPort_Type()
)
voipH248MgPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipH248MgPort.setStatus("current")
_VoipRing_ObjectIdentity = ObjectIdentity
voipRing = _VoipRing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 16, 11)
)
_VoipRingTable_Object = MibTable
voipRingTable = _VoipRingTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 16, 11, 1)
)
if mibBuilder.loadTexts:
    voipRingTable.setStatus("current")
_VoipRingEntry_Object = MibTableRow
voipRingEntry = _VoipRingEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 16, 11, 1, 1)
)
voipRingEntry.setIndexNames(
    (0, "E5-121-MIB", "voipRingIndex"),
)
if mibBuilder.loadTexts:
    voipRingEntry.setStatus("current")


class _VoipRingIndex_Type(Integer32):
    """Custom type voipRingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_VoipRingIndex_Type.__name__ = "Integer32"
_VoipRingIndex_Object = MibTableColumn
voipRingIndex = _VoipRingIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 16, 11, 1, 1, 1),
    _VoipRingIndex_Type()
)
voipRingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipRingIndex.setStatus("current")


class _VoipRingName_Type(DisplayString):
    """Custom type voipRingName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_VoipRingName_Type.__name__ = "DisplayString"
_VoipRingName_Object = MibTableColumn
voipRingName = _VoipRingName_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 16, 11, 1, 1, 2),
    _VoipRingName_Type()
)
voipRingName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    voipRingName.setStatus("current")


class _VoipRingOn1_Type(Integer32):
    """Custom type voipRingOn1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 10000),
    )


_VoipRingOn1_Type.__name__ = "Integer32"
_VoipRingOn1_Object = MibTableColumn
voipRingOn1 = _VoipRingOn1_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 16, 11, 1, 1, 3),
    _VoipRingOn1_Type()
)
voipRingOn1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    voipRingOn1.setStatus("current")


class _VoipRingOff1_Type(Integer32):
    """Custom type voipRingOff1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 10000),
    )


_VoipRingOff1_Type.__name__ = "Integer32"
_VoipRingOff1_Object = MibTableColumn
voipRingOff1 = _VoipRingOff1_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 16, 11, 1, 1, 4),
    _VoipRingOff1_Type()
)
voipRingOff1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    voipRingOff1.setStatus("current")


class _VoipRingOn2_Type(Integer32):
    """Custom type voipRingOn2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 10000),
    )


_VoipRingOn2_Type.__name__ = "Integer32"
_VoipRingOn2_Object = MibTableColumn
voipRingOn2 = _VoipRingOn2_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 16, 11, 1, 1, 5),
    _VoipRingOn2_Type()
)
voipRingOn2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    voipRingOn2.setStatus("current")


class _VoipRingOff2_Type(Integer32):
    """Custom type voipRingOff2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 10000),
    )


_VoipRingOff2_Type.__name__ = "Integer32"
_VoipRingOff2_Object = MibTableColumn
voipRingOff2 = _VoipRingOff2_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 16, 11, 1, 1, 6),
    _VoipRingOff2_Type()
)
voipRingOff2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    voipRingOff2.setStatus("current")


class _VoipRingOn3_Type(Integer32):
    """Custom type voipRingOn3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 10000),
    )


_VoipRingOn3_Type.__name__ = "Integer32"
_VoipRingOn3_Object = MibTableColumn
voipRingOn3 = _VoipRingOn3_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 16, 11, 1, 1, 7),
    _VoipRingOn3_Type()
)
voipRingOn3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    voipRingOn3.setStatus("current")


class _VoipRingOff3_Type(Integer32):
    """Custom type voipRingOff3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 10000),
    )


_VoipRingOff3_Type.__name__ = "Integer32"
_VoipRingOff3_Object = MibTableColumn
voipRingOff3 = _VoipRingOff3_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 16, 11, 1, 1, 8),
    _VoipRingOff3_Type()
)
voipRingOff3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    voipRingOff3.setStatus("current")


class _VoipRingSetDefault_Type(Integer32):
    """Custom type voipRingSetDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_VoipRingSetDefault_Type.__name__ = "Integer32"
_VoipRingSetDefault_Object = MibScalar
voipRingSetDefault = _VoipRingSetDefault_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 16, 11, 2),
    _VoipRingSetDefault_Type()
)
voipRingSetDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipRingSetDefault.setStatus("current")


class _VoipBootRegDelay_Type(Integer32):
    """Custom type voipBootRegDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_VoipBootRegDelay_Type.__name__ = "Integer32"
_VoipBootRegDelay_Object = MibScalar
voipBootRegDelay = _VoipBootRegDelay_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 16, 12),
    _VoipBootRegDelay_Type()
)
voipBootRegDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipBootRegDelay.setStatus("current")
_VoipActiveCall_ObjectIdentity = ObjectIdentity
voipActiveCall = _VoipActiveCall_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 16, 13)
)
_VoipActiveCallMaxActiveCalls_Type = Integer32
_VoipActiveCallMaxActiveCalls_Object = MibScalar
voipActiveCallMaxActiveCalls = _VoipActiveCallMaxActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 16, 13, 1),
    _VoipActiveCallMaxActiveCalls_Type()
)
voipActiveCallMaxActiveCalls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipActiveCallMaxActiveCalls.setStatus("current")
_VoipActiveCallThreshold_Type = Integer32
_VoipActiveCallThreshold_Object = MibScalar
voipActiveCallThreshold = _VoipActiveCallThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 16, 13, 2),
    _VoipActiveCallThreshold_Type()
)
voipActiveCallThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipActiveCallThreshold.setStatus("current")


class _VoipMode_Type(Integer32):
    """Custom type voipMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("sip", 1),
          ("csip", 2),
          ("h248", 3))
    )


_VoipMode_Type.__name__ = "Integer32"
_VoipMode_Object = MibScalar
voipMode = _VoipMode_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 16, 100),
    _VoipMode_Type()
)
voipMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipMode.setStatus("current")
_AesSeriesCommon_ObjectIdentity = ObjectIdentity
aesSeriesCommon = _AesSeriesCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 97)
)
_IesSeriesCommon_ObjectIdentity = ObjectIdentity
iesSeriesCommon = _IesSeriesCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 98)
)
_AccessSwitchCommonATM_ObjectIdentity = ObjectIdentity
accessSwitchCommonATM = _AccessSwitchCommonATM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 4, 99)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "E5-121-MIB",
    **{"calixNetworks": calixNetworks,
       "calixRegistrations": calixRegistrations,
       "calixProducts": calixProducts,
       "e5x100": e5x100,
       "e5x121": e5x121,
       "alarmconf": alarmconf,
       "alarmOps": alarmOps,
       "alarmConfTable": alarmConfTable,
       "alarmConfEntry": alarmConfEntry,
       "alarmConfId": alarmConfId,
       "alarmConfFacility": alarmConfFacility,
       "alarmConfTarget": alarmConfTarget,
       "alarmConfSeverity": alarmConfSeverity,
       "alarmConfClearable": alarmConfClearable,
       "alarmCurrTable": alarmCurrTable,
       "alarmCurrEntry": alarmCurrEntry,
       "alarmCurrIndex": alarmCurrIndex,
       "alarmCurrOccurTime": alarmCurrOccurTime,
       "alarmCurrTrapOid": alarmCurrTrapOid,
       "alarmCurrParam1": alarmCurrParam1,
       "alarmCurrParam2": alarmCurrParam2,
       "alarmCurrParam3": alarmCurrParam3,
       "alarmCurrParam4": alarmCurrParam4,
       "alarmCurrParam5": alarmCurrParam5,
       "alarmCurrParam6": alarmCurrParam6,
       "alarmCurrParam7": alarmCurrParam7,
       "alarmCurrParam8": alarmCurrParam8,
       "alarmCurrTimeDescr": alarmCurrTimeDescr,
       "alarmCurrSeverity": alarmCurrSeverity,
       "alarmCurrDescr": alarmCurrDescr,
       "alarmSeverityPortTable": alarmSeverityPortTable,
       "alarmSeverityPortEntry": alarmSeverityPortEntry,
       "severityThresh": severityThresh,
       "diagnostic": diagnostic,
       "selt": selt,
       "seltTarget": seltTarget,
       "seltOps": seltOps,
       "seltStatus": seltStatus,
       "seltCableType": seltCableType,
       "seltLoopEstimateLengthFt": seltLoopEstimateLengthFt,
       "seltLoopEstimateLengthMeter": seltLoopEstimateLengthMeter,
       "ldm": ldm,
       "ldmTarget": ldmTarget,
       "ldmOps": ldmOps,
       "ldmStatus": ldmStatus,
       "ldmXtucLoopAttenuation": ldmXtucLoopAttenuation,
       "ldmXtucSignalAttenuation": ldmXtucSignalAttenuation,
       "ldmXtucSignalMargin": ldmXtucSignalMargin,
       "ldmXtucAggregateTxPower": ldmXtucAggregateTxPower,
       "ldmXtucAttainableBitRate": ldmXtucAttainableBitRate,
       "ldmXturLoopAttenuation": ldmXturLoopAttenuation,
       "ldmXturSignalAttenuation": ldmXturSignalAttenuation,
       "ldmXturSignalMargin": ldmXturSignalMargin,
       "ldmXturAggregateTxPower": ldmXturAggregateTxPower,
       "ldmXturAttainableBitRate": ldmXturAttainableBitRate,
       "ldmXtucNumOfSubcarriersPerPort": ldmXtucNumOfSubcarriersPerPort,
       "ldmXturNumOfSubcarriersPerPort": ldmXturNumOfSubcarriersPerPort,
       "ldmXtucHlinScale": ldmXtucHlinScale,
       "ldmXtucHlinReal1": ldmXtucHlinReal1,
       "ldmXtucHlinReal2": ldmXtucHlinReal2,
       "ldmXtucHlinImage1": ldmXtucHlinImage1,
       "ldmXtucHlinImage2": ldmXtucHlinImage2,
       "ldmXtucHlog1": ldmXtucHlog1,
       "ldmXtucHlog2": ldmXtucHlog2,
       "ldmXtucQln1": ldmXtucQln1,
       "ldmXtucQln2": ldmXtucQln2,
       "ldmXtucSnr1": ldmXtucSnr1,
       "ldmXtucSnr2": ldmXtucSnr2,
       "ldmXturHlinScale": ldmXturHlinScale,
       "ldmXturHlinReal": ldmXturHlinReal,
       "ldmXturHlinImage": ldmXturHlinImage,
       "ldmXturHlog": ldmXturHlog,
       "ldmXturQln": ldmXturQln,
       "ldmXturSnr": ldmXturSnr,
       "ldmXtucHlogGroupFactor": ldmXtucHlogGroupFactor,
       "ldmXtucQlnGroupFactor": ldmXtucQlnGroupFactor,
       "ldmXtucSnrGroupFactor": ldmXtucSnrGroupFactor,
       "ldmXturHlogGroupFactor": ldmXturHlogGroupFactor,
       "ldmXturQlnGroupFactor": ldmXturQlnGroupFactor,
       "ldmXturSnrGroupFactor": ldmXturSnrGroupFactor,
       "mlt": mlt,
       "mltTarget": mltTarget,
       "mltOps": mltOps,
       "mltOption": mltOption,
       "mltForce": mltForce,
       "mltResult": mltResult,
       "mltVacTip": mltVacTip,
       "mltVacRing": mltVacRing,
       "mltVacDiff": mltVacDiff,
       "mltVdcTip": mltVdcTip,
       "mltVdcRing": mltVdcRing,
       "mltVdcDiff": mltVdcDiff,
       "mltRLoop": mltRLoop,
       "mltRtg": mltRtg,
       "mltRrg": mltRrg,
       "mltRtr": mltRtr,
       "mltCtg": mltCtg,
       "mltCrg": mltCrg,
       "mltCtr": mltCtr,
       "mltRen": mltRen,
       "mltVRing": mltVRing,
       "mltVMetering": mltVMetering,
       "mltDialToneDetected": mltDialToneDetected,
       "mltDetectedDtmfCount": mltDetectedDtmfCount,
       "mltDialToneDelay": mltDialToneDelay,
       "mltRelayTable": mltRelayTable,
       "mltRelayEntry": mltRelayEntry,
       "mltRelaySet": mltRelaySet,
       "multicast": multicast,
       "igmpEnable": igmpEnable,
       "mcastBandwidth": mcastBandwidth,
       "mcastDefaultBandwidth": mcastDefaultBandwidth,
       "maxNumOfMcastBw": maxNumOfMcastBw,
       "mcastBwTable": mcastBwTable,
       "mcastBwEntry": mcastBwEntry,
       "mcastBwIndex": mcastBwIndex,
       "mcastBwStartIp": mcastBwStartIp,
       "mcastBwEndIp": mcastBwEndIp,
       "mcastBwBandwidth": mcastBwBandwidth,
       "mcastBwRowStatus": mcastBwRowStatus,
       "mcastBwPortTable": mcastBwPortTable,
       "mcastBwPortEntry": mcastBwPortEntry,
       "mcastBwPortEnable": mcastBwPortEnable,
       "mcastBwPortBandwidth": mcastBwPortBandwidth,
       "igmpCount": igmpCount,
       "igmpCountPortTable": igmpCountPortTable,
       "igmpCountPortEntry": igmpCountPortEntry,
       "igmpCountPortEnable": igmpCountPortEnable,
       "igmpCountPortLimit": igmpCountPortLimit,
       "mvlan": mvlan,
       "maxNumOfMvlan": maxNumOfMvlan,
       "mvlanTable": mvlanTable,
       "mvlanEntry": mvlanEntry,
       "mvlanIndex": mvlanIndex,
       "mvlanName": mvlanName,
       "mvlanEgressPorts": mvlanEgressPorts,
       "mvlanUntaggedPorts": mvlanUntaggedPorts,
       "mvlanRowStatus": mvlanRowStatus,
       "mvlanTranslateTable": mvlanTranslateTable,
       "mvlanTranslateEntry": mvlanTranslateEntry,
       "mvlanTranslateIndex": mvlanTranslateIndex,
       "mvlanTranslateStartIp": mvlanTranslateStartIp,
       "mvlanTranslateEndIp": mvlanTranslateEndIp,
       "queryVid": queryVid,
       "maxNumOfQryVid": maxNumOfQryVid,
       "qryVidConfTable": qryVidConfTable,
       "qryVidConfEntry": qryVidConfEntry,
       "qryVid": qryVid,
       "qryVidRowStatus": qryVidRowStatus,
       "qryVidStatusTable": qryVidStatusTable,
       "qryVidStatusEntry": qryVidStatusEntry,
       "qryVidType": qryVidType,
       "igmpVersion": igmpVersion,
       "igmpLeaveMode": igmpLeaveMode,
       "igmpTimer": igmpTimer,
       "igmpQryInterval": igmpQryInterval,
       "igmpRobust": igmpRobust,
       "igmpQryRespInterval": igmpQryRespInterval,
       "igmpLastMemQryInterval": igmpLastMemQryInterval,
       "igmpLastMemQryRobust": igmpLastMemQryRobust,
       "auditQuery": auditQuery,
       "auditQryEnable": auditQryEnable,
       "auditQryInterval": auditQryInterval,
       "auditQryRobust": auditQryRobust,
       "igmpProfile": igmpProfile,
       "maxNumberOfIgmpProfiles": maxNumberOfIgmpProfiles,
       "igmpProfileTable": igmpProfileTable,
       "igmpProfileEntry": igmpProfileEntry,
       "igmpProfileName": igmpProfileName,
       "igmpProfileEnable": igmpProfileEnable,
       "igmpProfileMaxGroup": igmpProfileMaxGroup,
       "igmpProfileRowStatus": igmpProfileRowStatus,
       "igmpFilterTable": igmpFilterTable,
       "igmpFilterEntry": igmpFilterEntry,
       "igmpFilterIndex": igmpFilterIndex,
       "igmpFilterStartIp": igmpFilterStartIp,
       "igmpFilterEndIp": igmpFilterEndIp,
       "igmpProfilePortTable": igmpProfilePortTable,
       "igmpProfilePortEntry": igmpProfilePortEntry,
       "igmpProfilePortProfile": igmpProfilePortProfile,
       "port": port,
       "subrPortTable": subrPortTable,
       "subrPortEntry": subrPortEntry,
       "subrPortName": subrPortName,
       "subrPortTel": subrPortTel,
       "vdslPort": vdslPort,
       "vdslLineConfTable": vdslLineConfTable,
       "vdslLineConfEntry": vdslLineConfEntry,
       "vdslLineConfUpbo": vdslLineConfUpbo,
       "vdslLineConfVdslProfile": vdslLineConfVdslProfile,
       "vdslLineConfRfiBand": vdslLineConfRfiBand,
       "vdslLineConfIpqosProfile": vdslLineConfIpqosProfile,
       "vdslLineConfVturInp": vdslLineConfVturInp,
       "vdslLineConfVtucInp": vdslLineConfVtucInp,
       "vdslLineConfOptionMask": vdslLineConfOptionMask,
       "vdslLineConfUpboForceLength": vdslLineConfUpboForceLength,
       "vdslLineConfPsdShape": vdslLineConfPsdShape,
       "vdslLineConfDpbo": vdslLineConfDpbo,
       "vdslLineConfDpboParamEsel": vdslLineConfDpboParamEsel,
       "vdslLineConfDpboParamEscma": vdslLineConfDpboParamEscma,
       "vdslLineConfDpboParamEscmb": vdslLineConfDpboParamEscmb,
       "vdslLineConfDpboParamEscmc": vdslLineConfDpboParamEscmc,
       "vdslLineConfDpboParamMus": vdslLineConfDpboParamMus,
       "vdslLineConfDpboParamFmin": vdslLineConfDpboParamFmin,
       "vdslLineConfDpboParamFmax": vdslLineConfDpboParamFmax,
       "vdslLineConfDpboParamPsdId": vdslLineConfDpboParamPsdId,
       "vdslVlan": vdslVlan,
       "vdslPortConfTable": vdslPortConfTable,
       "vdslPortConfEntry": vdslPortConfEntry,
       "vdslPortConfTlsEnable": vdslPortConfTlsEnable,
       "vdslPortConfTlsVid": vdslPortConfTlsVid,
       "vdslPortConfTlsPriority": vdslPortConfTlsPriority,
       "vdslPortConfDtEnable": vdslPortConfDtEnable,
       "vdslPortConfDtSVid": vdslPortConfDtSVid,
       "vdslPortConfDtSPriority": vdslPortConfDtSPriority,
       "vdslPortConfDtCVid": vdslPortConfDtCVid,
       "vdslPortConfDtCPriority": vdslPortConfDtCPriority,
       "vdslPortVlanTranslateTable": vdslPortVlanTranslateTable,
       "vdslPortVlanTranslateEntry": vdslPortVlanTranslateEntry,
       "vdslPortVlanTranslateVpi": vdslPortVlanTranslateVpi,
       "vdslPortVlanTranslateVci": vdslPortVlanTranslateVci,
       "vdslPortVlanTranslateCxvid": vdslPortVlanTranslateCxvid,
       "vdslPortVlanTranslateCvid": vdslPortVlanTranslateCvid,
       "vdslPortVlanTranslateSvid": vdslPortVlanTranslateSvid,
       "vdslPortVlanTranslateDsonly": vdslPortVlanTranslateDsonly,
       "vdslPortVlanTranslateRowStatus": vdslPortVlanTranslateRowStatus,
       "vdslPortPvlanTable": vdslPortPvlanTable,
       "vdslPortPvlanEntry": vdslPortPvlanEntry,
       "vdslPortPvlanEtype": vdslPortPvlanEtype,
       "vdslPortPvlanVid": vdslPortPvlanVid,
       "vdslPortPvlanPriority": vdslPortPvlanPriority,
       "vdslPortPvlanRowStatus": vdslPortPvlanRowStatus,
       "vdslRfiCustomTable": vdslRfiCustomTable,
       "vdslRfiCustomEntry": vdslRfiCustomEntry,
       "vdslRfiCustomIndex": vdslRfiCustomIndex,
       "vdslRfiCustomStartFreq": vdslRfiCustomStartFreq,
       "vdslRfiCustomEndFreq": vdslRfiCustomEndFreq,
       "vdslRfiCustomEnable": vdslRfiCustomEnable,
       "vdslLineConfUpboParamTable": vdslLineConfUpboParamTable,
       "vdslLineConfUpboParamEntry": vdslLineConfUpboParamEntry,
       "vdslLineConfUpboParamBand": vdslLineConfUpboParamBand,
       "vdslLineConfUpboParamA": vdslLineConfUpboParamA,
       "vdslLineConfUpboParamB": vdslLineConfUpboParamB,
       "vdslLineConfDpboTable": vdslLineConfDpboTable,
       "vdslLineConfDpboEntry": vdslLineConfDpboEntry,
       "vdslLineConfDpboIndex": vdslLineConfDpboIndex,
       "vdslLineConfDpboTone": vdslLineConfDpboTone,
       "vdslLineConfDpboPsd": vdslLineConfDpboPsd,
       "pvc": pvc,
       "maxNumOfPvcs": maxNumOfPvcs,
       "pvcTable": pvcTable,
       "pvcEntry": pvcEntry,
       "pvcVpi": pvcVpi,
       "pvcVci": pvcVci,
       "pvcPvid": pvcPvid,
       "pvcPriority": pvcPriority,
       "pvcProfile": pvcProfile,
       "pvcEncap": pvcEncap,
       "pvcRowStatus": pvcRowStatus,
       "pvcAcName": pvcAcName,
       "pvcServiceName": pvcServiceName,
       "pvcHelloTime": pvcHelloTime,
       "pvcAuto": pvcAuto,
       "pvcStateTable": pvcStateTable,
       "pvcStateEntry": pvcStateEntry,
       "pvcStateVpi": pvcStateVpi,
       "pvcStateVci": pvcStateVci,
       "pvcStatePvid": pvcStatePvid,
       "pvcStatePriority": pvcStatePriority,
       "pvcStateChannelType": pvcStateChannelType,
       "pvcStateEncap": pvcStateEncap,
       "rpvc": rpvc,
       "rpvcGatewayTable": rpvcGatewayTable,
       "rpvcGatewayEntry": rpvcGatewayEntry,
       "rpvcGatewayIp": rpvcGatewayIp,
       "rpvcGatewayVlanId": rpvcGatewayVlanId,
       "rpvcGatewayRowStatus": rpvcGatewayRowStatus,
       "rpvcGatewayPriority": rpvcGatewayPriority,
       "rpvcTable": rpvcTable,
       "rpvcEntry": rpvcEntry,
       "rpvcVpi": rpvcVpi,
       "rpvcVci": rpvcVci,
       "rpvcEncap": rpvcEncap,
       "rpvcProfile": rpvcProfile,
       "rpvcIp": rpvcIp,
       "rpvcNetmask": rpvcNetmask,
       "rpvcGatewayIpAddress": rpvcGatewayIpAddress,
       "rpvcRowStatus": rpvcRowStatus,
       "rpvcRouteDomainTable": rpvcRouteDomainTable,
       "rpvcRouteDomainEntry": rpvcRouteDomainEntry,
       "rpvcRouteDomainVpi": rpvcRouteDomainVpi,
       "rpvcRouteDomainVci": rpvcRouteDomainVci,
       "rpvcRouteDomainIp": rpvcRouteDomainIp,
       "rpvcRouteDomainNetmask": rpvcRouteDomainNetmask,
       "rpvcRouteDomainRowStatus": rpvcRouteDomainRowStatus,
       "rpvcArpAgingTime": rpvcArpAgingTime,
       "rpvcArpFlush": rpvcArpFlush,
       "dsBcastDisableTable": dsBcastDisableTable,
       "dsBcastDisableEntry": dsBcastDisableEntry,
       "dsBcastDisableVlanId": dsBcastDisableVlanId,
       "dsBcastDisableRowStatus": dsBcastDisableRowStatus,
       "paepvc": paepvc,
       "paepvcTable": paepvcTable,
       "paepvcEntry": paepvcEntry,
       "paepvcVpi": paepvcVpi,
       "paepvcVci": paepvcVci,
       "paepvcPvid": paepvcPvid,
       "paepvcEncap": paepvcEncap,
       "paepvcPriority": paepvcPriority,
       "paepvcProfile": paepvcProfile,
       "paepvcAcName": paepvcAcName,
       "paepvcServiceName": paepvcServiceName,
       "paepvcHelloTime": paepvcHelloTime,
       "paepvcRowStatus": paepvcRowStatus,
       "paepvcCvid": paepvcCvid,
       "paepvcCPriority": paepvcCPriority,
       "tlspvc": tlspvc,
       "tlspvcTable": tlspvcTable,
       "tlspvcEntry": tlspvcEntry,
       "tlspvcVpi": tlspvcVpi,
       "tlspvcVci": tlspvcVci,
       "tlspvcSvid": tlspvcSvid,
       "tlspvcEncap": tlspvcEncap,
       "tlspvcSpriority": tlspvcSpriority,
       "tlspvcProfile": tlspvcProfile,
       "tlspvcRowStatus": tlspvcRowStatus,
       "dtpvc": dtpvc,
       "dtpvcTable": dtpvcTable,
       "dtpvcEntry": dtpvcEntry,
       "dtpvcVpi": dtpvcVpi,
       "dtpvcVci": dtpvcVci,
       "dtpvcSvid": dtpvcSvid,
       "dtpvcSpriority": dtpvcSpriority,
       "dtpvcCvid": dtpvcCvid,
       "dtpvcCpriority": dtpvcCpriority,
       "dtpvcEncap": dtpvcEncap,
       "dtpvcProfile": dtpvcProfile,
       "dtpvcRowStatus": dtpvcRowStatus,
       "dtpvcSuperChannel": dtpvcSuperChannel,
       "dtpvcAcName": dtpvcAcName,
       "dtpvcServiceName": dtpvcServiceName,
       "dtpvcHelloTime": dtpvcHelloTime,
       "dtpvcAuto": dtpvcAuto,
       "dtpvcStateTable": dtpvcStateTable,
       "dtpvcStateEntry": dtpvcStateEntry,
       "dtpvcStateVpi": dtpvcStateVpi,
       "dtpvcStateVci": dtpvcStateVci,
       "dtpvcStateSvid": dtpvcStateSvid,
       "dtpvcStateSPriority": dtpvcStateSPriority,
       "dtpvcStateCvid": dtpvcStateCvid,
       "dtpvcStateCPriority": dtpvcStateCPriority,
       "dtpvcStateChannelType": dtpvcStateChannelType,
       "dtpvcStateEncap": dtpvcStateEncap,
       "voipPort": voipPort,
       "voipSipLineConfTable": voipSipLineConfTable,
       "voipSipLineConfEntry": voipSipLineConfEntry,
       "voipSipLineConfSipProfile": voipSipLineConfSipProfile,
       "voipSipLineConfSipCallSvcProfile": voipSipLineConfSipCallSvcProfile,
       "voipSipLineConfDspProfile": voipSipLineConfDspProfile,
       "portOperations": portOperations,
       "voipPortTarget": voipPortTarget,
       "voipPortOps": voipPortOps,
       "voipPortTelTable": voipPortTelTable,
       "voipPortTelEntry": voipPortTelEntry,
       "voipPortTel": voipPortTel,
       "voipH248LineConfTable": voipH248LineConfTable,
       "voipH248LineConfEntry": voipH248LineConfEntry,
       "voipH248LineConfMgName": voipH248LineConfMgName,
       "voipH248LineConfDspProfile": voipH248LineConfDspProfile,
       "voipH248LineConfVBDProfile": voipH248LineConfVBDProfile,
       "voipPortH248TerminationTable": voipPortH248TerminationTable,
       "voipPortH248TerminationEntry": voipPortH248TerminationEntry,
       "voipPortH248TermName": voipPortH248TermName,
       "voipPortGainTable": voipPortGainTable,
       "voipPortGainEntry": voipPortGainEntry,
       "voipPortTXGain": voipPortTXGain,
       "voipPortRXGain": voipPortRXGain,
       "voipPortSeizureModeTable": voipPortSeizureModeTable,
       "voipPortSeizureModeEntry": voipPortSeizureModeEntry,
       "voipPortSeizureMode": voipPortSeizureMode,
       "voipPortSipAuthTable": voipPortSipAuthTable,
       "voipPortSipAuthEntry": voipPortSipAuthEntry,
       "voipPortSipAuthMode": voipPortSipAuthMode,
       "voipPortSipAuthUsername": voipPortSipAuthUsername,
       "voipPortSipAuthPasswdOn": voipPortSipAuthPasswdOn,
       "voipPortSipAuthPasswd": voipPortSipAuthPasswd,
       "voipPortSipCallsvcTable": voipPortSipCallsvcTable,
       "voipPortSipCallsvcEntry": voipPortSipCallsvcEntry,
       "voipPortSipCallsvcMode": voipPortSipCallsvcMode,
       "voipPortSipCallsvcStateMask": voipPortSipCallsvcStateMask,
       "voipPortSipCallsvcCPCOn": voipPortSipCallsvcCPCOn,
       "voipPortSipCallsvcCPCTimeout": voipPortSipCallsvcCPCTimeout,
       "snrMgn": snrMgn,
       "snrMgnTable": snrMgnTable,
       "snrMgnEntry": snrMgnEntry,
       "snrMgnMode": snrMgnMode,
       "snrMgnUcTarget": snrMgnUcTarget,
       "snrMgnUcMax": snrMgnUcMax,
       "snrMgnUcMin": snrMgnUcMin,
       "snrMgnUcDownshift": snrMgnUcDownshift,
       "snrMgnUcUpshift": snrMgnUcUpshift,
       "snrMgnUrTarget": snrMgnUrTarget,
       "snrMgnUrMax": snrMgnUrMax,
       "snrMgnUrMin": snrMgnUrMin,
       "snrMgnUrDownshift": snrMgnUrDownshift,
       "snrMgnUrUpshift": snrMgnUrUpshift,
       "dslRate": dslRate,
       "dslRateTable": dslRateTable,
       "dslRateEntry": dslRateEntry,
       "dslRateMode": dslRateMode,
       "dslRateLatencyMode": dslRateLatencyMode,
       "dslRateXtucMaxInterleaveDelay": dslRateXtucMaxInterleaveDelay,
       "dslRateXtucMaxTxRate": dslRateXtucMaxTxRate,
       "dslRateXtucMinTxRate": dslRateXtucMinTxRate,
       "dslRateXturMaxInterleaveDelay": dslRateXturMaxInterleaveDelay,
       "dslRateXturMaxTxRate": dslRateXturMaxTxRate,
       "dslRateXturMinTxRate": dslRateXturMinTxRate,
       "gbond": gbond,
       "gbondGroupTable": gbondGroupTable,
       "gbondGroupEntry": gbondGroupEntry,
       "gbondGroupName": gbondGroupName,
       "gbondGroupPorts": gbondGroupPorts,
       "gbondGroupUpRate": gbondGroupUpRate,
       "gbondGroupDownRate": gbondGroupDownRate,
       "gbondGroupRowStatus": gbondGroupRowStatus,
       "profile": profile,
       "sraShiftMarginProfile": sraShiftMarginProfile,
       "sraShiftMarginProfileTable": sraShiftMarginProfileTable,
       "sraShiftMarginProfileEntry": sraShiftMarginProfileEntry,
       "sraShiftMarginProfileName": sraShiftMarginProfileName,
       "xtucConfDownshiftSnrMgn": xtucConfDownshiftSnrMgn,
       "xtucConfUpshiftSnrMgn": xtucConfUpshiftSnrMgn,
       "xtucConfDownshiftTime": xtucConfDownshiftTime,
       "xtucConfUpshiftTime": xtucConfUpshiftTime,
       "xturConfDownshiftSnrMgn": xturConfDownshiftSnrMgn,
       "xturConfUpshiftSnrMgn": xturConfUpshiftSnrMgn,
       "xturConfDownshiftTime": xturConfDownshiftTime,
       "xturConfUpshiftTime": xturConfUpshiftTime,
       "sraShiftMarginProfileStatus": sraShiftMarginProfileStatus,
       "voipProfile": voipProfile,
       "sipProfile": sipProfile,
       "maxNumOfSipProfiles": maxNumOfSipProfiles,
       "sipProfileTable": sipProfileTable,
       "sipProfileEntry": sipProfileEntry,
       "sipProfileName": sipProfileName,
       "sipProfileSipSvr": sipProfileSipSvr,
       "sipProfileRegSvr": sipProfileRegSvr,
       "sipProfileProxySvr": sipProfileProxySvr,
       "sipProfileSipPort": sipProfileSipPort,
       "sipProfileRegSvrPort": sipProfileRegSvrPort,
       "sipProfileProxySvrPort": sipProfileProxySvrPort,
       "sipProfileUriType": sipProfileUriType,
       "sipProfilePbit": sipProfilePbit,
       "sipProfileDscp": sipProfileDscp,
       "sipProfileKeepAlive": sipProfileKeepAlive,
       "sipProfileSe": sipProfileSe,
       "sipProfilePrack": sipProfilePrack,
       "sipProfileRowStatus": sipProfileRowStatus,
       "sipProfileRegExpire": sipProfileRegExpire,
       "maxNumOfSipCallSvcProfiles": maxNumOfSipCallSvcProfiles,
       "sipCallSvcProfileTable": sipCallSvcProfileTable,
       "sipCallSvcProfileEntry": sipCallSvcProfileEntry,
       "sipCallSvcProfileName": sipCallSvcProfileName,
       "sipCallSvcProfilePasswdOn": sipCallSvcProfilePasswdOn,
       "sipCallSvcProfilePasswd": sipCallSvcProfilePasswd,
       "sipCallSvcProfileNumberPlanOn": sipCallSvcProfileNumberPlanOn,
       "sipCallSvcProfileNumberPlanCc": sipCallSvcProfileNumberPlanCc,
       "sipCallSvcProfileNumberPlanNdc": sipCallSvcProfileNumberPlanNdc,
       "sipCallSvcProfileNumberPlanTable": sipCallSvcProfileNumberPlanTable,
       "sipCallSvcProfileStateMask": sipCallSvcProfileStateMask,
       "sipCallSvcProfileDtmf": sipCallSvcProfileDtmf,
       "sipCallSvcProfileFax": sipCallSvcProfileFax,
       "sipCallSvcProfileRowStatus": sipCallSvcProfileRowStatus,
       "sipCallSvcProfileFlashType": sipCallSvcProfileFlashType,
       "sipCallSvcProfileFlashInfo": sipCallSvcProfileFlashInfo,
       "sipCallSvcProfileSoftSwitchType": sipCallSvcProfileSoftSwitchType,
       "sipCallSvcProfileCPCOn": sipCallSvcProfileCPCOn,
       "sipCallSvcProfileCPCTimeout": sipCallSvcProfileCPCTimeout,
       "maxNumOfDspProfiles": maxNumOfDspProfiles,
       "dspProfileTable": dspProfileTable,
       "dspProfileEntry": dspProfileEntry,
       "dspProfileName": dspProfileName,
       "dspProfileCodec": dspProfileCodec,
       "dspProfilePlayBufferMinDelay": dspProfilePlayBufferMinDelay,
       "dspProfilePlayBufferMaxDelay": dspProfilePlayBufferMaxDelay,
       "dspProfileEchoTail": dspProfileEchoTail,
       "dspProfileRowStatus": dspProfileRowStatus,
       "dspProfileG711Vpi": dspProfileG711Vpi,
       "dspProfileG723Vpi": dspProfileG723Vpi,
       "dspProfileG726Vpi": dspProfileG726Vpi,
       "dspProfileG729Vpi": dspProfileG729Vpi,
       "h248Profile": h248Profile,
       "maxNumOfH248Profiles": maxNumOfH248Profiles,
       "h248ProfileTable": h248ProfileTable,
       "h248ProfileEntry": h248ProfileEntry,
       "h248ProfileName": h248ProfileName,
       "h248ProfileMgcSvr": h248ProfileMgcSvr,
       "h248ProfileMgcPort": h248ProfileMgcPort,
       "h248ProfileMgc2On": h248ProfileMgc2On,
       "h248ProfileMgc2Svr": h248ProfileMgc2Svr,
       "h248ProfileMgc2Port": h248ProfileMgc2Port,
       "h248ProfileTransport": h248ProfileTransport,
       "h248ProfileEncode": h248ProfileEncode,
       "h248ProfilePbit": h248ProfilePbit,
       "h248ProfileDscp": h248ProfileDscp,
       "h248ProfileRowStatus": h248ProfileRowStatus,
       "h248ProfileVbd": h248ProfileVbd,
       "h248ProfileEphemeralPrefix": h248ProfileEphemeralPrefix,
       "h248ProfileSoftswitch": h248ProfileSoftswitch,
       "h248ProfileForceVer": h248ProfileForceVer,
       "h248ProfileStartRTPPort": h248ProfileStartRTPPort,
       "h248ProfileEndRTPPort": h248ProfileEndRTPPort,
       "h248ProfileEphemeralStartNumber": h248ProfileEphemeralStartNumber,
       "h248ProfileEphemeralSuffixLength": h248ProfileEphemeralSuffixLength,
       "h248ProfilePhysicalPrefix": h248ProfilePhysicalPrefix,
       "h248ProfilePhysicalStartNumber": h248ProfilePhysicalStartNumber,
       "h248ProfilePhysicalSuffixLength": h248ProfilePhysicalSuffixLength,
       "h248ProfileRfc2833Mode": h248ProfileRfc2833Mode,
       "h248ProfileRfc2833ModePayloadType": h248ProfileRfc2833ModePayloadType,
       "ipqosProfile": ipqosProfile,
       "maxNumOfIpqosProfiles": maxNumOfIpqosProfiles,
       "ipqosProfileTable": ipqosProfileTable,
       "ipqosProfileEntry": ipqosProfileEntry,
       "ipqosProfileName": ipqosProfileName,
       "ipqosProfileNumOfQueue": ipqosProfileNumOfQueue,
       "ipqosProfileRowStatus": ipqosProfileRowStatus,
       "ipqosProfileQueueTable": ipqosProfileQueueTable,
       "ipqosProfileQueueEntry": ipqosProfileQueueEntry,
       "ipqosProfileQueueIndex": ipqosProfileQueueIndex,
       "ipqosProfileQueuePIR": ipqosProfileQueuePIR,
       "ipqosProfileQueueCIR": ipqosProfileQueueCIR,
       "ipqosProfileQueuePBS": ipqosProfileQueuePBS,
       "ipqosProfileQueueCBS": ipqosProfileQueueCBS,
       "ipqosProfileQueueLevel": ipqosProfileQueueLevel,
       "ipqosProfileQueueWeight": ipqosProfileQueueWeight,
       "switch": switch,
       "dot3ad": dot3ad,
       "dot3adTable": dot3adTable,
       "dot3adEntry": dot3adEntry,
       "dot3adGroupId": dot3adGroupId,
       "dot3adEnable": dot3adEnable,
       "lacpPriority": lacpPriority,
       "lacpTimeout": lacpTimeout,
       "portTrunkingTable": portTrunkingTable,
       "portTrunkingEntry": portTrunkingEntry,
       "portTrunkingGroupId": portTrunkingGroupId,
       "portTrunkingStatus": portTrunkingStatus,
       "portTrunkingPortList": portTrunkingPortList,
       "dscp": dscp,
       "dscpMappingTable": dscpMappingTable,
       "dscpMappingEntry": dscpMappingEntry,
       "dscpSrcCodePoint": dscpSrcCodePoint,
       "dscpMapPriority": dscpMapPriority,
       "dscpPortTable": dscpPortTable,
       "dscpPortEntry": dscpPortEntry,
       "dscpStatusEnable": dscpStatusEnable,
       "vlanIsolation": vlanIsolation,
       "vlanIsolationTable": vlanIsolationTable,
       "vlanIsolationEntry": vlanIsolationEntry,
       "vlanIsolationRowStatus": vlanIsolationRowStatus,
       "enetMtu": enetMtu,
       "enetMtuEntry": enetMtuEntry,
       "tpid": tpid,
       "tpidEntry": tpidEntry,
       "cfm": cfm,
       "cfmLoopbackPortTable": cfmLoopbackPortTable,
       "cfmLoopbackPortEntry": cfmLoopbackPortEntry,
       "cfmLoopbackPortState": cfmLoopbackPortState,
       "cfmMIPTable": cfmMIPTable,
       "cfmMIPEntry": cfmMIPEntry,
       "cfmPort": cfmPort,
       "cfmMIPRowStatus": cfmMIPRowStatus,
       "cfmMIPMacAddr": cfmMIPMacAddr,
       "cfmActionEnableStatus": cfmActionEnableStatus,
       "cfmMode": cfmMode,
       "cfmLbmTimeout": cfmLbmTimeout,
       "cfmLbmDataTlvLength": cfmLbmDataTlvLength,
       "cfmLbrTable": cfmLbrTable,
       "cfmLbrEntry": cfmLbrEntry,
       "cfmLbmIndex": cfmLbmIndex,
       "cfmLbrIndex": cfmLbrIndex,
       "cfmLbrSrcMac": cfmLbrSrcMac,
       "cfmLbrStatus": cfmLbrStatus,
       "cfmLbrRtt": cfmLbrRtt,
       "dhcp": dhcp,
       "dhcpRelay82Table": dhcpRelay82Table,
       "dhcpRelay82Entry": dhcpRelay82Entry,
       "dhcpRelay82PrimaryServer": dhcpRelay82PrimaryServer,
       "dhcpRelay82SecondaryServer": dhcpRelay82SecondaryServer,
       "dhcpRelay82ActiveServer": dhcpRelay82ActiveServer,
       "dhcpRelay82Enable": dhcpRelay82Enable,
       "dhcpRelay82Info": dhcpRelay82Info,
       "dhcpRelay82RelayMode": dhcpRelay82RelayMode,
       "dhcpRelay82Suboption2Enable": dhcpRelay82Suboption2Enable,
       "dhcpRelay82Suboption2Info": dhcpRelay82Suboption2Info,
       "dhcpRelay82EntryEnable": dhcpRelay82EntryEnable,
       "dhcpRelay82EntryOptionMode": dhcpRelay82EntryOptionMode,
       "dhcpRelay82VlanIp": dhcpRelay82VlanIp,
       "dhcpRelay82VlanMask": dhcpRelay82VlanMask,
       "dhcpRelay82VlanGateway": dhcpRelay82VlanGateway,
       "dhcpRelay82ThirdServer": dhcpRelay82ThirdServer,
       "dhcpRelay82FourthServer": dhcpRelay82FourthServer,
       "dhcpRelay82FifthServer": dhcpRelay82FifthServer,
       "dhcpRelay82ServerVid": dhcpRelay82ServerVid,
       "dhcpRelayTest": dhcpRelayTest,
       "dhcpRelayTestVid": dhcpRelayTestVid,
       "dhcpRelayTestIp": dhcpRelayTestIp,
       "dhcpRelayTestOps": dhcpRelayTestOps,
       "dhcpRelayTestStatus": dhcpRelayTestStatus,
       "dhcpRelayArp": dhcpRelayArp,
       "dhcpRelayArpShowTable": dhcpRelayArpShowTable,
       "dhcpRelayArpShowEntry": dhcpRelayArpShowEntry,
       "dhcpRelayArpShowVid": dhcpRelayArpShowVid,
       "dhcpRelayArpShowIp": dhcpRelayArpShowIp,
       "dhcpRelayArpShowMac": dhcpRelayArpShowMac,
       "dhcpRelayArpFlushOps": dhcpRelayArpFlushOps,
       "macfilter": macfilter,
       "macFilterPortTable": macFilterPortTable,
       "macFilterPortEntry": macFilterPortEntry,
       "macFilterPortEnable": macFilterPortEnable,
       "macFilterPortMacCount": macFilterPortMacCount,
       "macFilterPortFilterMode": macFilterPortFilterMode,
       "maxNumOfMacFiltersInSystem": maxNumOfMacFiltersInSystem,
       "maxNumOfMacFiltersPerPort": maxNumOfMacFiltersPerPort,
       "currNumOfMacFiltersInSystem": currNumOfMacFiltersInSystem,
       "macFilterTable": macFilterTable,
       "macFilterEntry": macFilterEntry,
       "macFilterAddr": macFilterAddr,
       "macFilterRowStatus": macFilterRowStatus,
       "macfilterBatchSet": macfilterBatchSet,
       "macfilterTarget": macfilterTarget,
       "macfilterOps": macfilterOps,
       "macFilterMacCountForBatchSet": macFilterMacCountForBatchSet,
       "ouiFilterTable": ouiFilterTable,
       "ouiFilterEntry": ouiFilterEntry,
       "ouiFilterAddr": ouiFilterAddr,
       "ouiFilterRowStatus": ouiFilterRowStatus,
       "maxNumOfOuiFiltersPerPort": maxNumOfOuiFiltersPerPort,
       "ouiFilterPortTable": ouiFilterPortTable,
       "ouiFilterPortEntry": ouiFilterPortEntry,
       "ouiFilterPortEnable": ouiFilterPortEnable,
       "ouiFilterPortFilterMode": ouiFilterPortFilterMode,
       "dhcpSnoop": dhcpSnoop,
       "dhcpSnoopPortTable": dhcpSnoopPortTable,
       "dhcpSnoopPortEntry": dhcpSnoopPortEntry,
       "dhcpSnoopEnable": dhcpSnoopEnable,
       "dhcpSnoopMaxcnt": dhcpSnoopMaxcnt,
       "dhcpSnoopSmacverifyEnable": dhcpSnoopSmacverifyEnable,
       "dhcpSnoopTarget": dhcpSnoopTarget,
       "dhcpSnoopOps": dhcpSnoopOps,
       "dhcpStaticTable": dhcpStaticTable,
       "dhcpStaticEntry": dhcpStaticEntry,
       "dhcpStaticIpAddr": dhcpStaticIpAddr,
       "dhcpStaticRowStatus": dhcpStaticRowStatus,
       "maxNumOfDhcpStaticIp": maxNumOfDhcpStaticIp,
       "dhcpSnoopMaxcntMode": dhcpSnoopMaxcntMode,
       "acl": acl,
       "aclSetTable": aclSetTable,
       "aclSetEntry": aclSetEntry,
       "aclSetVpi": aclSetVpi,
       "aclSetVci": aclSetVci,
       "aclSetProfileName": aclSetProfileName,
       "aclSetRowStatus": aclSetRowStatus,
       "aclProfileTable": aclProfileTable,
       "aclProfileEntry": aclProfileEntry,
       "aclProfileRuleName": aclProfileRuleName,
       "aclProfileRuleNumber": aclProfileRuleNumber,
       "aclProfileActionNumber": aclProfileActionNumber,
       "aclProfileRuleParamMask": aclProfileRuleParamMask,
       "aclProfileRuleEtype": aclProfileRuleEtype,
       "aclProfileRuleVid": aclProfileRuleVid,
       "aclProfileRuleSmac": aclProfileRuleSmac,
       "aclProfileRuleDmac": aclProfileRuleDmac,
       "aclProfileRulePriority": aclProfileRulePriority,
       "aclProfileRuleProtocol": aclProfileRuleProtocol,
       "aclProfileActionRate": aclProfileActionRate,
       "aclProfileActionrvlan": aclProfileActionrvlan,
       "aclProfileActionrpri": aclProfileActionrpri,
       "aclProfileRowStatus": aclProfileRowStatus,
       "aclProfileRuleSip": aclProfileRuleSip,
       "aclProfileRuleDip": aclProfileRuleDip,
       "aclProfileRuleSport": aclProfileRuleSport,
       "aclProfileRuleDport": aclProfileRuleDport,
       "pppoeAgent": pppoeAgent,
       "pppoeAgentTable": pppoeAgentTable,
       "pppoeAgentEntry": pppoeAgentEntry,
       "pppoeAgentEnable": pppoeAgentEnable,
       "pppoeAgentInfo": pppoeAgentInfo,
       "pppoeAgentRowStatus": pppoeAgentRowStatus,
       "pppoeAgentOptionMode": pppoeAgentOptionMode,
       "maxNumOfPppoeAgentConf": maxNumOfPppoeAgentConf,
       "n1mac": n1mac,
       "n1macReplaceMac": n1macReplaceMac,
       "n1macPortTable": n1macPortTable,
       "n1macPortEntry": n1macPortEntry,
       "n1macStatusEnable": n1macStatusEnable,
       "macff": macff,
       "macFfTable": macFfTable,
       "macFfEntry": macFfEntry,
       "macFfIndex": macFfIndex,
       "macFfVid": macFfVid,
       "macFfArIP": macFfArIP,
       "macFfSrcIP": macFfSrcIP,
       "macFfSrcMask": macFfSrcMask,
       "macFfRowStatus": macFfRowStatus,
       "macFfArpFlush": macFfArpFlush,
       "maxNumOfMacFfVlanInSystem": maxNumOfMacFfVlanInSystem,
       "macFfVlanTable": macFfVlanTable,
       "macFfVlanEntry": macFfVlanEntry,
       "macFfVlanRowstatus": macFfVlanRowstatus,
       "macFfStaticIPTable": macFfStaticIPTable,
       "macFfStaticIPEntry": macFfStaticIPEntry,
       "macFfStaticIPPort": macFfStaticIPPort,
       "macFfStaticIPVid": macFfStaticIPVid,
       "macFfstaticIP": macFfstaticIP,
       "macFfStaticIPMask": macFfStaticIPMask,
       "macFfStaticIPRowStatus": macFfStaticIPRowStatus,
       "macFfServerMacTable": macFfServerMacTable,
       "macFfServerMacEntry": macFfServerMacEntry,
       "macFfServerMacVid": macFfServerMacVid,
       "macFfServerMacAddr": macFfServerMacAddr,
       "macFfServerMacRowStatus": macFfServerMacRowStatus,
       "sys": sys,
       "timeSetup": timeSetup,
       "dayLightSaving": dayLightSaving,
       "dayLightSavingAdminStatus": dayLightSavingAdminStatus,
       "dayLightSavingStartTime": dayLightSavingStartTime,
       "dayLightSavingStartMonth": dayLightSavingStartMonth,
       "dayLightSavingStartWeek": dayLightSavingStartWeek,
       "dayLightSavingStartWday": dayLightSavingStartWday,
       "dayLightSavingStartHour": dayLightSavingStartHour,
       "dayLightSavingEndTime": dayLightSavingEndTime,
       "dayLightSavingEndMonth": dayLightSavingEndMonth,
       "dayLightSavingEndWeek": dayLightSavingEndWeek,
       "dayLightSavingEndWday": dayLightSavingEndWday,
       "dayLightSavingEndHour": dayLightSavingEndHour,
       "accessCtrl": accessCtrl,
       "securedClientTable": securedClientTable,
       "securedClientEntry": securedClientEntry,
       "securedClientIndex": securedClientIndex,
       "securedClientStartIp": securedClientStartIp,
       "securedClientEndIp": securedClientEndIp,
       "securedClientService": securedClientService,
       "securedClientEnable": securedClientEnable,
       "extAlarm": extAlarm,
       "extAlarmTable": extAlarmTable,
       "extAlarmEntry": extAlarmEntry,
       "extAlarmIndex": extAlarmIndex,
       "extAlarmName": extAlarmName,
       "extAlarmStatus": extAlarmStatus,
       "extAlarmTriggeredMode": extAlarmTriggeredMode,
       "user": user,
       "userAuthMode": userAuthMode,
       "userAuthServerIp": userAuthServerIp,
       "userAuthServerPort": userAuthServerPort,
       "userAuthServerSecret": userAuthServerSecret,
       "userTable": userTable,
       "userEntry": userEntry,
       "userName": userName,
       "userPassword": userPassword,
       "userPriviledge": userPriviledge,
       "userRowStatus": userRowStatus,
       "userAuthDefaultPriviledge": userAuthDefaultPriviledge,
       "usbCastCtrl": usbCastCtrl,
       "usBcastCtrlEnable": usBcastCtrlEnable,
       "usBcastCtrlRate": usBcastCtrlRate,
       "dsQos": dsQos,
       "dsQosEnableMode": dsQosEnableMode,
       "dsQosDefaultPri": dsQosDefaultPri,
       "dsQoSOverridingTable": dsQoSOverridingTable,
       "dsQoSOverridingEntry": dsQoSOverridingEntry,
       "dsQosPriority": dsQosPriority,
       "dsQosValueList": dsQosValueList,
       "stdioTimeout": stdioTimeout,
       "isConfigChanged": isConfigChanged,
       "fwUpgrade": fwUpgrade,
       "fwUpgradeVersion": fwUpgradeVersion,
       "fwUpgradeCheck": fwUpgradeCheck,
       "fwUpgradeStatus": fwUpgradeStatus,
       "delayedReboot": delayedReboot,
       "delayedRebootTimer": delayedRebootTimer,
       "delayedRebootRemainingTime": delayedRebootRemainingTime,
       "delayedRebootCancel": delayedRebootCancel,
       "trap": trap,
       "statistics": statistics,
       "igmpQueryCntTotal": igmpQueryCntTotal,
       "igmpReportCntTotal": igmpReportCntTotal,
       "igmpLeaveCntTotal": igmpLeaveCntTotal,
       "igmpNumOfActiveGroups": igmpNumOfActiveGroups,
       "igmpGroupTable": igmpGroupTable,
       "igmpGroupEntry": igmpGroupEntry,
       "igmpGroupIp": igmpGroupIp,
       "igmpGroupvid": igmpGroupvid,
       "igmpGroupnumberOfMembers": igmpGroupnumberOfMembers,
       "igmpGroupMemberPorts": igmpGroupMemberPorts,
       "igmpGroupPortTable": igmpGroupPortTable,
       "igmpGroupPortEntry": igmpGroupPortEntry,
       "igmpGroupPortIp": igmpGroupPortIp,
       "igmpGroupPortvid": igmpGroupPortvid,
       "igmpGroupV2Table": igmpGroupV2Table,
       "igmpGroupV2Entry": igmpGroupV2Entry,
       "igmpGroupV2Vid": igmpGroupV2Vid,
       "igmpGroupV2Ip": igmpGroupV2Ip,
       "igmpGroupV2NumOfMembers": igmpGroupV2NumOfMembers,
       "igmpGroupV2MemberPorts": igmpGroupV2MemberPorts,
       "igmpGroupPortV2Table": igmpGroupPortV2Table,
       "igmpGroupPortV2Entry": igmpGroupPortV2Entry,
       "igmpGroupPortV2Vid": igmpGroupPortV2Vid,
       "igmpGroupPortV2Ip": igmpGroupPortV2Ip,
       "igmpGroupPortV2SourceIp": igmpGroupPortV2SourceIp,
       "igmpPortCtrlPduTable": igmpPortCtrlPduTable,
       "igmpPortCtrlPduEntry": igmpPortCtrlPduEntry,
       "igmpPortCtrlPduQueryCnt": igmpPortCtrlPduQueryCnt,
       "igmpPortCtrlPduReportCnt": igmpPortCtrlPduReportCnt,
       "igmpPortCtrlPduLeaveCnt": igmpPortCtrlPduLeaveCnt,
       "igmpPortNumOfActiveGroups": igmpPortNumOfActiveGroups,
       "igmpPortCtrlAuditLeaveCnt": igmpPortCtrlAuditLeaveCnt,
       "dhcpStats": dhcpStats,
       "dhcpSnoopIpTable": dhcpSnoopIpTable,
       "dhcpSnoopIpEntry": dhcpSnoopIpEntry,
       "dhcpSnoopIp": dhcpSnoopIp,
       "dhcpSnoopMac": dhcpSnoopMac,
       "dhcpSnoopVid": dhcpSnoopVid,
       "dhcpSnoopMask": dhcpSnoopMask,
       "dhcpSnoopGateway": dhcpSnoopGateway,
       "dhcpSnoopRouteMap": dhcpSnoopRouteMap,
       "dhcpSnoopCounterTable": dhcpSnoopCounterTable,
       "dhcpSnoopCounterEntry": dhcpSnoopCounterEntry,
       "dhcpDiscovery": dhcpDiscovery,
       "dhcpOffer": dhcpOffer,
       "dhcpRequest": dhcpRequest,
       "dhcpAck": dhcpAck,
       "dhcpAckBySnoopFull": dhcpAckBySnoopFull,
       "dhcpRouteTable": dhcpRouteTable,
       "dhcpRouteEntry": dhcpRouteEntry,
       "dhcpRouteIndex": dhcpRouteIndex,
       "dhcpRouteVid": dhcpRouteVid,
       "dhcpRouteIP": dhcpRouteIP,
       "dhcpRouteMask": dhcpRouteMask,
       "dhcpRouteGwIP": dhcpRouteGwIP,
       "paepvcStats": paepvcStats,
       "paepvcSessionTable": paepvcSessionTable,
       "paepvcSessionEntry": paepvcSessionEntry,
       "paepvcSessionVpi": paepvcSessionVpi,
       "paepvcSessionVci": paepvcSessionVci,
       "paepvcSessionState": paepvcSessionState,
       "paepvcSessionId": paepvcSessionId,
       "paepvcSessionUptime": paepvcSessionUptime,
       "paepvcSessionacname": paepvcSessionacname,
       "paepvcSessionsrvcname": paepvcSessionsrvcname,
       "paepvcCountTable": paepvcCountTable,
       "paepvcCountEntry": paepvcCountEntry,
       "paepvcCountVpi": paepvcCountVpi,
       "paepvcCountVci": paepvcCountVci,
       "paepvcCountPppLcpCfgReqRx": paepvcCountPppLcpCfgReqRx,
       "paepvcCountPppLcpEchoReqRx": paepvcCountPppLcpEchoReqRx,
       "paepvcCountPppLcpEchoReplyRx": paepvcCountPppLcpEchoReplyRx,
       "paepvcCountPadiTx": paepvcCountPadiTx,
       "paepvcCountPadoRx": paepvcCountPadoRx,
       "paepvcCountPadrTx": paepvcCountPadrTx,
       "paepvcCountPadsRx": paepvcCountPadsRx,
       "paepvcCountPadtTx": paepvcCountPadtTx,
       "paepvcCountPadtRx": paepvcCountPadtRx,
       "paepvcCountSrvcnameErrRx": paepvcCountSrvcnameErrRx,
       "paepvcCountAcSystemErrRx": paepvcCountAcSystemErrRx,
       "paepvcCountGenericErrTx": paepvcCountGenericErrTx,
       "paepvcCountGenericErrRx": paepvcCountGenericErrRx,
       "macStats": macStats,
       "macDisplayTarget": macDisplayTarget,
       "macTable": macTable,
       "macEntry": macEntry,
       "macAddress": macAddress,
       "macPort": macPort,
       "macStatus": macStatus,
       "macVid": macVid,
       "n1macStats": n1macStats,
       "n1macTable": n1macTable,
       "n1macEntry": n1macEntry,
       "n1macProtoVal": n1macProtoVal,
       "n1macProtoType": n1macProtoType,
       "n1macMacAddr": n1macMacAddr,
       "enetStats": enetStats,
       "enetPrimaryPort": enetPrimaryPort,
       "enetSfpInfoTable": enetSfpInfoTable,
       "enetSfpInfoEntry": enetSfpInfoEntry,
       "enetSfpInfoTxpower": enetSfpInfoTxpower,
       "enetSfpInfoRxpower": enetSfpInfoRxpower,
       "enetSfpInfoTemperature": enetSfpInfoTemperature,
       "enetSfpInfoTxBias": enetSfpInfoTxBias,
       "enetSfpInfoVoltage": enetSfpInfoVoltage,
       "vdslStats": vdslStats,
       "vdslLineStatsTable": vdslLineStatsTable,
       "vdslLineStatsEntry": vdslLineStatsEntry,
       "vdslLineStatsVtucBits1": vdslLineStatsVtucBits1,
       "vdslLineStatsVtucBits2": vdslLineStatsVtucBits2,
       "vdslLineStatsVtucBits3": vdslLineStatsVtucBits3,
       "vdslLineStatsVtucBits4": vdslLineStatsVtucBits4,
       "vdslLineStatsVturBits1": vdslLineStatsVturBits1,
       "vdslLineStatsVturBits2": vdslLineStatsVturBits2,
       "vdslLineStatsVturBits3": vdslLineStatsVturBits3,
       "vdslLineStatsVturBits4": vdslLineStatsVturBits4,
       "vdslLineStatsVtucGain1": vdslLineStatsVtucGain1,
       "vdslLineStatsVtucGain2": vdslLineStatsVtucGain2,
       "vdslLineStatsVtucGain3": vdslLineStatsVtucGain3,
       "vdslLineStatsVtucGain4": vdslLineStatsVtucGain4,
       "vdslLineStatsVtucGain5": vdslLineStatsVtucGain5,
       "vdslLineStatsVtucGain6": vdslLineStatsVtucGain6,
       "vdslLineStatsVtucGain7": vdslLineStatsVtucGain7,
       "vdslLineStatsVtucGain8": vdslLineStatsVtucGain8,
       "vdslLineStatsVturGain1": vdslLineStatsVturGain1,
       "vdslLineStatsVturGain2": vdslLineStatsVturGain2,
       "vdslLineStatsVturGain3": vdslLineStatsVturGain3,
       "vdslLineStatsVturGain4": vdslLineStatsVturGain4,
       "vdslLineStatsVturGain5": vdslLineStatsVturGain5,
       "vdslLineStatsVturGain6": vdslLineStatsVturGain6,
       "vdslLineStatsVturGain7": vdslLineStatsVturGain7,
       "vdslLineStatsVturGain8": vdslLineStatsVturGain8,
       "vdslLineStatsVtucHlog": vdslLineStatsVtucHlog,
       "vdslLineStatsVturHlog": vdslLineStatsVturHlog,
       "vdslLineStatsVtucQln": vdslLineStatsVtucQln,
       "vdslLineStatsVturQln": vdslLineStatsVturQln,
       "vdslLineStatsVtucSnr": vdslLineStatsVtucSnr,
       "vdslLineStatsVturSnr": vdslLineStatsVturSnr,
       "vdslLineStatsVtucTssi": vdslLineStatsVtucTssi,
       "vdslLineStatsVturTssi": vdslLineStatsVturTssi,
       "vdslLineStatsProtocol": vdslLineStatsProtocol,
       "voipStats": voipStats,
       "voipLineStatusTable": voipLineStatusTable,
       "voipLineStatusEntry": voipLineStatusEntry,
       "voipLineStatusPhoneStatus": voipLineStatusPhoneStatus,
       "voipLineStatusServiceStatus": voipLineStatusServiceStatus,
       "voipLineInfoTable": voipLineInfoTable,
       "voipLineInfoEntry": voipLineInfoEntry,
       "voipLineInfoSipLocalUri": voipLineInfoSipLocalUri,
       "voipLineInfoSipRemoteUri": voipLineInfoSipRemoteUri,
       "voipLineInfoRtpTxCodecType": voipLineInfoRtpTxCodecType,
       "voipLineInfoRtpRxCodecType": voipLineInfoRtpRxCodecType,
       "voipLineInfoRtpTxPt": voipLineInfoRtpTxPt,
       "voipLineInfoRtpRxPt": voipLineInfoRtpRxPt,
       "voipLineInfoRtpLocalIp": voipLineInfoRtpLocalIp,
       "voipLineInfoRtpRemoteIp": voipLineInfoRtpRemoteIp,
       "voipLineInfoRtpLocalPort": voipLineInfoRtpLocalPort,
       "voipLineInfoRtpRemotePort": voipLineInfoRtpRemotePort,
       "voipLineInfoSipLocalUri2": voipLineInfoSipLocalUri2,
       "voipLineInfoSipRemoteUri2": voipLineInfoSipRemoteUri2,
       "voipLineInfoRtpTxCodecType2": voipLineInfoRtpTxCodecType2,
       "voipLineInfoRtpRxCodecType2": voipLineInfoRtpRxCodecType2,
       "voipLineInfoRtpTxPt2": voipLineInfoRtpTxPt2,
       "voipLineInfoRtpRxPt2": voipLineInfoRtpRxPt2,
       "voipLineInfoRtpLocalIp2": voipLineInfoRtpLocalIp2,
       "voipLineInfoRtpRemoteIp2": voipLineInfoRtpRemoteIp2,
       "voipLineInfoRtpLocalPort2": voipLineInfoRtpLocalPort2,
       "voipLineInfoRtpRemotePort2": voipLineInfoRtpRemotePort2,
       "voipH248Status": voipH248Status,
       "voipH248StatusMgName": voipH248StatusMgName,
       "voipH248StatusMgStatus": voipH248StatusMgStatus,
       "voipActiveCallStat": voipActiveCallStat,
       "voipActiveCallStatCurrentActiveCalls": voipActiveCallStatCurrentActiveCalls,
       "voipActiveCallStatFailAttempts": voipActiveCallStatFailAttempts,
       "voipActiveCallStatClear": voipActiveCallStatClear,
       "macffStats": macffStats,
       "macFfStatsTable": macFfStatsTable,
       "macFfStatsEntry": macFfStatsEntry,
       "macFfStatsIndex": macFfStatsIndex,
       "macFfStatsVid": macFfStatsVid,
       "macFfStatsArIP": macFfStatsArIP,
       "macFfStatsSrcIP": macFfStatsSrcIP,
       "macFfStatsSrcMask": macFfStatsSrcMask,
       "macFfArpTable": macFfArpTable,
       "macFfArpEntry": macFfArpEntry,
       "macFfArpVid": macFfArpVid,
       "macFfArpIP": macFfArpIP,
       "macFfArpPort": macFfArpPort,
       "macFfArpMac": macFfArpMac,
       "macFfArpCounterTable": macFfArpCounterTable,
       "macFfArpCounterEntry": macFfArpCounterEntry,
       "macFfArpCounterRequestTX": macFfArpCounterRequestTX,
       "macFfArpCounterRequestRX": macFfArpCounterRequestRX,
       "macFfArpCounterRequestRXDrop": macFfArpCounterRequestRXDrop,
       "macFfArpCounterReplyTX": macFfArpCounterReplyTX,
       "macFfArpCounterReplyRX": macFfArpCounterReplyRX,
       "macFfArpCounterReplyRXDrop": macFfArpCounterReplyRXDrop,
       "adslStats": adslStats,
       "adslPortUtilTable": adslPortUtilTable,
       "adslPortUtilEntry": adslPortUtilEntry,
       "adslPortUtilTx": adslPortUtilTx,
       "adslPortUtilRx": adslPortUtilRx,
       "adslStatsXturInp": adslStatsXturInp,
       "adslStatsXtucInp": adslStatsXtucInp,
       "clear": clear,
       "counterClearTarget": counterClearTarget,
       "counterClearOps": counterClearOps,
       "counterClearVpi": counterClearVpi,
       "counterClearVci": counterClearVci,
       "voip": voip,
       "voipArp": voipArp,
       "voipArpFlushOps": voipArpFlushOps,
       "voipArpShowTable": voipArpShowTable,
       "voipArpShowEntry": voipArpShowEntry,
       "voipArpShowIp": voipArpShowIp,
       "voipArpShowMac": voipArpShowMac,
       "voipSip": voipSip,
       "maxNumOfVoipNumberPlan": maxNumOfVoipNumberPlan,
       "voipNumberPlanTable": voipNumberPlanTable,
       "voipNumberPlanEntry": voipNumberPlanEntry,
       "voipNumberPlanName": voipNumberPlanName,
       "voipNumberPlanIndex": voipNumberPlanIndex,
       "voipNumberPlanPattern": voipNumberPlanPattern,
       "voipNumberPlanRule": voipNumberPlanRule,
       "voipNumberPlanRowStatus": voipNumberPlanRowStatus,
       "voipNumberPlanDftTable": voipNumberPlanDftTable,
       "voipNumberPlanDftEntry": voipNumberPlanDftEntry,
       "voipNumberPlanDftRule": voipNumberPlanDftRule,
       "digitSetup": digitSetup,
       "timeoutSetup": timeoutSetup,
       "initialTimeout": initialTimeout,
       "interDigitTimeout": interDigitTimeout,
       "digitPauseTimeout": digitPauseTimeout,
       "matchingTimeout": matchingTimeout,
       "voipIp": voipIp,
       "voipIpSetIp": voipIpSetIp,
       "voipIpSetVid": voipIpSetVid,
       "voipIpSetMask": voipIpSetMask,
       "voipIpSetDhcpClientEnable": voipIpSetDhcpClientEnable,
       "voipIpGateway": voipIpGateway,
       "voipDns": voipDns,
       "voipDnsIp": voipDnsIp,
       "maxNumOfVoipRoute": maxNumOfVoipRoute,
       "voipRouteTable": voipRouteTable,
       "voipRouteEntry": voipRouteEntry,
       "voipRouteIp": voipRouteIp,
       "voipRouteGateway": voipRouteGateway,
       "voipRouteMask": voipRouteMask,
       "voipRouteMetric": voipRouteMetric,
       "voipRouteRowStatus": voipRouteRowStatus,
       "voipCountryCode": voipCountryCode,
       "voipH248": voipH248,
       "maxNumOfVoipH248MgConf": maxNumOfVoipH248MgConf,
       "voipH248MgConf": voipH248MgConf,
       "voipH248MgName": voipH248MgName,
       "voipH248MgEnable": voipH248MgEnable,
       "voipH248MgH248Profile": voipH248MgH248Profile,
       "voipH248MgPort": voipH248MgPort,
       "voipRing": voipRing,
       "voipRingTable": voipRingTable,
       "voipRingEntry": voipRingEntry,
       "voipRingIndex": voipRingIndex,
       "voipRingName": voipRingName,
       "voipRingOn1": voipRingOn1,
       "voipRingOff1": voipRingOff1,
       "voipRingOn2": voipRingOn2,
       "voipRingOff2": voipRingOff2,
       "voipRingOn3": voipRingOn3,
       "voipRingOff3": voipRingOff3,
       "voipRingSetDefault": voipRingSetDefault,
       "voipBootRegDelay": voipBootRegDelay,
       "voipActiveCall": voipActiveCall,
       "voipActiveCallMaxActiveCalls": voipActiveCallMaxActiveCalls,
       "voipActiveCallThreshold": voipActiveCallThreshold,
       "voipMode": voipMode,
       "aesSeriesCommon": aesSeriesCommon,
       "iesSeriesCommon": iesSeriesCommon,
       "accessSwitchCommonATM": accessSwitchCommonATM}
)
