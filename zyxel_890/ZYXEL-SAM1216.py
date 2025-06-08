# SNMP MIB module (ZYXEL-SAM1216) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/zyxel_890/ZYXEL-SAM1216.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 08:35:51 2025
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
 Timeout) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "BridgeId",
    "MacAddress",
    "Timeout")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(PortList,
 VlanIndex,
 dot1qVlanIndex) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList",
    "VlanIndex",
    "dot1qVlanIndex")

(Counter64,
 Unsigned32) = mibBuilder.importSymbols(
    "RFC1155-SMI",
    "Counter64",
    "Unsigned32")

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
_SesSeries_ObjectIdentity = ObjectIdentity
sesSeries = _SesSeries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5)
)
_Sam1216_22_ObjectIdentity = ObjectIdentity
sam1216_22 = _Sam1216_22_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6)
)
_Alarmconf_ObjectIdentity = ObjectIdentity
alarmconf = _Alarmconf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 2)
)
_AlarmOps_Type = Integer32
_AlarmOps_Object = MibScalar
alarmOps = _AlarmOps_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 2, 1),
    _AlarmOps_Type()
)
alarmOps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmOps.setStatus("current")
_AlarmConfTable_Object = MibTable
alarmConfTable = _AlarmConfTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 2, 2)
)
if mibBuilder.loadTexts:
    alarmConfTable.setStatus("current")
_AlarmConfEntry_Object = MibTableRow
alarmConfEntry = _AlarmConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 2, 2, 1)
)
alarmConfEntry.setIndexNames(
    (0, "ZYXEL-SAM1216", "alarmConfId"),
)
if mibBuilder.loadTexts:
    alarmConfEntry.setStatus("current")
_AlarmConfId_Type = Integer32
_AlarmConfId_Object = MibTableColumn
alarmConfId = _AlarmConfId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 2, 2, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 2, 2, 1, 2),
    _AlarmConfFacility_Type()
)
alarmConfFacility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmConfFacility.setStatus("current")
_AlarmConfTarget_Type = Integer32
_AlarmConfTarget_Object = MibTableColumn
alarmConfTarget = _AlarmConfTarget_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 2, 2, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 2, 2, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 2, 2, 1, 5),
    _AlarmConfClearable_Type()
)
alarmConfClearable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmConfClearable.setStatus("current")
_AlarmCurrTable_Object = MibTable
alarmCurrTable = _AlarmCurrTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 2, 3)
)
if mibBuilder.loadTexts:
    alarmCurrTable.setStatus("current")
_AlarmCurrEntry_Object = MibTableRow
alarmCurrEntry = _AlarmCurrEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 2, 3, 1)
)
alarmCurrEntry.setIndexNames(
    (0, "ZYXEL-SAM1216", "alarmCurrIndex"),
)
if mibBuilder.loadTexts:
    alarmCurrEntry.setStatus("current")
_AlarmCurrIndex_Type = Integer32
_AlarmCurrIndex_Object = MibTableColumn
alarmCurrIndex = _AlarmCurrIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 2, 3, 1, 1),
    _AlarmCurrIndex_Type()
)
alarmCurrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmCurrIndex.setStatus("current")
_AlarmCurrOccurTime_Type = TimeTicks
_AlarmCurrOccurTime_Object = MibTableColumn
alarmCurrOccurTime = _AlarmCurrOccurTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 2, 3, 1, 2),
    _AlarmCurrOccurTime_Type()
)
alarmCurrOccurTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmCurrOccurTime.setStatus("current")
_AlarmCurrTrapOid_Type = ObjectIdentifier
_AlarmCurrTrapOid_Object = MibTableColumn
alarmCurrTrapOid = _AlarmCurrTrapOid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 2, 3, 1, 3),
    _AlarmCurrTrapOid_Type()
)
alarmCurrTrapOid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmCurrTrapOid.setStatus("current")
_AlarmCurrParam1_Type = Integer32
_AlarmCurrParam1_Object = MibTableColumn
alarmCurrParam1 = _AlarmCurrParam1_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 2, 3, 1, 4),
    _AlarmCurrParam1_Type()
)
alarmCurrParam1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmCurrParam1.setStatus("current")
_AlarmCurrParam2_Type = Integer32
_AlarmCurrParam2_Object = MibTableColumn
alarmCurrParam2 = _AlarmCurrParam2_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 2, 3, 1, 5),
    _AlarmCurrParam2_Type()
)
alarmCurrParam2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmCurrParam2.setStatus("current")
_AlarmCurrParam3_Type = Integer32
_AlarmCurrParam3_Object = MibTableColumn
alarmCurrParam3 = _AlarmCurrParam3_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 2, 3, 1, 6),
    _AlarmCurrParam3_Type()
)
alarmCurrParam3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmCurrParam3.setStatus("current")
_AlarmCurrParam4_Type = Integer32
_AlarmCurrParam4_Object = MibTableColumn
alarmCurrParam4 = _AlarmCurrParam4_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 2, 3, 1, 7),
    _AlarmCurrParam4_Type()
)
alarmCurrParam4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmCurrParam4.setStatus("current")
_AlarmCurrParam5_Type = Integer32
_AlarmCurrParam5_Object = MibTableColumn
alarmCurrParam5 = _AlarmCurrParam5_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 2, 3, 1, 8),
    _AlarmCurrParam5_Type()
)
alarmCurrParam5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmCurrParam5.setStatus("current")
_AlarmCurrParam6_Type = Integer32
_AlarmCurrParam6_Object = MibTableColumn
alarmCurrParam6 = _AlarmCurrParam6_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 2, 3, 1, 9),
    _AlarmCurrParam6_Type()
)
alarmCurrParam6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmCurrParam6.setStatus("current")
_AlarmCurrParam7_Type = Integer32
_AlarmCurrParam7_Object = MibTableColumn
alarmCurrParam7 = _AlarmCurrParam7_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 2, 3, 1, 10),
    _AlarmCurrParam7_Type()
)
alarmCurrParam7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmCurrParam7.setStatus("current")
_AlarmCurrParam8_Type = Integer32
_AlarmCurrParam8_Object = MibTableColumn
alarmCurrParam8 = _AlarmCurrParam8_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 2, 3, 1, 11),
    _AlarmCurrParam8_Type()
)
alarmCurrParam8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmCurrParam8.setStatus("current")
_AlarmCurrTimeDescr_Type = DisplayString
_AlarmCurrTimeDescr_Object = MibTableColumn
alarmCurrTimeDescr = _AlarmCurrTimeDescr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 2, 3, 1, 12),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 2, 3, 1, 13),
    _AlarmCurrSeverity_Type()
)
alarmCurrSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmCurrSeverity.setStatus("current")
_AlarmCurrDescr_Type = DisplayString
_AlarmCurrDescr_Object = MibTableColumn
alarmCurrDescr = _AlarmCurrDescr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 2, 3, 1, 14),
    _AlarmCurrDescr_Type()
)
alarmCurrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmCurrDescr.setStatus("current")
_AlarmSeverityPortTable_Object = MibTable
alarmSeverityPortTable = _AlarmSeverityPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 2, 4)
)
if mibBuilder.loadTexts:
    alarmSeverityPortTable.setStatus("current")
_AlarmSeverityPortEntry_Object = MibTableRow
alarmSeverityPortEntry = _AlarmSeverityPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 2, 4, 1)
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 2, 4, 1, 1),
    _SeverityThresh_Type()
)
severityThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityThresh.setStatus("current")
_Multicast_ObjectIdentity = ObjectIdentity
multicast = _Multicast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 7)
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 7, 1),
    _IgmpEnable_Type()
)
igmpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpEnable.setStatus("current")
_McastBandwidth_ObjectIdentity = ObjectIdentity
mcastBandwidth = _McastBandwidth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 7, 4)
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 7, 4, 1),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 7, 4, 2),
    _MaxNumOfMcastBw_Type()
)
maxNumOfMcastBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumOfMcastBw.setStatus("current")
_McastBwTable_Object = MibTable
mcastBwTable = _McastBwTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 7, 4, 3)
)
if mibBuilder.loadTexts:
    mcastBwTable.setStatus("current")
_McastBwEntry_Object = MibTableRow
mcastBwEntry = _McastBwEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 7, 4, 3, 1)
)
mcastBwEntry.setIndexNames(
    (0, "ZYXEL-SAM1216", "mcastBwIndex"),
    (0, "ZYXEL-SAM1216", "mcastBwStartIp"),
    (0, "ZYXEL-SAM1216", "mcastBwEndIp"),
)
if mibBuilder.loadTexts:
    mcastBwEntry.setStatus("current")
_McastBwIndex_Type = Integer32
_McastBwIndex_Object = MibTableColumn
mcastBwIndex = _McastBwIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 7, 4, 3, 1, 1),
    _McastBwIndex_Type()
)
mcastBwIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcastBwIndex.setStatus("current")
_McastBwStartIp_Type = IpAddress
_McastBwStartIp_Object = MibTableColumn
mcastBwStartIp = _McastBwStartIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 7, 4, 3, 1, 2),
    _McastBwStartIp_Type()
)
mcastBwStartIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mcastBwStartIp.setStatus("current")
_McastBwEndIp_Type = IpAddress
_McastBwEndIp_Object = MibTableColumn
mcastBwEndIp = _McastBwEndIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 7, 4, 3, 1, 3),
    _McastBwEndIp_Type()
)
mcastBwEndIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mcastBwEndIp.setStatus("current")
_McastBwBandwidth_Type = Integer32
_McastBwBandwidth_Object = MibTableColumn
mcastBwBandwidth = _McastBwBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 7, 4, 3, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 7, 4, 3, 1, 5),
    _McastBwRowStatus_Type()
)
mcastBwRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mcastBwRowStatus.setStatus("current")
_McastBwPortTable_Object = MibTable
mcastBwPortTable = _McastBwPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 7, 4, 4)
)
if mibBuilder.loadTexts:
    mcastBwPortTable.setStatus("current")
_McastBwPortEntry_Object = MibTableRow
mcastBwPortEntry = _McastBwPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 7, 4, 4, 1)
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 7, 4, 4, 1, 1),
    _McastBwPortEnable_Type()
)
mcastBwPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcastBwPortEnable.setStatus("current")
_McastBwPortBandwidth_Type = Integer32
_McastBwPortBandwidth_Object = MibTableColumn
mcastBwPortBandwidth = _McastBwPortBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 7, 4, 4, 1, 2),
    _McastBwPortBandwidth_Type()
)
mcastBwPortBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcastBwPortBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    mcastBwPortBandwidth.setUnits("Kbps")
_IgmpCount_ObjectIdentity = ObjectIdentity
igmpCount = _IgmpCount_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 7, 5)
)
_IgmpCountPortTable_Object = MibTable
igmpCountPortTable = _IgmpCountPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 7, 5, 1)
)
if mibBuilder.loadTexts:
    igmpCountPortTable.setStatus("current")
_IgmpCountPortEntry_Object = MibTableRow
igmpCountPortEntry = _IgmpCountPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 7, 5, 1, 1)
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 7, 5, 1, 1, 1),
    _IgmpCountPortEnable_Type()
)
igmpCountPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpCountPortEnable.setStatus("current")
_IgmpCountPortLimit_Type = Integer32
_IgmpCountPortLimit_Object = MibTableColumn
igmpCountPortLimit = _IgmpCountPortLimit_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 7, 5, 1, 1, 2),
    _IgmpCountPortLimit_Type()
)
igmpCountPortLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpCountPortLimit.setStatus("current")
_Mvlan_ObjectIdentity = ObjectIdentity
mvlan = _Mvlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 7, 6)
)
_MaxNumOfMvlan_Type = Integer32
_MaxNumOfMvlan_Object = MibScalar
maxNumOfMvlan = _MaxNumOfMvlan_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 7, 6, 1),
    _MaxNumOfMvlan_Type()
)
maxNumOfMvlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumOfMvlan.setStatus("current")
_MvlanTable_Object = MibTable
mvlanTable = _MvlanTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 7, 6, 2)
)
if mibBuilder.loadTexts:
    mvlanTable.setStatus("current")
_MvlanEntry_Object = MibTableRow
mvlanEntry = _MvlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 7, 6, 2, 1)
)
mvlanEntry.setIndexNames(
    (0, "ZYXEL-SAM1216", "mvlanIndex"),
)
if mibBuilder.loadTexts:
    mvlanEntry.setStatus("current")
_MvlanIndex_Type = VlanIndex
_MvlanIndex_Object = MibTableColumn
mvlanIndex = _MvlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 7, 6, 2, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 7, 6, 2, 1, 2),
    _MvlanName_Type()
)
mvlanName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mvlanName.setStatus("current")
_MvlanEgressPorts_Type = PortList
_MvlanEgressPorts_Object = MibTableColumn
mvlanEgressPorts = _MvlanEgressPorts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 7, 6, 2, 1, 3),
    _MvlanEgressPorts_Type()
)
mvlanEgressPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mvlanEgressPorts.setStatus("current")
_MvlanUntaggedPorts_Type = PortList
_MvlanUntaggedPorts_Object = MibTableColumn
mvlanUntaggedPorts = _MvlanUntaggedPorts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 7, 6, 2, 1, 4),
    _MvlanUntaggedPorts_Type()
)
mvlanUntaggedPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mvlanUntaggedPorts.setStatus("current")
_MvlanRowStatus_Type = RowStatus
_MvlanRowStatus_Object = MibTableColumn
mvlanRowStatus = _MvlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 7, 6, 2, 1, 5),
    _MvlanRowStatus_Type()
)
mvlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mvlanRowStatus.setStatus("current")
_MvlanTranslateTable_Object = MibTable
mvlanTranslateTable = _MvlanTranslateTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 7, 6, 3)
)
if mibBuilder.loadTexts:
    mvlanTranslateTable.setStatus("current")
_MvlanTranslateEntry_Object = MibTableRow
mvlanTranslateEntry = _MvlanTranslateEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 7, 6, 3, 1)
)
mvlanTranslateEntry.setIndexNames(
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
    (0, "ZYXEL-SAM1216", "mvlanTranslateIndex"),
)
if mibBuilder.loadTexts:
    mvlanTranslateEntry.setStatus("current")
