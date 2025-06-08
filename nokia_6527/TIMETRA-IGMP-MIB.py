# SNMP MIB module (TIMETRA-IGMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_6527/TIMETRA-IGMP-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 17:44:24 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRNotifyPrefix,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRNotifyPrefix",
    "tmnxSRObjs")

(tmnxMcacLagPortsDown,
 tmnxMcacLevelId) = mibBuilder.importSymbols(
    "TIMETRA-MCAST-CAC-MIB",
    "tmnxMcacLagPortsDown",
    "tmnxMcacLevelId")

(sapEncapValue,
 sapPortId) = mibBuilder.importSymbols(
    "TIMETRA-SAP-MIB",
    "sapEncapValue",
    "sapPortId")

(TNamedItem,
 TNamedItemOrEmpty,
 TPolicyStatementNameOrEmpty,
 TmnxAdminState,
 TmnxIgmpGroupFilterMode,
 TmnxIgmpGroupType,
 TmnxOperState,
 TmnxPppoeSessionId,
 TmnxServId,
 TmnxSubIdentStringOrEmpty,
 TmnxVRtrID) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TNamedItem",
    "TNamedItemOrEmpty",
    "TPolicyStatementNameOrEmpty",
    "TmnxAdminState",
    "TmnxIgmpGroupFilterMode",
    "TmnxIgmpGroupType",
    "TmnxOperState",
    "TmnxPppoeSessionId",
    "TmnxServId",
    "TmnxSubIdentStringOrEmpty",
    "TmnxVRtrID")

(vRtrID,
 vRtrIfIndex) = mibBuilder.importSymbols(
    "TIMETRA-VRTR-MIB",
    "vRtrID",
    "vRtrIfIndex")


# MODULE-IDENTITY

timetraIgmpMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 23)
)
if mibBuilder.loadTexts:
    timetraIgmpMIBModule.setRevisions(
        ("2014-01-01 00:00",
         "2011-02-01 00:00",
         "2009-02-28 00:00",
         "2008-07-01 00:00",
         "2008-01-01 00:00",
         "2007-01-01 00:00",
         "2006-03-23 00:00",
         "2005-08-31 00:00",
         "2005-01-24 00:00",
         "2004-01-15 00:00",
         "2003-08-15 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class IgmpGrpItfOperState(TextualConvention, Integer32):
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
        *(("unknown", 1),
          ("noIgmpOnGrpItf", 2),
          ("grpItfDown", 3),
          ("inService", 4),
          ("notFwding", 5))
    )



class VRtrIgmpHostMcRDstStatType(TextualConvention, Integer32):
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
        *(("joinTx", 1),
          ("joinDenyTx", 2),
          ("dropTx", 3),
          ("joinLost", 4),
          ("joinDenyLost", 5),
          ("dropLost", 6))
    )



# MIB Managed Objects in the order of their OIDs

_TmnxIgmpConformance_ObjectIdentity = ObjectIdentity
tmnxIgmpConformance = _TmnxIgmpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 23)
)
_TmnxIgmpCompliances_ObjectIdentity = ObjectIdentity
tmnxIgmpCompliances = _TmnxIgmpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 23, 1)
)
_TmnxIgmpGroups_ObjectIdentity = ObjectIdentity
tmnxIgmpGroups = _TmnxIgmpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 23, 2)
)
_TmnxIgmpObjs_ObjectIdentity = ObjectIdentity
tmnxIgmpObjs = _TmnxIgmpObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23)
)
_VRtrIgmpProtocolObjs_ObjectIdentity = ObjectIdentity
vRtrIgmpProtocolObjs = _VRtrIgmpProtocolObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 1)
)
_VRtrIgmpGeneralTable_Object = MibTable
vRtrIgmpGeneralTable = _VRtrIgmpGeneralTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 1, 1)
)
if mibBuilder.loadTexts:
    vRtrIgmpGeneralTable.setStatus("current")
_VRtrIgmpGeneralEntry_Object = MibTableRow
vRtrIgmpGeneralEntry = _VRtrIgmpGeneralEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 1, 1, 1)
)
vRtrIgmpGeneralEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
)
if mibBuilder.loadTexts:
    vRtrIgmpGeneralEntry.setStatus("current")


class _VRtrIgmpGenQueryInterval_Type(Unsigned32):
    """Custom type vRtrIgmpGenQueryInterval based on Unsigned32"""
    defaultValue = 125

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 1024),
    )


_VRtrIgmpGenQueryInterval_Type.__name__ = "Unsigned32"
_VRtrIgmpGenQueryInterval_Object = MibTableColumn
vRtrIgmpGenQueryInterval = _VRtrIgmpGenQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 1, 1, 1, 1),
    _VRtrIgmpGenQueryInterval_Type()
)
vRtrIgmpGenQueryInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIgmpGenQueryInterval.setStatus("current")
if mibBuilder.loadTexts:
    vRtrIgmpGenQueryInterval.setUnits("seconds")


class _VRtrIgmpGenLastMembQueryIntvl_Type(Unsigned32):
    """Custom type vRtrIgmpGenLastMembQueryIntvl based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_VRtrIgmpGenLastMembQueryIntvl_Type.__name__ = "Unsigned32"
_VRtrIgmpGenLastMembQueryIntvl_Object = MibTableColumn
vRtrIgmpGenLastMembQueryIntvl = _VRtrIgmpGenLastMembQueryIntvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 1, 1, 1, 2),
    _VRtrIgmpGenLastMembQueryIntvl_Type()
)
vRtrIgmpGenLastMembQueryIntvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIgmpGenLastMembQueryIntvl.setStatus("current")
if mibBuilder.loadTexts:
    vRtrIgmpGenLastMembQueryIntvl.setUnits("seconds")


class _VRtrIgmpGenQueryResponseIntvl_Type(Unsigned32):
    """Custom type vRtrIgmpGenQueryResponseIntvl based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_VRtrIgmpGenQueryResponseIntvl_Type.__name__ = "Unsigned32"
_VRtrIgmpGenQueryResponseIntvl_Object = MibTableColumn
vRtrIgmpGenQueryResponseIntvl = _VRtrIgmpGenQueryResponseIntvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 1, 1, 1, 3),
    _VRtrIgmpGenQueryResponseIntvl_Type()
)
vRtrIgmpGenQueryResponseIntvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIgmpGenQueryResponseIntvl.setStatus("current")
if mibBuilder.loadTexts:
    vRtrIgmpGenQueryResponseIntvl.setUnits("seconds")


class _VRtrIgmpGenRobustCount_Type(Unsigned32):
    """Custom type vRtrIgmpGenRobustCount based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_VRtrIgmpGenRobustCount_Type.__name__ = "Unsigned32"
_VRtrIgmpGenRobustCount_Object = MibTableColumn
vRtrIgmpGenRobustCount = _VRtrIgmpGenRobustCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 1, 1, 1, 4),
    _VRtrIgmpGenRobustCount_Type()
)
vRtrIgmpGenRobustCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIgmpGenRobustCount.setStatus("current")
_VRtrIgmpGenLastChange_Type = TimeStamp
_VRtrIgmpGenLastChange_Object = MibTableColumn
vRtrIgmpGenLastChange = _VRtrIgmpGenLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 1, 1, 1, 5),
    _VRtrIgmpGenLastChange_Type()
)
vRtrIgmpGenLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpGenLastChange.setStatus("current")


class _VRtrIgmpGenAdminState_Type(TmnxAdminState):
    """Custom type vRtrIgmpGenAdminState based on TmnxAdminState"""
    defaultValue = 3


_VRtrIgmpGenAdminState_Type.__name__ = "TmnxAdminState"
_VRtrIgmpGenAdminState_Object = MibTableColumn
vRtrIgmpGenAdminState = _VRtrIgmpGenAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 1, 1, 1, 6),
    _VRtrIgmpGenAdminState_Type()
)
vRtrIgmpGenAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIgmpGenAdminState.setStatus("current")
_VRtrIgmpGenOperState_Type = TmnxOperState
_VRtrIgmpGenOperState_Object = MibTableColumn
vRtrIgmpGenOperState = _VRtrIgmpGenOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 1, 1, 1, 7),
    _VRtrIgmpGenOperState_Type()
)
vRtrIgmpGenOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpGenOperState.setStatus("current")
_VRtrIgmpGenGrpIfQuerySrcIp_Type = IpAddress
_VRtrIgmpGenGrpIfQuerySrcIp_Object = MibTableColumn
vRtrIgmpGenGrpIfQuerySrcIp = _VRtrIgmpGenGrpIfQuerySrcIp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 1, 1, 1, 8),
    _VRtrIgmpGenGrpIfQuerySrcIp_Type()
)
vRtrIgmpGenGrpIfQuerySrcIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIgmpGenGrpIfQuerySrcIp.setStatus("current")
_VRtrIgmpGrpSrcTable_Object = MibTable
vRtrIgmpGrpSrcTable = _VRtrIgmpGrpSrcTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 1, 2)
)
if mibBuilder.loadTexts:
    vRtrIgmpGrpSrcTable.setStatus("current")
_VRtrIgmpGrpSrcEntry_Object = MibTableRow
vRtrIgmpGrpSrcEntry = _VRtrIgmpGrpSrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 1, 2, 1)
)
vRtrIgmpGrpSrcEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-IGMP-MIB", "vRtrIgmpGrpSrcGroupAddress"),
    (0, "TIMETRA-IGMP-MIB", "vRtrIgmpGrpSrcSourceAddress"),
    (0, "TIMETRA-IGMP-MIB", "vRtrIgmpGrpSrcFwdOrBlk"),
    (0, "TIMETRA-VRTR-MIB", "vRtrIfIndex"),
)
if mibBuilder.loadTexts:
    vRtrIgmpGrpSrcEntry.setStatus("current")
_VRtrIgmpGrpSrcGroupAddress_Type = IpAddress
_VRtrIgmpGrpSrcGroupAddress_Object = MibTableColumn
vRtrIgmpGrpSrcGroupAddress = _VRtrIgmpGrpSrcGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 1, 2, 1, 1),
    _VRtrIgmpGrpSrcGroupAddress_Type()
)
vRtrIgmpGrpSrcGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrIgmpGrpSrcGroupAddress.setStatus("current")
_VRtrIgmpGrpSrcSourceAddress_Type = IpAddress
_VRtrIgmpGrpSrcSourceAddress_Object = MibTableColumn
vRtrIgmpGrpSrcSourceAddress = _VRtrIgmpGrpSrcSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 1, 2, 1, 2),
    _VRtrIgmpGrpSrcSourceAddress_Type()
)
vRtrIgmpGrpSrcSourceAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrIgmpGrpSrcSourceAddress.setStatus("current")


class _VRtrIgmpGrpSrcFwdOrBlk_Type(Integer32):
    """Custom type vRtrIgmpGrpSrcFwdOrBlk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forward", 1),
          ("block", 2))
    )


_VRtrIgmpGrpSrcFwdOrBlk_Type.__name__ = "Integer32"
_VRtrIgmpGrpSrcFwdOrBlk_Object = MibTableColumn
vRtrIgmpGrpSrcFwdOrBlk = _VRtrIgmpGrpSrcFwdOrBlk_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 1, 2, 1, 3),
    _VRtrIgmpGrpSrcFwdOrBlk_Type()
)
vRtrIgmpGrpSrcFwdOrBlk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpGrpSrcFwdOrBlk.setStatus("current")
_VRtrIgmpGrpSrcUpTime_Type = Unsigned32
_VRtrIgmpGrpSrcUpTime_Object = MibTableColumn
vRtrIgmpGrpSrcUpTime = _VRtrIgmpGrpSrcUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 1, 2, 1, 4),
    _VRtrIgmpGrpSrcUpTime_Type()
)
vRtrIgmpGrpSrcUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpGrpSrcUpTime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrIgmpGrpSrcUpTime.setUnits("seconds")
_VRtrIgmpSSMTranslateTable_Object = MibTable
vRtrIgmpSSMTranslateTable = _VRtrIgmpSSMTranslateTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 1, 3)
)
if mibBuilder.loadTexts:
    vRtrIgmpSSMTranslateTable.setStatus("current")
_VRtrIgmpSSMTranslateEntry_Object = MibTableRow
vRtrIgmpSSMTranslateEntry = _VRtrIgmpSSMTranslateEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 1, 3, 1)
)
vRtrIgmpSSMTranslateEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-IGMP-MIB", "vRtrIgmpSSMTranslateGrpAddr1"),
    (0, "TIMETRA-IGMP-MIB", "vRtrIgmpSSMTranslateGrpAddr2"),
    (0, "TIMETRA-IGMP-MIB", "vRtrIgmpSSMTranslateSrcAddr"),
)
if mibBuilder.loadTexts:
    vRtrIgmpSSMTranslateEntry.setStatus("current")
_VRtrIgmpSSMTranslateGrpAddr1_Type = IpAddress
_VRtrIgmpSSMTranslateGrpAddr1_Object = MibTableColumn
vRtrIgmpSSMTranslateGrpAddr1 = _VRtrIgmpSSMTranslateGrpAddr1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 1, 3, 1, 1),
    _VRtrIgmpSSMTranslateGrpAddr1_Type()
)
vRtrIgmpSSMTranslateGrpAddr1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrIgmpSSMTranslateGrpAddr1.setStatus("current")
_VRtrIgmpSSMTranslateGrpAddr2_Type = IpAddress
_VRtrIgmpSSMTranslateGrpAddr2_Object = MibTableColumn
vRtrIgmpSSMTranslateGrpAddr2 = _VRtrIgmpSSMTranslateGrpAddr2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 1, 3, 1, 2),
    _VRtrIgmpSSMTranslateGrpAddr2_Type()
)
vRtrIgmpSSMTranslateGrpAddr2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrIgmpSSMTranslateGrpAddr2.setStatus("current")
_VRtrIgmpSSMTranslateSrcAddr_Type = IpAddress
_VRtrIgmpSSMTranslateSrcAddr_Object = MibTableColumn
vRtrIgmpSSMTranslateSrcAddr = _VRtrIgmpSSMTranslateSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 1, 3, 1, 3),
    _VRtrIgmpSSMTranslateSrcAddr_Type()
)
vRtrIgmpSSMTranslateSrcAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrIgmpSSMTranslateSrcAddr.setStatus("current")
_VRtrIgmpSSMTranslateRowStatus_Type = RowStatus
_VRtrIgmpSSMTranslateRowStatus_Object = MibTableColumn
vRtrIgmpSSMTranslateRowStatus = _VRtrIgmpSSMTranslateRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 1, 3, 1, 4),
    _VRtrIgmpSSMTranslateRowStatus_Type()
)
vRtrIgmpSSMTranslateRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIgmpSSMTranslateRowStatus.setStatus("current")
_VRtrIgmpGenStatsTable_Object = MibTable
vRtrIgmpGenStatsTable = _VRtrIgmpGenStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 1, 4)
)
if mibBuilder.loadTexts:
    vRtrIgmpGenStatsTable.setStatus("current")
_VRtrIgmpGenStatsEntry_Object = MibTableRow
vRtrIgmpGenStatsEntry = _VRtrIgmpGenStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 1, 4, 1)
)
if mibBuilder.loadTexts:
    vRtrIgmpGenStatsEntry.setStatus("current")
_VRtrIgmpGenStatsStarGTypes_Type = Gauge32
_VRtrIgmpGenStatsStarGTypes_Object = MibTableColumn
vRtrIgmpGenStatsStarGTypes = _VRtrIgmpGenStatsStarGTypes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 1, 4, 1, 1),
    _VRtrIgmpGenStatsStarGTypes_Type()
)
vRtrIgmpGenStatsStarGTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpGenStatsStarGTypes.setStatus("current")
_VRtrIgmpGenStatsSGTypes_Type = Gauge32
_VRtrIgmpGenStatsSGTypes_Object = MibTableColumn
vRtrIgmpGenStatsSGTypes = _VRtrIgmpGenStatsSGTypes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 1, 4, 1, 2),
    _VRtrIgmpGenStatsSGTypes_Type()
)
vRtrIgmpGenStatsSGTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpGenStatsSGTypes.setStatus("current")
_VRtrIgmpGrpSrcSummaryTable_Object = MibTable
vRtrIgmpGrpSrcSummaryTable = _VRtrIgmpGrpSrcSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 1, 5)
)
if mibBuilder.loadTexts:
    vRtrIgmpGrpSrcSummaryTable.setStatus("current")
_VRtrIgmpGrpSrcSummaryEntry_Object = MibTableRow
vRtrIgmpGrpSrcSummaryEntry = _VRtrIgmpGrpSrcSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 1, 5, 1)
)
vRtrIgmpGrpSrcSummaryEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-IGMP-MIB", "vRtrIgmpGrpSrcGroupAddress"),
    (0, "TIMETRA-IGMP-MIB", "vRtrIgmpGrpSrcSourceAddress"),
)
if mibBuilder.loadTexts:
    vRtrIgmpGrpSrcSummaryEntry.setStatus("current")
_VRtrIgmpGrpSrcSummFwdInterfaces_Type = Gauge32
_VRtrIgmpGrpSrcSummFwdInterfaces_Object = MibTableColumn
vRtrIgmpGrpSrcSummFwdInterfaces = _VRtrIgmpGrpSrcSummFwdInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 1, 5, 1, 1),
    _VRtrIgmpGrpSrcSummFwdInterfaces_Type()
)
vRtrIgmpGrpSrcSummFwdInterfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpGrpSrcSummFwdInterfaces.setStatus("current")
_VRtrIgmpGrpSrcSummBlkInterfaces_Type = Gauge32
_VRtrIgmpGrpSrcSummBlkInterfaces_Object = MibTableColumn
vRtrIgmpGrpSrcSummBlkInterfaces = _VRtrIgmpGrpSrcSummBlkInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 1, 5, 1, 2),
    _VRtrIgmpGrpSrcSummBlkInterfaces_Type()
)
vRtrIgmpGrpSrcSummBlkInterfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpGrpSrcSummBlkInterfaces.setStatus("current")
_VRtrIgmpGrpSrcSummFwdHosts_Type = Gauge32
_VRtrIgmpGrpSrcSummFwdHosts_Object = MibTableColumn
vRtrIgmpGrpSrcSummFwdHosts = _VRtrIgmpGrpSrcSummFwdHosts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 1, 5, 1, 3),
    _VRtrIgmpGrpSrcSummFwdHosts_Type()
)
vRtrIgmpGrpSrcSummFwdHosts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpGrpSrcSummFwdHosts.setStatus("current")
_VRtrIgmpGrpSrcSummBlkHosts_Type = Gauge32
_VRtrIgmpGrpSrcSummBlkHosts_Object = MibTableColumn
vRtrIgmpGrpSrcSummBlkHosts = _VRtrIgmpGrpSrcSummBlkHosts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 1, 5, 1, 4),
    _VRtrIgmpGrpSrcSummBlkHosts_Type()
)
vRtrIgmpGrpSrcSummBlkHosts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpGrpSrcSummBlkHosts.setStatus("current")
_VRtrIgmpGrpSrcSummFwdGrpIfSaps_Type = Gauge32
_VRtrIgmpGrpSrcSummFwdGrpIfSaps_Object = MibTableColumn
vRtrIgmpGrpSrcSummFwdGrpIfSaps = _VRtrIgmpGrpSrcSummFwdGrpIfSaps_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 1, 5, 1, 5),
    _VRtrIgmpGrpSrcSummFwdGrpIfSaps_Type()
)
vRtrIgmpGrpSrcSummFwdGrpIfSaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpGrpSrcSummFwdGrpIfSaps.setStatus("current")
_VRtrIgmpGrpSrcSummBlkGrpIfSaps_Type = Gauge32
_VRtrIgmpGrpSrcSummBlkGrpIfSaps_Object = MibTableColumn
vRtrIgmpGrpSrcSummBlkGrpIfSaps = _VRtrIgmpGrpSrcSummBlkGrpIfSaps_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 1, 5, 1, 6),
    _VRtrIgmpGrpSrcSummBlkGrpIfSaps_Type()
)
vRtrIgmpGrpSrcSummBlkGrpIfSaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpGrpSrcSummBlkGrpIfSaps.setStatus("current")
_VRtrIgmpIfObjs_ObjectIdentity = ObjectIdentity
vRtrIgmpIfObjs = _VRtrIgmpIfObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2)
)
_VRtrIgmpIfTable_Object = MibTable
vRtrIgmpIfTable = _VRtrIgmpIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 1)
)
if mibBuilder.loadTexts:
    vRtrIgmpIfTable.setStatus("current")
_VRtrIgmpIfEntry_Object = MibTableRow
vRtrIgmpIfEntry = _VRtrIgmpIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 1, 1)
)
vRtrIgmpIfEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-VRTR-MIB", "vRtrIfIndex"),
)
if mibBuilder.loadTexts:
    vRtrIgmpIfEntry.setStatus("current")
_VRtrIgmpIfRowStatus_Type = RowStatus
_VRtrIgmpIfRowStatus_Object = MibTableColumn
vRtrIgmpIfRowStatus = _VRtrIgmpIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 1, 1, 1),
    _VRtrIgmpIfRowStatus_Type()
)
vRtrIgmpIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIgmpIfRowStatus.setStatus("current")
_VRtrIgmpIfLastChangeTime_Type = TimeStamp
_VRtrIgmpIfLastChangeTime_Object = MibTableColumn
vRtrIgmpIfLastChangeTime = _VRtrIgmpIfLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 1, 1, 2),
    _VRtrIgmpIfLastChangeTime_Type()
)
vRtrIgmpIfLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpIfLastChangeTime.setStatus("current")


class _VRtrIgmpIfAdminState_Type(TmnxAdminState):
    """Custom type vRtrIgmpIfAdminState based on TmnxAdminState"""
    defaultValue = 2


_VRtrIgmpIfAdminState_Type.__name__ = "TmnxAdminState"
_VRtrIgmpIfAdminState_Object = MibTableColumn
vRtrIgmpIfAdminState = _VRtrIgmpIfAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 1, 1, 3),
    _VRtrIgmpIfAdminState_Type()
)
vRtrIgmpIfAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIgmpIfAdminState.setStatus("current")
_VRtrIgmpIfOperState_Type = TmnxOperState
_VRtrIgmpIfOperState_Object = MibTableColumn
vRtrIgmpIfOperState = _VRtrIgmpIfOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 1, 1, 4),
    _VRtrIgmpIfOperState_Type()
)
vRtrIgmpIfOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpIfOperState.setStatus("current")


class _VRtrIgmpIfAdminVersion_Type(Unsigned32):
    """Custom type vRtrIgmpIfAdminVersion based on Unsigned32"""
    defaultValue = 3


_VRtrIgmpIfAdminVersion_Type.__name__ = "Unsigned32"
_VRtrIgmpIfAdminVersion_Object = MibTableColumn
vRtrIgmpIfAdminVersion = _VRtrIgmpIfAdminVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 1, 1, 5),
    _VRtrIgmpIfAdminVersion_Type()
)
vRtrIgmpIfAdminVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIgmpIfAdminVersion.setStatus("current")
_VRtrIgmpIfOperVersion_Type = Unsigned32
_VRtrIgmpIfOperVersion_Object = MibTableColumn
vRtrIgmpIfOperVersion = _VRtrIgmpIfOperVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 1, 1, 6),
    _VRtrIgmpIfOperVersion_Type()
)
vRtrIgmpIfOperVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpIfOperVersion.setStatus("current")
_VRtrIgmpIfQuerier_Type = IpAddress
_VRtrIgmpIfQuerier_Object = MibTableColumn
vRtrIgmpIfQuerier = _VRtrIgmpIfQuerier_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 1, 1, 7),
    _VRtrIgmpIfQuerier_Type()
)
vRtrIgmpIfQuerier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpIfQuerier.setStatus("current")


class _VRtrIgmpIfImportPolicy_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrIgmpIfImportPolicy based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrIgmpIfImportPolicy_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrIgmpIfImportPolicy_Object = MibTableColumn
vRtrIgmpIfImportPolicy = _VRtrIgmpIfImportPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 1, 1, 8),
    _VRtrIgmpIfImportPolicy_Type()
)
vRtrIgmpIfImportPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIgmpIfImportPolicy.setStatus("current")
_VRtrIgmpIfGroupCount_Type = Unsigned32
_VRtrIgmpIfGroupCount_Object = MibTableColumn
vRtrIgmpIfGroupCount = _VRtrIgmpIfGroupCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 1, 1, 9),
    _VRtrIgmpIfGroupCount_Type()
)
vRtrIgmpIfGroupCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpIfGroupCount.setStatus("current")
_VRtrIgmpIfQuerierUpTime_Type = Unsigned32
_VRtrIgmpIfQuerierUpTime_Object = MibTableColumn
vRtrIgmpIfQuerierUpTime = _VRtrIgmpIfQuerierUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 1, 1, 10),
    _VRtrIgmpIfQuerierUpTime_Type()
)
vRtrIgmpIfQuerierUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpIfQuerierUpTime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrIgmpIfQuerierUpTime.setUnits("seconds")
_VRtrIgmpIfQuerierExpiryTime_Type = Unsigned32
_VRtrIgmpIfQuerierExpiryTime_Object = MibTableColumn
vRtrIgmpIfQuerierExpiryTime = _VRtrIgmpIfQuerierExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 1, 1, 11),
    _VRtrIgmpIfQuerierExpiryTime_Type()
)
vRtrIgmpIfQuerierExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpIfQuerierExpiryTime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrIgmpIfQuerierExpiryTime.setUnits("seconds")
_VRtrIgmpIfNextGenQueryTime_Type = Unsigned32
_VRtrIgmpIfNextGenQueryTime_Object = MibTableColumn
vRtrIgmpIfNextGenQueryTime = _VRtrIgmpIfNextGenQueryTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 1, 1, 12),
    _VRtrIgmpIfNextGenQueryTime_Type()
)
vRtrIgmpIfNextGenQueryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpIfNextGenQueryTime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrIgmpIfNextGenQueryTime.setUnits("seconds")


class _VRtrIgmpIfSubnetCheck_Type(TruthValue):
    """Custom type vRtrIgmpIfSubnetCheck based on TruthValue"""
    defaultValue = 1


_VRtrIgmpIfSubnetCheck_Type.__name__ = "TruthValue"
_VRtrIgmpIfSubnetCheck_Object = MibTableColumn
vRtrIgmpIfSubnetCheck = _VRtrIgmpIfSubnetCheck_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 1, 1, 13),
    _VRtrIgmpIfSubnetCheck_Type()
)
vRtrIgmpIfSubnetCheck.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIgmpIfSubnetCheck.setStatus("current")


class _VRtrIgmpIfMaxGroups_Type(Unsigned32):
    """Custom type vRtrIgmpIfMaxGroups based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 16000),
    )


_VRtrIgmpIfMaxGroups_Type.__name__ = "Unsigned32"
_VRtrIgmpIfMaxGroups_Object = MibTableColumn
vRtrIgmpIfMaxGroups = _VRtrIgmpIfMaxGroups_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 1, 1, 14),
    _VRtrIgmpIfMaxGroups_Type()
)
vRtrIgmpIfMaxGroups.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIgmpIfMaxGroups.setStatus("current")
_VRtrIgmpIfMaxGroupsTillNow_Type = Counter32
_VRtrIgmpIfMaxGroupsTillNow_Object = MibTableColumn
vRtrIgmpIfMaxGroupsTillNow = _VRtrIgmpIfMaxGroupsTillNow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 1, 1, 15),
    _VRtrIgmpIfMaxGroupsTillNow_Type()
)
vRtrIgmpIfMaxGroupsTillNow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpIfMaxGroupsTillNow.setStatus("current")


class _VRtrIgmpIfMcacPolicyName_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrIgmpIfMcacPolicyName based on TPolicyStatementNameOrEmpty"""
    defaultValue = OctetString("")


_VRtrIgmpIfMcacPolicyName_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrIgmpIfMcacPolicyName_Object = MibTableColumn
vRtrIgmpIfMcacPolicyName = _VRtrIgmpIfMcacPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 1, 1, 16),
    _VRtrIgmpIfMcacPolicyName_Type()
)
vRtrIgmpIfMcacPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIgmpIfMcacPolicyName.setStatus("current")


class _VRtrIgmpIfMcacUnconstrainedBW_Type(Integer32):
    """Custom type vRtrIgmpIfMcacUnconstrainedBW based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_VRtrIgmpIfMcacUnconstrainedBW_Type.__name__ = "Integer32"
_VRtrIgmpIfMcacUnconstrainedBW_Object = MibTableColumn
vRtrIgmpIfMcacUnconstrainedBW = _VRtrIgmpIfMcacUnconstrainedBW_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 1, 1, 17),
    _VRtrIgmpIfMcacUnconstrainedBW_Type()
)
vRtrIgmpIfMcacUnconstrainedBW.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIgmpIfMcacUnconstrainedBW.setStatus("current")
if mibBuilder.loadTexts:
    vRtrIgmpIfMcacUnconstrainedBW.setUnits("kbps")


class _VRtrIgmpIfMcacConstAdminState_Type(TmnxAdminState):
    """Custom type vRtrIgmpIfMcacConstAdminState based on TmnxAdminState"""
    defaultValue = 2


_VRtrIgmpIfMcacConstAdminState_Type.__name__ = "TmnxAdminState"
_VRtrIgmpIfMcacConstAdminState_Object = MibTableColumn
vRtrIgmpIfMcacConstAdminState = _VRtrIgmpIfMcacConstAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 1, 1, 18),
    _VRtrIgmpIfMcacConstAdminState_Type()
)
vRtrIgmpIfMcacConstAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIgmpIfMcacConstAdminState.setStatus("current")


class _VRtrIgmpIfMcacPreRsvdMandBW_Type(Integer32):
    """Custom type vRtrIgmpIfMcacPreRsvdMandBW based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_VRtrIgmpIfMcacPreRsvdMandBW_Type.__name__ = "Integer32"
_VRtrIgmpIfMcacPreRsvdMandBW_Object = MibTableColumn
vRtrIgmpIfMcacPreRsvdMandBW = _VRtrIgmpIfMcacPreRsvdMandBW_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 1, 1, 19),
    _VRtrIgmpIfMcacPreRsvdMandBW_Type()
)
vRtrIgmpIfMcacPreRsvdMandBW.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIgmpIfMcacPreRsvdMandBW.setStatus("current")
if mibBuilder.loadTexts:
    vRtrIgmpIfMcacPreRsvdMandBW.setUnits("kbps")
_VRtrIgmpIfMcacinUseMandBw_Type = Unsigned32
_VRtrIgmpIfMcacinUseMandBw_Object = MibTableColumn
vRtrIgmpIfMcacinUseMandBw = _VRtrIgmpIfMcacinUseMandBw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 1, 1, 20),
    _VRtrIgmpIfMcacinUseMandBw_Type()
)
vRtrIgmpIfMcacinUseMandBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpIfMcacinUseMandBw.setStatus("current")
if mibBuilder.loadTexts:
    vRtrIgmpIfMcacinUseMandBw.setUnits("kbps")
_VRtrIgmpIfMcacinUseOpnlBw_Type = Unsigned32
_VRtrIgmpIfMcacinUseOpnlBw_Object = MibTableColumn
vRtrIgmpIfMcacinUseOpnlBw = _VRtrIgmpIfMcacinUseOpnlBw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 1, 1, 21),
    _VRtrIgmpIfMcacinUseOpnlBw_Type()
)
vRtrIgmpIfMcacinUseOpnlBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpIfMcacinUseOpnlBw.setStatus("current")
if mibBuilder.loadTexts:
    vRtrIgmpIfMcacinUseOpnlBw.setUnits("kbps")
