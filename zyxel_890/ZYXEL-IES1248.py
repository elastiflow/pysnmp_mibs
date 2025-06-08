# SNMP MIB module (ZYXEL-IES1248) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/zyxel_890/ZYXEL-IES1248.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 10:07:44 2025
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
 Timeout,
 dot1dBasePort) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "BridgeId",
    "Timeout",
    "dot1dBasePort")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

ies1248 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Zyxel_ObjectIdentity = ObjectIdentity
zyxel = _Zyxel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1)
)
_AccessSwitch_ObjectIdentity = ObjectIdentity
accessSwitch = _AccessSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5)
)
_IesSeries_ObjectIdentity = ObjectIdentity
iesSeries = _IesSeries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13)
)
_Alarmconf_ObjectIdentity = ObjectIdentity
alarmconf = _Alarmconf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 2)
)
_AlarmOps_Type = Integer32
_AlarmOps_Object = MibScalar
alarmOps = _AlarmOps_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 2, 1),
    _AlarmOps_Type()
)
alarmOps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmOps.setStatus("current")
_AlarmConfTable_Object = MibTable
alarmConfTable = _AlarmConfTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 2, 2)
)
if mibBuilder.loadTexts:
    alarmConfTable.setStatus("current")
_AlarmConfEntry_Object = MibTableRow
alarmConfEntry = _AlarmConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 2, 2, 1)
)
alarmConfEntry.setIndexNames(
    (0, "ZYXEL-IES1248", "alarmConfId"),
)
if mibBuilder.loadTexts:
    alarmConfEntry.setStatus("current")
_AlarmConfId_Type = Integer32
_AlarmConfId_Object = MibTableColumn
alarmConfId = _AlarmConfId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 2, 2, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 2, 2, 1, 2),
    _AlarmConfFacility_Type()
)
alarmConfFacility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmConfFacility.setStatus("current")
_AlarmConfTarget_Type = Integer32
_AlarmConfTarget_Object = MibTableColumn
alarmConfTarget = _AlarmConfTarget_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 2, 2, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 2, 2, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 2, 2, 1, 5),
    _AlarmConfClearable_Type()
)
alarmConfClearable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmConfClearable.setStatus("current")
_AlarmCurrTable_Object = MibTable
alarmCurrTable = _AlarmCurrTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 2, 3)
)
if mibBuilder.loadTexts:
    alarmCurrTable.setStatus("current")
_AlarmCurrEntry_Object = MibTableRow
alarmCurrEntry = _AlarmCurrEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 2, 3, 1)
)
alarmCurrEntry.setIndexNames(
    (0, "ZYXEL-IES1248", "alarmCurrIndex"),
)
if mibBuilder.loadTexts:
    alarmCurrEntry.setStatus("current")
_AlarmCurrIndex_Type = Integer32
_AlarmCurrIndex_Object = MibTableColumn
alarmCurrIndex = _AlarmCurrIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 2, 3, 1, 1),
    _AlarmCurrIndex_Type()
)
alarmCurrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmCurrIndex.setStatus("current")
_AlarmCurrOccurTime_Type = TimeTicks
_AlarmCurrOccurTime_Object = MibTableColumn
alarmCurrOccurTime = _AlarmCurrOccurTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 2, 3, 1, 2),
    _AlarmCurrOccurTime_Type()
)
alarmCurrOccurTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmCurrOccurTime.setStatus("current")
_AlarmCurrTrapOid_Type = ObjectIdentifier
_AlarmCurrTrapOid_Object = MibTableColumn
alarmCurrTrapOid = _AlarmCurrTrapOid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 2, 3, 1, 3),
    _AlarmCurrTrapOid_Type()
)
alarmCurrTrapOid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmCurrTrapOid.setStatus("current")
_AlarmCurrParam1_Type = Integer32
_AlarmCurrParam1_Object = MibTableColumn
alarmCurrParam1 = _AlarmCurrParam1_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 2, 3, 1, 4),
    _AlarmCurrParam1_Type()
)
alarmCurrParam1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmCurrParam1.setStatus("current")
_AlarmCurrParam2_Type = Integer32
_AlarmCurrParam2_Object = MibTableColumn
alarmCurrParam2 = _AlarmCurrParam2_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 2, 3, 1, 5),
    _AlarmCurrParam2_Type()
)
alarmCurrParam2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmCurrParam2.setStatus("current")
_AlarmCurrParam3_Type = Integer32
_AlarmCurrParam3_Object = MibTableColumn
alarmCurrParam3 = _AlarmCurrParam3_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 2, 3, 1, 6),
    _AlarmCurrParam3_Type()
)
alarmCurrParam3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmCurrParam3.setStatus("current")
_AlarmCurrParam4_Type = Integer32
_AlarmCurrParam4_Object = MibTableColumn
alarmCurrParam4 = _AlarmCurrParam4_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 2, 3, 1, 7),
    _AlarmCurrParam4_Type()
)
alarmCurrParam4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmCurrParam4.setStatus("current")
_AlarmCurrParam5_Type = Integer32
_AlarmCurrParam5_Object = MibTableColumn
alarmCurrParam5 = _AlarmCurrParam5_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 2, 3, 1, 8),
    _AlarmCurrParam5_Type()
)
alarmCurrParam5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmCurrParam5.setStatus("current")
_AlarmCurrParam6_Type = Integer32
_AlarmCurrParam6_Object = MibTableColumn
alarmCurrParam6 = _AlarmCurrParam6_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 2, 3, 1, 9),
    _AlarmCurrParam6_Type()
)
alarmCurrParam6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmCurrParam6.setStatus("current")
_AlarmCurrParam7_Type = Integer32
_AlarmCurrParam7_Object = MibTableColumn
alarmCurrParam7 = _AlarmCurrParam7_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 2, 3, 1, 10),
    _AlarmCurrParam7_Type()
)
alarmCurrParam7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmCurrParam7.setStatus("current")
_AlarmCurrParam8_Type = Integer32
_AlarmCurrParam8_Object = MibTableColumn
alarmCurrParam8 = _AlarmCurrParam8_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 2, 3, 1, 11),
    _AlarmCurrParam8_Type()
)
alarmCurrParam8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmCurrParam8.setStatus("current")
_AlarmCurrTimeDescr_Type = DisplayString
_AlarmCurrTimeDescr_Object = MibTableColumn
alarmCurrTimeDescr = _AlarmCurrTimeDescr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 2, 3, 1, 12),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 2, 3, 1, 13),
    _AlarmCurrSeverity_Type()
)
alarmCurrSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmCurrSeverity.setStatus("current")
_AlarmCurrDescr_Type = DisplayString
_AlarmCurrDescr_Object = MibTableColumn
alarmCurrDescr = _AlarmCurrDescr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 2, 3, 1, 14),
    _AlarmCurrDescr_Type()
)
alarmCurrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmCurrDescr.setStatus("current")
_AlarmSeverityPortTable_Object = MibTable
alarmSeverityPortTable = _AlarmSeverityPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 2, 4)
)
if mibBuilder.loadTexts:
    alarmSeverityPortTable.setStatus("current")
_AlarmSeverityPortEntry_Object = MibTableRow
alarmSeverityPortEntry = _AlarmSeverityPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 2, 4, 1)
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 2, 4, 1, 1),
    _SeverityThresh_Type()
)
severityThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityThresh.setStatus("current")
_Diagnostic_ObjectIdentity = ObjectIdentity
diagnostic = _Diagnostic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 4)
)
_Selt_ObjectIdentity = ObjectIdentity
selt = _Selt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 4, 3)
)
_SeltTarget_Type = Integer32
_SeltTarget_Object = MibScalar
seltTarget = _SeltTarget_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 4, 3, 1),
    _SeltTarget_Type()
)
seltTarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    seltTarget.setStatus("current")
_SeltOps_Type = Integer32
_SeltOps_Object = MibScalar
seltOps = _SeltOps_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 4, 3, 2),
    _SeltOps_Type()
)
seltOps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    seltOps.setStatus("current")
_SeltStatus_Type = DisplayString
_SeltStatus_Object = MibScalar
seltStatus = _SeltStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 4, 3, 3),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 4, 3, 4),
    _SeltCableType_Type()
)
seltCableType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    seltCableType.setStatus("current")
_SeltLoopEstimateLengthFt_Type = Integer32
_SeltLoopEstimateLengthFt_Object = MibScalar
seltLoopEstimateLengthFt = _SeltLoopEstimateLengthFt_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 4, 3, 5),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 4, 3, 6),
    _SeltLoopEstimateLengthMeter_Type()
)
seltLoopEstimateLengthMeter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    seltLoopEstimateLengthMeter.setStatus("current")
if mibBuilder.loadTexts:
    seltLoopEstimateLengthMeter.setUnits("meter")
_Multicast_ObjectIdentity = ObjectIdentity
multicast = _Multicast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 7)
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 7, 1),
    _IgmpEnable_Type()
)
igmpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpEnable.setStatus("current")
_McastBandwidth_ObjectIdentity = ObjectIdentity
mcastBandwidth = _McastBandwidth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 7, 4)
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 7, 4, 1),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 7, 4, 2),
    _MaxNumOfMcastBw_Type()
)
maxNumOfMcastBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumOfMcastBw.setStatus("current")
_McastBwTable_Object = MibTable
mcastBwTable = _McastBwTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 7, 4, 3)
)
if mibBuilder.loadTexts:
    mcastBwTable.setStatus("current")
_McastBwEntry_Object = MibTableRow
mcastBwEntry = _McastBwEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 7, 4, 3, 1)
)
mcastBwEntry.setIndexNames(
    (0, "ZYXEL-IES1248", "mcastBwIndex"),
    (0, "ZYXEL-IES1248", "mcastBwStartIp"),
    (0, "ZYXEL-IES1248", "mcastBwEndIp"),
)
if mibBuilder.loadTexts:
    mcastBwEntry.setStatus("current")
_McastBwIndex_Type = Integer32
_McastBwIndex_Object = MibTableColumn
mcastBwIndex = _McastBwIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 7, 4, 3, 1, 1),
    _McastBwIndex_Type()
)
mcastBwIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcastBwIndex.setStatus("current")
_McastBwStartIp_Type = IpAddress
_McastBwStartIp_Object = MibTableColumn
mcastBwStartIp = _McastBwStartIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 7, 4, 3, 1, 2),
    _McastBwStartIp_Type()
)
mcastBwStartIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcastBwStartIp.setStatus("current")
_McastBwEndIp_Type = IpAddress
_McastBwEndIp_Object = MibTableColumn
mcastBwEndIp = _McastBwEndIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 7, 4, 3, 1, 3),
    _McastBwEndIp_Type()
)
mcastBwEndIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcastBwEndIp.setStatus("current")
_McastBwBandwidth_Type = Integer32
_McastBwBandwidth_Object = MibTableColumn
mcastBwBandwidth = _McastBwBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 7, 4, 3, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 7, 4, 3, 1, 5),
    _McastBwRowStatus_Type()
)
mcastBwRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mcastBwRowStatus.setStatus("current")
_McastBwPortTable_Object = MibTable
mcastBwPortTable = _McastBwPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 7, 4, 4)
)
if mibBuilder.loadTexts:
    mcastBwPortTable.setStatus("current")
_McastBwPortEntry_Object = MibTableRow
mcastBwPortEntry = _McastBwPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 7, 4, 4, 1)
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 7, 4, 4, 1, 1),
    _McastBwPortEnable_Type()
)
mcastBwPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcastBwPortEnable.setStatus("current")
_McastBwPortBandwidth_Type = Integer32
_McastBwPortBandwidth_Object = MibTableColumn
mcastBwPortBandwidth = _McastBwPortBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 7, 4, 4, 1, 2),
    _McastBwPortBandwidth_Type()
)
mcastBwPortBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcastBwPortBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    mcastBwPortBandwidth.setUnits("Kbps")
_IgmpCount_ObjectIdentity = ObjectIdentity
igmpCount = _IgmpCount_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 7, 5)
)
_IgmpCountPortTable_Object = MibTable
igmpCountPortTable = _IgmpCountPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 7, 5, 1)
)
if mibBuilder.loadTexts:
    igmpCountPortTable.setStatus("current")
_IgmpCountPortEntry_Object = MibTableRow
igmpCountPortEntry = _IgmpCountPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 7, 5, 1, 1)
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 7, 5, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 7, 5, 1, 1, 2),
    _IgmpCountPortLimit_Type()
)
igmpCountPortLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpCountPortLimit.setStatus("current")
_Mvlan_ObjectIdentity = ObjectIdentity
mvlan = _Mvlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 7, 6)
)
_MaxNumOfMvlan_Type = Integer32
_MaxNumOfMvlan_Object = MibScalar
maxNumOfMvlan = _MaxNumOfMvlan_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 7, 6, 1),
    _MaxNumOfMvlan_Type()
)
maxNumOfMvlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumOfMvlan.setStatus("current")
_MvlanTable_Object = MibTable
mvlanTable = _MvlanTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 7, 6, 2)
)
if mibBuilder.loadTexts:
    mvlanTable.setStatus("current")
_MvlanEntry_Object = MibTableRow
mvlanEntry = _MvlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 7, 6, 2, 1)
)
mvlanEntry.setIndexNames(
    (0, "ZYXEL-IES1248", "mvlanIndex"),
)
if mibBuilder.loadTexts:
    mvlanEntry.setStatus("current")
_MvlanIndex_Type = VlanIndex
_MvlanIndex_Object = MibTableColumn
mvlanIndex = _MvlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 7, 6, 2, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 7, 6, 2, 1, 2),
    _MvlanName_Type()
)
mvlanName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mvlanName.setStatus("current")
_MvlanEgressPorts_Type = PortList
_MvlanEgressPorts_Object = MibTableColumn
mvlanEgressPorts = _MvlanEgressPorts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 7, 6, 2, 1, 3),
    _MvlanEgressPorts_Type()
)
mvlanEgressPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mvlanEgressPorts.setStatus("current")
_MvlanUntaggedPorts_Type = PortList
_MvlanUntaggedPorts_Object = MibTableColumn
mvlanUntaggedPorts = _MvlanUntaggedPorts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 7, 6, 2, 1, 4),
    _MvlanUntaggedPorts_Type()
)
mvlanUntaggedPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mvlanUntaggedPorts.setStatus("current")
_MvlanRowStatus_Type = RowStatus
_MvlanRowStatus_Object = MibTableColumn
mvlanRowStatus = _MvlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 7, 6, 2, 1, 5),
    _MvlanRowStatus_Type()
)
mvlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mvlanRowStatus.setStatus("current")
_MvlanTranslateTable_Object = MibTable
mvlanTranslateTable = _MvlanTranslateTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 7, 6, 3)
)
if mibBuilder.loadTexts:
    mvlanTranslateTable.setStatus("current")
_MvlanTranslateEntry_Object = MibTableRow
mvlanTranslateEntry = _MvlanTranslateEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 7, 6, 3, 1)
)
mvlanTranslateEntry.setIndexNames(
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
    (0, "ZYXEL-IES1248", "mvlanTranslateIndex"),
)
if mibBuilder.loadTexts:
    mvlanTranslateEntry.setStatus("current")
_MvlanTranslateIndex_Type = Integer32
_MvlanTranslateIndex_Object = MibTableColumn
mvlanTranslateIndex = _MvlanTranslateIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 7, 6, 3, 1, 1),
    _MvlanTranslateIndex_Type()
)
mvlanTranslateIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvlanTranslateIndex.setStatus("current")
_MvlanTranslateStartIp_Type = IpAddress
_MvlanTranslateStartIp_Object = MibTableColumn
mvlanTranslateStartIp = _MvlanTranslateStartIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 7, 6, 3, 1, 2),
    _MvlanTranslateStartIp_Type()
)
mvlanTranslateStartIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvlanTranslateStartIp.setStatus("current")
_MvlanTranslateEndIp_Type = IpAddress
_MvlanTranslateEndIp_Object = MibTableColumn
mvlanTranslateEndIp = _MvlanTranslateEndIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 7, 6, 3, 1, 3),
    _MvlanTranslateEndIp_Type()
)
mvlanTranslateEndIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvlanTranslateEndIp.setStatus("current")
_QueryVid_ObjectIdentity = ObjectIdentity
queryVid = _QueryVid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 7, 7)
)
_MaxNumOfQryVid_Type = Integer32
_MaxNumOfQryVid_Object = MibScalar
maxNumOfQryVid = _MaxNumOfQryVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 7, 7, 1),
    _MaxNumOfQryVid_Type()
)
maxNumOfQryVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumOfQryVid.setStatus("current")
_QryVidConfTable_Object = MibTable
qryVidConfTable = _QryVidConfTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 7, 7, 2)
)
if mibBuilder.loadTexts:
    qryVidConfTable.setStatus("current")
_QryVidConfEntry_Object = MibTableRow
qryVidConfEntry = _QryVidConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 7, 7, 2, 1)
)
qryVidConfEntry.setIndexNames(
    (0, "ZYXEL-IES1248", "qryVid"),
)
if mibBuilder.loadTexts:
    qryVidConfEntry.setStatus("current")
_QryVid_Type = Integer32
_QryVid_Object = MibTableColumn
qryVid = _QryVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 7, 7, 2, 1, 1),
    _QryVid_Type()
)
qryVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qryVid.setStatus("current")
_QryVidRowStatus_Type = RowStatus
_QryVidRowStatus_Object = MibTableColumn
qryVidRowStatus = _QryVidRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 7, 7, 2, 1, 2),
    _QryVidRowStatus_Type()
)
qryVidRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qryVidRowStatus.setStatus("current")
_QryVidStatusTable_Object = MibTable
qryVidStatusTable = _QryVidStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 7, 7, 3)
)
if mibBuilder.loadTexts:
    qryVidStatusTable.setStatus("current")
_QryVidStatusEntry_Object = MibTableRow
qryVidStatusEntry = _QryVidStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 7, 7, 3, 1)
)
qryVidStatusEntry.setIndexNames(
    (0, "ZYXEL-IES1248", "qryVid"),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 7, 7, 3, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 7, 9),
    _IgmpVersion_Type()
)
igmpVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpVersion.setStatus("current")
_Port_ObjectIdentity = ObjectIdentity
port = _Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8)
)
_SubrPortTable_Object = MibTable
subrPortTable = _SubrPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 1)
)
if mibBuilder.loadTexts:
    subrPortTable.setStatus("current")
_SubrPortEntry_Object = MibTableRow
subrPortEntry = _SubrPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 1, 1)
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 1, 1, 2),
    _SubrPortTel_Type()
)
subrPortTel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subrPortTel.setStatus("current")
_AdslPort_ObjectIdentity = ObjectIdentity
adslPort = _AdslPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 2)
)
_AdslLineConfTable_Object = MibTable
adslLineConfTable = _AdslLineConfTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 2, 1)
)
if mibBuilder.loadTexts:
    adslLineConfTable.setStatus("current")
_AdslLineConfEntry_Object = MibTableRow
adslLineConfEntry = _AdslLineConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 2, 1, 1)
)
adslLineConfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adslLineConfEntry.setStatus("current")


class _AdslLineConfAdslMode_Type(Integer32):
    """Custom type adslLineConfAdslMode based on Integer32"""
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
        *(("gDotLite", 1),
          ("gDotDmt", 2),
          ("t1Dot413", 3),
          ("auto", 4),
          ("etsi", 5),
          ("adsl2", 6),
          ("adsl2Plus", 7))
    )


_AdslLineConfAdslMode_Type.__name__ = "Integer32"
_AdslLineConfAdslMode_Object = MibTableColumn
adslLineConfAdslMode = _AdslLineConfAdslMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 2, 1, 1, 1),
    _AdslLineConfAdslMode_Type()
)
adslLineConfAdslMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adslLineConfAdslMode.setStatus("current")


class _AdslLineConfAnnexL_Type(Integer32):
    """Custom type adslLineConfAnnexL based on Integer32"""
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
        *(("enableWideMode", 1),
          ("enableNarrowMode", 2),
          ("enableBothMode", 3),
          ("disable", 4))
    )


_AdslLineConfAnnexL_Type.__name__ = "Integer32"
_AdslLineConfAnnexL_Object = MibTableColumn
adslLineConfAnnexL = _AdslLineConfAnnexL_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 2, 1, 1, 2),
    _AdslLineConfAnnexL_Type()
)
adslLineConfAnnexL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adslLineConfAnnexL.setStatus("current")


class _AdslLineConfAnnexM_Type(Integer32):
    """Custom type adslLineConfAnnexM based on Integer32"""
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


_AdslLineConfAnnexM_Type.__name__ = "Integer32"
_AdslLineConfAnnexM_Object = MibTableColumn
adslLineConfAnnexM = _AdslLineConfAnnexM_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 2, 1, 1, 3),
    _AdslLineConfAnnexM_Type()
)
adslLineConfAnnexM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adslLineConfAnnexM.setStatus("current")


class _AdslLineConfAnnexI_Type(Integer32):
    """Custom type adslLineConfAnnexI based on Integer32"""
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


_AdslLineConfAnnexI_Type.__name__ = "Integer32"
_AdslLineConfAnnexI_Object = MibTableColumn
adslLineConfAnnexI = _AdslLineConfAnnexI_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 2, 1, 1, 4),
    _AdslLineConfAnnexI_Type()
)
adslLineConfAnnexI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adslLineConfAnnexI.setStatus("current")
_AdslLineConfOptionMask_Type = Integer32
_AdslLineConfOptionMask_Object = MibTableColumn
adslLineConfOptionMask = _AdslLineConfOptionMask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 2, 1, 1, 5),
    _AdslLineConfOptionMask_Type()
)
adslLineConfOptionMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adslLineConfOptionMask.setStatus("current")


class _AdslLineConfPowerMgmt_Type(Integer32):
    """Custom type adslLineConfPowerMgmt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enableL2", 1),
          ("enableL2andL3", 2),
          ("disable", 3))
    )


_AdslLineConfPowerMgmt_Type.__name__ = "Integer32"
_AdslLineConfPowerMgmt_Object = MibTableColumn
adslLineConfPowerMgmt = _AdslLineConfPowerMgmt_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 2, 1, 1, 6),
    _AdslLineConfPowerMgmt_Type()
)
adslLineConfPowerMgmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adslLineConfPowerMgmt.setStatus("current")


class _AdslLineConfPowerMode_Type(Integer32):
    """Custom type adslLineConfPowerMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fix", 1),
          ("priorityToPower", 2),
          ("priorityToRate", 3))
    )


_AdslLineConfPowerMode_Type.__name__ = "Integer32"
_AdslLineConfPowerMode_Object = MibTableColumn
adslLineConfPowerMode = _AdslLineConfPowerMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 2, 1, 1, 7),
    _AdslLineConfPowerMode_Type()
)
adslLineConfPowerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adslLineConfPowerMode.setStatus("current")


class _AdslLineConfAturMaxTxPower_Type(Integer32):
    """Custom type adslLineConfAturMaxTxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-130, 200),
    )


_AdslLineConfAturMaxTxPower_Type.__name__ = "Integer32"
_AdslLineConfAturMaxTxPower_Object = MibTableColumn
adslLineConfAturMaxTxPower = _AdslLineConfAturMaxTxPower_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 2, 1, 1, 8),
    _AdslLineConfAturMaxTxPower_Type()
)
adslLineConfAturMaxTxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adslLineConfAturMaxTxPower.setStatus("current")
if mibBuilder.loadTexts:
    adslLineConfAturMaxTxPower.setUnits("tenth dBm")


class _AdslLineConfAtucMaxTxPower_Type(Integer32):
    """Custom type adslLineConfAtucMaxTxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 200),
    )


_AdslLineConfAtucMaxTxPower_Type.__name__ = "Integer32"
_AdslLineConfAtucMaxTxPower_Object = MibTableColumn
adslLineConfAtucMaxTxPower = _AdslLineConfAtucMaxTxPower_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 2, 1, 1, 9),
    _AdslLineConfAtucMaxTxPower_Type()
)
adslLineConfAtucMaxTxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adslLineConfAtucMaxTxPower.setStatus("current")
if mibBuilder.loadTexts:
    adslLineConfAtucMaxTxPower.setUnits("tenth dBm")