_MvlanTranslateIndex_Type = Integer32
_MvlanTranslateIndex_Object = MibTableColumn
mvlanTranslateIndex = _MvlanTranslateIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 7, 6, 3, 1, 1),
    _MvlanTranslateIndex_Type()
)
mvlanTranslateIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvlanTranslateIndex.setStatus("current")
_MvlanTranslateStartIp_Type = IpAddress
_MvlanTranslateStartIp_Object = MibTableColumn
mvlanTranslateStartIp = _MvlanTranslateStartIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 7, 6, 3, 1, 2),
    _MvlanTranslateStartIp_Type()
)
mvlanTranslateStartIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvlanTranslateStartIp.setStatus("current")
_MvlanTranslateEndIp_Type = IpAddress
_MvlanTranslateEndIp_Object = MibTableColumn
mvlanTranslateEndIp = _MvlanTranslateEndIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 7, 6, 3, 1, 3),
    _MvlanTranslateEndIp_Type()
)
mvlanTranslateEndIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvlanTranslateEndIp.setStatus("current")
_QueryVid_ObjectIdentity = ObjectIdentity
queryVid = _QueryVid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 7, 7)
)


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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 7, 7),
    _IgmpVersion_Type()
)
igmpVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpVersion.setStatus("current")
_MaxNumOfQryVid_Type = Integer32
_MaxNumOfQryVid_Object = MibScalar
maxNumOfQryVid = _MaxNumOfQryVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 7, 7, 1),
    _MaxNumOfQryVid_Type()
)
maxNumOfQryVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumOfQryVid.setStatus("current")
_QryVidConfTable_Object = MibTable
qryVidConfTable = _QryVidConfTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 7, 7, 2)
)
if mibBuilder.loadTexts:
    qryVidConfTable.setStatus("current")
_QryVidConfEntry_Object = MibTableRow
qryVidConfEntry = _QryVidConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 7, 7, 2, 1)
)
qryVidConfEntry.setIndexNames(
    (0, "ZYXEL-SAM1216", "qryVid"),
)
if mibBuilder.loadTexts:
    qryVidConfEntry.setStatus("current")
_QryVid_Type = Integer32
_QryVid_Object = MibTableColumn
qryVid = _QryVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 7, 7, 2, 1, 1),
    _QryVid_Type()
)
qryVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qryVid.setStatus("current")
_QryVidRowStatus_Type = RowStatus
_QryVidRowStatus_Object = MibTableColumn
qryVidRowStatus = _QryVidRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 7, 7, 2, 1, 2),
    _QryVidRowStatus_Type()
)
qryVidRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qryVidRowStatus.setStatus("current")
_QryVidStatusTable_Object = MibTable
qryVidStatusTable = _QryVidStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 7, 7, 3)
)
if mibBuilder.loadTexts:
    qryVidStatusTable.setStatus("current")
_QryVidStatusEntry_Object = MibTableRow
qryVidStatusEntry = _QryVidStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 7, 7, 3, 1)
)
qryVidStatusEntry.setIndexNames(
    (0, "ZYXEL-SAM1216", "qryVid"),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 7, 7, 3, 1, 1),
    _QryVidType_Type()
)
qryVidType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qryVidType.setStatus("current")
_Port_ObjectIdentity = ObjectIdentity
port = _Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8)
)
_SubrPortTable_Object = MibTable
subrPortTable = _SubrPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 1)
)
if mibBuilder.loadTexts:
    subrPortTable.setStatus("current")
_SubrPortEntry_Object = MibTableRow
subrPortEntry = _SubrPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 1, 1)
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 1, 1, 2),
    _SubrPortTel_Type()
)
subrPortTel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subrPortTel.setStatus("current")
_ShdslPort_ObjectIdentity = ObjectIdentity
shdslPort = _ShdslPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 3)
)
_ShdslLineConfTable_Object = MibTable
shdslLineConfTable = _ShdslLineConfTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 3, 1)
)
if mibBuilder.loadTexts:
    shdslLineConfTable.setStatus("current")
_ShdslLineConfEntry_Object = MibTableRow
shdslLineConfEntry = _ShdslLineConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 3, 1, 1)
)
shdslLineConfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    shdslLineConfEntry.setStatus("current")


class _ShdslLineConfShdslMode_Type(Integer32):
    """Custom type shdslLineConfShdslMode based on Integer32"""
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
        *(("stuc", 1),
          ("stur", 2),
          ("auto", 3),
          ("pam16", 4),
          ("pam32", 5))
    )


_ShdslLineConfShdslMode_Type.__name__ = "Integer32"
_ShdslLineConfShdslMode_Object = MibTableColumn
shdslLineConfShdslMode = _ShdslLineConfShdslMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 3, 1, 1, 1),
    _ShdslLineConfShdslMode_Type()
)
shdslLineConfShdslMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shdslLineConfShdslMode.setStatus("current")


class _ShdslLineConfPmms_Type(Integer32):
    """Custom type shdslLineConfPmms based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("forced", 2))
    )


_ShdslLineConfPmms_Type.__name__ = "Integer32"
_ShdslLineConfPmms_Object = MibTableColumn
shdslLineConfPmms = _ShdslLineConfPmms_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 3, 1, 1, 2),
    _ShdslLineConfPmms_Type()
)
shdslLineConfPmms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shdslLineConfPmms.setStatus("current")


class _ShdslLineConfPboMode_Type(Integer32):
    """Custom type shdslLineConfPboMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normalepl", 1),
          ("forcedepl", 2),
          ("forcednoepl", 3))
    )


_ShdslLineConfPboMode_Type.__name__ = "Integer32"
_ShdslLineConfPboMode_Object = MibTableColumn
shdslLineConfPboMode = _ShdslLineConfPboMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 3, 1, 1, 3),
    _ShdslLineConfPboMode_Type()
)
shdslLineConfPboMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shdslLineConfPboMode.setStatus("current")


class _ShdslLineConfPboValue_Type(Integer32):
    """Custom type shdslLineConfPboValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_ShdslLineConfPboValue_Type.__name__ = "Integer32"
_ShdslLineConfPboValue_Object = MibTableColumn
shdslLineConfPboValue = _ShdslLineConfPboValue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 3, 1, 1, 4),
    _ShdslLineConfPboValue_Type()
)
shdslLineConfPboValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shdslLineConfPboValue.setStatus("current")
if mibBuilder.loadTexts:
    shdslLineConfPboValue.setUnits("dB")


class _ShdslLineConfShdslTCMode_Type(Integer32):
    """Custom type shdslLineConfShdslTCMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("atm", 1),
          ("efm", 2))
    )


_ShdslLineConfShdslTCMode_Type.__name__ = "Integer32"
_ShdslLineConfShdslTCMode_Object = MibTableColumn
shdslLineConfShdslTCMode = _ShdslLineConfShdslTCMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 3, 1, 1, 5),
    _ShdslLineConfShdslTCMode_Type()
)
shdslLineConfShdslTCMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shdslLineConfShdslTCMode.setStatus("current")
_ShdslPortBatchSet_ObjectIdentity = ObjectIdentity
shdslPortBatchSet = _ShdslPortBatchSet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 3, 2)
)
_ShdslPortTarget_Type = OctetString
_ShdslPortTarget_Object = MibScalar
shdslPortTarget = _ShdslPortTarget_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 3, 2, 1),
    _ShdslPortTarget_Type()
)
shdslPortTarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shdslPortTarget.setStatus("current")
_ShdslPortOps_Type = Integer32
_ShdslPortOps_Object = MibScalar
shdslPortOps = _ShdslPortOps_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 3, 2, 2),
    _ShdslPortOps_Type()
)
shdslPortOps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shdslPortOps.setStatus("current")


class _ShdslModeForBatchSet_Type(Integer32):
    """Custom type shdslModeForBatchSet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stuc", 1),
          ("stur", 2))
    )


_ShdslModeForBatchSet_Type.__name__ = "Integer32"
_ShdslModeForBatchSet_Object = MibScalar
shdslModeForBatchSet = _ShdslModeForBatchSet_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 3, 2, 3),
    _ShdslModeForBatchSet_Type()
)
shdslModeForBatchSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shdslModeForBatchSet.setStatus("current")


class _ShdslLineProfileForBatchSet_Type(DisplayString):
    """Custom type shdslLineProfileForBatchSet based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_ShdslLineProfileForBatchSet_Type.__name__ = "DisplayString"
_ShdslLineProfileForBatchSet_Object = MibScalar
shdslLineProfileForBatchSet = _ShdslLineProfileForBatchSet_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 3, 2, 4),
    _ShdslLineProfileForBatchSet_Type()
)
shdslLineProfileForBatchSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shdslLineProfileForBatchSet.setStatus("current")


class _ShdslAlarmProfileForBatchSet_Type(DisplayString):
    """Custom type shdslAlarmProfileForBatchSet based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_ShdslAlarmProfileForBatchSet_Type.__name__ = "DisplayString"
_ShdslAlarmProfileForBatchSet_Object = MibScalar
shdslAlarmProfileForBatchSet = _ShdslAlarmProfileForBatchSet_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 3, 2, 5),
    _ShdslAlarmProfileForBatchSet_Type()
)
shdslAlarmProfileForBatchSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shdslAlarmProfileForBatchSet.setStatus("current")


class _ShdslPboValueForBatchSet_Type(Integer32):
    """Custom type shdslPboValueForBatchSet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_ShdslPboValueForBatchSet_Type.__name__ = "Integer32"
_ShdslPboValueForBatchSet_Object = MibScalar
shdslPboValueForBatchSet = _ShdslPboValueForBatchSet_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 3, 2, 6),
    _ShdslPboValueForBatchSet_Type()
)
shdslPboValueForBatchSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shdslPboValueForBatchSet.setStatus("current")
if mibBuilder.loadTexts:
    shdslPboValueForBatchSet.setUnits("dB")
_Pvc_ObjectIdentity = ObjectIdentity
pvc = _Pvc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 4)
)
_MaxNumOfPvcs_Type = Integer32
_MaxNumOfPvcs_Object = MibScalar
maxNumOfPvcs = _MaxNumOfPvcs_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 4, 1),
    _MaxNumOfPvcs_Type()
)
maxNumOfPvcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumOfPvcs.setStatus("current")
_PvcTable_Object = MibTable
pvcTable = _PvcTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 4, 2)
)
if mibBuilder.loadTexts:
    pvcTable.setStatus("current")
_PvcEntry_Object = MibTableRow
pvcEntry = _PvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 4, 2, 1)
)
pvcEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZYXEL-SAM1216", "pvcVpi"),
    (0, "ZYXEL-SAM1216", "pvcVci"),
    (0, "ZYXEL-SAM1216", "pvcPvid"),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 4, 2, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 4, 2, 1, 2),
    _PvcVci_Type()
)
pvcVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcVci.setStatus("current")
_PvcPvid_Type = VlanIndex
_PvcPvid_Object = MibTableColumn
pvcPvid = _PvcPvid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 4, 2, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 4, 2, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 4, 2, 1, 6),
    _PvcProfileDS_Type()
)
pvcProfileDS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvcProfileDS.setStatus("current")
_PvcRowStatus_Type = RowStatus
_PvcRowStatus_Object = MibTableColumn
pvcRowStatus = _PvcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 4, 2, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 4, 2, 1, 8),
    _PvcProfileUS_Type()
)
pvcProfileUS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvcProfileUS.setStatus("current")
_PvcUsRateLimitTable_Object = MibTable
pvcUsRateLimitTable = _PvcUsRateLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 4, 4)
)
if mibBuilder.loadTexts:
    pvcUsRateLimitTable.setStatus("current")
_PvcUsRateLimitEntry_Object = MibTableRow
pvcUsRateLimitEntry = _PvcUsRateLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 4, 4, 1)
)
pvcUsRateLimitEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZYXEL-SAM1216", "pvcVpi"),
    (0, "ZYXEL-SAM1216", "pvcVci"),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 4, 4, 1, 1),
    _PvcUsRateLimitEnable_Type()
)
pvcUsRateLimitEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcUsRateLimitEnable.setStatus("current")
_PvcUsRateLimit_Type = Integer32
_PvcUsRateLimit_Object = MibTableColumn
pvcUsRateLimit = _PvcUsRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 4, 4, 1, 2),
    _PvcUsRateLimit_Type()
)
pvcUsRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcUsRateLimit.setStatus("current")
if mibBuilder.loadTexts:
    pvcUsRateLimit.setUnits("Kbps")
_Ppvc_ObjectIdentity = ObjectIdentity
ppvc = _Ppvc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 5)
)
_MaxNumOfPriorityPvcs_Type = Integer32
_MaxNumOfPriorityPvcs_Object = MibScalar
maxNumOfPriorityPvcs = _MaxNumOfPriorityPvcs_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 5, 1),
    _MaxNumOfPriorityPvcs_Type()
)
maxNumOfPriorityPvcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumOfPriorityPvcs.setStatus("current")
_PpvcTable_Object = MibTable
ppvcTable = _PpvcTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 5, 2)
)
if mibBuilder.loadTexts:
    ppvcTable.setStatus("current")
_PpvcEntry_Object = MibTableRow
ppvcEntry = _PpvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 5, 2, 1)
)
ppvcEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZYXEL-SAM1216", "ppvcVpi"),
    (0, "ZYXEL-SAM1216", "ppvcVci"),
    (0, "ZYXEL-SAM1216", "ppvcPvid"),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 5, 2, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 5, 2, 1, 2),
    _PpvcVci_Type()
)
ppvcVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppvcVci.setStatus("current")
_PpvcPvid_Type = VlanIndex
_PpvcPvid_Object = MibTableColumn
ppvcPvid = _PpvcPvid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 5, 2, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 5, 2, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 5, 2, 1, 5),
    _PpvcPriority_Type()
)
ppvcPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ppvcPriority.setStatus("current")
_PpvcRowStatus_Type = RowStatus
_PpvcRowStatus_Object = MibTableColumn
ppvcRowStatus = _PpvcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 5, 2, 1, 6),
    _PpvcRowStatus_Type()
)
ppvcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ppvcRowStatus.setStatus("current")
_PpvcMemberTable_Object = MibTable
ppvcMemberTable = _PpvcMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 5, 4)
)
if mibBuilder.loadTexts:
    ppvcMemberTable.setStatus("current")