_VRtrIgmpIfMcacAvailMandBw_Type = Unsigned32
_VRtrIgmpIfMcacAvailMandBw_Object = MibTableColumn
vRtrIgmpIfMcacAvailMandBw = _VRtrIgmpIfMcacAvailMandBw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 1, 1, 22),
    _VRtrIgmpIfMcacAvailMandBw_Type()
)
vRtrIgmpIfMcacAvailMandBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpIfMcacAvailMandBw.setStatus("current")
if mibBuilder.loadTexts:
    vRtrIgmpIfMcacAvailMandBw.setUnits("kbps")
_VRtrIgmpIfMcacAvailOpnlBw_Type = Unsigned32
_VRtrIgmpIfMcacAvailOpnlBw_Object = MibTableColumn
vRtrIgmpIfMcacAvailOpnlBw = _VRtrIgmpIfMcacAvailOpnlBw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 1, 1, 23),
    _VRtrIgmpIfMcacAvailOpnlBw_Type()
)
vRtrIgmpIfMcacAvailOpnlBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpIfMcacAvailOpnlBw.setStatus("current")
if mibBuilder.loadTexts:
    vRtrIgmpIfMcacAvailOpnlBw.setUnits("kbps")
_VRtrIgmpIfMcacValuesInTransit_Type = TruthValue
_VRtrIgmpIfMcacValuesInTransit_Object = MibTableColumn
vRtrIgmpIfMcacValuesInTransit = _VRtrIgmpIfMcacValuesInTransit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 1, 1, 24),
    _VRtrIgmpIfMcacValuesInTransit_Type()
)
vRtrIgmpIfMcacValuesInTransit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpIfMcacValuesInTransit.setStatus("current")


class _VRtrIgmpIfDisRtrAlertChk_Type(TruthValue):
    """Custom type vRtrIgmpIfDisRtrAlertChk based on TruthValue"""
    defaultValue = 2


_VRtrIgmpIfDisRtrAlertChk_Type.__name__ = "TruthValue"
_VRtrIgmpIfDisRtrAlertChk_Object = MibTableColumn
vRtrIgmpIfDisRtrAlertChk = _VRtrIgmpIfDisRtrAlertChk_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 1, 1, 25),
    _VRtrIgmpIfDisRtrAlertChk_Type()
)
vRtrIgmpIfDisRtrAlertChk.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIgmpIfDisRtrAlertChk.setStatus("current")


class _VRtrIgmpIfMaxSources_Type(Unsigned32):
    """Custom type vRtrIgmpIfMaxSources based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1000),
    )


_VRtrIgmpIfMaxSources_Type.__name__ = "Unsigned32"
_VRtrIgmpIfMaxSources_Object = MibTableColumn
vRtrIgmpIfMaxSources = _VRtrIgmpIfMaxSources_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 1, 1, 26),
    _VRtrIgmpIfMaxSources_Type()
)
vRtrIgmpIfMaxSources.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIgmpIfMaxSources.setStatus("current")


class _VRtrIgmpIfMaxGrpSources_Type(Unsigned32):
    """Custom type vRtrIgmpIfMaxGrpSources based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 32000),
    )


_VRtrIgmpIfMaxGrpSources_Type.__name__ = "Unsigned32"
_VRtrIgmpIfMaxGrpSources_Object = MibTableColumn
vRtrIgmpIfMaxGrpSources = _VRtrIgmpIfMaxGrpSources_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 1, 1, 27),
    _VRtrIgmpIfMaxGrpSources_Type()
)
vRtrIgmpIfMaxGrpSources.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIgmpIfMaxGrpSources.setStatus("current")


class _VRtrIgmpIfQueryInterval_Type(Unsigned32):
    """Custom type vRtrIgmpIfQueryInterval based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2, 1024),
    )


_VRtrIgmpIfQueryInterval_Type.__name__ = "Unsigned32"
_VRtrIgmpIfQueryInterval_Object = MibTableColumn
vRtrIgmpIfQueryInterval = _VRtrIgmpIfQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 1, 1, 28),
    _VRtrIgmpIfQueryInterval_Type()
)
vRtrIgmpIfQueryInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIgmpIfQueryInterval.setStatus("current")
if mibBuilder.loadTexts:
    vRtrIgmpIfQueryInterval.setUnits("seconds")


class _VRtrIgmpIfLastMembQueryIntvl_Type(Unsigned32):
    """Custom type vRtrIgmpIfLastMembQueryIntvl based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1023),
    )


_VRtrIgmpIfLastMembQueryIntvl_Type.__name__ = "Unsigned32"
_VRtrIgmpIfLastMembQueryIntvl_Object = MibTableColumn
vRtrIgmpIfLastMembQueryIntvl = _VRtrIgmpIfLastMembQueryIntvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 1, 1, 29),
    _VRtrIgmpIfLastMembQueryIntvl_Type()
)
vRtrIgmpIfLastMembQueryIntvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIgmpIfLastMembQueryIntvl.setStatus("current")
if mibBuilder.loadTexts:
    vRtrIgmpIfLastMembQueryIntvl.setUnits("seconds")


class _VRtrIgmpIfQueryResponseIntvl_Type(Unsigned32):
    """Custom type vRtrIgmpIfQueryResponseIntvl based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1023),
    )


_VRtrIgmpIfQueryResponseIntvl_Type.__name__ = "Unsigned32"
_VRtrIgmpIfQueryResponseIntvl_Object = MibTableColumn
vRtrIgmpIfQueryResponseIntvl = _VRtrIgmpIfQueryResponseIntvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 1, 1, 30),
    _VRtrIgmpIfQueryResponseIntvl_Type()
)
vRtrIgmpIfQueryResponseIntvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIgmpIfQueryResponseIntvl.setStatus("current")
if mibBuilder.loadTexts:
    vRtrIgmpIfQueryResponseIntvl.setUnits("seconds")


class _VRtrIgmpIfMcacUseLagPortWeight_Type(TruthValue):
    """Custom type vRtrIgmpIfMcacUseLagPortWeight based on TruthValue"""
    defaultValue = 2


_VRtrIgmpIfMcacUseLagPortWeight_Type.__name__ = "TruthValue"
_VRtrIgmpIfMcacUseLagPortWeight_Object = MibTableColumn
vRtrIgmpIfMcacUseLagPortWeight = _VRtrIgmpIfMcacUseLagPortWeight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 1, 1, 31),
    _VRtrIgmpIfMcacUseLagPortWeight_Type()
)
vRtrIgmpIfMcacUseLagPortWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIgmpIfMcacUseLagPortWeight.setStatus("current")


class _VRtrIgmpIfRedundantMcast_Type(TruthValue):
    """Custom type vRtrIgmpIfRedundantMcast based on TruthValue"""
    defaultValue = 2


_VRtrIgmpIfRedundantMcast_Type.__name__ = "TruthValue"
_VRtrIgmpIfRedundantMcast_Object = MibTableColumn
vRtrIgmpIfRedundantMcast = _VRtrIgmpIfRedundantMcast_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 1, 1, 32),
    _VRtrIgmpIfRedundantMcast_Type()
)
vRtrIgmpIfRedundantMcast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIgmpIfRedundantMcast.setStatus("current")


class _VRtrIgmpIfRedundantMcastFwding_Type(TruthValue):
    """Custom type vRtrIgmpIfRedundantMcastFwding based on TruthValue"""
    defaultValue = 2


_VRtrIgmpIfRedundantMcastFwding_Type.__name__ = "TruthValue"
_VRtrIgmpIfRedundantMcastFwding_Object = MibTableColumn
vRtrIgmpIfRedundantMcastFwding = _VRtrIgmpIfRedundantMcastFwding_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 1, 1, 33),
    _VRtrIgmpIfRedundantMcastFwding_Type()
)
vRtrIgmpIfRedundantMcastFwding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpIfRedundantMcastFwding.setStatus("current")
_VRtrIgmpIfGroupTable_Object = MibTable
vRtrIgmpIfGroupTable = _VRtrIgmpIfGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 2)
)
if mibBuilder.loadTexts:
    vRtrIgmpIfGroupTable.setStatus("current")
_VRtrIgmpIfGroupEntry_Object = MibTableRow
vRtrIgmpIfGroupEntry = _VRtrIgmpIfGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 2, 1)
)
vRtrIgmpIfGroupEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-VRTR-MIB", "vRtrIfIndex"),
    (0, "TIMETRA-IGMP-MIB", "vRtrIgmpIfGroupAddress"),
)
if mibBuilder.loadTexts:
    vRtrIgmpIfGroupEntry.setStatus("current")
_VRtrIgmpIfGroupAddress_Type = IpAddress
_VRtrIgmpIfGroupAddress_Object = MibTableColumn
vRtrIgmpIfGroupAddress = _VRtrIgmpIfGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 2, 1, 1),
    _VRtrIgmpIfGroupAddress_Type()
)
vRtrIgmpIfGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrIgmpIfGroupAddress.setStatus("current")
_VRtrIgmpIfGroupType_Type = TmnxIgmpGroupType
_VRtrIgmpIfGroupType_Object = MibTableColumn
vRtrIgmpIfGroupType = _VRtrIgmpIfGroupType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 2, 1, 2),
    _VRtrIgmpIfGroupType_Type()
)
vRtrIgmpIfGroupType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpIfGroupType.setStatus("current")
_VRtrIgmpIfGroupUpTime_Type = TimeTicks
_VRtrIgmpIfGroupUpTime_Object = MibTableColumn
vRtrIgmpIfGroupUpTime = _VRtrIgmpIfGroupUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 2, 1, 3),
    _VRtrIgmpIfGroupUpTime_Type()
)
vRtrIgmpIfGroupUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpIfGroupUpTime.setStatus("current")
_VRtrIgmpIfGroupExpiryTime_Type = TimeTicks
_VRtrIgmpIfGroupExpiryTime_Object = MibTableColumn
vRtrIgmpIfGroupExpiryTime = _VRtrIgmpIfGroupExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 2, 1, 4),
    _VRtrIgmpIfGroupExpiryTime_Type()
)
vRtrIgmpIfGroupExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpIfGroupExpiryTime.setStatus("current")
_VRtrIgmpIfGroupVersion1HostTimer_Type = TimeTicks
_VRtrIgmpIfGroupVersion1HostTimer_Object = MibTableColumn
vRtrIgmpIfGroupVersion1HostTimer = _VRtrIgmpIfGroupVersion1HostTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 2, 1, 5),
    _VRtrIgmpIfGroupVersion1HostTimer_Type()
)
vRtrIgmpIfGroupVersion1HostTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpIfGroupVersion1HostTimer.setStatus("current")
_VRtrIgmpIfGroupMode_Type = TmnxIgmpGroupFilterMode
_VRtrIgmpIfGroupMode_Object = MibTableColumn
vRtrIgmpIfGroupMode = _VRtrIgmpIfGroupMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 2, 1, 6),
    _VRtrIgmpIfGroupMode_Type()
)
vRtrIgmpIfGroupMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpIfGroupMode.setStatus("current")
_VRtrIgmpIfGroupCompatMode_Type = Unsigned32
_VRtrIgmpIfGroupCompatMode_Object = MibTableColumn
vRtrIgmpIfGroupCompatMode = _VRtrIgmpIfGroupCompatMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 2, 1, 7),
    _VRtrIgmpIfGroupCompatMode_Type()
)
vRtrIgmpIfGroupCompatMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpIfGroupCompatMode.setStatus("current")
_VRtrIgmpIfGroupVersion2HostTimer_Type = TimeTicks
_VRtrIgmpIfGroupVersion2HostTimer_Object = MibTableColumn
vRtrIgmpIfGroupVersion2HostTimer = _VRtrIgmpIfGroupVersion2HostTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 2, 1, 8),
    _VRtrIgmpIfGroupVersion2HostTimer_Type()
)
vRtrIgmpIfGroupVersion2HostTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpIfGroupVersion2HostTimer.setStatus("current")
_VRtrIgmpIfGroupLastReporter_Type = IpAddress
_VRtrIgmpIfGroupLastReporter_Object = MibTableColumn
vRtrIgmpIfGroupLastReporter = _VRtrIgmpIfGroupLastReporter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 2, 1, 9),
    _VRtrIgmpIfGroupLastReporter_Type()
)
vRtrIgmpIfGroupLastReporter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpIfGroupLastReporter.setStatus("current")
_VRtrIgmpIfGrpSrcTable_Object = MibTable
vRtrIgmpIfGrpSrcTable = _VRtrIgmpIfGrpSrcTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 3)
)
if mibBuilder.loadTexts:
    vRtrIgmpIfGrpSrcTable.setStatus("current")
_VRtrIgmpIfGrpSrcEntry_Object = MibTableRow
vRtrIgmpIfGrpSrcEntry = _VRtrIgmpIfGrpSrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 3, 1)
)
vRtrIgmpIfGrpSrcEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-VRTR-MIB", "vRtrIfIndex"),
    (0, "TIMETRA-IGMP-MIB", "vRtrIgmpIfGroupAddress"),
    (0, "TIMETRA-IGMP-MIB", "vRtrIgmpIfGrpSrcAddress"),
)
if mibBuilder.loadTexts:
    vRtrIgmpIfGrpSrcEntry.setStatus("current")
_VRtrIgmpIfGrpSrcAddress_Type = IpAddress
_VRtrIgmpIfGrpSrcAddress_Object = MibTableColumn
vRtrIgmpIfGrpSrcAddress = _VRtrIgmpIfGrpSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 3, 1, 1),
    _VRtrIgmpIfGrpSrcAddress_Type()
)
vRtrIgmpIfGrpSrcAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrIgmpIfGrpSrcAddress.setStatus("current")
_VRtrIgmpIfGrpSrcExpiryTime_Type = TimeTicks
_VRtrIgmpIfGrpSrcExpiryTime_Object = MibTableColumn
vRtrIgmpIfGrpSrcExpiryTime = _VRtrIgmpIfGrpSrcExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 3, 1, 2),
    _VRtrIgmpIfGrpSrcExpiryTime_Type()
)
vRtrIgmpIfGrpSrcExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpIfGrpSrcExpiryTime.setStatus("current")
_VRtrIgmpIfGrpSrcType_Type = TmnxIgmpGroupType
_VRtrIgmpIfGrpSrcType_Object = MibTableColumn
vRtrIgmpIfGrpSrcType = _VRtrIgmpIfGrpSrcType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 3, 1, 3),
    _VRtrIgmpIfGrpSrcType_Type()
)
vRtrIgmpIfGrpSrcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpIfGrpSrcType.setStatus("current")
_VRtrIgmpIfStaticGrpSrcTable_Object = MibTable
vRtrIgmpIfStaticGrpSrcTable = _VRtrIgmpIfStaticGrpSrcTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 4)
)
if mibBuilder.loadTexts:
    vRtrIgmpIfStaticGrpSrcTable.setStatus("current")
_VRtrIgmpIfStaticGrpSrcEntry_Object = MibTableRow
vRtrIgmpIfStaticGrpSrcEntry = _VRtrIgmpIfStaticGrpSrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 4, 1)
)
vRtrIgmpIfStaticGrpSrcEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-VRTR-MIB", "vRtrIfIndex"),
    (0, "TIMETRA-IGMP-MIB", "vRtrIgmpIfGroupAddress"),
    (0, "TIMETRA-IGMP-MIB", "vRtrIgmpIfGrpSrcAddress"),
)
if mibBuilder.loadTexts:
    vRtrIgmpIfStaticGrpSrcEntry.setStatus("current")
_VRtrIgmpIfStaticGrpSrcRowStatus_Type = RowStatus
_VRtrIgmpIfStaticGrpSrcRowStatus_Object = MibTableColumn
vRtrIgmpIfStaticGrpSrcRowStatus = _VRtrIgmpIfStaticGrpSrcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 4, 1, 1),
    _VRtrIgmpIfStaticGrpSrcRowStatus_Type()
)
vRtrIgmpIfStaticGrpSrcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIgmpIfStaticGrpSrcRowStatus.setStatus("current")
_VRtrIgmpIfStatsTable_Object = MibTable
vRtrIgmpIfStatsTable = _VRtrIgmpIfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 5)
)
if mibBuilder.loadTexts:
    vRtrIgmpIfStatsTable.setStatus("current")
_VRtrIgmpIfStatsEntry_Object = MibTableRow
vRtrIgmpIfStatsEntry = _VRtrIgmpIfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 5, 1)
)
if mibBuilder.loadTexts:
    vRtrIgmpIfStatsEntry.setStatus("current")
_VRtrIgmpIfTxGenQueries_Type = Counter32
_VRtrIgmpIfTxGenQueries_Object = MibTableColumn
vRtrIgmpIfTxGenQueries = _VRtrIgmpIfTxGenQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 5, 1, 1),
    _VRtrIgmpIfTxGenQueries_Type()
)
vRtrIgmpIfTxGenQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpIfTxGenQueries.setStatus("current")
_VRtrIgmpIfTxGrpQueries_Type = Counter32
_VRtrIgmpIfTxGrpQueries_Object = MibTableColumn
vRtrIgmpIfTxGrpQueries = _VRtrIgmpIfTxGrpQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 5, 1, 2),
    _VRtrIgmpIfTxGrpQueries_Type()
)
vRtrIgmpIfTxGrpQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpIfTxGrpQueries.setStatus("current")
_VRtrIgmpIfTxGrpSrcQueries_Type = Counter32
_VRtrIgmpIfTxGrpSrcQueries_Object = MibTableColumn
vRtrIgmpIfTxGrpSrcQueries = _VRtrIgmpIfTxGrpSrcQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 5, 1, 3),
    _VRtrIgmpIfTxGrpSrcQueries_Type()
)
vRtrIgmpIfTxGrpSrcQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpIfTxGrpSrcQueries.setStatus("current")
_VRtrIgmpIfTxV1Reports_Type = Counter32
_VRtrIgmpIfTxV1Reports_Object = MibTableColumn
vRtrIgmpIfTxV1Reports = _VRtrIgmpIfTxV1Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 5, 1, 4),
    _VRtrIgmpIfTxV1Reports_Type()
)
vRtrIgmpIfTxV1Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpIfTxV1Reports.setStatus("current")
_VRtrIgmpIfTxV2Reports_Type = Counter32
_VRtrIgmpIfTxV2Reports_Object = MibTableColumn
vRtrIgmpIfTxV2Reports = _VRtrIgmpIfTxV2Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 5, 1, 5),
    _VRtrIgmpIfTxV2Reports_Type()
)
vRtrIgmpIfTxV2Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpIfTxV2Reports.setStatus("current")
_VRtrIgmpIfTxV3Reports_Type = Counter32
_VRtrIgmpIfTxV3Reports_Object = MibTableColumn
vRtrIgmpIfTxV3Reports = _VRtrIgmpIfTxV3Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 5, 1, 6),
    _VRtrIgmpIfTxV3Reports_Type()
)
vRtrIgmpIfTxV3Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpIfTxV3Reports.setStatus("current")
_VRtrIgmpIfTxLeaves_Type = Counter32
_VRtrIgmpIfTxLeaves_Object = MibTableColumn
vRtrIgmpIfTxLeaves = _VRtrIgmpIfTxLeaves_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 5, 1, 7),
    _VRtrIgmpIfTxLeaves_Type()
)
vRtrIgmpIfTxLeaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpIfTxLeaves.setStatus("current")
_VRtrIgmpIfTxErrors_Type = Counter32
_VRtrIgmpIfTxErrors_Object = MibTableColumn
vRtrIgmpIfTxErrors = _VRtrIgmpIfTxErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 5, 1, 8),
    _VRtrIgmpIfTxErrors_Type()
)
vRtrIgmpIfTxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpIfTxErrors.setStatus("current")
_VRtrIgmpIfRxGenQueries_Type = Counter32
_VRtrIgmpIfRxGenQueries_Object = MibTableColumn
vRtrIgmpIfRxGenQueries = _VRtrIgmpIfRxGenQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 5, 1, 9),
    _VRtrIgmpIfRxGenQueries_Type()
)
vRtrIgmpIfRxGenQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpIfRxGenQueries.setStatus("current")
_VRtrIgmpIfRxGrpQueries_Type = Counter32
_VRtrIgmpIfRxGrpQueries_Object = MibTableColumn
vRtrIgmpIfRxGrpQueries = _VRtrIgmpIfRxGrpQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 5, 1, 10),
    _VRtrIgmpIfRxGrpQueries_Type()
)
vRtrIgmpIfRxGrpQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpIfRxGrpQueries.setStatus("current")
_VRtrIgmpIfRxGrpSrcQueries_Type = Counter32
_VRtrIgmpIfRxGrpSrcQueries_Object = MibTableColumn
vRtrIgmpIfRxGrpSrcQueries = _VRtrIgmpIfRxGrpSrcQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 5, 1, 11),
    _VRtrIgmpIfRxGrpSrcQueries_Type()
)
vRtrIgmpIfRxGrpSrcQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpIfRxGrpSrcQueries.setStatus("current")
_VRtrIgmpIfRxV1Reports_Type = Counter32
_VRtrIgmpIfRxV1Reports_Object = MibTableColumn
vRtrIgmpIfRxV1Reports = _VRtrIgmpIfRxV1Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 5, 1, 12),
    _VRtrIgmpIfRxV1Reports_Type()
)
vRtrIgmpIfRxV1Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpIfRxV1Reports.setStatus("current")
_VRtrIgmpIfRxV2Reports_Type = Counter32
_VRtrIgmpIfRxV2Reports_Object = MibTableColumn
vRtrIgmpIfRxV2Reports = _VRtrIgmpIfRxV2Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 5, 1, 13),
    _VRtrIgmpIfRxV2Reports_Type()
)
vRtrIgmpIfRxV2Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpIfRxV2Reports.setStatus("current")
_VRtrIgmpIfRxV3Reports_Type = Counter32
_VRtrIgmpIfRxV3Reports_Object = MibTableColumn
vRtrIgmpIfRxV3Reports = _VRtrIgmpIfRxV3Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 5, 1, 14),
    _VRtrIgmpIfRxV3Reports_Type()
)
vRtrIgmpIfRxV3Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpIfRxV3Reports.setStatus("current")
_VRtrIgmpIfRxLeaves_Type = Counter32
_VRtrIgmpIfRxLeaves_Object = MibTableColumn
vRtrIgmpIfRxLeaves = _VRtrIgmpIfRxLeaves_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 5, 1, 15),
    _VRtrIgmpIfRxLeaves_Type()
)
vRtrIgmpIfRxLeaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpIfRxLeaves.setStatus("current")
_VRtrIgmpIfRxBadLenPkts_Type = Counter32
_VRtrIgmpIfRxBadLenPkts_Object = MibTableColumn
vRtrIgmpIfRxBadLenPkts = _VRtrIgmpIfRxBadLenPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 5, 1, 16),
    _VRtrIgmpIfRxBadLenPkts_Type()
)
vRtrIgmpIfRxBadLenPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpIfRxBadLenPkts.setStatus("current")
_VRtrIgmpIfRxBadChecksumPkts_Type = Counter32
_VRtrIgmpIfRxBadChecksumPkts_Object = MibTableColumn
vRtrIgmpIfRxBadChecksumPkts = _VRtrIgmpIfRxBadChecksumPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 5, 1, 17),
    _VRtrIgmpIfRxBadChecksumPkts_Type()
)
vRtrIgmpIfRxBadChecksumPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpIfRxBadChecksumPkts.setStatus("current")
_VRtrIgmpIfRxUnknownTypePkts_Type = Counter32
_VRtrIgmpIfRxUnknownTypePkts_Object = MibTableColumn
vRtrIgmpIfRxUnknownTypePkts = _VRtrIgmpIfRxUnknownTypePkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 5, 1, 18),
    _VRtrIgmpIfRxUnknownTypePkts_Type()
)
vRtrIgmpIfRxUnknownTypePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpIfRxUnknownTypePkts.setStatus("current")
_VRtrIgmpIfRxBadReceiveIfPkts_Type = Counter32
_VRtrIgmpIfRxBadReceiveIfPkts_Object = MibTableColumn
vRtrIgmpIfRxBadReceiveIfPkts = _VRtrIgmpIfRxBadReceiveIfPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 5, 1, 19),
    _VRtrIgmpIfRxBadReceiveIfPkts_Type()
)
vRtrIgmpIfRxBadReceiveIfPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpIfRxBadReceiveIfPkts.setStatus("current")
_VRtrIgmpIfRxNonLocal_Type = Counter32
_VRtrIgmpIfRxNonLocal_Object = MibTableColumn
vRtrIgmpIfRxNonLocal = _VRtrIgmpIfRxNonLocal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 5, 1, 20),
    _VRtrIgmpIfRxNonLocal_Type()
)
vRtrIgmpIfRxNonLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpIfRxNonLocal.setStatus("current")
_VRtrIgmpIfRxWrongVersions_Type = Counter32
_VRtrIgmpIfRxWrongVersions_Object = MibTableColumn
vRtrIgmpIfRxWrongVersions = _VRtrIgmpIfRxWrongVersions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 5, 1, 21),
    _VRtrIgmpIfRxWrongVersions_Type()
)
vRtrIgmpIfRxWrongVersions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpIfRxWrongVersions.setStatus("current")
_VRtrIgmpIfImportPolicyDrops_Type = Counter32
_VRtrIgmpIfImportPolicyDrops_Object = MibTableColumn
vRtrIgmpIfImportPolicyDrops = _VRtrIgmpIfImportPolicyDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 5, 1, 22),
    _VRtrIgmpIfImportPolicyDrops_Type()
)
vRtrIgmpIfImportPolicyDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpIfImportPolicyDrops.setStatus("current")
_VRtrIgmpIfRxNoRtrAlertPkts_Type = Counter32
_VRtrIgmpIfRxNoRtrAlertPkts_Object = MibTableColumn
vRtrIgmpIfRxNoRtrAlertPkts = _VRtrIgmpIfRxNoRtrAlertPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 5, 1, 23),
    _VRtrIgmpIfRxNoRtrAlertPkts_Type()
)
vRtrIgmpIfRxNoRtrAlertPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpIfRxNoRtrAlertPkts.setStatus("current")
_VRtrIgmpIfRxBadEncodings_Type = Counter32
_VRtrIgmpIfRxBadEncodings_Object = MibTableColumn
vRtrIgmpIfRxBadEncodings = _VRtrIgmpIfRxBadEncodings_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 5, 1, 24),
    _VRtrIgmpIfRxBadEncodings_Type()
)
vRtrIgmpIfRxBadEncodings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpIfRxBadEncodings.setStatus("current")
_VRtrIgmpIfRxPktDrops_Type = Counter32
_VRtrIgmpIfRxPktDrops_Object = MibTableColumn
vRtrIgmpIfRxPktDrops = _VRtrIgmpIfRxPktDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 5, 1, 25),
    _VRtrIgmpIfRxPktDrops_Type()
)
vRtrIgmpIfRxPktDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpIfRxPktDrops.setStatus("current")
_VRtrIgmpIfStatsStarGTypes_Type = Gauge32
_VRtrIgmpIfStatsStarGTypes_Object = MibTableColumn
vRtrIgmpIfStatsStarGTypes = _VRtrIgmpIfStatsStarGTypes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 5, 1, 26),
    _VRtrIgmpIfStatsStarGTypes_Type()
)
vRtrIgmpIfStatsStarGTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpIfStatsStarGTypes.setStatus("current")
_VRtrIgmpIfStatsSGTypes_Type = Gauge32
_VRtrIgmpIfStatsSGTypes_Object = MibTableColumn
vRtrIgmpIfStatsSGTypes = _VRtrIgmpIfStatsSGTypes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 5, 1, 27),
    _VRtrIgmpIfStatsSGTypes_Type()
)
vRtrIgmpIfStatsSGTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpIfStatsSGTypes.setStatus("current")
_VRtrIgmpIfStatsMcacPolicyDrops_Type = Counter32
_VRtrIgmpIfStatsMcacPolicyDrops_Object = MibTableColumn
vRtrIgmpIfStatsMcacPolicyDrops = _VRtrIgmpIfStatsMcacPolicyDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 5, 1, 28),
    _VRtrIgmpIfStatsMcacPolicyDrops_Type()
)
vRtrIgmpIfStatsMcacPolicyDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpIfStatsMcacPolicyDrops.setStatus("current")
_VRtrIgmpIfRxLocalScopePkts_Type = Counter32
_VRtrIgmpIfRxLocalScopePkts_Object = MibTableColumn
vRtrIgmpIfRxLocalScopePkts = _VRtrIgmpIfRxLocalScopePkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 5, 1, 29),
    _VRtrIgmpIfRxLocalScopePkts_Type()
)
vRtrIgmpIfRxLocalScopePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpIfRxLocalScopePkts.setStatus("current")
_VRtrIgmpIfRxRsvdScopePkts_Type = Counter32
_VRtrIgmpIfRxRsvdScopePkts_Object = MibTableColumn
vRtrIgmpIfRxRsvdScopePkts = _VRtrIgmpIfRxRsvdScopePkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 5, 1, 30),
    _VRtrIgmpIfRxRsvdScopePkts_Type()
)
vRtrIgmpIfRxRsvdScopePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpIfRxRsvdScopePkts.setStatus("current")
_VRtrIgmpIfMcacLevelTable_Object = MibTable
vRtrIgmpIfMcacLevelTable = _VRtrIgmpIfMcacLevelTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 6)
)
if mibBuilder.loadTexts:
    vRtrIgmpIfMcacLevelTable.setStatus("current")
_VRtrIgmpIfMcacLevelEntry_Object = MibTableRow
vRtrIgmpIfMcacLevelEntry = _VRtrIgmpIfMcacLevelEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 6, 1)
)
vRtrIgmpIfMcacLevelEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-VRTR-MIB", "vRtrIfIndex"),
    (0, "TIMETRA-MCAST-CAC-MIB", "tmnxMcacLevelId"),
)
if mibBuilder.loadTexts:
    vRtrIgmpIfMcacLevelEntry.setStatus("current")
_VRtrIgmpIfMcacLevelRowStatus_Type = RowStatus
_VRtrIgmpIfMcacLevelRowStatus_Object = MibTableColumn
vRtrIgmpIfMcacLevelRowStatus = _VRtrIgmpIfMcacLevelRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 6, 1, 1),
    _VRtrIgmpIfMcacLevelRowStatus_Type()
)
vRtrIgmpIfMcacLevelRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIgmpIfMcacLevelRowStatus.setStatus("current")


class _VRtrIgmpIfMcacLevelBW_Type(Unsigned32):
    """Custom type vRtrIgmpIfMcacLevelBW based on Unsigned32"""
    defaultValue = 1


_VRtrIgmpIfMcacLevelBW_Type.__name__ = "Unsigned32"
_VRtrIgmpIfMcacLevelBW_Object = MibTableColumn
vRtrIgmpIfMcacLevelBW = _VRtrIgmpIfMcacLevelBW_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 6, 1, 2),
    _VRtrIgmpIfMcacLevelBW_Type()
)
vRtrIgmpIfMcacLevelBW.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIgmpIfMcacLevelBW.setStatus("current")
if mibBuilder.loadTexts:
    vRtrIgmpIfMcacLevelBW.setUnits("kbps")
_VRtrIgmpIfMcacLagTable_Object = MibTable
vRtrIgmpIfMcacLagTable = _VRtrIgmpIfMcacLagTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 7)
)
if mibBuilder.loadTexts:
    vRtrIgmpIfMcacLagTable.setStatus("current")
_VRtrIgmpIfMcacLagEntry_Object = MibTableRow
vRtrIgmpIfMcacLagEntry = _VRtrIgmpIfMcacLagEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 7, 1)
)
vRtrIgmpIfMcacLagEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-VRTR-MIB", "vRtrIfIndex"),
    (0, "TIMETRA-MCAST-CAC-MIB", "tmnxMcacLagPortsDown"),
)
if mibBuilder.loadTexts:
    vRtrIgmpIfMcacLagEntry.setStatus("current")
_VRtrIgmpIfMcacLagRowStatus_Type = RowStatus
_VRtrIgmpIfMcacLagRowStatus_Object = MibTableColumn
vRtrIgmpIfMcacLagRowStatus = _VRtrIgmpIfMcacLagRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 7, 1, 1),
    _VRtrIgmpIfMcacLagRowStatus_Type()
)
vRtrIgmpIfMcacLagRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIgmpIfMcacLagRowStatus.setStatus("current")


class _VRtrIgmpIfMcacLagLevel_Type(Unsigned32):
    """Custom type vRtrIgmpIfMcacLagLevel based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_VRtrIgmpIfMcacLagLevel_Type.__name__ = "Unsigned32"