class _AdslLineConfMaxRxPower_Type(Integer32):
    """Custom type adslLineConfMaxRxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-255, 255),
    )


_AdslLineConfMaxRxPower_Type.__name__ = "Integer32"
_AdslLineConfMaxRxPower_Object = MibTableColumn
adslLineConfMaxRxPower = _AdslLineConfMaxRxPower_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 2, 1, 1, 10),
    _AdslLineConfMaxRxPower_Type()
)
adslLineConfMaxRxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adslLineConfMaxRxPower.setStatus("current")
if mibBuilder.loadTexts:
    adslLineConfMaxRxPower.setUnits("tenth dBm")
_AdslLineConfAturCarrierMask_Type = OctetString
_AdslLineConfAturCarrierMask_Object = MibTableColumn
adslLineConfAturCarrierMask = _AdslLineConfAturCarrierMask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 2, 1, 1, 11),
    _AdslLineConfAturCarrierMask_Type()
)
adslLineConfAturCarrierMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adslLineConfAturCarrierMask.setStatus("current")
_AdslLineConfAtucCarrierMask0_Type = OctetString
_AdslLineConfAtucCarrierMask0_Object = MibTableColumn
adslLineConfAtucCarrierMask0 = _AdslLineConfAtucCarrierMask0_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 2, 1, 1, 12),
    _AdslLineConfAtucCarrierMask0_Type()
)
adslLineConfAtucCarrierMask0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adslLineConfAtucCarrierMask0.setStatus("current")
_AdslLineConfAtucCarrierMask1_Type = OctetString
_AdslLineConfAtucCarrierMask1_Object = MibTableColumn
adslLineConfAtucCarrierMask1 = _AdslLineConfAtucCarrierMask1_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 2, 1, 1, 13),
    _AdslLineConfAtucCarrierMask1_Type()
)
adslLineConfAtucCarrierMask1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adslLineConfAtucCarrierMask1.setStatus("current")


class _AdslLineConfAturInp_Type(Integer32):
    """Custom type adslLineConfAturInp based on Integer32"""
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
        *(("zero", 1),
          ("zero_point_five", 2),
          ("one", 3),
          ("two", 4),
          ("four", 5),
          ("eight", 6),
          ("sixteen", 7))
    )


_AdslLineConfAturInp_Type.__name__ = "Integer32"
_AdslLineConfAturInp_Object = MibTableColumn
adslLineConfAturInp = _AdslLineConfAturInp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 2, 1, 1, 14),
    _AdslLineConfAturInp_Type()
)
adslLineConfAturInp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adslLineConfAturInp.setStatus("current")


class _AdslLineConfAtucInp_Type(Integer32):
    """Custom type adslLineConfAtucInp based on Integer32"""
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
        *(("zero", 1),
          ("zero_point_five", 2),
          ("one", 3),
          ("two", 4),
          ("four", 5),
          ("eight", 6),
          ("sixteen", 7))
    )


_AdslLineConfAtucInp_Type.__name__ = "Integer32"
_AdslLineConfAtucInp_Object = MibTableColumn
adslLineConfAtucInp = _AdslLineConfAtucInp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 2, 1, 1, 15),
    _AdslLineConfAtucInp_Type()
)
adslLineConfAtucInp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adslLineConfAtucInp.setStatus("current")
_AdslLineConfL0Time_Type = Integer32
_AdslLineConfL0Time_Object = MibTableColumn
adslLineConfL0Time = _AdslLineConfL0Time_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 2, 1, 1, 16),
    _AdslLineConfL0Time_Type()
)
adslLineConfL0Time.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adslLineConfL0Time.setStatus("current")
_AdslLineConfL2Time_Type = Integer32
_AdslLineConfL2Time_Object = MibTableColumn
adslLineConfL2Time = _AdslLineConfL2Time_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 2, 1, 1, 17),
    _AdslLineConfL2Time_Type()
)
adslLineConfL2Time.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adslLineConfL2Time.setStatus("current")
_AdslLineConfL2ATPR_Type = Integer32
_AdslLineConfL2ATPR_Object = MibTableColumn
adslLineConfL2ATPR = _AdslLineConfL2ATPR_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 2, 1, 1, 18),
    _AdslLineConfL2ATPR_Type()
)
adslLineConfL2ATPR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adslLineConfL2ATPR.setStatus("current")
if mibBuilder.loadTexts:
    adslLineConfL2ATPR.setUnits("dB")
_AdslLineConfL2ATPRT_Type = Integer32
_AdslLineConfL2ATPRT_Object = MibTableColumn
adslLineConfL2ATPRT = _AdslLineConfL2ATPRT_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 2, 1, 1, 19),
    _AdslLineConfL2ATPRT_Type()
)
adslLineConfL2ATPRT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adslLineConfL2ATPRT.setStatus("current")
if mibBuilder.loadTexts:
    adslLineConfL2ATPRT.setUnits("dB")
_AdslLineConfMaxL2Rate_Type = Integer32
_AdslLineConfMaxL2Rate_Object = MibTableColumn
adslLineConfMaxL2Rate = _AdslLineConfMaxL2Rate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 2, 1, 1, 20),
    _AdslLineConfMaxL2Rate_Type()
)
adslLineConfMaxL2Rate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adslLineConfMaxL2Rate.setStatus("current")
if mibBuilder.loadTexts:
    adslLineConfMaxL2Rate.setUnits("kbps")
_AdslLineConfMinL2Rate_Type = Integer32
_AdslLineConfMinL2Rate_Object = MibTableColumn
adslLineConfMinL2Rate = _AdslLineConfMinL2Rate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 2, 1, 1, 21),
    _AdslLineConfMinL2Rate_Type()
)
adslLineConfMinL2Rate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adslLineConfMinL2Rate.setStatus("current")
if mibBuilder.loadTexts:
    adslLineConfMinL2Rate.setUnits("kbps")
_AdslLineConfL0toL2Rate_Type = Integer32
_AdslLineConfL0toL2Rate_Object = MibTableColumn
adslLineConfL0toL2Rate = _AdslLineConfL0toL2Rate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 2, 1, 1, 22),
    _AdslLineConfL0toL2Rate_Type()
)
adslLineConfL0toL2Rate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adslLineConfL0toL2Rate.setStatus("current")
if mibBuilder.loadTexts:
    adslLineConfL0toL2Rate.setUnits("kbps")
_AdslPortBatchSet_ObjectIdentity = ObjectIdentity
adslPortBatchSet = _AdslPortBatchSet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 2, 3)
)
_AdslPortTarget_Type = OctetString
_AdslPortTarget_Object = MibScalar
adslPortTarget = _AdslPortTarget_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 2, 3, 1),
    _AdslPortTarget_Type()
)
adslPortTarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adslPortTarget.setStatus("current")
_AdslPortOps_Type = Integer32
_AdslPortOps_Object = MibScalar
adslPortOps = _AdslPortOps_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 2, 3, 2),
    _AdslPortOps_Type()
)
adslPortOps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adslPortOps.setStatus("current")
_AdslPortOps2_Type = Integer32
_AdslPortOps2_Object = MibScalar
adslPortOps2 = _AdslPortOps2_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 2, 3, 3),
    _AdslPortOps2_Type()
)
adslPortOps2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adslPortOps2.setStatus("current")


class _AdslModeForBatchSet_Type(Integer32):
    """Custom type adslModeForBatchSet based on Integer32"""
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
        *(("gDotLite", 1),
          ("gDotDmt", 2),
          ("t1Dot413", 3),
          ("auto", 4),
          ("etsi", 5),
          ("adsl2", 6),
          ("adsl2Plus", 7))
    )


_AdslModeForBatchSet_Type.__name__ = "Integer32"
_AdslModeForBatchSet_Object = MibScalar
adslModeForBatchSet = _AdslModeForBatchSet_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 2, 3, 4),
    _AdslModeForBatchSet_Type()
)
adslModeForBatchSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adslModeForBatchSet.setStatus("current")


class _AdslLineProfileForBatchSet_Type(DisplayString):
    """Custom type adslLineProfileForBatchSet based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AdslLineProfileForBatchSet_Type.__name__ = "DisplayString"
_AdslLineProfileForBatchSet_Object = MibScalar
adslLineProfileForBatchSet = _AdslLineProfileForBatchSet_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 2, 3, 5),
    _AdslLineProfileForBatchSet_Type()
)
adslLineProfileForBatchSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adslLineProfileForBatchSet.setStatus("current")


class _AdslAlarmProfileForBatchSet_Type(DisplayString):
    """Custom type adslAlarmProfileForBatchSet based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AdslAlarmProfileForBatchSet_Type.__name__ = "DisplayString"
_AdslAlarmProfileForBatchSet_Object = MibScalar
adslAlarmProfileForBatchSet = _AdslAlarmProfileForBatchSet_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 2, 3, 6),
    _AdslAlarmProfileForBatchSet_Type()
)
adslAlarmProfileForBatchSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adslAlarmProfileForBatchSet.setStatus("current")
_AdslOptionMaskForBatchSet_Type = Integer32
_AdslOptionMaskForBatchSet_Object = MibScalar
adslOptionMaskForBatchSet = _AdslOptionMaskForBatchSet_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 2, 3, 7),
    _AdslOptionMaskForBatchSet_Type()
)
adslOptionMaskForBatchSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adslOptionMaskForBatchSet.setStatus("current")


class _AdslAturMaxTxPowerForBatchSet_Type(Integer32):
    """Custom type adslAturMaxTxPowerForBatchSet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-130, 200),
    )


_AdslAturMaxTxPowerForBatchSet_Type.__name__ = "Integer32"
_AdslAturMaxTxPowerForBatchSet_Object = MibScalar
adslAturMaxTxPowerForBatchSet = _AdslAturMaxTxPowerForBatchSet_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 2, 3, 8),
    _AdslAturMaxTxPowerForBatchSet_Type()
)
adslAturMaxTxPowerForBatchSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adslAturMaxTxPowerForBatchSet.setStatus("current")
if mibBuilder.loadTexts:
    adslAturMaxTxPowerForBatchSet.setUnits("tenth dBm")


class _AdslAtucMaxTxPowerForBatchSet_Type(Integer32):
    """Custom type adslAtucMaxTxPowerForBatchSet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 200),
    )


_AdslAtucMaxTxPowerForBatchSet_Type.__name__ = "Integer32"
_AdslAtucMaxTxPowerForBatchSet_Object = MibScalar
adslAtucMaxTxPowerForBatchSet = _AdslAtucMaxTxPowerForBatchSet_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 2, 3, 9),
    _AdslAtucMaxTxPowerForBatchSet_Type()
)
adslAtucMaxTxPowerForBatchSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adslAtucMaxTxPowerForBatchSet.setStatus("current")
if mibBuilder.loadTexts:
    adslAtucMaxTxPowerForBatchSet.setUnits("tenth dBm")


class _AdslMaxRxPowerForBatchSet_Type(Integer32):
    """Custom type adslMaxRxPowerForBatchSet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-255, 255),
    )


_AdslMaxRxPowerForBatchSet_Type.__name__ = "Integer32"
_AdslMaxRxPowerForBatchSet_Object = MibScalar
adslMaxRxPowerForBatchSet = _AdslMaxRxPowerForBatchSet_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 2, 3, 10),
    _AdslMaxRxPowerForBatchSet_Type()
)
adslMaxRxPowerForBatchSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adslMaxRxPowerForBatchSet.setStatus("current")
if mibBuilder.loadTexts:
    adslMaxRxPowerForBatchSet.setUnits("tenth dBm")
_AdslAturCarrierMaskForBatchSet_Type = OctetString
_AdslAturCarrierMaskForBatchSet_Object = MibScalar
adslAturCarrierMaskForBatchSet = _AdslAturCarrierMaskForBatchSet_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 2, 3, 11),
    _AdslAturCarrierMaskForBatchSet_Type()
)
adslAturCarrierMaskForBatchSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adslAturCarrierMaskForBatchSet.setStatus("current")
_AdslAtucCarrierMask0ForBatchSet_Type = OctetString
_AdslAtucCarrierMask0ForBatchSet_Object = MibScalar
adslAtucCarrierMask0ForBatchSet = _AdslAtucCarrierMask0ForBatchSet_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 2, 3, 12),
    _AdslAtucCarrierMask0ForBatchSet_Type()
)
adslAtucCarrierMask0ForBatchSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adslAtucCarrierMask0ForBatchSet.setStatus("current")
_AdslAtucCarrierMask1ForBatchSet_Type = OctetString
_AdslAtucCarrierMask1ForBatchSet_Object = MibScalar
adslAtucCarrierMask1ForBatchSet = _AdslAtucCarrierMask1ForBatchSet_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 2, 3, 13),
    _AdslAtucCarrierMask1ForBatchSet_Type()
)
adslAtucCarrierMask1ForBatchSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adslAtucCarrierMask1ForBatchSet.setStatus("current")


class _AdslAturInpForBatchSet_Type(Integer32):
    """Custom type adslAturInpForBatchSet based on Integer32"""
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
        *(("zero", 1),
          ("zero_point_five", 2),
          ("one", 3),
          ("two", 4),
          ("four", 5),
          ("eight", 6),
          ("sixteen", 7))
    )


_AdslAturInpForBatchSet_Type.__name__ = "Integer32"
_AdslAturInpForBatchSet_Object = MibScalar
adslAturInpForBatchSet = _AdslAturInpForBatchSet_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 2, 3, 14),
    _AdslAturInpForBatchSet_Type()
)
adslAturInpForBatchSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adslAturInpForBatchSet.setStatus("current")


class _AdslAtucInpForBatchSet_Type(Integer32):
    """Custom type adslAtucInpForBatchSet based on Integer32"""
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
        *(("zero", 1),
          ("zero_point_five", 2),
          ("one", 3),
          ("two", 4),
          ("four", 5),
          ("eight", 6),
          ("sixteen", 7))
    )


_AdslAtucInpForBatchSet_Type.__name__ = "Integer32"
_AdslAtucInpForBatchSet_Object = MibScalar
adslAtucInpForBatchSet = _AdslAtucInpForBatchSet_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 2, 3, 15),
    _AdslAtucInpForBatchSet_Type()
)
adslAtucInpForBatchSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adslAtucInpForBatchSet.setStatus("current")
_AdslL0TimeForBatchSet_Type = Integer32
_AdslL0TimeForBatchSet_Object = MibScalar
adslL0TimeForBatchSet = _AdslL0TimeForBatchSet_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 2, 3, 16),
    _AdslL0TimeForBatchSet_Type()
)
adslL0TimeForBatchSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adslL0TimeForBatchSet.setStatus("current")
_AdslL2TimeForBatchSet_Type = Integer32
_AdslL2TimeForBatchSet_Object = MibScalar
adslL2TimeForBatchSet = _AdslL2TimeForBatchSet_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 2, 3, 17),
    _AdslL2TimeForBatchSet_Type()
)
adslL2TimeForBatchSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adslL2TimeForBatchSet.setStatus("current")
_AdslL2ATPRForBatchSet_Type = Integer32
_AdslL2ATPRForBatchSet_Object = MibScalar
adslL2ATPRForBatchSet = _AdslL2ATPRForBatchSet_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 2, 3, 18),
    _AdslL2ATPRForBatchSet_Type()
)
adslL2ATPRForBatchSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adslL2ATPRForBatchSet.setStatus("current")
if mibBuilder.loadTexts:
    adslL2ATPRForBatchSet.setUnits("dB")
_AdslL2ATPRTForBatchSet_Type = Integer32
_AdslL2ATPRTForBatchSet_Object = MibScalar
adslL2ATPRTForBatchSet = _AdslL2ATPRTForBatchSet_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 2, 3, 19),
    _AdslL2ATPRTForBatchSet_Type()
)
adslL2ATPRTForBatchSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adslL2ATPRTForBatchSet.setStatus("current")
if mibBuilder.loadTexts:
    adslL2ATPRTForBatchSet.setUnits("dB")
_AdslMaxL2RateForBatchSet_Type = Integer32
_AdslMaxL2RateForBatchSet_Object = MibScalar
adslMaxL2RateForBatchSet = _AdslMaxL2RateForBatchSet_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 2, 3, 20),
    _AdslMaxL2RateForBatchSet_Type()
)
adslMaxL2RateForBatchSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adslMaxL2RateForBatchSet.setStatus("current")
if mibBuilder.loadTexts:
    adslMaxL2RateForBatchSet.setUnits("kbps")
_AdslMinL2RateForBatchSet_Type = Integer32
_AdslMinL2RateForBatchSet_Object = MibScalar
adslMinL2RateForBatchSet = _AdslMinL2RateForBatchSet_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 2, 3, 21),
    _AdslMinL2RateForBatchSet_Type()
)
adslMinL2RateForBatchSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adslMinL2RateForBatchSet.setStatus("current")
if mibBuilder.loadTexts:
    adslMinL2RateForBatchSet.setUnits("kbps")
_AdslL0toL2RateForBatchSet_Type = Integer32
_AdslL0toL2RateForBatchSet_Object = MibScalar
adslL0toL2RateForBatchSet = _AdslL0toL2RateForBatchSet_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 2, 3, 22),
    _AdslL0toL2RateForBatchSet_Type()
)
adslL0toL2RateForBatchSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adslL0toL2RateForBatchSet.setStatus("current")
if mibBuilder.loadTexts:
    adslL0toL2RateForBatchSet.setUnits("kbps")
_AdslLineStatusTable_Object = MibTable
adslLineStatusTable = _AdslLineStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 2, 4)
)
if mibBuilder.loadTexts:
    adslLineStatusTable.setStatus("current")
_AdslLineStatusEntry_Object = MibTableRow
adslLineStatusEntry = _AdslLineStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 2, 4, 1)
)
adslLineStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adslLineStatusEntry.setStatus("current")


class _AdslLineStatusMode_Type(Integer32):
    """Custom type adslLineStatusMode based on Integer32"""
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
        *(("gDotLite", 1),
          ("gDotDmt", 2),
          ("t1Dot413", 3),
          ("etsi", 4),
          ("adsl2", 5),
          ("adsl2Plus", 6),
          ("none", 7))
    )


_AdslLineStatusMode_Type.__name__ = "Integer32"
_AdslLineStatusMode_Object = MibTableColumn
adslLineStatusMode = _AdslLineStatusMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 2, 4, 1, 1),
    _AdslLineStatusMode_Type()
)
adslLineStatusMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslLineStatusMode.setStatus("current")
_AdslLineUpTime_Type = Integer32
_AdslLineUpTime_Object = MibTableColumn
adslLineUpTime = _AdslLineUpTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 2, 4, 1, 2),
    _AdslLineUpTime_Type()
)
adslLineUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslLineUpTime.setStatus("current")
_PowerMgmtParamTable_Object = MibTable
powerMgmtParamTable = _PowerMgmtParamTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 2, 5)
)
if mibBuilder.loadTexts:
    powerMgmtParamTable.setStatus("current")
_PowerMgmtParamEntry_Object = MibTableRow
powerMgmtParamEntry = _PowerMgmtParamEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 2, 5, 1)
)
powerMgmtParamEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    powerMgmtParamEntry.setStatus("current")
_PowerMgmtL0Time_Type = Integer32
_PowerMgmtL0Time_Object = MibTableColumn
powerMgmtL0Time = _PowerMgmtL0Time_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 2, 5, 1, 1),
    _PowerMgmtL0Time_Type()
)
powerMgmtL0Time.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    powerMgmtL0Time.setStatus("current")
if mibBuilder.loadTexts:
    powerMgmtL0Time.setUnits("second")
_PowerMgmtL2Time_Type = Integer32
_PowerMgmtL2Time_Object = MibTableColumn
powerMgmtL2Time = _PowerMgmtL2Time_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 2, 5, 1, 2),
    _PowerMgmtL2Time_Type()
)
powerMgmtL2Time.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    powerMgmtL2Time.setStatus("current")
if mibBuilder.loadTexts:
    powerMgmtL2Time.setUnits("second")
_PowerMgmtL2Atpr_Type = Integer32
_PowerMgmtL2Atpr_Object = MibTableColumn
powerMgmtL2Atpr = _PowerMgmtL2Atpr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 2, 5, 1, 3),
    _PowerMgmtL2Atpr_Type()
)
powerMgmtL2Atpr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    powerMgmtL2Atpr.setStatus("current")
if mibBuilder.loadTexts:
    powerMgmtL2Atpr.setUnits("dB")
_PowerMgmtL2Atprt_Type = Integer32
_PowerMgmtL2Atprt_Object = MibTableColumn
powerMgmtL2Atprt = _PowerMgmtL2Atprt_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 2, 5, 1, 4),
    _PowerMgmtL2Atprt_Type()
)
powerMgmtL2Atprt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    powerMgmtL2Atprt.setStatus("current")
if mibBuilder.loadTexts:
    powerMgmtL2Atprt.setUnits("dB")
_PowerMgmtL2MinRate_Type = Integer32
_PowerMgmtL2MinRate_Object = MibTableColumn
powerMgmtL2MinRate = _PowerMgmtL2MinRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 2, 5, 1, 5),
    _PowerMgmtL2MinRate_Type()
)
powerMgmtL2MinRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    powerMgmtL2MinRate.setStatus("current")
if mibBuilder.loadTexts:
    powerMgmtL2MinRate.setUnits("Kbps")
_PowerMgmtL2MaxRate_Type = Integer32
_PowerMgmtL2MaxRate_Object = MibTableColumn
powerMgmtL2MaxRate = _PowerMgmtL2MaxRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 2, 5, 1, 6),
    _PowerMgmtL2MaxRate_Type()
)
powerMgmtL2MaxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    powerMgmtL2MaxRate.setStatus("current")
if mibBuilder.loadTexts:
    powerMgmtL2MaxRate.setUnits("Kbps")
_PowerMgmtL2ThreshRate_Type = Integer32
_PowerMgmtL2ThreshRate_Object = MibTableColumn
powerMgmtL2ThreshRate = _PowerMgmtL2ThreshRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 2, 5, 1, 7),
    _PowerMgmtL2ThreshRate_Type()
)
powerMgmtL2ThreshRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    powerMgmtL2ThreshRate.setStatus("current")
if mibBuilder.loadTexts:
    powerMgmtL2ThreshRate.setUnits("Kbps")
_PowerMgmtPSDTable_Object = MibTable
powerMgmtPSDTable = _PowerMgmtPSDTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 2, 6)
)
if mibBuilder.loadTexts:
    powerMgmtPSDTable.setStatus("current")
_PowerMgmtPSDEntry_Object = MibTableRow
powerMgmtPSDEntry = _PowerMgmtPSDEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 2, 6, 1)
)
powerMgmtPSDEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    powerMgmtPSDEntry.setStatus("current")
_PowerMgmtAtucMaxPSD_Type = Integer32
_PowerMgmtAtucMaxPSD_Object = MibTableColumn
powerMgmtAtucMaxPSD = _PowerMgmtAtucMaxPSD_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 2, 6, 1, 1),
    _PowerMgmtAtucMaxPSD_Type()
)
powerMgmtAtucMaxPSD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    powerMgmtAtucMaxPSD.setStatus("current")
if mibBuilder.loadTexts:
    powerMgmtAtucMaxPSD.setUnits("0.1dBm/Hz")
_PowerMgmtAturMaxPSD_Type = Integer32
_PowerMgmtAturMaxPSD_Object = MibTableColumn
powerMgmtAturMaxPSD = _PowerMgmtAturMaxPSD_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 2, 6, 1, 2),
    _PowerMgmtAturMaxPSD_Type()
)
powerMgmtAturMaxPSD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    powerMgmtAturMaxPSD.setStatus("current")
if mibBuilder.loadTexts:
    powerMgmtAturMaxPSD.setUnits("0.1dBm/Hz")
_Pvc_ObjectIdentity = ObjectIdentity
pvc = _Pvc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 4)
)
_MaxNumOfPvcs_Type = Integer32
_MaxNumOfPvcs_Object = MibScalar
maxNumOfPvcs = _MaxNumOfPvcs_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 4, 1),
    _MaxNumOfPvcs_Type()
)
maxNumOfPvcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumOfPvcs.setStatus("current")
_PvcTable_Object = MibTable
pvcTable = _PvcTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 4, 2)
)
if mibBuilder.loadTexts:
    pvcTable.setStatus("current")
_PvcEntry_Object = MibTableRow
pvcEntry = _PvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 4, 2, 1)
)
pvcEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZYXEL-IES1248", "pvcVpi"),
    (0, "ZYXEL-IES1248", "pvcVci"),
    (0, "ZYXEL-IES1248", "pvcPvid"),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 4, 2, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 4, 2, 1, 2),
    _PvcVci_Type()
)
pvcVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcVci.setStatus("current")
_PvcPvid_Type = VlanIndex
_PvcPvid_Object = MibTableColumn
pvcPvid = _PvcPvid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 4, 2, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 4, 2, 1, 5),
    _PvcPriority_Type()
)
pvcPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvcPriority.setStatus("current")


class _PvcProfileDS_Type(DisplayString):
    """Custom type pvcProfileDS based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_PvcProfileDS_Type.__name__ = "DisplayString"
_PvcProfileDS_Object = MibTableColumn
pvcProfileDS = _PvcProfileDS_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 4, 2, 1, 6),
    _PvcProfileDS_Type()
)
pvcProfileDS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvcProfileDS.setStatus("current")
_PvcRowStatus_Type = RowStatus
_PvcRowStatus_Object = MibTableColumn
pvcRowStatus = _PvcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 4, 2, 1, 7),
    _PvcRowStatus_Type()
)
pvcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvcRowStatus.setStatus("current")


class _PvcProfileUS_Type(DisplayString):
    """Custom type pvcProfileUS based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_PvcProfileUS_Type.__name__ = "DisplayString"
_PvcProfileUS_Object = MibTableColumn
pvcProfileUS = _PvcProfileUS_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 4, 2, 1, 8),
    _PvcProfileUS_Type()
)
pvcProfileUS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvcProfileUS.setStatus("current")


class _Pvcmaccnt_Type(Integer32):
    """Custom type pvcmaccnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pvcmaccnt_Type.__name__ = "Integer32"
_Pvcmaccnt_Object = MibTableColumn
pvcmaccnt = _Pvcmaccnt_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 4, 2, 1, 9),
    _Pvcmaccnt_Type()
)
pvcmaccnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcmaccnt.setStatus("current")
_PvcUsRateLimitTable_Object = MibTable
pvcUsRateLimitTable = _PvcUsRateLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 4, 4)
)
if mibBuilder.loadTexts:
    pvcUsRateLimitTable.setStatus("current")
_PvcUsRateLimitEntry_Object = MibTableRow
pvcUsRateLimitEntry = _PvcUsRateLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 4, 4, 1)
)
pvcUsRateLimitEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZYXEL-IES1248", "pvcVpi"),
    (0, "ZYXEL-IES1248", "pvcVci"),
)
if mibBuilder.loadTexts:
    pvcUsRateLimitEntry.setStatus("current")


class _PvcUsRateLimitEnable_Type(Integer32):
    """Custom type pvcUsRateLimitEnable based on Integer32"""
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


_PvcUsRateLimitEnable_Type.__name__ = "Integer32"
_PvcUsRateLimitEnable_Object = MibTableColumn
pvcUsRateLimitEnable = _PvcUsRateLimitEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 4, 4, 1, 1),
    _PvcUsRateLimitEnable_Type()
)
pvcUsRateLimitEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcUsRateLimitEnable.setStatus("current")
_PvcUsRateLimit_Type = Integer32
_PvcUsRateLimit_Object = MibTableColumn
pvcUsRateLimit = _PvcUsRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 4, 4, 1, 2),
    _PvcUsRateLimit_Type()
)
pvcUsRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcUsRateLimit.setStatus("current")
if mibBuilder.loadTexts:
    pvcUsRateLimit.setUnits("Kbps")
_Ppvc_ObjectIdentity = ObjectIdentity
ppvc = _Ppvc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 5)
)
_MaxNumOfPriorityPvcs_Type = Integer32
_MaxNumOfPriorityPvcs_Object = MibScalar
maxNumOfPriorityPvcs = _MaxNumOfPriorityPvcs_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 5, 1),
    _MaxNumOfPriorityPvcs_Type()
)
maxNumOfPriorityPvcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumOfPriorityPvcs.setStatus("current")
_PpvcTable_Object = MibTable
ppvcTable = _PpvcTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 5, 2)
)
if mibBuilder.loadTexts:
    ppvcTable.setStatus("current")
_PpvcEntry_Object = MibTableRow
ppvcEntry = _PpvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 5, 2, 1)
)
ppvcEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZYXEL-IES1248", "ppvcVpi"),
    (0, "ZYXEL-IES1248", "ppvcVci"),
    (0, "ZYXEL-IES1248", "ppvcPvid"),
)
if mibBuilder.loadTexts:
    ppvcEntry.setStatus("current")


class _PpvcVpi_Type(Integer32):
    """Custom type ppvcVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PpvcVpi_Type.__name__ = "Integer32"