_PpvcMemberEntry_Object = MibTableRow
ppvcMemberEntry = _PpvcMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 5, 4, 1)
)
ppvcMemberEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZYXEL-SAM1216", "ppvcVpi"),
    (0, "ZYXEL-SAM1216", "ppvcVci"),
    (0, "ZYXEL-SAM1216", "ppvcMemberVpi"),
    (0, "ZYXEL-SAM1216", "ppvcMemberVci"),
    (0, "ZYXEL-SAM1216", "ppvcMemberPriority"),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 5, 4, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 5, 4, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 5, 4, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 5, 4, 1, 4),
    _PpvcMemberProfileDS_Type()
)
ppvcMemberProfileDS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ppvcMemberProfileDS.setStatus("current")
_PpvcMemberRowStatus_Type = RowStatus
_PpvcMemberRowStatus_Object = MibTableColumn
ppvcMemberRowStatus = _PpvcMemberRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 5, 4, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 5, 4, 1, 6),
    _PpvcMemberProfileUS_Type()
)
ppvcMemberProfileUS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ppvcMemberProfileUS.setStatus("current")
_PortOperation_ObjectIdentity = ObjectIdentity
portOperation = _PortOperation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 6)
)
_PortTarget_Type = OctetString
_PortTarget_Object = MibScalar
portTarget = _PortTarget_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 6, 1),
    _PortTarget_Type()
)
portTarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portTarget.setStatus("current")
_PortOps_Type = Integer32
_PortOps_Object = MibScalar
portOps = _PortOps_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 6, 2),
    _PortOps_Type()
)
portOps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portOps.setStatus("current")
_Rpvc_ObjectIdentity = ObjectIdentity
rpvc = _Rpvc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 8)
)
_RpvcGatewayTable_Object = MibTable
rpvcGatewayTable = _RpvcGatewayTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 8, 1)
)
if mibBuilder.loadTexts:
    rpvcGatewayTable.setStatus("current")
_RpvcGatewayEntry_Object = MibTableRow
rpvcGatewayEntry = _RpvcGatewayEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 8, 1, 1)
)
rpvcGatewayEntry.setIndexNames(
    (0, "ZYXEL-SAM1216", "rpvcGatewayIp"),
)
if mibBuilder.loadTexts:
    rpvcGatewayEntry.setStatus("current")
_RpvcGatewayIp_Type = IpAddress
_RpvcGatewayIp_Object = MibTableColumn
rpvcGatewayIp = _RpvcGatewayIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 8, 1, 1, 1),
    _RpvcGatewayIp_Type()
)
rpvcGatewayIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpvcGatewayIp.setStatus("current")
_RpvcGatewayVlanId_Type = VlanIndex
_RpvcGatewayVlanId_Object = MibTableColumn
rpvcGatewayVlanId = _RpvcGatewayVlanId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 8, 1, 1, 2),
    _RpvcGatewayVlanId_Type()
)
rpvcGatewayVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rpvcGatewayVlanId.setStatus("current")
_RpvcGatewayRowStatus_Type = RowStatus
_RpvcGatewayRowStatus_Object = MibTableColumn
rpvcGatewayRowStatus = _RpvcGatewayRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 8, 1, 1, 3),
    _RpvcGatewayRowStatus_Type()
)
rpvcGatewayRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rpvcGatewayRowStatus.setStatus("current")
_RpvcGatewayPriority_Type = Integer32
_RpvcGatewayPriority_Object = MibTableColumn
rpvcGatewayPriority = _RpvcGatewayPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 8, 1, 1, 4),
    _RpvcGatewayPriority_Type()
)
rpvcGatewayPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rpvcGatewayPriority.setStatus("current")
_RpvcTable_Object = MibTable
rpvcTable = _RpvcTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 8, 2)
)
if mibBuilder.loadTexts:
    rpvcTable.setStatus("current")
_RpvcTableEntry_Object = MibTableRow
rpvcTableEntry = _RpvcTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 8, 2, 1)
)
rpvcTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZYXEL-SAM1216", "rpvcVpi"),
    (0, "ZYXEL-SAM1216", "rpvcVci"),
    (0, "ZYXEL-SAM1216", "rpvcIp"),
    (0, "ZYXEL-SAM1216", "rpvcNetmask"),
)
if mibBuilder.loadTexts:
    rpvcTableEntry.setStatus("current")


class _RpvcVpi_Type(Integer32):
    """Custom type rpvcVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RpvcVpi_Type.__name__ = "Integer32"
_RpvcVpi_Object = MibTableColumn
rpvcVpi = _RpvcVpi_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 8, 2, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 8, 2, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 8, 2, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 8, 2, 1, 4),
    _RpvcUSProfile_Type()
)
rpvcUSProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rpvcUSProfile.setStatus("current")
_RpvcIp_Type = IpAddress
_RpvcIp_Object = MibTableColumn
rpvcIp = _RpvcIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 8, 2, 1, 5),
    _RpvcIp_Type()
)
rpvcIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpvcIp.setStatus("current")
_RpvcNetmask_Type = IpAddress
_RpvcNetmask_Object = MibTableColumn
rpvcNetmask = _RpvcNetmask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 8, 2, 1, 6),
    _RpvcNetmask_Type()
)
rpvcNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpvcNetmask.setStatus("current")
_RpvcGatewayIpAddress_Type = IpAddress
_RpvcGatewayIpAddress_Object = MibTableColumn
rpvcGatewayIpAddress = _RpvcGatewayIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 8, 2, 1, 7),
    _RpvcGatewayIpAddress_Type()
)
rpvcGatewayIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rpvcGatewayIpAddress.setStatus("current")
_RpvcRowStatus_Type = RowStatus
_RpvcRowStatus_Object = MibTableColumn
rpvcRowStatus = _RpvcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 8, 2, 1, 8),
    _RpvcRowStatus_Type()
)
rpvcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rpvcRowStatus.setStatus("current")
_RpvcRouteDomainTable_Object = MibTable
rpvcRouteDomainTable = _RpvcRouteDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 8, 3)
)
if mibBuilder.loadTexts:
    rpvcRouteDomainTable.setStatus("current")
_RpvcRouteDomainTableEntry_Object = MibTableRow
rpvcRouteDomainTableEntry = _RpvcRouteDomainTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 8, 3, 1)
)
rpvcRouteDomainTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZYXEL-SAM1216", "rpvcRouteDomainVpi"),
    (0, "ZYXEL-SAM1216", "rpvcRouteDomainVci"),
    (0, "ZYXEL-SAM1216", "rpvcRouteDomainIp"),
    (0, "ZYXEL-SAM1216", "rpvcRouteDomainNetmask"),
)
if mibBuilder.loadTexts:
    rpvcRouteDomainTableEntry.setStatus("current")


class _RpvcRouteDomainVpi_Type(Integer32):
    """Custom type rpvcRouteDomainVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RpvcRouteDomainVpi_Type.__name__ = "Integer32"
_RpvcRouteDomainVpi_Object = MibTableColumn
rpvcRouteDomainVpi = _RpvcRouteDomainVpi_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 8, 3, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 8, 3, 1, 2),
    _RpvcRouteDomainVci_Type()
)
rpvcRouteDomainVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpvcRouteDomainVci.setStatus("current")
_RpvcRouteDomainIp_Type = IpAddress
_RpvcRouteDomainIp_Object = MibTableColumn
rpvcRouteDomainIp = _RpvcRouteDomainIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 8, 3, 1, 3),
    _RpvcRouteDomainIp_Type()
)
rpvcRouteDomainIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpvcRouteDomainIp.setStatus("current")
_RpvcRouteDomainNetmask_Type = IpAddress
_RpvcRouteDomainNetmask_Object = MibTableColumn
rpvcRouteDomainNetmask = _RpvcRouteDomainNetmask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 8, 3, 1, 4),
    _RpvcRouteDomainNetmask_Type()
)
rpvcRouteDomainNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpvcRouteDomainNetmask.setStatus("current")
_RpvcRouteDomainRowStatus_Type = RowStatus
_RpvcRouteDomainRowStatus_Object = MibTableColumn
rpvcRouteDomainRowStatus = _RpvcRouteDomainRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 8, 3, 1, 5),
    _RpvcRouteDomainRowStatus_Type()
)
rpvcRouteDomainRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rpvcRouteDomainRowStatus.setStatus("current")
_RpvcArpAgingTime_Type = Integer32
_RpvcArpAgingTime_Object = MibScalar
rpvcArpAgingTime = _RpvcArpAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 8, 4),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 8, 5),
    _RpvcArpFlush_Type()
)
rpvcArpFlush.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rpvcArpFlush.setStatus("current")
_DsBcastDisableTable_Object = MibTable
dsBcastDisableTable = _DsBcastDisableTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 9)
)
if mibBuilder.loadTexts:
    dsBcastDisableTable.setStatus("current")
_DsBcastDisableEntry_Object = MibTableRow
dsBcastDisableEntry = _DsBcastDisableEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 9, 1)
)
dsBcastDisableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZYXEL-SAM1216", "dsBcastDisableVlanId"),
)
if mibBuilder.loadTexts:
    dsBcastDisableEntry.setStatus("current")
_DsBcastDisableVlanId_Type = Integer32
_DsBcastDisableVlanId_Object = MibTableColumn
dsBcastDisableVlanId = _DsBcastDisableVlanId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 9, 1, 1),
    _DsBcastDisableVlanId_Type()
)
dsBcastDisableVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsBcastDisableVlanId.setStatus("current")
_DsBcastDisableRowStatus_Type = RowStatus
_DsBcastDisableRowStatus_Object = MibTableColumn
dsBcastDisableRowStatus = _DsBcastDisableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 9, 1, 2),
    _DsBcastDisableRowStatus_Type()
)
dsBcastDisableRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsBcastDisableRowStatus.setStatus("current")
_Paepvc_ObjectIdentity = ObjectIdentity
paepvc = _Paepvc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 10)
)
_PaepvcTable_Object = MibTable
paepvcTable = _PaepvcTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 10, 1)
)
if mibBuilder.loadTexts:
    paepvcTable.setStatus("current")
_PaepvcEntry_Object = MibTableRow
paepvcEntry = _PaepvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 10, 1, 1)
)
paepvcEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZYXEL-SAM1216", "paepvcVpi"),
    (0, "ZYXEL-SAM1216", "paepvcVci"),
    (0, "ZYXEL-SAM1216", "paepvcPvid"),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 10, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 10, 1, 1, 2),
    _PaepvcVci_Type()
)
paepvcVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcVci.setStatus("current")
_PaepvcPvid_Type = VlanIndex
_PaepvcPvid_Object = MibTableColumn
paepvcPvid = _PaepvcPvid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 10, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 10, 1, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 10, 1, 1, 6),
    _PaepvcProfileDS_Type()
)
paepvcProfileDS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    paepvcProfileDS.setStatus("current")
_PaepvcAcName_Type = DisplayString
_PaepvcAcName_Object = MibTableColumn
paepvcAcName = _PaepvcAcName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 10, 1, 1, 7),
    _PaepvcAcName_Type()
)
paepvcAcName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    paepvcAcName.setStatus("current")
_PaepvcServiceName_Type = DisplayString
_PaepvcServiceName_Object = MibTableColumn
paepvcServiceName = _PaepvcServiceName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 10, 1, 1, 8),
    _PaepvcServiceName_Type()
)
paepvcServiceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    paepvcServiceName.setStatus("current")
_PaepvcHelloTime_Type = Integer32
_PaepvcHelloTime_Object = MibTableColumn
paepvcHelloTime = _PaepvcHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 10, 1, 1, 9),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 10, 1, 1, 10),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 10, 1, 1, 11),
    _PaepvcProfileUS_Type()
)
paepvcProfileUS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    paepvcProfileUS.setStatus("current")
_Tlspvc_ObjectIdentity = ObjectIdentity
tlspvc = _Tlspvc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 11)
)
_TlspvcTable_Object = MibTable
tlspvcTable = _TlspvcTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 11, 1)
)
if mibBuilder.loadTexts:
    tlspvcTable.setStatus("current")
_TlspvcEntry_Object = MibTableRow
tlspvcEntry = _TlspvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 11, 1, 1)
)
tlspvcEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZYXEL-SAM1216", "tlspvcVpi"),
    (0, "ZYXEL-SAM1216", "tlspvcVci"),
    (0, "ZYXEL-SAM1216", "tlspvcSvid"),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 11, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 11, 1, 1, 2),
    _TlspvcVci_Type()
)
tlspvcVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlspvcVci.setStatus("current")
_TlspvcSvid_Type = VlanIndex
_TlspvcSvid_Object = MibTableColumn
tlspvcSvid = _TlspvcSvid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 11, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 11, 1, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 11, 1, 1, 6),
    _TlspvcProfileDS_Type()
)
tlspvcProfileDS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tlspvcProfileDS.setStatus("current")
_TlspvcRowStatus_Type = RowStatus
_TlspvcRowStatus_Object = MibTableColumn
tlspvcRowStatus = _TlspvcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 11, 1, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 11, 1, 1, 8),
    _TlspvcProfileUS_Type()
)
tlspvcProfileUS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tlspvcProfileUS.setStatus("current")
_Gbond_ObjectIdentity = ObjectIdentity
gbond = _Gbond_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 51)
)
_GbondGroupTable_Object = MibTable
gbondGroupTable = _GbondGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 51, 1)
)
if mibBuilder.loadTexts:
    gbondGroupTable.setStatus("current")