_VRtrIgmpIfMcacLagLevel_Object = MibTableColumn
vRtrIgmpIfMcacLagLevel = _VRtrIgmpIfMcacLagLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 7, 1, 2),
    _VRtrIgmpIfMcacLagLevel_Type()
)
vRtrIgmpIfMcacLagLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIgmpIfMcacLagLevel.setStatus("current")
_VRtrIgmpIfSSMTltTableLastChanged_Type = TimeStamp
_VRtrIgmpIfSSMTltTableLastChanged_Object = MibScalar
vRtrIgmpIfSSMTltTableLastChanged = _VRtrIgmpIfSSMTltTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 8),
    _VRtrIgmpIfSSMTltTableLastChanged_Type()
)
vRtrIgmpIfSSMTltTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpIfSSMTltTableLastChanged.setStatus("current")
_VRtrIgmpIfSSMTransTable_Object = MibTable
vRtrIgmpIfSSMTransTable = _VRtrIgmpIfSSMTransTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 9)
)
if mibBuilder.loadTexts:
    vRtrIgmpIfSSMTransTable.setStatus("current")
_VRtrIgmpIfSSMTransEntry_Object = MibTableRow
vRtrIgmpIfSSMTransEntry = _VRtrIgmpIfSSMTransEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 9, 1)
)
vRtrIgmpIfSSMTransEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-VRTR-MIB", "vRtrIfIndex"),
    (0, "TIMETRA-IGMP-MIB", "vRtrIgmpIfSSMTransGrpAddrType1"),
    (0, "TIMETRA-IGMP-MIB", "vRtrIgmpIfSSMTransGrpAddr1"),
    (0, "TIMETRA-IGMP-MIB", "vRtrIgmpIfSSMTransGrpAddrType2"),
    (0, "TIMETRA-IGMP-MIB", "vRtrIgmpIfSSMTransGrpAddr2"),
    (0, "TIMETRA-IGMP-MIB", "vRtrIgmpIfSSMTransSrcAddrType"),
    (0, "TIMETRA-IGMP-MIB", "vRtrIgmpIfSSMTransSrcAddr"),
)
if mibBuilder.loadTexts:
    vRtrIgmpIfSSMTransEntry.setStatus("current")
_VRtrIgmpIfSSMTransGrpAddrType1_Type = InetAddressType
_VRtrIgmpIfSSMTransGrpAddrType1_Object = MibTableColumn
vRtrIgmpIfSSMTransGrpAddrType1 = _VRtrIgmpIfSSMTransGrpAddrType1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 9, 1, 1),
    _VRtrIgmpIfSSMTransGrpAddrType1_Type()
)
vRtrIgmpIfSSMTransGrpAddrType1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrIgmpIfSSMTransGrpAddrType1.setStatus("current")


class _VRtrIgmpIfSSMTransGrpAddr1_Type(InetAddress):
    """Custom type vRtrIgmpIfSSMTransGrpAddr1 based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_VRtrIgmpIfSSMTransGrpAddr1_Type.__name__ = "InetAddress"
_VRtrIgmpIfSSMTransGrpAddr1_Object = MibTableColumn
vRtrIgmpIfSSMTransGrpAddr1 = _VRtrIgmpIfSSMTransGrpAddr1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 9, 1, 2),
    _VRtrIgmpIfSSMTransGrpAddr1_Type()
)
vRtrIgmpIfSSMTransGrpAddr1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrIgmpIfSSMTransGrpAddr1.setStatus("current")
_VRtrIgmpIfSSMTransGrpAddrType2_Type = InetAddressType
_VRtrIgmpIfSSMTransGrpAddrType2_Object = MibTableColumn
vRtrIgmpIfSSMTransGrpAddrType2 = _VRtrIgmpIfSSMTransGrpAddrType2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 9, 1, 3),
    _VRtrIgmpIfSSMTransGrpAddrType2_Type()
)
vRtrIgmpIfSSMTransGrpAddrType2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrIgmpIfSSMTransGrpAddrType2.setStatus("current")


class _VRtrIgmpIfSSMTransGrpAddr2_Type(InetAddress):
    """Custom type vRtrIgmpIfSSMTransGrpAddr2 based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_VRtrIgmpIfSSMTransGrpAddr2_Type.__name__ = "InetAddress"
_VRtrIgmpIfSSMTransGrpAddr2_Object = MibTableColumn
vRtrIgmpIfSSMTransGrpAddr2 = _VRtrIgmpIfSSMTransGrpAddr2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 9, 1, 4),
    _VRtrIgmpIfSSMTransGrpAddr2_Type()
)
vRtrIgmpIfSSMTransGrpAddr2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrIgmpIfSSMTransGrpAddr2.setStatus("current")
_VRtrIgmpIfSSMTransSrcAddrType_Type = InetAddressType
_VRtrIgmpIfSSMTransSrcAddrType_Object = MibTableColumn
vRtrIgmpIfSSMTransSrcAddrType = _VRtrIgmpIfSSMTransSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 9, 1, 5),
    _VRtrIgmpIfSSMTransSrcAddrType_Type()
)
vRtrIgmpIfSSMTransSrcAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrIgmpIfSSMTransSrcAddrType.setStatus("current")


class _VRtrIgmpIfSSMTransSrcAddr_Type(InetAddress):
    """Custom type vRtrIgmpIfSSMTransSrcAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_VRtrIgmpIfSSMTransSrcAddr_Type.__name__ = "InetAddress"
_VRtrIgmpIfSSMTransSrcAddr_Object = MibTableColumn
vRtrIgmpIfSSMTransSrcAddr = _VRtrIgmpIfSSMTransSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 9, 1, 6),
    _VRtrIgmpIfSSMTransSrcAddr_Type()
)
vRtrIgmpIfSSMTransSrcAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrIgmpIfSSMTransSrcAddr.setStatus("current")
_VRtrIgmpIfSSMTransRowStatus_Type = RowStatus
_VRtrIgmpIfSSMTransRowStatus_Object = MibTableColumn
vRtrIgmpIfSSMTransRowStatus = _VRtrIgmpIfSSMTransRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 9, 1, 7),
    _VRtrIgmpIfSSMTransRowStatus_Type()
)
vRtrIgmpIfSSMTransRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIgmpIfSSMTransRowStatus.setStatus("current")
_VRtrIgmpRsvpIfTable_Object = MibTable
vRtrIgmpRsvpIfTable = _VRtrIgmpRsvpIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 10)
)
if mibBuilder.loadTexts:
    vRtrIgmpRsvpIfTable.setStatus("current")
_VRtrIgmpRsvpIfEntry_Object = MibTableRow
vRtrIgmpRsvpIfEntry = _VRtrIgmpRsvpIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 10, 1)
)
vRtrIgmpRsvpIfEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-IGMP-MIB", "vRtrIgmpRsvpIfLspName"),
    (0, "TIMETRA-IGMP-MIB", "vRtrIgmpRsvpIfSenderAddrType"),
    (0, "TIMETRA-IGMP-MIB", "vRtrIgmpRsvpIfSenderAddr"),
)
if mibBuilder.loadTexts:
    vRtrIgmpRsvpIfEntry.setStatus("current")
_VRtrIgmpRsvpIfLspName_Type = TNamedItem
_VRtrIgmpRsvpIfLspName_Object = MibTableColumn
vRtrIgmpRsvpIfLspName = _VRtrIgmpRsvpIfLspName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 10, 1, 1),
    _VRtrIgmpRsvpIfLspName_Type()
)
vRtrIgmpRsvpIfLspName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrIgmpRsvpIfLspName.setStatus("current")
_VRtrIgmpRsvpIfSenderAddrType_Type = InetAddressType
_VRtrIgmpRsvpIfSenderAddrType_Object = MibTableColumn
vRtrIgmpRsvpIfSenderAddrType = _VRtrIgmpRsvpIfSenderAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 10, 1, 2),
    _VRtrIgmpRsvpIfSenderAddrType_Type()
)
vRtrIgmpRsvpIfSenderAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrIgmpRsvpIfSenderAddrType.setStatus("current")


class _VRtrIgmpRsvpIfSenderAddr_Type(InetAddress):
    """Custom type vRtrIgmpRsvpIfSenderAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_VRtrIgmpRsvpIfSenderAddr_Type.__name__ = "InetAddress"
_VRtrIgmpRsvpIfSenderAddr_Object = MibTableColumn
vRtrIgmpRsvpIfSenderAddr = _VRtrIgmpRsvpIfSenderAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 10, 1, 3),
    _VRtrIgmpRsvpIfSenderAddr_Type()
)
vRtrIgmpRsvpIfSenderAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrIgmpRsvpIfSenderAddr.setStatus("current")
_VRtrIgmpRsvpIfRowStatus_Type = RowStatus
_VRtrIgmpRsvpIfRowStatus_Object = MibTableColumn
vRtrIgmpRsvpIfRowStatus = _VRtrIgmpRsvpIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 10, 1, 4),
    _VRtrIgmpRsvpIfRowStatus_Type()
)
vRtrIgmpRsvpIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIgmpRsvpIfRowStatus.setStatus("current")
_VRtrIgmpRsvpIfIndex_Type = InterfaceIndex
_VRtrIgmpRsvpIfIndex_Object = MibTableColumn
vRtrIgmpRsvpIfIndex = _VRtrIgmpRsvpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 10, 1, 5),
    _VRtrIgmpRsvpIfIndex_Type()
)
vRtrIgmpRsvpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpRsvpIfIndex.setStatus("current")


class _VRtrIgmpRsvpIfBfdEnable_Type(TruthValue):
    """Custom type vRtrIgmpRsvpIfBfdEnable based on TruthValue"""
    defaultValue = 2


_VRtrIgmpRsvpIfBfdEnable_Type.__name__ = "TruthValue"
_VRtrIgmpRsvpIfBfdEnable_Object = MibTableColumn
vRtrIgmpRsvpIfBfdEnable = _VRtrIgmpRsvpIfBfdEnable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 10, 1, 6),
    _VRtrIgmpRsvpIfBfdEnable_Type()
)
vRtrIgmpRsvpIfBfdEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIgmpRsvpIfBfdEnable.setStatus("current")


class _VRtrIgmpRsvpIfAdminState_Type(TmnxAdminState):
    """Custom type vRtrIgmpRsvpIfAdminState based on TmnxAdminState"""
    defaultValue = 2


_VRtrIgmpRsvpIfAdminState_Type.__name__ = "TmnxAdminState"
_VRtrIgmpRsvpIfAdminState_Object = MibTableColumn
vRtrIgmpRsvpIfAdminState = _VRtrIgmpRsvpIfAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 10, 1, 7),
    _VRtrIgmpRsvpIfAdminState_Type()
)
vRtrIgmpRsvpIfAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIgmpRsvpIfAdminState.setStatus("current")
_VRtrIgmpRsvpIfOperState_Type = TmnxOperState
_VRtrIgmpRsvpIfOperState_Object = MibTableColumn
vRtrIgmpRsvpIfOperState = _VRtrIgmpRsvpIfOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 10, 1, 8),
    _VRtrIgmpRsvpIfOperState_Type()
)
vRtrIgmpRsvpIfOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpRsvpIfOperState.setStatus("current")
_VRtrIgmpLdpIfTableLastChanged_Type = TimeStamp
_VRtrIgmpLdpIfTableLastChanged_Object = MibScalar
vRtrIgmpLdpIfTableLastChanged = _VRtrIgmpLdpIfTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 11),
    _VRtrIgmpLdpIfTableLastChanged_Type()
)
vRtrIgmpLdpIfTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpLdpIfTableLastChanged.setStatus("current")
_VRtrIgmpLdpIfTable_Object = MibTable
vRtrIgmpLdpIfTable = _VRtrIgmpLdpIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 12)
)
if mibBuilder.loadTexts:
    vRtrIgmpLdpIfTable.setStatus("current")
_VRtrIgmpLdpIfEntry_Object = MibTableRow
vRtrIgmpLdpIfEntry = _VRtrIgmpLdpIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 12, 1)
)
vRtrIgmpLdpIfEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-IGMP-MIB", "vRtrIgmpLdpP2mpId"),
    (0, "TIMETRA-IGMP-MIB", "vRtrIgmpLdpIfSenderAddrType"),
    (0, "TIMETRA-IGMP-MIB", "vRtrIgmpLdpIfSenderAddr"),
)
if mibBuilder.loadTexts:
    vRtrIgmpLdpIfEntry.setStatus("current")
_VRtrIgmpLdpP2mpId_Type = Unsigned32
_VRtrIgmpLdpP2mpId_Object = MibTableColumn
vRtrIgmpLdpP2mpId = _VRtrIgmpLdpP2mpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 12, 1, 1),
    _VRtrIgmpLdpP2mpId_Type()
)
vRtrIgmpLdpP2mpId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrIgmpLdpP2mpId.setStatus("current")
_VRtrIgmpLdpIfSenderAddrType_Type = InetAddressType
_VRtrIgmpLdpIfSenderAddrType_Object = MibTableColumn
vRtrIgmpLdpIfSenderAddrType = _VRtrIgmpLdpIfSenderAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 12, 1, 2),
    _VRtrIgmpLdpIfSenderAddrType_Type()
)
vRtrIgmpLdpIfSenderAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrIgmpLdpIfSenderAddrType.setStatus("current")


class _VRtrIgmpLdpIfSenderAddr_Type(InetAddress):
    """Custom type vRtrIgmpLdpIfSenderAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_VRtrIgmpLdpIfSenderAddr_Type.__name__ = "InetAddress"
_VRtrIgmpLdpIfSenderAddr_Object = MibTableColumn
vRtrIgmpLdpIfSenderAddr = _VRtrIgmpLdpIfSenderAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 12, 1, 3),
    _VRtrIgmpLdpIfSenderAddr_Type()
)
vRtrIgmpLdpIfSenderAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrIgmpLdpIfSenderAddr.setStatus("current")
_VRtrIgmpLdpIfRowStatus_Type = RowStatus
_VRtrIgmpLdpIfRowStatus_Object = MibTableColumn
vRtrIgmpLdpIfRowStatus = _VRtrIgmpLdpIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 12, 1, 4),
    _VRtrIgmpLdpIfRowStatus_Type()
)
vRtrIgmpLdpIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIgmpLdpIfRowStatus.setStatus("current")
_VRtrIgmpLdpIfLastChanged_Type = TimeStamp
_VRtrIgmpLdpIfLastChanged_Object = MibTableColumn
vRtrIgmpLdpIfLastChanged = _VRtrIgmpLdpIfLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 12, 1, 5),
    _VRtrIgmpLdpIfLastChanged_Type()
)
vRtrIgmpLdpIfLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpLdpIfLastChanged.setStatus("current")
_VRtrIgmpLdpIfIndex_Type = InterfaceIndex
_VRtrIgmpLdpIfIndex_Object = MibTableColumn
vRtrIgmpLdpIfIndex = _VRtrIgmpLdpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 12, 1, 6),
    _VRtrIgmpLdpIfIndex_Type()
)
vRtrIgmpLdpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpLdpIfIndex.setStatus("current")


class _VRtrIgmpLdpIfAdminState_Type(TmnxAdminState):
    """Custom type vRtrIgmpLdpIfAdminState based on TmnxAdminState"""
    defaultValue = 2


_VRtrIgmpLdpIfAdminState_Type.__name__ = "TmnxAdminState"
_VRtrIgmpLdpIfAdminState_Object = MibTableColumn
vRtrIgmpLdpIfAdminState = _VRtrIgmpLdpIfAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 12, 1, 7),
    _VRtrIgmpLdpIfAdminState_Type()
)
vRtrIgmpLdpIfAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIgmpLdpIfAdminState.setStatus("current")
_VRtrIgmpLdpIfOperState_Type = TmnxOperState
_VRtrIgmpLdpIfOperState_Object = MibTableColumn
vRtrIgmpLdpIfOperState = _VRtrIgmpLdpIfOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 2, 12, 1, 8),
    _VRtrIgmpLdpIfOperState_Type()
)
vRtrIgmpLdpIfOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpLdpIfOperState.setStatus("current")
_VRtrIgmpNotificationObjs_ObjectIdentity = ObjectIdentity
vRtrIgmpNotificationObjs = _VRtrIgmpNotificationObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 3)
)
_VRtrIgmpNotifyQueryVersion_Type = Unsigned32
_VRtrIgmpNotifyQueryVersion_Object = MibScalar
vRtrIgmpNotifyQueryVersion = _VRtrIgmpNotifyQueryVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 3, 1),
    _VRtrIgmpNotifyQueryVersion_Type()
)
vRtrIgmpNotifyQueryVersion.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrIgmpNotifyQueryVersion.setStatus("current")
_VRtrIgmpNotifyGrpAddrType_Type = InetAddressType
_VRtrIgmpNotifyGrpAddrType_Object = MibScalar
vRtrIgmpNotifyGrpAddrType = _VRtrIgmpNotifyGrpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 3, 2),
    _VRtrIgmpNotifyGrpAddrType_Type()
)
vRtrIgmpNotifyGrpAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrIgmpNotifyGrpAddrType.setStatus("current")
_VRtrIgmpNotifyGrpAddr_Type = InetAddress
_VRtrIgmpNotifyGrpAddr_Object = MibScalar
vRtrIgmpNotifyGrpAddr = _VRtrIgmpNotifyGrpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 3, 3),
    _VRtrIgmpNotifyGrpAddr_Type()
)
vRtrIgmpNotifyGrpAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrIgmpNotifyGrpAddr.setStatus("current")
_VRtrIgmpNotifyDescription_Type = DisplayString
_VRtrIgmpNotifyDescription_Object = MibScalar
vRtrIgmpNotifyDescription = _VRtrIgmpNotifyDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 3, 4),
    _VRtrIgmpNotifyDescription_Type()
)
vRtrIgmpNotifyDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrIgmpNotifyDescription.setStatus("current")
_VRtrIgmpNotifyMcacPolicyName_Type = TPolicyStatementNameOrEmpty
_VRtrIgmpNotifyMcacPolicyName_Object = MibScalar
vRtrIgmpNotifyMcacPolicyName = _VRtrIgmpNotifyMcacPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 3, 5),
    _VRtrIgmpNotifyMcacPolicyName_Type()
)
vRtrIgmpNotifyMcacPolicyName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrIgmpNotifyMcacPolicyName.setStatus("current")
_VRtrIgmpNotifySrcAddrType_Type = InetAddressType
_VRtrIgmpNotifySrcAddrType_Object = MibScalar
vRtrIgmpNotifySrcAddrType = _VRtrIgmpNotifySrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 3, 6),
    _VRtrIgmpNotifySrcAddrType_Type()
)
vRtrIgmpNotifySrcAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrIgmpNotifySrcAddrType.setStatus("current")
_VRtrIgmpNotifySrcAddr_Type = InetAddress
_VRtrIgmpNotifySrcAddr_Object = MibScalar
vRtrIgmpNotifySrcAddr = _VRtrIgmpNotifySrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 3, 7),
    _VRtrIgmpNotifySrcAddr_Type()
)
vRtrIgmpNotifySrcAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrIgmpNotifySrcAddr.setStatus("current")
_VRtrIgmpHostObjs_ObjectIdentity = ObjectIdentity
vRtrIgmpHostObjs = _VRtrIgmpHostObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4)
)
_VRtrIgmpHostTable_Object = MibTable
vRtrIgmpHostTable = _VRtrIgmpHostTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 1)
)
if mibBuilder.loadTexts:
    vRtrIgmpHostTable.setStatus("current")
_VRtrIgmpHostEntry_Object = MibTableRow
vRtrIgmpHostEntry = _VRtrIgmpHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 1, 1)
)
vRtrIgmpHostEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-IGMP-MIB", "vRtrIgmpHostAddress"),
)
if mibBuilder.loadTexts:
    vRtrIgmpHostEntry.setStatus("current")
_VRtrIgmpHostAddress_Type = IpAddress
_VRtrIgmpHostAddress_Object = MibTableColumn
vRtrIgmpHostAddress = _VRtrIgmpHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 1, 1, 1),
    _VRtrIgmpHostAddress_Type()
)
vRtrIgmpHostAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrIgmpHostAddress.setStatus("current")
_VRtrIgmpHostLastChangeTime_Type = TimeStamp
_VRtrIgmpHostLastChangeTime_Object = MibTableColumn
vRtrIgmpHostLastChangeTime = _VRtrIgmpHostLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 1, 1, 2),
    _VRtrIgmpHostLastChangeTime_Type()
)
vRtrIgmpHostLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpHostLastChangeTime.setStatus("current")
_VRtrIgmpHostOperState_Type = IgmpGrpItfOperState
_VRtrIgmpHostOperState_Object = MibTableColumn
vRtrIgmpHostOperState = _VRtrIgmpHostOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 1, 1, 3),
    _VRtrIgmpHostOperState_Type()
)
vRtrIgmpHostOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpHostOperState.setStatus("current")
_VRtrIgmpHostOperVersion_Type = Unsigned32
_VRtrIgmpHostOperVersion_Object = MibTableColumn
vRtrIgmpHostOperVersion = _VRtrIgmpHostOperVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 1, 1, 4),
    _VRtrIgmpHostOperVersion_Type()
)
vRtrIgmpHostOperVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpHostOperVersion.setStatus("current")
_VRtrIgmpHostGroupCount_Type = Unsigned32
_VRtrIgmpHostGroupCount_Object = MibTableColumn
vRtrIgmpHostGroupCount = _VRtrIgmpHostGroupCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 1, 1, 5),
    _VRtrIgmpHostGroupCount_Type()
)
vRtrIgmpHostGroupCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpHostGroupCount.setStatus("current")
_VRtrIgmpHostNextGenQueryTime_Type = Unsigned32
_VRtrIgmpHostNextGenQueryTime_Object = MibTableColumn
vRtrIgmpHostNextGenQueryTime = _VRtrIgmpHostNextGenQueryTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 1, 1, 6),
    _VRtrIgmpHostNextGenQueryTime_Type()
)
vRtrIgmpHostNextGenQueryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpHostNextGenQueryTime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrIgmpHostNextGenQueryTime.setUnits("seconds")
_VRtrIgmpHostMaxGroupsTillNow_Type = Counter32
_VRtrIgmpHostMaxGroupsTillNow_Object = MibTableColumn
vRtrIgmpHostMaxGroupsTillNow = _VRtrIgmpHostMaxGroupsTillNow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 1, 1, 7),
    _VRtrIgmpHostMaxGroupsTillNow_Type()
)
vRtrIgmpHostMaxGroupsTillNow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpHostMaxGroupsTillNow.setStatus("current")


class _VRtrIgmpHostFwdSvcId_Type(TmnxServId):
    """Custom type vRtrIgmpHostFwdSvcId based on TmnxServId"""
    defaultValue = 0


_VRtrIgmpHostFwdSvcId_Type.__name__ = "TmnxServId"
_VRtrIgmpHostFwdSvcId_Object = MibTableColumn
vRtrIgmpHostFwdSvcId = _VRtrIgmpHostFwdSvcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 1, 1, 8),
    _VRtrIgmpHostFwdSvcId_Type()
)
vRtrIgmpHostFwdSvcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpHostFwdSvcId.setStatus("current")
_VRtrIgmpHostGrpIfId_Type = InterfaceIndex
_VRtrIgmpHostGrpIfId_Object = MibTableColumn
vRtrIgmpHostGrpIfId = _VRtrIgmpHostGrpIfId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 1, 1, 9),
    _VRtrIgmpHostGrpIfId_Type()
)
vRtrIgmpHostGrpIfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpHostGrpIfId.setStatus("current")
_VRtrIgmpHostPppoeSessionId_Type = TmnxPppoeSessionId
_VRtrIgmpHostPppoeSessionId_Object = MibTableColumn
vRtrIgmpHostPppoeSessionId = _VRtrIgmpHostPppoeSessionId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 1, 1, 10),
    _VRtrIgmpHostPppoeSessionId_Type()
)
vRtrIgmpHostPppoeSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpHostPppoeSessionId.setStatus("current")
_VRtrIgmpHostSubscriberId_Type = TmnxSubIdentStringOrEmpty
_VRtrIgmpHostSubscriberId_Object = MibTableColumn
vRtrIgmpHostSubscriberId = _VRtrIgmpHostSubscriberId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 1, 1, 11),
    _VRtrIgmpHostSubscriberId_Type()
)
vRtrIgmpHostSubscriberId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpHostSubscriberId.setStatus("current")
_VRtrIgmpHostMacAddress_Type = MacAddress
_VRtrIgmpHostMacAddress_Object = MibTableColumn
vRtrIgmpHostMacAddress = _VRtrIgmpHostMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 1, 1, 12),
    _VRtrIgmpHostMacAddress_Type()
)
vRtrIgmpHostMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpHostMacAddress.setStatus("current")


class _VRtrIgmpHostIgmpPolicy_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrIgmpHostIgmpPolicy based on TPolicyStatementNameOrEmpty"""
    defaultValue = OctetString("")


_VRtrIgmpHostIgmpPolicy_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrIgmpHostIgmpPolicy_Object = MibTableColumn
vRtrIgmpHostIgmpPolicy = _VRtrIgmpHostIgmpPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 1, 1, 13),
    _VRtrIgmpHostIgmpPolicy_Type()
)
vRtrIgmpHostIgmpPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpHostIgmpPolicy.setStatus("current")


class _VRtrIgmpHostMaxGroups_Type(Unsigned32):
    """Custom type vRtrIgmpHostMaxGroups based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 16000),
    )


_VRtrIgmpHostMaxGroups_Type.__name__ = "Unsigned32"
_VRtrIgmpHostMaxGroups_Object = MibTableColumn
vRtrIgmpHostMaxGroups = _VRtrIgmpHostMaxGroups_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 1, 1, 14),
    _VRtrIgmpHostMaxGroups_Type()
)
vRtrIgmpHostMaxGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpHostMaxGroups.setStatus("current")


class _VRtrIgmpHostAdminVersion_Type(Unsigned32):
    """Custom type vRtrIgmpHostAdminVersion based on Unsigned32"""
    defaultValue = 3


_VRtrIgmpHostAdminVersion_Type.__name__ = "Unsigned32"
_VRtrIgmpHostAdminVersion_Object = MibTableColumn
vRtrIgmpHostAdminVersion = _VRtrIgmpHostAdminVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 1, 1, 15),
    _VRtrIgmpHostAdminVersion_Type()
)
vRtrIgmpHostAdminVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpHostAdminVersion.setStatus("current")


class _VRtrIgmpHostMaxSources_Type(Unsigned32):
    """Custom type vRtrIgmpHostMaxSources based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1000),
    )


_VRtrIgmpHostMaxSources_Type.__name__ = "Unsigned32"
_VRtrIgmpHostMaxSources_Object = MibTableColumn
vRtrIgmpHostMaxSources = _VRtrIgmpHostMaxSources_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 1, 1, 16),
    _VRtrIgmpHostMaxSources_Type()
)
vRtrIgmpHostMaxSources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpHostMaxSources.setStatus("current")