_PpvcVpi_Object = MibTableColumn
ppvcVpi = _PpvcVpi_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 5, 2, 1, 1),
    _PpvcVpi_Type()
)
ppvcVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppvcVpi.setStatus("current")


class _PpvcVci_Type(Integer32):
    """Custom type ppvcVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PpvcVci_Type.__name__ = "Integer32"
_PpvcVci_Object = MibTableColumn
ppvcVci = _PpvcVci_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 5, 2, 1, 2),
    _PpvcVci_Type()
)
ppvcVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppvcVci.setStatus("current")
_PpvcPvid_Type = VlanIndex
_PpvcPvid_Object = MibTableColumn
ppvcPvid = _PpvcPvid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 5, 2, 1, 3),
    _PpvcPvid_Type()
)
ppvcPvid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppvcPvid.setStatus("current")


class _PpvcEncap_Type(Integer32):
    """Custom type ppvcEncap based on Integer32"""
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


_PpvcEncap_Type.__name__ = "Integer32"
_PpvcEncap_Object = MibTableColumn
ppvcEncap = _PpvcEncap_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 5, 2, 1, 4),
    _PpvcEncap_Type()
)
ppvcEncap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ppvcEncap.setStatus("current")


class _PpvcPriority_Type(Integer32):
    """Custom type ppvcPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PpvcPriority_Type.__name__ = "Integer32"
_PpvcPriority_Object = MibTableColumn
ppvcPriority = _PpvcPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 5, 2, 1, 5),
    _PpvcPriority_Type()
)
ppvcPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ppvcPriority.setStatus("current")
_PpvcRowStatus_Type = RowStatus
_PpvcRowStatus_Object = MibTableColumn
ppvcRowStatus = _PpvcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 5, 2, 1, 6),
    _PpvcRowStatus_Type()
)
ppvcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ppvcRowStatus.setStatus("current")
_PpvcMemberTable_Object = MibTable
ppvcMemberTable = _PpvcMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 5, 4)
)
if mibBuilder.loadTexts:
    ppvcMemberTable.setStatus("current")
_PpvcMemberEntry_Object = MibTableRow
ppvcMemberEntry = _PpvcMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 5, 4, 1)
)
ppvcMemberEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZYXEL-IES1248", "ppvcVpi"),
    (0, "ZYXEL-IES1248", "ppvcVci"),
    (0, "ZYXEL-IES1248", "ppvcMemberVpi"),
    (0, "ZYXEL-IES1248", "ppvcMemberVci"),
    (0, "ZYXEL-IES1248", "ppvcMemberPriority"),
)
if mibBuilder.loadTexts:
    ppvcMemberEntry.setStatus("current")


class _PpvcMemberVpi_Type(Integer32):
    """Custom type ppvcMemberVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PpvcMemberVpi_Type.__name__ = "Integer32"
_PpvcMemberVpi_Object = MibTableColumn
ppvcMemberVpi = _PpvcMemberVpi_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 5, 4, 1, 1),
    _PpvcMemberVpi_Type()
)
ppvcMemberVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppvcMemberVpi.setStatus("current")


class _PpvcMemberVci_Type(Integer32):
    """Custom type ppvcMemberVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PpvcMemberVci_Type.__name__ = "Integer32"
_PpvcMemberVci_Object = MibTableColumn
ppvcMemberVci = _PpvcMemberVci_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 5, 4, 1, 2),
    _PpvcMemberVci_Type()
)
ppvcMemberVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppvcMemberVci.setStatus("current")


class _PpvcMemberPriority_Type(Integer32):
    """Custom type ppvcMemberPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PpvcMemberPriority_Type.__name__ = "Integer32"
_PpvcMemberPriority_Object = MibTableColumn
ppvcMemberPriority = _PpvcMemberPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 5, 4, 1, 3),
    _PpvcMemberPriority_Type()
)
ppvcMemberPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppvcMemberPriority.setStatus("current")


class _PpvcMemberProfileDS_Type(DisplayString):
    """Custom type ppvcMemberProfileDS based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_PpvcMemberProfileDS_Type.__name__ = "DisplayString"
_PpvcMemberProfileDS_Object = MibTableColumn
ppvcMemberProfileDS = _PpvcMemberProfileDS_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 5, 4, 1, 4),
    _PpvcMemberProfileDS_Type()
)
ppvcMemberProfileDS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ppvcMemberProfileDS.setStatus("current")
_PpvcMemberRowStatus_Type = RowStatus
_PpvcMemberRowStatus_Object = MibTableColumn
ppvcMemberRowStatus = _PpvcMemberRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 5, 4, 1, 5),
    _PpvcMemberRowStatus_Type()
)
ppvcMemberRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ppvcMemberRowStatus.setStatus("current")


class _PpvcMemberProfileUS_Type(DisplayString):
    """Custom type ppvcMemberProfileUS based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_PpvcMemberProfileUS_Type.__name__ = "DisplayString"
_PpvcMemberProfileUS_Object = MibTableColumn
ppvcMemberProfileUS = _PpvcMemberProfileUS_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 5, 4, 1, 6),
    _PpvcMemberProfileUS_Type()
)
ppvcMemberProfileUS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ppvcMemberProfileUS.setStatus("current")
_Rpvc_ObjectIdentity = ObjectIdentity
rpvc = _Rpvc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 8)
)
_RpvcGatewayTable_Object = MibTable
rpvcGatewayTable = _RpvcGatewayTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 8, 1)
)
if mibBuilder.loadTexts:
    rpvcGatewayTable.setStatus("current")
_RpvcGatewayEntry_Object = MibTableRow
rpvcGatewayEntry = _RpvcGatewayEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 8, 1, 1)
)
rpvcGatewayEntry.setIndexNames(
    (0, "ZYXEL-IES1248", "rpvcGatewayIp"),
)
if mibBuilder.loadTexts:
    rpvcGatewayEntry.setStatus("current")
_RpvcGatewayIp_Type = IpAddress
_RpvcGatewayIp_Object = MibTableColumn
rpvcGatewayIp = _RpvcGatewayIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 8, 1, 1, 1),
    _RpvcGatewayIp_Type()
)
rpvcGatewayIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpvcGatewayIp.setStatus("current")
_RpvcGatewayVlanId_Type = VlanIndex
_RpvcGatewayVlanId_Object = MibTableColumn
rpvcGatewayVlanId = _RpvcGatewayVlanId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 8, 1, 1, 2),
    _RpvcGatewayVlanId_Type()
)
rpvcGatewayVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rpvcGatewayVlanId.setStatus("current")
_RpvcGatewayRowStatus_Type = RowStatus
_RpvcGatewayRowStatus_Object = MibTableColumn
rpvcGatewayRowStatus = _RpvcGatewayRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 8, 1, 1, 3),
    _RpvcGatewayRowStatus_Type()
)
rpvcGatewayRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rpvcGatewayRowStatus.setStatus("current")
_RpvcGatewayPriority_Type = Integer32
_RpvcGatewayPriority_Object = MibTableColumn
rpvcGatewayPriority = _RpvcGatewayPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 8, 1, 1, 4),
    _RpvcGatewayPriority_Type()
)
rpvcGatewayPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rpvcGatewayPriority.setStatus("current")
_RpvcTable_Object = MibTable
rpvcTable = _RpvcTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 8, 2)
)
if mibBuilder.loadTexts:
    rpvcTable.setStatus("current")
_RpvcEntry_Object = MibTableRow
rpvcEntry = _RpvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 8, 2, 1)
)
rpvcEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZYXEL-IES1248", "rpvcVpi"),
    (0, "ZYXEL-IES1248", "rpvcVci"),
    (0, "ZYXEL-IES1248", "rpvcIp"),
    (0, "ZYXEL-IES1248", "rpvcNetmask"),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 8, 2, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 8, 2, 1, 2),
    _RpvcVci_Type()
)
rpvcVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpvcVci.setStatus("current")


class _RpvcDSProfile_Type(DisplayString):
    """Custom type rpvcDSProfile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_RpvcDSProfile_Type.__name__ = "DisplayString"
_RpvcDSProfile_Object = MibTableColumn
rpvcDSProfile = _RpvcDSProfile_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 8, 2, 1, 3),
    _RpvcDSProfile_Type()
)
rpvcDSProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rpvcDSProfile.setStatus("current")


class _RpvcUSProfile_Type(DisplayString):
    """Custom type rpvcUSProfile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_RpvcUSProfile_Type.__name__ = "DisplayString"
_RpvcUSProfile_Object = MibTableColumn
rpvcUSProfile = _RpvcUSProfile_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 8, 2, 1, 4),
    _RpvcUSProfile_Type()
)
rpvcUSProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rpvcUSProfile.setStatus("current")
_RpvcIp_Type = IpAddress
_RpvcIp_Object = MibTableColumn
rpvcIp = _RpvcIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 8, 2, 1, 5),
    _RpvcIp_Type()
)
rpvcIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpvcIp.setStatus("current")
_RpvcNetmask_Type = IpAddress
_RpvcNetmask_Object = MibTableColumn
rpvcNetmask = _RpvcNetmask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 8, 2, 1, 6),
    _RpvcNetmask_Type()
)
rpvcNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpvcNetmask.setStatus("current")
_RpvcGatewayIpAddress_Type = IpAddress
_RpvcGatewayIpAddress_Object = MibTableColumn
rpvcGatewayIpAddress = _RpvcGatewayIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 8, 2, 1, 7),
    _RpvcGatewayIpAddress_Type()
)
rpvcGatewayIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rpvcGatewayIpAddress.setStatus("current")
_RpvcRowStatus_Type = RowStatus
_RpvcRowStatus_Object = MibTableColumn
rpvcRowStatus = _RpvcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 8, 2, 1, 8),
    _RpvcRowStatus_Type()
)
rpvcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rpvcRowStatus.setStatus("current")
_RpvcRouteDomainTable_Object = MibTable
rpvcRouteDomainTable = _RpvcRouteDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 8, 3)
)
if mibBuilder.loadTexts:
    rpvcRouteDomainTable.setStatus("current")
_RpvcRouteDomainEntry_Object = MibTableRow
rpvcRouteDomainEntry = _RpvcRouteDomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 8, 3, 1)
)
rpvcRouteDomainEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZYXEL-IES1248", "rpvcRouteDomainVpi"),
    (0, "ZYXEL-IES1248", "rpvcRouteDomainVci"),
    (0, "ZYXEL-IES1248", "rpvcRouteDomainIp"),
    (0, "ZYXEL-IES1248", "rpvcRouteDomainNetmask"),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 8, 3, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 8, 3, 1, 2),
    _RpvcRouteDomainVci_Type()
)
rpvcRouteDomainVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpvcRouteDomainVci.setStatus("current")
_RpvcRouteDomainIp_Type = IpAddress
_RpvcRouteDomainIp_Object = MibTableColumn
rpvcRouteDomainIp = _RpvcRouteDomainIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 8, 3, 1, 3),
    _RpvcRouteDomainIp_Type()
)
rpvcRouteDomainIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpvcRouteDomainIp.setStatus("current")
_RpvcRouteDomainNetmask_Type = IpAddress
_RpvcRouteDomainNetmask_Object = MibTableColumn
rpvcRouteDomainNetmask = _RpvcRouteDomainNetmask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 8, 3, 1, 4),
    _RpvcRouteDomainNetmask_Type()
)
rpvcRouteDomainNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpvcRouteDomainNetmask.setStatus("current")
_RpvcRouteDomainRowStatus_Type = RowStatus
_RpvcRouteDomainRowStatus_Object = MibTableColumn
rpvcRouteDomainRowStatus = _RpvcRouteDomainRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 8, 3, 1, 5),
    _RpvcRouteDomainRowStatus_Type()
)
rpvcRouteDomainRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rpvcRouteDomainRowStatus.setStatus("current")
_RpvcArpAgingTime_Type = Integer32
_RpvcArpAgingTime_Object = MibScalar
rpvcArpAgingTime = _RpvcArpAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 8, 4),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 8, 5),
    _RpvcArpFlush_Type()
)
rpvcArpFlush.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rpvcArpFlush.setStatus("current")
_DsBcastDisableTable_Object = MibTable
dsBcastDisableTable = _DsBcastDisableTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 9)
)
if mibBuilder.loadTexts:
    dsBcastDisableTable.setStatus("current")
_DsBcastDisableEntry_Object = MibTableRow
dsBcastDisableEntry = _DsBcastDisableEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 9, 1)
)
dsBcastDisableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZYXEL-IES1248", "dsBcastDisableVlanId"),
)
if mibBuilder.loadTexts:
    dsBcastDisableEntry.setStatus("current")
_DsBcastDisableVlanId_Type = Integer32
_DsBcastDisableVlanId_Object = MibTableColumn
dsBcastDisableVlanId = _DsBcastDisableVlanId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 9, 1, 1),
    _DsBcastDisableVlanId_Type()
)
dsBcastDisableVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsBcastDisableVlanId.setStatus("current")
_DsBcastDisableRowStatus_Type = RowStatus
_DsBcastDisableRowStatus_Object = MibTableColumn
dsBcastDisableRowStatus = _DsBcastDisableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 9, 1, 2),
    _DsBcastDisableRowStatus_Type()
)
dsBcastDisableRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsBcastDisableRowStatus.setStatus("current")
_Paepvc_ObjectIdentity = ObjectIdentity
paepvc = _Paepvc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 10)
)
_PaepvcTable_Object = MibTable
paepvcTable = _PaepvcTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 10, 1)
)
if mibBuilder.loadTexts:
    paepvcTable.setStatus("current")
_PaepvcEntry_Object = MibTableRow
paepvcEntry = _PaepvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 10, 1, 1)
)
paepvcEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZYXEL-IES1248", "paepvcVpi"),
    (0, "ZYXEL-IES1248", "paepvcVci"),
    (0, "ZYXEL-IES1248", "paepvcPvid"),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 10, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 10, 1, 1, 2),
    _PaepvcVci_Type()
)
paepvcVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcVci.setStatus("current")
_PaepvcPvid_Type = VlanIndex
_PaepvcPvid_Object = MibTableColumn
paepvcPvid = _PaepvcPvid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 10, 1, 1, 3),
    _PaepvcPvid_Type()
)
paepvcPvid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcPvid.setStatus("current")


class _PaepvcPriority_Type(Integer32):
    """Custom type paepvcPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PaepvcPriority_Type.__name__ = "Integer32"
_PaepvcPriority_Object = MibTableColumn
paepvcPriority = _PaepvcPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 10, 1, 1, 5),
    _PaepvcPriority_Type()
)
paepvcPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    paepvcPriority.setStatus("current")


class _PaepvcProfileDS_Type(DisplayString):
    """Custom type paepvcProfileDS based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_PaepvcProfileDS_Type.__name__ = "DisplayString"
_PaepvcProfileDS_Object = MibTableColumn
paepvcProfileDS = _PaepvcProfileDS_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 10, 1, 1, 6),
    _PaepvcProfileDS_Type()
)
paepvcProfileDS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    paepvcProfileDS.setStatus("current")
_PaepvcAcName_Type = DisplayString
_PaepvcAcName_Object = MibTableColumn
paepvcAcName = _PaepvcAcName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 10, 1, 1, 7),
    _PaepvcAcName_Type()
)
paepvcAcName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    paepvcAcName.setStatus("current")
_PaepvcServiceName_Type = DisplayString
_PaepvcServiceName_Object = MibTableColumn
paepvcServiceName = _PaepvcServiceName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 10, 1, 1, 8),
    _PaepvcServiceName_Type()
)
paepvcServiceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    paepvcServiceName.setStatus("current")
_PaepvcHelloTime_Type = Integer32
_PaepvcHelloTime_Object = MibTableColumn
paepvcHelloTime = _PaepvcHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 10, 1, 1, 9),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 10, 1, 1, 10),
    _PaepvcRowStatus_Type()
)
paepvcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    paepvcRowStatus.setStatus("current")


class _PaepvcProfileUS_Type(DisplayString):
    """Custom type paepvcProfileUS based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_PaepvcProfileUS_Type.__name__ = "DisplayString"
_PaepvcProfileUS_Object = MibTableColumn
paepvcProfileUS = _PaepvcProfileUS_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 10, 1, 1, 11),
    _PaepvcProfileUS_Type()
)
paepvcProfileUS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    paepvcProfileUS.setStatus("current")
_Tlspvc_ObjectIdentity = ObjectIdentity
tlspvc = _Tlspvc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 11)
)
_TlspvcTable_Object = MibTable
tlspvcTable = _TlspvcTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 11, 1)
)
if mibBuilder.loadTexts:
    tlspvcTable.setStatus("current")
_TlspvcEntry_Object = MibTableRow
tlspvcEntry = _TlspvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 11, 1, 1)
)
tlspvcEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZYXEL-IES1248", "tlspvcVpi"),
    (0, "ZYXEL-IES1248", "tlspvcVci"),
    (0, "ZYXEL-IES1248", "tlspvcSvid"),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 11, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 11, 1, 1, 2),
    _TlspvcVci_Type()
)
tlspvcVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlspvcVci.setStatus("current")
_TlspvcSvid_Type = VlanIndex
_TlspvcSvid_Object = MibTableColumn
tlspvcSvid = _TlspvcSvid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 11, 1, 1, 3),
    _TlspvcSvid_Type()
)
tlspvcSvid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlspvcSvid.setStatus("current")


class _TlspvcSpriority_Type(Integer32):
    """Custom type tlspvcSpriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TlspvcSpriority_Type.__name__ = "Integer32"
_TlspvcSpriority_Object = MibTableColumn
tlspvcSpriority = _TlspvcSpriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 11, 1, 1, 5),
    _TlspvcSpriority_Type()
)
tlspvcSpriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tlspvcSpriority.setStatus("current")


class _TlspvcProfileDS_Type(DisplayString):
    """Custom type tlspvcProfileDS based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_TlspvcProfileDS_Type.__name__ = "DisplayString"
_TlspvcProfileDS_Object = MibTableColumn
tlspvcProfileDS = _TlspvcProfileDS_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 11, 1, 1, 6),
    _TlspvcProfileDS_Type()
)
tlspvcProfileDS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tlspvcProfileDS.setStatus("current")
_TlspvcRowStatus_Type = RowStatus
_TlspvcRowStatus_Object = MibTableColumn
tlspvcRowStatus = _TlspvcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 11, 1, 1, 7),
    _TlspvcRowStatus_Type()
)
tlspvcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tlspvcRowStatus.setStatus("current")


class _TlspvcProfileUS_Type(DisplayString):
    """Custom type tlspvcProfileUS based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_TlspvcProfileUS_Type.__name__ = "DisplayString"
_TlspvcProfileUS_Object = MibTableColumn
tlspvcProfileUS = _TlspvcProfileUS_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 11, 1, 1, 8),
    _TlspvcProfileUS_Type()
)
tlspvcProfileUS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tlspvcProfileUS.setStatus("current")
_Ipbpvc_ObjectIdentity = ObjectIdentity
ipbpvc = _Ipbpvc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 12)
)
_IpbpvcDomainTable_Object = MibTable
ipbpvcDomainTable = _IpbpvcDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 12, 1)
)
if mibBuilder.loadTexts:
    ipbpvcDomainTable.setStatus("current")
_IpbpvcDomainEntry_Object = MibTableRow
ipbpvcDomainEntry = _IpbpvcDomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 12, 1, 1)
)
ipbpvcDomainEntry.setIndexNames(
    (0, "ZYXEL-IES1248", "ipbpvcDomainName"),
)
if mibBuilder.loadTexts:
    ipbpvcDomainEntry.setStatus("current")
_IpbpvcDomainName_Type = OctetString
_IpbpvcDomainName_Object = MibTableColumn
ipbpvcDomainName = _IpbpvcDomainName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 12, 1, 1, 1),
    _IpbpvcDomainName_Type()
)
ipbpvcDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipbpvcDomainName.setStatus("current")
_IpbpvcDomainRowStatus_Type = RowStatus
_IpbpvcDomainRowStatus_Object = MibTableColumn
ipbpvcDomainRowStatus = _IpbpvcDomainRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 12, 1, 1, 2),
    _IpbpvcDomainRowStatus_Type()
)
ipbpvcDomainRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipbpvcDomainRowStatus.setStatus("current")
_IpbpvcDomainVlanTable_Object = MibTable
ipbpvcDomainVlanTable = _IpbpvcDomainVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 12, 2)
)
if mibBuilder.loadTexts:
    ipbpvcDomainVlanTable.setStatus("current")
_IpbpvcDomainVlanEntry_Object = MibTableRow
ipbpvcDomainVlanEntry = _IpbpvcDomainVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 12, 2, 1)
)
ipbpvcDomainVlanEntry.setIndexNames(
    (0, "ZYXEL-IES1248", "ipbpvcDomainName"),
    (0, "ZYXEL-IES1248", "ipbpvcDomainVlanId"),
)
if mibBuilder.loadTexts:
    ipbpvcDomainVlanEntry.setStatus("current")
_IpbpvcDomainVlanId_Type = VlanIndex
_IpbpvcDomainVlanId_Object = MibTableColumn
ipbpvcDomainVlanId = _IpbpvcDomainVlanId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 12, 2, 1, 1),
    _IpbpvcDomainVlanId_Type()
)
ipbpvcDomainVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipbpvcDomainVlanId.setStatus("current")


class _IpbpvcDomainDhcpVlanEnable_Type(Integer32):
    """Custom type ipbpvcDomainDhcpVlanEnable based on Integer32"""
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


_IpbpvcDomainDhcpVlanEnable_Type.__name__ = "Integer32"
_IpbpvcDomainDhcpVlanEnable_Object = MibTableColumn
ipbpvcDomainDhcpVlanEnable = _IpbpvcDomainDhcpVlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 12, 2, 1, 2),
    _IpbpvcDomainDhcpVlanEnable_Type()
)
ipbpvcDomainDhcpVlanEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipbpvcDomainDhcpVlanEnable.setStatus("current")
_IpbpvcDomainVlanRowStatus_Type = RowStatus
_IpbpvcDomainVlanRowStatus_Object = MibTableColumn
ipbpvcDomainVlanRowStatus = _IpbpvcDomainVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 12, 2, 1, 3),
    _IpbpvcDomainVlanRowStatus_Type()
)
ipbpvcDomainVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipbpvcDomainVlanRowStatus.setStatus("current")
_IpbpvcEdgeRouterTable_Object = MibTable
ipbpvcEdgeRouterTable = _IpbpvcEdgeRouterTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 12, 3)
)
if mibBuilder.loadTexts:
    ipbpvcEdgeRouterTable.setStatus("current")
_IpbpvcEdgeRouterEntry_Object = MibTableRow
ipbpvcEdgeRouterEntry = _IpbpvcEdgeRouterEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 12, 3, 1)
)
ipbpvcEdgeRouterEntry.setIndexNames(
    (0, "ZYXEL-IES1248", "ipbpvcDomainName"),
    (0, "ZYXEL-IES1248", "ipbpvcEdgeRouterIp"),
    (0, "ZYXEL-IES1248", "ipbpvcEdgeRouterMask"),
    (0, "ZYXEL-IES1248", "ipbpvcEdgeRouterVid"),
)
if mibBuilder.loadTexts:
    ipbpvcEdgeRouterEntry.setStatus("current")
_IpbpvcEdgeRouterIp_Type = IpAddress
_IpbpvcEdgeRouterIp_Object = MibTableColumn
ipbpvcEdgeRouterIp = _IpbpvcEdgeRouterIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 12, 3, 1, 1),
    _IpbpvcEdgeRouterIp_Type()
)
ipbpvcEdgeRouterIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipbpvcEdgeRouterIp.setStatus("current")
_IpbpvcEdgeRouterVid_Type = VlanIndex
_IpbpvcEdgeRouterVid_Object = MibTableColumn
ipbpvcEdgeRouterVid = _IpbpvcEdgeRouterVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 12, 3, 1, 2),
    _IpbpvcEdgeRouterVid_Type()
)
ipbpvcEdgeRouterVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipbpvcEdgeRouterVid.setStatus("current")
_IpbpvcEdgeRouterMask_Type = Integer32
_IpbpvcEdgeRouterMask_Object = MibTableColumn
ipbpvcEdgeRouterMask = _IpbpvcEdgeRouterMask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 12, 3, 1, 3),
    _IpbpvcEdgeRouterMask_Type()
)
ipbpvcEdgeRouterMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipbpvcEdgeRouterMask.setStatus("current")
_IpbpvcEdgeRouterRowStatus_Type = RowStatus
_IpbpvcEdgeRouterRowStatus_Object = MibTableColumn
ipbpvcEdgeRouterRowStatus = _IpbpvcEdgeRouterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 12, 3, 1, 4),
    _IpbpvcEdgeRouterRowStatus_Type()
)
ipbpvcEdgeRouterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipbpvcEdgeRouterRowStatus.setStatus("current")
_IpbpvcInterfaceTable_Object = MibTable
ipbpvcInterfaceTable = _IpbpvcInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 12, 4)
)
if mibBuilder.loadTexts:
    ipbpvcInterfaceTable.setStatus("current")
_IpbpvcInterfaceEntry_Object = MibTableRow
ipbpvcInterfaceEntry = _IpbpvcInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 12, 4, 1)
)
ipbpvcInterfaceEntry.setIndexNames(
    (0, "ZYXEL-IES1248", "ipbpvcDomainName"),
    (0, "ZYXEL-IES1248", "ipbpvcInterfaceIp"),
    (0, "ZYXEL-IES1248", "ipbpvcInterfaceMask"),
    (0, "ZYXEL-IES1248", "ipbpvcInterfaceVid"),
)
if mibBuilder.loadTexts:
    ipbpvcInterfaceEntry.setStatus("current")
_IpbpvcInterfaceIp_Type = IpAddress
_IpbpvcInterfaceIp_Object = MibTableColumn
ipbpvcInterfaceIp = _IpbpvcInterfaceIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 12, 4, 1, 1),
    _IpbpvcInterfaceIp_Type()
)
ipbpvcInterfaceIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipbpvcInterfaceIp.setStatus("current")
_IpbpvcInterfaceMask_Type = Integer32
_IpbpvcInterfaceMask_Object = MibTableColumn
ipbpvcInterfaceMask = _IpbpvcInterfaceMask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 12, 4, 1, 2),
    _IpbpvcInterfaceMask_Type()
)
ipbpvcInterfaceMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipbpvcInterfaceMask.setStatus("current")
_IpbpvcInterfaceVid_Type = VlanIndex
_IpbpvcInterfaceVid_Object = MibTableColumn
ipbpvcInterfaceVid = _IpbpvcInterfaceVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 12, 4, 1, 3),
    _IpbpvcInterfaceVid_Type()
)
ipbpvcInterfaceVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipbpvcInterfaceVid.setStatus("current")
_IpbpvcInterfaceIfIndex_Type = Integer32
_IpbpvcInterfaceIfIndex_Object = MibTableColumn
ipbpvcInterfaceIfIndex = _IpbpvcInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 12, 4, 1, 4),
    _IpbpvcInterfaceIfIndex_Type()
)
ipbpvcInterfaceIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipbpvcInterfaceIfIndex.setStatus("current")
_IpbpvcInterfaceVpi_Type = Integer32
_IpbpvcInterfaceVpi_Object = MibTableColumn
ipbpvcInterfaceVpi = _IpbpvcInterfaceVpi_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 12, 4, 1, 5),
    _IpbpvcInterfaceVpi_Type()
)
ipbpvcInterfaceVpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipbpvcInterfaceVpi.setStatus("current")
_IpbpvcInterfaceVci_Type = Integer32
_IpbpvcInterfaceVci_Object = MibTableColumn
ipbpvcInterfaceVci = _IpbpvcInterfaceVci_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 12, 4, 1, 6),
    _IpbpvcInterfaceVci_Type()
)
ipbpvcInterfaceVci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipbpvcInterfaceVci.setStatus("current")
_IpbpvcInterfaceRowStatus_Type = RowStatus
_IpbpvcInterfaceRowStatus_Object = MibTableColumn
ipbpvcInterfaceRowStatus = _IpbpvcInterfaceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 12, 4, 1, 7),
    _IpbpvcInterfaceRowStatus_Type()
)
ipbpvcInterfaceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipbpvcInterfaceRowStatus.setStatus("current")
_IpbpvcRouteTable_Object = MibTable
ipbpvcRouteTable = _IpbpvcRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 12, 5)
)
if mibBuilder.loadTexts:
    ipbpvcRouteTable.setStatus("current")
_IpbpvcRouteEntry_Object = MibTableRow
ipbpvcRouteEntry = _IpbpvcRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 12, 5, 1)
)
ipbpvcRouteEntry.setIndexNames(
    (0, "ZYXEL-IES1248", "ipbpvcDomainName"),
    (0, "ZYXEL-IES1248", "ipbpvcRouteIp"),
    (0, "ZYXEL-IES1248", "ipbpvcRouteMask"),
    (0, "ZYXEL-IES1248", "ipbpvcRouteNextHop"),
)
if mibBuilder.loadTexts:
    ipbpvcRouteEntry.setStatus("current")
_IpbpvcRouteIp_Type = IpAddress
_IpbpvcRouteIp_Object = MibTableColumn
ipbpvcRouteIp = _IpbpvcRouteIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 12, 5, 1, 1),
    _IpbpvcRouteIp_Type()
)
ipbpvcRouteIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipbpvcRouteIp.setStatus("current")
_IpbpvcRouteMask_Type = Integer32
_IpbpvcRouteMask_Object = MibTableColumn
ipbpvcRouteMask = _IpbpvcRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 12, 5, 1, 2),
    _IpbpvcRouteMask_Type()
)
ipbpvcRouteMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipbpvcRouteMask.setStatus("current")
_IpbpvcRouteNextHop_Type = IpAddress
_IpbpvcRouteNextHop_Object = MibTableColumn
ipbpvcRouteNextHop = _IpbpvcRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 12, 5, 1, 3),
    _IpbpvcRouteNextHop_Type()
)
ipbpvcRouteNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipbpvcRouteNextHop.setStatus("current")


class _IpbpvcRouteMetric_Type(Integer32):
    """Custom type ipbpvcRouteMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_IpbpvcRouteMetric_Type.__name__ = "Integer32"
