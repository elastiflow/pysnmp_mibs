# SNMP MIB module (TIMETRA-MLD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_6527/TIMETRA-MLD-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 17:41:47 2025
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
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
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

(vRtrGrpIfIndex,
 vRtrIfFwdSvcId) = mibBuilder.importSymbols(
    "TIMETRA-IGMP-MIB",
    "vRtrGrpIfIndex",
    "vRtrIfFwdSvcId")

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

(TPolicyStatementNameOrEmpty,
 TmnxAdminState,
 TmnxMldGroupFilterMode,
 TmnxMldGroupType,
 TmnxMldVersion,
 TmnxOperState,
 TmnxPppoeSessionId,
 TmnxServId,
 TmnxSubIdentStringOrEmpty,
 TmnxVRtrID) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TPolicyStatementNameOrEmpty",
    "TmnxAdminState",
    "TmnxMldGroupFilterMode",
    "TmnxMldGroupType",
    "TmnxMldVersion",
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

timetraMldMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 46)
)
if mibBuilder.loadTexts:
    timetraMldMIBModule.setRevisions(
        ("2014-01-01 00:00",
         "2008-07-01 00:00",
         "2008-01-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class MldGrpItfOperState(TextualConvention, Integer32):
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
          ("noMldOnGrpItf", 2),
          ("grpItfDown", 3),
          ("inService", 4),
          ("notFwding", 5))
    )



# MIB Managed Objects in the order of their OIDs

_TmnxMldConformance_ObjectIdentity = ObjectIdentity
tmnxMldConformance = _TmnxMldConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 46)
)
_TmnxMldCompliances_ObjectIdentity = ObjectIdentity
tmnxMldCompliances = _TmnxMldCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 46, 1)
)
_TmnxMldGroups_ObjectIdentity = ObjectIdentity
tmnxMldGroups = _TmnxMldGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 46, 2)
)
_TmnxMldObjs_ObjectIdentity = ObjectIdentity
tmnxMldObjs = _TmnxMldObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46)
)
_VRtrMldProtocolObjs_ObjectIdentity = ObjectIdentity
vRtrMldProtocolObjs = _VRtrMldProtocolObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 1)
)
_VRtrMldGeneralTableLastChanged_Type = TimeStamp
_VRtrMldGeneralTableLastChanged_Object = MibScalar
vRtrMldGeneralTableLastChanged = _VRtrMldGeneralTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 1, 1),
    _VRtrMldGeneralTableLastChanged_Type()
)
vRtrMldGeneralTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldGeneralTableLastChanged.setStatus("current")
_VRtrMldGeneralTable_Object = MibTable
vRtrMldGeneralTable = _VRtrMldGeneralTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 1, 2)
)
if mibBuilder.loadTexts:
    vRtrMldGeneralTable.setStatus("current")
_VRtrMldGeneralEntry_Object = MibTableRow
vRtrMldGeneralEntry = _VRtrMldGeneralEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 1, 2, 1)
)
vRtrMldGeneralEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
)
if mibBuilder.loadTexts:
    vRtrMldGeneralEntry.setStatus("current")


class _VRtrMldGenQueryInterval_Type(Unsigned32):
    """Custom type vRtrMldGenQueryInterval based on Unsigned32"""
    defaultValue = 125

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 1024),
    )


_VRtrMldGenQueryInterval_Type.__name__ = "Unsigned32"
_VRtrMldGenQueryInterval_Object = MibTableColumn
vRtrMldGenQueryInterval = _VRtrMldGenQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 1, 2, 1, 1),
    _VRtrMldGenQueryInterval_Type()
)
vRtrMldGenQueryInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMldGenQueryInterval.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMldGenQueryInterval.setUnits("seconds")


class _VRtrMldGenLastMembQueryIntvl_Type(Unsigned32):
    """Custom type vRtrMldGenLastMembQueryIntvl based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_VRtrMldGenLastMembQueryIntvl_Type.__name__ = "Unsigned32"
_VRtrMldGenLastMembQueryIntvl_Object = MibTableColumn
vRtrMldGenLastMembQueryIntvl = _VRtrMldGenLastMembQueryIntvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 1, 2, 1, 2),
    _VRtrMldGenLastMembQueryIntvl_Type()
)
vRtrMldGenLastMembQueryIntvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMldGenLastMembQueryIntvl.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMldGenLastMembQueryIntvl.setUnits("seconds")


class _VRtrMldGenQueryResponseIntvl_Type(Unsigned32):
    """Custom type vRtrMldGenQueryResponseIntvl based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_VRtrMldGenQueryResponseIntvl_Type.__name__ = "Unsigned32"
_VRtrMldGenQueryResponseIntvl_Object = MibTableColumn
vRtrMldGenQueryResponseIntvl = _VRtrMldGenQueryResponseIntvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 1, 2, 1, 3),
    _VRtrMldGenQueryResponseIntvl_Type()
)
vRtrMldGenQueryResponseIntvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMldGenQueryResponseIntvl.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMldGenQueryResponseIntvl.setUnits("seconds")


class _VRtrMldGenRobustCount_Type(Unsigned32):
    """Custom type vRtrMldGenRobustCount based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_VRtrMldGenRobustCount_Type.__name__ = "Unsigned32"
_VRtrMldGenRobustCount_Object = MibTableColumn
vRtrMldGenRobustCount = _VRtrMldGenRobustCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 1, 2, 1, 4),
    _VRtrMldGenRobustCount_Type()
)
vRtrMldGenRobustCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMldGenRobustCount.setStatus("current")
_VRtrMldGenLastChange_Type = TimeStamp
_VRtrMldGenLastChange_Object = MibTableColumn
vRtrMldGenLastChange = _VRtrMldGenLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 1, 2, 1, 5),
    _VRtrMldGenLastChange_Type()
)
vRtrMldGenLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldGenLastChange.setStatus("current")


class _VRtrMldGenAdminState_Type(TmnxAdminState):
    """Custom type vRtrMldGenAdminState based on TmnxAdminState"""
    defaultValue = 3


_VRtrMldGenAdminState_Type.__name__ = "TmnxAdminState"
_VRtrMldGenAdminState_Object = MibTableColumn
vRtrMldGenAdminState = _VRtrMldGenAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 1, 2, 1, 6),
    _VRtrMldGenAdminState_Type()
)
vRtrMldGenAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMldGenAdminState.setStatus("current")
_VRtrMldGenOperState_Type = TmnxOperState
_VRtrMldGenOperState_Object = MibTableColumn
vRtrMldGenOperState = _VRtrMldGenOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 1, 2, 1, 7),
    _VRtrMldGenOperState_Type()
)
vRtrMldGenOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldGenOperState.setStatus("current")
_VRtrMldGenGrpIfQrySrcIpAddrType_Type = InetAddressType
_VRtrMldGenGrpIfQrySrcIpAddrType_Object = MibTableColumn
vRtrMldGenGrpIfQrySrcIpAddrType = _VRtrMldGenGrpIfQrySrcIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 1, 2, 1, 8),
    _VRtrMldGenGrpIfQrySrcIpAddrType_Type()
)
vRtrMldGenGrpIfQrySrcIpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMldGenGrpIfQrySrcIpAddrType.setStatus("current")


class _VRtrMldGenGrpIfQrySrcIpAddr_Type(InetAddress):
    """Custom type vRtrMldGenGrpIfQrySrcIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_VRtrMldGenGrpIfQrySrcIpAddr_Type.__name__ = "InetAddress"
_VRtrMldGenGrpIfQrySrcIpAddr_Object = MibTableColumn
vRtrMldGenGrpIfQrySrcIpAddr = _VRtrMldGenGrpIfQrySrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 1, 2, 1, 9),
    _VRtrMldGenGrpIfQrySrcIpAddr_Type()
)
vRtrMldGenGrpIfQrySrcIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMldGenGrpIfQrySrcIpAddr.setStatus("current")
_VRtrMldGrpSrcTable_Object = MibTable
vRtrMldGrpSrcTable = _VRtrMldGrpSrcTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 1, 3)
)
if mibBuilder.loadTexts:
    vRtrMldGrpSrcTable.setStatus("current")
_VRtrMldGrpSrcEntry_Object = MibTableRow
vRtrMldGrpSrcEntry = _VRtrMldGrpSrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 1, 3, 1)
)
vRtrMldGrpSrcEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MLD-MIB", "vRtrMldGrpSrcGroupAddrType"),
    (0, "TIMETRA-MLD-MIB", "vRtrMldGrpSrcGroupAddress"),
    (0, "TIMETRA-MLD-MIB", "vRtrMldGrpSrcSourceAddrType"),
    (0, "TIMETRA-MLD-MIB", "vRtrMldGrpSrcSourceAddress"),
    (0, "TIMETRA-MLD-MIB", "vRtrMldGrpSrcFwdOrBlk"),
    (0, "TIMETRA-VRTR-MIB", "vRtrIfIndex"),
)
if mibBuilder.loadTexts:
    vRtrMldGrpSrcEntry.setStatus("current")
_VRtrMldGrpSrcGroupAddrType_Type = InetAddressType
_VRtrMldGrpSrcGroupAddrType_Object = MibTableColumn
vRtrMldGrpSrcGroupAddrType = _VRtrMldGrpSrcGroupAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 1, 3, 1, 1),
    _VRtrMldGrpSrcGroupAddrType_Type()
)
vRtrMldGrpSrcGroupAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMldGrpSrcGroupAddrType.setStatus("current")


class _VRtrMldGrpSrcGroupAddress_Type(InetAddress):
    """Custom type vRtrMldGrpSrcGroupAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_VRtrMldGrpSrcGroupAddress_Type.__name__ = "InetAddress"
_VRtrMldGrpSrcGroupAddress_Object = MibTableColumn
vRtrMldGrpSrcGroupAddress = _VRtrMldGrpSrcGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 1, 3, 1, 2),
    _VRtrMldGrpSrcGroupAddress_Type()
)
vRtrMldGrpSrcGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMldGrpSrcGroupAddress.setStatus("current")
_VRtrMldGrpSrcSourceAddrType_Type = InetAddressType
_VRtrMldGrpSrcSourceAddrType_Object = MibTableColumn
vRtrMldGrpSrcSourceAddrType = _VRtrMldGrpSrcSourceAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 1, 3, 1, 3),
    _VRtrMldGrpSrcSourceAddrType_Type()
)
vRtrMldGrpSrcSourceAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMldGrpSrcSourceAddrType.setStatus("current")


class _VRtrMldGrpSrcSourceAddress_Type(InetAddress):
    """Custom type vRtrMldGrpSrcSourceAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_VRtrMldGrpSrcSourceAddress_Type.__name__ = "InetAddress"
_VRtrMldGrpSrcSourceAddress_Object = MibTableColumn
vRtrMldGrpSrcSourceAddress = _VRtrMldGrpSrcSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 1, 3, 1, 4),
    _VRtrMldGrpSrcSourceAddress_Type()
)
vRtrMldGrpSrcSourceAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMldGrpSrcSourceAddress.setStatus("current")


class _VRtrMldGrpSrcFwdOrBlk_Type(Integer32):
    """Custom type vRtrMldGrpSrcFwdOrBlk based on Integer32"""
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


_VRtrMldGrpSrcFwdOrBlk_Type.__name__ = "Integer32"
_VRtrMldGrpSrcFwdOrBlk_Object = MibTableColumn
vRtrMldGrpSrcFwdOrBlk = _VRtrMldGrpSrcFwdOrBlk_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 1, 3, 1, 5),
    _VRtrMldGrpSrcFwdOrBlk_Type()
)
vRtrMldGrpSrcFwdOrBlk.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMldGrpSrcFwdOrBlk.setStatus("current")
_VRtrMldGrpSrcUpTime_Type = Unsigned32
_VRtrMldGrpSrcUpTime_Object = MibTableColumn
vRtrMldGrpSrcUpTime = _VRtrMldGrpSrcUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 1, 3, 1, 6),
    _VRtrMldGrpSrcUpTime_Type()
)
vRtrMldGrpSrcUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldGrpSrcUpTime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMldGrpSrcUpTime.setUnits("seconds")
_VRtrMldSsmTransTableLastChanged_Type = TimeStamp
_VRtrMldSsmTransTableLastChanged_Object = MibScalar
vRtrMldSsmTransTableLastChanged = _VRtrMldSsmTransTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 1, 4),
    _VRtrMldSsmTransTableLastChanged_Type()
)
vRtrMldSsmTransTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldSsmTransTableLastChanged.setStatus("current")
_VRtrMldSsmTransTable_Object = MibTable
vRtrMldSsmTransTable = _VRtrMldSsmTransTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 1, 5)
)
if mibBuilder.loadTexts:
    vRtrMldSsmTransTable.setStatus("current")
_VRtrMldSsmTransEntry_Object = MibTableRow
vRtrMldSsmTransEntry = _VRtrMldSsmTransEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 1, 5, 1)
)
vRtrMldSsmTransEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MLD-MIB", "vRtrMldSsmTransGrpAddrType1"),
    (0, "TIMETRA-MLD-MIB", "vRtrMldSsmTransGrpAddr1"),
    (0, "TIMETRA-MLD-MIB", "vRtrMldSsmTransGrpAddrType2"),
    (0, "TIMETRA-MLD-MIB", "vRtrMldSsmTransGrpAddr2"),
    (0, "TIMETRA-MLD-MIB", "vRtrMldSsmTransSrcAddrType"),
    (0, "TIMETRA-MLD-MIB", "vRtrMldSsmTransSrcAddr"),
)
if mibBuilder.loadTexts:
    vRtrMldSsmTransEntry.setStatus("current")
_VRtrMldSsmTransGrpAddrType1_Type = InetAddressType
_VRtrMldSsmTransGrpAddrType1_Object = MibTableColumn
vRtrMldSsmTransGrpAddrType1 = _VRtrMldSsmTransGrpAddrType1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 1, 5, 1, 1),
    _VRtrMldSsmTransGrpAddrType1_Type()
)
vRtrMldSsmTransGrpAddrType1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMldSsmTransGrpAddrType1.setStatus("current")


class _VRtrMldSsmTransGrpAddr1_Type(InetAddress):
    """Custom type vRtrMldSsmTransGrpAddr1 based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_VRtrMldSsmTransGrpAddr1_Type.__name__ = "InetAddress"
_VRtrMldSsmTransGrpAddr1_Object = MibTableColumn
vRtrMldSsmTransGrpAddr1 = _VRtrMldSsmTransGrpAddr1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 1, 5, 1, 2),
    _VRtrMldSsmTransGrpAddr1_Type()
)
vRtrMldSsmTransGrpAddr1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMldSsmTransGrpAddr1.setStatus("current")
_VRtrMldSsmTransGrpAddrType2_Type = InetAddressType
_VRtrMldSsmTransGrpAddrType2_Object = MibTableColumn
vRtrMldSsmTransGrpAddrType2 = _VRtrMldSsmTransGrpAddrType2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 1, 5, 1, 3),
    _VRtrMldSsmTransGrpAddrType2_Type()
)
vRtrMldSsmTransGrpAddrType2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMldSsmTransGrpAddrType2.setStatus("current")


class _VRtrMldSsmTransGrpAddr2_Type(InetAddress):
    """Custom type vRtrMldSsmTransGrpAddr2 based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_VRtrMldSsmTransGrpAddr2_Type.__name__ = "InetAddress"
_VRtrMldSsmTransGrpAddr2_Object = MibTableColumn
vRtrMldSsmTransGrpAddr2 = _VRtrMldSsmTransGrpAddr2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 1, 5, 1, 4),
    _VRtrMldSsmTransGrpAddr2_Type()
)
vRtrMldSsmTransGrpAddr2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMldSsmTransGrpAddr2.setStatus("current")
_VRtrMldSsmTransSrcAddrType_Type = InetAddressType
_VRtrMldSsmTransSrcAddrType_Object = MibTableColumn
vRtrMldSsmTransSrcAddrType = _VRtrMldSsmTransSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 1, 5, 1, 5),
    _VRtrMldSsmTransSrcAddrType_Type()
)
vRtrMldSsmTransSrcAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMldSsmTransSrcAddrType.setStatus("current")


class _VRtrMldSsmTransSrcAddr_Type(InetAddress):
    """Custom type vRtrMldSsmTransSrcAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_VRtrMldSsmTransSrcAddr_Type.__name__ = "InetAddress"
_VRtrMldSsmTransSrcAddr_Object = MibTableColumn
vRtrMldSsmTransSrcAddr = _VRtrMldSsmTransSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 1, 5, 1, 6),
    _VRtrMldSsmTransSrcAddr_Type()
)
vRtrMldSsmTransSrcAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMldSsmTransSrcAddr.setStatus("current")
_VRtrMldSsmTransRowStatus_Type = RowStatus
_VRtrMldSsmTransRowStatus_Object = MibTableColumn
vRtrMldSsmTransRowStatus = _VRtrMldSsmTransRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 1, 5, 1, 7),
    _VRtrMldSsmTransRowStatus_Type()
)
vRtrMldSsmTransRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMldSsmTransRowStatus.setStatus("current")
_VRtrMldSsmTransLastChanged_Type = TimeStamp
_VRtrMldSsmTransLastChanged_Object = MibTableColumn
vRtrMldSsmTransLastChanged = _VRtrMldSsmTransLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 1, 5, 1, 8),
    _VRtrMldSsmTransLastChanged_Type()
)
vRtrMldSsmTransLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldSsmTransLastChanged.setStatus("current")
_VRtrMldGenStatsTable_Object = MibTable
vRtrMldGenStatsTable = _VRtrMldGenStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 1, 6)
)
if mibBuilder.loadTexts:
    vRtrMldGenStatsTable.setStatus("current")
_VRtrMldGenStatsEntry_Object = MibTableRow
vRtrMldGenStatsEntry = _VRtrMldGenStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 1, 6, 1)
)
if mibBuilder.loadTexts:
    vRtrMldGenStatsEntry.setStatus("current")
_VRtrMldGenStatsStarGTypes_Type = Gauge32
_VRtrMldGenStatsStarGTypes_Object = MibTableColumn
vRtrMldGenStatsStarGTypes = _VRtrMldGenStatsStarGTypes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 1, 6, 1, 1),
    _VRtrMldGenStatsStarGTypes_Type()
)
vRtrMldGenStatsStarGTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldGenStatsStarGTypes.setStatus("current")
_VRtrMldGenStatsSGTypes_Type = Gauge32
_VRtrMldGenStatsSGTypes_Object = MibTableColumn
vRtrMldGenStatsSGTypes = _VRtrMldGenStatsSGTypes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 1, 6, 1, 2),
    _VRtrMldGenStatsSGTypes_Type()
)
vRtrMldGenStatsSGTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldGenStatsSGTypes.setStatus("current")
_VRtrMldGrpSrcSummaryTable_Object = MibTable
vRtrMldGrpSrcSummaryTable = _VRtrMldGrpSrcSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 1, 7)
)
if mibBuilder.loadTexts:
    vRtrMldGrpSrcSummaryTable.setStatus("current")
_VRtrMldGrpSrcSummaryEntry_Object = MibTableRow
vRtrMldGrpSrcSummaryEntry = _VRtrMldGrpSrcSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 1, 7, 1)
)
vRtrMldGrpSrcSummaryEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MLD-MIB", "vRtrMldGrpSrcGroupAddrType"),
    (0, "TIMETRA-MLD-MIB", "vRtrMldGrpSrcGroupAddress"),
    (0, "TIMETRA-MLD-MIB", "vRtrMldGrpSrcSourceAddrType"),
    (0, "TIMETRA-MLD-MIB", "vRtrMldGrpSrcSourceAddress"),
)
if mibBuilder.loadTexts:
    vRtrMldGrpSrcSummaryEntry.setStatus("current")
_VRtrMldGrpSrcSummFwdInterfaces_Type = Gauge32
_VRtrMldGrpSrcSummFwdInterfaces_Object = MibTableColumn
vRtrMldGrpSrcSummFwdInterfaces = _VRtrMldGrpSrcSummFwdInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 1, 7, 1, 1),
    _VRtrMldGrpSrcSummFwdInterfaces_Type()
)
vRtrMldGrpSrcSummFwdInterfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldGrpSrcSummFwdInterfaces.setStatus("current")
_VRtrMldGrpSrcSummBlkInterfaces_Type = Gauge32
_VRtrMldGrpSrcSummBlkInterfaces_Object = MibTableColumn
vRtrMldGrpSrcSummBlkInterfaces = _VRtrMldGrpSrcSummBlkInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 1, 7, 1, 2),
    _VRtrMldGrpSrcSummBlkInterfaces_Type()
)
vRtrMldGrpSrcSummBlkInterfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldGrpSrcSummBlkInterfaces.setStatus("current")
_VRtrMldGrpSrcSummFwdHosts_Type = Gauge32
_VRtrMldGrpSrcSummFwdHosts_Object = MibTableColumn
vRtrMldGrpSrcSummFwdHosts = _VRtrMldGrpSrcSummFwdHosts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 1, 7, 1, 3),
    _VRtrMldGrpSrcSummFwdHosts_Type()
)
vRtrMldGrpSrcSummFwdHosts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldGrpSrcSummFwdHosts.setStatus("current")
_VRtrMldGrpSrcSummBlkHosts_Type = Gauge32
_VRtrMldGrpSrcSummBlkHosts_Object = MibTableColumn
vRtrMldGrpSrcSummBlkHosts = _VRtrMldGrpSrcSummBlkHosts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 1, 7, 1, 4),
    _VRtrMldGrpSrcSummBlkHosts_Type()
)
vRtrMldGrpSrcSummBlkHosts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldGrpSrcSummBlkHosts.setStatus("current")
_VRtrMldGrpSrcSummFwdGrpIfSaps_Type = Gauge32
_VRtrMldGrpSrcSummFwdGrpIfSaps_Object = MibTableColumn
vRtrMldGrpSrcSummFwdGrpIfSaps = _VRtrMldGrpSrcSummFwdGrpIfSaps_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 1, 7, 1, 5),
    _VRtrMldGrpSrcSummFwdGrpIfSaps_Type()
)
vRtrMldGrpSrcSummFwdGrpIfSaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldGrpSrcSummFwdGrpIfSaps.setStatus("current")
_VRtrMldGrpSrcSummBlkGrpIfSaps_Type = Gauge32
_VRtrMldGrpSrcSummBlkGrpIfSaps_Object = MibTableColumn
vRtrMldGrpSrcSummBlkGrpIfSaps = _VRtrMldGrpSrcSummBlkGrpIfSaps_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 1, 7, 1, 6),
    _VRtrMldGrpSrcSummBlkGrpIfSaps_Type()
)
vRtrMldGrpSrcSummBlkGrpIfSaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldGrpSrcSummBlkGrpIfSaps.setStatus("current")
_VRtrMldIfObjs_ObjectIdentity = ObjectIdentity
vRtrMldIfObjs = _VRtrMldIfObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2)
)
_VRtrMldIfTableLastChanged_Type = TimeStamp
_VRtrMldIfTableLastChanged_Object = MibScalar
vRtrMldIfTableLastChanged = _VRtrMldIfTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 1),
    _VRtrMldIfTableLastChanged_Type()
)
vRtrMldIfTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldIfTableLastChanged.setStatus("current")
_VRtrMldIfTable_Object = MibTable
vRtrMldIfTable = _VRtrMldIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 2)
)
if mibBuilder.loadTexts:
    vRtrMldIfTable.setStatus("current")
_VRtrMldIfEntry_Object = MibTableRow
vRtrMldIfEntry = _VRtrMldIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 2, 1)
)
vRtrMldIfEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-VRTR-MIB", "vRtrIfIndex"),
)
if mibBuilder.loadTexts:
    vRtrMldIfEntry.setStatus("current")
_VRtrMldIfRowStatus_Type = RowStatus
_VRtrMldIfRowStatus_Object = MibTableColumn
vRtrMldIfRowStatus = _VRtrMldIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 2, 1, 1),
    _VRtrMldIfRowStatus_Type()
)
vRtrMldIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMldIfRowStatus.setStatus("current")
_VRtrMldIfLastChanged_Type = TimeStamp
_VRtrMldIfLastChanged_Object = MibTableColumn
vRtrMldIfLastChanged = _VRtrMldIfLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 2, 1, 2),
    _VRtrMldIfLastChanged_Type()
)
vRtrMldIfLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldIfLastChanged.setStatus("current")


class _VRtrMldIfAdminState_Type(TmnxAdminState):
    """Custom type vRtrMldIfAdminState based on TmnxAdminState"""
    defaultValue = 2


_VRtrMldIfAdminState_Type.__name__ = "TmnxAdminState"
_VRtrMldIfAdminState_Object = MibTableColumn
vRtrMldIfAdminState = _VRtrMldIfAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 2, 1, 3),
    _VRtrMldIfAdminState_Type()
)
vRtrMldIfAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMldIfAdminState.setStatus("current")
_VRtrMldIfOperState_Type = TmnxOperState
_VRtrMldIfOperState_Object = MibTableColumn
vRtrMldIfOperState = _VRtrMldIfOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 2, 1, 4),
    _VRtrMldIfOperState_Type()
)
vRtrMldIfOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldIfOperState.setStatus("current")


class _VRtrMldIfAdminVersion_Type(TmnxMldVersion):
    """Custom type vRtrMldIfAdminVersion based on TmnxMldVersion"""
    defaultValue = 2


_VRtrMldIfAdminVersion_Type.__name__ = "TmnxMldVersion"
_VRtrMldIfAdminVersion_Object = MibTableColumn
vRtrMldIfAdminVersion = _VRtrMldIfAdminVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 2, 1, 5),
    _VRtrMldIfAdminVersion_Type()
)
vRtrMldIfAdminVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMldIfAdminVersion.setStatus("current")
_VRtrMldIfOperVersion_Type = TmnxMldVersion
_VRtrMldIfOperVersion_Object = MibTableColumn
vRtrMldIfOperVersion = _VRtrMldIfOperVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 2, 1, 6),
    _VRtrMldIfOperVersion_Type()
)
vRtrMldIfOperVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldIfOperVersion.setStatus("current")
_VRtrMldIfQuerierType_Type = InetAddressType
_VRtrMldIfQuerierType_Object = MibTableColumn
vRtrMldIfQuerierType = _VRtrMldIfQuerierType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 2, 1, 7),
    _VRtrMldIfQuerierType_Type()
)
vRtrMldIfQuerierType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldIfQuerierType.setStatus("current")


class _VRtrMldIfQuerier_Type(InetAddress):
    """Custom type vRtrMldIfQuerier based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_VRtrMldIfQuerier_Type.__name__ = "InetAddress"
_VRtrMldIfQuerier_Object = MibTableColumn
vRtrMldIfQuerier = _VRtrMldIfQuerier_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 2, 1, 8),
    _VRtrMldIfQuerier_Type()
)
vRtrMldIfQuerier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldIfQuerier.setStatus("current")


class _VRtrMldIfImportPolicy_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrMldIfImportPolicy based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrMldIfImportPolicy_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrMldIfImportPolicy_Object = MibTableColumn
vRtrMldIfImportPolicy = _VRtrMldIfImportPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 2, 1, 9),
    _VRtrMldIfImportPolicy_Type()
)
vRtrMldIfImportPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMldIfImportPolicy.setStatus("current")
_VRtrMldIfGroupCount_Type = Gauge32
_VRtrMldIfGroupCount_Object = MibTableColumn
vRtrMldIfGroupCount = _VRtrMldIfGroupCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 2, 1, 10),
    _VRtrMldIfGroupCount_Type()
)
vRtrMldIfGroupCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldIfGroupCount.setStatus("current")
_VRtrMldIfQuerierUpTime_Type = Unsigned32
_VRtrMldIfQuerierUpTime_Object = MibTableColumn
vRtrMldIfQuerierUpTime = _VRtrMldIfQuerierUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 2, 1, 11),
    _VRtrMldIfQuerierUpTime_Type()
)
vRtrMldIfQuerierUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldIfQuerierUpTime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMldIfQuerierUpTime.setUnits("seconds")
_VRtrMldIfQuerierExpiryTime_Type = Unsigned32
_VRtrMldIfQuerierExpiryTime_Object = MibTableColumn
vRtrMldIfQuerierExpiryTime = _VRtrMldIfQuerierExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 2, 1, 12),
    _VRtrMldIfQuerierExpiryTime_Type()
)
vRtrMldIfQuerierExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldIfQuerierExpiryTime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMldIfQuerierExpiryTime.setUnits("seconds")
_VRtrMldIfNextGenQueryTime_Type = Unsigned32
_VRtrMldIfNextGenQueryTime_Object = MibTableColumn
vRtrMldIfNextGenQueryTime = _VRtrMldIfNextGenQueryTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 2, 1, 13),
    _VRtrMldIfNextGenQueryTime_Type()
)
vRtrMldIfNextGenQueryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldIfNextGenQueryTime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMldIfNextGenQueryTime.setUnits("seconds")


class _VRtrMldIfMaxGroups_Type(Unsigned32):
    """Custom type vRtrMldIfMaxGroups based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 16000),
    )


_VRtrMldIfMaxGroups_Type.__name__ = "Unsigned32"
_VRtrMldIfMaxGroups_Object = MibTableColumn
vRtrMldIfMaxGroups = _VRtrMldIfMaxGroups_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 2, 1, 14),
    _VRtrMldIfMaxGroups_Type()
)
vRtrMldIfMaxGroups.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMldIfMaxGroups.setStatus("current")
_VRtrMldIfMaxGroupsTillNow_Type = Counter32
_VRtrMldIfMaxGroupsTillNow_Object = MibTableColumn
vRtrMldIfMaxGroupsTillNow = _VRtrMldIfMaxGroupsTillNow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 2, 1, 15),
    _VRtrMldIfMaxGroupsTillNow_Type()
)
vRtrMldIfMaxGroupsTillNow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldIfMaxGroupsTillNow.setStatus("current")


class _VRtrMldIfQueryInterval_Type(Unsigned32):
    """Custom type vRtrMldIfQueryInterval based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2, 1024),
    )