class _VRtrIgmpHostMaxGrpSources_Type(Unsigned32):
    """Custom type vRtrIgmpHostMaxGrpSources based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1000),
    )


_VRtrIgmpHostMaxGrpSources_Type.__name__ = "Unsigned32"
_VRtrIgmpHostMaxGrpSources_Object = MibTableColumn
vRtrIgmpHostMaxGrpSources = _VRtrIgmpHostMaxGrpSources_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 1, 1, 17),
    _VRtrIgmpHostMaxGrpSources_Type()
)
vRtrIgmpHostMaxGrpSources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpHostMaxGrpSources.setStatus("current")
_VRtrIgmpHostStatsTable_Object = MibTable
vRtrIgmpHostStatsTable = _VRtrIgmpHostStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 2)
)
if mibBuilder.loadTexts:
    vRtrIgmpHostStatsTable.setStatus("current")
_VRtrIgmpHostStatsEntry_Object = MibTableRow
vRtrIgmpHostStatsEntry = _VRtrIgmpHostStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 2, 1)
)
if mibBuilder.loadTexts:
    vRtrIgmpHostStatsEntry.setStatus("current")
_VRtrIgmpHostTxGenQueries_Type = Counter32
_VRtrIgmpHostTxGenQueries_Object = MibTableColumn
vRtrIgmpHostTxGenQueries = _VRtrIgmpHostTxGenQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 2, 1, 1),
    _VRtrIgmpHostTxGenQueries_Type()
)
vRtrIgmpHostTxGenQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpHostTxGenQueries.setStatus("current")
_VRtrIgmpHostTxGrpQueries_Type = Counter32
_VRtrIgmpHostTxGrpQueries_Object = MibTableColumn
vRtrIgmpHostTxGrpQueries = _VRtrIgmpHostTxGrpQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 2, 1, 2),
    _VRtrIgmpHostTxGrpQueries_Type()
)
vRtrIgmpHostTxGrpQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpHostTxGrpQueries.setStatus("current")
_VRtrIgmpHostTxGrpSrcQueries_Type = Counter32
_VRtrIgmpHostTxGrpSrcQueries_Object = MibTableColumn
vRtrIgmpHostTxGrpSrcQueries = _VRtrIgmpHostTxGrpSrcQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 2, 1, 3),
    _VRtrIgmpHostTxGrpSrcQueries_Type()
)
vRtrIgmpHostTxGrpSrcQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpHostTxGrpSrcQueries.setStatus("current")
_VRtrIgmpHostTxV1Reports_Type = Counter32
_VRtrIgmpHostTxV1Reports_Object = MibTableColumn
vRtrIgmpHostTxV1Reports = _VRtrIgmpHostTxV1Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 2, 1, 4),
    _VRtrIgmpHostTxV1Reports_Type()
)
vRtrIgmpHostTxV1Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpHostTxV1Reports.setStatus("current")
_VRtrIgmpHostTxV2Reports_Type = Counter32
_VRtrIgmpHostTxV2Reports_Object = MibTableColumn
vRtrIgmpHostTxV2Reports = _VRtrIgmpHostTxV2Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 2, 1, 5),
    _VRtrIgmpHostTxV2Reports_Type()
)
vRtrIgmpHostTxV2Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpHostTxV2Reports.setStatus("current")
_VRtrIgmpHostTxV3Reports_Type = Counter32
_VRtrIgmpHostTxV3Reports_Object = MibTableColumn
vRtrIgmpHostTxV3Reports = _VRtrIgmpHostTxV3Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 2, 1, 6),
    _VRtrIgmpHostTxV3Reports_Type()
)
vRtrIgmpHostTxV3Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpHostTxV3Reports.setStatus("current")
_VRtrIgmpHostTxLeaves_Type = Counter32
_VRtrIgmpHostTxLeaves_Object = MibTableColumn
vRtrIgmpHostTxLeaves = _VRtrIgmpHostTxLeaves_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 2, 1, 7),
    _VRtrIgmpHostTxLeaves_Type()
)
vRtrIgmpHostTxLeaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpHostTxLeaves.setStatus("current")
_VRtrIgmpHostTxErrors_Type = Counter32
_VRtrIgmpHostTxErrors_Object = MibTableColumn
vRtrIgmpHostTxErrors = _VRtrIgmpHostTxErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 2, 1, 8),
    _VRtrIgmpHostTxErrors_Type()
)
vRtrIgmpHostTxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpHostTxErrors.setStatus("current")
_VRtrIgmpHostRxGenQueries_Type = Counter32
_VRtrIgmpHostRxGenQueries_Object = MibTableColumn
vRtrIgmpHostRxGenQueries = _VRtrIgmpHostRxGenQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 2, 1, 9),
    _VRtrIgmpHostRxGenQueries_Type()
)
vRtrIgmpHostRxGenQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpHostRxGenQueries.setStatus("current")
_VRtrIgmpHostRxGrpQueries_Type = Counter32
_VRtrIgmpHostRxGrpQueries_Object = MibTableColumn
vRtrIgmpHostRxGrpQueries = _VRtrIgmpHostRxGrpQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 2, 1, 10),
    _VRtrIgmpHostRxGrpQueries_Type()
)
vRtrIgmpHostRxGrpQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpHostRxGrpQueries.setStatus("current")
_VRtrIgmpHostRxGrpSrcQueries_Type = Counter32
_VRtrIgmpHostRxGrpSrcQueries_Object = MibTableColumn
vRtrIgmpHostRxGrpSrcQueries = _VRtrIgmpHostRxGrpSrcQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 2, 1, 11),
    _VRtrIgmpHostRxGrpSrcQueries_Type()
)
vRtrIgmpHostRxGrpSrcQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpHostRxGrpSrcQueries.setStatus("current")
_VRtrIgmpHostRxV1Reports_Type = Counter32
_VRtrIgmpHostRxV1Reports_Object = MibTableColumn
vRtrIgmpHostRxV1Reports = _VRtrIgmpHostRxV1Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 2, 1, 12),
    _VRtrIgmpHostRxV1Reports_Type()
)
vRtrIgmpHostRxV1Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpHostRxV1Reports.setStatus("current")
_VRtrIgmpHostRxV2Reports_Type = Counter32
_VRtrIgmpHostRxV2Reports_Object = MibTableColumn
vRtrIgmpHostRxV2Reports = _VRtrIgmpHostRxV2Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 2, 1, 13),
    _VRtrIgmpHostRxV2Reports_Type()
)
vRtrIgmpHostRxV2Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpHostRxV2Reports.setStatus("current")
_VRtrIgmpHostRxV3Reports_Type = Counter32
_VRtrIgmpHostRxV3Reports_Object = MibTableColumn
vRtrIgmpHostRxV3Reports = _VRtrIgmpHostRxV3Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 2, 1, 14),
    _VRtrIgmpHostRxV3Reports_Type()
)
vRtrIgmpHostRxV3Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpHostRxV3Reports.setStatus("current")
_VRtrIgmpHostRxLeaves_Type = Counter32
_VRtrIgmpHostRxLeaves_Object = MibTableColumn
vRtrIgmpHostRxLeaves = _VRtrIgmpHostRxLeaves_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 2, 1, 15),
    _VRtrIgmpHostRxLeaves_Type()
)
vRtrIgmpHostRxLeaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpHostRxLeaves.setStatus("current")
_VRtrIgmpHostRxBadLenPkts_Type = Counter32
_VRtrIgmpHostRxBadLenPkts_Object = MibTableColumn
vRtrIgmpHostRxBadLenPkts = _VRtrIgmpHostRxBadLenPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 2, 1, 16),
    _VRtrIgmpHostRxBadLenPkts_Type()
)
vRtrIgmpHostRxBadLenPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpHostRxBadLenPkts.setStatus("current")
_VRtrIgmpHostRxBadChecksumPkts_Type = Counter32
_VRtrIgmpHostRxBadChecksumPkts_Object = MibTableColumn
vRtrIgmpHostRxBadChecksumPkts = _VRtrIgmpHostRxBadChecksumPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 2, 1, 17),
    _VRtrIgmpHostRxBadChecksumPkts_Type()
)
vRtrIgmpHostRxBadChecksumPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpHostRxBadChecksumPkts.setStatus("current")
_VRtrIgmpHostRxUnknownTypePkts_Type = Counter32
_VRtrIgmpHostRxUnknownTypePkts_Object = MibTableColumn
vRtrIgmpHostRxUnknownTypePkts = _VRtrIgmpHostRxUnknownTypePkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 2, 1, 18),
    _VRtrIgmpHostRxUnknownTypePkts_Type()
)
vRtrIgmpHostRxUnknownTypePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpHostRxUnknownTypePkts.setStatus("current")
_VRtrIgmpHostRxBadReceiveIfPkts_Type = Counter32
_VRtrIgmpHostRxBadReceiveIfPkts_Object = MibTableColumn
vRtrIgmpHostRxBadReceiveIfPkts = _VRtrIgmpHostRxBadReceiveIfPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 2, 1, 19),
    _VRtrIgmpHostRxBadReceiveIfPkts_Type()
)
vRtrIgmpHostRxBadReceiveIfPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpHostRxBadReceiveIfPkts.setStatus("current")
_VRtrIgmpHostRxNonLocal_Type = Counter32
_VRtrIgmpHostRxNonLocal_Object = MibTableColumn
vRtrIgmpHostRxNonLocal = _VRtrIgmpHostRxNonLocal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 2, 1, 20),
    _VRtrIgmpHostRxNonLocal_Type()
)
vRtrIgmpHostRxNonLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpHostRxNonLocal.setStatus("current")
_VRtrIgmpHostRxWrongVersions_Type = Counter32
_VRtrIgmpHostRxWrongVersions_Object = MibTableColumn
vRtrIgmpHostRxWrongVersions = _VRtrIgmpHostRxWrongVersions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 2, 1, 21),
    _VRtrIgmpHostRxWrongVersions_Type()
)
vRtrIgmpHostRxWrongVersions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpHostRxWrongVersions.setStatus("current")
_VRtrIgmpHostImportPolicyDrops_Type = Counter32
_VRtrIgmpHostImportPolicyDrops_Object = MibTableColumn
vRtrIgmpHostImportPolicyDrops = _VRtrIgmpHostImportPolicyDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 2, 1, 22),
    _VRtrIgmpHostImportPolicyDrops_Type()
)
vRtrIgmpHostImportPolicyDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpHostImportPolicyDrops.setStatus("current")
_VRtrIgmpHostRxNoRtrAlertPkts_Type = Counter32
_VRtrIgmpHostRxNoRtrAlertPkts_Object = MibTableColumn
vRtrIgmpHostRxNoRtrAlertPkts = _VRtrIgmpHostRxNoRtrAlertPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 2, 1, 23),
    _VRtrIgmpHostRxNoRtrAlertPkts_Type()
)
vRtrIgmpHostRxNoRtrAlertPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpHostRxNoRtrAlertPkts.setStatus("current")
_VRtrIgmpHostRxBadEncodings_Type = Counter32
_VRtrIgmpHostRxBadEncodings_Object = MibTableColumn
vRtrIgmpHostRxBadEncodings = _VRtrIgmpHostRxBadEncodings_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 2, 1, 24),
    _VRtrIgmpHostRxBadEncodings_Type()
)
vRtrIgmpHostRxBadEncodings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpHostRxBadEncodings.setStatus("current")
_VRtrIgmpHostRxPktDrops_Type = Counter32
_VRtrIgmpHostRxPktDrops_Object = MibTableColumn
vRtrIgmpHostRxPktDrops = _VRtrIgmpHostRxPktDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 2, 1, 25),
    _VRtrIgmpHostRxPktDrops_Type()
)
vRtrIgmpHostRxPktDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpHostRxPktDrops.setStatus("current")
_VRtrIgmpHostStatsStarGTypes_Type = Gauge32
_VRtrIgmpHostStatsStarGTypes_Object = MibTableColumn
vRtrIgmpHostStatsStarGTypes = _VRtrIgmpHostStatsStarGTypes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 2, 1, 26),
    _VRtrIgmpHostStatsStarGTypes_Type()
)
vRtrIgmpHostStatsStarGTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpHostStatsStarGTypes.setStatus("current")
_VRtrIgmpHostStatsSGTypes_Type = Gauge32
_VRtrIgmpHostStatsSGTypes_Object = MibTableColumn
vRtrIgmpHostStatsSGTypes = _VRtrIgmpHostStatsSGTypes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 2, 1, 27),
    _VRtrIgmpHostStatsSGTypes_Type()
)
vRtrIgmpHostStatsSGTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpHostStatsSGTypes.setStatus("current")
_VRtrIgmpHostStatsMcacPolicyDrops_Type = Counter32
_VRtrIgmpHostStatsMcacPolicyDrops_Object = MibTableColumn
vRtrIgmpHostStatsMcacPolicyDrops = _VRtrIgmpHostStatsMcacPolicyDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 2, 1, 28),
    _VRtrIgmpHostStatsMcacPolicyDrops_Type()
)
vRtrIgmpHostStatsMcacPolicyDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpHostStatsMcacPolicyDrops.setStatus("current")
_VRtrIgmpHostRxLocalScopePkts_Type = Counter32
_VRtrIgmpHostRxLocalScopePkts_Object = MibTableColumn
vRtrIgmpHostRxLocalScopePkts = _VRtrIgmpHostRxLocalScopePkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 2, 1, 29),
    _VRtrIgmpHostRxLocalScopePkts_Type()
)
vRtrIgmpHostRxLocalScopePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpHostRxLocalScopePkts.setStatus("current")
_VRtrIgmpHostRxRsvdScopePkts_Type = Counter32
_VRtrIgmpHostRxRsvdScopePkts_Object = MibTableColumn
vRtrIgmpHostRxRsvdScopePkts = _VRtrIgmpHostRxRsvdScopePkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 2, 1, 30),
    _VRtrIgmpHostRxRsvdScopePkts_Type()
)
vRtrIgmpHostRxRsvdScopePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpHostRxRsvdScopePkts.setStatus("current")
_VRtrIgmpHostRedirectionDrops_Type = Counter32
_VRtrIgmpHostRedirectionDrops_Object = MibTableColumn
vRtrIgmpHostRedirectionDrops = _VRtrIgmpHostRedirectionDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 2, 1, 31),
    _VRtrIgmpHostRedirectionDrops_Type()
)
vRtrIgmpHostRedirectionDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpHostRedirectionDrops.setStatus("current")
_VRtrIgmpGrpIfTable_Object = MibTable
vRtrIgmpGrpIfTable = _VRtrIgmpGrpIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 3)
)
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfTable.setStatus("current")
_VRtrIgmpGrpIfEntry_Object = MibTableRow
vRtrIgmpGrpIfEntry = _VRtrIgmpGrpIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 3, 1)
)
vRtrIgmpGrpIfEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-IGMP-MIB", "vRtrIfFwdSvcId"),
    (0, "TIMETRA-VRTR-MIB", "vRtrIfIndex"),
)
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfEntry.setStatus("current")


class _VRtrIfFwdSvcId_Type(TmnxServId):
    """Custom type vRtrIfFwdSvcId based on TmnxServId"""
    defaultValue = 0


_VRtrIfFwdSvcId_Type.__name__ = "TmnxServId"
_VRtrIfFwdSvcId_Object = MibTableColumn
vRtrIfFwdSvcId = _VRtrIfFwdSvcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 3, 1, 1),
    _VRtrIfFwdSvcId_Type()
)
vRtrIfFwdSvcId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrIfFwdSvcId.setStatus("current")
_VRtrIgmpGrpIfRowStatus_Type = RowStatus
_VRtrIgmpGrpIfRowStatus_Object = MibTableColumn
vRtrIgmpGrpIfRowStatus = _VRtrIgmpGrpIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 3, 1, 2),
    _VRtrIgmpGrpIfRowStatus_Type()
)
vRtrIgmpGrpIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfRowStatus.setStatus("current")
_VRtrIgmpGrpIfLastChangeTime_Type = TimeStamp
_VRtrIgmpGrpIfLastChangeTime_Object = MibTableColumn
vRtrIgmpGrpIfLastChangeTime = _VRtrIgmpGrpIfLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 3, 1, 3),
    _VRtrIgmpGrpIfLastChangeTime_Type()
)
vRtrIgmpGrpIfLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfLastChangeTime.setStatus("current")


class _VRtrIgmpGrpIfAdminState_Type(TmnxAdminState):
    """Custom type vRtrIgmpGrpIfAdminState based on TmnxAdminState"""
    defaultValue = 2


_VRtrIgmpGrpIfAdminState_Type.__name__ = "TmnxAdminState"
_VRtrIgmpGrpIfAdminState_Object = MibTableColumn
vRtrIgmpGrpIfAdminState = _VRtrIgmpGrpIfAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 3, 1, 4),
    _VRtrIgmpGrpIfAdminState_Type()
)
vRtrIgmpGrpIfAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfAdminState.setStatus("current")
_VRtrIgmpGrpIfOperState_Type = TmnxOperState
_VRtrIgmpGrpIfOperState_Object = MibTableColumn
vRtrIgmpGrpIfOperState = _VRtrIgmpGrpIfOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 3, 1, 5),
    _VRtrIgmpGrpIfOperState_Type()
)
vRtrIgmpGrpIfOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfOperState.setStatus("current")


class _VRtrIgmpGrpIfSubHostsOnly_Type(TruthValue):
    """Custom type vRtrIgmpGrpIfSubHostsOnly based on TruthValue"""
    defaultValue = 1


_VRtrIgmpGrpIfSubHostsOnly_Type.__name__ = "TruthValue"
_VRtrIgmpGrpIfSubHostsOnly_Object = MibTableColumn
vRtrIgmpGrpIfSubHostsOnly = _VRtrIgmpGrpIfSubHostsOnly_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 3, 1, 6),
    _VRtrIgmpGrpIfSubHostsOnly_Type()
)
vRtrIgmpGrpIfSubHostsOnly.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfSubHostsOnly.setStatus("current")


class _VRtrIgmpGrpIfAdminVersion_Type(Unsigned32):
    """Custom type vRtrIgmpGrpIfAdminVersion based on Unsigned32"""
    defaultValue = 3


_VRtrIgmpGrpIfAdminVersion_Type.__name__ = "Unsigned32"
_VRtrIgmpGrpIfAdminVersion_Object = MibTableColumn
vRtrIgmpGrpIfAdminVersion = _VRtrIgmpGrpIfAdminVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 3, 1, 7),
    _VRtrIgmpGrpIfAdminVersion_Type()
)
vRtrIgmpGrpIfAdminVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfAdminVersion.setStatus("current")


class _VRtrIgmpGrpIfImportPolicy_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrIgmpGrpIfImportPolicy based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrIgmpGrpIfImportPolicy_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrIgmpGrpIfImportPolicy_Object = MibTableColumn
vRtrIgmpGrpIfImportPolicy = _VRtrIgmpGrpIfImportPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 3, 1, 8),
    _VRtrIgmpGrpIfImportPolicy_Type()
)
vRtrIgmpGrpIfImportPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfImportPolicy.setStatus("current")


class _VRtrIgmpGrpIfSubnetCheck_Type(TruthValue):
    """Custom type vRtrIgmpGrpIfSubnetCheck based on TruthValue"""
    defaultValue = 1


_VRtrIgmpGrpIfSubnetCheck_Type.__name__ = "TruthValue"
_VRtrIgmpGrpIfSubnetCheck_Object = MibTableColumn
vRtrIgmpGrpIfSubnetCheck = _VRtrIgmpGrpIfSubnetCheck_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 3, 1, 9),
    _VRtrIgmpGrpIfSubnetCheck_Type()
)
vRtrIgmpGrpIfSubnetCheck.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfSubnetCheck.setStatus("current")


class _VRtrIgmpGrpIfMcacPolicyName_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrIgmpGrpIfMcacPolicyName based on TPolicyStatementNameOrEmpty"""
    defaultValue = OctetString("")


_VRtrIgmpGrpIfMcacPolicyName_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrIgmpGrpIfMcacPolicyName_Object = MibTableColumn
vRtrIgmpGrpIfMcacPolicyName = _VRtrIgmpGrpIfMcacPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 3, 1, 10),
    _VRtrIgmpGrpIfMcacPolicyName_Type()
)
vRtrIgmpGrpIfMcacPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfMcacPolicyName.setStatus("current")


class _VRtrIgmpGrpIfMcacUnconstrainedBW_Type(Integer32):
    """Custom type vRtrIgmpGrpIfMcacUnconstrainedBW based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_VRtrIgmpGrpIfMcacUnconstrainedBW_Type.__name__ = "Integer32"
_VRtrIgmpGrpIfMcacUnconstrainedBW_Object = MibTableColumn
vRtrIgmpGrpIfMcacUnconstrainedBW = _VRtrIgmpGrpIfMcacUnconstrainedBW_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 3, 1, 11),
    _VRtrIgmpGrpIfMcacUnconstrainedBW_Type()
)
vRtrIgmpGrpIfMcacUnconstrainedBW.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfMcacUnconstrainedBW.setStatus("current")
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfMcacUnconstrainedBW.setUnits("kbps")


class _VRtrIgmpGrpIfMcacConstAdminState_Type(TmnxAdminState):
    """Custom type vRtrIgmpGrpIfMcacConstAdminState based on TmnxAdminState"""
    defaultValue = 2


_VRtrIgmpGrpIfMcacConstAdminState_Type.__name__ = "TmnxAdminState"
_VRtrIgmpGrpIfMcacConstAdminState_Object = MibTableColumn
vRtrIgmpGrpIfMcacConstAdminState = _VRtrIgmpGrpIfMcacConstAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 3, 1, 12),
    _VRtrIgmpGrpIfMcacConstAdminState_Type()
)
vRtrIgmpGrpIfMcacConstAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfMcacConstAdminState.setStatus("current")


class _VRtrIgmpGrpIfMcacPreRsvdMandBW_Type(Integer32):
    """Custom type vRtrIgmpGrpIfMcacPreRsvdMandBW based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_VRtrIgmpGrpIfMcacPreRsvdMandBW_Type.__name__ = "Integer32"
_VRtrIgmpGrpIfMcacPreRsvdMandBW_Object = MibTableColumn
vRtrIgmpGrpIfMcacPreRsvdMandBW = _VRtrIgmpGrpIfMcacPreRsvdMandBW_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 3, 1, 13),
    _VRtrIgmpGrpIfMcacPreRsvdMandBW_Type()
)
vRtrIgmpGrpIfMcacPreRsvdMandBW.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfMcacPreRsvdMandBW.setStatus("current")
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfMcacPreRsvdMandBW.setUnits("kbps")
_VRtrIgmpGrpIfMcacinUseMandBw_Type = Unsigned32
_VRtrIgmpGrpIfMcacinUseMandBw_Object = MibTableColumn
vRtrIgmpGrpIfMcacinUseMandBw = _VRtrIgmpGrpIfMcacinUseMandBw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 3, 1, 14),
    _VRtrIgmpGrpIfMcacinUseMandBw_Type()
)
vRtrIgmpGrpIfMcacinUseMandBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfMcacinUseMandBw.setStatus("current")
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfMcacinUseMandBw.setUnits("kbps")
_VRtrIgmpGrpIfMcacinUseOpnlBw_Type = Unsigned32
_VRtrIgmpGrpIfMcacinUseOpnlBw_Object = MibTableColumn
vRtrIgmpGrpIfMcacinUseOpnlBw = _VRtrIgmpGrpIfMcacinUseOpnlBw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 3, 1, 15),
    _VRtrIgmpGrpIfMcacinUseOpnlBw_Type()
)
vRtrIgmpGrpIfMcacinUseOpnlBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfMcacinUseOpnlBw.setStatus("current")
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfMcacinUseOpnlBw.setUnits("kbps")
_VRtrIgmpGrpIfMcacAvailMandBw_Type = Unsigned32
_VRtrIgmpGrpIfMcacAvailMandBw_Object = MibTableColumn
vRtrIgmpGrpIfMcacAvailMandBw = _VRtrIgmpGrpIfMcacAvailMandBw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 3, 1, 16),
    _VRtrIgmpGrpIfMcacAvailMandBw_Type()
)
vRtrIgmpGrpIfMcacAvailMandBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfMcacAvailMandBw.setStatus("current")
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfMcacAvailMandBw.setUnits("kbps")
_VRtrIgmpGrpIfMcacAvailOpnlBw_Type = Unsigned32
_VRtrIgmpGrpIfMcacAvailOpnlBw_Object = MibTableColumn
vRtrIgmpGrpIfMcacAvailOpnlBw = _VRtrIgmpGrpIfMcacAvailOpnlBw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 3, 1, 17),
    _VRtrIgmpGrpIfMcacAvailOpnlBw_Type()
)
vRtrIgmpGrpIfMcacAvailOpnlBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfMcacAvailOpnlBw.setStatus("current")
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfMcacAvailOpnlBw.setUnits("kbps")
_VRtrIgmpGrpIfMcacValuesInTransit_Type = TruthValue
_VRtrIgmpGrpIfMcacValuesInTransit_Object = MibTableColumn
vRtrIgmpGrpIfMcacValuesInTransit = _VRtrIgmpGrpIfMcacValuesInTransit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 3, 1, 18),
    _VRtrIgmpGrpIfMcacValuesInTransit_Type()
)
vRtrIgmpGrpIfMcacValuesInTransit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfMcacValuesInTransit.setStatus("current")


class _VRtrIgmpGrpIfDisRtrAlertChk_Type(TruthValue):
    """Custom type vRtrIgmpGrpIfDisRtrAlertChk based on TruthValue"""
    defaultValue = 2


_VRtrIgmpGrpIfDisRtrAlertChk_Type.__name__ = "TruthValue"
_VRtrIgmpGrpIfDisRtrAlertChk_Object = MibTableColumn
vRtrIgmpGrpIfDisRtrAlertChk = _VRtrIgmpGrpIfDisRtrAlertChk_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 3, 1, 19),
    _VRtrIgmpGrpIfDisRtrAlertChk_Type()
)
vRtrIgmpGrpIfDisRtrAlertChk.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfDisRtrAlertChk.setStatus("current")


class _VRtrIgmpGrpIfMaxGroups_Type(Unsigned32):
    """Custom type vRtrIgmpGrpIfMaxGroups based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 16000),
    )


_VRtrIgmpGrpIfMaxGroups_Type.__name__ = "Unsigned32"
_VRtrIgmpGrpIfMaxGroups_Object = MibTableColumn
vRtrIgmpGrpIfMaxGroups = _VRtrIgmpGrpIfMaxGroups_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 3, 1, 20),
    _VRtrIgmpGrpIfMaxGroups_Type()
)
vRtrIgmpGrpIfMaxGroups.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfMaxGroups.setStatus("current")


class _VRtrIgmpGrpIfMaxSources_Type(Unsigned32):
    """Custom type vRtrIgmpGrpIfMaxSources based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1000),
    )


_VRtrIgmpGrpIfMaxSources_Type.__name__ = "Unsigned32"
_VRtrIgmpGrpIfMaxSources_Object = MibTableColumn
vRtrIgmpGrpIfMaxSources = _VRtrIgmpGrpIfMaxSources_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 3, 1, 21),
    _VRtrIgmpGrpIfMaxSources_Type()
)
vRtrIgmpGrpIfMaxSources.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfMaxSources.setStatus("current")