_GbondGroupEntry_Object = MibTableRow
gbondGroupEntry = _GbondGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 51, 1, 1)
)
gbondGroupEntry.setIndexNames(
    (0, "ZYXEL-SAM1216", "gbondGroupName"),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 51, 1, 1, 1),
    _GbondGroupName_Type()
)
gbondGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gbondGroupName.setStatus("current")
_GbondGroupPorts_Type = OctetString
_GbondGroupPorts_Object = MibTableColumn
gbondGroupPorts = _GbondGroupPorts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 51, 1, 1, 2),
    _GbondGroupPorts_Type()
)
gbondGroupPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gbondGroupPorts.setStatus("current")


class _GbondGroupSid_Type(Integer32):
    """Custom type gbondGroupSid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sid8", 1),
          ("sid12", 2))
    )


_GbondGroupSid_Type.__name__ = "Integer32"
_GbondGroupSid_Object = MibTableColumn
gbondGroupSid = _GbondGroupSid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 51, 1, 1, 3),
    _GbondGroupSid_Type()
)
gbondGroupSid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gbondGroupSid.setStatus("current")
_GbondGroupUpRate_Type = Unsigned32
_GbondGroupUpRate_Object = MibTableColumn
gbondGroupUpRate = _GbondGroupUpRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 51, 1, 1, 4),
    _GbondGroupUpRate_Type()
)
gbondGroupUpRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gbondGroupUpRate.setStatus("current")
_GbondGroupDownRate_Type = Unsigned32
_GbondGroupDownRate_Object = MibTableColumn
gbondGroupDownRate = _GbondGroupDownRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 51, 1, 1, 5),
    _GbondGroupDownRate_Type()
)
gbondGroupDownRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gbondGroupDownRate.setStatus("current")
_GbondGroupRowStatus_Type = RowStatus
_GbondGroupRowStatus_Object = MibTableColumn
gbondGroupRowStatus = _GbondGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 8, 51, 1, 1, 6),
    _GbondGroupRowStatus_Type()
)
gbondGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gbondGroupRowStatus.setStatus("current")
_Switch_ObjectIdentity = ObjectIdentity
switch = _Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10)
)
_Dscp_ObjectIdentity = ObjectIdentity
dscp = _Dscp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 10)
)
_DscpMappingTable_Object = MibTable
dscpMappingTable = _DscpMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 10, 1)
)
if mibBuilder.loadTexts:
    dscpMappingTable.setStatus("current")
_DscpMappingEntry_Object = MibTableRow
dscpMappingEntry = _DscpMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 10, 1, 1)
)
dscpMappingEntry.setIndexNames(
    (0, "ZYXEL-SAM1216", "dscpSrcCodePoint"),
)
if mibBuilder.loadTexts:
    dscpMappingEntry.setStatus("current")
_DscpSrcCodePoint_Type = Integer32
_DscpSrcCodePoint_Object = MibTableColumn
dscpSrcCodePoint = _DscpSrcCodePoint_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 10, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 10, 1, 1, 3),
    _DscpMapPriority_Type()
)
dscpMapPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dscpMapPriority.setStatus("current")
_DscpPortTable_Object = MibTable
dscpPortTable = _DscpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 10, 2)
)
if mibBuilder.loadTexts:
    dscpPortTable.setStatus("current")
_DscpPortEntry_Object = MibTableRow
dscpPortEntry = _DscpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 10, 2, 1)
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 10, 2, 1, 1),
    _DscpStatusEnable_Type()
)
dscpStatusEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dscpStatusEnable.setStatus("current")
_VlanIsolation_ObjectIdentity = ObjectIdentity
vlanIsolation = _VlanIsolation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 12)
)
_VlanIsolationTable_Object = MibTable
vlanIsolationTable = _VlanIsolationTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 12, 1)
)
if mibBuilder.loadTexts:
    vlanIsolationTable.setStatus("current")
_VlanIsolationEntry_Object = MibTableRow
vlanIsolationEntry = _VlanIsolationEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 12, 1, 1)
)
vlanIsolationEntry.setIndexNames(
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
)
if mibBuilder.loadTexts:
    vlanIsolationEntry.setStatus("current")
_VlanIsolationRowStatus_Type = RowStatus
_VlanIsolationRowStatus_Object = MibTableColumn
vlanIsolationRowStatus = _VlanIsolationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 12, 1, 1, 1),
    _VlanIsolationRowStatus_Type()
)
vlanIsolationRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanIsolationRowStatus.setStatus("current")
_EnetMtu_ObjectIdentity = ObjectIdentity
enetMtu = _EnetMtu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 13)
)
_EnetMaxMtu_Type = Integer32
_EnetMaxMtu_Object = MibScalar
enetMaxMtu = _EnetMaxMtu_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 13, 1),
    _EnetMaxMtu_Type()
)
enetMaxMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enetMaxMtu.setStatus("current")
_Dhcp_ObjectIdentity = ObjectIdentity
dhcp = _Dhcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 51)
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 51, 1),
    _DhcpRelayEnable_Type()
)
dhcpRelayEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelayEnable.setStatus("current")
_DhcpRelay82Table_Object = MibTable
dhcpRelay82Table = _DhcpRelay82Table_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 51, 2)
)
if mibBuilder.loadTexts:
    dhcpRelay82Table.setStatus("current")
_DhcpRelay82Entry_Object = MibTableRow
dhcpRelay82Entry = _DhcpRelay82Entry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 51, 2, 1)
)
dhcpRelay82Entry.setIndexNames(
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
)
if mibBuilder.loadTexts:
    dhcpRelay82Entry.setStatus("current")
_DhcpRelay82PrimaryServer_Type = IpAddress
_DhcpRelay82PrimaryServer_Object = MibTableColumn
dhcpRelay82PrimaryServer = _DhcpRelay82PrimaryServer_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 51, 2, 1, 1),
    _DhcpRelay82PrimaryServer_Type()
)
dhcpRelay82PrimaryServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelay82PrimaryServer.setStatus("current")
_DhcpRelay82SecondaryServer_Type = IpAddress
_DhcpRelay82SecondaryServer_Object = MibTableColumn
dhcpRelay82SecondaryServer = _DhcpRelay82SecondaryServer_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 51, 2, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 51, 2, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 51, 2, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 51, 2, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 51, 2, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 51, 2, 1, 8),
    _DhcpRelay82Suboption2Enable_Type()
)
dhcpRelay82Suboption2Enable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpRelay82Suboption2Enable.setStatus("current")
_DhcpRelay82Suboption2Info_Type = DisplayString
_DhcpRelay82Suboption2Info_Object = MibTableColumn
dhcpRelay82Suboption2Info = _DhcpRelay82Suboption2Info_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 51, 2, 1, 9),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 51, 2, 1, 10),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 51, 2, 1, 11),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 51, 3),
    _DhcpRelayOption82Sub1Info_Type()
)
dhcpRelayOption82Sub1Info.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelayOption82Sub1Info.setStatus("current")
_MaxNumOfDhcpRelay82Conf_Type = Integer32
_MaxNumOfDhcpRelay82Conf_Object = MibScalar
maxNumOfDhcpRelay82Conf = _MaxNumOfDhcpRelay82Conf_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 51, 4),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 51, 5),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 51, 6),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 51, 7),
    _DhcpRelayOption82Sub2Enable_Type()
)
dhcpRelayOption82Sub2Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelayOption82Sub2Enable.setStatus("current")
_Macfilter_ObjectIdentity = ObjectIdentity
macfilter = _Macfilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 53)
)
_MacFilterPortTable_Object = MibTable
macFilterPortTable = _MacFilterPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 53, 1)
)
if mibBuilder.loadTexts:
    macFilterPortTable.setStatus("current")
_MacFilterPortEntry_Object = MibTableRow
macFilterPortEntry = _MacFilterPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 53, 1, 1)
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 53, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 53, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 53, 1, 1, 3),
    _MacFilterPortFilterMode_Type()
)
macFilterPortFilterMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macFilterPortFilterMode.setStatus("current")
_MaxNumOfMacFiltersInSystem_Type = Integer32
_MaxNumOfMacFiltersInSystem_Object = MibScalar
maxNumOfMacFiltersInSystem = _MaxNumOfMacFiltersInSystem_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 53, 2),
    _MaxNumOfMacFiltersInSystem_Type()
)
maxNumOfMacFiltersInSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumOfMacFiltersInSystem.setStatus("current")
_MaxNumOfMacFiltersPerPort_Type = Integer32
_MaxNumOfMacFiltersPerPort_Object = MibScalar
maxNumOfMacFiltersPerPort = _MaxNumOfMacFiltersPerPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 53, 3),
    _MaxNumOfMacFiltersPerPort_Type()
)
maxNumOfMacFiltersPerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumOfMacFiltersPerPort.setStatus("current")
_CurrNumOfMacFiltersInSystem_Type = Integer32
_CurrNumOfMacFiltersInSystem_Object = MibScalar
currNumOfMacFiltersInSystem = _CurrNumOfMacFiltersInSystem_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 53, 4),
    _CurrNumOfMacFiltersInSystem_Type()
)
currNumOfMacFiltersInSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currNumOfMacFiltersInSystem.setStatus("current")
_MacFilterTable_Object = MibTable
macFilterTable = _MacFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 53, 5)
)
if mibBuilder.loadTexts:
    macFilterTable.setStatus("current")
_MacFilterEntry_Object = MibTableRow
macFilterEntry = _MacFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 53, 5, 1)
)
macFilterEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZYXEL-SAM1216", "macFilterAddr"),
)
if mibBuilder.loadTexts:
    macFilterEntry.setStatus("current")
_MacFilterAddr_Type = PhysAddress
_MacFilterAddr_Object = MibTableColumn
macFilterAddr = _MacFilterAddr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 53, 5, 1, 1),
    _MacFilterAddr_Type()
)
macFilterAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macFilterAddr.setStatus("current")
_MacFilterRowStatus_Type = RowStatus
_MacFilterRowStatus_Object = MibTableColumn
macFilterRowStatus = _MacFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 53, 5, 1, 2),
    _MacFilterRowStatus_Type()
)
macFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    macFilterRowStatus.setStatus("current")
_MacfilterBatchSet_ObjectIdentity = ObjectIdentity
macfilterBatchSet = _MacfilterBatchSet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 53, 6)
)
_MacfilterTarget_Type = OctetString
_MacfilterTarget_Object = MibScalar
macfilterTarget = _MacfilterTarget_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 53, 6, 1),
    _MacfilterTarget_Type()
)
macfilterTarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macfilterTarget.setStatus("current")
_MacfilterOps_Type = Integer32
_MacfilterOps_Object = MibScalar
macfilterOps = _MacfilterOps_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 53, 6, 2),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 53, 6, 3),
    _MacFilterMacCountForBatchSet_Type()
)
macFilterMacCountForBatchSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macFilterMacCountForBatchSet.setStatus("current")
_OuiFilterTable_Object = MibTable
ouiFilterTable = _OuiFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 53, 7)
)
if mibBuilder.loadTexts:
    ouiFilterTable.setStatus("current")
_OuiFilterEntry_Object = MibTableRow
ouiFilterEntry = _OuiFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 53, 7, 1)
)
ouiFilterEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZYXEL-SAM1216", "ouiFilterAddr"),
)
if mibBuilder.loadTexts:
    ouiFilterEntry.setStatus("current")
_OuiFilterAddr_Type = OctetString
_OuiFilterAddr_Object = MibTableColumn
ouiFilterAddr = _OuiFilterAddr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 53, 7, 1, 1),
    _OuiFilterAddr_Type()
)
ouiFilterAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ouiFilterAddr.setStatus("current")
_OuiFilterRowStatus_Type = RowStatus
_OuiFilterRowStatus_Object = MibTableColumn
ouiFilterRowStatus = _OuiFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 53, 7, 1, 2),
    _OuiFilterRowStatus_Type()
)
ouiFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ouiFilterRowStatus.setStatus("current")
_MaxNumOfOuiFiltersPerPort_Type = Integer32
_MaxNumOfOuiFiltersPerPort_Object = MibScalar
maxNumOfOuiFiltersPerPort = _MaxNumOfOuiFiltersPerPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 53, 8),
    _MaxNumOfOuiFiltersPerPort_Type()
)
maxNumOfOuiFiltersPerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumOfOuiFiltersPerPort.setStatus("current")
_OuiFilterPortTable_Object = MibTable
ouiFilterPortTable = _OuiFilterPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 53, 9)
)
if mibBuilder.loadTexts:
    ouiFilterPortTable.setStatus("current")
_OuiFilterPortEntry_Object = MibTableRow
ouiFilterPortEntry = _OuiFilterPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 53, 9, 1)
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 53, 9, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 53, 9, 1, 2),
    _OuiFilterPortFilterMode_Type()
)
ouiFilterPortFilterMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ouiFilterPortFilterMode.setStatus("current")
_DhcpSnoop_ObjectIdentity = ObjectIdentity
dhcpSnoop = _DhcpSnoop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 55)
)
_DhcpSnoopPortTable_Object = MibTable
dhcpSnoopPortTable = _DhcpSnoopPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 55, 1)
)
if mibBuilder.loadTexts:
    dhcpSnoopPortTable.setStatus("current")
_DhcpSnoopPortEntry_Object = MibTableRow
dhcpSnoopPortEntry = _DhcpSnoopPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 55, 1, 1)
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 55, 1, 1, 1),
    _DhcpSnoopEnable_Type()
)
dhcpSnoopEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnoopEnable.setStatus("current")
_DhcpSnoopTarget_Type = OctetString
_DhcpSnoopTarget_Object = MibScalar
dhcpSnoopTarget = _DhcpSnoopTarget_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 55, 2),
    _DhcpSnoopTarget_Type()
)
dhcpSnoopTarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnoopTarget.setStatus("current")
_DhcpSnoopOps_Type = Integer32
_DhcpSnoopOps_Object = MibScalar
dhcpSnoopOps = _DhcpSnoopOps_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 55, 3),
    _DhcpSnoopOps_Type()
)
dhcpSnoopOps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnoopOps.setStatus("current")
_DhcpStaticTable_Object = MibTable
dhcpStaticTable = _DhcpStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 55, 4)
)
if mibBuilder.loadTexts:
    dhcpStaticTable.setStatus("current")
_DhcpStaticEntry_Object = MibTableRow
dhcpStaticEntry = _DhcpStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 55, 4, 1)
)
dhcpStaticEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZYXEL-SAM1216", "dhcpStaticIpAddr"),
)
if mibBuilder.loadTexts:
    dhcpStaticEntry.setStatus("current")
_DhcpStaticIpAddr_Type = IpAddress
_DhcpStaticIpAddr_Object = MibTableColumn
dhcpStaticIpAddr = _DhcpStaticIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 55, 4, 1, 1),
    _DhcpStaticIpAddr_Type()
)
dhcpStaticIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpStaticIpAddr.setStatus("current")
_DhcpStaticRowStatus_Type = RowStatus
_DhcpStaticRowStatus_Object = MibTableColumn
dhcpStaticRowStatus = _DhcpStaticRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 55, 4, 1, 2),
    _DhcpStaticRowStatus_Type()
)
dhcpStaticRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpStaticRowStatus.setStatus("current")
_MaxNumOfDhcpStaticIp_Type = Integer32
_MaxNumOfDhcpStaticIp_Object = MibScalar
maxNumOfDhcpStaticIp = _MaxNumOfDhcpStaticIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 55, 5),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 55, 6),
    _DhcpSnoopLan2lanEnable_Type()
)
dhcpSnoopLan2lanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnoopLan2lanEnable.setStatus("current")
_Acl_ObjectIdentity = ObjectIdentity
acl = _Acl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 56)
)
_AclSetTable_Object = MibTable
aclSetTable = _AclSetTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 56, 1)
)
if mibBuilder.loadTexts:
    aclSetTable.setStatus("current")
_AclSetEntry_Object = MibTableRow
aclSetEntry = _AclSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 56, 1, 1)
)
aclSetEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZYXEL-SAM1216", "aclSetVpi"),
    (0, "ZYXEL-SAM1216", "aclSetVci"),
    (0, "ZYXEL-SAM1216", "aclSetProfileName"),
)
if mibBuilder.loadTexts:
    aclSetEntry.setStatus("current")
_AclSetVpi_Type = Integer32
_AclSetVpi_Object = MibTableColumn
aclSetVpi = _AclSetVpi_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 56, 1, 1, 1),
    _AclSetVpi_Type()
)
aclSetVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclSetVpi.setStatus("current")
_AclSetVci_Type = Integer32
_AclSetVci_Object = MibTableColumn
aclSetVci = _AclSetVci_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 56, 1, 1, 2),
    _AclSetVci_Type()
)
aclSetVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclSetVci.setStatus("current")
_AclSetProfileName_Type = DisplayString
_AclSetProfileName_Object = MibTableColumn
aclSetProfileName = _AclSetProfileName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 56, 1, 1, 3),
    _AclSetProfileName_Type()
)
aclSetProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclSetProfileName.setStatus("current")
_AclSetRowStatus_Type = RowStatus
_AclSetRowStatus_Object = MibTableColumn
aclSetRowStatus = _AclSetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 56, 1, 1, 4),
    _AclSetRowStatus_Type()
)
aclSetRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclSetRowStatus.setStatus("current")
_AclProfileTable_Object = MibTable
aclProfileTable = _AclProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 56, 2)
)
if mibBuilder.loadTexts:
    aclProfileTable.setStatus("current")
_AclProfileEntry_Object = MibTableRow
aclProfileEntry = _AclProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 56, 2, 1)
)
aclProfileEntry.setIndexNames(
    (0, "ZYXEL-SAM1216", "aclProfileRuleName"),
)
if mibBuilder.loadTexts:
    aclProfileEntry.setStatus("current")
_AclProfileRuleName_Type = DisplayString
_AclProfileRuleName_Object = MibTableColumn
aclProfileRuleName = _AclProfileRuleName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 56, 2, 1, 1),
    _AclProfileRuleName_Type()
)
aclProfileRuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclProfileRuleName.setStatus("current")
_AclProfileRuleNumber_Type = Integer32
_AclProfileRuleNumber_Object = MibTableColumn
aclProfileRuleNumber = _AclProfileRuleNumber_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 56, 2, 1, 2),
    _AclProfileRuleNumber_Type()
)
aclProfileRuleNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileRuleNumber.setStatus("current")
_AclProfileActionNumber_Type = Integer32
_AclProfileActionNumber_Object = MibTableColumn
aclProfileActionNumber = _AclProfileActionNumber_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 56, 2, 1, 3),
    _AclProfileActionNumber_Type()
)
aclProfileActionNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileActionNumber.setStatus("current")
_AclProfileRuleParamMask_Type = Integer32
_AclProfileRuleParamMask_Object = MibTableColumn
aclProfileRuleParamMask = _AclProfileRuleParamMask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 56, 2, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 56, 2, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 56, 2, 1, 6),
    _AclProfileRuleVid_Type()
)
aclProfileRuleVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileRuleVid.setStatus("current")
_AclProfileRuleSmac_Type = PhysAddress
_AclProfileRuleSmac_Object = MibTableColumn
aclProfileRuleSmac = _AclProfileRuleSmac_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 56, 2, 1, 7),
    _AclProfileRuleSmac_Type()
)
aclProfileRuleSmac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileRuleSmac.setStatus("current")
_AclProfileRuleDmac_Type = PhysAddress
_AclProfileRuleDmac_Object = MibTableColumn
aclProfileRuleDmac = _AclProfileRuleDmac_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 56, 2, 1, 8),
    _AclProfileRuleDmac_Type()
)
aclProfileRuleDmac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileRuleDmac.setStatus("current")


class _AclProfileRulePriority_Type(Integer32):
    """Custom type aclProfileRulePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_AclProfileRulePriority_Type.__name__ = "Integer32"