_IpbpvcRouteMetric_Object = MibTableColumn
ipbpvcRouteMetric = _IpbpvcRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 12, 5, 1, 4),
    _IpbpvcRouteMetric_Type()
)
ipbpvcRouteMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipbpvcRouteMetric.setStatus("current")
_IpbpvcRoutePriority_Type = Integer32
_IpbpvcRoutePriority_Object = MibTableColumn
ipbpvcRoutePriority = _IpbpvcRoutePriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 12, 5, 1, 5),
    _IpbpvcRoutePriority_Type()
)
ipbpvcRoutePriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipbpvcRoutePriority.setStatus("current")
_IpbpvcRouteRowStatus_Type = RowStatus
_IpbpvcRouteRowStatus_Object = MibTableColumn
ipbpvcRouteRowStatus = _IpbpvcRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 12, 5, 1, 6),
    _IpbpvcRouteRowStatus_Type()
)
ipbpvcRouteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipbpvcRouteRowStatus.setStatus("current")
_IpbpvcTable_Object = MibTable
ipbpvcTable = _IpbpvcTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 12, 6)
)
if mibBuilder.loadTexts:
    ipbpvcTable.setStatus("current")
_IpbpvcEntry_Object = MibTableRow
ipbpvcEntry = _IpbpvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 12, 6, 1)
)
ipbpvcEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZYXEL-IES1248", "ipbpvcVpi"),
    (0, "ZYXEL-IES1248", "ipbpvcVci"),
    (0, "ZYXEL-IES1248", "ipbpvcPvid"),
)
if mibBuilder.loadTexts:
    ipbpvcEntry.setStatus("current")
_IpbpvcVpi_Type = Integer32
_IpbpvcVpi_Object = MibTableColumn
ipbpvcVpi = _IpbpvcVpi_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 12, 6, 1, 1),
    _IpbpvcVpi_Type()
)
ipbpvcVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipbpvcVpi.setStatus("current")
_IpbpvcVci_Type = Integer32
_IpbpvcVci_Object = MibTableColumn
ipbpvcVci = _IpbpvcVci_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 12, 6, 1, 2),
    _IpbpvcVci_Type()
)
ipbpvcVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipbpvcVci.setStatus("current")
_IpbpvcPvid_Type = Integer32
_IpbpvcPvid_Object = MibTableColumn
ipbpvcPvid = _IpbpvcPvid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 12, 6, 1, 3),
    _IpbpvcPvid_Type()
)
ipbpvcPvid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipbpvcPvid.setStatus("current")


class _IpbpvcEncap_Type(Integer32):
    """Custom type ipbpvcEncap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipoe", 1),
          ("ipoa", 2))
    )


_IpbpvcEncap_Type.__name__ = "Integer32"
_IpbpvcEncap_Object = MibTableColumn
ipbpvcEncap = _IpbpvcEncap_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 12, 6, 1, 4),
    _IpbpvcEncap_Type()
)
ipbpvcEncap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipbpvcEncap.setStatus("current")


class _IpbpvcPriority_Type(Integer32):
    """Custom type ipbpvcPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_IpbpvcPriority_Type.__name__ = "Integer32"
_IpbpvcPriority_Object = MibTableColumn
ipbpvcPriority = _IpbpvcPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 12, 6, 1, 5),
    _IpbpvcPriority_Type()
)
ipbpvcPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipbpvcPriority.setStatus("current")
_IpbpvcProfile_Type = OctetString
_IpbpvcProfile_Object = MibTableColumn
ipbpvcProfile = _IpbpvcProfile_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 12, 6, 1, 6),
    _IpbpvcProfile_Type()
)
ipbpvcProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipbpvcProfile.setStatus("current")
_IpbpvcRowStatus_Type = Integer32
_IpbpvcRowStatus_Object = MibTableColumn
ipbpvcRowStatus = _IpbpvcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 12, 6, 1, 7),
    _IpbpvcRowStatus_Type()
)
ipbpvcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipbpvcRowStatus.setStatus("current")
_IpbpvcProfileUS_Type = OctetString
_IpbpvcProfileUS_Object = MibTableColumn
ipbpvcProfileUS = _IpbpvcProfileUS_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 12, 6, 1, 8),
    _IpbpvcProfileUS_Type()
)
ipbpvcProfileUS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipbpvcProfileUS.setStatus("current")
_Arpproxy_ObjectIdentity = ObjectIdentity
arpproxy = _Arpproxy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 12, 8)
)


class _ArpproxyAge_Type(Integer32):
    """Custom type arpproxyAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 10000),
    )


_ArpproxyAge_Type.__name__ = "Integer32"
_ArpproxyAge_Object = MibScalar
arpproxyAge = _ArpproxyAge_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 12, 8, 1),
    _ArpproxyAge_Type()
)
arpproxyAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpproxyAge.setStatus("current")
if mibBuilder.loadTexts:
    arpproxyAge.setUnits("second")
_ArpproxyFlush_ObjectIdentity = ObjectIdentity
arpproxyFlush = _ArpproxyFlush_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 12, 8, 2)
)


class _ArpproxyFlushTarget_Type(Integer32):
    """Custom type arpproxyFlushTarget based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("edgerouter", 2),
          ("interface", 3))
    )


_ArpproxyFlushTarget_Type.__name__ = "Integer32"
_ArpproxyFlushTarget_Object = MibScalar
arpproxyFlushTarget = _ArpproxyFlushTarget_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 12, 8, 2, 1),
    _ArpproxyFlushTarget_Type()
)
arpproxyFlushTarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpproxyFlushTarget.setStatus("current")
_ArpproxyFlushOps_Type = Integer32
_ArpproxyFlushOps_Object = MibScalar
arpproxyFlushOps = _ArpproxyFlushOps_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 12, 8, 2, 2),
    _ArpproxyFlushOps_Type()
)
arpproxyFlushOps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpproxyFlushOps.setStatus("current")
_ArpproxyFlushEdgeRouterIp_Type = IpAddress
_ArpproxyFlushEdgeRouterIp_Object = MibScalar
arpproxyFlushEdgeRouterIp = _ArpproxyFlushEdgeRouterIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 12, 8, 2, 3),
    _ArpproxyFlushEdgeRouterIp_Type()
)
arpproxyFlushEdgeRouterIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpproxyFlushEdgeRouterIp.setStatus("current")
_ArpproxyFlushEdgeRouterVid_Type = VlanIndex
_ArpproxyFlushEdgeRouterVid_Object = MibScalar
arpproxyFlushEdgeRouterVid = _ArpproxyFlushEdgeRouterVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 12, 8, 2, 4),
    _ArpproxyFlushEdgeRouterVid_Type()
)
arpproxyFlushEdgeRouterVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpproxyFlushEdgeRouterVid.setStatus("current")
_ArpproxyFlushInterfaceIp_Type = IpAddress
_ArpproxyFlushInterfaceIp_Object = MibScalar
arpproxyFlushInterfaceIp = _ArpproxyFlushInterfaceIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 12, 8, 2, 5),
    _ArpproxyFlushInterfaceIp_Type()
)
arpproxyFlushInterfaceIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpproxyFlushInterfaceIp.setStatus("current")
_ArpproxyFlushInterfaceMask_Type = Integer32
_ArpproxyFlushInterfaceMask_Object = MibScalar
arpproxyFlushInterfaceMask = _ArpproxyFlushInterfaceMask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 12, 8, 2, 6),
    _ArpproxyFlushInterfaceMask_Type()
)
arpproxyFlushInterfaceMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpproxyFlushInterfaceMask.setStatus("current")
_ArpproxyFlushInterfaceVid_Type = VlanIndex
_ArpproxyFlushInterfaceVid_Object = MibScalar
arpproxyFlushInterfaceVid = _ArpproxyFlushInterfaceVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 12, 8, 2, 7),
    _ArpproxyFlushInterfaceVid_Type()
)
arpproxyFlushInterfaceVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpproxyFlushInterfaceVid.setStatus("current")
_Gbond_ObjectIdentity = ObjectIdentity
gbond = _Gbond_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 51)
)
_GbondGroupTable_Object = MibTable
gbondGroupTable = _GbondGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 51, 1)
)
if mibBuilder.loadTexts:
    gbondGroupTable.setStatus("current")
_GbondGroupEntry_Object = MibTableRow
gbondGroupEntry = _GbondGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 51, 1, 1)
)
gbondGroupEntry.setIndexNames(
    (0, "ZYXEL-IES1248", "gbondGroupName"),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 51, 1, 1, 1),
    _GbondGroupName_Type()
)
gbondGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gbondGroupName.setStatus("current")
_GbondGroupPorts_Type = OctetString
_GbondGroupPorts_Object = MibTableColumn
gbondGroupPorts = _GbondGroupPorts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 51, 1, 1, 2),
    _GbondGroupPorts_Type()
)
gbondGroupPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gbondGroupPorts.setStatus("current")
_GbondGroupUpRate_Type = Unsigned32
_GbondGroupUpRate_Object = MibTableColumn
gbondGroupUpRate = _GbondGroupUpRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 51, 1, 1, 4),
    _GbondGroupUpRate_Type()
)
gbondGroupUpRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gbondGroupUpRate.setStatus("current")
_GbondGroupDownRate_Type = Unsigned32
_GbondGroupDownRate_Object = MibTableColumn
gbondGroupDownRate = _GbondGroupDownRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 51, 1, 1, 5),
    _GbondGroupDownRate_Type()
)
gbondGroupDownRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gbondGroupDownRate.setStatus("current")
_GbondGroupRowStatus_Type = RowStatus
_GbondGroupRowStatus_Object = MibTableColumn
gbondGroupRowStatus = _GbondGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 8, 51, 1, 1, 6),
    _GbondGroupRowStatus_Type()
)
gbondGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gbondGroupRowStatus.setStatus("current")
_Switch_ObjectIdentity = ObjectIdentity
switch = _Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10)
)
_Dot1x_ObjectIdentity = ObjectIdentity
dot1x = _Dot1x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 5)
)
_MaxNumberOfRadiusServers_Type = Integer32
_MaxNumberOfRadiusServers_Object = MibScalar
maxNumberOfRadiusServers = _MaxNumberOfRadiusServers_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 5, 1),
    _MaxNumberOfRadiusServers_Type()
)
maxNumberOfRadiusServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumberOfRadiusServers.setStatus("current")
_RadiusServerTable_Object = MibTable
radiusServerTable = _RadiusServerTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 5, 2)
)
if mibBuilder.loadTexts:
    radiusServerTable.setStatus("current")
_RadiusServerEntry_Object = MibTableRow
radiusServerEntry = _RadiusServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 5, 2, 1)
)
radiusServerEntry.setIndexNames(
    (0, "ZYXEL-IES1248", "radiusServerIndex"),
)
if mibBuilder.loadTexts:
    radiusServerEntry.setStatus("current")
_RadiusServerIndex_Type = Integer32
_RadiusServerIndex_Object = MibTableColumn
radiusServerIndex = _RadiusServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 5, 2, 1, 1),
    _RadiusServerIndex_Type()
)
radiusServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusServerIndex.setStatus("current")
_RadiusServerIp_Type = IpAddress
_RadiusServerIp_Object = MibTableColumn
radiusServerIp = _RadiusServerIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 5, 2, 1, 2),
    _RadiusServerIp_Type()
)
radiusServerIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radiusServerIp.setStatus("current")
_RadiusServerPort_Type = Integer32
_RadiusServerPort_Object = MibTableColumn
radiusServerPort = _RadiusServerPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 5, 2, 1, 3),
    _RadiusServerPort_Type()
)
radiusServerPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radiusServerPort.setStatus("current")
_RadiusSharedSecret_Type = DisplayString
_RadiusSharedSecret_Object = MibTableColumn
radiusSharedSecret = _RadiusSharedSecret_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 5, 2, 1, 4),
    _RadiusSharedSecret_Type()
)
radiusSharedSecret.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radiusSharedSecret.setStatus("current")
_RadiusServerRowStatus_Type = RowStatus
_RadiusServerRowStatus_Object = MibTableColumn
radiusServerRowStatus = _RadiusServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 5, 2, 1, 5),
    _RadiusServerRowStatus_Type()
)
radiusServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radiusServerRowStatus.setStatus("current")


class _Dot1xEnable_Type(Integer32):
    """Custom type dot1xEnable based on Integer32"""
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


_Dot1xEnable_Type.__name__ = "Integer32"
_Dot1xEnable_Object = MibScalar
dot1xEnable = _Dot1xEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 5, 3),
    _Dot1xEnable_Type()
)
dot1xEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1xEnable.setStatus("current")
_Dot1xPortTable_Object = MibTable
dot1xPortTable = _Dot1xPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 5, 4)
)
if mibBuilder.loadTexts:
    dot1xPortTable.setStatus("current")
_Dot1xPortEntry_Object = MibTableRow
dot1xPortEntry = _Dot1xPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 5, 4, 1)
)
dot1xPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dot1xPortEntry.setStatus("current")


class _Dot1xPortEnable_Type(Integer32):
    """Custom type dot1xPortEnable based on Integer32"""
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


_Dot1xPortEnable_Type.__name__ = "Integer32"
_Dot1xPortEnable_Object = MibTableColumn
dot1xPortEnable = _Dot1xPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 5, 4, 1, 1),
    _Dot1xPortEnable_Type()
)
dot1xPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1xPortEnable.setStatus("current")


class _Dot1xPortControl_Type(Integer32):
    """Custom type dot1xPortControl based on Integer32"""
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
          ("forceAuth", 2),
          ("forceUnAuth", 3))
    )


_Dot1xPortControl_Type.__name__ = "Integer32"
_Dot1xPortControl_Object = MibTableColumn
dot1xPortControl = _Dot1xPortControl_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 5, 4, 1, 2),
    _Dot1xPortControl_Type()
)
dot1xPortControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1xPortControl.setStatus("current")


class _Dot1xPortReAuthEnable_Type(Integer32):
    """Custom type dot1xPortReAuthEnable based on Integer32"""
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


_Dot1xPortReAuthEnable_Type.__name__ = "Integer32"
_Dot1xPortReAuthEnable_Object = MibTableColumn
dot1xPortReAuthEnable = _Dot1xPortReAuthEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 5, 4, 1, 3),
    _Dot1xPortReAuthEnable_Type()
)
dot1xPortReAuthEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1xPortReAuthEnable.setStatus("current")
_Dot1xPortReAuthPeriod_Type = Integer32
_Dot1xPortReAuthPeriod_Object = MibTableColumn
dot1xPortReAuthPeriod = _Dot1xPortReAuthPeriod_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 5, 4, 1, 4),
    _Dot1xPortReAuthPeriod_Type()
)
dot1xPortReAuthPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1xPortReAuthPeriod.setStatus("current")


class _RadiusMode_Type(Integer32):
    """Custom type radiusMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("authentication_server", 1),
          ("local_user_profile", 2))
    )


_RadiusMode_Type.__name__ = "Integer32"
_RadiusMode_Object = MibScalar
radiusMode = _RadiusMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 5, 5),
    _RadiusMode_Type()
)
radiusMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusMode.setStatus("current")
_MaxNumberOfRadiusUserProfiles_Type = Integer32
_MaxNumberOfRadiusUserProfiles_Object = MibScalar
maxNumberOfRadiusUserProfiles = _MaxNumberOfRadiusUserProfiles_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 5, 6),
    _MaxNumberOfRadiusUserProfiles_Type()
)
maxNumberOfRadiusUserProfiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumberOfRadiusUserProfiles.setStatus("current")
_RadiusUserProfileTable_Object = MibTable
radiusUserProfileTable = _RadiusUserProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 5, 7)
)
if mibBuilder.loadTexts:
    radiusUserProfileTable.setStatus("current")
_RadiusUserProfileEntry_Object = MibTableRow
radiusUserProfileEntry = _RadiusUserProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 5, 7, 1)
)
radiusUserProfileEntry.setIndexNames(
    (0, "ZYXEL-IES1248", "radiusUserProfileUserName"),
)
if mibBuilder.loadTexts:
    radiusUserProfileEntry.setStatus("current")
_RadiusUserProfileUserName_Type = DisplayString
_RadiusUserProfileUserName_Object = MibTableColumn
radiusUserProfileUserName = _RadiusUserProfileUserName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 5, 7, 1, 1),
    _RadiusUserProfileUserName_Type()
)
radiusUserProfileUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusUserProfileUserName.setStatus("current")
_RadiusUserProfileUserPassword_Type = DisplayString
_RadiusUserProfileUserPassword_Object = MibTableColumn
radiusUserProfileUserPassword = _RadiusUserProfileUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 5, 7, 1, 2),
    _RadiusUserProfileUserPassword_Type()
)
radiusUserProfileUserPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radiusUserProfileUserPassword.setStatus("current")
_RadiusUserProfileRowStatus_Type = RowStatus
_RadiusUserProfileRowStatus_Object = MibTableColumn
radiusUserProfileRowStatus = _RadiusUserProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 5, 7, 1, 3),
    _RadiusUserProfileRowStatus_Type()
)
radiusUserProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radiusUserProfileRowStatus.setStatus("current")
_Dscp_ObjectIdentity = ObjectIdentity
dscp = _Dscp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 10)
)
_DscpMappingTable_Object = MibTable
dscpMappingTable = _DscpMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 10, 1)
)
if mibBuilder.loadTexts:
    dscpMappingTable.setStatus("current")
_DscpMappingEntry_Object = MibTableRow
dscpMappingEntry = _DscpMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 10, 1, 1)
)
dscpMappingEntry.setIndexNames(
    (0, "ZYXEL-IES1248", "dscpSrcCodePoint"),
)
if mibBuilder.loadTexts:
    dscpMappingEntry.setStatus("current")
_DscpSrcCodePoint_Type = Integer32
_DscpSrcCodePoint_Object = MibTableColumn
dscpSrcCodePoint = _DscpSrcCodePoint_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 10, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 10, 1, 1, 3),
    _DscpMapPriority_Type()
)
dscpMapPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dscpMapPriority.setStatus("current")
_DscpPortTable_Object = MibTable
dscpPortTable = _DscpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 10, 2)
)
if mibBuilder.loadTexts:
    dscpPortTable.setStatus("current")
_DscpPortEntry_Object = MibTableRow
dscpPortEntry = _DscpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 10, 2, 1)
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 10, 2, 1, 1),
    _DscpStatusEnable_Type()
)
dscpStatusEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dscpStatusEnable.setStatus("current")
_VlanIsolation_ObjectIdentity = ObjectIdentity
vlanIsolation = _VlanIsolation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 12)
)
_VlanIsolationTable_Object = MibTable
vlanIsolationTable = _VlanIsolationTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 12, 1)
)
if mibBuilder.loadTexts:
    vlanIsolationTable.setStatus("current")
_VlanIsolationEntry_Object = MibTableRow
vlanIsolationEntry = _VlanIsolationEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 12, 1, 1)
)
vlanIsolationEntry.setIndexNames(
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
)
if mibBuilder.loadTexts:
    vlanIsolationEntry.setStatus("current")
_VlanIsolationRowStatus_Type = RowStatus
_VlanIsolationRowStatus_Object = MibTableColumn
vlanIsolationRowStatus = _VlanIsolationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 12, 1, 1, 1),
    _VlanIsolationRowStatus_Type()
)
vlanIsolationRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanIsolationRowStatus.setStatus("current")
_EnetMtu_ObjectIdentity = ObjectIdentity
enetMtu = _EnetMtu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 13)
)
_EnetMaxMtu_Type = Integer32
_EnetMaxMtu_Object = MibScalar
enetMaxMtu = _EnetMaxMtu_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 13, 1),
    _EnetMaxMtu_Type()
)
enetMaxMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enetMaxMtu.setStatus("current")
_Dhcp_ObjectIdentity = ObjectIdentity
dhcp = _Dhcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 51)
)


class _DhcpRelayEnable_Type(Integer32):
    """Custom type dhcpRelayEnable based on Integer32"""
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
          ("both", 2),
          ("disable", 3))
    )


_DhcpRelayEnable_Type.__name__ = "Integer32"
_DhcpRelayEnable_Object = MibScalar
dhcpRelayEnable = _DhcpRelayEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 51, 1),
    _DhcpRelayEnable_Type()
)
dhcpRelayEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelayEnable.setStatus("current")
_DhcpRelay82Table_Object = MibTable
dhcpRelay82Table = _DhcpRelay82Table_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 51, 2)
)
if mibBuilder.loadTexts:
    dhcpRelay82Table.setStatus("current")
_DhcpRelay82Entry_Object = MibTableRow
dhcpRelay82Entry = _DhcpRelay82Entry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 51, 2, 1)
)
dhcpRelay82Entry.setIndexNames(
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
)
if mibBuilder.loadTexts:
    dhcpRelay82Entry.setStatus("current")
_DhcpRelay82PrimaryServer_Type = IpAddress
_DhcpRelay82PrimaryServer_Object = MibTableColumn
dhcpRelay82PrimaryServer = _DhcpRelay82PrimaryServer_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 51, 2, 1, 1),
    _DhcpRelay82PrimaryServer_Type()
)
dhcpRelay82PrimaryServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelay82PrimaryServer.setStatus("current")
_DhcpRelay82SecondaryServer_Type = IpAddress
_DhcpRelay82SecondaryServer_Object = MibTableColumn
dhcpRelay82SecondaryServer = _DhcpRelay82SecondaryServer_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 51, 2, 1, 2),
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
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_DhcpRelay82ActiveServer_Type.__name__ = "Integer32"
_DhcpRelay82ActiveServer_Object = MibTableColumn
dhcpRelay82ActiveServer = _DhcpRelay82ActiveServer_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 51, 2, 1, 3),
    _DhcpRelay82ActiveServer_Type()
)
dhcpRelay82ActiveServer.setMaxAccess("read-write")
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 51, 2, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 51, 2, 1, 5),
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
          ("both", 2))
    )


_DhcpRelay82RelayMode_Type.__name__ = "Integer32"
_DhcpRelay82RelayMode_Object = MibTableColumn
dhcpRelay82RelayMode = _DhcpRelay82RelayMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 51, 2, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 51, 2, 1, 8),
    _DhcpRelay82Suboption2Enable_Type()
)
dhcpRelay82Suboption2Enable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpRelay82Suboption2Enable.setStatus("current")
_DhcpRelay82Suboption2Info_Type = DisplayString
_DhcpRelay82Suboption2Info_Object = MibTableColumn
dhcpRelay82Suboption2Info = _DhcpRelay82Suboption2Info_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 51, 2, 1, 9),
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
          ("both", 2),
          ("disable", 3))
    )


_DhcpRelay82EntryEnable_Type.__name__ = "Integer32"
_DhcpRelay82EntryEnable_Object = MibTableColumn
dhcpRelay82EntryEnable = _DhcpRelay82EntryEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 51, 2, 1, 10),
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
          ("tr101WithVlan", 3))
    )


_DhcpRelay82EntryOptionMode_Type.__name__ = "Integer32"
_DhcpRelay82EntryOptionMode_Object = MibTableColumn
dhcpRelay82EntryOptionMode = _DhcpRelay82EntryOptionMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 51, 2, 1, 11),
    _DhcpRelay82EntryOptionMode_Type()
)
dhcpRelay82EntryOptionMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpRelay82EntryOptionMode.setStatus("current")


class _DhcpRelayOption82Sub1Info_Type(DisplayString):
    """Custom type dhcpRelayOption82Sub1Info based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 23),
    )