class _VRtrIgmpGrpIfMaxGrpSources_Type(Unsigned32):
    """Custom type vRtrIgmpGrpIfMaxGrpSources based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 32000),
    )


_VRtrIgmpGrpIfMaxGrpSources_Type.__name__ = "Unsigned32"
_VRtrIgmpGrpIfMaxGrpSources_Object = MibTableColumn
vRtrIgmpGrpIfMaxGrpSources = _VRtrIgmpGrpIfMaxGrpSources_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 3, 1, 22),
    _VRtrIgmpGrpIfMaxGrpSources_Type()
)
vRtrIgmpGrpIfMaxGrpSources.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfMaxGrpSources.setStatus("current")
_VRtrIgmpGrpIfQuerySrcIp_Type = IpAddress
_VRtrIgmpGrpIfQuerySrcIp_Object = MibTableColumn
vRtrIgmpGrpIfQuerySrcIp = _VRtrIgmpGrpIfQuerySrcIp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 3, 1, 23),
    _VRtrIgmpGrpIfQuerySrcIp_Type()
)
vRtrIgmpGrpIfQuerySrcIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfQuerySrcIp.setStatus("current")
_VRtrIgmpGrpIfHostGrpTable_Object = MibTable
vRtrIgmpGrpIfHostGrpTable = _VRtrIgmpGrpIfHostGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 4)
)
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfHostGrpTable.setStatus("current")
_VRtrIgmpGrpIfHostGrpEntry_Object = MibTableRow
vRtrIgmpGrpIfHostGrpEntry = _VRtrIgmpGrpIfHostGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 4, 1)
)
vRtrIgmpGrpIfHostGrpEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-IGMP-MIB", "vRtrIfFwdSvcId"),
    (0, "TIMETRA-IGMP-MIB", "vRtrGrpIfIndex"),
    (0, "TIMETRA-IGMP-MIB", "vRtrIgmpHostAddress"),
    (0, "TIMETRA-IGMP-MIB", "vRtrIgmpHostGroupAddress"),
)
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfHostGrpEntry.setStatus("current")
_VRtrGrpIfIndex_Type = InterfaceIndex
_VRtrGrpIfIndex_Object = MibTableColumn
vRtrGrpIfIndex = _VRtrGrpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 4, 1, 1),
    _VRtrGrpIfIndex_Type()
)
vRtrGrpIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrGrpIfIndex.setStatus("current")
_VRtrIgmpHostGroupAddress_Type = IpAddress
_VRtrIgmpHostGroupAddress_Object = MibTableColumn
vRtrIgmpHostGroupAddress = _VRtrIgmpHostGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 4, 1, 2),
    _VRtrIgmpHostGroupAddress_Type()
)
vRtrIgmpHostGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrIgmpHostGroupAddress.setStatus("current")
_VRtrIgmpGrpIfHostGrpType_Type = TmnxIgmpGroupType
_VRtrIgmpGrpIfHostGrpType_Object = MibTableColumn
vRtrIgmpGrpIfHostGrpType = _VRtrIgmpGrpIfHostGrpType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 4, 1, 3),
    _VRtrIgmpGrpIfHostGrpType_Type()
)
vRtrIgmpGrpIfHostGrpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfHostGrpType.setStatus("current")
_VRtrIgmpGrpIfHostGrpUpTime_Type = TimeTicks
_VRtrIgmpGrpIfHostGrpUpTime_Object = MibTableColumn
vRtrIgmpGrpIfHostGrpUpTime = _VRtrIgmpGrpIfHostGrpUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 4, 1, 4),
    _VRtrIgmpGrpIfHostGrpUpTime_Type()
)
vRtrIgmpGrpIfHostGrpUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfHostGrpUpTime.setStatus("current")
_VRtrIgmpGrpIfHostGrpExpiryTime_Type = TimeTicks
_VRtrIgmpGrpIfHostGrpExpiryTime_Object = MibTableColumn
vRtrIgmpGrpIfHostGrpExpiryTime = _VRtrIgmpGrpIfHostGrpExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 4, 1, 5),
    _VRtrIgmpGrpIfHostGrpExpiryTime_Type()
)
vRtrIgmpGrpIfHostGrpExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfHostGrpExpiryTime.setStatus("current")
_VRtrIgmpGrpIfHostGrpVer1HostTmr_Type = TimeTicks
_VRtrIgmpGrpIfHostGrpVer1HostTmr_Object = MibTableColumn
vRtrIgmpGrpIfHostGrpVer1HostTmr = _VRtrIgmpGrpIfHostGrpVer1HostTmr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 4, 1, 6),
    _VRtrIgmpGrpIfHostGrpVer1HostTmr_Type()
)
vRtrIgmpGrpIfHostGrpVer1HostTmr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfHostGrpVer1HostTmr.setStatus("current")
_VRtrIgmpGrpIfHostGrpMode_Type = TmnxIgmpGroupFilterMode
_VRtrIgmpGrpIfHostGrpMode_Object = MibTableColumn
vRtrIgmpGrpIfHostGrpMode = _VRtrIgmpGrpIfHostGrpMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 4, 1, 7),
    _VRtrIgmpGrpIfHostGrpMode_Type()
)
vRtrIgmpGrpIfHostGrpMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfHostGrpMode.setStatus("current")
_VRtrIgmpGrpIfHostGrpCompatMode_Type = Unsigned32
_VRtrIgmpGrpIfHostGrpCompatMode_Object = MibTableColumn
vRtrIgmpGrpIfHostGrpCompatMode = _VRtrIgmpGrpIfHostGrpCompatMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 4, 1, 8),
    _VRtrIgmpGrpIfHostGrpCompatMode_Type()
)
vRtrIgmpGrpIfHostGrpCompatMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfHostGrpCompatMode.setStatus("current")
_VRtrIgmpGrpIfHostGrpVer2HostTmr_Type = TimeTicks
_VRtrIgmpGrpIfHostGrpVer2HostTmr_Object = MibTableColumn
vRtrIgmpGrpIfHostGrpVer2HostTmr = _VRtrIgmpGrpIfHostGrpVer2HostTmr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 4, 1, 9),
    _VRtrIgmpGrpIfHostGrpVer2HostTmr_Type()
)
vRtrIgmpGrpIfHostGrpVer2HostTmr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfHostGrpVer2HostTmr.setStatus("current")
_VRtrIgmpGrpIfHostGrpMRDstVrId_Type = TmnxVRtrID
_VRtrIgmpGrpIfHostGrpMRDstVrId_Object = MibTableColumn
vRtrIgmpGrpIfHostGrpMRDstVrId = _VRtrIgmpGrpIfHostGrpMRDstVrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 4, 1, 10),
    _VRtrIgmpGrpIfHostGrpMRDstVrId_Type()
)
vRtrIgmpGrpIfHostGrpMRDstVrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfHostGrpMRDstVrId.setStatus("current")
_VRtrIgmpGrpIfHostGrpMRDstIfId_Type = InterfaceIndex
_VRtrIgmpGrpIfHostGrpMRDstIfId_Object = MibTableColumn
vRtrIgmpGrpIfHostGrpMRDstIfId = _VRtrIgmpGrpIfHostGrpMRDstIfId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 4, 1, 11),
    _VRtrIgmpGrpIfHostGrpMRDstIfId_Type()
)
vRtrIgmpGrpIfHostGrpMRDstIfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfHostGrpMRDstIfId.setStatus("current")
_VRtrIgmpGrpIfHostGrpSrcTable_Object = MibTable
vRtrIgmpGrpIfHostGrpSrcTable = _VRtrIgmpGrpIfHostGrpSrcTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 5)
)
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfHostGrpSrcTable.setStatus("current")
_VRtrIgmpGrpIfHostGrpSrcEntry_Object = MibTableRow
vRtrIgmpGrpIfHostGrpSrcEntry = _VRtrIgmpGrpIfHostGrpSrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 5, 1)
)
vRtrIgmpGrpIfHostGrpSrcEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-IGMP-MIB", "vRtrIfFwdSvcId"),
    (0, "TIMETRA-IGMP-MIB", "vRtrGrpIfIndex"),
    (0, "TIMETRA-IGMP-MIB", "vRtrIgmpHostAddress"),
    (0, "TIMETRA-IGMP-MIB", "vRtrIgmpHostGroupAddress"),
    (0, "TIMETRA-IGMP-MIB", "vRtrIgmpHostGrpSrcAddress"),
)
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfHostGrpSrcEntry.setStatus("current")
_VRtrIgmpHostGrpSrcAddress_Type = IpAddress
_VRtrIgmpHostGrpSrcAddress_Object = MibTableColumn
vRtrIgmpHostGrpSrcAddress = _VRtrIgmpHostGrpSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 5, 1, 1),
    _VRtrIgmpHostGrpSrcAddress_Type()
)
vRtrIgmpHostGrpSrcAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrIgmpHostGrpSrcAddress.setStatus("current")
_VRtrIgmpGrpIfHostGrpSrcExpTime_Type = TimeTicks
_VRtrIgmpGrpIfHostGrpSrcExpTime_Object = MibTableColumn
vRtrIgmpGrpIfHostGrpSrcExpTime = _VRtrIgmpGrpIfHostGrpSrcExpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 5, 1, 2),
    _VRtrIgmpGrpIfHostGrpSrcExpTime_Type()
)
vRtrIgmpGrpIfHostGrpSrcExpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfHostGrpSrcExpTime.setStatus("current")
_VRtrIgmpGrpIfHostGrpSrcType_Type = TmnxIgmpGroupType
_VRtrIgmpGrpIfHostGrpSrcType_Object = MibTableColumn
vRtrIgmpGrpIfHostGrpSrcType = _VRtrIgmpGrpIfHostGrpSrcType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 5, 1, 3),
    _VRtrIgmpGrpIfHostGrpSrcType_Type()
)
vRtrIgmpGrpIfHostGrpSrcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfHostGrpSrcType.setStatus("current")
_VRtrIgmpGrpIfHostGrpSrcMRDstVrId_Type = TmnxVRtrID
_VRtrIgmpGrpIfHostGrpSrcMRDstVrId_Object = MibTableColumn
vRtrIgmpGrpIfHostGrpSrcMRDstVrId = _VRtrIgmpGrpIfHostGrpSrcMRDstVrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 5, 1, 4),
    _VRtrIgmpGrpIfHostGrpSrcMRDstVrId_Type()
)
vRtrIgmpGrpIfHostGrpSrcMRDstVrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfHostGrpSrcMRDstVrId.setStatus("current")
_VRtrIgmpGrpIfHostGrpSrcMRDstIfId_Type = InterfaceIndex
_VRtrIgmpGrpIfHostGrpSrcMRDstIfId_Object = MibTableColumn
vRtrIgmpGrpIfHostGrpSrcMRDstIfId = _VRtrIgmpGrpIfHostGrpSrcMRDstIfId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 5, 1, 5),
    _VRtrIgmpGrpIfHostGrpSrcMRDstIfId_Type()
)
vRtrIgmpGrpIfHostGrpSrcMRDstIfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfHostGrpSrcMRDstIfId.setStatus("current")
_VRtrIgmpGrpSrcHostTable_Object = MibTable
vRtrIgmpGrpSrcHostTable = _VRtrIgmpGrpSrcHostTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 6)
)
if mibBuilder.loadTexts:
    vRtrIgmpGrpSrcHostTable.setStatus("current")
_VRtrIgmpGrpSrcHostEntry_Object = MibTableRow
vRtrIgmpGrpSrcHostEntry = _VRtrIgmpGrpSrcHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 6, 1)
)
vRtrIgmpGrpSrcHostEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-IGMP-MIB", "vRtrIgmpGrpSrcGroupAddress"),
    (0, "TIMETRA-IGMP-MIB", "vRtrIgmpGrpSrcSourceAddress"),
    (0, "TIMETRA-IGMP-MIB", "vRtrIgmpGrpSrcFwdOrBlk"),
    (0, "TIMETRA-IGMP-MIB", "vRtrIgmpHostAddress"),
)
if mibBuilder.loadTexts:
    vRtrIgmpGrpSrcHostEntry.setStatus("current")
_VRtrIgmpGrpSrcHostUpTime_Type = Unsigned32
_VRtrIgmpGrpSrcHostUpTime_Object = MibTableColumn
vRtrIgmpGrpSrcHostUpTime = _VRtrIgmpGrpSrcHostUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 6, 1, 1),
    _VRtrIgmpGrpSrcHostUpTime_Type()
)
vRtrIgmpGrpSrcHostUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpGrpSrcHostUpTime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrIgmpGrpSrcHostUpTime.setUnits("seconds")
_VRtrIgmpHostGrpSrcTable_Object = MibTable
vRtrIgmpHostGrpSrcTable = _VRtrIgmpHostGrpSrcTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 7)
)
if mibBuilder.loadTexts:
    vRtrIgmpHostGrpSrcTable.setStatus("current")
_VRtrIgmpHostGrpSrcEntry_Object = MibTableRow
vRtrIgmpHostGrpSrcEntry = _VRtrIgmpHostGrpSrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 7, 1)
)
vRtrIgmpHostGrpSrcEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-IGMP-MIB", "vRtrIgmpHostAddress"),
    (0, "TIMETRA-IGMP-MIB", "vRtrIgmpHostGroupAddress"),
    (0, "TIMETRA-IGMP-MIB", "vRtrIgmpHostGrpSrcAddress"),
)
if mibBuilder.loadTexts:
    vRtrIgmpHostGrpSrcEntry.setStatus("current")
_VRtrIgmpHostGrpSrcExpiryTime_Type = TimeTicks
_VRtrIgmpHostGrpSrcExpiryTime_Object = MibTableColumn
vRtrIgmpHostGrpSrcExpiryTime = _VRtrIgmpHostGrpSrcExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 7, 1, 1),
    _VRtrIgmpHostGrpSrcExpiryTime_Type()
)
vRtrIgmpHostGrpSrcExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpHostGrpSrcExpiryTime.setStatus("current")
_VRtrIgmpHostGrpSrcType_Type = TmnxIgmpGroupType
_VRtrIgmpHostGrpSrcType_Object = MibTableColumn
vRtrIgmpHostGrpSrcType = _VRtrIgmpHostGrpSrcType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 7, 1, 2),
    _VRtrIgmpHostGrpSrcType_Type()
)
vRtrIgmpHostGrpSrcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpHostGrpSrcType.setStatus("current")
_VRtrIgmpHostGrpSrcMcRdrDstVRtrID_Type = TmnxVRtrID
_VRtrIgmpHostGrpSrcMcRdrDstVRtrID_Object = MibTableColumn
vRtrIgmpHostGrpSrcMcRdrDstVRtrID = _VRtrIgmpHostGrpSrcMcRdrDstVRtrID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 7, 1, 3),
    _VRtrIgmpHostGrpSrcMcRdrDstVRtrID_Type()
)
vRtrIgmpHostGrpSrcMcRdrDstVRtrID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpHostGrpSrcMcRdrDstVRtrID.setStatus("current")
_VRtrIgmpHostGrpSrcMcRdrDstIfIdx_Type = InterfaceIndex
_VRtrIgmpHostGrpSrcMcRdrDstIfIdx_Object = MibTableColumn
vRtrIgmpHostGrpSrcMcRdrDstIfIdx = _VRtrIgmpHostGrpSrcMcRdrDstIfIdx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 7, 1, 4),
    _VRtrIgmpHostGrpSrcMcRdrDstIfIdx_Type()
)
vRtrIgmpHostGrpSrcMcRdrDstIfIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpHostGrpSrcMcRdrDstIfIdx.setStatus("current")
_VRtrIgmpHostGrpTable_Object = MibTable
vRtrIgmpHostGrpTable = _VRtrIgmpHostGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 8)
)
if mibBuilder.loadTexts:
    vRtrIgmpHostGrpTable.setStatus("current")
_VRtrIgmpHostGrpEntry_Object = MibTableRow
vRtrIgmpHostGrpEntry = _VRtrIgmpHostGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 8, 1)
)
vRtrIgmpHostGrpEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-IGMP-MIB", "vRtrIgmpHostAddress"),
    (0, "TIMETRA-IGMP-MIB", "vRtrIgmpHostGroupAddress"),
)
if mibBuilder.loadTexts:
    vRtrIgmpHostGrpEntry.setStatus("current")
_VRtrIgmpHostGrpType_Type = TmnxIgmpGroupType
_VRtrIgmpHostGrpType_Object = MibTableColumn
vRtrIgmpHostGrpType = _VRtrIgmpHostGrpType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 8, 1, 1),
    _VRtrIgmpHostGrpType_Type()
)
vRtrIgmpHostGrpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpHostGrpType.setStatus("current")
_VRtrIgmpHostGrpUpTime_Type = TimeTicks
_VRtrIgmpHostGrpUpTime_Object = MibTableColumn
vRtrIgmpHostGrpUpTime = _VRtrIgmpHostGrpUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 8, 1, 2),
    _VRtrIgmpHostGrpUpTime_Type()
)
vRtrIgmpHostGrpUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpHostGrpUpTime.setStatus("current")
_VRtrIgmpHostGrpExpiryTime_Type = TimeTicks
_VRtrIgmpHostGrpExpiryTime_Object = MibTableColumn
vRtrIgmpHostGrpExpiryTime = _VRtrIgmpHostGrpExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 8, 1, 3),
    _VRtrIgmpHostGrpExpiryTime_Type()
)
vRtrIgmpHostGrpExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpHostGrpExpiryTime.setStatus("current")
_VRtrIgmpHostGrpVer1HostTmr_Type = TimeTicks
_VRtrIgmpHostGrpVer1HostTmr_Object = MibTableColumn
vRtrIgmpHostGrpVer1HostTmr = _VRtrIgmpHostGrpVer1HostTmr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 8, 1, 4),
    _VRtrIgmpHostGrpVer1HostTmr_Type()
)
vRtrIgmpHostGrpVer1HostTmr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpHostGrpVer1HostTmr.setStatus("current")
_VRtrIgmpHostGrpMode_Type = TmnxIgmpGroupFilterMode
_VRtrIgmpHostGrpMode_Object = MibTableColumn
vRtrIgmpHostGrpMode = _VRtrIgmpHostGrpMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 8, 1, 5),
    _VRtrIgmpHostGrpMode_Type()
)
vRtrIgmpHostGrpMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpHostGrpMode.setStatus("current")
_VRtrIgmpHostGrpCompatMode_Type = Unsigned32
_VRtrIgmpHostGrpCompatMode_Object = MibTableColumn
vRtrIgmpHostGrpCompatMode = _VRtrIgmpHostGrpCompatMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 8, 1, 6),
    _VRtrIgmpHostGrpCompatMode_Type()
)
vRtrIgmpHostGrpCompatMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpHostGrpCompatMode.setStatus("current")
_VRtrIgmpHostGrpVer2HostTmr_Type = TimeTicks
_VRtrIgmpHostGrpVer2HostTmr_Object = MibTableColumn
vRtrIgmpHostGrpVer2HostTmr = _VRtrIgmpHostGrpVer2HostTmr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 8, 1, 7),
    _VRtrIgmpHostGrpVer2HostTmr_Type()
)
vRtrIgmpHostGrpVer2HostTmr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpHostGrpVer2HostTmr.setStatus("current")
_VRtrIgmpHostGrpMcRdrDstVrId_Type = TmnxVRtrID
_VRtrIgmpHostGrpMcRdrDstVrId_Object = MibTableColumn
vRtrIgmpHostGrpMcRdrDstVrId = _VRtrIgmpHostGrpMcRdrDstVrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 8, 1, 8),
    _VRtrIgmpHostGrpMcRdrDstVrId_Type()
)
vRtrIgmpHostGrpMcRdrDstVrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpHostGrpMcRdrDstVrId.setStatus("current")
_VRtrIgmpHostGrpMcRdrDstIfId_Type = InterfaceIndex
_VRtrIgmpHostGrpMcRdrDstIfId_Object = MibTableColumn
vRtrIgmpHostGrpMcRdrDstIfId = _VRtrIgmpHostGrpMcRdrDstIfId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 8, 1, 9),
    _VRtrIgmpHostGrpMcRdrDstIfId_Type()
)
vRtrIgmpHostGrpMcRdrDstIfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpHostGrpMcRdrDstIfId.setStatus("current")
_VRtrIgmpGrpIfHostTable_Object = MibTable
vRtrIgmpGrpIfHostTable = _VRtrIgmpGrpIfHostTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 9)
)
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfHostTable.setStatus("current")
_VRtrIgmpGrpIfHostEntry_Object = MibTableRow
vRtrIgmpGrpIfHostEntry = _VRtrIgmpGrpIfHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 9, 1)
)
vRtrIgmpGrpIfHostEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-IGMP-MIB", "vRtrIfFwdSvcId"),
    (0, "TIMETRA-IGMP-MIB", "vRtrGrpIfIndex"),
    (0, "TIMETRA-IGMP-MIB", "vRtrIgmpHostAddress"),
)
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfHostEntry.setStatus("current")
_VRtrIgmpGrpIfHostLastChangeTime_Type = TimeStamp
_VRtrIgmpGrpIfHostLastChangeTime_Object = MibTableColumn
vRtrIgmpGrpIfHostLastChangeTime = _VRtrIgmpGrpIfHostLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 9, 1, 1),
    _VRtrIgmpGrpIfHostLastChangeTime_Type()
)
vRtrIgmpGrpIfHostLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfHostLastChangeTime.setStatus("current")
_VRtrIgmpGrpIfHostOperState_Type = IgmpGrpItfOperState
_VRtrIgmpGrpIfHostOperState_Object = MibTableColumn
vRtrIgmpGrpIfHostOperState = _VRtrIgmpGrpIfHostOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 9, 1, 2),
    _VRtrIgmpGrpIfHostOperState_Type()
)
vRtrIgmpGrpIfHostOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfHostOperState.setStatus("current")
_VRtrIgmpHostMcRDstStatTable_Object = MibTable
vRtrIgmpHostMcRDstStatTable = _VRtrIgmpHostMcRDstStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 10)
)
if mibBuilder.loadTexts:
    vRtrIgmpHostMcRDstStatTable.setStatus("current")
_VRtrIgmpHostMcRDstStatEntry_Object = MibTableRow
vRtrIgmpHostMcRDstStatEntry = _VRtrIgmpHostMcRDstStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 10, 1)
)
vRtrIgmpHostMcRDstStatEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-IGMP-MIB", "vRtrIgmpHostAddress"),
    (0, "TIMETRA-IGMP-MIB", "vRtrIgmpHostMcRDstStatType"),
)
if mibBuilder.loadTexts:
    vRtrIgmpHostMcRDstStatEntry.setStatus("current")
_VRtrIgmpHostMcRDstStatType_Type = VRtrIgmpHostMcRDstStatType
_VRtrIgmpHostMcRDstStatType_Object = MibTableColumn
vRtrIgmpHostMcRDstStatType = _VRtrIgmpHostMcRDstStatType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 10, 1, 1),
    _VRtrIgmpHostMcRDstStatType_Type()
)
vRtrIgmpHostMcRDstStatType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrIgmpHostMcRDstStatType.setStatus("current")
_VRtrIgmpHostMcRDstStatVal_Type = Counter32
_VRtrIgmpHostMcRDstStatVal_Object = MibTableColumn
vRtrIgmpHostMcRDstStatVal = _VRtrIgmpHostMcRDstStatVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 4, 10, 1, 2),
    _VRtrIgmpHostMcRDstStatVal_Type()
)
vRtrIgmpHostMcRDstStatVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpHostMcRDstStatVal.setStatus("current")
_VRtrIgmpGrpIfObjs_ObjectIdentity = ObjectIdentity
vRtrIgmpGrpIfObjs = _VRtrIgmpGrpIfObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 5)
)
_VRtrIgmpGrpIfSapTable_Object = MibTable
vRtrIgmpGrpIfSapTable = _VRtrIgmpGrpIfSapTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 5, 1)
)
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfSapTable.setStatus("current")
_VRtrIgmpGrpIfSapEntry_Object = MibTableRow
vRtrIgmpGrpIfSapEntry = _VRtrIgmpGrpIfSapEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 5, 1, 1)
)
vRtrIgmpGrpIfSapEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-IGMP-MIB", "vRtrIfFwdSvcId"),
    (0, "TIMETRA-IGMP-MIB", "vRtrGrpIfIndex"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
)
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfSapEntry.setStatus("current")
_VRtrIgmpGrpIfSapLastChangeTime_Type = TimeStamp
_VRtrIgmpGrpIfSapLastChangeTime_Object = MibTableColumn
vRtrIgmpGrpIfSapLastChangeTime = _VRtrIgmpGrpIfSapLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 5, 1, 1, 1),
    _VRtrIgmpGrpIfSapLastChangeTime_Type()
)
vRtrIgmpGrpIfSapLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfSapLastChangeTime.setStatus("current")
_VRtrIgmpGrpIfSapOperState_Type = IgmpGrpItfOperState
_VRtrIgmpGrpIfSapOperState_Object = MibTableColumn
vRtrIgmpGrpIfSapOperState = _VRtrIgmpGrpIfSapOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 5, 1, 1, 2),
    _VRtrIgmpGrpIfSapOperState_Type()
)
vRtrIgmpGrpIfSapOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfSapOperState.setStatus("current")


class _VRtrIgmpGrpIfSapAdminVersion_Type(Unsigned32):
    """Custom type vRtrIgmpGrpIfSapAdminVersion based on Unsigned32"""
    defaultValue = 3


_VRtrIgmpGrpIfSapAdminVersion_Type.__name__ = "Unsigned32"
_VRtrIgmpGrpIfSapAdminVersion_Object = MibTableColumn
vRtrIgmpGrpIfSapAdminVersion = _VRtrIgmpGrpIfSapAdminVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 5, 1, 1, 3),
    _VRtrIgmpGrpIfSapAdminVersion_Type()
)
vRtrIgmpGrpIfSapAdminVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfSapAdminVersion.setStatus("current")
_VRtrIgmpGrpIfSapOperVersion_Type = Unsigned32
_VRtrIgmpGrpIfSapOperVersion_Object = MibTableColumn
vRtrIgmpGrpIfSapOperVersion = _VRtrIgmpGrpIfSapOperVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 5, 1, 1, 4),
    _VRtrIgmpGrpIfSapOperVersion_Type()
)
vRtrIgmpGrpIfSapOperVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfSapOperVersion.setStatus("current")
_VRtrIgmpGrpIfSapGroupCount_Type = Unsigned32
_VRtrIgmpGrpIfSapGroupCount_Object = MibTableColumn
vRtrIgmpGrpIfSapGroupCount = _VRtrIgmpGrpIfSapGroupCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 5, 1, 1, 5),
    _VRtrIgmpGrpIfSapGroupCount_Type()
)
vRtrIgmpGrpIfSapGroupCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfSapGroupCount.setStatus("current")
_VRtrIgmpGrpIfSapNextGenQueryTime_Type = Unsigned32
_VRtrIgmpGrpIfSapNextGenQueryTime_Object = MibTableColumn
vRtrIgmpGrpIfSapNextGenQueryTime = _VRtrIgmpGrpIfSapNextGenQueryTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 5, 1, 1, 6),
    _VRtrIgmpGrpIfSapNextGenQueryTime_Type()
)
vRtrIgmpGrpIfSapNextGenQueryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfSapNextGenQueryTime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfSapNextGenQueryTime.setUnits("seconds")


class _VRtrIgmpGrpIfSapMaxGroups_Type(Unsigned32):
    """Custom type vRtrIgmpGrpIfSapMaxGroups based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 16000),
    )


_VRtrIgmpGrpIfSapMaxGroups_Type.__name__ = "Unsigned32"
_VRtrIgmpGrpIfSapMaxGroups_Object = MibTableColumn
vRtrIgmpGrpIfSapMaxGroups = _VRtrIgmpGrpIfSapMaxGroups_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 5, 1, 1, 7),
    _VRtrIgmpGrpIfSapMaxGroups_Type()
)
vRtrIgmpGrpIfSapMaxGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfSapMaxGroups.setStatus("current")
_VRtrIgmpGrpIfSapMaxGroupsTillNow_Type = Counter32
_VRtrIgmpGrpIfSapMaxGroupsTillNow_Object = MibTableColumn
vRtrIgmpGrpIfSapMaxGroupsTillNow = _VRtrIgmpGrpIfSapMaxGroupsTillNow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 5, 1, 1, 8),
    _VRtrIgmpGrpIfSapMaxGroupsTillNow_Type()
)
vRtrIgmpGrpIfSapMaxGroupsTillNow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfSapMaxGroupsTillNow.setStatus("current")


class _VRtrIgmpGrpIfSapMaxSources_Type(Unsigned32):
    """Custom type vRtrIgmpGrpIfSapMaxSources based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1000),
    )


_VRtrIgmpGrpIfSapMaxSources_Type.__name__ = "Unsigned32"
_VRtrIgmpGrpIfSapMaxSources_Object = MibTableColumn
vRtrIgmpGrpIfSapMaxSources = _VRtrIgmpGrpIfSapMaxSources_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 5, 1, 1, 9),
    _VRtrIgmpGrpIfSapMaxSources_Type()
)
vRtrIgmpGrpIfSapMaxSources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfSapMaxSources.setStatus("current")


class _VRtrIgmpGrpIfSapMaxGrpSources_Type(Unsigned32):
    """Custom type vRtrIgmpGrpIfSapMaxGrpSources based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1000),
    )


