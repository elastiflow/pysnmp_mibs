# SNMP MIB module (TIMETRA-MPLS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_6527/TIMETRA-MPLS-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 17:41:37 2025
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

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressIPv6,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressIPv6",
    "InetAddressType")

(MplsLSPID,
 MplsLabel,
 mplsInSegmentEntry,
 mplsOutSegmentEntry,
 mplsXCLspId) = mibBuilder.importSymbols(
    "MPLS-LSR-MIB",
    "MplsLSPID",
    "MplsLabel",
    "mplsInSegmentEntry",
    "mplsOutSegmentEntry",
    "mplsXCLspId")

(MplsTunnelIndex,
 mplsTunnelARHopEntry,
 mplsTunnelIndex,
 mplsTunnelIngressLSRId,
 mplsTunnelInstance) = mibBuilder.importSymbols(
    "MPLS-TE-MIB",
    "MplsTunnelIndex",
    "mplsTunnelARHopEntry",
    "mplsTunnelIndex",
    "mplsTunnelIngressLSRId",
    "mplsTunnelInstance")

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
 RowPointer,
 RowStatus,
 TextualConvention,
 TestAndIncr,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowPointer",
    "RowStatus",
    "TextualConvention",
    "TestAndIncr",
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

(TLNamedItem,
 TLNamedItemOrEmpty,
 TNamedItem,
 TNamedItemOrEmpty,
 TPolicyStatementNameOrEmpty,
 TmnxActionType,
 TmnxAdminState,
 TmnxCBFClasses,
 TmnxEnabledDisabled,
 TmnxMplsTpGlobalID,
 TmnxMplsTpNodeID,
 TmnxOperState,
 TmnxRsvpDSTEClassType,
 TmnxTimeInterval,
 TmnxVRtrMplsLspID) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TLNamedItem",
    "TLNamedItemOrEmpty",
    "TNamedItem",
    "TNamedItemOrEmpty",
    "TPolicyStatementNameOrEmpty",
    "TmnxActionType",
    "TmnxAdminState",
    "TmnxCBFClasses",
    "TmnxEnabledDisabled",
    "TmnxMplsTpGlobalID",
    "TmnxMplsTpNodeID",
    "TmnxOperState",
    "TmnxRsvpDSTEClassType",
    "TmnxTimeInterval",
    "TmnxVRtrMplsLspID")

(vRtrID,
 vRtrIfIndex) = mibBuilder.importSymbols(
    "TIMETRA-VRTR-MIB",
    "vRtrID",
    "vRtrIfIndex")


# MODULE-IDENTITY

timetraMplsMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 6)
)
if mibBuilder.loadTexts:
    timetraMplsMIBModule.setRevisions(
        ("2016-01-01 00:00",
         "2015-01-01 00:00",
         "2014-01-01 00:00",
         "2011-02-01 00:00",
         "2009-02-28 00:00",
         "2008-07-01 00:00",
         "2008-01-01 00:00",
         "2007-01-01 00:00",
         "2006-03-23 00:00",
         "2005-08-31 00:00",
         "2005-01-24 00:00",
         "2004-01-15 00:00",
         "2003-08-15 00:00",
         "2000-09-07 00:00",
         "2000-08-14 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TmnxMplsLspFailCode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              50)
        )
    )
    namedValues = NamedValues(
        *(("noError", 0),
          ("admissionControlError", 1),
          ("noRouteToDestination", 2),
          ("trafficControlSystemError", 3),
          ("routingError", 4),
          ("noResourcesAvailable", 5),
          ("badNode", 6),
          ("routingLoop", 7),
          ("labelAllocationError", 8),
          ("badL3PID", 9),
          ("tunnelLocallyRepaired", 10),
          ("unknownObjectClass", 11),
          ("unknownCType", 12),
          ("noEgressMplsInterface", 13),
          ("noEgressRsvpInterface", 14),
          ("looseHopsInFRRLsp", 15),
          ("unknown", 16),
          ("retryExceeded", 17),
          ("noCspfRouteOwner", 18),
          ("noCspfRouteToDestination", 19),
          ("hopLimitExceeded", 20),
          ("looseHopsInManualBypassLsp", 21),
          ("emptyPathInManualBypassLsp", 22),
          ("lspFlowControlled", 23),
          ("srlgSecondaryNotDisjoint", 24),
          ("srlgPrimaryCspfDisabled", 25),
          ("srlgPrimaryPathDown", 26),
          ("localLinkMaintenance", 27),
          ("unexpectedCtObject", 28),
          ("unsupportedCt", 29),
          ("invalidCt", 30),
          ("invCtAndSetupPri", 31),
          ("invCtAndHoldPri", 32),
          ("invCtAndSetupAndHoldPri", 33),
          ("localNodeMaintenance", 34),
          ("softPreemption", 35),
          ("p2mpNotSupported", 36),
          ("badXro", 37),
          ("localNodeInXro", 38),
          ("routeBlockedByXro", 39),
          ("xroTooComplex", 40),
          ("rsvpNotSupported", 41),
          ("conflictingAdminGroups", 42),
          ("nodeInIgpOverload", 43),
          ("srTunnelDown", 44),
          ("fibAddFailed", 45),
          ("labelStackExceeded", 46),
          ("pccDown", 47),
          ("pccError", 48),
          ("pceDown", 49),
          ("pceError", 50))
    )



class TmnxMplsLabelOwner(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("none", 0),
          ("rsvp", 1),
          ("tldp", 2),
          ("ildp", 3),
          ("svcmgr", 4),
          ("bgp", 5),
          ("mirror", 6),
          ("static", 7),
          ("vprn", 8),
          ("sr", 9))
    )



class TmnxMplsOperDownReasonCode(TextualConvention, Integer32):
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
        *(("operUp", 0),
          ("adminDown", 1),
          ("noResources", 2),
          ("systemIpDown", 3),
          ("iomFailure", 4),
          ("clearDown", 5))
    )



class TmnxMplsMBBType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("none", 0),
          ("configChange", 1),
          ("timerBasedResignal", 2),
          ("manualResignal", 3),
          ("globalRevert", 4),
          ("delayedRetry", 5),
          ("gracefulShutdown", 6),
          ("softPreemption", 7),
          ("pathChange", 8),
          ("autoBandwidth", 9),
          ("pceLspUpdate", 10))
    )



class TmnxMplsP2mpInstFailCode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noError", 0),
          ("noS2LOperational", 1))
    )



class TmnxMplsRouterId(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



class TmnxMplsLspAutoBWLastAdjCause(TextualConvention, Integer32):
    status = "current"
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
        *(("none", 0),
          ("manual", 1),
          ("normal", 2),
          ("overflow", 3),
          ("vllCAC", 4),
          ("underflow", 5),
          ("activePathChange", 6))
    )



class TmnxMplsLspBgpRSVPLSPTunState(TextualConvention, Integer32):
    status = "current"
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



class TmnxMplsLspAddrType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("nodeId", 2))
    )



class TmnxMplsClassFwdSetId(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )



# MIB Managed Objects in the order of their OIDs

_TmnxMplsConformance_ObjectIdentity = ObjectIdentity
tmnxMplsConformance = _TmnxMplsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6)
)
_TmnxMplsCompliances_ObjectIdentity = ObjectIdentity
tmnxMplsCompliances = _TmnxMplsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 1)
)
_TmnxMplsGroups_ObjectIdentity = ObjectIdentity
tmnxMplsGroups = _TmnxMplsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2)
)
_TmnxMplsObjs_ObjectIdentity = ObjectIdentity
tmnxMplsObjs = _TmnxMplsObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6)
)
_VRtrMplsLspTable_Object = MibTable
vRtrMplsLspTable = _VRtrMplsLspTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1)
)
if mibBuilder.loadTexts:
    vRtrMplsLspTable.setStatus("current")
_VRtrMplsLspEntry_Object = MibTableRow
vRtrMplsLspEntry = _VRtrMplsLspEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1)
)
vRtrMplsLspEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsLspIndex"),
)
if mibBuilder.loadTexts:
    vRtrMplsLspEntry.setStatus("current")
_VRtrMplsLspIndex_Type = TmnxVRtrMplsLspID
_VRtrMplsLspIndex_Object = MibTableColumn
vRtrMplsLspIndex = _VRtrMplsLspIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 1),
    _VRtrMplsLspIndex_Type()
)
vRtrMplsLspIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrMplsLspIndex.setStatus("current")
_VRtrMplsLspRowStatus_Type = RowStatus
_VRtrMplsLspRowStatus_Object = MibTableColumn
vRtrMplsLspRowStatus = _VRtrMplsLspRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 2),
    _VRtrMplsLspRowStatus_Type()
)
vRtrMplsLspRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspRowStatus.setStatus("current")
_VRtrMplsLspLastChange_Type = TimeStamp
_VRtrMplsLspLastChange_Object = MibTableColumn
vRtrMplsLspLastChange = _VRtrMplsLspLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 3),
    _VRtrMplsLspLastChange_Type()
)
vRtrMplsLspLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspLastChange.setStatus("current")
_VRtrMplsLspName_Type = TLNamedItemOrEmpty
_VRtrMplsLspName_Object = MibTableColumn
vRtrMplsLspName = _VRtrMplsLspName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 4),
    _VRtrMplsLspName_Type()
)
vRtrMplsLspName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspName.setStatus("current")


class _VRtrMplsLspAdminState_Type(TmnxAdminState):
    """Custom type vRtrMplsLspAdminState based on TmnxAdminState"""
    defaultValue = 3


_VRtrMplsLspAdminState_Type.__name__ = "TmnxAdminState"
_VRtrMplsLspAdminState_Object = MibTableColumn
vRtrMplsLspAdminState = _VRtrMplsLspAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 5),
    _VRtrMplsLspAdminState_Type()
)
vRtrMplsLspAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspAdminState.setStatus("current")
_VRtrMplsLspOperState_Type = TmnxOperState
_VRtrMplsLspOperState_Object = MibTableColumn
vRtrMplsLspOperState = _VRtrMplsLspOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 6),
    _VRtrMplsLspOperState_Type()
)
vRtrMplsLspOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspOperState.setStatus("current")
_VRtrMplsLspFromAddr_Type = IpAddress
_VRtrMplsLspFromAddr_Object = MibTableColumn
vRtrMplsLspFromAddr = _VRtrMplsLspFromAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 7),
    _VRtrMplsLspFromAddr_Type()
)
vRtrMplsLspFromAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspFromAddr.setStatus("current")
_VRtrMplsLspToAddr_Type = IpAddress
_VRtrMplsLspToAddr_Object = MibTableColumn
vRtrMplsLspToAddr = _VRtrMplsLspToAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 8),
    _VRtrMplsLspToAddr_Type()
)
vRtrMplsLspToAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspToAddr.setStatus("current")


class _VRtrMplsLspType_Type(Integer32):
    """Custom type vRtrMplsLspType based on Integer32"""
    defaultValue = 2

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
        *(("unknown", 1),
          ("dynamic", 2),
          ("static", 3),
          ("bypassOnly", 4),
          ("p2mpLsp", 5),
          ("p2mpAuto", 6),
          ("mplsTp", 7),
          ("meshP2p", 8),
          ("oneHopP2p", 9),
          ("srTe", 10))
    )


_VRtrMplsLspType_Type.__name__ = "Integer32"
_VRtrMplsLspType_Object = MibTableColumn
vRtrMplsLspType = _VRtrMplsLspType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 9),
    _VRtrMplsLspType_Type()
)
vRtrMplsLspType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspType.setStatus("current")


class _VRtrMplsLspOutSegIndx_Type(Integer32):
    """Custom type vRtrMplsLspOutSegIndx based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_VRtrMplsLspOutSegIndx_Type.__name__ = "Integer32"
_VRtrMplsLspOutSegIndx_Object = MibTableColumn
vRtrMplsLspOutSegIndx = _VRtrMplsLspOutSegIndx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 10),
    _VRtrMplsLspOutSegIndx_Type()
)
vRtrMplsLspOutSegIndx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspOutSegIndx.setStatus("current")


class _VRtrMplsLspRetryTimer_Type(Unsigned32):
    """Custom type vRtrMplsLspRetryTimer based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_VRtrMplsLspRetryTimer_Type.__name__ = "Unsigned32"
_VRtrMplsLspRetryTimer_Object = MibTableColumn
vRtrMplsLspRetryTimer = _VRtrMplsLspRetryTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 11),
    _VRtrMplsLspRetryTimer_Type()
)
vRtrMplsLspRetryTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspRetryTimer.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspRetryTimer.setUnits("seconds")


class _VRtrMplsLspRetryLimit_Type(Unsigned32):
    """Custom type vRtrMplsLspRetryLimit based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_VRtrMplsLspRetryLimit_Type.__name__ = "Unsigned32"
_VRtrMplsLspRetryLimit_Object = MibTableColumn
vRtrMplsLspRetryLimit = _VRtrMplsLspRetryLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 12),
    _VRtrMplsLspRetryLimit_Type()
)
vRtrMplsLspRetryLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspRetryLimit.setStatus("current")


class _VRtrMplsLspMetric_Type(Unsigned32):
    """Custom type vRtrMplsLspMetric based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 16777215),
    )


_VRtrMplsLspMetric_Type.__name__ = "Unsigned32"
_VRtrMplsLspMetric_Object = MibTableColumn
vRtrMplsLspMetric = _VRtrMplsLspMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 13),
    _VRtrMplsLspMetric_Type()
)
vRtrMplsLspMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspMetric.setStatus("current")


class _VRtrMplsLspDecrementTtl_Type(TruthValue):
    """Custom type vRtrMplsLspDecrementTtl based on TruthValue"""
    defaultValue = 1


_VRtrMplsLspDecrementTtl_Type.__name__ = "TruthValue"
_VRtrMplsLspDecrementTtl_Object = MibTableColumn
vRtrMplsLspDecrementTtl = _VRtrMplsLspDecrementTtl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 14),
    _VRtrMplsLspDecrementTtl_Type()
)
vRtrMplsLspDecrementTtl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspDecrementTtl.setStatus("obsolete")


class _VRtrMplsLspCspf_Type(TruthValue):
    """Custom type vRtrMplsLspCspf based on TruthValue"""
    defaultValue = 2


_VRtrMplsLspCspf_Type.__name__ = "TruthValue"
_VRtrMplsLspCspf_Object = MibTableColumn
vRtrMplsLspCspf = _VRtrMplsLspCspf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 15),
    _VRtrMplsLspCspf_Type()
)
vRtrMplsLspCspf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspCspf.setStatus("current")


class _VRtrMplsLspFastReroute_Type(TruthValue):
    """Custom type vRtrMplsLspFastReroute based on TruthValue"""
    defaultValue = 2


_VRtrMplsLspFastReroute_Type.__name__ = "TruthValue"
_VRtrMplsLspFastReroute_Object = MibTableColumn
vRtrMplsLspFastReroute = _VRtrMplsLspFastReroute_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 16),
    _VRtrMplsLspFastReroute_Type()
)
vRtrMplsLspFastReroute.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspFastReroute.setStatus("current")


class _VRtrMplsLspFRHopLimit_Type(Unsigned32):
    """Custom type vRtrMplsLspFRHopLimit based on Unsigned32"""
    defaultValue = 16

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VRtrMplsLspFRHopLimit_Type.__name__ = "Unsigned32"
_VRtrMplsLspFRHopLimit_Object = MibTableColumn
vRtrMplsLspFRHopLimit = _VRtrMplsLspFRHopLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 17),
    _VRtrMplsLspFRHopLimit_Type()
)
vRtrMplsLspFRHopLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspFRHopLimit.setStatus("current")


class _VRtrMplsLspFRBandwidth_Type(Unsigned32):
    """Custom type vRtrMplsLspFRBandwidth based on Unsigned32"""
    defaultValue = 0


_VRtrMplsLspFRBandwidth_Type.__name__ = "Unsigned32"
_VRtrMplsLspFRBandwidth_Object = MibTableColumn
vRtrMplsLspFRBandwidth = _VRtrMplsLspFRBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 18),
    _VRtrMplsLspFRBandwidth_Type()
)
vRtrMplsLspFRBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspFRBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspFRBandwidth.setUnits("mega-bits per second")


class _VRtrMplsLspClassOfService_Type(TNamedItemOrEmpty):
    """Custom type vRtrMplsLspClassOfService based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_VRtrMplsLspClassOfService_Type.__name__ = "TNamedItemOrEmpty"
_VRtrMplsLspClassOfService_Object = MibTableColumn
vRtrMplsLspClassOfService = _VRtrMplsLspClassOfService_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 19),
    _VRtrMplsLspClassOfService_Type()
)
vRtrMplsLspClassOfService.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspClassOfService.setStatus("obsolete")


class _VRtrMplsLspSetupPriority_Type(Unsigned32):
    """Custom type vRtrMplsLspSetupPriority based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_VRtrMplsLspSetupPriority_Type.__name__ = "Unsigned32"
_VRtrMplsLspSetupPriority_Object = MibTableColumn
vRtrMplsLspSetupPriority = _VRtrMplsLspSetupPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 20),
    _VRtrMplsLspSetupPriority_Type()
)
vRtrMplsLspSetupPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspSetupPriority.setStatus("current")


class _VRtrMplsLspHoldPriority_Type(Unsigned32):
    """Custom type vRtrMplsLspHoldPriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_VRtrMplsLspHoldPriority_Type.__name__ = "Unsigned32"
_VRtrMplsLspHoldPriority_Object = MibTableColumn
vRtrMplsLspHoldPriority = _VRtrMplsLspHoldPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 21),
    _VRtrMplsLspHoldPriority_Type()
)
vRtrMplsLspHoldPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspHoldPriority.setStatus("current")


class _VRtrMplsLspRecord_Type(TruthValue):
    """Custom type vRtrMplsLspRecord based on TruthValue"""
    defaultValue = 1


_VRtrMplsLspRecord_Type.__name__ = "TruthValue"
_VRtrMplsLspRecord_Object = MibTableColumn
vRtrMplsLspRecord = _VRtrMplsLspRecord_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 22),
    _VRtrMplsLspRecord_Type()
)
vRtrMplsLspRecord.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspRecord.setStatus("current")


class _VRtrMplsLspPreference_Type(Unsigned32):
    """Custom type vRtrMplsLspPreference based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_VRtrMplsLspPreference_Type.__name__ = "Unsigned32"
_VRtrMplsLspPreference_Object = MibTableColumn
vRtrMplsLspPreference = _VRtrMplsLspPreference_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 23),
    _VRtrMplsLspPreference_Type()
)
vRtrMplsLspPreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspPreference.setStatus("obsolete")


class _VRtrMplsLspBandwidth_Type(Integer32):
    """Custom type vRtrMplsLspBandwidth based on Integer32"""
    defaultValue = 0


_VRtrMplsLspBandwidth_Type.__name__ = "Integer32"
_VRtrMplsLspBandwidth_Object = MibTableColumn
vRtrMplsLspBandwidth = _VRtrMplsLspBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 24),
    _VRtrMplsLspBandwidth_Type()
)
vRtrMplsLspBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspBandwidth.setStatus("obsolete")
if mibBuilder.loadTexts:
    vRtrMplsLspBandwidth.setUnits("mega-bits per second")


class _VRtrMplsLspBwProtect_Type(TruthValue):
    """Custom type vRtrMplsLspBwProtect based on TruthValue"""
    defaultValue = 2


_VRtrMplsLspBwProtect_Type.__name__ = "TruthValue"
_VRtrMplsLspBwProtect_Object = MibTableColumn
vRtrMplsLspBwProtect = _VRtrMplsLspBwProtect_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 25),
    _VRtrMplsLspBwProtect_Type()
)
vRtrMplsLspBwProtect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspBwProtect.setStatus("obsolete")


class _VRtrMplsLspHopLimit_Type(Unsigned32):
    """Custom type vRtrMplsLspHopLimit based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 255),
    )


_VRtrMplsLspHopLimit_Type.__name__ = "Unsigned32"
_VRtrMplsLspHopLimit_Object = MibTableColumn
vRtrMplsLspHopLimit = _VRtrMplsLspHopLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 26),
    _VRtrMplsLspHopLimit_Type()
)
vRtrMplsLspHopLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspHopLimit.setStatus("current")


class _VRtrMplsLspNegotiatedMTU_Type(Unsigned32):
    """Custom type vRtrMplsLspNegotiatedMTU based on Unsigned32"""
    defaultValue = 0


_VRtrMplsLspNegotiatedMTU_Type.__name__ = "Unsigned32"
_VRtrMplsLspNegotiatedMTU_Object = MibTableColumn
vRtrMplsLspNegotiatedMTU = _VRtrMplsLspNegotiatedMTU_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 27),
    _VRtrMplsLspNegotiatedMTU_Type()
)
vRtrMplsLspNegotiatedMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspNegotiatedMTU.setStatus("current")


class _VRtrMplsLspRsvpResvStyle_Type(Integer32):
    """Custom type vRtrMplsLspRsvpResvStyle based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("se", 1),
          ("ff", 2))
    )


_VRtrMplsLspRsvpResvStyle_Type.__name__ = "Integer32"
_VRtrMplsLspRsvpResvStyle_Object = MibTableColumn
vRtrMplsLspRsvpResvStyle = _VRtrMplsLspRsvpResvStyle_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 28),
    _VRtrMplsLspRsvpResvStyle_Type()
)
vRtrMplsLspRsvpResvStyle.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspRsvpResvStyle.setStatus("current")


class _VRtrMplsLspRsvpAdspec_Type(TruthValue):
    """Custom type vRtrMplsLspRsvpAdspec based on TruthValue"""
    defaultValue = 2


_VRtrMplsLspRsvpAdspec_Type.__name__ = "TruthValue"
_VRtrMplsLspRsvpAdspec_Object = MibTableColumn
vRtrMplsLspRsvpAdspec = _VRtrMplsLspRsvpAdspec_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 29),
    _VRtrMplsLspRsvpAdspec_Type()
)
vRtrMplsLspRsvpAdspec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspRsvpAdspec.setStatus("current")


class _VRtrMplsLspFRMethod_Type(Integer32):
    """Custom type vRtrMplsLspFRMethod based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oneToOneBackup", 1),
          ("facilityBackup", 2))
    )


_VRtrMplsLspFRMethod_Type.__name__ = "Integer32"
_VRtrMplsLspFRMethod_Object = MibTableColumn
vRtrMplsLspFRMethod = _VRtrMplsLspFRMethod_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 30),
    _VRtrMplsLspFRMethod_Type()
)
vRtrMplsLspFRMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspFRMethod.setStatus("current")


class _VRtrMplsLspFRNodeProtect_Type(TruthValue):
    """Custom type vRtrMplsLspFRNodeProtect based on TruthValue"""
    defaultValue = 1


_VRtrMplsLspFRNodeProtect_Type.__name__ = "TruthValue"
_VRtrMplsLspFRNodeProtect_Object = MibTableColumn
vRtrMplsLspFRNodeProtect = _VRtrMplsLspFRNodeProtect_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 31),
    _VRtrMplsLspFRNodeProtect_Type()
)
vRtrMplsLspFRNodeProtect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspFRNodeProtect.setStatus("current")


class _VRtrMplsLspAdminGroupInclude_Type(Unsigned32):
    """Custom type vRtrMplsLspAdminGroupInclude based on Unsigned32"""
    defaultValue = 0


_VRtrMplsLspAdminGroupInclude_Type.__name__ = "Unsigned32"
_VRtrMplsLspAdminGroupInclude_Object = MibTableColumn
vRtrMplsLspAdminGroupInclude = _VRtrMplsLspAdminGroupInclude_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 32),
    _VRtrMplsLspAdminGroupInclude_Type()
)
vRtrMplsLspAdminGroupInclude.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspAdminGroupInclude.setStatus("current")


class _VRtrMplsLspAdminGroupExclude_Type(Unsigned32):
    """Custom type vRtrMplsLspAdminGroupExclude based on Unsigned32"""
    defaultValue = 0


_VRtrMplsLspAdminGroupExclude_Type.__name__ = "Unsigned32"
_VRtrMplsLspAdminGroupExclude_Object = MibTableColumn
vRtrMplsLspAdminGroupExclude = _VRtrMplsLspAdminGroupExclude_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 33),
    _VRtrMplsLspAdminGroupExclude_Type()
)
vRtrMplsLspAdminGroupExclude.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspAdminGroupExclude.setStatus("current")


class _VRtrMplsLspAdaptive_Type(TruthValue):
    """Custom type vRtrMplsLspAdaptive based on TruthValue"""
    defaultValue = 1


_VRtrMplsLspAdaptive_Type.__name__ = "TruthValue"
_VRtrMplsLspAdaptive_Object = MibTableColumn
vRtrMplsLspAdaptive = _VRtrMplsLspAdaptive_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 34),
    _VRtrMplsLspAdaptive_Type()
)
vRtrMplsLspAdaptive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspAdaptive.setStatus("current")


class _VRtrMplsLspInheritance_Type(Unsigned32):
    """Custom type vRtrMplsLspInheritance based on Unsigned32"""
    defaultValue = 0


_VRtrMplsLspInheritance_Type.__name__ = "Unsigned32"
_VRtrMplsLspInheritance_Object = MibTableColumn
vRtrMplsLspInheritance = _VRtrMplsLspInheritance_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 35),
    _VRtrMplsLspInheritance_Type()
)
vRtrMplsLspInheritance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspInheritance.setStatus("current")


class _VRtrMplsLspOptimizeTimer_Type(Unsigned32):
    """Custom type vRtrMplsLspOptimizeTimer based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VRtrMplsLspOptimizeTimer_Type.__name__ = "Unsigned32"
_VRtrMplsLspOptimizeTimer_Object = MibTableColumn
vRtrMplsLspOptimizeTimer = _VRtrMplsLspOptimizeTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 36),
    _VRtrMplsLspOptimizeTimer_Type()
)
vRtrMplsLspOptimizeTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspOptimizeTimer.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspOptimizeTimer.setUnits("seconds")
_VRtrMplsLspOperFastReroute_Type = TruthValue
_VRtrMplsLspOperFastReroute_Object = MibTableColumn
vRtrMplsLspOperFastReroute = _VRtrMplsLspOperFastReroute_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 37),
    _VRtrMplsLspOperFastReroute_Type()
)
vRtrMplsLspOperFastReroute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspOperFastReroute.setStatus("current")


class _VRtrMplsLspFRObject_Type(TruthValue):
    """Custom type vRtrMplsLspFRObject based on TruthValue"""
    defaultValue = 1


_VRtrMplsLspFRObject_Type.__name__ = "TruthValue"
_VRtrMplsLspFRObject_Object = MibTableColumn
vRtrMplsLspFRObject = _VRtrMplsLspFRObject_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 38),
    _VRtrMplsLspFRObject_Type()
)
vRtrMplsLspFRObject.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspFRObject.setStatus("current")


class _VRtrMplsLspHoldTimer_Type(Unsigned32):
    """Custom type vRtrMplsLspHoldTimer based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_VRtrMplsLspHoldTimer_Type.__name__ = "Unsigned32"
_VRtrMplsLspHoldTimer_Object = MibTableColumn
vRtrMplsLspHoldTimer = _VRtrMplsLspHoldTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 39),
    _VRtrMplsLspHoldTimer_Type()
)
vRtrMplsLspHoldTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspHoldTimer.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspHoldTimer.setUnits("seconds")


class _VRtrMplsLspCspfTeMetricEnabled_Type(TruthValue):
    """Custom type vRtrMplsLspCspfTeMetricEnabled based on TruthValue"""
    defaultValue = 2


_VRtrMplsLspCspfTeMetricEnabled_Type.__name__ = "TruthValue"
_VRtrMplsLspCspfTeMetricEnabled_Object = MibTableColumn
vRtrMplsLspCspfTeMetricEnabled = _VRtrMplsLspCspfTeMetricEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 40),
    _VRtrMplsLspCspfTeMetricEnabled_Type()
)
vRtrMplsLspCspfTeMetricEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspCspfTeMetricEnabled.setStatus("current")


class _VRtrMplsLspP2mpId_Type(Unsigned32):
    """Custom type vRtrMplsLspP2mpId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 65535),
    )


_VRtrMplsLspP2mpId_Type.__name__ = "Unsigned32"
_VRtrMplsLspP2mpId_Object = MibTableColumn
vRtrMplsLspP2mpId = _VRtrMplsLspP2mpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 41),
    _VRtrMplsLspP2mpId_Type()
)
vRtrMplsLspP2mpId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspP2mpId.setStatus("current")


class _VRtrMplsLspClassType_Type(TmnxRsvpDSTEClassType):
    """Custom type vRtrMplsLspClassType based on TmnxRsvpDSTEClassType"""
    defaultValue = 0


_VRtrMplsLspClassType_Type.__name__ = "TmnxRsvpDSTEClassType"
_VRtrMplsLspClassType_Object = MibTableColumn
vRtrMplsLspClassType = _VRtrMplsLspClassType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 42),
    _VRtrMplsLspClassType_Type()
)
vRtrMplsLspClassType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspClassType.setStatus("current")
_VRtrMplsLspOperMetric_Type = Unsigned32
_VRtrMplsLspOperMetric_Object = MibTableColumn
vRtrMplsLspOperMetric = _VRtrMplsLspOperMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 43),
    _VRtrMplsLspOperMetric_Type()
)
vRtrMplsLspOperMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspOperMetric.setStatus("current")


class _VRtrMplsLspLdpOverRsvpInclude_Type(TruthValue):
    """Custom type vRtrMplsLspLdpOverRsvpInclude based on TruthValue"""
    defaultValue = 1


_VRtrMplsLspLdpOverRsvpInclude_Type.__name__ = "TruthValue"
_VRtrMplsLspLdpOverRsvpInclude_Object = MibTableColumn
vRtrMplsLspLdpOverRsvpInclude = _VRtrMplsLspLdpOverRsvpInclude_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 44),
    _VRtrMplsLspLdpOverRsvpInclude_Type()
)
vRtrMplsLspLdpOverRsvpInclude.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspLdpOverRsvpInclude.setStatus("current")


class _VRtrMplsLspLeastFill_Type(TruthValue):
    """Custom type vRtrMplsLspLeastFill based on TruthValue"""
    defaultValue = 2


_VRtrMplsLspLeastFill_Type.__name__ = "TruthValue"
_VRtrMplsLspLeastFill_Object = MibTableColumn
vRtrMplsLspLeastFill = _VRtrMplsLspLeastFill_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 45),
    _VRtrMplsLspLeastFill_Type()
)
vRtrMplsLspLeastFill.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspLeastFill.setStatus("current")


class _VRtrMplsLspVprnAutoBindInclude_Type(TruthValue):
    """Custom type vRtrMplsLspVprnAutoBindInclude based on TruthValue"""
    defaultValue = 1


_VRtrMplsLspVprnAutoBindInclude_Type.__name__ = "TruthValue"
_VRtrMplsLspVprnAutoBindInclude_Object = MibTableColumn
vRtrMplsLspVprnAutoBindInclude = _VRtrMplsLspVprnAutoBindInclude_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 46),
    _VRtrMplsLspVprnAutoBindInclude_Type()
)
vRtrMplsLspVprnAutoBindInclude.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspVprnAutoBindInclude.setStatus("current")


class _VRtrMplsLspMainCTRetryLimit_Type(Unsigned32):
    """Custom type vRtrMplsLspMainCTRetryLimit based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_VRtrMplsLspMainCTRetryLimit_Type.__name__ = "Unsigned32"
_VRtrMplsLspMainCTRetryLimit_Object = MibTableColumn
vRtrMplsLspMainCTRetryLimit = _VRtrMplsLspMainCTRetryLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 47),
    _VRtrMplsLspMainCTRetryLimit_Type()
)
vRtrMplsLspMainCTRetryLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspMainCTRetryLimit.setStatus("current")


class _VRtrMplsLspIgpShortcut_Type(TruthValue):
    """Custom type vRtrMplsLspIgpShortcut based on TruthValue"""
    defaultValue = 1


_VRtrMplsLspIgpShortcut_Type.__name__ = "TruthValue"
_VRtrMplsLspIgpShortcut_Object = MibTableColumn
vRtrMplsLspIgpShortcut = _VRtrMplsLspIgpShortcut_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 48),
    _VRtrMplsLspIgpShortcut_Type()
)
vRtrMplsLspIgpShortcut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspIgpShortcut.setStatus("current")
_VRtrMplsLspOriginTemplate_Type = TNamedItemOrEmpty
_VRtrMplsLspOriginTemplate_Object = MibTableColumn
vRtrMplsLspOriginTemplate = _VRtrMplsLspOriginTemplate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 49),
    _VRtrMplsLspOriginTemplate_Type()
)
vRtrMplsLspOriginTemplate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspOriginTemplate.setStatus("current")


class _VRtrMplsLspAutoBandwidth_Type(TruthValue):
    """Custom type vRtrMplsLspAutoBandwidth based on TruthValue"""
    defaultValue = 2


_VRtrMplsLspAutoBandwidth_Type.__name__ = "TruthValue"
_VRtrMplsLspAutoBandwidth_Object = MibTableColumn
vRtrMplsLspAutoBandwidth = _VRtrMplsLspAutoBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 50),
    _VRtrMplsLspAutoBandwidth_Type()
)
vRtrMplsLspAutoBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBandwidth.setStatus("current")


class _VRtrMplsLspCspfToFirstLoose_Type(TruthValue):
    """Custom type vRtrMplsLspCspfToFirstLoose based on TruthValue"""
    defaultValue = 2


_VRtrMplsLspCspfToFirstLoose_Type.__name__ = "TruthValue"
_VRtrMplsLspCspfToFirstLoose_Object = MibTableColumn
vRtrMplsLspCspfToFirstLoose = _VRtrMplsLspCspfToFirstLoose_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 51),
    _VRtrMplsLspCspfToFirstLoose_Type()
)
vRtrMplsLspCspfToFirstLoose.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspCspfToFirstLoose.setStatus("obsolete")


class _VRtrMplsLspPropAdminGroup_Type(TruthValue):
    """Custom type vRtrMplsLspPropAdminGroup based on TruthValue"""
    defaultValue = 2


_VRtrMplsLspPropAdminGroup_Type.__name__ = "TruthValue"
_VRtrMplsLspPropAdminGroup_Object = MibTableColumn
vRtrMplsLspPropAdminGroup = _VRtrMplsLspPropAdminGroup_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 52),
    _VRtrMplsLspPropAdminGroup_Type()
)
vRtrMplsLspPropAdminGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspPropAdminGroup.setStatus("current")


class _VRtrMplsLspBgpShortcut_Type(TruthValue):
    """Custom type vRtrMplsLspBgpShortcut based on TruthValue"""
    defaultValue = 1


_VRtrMplsLspBgpShortcut_Type.__name__ = "TruthValue"
_VRtrMplsLspBgpShortcut_Object = MibTableColumn
vRtrMplsLspBgpShortcut = _VRtrMplsLspBgpShortcut_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 53),
    _VRtrMplsLspBgpShortcut_Type()
)
vRtrMplsLspBgpShortcut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspBgpShortcut.setStatus("current")


class _VRtrMplsLspBgpTransportTunnel_Type(TmnxMplsLspBgpRSVPLSPTunState):
    """Custom type vRtrMplsLspBgpTransportTunnel based on TmnxMplsLspBgpRSVPLSPTunState"""
    defaultValue = 1


_VRtrMplsLspBgpTransportTunnel_Type.__name__ = "TmnxMplsLspBgpRSVPLSPTunState"
_VRtrMplsLspBgpTransportTunnel_Object = MibTableColumn
vRtrMplsLspBgpTransportTunnel = _VRtrMplsLspBgpTransportTunnel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 54),
    _VRtrMplsLspBgpTransportTunnel_Type()
)
vRtrMplsLspBgpTransportTunnel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspBgpTransportTunnel.setStatus("current")
_VRtrMplsLspSwitchStbyPath_Type = TmnxActionType
_VRtrMplsLspSwitchStbyPath_Object = MibTableColumn
vRtrMplsLspSwitchStbyPath = _VRtrMplsLspSwitchStbyPath_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 55),
    _VRtrMplsLspSwitchStbyPath_Type()
)
vRtrMplsLspSwitchStbyPath.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspSwitchStbyPath.setStatus("current")
_VRtrMplsLspSwitchStbyPathIndex_Type = MplsTunnelIndex
_VRtrMplsLspSwitchStbyPathIndex_Object = MibTableColumn
vRtrMplsLspSwitchStbyPathIndex = _VRtrMplsLspSwitchStbyPathIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 56),
    _VRtrMplsLspSwitchStbyPathIndex_Type()
)
vRtrMplsLspSwitchStbyPathIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspSwitchStbyPathIndex.setStatus("current")


class _VRtrMplsLspSwitchStbyPathForce_Type(TruthValue):
    """Custom type vRtrMplsLspSwitchStbyPathForce based on TruthValue"""
    defaultValue = 2


_VRtrMplsLspSwitchStbyPathForce_Type.__name__ = "TruthValue"
_VRtrMplsLspSwitchStbyPathForce_Object = MibTableColumn
vRtrMplsLspSwitchStbyPathForce = _VRtrMplsLspSwitchStbyPathForce_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 57),
    _VRtrMplsLspSwitchStbyPathForce_Type()
)
vRtrMplsLspSwitchStbyPathForce.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspSwitchStbyPathForce.setStatus("current")
_VRtrMplsLspExcludeNodeAddrType_Type = InetAddressType
_VRtrMplsLspExcludeNodeAddrType_Object = MibTableColumn
vRtrMplsLspExcludeNodeAddrType = _VRtrMplsLspExcludeNodeAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 58),
    _VRtrMplsLspExcludeNodeAddrType_Type()
)
vRtrMplsLspExcludeNodeAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspExcludeNodeAddrType.setStatus("current")


class _VRtrMplsLspExcludeNodeAddr_Type(InetAddress):
    """Custom type vRtrMplsLspExcludeNodeAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_VRtrMplsLspExcludeNodeAddr_Type.__name__ = "InetAddress"
_VRtrMplsLspExcludeNodeAddr_Object = MibTableColumn
vRtrMplsLspExcludeNodeAddr = _VRtrMplsLspExcludeNodeAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 59),
    _VRtrMplsLspExcludeNodeAddr_Type()
)
vRtrMplsLspExcludeNodeAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspExcludeNodeAddr.setStatus("current")


class _VRtrMplsLspIgpShortcutLfaType_Type(Integer32):
    """Custom type vRtrMplsLspIgpShortcutLfaType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("lfaProtect", 1),
          ("lfaOnly", 2))
    )


_VRtrMplsLspIgpShortcutLfaType_Type.__name__ = "Integer32"
_VRtrMplsLspIgpShortcutLfaType_Object = MibTableColumn
vRtrMplsLspIgpShortcutLfaType = _VRtrMplsLspIgpShortcutLfaType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 60),
    _VRtrMplsLspIgpShortcutLfaType_Type()
)
vRtrMplsLspIgpShortcutLfaType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspIgpShortcutLfaType.setStatus("current")


class _VRtrMplsLspToAddrType_Type(TmnxMplsLspAddrType):
    """Custom type vRtrMplsLspToAddrType based on TmnxMplsLspAddrType"""
    defaultValue = 1


_VRtrMplsLspToAddrType_Type.__name__ = "TmnxMplsLspAddrType"
_VRtrMplsLspToAddrType_Object = MibTableColumn
vRtrMplsLspToAddrType = _VRtrMplsLspToAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 61),
    _VRtrMplsLspToAddrType_Type()
)
vRtrMplsLspToAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspToAddrType.setStatus("current")


class _VRtrMplsLspFromAddrType_Type(TmnxMplsLspAddrType):
    """Custom type vRtrMplsLspFromAddrType based on TmnxMplsLspAddrType"""
    defaultValue = 1


_VRtrMplsLspFromAddrType_Type.__name__ = "TmnxMplsLspAddrType"
_VRtrMplsLspFromAddrType_Object = MibTableColumn
vRtrMplsLspFromAddrType = _VRtrMplsLspFromAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 62),
    _VRtrMplsLspFromAddrType_Type()
)
vRtrMplsLspFromAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspFromAddrType.setStatus("current")


class _VRtrMplsLspToNodeId_Type(TmnxMplsTpNodeID):
    """Custom type vRtrMplsLspToNodeId based on TmnxMplsTpNodeID"""
    defaultValue = 0


_VRtrMplsLspToNodeId_Type.__name__ = "TmnxMplsTpNodeID"
_VRtrMplsLspToNodeId_Object = MibTableColumn
vRtrMplsLspToNodeId = _VRtrMplsLspToNodeId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 63),
    _VRtrMplsLspToNodeId_Type()
)
vRtrMplsLspToNodeId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspToNodeId.setStatus("current")
_VRtrMplsLspFromNodeId_Type = TmnxMplsTpNodeID
_VRtrMplsLspFromNodeId_Object = MibTableColumn
vRtrMplsLspFromNodeId = _VRtrMplsLspFromNodeId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 64),
    _VRtrMplsLspFromNodeId_Type()
)
vRtrMplsLspFromNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspFromNodeId.setStatus("current")


class _VRtrMplsLspDestGlobalId_Type(TmnxMplsTpGlobalID):
    """Custom type vRtrMplsLspDestGlobalId based on TmnxMplsTpGlobalID"""
    defaultValue = 0


_VRtrMplsLspDestGlobalId_Type.__name__ = "TmnxMplsTpGlobalID"
_VRtrMplsLspDestGlobalId_Object = MibTableColumn
vRtrMplsLspDestGlobalId = _VRtrMplsLspDestGlobalId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 65),
    _VRtrMplsLspDestGlobalId_Type()
)
vRtrMplsLspDestGlobalId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspDestGlobalId.setStatus("current")


class _VRtrMplsLspDestTunnelNum_Type(Unsigned32):
    """Custom type vRtrMplsLspDestTunnelNum based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 61440),
    )


_VRtrMplsLspDestTunnelNum_Type.__name__ = "Unsigned32"
_VRtrMplsLspDestTunnelNum_Object = MibTableColumn
vRtrMplsLspDestTunnelNum = _VRtrMplsLspDestTunnelNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 66),
    _VRtrMplsLspDestTunnelNum_Type()
)
vRtrMplsLspDestTunnelNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspDestTunnelNum.setStatus("current")


class _VRtrMplsLspFRPropAdminGroup_Type(TruthValue):
    """Custom type vRtrMplsLspFRPropAdminGroup based on TruthValue"""
    defaultValue = 2


_VRtrMplsLspFRPropAdminGroup_Type.__name__ = "TruthValue"
_VRtrMplsLspFRPropAdminGroup_Object = MibTableColumn
vRtrMplsLspFRPropAdminGroup = _VRtrMplsLspFRPropAdminGroup_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 67),
    _VRtrMplsLspFRPropAdminGroup_Type()
)
vRtrMplsLspFRPropAdminGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspFRPropAdminGroup.setStatus("current")


class _VRtrMplsLspIgpShortcutRelOffset_Type(Integer32):
    """Custom type vRtrMplsLspIgpShortcutRelOffset based on Integer32"""
    defaultValue = 2147483647

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-10, 10),
        ValueRangeConstraint(2147483647, 2147483647),
    )


_VRtrMplsLspIgpShortcutRelOffset_Type.__name__ = "Integer32"
_VRtrMplsLspIgpShortcutRelOffset_Object = MibTableColumn
vRtrMplsLspIgpShortcutRelOffset = _VRtrMplsLspIgpShortcutRelOffset_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 68),
    _VRtrMplsLspIgpShortcutRelOffset_Type()
)
vRtrMplsLspIgpShortcutRelOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspIgpShortcutRelOffset.setStatus("current")


class _VRtrMplsLspRevertTimer_Type(Unsigned32):
    """Custom type vRtrMplsLspRevertTimer based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4320),
    )


_VRtrMplsLspRevertTimer_Type.__name__ = "Unsigned32"
_VRtrMplsLspRevertTimer_Object = MibTableColumn
vRtrMplsLspRevertTimer = _VRtrMplsLspRevertTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 69),
    _VRtrMplsLspRevertTimer_Type()
)
vRtrMplsLspRevertTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspRevertTimer.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspRevertTimer.setUnits("minutes")
_VRtrMplsLspRevertTimeRemain_Type = Unsigned32
_VRtrMplsLspRevertTimeRemain_Object = MibTableColumn
vRtrMplsLspRevertTimeRemain = _VRtrMplsLspRevertTimeRemain_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 70),
    _VRtrMplsLspRevertTimeRemain_Type()
)
vRtrMplsLspRevertTimeRemain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspRevertTimeRemain.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspRevertTimeRemain.setUnits("minutes")


class _VRtrMplsLspLoadBalancingWeight_Type(Unsigned32):
    """Custom type vRtrMplsLspLoadBalancingWeight based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4294967295),
    )


_VRtrMplsLspLoadBalancingWeight_Type.__name__ = "Unsigned32"
_VRtrMplsLspLoadBalancingWeight_Object = MibTableColumn
vRtrMplsLspLoadBalancingWeight = _VRtrMplsLspLoadBalancingWeight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 71),
    _VRtrMplsLspLoadBalancingWeight_Type()
)
vRtrMplsLspLoadBalancingWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspLoadBalancingWeight.setStatus("current")


class _VRtrMplsLspClassFwdingEnabled_Type(TruthValue):
    """Custom type vRtrMplsLspClassFwdingEnabled based on TruthValue"""
    defaultValue = 2


_VRtrMplsLspClassFwdingEnabled_Type.__name__ = "TruthValue"
_VRtrMplsLspClassFwdingEnabled_Object = MibTableColumn
vRtrMplsLspClassFwdingEnabled = _VRtrMplsLspClassFwdingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 72),
    _VRtrMplsLspClassFwdingEnabled_Type()
)
vRtrMplsLspClassFwdingEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspClassFwdingEnabled.setStatus("current")


class _VRtrMplsLspFC_Type(TmnxCBFClasses):
    """Custom type vRtrMplsLspFC based on TmnxCBFClasses"""
    defaultBinValue = "0"


_VRtrMplsLspFC_Type.__name__ = "TmnxCBFClasses"
_VRtrMplsLspFC_Object = MibTableColumn
vRtrMplsLspFC = _VRtrMplsLspFC_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 73),
    _VRtrMplsLspFC_Type()
)
vRtrMplsLspFC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspFC.setStatus("current")
_VRtrMplsLspBfdTemplateName_Type = TNamedItemOrEmpty
_VRtrMplsLspBfdTemplateName_Object = MibTableColumn
vRtrMplsLspBfdTemplateName = _VRtrMplsLspBfdTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 74),
    _VRtrMplsLspBfdTemplateName_Type()
)
vRtrMplsLspBfdTemplateName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspBfdTemplateName.setStatus("current")


class _VRtrMplsLspBfdEnable_Type(TruthValue):
    """Custom type vRtrMplsLspBfdEnable based on TruthValue"""
    defaultValue = 2


_VRtrMplsLspBfdEnable_Type.__name__ = "TruthValue"
_VRtrMplsLspBfdEnable_Object = MibTableColumn
vRtrMplsLspBfdEnable = _VRtrMplsLspBfdEnable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 75),
    _VRtrMplsLspBfdEnable_Type()
)
vRtrMplsLspBfdEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspBfdEnable.setStatus("current")


class _VRtrMplsLspBfdPingIntvl_Type(Unsigned32):
    """Custom type vRtrMplsLspBfdPingIntvl based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(60, 300),
    )


_VRtrMplsLspBfdPingIntvl_Type.__name__ = "Unsigned32"
_VRtrMplsLspBfdPingIntvl_Object = MibTableColumn
vRtrMplsLspBfdPingIntvl = _VRtrMplsLspBfdPingIntvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 76),
    _VRtrMplsLspBfdPingIntvl_Type()
)
vRtrMplsLspBfdPingIntvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspBfdPingIntvl.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspBfdPingIntvl.setUnits("seconds")
_VRtrMplsLspStatTable_Object = MibTable
vRtrMplsLspStatTable = _VRtrMplsLspStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 2)
)
if mibBuilder.loadTexts:
    vRtrMplsLspStatTable.setStatus("current")
_VRtrMplsLspStatEntry_Object = MibTableRow
vRtrMplsLspStatEntry = _VRtrMplsLspStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 2, 1)
)
if mibBuilder.loadTexts:
    vRtrMplsLspStatEntry.setStatus("current")
_VRtrMplsLspOctets_Type = Counter64
_VRtrMplsLspOctets_Object = MibTableColumn
vRtrMplsLspOctets = _VRtrMplsLspOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 2, 1, 1),
    _VRtrMplsLspOctets_Type()
)
vRtrMplsLspOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspOctets.setStatus("current")
_VRtrMplsLspPackets_Type = Counter64
_VRtrMplsLspPackets_Object = MibTableColumn
vRtrMplsLspPackets = _VRtrMplsLspPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 2, 1, 2),
    _VRtrMplsLspPackets_Type()
)
vRtrMplsLspPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPackets.setStatus("current")
_VRtrMplsLspAge_Type = TmnxTimeInterval
_VRtrMplsLspAge_Object = MibTableColumn
vRtrMplsLspAge = _VRtrMplsLspAge_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 2, 1, 3),
    _VRtrMplsLspAge_Type()
)
vRtrMplsLspAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspAge.setStatus("current")
_VRtrMplsLspTimeUp_Type = TmnxTimeInterval
_VRtrMplsLspTimeUp_Object = MibTableColumn
vRtrMplsLspTimeUp = _VRtrMplsLspTimeUp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 2, 1, 4),
    _VRtrMplsLspTimeUp_Type()
)
vRtrMplsLspTimeUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspTimeUp.setStatus("current")
_VRtrMplsLspTimeDown_Type = TmnxTimeInterval
_VRtrMplsLspTimeDown_Object = MibTableColumn
vRtrMplsLspTimeDown = _VRtrMplsLspTimeDown_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 2, 1, 5),
    _VRtrMplsLspTimeDown_Type()
)
vRtrMplsLspTimeDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspTimeDown.setStatus("current")
_VRtrMplsLspPrimaryTimeUp_Type = TmnxTimeInterval
_VRtrMplsLspPrimaryTimeUp_Object = MibTableColumn
vRtrMplsLspPrimaryTimeUp = _VRtrMplsLspPrimaryTimeUp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 2, 1, 6),
    _VRtrMplsLspPrimaryTimeUp_Type()
)
vRtrMplsLspPrimaryTimeUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPrimaryTimeUp.setStatus("current")
_VRtrMplsLspTransitions_Type = Counter32
_VRtrMplsLspTransitions_Object = MibTableColumn
vRtrMplsLspTransitions = _VRtrMplsLspTransitions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 2, 1, 7),
    _VRtrMplsLspTransitions_Type()
)
vRtrMplsLspTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspTransitions.setStatus("current")
_VRtrMplsLspLastTransition_Type = TmnxTimeInterval
_VRtrMplsLspLastTransition_Object = MibTableColumn
vRtrMplsLspLastTransition = _VRtrMplsLspLastTransition_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 2, 1, 8),
    _VRtrMplsLspLastTransition_Type()
)
vRtrMplsLspLastTransition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspLastTransition.setStatus("current")
_VRtrMplsLspPathChanges_Type = Counter32
_VRtrMplsLspPathChanges_Object = MibTableColumn
vRtrMplsLspPathChanges = _VRtrMplsLspPathChanges_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 2, 1, 9),
    _VRtrMplsLspPathChanges_Type()
)
vRtrMplsLspPathChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathChanges.setStatus("current")
_VRtrMplsLspLastPathChange_Type = TmnxTimeInterval
_VRtrMplsLspLastPathChange_Object = MibTableColumn
vRtrMplsLspLastPathChange = _VRtrMplsLspLastPathChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 2, 1, 10),
    _VRtrMplsLspLastPathChange_Type()
)
vRtrMplsLspLastPathChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspLastPathChange.setStatus("current")
_VRtrMplsLspConfiguredPaths_Type = Integer32
_VRtrMplsLspConfiguredPaths_Object = MibTableColumn
vRtrMplsLspConfiguredPaths = _VRtrMplsLspConfiguredPaths_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 2, 1, 11),
    _VRtrMplsLspConfiguredPaths_Type()
)
vRtrMplsLspConfiguredPaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspConfiguredPaths.setStatus("current")
_VRtrMplsLspStandbyPaths_Type = Integer32
_VRtrMplsLspStandbyPaths_Object = MibTableColumn
vRtrMplsLspStandbyPaths = _VRtrMplsLspStandbyPaths_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 2, 1, 12),
    _VRtrMplsLspStandbyPaths_Type()
)
vRtrMplsLspStandbyPaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspStandbyPaths.setStatus("current")
_VRtrMplsLspOperationalPaths_Type = Integer32
_VRtrMplsLspOperationalPaths_Object = MibTableColumn
vRtrMplsLspOperationalPaths = _VRtrMplsLspOperationalPaths_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 2, 1, 13),
    _VRtrMplsLspOperationalPaths_Type()
)
vRtrMplsLspOperationalPaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspOperationalPaths.setStatus("current")
_VRtrMplsLspConfP2mpInstances_Type = Gauge32
_VRtrMplsLspConfP2mpInstances_Object = MibTableColumn
vRtrMplsLspConfP2mpInstances = _VRtrMplsLspConfP2mpInstances_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 2, 1, 14),
    _VRtrMplsLspConfP2mpInstances_Type()
)
vRtrMplsLspConfP2mpInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspConfP2mpInstances.setStatus("current")
_VRtrMplsLspStatsEgrIndexUnAvail_Type = TruthValue
_VRtrMplsLspStatsEgrIndexUnAvail_Object = MibTableColumn
vRtrMplsLspStatsEgrIndexUnAvail = _VRtrMplsLspStatsEgrIndexUnAvail_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 2, 1, 15),
    _VRtrMplsLspStatsEgrIndexUnAvail_Type()
)
vRtrMplsLspStatsEgrIndexUnAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspStatsEgrIndexUnAvail.setStatus("current")


class _VRtrMplsLspPathTableSpinlock_Type(TestAndIncr):
    """Custom type vRtrMplsLspPathTableSpinlock based on TestAndIncr"""
    defaultValue = 0


_VRtrMplsLspPathTableSpinlock_Type.__name__ = "TestAndIncr"
_VRtrMplsLspPathTableSpinlock_Object = MibScalar
vRtrMplsLspPathTableSpinlock = _VRtrMplsLspPathTableSpinlock_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 3),
    _VRtrMplsLspPathTableSpinlock_Type()
)
vRtrMplsLspPathTableSpinlock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLspPathTableSpinlock.setStatus("current")
_VRtrMplsLspPathTable_Object = MibTable
vRtrMplsLspPathTable = _VRtrMplsLspPathTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4)
)
if mibBuilder.loadTexts:
    vRtrMplsLspPathTable.setStatus("current")
_VRtrMplsLspPathEntry_Object = MibTableRow
vRtrMplsLspPathEntry = _VRtrMplsLspPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1)
)
vRtrMplsLspPathEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsLspIndex"),
    (0, "MPLS-TE-MIB", "mplsTunnelIndex"),
    (0, "MPLS-TE-MIB", "mplsTunnelInstance"),
    (0, "MPLS-TE-MIB", "mplsTunnelIngressLSRId"),
)
if mibBuilder.loadTexts:
    vRtrMplsLspPathEntry.setStatus("current")
_VRtrMplsLspPathRowStatus_Type = RowStatus
_VRtrMplsLspPathRowStatus_Object = MibTableColumn
vRtrMplsLspPathRowStatus = _VRtrMplsLspPathRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 1),
    _VRtrMplsLspPathRowStatus_Type()
)
vRtrMplsLspPathRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspPathRowStatus.setStatus("current")
_VRtrMplsLspPathLastChange_Type = TimeStamp
_VRtrMplsLspPathLastChange_Object = MibTableColumn
vRtrMplsLspPathLastChange = _VRtrMplsLspPathLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 2),
    _VRtrMplsLspPathLastChange_Type()
)
vRtrMplsLspPathLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathLastChange.setStatus("current")


class _VRtrMplsLspPathType_Type(Integer32):
    """Custom type vRtrMplsLspPathType based on Integer32"""
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
        *(("other", 1),
          ("primary", 2),
          ("standby", 3),
          ("secondary", 4))
    )


_VRtrMplsLspPathType_Type.__name__ = "Integer32"
_VRtrMplsLspPathType_Object = MibTableColumn
vRtrMplsLspPathType = _VRtrMplsLspPathType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 3),
    _VRtrMplsLspPathType_Type()
)
vRtrMplsLspPathType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspPathType.setStatus("current")


class _VRtrMplsLspPathCos_Type(Integer32):
    """Custom type vRtrMplsLspPathCos based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_VRtrMplsLspPathCos_Type.__name__ = "Integer32"
_VRtrMplsLspPathCos_Object = MibTableColumn
vRtrMplsLspPathCos = _VRtrMplsLspPathCos_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 4),
    _VRtrMplsLspPathCos_Type()
)
vRtrMplsLspPathCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspPathCos.setStatus("obsolete")


class _VRtrMplsLspPathProperties_Type(Bits):
    """Custom type vRtrMplsLspPathProperties based on Bits"""
    namedValues = NamedValues(
        *(("record-route", 0),
          ("adaptive", 1),
          ("cspf", 2),
          ("mergeable", 3),
          ("fast-reroute", 4),
          ("pce-reported", 5),
          ("pce-controlled", 6))
    )

_VRtrMplsLspPathProperties_Type.__name__ = "Bits"
_VRtrMplsLspPathProperties_Object = MibTableColumn
vRtrMplsLspPathProperties = _VRtrMplsLspPathProperties_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 5),
    _VRtrMplsLspPathProperties_Type()
)
vRtrMplsLspPathProperties.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathProperties.setStatus("current")


class _VRtrMplsLspPathBandwidth_Type(Integer32):
    """Custom type vRtrMplsLspPathBandwidth based on Integer32"""
    defaultValue = 0


_VRtrMplsLspPathBandwidth_Type.__name__ = "Integer32"
_VRtrMplsLspPathBandwidth_Object = MibTableColumn
vRtrMplsLspPathBandwidth = _VRtrMplsLspPathBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 6),
    _VRtrMplsLspPathBandwidth_Type()
)
vRtrMplsLspPathBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspPathBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspPathBandwidth.setUnits("mega-bits per second")


class _VRtrMplsLspPathBwProtect_Type(TruthValue):
    """Custom type vRtrMplsLspPathBwProtect based on TruthValue"""
    defaultValue = 2


_VRtrMplsLspPathBwProtect_Type.__name__ = "TruthValue"
_VRtrMplsLspPathBwProtect_Object = MibTableColumn
vRtrMplsLspPathBwProtect = _VRtrMplsLspPathBwProtect_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 7),
    _VRtrMplsLspPathBwProtect_Type()
)
vRtrMplsLspPathBwProtect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspPathBwProtect.setStatus("obsolete")


class _VRtrMplsLspPathState_Type(Integer32):
    """Custom type vRtrMplsLspPathState based on Integer32"""
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
        *(("unknown", 1),
          ("active", 2),
          ("inactive", 3))
    )


_VRtrMplsLspPathState_Type.__name__ = "Integer32"
_VRtrMplsLspPathState_Object = MibTableColumn
vRtrMplsLspPathState = _VRtrMplsLspPathState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 8),
    _VRtrMplsLspPathState_Type()
)
vRtrMplsLspPathState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathState.setStatus("current")


class _VRtrMplsLspPathPreference_Type(Integer32):
    """Custom type vRtrMplsLspPathPreference based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VRtrMplsLspPathPreference_Type.__name__ = "Integer32"
_VRtrMplsLspPathPreference_Object = MibTableColumn
vRtrMplsLspPathPreference = _VRtrMplsLspPathPreference_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 9),
    _VRtrMplsLspPathPreference_Type()
)
vRtrMplsLspPathPreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspPathPreference.setStatus("current")


class _VRtrMplsLspPathCosSource_Type(TruthValue):
    """Custom type vRtrMplsLspPathCosSource based on TruthValue"""
    defaultValue = 2


_VRtrMplsLspPathCosSource_Type.__name__ = "TruthValue"
_VRtrMplsLspPathCosSource_Object = MibTableColumn
vRtrMplsLspPathCosSource = _VRtrMplsLspPathCosSource_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 10),
    _VRtrMplsLspPathCosSource_Type()
)
vRtrMplsLspPathCosSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspPathCosSource.setStatus("obsolete")


class _VRtrMplsLspPathClassOfService_Type(TNamedItemOrEmpty):
    """Custom type vRtrMplsLspPathClassOfService based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_VRtrMplsLspPathClassOfService_Type.__name__ = "TNamedItemOrEmpty"
_VRtrMplsLspPathClassOfService_Object = MibTableColumn
vRtrMplsLspPathClassOfService = _VRtrMplsLspPathClassOfService_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 11),
    _VRtrMplsLspPathClassOfService_Type()
)
vRtrMplsLspPathClassOfService.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspPathClassOfService.setStatus("obsolete")


class _VRtrMplsLspPathSetupPriority_Type(Unsigned32):
    """Custom type vRtrMplsLspPathSetupPriority based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_VRtrMplsLspPathSetupPriority_Type.__name__ = "Unsigned32"
_VRtrMplsLspPathSetupPriority_Object = MibTableColumn
vRtrMplsLspPathSetupPriority = _VRtrMplsLspPathSetupPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 12),
    _VRtrMplsLspPathSetupPriority_Type()
)
vRtrMplsLspPathSetupPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspPathSetupPriority.setStatus("current")


class _VRtrMplsLspPathHoldPriority_Type(Unsigned32):
    """Custom type vRtrMplsLspPathHoldPriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_VRtrMplsLspPathHoldPriority_Type.__name__ = "Unsigned32"
_VRtrMplsLspPathHoldPriority_Object = MibTableColumn
vRtrMplsLspPathHoldPriority = _VRtrMplsLspPathHoldPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 13),
    _VRtrMplsLspPathHoldPriority_Type()
)
vRtrMplsLspPathHoldPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspPathHoldPriority.setStatus("current")


class _VRtrMplsLspPathRecord_Type(Integer32):
    """Custom type vRtrMplsLspPathRecord based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("record", 1),
          ("noRecord", 2))
    )


_VRtrMplsLspPathRecord_Type.__name__ = "Integer32"
_VRtrMplsLspPathRecord_Object = MibTableColumn
vRtrMplsLspPathRecord = _VRtrMplsLspPathRecord_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 14),
    _VRtrMplsLspPathRecord_Type()
)
vRtrMplsLspPathRecord.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspPathRecord.setStatus("current")


class _VRtrMplsLspPathHopLimit_Type(Unsigned32):
    """Custom type vRtrMplsLspPathHopLimit based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 255),
    )


_VRtrMplsLspPathHopLimit_Type.__name__ = "Unsigned32"
_VRtrMplsLspPathHopLimit_Object = MibTableColumn
vRtrMplsLspPathHopLimit = _VRtrMplsLspPathHopLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 15),
    _VRtrMplsLspPathHopLimit_Type()
)
vRtrMplsLspPathHopLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspPathHopLimit.setStatus("current")


class _VRtrMplsLspPathSharing_Type(TruthValue):
    """Custom type vRtrMplsLspPathSharing based on TruthValue"""
    defaultValue = 2


_VRtrMplsLspPathSharing_Type.__name__ = "TruthValue"
_VRtrMplsLspPathSharing_Object = MibTableColumn
vRtrMplsLspPathSharing = _VRtrMplsLspPathSharing_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 16),
    _VRtrMplsLspPathSharing_Type()
)
vRtrMplsLspPathSharing.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspPathSharing.setStatus("obsolete")


class _VRtrMplsLspPathAdminState_Type(TmnxAdminState):
    """Custom type vRtrMplsLspPathAdminState based on TmnxAdminState"""
    defaultValue = 2


_VRtrMplsLspPathAdminState_Type.__name__ = "TmnxAdminState"
_VRtrMplsLspPathAdminState_Object = MibTableColumn
vRtrMplsLspPathAdminState = _VRtrMplsLspPathAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 17),
    _VRtrMplsLspPathAdminState_Type()
)
vRtrMplsLspPathAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspPathAdminState.setStatus("current")
_VRtrMplsLspPathOperState_Type = TmnxOperState
_VRtrMplsLspPathOperState_Object = MibTableColumn
vRtrMplsLspPathOperState = _VRtrMplsLspPathOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 18),
    _VRtrMplsLspPathOperState_Type()
)
vRtrMplsLspPathOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathOperState.setStatus("current")


class _VRtrMplsLspPathInheritance_Type(Unsigned32):
    """Custom type vRtrMplsLspPathInheritance based on Unsigned32"""
    defaultValue = 0


_VRtrMplsLspPathInheritance_Type.__name__ = "Unsigned32"
_VRtrMplsLspPathInheritance_Object = MibTableColumn
vRtrMplsLspPathInheritance = _VRtrMplsLspPathInheritance_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 19),
    _VRtrMplsLspPathInheritance_Type()
)
vRtrMplsLspPathInheritance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspPathInheritance.setStatus("current")
_VRtrMplsLspPathLspId_Type = MplsLSPID
_VRtrMplsLspPathLspId_Object = MibTableColumn
vRtrMplsLspPathLspId = _VRtrMplsLspPathLspId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 20),
    _VRtrMplsLspPathLspId_Type()
)
vRtrMplsLspPathLspId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathLspId.setStatus("current")
_VRtrMplsLspPathRetryTimeRemaining_Type = Unsigned32
_VRtrMplsLspPathRetryTimeRemaining_Object = MibTableColumn
vRtrMplsLspPathRetryTimeRemaining = _VRtrMplsLspPathRetryTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 21),
    _VRtrMplsLspPathRetryTimeRemaining_Type()
)
vRtrMplsLspPathRetryTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathRetryTimeRemaining.setStatus("current")


class _VRtrMplsLspPathTunnelARHopListIndex_Type(Integer32):
    """Custom type vRtrMplsLspPathTunnelARHopListIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 2147483647),
    )


_VRtrMplsLspPathTunnelARHopListIndex_Type.__name__ = "Integer32"
_VRtrMplsLspPathTunnelARHopListIndex_Object = MibTableColumn
vRtrMplsLspPathTunnelARHopListIndex = _VRtrMplsLspPathTunnelARHopListIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 22),
    _VRtrMplsLspPathTunnelARHopListIndex_Type()
)
vRtrMplsLspPathTunnelARHopListIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathTunnelARHopListIndex.setStatus("current")


class _VRtrMplsLspPathNegotiatedMTU_Type(Unsigned32):
    """Custom type vRtrMplsLspPathNegotiatedMTU based on Unsigned32"""
    defaultValue = 0


_VRtrMplsLspPathNegotiatedMTU_Type.__name__ = "Unsigned32"
_VRtrMplsLspPathNegotiatedMTU_Object = MibTableColumn
vRtrMplsLspPathNegotiatedMTU = _VRtrMplsLspPathNegotiatedMTU_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 23),
    _VRtrMplsLspPathNegotiatedMTU_Type()
)
vRtrMplsLspPathNegotiatedMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathNegotiatedMTU.setStatus("current")
_VRtrMplsLspPathFailCode_Type = TmnxMplsLspFailCode
_VRtrMplsLspPathFailCode_Object = MibTableColumn
vRtrMplsLspPathFailCode = _VRtrMplsLspPathFailCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 24),
    _VRtrMplsLspPathFailCode_Type()
)
vRtrMplsLspPathFailCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathFailCode.setStatus("current")
_VRtrMplsLspPathFailNodeAddr_Type = IpAddress
_VRtrMplsLspPathFailNodeAddr_Object = MibTableColumn
vRtrMplsLspPathFailNodeAddr = _VRtrMplsLspPathFailNodeAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 25),
    _VRtrMplsLspPathFailNodeAddr_Type()
)
vRtrMplsLspPathFailNodeAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathFailNodeAddr.setStatus("current")


class _VRtrMplsLspPathAdminGroupInclude_Type(Unsigned32):
    """Custom type vRtrMplsLspPathAdminGroupInclude based on Unsigned32"""
    defaultValue = 0


_VRtrMplsLspPathAdminGroupInclude_Type.__name__ = "Unsigned32"
_VRtrMplsLspPathAdminGroupInclude_Object = MibTableColumn
vRtrMplsLspPathAdminGroupInclude = _VRtrMplsLspPathAdminGroupInclude_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 26),
    _VRtrMplsLspPathAdminGroupInclude_Type()
)
vRtrMplsLspPathAdminGroupInclude.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspPathAdminGroupInclude.setStatus("current")


class _VRtrMplsLspPathAdminGroupExclude_Type(Unsigned32):
    """Custom type vRtrMplsLspPathAdminGroupExclude based on Unsigned32"""
    defaultValue = 0


_VRtrMplsLspPathAdminGroupExclude_Type.__name__ = "Unsigned32"
_VRtrMplsLspPathAdminGroupExclude_Object = MibTableColumn
vRtrMplsLspPathAdminGroupExclude = _VRtrMplsLspPathAdminGroupExclude_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 27),
    _VRtrMplsLspPathAdminGroupExclude_Type()
)
vRtrMplsLspPathAdminGroupExclude.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspPathAdminGroupExclude.setStatus("current")


class _VRtrMplsLspPathAdaptive_Type(TruthValue):
    """Custom type vRtrMplsLspPathAdaptive based on TruthValue"""
    defaultValue = 1


_VRtrMplsLspPathAdaptive_Type.__name__ = "TruthValue"
_VRtrMplsLspPathAdaptive_Object = MibTableColumn
vRtrMplsLspPathAdaptive = _VRtrMplsLspPathAdaptive_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 28),
    _VRtrMplsLspPathAdaptive_Type()
)
vRtrMplsLspPathAdaptive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspPathAdaptive.setStatus("current")


class _VRtrMplsLspPathOptimizeTimer_Type(Unsigned32):
    """Custom type vRtrMplsLspPathOptimizeTimer based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VRtrMplsLspPathOptimizeTimer_Type.__name__ = "Unsigned32"
_VRtrMplsLspPathOptimizeTimer_Object = MibTableColumn
vRtrMplsLspPathOptimizeTimer = _VRtrMplsLspPathOptimizeTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 29),
    _VRtrMplsLspPathOptimizeTimer_Type()
)
vRtrMplsLspPathOptimizeTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspPathOptimizeTimer.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspPathOptimizeTimer.setUnits("seconds")


class _VRtrMplsLspPathNextOptimize_Type(Unsigned32):
    """Custom type vRtrMplsLspPathNextOptimize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VRtrMplsLspPathNextOptimize_Type.__name__ = "Unsigned32"
_VRtrMplsLspPathNextOptimize_Object = MibTableColumn
vRtrMplsLspPathNextOptimize = _VRtrMplsLspPathNextOptimize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 30),
    _VRtrMplsLspPathNextOptimize_Type()
)
vRtrMplsLspPathNextOptimize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathNextOptimize.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspPathNextOptimize.setUnits("seconds")
_VRtrMplsLspPathOperBandwidth_Type = Integer32
_VRtrMplsLspPathOperBandwidth_Object = MibTableColumn
vRtrMplsLspPathOperBandwidth = _VRtrMplsLspPathOperBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 31),
    _VRtrMplsLspPathOperBandwidth_Type()
)
vRtrMplsLspPathOperBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathOperBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspPathOperBandwidth.setUnits("mega-bits per second")


class _VRtrMplsLspPathMBBState_Type(Integer32):
    """Custom type vRtrMplsLspPathMBBState based on Integer32"""
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
        *(("none", 1),
          ("success", 2),
          ("inProgress", 3),
          ("fail", 4))
    )


_VRtrMplsLspPathMBBState_Type.__name__ = "Integer32"
_VRtrMplsLspPathMBBState_Object = MibTableColumn
vRtrMplsLspPathMBBState = _VRtrMplsLspPathMBBState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 32),
    _VRtrMplsLspPathMBBState_Type()
)
vRtrMplsLspPathMBBState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathMBBState.setStatus("obsolete")
_VRtrMplsLspPathResignal_Type = TmnxActionType
_VRtrMplsLspPathResignal_Object = MibTableColumn
vRtrMplsLspPathResignal = _VRtrMplsLspPathResignal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 33),
    _VRtrMplsLspPathResignal_Type()
)
vRtrMplsLspPathResignal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspPathResignal.setStatus("current")


class _VRtrMplsLspPathTunnelCRHopListIndex_Type(Integer32):
    """Custom type vRtrMplsLspPathTunnelCRHopListIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 2147483647),
    )


_VRtrMplsLspPathTunnelCRHopListIndex_Type.__name__ = "Integer32"
_VRtrMplsLspPathTunnelCRHopListIndex_Object = MibTableColumn
vRtrMplsLspPathTunnelCRHopListIndex = _VRtrMplsLspPathTunnelCRHopListIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 34),
    _VRtrMplsLspPathTunnelCRHopListIndex_Type()
)
vRtrMplsLspPathTunnelCRHopListIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathTunnelCRHopListIndex.setStatus("current")
_VRtrMplsLspPathOperMTU_Type = Unsigned32
_VRtrMplsLspPathOperMTU_Object = MibTableColumn
vRtrMplsLspPathOperMTU = _VRtrMplsLspPathOperMTU_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 35),
    _VRtrMplsLspPathOperMTU_Type()
)
vRtrMplsLspPathOperMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathOperMTU.setStatus("current")


class _VRtrMplsLspPathRecordLabel_Type(Integer32):
    """Custom type vRtrMplsLspPathRecordLabel based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("record", 1),
          ("noRecord", 2))
    )


_VRtrMplsLspPathRecordLabel_Type.__name__ = "Integer32"
_VRtrMplsLspPathRecordLabel_Object = MibTableColumn
vRtrMplsLspPathRecordLabel = _VRtrMplsLspPathRecordLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 36),
    _VRtrMplsLspPathRecordLabel_Type()
)
vRtrMplsLspPathRecordLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspPathRecordLabel.setStatus("current")


class _VRtrMplsLspPathSrlg_Type(TruthValue):
    """Custom type vRtrMplsLspPathSrlg based on TruthValue"""
    defaultValue = 2


_VRtrMplsLspPathSrlg_Type.__name__ = "TruthValue"
_VRtrMplsLspPathSrlg_Object = MibTableColumn
vRtrMplsLspPathSrlg = _VRtrMplsLspPathSrlg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 37),
    _VRtrMplsLspPathSrlg_Type()
)
vRtrMplsLspPathSrlg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspPathSrlg.setStatus("current")
_VRtrMplsLspPathSrlgDisjoint_Type = TruthValue
_VRtrMplsLspPathSrlgDisjoint_Object = MibTableColumn
vRtrMplsLspPathSrlgDisjoint = _VRtrMplsLspPathSrlgDisjoint_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 38),
    _VRtrMplsLspPathSrlgDisjoint_Type()
)
vRtrMplsLspPathSrlgDisjoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathSrlgDisjoint.setStatus("current")
_VRtrMplsLspPathLastResigAttempt_Type = TimeStamp
_VRtrMplsLspPathLastResigAttempt_Object = MibTableColumn
vRtrMplsLspPathLastResigAttempt = _VRtrMplsLspPathLastResigAttempt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 39),
    _VRtrMplsLspPathLastResigAttempt_Type()
)
vRtrMplsLspPathLastResigAttempt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathLastResigAttempt.setStatus("current")
_VRtrMplsLspPathMetric_Type = Unsigned32
_VRtrMplsLspPathMetric_Object = MibTableColumn
vRtrMplsLspPathMetric = _VRtrMplsLspPathMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 40),
    _VRtrMplsLspPathMetric_Type()
)
vRtrMplsLspPathMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathMetric.setStatus("current")
_VRtrMplsLspPathLastMBBType_Type = TmnxMplsMBBType
_VRtrMplsLspPathLastMBBType_Object = MibTableColumn
vRtrMplsLspPathLastMBBType = _VRtrMplsLspPathLastMBBType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 41),
    _VRtrMplsLspPathLastMBBType_Type()
)
vRtrMplsLspPathLastMBBType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathLastMBBType.setStatus("current")
_VRtrMplsLspPathLastMBBEnd_Type = TimeStamp
_VRtrMplsLspPathLastMBBEnd_Object = MibTableColumn
vRtrMplsLspPathLastMBBEnd = _VRtrMplsLspPathLastMBBEnd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 42),
    _VRtrMplsLspPathLastMBBEnd_Type()
)
vRtrMplsLspPathLastMBBEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathLastMBBEnd.setStatus("current")
_VRtrMplsLspPathLastMBBMetric_Type = Unsigned32
_VRtrMplsLspPathLastMBBMetric_Object = MibTableColumn
vRtrMplsLspPathLastMBBMetric = _VRtrMplsLspPathLastMBBMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 43),
    _VRtrMplsLspPathLastMBBMetric_Type()
)
vRtrMplsLspPathLastMBBMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathLastMBBMetric.setStatus("current")


class _VRtrMplsLspPathLastMBBState_Type(Integer32):
    """Custom type vRtrMplsLspPathLastMBBState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("success", 2),
          ("fail", 3))
    )


_VRtrMplsLspPathLastMBBState_Type.__name__ = "Integer32"
_VRtrMplsLspPathLastMBBState_Object = MibTableColumn
vRtrMplsLspPathLastMBBState = _VRtrMplsLspPathLastMBBState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 44),
    _VRtrMplsLspPathLastMBBState_Type()
)
vRtrMplsLspPathLastMBBState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathLastMBBState.setStatus("current")
_VRtrMplsLspPathMBBTypeInProg_Type = TmnxMplsMBBType
_VRtrMplsLspPathMBBTypeInProg_Object = MibTableColumn
vRtrMplsLspPathMBBTypeInProg = _VRtrMplsLspPathMBBTypeInProg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 45),
    _VRtrMplsLspPathMBBTypeInProg_Type()
)
vRtrMplsLspPathMBBTypeInProg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathMBBTypeInProg.setStatus("current")
_VRtrMplsLspPathMBBStarted_Type = TimeStamp
_VRtrMplsLspPathMBBStarted_Object = MibTableColumn
vRtrMplsLspPathMBBStarted = _VRtrMplsLspPathMBBStarted_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 46),
    _VRtrMplsLspPathMBBStarted_Type()
)
vRtrMplsLspPathMBBStarted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathMBBStarted.setStatus("current")
_VRtrMplsLspPathMBBNextRetry_Type = Unsigned32
_VRtrMplsLspPathMBBNextRetry_Object = MibTableColumn
vRtrMplsLspPathMBBNextRetry = _VRtrMplsLspPathMBBNextRetry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 47),
    _VRtrMplsLspPathMBBNextRetry_Type()
)
vRtrMplsLspPathMBBNextRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathMBBNextRetry.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspPathMBBNextRetry.setUnits("seconds")
_VRtrMplsLspPathMBBRetryAttempts_Type = Unsigned32
_VRtrMplsLspPathMBBRetryAttempts_Object = MibTableColumn
vRtrMplsLspPathMBBRetryAttempts = _VRtrMplsLspPathMBBRetryAttempts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 48),
    _VRtrMplsLspPathMBBRetryAttempts_Type()
)
vRtrMplsLspPathMBBRetryAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathMBBRetryAttempts.setStatus("current")
_VRtrMplsLspPathMBBFailCode_Type = TmnxMplsLspFailCode
_VRtrMplsLspPathMBBFailCode_Object = MibTableColumn
vRtrMplsLspPathMBBFailCode = _VRtrMplsLspPathMBBFailCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 49),
    _VRtrMplsLspPathMBBFailCode_Type()
)
vRtrMplsLspPathMBBFailCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathMBBFailCode.setStatus("current")
_VRtrMplsLspPathMBBFailNodeArType_Type = InetAddressType
_VRtrMplsLspPathMBBFailNodeArType_Object = MibTableColumn
vRtrMplsLspPathMBBFailNodeArType = _VRtrMplsLspPathMBBFailNodeArType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 50),
    _VRtrMplsLspPathMBBFailNodeArType_Type()
)
vRtrMplsLspPathMBBFailNodeArType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathMBBFailNodeArType.setStatus("current")


class _VRtrMplsLspPathMBBFailNodeAddr_Type(InetAddress):
    """Custom type vRtrMplsLspPathMBBFailNodeAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_VRtrMplsLspPathMBBFailNodeAddr_Type.__name__ = "InetAddress"
_VRtrMplsLspPathMBBFailNodeAddr_Object = MibTableColumn
vRtrMplsLspPathMBBFailNodeAddr = _VRtrMplsLspPathMBBFailNodeAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 51),
    _VRtrMplsLspPathMBBFailNodeAddr_Type()
)
vRtrMplsLspPathMBBFailNodeAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathMBBFailNodeAddr.setStatus("current")


class _VRtrMplsLspPathClassType_Type(TmnxRsvpDSTEClassType):
    """Custom type vRtrMplsLspPathClassType based on TmnxRsvpDSTEClassType"""
    defaultValue = 0


_VRtrMplsLspPathClassType_Type.__name__ = "TmnxRsvpDSTEClassType"
_VRtrMplsLspPathClassType_Object = MibTableColumn
vRtrMplsLspPathClassType = _VRtrMplsLspPathClassType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 52),
    _VRtrMplsLspPathClassType_Type()
)
vRtrMplsLspPathClassType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspPathClassType.setStatus("current")
_VRtrMplsLspPathOperMetric_Type = Unsigned32
_VRtrMplsLspPathOperMetric_Object = MibTableColumn
vRtrMplsLspPathOperMetric = _VRtrMplsLspPathOperMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 53),
    _VRtrMplsLspPathOperMetric_Type()
)
vRtrMplsLspPathOperMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathOperMetric.setStatus("current")
_VRtrMplsLspPathResignalEligible_Type = TruthValue
_VRtrMplsLspPathResignalEligible_Object = MibTableColumn
vRtrMplsLspPathResignalEligible = _VRtrMplsLspPathResignalEligible_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 54),
    _VRtrMplsLspPathResignalEligible_Type()
)
vRtrMplsLspPathResignalEligible.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathResignalEligible.setStatus("current")
_VRtrMplsLspPathIsFastRetry_Type = TruthValue
_VRtrMplsLspPathIsFastRetry_Object = MibTableColumn
vRtrMplsLspPathIsFastRetry = _VRtrMplsLspPathIsFastRetry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 55),
    _VRtrMplsLspPathIsFastRetry_Type()
)
vRtrMplsLspPathIsFastRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathIsFastRetry.setStatus("current")


class _VRtrMplsLspPathBackupCT_Type(Integer32):
    """Custom type vRtrMplsLspPathBackupCT based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 7),
    )


_VRtrMplsLspPathBackupCT_Type.__name__ = "Integer32"
_VRtrMplsLspPathBackupCT_Object = MibTableColumn
vRtrMplsLspPathBackupCT = _VRtrMplsLspPathBackupCT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 56),
    _VRtrMplsLspPathBackupCT_Type()
)
vRtrMplsLspPathBackupCT.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspPathBackupCT.setStatus("current")
_VRtrMplsLspPathMainCTRetryRem_Type = Unsigned32
_VRtrMplsLspPathMainCTRetryRem_Object = MibTableColumn
vRtrMplsLspPathMainCTRetryRem = _VRtrMplsLspPathMainCTRetryRem_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 57),
    _VRtrMplsLspPathMainCTRetryRem_Type()
)
vRtrMplsLspPathMainCTRetryRem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathMainCTRetryRem.setStatus("current")


class _VRtrMplsLspPathOperCT_Type(Integer32):
    """Custom type vRtrMplsLspPathOperCT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 7),
    )


_VRtrMplsLspPathOperCT_Type.__name__ = "Integer32"
_VRtrMplsLspPathOperCT_Object = MibTableColumn
vRtrMplsLspPathOperCT = _VRtrMplsLspPathOperCT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 58),
    _VRtrMplsLspPathOperCT_Type()
)
vRtrMplsLspPathOperCT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathOperCT.setStatus("current")
_VRtrMplsLspPathNewPathIndex_Type = MplsTunnelIndex
_VRtrMplsLspPathNewPathIndex_Object = MibTableColumn
vRtrMplsLspPathNewPathIndex = _VRtrMplsLspPathNewPathIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 59),
    _VRtrMplsLspPathNewPathIndex_Type()
)
vRtrMplsLspPathNewPathIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspPathNewPathIndex.setStatus("current")
_VRtrMplsLspPathMBBMainCTRetryRem_Type = Unsigned32
_VRtrMplsLspPathMBBMainCTRetryRem_Object = MibTableColumn
vRtrMplsLspPathMBBMainCTRetryRem = _VRtrMplsLspPathMBBMainCTRetryRem_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 60),
    _VRtrMplsLspPathMBBMainCTRetryRem_Type()
)
vRtrMplsLspPathMBBMainCTRetryRem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathMBBMainCTRetryRem.setStatus("current")
_VRtrMplsLspPathSigBWMBBInProg_Type = Unsigned32
_VRtrMplsLspPathSigBWMBBInProg_Object = MibTableColumn
vRtrMplsLspPathSigBWMBBInProg = _VRtrMplsLspPathSigBWMBBInProg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 61),
    _VRtrMplsLspPathSigBWMBBInProg_Type()
)
vRtrMplsLspPathSigBWMBBInProg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathSigBWMBBInProg.setStatus("current")
_VRtrMplsLspPathSigBWLastMBB_Type = Unsigned32
_VRtrMplsLspPathSigBWLastMBB_Object = MibTableColumn
vRtrMplsLspPathSigBWLastMBB = _VRtrMplsLspPathSigBWLastMBB_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 62),
    _VRtrMplsLspPathSigBWLastMBB_Type()
)
vRtrMplsLspPathSigBWLastMBB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathSigBWLastMBB.setStatus("current")


class _VRtrMplsLspPathActiveByManual_Type(Integer32):
    """Custom type vRtrMplsLspPathActiveByManual based on Integer32"""
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
          ("noForce", 1),
          ("force", 2))
    )


_VRtrMplsLspPathActiveByManual_Type.__name__ = "Integer32"
_VRtrMplsLspPathActiveByManual_Object = MibTableColumn
vRtrMplsLspPathActiveByManual = _VRtrMplsLspPathActiveByManual_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 63),
    _VRtrMplsLspPathActiveByManual_Type()
)
vRtrMplsLspPathActiveByManual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathActiveByManual.setStatus("current")
_VRtrMplsLspPathTimeoutIn_Type = Unsigned32
_VRtrMplsLspPathTimeoutIn_Object = MibTableColumn
vRtrMplsLspPathTimeoutIn = _VRtrMplsLspPathTimeoutIn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 64),
    _VRtrMplsLspPathTimeoutIn_Type()
)
vRtrMplsLspPathTimeoutIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathTimeoutIn.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspPathTimeoutIn.setUnits("seconds")
_VRtrMplsLspPathMBBTimeoutIn_Type = Unsigned32
_VRtrMplsLspPathMBBTimeoutIn_Object = MibTableColumn
vRtrMplsLspPathMBBTimeoutIn = _VRtrMplsLspPathMBBTimeoutIn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 65),
    _VRtrMplsLspPathMBBTimeoutIn_Type()
)
vRtrMplsLspPathMBBTimeoutIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathMBBTimeoutIn.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspPathMBBTimeoutIn.setUnits("seconds")
_VRtrMplsLspPathBfdTemplateName_Type = TNamedItemOrEmpty
_VRtrMplsLspPathBfdTemplateName_Object = MibTableColumn
vRtrMplsLspPathBfdTemplateName = _VRtrMplsLspPathBfdTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 66),
    _VRtrMplsLspPathBfdTemplateName_Type()
)
vRtrMplsLspPathBfdTemplateName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspPathBfdTemplateName.setStatus("current")


class _VRtrMplsLspPathBfdEnable_Type(TruthValue):
    """Custom type vRtrMplsLspPathBfdEnable based on TruthValue"""
    defaultValue = 2


_VRtrMplsLspPathBfdEnable_Type.__name__ = "TruthValue"
_VRtrMplsLspPathBfdEnable_Object = MibTableColumn
vRtrMplsLspPathBfdEnable = _VRtrMplsLspPathBfdEnable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 67),
    _VRtrMplsLspPathBfdEnable_Type()
)
vRtrMplsLspPathBfdEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspPathBfdEnable.setStatus("current")


class _VRtrMplsLspPathBfdPingIntvl_Type(Unsigned32):
    """Custom type vRtrMplsLspPathBfdPingIntvl based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(60, 300),
    )


_VRtrMplsLspPathBfdPingIntvl_Type.__name__ = "Unsigned32"
_VRtrMplsLspPathBfdPingIntvl_Object = MibTableColumn
vRtrMplsLspPathBfdPingIntvl = _VRtrMplsLspPathBfdPingIntvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 68),
    _VRtrMplsLspPathBfdPingIntvl_Type()
)
vRtrMplsLspPathBfdPingIntvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspPathBfdPingIntvl.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspPathBfdPingIntvl.setUnits("seconds")
_VRtrMplsLspPathLastUpdateTime_Type = TimeStamp
_VRtrMplsLspPathLastUpdateTime_Object = MibTableColumn
vRtrMplsLspPathLastUpdateTime = _VRtrMplsLspPathLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 69),
    _VRtrMplsLspPathLastUpdateTime_Type()
)
vRtrMplsLspPathLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathLastUpdateTime.setStatus("current")
_VRtrMplsLspPathLastUpdateId_Type = Unsigned32
_VRtrMplsLspPathLastUpdateId_Object = MibTableColumn
vRtrMplsLspPathLastUpdateId = _VRtrMplsLspPathLastUpdateId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 70),
    _VRtrMplsLspPathLastUpdateId_Type()
)
vRtrMplsLspPathLastUpdateId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathLastUpdateId.setStatus("current")


class _VRtrMplsLspPathLastUpdateState_Type(Integer32):
    """Custom type vRtrMplsLspPathLastUpdateState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("success", 2),
          ("fail", 3))
    )


_VRtrMplsLspPathLastUpdateState_Type.__name__ = "Integer32"
_VRtrMplsLspPathLastUpdateState_Object = MibTableColumn
vRtrMplsLspPathLastUpdateState = _VRtrMplsLspPathLastUpdateState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 71),
    _VRtrMplsLspPathLastUpdateState_Type()
)
vRtrMplsLspPathLastUpdateState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathLastUpdateState.setStatus("current")
_VRtrMplsLspPathLastUpdFailCode_Type = TmnxMplsLspFailCode
_VRtrMplsLspPathLastUpdFailCode_Object = MibTableColumn
vRtrMplsLspPathLastUpdFailCode = _VRtrMplsLspPathLastUpdFailCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 72),
    _VRtrMplsLspPathLastUpdFailCode_Type()
)
vRtrMplsLspPathLastUpdFailCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathLastUpdFailCode.setStatus("current")
_VRtrMplsLspPathStatTable_Object = MibTable
vRtrMplsLspPathStatTable = _VRtrMplsLspPathStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 5)
)
if mibBuilder.loadTexts:
    vRtrMplsLspPathStatTable.setStatus("current")
_VRtrMplsLspPathStatEntry_Object = MibTableRow
vRtrMplsLspPathStatEntry = _VRtrMplsLspPathStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 5, 1)
)
if mibBuilder.loadTexts:
    vRtrMplsLspPathStatEntry.setStatus("current")
_VRtrMplsLspPathTimeUp_Type = TimeInterval
_VRtrMplsLspPathTimeUp_Object = MibTableColumn
vRtrMplsLspPathTimeUp = _VRtrMplsLspPathTimeUp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 5, 1, 1),
    _VRtrMplsLspPathTimeUp_Type()
)
vRtrMplsLspPathTimeUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathTimeUp.setStatus("current")
_VRtrMplsLspPathTimeDown_Type = TimeInterval
_VRtrMplsLspPathTimeDown_Object = MibTableColumn
vRtrMplsLspPathTimeDown = _VRtrMplsLspPathTimeDown_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 5, 1, 2),
    _VRtrMplsLspPathTimeDown_Type()
)
vRtrMplsLspPathTimeDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathTimeDown.setStatus("current")
_VRtrMplsLspPathRetryAttempts_Type = Unsigned32
_VRtrMplsLspPathRetryAttempts_Object = MibTableColumn
vRtrMplsLspPathRetryAttempts = _VRtrMplsLspPathRetryAttempts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 5, 1, 3),
    _VRtrMplsLspPathRetryAttempts_Type()
)
vRtrMplsLspPathRetryAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathRetryAttempts.setStatus("current")
_VRtrMplsLspPathTransitionCount_Type = Counter32
_VRtrMplsLspPathTransitionCount_Object = MibTableColumn
vRtrMplsLspPathTransitionCount = _VRtrMplsLspPathTransitionCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 5, 1, 4),
    _VRtrMplsLspPathTransitionCount_Type()
)
vRtrMplsLspPathTransitionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathTransitionCount.setStatus("current")
_VRtrMplsLspPathCspfQueries_Type = Counter32
_VRtrMplsLspPathCspfQueries_Object = MibTableColumn
vRtrMplsLspPathCspfQueries = _VRtrMplsLspPathCspfQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 5, 1, 5),
    _VRtrMplsLspPathCspfQueries_Type()
)
vRtrMplsLspPathCspfQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathCspfQueries.setStatus("current")
_VRtrMplsXCTable_Object = MibTable
vRtrMplsXCTable = _VRtrMplsXCTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 6)
)
if mibBuilder.loadTexts:
    vRtrMplsXCTable.setStatus("current")
_VRtrMplsXCEntry_Object = MibTableRow
vRtrMplsXCEntry = _VRtrMplsXCEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 6, 1)
)
vRtrMplsXCEntry.setIndexNames(
    (0, "MPLS-LSR-MIB", "mplsXCLspId"),
)
if mibBuilder.loadTexts:
    vRtrMplsXCEntry.setStatus("current")


class _VRtrMplsXCIndex_Type(Integer32):
    """Custom type vRtrMplsXCIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VRtrMplsXCIndex_Type.__name__ = "Integer32"
_VRtrMplsXCIndex_Object = MibTableColumn
vRtrMplsXCIndex = _VRtrMplsXCIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 6, 1, 1),
    _VRtrMplsXCIndex_Type()
)
vRtrMplsXCIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsXCIndex.setStatus("current")
_VRtrMplsInSegmentIfIndex_Type = InterfaceIndexOrZero
_VRtrMplsInSegmentIfIndex_Object = MibTableColumn
vRtrMplsInSegmentIfIndex = _VRtrMplsInSegmentIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 6, 1, 2),
    _VRtrMplsInSegmentIfIndex_Type()
)
vRtrMplsInSegmentIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInSegmentIfIndex.setStatus("current")
_VRtrMplsInSegmentLabel_Type = MplsLabel
_VRtrMplsInSegmentLabel_Object = MibTableColumn
vRtrMplsInSegmentLabel = _VRtrMplsInSegmentLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 6, 1, 3),
    _VRtrMplsInSegmentLabel_Type()
)
vRtrMplsInSegmentLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInSegmentLabel.setStatus("current")


class _VRtrMplsOutSegmentIndex_Type(Integer32):
    """Custom type vRtrMplsOutSegmentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_VRtrMplsOutSegmentIndex_Type.__name__ = "Integer32"
_VRtrMplsOutSegmentIndex_Object = MibTableColumn
vRtrMplsOutSegmentIndex = _VRtrMplsOutSegmentIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 6, 1, 4),
    _VRtrMplsOutSegmentIndex_Type()
)
vRtrMplsOutSegmentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsOutSegmentIndex.setStatus("current")
_VRtrMplsERHopTunnelIndex_Type = Integer32
_VRtrMplsERHopTunnelIndex_Object = MibTableColumn
vRtrMplsERHopTunnelIndex = _VRtrMplsERHopTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 6, 1, 5),
    _VRtrMplsERHopTunnelIndex_Type()
)
vRtrMplsERHopTunnelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsERHopTunnelIndex.setStatus("current")
_VRtrMplsARHopTunnelIndex_Type = Integer32
_VRtrMplsARHopTunnelIndex_Object = MibTableColumn
vRtrMplsARHopTunnelIndex = _VRtrMplsARHopTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 6, 1, 6),
    _VRtrMplsARHopTunnelIndex_Type()
)
vRtrMplsARHopTunnelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsARHopTunnelIndex.setStatus("current")
_VRtrMplsRsvpSessionIndex_Type = Unsigned32
_VRtrMplsRsvpSessionIndex_Object = MibTableColumn
vRtrMplsRsvpSessionIndex = _VRtrMplsRsvpSessionIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 6, 1, 7),
    _VRtrMplsRsvpSessionIndex_Type()
)
vRtrMplsRsvpSessionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsRsvpSessionIndex.setStatus("current")
_VRtrMplsXCFailCode_Type = TmnxMplsLspFailCode
_VRtrMplsXCFailCode_Object = MibTableColumn
vRtrMplsXCFailCode = _VRtrMplsXCFailCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 6, 1, 8),
    _VRtrMplsXCFailCode_Type()
)
vRtrMplsXCFailCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsXCFailCode.setStatus("current")
_VRtrMplsXCCHopTableIndex_Type = Integer32
_VRtrMplsXCCHopTableIndex_Object = MibTableColumn
vRtrMplsXCCHopTableIndex = _VRtrMplsXCCHopTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 6, 1, 9),
    _VRtrMplsXCCHopTableIndex_Type()
)
vRtrMplsXCCHopTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsXCCHopTableIndex.setStatus("current")
_VRtrMplsGeneralTable_Object = MibTable
vRtrMplsGeneralTable = _VRtrMplsGeneralTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7)
)
if mibBuilder.loadTexts:
    vRtrMplsGeneralTable.setStatus("current")
_VRtrMplsGeneralEntry_Object = MibTableRow
vRtrMplsGeneralEntry = _VRtrMplsGeneralEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1)
)
vRtrMplsGeneralEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
)
if mibBuilder.loadTexts:
    vRtrMplsGeneralEntry.setStatus("current")
_VRtrMplsGeneralLastChange_Type = TimeStamp
_VRtrMplsGeneralLastChange_Object = MibTableColumn
vRtrMplsGeneralLastChange = _VRtrMplsGeneralLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 1),
    _VRtrMplsGeneralLastChange_Type()
)
vRtrMplsGeneralLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGeneralLastChange.setStatus("current")


class _VRtrMplsGeneralAdminState_Type(TmnxAdminState):
    """Custom type vRtrMplsGeneralAdminState based on TmnxAdminState"""
    defaultValue = 3


_VRtrMplsGeneralAdminState_Type.__name__ = "TmnxAdminState"
_VRtrMplsGeneralAdminState_Object = MibTableColumn
vRtrMplsGeneralAdminState = _VRtrMplsGeneralAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 2),
    _VRtrMplsGeneralAdminState_Type()
)
vRtrMplsGeneralAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGeneralAdminState.setStatus("current")
_VRtrMplsGeneralOperState_Type = TmnxOperState
_VRtrMplsGeneralOperState_Object = MibTableColumn
vRtrMplsGeneralOperState = _VRtrMplsGeneralOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 3),
    _VRtrMplsGeneralOperState_Type()
)
vRtrMplsGeneralOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGeneralOperState.setStatus("current")


class _VRtrMplsGeneralPropagateTtl_Type(TruthValue):
    """Custom type vRtrMplsGeneralPropagateTtl based on TruthValue"""
    defaultValue = 1


_VRtrMplsGeneralPropagateTtl_Type.__name__ = "TruthValue"
_VRtrMplsGeneralPropagateTtl_Object = MibTableColumn
vRtrMplsGeneralPropagateTtl = _VRtrMplsGeneralPropagateTtl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 4),
    _VRtrMplsGeneralPropagateTtl_Type()
)
vRtrMplsGeneralPropagateTtl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGeneralPropagateTtl.setStatus("obsolete")


class _VRtrMplsGeneralTE_Type(Integer32):
    """Custom type vRtrMplsGeneralTE based on Integer32"""
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
        *(("none", 1),
          ("bgp", 2),
          ("bgpigp", 3))
    )


_VRtrMplsGeneralTE_Type.__name__ = "Integer32"
_VRtrMplsGeneralTE_Object = MibTableColumn
vRtrMplsGeneralTE = _VRtrMplsGeneralTE_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 5),
    _VRtrMplsGeneralTE_Type()
)
vRtrMplsGeneralTE.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGeneralTE.setStatus("obsolete")
_VRtrMplsGeneralNewLspIndex_Type = TestAndIncr
_VRtrMplsGeneralNewLspIndex_Object = MibTableColumn
vRtrMplsGeneralNewLspIndex = _VRtrMplsGeneralNewLspIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 6),
    _VRtrMplsGeneralNewLspIndex_Type()
)
vRtrMplsGeneralNewLspIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGeneralNewLspIndex.setStatus("current")


class _VRtrMplsGeneralOptimizeTimer_Type(Unsigned32):
    """Custom type vRtrMplsGeneralOptimizeTimer based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VRtrMplsGeneralOptimizeTimer_Type.__name__ = "Unsigned32"
_VRtrMplsGeneralOptimizeTimer_Object = MibTableColumn
vRtrMplsGeneralOptimizeTimer = _VRtrMplsGeneralOptimizeTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 7),
    _VRtrMplsGeneralOptimizeTimer_Type()
)
vRtrMplsGeneralOptimizeTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGeneralOptimizeTimer.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsGeneralOptimizeTimer.setUnits("seconds")


class _VRtrMplsGeneralFRObject_Type(TruthValue):
    """Custom type vRtrMplsGeneralFRObject based on TruthValue"""
    defaultValue = 1


_VRtrMplsGeneralFRObject_Type.__name__ = "TruthValue"
_VRtrMplsGeneralFRObject_Object = MibTableColumn
vRtrMplsGeneralFRObject = _VRtrMplsGeneralFRObject_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 8),
    _VRtrMplsGeneralFRObject_Type()
)
vRtrMplsGeneralFRObject.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGeneralFRObject.setStatus("current")


class _VRtrMplsGeneralResignalTimer_Type(Unsigned32):
    """Custom type vRtrMplsGeneralResignalTimer based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(30, 10080),
    )


_VRtrMplsGeneralResignalTimer_Type.__name__ = "Unsigned32"
_VRtrMplsGeneralResignalTimer_Object = MibTableColumn
vRtrMplsGeneralResignalTimer = _VRtrMplsGeneralResignalTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 9),
    _VRtrMplsGeneralResignalTimer_Type()
)
vRtrMplsGeneralResignalTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGeneralResignalTimer.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsGeneralResignalTimer.setUnits("minutes")


class _VRtrMplsGeneralHoldTimer_Type(Unsigned32):
    """Custom type vRtrMplsGeneralHoldTimer based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_VRtrMplsGeneralHoldTimer_Type.__name__ = "Unsigned32"
_VRtrMplsGeneralHoldTimer_Object = MibTableColumn
vRtrMplsGeneralHoldTimer = _VRtrMplsGeneralHoldTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 10),
    _VRtrMplsGeneralHoldTimer_Type()
)
vRtrMplsGeneralHoldTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGeneralHoldTimer.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsGeneralHoldTimer.setUnits("seconds")


class _VRtrMplsGeneralDynamicBypass_Type(TruthValue):
    """Custom type vRtrMplsGeneralDynamicBypass based on TruthValue"""
    defaultValue = 1


_VRtrMplsGeneralDynamicBypass_Type.__name__ = "TruthValue"
_VRtrMplsGeneralDynamicBypass_Object = MibTableColumn
vRtrMplsGeneralDynamicBypass = _VRtrMplsGeneralDynamicBypass_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 11),
    _VRtrMplsGeneralDynamicBypass_Type()
)
vRtrMplsGeneralDynamicBypass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGeneralDynamicBypass.setStatus("current")
_VRtrMplsGeneralNextResignal_Type = Unsigned32
_VRtrMplsGeneralNextResignal_Object = MibTableColumn
vRtrMplsGeneralNextResignal = _VRtrMplsGeneralNextResignal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 12),
    _VRtrMplsGeneralNextResignal_Type()
)
vRtrMplsGeneralNextResignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGeneralNextResignal.setStatus("current")
_VRtrMplsGeneralOperDownReason_Type = TmnxMplsOperDownReasonCode
_VRtrMplsGeneralOperDownReason_Object = MibTableColumn
vRtrMplsGeneralOperDownReason = _VRtrMplsGeneralOperDownReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 13),
    _VRtrMplsGeneralOperDownReason_Type()
)
vRtrMplsGeneralOperDownReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGeneralOperDownReason.setStatus("current")


class _VRtrMplsGeneralSrlgFrr_Type(TruthValue):
    """Custom type vRtrMplsGeneralSrlgFrr based on TruthValue"""
    defaultValue = 2


_VRtrMplsGeneralSrlgFrr_Type.__name__ = "TruthValue"
_VRtrMplsGeneralSrlgFrr_Object = MibTableColumn
vRtrMplsGeneralSrlgFrr = _VRtrMplsGeneralSrlgFrr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 14),
    _VRtrMplsGeneralSrlgFrr_Type()
)
vRtrMplsGeneralSrlgFrr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGeneralSrlgFrr.setStatus("current")


class _VRtrMplsGeneralSrlgFrrStrict_Type(TruthValue):
    """Custom type vRtrMplsGeneralSrlgFrrStrict based on TruthValue"""
    defaultValue = 2


_VRtrMplsGeneralSrlgFrrStrict_Type.__name__ = "TruthValue"
_VRtrMplsGeneralSrlgFrrStrict_Object = MibTableColumn
vRtrMplsGeneralSrlgFrrStrict = _VRtrMplsGeneralSrlgFrrStrict_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 15),
    _VRtrMplsGeneralSrlgFrrStrict_Type()
)
vRtrMplsGeneralSrlgFrrStrict.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGeneralSrlgFrrStrict.setStatus("current")
_VRtrMplsGeneralNewP2mpInstIndex_Type = TestAndIncr
_VRtrMplsGeneralNewP2mpInstIndex_Object = MibTableColumn
vRtrMplsGeneralNewP2mpInstIndex = _VRtrMplsGeneralNewP2mpInstIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 16),
    _VRtrMplsGeneralNewP2mpInstIndex_Type()
)
vRtrMplsGeneralNewP2mpInstIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGeneralNewP2mpInstIndex.setStatus("current")


class _VRtrMplsGeneralLeastFillMinThd_Type(Unsigned32):
    """Custom type vRtrMplsGeneralLeastFillMinThd based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_VRtrMplsGeneralLeastFillMinThd_Type.__name__ = "Unsigned32"
_VRtrMplsGeneralLeastFillMinThd_Object = MibTableColumn
vRtrMplsGeneralLeastFillMinThd = _VRtrMplsGeneralLeastFillMinThd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 17),
    _VRtrMplsGeneralLeastFillMinThd_Type()
)
vRtrMplsGeneralLeastFillMinThd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGeneralLeastFillMinThd.setStatus("current")


class _VRtrMplsGenLeastFillReoptiThd_Type(Unsigned32):
    """Custom type vRtrMplsGenLeastFillReoptiThd based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_VRtrMplsGenLeastFillReoptiThd_Type.__name__ = "Unsigned32"
_VRtrMplsGenLeastFillReoptiThd_Object = MibTableColumn
vRtrMplsGenLeastFillReoptiThd = _VRtrMplsGenLeastFillReoptiThd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 18),
    _VRtrMplsGenLeastFillReoptiThd_Type()
)
vRtrMplsGenLeastFillReoptiThd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGenLeastFillReoptiThd.setStatus("current")


class _VRtrMplsGeneralUseSrlgDB_Type(TruthValue):
    """Custom type vRtrMplsGeneralUseSrlgDB based on TruthValue"""
    defaultValue = 2


_VRtrMplsGeneralUseSrlgDB_Type.__name__ = "TruthValue"
_VRtrMplsGeneralUseSrlgDB_Object = MibTableColumn
vRtrMplsGeneralUseSrlgDB = _VRtrMplsGeneralUseSrlgDB_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 19),
    _VRtrMplsGeneralUseSrlgDB_Type()
)
vRtrMplsGeneralUseSrlgDB.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGeneralUseSrlgDB.setStatus("current")


class _VRtrMplsGeneralP2mpResigTimer_Type(Unsigned32):
    """Custom type vRtrMplsGeneralP2mpResigTimer based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(60, 10080),
    )


_VRtrMplsGeneralP2mpResigTimer_Type.__name__ = "Unsigned32"
_VRtrMplsGeneralP2mpResigTimer_Object = MibTableColumn
vRtrMplsGeneralP2mpResigTimer = _VRtrMplsGeneralP2mpResigTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 20),
    _VRtrMplsGeneralP2mpResigTimer_Type()
)
vRtrMplsGeneralP2mpResigTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGeneralP2mpResigTimer.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsGeneralP2mpResigTimer.setUnits("minutes")
_VRtrMplsGeneralP2mpNextResignal_Type = Unsigned32
_VRtrMplsGeneralP2mpNextResignal_Object = MibTableColumn
vRtrMplsGeneralP2mpNextResignal = _VRtrMplsGeneralP2mpNextResignal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 21),
    _VRtrMplsGeneralP2mpNextResignal_Type()
)
vRtrMplsGeneralP2mpNextResignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGeneralP2mpNextResignal.setStatus("current")


class _VRtrMplsGeneralSecFastRetryTimer_Type(Unsigned32):
    """Custom type vRtrMplsGeneralSecFastRetryTimer based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_VRtrMplsGeneralSecFastRetryTimer_Type.__name__ = "Unsigned32"
_VRtrMplsGeneralSecFastRetryTimer_Object = MibTableColumn
vRtrMplsGeneralSecFastRetryTimer = _VRtrMplsGeneralSecFastRetryTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 22),
    _VRtrMplsGeneralSecFastRetryTimer_Type()
)
vRtrMplsGeneralSecFastRetryTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGeneralSecFastRetryTimer.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsGeneralSecFastRetryTimer.setUnits("seconds")


class _VRtrMplsGeneralShortTTLPropLocal_Type(TruthValue):
    """Custom type vRtrMplsGeneralShortTTLPropLocal based on TruthValue"""
    defaultValue = 1


_VRtrMplsGeneralShortTTLPropLocal_Type.__name__ = "TruthValue"
_VRtrMplsGeneralShortTTLPropLocal_Object = MibTableColumn
vRtrMplsGeneralShortTTLPropLocal = _VRtrMplsGeneralShortTTLPropLocal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 23),
    _VRtrMplsGeneralShortTTLPropLocal_Type()
)
vRtrMplsGeneralShortTTLPropLocal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGeneralShortTTLPropLocal.setStatus("current")


class _VRtrMplsGeneralShortTTLPropTrans_Type(TruthValue):
    """Custom type vRtrMplsGeneralShortTTLPropTrans based on TruthValue"""
    defaultValue = 1


_VRtrMplsGeneralShortTTLPropTrans_Type.__name__ = "TruthValue"
_VRtrMplsGeneralShortTTLPropTrans_Object = MibTableColumn
vRtrMplsGeneralShortTTLPropTrans = _VRtrMplsGeneralShortTTLPropTrans_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 24),
    _VRtrMplsGeneralShortTTLPropTrans_Type()
)
vRtrMplsGeneralShortTTLPropTrans.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGeneralShortTTLPropTrans.setStatus("current")


class _VRtrMplsGeneralStaticLspFRTimer_Type(Unsigned32):
    """Custom type vRtrMplsGeneralStaticLspFRTimer based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_VRtrMplsGeneralStaticLspFRTimer_Type.__name__ = "Unsigned32"
_VRtrMplsGeneralStaticLspFRTimer_Object = MibTableColumn
vRtrMplsGeneralStaticLspFRTimer = _VRtrMplsGeneralStaticLspFRTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 25),
    _VRtrMplsGeneralStaticLspFRTimer_Type()
)
vRtrMplsGeneralStaticLspFRTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGeneralStaticLspFRTimer.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsGeneralStaticLspFRTimer.setUnits("seconds")


class _VRtrMplsGeneralAutoBWDefSampMul_Type(Unsigned32):
    """Custom type vRtrMplsGeneralAutoBWDefSampMul based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 511),
    )


_VRtrMplsGeneralAutoBWDefSampMul_Type.__name__ = "Unsigned32"
_VRtrMplsGeneralAutoBWDefSampMul_Object = MibTableColumn
vRtrMplsGeneralAutoBWDefSampMul = _VRtrMplsGeneralAutoBWDefSampMul_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 26),
    _VRtrMplsGeneralAutoBWDefSampMul_Type()
)
vRtrMplsGeneralAutoBWDefSampMul.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGeneralAutoBWDefSampMul.setStatus("current")


class _VRtrMplsGeneralAutoBWDefAdjMul_Type(Unsigned32):
    """Custom type vRtrMplsGeneralAutoBWDefAdjMul based on Unsigned32"""
    defaultValue = 288

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16383),
    )


_VRtrMplsGeneralAutoBWDefAdjMul_Type.__name__ = "Unsigned32"
_VRtrMplsGeneralAutoBWDefAdjMul_Object = MibTableColumn
vRtrMplsGeneralAutoBWDefAdjMul = _VRtrMplsGeneralAutoBWDefAdjMul_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 27),
    _VRtrMplsGeneralAutoBWDefAdjMul_Type()
)
vRtrMplsGeneralAutoBWDefAdjMul.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGeneralAutoBWDefAdjMul.setStatus("current")


class _VRtrMplsGeneralExpBackoffRetry_Type(TruthValue):
    """Custom type vRtrMplsGeneralExpBackoffRetry based on TruthValue"""
    defaultValue = 2


_VRtrMplsGeneralExpBackoffRetry_Type.__name__ = "TruthValue"
_VRtrMplsGeneralExpBackoffRetry_Object = MibTableColumn
vRtrMplsGeneralExpBackoffRetry = _VRtrMplsGeneralExpBackoffRetry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 28),
    _VRtrMplsGeneralExpBackoffRetry_Type()
)
vRtrMplsGeneralExpBackoffRetry.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGeneralExpBackoffRetry.setStatus("current")


class _VRtrMplsGeneralCspfOnLooseHop_Type(TruthValue):
    """Custom type vRtrMplsGeneralCspfOnLooseHop based on TruthValue"""
    defaultValue = 2


_VRtrMplsGeneralCspfOnLooseHop_Type.__name__ = "TruthValue"
_VRtrMplsGeneralCspfOnLooseHop_Object = MibTableColumn
vRtrMplsGeneralCspfOnLooseHop = _VRtrMplsGeneralCspfOnLooseHop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 29),
    _VRtrMplsGeneralCspfOnLooseHop_Type()
)
vRtrMplsGeneralCspfOnLooseHop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGeneralCspfOnLooseHop.setStatus("current")


class _VRtrMplsGeneralP2PMaxByPassAssoc_Type(Unsigned32):
    """Custom type vRtrMplsGeneralP2PMaxByPassAssoc based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 131072),
    )


_VRtrMplsGeneralP2PMaxByPassAssoc_Type.__name__ = "Unsigned32"
_VRtrMplsGeneralP2PMaxByPassAssoc_Object = MibTableColumn
vRtrMplsGeneralP2PMaxByPassAssoc = _VRtrMplsGeneralP2PMaxByPassAssoc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 30),
    _VRtrMplsGeneralP2PMaxByPassAssoc_Type()
)
vRtrMplsGeneralP2PMaxByPassAssoc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGeneralP2PMaxByPassAssoc.setStatus("current")


class _VRtrMplsGenP2pActPathFastRetry_Type(Unsigned32):
    """Custom type vRtrMplsGenP2pActPathFastRetry based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_VRtrMplsGenP2pActPathFastRetry_Type.__name__ = "Unsigned32"
_VRtrMplsGenP2pActPathFastRetry_Object = MibTableColumn
vRtrMplsGenP2pActPathFastRetry = _VRtrMplsGenP2pActPathFastRetry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 31),
    _VRtrMplsGenP2pActPathFastRetry_Type()
)
vRtrMplsGenP2pActPathFastRetry.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGenP2pActPathFastRetry.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsGenP2pActPathFastRetry.setUnits("seconds")


class _VRtrMplsGenP2mpS2lFastRetry_Type(Unsigned32):
    """Custom type vRtrMplsGenP2mpS2lFastRetry based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_VRtrMplsGenP2mpS2lFastRetry_Type.__name__ = "Unsigned32"
_VRtrMplsGenP2mpS2lFastRetry_Object = MibTableColumn
vRtrMplsGenP2mpS2lFastRetry = _VRtrMplsGenP2mpS2lFastRetry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 32),
    _VRtrMplsGenP2mpS2lFastRetry_Type()
)
vRtrMplsGenP2mpS2lFastRetry.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGenP2mpS2lFastRetry.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsGenP2mpS2lFastRetry.setUnits("seconds")


class _VRtrMplsGenLspInitRetryTimeout_Type(Unsigned32):
    """Custom type vRtrMplsGenLspInitRetryTimeout based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 600),
    )


_VRtrMplsGenLspInitRetryTimeout_Type.__name__ = "Unsigned32"
_VRtrMplsGenLspInitRetryTimeout_Object = MibTableColumn
vRtrMplsGenLspInitRetryTimeout = _VRtrMplsGenLspInitRetryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 33),
    _VRtrMplsGenLspInitRetryTimeout_Type()
)
vRtrMplsGenLspInitRetryTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGenLspInitRetryTimeout.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsGenLspInitRetryTimeout.setUnits("seconds")


class _VRtrMplsLoggerEventBundling_Type(TruthValue):
    """Custom type vRtrMplsLoggerEventBundling based on TruthValue"""
    defaultValue = 2


_VRtrMplsLoggerEventBundling_Type.__name__ = "TruthValue"
_VRtrMplsLoggerEventBundling_Object = MibTableColumn
vRtrMplsLoggerEventBundling = _VRtrMplsLoggerEventBundling_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 34),
    _VRtrMplsLoggerEventBundling_Type()
)
vRtrMplsLoggerEventBundling.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLoggerEventBundling.setStatus("current")
_VRtrMplsGenIssuMplsLockdown_Type = TruthValue
_VRtrMplsGenIssuMplsLockdown_Object = MibTableColumn
vRtrMplsGenIssuMplsLockdown = _VRtrMplsGenIssuMplsLockdown_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 39),
    _VRtrMplsGenIssuMplsLockdown_Type()
)
vRtrMplsGenIssuMplsLockdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGenIssuMplsLockdown.setStatus("current")


class _VRtrMplsGenFRAdminGroup_Type(TruthValue):
    """Custom type vRtrMplsGenFRAdminGroup based on TruthValue"""
    defaultValue = 2


_VRtrMplsGenFRAdminGroup_Type.__name__ = "TruthValue"
_VRtrMplsGenFRAdminGroup_Object = MibTableColumn
vRtrMplsGenFRAdminGroup = _VRtrMplsGenFRAdminGroup_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 40),
    _VRtrMplsGenFRAdminGroup_Type()
)
vRtrMplsGenFRAdminGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGenFRAdminGroup.setStatus("current")


class _VRtrMplsGenRetryOnIgpOverload_Type(TruthValue):
    """Custom type vRtrMplsGenRetryOnIgpOverload based on TruthValue"""
    defaultValue = 2


_VRtrMplsGenRetryOnIgpOverload_Type.__name__ = "TruthValue"
_VRtrMplsGenRetryOnIgpOverload_Object = MibTableColumn
vRtrMplsGenRetryOnIgpOverload = _VRtrMplsGenRetryOnIgpOverload_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 41),
    _VRtrMplsGenRetryOnIgpOverload_Type()
)
vRtrMplsGenRetryOnIgpOverload.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGenRetryOnIgpOverload.setStatus("current")


class _VRtrMplsGenMbbPrefCurrentHops_Type(TruthValue):
    """Custom type vRtrMplsGenMbbPrefCurrentHops based on TruthValue"""
    defaultValue = 2


_VRtrMplsGenMbbPrefCurrentHops_Type.__name__ = "TruthValue"
_VRtrMplsGenMbbPrefCurrentHops_Object = MibTableColumn
vRtrMplsGenMbbPrefCurrentHops = _VRtrMplsGenMbbPrefCurrentHops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 42),
    _VRtrMplsGenMbbPrefCurrentHops_Type()
)
vRtrMplsGenMbbPrefCurrentHops.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGenMbbPrefCurrentHops.setStatus("current")


class _VRtrMplsGeneralBypassResigTimer_Type(Unsigned32):
    """Custom type vRtrMplsGeneralBypassResigTimer based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(30, 10080),
    )


_VRtrMplsGeneralBypassResigTimer_Type.__name__ = "Unsigned32"
_VRtrMplsGeneralBypassResigTimer_Object = MibTableColumn
vRtrMplsGeneralBypassResigTimer = _VRtrMplsGeneralBypassResigTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 43),
    _VRtrMplsGeneralBypassResigTimer_Type()
)
vRtrMplsGeneralBypassResigTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGeneralBypassResigTimer.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsGeneralBypassResigTimer.setUnits("minutes")
_VRtrMplsGenBypassNextResignal_Type = Unsigned32
_VRtrMplsGenBypassNextResignal_Object = MibTableColumn
vRtrMplsGenBypassNextResignal = _VRtrMplsGenBypassNextResignal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 44),
    _VRtrMplsGenBypassNextResignal_Type()
)
vRtrMplsGenBypassNextResignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGenBypassNextResignal.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsGenBypassNextResignal.setUnits("minutes")
_VRtrMplsGeneralNewLspSRIndex_Type = TestAndIncr
_VRtrMplsGeneralNewLspSRIndex_Object = MibTableColumn
vRtrMplsGeneralNewLspSRIndex = _VRtrMplsGeneralNewLspSRIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 45),
    _VRtrMplsGeneralNewLspSRIndex_Type()
)
vRtrMplsGeneralNewLspSRIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGeneralNewLspSRIndex.setStatus("current")


class _VRtrMplsGeneralPceReport_Type(Bits):
    """Custom type vRtrMplsGeneralPceReport based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("srTe", 0),
          ("rsvpTe", 1))
    )

_VRtrMplsGeneralPceReport_Type.__name__ = "Bits"
_VRtrMplsGeneralPceReport_Object = MibTableColumn
vRtrMplsGeneralPceReport = _VRtrMplsGeneralPceReport_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 46),
    _VRtrMplsGeneralPceReport_Type()
)
vRtrMplsGeneralPceReport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGeneralPceReport.setStatus("current")


class _VRtrMplsGeneralEntropyLblRsvpTe_Type(Integer32):
    """Custom type vRtrMplsGeneralEntropyLblRsvpTe based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forceDisable", 1),
          ("enable", 2))
    )


_VRtrMplsGeneralEntropyLblRsvpTe_Type.__name__ = "Integer32"
_VRtrMplsGeneralEntropyLblRsvpTe_Object = MibTableColumn
vRtrMplsGeneralEntropyLblRsvpTe = _VRtrMplsGeneralEntropyLblRsvpTe_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 47),
    _VRtrMplsGeneralEntropyLblRsvpTe_Type()
)
vRtrMplsGeneralEntropyLblRsvpTe.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGeneralEntropyLblRsvpTe.setStatus("current")
_VRtrMplsGeneralStatTable_Object = MibTable
vRtrMplsGeneralStatTable = _VRtrMplsGeneralStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 8)
)
if mibBuilder.loadTexts:
    vRtrMplsGeneralStatTable.setStatus("current")
_VRtrMplsGeneralStatEntry_Object = MibTableRow
vRtrMplsGeneralStatEntry = _VRtrMplsGeneralStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 8, 1)
)
if mibBuilder.loadTexts:
    vRtrMplsGeneralStatEntry.setStatus("current")
_VRtrMplsGeneralStaticLspOriginate_Type = Gauge32
_VRtrMplsGeneralStaticLspOriginate_Object = MibTableColumn
vRtrMplsGeneralStaticLspOriginate = _VRtrMplsGeneralStaticLspOriginate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 8, 1, 1),
    _VRtrMplsGeneralStaticLspOriginate_Type()
)
vRtrMplsGeneralStaticLspOriginate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGeneralStaticLspOriginate.setStatus("current")
_VRtrMplsGeneralStaticLspTransit_Type = Gauge32
_VRtrMplsGeneralStaticLspTransit_Object = MibTableColumn
vRtrMplsGeneralStaticLspTransit = _VRtrMplsGeneralStaticLspTransit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 8, 1, 2),
    _VRtrMplsGeneralStaticLspTransit_Type()
)
vRtrMplsGeneralStaticLspTransit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGeneralStaticLspTransit.setStatus("current")
_VRtrMplsGeneralStaticLspTerminate_Type = Gauge32
_VRtrMplsGeneralStaticLspTerminate_Object = MibTableColumn
vRtrMplsGeneralStaticLspTerminate = _VRtrMplsGeneralStaticLspTerminate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 8, 1, 3),
    _VRtrMplsGeneralStaticLspTerminate_Type()
)
vRtrMplsGeneralStaticLspTerminate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGeneralStaticLspTerminate.setStatus("current")
_VRtrMplsGeneralDynamicLspOriginate_Type = Gauge32
_VRtrMplsGeneralDynamicLspOriginate_Object = MibTableColumn
vRtrMplsGeneralDynamicLspOriginate = _VRtrMplsGeneralDynamicLspOriginate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 8, 1, 4),
    _VRtrMplsGeneralDynamicLspOriginate_Type()
)
vRtrMplsGeneralDynamicLspOriginate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGeneralDynamicLspOriginate.setStatus("current")
_VRtrMplsGeneralDynamicLspTransit_Type = Gauge32
_VRtrMplsGeneralDynamicLspTransit_Object = MibTableColumn
vRtrMplsGeneralDynamicLspTransit = _VRtrMplsGeneralDynamicLspTransit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 8, 1, 5),
    _VRtrMplsGeneralDynamicLspTransit_Type()
)
vRtrMplsGeneralDynamicLspTransit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGeneralDynamicLspTransit.setStatus("current")
_VRtrMplsGeneralDynamicLspTerminate_Type = Gauge32
_VRtrMplsGeneralDynamicLspTerminate_Object = MibTableColumn
vRtrMplsGeneralDynamicLspTerminate = _VRtrMplsGeneralDynamicLspTerminate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 8, 1, 6),
    _VRtrMplsGeneralDynamicLspTerminate_Type()
)
vRtrMplsGeneralDynamicLspTerminate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGeneralDynamicLspTerminate.setStatus("current")
_VRtrMplsGeneralDetourLspOriginate_Type = Gauge32
_VRtrMplsGeneralDetourLspOriginate_Object = MibTableColumn
vRtrMplsGeneralDetourLspOriginate = _VRtrMplsGeneralDetourLspOriginate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 8, 1, 7),
    _VRtrMplsGeneralDetourLspOriginate_Type()
)
vRtrMplsGeneralDetourLspOriginate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGeneralDetourLspOriginate.setStatus("current")
_VRtrMplsGeneralDetourLspTransit_Type = Gauge32
_VRtrMplsGeneralDetourLspTransit_Object = MibTableColumn
vRtrMplsGeneralDetourLspTransit = _VRtrMplsGeneralDetourLspTransit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 8, 1, 8),
    _VRtrMplsGeneralDetourLspTransit_Type()
)
vRtrMplsGeneralDetourLspTransit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGeneralDetourLspTransit.setStatus("current")
_VRtrMplsGeneralDetourLspTerminate_Type = Gauge32
_VRtrMplsGeneralDetourLspTerminate_Object = MibTableColumn
vRtrMplsGeneralDetourLspTerminate = _VRtrMplsGeneralDetourLspTerminate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 8, 1, 9),
    _VRtrMplsGeneralDetourLspTerminate_Type()
)
vRtrMplsGeneralDetourLspTerminate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGeneralDetourLspTerminate.setStatus("current")
_VRtrMplsGeneralS2lOriginate_Type = Gauge32
_VRtrMplsGeneralS2lOriginate_Object = MibTableColumn
vRtrMplsGeneralS2lOriginate = _VRtrMplsGeneralS2lOriginate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 8, 1, 10),
    _VRtrMplsGeneralS2lOriginate_Type()
)
vRtrMplsGeneralS2lOriginate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGeneralS2lOriginate.setStatus("current")
_VRtrMplsGeneralS2lTransit_Type = Gauge32
_VRtrMplsGeneralS2lTransit_Object = MibTableColumn
vRtrMplsGeneralS2lTransit = _VRtrMplsGeneralS2lTransit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 8, 1, 11),
    _VRtrMplsGeneralS2lTransit_Type()
)
vRtrMplsGeneralS2lTransit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGeneralS2lTransit.setStatus("current")
_VRtrMplsGeneralS2lTerminate_Type = Gauge32
_VRtrMplsGeneralS2lTerminate_Object = MibTableColumn
vRtrMplsGeneralS2lTerminate = _VRtrMplsGeneralS2lTerminate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 8, 1, 12),
    _VRtrMplsGeneralS2lTerminate_Type()
)
vRtrMplsGeneralS2lTerminate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGeneralS2lTerminate.setStatus("current")
_VRtrMplsGeneralLspEgrStatCount_Type = Counter32
_VRtrMplsGeneralLspEgrStatCount_Object = MibTableColumn
vRtrMplsGeneralLspEgrStatCount = _VRtrMplsGeneralLspEgrStatCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 8, 1, 13),
    _VRtrMplsGeneralLspEgrStatCount_Type()
)
vRtrMplsGeneralLspEgrStatCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGeneralLspEgrStatCount.setStatus("current")
_VRtrMplsGeneralLspIgrStatCount_Type = Counter32
_VRtrMplsGeneralLspIgrStatCount_Object = MibTableColumn
vRtrMplsGeneralLspIgrStatCount = _VRtrMplsGeneralLspIgrStatCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 8, 1, 14),
    _VRtrMplsGeneralLspIgrStatCount_Type()
)
vRtrMplsGeneralLspIgrStatCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGeneralLspIgrStatCount.setStatus("current")
_VRtrMplsGenMplsTpLspOriginate_Type = Gauge32
_VRtrMplsGenMplsTpLspOriginate_Object = MibTableColumn
vRtrMplsGenMplsTpLspOriginate = _VRtrMplsGenMplsTpLspOriginate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 8, 1, 15),
    _VRtrMplsGenMplsTpLspOriginate_Type()
)
vRtrMplsGenMplsTpLspOriginate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGenMplsTpLspOriginate.setStatus("current")
_VRtrMplsGenMplsTpLspTransit_Type = Gauge32
_VRtrMplsGenMplsTpLspTransit_Object = MibTableColumn
vRtrMplsGenMplsTpLspTransit = _VRtrMplsGenMplsTpLspTransit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 8, 1, 16),
    _VRtrMplsGenMplsTpLspTransit_Type()
)
vRtrMplsGenMplsTpLspTransit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGenMplsTpLspTransit.setStatus("current")
_VRtrMplsGenMplsTpLspTerminate_Type = Gauge32
_VRtrMplsGenMplsTpLspTerminate_Object = MibTableColumn
vRtrMplsGenMplsTpLspTerminate = _VRtrMplsGenMplsTpLspTerminate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 8, 1, 17),
    _VRtrMplsGenMplsTpLspTerminate_Type()
)
vRtrMplsGenMplsTpLspTerminate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGenMplsTpLspTerminate.setStatus("current")
_VRtrMplsGenMplsTpOrigPathInst_Type = Gauge32
_VRtrMplsGenMplsTpOrigPathInst_Object = MibTableColumn
vRtrMplsGenMplsTpOrigPathInst = _VRtrMplsGenMplsTpOrigPathInst_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 8, 1, 18),
    _VRtrMplsGenMplsTpOrigPathInst_Type()
)
vRtrMplsGenMplsTpOrigPathInst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGenMplsTpOrigPathInst.setStatus("current")
_VRtrMplsGenMplsTpTranPathInst_Type = Gauge32
_VRtrMplsGenMplsTpTranPathInst_Object = MibTableColumn
vRtrMplsGenMplsTpTranPathInst = _VRtrMplsGenMplsTpTranPathInst_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 8, 1, 19),
    _VRtrMplsGenMplsTpTranPathInst_Type()
)
vRtrMplsGenMplsTpTranPathInst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGenMplsTpTranPathInst.setStatus("current")
_VRtrMplsGenMplsTpTermPathInst_Type = Gauge32
_VRtrMplsGenMplsTpTermPathInst_Object = MibTableColumn
vRtrMplsGenMplsTpTermPathInst = _VRtrMplsGenMplsTpTermPathInst_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 8, 1, 20),
    _VRtrMplsGenMplsTpTermPathInst_Type()
)
vRtrMplsGenMplsTpTermPathInst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGenMplsTpTermPathInst.setStatus("current")
_VRtrMplsGeneralMeshP2pOriginate_Type = Gauge32
_VRtrMplsGeneralMeshP2pOriginate_Object = MibTableColumn
vRtrMplsGeneralMeshP2pOriginate = _VRtrMplsGeneralMeshP2pOriginate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 8, 1, 21),
    _VRtrMplsGeneralMeshP2pOriginate_Type()
)
vRtrMplsGeneralMeshP2pOriginate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGeneralMeshP2pOriginate.setStatus("current")
_VRtrMplsGeneralOneHopP2pOrigin_Type = Gauge32
_VRtrMplsGeneralOneHopP2pOrigin_Object = MibTableColumn
vRtrMplsGeneralOneHopP2pOrigin = _VRtrMplsGeneralOneHopP2pOrigin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 8, 1, 22),
    _VRtrMplsGeneralOneHopP2pOrigin_Type()
)
vRtrMplsGeneralOneHopP2pOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGeneralOneHopP2pOrigin.setStatus("current")
_VRtrMplsGeneralSrTeLspOriginate_Type = Gauge32
_VRtrMplsGeneralSrTeLspOriginate_Object = MibTableColumn
vRtrMplsGeneralSrTeLspOriginate = _VRtrMplsGeneralSrTeLspOriginate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 8, 1, 23),
    _VRtrMplsGeneralSrTeLspOriginate_Type()
)
vRtrMplsGeneralSrTeLspOriginate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGeneralSrTeLspOriginate.setStatus("current")
_VRtrMplsIfTable_Object = MibTable
vRtrMplsIfTable = _VRtrMplsIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 9)
)
if mibBuilder.loadTexts:
    vRtrMplsIfTable.setStatus("current")
_VRtrMplsIfEntry_Object = MibTableRow
vRtrMplsIfEntry = _VRtrMplsIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 9, 1)
)
vRtrMplsIfEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-VRTR-MIB", "vRtrIfIndex"),
)
if mibBuilder.loadTexts:
    vRtrMplsIfEntry.setStatus("current")


class _VRtrMplsIfAdminState_Type(TmnxAdminState):
    """Custom type vRtrMplsIfAdminState based on TmnxAdminState"""
    defaultValue = 3


_VRtrMplsIfAdminState_Type.__name__ = "TmnxAdminState"
_VRtrMplsIfAdminState_Object = MibTableColumn
vRtrMplsIfAdminState = _VRtrMplsIfAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 9, 1, 1),
    _VRtrMplsIfAdminState_Type()
)
vRtrMplsIfAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsIfAdminState.setStatus("current")
_VRtrMplsIfOperState_Type = TmnxOperState
_VRtrMplsIfOperState_Object = MibTableColumn
vRtrMplsIfOperState = _VRtrMplsIfOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 9, 1, 2),
    _VRtrMplsIfOperState_Type()
)
vRtrMplsIfOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsIfOperState.setStatus("current")


class _VRtrMplsIfAdminGroup_Type(Unsigned32):
    """Custom type vRtrMplsIfAdminGroup based on Unsigned32"""
    defaultValue = 0


_VRtrMplsIfAdminGroup_Type.__name__ = "Unsigned32"
_VRtrMplsIfAdminGroup_Object = MibTableColumn
vRtrMplsIfAdminGroup = _VRtrMplsIfAdminGroup_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 9, 1, 3),
    _VRtrMplsIfAdminGroup_Type()
)
vRtrMplsIfAdminGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsIfAdminGroup.setStatus("current")


class _VRtrMplsIfTeMetric_Type(Unsigned32):
    """Custom type vRtrMplsIfTeMetric based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 16777215),
    )


_VRtrMplsIfTeMetric_Type.__name__ = "Unsigned32"
_VRtrMplsIfTeMetric_Object = MibTableColumn
vRtrMplsIfTeMetric = _VRtrMplsIfTeMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 9, 1, 4),
    _VRtrMplsIfTeMetric_Type()
)
vRtrMplsIfTeMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsIfTeMetric.setStatus("current")
_VRtrMplsIfStatTable_Object = MibTable
vRtrMplsIfStatTable = _VRtrMplsIfStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 10)
)
if mibBuilder.loadTexts:
    vRtrMplsIfStatTable.setStatus("current")
_VRtrMplsIfStatEntry_Object = MibTableRow
vRtrMplsIfStatEntry = _VRtrMplsIfStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 10, 1)
)
if mibBuilder.loadTexts:
    vRtrMplsIfStatEntry.setStatus("current")
_VRtrMplsIfTxPktCount_Type = Counter64
_VRtrMplsIfTxPktCount_Object = MibTableColumn
vRtrMplsIfTxPktCount = _VRtrMplsIfTxPktCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 10, 1, 1),
    _VRtrMplsIfTxPktCount_Type()
)
vRtrMplsIfTxPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsIfTxPktCount.setStatus("current")
_VRtrMplsIfRxPktCount_Type = Counter64
_VRtrMplsIfRxPktCount_Object = MibTableColumn
vRtrMplsIfRxPktCount = _VRtrMplsIfRxPktCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 10, 1, 2),
    _VRtrMplsIfRxPktCount_Type()
)
vRtrMplsIfRxPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsIfRxPktCount.setStatus("current")
_VRtrMplsIfTxOctetCount_Type = Counter64
_VRtrMplsIfTxOctetCount_Object = MibTableColumn
vRtrMplsIfTxOctetCount = _VRtrMplsIfTxOctetCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 10, 1, 3),
    _VRtrMplsIfTxOctetCount_Type()
)
vRtrMplsIfTxOctetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsIfTxOctetCount.setStatus("current")
_VRtrMplsIfRxOctetCount_Type = Counter64
_VRtrMplsIfRxOctetCount_Object = MibTableColumn
vRtrMplsIfRxOctetCount = _VRtrMplsIfRxOctetCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 10, 1, 4),
    _VRtrMplsIfRxOctetCount_Type()
)
vRtrMplsIfRxOctetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsIfRxOctetCount.setStatus("current")
_VRtrMplsTunnelARHopTable_Object = MibTable
vRtrMplsTunnelARHopTable = _VRtrMplsTunnelARHopTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 11)
)
if mibBuilder.loadTexts:
    vRtrMplsTunnelARHopTable.setStatus("current")
_VRtrMplsTunnelARHopEntry_Object = MibTableRow
vRtrMplsTunnelARHopEntry = _VRtrMplsTunnelARHopEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 11, 1)
)
if mibBuilder.loadTexts:
    vRtrMplsTunnelARHopEntry.setStatus("current")


class _VRtrMplsTunnelARHopProtection_Type(Bits):
    """Custom type vRtrMplsTunnelARHopProtection based on Bits"""
    namedValues = NamedValues(
        *(("localAvailable", 0),
          ("localInUse", 1),
          ("bandwidthProtected", 2),
          ("nodeProtected", 3),
          ("preemptionPending", 4),
          ("nodeId", 5))
    )

_VRtrMplsTunnelARHopProtection_Type.__name__ = "Bits"
_VRtrMplsTunnelARHopProtection_Object = MibTableColumn
vRtrMplsTunnelARHopProtection = _VRtrMplsTunnelARHopProtection_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 11, 1, 1),
    _VRtrMplsTunnelARHopProtection_Type()
)
vRtrMplsTunnelARHopProtection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsTunnelARHopProtection.setStatus("current")
_VRtrMplsTunnelARHopRecordLabel_Type = MplsLabel
_VRtrMplsTunnelARHopRecordLabel_Object = MibTableColumn
vRtrMplsTunnelARHopRecordLabel = _VRtrMplsTunnelARHopRecordLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 11, 1, 2),
    _VRtrMplsTunnelARHopRecordLabel_Type()
)
vRtrMplsTunnelARHopRecordLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsTunnelARHopRecordLabel.setStatus("current")
_VRtrMplsTunnelARHopRouterId_Type = IpAddress
_VRtrMplsTunnelARHopRouterId_Object = MibTableColumn
vRtrMplsTunnelARHopRouterId = _VRtrMplsTunnelARHopRouterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 11, 1, 3),
    _VRtrMplsTunnelARHopRouterId_Type()
)
vRtrMplsTunnelARHopRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsTunnelARHopRouterId.setStatus("current")
_VRtrMplsTunnelARHopUnnumIfID_Type = Unsigned32
_VRtrMplsTunnelARHopUnnumIfID_Object = MibTableColumn
vRtrMplsTunnelARHopUnnumIfID = _VRtrMplsTunnelARHopUnnumIfID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 11, 1, 4),
    _VRtrMplsTunnelARHopUnnumIfID_Type()
)
vRtrMplsTunnelARHopUnnumIfID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsTunnelARHopUnnumIfID.setStatus("current")
_VRtrMplsTunnelCHopTable_Object = MibTable
vRtrMplsTunnelCHopTable = _VRtrMplsTunnelCHopTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 12)
)
if mibBuilder.loadTexts:
    vRtrMplsTunnelCHopTable.setStatus("current")
_VRtrMplsTunnelCHopEntry_Object = MibTableRow
vRtrMplsTunnelCHopEntry = _VRtrMplsTunnelCHopEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 12, 1)
)
vRtrMplsTunnelCHopEntry.setIndexNames(
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsTunnelCHopListIndex"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsTunnelCHopIndex"),
)
if mibBuilder.loadTexts:
    vRtrMplsTunnelCHopEntry.setStatus("current")


class _VRtrMplsTunnelCHopListIndex_Type(Integer32):
    """Custom type vRtrMplsTunnelCHopListIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VRtrMplsTunnelCHopListIndex_Type.__name__ = "Integer32"
_VRtrMplsTunnelCHopListIndex_Object = MibTableColumn
vRtrMplsTunnelCHopListIndex = _VRtrMplsTunnelCHopListIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 12, 1, 1),
    _VRtrMplsTunnelCHopListIndex_Type()
)
vRtrMplsTunnelCHopListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsTunnelCHopListIndex.setStatus("current")


class _VRtrMplsTunnelCHopIndex_Type(Integer32):
    """Custom type vRtrMplsTunnelCHopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VRtrMplsTunnelCHopIndex_Type.__name__ = "Integer32"
_VRtrMplsTunnelCHopIndex_Object = MibTableColumn
vRtrMplsTunnelCHopIndex = _VRtrMplsTunnelCHopIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 12, 1, 2),
    _VRtrMplsTunnelCHopIndex_Type()
)
vRtrMplsTunnelCHopIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsTunnelCHopIndex.setStatus("current")


class _VRtrMplsTunnelCHopAddrType_Type(Integer32):
    """Custom type vRtrMplsTunnelCHopAddrType based on Integer32"""
    defaultValue = 1

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
        *(("ipV4", 1),
          ("ipV6", 2),
          ("asNumber", 3),
          ("lspid", 4),
          ("unnum", 5))
    )


_VRtrMplsTunnelCHopAddrType_Type.__name__ = "Integer32"
_VRtrMplsTunnelCHopAddrType_Object = MibTableColumn
vRtrMplsTunnelCHopAddrType = _VRtrMplsTunnelCHopAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 12, 1, 3),
    _VRtrMplsTunnelCHopAddrType_Type()
)
vRtrMplsTunnelCHopAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsTunnelCHopAddrType.setStatus("current")
_VRtrMplsTunnelCHopIpv4Addr_Type = IpAddress
_VRtrMplsTunnelCHopIpv4Addr_Object = MibTableColumn
vRtrMplsTunnelCHopIpv4Addr = _VRtrMplsTunnelCHopIpv4Addr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 12, 1, 4),
    _VRtrMplsTunnelCHopIpv4Addr_Type()
)
vRtrMplsTunnelCHopIpv4Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsTunnelCHopIpv4Addr.setStatus("current")


class _VRtrMplsTunnelCHopIpv4PrefixLen_Type(Integer32):
    """Custom type vRtrMplsTunnelCHopIpv4PrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_VRtrMplsTunnelCHopIpv4PrefixLen_Type.__name__ = "Integer32"
_VRtrMplsTunnelCHopIpv4PrefixLen_Object = MibTableColumn
vRtrMplsTunnelCHopIpv4PrefixLen = _VRtrMplsTunnelCHopIpv4PrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 12, 1, 5),
    _VRtrMplsTunnelCHopIpv4PrefixLen_Type()
)
vRtrMplsTunnelCHopIpv4PrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsTunnelCHopIpv4PrefixLen.setStatus("current")
_VRtrMplsTunnelCHopIpv6Addr_Type = InetAddressIPv6
_VRtrMplsTunnelCHopIpv6Addr_Object = MibTableColumn
vRtrMplsTunnelCHopIpv6Addr = _VRtrMplsTunnelCHopIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 12, 1, 6),
    _VRtrMplsTunnelCHopIpv6Addr_Type()
)
vRtrMplsTunnelCHopIpv6Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsTunnelCHopIpv6Addr.setStatus("current")


class _VRtrMplsTunnelCHopIpv6PrefixLen_Type(Integer32):
    """Custom type vRtrMplsTunnelCHopIpv6PrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_VRtrMplsTunnelCHopIpv6PrefixLen_Type.__name__ = "Integer32"
_VRtrMplsTunnelCHopIpv6PrefixLen_Object = MibTableColumn
vRtrMplsTunnelCHopIpv6PrefixLen = _VRtrMplsTunnelCHopIpv6PrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 12, 1, 7),
    _VRtrMplsTunnelCHopIpv6PrefixLen_Type()
)
vRtrMplsTunnelCHopIpv6PrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsTunnelCHopIpv6PrefixLen.setStatus("current")


class _VRtrMplsTunnelCHopAsNumber_Type(Integer32):
    """Custom type vRtrMplsTunnelCHopAsNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VRtrMplsTunnelCHopAsNumber_Type.__name__ = "Integer32"
_VRtrMplsTunnelCHopAsNumber_Object = MibTableColumn
vRtrMplsTunnelCHopAsNumber = _VRtrMplsTunnelCHopAsNumber_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 12, 1, 8),
    _VRtrMplsTunnelCHopAsNumber_Type()
)
vRtrMplsTunnelCHopAsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsTunnelCHopAsNumber.setStatus("current")
_VRtrMplsTunnelCHopLspId_Type = MplsLSPID
_VRtrMplsTunnelCHopLspId_Object = MibTableColumn
vRtrMplsTunnelCHopLspId = _VRtrMplsTunnelCHopLspId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 12, 1, 9),
    _VRtrMplsTunnelCHopLspId_Type()
)
vRtrMplsTunnelCHopLspId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsTunnelCHopLspId.setStatus("current")


class _VRtrMplsTunnelCHopStrictOrLoose_Type(Integer32):
    """Custom type vRtrMplsTunnelCHopStrictOrLoose based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("strict", 1),
          ("loose", 2))
    )


_VRtrMplsTunnelCHopStrictOrLoose_Type.__name__ = "Integer32"
_VRtrMplsTunnelCHopStrictOrLoose_Object = MibTableColumn
vRtrMplsTunnelCHopStrictOrLoose = _VRtrMplsTunnelCHopStrictOrLoose_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 12, 1, 10),
    _VRtrMplsTunnelCHopStrictOrLoose_Type()
)
vRtrMplsTunnelCHopStrictOrLoose.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsTunnelCHopStrictOrLoose.setStatus("current")
_VRtrMplsTunnelCHopEgressAdmGrp_Type = Unsigned32
_VRtrMplsTunnelCHopEgressAdmGrp_Object = MibTableColumn
vRtrMplsTunnelCHopEgressAdmGrp = _VRtrMplsTunnelCHopEgressAdmGrp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 12, 1, 11),
    _VRtrMplsTunnelCHopEgressAdmGrp_Type()
)
vRtrMplsTunnelCHopEgressAdmGrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsTunnelCHopEgressAdmGrp.setStatus("current")
_VRtrMplsTunnelCHopUnnumIfID_Type = Unsigned32
_VRtrMplsTunnelCHopUnnumIfID_Object = MibTableColumn
vRtrMplsTunnelCHopUnnumIfID = _VRtrMplsTunnelCHopUnnumIfID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 12, 1, 12),
    _VRtrMplsTunnelCHopUnnumIfID_Type()
)
vRtrMplsTunnelCHopUnnumIfID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsTunnelCHopUnnumIfID.setStatus("current")
_VRtrMplsTunnelCHopRtrID_Type = IpAddress
_VRtrMplsTunnelCHopRtrID_Object = MibTableColumn
vRtrMplsTunnelCHopRtrID = _VRtrMplsTunnelCHopRtrID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 12, 1, 13),
    _VRtrMplsTunnelCHopRtrID_Type()
)
vRtrMplsTunnelCHopRtrID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsTunnelCHopRtrID.setStatus("current")
_VRtrMplsTunnelCHopIsABR_Type = TruthValue
_VRtrMplsTunnelCHopIsABR_Object = MibTableColumn
vRtrMplsTunnelCHopIsABR = _VRtrMplsTunnelCHopIsABR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 12, 1, 14),
    _VRtrMplsTunnelCHopIsABR_Type()
)
vRtrMplsTunnelCHopIsABR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsTunnelCHopIsABR.setStatus("current")
_VRtrMplsAdminGroupTable_Object = MibTable
vRtrMplsAdminGroupTable = _VRtrMplsAdminGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 13)
)
if mibBuilder.loadTexts:
    vRtrMplsAdminGroupTable.setStatus("obsolete")
_VRtrMplsAdminGroupEntry_Object = MibTableRow
vRtrMplsAdminGroupEntry = _VRtrMplsAdminGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 13, 1)
)
vRtrMplsAdminGroupEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (1, "TIMETRA-MPLS-MIB", "vRtrMplsAdminGroupName"),
)
if mibBuilder.loadTexts:
    vRtrMplsAdminGroupEntry.setStatus("obsolete")
_VRtrMplsAdminGroupName_Type = TNamedItem
_VRtrMplsAdminGroupName_Object = MibTableColumn
vRtrMplsAdminGroupName = _VRtrMplsAdminGroupName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 13, 1, 1),
    _VRtrMplsAdminGroupName_Type()
)
vRtrMplsAdminGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsAdminGroupName.setStatus("obsolete")
_VRtrMplsAdminGroupRowStatus_Type = RowStatus
_VRtrMplsAdminGroupRowStatus_Object = MibTableColumn
vRtrMplsAdminGroupRowStatus = _VRtrMplsAdminGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 13, 1, 2),
    _VRtrMplsAdminGroupRowStatus_Type()
)
vRtrMplsAdminGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsAdminGroupRowStatus.setStatus("obsolete")


class _VRtrMplsAdminGroupValue_Type(Integer32):
    """Custom type vRtrMplsAdminGroupValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 31),
    )


_VRtrMplsAdminGroupValue_Type.__name__ = "Integer32"
_VRtrMplsAdminGroupValue_Object = MibTableColumn
vRtrMplsAdminGroupValue = _VRtrMplsAdminGroupValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 13, 1, 3),
    _VRtrMplsAdminGroupValue_Type()
)
vRtrMplsAdminGroupValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsAdminGroupValue.setStatus("obsolete")
_VRtrMplsFSGroupTable_Object = MibTable
vRtrMplsFSGroupTable = _VRtrMplsFSGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 14)
)
if mibBuilder.loadTexts:
    vRtrMplsFSGroupTable.setStatus("obsolete")
_VRtrMplsFSGroupEntry_Object = MibTableRow
vRtrMplsFSGroupEntry = _VRtrMplsFSGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 14, 1)
)
vRtrMplsFSGroupEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsFSGroupName"),
)
if mibBuilder.loadTexts:
    vRtrMplsFSGroupEntry.setStatus("obsolete")
_VRtrMplsFSGroupName_Type = TNamedItem
_VRtrMplsFSGroupName_Object = MibTableColumn
vRtrMplsFSGroupName = _VRtrMplsFSGroupName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 14, 1, 1),
    _VRtrMplsFSGroupName_Type()
)
vRtrMplsFSGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsFSGroupName.setStatus("obsolete")
_VRtrMplsFSGroupRowStatus_Type = RowStatus
_VRtrMplsFSGroupRowStatus_Object = MibTableColumn
vRtrMplsFSGroupRowStatus = _VRtrMplsFSGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 14, 1, 2),
    _VRtrMplsFSGroupRowStatus_Type()
)
vRtrMplsFSGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsFSGroupRowStatus.setStatus("obsolete")


class _VRtrMplsFSGroupCost_Type(Unsigned32):
    """Custom type vRtrMplsFSGroupCost based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VRtrMplsFSGroupCost_Type.__name__ = "Unsigned32"
_VRtrMplsFSGroupCost_Object = MibTableColumn
vRtrMplsFSGroupCost = _VRtrMplsFSGroupCost_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 14, 1, 3),
    _VRtrMplsFSGroupCost_Type()
)
vRtrMplsFSGroupCost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsFSGroupCost.setStatus("obsolete")
_VRtrMplsFSGroupParamsTable_Object = MibTable
vRtrMplsFSGroupParamsTable = _VRtrMplsFSGroupParamsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 15)
)
if mibBuilder.loadTexts:
    vRtrMplsFSGroupParamsTable.setStatus("obsolete")
_VRtrMplsFSGroupParamsEntry_Object = MibTableRow
vRtrMplsFSGroupParamsEntry = _VRtrMplsFSGroupParamsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 15, 1)
)
vRtrMplsFSGroupParamsEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsFSGroupName"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsFSGroupParamsFromAddr"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsFSGroupParamsToAddr"),
)
if mibBuilder.loadTexts:
    vRtrMplsFSGroupParamsEntry.setStatus("obsolete")
_VRtrMplsFSGroupParamsFromAddr_Type = IpAddress
_VRtrMplsFSGroupParamsFromAddr_Object = MibTableColumn
vRtrMplsFSGroupParamsFromAddr = _VRtrMplsFSGroupParamsFromAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 15, 1, 1),
    _VRtrMplsFSGroupParamsFromAddr_Type()
)
vRtrMplsFSGroupParamsFromAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsFSGroupParamsFromAddr.setStatus("obsolete")
_VRtrMplsFSGroupParamsToAddr_Type = IpAddress
_VRtrMplsFSGroupParamsToAddr_Object = MibTableColumn
vRtrMplsFSGroupParamsToAddr = _VRtrMplsFSGroupParamsToAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 15, 1, 2),
    _VRtrMplsFSGroupParamsToAddr_Type()
)
vRtrMplsFSGroupParamsToAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsFSGroupParamsToAddr.setStatus("obsolete")
_VRtrMplsFSGroupParamsRowStatus_Type = RowStatus
_VRtrMplsFSGroupParamsRowStatus_Object = MibTableColumn
vRtrMplsFSGroupParamsRowStatus = _VRtrMplsFSGroupParamsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 15, 1, 3),
    _VRtrMplsFSGroupParamsRowStatus_Type()
)
vRtrMplsFSGroupParamsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsFSGroupParamsRowStatus.setStatus("obsolete")
_TmnxMplsNotificationObjects_ObjectIdentity = ObjectIdentity
tmnxMplsNotificationObjects = _TmnxMplsNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 16)
)


class _VRtrMplsLspNotificationReasonCode_Type(Integer32):
    """Custom type vRtrMplsLspNotificationReasonCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noError", 0),
          ("noPathIsOperational", 1))
    )


_VRtrMplsLspNotificationReasonCode_Type.__name__ = "Integer32"
_VRtrMplsLspNotificationReasonCode_Object = MibScalar
vRtrMplsLspNotificationReasonCode = _VRtrMplsLspNotificationReasonCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 16, 1),
    _VRtrMplsLspNotificationReasonCode_Type()
)
vRtrMplsLspNotificationReasonCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrMplsLspNotificationReasonCode.setStatus("current")
_VRtrMplsLspPathNotificationReasonCode_Type = TmnxMplsLspFailCode
_VRtrMplsLspPathNotificationReasonCode_Object = MibScalar
vRtrMplsLspPathNotificationReasonCode = _VRtrMplsLspPathNotificationReasonCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 16, 2),
    _VRtrMplsLspPathNotificationReasonCode_Type()
)
vRtrMplsLspPathNotificationReasonCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrMplsLspPathNotificationReasonCode.setStatus("current")
_VRtrMplsNotifyRow_Type = RowPointer
_VRtrMplsNotifyRow_Object = MibScalar
vRtrMplsNotifyRow = _VRtrMplsNotifyRow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 16, 3),
    _VRtrMplsNotifyRow_Type()
)
vRtrMplsNotifyRow.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrMplsNotifyRow.setStatus("current")
_VRtrMplsP2mpInstNotifIndex_Type = TmnxVRtrMplsLspID
_VRtrMplsP2mpInstNotifIndex_Object = MibScalar
vRtrMplsP2mpInstNotifIndex = _VRtrMplsP2mpInstNotifIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 16, 4),
    _VRtrMplsP2mpInstNotifIndex_Type()
)
vRtrMplsP2mpInstNotifIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstNotifIndex.setStatus("current")
_VRtrMplsP2mpInstNotifReasonCode_Type = TmnxMplsP2mpInstFailCode
_VRtrMplsP2mpInstNotifReasonCode_Object = MibScalar
vRtrMplsP2mpInstNotifReasonCode = _VRtrMplsP2mpInstNotifReasonCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 16, 5),
    _VRtrMplsP2mpInstNotifReasonCode_Type()
)
vRtrMplsP2mpInstNotifReasonCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstNotifReasonCode.setStatus("current")
_VRtrMplsS2lSubLspNtDstAddrType_Type = InetAddressType
_VRtrMplsS2lSubLspNtDstAddrType_Object = MibScalar
vRtrMplsS2lSubLspNtDstAddrType = _VRtrMplsS2lSubLspNtDstAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 16, 6),
    _VRtrMplsS2lSubLspNtDstAddrType_Type()
)
vRtrMplsS2lSubLspNtDstAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspNtDstAddrType.setStatus("current")


class _VRtrMplsS2lSubLspNtDstAddr_Type(InetAddress):
    """Custom type vRtrMplsS2lSubLspNtDstAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_VRtrMplsS2lSubLspNtDstAddr_Type.__name__ = "InetAddress"
_VRtrMplsS2lSubLspNtDstAddr_Object = MibScalar
vRtrMplsS2lSubLspNtDstAddr = _VRtrMplsS2lSubLspNtDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 16, 7),
    _VRtrMplsS2lSubLspNtDstAddr_Type()
)
vRtrMplsS2lSubLspNtDstAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspNtDstAddr.setStatus("current")
_VRtrMplsLspPathCongChgPercent_Type = Unsigned32
_VRtrMplsLspPathCongChgPercent_Object = MibScalar
vRtrMplsLspPathCongChgPercent = _VRtrMplsLspPathCongChgPercent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 16, 8),
    _VRtrMplsLspPathCongChgPercent_Type()
)
vRtrMplsLspPathCongChgPercent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrMplsLspPathCongChgPercent.setStatus("current")


class _VRtrMplsLspPathMbbStatus_Type(Integer32):
    """Custom type vRtrMplsLspPathMbbStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("successful", 0),
          ("failed", 1),
          ("aborted", 2),
          ("ignored", 3))
    )


_VRtrMplsLspPathMbbStatus_Type.__name__ = "Integer32"
_VRtrMplsLspPathMbbStatus_Object = MibScalar
vRtrMplsLspPathMbbStatus = _VRtrMplsLspPathMbbStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 16, 9),
    _VRtrMplsLspPathMbbStatus_Type()
)
vRtrMplsLspPathMbbStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrMplsLspPathMbbStatus.setStatus("current")


class _VRtrMplsLspPathMbbReasonCode_Type(Integer32):
    """Custom type vRtrMplsLspPathMbbReasonCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("mbbRetryExceeded", 1),
          ("lspPathGoingDown", 2),
          ("startingHighPriMbb", 3),
          ("restartingMbb", 4),
          ("mbbAlreadyInProg", 5),
          ("lspPceControlled", 6),
          ("lspNotPceControlled", 7))
    )


_VRtrMplsLspPathMbbReasonCode_Type.__name__ = "Integer32"
_VRtrMplsLspPathMbbReasonCode_Object = MibScalar
vRtrMplsLspPathMbbReasonCode = _VRtrMplsLspPathMbbReasonCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 16, 10),
    _VRtrMplsLspPathMbbReasonCode_Type()
)
vRtrMplsLspPathMbbReasonCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrMplsLspPathMbbReasonCode.setStatus("current")


class _VRtrMplsLspSwitchStbyReasonCode_Type(Integer32):
    """Custom type vRtrMplsLspSwitchStbyReasonCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("lspIsDown", 1),
          ("lspIsNotDynamic", 2),
          ("lspHasNoActivePath", 3),
          ("lspActivePathIsNotStandby", 4),
          ("pathSpecifiedIsNotLspPath", 5),
          ("pathSpecifiedIsNotStandby", 6),
          ("pathSpecifiedIsDown", 7),
          ("pathHasDiffPrefThanActLspPath", 8),
          ("lspHoldTimerIsRunning", 9),
          ("currentLspPathActiveByForce", 10),
          ("lspPathInPreemption", 11),
          ("lspActivePathIsPrimary", 12),
          ("currentActivePathIsBest", 13),
          ("betterPathFound", 14),
          ("currentActivePathWentDown", 15))
    )


_VRtrMplsLspSwitchStbyReasonCode_Type.__name__ = "Integer32"
_VRtrMplsLspSwitchStbyReasonCode_Object = MibScalar
vRtrMplsLspSwitchStbyReasonCode = _VRtrMplsLspSwitchStbyReasonCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 16, 13),
    _VRtrMplsLspSwitchStbyReasonCode_Type()
)
vRtrMplsLspSwitchStbyReasonCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrMplsLspSwitchStbyReasonCode.setStatus("current")
_VRtrMplsLspOldTunnelIndex_Type = MplsTunnelIndex
_VRtrMplsLspOldTunnelIndex_Object = MibScalar
vRtrMplsLspOldTunnelIndex = _VRtrMplsLspOldTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 16, 14),
    _VRtrMplsLspOldTunnelIndex_Type()
)
vRtrMplsLspOldTunnelIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrMplsLspOldTunnelIndex.setStatus("current")


class _VRtrMplsXCNotifRednIndicesBitMap_Type(OctetString):
    """Custom type vRtrMplsXCNotifRednIndicesBitMap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1000),
    )


_VRtrMplsXCNotifRednIndicesBitMap_Type.__name__ = "OctetString"
_VRtrMplsXCNotifRednIndicesBitMap_Object = MibScalar
vRtrMplsXCNotifRednIndicesBitMap = _VRtrMplsXCNotifRednIndicesBitMap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 16, 15),
    _VRtrMplsXCNotifRednIndicesBitMap_Type()
)
vRtrMplsXCNotifRednIndicesBitMap.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrMplsXCNotifRednIndicesBitMap.setStatus("current")


class _VRtrMplsXCNotifyRednBundlingType_Type(Integer32):
    """Custom type vRtrMplsXCNotifyRednBundlingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 1),
          ("create", 2))
    )


_VRtrMplsXCNotifyRednBundlingType_Type.__name__ = "Integer32"
_VRtrMplsXCNotifyRednBundlingType_Object = MibScalar
vRtrMplsXCNotifyRednBundlingType = _VRtrMplsXCNotifyRednBundlingType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 16, 16),
    _VRtrMplsXCNotifyRednBundlingType_Type()
)
vRtrMplsXCNotifyRednBundlingType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrMplsXCNotifyRednBundlingType.setStatus("current")
_VRtrMplsXCNotifyRednNumOfBitsSet_Type = Unsigned32
_VRtrMplsXCNotifyRednNumOfBitsSet_Object = MibScalar
vRtrMplsXCNotifyRednNumOfBitsSet = _VRtrMplsXCNotifyRednNumOfBitsSet_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 16, 17),
    _VRtrMplsXCNotifyRednNumOfBitsSet_Type()
)
vRtrMplsXCNotifyRednNumOfBitsSet.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrMplsXCNotifyRednNumOfBitsSet.setStatus("current")
_VRtrMplsXCNotifyRednStartIndex_Type = Unsigned32
_VRtrMplsXCNotifyRednStartIndex_Object = MibScalar
vRtrMplsXCNotifyRednStartIndex = _VRtrMplsXCNotifyRednStartIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 16, 18),
    _VRtrMplsXCNotifyRednStartIndex_Type()
)
vRtrMplsXCNotifyRednStartIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrMplsXCNotifyRednStartIndex.setStatus("current")
_VRtrMplsXCNotifyRednEndIndex_Type = Unsigned32
_VRtrMplsXCNotifyRednEndIndex_Object = MibScalar
vRtrMplsXCNotifyRednEndIndex = _VRtrMplsXCNotifyRednEndIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 16, 19),
    _VRtrMplsXCNotifyRednEndIndex_Type()
)
vRtrMplsXCNotifyRednEndIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrMplsXCNotifyRednEndIndex.setStatus("current")
_VRtrMplsIgpOverloadRtrAddrType_Type = InetAddressType
_VRtrMplsIgpOverloadRtrAddrType_Object = MibScalar
vRtrMplsIgpOverloadRtrAddrType = _VRtrMplsIgpOverloadRtrAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 16, 20),
    _VRtrMplsIgpOverloadRtrAddrType_Type()
)
vRtrMplsIgpOverloadRtrAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrMplsIgpOverloadRtrAddrType.setStatus("current")


class _VRtrMplsIgpOverloadRtrAddr_Type(InetAddress):
    """Custom type vRtrMplsIgpOverloadRtrAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrMplsIgpOverloadRtrAddr_Type.__name__ = "InetAddress"
_VRtrMplsIgpOverloadRtrAddr_Object = MibScalar
vRtrMplsIgpOverloadRtrAddr = _VRtrMplsIgpOverloadRtrAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 16, 21),
    _VRtrMplsIgpOverloadRtrAddr_Type()
)
vRtrMplsIgpOverloadRtrAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrMplsIgpOverloadRtrAddr.setStatus("current")


class _VRtrMplsIgpOverloadIgpType_Type(Integer32):
    """Custom type vRtrMplsIgpOverloadIgpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("isis", 1),
          ("ospf", 2))
    )


_VRtrMplsIgpOverloadIgpType_Type.__name__ = "Integer32"
_VRtrMplsIgpOverloadIgpType_Object = MibScalar
vRtrMplsIgpOverloadIgpType = _VRtrMplsIgpOverloadIgpType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 16, 22),
    _VRtrMplsIgpOverloadIgpType_Type()
)
vRtrMplsIgpOverloadIgpType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrMplsIgpOverloadIgpType.setStatus("current")
_VRtrMplsLabelRangeTable_Object = MibTable
vRtrMplsLabelRangeTable = _VRtrMplsLabelRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 17)
)
if mibBuilder.loadTexts:
    vRtrMplsLabelRangeTable.setStatus("current")
_VRtrMplsLabelRangeEntry_Object = MibTableRow
vRtrMplsLabelRangeEntry = _VRtrMplsLabelRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 17, 1)
)
vRtrMplsLabelRangeEntry.setIndexNames(
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsLabelType"),
)
if mibBuilder.loadTexts:
    vRtrMplsLabelRangeEntry.setStatus("current")


class _VRtrMplsLabelType_Type(Integer32):
    """Custom type vRtrMplsLabelType based on Integer32"""
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
        *(("staticLsp", 1),
          ("staticSvc", 2),
          ("dynamic", 3),
          ("segmentRoute", 4),
          ("static", 5))
    )


_VRtrMplsLabelType_Type.__name__ = "Integer32"
_VRtrMplsLabelType_Object = MibTableColumn
vRtrMplsLabelType = _VRtrMplsLabelType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 17, 1, 1),
    _VRtrMplsLabelType_Type()
)
vRtrMplsLabelType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsLabelType.setStatus("current")
_VRtrMplsLabelRangeMin_Type = Unsigned32
_VRtrMplsLabelRangeMin_Object = MibTableColumn
vRtrMplsLabelRangeMin = _VRtrMplsLabelRangeMin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 17, 1, 2),
    _VRtrMplsLabelRangeMin_Type()
)
vRtrMplsLabelRangeMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLabelRangeMin.setStatus("current")
_VRtrMplsLabelRangeMax_Type = Unsigned32
_VRtrMplsLabelRangeMax_Object = MibTableColumn
vRtrMplsLabelRangeMax = _VRtrMplsLabelRangeMax_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 17, 1, 3),
    _VRtrMplsLabelRangeMax_Type()
)
vRtrMplsLabelRangeMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLabelRangeMax.setStatus("current")
_VRtrMplsLabelRangeAging_Type = Unsigned32
_VRtrMplsLabelRangeAging_Object = MibTableColumn
vRtrMplsLabelRangeAging = _VRtrMplsLabelRangeAging_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 17, 1, 4),
    _VRtrMplsLabelRangeAging_Type()
)
vRtrMplsLabelRangeAging.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLabelRangeAging.setStatus("current")
_VRtrMplsLabelRangeAvailable_Type = Unsigned32
_VRtrMplsLabelRangeAvailable_Object = MibTableColumn
vRtrMplsLabelRangeAvailable = _VRtrMplsLabelRangeAvailable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 17, 1, 5),
    _VRtrMplsLabelRangeAvailable_Type()
)
vRtrMplsLabelRangeAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLabelRangeAvailable.setStatus("current")
_VRtrMplsStaticLSPLabelTable_Object = MibTable
vRtrMplsStaticLSPLabelTable = _VRtrMplsStaticLSPLabelTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 18)
)
if mibBuilder.loadTexts:
    vRtrMplsStaticLSPLabelTable.setStatus("current")
_VRtrMplsStaticLSPLabelEntry_Object = MibTableRow
vRtrMplsStaticLSPLabelEntry = _VRtrMplsStaticLSPLabelEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 18, 1)
)
vRtrMplsStaticLSPLabelEntry.setIndexNames(
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsStaticLSPLabel"),
)
if mibBuilder.loadTexts:
    vRtrMplsStaticLSPLabelEntry.setStatus("current")


class _VRtrMplsStaticLSPLabel_Type(MplsLabel):
    """Custom type vRtrMplsStaticLSPLabel based on MplsLabel"""
    subtypeSpec = MplsLabel.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 262112),
    )


_VRtrMplsStaticLSPLabel_Type.__name__ = "MplsLabel"
_VRtrMplsStaticLSPLabel_Object = MibTableColumn
vRtrMplsStaticLSPLabel = _VRtrMplsStaticLSPLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 18, 1, 1),
    _VRtrMplsStaticLSPLabel_Type()
)
vRtrMplsStaticLSPLabel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsStaticLSPLabel.setStatus("current")
_VRtrMplsStaticLSPLabelOwner_Type = TmnxMplsLabelOwner
_VRtrMplsStaticLSPLabelOwner_Object = MibTableColumn
vRtrMplsStaticLSPLabelOwner = _VRtrMplsStaticLSPLabelOwner_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 18, 1, 2),
    _VRtrMplsStaticLSPLabelOwner_Type()
)
vRtrMplsStaticLSPLabelOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsStaticLSPLabelOwner.setStatus("current")
_VRtrMplsStaticSvcLabelTable_Object = MibTable
vRtrMplsStaticSvcLabelTable = _VRtrMplsStaticSvcLabelTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 19)
)
if mibBuilder.loadTexts:
    vRtrMplsStaticSvcLabelTable.setStatus("current")
_VRtrMplsStaticSvcLabelEntry_Object = MibTableRow
vRtrMplsStaticSvcLabelEntry = _VRtrMplsStaticSvcLabelEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 19, 1)
)
vRtrMplsStaticSvcLabelEntry.setIndexNames(
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsStaticSvcLabel"),
)
if mibBuilder.loadTexts:
    vRtrMplsStaticSvcLabelEntry.setStatus("current")


class _VRtrMplsStaticSvcLabel_Type(MplsLabel):
    """Custom type vRtrMplsStaticSvcLabel based on MplsLabel"""
    subtypeSpec = MplsLabel.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 262112),
    )


_VRtrMplsStaticSvcLabel_Type.__name__ = "MplsLabel"
_VRtrMplsStaticSvcLabel_Object = MibTableColumn
vRtrMplsStaticSvcLabel = _VRtrMplsStaticSvcLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 19, 1, 1),
    _VRtrMplsStaticSvcLabel_Type()
)
vRtrMplsStaticSvcLabel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsStaticSvcLabel.setStatus("current")


class _VRtrMplsStaticSvcLabelOwner_Type(TmnxMplsLabelOwner):
    """Custom type vRtrMplsStaticSvcLabelOwner based on TmnxMplsLabelOwner"""
    defaultValue = 0


_VRtrMplsStaticSvcLabelOwner_Type.__name__ = "TmnxMplsLabelOwner"
_VRtrMplsStaticSvcLabelOwner_Object = MibTableColumn
vRtrMplsStaticSvcLabelOwner = _VRtrMplsStaticSvcLabelOwner_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 19, 1, 2),
    _VRtrMplsStaticSvcLabelOwner_Type()
)
vRtrMplsStaticSvcLabelOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsStaticSvcLabelOwner.setStatus("current")
_VRtrMplsSrlgGrpTableLastChanged_Type = TimeStamp
_VRtrMplsSrlgGrpTableLastChanged_Object = MibScalar
vRtrMplsSrlgGrpTableLastChanged = _VRtrMplsSrlgGrpTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 20),
    _VRtrMplsSrlgGrpTableLastChanged_Type()
)
vRtrMplsSrlgGrpTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsSrlgGrpTableLastChanged.setStatus("obsolete")
_VRtrMplsSrlgGrpTable_Object = MibTable
vRtrMplsSrlgGrpTable = _VRtrMplsSrlgGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 21)
)
if mibBuilder.loadTexts:
    vRtrMplsSrlgGrpTable.setStatus("obsolete")
_VRtrMplsSrlgGrpEntry_Object = MibTableRow
vRtrMplsSrlgGrpEntry = _VRtrMplsSrlgGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 21, 1)
)
vRtrMplsSrlgGrpEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (1, "TIMETRA-MPLS-MIB", "vRtrMplsSrlgGrpName"),
)
if mibBuilder.loadTexts:
    vRtrMplsSrlgGrpEntry.setStatus("obsolete")
_VRtrMplsSrlgGrpName_Type = TNamedItem
_VRtrMplsSrlgGrpName_Object = MibTableColumn
vRtrMplsSrlgGrpName = _VRtrMplsSrlgGrpName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 21, 1, 1),
    _VRtrMplsSrlgGrpName_Type()
)
vRtrMplsSrlgGrpName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsSrlgGrpName.setStatus("obsolete")
_VRtrMplsSrlgGrpRowStatus_Type = RowStatus
_VRtrMplsSrlgGrpRowStatus_Object = MibTableColumn
vRtrMplsSrlgGrpRowStatus = _VRtrMplsSrlgGrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 21, 1, 2),
    _VRtrMplsSrlgGrpRowStatus_Type()
)
vRtrMplsSrlgGrpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsSrlgGrpRowStatus.setStatus("obsolete")
_VRtrMplsSrlgGrpLastChanged_Type = TimeStamp
_VRtrMplsSrlgGrpLastChanged_Object = MibTableColumn
vRtrMplsSrlgGrpLastChanged = _VRtrMplsSrlgGrpLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 21, 1, 3),
    _VRtrMplsSrlgGrpLastChanged_Type()
)
vRtrMplsSrlgGrpLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsSrlgGrpLastChanged.setStatus("obsolete")
_VRtrMplsSrlgGrpValue_Type = Unsigned32
_VRtrMplsSrlgGrpValue_Object = MibTableColumn
vRtrMplsSrlgGrpValue = _VRtrMplsSrlgGrpValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 21, 1, 4),
    _VRtrMplsSrlgGrpValue_Type()
)
vRtrMplsSrlgGrpValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsSrlgGrpValue.setStatus("obsolete")
_VRtrMplsIfSrlgGrpTblLastChanged_Type = TimeStamp
_VRtrMplsIfSrlgGrpTblLastChanged_Object = MibScalar
vRtrMplsIfSrlgGrpTblLastChanged = _VRtrMplsIfSrlgGrpTblLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 22),
    _VRtrMplsIfSrlgGrpTblLastChanged_Type()
)
vRtrMplsIfSrlgGrpTblLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsIfSrlgGrpTblLastChanged.setStatus("current")
_VRtrMplsIfSrlgGrpTable_Object = MibTable
vRtrMplsIfSrlgGrpTable = _VRtrMplsIfSrlgGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 23)
)
if mibBuilder.loadTexts:
    vRtrMplsIfSrlgGrpTable.setStatus("current")
_VRtrMplsIfSrlgGrpEntry_Object = MibTableRow
vRtrMplsIfSrlgGrpEntry = _VRtrMplsIfSrlgGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 23, 1)
)
vRtrMplsIfSrlgGrpEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-VRTR-MIB", "vRtrIfIndex"),
    (1, "TIMETRA-MPLS-MIB", "vRtrMplsIfSrlgGrpName"),
)
if mibBuilder.loadTexts:
    vRtrMplsIfSrlgGrpEntry.setStatus("current")
_VRtrMplsIfSrlgGrpName_Type = TNamedItem
_VRtrMplsIfSrlgGrpName_Object = MibTableColumn
vRtrMplsIfSrlgGrpName = _VRtrMplsIfSrlgGrpName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 23, 1, 1),
    _VRtrMplsIfSrlgGrpName_Type()
)
vRtrMplsIfSrlgGrpName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsIfSrlgGrpName.setStatus("current")
_VRtrMplsIfSrlgGrpRowStatus_Type = RowStatus
_VRtrMplsIfSrlgGrpRowStatus_Object = MibTableColumn
vRtrMplsIfSrlgGrpRowStatus = _VRtrMplsIfSrlgGrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 23, 1, 2),
    _VRtrMplsIfSrlgGrpRowStatus_Type()
)
vRtrMplsIfSrlgGrpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsIfSrlgGrpRowStatus.setStatus("current")
_VRtrMplsIfSrlgGrpLastChanged_Type = TimeStamp
_VRtrMplsIfSrlgGrpLastChanged_Object = MibTableColumn
vRtrMplsIfSrlgGrpLastChanged = _VRtrMplsIfSrlgGrpLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 23, 1, 3),
    _VRtrMplsIfSrlgGrpLastChanged_Type()
)
vRtrMplsIfSrlgGrpLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsIfSrlgGrpLastChanged.setStatus("current")
_VRtrMplsP2mpInstTblLastChanged_Type = TimeStamp
_VRtrMplsP2mpInstTblLastChanged_Object = MibScalar
vRtrMplsP2mpInstTblLastChanged = _VRtrMplsP2mpInstTblLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 24),
    _VRtrMplsP2mpInstTblLastChanged_Type()
)
vRtrMplsP2mpInstTblLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstTblLastChanged.setStatus("current")
_VRtrMplsP2mpInstTable_Object = MibTable
vRtrMplsP2mpInstTable = _VRtrMplsP2mpInstTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 25)
)
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstTable.setStatus("current")
_VRtrMplsP2mpInstEntry_Object = MibTableRow
vRtrMplsP2mpInstEntry = _VRtrMplsP2mpInstEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 25, 1)
)
vRtrMplsP2mpInstEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsLspIndex"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstIndex"),
)
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstEntry.setStatus("current")
_VRtrMplsP2mpInstIndex_Type = TmnxVRtrMplsLspID
_VRtrMplsP2mpInstIndex_Object = MibTableColumn
vRtrMplsP2mpInstIndex = _VRtrMplsP2mpInstIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 25, 1, 1),
    _VRtrMplsP2mpInstIndex_Type()
)
vRtrMplsP2mpInstIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstIndex.setStatus("current")
_VRtrMplsP2mpInstRowStatus_Type = RowStatus
_VRtrMplsP2mpInstRowStatus_Object = MibTableColumn
vRtrMplsP2mpInstRowStatus = _VRtrMplsP2mpInstRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 25, 1, 2),
    _VRtrMplsP2mpInstRowStatus_Type()
)
vRtrMplsP2mpInstRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstRowStatus.setStatus("current")
_VRtrMplsP2mpInstLastChange_Type = TimeStamp
_VRtrMplsP2mpInstLastChange_Object = MibTableColumn
vRtrMplsP2mpInstLastChange = _VRtrMplsP2mpInstLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 25, 1, 3),
    _VRtrMplsP2mpInstLastChange_Type()
)
vRtrMplsP2mpInstLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstLastChange.setStatus("current")
_VRtrMplsP2mpInstName_Type = TNamedItemOrEmpty
_VRtrMplsP2mpInstName_Object = MibTableColumn
vRtrMplsP2mpInstName = _VRtrMplsP2mpInstName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 25, 1, 4),
    _VRtrMplsP2mpInstName_Type()
)
vRtrMplsP2mpInstName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstName.setStatus("current")


class _VRtrMplsP2mpInstType_Type(Integer32):
    """Custom type vRtrMplsP2mpInstType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("primary", 2))
    )


_VRtrMplsP2mpInstType_Type.__name__ = "Integer32"
_VRtrMplsP2mpInstType_Object = MibTableColumn
vRtrMplsP2mpInstType = _VRtrMplsP2mpInstType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 25, 1, 5),
    _VRtrMplsP2mpInstType_Type()
)
vRtrMplsP2mpInstType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstType.setStatus("current")


class _VRtrMplsP2mpInstProperties_Type(Bits):
    """Custom type vRtrMplsP2mpInstProperties based on Bits"""
    namedValues = NamedValues(
        *(("recordRoute", 0),
          ("adaptive", 1),
          ("cspf", 2),
          ("mergeable", 3),
          ("fastReroute", 4))
    )

_VRtrMplsP2mpInstProperties_Type.__name__ = "Bits"
_VRtrMplsP2mpInstProperties_Object = MibTableColumn
vRtrMplsP2mpInstProperties = _VRtrMplsP2mpInstProperties_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 25, 1, 6),
    _VRtrMplsP2mpInstProperties_Type()
)
vRtrMplsP2mpInstProperties.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstProperties.setStatus("current")


class _VRtrMplsP2mpInstBandwidth_Type(Unsigned32):
    """Custom type vRtrMplsP2mpInstBandwidth based on Unsigned32"""
    defaultValue = 0


_VRtrMplsP2mpInstBandwidth_Type.__name__ = "Unsigned32"
_VRtrMplsP2mpInstBandwidth_Object = MibTableColumn
vRtrMplsP2mpInstBandwidth = _VRtrMplsP2mpInstBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 25, 1, 7),
    _VRtrMplsP2mpInstBandwidth_Type()
)
vRtrMplsP2mpInstBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstBandwidth.setUnits("mega-bits per second")


class _VRtrMplsP2mpInstState_Type(Integer32):
    """Custom type vRtrMplsP2mpInstState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("active", 2),
          ("inactive", 3))
    )


_VRtrMplsP2mpInstState_Type.__name__ = "Integer32"
_VRtrMplsP2mpInstState_Object = MibTableColumn
vRtrMplsP2mpInstState = _VRtrMplsP2mpInstState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 25, 1, 8),
    _VRtrMplsP2mpInstState_Type()
)
vRtrMplsP2mpInstState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstState.setStatus("current")


class _VRtrMplsP2mpInstSetupPriority_Type(Unsigned32):
    """Custom type vRtrMplsP2mpInstSetupPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_VRtrMplsP2mpInstSetupPriority_Type.__name__ = "Unsigned32"
_VRtrMplsP2mpInstSetupPriority_Object = MibTableColumn
vRtrMplsP2mpInstSetupPriority = _VRtrMplsP2mpInstSetupPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 25, 1, 9),
    _VRtrMplsP2mpInstSetupPriority_Type()
)
vRtrMplsP2mpInstSetupPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstSetupPriority.setStatus("current")


class _VRtrMplsP2mpInstHoldPriority_Type(Unsigned32):
    """Custom type vRtrMplsP2mpInstHoldPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_VRtrMplsP2mpInstHoldPriority_Type.__name__ = "Unsigned32"
_VRtrMplsP2mpInstHoldPriority_Object = MibTableColumn
vRtrMplsP2mpInstHoldPriority = _VRtrMplsP2mpInstHoldPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 25, 1, 10),
    _VRtrMplsP2mpInstHoldPriority_Type()
)
vRtrMplsP2mpInstHoldPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstHoldPriority.setStatus("current")


class _VRtrMplsP2mpInstRecord_Type(TruthValue):
    """Custom type vRtrMplsP2mpInstRecord based on TruthValue"""
    defaultValue = 1


_VRtrMplsP2mpInstRecord_Type.__name__ = "TruthValue"
_VRtrMplsP2mpInstRecord_Object = MibTableColumn
vRtrMplsP2mpInstRecord = _VRtrMplsP2mpInstRecord_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 25, 1, 11),
    _VRtrMplsP2mpInstRecord_Type()
)
vRtrMplsP2mpInstRecord.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstRecord.setStatus("current")


class _VRtrMplsP2mpInstHopLimit_Type(Unsigned32):
    """Custom type vRtrMplsP2mpInstHopLimit based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 255),
    )


_VRtrMplsP2mpInstHopLimit_Type.__name__ = "Unsigned32"
_VRtrMplsP2mpInstHopLimit_Object = MibTableColumn
vRtrMplsP2mpInstHopLimit = _VRtrMplsP2mpInstHopLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 25, 1, 12),
    _VRtrMplsP2mpInstHopLimit_Type()
)
vRtrMplsP2mpInstHopLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstHopLimit.setStatus("current")


class _VRtrMplsP2mpInstAdminState_Type(TmnxAdminState):
    """Custom type vRtrMplsP2mpInstAdminState based on TmnxAdminState"""
    defaultValue = 2


_VRtrMplsP2mpInstAdminState_Type.__name__ = "TmnxAdminState"
_VRtrMplsP2mpInstAdminState_Object = MibTableColumn
vRtrMplsP2mpInstAdminState = _VRtrMplsP2mpInstAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 25, 1, 13),
    _VRtrMplsP2mpInstAdminState_Type()
)
vRtrMplsP2mpInstAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstAdminState.setStatus("current")
_VRtrMplsP2mpInstOperState_Type = TmnxOperState
_VRtrMplsP2mpInstOperState_Object = MibTableColumn
vRtrMplsP2mpInstOperState = _VRtrMplsP2mpInstOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 25, 1, 14),
    _VRtrMplsP2mpInstOperState_Type()
)
vRtrMplsP2mpInstOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstOperState.setStatus("current")


class _VRtrMplsP2mpInstInheritance_Type(Unsigned32):
    """Custom type vRtrMplsP2mpInstInheritance based on Unsigned32"""
    defaultValue = 0


_VRtrMplsP2mpInstInheritance_Type.__name__ = "Unsigned32"
_VRtrMplsP2mpInstInheritance_Object = MibTableColumn
vRtrMplsP2mpInstInheritance = _VRtrMplsP2mpInstInheritance_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 25, 1, 15),
    _VRtrMplsP2mpInstInheritance_Type()
)
vRtrMplsP2mpInstInheritance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstInheritance.setStatus("current")
_VRtrMplsP2mpInstLspId_Type = MplsLSPID
_VRtrMplsP2mpInstLspId_Object = MibTableColumn
vRtrMplsP2mpInstLspId = _VRtrMplsP2mpInstLspId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 25, 1, 16),
    _VRtrMplsP2mpInstLspId_Type()
)
vRtrMplsP2mpInstLspId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstLspId.setStatus("current")
_VRtrMplsP2mpInstNegotiatedMTU_Type = Unsigned32
_VRtrMplsP2mpInstNegotiatedMTU_Object = MibTableColumn
vRtrMplsP2mpInstNegotiatedMTU = _VRtrMplsP2mpInstNegotiatedMTU_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 25, 1, 17),
    _VRtrMplsP2mpInstNegotiatedMTU_Type()
)
vRtrMplsP2mpInstNegotiatedMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstNegotiatedMTU.setStatus("current")
_VRtrMplsP2mpInstFailCode_Type = TmnxMplsLspFailCode
_VRtrMplsP2mpInstFailCode_Object = MibTableColumn
vRtrMplsP2mpInstFailCode = _VRtrMplsP2mpInstFailCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 25, 1, 18),
    _VRtrMplsP2mpInstFailCode_Type()
)
vRtrMplsP2mpInstFailCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstFailCode.setStatus("current")
_VRtrMplsP2mpInstFailNodeArType_Type = InetAddressType
_VRtrMplsP2mpInstFailNodeArType_Object = MibTableColumn
vRtrMplsP2mpInstFailNodeArType = _VRtrMplsP2mpInstFailNodeArType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 25, 1, 19),
    _VRtrMplsP2mpInstFailNodeArType_Type()
)
vRtrMplsP2mpInstFailNodeArType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstFailNodeArType.setStatus("current")


class _VRtrMplsP2mpInstFailNodeAddr_Type(InetAddress):
    """Custom type vRtrMplsP2mpInstFailNodeAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_VRtrMplsP2mpInstFailNodeAddr_Type.__name__ = "InetAddress"
_VRtrMplsP2mpInstFailNodeAddr_Object = MibTableColumn
vRtrMplsP2mpInstFailNodeAddr = _VRtrMplsP2mpInstFailNodeAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 25, 1, 20),
    _VRtrMplsP2mpInstFailNodeAddr_Type()
)
vRtrMplsP2mpInstFailNodeAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstFailNodeAddr.setStatus("current")


class _VRtrMplsP2mpInstAdminGrpInclude_Type(Unsigned32):
    """Custom type vRtrMplsP2mpInstAdminGrpInclude based on Unsigned32"""
    defaultValue = 0


_VRtrMplsP2mpInstAdminGrpInclude_Type.__name__ = "Unsigned32"
_VRtrMplsP2mpInstAdminGrpInclude_Object = MibTableColumn
vRtrMplsP2mpInstAdminGrpInclude = _VRtrMplsP2mpInstAdminGrpInclude_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 25, 1, 21),
    _VRtrMplsP2mpInstAdminGrpInclude_Type()
)
vRtrMplsP2mpInstAdminGrpInclude.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstAdminGrpInclude.setStatus("current")


class _VRtrMplsP2mpInstAdminGrpExclude_Type(Unsigned32):
    """Custom type vRtrMplsP2mpInstAdminGrpExclude based on Unsigned32"""
    defaultValue = 0


_VRtrMplsP2mpInstAdminGrpExclude_Type.__name__ = "Unsigned32"
_VRtrMplsP2mpInstAdminGrpExclude_Object = MibTableColumn
vRtrMplsP2mpInstAdminGrpExclude = _VRtrMplsP2mpInstAdminGrpExclude_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 25, 1, 22),
    _VRtrMplsP2mpInstAdminGrpExclude_Type()
)
vRtrMplsP2mpInstAdminGrpExclude.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstAdminGrpExclude.setStatus("current")


class _VRtrMplsP2mpInstAdaptive_Type(TruthValue):
    """Custom type vRtrMplsP2mpInstAdaptive based on TruthValue"""
    defaultValue = 1


_VRtrMplsP2mpInstAdaptive_Type.__name__ = "TruthValue"
_VRtrMplsP2mpInstAdaptive_Object = MibTableColumn
vRtrMplsP2mpInstAdaptive = _VRtrMplsP2mpInstAdaptive_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 25, 1, 23),
    _VRtrMplsP2mpInstAdaptive_Type()
)
vRtrMplsP2mpInstAdaptive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstAdaptive.setStatus("current")
_VRtrMplsP2mpInstOperBandwidth_Type = Integer32
_VRtrMplsP2mpInstOperBandwidth_Object = MibTableColumn
vRtrMplsP2mpInstOperBandwidth = _VRtrMplsP2mpInstOperBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 25, 1, 24),
    _VRtrMplsP2mpInstOperBandwidth_Type()
)
vRtrMplsP2mpInstOperBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstOperBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstOperBandwidth.setUnits("mega-bits per second")


class _VRtrMplsP2mpInstResignal_Type(TmnxActionType):
    """Custom type vRtrMplsP2mpInstResignal based on TmnxActionType"""
    defaultValue = 2


_VRtrMplsP2mpInstResignal_Type.__name__ = "TmnxActionType"
_VRtrMplsP2mpInstResignal_Object = MibTableColumn
vRtrMplsP2mpInstResignal = _VRtrMplsP2mpInstResignal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 25, 1, 25),
    _VRtrMplsP2mpInstResignal_Type()
)
vRtrMplsP2mpInstResignal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstResignal.setStatus("current")
_VRtrMplsP2mpInstOperMTU_Type = Unsigned32
_VRtrMplsP2mpInstOperMTU_Object = MibTableColumn
vRtrMplsP2mpInstOperMTU = _VRtrMplsP2mpInstOperMTU_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 25, 1, 26),
    _VRtrMplsP2mpInstOperMTU_Type()
)
vRtrMplsP2mpInstOperMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstOperMTU.setStatus("current")


class _VRtrMplsP2mpInstRecordLabel_Type(Integer32):
    """Custom type vRtrMplsP2mpInstRecordLabel based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("record", 1),
          ("noRecord", 2))
    )


_VRtrMplsP2mpInstRecordLabel_Type.__name__ = "Integer32"
_VRtrMplsP2mpInstRecordLabel_Object = MibTableColumn
vRtrMplsP2mpInstRecordLabel = _VRtrMplsP2mpInstRecordLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 25, 1, 27),
    _VRtrMplsP2mpInstRecordLabel_Type()
)
vRtrMplsP2mpInstRecordLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstRecordLabel.setStatus("current")
_VRtrMplsP2mpInstLastResigAttpt_Type = TimeStamp
_VRtrMplsP2mpInstLastResigAttpt_Object = MibTableColumn
vRtrMplsP2mpInstLastResigAttpt = _VRtrMplsP2mpInstLastResigAttpt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 25, 1, 28),
    _VRtrMplsP2mpInstLastResigAttpt_Type()
)
vRtrMplsP2mpInstLastResigAttpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstLastResigAttpt.setStatus("current")
_VRtrMplsP2mpInstMetric_Type = Unsigned32
_VRtrMplsP2mpInstMetric_Object = MibTableColumn
vRtrMplsP2mpInstMetric = _VRtrMplsP2mpInstMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 25, 1, 29),
    _VRtrMplsP2mpInstMetric_Type()
)
vRtrMplsP2mpInstMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstMetric.setStatus("current")
_VRtrMplsP2mpInstLastMBBType_Type = TmnxMplsMBBType
_VRtrMplsP2mpInstLastMBBType_Object = MibTableColumn
vRtrMplsP2mpInstLastMBBType = _VRtrMplsP2mpInstLastMBBType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 25, 1, 30),
    _VRtrMplsP2mpInstLastMBBType_Type()
)
vRtrMplsP2mpInstLastMBBType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstLastMBBType.setStatus("current")
_VRtrMplsP2mpInstLastMBBEnd_Type = TimeStamp
_VRtrMplsP2mpInstLastMBBEnd_Object = MibTableColumn
vRtrMplsP2mpInstLastMBBEnd = _VRtrMplsP2mpInstLastMBBEnd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 25, 1, 31),
    _VRtrMplsP2mpInstLastMBBEnd_Type()
)
vRtrMplsP2mpInstLastMBBEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstLastMBBEnd.setStatus("current")
_VRtrMplsP2mpInstLastMBBMetric_Type = Unsigned32
_VRtrMplsP2mpInstLastMBBMetric_Object = MibTableColumn
vRtrMplsP2mpInstLastMBBMetric = _VRtrMplsP2mpInstLastMBBMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 25, 1, 32),
    _VRtrMplsP2mpInstLastMBBMetric_Type()
)
vRtrMplsP2mpInstLastMBBMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstLastMBBMetric.setStatus("current")


class _VRtrMplsP2mpInstLastMBBState_Type(Integer32):
    """Custom type vRtrMplsP2mpInstLastMBBState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("success", 2),
          ("fail", 3))
    )


_VRtrMplsP2mpInstLastMBBState_Type.__name__ = "Integer32"
_VRtrMplsP2mpInstLastMBBState_Object = MibTableColumn
vRtrMplsP2mpInstLastMBBState = _VRtrMplsP2mpInstLastMBBState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 25, 1, 33),
    _VRtrMplsP2mpInstLastMBBState_Type()
)
vRtrMplsP2mpInstLastMBBState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstLastMBBState.setStatus("current")
_VRtrMplsP2mpInstMBBTypeInProg_Type = TmnxMplsMBBType
_VRtrMplsP2mpInstMBBTypeInProg_Object = MibTableColumn
vRtrMplsP2mpInstMBBTypeInProg = _VRtrMplsP2mpInstMBBTypeInProg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 25, 1, 34),
    _VRtrMplsP2mpInstMBBTypeInProg_Type()
)
vRtrMplsP2mpInstMBBTypeInProg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstMBBTypeInProg.setStatus("current")
_VRtrMplsP2mpInstMBBStarted_Type = TimeStamp
_VRtrMplsP2mpInstMBBStarted_Object = MibTableColumn
vRtrMplsP2mpInstMBBStarted = _VRtrMplsP2mpInstMBBStarted_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 25, 1, 35),
    _VRtrMplsP2mpInstMBBStarted_Type()
)
vRtrMplsP2mpInstMBBStarted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstMBBStarted.setStatus("current")
_VRtrMplsP2mpInstMBBNextRetry_Type = Unsigned32
_VRtrMplsP2mpInstMBBNextRetry_Object = MibTableColumn
vRtrMplsP2mpInstMBBNextRetry = _VRtrMplsP2mpInstMBBNextRetry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 25, 1, 36),
    _VRtrMplsP2mpInstMBBNextRetry_Type()
)
vRtrMplsP2mpInstMBBNextRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstMBBNextRetry.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstMBBNextRetry.setUnits("seconds")
_VRtrMplsP2mpInstMBBRetryAttpts_Type = Unsigned32
_VRtrMplsP2mpInstMBBRetryAttpts_Object = MibTableColumn
vRtrMplsP2mpInstMBBRetryAttpts = _VRtrMplsP2mpInstMBBRetryAttpts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 25, 1, 37),
    _VRtrMplsP2mpInstMBBRetryAttpts_Type()
)
vRtrMplsP2mpInstMBBRetryAttpts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstMBBRetryAttpts.setStatus("current")
_VRtrMplsP2mpInstMBBFailCode_Type = TmnxMplsLspFailCode
_VRtrMplsP2mpInstMBBFailCode_Object = MibTableColumn
vRtrMplsP2mpInstMBBFailCode = _VRtrMplsP2mpInstMBBFailCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 25, 1, 38),
    _VRtrMplsP2mpInstMBBFailCode_Type()
)
vRtrMplsP2mpInstMBBFailCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstMBBFailCode.setStatus("current")
_VRtrMplsP2mpInstMBBFailNodeType_Type = InetAddressType
_VRtrMplsP2mpInstMBBFailNodeType_Object = MibTableColumn
vRtrMplsP2mpInstMBBFailNodeType = _VRtrMplsP2mpInstMBBFailNodeType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 25, 1, 39),
    _VRtrMplsP2mpInstMBBFailNodeType_Type()
)
vRtrMplsP2mpInstMBBFailNodeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstMBBFailNodeType.setStatus("current")


class _VRtrMplsP2mpInstMBBFailNodeAddr_Type(InetAddress):
    """Custom type vRtrMplsP2mpInstMBBFailNodeAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_VRtrMplsP2mpInstMBBFailNodeAddr_Type.__name__ = "InetAddress"
_VRtrMplsP2mpInstMBBFailNodeAddr_Object = MibTableColumn
vRtrMplsP2mpInstMBBFailNodeAddr = _VRtrMplsP2mpInstMBBFailNodeAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 25, 1, 40),
    _VRtrMplsP2mpInstMBBFailNodeAddr_Type()
)
vRtrMplsP2mpInstMBBFailNodeAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstMBBFailNodeAddr.setStatus("current")
_VRtrMplsP2mpInstStatTable_Object = MibTable
vRtrMplsP2mpInstStatTable = _VRtrMplsP2mpInstStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 26)
)
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstStatTable.setStatus("current")
_VRtrMplsP2mpInstStatEntry_Object = MibTableRow
vRtrMplsP2mpInstStatEntry = _VRtrMplsP2mpInstStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 26, 1)
)
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstStatEntry.setStatus("current")
_VRtrMplsP2mpInstStatS2lChanges_Type = Counter32
_VRtrMplsP2mpInstStatS2lChanges_Object = MibTableColumn
vRtrMplsP2mpInstStatS2lChanges = _VRtrMplsP2mpInstStatS2lChanges_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 26, 1, 1),
    _VRtrMplsP2mpInstStatS2lChanges_Type()
)
vRtrMplsP2mpInstStatS2lChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstStatS2lChanges.setStatus("current")
_VRtrMplsP2mpInstStatLastS2lChange_Type = TimeInterval
_VRtrMplsP2mpInstStatLastS2lChange_Object = MibTableColumn
vRtrMplsP2mpInstStatLastS2lChange = _VRtrMplsP2mpInstStatLastS2lChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 26, 1, 2),
    _VRtrMplsP2mpInstStatLastS2lChange_Type()
)
vRtrMplsP2mpInstStatLastS2lChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstStatLastS2lChange.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstStatLastS2lChange.setUnits("10-milliseconds")
_VRtrMplsP2mpInstStatConfiguredS2ls_Type = Gauge32
_VRtrMplsP2mpInstStatConfiguredS2ls_Object = MibTableColumn
vRtrMplsP2mpInstStatConfiguredS2ls = _VRtrMplsP2mpInstStatConfiguredS2ls_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 26, 1, 3),
    _VRtrMplsP2mpInstStatConfiguredS2ls_Type()
)
vRtrMplsP2mpInstStatConfiguredS2ls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstStatConfiguredS2ls.setStatus("current")
_VRtrMplsP2mpInstStatOperationalS2ls_Type = Gauge32
_VRtrMplsP2mpInstStatOperationalS2ls_Object = MibTableColumn
vRtrMplsP2mpInstStatOperationalS2ls = _VRtrMplsP2mpInstStatOperationalS2ls_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 26, 1, 4),
    _VRtrMplsP2mpInstStatOperationalS2ls_Type()
)
vRtrMplsP2mpInstStatOperationalS2ls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstStatOperationalS2ls.setStatus("current")
_VRtrMplsP2mpInstStatLastS2lTimeUp_Type = TimeInterval
_VRtrMplsP2mpInstStatLastS2lTimeUp_Object = MibTableColumn
vRtrMplsP2mpInstStatLastS2lTimeUp = _VRtrMplsP2mpInstStatLastS2lTimeUp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 26, 1, 5),
    _VRtrMplsP2mpInstStatLastS2lTimeUp_Type()
)
vRtrMplsP2mpInstStatLastS2lTimeUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstStatLastS2lTimeUp.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstStatLastS2lTimeUp.setUnits("10-milliseconds")
_VRtrMplsP2mpInstStatLastS2lTimeDown_Type = TimeInterval
_VRtrMplsP2mpInstStatLastS2lTimeDown_Object = MibTableColumn
vRtrMplsP2mpInstStatLastS2lTimeDown = _VRtrMplsP2mpInstStatLastS2lTimeDown_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 26, 1, 6),
    _VRtrMplsP2mpInstStatLastS2lTimeDown_Type()
)
vRtrMplsP2mpInstStatLastS2lTimeDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstStatLastS2lTimeDown.setStatus("current")
_VRtrMplsP2mpInstStatTimeUp_Type = TimeInterval
_VRtrMplsP2mpInstStatTimeUp_Object = MibTableColumn
vRtrMplsP2mpInstStatTimeUp = _VRtrMplsP2mpInstStatTimeUp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 26, 1, 7),
    _VRtrMplsP2mpInstStatTimeUp_Type()
)
vRtrMplsP2mpInstStatTimeUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstStatTimeUp.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstStatTimeUp.setUnits("10-milliseconds")
_VRtrMplsP2mpInstStatTimeDown_Type = TimeInterval
_VRtrMplsP2mpInstStatTimeDown_Object = MibTableColumn
vRtrMplsP2mpInstStatTimeDown = _VRtrMplsP2mpInstStatTimeDown_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 26, 1, 8),
    _VRtrMplsP2mpInstStatTimeDown_Type()
)
vRtrMplsP2mpInstStatTimeDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstStatTimeDown.setStatus("current")
_VRtrMplsP2mpInstStatTransitions_Type = Counter32
_VRtrMplsP2mpInstStatTransitions_Object = MibTableColumn
vRtrMplsP2mpInstStatTransitions = _VRtrMplsP2mpInstStatTransitions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 26, 1, 9),
    _VRtrMplsP2mpInstStatTransitions_Type()
)
vRtrMplsP2mpInstStatTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstStatTransitions.setStatus("current")
_VRtrMplsP2mpInstStatLastTrans_Type = TimeInterval
_VRtrMplsP2mpInstStatLastTrans_Object = MibTableColumn
vRtrMplsP2mpInstStatLastTrans = _VRtrMplsP2mpInstStatLastTrans_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 26, 1, 10),
    _VRtrMplsP2mpInstStatLastTrans_Type()
)
vRtrMplsP2mpInstStatLastTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstStatLastTrans.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstStatLastTrans.setUnits("ten-milliseconds")
_VRtrMplsS2lSubLspTblLastChanged_Type = TimeStamp
_VRtrMplsS2lSubLspTblLastChanged_Object = MibScalar
vRtrMplsS2lSubLspTblLastChanged = _VRtrMplsS2lSubLspTblLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 27),
    _VRtrMplsS2lSubLspTblLastChanged_Type()
)
vRtrMplsS2lSubLspTblLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspTblLastChanged.setStatus("current")
_VRtrMplsS2lSubLspTable_Object = MibTable
vRtrMplsS2lSubLspTable = _VRtrMplsS2lSubLspTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 28)
)
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspTable.setStatus("current")
_VRtrMplsS2lSubLspEntry_Object = MibTableRow
vRtrMplsS2lSubLspEntry = _VRtrMplsS2lSubLspEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 28, 1)
)
vRtrMplsS2lSubLspEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsLspIndex"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstIndex"),
    (0, "MPLS-TE-MIB", "mplsTunnelIndex"),
    (0, "MPLS-TE-MIB", "mplsTunnelInstance"),
    (0, "MPLS-TE-MIB", "mplsTunnelIngressLSRId"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspDstAddrType"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspDstAddr"),
)
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspEntry.setStatus("current")
_VRtrMplsS2lSubLspDstAddrType_Type = InetAddressType
_VRtrMplsS2lSubLspDstAddrType_Object = MibTableColumn
vRtrMplsS2lSubLspDstAddrType = _VRtrMplsS2lSubLspDstAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 28, 1, 1),
    _VRtrMplsS2lSubLspDstAddrType_Type()
)
vRtrMplsS2lSubLspDstAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspDstAddrType.setStatus("current")


class _VRtrMplsS2lSubLspDstAddr_Type(InetAddress):
    """Custom type vRtrMplsS2lSubLspDstAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_VRtrMplsS2lSubLspDstAddr_Type.__name__ = "InetAddress"
_VRtrMplsS2lSubLspDstAddr_Object = MibTableColumn
vRtrMplsS2lSubLspDstAddr = _VRtrMplsS2lSubLspDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 28, 1, 2),
    _VRtrMplsS2lSubLspDstAddr_Type()
)
vRtrMplsS2lSubLspDstAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspDstAddr.setStatus("current")
_VRtrMplsS2lSubLspRowStatus_Type = RowStatus
_VRtrMplsS2lSubLspRowStatus_Object = MibTableColumn
vRtrMplsS2lSubLspRowStatus = _VRtrMplsS2lSubLspRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 28, 1, 3),
    _VRtrMplsS2lSubLspRowStatus_Type()
)
vRtrMplsS2lSubLspRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspRowStatus.setStatus("current")
_VRtrMplsS2lSubLspLastChange_Type = TimeStamp
_VRtrMplsS2lSubLspLastChange_Object = MibTableColumn
vRtrMplsS2lSubLspLastChange = _VRtrMplsS2lSubLspLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 28, 1, 4),
    _VRtrMplsS2lSubLspLastChange_Type()
)
vRtrMplsS2lSubLspLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspLastChange.setStatus("current")


class _VRtrMplsS2lSubLspType_Type(Integer32):
    """Custom type vRtrMplsS2lSubLspType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("s2lPath", 1)
    )


_VRtrMplsS2lSubLspType_Type.__name__ = "Integer32"
_VRtrMplsS2lSubLspType_Object = MibTableColumn
vRtrMplsS2lSubLspType = _VRtrMplsS2lSubLspType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 28, 1, 5),
    _VRtrMplsS2lSubLspType_Type()
)
vRtrMplsS2lSubLspType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspType.setStatus("current")


class _VRtrMplsS2lSubLspProperties_Type(Bits):
    """Custom type vRtrMplsS2lSubLspProperties based on Bits"""
    namedValues = NamedValues(
        *(("recordRoute", 0),
          ("adaptive", 1),
          ("cspf", 2),
          ("mergeable", 3),
          ("fastReroute", 4))
    )

_VRtrMplsS2lSubLspProperties_Type.__name__ = "Bits"
_VRtrMplsS2lSubLspProperties_Object = MibTableColumn
vRtrMplsS2lSubLspProperties = _VRtrMplsS2lSubLspProperties_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 28, 1, 6),
    _VRtrMplsS2lSubLspProperties_Type()
)
vRtrMplsS2lSubLspProperties.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspProperties.setStatus("current")


class _VRtrMplsS2lSubLspState_Type(Integer32):
    """Custom type vRtrMplsS2lSubLspState based on Integer32"""
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
        *(("unknown", 1),
          ("active", 2),
          ("inactive", 3))
    )


_VRtrMplsS2lSubLspState_Type.__name__ = "Integer32"
_VRtrMplsS2lSubLspState_Object = MibTableColumn
vRtrMplsS2lSubLspState = _VRtrMplsS2lSubLspState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 28, 1, 7),
    _VRtrMplsS2lSubLspState_Type()
)
vRtrMplsS2lSubLspState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspState.setStatus("current")


class _VRtrMplsS2lSubLspAdminState_Type(TmnxAdminState):
    """Custom type vRtrMplsS2lSubLspAdminState based on TmnxAdminState"""
    defaultValue = 2


_VRtrMplsS2lSubLspAdminState_Type.__name__ = "TmnxAdminState"
_VRtrMplsS2lSubLspAdminState_Object = MibTableColumn
vRtrMplsS2lSubLspAdminState = _VRtrMplsS2lSubLspAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 28, 1, 8),
    _VRtrMplsS2lSubLspAdminState_Type()
)
vRtrMplsS2lSubLspAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspAdminState.setStatus("current")
_VRtrMplsS2lSubLspOperState_Type = TmnxOperState
_VRtrMplsS2lSubLspOperState_Object = MibTableColumn
vRtrMplsS2lSubLspOperState = _VRtrMplsS2lSubLspOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 28, 1, 9),
    _VRtrMplsS2lSubLspOperState_Type()
)
vRtrMplsS2lSubLspOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspOperState.setStatus("current")
_VRtrMplsS2lSubGroupId_Type = Unsigned32
_VRtrMplsS2lSubGroupId_Object = MibTableColumn
vRtrMplsS2lSubGroupId = _VRtrMplsS2lSubGroupId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 28, 1, 10),
    _VRtrMplsS2lSubGroupId_Type()
)
vRtrMplsS2lSubGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubGroupId.setStatus("current")
_VRtrMplsS2lSubLspId_Type = MplsLSPID
_VRtrMplsS2lSubLspId_Object = MibTableColumn
vRtrMplsS2lSubLspId = _VRtrMplsS2lSubLspId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 28, 1, 11),
    _VRtrMplsS2lSubLspId_Type()
)
vRtrMplsS2lSubLspId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspId.setStatus("current")
_VRtrMplsS2lSubLspRetryTimeRemain_Type = Unsigned32
_VRtrMplsS2lSubLspRetryTimeRemain_Object = MibTableColumn
vRtrMplsS2lSubLspRetryTimeRemain = _VRtrMplsS2lSubLspRetryTimeRemain_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 28, 1, 12),
    _VRtrMplsS2lSubLspRetryTimeRemain_Type()
)
vRtrMplsS2lSubLspRetryTimeRemain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspRetryTimeRemain.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspRetryTimeRemain.setUnits("10-milliseconds")


class _VRtrMplsS2lSubLspTunARHopLtIndex_Type(Integer32):
    """Custom type vRtrMplsS2lSubLspTunARHopLtIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 2147483647),
    )


_VRtrMplsS2lSubLspTunARHopLtIndex_Type.__name__ = "Integer32"
_VRtrMplsS2lSubLspTunARHopLtIndex_Object = MibTableColumn
vRtrMplsS2lSubLspTunARHopLtIndex = _VRtrMplsS2lSubLspTunARHopLtIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 28, 1, 13),
    _VRtrMplsS2lSubLspTunARHopLtIndex_Type()
)
vRtrMplsS2lSubLspTunARHopLtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspTunARHopLtIndex.setStatus("current")


class _VRtrMplsS2lSubLspNegotiatedMTU_Type(Unsigned32):
    """Custom type vRtrMplsS2lSubLspNegotiatedMTU based on Unsigned32"""
    defaultValue = 0


_VRtrMplsS2lSubLspNegotiatedMTU_Type.__name__ = "Unsigned32"
_VRtrMplsS2lSubLspNegotiatedMTU_Object = MibTableColumn
vRtrMplsS2lSubLspNegotiatedMTU = _VRtrMplsS2lSubLspNegotiatedMTU_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 28, 1, 14),
    _VRtrMplsS2lSubLspNegotiatedMTU_Type()
)
vRtrMplsS2lSubLspNegotiatedMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspNegotiatedMTU.setStatus("current")
_VRtrMplsS2lSubLspFailCode_Type = TmnxMplsLspFailCode
_VRtrMplsS2lSubLspFailCode_Object = MibTableColumn
vRtrMplsS2lSubLspFailCode = _VRtrMplsS2lSubLspFailCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 28, 1, 15),
    _VRtrMplsS2lSubLspFailCode_Type()
)
vRtrMplsS2lSubLspFailCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspFailCode.setStatus("current")
_VRtrMplsS2lSubLspFailNodeArType_Type = InetAddressType
_VRtrMplsS2lSubLspFailNodeArType_Object = MibTableColumn
vRtrMplsS2lSubLspFailNodeArType = _VRtrMplsS2lSubLspFailNodeArType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 28, 1, 16),
    _VRtrMplsS2lSubLspFailNodeArType_Type()
)
vRtrMplsS2lSubLspFailNodeArType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspFailNodeArType.setStatus("current")


class _VRtrMplsS2lSubLspFailNodeAddr_Type(InetAddress):
    """Custom type vRtrMplsS2lSubLspFailNodeAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_VRtrMplsS2lSubLspFailNodeAddr_Type.__name__ = "InetAddress"
_VRtrMplsS2lSubLspFailNodeAddr_Object = MibTableColumn
vRtrMplsS2lSubLspFailNodeAddr = _VRtrMplsS2lSubLspFailNodeAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 28, 1, 17),
    _VRtrMplsS2lSubLspFailNodeAddr_Type()
)
vRtrMplsS2lSubLspFailNodeAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspFailNodeAddr.setStatus("current")
_VRtrMplsS2lSubLspOperBandwidth_Type = Integer32
_VRtrMplsS2lSubLspOperBandwidth_Object = MibTableColumn
vRtrMplsS2lSubLspOperBandwidth = _VRtrMplsS2lSubLspOperBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 28, 1, 18),
    _VRtrMplsS2lSubLspOperBandwidth_Type()
)
vRtrMplsS2lSubLspOperBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspOperBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspOperBandwidth.setUnits("mega-bits per second")


class _VRtrMplsS2lSubLspTunCRHopLtIndex_Type(Integer32):
    """Custom type vRtrMplsS2lSubLspTunCRHopLtIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 2147483647),
    )


_VRtrMplsS2lSubLspTunCRHopLtIndex_Type.__name__ = "Integer32"
_VRtrMplsS2lSubLspTunCRHopLtIndex_Object = MibTableColumn
vRtrMplsS2lSubLspTunCRHopLtIndex = _VRtrMplsS2lSubLspTunCRHopLtIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 28, 1, 19),
    _VRtrMplsS2lSubLspTunCRHopLtIndex_Type()
)
vRtrMplsS2lSubLspTunCRHopLtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspTunCRHopLtIndex.setStatus("current")
_VRtrMplsS2lSubLspOperMTU_Type = Unsigned32
_VRtrMplsS2lSubLspOperMTU_Object = MibTableColumn
vRtrMplsS2lSubLspOperMTU = _VRtrMplsS2lSubLspOperMTU_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 28, 1, 20),
    _VRtrMplsS2lSubLspOperMTU_Type()
)
vRtrMplsS2lSubLspOperMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspOperMTU.setStatus("current")
_VRtrMplsS2lSubLspLastResigAttpt_Type = TimeStamp
_VRtrMplsS2lSubLspLastResigAttpt_Object = MibTableColumn
vRtrMplsS2lSubLspLastResigAttpt = _VRtrMplsS2lSubLspLastResigAttpt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 28, 1, 21),
    _VRtrMplsS2lSubLspLastResigAttpt_Type()
)
vRtrMplsS2lSubLspLastResigAttpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspLastResigAttpt.setStatus("current")
_VRtrMplsS2lSubLspLastMBBType_Type = TmnxMplsMBBType
_VRtrMplsS2lSubLspLastMBBType_Object = MibTableColumn
vRtrMplsS2lSubLspLastMBBType = _VRtrMplsS2lSubLspLastMBBType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 28, 1, 22),
    _VRtrMplsS2lSubLspLastMBBType_Type()
)
vRtrMplsS2lSubLspLastMBBType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspLastMBBType.setStatus("current")
_VRtrMplsS2lSubLspLastMBBEnd_Type = TimeStamp
_VRtrMplsS2lSubLspLastMBBEnd_Object = MibTableColumn
vRtrMplsS2lSubLspLastMBBEnd = _VRtrMplsS2lSubLspLastMBBEnd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 28, 1, 23),
    _VRtrMplsS2lSubLspLastMBBEnd_Type()
)
vRtrMplsS2lSubLspLastMBBEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspLastMBBEnd.setStatus("current")
_VRtrMplsS2lSubLspLastMBBMetric_Type = Unsigned32
_VRtrMplsS2lSubLspLastMBBMetric_Object = MibTableColumn
vRtrMplsS2lSubLspLastMBBMetric = _VRtrMplsS2lSubLspLastMBBMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 28, 1, 24),
    _VRtrMplsS2lSubLspLastMBBMetric_Type()
)
vRtrMplsS2lSubLspLastMBBMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspLastMBBMetric.setStatus("current")


class _VRtrMplsS2lSubLspLastMBBState_Type(Integer32):
    """Custom type vRtrMplsS2lSubLspLastMBBState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("success", 2),
          ("fail", 3))
    )


_VRtrMplsS2lSubLspLastMBBState_Type.__name__ = "Integer32"
_VRtrMplsS2lSubLspLastMBBState_Object = MibTableColumn
vRtrMplsS2lSubLspLastMBBState = _VRtrMplsS2lSubLspLastMBBState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 28, 1, 25),
    _VRtrMplsS2lSubLspLastMBBState_Type()
)
vRtrMplsS2lSubLspLastMBBState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspLastMBBState.setStatus("current")
_VRtrMplsS2lSubLspMBBTypeInProg_Type = TmnxMplsMBBType
_VRtrMplsS2lSubLspMBBTypeInProg_Object = MibTableColumn
vRtrMplsS2lSubLspMBBTypeInProg = _VRtrMplsS2lSubLspMBBTypeInProg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 28, 1, 26),
    _VRtrMplsS2lSubLspMBBTypeInProg_Type()
)
vRtrMplsS2lSubLspMBBTypeInProg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspMBBTypeInProg.setStatus("current")
_VRtrMplsS2lSubLspMBBStarted_Type = TimeStamp
_VRtrMplsS2lSubLspMBBStarted_Object = MibTableColumn
vRtrMplsS2lSubLspMBBStarted = _VRtrMplsS2lSubLspMBBStarted_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 28, 1, 27),
    _VRtrMplsS2lSubLspMBBStarted_Type()
)
vRtrMplsS2lSubLspMBBStarted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspMBBStarted.setStatus("current")
_VRtrMplsS2lSubLspMBBNextRetry_Type = Unsigned32
_VRtrMplsS2lSubLspMBBNextRetry_Object = MibTableColumn
vRtrMplsS2lSubLspMBBNextRetry = _VRtrMplsS2lSubLspMBBNextRetry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 28, 1, 28),
    _VRtrMplsS2lSubLspMBBNextRetry_Type()
)
vRtrMplsS2lSubLspMBBNextRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspMBBNextRetry.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspMBBNextRetry.setUnits("seconds")
_VRtrMplsS2lSubLspMBBRetryAttpts_Type = Unsigned32
_VRtrMplsS2lSubLspMBBRetryAttpts_Object = MibTableColumn
vRtrMplsS2lSubLspMBBRetryAttpts = _VRtrMplsS2lSubLspMBBRetryAttpts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 28, 1, 29),
    _VRtrMplsS2lSubLspMBBRetryAttpts_Type()
)
vRtrMplsS2lSubLspMBBRetryAttpts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspMBBRetryAttpts.setStatus("current")
_VRtrMplsS2lSubLspMBBFailCode_Type = TmnxMplsLspFailCode
_VRtrMplsS2lSubLspMBBFailCode_Object = MibTableColumn
vRtrMplsS2lSubLspMBBFailCode = _VRtrMplsS2lSubLspMBBFailCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 28, 1, 30),
    _VRtrMplsS2lSubLspMBBFailCode_Type()
)
vRtrMplsS2lSubLspMBBFailCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspMBBFailCode.setStatus("current")
_VRtrMplsS2lSubLspMBBFailNodeType_Type = InetAddressType
_VRtrMplsS2lSubLspMBBFailNodeType_Object = MibTableColumn
vRtrMplsS2lSubLspMBBFailNodeType = _VRtrMplsS2lSubLspMBBFailNodeType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 28, 1, 31),
    _VRtrMplsS2lSubLspMBBFailNodeType_Type()
)
vRtrMplsS2lSubLspMBBFailNodeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspMBBFailNodeType.setStatus("current")


class _VRtrMplsS2lSubLspMBBFailNodeAddr_Type(InetAddress):
    """Custom type vRtrMplsS2lSubLspMBBFailNodeAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_VRtrMplsS2lSubLspMBBFailNodeAddr_Type.__name__ = "InetAddress"
_VRtrMplsS2lSubLspMBBFailNodeAddr_Object = MibTableColumn
vRtrMplsS2lSubLspMBBFailNodeAddr = _VRtrMplsS2lSubLspMBBFailNodeAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 28, 1, 32),
    _VRtrMplsS2lSubLspMBBFailNodeAddr_Type()
)
vRtrMplsS2lSubLspMBBFailNodeAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspMBBFailNodeAddr.setStatus("current")
_VRtrMplsS2lSubLspUpTime_Type = TimeStamp
_VRtrMplsS2lSubLspUpTime_Object = MibTableColumn
vRtrMplsS2lSubLspUpTime = _VRtrMplsS2lSubLspUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 28, 1, 33),
    _VRtrMplsS2lSubLspUpTime_Type()
)
vRtrMplsS2lSubLspUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspUpTime.setStatus("current")
_VRtrMplsS2lSubLspDownTime_Type = TimeStamp
_VRtrMplsS2lSubLspDownTime_Object = MibTableColumn
vRtrMplsS2lSubLspDownTime = _VRtrMplsS2lSubLspDownTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 28, 1, 34),
    _VRtrMplsS2lSubLspDownTime_Type()
)
vRtrMplsS2lSubLspDownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspDownTime.setStatus("current")
_VRtrMplsS2lSubLspIsFastRetry_Type = TruthValue
_VRtrMplsS2lSubLspIsFastRetry_Object = MibTableColumn
vRtrMplsS2lSubLspIsFastRetry = _VRtrMplsS2lSubLspIsFastRetry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 28, 1, 35),
    _VRtrMplsS2lSubLspIsFastRetry_Type()
)
vRtrMplsS2lSubLspIsFastRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspIsFastRetry.setStatus("current")
_VRtrMplsS2lSubLspTimeoutIn_Type = Unsigned32
_VRtrMplsS2lSubLspTimeoutIn_Object = MibTableColumn
vRtrMplsS2lSubLspTimeoutIn = _VRtrMplsS2lSubLspTimeoutIn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 28, 1, 36),
    _VRtrMplsS2lSubLspTimeoutIn_Type()
)
vRtrMplsS2lSubLspTimeoutIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspTimeoutIn.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspTimeoutIn.setUnits("seconds")
_VRtrMplsS2lSubLspMBBTimeoutIn_Type = Unsigned32
_VRtrMplsS2lSubLspMBBTimeoutIn_Object = MibTableColumn
vRtrMplsS2lSubLspMBBTimeoutIn = _VRtrMplsS2lSubLspMBBTimeoutIn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 28, 1, 37),
    _VRtrMplsS2lSubLspMBBTimeoutIn_Type()
)
vRtrMplsS2lSubLspMBBTimeoutIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspMBBTimeoutIn.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspMBBTimeoutIn.setUnits("seconds")
_VRtrMplsS2lSubLspInterArea_Type = TruthValue
_VRtrMplsS2lSubLspInterArea_Object = MibTableColumn
vRtrMplsS2lSubLspInterArea = _VRtrMplsS2lSubLspInterArea_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 28, 1, 38),
    _VRtrMplsS2lSubLspInterArea_Type()
)
vRtrMplsS2lSubLspInterArea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspInterArea.setStatus("current")
_VRtrMplsS2lSubLspStatTable_Object = MibTable
vRtrMplsS2lSubLspStatTable = _VRtrMplsS2lSubLspStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 29)
)
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspStatTable.setStatus("current")
_VRtrMplsS2lSubLspStatEntry_Object = MibTableRow
vRtrMplsS2lSubLspStatEntry = _VRtrMplsS2lSubLspStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 29, 1)
)
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspStatEntry.setStatus("current")
_VRtrMplsS2lSubLspTimeUp_Type = TimeInterval
_VRtrMplsS2lSubLspTimeUp_Object = MibTableColumn
vRtrMplsS2lSubLspTimeUp = _VRtrMplsS2lSubLspTimeUp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 29, 1, 1),
    _VRtrMplsS2lSubLspTimeUp_Type()
)
vRtrMplsS2lSubLspTimeUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspTimeUp.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspTimeUp.setUnits("10-milliseconds")
_VRtrMplsS2lSubLspTimeDown_Type = TimeInterval
_VRtrMplsS2lSubLspTimeDown_Object = MibTableColumn
vRtrMplsS2lSubLspTimeDown = _VRtrMplsS2lSubLspTimeDown_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 29, 1, 2),
    _VRtrMplsS2lSubLspTimeDown_Type()
)
vRtrMplsS2lSubLspTimeDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspTimeDown.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspTimeDown.setUnits("10-milliseconds")
_VRtrMplsS2lSubLspRetryAttempts_Type = Counter32
_VRtrMplsS2lSubLspRetryAttempts_Object = MibTableColumn
vRtrMplsS2lSubLspRetryAttempts = _VRtrMplsS2lSubLspRetryAttempts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 29, 1, 3),
    _VRtrMplsS2lSubLspRetryAttempts_Type()
)
vRtrMplsS2lSubLspRetryAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspRetryAttempts.setStatus("current")
_VRtrMplsS2lSubLspTransitionCount_Type = Counter32
_VRtrMplsS2lSubLspTransitionCount_Object = MibTableColumn
vRtrMplsS2lSubLspTransitionCount = _VRtrMplsS2lSubLspTransitionCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 29, 1, 4),
    _VRtrMplsS2lSubLspTransitionCount_Type()
)
vRtrMplsS2lSubLspTransitionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspTransitionCount.setStatus("current")
_VRtrMplsS2lSubLspCspfQueries_Type = Counter32
_VRtrMplsS2lSubLspCspfQueries_Object = MibTableColumn
vRtrMplsS2lSubLspCspfQueries = _VRtrMplsS2lSubLspCspfQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 29, 1, 5),
    _VRtrMplsS2lSubLspCspfQueries_Type()
)
vRtrMplsS2lSubLspCspfQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspCspfQueries.setStatus("current")
_VRtrMplsSrlgDBRtrIdTblLastChg_Type = TimeStamp
_VRtrMplsSrlgDBRtrIdTblLastChg_Object = MibScalar
vRtrMplsSrlgDBRtrIdTblLastChg = _VRtrMplsSrlgDBRtrIdTblLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 30),
    _VRtrMplsSrlgDBRtrIdTblLastChg_Type()
)
vRtrMplsSrlgDBRtrIdTblLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsSrlgDBRtrIdTblLastChg.setStatus("current")
_VRtrMplsSrlgDBRtrIdTable_Object = MibTable
vRtrMplsSrlgDBRtrIdTable = _VRtrMplsSrlgDBRtrIdTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 31)
)
if mibBuilder.loadTexts:
    vRtrMplsSrlgDBRtrIdTable.setStatus("current")
_VRtrMplsSrlgDBRtrIdEntry_Object = MibTableRow
vRtrMplsSrlgDBRtrIdEntry = _VRtrMplsSrlgDBRtrIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 31, 1)
)
vRtrMplsSrlgDBRtrIdEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsSrlgDBRtrIdRouterID"),
)
if mibBuilder.loadTexts:
    vRtrMplsSrlgDBRtrIdEntry.setStatus("current")
_VRtrMplsSrlgDBRtrIdRouterID_Type = TmnxMplsRouterId
_VRtrMplsSrlgDBRtrIdRouterID_Object = MibTableColumn
vRtrMplsSrlgDBRtrIdRouterID = _VRtrMplsSrlgDBRtrIdRouterID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 31, 1, 1),
    _VRtrMplsSrlgDBRtrIdRouterID_Type()
)
vRtrMplsSrlgDBRtrIdRouterID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsSrlgDBRtrIdRouterID.setStatus("current")
_VRtrMplsSrlgDBRtrIdRowStatus_Type = RowStatus
_VRtrMplsSrlgDBRtrIdRowStatus_Object = MibTableColumn
vRtrMplsSrlgDBRtrIdRowStatus = _VRtrMplsSrlgDBRtrIdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 31, 1, 2),
    _VRtrMplsSrlgDBRtrIdRowStatus_Type()
)
vRtrMplsSrlgDBRtrIdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsSrlgDBRtrIdRowStatus.setStatus("current")


class _VRtrMplsSrlgDBRtrIdAdminState_Type(TmnxAdminState):
    """Custom type vRtrMplsSrlgDBRtrIdAdminState based on TmnxAdminState"""
    defaultValue = 3


_VRtrMplsSrlgDBRtrIdAdminState_Type.__name__ = "TmnxAdminState"
_VRtrMplsSrlgDBRtrIdAdminState_Object = MibTableColumn
vRtrMplsSrlgDBRtrIdAdminState = _VRtrMplsSrlgDBRtrIdAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 31, 1, 3),
    _VRtrMplsSrlgDBRtrIdAdminState_Type()
)
vRtrMplsSrlgDBRtrIdAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsSrlgDBRtrIdAdminState.setStatus("current")
_VRtrMplsSrlgDBRtrIdLastChanged_Type = TimeStamp
_VRtrMplsSrlgDBRtrIdLastChanged_Object = MibTableColumn
vRtrMplsSrlgDBRtrIdLastChanged = _VRtrMplsSrlgDBRtrIdLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 31, 1, 4),
    _VRtrMplsSrlgDBRtrIdLastChanged_Type()
)
vRtrMplsSrlgDBRtrIdLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsSrlgDBRtrIdLastChanged.setStatus("current")
_VRtrMplsSrlgDBIfTblLastChanged_Type = TimeStamp
_VRtrMplsSrlgDBIfTblLastChanged_Object = MibScalar
vRtrMplsSrlgDBIfTblLastChanged = _VRtrMplsSrlgDBIfTblLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 32),
    _VRtrMplsSrlgDBIfTblLastChanged_Type()
)
vRtrMplsSrlgDBIfTblLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsSrlgDBIfTblLastChanged.setStatus("current")
_VRtrMplsSrlgDBIfTable_Object = MibTable
vRtrMplsSrlgDBIfTable = _VRtrMplsSrlgDBIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 33)
)
if mibBuilder.loadTexts:
    vRtrMplsSrlgDBIfTable.setStatus("current")
_VRtrMplsSrlgDBIfEntry_Object = MibTableRow
vRtrMplsSrlgDBIfEntry = _VRtrMplsSrlgDBIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 33, 1)
)
vRtrMplsSrlgDBIfEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsSrlgDBRtrIdRouterID"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsSrlgDBIfIntIpAddrType"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsSrlgDBIfIntIpAddr"),
    (1, "TIMETRA-MPLS-MIB", "vRtrMplsSrlgDBIfSrlgGroupName"),
)
if mibBuilder.loadTexts:
    vRtrMplsSrlgDBIfEntry.setStatus("current")
_VRtrMplsSrlgDBIfIntIpAddrType_Type = InetAddressType
_VRtrMplsSrlgDBIfIntIpAddrType_Object = MibTableColumn
vRtrMplsSrlgDBIfIntIpAddrType = _VRtrMplsSrlgDBIfIntIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 33, 1, 1),
    _VRtrMplsSrlgDBIfIntIpAddrType_Type()
)
vRtrMplsSrlgDBIfIntIpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsSrlgDBIfIntIpAddrType.setStatus("current")


class _VRtrMplsSrlgDBIfIntIpAddr_Type(InetAddress):
    """Custom type vRtrMplsSrlgDBIfIntIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_VRtrMplsSrlgDBIfIntIpAddr_Type.__name__ = "InetAddress"
_VRtrMplsSrlgDBIfIntIpAddr_Object = MibTableColumn
vRtrMplsSrlgDBIfIntIpAddr = _VRtrMplsSrlgDBIfIntIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 33, 1, 2),
    _VRtrMplsSrlgDBIfIntIpAddr_Type()
)
vRtrMplsSrlgDBIfIntIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsSrlgDBIfIntIpAddr.setStatus("current")
_VRtrMplsSrlgDBIfSrlgGroupName_Type = TNamedItem
_VRtrMplsSrlgDBIfSrlgGroupName_Object = MibTableColumn
vRtrMplsSrlgDBIfSrlgGroupName = _VRtrMplsSrlgDBIfSrlgGroupName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 33, 1, 3),
    _VRtrMplsSrlgDBIfSrlgGroupName_Type()
)
vRtrMplsSrlgDBIfSrlgGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsSrlgDBIfSrlgGroupName.setStatus("current")
_VRtrMplsSrlgDBIfRowStatus_Type = RowStatus
_VRtrMplsSrlgDBIfRowStatus_Object = MibTableColumn
vRtrMplsSrlgDBIfRowStatus = _VRtrMplsSrlgDBIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 33, 1, 4),
    _VRtrMplsSrlgDBIfRowStatus_Type()
)
vRtrMplsSrlgDBIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsSrlgDBIfRowStatus.setStatus("current")
_VRtrMplsSrlgDBIfLastChanged_Type = TimeStamp
_VRtrMplsSrlgDBIfLastChanged_Object = MibTableColumn
vRtrMplsSrlgDBIfLastChanged = _VRtrMplsSrlgDBIfLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 33, 1, 5),
    _VRtrMplsSrlgDBIfLastChanged_Type()
)
vRtrMplsSrlgDBIfLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsSrlgDBIfLastChanged.setStatus("current")
_VRtrMplsInSegmentTable_Object = MibTable
vRtrMplsInSegmentTable = _VRtrMplsInSegmentTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 34)
)
if mibBuilder.loadTexts:
    vRtrMplsInSegmentTable.setStatus("current")
_VRtrMplsInSegmentEntry_Object = MibTableRow
vRtrMplsInSegmentEntry = _VRtrMplsInSegmentEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 34, 1)
)
if mibBuilder.loadTexts:
    vRtrMplsInSegmentEntry.setStatus("current")
_VRtrMplsInSegmentNumS2ls_Type = Unsigned32
_VRtrMplsInSegmentNumS2ls_Object = MibTableColumn
vRtrMplsInSegmentNumS2ls = _VRtrMplsInSegmentNumS2ls_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 34, 1, 1),
    _VRtrMplsInSegmentNumS2ls_Type()
)
vRtrMplsInSegmentNumS2ls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInSegmentNumS2ls.setStatus("current")
_VRtrMplsOutSegmentTable_Object = MibTable
vRtrMplsOutSegmentTable = _VRtrMplsOutSegmentTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 35)
)
if mibBuilder.loadTexts:
    vRtrMplsOutSegmentTable.setStatus("current")
_VRtrMplsOutSegmentEntry_Object = MibTableRow
vRtrMplsOutSegmentEntry = _VRtrMplsOutSegmentEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 35, 1)
)
if mibBuilder.loadTexts:
    vRtrMplsOutSegmentEntry.setStatus("current")
_VRtrMplsOutSegmentNumS2ls_Type = Unsigned32
_VRtrMplsOutSegmentNumS2ls_Object = MibTableColumn
vRtrMplsOutSegmentNumS2ls = _VRtrMplsOutSegmentNumS2ls_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 35, 1, 1),
    _VRtrMplsOutSegmentNumS2ls_Type()
)
vRtrMplsOutSegmentNumS2ls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsOutSegmentNumS2ls.setStatus("current")
_VRtrMplsLspStatsTblLastChgd_Type = TimeStamp
_VRtrMplsLspStatsTblLastChgd_Object = MibScalar
vRtrMplsLspStatsTblLastChgd = _VRtrMplsLspStatsTblLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 37),
    _VRtrMplsLspStatsTblLastChgd_Type()
)
vRtrMplsLspStatsTblLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspStatsTblLastChgd.setStatus("current")
_VRtrMplsLspStatsTable_Object = MibTable
vRtrMplsLspStatsTable = _VRtrMplsLspStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 38)
)
if mibBuilder.loadTexts:
    vRtrMplsLspStatsTable.setStatus("current")
_VRtrMplsLspStatsEntry_Object = MibTableRow
vRtrMplsLspStatsEntry = _VRtrMplsLspStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 38, 1)
)
vRtrMplsLspStatsEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsLspStatsType"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsLspStatsSenderAddrType"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsLspStatsSenderAddr"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsLspStatsLspName"),
)
if mibBuilder.loadTexts:
    vRtrMplsLspStatsEntry.setStatus("current")


class _VRtrMplsLspStatsType_Type(Integer32):
    """Custom type vRtrMplsLspStatsType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("egress", 0),
          ("ingress", 1))
    )


_VRtrMplsLspStatsType_Type.__name__ = "Integer32"
_VRtrMplsLspStatsType_Object = MibTableColumn
vRtrMplsLspStatsType = _VRtrMplsLspStatsType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 38, 1, 1),
    _VRtrMplsLspStatsType_Type()
)
vRtrMplsLspStatsType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsLspStatsType.setStatus("current")
_VRtrMplsLspStatsSenderAddrType_Type = InetAddressType
_VRtrMplsLspStatsSenderAddrType_Object = MibTableColumn
vRtrMplsLspStatsSenderAddrType = _VRtrMplsLspStatsSenderAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 38, 1, 2),
    _VRtrMplsLspStatsSenderAddrType_Type()
)
vRtrMplsLspStatsSenderAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsLspStatsSenderAddrType.setStatus("current")


class _VRtrMplsLspStatsSenderAddr_Type(InetAddress):
    """Custom type vRtrMplsLspStatsSenderAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrMplsLspStatsSenderAddr_Type.__name__ = "InetAddress"
_VRtrMplsLspStatsSenderAddr_Object = MibTableColumn
vRtrMplsLspStatsSenderAddr = _VRtrMplsLspStatsSenderAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 38, 1, 3),
    _VRtrMplsLspStatsSenderAddr_Type()
)
vRtrMplsLspStatsSenderAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsLspStatsSenderAddr.setStatus("current")
_VRtrMplsLspStatsLspName_Type = TLNamedItem
_VRtrMplsLspStatsLspName_Object = MibTableColumn
vRtrMplsLspStatsLspName = _VRtrMplsLspStatsLspName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 38, 1, 4),
    _VRtrMplsLspStatsLspName_Type()
)
vRtrMplsLspStatsLspName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsLspStatsLspName.setStatus("current")
_VRtrMplsLspStatsRowStatus_Type = RowStatus
_VRtrMplsLspStatsRowStatus_Object = MibTableColumn
vRtrMplsLspStatsRowStatus = _VRtrMplsLspStatsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 38, 1, 5),
    _VRtrMplsLspStatsRowStatus_Type()
)
vRtrMplsLspStatsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspStatsRowStatus.setStatus("current")
_VRtrMplsLspStatsLastChanged_Type = TimeStamp
_VRtrMplsLspStatsLastChanged_Object = MibTableColumn
vRtrMplsLspStatsLastChanged = _VRtrMplsLspStatsLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 38, 1, 6),
    _VRtrMplsLspStatsLastChanged_Type()
)
vRtrMplsLspStatsLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspStatsLastChanged.setStatus("current")


class _VRtrMplsLspStatsCollectStats_Type(TruthValue):
    """Custom type vRtrMplsLspStatsCollectStats based on TruthValue"""
    defaultValue = 2


_VRtrMplsLspStatsCollectStats_Type.__name__ = "TruthValue"
_VRtrMplsLspStatsCollectStats_Object = MibTableColumn
vRtrMplsLspStatsCollectStats = _VRtrMplsLspStatsCollectStats_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 38, 1, 7),
    _VRtrMplsLspStatsCollectStats_Type()
)
vRtrMplsLspStatsCollectStats.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspStatsCollectStats.setStatus("current")


class _VRtrMplsLspStatsAccntingPolicy_Type(Unsigned32):
    """Custom type vRtrMplsLspStatsAccntingPolicy based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 99),
    )


_VRtrMplsLspStatsAccntingPolicy_Type.__name__ = "Unsigned32"
_VRtrMplsLspStatsAccntingPolicy_Object = MibTableColumn
vRtrMplsLspStatsAccntingPolicy = _VRtrMplsLspStatsAccntingPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 38, 1, 8),
    _VRtrMplsLspStatsAccntingPolicy_Type()
)
vRtrMplsLspStatsAccntingPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspStatsAccntingPolicy.setStatus("current")


class _VRtrMplsLspStatsAdminState_Type(TmnxAdminState):
    """Custom type vRtrMplsLspStatsAdminState based on TmnxAdminState"""
    defaultValue = 3


_VRtrMplsLspStatsAdminState_Type.__name__ = "TmnxAdminState"
_VRtrMplsLspStatsAdminState_Object = MibTableColumn
vRtrMplsLspStatsAdminState = _VRtrMplsLspStatsAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 38, 1, 9),
    _VRtrMplsLspStatsAdminState_Type()
)
vRtrMplsLspStatsAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspStatsAdminState.setStatus("current")
_VRtrMplsLspStatisticsTable_Object = MibTable
vRtrMplsLspStatisticsTable = _VRtrMplsLspStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39)
)
if mibBuilder.loadTexts:
    vRtrMplsLspStatisticsTable.setStatus("current")
_VRtrMplsLspStatisticsEntry_Object = MibTableRow
vRtrMplsLspStatisticsEntry = _VRtrMplsLspStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1)
)
if mibBuilder.loadTexts:
    vRtrMplsLspStatisticsEntry.setStatus("current")
_VRtrMplsInProfilePktsFc0_Type = Counter64
_VRtrMplsInProfilePktsFc0_Object = MibTableColumn
vRtrMplsInProfilePktsFc0 = _VRtrMplsInProfilePktsFc0_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 1),
    _VRtrMplsInProfilePktsFc0_Type()
)
vRtrMplsInProfilePktsFc0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInProfilePktsFc0.setStatus("current")
_VRtrMplsInProfilePktsFc0Low32_Type = Counter32
_VRtrMplsInProfilePktsFc0Low32_Object = MibTableColumn
vRtrMplsInProfilePktsFc0Low32 = _VRtrMplsInProfilePktsFc0Low32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 2),
    _VRtrMplsInProfilePktsFc0Low32_Type()
)
vRtrMplsInProfilePktsFc0Low32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInProfilePktsFc0Low32.setStatus("current")
_VRtrMplsInProfilePktsFc0High32_Type = Counter32
_VRtrMplsInProfilePktsFc0High32_Object = MibTableColumn
vRtrMplsInProfilePktsFc0High32 = _VRtrMplsInProfilePktsFc0High32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 3),
    _VRtrMplsInProfilePktsFc0High32_Type()
)
vRtrMplsInProfilePktsFc0High32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInProfilePktsFc0High32.setStatus("current")
_VRtrMplsInProfilePktsFc1_Type = Counter64
_VRtrMplsInProfilePktsFc1_Object = MibTableColumn
vRtrMplsInProfilePktsFc1 = _VRtrMplsInProfilePktsFc1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 4),
    _VRtrMplsInProfilePktsFc1_Type()
)
vRtrMplsInProfilePktsFc1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInProfilePktsFc1.setStatus("current")
_VRtrMplsInProfilePktsFc1Low32_Type = Counter32
_VRtrMplsInProfilePktsFc1Low32_Object = MibTableColumn
vRtrMplsInProfilePktsFc1Low32 = _VRtrMplsInProfilePktsFc1Low32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 5),
    _VRtrMplsInProfilePktsFc1Low32_Type()
)
vRtrMplsInProfilePktsFc1Low32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInProfilePktsFc1Low32.setStatus("current")
_VRtrMplsInProfilePktsFc1High32_Type = Counter32
_VRtrMplsInProfilePktsFc1High32_Object = MibTableColumn
vRtrMplsInProfilePktsFc1High32 = _VRtrMplsInProfilePktsFc1High32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 6),
    _VRtrMplsInProfilePktsFc1High32_Type()
)
vRtrMplsInProfilePktsFc1High32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInProfilePktsFc1High32.setStatus("current")
_VRtrMplsInProfilePktsFc2_Type = Counter64
_VRtrMplsInProfilePktsFc2_Object = MibTableColumn
vRtrMplsInProfilePktsFc2 = _VRtrMplsInProfilePktsFc2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 7),
    _VRtrMplsInProfilePktsFc2_Type()
)
vRtrMplsInProfilePktsFc2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInProfilePktsFc2.setStatus("current")
_VRtrMplsInProfilePktsFc2Low32_Type = Counter32
_VRtrMplsInProfilePktsFc2Low32_Object = MibTableColumn
vRtrMplsInProfilePktsFc2Low32 = _VRtrMplsInProfilePktsFc2Low32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 8),
    _VRtrMplsInProfilePktsFc2Low32_Type()
)
vRtrMplsInProfilePktsFc2Low32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInProfilePktsFc2Low32.setStatus("current")
_VRtrMplsInProfilePktsFc2High32_Type = Counter32
_VRtrMplsInProfilePktsFc2High32_Object = MibTableColumn
vRtrMplsInProfilePktsFc2High32 = _VRtrMplsInProfilePktsFc2High32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 9),
    _VRtrMplsInProfilePktsFc2High32_Type()
)
vRtrMplsInProfilePktsFc2High32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInProfilePktsFc2High32.setStatus("current")
_VRtrMplsInProfilePktsFc3_Type = Counter64
_VRtrMplsInProfilePktsFc3_Object = MibTableColumn
vRtrMplsInProfilePktsFc3 = _VRtrMplsInProfilePktsFc3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 10),
    _VRtrMplsInProfilePktsFc3_Type()
)
vRtrMplsInProfilePktsFc3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInProfilePktsFc3.setStatus("current")
_VRtrMplsInProfilePktsFc3Low32_Type = Counter32
_VRtrMplsInProfilePktsFc3Low32_Object = MibTableColumn
vRtrMplsInProfilePktsFc3Low32 = _VRtrMplsInProfilePktsFc3Low32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 11),
    _VRtrMplsInProfilePktsFc3Low32_Type()
)
vRtrMplsInProfilePktsFc3Low32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInProfilePktsFc3Low32.setStatus("current")
_VRtrMplsInProfilePktsFc3High32_Type = Counter32
_VRtrMplsInProfilePktsFc3High32_Object = MibTableColumn
vRtrMplsInProfilePktsFc3High32 = _VRtrMplsInProfilePktsFc3High32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 12),
    _VRtrMplsInProfilePktsFc3High32_Type()
)
vRtrMplsInProfilePktsFc3High32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInProfilePktsFc3High32.setStatus("current")
_VRtrMplsInProfilePktsFc4_Type = Counter64
_VRtrMplsInProfilePktsFc4_Object = MibTableColumn
vRtrMplsInProfilePktsFc4 = _VRtrMplsInProfilePktsFc4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 13),
    _VRtrMplsInProfilePktsFc4_Type()
)
vRtrMplsInProfilePktsFc4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInProfilePktsFc4.setStatus("current")
_VRtrMplsInProfilePktsFc4Low32_Type = Counter32
_VRtrMplsInProfilePktsFc4Low32_Object = MibTableColumn
vRtrMplsInProfilePktsFc4Low32 = _VRtrMplsInProfilePktsFc4Low32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 14),
    _VRtrMplsInProfilePktsFc4Low32_Type()
)
vRtrMplsInProfilePktsFc4Low32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInProfilePktsFc4Low32.setStatus("current")
_VRtrMplsInProfilePktsFc4High32_Type = Counter32
_VRtrMplsInProfilePktsFc4High32_Object = MibTableColumn
vRtrMplsInProfilePktsFc4High32 = _VRtrMplsInProfilePktsFc4High32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 15),
    _VRtrMplsInProfilePktsFc4High32_Type()
)
vRtrMplsInProfilePktsFc4High32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInProfilePktsFc4High32.setStatus("current")
_VRtrMplsInProfilePktsFc5_Type = Counter64
_VRtrMplsInProfilePktsFc5_Object = MibTableColumn
vRtrMplsInProfilePktsFc5 = _VRtrMplsInProfilePktsFc5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 16),
    _VRtrMplsInProfilePktsFc5_Type()
)
vRtrMplsInProfilePktsFc5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInProfilePktsFc5.setStatus("current")
_VRtrMplsInProfilePktsFc5Low32_Type = Counter32
_VRtrMplsInProfilePktsFc5Low32_Object = MibTableColumn
vRtrMplsInProfilePktsFc5Low32 = _VRtrMplsInProfilePktsFc5Low32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 17),
    _VRtrMplsInProfilePktsFc5Low32_Type()
)
vRtrMplsInProfilePktsFc5Low32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInProfilePktsFc5Low32.setStatus("current")
_VRtrMplsInProfilePktsFc5High32_Type = Counter32
_VRtrMplsInProfilePktsFc5High32_Object = MibTableColumn
vRtrMplsInProfilePktsFc5High32 = _VRtrMplsInProfilePktsFc5High32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 18),
    _VRtrMplsInProfilePktsFc5High32_Type()
)
vRtrMplsInProfilePktsFc5High32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInProfilePktsFc5High32.setStatus("current")
_VRtrMplsInProfilePktsFc6_Type = Counter64
_VRtrMplsInProfilePktsFc6_Object = MibTableColumn
vRtrMplsInProfilePktsFc6 = _VRtrMplsInProfilePktsFc6_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 19),
    _VRtrMplsInProfilePktsFc6_Type()
)
vRtrMplsInProfilePktsFc6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInProfilePktsFc6.setStatus("current")
_VRtrMplsInProfilePktsFc6Low32_Type = Counter32
_VRtrMplsInProfilePktsFc6Low32_Object = MibTableColumn
vRtrMplsInProfilePktsFc6Low32 = _VRtrMplsInProfilePktsFc6Low32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 20),
    _VRtrMplsInProfilePktsFc6Low32_Type()
)
vRtrMplsInProfilePktsFc6Low32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInProfilePktsFc6Low32.setStatus("current")
_VRtrMplsInProfilePktsFc6High32_Type = Counter32
_VRtrMplsInProfilePktsFc6High32_Object = MibTableColumn
vRtrMplsInProfilePktsFc6High32 = _VRtrMplsInProfilePktsFc6High32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 21),
    _VRtrMplsInProfilePktsFc6High32_Type()
)
vRtrMplsInProfilePktsFc6High32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInProfilePktsFc6High32.setStatus("current")
_VRtrMplsInProfilePktsFc7_Type = Counter64
_VRtrMplsInProfilePktsFc7_Object = MibTableColumn
vRtrMplsInProfilePktsFc7 = _VRtrMplsInProfilePktsFc7_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 22),
    _VRtrMplsInProfilePktsFc7_Type()
)
vRtrMplsInProfilePktsFc7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInProfilePktsFc7.setStatus("current")
_VRtrMplsInProfilePktsFc7Low32_Type = Counter32
_VRtrMplsInProfilePktsFc7Low32_Object = MibTableColumn
vRtrMplsInProfilePktsFc7Low32 = _VRtrMplsInProfilePktsFc7Low32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 23),
    _VRtrMplsInProfilePktsFc7Low32_Type()
)
vRtrMplsInProfilePktsFc7Low32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInProfilePktsFc7Low32.setStatus("current")
_VRtrMplsInProfilePktsFc7High32_Type = Counter32
_VRtrMplsInProfilePktsFc7High32_Object = MibTableColumn
vRtrMplsInProfilePktsFc7High32 = _VRtrMplsInProfilePktsFc7High32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 24),
    _VRtrMplsInProfilePktsFc7High32_Type()
)
vRtrMplsInProfilePktsFc7High32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInProfilePktsFc7High32.setStatus("current")
_VRtrMplsInProfileOctetsFc0_Type = Counter64
_VRtrMplsInProfileOctetsFc0_Object = MibTableColumn
vRtrMplsInProfileOctetsFc0 = _VRtrMplsInProfileOctetsFc0_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 25),
    _VRtrMplsInProfileOctetsFc0_Type()
)
vRtrMplsInProfileOctetsFc0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInProfileOctetsFc0.setStatus("current")
_VRtrMplsInProfileOctetsFc0Low32_Type = Counter32
_VRtrMplsInProfileOctetsFc0Low32_Object = MibTableColumn
vRtrMplsInProfileOctetsFc0Low32 = _VRtrMplsInProfileOctetsFc0Low32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 26),
    _VRtrMplsInProfileOctetsFc0Low32_Type()
)
vRtrMplsInProfileOctetsFc0Low32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInProfileOctetsFc0Low32.setStatus("current")
_VRtrMplsInProfileOctetsFc0High32_Type = Counter32
_VRtrMplsInProfileOctetsFc0High32_Object = MibTableColumn
vRtrMplsInProfileOctetsFc0High32 = _VRtrMplsInProfileOctetsFc0High32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 27),
    _VRtrMplsInProfileOctetsFc0High32_Type()
)
vRtrMplsInProfileOctetsFc0High32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInProfileOctetsFc0High32.setStatus("current")
_VRtrMplsInProfileOctetsFc1_Type = Counter64
_VRtrMplsInProfileOctetsFc1_Object = MibTableColumn
vRtrMplsInProfileOctetsFc1 = _VRtrMplsInProfileOctetsFc1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 28),
    _VRtrMplsInProfileOctetsFc1_Type()
)
vRtrMplsInProfileOctetsFc1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInProfileOctetsFc1.setStatus("current")
_VRtrMplsInProfileOctetsFc1Low32_Type = Counter32
_VRtrMplsInProfileOctetsFc1Low32_Object = MibTableColumn
vRtrMplsInProfileOctetsFc1Low32 = _VRtrMplsInProfileOctetsFc1Low32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 29),
    _VRtrMplsInProfileOctetsFc1Low32_Type()
)
vRtrMplsInProfileOctetsFc1Low32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInProfileOctetsFc1Low32.setStatus("current")
_VRtrMplsInProfileOctetsFc1High32_Type = Counter32
_VRtrMplsInProfileOctetsFc1High32_Object = MibTableColumn
vRtrMplsInProfileOctetsFc1High32 = _VRtrMplsInProfileOctetsFc1High32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 30),
    _VRtrMplsInProfileOctetsFc1High32_Type()
)
vRtrMplsInProfileOctetsFc1High32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInProfileOctetsFc1High32.setStatus("current")
_VRtrMplsInProfileOctetsFc2_Type = Counter64
_VRtrMplsInProfileOctetsFc2_Object = MibTableColumn
vRtrMplsInProfileOctetsFc2 = _VRtrMplsInProfileOctetsFc2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 31),
    _VRtrMplsInProfileOctetsFc2_Type()
)
vRtrMplsInProfileOctetsFc2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInProfileOctetsFc2.setStatus("current")
_VRtrMplsInProfileOctetsFc2Low32_Type = Counter32
_VRtrMplsInProfileOctetsFc2Low32_Object = MibTableColumn
vRtrMplsInProfileOctetsFc2Low32 = _VRtrMplsInProfileOctetsFc2Low32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 32),
    _VRtrMplsInProfileOctetsFc2Low32_Type()
)
vRtrMplsInProfileOctetsFc2Low32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInProfileOctetsFc2Low32.setStatus("current")
_VRtrMplsInProfileOctetsFc2High32_Type = Counter32
_VRtrMplsInProfileOctetsFc2High32_Object = MibTableColumn
vRtrMplsInProfileOctetsFc2High32 = _VRtrMplsInProfileOctetsFc2High32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 33),
    _VRtrMplsInProfileOctetsFc2High32_Type()
)
vRtrMplsInProfileOctetsFc2High32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInProfileOctetsFc2High32.setStatus("current")
_VRtrMplsInProfileOctetsFc3_Type = Counter64
_VRtrMplsInProfileOctetsFc3_Object = MibTableColumn
vRtrMplsInProfileOctetsFc3 = _VRtrMplsInProfileOctetsFc3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 34),
    _VRtrMplsInProfileOctetsFc3_Type()
)
vRtrMplsInProfileOctetsFc3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInProfileOctetsFc3.setStatus("current")
_VRtrMplsInProfileOctetsFc3Low32_Type = Counter32
_VRtrMplsInProfileOctetsFc3Low32_Object = MibTableColumn
vRtrMplsInProfileOctetsFc3Low32 = _VRtrMplsInProfileOctetsFc3Low32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 35),
    _VRtrMplsInProfileOctetsFc3Low32_Type()
)
vRtrMplsInProfileOctetsFc3Low32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInProfileOctetsFc3Low32.setStatus("current")
_VRtrMplsInProfileOctetsFc3High32_Type = Counter32
_VRtrMplsInProfileOctetsFc3High32_Object = MibTableColumn
vRtrMplsInProfileOctetsFc3High32 = _VRtrMplsInProfileOctetsFc3High32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 36),
    _VRtrMplsInProfileOctetsFc3High32_Type()
)
vRtrMplsInProfileOctetsFc3High32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInProfileOctetsFc3High32.setStatus("current")
_VRtrMplsInProfileOctetsFc4_Type = Counter64
_VRtrMplsInProfileOctetsFc4_Object = MibTableColumn
vRtrMplsInProfileOctetsFc4 = _VRtrMplsInProfileOctetsFc4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 37),
    _VRtrMplsInProfileOctetsFc4_Type()
)
vRtrMplsInProfileOctetsFc4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInProfileOctetsFc4.setStatus("current")
_VRtrMplsInProfileOctetsFc4Low32_Type = Counter32
_VRtrMplsInProfileOctetsFc4Low32_Object = MibTableColumn
vRtrMplsInProfileOctetsFc4Low32 = _VRtrMplsInProfileOctetsFc4Low32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 38),
    _VRtrMplsInProfileOctetsFc4Low32_Type()
)
vRtrMplsInProfileOctetsFc4Low32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInProfileOctetsFc4Low32.setStatus("current")
_VRtrMplsInProfileOctetsFc4High32_Type = Counter32
_VRtrMplsInProfileOctetsFc4High32_Object = MibTableColumn
vRtrMplsInProfileOctetsFc4High32 = _VRtrMplsInProfileOctetsFc4High32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 39),
    _VRtrMplsInProfileOctetsFc4High32_Type()
)
vRtrMplsInProfileOctetsFc4High32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInProfileOctetsFc4High32.setStatus("current")
_VRtrMplsInProfileOctetsFc5_Type = Counter64
_VRtrMplsInProfileOctetsFc5_Object = MibTableColumn
vRtrMplsInProfileOctetsFc5 = _VRtrMplsInProfileOctetsFc5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 40),
    _VRtrMplsInProfileOctetsFc5_Type()
)
vRtrMplsInProfileOctetsFc5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInProfileOctetsFc5.setStatus("current")
_VRtrMplsInProfileOctetsFc5Low32_Type = Counter32
_VRtrMplsInProfileOctetsFc5Low32_Object = MibTableColumn
vRtrMplsInProfileOctetsFc5Low32 = _VRtrMplsInProfileOctetsFc5Low32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 41),
    _VRtrMplsInProfileOctetsFc5Low32_Type()
)
vRtrMplsInProfileOctetsFc5Low32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInProfileOctetsFc5Low32.setStatus("current")
_VRtrMplsInProfileOctetsFc5High32_Type = Counter32
_VRtrMplsInProfileOctetsFc5High32_Object = MibTableColumn
vRtrMplsInProfileOctetsFc5High32 = _VRtrMplsInProfileOctetsFc5High32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 42),
    _VRtrMplsInProfileOctetsFc5High32_Type()
)
vRtrMplsInProfileOctetsFc5High32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInProfileOctetsFc5High32.setStatus("current")
_VRtrMplsInProfileOctetsFc6_Type = Counter64
_VRtrMplsInProfileOctetsFc6_Object = MibTableColumn
vRtrMplsInProfileOctetsFc6 = _VRtrMplsInProfileOctetsFc6_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 43),
    _VRtrMplsInProfileOctetsFc6_Type()
)
vRtrMplsInProfileOctetsFc6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInProfileOctetsFc6.setStatus("current")
_VRtrMplsInProfileOctetsFc6Low32_Type = Counter32
_VRtrMplsInProfileOctetsFc6Low32_Object = MibTableColumn
vRtrMplsInProfileOctetsFc6Low32 = _VRtrMplsInProfileOctetsFc6Low32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 44),
    _VRtrMplsInProfileOctetsFc6Low32_Type()
)
vRtrMplsInProfileOctetsFc6Low32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInProfileOctetsFc6Low32.setStatus("current")
_VRtrMplsInProfileOctetsFc6High32_Type = Counter32
_VRtrMplsInProfileOctetsFc6High32_Object = MibTableColumn
vRtrMplsInProfileOctetsFc6High32 = _VRtrMplsInProfileOctetsFc6High32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 45),
    _VRtrMplsInProfileOctetsFc6High32_Type()
)
vRtrMplsInProfileOctetsFc6High32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInProfileOctetsFc6High32.setStatus("current")
_VRtrMplsInProfileOctetsFc7_Type = Counter64
_VRtrMplsInProfileOctetsFc7_Object = MibTableColumn
vRtrMplsInProfileOctetsFc7 = _VRtrMplsInProfileOctetsFc7_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 46),
    _VRtrMplsInProfileOctetsFc7_Type()
)
vRtrMplsInProfileOctetsFc7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInProfileOctetsFc7.setStatus("current")
_VRtrMplsInProfileOctetsFc7Low32_Type = Counter32
_VRtrMplsInProfileOctetsFc7Low32_Object = MibTableColumn
vRtrMplsInProfileOctetsFc7Low32 = _VRtrMplsInProfileOctetsFc7Low32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 47),
    _VRtrMplsInProfileOctetsFc7Low32_Type()
)
vRtrMplsInProfileOctetsFc7Low32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInProfileOctetsFc7Low32.setStatus("current")
_VRtrMplsInProfileOctetsFc7High32_Type = Counter32
_VRtrMplsInProfileOctetsFc7High32_Object = MibTableColumn
vRtrMplsInProfileOctetsFc7High32 = _VRtrMplsInProfileOctetsFc7High32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 48),
    _VRtrMplsInProfileOctetsFc7High32_Type()
)
vRtrMplsInProfileOctetsFc7High32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInProfileOctetsFc7High32.setStatus("current")
_VRtrMplsOutOfProfPktsFc0_Type = Counter64
_VRtrMplsOutOfProfPktsFc0_Object = MibTableColumn
vRtrMplsOutOfProfPktsFc0 = _VRtrMplsOutOfProfPktsFc0_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 49),
    _VRtrMplsOutOfProfPktsFc0_Type()
)
vRtrMplsOutOfProfPktsFc0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsOutOfProfPktsFc0.setStatus("current")
_VRtrMplsOutOfProfPktsFc0Low32_Type = Counter32
_VRtrMplsOutOfProfPktsFc0Low32_Object = MibTableColumn
vRtrMplsOutOfProfPktsFc0Low32 = _VRtrMplsOutOfProfPktsFc0Low32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 50),
    _VRtrMplsOutOfProfPktsFc0Low32_Type()
)
vRtrMplsOutOfProfPktsFc0Low32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsOutOfProfPktsFc0Low32.setStatus("current")
_VRtrMplsOutOfProfPktsFc0High32_Type = Counter32
_VRtrMplsOutOfProfPktsFc0High32_Object = MibTableColumn
vRtrMplsOutOfProfPktsFc0High32 = _VRtrMplsOutOfProfPktsFc0High32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 51),
    _VRtrMplsOutOfProfPktsFc0High32_Type()
)
vRtrMplsOutOfProfPktsFc0High32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsOutOfProfPktsFc0High32.setStatus("current")
_VRtrMplsOutOfProfPktsFc1_Type = Counter64
_VRtrMplsOutOfProfPktsFc1_Object = MibTableColumn
vRtrMplsOutOfProfPktsFc1 = _VRtrMplsOutOfProfPktsFc1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 52),
    _VRtrMplsOutOfProfPktsFc1_Type()
)
vRtrMplsOutOfProfPktsFc1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsOutOfProfPktsFc1.setStatus("current")
_VRtrMplsOutOfProfPktsFc1Low32_Type = Counter32
_VRtrMplsOutOfProfPktsFc1Low32_Object = MibTableColumn
vRtrMplsOutOfProfPktsFc1Low32 = _VRtrMplsOutOfProfPktsFc1Low32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 53),
    _VRtrMplsOutOfProfPktsFc1Low32_Type()
)
vRtrMplsOutOfProfPktsFc1Low32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsOutOfProfPktsFc1Low32.setStatus("current")
_VRtrMplsOutOfProfPktsFc1High32_Type = Counter32
_VRtrMplsOutOfProfPktsFc1High32_Object = MibTableColumn
vRtrMplsOutOfProfPktsFc1High32 = _VRtrMplsOutOfProfPktsFc1High32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 54),
    _VRtrMplsOutOfProfPktsFc1High32_Type()
)
vRtrMplsOutOfProfPktsFc1High32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsOutOfProfPktsFc1High32.setStatus("current")
_VRtrMplsOutOfProfPktsFc2_Type = Counter64
_VRtrMplsOutOfProfPktsFc2_Object = MibTableColumn
vRtrMplsOutOfProfPktsFc2 = _VRtrMplsOutOfProfPktsFc2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 55),
    _VRtrMplsOutOfProfPktsFc2_Type()
)
vRtrMplsOutOfProfPktsFc2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsOutOfProfPktsFc2.setStatus("current")
_VRtrMplsOutOfProfPktsFc2Low32_Type = Counter32
_VRtrMplsOutOfProfPktsFc2Low32_Object = MibTableColumn
vRtrMplsOutOfProfPktsFc2Low32 = _VRtrMplsOutOfProfPktsFc2Low32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 56),
    _VRtrMplsOutOfProfPktsFc2Low32_Type()
)
vRtrMplsOutOfProfPktsFc2Low32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsOutOfProfPktsFc2Low32.setStatus("current")
_VRtrMplsOutOfProfPktsFc2High32_Type = Counter32
_VRtrMplsOutOfProfPktsFc2High32_Object = MibTableColumn
vRtrMplsOutOfProfPktsFc2High32 = _VRtrMplsOutOfProfPktsFc2High32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 57),
    _VRtrMplsOutOfProfPktsFc2High32_Type()
)
vRtrMplsOutOfProfPktsFc2High32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsOutOfProfPktsFc2High32.setStatus("current")
_VRtrMplsOutOfProfPktsFc3_Type = Counter64
_VRtrMplsOutOfProfPktsFc3_Object = MibTableColumn
vRtrMplsOutOfProfPktsFc3 = _VRtrMplsOutOfProfPktsFc3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 58),
    _VRtrMplsOutOfProfPktsFc3_Type()
)
vRtrMplsOutOfProfPktsFc3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsOutOfProfPktsFc3.setStatus("current")
_VRtrMplsOutOfProfPktsFc3Low32_Type = Counter32
_VRtrMplsOutOfProfPktsFc3Low32_Object = MibTableColumn
vRtrMplsOutOfProfPktsFc3Low32 = _VRtrMplsOutOfProfPktsFc3Low32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 59),
    _VRtrMplsOutOfProfPktsFc3Low32_Type()
)
vRtrMplsOutOfProfPktsFc3Low32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsOutOfProfPktsFc3Low32.setStatus("current")
_VRtrMplsOutOfProfPktsFc3High32_Type = Counter32
_VRtrMplsOutOfProfPktsFc3High32_Object = MibTableColumn
vRtrMplsOutOfProfPktsFc3High32 = _VRtrMplsOutOfProfPktsFc3High32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 60),
    _VRtrMplsOutOfProfPktsFc3High32_Type()
)
vRtrMplsOutOfProfPktsFc3High32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsOutOfProfPktsFc3High32.setStatus("current")
_VRtrMplsOutOfProfPktsFc4_Type = Counter64
_VRtrMplsOutOfProfPktsFc4_Object = MibTableColumn
vRtrMplsOutOfProfPktsFc4 = _VRtrMplsOutOfProfPktsFc4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 61),
    _VRtrMplsOutOfProfPktsFc4_Type()
)
vRtrMplsOutOfProfPktsFc4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsOutOfProfPktsFc4.setStatus("current")
_VRtrMplsOutOfProfPktsFc4Low32_Type = Counter32
_VRtrMplsOutOfProfPktsFc4Low32_Object = MibTableColumn
vRtrMplsOutOfProfPktsFc4Low32 = _VRtrMplsOutOfProfPktsFc4Low32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 62),
    _VRtrMplsOutOfProfPktsFc4Low32_Type()
)
vRtrMplsOutOfProfPktsFc4Low32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsOutOfProfPktsFc4Low32.setStatus("current")
_VRtrMplsOutOfProfPktsFc4High32_Type = Counter32
_VRtrMplsOutOfProfPktsFc4High32_Object = MibTableColumn
vRtrMplsOutOfProfPktsFc4High32 = _VRtrMplsOutOfProfPktsFc4High32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 63),
    _VRtrMplsOutOfProfPktsFc4High32_Type()
)
vRtrMplsOutOfProfPktsFc4High32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsOutOfProfPktsFc4High32.setStatus("current")
_VRtrMplsOutOfProfPktsFc5_Type = Counter64
_VRtrMplsOutOfProfPktsFc5_Object = MibTableColumn
vRtrMplsOutOfProfPktsFc5 = _VRtrMplsOutOfProfPktsFc5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 64),
    _VRtrMplsOutOfProfPktsFc5_Type()
)
vRtrMplsOutOfProfPktsFc5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsOutOfProfPktsFc5.setStatus("current")
_VRtrMplsOutOfProfPktsFc5Low32_Type = Counter32
_VRtrMplsOutOfProfPktsFc5Low32_Object = MibTableColumn
vRtrMplsOutOfProfPktsFc5Low32 = _VRtrMplsOutOfProfPktsFc5Low32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 65),
    _VRtrMplsOutOfProfPktsFc5Low32_Type()
)
vRtrMplsOutOfProfPktsFc5Low32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsOutOfProfPktsFc5Low32.setStatus("current")
_VRtrMplsOutOfProfPktsFc5High32_Type = Counter32
_VRtrMplsOutOfProfPktsFc5High32_Object = MibTableColumn
vRtrMplsOutOfProfPktsFc5High32 = _VRtrMplsOutOfProfPktsFc5High32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 66),
    _VRtrMplsOutOfProfPktsFc5High32_Type()
)
vRtrMplsOutOfProfPktsFc5High32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsOutOfProfPktsFc5High32.setStatus("current")
_VRtrMplsOutOfProfPktsFc6_Type = Counter64
_VRtrMplsOutOfProfPktsFc6_Object = MibTableColumn
vRtrMplsOutOfProfPktsFc6 = _VRtrMplsOutOfProfPktsFc6_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 67),
    _VRtrMplsOutOfProfPktsFc6_Type()
)
vRtrMplsOutOfProfPktsFc6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsOutOfProfPktsFc6.setStatus("current")
_VRtrMplsOutOfProfPktsFc6Low32_Type = Counter32
_VRtrMplsOutOfProfPktsFc6Low32_Object = MibTableColumn
vRtrMplsOutOfProfPktsFc6Low32 = _VRtrMplsOutOfProfPktsFc6Low32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 68),
    _VRtrMplsOutOfProfPktsFc6Low32_Type()
)
vRtrMplsOutOfProfPktsFc6Low32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsOutOfProfPktsFc6Low32.setStatus("current")
_VRtrMplsOutOfProfPktsFc6High32_Type = Counter32
_VRtrMplsOutOfProfPktsFc6High32_Object = MibTableColumn
vRtrMplsOutOfProfPktsFc6High32 = _VRtrMplsOutOfProfPktsFc6High32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 69),
    _VRtrMplsOutOfProfPktsFc6High32_Type()
)
vRtrMplsOutOfProfPktsFc6High32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsOutOfProfPktsFc6High32.setStatus("current")
_VRtrMplsOutOfProfPktsFc7_Type = Counter64
_VRtrMplsOutOfProfPktsFc7_Object = MibTableColumn
vRtrMplsOutOfProfPktsFc7 = _VRtrMplsOutOfProfPktsFc7_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 70),
    _VRtrMplsOutOfProfPktsFc7_Type()
)
vRtrMplsOutOfProfPktsFc7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsOutOfProfPktsFc7.setStatus("current")
_VRtrMplsOutOfProfPktsFc7Low32_Type = Counter32
_VRtrMplsOutOfProfPktsFc7Low32_Object = MibTableColumn
vRtrMplsOutOfProfPktsFc7Low32 = _VRtrMplsOutOfProfPktsFc7Low32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 71),
    _VRtrMplsOutOfProfPktsFc7Low32_Type()
)
vRtrMplsOutOfProfPktsFc7Low32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsOutOfProfPktsFc7Low32.setStatus("current")
_VRtrMplsOutOfProfPktsFc7High32_Type = Counter32
_VRtrMplsOutOfProfPktsFc7High32_Object = MibTableColumn
vRtrMplsOutOfProfPktsFc7High32 = _VRtrMplsOutOfProfPktsFc7High32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 72),
    _VRtrMplsOutOfProfPktsFc7High32_Type()
)
vRtrMplsOutOfProfPktsFc7High32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsOutOfProfPktsFc7High32.setStatus("current")
_VRtrMplsOutOfProfOctetsFc0_Type = Counter64
_VRtrMplsOutOfProfOctetsFc0_Object = MibTableColumn
vRtrMplsOutOfProfOctetsFc0 = _VRtrMplsOutOfProfOctetsFc0_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 73),
    _VRtrMplsOutOfProfOctetsFc0_Type()
)
vRtrMplsOutOfProfOctetsFc0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsOutOfProfOctetsFc0.setStatus("current")
_VRtrMplsOutOfProfOctetsFc0Low32_Type = Counter32
_VRtrMplsOutOfProfOctetsFc0Low32_Object = MibTableColumn
vRtrMplsOutOfProfOctetsFc0Low32 = _VRtrMplsOutOfProfOctetsFc0Low32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 74),
    _VRtrMplsOutOfProfOctetsFc0Low32_Type()
)
vRtrMplsOutOfProfOctetsFc0Low32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsOutOfProfOctetsFc0Low32.setStatus("current")
_VRtrMplsOutOfProfOctetsFc0High32_Type = Counter32
_VRtrMplsOutOfProfOctetsFc0High32_Object = MibTableColumn
vRtrMplsOutOfProfOctetsFc0High32 = _VRtrMplsOutOfProfOctetsFc0High32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 75),
    _VRtrMplsOutOfProfOctetsFc0High32_Type()
)
vRtrMplsOutOfProfOctetsFc0High32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsOutOfProfOctetsFc0High32.setStatus("current")
_VRtrMplsOutOfProfOctetsFc1_Type = Counter64
_VRtrMplsOutOfProfOctetsFc1_Object = MibTableColumn
vRtrMplsOutOfProfOctetsFc1 = _VRtrMplsOutOfProfOctetsFc1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 76),
    _VRtrMplsOutOfProfOctetsFc1_Type()
)
vRtrMplsOutOfProfOctetsFc1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsOutOfProfOctetsFc1.setStatus("current")
_VRtrMplsOutOfProfOctetsFc1Low32_Type = Counter32
_VRtrMplsOutOfProfOctetsFc1Low32_Object = MibTableColumn
vRtrMplsOutOfProfOctetsFc1Low32 = _VRtrMplsOutOfProfOctetsFc1Low32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 77),
    _VRtrMplsOutOfProfOctetsFc1Low32_Type()
)
vRtrMplsOutOfProfOctetsFc1Low32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsOutOfProfOctetsFc1Low32.setStatus("current")
_VRtrMplsOutOfProfOctetsFc1High32_Type = Counter32
_VRtrMplsOutOfProfOctetsFc1High32_Object = MibTableColumn
vRtrMplsOutOfProfOctetsFc1High32 = _VRtrMplsOutOfProfOctetsFc1High32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 78),
    _VRtrMplsOutOfProfOctetsFc1High32_Type()
)
vRtrMplsOutOfProfOctetsFc1High32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsOutOfProfOctetsFc1High32.setStatus("current")
_VRtrMplsOutOfProfOctetsFc2_Type = Counter64
_VRtrMplsOutOfProfOctetsFc2_Object = MibTableColumn
vRtrMplsOutOfProfOctetsFc2 = _VRtrMplsOutOfProfOctetsFc2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 79),
    _VRtrMplsOutOfProfOctetsFc2_Type()
)
vRtrMplsOutOfProfOctetsFc2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsOutOfProfOctetsFc2.setStatus("current")
_VRtrMplsOutOfProfOctetsFc2Low32_Type = Counter32
_VRtrMplsOutOfProfOctetsFc2Low32_Object = MibTableColumn
vRtrMplsOutOfProfOctetsFc2Low32 = _VRtrMplsOutOfProfOctetsFc2Low32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 80),
    _VRtrMplsOutOfProfOctetsFc2Low32_Type()
)
vRtrMplsOutOfProfOctetsFc2Low32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsOutOfProfOctetsFc2Low32.setStatus("current")
_VRtrMplsOutOfProfOctetsFc2High32_Type = Counter32
_VRtrMplsOutOfProfOctetsFc2High32_Object = MibTableColumn
vRtrMplsOutOfProfOctetsFc2High32 = _VRtrMplsOutOfProfOctetsFc2High32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 81),
    _VRtrMplsOutOfProfOctetsFc2High32_Type()
)
vRtrMplsOutOfProfOctetsFc2High32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsOutOfProfOctetsFc2High32.setStatus("current")
_VRtrMplsOutOfProfOctetsFc3_Type = Counter64
_VRtrMplsOutOfProfOctetsFc3_Object = MibTableColumn
vRtrMplsOutOfProfOctetsFc3 = _VRtrMplsOutOfProfOctetsFc3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 82),
    _VRtrMplsOutOfProfOctetsFc3_Type()
)
vRtrMplsOutOfProfOctetsFc3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsOutOfProfOctetsFc3.setStatus("current")
_VRtrMplsOutOfProfOctetsFc3Low32_Type = Counter32
_VRtrMplsOutOfProfOctetsFc3Low32_Object = MibTableColumn
vRtrMplsOutOfProfOctetsFc3Low32 = _VRtrMplsOutOfProfOctetsFc3Low32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 83),
    _VRtrMplsOutOfProfOctetsFc3Low32_Type()
)
vRtrMplsOutOfProfOctetsFc3Low32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsOutOfProfOctetsFc3Low32.setStatus("current")
_VRtrMplsOutOfProfOctetsFc3High32_Type = Counter32
_VRtrMplsOutOfProfOctetsFc3High32_Object = MibTableColumn
vRtrMplsOutOfProfOctetsFc3High32 = _VRtrMplsOutOfProfOctetsFc3High32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 84),
    _VRtrMplsOutOfProfOctetsFc3High32_Type()
)
vRtrMplsOutOfProfOctetsFc3High32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsOutOfProfOctetsFc3High32.setStatus("current")
_VRtrMplsOutOfProfOctetsFc4_Type = Counter64
_VRtrMplsOutOfProfOctetsFc4_Object = MibTableColumn
vRtrMplsOutOfProfOctetsFc4 = _VRtrMplsOutOfProfOctetsFc4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 85),
    _VRtrMplsOutOfProfOctetsFc4_Type()
)
vRtrMplsOutOfProfOctetsFc4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsOutOfProfOctetsFc4.setStatus("current")
_VRtrMplsOutOfProfOctetsFc4Low32_Type = Counter32
_VRtrMplsOutOfProfOctetsFc4Low32_Object = MibTableColumn
vRtrMplsOutOfProfOctetsFc4Low32 = _VRtrMplsOutOfProfOctetsFc4Low32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 86),
    _VRtrMplsOutOfProfOctetsFc4Low32_Type()
)
vRtrMplsOutOfProfOctetsFc4Low32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsOutOfProfOctetsFc4Low32.setStatus("current")
_VRtrMplsOutOfProfOctetsFc4High32_Type = Counter32
_VRtrMplsOutOfProfOctetsFc4High32_Object = MibTableColumn
vRtrMplsOutOfProfOctetsFc4High32 = _VRtrMplsOutOfProfOctetsFc4High32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 87),
    _VRtrMplsOutOfProfOctetsFc4High32_Type()
)
vRtrMplsOutOfProfOctetsFc4High32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsOutOfProfOctetsFc4High32.setStatus("current")
_VRtrMplsOutOfProfOctetsFc5_Type = Counter64
_VRtrMplsOutOfProfOctetsFc5_Object = MibTableColumn
vRtrMplsOutOfProfOctetsFc5 = _VRtrMplsOutOfProfOctetsFc5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 88),
    _VRtrMplsOutOfProfOctetsFc5_Type()
)
vRtrMplsOutOfProfOctetsFc5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsOutOfProfOctetsFc5.setStatus("current")
_VRtrMplsOutOfProfOctetsFc5Low32_Type = Counter32
_VRtrMplsOutOfProfOctetsFc5Low32_Object = MibTableColumn
vRtrMplsOutOfProfOctetsFc5Low32 = _VRtrMplsOutOfProfOctetsFc5Low32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 89),
    _VRtrMplsOutOfProfOctetsFc5Low32_Type()
)
vRtrMplsOutOfProfOctetsFc5Low32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsOutOfProfOctetsFc5Low32.setStatus("current")
_VRtrMplsOutOfProfOctetsFc5High32_Type = Counter32
_VRtrMplsOutOfProfOctetsFc5High32_Object = MibTableColumn
vRtrMplsOutOfProfOctetsFc5High32 = _VRtrMplsOutOfProfOctetsFc5High32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 90),
    _VRtrMplsOutOfProfOctetsFc5High32_Type()
)
vRtrMplsOutOfProfOctetsFc5High32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsOutOfProfOctetsFc5High32.setStatus("current")
_VRtrMplsOutOfProfOctetsFc6_Type = Counter64
_VRtrMplsOutOfProfOctetsFc6_Object = MibTableColumn
vRtrMplsOutOfProfOctetsFc6 = _VRtrMplsOutOfProfOctetsFc6_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 91),
    _VRtrMplsOutOfProfOctetsFc6_Type()
)
vRtrMplsOutOfProfOctetsFc6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsOutOfProfOctetsFc6.setStatus("current")
_VRtrMplsOutOfProfOctetsFc6Low32_Type = Counter32
_VRtrMplsOutOfProfOctetsFc6Low32_Object = MibTableColumn
vRtrMplsOutOfProfOctetsFc6Low32 = _VRtrMplsOutOfProfOctetsFc6Low32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 92),
    _VRtrMplsOutOfProfOctetsFc6Low32_Type()
)
vRtrMplsOutOfProfOctetsFc6Low32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsOutOfProfOctetsFc6Low32.setStatus("current")
_VRtrMplsOutOfProfOctetsFc6High32_Type = Counter32
_VRtrMplsOutOfProfOctetsFc6High32_Object = MibTableColumn
vRtrMplsOutOfProfOctetsFc6High32 = _VRtrMplsOutOfProfOctetsFc6High32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 93),
    _VRtrMplsOutOfProfOctetsFc6High32_Type()
)
vRtrMplsOutOfProfOctetsFc6High32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsOutOfProfOctetsFc6High32.setStatus("current")
_VRtrMplsOutOfProfOctetsFc7_Type = Counter64
_VRtrMplsOutOfProfOctetsFc7_Object = MibTableColumn
vRtrMplsOutOfProfOctetsFc7 = _VRtrMplsOutOfProfOctetsFc7_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 94),
    _VRtrMplsOutOfProfOctetsFc7_Type()
)
vRtrMplsOutOfProfOctetsFc7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsOutOfProfOctetsFc7.setStatus("current")
_VRtrMplsOutOfProfOctetsFc7Low32_Type = Counter32
_VRtrMplsOutOfProfOctetsFc7Low32_Object = MibTableColumn
vRtrMplsOutOfProfOctetsFc7Low32 = _VRtrMplsOutOfProfOctetsFc7Low32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 95),
    _VRtrMplsOutOfProfOctetsFc7Low32_Type()
)
vRtrMplsOutOfProfOctetsFc7Low32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsOutOfProfOctetsFc7Low32.setStatus("current")
_VRtrMplsOutOfProfOctetsFc7High32_Type = Counter32
_VRtrMplsOutOfProfOctetsFc7High32_Object = MibTableColumn
vRtrMplsOutOfProfOctetsFc7High32 = _VRtrMplsOutOfProfOctetsFc7High32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 96),
    _VRtrMplsOutOfProfOctetsFc7High32_Type()
)
vRtrMplsOutOfProfOctetsFc7High32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsOutOfProfOctetsFc7High32.setStatus("current")
_VRtrMplsLspStatsPSBMatch_Type = TruthValue
_VRtrMplsLspStatsPSBMatch_Object = MibTableColumn
vRtrMplsLspStatsPSBMatch = _VRtrMplsLspStatsPSBMatch_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 97),
    _VRtrMplsLspStatsPSBMatch_Type()
)
vRtrMplsLspStatsPSBMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspStatsPSBMatch.setStatus("current")
_VRtrMplsLspStatsTpOnly_Type = TruthValue
_VRtrMplsLspStatsTpOnly_Object = MibTableColumn
vRtrMplsLspStatsTpOnly = _VRtrMplsLspStatsTpOnly_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 98),
    _VRtrMplsLspStatsTpOnly_Type()
)
vRtrMplsLspStatsTpOnly.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspStatsTpOnly.setStatus("current")


class _VRtrMplsLspStatsLspType_Type(Integer32):
    """Custom type vRtrMplsLspStatsLspType based on Integer32"""
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
          ("p2p", 1),
          ("p2mp", 2),
          ("autoP2p", 3),
          ("autoP2mp", 4),
          ("tpLsp", 5))
    )


_VRtrMplsLspStatsLspType_Type.__name__ = "Integer32"
_VRtrMplsLspStatsLspType_Object = MibTableColumn
vRtrMplsLspStatsLspType = _VRtrMplsLspStatsLspType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 39, 1, 99),
    _VRtrMplsLspStatsLspType_Type()
)
vRtrMplsLspStatsLspType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspStatsLspType.setStatus("current")
_VRtrMplsLspTemplateTblLastChgd_Type = TimeStamp
_VRtrMplsLspTemplateTblLastChgd_Object = MibScalar
vRtrMplsLspTemplateTblLastChgd = _VRtrMplsLspTemplateTblLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 40),
    _VRtrMplsLspTemplateTblLastChgd_Type()
)
vRtrMplsLspTemplateTblLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspTemplateTblLastChgd.setStatus("current")
_VRtrMplsLspTemplateTable_Object = MibTable
vRtrMplsLspTemplateTable = _VRtrMplsLspTemplateTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41)
)
if mibBuilder.loadTexts:
    vRtrMplsLspTemplateTable.setStatus("current")
_VRtrMplsLspTemplateEntry_Object = MibTableRow
vRtrMplsLspTemplateEntry = _VRtrMplsLspTemplateEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1)
)
vRtrMplsLspTemplateEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateName"),
)
if mibBuilder.loadTexts:
    vRtrMplsLspTemplateEntry.setStatus("current")
_VRtrMplsLspTemplateName_Type = TNamedItem
_VRtrMplsLspTemplateName_Object = MibTableColumn
vRtrMplsLspTemplateName = _VRtrMplsLspTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 1),
    _VRtrMplsLspTemplateName_Type()
)
vRtrMplsLspTemplateName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsLspTemplateName.setStatus("current")
_VRtrMplsLspTemplateRowStatus_Type = RowStatus
_VRtrMplsLspTemplateRowStatus_Object = MibTableColumn
vRtrMplsLspTemplateRowStatus = _VRtrMplsLspTemplateRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 2),
    _VRtrMplsLspTemplateRowStatus_Type()
)
vRtrMplsLspTemplateRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTemplateRowStatus.setStatus("current")
_VRtrMplsLspTemplateLastChanged_Type = TimeStamp
_VRtrMplsLspTemplateLastChanged_Object = MibTableColumn
vRtrMplsLspTemplateLastChanged = _VRtrMplsLspTemplateLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 3),
    _VRtrMplsLspTemplateLastChanged_Type()
)
vRtrMplsLspTemplateLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspTemplateLastChanged.setStatus("current")


class _VRtrMplsLspTemplateAdminState_Type(TmnxAdminState):
    """Custom type vRtrMplsLspTemplateAdminState based on TmnxAdminState"""
    defaultValue = 3


_VRtrMplsLspTemplateAdminState_Type.__name__ = "TmnxAdminState"
_VRtrMplsLspTemplateAdminState_Object = MibTableColumn
vRtrMplsLspTemplateAdminState = _VRtrMplsLspTemplateAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 4),
    _VRtrMplsLspTemplateAdminState_Type()
)
vRtrMplsLspTemplateAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTemplateAdminState.setStatus("current")


class _VRtrMplsLspTemplateType_Type(Integer32):
    """Custom type vRtrMplsLspTemplateType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("p2mp", 1),
          ("onehopP2P", 2),
          ("meshP2P", 3))
    )


_VRtrMplsLspTemplateType_Type.__name__ = "Integer32"
_VRtrMplsLspTemplateType_Object = MibTableColumn
vRtrMplsLspTemplateType = _VRtrMplsLspTemplateType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 5),
    _VRtrMplsLspTemplateType_Type()
)
vRtrMplsLspTemplateType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTemplateType.setStatus("current")


class _VRtrMplsLspTemplateAdaptive_Type(TruthValue):
    """Custom type vRtrMplsLspTemplateAdaptive based on TruthValue"""
    defaultValue = 1


_VRtrMplsLspTemplateAdaptive_Type.__name__ = "TruthValue"
_VRtrMplsLspTemplateAdaptive_Object = MibTableColumn
vRtrMplsLspTemplateAdaptive = _VRtrMplsLspTemplateAdaptive_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 6),
    _VRtrMplsLspTemplateAdaptive_Type()
)
vRtrMplsLspTemplateAdaptive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTemplateAdaptive.setStatus("current")


class _VRtrMplsLspTemplateBandwidth_Type(Integer32):
    """Custom type vRtrMplsLspTemplateBandwidth based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_VRtrMplsLspTemplateBandwidth_Type.__name__ = "Integer32"
_VRtrMplsLspTemplateBandwidth_Object = MibTableColumn
vRtrMplsLspTemplateBandwidth = _VRtrMplsLspTemplateBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 7),
    _VRtrMplsLspTemplateBandwidth_Type()
)
vRtrMplsLspTemplateBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTemplateBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspTemplateBandwidth.setUnits("mega-bits per second")


class _VRtrMplsLspTemplateCspf_Type(TruthValue):
    """Custom type vRtrMplsLspTemplateCspf based on TruthValue"""
    defaultValue = 2


_VRtrMplsLspTemplateCspf_Type.__name__ = "TruthValue"
_VRtrMplsLspTemplateCspf_Object = MibTableColumn
vRtrMplsLspTemplateCspf = _VRtrMplsLspTemplateCspf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 8),
    _VRtrMplsLspTemplateCspf_Type()
)
vRtrMplsLspTemplateCspf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTemplateCspf.setStatus("current")
_VRtrMplsLspTemplateDefaultPath_Type = MplsTunnelIndex
_VRtrMplsLspTemplateDefaultPath_Object = MibTableColumn
vRtrMplsLspTemplateDefaultPath = _VRtrMplsLspTemplateDefaultPath_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 9),
    _VRtrMplsLspTemplateDefaultPath_Type()
)
vRtrMplsLspTemplateDefaultPath.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTemplateDefaultPath.setStatus("current")


class _VRtrMplsLspTemplateAdmGrpIncl_Type(Unsigned32):
    """Custom type vRtrMplsLspTemplateAdmGrpIncl based on Unsigned32"""
    defaultValue = 0


_VRtrMplsLspTemplateAdmGrpIncl_Type.__name__ = "Unsigned32"
_VRtrMplsLspTemplateAdmGrpIncl_Object = MibTableColumn
vRtrMplsLspTemplateAdmGrpIncl = _VRtrMplsLspTemplateAdmGrpIncl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 10),
    _VRtrMplsLspTemplateAdmGrpIncl_Type()
)
vRtrMplsLspTemplateAdmGrpIncl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTemplateAdmGrpIncl.setStatus("current")


class _VRtrMplsLspTemplateAdmGrpExcl_Type(Unsigned32):
    """Custom type vRtrMplsLspTemplateAdmGrpExcl based on Unsigned32"""
    defaultValue = 0


_VRtrMplsLspTemplateAdmGrpExcl_Type.__name__ = "Unsigned32"
_VRtrMplsLspTemplateAdmGrpExcl_Object = MibTableColumn
vRtrMplsLspTemplateAdmGrpExcl = _VRtrMplsLspTemplateAdmGrpExcl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 11),
    _VRtrMplsLspTemplateAdmGrpExcl_Type()
)
vRtrMplsLspTemplateAdmGrpExcl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTemplateAdmGrpExcl.setStatus("current")


class _VRtrMplsLspTemplateFastReroute_Type(TruthValue):
    """Custom type vRtrMplsLspTemplateFastReroute based on TruthValue"""
    defaultValue = 2


_VRtrMplsLspTemplateFastReroute_Type.__name__ = "TruthValue"
_VRtrMplsLspTemplateFastReroute_Object = MibTableColumn
vRtrMplsLspTemplateFastReroute = _VRtrMplsLspTemplateFastReroute_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 12),
    _VRtrMplsLspTemplateFastReroute_Type()
)
vRtrMplsLspTemplateFastReroute.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTemplateFastReroute.setStatus("current")


class _VRtrMplsLspTemplateFRMethod_Type(Integer32):
    """Custom type vRtrMplsLspTemplateFRMethod based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oneToOneBackup", 1),
          ("facilityBackup", 2))
    )


_VRtrMplsLspTemplateFRMethod_Type.__name__ = "Integer32"
_VRtrMplsLspTemplateFRMethod_Object = MibTableColumn
vRtrMplsLspTemplateFRMethod = _VRtrMplsLspTemplateFRMethod_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 13),
    _VRtrMplsLspTemplateFRMethod_Type()
)
vRtrMplsLspTemplateFRMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTemplateFRMethod.setStatus("current")


class _VRtrMplsLspTemplateFRHopLimit_Type(Unsigned32):
    """Custom type vRtrMplsLspTemplateFRHopLimit based on Unsigned32"""
    defaultValue = 16

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VRtrMplsLspTemplateFRHopLimit_Type.__name__ = "Unsigned32"
_VRtrMplsLspTemplateFRHopLimit_Object = MibTableColumn
vRtrMplsLspTemplateFRHopLimit = _VRtrMplsLspTemplateFRHopLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 14),
    _VRtrMplsLspTemplateFRHopLimit_Type()
)
vRtrMplsLspTemplateFRHopLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTemplateFRHopLimit.setStatus("current")


class _VRtrMplsLspTemplateHopLimit_Type(Unsigned32):
    """Custom type vRtrMplsLspTemplateHopLimit based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 255),
    )


_VRtrMplsLspTemplateHopLimit_Type.__name__ = "Unsigned32"
_VRtrMplsLspTemplateHopLimit_Object = MibTableColumn
vRtrMplsLspTemplateHopLimit = _VRtrMplsLspTemplateHopLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 15),
    _VRtrMplsLspTemplateHopLimit_Type()
)
vRtrMplsLspTemplateHopLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTemplateHopLimit.setStatus("current")


class _VRtrMplsLspTemplateRecord_Type(Integer32):
    """Custom type vRtrMplsLspTemplateRecord based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("record", 1),
          ("noRecord", 2))
    )


_VRtrMplsLspTemplateRecord_Type.__name__ = "Integer32"
_VRtrMplsLspTemplateRecord_Object = MibTableColumn
vRtrMplsLspTemplateRecord = _VRtrMplsLspTemplateRecord_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 16),
    _VRtrMplsLspTemplateRecord_Type()
)
vRtrMplsLspTemplateRecord.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTemplateRecord.setStatus("current")


class _VRtrMplsLspTemplateRecordLabel_Type(Integer32):
    """Custom type vRtrMplsLspTemplateRecordLabel based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("record", 1),
          ("noRecord", 2))
    )


_VRtrMplsLspTemplateRecordLabel_Type.__name__ = "Integer32"
_VRtrMplsLspTemplateRecordLabel_Object = MibTableColumn
vRtrMplsLspTemplateRecordLabel = _VRtrMplsLspTemplateRecordLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 17),
    _VRtrMplsLspTemplateRecordLabel_Type()
)
vRtrMplsLspTemplateRecordLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTemplateRecordLabel.setStatus("current")


class _VRtrMplsLspTemplateRetryLimit_Type(Unsigned32):
    """Custom type vRtrMplsLspTemplateRetryLimit based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_VRtrMplsLspTemplateRetryLimit_Type.__name__ = "Unsigned32"
_VRtrMplsLspTemplateRetryLimit_Object = MibTableColumn
vRtrMplsLspTemplateRetryLimit = _VRtrMplsLspTemplateRetryLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 18),
    _VRtrMplsLspTemplateRetryLimit_Type()
)
vRtrMplsLspTemplateRetryLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTemplateRetryLimit.setStatus("current")


class _VRtrMplsLspTemplateRetryTimer_Type(Unsigned32):
    """Custom type vRtrMplsLspTemplateRetryTimer based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_VRtrMplsLspTemplateRetryTimer_Type.__name__ = "Unsigned32"
_VRtrMplsLspTemplateRetryTimer_Object = MibTableColumn
vRtrMplsLspTemplateRetryTimer = _VRtrMplsLspTemplateRetryTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 19),
    _VRtrMplsLspTemplateRetryTimer_Type()
)
vRtrMplsLspTemplateRetryTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTemplateRetryTimer.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspTemplateRetryTimer.setUnits("seconds")


class _VRtrMplsLspTemplateCspfTeMetric_Type(TruthValue):
    """Custom type vRtrMplsLspTemplateCspfTeMetric based on TruthValue"""
    defaultValue = 2


_VRtrMplsLspTemplateCspfTeMetric_Type.__name__ = "TruthValue"
_VRtrMplsLspTemplateCspfTeMetric_Object = MibTableColumn
vRtrMplsLspTemplateCspfTeMetric = _VRtrMplsLspTemplateCspfTeMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 20),
    _VRtrMplsLspTemplateCspfTeMetric_Type()
)
vRtrMplsLspTemplateCspfTeMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTemplateCspfTeMetric.setStatus("current")
_VRtrMplsLspTemplateLspCount_Type = Gauge32
_VRtrMplsLspTemplateLspCount_Object = MibTableColumn
vRtrMplsLspTemplateLspCount = _VRtrMplsLspTemplateLspCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 21),
    _VRtrMplsLspTemplateLspCount_Type()
)
vRtrMplsLspTemplateLspCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspTemplateLspCount.setStatus("current")
_VRtrMplsLspTemplateMvpnRefCount_Type = Gauge32
_VRtrMplsLspTemplateMvpnRefCount_Object = MibTableColumn
vRtrMplsLspTemplateMvpnRefCount = _VRtrMplsLspTemplateMvpnRefCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 22),
    _VRtrMplsLspTemplateMvpnRefCount_Type()
)
vRtrMplsLspTemplateMvpnRefCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspTemplateMvpnRefCount.setStatus("current")


class _VRtrMplsLspTemplateFRPropAdmGrp_Type(TruthValue):
    """Custom type vRtrMplsLspTemplateFRPropAdmGrp based on TruthValue"""
    defaultValue = 2


_VRtrMplsLspTemplateFRPropAdmGrp_Type.__name__ = "TruthValue"
_VRtrMplsLspTemplateFRPropAdmGrp_Object = MibTableColumn
vRtrMplsLspTemplateFRPropAdmGrp = _VRtrMplsLspTemplateFRPropAdmGrp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 23),
    _VRtrMplsLspTemplateFRPropAdmGrp_Type()
)
vRtrMplsLspTemplateFRPropAdmGrp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTemplateFRPropAdmGrp.setStatus("current")


class _VRtrMplsLspTemplatePropAdmGrp_Type(TruthValue):
    """Custom type vRtrMplsLspTemplatePropAdmGrp based on TruthValue"""
    defaultValue = 2


_VRtrMplsLspTemplatePropAdmGrp_Type.__name__ = "TruthValue"
_VRtrMplsLspTemplatePropAdmGrp_Object = MibTableColumn
vRtrMplsLspTemplatePropAdmGrp = _VRtrMplsLspTemplatePropAdmGrp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 24),
    _VRtrMplsLspTemplatePropAdmGrp_Type()
)
vRtrMplsLspTemplatePropAdmGrp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTemplatePropAdmGrp.setStatus("current")


class _VRtrMplsLspTemplateBgpShortcut_Type(TruthValue):
    """Custom type vRtrMplsLspTemplateBgpShortcut based on TruthValue"""
    defaultValue = 1


_VRtrMplsLspTemplateBgpShortcut_Type.__name__ = "TruthValue"
_VRtrMplsLspTemplateBgpShortcut_Object = MibTableColumn
vRtrMplsLspTemplateBgpShortcut = _VRtrMplsLspTemplateBgpShortcut_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 25),
    _VRtrMplsLspTemplateBgpShortcut_Type()
)
vRtrMplsLspTemplateBgpShortcut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTemplateBgpShortcut.setStatus("current")


class _VRtrMplsLspTemplateIgpShortcut_Type(TruthValue):
    """Custom type vRtrMplsLspTemplateIgpShortcut based on TruthValue"""
    defaultValue = 1


_VRtrMplsLspTemplateIgpShortcut_Type.__name__ = "TruthValue"
_VRtrMplsLspTemplateIgpShortcut_Object = MibTableColumn
vRtrMplsLspTemplateIgpShortcut = _VRtrMplsLspTemplateIgpShortcut_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 26),
    _VRtrMplsLspTemplateIgpShortcut_Type()
)
vRtrMplsLspTemplateIgpShortcut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTemplateIgpShortcut.setStatus("current")


class _VRtrMplsLspTemplateLdpOverRsvp_Type(TruthValue):
    """Custom type vRtrMplsLspTemplateLdpOverRsvp based on TruthValue"""
    defaultValue = 1


_VRtrMplsLspTemplateLdpOverRsvp_Type.__name__ = "TruthValue"
_VRtrMplsLspTemplateLdpOverRsvp_Object = MibTableColumn
vRtrMplsLspTemplateLdpOverRsvp = _VRtrMplsLspTemplateLdpOverRsvp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 27),
    _VRtrMplsLspTemplateLdpOverRsvp_Type()
)
vRtrMplsLspTemplateLdpOverRsvp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTemplateLdpOverRsvp.setStatus("current")


class _VRtrMplsLspTemplateLeastFill_Type(TruthValue):
    """Custom type vRtrMplsLspTemplateLeastFill based on TruthValue"""
    defaultValue = 2


_VRtrMplsLspTemplateLeastFill_Type.__name__ = "TruthValue"
_VRtrMplsLspTemplateLeastFill_Object = MibTableColumn
vRtrMplsLspTemplateLeastFill = _VRtrMplsLspTemplateLeastFill_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 28),
    _VRtrMplsLspTemplateLeastFill_Type()
)
vRtrMplsLspTemplateLeastFill.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTemplateLeastFill.setStatus("current")


class _VRtrMplsLspTemplateMetric_Type(Unsigned32):
    """Custom type vRtrMplsLspTemplateMetric based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 16777215),
    )


_VRtrMplsLspTemplateMetric_Type.__name__ = "Unsigned32"
_VRtrMplsLspTemplateMetric_Object = MibTableColumn
vRtrMplsLspTemplateMetric = _VRtrMplsLspTemplateMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 29),
    _VRtrMplsLspTemplateMetric_Type()
)
vRtrMplsLspTemplateMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTemplateMetric.setStatus("current")


class _VRtrMplsLspTemplateSetupPriority_Type(Unsigned32):
    """Custom type vRtrMplsLspTemplateSetupPriority based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_VRtrMplsLspTemplateSetupPriority_Type.__name__ = "Unsigned32"
_VRtrMplsLspTemplateSetupPriority_Object = MibTableColumn
vRtrMplsLspTemplateSetupPriority = _VRtrMplsLspTemplateSetupPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 30),
    _VRtrMplsLspTemplateSetupPriority_Type()
)
vRtrMplsLspTemplateSetupPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTemplateSetupPriority.setStatus("current")


class _VRtrMplsLspTemplateHoldPriority_Type(Unsigned32):
    """Custom type vRtrMplsLspTemplateHoldPriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_VRtrMplsLspTemplateHoldPriority_Type.__name__ = "Unsigned32"
_VRtrMplsLspTemplateHoldPriority_Object = MibTableColumn
vRtrMplsLspTemplateHoldPriority = _VRtrMplsLspTemplateHoldPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 31),
    _VRtrMplsLspTemplateHoldPriority_Type()
)
vRtrMplsLspTemplateHoldPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTemplateHoldPriority.setStatus("current")


class _VRtrMplsLspTemplateVprnAutoBind_Type(TruthValue):
    """Custom type vRtrMplsLspTemplateVprnAutoBind based on TruthValue"""
    defaultValue = 1


_VRtrMplsLspTemplateVprnAutoBind_Type.__name__ = "TruthValue"
_VRtrMplsLspTemplateVprnAutoBind_Object = MibTableColumn
vRtrMplsLspTemplateVprnAutoBind = _VRtrMplsLspTemplateVprnAutoBind_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 32),
    _VRtrMplsLspTemplateVprnAutoBind_Type()
)
vRtrMplsLspTemplateVprnAutoBind.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTemplateVprnAutoBind.setStatus("current")


class _VRtrMplsLspTempIgpSCutLfaType_Type(Integer32):
    """Custom type vRtrMplsLspTempIgpSCutLfaType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("lfaProtect", 1),
          ("lfaOnly", 2))
    )


_VRtrMplsLspTempIgpSCutLfaType_Type.__name__ = "Integer32"
_VRtrMplsLspTempIgpSCutLfaType_Object = MibTableColumn
vRtrMplsLspTempIgpSCutLfaType = _VRtrMplsLspTempIgpSCutLfaType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 33),
    _VRtrMplsLspTempIgpSCutLfaType_Type()
)
vRtrMplsLspTempIgpSCutLfaType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTempIgpSCutLfaType.setStatus("current")


class _VRtrMplsLspTempIgpSCutRelOffset_Type(Integer32):
    """Custom type vRtrMplsLspTempIgpSCutRelOffset based on Integer32"""
    defaultValue = 2147483647

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-10, 10),
        ValueRangeConstraint(2147483647, 2147483647),
    )


_VRtrMplsLspTempIgpSCutRelOffset_Type.__name__ = "Integer32"
_VRtrMplsLspTempIgpSCutRelOffset_Object = MibTableColumn
vRtrMplsLspTempIgpSCutRelOffset = _VRtrMplsLspTempIgpSCutRelOffset_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 34),
    _VRtrMplsLspTempIgpSCutRelOffset_Type()
)
vRtrMplsLspTempIgpSCutRelOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTempIgpSCutRelOffset.setStatus("current")


class _VRtrMplsLspTempAutoBandwidth_Type(TruthValue):
    """Custom type vRtrMplsLspTempAutoBandwidth based on TruthValue"""
    defaultValue = 2


_VRtrMplsLspTempAutoBandwidth_Type.__name__ = "TruthValue"
_VRtrMplsLspTempAutoBandwidth_Object = MibTableColumn
vRtrMplsLspTempAutoBandwidth = _VRtrMplsLspTempAutoBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 35),
    _VRtrMplsLspTempAutoBandwidth_Type()
)
vRtrMplsLspTempAutoBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAutoBandwidth.setStatus("current")


class _VRtrMplsLspTempFRNodeProtect_Type(TruthValue):
    """Custom type vRtrMplsLspTempFRNodeProtect based on TruthValue"""
    defaultValue = 2


_VRtrMplsLspTempFRNodeProtect_Type.__name__ = "TruthValue"
_VRtrMplsLspTempFRNodeProtect_Object = MibTableColumn
vRtrMplsLspTempFRNodeProtect = _VRtrMplsLspTempFRNodeProtect_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 36),
    _VRtrMplsLspTempFRNodeProtect_Type()
)
vRtrMplsLspTempFRNodeProtect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTempFRNodeProtect.setStatus("current")


class _VRtrMplsLspTemplateEgrStats_Type(TruthValue):
    """Custom type vRtrMplsLspTemplateEgrStats based on TruthValue"""
    defaultValue = 2


_VRtrMplsLspTemplateEgrStats_Type.__name__ = "TruthValue"
_VRtrMplsLspTemplateEgrStats_Object = MibTableColumn
vRtrMplsLspTemplateEgrStats = _VRtrMplsLspTemplateEgrStats_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 37),
    _VRtrMplsLspTemplateEgrStats_Type()
)
vRtrMplsLspTemplateEgrStats.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTemplateEgrStats.setStatus("current")


class _VRtrMplsLspTempCollectStats_Type(TruthValue):
    """Custom type vRtrMplsLspTempCollectStats based on TruthValue"""
    defaultValue = 2


_VRtrMplsLspTempCollectStats_Type.__name__ = "TruthValue"
_VRtrMplsLspTempCollectStats_Object = MibTableColumn
vRtrMplsLspTempCollectStats = _VRtrMplsLspTempCollectStats_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 38),
    _VRtrMplsLspTempCollectStats_Type()
)
vRtrMplsLspTempCollectStats.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTempCollectStats.setStatus("current")


class _VRtrMplsLspTempAccntingPolicy_Type(Unsigned32):
    """Custom type vRtrMplsLspTempAccntingPolicy based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 99),
    )


_VRtrMplsLspTempAccntingPolicy_Type.__name__ = "Unsigned32"
_VRtrMplsLspTempAccntingPolicy_Object = MibTableColumn
vRtrMplsLspTempAccntingPolicy = _VRtrMplsLspTempAccntingPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 39),
    _VRtrMplsLspTempAccntingPolicy_Type()
)
vRtrMplsLspTempAccntingPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAccntingPolicy.setStatus("current")


class _VRtrMplsLspTemplateFromAddrType_Type(InetAddressType):
    """Custom type vRtrMplsLspTemplateFromAddrType based on InetAddressType"""
    defaultValue = 0


_VRtrMplsLspTemplateFromAddrType_Type.__name__ = "InetAddressType"
_VRtrMplsLspTemplateFromAddrType_Object = MibTableColumn
vRtrMplsLspTemplateFromAddrType = _VRtrMplsLspTemplateFromAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 40),
    _VRtrMplsLspTemplateFromAddrType_Type()
)
vRtrMplsLspTemplateFromAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTemplateFromAddrType.setStatus("current")


class _VRtrMplsLspTemplateFromAddr_Type(InetAddress):
    """Custom type vRtrMplsLspTemplateFromAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrMplsLspTemplateFromAddr_Type.__name__ = "InetAddress"
_VRtrMplsLspTemplateFromAddr_Object = MibTableColumn
vRtrMplsLspTemplateFromAddr = _VRtrMplsLspTemplateFromAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 41),
    _VRtrMplsLspTemplateFromAddr_Type()
)
vRtrMplsLspTemplateFromAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTemplateFromAddr.setStatus("current")


class _VRtrMplsLspTemplateClassType_Type(TmnxRsvpDSTEClassType):
    """Custom type vRtrMplsLspTemplateClassType based on TmnxRsvpDSTEClassType"""
    defaultValue = 0


_VRtrMplsLspTemplateClassType_Type.__name__ = "TmnxRsvpDSTEClassType"
_VRtrMplsLspTemplateClassType_Object = MibTableColumn
vRtrMplsLspTemplateClassType = _VRtrMplsLspTemplateClassType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 42),
    _VRtrMplsLspTemplateClassType_Type()
)
vRtrMplsLspTemplateClassType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTemplateClassType.setStatus("current")


class _VRtrMplsLspTempBkupClassType_Type(TmnxRsvpDSTEClassType):
    """Custom type vRtrMplsLspTempBkupClassType based on TmnxRsvpDSTEClassType"""
    defaultValue = 0


_VRtrMplsLspTempBkupClassType_Type.__name__ = "TmnxRsvpDSTEClassType"
_VRtrMplsLspTempBkupClassType_Object = MibTableColumn
vRtrMplsLspTempBkupClassType = _VRtrMplsLspTempBkupClassType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 43),
    _VRtrMplsLspTempBkupClassType_Type()
)
vRtrMplsLspTempBkupClassType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTempBkupClassType.setStatus("current")


class _VRtrMplsLspTempBgpTransportTunn_Type(TmnxMplsLspBgpRSVPLSPTunState):
    """Custom type vRtrMplsLspTempBgpTransportTunn based on TmnxMplsLspBgpRSVPLSPTunState"""
    defaultValue = 1


_VRtrMplsLspTempBgpTransportTunn_Type.__name__ = "TmnxMplsLspBgpRSVPLSPTunState"
_VRtrMplsLspTempBgpTransportTunn_Object = MibTableColumn
vRtrMplsLspTempBgpTransportTunn = _VRtrMplsLspTempBgpTransportTunn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 44),
    _VRtrMplsLspTempBgpTransportTunn_Type()
)
vRtrMplsLspTempBgpTransportTunn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTempBgpTransportTunn.setStatus("current")


class _VRtrMplsLspTempMainCTRetryLimit_Type(Unsigned32):
    """Custom type vRtrMplsLspTempMainCTRetryLimit based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_VRtrMplsLspTempMainCTRetryLimit_Type.__name__ = "Unsigned32"
_VRtrMplsLspTempMainCTRetryLimit_Object = MibTableColumn
vRtrMplsLspTempMainCTRetryLimit = _VRtrMplsLspTempMainCTRetryLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 45),
    _VRtrMplsLspTempMainCTRetryLimit_Type()
)
vRtrMplsLspTempMainCTRetryLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTempMainCTRetryLimit.setStatus("current")


class _VRtrMplsLspTemplateRsvpAdspec_Type(TruthValue):
    """Custom type vRtrMplsLspTemplateRsvpAdspec based on TruthValue"""
    defaultValue = 2


_VRtrMplsLspTemplateRsvpAdspec_Type.__name__ = "TruthValue"
_VRtrMplsLspTemplateRsvpAdspec_Object = MibTableColumn
vRtrMplsLspTemplateRsvpAdspec = _VRtrMplsLspTemplateRsvpAdspec_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 46),
    _VRtrMplsLspTemplateRsvpAdspec_Type()
)
vRtrMplsLspTemplateRsvpAdspec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTemplateRsvpAdspec.setStatus("current")


class _VRtrMplsLspTempLoadBalancingWt_Type(Unsigned32):
    """Custom type vRtrMplsLspTempLoadBalancingWt based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4294967295),
    )


_VRtrMplsLspTempLoadBalancingWt_Type.__name__ = "Unsigned32"
_VRtrMplsLspTempLoadBalancingWt_Object = MibTableColumn
vRtrMplsLspTempLoadBalancingWt = _VRtrMplsLspTempLoadBalancingWt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 47),
    _VRtrMplsLspTempLoadBalancingWt_Type()
)
vRtrMplsLspTempLoadBalancingWt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTempLoadBalancingWt.setStatus("current")


class _VRtrMplsLspTempClassFwdEnabled_Type(TruthValue):
    """Custom type vRtrMplsLspTempClassFwdEnabled based on TruthValue"""
    defaultValue = 2


_VRtrMplsLspTempClassFwdEnabled_Type.__name__ = "TruthValue"
_VRtrMplsLspTempClassFwdEnabled_Object = MibTableColumn
vRtrMplsLspTempClassFwdEnabled = _VRtrMplsLspTempClassFwdEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 48),
    _VRtrMplsLspTempClassFwdEnabled_Type()
)
vRtrMplsLspTempClassFwdEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTempClassFwdEnabled.setStatus("current")


class _VRtrMplsLspTempFC_Type(TmnxCBFClasses):
    """Custom type vRtrMplsLspTempFC based on TmnxCBFClasses"""
    defaultBinValue = "0"


_VRtrMplsLspTempFC_Type.__name__ = "TmnxCBFClasses"
_VRtrMplsLspTempFC_Object = MibTableColumn
vRtrMplsLspTempFC = _VRtrMplsLspTempFC_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 49),
    _VRtrMplsLspTempFC_Type()
)
vRtrMplsLspTempFC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTempFC.setStatus("current")
_VRtrMplsLspTempBfdTemplateName_Type = TNamedItemOrEmpty
_VRtrMplsLspTempBfdTemplateName_Object = MibTableColumn
vRtrMplsLspTempBfdTemplateName = _VRtrMplsLspTempBfdTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 50),
    _VRtrMplsLspTempBfdTemplateName_Type()
)
vRtrMplsLspTempBfdTemplateName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTempBfdTemplateName.setStatus("current")


class _VRtrMplsLspTempBfdEnable_Type(TruthValue):
    """Custom type vRtrMplsLspTempBfdEnable based on TruthValue"""
    defaultValue = 2


_VRtrMplsLspTempBfdEnable_Type.__name__ = "TruthValue"
_VRtrMplsLspTempBfdEnable_Object = MibTableColumn
vRtrMplsLspTempBfdEnable = _VRtrMplsLspTempBfdEnable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 51),
    _VRtrMplsLspTempBfdEnable_Type()
)
vRtrMplsLspTempBfdEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTempBfdEnable.setStatus("current")


class _VRtrMplsLspTempBfdPingIntvl_Type(Unsigned32):
    """Custom type vRtrMplsLspTempBfdPingIntvl based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(60, 300),
    )


_VRtrMplsLspTempBfdPingIntvl_Type.__name__ = "Unsigned32"
_VRtrMplsLspTempBfdPingIntvl_Object = MibTableColumn
vRtrMplsLspTempBfdPingIntvl = _VRtrMplsLspTempBfdPingIntvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 52),
    _VRtrMplsLspTempBfdPingIntvl_Type()
)
vRtrMplsLspTempBfdPingIntvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTempBfdPingIntvl.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspTempBfdPingIntvl.setUnits("seconds")


class _VRtrMplsLspTempEntropyLabel_Type(Integer32):
    """Custom type vRtrMplsLspTempEntropyLabel based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("forceDisable", 1),
          ("enable", 2),
          ("inherit", 3))
    )


_VRtrMplsLspTempEntropyLabel_Type.__name__ = "Integer32"
_VRtrMplsLspTempEntropyLabel_Object = MibTableColumn
vRtrMplsLspTempEntropyLabel = _VRtrMplsLspTempEntropyLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 53),
    _VRtrMplsLspTempEntropyLabel_Type()
)
vRtrMplsLspTempEntropyLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTempEntropyLabel.setStatus("current")


class _VRtrMplsLspTemplatePceReport_Type(Integer32):
    """Custom type vRtrMplsLspTemplatePceReport based on Integer32"""
    defaultValue = 3

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
          ("disable", 2),
          ("inherit", 3))
    )


_VRtrMplsLspTemplatePceReport_Type.__name__ = "Integer32"
_VRtrMplsLspTemplatePceReport_Object = MibTableColumn
vRtrMplsLspTemplatePceReport = _VRtrMplsLspTemplatePceReport_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 54),
    _VRtrMplsLspTemplatePceReport_Type()
)
vRtrMplsLspTemplatePceReport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTemplatePceReport.setStatus("current")


class _VRtrMplsLspTempBfdFailureAction_Type(Integer32):
    """Custom type vRtrMplsLspTempBfdFailureAction based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("down", 1))
    )


_VRtrMplsLspTempBfdFailureAction_Type.__name__ = "Integer32"
_VRtrMplsLspTempBfdFailureAction_Object = MibTableColumn
vRtrMplsLspTempBfdFailureAction = _VRtrMplsLspTempBfdFailureAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 41, 1, 57),
    _VRtrMplsLspTempBfdFailureAction_Type()
)
vRtrMplsLspTempBfdFailureAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTempBfdFailureAction.setStatus("current")
_VRtrMplsLspAutoBWTableLastChg_Type = TimeStamp
_VRtrMplsLspAutoBWTableLastChg_Object = MibScalar
vRtrMplsLspAutoBWTableLastChg = _VRtrMplsLspAutoBWTableLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 42),
    _VRtrMplsLspAutoBWTableLastChg_Type()
)
vRtrMplsLspAutoBWTableLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWTableLastChg.setStatus("current")
_VRtrMplsLspAutoBandwidthTable_Object = MibTable
vRtrMplsLspAutoBandwidthTable = _VRtrMplsLspAutoBandwidthTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 43)
)
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBandwidthTable.setStatus("current")
_VRtrMplsLspAutoBandwidthEntry_Object = MibTableRow
vRtrMplsLspAutoBandwidthEntry = _VRtrMplsLspAutoBandwidthEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 43, 1)
)
vRtrMplsLspAutoBandwidthEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsLspAutoBWLspName"),
)
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBandwidthEntry.setStatus("current")
_VRtrMplsLspAutoBWLspName_Type = TLNamedItem
_VRtrMplsLspAutoBWLspName_Object = MibTableColumn
vRtrMplsLspAutoBWLspName = _VRtrMplsLspAutoBWLspName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 43, 1, 1),
    _VRtrMplsLspAutoBWLspName_Type()
)
vRtrMplsLspAutoBWLspName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWLspName.setStatus("current")
_VRtrMplsLspAutoBWLastChange_Type = TimeStamp
_VRtrMplsLspAutoBWLastChange_Object = MibTableColumn
vRtrMplsLspAutoBWLastChange = _VRtrMplsLspAutoBWLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 43, 1, 2),
    _VRtrMplsLspAutoBWLastChange_Type()
)
vRtrMplsLspAutoBWLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWLastChange.setStatus("current")


class _VRtrMplsLspAutoBWAdjDNPercent_Type(Unsigned32):
    """Custom type vRtrMplsLspAutoBWAdjDNPercent based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VRtrMplsLspAutoBWAdjDNPercent_Type.__name__ = "Unsigned32"
_VRtrMplsLspAutoBWAdjDNPercent_Object = MibTableColumn
vRtrMplsLspAutoBWAdjDNPercent = _VRtrMplsLspAutoBWAdjDNPercent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 43, 1, 3),
    _VRtrMplsLspAutoBWAdjDNPercent_Type()
)
vRtrMplsLspAutoBWAdjDNPercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWAdjDNPercent.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWAdjDNPercent.setUnits("percent")


class _VRtrMplsLspAutoBWAdjDNMbps_Type(Unsigned32):
    """Custom type vRtrMplsLspAutoBWAdjDNMbps based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_VRtrMplsLspAutoBWAdjDNMbps_Type.__name__ = "Unsigned32"
_VRtrMplsLspAutoBWAdjDNMbps_Object = MibTableColumn
vRtrMplsLspAutoBWAdjDNMbps = _VRtrMplsLspAutoBWAdjDNMbps_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 43, 1, 4),
    _VRtrMplsLspAutoBWAdjDNMbps_Type()
)
vRtrMplsLspAutoBWAdjDNMbps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWAdjDNMbps.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWAdjDNMbps.setUnits("Mbps")


class _VRtrMplsLspAutoBWAdjMultiplier_Type(Unsigned32):
    """Custom type vRtrMplsLspAutoBWAdjMultiplier based on Unsigned32"""
    defaultValue = 288

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16383),
    )


_VRtrMplsLspAutoBWAdjMultiplier_Type.__name__ = "Unsigned32"
_VRtrMplsLspAutoBWAdjMultiplier_Object = MibTableColumn
vRtrMplsLspAutoBWAdjMultiplier = _VRtrMplsLspAutoBWAdjMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 43, 1, 5),
    _VRtrMplsLspAutoBWAdjMultiplier_Type()
)
vRtrMplsLspAutoBWAdjMultiplier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWAdjMultiplier.setStatus("current")


class _VRtrMplsLspAutoBWAdjUPPercent_Type(Unsigned32):
    """Custom type vRtrMplsLspAutoBWAdjUPPercent based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VRtrMplsLspAutoBWAdjUPPercent_Type.__name__ = "Unsigned32"
_VRtrMplsLspAutoBWAdjUPPercent_Object = MibTableColumn
vRtrMplsLspAutoBWAdjUPPercent = _VRtrMplsLspAutoBWAdjUPPercent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 43, 1, 6),
    _VRtrMplsLspAutoBWAdjUPPercent_Type()
)
vRtrMplsLspAutoBWAdjUPPercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWAdjUPPercent.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWAdjUPPercent.setUnits("percent")


class _VRtrMplsLspAutoBWAdjUPMbps_Type(Unsigned32):
    """Custom type vRtrMplsLspAutoBWAdjUPMbps based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_VRtrMplsLspAutoBWAdjUPMbps_Type.__name__ = "Unsigned32"
_VRtrMplsLspAutoBWAdjUPMbps_Object = MibTableColumn
vRtrMplsLspAutoBWAdjUPMbps = _VRtrMplsLspAutoBWAdjUPMbps_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 43, 1, 7),
    _VRtrMplsLspAutoBWAdjUPMbps_Type()
)
vRtrMplsLspAutoBWAdjUPMbps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWAdjUPMbps.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWAdjUPMbps.setUnits("Mbps")


class _VRtrMplsLspAutoBWMaxBW_Type(Unsigned32):
    """Custom type vRtrMplsLspAutoBWMaxBW based on Unsigned32"""
    defaultValue = 100000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_VRtrMplsLspAutoBWMaxBW_Type.__name__ = "Unsigned32"
_VRtrMplsLspAutoBWMaxBW_Object = MibTableColumn
vRtrMplsLspAutoBWMaxBW = _VRtrMplsLspAutoBWMaxBW_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 43, 1, 8),
    _VRtrMplsLspAutoBWMaxBW_Type()
)
vRtrMplsLspAutoBWMaxBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWMaxBW.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWMaxBW.setUnits("Mbps")


class _VRtrMplsLspAutoBWMinBW_Type(Unsigned32):
    """Custom type vRtrMplsLspAutoBWMinBW based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_VRtrMplsLspAutoBWMinBW_Type.__name__ = "Unsigned32"
_VRtrMplsLspAutoBWMinBW_Object = MibTableColumn
vRtrMplsLspAutoBWMinBW = _VRtrMplsLspAutoBWMinBW_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 43, 1, 9),
    _VRtrMplsLspAutoBWMinBW_Type()
)
vRtrMplsLspAutoBWMinBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWMinBW.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWMinBW.setUnits("Mbps")


class _VRtrMplsLspAutoBWMonitorBW_Type(TruthValue):
    """Custom type vRtrMplsLspAutoBWMonitorBW based on TruthValue"""
    defaultValue = 2


_VRtrMplsLspAutoBWMonitorBW_Type.__name__ = "TruthValue"
_VRtrMplsLspAutoBWMonitorBW_Object = MibTableColumn
vRtrMplsLspAutoBWMonitorBW = _VRtrMplsLspAutoBWMonitorBW_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 43, 1, 10),
    _VRtrMplsLspAutoBWMonitorBW_Type()
)
vRtrMplsLspAutoBWMonitorBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWMonitorBW.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWMonitorBW.setUnits("Mbps")


class _VRtrMplsLspAutoBWOverFlow_Type(Unsigned32):
    """Custom type vRtrMplsLspAutoBWOverFlow based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 10),
    )


_VRtrMplsLspAutoBWOverFlow_Type.__name__ = "Unsigned32"
_VRtrMplsLspAutoBWOverFlow_Object = MibTableColumn
vRtrMplsLspAutoBWOverFlow = _VRtrMplsLspAutoBWOverFlow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 43, 1, 11),
    _VRtrMplsLspAutoBWOverFlow_Type()
)
vRtrMplsLspAutoBWOverFlow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWOverFlow.setStatus("current")


class _VRtrMplsLspAutoBWOvrFlwThreshold_Type(Unsigned32):
    """Custom type vRtrMplsLspAutoBWOvrFlwThreshold based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 100),
    )


_VRtrMplsLspAutoBWOvrFlwThreshold_Type.__name__ = "Unsigned32"
_VRtrMplsLspAutoBWOvrFlwThreshold_Object = MibTableColumn
vRtrMplsLspAutoBWOvrFlwThreshold = _VRtrMplsLspAutoBWOvrFlwThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 43, 1, 12),
    _VRtrMplsLspAutoBWOvrFlwThreshold_Type()
)
vRtrMplsLspAutoBWOvrFlwThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWOvrFlwThreshold.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWOvrFlwThreshold.setUnits("percent")


class _VRtrMplsLspAutoBWOvrFlwBW_Type(Unsigned32):
    """Custom type vRtrMplsLspAutoBWOvrFlwBW based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_VRtrMplsLspAutoBWOvrFlwBW_Type.__name__ = "Unsigned32"
_VRtrMplsLspAutoBWOvrFlwBW_Object = MibTableColumn
vRtrMplsLspAutoBWOvrFlwBW = _VRtrMplsLspAutoBWOvrFlwBW_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 43, 1, 13),
    _VRtrMplsLspAutoBWOvrFlwBW_Type()
)
vRtrMplsLspAutoBWOvrFlwBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWOvrFlwBW.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWOvrFlwBW.setUnits("Mbps")


class _VRtrMplsLspAutoBWSampMultiplier_Type(Unsigned32):
    """Custom type vRtrMplsLspAutoBWSampMultiplier based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 511),
    )


_VRtrMplsLspAutoBWSampMultiplier_Type.__name__ = "Unsigned32"
_VRtrMplsLspAutoBWSampMultiplier_Object = MibTableColumn
vRtrMplsLspAutoBWSampMultiplier = _VRtrMplsLspAutoBWSampMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 43, 1, 14),
    _VRtrMplsLspAutoBWSampMultiplier_Type()
)
vRtrMplsLspAutoBWSampMultiplier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWSampMultiplier.setStatus("current")
_VRtrMplsLspAutoBWSampTime_Type = Unsigned32
_VRtrMplsLspAutoBWSampTime_Object = MibTableColumn
vRtrMplsLspAutoBWSampTime = _VRtrMplsLspAutoBWSampTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 43, 1, 15),
    _VRtrMplsLspAutoBWSampTime_Type()
)
vRtrMplsLspAutoBWSampTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWSampTime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWSampTime.setUnits("minutes")
_VRtrMplsLspAutoBWLastAdj_Type = TimeStamp
_VRtrMplsLspAutoBWLastAdj_Object = MibTableColumn
vRtrMplsLspAutoBWLastAdj = _VRtrMplsLspAutoBWLastAdj_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 43, 1, 16),
    _VRtrMplsLspAutoBWLastAdj_Type()
)
vRtrMplsLspAutoBWLastAdj.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWLastAdj.setStatus("current")
_VRtrMplsLspAutoBWLastAdjCause_Type = TmnxMplsLspAutoBWLastAdjCause
_VRtrMplsLspAutoBWLastAdjCause_Object = MibTableColumn
vRtrMplsLspAutoBWLastAdjCause = _VRtrMplsLspAutoBWLastAdjCause_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 43, 1, 17),
    _VRtrMplsLspAutoBWLastAdjCause_Type()
)
vRtrMplsLspAutoBWLastAdjCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWLastAdjCause.setStatus("current")
_VRtrMplsLspAutoBWNextAdj_Type = Unsigned32
_VRtrMplsLspAutoBWNextAdj_Object = MibTableColumn
vRtrMplsLspAutoBWNextAdj = _VRtrMplsLspAutoBWNextAdj_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 43, 1, 18),
    _VRtrMplsLspAutoBWNextAdj_Type()
)
vRtrMplsLspAutoBWNextAdj.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWNextAdj.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWNextAdj.setUnits("minutes")
_VRtrMplsLspAutoBWMaxAvgRate_Type = Unsigned32
_VRtrMplsLspAutoBWMaxAvgRate_Object = MibTableColumn
vRtrMplsLspAutoBWMaxAvgRate = _VRtrMplsLspAutoBWMaxAvgRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 43, 1, 19),
    _VRtrMplsLspAutoBWMaxAvgRate_Type()
)
vRtrMplsLspAutoBWMaxAvgRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWMaxAvgRate.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWMaxAvgRate.setUnits("Mbps")
_VRtrMplsLspAutoBWLastAvgRate_Type = Unsigned32
_VRtrMplsLspAutoBWLastAvgRate_Object = MibTableColumn
vRtrMplsLspAutoBWLastAvgRate = _VRtrMplsLspAutoBWLastAvgRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 43, 1, 20),
    _VRtrMplsLspAutoBWLastAvgRate_Type()
)
vRtrMplsLspAutoBWLastAvgRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWLastAvgRate.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWLastAvgRate.setUnits("Mbps")


class _VRtrMplsLspAutoBWInheritance_Type(Unsigned32):
    """Custom type vRtrMplsLspAutoBWInheritance based on Unsigned32"""
    defaultValue = 0


_VRtrMplsLspAutoBWInheritance_Type.__name__ = "Unsigned32"
_VRtrMplsLspAutoBWInheritance_Object = MibTableColumn
vRtrMplsLspAutoBWInheritance = _VRtrMplsLspAutoBWInheritance_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 43, 1, 21),
    _VRtrMplsLspAutoBWInheritance_Type()
)
vRtrMplsLspAutoBWInheritance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWInheritance.setStatus("current")
_VRtrMplsLspAutoBWCurrentBW_Type = Unsigned32
_VRtrMplsLspAutoBWCurrentBW_Object = MibTableColumn
vRtrMplsLspAutoBWCurrentBW = _VRtrMplsLspAutoBWCurrentBW_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 43, 1, 22),
    _VRtrMplsLspAutoBWCurrentBW_Type()
)
vRtrMplsLspAutoBWCurrentBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWCurrentBW.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWCurrentBW.setUnits("Mbps")
_VRtrMplsLspAutoBWAdjTime_Type = Unsigned32
_VRtrMplsLspAutoBWAdjTime_Object = MibTableColumn
vRtrMplsLspAutoBWAdjTime = _VRtrMplsLspAutoBWAdjTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 43, 1, 23),
    _VRtrMplsLspAutoBWAdjTime_Type()
)
vRtrMplsLspAutoBWAdjTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWAdjTime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWAdjTime.setUnits("minutes")
_VRtrMplsLspAutoBWOvrFlwCount_Type = Unsigned32
_VRtrMplsLspAutoBWOvrFlwCount_Object = MibTableColumn
vRtrMplsLspAutoBWOvrFlwCount = _VRtrMplsLspAutoBWOvrFlwCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 43, 1, 24),
    _VRtrMplsLspAutoBWOvrFlwCount_Type()
)
vRtrMplsLspAutoBWOvrFlwCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWOvrFlwCount.setStatus("current")
_VRtrMplsLspAutoBWSampCount_Type = Unsigned32
_VRtrMplsLspAutoBWSampCount_Object = MibTableColumn
vRtrMplsLspAutoBWSampCount = _VRtrMplsLspAutoBWSampCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 43, 1, 25),
    _VRtrMplsLspAutoBWSampCount_Type()
)
vRtrMplsLspAutoBWSampCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWSampCount.setStatus("current")
_VRtrMplsLspAutoBWAdjCount_Type = Unsigned32
_VRtrMplsLspAutoBWAdjCount_Object = MibTableColumn
vRtrMplsLspAutoBWAdjCount = _VRtrMplsLspAutoBWAdjCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 43, 1, 26),
    _VRtrMplsLspAutoBWAdjCount_Type()
)
vRtrMplsLspAutoBWAdjCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWAdjCount.setStatus("current")
_VRtrMplsLspAutoBWOperState_Type = TmnxEnabledDisabled
_VRtrMplsLspAutoBWOperState_Object = MibTableColumn
vRtrMplsLspAutoBWOperState = _VRtrMplsLspAutoBWOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 43, 1, 27),
    _VRtrMplsLspAutoBWOperState_Type()
)
vRtrMplsLspAutoBWOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWOperState.setStatus("current")
_VRtrMplsLspAutoBWSampInterval_Type = Unsigned32
_VRtrMplsLspAutoBWSampInterval_Object = MibTableColumn
vRtrMplsLspAutoBWSampInterval = _VRtrMplsLspAutoBWSampInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 43, 1, 28),
    _VRtrMplsLspAutoBWSampInterval_Type()
)
vRtrMplsLspAutoBWSampInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWSampInterval.setStatus("current")


class _VRtrMplsLspAutoBWBeWeight_Type(Unsigned32):
    """Custom type vRtrMplsLspAutoBWBeWeight based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VRtrMplsLspAutoBWBeWeight_Type.__name__ = "Unsigned32"
_VRtrMplsLspAutoBWBeWeight_Object = MibTableColumn
vRtrMplsLspAutoBWBeWeight = _VRtrMplsLspAutoBWBeWeight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 43, 1, 29),
    _VRtrMplsLspAutoBWBeWeight_Type()
)
vRtrMplsLspAutoBWBeWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWBeWeight.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWBeWeight.setUnits("percent")


class _VRtrMplsLspAutoBWL2Weight_Type(Unsigned32):
    """Custom type vRtrMplsLspAutoBWL2Weight based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VRtrMplsLspAutoBWL2Weight_Type.__name__ = "Unsigned32"
_VRtrMplsLspAutoBWL2Weight_Object = MibTableColumn
vRtrMplsLspAutoBWL2Weight = _VRtrMplsLspAutoBWL2Weight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 43, 1, 30),
    _VRtrMplsLspAutoBWL2Weight_Type()
)
vRtrMplsLspAutoBWL2Weight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWL2Weight.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWL2Weight.setUnits("percent")


class _VRtrMplsLspAutoBWAfWeight_Type(Unsigned32):
    """Custom type vRtrMplsLspAutoBWAfWeight based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VRtrMplsLspAutoBWAfWeight_Type.__name__ = "Unsigned32"
_VRtrMplsLspAutoBWAfWeight_Object = MibTableColumn
vRtrMplsLspAutoBWAfWeight = _VRtrMplsLspAutoBWAfWeight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 43, 1, 31),
    _VRtrMplsLspAutoBWAfWeight_Type()
)
vRtrMplsLspAutoBWAfWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWAfWeight.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWAfWeight.setUnits("percent")


class _VRtrMplsLspAutoBWL1Weight_Type(Unsigned32):
    """Custom type vRtrMplsLspAutoBWL1Weight based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VRtrMplsLspAutoBWL1Weight_Type.__name__ = "Unsigned32"
_VRtrMplsLspAutoBWL1Weight_Object = MibTableColumn
vRtrMplsLspAutoBWL1Weight = _VRtrMplsLspAutoBWL1Weight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 43, 1, 32),
    _VRtrMplsLspAutoBWL1Weight_Type()
)
vRtrMplsLspAutoBWL1Weight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWL1Weight.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWL1Weight.setUnits("percent")


class _VRtrMplsLspAutoBWH2Weight_Type(Unsigned32):
    """Custom type vRtrMplsLspAutoBWH2Weight based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VRtrMplsLspAutoBWH2Weight_Type.__name__ = "Unsigned32"
_VRtrMplsLspAutoBWH2Weight_Object = MibTableColumn
vRtrMplsLspAutoBWH2Weight = _VRtrMplsLspAutoBWH2Weight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 43, 1, 33),
    _VRtrMplsLspAutoBWH2Weight_Type()
)
vRtrMplsLspAutoBWH2Weight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWH2Weight.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWH2Weight.setUnits("percent")


class _VRtrMplsLspAutoBWEfWeight_Type(Unsigned32):
    """Custom type vRtrMplsLspAutoBWEfWeight based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VRtrMplsLspAutoBWEfWeight_Type.__name__ = "Unsigned32"
_VRtrMplsLspAutoBWEfWeight_Object = MibTableColumn
vRtrMplsLspAutoBWEfWeight = _VRtrMplsLspAutoBWEfWeight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 43, 1, 34),
    _VRtrMplsLspAutoBWEfWeight_Type()
)
vRtrMplsLspAutoBWEfWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWEfWeight.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWEfWeight.setUnits("percent")


class _VRtrMplsLspAutoBWH1Weight_Type(Unsigned32):
    """Custom type vRtrMplsLspAutoBWH1Weight based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VRtrMplsLspAutoBWH1Weight_Type.__name__ = "Unsigned32"
_VRtrMplsLspAutoBWH1Weight_Object = MibTableColumn
vRtrMplsLspAutoBWH1Weight = _VRtrMplsLspAutoBWH1Weight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 43, 1, 35),
    _VRtrMplsLspAutoBWH1Weight_Type()
)
vRtrMplsLspAutoBWH1Weight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWH1Weight.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWH1Weight.setUnits("percent")


class _VRtrMplsLspAutoBWNcWeight_Type(Unsigned32):
    """Custom type vRtrMplsLspAutoBWNcWeight based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VRtrMplsLspAutoBWNcWeight_Type.__name__ = "Unsigned32"
_VRtrMplsLspAutoBWNcWeight_Object = MibTableColumn
vRtrMplsLspAutoBWNcWeight = _VRtrMplsLspAutoBWNcWeight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 43, 1, 36),
    _VRtrMplsLspAutoBWNcWeight_Type()
)
vRtrMplsLspAutoBWNcWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWNcWeight.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWNcWeight.setUnits("percent")


class _VRtrMplsLspAutoBWUnderFlow_Type(Unsigned32):
    """Custom type vRtrMplsLspAutoBWUnderFlow based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 10),
    )


_VRtrMplsLspAutoBWUnderFlow_Type.__name__ = "Unsigned32"
_VRtrMplsLspAutoBWUnderFlow_Object = MibTableColumn
vRtrMplsLspAutoBWUnderFlow = _VRtrMplsLspAutoBWUnderFlow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 43, 1, 37),
    _VRtrMplsLspAutoBWUnderFlow_Type()
)
vRtrMplsLspAutoBWUnderFlow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWUnderFlow.setStatus("current")


class _VRtrMplsLspAutoBWUndFlwThreshold_Type(Unsigned32):
    """Custom type vRtrMplsLspAutoBWUndFlwThreshold based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 100),
    )


_VRtrMplsLspAutoBWUndFlwThreshold_Type.__name__ = "Unsigned32"
_VRtrMplsLspAutoBWUndFlwThreshold_Object = MibTableColumn
vRtrMplsLspAutoBWUndFlwThreshold = _VRtrMplsLspAutoBWUndFlwThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 43, 1, 38),
    _VRtrMplsLspAutoBWUndFlwThreshold_Type()
)
vRtrMplsLspAutoBWUndFlwThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWUndFlwThreshold.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWUndFlwThreshold.setUnits("percent")


class _VRtrMplsLspAutoBWUndFlwBW_Type(Unsigned32):
    """Custom type vRtrMplsLspAutoBWUndFlwBW based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_VRtrMplsLspAutoBWUndFlwBW_Type.__name__ = "Unsigned32"
_VRtrMplsLspAutoBWUndFlwBW_Object = MibTableColumn
vRtrMplsLspAutoBWUndFlwBW = _VRtrMplsLspAutoBWUndFlwBW_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 43, 1, 39),
    _VRtrMplsLspAutoBWUndFlwBW_Type()
)
vRtrMplsLspAutoBWUndFlwBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWUndFlwBW.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWUndFlwBW.setUnits("Mbps")
_VRtrMplsLspAutoBWUndFlwCount_Type = Counter32
_VRtrMplsLspAutoBWUndFlwCount_Object = MibTableColumn
vRtrMplsLspAutoBWUndFlwCount = _VRtrMplsLspAutoBWUndFlwCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 43, 1, 40),
    _VRtrMplsLspAutoBWUndFlwCount_Type()
)
vRtrMplsLspAutoBWUndFlwCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWUndFlwCount.setStatus("current")
_VRtrMplsLspAutoBWMaxUndFlwBw_Type = Unsigned32
_VRtrMplsLspAutoBWMaxUndFlwBw_Object = MibTableColumn
vRtrMplsLspAutoBWMaxUndFlwBw = _VRtrMplsLspAutoBWMaxUndFlwBw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 43, 1, 41),
    _VRtrMplsLspAutoBWMaxUndFlwBw_Type()
)
vRtrMplsLspAutoBWMaxUndFlwBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWMaxUndFlwBw.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBWMaxUndFlwBw.setUnits("Mbps")
_VRtrMplsLspPathOperTable_Object = MibTable
vRtrMplsLspPathOperTable = _VRtrMplsLspPathOperTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 44)
)
if mibBuilder.loadTexts:
    vRtrMplsLspPathOperTable.setStatus("current")
_VRtrMplsLspPathOperEntry_Object = MibTableRow
vRtrMplsLspPathOperEntry = _VRtrMplsLspPathOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 44, 1)
)
if mibBuilder.loadTexts:
    vRtrMplsLspPathOperEntry.setStatus("current")


class _VRtrMplsLspPathOperSetupPriority_Type(Unsigned32):
    """Custom type vRtrMplsLspPathOperSetupPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_VRtrMplsLspPathOperSetupPriority_Type.__name__ = "Unsigned32"
_VRtrMplsLspPathOperSetupPriority_Object = MibTableColumn
vRtrMplsLspPathOperSetupPriority = _VRtrMplsLspPathOperSetupPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 44, 1, 1),
    _VRtrMplsLspPathOperSetupPriority_Type()
)
vRtrMplsLspPathOperSetupPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathOperSetupPriority.setStatus("current")


class _VRtrMplsLspPathOperHoldPriority_Type(Unsigned32):
    """Custom type vRtrMplsLspPathOperHoldPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_VRtrMplsLspPathOperHoldPriority_Type.__name__ = "Unsigned32"
_VRtrMplsLspPathOperHoldPriority_Object = MibTableColumn
vRtrMplsLspPathOperHoldPriority = _VRtrMplsLspPathOperHoldPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 44, 1, 2),
    _VRtrMplsLspPathOperHoldPriority_Type()
)
vRtrMplsLspPathOperHoldPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathOperHoldPriority.setStatus("current")


class _VRtrMplsLspPathOperRecord_Type(Integer32):
    """Custom type vRtrMplsLspPathOperRecord based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("record", 1),
          ("noRecord", 2))
    )


_VRtrMplsLspPathOperRecord_Type.__name__ = "Integer32"
_VRtrMplsLspPathOperRecord_Object = MibTableColumn
vRtrMplsLspPathOperRecord = _VRtrMplsLspPathOperRecord_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 44, 1, 3),
    _VRtrMplsLspPathOperRecord_Type()
)
vRtrMplsLspPathOperRecord.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathOperRecord.setStatus("current")


class _VRtrMplsLspPathOperRecordLabel_Type(Integer32):
    """Custom type vRtrMplsLspPathOperRecordLabel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("record", 1),
          ("noRecord", 2))
    )


_VRtrMplsLspPathOperRecordLabel_Type.__name__ = "Integer32"
_VRtrMplsLspPathOperRecordLabel_Object = MibTableColumn
vRtrMplsLspPathOperRecordLabel = _VRtrMplsLspPathOperRecordLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 44, 1, 4),
    _VRtrMplsLspPathOperRecordLabel_Type()
)
vRtrMplsLspPathOperRecordLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathOperRecordLabel.setStatus("current")


class _VRtrMplsLspPathOperHopLimit_Type(Unsigned32):
    """Custom type vRtrMplsLspPathOperHopLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 255),
    )


_VRtrMplsLspPathOperHopLimit_Type.__name__ = "Unsigned32"
_VRtrMplsLspPathOperHopLimit_Object = MibTableColumn
vRtrMplsLspPathOperHopLimit = _VRtrMplsLspPathOperHopLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 44, 1, 5),
    _VRtrMplsLspPathOperHopLimit_Type()
)
vRtrMplsLspPathOperHopLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathOperHopLimit.setStatus("current")
_VRtrMplsLspPathOperAdminGrpIncl_Type = Unsigned32
_VRtrMplsLspPathOperAdminGrpIncl_Object = MibTableColumn
vRtrMplsLspPathOperAdminGrpIncl = _VRtrMplsLspPathOperAdminGrpIncl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 44, 1, 6),
    _VRtrMplsLspPathOperAdminGrpIncl_Type()
)
vRtrMplsLspPathOperAdminGrpIncl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathOperAdminGrpIncl.setStatus("current")
_VRtrMplsLspPathOperAdminGrExcld_Type = Unsigned32
_VRtrMplsLspPathOperAdminGrExcld_Object = MibTableColumn
vRtrMplsLspPathOperAdminGrExcld = _VRtrMplsLspPathOperAdminGrExcld_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 44, 1, 7),
    _VRtrMplsLspPathOperAdminGrExcld_Type()
)
vRtrMplsLspPathOperAdminGrExcld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathOperAdminGrExcld.setStatus("current")
_VRtrMplsLspPathOperCspf_Type = TruthValue
_VRtrMplsLspPathOperCspf_Object = MibTableColumn
vRtrMplsLspPathOperCspf = _VRtrMplsLspPathOperCspf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 44, 1, 8),
    _VRtrMplsLspPathOperCspf_Type()
)
vRtrMplsLspPathOperCspf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathOperCspf.setStatus("current")
_VRtrMplsLspPathOperCspfToFrstLs_Type = TruthValue
_VRtrMplsLspPathOperCspfToFrstLs_Object = MibTableColumn
vRtrMplsLspPathOperCspfToFrstLs = _VRtrMplsLspPathOperCspfToFrstLs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 44, 1, 9),
    _VRtrMplsLspPathOperCspfToFrstLs_Type()
)
vRtrMplsLspPathOperCspfToFrstLs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathOperCspfToFrstLs.setStatus("obsolete")
_VRtrMplsLspPathOperLeastFill_Type = TruthValue
_VRtrMplsLspPathOperLeastFill_Object = MibTableColumn
vRtrMplsLspPathOperLeastFill = _VRtrMplsLspPathOperLeastFill_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 44, 1, 10),
    _VRtrMplsLspPathOperLeastFill_Type()
)
vRtrMplsLspPathOperLeastFill.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathOperLeastFill.setStatus("current")
_VRtrMplsLspPathOperRsvpAdspec_Type = TruthValue
_VRtrMplsLspPathOperRsvpAdspec_Object = MibTableColumn
vRtrMplsLspPathOperRsvpAdspec = _VRtrMplsLspPathOperRsvpAdspec_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 44, 1, 11),
    _VRtrMplsLspPathOperRsvpAdspec_Type()
)
vRtrMplsLspPathOperRsvpAdspec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathOperRsvpAdspec.setStatus("current")
_VRtrMplsLspPathOperFRNodeProtect_Type = TruthValue
_VRtrMplsLspPathOperFRNodeProtect_Object = MibTableColumn
vRtrMplsLspPathOperFRNodeProtect = _VRtrMplsLspPathOperFRNodeProtect_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 44, 1, 12),
    _VRtrMplsLspPathOperFRNodeProtect_Type()
)
vRtrMplsLspPathOperFRNodeProtect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathOperFRNodeProtect.setStatus("current")
_VRtrMplsLspPathOperPropAdminGrp_Type = TruthValue
_VRtrMplsLspPathOperPropAdminGrp_Object = MibTableColumn
vRtrMplsLspPathOperPropAdminGrp = _VRtrMplsLspPathOperPropAdminGrp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 44, 1, 13),
    _VRtrMplsLspPathOperPropAdminGrp_Type()
)
vRtrMplsLspPathOperPropAdminGrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathOperPropAdminGrp.setStatus("current")


class _VRtrMplsLspPathOperFRHopLimit_Type(Unsigned32):
    """Custom type vRtrMplsLspPathOperFRHopLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VRtrMplsLspPathOperFRHopLimit_Type.__name__ = "Unsigned32"
_VRtrMplsLspPathOperFRHopLimit_Object = MibTableColumn
vRtrMplsLspPathOperFRHopLimit = _VRtrMplsLspPathOperFRHopLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 44, 1, 14),
    _VRtrMplsLspPathOperFRHopLimit_Type()
)
vRtrMplsLspPathOperFRHopLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathOperFRHopLimit.setStatus("current")
_VRtrMplsLspPathOperFRPropAdmGrp_Type = TruthValue
_VRtrMplsLspPathOperFRPropAdmGrp_Object = MibTableColumn
vRtrMplsLspPathOperFRPropAdmGrp = _VRtrMplsLspPathOperFRPropAdmGrp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 44, 1, 15),
    _VRtrMplsLspPathOperFRPropAdmGrp_Type()
)
vRtrMplsLspPathOperFRPropAdmGrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathOperFRPropAdmGrp.setStatus("current")
_VRtrMplsLspPathOperInterArea_Type = TruthValue
_VRtrMplsLspPathOperInterArea_Object = MibTableColumn
vRtrMplsLspPathOperInterArea = _VRtrMplsLspPathOperInterArea_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 44, 1, 16),
    _VRtrMplsLspPathOperInterArea_Type()
)
vRtrMplsLspPathOperInterArea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathOperInterArea.setStatus("current")
_VRtrMplsLabelObjs_ObjectIdentity = ObjectIdentity
vRtrMplsLabelObjs = _VRtrMplsLabelObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 45)
)


class _VRtrMplsLabelMaxStaticLspLabels_Type(Unsigned32):
    """Custom type vRtrMplsLabelMaxStaticLspLabels based on Unsigned32"""
    defaultValue = 2016

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 262112),
    )


_VRtrMplsLabelMaxStaticLspLabels_Type.__name__ = "Unsigned32"
_VRtrMplsLabelMaxStaticLspLabels_Object = MibScalar
vRtrMplsLabelMaxStaticLspLabels = _VRtrMplsLabelMaxStaticLspLabels_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 45, 1),
    _VRtrMplsLabelMaxStaticLspLabels_Type()
)
vRtrMplsLabelMaxStaticLspLabels.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLabelMaxStaticLspLabels.setStatus("obsolete")


class _VRtrMplsLabelMaxStaticSvcLabels_Type(Unsigned32):
    """Custom type vRtrMplsLabelMaxStaticSvcLabels based on Unsigned32"""
    defaultValue = 16384

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 262112),
    )


_VRtrMplsLabelMaxStaticSvcLabels_Type.__name__ = "Unsigned32"
_VRtrMplsLabelMaxStaticSvcLabels_Object = MibScalar
vRtrMplsLabelMaxStaticSvcLabels = _VRtrMplsLabelMaxStaticSvcLabels_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 45, 2),
    _VRtrMplsLabelMaxStaticSvcLabels_Type()
)
vRtrMplsLabelMaxStaticSvcLabels.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLabelMaxStaticSvcLabels.setStatus("obsolete")


class _VRtrMplsLabelBgpLabelsHoldTimer_Type(Unsigned32):
    """Custom type vRtrMplsLabelBgpLabelsHoldTimer based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VRtrMplsLabelBgpLabelsHoldTimer_Type.__name__ = "Unsigned32"
_VRtrMplsLabelBgpLabelsHoldTimer_Object = MibScalar
vRtrMplsLabelBgpLabelsHoldTimer = _VRtrMplsLabelBgpLabelsHoldTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 45, 3),
    _VRtrMplsLabelBgpLabelsHoldTimer_Type()
)
vRtrMplsLabelBgpLabelsHoldTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLabelBgpLabelsHoldTimer.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLabelBgpLabelsHoldTimer.setUnits("seconds")


class _VRtrMplsLabelSegRouteStartLabel_Type(Unsigned32):
    """Custom type vRtrMplsLabelSegRouteStartLabel based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(32, 524287),
    )


_VRtrMplsLabelSegRouteStartLabel_Type.__name__ = "Unsigned32"
_VRtrMplsLabelSegRouteStartLabel_Object = MibScalar
vRtrMplsLabelSegRouteStartLabel = _VRtrMplsLabelSegRouteStartLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 45, 4),
    _VRtrMplsLabelSegRouteStartLabel_Type()
)
vRtrMplsLabelSegRouteStartLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLabelSegRouteStartLabel.setStatus("current")


class _VRtrMplsLabelSegRouteEndLabel_Type(Unsigned32):
    """Custom type vRtrMplsLabelSegRouteEndLabel based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(32, 524287),
    )


_VRtrMplsLabelSegRouteEndLabel_Type.__name__ = "Unsigned32"
_VRtrMplsLabelSegRouteEndLabel_Object = MibScalar
vRtrMplsLabelSegRouteEndLabel = _VRtrMplsLabelSegRouteEndLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 45, 5),
    _VRtrMplsLabelSegRouteEndLabel_Type()
)
vRtrMplsLabelSegRouteEndLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLabelSegRouteEndLabel.setStatus("current")


class _VRtrMplsLabelStaticLabelRange_Type(Unsigned32):
    """Custom type vRtrMplsLabelStaticLabelRange based on Unsigned32"""
    defaultValue = 18400

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 262112),
    )


_VRtrMplsLabelStaticLabelRange_Type.__name__ = "Unsigned32"
_VRtrMplsLabelStaticLabelRange_Object = MibScalar
vRtrMplsLabelStaticLabelRange = _VRtrMplsLabelStaticLabelRange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 45, 6),
    _VRtrMplsLabelStaticLabelRange_Type()
)
vRtrMplsLabelStaticLabelRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLabelStaticLabelRange.setStatus("current")
_VRtrMplsLspTempAutoBWTblLastChg_Type = TimeStamp
_VRtrMplsLspTempAutoBWTblLastChg_Object = MibScalar
vRtrMplsLspTempAutoBWTblLastChg = _VRtrMplsLspTempAutoBWTblLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 46),
    _VRtrMplsLspTempAutoBWTblLastChg_Type()
)
vRtrMplsLspTempAutoBWTblLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAutoBWTblLastChg.setStatus("current")
_VRtrMplsLspTempAutoBWTable_Object = MibTable
vRtrMplsLspTempAutoBWTable = _VRtrMplsLspTempAutoBWTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 47)
)
if mibBuilder.loadTexts:
    vRtrMplsLspTempAutoBWTable.setStatus("current")
_VRtrMplsLspTempAutoBWEntry_Object = MibTableRow
vRtrMplsLspTempAutoBWEntry = _VRtrMplsLspTempAutoBWEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 47, 1)
)
vRtrMplsLspTempAutoBWEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateName"),
)
if mibBuilder.loadTexts:
    vRtrMplsLspTempAutoBWEntry.setStatus("current")
_VRtrMplsLspTempAutoBWLastChg_Type = TimeStamp
_VRtrMplsLspTempAutoBWLastChg_Object = MibTableColumn
vRtrMplsLspTempAutoBWLastChg = _VRtrMplsLspTempAutoBWLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 47, 1, 1),
    _VRtrMplsLspTempAutoBWLastChg_Type()
)
vRtrMplsLspTempAutoBWLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAutoBWLastChg.setStatus("current")


class _VRtrMplsLspTempAutoBWAdjDNPer_Type(Unsigned32):
    """Custom type vRtrMplsLspTempAutoBWAdjDNPer based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VRtrMplsLspTempAutoBWAdjDNPer_Type.__name__ = "Unsigned32"
_VRtrMplsLspTempAutoBWAdjDNPer_Object = MibTableColumn
vRtrMplsLspTempAutoBWAdjDNPer = _VRtrMplsLspTempAutoBWAdjDNPer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 47, 1, 2),
    _VRtrMplsLspTempAutoBWAdjDNPer_Type()
)
vRtrMplsLspTempAutoBWAdjDNPer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAutoBWAdjDNPer.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAutoBWAdjDNPer.setUnits("percent")


class _VRtrMplsLspTempAutoBWAdjDNMbps_Type(Unsigned32):
    """Custom type vRtrMplsLspTempAutoBWAdjDNMbps based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_VRtrMplsLspTempAutoBWAdjDNMbps_Type.__name__ = "Unsigned32"
_VRtrMplsLspTempAutoBWAdjDNMbps_Object = MibTableColumn
vRtrMplsLspTempAutoBWAdjDNMbps = _VRtrMplsLspTempAutoBWAdjDNMbps_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 47, 1, 3),
    _VRtrMplsLspTempAutoBWAdjDNMbps_Type()
)
vRtrMplsLspTempAutoBWAdjDNMbps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAutoBWAdjDNMbps.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAutoBWAdjDNMbps.setUnits("Mbps")


class _VRtrMplsLspTempAutoBWAdjUPPer_Type(Unsigned32):
    """Custom type vRtrMplsLspTempAutoBWAdjUPPer based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VRtrMplsLspTempAutoBWAdjUPPer_Type.__name__ = "Unsigned32"
_VRtrMplsLspTempAutoBWAdjUPPer_Object = MibTableColumn
vRtrMplsLspTempAutoBWAdjUPPer = _VRtrMplsLspTempAutoBWAdjUPPer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 47, 1, 4),
    _VRtrMplsLspTempAutoBWAdjUPPer_Type()
)
vRtrMplsLspTempAutoBWAdjUPPer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAutoBWAdjUPPer.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAutoBWAdjUPPer.setUnits("percent")


class _VRtrMplsLspTempAutoBWAdjUPMbps_Type(Unsigned32):
    """Custom type vRtrMplsLspTempAutoBWAdjUPMbps based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_VRtrMplsLspTempAutoBWAdjUPMbps_Type.__name__ = "Unsigned32"
_VRtrMplsLspTempAutoBWAdjUPMbps_Object = MibTableColumn
vRtrMplsLspTempAutoBWAdjUPMbps = _VRtrMplsLspTempAutoBWAdjUPMbps_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 47, 1, 5),
    _VRtrMplsLspTempAutoBWAdjUPMbps_Type()
)
vRtrMplsLspTempAutoBWAdjUPMbps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAutoBWAdjUPMbps.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAutoBWAdjUPMbps.setUnits("Mbps")


class _VRtrMplsLspTempAutoBWMaxBW_Type(Unsigned32):
    """Custom type vRtrMplsLspTempAutoBWMaxBW based on Unsigned32"""
    defaultValue = 100000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_VRtrMplsLspTempAutoBWMaxBW_Type.__name__ = "Unsigned32"
_VRtrMplsLspTempAutoBWMaxBW_Object = MibTableColumn
vRtrMplsLspTempAutoBWMaxBW = _VRtrMplsLspTempAutoBWMaxBW_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 47, 1, 6),
    _VRtrMplsLspTempAutoBWMaxBW_Type()
)
vRtrMplsLspTempAutoBWMaxBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAutoBWMaxBW.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAutoBWMaxBW.setUnits("Mbps")


class _VRtrMplsLspTempAutoBWMinBW_Type(Unsigned32):
    """Custom type vRtrMplsLspTempAutoBWMinBW based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_VRtrMplsLspTempAutoBWMinBW_Type.__name__ = "Unsigned32"
_VRtrMplsLspTempAutoBWMinBW_Object = MibTableColumn
vRtrMplsLspTempAutoBWMinBW = _VRtrMplsLspTempAutoBWMinBW_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 47, 1, 7),
    _VRtrMplsLspTempAutoBWMinBW_Type()
)
vRtrMplsLspTempAutoBWMinBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAutoBWMinBW.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAutoBWMinBW.setUnits("Mbps")


class _VRtrMplsLspTempAutoBWMntrBW_Type(TruthValue):
    """Custom type vRtrMplsLspTempAutoBWMntrBW based on TruthValue"""
    defaultValue = 2


_VRtrMplsLspTempAutoBWMntrBW_Type.__name__ = "TruthValue"
_VRtrMplsLspTempAutoBWMntrBW_Object = MibTableColumn
vRtrMplsLspTempAutoBWMntrBW = _VRtrMplsLspTempAutoBWMntrBW_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 47, 1, 8),
    _VRtrMplsLspTempAutoBWMntrBW_Type()
)
vRtrMplsLspTempAutoBWMntrBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAutoBWMntrBW.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAutoBWMntrBW.setUnits("Mbps")


class _VRtrMplsLspTempAutoBWAdjMult_Type(Unsigned32):
    """Custom type vRtrMplsLspTempAutoBWAdjMult based on Unsigned32"""
    defaultValue = 288

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16383),
    )


_VRtrMplsLspTempAutoBWAdjMult_Type.__name__ = "Unsigned32"
_VRtrMplsLspTempAutoBWAdjMult_Object = MibTableColumn
vRtrMplsLspTempAutoBWAdjMult = _VRtrMplsLspTempAutoBWAdjMult_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 47, 1, 9),
    _VRtrMplsLspTempAutoBWAdjMult_Type()
)
vRtrMplsLspTempAutoBWAdjMult.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAutoBWAdjMult.setStatus("current")


class _VRtrMplsLspTempAutoBWOverFlow_Type(Unsigned32):
    """Custom type vRtrMplsLspTempAutoBWOverFlow based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 10),
    )


_VRtrMplsLspTempAutoBWOverFlow_Type.__name__ = "Unsigned32"
_VRtrMplsLspTempAutoBWOverFlow_Object = MibTableColumn
vRtrMplsLspTempAutoBWOverFlow = _VRtrMplsLspTempAutoBWOverFlow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 47, 1, 10),
    _VRtrMplsLspTempAutoBWOverFlow_Type()
)
vRtrMplsLspTempAutoBWOverFlow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAutoBWOverFlow.setStatus("current")


class _VRtrMplsLspTempAutoBWOvrFlwThr_Type(Unsigned32):
    """Custom type vRtrMplsLspTempAutoBWOvrFlwThr based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 100),
    )


_VRtrMplsLspTempAutoBWOvrFlwThr_Type.__name__ = "Unsigned32"
_VRtrMplsLspTempAutoBWOvrFlwThr_Object = MibTableColumn
vRtrMplsLspTempAutoBWOvrFlwThr = _VRtrMplsLspTempAutoBWOvrFlwThr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 47, 1, 11),
    _VRtrMplsLspTempAutoBWOvrFlwThr_Type()
)
vRtrMplsLspTempAutoBWOvrFlwThr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAutoBWOvrFlwThr.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAutoBWOvrFlwThr.setUnits("percent")


class _VRtrMplsLspTempAutoBWOvrFlwBW_Type(Unsigned32):
    """Custom type vRtrMplsLspTempAutoBWOvrFlwBW based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_VRtrMplsLspTempAutoBWOvrFlwBW_Type.__name__ = "Unsigned32"
_VRtrMplsLspTempAutoBWOvrFlwBW_Object = MibTableColumn
vRtrMplsLspTempAutoBWOvrFlwBW = _VRtrMplsLspTempAutoBWOvrFlwBW_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 47, 1, 12),
    _VRtrMplsLspTempAutoBWOvrFlwBW_Type()
)
vRtrMplsLspTempAutoBWOvrFlwBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAutoBWOvrFlwBW.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAutoBWOvrFlwBW.setUnits("Mbps")


class _VRtrMplsLspTempAutoBWSampMult_Type(Unsigned32):
    """Custom type vRtrMplsLspTempAutoBWSampMult based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 511),
    )


_VRtrMplsLspTempAutoBWSampMult_Type.__name__ = "Unsigned32"
_VRtrMplsLspTempAutoBWSampMult_Object = MibTableColumn
vRtrMplsLspTempAutoBWSampMult = _VRtrMplsLspTempAutoBWSampMult_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 47, 1, 13),
    _VRtrMplsLspTempAutoBWSampMult_Type()
)
vRtrMplsLspTempAutoBWSampMult.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAutoBWSampMult.setStatus("current")
_VRtrMplsLspTempAutoBWSampTime_Type = Unsigned32
_VRtrMplsLspTempAutoBWSampTime_Object = MibTableColumn
vRtrMplsLspTempAutoBWSampTime = _VRtrMplsLspTempAutoBWSampTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 47, 1, 14),
    _VRtrMplsLspTempAutoBWSampTime_Type()
)
vRtrMplsLspTempAutoBWSampTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAutoBWSampTime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAutoBWSampTime.setUnits("minutes")


class _VRtrMplsLspTempAutoBWInherit_Type(Unsigned32):
    """Custom type vRtrMplsLspTempAutoBWInherit based on Unsigned32"""
    defaultValue = 0


_VRtrMplsLspTempAutoBWInherit_Type.__name__ = "Unsigned32"
_VRtrMplsLspTempAutoBWInherit_Object = MibTableColumn
vRtrMplsLspTempAutoBWInherit = _VRtrMplsLspTempAutoBWInherit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 47, 1, 15),
    _VRtrMplsLspTempAutoBWInherit_Type()
)
vRtrMplsLspTempAutoBWInherit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAutoBWInherit.setStatus("current")


class _VRtrMplsLspTempAutoBWBeWeight_Type(Unsigned32):
    """Custom type vRtrMplsLspTempAutoBWBeWeight based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VRtrMplsLspTempAutoBWBeWeight_Type.__name__ = "Unsigned32"
_VRtrMplsLspTempAutoBWBeWeight_Object = MibTableColumn
vRtrMplsLspTempAutoBWBeWeight = _VRtrMplsLspTempAutoBWBeWeight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 47, 1, 16),
    _VRtrMplsLspTempAutoBWBeWeight_Type()
)
vRtrMplsLspTempAutoBWBeWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAutoBWBeWeight.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAutoBWBeWeight.setUnits("percent")


class _VRtrMplsLspTempAutoBWL2Weight_Type(Unsigned32):
    """Custom type vRtrMplsLspTempAutoBWL2Weight based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VRtrMplsLspTempAutoBWL2Weight_Type.__name__ = "Unsigned32"
_VRtrMplsLspTempAutoBWL2Weight_Object = MibTableColumn
vRtrMplsLspTempAutoBWL2Weight = _VRtrMplsLspTempAutoBWL2Weight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 47, 1, 17),
    _VRtrMplsLspTempAutoBWL2Weight_Type()
)
vRtrMplsLspTempAutoBWL2Weight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAutoBWL2Weight.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAutoBWL2Weight.setUnits("percent")


class _VRtrMplsLspTempAutoBWAfWeight_Type(Unsigned32):
    """Custom type vRtrMplsLspTempAutoBWAfWeight based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VRtrMplsLspTempAutoBWAfWeight_Type.__name__ = "Unsigned32"
_VRtrMplsLspTempAutoBWAfWeight_Object = MibTableColumn
vRtrMplsLspTempAutoBWAfWeight = _VRtrMplsLspTempAutoBWAfWeight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 47, 1, 18),
    _VRtrMplsLspTempAutoBWAfWeight_Type()
)
vRtrMplsLspTempAutoBWAfWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAutoBWAfWeight.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAutoBWAfWeight.setUnits("percent")


class _VRtrMplsLspTempAutoBWL1Weight_Type(Unsigned32):
    """Custom type vRtrMplsLspTempAutoBWL1Weight based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VRtrMplsLspTempAutoBWL1Weight_Type.__name__ = "Unsigned32"
_VRtrMplsLspTempAutoBWL1Weight_Object = MibTableColumn
vRtrMplsLspTempAutoBWL1Weight = _VRtrMplsLspTempAutoBWL1Weight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 47, 1, 19),
    _VRtrMplsLspTempAutoBWL1Weight_Type()
)
vRtrMplsLspTempAutoBWL1Weight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAutoBWL1Weight.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAutoBWL1Weight.setUnits("percent")


class _VRtrMplsLspTempAutoBWH2Weight_Type(Unsigned32):
    """Custom type vRtrMplsLspTempAutoBWH2Weight based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VRtrMplsLspTempAutoBWH2Weight_Type.__name__ = "Unsigned32"
_VRtrMplsLspTempAutoBWH2Weight_Object = MibTableColumn
vRtrMplsLspTempAutoBWH2Weight = _VRtrMplsLspTempAutoBWH2Weight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 47, 1, 20),
    _VRtrMplsLspTempAutoBWH2Weight_Type()
)
vRtrMplsLspTempAutoBWH2Weight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAutoBWH2Weight.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAutoBWH2Weight.setUnits("percent")


class _VRtrMplsLspTempAutoBWEfWeight_Type(Unsigned32):
    """Custom type vRtrMplsLspTempAutoBWEfWeight based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VRtrMplsLspTempAutoBWEfWeight_Type.__name__ = "Unsigned32"
_VRtrMplsLspTempAutoBWEfWeight_Object = MibTableColumn
vRtrMplsLspTempAutoBWEfWeight = _VRtrMplsLspTempAutoBWEfWeight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 47, 1, 21),
    _VRtrMplsLspTempAutoBWEfWeight_Type()
)
vRtrMplsLspTempAutoBWEfWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAutoBWEfWeight.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAutoBWEfWeight.setUnits("percent")


class _VRtrMplsLspTempAutoBWH1Weight_Type(Unsigned32):
    """Custom type vRtrMplsLspTempAutoBWH1Weight based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VRtrMplsLspTempAutoBWH1Weight_Type.__name__ = "Unsigned32"
_VRtrMplsLspTempAutoBWH1Weight_Object = MibTableColumn
vRtrMplsLspTempAutoBWH1Weight = _VRtrMplsLspTempAutoBWH1Weight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 47, 1, 22),
    _VRtrMplsLspTempAutoBWH1Weight_Type()
)
vRtrMplsLspTempAutoBWH1Weight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAutoBWH1Weight.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAutoBWH1Weight.setUnits("percent")


class _VRtrMplsLspTempAutoBWNcWeight_Type(Unsigned32):
    """Custom type vRtrMplsLspTempAutoBWNcWeight based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VRtrMplsLspTempAutoBWNcWeight_Type.__name__ = "Unsigned32"
_VRtrMplsLspTempAutoBWNcWeight_Object = MibTableColumn
vRtrMplsLspTempAutoBWNcWeight = _VRtrMplsLspTempAutoBWNcWeight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 47, 1, 23),
    _VRtrMplsLspTempAutoBWNcWeight_Type()
)
vRtrMplsLspTempAutoBWNcWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAutoBWNcWeight.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAutoBWNcWeight.setUnits("percent")


class _VRtrMplsLspTempAutoBWUnderFlow_Type(Unsigned32):
    """Custom type vRtrMplsLspTempAutoBWUnderFlow based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 10),
    )


_VRtrMplsLspTempAutoBWUnderFlow_Type.__name__ = "Unsigned32"
_VRtrMplsLspTempAutoBWUnderFlow_Object = MibTableColumn
vRtrMplsLspTempAutoBWUnderFlow = _VRtrMplsLspTempAutoBWUnderFlow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 47, 1, 24),
    _VRtrMplsLspTempAutoBWUnderFlow_Type()
)
vRtrMplsLspTempAutoBWUnderFlow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAutoBWUnderFlow.setStatus("current")


class _VRtrMplsLspTempAutoBWUndFlwThr_Type(Unsigned32):
    """Custom type vRtrMplsLspTempAutoBWUndFlwThr based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 100),
    )


_VRtrMplsLspTempAutoBWUndFlwThr_Type.__name__ = "Unsigned32"
_VRtrMplsLspTempAutoBWUndFlwThr_Object = MibTableColumn
vRtrMplsLspTempAutoBWUndFlwThr = _VRtrMplsLspTempAutoBWUndFlwThr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 47, 1, 25),
    _VRtrMplsLspTempAutoBWUndFlwThr_Type()
)
vRtrMplsLspTempAutoBWUndFlwThr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAutoBWUndFlwThr.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAutoBWUndFlwThr.setUnits("percent")


class _VRtrMplsLspTempAutoBWUndFlwBW_Type(Unsigned32):
    """Custom type vRtrMplsLspTempAutoBWUndFlwBW based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_VRtrMplsLspTempAutoBWUndFlwBW_Type.__name__ = "Unsigned32"
_VRtrMplsLspTempAutoBWUndFlwBW_Object = MibTableColumn
vRtrMplsLspTempAutoBWUndFlwBW = _VRtrMplsLspTempAutoBWUndFlwBW_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 47, 1, 26),
    _VRtrMplsLspTempAutoBWUndFlwBW_Type()
)
vRtrMplsLspTempAutoBWUndFlwBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAutoBWUndFlwBW.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspTempAutoBWUndFlwBW.setUnits("Mbps")
_VRtrMplsTemplPlcyBindTblLastChg_Type = TimeStamp
_VRtrMplsTemplPlcyBindTblLastChg_Object = MibScalar
vRtrMplsTemplPlcyBindTblLastChg = _VRtrMplsTemplPlcyBindTblLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 48),
    _VRtrMplsTemplPlcyBindTblLastChg_Type()
)
vRtrMplsTemplPlcyBindTblLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsTemplPlcyBindTblLastChg.setStatus("current")
_VRtrMplsLspTemplPlcyBindTable_Object = MibTable
vRtrMplsLspTemplPlcyBindTable = _VRtrMplsLspTemplPlcyBindTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 49)
)
if mibBuilder.loadTexts:
    vRtrMplsLspTemplPlcyBindTable.setStatus("current")
_VRtrMplsLspTemplPlcyBindEntry_Object = MibTableRow
vRtrMplsLspTemplPlcyBindEntry = _VRtrMplsLspTemplPlcyBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 49, 1)
)
vRtrMplsLspTemplPlcyBindEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateName"),
)
if mibBuilder.loadTexts:
    vRtrMplsLspTemplPlcyBindEntry.setStatus("current")
_VRtrMplsLspTemplPlcyBindLastChg_Type = TimeStamp
_VRtrMplsLspTemplPlcyBindLastChg_Object = MibTableColumn
vRtrMplsLspTemplPlcyBindLastChg = _VRtrMplsLspTemplPlcyBindLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 49, 1, 1),
    _VRtrMplsLspTemplPlcyBindLastChg_Type()
)
vRtrMplsLspTemplPlcyBindLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspTemplPlcyBindLastChg.setStatus("current")
_VRtrMplsLspTemplPlcyBindRowStat_Type = RowStatus
_VRtrMplsLspTemplPlcyBindRowStat_Object = MibTableColumn
vRtrMplsLspTemplPlcyBindRowStat = _VRtrMplsLspTemplPlcyBindRowStat_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 49, 1, 2),
    _VRtrMplsLspTemplPlcyBindRowStat_Type()
)
vRtrMplsLspTemplPlcyBindRowStat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTemplPlcyBindRowStat.setStatus("current")


class _VRtrMplsLspTemplPlcyBind1_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrMplsLspTemplPlcyBind1 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrMplsLspTemplPlcyBind1_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrMplsLspTemplPlcyBind1_Object = MibTableColumn
vRtrMplsLspTemplPlcyBind1 = _VRtrMplsLspTemplPlcyBind1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 49, 1, 3),
    _VRtrMplsLspTemplPlcyBind1_Type()
)
vRtrMplsLspTemplPlcyBind1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTemplPlcyBind1.setStatus("current")


class _VRtrMplsLspTemplPlcyBind2_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrMplsLspTemplPlcyBind2 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrMplsLspTemplPlcyBind2_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrMplsLspTemplPlcyBind2_Object = MibTableColumn
vRtrMplsLspTemplPlcyBind2 = _VRtrMplsLspTemplPlcyBind2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 49, 1, 4),
    _VRtrMplsLspTemplPlcyBind2_Type()
)
vRtrMplsLspTemplPlcyBind2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTemplPlcyBind2.setStatus("current")


class _VRtrMplsLspTemplPlcyBind3_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrMplsLspTemplPlcyBind3 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrMplsLspTemplPlcyBind3_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrMplsLspTemplPlcyBind3_Object = MibTableColumn
vRtrMplsLspTemplPlcyBind3 = _VRtrMplsLspTemplPlcyBind3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 49, 1, 5),
    _VRtrMplsLspTemplPlcyBind3_Type()
)
vRtrMplsLspTemplPlcyBind3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTemplPlcyBind3.setStatus("current")


class _VRtrMplsLspTemplPlcyBind4_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrMplsLspTemplPlcyBind4 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrMplsLspTemplPlcyBind4_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrMplsLspTemplPlcyBind4_Object = MibTableColumn
vRtrMplsLspTemplPlcyBind4 = _VRtrMplsLspTemplPlcyBind4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 49, 1, 6),
    _VRtrMplsLspTemplPlcyBind4_Type()
)
vRtrMplsLspTemplPlcyBind4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTemplPlcyBind4.setStatus("current")


class _VRtrMplsLspTemplPlcyBind5_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrMplsLspTemplPlcyBind5 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrMplsLspTemplPlcyBind5_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrMplsLspTemplPlcyBind5_Object = MibTableColumn
vRtrMplsLspTemplPlcyBind5 = _VRtrMplsLspTemplPlcyBind5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 49, 1, 7),
    _VRtrMplsLspTemplPlcyBind5_Type()
)
vRtrMplsLspTemplPlcyBind5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTemplPlcyBind5.setStatus("current")


class _VRtrMplsLspTemplPlcyBindOneHop_Type(TruthValue):
    """Custom type vRtrMplsLspTemplPlcyBindOneHop based on TruthValue"""
    defaultValue = 2


_VRtrMplsLspTemplPlcyBindOneHop_Type.__name__ = "TruthValue"
_VRtrMplsLspTemplPlcyBindOneHop_Object = MibTableColumn
vRtrMplsLspTemplPlcyBindOneHop = _VRtrMplsLspTemplPlcyBindOneHop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 49, 1, 8),
    _VRtrMplsLspTemplPlcyBindOneHop_Type()
)
vRtrMplsLspTemplPlcyBindOneHop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTemplPlcyBindOneHop.setStatus("current")
_VRtrMplsLspTempInStatTblLstChg_Type = TimeStamp
_VRtrMplsLspTempInStatTblLstChg_Object = MibScalar
vRtrMplsLspTempInStatTblLstChg = _VRtrMplsLspTempInStatTblLstChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 50),
    _VRtrMplsLspTempInStatTblLstChg_Type()
)
vRtrMplsLspTempInStatTblLstChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspTempInStatTblLstChg.setStatus("current")
_VRtrMplsLspTempInStatTable_Object = MibTable
vRtrMplsLspTempInStatTable = _VRtrMplsLspTempInStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 51)
)
if mibBuilder.loadTexts:
    vRtrMplsLspTempInStatTable.setStatus("current")
_VRtrMplsLspTempInStatEntry_Object = MibTableRow
vRtrMplsLspTempInStatEntry = _VRtrMplsLspTempInStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 51, 1)
)
vRtrMplsLspTempInStatEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsLspTempInStatType"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsLspTempInStatSndrAddrTyp"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsLspTempInStatSndrAddr"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsLspTempInStatLspNamePref"),
)
if mibBuilder.loadTexts:
    vRtrMplsLspTempInStatEntry.setStatus("current")


class _VRtrMplsLspTempInStatType_Type(Integer32):
    """Custom type vRtrMplsLspTempInStatType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("p2p", 1),
          ("p2mp", 2))
    )


_VRtrMplsLspTempInStatType_Type.__name__ = "Integer32"
_VRtrMplsLspTempInStatType_Object = MibTableColumn
vRtrMplsLspTempInStatType = _VRtrMplsLspTempInStatType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 51, 1, 1),
    _VRtrMplsLspTempInStatType_Type()
)
vRtrMplsLspTempInStatType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsLspTempInStatType.setStatus("current")
_VRtrMplsLspTempInStatSndrAddrTyp_Type = InetAddressType
_VRtrMplsLspTempInStatSndrAddrTyp_Object = MibTableColumn
vRtrMplsLspTempInStatSndrAddrTyp = _VRtrMplsLspTempInStatSndrAddrTyp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 51, 1, 2),
    _VRtrMplsLspTempInStatSndrAddrTyp_Type()
)
vRtrMplsLspTempInStatSndrAddrTyp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsLspTempInStatSndrAddrTyp.setStatus("current")


class _VRtrMplsLspTempInStatSndrAddr_Type(InetAddress):
    """Custom type vRtrMplsLspTempInStatSndrAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrMplsLspTempInStatSndrAddr_Type.__name__ = "InetAddress"
_VRtrMplsLspTempInStatSndrAddr_Object = MibTableColumn
vRtrMplsLspTempInStatSndrAddr = _VRtrMplsLspTempInStatSndrAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 51, 1, 3),
    _VRtrMplsLspTempInStatSndrAddr_Type()
)
vRtrMplsLspTempInStatSndrAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsLspTempInStatSndrAddr.setStatus("current")
_VRtrMplsLspTempInStatLspNamePref_Type = TLNamedItem
_VRtrMplsLspTempInStatLspNamePref_Object = MibTableColumn
vRtrMplsLspTempInStatLspNamePref = _VRtrMplsLspTempInStatLspNamePref_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 51, 1, 4),
    _VRtrMplsLspTempInStatLspNamePref_Type()
)
vRtrMplsLspTempInStatLspNamePref.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsLspTempInStatLspNamePref.setStatus("current")
_VRtrMplsLspTempInStatRowStatus_Type = RowStatus
_VRtrMplsLspTempInStatRowStatus_Object = MibTableColumn
vRtrMplsLspTempInStatRowStatus = _VRtrMplsLspTempInStatRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 51, 1, 5),
    _VRtrMplsLspTempInStatRowStatus_Type()
)
vRtrMplsLspTempInStatRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTempInStatRowStatus.setStatus("current")
_VRtrMplsLspTempInStatLastChanged_Type = TimeStamp
_VRtrMplsLspTempInStatLastChanged_Object = MibTableColumn
vRtrMplsLspTempInStatLastChanged = _VRtrMplsLspTempInStatLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 51, 1, 6),
    _VRtrMplsLspTempInStatLastChanged_Type()
)
vRtrMplsLspTempInStatLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspTempInStatLastChanged.setStatus("current")


class _VRtrMplsLspTempInStatCollectStat_Type(TruthValue):
    """Custom type vRtrMplsLspTempInStatCollectStat based on TruthValue"""
    defaultValue = 2


_VRtrMplsLspTempInStatCollectStat_Type.__name__ = "TruthValue"
_VRtrMplsLspTempInStatCollectStat_Object = MibTableColumn
vRtrMplsLspTempInStatCollectStat = _VRtrMplsLspTempInStatCollectStat_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 51, 1, 7),
    _VRtrMplsLspTempInStatCollectStat_Type()
)
vRtrMplsLspTempInStatCollectStat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTempInStatCollectStat.setStatus("current")


class _VRtrMplsLspTempInStatAccntPolicy_Type(Unsigned32):
    """Custom type vRtrMplsLspTempInStatAccntPolicy based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 99),
    )


_VRtrMplsLspTempInStatAccntPolicy_Type.__name__ = "Unsigned32"
_VRtrMplsLspTempInStatAccntPolicy_Object = MibTableColumn
vRtrMplsLspTempInStatAccntPolicy = _VRtrMplsLspTempInStatAccntPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 51, 1, 8),
    _VRtrMplsLspTempInStatAccntPolicy_Type()
)
vRtrMplsLspTempInStatAccntPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTempInStatAccntPolicy.setStatus("current")


class _VRtrMplsLspTempInStatAdminState_Type(TmnxAdminState):
    """Custom type vRtrMplsLspTempInStatAdminState based on TmnxAdminState"""
    defaultValue = 3


_VRtrMplsLspTempInStatAdminState_Type.__name__ = "TmnxAdminState"
_VRtrMplsLspTempInStatAdminState_Object = MibTableColumn
vRtrMplsLspTempInStatAdminState = _VRtrMplsLspTempInStatAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 51, 1, 9),
    _VRtrMplsLspTempInStatAdminState_Type()
)
vRtrMplsLspTempInStatAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTempInStatAdminState.setStatus("current")


class _VRtrMplsLspTempInStatMaxStats_Type(Unsigned32):
    """Custom type vRtrMplsLspTempInStatMaxStats based on Unsigned32"""
    defaultValue = 8191

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_VRtrMplsLspTempInStatMaxStats_Type.__name__ = "Unsigned32"
_VRtrMplsLspTempInStatMaxStats_Object = MibTableColumn
vRtrMplsLspTempInStatMaxStats = _VRtrMplsLspTempInStatMaxStats_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 51, 1, 10),
    _VRtrMplsLspTempInStatMaxStats_Type()
)
vRtrMplsLspTempInStatMaxStats.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspTempInStatMaxStats.setStatus("current")
_VRtrMplsLspTempInStatTotlSession_Type = Unsigned32
_VRtrMplsLspTempInStatTotlSession_Object = MibTableColumn
vRtrMplsLspTempInStatTotlSession = _VRtrMplsLspTempInStatTotlSession_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 51, 1, 11),
    _VRtrMplsLspTempInStatTotlSession_Type()
)
vRtrMplsLspTempInStatTotlSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspTempInStatTotlSession.setStatus("current")
_VRtrMplsLspExtTable_Object = MibTable
vRtrMplsLspExtTable = _VRtrMplsLspExtTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 52)
)
if mibBuilder.loadTexts:
    vRtrMplsLspExtTable.setStatus("current")
_VRtrMplsLspExtEntry_Object = MibTableRow
vRtrMplsLspExtEntry = _VRtrMplsLspExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 52, 1)
)
if mibBuilder.loadTexts:
    vRtrMplsLspExtEntry.setStatus("current")


class _VRtrMplsLspExtPceCompute_Type(TruthValue):
    """Custom type vRtrMplsLspExtPceCompute based on TruthValue"""
    defaultValue = 2


_VRtrMplsLspExtPceCompute_Type.__name__ = "TruthValue"
_VRtrMplsLspExtPceCompute_Object = MibTableColumn
vRtrMplsLspExtPceCompute = _VRtrMplsLspExtPceCompute_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 52, 1, 1),
    _VRtrMplsLspExtPceCompute_Type()
)
vRtrMplsLspExtPceCompute.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspExtPceCompute.setStatus("current")


class _VRtrMplsLspExtPceControl_Type(TruthValue):
    """Custom type vRtrMplsLspExtPceControl based on TruthValue"""
    defaultValue = 2


_VRtrMplsLspExtPceControl_Type.__name__ = "TruthValue"
_VRtrMplsLspExtPceControl_Object = MibTableColumn
vRtrMplsLspExtPceControl = _VRtrMplsLspExtPceControl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 52, 1, 2),
    _VRtrMplsLspExtPceControl_Type()
)
vRtrMplsLspExtPceControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspExtPceControl.setStatus("current")


class _VRtrMplsLspExtPceReport_Type(Integer32):
    """Custom type vRtrMplsLspExtPceReport based on Integer32"""
    defaultValue = 3

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
          ("disable", 2),
          ("inherit", 3))
    )


_VRtrMplsLspExtPceReport_Type.__name__ = "Integer32"
_VRtrMplsLspExtPceReport_Object = MibTableColumn
vRtrMplsLspExtPceReport = _VRtrMplsLspExtPceReport_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 52, 1, 3),
    _VRtrMplsLspExtPceReport_Type()
)
vRtrMplsLspExtPceReport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspExtPceReport.setStatus("current")
_VRtrMplsLspExtTtmTunnelId_Type = Unsigned32
_VRtrMplsLspExtTtmTunnelId_Object = MibTableColumn
vRtrMplsLspExtTtmTunnelId = _VRtrMplsLspExtTtmTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 52, 1, 4),
    _VRtrMplsLspExtTtmTunnelId_Type()
)
vRtrMplsLspExtTtmTunnelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspExtTtmTunnelId.setStatus("current")


class _VRtrMplsLspExtMaxSrLabels_Type(Unsigned32):
    """Custom type vRtrMplsLspExtMaxSrLabels based on Unsigned32"""
    defaultValue = 6

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11),
    )


_VRtrMplsLspExtMaxSrLabels_Type.__name__ = "Unsigned32"
_VRtrMplsLspExtMaxSrLabels_Object = MibTableColumn
vRtrMplsLspExtMaxSrLabels = _VRtrMplsLspExtMaxSrLabels_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 52, 1, 5),
    _VRtrMplsLspExtMaxSrLabels_Type()
)
vRtrMplsLspExtMaxSrLabels.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspExtMaxSrLabels.setStatus("current")
_VRtrMplsLspExtTunnelId_Type = Unsigned32
_VRtrMplsLspExtTunnelId_Object = MibTableColumn
vRtrMplsLspExtTunnelId = _VRtrMplsLspExtTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 52, 1, 6),
    _VRtrMplsLspExtTunnelId_Type()
)
vRtrMplsLspExtTunnelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspExtTunnelId.setStatus("current")


class _VRtrMplsLspExtEntropyLabel_Type(Integer32):
    """Custom type vRtrMplsLspExtEntropyLabel based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("forceDisable", 1),
          ("enable", 2),
          ("inherit", 3))
    )


_VRtrMplsLspExtEntropyLabel_Type.__name__ = "Integer32"
_VRtrMplsLspExtEntropyLabel_Object = MibTableColumn
vRtrMplsLspExtEntropyLabel = _VRtrMplsLspExtEntropyLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 52, 1, 7),
    _VRtrMplsLspExtEntropyLabel_Type()
)
vRtrMplsLspExtEntropyLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspExtEntropyLabel.setStatus("current")


class _VRtrMplsLspExtOperEntropyLabel_Type(Integer32):
    """Custom type vRtrMplsLspExtOperEntropyLabel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forceDisable", 1),
          ("enable", 2))
    )


_VRtrMplsLspExtOperEntropyLabel_Type.__name__ = "Integer32"
_VRtrMplsLspExtOperEntropyLabel_Object = MibTableColumn
vRtrMplsLspExtOperEntropyLabel = _VRtrMplsLspExtOperEntropyLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 52, 1, 8),
    _VRtrMplsLspExtOperEntropyLabel_Type()
)
vRtrMplsLspExtOperEntropyLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspExtOperEntropyLabel.setStatus("current")


class _VRtrMplsLspExtFrrOverheadLabel_Type(Unsigned32):
    """Custom type vRtrMplsLspExtFrrOverheadLabel based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_VRtrMplsLspExtFrrOverheadLabel_Type.__name__ = "Unsigned32"
_VRtrMplsLspExtFrrOverheadLabel_Object = MibTableColumn
vRtrMplsLspExtFrrOverheadLabel = _VRtrMplsLspExtFrrOverheadLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 52, 1, 9),
    _VRtrMplsLspExtFrrOverheadLabel_Type()
)
vRtrMplsLspExtFrrOverheadLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspExtFrrOverheadLabel.setStatus("current")


class _VRtrMplsLspExtNegEntropyLbl_Type(Integer32):
    """Custom type vRtrMplsLspExtNegEntropyLbl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forceDisable", 1),
          ("enable", 2))
    )


_VRtrMplsLspExtNegEntropyLbl_Type.__name__ = "Integer32"
_VRtrMplsLspExtNegEntropyLbl_Object = MibTableColumn
vRtrMplsLspExtNegEntropyLbl = _VRtrMplsLspExtNegEntropyLbl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 52, 1, 10),
    _VRtrMplsLspExtNegEntropyLbl_Type()
)
vRtrMplsLspExtNegEntropyLbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspExtNegEntropyLbl.setStatus("current")


class _VRtrMplsLspExtBfdFailureAction_Type(Integer32):
    """Custom type vRtrMplsLspExtBfdFailureAction based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("down", 1))
    )


_VRtrMplsLspExtBfdFailureAction_Type.__name__ = "Integer32"
_VRtrMplsLspExtBfdFailureAction_Object = MibTableColumn
vRtrMplsLspExtBfdFailureAction = _VRtrMplsLspExtBfdFailureAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 52, 1, 11),
    _VRtrMplsLspExtBfdFailureAction_Type()
)
vRtrMplsLspExtBfdFailureAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspExtBfdFailureAction.setStatus("current")
_VRtrMplsLspPathProfTblLstChg_Type = TimeStamp
_VRtrMplsLspPathProfTblLstChg_Object = MibScalar
vRtrMplsLspPathProfTblLstChg = _VRtrMplsLspPathProfTblLstChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 53),
    _VRtrMplsLspPathProfTblLstChg_Type()
)
vRtrMplsLspPathProfTblLstChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathProfTblLstChg.setStatus("current")
_VRtrMplsLspPathProfTable_Object = MibTable
vRtrMplsLspPathProfTable = _VRtrMplsLspPathProfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 54)
)
if mibBuilder.loadTexts:
    vRtrMplsLspPathProfTable.setStatus("current")
_VRtrMplsLspPathProfEntry_Object = MibTableRow
vRtrMplsLspPathProfEntry = _VRtrMplsLspPathProfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 54, 1)
)
vRtrMplsLspPathProfEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsLspIndex"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsLspPathProfId"),
)
if mibBuilder.loadTexts:
    vRtrMplsLspPathProfEntry.setStatus("current")


class _VRtrMplsLspPathProfId_Type(Unsigned32):
    """Custom type vRtrMplsLspPathProfId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_VRtrMplsLspPathProfId_Type.__name__ = "Unsigned32"
_VRtrMplsLspPathProfId_Object = MibTableColumn
vRtrMplsLspPathProfId = _VRtrMplsLspPathProfId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 54, 1, 1),
    _VRtrMplsLspPathProfId_Type()
)
vRtrMplsLspPathProfId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsLspPathProfId.setStatus("current")
_VRtrMplsLspPathProfRowStatus_Type = RowStatus
_VRtrMplsLspPathProfRowStatus_Object = MibTableColumn
vRtrMplsLspPathProfRowStatus = _VRtrMplsLspPathProfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 54, 1, 2),
    _VRtrMplsLspPathProfRowStatus_Type()
)
vRtrMplsLspPathProfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspPathProfRowStatus.setStatus("current")
_VRtrMplsLspPathProfLastChange_Type = TimeStamp
_VRtrMplsLspPathProfLastChange_Object = MibTableColumn
vRtrMplsLspPathProfLastChange = _VRtrMplsLspPathProfLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 54, 1, 3),
    _VRtrMplsLspPathProfLastChange_Type()
)
vRtrMplsLspPathProfLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathProfLastChange.setStatus("current")


class _VRtrMplsLspPathProfGroupId_Type(Unsigned32):
    """Custom type vRtrMplsLspPathProfGroupId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4294967295),
    )


_VRtrMplsLspPathProfGroupId_Type.__name__ = "Unsigned32"
_VRtrMplsLspPathProfGroupId_Object = MibTableColumn
vRtrMplsLspPathProfGroupId = _VRtrMplsLspPathProfGroupId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 54, 1, 4),
    _VRtrMplsLspPathProfGroupId_Type()
)
vRtrMplsLspPathProfGroupId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspPathProfGroupId.setStatus("current")
_VRtrMplsClassFwdPlcyTblLstChg_Type = TimeStamp
_VRtrMplsClassFwdPlcyTblLstChg_Object = MibScalar
vRtrMplsClassFwdPlcyTblLstChg = _VRtrMplsClassFwdPlcyTblLstChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 55),
    _VRtrMplsClassFwdPlcyTblLstChg_Type()
)
vRtrMplsClassFwdPlcyTblLstChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsClassFwdPlcyTblLstChg.setStatus("current")
_VRtrMplsClassFwdPlcyTable_Object = MibTable
vRtrMplsClassFwdPlcyTable = _VRtrMplsClassFwdPlcyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 56)
)
if mibBuilder.loadTexts:
    vRtrMplsClassFwdPlcyTable.setStatus("current")
_VRtrMplsClassFwdPlcyEntry_Object = MibTableRow
vRtrMplsClassFwdPlcyEntry = _VRtrMplsClassFwdPlcyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 56, 1)
)
vRtrMplsClassFwdPlcyEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsClassFwdPlcyName"),
)
if mibBuilder.loadTexts:
    vRtrMplsClassFwdPlcyEntry.setStatus("current")
_VRtrMplsClassFwdPlcyName_Type = TNamedItem
_VRtrMplsClassFwdPlcyName_Object = MibTableColumn
vRtrMplsClassFwdPlcyName = _VRtrMplsClassFwdPlcyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 56, 1, 1),
    _VRtrMplsClassFwdPlcyName_Type()
)
vRtrMplsClassFwdPlcyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsClassFwdPlcyName.setStatus("current")
_VRtrMplsClassFwdPlcyRowStatus_Type = RowStatus
_VRtrMplsClassFwdPlcyRowStatus_Object = MibTableColumn
vRtrMplsClassFwdPlcyRowStatus = _VRtrMplsClassFwdPlcyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 56, 1, 2),
    _VRtrMplsClassFwdPlcyRowStatus_Type()
)
vRtrMplsClassFwdPlcyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsClassFwdPlcyRowStatus.setStatus("current")
_VRtrMplsClassFwdPlcyLastChanged_Type = TimeStamp
_VRtrMplsClassFwdPlcyLastChanged_Object = MibTableColumn
vRtrMplsClassFwdPlcyLastChanged = _VRtrMplsClassFwdPlcyLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 56, 1, 3),
    _VRtrMplsClassFwdPlcyLastChanged_Type()
)
vRtrMplsClassFwdPlcyLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsClassFwdPlcyLastChanged.setStatus("current")


class _VRtrMplsClassFwdPlcyFcBEFwdSet_Type(TmnxMplsClassFwdSetId):
    """Custom type vRtrMplsClassFwdPlcyFcBEFwdSet based on TmnxMplsClassFwdSetId"""
    defaultValue = 1


_VRtrMplsClassFwdPlcyFcBEFwdSet_Type.__name__ = "TmnxMplsClassFwdSetId"
_VRtrMplsClassFwdPlcyFcBEFwdSet_Object = MibTableColumn
vRtrMplsClassFwdPlcyFcBEFwdSet = _VRtrMplsClassFwdPlcyFcBEFwdSet_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 56, 1, 4),
    _VRtrMplsClassFwdPlcyFcBEFwdSet_Type()
)
vRtrMplsClassFwdPlcyFcBEFwdSet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsClassFwdPlcyFcBEFwdSet.setStatus("current")


class _VRtrMplsClassFwdPlcyFcL2FwdSet_Type(TmnxMplsClassFwdSetId):
    """Custom type vRtrMplsClassFwdPlcyFcL2FwdSet based on TmnxMplsClassFwdSetId"""
    defaultValue = 1


_VRtrMplsClassFwdPlcyFcL2FwdSet_Type.__name__ = "TmnxMplsClassFwdSetId"
_VRtrMplsClassFwdPlcyFcL2FwdSet_Object = MibTableColumn
vRtrMplsClassFwdPlcyFcL2FwdSet = _VRtrMplsClassFwdPlcyFcL2FwdSet_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 56, 1, 5),
    _VRtrMplsClassFwdPlcyFcL2FwdSet_Type()
)
vRtrMplsClassFwdPlcyFcL2FwdSet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsClassFwdPlcyFcL2FwdSet.setStatus("current")


class _VRtrMplsClassFwdPlcyFcAFFwdSet_Type(TmnxMplsClassFwdSetId):
    """Custom type vRtrMplsClassFwdPlcyFcAFFwdSet based on TmnxMplsClassFwdSetId"""
    defaultValue = 1


_VRtrMplsClassFwdPlcyFcAFFwdSet_Type.__name__ = "TmnxMplsClassFwdSetId"
_VRtrMplsClassFwdPlcyFcAFFwdSet_Object = MibTableColumn
vRtrMplsClassFwdPlcyFcAFFwdSet = _VRtrMplsClassFwdPlcyFcAFFwdSet_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 56, 1, 6),
    _VRtrMplsClassFwdPlcyFcAFFwdSet_Type()
)
vRtrMplsClassFwdPlcyFcAFFwdSet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsClassFwdPlcyFcAFFwdSet.setStatus("current")


class _VRtrMplsClassFwdPlcyFcL1FwdSet_Type(TmnxMplsClassFwdSetId):
    """Custom type vRtrMplsClassFwdPlcyFcL1FwdSet based on TmnxMplsClassFwdSetId"""
    defaultValue = 1


_VRtrMplsClassFwdPlcyFcL1FwdSet_Type.__name__ = "TmnxMplsClassFwdSetId"
_VRtrMplsClassFwdPlcyFcL1FwdSet_Object = MibTableColumn
vRtrMplsClassFwdPlcyFcL1FwdSet = _VRtrMplsClassFwdPlcyFcL1FwdSet_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 56, 1, 7),
    _VRtrMplsClassFwdPlcyFcL1FwdSet_Type()
)
vRtrMplsClassFwdPlcyFcL1FwdSet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsClassFwdPlcyFcL1FwdSet.setStatus("current")


class _VRtrMplsClassFwdPlcyFcH2FwdSet_Type(TmnxMplsClassFwdSetId):
    """Custom type vRtrMplsClassFwdPlcyFcH2FwdSet based on TmnxMplsClassFwdSetId"""
    defaultValue = 1


_VRtrMplsClassFwdPlcyFcH2FwdSet_Type.__name__ = "TmnxMplsClassFwdSetId"
_VRtrMplsClassFwdPlcyFcH2FwdSet_Object = MibTableColumn
vRtrMplsClassFwdPlcyFcH2FwdSet = _VRtrMplsClassFwdPlcyFcH2FwdSet_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 56, 1, 8),
    _VRtrMplsClassFwdPlcyFcH2FwdSet_Type()
)
vRtrMplsClassFwdPlcyFcH2FwdSet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsClassFwdPlcyFcH2FwdSet.setStatus("current")


class _VRtrMplsClassFwdPlcyFcEFFwdSet_Type(TmnxMplsClassFwdSetId):
    """Custom type vRtrMplsClassFwdPlcyFcEFFwdSet based on TmnxMplsClassFwdSetId"""
    defaultValue = 1


_VRtrMplsClassFwdPlcyFcEFFwdSet_Type.__name__ = "TmnxMplsClassFwdSetId"
_VRtrMplsClassFwdPlcyFcEFFwdSet_Object = MibTableColumn
vRtrMplsClassFwdPlcyFcEFFwdSet = _VRtrMplsClassFwdPlcyFcEFFwdSet_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 56, 1, 9),
    _VRtrMplsClassFwdPlcyFcEFFwdSet_Type()
)
vRtrMplsClassFwdPlcyFcEFFwdSet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsClassFwdPlcyFcEFFwdSet.setStatus("current")


class _VRtrMplsClassFwdPlcyFcH1FwdSet_Type(TmnxMplsClassFwdSetId):
    """Custom type vRtrMplsClassFwdPlcyFcH1FwdSet based on TmnxMplsClassFwdSetId"""
    defaultValue = 1


_VRtrMplsClassFwdPlcyFcH1FwdSet_Type.__name__ = "TmnxMplsClassFwdSetId"
_VRtrMplsClassFwdPlcyFcH1FwdSet_Object = MibTableColumn
vRtrMplsClassFwdPlcyFcH1FwdSet = _VRtrMplsClassFwdPlcyFcH1FwdSet_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 56, 1, 10),
    _VRtrMplsClassFwdPlcyFcH1FwdSet_Type()
)
vRtrMplsClassFwdPlcyFcH1FwdSet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsClassFwdPlcyFcH1FwdSet.setStatus("current")


class _VRtrMplsClassFwdPlcyFcNCFwdSet_Type(TmnxMplsClassFwdSetId):
    """Custom type vRtrMplsClassFwdPlcyFcNCFwdSet based on TmnxMplsClassFwdSetId"""
    defaultValue = 1


_VRtrMplsClassFwdPlcyFcNCFwdSet_Type.__name__ = "TmnxMplsClassFwdSetId"
_VRtrMplsClassFwdPlcyFcNCFwdSet_Object = MibTableColumn
vRtrMplsClassFwdPlcyFcNCFwdSet = _VRtrMplsClassFwdPlcyFcNCFwdSet_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 56, 1, 11),
    _VRtrMplsClassFwdPlcyFcNCFwdSet_Type()
)
vRtrMplsClassFwdPlcyFcNCFwdSet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsClassFwdPlcyFcNCFwdSet.setStatus("current")


class _VRtrMplsClassFwdPlcyDefFwdSet_Type(TmnxMplsClassFwdSetId):
    """Custom type vRtrMplsClassFwdPlcyDefFwdSet based on TmnxMplsClassFwdSetId"""
    defaultValue = 1


_VRtrMplsClassFwdPlcyDefFwdSet_Type.__name__ = "TmnxMplsClassFwdSetId"
_VRtrMplsClassFwdPlcyDefFwdSet_Object = MibTableColumn
vRtrMplsClassFwdPlcyDefFwdSet = _VRtrMplsClassFwdPlcyDefFwdSet_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 56, 1, 12),
    _VRtrMplsClassFwdPlcyDefFwdSet_Type()
)
vRtrMplsClassFwdPlcyDefFwdSet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsClassFwdPlcyDefFwdSet.setStatus("current")
_VRtrMplsClassFwdPlcyRefCount_Type = Gauge32
_VRtrMplsClassFwdPlcyRefCount_Object = MibTableColumn
vRtrMplsClassFwdPlcyRefCount = _VRtrMplsClassFwdPlcyRefCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 56, 1, 13),
    _VRtrMplsClassFwdPlcyRefCount_Type()
)
vRtrMplsClassFwdPlcyRefCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsClassFwdPlcyRefCount.setStatus("current")
_TmnxMplsNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxMplsNotifyPrefix = _TmnxMplsNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 6)
)
_TmnxMplsNotifications_ObjectIdentity = ObjectIdentity
tmnxMplsNotifications = _TmnxMplsNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 6, 0)
)
vRtrMplsLspEntry.registerAugmentions(
    ("TIMETRA-MPLS-MIB",
     "vRtrMplsLspStatEntry")
)
vRtrMplsLspStatEntry.setIndexNames(*vRtrMplsLspEntry.getIndexNames())
vRtrMplsLspPathEntry.registerAugmentions(
    ("TIMETRA-MPLS-MIB",
     "vRtrMplsLspPathStatEntry")
)
vRtrMplsLspPathStatEntry.setIndexNames(*vRtrMplsLspPathEntry.getIndexNames())
vRtrMplsGeneralEntry.registerAugmentions(
    ("TIMETRA-MPLS-MIB",
     "vRtrMplsGeneralStatEntry")
)
vRtrMplsGeneralStatEntry.setIndexNames(*vRtrMplsGeneralEntry.getIndexNames())
vRtrMplsIfEntry.registerAugmentions(
    ("TIMETRA-MPLS-MIB",
     "vRtrMplsIfStatEntry")
)
vRtrMplsIfStatEntry.setIndexNames(*vRtrMplsIfEntry.getIndexNames())
mplsTunnelARHopEntry.registerAugmentions(
    ("TIMETRA-MPLS-MIB",
     "vRtrMplsTunnelARHopEntry")
)
vRtrMplsTunnelARHopEntry.setIndexNames(*mplsTunnelARHopEntry.getIndexNames())
vRtrMplsP2mpInstEntry.registerAugmentions(
    ("TIMETRA-MPLS-MIB",
     "vRtrMplsP2mpInstStatEntry")
)
vRtrMplsP2mpInstStatEntry.setIndexNames(*vRtrMplsP2mpInstEntry.getIndexNames())
vRtrMplsS2lSubLspEntry.registerAugmentions(
    ("TIMETRA-MPLS-MIB",
     "vRtrMplsS2lSubLspStatEntry")
)
vRtrMplsS2lSubLspStatEntry.setIndexNames(*vRtrMplsS2lSubLspEntry.getIndexNames())
mplsInSegmentEntry.registerAugmentions(
    ("TIMETRA-MPLS-MIB",
     "vRtrMplsInSegmentEntry")
)
vRtrMplsInSegmentEntry.setIndexNames(*mplsInSegmentEntry.getIndexNames())
mplsOutSegmentEntry.registerAugmentions(
    ("TIMETRA-MPLS-MIB",
     "vRtrMplsOutSegmentEntry")
)
vRtrMplsOutSegmentEntry.setIndexNames(*mplsOutSegmentEntry.getIndexNames())
vRtrMplsLspStatsEntry.registerAugmentions(
    ("TIMETRA-MPLS-MIB",
     "vRtrMplsLspStatisticsEntry")
)
vRtrMplsLspStatisticsEntry.setIndexNames(*vRtrMplsLspStatsEntry.getIndexNames())
vRtrMplsLspPathEntry.registerAugmentions(
    ("TIMETRA-MPLS-MIB",
     "vRtrMplsLspPathOperEntry")
)
vRtrMplsLspPathOperEntry.setIndexNames(*vRtrMplsLspPathEntry.getIndexNames())
vRtrMplsLspEntry.registerAugmentions(
    ("TIMETRA-MPLS-MIB",
     "vRtrMplsLspExtEntry")
)
vRtrMplsLspExtEntry.setIndexNames(*vRtrMplsLspEntry.getIndexNames())

# Managed Objects groups

tmnxMplsLspPathGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 3)
)
tmnxMplsLspPathGroup.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLspPathTableSpinlock"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathRowStatus"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathLastChange"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathCos"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathProperties"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathBandwidth"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathBwProtect"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathPreference"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathCosSource"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathClassOfService"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathSetupPriority"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathHoldPriority"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathRecord"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathHopLimit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathSharing"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathAdminState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathInheritance"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathLspId"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathRetryTimeRemaining"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathTunnelARHopListIndex"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathNegotiatedMTU"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathFailCode"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathFailNodeAddr"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathAdminGroupInclude"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathAdminGroupExclude"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathAdaptive"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOptimizeTimer"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathNextOptimize"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperBandwidth"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathMBBState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathResignal"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathTunnelCRHopListIndex"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperMTU"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathRecordLabel"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathTimeUp"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathTimeDown"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathRetryAttempts"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathTransitionCount"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathCspfQueries"))
)
if mibBuilder.loadTexts:
    tmnxMplsLspPathGroup.setStatus("obsolete")

tmnxMplsXCGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 4)
)
tmnxMplsXCGroup.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsXCIndex"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInSegmentIfIndex"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInSegmentLabel"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsOutSegmentIndex"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsERHopTunnelIndex"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsARHopTunnelIndex"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsRsvpSessionIndex"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsXCFailCode"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsXCCHopTableIndex"))
)
if mibBuilder.loadTexts:
    tmnxMplsXCGroup.setStatus("current")

tmnxMplsIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 5)
)
tmnxMplsIfGroup.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsIfAdminState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsIfOperState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsIfAdminGroup"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsIfTxPktCount"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsIfRxPktCount"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsIfTxOctetCount"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsIfRxOctetCount"))
)
if mibBuilder.loadTexts:
    tmnxMplsIfGroup.setStatus("current")

tmnxMplsTunnelARHopGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 6)
)
tmnxMplsTunnelARHopGroup.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsTunnelARHopProtection"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsTunnelARHopRecordLabel"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsTunnelARHopRouterId"))
)
if mibBuilder.loadTexts:
    tmnxMplsTunnelARHopGroup.setStatus("current")

tmnxMplsTunnelCHopGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 7)
)
tmnxMplsTunnelCHopGroup.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsTunnelCHopAddrType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsTunnelCHopIpv4Addr"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsTunnelCHopIpv4PrefixLen"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsTunnelCHopIpv6Addr"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsTunnelCHopIpv6PrefixLen"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsTunnelCHopAsNumber"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsTunnelCHopLspId"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsTunnelCHopStrictOrLoose"))
)
if mibBuilder.loadTexts:
    tmnxMplsTunnelCHopGroup.setStatus("current")

tmnxMplsAdminGroupGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 8)
)
tmnxMplsAdminGroupGroup.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsAdminGroupRowStatus"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsAdminGroupValue"))
)
if mibBuilder.loadTexts:
    tmnxMplsAdminGroupGroup.setStatus("obsolete")

tmnxMplsFSGroupGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 9)
)
tmnxMplsFSGroupGroup.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsFSGroupRowStatus"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsFSGroupCost"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsFSGroupParamsRowStatus"))
)
if mibBuilder.loadTexts:
    tmnxMplsFSGroupGroup.setStatus("obsolete")

tmnxMplsNotifyObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 10)
)
tmnxMplsNotifyObjsGroup.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLspNotificationReasonCode"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathNotificationReasonCode"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsNotifyRow"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspIndex"))
)
if mibBuilder.loadTexts:
    tmnxMplsNotifyObjsGroup.setStatus("current")

tmnxMplsGlobalR2r1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 12)
)
tmnxMplsGlobalR2r1Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsGeneralLastChange"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralAdminState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralOperState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralPropagateTtl"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralTE"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralNewLspIndex"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralOptimizeTimer"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralFRObject"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralResignalTimer"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralStaticLspOriginate"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralStaticLspTransit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralStaticLspTerminate"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralDynamicLspOriginate"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralDynamicLspTransit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralDynamicLspTerminate"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralDetourLspOriginate"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralDetourLspTransit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralDetourLspTerminate"))
)
if mibBuilder.loadTexts:
    tmnxMplsGlobalR2r1Group.setStatus("obsolete")

tmnxMplsLspR2r1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 13)
)
tmnxMplsLspR2r1Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLspRowStatus"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspLastChange"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspName"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAdminState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspOperState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspFromAddr"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspToAddr"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspOutSegIndx"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspRetryTimer"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspRetryLimit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspMetric"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspDecrementTtl"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspCspf"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspFastReroute"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspFRHopLimit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspFRBandwidth"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspClassOfService"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspSetupPriority"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspHoldPriority"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspRecord"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPreference"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspBandwidth"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspBwProtect"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspHopLimit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspNegotiatedMTU"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspRsvpResvStyle"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspRsvpAdspec"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspFRMethod"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspFRNodeProtect"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAdminGroupInclude"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAdminGroupExclude"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAdaptive"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspInheritance"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspOptimizeTimer"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspOperFastReroute"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspFRObject"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspOctets"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPackets"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAge"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTimeUp"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTimeDown"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPrimaryTimeUp"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTransitions"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspLastTransition"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathChanges"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspLastPathChange"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspConfiguredPaths"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspStandbyPaths"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspOperationalPaths"))
)
if mibBuilder.loadTexts:
    tmnxMplsLspR2r1Group.setStatus("obsolete")

tmnxMplsLabelRangeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 15)
)
tmnxMplsLabelRangeGroup.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLabelRangeMin"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLabelRangeMax"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLabelRangeAging"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLabelRangeAvailable"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsStaticLSPLabelOwner"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsStaticSvcLabelOwner"))
)
if mibBuilder.loadTexts:
    tmnxMplsLabelRangeGroup.setStatus("current")

tmnxMplsGlobalV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 16)
)
tmnxMplsGlobalV5v0Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsGeneralLastChange"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralAdminState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralOperState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralPropagateTtl"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralTE"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralNewLspIndex"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralOptimizeTimer"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralFRObject"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralResignalTimer"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralStaticLspOriginate"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralStaticLspTransit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralStaticLspTerminate"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralDynamicLspOriginate"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralDynamicLspTransit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralDynamicLspTerminate"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralDetourLspOriginate"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralDetourLspTransit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralDetourLspTerminate"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralHoldTimer"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralDynamicBypass"))
)
if mibBuilder.loadTexts:
    tmnxMplsGlobalV5v0Group.setStatus("obsolete")

tmnxMplsLspV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 17)
)
tmnxMplsLspV5v0Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLspRowStatus"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspLastChange"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspName"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAdminState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspOperState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspFromAddr"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspToAddr"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspOutSegIndx"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspRetryTimer"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspRetryLimit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspMetric"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspDecrementTtl"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspCspf"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspFastReroute"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspFRHopLimit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspFRBandwidth"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspClassOfService"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspSetupPriority"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspHoldPriority"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspRecord"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPreference"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspBandwidth"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspBwProtect"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspHopLimit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspNegotiatedMTU"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspRsvpResvStyle"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspRsvpAdspec"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspFRMethod"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspFRNodeProtect"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAdminGroupInclude"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAdminGroupExclude"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAdaptive"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspInheritance"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspOptimizeTimer"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspOperFastReroute"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspFRObject"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspOctets"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPackets"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAge"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTimeUp"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTimeDown"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPrimaryTimeUp"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTransitions"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspLastTransition"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathChanges"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspLastPathChange"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspConfiguredPaths"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspStandbyPaths"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspOperationalPaths"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspHoldTimer"))
)
if mibBuilder.loadTexts:
    tmnxMplsLspV5v0Group.setStatus("obsolete")

tmnxMplsGlobalV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 18)
)
tmnxMplsGlobalV6v0Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsGeneralLastChange"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralAdminState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralOperState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralPropagateTtl"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralTE"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralNewLspIndex"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralOptimizeTimer"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralFRObject"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralResignalTimer"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralStaticLspOriginate"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralStaticLspTransit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralStaticLspTerminate"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralDynamicLspOriginate"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralDynamicLspTransit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralDynamicLspTerminate"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralDetourLspOriginate"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralDetourLspTransit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralDetourLspTerminate"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralHoldTimer"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralDynamicBypass"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralNextResignal"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralOperDownReason"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralSrlgFrr"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralSrlgFrrStrict"))
)
if mibBuilder.loadTexts:
    tmnxMplsGlobalV6v0Group.setStatus("obsolete")

tmnxMplsSrlgV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 19)
)
tmnxMplsSrlgV6v0Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsSrlgGrpTableLastChanged"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsSrlgGrpRowStatus"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsSrlgGrpLastChanged"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsSrlgGrpValue"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsIfSrlgGrpTblLastChanged"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsIfSrlgGrpRowStatus"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsIfSrlgGrpLastChanged"))
)
if mibBuilder.loadTexts:
    tmnxMplsSrlgV6v0Group.setStatus("obsolete")

tmnxMplsLspPathV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 20)
)
tmnxMplsLspPathV6v0Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLspPathSrlg"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathSrlgDisjoint"))
)
if mibBuilder.loadTexts:
    tmnxMplsLspPathV6v0Group.setStatus("current")

tmnxMplsIfV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 21)
)
tmnxMplsIfV6v0Group.setObjects(
    ("TIMETRA-MPLS-MIB", "vRtrMplsIfTeMetric")
)
if mibBuilder.loadTexts:
    tmnxMplsIfV6v0Group.setStatus("current")

tmnxMplsLspV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 22)
)
tmnxMplsLspV6v0Group.setObjects(
    ("TIMETRA-MPLS-MIB", "vRtrMplsLspCspfTeMetricEnabled")
)
if mibBuilder.loadTexts:
    tmnxMplsLspV6v0Group.setStatus("current")

tmnxMplsLspPathV6v1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 23)
)
tmnxMplsLspPathV6v1Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLspPathTableSpinlock"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathRowStatus"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathLastChange"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathCos"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathProperties"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathBandwidth"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathBwProtect"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathPreference"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathCosSource"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathClassOfService"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathSetupPriority"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathHoldPriority"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathRecord"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathHopLimit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathSharing"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathAdminState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathInheritance"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathLspId"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathRetryTimeRemaining"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathTunnelARHopListIndex"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathNegotiatedMTU"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathFailCode"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathFailNodeAddr"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathAdminGroupInclude"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathAdminGroupExclude"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathAdaptive"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOptimizeTimer"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathNextOptimize"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperBandwidth"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathResignal"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathTunnelCRHopListIndex"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperMTU"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathRecordLabel"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathTimeUp"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathTimeDown"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathRetryAttempts"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathTransitionCount"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathCspfQueries"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathLastResigAttempt"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathMetric"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathLastMBBType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathLastMBBEnd"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathLastMBBMetric"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathLastMBBState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathMBBTypeInProg"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathMBBStarted"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathMBBNextRetry"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathMBBRetryAttempts"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathMBBFailCode"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathMBBFailNodeArType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathMBBFailNodeAddr"))
)
if mibBuilder.loadTexts:
    tmnxMplsLspPathV6v1Group.setStatus("obsolete")

tmnxMplsObsoleteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 24)
)
tmnxMplsObsoleteGroup.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLspPathMBBState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsFSGroupCost"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsFSGroupParamsRowStatus"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsFSGroupRowStatus"))
)
if mibBuilder.loadTexts:
    tmnxMplsObsoleteGroup.setStatus("current")

tmnxMplsLspV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 25)
)
tmnxMplsLspV7v0Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLspP2mpId"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspClassType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspOperMetric"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspLdpOverRsvpInclude"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspLeastFill"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspVprnAutoBindInclude"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspConfP2mpInstances"))
)
if mibBuilder.loadTexts:
    tmnxMplsLspV7v0Group.setStatus("current")

tmnxMplsGlobalV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 26)
)
tmnxMplsGlobalV7v0Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsGeneralNewP2mpInstIndex"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralS2lOriginate"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralS2lTransit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralS2lTerminate"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralLeastFillMinThd"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGenLeastFillReoptiThd"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralUseSrlgDB"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInSegmentNumS2ls"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsOutSegmentNumS2ls"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralP2mpResigTimer"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralP2mpNextResignal"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralSecFastRetryTimer"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralStaticLspFRTimer"))
)
if mibBuilder.loadTexts:
    tmnxMplsGlobalV7v0Group.setStatus("current")

tmnxMplsP2mpInstanceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 27)
)
tmnxMplsP2mpInstanceGroup.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstTblLastChanged"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstRowStatus"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstLastChange"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstName"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstProperties"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstBandwidth"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstSetupPriority"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstHoldPriority"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstRecord"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstHopLimit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstAdminState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstOperState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstInheritance"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstLspId"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstNegotiatedMTU"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstFailCode"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstFailNodeArType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstFailNodeAddr"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstAdminGrpInclude"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstAdminGrpExclude"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstAdaptive"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstOperBandwidth"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstResignal"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstOperMTU"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstRecordLabel"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstLastResigAttpt"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstMetric"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstLastMBBType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstLastMBBEnd"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstLastMBBMetric"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstLastMBBState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstMBBTypeInProg"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstMBBStarted"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstMBBNextRetry"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstMBBRetryAttpts"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstMBBFailCode"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstMBBFailNodeType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstMBBFailNodeAddr"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstStatS2lChanges"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstStatLastS2lChange"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstStatConfiguredS2ls"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstStatOperationalS2ls"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstStatLastS2lTimeUp"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstStatLastS2lTimeDown"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstStatTimeUp"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstStatTimeDown"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstStatTransitions"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstStatLastTrans"))
)
if mibBuilder.loadTexts:
    tmnxMplsP2mpInstanceGroup.setStatus("current")

tmnxMplsP2mpS2lGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 28)
)
tmnxMplsP2mpS2lGroup.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspTblLastChanged"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspRowStatus"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspLastChange"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspProperties"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspAdminState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspOperState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubGroupId"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspId"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspRetryTimeRemain"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspNegotiatedMTU"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspFailCode"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspFailNodeArType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspFailNodeAddr"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspOperBandwidth"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspOperMTU"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspLastResigAttpt"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspLastMBBType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspLastMBBEnd"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspLastMBBMetric"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspLastMBBState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspMBBTypeInProg"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspMBBStarted"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspMBBNextRetry"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspMBBRetryAttpts"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspMBBFailCode"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspMBBFailNodeType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspMBBFailNodeAddr"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspUpTime"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspDownTime"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspTimeUp"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspTimeDown"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspRetryAttempts"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspTransitionCount"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspCspfQueries"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspTunARHopLtIndex"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspTunCRHopLtIndex"))
)
if mibBuilder.loadTexts:
    tmnxMplsP2mpS2lGroup.setStatus("current")

tmnxMplsNotifyObjsV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 29)
)
tmnxMplsNotifyObjsV7v0Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstNotifIndex"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspNtDstAddrType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspNtDstAddr"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstNotifReasonCode"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathCongChgPercent"))
)
if mibBuilder.loadTexts:
    tmnxMplsNotifyObjsV7v0Group.setStatus("current")

tmnxMplsLspPathV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 31)
)
tmnxMplsLspPathV7v0Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLspPathClassType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperMetric"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathResignalEligible"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathIsFastRetry"))
)
if mibBuilder.loadTexts:
    tmnxMplsLspPathV7v0Group.setStatus("current")

tmnxMplsSrlgV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 32)
)
tmnxMplsSrlgV7v0Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsSrlgDBRtrIdRowStatus"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsSrlgDBRtrIdAdminState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsSrlgDBRtrIdLastChanged"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsSrlgDBRtrIdTblLastChg"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsSrlgDBIfRowStatus"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsSrlgDBIfLastChanged"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsSrlgDBIfTblLastChanged"))
)
if mibBuilder.loadTexts:
    tmnxMplsSrlgV7v0Group.setStatus("current")

tmnxMplsLspStatsV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 33)
)
tmnxMplsLspStatsV7v0Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLspStatsAccntingPolicy"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspStatsCollectStats"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspStatsLastChanged"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspStatsRowStatus"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspStatsTblLastChgd"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspStatsAdminState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInProfileOctetsFc0"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInProfileOctetsFc0High32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInProfileOctetsFc0Low32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInProfileOctetsFc1"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInProfileOctetsFc1High32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInProfileOctetsFc1Low32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInProfileOctetsFc2"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInProfileOctetsFc2High32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInProfileOctetsFc2Low32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInProfileOctetsFc3"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInProfileOctetsFc3High32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInProfileOctetsFc3Low32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInProfileOctetsFc4"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInProfileOctetsFc4High32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInProfileOctetsFc4Low32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInProfileOctetsFc5"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInProfileOctetsFc5High32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInProfileOctetsFc5Low32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInProfileOctetsFc6"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInProfileOctetsFc6High32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInProfileOctetsFc6Low32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInProfileOctetsFc7"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInProfileOctetsFc7High32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInProfileOctetsFc7Low32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInProfilePktsFc0"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInProfilePktsFc0High32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInProfilePktsFc0Low32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInProfilePktsFc1"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInProfilePktsFc1High32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInProfilePktsFc1Low32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInProfilePktsFc2"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInProfilePktsFc2High32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInProfilePktsFc2Low32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInProfilePktsFc3"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInProfilePktsFc3High32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInProfilePktsFc3Low32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInProfilePktsFc4"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInProfilePktsFc4High32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInProfilePktsFc4Low32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInProfilePktsFc5"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInProfilePktsFc5High32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInProfilePktsFc5Low32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInProfilePktsFc6"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInProfilePktsFc6High32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInProfilePktsFc6Low32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInProfilePktsFc7"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInProfilePktsFc7High32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsInProfilePktsFc7Low32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsOutOfProfOctetsFc0"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsOutOfProfOctetsFc0High32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsOutOfProfOctetsFc0Low32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsOutOfProfOctetsFc1"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsOutOfProfOctetsFc1High32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsOutOfProfOctetsFc1Low32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsOutOfProfOctetsFc2"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsOutOfProfOctetsFc2High32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsOutOfProfOctetsFc2Low32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsOutOfProfOctetsFc3"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsOutOfProfOctetsFc3High32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsOutOfProfOctetsFc3Low32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsOutOfProfOctetsFc4"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsOutOfProfOctetsFc4High32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsOutOfProfOctetsFc4Low32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsOutOfProfOctetsFc5"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsOutOfProfOctetsFc5High32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsOutOfProfOctetsFc5Low32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsOutOfProfOctetsFc6"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsOutOfProfOctetsFc6High32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsOutOfProfOctetsFc6Low32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsOutOfProfOctetsFc7"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsOutOfProfOctetsFc7High32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsOutOfProfOctetsFc7Low32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsOutOfProfPktsFc0"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsOutOfProfPktsFc0High32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsOutOfProfPktsFc0Low32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsOutOfProfPktsFc1"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsOutOfProfPktsFc1High32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsOutOfProfPktsFc1Low32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsOutOfProfPktsFc2"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsOutOfProfPktsFc2High32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsOutOfProfPktsFc2Low32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsOutOfProfPktsFc3"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsOutOfProfPktsFc3High32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsOutOfProfPktsFc3Low32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsOutOfProfPktsFc4"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsOutOfProfPktsFc4High32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsOutOfProfPktsFc4Low32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsOutOfProfPktsFc5"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsOutOfProfPktsFc5High32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsOutOfProfPktsFc5Low32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsOutOfProfPktsFc6"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsOutOfProfPktsFc6High32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsOutOfProfPktsFc6Low32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsOutOfProfPktsFc7"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsOutOfProfPktsFc7High32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsOutOfProfPktsFc7Low32"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspStatsPSBMatch"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralLspEgrStatCount"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralLspIgrStatCount"))
)
if mibBuilder.loadTexts:
    tmnxMplsLspStatsV7v0Group.setStatus("current")

tmnxMplsLspV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 34)
)
tmnxMplsLspV8v0Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLspMainCTRetryLimit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspIgpShortcut"))
)
if mibBuilder.loadTexts:
    tmnxMplsLspV8v0Group.setStatus("current")

tmnxMplsLspPathV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 35)
)
tmnxMplsLspPathV8v0Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLspPathBackupCT"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathMainCTRetryRem"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperCT"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathNewPathIndex"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathMBBMainCTRetryRem"))
)
if mibBuilder.loadTexts:
    tmnxMplsLspPathV8v0Group.setStatus("current")

tmnxMplsNotifyObjsV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 36)
)
tmnxMplsNotifyObjsV8v0Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLspPathMbbStatus"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathMbbReasonCode"))
)
if mibBuilder.loadTexts:
    tmnxMplsNotifyObjsV8v0Group.setStatus("current")

tmnxMplsGlobalV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 38)
)
tmnxMplsGlobalV8v0Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsGeneralShortTTLPropLocal"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralShortTTLPropTrans"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralAutoBWDefSampMul"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralAutoBWDefAdjMul"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralExpBackoffRetry"))
)
if mibBuilder.loadTexts:
    tmnxMplsGlobalV8v0Group.setStatus("current")

tmnxMplsLspTemplateV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 39)
)
tmnxMplsLspTemplateV8v0Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateTblLastChgd"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateRowStatus"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateLastChanged"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateAdminState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateAdaptive"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateBandwidth"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateCspf"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateDefaultPath"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateAdmGrpIncl"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateAdmGrpExcl"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateFastReroute"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateFRMethod"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateFRHopLimit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateHopLimit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateRecord"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateRecordLabel"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateRetryLimit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateRetryTimer"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateCspfTeMetric"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspOriginTemplate"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateLspCount"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateMvpnRefCount"))
)
if mibBuilder.loadTexts:
    tmnxMplsLspTemplateV8v0Group.setStatus("current")

tmnxMplsLspAutoBWV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 40)
)
tmnxMplsLspAutoBWV8v0Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLspAutoBandwidth"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAutoBWTableLastChg"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAutoBWLastChange"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAutoBWAdjDNPercent"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAutoBWAdjDNMbps"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAutoBWAdjMultiplier"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAutoBWAdjUPPercent"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAutoBWAdjUPMbps"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAutoBWMaxBW"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAutoBWMinBW"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAutoBWMonitorBW"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAutoBWOverFlow"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAutoBWOvrFlwThreshold"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAutoBWOvrFlwBW"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAutoBWSampMultiplier"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAutoBWSampTime"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAutoBWLastAdj"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAutoBWLastAdjCause"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAutoBWNextAdj"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAutoBWMaxAvgRate"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAutoBWLastAvgRate"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAutoBWInheritance"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAutoBWCurrentBW"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAutoBWAdjTime"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAutoBWOvrFlwCount"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAutoBWSampCount"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAutoBWAdjCount"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAutoBWOperState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAutoBWSampInterval"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathSigBWMBBInProg"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathSigBWLastMBB"))
)
if mibBuilder.loadTexts:
    tmnxMplsLspAutoBWV8v0Group.setStatus("current")

tmnxMplsGlobalV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 41)
)
tmnxMplsGlobalV9v0Group.setObjects(
    ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralCspfOnLooseHop")
)
if mibBuilder.loadTexts:
    tmnxMplsGlobalV9v0Group.setStatus("current")

tmnxMplsLspV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 42)
)
tmnxMplsLspV9v0Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLspCspfToFirstLoose"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPropAdminGroup"))
)
if mibBuilder.loadTexts:
    tmnxMplsLspV9v0Group.setStatus("obsolete")

tmnxMplsLspV9v0R4Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 43)
)
tmnxMplsLspV9v0R4Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLspBgpShortcut"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspBgpTransportTunnel"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspSwitchStbyPath"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspSwitchStbyPathIndex"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspSwitchStbyPathForce"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralP2PMaxByPassAssoc"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspExcludeNodeAddr"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspExcludeNodeAddrType"))
)
if mibBuilder.loadTexts:
    tmnxMplsLspV9v0R4Group.setStatus("current")

tmnxMplsNotifyObjsV9v0R4Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 44)
)
tmnxMplsNotifyObjsV9v0R4Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLspSwitchStbyReasonCode"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspOldTunnelIndex"))
)
if mibBuilder.loadTexts:
    tmnxMplsNotifyObjsV9v0R4Group.setStatus("current")

tmnxMplsLspPathV9v0R4Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 46)
)
tmnxMplsLspPathV9v0R4Group.setObjects(
    ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathActiveByManual")
)
if mibBuilder.loadTexts:
    tmnxMplsLspPathV9v0R4Group.setStatus("current")

tmnxMplsGlobalV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 47)
)
tmnxMplsGlobalV10v0Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsGenP2pActPathFastRetry"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGenP2mpS2lFastRetry"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspIsFastRetry"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathTimeoutIn"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathMBBTimeoutIn"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspTimeoutIn"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspMBBTimeoutIn"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperSetupPriority"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperHoldPriority"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperRecord"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperRecordLabel"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperHopLimit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperAdminGrpIncl"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperAdminGrExcld"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperCspf"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperCspfToFrstLs"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperLeastFill"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperRsvpAdspec"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperFRNodeProtect"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperPropAdminGrp"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperFRHopLimit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGenLspInitRetryTimeout"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspIgpShortcutLfaType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLoggerEventBundling"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGenIssuMplsLockdown"))
)
if mibBuilder.loadTexts:
    tmnxMplsGlobalV10v0Group.setStatus("obsolete")

tmnxMplsTpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 48)
)
tmnxMplsTpGroup.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLspToAddrType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspFromAddrType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspToNodeId"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspFromNodeId"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspDestGlobalId"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspDestTunnelNum"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGenMplsTpLspOriginate"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGenMplsTpLspTransit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGenMplsTpLspTerminate"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGenMplsTpOrigPathInst"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGenMplsTpTranPathInst"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGenMplsTpTermPathInst"))
)
if mibBuilder.loadTexts:
    tmnxMplsTpGroup.setStatus("current")

tmnxMplsNotifyObjsV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 49)
)
tmnxMplsNotifyObjsV10v0Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsXCNotifRednIndicesBitMap"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsXCNotifyRednBundlingType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsXCNotifyRednNumOfBitsSet"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsXCNotifyRednStartIndex"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsXCNotifyRednEndIndex"))
)
if mibBuilder.loadTexts:
    tmnxMplsNotifyObjsV10v0Group.setStatus("current")

tmnxMplsFRAdminGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 51)
)
tmnxMplsFRAdminGroup.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsGenFRAdminGroup"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateFRPropAdmGrp"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspFRPropAdminGroup"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsTunnelCHopEgressAdmGrp"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperFRPropAdmGrp"))
)
if mibBuilder.loadTexts:
    tmnxMplsFRAdminGroup.setStatus("current")

tmnxMplsGlobalV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 52)
)
tmnxMplsGlobalV11v0Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperInterArea"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsTunnelCHopUnnumIfID"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsTunnelCHopRtrID"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsTunnelCHopIsABR"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsTunnelARHopUnnumIfID"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspRowStatus"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspLastChange"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspName"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAdminState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspOperState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspFromAddr"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspToAddr"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspOutSegIndx"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspRetryTimer"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspRetryLimit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspMetric"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspCspf"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspFastReroute"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspFRHopLimit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspFRBandwidth"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspSetupPriority"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspHoldPriority"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspRecord"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspBandwidth"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspHopLimit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspNegotiatedMTU"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspRsvpResvStyle"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspRsvpAdspec"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspFRMethod"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspFRNodeProtect"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAdminGroupInclude"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAdminGroupExclude"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAdaptive"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspInheritance"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspOptimizeTimer"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspOperFastReroute"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspFRObject"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspOctets"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPackets"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAge"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTimeUp"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTimeDown"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPrimaryTimeUp"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTransitions"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspLastTransition"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathChanges"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspLastPathChange"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspConfiguredPaths"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspStandbyPaths"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspOperationalPaths"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspHoldTimer"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathTableSpinlock"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathRowStatus"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathLastChange"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathProperties"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathBandwidth"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathPreference"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathSetupPriority"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathHoldPriority"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathRecord"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathHopLimit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathAdminState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathInheritance"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathLspId"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathRetryTimeRemaining"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathTunnelARHopListIndex"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathNegotiatedMTU"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathFailCode"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathFailNodeAddr"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathAdminGroupInclude"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathAdminGroupExclude"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathAdaptive"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOptimizeTimer"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathNextOptimize"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperBandwidth"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathResignal"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathTunnelCRHopListIndex"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperMTU"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathRecordLabel"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathTimeUp"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathTimeDown"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathRetryAttempts"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathTransitionCount"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathCspfQueries"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathLastResigAttempt"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathMetric"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathLastMBBType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathLastMBBEnd"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathLastMBBMetric"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathLastMBBState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathMBBTypeInProg"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathMBBStarted"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathMBBNextRetry"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathMBBRetryAttempts"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathMBBFailCode"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathMBBFailNodeArType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathMBBFailNodeAddr"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralLastChange"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralAdminState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralOperState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralNewLspIndex"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralOptimizeTimer"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralFRObject"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralResignalTimer"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralStaticLspOriginate"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralStaticLspTransit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralStaticLspTerminate"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralDynamicLspOriginate"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralDynamicLspTransit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralDynamicLspTerminate"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralDetourLspOriginate"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralDetourLspTransit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralDetourLspTerminate"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralHoldTimer"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralDynamicBypass"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralNextResignal"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralOperDownReason"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralSrlgFrr"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralSrlgFrrStrict"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplatePropAdmGrp"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLabelMaxStaticLspLabels"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLabelMaxStaticSvcLabels"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspInterArea"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGenP2pActPathFastRetry"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGenP2mpS2lFastRetry"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspIsFastRetry"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathTimeoutIn"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathMBBTimeoutIn"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspTimeoutIn"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspMBBTimeoutIn"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperSetupPriority"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperHoldPriority"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperRecord"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperRecordLabel"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperHopLimit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperAdminGrpIncl"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperAdminGrExcld"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperCspf"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperLeastFill"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperRsvpAdspec"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperFRNodeProtect"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperPropAdminGrp"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperFRHopLimit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGenLspInitRetryTimeout"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspIgpShortcutLfaType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLoggerEventBundling"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGenIssuMplsLockdown"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPropAdminGroup"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspIgpShortcutRelOffset"))
)
if mibBuilder.loadTexts:
    tmnxMplsGlobalV11v0Group.setStatus("obsolete")

tmnxMplsV11v0ObsoleteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 53)
)
tmnxMplsV11v0ObsoleteGroup.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLspDecrementTtl"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspClassOfService"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathCos"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathCosSource"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathClassOfService"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspBwProtect"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathBwProtect"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPreference"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathSharing"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralPropagateTtl"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralTE"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperCspfToFrstLs"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspCspfToFirstLoose"))
)
if mibBuilder.loadTexts:
    tmnxMplsV11v0ObsoleteGroup.setStatus("current")

tmnxMplsLspTemplateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 54)
)
tmnxMplsLspTemplateGroup.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateBgpShortcut"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateIgpShortcut"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateLdpOverRsvp"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateLeastFill"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateMetric"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateSetupPriority"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateHoldPriority"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateVprnAutoBind"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempIgpSCutLfaType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempIgpSCutRelOffset"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempAutoBandwidth"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempFRNodeProtect"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempAutoBWTblLastChg"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempAutoBWLastChg"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempAutoBWAdjDNPer"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempAutoBWAdjDNMbps"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempAutoBWAdjUPPer"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempAutoBWAdjUPMbps"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempAutoBWMaxBW"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempAutoBWMinBW"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempAutoBWMntrBW"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempAutoBWAdjMult"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempAutoBWOverFlow"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempAutoBWOvrFlwThr"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempAutoBWOvrFlwBW"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempAutoBWSampMult"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempAutoBWSampTime"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempAutoBWInherit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateEgrStats"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempCollectStats"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempAccntingPolicy"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsTemplPlcyBindTblLastChg"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplPlcyBindLastChg"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplPlcyBindRowStat"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplPlcyBind1"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplPlcyBind2"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplPlcyBind3"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplPlcyBind4"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplPlcyBind5"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplPlcyBindOneHop"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempAutoBWBeWeight"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempAutoBWL2Weight"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempAutoBWAfWeight"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempAutoBWL1Weight"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempAutoBWH2Weight"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempAutoBWEfWeight"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempAutoBWH1Weight"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempAutoBWNcWeight"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateFromAddrType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateFromAddr"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateClassType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempBkupClassType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempBgpTransportTunn"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempMainCTRetryLimit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplateRsvpAdspec"))
)
if mibBuilder.loadTexts:
    tmnxMplsLspTemplateGroup.setStatus("current")

tmnxMplsLspAutoBWFcWtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 56)
)
tmnxMplsLspAutoBWFcWtGroup.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLspAutoBWBeWeight"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAutoBWL2Weight"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAutoBWAfWeight"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAutoBWL1Weight"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAutoBWH2Weight"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAutoBWEfWeight"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAutoBWH1Weight"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAutoBWNcWeight"))
)
if mibBuilder.loadTexts:
    tmnxMplsLspAutoBWFcWtGroup.setStatus("current")

tmnxMplsGlobalV11v0R4Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 57)
)
tmnxMplsGlobalV11v0R4Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLspStatsTpOnly"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralMeshP2pOriginate"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralOneHopP2pOrigin"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGenRetryOnIgpOverload"))
)
if mibBuilder.loadTexts:
    tmnxMplsGlobalV11v0R4Group.setStatus("current")

tmnxMplsV12v0ObsoleteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 58)
)
tmnxMplsV12v0ObsoleteGroup.setObjects(
    ("TIMETRA-MPLS-MIB", "vRtrMplsLspBandwidth")
)
if mibBuilder.loadTexts:
    tmnxMplsV12v0ObsoleteGroup.setStatus("current")

tmnxMplsNotifyObjsIgpOverload = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 59)
)
tmnxMplsNotifyObjsIgpOverload.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsIgpOverloadRtrAddrType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsIgpOverloadRtrAddr"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsIgpOverloadIgpType"))
)
if mibBuilder.loadTexts:
    tmnxMplsNotifyObjsIgpOverload.setStatus("current")

tmnxMplsLspTempInStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 61)
)
tmnxMplsLspTempInStatsGroup.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLspTempInStatTblLstChg"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempInStatRowStatus"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempInStatLastChanged"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempInStatCollectStat"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempInStatAccntPolicy"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempInStatAdminState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempInStatMaxStats"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspStatsLspType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempInStatTotlSession"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspStatsEgrIndexUnAvail"))
)
if mibBuilder.loadTexts:
    tmnxMplsLspTempInStatsGroup.setStatus("current")

tmnxMplsAutoBwUnderflowGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 62)
)
tmnxMplsAutoBwUnderflowGroup.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLspAutoBWUnderFlow"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAutoBWUndFlwThreshold"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAutoBWUndFlwBW"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAutoBWUndFlwCount"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAutoBWMaxUndFlwBw"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempAutoBWUnderFlow"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempAutoBWUndFlwThr"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempAutoBWUndFlwBW"))
)
if mibBuilder.loadTexts:
    tmnxMplsAutoBwUnderflowGroup.setStatus("current")

tmnxMplsBgpLabelRetentionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 63)
)
tmnxMplsBgpLabelRetentionGroup.setObjects(
    ("TIMETRA-MPLS-MIB", "vRtrMplsLabelBgpLabelsHoldTimer")
)
if mibBuilder.loadTexts:
    tmnxMplsBgpLabelRetentionGroup.setStatus("current")

tmnxMplsGlobalV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 64)
)
tmnxMplsGlobalV12v0Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsTunnelCHopUnnumIfID"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsTunnelCHopRtrID"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsTunnelCHopIsABR"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsTunnelARHopUnnumIfID"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplatePropAdmGrp"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLabelMaxStaticLspLabels"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLabelMaxStaticSvcLabels"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspInterArea"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspIsFastRetry"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspTimeoutIn"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspMBBTimeoutIn"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLoggerEventBundling"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspIgpShortcutRelOffset"))
)
if mibBuilder.loadTexts:
    tmnxMplsGlobalV12v0Group.setStatus("obsolete")

tmnxMplsBypassOptGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 65)
)
tmnxMplsBypassOptGroup.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsGeneralBypassResigTimer"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGenBypassNextResignal"))
)
if mibBuilder.loadTexts:
    tmnxMplsBypassOptGroup.setStatus("current")

tmnxMplsGenV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 66)
)
tmnxMplsGenV12v0Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsGeneralLastChange"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralAdminState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralOperState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralNewLspIndex"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralOptimizeTimer"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralFRObject"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralResignalTimer"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralStaticLspOriginate"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralStaticLspTransit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralStaticLspTerminate"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralDynamicLspOriginate"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralDynamicLspTransit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralDynamicLspTerminate"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralDetourLspOriginate"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralDetourLspTransit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralDetourLspTerminate"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralHoldTimer"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralDynamicBypass"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralNextResignal"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralOperDownReason"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralSrlgFrr"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralSrlgFrrStrict"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGenMbbPrefCurrentHops"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGenP2pActPathFastRetry"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGenP2mpS2lFastRetry"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGenLspInitRetryTimeout"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGenIssuMplsLockdown"))
)
if mibBuilder.loadTexts:
    tmnxMplsGenV12v0Group.setStatus("current")

tmnxMplsLSPPathV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 67)
)
tmnxMplsLSPPathV12v0Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLspPathTableSpinlock"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathRowStatus"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathLastChange"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathProperties"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathBandwidth"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathPreference"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathSetupPriority"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathHoldPriority"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathRecord"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathHopLimit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathAdminState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathInheritance"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathLspId"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathRetryTimeRemaining"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathTunnelARHopListIndex"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathNegotiatedMTU"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathFailCode"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathFailNodeAddr"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathAdminGroupInclude"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathAdminGroupExclude"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathAdaptive"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOptimizeTimer"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathNextOptimize"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperBandwidth"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathResignal"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathTunnelCRHopListIndex"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperMTU"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathRecordLabel"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathTimeUp"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathTimeDown"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathRetryAttempts"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathTransitionCount"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathCspfQueries"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathLastResigAttempt"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathMetric"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathLastMBBType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathLastMBBEnd"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathLastMBBMetric"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathLastMBBState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathMBBTypeInProg"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathMBBStarted"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathMBBNextRetry"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathMBBRetryAttempts"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathMBBFailCode"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathMBBFailNodeArType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathMBBFailNodeAddr"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperInterArea"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathChanges"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathTimeoutIn"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathMBBTimeoutIn"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperSetupPriority"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperHoldPriority"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperRecord"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperRecordLabel"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperHopLimit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperAdminGrpIncl"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperAdminGrExcld"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperCspf"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperLeastFill"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperRsvpAdspec"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperFRNodeProtect"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperPropAdminGrp"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperFRHopLimit"))
)
if mibBuilder.loadTexts:
    tmnxMplsLSPPathV12v0Group.setStatus("current")

tmnxMplsLSPV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 68)
)
tmnxMplsLSPV12v0Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLspRowStatus"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspLastChange"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspName"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAdminState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspOperState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspFromAddr"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspToAddr"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspOutSegIndx"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspRetryTimer"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspRetryLimit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspMetric"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspCspf"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspFastReroute"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspFRHopLimit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspFRBandwidth"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspSetupPriority"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspHoldPriority"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspRecord"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspHopLimit"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspNegotiatedMTU"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspRsvpResvStyle"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspRsvpAdspec"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspFRMethod"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspFRNodeProtect"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAdminGroupInclude"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAdminGroupExclude"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAdaptive"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspInheritance"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspOptimizeTimer"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspOperFastReroute"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspFRObject"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspOctets"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPackets"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAge"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTimeUp"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTimeDown"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPrimaryTimeUp"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTransitions"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspLastTransition"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspLastPathChange"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspConfiguredPaths"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspStandbyPaths"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspOperationalPaths"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspHoldTimer"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspIgpShortcutLfaType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPropAdminGroup"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspIgpShortcutRelOffset"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspRevertTimer"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspRevertTimeRemain"))
)
if mibBuilder.loadTexts:
    tmnxMplsLSPV12v0Group.setStatus("current")

tmnxMplsLoadBalanceWtV13v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 70)
)
tmnxMplsLoadBalanceWtV13v0Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLspLoadBalancingWeight"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempLoadBalancingWt"))
)
if mibBuilder.loadTexts:
    tmnxMplsLoadBalanceWtV13v0Group.setStatus("current")

tmnxMplsLabelSegRouteV13v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 71)
)
tmnxMplsLabelSegRouteV13v0Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLabelSegRouteStartLabel"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLabelSegRouteEndLabel"))
)
if mibBuilder.loadTexts:
    tmnxMplsLabelSegRouteV13v0Group.setStatus("current")

tmnxMplsLabelStaticRgeV13v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 72)
)
tmnxMplsLabelStaticRgeV13v0Group.setObjects(
    ("TIMETRA-MPLS-MIB", "vRtrMplsLabelStaticLabelRange")
)
if mibBuilder.loadTexts:
    tmnxMplsLabelStaticRgeV13v0Group.setStatus("current")

tmnxMpls13v0ObsoleteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 73)
)
tmnxMpls13v0ObsoleteGroup.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLabelMaxStaticLspLabels"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLabelMaxStaticSvcLabels"))
)
if mibBuilder.loadTexts:
    tmnxMpls13v0ObsoleteGroup.setStatus("current")

tmnxMplsGlobalV13v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 74)
)
tmnxMplsGlobalV13v0Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsTunnelCHopUnnumIfID"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsTunnelCHopRtrID"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsTunnelCHopIsABR"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsTunnelARHopUnnumIfID"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplatePropAdmGrp"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspInterArea"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspIsFastRetry"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspTimeoutIn"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspMBBTimeoutIn"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLoggerEventBundling"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspIgpShortcutRelOffset"))
)
if mibBuilder.loadTexts:
    tmnxMplsGlobalV13v0Group.setStatus("current")

tmnxMplsClassBasedFwdV13v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 75)
)
tmnxMplsClassBasedFwdV13v0Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLspClassFwdingEnabled"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspFC"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempClassFwdEnabled"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempFC"))
)
if mibBuilder.loadTexts:
    tmnxMplsClassBasedFwdV13v0Group.setStatus("current")

tmnxMplsBfdOnLspV13v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 76)
)
tmnxMplsBfdOnLspV13v0Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLspBfdTemplateName"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspBfdEnable"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspBfdPingIntvl"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathBfdTemplateName"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathBfdEnable"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathBfdPingIntvl"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempBfdTemplateName"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempBfdEnable"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempBfdPingIntvl"))
)
if mibBuilder.loadTexts:
    tmnxMplsBfdOnLspV13v0Group.setStatus("current")

tmnxMplsAdminGroupObsoleteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 77)
)
tmnxMplsAdminGroupObsoleteGroup.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsAdminGroupRowStatus"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsAdminGroupValue"))
)
if mibBuilder.loadTexts:
    tmnxMplsAdminGroupObsoleteGroup.setStatus("current")

tmnxMplsIfSrlgV14v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 78)
)
tmnxMplsIfSrlgV14v0Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsIfSrlgGrpTblLastChanged"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsIfSrlgGrpRowStatus"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsIfSrlgGrpLastChanged"))
)
if mibBuilder.loadTexts:
    tmnxMplsIfSrlgV14v0Group.setStatus("current")

tmnxMplsSrlgObsoleteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 79)
)
tmnxMplsSrlgObsoleteGroup.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsSrlgGrpTableLastChanged"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsSrlgGrpRowStatus"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsSrlgGrpLastChanged"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsSrlgGrpValue"))
)
if mibBuilder.loadTexts:
    tmnxMplsSrlgObsoleteGroup.setStatus("current")

tmnxMplsSegRouting14v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 80)
)
tmnxMplsSegRouting14v0Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsGeneralNewLspSRIndex"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralSrTeLspOriginate"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralPceReport"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspExtPceCompute"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspExtPceControl"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspExtPceReport"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspExtTtmTunnelId"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspExtMaxSrLabels"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspExtTunnelId"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathProfTblLstChg"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathProfRowStatus"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathProfLastChange"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathProfGroupId"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathLastUpdateTime"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathLastUpdateId"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathLastUpdateState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathLastUpdFailCode"))
)
if mibBuilder.loadTexts:
    tmnxMplsSegRouting14v0Group.setStatus("current")

tmnxMplsEntropyLabel14v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 81)
)
tmnxMplsEntropyLabel14v0Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsGeneralEntropyLblRsvpTe"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspExtEntropyLabel"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspExtOperEntropyLabel"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspExtNegEntropyLbl"))
)
if mibBuilder.loadTexts:
    tmnxMplsEntropyLabel14v0Group.setStatus("current")

tmnxMplsLspTemplEL14v4Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 82)
)
tmnxMplsLspTemplEL14v4Group.setObjects(
    ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempEntropyLabel")
)
if mibBuilder.loadTexts:
    tmnxMplsLspTemplEL14v4Group.setStatus("current")

tmnxMplsSRLfaOvrhd14v4Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 83)
)
tmnxMplsSRLfaOvrhd14v4Group.setObjects(
    ("TIMETRA-MPLS-MIB", "vRtrMplsLspExtFrrOverheadLabel")
)
if mibBuilder.loadTexts:
    tmnxMplsSRLfaOvrhd14v4Group.setStatus("current")

tmnxMplsLspTempl15v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 84)
)
tmnxMplsLspTempl15v0Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLspTemplatePceReport"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspTempBfdFailureAction"))
)
if mibBuilder.loadTexts:
    tmnxMplsLspTempl15v0Group.setStatus("current")

tmnxMplsLspExt15v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 86)
)
tmnxMplsLspExt15v0Group.setObjects(
    ("TIMETRA-MPLS-MIB", "vRtrMplsLspExtBfdFailureAction")
)
if mibBuilder.loadTexts:
    tmnxMplsLspExt15v0Group.setStatus("current")

tmnxMplsClassFwdPlcy15v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 87)
)
tmnxMplsClassFwdPlcy15v0Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsClassFwdPlcyTblLstChg"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsClassFwdPlcyRowStatus"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsClassFwdPlcyLastChanged"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsClassFwdPlcyFcBEFwdSet"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsClassFwdPlcyFcL2FwdSet"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsClassFwdPlcyFcAFFwdSet"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsClassFwdPlcyFcL1FwdSet"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsClassFwdPlcyFcH2FwdSet"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsClassFwdPlcyFcEFFwdSet"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsClassFwdPlcyFcH1FwdSet"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsClassFwdPlcyFcNCFwdSet"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsClassFwdPlcyDefFwdSet"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsClassFwdPlcyRefCount"))
)
if mibBuilder.loadTexts:
    tmnxMplsClassFwdPlcy15v0Group.setStatus("current")


# Notification objects

vRtrMplsStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 6, 0, 1)
)
vRtrMplsStateChange.setObjects(
      *(("TIMETRA-VRTR-MIB", "vRtrID"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralAdminState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralOperState"))
)
if mibBuilder.loadTexts:
    vRtrMplsStateChange.setStatus(
        "current"
    )

vRtrMplsIfStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 6, 0, 2)
)
vRtrMplsIfStateChange.setObjects(
      *(("TIMETRA-VRTR-MIB", "vRtrID"),
        ("TIMETRA-VRTR-MIB", "vRtrIfIndex"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsIfAdminState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsIfOperState"))
)
if mibBuilder.loadTexts:
    vRtrMplsIfStateChange.setStatus(
        "current"
    )

vRtrMplsLspUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 6, 0, 3)
)
vRtrMplsLspUp.setObjects(
      *(("TIMETRA-VRTR-MIB", "vRtrID"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspIndex"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAdminState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspOperState"))
)
if mibBuilder.loadTexts:
    vRtrMplsLspUp.setStatus(
        "current"
    )

vRtrMplsLspDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 6, 0, 4)
)
vRtrMplsLspDown.setObjects(
      *(("TIMETRA-VRTR-MIB", "vRtrID"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspIndex"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAdminState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspOperState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspNotificationReasonCode"))
)
if mibBuilder.loadTexts:
    vRtrMplsLspDown.setStatus(
        "current"
    )

vRtrMplsLspPathUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 6, 0, 5)
)
vRtrMplsLspPathUp.setObjects(
      *(("TIMETRA-VRTR-MIB", "vRtrID"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspIndex"),
        ("MPLS-TE-MIB", "mplsTunnelIndex"),
        ("MPLS-TE-MIB", "mplsTunnelInstance"),
        ("MPLS-TE-MIB", "mplsTunnelIngressLSRId"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathAdminState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperState"))
)
if mibBuilder.loadTexts:
    vRtrMplsLspPathUp.setStatus(
        "current"
    )

vRtrMplsLspPathDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 6, 0, 6)
)
vRtrMplsLspPathDown.setObjects(
      *(("TIMETRA-VRTR-MIB", "vRtrID"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspIndex"),
        ("MPLS-TE-MIB", "mplsTunnelIndex"),
        ("MPLS-TE-MIB", "mplsTunnelInstance"),
        ("MPLS-TE-MIB", "mplsTunnelIngressLSRId"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathAdminState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathNotificationReasonCode"))
)
if mibBuilder.loadTexts:
    vRtrMplsLspPathDown.setStatus(
        "current"
    )

vRtrMplsLspPathRerouted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 6, 0, 7)
)
vRtrMplsLspPathRerouted.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLspPathAdminState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperState"))
)
if mibBuilder.loadTexts:
    vRtrMplsLspPathRerouted.setStatus(
        "current"
    )

vRtrMplsLspPathResignaled = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 6, 0, 8)
)
vRtrMplsLspPathResignaled.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLspPathAdminState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathLastMBBType"))
)
if mibBuilder.loadTexts:
    vRtrMplsLspPathResignaled.setStatus(
        "current"
    )

vRtrMplsP2mpInstanceUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 6, 0, 9)
)
vRtrMplsP2mpInstanceUp.setObjects(
      *(("TIMETRA-VRTR-MIB", "vRtrID"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspIndex"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstNotifIndex"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstAdminState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstOperState"))
)
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstanceUp.setStatus(
        "current"
    )

vRtrMplsP2mpInstanceDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 6, 0, 10)
)
vRtrMplsP2mpInstanceDown.setObjects(
      *(("TIMETRA-VRTR-MIB", "vRtrID"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspIndex"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstNotifIndex"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstAdminState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstOperState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstNotifReasonCode"))
)
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstanceDown.setStatus(
        "current"
    )

vRtrMplsS2lSubLspUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 6, 0, 11)
)
vRtrMplsS2lSubLspUp.setObjects(
      *(("TIMETRA-VRTR-MIB", "vRtrID"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspIndex"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstNotifIndex"),
        ("MPLS-TE-MIB", "mplsTunnelIndex"),
        ("MPLS-TE-MIB", "mplsTunnelInstance"),
        ("MPLS-TE-MIB", "mplsTunnelIngressLSRId"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspNtDstAddrType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspNtDstAddr"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspAdminState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspOperState"))
)
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspUp.setStatus(
        "current"
    )

vRtrMplsS2lSubLspDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 6, 0, 12)
)
vRtrMplsS2lSubLspDown.setObjects(
      *(("TIMETRA-VRTR-MIB", "vRtrID"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspIndex"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstNotifIndex"),
        ("MPLS-TE-MIB", "mplsTunnelIndex"),
        ("MPLS-TE-MIB", "mplsTunnelInstance"),
        ("MPLS-TE-MIB", "mplsTunnelIngressLSRId"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspNtDstAddrType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspNtDstAddr"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspAdminState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspOperState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstNotifReasonCode"))
)
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspDown.setStatus(
        "current"
    )

vRtrMplsS2lSubLspRerouted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 6, 0, 13)
)
vRtrMplsS2lSubLspRerouted.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspAdminState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspOperState"))
)
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspRerouted.setStatus(
        "current"
    )

vRtrMplsS2lSubLspResignaled = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 6, 0, 14)
)
vRtrMplsS2lSubLspResignaled.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspAdminState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspOperState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspLastMBBType"))
)
if mibBuilder.loadTexts:
    vRtrMplsS2lSubLspResignaled.setStatus(
        "current"
    )

vRtrMplsLspPathSoftPreempted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 6, 0, 15)
)
vRtrMplsLspPathSoftPreempted.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLspPathAdminState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperState"))
)
if mibBuilder.loadTexts:
    vRtrMplsLspPathSoftPreempted.setStatus(
        "current"
    )

vRtrMplsLspPathLstFillReoptElig = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 6, 0, 16)
)
vRtrMplsLspPathLstFillReoptElig.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLspPathResignalEligible"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathCongChgPercent"))
)
if mibBuilder.loadTexts:
    vRtrMplsLspPathLstFillReoptElig.setStatus(
        "current"
    )

vRtrMplsP2mpInstanceResignaled = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 6, 0, 17)
)
vRtrMplsP2mpInstanceResignaled.setObjects(
      *(("TIMETRA-VRTR-MIB", "vRtrID"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspIndex"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstNotifIndex"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstAdminState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstOperState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstLastMBBType"))
)
if mibBuilder.loadTexts:
    vRtrMplsP2mpInstanceResignaled.setStatus(
        "current"
    )

vRtrMplsResignalTimerExpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 6, 0, 18)
)
vRtrMplsResignalTimerExpired.setObjects(
    ("TIMETRA-MPLS-MIB", "vRtrMplsGeneralResignalTimer")
)
if mibBuilder.loadTexts:
    vRtrMplsResignalTimerExpired.setStatus(
        "current"
    )

vRtrMplsLspPathMbbStatusEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 6, 0, 19)
)
vRtrMplsLspPathMbbStatusEvent.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLspPathAdminState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathLastMBBType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathMbbStatus"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathMbbReasonCode"))
)
if mibBuilder.loadTexts:
    vRtrMplsLspPathMbbStatusEvent.setStatus(
        "current"
    )

vRtrMplsLspSwitchStbyFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 6, 0, 20)
)
vRtrMplsLspSwitchStbyFailure.setObjects(
      *(("TIMETRA-VRTR-MIB", "vRtrID"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspIndex"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspAdminState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspOperState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspSwitchStbyPathForce"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspSwitchStbyPathIndex"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspSwitchStbyReasonCode"))
)
if mibBuilder.loadTexts:
    vRtrMplsLspSwitchStbyFailure.setStatus(
        "current"
    )

vRtrMplsLspActivePathChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 6, 0, 21)
)
vRtrMplsLspActivePathChanged.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLspPathState"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathActiveByManual"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspOldTunnelIndex"))
)
if mibBuilder.loadTexts:
    vRtrMplsLspActivePathChanged.setStatus(
        "current"
    )

vRtrMplsXCBundleChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 6, 0, 22)
)
vRtrMplsXCBundleChange.setObjects(
      *(("TIMETRA-VRTR-MIB", "vRtrID"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsXCNotifRednIndicesBitMap"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsXCNotifyRednBundlingType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsXCNotifyRednNumOfBitsSet"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsXCNotifyRednStartIndex"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsXCNotifyRednEndIndex"))
)
if mibBuilder.loadTexts:
    vRtrMplsXCBundleChange.setStatus(
        "current"
    )

vRtrMplsLblRangeModify = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 6, 0, 23)
)
vRtrMplsLblRangeModify.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLabelMaxStaticLspLabels"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLabelMaxStaticSvcLabels"))
)
if mibBuilder.loadTexts:
    vRtrMplsLblRangeModify.setStatus(
        "obsolete"
    )

vRtrMplsNodeInIgpOverload = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 6, 0, 24)
)
vRtrMplsNodeInIgpOverload.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsGenRetryOnIgpOverload"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsIgpOverloadRtrAddrType"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsIgpOverloadRtrAddr"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsIgpOverloadIgpType"))
)
if mibBuilder.loadTexts:
    vRtrMplsNodeInIgpOverload.setStatus(
        "current"
    )


# Notifications groups

tmnxMplsNotificationR2r1Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 14)
)
tmnxMplsNotificationR2r1Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsStateChange"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsIfStateChange"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspUp"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspDown"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathUp"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathDown"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathRerouted"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathResignaled"))
)
if mibBuilder.loadTexts:
    tmnxMplsNotificationR2r1Group.setStatus(
        "current"
    )

tmnxMplsNotificationV7v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 30)
)
tmnxMplsNotificationV7v0Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstanceUp"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstanceDown"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspUp"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspDown"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspRerouted"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsS2lSubLspResignaled"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathSoftPreempted"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathLstFillReoptElig"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsP2mpInstanceResignaled"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsResignalTimerExpired"))
)
if mibBuilder.loadTexts:
    tmnxMplsNotificationV7v0Group.setStatus(
        "current"
    )

tmnxMplsNotificationV8v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 37)
)
tmnxMplsNotificationV8v0Group.setObjects(
    ("TIMETRA-MPLS-MIB", "vRtrMplsLspPathMbbStatusEvent")
)
if mibBuilder.loadTexts:
    tmnxMplsNotificationV8v0Group.setStatus(
        "current"
    )

tmnxMplsNotifV9v0R4Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 45)
)
tmnxMplsNotifV9v0R4Group.setObjects(
      *(("TIMETRA-MPLS-MIB", "vRtrMplsLspSwitchStbyFailure"),
        ("TIMETRA-MPLS-MIB", "vRtrMplsLspActivePathChanged"))
)
if mibBuilder.loadTexts:
    tmnxMplsNotifV9v0R4Group.setStatus(
        "current"
    )

tmnxMplsNotifyV10v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 50)
)
tmnxMplsNotifyV10v0Group.setObjects(
    ("TIMETRA-MPLS-MIB", "vRtrMplsXCBundleChange")
)
if mibBuilder.loadTexts:
    tmnxMplsNotifyV10v0Group.setStatus(
        "current"
    )

tmnxMplsNotifyV11v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 55)
)
tmnxMplsNotifyV11v0Group.setObjects(
    ("TIMETRA-MPLS-MIB", "vRtrMplsLblRangeModify")
)
if mibBuilder.loadTexts:
    tmnxMplsNotifyV11v0Group.setStatus(
        "obsolete"
    )

tmnxMplsIgpOverloadNotify = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 60)
)
tmnxMplsIgpOverloadNotify.setObjects(
    ("TIMETRA-MPLS-MIB", "vRtrMplsNodeInIgpOverload")
)
if mibBuilder.loadTexts:
    tmnxMplsIgpOverloadNotify.setStatus(
        "current"
    )

tmnxMplsObsoleteNotifyV12Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 69)
)
tmnxMplsObsoleteNotifyV12Group.setObjects(
    ("TIMETRA-MPLS-MIB", "vRtrMplsLblRangeModify")
)
if mibBuilder.loadTexts:
    tmnxMplsObsoleteNotifyV12Group.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tmnxMplsV3v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 1, 3)
)
tmnxMplsV3v0Compliance.setObjects(
      *(("TIMETRA-MPLS-MIB", "tmnxMplsGlobalR2r1Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspR2r1Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspPathGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsXCGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsIfGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsTunnelARHopGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsTunnelCHopGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsAdminGroupGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotificationR2r1Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLabelRangeGroup"))
)
if mibBuilder.loadTexts:
    tmnxMplsV3v0Compliance.setStatus(
        "obsolete"
    )

tmnxMplsV5v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 1, 4)
)
tmnxMplsV5v0Compliance.setObjects(
      *(("TIMETRA-MPLS-MIB", "tmnxMplsGlobalV5v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspV5v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspPathGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsXCGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsIfGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsTunnelARHopGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsTunnelCHopGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsAdminGroupGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotificationR2r1Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLabelRangeGroup"))
)
if mibBuilder.loadTexts:
    tmnxMplsV5v0Compliance.setStatus(
        "obsolete"
    )

tmnxMplsV6v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 1, 5)
)
tmnxMplsV6v0Compliance.setObjects(
      *(("TIMETRA-MPLS-MIB", "tmnxMplsGlobalV6v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspV5v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspPathGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsXCGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsIfGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsTunnelARHopGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsTunnelCHopGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsAdminGroupGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotificationR2r1Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLabelRangeGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsSrlgV6v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspPathV6v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsIfV6v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspV6v0Group"))
)
if mibBuilder.loadTexts:
    tmnxMplsV6v0Compliance.setStatus(
        "obsolete"
    )

tmnxMplsV6v1Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 1, 6)
)
tmnxMplsV6v1Compliance.setObjects(
      *(("TIMETRA-MPLS-MIB", "tmnxMplsGlobalV6v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspV5v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspPathV6v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsXCGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsIfGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsTunnelARHopGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsTunnelCHopGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsAdminGroupGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotificationR2r1Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLabelRangeGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsSrlgV6v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspPathV6v1Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsIfV6v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspV6v0Group"))
)
if mibBuilder.loadTexts:
    tmnxMplsV6v1Compliance.setStatus(
        "obsolete"
    )

tmnxMplsV7v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 1, 7)
)
tmnxMplsV7v0Compliance.setObjects(
      *(("TIMETRA-MPLS-MIB", "tmnxMplsGlobalV6v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspV5v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspPathV6v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsXCGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsIfGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsTunnelARHopGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsTunnelCHopGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsAdminGroupGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotificationR2r1Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLabelRangeGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsSrlgV6v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspPathV6v1Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsIfV6v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspV6v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsGlobalV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsP2mpInstanceGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsP2mpS2lGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotificationV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspPathV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsSrlgV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspStatsV7v0Group"))
)
if mibBuilder.loadTexts:
    tmnxMplsV7v0Compliance.setStatus(
        "obsolete"
    )

tmnxMplsV8v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 1, 8)
)
tmnxMplsV8v0Compliance.setObjects(
      *(("TIMETRA-MPLS-MIB", "tmnxMplsGlobalV6v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspV5v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspPathV6v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsXCGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsIfGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsTunnelARHopGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsTunnelCHopGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsAdminGroupGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotificationR2r1Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLabelRangeGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsSrlgV6v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspPathV6v1Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsIfV6v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspV6v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsGlobalV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsP2mpInstanceGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsP2mpS2lGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotificationV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspPathV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsSrlgV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspStatsV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspPathV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotifyObjsV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotificationV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsGlobalV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspAutoBWV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspTemplateV8v0Group"))
)
if mibBuilder.loadTexts:
    tmnxMplsV8v0Compliance.setStatus(
        "obsolete"
    )

tmnxMplsV9v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 1, 9)
)
tmnxMplsV9v0Compliance.setObjects(
      *(("TIMETRA-MPLS-MIB", "tmnxMplsGlobalV6v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspV5v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspPathV6v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsXCGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsIfGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsTunnelARHopGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsTunnelCHopGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsAdminGroupGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotificationR2r1Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLabelRangeGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsSrlgV6v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspPathV6v1Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsIfV6v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspV6v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsGlobalV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsP2mpInstanceGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsP2mpS2lGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotificationV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspPathV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsSrlgV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspStatsV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspPathV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotifyObjsV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotificationV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsGlobalV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspAutoBWV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspTemplateV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsGlobalV9v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspV9v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspV9v0R4Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotifV9v0R4Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspPathV9v0R4Group"))
)
if mibBuilder.loadTexts:
    tmnxMplsV9v0Compliance.setStatus(
        "obsolete"
    )

tmnxMplsV10v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 1, 10)
)
tmnxMplsV10v0Compliance.setObjects(
      *(("TIMETRA-MPLS-MIB", "tmnxMplsGlobalV6v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspV5v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspPathV6v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsXCGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsIfGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsTunnelARHopGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsTunnelCHopGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsAdminGroupGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotificationR2r1Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLabelRangeGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsSrlgV6v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspPathV6v1Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsIfV6v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspV6v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsGlobalV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsP2mpInstanceGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsP2mpS2lGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotificationV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspPathV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsSrlgV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspStatsV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspPathV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotifyObjsV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotificationV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsGlobalV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspAutoBWV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspTemplateV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsGlobalV9v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspV9v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspV9v0R4Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotifV9v0R4Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspPathV9v0R4Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsGlobalV10v0Group"))
)
if mibBuilder.loadTexts:
    tmnxMplsV10v0Compliance.setStatus(
        "obsolete"
    )

tmnxMplsV11v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 1, 11)
)
tmnxMplsV11v0Compliance.setObjects(
      *(("TIMETRA-MPLS-MIB", "tmnxMplsLspPathV6v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsXCGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsIfGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsTunnelARHopGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsTunnelCHopGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsAdminGroupGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotificationR2r1Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLabelRangeGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsSrlgV6v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsIfV6v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspV6v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsGlobalV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsP2mpInstanceGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsP2mpS2lGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotificationV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspPathV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsSrlgV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspStatsV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspPathV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotifyObjsV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotificationV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsGlobalV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspAutoBWV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspTemplateV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsGlobalV9v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspV9v0R4Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotifV9v0R4Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspPathV9v0R4Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsTpGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotifyObjsV10v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotifyV10v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsFRAdminGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsGlobalV11v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspTemplateGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotifyV11v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspAutoBWFcWtGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsGlobalV11v0R4Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotifyObjsIgpOverload"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsIgpOverloadNotify"))
)
if mibBuilder.loadTexts:
    tmnxMplsV11v0Compliance.setStatus(
        "obsolete"
    )

tmnxMplsV12v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 1, 12)
)
tmnxMplsV12v0Compliance.setObjects(
      *(("TIMETRA-MPLS-MIB", "tmnxMplsLspPathV6v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsXCGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsIfGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsTunnelARHopGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsTunnelCHopGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsAdminGroupGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotificationR2r1Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLabelRangeGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsSrlgV6v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsIfV6v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspV6v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsGlobalV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsP2mpInstanceGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsP2mpS2lGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotificationV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspPathV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsSrlgV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspStatsV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspPathV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotifyObjsV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotificationV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsGlobalV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspAutoBWV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspTemplateV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsGlobalV9v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspV9v0R4Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotifV9v0R4Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspPathV9v0R4Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsTpGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotifyObjsV10v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotifyV10v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsFRAdminGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspTemplateGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspAutoBWFcWtGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsGlobalV11v0R4Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotifyObjsIgpOverload"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsIgpOverloadNotify"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspTempInStatsGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsAutoBwUnderflowGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsBgpLabelRetentionGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsGlobalV12v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsBypassOptGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsGlobalV12v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLSPPathV12v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsGenV12v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLSPV12v0Group"))
)
if mibBuilder.loadTexts:
    tmnxMplsV12v0Compliance.setStatus(
        "obsolete"
    )

tmnxMplsV13v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 1, 13)
)
tmnxMplsV13v0Compliance.setObjects(
      *(("TIMETRA-MPLS-MIB", "tmnxMplsLspPathV6v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsXCGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsIfGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsTunnelARHopGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsTunnelCHopGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsAdminGroupGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotificationR2r1Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLabelRangeGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsSrlgV6v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsIfV6v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspV6v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsGlobalV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsP2mpInstanceGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsP2mpS2lGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotificationV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspPathV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsSrlgV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspStatsV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspPathV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotifyObjsV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotificationV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsGlobalV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspAutoBWV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspTemplateV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsGlobalV9v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspV9v0R4Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotifV9v0R4Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspPathV9v0R4Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsTpGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotifyObjsV10v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotifyV10v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsFRAdminGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspTemplateGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspAutoBWFcWtGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsGlobalV11v0R4Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotifyObjsIgpOverload"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsIgpOverloadNotify"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspTempInStatsGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsAutoBwUnderflowGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsBgpLabelRetentionGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsBypassOptGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLSPPathV12v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsGenV12v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLSPV12v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLoadBalanceWtV13v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLabelSegRouteV13v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLabelStaticRgeV13v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsGlobalV13v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsClassBasedFwdV13v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsBfdOnLspV13v0Group"))
)
if mibBuilder.loadTexts:
    tmnxMplsV13v0Compliance.setStatus(
        "obsolete"
    )

tmnxMplsV14v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 1, 14)
)
tmnxMplsV14v0Compliance.setObjects(
      *(("TIMETRA-MPLS-MIB", "tmnxMplsLspPathV6v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsXCGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsIfGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsTunnelARHopGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsTunnelCHopGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotificationR2r1Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLabelRangeGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsIfV6v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspV6v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsGlobalV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsP2mpInstanceGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsP2mpS2lGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotificationV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspPathV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsSrlgV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspStatsV7v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspPathV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotifyObjsV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotificationV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsGlobalV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspAutoBWV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspTemplateV8v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsGlobalV9v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspV9v0R4Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotifV9v0R4Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspPathV9v0R4Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsTpGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotifyObjsV10v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotifyV10v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsFRAdminGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspTemplateGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspAutoBWFcWtGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsGlobalV11v0R4Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsNotifyObjsIgpOverload"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsIgpOverloadNotify"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspTempInStatsGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsAutoBwUnderflowGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsBgpLabelRetentionGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsBypassOptGroup"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLSPPathV12v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsGenV12v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLSPV12v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLoadBalanceWtV13v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLabelSegRouteV13v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLabelStaticRgeV13v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsGlobalV13v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsClassBasedFwdV13v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsIfSrlgV14v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsBfdOnLspV13v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsSegRouting14v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsEntropyLabel14v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspTemplEL14v4Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsSRLfaOvrhd14v4Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsLspTempl15v0Group"))
)
if mibBuilder.loadTexts:
    tmnxMplsV14v0Compliance.setStatus(
        "current"
    )

tmnxMplsV15v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 1, 15)
)
tmnxMplsV15v0Compliance.setObjects(
      *(("TIMETRA-MPLS-MIB", "tmnxMplsLspExt15v0Group"),
        ("TIMETRA-MPLS-MIB", "tmnxMplsClassFwdPlcy15v0Group"))
)
if mibBuilder.loadTexts:
    tmnxMplsV15v0Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-MPLS-MIB",
    **{"TmnxMplsLspFailCode": TmnxMplsLspFailCode,
       "TmnxMplsLabelOwner": TmnxMplsLabelOwner,
       "TmnxMplsOperDownReasonCode": TmnxMplsOperDownReasonCode,
       "TmnxMplsMBBType": TmnxMplsMBBType,
       "TmnxMplsP2mpInstFailCode": TmnxMplsP2mpInstFailCode,
       "TmnxMplsRouterId": TmnxMplsRouterId,
       "TmnxMplsLspAutoBWLastAdjCause": TmnxMplsLspAutoBWLastAdjCause,
       "TmnxMplsLspBgpRSVPLSPTunState": TmnxMplsLspBgpRSVPLSPTunState,
       "TmnxMplsLspAddrType": TmnxMplsLspAddrType,
       "TmnxMplsClassFwdSetId": TmnxMplsClassFwdSetId,
       "timetraMplsMIBModule": timetraMplsMIBModule,
       "tmnxMplsConformance": tmnxMplsConformance,
       "tmnxMplsCompliances": tmnxMplsCompliances,
       "tmnxMplsV3v0Compliance": tmnxMplsV3v0Compliance,
       "tmnxMplsV5v0Compliance": tmnxMplsV5v0Compliance,
       "tmnxMplsV6v0Compliance": tmnxMplsV6v0Compliance,
       "tmnxMplsV6v1Compliance": tmnxMplsV6v1Compliance,
       "tmnxMplsV7v0Compliance": tmnxMplsV7v0Compliance,
       "tmnxMplsV8v0Compliance": tmnxMplsV8v0Compliance,
       "tmnxMplsV9v0Compliance": tmnxMplsV9v0Compliance,
       "tmnxMplsV10v0Compliance": tmnxMplsV10v0Compliance,
       "tmnxMplsV11v0Compliance": tmnxMplsV11v0Compliance,
       "tmnxMplsV12v0Compliance": tmnxMplsV12v0Compliance,
       "tmnxMplsV13v0Compliance": tmnxMplsV13v0Compliance,
       "tmnxMplsV14v0Compliance": tmnxMplsV14v0Compliance,
       "tmnxMplsV15v0Compliance": tmnxMplsV15v0Compliance,
       "tmnxMplsGroups": tmnxMplsGroups,
       "tmnxMplsLspPathGroup": tmnxMplsLspPathGroup,
       "tmnxMplsXCGroup": tmnxMplsXCGroup,
       "tmnxMplsIfGroup": tmnxMplsIfGroup,
       "tmnxMplsTunnelARHopGroup": tmnxMplsTunnelARHopGroup,
       "tmnxMplsTunnelCHopGroup": tmnxMplsTunnelCHopGroup,
       "tmnxMplsAdminGroupGroup": tmnxMplsAdminGroupGroup,
       "tmnxMplsFSGroupGroup": tmnxMplsFSGroupGroup,
       "tmnxMplsNotifyObjsGroup": tmnxMplsNotifyObjsGroup,
       "tmnxMplsGlobalR2r1Group": tmnxMplsGlobalR2r1Group,
       "tmnxMplsLspR2r1Group": tmnxMplsLspR2r1Group,
       "tmnxMplsNotificationR2r1Group": tmnxMplsNotificationR2r1Group,
       "tmnxMplsLabelRangeGroup": tmnxMplsLabelRangeGroup,
       "tmnxMplsGlobalV5v0Group": tmnxMplsGlobalV5v0Group,
       "tmnxMplsLspV5v0Group": tmnxMplsLspV5v0Group,
       "tmnxMplsGlobalV6v0Group": tmnxMplsGlobalV6v0Group,
       "tmnxMplsSrlgV6v0Group": tmnxMplsSrlgV6v0Group,
       "tmnxMplsLspPathV6v0Group": tmnxMplsLspPathV6v0Group,
       "tmnxMplsIfV6v0Group": tmnxMplsIfV6v0Group,
       "tmnxMplsLspV6v0Group": tmnxMplsLspV6v0Group,
       "tmnxMplsLspPathV6v1Group": tmnxMplsLspPathV6v1Group,
       "tmnxMplsObsoleteGroup": tmnxMplsObsoleteGroup,
       "tmnxMplsLspV7v0Group": tmnxMplsLspV7v0Group,
       "tmnxMplsGlobalV7v0Group": tmnxMplsGlobalV7v0Group,
       "tmnxMplsP2mpInstanceGroup": tmnxMplsP2mpInstanceGroup,
       "tmnxMplsP2mpS2lGroup": tmnxMplsP2mpS2lGroup,
       "tmnxMplsNotifyObjsV7v0Group": tmnxMplsNotifyObjsV7v0Group,
       "tmnxMplsNotificationV7v0Group": tmnxMplsNotificationV7v0Group,
       "tmnxMplsLspPathV7v0Group": tmnxMplsLspPathV7v0Group,
       "tmnxMplsSrlgV7v0Group": tmnxMplsSrlgV7v0Group,
       "tmnxMplsLspStatsV7v0Group": tmnxMplsLspStatsV7v0Group,
       "tmnxMplsLspV8v0Group": tmnxMplsLspV8v0Group,
       "tmnxMplsLspPathV8v0Group": tmnxMplsLspPathV8v0Group,
       "tmnxMplsNotifyObjsV8v0Group": tmnxMplsNotifyObjsV8v0Group,
       "tmnxMplsNotificationV8v0Group": tmnxMplsNotificationV8v0Group,
       "tmnxMplsGlobalV8v0Group": tmnxMplsGlobalV8v0Group,
       "tmnxMplsLspTemplateV8v0Group": tmnxMplsLspTemplateV8v0Group,
       "tmnxMplsLspAutoBWV8v0Group": tmnxMplsLspAutoBWV8v0Group,
       "tmnxMplsGlobalV9v0Group": tmnxMplsGlobalV9v0Group,
       "tmnxMplsLspV9v0Group": tmnxMplsLspV9v0Group,
       "tmnxMplsLspV9v0R4Group": tmnxMplsLspV9v0R4Group,
       "tmnxMplsNotifyObjsV9v0R4Group": tmnxMplsNotifyObjsV9v0R4Group,
       "tmnxMplsNotifV9v0R4Group": tmnxMplsNotifV9v0R4Group,
       "tmnxMplsLspPathV9v0R4Group": tmnxMplsLspPathV9v0R4Group,
       "tmnxMplsGlobalV10v0Group": tmnxMplsGlobalV10v0Group,
       "tmnxMplsTpGroup": tmnxMplsTpGroup,
       "tmnxMplsNotifyObjsV10v0Group": tmnxMplsNotifyObjsV10v0Group,
       "tmnxMplsNotifyV10v0Group": tmnxMplsNotifyV10v0Group,
       "tmnxMplsFRAdminGroup": tmnxMplsFRAdminGroup,
       "tmnxMplsGlobalV11v0Group": tmnxMplsGlobalV11v0Group,
       "tmnxMplsV11v0ObsoleteGroup": tmnxMplsV11v0ObsoleteGroup,
       "tmnxMplsLspTemplateGroup": tmnxMplsLspTemplateGroup,
       "tmnxMplsNotifyV11v0Group": tmnxMplsNotifyV11v0Group,
       "tmnxMplsLspAutoBWFcWtGroup": tmnxMplsLspAutoBWFcWtGroup,
       "tmnxMplsGlobalV11v0R4Group": tmnxMplsGlobalV11v0R4Group,
       "tmnxMplsV12v0ObsoleteGroup": tmnxMplsV12v0ObsoleteGroup,
       "tmnxMplsNotifyObjsIgpOverload": tmnxMplsNotifyObjsIgpOverload,
       "tmnxMplsIgpOverloadNotify": tmnxMplsIgpOverloadNotify,
       "tmnxMplsLspTempInStatsGroup": tmnxMplsLspTempInStatsGroup,
       "tmnxMplsAutoBwUnderflowGroup": tmnxMplsAutoBwUnderflowGroup,
       "tmnxMplsBgpLabelRetentionGroup": tmnxMplsBgpLabelRetentionGroup,
       "tmnxMplsGlobalV12v0Group": tmnxMplsGlobalV12v0Group,
       "tmnxMplsBypassOptGroup": tmnxMplsBypassOptGroup,
       "tmnxMplsGenV12v0Group": tmnxMplsGenV12v0Group,
       "tmnxMplsLSPPathV12v0Group": tmnxMplsLSPPathV12v0Group,
       "tmnxMplsLSPV12v0Group": tmnxMplsLSPV12v0Group,
       "tmnxMplsObsoleteNotifyV12Group": tmnxMplsObsoleteNotifyV12Group,
       "tmnxMplsLoadBalanceWtV13v0Group": tmnxMplsLoadBalanceWtV13v0Group,
       "tmnxMplsLabelSegRouteV13v0Group": tmnxMplsLabelSegRouteV13v0Group,
       "tmnxMplsLabelStaticRgeV13v0Group": tmnxMplsLabelStaticRgeV13v0Group,
       "tmnxMpls13v0ObsoleteGroup": tmnxMpls13v0ObsoleteGroup,
       "tmnxMplsGlobalV13v0Group": tmnxMplsGlobalV13v0Group,
       "tmnxMplsClassBasedFwdV13v0Group": tmnxMplsClassBasedFwdV13v0Group,
       "tmnxMplsBfdOnLspV13v0Group": tmnxMplsBfdOnLspV13v0Group,
       "tmnxMplsAdminGroupObsoleteGroup": tmnxMplsAdminGroupObsoleteGroup,
       "tmnxMplsIfSrlgV14v0Group": tmnxMplsIfSrlgV14v0Group,
       "tmnxMplsSrlgObsoleteGroup": tmnxMplsSrlgObsoleteGroup,
       "tmnxMplsSegRouting14v0Group": tmnxMplsSegRouting14v0Group,
       "tmnxMplsEntropyLabel14v0Group": tmnxMplsEntropyLabel14v0Group,
       "tmnxMplsLspTemplEL14v4Group": tmnxMplsLspTemplEL14v4Group,
       "tmnxMplsSRLfaOvrhd14v4Group": tmnxMplsSRLfaOvrhd14v4Group,
       "tmnxMplsLspTempl15v0Group": tmnxMplsLspTempl15v0Group,
       "tmnxMplsLspExt15v0Group": tmnxMplsLspExt15v0Group,
       "tmnxMplsClassFwdPlcy15v0Group": tmnxMplsClassFwdPlcy15v0Group,
       "tmnxMplsObjs": tmnxMplsObjs,
       "vRtrMplsLspTable": vRtrMplsLspTable,
       "vRtrMplsLspEntry": vRtrMplsLspEntry,
       "vRtrMplsLspIndex": vRtrMplsLspIndex,
       "vRtrMplsLspRowStatus": vRtrMplsLspRowStatus,
       "vRtrMplsLspLastChange": vRtrMplsLspLastChange,
       "vRtrMplsLspName": vRtrMplsLspName,
       "vRtrMplsLspAdminState": vRtrMplsLspAdminState,
       "vRtrMplsLspOperState": vRtrMplsLspOperState,
       "vRtrMplsLspFromAddr": vRtrMplsLspFromAddr,
       "vRtrMplsLspToAddr": vRtrMplsLspToAddr,
       "vRtrMplsLspType": vRtrMplsLspType,
       "vRtrMplsLspOutSegIndx": vRtrMplsLspOutSegIndx,
       "vRtrMplsLspRetryTimer": vRtrMplsLspRetryTimer,
       "vRtrMplsLspRetryLimit": vRtrMplsLspRetryLimit,
       "vRtrMplsLspMetric": vRtrMplsLspMetric,
       "vRtrMplsLspDecrementTtl": vRtrMplsLspDecrementTtl,
       "vRtrMplsLspCspf": vRtrMplsLspCspf,
       "vRtrMplsLspFastReroute": vRtrMplsLspFastReroute,
       "vRtrMplsLspFRHopLimit": vRtrMplsLspFRHopLimit,
       "vRtrMplsLspFRBandwidth": vRtrMplsLspFRBandwidth,
       "vRtrMplsLspClassOfService": vRtrMplsLspClassOfService,
       "vRtrMplsLspSetupPriority": vRtrMplsLspSetupPriority,
       "vRtrMplsLspHoldPriority": vRtrMplsLspHoldPriority,
       "vRtrMplsLspRecord": vRtrMplsLspRecord,
       "vRtrMplsLspPreference": vRtrMplsLspPreference,
       "vRtrMplsLspBandwidth": vRtrMplsLspBandwidth,
       "vRtrMplsLspBwProtect": vRtrMplsLspBwProtect,
       "vRtrMplsLspHopLimit": vRtrMplsLspHopLimit,
       "vRtrMplsLspNegotiatedMTU": vRtrMplsLspNegotiatedMTU,
       "vRtrMplsLspRsvpResvStyle": vRtrMplsLspRsvpResvStyle,
       "vRtrMplsLspRsvpAdspec": vRtrMplsLspRsvpAdspec,
       "vRtrMplsLspFRMethod": vRtrMplsLspFRMethod,
       "vRtrMplsLspFRNodeProtect": vRtrMplsLspFRNodeProtect,
       "vRtrMplsLspAdminGroupInclude": vRtrMplsLspAdminGroupInclude,
       "vRtrMplsLspAdminGroupExclude": vRtrMplsLspAdminGroupExclude,
       "vRtrMplsLspAdaptive": vRtrMplsLspAdaptive,
       "vRtrMplsLspInheritance": vRtrMplsLspInheritance,
       "vRtrMplsLspOptimizeTimer": vRtrMplsLspOptimizeTimer,
       "vRtrMplsLspOperFastReroute": vRtrMplsLspOperFastReroute,
       "vRtrMplsLspFRObject": vRtrMplsLspFRObject,
       "vRtrMplsLspHoldTimer": vRtrMplsLspHoldTimer,
       "vRtrMplsLspCspfTeMetricEnabled": vRtrMplsLspCspfTeMetricEnabled,
       "vRtrMplsLspP2mpId": vRtrMplsLspP2mpId,
       "vRtrMplsLspClassType": vRtrMplsLspClassType,
       "vRtrMplsLspOperMetric": vRtrMplsLspOperMetric,
       "vRtrMplsLspLdpOverRsvpInclude": vRtrMplsLspLdpOverRsvpInclude,
       "vRtrMplsLspLeastFill": vRtrMplsLspLeastFill,
       "vRtrMplsLspVprnAutoBindInclude": vRtrMplsLspVprnAutoBindInclude,
       "vRtrMplsLspMainCTRetryLimit": vRtrMplsLspMainCTRetryLimit,
       "vRtrMplsLspIgpShortcut": vRtrMplsLspIgpShortcut,
       "vRtrMplsLspOriginTemplate": vRtrMplsLspOriginTemplate,
       "vRtrMplsLspAutoBandwidth": vRtrMplsLspAutoBandwidth,
       "vRtrMplsLspCspfToFirstLoose": vRtrMplsLspCspfToFirstLoose,
       "vRtrMplsLspPropAdminGroup": vRtrMplsLspPropAdminGroup,
       "vRtrMplsLspBgpShortcut": vRtrMplsLspBgpShortcut,
       "vRtrMplsLspBgpTransportTunnel": vRtrMplsLspBgpTransportTunnel,
       "vRtrMplsLspSwitchStbyPath": vRtrMplsLspSwitchStbyPath,
       "vRtrMplsLspSwitchStbyPathIndex": vRtrMplsLspSwitchStbyPathIndex,
       "vRtrMplsLspSwitchStbyPathForce": vRtrMplsLspSwitchStbyPathForce,
       "vRtrMplsLspExcludeNodeAddrType": vRtrMplsLspExcludeNodeAddrType,
       "vRtrMplsLspExcludeNodeAddr": vRtrMplsLspExcludeNodeAddr,
       "vRtrMplsLspIgpShortcutLfaType": vRtrMplsLspIgpShortcutLfaType,
       "vRtrMplsLspToAddrType": vRtrMplsLspToAddrType,
       "vRtrMplsLspFromAddrType": vRtrMplsLspFromAddrType,
       "vRtrMplsLspToNodeId": vRtrMplsLspToNodeId,
       "vRtrMplsLspFromNodeId": vRtrMplsLspFromNodeId,
       "vRtrMplsLspDestGlobalId": vRtrMplsLspDestGlobalId,
       "vRtrMplsLspDestTunnelNum": vRtrMplsLspDestTunnelNum,
       "vRtrMplsLspFRPropAdminGroup": vRtrMplsLspFRPropAdminGroup,
       "vRtrMplsLspIgpShortcutRelOffset": vRtrMplsLspIgpShortcutRelOffset,
       "vRtrMplsLspRevertTimer": vRtrMplsLspRevertTimer,
       "vRtrMplsLspRevertTimeRemain": vRtrMplsLspRevertTimeRemain,
       "vRtrMplsLspLoadBalancingWeight": vRtrMplsLspLoadBalancingWeight,
       "vRtrMplsLspClassFwdingEnabled": vRtrMplsLspClassFwdingEnabled,
       "vRtrMplsLspFC": vRtrMplsLspFC,
       "vRtrMplsLspBfdTemplateName": vRtrMplsLspBfdTemplateName,
       "vRtrMplsLspBfdEnable": vRtrMplsLspBfdEnable,
       "vRtrMplsLspBfdPingIntvl": vRtrMplsLspBfdPingIntvl,
       "vRtrMplsLspStatTable": vRtrMplsLspStatTable,
       "vRtrMplsLspStatEntry": vRtrMplsLspStatEntry,
       "vRtrMplsLspOctets": vRtrMplsLspOctets,
       "vRtrMplsLspPackets": vRtrMplsLspPackets,
       "vRtrMplsLspAge": vRtrMplsLspAge,
       "vRtrMplsLspTimeUp": vRtrMplsLspTimeUp,
       "vRtrMplsLspTimeDown": vRtrMplsLspTimeDown,
       "vRtrMplsLspPrimaryTimeUp": vRtrMplsLspPrimaryTimeUp,
       "vRtrMplsLspTransitions": vRtrMplsLspTransitions,
       "vRtrMplsLspLastTransition": vRtrMplsLspLastTransition,
       "vRtrMplsLspPathChanges": vRtrMplsLspPathChanges,
       "vRtrMplsLspLastPathChange": vRtrMplsLspLastPathChange,
       "vRtrMplsLspConfiguredPaths": vRtrMplsLspConfiguredPaths,
       "vRtrMplsLspStandbyPaths": vRtrMplsLspStandbyPaths,
       "vRtrMplsLspOperationalPaths": vRtrMplsLspOperationalPaths,
       "vRtrMplsLspConfP2mpInstances": vRtrMplsLspConfP2mpInstances,
       "vRtrMplsLspStatsEgrIndexUnAvail": vRtrMplsLspStatsEgrIndexUnAvail,
       "vRtrMplsLspPathTableSpinlock": vRtrMplsLspPathTableSpinlock,
       "vRtrMplsLspPathTable": vRtrMplsLspPathTable,
       "vRtrMplsLspPathEntry": vRtrMplsLspPathEntry,
       "vRtrMplsLspPathRowStatus": vRtrMplsLspPathRowStatus,
       "vRtrMplsLspPathLastChange": vRtrMplsLspPathLastChange,
       "vRtrMplsLspPathType": vRtrMplsLspPathType,
       "vRtrMplsLspPathCos": vRtrMplsLspPathCos,
       "vRtrMplsLspPathProperties": vRtrMplsLspPathProperties,
       "vRtrMplsLspPathBandwidth": vRtrMplsLspPathBandwidth,
       "vRtrMplsLspPathBwProtect": vRtrMplsLspPathBwProtect,
       "vRtrMplsLspPathState": vRtrMplsLspPathState,
       "vRtrMplsLspPathPreference": vRtrMplsLspPathPreference,
       "vRtrMplsLspPathCosSource": vRtrMplsLspPathCosSource,
       "vRtrMplsLspPathClassOfService": vRtrMplsLspPathClassOfService,
       "vRtrMplsLspPathSetupPriority": vRtrMplsLspPathSetupPriority,
       "vRtrMplsLspPathHoldPriority": vRtrMplsLspPathHoldPriority,
       "vRtrMplsLspPathRecord": vRtrMplsLspPathRecord,
       "vRtrMplsLspPathHopLimit": vRtrMplsLspPathHopLimit,
       "vRtrMplsLspPathSharing": vRtrMplsLspPathSharing,
       "vRtrMplsLspPathAdminState": vRtrMplsLspPathAdminState,
       "vRtrMplsLspPathOperState": vRtrMplsLspPathOperState,
       "vRtrMplsLspPathInheritance": vRtrMplsLspPathInheritance,
       "vRtrMplsLspPathLspId": vRtrMplsLspPathLspId,
       "vRtrMplsLspPathRetryTimeRemaining": vRtrMplsLspPathRetryTimeRemaining,
       "vRtrMplsLspPathTunnelARHopListIndex": vRtrMplsLspPathTunnelARHopListIndex,
       "vRtrMplsLspPathNegotiatedMTU": vRtrMplsLspPathNegotiatedMTU,
       "vRtrMplsLspPathFailCode": vRtrMplsLspPathFailCode,
       "vRtrMplsLspPathFailNodeAddr": vRtrMplsLspPathFailNodeAddr,
       "vRtrMplsLspPathAdminGroupInclude": vRtrMplsLspPathAdminGroupInclude,
       "vRtrMplsLspPathAdminGroupExclude": vRtrMplsLspPathAdminGroupExclude,
       "vRtrMplsLspPathAdaptive": vRtrMplsLspPathAdaptive,
       "vRtrMplsLspPathOptimizeTimer": vRtrMplsLspPathOptimizeTimer,
       "vRtrMplsLspPathNextOptimize": vRtrMplsLspPathNextOptimize,
       "vRtrMplsLspPathOperBandwidth": vRtrMplsLspPathOperBandwidth,
       "vRtrMplsLspPathMBBState": vRtrMplsLspPathMBBState,
       "vRtrMplsLspPathResignal": vRtrMplsLspPathResignal,
       "vRtrMplsLspPathTunnelCRHopListIndex": vRtrMplsLspPathTunnelCRHopListIndex,
       "vRtrMplsLspPathOperMTU": vRtrMplsLspPathOperMTU,
       "vRtrMplsLspPathRecordLabel": vRtrMplsLspPathRecordLabel,
       "vRtrMplsLspPathSrlg": vRtrMplsLspPathSrlg,
       "vRtrMplsLspPathSrlgDisjoint": vRtrMplsLspPathSrlgDisjoint,
       "vRtrMplsLspPathLastResigAttempt": vRtrMplsLspPathLastResigAttempt,
       "vRtrMplsLspPathMetric": vRtrMplsLspPathMetric,
       "vRtrMplsLspPathLastMBBType": vRtrMplsLspPathLastMBBType,
       "vRtrMplsLspPathLastMBBEnd": vRtrMplsLspPathLastMBBEnd,
       "vRtrMplsLspPathLastMBBMetric": vRtrMplsLspPathLastMBBMetric,
       "vRtrMplsLspPathLastMBBState": vRtrMplsLspPathLastMBBState,
       "vRtrMplsLspPathMBBTypeInProg": vRtrMplsLspPathMBBTypeInProg,
       "vRtrMplsLspPathMBBStarted": vRtrMplsLspPathMBBStarted,
       "vRtrMplsLspPathMBBNextRetry": vRtrMplsLspPathMBBNextRetry,
       "vRtrMplsLspPathMBBRetryAttempts": vRtrMplsLspPathMBBRetryAttempts,
       "vRtrMplsLspPathMBBFailCode": vRtrMplsLspPathMBBFailCode,
       "vRtrMplsLspPathMBBFailNodeArType": vRtrMplsLspPathMBBFailNodeArType,
       "vRtrMplsLspPathMBBFailNodeAddr": vRtrMplsLspPathMBBFailNodeAddr,
       "vRtrMplsLspPathClassType": vRtrMplsLspPathClassType,
       "vRtrMplsLspPathOperMetric": vRtrMplsLspPathOperMetric,
       "vRtrMplsLspPathResignalEligible": vRtrMplsLspPathResignalEligible,
       "vRtrMplsLspPathIsFastRetry": vRtrMplsLspPathIsFastRetry,
       "vRtrMplsLspPathBackupCT": vRtrMplsLspPathBackupCT,
       "vRtrMplsLspPathMainCTRetryRem": vRtrMplsLspPathMainCTRetryRem,
       "vRtrMplsLspPathOperCT": vRtrMplsLspPathOperCT,
       "vRtrMplsLspPathNewPathIndex": vRtrMplsLspPathNewPathIndex,
       "vRtrMplsLspPathMBBMainCTRetryRem": vRtrMplsLspPathMBBMainCTRetryRem,
       "vRtrMplsLspPathSigBWMBBInProg": vRtrMplsLspPathSigBWMBBInProg,
       "vRtrMplsLspPathSigBWLastMBB": vRtrMplsLspPathSigBWLastMBB,
       "vRtrMplsLspPathActiveByManual": vRtrMplsLspPathActiveByManual,
       "vRtrMplsLspPathTimeoutIn": vRtrMplsLspPathTimeoutIn,
       "vRtrMplsLspPathMBBTimeoutIn": vRtrMplsLspPathMBBTimeoutIn,
       "vRtrMplsLspPathBfdTemplateName": vRtrMplsLspPathBfdTemplateName,
       "vRtrMplsLspPathBfdEnable": vRtrMplsLspPathBfdEnable,
       "vRtrMplsLspPathBfdPingIntvl": vRtrMplsLspPathBfdPingIntvl,
       "vRtrMplsLspPathLastUpdateTime": vRtrMplsLspPathLastUpdateTime,
       "vRtrMplsLspPathLastUpdateId": vRtrMplsLspPathLastUpdateId,
       "vRtrMplsLspPathLastUpdateState": vRtrMplsLspPathLastUpdateState,
       "vRtrMplsLspPathLastUpdFailCode": vRtrMplsLspPathLastUpdFailCode,
       "vRtrMplsLspPathStatTable": vRtrMplsLspPathStatTable,
       "vRtrMplsLspPathStatEntry": vRtrMplsLspPathStatEntry,
       "vRtrMplsLspPathTimeUp": vRtrMplsLspPathTimeUp,
       "vRtrMplsLspPathTimeDown": vRtrMplsLspPathTimeDown,
       "vRtrMplsLspPathRetryAttempts": vRtrMplsLspPathRetryAttempts,
       "vRtrMplsLspPathTransitionCount": vRtrMplsLspPathTransitionCount,
       "vRtrMplsLspPathCspfQueries": vRtrMplsLspPathCspfQueries,
       "vRtrMplsXCTable": vRtrMplsXCTable,
       "vRtrMplsXCEntry": vRtrMplsXCEntry,
       "vRtrMplsXCIndex": vRtrMplsXCIndex,
       "vRtrMplsInSegmentIfIndex": vRtrMplsInSegmentIfIndex,
       "vRtrMplsInSegmentLabel": vRtrMplsInSegmentLabel,
       "vRtrMplsOutSegmentIndex": vRtrMplsOutSegmentIndex,
       "vRtrMplsERHopTunnelIndex": vRtrMplsERHopTunnelIndex,
       "vRtrMplsARHopTunnelIndex": vRtrMplsARHopTunnelIndex,
       "vRtrMplsRsvpSessionIndex": vRtrMplsRsvpSessionIndex,
       "vRtrMplsXCFailCode": vRtrMplsXCFailCode,
       "vRtrMplsXCCHopTableIndex": vRtrMplsXCCHopTableIndex,
       "vRtrMplsGeneralTable": vRtrMplsGeneralTable,
       "vRtrMplsGeneralEntry": vRtrMplsGeneralEntry,
       "vRtrMplsGeneralLastChange": vRtrMplsGeneralLastChange,
       "vRtrMplsGeneralAdminState": vRtrMplsGeneralAdminState,
       "vRtrMplsGeneralOperState": vRtrMplsGeneralOperState,
       "vRtrMplsGeneralPropagateTtl": vRtrMplsGeneralPropagateTtl,
       "vRtrMplsGeneralTE": vRtrMplsGeneralTE,
       "vRtrMplsGeneralNewLspIndex": vRtrMplsGeneralNewLspIndex,
       "vRtrMplsGeneralOptimizeTimer": vRtrMplsGeneralOptimizeTimer,
       "vRtrMplsGeneralFRObject": vRtrMplsGeneralFRObject,
       "vRtrMplsGeneralResignalTimer": vRtrMplsGeneralResignalTimer,
       "vRtrMplsGeneralHoldTimer": vRtrMplsGeneralHoldTimer,
       "vRtrMplsGeneralDynamicBypass": vRtrMplsGeneralDynamicBypass,
       "vRtrMplsGeneralNextResignal": vRtrMplsGeneralNextResignal,
       "vRtrMplsGeneralOperDownReason": vRtrMplsGeneralOperDownReason,
       "vRtrMplsGeneralSrlgFrr": vRtrMplsGeneralSrlgFrr,
       "vRtrMplsGeneralSrlgFrrStrict": vRtrMplsGeneralSrlgFrrStrict,
       "vRtrMplsGeneralNewP2mpInstIndex": vRtrMplsGeneralNewP2mpInstIndex,
       "vRtrMplsGeneralLeastFillMinThd": vRtrMplsGeneralLeastFillMinThd,
       "vRtrMplsGenLeastFillReoptiThd": vRtrMplsGenLeastFillReoptiThd,
       "vRtrMplsGeneralUseSrlgDB": vRtrMplsGeneralUseSrlgDB,
       "vRtrMplsGeneralP2mpResigTimer": vRtrMplsGeneralP2mpResigTimer,
       "vRtrMplsGeneralP2mpNextResignal": vRtrMplsGeneralP2mpNextResignal,
       "vRtrMplsGeneralSecFastRetryTimer": vRtrMplsGeneralSecFastRetryTimer,
       "vRtrMplsGeneralShortTTLPropLocal": vRtrMplsGeneralShortTTLPropLocal,
       "vRtrMplsGeneralShortTTLPropTrans": vRtrMplsGeneralShortTTLPropTrans,
       "vRtrMplsGeneralStaticLspFRTimer": vRtrMplsGeneralStaticLspFRTimer,
       "vRtrMplsGeneralAutoBWDefSampMul": vRtrMplsGeneralAutoBWDefSampMul,
       "vRtrMplsGeneralAutoBWDefAdjMul": vRtrMplsGeneralAutoBWDefAdjMul,
       "vRtrMplsGeneralExpBackoffRetry": vRtrMplsGeneralExpBackoffRetry,
       "vRtrMplsGeneralCspfOnLooseHop": vRtrMplsGeneralCspfOnLooseHop,
       "vRtrMplsGeneralP2PMaxByPassAssoc": vRtrMplsGeneralP2PMaxByPassAssoc,
       "vRtrMplsGenP2pActPathFastRetry": vRtrMplsGenP2pActPathFastRetry,
       "vRtrMplsGenP2mpS2lFastRetry": vRtrMplsGenP2mpS2lFastRetry,
       "vRtrMplsGenLspInitRetryTimeout": vRtrMplsGenLspInitRetryTimeout,
       "vRtrMplsLoggerEventBundling": vRtrMplsLoggerEventBundling,
       "vRtrMplsGenIssuMplsLockdown": vRtrMplsGenIssuMplsLockdown,
       "vRtrMplsGenFRAdminGroup": vRtrMplsGenFRAdminGroup,
       "vRtrMplsGenRetryOnIgpOverload": vRtrMplsGenRetryOnIgpOverload,
       "vRtrMplsGenMbbPrefCurrentHops": vRtrMplsGenMbbPrefCurrentHops,
       "vRtrMplsGeneralBypassResigTimer": vRtrMplsGeneralBypassResigTimer,
       "vRtrMplsGenBypassNextResignal": vRtrMplsGenBypassNextResignal,
       "vRtrMplsGeneralNewLspSRIndex": vRtrMplsGeneralNewLspSRIndex,
       "vRtrMplsGeneralPceReport": vRtrMplsGeneralPceReport,
       "vRtrMplsGeneralEntropyLblRsvpTe": vRtrMplsGeneralEntropyLblRsvpTe,
       "vRtrMplsGeneralStatTable": vRtrMplsGeneralStatTable,
       "vRtrMplsGeneralStatEntry": vRtrMplsGeneralStatEntry,
       "vRtrMplsGeneralStaticLspOriginate": vRtrMplsGeneralStaticLspOriginate,
       "vRtrMplsGeneralStaticLspTransit": vRtrMplsGeneralStaticLspTransit,
       "vRtrMplsGeneralStaticLspTerminate": vRtrMplsGeneralStaticLspTerminate,
       "vRtrMplsGeneralDynamicLspOriginate": vRtrMplsGeneralDynamicLspOriginate,
       "vRtrMplsGeneralDynamicLspTransit": vRtrMplsGeneralDynamicLspTransit,
       "vRtrMplsGeneralDynamicLspTerminate": vRtrMplsGeneralDynamicLspTerminate,
       "vRtrMplsGeneralDetourLspOriginate": vRtrMplsGeneralDetourLspOriginate,
       "vRtrMplsGeneralDetourLspTransit": vRtrMplsGeneralDetourLspTransit,
       "vRtrMplsGeneralDetourLspTerminate": vRtrMplsGeneralDetourLspTerminate,
       "vRtrMplsGeneralS2lOriginate": vRtrMplsGeneralS2lOriginate,
       "vRtrMplsGeneralS2lTransit": vRtrMplsGeneralS2lTransit,
       "vRtrMplsGeneralS2lTerminate": vRtrMplsGeneralS2lTerminate,
       "vRtrMplsGeneralLspEgrStatCount": vRtrMplsGeneralLspEgrStatCount,
       "vRtrMplsGeneralLspIgrStatCount": vRtrMplsGeneralLspIgrStatCount,
       "vRtrMplsGenMplsTpLspOriginate": vRtrMplsGenMplsTpLspOriginate,
       "vRtrMplsGenMplsTpLspTransit": vRtrMplsGenMplsTpLspTransit,
       "vRtrMplsGenMplsTpLspTerminate": vRtrMplsGenMplsTpLspTerminate,
       "vRtrMplsGenMplsTpOrigPathInst": vRtrMplsGenMplsTpOrigPathInst,
       "vRtrMplsGenMplsTpTranPathInst": vRtrMplsGenMplsTpTranPathInst,
       "vRtrMplsGenMplsTpTermPathInst": vRtrMplsGenMplsTpTermPathInst,
       "vRtrMplsGeneralMeshP2pOriginate": vRtrMplsGeneralMeshP2pOriginate,
       "vRtrMplsGeneralOneHopP2pOrigin": vRtrMplsGeneralOneHopP2pOrigin,
       "vRtrMplsGeneralSrTeLspOriginate": vRtrMplsGeneralSrTeLspOriginate,
       "vRtrMplsIfTable": vRtrMplsIfTable,
       "vRtrMplsIfEntry": vRtrMplsIfEntry,
       "vRtrMplsIfAdminState": vRtrMplsIfAdminState,
       "vRtrMplsIfOperState": vRtrMplsIfOperState,
       "vRtrMplsIfAdminGroup": vRtrMplsIfAdminGroup,
       "vRtrMplsIfTeMetric": vRtrMplsIfTeMetric,
       "vRtrMplsIfStatTable": vRtrMplsIfStatTable,
       "vRtrMplsIfStatEntry": vRtrMplsIfStatEntry,
       "vRtrMplsIfTxPktCount": vRtrMplsIfTxPktCount,
       "vRtrMplsIfRxPktCount": vRtrMplsIfRxPktCount,
       "vRtrMplsIfTxOctetCount": vRtrMplsIfTxOctetCount,
       "vRtrMplsIfRxOctetCount": vRtrMplsIfRxOctetCount,
       "vRtrMplsTunnelARHopTable": vRtrMplsTunnelARHopTable,
       "vRtrMplsTunnelARHopEntry": vRtrMplsTunnelARHopEntry,
       "vRtrMplsTunnelARHopProtection": vRtrMplsTunnelARHopProtection,
       "vRtrMplsTunnelARHopRecordLabel": vRtrMplsTunnelARHopRecordLabel,
       "vRtrMplsTunnelARHopRouterId": vRtrMplsTunnelARHopRouterId,
       "vRtrMplsTunnelARHopUnnumIfID": vRtrMplsTunnelARHopUnnumIfID,
       "vRtrMplsTunnelCHopTable": vRtrMplsTunnelCHopTable,
       "vRtrMplsTunnelCHopEntry": vRtrMplsTunnelCHopEntry,
       "vRtrMplsTunnelCHopListIndex": vRtrMplsTunnelCHopListIndex,
       "vRtrMplsTunnelCHopIndex": vRtrMplsTunnelCHopIndex,
       "vRtrMplsTunnelCHopAddrType": vRtrMplsTunnelCHopAddrType,
       "vRtrMplsTunnelCHopIpv4Addr": vRtrMplsTunnelCHopIpv4Addr,
       "vRtrMplsTunnelCHopIpv4PrefixLen": vRtrMplsTunnelCHopIpv4PrefixLen,
       "vRtrMplsTunnelCHopIpv6Addr": vRtrMplsTunnelCHopIpv6Addr,
       "vRtrMplsTunnelCHopIpv6PrefixLen": vRtrMplsTunnelCHopIpv6PrefixLen,
       "vRtrMplsTunnelCHopAsNumber": vRtrMplsTunnelCHopAsNumber,
       "vRtrMplsTunnelCHopLspId": vRtrMplsTunnelCHopLspId,
       "vRtrMplsTunnelCHopStrictOrLoose": vRtrMplsTunnelCHopStrictOrLoose,
       "vRtrMplsTunnelCHopEgressAdmGrp": vRtrMplsTunnelCHopEgressAdmGrp,
       "vRtrMplsTunnelCHopUnnumIfID": vRtrMplsTunnelCHopUnnumIfID,
       "vRtrMplsTunnelCHopRtrID": vRtrMplsTunnelCHopRtrID,
       "vRtrMplsTunnelCHopIsABR": vRtrMplsTunnelCHopIsABR,
       "vRtrMplsAdminGroupTable": vRtrMplsAdminGroupTable,
       "vRtrMplsAdminGroupEntry": vRtrMplsAdminGroupEntry,
       "vRtrMplsAdminGroupName": vRtrMplsAdminGroupName,
       "vRtrMplsAdminGroupRowStatus": vRtrMplsAdminGroupRowStatus,
       "vRtrMplsAdminGroupValue": vRtrMplsAdminGroupValue,
       "vRtrMplsFSGroupTable": vRtrMplsFSGroupTable,
       "vRtrMplsFSGroupEntry": vRtrMplsFSGroupEntry,
       "vRtrMplsFSGroupName": vRtrMplsFSGroupName,
       "vRtrMplsFSGroupRowStatus": vRtrMplsFSGroupRowStatus,
       "vRtrMplsFSGroupCost": vRtrMplsFSGroupCost,
       "vRtrMplsFSGroupParamsTable": vRtrMplsFSGroupParamsTable,
       "vRtrMplsFSGroupParamsEntry": vRtrMplsFSGroupParamsEntry,
       "vRtrMplsFSGroupParamsFromAddr": vRtrMplsFSGroupParamsFromAddr,
       "vRtrMplsFSGroupParamsToAddr": vRtrMplsFSGroupParamsToAddr,
       "vRtrMplsFSGroupParamsRowStatus": vRtrMplsFSGroupParamsRowStatus,
       "tmnxMplsNotificationObjects": tmnxMplsNotificationObjects,
       "vRtrMplsLspNotificationReasonCode": vRtrMplsLspNotificationReasonCode,
       "vRtrMplsLspPathNotificationReasonCode": vRtrMplsLspPathNotificationReasonCode,
       "vRtrMplsNotifyRow": vRtrMplsNotifyRow,
       "vRtrMplsP2mpInstNotifIndex": vRtrMplsP2mpInstNotifIndex,
       "vRtrMplsP2mpInstNotifReasonCode": vRtrMplsP2mpInstNotifReasonCode,
       "vRtrMplsS2lSubLspNtDstAddrType": vRtrMplsS2lSubLspNtDstAddrType,
       "vRtrMplsS2lSubLspNtDstAddr": vRtrMplsS2lSubLspNtDstAddr,
       "vRtrMplsLspPathCongChgPercent": vRtrMplsLspPathCongChgPercent,
       "vRtrMplsLspPathMbbStatus": vRtrMplsLspPathMbbStatus,
       "vRtrMplsLspPathMbbReasonCode": vRtrMplsLspPathMbbReasonCode,
       "vRtrMplsLspSwitchStbyReasonCode": vRtrMplsLspSwitchStbyReasonCode,
       "vRtrMplsLspOldTunnelIndex": vRtrMplsLspOldTunnelIndex,
       "vRtrMplsXCNotifRednIndicesBitMap": vRtrMplsXCNotifRednIndicesBitMap,
       "vRtrMplsXCNotifyRednBundlingType": vRtrMplsXCNotifyRednBundlingType,
       "vRtrMplsXCNotifyRednNumOfBitsSet": vRtrMplsXCNotifyRednNumOfBitsSet,
       "vRtrMplsXCNotifyRednStartIndex": vRtrMplsXCNotifyRednStartIndex,
       "vRtrMplsXCNotifyRednEndIndex": vRtrMplsXCNotifyRednEndIndex,
       "vRtrMplsIgpOverloadRtrAddrType": vRtrMplsIgpOverloadRtrAddrType,
       "vRtrMplsIgpOverloadRtrAddr": vRtrMplsIgpOverloadRtrAddr,
       "vRtrMplsIgpOverloadIgpType": vRtrMplsIgpOverloadIgpType,
       "vRtrMplsLabelRangeTable": vRtrMplsLabelRangeTable,
       "vRtrMplsLabelRangeEntry": vRtrMplsLabelRangeEntry,
       "vRtrMplsLabelType": vRtrMplsLabelType,
       "vRtrMplsLabelRangeMin": vRtrMplsLabelRangeMin,
       "vRtrMplsLabelRangeMax": vRtrMplsLabelRangeMax,
       "vRtrMplsLabelRangeAging": vRtrMplsLabelRangeAging,
       "vRtrMplsLabelRangeAvailable": vRtrMplsLabelRangeAvailable,
       "vRtrMplsStaticLSPLabelTable": vRtrMplsStaticLSPLabelTable,
       "vRtrMplsStaticLSPLabelEntry": vRtrMplsStaticLSPLabelEntry,
       "vRtrMplsStaticLSPLabel": vRtrMplsStaticLSPLabel,
       "vRtrMplsStaticLSPLabelOwner": vRtrMplsStaticLSPLabelOwner,
       "vRtrMplsStaticSvcLabelTable": vRtrMplsStaticSvcLabelTable,
       "vRtrMplsStaticSvcLabelEntry": vRtrMplsStaticSvcLabelEntry,
       "vRtrMplsStaticSvcLabel": vRtrMplsStaticSvcLabel,
       "vRtrMplsStaticSvcLabelOwner": vRtrMplsStaticSvcLabelOwner,
       "vRtrMplsSrlgGrpTableLastChanged": vRtrMplsSrlgGrpTableLastChanged,
       "vRtrMplsSrlgGrpTable": vRtrMplsSrlgGrpTable,
       "vRtrMplsSrlgGrpEntry": vRtrMplsSrlgGrpEntry,
       "vRtrMplsSrlgGrpName": vRtrMplsSrlgGrpName,
       "vRtrMplsSrlgGrpRowStatus": vRtrMplsSrlgGrpRowStatus,
       "vRtrMplsSrlgGrpLastChanged": vRtrMplsSrlgGrpLastChanged,
       "vRtrMplsSrlgGrpValue": vRtrMplsSrlgGrpValue,
       "vRtrMplsIfSrlgGrpTblLastChanged": vRtrMplsIfSrlgGrpTblLastChanged,
       "vRtrMplsIfSrlgGrpTable": vRtrMplsIfSrlgGrpTable,
       "vRtrMplsIfSrlgGrpEntry": vRtrMplsIfSrlgGrpEntry,
       "vRtrMplsIfSrlgGrpName": vRtrMplsIfSrlgGrpName,
       "vRtrMplsIfSrlgGrpRowStatus": vRtrMplsIfSrlgGrpRowStatus,
       "vRtrMplsIfSrlgGrpLastChanged": vRtrMplsIfSrlgGrpLastChanged,
       "vRtrMplsP2mpInstTblLastChanged": vRtrMplsP2mpInstTblLastChanged,
       "vRtrMplsP2mpInstTable": vRtrMplsP2mpInstTable,
       "vRtrMplsP2mpInstEntry": vRtrMplsP2mpInstEntry,
       "vRtrMplsP2mpInstIndex": vRtrMplsP2mpInstIndex,
       "vRtrMplsP2mpInstRowStatus": vRtrMplsP2mpInstRowStatus,
       "vRtrMplsP2mpInstLastChange": vRtrMplsP2mpInstLastChange,
       "vRtrMplsP2mpInstName": vRtrMplsP2mpInstName,
       "vRtrMplsP2mpInstType": vRtrMplsP2mpInstType,
       "vRtrMplsP2mpInstProperties": vRtrMplsP2mpInstProperties,
       "vRtrMplsP2mpInstBandwidth": vRtrMplsP2mpInstBandwidth,
       "vRtrMplsP2mpInstState": vRtrMplsP2mpInstState,
       "vRtrMplsP2mpInstSetupPriority": vRtrMplsP2mpInstSetupPriority,
       "vRtrMplsP2mpInstHoldPriority": vRtrMplsP2mpInstHoldPriority,
       "vRtrMplsP2mpInstRecord": vRtrMplsP2mpInstRecord,
       "vRtrMplsP2mpInstHopLimit": vRtrMplsP2mpInstHopLimit,
       "vRtrMplsP2mpInstAdminState": vRtrMplsP2mpInstAdminState,
       "vRtrMplsP2mpInstOperState": vRtrMplsP2mpInstOperState,
       "vRtrMplsP2mpInstInheritance": vRtrMplsP2mpInstInheritance,
       "vRtrMplsP2mpInstLspId": vRtrMplsP2mpInstLspId,
       "vRtrMplsP2mpInstNegotiatedMTU": vRtrMplsP2mpInstNegotiatedMTU,
       "vRtrMplsP2mpInstFailCode": vRtrMplsP2mpInstFailCode,
       "vRtrMplsP2mpInstFailNodeArType": vRtrMplsP2mpInstFailNodeArType,
       "vRtrMplsP2mpInstFailNodeAddr": vRtrMplsP2mpInstFailNodeAddr,
       "vRtrMplsP2mpInstAdminGrpInclude": vRtrMplsP2mpInstAdminGrpInclude,
       "vRtrMplsP2mpInstAdminGrpExclude": vRtrMplsP2mpInstAdminGrpExclude,
       "vRtrMplsP2mpInstAdaptive": vRtrMplsP2mpInstAdaptive,
       "vRtrMplsP2mpInstOperBandwidth": vRtrMplsP2mpInstOperBandwidth,
       "vRtrMplsP2mpInstResignal": vRtrMplsP2mpInstResignal,
       "vRtrMplsP2mpInstOperMTU": vRtrMplsP2mpInstOperMTU,
       "vRtrMplsP2mpInstRecordLabel": vRtrMplsP2mpInstRecordLabel,
       "vRtrMplsP2mpInstLastResigAttpt": vRtrMplsP2mpInstLastResigAttpt,
       "vRtrMplsP2mpInstMetric": vRtrMplsP2mpInstMetric,
       "vRtrMplsP2mpInstLastMBBType": vRtrMplsP2mpInstLastMBBType,
       "vRtrMplsP2mpInstLastMBBEnd": vRtrMplsP2mpInstLastMBBEnd,
       "vRtrMplsP2mpInstLastMBBMetric": vRtrMplsP2mpInstLastMBBMetric,
       "vRtrMplsP2mpInstLastMBBState": vRtrMplsP2mpInstLastMBBState,
       "vRtrMplsP2mpInstMBBTypeInProg": vRtrMplsP2mpInstMBBTypeInProg,
       "vRtrMplsP2mpInstMBBStarted": vRtrMplsP2mpInstMBBStarted,
       "vRtrMplsP2mpInstMBBNextRetry": vRtrMplsP2mpInstMBBNextRetry,
       "vRtrMplsP2mpInstMBBRetryAttpts": vRtrMplsP2mpInstMBBRetryAttpts,
       "vRtrMplsP2mpInstMBBFailCode": vRtrMplsP2mpInstMBBFailCode,
       "vRtrMplsP2mpInstMBBFailNodeType": vRtrMplsP2mpInstMBBFailNodeType,
       "vRtrMplsP2mpInstMBBFailNodeAddr": vRtrMplsP2mpInstMBBFailNodeAddr,
       "vRtrMplsP2mpInstStatTable": vRtrMplsP2mpInstStatTable,
       "vRtrMplsP2mpInstStatEntry": vRtrMplsP2mpInstStatEntry,
       "vRtrMplsP2mpInstStatS2lChanges": vRtrMplsP2mpInstStatS2lChanges,
       "vRtrMplsP2mpInstStatLastS2lChange": vRtrMplsP2mpInstStatLastS2lChange,
       "vRtrMplsP2mpInstStatConfiguredS2ls": vRtrMplsP2mpInstStatConfiguredS2ls,
       "vRtrMplsP2mpInstStatOperationalS2ls": vRtrMplsP2mpInstStatOperationalS2ls,
       "vRtrMplsP2mpInstStatLastS2lTimeUp": vRtrMplsP2mpInstStatLastS2lTimeUp,
       "vRtrMplsP2mpInstStatLastS2lTimeDown": vRtrMplsP2mpInstStatLastS2lTimeDown,
       "vRtrMplsP2mpInstStatTimeUp": vRtrMplsP2mpInstStatTimeUp,
       "vRtrMplsP2mpInstStatTimeDown": vRtrMplsP2mpInstStatTimeDown,
       "vRtrMplsP2mpInstStatTransitions": vRtrMplsP2mpInstStatTransitions,
       "vRtrMplsP2mpInstStatLastTrans": vRtrMplsP2mpInstStatLastTrans,
       "vRtrMplsS2lSubLspTblLastChanged": vRtrMplsS2lSubLspTblLastChanged,
       "vRtrMplsS2lSubLspTable": vRtrMplsS2lSubLspTable,
       "vRtrMplsS2lSubLspEntry": vRtrMplsS2lSubLspEntry,
       "vRtrMplsS2lSubLspDstAddrType": vRtrMplsS2lSubLspDstAddrType,
       "vRtrMplsS2lSubLspDstAddr": vRtrMplsS2lSubLspDstAddr,
       "vRtrMplsS2lSubLspRowStatus": vRtrMplsS2lSubLspRowStatus,
       "vRtrMplsS2lSubLspLastChange": vRtrMplsS2lSubLspLastChange,
       "vRtrMplsS2lSubLspType": vRtrMplsS2lSubLspType,
       "vRtrMplsS2lSubLspProperties": vRtrMplsS2lSubLspProperties,
       "vRtrMplsS2lSubLspState": vRtrMplsS2lSubLspState,
       "vRtrMplsS2lSubLspAdminState": vRtrMplsS2lSubLspAdminState,
       "vRtrMplsS2lSubLspOperState": vRtrMplsS2lSubLspOperState,
       "vRtrMplsS2lSubGroupId": vRtrMplsS2lSubGroupId,
       "vRtrMplsS2lSubLspId": vRtrMplsS2lSubLspId,
       "vRtrMplsS2lSubLspRetryTimeRemain": vRtrMplsS2lSubLspRetryTimeRemain,
       "vRtrMplsS2lSubLspTunARHopLtIndex": vRtrMplsS2lSubLspTunARHopLtIndex,
       "vRtrMplsS2lSubLspNegotiatedMTU": vRtrMplsS2lSubLspNegotiatedMTU,
       "vRtrMplsS2lSubLspFailCode": vRtrMplsS2lSubLspFailCode,
       "vRtrMplsS2lSubLspFailNodeArType": vRtrMplsS2lSubLspFailNodeArType,
       "vRtrMplsS2lSubLspFailNodeAddr": vRtrMplsS2lSubLspFailNodeAddr,
       "vRtrMplsS2lSubLspOperBandwidth": vRtrMplsS2lSubLspOperBandwidth,
       "vRtrMplsS2lSubLspTunCRHopLtIndex": vRtrMplsS2lSubLspTunCRHopLtIndex,
       "vRtrMplsS2lSubLspOperMTU": vRtrMplsS2lSubLspOperMTU,
       "vRtrMplsS2lSubLspLastResigAttpt": vRtrMplsS2lSubLspLastResigAttpt,
       "vRtrMplsS2lSubLspLastMBBType": vRtrMplsS2lSubLspLastMBBType,
       "vRtrMplsS2lSubLspLastMBBEnd": vRtrMplsS2lSubLspLastMBBEnd,
       "vRtrMplsS2lSubLspLastMBBMetric": vRtrMplsS2lSubLspLastMBBMetric,
       "vRtrMplsS2lSubLspLastMBBState": vRtrMplsS2lSubLspLastMBBState,
       "vRtrMplsS2lSubLspMBBTypeInProg": vRtrMplsS2lSubLspMBBTypeInProg,
       "vRtrMplsS2lSubLspMBBStarted": vRtrMplsS2lSubLspMBBStarted,
       "vRtrMplsS2lSubLspMBBNextRetry": vRtrMplsS2lSubLspMBBNextRetry,
       "vRtrMplsS2lSubLspMBBRetryAttpts": vRtrMplsS2lSubLspMBBRetryAttpts,
       "vRtrMplsS2lSubLspMBBFailCode": vRtrMplsS2lSubLspMBBFailCode,
       "vRtrMplsS2lSubLspMBBFailNodeType": vRtrMplsS2lSubLspMBBFailNodeType,
       "vRtrMplsS2lSubLspMBBFailNodeAddr": vRtrMplsS2lSubLspMBBFailNodeAddr,
       "vRtrMplsS2lSubLspUpTime": vRtrMplsS2lSubLspUpTime,
       "vRtrMplsS2lSubLspDownTime": vRtrMplsS2lSubLspDownTime,
       "vRtrMplsS2lSubLspIsFastRetry": vRtrMplsS2lSubLspIsFastRetry,
       "vRtrMplsS2lSubLspTimeoutIn": vRtrMplsS2lSubLspTimeoutIn,
       "vRtrMplsS2lSubLspMBBTimeoutIn": vRtrMplsS2lSubLspMBBTimeoutIn,
       "vRtrMplsS2lSubLspInterArea": vRtrMplsS2lSubLspInterArea,
       "vRtrMplsS2lSubLspStatTable": vRtrMplsS2lSubLspStatTable,
       "vRtrMplsS2lSubLspStatEntry": vRtrMplsS2lSubLspStatEntry,
       "vRtrMplsS2lSubLspTimeUp": vRtrMplsS2lSubLspTimeUp,
       "vRtrMplsS2lSubLspTimeDown": vRtrMplsS2lSubLspTimeDown,
       "vRtrMplsS2lSubLspRetryAttempts": vRtrMplsS2lSubLspRetryAttempts,
       "vRtrMplsS2lSubLspTransitionCount": vRtrMplsS2lSubLspTransitionCount,
       "vRtrMplsS2lSubLspCspfQueries": vRtrMplsS2lSubLspCspfQueries,
       "vRtrMplsSrlgDBRtrIdTblLastChg": vRtrMplsSrlgDBRtrIdTblLastChg,
       "vRtrMplsSrlgDBRtrIdTable": vRtrMplsSrlgDBRtrIdTable,
       "vRtrMplsSrlgDBRtrIdEntry": vRtrMplsSrlgDBRtrIdEntry,
       "vRtrMplsSrlgDBRtrIdRouterID": vRtrMplsSrlgDBRtrIdRouterID,
       "vRtrMplsSrlgDBRtrIdRowStatus": vRtrMplsSrlgDBRtrIdRowStatus,
       "vRtrMplsSrlgDBRtrIdAdminState": vRtrMplsSrlgDBRtrIdAdminState,
       "vRtrMplsSrlgDBRtrIdLastChanged": vRtrMplsSrlgDBRtrIdLastChanged,
       "vRtrMplsSrlgDBIfTblLastChanged": vRtrMplsSrlgDBIfTblLastChanged,
       "vRtrMplsSrlgDBIfTable": vRtrMplsSrlgDBIfTable,
       "vRtrMplsSrlgDBIfEntry": vRtrMplsSrlgDBIfEntry,
       "vRtrMplsSrlgDBIfIntIpAddrType": vRtrMplsSrlgDBIfIntIpAddrType,
       "vRtrMplsSrlgDBIfIntIpAddr": vRtrMplsSrlgDBIfIntIpAddr,
       "vRtrMplsSrlgDBIfSrlgGroupName": vRtrMplsSrlgDBIfSrlgGroupName,
       "vRtrMplsSrlgDBIfRowStatus": vRtrMplsSrlgDBIfRowStatus,
       "vRtrMplsSrlgDBIfLastChanged": vRtrMplsSrlgDBIfLastChanged,
       "vRtrMplsInSegmentTable": vRtrMplsInSegmentTable,
       "vRtrMplsInSegmentEntry": vRtrMplsInSegmentEntry,
       "vRtrMplsInSegmentNumS2ls": vRtrMplsInSegmentNumS2ls,
       "vRtrMplsOutSegmentTable": vRtrMplsOutSegmentTable,
       "vRtrMplsOutSegmentEntry": vRtrMplsOutSegmentEntry,
       "vRtrMplsOutSegmentNumS2ls": vRtrMplsOutSegmentNumS2ls,
       "vRtrMplsLspStatsTblLastChgd": vRtrMplsLspStatsTblLastChgd,
       "vRtrMplsLspStatsTable": vRtrMplsLspStatsTable,
       "vRtrMplsLspStatsEntry": vRtrMplsLspStatsEntry,
       "vRtrMplsLspStatsType": vRtrMplsLspStatsType,
       "vRtrMplsLspStatsSenderAddrType": vRtrMplsLspStatsSenderAddrType,
       "vRtrMplsLspStatsSenderAddr": vRtrMplsLspStatsSenderAddr,
       "vRtrMplsLspStatsLspName": vRtrMplsLspStatsLspName,
       "vRtrMplsLspStatsRowStatus": vRtrMplsLspStatsRowStatus,
       "vRtrMplsLspStatsLastChanged": vRtrMplsLspStatsLastChanged,
       "vRtrMplsLspStatsCollectStats": vRtrMplsLspStatsCollectStats,
       "vRtrMplsLspStatsAccntingPolicy": vRtrMplsLspStatsAccntingPolicy,
       "vRtrMplsLspStatsAdminState": vRtrMplsLspStatsAdminState,
       "vRtrMplsLspStatisticsTable": vRtrMplsLspStatisticsTable,
       "vRtrMplsLspStatisticsEntry": vRtrMplsLspStatisticsEntry,
       "vRtrMplsInProfilePktsFc0": vRtrMplsInProfilePktsFc0,
       "vRtrMplsInProfilePktsFc0Low32": vRtrMplsInProfilePktsFc0Low32,
       "vRtrMplsInProfilePktsFc0High32": vRtrMplsInProfilePktsFc0High32,
       "vRtrMplsInProfilePktsFc1": vRtrMplsInProfilePktsFc1,
       "vRtrMplsInProfilePktsFc1Low32": vRtrMplsInProfilePktsFc1Low32,
       "vRtrMplsInProfilePktsFc1High32": vRtrMplsInProfilePktsFc1High32,
       "vRtrMplsInProfilePktsFc2": vRtrMplsInProfilePktsFc2,
       "vRtrMplsInProfilePktsFc2Low32": vRtrMplsInProfilePktsFc2Low32,
       "vRtrMplsInProfilePktsFc2High32": vRtrMplsInProfilePktsFc2High32,
       "vRtrMplsInProfilePktsFc3": vRtrMplsInProfilePktsFc3,
       "vRtrMplsInProfilePktsFc3Low32": vRtrMplsInProfilePktsFc3Low32,
       "vRtrMplsInProfilePktsFc3High32": vRtrMplsInProfilePktsFc3High32,
       "vRtrMplsInProfilePktsFc4": vRtrMplsInProfilePktsFc4,
       "vRtrMplsInProfilePktsFc4Low32": vRtrMplsInProfilePktsFc4Low32,
       "vRtrMplsInProfilePktsFc4High32": vRtrMplsInProfilePktsFc4High32,
       "vRtrMplsInProfilePktsFc5": vRtrMplsInProfilePktsFc5,
       "vRtrMplsInProfilePktsFc5Low32": vRtrMplsInProfilePktsFc5Low32,
       "vRtrMplsInProfilePktsFc5High32": vRtrMplsInProfilePktsFc5High32,
       "vRtrMplsInProfilePktsFc6": vRtrMplsInProfilePktsFc6,
       "vRtrMplsInProfilePktsFc6Low32": vRtrMplsInProfilePktsFc6Low32,
       "vRtrMplsInProfilePktsFc6High32": vRtrMplsInProfilePktsFc6High32,
       "vRtrMplsInProfilePktsFc7": vRtrMplsInProfilePktsFc7,
       "vRtrMplsInProfilePktsFc7Low32": vRtrMplsInProfilePktsFc7Low32,
       "vRtrMplsInProfilePktsFc7High32": vRtrMplsInProfilePktsFc7High32,
       "vRtrMplsInProfileOctetsFc0": vRtrMplsInProfileOctetsFc0,
       "vRtrMplsInProfileOctetsFc0Low32": vRtrMplsInProfileOctetsFc0Low32,
       "vRtrMplsInProfileOctetsFc0High32": vRtrMplsInProfileOctetsFc0High32,
       "vRtrMplsInProfileOctetsFc1": vRtrMplsInProfileOctetsFc1,
       "vRtrMplsInProfileOctetsFc1Low32": vRtrMplsInProfileOctetsFc1Low32,
       "vRtrMplsInProfileOctetsFc1High32": vRtrMplsInProfileOctetsFc1High32,
       "vRtrMplsInProfileOctetsFc2": vRtrMplsInProfileOctetsFc2,
       "vRtrMplsInProfileOctetsFc2Low32": vRtrMplsInProfileOctetsFc2Low32,
       "vRtrMplsInProfileOctetsFc2High32": vRtrMplsInProfileOctetsFc2High32,
       "vRtrMplsInProfileOctetsFc3": vRtrMplsInProfileOctetsFc3,
       "vRtrMplsInProfileOctetsFc3Low32": vRtrMplsInProfileOctetsFc3Low32,
       "vRtrMplsInProfileOctetsFc3High32": vRtrMplsInProfileOctetsFc3High32,
       "vRtrMplsInProfileOctetsFc4": vRtrMplsInProfileOctetsFc4,
       "vRtrMplsInProfileOctetsFc4Low32": vRtrMplsInProfileOctetsFc4Low32,
       "vRtrMplsInProfileOctetsFc4High32": vRtrMplsInProfileOctetsFc4High32,
       "vRtrMplsInProfileOctetsFc5": vRtrMplsInProfileOctetsFc5,
       "vRtrMplsInProfileOctetsFc5Low32": vRtrMplsInProfileOctetsFc5Low32,
       "vRtrMplsInProfileOctetsFc5High32": vRtrMplsInProfileOctetsFc5High32,
       "vRtrMplsInProfileOctetsFc6": vRtrMplsInProfileOctetsFc6,
       "vRtrMplsInProfileOctetsFc6Low32": vRtrMplsInProfileOctetsFc6Low32,
       "vRtrMplsInProfileOctetsFc6High32": vRtrMplsInProfileOctetsFc6High32,
       "vRtrMplsInProfileOctetsFc7": vRtrMplsInProfileOctetsFc7,
       "vRtrMplsInProfileOctetsFc7Low32": vRtrMplsInProfileOctetsFc7Low32,
       "vRtrMplsInProfileOctetsFc7High32": vRtrMplsInProfileOctetsFc7High32,
       "vRtrMplsOutOfProfPktsFc0": vRtrMplsOutOfProfPktsFc0,
       "vRtrMplsOutOfProfPktsFc0Low32": vRtrMplsOutOfProfPktsFc0Low32,
       "vRtrMplsOutOfProfPktsFc0High32": vRtrMplsOutOfProfPktsFc0High32,
       "vRtrMplsOutOfProfPktsFc1": vRtrMplsOutOfProfPktsFc1,
       "vRtrMplsOutOfProfPktsFc1Low32": vRtrMplsOutOfProfPktsFc1Low32,
       "vRtrMplsOutOfProfPktsFc1High32": vRtrMplsOutOfProfPktsFc1High32,
       "vRtrMplsOutOfProfPktsFc2": vRtrMplsOutOfProfPktsFc2,
       "vRtrMplsOutOfProfPktsFc2Low32": vRtrMplsOutOfProfPktsFc2Low32,
       "vRtrMplsOutOfProfPktsFc2High32": vRtrMplsOutOfProfPktsFc2High32,
       "vRtrMplsOutOfProfPktsFc3": vRtrMplsOutOfProfPktsFc3,
       "vRtrMplsOutOfProfPktsFc3Low32": vRtrMplsOutOfProfPktsFc3Low32,
       "vRtrMplsOutOfProfPktsFc3High32": vRtrMplsOutOfProfPktsFc3High32,
       "vRtrMplsOutOfProfPktsFc4": vRtrMplsOutOfProfPktsFc4,
       "vRtrMplsOutOfProfPktsFc4Low32": vRtrMplsOutOfProfPktsFc4Low32,
       "vRtrMplsOutOfProfPktsFc4High32": vRtrMplsOutOfProfPktsFc4High32,
       "vRtrMplsOutOfProfPktsFc5": vRtrMplsOutOfProfPktsFc5,
       "vRtrMplsOutOfProfPktsFc5Low32": vRtrMplsOutOfProfPktsFc5Low32,
       "vRtrMplsOutOfProfPktsFc5High32": vRtrMplsOutOfProfPktsFc5High32,
       "vRtrMplsOutOfProfPktsFc6": vRtrMplsOutOfProfPktsFc6,
       "vRtrMplsOutOfProfPktsFc6Low32": vRtrMplsOutOfProfPktsFc6Low32,
       "vRtrMplsOutOfProfPktsFc6High32": vRtrMplsOutOfProfPktsFc6High32,
       "vRtrMplsOutOfProfPktsFc7": vRtrMplsOutOfProfPktsFc7,
       "vRtrMplsOutOfProfPktsFc7Low32": vRtrMplsOutOfProfPktsFc7Low32,
       "vRtrMplsOutOfProfPktsFc7High32": vRtrMplsOutOfProfPktsFc7High32,
       "vRtrMplsOutOfProfOctetsFc0": vRtrMplsOutOfProfOctetsFc0,
       "vRtrMplsOutOfProfOctetsFc0Low32": vRtrMplsOutOfProfOctetsFc0Low32,
       "vRtrMplsOutOfProfOctetsFc0High32": vRtrMplsOutOfProfOctetsFc0High32,
       "vRtrMplsOutOfProfOctetsFc1": vRtrMplsOutOfProfOctetsFc1,
       "vRtrMplsOutOfProfOctetsFc1Low32": vRtrMplsOutOfProfOctetsFc1Low32,
       "vRtrMplsOutOfProfOctetsFc1High32": vRtrMplsOutOfProfOctetsFc1High32,
       "vRtrMplsOutOfProfOctetsFc2": vRtrMplsOutOfProfOctetsFc2,
       "vRtrMplsOutOfProfOctetsFc2Low32": vRtrMplsOutOfProfOctetsFc2Low32,
       "vRtrMplsOutOfProfOctetsFc2High32": vRtrMplsOutOfProfOctetsFc2High32,
       "vRtrMplsOutOfProfOctetsFc3": vRtrMplsOutOfProfOctetsFc3,
       "vRtrMplsOutOfProfOctetsFc3Low32": vRtrMplsOutOfProfOctetsFc3Low32,
       "vRtrMplsOutOfProfOctetsFc3High32": vRtrMplsOutOfProfOctetsFc3High32,
       "vRtrMplsOutOfProfOctetsFc4": vRtrMplsOutOfProfOctetsFc4,
       "vRtrMplsOutOfProfOctetsFc4Low32": vRtrMplsOutOfProfOctetsFc4Low32,
       "vRtrMplsOutOfProfOctetsFc4High32": vRtrMplsOutOfProfOctetsFc4High32,
       "vRtrMplsOutOfProfOctetsFc5": vRtrMplsOutOfProfOctetsFc5,
       "vRtrMplsOutOfProfOctetsFc5Low32": vRtrMplsOutOfProfOctetsFc5Low32,
       "vRtrMplsOutOfProfOctetsFc5High32": vRtrMplsOutOfProfOctetsFc5High32,
       "vRtrMplsOutOfProfOctetsFc6": vRtrMplsOutOfProfOctetsFc6,
       "vRtrMplsOutOfProfOctetsFc6Low32": vRtrMplsOutOfProfOctetsFc6Low32,
       "vRtrMplsOutOfProfOctetsFc6High32": vRtrMplsOutOfProfOctetsFc6High32,
       "vRtrMplsOutOfProfOctetsFc7": vRtrMplsOutOfProfOctetsFc7,
       "vRtrMplsOutOfProfOctetsFc7Low32": vRtrMplsOutOfProfOctetsFc7Low32,
       "vRtrMplsOutOfProfOctetsFc7High32": vRtrMplsOutOfProfOctetsFc7High32,
       "vRtrMplsLspStatsPSBMatch": vRtrMplsLspStatsPSBMatch,
       "vRtrMplsLspStatsTpOnly": vRtrMplsLspStatsTpOnly,
       "vRtrMplsLspStatsLspType": vRtrMplsLspStatsLspType,
       "vRtrMplsLspTemplateTblLastChgd": vRtrMplsLspTemplateTblLastChgd,
       "vRtrMplsLspTemplateTable": vRtrMplsLspTemplateTable,
       "vRtrMplsLspTemplateEntry": vRtrMplsLspTemplateEntry,
       "vRtrMplsLspTemplateName": vRtrMplsLspTemplateName,
       "vRtrMplsLspTemplateRowStatus": vRtrMplsLspTemplateRowStatus,
       "vRtrMplsLspTemplateLastChanged": vRtrMplsLspTemplateLastChanged,
       "vRtrMplsLspTemplateAdminState": vRtrMplsLspTemplateAdminState,
       "vRtrMplsLspTemplateType": vRtrMplsLspTemplateType,
       "vRtrMplsLspTemplateAdaptive": vRtrMplsLspTemplateAdaptive,
       "vRtrMplsLspTemplateBandwidth": vRtrMplsLspTemplateBandwidth,
       "vRtrMplsLspTemplateCspf": vRtrMplsLspTemplateCspf,
       "vRtrMplsLspTemplateDefaultPath": vRtrMplsLspTemplateDefaultPath,
       "vRtrMplsLspTemplateAdmGrpIncl": vRtrMplsLspTemplateAdmGrpIncl,
       "vRtrMplsLspTemplateAdmGrpExcl": vRtrMplsLspTemplateAdmGrpExcl,
       "vRtrMplsLspTemplateFastReroute": vRtrMplsLspTemplateFastReroute,
       "vRtrMplsLspTemplateFRMethod": vRtrMplsLspTemplateFRMethod,
       "vRtrMplsLspTemplateFRHopLimit": vRtrMplsLspTemplateFRHopLimit,
       "vRtrMplsLspTemplateHopLimit": vRtrMplsLspTemplateHopLimit,
       "vRtrMplsLspTemplateRecord": vRtrMplsLspTemplateRecord,
       "vRtrMplsLspTemplateRecordLabel": vRtrMplsLspTemplateRecordLabel,
       "vRtrMplsLspTemplateRetryLimit": vRtrMplsLspTemplateRetryLimit,
       "vRtrMplsLspTemplateRetryTimer": vRtrMplsLspTemplateRetryTimer,
       "vRtrMplsLspTemplateCspfTeMetric": vRtrMplsLspTemplateCspfTeMetric,
       "vRtrMplsLspTemplateLspCount": vRtrMplsLspTemplateLspCount,
       "vRtrMplsLspTemplateMvpnRefCount": vRtrMplsLspTemplateMvpnRefCount,
       "vRtrMplsLspTemplateFRPropAdmGrp": vRtrMplsLspTemplateFRPropAdmGrp,
       "vRtrMplsLspTemplatePropAdmGrp": vRtrMplsLspTemplatePropAdmGrp,
       "vRtrMplsLspTemplateBgpShortcut": vRtrMplsLspTemplateBgpShortcut,
       "vRtrMplsLspTemplateIgpShortcut": vRtrMplsLspTemplateIgpShortcut,
       "vRtrMplsLspTemplateLdpOverRsvp": vRtrMplsLspTemplateLdpOverRsvp,
       "vRtrMplsLspTemplateLeastFill": vRtrMplsLspTemplateLeastFill,
       "vRtrMplsLspTemplateMetric": vRtrMplsLspTemplateMetric,
       "vRtrMplsLspTemplateSetupPriority": vRtrMplsLspTemplateSetupPriority,
       "vRtrMplsLspTemplateHoldPriority": vRtrMplsLspTemplateHoldPriority,
       "vRtrMplsLspTemplateVprnAutoBind": vRtrMplsLspTemplateVprnAutoBind,
       "vRtrMplsLspTempIgpSCutLfaType": vRtrMplsLspTempIgpSCutLfaType,
       "vRtrMplsLspTempIgpSCutRelOffset": vRtrMplsLspTempIgpSCutRelOffset,
       "vRtrMplsLspTempAutoBandwidth": vRtrMplsLspTempAutoBandwidth,
       "vRtrMplsLspTempFRNodeProtect": vRtrMplsLspTempFRNodeProtect,
       "vRtrMplsLspTemplateEgrStats": vRtrMplsLspTemplateEgrStats,
       "vRtrMplsLspTempCollectStats": vRtrMplsLspTempCollectStats,
       "vRtrMplsLspTempAccntingPolicy": vRtrMplsLspTempAccntingPolicy,
       "vRtrMplsLspTemplateFromAddrType": vRtrMplsLspTemplateFromAddrType,
       "vRtrMplsLspTemplateFromAddr": vRtrMplsLspTemplateFromAddr,
       "vRtrMplsLspTemplateClassType": vRtrMplsLspTemplateClassType,
       "vRtrMplsLspTempBkupClassType": vRtrMplsLspTempBkupClassType,
       "vRtrMplsLspTempBgpTransportTunn": vRtrMplsLspTempBgpTransportTunn,
       "vRtrMplsLspTempMainCTRetryLimit": vRtrMplsLspTempMainCTRetryLimit,
       "vRtrMplsLspTemplateRsvpAdspec": vRtrMplsLspTemplateRsvpAdspec,
       "vRtrMplsLspTempLoadBalancingWt": vRtrMplsLspTempLoadBalancingWt,
       "vRtrMplsLspTempClassFwdEnabled": vRtrMplsLspTempClassFwdEnabled,
       "vRtrMplsLspTempFC": vRtrMplsLspTempFC,
       "vRtrMplsLspTempBfdTemplateName": vRtrMplsLspTempBfdTemplateName,
       "vRtrMplsLspTempBfdEnable": vRtrMplsLspTempBfdEnable,
       "vRtrMplsLspTempBfdPingIntvl": vRtrMplsLspTempBfdPingIntvl,
       "vRtrMplsLspTempEntropyLabel": vRtrMplsLspTempEntropyLabel,
       "vRtrMplsLspTemplatePceReport": vRtrMplsLspTemplatePceReport,
       "vRtrMplsLspTempBfdFailureAction": vRtrMplsLspTempBfdFailureAction,
       "vRtrMplsLspAutoBWTableLastChg": vRtrMplsLspAutoBWTableLastChg,
       "vRtrMplsLspAutoBandwidthTable": vRtrMplsLspAutoBandwidthTable,
       "vRtrMplsLspAutoBandwidthEntry": vRtrMplsLspAutoBandwidthEntry,
       "vRtrMplsLspAutoBWLspName": vRtrMplsLspAutoBWLspName,
       "vRtrMplsLspAutoBWLastChange": vRtrMplsLspAutoBWLastChange,
       "vRtrMplsLspAutoBWAdjDNPercent": vRtrMplsLspAutoBWAdjDNPercent,
       "vRtrMplsLspAutoBWAdjDNMbps": vRtrMplsLspAutoBWAdjDNMbps,
       "vRtrMplsLspAutoBWAdjMultiplier": vRtrMplsLspAutoBWAdjMultiplier,
       "vRtrMplsLspAutoBWAdjUPPercent": vRtrMplsLspAutoBWAdjUPPercent,
       "vRtrMplsLspAutoBWAdjUPMbps": vRtrMplsLspAutoBWAdjUPMbps,
       "vRtrMplsLspAutoBWMaxBW": vRtrMplsLspAutoBWMaxBW,
       "vRtrMplsLspAutoBWMinBW": vRtrMplsLspAutoBWMinBW,
       "vRtrMplsLspAutoBWMonitorBW": vRtrMplsLspAutoBWMonitorBW,
       "vRtrMplsLspAutoBWOverFlow": vRtrMplsLspAutoBWOverFlow,
       "vRtrMplsLspAutoBWOvrFlwThreshold": vRtrMplsLspAutoBWOvrFlwThreshold,
       "vRtrMplsLspAutoBWOvrFlwBW": vRtrMplsLspAutoBWOvrFlwBW,
       "vRtrMplsLspAutoBWSampMultiplier": vRtrMplsLspAutoBWSampMultiplier,
       "vRtrMplsLspAutoBWSampTime": vRtrMplsLspAutoBWSampTime,
       "vRtrMplsLspAutoBWLastAdj": vRtrMplsLspAutoBWLastAdj,
       "vRtrMplsLspAutoBWLastAdjCause": vRtrMplsLspAutoBWLastAdjCause,
       "vRtrMplsLspAutoBWNextAdj": vRtrMplsLspAutoBWNextAdj,
       "vRtrMplsLspAutoBWMaxAvgRate": vRtrMplsLspAutoBWMaxAvgRate,
       "vRtrMplsLspAutoBWLastAvgRate": vRtrMplsLspAutoBWLastAvgRate,
       "vRtrMplsLspAutoBWInheritance": vRtrMplsLspAutoBWInheritance,
       "vRtrMplsLspAutoBWCurrentBW": vRtrMplsLspAutoBWCurrentBW,
       "vRtrMplsLspAutoBWAdjTime": vRtrMplsLspAutoBWAdjTime,
       "vRtrMplsLspAutoBWOvrFlwCount": vRtrMplsLspAutoBWOvrFlwCount,
       "vRtrMplsLspAutoBWSampCount": vRtrMplsLspAutoBWSampCount,
       "vRtrMplsLspAutoBWAdjCount": vRtrMplsLspAutoBWAdjCount,
       "vRtrMplsLspAutoBWOperState": vRtrMplsLspAutoBWOperState,
       "vRtrMplsLspAutoBWSampInterval": vRtrMplsLspAutoBWSampInterval,
       "vRtrMplsLspAutoBWBeWeight": vRtrMplsLspAutoBWBeWeight,
       "vRtrMplsLspAutoBWL2Weight": vRtrMplsLspAutoBWL2Weight,
       "vRtrMplsLspAutoBWAfWeight": vRtrMplsLspAutoBWAfWeight,
       "vRtrMplsLspAutoBWL1Weight": vRtrMplsLspAutoBWL1Weight,
       "vRtrMplsLspAutoBWH2Weight": vRtrMplsLspAutoBWH2Weight,
       "vRtrMplsLspAutoBWEfWeight": vRtrMplsLspAutoBWEfWeight,
       "vRtrMplsLspAutoBWH1Weight": vRtrMplsLspAutoBWH1Weight,
       "vRtrMplsLspAutoBWNcWeight": vRtrMplsLspAutoBWNcWeight,
       "vRtrMplsLspAutoBWUnderFlow": vRtrMplsLspAutoBWUnderFlow,
       "vRtrMplsLspAutoBWUndFlwThreshold": vRtrMplsLspAutoBWUndFlwThreshold,
       "vRtrMplsLspAutoBWUndFlwBW": vRtrMplsLspAutoBWUndFlwBW,
       "vRtrMplsLspAutoBWUndFlwCount": vRtrMplsLspAutoBWUndFlwCount,
       "vRtrMplsLspAutoBWMaxUndFlwBw": vRtrMplsLspAutoBWMaxUndFlwBw,
       "vRtrMplsLspPathOperTable": vRtrMplsLspPathOperTable,
       "vRtrMplsLspPathOperEntry": vRtrMplsLspPathOperEntry,
       "vRtrMplsLspPathOperSetupPriority": vRtrMplsLspPathOperSetupPriority,
       "vRtrMplsLspPathOperHoldPriority": vRtrMplsLspPathOperHoldPriority,
       "vRtrMplsLspPathOperRecord": vRtrMplsLspPathOperRecord,
       "vRtrMplsLspPathOperRecordLabel": vRtrMplsLspPathOperRecordLabel,
       "vRtrMplsLspPathOperHopLimit": vRtrMplsLspPathOperHopLimit,
       "vRtrMplsLspPathOperAdminGrpIncl": vRtrMplsLspPathOperAdminGrpIncl,
       "vRtrMplsLspPathOperAdminGrExcld": vRtrMplsLspPathOperAdminGrExcld,
       "vRtrMplsLspPathOperCspf": vRtrMplsLspPathOperCspf,
       "vRtrMplsLspPathOperCspfToFrstLs": vRtrMplsLspPathOperCspfToFrstLs,
       "vRtrMplsLspPathOperLeastFill": vRtrMplsLspPathOperLeastFill,
       "vRtrMplsLspPathOperRsvpAdspec": vRtrMplsLspPathOperRsvpAdspec,
       "vRtrMplsLspPathOperFRNodeProtect": vRtrMplsLspPathOperFRNodeProtect,
       "vRtrMplsLspPathOperPropAdminGrp": vRtrMplsLspPathOperPropAdminGrp,
       "vRtrMplsLspPathOperFRHopLimit": vRtrMplsLspPathOperFRHopLimit,
       "vRtrMplsLspPathOperFRPropAdmGrp": vRtrMplsLspPathOperFRPropAdmGrp,
       "vRtrMplsLspPathOperInterArea": vRtrMplsLspPathOperInterArea,
       "vRtrMplsLabelObjs": vRtrMplsLabelObjs,
       "vRtrMplsLabelMaxStaticLspLabels": vRtrMplsLabelMaxStaticLspLabels,
       "vRtrMplsLabelMaxStaticSvcLabels": vRtrMplsLabelMaxStaticSvcLabels,
       "vRtrMplsLabelBgpLabelsHoldTimer": vRtrMplsLabelBgpLabelsHoldTimer,
       "vRtrMplsLabelSegRouteStartLabel": vRtrMplsLabelSegRouteStartLabel,
       "vRtrMplsLabelSegRouteEndLabel": vRtrMplsLabelSegRouteEndLabel,
       "vRtrMplsLabelStaticLabelRange": vRtrMplsLabelStaticLabelRange,
       "vRtrMplsLspTempAutoBWTblLastChg": vRtrMplsLspTempAutoBWTblLastChg,
       "vRtrMplsLspTempAutoBWTable": vRtrMplsLspTempAutoBWTable,
       "vRtrMplsLspTempAutoBWEntry": vRtrMplsLspTempAutoBWEntry,
       "vRtrMplsLspTempAutoBWLastChg": vRtrMplsLspTempAutoBWLastChg,
       "vRtrMplsLspTempAutoBWAdjDNPer": vRtrMplsLspTempAutoBWAdjDNPer,
       "vRtrMplsLspTempAutoBWAdjDNMbps": vRtrMplsLspTempAutoBWAdjDNMbps,
       "vRtrMplsLspTempAutoBWAdjUPPer": vRtrMplsLspTempAutoBWAdjUPPer,
       "vRtrMplsLspTempAutoBWAdjUPMbps": vRtrMplsLspTempAutoBWAdjUPMbps,
       "vRtrMplsLspTempAutoBWMaxBW": vRtrMplsLspTempAutoBWMaxBW,
       "vRtrMplsLspTempAutoBWMinBW": vRtrMplsLspTempAutoBWMinBW,
       "vRtrMplsLspTempAutoBWMntrBW": vRtrMplsLspTempAutoBWMntrBW,
       "vRtrMplsLspTempAutoBWAdjMult": vRtrMplsLspTempAutoBWAdjMult,
       "vRtrMplsLspTempAutoBWOverFlow": vRtrMplsLspTempAutoBWOverFlow,
       "vRtrMplsLspTempAutoBWOvrFlwThr": vRtrMplsLspTempAutoBWOvrFlwThr,
       "vRtrMplsLspTempAutoBWOvrFlwBW": vRtrMplsLspTempAutoBWOvrFlwBW,
       "vRtrMplsLspTempAutoBWSampMult": vRtrMplsLspTempAutoBWSampMult,
       "vRtrMplsLspTempAutoBWSampTime": vRtrMplsLspTempAutoBWSampTime,
       "vRtrMplsLspTempAutoBWInherit": vRtrMplsLspTempAutoBWInherit,
       "vRtrMplsLspTempAutoBWBeWeight": vRtrMplsLspTempAutoBWBeWeight,
       "vRtrMplsLspTempAutoBWL2Weight": vRtrMplsLspTempAutoBWL2Weight,
       "vRtrMplsLspTempAutoBWAfWeight": vRtrMplsLspTempAutoBWAfWeight,
       "vRtrMplsLspTempAutoBWL1Weight": vRtrMplsLspTempAutoBWL1Weight,
       "vRtrMplsLspTempAutoBWH2Weight": vRtrMplsLspTempAutoBWH2Weight,
       "vRtrMplsLspTempAutoBWEfWeight": vRtrMplsLspTempAutoBWEfWeight,
       "vRtrMplsLspTempAutoBWH1Weight": vRtrMplsLspTempAutoBWH1Weight,
       "vRtrMplsLspTempAutoBWNcWeight": vRtrMplsLspTempAutoBWNcWeight,
       "vRtrMplsLspTempAutoBWUnderFlow": vRtrMplsLspTempAutoBWUnderFlow,
       "vRtrMplsLspTempAutoBWUndFlwThr": vRtrMplsLspTempAutoBWUndFlwThr,
       "vRtrMplsLspTempAutoBWUndFlwBW": vRtrMplsLspTempAutoBWUndFlwBW,
       "vRtrMplsTemplPlcyBindTblLastChg": vRtrMplsTemplPlcyBindTblLastChg,
       "vRtrMplsLspTemplPlcyBindTable": vRtrMplsLspTemplPlcyBindTable,
       "vRtrMplsLspTemplPlcyBindEntry": vRtrMplsLspTemplPlcyBindEntry,
       "vRtrMplsLspTemplPlcyBindLastChg": vRtrMplsLspTemplPlcyBindLastChg,
       "vRtrMplsLspTemplPlcyBindRowStat": vRtrMplsLspTemplPlcyBindRowStat,
       "vRtrMplsLspTemplPlcyBind1": vRtrMplsLspTemplPlcyBind1,
       "vRtrMplsLspTemplPlcyBind2": vRtrMplsLspTemplPlcyBind2,
       "vRtrMplsLspTemplPlcyBind3": vRtrMplsLspTemplPlcyBind3,
       "vRtrMplsLspTemplPlcyBind4": vRtrMplsLspTemplPlcyBind4,
       "vRtrMplsLspTemplPlcyBind5": vRtrMplsLspTemplPlcyBind5,
       "vRtrMplsLspTemplPlcyBindOneHop": vRtrMplsLspTemplPlcyBindOneHop,
       "vRtrMplsLspTempInStatTblLstChg": vRtrMplsLspTempInStatTblLstChg,
       "vRtrMplsLspTempInStatTable": vRtrMplsLspTempInStatTable,
       "vRtrMplsLspTempInStatEntry": vRtrMplsLspTempInStatEntry,
       "vRtrMplsLspTempInStatType": vRtrMplsLspTempInStatType,
       "vRtrMplsLspTempInStatSndrAddrTyp": vRtrMplsLspTempInStatSndrAddrTyp,
       "vRtrMplsLspTempInStatSndrAddr": vRtrMplsLspTempInStatSndrAddr,
       "vRtrMplsLspTempInStatLspNamePref": vRtrMplsLspTempInStatLspNamePref,
       "vRtrMplsLspTempInStatRowStatus": vRtrMplsLspTempInStatRowStatus,
       "vRtrMplsLspTempInStatLastChanged": vRtrMplsLspTempInStatLastChanged,
       "vRtrMplsLspTempInStatCollectStat": vRtrMplsLspTempInStatCollectStat,
       "vRtrMplsLspTempInStatAccntPolicy": vRtrMplsLspTempInStatAccntPolicy,
       "vRtrMplsLspTempInStatAdminState": vRtrMplsLspTempInStatAdminState,
       "vRtrMplsLspTempInStatMaxStats": vRtrMplsLspTempInStatMaxStats,
       "vRtrMplsLspTempInStatTotlSession": vRtrMplsLspTempInStatTotlSession,
       "vRtrMplsLspExtTable": vRtrMplsLspExtTable,
       "vRtrMplsLspExtEntry": vRtrMplsLspExtEntry,
       "vRtrMplsLspExtPceCompute": vRtrMplsLspExtPceCompute,
       "vRtrMplsLspExtPceControl": vRtrMplsLspExtPceControl,
       "vRtrMplsLspExtPceReport": vRtrMplsLspExtPceReport,
       "vRtrMplsLspExtTtmTunnelId": vRtrMplsLspExtTtmTunnelId,
       "vRtrMplsLspExtMaxSrLabels": vRtrMplsLspExtMaxSrLabels,
       "vRtrMplsLspExtTunnelId": vRtrMplsLspExtTunnelId,
       "vRtrMplsLspExtEntropyLabel": vRtrMplsLspExtEntropyLabel,
       "vRtrMplsLspExtOperEntropyLabel": vRtrMplsLspExtOperEntropyLabel,
       "vRtrMplsLspExtFrrOverheadLabel": vRtrMplsLspExtFrrOverheadLabel,
       "vRtrMplsLspExtNegEntropyLbl": vRtrMplsLspExtNegEntropyLbl,
       "vRtrMplsLspExtBfdFailureAction": vRtrMplsLspExtBfdFailureAction,
       "vRtrMplsLspPathProfTblLstChg": vRtrMplsLspPathProfTblLstChg,
       "vRtrMplsLspPathProfTable": vRtrMplsLspPathProfTable,
       "vRtrMplsLspPathProfEntry": vRtrMplsLspPathProfEntry,
       "vRtrMplsLspPathProfId": vRtrMplsLspPathProfId,
       "vRtrMplsLspPathProfRowStatus": vRtrMplsLspPathProfRowStatus,
       "vRtrMplsLspPathProfLastChange": vRtrMplsLspPathProfLastChange,
       "vRtrMplsLspPathProfGroupId": vRtrMplsLspPathProfGroupId,
       "vRtrMplsClassFwdPlcyTblLstChg": vRtrMplsClassFwdPlcyTblLstChg,
       "vRtrMplsClassFwdPlcyTable": vRtrMplsClassFwdPlcyTable,
       "vRtrMplsClassFwdPlcyEntry": vRtrMplsClassFwdPlcyEntry,
       "vRtrMplsClassFwdPlcyName": vRtrMplsClassFwdPlcyName,
       "vRtrMplsClassFwdPlcyRowStatus": vRtrMplsClassFwdPlcyRowStatus,
       "vRtrMplsClassFwdPlcyLastChanged": vRtrMplsClassFwdPlcyLastChanged,
       "vRtrMplsClassFwdPlcyFcBEFwdSet": vRtrMplsClassFwdPlcyFcBEFwdSet,
       "vRtrMplsClassFwdPlcyFcL2FwdSet": vRtrMplsClassFwdPlcyFcL2FwdSet,
       "vRtrMplsClassFwdPlcyFcAFFwdSet": vRtrMplsClassFwdPlcyFcAFFwdSet,
       "vRtrMplsClassFwdPlcyFcL1FwdSet": vRtrMplsClassFwdPlcyFcL1FwdSet,
       "vRtrMplsClassFwdPlcyFcH2FwdSet": vRtrMplsClassFwdPlcyFcH2FwdSet,
       "vRtrMplsClassFwdPlcyFcEFFwdSet": vRtrMplsClassFwdPlcyFcEFFwdSet,
       "vRtrMplsClassFwdPlcyFcH1FwdSet": vRtrMplsClassFwdPlcyFcH1FwdSet,
       "vRtrMplsClassFwdPlcyFcNCFwdSet": vRtrMplsClassFwdPlcyFcNCFwdSet,
       "vRtrMplsClassFwdPlcyDefFwdSet": vRtrMplsClassFwdPlcyDefFwdSet,
       "vRtrMplsClassFwdPlcyRefCount": vRtrMplsClassFwdPlcyRefCount,
       "tmnxMplsNotifyPrefix": tmnxMplsNotifyPrefix,
       "tmnxMplsNotifications": tmnxMplsNotifications,
       "vRtrMplsStateChange": vRtrMplsStateChange,
       "vRtrMplsIfStateChange": vRtrMplsIfStateChange,
       "vRtrMplsLspUp": vRtrMplsLspUp,
       "vRtrMplsLspDown": vRtrMplsLspDown,
       "vRtrMplsLspPathUp": vRtrMplsLspPathUp,
       "vRtrMplsLspPathDown": vRtrMplsLspPathDown,
       "vRtrMplsLspPathRerouted": vRtrMplsLspPathRerouted,
       "vRtrMplsLspPathResignaled": vRtrMplsLspPathResignaled,
       "vRtrMplsP2mpInstanceUp": vRtrMplsP2mpInstanceUp,
       "vRtrMplsP2mpInstanceDown": vRtrMplsP2mpInstanceDown,
       "vRtrMplsS2lSubLspUp": vRtrMplsS2lSubLspUp,
       "vRtrMplsS2lSubLspDown": vRtrMplsS2lSubLspDown,
       "vRtrMplsS2lSubLspRerouted": vRtrMplsS2lSubLspRerouted,
       "vRtrMplsS2lSubLspResignaled": vRtrMplsS2lSubLspResignaled,
       "vRtrMplsLspPathSoftPreempted": vRtrMplsLspPathSoftPreempted,
       "vRtrMplsLspPathLstFillReoptElig": vRtrMplsLspPathLstFillReoptElig,
       "vRtrMplsP2mpInstanceResignaled": vRtrMplsP2mpInstanceResignaled,
       "vRtrMplsResignalTimerExpired": vRtrMplsResignalTimerExpired,
       "vRtrMplsLspPathMbbStatusEvent": vRtrMplsLspPathMbbStatusEvent,
       "vRtrMplsLspSwitchStbyFailure": vRtrMplsLspSwitchStbyFailure,
       "vRtrMplsLspActivePathChanged": vRtrMplsLspActivePathChanged,
       "vRtrMplsXCBundleChange": vRtrMplsXCBundleChange,
       "vRtrMplsLblRangeModify": vRtrMplsLblRangeModify,
       "vRtrMplsNodeInIgpOverload": vRtrMplsNodeInIgpOverload}
)