_DhcpRelayOption82Sub1Info_Type.__name__ = "DisplayString"
_DhcpRelayOption82Sub1Info_Object = MibScalar
dhcpRelayOption82Sub1Info = _DhcpRelayOption82Sub1Info_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 51, 3),
    _DhcpRelayOption82Sub1Info_Type()
)
dhcpRelayOption82Sub1Info.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelayOption82Sub1Info.setStatus("current")
_MaxNumOfDhcpRelay82Conf_Type = Integer32
_MaxNumOfDhcpRelay82Conf_Object = MibScalar
maxNumOfDhcpRelay82Conf = _MaxNumOfDhcpRelay82Conf_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 51, 4),
    _MaxNumOfDhcpRelay82Conf_Type()
)
maxNumOfDhcpRelay82Conf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumOfDhcpRelay82Conf.setStatus("current")


class _DhcpRelayOption82Sub1Enable_Type(Integer32):
    """Custom type dhcpRelayOption82Sub1Enable based on Integer32"""
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


_DhcpRelayOption82Sub1Enable_Type.__name__ = "Integer32"
_DhcpRelayOption82Sub1Enable_Object = MibScalar
dhcpRelayOption82Sub1Enable = _DhcpRelayOption82Sub1Enable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 51, 5),
    _DhcpRelayOption82Sub1Enable_Type()
)
dhcpRelayOption82Sub1Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelayOption82Sub1Enable.setStatus("current")


class _DhcpRelayOption82Sub2Info_Type(DisplayString):
    """Custom type dhcpRelayOption82Sub2Info based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 23),
    )


_DhcpRelayOption82Sub2Info_Type.__name__ = "DisplayString"
_DhcpRelayOption82Sub2Info_Object = MibScalar
dhcpRelayOption82Sub2Info = _DhcpRelayOption82Sub2Info_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 51, 6),
    _DhcpRelayOption82Sub2Info_Type()
)
dhcpRelayOption82Sub2Info.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelayOption82Sub2Info.setStatus("current")


class _DhcpRelayOption82Sub2Enable_Type(Integer32):
    """Custom type dhcpRelayOption82Sub2Enable based on Integer32"""
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


_DhcpRelayOption82Sub2Enable_Type.__name__ = "Integer32"
_DhcpRelayOption82Sub2Enable_Object = MibScalar
dhcpRelayOption82Sub2Enable = _DhcpRelayOption82Sub2Enable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 51, 7),
    _DhcpRelayOption82Sub2Enable_Type()
)
dhcpRelayOption82Sub2Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelayOption82Sub2Enable.setStatus("current")
_Macfilter_ObjectIdentity = ObjectIdentity
macfilter = _Macfilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 53)
)
_MacFilterPortTable_Object = MibTable
macFilterPortTable = _MacFilterPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 53, 1)
)
if mibBuilder.loadTexts:
    macFilterPortTable.setStatus("current")
_MacFilterPortEntry_Object = MibTableRow
macFilterPortEntry = _MacFilterPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 53, 1, 1)
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 53, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 53, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 53, 1, 1, 3),
    _MacFilterPortFilterMode_Type()
)
macFilterPortFilterMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macFilterPortFilterMode.setStatus("current")
_MaxNumOfMacFiltersInSystem_Type = Integer32
_MaxNumOfMacFiltersInSystem_Object = MibScalar
maxNumOfMacFiltersInSystem = _MaxNumOfMacFiltersInSystem_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 53, 2),
    _MaxNumOfMacFiltersInSystem_Type()
)
maxNumOfMacFiltersInSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumOfMacFiltersInSystem.setStatus("current")
_MaxNumOfMacFiltersPerPort_Type = Integer32
_MaxNumOfMacFiltersPerPort_Object = MibScalar
maxNumOfMacFiltersPerPort = _MaxNumOfMacFiltersPerPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 53, 3),
    _MaxNumOfMacFiltersPerPort_Type()
)
maxNumOfMacFiltersPerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumOfMacFiltersPerPort.setStatus("current")
_CurrNumOfMacFiltersInSystem_Type = Integer32
_CurrNumOfMacFiltersInSystem_Object = MibScalar
currNumOfMacFiltersInSystem = _CurrNumOfMacFiltersInSystem_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 53, 4),
    _CurrNumOfMacFiltersInSystem_Type()
)
currNumOfMacFiltersInSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currNumOfMacFiltersInSystem.setStatus("current")
_MacFilterTable_Object = MibTable
macFilterTable = _MacFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 53, 5)
)
if mibBuilder.loadTexts:
    macFilterTable.setStatus("current")
_MacFilterEntry_Object = MibTableRow
macFilterEntry = _MacFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 53, 5, 1)
)
macFilterEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZYXEL-IES1248", "macFilterAddr"),
)
if mibBuilder.loadTexts:
    macFilterEntry.setStatus("current")
_MacFilterAddr_Type = PhysAddress
_MacFilterAddr_Object = MibTableColumn
macFilterAddr = _MacFilterAddr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 53, 5, 1, 1),
    _MacFilterAddr_Type()
)
macFilterAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macFilterAddr.setStatus("current")
_MacFilterRowStatus_Type = RowStatus
_MacFilterRowStatus_Object = MibTableColumn
macFilterRowStatus = _MacFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 53, 5, 1, 2),
    _MacFilterRowStatus_Type()
)
macFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    macFilterRowStatus.setStatus("current")
_MacfilterBatchSet_ObjectIdentity = ObjectIdentity
macfilterBatchSet = _MacfilterBatchSet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 53, 6)
)
_MacfilterTarget_Type = OctetString
_MacfilterTarget_Object = MibScalar
macfilterTarget = _MacfilterTarget_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 53, 6, 1),
    _MacfilterTarget_Type()
)
macfilterTarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macfilterTarget.setStatus("current")
_MacfilterOps_Type = Integer32
_MacfilterOps_Object = MibScalar
macfilterOps = _MacfilterOps_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 53, 6, 2),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 53, 6, 3),
    _MacFilterMacCountForBatchSet_Type()
)
macFilterMacCountForBatchSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macFilterMacCountForBatchSet.setStatus("current")
_OuiFilterTable_Object = MibTable
ouiFilterTable = _OuiFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 53, 7)
)
if mibBuilder.loadTexts:
    ouiFilterTable.setStatus("current")
_OuiFilterEntry_Object = MibTableRow
ouiFilterEntry = _OuiFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 53, 7, 1)
)
ouiFilterEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZYXEL-IES1248", "ouiFilterAddr"),
)
if mibBuilder.loadTexts:
    ouiFilterEntry.setStatus("current")
_OuiFilterAddr_Type = OctetString
_OuiFilterAddr_Object = MibTableColumn
ouiFilterAddr = _OuiFilterAddr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 53, 7, 1, 1),
    _OuiFilterAddr_Type()
)
ouiFilterAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ouiFilterAddr.setStatus("current")
_OuiFilterRowStatus_Type = RowStatus
_OuiFilterRowStatus_Object = MibTableColumn
ouiFilterRowStatus = _OuiFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 53, 7, 1, 2),
    _OuiFilterRowStatus_Type()
)
ouiFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ouiFilterRowStatus.setStatus("current")
_MaxNumOfOuiFiltersPerPort_Type = Integer32
_MaxNumOfOuiFiltersPerPort_Object = MibScalar
maxNumOfOuiFiltersPerPort = _MaxNumOfOuiFiltersPerPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 53, 8),
    _MaxNumOfOuiFiltersPerPort_Type()
)
maxNumOfOuiFiltersPerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumOfOuiFiltersPerPort.setStatus("current")
_OuiFilterPortTable_Object = MibTable
ouiFilterPortTable = _OuiFilterPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 53, 9)
)
if mibBuilder.loadTexts:
    ouiFilterPortTable.setStatus("current")
_OuiFilterPortEntry_Object = MibTableRow
ouiFilterPortEntry = _OuiFilterPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 53, 9, 1)
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 53, 9, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 53, 9, 1, 2),
    _OuiFilterPortFilterMode_Type()
)
ouiFilterPortFilterMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ouiFilterPortFilterMode.setStatus("current")
_DhcpSnoop_ObjectIdentity = ObjectIdentity
dhcpSnoop = _DhcpSnoop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 55)
)
_DhcpSnoopPortTable_Object = MibTable
dhcpSnoopPortTable = _DhcpSnoopPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 55, 1)
)
if mibBuilder.loadTexts:
    dhcpSnoopPortTable.setStatus("current")
_DhcpSnoopPortEntry_Object = MibTableRow
dhcpSnoopPortEntry = _DhcpSnoopPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 55, 1, 1)
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 55, 1, 1, 1),
    _DhcpSnoopEnable_Type()
)
dhcpSnoopEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnoopEnable.setStatus("current")
_DhcpSnoopTarget_Type = OctetString
_DhcpSnoopTarget_Object = MibScalar
dhcpSnoopTarget = _DhcpSnoopTarget_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 55, 2),
    _DhcpSnoopTarget_Type()
)
dhcpSnoopTarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnoopTarget.setStatus("current")
_DhcpSnoopOps_Type = Integer32
_DhcpSnoopOps_Object = MibScalar
dhcpSnoopOps = _DhcpSnoopOps_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 55, 3),
    _DhcpSnoopOps_Type()
)
dhcpSnoopOps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnoopOps.setStatus("current")
_DhcpStaticTable_Object = MibTable
dhcpStaticTable = _DhcpStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 55, 4)
)
if mibBuilder.loadTexts:
    dhcpStaticTable.setStatus("current")
_DhcpStaticEntry_Object = MibTableRow
dhcpStaticEntry = _DhcpStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 55, 4, 1)
)
dhcpStaticEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZYXEL-IES1248", "dhcpStaticIpAddr"),
)
if mibBuilder.loadTexts:
    dhcpStaticEntry.setStatus("current")
_DhcpStaticIpAddr_Type = IpAddress
_DhcpStaticIpAddr_Object = MibTableColumn
dhcpStaticIpAddr = _DhcpStaticIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 55, 4, 1, 1),
    _DhcpStaticIpAddr_Type()
)
dhcpStaticIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpStaticIpAddr.setStatus("current")
_DhcpStaticRowStatus_Type = RowStatus
_DhcpStaticRowStatus_Object = MibTableColumn
dhcpStaticRowStatus = _DhcpStaticRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 55, 4, 1, 2),
    _DhcpStaticRowStatus_Type()
)
dhcpStaticRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpStaticRowStatus.setStatus("current")
_MaxNumOfDhcpStaticIp_Type = Integer32
_MaxNumOfDhcpStaticIp_Object = MibScalar
maxNumOfDhcpStaticIp = _MaxNumOfDhcpStaticIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 55, 5),
    _MaxNumOfDhcpStaticIp_Type()
)
maxNumOfDhcpStaticIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumOfDhcpStaticIp.setStatus("current")


class _DhcpSnoopLan2lanEnable_Type(Integer32):
    """Custom type dhcpSnoopLan2lanEnable based on Integer32"""
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


_DhcpSnoopLan2lanEnable_Type.__name__ = "Integer32"
_DhcpSnoopLan2lanEnable_Object = MibScalar
dhcpSnoopLan2lanEnable = _DhcpSnoopLan2lanEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 55, 6),
    _DhcpSnoopLan2lanEnable_Type()
)
dhcpSnoopLan2lanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnoopLan2lanEnable.setStatus("current")
_Acl_ObjectIdentity = ObjectIdentity
acl = _Acl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 56)
)
_AclSetTable_Object = MibTable
aclSetTable = _AclSetTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 56, 1)
)
if mibBuilder.loadTexts:
    aclSetTable.setStatus("current")
_AclSetEntry_Object = MibTableRow
aclSetEntry = _AclSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 56, 1, 1)
)
aclSetEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZYXEL-IES1248", "aclSetVpi"),
    (0, "ZYXEL-IES1248", "aclSetVci"),
    (0, "ZYXEL-IES1248", "aclSetProfileName"),
)
if mibBuilder.loadTexts:
    aclSetEntry.setStatus("current")
_AclSetVpi_Type = Integer32
_AclSetVpi_Object = MibTableColumn
aclSetVpi = _AclSetVpi_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 56, 1, 1, 1),
    _AclSetVpi_Type()
)
aclSetVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclSetVpi.setStatus("current")
_AclSetVci_Type = Integer32
_AclSetVci_Object = MibTableColumn
aclSetVci = _AclSetVci_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 56, 1, 1, 2),
    _AclSetVci_Type()
)
aclSetVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclSetVci.setStatus("current")
_AclSetProfileName_Type = DisplayString
_AclSetProfileName_Object = MibTableColumn
aclSetProfileName = _AclSetProfileName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 56, 1, 1, 3),
    _AclSetProfileName_Type()
)
aclSetProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclSetProfileName.setStatus("current")
_AclSetRowStatus_Type = RowStatus
_AclSetRowStatus_Object = MibTableColumn
aclSetRowStatus = _AclSetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 56, 1, 1, 4),
    _AclSetRowStatus_Type()
)
aclSetRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclSetRowStatus.setStatus("current")
_AclProfileTable_Object = MibTable
aclProfileTable = _AclProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 56, 2)
)
if mibBuilder.loadTexts:
    aclProfileTable.setStatus("current")
_AclProfileEntry_Object = MibTableRow
aclProfileEntry = _AclProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 56, 2, 1)
)
aclProfileEntry.setIndexNames(
    (0, "ZYXEL-IES1248", "aclProfileRuleName"),
)
if mibBuilder.loadTexts:
    aclProfileEntry.setStatus("current")
_AclProfileRuleName_Type = DisplayString
_AclProfileRuleName_Object = MibTableColumn
aclProfileRuleName = _AclProfileRuleName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 56, 2, 1, 1),
    _AclProfileRuleName_Type()
)
aclProfileRuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclProfileRuleName.setStatus("current")
_AclProfileRuleNumber_Type = Integer32
_AclProfileRuleNumber_Object = MibTableColumn
aclProfileRuleNumber = _AclProfileRuleNumber_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 56, 2, 1, 2),
    _AclProfileRuleNumber_Type()
)
aclProfileRuleNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileRuleNumber.setStatus("current")
_AclProfileActionNumber_Type = Integer32
_AclProfileActionNumber_Object = MibTableColumn
aclProfileActionNumber = _AclProfileActionNumber_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 56, 2, 1, 3),
    _AclProfileActionNumber_Type()
)
aclProfileActionNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileActionNumber.setStatus("current")
_AclProfileRuleParamMask_Type = Integer32
_AclProfileRuleParamMask_Object = MibTableColumn
aclProfileRuleParamMask = _AclProfileRuleParamMask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 56, 2, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 56, 2, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 56, 2, 1, 6),
    _AclProfileRuleVid_Type()
)
aclProfileRuleVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileRuleVid.setStatus("current")
_AclProfileRuleSmac_Type = PhysAddress
_AclProfileRuleSmac_Object = MibTableColumn
aclProfileRuleSmac = _AclProfileRuleSmac_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 56, 2, 1, 7),
    _AclProfileRuleSmac_Type()
)
aclProfileRuleSmac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileRuleSmac.setStatus("current")
_AclProfileRuleDmac_Type = PhysAddress
_AclProfileRuleDmac_Object = MibTableColumn
aclProfileRuleDmac = _AclProfileRuleDmac_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 56, 2, 1, 8),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 56, 2, 1, 9),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 56, 2, 1, 10),
    _AclProfileRuleProtocol_Type()
)
aclProfileRuleProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileRuleProtocol.setStatus("current")
_AclProfileRuleSrcIP_Type = IpAddress
_AclProfileRuleSrcIP_Object = MibTableColumn
aclProfileRuleSrcIP = _AclProfileRuleSrcIP_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 56, 2, 1, 11),
    _AclProfileRuleSrcIP_Type()
)
aclProfileRuleSrcIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileRuleSrcIP.setStatus("current")


class _AclProfileRuleSrcIPMask_Type(Integer32):
    """Custom type aclProfileRuleSrcIPMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_AclProfileRuleSrcIPMask_Type.__name__ = "Integer32"
_AclProfileRuleSrcIPMask_Object = MibTableColumn
aclProfileRuleSrcIPMask = _AclProfileRuleSrcIPMask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 56, 2, 1, 12),
    _AclProfileRuleSrcIPMask_Type()
)
aclProfileRuleSrcIPMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileRuleSrcIPMask.setStatus("current")
_AclProfileRuleDestIP_Type = IpAddress
_AclProfileRuleDestIP_Object = MibTableColumn
aclProfileRuleDestIP = _AclProfileRuleDestIP_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 56, 2, 1, 13),
    _AclProfileRuleDestIP_Type()
)
aclProfileRuleDestIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileRuleDestIP.setStatus("current")


class _AclProfileRuleDestIPMask_Type(Integer32):
    """Custom type aclProfileRuleDestIPMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_AclProfileRuleDestIPMask_Type.__name__ = "Integer32"
_AclProfileRuleDestIPMask_Object = MibTableColumn
aclProfileRuleDestIPMask = _AclProfileRuleDestIPMask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 56, 2, 1, 14),
    _AclProfileRuleDestIPMask_Type()
)
aclProfileRuleDestIPMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileRuleDestIPMask.setStatus("current")


class _AclProfileRuleStartTos_Type(Integer32):
    """Custom type aclProfileRuleStartTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AclProfileRuleStartTos_Type.__name__ = "Integer32"
_AclProfileRuleStartTos_Object = MibTableColumn
aclProfileRuleStartTos = _AclProfileRuleStartTos_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 56, 2, 1, 15),
    _AclProfileRuleStartTos_Type()
)
aclProfileRuleStartTos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileRuleStartTos.setStatus("current")


class _AclProfileRuleEndTos_Type(Integer32):
    """Custom type aclProfileRuleEndTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AclProfileRuleEndTos_Type.__name__ = "Integer32"
_AclProfileRuleEndTos_Object = MibTableColumn
aclProfileRuleEndTos = _AclProfileRuleEndTos_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 56, 2, 1, 16),
    _AclProfileRuleEndTos_Type()
)
aclProfileRuleEndTos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileRuleEndTos.setStatus("current")


class _AclProfileRuleSrcStartPort_Type(Integer32):
    """Custom type aclProfileRuleSrcStartPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AclProfileRuleSrcStartPort_Type.__name__ = "Integer32"
_AclProfileRuleSrcStartPort_Object = MibTableColumn
aclProfileRuleSrcStartPort = _AclProfileRuleSrcStartPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 56, 2, 1, 17),
    _AclProfileRuleSrcStartPort_Type()
)
aclProfileRuleSrcStartPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileRuleSrcStartPort.setStatus("current")


class _AclProfileRuleSrcEndPort_Type(Integer32):
    """Custom type aclProfileRuleSrcEndPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AclProfileRuleSrcEndPort_Type.__name__ = "Integer32"
_AclProfileRuleSrcEndPort_Object = MibTableColumn
aclProfileRuleSrcEndPort = _AclProfileRuleSrcEndPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 56, 2, 1, 18),
    _AclProfileRuleSrcEndPort_Type()
)
aclProfileRuleSrcEndPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileRuleSrcEndPort.setStatus("current")


class _AclProfileRuleDestStartPort_Type(Integer32):
    """Custom type aclProfileRuleDestStartPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AclProfileRuleDestStartPort_Type.__name__ = "Integer32"
_AclProfileRuleDestStartPort_Object = MibTableColumn
aclProfileRuleDestStartPort = _AclProfileRuleDestStartPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 56, 2, 1, 19),
    _AclProfileRuleDestStartPort_Type()
)
aclProfileRuleDestStartPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileRuleDestStartPort.setStatus("current")


class _AclProfileRuleDestEndPort_Type(Integer32):
    """Custom type aclProfileRuleDestEndPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AclProfileRuleDestEndPort_Type.__name__ = "Integer32"
_AclProfileRuleDestEndPort_Object = MibTableColumn
aclProfileRuleDestEndPort = _AclProfileRuleDestEndPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 56, 2, 1, 20),
    _AclProfileRuleDestEndPort_Type()
)
aclProfileRuleDestEndPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileRuleDestEndPort.setStatus("current")


class _AclProfileActionRate_Type(Integer32):
    """Custom type aclProfileActionRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AclProfileActionRate_Type.__name__ = "Integer32"
_AclProfileActionRate_Object = MibTableColumn
aclProfileActionRate = _AclProfileActionRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 56, 2, 1, 21),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 56, 2, 1, 22),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 56, 2, 1, 23),
    _AclProfileActionrpri_Type()
)
aclProfileActionrpri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileActionrpri.setStatus("current")
_AclProfileRowStatus_Type = RowStatus
_AclProfileRowStatus_Object = MibTableColumn
aclProfileRowStatus = _AclProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 56, 2, 1, 24),
    _AclProfileRowStatus_Type()
)
aclProfileRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileRowStatus.setStatus("current")
_PppoeAgent_ObjectIdentity = ObjectIdentity
pppoeAgent = _PppoeAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 57)
)
_PppoeAgentTable_Object = MibTable
pppoeAgentTable = _PppoeAgentTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 57, 1)
)
if mibBuilder.loadTexts:
    pppoeAgentTable.setStatus("current")
_PppoeAgentEntry_Object = MibTableRow
pppoeAgentEntry = _PppoeAgentEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 57, 1, 1)
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 57, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 57, 1, 1, 2),
    _PppoeAgentInfo_Type()
)
pppoeAgentInfo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pppoeAgentInfo.setStatus("current")
_PppoeAgentRowStatus_Type = RowStatus
_PppoeAgentRowStatus_Object = MibTableColumn
pppoeAgentRowStatus = _PppoeAgentRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 57, 1, 1, 3),
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
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("private", 1),
          ("tr101", 2),
          ("tr101WithVlan", 3))
    )


_PppoeAgentOptionMode_Type.__name__ = "Integer32"
_PppoeAgentOptionMode_Object = MibTableColumn
pppoeAgentOptionMode = _PppoeAgentOptionMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 57, 1, 1, 4),
    _PppoeAgentOptionMode_Type()
)
pppoeAgentOptionMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pppoeAgentOptionMode.setStatus("current")
_MaxNumOfPppoeAgentConf_Type = Integer32
_MaxNumOfPppoeAgentConf_Object = MibScalar
maxNumOfPppoeAgentConf = _MaxNumOfPppoeAgentConf_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 57, 2),
    _MaxNumOfPppoeAgentConf_Type()
)
maxNumOfPppoeAgentConf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumOfPppoeAgentConf.setStatus("current")
_Fdb_ObjectIdentity = ObjectIdentity
fdb = _Fdb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 58)
)


class _FdbAntiSpoofing_Type(Integer32):
    """Custom type fdbAntiSpoofing based on Integer32"""
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


_FdbAntiSpoofing_Type.__name__ = "Integer32"
_FdbAntiSpoofing_Object = MibScalar
fdbAntiSpoofing = _FdbAntiSpoofing_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 58, 1),
    _FdbAntiSpoofing_Type()
)
fdbAntiSpoofing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fdbAntiSpoofing.setStatus("current")


class _FdbPolicy_Type(Integer32):
    """Custom type fdbPolicy based on Integer32"""
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


_FdbPolicy_Type.__name__ = "Integer32"
_FdbPolicy_Object = MibScalar
fdbPolicy = _FdbPolicy_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 58, 2),
    _FdbPolicy_Type()
)
fdbPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fdbPolicy.setStatus("current")
_Loopguard_ObjectIdentity = ObjectIdentity
loopguard = _Loopguard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 60)
)
_LoopguardPortTable_Object = MibTable
loopguardPortTable = _LoopguardPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 60, 1)
)
if mibBuilder.loadTexts:
    loopguardPortTable.setStatus("current")
_LoopguardPortEntry_Object = MibTableRow
loopguardPortEntry = _LoopguardPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 60, 1, 1)
)
loopguardPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    loopguardPortEntry.setStatus("current")


class _LoopguardPortEnable_Type(Integer32):
    """Custom type loopguardPortEnable based on Integer32"""
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


_LoopguardPortEnable_Type.__name__ = "Integer32"
_LoopguardPortEnable_Object = MibTableColumn
loopguardPortEnable = _LoopguardPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 60, 1, 1, 1),
    _LoopguardPortEnable_Type()
)
loopguardPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loopguardPortEnable.setStatus("current")