_VRtrMldIfQueryInterval_Type.__name__ = "Unsigned32"
_VRtrMldIfQueryInterval_Object = MibTableColumn
vRtrMldIfQueryInterval = _VRtrMldIfQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 2, 1, 16),
    _VRtrMldIfQueryInterval_Type()
)
vRtrMldIfQueryInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMldIfQueryInterval.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMldIfQueryInterval.setUnits("seconds")


class _VRtrMldIfLastMembQueryIntvl_Type(Unsigned32):
    """Custom type vRtrMldIfLastMembQueryIntvl based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1023),
    )


_VRtrMldIfLastMembQueryIntvl_Type.__name__ = "Unsigned32"
_VRtrMldIfLastMembQueryIntvl_Object = MibTableColumn
vRtrMldIfLastMembQueryIntvl = _VRtrMldIfLastMembQueryIntvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 2, 1, 17),
    _VRtrMldIfLastMembQueryIntvl_Type()
)
vRtrMldIfLastMembQueryIntvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMldIfLastMembQueryIntvl.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMldIfLastMembQueryIntvl.setUnits("seconds")


class _VRtrMldIfQueryResponseIntvl_Type(Unsigned32):
    """Custom type vRtrMldIfQueryResponseIntvl based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1023),
    )


_VRtrMldIfQueryResponseIntvl_Type.__name__ = "Unsigned32"
_VRtrMldIfQueryResponseIntvl_Object = MibTableColumn
vRtrMldIfQueryResponseIntvl = _VRtrMldIfQueryResponseIntvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 2, 1, 18),
    _VRtrMldIfQueryResponseIntvl_Type()
)
vRtrMldIfQueryResponseIntvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMldIfQueryResponseIntvl.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMldIfQueryResponseIntvl.setUnits("seconds")


class _VRtrMldIfDisRtrAlertChk_Type(TruthValue):
    """Custom type vRtrMldIfDisRtrAlertChk based on TruthValue"""
    defaultValue = 2


_VRtrMldIfDisRtrAlertChk_Type.__name__ = "TruthValue"
_VRtrMldIfDisRtrAlertChk_Object = MibTableColumn
vRtrMldIfDisRtrAlertChk = _VRtrMldIfDisRtrAlertChk_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 2, 1, 19),
    _VRtrMldIfDisRtrAlertChk_Type()
)
vRtrMldIfDisRtrAlertChk.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMldIfDisRtrAlertChk.setStatus("current")


class _VRtrMldIfMcacPolicyName_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrMldIfMcacPolicyName based on TPolicyStatementNameOrEmpty"""
    defaultValue = OctetString("")


_VRtrMldIfMcacPolicyName_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrMldIfMcacPolicyName_Object = MibTableColumn
vRtrMldIfMcacPolicyName = _VRtrMldIfMcacPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 2, 1, 20),
    _VRtrMldIfMcacPolicyName_Type()
)
vRtrMldIfMcacPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMldIfMcacPolicyName.setStatus("current")


class _VRtrMldIfMcacUnconstrainedBW_Type(Integer32):
    """Custom type vRtrMldIfMcacUnconstrainedBW based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_VRtrMldIfMcacUnconstrainedBW_Type.__name__ = "Integer32"
_VRtrMldIfMcacUnconstrainedBW_Object = MibTableColumn
vRtrMldIfMcacUnconstrainedBW = _VRtrMldIfMcacUnconstrainedBW_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 2, 1, 21),
    _VRtrMldIfMcacUnconstrainedBW_Type()
)
vRtrMldIfMcacUnconstrainedBW.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMldIfMcacUnconstrainedBW.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMldIfMcacUnconstrainedBW.setUnits("kbps")


class _VRtrMldIfMcacConstAdminState_Type(TmnxAdminState):
    """Custom type vRtrMldIfMcacConstAdminState based on TmnxAdminState"""
    defaultValue = 2


_VRtrMldIfMcacConstAdminState_Type.__name__ = "TmnxAdminState"
_VRtrMldIfMcacConstAdminState_Object = MibTableColumn
vRtrMldIfMcacConstAdminState = _VRtrMldIfMcacConstAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 2, 1, 22),
    _VRtrMldIfMcacConstAdminState_Type()
)
vRtrMldIfMcacConstAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMldIfMcacConstAdminState.setStatus("current")


class _VRtrMldIfMcacPreRsvdMandBW_Type(Integer32):
    """Custom type vRtrMldIfMcacPreRsvdMandBW based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_VRtrMldIfMcacPreRsvdMandBW_Type.__name__ = "Integer32"
_VRtrMldIfMcacPreRsvdMandBW_Object = MibTableColumn
vRtrMldIfMcacPreRsvdMandBW = _VRtrMldIfMcacPreRsvdMandBW_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 2, 1, 23),
    _VRtrMldIfMcacPreRsvdMandBW_Type()
)
vRtrMldIfMcacPreRsvdMandBW.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMldIfMcacPreRsvdMandBW.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMldIfMcacPreRsvdMandBW.setUnits("kbps")
_VRtrMldIfMcacinUseMandBw_Type = Unsigned32
_VRtrMldIfMcacinUseMandBw_Object = MibTableColumn
vRtrMldIfMcacinUseMandBw = _VRtrMldIfMcacinUseMandBw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 2, 1, 24),
    _VRtrMldIfMcacinUseMandBw_Type()
)
vRtrMldIfMcacinUseMandBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldIfMcacinUseMandBw.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMldIfMcacinUseMandBw.setUnits("kbps")
_VRtrMldIfMcacinUseOpnlBw_Type = Unsigned32
_VRtrMldIfMcacinUseOpnlBw_Object = MibTableColumn
vRtrMldIfMcacinUseOpnlBw = _VRtrMldIfMcacinUseOpnlBw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 2, 1, 25),
    _VRtrMldIfMcacinUseOpnlBw_Type()
)
vRtrMldIfMcacinUseOpnlBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldIfMcacinUseOpnlBw.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMldIfMcacinUseOpnlBw.setUnits("kbps")
_VRtrMldIfMcacAvailMandBw_Type = Unsigned32
_VRtrMldIfMcacAvailMandBw_Object = MibTableColumn
vRtrMldIfMcacAvailMandBw = _VRtrMldIfMcacAvailMandBw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 2, 1, 26),
    _VRtrMldIfMcacAvailMandBw_Type()
)
vRtrMldIfMcacAvailMandBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldIfMcacAvailMandBw.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMldIfMcacAvailMandBw.setUnits("kbps")
_VRtrMldIfMcacAvailOpnlBw_Type = Unsigned32
_VRtrMldIfMcacAvailOpnlBw_Object = MibTableColumn
vRtrMldIfMcacAvailOpnlBw = _VRtrMldIfMcacAvailOpnlBw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 2, 1, 27),
    _VRtrMldIfMcacAvailOpnlBw_Type()
)
vRtrMldIfMcacAvailOpnlBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldIfMcacAvailOpnlBw.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMldIfMcacAvailOpnlBw.setUnits("kbps")
_VRtrMldIfMcacValuesInTransit_Type = TruthValue
_VRtrMldIfMcacValuesInTransit_Object = MibTableColumn
vRtrMldIfMcacValuesInTransit = _VRtrMldIfMcacValuesInTransit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 2, 1, 28),
    _VRtrMldIfMcacValuesInTransit_Type()
)
vRtrMldIfMcacValuesInTransit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldIfMcacValuesInTransit.setStatus("current")


class _VRtrMldIfMaxSources_Type(Unsigned32):
    """Custom type vRtrMldIfMaxSources based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1000),
    )


_VRtrMldIfMaxSources_Type.__name__ = "Unsigned32"
_VRtrMldIfMaxSources_Object = MibTableColumn
vRtrMldIfMaxSources = _VRtrMldIfMaxSources_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 2, 1, 29),
    _VRtrMldIfMaxSources_Type()
)
vRtrMldIfMaxSources.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMldIfMaxSources.setStatus("current")


class _VRtrMldIfMaxGrpSources_Type(Unsigned32):
    """Custom type vRtrMldIfMaxGrpSources based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 32000),
    )


_VRtrMldIfMaxGrpSources_Type.__name__ = "Unsigned32"
_VRtrMldIfMaxGrpSources_Object = MibTableColumn
vRtrMldIfMaxGrpSources = _VRtrMldIfMaxGrpSources_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 2, 1, 30),
    _VRtrMldIfMaxGrpSources_Type()
)
vRtrMldIfMaxGrpSources.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMldIfMaxGrpSources.setStatus("current")


class _VRtrMldIfMcacUseLagPortWeight_Type(TruthValue):
    """Custom type vRtrMldIfMcacUseLagPortWeight based on TruthValue"""
    defaultValue = 2


_VRtrMldIfMcacUseLagPortWeight_Type.__name__ = "TruthValue"
_VRtrMldIfMcacUseLagPortWeight_Object = MibTableColumn
vRtrMldIfMcacUseLagPortWeight = _VRtrMldIfMcacUseLagPortWeight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 2, 1, 31),
    _VRtrMldIfMcacUseLagPortWeight_Type()
)
vRtrMldIfMcacUseLagPortWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMldIfMcacUseLagPortWeight.setStatus("current")
_VRtrMldIfGroupTable_Object = MibTable
vRtrMldIfGroupTable = _VRtrMldIfGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 3)
)
if mibBuilder.loadTexts:
    vRtrMldIfGroupTable.setStatus("current")
_VRtrMldIfGroupEntry_Object = MibTableRow
vRtrMldIfGroupEntry = _VRtrMldIfGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 3, 1)
)
vRtrMldIfGroupEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-VRTR-MIB", "vRtrIfIndex"),
    (0, "TIMETRA-MLD-MIB", "vRtrMldIfGroupAddressType"),
    (0, "TIMETRA-MLD-MIB", "vRtrMldIfGroupAddress"),
)
if mibBuilder.loadTexts:
    vRtrMldIfGroupEntry.setStatus("current")
_VRtrMldIfGroupAddressType_Type = InetAddressType
_VRtrMldIfGroupAddressType_Object = MibTableColumn
vRtrMldIfGroupAddressType = _VRtrMldIfGroupAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 3, 1, 1),
    _VRtrMldIfGroupAddressType_Type()
)
vRtrMldIfGroupAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMldIfGroupAddressType.setStatus("current")


class _VRtrMldIfGroupAddress_Type(InetAddress):
    """Custom type vRtrMldIfGroupAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_VRtrMldIfGroupAddress_Type.__name__ = "InetAddress"
_VRtrMldIfGroupAddress_Object = MibTableColumn
vRtrMldIfGroupAddress = _VRtrMldIfGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 3, 1, 2),
    _VRtrMldIfGroupAddress_Type()
)
vRtrMldIfGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMldIfGroupAddress.setStatus("current")


class _VRtrMldIfGroupType_Type(Integer32):
    """Custom type vRtrMldIfGroupType based on Integer32"""
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


_VRtrMldIfGroupType_Type.__name__ = "Integer32"
_VRtrMldIfGroupType_Object = MibTableColumn
vRtrMldIfGroupType = _VRtrMldIfGroupType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 3, 1, 3),
    _VRtrMldIfGroupType_Type()
)
vRtrMldIfGroupType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldIfGroupType.setStatus("current")
_VRtrMldIfGroupUpTime_Type = TimeInterval
_VRtrMldIfGroupUpTime_Object = MibTableColumn
vRtrMldIfGroupUpTime = _VRtrMldIfGroupUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 3, 1, 4),
    _VRtrMldIfGroupUpTime_Type()
)
vRtrMldIfGroupUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldIfGroupUpTime.setStatus("current")
_VRtrMldIfGroupExpiryTime_Type = TimeInterval
_VRtrMldIfGroupExpiryTime_Object = MibTableColumn
vRtrMldIfGroupExpiryTime = _VRtrMldIfGroupExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 3, 1, 5),
    _VRtrMldIfGroupExpiryTime_Type()
)
vRtrMldIfGroupExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldIfGroupExpiryTime.setStatus("current")
_VRtrMldIfGroupVer1HostTimer_Type = TimeInterval
_VRtrMldIfGroupVer1HostTimer_Object = MibTableColumn
vRtrMldIfGroupVer1HostTimer = _VRtrMldIfGroupVer1HostTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 3, 1, 6),
    _VRtrMldIfGroupVer1HostTimer_Type()
)
vRtrMldIfGroupVer1HostTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldIfGroupVer1HostTimer.setStatus("current")


class _VRtrMldIfGroupMode_Type(Integer32):
    """Custom type vRtrMldIfGroupMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("include", 1),
          ("exclude", 2))
    )


_VRtrMldIfGroupMode_Type.__name__ = "Integer32"
_VRtrMldIfGroupMode_Object = MibTableColumn
vRtrMldIfGroupMode = _VRtrMldIfGroupMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 3, 1, 7),
    _VRtrMldIfGroupMode_Type()
)
vRtrMldIfGroupMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldIfGroupMode.setStatus("current")
_VRtrMldIfGroupCompatMode_Type = TmnxMldVersion
_VRtrMldIfGroupCompatMode_Object = MibTableColumn
vRtrMldIfGroupCompatMode = _VRtrMldIfGroupCompatMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 3, 1, 8),
    _VRtrMldIfGroupCompatMode_Type()
)
vRtrMldIfGroupCompatMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldIfGroupCompatMode.setStatus("current")
_VRtrMldIfGroupLstRprtrType_Type = InetAddressType
_VRtrMldIfGroupLstRprtrType_Object = MibTableColumn
vRtrMldIfGroupLstRprtrType = _VRtrMldIfGroupLstRprtrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 3, 1, 9),
    _VRtrMldIfGroupLstRprtrType_Type()
)
vRtrMldIfGroupLstRprtrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldIfGroupLstRprtrType.setStatus("current")


class _VRtrMldIfGroupLastReporter_Type(InetAddress):
    """Custom type vRtrMldIfGroupLastReporter based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_VRtrMldIfGroupLastReporter_Type.__name__ = "InetAddress"
_VRtrMldIfGroupLastReporter_Object = MibTableColumn
vRtrMldIfGroupLastReporter = _VRtrMldIfGroupLastReporter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 3, 1, 10),
    _VRtrMldIfGroupLastReporter_Type()
)
vRtrMldIfGroupLastReporter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldIfGroupLastReporter.setStatus("current")
_VRtrMldIfGrpSrcTable_Object = MibTable
vRtrMldIfGrpSrcTable = _VRtrMldIfGrpSrcTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 4)
)
if mibBuilder.loadTexts:
    vRtrMldIfGrpSrcTable.setStatus("current")
_VRtrMldIfGrpSrcEntry_Object = MibTableRow
vRtrMldIfGrpSrcEntry = _VRtrMldIfGrpSrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 4, 1)
)
vRtrMldIfGrpSrcEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-VRTR-MIB", "vRtrIfIndex"),
    (0, "TIMETRA-MLD-MIB", "vRtrMldIfGroupAddressType"),
    (0, "TIMETRA-MLD-MIB", "vRtrMldIfGroupAddress"),
    (0, "TIMETRA-MLD-MIB", "vRtrMldIfGrpSrcAddrType"),
    (0, "TIMETRA-MLD-MIB", "vRtrMldIfGrpSrcAddress"),
)
if mibBuilder.loadTexts:
    vRtrMldIfGrpSrcEntry.setStatus("current")
_VRtrMldIfGrpSrcAddrType_Type = InetAddressType
_VRtrMldIfGrpSrcAddrType_Object = MibTableColumn
vRtrMldIfGrpSrcAddrType = _VRtrMldIfGrpSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 4, 1, 1),
    _VRtrMldIfGrpSrcAddrType_Type()
)
vRtrMldIfGrpSrcAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMldIfGrpSrcAddrType.setStatus("current")


class _VRtrMldIfGrpSrcAddress_Type(InetAddress):
    """Custom type vRtrMldIfGrpSrcAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_VRtrMldIfGrpSrcAddress_Type.__name__ = "InetAddress"
_VRtrMldIfGrpSrcAddress_Object = MibTableColumn
vRtrMldIfGrpSrcAddress = _VRtrMldIfGrpSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 4, 1, 2),
    _VRtrMldIfGrpSrcAddress_Type()
)
vRtrMldIfGrpSrcAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMldIfGrpSrcAddress.setStatus("current")
_VRtrMldIfGrpSrcExpiryTime_Type = TimeInterval
_VRtrMldIfGrpSrcExpiryTime_Object = MibTableColumn
vRtrMldIfGrpSrcExpiryTime = _VRtrMldIfGrpSrcExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 4, 1, 3),
    _VRtrMldIfGrpSrcExpiryTime_Type()
)
vRtrMldIfGrpSrcExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldIfGrpSrcExpiryTime.setStatus("current")


class _VRtrMldIfGrpSrcType_Type(Integer32):
    """Custom type vRtrMldIfGrpSrcType based on Integer32"""
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


_VRtrMldIfGrpSrcType_Type.__name__ = "Integer32"
_VRtrMldIfGrpSrcType_Object = MibTableColumn
vRtrMldIfGrpSrcType = _VRtrMldIfGrpSrcType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 4, 1, 4),
    _VRtrMldIfGrpSrcType_Type()
)
vRtrMldIfGrpSrcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldIfGrpSrcType.setStatus("current")
_VRtrMldIfStatcGrpSrcTblLstChngd_Type = TimeStamp
_VRtrMldIfStatcGrpSrcTblLstChngd_Object = MibScalar
vRtrMldIfStatcGrpSrcTblLstChngd = _VRtrMldIfStatcGrpSrcTblLstChngd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 5),
    _VRtrMldIfStatcGrpSrcTblLstChngd_Type()
)
vRtrMldIfStatcGrpSrcTblLstChngd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldIfStatcGrpSrcTblLstChngd.setStatus("current")
_VRtrMldIfStaticGrpSrcTable_Object = MibTable
vRtrMldIfStaticGrpSrcTable = _VRtrMldIfStaticGrpSrcTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 6)
)
if mibBuilder.loadTexts:
    vRtrMldIfStaticGrpSrcTable.setStatus("current")
_VRtrMldIfStaticGrpSrcEntry_Object = MibTableRow
vRtrMldIfStaticGrpSrcEntry = _VRtrMldIfStaticGrpSrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 6, 1)
)
vRtrMldIfStaticGrpSrcEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-VRTR-MIB", "vRtrIfIndex"),
    (0, "TIMETRA-MLD-MIB", "vRtrMldIfGroupAddressType"),
    (0, "TIMETRA-MLD-MIB", "vRtrMldIfGroupAddress"),
    (0, "TIMETRA-MLD-MIB", "vRtrMldIfGrpSrcAddrType"),
    (0, "TIMETRA-MLD-MIB", "vRtrMldIfGrpSrcAddress"),
)
if mibBuilder.loadTexts:
    vRtrMldIfStaticGrpSrcEntry.setStatus("current")
_VRtrMldIfStaticGrpSrcRowStatus_Type = RowStatus
_VRtrMldIfStaticGrpSrcRowStatus_Object = MibTableColumn
vRtrMldIfStaticGrpSrcRowStatus = _VRtrMldIfStaticGrpSrcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 6, 1, 1),
    _VRtrMldIfStaticGrpSrcRowStatus_Type()
)
vRtrMldIfStaticGrpSrcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMldIfStaticGrpSrcRowStatus.setStatus("current")
_VRtrMldIfStaticGrpSrcLstChanged_Type = TimeStamp
_VRtrMldIfStaticGrpSrcLstChanged_Object = MibTableColumn
vRtrMldIfStaticGrpSrcLstChanged = _VRtrMldIfStaticGrpSrcLstChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 6, 1, 2),
    _VRtrMldIfStaticGrpSrcLstChanged_Type()
)
vRtrMldIfStaticGrpSrcLstChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldIfStaticGrpSrcLstChanged.setStatus("current")
_VRtrMldIfStatsTable_Object = MibTable
vRtrMldIfStatsTable = _VRtrMldIfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 7)
)
if mibBuilder.loadTexts:
    vRtrMldIfStatsTable.setStatus("current")
_VRtrMldIfStatsEntry_Object = MibTableRow
vRtrMldIfStatsEntry = _VRtrMldIfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 7, 1)
)
if mibBuilder.loadTexts:
    vRtrMldIfStatsEntry.setStatus("current")
_VRtrMldIfTxGenQueries_Type = Counter32
_VRtrMldIfTxGenQueries_Object = MibTableColumn
vRtrMldIfTxGenQueries = _VRtrMldIfTxGenQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 7, 1, 1),
    _VRtrMldIfTxGenQueries_Type()
)
vRtrMldIfTxGenQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldIfTxGenQueries.setStatus("current")
_VRtrMldIfTxGrpQueries_Type = Counter32
_VRtrMldIfTxGrpQueries_Object = MibTableColumn
vRtrMldIfTxGrpQueries = _VRtrMldIfTxGrpQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 7, 1, 2),
    _VRtrMldIfTxGrpQueries_Type()
)
vRtrMldIfTxGrpQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldIfTxGrpQueries.setStatus("current")
_VRtrMldIfTxGrpSrcQueries_Type = Counter32
_VRtrMldIfTxGrpSrcQueries_Object = MibTableColumn
vRtrMldIfTxGrpSrcQueries = _VRtrMldIfTxGrpSrcQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 7, 1, 3),
    _VRtrMldIfTxGrpSrcQueries_Type()
)
vRtrMldIfTxGrpSrcQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldIfTxGrpSrcQueries.setStatus("current")
_VRtrMldIfTxV1Reports_Type = Counter32
_VRtrMldIfTxV1Reports_Object = MibTableColumn
vRtrMldIfTxV1Reports = _VRtrMldIfTxV1Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 7, 1, 4),
    _VRtrMldIfTxV1Reports_Type()
)
vRtrMldIfTxV1Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldIfTxV1Reports.setStatus("current")
_VRtrMldIfTxV2Reports_Type = Counter32
_VRtrMldIfTxV2Reports_Object = MibTableColumn
vRtrMldIfTxV2Reports = _VRtrMldIfTxV2Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 7, 1, 5),
    _VRtrMldIfTxV2Reports_Type()
)
vRtrMldIfTxV2Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldIfTxV2Reports.setStatus("current")
_VRtrMldIfTxLeaves_Type = Counter32
_VRtrMldIfTxLeaves_Object = MibTableColumn
vRtrMldIfTxLeaves = _VRtrMldIfTxLeaves_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 7, 1, 6),
    _VRtrMldIfTxLeaves_Type()
)
vRtrMldIfTxLeaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldIfTxLeaves.setStatus("current")
_VRtrMldIfTxErrors_Type = Counter32
_VRtrMldIfTxErrors_Object = MibTableColumn
vRtrMldIfTxErrors = _VRtrMldIfTxErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 7, 1, 7),
    _VRtrMldIfTxErrors_Type()
)
vRtrMldIfTxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldIfTxErrors.setStatus("current")
_VRtrMldIfRxGenQueries_Type = Counter32
_VRtrMldIfRxGenQueries_Object = MibTableColumn
vRtrMldIfRxGenQueries = _VRtrMldIfRxGenQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 7, 1, 8),
    _VRtrMldIfRxGenQueries_Type()
)
vRtrMldIfRxGenQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldIfRxGenQueries.setStatus("current")
_VRtrMldIfRxGrpQueries_Type = Counter32
_VRtrMldIfRxGrpQueries_Object = MibTableColumn
vRtrMldIfRxGrpQueries = _VRtrMldIfRxGrpQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 7, 1, 9),
    _VRtrMldIfRxGrpQueries_Type()
)
vRtrMldIfRxGrpQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldIfRxGrpQueries.setStatus("current")
_VRtrMldIfRxGrpSrcQueries_Type = Counter32
_VRtrMldIfRxGrpSrcQueries_Object = MibTableColumn
vRtrMldIfRxGrpSrcQueries = _VRtrMldIfRxGrpSrcQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 7, 1, 10),
    _VRtrMldIfRxGrpSrcQueries_Type()
)
vRtrMldIfRxGrpSrcQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldIfRxGrpSrcQueries.setStatus("current")
_VRtrMldIfRxV1Reports_Type = Counter32
_VRtrMldIfRxV1Reports_Object = MibTableColumn
vRtrMldIfRxV1Reports = _VRtrMldIfRxV1Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 7, 1, 11),
    _VRtrMldIfRxV1Reports_Type()
)
vRtrMldIfRxV1Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldIfRxV1Reports.setStatus("current")
_VRtrMldIfRxV2Reports_Type = Counter32
_VRtrMldIfRxV2Reports_Object = MibTableColumn
vRtrMldIfRxV2Reports = _VRtrMldIfRxV2Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 7, 1, 12),
    _VRtrMldIfRxV2Reports_Type()
)
vRtrMldIfRxV2Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldIfRxV2Reports.setStatus("current")
_VRtrMldIfRxLeaves_Type = Counter32
_VRtrMldIfRxLeaves_Object = MibTableColumn
vRtrMldIfRxLeaves = _VRtrMldIfRxLeaves_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 7, 1, 13),
    _VRtrMldIfRxLeaves_Type()
)
vRtrMldIfRxLeaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldIfRxLeaves.setStatus("current")
_VRtrMldIfRxBadLenPkts_Type = Counter32
_VRtrMldIfRxBadLenPkts_Object = MibTableColumn
vRtrMldIfRxBadLenPkts = _VRtrMldIfRxBadLenPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 7, 1, 14),
    _VRtrMldIfRxBadLenPkts_Type()
)
vRtrMldIfRxBadLenPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldIfRxBadLenPkts.setStatus("current")
_VRtrMldIfRxBadChecksumPkts_Type = Counter32
_VRtrMldIfRxBadChecksumPkts_Object = MibTableColumn
vRtrMldIfRxBadChecksumPkts = _VRtrMldIfRxBadChecksumPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 7, 1, 15),
    _VRtrMldIfRxBadChecksumPkts_Type()
)
vRtrMldIfRxBadChecksumPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldIfRxBadChecksumPkts.setStatus("current")
_VRtrMldIfRxUnknownTypePkts_Type = Counter32
_VRtrMldIfRxUnknownTypePkts_Object = MibTableColumn
vRtrMldIfRxUnknownTypePkts = _VRtrMldIfRxUnknownTypePkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 7, 1, 16),
    _VRtrMldIfRxUnknownTypePkts_Type()
)
vRtrMldIfRxUnknownTypePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldIfRxUnknownTypePkts.setStatus("current")
_VRtrMldIfRxBadReceiveIfPkts_Type = Counter32
_VRtrMldIfRxBadReceiveIfPkts_Object = MibTableColumn
vRtrMldIfRxBadReceiveIfPkts = _VRtrMldIfRxBadReceiveIfPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 7, 1, 17),
    _VRtrMldIfRxBadReceiveIfPkts_Type()
)
vRtrMldIfRxBadReceiveIfPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldIfRxBadReceiveIfPkts.setStatus("current")
_VRtrMldIfRxNonLocal_Type = Counter32
_VRtrMldIfRxNonLocal_Object = MibTableColumn
vRtrMldIfRxNonLocal = _VRtrMldIfRxNonLocal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 7, 1, 18),
    _VRtrMldIfRxNonLocal_Type()
)
vRtrMldIfRxNonLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldIfRxNonLocal.setStatus("current")
_VRtrMldIfRxWrongVersions_Type = Counter32
_VRtrMldIfRxWrongVersions_Object = MibTableColumn
vRtrMldIfRxWrongVersions = _VRtrMldIfRxWrongVersions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 7, 1, 19),
    _VRtrMldIfRxWrongVersions_Type()
)
vRtrMldIfRxWrongVersions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldIfRxWrongVersions.setStatus("current")
_VRtrMldIfImportPolicyDrops_Type = Counter32
_VRtrMldIfImportPolicyDrops_Object = MibTableColumn
vRtrMldIfImportPolicyDrops = _VRtrMldIfImportPolicyDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 7, 1, 20),
    _VRtrMldIfImportPolicyDrops_Type()
)
vRtrMldIfImportPolicyDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldIfImportPolicyDrops.setStatus("current")
_VRtrMldIfRxNoRtrAlertPkts_Type = Counter32
_VRtrMldIfRxNoRtrAlertPkts_Object = MibTableColumn
vRtrMldIfRxNoRtrAlertPkts = _VRtrMldIfRxNoRtrAlertPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 7, 1, 21),
    _VRtrMldIfRxNoRtrAlertPkts_Type()
)
vRtrMldIfRxNoRtrAlertPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldIfRxNoRtrAlertPkts.setStatus("current")
_VRtrMldIfRxBadEncodings_Type = Counter32
_VRtrMldIfRxBadEncodings_Object = MibTableColumn
vRtrMldIfRxBadEncodings = _VRtrMldIfRxBadEncodings_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 7, 1, 22),
    _VRtrMldIfRxBadEncodings_Type()
)
vRtrMldIfRxBadEncodings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldIfRxBadEncodings.setStatus("current")
_VRtrMldIfRxPktDrops_Type = Counter32
_VRtrMldIfRxPktDrops_Object = MibTableColumn
vRtrMldIfRxPktDrops = _VRtrMldIfRxPktDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 7, 1, 23),
    _VRtrMldIfRxPktDrops_Type()
)
vRtrMldIfRxPktDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldIfRxPktDrops.setStatus("current")
_VRtrMldIfStatsStarGTypes_Type = Gauge32
_VRtrMldIfStatsStarGTypes_Object = MibTableColumn
vRtrMldIfStatsStarGTypes = _VRtrMldIfStatsStarGTypes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 7, 1, 24),
    _VRtrMldIfStatsStarGTypes_Type()
)
vRtrMldIfStatsStarGTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldIfStatsStarGTypes.setStatus("current")
_VRtrMldIfStatsSGTypes_Type = Gauge32
_VRtrMldIfStatsSGTypes_Object = MibTableColumn
vRtrMldIfStatsSGTypes = _VRtrMldIfStatsSGTypes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 7, 1, 25),
    _VRtrMldIfStatsSGTypes_Type()
)
vRtrMldIfStatsSGTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldIfStatsSGTypes.setStatus("current")
_VRtrMldIfRxLocalScopePkts_Type = Counter32
_VRtrMldIfRxLocalScopePkts_Object = MibTableColumn
vRtrMldIfRxLocalScopePkts = _VRtrMldIfRxLocalScopePkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 7, 1, 26),
    _VRtrMldIfRxLocalScopePkts_Type()
)
vRtrMldIfRxLocalScopePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldIfRxLocalScopePkts.setStatus("current")
_VRtrMldIfRxRsvdScopePkts_Type = Counter32
_VRtrMldIfRxRsvdScopePkts_Object = MibTableColumn
vRtrMldIfRxRsvdScopePkts = _VRtrMldIfRxRsvdScopePkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 7, 1, 27),
    _VRtrMldIfRxRsvdScopePkts_Type()
)
vRtrMldIfRxRsvdScopePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldIfRxRsvdScopePkts.setStatus("current")
_VRtrMldIfStatsMcacPolicyDrops_Type = Counter32
_VRtrMldIfStatsMcacPolicyDrops_Object = MibTableColumn
vRtrMldIfStatsMcacPolicyDrops = _VRtrMldIfStatsMcacPolicyDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 7, 1, 28),
    _VRtrMldIfStatsMcacPolicyDrops_Type()
)
vRtrMldIfStatsMcacPolicyDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldIfStatsMcacPolicyDrops.setStatus("current")
_VRtrMldIfSsmTltTableLastChanged_Type = TimeStamp
_VRtrMldIfSsmTltTableLastChanged_Object = MibScalar
vRtrMldIfSsmTltTableLastChanged = _VRtrMldIfSsmTltTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 8),
    _VRtrMldIfSsmTltTableLastChanged_Type()
)
vRtrMldIfSsmTltTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldIfSsmTltTableLastChanged.setStatus("current")
_VRtrMldIfSsmTransTable_Object = MibTable
vRtrMldIfSsmTransTable = _VRtrMldIfSsmTransTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 9)
)
if mibBuilder.loadTexts:
    vRtrMldIfSsmTransTable.setStatus("current")
_VRtrMldIfSsmTransEntry_Object = MibTableRow
vRtrMldIfSsmTransEntry = _VRtrMldIfSsmTransEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 9, 1)
)
vRtrMldIfSsmTransEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-VRTR-MIB", "vRtrIfIndex"),
    (0, "TIMETRA-MLD-MIB", "vRtrMldIfSsmTransGrpAddrType1"),
    (0, "TIMETRA-MLD-MIB", "vRtrMldIfSsmTransGrpAddr1"),
    (0, "TIMETRA-MLD-MIB", "vRtrMldIfSsmTransGrpAddrType2"),
    (0, "TIMETRA-MLD-MIB", "vRtrMldIfSsmTransGrpAddr2"),
    (0, "TIMETRA-MLD-MIB", "vRtrMldIfSsmTransSrcAddrType"),
    (0, "TIMETRA-MLD-MIB", "vRtrMldIfSsmTransSrcAddr"),
)
if mibBuilder.loadTexts:
    vRtrMldIfSsmTransEntry.setStatus("current")
_VRtrMldIfSsmTransGrpAddrType1_Type = InetAddressType
_VRtrMldIfSsmTransGrpAddrType1_Object = MibTableColumn
vRtrMldIfSsmTransGrpAddrType1 = _VRtrMldIfSsmTransGrpAddrType1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 9, 1, 1),
    _VRtrMldIfSsmTransGrpAddrType1_Type()
)
vRtrMldIfSsmTransGrpAddrType1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMldIfSsmTransGrpAddrType1.setStatus("current")


class _VRtrMldIfSsmTransGrpAddr1_Type(InetAddress):
    """Custom type vRtrMldIfSsmTransGrpAddr1 based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_VRtrMldIfSsmTransGrpAddr1_Type.__name__ = "InetAddress"