_VRtrIgmpGrpIfSapMaxGrpSources_Type.__name__ = "Unsigned32"
_VRtrIgmpGrpIfSapMaxGrpSources_Object = MibTableColumn
vRtrIgmpGrpIfSapMaxGrpSources = _VRtrIgmpGrpIfSapMaxGrpSources_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 5, 1, 1, 10),
    _VRtrIgmpGrpIfSapMaxGrpSources_Type()
)
vRtrIgmpGrpIfSapMaxGrpSources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfSapMaxGrpSources.setStatus("current")
_VRtrIgmpGrpIfSapStatsTable_Object = MibTable
vRtrIgmpGrpIfSapStatsTable = _VRtrIgmpGrpIfSapStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 5, 2)
)
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfSapStatsTable.setStatus("current")
_VRtrIgmpGrpIfSapStatsEntry_Object = MibTableRow
vRtrIgmpGrpIfSapStatsEntry = _VRtrIgmpGrpIfSapStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 5, 2, 1)
)
vRtrIgmpGrpIfSapStatsEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-IGMP-MIB", "vRtrIfFwdSvcId"),
    (0, "TIMETRA-IGMP-MIB", "vRtrGrpIfIndex"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
)
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfSapStatsEntry.setStatus("current")
_VRtrIgmpGrpIfSapTxGenQueries_Type = Counter32
_VRtrIgmpGrpIfSapTxGenQueries_Object = MibTableColumn
vRtrIgmpGrpIfSapTxGenQueries = _VRtrIgmpGrpIfSapTxGenQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 5, 2, 1, 1),
    _VRtrIgmpGrpIfSapTxGenQueries_Type()
)
vRtrIgmpGrpIfSapTxGenQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfSapTxGenQueries.setStatus("current")
_VRtrIgmpGrpIfSapTxGrpQueries_Type = Counter32
_VRtrIgmpGrpIfSapTxGrpQueries_Object = MibTableColumn
vRtrIgmpGrpIfSapTxGrpQueries = _VRtrIgmpGrpIfSapTxGrpQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 5, 2, 1, 2),
    _VRtrIgmpGrpIfSapTxGrpQueries_Type()
)
vRtrIgmpGrpIfSapTxGrpQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfSapTxGrpQueries.setStatus("current")
_VRtrIgmpGrpIfSapTxGrpSrcQueries_Type = Counter32
_VRtrIgmpGrpIfSapTxGrpSrcQueries_Object = MibTableColumn
vRtrIgmpGrpIfSapTxGrpSrcQueries = _VRtrIgmpGrpIfSapTxGrpSrcQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 5, 2, 1, 3),
    _VRtrIgmpGrpIfSapTxGrpSrcQueries_Type()
)
vRtrIgmpGrpIfSapTxGrpSrcQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfSapTxGrpSrcQueries.setStatus("current")
_VRtrIgmpGrpIfSapTxV1Reports_Type = Counter32
_VRtrIgmpGrpIfSapTxV1Reports_Object = MibTableColumn
vRtrIgmpGrpIfSapTxV1Reports = _VRtrIgmpGrpIfSapTxV1Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 5, 2, 1, 4),
    _VRtrIgmpGrpIfSapTxV1Reports_Type()
)
vRtrIgmpGrpIfSapTxV1Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfSapTxV1Reports.setStatus("current")
_VRtrIgmpGrpIfSapTxV2Reports_Type = Counter32
_VRtrIgmpGrpIfSapTxV2Reports_Object = MibTableColumn
vRtrIgmpGrpIfSapTxV2Reports = _VRtrIgmpGrpIfSapTxV2Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 5, 2, 1, 5),
    _VRtrIgmpGrpIfSapTxV2Reports_Type()
)
vRtrIgmpGrpIfSapTxV2Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfSapTxV2Reports.setStatus("current")
_VRtrIgmpGrpIfSapTxV3Reports_Type = Counter32
_VRtrIgmpGrpIfSapTxV3Reports_Object = MibTableColumn
vRtrIgmpGrpIfSapTxV3Reports = _VRtrIgmpGrpIfSapTxV3Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 5, 2, 1, 6),
    _VRtrIgmpGrpIfSapTxV3Reports_Type()
)
vRtrIgmpGrpIfSapTxV3Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfSapTxV3Reports.setStatus("current")
_VRtrIgmpGrpIfSapTxLeaves_Type = Counter32
_VRtrIgmpGrpIfSapTxLeaves_Object = MibTableColumn
vRtrIgmpGrpIfSapTxLeaves = _VRtrIgmpGrpIfSapTxLeaves_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 5, 2, 1, 7),
    _VRtrIgmpGrpIfSapTxLeaves_Type()
)
vRtrIgmpGrpIfSapTxLeaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfSapTxLeaves.setStatus("current")
_VRtrIgmpGrpIfSapTxErrors_Type = Counter32
_VRtrIgmpGrpIfSapTxErrors_Object = MibTableColumn
vRtrIgmpGrpIfSapTxErrors = _VRtrIgmpGrpIfSapTxErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 5, 2, 1, 8),
    _VRtrIgmpGrpIfSapTxErrors_Type()
)
vRtrIgmpGrpIfSapTxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfSapTxErrors.setStatus("current")
_VRtrIgmpGrpIfSapRxGenQueries_Type = Counter32
_VRtrIgmpGrpIfSapRxGenQueries_Object = MibTableColumn
vRtrIgmpGrpIfSapRxGenQueries = _VRtrIgmpGrpIfSapRxGenQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 5, 2, 1, 9),
    _VRtrIgmpGrpIfSapRxGenQueries_Type()
)
vRtrIgmpGrpIfSapRxGenQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfSapRxGenQueries.setStatus("current")
_VRtrIgmpGrpIfSapRxGrpQueries_Type = Counter32
_VRtrIgmpGrpIfSapRxGrpQueries_Object = MibTableColumn
vRtrIgmpGrpIfSapRxGrpQueries = _VRtrIgmpGrpIfSapRxGrpQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 5, 2, 1, 10),
    _VRtrIgmpGrpIfSapRxGrpQueries_Type()
)
vRtrIgmpGrpIfSapRxGrpQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfSapRxGrpQueries.setStatus("current")
_VRtrIgmpGrpIfSapRxGrpSrcQueries_Type = Counter32
_VRtrIgmpGrpIfSapRxGrpSrcQueries_Object = MibTableColumn
vRtrIgmpGrpIfSapRxGrpSrcQueries = _VRtrIgmpGrpIfSapRxGrpSrcQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 5, 2, 1, 11),
    _VRtrIgmpGrpIfSapRxGrpSrcQueries_Type()
)
vRtrIgmpGrpIfSapRxGrpSrcQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfSapRxGrpSrcQueries.setStatus("current")
_VRtrIgmpGrpIfSapRxV1Reports_Type = Counter32
_VRtrIgmpGrpIfSapRxV1Reports_Object = MibTableColumn
vRtrIgmpGrpIfSapRxV1Reports = _VRtrIgmpGrpIfSapRxV1Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 5, 2, 1, 12),
    _VRtrIgmpGrpIfSapRxV1Reports_Type()
)
vRtrIgmpGrpIfSapRxV1Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfSapRxV1Reports.setStatus("current")
_VRtrIgmpGrpIfSapRxV2Reports_Type = Counter32
_VRtrIgmpGrpIfSapRxV2Reports_Object = MibTableColumn
vRtrIgmpGrpIfSapRxV2Reports = _VRtrIgmpGrpIfSapRxV2Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 5, 2, 1, 13),
    _VRtrIgmpGrpIfSapRxV2Reports_Type()
)
vRtrIgmpGrpIfSapRxV2Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfSapRxV2Reports.setStatus("current")
_VRtrIgmpGrpIfSapRxV3Reports_Type = Counter32
_VRtrIgmpGrpIfSapRxV3Reports_Object = MibTableColumn
vRtrIgmpGrpIfSapRxV3Reports = _VRtrIgmpGrpIfSapRxV3Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 5, 2, 1, 14),
    _VRtrIgmpGrpIfSapRxV3Reports_Type()
)
vRtrIgmpGrpIfSapRxV3Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfSapRxV3Reports.setStatus("current")
_VRtrIgmpGrpIfSapRxLeaves_Type = Counter32
_VRtrIgmpGrpIfSapRxLeaves_Object = MibTableColumn
vRtrIgmpGrpIfSapRxLeaves = _VRtrIgmpGrpIfSapRxLeaves_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 5, 2, 1, 15),
    _VRtrIgmpGrpIfSapRxLeaves_Type()
)
vRtrIgmpGrpIfSapRxLeaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfSapRxLeaves.setStatus("current")
_VRtrIgmpGrpIfSapRxBadLenPkts_Type = Counter32
_VRtrIgmpGrpIfSapRxBadLenPkts_Object = MibTableColumn
vRtrIgmpGrpIfSapRxBadLenPkts = _VRtrIgmpGrpIfSapRxBadLenPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 5, 2, 1, 16),
    _VRtrIgmpGrpIfSapRxBadLenPkts_Type()
)
vRtrIgmpGrpIfSapRxBadLenPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfSapRxBadLenPkts.setStatus("current")
_VRtrIgmpGrpIfSapRxBadChksumPkts_Type = Counter32
_VRtrIgmpGrpIfSapRxBadChksumPkts_Object = MibTableColumn
vRtrIgmpGrpIfSapRxBadChksumPkts = _VRtrIgmpGrpIfSapRxBadChksumPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 5, 2, 1, 17),
    _VRtrIgmpGrpIfSapRxBadChksumPkts_Type()
)
vRtrIgmpGrpIfSapRxBadChksumPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfSapRxBadChksumPkts.setStatus("current")
_VRtrIgmpGrpIfSapRxUnknTypePkts_Type = Counter32
_VRtrIgmpGrpIfSapRxUnknTypePkts_Object = MibTableColumn
vRtrIgmpGrpIfSapRxUnknTypePkts = _VRtrIgmpGrpIfSapRxUnknTypePkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 5, 2, 1, 18),
    _VRtrIgmpGrpIfSapRxUnknTypePkts_Type()
)
vRtrIgmpGrpIfSapRxUnknTypePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfSapRxUnknTypePkts.setStatus("current")
_VRtrIgmpGrpIfSapRxBadRecvIfPkts_Type = Counter32
_VRtrIgmpGrpIfSapRxBadRecvIfPkts_Object = MibTableColumn
vRtrIgmpGrpIfSapRxBadRecvIfPkts = _VRtrIgmpGrpIfSapRxBadRecvIfPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 5, 2, 1, 19),
    _VRtrIgmpGrpIfSapRxBadRecvIfPkts_Type()
)
vRtrIgmpGrpIfSapRxBadRecvIfPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfSapRxBadRecvIfPkts.setStatus("current")
_VRtrIgmpGrpIfSapRxNonLocal_Type = Counter32
_VRtrIgmpGrpIfSapRxNonLocal_Object = MibTableColumn
vRtrIgmpGrpIfSapRxNonLocal = _VRtrIgmpGrpIfSapRxNonLocal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 5, 2, 1, 20),
    _VRtrIgmpGrpIfSapRxNonLocal_Type()
)
vRtrIgmpGrpIfSapRxNonLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfSapRxNonLocal.setStatus("current")
_VRtrIgmpGrpIfSapRxWrongVersions_Type = Counter32
_VRtrIgmpGrpIfSapRxWrongVersions_Object = MibTableColumn
vRtrIgmpGrpIfSapRxWrongVersions = _VRtrIgmpGrpIfSapRxWrongVersions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 5, 2, 1, 21),
    _VRtrIgmpGrpIfSapRxWrongVersions_Type()
)
vRtrIgmpGrpIfSapRxWrongVersions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfSapRxWrongVersions.setStatus("current")
_VRtrIgmpGrpIfSapImportPlcyDrops_Type = Counter32
_VRtrIgmpGrpIfSapImportPlcyDrops_Object = MibTableColumn
vRtrIgmpGrpIfSapImportPlcyDrops = _VRtrIgmpGrpIfSapImportPlcyDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 5, 2, 1, 22),
    _VRtrIgmpGrpIfSapImportPlcyDrops_Type()
)
vRtrIgmpGrpIfSapImportPlcyDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfSapImportPlcyDrops.setStatus("current")
_VRtrIgmpGrpIfSapRxNoRtrAlertPkts_Type = Counter32
_VRtrIgmpGrpIfSapRxNoRtrAlertPkts_Object = MibTableColumn
vRtrIgmpGrpIfSapRxNoRtrAlertPkts = _VRtrIgmpGrpIfSapRxNoRtrAlertPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 5, 2, 1, 23),
    _VRtrIgmpGrpIfSapRxNoRtrAlertPkts_Type()
)
vRtrIgmpGrpIfSapRxNoRtrAlertPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfSapRxNoRtrAlertPkts.setStatus("current")
_VRtrIgmpGrpIfSapRxBadEncodings_Type = Counter32
_VRtrIgmpGrpIfSapRxBadEncodings_Object = MibTableColumn
vRtrIgmpGrpIfSapRxBadEncodings = _VRtrIgmpGrpIfSapRxBadEncodings_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 5, 2, 1, 24),
    _VRtrIgmpGrpIfSapRxBadEncodings_Type()
)
vRtrIgmpGrpIfSapRxBadEncodings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfSapRxBadEncodings.setStatus("current")
_VRtrIgmpGrpIfSapRxPktDrops_Type = Counter32
_VRtrIgmpGrpIfSapRxPktDrops_Object = MibTableColumn
vRtrIgmpGrpIfSapRxPktDrops = _VRtrIgmpGrpIfSapRxPktDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 5, 2, 1, 25),
    _VRtrIgmpGrpIfSapRxPktDrops_Type()
)
vRtrIgmpGrpIfSapRxPktDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfSapRxPktDrops.setStatus("current")
_VRtrIgmpGrpIfSapStatsStarGTypes_Type = Gauge32
_VRtrIgmpGrpIfSapStatsStarGTypes_Object = MibTableColumn
vRtrIgmpGrpIfSapStatsStarGTypes = _VRtrIgmpGrpIfSapStatsStarGTypes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 5, 2, 1, 26),
    _VRtrIgmpGrpIfSapStatsStarGTypes_Type()
)
vRtrIgmpGrpIfSapStatsStarGTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfSapStatsStarGTypes.setStatus("current")
_VRtrIgmpGrpIfSapStatsSGTypes_Type = Gauge32
_VRtrIgmpGrpIfSapStatsSGTypes_Object = MibTableColumn
vRtrIgmpGrpIfSapStatsSGTypes = _VRtrIgmpGrpIfSapStatsSGTypes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 5, 2, 1, 27),
    _VRtrIgmpGrpIfSapStatsSGTypes_Type()
)
vRtrIgmpGrpIfSapStatsSGTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfSapStatsSGTypes.setStatus("current")
_VRtrIgmpGrpIfSapStatsMcacPlcyDrp_Type = Counter32
_VRtrIgmpGrpIfSapStatsMcacPlcyDrp_Object = MibTableColumn
vRtrIgmpGrpIfSapStatsMcacPlcyDrp = _VRtrIgmpGrpIfSapStatsMcacPlcyDrp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 5, 2, 1, 28),
    _VRtrIgmpGrpIfSapStatsMcacPlcyDrp_Type()
)
vRtrIgmpGrpIfSapStatsMcacPlcyDrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfSapStatsMcacPlcyDrp.setStatus("current")
_VRtrIgmpGrpIfSapRxLocalScopePkts_Type = Counter32
_VRtrIgmpGrpIfSapRxLocalScopePkts_Object = MibTableColumn
vRtrIgmpGrpIfSapRxLocalScopePkts = _VRtrIgmpGrpIfSapRxLocalScopePkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 5, 2, 1, 29),
    _VRtrIgmpGrpIfSapRxLocalScopePkts_Type()
)
vRtrIgmpGrpIfSapRxLocalScopePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfSapRxLocalScopePkts.setStatus("current")
_VRtrIgmpGrpIfSapRxRsvdScopePkts_Type = Counter32
_VRtrIgmpGrpIfSapRxRsvdScopePkts_Object = MibTableColumn
vRtrIgmpGrpIfSapRxRsvdScopePkts = _VRtrIgmpGrpIfSapRxRsvdScopePkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 5, 2, 1, 30),
    _VRtrIgmpGrpIfSapRxRsvdScopePkts_Type()
)
vRtrIgmpGrpIfSapRxRsvdScopePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfSapRxRsvdScopePkts.setStatus("current")
_VRtrIgmpGrpIfSapGrpTable_Object = MibTable
vRtrIgmpGrpIfSapGrpTable = _VRtrIgmpGrpIfSapGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 5, 3)
)
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfSapGrpTable.setStatus("current")
_VRtrIgmpGrpIfSapGrpEntry_Object = MibTableRow
vRtrIgmpGrpIfSapGrpEntry = _VRtrIgmpGrpIfSapGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 5, 3, 1)
)
vRtrIgmpGrpIfSapGrpEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-IGMP-MIB", "vRtrIfFwdSvcId"),
    (0, "TIMETRA-IGMP-MIB", "vRtrGrpIfIndex"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfSapGroupAddress"),
)
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfSapGrpEntry.setStatus("current")
_VRtrIgmpGrpIfSapGroupAddress_Type = IpAddress
_VRtrIgmpGrpIfSapGroupAddress_Object = MibTableColumn
vRtrIgmpGrpIfSapGroupAddress = _VRtrIgmpGrpIfSapGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 5, 3, 1, 1),
    _VRtrIgmpGrpIfSapGroupAddress_Type()
)
vRtrIgmpGrpIfSapGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfSapGroupAddress.setStatus("current")
_VRtrIgmpGrpIfSapGrpType_Type = TmnxIgmpGroupType
_VRtrIgmpGrpIfSapGrpType_Object = MibTableColumn
vRtrIgmpGrpIfSapGrpType = _VRtrIgmpGrpIfSapGrpType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 5, 3, 1, 2),
    _VRtrIgmpGrpIfSapGrpType_Type()
)
vRtrIgmpGrpIfSapGrpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfSapGrpType.setStatus("current")
_VRtrIgmpGrpIfSapGrpUpTime_Type = TimeTicks
_VRtrIgmpGrpIfSapGrpUpTime_Object = MibTableColumn
vRtrIgmpGrpIfSapGrpUpTime = _VRtrIgmpGrpIfSapGrpUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 5, 3, 1, 3),
    _VRtrIgmpGrpIfSapGrpUpTime_Type()
)
vRtrIgmpGrpIfSapGrpUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfSapGrpUpTime.setStatus("current")
_VRtrIgmpGrpIfSapGrpExpiryTime_Type = TimeTicks
_VRtrIgmpGrpIfSapGrpExpiryTime_Object = MibTableColumn
vRtrIgmpGrpIfSapGrpExpiryTime = _VRtrIgmpGrpIfSapGrpExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 5, 3, 1, 4),
    _VRtrIgmpGrpIfSapGrpExpiryTime_Type()
)
vRtrIgmpGrpIfSapGrpExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfSapGrpExpiryTime.setStatus("current")
_VRtrIgmpGrpIfSapGrpVer1HostTmr_Type = TimeTicks
_VRtrIgmpGrpIfSapGrpVer1HostTmr_Object = MibTableColumn
vRtrIgmpGrpIfSapGrpVer1HostTmr = _VRtrIgmpGrpIfSapGrpVer1HostTmr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 5, 3, 1, 5),
    _VRtrIgmpGrpIfSapGrpVer1HostTmr_Type()
)
vRtrIgmpGrpIfSapGrpVer1HostTmr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfSapGrpVer1HostTmr.setStatus("current")
_VRtrIgmpGrpIfSapGrpMode_Type = TmnxIgmpGroupFilterMode
_VRtrIgmpGrpIfSapGrpMode_Object = MibTableColumn
vRtrIgmpGrpIfSapGrpMode = _VRtrIgmpGrpIfSapGrpMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 5, 3, 1, 6),
    _VRtrIgmpGrpIfSapGrpMode_Type()
)
vRtrIgmpGrpIfSapGrpMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfSapGrpMode.setStatus("current")
_VRtrIgmpGrpIfSapGrpCompatMode_Type = Unsigned32
_VRtrIgmpGrpIfSapGrpCompatMode_Object = MibTableColumn
vRtrIgmpGrpIfSapGrpCompatMode = _VRtrIgmpGrpIfSapGrpCompatMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 5, 3, 1, 7),
    _VRtrIgmpGrpIfSapGrpCompatMode_Type()
)
vRtrIgmpGrpIfSapGrpCompatMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfSapGrpCompatMode.setStatus("current")
_VRtrIgmpGrpIfSapGrpVer2HostTmr_Type = TimeTicks
_VRtrIgmpGrpIfSapGrpVer2HostTmr_Object = MibTableColumn
vRtrIgmpGrpIfSapGrpVer2HostTmr = _VRtrIgmpGrpIfSapGrpVer2HostTmr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 5, 3, 1, 8),
    _VRtrIgmpGrpIfSapGrpVer2HostTmr_Type()
)
vRtrIgmpGrpIfSapGrpVer2HostTmr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfSapGrpVer2HostTmr.setStatus("current")
_VRtrIgmpGrpIfSapGrpSrcTable_Object = MibTable
vRtrIgmpGrpIfSapGrpSrcTable = _VRtrIgmpGrpIfSapGrpSrcTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 5, 4)
)
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfSapGrpSrcTable.setStatus("current")
_VRtrIgmpGrpIfSapGrpSrcEntry_Object = MibTableRow
vRtrIgmpGrpIfSapGrpSrcEntry = _VRtrIgmpGrpIfSapGrpSrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 5, 4, 1)
)
vRtrIgmpGrpIfSapGrpSrcEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-IGMP-MIB", "vRtrIfFwdSvcId"),
    (0, "TIMETRA-IGMP-MIB", "vRtrGrpIfIndex"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfSapGroupAddress"),
    (0, "TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfSapGrpSrcAddress"),
)
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfSapGrpSrcEntry.setStatus("current")
_VRtrIgmpGrpIfSapGrpSrcAddress_Type = IpAddress
_VRtrIgmpGrpIfSapGrpSrcAddress_Object = MibTableColumn
vRtrIgmpGrpIfSapGrpSrcAddress = _VRtrIgmpGrpIfSapGrpSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 5, 4, 1, 1),
    _VRtrIgmpGrpIfSapGrpSrcAddress_Type()
)
vRtrIgmpGrpIfSapGrpSrcAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfSapGrpSrcAddress.setStatus("current")
_VRtrIgmpGrpIfSapGrpSrcExpTime_Type = TimeTicks
_VRtrIgmpGrpIfSapGrpSrcExpTime_Object = MibTableColumn
vRtrIgmpGrpIfSapGrpSrcExpTime = _VRtrIgmpGrpIfSapGrpSrcExpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 5, 4, 1, 2),
    _VRtrIgmpGrpIfSapGrpSrcExpTime_Type()
)
vRtrIgmpGrpIfSapGrpSrcExpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfSapGrpSrcExpTime.setStatus("current")
_VRtrIgmpGrpIfSapGrpSrcType_Type = TmnxIgmpGroupType
_VRtrIgmpGrpIfSapGrpSrcType_Object = MibTableColumn
vRtrIgmpGrpIfSapGrpSrcType = _VRtrIgmpGrpIfSapGrpSrcType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 5, 4, 1, 3),
    _VRtrIgmpGrpIfSapGrpSrcType_Type()
)
vRtrIgmpGrpIfSapGrpSrcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfSapGrpSrcType.setStatus("current")
_VRtrIgmpGrpSrcGrpIfSapTable_Object = MibTable
vRtrIgmpGrpSrcGrpIfSapTable = _VRtrIgmpGrpSrcGrpIfSapTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 5, 5)
)
if mibBuilder.loadTexts:
    vRtrIgmpGrpSrcGrpIfSapTable.setStatus("current")
_VRtrIgmpGrpSrcGrpIfSapEntry_Object = MibTableRow
vRtrIgmpGrpSrcGrpIfSapEntry = _VRtrIgmpGrpSrcGrpIfSapEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 5, 5, 1)
)
vRtrIgmpGrpSrcGrpIfSapEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-IGMP-MIB", "vRtrIgmpGrpSrcGroupAddress"),
    (0, "TIMETRA-IGMP-MIB", "vRtrIgmpGrpSrcSourceAddress"),
    (0, "TIMETRA-IGMP-MIB", "vRtrIgmpGrpSrcFwdOrBlk"),
    (0, "TIMETRA-IGMP-MIB", "vRtrIfFwdSvcId"),
    (0, "TIMETRA-IGMP-MIB", "vRtrGrpIfIndex"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
)
if mibBuilder.loadTexts:
    vRtrIgmpGrpSrcGrpIfSapEntry.setStatus("current")
_VRtrIgmpGrpSrcGrpIfSapUpTime_Type = Unsigned32
_VRtrIgmpGrpSrcGrpIfSapUpTime_Object = MibTableColumn
vRtrIgmpGrpSrcGrpIfSapUpTime = _VRtrIgmpGrpSrcGrpIfSapUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 23, 5, 5, 1, 1),
    _VRtrIgmpGrpSrcGrpIfSapUpTime_Type()
)
vRtrIgmpGrpSrcGrpIfSapUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIgmpGrpSrcGrpIfSapUpTime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrIgmpGrpSrcGrpIfSapUpTime.setUnits("seconds")
_VRtrIgmpNotifyPrefix_ObjectIdentity = ObjectIdentity
vRtrIgmpNotifyPrefix = _VRtrIgmpNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 23)
)
_VRtrIgmpNotifications_ObjectIdentity = ObjectIdentity
vRtrIgmpNotifications = _VRtrIgmpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 23, 0)
)
vRtrIgmpGeneralEntry.registerAugmentions(
    ("TIMETRA-IGMP-MIB",
     "vRtrIgmpGenStatsEntry")
)
vRtrIgmpGenStatsEntry.setIndexNames(*vRtrIgmpGeneralEntry.getIndexNames())
vRtrIgmpIfEntry.registerAugmentions(
    ("TIMETRA-IGMP-MIB",
     "vRtrIgmpIfStatsEntry")
)
vRtrIgmpIfStatsEntry.setIndexNames(*vRtrIgmpIfEntry.getIndexNames())
vRtrIgmpHostEntry.registerAugmentions(
    ("TIMETRA-IGMP-MIB",
     "vRtrIgmpHostStatsEntry")
)
vRtrIgmpHostStatsEntry.setIndexNames(*vRtrIgmpHostEntry.getIndexNames())

# Managed Objects groups

tmnxIgmpGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 23, 2, 1)
)
tmnxIgmpGlobalGroup.setObjects(
      *(("TIMETRA-IGMP-MIB", "vRtrIgmpGenQueryInterval"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGenLastMembQueryIntvl"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGenQueryResponseIntvl"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGenRobustCount"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGenLastChange"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGenAdminState"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGenOperState"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpSrcFwdOrBlk"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpSrcUpTime"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpSSMTranslateRowStatus"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGenStatsStarGTypes"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGenStatsSGTypes"))
)
if mibBuilder.loadTexts:
    tmnxIgmpGlobalGroup.setStatus("current")

tmnxIgmpNotifyObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 23, 2, 3)
)
tmnxIgmpNotifyObjsGroup.setObjects(
    ("TIMETRA-IGMP-MIB", "vRtrIgmpNotifyQueryVersion")
)
if mibBuilder.loadTexts:
    tmnxIgmpNotifyObjsGroup.setStatus("obsolete")

tmnxIgmpIfV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 23, 2, 5)
)
tmnxIgmpIfV4v0Group.setObjects(
      *(("TIMETRA-IGMP-MIB", "vRtrIgmpIfRowStatus"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfLastChangeTime"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfAdminState"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfOperState"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfAdminVersion"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfOperVersion"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfQuerier"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfImportPolicy"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfGroupCount"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfQuerierUpTime"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfQuerierExpiryTime"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfNextGenQueryTime"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfSubnetCheck"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfGroupType"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfGroupUpTime"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfGroupExpiryTime"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfGroupVersion1HostTimer"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfGroupMode"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfGroupCompatMode"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfGroupVersion2HostTimer"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfGroupLastReporter"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfGrpSrcExpiryTime"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfGrpSrcType"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfStaticGrpSrcRowStatus"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfTxGenQueries"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfTxGrpQueries"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfTxGrpSrcQueries"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfTxV1Reports"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfTxV2Reports"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfTxV3Reports"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfTxLeaves"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfTxErrors"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfRxGenQueries"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfRxGrpQueries"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfRxGrpSrcQueries"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfRxV1Reports"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfRxV2Reports"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfRxV3Reports"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfRxLeaves"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfRxBadLenPkts"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfRxBadChecksumPkts"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfRxUnknownTypePkts"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfRxBadReceiveIfPkts"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfRxNonLocal"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfRxWrongVersions"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfImportPolicyDrops"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfRxNoRtrAlertPkts"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfRxBadEncodings"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfRxPktDrops"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfStatsStarGTypes"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfStatsSGTypes"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfMaxGroups"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfMaxGroupsTillNow"))
)
if mibBuilder.loadTexts:
    tmnxIgmpIfV4v0Group.setStatus("obsolete")

tmnxIgmpIfV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 23, 2, 6)
)
tmnxIgmpIfV5v0Group.setObjects(
      *(("TIMETRA-IGMP-MIB", "vRtrIgmpIfRowStatus"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfLastChangeTime"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfAdminState"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfOperState"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfAdminVersion"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfOperVersion"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfQuerier"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfImportPolicy"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfGroupCount"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfQuerierUpTime"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfQuerierExpiryTime"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfNextGenQueryTime"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfSubnetCheck"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfGroupType"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfGroupUpTime"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfGroupExpiryTime"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfGroupVersion1HostTimer"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfGroupMode"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfGroupCompatMode"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfGroupVersion2HostTimer"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfGroupLastReporter"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfGrpSrcExpiryTime"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfGrpSrcType"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfStaticGrpSrcRowStatus"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfTxGenQueries"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfTxGrpQueries"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfTxGrpSrcQueries"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfTxV1Reports"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfTxV2Reports"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfTxV3Reports"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfTxLeaves"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfTxErrors"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfRxGenQueries"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfRxGrpQueries"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfRxGrpSrcQueries"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfRxV1Reports"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfRxV2Reports"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfRxV3Reports"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfRxLeaves"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfRxBadLenPkts"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfRxBadChecksumPkts"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfRxUnknownTypePkts"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfRxBadReceiveIfPkts"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfRxNonLocal"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfRxWrongVersions"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfImportPolicyDrops"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfRxNoRtrAlertPkts"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfRxBadEncodings"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfRxPktDrops"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfStatsStarGTypes"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfStatsSGTypes"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfMaxGroups"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfMaxGroupsTillNow"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfMcacPolicyName"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfMcacUnconstrainedBW"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfMcacConstAdminState"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfMcacLevelRowStatus"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfMcacLevelBW"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfMcacLagRowStatus"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfMcacLagLevel"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfStatsMcacPolicyDrops"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfRxLocalScopePkts"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfRxRsvdScopePkts"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfMcacPreRsvdMandBW"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfMcacinUseMandBw"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfMcacinUseOpnlBw"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfMcacAvailMandBw"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfMcacAvailOpnlBw"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfMcacValuesInTransit"))
)
if mibBuilder.loadTexts:
    tmnxIgmpIfV5v0Group.setStatus("current")

tmnxIgmpNotifyObjsV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 23, 2, 7)
)
tmnxIgmpNotifyObjsV5v0Group.setObjects(
      *(("TIMETRA-IGMP-MIB", "vRtrIgmpNotifyQueryVersion"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpNotifyGrpAddrType"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpNotifyGrpAddr"))
)
if mibBuilder.loadTexts:
    tmnxIgmpNotifyObjsV5v0Group.setStatus("obsolete")

tmnxIgmpIfV6v1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 23, 2, 9)
)
tmnxIgmpIfV6v1Group.setObjects(
      *(("TIMETRA-IGMP-MIB", "vRtrIgmpIfSSMTltTableLastChanged"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfSSMTransRowStatus"))
)
if mibBuilder.loadTexts:
    tmnxIgmpIfV6v1Group.setStatus("current")

tmnxIgmpIfV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 23, 2, 10)
)
tmnxIgmpIfV7v0Group.setObjects(
      *(("TIMETRA-IGMP-MIB", "vRtrIgmpRsvpIfRowStatus"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpRsvpIfIndex"))
)
if mibBuilder.loadTexts:
    tmnxIgmpIfV7v0Group.setStatus("current")

tmnxIgmpIfV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 23, 2, 11)
)
tmnxIgmpIfV8v0Group.setObjects(
      *(("TIMETRA-IGMP-MIB", "vRtrIgmpLdpIfTableLastChanged"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpRsvpIfBfdEnable"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpRsvpIfAdminState"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpRsvpIfOperState"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpLdpIfRowStatus"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpLdpIfLastChanged"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpLdpIfIndex"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpLdpIfAdminState"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpLdpIfOperState"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpHostLastChangeTime"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpHostOperState"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpHostOperVersion"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpHostGroupCount"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpHostNextGenQueryTime"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpHostMaxGroupsTillNow"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpHostFwdSvcId"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpHostGrpIfId"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpHostPppoeSessionId"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpHostSubscriberId"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpHostMacAddress"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpHostIgmpPolicy"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpHostMaxGroups"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpHostAdminVersion"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpHostTxGenQueries"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpHostTxGrpQueries"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpHostTxGrpSrcQueries"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpHostTxV1Reports"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpHostTxV2Reports"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpHostTxV3Reports"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpHostTxLeaves"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpHostTxErrors"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpHostRxGenQueries"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpHostRxGrpQueries"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpHostRxGrpSrcQueries"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpHostRxV1Reports"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpHostRxV2Reports"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpHostRxV3Reports"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpHostRxLeaves"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpHostRxBadLenPkts"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpHostRxBadChecksumPkts"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpHostRxUnknownTypePkts"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpHostRxBadReceiveIfPkts"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpHostRxNonLocal"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpHostRxWrongVersions"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpHostImportPolicyDrops"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpHostRxNoRtrAlertPkts"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpHostRxBadEncodings"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpHostRxPktDrops"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpHostStatsStarGTypes"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpHostStatsSGTypes"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpHostStatsMcacPolicyDrops"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpHostRxLocalScopePkts"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpHostRxRsvdScopePkts"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpHostRedirectionDrops"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfRowStatus"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfLastChangeTime"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfAdminState"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfOperState"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfHostGrpType"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfHostGrpUpTime"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfHostGrpExpiryTime"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfHostGrpVer1HostTmr"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfHostGrpMode"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfHostGrpCompatMode"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfHostGrpVer2HostTmr"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfHostGrpSrcExpTime"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfHostGrpSrcType"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfHostGrpSrcMRDstVrId"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfHostGrpSrcMRDstIfId"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpSrcHostUpTime"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpHostGrpSrcExpiryTime"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpHostGrpSrcType"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpHostGrpSrcMcRdrDstVRtrID"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpHostGrpSrcMcRdrDstIfIdx"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpHostGrpType"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpHostGrpUpTime"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpHostGrpExpiryTime"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpHostGrpVer1HostTmr"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpHostGrpMode"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpHostGrpCompatMode"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpHostGrpVer2HostTmr"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfHostLastChangeTime"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfHostOperState"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfDisRtrAlertChk"))
)
if mibBuilder.loadTexts:
    tmnxIgmpIfV8v0Group.setStatus("current")

tmnxIgmpNotifyObjsV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 23, 2, 12)
)
tmnxIgmpNotifyObjsV8v0Group.setObjects(
      *(("TIMETRA-IGMP-MIB", "vRtrIgmpNotifyQueryVersion"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpNotifyGrpAddrType"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpNotifyGrpAddr"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpNotifyDescription"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpNotifyMcacPolicyName"))
)
if mibBuilder.loadTexts:
    tmnxIgmpNotifyObjsV8v0Group.setStatus("current")

tmnxIgmpIfV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 23, 2, 14)
)
tmnxIgmpIfV9v0Group.setObjects(
      *(("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfSubHostsOnly"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfAdminVersion"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfImportPolicy"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfSubnetCheck"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfMcacPolicyName"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfMcacUnconstrainedBW"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfMcacConstAdminState"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfMcacPreRsvdMandBW"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfMcacinUseMandBw"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfMcacinUseOpnlBw"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfMcacAvailMandBw"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfMcacAvailOpnlBw"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfMcacValuesInTransit"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfDisRtrAlertChk"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfMaxGroups"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfSapLastChangeTime"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfSapOperState"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfSapAdminVersion"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfSapOperVersion"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfSapGroupCount"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfSapNextGenQueryTime"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfSapMaxGroups"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfSapMaxGroupsTillNow"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfSapTxGenQueries"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfSapTxGrpQueries"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfSapTxGrpSrcQueries"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfSapTxV1Reports"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfSapTxV2Reports"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfSapTxV3Reports"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfSapTxLeaves"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfSapTxErrors"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfSapRxGenQueries"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfSapRxGrpQueries"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfSapRxGrpSrcQueries"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfSapRxV1Reports"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfSapRxV2Reports"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfSapRxV3Reports"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfSapRxLeaves"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfSapRxBadLenPkts"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfSapRxBadChksumPkts"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfSapRxUnknTypePkts"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfSapRxBadRecvIfPkts"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfSapRxNonLocal"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfSapRxWrongVersions"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfSapImportPlcyDrops"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfSapRxNoRtrAlertPkts"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfSapRxBadEncodings"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfSapRxPktDrops"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfSapStatsStarGTypes"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfSapStatsSGTypes"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfSapStatsMcacPlcyDrp"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfSapRxLocalScopePkts"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfSapRxRsvdScopePkts"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfSapGrpType"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfSapGrpUpTime"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfSapGrpExpiryTime"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfSapGrpVer1HostTmr"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfSapGrpMode"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfSapGrpCompatMode"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfSapGrpVer2HostTmr"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfSapGrpSrcExpTime"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfSapGrpSrcType"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpSrcGrpIfSapUpTime"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpHostMcRDstStatVal"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfHostGrpMRDstVrId"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfHostGrpMRDstIfId"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpHostGrpMcRdrDstVrId"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpHostGrpMcRdrDstIfId"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpSrcSummFwdInterfaces"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpSrcSummBlkInterfaces"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpSrcSummFwdHosts"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpSrcSummBlkHosts"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpSrcSummFwdGrpIfSaps"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpSrcSummBlkGrpIfSaps"))
)
if mibBuilder.loadTexts:
    tmnxIgmpIfV9v0Group.setStatus("current")

tmnxIgmpIfV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 23, 2, 15)
)
tmnxIgmpIfV10v0Group.setObjects(
      *(("TIMETRA-IGMP-MIB", "vRtrIgmpIfMaxSources"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfMaxSources"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpHostMaxSources"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfSapMaxSources"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfQuerySrcIp"))
)
if mibBuilder.loadTexts:
    tmnxIgmpIfV10v0Group.setStatus("current")

tmnxIgmpGlobalV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 23, 2, 17)
)
tmnxIgmpGlobalV10v0Group.setObjects(
    ("TIMETRA-IGMP-MIB", "vRtrIgmpGenGrpIfQuerySrcIp")
)
if mibBuilder.loadTexts:
    tmnxIgmpGlobalV10v0Group.setStatus("current")

tmnxIgmpIfV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 23, 2, 18)
)
tmnxIgmpIfV11v0Group.setObjects(
      *(("TIMETRA-IGMP-MIB", "vRtrIgmpIfMaxGrpSources"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfMaxGrpSources"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpHostMaxGrpSources"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfSapMaxGrpSources"))
)
if mibBuilder.loadTexts:
    tmnxIgmpIfV11v0Group.setStatus("current")

tmnxIgmpIfV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 23, 2, 20)
)
tmnxIgmpIfV12v0Group.setObjects(
      *(("TIMETRA-IGMP-MIB", "vRtrIgmpIfQueryInterval"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfLastMembQueryIntvl"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfQueryResponseIntvl"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfMcacUseLagPortWeight"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfRedundantMcast"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfRedundantMcastFwding"))
)
if mibBuilder.loadTexts:
    tmnxIgmpIfV12v0Group.setStatus("current")

tmnxIgmpNotifyObjsV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 23, 2, 21)
)
tmnxIgmpNotifyObjsV12v0Group.setObjects(
      *(("TIMETRA-IGMP-MIB", "vRtrIgmpNotifySrcAddrType"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpNotifySrcAddr"))
)
if mibBuilder.loadTexts:
    tmnxIgmpNotifyObjsV12v0Group.setStatus("current")


# Notification objects

vRtrIgmpIfRxQueryVerMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 23, 0, 1)
)
vRtrIgmpIfRxQueryVerMismatch.setObjects(
      *(("TIMETRA-VRTR-MIB", "vRtrID"),
        ("TIMETRA-VRTR-MIB", "vRtrIfIndex"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfAdminVersion"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpNotifyQueryVersion"))
)
if mibBuilder.loadTexts:
    vRtrIgmpIfRxQueryVerMismatch.setStatus(
        "current"
    )

vRtrIgmpIfCModeRxQueryMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 23, 0, 2)
)
vRtrIgmpIfCModeRxQueryMismatch.setObjects(
      *(("TIMETRA-VRTR-MIB", "vRtrID"),
        ("TIMETRA-VRTR-MIB", "vRtrIfIndex"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfOperVersion"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpNotifyQueryVersion"))
)
if mibBuilder.loadTexts:
    vRtrIgmpIfCModeRxQueryMismatch.setStatus(
        "current"
    )

vRtrIgmpMaxGrpsLimitExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 23, 0, 3)
)
vRtrIgmpMaxGrpsLimitExceeded.setObjects(
    ("TIMETRA-IGMP-MIB", "vRtrIgmpIfMaxGroups")
)
if mibBuilder.loadTexts:
    vRtrIgmpMaxGrpsLimitExceeded.setStatus(
        "current"
    )

vRtrIgmpMcacPlcyDropped = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 23, 0, 4)
)
vRtrIgmpMcacPlcyDropped.setObjects(
      *(("TIMETRA-IGMP-MIB", "vRtrIgmpIfMcacPolicyName"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpNotifyGrpAddrType"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpNotifyGrpAddr"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpNotifySrcAddrType"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpNotifySrcAddr"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpNotifyDescription"))
)
if mibBuilder.loadTexts:
    vRtrIgmpMcacPlcyDropped.setStatus(
        "current"
    )

vRtrIgmpHostInstantiationFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 23, 0, 5)
)
vRtrIgmpHostInstantiationFail.setObjects(
      *(("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfHostLastChangeTime"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpNotifyDescription"))
)
if mibBuilder.loadTexts:
    vRtrIgmpHostInstantiationFail.setStatus(
        "current"
    )

vRtrIgmpHostMaxGrpsLimitExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 23, 0, 6)
)
vRtrIgmpHostMaxGrpsLimitExceeded.setObjects(
      *(("TIMETRA-IGMP-MIB", "vRtrIgmpHostFwdSvcId"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpHostGrpIfId"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpHostMaxGroups"))
)
if mibBuilder.loadTexts:
    vRtrIgmpHostMaxGrpsLimitExceeded.setStatus(
        "current"
    )

vRtrIgmpHostMcacPlcyDropped = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 23, 0, 7)
)
vRtrIgmpHostMcacPlcyDropped.setObjects(
      *(("TIMETRA-IGMP-MIB", "vRtrIgmpHostSubscriberId"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpNotifyMcacPolicyName"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpNotifyGrpAddrType"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpNotifyGrpAddr"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpNotifySrcAddrType"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpNotifySrcAddr"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpNotifyDescription"))
)
if mibBuilder.loadTexts:
    vRtrIgmpHostMcacPlcyDropped.setStatus(
        "current"
    )

vRtrIgmpHostCModeRxQueryMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 23, 0, 8)
)
vRtrIgmpHostCModeRxQueryMismatch.setObjects(
      *(("TIMETRA-IGMP-MIB", "vRtrIgmpHostOperVersion"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpNotifyQueryVersion"))
)
if mibBuilder.loadTexts:
    vRtrIgmpHostCModeRxQueryMismatch.setStatus(
        "current"
    )

vRtrIgmpHostRxQueryVerMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 23, 0, 9)
)
vRtrIgmpHostRxQueryVerMismatch.setObjects(
      *(("TIMETRA-IGMP-MIB", "vRtrIgmpHostAdminVersion"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpNotifyQueryVersion"))
)
if mibBuilder.loadTexts:
    vRtrIgmpHostRxQueryVerMismatch.setStatus(
        "current"
    )

vRtrIgmpHostMaxSrcsLimitExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 23, 0, 10)
)
vRtrIgmpHostMaxSrcsLimitExceeded.setObjects(
      *(("TIMETRA-IGMP-MIB", "vRtrIgmpHostFwdSvcId"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpHostGrpIfId"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpHostMaxSources"))
)
if mibBuilder.loadTexts:
    vRtrIgmpHostMaxSrcsLimitExceeded.setStatus(
        "current"
    )

vRtrIgmpMaxSrcsLimitExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 23, 0, 11)
)
vRtrIgmpMaxSrcsLimitExceeded.setObjects(
    ("TIMETRA-IGMP-MIB", "vRtrIgmpIfMaxSources")
)
if mibBuilder.loadTexts:
    vRtrIgmpMaxSrcsLimitExceeded.setStatus(
        "current"
    )

vRtrIgmpGrpIfSapMaxGrpsLimExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 23, 0, 12)
)
vRtrIgmpGrpIfSapMaxGrpsLimExceed.setObjects(
    ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfSapMaxGroups")
)
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfSapMaxGrpsLimExceed.setStatus(
        "current"
    )

vRtrIgmpGrpIfSapMaxSrcsLimExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 23, 0, 13)
)
vRtrIgmpGrpIfSapMaxSrcsLimExceed.setObjects(
    ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfSapMaxSources")
)
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfSapMaxSrcsLimExceed.setStatus(
        "current"
    )

vRtrIgmpGrpIfSapMcacPlcyDropped = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 23, 0, 14)
)
vRtrIgmpGrpIfSapMcacPlcyDropped.setObjects(
      *(("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfSapLastChangeTime"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpNotifyMcacPolicyName"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpNotifyGrpAddrType"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpNotifyGrpAddr"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpNotifySrcAddrType"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpNotifySrcAddr"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpNotifyDescription"))
)
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfSapMcacPlcyDropped.setStatus(
        "current"
    )

vRtrIgmpGrpIfSapCModeRxQueryMism = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 23, 0, 15)
)
vRtrIgmpGrpIfSapCModeRxQueryMism.setObjects(
      *(("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfSapOperVersion"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpNotifyQueryVersion"))
)
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfSapCModeRxQueryMism.setStatus(
        "current"
    )

vRtrIgmpGrpIfSapRxQueryVerMism = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 23, 0, 16)
)
vRtrIgmpGrpIfSapRxQueryVerMism.setObjects(
      *(("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfSapAdminVersion"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpNotifyQueryVersion"))
)
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfSapRxQueryVerMism.setStatus(
        "current"
    )

vRtrIgmpHostMaxGrpSrcsLimitExcd = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 23, 0, 17)
)
vRtrIgmpHostMaxGrpSrcsLimitExcd.setObjects(
      *(("TIMETRA-IGMP-MIB", "vRtrIgmpHostFwdSvcId"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpHostGrpIfId"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpHostMaxGrpSources"))
)
if mibBuilder.loadTexts:
    vRtrIgmpHostMaxGrpSrcsLimitExcd.setStatus(
        "current"
    )

vRtrIgmpMaxGrpSrcsLimitExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 23, 0, 18)
)
vRtrIgmpMaxGrpSrcsLimitExceeded.setObjects(
    ("TIMETRA-IGMP-MIB", "vRtrIgmpIfMaxGrpSources")
)
if mibBuilder.loadTexts:
    vRtrIgmpMaxGrpSrcsLimitExceeded.setStatus(
        "current"
    )

vRtrIgmpGrpIfSapMaxGrpSrcLimExcd = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 23, 0, 19)
)
vRtrIgmpGrpIfSapMaxGrpSrcLimExcd.setObjects(
    ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfSapMaxGrpSources")
)
if mibBuilder.loadTexts:
    vRtrIgmpGrpIfSapMaxGrpSrcLimExcd.setStatus(
        "current"
    )


# Notifications groups

tmnxIgmpNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 23, 2, 4)
)
tmnxIgmpNotificationGroup.setObjects(
      *(("TIMETRA-IGMP-MIB", "vRtrIgmpIfRxQueryVerMismatch"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfCModeRxQueryMismatch"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpMaxGrpsLimitExceeded"))
)
if mibBuilder.loadTexts:
    tmnxIgmpNotificationGroup.setStatus(
        "obsolete"
    )

tmnxIgmpNotificationV5v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 23, 2, 8)
)
tmnxIgmpNotificationV5v0Group.setObjects(
      *(("TIMETRA-IGMP-MIB", "vRtrIgmpIfRxQueryVerMismatch"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfCModeRxQueryMismatch"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpMaxGrpsLimitExceeded"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpMcacPlcyDropped"))
)
if mibBuilder.loadTexts:
    tmnxIgmpNotificationV5v0Group.setStatus(
        "obsolete"
    )

tmnxIgmpNotificationV8v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 23, 2, 13)
)
tmnxIgmpNotificationV8v0Group.setObjects(
      *(("TIMETRA-IGMP-MIB", "vRtrIgmpIfRxQueryVerMismatch"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfCModeRxQueryMismatch"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpMaxGrpsLimitExceeded"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpMcacPlcyDropped"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpHostInstantiationFail"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpHostMaxGrpsLimitExceeded"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpHostMcacPlcyDropped"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpHostCModeRxQueryMismatch"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpHostRxQueryVerMismatch"))
)
if mibBuilder.loadTexts:
    tmnxIgmpNotificationV8v0Group.setStatus(
        "obsolete"
    )

tmnxIgmpNotificationV10v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 23, 2, 16)
)
tmnxIgmpNotificationV10v0Group.setObjects(
      *(("TIMETRA-IGMP-MIB", "vRtrIgmpIfRxQueryVerMismatch"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfCModeRxQueryMismatch"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpMaxGrpsLimitExceeded"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpMcacPlcyDropped"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpHostInstantiationFail"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpHostMaxGrpsLimitExceeded"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpHostMcacPlcyDropped"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpHostCModeRxQueryMismatch"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpHostRxQueryVerMismatch"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpHostMaxSrcsLimitExceeded"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpMaxSrcsLimitExceeded"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfSapMaxGrpsLimExceed"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfSapMaxSrcsLimExceed"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfSapMcacPlcyDropped"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfSapCModeRxQueryMism"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfSapRxQueryVerMism"))
)
if mibBuilder.loadTexts:
    tmnxIgmpNotificationV10v0Group.setStatus(
        "obsolete"
    )

tmnxIgmpNotificationV11v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 23, 2, 19)
)
tmnxIgmpNotificationV11v0Group.setObjects(
      *(("TIMETRA-IGMP-MIB", "vRtrIgmpIfRxQueryVerMismatch"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpIfCModeRxQueryMismatch"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpMaxGrpsLimitExceeded"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpMcacPlcyDropped"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpHostInstantiationFail"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpHostMaxGrpsLimitExceeded"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpHostMcacPlcyDropped"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpHostCModeRxQueryMismatch"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpHostRxQueryVerMismatch"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpHostMaxSrcsLimitExceeded"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpMaxSrcsLimitExceeded"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfSapMaxGrpsLimExceed"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfSapMaxSrcsLimExceed"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfSapMcacPlcyDropped"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfSapCModeRxQueryMism"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfSapRxQueryVerMism"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpHostMaxGrpSrcsLimitExcd"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpMaxGrpSrcsLimitExceeded"),
        ("TIMETRA-IGMP-MIB", "vRtrIgmpGrpIfSapMaxGrpSrcLimExcd"))
)
if mibBuilder.loadTexts:
    tmnxIgmpNotificationV11v0Group.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tmnxIgmpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 23, 1, 1)
)
tmnxIgmpCompliance.setObjects(
      *(("TIMETRA-IGMP-MIB", "tmnxIgmpGlobalGroup"),
        ("TIMETRA-IGMP-MIB", "tmnxIgmpNotificationGroup"),
        ("TIMETRA-IGMP-MIB", "tmnxIgmpIfV4v0Group"))
)
if mibBuilder.loadTexts:
    tmnxIgmpCompliance.setStatus(
        "obsolete"
    )

tmnxIgmpV5v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 23, 1, 2)
)
tmnxIgmpV5v0Compliance.setObjects(
      *(("TIMETRA-IGMP-MIB", "tmnxIgmpGlobalGroup"),
        ("TIMETRA-IGMP-MIB", "tmnxIgmpNotificationV5v0Group"),
        ("TIMETRA-IGMP-MIB", "tmnxIgmpIfV5v0Group"))
)
if mibBuilder.loadTexts:
    tmnxIgmpV5v0Compliance.setStatus(
        "obsolete"
    )

tmnxIgmpV6v1Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 23, 1, 3)
)
tmnxIgmpV6v1Compliance.setObjects(
      *(("TIMETRA-IGMP-MIB", "tmnxIgmpGlobalGroup"),
        ("TIMETRA-IGMP-MIB", "tmnxIgmpNotificationV5v0Group"),
        ("TIMETRA-IGMP-MIB", "tmnxIgmpIfV5v0Group"),
        ("TIMETRA-IGMP-MIB", "tmnxIgmpIfV6v1Group"))
)
if mibBuilder.loadTexts:
    tmnxIgmpV6v1Compliance.setStatus(
        "obsolete"
    )

tmnxIgmpV7v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 23, 1, 4)
)
tmnxIgmpV7v0Compliance.setObjects(
      *(("TIMETRA-IGMP-MIB", "tmnxIgmpGlobalGroup"),
        ("TIMETRA-IGMP-MIB", "tmnxIgmpNotificationV5v0Group"),
        ("TIMETRA-IGMP-MIB", "tmnxIgmpIfV5v0Group"),
        ("TIMETRA-IGMP-MIB", "tmnxIgmpIfV6v1Group"),
        ("TIMETRA-IGMP-MIB", "tmnxIgmpIfV7v0Group"))
)
if mibBuilder.loadTexts:
    tmnxIgmpV7v0Compliance.setStatus(
        "obsolete"
    )

tmnxIgmpV8v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 23, 1, 5)
)
tmnxIgmpV8v0Compliance.setObjects(
      *(("TIMETRA-IGMP-MIB", "tmnxIgmpGlobalGroup"),
        ("TIMETRA-IGMP-MIB", "tmnxIgmpNotificationV8v0Group"),
        ("TIMETRA-IGMP-MIB", "tmnxIgmpIfV5v0Group"),
        ("TIMETRA-IGMP-MIB", "tmnxIgmpIfV6v1Group"),
        ("TIMETRA-IGMP-MIB", "tmnxIgmpIfV7v0Group"),
        ("TIMETRA-IGMP-MIB", "tmnxIgmpIfV8v0Group"))
)
if mibBuilder.loadTexts:
    tmnxIgmpV8v0Compliance.setStatus(
        "obsolete"
    )

tmnxIgmpV9v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 23, 1, 6)
)
tmnxIgmpV9v0Compliance.setObjects(
      *(("TIMETRA-IGMP-MIB", "tmnxIgmpGlobalGroup"),
        ("TIMETRA-IGMP-MIB", "tmnxIgmpNotificationV8v0Group"),
        ("TIMETRA-IGMP-MIB", "tmnxIgmpIfV5v0Group"),
        ("TIMETRA-IGMP-MIB", "tmnxIgmpIfV6v1Group"),
        ("TIMETRA-IGMP-MIB", "tmnxIgmpIfV7v0Group"),
        ("TIMETRA-IGMP-MIB", "tmnxIgmpIfV8v0Group"),
        ("TIMETRA-IGMP-MIB", "tmnxIgmpIfV9v0Group"))
)
if mibBuilder.loadTexts:
    tmnxIgmpV9v0Compliance.setStatus(
        "obsolete"
    )

tmnxIgmpV10v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 23, 1, 7)
)
tmnxIgmpV10v0Compliance.setObjects(
      *(("TIMETRA-IGMP-MIB", "tmnxIgmpGlobalGroup"),
        ("TIMETRA-IGMP-MIB", "tmnxIgmpGlobalV10v0Group"),
        ("TIMETRA-IGMP-MIB", "tmnxIgmpIfV5v0Group"),
        ("TIMETRA-IGMP-MIB", "tmnxIgmpIfV6v1Group"),
        ("TIMETRA-IGMP-MIB", "tmnxIgmpIfV7v0Group"),
        ("TIMETRA-IGMP-MIB", "tmnxIgmpIfV8v0Group"),
        ("TIMETRA-IGMP-MIB", "tmnxIgmpIfV9v0Group"),
        ("TIMETRA-IGMP-MIB", "tmnxIgmpIfV10v0Group"),
        ("TIMETRA-IGMP-MIB", "tmnxIgmpNotificationV10v0Group"))
)
if mibBuilder.loadTexts:
    tmnxIgmpV10v0Compliance.setStatus(
        "obsolete"
    )

tmnxIgmpV11v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 23, 1, 8)
)
tmnxIgmpV11v0Compliance.setObjects(
      *(("TIMETRA-IGMP-MIB", "tmnxIgmpGlobalGroup"),
        ("TIMETRA-IGMP-MIB", "tmnxIgmpGlobalV10v0Group"),
        ("TIMETRA-IGMP-MIB", "tmnxIgmpIfV5v0Group"),
        ("TIMETRA-IGMP-MIB", "tmnxIgmpIfV6v1Group"),
        ("TIMETRA-IGMP-MIB", "tmnxIgmpIfV7v0Group"),
        ("TIMETRA-IGMP-MIB", "tmnxIgmpIfV8v0Group"),
        ("TIMETRA-IGMP-MIB", "tmnxIgmpIfV9v0Group"),
        ("TIMETRA-IGMP-MIB", "tmnxIgmpIfV10v0Group"),
        ("TIMETRA-IGMP-MIB", "tmnxIgmpIfV11v0Group"),
        ("TIMETRA-IGMP-MIB", "tmnxIgmpNotificationV11v0Group"))
)
if mibBuilder.loadTexts:
    tmnxIgmpV11v0Compliance.setStatus(
        "obsolete"
    )