class _LoopguardPortMode_Type(Integer32):
    """Custom type loopguardPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fix", 1),
          ("dynamic", 2))
    )


_LoopguardPortMode_Type.__name__ = "Integer32"
_LoopguardPortMode_Object = MibTableColumn
loopguardPortMode = _LoopguardPortMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 60, 1, 1, 2),
    _LoopguardPortMode_Type()
)
loopguardPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loopguardPortMode.setStatus("current")


class _LoopguardPortRecoverTime_Type(Integer32):
    """Custom type loopguardPortRecoverTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 600),
    )


_LoopguardPortRecoverTime_Type.__name__ = "Integer32"
_LoopguardPortRecoverTime_Object = MibTableColumn
loopguardPortRecoverTime = _LoopguardPortRecoverTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 10, 60, 1, 1, 3),
    _LoopguardPortRecoverTime_Type()
)
loopguardPortRecoverTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loopguardPortRecoverTime.setStatus("current")
if mibBuilder.loadTexts:
    loopguardPortRecoverTime.setUnits("seconds")
_Sys_ObjectIdentity = ObjectIdentity
sys = _Sys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 11)
)
_TimeSetup_ObjectIdentity = ObjectIdentity
timeSetup = _TimeSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 11, 4)
)
_DayLightSaving_ObjectIdentity = ObjectIdentity
dayLightSaving = _DayLightSaving_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 11, 4, 7)
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 11, 4, 7, 1),
    _DayLightSavingAdminStatus_Type()
)
dayLightSavingAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dayLightSavingAdminStatus.setStatus("current")
_DayLightSavingStartTime_ObjectIdentity = ObjectIdentity
dayLightSavingStartTime = _DayLightSavingStartTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 11, 4, 7, 2)
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
        *(("jan", 1),
          ("feb", 2),
          ("mar", 3),
          ("apr", 4),
          ("may", 5),
          ("jun", 6),
          ("jul", 7),
          ("aug", 8),
          ("sep", 9),
          ("oct", 10),
          ("nov", 11),
          ("dec", 12))
    )


_DayLightSavingStartMonth_Type.__name__ = "Integer32"
_DayLightSavingStartMonth_Object = MibScalar
dayLightSavingStartMonth = _DayLightSavingStartMonth_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 11, 4, 7, 2, 1),
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
        *(("first", 1),
          ("second", 2),
          ("third", 3),
          ("fourth", 4),
          ("last", 5))
    )


_DayLightSavingStartWeek_Type.__name__ = "Integer32"
_DayLightSavingStartWeek_Object = MibScalar
dayLightSavingStartWeek = _DayLightSavingStartWeek_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 11, 4, 7, 2, 2),
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
        *(("sun", 1),
          ("mon", 2),
          ("tus", 3),
          ("wed", 4),
          ("thu", 5),
          ("fri", 6),
          ("sat", 7))
    )


_DayLightSavingStartWday_Type.__name__ = "Integer32"
_DayLightSavingStartWday_Object = MibScalar
dayLightSavingStartWday = _DayLightSavingStartWday_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 11, 4, 7, 2, 3),
    _DayLightSavingStartWday_Type()
)
dayLightSavingStartWday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dayLightSavingStartWday.setStatus("current")


class _DayLightSavingStartHour_Type(Integer32):
    """Custom type dayLightSavingStartHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_DayLightSavingStartHour_Type.__name__ = "Integer32"
_DayLightSavingStartHour_Object = MibScalar
dayLightSavingStartHour = _DayLightSavingStartHour_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 11, 4, 7, 2, 4),
    _DayLightSavingStartHour_Type()
)
dayLightSavingStartHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dayLightSavingStartHour.setStatus("current")
_DayLightSavingEndTime_ObjectIdentity = ObjectIdentity
dayLightSavingEndTime = _DayLightSavingEndTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 11, 4, 7, 3)
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
        *(("jan", 1),
          ("feb", 2),
          ("mar", 3),
          ("apr", 4),
          ("may", 5),
          ("jun", 6),
          ("jul", 7),
          ("aug", 8),
          ("sep", 9),
          ("oct", 10),
          ("nov", 11),
          ("dec", 12))
    )


_DayLightSavingEndMonth_Type.__name__ = "Integer32"
_DayLightSavingEndMonth_Object = MibScalar
dayLightSavingEndMonth = _DayLightSavingEndMonth_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 11, 4, 7, 3, 1),
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
        *(("first", 1),
          ("second", 2),
          ("third", 3),
          ("fourth", 4),
          ("last", 5))
    )


_DayLightSavingEndWeek_Type.__name__ = "Integer32"
_DayLightSavingEndWeek_Object = MibScalar
dayLightSavingEndWeek = _DayLightSavingEndWeek_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 11, 4, 7, 3, 2),
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
        *(("sun", 1),
          ("mon", 2),
          ("tus", 3),
          ("wed", 4),
          ("thu", 5),
          ("fri", 6),
          ("sat", 7))
    )


_DayLightSavingEndWday_Type.__name__ = "Integer32"
_DayLightSavingEndWday_Object = MibScalar
dayLightSavingEndWday = _DayLightSavingEndWday_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 11, 4, 7, 3, 3),
    _DayLightSavingEndWday_Type()
)
dayLightSavingEndWday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dayLightSavingEndWday.setStatus("current")


class _DayLightSavingEndHour_Type(Integer32):
    """Custom type dayLightSavingEndHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_DayLightSavingEndHour_Type.__name__ = "Integer32"
_DayLightSavingEndHour_Object = MibScalar
dayLightSavingEndHour = _DayLightSavingEndHour_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 11, 4, 7, 3, 4),
    _DayLightSavingEndHour_Type()
)
dayLightSavingEndHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dayLightSavingEndHour.setStatus("current")
_AccessCtrl_ObjectIdentity = ObjectIdentity
accessCtrl = _AccessCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 11, 5)
)
_SecuredClientTable_Object = MibTable
securedClientTable = _SecuredClientTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 11, 5, 2)
)
if mibBuilder.loadTexts:
    securedClientTable.setStatus("current")
_SecuredClientEntry_Object = MibTableRow
securedClientEntry = _SecuredClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 11, 5, 2, 1)
)
securedClientEntry.setIndexNames(
    (0, "ZYXEL-IES1248", "securedClientIndex"),
)
if mibBuilder.loadTexts:
    securedClientEntry.setStatus("current")
_SecuredClientIndex_Type = Integer32
_SecuredClientIndex_Object = MibTableColumn
securedClientIndex = _SecuredClientIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 11, 5, 2, 1, 1),
    _SecuredClientIndex_Type()
)
securedClientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securedClientIndex.setStatus("current")
_SecuredClientStartIp_Type = IpAddress
_SecuredClientStartIp_Object = MibTableColumn
securedClientStartIp = _SecuredClientStartIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 11, 5, 2, 1, 2),
    _SecuredClientStartIp_Type()
)
securedClientStartIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securedClientStartIp.setStatus("current")
_SecuredClientEndIp_Type = IpAddress
_SecuredClientEndIp_Object = MibTableColumn
securedClientEndIp = _SecuredClientEndIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 11, 5, 2, 1, 3),
    _SecuredClientEndIp_Type()
)
securedClientEndIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securedClientEndIp.setStatus("current")
_SecuredClientService_Type = Integer32
_SecuredClientService_Object = MibTableColumn
securedClientService = _SecuredClientService_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 11, 5, 2, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 11, 5, 2, 1, 5),
    _SecuredClientEnable_Type()
)
securedClientEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securedClientEnable.setStatus("current")
_ExtAlarm_ObjectIdentity = ObjectIdentity
extAlarm = _ExtAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 11, 8)
)
_ExtAlarmTable_Object = MibTable
extAlarmTable = _ExtAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 11, 8, 1)
)
if mibBuilder.loadTexts:
    extAlarmTable.setStatus("current")
_ExtAlarmEntry_Object = MibTableRow
extAlarmEntry = _ExtAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 11, 8, 1, 1)
)
extAlarmEntry.setIndexNames(
    (0, "ZYXEL-IES1248", "extAlarmIndex"),
)
if mibBuilder.loadTexts:
    extAlarmEntry.setStatus("current")
_ExtAlarmIndex_Type = Integer32
_ExtAlarmIndex_Object = MibTableColumn
extAlarmIndex = _ExtAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 11, 8, 1, 1, 1),
    _ExtAlarmIndex_Type()
)
extAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extAlarmIndex.setStatus("current")


class _ExtAlarmname_Type(DisplayString):
    """Custom type extAlarmname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_ExtAlarmname_Type.__name__ = "DisplayString"
_ExtAlarmname_Object = MibTableColumn
extAlarmname = _ExtAlarmname_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 11, 8, 1, 1, 2),
    _ExtAlarmname_Type()
)
extAlarmname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extAlarmname.setStatus("current")


class _ExtAlarmstatus_Type(DisplayString):
    """Custom type extAlarmstatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_ExtAlarmstatus_Type.__name__ = "DisplayString"
_ExtAlarmstatus_Object = MibTableColumn
extAlarmstatus = _ExtAlarmstatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 11, 8, 1, 1, 3),
    _ExtAlarmstatus_Type()
)
extAlarmstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extAlarmstatus.setStatus("current")
_User_ObjectIdentity = ObjectIdentity
user = _User_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 11, 9)
)


class _UserAuthMode_Type(Integer32):
    """Custom type userAuthMode based on Integer32"""
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
        *(("local", 1),
          ("radius", 2),
          ("localThenRadius", 3),
          ("tacacsplus", 4),
          ("localThenTacacsplus", 5),
          ("radiusThenLocal", 6),
          ("tacacsplusThenLocal", 7))
    )


_UserAuthMode_Type.__name__ = "Integer32"
_UserAuthMode_Object = MibScalar
userAuthMode = _UserAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 11, 9, 1),
    _UserAuthMode_Type()
)
userAuthMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userAuthMode.setStatus("current")
_UserAuthServerIp_Type = IpAddress
_UserAuthServerIp_Object = MibScalar
userAuthServerIp = _UserAuthServerIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 11, 9, 2),
    _UserAuthServerIp_Type()
)
userAuthServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userAuthServerIp.setStatus("current")
_UserAuthServerPort_Type = Integer32
_UserAuthServerPort_Object = MibScalar
userAuthServerPort = _UserAuthServerPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 11, 9, 3),
    _UserAuthServerPort_Type()
)
userAuthServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userAuthServerPort.setStatus("current")
_UserAuthServerSecret_Type = OctetString
_UserAuthServerSecret_Object = MibScalar
userAuthServerSecret = _UserAuthServerSecret_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 11, 9, 4),
    _UserAuthServerSecret_Type()
)
userAuthServerSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userAuthServerSecret.setStatus("current")
_UserTable_Object = MibTable
userTable = _UserTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 11, 9, 5)
)
if mibBuilder.loadTexts:
    userTable.setStatus("current")
_UserEntry_Object = MibTableRow
userEntry = _UserEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 11, 9, 5, 1)
)
userEntry.setIndexNames(
    (0, "ZYXEL-IES1248", "userName"),
)
if mibBuilder.loadTexts:
    userEntry.setStatus("current")
_UserName_Type = DisplayString
_UserName_Object = MibTableColumn
userName = _UserName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 11, 9, 5, 1, 1),
    _UserName_Type()
)
userName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userName.setStatus("current")
_UserPassword_Type = DisplayString
_UserPassword_Object = MibTableColumn
userPassword = _UserPassword_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 11, 9, 5, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 11, 9, 5, 1, 3),
    _UserPriviledge_Type()
)
userPriviledge.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    userPriviledge.setStatus("current")
_UserRowStatus_Type = RowStatus
_UserRowStatus_Object = MibTableColumn
userRowStatus = _UserRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 11, 9, 5, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 11, 9, 6),
    _UserAuthDefaultPriviledge_Type()
)
userAuthDefaultPriviledge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userAuthDefaultPriviledge.setStatus("current")
_SysSlotId_Type = Integer32
_SysSlotId_Object = MibScalar
sysSlotId = _SysSlotId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 11, 10),
    _SysSlotId_Type()
)
sysSlotId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSlotId.setStatus("current")
_Trap_ObjectIdentity = ObjectIdentity
trap = _Trap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 12)
)
_Object_ObjectIdentity = ObjectIdentity
object = _Object_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 12, 1)
)
_EqptAlarmInputIndex_Type = Integer32
_EqptAlarmInputIndex_Object = MibScalar
eqptAlarmInputIndex = _EqptAlarmInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 12, 1, 2),
    _EqptAlarmInputIndex_Type()
)
eqptAlarmInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqptAlarmInputIndex.setStatus("current")
_EqptAlarmInputName_Type = DisplayString
_EqptAlarmInputName_Object = MibScalar
eqptAlarmInputName = _EqptAlarmInputName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 12, 1, 8),
    _EqptAlarmInputName_Type()
)
eqptAlarmInputName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqptAlarmInputName.setStatus("current")
_SysMacAntiSpoofOrig_Type = Integer32
_SysMacAntiSpoofOrig_Object = MibScalar
sysMacAntiSpoofOrig = _SysMacAntiSpoofOrig_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 12, 1, 9),
    _SysMacAntiSpoofOrig_Type()
)
sysMacAntiSpoofOrig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMacAntiSpoofOrig.setStatus("current")
_SysMacAntiSpoofNew_Type = Integer32
_SysMacAntiSpoofNew_Object = MibScalar
sysMacAntiSpoofNew = _SysMacAntiSpoofNew_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 12, 1, 10),
    _SysMacAntiSpoofNew_Type()
)
sysMacAntiSpoofNew.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMacAntiSpoofNew.setStatus("current")
_SysMacAntiSpoofMAC_Type = DisplayString
_SysMacAntiSpoofMAC_Object = MibScalar
sysMacAntiSpoofMAC = _SysMacAntiSpoofMAC_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 12, 1, 11),
    _SysMacAntiSpoofMAC_Type()
)
sysMacAntiSpoofMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMacAntiSpoofMAC.setStatus("current")
_SysUser_Type = DisplayString
_SysUser_Object = MibScalar
sysUser = _SysUser_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 12, 1, 12),
    _SysUser_Type()
)
sysUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysUser.setStatus("current")


class _SysAccessPoint_Type(Integer32):
    """Custom type sysAccessPoint based on Integer32"""
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
        *(("console", 1),
          ("telnet", 2),
          ("ssh", 3),
          ("web", 4),
          ("ftp", 5))
    )


_SysAccessPoint_Type.__name__ = "Integer32"
_SysAccessPoint_Object = MibScalar
sysAccessPoint = _SysAccessPoint_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 12, 1, 13),
    _SysAccessPoint_Type()
)
sysAccessPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysAccessPoint.setStatus("current")
_LgReceiverIfIndex_Type = Integer32
_LgReceiverIfIndex_Object = MibScalar
lgReceiverIfIndex = _LgReceiverIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 12, 1, 14),
    _LgReceiverIfIndex_Type()
)
lgReceiverIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgReceiverIfIndex.setStatus("current")
_LgSenderIfIndex_Type = Integer32
_LgSenderIfIndex_Object = MibScalar
lgSenderIfIndex = _LgSenderIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 12, 1, 15),
    _LgSenderIfIndex_Type()
)
lgSenderIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgSenderIfIndex.setStatus("current")
_Equipment_ObjectIdentity = ObjectIdentity
equipment = _Equipment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 12, 3)
)
_Systrap_ObjectIdentity = ObjectIdentity
systrap = _Systrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 12, 4)
)
_Dsltrap_ObjectIdentity = ObjectIdentity
dsltrap = _Dsltrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 12, 5)
)
_Enettrap_ObjectIdentity = ObjectIdentity
enettrap = _Enettrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 12, 6)
)
_Statistics_ObjectIdentity = ObjectIdentity
statistics = _Statistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13)
)
_IgmpQueryCntTotal_Type = Counter32
_IgmpQueryCntTotal_Object = MibScalar
igmpQueryCntTotal = _IgmpQueryCntTotal_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 1),
    _IgmpQueryCntTotal_Type()
)
igmpQueryCntTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpQueryCntTotal.setStatus("current")
_IgmpReportCntTotal_Type = Counter32
_IgmpReportCntTotal_Object = MibScalar
igmpReportCntTotal = _IgmpReportCntTotal_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 2),
    _IgmpReportCntTotal_Type()
)
igmpReportCntTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpReportCntTotal.setStatus("current")
_IgmpLeaveCntTotal_Type = Counter32
_IgmpLeaveCntTotal_Object = MibScalar
igmpLeaveCntTotal = _IgmpLeaveCntTotal_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 3),
    _IgmpLeaveCntTotal_Type()
)
igmpLeaveCntTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpLeaveCntTotal.setStatus("current")
_IgmpNumOfActiveGroups_Type = Integer32
_IgmpNumOfActiveGroups_Object = MibScalar
igmpNumOfActiveGroups = _IgmpNumOfActiveGroups_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 4),
    _IgmpNumOfActiveGroups_Type()
)
igmpNumOfActiveGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpNumOfActiveGroups.setStatus("current")
_IgmpGroupTable_Object = MibTable
igmpGroupTable = _IgmpGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 5)
)
if mibBuilder.loadTexts:
    igmpGroupTable.setStatus("current")
_IgmpGroupEntry_Object = MibTableRow
igmpGroupEntry = _IgmpGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 5, 1)
)
igmpGroupEntry.setIndexNames(
    (0, "ZYXEL-IES1248", "igmpGroupIp"),
)
if mibBuilder.loadTexts:
    igmpGroupEntry.setStatus("current")
_IgmpGroupIp_Type = IpAddress
_IgmpGroupIp_Object = MibTableColumn
igmpGroupIp = _IgmpGroupIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 5, 1, 1),
    _IgmpGroupIp_Type()
)
igmpGroupIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpGroupIp.setStatus("current")
_IgmpGroupvid_Type = Integer32
_IgmpGroupvid_Object = MibTableColumn
igmpGroupvid = _IgmpGroupvid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 5, 1, 2),
    _IgmpGroupvid_Type()
)
igmpGroupvid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpGroupvid.setStatus("current")
_IgmpGroupnumberOfMembers_Type = Integer32
_IgmpGroupnumberOfMembers_Object = MibTableColumn
igmpGroupnumberOfMembers = _IgmpGroupnumberOfMembers_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 5, 1, 3),
    _IgmpGroupnumberOfMembers_Type()
)
igmpGroupnumberOfMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpGroupnumberOfMembers.setStatus("current")
_IgmpGroupMemberPorts_Type = PortList
_IgmpGroupMemberPorts_Object = MibTableColumn
igmpGroupMemberPorts = _IgmpGroupMemberPorts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 5, 1, 4),
    _IgmpGroupMemberPorts_Type()
)
igmpGroupMemberPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpGroupMemberPorts.setStatus("current")
_IgmpGroupPortTable_Object = MibTable
igmpGroupPortTable = _IgmpGroupPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 6)
)
if mibBuilder.loadTexts:
    igmpGroupPortTable.setStatus("current")
_IgmpGroupPortEntry_Object = MibTableRow
igmpGroupPortEntry = _IgmpGroupPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 6, 1)
)
igmpGroupPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZYXEL-IES1248", "igmpGroupPortIp"),
    (0, "ZYXEL-IES1248", "igmpGroupPortvid"),
)
if mibBuilder.loadTexts:
    igmpGroupPortEntry.setStatus("current")
_IgmpGroupPortIp_Type = IpAddress
_IgmpGroupPortIp_Object = MibTableColumn
igmpGroupPortIp = _IgmpGroupPortIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 6, 1, 1),
    _IgmpGroupPortIp_Type()
)
igmpGroupPortIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpGroupPortIp.setStatus("current")
_IgmpGroupPortvid_Type = Integer32
_IgmpGroupPortvid_Object = MibTableColumn
igmpGroupPortvid = _IgmpGroupPortvid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 6, 1, 2),
    _IgmpGroupPortvid_Type()
)
igmpGroupPortvid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpGroupPortvid.setStatus("current")
_IgmpGroupV2Table_Object = MibTable
igmpGroupV2Table = _IgmpGroupV2Table_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 7)
)
if mibBuilder.loadTexts:
    igmpGroupV2Table.setStatus("current")
_IgmpGroupV2Entry_Object = MibTableRow
igmpGroupV2Entry = _IgmpGroupV2Entry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 7, 1)
)
igmpGroupV2Entry.setIndexNames(
    (0, "ZYXEL-IES1248", "igmpGroupV2Vid"),
    (0, "ZYXEL-IES1248", "igmpGroupV2Ip"),
)
if mibBuilder.loadTexts:
    igmpGroupV2Entry.setStatus("current")
_IgmpGroupV2Vid_Type = VlanIndex
_IgmpGroupV2Vid_Object = MibTableColumn
igmpGroupV2Vid = _IgmpGroupV2Vid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 7, 1, 1),
    _IgmpGroupV2Vid_Type()
)
igmpGroupV2Vid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpGroupV2Vid.setStatus("current")
_IgmpGroupV2Ip_Type = IpAddress
_IgmpGroupV2Ip_Object = MibTableColumn
igmpGroupV2Ip = _IgmpGroupV2Ip_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 7, 1, 2),
    _IgmpGroupV2Ip_Type()
)
igmpGroupV2Ip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpGroupV2Ip.setStatus("current")
_IgmpGroupV2NumOfMembers_Type = Integer32
_IgmpGroupV2NumOfMembers_Object = MibTableColumn
igmpGroupV2NumOfMembers = _IgmpGroupV2NumOfMembers_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 7, 1, 3),
    _IgmpGroupV2NumOfMembers_Type()
)
igmpGroupV2NumOfMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpGroupV2NumOfMembers.setStatus("current")
_IgmpGroupV2MemberPorts_Type = PortList
_IgmpGroupV2MemberPorts_Object = MibTableColumn
igmpGroupV2MemberPorts = _IgmpGroupV2MemberPorts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 7, 1, 4),
    _IgmpGroupV2MemberPorts_Type()
)
igmpGroupV2MemberPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpGroupV2MemberPorts.setStatus("current")
_IgmpGroupPortV2Table_Object = MibTable
igmpGroupPortV2Table = _IgmpGroupPortV2Table_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 8)
)
if mibBuilder.loadTexts:
    igmpGroupPortV2Table.setStatus("current")
_IgmpGroupPortV2Entry_Object = MibTableRow
igmpGroupPortV2Entry = _IgmpGroupPortV2Entry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 8, 1)
)
igmpGroupPortV2Entry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZYXEL-IES1248", "igmpGroupPortV2Vid"),
    (0, "ZYXEL-IES1248", "igmpGroupPortV2Ip"),
    (0, "ZYXEL-IES1248", "igmpGroupPortV2SourceIp"),
)
if mibBuilder.loadTexts:
    igmpGroupPortV2Entry.setStatus("current")
_IgmpGroupPortV2Vid_Type = VlanIndex
_IgmpGroupPortV2Vid_Object = MibTableColumn
igmpGroupPortV2Vid = _IgmpGroupPortV2Vid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 8, 1, 1),
    _IgmpGroupPortV2Vid_Type()
)
igmpGroupPortV2Vid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpGroupPortV2Vid.setStatus("current")
_IgmpGroupPortV2Ip_Type = IpAddress
_IgmpGroupPortV2Ip_Object = MibTableColumn
igmpGroupPortV2Ip = _IgmpGroupPortV2Ip_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 8, 1, 2),
    _IgmpGroupPortV2Ip_Type()
)
igmpGroupPortV2Ip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpGroupPortV2Ip.setStatus("current")
_IgmpGroupPortV2SourceIp_Type = IpAddress
_IgmpGroupPortV2SourceIp_Object = MibTableColumn
igmpGroupPortV2SourceIp = _IgmpGroupPortV2SourceIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 8, 1, 3),
    _IgmpGroupPortV2SourceIp_Type()
)
igmpGroupPortV2SourceIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpGroupPortV2SourceIp.setStatus("current")
_IgmpPortCtrlPduTable_Object = MibTable
igmpPortCtrlPduTable = _IgmpPortCtrlPduTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 9)
)
if mibBuilder.loadTexts:
    igmpPortCtrlPduTable.setStatus("current")
_IgmpPortCtrlPduEntry_Object = MibTableRow
igmpPortCtrlPduEntry = _IgmpPortCtrlPduEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 9, 1)
)
igmpPortCtrlPduEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    igmpPortCtrlPduEntry.setStatus("current")
_IgmpPortCtrlPduQueryCnt_Type = Counter32
_IgmpPortCtrlPduQueryCnt_Object = MibTableColumn
igmpPortCtrlPduQueryCnt = _IgmpPortCtrlPduQueryCnt_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 9, 1, 1),
    _IgmpPortCtrlPduQueryCnt_Type()
)
igmpPortCtrlPduQueryCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpPortCtrlPduQueryCnt.setStatus("current")
_IgmpPortCtrlPduReportCnt_Type = Counter32
_IgmpPortCtrlPduReportCnt_Object = MibTableColumn
igmpPortCtrlPduReportCnt = _IgmpPortCtrlPduReportCnt_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 9, 1, 2),
    _IgmpPortCtrlPduReportCnt_Type()
)
igmpPortCtrlPduReportCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpPortCtrlPduReportCnt.setStatus("current")
_IgmpPortCtrlPduLeaveCnt_Type = Counter32
_IgmpPortCtrlPduLeaveCnt_Object = MibTableColumn
igmpPortCtrlPduLeaveCnt = _IgmpPortCtrlPduLeaveCnt_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 9, 1, 3),
    _IgmpPortCtrlPduLeaveCnt_Type()
)
igmpPortCtrlPduLeaveCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpPortCtrlPduLeaveCnt.setStatus("current")
_IgmpPortNumOfActiveGroups_Type = Integer32
_IgmpPortNumOfActiveGroups_Object = MibTableColumn
igmpPortNumOfActiveGroups = _IgmpPortNumOfActiveGroups_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 9, 1, 4),
    _IgmpPortNumOfActiveGroups_Type()
)
igmpPortNumOfActiveGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpPortNumOfActiveGroups.setStatus("current")
_DhcpStats_ObjectIdentity = ObjectIdentity
dhcpStats = _DhcpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 11)
)
_DhcpSnoopIpTable_Object = MibTable
dhcpSnoopIpTable = _DhcpSnoopIpTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 11, 1)
)
if mibBuilder.loadTexts:
    dhcpSnoopIpTable.setStatus("current")