_VRtrMldIfSsmTransGrpAddr1_Object = MibTableColumn
vRtrMldIfSsmTransGrpAddr1 = _VRtrMldIfSsmTransGrpAddr1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 9, 1, 2),
    _VRtrMldIfSsmTransGrpAddr1_Type()
)
vRtrMldIfSsmTransGrpAddr1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMldIfSsmTransGrpAddr1.setStatus("current")
_VRtrMldIfSsmTransGrpAddrType2_Type = InetAddressType
_VRtrMldIfSsmTransGrpAddrType2_Object = MibTableColumn
vRtrMldIfSsmTransGrpAddrType2 = _VRtrMldIfSsmTransGrpAddrType2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 9, 1, 3),
    _VRtrMldIfSsmTransGrpAddrType2_Type()
)
vRtrMldIfSsmTransGrpAddrType2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMldIfSsmTransGrpAddrType2.setStatus("current")


class _VRtrMldIfSsmTransGrpAddr2_Type(InetAddress):
    """Custom type vRtrMldIfSsmTransGrpAddr2 based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_VRtrMldIfSsmTransGrpAddr2_Type.__name__ = "InetAddress"
_VRtrMldIfSsmTransGrpAddr2_Object = MibTableColumn
vRtrMldIfSsmTransGrpAddr2 = _VRtrMldIfSsmTransGrpAddr2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 9, 1, 4),
    _VRtrMldIfSsmTransGrpAddr2_Type()
)
vRtrMldIfSsmTransGrpAddr2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMldIfSsmTransGrpAddr2.setStatus("current")
_VRtrMldIfSsmTransSrcAddrType_Type = InetAddressType
_VRtrMldIfSsmTransSrcAddrType_Object = MibTableColumn
vRtrMldIfSsmTransSrcAddrType = _VRtrMldIfSsmTransSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 9, 1, 5),
    _VRtrMldIfSsmTransSrcAddrType_Type()
)
vRtrMldIfSsmTransSrcAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMldIfSsmTransSrcAddrType.setStatus("current")


class _VRtrMldIfSsmTransSrcAddr_Type(InetAddress):
    """Custom type vRtrMldIfSsmTransSrcAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_VRtrMldIfSsmTransSrcAddr_Type.__name__ = "InetAddress"
_VRtrMldIfSsmTransSrcAddr_Object = MibTableColumn
vRtrMldIfSsmTransSrcAddr = _VRtrMldIfSsmTransSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 9, 1, 6),
    _VRtrMldIfSsmTransSrcAddr_Type()
)
vRtrMldIfSsmTransSrcAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMldIfSsmTransSrcAddr.setStatus("current")
_VRtrMldIfSsmTransRowStatus_Type = RowStatus
_VRtrMldIfSsmTransRowStatus_Object = MibTableColumn
vRtrMldIfSsmTransRowStatus = _VRtrMldIfSsmTransRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 9, 1, 7),
    _VRtrMldIfSsmTransRowStatus_Type()
)
vRtrMldIfSsmTransRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMldIfSsmTransRowStatus.setStatus("current")
_VRtrMldIfMcacLevelTable_Object = MibTable
vRtrMldIfMcacLevelTable = _VRtrMldIfMcacLevelTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 10)
)
if mibBuilder.loadTexts:
    vRtrMldIfMcacLevelTable.setStatus("current")
_VRtrMldIfMcacLevelEntry_Object = MibTableRow
vRtrMldIfMcacLevelEntry = _VRtrMldIfMcacLevelEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 10, 1)
)
vRtrMldIfMcacLevelEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-VRTR-MIB", "vRtrIfIndex"),
    (0, "TIMETRA-MCAST-CAC-MIB", "tmnxMcacLevelId"),
)
if mibBuilder.loadTexts:
    vRtrMldIfMcacLevelEntry.setStatus("current")
_VRtrMldIfMcacLevelRowStatus_Type = RowStatus
_VRtrMldIfMcacLevelRowStatus_Object = MibTableColumn
vRtrMldIfMcacLevelRowStatus = _VRtrMldIfMcacLevelRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 10, 1, 1),
    _VRtrMldIfMcacLevelRowStatus_Type()
)
vRtrMldIfMcacLevelRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMldIfMcacLevelRowStatus.setStatus("current")


class _VRtrMldIfMcacLevelBW_Type(Unsigned32):
    """Custom type vRtrMldIfMcacLevelBW based on Unsigned32"""
    defaultValue = 1


_VRtrMldIfMcacLevelBW_Type.__name__ = "Unsigned32"
_VRtrMldIfMcacLevelBW_Object = MibTableColumn
vRtrMldIfMcacLevelBW = _VRtrMldIfMcacLevelBW_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 10, 1, 2),
    _VRtrMldIfMcacLevelBW_Type()
)
vRtrMldIfMcacLevelBW.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMldIfMcacLevelBW.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMldIfMcacLevelBW.setUnits("kbps")
_VRtrMldIfMcacLagTable_Object = MibTable
vRtrMldIfMcacLagTable = _VRtrMldIfMcacLagTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 11)
)
if mibBuilder.loadTexts:
    vRtrMldIfMcacLagTable.setStatus("current")
_VRtrMldIfMcacLagEntry_Object = MibTableRow
vRtrMldIfMcacLagEntry = _VRtrMldIfMcacLagEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 11, 1)
)
vRtrMldIfMcacLagEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-VRTR-MIB", "vRtrIfIndex"),
    (0, "TIMETRA-MCAST-CAC-MIB", "tmnxMcacLagPortsDown"),
)
if mibBuilder.loadTexts:
    vRtrMldIfMcacLagEntry.setStatus("current")
_VRtrMldIfMcacLagRowStatus_Type = RowStatus
_VRtrMldIfMcacLagRowStatus_Object = MibTableColumn
vRtrMldIfMcacLagRowStatus = _VRtrMldIfMcacLagRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 11, 1, 1),
    _VRtrMldIfMcacLagRowStatus_Type()
)
vRtrMldIfMcacLagRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMldIfMcacLagRowStatus.setStatus("current")


class _VRtrMldIfMcacLagLevel_Type(Unsigned32):
    """Custom type vRtrMldIfMcacLagLevel based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_VRtrMldIfMcacLagLevel_Type.__name__ = "Unsigned32"
_VRtrMldIfMcacLagLevel_Object = MibTableColumn
vRtrMldIfMcacLagLevel = _VRtrMldIfMcacLagLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 2, 11, 1, 2),
    _VRtrMldIfMcacLagLevel_Type()
)
vRtrMldIfMcacLagLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMldIfMcacLagLevel.setStatus("current")
_VRtrMldNotificationObjs_ObjectIdentity = ObjectIdentity
vRtrMldNotificationObjs = _VRtrMldNotificationObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 3)
)
_VRtrMldNotifyQueryVersion_Type = Unsigned32
_VRtrMldNotifyQueryVersion_Object = MibScalar
vRtrMldNotifyQueryVersion = _VRtrMldNotifyQueryVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 3, 1),
    _VRtrMldNotifyQueryVersion_Type()
)
vRtrMldNotifyQueryVersion.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrMldNotifyQueryVersion.setStatus("current")
_VRtrMldNotifyGrpAddrType_Type = InetAddressType
_VRtrMldNotifyGrpAddrType_Object = MibScalar
vRtrMldNotifyGrpAddrType = _VRtrMldNotifyGrpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 3, 2),
    _VRtrMldNotifyGrpAddrType_Type()
)
vRtrMldNotifyGrpAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrMldNotifyGrpAddrType.setStatus("current")
_VRtrMldNotifyGrpAddr_Type = InetAddress
_VRtrMldNotifyGrpAddr_Object = MibScalar
vRtrMldNotifyGrpAddr = _VRtrMldNotifyGrpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 3, 3),
    _VRtrMldNotifyGrpAddr_Type()
)
vRtrMldNotifyGrpAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrMldNotifyGrpAddr.setStatus("current")
_VRtrMldNotifyDescription_Type = DisplayString
_VRtrMldNotifyDescription_Object = MibScalar
vRtrMldNotifyDescription = _VRtrMldNotifyDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 3, 4),
    _VRtrMldNotifyDescription_Type()
)
vRtrMldNotifyDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrMldNotifyDescription.setStatus("current")
_VRtrMldNotifyMcacPolicyName_Type = TPolicyStatementNameOrEmpty
_VRtrMldNotifyMcacPolicyName_Object = MibScalar
vRtrMldNotifyMcacPolicyName = _VRtrMldNotifyMcacPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 3, 5),
    _VRtrMldNotifyMcacPolicyName_Type()
)
vRtrMldNotifyMcacPolicyName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrMldNotifyMcacPolicyName.setStatus("current")
_VRtrMldNotifySrcAddrType_Type = InetAddressType
_VRtrMldNotifySrcAddrType_Object = MibScalar
vRtrMldNotifySrcAddrType = _VRtrMldNotifySrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 3, 6),
    _VRtrMldNotifySrcAddrType_Type()
)
vRtrMldNotifySrcAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrMldNotifySrcAddrType.setStatus("current")
_VRtrMldNotifySrcAddr_Type = InetAddress
_VRtrMldNotifySrcAddr_Object = MibScalar
vRtrMldNotifySrcAddr = _VRtrMldNotifySrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 3, 7),
    _VRtrMldNotifySrcAddr_Type()
)
vRtrMldNotifySrcAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrMldNotifySrcAddr.setStatus("current")
_VRtrMldHostObjs_ObjectIdentity = ObjectIdentity
vRtrMldHostObjs = _VRtrMldHostObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4)
)
_VRtrMldHostTable_Object = MibTable
vRtrMldHostTable = _VRtrMldHostTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 1)
)
if mibBuilder.loadTexts:
    vRtrMldHostTable.setStatus("current")
_VRtrMldHostEntry_Object = MibTableRow
vRtrMldHostEntry = _VRtrMldHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 1, 1)
)
vRtrMldHostEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MLD-MIB", "vRtrMldHostAddressType"),
    (0, "TIMETRA-MLD-MIB", "vRtrMldHostAddress"),
    (0, "TIMETRA-MLD-MIB", "vRtrMldHostMacAddress"),
    (0, "TIMETRA-MLD-MIB", "vRtrMldHostPppoeSessionId"),
)
if mibBuilder.loadTexts:
    vRtrMldHostEntry.setStatus("current")
_VRtrMldHostAddressType_Type = InetAddressType
_VRtrMldHostAddressType_Object = MibTableColumn
vRtrMldHostAddressType = _VRtrMldHostAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 1, 1, 1),
    _VRtrMldHostAddressType_Type()
)
vRtrMldHostAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMldHostAddressType.setStatus("current")


class _VRtrMldHostAddress_Type(InetAddress):
    """Custom type vRtrMldHostAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_VRtrMldHostAddress_Type.__name__ = "InetAddress"
_VRtrMldHostAddress_Object = MibTableColumn
vRtrMldHostAddress = _VRtrMldHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 1, 1, 2),
    _VRtrMldHostAddress_Type()
)
vRtrMldHostAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMldHostAddress.setStatus("current")
_VRtrMldHostMacAddress_Type = MacAddress
_VRtrMldHostMacAddress_Object = MibTableColumn
vRtrMldHostMacAddress = _VRtrMldHostMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 1, 1, 3),
    _VRtrMldHostMacAddress_Type()
)
vRtrMldHostMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMldHostMacAddress.setStatus("current")
_VRtrMldHostPppoeSessionId_Type = TmnxPppoeSessionId
_VRtrMldHostPppoeSessionId_Object = MibTableColumn
vRtrMldHostPppoeSessionId = _VRtrMldHostPppoeSessionId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 1, 1, 4),
    _VRtrMldHostPppoeSessionId_Type()
)
vRtrMldHostPppoeSessionId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMldHostPppoeSessionId.setStatus("current")
_VRtrMldHostLastChangeTime_Type = TimeStamp
_VRtrMldHostLastChangeTime_Object = MibTableColumn
vRtrMldHostLastChangeTime = _VRtrMldHostLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 1, 1, 5),
    _VRtrMldHostLastChangeTime_Type()
)
vRtrMldHostLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldHostLastChangeTime.setStatus("current")
_VRtrMldHostOperState_Type = MldGrpItfOperState
_VRtrMldHostOperState_Object = MibTableColumn
vRtrMldHostOperState = _VRtrMldHostOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 1, 1, 6),
    _VRtrMldHostOperState_Type()
)
vRtrMldHostOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldHostOperState.setStatus("current")
_VRtrMldHostOperVersion_Type = TmnxMldVersion
_VRtrMldHostOperVersion_Object = MibTableColumn
vRtrMldHostOperVersion = _VRtrMldHostOperVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 1, 1, 7),
    _VRtrMldHostOperVersion_Type()
)
vRtrMldHostOperVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldHostOperVersion.setStatus("current")
_VRtrMldHostGroupCount_Type = Unsigned32
_VRtrMldHostGroupCount_Object = MibTableColumn
vRtrMldHostGroupCount = _VRtrMldHostGroupCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 1, 1, 8),
    _VRtrMldHostGroupCount_Type()
)
vRtrMldHostGroupCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldHostGroupCount.setStatus("current")
_VRtrMldHostNextGenQueryTime_Type = Unsigned32
_VRtrMldHostNextGenQueryTime_Object = MibTableColumn
vRtrMldHostNextGenQueryTime = _VRtrMldHostNextGenQueryTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 1, 1, 9),
    _VRtrMldHostNextGenQueryTime_Type()
)
vRtrMldHostNextGenQueryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldHostNextGenQueryTime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMldHostNextGenQueryTime.setUnits("seconds")
_VRtrMldHostMaxGroupsTillNow_Type = Counter32
_VRtrMldHostMaxGroupsTillNow_Object = MibTableColumn
vRtrMldHostMaxGroupsTillNow = _VRtrMldHostMaxGroupsTillNow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 1, 1, 10),
    _VRtrMldHostMaxGroupsTillNow_Type()
)
vRtrMldHostMaxGroupsTillNow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldHostMaxGroupsTillNow.setStatus("current")


class _VRtrMldHostFwdSvcId_Type(TmnxServId):
    """Custom type vRtrMldHostFwdSvcId based on TmnxServId"""
    defaultValue = 0


_VRtrMldHostFwdSvcId_Type.__name__ = "TmnxServId"
_VRtrMldHostFwdSvcId_Object = MibTableColumn
vRtrMldHostFwdSvcId = _VRtrMldHostFwdSvcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 1, 1, 11),
    _VRtrMldHostFwdSvcId_Type()
)
vRtrMldHostFwdSvcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldHostFwdSvcId.setStatus("current")
_VRtrMldHostGrpIfId_Type = InterfaceIndex
_VRtrMldHostGrpIfId_Object = MibTableColumn
vRtrMldHostGrpIfId = _VRtrMldHostGrpIfId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 1, 1, 12),
    _VRtrMldHostGrpIfId_Type()
)
vRtrMldHostGrpIfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldHostGrpIfId.setStatus("current")
_VRtrMldHostSubscriberId_Type = TmnxSubIdentStringOrEmpty
_VRtrMldHostSubscriberId_Object = MibTableColumn
vRtrMldHostSubscriberId = _VRtrMldHostSubscriberId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 1, 1, 13),
    _VRtrMldHostSubscriberId_Type()
)
vRtrMldHostSubscriberId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldHostSubscriberId.setStatus("current")


class _VRtrMldHostMldPolicy_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrMldHostMldPolicy based on TPolicyStatementNameOrEmpty"""
    defaultValue = OctetString("")


_VRtrMldHostMldPolicy_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrMldHostMldPolicy_Object = MibTableColumn
vRtrMldHostMldPolicy = _VRtrMldHostMldPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 1, 1, 14),
    _VRtrMldHostMldPolicy_Type()
)
vRtrMldHostMldPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldHostMldPolicy.setStatus("current")


class _VRtrMldHostMaxGroups_Type(Unsigned32):
    """Custom type vRtrMldHostMaxGroups based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 16000),
    )


_VRtrMldHostMaxGroups_Type.__name__ = "Unsigned32"
_VRtrMldHostMaxGroups_Object = MibTableColumn
vRtrMldHostMaxGroups = _VRtrMldHostMaxGroups_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 1, 1, 15),
    _VRtrMldHostMaxGroups_Type()
)
vRtrMldHostMaxGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldHostMaxGroups.setStatus("current")


class _VRtrMldHostAdminVersion_Type(TmnxMldVersion):
    """Custom type vRtrMldHostAdminVersion based on TmnxMldVersion"""
    defaultValue = 2


_VRtrMldHostAdminVersion_Type.__name__ = "TmnxMldVersion"
_VRtrMldHostAdminVersion_Object = MibTableColumn
vRtrMldHostAdminVersion = _VRtrMldHostAdminVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 1, 1, 16),
    _VRtrMldHostAdminVersion_Type()
)
vRtrMldHostAdminVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldHostAdminVersion.setStatus("current")


class _VRtrMldHostMaxSources_Type(Unsigned32):
    """Custom type vRtrMldHostMaxSources based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1000),
    )


_VRtrMldHostMaxSources_Type.__name__ = "Unsigned32"
_VRtrMldHostMaxSources_Object = MibTableColumn
vRtrMldHostMaxSources = _VRtrMldHostMaxSources_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 1, 1, 17),
    _VRtrMldHostMaxSources_Type()
)
vRtrMldHostMaxSources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldHostMaxSources.setStatus("current")


class _VRtrMldHostMaxGrpSources_Type(Unsigned32):
    """Custom type vRtrMldHostMaxGrpSources based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1000),
    )


_VRtrMldHostMaxGrpSources_Type.__name__ = "Unsigned32"
_VRtrMldHostMaxGrpSources_Object = MibTableColumn
vRtrMldHostMaxGrpSources = _VRtrMldHostMaxGrpSources_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 1, 1, 18),
    _VRtrMldHostMaxGrpSources_Type()
)
vRtrMldHostMaxGrpSources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldHostMaxGrpSources.setStatus("current")
_VRtrMldHostStatsTable_Object = MibTable
vRtrMldHostStatsTable = _VRtrMldHostStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 2)
)
if mibBuilder.loadTexts:
    vRtrMldHostStatsTable.setStatus("current")
_VRtrMldHostStatsEntry_Object = MibTableRow
vRtrMldHostStatsEntry = _VRtrMldHostStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 2, 1)
)
if mibBuilder.loadTexts:
    vRtrMldHostStatsEntry.setStatus("current")
_VRtrMldHostTxGenQueries_Type = Counter32
_VRtrMldHostTxGenQueries_Object = MibTableColumn
vRtrMldHostTxGenQueries = _VRtrMldHostTxGenQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 2, 1, 1),
    _VRtrMldHostTxGenQueries_Type()
)
vRtrMldHostTxGenQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldHostTxGenQueries.setStatus("current")
_VRtrMldHostTxGrpQueries_Type = Counter32
_VRtrMldHostTxGrpQueries_Object = MibTableColumn
vRtrMldHostTxGrpQueries = _VRtrMldHostTxGrpQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 2, 1, 2),
    _VRtrMldHostTxGrpQueries_Type()
)
vRtrMldHostTxGrpQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldHostTxGrpQueries.setStatus("current")
_VRtrMldHostTxGrpSrcQueries_Type = Counter32
_VRtrMldHostTxGrpSrcQueries_Object = MibTableColumn
vRtrMldHostTxGrpSrcQueries = _VRtrMldHostTxGrpSrcQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 2, 1, 3),
    _VRtrMldHostTxGrpSrcQueries_Type()
)
vRtrMldHostTxGrpSrcQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldHostTxGrpSrcQueries.setStatus("current")
_VRtrMldHostTxV1Reports_Type = Counter32
_VRtrMldHostTxV1Reports_Object = MibTableColumn
vRtrMldHostTxV1Reports = _VRtrMldHostTxV1Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 2, 1, 4),
    _VRtrMldHostTxV1Reports_Type()
)
vRtrMldHostTxV1Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldHostTxV1Reports.setStatus("current")
_VRtrMldHostTxV2Reports_Type = Counter32
_VRtrMldHostTxV2Reports_Object = MibTableColumn
vRtrMldHostTxV2Reports = _VRtrMldHostTxV2Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 2, 1, 5),
    _VRtrMldHostTxV2Reports_Type()
)
vRtrMldHostTxV2Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldHostTxV2Reports.setStatus("current")
_VRtrMldHostTxLeaves_Type = Counter32
_VRtrMldHostTxLeaves_Object = MibTableColumn
vRtrMldHostTxLeaves = _VRtrMldHostTxLeaves_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 2, 1, 6),
    _VRtrMldHostTxLeaves_Type()
)
vRtrMldHostTxLeaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldHostTxLeaves.setStatus("current")
_VRtrMldHostTxErrors_Type = Counter32
_VRtrMldHostTxErrors_Object = MibTableColumn
vRtrMldHostTxErrors = _VRtrMldHostTxErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 2, 1, 7),
    _VRtrMldHostTxErrors_Type()
)
vRtrMldHostTxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldHostTxErrors.setStatus("current")
_VRtrMldHostRxGenQueries_Type = Counter32
_VRtrMldHostRxGenQueries_Object = MibTableColumn
vRtrMldHostRxGenQueries = _VRtrMldHostRxGenQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 2, 1, 8),
    _VRtrMldHostRxGenQueries_Type()
)
vRtrMldHostRxGenQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldHostRxGenQueries.setStatus("current")
_VRtrMldHostRxGrpQueries_Type = Counter32
_VRtrMldHostRxGrpQueries_Object = MibTableColumn
vRtrMldHostRxGrpQueries = _VRtrMldHostRxGrpQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 2, 1, 9),
    _VRtrMldHostRxGrpQueries_Type()
)
vRtrMldHostRxGrpQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldHostRxGrpQueries.setStatus("current")
_VRtrMldHostRxGrpSrcQueries_Type = Counter32
_VRtrMldHostRxGrpSrcQueries_Object = MibTableColumn
vRtrMldHostRxGrpSrcQueries = _VRtrMldHostRxGrpSrcQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 2, 1, 10),
    _VRtrMldHostRxGrpSrcQueries_Type()
)
vRtrMldHostRxGrpSrcQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldHostRxGrpSrcQueries.setStatus("current")
_VRtrMldHostRxV1Reports_Type = Counter32
_VRtrMldHostRxV1Reports_Object = MibTableColumn
vRtrMldHostRxV1Reports = _VRtrMldHostRxV1Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 2, 1, 11),
    _VRtrMldHostRxV1Reports_Type()
)
vRtrMldHostRxV1Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldHostRxV1Reports.setStatus("current")
_VRtrMldHostRxV2Reports_Type = Counter32
_VRtrMldHostRxV2Reports_Object = MibTableColumn
vRtrMldHostRxV2Reports = _VRtrMldHostRxV2Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 2, 1, 12),
    _VRtrMldHostRxV2Reports_Type()
)
vRtrMldHostRxV2Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldHostRxV2Reports.setStatus("current")
_VRtrMldHostRxLeaves_Type = Counter32
_VRtrMldHostRxLeaves_Object = MibTableColumn
vRtrMldHostRxLeaves = _VRtrMldHostRxLeaves_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 2, 1, 13),
    _VRtrMldHostRxLeaves_Type()
)
vRtrMldHostRxLeaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldHostRxLeaves.setStatus("current")
_VRtrMldHostRxBadLenPkts_Type = Counter32
_VRtrMldHostRxBadLenPkts_Object = MibTableColumn
vRtrMldHostRxBadLenPkts = _VRtrMldHostRxBadLenPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 2, 1, 14),
    _VRtrMldHostRxBadLenPkts_Type()
)
vRtrMldHostRxBadLenPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldHostRxBadLenPkts.setStatus("current")
_VRtrMldHostRxBadChecksumPkts_Type = Counter32
_VRtrMldHostRxBadChecksumPkts_Object = MibTableColumn
vRtrMldHostRxBadChecksumPkts = _VRtrMldHostRxBadChecksumPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 2, 1, 15),
    _VRtrMldHostRxBadChecksumPkts_Type()
)
vRtrMldHostRxBadChecksumPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldHostRxBadChecksumPkts.setStatus("current")
_VRtrMldHostRxUnknownTypePkts_Type = Counter32
_VRtrMldHostRxUnknownTypePkts_Object = MibTableColumn
vRtrMldHostRxUnknownTypePkts = _VRtrMldHostRxUnknownTypePkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 2, 1, 16),
    _VRtrMldHostRxUnknownTypePkts_Type()
)
vRtrMldHostRxUnknownTypePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldHostRxUnknownTypePkts.setStatus("current")
_VRtrMldHostRxBadReceiveIfPkts_Type = Counter32
_VRtrMldHostRxBadReceiveIfPkts_Object = MibTableColumn
vRtrMldHostRxBadReceiveIfPkts = _VRtrMldHostRxBadReceiveIfPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 2, 1, 17),
    _VRtrMldHostRxBadReceiveIfPkts_Type()
)
vRtrMldHostRxBadReceiveIfPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldHostRxBadReceiveIfPkts.setStatus("current")
_VRtrMldHostRxNonLocal_Type = Counter32
_VRtrMldHostRxNonLocal_Object = MibTableColumn
vRtrMldHostRxNonLocal = _VRtrMldHostRxNonLocal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 2, 1, 18),
    _VRtrMldHostRxNonLocal_Type()
)
vRtrMldHostRxNonLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldHostRxNonLocal.setStatus("current")
_VRtrMldHostRxWrongVersions_Type = Counter32
_VRtrMldHostRxWrongVersions_Object = MibTableColumn
vRtrMldHostRxWrongVersions = _VRtrMldHostRxWrongVersions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 2, 1, 19),
    _VRtrMldHostRxWrongVersions_Type()
)
vRtrMldHostRxWrongVersions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldHostRxWrongVersions.setStatus("current")
_VRtrMldHostImportPolicyDrops_Type = Counter32
_VRtrMldHostImportPolicyDrops_Object = MibTableColumn
vRtrMldHostImportPolicyDrops = _VRtrMldHostImportPolicyDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 2, 1, 20),
    _VRtrMldHostImportPolicyDrops_Type()
)
vRtrMldHostImportPolicyDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldHostImportPolicyDrops.setStatus("current")
_VRtrMldHostRxNoRtrAlertPkts_Type = Counter32
_VRtrMldHostRxNoRtrAlertPkts_Object = MibTableColumn
vRtrMldHostRxNoRtrAlertPkts = _VRtrMldHostRxNoRtrAlertPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 2, 1, 21),
    _VRtrMldHostRxNoRtrAlertPkts_Type()
)
vRtrMldHostRxNoRtrAlertPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldHostRxNoRtrAlertPkts.setStatus("current")
_VRtrMldHostRxBadEncodings_Type = Counter32
_VRtrMldHostRxBadEncodings_Object = MibTableColumn
vRtrMldHostRxBadEncodings = _VRtrMldHostRxBadEncodings_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 2, 1, 22),
    _VRtrMldHostRxBadEncodings_Type()
)
vRtrMldHostRxBadEncodings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldHostRxBadEncodings.setStatus("current")
_VRtrMldHostRxPktDrops_Type = Counter32
_VRtrMldHostRxPktDrops_Object = MibTableColumn
vRtrMldHostRxPktDrops = _VRtrMldHostRxPktDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 2, 1, 23),
    _VRtrMldHostRxPktDrops_Type()
)
vRtrMldHostRxPktDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldHostRxPktDrops.setStatus("current")
_VRtrMldHostStatsStarGTypes_Type = Gauge32
_VRtrMldHostStatsStarGTypes_Object = MibTableColumn
vRtrMldHostStatsStarGTypes = _VRtrMldHostStatsStarGTypes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 2, 1, 24),
    _VRtrMldHostStatsStarGTypes_Type()
)
vRtrMldHostStatsStarGTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldHostStatsStarGTypes.setStatus("current")
_VRtrMldHostStatsSGTypes_Type = Gauge32
_VRtrMldHostStatsSGTypes_Object = MibTableColumn
vRtrMldHostStatsSGTypes = _VRtrMldHostStatsSGTypes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 2, 1, 25),
    _VRtrMldHostStatsSGTypes_Type()
)
vRtrMldHostStatsSGTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldHostStatsSGTypes.setStatus("current")
_VRtrMldHostStatsMcacPolicyDrops_Type = Counter32
_VRtrMldHostStatsMcacPolicyDrops_Object = MibTableColumn
vRtrMldHostStatsMcacPolicyDrops = _VRtrMldHostStatsMcacPolicyDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 2, 1, 26),
    _VRtrMldHostStatsMcacPolicyDrops_Type()
)
vRtrMldHostStatsMcacPolicyDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldHostStatsMcacPolicyDrops.setStatus("current")
_VRtrMldHostRxLocalScopePkts_Type = Counter32
_VRtrMldHostRxLocalScopePkts_Object = MibTableColumn
vRtrMldHostRxLocalScopePkts = _VRtrMldHostRxLocalScopePkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 2, 1, 27),
    _VRtrMldHostRxLocalScopePkts_Type()
)
vRtrMldHostRxLocalScopePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldHostRxLocalScopePkts.setStatus("current")
_VRtrMldHostRxRsvdScopePkts_Type = Counter32
_VRtrMldHostRxRsvdScopePkts_Object = MibTableColumn
vRtrMldHostRxRsvdScopePkts = _VRtrMldHostRxRsvdScopePkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 2, 1, 28),
    _VRtrMldHostRxRsvdScopePkts_Type()
)
vRtrMldHostRxRsvdScopePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldHostRxRsvdScopePkts.setStatus("current")
_VRtrMldHostRedirectionDrops_Type = Counter32
_VRtrMldHostRedirectionDrops_Object = MibTableColumn
vRtrMldHostRedirectionDrops = _VRtrMldHostRedirectionDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 2, 1, 29),
    _VRtrMldHostRedirectionDrops_Type()
)
vRtrMldHostRedirectionDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldHostRedirectionDrops.setStatus("current")
_VRtrMldGrpIfTable_Object = MibTable
vRtrMldGrpIfTable = _VRtrMldGrpIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 3)
)
if mibBuilder.loadTexts:
    vRtrMldGrpIfTable.setStatus("current")