_AclProfileRulePriority_Object = MibTableColumn
aclProfileRulePriority = _AclProfileRulePriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 56, 2, 1, 9),
    _AclProfileRulePriority_Type()
)
aclProfileRulePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileRulePriority.setStatus("current")


class _AclProfileRuleProtocol_Type(Integer32):
    """Custom type aclProfileRuleProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AclProfileRuleProtocol_Type.__name__ = "Integer32"
_AclProfileRuleProtocol_Object = MibTableColumn
aclProfileRuleProtocol = _AclProfileRuleProtocol_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 56, 2, 1, 10),
    _AclProfileRuleProtocol_Type()
)
aclProfileRuleProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileRuleProtocol.setStatus("current")
_AclProfileRuleSrcIP_Type = IpAddress
_AclProfileRuleSrcIP_Object = MibTableColumn
aclProfileRuleSrcIP = _AclProfileRuleSrcIP_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 56, 2, 1, 11),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 56, 2, 1, 12),
    _AclProfileRuleSrcIPMask_Type()
)
aclProfileRuleSrcIPMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileRuleSrcIPMask.setStatus("current")
_AclProfileRuleDestIP_Type = IpAddress
_AclProfileRuleDestIP_Object = MibTableColumn
aclProfileRuleDestIP = _AclProfileRuleDestIP_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 56, 2, 1, 13),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 56, 2, 1, 14),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 56, 2, 1, 15),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 56, 2, 1, 16),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 56, 2, 1, 17),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 56, 2, 1, 18),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 56, 2, 1, 19),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 56, 2, 1, 20),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 56, 2, 1, 21),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 56, 2, 1, 22),
    _AclProfileActionrvlan_Type()
)
aclProfileActionrvlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileActionrvlan.setStatus("current")


class _AclProfileActionrpri_Type(Integer32):
    """Custom type aclProfileActionrpri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_AclProfileActionrpri_Type.__name__ = "Integer32"
_AclProfileActionrpri_Object = MibTableColumn
aclProfileActionrpri = _AclProfileActionrpri_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 56, 2, 1, 23),
    _AclProfileActionrpri_Type()
)
aclProfileActionrpri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileActionrpri.setStatus("current")
_AclProfileRowStatus_Type = RowStatus
_AclProfileRowStatus_Object = MibTableColumn
aclProfileRowStatus = _AclProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 56, 2, 1, 24),
    _AclProfileRowStatus_Type()
)
aclProfileRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileRowStatus.setStatus("current")
_PppoeAgent_ObjectIdentity = ObjectIdentity
pppoeAgent = _PppoeAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 57)
)
_PppoeAgentTable_Object = MibTable
pppoeAgentTable = _PppoeAgentTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 57, 1)
)
if mibBuilder.loadTexts:
    pppoeAgentTable.setStatus("current")
_PppoeAgentEntry_Object = MibTableRow
pppoeAgentEntry = _PppoeAgentEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 57, 1, 1)
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 57, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 57, 1, 1, 2),
    _PppoeAgentInfo_Type()
)
pppoeAgentInfo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pppoeAgentInfo.setStatus("current")
_PppoeAgentRowStatus_Type = RowStatus
_PppoeAgentRowStatus_Object = MibTableColumn
pppoeAgentRowStatus = _PppoeAgentRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 57, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 57, 1, 1, 4),
    _PppoeAgentOptionMode_Type()
)
pppoeAgentOptionMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pppoeAgentOptionMode.setStatus("current")
_MaxNumOfPppoeAgentConf_Type = Integer32
_MaxNumOfPppoeAgentConf_Object = MibScalar
maxNumOfPppoeAgentConf = _MaxNumOfPppoeAgentConf_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 10, 57, 2),
    _MaxNumOfPppoeAgentConf_Type()
)
maxNumOfPppoeAgentConf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumOfPppoeAgentConf.setStatus("current")
_Sys_ObjectIdentity = ObjectIdentity
sys = _Sys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 11)
)
_AccessCtrl_ObjectIdentity = ObjectIdentity
accessCtrl = _AccessCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 11, 5)
)
_SecuredClientTable_Object = MibTable
securedClientTable = _SecuredClientTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 11, 5, 2)
)
if mibBuilder.loadTexts:
    securedClientTable.setStatus("current")
_SecuredClientEntry_Object = MibTableRow
securedClientEntry = _SecuredClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 11, 5, 2, 1)
)
securedClientEntry.setIndexNames(
    (0, "ZYXEL-SAM1216", "securedClientIndex"),
)
if mibBuilder.loadTexts:
    securedClientEntry.setStatus("current")
_SecuredClientIndex_Type = Integer32
_SecuredClientIndex_Object = MibTableColumn
securedClientIndex = _SecuredClientIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 11, 5, 2, 1, 1),
    _SecuredClientIndex_Type()
)
securedClientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securedClientIndex.setStatus("current")
_SecuredClientStartIp_Type = IpAddress
_SecuredClientStartIp_Object = MibTableColumn
securedClientStartIp = _SecuredClientStartIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 11, 5, 2, 1, 2),
    _SecuredClientStartIp_Type()
)
securedClientStartIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securedClientStartIp.setStatus("current")
_SecuredClientEndIp_Type = IpAddress
_SecuredClientEndIp_Object = MibTableColumn
securedClientEndIp = _SecuredClientEndIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 11, 5, 2, 1, 3),
    _SecuredClientEndIp_Type()
)
securedClientEndIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securedClientEndIp.setStatus("current")
_SecuredClientService_Type = Integer32
_SecuredClientService_Object = MibTableColumn
securedClientService = _SecuredClientService_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 11, 5, 2, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 11, 5, 2, 1, 5),
    _SecuredClientEnable_Type()
)
securedClientEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securedClientEnable.setStatus("current")
_ExtAlarm_ObjectIdentity = ObjectIdentity
extAlarm = _ExtAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 11, 8)
)
_ExtAlarmTable_Object = MibTable
extAlarmTable = _ExtAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 11, 8, 1)
)
if mibBuilder.loadTexts:
    extAlarmTable.setStatus("current")
_ExtAlarmEntry_Object = MibTableRow
extAlarmEntry = _ExtAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 11, 8, 1, 1)
)
extAlarmEntry.setIndexNames(
    (0, "ZYXEL-SAM1216", "extAlarmIndex"),
)
if mibBuilder.loadTexts:
    extAlarmEntry.setStatus("current")
_ExtAlarmIndex_Type = Integer32
_ExtAlarmIndex_Object = MibTableColumn
extAlarmIndex = _ExtAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 11, 8, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 11, 8, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 11, 8, 1, 1, 3),
    _ExtAlarmstatus_Type()
)
extAlarmstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extAlarmstatus.setStatus("current")
_User_ObjectIdentity = ObjectIdentity
user = _User_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 11, 9)
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 11, 9, 1),
    _UserAuthMode_Type()
)
userAuthMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userAuthMode.setStatus("current")
_UserAuthServerIp_Type = IpAddress
_UserAuthServerIp_Object = MibScalar
userAuthServerIp = _UserAuthServerIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 11, 9, 2),
    _UserAuthServerIp_Type()
)
userAuthServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userAuthServerIp.setStatus("current")
_UserAuthServerPort_Type = Integer32
_UserAuthServerPort_Object = MibScalar
userAuthServerPort = _UserAuthServerPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 11, 9, 3),
    _UserAuthServerPort_Type()
)
userAuthServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userAuthServerPort.setStatus("current")
_UserAuthServerSecret_Type = OctetString
_UserAuthServerSecret_Object = MibScalar
userAuthServerSecret = _UserAuthServerSecret_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 11, 9, 4),
    _UserAuthServerSecret_Type()
)
userAuthServerSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userAuthServerSecret.setStatus("current")
_UserTable_Object = MibTable
userTable = _UserTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 11, 9, 5)
)
if mibBuilder.loadTexts:
    userTable.setStatus("current")
_UserEntry_Object = MibTableRow
userEntry = _UserEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 11, 9, 5, 1)
)
userEntry.setIndexNames(
    (0, "ZYXEL-SAM1216", "userName"),
)
if mibBuilder.loadTexts:
    userEntry.setStatus("current")