_DhcpSnoopIpEntry_Object = MibTableRow
dhcpSnoopIpEntry = _DhcpSnoopIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 11, 1, 1)
)
dhcpSnoopIpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZYXEL-IES1248", "dhcpSnoopIp"),
)
if mibBuilder.loadTexts:
    dhcpSnoopIpEntry.setStatus("current")
_DhcpSnoopIp_Type = IpAddress
_DhcpSnoopIp_Object = MibTableColumn
dhcpSnoopIp = _DhcpSnoopIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 11, 1, 1, 1),
    _DhcpSnoopIp_Type()
)
dhcpSnoopIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnoopIp.setStatus("current")
_DhcpSnoopMac_Type = PhysAddress
_DhcpSnoopMac_Object = MibTableColumn
dhcpSnoopMac = _DhcpSnoopMac_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 11, 1, 1, 2),
    _DhcpSnoopMac_Type()
)
dhcpSnoopMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnoopMac.setStatus("current")
_DhcpSnoopVid_Type = VlanIndex
_DhcpSnoopVid_Object = MibTableColumn
dhcpSnoopVid = _DhcpSnoopVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 11, 1, 1, 3),
    _DhcpSnoopVid_Type()
)
dhcpSnoopVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnoopVid.setStatus("current")
_DhcpSnoopCounterTable_Object = MibTable
dhcpSnoopCounterTable = _DhcpSnoopCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 11, 2)
)
if mibBuilder.loadTexts:
    dhcpSnoopCounterTable.setStatus("current")
_DhcpSnoopCounterEntry_Object = MibTableRow
dhcpSnoopCounterEntry = _DhcpSnoopCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 11, 2, 1)
)
dhcpSnoopCounterEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dhcpSnoopCounterEntry.setStatus("current")
_DhcpDiscovery_Type = Counter64
_DhcpDiscovery_Object = MibTableColumn
dhcpDiscovery = _DhcpDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 11, 2, 1, 1),
    _DhcpDiscovery_Type()
)
dhcpDiscovery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpDiscovery.setStatus("current")
_DhcpOffer_Type = Counter64
_DhcpOffer_Object = MibTableColumn
dhcpOffer = _DhcpOffer_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 11, 2, 1, 2),
    _DhcpOffer_Type()
)
dhcpOffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpOffer.setStatus("current")
_DhcpRequest_Type = Counter64
_DhcpRequest_Object = MibTableColumn
dhcpRequest = _DhcpRequest_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 11, 2, 1, 3),
    _DhcpRequest_Type()
)
dhcpRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRequest.setStatus("current")
_DhcpAck_Type = Counter64
_DhcpAck_Object = MibTableColumn
dhcpAck = _DhcpAck_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 11, 2, 1, 4),
    _DhcpAck_Type()
)
dhcpAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpAck.setStatus("current")
_DhcpAckBySnoopFull_Type = Counter64
_DhcpAckBySnoopFull_Object = MibTableColumn
dhcpAckBySnoopFull = _DhcpAckBySnoopFull_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 11, 2, 1, 5),
    _DhcpAckBySnoopFull_Type()
)
dhcpAckBySnoopFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpAckBySnoopFull.setStatus("current")
_PaepvcStats_ObjectIdentity = ObjectIdentity
paepvcStats = _PaepvcStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 12)
)
_PaepvcSessionTable_Object = MibTable
paepvcSessionTable = _PaepvcSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 12, 1)
)
if mibBuilder.loadTexts:
    paepvcSessionTable.setStatus("current")
_PaepvcSessionEntry_Object = MibTableRow
paepvcSessionEntry = _PaepvcSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 12, 1, 1)
)
paepvcSessionEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZYXEL-IES1248", "paepvcSessionVpi"),
    (0, "ZYXEL-IES1248", "paepvcSessionVci"),
)
if mibBuilder.loadTexts:
    paepvcSessionEntry.setStatus("current")
_PaepvcSessionVpi_Type = Integer32
_PaepvcSessionVpi_Object = MibTableColumn
paepvcSessionVpi = _PaepvcSessionVpi_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 12, 1, 1, 1),
    _PaepvcSessionVpi_Type()
)
paepvcSessionVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcSessionVpi.setStatus("current")
_PaepvcSessionVci_Type = Integer32
_PaepvcSessionVci_Object = MibTableColumn
paepvcSessionVci = _PaepvcSessionVci_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 12, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 12, 1, 1, 3),
    _PaepvcSessionState_Type()
)
paepvcSessionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcSessionState.setStatus("current")
_PaepvcSessionId_Type = Integer32
_PaepvcSessionId_Object = MibTableColumn
paepvcSessionId = _PaepvcSessionId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 12, 1, 1, 4),
    _PaepvcSessionId_Type()
)
paepvcSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcSessionId.setStatus("current")
_PaepvcSessionUptime_Type = Unsigned32
_PaepvcSessionUptime_Object = MibTableColumn
paepvcSessionUptime = _PaepvcSessionUptime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 12, 1, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 12, 1, 1, 6),
    _PaepvcSessionacname_Type()
)
paepvcSessionacname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcSessionacname.setStatus("current")
_PaepvcSessionsrvcname_Type = DisplayString
_PaepvcSessionsrvcname_Object = MibTableColumn
paepvcSessionsrvcname = _PaepvcSessionsrvcname_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 12, 1, 1, 7),
    _PaepvcSessionsrvcname_Type()
)
paepvcSessionsrvcname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcSessionsrvcname.setStatus("current")
_PaepvcCountTable_Object = MibTable
paepvcCountTable = _PaepvcCountTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 12, 2)
)
if mibBuilder.loadTexts:
    paepvcCountTable.setStatus("current")
_PaepvcCountEntry_Object = MibTableRow
paepvcCountEntry = _PaepvcCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 12, 2, 1)
)
paepvcCountEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZYXEL-IES1248", "paepvcCountVpi"),
    (0, "ZYXEL-IES1248", "paepvcCountVci"),
)
if mibBuilder.loadTexts:
    paepvcCountEntry.setStatus("current")
_PaepvcCountVpi_Type = Integer32
_PaepvcCountVpi_Object = MibTableColumn
paepvcCountVpi = _PaepvcCountVpi_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 12, 2, 1, 1),
    _PaepvcCountVpi_Type()
)
paepvcCountVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcCountVpi.setStatus("current")
_PaepvcCountVci_Type = Integer32
_PaepvcCountVci_Object = MibTableColumn
paepvcCountVci = _PaepvcCountVci_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 12, 2, 1, 2),
    _PaepvcCountVci_Type()
)
paepvcCountVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcCountVci.setStatus("current")
_PaepvcCountPppLcpCfgReqRx_Type = Unsigned32
_PaepvcCountPppLcpCfgReqRx_Object = MibTableColumn
paepvcCountPppLcpCfgReqRx = _PaepvcCountPppLcpCfgReqRx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 12, 2, 1, 3),
    _PaepvcCountPppLcpCfgReqRx_Type()
)
paepvcCountPppLcpCfgReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcCountPppLcpCfgReqRx.setStatus("current")
_PaepvcCountPppLcpEchoReqRx_Type = Unsigned32
_PaepvcCountPppLcpEchoReqRx_Object = MibTableColumn
paepvcCountPppLcpEchoReqRx = _PaepvcCountPppLcpEchoReqRx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 12, 2, 1, 4),
    _PaepvcCountPppLcpEchoReqRx_Type()
)
paepvcCountPppLcpEchoReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcCountPppLcpEchoReqRx.setStatus("current")
_PaepvcCountPppLcpEchoReplyRx_Type = Unsigned32
_PaepvcCountPppLcpEchoReplyRx_Object = MibTableColumn
paepvcCountPppLcpEchoReplyRx = _PaepvcCountPppLcpEchoReplyRx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 12, 2, 1, 5),
    _PaepvcCountPppLcpEchoReplyRx_Type()
)
paepvcCountPppLcpEchoReplyRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcCountPppLcpEchoReplyRx.setStatus("current")
_PaepvcCountPadiTx_Type = Unsigned32
_PaepvcCountPadiTx_Object = MibTableColumn
paepvcCountPadiTx = _PaepvcCountPadiTx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 12, 2, 1, 6),
    _PaepvcCountPadiTx_Type()
)
paepvcCountPadiTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcCountPadiTx.setStatus("current")
_PaepvcCountPadoRx_Type = Unsigned32
_PaepvcCountPadoRx_Object = MibTableColumn
paepvcCountPadoRx = _PaepvcCountPadoRx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 12, 2, 1, 7),
    _PaepvcCountPadoRx_Type()
)
paepvcCountPadoRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcCountPadoRx.setStatus("current")
_PaepvcCountPadrTx_Type = Unsigned32
_PaepvcCountPadrTx_Object = MibTableColumn
paepvcCountPadrTx = _PaepvcCountPadrTx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 12, 2, 1, 8),
    _PaepvcCountPadrTx_Type()
)
paepvcCountPadrTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcCountPadrTx.setStatus("current")
_PaepvcCountPadsRx_Type = Unsigned32
_PaepvcCountPadsRx_Object = MibTableColumn
paepvcCountPadsRx = _PaepvcCountPadsRx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 12, 2, 1, 9),
    _PaepvcCountPadsRx_Type()
)
paepvcCountPadsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcCountPadsRx.setStatus("current")
_PaepvcCountPadtTx_Type = Unsigned32
_PaepvcCountPadtTx_Object = MibTableColumn
paepvcCountPadtTx = _PaepvcCountPadtTx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 12, 2, 1, 10),
    _PaepvcCountPadtTx_Type()
)
paepvcCountPadtTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcCountPadtTx.setStatus("current")
_PaepvcCountPadtRx_Type = Unsigned32
_PaepvcCountPadtRx_Object = MibTableColumn
paepvcCountPadtRx = _PaepvcCountPadtRx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 12, 2, 1, 11),
    _PaepvcCountPadtRx_Type()
)
paepvcCountPadtRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcCountPadtRx.setStatus("current")
_PaepvcCountSrvcnameErrRx_Type = Unsigned32
_PaepvcCountSrvcnameErrRx_Object = MibTableColumn
paepvcCountSrvcnameErrRx = _PaepvcCountSrvcnameErrRx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 12, 2, 1, 12),
    _PaepvcCountSrvcnameErrRx_Type()
)
paepvcCountSrvcnameErrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcCountSrvcnameErrRx.setStatus("current")
_PaepvcCountAcSystemErrRx_Type = Unsigned32
_PaepvcCountAcSystemErrRx_Object = MibTableColumn
paepvcCountAcSystemErrRx = _PaepvcCountAcSystemErrRx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 12, 2, 1, 13),
    _PaepvcCountAcSystemErrRx_Type()
)
paepvcCountAcSystemErrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcCountAcSystemErrRx.setStatus("current")
_PaepvcCountGenericErrTx_Type = Unsigned32
_PaepvcCountGenericErrTx_Object = MibTableColumn
paepvcCountGenericErrTx = _PaepvcCountGenericErrTx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 12, 2, 1, 14),
    _PaepvcCountGenericErrTx_Type()
)
paepvcCountGenericErrTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcCountGenericErrTx.setStatus("current")
_PaepvcCountGenericErrRx_Type = Unsigned32
_PaepvcCountGenericErrRx_Object = MibTableColumn
paepvcCountGenericErrRx = _PaepvcCountGenericErrRx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 12, 2, 1, 15),
    _PaepvcCountGenericErrRx_Type()
)
paepvcCountGenericErrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcCountGenericErrRx.setStatus("current")
_MacStats_ObjectIdentity = ObjectIdentity
macStats = _MacStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 13)
)
_MacDisplayTarget_Type = Integer32
_MacDisplayTarget_Object = MibScalar
macDisplayTarget = _MacDisplayTarget_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 13, 1),
    _MacDisplayTarget_Type()
)
macDisplayTarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macDisplayTarget.setStatus("current")
_MacTable_Object = MibTable
macTable = _MacTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 13, 2)
)
if mibBuilder.loadTexts:
    macTable.setStatus("current")
_MacEntry_Object = MibTableRow
macEntry = _MacEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 13, 2, 1)
)
macEntry.setIndexNames(
    (0, "ZYXEL-IES1248", "macAddress"),
)
if mibBuilder.loadTexts:
    macEntry.setStatus("current")
_MacAddress_Type = MacAddress
_MacAddress_Object = MibTableColumn
macAddress = _MacAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 13, 2, 1, 1),
    _MacAddress_Type()
)
macAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macAddress.setStatus("current")
_MacPort_Type = Integer32
_MacPort_Object = MibTableColumn
macPort = _MacPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 13, 2, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 13, 2, 1, 3),
    _MacStatus_Type()
)
macStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macStatus.setStatus("current")
_IpbpvcStats_ObjectIdentity = ObjectIdentity
ipbpvcStats = _IpbpvcStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 14)
)
_ArpproxyTable_Object = MibTable
arpproxyTable = _ArpproxyTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 14, 1)
)
if mibBuilder.loadTexts:
    arpproxyTable.setStatus("current")
_ArpproxyEntry_Object = MibTableRow
arpproxyEntry = _ArpproxyEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 14, 1, 1)
)
arpproxyEntry.setIndexNames(
    (0, "ZYXEL-IES1248", "ipbpvcDomainName"),
    (0, "ZYXEL-IES1248", "arpproxyIp"),
)
if mibBuilder.loadTexts:
    arpproxyEntry.setStatus("current")
_ArpproxyIp_Type = IpAddress
_ArpproxyIp_Object = MibTableColumn
arpproxyIp = _ArpproxyIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 14, 1, 1, 1),
    _ArpproxyIp_Type()
)
arpproxyIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpproxyIp.setStatus("current")
_ArpproxyMac_Type = MacAddress
_ArpproxyMac_Object = MibTableColumn
arpproxyMac = _ArpproxyMac_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 14, 1, 1, 2),
    _ArpproxyMac_Type()
)
arpproxyMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpproxyMac.setStatus("current")
_ArpproxyIfIndex_Type = Integer32
_ArpproxyIfIndex_Object = MibTableColumn
arpproxyIfIndex = _ArpproxyIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 14, 1, 1, 3),
    _ArpproxyIfIndex_Type()
)
arpproxyIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpproxyIfIndex.setStatus("current")
_ArpproxyVpi_Type = Integer32
_ArpproxyVpi_Object = MibTableColumn
arpproxyVpi = _ArpproxyVpi_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 14, 1, 1, 4),
    _ArpproxyVpi_Type()
)
arpproxyVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpproxyVpi.setStatus("current")
_ArpproxyVci_Type = Integer32
_ArpproxyVci_Object = MibTableColumn
arpproxyVci = _ArpproxyVci_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 14, 1, 1, 5),
    _ArpproxyVci_Type()
)
arpproxyVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpproxyVci.setStatus("current")
_ArpproxyInterfaceIp_Type = IpAddress
_ArpproxyInterfaceIp_Object = MibTableColumn
arpproxyInterfaceIp = _ArpproxyInterfaceIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 14, 1, 1, 6),
    _ArpproxyInterfaceIp_Type()
)
arpproxyInterfaceIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpproxyInterfaceIp.setStatus("current")
_ArpproxyInterfaceMask_Type = Integer32
_ArpproxyInterfaceMask_Object = MibTableColumn
arpproxyInterfaceMask = _ArpproxyInterfaceMask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 14, 1, 1, 7),
    _ArpproxyInterfaceMask_Type()
)
arpproxyInterfaceMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpproxyInterfaceMask.setStatus("current")
_ArpproxyInterfaceVid_Type = VlanIndex
_ArpproxyInterfaceVid_Object = MibTableColumn
arpproxyInterfaceVid = _ArpproxyInterfaceVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 14, 1, 1, 8),
    _ArpproxyInterfaceVid_Type()
)
arpproxyInterfaceVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpproxyInterfaceVid.setStatus("current")


class _ArpproxyDhcpIp_Type(Integer32):
    """Custom type arpproxyDhcpIp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_ArpproxyDhcpIp_Type.__name__ = "Integer32"
_ArpproxyDhcpIp_Object = MibTableColumn
arpproxyDhcpIp = _ArpproxyDhcpIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 14, 1, 1, 9),
    _ArpproxyDhcpIp_Type()
)
arpproxyDhcpIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpproxyDhcpIp.setStatus("current")


class _ArpproxyType_Type(Integer32):
    """Custom type arpproxyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("upstream", 1),
          ("downstream", 2))
    )


_ArpproxyType_Type.__name__ = "Integer32"
_ArpproxyType_Object = MibTableColumn
arpproxyType = _ArpproxyType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 14, 1, 1, 10),
    _ArpproxyType_Type()
)
arpproxyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpproxyType.setStatus("current")
_IpbpvcIfDynamicTable_Object = MibTable
ipbpvcIfDynamicTable = _IpbpvcIfDynamicTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 14, 2)
)
if mibBuilder.loadTexts:
    ipbpvcIfDynamicTable.setStatus("current")
_IpbpvcIfDynamicEntry_Object = MibTableRow
ipbpvcIfDynamicEntry = _IpbpvcIfDynamicEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 14, 2, 1)
)
ipbpvcIfDynamicEntry.setIndexNames(
    (0, "ZYXEL-IES1248", "ipbpvcDomainName"),
    (0, "ZYXEL-IES1248", "ipbpvcIfDynamicIp"),
    (0, "ZYXEL-IES1248", "ipbpvcIfDynamicMask"),
    (0, "ZYXEL-IES1248", "ipbpvcDomainVlanId"),
)
if mibBuilder.loadTexts:
    ipbpvcIfDynamicEntry.setStatus("current")
_IpbpvcIfDynamicIp_Type = IpAddress
_IpbpvcIfDynamicIp_Object = MibTableColumn
ipbpvcIfDynamicIp = _IpbpvcIfDynamicIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 14, 2, 1, 1),
    _IpbpvcIfDynamicIp_Type()
)
ipbpvcIfDynamicIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipbpvcIfDynamicIp.setStatus("current")
_IpbpvcIfDynamicMask_Type = Integer32
_IpbpvcIfDynamicMask_Object = MibTableColumn
ipbpvcIfDynamicMask = _IpbpvcIfDynamicMask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 14, 2, 1, 2),
    _IpbpvcIfDynamicMask_Type()
)
ipbpvcIfDynamicMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipbpvcIfDynamicMask.setStatus("current")
_IpbpvcIfDynamicIfIndex_Type = Integer32
_IpbpvcIfDynamicIfIndex_Object = MibTableColumn
ipbpvcIfDynamicIfIndex = _IpbpvcIfDynamicIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 14, 2, 1, 3),
    _IpbpvcIfDynamicIfIndex_Type()
)
ipbpvcIfDynamicIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipbpvcIfDynamicIfIndex.setStatus("current")
_IpbpvcIfDynamicVpi_Type = Integer32
_IpbpvcIfDynamicVpi_Object = MibTableColumn
ipbpvcIfDynamicVpi = _IpbpvcIfDynamicVpi_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 14, 2, 1, 4),
    _IpbpvcIfDynamicVpi_Type()
)
ipbpvcIfDynamicVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipbpvcIfDynamicVpi.setStatus("current")
_IpbpvcIfDynamicVci_Type = Integer32
_IpbpvcIfDynamicVci_Object = MibTableColumn
ipbpvcIfDynamicVci = _IpbpvcIfDynamicVci_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 14, 2, 1, 5),
    _IpbpvcIfDynamicVci_Type()
)
ipbpvcIfDynamicVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipbpvcIfDynamicVci.setStatus("current")
_IpbpvcRouteDynamicTable_Object = MibTable
ipbpvcRouteDynamicTable = _IpbpvcRouteDynamicTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 14, 3)
)
if mibBuilder.loadTexts:
    ipbpvcRouteDynamicTable.setStatus("current")
_IpbpvcRouteDynamicEntry_Object = MibTableRow
ipbpvcRouteDynamicEntry = _IpbpvcRouteDynamicEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 14, 3, 1)
)
ipbpvcRouteDynamicEntry.setIndexNames(
    (0, "ZYXEL-IES1248", "ipbpvcDomainName"),
    (0, "ZYXEL-IES1248", "ipbpvcRouteDynamicType"),
    (0, "ZYXEL-IES1248", "ipbpvcRouteDynamicIp"),
    (0, "ZYXEL-IES1248", "ipbpvcRouteDynamicMask"),
)
if mibBuilder.loadTexts:
    ipbpvcRouteDynamicEntry.setStatus("current")


class _IpbpvcRouteDynamicType_Type(Integer32):
    """Custom type ipbpvcRouteDynamicType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("upstream", 1),
          ("downstream", 2))
    )


_IpbpvcRouteDynamicType_Type.__name__ = "Integer32"
_IpbpvcRouteDynamicType_Object = MibTableColumn
ipbpvcRouteDynamicType = _IpbpvcRouteDynamicType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 14, 3, 1, 1),
    _IpbpvcRouteDynamicType_Type()
)
ipbpvcRouteDynamicType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipbpvcRouteDynamicType.setStatus("current")
_IpbpvcRouteDynamicIp_Type = IpAddress
_IpbpvcRouteDynamicIp_Object = MibTableColumn
ipbpvcRouteDynamicIp = _IpbpvcRouteDynamicIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 14, 3, 1, 2),
    _IpbpvcRouteDynamicIp_Type()
)
ipbpvcRouteDynamicIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipbpvcRouteDynamicIp.setStatus("current")
_IpbpvcRouteDynamicMask_Type = Integer32
_IpbpvcRouteDynamicMask_Object = MibTableColumn
ipbpvcRouteDynamicMask = _IpbpvcRouteDynamicMask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 14, 3, 1, 3),
    _IpbpvcRouteDynamicMask_Type()
)
ipbpvcRouteDynamicMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipbpvcRouteDynamicMask.setStatus("current")
_IpbpvcRouteDynamicNextHop_Type = IpAddress
_IpbpvcRouteDynamicNextHop_Object = MibTableColumn
ipbpvcRouteDynamicNextHop = _IpbpvcRouteDynamicNextHop_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 14, 3, 1, 4),
    _IpbpvcRouteDynamicNextHop_Type()
)
ipbpvcRouteDynamicNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipbpvcRouteDynamicNextHop.setStatus("current")
_IpbpvcRouteDynamicMetric_Type = Integer32
_IpbpvcRouteDynamicMetric_Object = MibTableColumn
ipbpvcRouteDynamicMetric = _IpbpvcRouteDynamicMetric_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 14, 3, 1, 5),
    _IpbpvcRouteDynamicMetric_Type()
)
ipbpvcRouteDynamicMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipbpvcRouteDynamicMetric.setStatus("current")
_IpbpvcRouteDynamicPriority_Type = Integer32
_IpbpvcRouteDynamicPriority_Object = MibTableColumn
ipbpvcRouteDynamicPriority = _IpbpvcRouteDynamicPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 14, 3, 1, 6),
    _IpbpvcRouteDynamicPriority_Type()
)
ipbpvcRouteDynamicPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipbpvcRouteDynamicPriority.setStatus("current")
_LoopguardStats_ObjectIdentity = ObjectIdentity
loopguardStats = _LoopguardStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 17)
)


class _LoopguardSysStatus_Type(Integer32):
    """Custom type loopguardSysStatus based on Integer32"""
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


_LoopguardSysStatus_Type.__name__ = "Integer32"
_LoopguardSysStatus_Object = MibScalar
loopguardSysStatus = _LoopguardSysStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 17, 1),
    _LoopguardSysStatus_Type()
)
loopguardSysStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loopguardSysStatus.setStatus("current")
_LoopguardPortStatsTable_Object = MibTable
loopguardPortStatsTable = _LoopguardPortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 17, 2)
)
if mibBuilder.loadTexts:
    loopguardPortStatsTable.setStatus("current")
_LoopguardPortStatsEntry_Object = MibTableRow
loopguardPortStatsEntry = _LoopguardPortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 17, 2, 1)
)
loopguardPortStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    loopguardPortStatsEntry.setStatus("current")


class _LoopguardPortStatsLoopDetected_Type(Integer32):
    """Custom type loopguardPortStatsLoopDetected based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("loop", 1),
          ("noLoop", 2))
    )


_LoopguardPortStatsLoopDetected_Type.__name__ = "Integer32"
_LoopguardPortStatsLoopDetected_Object = MibTableColumn
loopguardPortStatsLoopDetected = _LoopguardPortStatsLoopDetected_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 17, 2, 1, 1),
    _LoopguardPortStatsLoopDetected_Type()
)
loopguardPortStatsLoopDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loopguardPortStatsLoopDetected.setStatus("current")


class _LoopguardPortStatsLinkedState_Type(Integer32):
    """Custom type loopguardPortStatsLinkedState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_LoopguardPortStatsLinkedState_Type.__name__ = "Integer32"
_LoopguardPortStatsLinkedState_Object = MibTableColumn
loopguardPortStatsLinkedState = _LoopguardPortStatsLinkedState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 17, 2, 1, 2),
    _LoopguardPortStatsLinkedState_Type()
)
loopguardPortStatsLinkedState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loopguardPortStatsLinkedState.setStatus("current")
_LoopguardPortStatsTxPkts_Type = Counter32
_LoopguardPortStatsTxPkts_Object = MibTableColumn
loopguardPortStatsTxPkts = _LoopguardPortStatsTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 17, 2, 1, 3),
    _LoopguardPortStatsTxPkts_Type()
)
loopguardPortStatsTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loopguardPortStatsTxPkts.setStatus("current")
_LoopguardPortStatsRxPkts_Type = Counter32
_LoopguardPortStatsRxPkts_Object = MibTableColumn
loopguardPortStatsRxPkts = _LoopguardPortStatsRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 17, 2, 1, 4),
    _LoopguardPortStatsRxPkts_Type()
)
loopguardPortStatsRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loopguardPortStatsRxPkts.setStatus("current")
_LoopguardPortStatsBadPkts_Type = Counter32
_LoopguardPortStatsBadPkts_Object = MibTableColumn
loopguardPortStatsBadPkts = _LoopguardPortStatsBadPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 17, 2, 1, 5),
    _LoopguardPortStatsBadPkts_Type()
)
loopguardPortStatsBadPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loopguardPortStatsBadPkts.setStatus("current")
_LoopguardPortStatsShutdownTime_Type = DisplayString
_LoopguardPortStatsShutdownTime_Object = MibTableColumn
loopguardPortStatsShutdownTime = _LoopguardPortStatsShutdownTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 17, 2, 1, 6),
    _LoopguardPortStatsShutdownTime_Type()
)
loopguardPortStatsShutdownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loopguardPortStatsShutdownTime.setStatus("current")


class _LoopguardPortStatsOps_Type(Integer32):
    """Custom type loopguardPortStatsOps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clearLoopguardStatistics", 1)
    )