_VRtrMldGrpIfEntry_Object = MibTableRow
vRtrMldGrpIfEntry = _VRtrMldGrpIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 3, 1)
)
vRtrMldGrpIfEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-IGMP-MIB", "vRtrIfFwdSvcId"),
    (0, "TIMETRA-VRTR-MIB", "vRtrIfIndex"),
)
if mibBuilder.loadTexts:
    vRtrMldGrpIfEntry.setStatus("current")
_VRtrMldGrpIfRowStatus_Type = RowStatus
_VRtrMldGrpIfRowStatus_Object = MibTableColumn
vRtrMldGrpIfRowStatus = _VRtrMldGrpIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 3, 1, 1),
    _VRtrMldGrpIfRowStatus_Type()
)
vRtrMldGrpIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMldGrpIfRowStatus.setStatus("current")
_VRtrMldGrpIfLastChangeTime_Type = TimeStamp
_VRtrMldGrpIfLastChangeTime_Object = MibTableColumn
vRtrMldGrpIfLastChangeTime = _VRtrMldGrpIfLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 3, 1, 2),
    _VRtrMldGrpIfLastChangeTime_Type()
)
vRtrMldGrpIfLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldGrpIfLastChangeTime.setStatus("current")


class _VRtrMldGrpIfAdminState_Type(TmnxAdminState):
    """Custom type vRtrMldGrpIfAdminState based on TmnxAdminState"""
    defaultValue = 2


_VRtrMldGrpIfAdminState_Type.__name__ = "TmnxAdminState"
_VRtrMldGrpIfAdminState_Object = MibTableColumn
vRtrMldGrpIfAdminState = _VRtrMldGrpIfAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 3, 1, 3),
    _VRtrMldGrpIfAdminState_Type()
)
vRtrMldGrpIfAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMldGrpIfAdminState.setStatus("current")
_VRtrMldGrpIfOperState_Type = TmnxOperState
_VRtrMldGrpIfOperState_Object = MibTableColumn
vRtrMldGrpIfOperState = _VRtrMldGrpIfOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 3, 1, 4),
    _VRtrMldGrpIfOperState_Type()
)
vRtrMldGrpIfOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldGrpIfOperState.setStatus("current")


class _VRtrMldGrpIfSubHostsOnly_Type(TruthValue):
    """Custom type vRtrMldGrpIfSubHostsOnly based on TruthValue"""
    defaultValue = 1


_VRtrMldGrpIfSubHostsOnly_Type.__name__ = "TruthValue"
_VRtrMldGrpIfSubHostsOnly_Object = MibTableColumn
vRtrMldGrpIfSubHostsOnly = _VRtrMldGrpIfSubHostsOnly_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 3, 1, 5),
    _VRtrMldGrpIfSubHostsOnly_Type()
)
vRtrMldGrpIfSubHostsOnly.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMldGrpIfSubHostsOnly.setStatus("current")


class _VRtrMldGrpIfAdminVersion_Type(TmnxMldVersion):
    """Custom type vRtrMldGrpIfAdminVersion based on TmnxMldVersion"""
    defaultValue = 2


_VRtrMldGrpIfAdminVersion_Type.__name__ = "TmnxMldVersion"
_VRtrMldGrpIfAdminVersion_Object = MibTableColumn
vRtrMldGrpIfAdminVersion = _VRtrMldGrpIfAdminVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 3, 1, 6),
    _VRtrMldGrpIfAdminVersion_Type()
)
vRtrMldGrpIfAdminVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMldGrpIfAdminVersion.setStatus("current")


class _VRtrMldGrpIfImportPolicy_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrMldGrpIfImportPolicy based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrMldGrpIfImportPolicy_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrMldGrpIfImportPolicy_Object = MibTableColumn
vRtrMldGrpIfImportPolicy = _VRtrMldGrpIfImportPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 3, 1, 7),
    _VRtrMldGrpIfImportPolicy_Type()
)
vRtrMldGrpIfImportPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMldGrpIfImportPolicy.setStatus("current")


class _VRtrMldGrpIfSubnetCheck_Type(TruthValue):
    """Custom type vRtrMldGrpIfSubnetCheck based on TruthValue"""
    defaultValue = 1


_VRtrMldGrpIfSubnetCheck_Type.__name__ = "TruthValue"
_VRtrMldGrpIfSubnetCheck_Object = MibTableColumn
vRtrMldGrpIfSubnetCheck = _VRtrMldGrpIfSubnetCheck_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 3, 1, 8),
    _VRtrMldGrpIfSubnetCheck_Type()
)
vRtrMldGrpIfSubnetCheck.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMldGrpIfSubnetCheck.setStatus("current")


class _VRtrMldGrpIfMcacPolicyName_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrMldGrpIfMcacPolicyName based on TPolicyStatementNameOrEmpty"""
    defaultValue = OctetString("")


_VRtrMldGrpIfMcacPolicyName_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrMldGrpIfMcacPolicyName_Object = MibTableColumn
vRtrMldGrpIfMcacPolicyName = _VRtrMldGrpIfMcacPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 3, 1, 9),
    _VRtrMldGrpIfMcacPolicyName_Type()
)
vRtrMldGrpIfMcacPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMldGrpIfMcacPolicyName.setStatus("current")


class _VRtrMldGrpIfMcacUnconstrainedBW_Type(Integer32):
    """Custom type vRtrMldGrpIfMcacUnconstrainedBW based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_VRtrMldGrpIfMcacUnconstrainedBW_Type.__name__ = "Integer32"
_VRtrMldGrpIfMcacUnconstrainedBW_Object = MibTableColumn
vRtrMldGrpIfMcacUnconstrainedBW = _VRtrMldGrpIfMcacUnconstrainedBW_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 3, 1, 10),
    _VRtrMldGrpIfMcacUnconstrainedBW_Type()
)
vRtrMldGrpIfMcacUnconstrainedBW.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMldGrpIfMcacUnconstrainedBW.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMldGrpIfMcacUnconstrainedBW.setUnits("kbps")


class _VRtrMldGrpIfMcacConstAdminState_Type(TmnxAdminState):
    """Custom type vRtrMldGrpIfMcacConstAdminState based on TmnxAdminState"""
    defaultValue = 2


_VRtrMldGrpIfMcacConstAdminState_Type.__name__ = "TmnxAdminState"
_VRtrMldGrpIfMcacConstAdminState_Object = MibTableColumn
vRtrMldGrpIfMcacConstAdminState = _VRtrMldGrpIfMcacConstAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 3, 1, 11),
    _VRtrMldGrpIfMcacConstAdminState_Type()
)
vRtrMldGrpIfMcacConstAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMldGrpIfMcacConstAdminState.setStatus("current")


class _VRtrMldGrpIfMcacPreRsvdMandBW_Type(Integer32):
    """Custom type vRtrMldGrpIfMcacPreRsvdMandBW based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_VRtrMldGrpIfMcacPreRsvdMandBW_Type.__name__ = "Integer32"
_VRtrMldGrpIfMcacPreRsvdMandBW_Object = MibTableColumn
vRtrMldGrpIfMcacPreRsvdMandBW = _VRtrMldGrpIfMcacPreRsvdMandBW_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 3, 1, 12),
    _VRtrMldGrpIfMcacPreRsvdMandBW_Type()
)
vRtrMldGrpIfMcacPreRsvdMandBW.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMldGrpIfMcacPreRsvdMandBW.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMldGrpIfMcacPreRsvdMandBW.setUnits("kbps")
_VRtrMldGrpIfMcacinUseMandBw_Type = Unsigned32
_VRtrMldGrpIfMcacinUseMandBw_Object = MibTableColumn
vRtrMldGrpIfMcacinUseMandBw = _VRtrMldGrpIfMcacinUseMandBw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 3, 1, 13),
    _VRtrMldGrpIfMcacinUseMandBw_Type()
)
vRtrMldGrpIfMcacinUseMandBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldGrpIfMcacinUseMandBw.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMldGrpIfMcacinUseMandBw.setUnits("kbps")
_VRtrMldGrpIfMcacinUseOpnlBw_Type = Unsigned32
_VRtrMldGrpIfMcacinUseOpnlBw_Object = MibTableColumn
vRtrMldGrpIfMcacinUseOpnlBw = _VRtrMldGrpIfMcacinUseOpnlBw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 3, 1, 14),
    _VRtrMldGrpIfMcacinUseOpnlBw_Type()
)
vRtrMldGrpIfMcacinUseOpnlBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldGrpIfMcacinUseOpnlBw.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMldGrpIfMcacinUseOpnlBw.setUnits("kbps")
_VRtrMldGrpIfMcacAvailMandBw_Type = Unsigned32
_VRtrMldGrpIfMcacAvailMandBw_Object = MibTableColumn
vRtrMldGrpIfMcacAvailMandBw = _VRtrMldGrpIfMcacAvailMandBw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 3, 1, 15),
    _VRtrMldGrpIfMcacAvailMandBw_Type()
)
vRtrMldGrpIfMcacAvailMandBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldGrpIfMcacAvailMandBw.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMldGrpIfMcacAvailMandBw.setUnits("kbps")
_VRtrMldGrpIfMcacAvailOpnlBw_Type = Unsigned32
_VRtrMldGrpIfMcacAvailOpnlBw_Object = MibTableColumn
vRtrMldGrpIfMcacAvailOpnlBw = _VRtrMldGrpIfMcacAvailOpnlBw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 3, 1, 16),
    _VRtrMldGrpIfMcacAvailOpnlBw_Type()
)
vRtrMldGrpIfMcacAvailOpnlBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldGrpIfMcacAvailOpnlBw.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMldGrpIfMcacAvailOpnlBw.setUnits("kbps")
_VRtrMldGrpIfMcacValuesInTransit_Type = TruthValue
_VRtrMldGrpIfMcacValuesInTransit_Object = MibTableColumn
vRtrMldGrpIfMcacValuesInTransit = _VRtrMldGrpIfMcacValuesInTransit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 3, 1, 17),
    _VRtrMldGrpIfMcacValuesInTransit_Type()
)
vRtrMldGrpIfMcacValuesInTransit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldGrpIfMcacValuesInTransit.setStatus("current")


class _VRtrMldGrpIfDisRtrAlertChk_Type(TruthValue):
    """Custom type vRtrMldGrpIfDisRtrAlertChk based on TruthValue"""
    defaultValue = 2


_VRtrMldGrpIfDisRtrAlertChk_Type.__name__ = "TruthValue"
_VRtrMldGrpIfDisRtrAlertChk_Object = MibTableColumn
vRtrMldGrpIfDisRtrAlertChk = _VRtrMldGrpIfDisRtrAlertChk_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 3, 1, 18),
    _VRtrMldGrpIfDisRtrAlertChk_Type()
)
vRtrMldGrpIfDisRtrAlertChk.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMldGrpIfDisRtrAlertChk.setStatus("current")


class _VRtrMldGrpIfMaxGroups_Type(Unsigned32):
    """Custom type vRtrMldGrpIfMaxGroups based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 16000),
    )


_VRtrMldGrpIfMaxGroups_Type.__name__ = "Unsigned32"
_VRtrMldGrpIfMaxGroups_Object = MibTableColumn
vRtrMldGrpIfMaxGroups = _VRtrMldGrpIfMaxGroups_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 3, 1, 19),
    _VRtrMldGrpIfMaxGroups_Type()
)
vRtrMldGrpIfMaxGroups.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMldGrpIfMaxGroups.setStatus("current")


class _VRtrMldGrpIfMaxSources_Type(Unsigned32):
    """Custom type vRtrMldGrpIfMaxSources based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1000),
    )


_VRtrMldGrpIfMaxSources_Type.__name__ = "Unsigned32"
_VRtrMldGrpIfMaxSources_Object = MibTableColumn
vRtrMldGrpIfMaxSources = _VRtrMldGrpIfMaxSources_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 3, 1, 20),
    _VRtrMldGrpIfMaxSources_Type()
)
vRtrMldGrpIfMaxSources.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMldGrpIfMaxSources.setStatus("current")


class _VRtrMldGrpIfMaxGrpSources_Type(Unsigned32):
    """Custom type vRtrMldGrpIfMaxGrpSources based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 32000),
    )


_VRtrMldGrpIfMaxGrpSources_Type.__name__ = "Unsigned32"
_VRtrMldGrpIfMaxGrpSources_Object = MibTableColumn
vRtrMldGrpIfMaxGrpSources = _VRtrMldGrpIfMaxGrpSources_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 3, 1, 21),
    _VRtrMldGrpIfMaxGrpSources_Type()
)
vRtrMldGrpIfMaxGrpSources.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMldGrpIfMaxGrpSources.setStatus("current")
_VRtrMldGrpIfQrySrcIpAddrType_Type = InetAddressType
_VRtrMldGrpIfQrySrcIpAddrType_Object = MibTableColumn
vRtrMldGrpIfQrySrcIpAddrType = _VRtrMldGrpIfQrySrcIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 3, 1, 22),
    _VRtrMldGrpIfQrySrcIpAddrType_Type()
)
vRtrMldGrpIfQrySrcIpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMldGrpIfQrySrcIpAddrType.setStatus("current")


class _VRtrMldGrpIfQrySrcIpAddr_Type(InetAddress):
    """Custom type vRtrMldGrpIfQrySrcIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_VRtrMldGrpIfQrySrcIpAddr_Type.__name__ = "InetAddress"
_VRtrMldGrpIfQrySrcIpAddr_Object = MibTableColumn
vRtrMldGrpIfQrySrcIpAddr = _VRtrMldGrpIfQrySrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 3, 1, 23),
    _VRtrMldGrpIfQrySrcIpAddr_Type()
)
vRtrMldGrpIfQrySrcIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMldGrpIfQrySrcIpAddr.setStatus("current")
_VRtrMldGrpIfHostGrpTable_Object = MibTable
vRtrMldGrpIfHostGrpTable = _VRtrMldGrpIfHostGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 4)
)
if mibBuilder.loadTexts:
    vRtrMldGrpIfHostGrpTable.setStatus("current")
_VRtrMldGrpIfHostGrpEntry_Object = MibTableRow
vRtrMldGrpIfHostGrpEntry = _VRtrMldGrpIfHostGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 4, 1)
)
vRtrMldGrpIfHostGrpEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-IGMP-MIB", "vRtrIfFwdSvcId"),
    (0, "TIMETRA-IGMP-MIB", "vRtrGrpIfIndex"),
    (0, "TIMETRA-MLD-MIB", "vRtrMldHostAddressType"),
    (0, "TIMETRA-MLD-MIB", "vRtrMldHostAddress"),
    (0, "TIMETRA-MLD-MIB", "vRtrMldHostMacAddress"),
    (0, "TIMETRA-MLD-MIB", "vRtrMldHostPppoeSessionId"),
    (0, "TIMETRA-MLD-MIB", "vRtrMldHostGroupAddressType"),
    (0, "TIMETRA-MLD-MIB", "vRtrMldHostGroupAddress"),
)
if mibBuilder.loadTexts:
    vRtrMldGrpIfHostGrpEntry.setStatus("current")
_VRtrMldHostGroupAddressType_Type = InetAddressType
_VRtrMldHostGroupAddressType_Object = MibTableColumn
vRtrMldHostGroupAddressType = _VRtrMldHostGroupAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 4, 1, 1),
    _VRtrMldHostGroupAddressType_Type()
)
vRtrMldHostGroupAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMldHostGroupAddressType.setStatus("current")


class _VRtrMldHostGroupAddress_Type(InetAddress):
    """Custom type vRtrMldHostGroupAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_VRtrMldHostGroupAddress_Type.__name__ = "InetAddress"
_VRtrMldHostGroupAddress_Object = MibTableColumn
vRtrMldHostGroupAddress = _VRtrMldHostGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 4, 1, 2),
    _VRtrMldHostGroupAddress_Type()
)
vRtrMldHostGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMldHostGroupAddress.setStatus("current")
_VRtrMldGrpIfHostGrpType_Type = TmnxMldGroupType
_VRtrMldGrpIfHostGrpType_Object = MibTableColumn
vRtrMldGrpIfHostGrpType = _VRtrMldGrpIfHostGrpType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 4, 1, 3),
    _VRtrMldGrpIfHostGrpType_Type()
)
vRtrMldGrpIfHostGrpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldGrpIfHostGrpType.setStatus("current")
_VRtrMldGrpIfHostGrpUpTime_Type = Unsigned32
_VRtrMldGrpIfHostGrpUpTime_Object = MibTableColumn
vRtrMldGrpIfHostGrpUpTime = _VRtrMldGrpIfHostGrpUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 4, 1, 4),
    _VRtrMldGrpIfHostGrpUpTime_Type()
)
vRtrMldGrpIfHostGrpUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldGrpIfHostGrpUpTime.setStatus("current")
_VRtrMldGrpIfHostGrpExpiryTime_Type = Unsigned32
_VRtrMldGrpIfHostGrpExpiryTime_Object = MibTableColumn
vRtrMldGrpIfHostGrpExpiryTime = _VRtrMldGrpIfHostGrpExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 4, 1, 5),
    _VRtrMldGrpIfHostGrpExpiryTime_Type()
)
vRtrMldGrpIfHostGrpExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldGrpIfHostGrpExpiryTime.setStatus("current")
_VRtrMldGrpIfHostGrpVer1HostTmr_Type = Unsigned32
_VRtrMldGrpIfHostGrpVer1HostTmr_Object = MibTableColumn
vRtrMldGrpIfHostGrpVer1HostTmr = _VRtrMldGrpIfHostGrpVer1HostTmr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 4, 1, 6),
    _VRtrMldGrpIfHostGrpVer1HostTmr_Type()
)
vRtrMldGrpIfHostGrpVer1HostTmr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldGrpIfHostGrpVer1HostTmr.setStatus("current")
_VRtrMldGrpIfHostGrpMode_Type = TmnxMldGroupFilterMode
_VRtrMldGrpIfHostGrpMode_Object = MibTableColumn
vRtrMldGrpIfHostGrpMode = _VRtrMldGrpIfHostGrpMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 4, 1, 7),
    _VRtrMldGrpIfHostGrpMode_Type()
)
vRtrMldGrpIfHostGrpMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldGrpIfHostGrpMode.setStatus("current")
_VRtrMldGrpIfHostGrpCompatMode_Type = TmnxMldVersion
_VRtrMldGrpIfHostGrpCompatMode_Object = MibTableColumn
vRtrMldGrpIfHostGrpCompatMode = _VRtrMldGrpIfHostGrpCompatMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 4, 1, 8),
    _VRtrMldGrpIfHostGrpCompatMode_Type()
)
vRtrMldGrpIfHostGrpCompatMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldGrpIfHostGrpCompatMode.setStatus("current")
_VRtrMldGrpIfHostGrpMRDstVrId_Type = TmnxVRtrID
_VRtrMldGrpIfHostGrpMRDstVrId_Object = MibTableColumn
vRtrMldGrpIfHostGrpMRDstVrId = _VRtrMldGrpIfHostGrpMRDstVrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 4, 1, 9),
    _VRtrMldGrpIfHostGrpMRDstVrId_Type()
)
vRtrMldGrpIfHostGrpMRDstVrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldGrpIfHostGrpMRDstVrId.setStatus("current")
_VRtrMldGrpIfHostGrpMRDstIfId_Type = InterfaceIndex
_VRtrMldGrpIfHostGrpMRDstIfId_Object = MibTableColumn
vRtrMldGrpIfHostGrpMRDstIfId = _VRtrMldGrpIfHostGrpMRDstIfId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 4, 1, 10),
    _VRtrMldGrpIfHostGrpMRDstIfId_Type()
)
vRtrMldGrpIfHostGrpMRDstIfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldGrpIfHostGrpMRDstIfId.setStatus("current")
_VRtrMldGrpIfHostGrpSrcTable_Object = MibTable
vRtrMldGrpIfHostGrpSrcTable = _VRtrMldGrpIfHostGrpSrcTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 5)
)
if mibBuilder.loadTexts:
    vRtrMldGrpIfHostGrpSrcTable.setStatus("current")
_VRtrMldGrpIfHostGrpSrcEntry_Object = MibTableRow
vRtrMldGrpIfHostGrpSrcEntry = _VRtrMldGrpIfHostGrpSrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 5, 1)
)
vRtrMldGrpIfHostGrpSrcEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-IGMP-MIB", "vRtrIfFwdSvcId"),
    (0, "TIMETRA-IGMP-MIB", "vRtrGrpIfIndex"),
    (0, "TIMETRA-MLD-MIB", "vRtrMldHostAddressType"),
    (0, "TIMETRA-MLD-MIB", "vRtrMldHostAddress"),
    (0, "TIMETRA-MLD-MIB", "vRtrMldHostMacAddress"),
    (0, "TIMETRA-MLD-MIB", "vRtrMldHostPppoeSessionId"),
    (0, "TIMETRA-MLD-MIB", "vRtrMldHostGroupAddressType"),
    (0, "TIMETRA-MLD-MIB", "vRtrMldHostGroupAddress"),
    (0, "TIMETRA-MLD-MIB", "vRtrMldHostGrpSrcAddressType"),
    (0, "TIMETRA-MLD-MIB", "vRtrMldHostGrpSrcAddress"),
)
if mibBuilder.loadTexts:
    vRtrMldGrpIfHostGrpSrcEntry.setStatus("current")
_VRtrMldHostGrpSrcAddressType_Type = InetAddressType
_VRtrMldHostGrpSrcAddressType_Object = MibTableColumn
vRtrMldHostGrpSrcAddressType = _VRtrMldHostGrpSrcAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 5, 1, 1),
    _VRtrMldHostGrpSrcAddressType_Type()
)
vRtrMldHostGrpSrcAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMldHostGrpSrcAddressType.setStatus("current")