tmnxIgmpV12v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 23, 1, 9)
)
tmnxIgmpV12v0Compliance.setObjects(
      *(("TIMETRA-IGMP-MIB", "tmnxIgmpGlobalGroup"),
        ("TIMETRA-IGMP-MIB", "tmnxIgmpGlobalV10v0Group"),
        ("TIMETRA-IGMP-MIB", "tmnxIgmpIfV5v0Group"),
        ("TIMETRA-IGMP-MIB", "tmnxIgmpIfV6v1Group"),
        ("TIMETRA-IGMP-MIB", "tmnxIgmpIfV7v0Group"),
        ("TIMETRA-IGMP-MIB", "tmnxIgmpIfV8v0Group"),
        ("TIMETRA-IGMP-MIB", "tmnxIgmpIfV9v0Group"),
        ("TIMETRA-IGMP-MIB", "tmnxIgmpIfV10v0Group"),
        ("TIMETRA-IGMP-MIB", "tmnxIgmpIfV11v0Group"),
        ("TIMETRA-IGMP-MIB", "tmnxIgmpIfV12v0Group"),
        ("TIMETRA-IGMP-MIB", "tmnxIgmpNotificationV11v0Group"))
)
if mibBuilder.loadTexts:
    tmnxIgmpV12v0Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-IGMP-MIB",
    **{"IgmpGrpItfOperState": IgmpGrpItfOperState,
       "VRtrIgmpHostMcRDstStatType": VRtrIgmpHostMcRDstStatType,
       "timetraIgmpMIBModule": timetraIgmpMIBModule,
       "tmnxIgmpConformance": tmnxIgmpConformance,
       "tmnxIgmpCompliances": tmnxIgmpCompliances,
       "tmnxIgmpCompliance": tmnxIgmpCompliance,
       "tmnxIgmpV5v0Compliance": tmnxIgmpV5v0Compliance,
       "tmnxIgmpV6v1Compliance": tmnxIgmpV6v1Compliance,
       "tmnxIgmpV7v0Compliance": tmnxIgmpV7v0Compliance,
       "tmnxIgmpV8v0Compliance": tmnxIgmpV8v0Compliance,
       "tmnxIgmpV9v0Compliance": tmnxIgmpV9v0Compliance,
       "tmnxIgmpV10v0Compliance": tmnxIgmpV10v0Compliance,
       "tmnxIgmpV11v0Compliance": tmnxIgmpV11v0Compliance,
       "tmnxIgmpV12v0Compliance": tmnxIgmpV12v0Compliance,
       "tmnxIgmpGroups": tmnxIgmpGroups,
       "tmnxIgmpGlobalGroup": tmnxIgmpGlobalGroup,
       "tmnxIgmpNotifyObjsGroup": tmnxIgmpNotifyObjsGroup,
       "tmnxIgmpNotificationGroup": tmnxIgmpNotificationGroup,
       "tmnxIgmpIfV4v0Group": tmnxIgmpIfV4v0Group,
       "tmnxIgmpIfV5v0Group": tmnxIgmpIfV5v0Group,
       "tmnxIgmpNotifyObjsV5v0Group": tmnxIgmpNotifyObjsV5v0Group,
       "tmnxIgmpNotificationV5v0Group": tmnxIgmpNotificationV5v0Group,
       "tmnxIgmpIfV6v1Group": tmnxIgmpIfV6v1Group,
       "tmnxIgmpIfV7v0Group": tmnxIgmpIfV7v0Group,
       "tmnxIgmpIfV8v0Group": tmnxIgmpIfV8v0Group,
       "tmnxIgmpNotifyObjsV8v0Group": tmnxIgmpNotifyObjsV8v0Group,
       "tmnxIgmpNotificationV8v0Group": tmnxIgmpNotificationV8v0Group,
       "tmnxIgmpIfV9v0Group": tmnxIgmpIfV9v0Group,
       "tmnxIgmpIfV10v0Group": tmnxIgmpIfV10v0Group,
       "tmnxIgmpNotificationV10v0Group": tmnxIgmpNotificationV10v0Group,
       "tmnxIgmpGlobalV10v0Group": tmnxIgmpGlobalV10v0Group,
       "tmnxIgmpIfV11v0Group": tmnxIgmpIfV11v0Group,
       "tmnxIgmpNotificationV11v0Group": tmnxIgmpNotificationV11v0Group,
       "tmnxIgmpIfV12v0Group": tmnxIgmpIfV12v0Group,
       "tmnxIgmpNotifyObjsV12v0Group": tmnxIgmpNotifyObjsV12v0Group,
       "tmnxIgmpObjs": tmnxIgmpObjs,
       "vRtrIgmpProtocolObjs": vRtrIgmpProtocolObjs,
       "vRtrIgmpGeneralTable": vRtrIgmpGeneralTable,
       "vRtrIgmpGeneralEntry": vRtrIgmpGeneralEntry,
       "vRtrIgmpGenQueryInterval": vRtrIgmpGenQueryInterval,
       "vRtrIgmpGenLastMembQueryIntvl": vRtrIgmpGenLastMembQueryIntvl,
       "vRtrIgmpGenQueryResponseIntvl": vRtrIgmpGenQueryResponseIntvl,
       "vRtrIgmpGenRobustCount": vRtrIgmpGenRobustCount,
       "vRtrIgmpGenLastChange": vRtrIgmpGenLastChange,
       "vRtrIgmpGenAdminState": vRtrIgmpGenAdminState,
       "vRtrIgmpGenOperState": vRtrIgmpGenOperState,
       "vRtrIgmpGenGrpIfQuerySrcIp": vRtrIgmpGenGrpIfQuerySrcIp,
       "vRtrIgmpGrpSrcTable": vRtrIgmpGrpSrcTable,
       "vRtrIgmpGrpSrcEntry": vRtrIgmpGrpSrcEntry,
       "vRtrIgmpGrpSrcGroupAddress": vRtrIgmpGrpSrcGroupAddress,
       "vRtrIgmpGrpSrcSourceAddress": vRtrIgmpGrpSrcSourceAddress,
       "vRtrIgmpGrpSrcFwdOrBlk": vRtrIgmpGrpSrcFwdOrBlk,
       "vRtrIgmpGrpSrcUpTime": vRtrIgmpGrpSrcUpTime,
       "vRtrIgmpSSMTranslateTable": vRtrIgmpSSMTranslateTable,
       "vRtrIgmpSSMTranslateEntry": vRtrIgmpSSMTranslateEntry,
       "vRtrIgmpSSMTranslateGrpAddr1": vRtrIgmpSSMTranslateGrpAddr1,
       "vRtrIgmpSSMTranslateGrpAddr2": vRtrIgmpSSMTranslateGrpAddr2,
       "vRtrIgmpSSMTranslateSrcAddr": vRtrIgmpSSMTranslateSrcAddr,
       "vRtrIgmpSSMTranslateRowStatus": vRtrIgmpSSMTranslateRowStatus,
       "vRtrIgmpGenStatsTable": vRtrIgmpGenStatsTable,
       "vRtrIgmpGenStatsEntry": vRtrIgmpGenStatsEntry,
       "vRtrIgmpGenStatsStarGTypes": vRtrIgmpGenStatsStarGTypes,
       "vRtrIgmpGenStatsSGTypes": vRtrIgmpGenStatsSGTypes,
       "vRtrIgmpGrpSrcSummaryTable": vRtrIgmpGrpSrcSummaryTable,
       "vRtrIgmpGrpSrcSummaryEntry": vRtrIgmpGrpSrcSummaryEntry,
       "vRtrIgmpGrpSrcSummFwdInterfaces": vRtrIgmpGrpSrcSummFwdInterfaces,
       "vRtrIgmpGrpSrcSummBlkInterfaces": vRtrIgmpGrpSrcSummBlkInterfaces,
       "vRtrIgmpGrpSrcSummFwdHosts": vRtrIgmpGrpSrcSummFwdHosts,
       "vRtrIgmpGrpSrcSummBlkHosts": vRtrIgmpGrpSrcSummBlkHosts,
       "vRtrIgmpGrpSrcSummFwdGrpIfSaps": vRtrIgmpGrpSrcSummFwdGrpIfSaps,
       "vRtrIgmpGrpSrcSummBlkGrpIfSaps": vRtrIgmpGrpSrcSummBlkGrpIfSaps,
       "vRtrIgmpIfObjs": vRtrIgmpIfObjs,
       "vRtrIgmpIfTable": vRtrIgmpIfTable,
       "vRtrIgmpIfEntry": vRtrIgmpIfEntry,
       "vRtrIgmpIfRowStatus": vRtrIgmpIfRowStatus,
       "vRtrIgmpIfLastChangeTime": vRtrIgmpIfLastChangeTime,
       "vRtrIgmpIfAdminState": vRtrIgmpIfAdminState,
       "vRtrIgmpIfOperState": vRtrIgmpIfOperState,
       "vRtrIgmpIfAdminVersion": vRtrIgmpIfAdminVersion,
       "vRtrIgmpIfOperVersion": vRtrIgmpIfOperVersion,
       "vRtrIgmpIfQuerier": vRtrIgmpIfQuerier,
       "vRtrIgmpIfImportPolicy": vRtrIgmpIfImportPolicy,
       "vRtrIgmpIfGroupCount": vRtrIgmpIfGroupCount,
       "vRtrIgmpIfQuerierUpTime": vRtrIgmpIfQuerierUpTime,
       "vRtrIgmpIfQuerierExpiryTime": vRtrIgmpIfQuerierExpiryTime,
       "vRtrIgmpIfNextGenQueryTime": vRtrIgmpIfNextGenQueryTime,
       "vRtrIgmpIfSubnetCheck": vRtrIgmpIfSubnetCheck,
       "vRtrIgmpIfMaxGroups": vRtrIgmpIfMaxGroups,
       "vRtrIgmpIfMaxGroupsTillNow": vRtrIgmpIfMaxGroupsTillNow,
       "vRtrIgmpIfMcacPolicyName": vRtrIgmpIfMcacPolicyName,
       "vRtrIgmpIfMcacUnconstrainedBW": vRtrIgmpIfMcacUnconstrainedBW,
       "vRtrIgmpIfMcacConstAdminState": vRtrIgmpIfMcacConstAdminState,
       "vRtrIgmpIfMcacPreRsvdMandBW": vRtrIgmpIfMcacPreRsvdMandBW,
       "vRtrIgmpIfMcacinUseMandBw": vRtrIgmpIfMcacinUseMandBw,
       "vRtrIgmpIfMcacinUseOpnlBw": vRtrIgmpIfMcacinUseOpnlBw,
       "vRtrIgmpIfMcacAvailMandBw": vRtrIgmpIfMcacAvailMandBw,
       "vRtrIgmpIfMcacAvailOpnlBw": vRtrIgmpIfMcacAvailOpnlBw,
       "vRtrIgmpIfMcacValuesInTransit": vRtrIgmpIfMcacValuesInTransit,
       "vRtrIgmpIfDisRtrAlertChk": vRtrIgmpIfDisRtrAlertChk,
       "vRtrIgmpIfMaxSources": vRtrIgmpIfMaxSources,
       "vRtrIgmpIfMaxGrpSources": vRtrIgmpIfMaxGrpSources,
       "vRtrIgmpIfQueryInterval": vRtrIgmpIfQueryInterval,
       "vRtrIgmpIfLastMembQueryIntvl": vRtrIgmpIfLastMembQueryIntvl,
       "vRtrIgmpIfQueryResponseIntvl": vRtrIgmpIfQueryResponseIntvl,
       "vRtrIgmpIfMcacUseLagPortWeight": vRtrIgmpIfMcacUseLagPortWeight,
       "vRtrIgmpIfRedundantMcast": vRtrIgmpIfRedundantMcast,
       "vRtrIgmpIfRedundantMcastFwding": vRtrIgmpIfRedundantMcastFwding,
       "vRtrIgmpIfGroupTable": vRtrIgmpIfGroupTable,
       "vRtrIgmpIfGroupEntry": vRtrIgmpIfGroupEntry,
       "vRtrIgmpIfGroupAddress": vRtrIgmpIfGroupAddress,
       "vRtrIgmpIfGroupType": vRtrIgmpIfGroupType,
       "vRtrIgmpIfGroupUpTime": vRtrIgmpIfGroupUpTime,
       "vRtrIgmpIfGroupExpiryTime": vRtrIgmpIfGroupExpiryTime,
       "vRtrIgmpIfGroupVersion1HostTimer": vRtrIgmpIfGroupVersion1HostTimer,
       "vRtrIgmpIfGroupMode": vRtrIgmpIfGroupMode,
       "vRtrIgmpIfGroupCompatMode": vRtrIgmpIfGroupCompatMode,
       "vRtrIgmpIfGroupVersion2HostTimer": vRtrIgmpIfGroupVersion2HostTimer,
       "vRtrIgmpIfGroupLastReporter": vRtrIgmpIfGroupLastReporter,
       "vRtrIgmpIfGrpSrcTable": vRtrIgmpIfGrpSrcTable,
       "vRtrIgmpIfGrpSrcEntry": vRtrIgmpIfGrpSrcEntry,
       "vRtrIgmpIfGrpSrcAddress": vRtrIgmpIfGrpSrcAddress,
       "vRtrIgmpIfGrpSrcExpiryTime": vRtrIgmpIfGrpSrcExpiryTime,
       "vRtrIgmpIfGrpSrcType": vRtrIgmpIfGrpSrcType,
       "vRtrIgmpIfStaticGrpSrcTable": vRtrIgmpIfStaticGrpSrcTable,
       "vRtrIgmpIfStaticGrpSrcEntry": vRtrIgmpIfStaticGrpSrcEntry,
       "vRtrIgmpIfStaticGrpSrcRowStatus": vRtrIgmpIfStaticGrpSrcRowStatus,
       "vRtrIgmpIfStatsTable": vRtrIgmpIfStatsTable,
       "vRtrIgmpIfStatsEntry": vRtrIgmpIfStatsEntry,
       "vRtrIgmpIfTxGenQueries": vRtrIgmpIfTxGenQueries,
       "vRtrIgmpIfTxGrpQueries": vRtrIgmpIfTxGrpQueries,
       "vRtrIgmpIfTxGrpSrcQueries": vRtrIgmpIfTxGrpSrcQueries,
       "vRtrIgmpIfTxV1Reports": vRtrIgmpIfTxV1Reports,
       "vRtrIgmpIfTxV2Reports": vRtrIgmpIfTxV2Reports,
       "vRtrIgmpIfTxV3Reports": vRtrIgmpIfTxV3Reports,
       "vRtrIgmpIfTxLeaves": vRtrIgmpIfTxLeaves,
       "vRtrIgmpIfTxErrors": vRtrIgmpIfTxErrors,
       "vRtrIgmpIfRxGenQueries": vRtrIgmpIfRxGenQueries,
       "vRtrIgmpIfRxGrpQueries": vRtrIgmpIfRxGrpQueries,
       "vRtrIgmpIfRxGrpSrcQueries": vRtrIgmpIfRxGrpSrcQueries,
       "vRtrIgmpIfRxV1Reports": vRtrIgmpIfRxV1Reports,
       "vRtrIgmpIfRxV2Reports": vRtrIgmpIfRxV2Reports,
       "vRtrIgmpIfRxV3Reports": vRtrIgmpIfRxV3Reports,
       "vRtrIgmpIfRxLeaves": vRtrIgmpIfRxLeaves,
       "vRtrIgmpIfRxBadLenPkts": vRtrIgmpIfRxBadLenPkts,
       "vRtrIgmpIfRxBadChecksumPkts": vRtrIgmpIfRxBadChecksumPkts,
       "vRtrIgmpIfRxUnknownTypePkts": vRtrIgmpIfRxUnknownTypePkts,
       "vRtrIgmpIfRxBadReceiveIfPkts": vRtrIgmpIfRxBadReceiveIfPkts,
       "vRtrIgmpIfRxNonLocal": vRtrIgmpIfRxNonLocal,
       "vRtrIgmpIfRxWrongVersions": vRtrIgmpIfRxWrongVersions,
       "vRtrIgmpIfImportPolicyDrops": vRtrIgmpIfImportPolicyDrops,
       "vRtrIgmpIfRxNoRtrAlertPkts": vRtrIgmpIfRxNoRtrAlertPkts,
       "vRtrIgmpIfRxBadEncodings": vRtrIgmpIfRxBadEncodings,
       "vRtrIgmpIfRxPktDrops": vRtrIgmpIfRxPktDrops,
       "vRtrIgmpIfStatsStarGTypes": vRtrIgmpIfStatsStarGTypes,
       "vRtrIgmpIfStatsSGTypes": vRtrIgmpIfStatsSGTypes,
       "vRtrIgmpIfStatsMcacPolicyDrops": vRtrIgmpIfStatsMcacPolicyDrops,
       "vRtrIgmpIfRxLocalScopePkts": vRtrIgmpIfRxLocalScopePkts,
       "vRtrIgmpIfRxRsvdScopePkts": vRtrIgmpIfRxRsvdScopePkts,
       "vRtrIgmpIfMcacLevelTable": vRtrIgmpIfMcacLevelTable,
       "vRtrIgmpIfMcacLevelEntry": vRtrIgmpIfMcacLevelEntry,
       "vRtrIgmpIfMcacLevelRowStatus": vRtrIgmpIfMcacLevelRowStatus,
       "vRtrIgmpIfMcacLevelBW": vRtrIgmpIfMcacLevelBW,
       "vRtrIgmpIfMcacLagTable": vRtrIgmpIfMcacLagTable,
       "vRtrIgmpIfMcacLagEntry": vRtrIgmpIfMcacLagEntry,
       "vRtrIgmpIfMcacLagRowStatus": vRtrIgmpIfMcacLagRowStatus,
       "vRtrIgmpIfMcacLagLevel": vRtrIgmpIfMcacLagLevel,
       "vRtrIgmpIfSSMTltTableLastChanged": vRtrIgmpIfSSMTltTableLastChanged,
       "vRtrIgmpIfSSMTransTable": vRtrIgmpIfSSMTransTable,
       "vRtrIgmpIfSSMTransEntry": vRtrIgmpIfSSMTransEntry,
       "vRtrIgmpIfSSMTransGrpAddrType1": vRtrIgmpIfSSMTransGrpAddrType1,
       "vRtrIgmpIfSSMTransGrpAddr1": vRtrIgmpIfSSMTransGrpAddr1,
       "vRtrIgmpIfSSMTransGrpAddrType2": vRtrIgmpIfSSMTransGrpAddrType2,
       "vRtrIgmpIfSSMTransGrpAddr2": vRtrIgmpIfSSMTransGrpAddr2,
       "vRtrIgmpIfSSMTransSrcAddrType": vRtrIgmpIfSSMTransSrcAddrType,
       "vRtrIgmpIfSSMTransSrcAddr": vRtrIgmpIfSSMTransSrcAddr,
       "vRtrIgmpIfSSMTransRowStatus": vRtrIgmpIfSSMTransRowStatus,
       "vRtrIgmpRsvpIfTable": vRtrIgmpRsvpIfTable,
       "vRtrIgmpRsvpIfEntry": vRtrIgmpRsvpIfEntry,
       "vRtrIgmpRsvpIfLspName": vRtrIgmpRsvpIfLspName,
       "vRtrIgmpRsvpIfSenderAddrType": vRtrIgmpRsvpIfSenderAddrType,
       "vRtrIgmpRsvpIfSenderAddr": vRtrIgmpRsvpIfSenderAddr,
       "vRtrIgmpRsvpIfRowStatus": vRtrIgmpRsvpIfRowStatus,
       "vRtrIgmpRsvpIfIndex": vRtrIgmpRsvpIfIndex,
       "vRtrIgmpRsvpIfBfdEnable": vRtrIgmpRsvpIfBfdEnable,
       "vRtrIgmpRsvpIfAdminState": vRtrIgmpRsvpIfAdminState,
       "vRtrIgmpRsvpIfOperState": vRtrIgmpRsvpIfOperState,
       "vRtrIgmpLdpIfTableLastChanged": vRtrIgmpLdpIfTableLastChanged,
       "vRtrIgmpLdpIfTable": vRtrIgmpLdpIfTable,
       "vRtrIgmpLdpIfEntry": vRtrIgmpLdpIfEntry,
       "vRtrIgmpLdpP2mpId": vRtrIgmpLdpP2mpId,
       "vRtrIgmpLdpIfSenderAddrType": vRtrIgmpLdpIfSenderAddrType,
       "vRtrIgmpLdpIfSenderAddr": vRtrIgmpLdpIfSenderAddr,
       "vRtrIgmpLdpIfRowStatus": vRtrIgmpLdpIfRowStatus,
       "vRtrIgmpLdpIfLastChanged": vRtrIgmpLdpIfLastChanged,
       "vRtrIgmpLdpIfIndex": vRtrIgmpLdpIfIndex,
       "vRtrIgmpLdpIfAdminState": vRtrIgmpLdpIfAdminState,
       "vRtrIgmpLdpIfOperState": vRtrIgmpLdpIfOperState,
       "vRtrIgmpNotificationObjs": vRtrIgmpNotificationObjs,
       "vRtrIgmpNotifyQueryVersion": vRtrIgmpNotifyQueryVersion,
       "vRtrIgmpNotifyGrpAddrType": vRtrIgmpNotifyGrpAddrType,
       "vRtrIgmpNotifyGrpAddr": vRtrIgmpNotifyGrpAddr,
       "vRtrIgmpNotifyDescription": vRtrIgmpNotifyDescription,
       "vRtrIgmpNotifyMcacPolicyName": vRtrIgmpNotifyMcacPolicyName,
       "vRtrIgmpNotifySrcAddrType": vRtrIgmpNotifySrcAddrType,
       "vRtrIgmpNotifySrcAddr": vRtrIgmpNotifySrcAddr,
       "vRtrIgmpHostObjs": vRtrIgmpHostObjs,
       "vRtrIgmpHostTable": vRtrIgmpHostTable,
       "vRtrIgmpHostEntry": vRtrIgmpHostEntry,
       "vRtrIgmpHostAddress": vRtrIgmpHostAddress,
       "vRtrIgmpHostLastChangeTime": vRtrIgmpHostLastChangeTime,
       "vRtrIgmpHostOperState": vRtrIgmpHostOperState,
       "vRtrIgmpHostOperVersion": vRtrIgmpHostOperVersion,
       "vRtrIgmpHostGroupCount": vRtrIgmpHostGroupCount,
       "vRtrIgmpHostNextGenQueryTime": vRtrIgmpHostNextGenQueryTime,
       "vRtrIgmpHostMaxGroupsTillNow": vRtrIgmpHostMaxGroupsTillNow,
       "vRtrIgmpHostFwdSvcId": vRtrIgmpHostFwdSvcId,
       "vRtrIgmpHostGrpIfId": vRtrIgmpHostGrpIfId,
       "vRtrIgmpHostPppoeSessionId": vRtrIgmpHostPppoeSessionId,
       "vRtrIgmpHostSubscriberId": vRtrIgmpHostSubscriberId,
       "vRtrIgmpHostMacAddress": vRtrIgmpHostMacAddress,
       "vRtrIgmpHostIgmpPolicy": vRtrIgmpHostIgmpPolicy,
       "vRtrIgmpHostMaxGroups": vRtrIgmpHostMaxGroups,
       "vRtrIgmpHostAdminVersion": vRtrIgmpHostAdminVersion,
       "vRtrIgmpHostMaxSources": vRtrIgmpHostMaxSources,
       "vRtrIgmpHostMaxGrpSources": vRtrIgmpHostMaxGrpSources,
       "vRtrIgmpHostStatsTable": vRtrIgmpHostStatsTable,
       "vRtrIgmpHostStatsEntry": vRtrIgmpHostStatsEntry,
       "vRtrIgmpHostTxGenQueries": vRtrIgmpHostTxGenQueries,
       "vRtrIgmpHostTxGrpQueries": vRtrIgmpHostTxGrpQueries,
       "vRtrIgmpHostTxGrpSrcQueries": vRtrIgmpHostTxGrpSrcQueries,
       "vRtrIgmpHostTxV1Reports": vRtrIgmpHostTxV1Reports,
       "vRtrIgmpHostTxV2Reports": vRtrIgmpHostTxV2Reports,
       "vRtrIgmpHostTxV3Reports": vRtrIgmpHostTxV3Reports,
       "vRtrIgmpHostTxLeaves": vRtrIgmpHostTxLeaves,
       "vRtrIgmpHostTxErrors": vRtrIgmpHostTxErrors,
       "vRtrIgmpHostRxGenQueries": vRtrIgmpHostRxGenQueries,
       "vRtrIgmpHostRxGrpQueries": vRtrIgmpHostRxGrpQueries,
       "vRtrIgmpHostRxGrpSrcQueries": vRtrIgmpHostRxGrpSrcQueries,
       "vRtrIgmpHostRxV1Reports": vRtrIgmpHostRxV1Reports,
       "vRtrIgmpHostRxV2Reports": vRtrIgmpHostRxV2Reports,
       "vRtrIgmpHostRxV3Reports": vRtrIgmpHostRxV3Reports,
       "vRtrIgmpHostRxLeaves": vRtrIgmpHostRxLeaves,
       "vRtrIgmpHostRxBadLenPkts": vRtrIgmpHostRxBadLenPkts,
       "vRtrIgmpHostRxBadChecksumPkts": vRtrIgmpHostRxBadChecksumPkts,
       "vRtrIgmpHostRxUnknownTypePkts": vRtrIgmpHostRxUnknownTypePkts,
       "vRtrIgmpHostRxBadReceiveIfPkts": vRtrIgmpHostRxBadReceiveIfPkts,
       "vRtrIgmpHostRxNonLocal": vRtrIgmpHostRxNonLocal,
       "vRtrIgmpHostRxWrongVersions": vRtrIgmpHostRxWrongVersions,
       "vRtrIgmpHostImportPolicyDrops": vRtrIgmpHostImportPolicyDrops,
       "vRtrIgmpHostRxNoRtrAlertPkts": vRtrIgmpHostRxNoRtrAlertPkts,
       "vRtrIgmpHostRxBadEncodings": vRtrIgmpHostRxBadEncodings,
       "vRtrIgmpHostRxPktDrops": vRtrIgmpHostRxPktDrops,
       "vRtrIgmpHostStatsStarGTypes": vRtrIgmpHostStatsStarGTypes,
       "vRtrIgmpHostStatsSGTypes": vRtrIgmpHostStatsSGTypes,
       "vRtrIgmpHostStatsMcacPolicyDrops": vRtrIgmpHostStatsMcacPolicyDrops,
       "vRtrIgmpHostRxLocalScopePkts": vRtrIgmpHostRxLocalScopePkts,
       "vRtrIgmpHostRxRsvdScopePkts": vRtrIgmpHostRxRsvdScopePkts,
       "vRtrIgmpHostRedirectionDrops": vRtrIgmpHostRedirectionDrops,
       "vRtrIgmpGrpIfTable": vRtrIgmpGrpIfTable,
       "vRtrIgmpGrpIfEntry": vRtrIgmpGrpIfEntry,
       "vRtrIfFwdSvcId": vRtrIfFwdSvcId,
       "vRtrIgmpGrpIfRowStatus": vRtrIgmpGrpIfRowStatus,
       "vRtrIgmpGrpIfLastChangeTime": vRtrIgmpGrpIfLastChangeTime,
       "vRtrIgmpGrpIfAdminState": vRtrIgmpGrpIfAdminState,
       "vRtrIgmpGrpIfOperState": vRtrIgmpGrpIfOperState,
       "vRtrIgmpGrpIfSubHostsOnly": vRtrIgmpGrpIfSubHostsOnly,
       "vRtrIgmpGrpIfAdminVersion": vRtrIgmpGrpIfAdminVersion,
       "vRtrIgmpGrpIfImportPolicy": vRtrIgmpGrpIfImportPolicy,
       "vRtrIgmpGrpIfSubnetCheck": vRtrIgmpGrpIfSubnetCheck,
       "vRtrIgmpGrpIfMcacPolicyName": vRtrIgmpGrpIfMcacPolicyName,
       "vRtrIgmpGrpIfMcacUnconstrainedBW": vRtrIgmpGrpIfMcacUnconstrainedBW,
       "vRtrIgmpGrpIfMcacConstAdminState": vRtrIgmpGrpIfMcacConstAdminState,
       "vRtrIgmpGrpIfMcacPreRsvdMandBW": vRtrIgmpGrpIfMcacPreRsvdMandBW,
       "vRtrIgmpGrpIfMcacinUseMandBw": vRtrIgmpGrpIfMcacinUseMandBw,
       "vRtrIgmpGrpIfMcacinUseOpnlBw": vRtrIgmpGrpIfMcacinUseOpnlBw,
       "vRtrIgmpGrpIfMcacAvailMandBw": vRtrIgmpGrpIfMcacAvailMandBw,
       "vRtrIgmpGrpIfMcacAvailOpnlBw": vRtrIgmpGrpIfMcacAvailOpnlBw,
       "vRtrIgmpGrpIfMcacValuesInTransit": vRtrIgmpGrpIfMcacValuesInTransit,
       "vRtrIgmpGrpIfDisRtrAlertChk": vRtrIgmpGrpIfDisRtrAlertChk,
       "vRtrIgmpGrpIfMaxGroups": vRtrIgmpGrpIfMaxGroups,
       "vRtrIgmpGrpIfMaxSources": vRtrIgmpGrpIfMaxSources,
       "vRtrIgmpGrpIfMaxGrpSources": vRtrIgmpGrpIfMaxGrpSources,
       "vRtrIgmpGrpIfQuerySrcIp": vRtrIgmpGrpIfQuerySrcIp,
       "vRtrIgmpGrpIfHostGrpTable": vRtrIgmpGrpIfHostGrpTable,
       "vRtrIgmpGrpIfHostGrpEntry": vRtrIgmpGrpIfHostGrpEntry,
       "vRtrGrpIfIndex": vRtrGrpIfIndex,
       "vRtrIgmpHostGroupAddress": vRtrIgmpHostGroupAddress,
       "vRtrIgmpGrpIfHostGrpType": vRtrIgmpGrpIfHostGrpType,
       "vRtrIgmpGrpIfHostGrpUpTime": vRtrIgmpGrpIfHostGrpUpTime,
       "vRtrIgmpGrpIfHostGrpExpiryTime": vRtrIgmpGrpIfHostGrpExpiryTime,
       "vRtrIgmpGrpIfHostGrpVer1HostTmr": vRtrIgmpGrpIfHostGrpVer1HostTmr,
       "vRtrIgmpGrpIfHostGrpMode": vRtrIgmpGrpIfHostGrpMode,
       "vRtrIgmpGrpIfHostGrpCompatMode": vRtrIgmpGrpIfHostGrpCompatMode,
       "vRtrIgmpGrpIfHostGrpVer2HostTmr": vRtrIgmpGrpIfHostGrpVer2HostTmr,
       "vRtrIgmpGrpIfHostGrpMRDstVrId": vRtrIgmpGrpIfHostGrpMRDstVrId,
       "vRtrIgmpGrpIfHostGrpMRDstIfId": vRtrIgmpGrpIfHostGrpMRDstIfId,
       "vRtrIgmpGrpIfHostGrpSrcTable": vRtrIgmpGrpIfHostGrpSrcTable,
       "vRtrIgmpGrpIfHostGrpSrcEntry": vRtrIgmpGrpIfHostGrpSrcEntry,
       "vRtrIgmpHostGrpSrcAddress": vRtrIgmpHostGrpSrcAddress,
       "vRtrIgmpGrpIfHostGrpSrcExpTime": vRtrIgmpGrpIfHostGrpSrcExpTime,
       "vRtrIgmpGrpIfHostGrpSrcType": vRtrIgmpGrpIfHostGrpSrcType,
       "vRtrIgmpGrpIfHostGrpSrcMRDstVrId": vRtrIgmpGrpIfHostGrpSrcMRDstVrId,
       "vRtrIgmpGrpIfHostGrpSrcMRDstIfId": vRtrIgmpGrpIfHostGrpSrcMRDstIfId,
       "vRtrIgmpGrpSrcHostTable": vRtrIgmpGrpSrcHostTable,
       "vRtrIgmpGrpSrcHostEntry": vRtrIgmpGrpSrcHostEntry,
       "vRtrIgmpGrpSrcHostUpTime": vRtrIgmpGrpSrcHostUpTime,
       "vRtrIgmpHostGrpSrcTable": vRtrIgmpHostGrpSrcTable,
       "vRtrIgmpHostGrpSrcEntry": vRtrIgmpHostGrpSrcEntry,
       "vRtrIgmpHostGrpSrcExpiryTime": vRtrIgmpHostGrpSrcExpiryTime,
       "vRtrIgmpHostGrpSrcType": vRtrIgmpHostGrpSrcType,
       "vRtrIgmpHostGrpSrcMcRdrDstVRtrID": vRtrIgmpHostGrpSrcMcRdrDstVRtrID,
       "vRtrIgmpHostGrpSrcMcRdrDstIfIdx": vRtrIgmpHostGrpSrcMcRdrDstIfIdx,
       "vRtrIgmpHostGrpTable": vRtrIgmpHostGrpTable,
       "vRtrIgmpHostGrpEntry": vRtrIgmpHostGrpEntry,
       "vRtrIgmpHostGrpType": vRtrIgmpHostGrpType,
       "vRtrIgmpHostGrpUpTime": vRtrIgmpHostGrpUpTime,
       "vRtrIgmpHostGrpExpiryTime": vRtrIgmpHostGrpExpiryTime,
       "vRtrIgmpHostGrpVer1HostTmr": vRtrIgmpHostGrpVer1HostTmr,
       "vRtrIgmpHostGrpMode": vRtrIgmpHostGrpMode,
       "vRtrIgmpHostGrpCompatMode": vRtrIgmpHostGrpCompatMode,
       "vRtrIgmpHostGrpVer2HostTmr": vRtrIgmpHostGrpVer2HostTmr,
       "vRtrIgmpHostGrpMcRdrDstVrId": vRtrIgmpHostGrpMcRdrDstVrId,
       "vRtrIgmpHostGrpMcRdrDstIfId": vRtrIgmpHostGrpMcRdrDstIfId,
       "vRtrIgmpGrpIfHostTable": vRtrIgmpGrpIfHostTable,
       "vRtrIgmpGrpIfHostEntry": vRtrIgmpGrpIfHostEntry,
       "vRtrIgmpGrpIfHostLastChangeTime": vRtrIgmpGrpIfHostLastChangeTime,
       "vRtrIgmpGrpIfHostOperState": vRtrIgmpGrpIfHostOperState,
       "vRtrIgmpHostMcRDstStatTable": vRtrIgmpHostMcRDstStatTable,
       "vRtrIgmpHostMcRDstStatEntry": vRtrIgmpHostMcRDstStatEntry,
       "vRtrIgmpHostMcRDstStatType": vRtrIgmpHostMcRDstStatType,
       "vRtrIgmpHostMcRDstStatVal": vRtrIgmpHostMcRDstStatVal,
       "vRtrIgmpGrpIfObjs": vRtrIgmpGrpIfObjs,
       "vRtrIgmpGrpIfSapTable": vRtrIgmpGrpIfSapTable,
       "vRtrIgmpGrpIfSapEntry": vRtrIgmpGrpIfSapEntry,
       "vRtrIgmpGrpIfSapLastChangeTime": vRtrIgmpGrpIfSapLastChangeTime,
       "vRtrIgmpGrpIfSapOperState": vRtrIgmpGrpIfSapOperState,
       "vRtrIgmpGrpIfSapAdminVersion": vRtrIgmpGrpIfSapAdminVersion,
       "vRtrIgmpGrpIfSapOperVersion": vRtrIgmpGrpIfSapOperVersion,
       "vRtrIgmpGrpIfSapGroupCount": vRtrIgmpGrpIfSapGroupCount,
       "vRtrIgmpGrpIfSapNextGenQueryTime": vRtrIgmpGrpIfSapNextGenQueryTime,
       "vRtrIgmpGrpIfSapMaxGroups": vRtrIgmpGrpIfSapMaxGroups,
       "vRtrIgmpGrpIfSapMaxGroupsTillNow": vRtrIgmpGrpIfSapMaxGroupsTillNow,
       "vRtrIgmpGrpIfSapMaxSources": vRtrIgmpGrpIfSapMaxSources,
       "vRtrIgmpGrpIfSapMaxGrpSources": vRtrIgmpGrpIfSapMaxGrpSources,
       "vRtrIgmpGrpIfSapStatsTable": vRtrIgmpGrpIfSapStatsTable,
       "vRtrIgmpGrpIfSapStatsEntry": vRtrIgmpGrpIfSapStatsEntry,
       "vRtrIgmpGrpIfSapTxGenQueries": vRtrIgmpGrpIfSapTxGenQueries,
       "vRtrIgmpGrpIfSapTxGrpQueries": vRtrIgmpGrpIfSapTxGrpQueries,
       "vRtrIgmpGrpIfSapTxGrpSrcQueries": vRtrIgmpGrpIfSapTxGrpSrcQueries,
       "vRtrIgmpGrpIfSapTxV1Reports": vRtrIgmpGrpIfSapTxV1Reports,
       "vRtrIgmpGrpIfSapTxV2Reports": vRtrIgmpGrpIfSapTxV2Reports,
       "vRtrIgmpGrpIfSapTxV3Reports": vRtrIgmpGrpIfSapTxV3Reports,
       "vRtrIgmpGrpIfSapTxLeaves": vRtrIgmpGrpIfSapTxLeaves,
       "vRtrIgmpGrpIfSapTxErrors": vRtrIgmpGrpIfSapTxErrors,
       "vRtrIgmpGrpIfSapRxGenQueries": vRtrIgmpGrpIfSapRxGenQueries,
       "vRtrIgmpGrpIfSapRxGrpQueries": vRtrIgmpGrpIfSapRxGrpQueries,
       "vRtrIgmpGrpIfSapRxGrpSrcQueries": vRtrIgmpGrpIfSapRxGrpSrcQueries,
       "vRtrIgmpGrpIfSapRxV1Reports": vRtrIgmpGrpIfSapRxV1Reports,
       "vRtrIgmpGrpIfSapRxV2Reports": vRtrIgmpGrpIfSapRxV2Reports,
       "vRtrIgmpGrpIfSapRxV3Reports": vRtrIgmpGrpIfSapRxV3Reports,
       "vRtrIgmpGrpIfSapRxLeaves": vRtrIgmpGrpIfSapRxLeaves,
       "vRtrIgmpGrpIfSapRxBadLenPkts": vRtrIgmpGrpIfSapRxBadLenPkts,
       "vRtrIgmpGrpIfSapRxBadChksumPkts": vRtrIgmpGrpIfSapRxBadChksumPkts,
       "vRtrIgmpGrpIfSapRxUnknTypePkts": vRtrIgmpGrpIfSapRxUnknTypePkts,
       "vRtrIgmpGrpIfSapRxBadRecvIfPkts": vRtrIgmpGrpIfSapRxBadRecvIfPkts,
       "vRtrIgmpGrpIfSapRxNonLocal": vRtrIgmpGrpIfSapRxNonLocal,
       "vRtrIgmpGrpIfSapRxWrongVersions": vRtrIgmpGrpIfSapRxWrongVersions,
       "vRtrIgmpGrpIfSapImportPlcyDrops": vRtrIgmpGrpIfSapImportPlcyDrops,
       "vRtrIgmpGrpIfSapRxNoRtrAlertPkts": vRtrIgmpGrpIfSapRxNoRtrAlertPkts,
       "vRtrIgmpGrpIfSapRxBadEncodings": vRtrIgmpGrpIfSapRxBadEncodings,
       "vRtrIgmpGrpIfSapRxPktDrops": vRtrIgmpGrpIfSapRxPktDrops,
       "vRtrIgmpGrpIfSapStatsStarGTypes": vRtrIgmpGrpIfSapStatsStarGTypes,
       "vRtrIgmpGrpIfSapStatsSGTypes": vRtrIgmpGrpIfSapStatsSGTypes,
       "vRtrIgmpGrpIfSapStatsMcacPlcyDrp": vRtrIgmpGrpIfSapStatsMcacPlcyDrp,
       "vRtrIgmpGrpIfSapRxLocalScopePkts": vRtrIgmpGrpIfSapRxLocalScopePkts,
       "vRtrIgmpGrpIfSapRxRsvdScopePkts": vRtrIgmpGrpIfSapRxRsvdScopePkts,
       "vRtrIgmpGrpIfSapGrpTable": vRtrIgmpGrpIfSapGrpTable,
       "vRtrIgmpGrpIfSapGrpEntry": vRtrIgmpGrpIfSapGrpEntry,
       "vRtrIgmpGrpIfSapGroupAddress": vRtrIgmpGrpIfSapGroupAddress,
       "vRtrIgmpGrpIfSapGrpType": vRtrIgmpGrpIfSapGrpType,
       "vRtrIgmpGrpIfSapGrpUpTime": vRtrIgmpGrpIfSapGrpUpTime,
       "vRtrIgmpGrpIfSapGrpExpiryTime": vRtrIgmpGrpIfSapGrpExpiryTime,
       "vRtrIgmpGrpIfSapGrpVer1HostTmr": vRtrIgmpGrpIfSapGrpVer1HostTmr,
       "vRtrIgmpGrpIfSapGrpMode": vRtrIgmpGrpIfSapGrpMode,
       "vRtrIgmpGrpIfSapGrpCompatMode": vRtrIgmpGrpIfSapGrpCompatMode,
       "vRtrIgmpGrpIfSapGrpVer2HostTmr": vRtrIgmpGrpIfSapGrpVer2HostTmr,
       "vRtrIgmpGrpIfSapGrpSrcTable": vRtrIgmpGrpIfSapGrpSrcTable,
       "vRtrIgmpGrpIfSapGrpSrcEntry": vRtrIgmpGrpIfSapGrpSrcEntry,
       "vRtrIgmpGrpIfSapGrpSrcAddress": vRtrIgmpGrpIfSapGrpSrcAddress,
       "vRtrIgmpGrpIfSapGrpSrcExpTime": vRtrIgmpGrpIfSapGrpSrcExpTime,
       "vRtrIgmpGrpIfSapGrpSrcType": vRtrIgmpGrpIfSapGrpSrcType,
       "vRtrIgmpGrpSrcGrpIfSapTable": vRtrIgmpGrpSrcGrpIfSapTable,
       "vRtrIgmpGrpSrcGrpIfSapEntry": vRtrIgmpGrpSrcGrpIfSapEntry,
       "vRtrIgmpGrpSrcGrpIfSapUpTime": vRtrIgmpGrpSrcGrpIfSapUpTime,
       "vRtrIgmpNotifyPrefix": vRtrIgmpNotifyPrefix,
       "vRtrIgmpNotifications": vRtrIgmpNotifications,
       "vRtrIgmpIfRxQueryVerMismatch": vRtrIgmpIfRxQueryVerMismatch,
       "vRtrIgmpIfCModeRxQueryMismatch": vRtrIgmpIfCModeRxQueryMismatch,
       "vRtrIgmpMaxGrpsLimitExceeded": vRtrIgmpMaxGrpsLimitExceeded,
       "vRtrIgmpMcacPlcyDropped": vRtrIgmpMcacPlcyDropped,
       "vRtrIgmpHostInstantiationFail": vRtrIgmpHostInstantiationFail,
       "vRtrIgmpHostMaxGrpsLimitExceeded": vRtrIgmpHostMaxGrpsLimitExceeded,
       "vRtrIgmpHostMcacPlcyDropped": vRtrIgmpHostMcacPlcyDropped,
       "vRtrIgmpHostCModeRxQueryMismatch": vRtrIgmpHostCModeRxQueryMismatch,
       "vRtrIgmpHostRxQueryVerMismatch": vRtrIgmpHostRxQueryVerMismatch,
       "vRtrIgmpHostMaxSrcsLimitExceeded": vRtrIgmpHostMaxSrcsLimitExceeded,
       "vRtrIgmpMaxSrcsLimitExceeded": vRtrIgmpMaxSrcsLimitExceeded,
       "vRtrIgmpGrpIfSapMaxGrpsLimExceed": vRtrIgmpGrpIfSapMaxGrpsLimExceed,
       "vRtrIgmpGrpIfSapMaxSrcsLimExceed": vRtrIgmpGrpIfSapMaxSrcsLimExceed,
       "vRtrIgmpGrpIfSapMcacPlcyDropped": vRtrIgmpGrpIfSapMcacPlcyDropped,
       "vRtrIgmpGrpIfSapCModeRxQueryMism": vRtrIgmpGrpIfSapCModeRxQueryMism,
       "vRtrIgmpGrpIfSapRxQueryVerMism": vRtrIgmpGrpIfSapRxQueryVerMism,
       "vRtrIgmpHostMaxGrpSrcsLimitExcd": vRtrIgmpHostMaxGrpSrcsLimitExcd,
       "vRtrIgmpMaxGrpSrcsLimitExceeded": vRtrIgmpMaxGrpSrcsLimitExceeded,
       "vRtrIgmpGrpIfSapMaxGrpSrcLimExcd": vRtrIgmpGrpIfSapMaxGrpSrcLimExcd}
)