_LoopguardPortStatsOps_Type.__name__ = "Integer32"
_LoopguardPortStatsOps_Object = MibTableColumn
loopguardPortStatsOps = _LoopguardPortStatsOps_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 13, 17, 2, 1, 7),
    _LoopguardPortStatsOps_Type()
)
loopguardPortStatsOps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loopguardPortStatsOps.setStatus("current")
_Clear_ObjectIdentity = ObjectIdentity
clear = _Clear_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 14)
)
_CounterClearTarget_Type = OctetString
_CounterClearTarget_Object = MibScalar
counterClearTarget = _CounterClearTarget_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 14, 1),
    _CounterClearTarget_Type()
)
counterClearTarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    counterClearTarget.setStatus("current")
_CounterClearOps_Type = Integer32
_CounterClearOps_Object = MibScalar
counterClearOps = _CounterClearOps_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 14, 2),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 14, 3),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 14, 4),
    _CounterClearVci_Type()
)
counterClearVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    counterClearVci.setStatus("current")

# Managed Objects groups


# Notification objects

eqptHWMonitorFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 12, 3, 1)
)
if mibBuilder.loadTexts:
    eqptHWMonitorFailure.setStatus(
        "current"
    )

sysMacAntiSpoofing = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 12, 4, 1)
)
sysMacAntiSpoofing.setObjects(
      *(("ZYXEL-IES1248", "sysMacAntiSpoofOrig"),
        ("ZYXEL-IES1248", "sysMacAntiSpoofNew"),
        ("ZYXEL-IES1248", "sysMacAntiSpoofMAC"))
)
if mibBuilder.loadTexts:
    sysMacAntiSpoofing.setStatus(
        "current"
    )

sysAlarmCutoffEnable = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 12, 4, 2)
)
if mibBuilder.loadTexts:
    sysAlarmCutoffEnable.setStatus(
        "current"
    )

sysAlarmClearEnable = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 12, 4, 3)
)
if mibBuilder.loadTexts:
    sysAlarmClearEnable.setStatus(
        "current"
    )

sysLoginFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 12, 4, 4)
)
if mibBuilder.loadTexts:
    sysLoginFailure.setStatus(
        "current"
    )

sysLoginOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 12, 4, 5)
)
sysLoginOk.setObjects(
      *(("ZYXEL-IES1248", "sysUser"),
        ("ZYXEL-IES1248", "sysAccessPoint"))
)
if mibBuilder.loadTexts:
    sysLoginOk.setStatus(
        "current"
    )

dslLoopguard = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 12, 5, 1)
)
dslLoopguard.setObjects(
      *(("ZYXEL-IES1248", "lgReceiverIfIndex"),
        ("ZYXEL-IES1248", "lgSenderIfIndex"))
)
if mibBuilder.loadTexts:
    dslLoopguard.setStatus(
        "current"
    )

dslLoopguardClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 12, 5, 2)
)
dslLoopguardClear.setObjects(
      *(("ZYXEL-IES1248", "lgReceiverIfIndex"),
        ("ZYXEL-IES1248", "lgSenderIfIndex"))
)
if mibBuilder.loadTexts:
    dslLoopguardClear.setStatus(
        "current"
    )

enetLoopguard = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 12, 6, 1)
)
enetLoopguard.setObjects(
      *(("ZYXEL-IES1248", "lgReceiverIfIndex"),
        ("ZYXEL-IES1248", "lgSenderIfIndex"))
)
if mibBuilder.loadTexts:
    enetLoopguard.setStatus(
        "current"
    )

enetLoopguardClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 13, 6, 12, 6, 2)
)
enetLoopguardClear.setObjects(
      *(("ZYXEL-IES1248", "lgReceiverIfIndex"),
        ("ZYXEL-IES1248", "lgSenderIfIndex"))
)
if mibBuilder.loadTexts:
    enetLoopguardClear.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-IES1248",
    **{"zyxel": zyxel,
       "products": products,
       "accessSwitch": accessSwitch,
       "iesSeries": iesSeries,
       "ies1248": ies1248,
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
       "port": port,
       "subrPortTable": subrPortTable,
       "subrPortEntry": subrPortEntry,
       "subrPortName": subrPortName,
       "subrPortTel": subrPortTel,
       "adslPort": adslPort,
       "adslLineConfTable": adslLineConfTable,
       "adslLineConfEntry": adslLineConfEntry,
       "adslLineConfAdslMode": adslLineConfAdslMode,
       "adslLineConfAnnexL": adslLineConfAnnexL,
       "adslLineConfAnnexM": adslLineConfAnnexM,
       "adslLineConfAnnexI": adslLineConfAnnexI,
       "adslLineConfOptionMask": adslLineConfOptionMask,
       "adslLineConfPowerMgmt": adslLineConfPowerMgmt,
       "adslLineConfPowerMode": adslLineConfPowerMode,
       "adslLineConfAturMaxTxPower": adslLineConfAturMaxTxPower,
       "adslLineConfAtucMaxTxPower": adslLineConfAtucMaxTxPower,
       "adslLineConfMaxRxPower": adslLineConfMaxRxPower,
       "adslLineConfAturCarrierMask": adslLineConfAturCarrierMask,
       "adslLineConfAtucCarrierMask0": adslLineConfAtucCarrierMask0,
       "adslLineConfAtucCarrierMask1": adslLineConfAtucCarrierMask1,
       "adslLineConfAturInp": adslLineConfAturInp,
       "adslLineConfAtucInp": adslLineConfAtucInp,
       "adslLineConfL0Time": adslLineConfL0Time,
       "adslLineConfL2Time": adslLineConfL2Time,
       "adslLineConfL2ATPR": adslLineConfL2ATPR,
       "adslLineConfL2ATPRT": adslLineConfL2ATPRT,
       "adslLineConfMaxL2Rate": adslLineConfMaxL2Rate,
       "adslLineConfMinL2Rate": adslLineConfMinL2Rate,
       "adslLineConfL0toL2Rate": adslLineConfL0toL2Rate,
       "adslPortBatchSet": adslPortBatchSet,
       "adslPortTarget": adslPortTarget,
       "adslPortOps": adslPortOps,
       "adslPortOps2": adslPortOps2,
       "adslModeForBatchSet": adslModeForBatchSet,
       "adslLineProfileForBatchSet": adslLineProfileForBatchSet,
       "adslAlarmProfileForBatchSet": adslAlarmProfileForBatchSet,
       "adslOptionMaskForBatchSet": adslOptionMaskForBatchSet,
       "adslAturMaxTxPowerForBatchSet": adslAturMaxTxPowerForBatchSet,
       "adslAtucMaxTxPowerForBatchSet": adslAtucMaxTxPowerForBatchSet,
       "adslMaxRxPowerForBatchSet": adslMaxRxPowerForBatchSet,
       "adslAturCarrierMaskForBatchSet": adslAturCarrierMaskForBatchSet,
       "adslAtucCarrierMask0ForBatchSet": adslAtucCarrierMask0ForBatchSet,
       "adslAtucCarrierMask1ForBatchSet": adslAtucCarrierMask1ForBatchSet,
       "adslAturInpForBatchSet": adslAturInpForBatchSet,
       "adslAtucInpForBatchSet": adslAtucInpForBatchSet,
       "adslL0TimeForBatchSet": adslL0TimeForBatchSet,
       "adslL2TimeForBatchSet": adslL2TimeForBatchSet,
       "adslL2ATPRForBatchSet": adslL2ATPRForBatchSet,
       "adslL2ATPRTForBatchSet": adslL2ATPRTForBatchSet,
       "adslMaxL2RateForBatchSet": adslMaxL2RateForBatchSet,
       "adslMinL2RateForBatchSet": adslMinL2RateForBatchSet,
       "adslL0toL2RateForBatchSet": adslL0toL2RateForBatchSet,
       "adslLineStatusTable": adslLineStatusTable,
       "adslLineStatusEntry": adslLineStatusEntry,
       "adslLineStatusMode": adslLineStatusMode,
       "adslLineUpTime": adslLineUpTime,
       "powerMgmtParamTable": powerMgmtParamTable,
       "powerMgmtParamEntry": powerMgmtParamEntry,
       "powerMgmtL0Time": powerMgmtL0Time,
       "powerMgmtL2Time": powerMgmtL2Time,
       "powerMgmtL2Atpr": powerMgmtL2Atpr,
       "powerMgmtL2Atprt": powerMgmtL2Atprt,
       "powerMgmtL2MinRate": powerMgmtL2MinRate,
       "powerMgmtL2MaxRate": powerMgmtL2MaxRate,
       "powerMgmtL2ThreshRate": powerMgmtL2ThreshRate,
       "powerMgmtPSDTable": powerMgmtPSDTable,
       "powerMgmtPSDEntry": powerMgmtPSDEntry,
       "powerMgmtAtucMaxPSD": powerMgmtAtucMaxPSD,
       "powerMgmtAturMaxPSD": powerMgmtAturMaxPSD,
       "pvc": pvc,
       "maxNumOfPvcs": maxNumOfPvcs,
       "pvcTable": pvcTable,
       "pvcEntry": pvcEntry,
       "pvcVpi": pvcVpi,
       "pvcVci": pvcVci,
       "pvcPvid": pvcPvid,
       "pvcPriority": pvcPriority,
       "pvcProfileDS": pvcProfileDS,
       "pvcRowStatus": pvcRowStatus,
       "pvcProfileUS": pvcProfileUS,
       "pvcmaccnt": pvcmaccnt,
       "pvcUsRateLimitTable": pvcUsRateLimitTable,
       "pvcUsRateLimitEntry": pvcUsRateLimitEntry,
       "pvcUsRateLimitEnable": pvcUsRateLimitEnable,
       "pvcUsRateLimit": pvcUsRateLimit,
       "ppvc": ppvc,
       "maxNumOfPriorityPvcs": maxNumOfPriorityPvcs,
       "ppvcTable": ppvcTable,
       "ppvcEntry": ppvcEntry,
       "ppvcVpi": ppvcVpi,
       "ppvcVci": ppvcVci,
       "ppvcPvid": ppvcPvid,
       "ppvcEncap": ppvcEncap,
       "ppvcPriority": ppvcPriority,
       "ppvcRowStatus": ppvcRowStatus,
       "ppvcMemberTable": ppvcMemberTable,
       "ppvcMemberEntry": ppvcMemberEntry,
       "ppvcMemberVpi": ppvcMemberVpi,
       "ppvcMemberVci": ppvcMemberVci,
       "ppvcMemberPriority": ppvcMemberPriority,
       "ppvcMemberProfileDS": ppvcMemberProfileDS,
       "ppvcMemberRowStatus": ppvcMemberRowStatus,
       "ppvcMemberProfileUS": ppvcMemberProfileUS,
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
       "rpvcDSProfile": rpvcDSProfile,
       "rpvcUSProfile": rpvcUSProfile,
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
       "paepvcPriority": paepvcPriority,
       "paepvcProfileDS": paepvcProfileDS,
       "paepvcAcName": paepvcAcName,
       "paepvcServiceName": paepvcServiceName,
       "paepvcHelloTime": paepvcHelloTime,
       "paepvcRowStatus": paepvcRowStatus,
       "paepvcProfileUS": paepvcProfileUS,
       "tlspvc": tlspvc,
       "tlspvcTable": tlspvcTable,
       "tlspvcEntry": tlspvcEntry,
       "tlspvcVpi": tlspvcVpi,
       "tlspvcVci": tlspvcVci,
       "tlspvcSvid": tlspvcSvid,
       "tlspvcSpriority": tlspvcSpriority,
       "tlspvcProfileDS": tlspvcProfileDS,
       "tlspvcRowStatus": tlspvcRowStatus,
       "tlspvcProfileUS": tlspvcProfileUS,
       "ipbpvc": ipbpvc,
       "ipbpvcDomainTable": ipbpvcDomainTable,
       "ipbpvcDomainEntry": ipbpvcDomainEntry,
       "ipbpvcDomainName": ipbpvcDomainName,
       "ipbpvcDomainRowStatus": ipbpvcDomainRowStatus,
       "ipbpvcDomainVlanTable": ipbpvcDomainVlanTable,
       "ipbpvcDomainVlanEntry": ipbpvcDomainVlanEntry,
       "ipbpvcDomainVlanId": ipbpvcDomainVlanId,
       "ipbpvcDomainDhcpVlanEnable": ipbpvcDomainDhcpVlanEnable,
       "ipbpvcDomainVlanRowStatus": ipbpvcDomainVlanRowStatus,
       "ipbpvcEdgeRouterTable": ipbpvcEdgeRouterTable,
       "ipbpvcEdgeRouterEntry": ipbpvcEdgeRouterEntry,
       "ipbpvcEdgeRouterIp": ipbpvcEdgeRouterIp,
       "ipbpvcEdgeRouterVid": ipbpvcEdgeRouterVid,
       "ipbpvcEdgeRouterMask": ipbpvcEdgeRouterMask,
       "ipbpvcEdgeRouterRowStatus": ipbpvcEdgeRouterRowStatus,
       "ipbpvcInterfaceTable": ipbpvcInterfaceTable,
       "ipbpvcInterfaceEntry": ipbpvcInterfaceEntry,
       "ipbpvcInterfaceIp": ipbpvcInterfaceIp,
       "ipbpvcInterfaceMask": ipbpvcInterfaceMask,
       "ipbpvcInterfaceVid": ipbpvcInterfaceVid,
       "ipbpvcInterfaceIfIndex": ipbpvcInterfaceIfIndex,
       "ipbpvcInterfaceVpi": ipbpvcInterfaceVpi,
       "ipbpvcInterfaceVci": ipbpvcInterfaceVci,
       "ipbpvcInterfaceRowStatus": ipbpvcInterfaceRowStatus,
       "ipbpvcRouteTable": ipbpvcRouteTable,
       "ipbpvcRouteEntry": ipbpvcRouteEntry,
       "ipbpvcRouteIp": ipbpvcRouteIp,
       "ipbpvcRouteMask": ipbpvcRouteMask,
       "ipbpvcRouteNextHop": ipbpvcRouteNextHop,
       "ipbpvcRouteMetric": ipbpvcRouteMetric,
       "ipbpvcRoutePriority": ipbpvcRoutePriority,
       "ipbpvcRouteRowStatus": ipbpvcRouteRowStatus,
       "ipbpvcTable": ipbpvcTable,
       "ipbpvcEntry": ipbpvcEntry,
       "ipbpvcVpi": ipbpvcVpi,
       "ipbpvcVci": ipbpvcVci,
       "ipbpvcPvid": ipbpvcPvid,
       "ipbpvcEncap": ipbpvcEncap,
       "ipbpvcPriority": ipbpvcPriority,
       "ipbpvcProfile": ipbpvcProfile,
       "ipbpvcRowStatus": ipbpvcRowStatus,
       "ipbpvcProfileUS": ipbpvcProfileUS,
       "arpproxy": arpproxy,
       "arpproxyAge": arpproxyAge,
       "arpproxyFlush": arpproxyFlush,
       "arpproxyFlushTarget": arpproxyFlushTarget,
       "arpproxyFlushOps": arpproxyFlushOps,
       "arpproxyFlushEdgeRouterIp": arpproxyFlushEdgeRouterIp,
       "arpproxyFlushEdgeRouterVid": arpproxyFlushEdgeRouterVid,
       "arpproxyFlushInterfaceIp": arpproxyFlushInterfaceIp,
       "arpproxyFlushInterfaceMask": arpproxyFlushInterfaceMask,
       "arpproxyFlushInterfaceVid": arpproxyFlushInterfaceVid,
       "gbond": gbond,
       "gbondGroupTable": gbondGroupTable,
       "gbondGroupEntry": gbondGroupEntry,
       "gbondGroupName": gbondGroupName,
       "gbondGroupPorts": gbondGroupPorts,
       "gbondGroupUpRate": gbondGroupUpRate,
       "gbondGroupDownRate": gbondGroupDownRate,
       "gbondGroupRowStatus": gbondGroupRowStatus,
       "switch": switch,
       "dot1x": dot1x,
       "maxNumberOfRadiusServers": maxNumberOfRadiusServers,
       "radiusServerTable": radiusServerTable,
       "radiusServerEntry": radiusServerEntry,
       "radiusServerIndex": radiusServerIndex,
       "radiusServerIp": radiusServerIp,
       "radiusServerPort": radiusServerPort,
       "radiusSharedSecret": radiusSharedSecret,
       "radiusServerRowStatus": radiusServerRowStatus,
       "dot1xEnable": dot1xEnable,
       "dot1xPortTable": dot1xPortTable,
       "dot1xPortEntry": dot1xPortEntry,
       "dot1xPortEnable": dot1xPortEnable,
       "dot1xPortControl": dot1xPortControl,
       "dot1xPortReAuthEnable": dot1xPortReAuthEnable,
       "dot1xPortReAuthPeriod": dot1xPortReAuthPeriod,
       "radiusMode": radiusMode,
       "maxNumberOfRadiusUserProfiles": maxNumberOfRadiusUserProfiles,
       "radiusUserProfileTable": radiusUserProfileTable,
       "radiusUserProfileEntry": radiusUserProfileEntry,
       "radiusUserProfileUserName": radiusUserProfileUserName,
       "radiusUserProfileUserPassword": radiusUserProfileUserPassword,
       "radiusUserProfileRowStatus": radiusUserProfileRowStatus,
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
       "enetMaxMtu": enetMaxMtu,
       "dhcp": dhcp,
       "dhcpRelayEnable": dhcpRelayEnable,
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
       "dhcpRelayOption82Sub1Info": dhcpRelayOption82Sub1Info,
       "maxNumOfDhcpRelay82Conf": maxNumOfDhcpRelay82Conf,
       "dhcpRelayOption82Sub1Enable": dhcpRelayOption82Sub1Enable,
       "dhcpRelayOption82Sub2Info": dhcpRelayOption82Sub2Info,
       "dhcpRelayOption82Sub2Enable": dhcpRelayOption82Sub2Enable,
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
       "dhcpSnoopTarget": dhcpSnoopTarget,
       "dhcpSnoopOps": dhcpSnoopOps,
       "dhcpStaticTable": dhcpStaticTable,
       "dhcpStaticEntry": dhcpStaticEntry,
       "dhcpStaticIpAddr": dhcpStaticIpAddr,
       "dhcpStaticRowStatus": dhcpStaticRowStatus,
       "maxNumOfDhcpStaticIp": maxNumOfDhcpStaticIp,
       "dhcpSnoopLan2lanEnable": dhcpSnoopLan2lanEnable,
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
       "aclProfileRuleSrcIP": aclProfileRuleSrcIP,
       "aclProfileRuleSrcIPMask": aclProfileRuleSrcIPMask,
       "aclProfileRuleDestIP": aclProfileRuleDestIP,
       "aclProfileRuleDestIPMask": aclProfileRuleDestIPMask,
       "aclProfileRuleStartTos": aclProfileRuleStartTos,
       "aclProfileRuleEndTos": aclProfileRuleEndTos,
       "aclProfileRuleSrcStartPort": aclProfileRuleSrcStartPort,
       "aclProfileRuleSrcEndPort": aclProfileRuleSrcEndPort,
       "aclProfileRuleDestStartPort": aclProfileRuleDestStartPort,
       "aclProfileRuleDestEndPort": aclProfileRuleDestEndPort,
       "aclProfileActionRate": aclProfileActionRate,
       "aclProfileActionrvlan": aclProfileActionrvlan,
       "aclProfileActionrpri": aclProfileActionrpri,
       "aclProfileRowStatus": aclProfileRowStatus,
       "pppoeAgent": pppoeAgent,
       "pppoeAgentTable": pppoeAgentTable,
       "pppoeAgentEntry": pppoeAgentEntry,
       "pppoeAgentEnable": pppoeAgentEnable,
       "pppoeAgentInfo": pppoeAgentInfo,
       "pppoeAgentRowStatus": pppoeAgentRowStatus,
       "pppoeAgentOptionMode": pppoeAgentOptionMode,
       "maxNumOfPppoeAgentConf": maxNumOfPppoeAgentConf,
       "fdb": fdb,
       "fdbAntiSpoofing": fdbAntiSpoofing,
       "fdbPolicy": fdbPolicy,
       "loopguard": loopguard,
       "loopguardPortTable": loopguardPortTable,
       "loopguardPortEntry": loopguardPortEntry,
       "loopguardPortEnable": loopguardPortEnable,
       "loopguardPortMode": loopguardPortMode,
       "loopguardPortRecoverTime": loopguardPortRecoverTime,
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
       "extAlarmname": extAlarmname,
       "extAlarmstatus": extAlarmstatus,
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
       "sysSlotId": sysSlotId,
       "trap": trap,
       "object": object,
       "eqptAlarmInputIndex": eqptAlarmInputIndex,
       "eqptAlarmInputName": eqptAlarmInputName,
       "sysMacAntiSpoofOrig": sysMacAntiSpoofOrig,
       "sysMacAntiSpoofNew": sysMacAntiSpoofNew,
       "sysMacAntiSpoofMAC": sysMacAntiSpoofMAC,
       "sysUser": sysUser,
       "sysAccessPoint": sysAccessPoint,
       "lgReceiverIfIndex": lgReceiverIfIndex,
       "lgSenderIfIndex": lgSenderIfIndex,
       "equipment": equipment,
       "eqptHWMonitorFailure": eqptHWMonitorFailure,
       "systrap": systrap,
       "sysMacAntiSpoofing": sysMacAntiSpoofing,
       "sysAlarmCutoffEnable": sysAlarmCutoffEnable,
       "sysAlarmClearEnable": sysAlarmClearEnable,
       "sysLoginFailure": sysLoginFailure,
       "sysLoginOk": sysLoginOk,
       "dsltrap": dsltrap,
       "dslLoopguard": dslLoopguard,
       "dslLoopguardClear": dslLoopguardClear,
       "enettrap": enettrap,
       "enetLoopguard": enetLoopguard,
       "enetLoopguardClear": enetLoopguardClear,
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
       "dhcpStats": dhcpStats,
       "dhcpSnoopIpTable": dhcpSnoopIpTable,
       "dhcpSnoopIpEntry": dhcpSnoopIpEntry,
       "dhcpSnoopIp": dhcpSnoopIp,
       "dhcpSnoopMac": dhcpSnoopMac,
       "dhcpSnoopVid": dhcpSnoopVid,
       "dhcpSnoopCounterTable": dhcpSnoopCounterTable,
       "dhcpSnoopCounterEntry": dhcpSnoopCounterEntry,
       "dhcpDiscovery": dhcpDiscovery,
       "dhcpOffer": dhcpOffer,
       "dhcpRequest": dhcpRequest,
       "dhcpAck": dhcpAck,
       "dhcpAckBySnoopFull": dhcpAckBySnoopFull,
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
       "ipbpvcStats": ipbpvcStats,
       "arpproxyTable": arpproxyTable,
       "arpproxyEntry": arpproxyEntry,
       "arpproxyIp": arpproxyIp,
       "arpproxyMac": arpproxyMac,
       "arpproxyIfIndex": arpproxyIfIndex,
       "arpproxyVpi": arpproxyVpi,
       "arpproxyVci": arpproxyVci,
       "arpproxyInterfaceIp": arpproxyInterfaceIp,
       "arpproxyInterfaceMask": arpproxyInterfaceMask,
       "arpproxyInterfaceVid": arpproxyInterfaceVid,
       "arpproxyDhcpIp": arpproxyDhcpIp,
       "arpproxyType": arpproxyType,
       "ipbpvcIfDynamicTable": ipbpvcIfDynamicTable,
       "ipbpvcIfDynamicEntry": ipbpvcIfDynamicEntry,
       "ipbpvcIfDynamicIp": ipbpvcIfDynamicIp,
       "ipbpvcIfDynamicMask": ipbpvcIfDynamicMask,
       "ipbpvcIfDynamicIfIndex": ipbpvcIfDynamicIfIndex,
       "ipbpvcIfDynamicVpi": ipbpvcIfDynamicVpi,
       "ipbpvcIfDynamicVci": ipbpvcIfDynamicVci,
       "ipbpvcRouteDynamicTable": ipbpvcRouteDynamicTable,
       "ipbpvcRouteDynamicEntry": ipbpvcRouteDynamicEntry,
       "ipbpvcRouteDynamicType": ipbpvcRouteDynamicType,
       "ipbpvcRouteDynamicIp": ipbpvcRouteDynamicIp,
       "ipbpvcRouteDynamicMask": ipbpvcRouteDynamicMask,
       "ipbpvcRouteDynamicNextHop": ipbpvcRouteDynamicNextHop,
       "ipbpvcRouteDynamicMetric": ipbpvcRouteDynamicMetric,
       "ipbpvcRouteDynamicPriority": ipbpvcRouteDynamicPriority,
       "loopguardStats": loopguardStats,
       "loopguardSysStatus": loopguardSysStatus,
       "loopguardPortStatsTable": loopguardPortStatsTable,
       "loopguardPortStatsEntry": loopguardPortStatsEntry,
       "loopguardPortStatsLoopDetected": loopguardPortStatsLoopDetected,
       "loopguardPortStatsLinkedState": loopguardPortStatsLinkedState,
       "loopguardPortStatsTxPkts": loopguardPortStatsTxPkts,
       "loopguardPortStatsRxPkts": loopguardPortStatsRxPkts,
       "loopguardPortStatsBadPkts": loopguardPortStatsBadPkts,
       "loopguardPortStatsShutdownTime": loopguardPortStatsShutdownTime,
       "loopguardPortStatsOps": loopguardPortStatsOps,
       "clear": clear,
       "counterClearTarget": counterClearTarget,
       "counterClearOps": counterClearOps,
       "counterClearVpi": counterClearVpi,
       "counterClearVci": counterClearVci}
)