class _VRtrMldHostGrpSrcAddress_Type(InetAddress):
    """Custom type vRtrMldHostGrpSrcAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_VRtrMldHostGrpSrcAddress_Type.__name__ = "InetAddress"
_VRtrMldHostGrpSrcAddress_Object = MibTableColumn
vRtrMldHostGrpSrcAddress = _VRtrMldHostGrpSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 5, 1, 2),
    _VRtrMldHostGrpSrcAddress_Type()
)
vRtrMldHostGrpSrcAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMldHostGrpSrcAddress.setStatus("current")
_VRtrMldGrpIfHostGrpSrcExpTime_Type = Unsigned32
_VRtrMldGrpIfHostGrpSrcExpTime_Object = MibTableColumn
vRtrMldGrpIfHostGrpSrcExpTime = _VRtrMldGrpIfHostGrpSrcExpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 5, 1, 3),
    _VRtrMldGrpIfHostGrpSrcExpTime_Type()
)
vRtrMldGrpIfHostGrpSrcExpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldGrpIfHostGrpSrcExpTime.setStatus("current")
_VRtrMldGrpIfHostGrpSrcType_Type = TmnxMldGroupType
_VRtrMldGrpIfHostGrpSrcType_Object = MibTableColumn
vRtrMldGrpIfHostGrpSrcType = _VRtrMldGrpIfHostGrpSrcType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 5, 1, 4),
    _VRtrMldGrpIfHostGrpSrcType_Type()
)
vRtrMldGrpIfHostGrpSrcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldGrpIfHostGrpSrcType.setStatus("current")
_VRtrMldGrpIfHostGrpSrcMRDstVrId_Type = TmnxVRtrID
_VRtrMldGrpIfHostGrpSrcMRDstVrId_Object = MibTableColumn
vRtrMldGrpIfHostGrpSrcMRDstVrId = _VRtrMldGrpIfHostGrpSrcMRDstVrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 5, 1, 5),
    _VRtrMldGrpIfHostGrpSrcMRDstVrId_Type()
)
vRtrMldGrpIfHostGrpSrcMRDstVrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldGrpIfHostGrpSrcMRDstVrId.setStatus("current")
_VRtrMldGrpIfHostGrpSrcMRDstIfId_Type = InterfaceIndex
_VRtrMldGrpIfHostGrpSrcMRDstIfId_Object = MibTableColumn
vRtrMldGrpIfHostGrpSrcMRDstIfId = _VRtrMldGrpIfHostGrpSrcMRDstIfId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 5, 1, 6),
    _VRtrMldGrpIfHostGrpSrcMRDstIfId_Type()
)
vRtrMldGrpIfHostGrpSrcMRDstIfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldGrpIfHostGrpSrcMRDstIfId.setStatus("current")
_VRtrMldGrpSrcHostTable_Object = MibTable
vRtrMldGrpSrcHostTable = _VRtrMldGrpSrcHostTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 6)
)
if mibBuilder.loadTexts:
    vRtrMldGrpSrcHostTable.setStatus("current")
_VRtrMldGrpSrcHostEntry_Object = MibTableRow
vRtrMldGrpSrcHostEntry = _VRtrMldGrpSrcHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 6, 1)
)
vRtrMldGrpSrcHostEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MLD-MIB", "vRtrMldGrpSrcGroupAddrType"),
    (0, "TIMETRA-MLD-MIB", "vRtrMldGrpSrcGroupAddress"),
    (0, "TIMETRA-MLD-MIB", "vRtrMldGrpSrcSourceAddrType"),
    (0, "TIMETRA-MLD-MIB", "vRtrMldGrpSrcSourceAddress"),
    (0, "TIMETRA-MLD-MIB", "vRtrMldGrpSrcFwdOrBlk"),
    (0, "TIMETRA-MLD-MIB", "vRtrMldHostAddressType"),
    (0, "TIMETRA-MLD-MIB", "vRtrMldHostAddress"),
    (0, "TIMETRA-MLD-MIB", "vRtrMldHostMacAddress"),
    (0, "TIMETRA-MLD-MIB", "vRtrMldHostPppoeSessionId"),
)
if mibBuilder.loadTexts:
    vRtrMldGrpSrcHostEntry.setStatus("current")
_VRtrMldGrpSrcHostUpTime_Type = Unsigned32
_VRtrMldGrpSrcHostUpTime_Object = MibTableColumn
vRtrMldGrpSrcHostUpTime = _VRtrMldGrpSrcHostUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 6, 1, 1),
    _VRtrMldGrpSrcHostUpTime_Type()
)
vRtrMldGrpSrcHostUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldGrpSrcHostUpTime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMldGrpSrcHostUpTime.setUnits("seconds")
_VRtrMldHostGrpSrcTable_Object = MibTable
vRtrMldHostGrpSrcTable = _VRtrMldHostGrpSrcTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 7)
)
if mibBuilder.loadTexts:
    vRtrMldHostGrpSrcTable.setStatus("current")
_VRtrMldHostGrpSrcEntry_Object = MibTableRow
vRtrMldHostGrpSrcEntry = _VRtrMldHostGrpSrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 7, 1)
)
vRtrMldHostGrpSrcEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MLD-MIB", "vRtrMldHostAddressType"),
    (0, "TIMETRA-MLD-MIB", "vRtrMldHostAddress"),
    (0, "TIMETRA-MLD-MIB", "vRtrMldHostMacAddress"),
    (0, "TIMETRA-MLD-MIB", "vRtrMldHostPppoeSessionId"),
    (0, "TIMETRA-MLD-MIB", "vRtrMldHostGroupAddressType"),
    (0, "TIMETRA-MLD-MIB", "vRtrMldHostGroupAddress"),
    (0, "TIMETRA-MLD-MIB", "vRtrMldHostGrpSrcAddressType"),
    (0, "TIMETRA-MLD-MIB", "vRtrMldHostGrpSrcAddress"),
)
if mibBuilder.loadTexts:
    vRtrMldHostGrpSrcEntry.setStatus("current")
_VRtrMldHostGrpSrcExpiryTime_Type = Unsigned32
_VRtrMldHostGrpSrcExpiryTime_Object = MibTableColumn
vRtrMldHostGrpSrcExpiryTime = _VRtrMldHostGrpSrcExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 7, 1, 1),
    _VRtrMldHostGrpSrcExpiryTime_Type()
)
vRtrMldHostGrpSrcExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldHostGrpSrcExpiryTime.setStatus("current")
_VRtrMldHostGrpSrcType_Type = TmnxMldGroupType
_VRtrMldHostGrpSrcType_Object = MibTableColumn
vRtrMldHostGrpSrcType = _VRtrMldHostGrpSrcType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 7, 1, 2),
    _VRtrMldHostGrpSrcType_Type()
)
vRtrMldHostGrpSrcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldHostGrpSrcType.setStatus("current")
_VRtrMldHostGrpSrcMcRdrDstVRtrID_Type = TmnxVRtrID
_VRtrMldHostGrpSrcMcRdrDstVRtrID_Object = MibTableColumn
vRtrMldHostGrpSrcMcRdrDstVRtrID = _VRtrMldHostGrpSrcMcRdrDstVRtrID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 7, 1, 3),
    _VRtrMldHostGrpSrcMcRdrDstVRtrID_Type()
)
vRtrMldHostGrpSrcMcRdrDstVRtrID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldHostGrpSrcMcRdrDstVRtrID.setStatus("current")
_VRtrMldHostGrpSrcMcRdrDstIfIdx_Type = InterfaceIndex
_VRtrMldHostGrpSrcMcRdrDstIfIdx_Object = MibTableColumn
vRtrMldHostGrpSrcMcRdrDstIfIdx = _VRtrMldHostGrpSrcMcRdrDstIfIdx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 7, 1, 4),
    _VRtrMldHostGrpSrcMcRdrDstIfIdx_Type()
)
vRtrMldHostGrpSrcMcRdrDstIfIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldHostGrpSrcMcRdrDstIfIdx.setStatus("current")
_VRtrMldHostGrpTable_Object = MibTable
vRtrMldHostGrpTable = _VRtrMldHostGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 8)
)
if mibBuilder.loadTexts:
    vRtrMldHostGrpTable.setStatus("current")
_VRtrMldHostGrpEntry_Object = MibTableRow
vRtrMldHostGrpEntry = _VRtrMldHostGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 8, 1)
)
vRtrMldHostGrpEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MLD-MIB", "vRtrMldHostAddressType"),
    (0, "TIMETRA-MLD-MIB", "vRtrMldHostAddress"),
    (0, "TIMETRA-MLD-MIB", "vRtrMldHostMacAddress"),
    (0, "TIMETRA-MLD-MIB", "vRtrMldHostPppoeSessionId"),
    (0, "TIMETRA-MLD-MIB", "vRtrMldHostGroupAddressType"),
    (0, "TIMETRA-MLD-MIB", "vRtrMldHostGroupAddress"),
)
if mibBuilder.loadTexts:
    vRtrMldHostGrpEntry.setStatus("current")
_VRtrMldHostGrpType_Type = TmnxMldGroupType
_VRtrMldHostGrpType_Object = MibTableColumn
vRtrMldHostGrpType = _VRtrMldHostGrpType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 8, 1, 1),
    _VRtrMldHostGrpType_Type()
)
vRtrMldHostGrpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldHostGrpType.setStatus("current")
_VRtrMldHostGrpUpTime_Type = Unsigned32
_VRtrMldHostGrpUpTime_Object = MibTableColumn
vRtrMldHostGrpUpTime = _VRtrMldHostGrpUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 8, 1, 2),
    _VRtrMldHostGrpUpTime_Type()
)
vRtrMldHostGrpUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldHostGrpUpTime.setStatus("current")
_VRtrMldHostGrpExpiryTime_Type = Unsigned32
_VRtrMldHostGrpExpiryTime_Object = MibTableColumn
vRtrMldHostGrpExpiryTime = _VRtrMldHostGrpExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 8, 1, 3),
    _VRtrMldHostGrpExpiryTime_Type()
)
vRtrMldHostGrpExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldHostGrpExpiryTime.setStatus("current")
_VRtrMldHostGrpVer1HostTmr_Type = Unsigned32
_VRtrMldHostGrpVer1HostTmr_Object = MibTableColumn
vRtrMldHostGrpVer1HostTmr = _VRtrMldHostGrpVer1HostTmr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 8, 1, 4),
    _VRtrMldHostGrpVer1HostTmr_Type()
)
vRtrMldHostGrpVer1HostTmr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldHostGrpVer1HostTmr.setStatus("current")
_VRtrMldHostGrpMode_Type = TmnxMldGroupFilterMode
_VRtrMldHostGrpMode_Object = MibTableColumn
vRtrMldHostGrpMode = _VRtrMldHostGrpMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 8, 1, 5),
    _VRtrMldHostGrpMode_Type()
)
vRtrMldHostGrpMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldHostGrpMode.setStatus("current")
_VRtrMldHostGrpCompatMode_Type = TmnxMldVersion
_VRtrMldHostGrpCompatMode_Object = MibTableColumn
vRtrMldHostGrpCompatMode = _VRtrMldHostGrpCompatMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 8, 1, 6),
    _VRtrMldHostGrpCompatMode_Type()
)
vRtrMldHostGrpCompatMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldHostGrpCompatMode.setStatus("current")
_VRtrMldHostGrpMcRdrDstVrId_Type = TmnxVRtrID
_VRtrMldHostGrpMcRdrDstVrId_Object = MibTableColumn
vRtrMldHostGrpMcRdrDstVrId = _VRtrMldHostGrpMcRdrDstVrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 8, 1, 7),
    _VRtrMldHostGrpMcRdrDstVrId_Type()
)
vRtrMldHostGrpMcRdrDstVrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldHostGrpMcRdrDstVrId.setStatus("current")
_VRtrMldHostGrpMcRdrDstIfId_Type = InterfaceIndex
_VRtrMldHostGrpMcRdrDstIfId_Object = MibTableColumn
vRtrMldHostGrpMcRdrDstIfId = _VRtrMldHostGrpMcRdrDstIfId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 8, 1, 8),
    _VRtrMldHostGrpMcRdrDstIfId_Type()
)
vRtrMldHostGrpMcRdrDstIfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldHostGrpMcRdrDstIfId.setStatus("current")
_VRtrMldGrpIfHostTable_Object = MibTable
vRtrMldGrpIfHostTable = _VRtrMldGrpIfHostTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 9)
)
if mibBuilder.loadTexts:
    vRtrMldGrpIfHostTable.setStatus("current")
_VRtrMldGrpIfHostEntry_Object = MibTableRow
vRtrMldGrpIfHostEntry = _VRtrMldGrpIfHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 9, 1)
)
vRtrMldGrpIfHostEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-IGMP-MIB", "vRtrIfFwdSvcId"),
    (0, "TIMETRA-IGMP-MIB", "vRtrGrpIfIndex"),
    (0, "TIMETRA-MLD-MIB", "vRtrMldHostAddressType"),
    (0, "TIMETRA-MLD-MIB", "vRtrMldHostAddress"),
    (0, "TIMETRA-MLD-MIB", "vRtrMldHostMacAddress"),
    (0, "TIMETRA-MLD-MIB", "vRtrMldHostPppoeSessionId"),
)
if mibBuilder.loadTexts:
    vRtrMldGrpIfHostEntry.setStatus("current")
_VRtrMldGrpIfHostLastChangeTime_Type = TimeStamp
_VRtrMldGrpIfHostLastChangeTime_Object = MibTableColumn
vRtrMldGrpIfHostLastChangeTime = _VRtrMldGrpIfHostLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 9, 1, 1),
    _VRtrMldGrpIfHostLastChangeTime_Type()
)
vRtrMldGrpIfHostLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldGrpIfHostLastChangeTime.setStatus("current")
_VRtrMldGrpIfHostOperState_Type = MldGrpItfOperState
_VRtrMldGrpIfHostOperState_Object = MibTableColumn
vRtrMldGrpIfHostOperState = _VRtrMldGrpIfHostOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 4, 9, 1, 2),
    _VRtrMldGrpIfHostOperState_Type()
)
vRtrMldGrpIfHostOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldGrpIfHostOperState.setStatus("current")
_VRtrMldGrpIfObjs_ObjectIdentity = ObjectIdentity
vRtrMldGrpIfObjs = _VRtrMldGrpIfObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 5)
)
_VRtrMldGrpIfSapTable_Object = MibTable
vRtrMldGrpIfSapTable = _VRtrMldGrpIfSapTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 5, 1)
)
if mibBuilder.loadTexts:
    vRtrMldGrpIfSapTable.setStatus("current")
_VRtrMldGrpIfSapEntry_Object = MibTableRow
vRtrMldGrpIfSapEntry = _VRtrMldGrpIfSapEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 5, 1, 1)
)
vRtrMldGrpIfSapEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-IGMP-MIB", "vRtrIfFwdSvcId"),
    (0, "TIMETRA-IGMP-MIB", "vRtrGrpIfIndex"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
)
if mibBuilder.loadTexts:
    vRtrMldGrpIfSapEntry.setStatus("current")
_VRtrMldGrpIfSapLastChangeTime_Type = TimeStamp
_VRtrMldGrpIfSapLastChangeTime_Object = MibTableColumn
vRtrMldGrpIfSapLastChangeTime = _VRtrMldGrpIfSapLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 5, 1, 1, 1),
    _VRtrMldGrpIfSapLastChangeTime_Type()
)
vRtrMldGrpIfSapLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldGrpIfSapLastChangeTime.setStatus("current")
_VRtrMldGrpIfSapOperState_Type = MldGrpItfOperState
_VRtrMldGrpIfSapOperState_Object = MibTableColumn
vRtrMldGrpIfSapOperState = _VRtrMldGrpIfSapOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 5, 1, 1, 2),
    _VRtrMldGrpIfSapOperState_Type()
)
vRtrMldGrpIfSapOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldGrpIfSapOperState.setStatus("current")


class _VRtrMldGrpIfSapAdminVersion_Type(TmnxMldVersion):
    """Custom type vRtrMldGrpIfSapAdminVersion based on TmnxMldVersion"""
    defaultValue = 2


_VRtrMldGrpIfSapAdminVersion_Type.__name__ = "TmnxMldVersion"
_VRtrMldGrpIfSapAdminVersion_Object = MibTableColumn
vRtrMldGrpIfSapAdminVersion = _VRtrMldGrpIfSapAdminVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 5, 1, 1, 3),
    _VRtrMldGrpIfSapAdminVersion_Type()
)
vRtrMldGrpIfSapAdminVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldGrpIfSapAdminVersion.setStatus("current")
_VRtrMldGrpIfSapOperVersion_Type = TmnxMldVersion
_VRtrMldGrpIfSapOperVersion_Object = MibTableColumn
vRtrMldGrpIfSapOperVersion = _VRtrMldGrpIfSapOperVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 5, 1, 1, 4),
    _VRtrMldGrpIfSapOperVersion_Type()
)
vRtrMldGrpIfSapOperVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldGrpIfSapOperVersion.setStatus("current")
_VRtrMldGrpIfSapGroupCount_Type = Unsigned32
_VRtrMldGrpIfSapGroupCount_Object = MibTableColumn
vRtrMldGrpIfSapGroupCount = _VRtrMldGrpIfSapGroupCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 5, 1, 1, 5),
    _VRtrMldGrpIfSapGroupCount_Type()
)
vRtrMldGrpIfSapGroupCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldGrpIfSapGroupCount.setStatus("current")
_VRtrMldGrpIfSapNextGenQueryTime_Type = Unsigned32
_VRtrMldGrpIfSapNextGenQueryTime_Object = MibTableColumn
vRtrMldGrpIfSapNextGenQueryTime = _VRtrMldGrpIfSapNextGenQueryTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 5, 1, 1, 6),
    _VRtrMldGrpIfSapNextGenQueryTime_Type()
)
vRtrMldGrpIfSapNextGenQueryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldGrpIfSapNextGenQueryTime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMldGrpIfSapNextGenQueryTime.setUnits("seconds")


class _VRtrMldGrpIfSapMaxGroups_Type(Unsigned32):
    """Custom type vRtrMldGrpIfSapMaxGroups based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 16000),
    )


_VRtrMldGrpIfSapMaxGroups_Type.__name__ = "Unsigned32"
_VRtrMldGrpIfSapMaxGroups_Object = MibTableColumn
vRtrMldGrpIfSapMaxGroups = _VRtrMldGrpIfSapMaxGroups_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 5, 1, 1, 7),
    _VRtrMldGrpIfSapMaxGroups_Type()
)
vRtrMldGrpIfSapMaxGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldGrpIfSapMaxGroups.setStatus("current")
_VRtrMldGrpIfSapMaxGroupsTillNow_Type = Counter32
_VRtrMldGrpIfSapMaxGroupsTillNow_Object = MibTableColumn
vRtrMldGrpIfSapMaxGroupsTillNow = _VRtrMldGrpIfSapMaxGroupsTillNow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 5, 1, 1, 8),
    _VRtrMldGrpIfSapMaxGroupsTillNow_Type()
)
vRtrMldGrpIfSapMaxGroupsTillNow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldGrpIfSapMaxGroupsTillNow.setStatus("current")


class _VRtrMldGrpIfSapMaxSources_Type(Unsigned32):
    """Custom type vRtrMldGrpIfSapMaxSources based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1000),
    )


_VRtrMldGrpIfSapMaxSources_Type.__name__ = "Unsigned32"
_VRtrMldGrpIfSapMaxSources_Object = MibTableColumn
vRtrMldGrpIfSapMaxSources = _VRtrMldGrpIfSapMaxSources_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 5, 1, 1, 9),
    _VRtrMldGrpIfSapMaxSources_Type()
)
vRtrMldGrpIfSapMaxSources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldGrpIfSapMaxSources.setStatus("current")


class _VRtrMldGrpIfSapMaxGrpSources_Type(Unsigned32):
    """Custom type vRtrMldGrpIfSapMaxGrpSources based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1000),
    )


_VRtrMldGrpIfSapMaxGrpSources_Type.__name__ = "Unsigned32"
_VRtrMldGrpIfSapMaxGrpSources_Object = MibTableColumn
vRtrMldGrpIfSapMaxGrpSources = _VRtrMldGrpIfSapMaxGrpSources_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 5, 1, 1, 10),
    _VRtrMldGrpIfSapMaxGrpSources_Type()
)
vRtrMldGrpIfSapMaxGrpSources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldGrpIfSapMaxGrpSources.setStatus("current")
_VRtrMldGrpIfSapStatsTable_Object = MibTable
vRtrMldGrpIfSapStatsTable = _VRtrMldGrpIfSapStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 5, 2)
)
if mibBuilder.loadTexts:
    vRtrMldGrpIfSapStatsTable.setStatus("current")
_VRtrMldGrpIfSapStatsEntry_Object = MibTableRow
vRtrMldGrpIfSapStatsEntry = _VRtrMldGrpIfSapStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 5, 2, 1)
)
vRtrMldGrpIfSapStatsEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-IGMP-MIB", "vRtrIfFwdSvcId"),
    (0, "TIMETRA-IGMP-MIB", "vRtrGrpIfIndex"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
)
if mibBuilder.loadTexts:
    vRtrMldGrpIfSapStatsEntry.setStatus("current")
_VRtrMldGrpIfSapTxGenQueries_Type = Counter32
_VRtrMldGrpIfSapTxGenQueries_Object = MibTableColumn
vRtrMldGrpIfSapTxGenQueries = _VRtrMldGrpIfSapTxGenQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 5, 2, 1, 1),
    _VRtrMldGrpIfSapTxGenQueries_Type()
)
vRtrMldGrpIfSapTxGenQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldGrpIfSapTxGenQueries.setStatus("current")
_VRtrMldGrpIfSapTxGrpQueries_Type = Counter32
_VRtrMldGrpIfSapTxGrpQueries_Object = MibTableColumn
vRtrMldGrpIfSapTxGrpQueries = _VRtrMldGrpIfSapTxGrpQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 5, 2, 1, 2),
    _VRtrMldGrpIfSapTxGrpQueries_Type()
)
vRtrMldGrpIfSapTxGrpQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldGrpIfSapTxGrpQueries.setStatus("current")
_VRtrMldGrpIfSapTxGrpSrcQueries_Type = Counter32
_VRtrMldGrpIfSapTxGrpSrcQueries_Object = MibTableColumn
vRtrMldGrpIfSapTxGrpSrcQueries = _VRtrMldGrpIfSapTxGrpSrcQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 5, 2, 1, 3),
    _VRtrMldGrpIfSapTxGrpSrcQueries_Type()
)
vRtrMldGrpIfSapTxGrpSrcQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldGrpIfSapTxGrpSrcQueries.setStatus("current")
_VRtrMldGrpIfSapTxV1Reports_Type = Counter32
_VRtrMldGrpIfSapTxV1Reports_Object = MibTableColumn
vRtrMldGrpIfSapTxV1Reports = _VRtrMldGrpIfSapTxV1Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 5, 2, 1, 4),
    _VRtrMldGrpIfSapTxV1Reports_Type()
)
vRtrMldGrpIfSapTxV1Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldGrpIfSapTxV1Reports.setStatus("current")
_VRtrMldGrpIfSapTxV2Reports_Type = Counter32
_VRtrMldGrpIfSapTxV2Reports_Object = MibTableColumn
vRtrMldGrpIfSapTxV2Reports = _VRtrMldGrpIfSapTxV2Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 5, 2, 1, 5),
    _VRtrMldGrpIfSapTxV2Reports_Type()
)
vRtrMldGrpIfSapTxV2Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldGrpIfSapTxV2Reports.setStatus("current")
_VRtrMldGrpIfSapTxLeaves_Type = Counter32
_VRtrMldGrpIfSapTxLeaves_Object = MibTableColumn
vRtrMldGrpIfSapTxLeaves = _VRtrMldGrpIfSapTxLeaves_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 5, 2, 1, 6),
    _VRtrMldGrpIfSapTxLeaves_Type()
)
vRtrMldGrpIfSapTxLeaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldGrpIfSapTxLeaves.setStatus("current")
_VRtrMldGrpIfSapTxErrors_Type = Counter32
_VRtrMldGrpIfSapTxErrors_Object = MibTableColumn
vRtrMldGrpIfSapTxErrors = _VRtrMldGrpIfSapTxErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 5, 2, 1, 7),
    _VRtrMldGrpIfSapTxErrors_Type()
)
vRtrMldGrpIfSapTxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldGrpIfSapTxErrors.setStatus("current")
_VRtrMldGrpIfSapRxGenQueries_Type = Counter32
_VRtrMldGrpIfSapRxGenQueries_Object = MibTableColumn
vRtrMldGrpIfSapRxGenQueries = _VRtrMldGrpIfSapRxGenQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 5, 2, 1, 8),
    _VRtrMldGrpIfSapRxGenQueries_Type()
)
vRtrMldGrpIfSapRxGenQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldGrpIfSapRxGenQueries.setStatus("current")
_VRtrMldGrpIfSapRxGrpQueries_Type = Counter32
_VRtrMldGrpIfSapRxGrpQueries_Object = MibTableColumn
vRtrMldGrpIfSapRxGrpQueries = _VRtrMldGrpIfSapRxGrpQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 5, 2, 1, 9),
    _VRtrMldGrpIfSapRxGrpQueries_Type()
)
vRtrMldGrpIfSapRxGrpQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldGrpIfSapRxGrpQueries.setStatus("current")
_VRtrMldGrpIfSapRxGrpSrcQueries_Type = Counter32
_VRtrMldGrpIfSapRxGrpSrcQueries_Object = MibTableColumn
vRtrMldGrpIfSapRxGrpSrcQueries = _VRtrMldGrpIfSapRxGrpSrcQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 5, 2, 1, 10),
    _VRtrMldGrpIfSapRxGrpSrcQueries_Type()
)
vRtrMldGrpIfSapRxGrpSrcQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldGrpIfSapRxGrpSrcQueries.setStatus("current")
_VRtrMldGrpIfSapRxV1Reports_Type = Counter32
_VRtrMldGrpIfSapRxV1Reports_Object = MibTableColumn
vRtrMldGrpIfSapRxV1Reports = _VRtrMldGrpIfSapRxV1Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 5, 2, 1, 11),
    _VRtrMldGrpIfSapRxV1Reports_Type()
)
vRtrMldGrpIfSapRxV1Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldGrpIfSapRxV1Reports.setStatus("current")
_VRtrMldGrpIfSapRxV2Reports_Type = Counter32
_VRtrMldGrpIfSapRxV2Reports_Object = MibTableColumn
vRtrMldGrpIfSapRxV2Reports = _VRtrMldGrpIfSapRxV2Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 5, 2, 1, 12),
    _VRtrMldGrpIfSapRxV2Reports_Type()
)
vRtrMldGrpIfSapRxV2Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldGrpIfSapRxV2Reports.setStatus("current")
_VRtrMldGrpIfSapRxLeaves_Type = Counter32
_VRtrMldGrpIfSapRxLeaves_Object = MibTableColumn
vRtrMldGrpIfSapRxLeaves = _VRtrMldGrpIfSapRxLeaves_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 5, 2, 1, 13),
    _VRtrMldGrpIfSapRxLeaves_Type()
)
vRtrMldGrpIfSapRxLeaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldGrpIfSapRxLeaves.setStatus("current")
_VRtrMldGrpIfSapRxBadLenPkts_Type = Counter32
_VRtrMldGrpIfSapRxBadLenPkts_Object = MibTableColumn
vRtrMldGrpIfSapRxBadLenPkts = _VRtrMldGrpIfSapRxBadLenPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 5, 2, 1, 14),
    _VRtrMldGrpIfSapRxBadLenPkts_Type()
)
vRtrMldGrpIfSapRxBadLenPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldGrpIfSapRxBadLenPkts.setStatus("current")
_VRtrMldGrpIfSapRxBadChksumPkts_Type = Counter32
_VRtrMldGrpIfSapRxBadChksumPkts_Object = MibTableColumn
vRtrMldGrpIfSapRxBadChksumPkts = _VRtrMldGrpIfSapRxBadChksumPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 5, 2, 1, 15),
    _VRtrMldGrpIfSapRxBadChksumPkts_Type()
)
vRtrMldGrpIfSapRxBadChksumPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldGrpIfSapRxBadChksumPkts.setStatus("current")
_VRtrMldGrpIfSapRxUnknTypePkts_Type = Counter32
_VRtrMldGrpIfSapRxUnknTypePkts_Object = MibTableColumn
vRtrMldGrpIfSapRxUnknTypePkts = _VRtrMldGrpIfSapRxUnknTypePkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 5, 2, 1, 16),
    _VRtrMldGrpIfSapRxUnknTypePkts_Type()
)
vRtrMldGrpIfSapRxUnknTypePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldGrpIfSapRxUnknTypePkts.setStatus("current")
_VRtrMldGrpIfSapRxBadRecvIfPkts_Type = Counter32
_VRtrMldGrpIfSapRxBadRecvIfPkts_Object = MibTableColumn
vRtrMldGrpIfSapRxBadRecvIfPkts = _VRtrMldGrpIfSapRxBadRecvIfPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 5, 2, 1, 17),
    _VRtrMldGrpIfSapRxBadRecvIfPkts_Type()
)
vRtrMldGrpIfSapRxBadRecvIfPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldGrpIfSapRxBadRecvIfPkts.setStatus("current")
_VRtrMldGrpIfSapRxNonLocal_Type = Counter32
_VRtrMldGrpIfSapRxNonLocal_Object = MibTableColumn
vRtrMldGrpIfSapRxNonLocal = _VRtrMldGrpIfSapRxNonLocal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 5, 2, 1, 18),
    _VRtrMldGrpIfSapRxNonLocal_Type()
)
vRtrMldGrpIfSapRxNonLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldGrpIfSapRxNonLocal.setStatus("current")
_VRtrMldGrpIfSapRxWrongVersions_Type = Counter32
_VRtrMldGrpIfSapRxWrongVersions_Object = MibTableColumn
vRtrMldGrpIfSapRxWrongVersions = _VRtrMldGrpIfSapRxWrongVersions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 5, 2, 1, 19),
    _VRtrMldGrpIfSapRxWrongVersions_Type()
)
vRtrMldGrpIfSapRxWrongVersions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldGrpIfSapRxWrongVersions.setStatus("current")
_VRtrMldGrpIfSapImportPlcyDrops_Type = Counter32
_VRtrMldGrpIfSapImportPlcyDrops_Object = MibTableColumn
vRtrMldGrpIfSapImportPlcyDrops = _VRtrMldGrpIfSapImportPlcyDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 5, 2, 1, 20),
    _VRtrMldGrpIfSapImportPlcyDrops_Type()
)
vRtrMldGrpIfSapImportPlcyDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldGrpIfSapImportPlcyDrops.setStatus("current")
_VRtrMldGrpIfSapRxNoRtrAlertPkts_Type = Counter32
_VRtrMldGrpIfSapRxNoRtrAlertPkts_Object = MibTableColumn
vRtrMldGrpIfSapRxNoRtrAlertPkts = _VRtrMldGrpIfSapRxNoRtrAlertPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 5, 2, 1, 21),
    _VRtrMldGrpIfSapRxNoRtrAlertPkts_Type()
)
vRtrMldGrpIfSapRxNoRtrAlertPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldGrpIfSapRxNoRtrAlertPkts.setStatus("current")
_VRtrMldGrpIfSapRxBadEncodings_Type = Counter32
_VRtrMldGrpIfSapRxBadEncodings_Object = MibTableColumn
vRtrMldGrpIfSapRxBadEncodings = _VRtrMldGrpIfSapRxBadEncodings_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 5, 2, 1, 22),
    _VRtrMldGrpIfSapRxBadEncodings_Type()
)
vRtrMldGrpIfSapRxBadEncodings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldGrpIfSapRxBadEncodings.setStatus("current")
_VRtrMldGrpIfSapRxPktDrops_Type = Counter32
_VRtrMldGrpIfSapRxPktDrops_Object = MibTableColumn
vRtrMldGrpIfSapRxPktDrops = _VRtrMldGrpIfSapRxPktDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 5, 2, 1, 23),
    _VRtrMldGrpIfSapRxPktDrops_Type()
)
vRtrMldGrpIfSapRxPktDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldGrpIfSapRxPktDrops.setStatus("current")
_VRtrMldGrpIfSapStatsStarGTypes_Type = Gauge32
_VRtrMldGrpIfSapStatsStarGTypes_Object = MibTableColumn
vRtrMldGrpIfSapStatsStarGTypes = _VRtrMldGrpIfSapStatsStarGTypes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 5, 2, 1, 24),
    _VRtrMldGrpIfSapStatsStarGTypes_Type()
)
vRtrMldGrpIfSapStatsStarGTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldGrpIfSapStatsStarGTypes.setStatus("current")
_VRtrMldGrpIfSapStatsSGTypes_Type = Gauge32
_VRtrMldGrpIfSapStatsSGTypes_Object = MibTableColumn
vRtrMldGrpIfSapStatsSGTypes = _VRtrMldGrpIfSapStatsSGTypes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 5, 2, 1, 25),
    _VRtrMldGrpIfSapStatsSGTypes_Type()
)
vRtrMldGrpIfSapStatsSGTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldGrpIfSapStatsSGTypes.setStatus("current")
_VRtrMldGrpIfSapStatsMcacPlcyDrp_Type = Counter32
_VRtrMldGrpIfSapStatsMcacPlcyDrp_Object = MibTableColumn
vRtrMldGrpIfSapStatsMcacPlcyDrp = _VRtrMldGrpIfSapStatsMcacPlcyDrp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 5, 2, 1, 26),
    _VRtrMldGrpIfSapStatsMcacPlcyDrp_Type()
)
vRtrMldGrpIfSapStatsMcacPlcyDrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldGrpIfSapStatsMcacPlcyDrp.setStatus("current")
_VRtrMldGrpIfSapRxLocalScopePkts_Type = Counter32
_VRtrMldGrpIfSapRxLocalScopePkts_Object = MibTableColumn
vRtrMldGrpIfSapRxLocalScopePkts = _VRtrMldGrpIfSapRxLocalScopePkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 5, 2, 1, 27),
    _VRtrMldGrpIfSapRxLocalScopePkts_Type()
)
vRtrMldGrpIfSapRxLocalScopePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldGrpIfSapRxLocalScopePkts.setStatus("current")
_VRtrMldGrpIfSapRxRsvdScopePkts_Type = Counter32
_VRtrMldGrpIfSapRxRsvdScopePkts_Object = MibTableColumn
vRtrMldGrpIfSapRxRsvdScopePkts = _VRtrMldGrpIfSapRxRsvdScopePkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 5, 2, 1, 28),
    _VRtrMldGrpIfSapRxRsvdScopePkts_Type()
)
vRtrMldGrpIfSapRxRsvdScopePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldGrpIfSapRxRsvdScopePkts.setStatus("current")
_VRtrMldGrpIfSapGrpTable_Object = MibTable
vRtrMldGrpIfSapGrpTable = _VRtrMldGrpIfSapGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 5, 3)
)
if mibBuilder.loadTexts:
    vRtrMldGrpIfSapGrpTable.setStatus("current")