_UserName_Type = DisplayString
_UserName_Object = MibTableColumn
userName = _UserName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 11, 9, 5, 1, 1),
    _UserName_Type()
)
userName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userName.setStatus("current")
_UserPassword_Type = DisplayString
_UserPassword_Object = MibTableColumn
userPassword = _UserPassword_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 11, 9, 5, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 11, 9, 5, 1, 3),
    _UserPriviledge_Type()
)
userPriviledge.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    userPriviledge.setStatus("current")
_UserRowStatus_Type = RowStatus
_UserRowStatus_Object = MibTableColumn
userRowStatus = _UserRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 11, 9, 5, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 11, 9, 6),
    _UserAuthDefaultPriviledge_Type()
)
userAuthDefaultPriviledge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userAuthDefaultPriviledge.setStatus("current")
_SysSlotId_Type = Integer32
_SysSlotId_Object = MibScalar
sysSlotId = _SysSlotId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 11, 10),
    _SysSlotId_Type()
)
sysSlotId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSlotId.setStatus("current")


class _StdioTimeout_Type(Integer32):
    """Custom type stdioTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 360),
    )


_StdioTimeout_Type.__name__ = "Integer32"
_StdioTimeout_Object = MibScalar
stdioTimeout = _StdioTimeout_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 11, 12),
    _StdioTimeout_Type()
)
stdioTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stdioTimeout.setStatus("current")
_Trap_ObjectIdentity = ObjectIdentity
trap = _Trap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 12)
)
_Object_ObjectIdentity = ObjectIdentity
object = _Object_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 12, 1)
)
_EqptAlarmInputIndex_Type = Integer32
_EqptAlarmInputIndex_Object = MibScalar
eqptAlarmInputIndex = _EqptAlarmInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 12, 1, 2),
    _EqptAlarmInputIndex_Type()
)
eqptAlarmInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqptAlarmInputIndex.setStatus("current")
_EqptAlarmInputName_Type = DisplayString
_EqptAlarmInputName_Object = MibScalar
eqptAlarmInputName = _EqptAlarmInputName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 12, 1, 8),
    _EqptAlarmInputName_Type()
)
eqptAlarmInputName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqptAlarmInputName.setStatus("current")
_SysMacAntiSpoofOrig_Type = Integer32
_SysMacAntiSpoofOrig_Object = MibScalar
sysMacAntiSpoofOrig = _SysMacAntiSpoofOrig_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 12, 1, 9),
    _SysMacAntiSpoofOrig_Type()
)
sysMacAntiSpoofOrig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMacAntiSpoofOrig.setStatus("current")
_SysMacAntiSpoofNew_Type = Integer32
_SysMacAntiSpoofNew_Object = MibScalar
sysMacAntiSpoofNew = _SysMacAntiSpoofNew_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 12, 1, 10),
    _SysMacAntiSpoofNew_Type()
)
sysMacAntiSpoofNew.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMacAntiSpoofNew.setStatus("current")
_SysMacAntiSpoofMAC_Type = DisplayString
_SysMacAntiSpoofMAC_Object = MibScalar
sysMacAntiSpoofMAC = _SysMacAntiSpoofMAC_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 12, 1, 11),
    _SysMacAntiSpoofMAC_Type()
)
sysMacAntiSpoofMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMacAntiSpoofMAC.setStatus("current")
_Equipment_ObjectIdentity = ObjectIdentity
equipment = _Equipment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 12, 3)
)
_Systrap_ObjectIdentity = ObjectIdentity
systrap = _Systrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 12, 4)
)
_Statistics_ObjectIdentity = ObjectIdentity
statistics = _Statistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 13)
)
_IgmpQueryCntTotal_Type = Counter32
_IgmpQueryCntTotal_Object = MibScalar
igmpQueryCntTotal = _IgmpQueryCntTotal_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 13, 1),
    _IgmpQueryCntTotal_Type()
)
igmpQueryCntTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpQueryCntTotal.setStatus("current")
_IgmpReportCntTotal_Type = Counter32
_IgmpReportCntTotal_Object = MibScalar
igmpReportCntTotal = _IgmpReportCntTotal_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 13, 2),
    _IgmpReportCntTotal_Type()
)
igmpReportCntTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpReportCntTotal.setStatus("current")
_IgmpLeaveCntTotal_Type = Counter32
_IgmpLeaveCntTotal_Object = MibScalar
igmpLeaveCntTotal = _IgmpLeaveCntTotal_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 13, 3),
    _IgmpLeaveCntTotal_Type()
)
igmpLeaveCntTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpLeaveCntTotal.setStatus("current")
_IgmpNumOfActiveGroups_Type = Integer32
_IgmpNumOfActiveGroups_Object = MibScalar
igmpNumOfActiveGroups = _IgmpNumOfActiveGroups_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 13, 4),
    _IgmpNumOfActiveGroups_Type()
)
igmpNumOfActiveGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpNumOfActiveGroups.setStatus("current")
_IgmpGroupTable_Object = MibTable
igmpGroupTable = _IgmpGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 13, 5)
)
if mibBuilder.loadTexts:
    igmpGroupTable.setStatus("current")
_IgmpGroupEntry_Object = MibTableRow
igmpGroupEntry = _IgmpGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 13, 5, 1)
)
igmpGroupEntry.setIndexNames(
    (0, "ZYXEL-SAM1216", "igmpGroupIp"),
)
if mibBuilder.loadTexts:
    igmpGroupEntry.setStatus("current")
_IgmpGroupIp_Type = IpAddress
_IgmpGroupIp_Object = MibTableColumn
igmpGroupIp = _IgmpGroupIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 13, 5, 1, 1),
    _IgmpGroupIp_Type()
)
igmpGroupIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpGroupIp.setStatus("current")
_IgmpGroupvid_Type = Integer32
_IgmpGroupvid_Object = MibTableColumn
igmpGroupvid = _IgmpGroupvid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 13, 5, 1, 2),
    _IgmpGroupvid_Type()
)
igmpGroupvid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpGroupvid.setStatus("current")
_IgmpGroupnumberOfMembers_Type = Integer32
_IgmpGroupnumberOfMembers_Object = MibTableColumn
igmpGroupnumberOfMembers = _IgmpGroupnumberOfMembers_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 13, 5, 1, 3),
    _IgmpGroupnumberOfMembers_Type()
)
igmpGroupnumberOfMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpGroupnumberOfMembers.setStatus("current")
_IgmpGroupMemberPorts_Type = PortList
_IgmpGroupMemberPorts_Object = MibTableColumn
igmpGroupMemberPorts = _IgmpGroupMemberPorts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 13, 5, 1, 4),
    _IgmpGroupMemberPorts_Type()
)
igmpGroupMemberPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpGroupMemberPorts.setStatus("current")
_IgmpGroupPortTable_Object = MibTable
igmpGroupPortTable = _IgmpGroupPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 13, 6)
)
if mibBuilder.loadTexts:
    igmpGroupPortTable.setStatus("current")
_IgmpGroupPortEntry_Object = MibTableRow
igmpGroupPortEntry = _IgmpGroupPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 13, 6, 1)
)
igmpGroupPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZYXEL-SAM1216", "igmpGroupPortIp"),
    (0, "ZYXEL-SAM1216", "igmpGroupPortvid"),
)
if mibBuilder.loadTexts:
    igmpGroupPortEntry.setStatus("current")
_IgmpGroupPortIp_Type = IpAddress
_IgmpGroupPortIp_Object = MibTableColumn
igmpGroupPortIp = _IgmpGroupPortIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 13, 6, 1, 1),
    _IgmpGroupPortIp_Type()
)
igmpGroupPortIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpGroupPortIp.setStatus("current")
_IgmpGroupPortvid_Type = Integer32
_IgmpGroupPortvid_Object = MibTableColumn
igmpGroupPortvid = _IgmpGroupPortvid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 13, 6, 1, 2),
    _IgmpGroupPortvid_Type()
)
igmpGroupPortvid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpGroupPortvid.setStatus("current")
_IgmpGroupTableV2_Object = MibTable
igmpGroupTableV2 = _IgmpGroupTableV2_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 13, 7)
)
if mibBuilder.loadTexts:
    igmpGroupTableV2.setStatus("current")
_IgmpGroupEntryV2_Object = MibTableRow
igmpGroupEntryV2 = _IgmpGroupEntryV2_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 13, 7, 1)
)
igmpGroupEntryV2.setIndexNames(
    (0, "ZYXEL-SAM1216", "igmpGroupV2Vid"),
    (0, "ZYXEL-SAM1216", "igmpGroupV2Ip"),
)
if mibBuilder.loadTexts:
    igmpGroupEntryV2.setStatus("current")
_IgmpGroupV2Vid_Type = VlanIndex
_IgmpGroupV2Vid_Object = MibTableColumn
igmpGroupV2Vid = _IgmpGroupV2Vid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 13, 7, 1, 1),
    _IgmpGroupV2Vid_Type()
)
igmpGroupV2Vid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpGroupV2Vid.setStatus("current")
_IgmpGroupV2Ip_Type = IpAddress
_IgmpGroupV2Ip_Object = MibTableColumn
igmpGroupV2Ip = _IgmpGroupV2Ip_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 13, 7, 1, 2),
    _IgmpGroupV2Ip_Type()
)
igmpGroupV2Ip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpGroupV2Ip.setStatus("current")
_IgmpGroupV2NumOfMembers_Type = Integer32
_IgmpGroupV2NumOfMembers_Object = MibTableColumn
igmpGroupV2NumOfMembers = _IgmpGroupV2NumOfMembers_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 13, 7, 1, 3),
    _IgmpGroupV2NumOfMembers_Type()
)
igmpGroupV2NumOfMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpGroupV2NumOfMembers.setStatus("current")
_IgmpGroupV2MemberPorts_Type = PortList
_IgmpGroupV2MemberPorts_Object = MibTableColumn
igmpGroupV2MemberPorts = _IgmpGroupV2MemberPorts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 13, 7, 1, 4),
    _IgmpGroupV2MemberPorts_Type()
)
igmpGroupV2MemberPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpGroupV2MemberPorts.setStatus("current")
_IgmpGroupPortTableV2_Object = MibTable
igmpGroupPortTableV2 = _IgmpGroupPortTableV2_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 13, 8)
)
if mibBuilder.loadTexts:
    igmpGroupPortTableV2.setStatus("current")
_IgmpGroupPortEntryV2_Object = MibTableRow
igmpGroupPortEntryV2 = _IgmpGroupPortEntryV2_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 13, 8, 1)
)
igmpGroupPortEntryV2.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZYXEL-SAM1216", "igmpGroupPortVid"),
    (0, "ZYXEL-SAM1216", "igmpGroupPortIp"),
    (0, "ZYXEL-SAM1216", "igmpGroupPortSourceIp"),
)
if mibBuilder.loadTexts:
    igmpGroupPortEntryV2.setStatus("current")
_IgmpGroupPortV2Vid_Type = VlanIndex
_IgmpGroupPortV2Vid_Object = MibTableColumn
igmpGroupPortV2Vid = _IgmpGroupPortV2Vid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 13, 8, 1, 1),
    _IgmpGroupPortV2Vid_Type()
)
igmpGroupPortV2Vid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpGroupPortV2Vid.setStatus("current")
_IgmpGroupPortV2Ip_Type = IpAddress
_IgmpGroupPortV2Ip_Object = MibTableColumn
igmpGroupPortV2Ip = _IgmpGroupPortV2Ip_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 13, 8, 1, 2),
    _IgmpGroupPortV2Ip_Type()
)
igmpGroupPortV2Ip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpGroupPortV2Ip.setStatus("current")
_IgmpGroupPortV2SourceIp_Type = IpAddress
_IgmpGroupPortV2SourceIp_Object = MibTableColumn
igmpGroupPortV2SourceIp = _IgmpGroupPortV2SourceIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 13, 8, 1, 3),
    _IgmpGroupPortV2SourceIp_Type()
)
igmpGroupPortV2SourceIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpGroupPortV2SourceIp.setStatus("current")
_IgmpPortCtrlPduTable_Object = MibTable
igmpPortCtrlPduTable = _IgmpPortCtrlPduTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 13, 9)
)
if mibBuilder.loadTexts:
    igmpPortCtrlPduTable.setStatus("current")
_IgmpPortCtrlPduEntry_Object = MibTableRow
igmpPortCtrlPduEntry = _IgmpPortCtrlPduEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 13, 9, 1)
)
igmpPortCtrlPduEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    igmpPortCtrlPduEntry.setStatus("current")
_IgmpPortCtrlPduQueryCnt_Type = Counter32
_IgmpPortCtrlPduQueryCnt_Object = MibTableColumn
igmpPortCtrlPduQueryCnt = _IgmpPortCtrlPduQueryCnt_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 13, 9, 1, 1),
    _IgmpPortCtrlPduQueryCnt_Type()
)
igmpPortCtrlPduQueryCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpPortCtrlPduQueryCnt.setStatus("current")
_IgmpPortCtrlPduReportCnt_Type = Counter32
_IgmpPortCtrlPduReportCnt_Object = MibTableColumn
igmpPortCtrlPduReportCnt = _IgmpPortCtrlPduReportCnt_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 13, 9, 1, 2),
    _IgmpPortCtrlPduReportCnt_Type()
)
igmpPortCtrlPduReportCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpPortCtrlPduReportCnt.setStatus("current")
_IgmpPortCtrlPduLeaveCnt_Type = Counter32
_IgmpPortCtrlPduLeaveCnt_Object = MibTableColumn
igmpPortCtrlPduLeaveCnt = _IgmpPortCtrlPduLeaveCnt_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 13, 9, 1, 3),
    _IgmpPortCtrlPduLeaveCnt_Type()
)
igmpPortCtrlPduLeaveCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpPortCtrlPduLeaveCnt.setStatus("current")
_IgmpPortNumOfActiveGroups_Type = Integer32
_IgmpPortNumOfActiveGroups_Object = MibTableColumn
igmpPortNumOfActiveGroups = _IgmpPortNumOfActiveGroups_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 13, 9, 1, 4),
    _IgmpPortNumOfActiveGroups_Type()
)
igmpPortNumOfActiveGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpPortNumOfActiveGroups.setStatus("current")
_DhcpStats_ObjectIdentity = ObjectIdentity
dhcpStats = _DhcpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 13, 11)
)
_DhcpSnoopIpTable_Object = MibTable
dhcpSnoopIpTable = _DhcpSnoopIpTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 13, 11, 1)
)
if mibBuilder.loadTexts:
    dhcpSnoopIpTable.setStatus("current")
_DhcpSnoopIpEntry_Object = MibTableRow
dhcpSnoopIpEntry = _DhcpSnoopIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 13, 11, 1, 1)
)
dhcpSnoopIpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZYXEL-SAM1216", "dhcpSnoopIp"),
)
if mibBuilder.loadTexts:
    dhcpSnoopIpEntry.setStatus("current")
_DhcpSnoopIp_Type = IpAddress
_DhcpSnoopIp_Object = MibTableColumn
dhcpSnoopIp = _DhcpSnoopIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 13, 11, 1, 1, 1),
    _DhcpSnoopIp_Type()
)
dhcpSnoopIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnoopIp.setStatus("current")
_DhcpSnoopMac_Type = PhysAddress
_DhcpSnoopMac_Object = MibTableColumn
dhcpSnoopMac = _DhcpSnoopMac_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 13, 11, 1, 1, 2),
    _DhcpSnoopMac_Type()
)
dhcpSnoopMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnoopMac.setStatus("current")
_DhcpSnoopCounterTable_Object = MibTable
dhcpSnoopCounterTable = _DhcpSnoopCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 13, 11, 2)
)
if mibBuilder.loadTexts:
    dhcpSnoopCounterTable.setStatus("current")
_DhcpSnoopCounterEntry_Object = MibTableRow
dhcpSnoopCounterEntry = _DhcpSnoopCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 13, 11, 2, 1)
)
dhcpSnoopCounterEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dhcpSnoopCounterEntry.setStatus("current")
_DhcpDiscovery_Type = Counter64
_DhcpDiscovery_Object = MibTableColumn
dhcpDiscovery = _DhcpDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 13, 11, 2, 1, 1),
    _DhcpDiscovery_Type()
)
dhcpDiscovery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpDiscovery.setStatus("current")
_DhcpOffer_Type = Counter64
_DhcpOffer_Object = MibTableColumn
dhcpOffer = _DhcpOffer_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 13, 11, 2, 1, 2),
    _DhcpOffer_Type()
)
dhcpOffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpOffer.setStatus("current")
_DhcpRequest_Type = Counter64
_DhcpRequest_Object = MibTableColumn
dhcpRequest = _DhcpRequest_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 13, 11, 2, 1, 3),
    _DhcpRequest_Type()
)
dhcpRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRequest.setStatus("current")
_DhcpAck_Type = Counter64
_DhcpAck_Object = MibTableColumn
dhcpAck = _DhcpAck_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 13, 11, 2, 1, 4),
    _DhcpAck_Type()
)
dhcpAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpAck.setStatus("current")
_DhcpAckBySnoopFull_Type = Counter64
_DhcpAckBySnoopFull_Object = MibTableColumn
dhcpAckBySnoopFull = _DhcpAckBySnoopFull_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 13, 11, 2, 1, 5),
    _DhcpAckBySnoopFull_Type()
)
dhcpAckBySnoopFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpAckBySnoopFull.setStatus("current")
_PaepvcStats_ObjectIdentity = ObjectIdentity
paepvcStats = _PaepvcStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 13, 12)
)
_PaepvcSessionTable_Object = MibTable
paepvcSessionTable = _PaepvcSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 13, 12, 1)
)
if mibBuilder.loadTexts:
    paepvcSessionTable.setStatus("current")
_PaepvcSessionEntry_Object = MibTableRow
paepvcSessionEntry = _PaepvcSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 13, 12, 1, 1)
)
paepvcSessionEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZYXEL-SAM1216", "paepvcSessionVpi"),
    (0, "ZYXEL-SAM1216", "paepvcSessionVci"),
)
if mibBuilder.loadTexts:
    paepvcSessionEntry.setStatus("current")
_PaepvcSessionVpi_Type = Integer32
_PaepvcSessionVpi_Object = MibTableColumn
paepvcSessionVpi = _PaepvcSessionVpi_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 13, 12, 1, 1, 1),
    _PaepvcSessionVpi_Type()
)
paepvcSessionVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcSessionVpi.setStatus("current")
_PaepvcSessionVci_Type = Integer32
_PaepvcSessionVci_Object = MibTableColumn
paepvcSessionVci = _PaepvcSessionVci_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 13, 12, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 13, 12, 1, 1, 3),
    _PaepvcSessionState_Type()
)
paepvcSessionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcSessionState.setStatus("current")
_PaepvcSessionId_Type = Integer32
_PaepvcSessionId_Object = MibTableColumn
paepvcSessionId = _PaepvcSessionId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 13, 12, 1, 1, 4),
    _PaepvcSessionId_Type()
)
paepvcSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcSessionId.setStatus("current")
_PaepvcSessionUptime_Type = Unsigned32
_PaepvcSessionUptime_Object = MibTableColumn
paepvcSessionUptime = _PaepvcSessionUptime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 13, 12, 1, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 13, 12, 1, 1, 6),
    _PaepvcSessionacname_Type()
)
paepvcSessionacname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcSessionacname.setStatus("current")
_PaepvcSessionsrvcname_Type = DisplayString
_PaepvcSessionsrvcname_Object = MibTableColumn
paepvcSessionsrvcname = _PaepvcSessionsrvcname_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 13, 12, 1, 1, 7),
    _PaepvcSessionsrvcname_Type()
)
paepvcSessionsrvcname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcSessionsrvcname.setStatus("current")
_PaepvcCountTable_Object = MibTable
paepvcCountTable = _PaepvcCountTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 13, 12, 2)
)
if mibBuilder.loadTexts:
    paepvcCountTable.setStatus("current")
_PaepvcCountEntry_Object = MibTableRow
paepvcCountEntry = _PaepvcCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 13, 12, 2, 1)
)
paepvcCountEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZYXEL-SAM1216", "paepvcCountVpi"),
    (0, "ZYXEL-SAM1216", "paepvcCountVci"),
)
if mibBuilder.loadTexts:
    paepvcCountEntry.setStatus("current")
_PaepvcCountVpi_Type = Integer32
_PaepvcCountVpi_Object = MibTableColumn
paepvcCountVpi = _PaepvcCountVpi_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 13, 12, 2, 1, 1),
    _PaepvcCountVpi_Type()
)
paepvcCountVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcCountVpi.setStatus("current")
_PaepvcCountVci_Type = Integer32
_PaepvcCountVci_Object = MibTableColumn
paepvcCountVci = _PaepvcCountVci_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 13, 12, 2, 1, 2),
    _PaepvcCountVci_Type()
)
paepvcCountVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcCountVci.setStatus("current")
_PaepvcCountPppLcpCfgReqRx_Type = Unsigned32
_PaepvcCountPppLcpCfgReqRx_Object = MibTableColumn
paepvcCountPppLcpCfgReqRx = _PaepvcCountPppLcpCfgReqRx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 13, 12, 2, 1, 3),
    _PaepvcCountPppLcpCfgReqRx_Type()
)
paepvcCountPppLcpCfgReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcCountPppLcpCfgReqRx.setStatus("current")
_PaepvcCountPppLcpEchoReqRx_Type = Unsigned32
_PaepvcCountPppLcpEchoReqRx_Object = MibTableColumn
paepvcCountPppLcpEchoReqRx = _PaepvcCountPppLcpEchoReqRx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 13, 12, 2, 1, 4),
    _PaepvcCountPppLcpEchoReqRx_Type()
)
paepvcCountPppLcpEchoReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcCountPppLcpEchoReqRx.setStatus("current")
_PaepvcCountPppLcpEchoReplyRx_Type = Unsigned32
_PaepvcCountPppLcpEchoReplyRx_Object = MibTableColumn
paepvcCountPppLcpEchoReplyRx = _PaepvcCountPppLcpEchoReplyRx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 13, 12, 2, 1, 5),
    _PaepvcCountPppLcpEchoReplyRx_Type()
)
paepvcCountPppLcpEchoReplyRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcCountPppLcpEchoReplyRx.setStatus("current")
_PaepvcCountPadiTx_Type = Unsigned32
_PaepvcCountPadiTx_Object = MibTableColumn
paepvcCountPadiTx = _PaepvcCountPadiTx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 13, 12, 2, 1, 6),
    _PaepvcCountPadiTx_Type()
)
paepvcCountPadiTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcCountPadiTx.setStatus("current")
_PaepvcCountPadoRx_Type = Unsigned32
_PaepvcCountPadoRx_Object = MibTableColumn
paepvcCountPadoRx = _PaepvcCountPadoRx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 13, 12, 2, 1, 7),
    _PaepvcCountPadoRx_Type()
)
paepvcCountPadoRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcCountPadoRx.setStatus("current")
_PaepvcCountPadrTx_Type = Unsigned32
_PaepvcCountPadrTx_Object = MibTableColumn
paepvcCountPadrTx = _PaepvcCountPadrTx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 13, 12, 2, 1, 8),
    _PaepvcCountPadrTx_Type()
)
paepvcCountPadrTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcCountPadrTx.setStatus("current")
_PaepvcCountPadsRx_Type = Unsigned32
_PaepvcCountPadsRx_Object = MibTableColumn
paepvcCountPadsRx = _PaepvcCountPadsRx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 13, 12, 2, 1, 9),
    _PaepvcCountPadsRx_Type()
)
paepvcCountPadsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcCountPadsRx.setStatus("current")
_PaepvcCountPadtTx_Type = Unsigned32
_PaepvcCountPadtTx_Object = MibTableColumn
paepvcCountPadtTx = _PaepvcCountPadtTx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 13, 12, 2, 1, 10),
    _PaepvcCountPadtTx_Type()
)
paepvcCountPadtTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcCountPadtTx.setStatus("current")
_PaepvcCountPadtRx_Type = Unsigned32
_PaepvcCountPadtRx_Object = MibTableColumn
paepvcCountPadtRx = _PaepvcCountPadtRx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 13, 12, 2, 1, 11),
    _PaepvcCountPadtRx_Type()
)
paepvcCountPadtRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcCountPadtRx.setStatus("current")
_PaepvcCountSrvcnameErrRx_Type = Unsigned32
_PaepvcCountSrvcnameErrRx_Object = MibTableColumn
paepvcCountSrvcnameErrRx = _PaepvcCountSrvcnameErrRx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 13, 12, 2, 1, 12),
    _PaepvcCountSrvcnameErrRx_Type()
)
paepvcCountSrvcnameErrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcCountSrvcnameErrRx.setStatus("current")
_PaepvcCountAcSystemErrRx_Type = Unsigned32
_PaepvcCountAcSystemErrRx_Object = MibTableColumn
paepvcCountAcSystemErrRx = _PaepvcCountAcSystemErrRx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 13, 12, 2, 1, 13),
    _PaepvcCountAcSystemErrRx_Type()
)
paepvcCountAcSystemErrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcCountAcSystemErrRx.setStatus("current")
_PaepvcCountGenericErrTx_Type = Unsigned32
_PaepvcCountGenericErrTx_Object = MibTableColumn
paepvcCountGenericErrTx = _PaepvcCountGenericErrTx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 13, 12, 2, 1, 14),
    _PaepvcCountGenericErrTx_Type()
)
paepvcCountGenericErrTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcCountGenericErrTx.setStatus("current")
_PaepvcCountGenericErrRx_Type = Unsigned32
_PaepvcCountGenericErrRx_Object = MibTableColumn
paepvcCountGenericErrRx = _PaepvcCountGenericErrRx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 13, 12, 2, 1, 15),
    _PaepvcCountGenericErrRx_Type()
)
paepvcCountGenericErrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcCountGenericErrRx.setStatus("current")
_MacStats_ObjectIdentity = ObjectIdentity
macStats = _MacStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 13, 13)
)
_MacDisplayTarget_Type = Integer32
_MacDisplayTarget_Object = MibScalar
macDisplayTarget = _MacDisplayTarget_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 13, 13, 1),
    _MacDisplayTarget_Type()
)
macDisplayTarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macDisplayTarget.setStatus("current")
_MacTable_Object = MibTable
macTable = _MacTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 13, 13, 2)
)
if mibBuilder.loadTexts:
    macTable.setStatus("current")
_MacEntry_Object = MibTableRow
macEntry = _MacEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 13, 13, 2, 1)
)
macEntry.setIndexNames(
    (0, "ZYXEL-SAM1216", "macAddress"),
)
if mibBuilder.loadTexts:
    macEntry.setStatus("current")
_MacAddress_Type = MacAddress
_MacAddress_Object = MibTableColumn
macAddress = _MacAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 13, 13, 2, 1, 1),
    _MacAddress_Type()
)
macAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macAddress.setStatus("current")
_MacPort_Type = Integer32
_MacPort_Object = MibTableColumn
macPort = _MacPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 13, 13, 2, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 13, 13, 2, 1, 3),
    _MacStatus_Type()
)
macStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macStatus.setStatus("current")
_ShdslStats_ObjectIdentity = ObjectIdentity
shdslStats = _ShdslStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 13, 14)
)
_ShdslLinePerfTable_Object = MibTable
shdslLinePerfTable = _ShdslLinePerfTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 13, 14, 1)
)
if mibBuilder.loadTexts:
    shdslLinePerfTable.setStatus("current")
_ShdslLinePerfEntry_Object = MibTableRow
shdslLinePerfEntry = _ShdslLinePerfEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 13, 14, 1, 1)
)
shdslLinePerfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    shdslLinePerfEntry.setStatus("current")
_ShdslLinePerfEs_Type = Counter32
_ShdslLinePerfEs_Object = MibTableColumn
shdslLinePerfEs = _ShdslLinePerfEs_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 13, 14, 1, 1, 1),
    _ShdslLinePerfEs_Type()
)
shdslLinePerfEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shdslLinePerfEs.setStatus("current")
_ShdslLinePerfSes_Type = Counter32
_ShdslLinePerfSes_Object = MibTableColumn
shdslLinePerfSes = _ShdslLinePerfSes_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 13, 14, 1, 1, 2),
    _ShdslLinePerfSes_Type()
)
shdslLinePerfSes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shdslLinePerfSes.setStatus("current")
_ShdslLinePerfCrc_Type = Counter32
_ShdslLinePerfCrc_Object = MibTableColumn
shdslLinePerfCrc = _ShdslLinePerfCrc_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 13, 14, 1, 1, 3),
    _ShdslLinePerfCrc_Type()
)
shdslLinePerfCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shdslLinePerfCrc.setStatus("current")
_ShdslLinePerfLosws_Type = Counter32
_ShdslLinePerfLosws_Object = MibTableColumn
shdslLinePerfLosws = _ShdslLinePerfLosws_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 13, 14, 1, 1, 4),
    _ShdslLinePerfLosws_Type()
)
shdslLinePerfLosws.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shdslLinePerfLosws.setStatus("current")
_ShdslLinePerfUas_Type = Counter32
_ShdslLinePerfUas_Object = MibTableColumn
shdslLinePerfUas = _ShdslLinePerfUas_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 13, 14, 1, 1, 5),
    _ShdslLinePerfUas_Type()
)
shdslLinePerfUas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shdslLinePerfUas.setStatus("current")
_ShdslLinePerfSegmentAnomalies_Type = Counter32
_ShdslLinePerfSegmentAnomalies_Object = MibTableColumn
shdslLinePerfSegmentAnomalies = _ShdslLinePerfSegmentAnomalies_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 13, 14, 1, 1, 6),
    _ShdslLinePerfSegmentAnomalies_Type()
)
shdslLinePerfSegmentAnomalies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shdslLinePerfSegmentAnomalies.setStatus("current")
_ShdslLinePerfSegmentDefect_Type = Counter32
_ShdslLinePerfSegmentDefect_Object = MibTableColumn
shdslLinePerfSegmentDefect = _ShdslLinePerfSegmentDefect_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 13, 14, 1, 1, 7),
    _ShdslLinePerfSegmentDefect_Type()
)
shdslLinePerfSegmentDefect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shdslLinePerfSegmentDefect.setStatus("current")
_GbondStats_ObjectIdentity = ObjectIdentity
gbondStats = _GbondStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 13, 51)
)
_GbondStateTable_Object = MibTable
gbondStateTable = _GbondStateTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 13, 51, 1)
)
if mibBuilder.loadTexts:
    gbondStateTable.setStatus("current")
_GbondStateEntry_Object = MibTableRow
gbondStateEntry = _GbondStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 13, 51, 1, 1)
)
gbondStateEntry.setIndexNames(
    (0, "ZYXEL-SAM1216", "gbondStateName"),
)
if mibBuilder.loadTexts:
    gbondStateEntry.setStatus("current")


class _GbondStateName_Type(OctetString):
    """Custom type gbondStateName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_GbondStateName_Type.__name__ = "OctetString"