_VRtrMldGrpIfSapGrpEntry_Object = MibTableRow
vRtrMldGrpIfSapGrpEntry = _VRtrMldGrpIfSapGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 5, 3, 1)
)
vRtrMldGrpIfSapGrpEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-IGMP-MIB", "vRtrIfFwdSvcId"),
    (0, "TIMETRA-IGMP-MIB", "vRtrGrpIfIndex"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "TIMETRA-MLD-MIB", "vRtrMldGrpIfSapGroupAddressType"),
    (0, "TIMETRA-MLD-MIB", "vRtrMldGrpIfSapGroupAddress"),
)
if mibBuilder.loadTexts:
    vRtrMldGrpIfSapGrpEntry.setStatus("current")
_VRtrMldGrpIfSapGroupAddressType_Type = InetAddressType
_VRtrMldGrpIfSapGroupAddressType_Object = MibTableColumn
vRtrMldGrpIfSapGroupAddressType = _VRtrMldGrpIfSapGroupAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 5, 3, 1, 1),
    _VRtrMldGrpIfSapGroupAddressType_Type()
)
vRtrMldGrpIfSapGroupAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMldGrpIfSapGroupAddressType.setStatus("current")


class _VRtrMldGrpIfSapGroupAddress_Type(InetAddress):
    """Custom type vRtrMldGrpIfSapGroupAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_VRtrMldGrpIfSapGroupAddress_Type.__name__ = "InetAddress"
_VRtrMldGrpIfSapGroupAddress_Object = MibTableColumn
vRtrMldGrpIfSapGroupAddress = _VRtrMldGrpIfSapGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 5, 3, 1, 2),
    _VRtrMldGrpIfSapGroupAddress_Type()
)
vRtrMldGrpIfSapGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMldGrpIfSapGroupAddress.setStatus("current")
_VRtrMldGrpIfSapGrpType_Type = TmnxMldGroupType
_VRtrMldGrpIfSapGrpType_Object = MibTableColumn
vRtrMldGrpIfSapGrpType = _VRtrMldGrpIfSapGrpType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 5, 3, 1, 3),
    _VRtrMldGrpIfSapGrpType_Type()
)
vRtrMldGrpIfSapGrpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldGrpIfSapGrpType.setStatus("current")
_VRtrMldGrpIfSapGrpUpTime_Type = Unsigned32
_VRtrMldGrpIfSapGrpUpTime_Object = MibTableColumn
vRtrMldGrpIfSapGrpUpTime = _VRtrMldGrpIfSapGrpUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 5, 3, 1, 4),
    _VRtrMldGrpIfSapGrpUpTime_Type()
)
vRtrMldGrpIfSapGrpUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldGrpIfSapGrpUpTime.setStatus("current")
_VRtrMldGrpIfSapGrpExpiryTime_Type = Unsigned32
_VRtrMldGrpIfSapGrpExpiryTime_Object = MibTableColumn
vRtrMldGrpIfSapGrpExpiryTime = _VRtrMldGrpIfSapGrpExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 5, 3, 1, 5),
    _VRtrMldGrpIfSapGrpExpiryTime_Type()
)
vRtrMldGrpIfSapGrpExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldGrpIfSapGrpExpiryTime.setStatus("current")
_VRtrMldGrpIfSapGrpVer1HostTmr_Type = Unsigned32
_VRtrMldGrpIfSapGrpVer1HostTmr_Object = MibTableColumn
vRtrMldGrpIfSapGrpVer1HostTmr = _VRtrMldGrpIfSapGrpVer1HostTmr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 5, 3, 1, 6),
    _VRtrMldGrpIfSapGrpVer1HostTmr_Type()
)
vRtrMldGrpIfSapGrpVer1HostTmr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldGrpIfSapGrpVer1HostTmr.setStatus("current")
_VRtrMldGrpIfSapGrpMode_Type = TmnxMldGroupFilterMode
_VRtrMldGrpIfSapGrpMode_Object = MibTableColumn
vRtrMldGrpIfSapGrpMode = _VRtrMldGrpIfSapGrpMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 5, 3, 1, 7),
    _VRtrMldGrpIfSapGrpMode_Type()
)
vRtrMldGrpIfSapGrpMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldGrpIfSapGrpMode.setStatus("current")
_VRtrMldGrpIfSapGrpCompatMode_Type = TmnxMldVersion
_VRtrMldGrpIfSapGrpCompatMode_Object = MibTableColumn
vRtrMldGrpIfSapGrpCompatMode = _VRtrMldGrpIfSapGrpCompatMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 5, 3, 1, 8),
    _VRtrMldGrpIfSapGrpCompatMode_Type()
)
vRtrMldGrpIfSapGrpCompatMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldGrpIfSapGrpCompatMode.setStatus("current")
_VRtrMldGrpIfSapGrpSrcTable_Object = MibTable
vRtrMldGrpIfSapGrpSrcTable = _VRtrMldGrpIfSapGrpSrcTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 5, 4)
)
if mibBuilder.loadTexts:
    vRtrMldGrpIfSapGrpSrcTable.setStatus("current")
_VRtrMldGrpIfSapGrpSrcEntry_Object = MibTableRow
vRtrMldGrpIfSapGrpSrcEntry = _VRtrMldGrpIfSapGrpSrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 5, 4, 1)
)
vRtrMldGrpIfSapGrpSrcEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-IGMP-MIB", "vRtrIfFwdSvcId"),
    (0, "TIMETRA-IGMP-MIB", "vRtrGrpIfIndex"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "TIMETRA-MLD-MIB", "vRtrMldGrpIfSapGroupAddressType"),
    (0, "TIMETRA-MLD-MIB", "vRtrMldGrpIfSapGroupAddress"),
    (0, "TIMETRA-MLD-MIB", "vRtrMldGrpIfSapGrpSrcAddressType"),
    (0, "TIMETRA-MLD-MIB", "vRtrMldGrpIfSapGrpSrcAddress"),
)
if mibBuilder.loadTexts:
    vRtrMldGrpIfSapGrpSrcEntry.setStatus("current")
_VRtrMldGrpIfSapGrpSrcAddressType_Type = InetAddressType
_VRtrMldGrpIfSapGrpSrcAddressType_Object = MibTableColumn
vRtrMldGrpIfSapGrpSrcAddressType = _VRtrMldGrpIfSapGrpSrcAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 5, 4, 1, 1),
    _VRtrMldGrpIfSapGrpSrcAddressType_Type()
)
vRtrMldGrpIfSapGrpSrcAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMldGrpIfSapGrpSrcAddressType.setStatus("current")


class _VRtrMldGrpIfSapGrpSrcAddress_Type(InetAddress):
    """Custom type vRtrMldGrpIfSapGrpSrcAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_VRtrMldGrpIfSapGrpSrcAddress_Type.__name__ = "InetAddress"
_VRtrMldGrpIfSapGrpSrcAddress_Object = MibTableColumn
vRtrMldGrpIfSapGrpSrcAddress = _VRtrMldGrpIfSapGrpSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 5, 4, 1, 2),
    _VRtrMldGrpIfSapGrpSrcAddress_Type()
)
vRtrMldGrpIfSapGrpSrcAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMldGrpIfSapGrpSrcAddress.setStatus("current")
_VRtrMldGrpIfSapGrpSrcExpTime_Type = Unsigned32
_VRtrMldGrpIfSapGrpSrcExpTime_Object = MibTableColumn
vRtrMldGrpIfSapGrpSrcExpTime = _VRtrMldGrpIfSapGrpSrcExpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 5, 4, 1, 3),
    _VRtrMldGrpIfSapGrpSrcExpTime_Type()
)
vRtrMldGrpIfSapGrpSrcExpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldGrpIfSapGrpSrcExpTime.setStatus("current")
_VRtrMldGrpIfSapGrpSrcType_Type = TmnxMldGroupType
_VRtrMldGrpIfSapGrpSrcType_Object = MibTableColumn
vRtrMldGrpIfSapGrpSrcType = _VRtrMldGrpIfSapGrpSrcType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 5, 4, 1, 4),
    _VRtrMldGrpIfSapGrpSrcType_Type()
)
vRtrMldGrpIfSapGrpSrcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldGrpIfSapGrpSrcType.setStatus("current")
_VRtrMldGrpSrcGrpIfSapTable_Object = MibTable
vRtrMldGrpSrcGrpIfSapTable = _VRtrMldGrpSrcGrpIfSapTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 5, 5)
)
if mibBuilder.loadTexts:
    vRtrMldGrpSrcGrpIfSapTable.setStatus("current")
_VRtrMldGrpSrcGrpIfSapEntry_Object = MibTableRow
vRtrMldGrpSrcGrpIfSapEntry = _VRtrMldGrpSrcGrpIfSapEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 5, 5, 1)
)
vRtrMldGrpSrcGrpIfSapEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MLD-MIB", "vRtrMldGrpSrcGroupAddrType"),
    (0, "TIMETRA-MLD-MIB", "vRtrMldGrpSrcGroupAddress"),
    (0, "TIMETRA-MLD-MIB", "vRtrMldGrpSrcSourceAddrType"),
    (0, "TIMETRA-MLD-MIB", "vRtrMldGrpSrcSourceAddress"),
    (0, "TIMETRA-MLD-MIB", "vRtrMldGrpSrcFwdOrBlk"),
    (0, "TIMETRA-IGMP-MIB", "vRtrIfFwdSvcId"),
    (0, "TIMETRA-IGMP-MIB", "vRtrGrpIfIndex"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
)
if mibBuilder.loadTexts:
    vRtrMldGrpSrcGrpIfSapEntry.setStatus("current")
_VRtrMldGrpSrcGrpIfSapUpTime_Type = Unsigned32
_VRtrMldGrpSrcGrpIfSapUpTime_Object = MibTableColumn
vRtrMldGrpSrcGrpIfSapUpTime = _VRtrMldGrpSrcGrpIfSapUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 46, 5, 5, 1, 1),
    _VRtrMldGrpSrcGrpIfSapUpTime_Type()
)
vRtrMldGrpSrcGrpIfSapUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMldGrpSrcGrpIfSapUpTime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMldGrpSrcGrpIfSapUpTime.setUnits("seconds")
_VRtrMldNotifyPrefix_ObjectIdentity = ObjectIdentity
vRtrMldNotifyPrefix = _VRtrMldNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 46)
)
_VRtrMldNotifications_ObjectIdentity = ObjectIdentity
vRtrMldNotifications = _VRtrMldNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 46, 0)
)
vRtrMldGeneralEntry.registerAugmentions(
    ("TIMETRA-MLD-MIB",
     "vRtrMldGenStatsEntry")
)
vRtrMldGenStatsEntry.setIndexNames(*vRtrMldGeneralEntry.getIndexNames())
vRtrMldIfEntry.registerAugmentions(
    ("TIMETRA-MLD-MIB",
     "vRtrMldIfStatsEntry")
)
vRtrMldIfStatsEntry.setIndexNames(*vRtrMldIfEntry.getIndexNames())
vRtrMldHostEntry.registerAugmentions(
    ("TIMETRA-MLD-MIB",
     "vRtrMldHostStatsEntry")
)
vRtrMldHostStatsEntry.setIndexNames(*vRtrMldHostEntry.getIndexNames())

# Managed Objects groups

tmnxMldGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 46, 2, 1)
)
tmnxMldGlobalGroup.setObjects(
      *(("TIMETRA-MLD-MIB", "vRtrMldGeneralTableLastChanged"),
        ("TIMETRA-MLD-MIB", "vRtrMldGenQueryInterval"),
        ("TIMETRA-MLD-MIB", "vRtrMldGenLastMembQueryIntvl"),
        ("TIMETRA-MLD-MIB", "vRtrMldGenQueryResponseIntvl"),
        ("TIMETRA-MLD-MIB", "vRtrMldGenRobustCount"),
        ("TIMETRA-MLD-MIB", "vRtrMldGenLastChange"),
        ("TIMETRA-MLD-MIB", "vRtrMldGenAdminState"),
        ("TIMETRA-MLD-MIB", "vRtrMldGenOperState"),
        ("TIMETRA-MLD-MIB", "vRtrMldGrpSrcUpTime"),
        ("TIMETRA-MLD-MIB", "vRtrMldSsmTransTableLastChanged"),
        ("TIMETRA-MLD-MIB", "vRtrMldSsmTransRowStatus"),
        ("TIMETRA-MLD-MIB", "vRtrMldSsmTransLastChanged"),
        ("TIMETRA-MLD-MIB", "vRtrMldGenStatsStarGTypes"),
        ("TIMETRA-MLD-MIB", "vRtrMldGenStatsSGTypes"))
)
if mibBuilder.loadTexts:
    tmnxMldGlobalGroup.setStatus("current")

tmnxMldIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 46, 2, 2)
)
tmnxMldIfGroup.setObjects(
      *(("TIMETRA-MLD-MIB", "vRtrMldIfTableLastChanged"),
        ("TIMETRA-MLD-MIB", "vRtrMldIfRowStatus"),
        ("TIMETRA-MLD-MIB", "vRtrMldIfLastChanged"),
        ("TIMETRA-MLD-MIB", "vRtrMldIfAdminState"),
        ("TIMETRA-MLD-MIB", "vRtrMldIfOperState"),
        ("TIMETRA-MLD-MIB", "vRtrMldIfAdminVersion"),
        ("TIMETRA-MLD-MIB", "vRtrMldIfOperVersion"),
        ("TIMETRA-MLD-MIB", "vRtrMldIfQuerierType"),
        ("TIMETRA-MLD-MIB", "vRtrMldIfQuerier"),
        ("TIMETRA-MLD-MIB", "vRtrMldIfImportPolicy"),
        ("TIMETRA-MLD-MIB", "vRtrMldIfGroupCount"),
        ("TIMETRA-MLD-MIB", "vRtrMldIfQuerierUpTime"),
        ("TIMETRA-MLD-MIB", "vRtrMldIfQuerierExpiryTime"),
        ("TIMETRA-MLD-MIB", "vRtrMldIfNextGenQueryTime"),
        ("TIMETRA-MLD-MIB", "vRtrMldIfMaxGroups"),
        ("TIMETRA-MLD-MIB", "vRtrMldIfMaxGroupsTillNow"),
        ("TIMETRA-MLD-MIB", "vRtrMldIfQueryInterval"),
        ("TIMETRA-MLD-MIB", "vRtrMldIfLastMembQueryIntvl"),
        ("TIMETRA-MLD-MIB", "vRtrMldIfQueryResponseIntvl"),
        ("TIMETRA-MLD-MIB", "vRtrMldIfGroupType"),
        ("TIMETRA-MLD-MIB", "vRtrMldIfGroupUpTime"),
        ("TIMETRA-MLD-MIB", "vRtrMldIfGroupExpiryTime"),
        ("TIMETRA-MLD-MIB", "vRtrMldIfGroupVer1HostTimer"),
        ("TIMETRA-MLD-MIB", "vRtrMldIfGroupMode"),
        ("TIMETRA-MLD-MIB", "vRtrMldIfGroupCompatMode"),
        ("TIMETRA-MLD-MIB", "vRtrMldIfGroupLstRprtrType"),
        ("TIMETRA-MLD-MIB", "vRtrMldIfGroupLastReporter"),
        ("TIMETRA-MLD-MIB", "vRtrMldIfGrpSrcExpiryTime"),
        ("TIMETRA-MLD-MIB", "vRtrMldIfGrpSrcType"),
        ("TIMETRA-MLD-MIB", "vRtrMldIfStatcGrpSrcTblLstChngd"),
        ("TIMETRA-MLD-MIB", "vRtrMldIfStaticGrpSrcRowStatus"),
        ("TIMETRA-MLD-MIB", "vRtrMldIfStaticGrpSrcLstChanged"),
        ("TIMETRA-MLD-MIB", "vRtrMldIfTxGenQueries"),
        ("TIMETRA-MLD-MIB", "vRtrMldIfTxGrpQueries"),
        ("TIMETRA-MLD-MIB", "vRtrMldIfTxGrpSrcQueries"),
        ("TIMETRA-MLD-MIB", "vRtrMldIfTxV1Reports"),
        ("TIMETRA-MLD-MIB", "vRtrMldIfTxV2Reports"),
        ("TIMETRA-MLD-MIB", "vRtrMldIfTxLeaves"),
        ("TIMETRA-MLD-MIB", "vRtrMldIfTxErrors"),
        ("TIMETRA-MLD-MIB", "vRtrMldIfRxGenQueries"),
        ("TIMETRA-MLD-MIB", "vRtrMldIfRxGrpQueries"),
        ("TIMETRA-MLD-MIB", "vRtrMldIfRxGrpSrcQueries"),
        ("TIMETRA-MLD-MIB", "vRtrMldIfRxV1Reports"),
        ("TIMETRA-MLD-MIB", "vRtrMldIfRxV2Reports"),
        ("TIMETRA-MLD-MIB", "vRtrMldIfRxLeaves"),
        ("TIMETRA-MLD-MIB", "vRtrMldIfRxBadLenPkts"),
        ("TIMETRA-MLD-MIB", "vRtrMldIfRxBadChecksumPkts"),
        ("TIMETRA-MLD-MIB", "vRtrMldIfRxUnknownTypePkts"),
        ("TIMETRA-MLD-MIB", "vRtrMldIfRxBadReceiveIfPkts"),
        ("TIMETRA-MLD-MIB", "vRtrMldIfRxNonLocal"),
        ("TIMETRA-MLD-MIB", "vRtrMldIfRxWrongVersions"),
        ("TIMETRA-MLD-MIB", "vRtrMldIfImportPolicyDrops"),
        ("TIMETRA-MLD-MIB", "vRtrMldIfRxNoRtrAlertPkts"),
        ("TIMETRA-MLD-MIB", "vRtrMldIfRxBadEncodings"),
        ("TIMETRA-MLD-MIB", "vRtrMldIfRxPktDrops"),
        ("TIMETRA-MLD-MIB", "vRtrMldIfStatsStarGTypes"),
        ("TIMETRA-MLD-MIB", "vRtrMldIfStatsSGTypes"),
        ("TIMETRA-MLD-MIB", "vRtrMldIfRxLocalScopePkts"),
        ("TIMETRA-MLD-MIB", "vRtrMldIfRxRsvdScopePkts"))
)
if mibBuilder.loadTexts:
    tmnxMldIfGroup.setStatus("current")

tmnxMldNotifyObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 46, 2, 3)
)
tmnxMldNotifyObjsGroup.setObjects(
    ("TIMETRA-MLD-MIB", "vRtrMldNotifyQueryVersion")
)
if mibBuilder.loadTexts:
    tmnxMldNotifyObjsGroup.setStatus("current")

tmnxMldIfV6v1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 46, 2, 5)
)
tmnxMldIfV6v1Group.setObjects(
      *(("TIMETRA-MLD-MIB", "vRtrMldIfSsmTltTableLastChanged"),
        ("TIMETRA-MLD-MIB", "vRtrMldIfSsmTransRowStatus"))
)
if mibBuilder.loadTexts:
    tmnxMldIfV6v1Group.setStatus("current")

tmnxMldIfV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 46, 2, 6)
)
tmnxMldIfV8v0Group.setObjects(
    ("TIMETRA-MLD-MIB", "vRtrMldIfDisRtrAlertChk")
)
if mibBuilder.loadTexts:
    tmnxMldIfV8v0Group.setStatus("current")

tmnxMldIfV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 46, 2, 7)
)
tmnxMldIfV12v0Group.setObjects(
      *(("TIMETRA-MLD-MIB", "vRtrMldIfMcacPolicyName"),
        ("TIMETRA-MLD-MIB", "vRtrMldIfMcacUnconstrainedBW"),
        ("TIMETRA-MLD-MIB", "vRtrMldIfMcacConstAdminState"),
        ("TIMETRA-MLD-MIB", "vRtrMldIfMcacPreRsvdMandBW"),
        ("TIMETRA-MLD-MIB", "vRtrMldIfMcacinUseMandBw"),
        ("TIMETRA-MLD-MIB", "vRtrMldIfMcacinUseOpnlBw"),
        ("TIMETRA-MLD-MIB", "vRtrMldIfMcacAvailMandBw"),
        ("TIMETRA-MLD-MIB", "vRtrMldIfMcacAvailOpnlBw"),
        ("TIMETRA-MLD-MIB", "vRtrMldIfMcacValuesInTransit"),
        ("TIMETRA-MLD-MIB", "vRtrMldIfMaxSources"),
        ("TIMETRA-MLD-MIB", "vRtrMldIfMaxGrpSources"),
        ("TIMETRA-MLD-MIB", "vRtrMldIfMcacUseLagPortWeight"),
        ("TIMETRA-MLD-MIB", "vRtrMldIfStatsMcacPolicyDrops"),
        ("TIMETRA-MLD-MIB", "vRtrMldIfMcacLevelRowStatus"),
        ("TIMETRA-MLD-MIB", "vRtrMldIfMcacLevelBW"),
        ("TIMETRA-MLD-MIB", "vRtrMldIfMcacLagRowStatus"),
        ("TIMETRA-MLD-MIB", "vRtrMldIfMcacLagLevel"),
        ("TIMETRA-MLD-MIB", "vRtrMldHostLastChangeTime"),
        ("TIMETRA-MLD-MIB", "vRtrMldHostOperState"),
        ("TIMETRA-MLD-MIB", "vRtrMldHostOperVersion"),
        ("TIMETRA-MLD-MIB", "vRtrMldHostGroupCount"),
        ("TIMETRA-MLD-MIB", "vRtrMldHostNextGenQueryTime"),
        ("TIMETRA-MLD-MIB", "vRtrMldHostMaxGroupsTillNow"),
        ("TIMETRA-MLD-MIB", "vRtrMldHostFwdSvcId"),
        ("TIMETRA-MLD-MIB", "vRtrMldHostGrpIfId"),
        ("TIMETRA-MLD-MIB", "vRtrMldHostSubscriberId"),
        ("TIMETRA-MLD-MIB", "vRtrMldHostMldPolicy"),
        ("TIMETRA-MLD-MIB", "vRtrMldHostMaxGroups"),
        ("TIMETRA-MLD-MIB", "vRtrMldHostAdminVersion"),
        ("TIMETRA-MLD-MIB", "vRtrMldHostMaxSources"),
        ("TIMETRA-MLD-MIB", "vRtrMldHostMaxGrpSources"),
        ("TIMETRA-MLD-MIB", "vRtrMldHostTxGenQueries"),
        ("TIMETRA-MLD-MIB", "vRtrMldHostTxGrpQueries"),
        ("TIMETRA-MLD-MIB", "vRtrMldHostTxGrpSrcQueries"),
        ("TIMETRA-MLD-MIB", "vRtrMldHostTxV1Reports"),
        ("TIMETRA-MLD-MIB", "vRtrMldHostTxV2Reports"),
        ("TIMETRA-MLD-MIB", "vRtrMldHostTxLeaves"),
        ("TIMETRA-MLD-MIB", "vRtrMldHostTxErrors"),
        ("TIMETRA-MLD-MIB", "vRtrMldHostRxGenQueries"),
        ("TIMETRA-MLD-MIB", "vRtrMldHostRxGrpQueries"),
        ("TIMETRA-MLD-MIB", "vRtrMldHostRxGrpSrcQueries"),
        ("TIMETRA-MLD-MIB", "vRtrMldHostRxV1Reports"),
        ("TIMETRA-MLD-MIB", "vRtrMldHostRxV2Reports"),
        ("TIMETRA-MLD-MIB", "vRtrMldHostRxLeaves"),
        ("TIMETRA-MLD-MIB", "vRtrMldHostRxBadLenPkts"),
        ("TIMETRA-MLD-MIB", "vRtrMldHostRxBadChecksumPkts"),
        ("TIMETRA-MLD-MIB", "vRtrMldHostRxUnknownTypePkts"),
        ("TIMETRA-MLD-MIB", "vRtrMldHostRxBadReceiveIfPkts"),
        ("TIMETRA-MLD-MIB", "vRtrMldHostRxNonLocal"),
        ("TIMETRA-MLD-MIB", "vRtrMldHostRxWrongVersions"),
        ("TIMETRA-MLD-MIB", "vRtrMldHostImportPolicyDrops"),
        ("TIMETRA-MLD-MIB", "vRtrMldHostRxNoRtrAlertPkts"),
        ("TIMETRA-MLD-MIB", "vRtrMldHostRxBadEncodings"),
        ("TIMETRA-MLD-MIB", "vRtrMldHostRxPktDrops"),
        ("TIMETRA-MLD-MIB", "vRtrMldHostStatsStarGTypes"),
        ("TIMETRA-MLD-MIB", "vRtrMldHostStatsSGTypes"),
        ("TIMETRA-MLD-MIB", "vRtrMldHostStatsMcacPolicyDrops"),
        ("TIMETRA-MLD-MIB", "vRtrMldHostRxLocalScopePkts"),
        ("TIMETRA-MLD-MIB", "vRtrMldHostRxRsvdScopePkts"),
        ("TIMETRA-MLD-MIB", "vRtrMldHostRedirectionDrops"),
        ("TIMETRA-MLD-MIB", "vRtrMldGrpIfRowStatus"),
        ("TIMETRA-MLD-MIB", "vRtrMldGrpIfLastChangeTime"),
        ("TIMETRA-MLD-MIB", "vRtrMldGrpIfAdminState"),
        ("TIMETRA-MLD-MIB", "vRtrMldGrpIfOperState"),
        ("TIMETRA-MLD-MIB", "vRtrMldGrpIfSubHostsOnly"),
        ("TIMETRA-MLD-MIB", "vRtrMldGrpIfAdminVersion"),
        ("TIMETRA-MLD-MIB", "vRtrMldGrpIfImportPolicy"),
        ("TIMETRA-MLD-MIB", "vRtrMldGrpIfSubnetCheck"),
        ("TIMETRA-MLD-MIB", "vRtrMldGrpIfMcacPolicyName"),
        ("TIMETRA-MLD-MIB", "vRtrMldGrpIfMcacUnconstrainedBW"),
        ("TIMETRA-MLD-MIB", "vRtrMldGrpIfMcacConstAdminState"),
        ("TIMETRA-MLD-MIB", "vRtrMldGrpIfMcacPreRsvdMandBW"),
        ("TIMETRA-MLD-MIB", "vRtrMldGrpIfMcacinUseMandBw"),
        ("TIMETRA-MLD-MIB", "vRtrMldGrpIfMcacinUseOpnlBw"),
        ("TIMETRA-MLD-MIB", "vRtrMldGrpIfMcacAvailMandBw"),
        ("TIMETRA-MLD-MIB", "vRtrMldGrpIfMcacAvailOpnlBw"),
        ("TIMETRA-MLD-MIB", "vRtrMldGrpIfMcacValuesInTransit"),
        ("TIMETRA-MLD-MIB", "vRtrMldGrpIfDisRtrAlertChk"),
        ("TIMETRA-MLD-MIB", "vRtrMldGrpIfMaxGroups"),
        ("TIMETRA-MLD-MIB", "vRtrMldGrpIfMaxSources"),
        ("TIMETRA-MLD-MIB", "vRtrMldGrpIfMaxGrpSources"),
        ("TIMETRA-MLD-MIB", "vRtrMldGrpIfHostGrpType"),
        ("TIMETRA-MLD-MIB", "vRtrMldGrpIfHostGrpUpTime"),
        ("TIMETRA-MLD-MIB", "vRtrMldGrpIfHostGrpExpiryTime"),
        ("TIMETRA-MLD-MIB", "vRtrMldGrpIfHostGrpVer1HostTmr"),
        ("TIMETRA-MLD-MIB", "vRtrMldGrpIfHostGrpMode"),
        ("TIMETRA-MLD-MIB", "vRtrMldGrpIfHostGrpCompatMode"),
        ("TIMETRA-MLD-MIB", "vRtrMldGrpIfHostGrpMRDstVrId"),
        ("TIMETRA-MLD-MIB", "vRtrMldGrpIfHostGrpMRDstIfId"),
        ("TIMETRA-MLD-MIB", "vRtrMldGrpIfHostGrpSrcExpTime"),
        ("TIMETRA-MLD-MIB", "vRtrMldGrpIfHostGrpSrcType"),
        ("TIMETRA-MLD-MIB", "vRtrMldGrpIfHostGrpSrcMRDstVrId"),
        ("TIMETRA-MLD-MIB", "vRtrMldGrpIfHostGrpSrcMRDstIfId"),
        ("TIMETRA-MLD-MIB", "vRtrMldGrpSrcHostUpTime"),
        ("TIMETRA-MLD-MIB", "vRtrMldHostGrpSrcExpiryTime"),
        ("TIMETRA-MLD-MIB", "vRtrMldHostGrpSrcType"),
        ("TIMETRA-MLD-MIB", "vRtrMldHostGrpSrcMcRdrDstVRtrID"),
        ("TIMETRA-MLD-MIB", "vRtrMldHostGrpSrcMcRdrDstIfIdx"),
        ("TIMETRA-MLD-MIB", "vRtrMldHostGrpType"),
        ("TIMETRA-MLD-MIB", "vRtrMldHostGrpUpTime"),
        ("TIMETRA-MLD-MIB", "vRtrMldHostGrpExpiryTime"),
        ("TIMETRA-MLD-MIB", "vRtrMldHostGrpVer1HostTmr"),
        ("TIMETRA-MLD-MIB", "vRtrMldHostGrpMode"),
        ("TIMETRA-MLD-MIB", "vRtrMldHostGrpCompatMode"),
        ("TIMETRA-MLD-MIB", "vRtrMldHostGrpMcRdrDstVrId"),
        ("TIMETRA-MLD-MIB", "vRtrMldHostGrpMcRdrDstIfId"),
        ("TIMETRA-MLD-MIB", "vRtrMldGrpIfHostLastChangeTime"),
        ("TIMETRA-MLD-MIB", "vRtrMldGrpIfHostOperState"),
        ("TIMETRA-MLD-MIB", "vRtrMldGrpIfSapLastChangeTime"),
        ("TIMETRA-MLD-MIB", "vRtrMldGrpIfSapOperState"),
        ("TIMETRA-MLD-MIB", "vRtrMldGrpIfSapAdminVersion"),
        ("TIMETRA-MLD-MIB", "vRtrMldGrpIfSapOperVersion"),
        ("TIMETRA-MLD-MIB", "vRtrMldGrpIfSapGroupCount"),
        ("TIMETRA-MLD-MIB", "vRtrMldGrpIfSapNextGenQueryTime"),
        ("TIMETRA-MLD-MIB", "vRtrMldGrpIfSapMaxGroups"),
        ("TIMETRA-MLD-MIB", "vRtrMldGrpIfSapMaxGroupsTillNow"),
        ("TIMETRA-MLD-MIB", "vRtrMldGrpIfSapMaxSources"),
        ("TIMETRA-MLD-MIB", "vRtrMldGrpIfSapMaxGrpSources"),
        ("TIMETRA-MLD-MIB", "vRtrMldGrpIfSapTxGenQueries"),
        ("TIMETRA-MLD-MIB", "vRtrMldGrpIfSapTxGrpQueries"),
        ("TIMETRA-MLD-MIB", "vRtrMldGrpIfSapTxGrpSrcQueries"),
        ("TIMETRA-MLD-MIB", "vRtrMldGrpIfSapTxV1Reports"),
        ("TIMETRA-MLD-MIB", "vRtrMldGrpIfSapTxV2Reports"),
        ("TIMETRA-MLD-MIB", "vRtrMldGrpIfSapTxLeaves"),
        ("TIMETRA-MLD-MIB", "vRtrMldGrpIfSapTxErrors"),
        ("TIMETRA-MLD-MIB", "vRtrMldGrpIfSapRxGenQueries"),
        ("TIMETRA-MLD-MIB", "vRtrMldGrpIfSapRxGrpQueries"),
        ("TIMETRA-MLD-MIB", "vRtrMldGrpIfSapRxGrpSrcQueries"),
        ("TIMETRA-MLD-MIB", "vRtrMldGrpIfSapRxV1Reports"),
        ("TIMETRA-MLD-MIB", "vRtrMldGrpIfSapRxV2Reports"),
        ("TIMETRA-MLD-MIB", "vRtrMldGrpIfSapRxLeaves"),
        ("TIMETRA-MLD-MIB", "vRtrMldGrpIfSapRxBadLenPkts"),
        ("TIMETRA-MLD-MIB", "vRtrMldGrpIfSapRxBadChksumPkts"),
        ("TIMETRA-MLD-MIB", "vRtrMldGrpIfSapRxUnknTypePkts"),
        ("TIMETRA-MLD-MIB", "vRtrMldGrpIfSapRxBadRecvIfPkts"),
        ("TIMETRA-MLD-MIB", "vRtrMldGrpIfSapRxNonLocal"),
        ("TIMETRA-MLD-MIB", "vRtrMldGrpIfSapRxWrongVersions"),
        ("TIMETRA-MLD-MIB", "vRtrMldGrpIfSapImportPlcyDrops"),
        ("TIMETRA-MLD-MIB", "vRtrMldGrpIfSapRxNoRtrAlertPkts"),
        ("TIMETRA-MLD-MIB", "vRtrMldGrpIfSapRxBadEncodings"),
        ("TIMETRA-MLD-MIB", "vRtrMldGrpIfSapRxPktDrops"),
        ("TIMETRA-MLD-MIB", "vRtrMldGrpIfSapStatsStarGTypes"),
        ("TIMETRA-MLD-MIB", "vRtrMldGrpIfSapStatsSGTypes"),
        ("TIMETRA-MLD-MIB", "vRtrMldGrpIfSapStatsMcacPlcyDrp"),
        ("TIMETRA-MLD-MIB", "vRtrMldGrpIfSapRxLocalScopePkts"),
        ("TIMETRA-MLD-MIB", "vRtrMldGrpIfSapRxRsvdScopePkts"),
        ("TIMETRA-MLD-MIB", "vRtrMldGrpIfSapGrpType"),
        ("TIMETRA-MLD-MIB", "vRtrMldGrpIfSapGrpUpTime"),
        ("TIMETRA-MLD-MIB", "vRtrMldGrpIfSapGrpExpiryTime"),
        ("TIMETRA-MLD-MIB", "vRtrMldGrpIfSapGrpVer1HostTmr"),
        ("TIMETRA-MLD-MIB", "vRtrMldGrpIfSapGrpMode"),
        ("TIMETRA-MLD-MIB", "vRtrMldGrpIfSapGrpCompatMode"),
        ("TIMETRA-MLD-MIB", "vRtrMldGrpIfSapGrpSrcExpTime"),
        ("TIMETRA-MLD-MIB", "vRtrMldGrpIfSapGrpSrcType"),
        ("TIMETRA-MLD-MIB", "vRtrMldGrpSrcGrpIfSapUpTime"),
        ("TIMETRA-MLD-MIB", "vRtrMldGrpSrcSummFwdInterfaces"),
        ("TIMETRA-MLD-MIB", "vRtrMldGrpSrcSummBlkInterfaces"),
        ("TIMETRA-MLD-MIB", "vRtrMldGrpSrcSummFwdHosts"),
        ("TIMETRA-MLD-MIB", "vRtrMldGrpSrcSummBlkHosts"),
        ("TIMETRA-MLD-MIB", "vRtrMldGrpSrcSummFwdGrpIfSaps"),
        ("TIMETRA-MLD-MIB", "vRtrMldGrpSrcSummBlkGrpIfSaps"),
        ("TIMETRA-MLD-MIB", "vRtrMldGrpIfQrySrcIpAddrType"),
        ("TIMETRA-MLD-MIB", "vRtrMldGrpIfQrySrcIpAddr"))
)
if mibBuilder.loadTexts:
    tmnxMldIfV12v0Group.setStatus("current")

tmnxMldNotifyObjsV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 46, 2, 8)
)
tmnxMldNotifyObjsV12v0Group.setObjects(
      *(("TIMETRA-MLD-MIB", "vRtrMldNotifyGrpAddrType"),
        ("TIMETRA-MLD-MIB", "vRtrMldNotifyGrpAddr"),
        ("TIMETRA-MLD-MIB", "vRtrMldNotifyDescription"),
        ("TIMETRA-MLD-MIB", "vRtrMldNotifyMcacPolicyName"),
        ("TIMETRA-MLD-MIB", "vRtrMldNotifySrcAddrType"),
        ("TIMETRA-MLD-MIB", "vRtrMldNotifySrcAddr"))
)
if mibBuilder.loadTexts:
    tmnxMldNotifyObjsV12v0Group.setStatus("current")

tmnxMldGlobalV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 46, 2, 10)
)
tmnxMldGlobalV12v0Group.setObjects(
      *(("TIMETRA-MLD-MIB", "vRtrMldGenGrpIfQrySrcIpAddrType"),
        ("TIMETRA-MLD-MIB", "vRtrMldGenGrpIfQrySrcIpAddr"))
)
if mibBuilder.loadTexts:
    tmnxMldGlobalV12v0Group.setStatus("current")


# Notification objects

vRtrMldIfRxQueryVerMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 46, 0, 1)
)
vRtrMldIfRxQueryVerMismatch.setObjects(
      *(("TIMETRA-VRTR-MIB", "vRtrID"),
        ("TIMETRA-VRTR-MIB", "vRtrIfIndex"),
        ("TIMETRA-MLD-MIB", "vRtrMldIfAdminVersion"),
        ("TIMETRA-MLD-MIB", "vRtrMldNotifyQueryVersion"))
)
if mibBuilder.loadTexts:
    vRtrMldIfRxQueryVerMismatch.setStatus(
        "current"
    )

vRtrMldIfCModeRxQueryMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 46, 0, 2)
)
vRtrMldIfCModeRxQueryMismatch.setObjects(
      *(("TIMETRA-VRTR-MIB", "vRtrID"),
        ("TIMETRA-VRTR-MIB", "vRtrIfIndex"),
        ("TIMETRA-MLD-MIB", "vRtrMldIfOperVersion"),
        ("TIMETRA-MLD-MIB", "vRtrMldNotifyQueryVersion"))
)
if mibBuilder.loadTexts:
    vRtrMldIfCModeRxQueryMismatch.setStatus(
        "current"
    )

vRtrMldMaxGrpsLimitExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 46, 0, 3)
)
vRtrMldMaxGrpsLimitExceeded.setObjects(
    ("TIMETRA-MLD-MIB", "vRtrMldIfMaxGroups")
)
if mibBuilder.loadTexts:
    vRtrMldMaxGrpsLimitExceeded.setStatus(
        "current"
    )

vRtrMldMcacPlcyDropped = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 46, 0, 4)
)
vRtrMldMcacPlcyDropped.setObjects(
      *(("TIMETRA-MLD-MIB", "vRtrMldIfMcacPolicyName"),
        ("TIMETRA-MLD-MIB", "vRtrMldNotifyGrpAddrType"),
        ("TIMETRA-MLD-MIB", "vRtrMldNotifyGrpAddr"),
        ("TIMETRA-MLD-MIB", "vRtrMldNotifySrcAddrType"),
        ("TIMETRA-MLD-MIB", "vRtrMldNotifySrcAddr"),
        ("TIMETRA-MLD-MIB", "vRtrMldNotifyDescription"))
)
if mibBuilder.loadTexts:
    vRtrMldMcacPlcyDropped.setStatus(
        "current"
    )

vRtrMldHostInstantiationFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 46, 0, 5)
)
vRtrMldHostInstantiationFail.setObjects(
      *(("TIMETRA-MLD-MIB", "vRtrMldGrpIfHostLastChangeTime"),
        ("TIMETRA-MLD-MIB", "vRtrMldNotifyDescription"))
)
if mibBuilder.loadTexts:
    vRtrMldHostInstantiationFail.setStatus(
        "current"
    )

vRtrMldHostMaxGrpsLimitExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 46, 0, 6)
)
vRtrMldHostMaxGrpsLimitExceeded.setObjects(
      *(("TIMETRA-MLD-MIB", "vRtrMldHostFwdSvcId"),
        ("TIMETRA-MLD-MIB", "vRtrMldHostGrpIfId"),
        ("TIMETRA-MLD-MIB", "vRtrMldHostMaxGroups"))
)
if mibBuilder.loadTexts:
    vRtrMldHostMaxGrpsLimitExceeded.setStatus(
        "current"
    )

vRtrMldHostMcacPlcyDropped = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 46, 0, 7)
)
vRtrMldHostMcacPlcyDropped.setObjects(
      *(("TIMETRA-MLD-MIB", "vRtrMldHostSubscriberId"),
        ("TIMETRA-MLD-MIB", "vRtrMldNotifyMcacPolicyName"),
        ("TIMETRA-MLD-MIB", "vRtrMldNotifyGrpAddrType"),
        ("TIMETRA-MLD-MIB", "vRtrMldNotifyGrpAddr"),
        ("TIMETRA-MLD-MIB", "vRtrMldNotifySrcAddrType"),
        ("TIMETRA-MLD-MIB", "vRtrMldNotifySrcAddr"),
        ("TIMETRA-MLD-MIB", "vRtrMldNotifyDescription"))
)
if mibBuilder.loadTexts:
    vRtrMldHostMcacPlcyDropped.setStatus(
        "current"
    )

vRtrMldHostCModeRxQueryMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 46, 0, 8)
)
vRtrMldHostCModeRxQueryMismatch.setObjects(
      *(("TIMETRA-MLD-MIB", "vRtrMldHostOperVersion"),
        ("TIMETRA-MLD-MIB", "vRtrMldNotifyQueryVersion"))
)
if mibBuilder.loadTexts:
    vRtrMldHostCModeRxQueryMismatch.setStatus(
        "current"
    )

vRtrMldHostRxQueryVerMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 46, 0, 9)
)
vRtrMldHostRxQueryVerMismatch.setObjects(
      *(("TIMETRA-MLD-MIB", "vRtrMldHostAdminVersion"),
        ("TIMETRA-MLD-MIB", "vRtrMldNotifyQueryVersion"))
)
if mibBuilder.loadTexts:
    vRtrMldHostRxQueryVerMismatch.setStatus(
        "current"
    )

vRtrMldHostMaxSrcsLimitExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 46, 0, 10)
)
vRtrMldHostMaxSrcsLimitExceeded.setObjects(
      *(("TIMETRA-MLD-MIB", "vRtrMldHostFwdSvcId"),
        ("TIMETRA-MLD-MIB", "vRtrMldHostGrpIfId"),
        ("TIMETRA-MLD-MIB", "vRtrMldHostMaxSources"))
)
if mibBuilder.loadTexts:
    vRtrMldHostMaxSrcsLimitExceeded.setStatus(
        "current"
    )

vRtrMldMaxSrcsLimitExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 46, 0, 11)
)
vRtrMldMaxSrcsLimitExceeded.setObjects(
    ("TIMETRA-MLD-MIB", "vRtrMldIfMaxSources")
)
if mibBuilder.loadTexts:
    vRtrMldMaxSrcsLimitExceeded.setStatus(
        "current"
    )

vRtrMldGrpIfSapMaxGrpsLimExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 46, 0, 12)
)
vRtrMldGrpIfSapMaxGrpsLimExceed.setObjects(
    ("TIMETRA-MLD-MIB", "vRtrMldGrpIfSapMaxGroups")
)
if mibBuilder.loadTexts:
    vRtrMldGrpIfSapMaxGrpsLimExceed.setStatus(
        "current"
    )

vRtrMldGrpIfSapMaxSrcsLimExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 46, 0, 13)
)
vRtrMldGrpIfSapMaxSrcsLimExceed.setObjects(
    ("TIMETRA-MLD-MIB", "vRtrMldGrpIfSapMaxSources")
)
if mibBuilder.loadTexts:
    vRtrMldGrpIfSapMaxSrcsLimExceed.setStatus(
        "current"
    )

vRtrMldGrpIfSapMcacPlcyDropped = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 46, 0, 14)
)
vRtrMldGrpIfSapMcacPlcyDropped.setObjects(
      *(("TIMETRA-MLD-MIB", "vRtrMldGrpIfSapLastChangeTime"),
        ("TIMETRA-MLD-MIB", "vRtrMldNotifyMcacPolicyName"),
        ("TIMETRA-MLD-MIB", "vRtrMldNotifyGrpAddrType"),
        ("TIMETRA-MLD-MIB", "vRtrMldNotifyGrpAddr"),
        ("TIMETRA-MLD-MIB", "vRtrMldNotifySrcAddrType"),
        ("TIMETRA-MLD-MIB", "vRtrMldNotifySrcAddr"),
        ("TIMETRA-MLD-MIB", "vRtrMldNotifyDescription"))
)
if mibBuilder.loadTexts:
    vRtrMldGrpIfSapMcacPlcyDropped.setStatus(
        "current"
    )

vRtrMldGrpIfSapCModeRxQueryMism = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 46, 0, 15)
)
vRtrMldGrpIfSapCModeRxQueryMism.setObjects(
      *(("TIMETRA-MLD-MIB", "vRtrMldGrpIfSapOperVersion"),
        ("TIMETRA-MLD-MIB", "vRtrMldNotifyQueryVersion"))
)
if mibBuilder.loadTexts:
    vRtrMldGrpIfSapCModeRxQueryMism.setStatus(
        "current"
    )

vRtrMldGrpIfSapRxQueryVerMism = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 46, 0, 16)
)
vRtrMldGrpIfSapRxQueryVerMism.setObjects(
      *(("TIMETRA-MLD-MIB", "vRtrMldGrpIfSapAdminVersion"),
        ("TIMETRA-MLD-MIB", "vRtrMldNotifyQueryVersion"))
)
if mibBuilder.loadTexts:
    vRtrMldGrpIfSapRxQueryVerMism.setStatus(
        "current"
    )

vRtrMldHostMaxGrpSrcsLimitExcd = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 46, 0, 17)
)
vRtrMldHostMaxGrpSrcsLimitExcd.setObjects(
      *(("TIMETRA-MLD-MIB", "vRtrMldHostFwdSvcId"),
        ("TIMETRA-MLD-MIB", "vRtrMldHostGrpIfId"),
        ("TIMETRA-MLD-MIB", "vRtrMldHostMaxGrpSources"))
)
if mibBuilder.loadTexts:
    vRtrMldHostMaxGrpSrcsLimitExcd.setStatus(
        "current"
    )

vRtrMldMaxGrpSrcsLimitExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 46, 0, 18)
)
vRtrMldMaxGrpSrcsLimitExceeded.setObjects(
    ("TIMETRA-MLD-MIB", "vRtrMldIfMaxGrpSources")
)
if mibBuilder.loadTexts:
    vRtrMldMaxGrpSrcsLimitExceeded.setStatus(
        "current"
    )

vRtrMldGrpIfSapMaxGrpSrcLimExcd = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 46, 0, 19)
)
vRtrMldGrpIfSapMaxGrpSrcLimExcd.setObjects(
    ("TIMETRA-MLD-MIB", "vRtrMldGrpIfSapMaxGrpSources")
)
if mibBuilder.loadTexts:
    vRtrMldGrpIfSapMaxGrpSrcLimExcd.setStatus(
        "current"
    )


# Notifications groups

tmnxMldNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 46, 2, 4)
)
tmnxMldNotificationGroup.setObjects(
      *(("TIMETRA-MLD-MIB", "vRtrMldIfRxQueryVerMismatch"),
        ("TIMETRA-MLD-MIB", "vRtrMldIfCModeRxQueryMismatch"),
        ("TIMETRA-MLD-MIB", "vRtrMldMaxGrpsLimitExceeded"))
)
if mibBuilder.loadTexts:
    tmnxMldNotificationGroup.setStatus(
        "current"
    )

tmnxMldNotificationV12v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 46, 2, 9)
)
tmnxMldNotificationV12v0Group.setObjects(
      *(("TIMETRA-MLD-MIB", "vRtrMldMcacPlcyDropped"),
        ("TIMETRA-MLD-MIB", "vRtrMldHostInstantiationFail"),
        ("TIMETRA-MLD-MIB", "vRtrMldHostMaxGrpsLimitExceeded"),
        ("TIMETRA-MLD-MIB", "vRtrMldHostMcacPlcyDropped"),
        ("TIMETRA-MLD-MIB", "vRtrMldHostCModeRxQueryMismatch"),
        ("TIMETRA-MLD-MIB", "vRtrMldHostRxQueryVerMismatch"),
        ("TIMETRA-MLD-MIB", "vRtrMldHostMaxSrcsLimitExceeded"),
        ("TIMETRA-MLD-MIB", "vRtrMldMaxSrcsLimitExceeded"),
        ("TIMETRA-MLD-MIB", "vRtrMldGrpIfSapMaxGrpsLimExceed"),
        ("TIMETRA-MLD-MIB", "vRtrMldGrpIfSapMaxSrcsLimExceed"),
        ("TIMETRA-MLD-MIB", "vRtrMldGrpIfSapMcacPlcyDropped"),
        ("TIMETRA-MLD-MIB", "vRtrMldGrpIfSapCModeRxQueryMism"),
        ("TIMETRA-MLD-MIB", "vRtrMldGrpIfSapRxQueryVerMism"),
        ("TIMETRA-MLD-MIB", "vRtrMldHostMaxGrpSrcsLimitExcd"),
        ("TIMETRA-MLD-MIB", "vRtrMldMaxGrpSrcsLimitExceeded"),
        ("TIMETRA-MLD-MIB", "vRtrMldGrpIfSapMaxGrpSrcLimExcd"))
)
if mibBuilder.loadTexts:
    tmnxMldNotificationV12v0Group.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tmnxMldCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 46, 1, 1)
)
tmnxMldCompliance.setObjects(
      *(("TIMETRA-MLD-MIB", "tmnxMldGlobalGroup"),
        ("TIMETRA-MLD-MIB", "tmnxMldIfGroup"),
        ("TIMETRA-MLD-MIB", "tmnxMldNotificationGroup"))
)
if mibBuilder.loadTexts:
    tmnxMldCompliance.setStatus(
        "obsolete"
    )

tmnxMldV6v1Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 46, 1, 2)
)
tmnxMldV6v1Compliance.setObjects(
      *(("TIMETRA-MLD-MIB", "tmnxMldGlobalGroup"),
        ("TIMETRA-MLD-MIB", "tmnxMldIfGroup"),
        ("TIMETRA-MLD-MIB", "tmnxMldNotificationGroup"),
        ("TIMETRA-MLD-MIB", "tmnxMldIfV6v1Group"))
)
if mibBuilder.loadTexts:
    tmnxMldV6v1Compliance.setStatus(
        "obsolete"
    )

tmnxMldV8v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 46, 1, 3)
)
tmnxMldV8v0Compliance.setObjects(
      *(("TIMETRA-MLD-MIB", "tmnxMldGlobalGroup"),
        ("TIMETRA-MLD-MIB", "tmnxMldIfGroup"),
        ("TIMETRA-MLD-MIB", "tmnxMldNotificationGroup"),
        ("TIMETRA-MLD-MIB", "tmnxMldIfV6v1Group"),
        ("TIMETRA-MLD-MIB", "tmnxMldIfV8v0Group"))
)
if mibBuilder.loadTexts:
    tmnxMldV8v0Compliance.setStatus(
        "obsolete"
    )