_GbondStateName_Object = MibTableColumn
gbondStateName = _GbondStateName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 13, 51, 1, 1, 1),
    _GbondStateName_Type()
)
gbondStateName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gbondStateName.setStatus("current")


class _GbondStateSid_Type(Integer32):
    """Custom type gbondStateSid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sid8", 1),
          ("sid12", 2))
    )


_GbondStateSid_Type.__name__ = "Integer32"
_GbondStateSid_Object = MibTableColumn
gbondStateSid = _GbondStateSid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 13, 51, 1, 1, 2),
    _GbondStateSid_Type()
)
gbondStateSid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gbondStateSid.setStatus("current")
_GbondStateUpRate_Type = Unsigned32
_GbondStateUpRate_Object = MibTableColumn
gbondStateUpRate = _GbondStateUpRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 13, 51, 1, 1, 3),
    _GbondStateUpRate_Type()
)
gbondStateUpRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gbondStateUpRate.setStatus("current")
_GbondStateDownRate_Type = Unsigned32
_GbondStateDownRate_Object = MibTableColumn
gbondStateDownRate = _GbondStateDownRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 13, 51, 1, 1, 4),
    _GbondStateDownRate_Type()
)
gbondStateDownRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gbondStateDownRate.setStatus("current")
_GbondStateMember_Type = OctetString
_GbondStateMember_Object = MibTableColumn
gbondStateMember = _GbondStateMember_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 13, 51, 1, 1, 5),
    _GbondStateMember_Type()
)
gbondStateMember.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gbondStateMember.setStatus("current")
_GbondStatelinkup_Type = OctetString
_GbondStatelinkup_Object = MibTableColumn
gbondStatelinkup = _GbondStatelinkup_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 13, 51, 1, 1, 6),
    _GbondStatelinkup_Type()
)
gbondStatelinkup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gbondStatelinkup.setStatus("current")
_GbondStateTx_Type = OctetString
_GbondStateTx_Object = MibTableColumn
gbondStateTx = _GbondStateTx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 13, 51, 1, 1, 7),
    _GbondStateTx_Type()
)
gbondStateTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gbondStateTx.setStatus("current")
_GbondStateRx_Type = OctetString
_GbondStateRx_Object = MibTableColumn
gbondStateRx = _GbondStateRx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 13, 51, 1, 1, 8),
    _GbondStateRx_Type()
)
gbondStateRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gbondStateRx.setStatus("current")
_GbondStatelinkdown_Type = OctetString
_GbondStatelinkdown_Object = MibTableColumn
gbondStatelinkdown = _GbondStatelinkdown_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 13, 51, 1, 1, 9),
    _GbondStatelinkdown_Type()
)
gbondStatelinkdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gbondStatelinkdown.setStatus("current")
_Clear_ObjectIdentity = ObjectIdentity
clear = _Clear_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 14)
)
_CounterClearTarget_Type = OctetString
_CounterClearTarget_Object = MibScalar
counterClearTarget = _CounterClearTarget_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 14, 1),
    _CounterClearTarget_Type()
)
counterClearTarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    counterClearTarget.setStatus("current")
_CounterClearOps_Type = Integer32
_CounterClearOps_Object = MibScalar
counterClearOps = _CounterClearOps_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 14, 2),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 14, 3),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 14, 4),
    _CounterClearVci_Type()
)
counterClearVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    counterClearVci.setStatus("current")

# Managed Objects groups


# Notification objects

eqptHWMonitorFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 12, 3, 1)
)
if mibBuilder.loadTexts:
    eqptHWMonitorFailure.setStatus(
        "current"
    )

sysMacAntiSpoofing = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 12, 4, 1)
)
sysMacAntiSpoofing.setObjects(
      *(("ZYXEL-SAM1216", "sysMacAntiSpoofOrig"),
        ("ZYXEL-SAM1216", "sysMacAntiSpoofNew"),
        ("ZYXEL-SAM1216", "sysMacAntiSpoofMAC"))
)
if mibBuilder.loadTexts:
    sysMacAntiSpoofing.setStatus(
        "current"
    )

sysAlarmCutoffEnable = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 12, 4, 2)
)
if mibBuilder.loadTexts:
    sysAlarmCutoffEnable.setStatus(
        "current"
    )

sysAlarmClearEnable = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 12, 4, 3)
)
if mibBuilder.loadTexts:
    sysAlarmClearEnable.setStatus(
        "current"
    )

sysLoginFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 6, 12, 4, 4)
)
if mibBuilder.loadTexts:
    sysLoginFailure.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-SAM1216",
    **{"zyxel": zyxel,
       "products": products,
       "accessSwitch": accessSwitch,
       "sesSeries": sesSeries,
       "sam1216-22": sam1216_22,
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
       "igmpVersion": igmpVersion,
       "maxNumOfQryVid": maxNumOfQryVid,
       "qryVidConfTable": qryVidConfTable,
       "qryVidConfEntry": qryVidConfEntry,
       "qryVid": qryVid,
       "qryVidRowStatus": qryVidRowStatus,
       "qryVidStatusTable": qryVidStatusTable,
       "qryVidStatusEntry": qryVidStatusEntry,
       "qryVidType": qryVidType,
       "port": port,
       "subrPortTable": subrPortTable,
       "subrPortEntry": subrPortEntry,
       "subrPortName": subrPortName,
       "subrPortTel": subrPortTel,
       "shdslPort": shdslPort,
       "shdslLineConfTable": shdslLineConfTable,
       "shdslLineConfEntry": shdslLineConfEntry,
       "shdslLineConfShdslMode": shdslLineConfShdslMode,
       "shdslLineConfPmms": shdslLineConfPmms,
       "shdslLineConfPboMode": shdslLineConfPboMode,
       "shdslLineConfPboValue": shdslLineConfPboValue,
       "shdslLineConfShdslTCMode": shdslLineConfShdslTCMode,
       "shdslPortBatchSet": shdslPortBatchSet,
       "shdslPortTarget": shdslPortTarget,
       "shdslPortOps": shdslPortOps,
       "shdslModeForBatchSet": shdslModeForBatchSet,
       "shdslLineProfileForBatchSet": shdslLineProfileForBatchSet,
       "shdslAlarmProfileForBatchSet": shdslAlarmProfileForBatchSet,
       "shdslPboValueForBatchSet": shdslPboValueForBatchSet,
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
       "portOperation": portOperation,
       "portTarget": portTarget,
       "portOps": portOps,
       "rpvc": rpvc,
       "rpvcGatewayTable": rpvcGatewayTable,
       "rpvcGatewayEntry": rpvcGatewayEntry,
       "rpvcGatewayIp": rpvcGatewayIp,
       "rpvcGatewayVlanId": rpvcGatewayVlanId,
       "rpvcGatewayRowStatus": rpvcGatewayRowStatus,
       "rpvcGatewayPriority": rpvcGatewayPriority,
       "rpvcTable": rpvcTable,
       "rpvcTableEntry": rpvcTableEntry,
       "rpvcVpi": rpvcVpi,
       "rpvcVci": rpvcVci,
       "rpvcDSProfile": rpvcDSProfile,
       "rpvcUSProfile": rpvcUSProfile,
       "rpvcIp": rpvcIp,
       "rpvcNetmask": rpvcNetmask,
       "rpvcGatewayIpAddress": rpvcGatewayIpAddress,
       "rpvcRowStatus": rpvcRowStatus,
       "rpvcRouteDomainTable": rpvcRouteDomainTable,
       "rpvcRouteDomainTableEntry": rpvcRouteDomainTableEntry,
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
       "gbond": gbond,
       "gbondGroupTable": gbondGroupTable,
       "gbondGroupEntry": gbondGroupEntry,
       "gbondGroupName": gbondGroupName,
       "gbondGroupPorts": gbondGroupPorts,
       "gbondGroupSid": gbondGroupSid,
       "gbondGroupUpRate": gbondGroupUpRate,
       "gbondGroupDownRate": gbondGroupDownRate,
       "gbondGroupRowStatus": gbondGroupRowStatus,
       "switch": switch,
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
       "sys": sys,
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
       "stdioTimeout": stdioTimeout,
       "trap": trap,
       "object": object,
       "eqptAlarmInputIndex": eqptAlarmInputIndex,
       "eqptAlarmInputName": eqptAlarmInputName,
       "sysMacAntiSpoofOrig": sysMacAntiSpoofOrig,
       "sysMacAntiSpoofNew": sysMacAntiSpoofNew,
       "sysMacAntiSpoofMAC": sysMacAntiSpoofMAC,
       "equipment": equipment,
       "eqptHWMonitorFailure": eqptHWMonitorFailure,
       "systrap": systrap,
       "sysMacAntiSpoofing": sysMacAntiSpoofing,
       "sysAlarmCutoffEnable": sysAlarmCutoffEnable,
       "sysAlarmClearEnable": sysAlarmClearEnable,
       "sysLoginFailure": sysLoginFailure,
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
       "igmpGroupTableV2": igmpGroupTableV2,
       "igmpGroupEntryV2": igmpGroupEntryV2,
       "igmpGroupV2Vid": igmpGroupV2Vid,
       "igmpGroupV2Ip": igmpGroupV2Ip,
       "igmpGroupV2NumOfMembers": igmpGroupV2NumOfMembers,
       "igmpGroupV2MemberPorts": igmpGroupV2MemberPorts,
       "igmpGroupPortTableV2": igmpGroupPortTableV2,
       "igmpGroupPortEntryV2": igmpGroupPortEntryV2,
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
       "shdslStats": shdslStats,
       "shdslLinePerfTable": shdslLinePerfTable,
       "shdslLinePerfEntry": shdslLinePerfEntry,
       "shdslLinePerfEs": shdslLinePerfEs,
       "shdslLinePerfSes": shdslLinePerfSes,
       "shdslLinePerfCrc": shdslLinePerfCrc,
       "shdslLinePerfLosws": shdslLinePerfLosws,
       "shdslLinePerfUas": shdslLinePerfUas,
       "shdslLinePerfSegmentAnomalies": shdslLinePerfSegmentAnomalies,
       "shdslLinePerfSegmentDefect": shdslLinePerfSegmentDefect,
       "gbondStats": gbondStats,
       "gbondStateTable": gbondStateTable,
       "gbondStateEntry": gbondStateEntry,
       "gbondStateName": gbondStateName,
       "gbondStateSid": gbondStateSid,
       "gbondStateUpRate": gbondStateUpRate,
       "gbondStateDownRate": gbondStateDownRate,
       "gbondStateMember": gbondStateMember,
       "gbondStatelinkup": gbondStatelinkup,
       "gbondStateTx": gbondStateTx,
       "gbondStateRx": gbondStateRx,
       "gbondStatelinkdown": gbondStatelinkdown,
       "clear": clear,
       "counterClearTarget": counterClearTarget,
       "counterClearOps": counterClearOps,
       "counterClearVpi": counterClearVpi,
       "counterClearVci": counterClearVci}
)