tmnxMldV12v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 46, 1, 4)
)
tmnxMldV12v0Compliance.setObjects(
      *(("TIMETRA-MLD-MIB", "tmnxMldGlobalGroup"),
        ("TIMETRA-MLD-MIB", "tmnxMldGlobalV12v0Group"),
        ("TIMETRA-MLD-MIB", "tmnxMldIfGroup"),
        ("TIMETRA-MLD-MIB", "tmnxMldNotificationGroup"),
        ("TIMETRA-MLD-MIB", "tmnxMldNotificationV12v0Group"),
        ("TIMETRA-MLD-MIB", "tmnxMldIfV6v1Group"),
        ("TIMETRA-MLD-MIB", "tmnxMldIfV8v0Group"),
        ("TIMETRA-MLD-MIB", "tmnxMldIfV12v0Group"))
)
if mibBuilder.loadTexts:
    tmnxMldV12v0Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-MLD-MIB",
    **{"MldGrpItfOperState": MldGrpItfOperState,
       "timetraMldMIBModule": timetraMldMIBModule,
       "tmnxMldConformance": tmnxMldConformance,
       "tmnxMldCompliances": tmnxMldCompliances,
       "tmnxMldCompliance": tmnxMldCompliance,
       "tmnxMldV6v1Compliance": tmnxMldV6v1Compliance,
       "tmnxMldV8v0Compliance": tmnxMldV8v0Compliance,
       "tmnxMldV12v0Compliance": tmnxMldV12v0Compliance,
       "tmnxMldGroups": tmnxMldGroups,
       "tmnxMldGlobalGroup": tmnxMldGlobalGroup,
       "tmnxMldIfGroup": tmnxMldIfGroup,
       "tmnxMldNotifyObjsGroup": tmnxMldNotifyObjsGroup,
       "tmnxMldNotificationGroup": tmnxMldNotificationGroup,
       "tmnxMldIfV6v1Group": tmnxMldIfV6v1Group,
       "tmnxMldIfV8v0Group": tmnxMldIfV8v0Group,
       "tmnxMldIfV12v0Group": tmnxMldIfV12v0Group,
       "tmnxMldNotifyObjsV12v0Group": tmnxMldNotifyObjsV12v0Group,
       "tmnxMldNotificationV12v0Group": tmnxMldNotificationV12v0Group,
       "tmnxMldGlobalV12v0Group": tmnxMldGlobalV12v0Group,
       "tmnxMldObjs": tmnxMldObjs,
       "vRtrMldProtocolObjs": vRtrMldProtocolObjs,
       "vRtrMldGeneralTableLastChanged": vRtrMldGeneralTableLastChanged,
       "vRtrMldGeneralTable": vRtrMldGeneralTable,
       "vRtrMldGeneralEntry": vRtrMldGeneralEntry,
       "vRtrMldGenQueryInterval": vRtrMldGenQueryInterval,
       "vRtrMldGenLastMembQueryIntvl": vRtrMldGenLastMembQueryIntvl,
       "vRtrMldGenQueryResponseIntvl": vRtrMldGenQueryResponseIntvl,
       "vRtrMldGenRobustCount": vRtrMldGenRobustCount,
       "vRtrMldGenLastChange": vRtrMldGenLastChange,
       "vRtrMldGenAdminState": vRtrMldGenAdminState,
       "vRtrMldGenOperState": vRtrMldGenOperState,
       "vRtrMldGenGrpIfQrySrcIpAddrType": vRtrMldGenGrpIfQrySrcIpAddrType,
       "vRtrMldGenGrpIfQrySrcIpAddr": vRtrMldGenGrpIfQrySrcIpAddr,
       "vRtrMldGrpSrcTable": vRtrMldGrpSrcTable,
       "vRtrMldGrpSrcEntry": vRtrMldGrpSrcEntry,
       "vRtrMldGrpSrcGroupAddrType": vRtrMldGrpSrcGroupAddrType,
       "vRtrMldGrpSrcGroupAddress": vRtrMldGrpSrcGroupAddress,
       "vRtrMldGrpSrcSourceAddrType": vRtrMldGrpSrcSourceAddrType,
       "vRtrMldGrpSrcSourceAddress": vRtrMldGrpSrcSourceAddress,
       "vRtrMldGrpSrcFwdOrBlk": vRtrMldGrpSrcFwdOrBlk,
       "vRtrMldGrpSrcUpTime": vRtrMldGrpSrcUpTime,
       "vRtrMldSsmTransTableLastChanged": vRtrMldSsmTransTableLastChanged,
       "vRtrMldSsmTransTable": vRtrMldSsmTransTable,
       "vRtrMldSsmTransEntry": vRtrMldSsmTransEntry,
       "vRtrMldSsmTransGrpAddrType1": vRtrMldSsmTransGrpAddrType1,
       "vRtrMldSsmTransGrpAddr1": vRtrMldSsmTransGrpAddr1,
       "vRtrMldSsmTransGrpAddrType2": vRtrMldSsmTransGrpAddrType2,
       "vRtrMldSsmTransGrpAddr2": vRtrMldSsmTransGrpAddr2,
       "vRtrMldSsmTransSrcAddrType": vRtrMldSsmTransSrcAddrType,
       "vRtrMldSsmTransSrcAddr": vRtrMldSsmTransSrcAddr,
       "vRtrMldSsmTransRowStatus": vRtrMldSsmTransRowStatus,
       "vRtrMldSsmTransLastChanged": vRtrMldSsmTransLastChanged,
       "vRtrMldGenStatsTable": vRtrMldGenStatsTable,
       "vRtrMldGenStatsEntry": vRtrMldGenStatsEntry,
       "vRtrMldGenStatsStarGTypes": vRtrMldGenStatsStarGTypes,
       "vRtrMldGenStatsSGTypes": vRtrMldGenStatsSGTypes,
       "vRtrMldGrpSrcSummaryTable": vRtrMldGrpSrcSummaryTable,
       "vRtrMldGrpSrcSummaryEntry": vRtrMldGrpSrcSummaryEntry,
       "vRtrMldGrpSrcSummFwdInterfaces": vRtrMldGrpSrcSummFwdInterfaces,
       "vRtrMldGrpSrcSummBlkInterfaces": vRtrMldGrpSrcSummBlkInterfaces,
       "vRtrMldGrpSrcSummFwdHosts": vRtrMldGrpSrcSummFwdHosts,
       "vRtrMldGrpSrcSummBlkHosts": vRtrMldGrpSrcSummBlkHosts,
       "vRtrMldGrpSrcSummFwdGrpIfSaps": vRtrMldGrpSrcSummFwdGrpIfSaps,
       "vRtrMldGrpSrcSummBlkGrpIfSaps": vRtrMldGrpSrcSummBlkGrpIfSaps,
       "vRtrMldIfObjs": vRtrMldIfObjs,
       "vRtrMldIfTableLastChanged": vRtrMldIfTableLastChanged,
       "vRtrMldIfTable": vRtrMldIfTable,
       "vRtrMldIfEntry": vRtrMldIfEntry,
       "vRtrMldIfRowStatus": vRtrMldIfRowStatus,
       "vRtrMldIfLastChanged": vRtrMldIfLastChanged,
       "vRtrMldIfAdminState": vRtrMldIfAdminState,
       "vRtrMldIfOperState": vRtrMldIfOperState,
       "vRtrMldIfAdminVersion": vRtrMldIfAdminVersion,
       "vRtrMldIfOperVersion": vRtrMldIfOperVersion,
       "vRtrMldIfQuerierType": vRtrMldIfQuerierType,
       "vRtrMldIfQuerier": vRtrMldIfQuerier,
       "vRtrMldIfImportPolicy": vRtrMldIfImportPolicy,
       "vRtrMldIfGroupCount": vRtrMldIfGroupCount,
       "vRtrMldIfQuerierUpTime": vRtrMldIfQuerierUpTime,
       "vRtrMldIfQuerierExpiryTime": vRtrMldIfQuerierExpiryTime,
       "vRtrMldIfNextGenQueryTime": vRtrMldIfNextGenQueryTime,
       "vRtrMldIfMaxGroups": vRtrMldIfMaxGroups,
       "vRtrMldIfMaxGroupsTillNow": vRtrMldIfMaxGroupsTillNow,
       "vRtrMldIfQueryInterval": vRtrMldIfQueryInterval,
       "vRtrMldIfLastMembQueryIntvl": vRtrMldIfLastMembQueryIntvl,
       "vRtrMldIfQueryResponseIntvl": vRtrMldIfQueryResponseIntvl,
       "vRtrMldIfDisRtrAlertChk": vRtrMldIfDisRtrAlertChk,
       "vRtrMldIfMcacPolicyName": vRtrMldIfMcacPolicyName,
       "vRtrMldIfMcacUnconstrainedBW": vRtrMldIfMcacUnconstrainedBW,
       "vRtrMldIfMcacConstAdminState": vRtrMldIfMcacConstAdminState,
       "vRtrMldIfMcacPreRsvdMandBW": vRtrMldIfMcacPreRsvdMandBW,
       "vRtrMldIfMcacinUseMandBw": vRtrMldIfMcacinUseMandBw,
       "vRtrMldIfMcacinUseOpnlBw": vRtrMldIfMcacinUseOpnlBw,
       "vRtrMldIfMcacAvailMandBw": vRtrMldIfMcacAvailMandBw,
       "vRtrMldIfMcacAvailOpnlBw": vRtrMldIfMcacAvailOpnlBw,
       "vRtrMldIfMcacValuesInTransit": vRtrMldIfMcacValuesInTransit,
       "vRtrMldIfMaxSources": vRtrMldIfMaxSources,
       "vRtrMldIfMaxGrpSources": vRtrMldIfMaxGrpSources,
       "vRtrMldIfMcacUseLagPortWeight": vRtrMldIfMcacUseLagPortWeight,
       "vRtrMldIfGroupTable": vRtrMldIfGroupTable,
       "vRtrMldIfGroupEntry": vRtrMldIfGroupEntry,
       "vRtrMldIfGroupAddressType": vRtrMldIfGroupAddressType,
       "vRtrMldIfGroupAddress": vRtrMldIfGroupAddress,
       "vRtrMldIfGroupType": vRtrMldIfGroupType,
       "vRtrMldIfGroupUpTime": vRtrMldIfGroupUpTime,
       "vRtrMldIfGroupExpiryTime": vRtrMldIfGroupExpiryTime,
       "vRtrMldIfGroupVer1HostTimer": vRtrMldIfGroupVer1HostTimer,
       "vRtrMldIfGroupMode": vRtrMldIfGroupMode,
       "vRtrMldIfGroupCompatMode": vRtrMldIfGroupCompatMode,
       "vRtrMldIfGroupLstRprtrType": vRtrMldIfGroupLstRprtrType,
       "vRtrMldIfGroupLastReporter": vRtrMldIfGroupLastReporter,
       "vRtrMldIfGrpSrcTable": vRtrMldIfGrpSrcTable,
       "vRtrMldIfGrpSrcEntry": vRtrMldIfGrpSrcEntry,
       "vRtrMldIfGrpSrcAddrType": vRtrMldIfGrpSrcAddrType,
       "vRtrMldIfGrpSrcAddress": vRtrMldIfGrpSrcAddress,
       "vRtrMldIfGrpSrcExpiryTime": vRtrMldIfGrpSrcExpiryTime,
       "vRtrMldIfGrpSrcType": vRtrMldIfGrpSrcType,
       "vRtrMldIfStatcGrpSrcTblLstChngd": vRtrMldIfStatcGrpSrcTblLstChngd,
       "vRtrMldIfStaticGrpSrcTable": vRtrMldIfStaticGrpSrcTable,
       "vRtrMldIfStaticGrpSrcEntry": vRtrMldIfStaticGrpSrcEntry,
       "vRtrMldIfStaticGrpSrcRowStatus": vRtrMldIfStaticGrpSrcRowStatus,
       "vRtrMldIfStaticGrpSrcLstChanged": vRtrMldIfStaticGrpSrcLstChanged,
       "vRtrMldIfStatsTable": vRtrMldIfStatsTable,
       "vRtrMldIfStatsEntry": vRtrMldIfStatsEntry,
       "vRtrMldIfTxGenQueries": vRtrMldIfTxGenQueries,
       "vRtrMldIfTxGrpQueries": vRtrMldIfTxGrpQueries,
       "vRtrMldIfTxGrpSrcQueries": vRtrMldIfTxGrpSrcQueries,
       "vRtrMldIfTxV1Reports": vRtrMldIfTxV1Reports,
       "vRtrMldIfTxV2Reports": vRtrMldIfTxV2Reports,
       "vRtrMldIfTxLeaves": vRtrMldIfTxLeaves,
       "vRtrMldIfTxErrors": vRtrMldIfTxErrors,
       "vRtrMldIfRxGenQueries": vRtrMldIfRxGenQueries,
       "vRtrMldIfRxGrpQueries": vRtrMldIfRxGrpQueries,
       "vRtrMldIfRxGrpSrcQueries": vRtrMldIfRxGrpSrcQueries,
       "vRtrMldIfRxV1Reports": vRtrMldIfRxV1Reports,
       "vRtrMldIfRxV2Reports": vRtrMldIfRxV2Reports,
       "vRtrMldIfRxLeaves": vRtrMldIfRxLeaves,
       "vRtrMldIfRxBadLenPkts": vRtrMldIfRxBadLenPkts,
       "vRtrMldIfRxBadChecksumPkts": vRtrMldIfRxBadChecksumPkts,
       "vRtrMldIfRxUnknownTypePkts": vRtrMldIfRxUnknownTypePkts,
       "vRtrMldIfRxBadReceiveIfPkts": vRtrMldIfRxBadReceiveIfPkts,
       "vRtrMldIfRxNonLocal": vRtrMldIfRxNonLocal,
       "vRtrMldIfRxWrongVersions": vRtrMldIfRxWrongVersions,
       "vRtrMldIfImportPolicyDrops": vRtrMldIfImportPolicyDrops,
       "vRtrMldIfRxNoRtrAlertPkts": vRtrMldIfRxNoRtrAlertPkts,
       "vRtrMldIfRxBadEncodings": vRtrMldIfRxBadEncodings,
       "vRtrMldIfRxPktDrops": vRtrMldIfRxPktDrops,
       "vRtrMldIfStatsStarGTypes": vRtrMldIfStatsStarGTypes,
       "vRtrMldIfStatsSGTypes": vRtrMldIfStatsSGTypes,
       "vRtrMldIfRxLocalScopePkts": vRtrMldIfRxLocalScopePkts,
       "vRtrMldIfRxRsvdScopePkts": vRtrMldIfRxRsvdScopePkts,
       "vRtrMldIfStatsMcacPolicyDrops": vRtrMldIfStatsMcacPolicyDrops,
       "vRtrMldIfSsmTltTableLastChanged": vRtrMldIfSsmTltTableLastChanged,
       "vRtrMldIfSsmTransTable": vRtrMldIfSsmTransTable,
       "vRtrMldIfSsmTransEntry": vRtrMldIfSsmTransEntry,
       "vRtrMldIfSsmTransGrpAddrType1": vRtrMldIfSsmTransGrpAddrType1,
       "vRtrMldIfSsmTransGrpAddr1": vRtrMldIfSsmTransGrpAddr1,
       "vRtrMldIfSsmTransGrpAddrType2": vRtrMldIfSsmTransGrpAddrType2,
       "vRtrMldIfSsmTransGrpAddr2": vRtrMldIfSsmTransGrpAddr2,
       "vRtrMldIfSsmTransSrcAddrType": vRtrMldIfSsmTransSrcAddrType,
       "vRtrMldIfSsmTransSrcAddr": vRtrMldIfSsmTransSrcAddr,
       "vRtrMldIfSsmTransRowStatus": vRtrMldIfSsmTransRowStatus,
       "vRtrMldIfMcacLevelTable": vRtrMldIfMcacLevelTable,
       "vRtrMldIfMcacLevelEntry": vRtrMldIfMcacLevelEntry,
       "vRtrMldIfMcacLevelRowStatus": vRtrMldIfMcacLevelRowStatus,
       "vRtrMldIfMcacLevelBW": vRtrMldIfMcacLevelBW,
       "vRtrMldIfMcacLagTable": vRtrMldIfMcacLagTable,
       "vRtrMldIfMcacLagEntry": vRtrMldIfMcacLagEntry,
       "vRtrMldIfMcacLagRowStatus": vRtrMldIfMcacLagRowStatus,
       "vRtrMldIfMcacLagLevel": vRtrMldIfMcacLagLevel,
       "vRtrMldNotificationObjs": vRtrMldNotificationObjs,
       "vRtrMldNotifyQueryVersion": vRtrMldNotifyQueryVersion,
       "vRtrMldNotifyGrpAddrType": vRtrMldNotifyGrpAddrType,
       "vRtrMldNotifyGrpAddr": vRtrMldNotifyGrpAddr,
       "vRtrMldNotifyDescription": vRtrMldNotifyDescription,
       "vRtrMldNotifyMcacPolicyName": vRtrMldNotifyMcacPolicyName,
       "vRtrMldNotifySrcAddrType": vRtrMldNotifySrcAddrType,
       "vRtrMldNotifySrcAddr": vRtrMldNotifySrcAddr,
       "vRtrMldHostObjs": vRtrMldHostObjs,
       "vRtrMldHostTable": vRtrMldHostTable,
       "vRtrMldHostEntry": vRtrMldHostEntry,
       "vRtrMldHostAddressType": vRtrMldHostAddressType,
       "vRtrMldHostAddress": vRtrMldHostAddress,
       "vRtrMldHostMacAddress": vRtrMldHostMacAddress,
       "vRtrMldHostPppoeSessionId": vRtrMldHostPppoeSessionId,
       "vRtrMldHostLastChangeTime": vRtrMldHostLastChangeTime,
       "vRtrMldHostOperState": vRtrMldHostOperState,
       "vRtrMldHostOperVersion": vRtrMldHostOperVersion,
       "vRtrMldHostGroupCount": vRtrMldHostGroupCount,
       "vRtrMldHostNextGenQueryTime": vRtrMldHostNextGenQueryTime,
       "vRtrMldHostMaxGroupsTillNow": vRtrMldHostMaxGroupsTillNow,
       "vRtrMldHostFwdSvcId": vRtrMldHostFwdSvcId,
       "vRtrMldHostGrpIfId": vRtrMldHostGrpIfId,
       "vRtrMldHostSubscriberId": vRtrMldHostSubscriberId,
       "vRtrMldHostMldPolicy": vRtrMldHostMldPolicy,
       "vRtrMldHostMaxGroups": vRtrMldHostMaxGroups,
       "vRtrMldHostAdminVersion": vRtrMldHostAdminVersion,
       "vRtrMldHostMaxSources": vRtrMldHostMaxSources,
       "vRtrMldHostMaxGrpSources": vRtrMldHostMaxGrpSources,
       "vRtrMldHostStatsTable": vRtrMldHostStatsTable,
       "vRtrMldHostStatsEntry": vRtrMldHostStatsEntry,
       "vRtrMldHostTxGenQueries": vRtrMldHostTxGenQueries,
       "vRtrMldHostTxGrpQueries": vRtrMldHostTxGrpQueries,
       "vRtrMldHostTxGrpSrcQueries": vRtrMldHostTxGrpSrcQueries,
       "vRtrMldHostTxV1Reports": vRtrMldHostTxV1Reports,
       "vRtrMldHostTxV2Reports": vRtrMldHostTxV2Reports,
       "vRtrMldHostTxLeaves": vRtrMldHostTxLeaves,
       "vRtrMldHostTxErrors": vRtrMldHostTxErrors,
       "vRtrMldHostRxGenQueries": vRtrMldHostRxGenQueries,
       "vRtrMldHostRxGrpQueries": vRtrMldHostRxGrpQueries,
       "vRtrMldHostRxGrpSrcQueries": vRtrMldHostRxGrpSrcQueries,
       "vRtrMldHostRxV1Reports": vRtrMldHostRxV1Reports,
       "vRtrMldHostRxV2Reports": vRtrMldHostRxV2Reports,
       "vRtrMldHostRxLeaves": vRtrMldHostRxLeaves,
       "vRtrMldHostRxBadLenPkts": vRtrMldHostRxBadLenPkts,
       "vRtrMldHostRxBadChecksumPkts": vRtrMldHostRxBadChecksumPkts,
       "vRtrMldHostRxUnknownTypePkts": vRtrMldHostRxUnknownTypePkts,
       "vRtrMldHostRxBadReceiveIfPkts": vRtrMldHostRxBadReceiveIfPkts,
       "vRtrMldHostRxNonLocal": vRtrMldHostRxNonLocal,
       "vRtrMldHostRxWrongVersions": vRtrMldHostRxWrongVersions,
       "vRtrMldHostImportPolicyDrops": vRtrMldHostImportPolicyDrops,
       "vRtrMldHostRxNoRtrAlertPkts": vRtrMldHostRxNoRtrAlertPkts,
       "vRtrMldHostRxBadEncodings": vRtrMldHostRxBadEncodings,
       "vRtrMldHostRxPktDrops": vRtrMldHostRxPktDrops,
       "vRtrMldHostStatsStarGTypes": vRtrMldHostStatsStarGTypes,
       "vRtrMldHostStatsSGTypes": vRtrMldHostStatsSGTypes,
       "vRtrMldHostStatsMcacPolicyDrops": vRtrMldHostStatsMcacPolicyDrops,
       "vRtrMldHostRxLocalScopePkts": vRtrMldHostRxLocalScopePkts,
       "vRtrMldHostRxRsvdScopePkts": vRtrMldHostRxRsvdScopePkts,
       "vRtrMldHostRedirectionDrops": vRtrMldHostRedirectionDrops,
       "vRtrMldGrpIfTable": vRtrMldGrpIfTable,
       "vRtrMldGrpIfEntry": vRtrMldGrpIfEntry,
       "vRtrMldGrpIfRowStatus": vRtrMldGrpIfRowStatus,
       "vRtrMldGrpIfLastChangeTime": vRtrMldGrpIfLastChangeTime,
       "vRtrMldGrpIfAdminState": vRtrMldGrpIfAdminState,
       "vRtrMldGrpIfOperState": vRtrMldGrpIfOperState,
       "vRtrMldGrpIfSubHostsOnly": vRtrMldGrpIfSubHostsOnly,
       "vRtrMldGrpIfAdminVersion": vRtrMldGrpIfAdminVersion,
       "vRtrMldGrpIfImportPolicy": vRtrMldGrpIfImportPolicy,
       "vRtrMldGrpIfSubnetCheck": vRtrMldGrpIfSubnetCheck,
       "vRtrMldGrpIfMcacPolicyName": vRtrMldGrpIfMcacPolicyName,
       "vRtrMldGrpIfMcacUnconstrainedBW": vRtrMldGrpIfMcacUnconstrainedBW,
       "vRtrMldGrpIfMcacConstAdminState": vRtrMldGrpIfMcacConstAdminState,
       "vRtrMldGrpIfMcacPreRsvdMandBW": vRtrMldGrpIfMcacPreRsvdMandBW,
       "vRtrMldGrpIfMcacinUseMandBw": vRtrMldGrpIfMcacinUseMandBw,
       "vRtrMldGrpIfMcacinUseOpnlBw": vRtrMldGrpIfMcacinUseOpnlBw,
       "vRtrMldGrpIfMcacAvailMandBw": vRtrMldGrpIfMcacAvailMandBw,
       "vRtrMldGrpIfMcacAvailOpnlBw": vRtrMldGrpIfMcacAvailOpnlBw,
       "vRtrMldGrpIfMcacValuesInTransit": vRtrMldGrpIfMcacValuesInTransit,
       "vRtrMldGrpIfDisRtrAlertChk": vRtrMldGrpIfDisRtrAlertChk,
       "vRtrMldGrpIfMaxGroups": vRtrMldGrpIfMaxGroups,
       "vRtrMldGrpIfMaxSources": vRtrMldGrpIfMaxSources,
       "vRtrMldGrpIfMaxGrpSources": vRtrMldGrpIfMaxGrpSources,
       "vRtrMldGrpIfQrySrcIpAddrType": vRtrMldGrpIfQrySrcIpAddrType,
       "vRtrMldGrpIfQrySrcIpAddr": vRtrMldGrpIfQrySrcIpAddr,
       "vRtrMldGrpIfHostGrpTable": vRtrMldGrpIfHostGrpTable,
       "vRtrMldGrpIfHostGrpEntry": vRtrMldGrpIfHostGrpEntry,
       "vRtrMldHostGroupAddressType": vRtrMldHostGroupAddressType,
       "vRtrMldHostGroupAddress": vRtrMldHostGroupAddress,
       "vRtrMldGrpIfHostGrpType": vRtrMldGrpIfHostGrpType,
       "vRtrMldGrpIfHostGrpUpTime": vRtrMldGrpIfHostGrpUpTime,
       "vRtrMldGrpIfHostGrpExpiryTime": vRtrMldGrpIfHostGrpExpiryTime,
       "vRtrMldGrpIfHostGrpVer1HostTmr": vRtrMldGrpIfHostGrpVer1HostTmr,
       "vRtrMldGrpIfHostGrpMode": vRtrMldGrpIfHostGrpMode,
       "vRtrMldGrpIfHostGrpCompatMode": vRtrMldGrpIfHostGrpCompatMode,
       "vRtrMldGrpIfHostGrpMRDstVrId": vRtrMldGrpIfHostGrpMRDstVrId,
       "vRtrMldGrpIfHostGrpMRDstIfId": vRtrMldGrpIfHostGrpMRDstIfId,
       "vRtrMldGrpIfHostGrpSrcTable": vRtrMldGrpIfHostGrpSrcTable,
       "vRtrMldGrpIfHostGrpSrcEntry": vRtrMldGrpIfHostGrpSrcEntry,
       "vRtrMldHostGrpSrcAddressType": vRtrMldHostGrpSrcAddressType,
       "vRtrMldHostGrpSrcAddress": vRtrMldHostGrpSrcAddress,
       "vRtrMldGrpIfHostGrpSrcExpTime": vRtrMldGrpIfHostGrpSrcExpTime,
       "vRtrMldGrpIfHostGrpSrcType": vRtrMldGrpIfHostGrpSrcType,
       "vRtrMldGrpIfHostGrpSrcMRDstVrId": vRtrMldGrpIfHostGrpSrcMRDstVrId,
       "vRtrMldGrpIfHostGrpSrcMRDstIfId": vRtrMldGrpIfHostGrpSrcMRDstIfId,
       "vRtrMldGrpSrcHostTable": vRtrMldGrpSrcHostTable,
       "vRtrMldGrpSrcHostEntry": vRtrMldGrpSrcHostEntry,
       "vRtrMldGrpSrcHostUpTime": vRtrMldGrpSrcHostUpTime,
       "vRtrMldHostGrpSrcTable": vRtrMldHostGrpSrcTable,
       "vRtrMldHostGrpSrcEntry": vRtrMldHostGrpSrcEntry,
       "vRtrMldHostGrpSrcExpiryTime": vRtrMldHostGrpSrcExpiryTime,
       "vRtrMldHostGrpSrcType": vRtrMldHostGrpSrcType,
       "vRtrMldHostGrpSrcMcRdrDstVRtrID": vRtrMldHostGrpSrcMcRdrDstVRtrID,
       "vRtrMldHostGrpSrcMcRdrDstIfIdx": vRtrMldHostGrpSrcMcRdrDstIfIdx,
       "vRtrMldHostGrpTable": vRtrMldHostGrpTable,
       "vRtrMldHostGrpEntry": vRtrMldHostGrpEntry,
       "vRtrMldHostGrpType": vRtrMldHostGrpType,
       "vRtrMldHostGrpUpTime": vRtrMldHostGrpUpTime,
       "vRtrMldHostGrpExpiryTime": vRtrMldHostGrpExpiryTime,
       "vRtrMldHostGrpVer1HostTmr": vRtrMldHostGrpVer1HostTmr,
       "vRtrMldHostGrpMode": vRtrMldHostGrpMode,
       "vRtrMldHostGrpCompatMode": vRtrMldHostGrpCompatMode,
       "vRtrMldHostGrpMcRdrDstVrId": vRtrMldHostGrpMcRdrDstVrId,
       "vRtrMldHostGrpMcRdrDstIfId": vRtrMldHostGrpMcRdrDstIfId,
       "vRtrMldGrpIfHostTable": vRtrMldGrpIfHostTable,
       "vRtrMldGrpIfHostEntry": vRtrMldGrpIfHostEntry,
       "vRtrMldGrpIfHostLastChangeTime": vRtrMldGrpIfHostLastChangeTime,
       "vRtrMldGrpIfHostOperState": vRtrMldGrpIfHostOperState,
       "vRtrMldGrpIfObjs": vRtrMldGrpIfObjs,
       "vRtrMldGrpIfSapTable": vRtrMldGrpIfSapTable,
       "vRtrMldGrpIfSapEntry": vRtrMldGrpIfSapEntry,
       "vRtrMldGrpIfSapLastChangeTime": vRtrMldGrpIfSapLastChangeTime,
       "vRtrMldGrpIfSapOperState": vRtrMldGrpIfSapOperState,
       "vRtrMldGrpIfSapAdminVersion": vRtrMldGrpIfSapAdminVersion,
       "vRtrMldGrpIfSapOperVersion": vRtrMldGrpIfSapOperVersion,
       "vRtrMldGrpIfSapGroupCount": vRtrMldGrpIfSapGroupCount,
       "vRtrMldGrpIfSapNextGenQueryTime": vRtrMldGrpIfSapNextGenQueryTime,
       "vRtrMldGrpIfSapMaxGroups": vRtrMldGrpIfSapMaxGroups,
       "vRtrMldGrpIfSapMaxGroupsTillNow": vRtrMldGrpIfSapMaxGroupsTillNow,
       "vRtrMldGrpIfSapMaxSources": vRtrMldGrpIfSapMaxSources,
       "vRtrMldGrpIfSapMaxGrpSources": vRtrMldGrpIfSapMaxGrpSources,
       "vRtrMldGrpIfSapStatsTable": vRtrMldGrpIfSapStatsTable,
       "vRtrMldGrpIfSapStatsEntry": vRtrMldGrpIfSapStatsEntry,
       "vRtrMldGrpIfSapTxGenQueries": vRtrMldGrpIfSapTxGenQueries,
       "vRtrMldGrpIfSapTxGrpQueries": vRtrMldGrpIfSapTxGrpQueries,
       "vRtrMldGrpIfSapTxGrpSrcQueries": vRtrMldGrpIfSapTxGrpSrcQueries,
       "vRtrMldGrpIfSapTxV1Reports": vRtrMldGrpIfSapTxV1Reports,
       "vRtrMldGrpIfSapTxV2Reports": vRtrMldGrpIfSapTxV2Reports,
       "vRtrMldGrpIfSapTxLeaves": vRtrMldGrpIfSapTxLeaves,
       "vRtrMldGrpIfSapTxErrors": vRtrMldGrpIfSapTxErrors,
       "vRtrMldGrpIfSapRxGenQueries": vRtrMldGrpIfSapRxGenQueries,
       "vRtrMldGrpIfSapRxGrpQueries": vRtrMldGrpIfSapRxGrpQueries,
       "vRtrMldGrpIfSapRxGrpSrcQueries": vRtrMldGrpIfSapRxGrpSrcQueries,
       "vRtrMldGrpIfSapRxV1Reports": vRtrMldGrpIfSapRxV1Reports,
       "vRtrMldGrpIfSapRxV2Reports": vRtrMldGrpIfSapRxV2Reports,
       "vRtrMldGrpIfSapRxLeaves": vRtrMldGrpIfSapRxLeaves,
       "vRtrMldGrpIfSapRxBadLenPkts": vRtrMldGrpIfSapRxBadLenPkts,
       "vRtrMldGrpIfSapRxBadChksumPkts": vRtrMldGrpIfSapRxBadChksumPkts,
       "vRtrMldGrpIfSapRxUnknTypePkts": vRtrMldGrpIfSapRxUnknTypePkts,
       "vRtrMldGrpIfSapRxBadRecvIfPkts": vRtrMldGrpIfSapRxBadRecvIfPkts,
       "vRtrMldGrpIfSapRxNonLocal": vRtrMldGrpIfSapRxNonLocal,
       "vRtrMldGrpIfSapRxWrongVersions": vRtrMldGrpIfSapRxWrongVersions,
       "vRtrMldGrpIfSapImportPlcyDrops": vRtrMldGrpIfSapImportPlcyDrops,
       "vRtrMldGrpIfSapRxNoRtrAlertPkts": vRtrMldGrpIfSapRxNoRtrAlertPkts,
       "vRtrMldGrpIfSapRxBadEncodings": vRtrMldGrpIfSapRxBadEncodings,
       "vRtrMldGrpIfSapRxPktDrops": vRtrMldGrpIfSapRxPktDrops,
       "vRtrMldGrpIfSapStatsStarGTypes": vRtrMldGrpIfSapStatsStarGTypes,
       "vRtrMldGrpIfSapStatsSGTypes": vRtrMldGrpIfSapStatsSGTypes,
       "vRtrMldGrpIfSapStatsMcacPlcyDrp": vRtrMldGrpIfSapStatsMcacPlcyDrp,
       "vRtrMldGrpIfSapRxLocalScopePkts": vRtrMldGrpIfSapRxLocalScopePkts,
       "vRtrMldGrpIfSapRxRsvdScopePkts": vRtrMldGrpIfSapRxRsvdScopePkts,
       "vRtrMldGrpIfSapGrpTable": vRtrMldGrpIfSapGrpTable,
       "vRtrMldGrpIfSapGrpEntry": vRtrMldGrpIfSapGrpEntry,
       "vRtrMldGrpIfSapGroupAddressType": vRtrMldGrpIfSapGroupAddressType,
       "vRtrMldGrpIfSapGroupAddress": vRtrMldGrpIfSapGroupAddress,
       "vRtrMldGrpIfSapGrpType": vRtrMldGrpIfSapGrpType,
       "vRtrMldGrpIfSapGrpUpTime": vRtrMldGrpIfSapGrpUpTime,
       "vRtrMldGrpIfSapGrpExpiryTime": vRtrMldGrpIfSapGrpExpiryTime,
       "vRtrMldGrpIfSapGrpVer1HostTmr": vRtrMldGrpIfSapGrpVer1HostTmr,
       "vRtrMldGrpIfSapGrpMode": vRtrMldGrpIfSapGrpMode,
       "vRtrMldGrpIfSapGrpCompatMode": vRtrMldGrpIfSapGrpCompatMode,
       "vRtrMldGrpIfSapGrpSrcTable": vRtrMldGrpIfSapGrpSrcTable,
       "vRtrMldGrpIfSapGrpSrcEntry": vRtrMldGrpIfSapGrpSrcEntry,
       "vRtrMldGrpIfSapGrpSrcAddressType": vRtrMldGrpIfSapGrpSrcAddressType,
       "vRtrMldGrpIfSapGrpSrcAddress": vRtrMldGrpIfSapGrpSrcAddress,
       "vRtrMldGrpIfSapGrpSrcExpTime": vRtrMldGrpIfSapGrpSrcExpTime,
       "vRtrMldGrpIfSapGrpSrcType": vRtrMldGrpIfSapGrpSrcType,
       "vRtrMldGrpSrcGrpIfSapTable": vRtrMldGrpSrcGrpIfSapTable,
       "vRtrMldGrpSrcGrpIfSapEntry": vRtrMldGrpSrcGrpIfSapEntry,
       "vRtrMldGrpSrcGrpIfSapUpTime": vRtrMldGrpSrcGrpIfSapUpTime,
       "vRtrMldNotifyPrefix": vRtrMldNotifyPrefix,
       "vRtrMldNotifications": vRtrMldNotifications,
       "vRtrMldIfRxQueryVerMismatch": vRtrMldIfRxQueryVerMismatch,
       "vRtrMldIfCModeRxQueryMismatch": vRtrMldIfCModeRxQueryMismatch,
       "vRtrMldMaxGrpsLimitExceeded": vRtrMldMaxGrpsLimitExceeded,
       "vRtrMldMcacPlcyDropped": vRtrMldMcacPlcyDropped,
       "vRtrMldHostInstantiationFail": vRtrMldHostInstantiationFail,
       "vRtrMldHostMaxGrpsLimitExceeded": vRtrMldHostMaxGrpsLimitExceeded,
       "vRtrMldHostMcacPlcyDropped": vRtrMldHostMcacPlcyDropped,
       "vRtrMldHostCModeRxQueryMismatch": vRtrMldHostCModeRxQueryMismatch,
       "vRtrMldHostRxQueryVerMismatch": vRtrMldHostRxQueryVerMismatch,
       "vRtrMldHostMaxSrcsLimitExceeded": vRtrMldHostMaxSrcsLimitExceeded,
       "vRtrMldMaxSrcsLimitExceeded": vRtrMldMaxSrcsLimitExceeded,
       "vRtrMldGrpIfSapMaxGrpsLimExceed": vRtrMldGrpIfSapMaxGrpsLimExceed,
       "vRtrMldGrpIfSapMaxSrcsLimExceed": vRtrMldGrpIfSapMaxSrcsLimExceed,
       "vRtrMldGrpIfSapMcacPlcyDropped": vRtrMldGrpIfSapMcacPlcyDropped,
       "vRtrMldGrpIfSapCModeRxQueryMism": vRtrMldGrpIfSapCModeRxQueryMism,
       "vRtrMldGrpIfSapRxQueryVerMism": vRtrMldGrpIfSapRxQueryVerMism,
       "vRtrMldHostMaxGrpSrcsLimitExcd": vRtrMldHostMaxGrpSrcsLimitExcd,
       "vRtrMldMaxGrpSrcsLimitExceeded": vRtrMldMaxGrpSrcsLimitExceeded,
       "vRtrMldGrpIfSapMaxGrpSrcLimExcd": vRtrMldGrpIfSapMaxGrpSrcLimExcd}
)
