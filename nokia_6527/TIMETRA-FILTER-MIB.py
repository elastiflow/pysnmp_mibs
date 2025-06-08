# SNMP MIB module (TIMETRA-FILTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_6527/TIMETRA-FILTER-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 17:44:31 2025
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

(InetAddress,
 InetAddressIPv6,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressIPv6",
    "InetAddressPrefixLength",
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
 Opaque,
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
    "Opaque",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 MacAddress,
 PhysAddress,
 RowPointer,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowPointer",
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

(Dot1PPriority,
 IPv6FlowLabel,
 IPv6FlowLabelMask,
 IpAddressPrefixLength,
 QTagFullRange,
 QTagFullRangeOrNone,
 SdpBindId,
 ServiceAccessPoint,
 SvcISID,
 TDSCPFilterActionValue,
 TDSCPNameOrEmpty,
 TFrameType,
 TIpOption,
 TIpProtocol,
 TItemDescription,
 TLNamedItemOrEmpty,
 TMacFilterType,
 TNamedItem,
 TNamedItemOrEmpty,
 TOperator,
 TRegularExpression,
 TTcpUdpPort,
 TTcpUdpPortOperator,
 TmnxAdminState,
 TmnxEncapVal,
 TmnxHttpRedirectUrl,
 TmnxNatSubscriberType,
 TmnxOperState,
 TmnxPortID,
 TmnxServId,
 TmnxVRtrIDOrZero,
 TmnxVRtrMplsLspID) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "Dot1PPriority",
    "IPv6FlowLabel",
    "IPv6FlowLabelMask",
    "IpAddressPrefixLength",
    "QTagFullRange",
    "QTagFullRangeOrNone",
    "SdpBindId",
    "ServiceAccessPoint",
    "SvcISID",
    "TDSCPFilterActionValue",
    "TDSCPNameOrEmpty",
    "TFrameType",
    "TIpOption",
    "TIpProtocol",
    "TItemDescription",
    "TLNamedItemOrEmpty",
    "TMacFilterType",
    "TNamedItem",
    "TNamedItemOrEmpty",
    "TOperator",
    "TRegularExpression",
    "TTcpUdpPort",
    "TTcpUdpPortOperator",
    "TmnxAdminState",
    "TmnxEncapVal",
    "TmnxHttpRedirectUrl",
    "TmnxNatSubscriberType",
    "TmnxOperState",
    "TmnxPortID",
    "TmnxServId",
    "TmnxVRtrIDOrZero",
    "TmnxVRtrMplsLspID")


# MODULE-IDENTITY

timetraFilterMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 21)
)
if mibBuilder.loadTexts:
    timetraFilterMIBModule.setRevisions(
        ("2014-01-01 00:00",
         "2012-08-01 00:00",
         "2011-02-01 00:00",
         "2009-07-01 00:00",
         "2008-07-01 00:00",
         "2008-01-01 00:00",
         "2007-01-01 00:00",
         "2006-02-28 00:00",
         "2005-08-31 00:00",
         "2005-01-24 00:00",
         "2004-01-15 00:00",
         "2003-08-15 00:00",
         "2003-01-29 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TFilterID(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class TIPFilterID(TFilterID):
    status = "current"


class TIPFilterIdOrEmpty(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 65535),
    )



class TMACFilterID(TFilterID):
    status = "current"


class TAnyFilterID(TextualConvention, Unsigned32):
    status = "current"


class TFilterScope(TextualConvention, Integer32):
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
        *(("exclusive", 1),
          ("template", 2),
          ("embedded", 3))
    )



class TItemMatch(TextualConvention, Integer32):
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
        *(("off", 1),
          ("false", 2),
          ("true", 3))
    )



class TEntryIndicator(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class TEntryId(TEntryIndicator):
    status = "current"
    subtypeSpec = TEntryIndicator.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )



class TAnyEntryId(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 131070),
    )



class TEntryIdOrZero(TEntryIndicator):
    status = "current"
    subtypeSpec = TEntryIndicator.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class TFilterAction(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("forward", 2),
          ("httpRedirect", 4),
          ("nat", 5),
          ("reassemble", 6),
          ("gtpLclBrkout", 7))
    )



class TFilterActionOrDefault(TextualConvention, Integer32):
    status = "current"
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
        *(("drop", 1),
          ("forward", 2),
          ("default", 3),
          ("httpRedirect", 4),
          ("nat", 5),
          ("reassemble", 6),
          ("gtpLclBrkout", 7))
    )



class TFilterLogId(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(101, 199),
    )



class TFilterLogDestination(TextualConvention, Integer32):
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
        *(("memory", 1),
          ("syslog", 2),
          ("file", 3))
    )



class TTimeRangeState(TextualConvention, Integer32):
    status = "current"
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
        *(("timeRangeNotApplic", 0),
          ("timeRangeNotActive", 1),
          ("timeRangeActive", 2),
          ("timeRangeActiveDownloadFailed", 3))
    )



class TFilterLogSummaryCriterium(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("srcAddr", 0),
          ("dstAddr", 1))
    )



class TFilterType(TextualConvention, Integer32):
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
        *(("fltrtypeselNone", 0),
          ("fltrtypeselIp", 1),
          ("fltrtypeselMac", 2),
          ("fltrtypeselCpm", 3),
          ("fltrtypeselIpv6", 4),
          ("fltrtypeselCpm6", 5),
          ("fltrtypeselCpmMac", 6))
    )



class TFilterSubInsSpaceOwner(TextualConvention, Integer32):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("radius", 1),
          ("creditControl", 2),
          ("bgpFlowspec", 3),
          ("li", 4),
          ("embedded", 5),
          ("radiusSharedHost", 6),
          ("openflow", 7))
    )



class TDHCPFilterID(TFilterID):
    status = "current"


class TDhcpFilterAction(TextualConvention, Integer32):
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
        *(("none", 1),
          ("bypass-host-creation", 2),
          ("drop", 3))
    )



class TDhcpFilterMatch(TextualConvention, Integer32):
    status = "current"
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
        *(("present", 1),
          ("absent", 2),
          ("string", 3),
          ("string-exact", 4),
          ("string-invert", 5),
          ("string-exact-invert", 6),
          ("hex", 7),
          ("hex-exact", 8),
          ("hex-invert", 9),
          ("hex-exact-invert", 10))
    )



class TFltrPrefixListType(TextualConvention, Integer32):
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
          ("ipv6", 2))
    )



class TmnxEmbeddedFltrOperState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("embedFailedNoResources", -1),
          ("inactive", 0),
          ("active", 1))
    )



class TmnxFltrEmbeddedEntryState(TextualConvention, Integer32):
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
        *(("inserted", 1),
          ("overruled", 2),
          ("inactiveAdminDown", 3),
          ("inactiveNoResources", 4))
    )



class TmnxFilterApplyPathSource(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("bgp-peers", 1))
    )



class TFltrPortSelector(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("and-port", 0),
          ("or-port", 1))
    )



class TFilterPacketLength(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



# MIB Managed Objects in the order of their OIDs

_TFilterMIBConformance_ObjectIdentity = ObjectIdentity
tFilterMIBConformance = _TFilterMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21)
)
_TFilterMIBCompliances_ObjectIdentity = ObjectIdentity
tFilterMIBCompliances = _TFilterMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 1)
)
_TFilterMIBGroups_ObjectIdentity = ObjectIdentity
tFilterMIBGroups = _TFilterMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2)
)
_TFilterObjects_ObjectIdentity = ObjectIdentity
tFilterObjects = _TFilterObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21)
)
_TIPFilterTable_Object = MibTable
tIPFilterTable = _TIPFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 1)
)
if mibBuilder.loadTexts:
    tIPFilterTable.setStatus("current")
_TIPFilterEntry_Object = MibTableRow
tIPFilterEntry = _TIPFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 1, 1)
)
tIPFilterEntry.setIndexNames(
    (0, "TIMETRA-FILTER-MIB", "tIPFilterId"),
)
if mibBuilder.loadTexts:
    tIPFilterEntry.setStatus("current")
_TIPFilterId_Type = TAnyFilterID
_TIPFilterId_Object = MibTableColumn
tIPFilterId = _TIPFilterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 1, 1, 1),
    _TIPFilterId_Type()
)
tIPFilterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tIPFilterId.setStatus("current")
_TIPFilterRowStatus_Type = RowStatus
_TIPFilterRowStatus_Object = MibTableColumn
tIPFilterRowStatus = _TIPFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 1, 1, 2),
    _TIPFilterRowStatus_Type()
)
tIPFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterRowStatus.setStatus("current")


class _TIPFilterScope_Type(TFilterScope):
    """Custom type tIPFilterScope based on TFilterScope"""
    defaultValue = 2


_TIPFilterScope_Type.__name__ = "TFilterScope"
_TIPFilterScope_Object = MibTableColumn
tIPFilterScope = _TIPFilterScope_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 1, 1, 3),
    _TIPFilterScope_Type()
)
tIPFilterScope.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterScope.setStatus("current")


class _TIPFilterDescription_Type(TItemDescription):
    """Custom type tIPFilterDescription based on TItemDescription"""
    defaultHexValue = ""


_TIPFilterDescription_Type.__name__ = "TItemDescription"
_TIPFilterDescription_Object = MibTableColumn
tIPFilterDescription = _TIPFilterDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 1, 1, 4),
    _TIPFilterDescription_Type()
)
tIPFilterDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterDescription.setStatus("current")


class _TIPFilterDefaultAction_Type(TFilterAction):
    """Custom type tIPFilterDefaultAction based on TFilterAction"""
    defaultValue = 1


_TIPFilterDefaultAction_Type.__name__ = "TFilterAction"
_TIPFilterDefaultAction_Object = MibTableColumn
tIPFilterDefaultAction = _TIPFilterDefaultAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 1, 1, 5),
    _TIPFilterDefaultAction_Type()
)
tIPFilterDefaultAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterDefaultAction.setStatus("current")


class _TIPFilterRadiusInsertPt_Type(TEntryIdOrZero):
    """Custom type tIPFilterRadiusInsertPt based on TEntryIdOrZero"""
    defaultValue = 0


_TIPFilterRadiusInsertPt_Type.__name__ = "TEntryIdOrZero"
_TIPFilterRadiusInsertPt_Object = MibTableColumn
tIPFilterRadiusInsertPt = _TIPFilterRadiusInsertPt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 1, 1, 6),
    _TIPFilterRadiusInsertPt_Type()
)
tIPFilterRadiusInsertPt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterRadiusInsertPt.setStatus("current")


class _TIPFilterRadiusInsertSize_Type(TEntryIdOrZero):
    """Custom type tIPFilterRadiusInsertSize based on TEntryIdOrZero"""
    defaultValue = 0


_TIPFilterRadiusInsertSize_Type.__name__ = "TEntryIdOrZero"
_TIPFilterRadiusInsertSize_Object = MibTableColumn
tIPFilterRadiusInsertSize = _TIPFilterRadiusInsertSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 1, 1, 7),
    _TIPFilterRadiusInsertSize_Type()
)
tIPFilterRadiusInsertSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterRadiusInsertSize.setStatus("current")


class _TIPFilterCreditCntrlInsertPt_Type(TEntryIdOrZero):
    """Custom type tIPFilterCreditCntrlInsertPt based on TEntryIdOrZero"""
    defaultValue = 0


_TIPFilterCreditCntrlInsertPt_Type.__name__ = "TEntryIdOrZero"
_TIPFilterCreditCntrlInsertPt_Object = MibTableColumn
tIPFilterCreditCntrlInsertPt = _TIPFilterCreditCntrlInsertPt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 1, 1, 8),
    _TIPFilterCreditCntrlInsertPt_Type()
)
tIPFilterCreditCntrlInsertPt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterCreditCntrlInsertPt.setStatus("current")


class _TIPFilterCreditCntrlInsertSize_Type(TEntryIdOrZero):
    """Custom type tIPFilterCreditCntrlInsertSize based on TEntryIdOrZero"""
    defaultValue = 0


_TIPFilterCreditCntrlInsertSize_Type.__name__ = "TEntryIdOrZero"
_TIPFilterCreditCntrlInsertSize_Object = MibTableColumn
tIPFilterCreditCntrlInsertSize = _TIPFilterCreditCntrlInsertSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 1, 1, 9),
    _TIPFilterCreditCntrlInsertSize_Type()
)
tIPFilterCreditCntrlInsertSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterCreditCntrlInsertSize.setStatus("current")


class _TIPFilterSubInsertHighWmark_Type(Integer32):
    """Custom type tIPFilterSubInsertHighWmark based on Integer32"""
    defaultValue = 95

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TIPFilterSubInsertHighWmark_Type.__name__ = "Integer32"
_TIPFilterSubInsertHighWmark_Object = MibTableColumn
tIPFilterSubInsertHighWmark = _TIPFilterSubInsertHighWmark_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 1, 1, 10),
    _TIPFilterSubInsertHighWmark_Type()
)
tIPFilterSubInsertHighWmark.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterSubInsertHighWmark.setStatus("current")


class _TIPFilterSubInsertLowWmark_Type(Integer32):
    """Custom type tIPFilterSubInsertLowWmark based on Integer32"""
    defaultValue = 90

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TIPFilterSubInsertLowWmark_Type.__name__ = "Integer32"
_TIPFilterSubInsertLowWmark_Object = MibTableColumn
tIPFilterSubInsertLowWmark = _TIPFilterSubInsertLowWmark_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 1, 1, 11),
    _TIPFilterSubInsertLowWmark_Type()
)
tIPFilterSubInsertLowWmark.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterSubInsertLowWmark.setStatus("current")
_TIpFilterCreditCntrlNbrInsertd_Type = Unsigned32
_TIpFilterCreditCntrlNbrInsertd_Object = MibTableColumn
tIpFilterCreditCntrlNbrInsertd = _TIpFilterCreditCntrlNbrInsertd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 1, 1, 12),
    _TIpFilterCreditCntrlNbrInsertd_Type()
)
tIpFilterCreditCntrlNbrInsertd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIpFilterCreditCntrlNbrInsertd.setStatus("current")
_TIpFilterRadiusNbrInsertd_Type = Unsigned32
_TIpFilterRadiusNbrInsertd_Object = MibTableColumn
tIpFilterRadiusNbrInsertd = _TIpFilterRadiusNbrInsertd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 1, 1, 13),
    _TIpFilterRadiusNbrInsertd_Type()
)
tIpFilterRadiusNbrInsertd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIpFilterRadiusNbrInsertd.setStatus("current")


class _TIpFilterName_Type(TLNamedItemOrEmpty):
    """Custom type tIpFilterName based on TLNamedItemOrEmpty"""
    defaultHexValue = ""


_TIpFilterName_Type.__name__ = "TLNamedItemOrEmpty"
_TIpFilterName_Object = MibTableColumn
tIpFilterName = _TIpFilterName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 1, 1, 14),
    _TIpFilterName_Type()
)
tIpFilterName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIpFilterName.setStatus("current")


class _TIPFilterHostSharedInsertPt_Type(TEntryIdOrZero):
    """Custom type tIPFilterHostSharedInsertPt based on TEntryIdOrZero"""
    defaultValue = 0


_TIPFilterHostSharedInsertPt_Type.__name__ = "TEntryIdOrZero"
_TIPFilterHostSharedInsertPt_Object = MibTableColumn
tIPFilterHostSharedInsertPt = _TIPFilterHostSharedInsertPt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 1, 1, 15),
    _TIPFilterHostSharedInsertPt_Type()
)
tIPFilterHostSharedInsertPt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterHostSharedInsertPt.setStatus("current")


class _TIPFilterHostSharedInsertSize_Type(TEntryIdOrZero):
    """Custom type tIPFilterHostSharedInsertSize based on TEntryIdOrZero"""
    defaultValue = 0


_TIPFilterHostSharedInsertSize_Type.__name__ = "TEntryIdOrZero"
_TIPFilterHostSharedInsertSize_Object = MibTableColumn
tIPFilterHostSharedInsertSize = _TIPFilterHostSharedInsertSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 1, 1, 16),
    _TIPFilterHostSharedInsertSize_Type()
)
tIPFilterHostSharedInsertSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterHostSharedInsertSize.setStatus("current")
_TIpFilterHostSharedNbrInsertd_Type = Unsigned32
_TIpFilterHostSharedNbrInsertd_Object = MibTableColumn
tIpFilterHostSharedNbrInsertd = _TIpFilterHostSharedNbrInsertd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 1, 1, 17),
    _TIpFilterHostSharedNbrInsertd_Type()
)
tIpFilterHostSharedNbrInsertd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIpFilterHostSharedNbrInsertd.setStatus("current")


class _TIPFilterHostSharedHighWmark_Type(Integer32):
    """Custom type tIPFilterHostSharedHighWmark based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 8000),
    )


_TIPFilterHostSharedHighWmark_Type.__name__ = "Integer32"
_TIPFilterHostSharedHighWmark_Object = MibTableColumn
tIPFilterHostSharedHighWmark = _TIPFilterHostSharedHighWmark_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 1, 1, 18),
    _TIPFilterHostSharedHighWmark_Type()
)
tIPFilterHostSharedHighWmark.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterHostSharedHighWmark.setStatus("current")


class _TIPFilterHostSharedLowWmark_Type(Integer32):
    """Custom type tIPFilterHostSharedLowWmark based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 8000),
    )


_TIPFilterHostSharedLowWmark_Type.__name__ = "Integer32"
_TIPFilterHostSharedLowWmark_Object = MibTableColumn
tIPFilterHostSharedLowWmark = _TIPFilterHostSharedLowWmark_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 1, 1, 19),
    _TIPFilterHostSharedLowWmark_Type()
)
tIPFilterHostSharedLowWmark.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterHostSharedLowWmark.setStatus("current")
_TIPFilterNbrHostSharedFltrs_Type = Unsigned32
_TIPFilterNbrHostSharedFltrs_Object = MibTableColumn
tIPFilterNbrHostSharedFltrs = _TIPFilterNbrHostSharedFltrs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 1, 1, 20),
    _TIPFilterNbrHostSharedFltrs_Type()
)
tIPFilterNbrHostSharedFltrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPFilterNbrHostSharedFltrs.setStatus("current")
_TIPFilterParamsTable_Object = MibTable
tIPFilterParamsTable = _TIPFilterParamsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2)
)
if mibBuilder.loadTexts:
    tIPFilterParamsTable.setStatus("current")
_TIPFilterParamsEntry_Object = MibTableRow
tIPFilterParamsEntry = _TIPFilterParamsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1)
)
tIPFilterParamsEntry.setIndexNames(
    (0, "TIMETRA-FILTER-MIB", "tIPFilterId"),
    (0, "TIMETRA-FILTER-MIB", "tIPFilterParamsIndex"),
)
if mibBuilder.loadTexts:
    tIPFilterParamsEntry.setStatus("current")
_TIPFilterParamsIndex_Type = TAnyEntryId
_TIPFilterParamsIndex_Object = MibTableColumn
tIPFilterParamsIndex = _TIPFilterParamsIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 1),
    _TIPFilterParamsIndex_Type()
)
tIPFilterParamsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tIPFilterParamsIndex.setStatus("current")
_TIPFilterParamsRowStatus_Type = RowStatus
_TIPFilterParamsRowStatus_Object = MibTableColumn
tIPFilterParamsRowStatus = _TIPFilterParamsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 2),
    _TIPFilterParamsRowStatus_Type()
)
tIPFilterParamsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsRowStatus.setStatus("current")


class _TIPFilterParamsLogId_Type(TFilterLogId):
    """Custom type tIPFilterParamsLogId based on TFilterLogId"""
    defaultValue = 0


_TIPFilterParamsLogId_Type.__name__ = "TFilterLogId"
_TIPFilterParamsLogId_Object = MibTableColumn
tIPFilterParamsLogId = _TIPFilterParamsLogId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 3),
    _TIPFilterParamsLogId_Type()
)
tIPFilterParamsLogId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsLogId.setStatus("current")


class _TIPFilterParamsDescription_Type(TItemDescription):
    """Custom type tIPFilterParamsDescription based on TItemDescription"""
    defaultHexValue = ""


_TIPFilterParamsDescription_Type.__name__ = "TItemDescription"
_TIPFilterParamsDescription_Object = MibTableColumn
tIPFilterParamsDescription = _TIPFilterParamsDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 4),
    _TIPFilterParamsDescription_Type()
)
tIPFilterParamsDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsDescription.setStatus("current")


class _TIPFilterParamsAction_Type(TFilterActionOrDefault):
    """Custom type tIPFilterParamsAction based on TFilterActionOrDefault"""
    defaultValue = 1


_TIPFilterParamsAction_Type.__name__ = "TFilterActionOrDefault"
_TIPFilterParamsAction_Object = MibTableColumn
tIPFilterParamsAction = _TIPFilterParamsAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 5),
    _TIPFilterParamsAction_Type()
)
tIPFilterParamsAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsAction.setStatus("current")


class _TIPFilterParamsForwardNH_Type(IpAddress):
    """Custom type tIPFilterParamsForwardNH based on IpAddress"""
    defaultHexValue = "00000000"


_TIPFilterParamsForwardNH_Type.__name__ = "IpAddress"
_TIPFilterParamsForwardNH_Object = MibTableColumn
tIPFilterParamsForwardNH = _TIPFilterParamsForwardNH_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 6),
    _TIPFilterParamsForwardNH_Type()
)
tIPFilterParamsForwardNH.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsForwardNH.setStatus("current")


class _TIPFilterParamsForwardNHIndirect_Type(TruthValue):
    """Custom type tIPFilterParamsForwardNHIndirect based on TruthValue"""
    defaultValue = 2


_TIPFilterParamsForwardNHIndirect_Type.__name__ = "TruthValue"
_TIPFilterParamsForwardNHIndirect_Object = MibTableColumn
tIPFilterParamsForwardNHIndirect = _TIPFilterParamsForwardNHIndirect_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 7),
    _TIPFilterParamsForwardNHIndirect_Type()
)
tIPFilterParamsForwardNHIndirect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsForwardNHIndirect.setStatus("current")


class _TIPFilterParamsRemarkDSCP_Type(TDSCPFilterActionValue):
    """Custom type tIPFilterParamsRemarkDSCP based on TDSCPFilterActionValue"""
    defaultValue = -1


_TIPFilterParamsRemarkDSCP_Type.__name__ = "TDSCPFilterActionValue"
_TIPFilterParamsRemarkDSCP_Object = MibTableColumn
tIPFilterParamsRemarkDSCP = _TIPFilterParamsRemarkDSCP_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 8),
    _TIPFilterParamsRemarkDSCP_Type()
)
tIPFilterParamsRemarkDSCP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsRemarkDSCP.setStatus("current")


class _TIPFilterParamsRemarkDSCPMask_Type(TDSCPFilterActionValue):
    """Custom type tIPFilterParamsRemarkDSCPMask based on TDSCPFilterActionValue"""
    defaultValue = 255


_TIPFilterParamsRemarkDSCPMask_Type.__name__ = "TDSCPFilterActionValue"
_TIPFilterParamsRemarkDSCPMask_Object = MibTableColumn
tIPFilterParamsRemarkDSCPMask = _TIPFilterParamsRemarkDSCPMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 9),
    _TIPFilterParamsRemarkDSCPMask_Type()
)
tIPFilterParamsRemarkDSCPMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsRemarkDSCPMask.setStatus("current")


class _TIPFilterParamsRemarkDot1p_Type(Dot1PPriority):
    """Custom type tIPFilterParamsRemarkDot1p based on Dot1PPriority"""
    defaultValue = -1


_TIPFilterParamsRemarkDot1p_Type.__name__ = "Dot1PPriority"
_TIPFilterParamsRemarkDot1p_Object = MibTableColumn
tIPFilterParamsRemarkDot1p = _TIPFilterParamsRemarkDot1p_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 10),
    _TIPFilterParamsRemarkDot1p_Type()
)
tIPFilterParamsRemarkDot1p.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsRemarkDot1p.setStatus("current")


class _TIPFilterParamsSourceIpAddr_Type(IpAddress):
    """Custom type tIPFilterParamsSourceIpAddr based on IpAddress"""
    defaultHexValue = "00000000"


_TIPFilterParamsSourceIpAddr_Type.__name__ = "IpAddress"
_TIPFilterParamsSourceIpAddr_Object = MibTableColumn
tIPFilterParamsSourceIpAddr = _TIPFilterParamsSourceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 11),
    _TIPFilterParamsSourceIpAddr_Type()
)
tIPFilterParamsSourceIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsSourceIpAddr.setStatus("current")


class _TIPFilterParamsSourceIpMask_Type(IpAddressPrefixLength):
    """Custom type tIPFilterParamsSourceIpMask based on IpAddressPrefixLength"""
    defaultValue = 0


_TIPFilterParamsSourceIpMask_Type.__name__ = "IpAddressPrefixLength"
_TIPFilterParamsSourceIpMask_Object = MibTableColumn
tIPFilterParamsSourceIpMask = _TIPFilterParamsSourceIpMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 12),
    _TIPFilterParamsSourceIpMask_Type()
)
tIPFilterParamsSourceIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsSourceIpMask.setStatus("current")


class _TIPFilterParamsDestinationIpAddr_Type(IpAddress):
    """Custom type tIPFilterParamsDestinationIpAddr based on IpAddress"""
    defaultHexValue = "00000000"


_TIPFilterParamsDestinationIpAddr_Type.__name__ = "IpAddress"
_TIPFilterParamsDestinationIpAddr_Object = MibTableColumn
tIPFilterParamsDestinationIpAddr = _TIPFilterParamsDestinationIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 13),
    _TIPFilterParamsDestinationIpAddr_Type()
)
tIPFilterParamsDestinationIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsDestinationIpAddr.setStatus("current")


class _TIPFilterParamsDestinationIpMask_Type(IpAddressPrefixLength):
    """Custom type tIPFilterParamsDestinationIpMask based on IpAddressPrefixLength"""
    defaultValue = 0


_TIPFilterParamsDestinationIpMask_Type.__name__ = "IpAddressPrefixLength"
_TIPFilterParamsDestinationIpMask_Object = MibTableColumn
tIPFilterParamsDestinationIpMask = _TIPFilterParamsDestinationIpMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 14),
    _TIPFilterParamsDestinationIpMask_Type()
)
tIPFilterParamsDestinationIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsDestinationIpMask.setStatus("current")


class _TIPFilterParamsProtocol_Type(TIpProtocol):
    """Custom type tIPFilterParamsProtocol based on TIpProtocol"""
    defaultValue = -1


_TIPFilterParamsProtocol_Type.__name__ = "TIpProtocol"
_TIPFilterParamsProtocol_Object = MibTableColumn
tIPFilterParamsProtocol = _TIPFilterParamsProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 15),
    _TIPFilterParamsProtocol_Type()
)
tIPFilterParamsProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsProtocol.setStatus("current")


class _TIPFilterParamsSourcePortValue1_Type(TTcpUdpPort):
    """Custom type tIPFilterParamsSourcePortValue1 based on TTcpUdpPort"""
    defaultValue = 0


_TIPFilterParamsSourcePortValue1_Type.__name__ = "TTcpUdpPort"
_TIPFilterParamsSourcePortValue1_Object = MibTableColumn
tIPFilterParamsSourcePortValue1 = _TIPFilterParamsSourcePortValue1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 16),
    _TIPFilterParamsSourcePortValue1_Type()
)
tIPFilterParamsSourcePortValue1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsSourcePortValue1.setStatus("current")


class _TIPFilterParamsSourcePortValue2_Type(TTcpUdpPort):
    """Custom type tIPFilterParamsSourcePortValue2 based on TTcpUdpPort"""
    defaultValue = 0


_TIPFilterParamsSourcePortValue2_Type.__name__ = "TTcpUdpPort"
_TIPFilterParamsSourcePortValue2_Object = MibTableColumn
tIPFilterParamsSourcePortValue2 = _TIPFilterParamsSourcePortValue2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 17),
    _TIPFilterParamsSourcePortValue2_Type()
)
tIPFilterParamsSourcePortValue2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsSourcePortValue2.setStatus("current")


class _TIPFilterParamsSourcePortOperator_Type(TTcpUdpPortOperator):
    """Custom type tIPFilterParamsSourcePortOperator based on TTcpUdpPortOperator"""
    defaultValue = 0


_TIPFilterParamsSourcePortOperator_Type.__name__ = "TTcpUdpPortOperator"
_TIPFilterParamsSourcePortOperator_Object = MibTableColumn
tIPFilterParamsSourcePortOperator = _TIPFilterParamsSourcePortOperator_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 18),
    _TIPFilterParamsSourcePortOperator_Type()
)
tIPFilterParamsSourcePortOperator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsSourcePortOperator.setStatus("current")


class _TIPFilterParamsDestPortValue1_Type(TTcpUdpPort):
    """Custom type tIPFilterParamsDestPortValue1 based on TTcpUdpPort"""
    defaultValue = 0


_TIPFilterParamsDestPortValue1_Type.__name__ = "TTcpUdpPort"
_TIPFilterParamsDestPortValue1_Object = MibTableColumn
tIPFilterParamsDestPortValue1 = _TIPFilterParamsDestPortValue1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 19),
    _TIPFilterParamsDestPortValue1_Type()
)
tIPFilterParamsDestPortValue1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsDestPortValue1.setStatus("current")


class _TIPFilterParamsDestPortValue2_Type(TTcpUdpPort):
    """Custom type tIPFilterParamsDestPortValue2 based on TTcpUdpPort"""
    defaultValue = 0


_TIPFilterParamsDestPortValue2_Type.__name__ = "TTcpUdpPort"
_TIPFilterParamsDestPortValue2_Object = MibTableColumn
tIPFilterParamsDestPortValue2 = _TIPFilterParamsDestPortValue2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 20),
    _TIPFilterParamsDestPortValue2_Type()
)
tIPFilterParamsDestPortValue2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsDestPortValue2.setStatus("current")


class _TIPFilterParamsDestPortOperator_Type(TTcpUdpPortOperator):
    """Custom type tIPFilterParamsDestPortOperator based on TTcpUdpPortOperator"""
    defaultValue = 0


_TIPFilterParamsDestPortOperator_Type.__name__ = "TTcpUdpPortOperator"
_TIPFilterParamsDestPortOperator_Object = MibTableColumn
tIPFilterParamsDestPortOperator = _TIPFilterParamsDestPortOperator_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 21),
    _TIPFilterParamsDestPortOperator_Type()
)
tIPFilterParamsDestPortOperator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsDestPortOperator.setStatus("current")


class _TIPFilterParamsDSCP_Type(TDSCPNameOrEmpty):
    """Custom type tIPFilterParamsDSCP based on TDSCPNameOrEmpty"""
    defaultHexValue = ""


_TIPFilterParamsDSCP_Type.__name__ = "TDSCPNameOrEmpty"
_TIPFilterParamsDSCP_Object = MibTableColumn
tIPFilterParamsDSCP = _TIPFilterParamsDSCP_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 22),
    _TIPFilterParamsDSCP_Type()
)
tIPFilterParamsDSCP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsDSCP.setStatus("current")


class _TIPFilterParamsFragment_Type(TItemMatch):
    """Custom type tIPFilterParamsFragment based on TItemMatch"""
    defaultValue = 1


_TIPFilterParamsFragment_Type.__name__ = "TItemMatch"
_TIPFilterParamsFragment_Object = MibTableColumn
tIPFilterParamsFragment = _TIPFilterParamsFragment_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 24),
    _TIPFilterParamsFragment_Type()
)
tIPFilterParamsFragment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsFragment.setStatus("current")


class _TIPFilterParamsOptionPresent_Type(TItemMatch):
    """Custom type tIPFilterParamsOptionPresent based on TItemMatch"""
    defaultValue = 1


_TIPFilterParamsOptionPresent_Type.__name__ = "TItemMatch"
_TIPFilterParamsOptionPresent_Object = MibTableColumn
tIPFilterParamsOptionPresent = _TIPFilterParamsOptionPresent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 25),
    _TIPFilterParamsOptionPresent_Type()
)
tIPFilterParamsOptionPresent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsOptionPresent.setStatus("current")


class _TIPFilterParamsIpOptionValue_Type(TIpOption):
    """Custom type tIPFilterParamsIpOptionValue based on TIpOption"""
    defaultValue = 0


_TIPFilterParamsIpOptionValue_Type.__name__ = "TIpOption"
_TIPFilterParamsIpOptionValue_Object = MibTableColumn
tIPFilterParamsIpOptionValue = _TIPFilterParamsIpOptionValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 26),
    _TIPFilterParamsIpOptionValue_Type()
)
tIPFilterParamsIpOptionValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsIpOptionValue.setStatus("current")


class _TIPFilterParamsIpOptionMask_Type(TIpOption):
    """Custom type tIPFilterParamsIpOptionMask based on TIpOption"""
    defaultValue = 0


_TIPFilterParamsIpOptionMask_Type.__name__ = "TIpOption"
_TIPFilterParamsIpOptionMask_Object = MibTableColumn
tIPFilterParamsIpOptionMask = _TIPFilterParamsIpOptionMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 27),
    _TIPFilterParamsIpOptionMask_Type()
)
tIPFilterParamsIpOptionMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsIpOptionMask.setStatus("current")


class _TIPFilterParamsMultipleOption_Type(TItemMatch):
    """Custom type tIPFilterParamsMultipleOption based on TItemMatch"""
    defaultValue = 1


_TIPFilterParamsMultipleOption_Type.__name__ = "TItemMatch"
_TIPFilterParamsMultipleOption_Object = MibTableColumn
tIPFilterParamsMultipleOption = _TIPFilterParamsMultipleOption_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 28),
    _TIPFilterParamsMultipleOption_Type()
)
tIPFilterParamsMultipleOption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsMultipleOption.setStatus("current")


class _TIPFilterParamsTcpSyn_Type(TItemMatch):
    """Custom type tIPFilterParamsTcpSyn based on TItemMatch"""
    defaultValue = 1


_TIPFilterParamsTcpSyn_Type.__name__ = "TItemMatch"
_TIPFilterParamsTcpSyn_Object = MibTableColumn
tIPFilterParamsTcpSyn = _TIPFilterParamsTcpSyn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 29),
    _TIPFilterParamsTcpSyn_Type()
)
tIPFilterParamsTcpSyn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsTcpSyn.setStatus("current")


class _TIPFilterParamsTcpAck_Type(TItemMatch):
    """Custom type tIPFilterParamsTcpAck based on TItemMatch"""
    defaultValue = 1


_TIPFilterParamsTcpAck_Type.__name__ = "TItemMatch"
_TIPFilterParamsTcpAck_Object = MibTableColumn
tIPFilterParamsTcpAck = _TIPFilterParamsTcpAck_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 30),
    _TIPFilterParamsTcpAck_Type()
)
tIPFilterParamsTcpAck.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsTcpAck.setStatus("current")


class _TIPFilterParamsIcmpCode_Type(Integer32):
    """Custom type tIPFilterParamsIcmpCode based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 255),
    )


_TIPFilterParamsIcmpCode_Type.__name__ = "Integer32"
_TIPFilterParamsIcmpCode_Object = MibTableColumn
tIPFilterParamsIcmpCode = _TIPFilterParamsIcmpCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 31),
    _TIPFilterParamsIcmpCode_Type()
)
tIPFilterParamsIcmpCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsIcmpCode.setStatus("current")


class _TIPFilterParamsIcmpType_Type(Integer32):
    """Custom type tIPFilterParamsIcmpType based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 255),
    )


_TIPFilterParamsIcmpType_Type.__name__ = "Integer32"
_TIPFilterParamsIcmpType_Object = MibTableColumn
tIPFilterParamsIcmpType = _TIPFilterParamsIcmpType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 32),
    _TIPFilterParamsIcmpType_Type()
)
tIPFilterParamsIcmpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsIcmpType.setStatus("current")


class _TIPFilterParamsCflowdSample_Type(TruthValue):
    """Custom type tIPFilterParamsCflowdSample based on TruthValue"""
    defaultValue = 2


_TIPFilterParamsCflowdSample_Type.__name__ = "TruthValue"
_TIPFilterParamsCflowdSample_Object = MibTableColumn
tIPFilterParamsCflowdSample = _TIPFilterParamsCflowdSample_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 33),
    _TIPFilterParamsCflowdSample_Type()
)
tIPFilterParamsCflowdSample.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsCflowdSample.setStatus("current")


class _TIPFilterParamsCflowdIfSample_Type(TruthValue):
    """Custom type tIPFilterParamsCflowdIfSample based on TruthValue"""
    defaultValue = 1


_TIPFilterParamsCflowdIfSample_Type.__name__ = "TruthValue"
_TIPFilterParamsCflowdIfSample_Object = MibTableColumn
tIPFilterParamsCflowdIfSample = _TIPFilterParamsCflowdIfSample_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 34),
    _TIPFilterParamsCflowdIfSample_Type()
)
tIPFilterParamsCflowdIfSample.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsCflowdIfSample.setStatus("current")


class _TIPFilterParamsForwardNHInterface_Type(DisplayString):
    """Custom type tIPFilterParamsForwardNHInterface based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TIPFilterParamsForwardNHInterface_Type.__name__ = "DisplayString"
_TIPFilterParamsForwardNHInterface_Object = MibTableColumn
tIPFilterParamsForwardNHInterface = _TIPFilterParamsForwardNHInterface_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 35),
    _TIPFilterParamsForwardNHInterface_Type()
)
tIPFilterParamsForwardNHInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsForwardNHInterface.setStatus("current")
_TIPFilterParamsIngressHitCount_Type = Counter64
_TIPFilterParamsIngressHitCount_Object = MibTableColumn
tIPFilterParamsIngressHitCount = _TIPFilterParamsIngressHitCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 36),
    _TIPFilterParamsIngressHitCount_Type()
)
tIPFilterParamsIngressHitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPFilterParamsIngressHitCount.setStatus("current")
_TIPFilterParamsEgressHitCount_Type = Counter64
_TIPFilterParamsEgressHitCount_Object = MibTableColumn
tIPFilterParamsEgressHitCount = _TIPFilterParamsEgressHitCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 37),
    _TIPFilterParamsEgressHitCount_Type()
)
tIPFilterParamsEgressHitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPFilterParamsEgressHitCount.setStatus("current")
_TIPFilterParamsLogInstantiated_Type = TruthValue
_TIPFilterParamsLogInstantiated_Object = MibTableColumn
tIPFilterParamsLogInstantiated = _TIPFilterParamsLogInstantiated_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 38),
    _TIPFilterParamsLogInstantiated_Type()
)
tIPFilterParamsLogInstantiated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPFilterParamsLogInstantiated.setStatus("current")


class _TIPFilterParamsForwardRedPlcy_Type(TNamedItemOrEmpty):
    """Custom type tIPFilterParamsForwardRedPlcy based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TIPFilterParamsForwardRedPlcy_Type.__name__ = "TNamedItemOrEmpty"
_TIPFilterParamsForwardRedPlcy_Object = MibTableColumn
tIPFilterParamsForwardRedPlcy = _TIPFilterParamsForwardRedPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 39),
    _TIPFilterParamsForwardRedPlcy_Type()
)
tIPFilterParamsForwardRedPlcy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsForwardRedPlcy.setStatus("current")
_TIPFilterParamsActiveDest_Type = IpAddress
_TIPFilterParamsActiveDest_Object = MibTableColumn
tIPFilterParamsActiveDest = _TIPFilterParamsActiveDest_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 40),
    _TIPFilterParamsActiveDest_Type()
)
tIPFilterParamsActiveDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPFilterParamsActiveDest.setStatus("current")
_TIPFilterParamsFwdSvcId_Type = TmnxServId
_TIPFilterParamsFwdSvcId_Object = MibTableColumn
tIPFilterParamsFwdSvcId = _TIPFilterParamsFwdSvcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 41),
    _TIPFilterParamsFwdSvcId_Type()
)
tIPFilterParamsFwdSvcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPFilterParamsFwdSvcId.setStatus("current")


class _TIPFilterParamsFwdSapPortId_Type(TmnxPortID):
    """Custom type tIPFilterParamsFwdSapPortId based on TmnxPortID"""
    defaultValue = 0


_TIPFilterParamsFwdSapPortId_Type.__name__ = "TmnxPortID"
_TIPFilterParamsFwdSapPortId_Object = MibTableColumn
tIPFilterParamsFwdSapPortId = _TIPFilterParamsFwdSapPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 42),
    _TIPFilterParamsFwdSapPortId_Type()
)
tIPFilterParamsFwdSapPortId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsFwdSapPortId.setStatus("current")


class _TIPFilterParamsFwdSapEncapVal_Type(TmnxEncapVal):
    """Custom type tIPFilterParamsFwdSapEncapVal based on TmnxEncapVal"""
    defaultValue = 0


_TIPFilterParamsFwdSapEncapVal_Type.__name__ = "TmnxEncapVal"
_TIPFilterParamsFwdSapEncapVal_Object = MibTableColumn
tIPFilterParamsFwdSapEncapVal = _TIPFilterParamsFwdSapEncapVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 43),
    _TIPFilterParamsFwdSapEncapVal_Type()
)
tIPFilterParamsFwdSapEncapVal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsFwdSapEncapVal.setStatus("current")
_TIPFilterParamsFwdSdpBind_Type = SdpBindId
_TIPFilterParamsFwdSdpBind_Object = MibTableColumn
tIPFilterParamsFwdSdpBind = _TIPFilterParamsFwdSdpBind_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 44),
    _TIPFilterParamsFwdSdpBind_Type()
)
tIPFilterParamsFwdSdpBind.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsFwdSdpBind.setStatus("current")


class _TIPFilterParamsTimeRangeName_Type(TNamedItemOrEmpty):
    """Custom type tIPFilterParamsTimeRangeName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TIPFilterParamsTimeRangeName_Type.__name__ = "TNamedItemOrEmpty"
_TIPFilterParamsTimeRangeName_Object = MibTableColumn
tIPFilterParamsTimeRangeName = _TIPFilterParamsTimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 45),
    _TIPFilterParamsTimeRangeName_Type()
)
tIPFilterParamsTimeRangeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsTimeRangeName.setStatus("current")
_TIPFilterParamsTimeRangeState_Type = TTimeRangeState
_TIPFilterParamsTimeRangeState_Object = MibTableColumn
tIPFilterParamsTimeRangeState = _TIPFilterParamsTimeRangeState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 46),
    _TIPFilterParamsTimeRangeState_Type()
)
tIPFilterParamsTimeRangeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPFilterParamsTimeRangeState.setStatus("current")


class _TIPFilterParamsRedirectURL_Type(TmnxHttpRedirectUrl):
    """Custom type tIPFilterParamsRedirectURL based on TmnxHttpRedirectUrl"""
    defaultHexValue = ""


_TIPFilterParamsRedirectURL_Type.__name__ = "TmnxHttpRedirectUrl"
_TIPFilterParamsRedirectURL_Object = MibTableColumn
tIPFilterParamsRedirectURL = _TIPFilterParamsRedirectURL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 47),
    _TIPFilterParamsRedirectURL_Type()
)
tIPFilterParamsRedirectURL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsRedirectURL.setStatus("current")
_TIPFilterParamsSrcIpFullMask_Type = IpAddress
_TIPFilterParamsSrcIpFullMask_Object = MibTableColumn
tIPFilterParamsSrcIpFullMask = _TIPFilterParamsSrcIpFullMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 48),
    _TIPFilterParamsSrcIpFullMask_Type()
)
tIPFilterParamsSrcIpFullMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsSrcIpFullMask.setStatus("current")
_TIPFilterParamsDestIpFullMask_Type = IpAddress
_TIPFilterParamsDestIpFullMask_Object = MibTableColumn
tIPFilterParamsDestIpFullMask = _TIPFilterParamsDestIpFullMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 49),
    _TIPFilterParamsDestIpFullMask_Type()
)
tIPFilterParamsDestIpFullMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsDestIpFullMask.setStatus("current")
_TIPFilterParamsIngrHitByteCount_Type = Counter64
_TIPFilterParamsIngrHitByteCount_Object = MibTableColumn
tIPFilterParamsIngrHitByteCount = _TIPFilterParamsIngrHitByteCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 50),
    _TIPFilterParamsIngrHitByteCount_Type()
)
tIPFilterParamsIngrHitByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPFilterParamsIngrHitByteCount.setStatus("current")
_TIPFilterParamsEgrHitByteCount_Type = Counter64
_TIPFilterParamsEgrHitByteCount_Object = MibTableColumn
tIPFilterParamsEgrHitByteCount = _TIPFilterParamsEgrHitByteCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 51),
    _TIPFilterParamsEgrHitByteCount_Type()
)
tIPFilterParamsEgrHitByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPFilterParamsEgrHitByteCount.setStatus("current")


class _TIPFilterParamsFwdRtrId_Type(TmnxVRtrIDOrZero):
    """Custom type tIPFilterParamsFwdRtrId based on TmnxVRtrIDOrZero"""
    defaultValue = 0


_TIPFilterParamsFwdRtrId_Type.__name__ = "TmnxVRtrIDOrZero"
_TIPFilterParamsFwdRtrId_Object = MibTableColumn
tIPFilterParamsFwdRtrId = _TIPFilterParamsFwdRtrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 52),
    _TIPFilterParamsFwdRtrId_Type()
)
tIPFilterParamsFwdRtrId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsFwdRtrId.setStatus("current")


class _TIPFilterParamsSrcRouteOption_Type(TItemMatch):
    """Custom type tIPFilterParamsSrcRouteOption based on TItemMatch"""
    defaultValue = 1


_TIPFilterParamsSrcRouteOption_Type.__name__ = "TItemMatch"
_TIPFilterParamsSrcRouteOption_Object = MibTableColumn
tIPFilterParamsSrcRouteOption = _TIPFilterParamsSrcRouteOption_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 53),
    _TIPFilterParamsSrcRouteOption_Type()
)
tIPFilterParamsSrcRouteOption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsSrcRouteOption.setStatus("current")


class _TIPFilterParamsSrcIpPrefixList_Type(TNamedItemOrEmpty):
    """Custom type tIPFilterParamsSrcIpPrefixList based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TIPFilterParamsSrcIpPrefixList_Type.__name__ = "TNamedItemOrEmpty"
_TIPFilterParamsSrcIpPrefixList_Object = MibTableColumn
tIPFilterParamsSrcIpPrefixList = _TIPFilterParamsSrcIpPrefixList_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 54),
    _TIPFilterParamsSrcIpPrefixList_Type()
)
tIPFilterParamsSrcIpPrefixList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsSrcIpPrefixList.setStatus("current")


class _TIPFilterParamsDstIpPrefixList_Type(TNamedItemOrEmpty):
    """Custom type tIPFilterParamsDstIpPrefixList based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TIPFilterParamsDstIpPrefixList_Type.__name__ = "TNamedItemOrEmpty"
_TIPFilterParamsDstIpPrefixList_Object = MibTableColumn
tIPFilterParamsDstIpPrefixList = _TIPFilterParamsDstIpPrefixList_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 55),
    _TIPFilterParamsDstIpPrefixList_Type()
)
tIPFilterParamsDstIpPrefixList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsDstIpPrefixList.setStatus("current")


class _TIPFilterParamsPortSelector_Type(TFltrPortSelector):
    """Custom type tIPFilterParamsPortSelector based on TFltrPortSelector"""
    defaultValue = 0


_TIPFilterParamsPortSelector_Type.__name__ = "TFltrPortSelector"
_TIPFilterParamsPortSelector_Object = MibTableColumn
tIPFilterParamsPortSelector = _TIPFilterParamsPortSelector_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 56),
    _TIPFilterParamsPortSelector_Type()
)
tIPFilterParamsPortSelector.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsPortSelector.setStatus("current")


class _TIPFilterParamsSrcPortList_Type(TNamedItemOrEmpty):
    """Custom type tIPFilterParamsSrcPortList based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TIPFilterParamsSrcPortList_Type.__name__ = "TNamedItemOrEmpty"
_TIPFilterParamsSrcPortList_Object = MibTableColumn
tIPFilterParamsSrcPortList = _TIPFilterParamsSrcPortList_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 57),
    _TIPFilterParamsSrcPortList_Type()
)
tIPFilterParamsSrcPortList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsSrcPortList.setStatus("current")


class _TIPFilterParamsDstPortList_Type(TNamedItemOrEmpty):
    """Custom type tIPFilterParamsDstPortList based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TIPFilterParamsDstPortList_Type.__name__ = "TNamedItemOrEmpty"
_TIPFilterParamsDstPortList_Object = MibTableColumn
tIPFilterParamsDstPortList = _TIPFilterParamsDstPortList_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 58),
    _TIPFilterParamsDstPortList_Type()
)
tIPFilterParamsDstPortList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsDstPortList.setStatus("current")


class _TIPFilterParamsRdirAllwRadOvrd_Type(TruthValue):
    """Custom type tIPFilterParamsRdirAllwRadOvrd based on TruthValue"""
    defaultValue = 2


_TIPFilterParamsRdirAllwRadOvrd_Type.__name__ = "TruthValue"
_TIPFilterParamsRdirAllwRadOvrd_Object = MibTableColumn
tIPFilterParamsRdirAllwRadOvrd = _TIPFilterParamsRdirAllwRadOvrd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 59),
    _TIPFilterParamsRdirAllwRadOvrd_Type()
)
tIPFilterParamsRdirAllwRadOvrd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsRdirAllwRadOvrd.setStatus("current")


class _TIPFilterParamsNatPolicyName_Type(TNamedItemOrEmpty):
    """Custom type tIPFilterParamsNatPolicyName based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TIPFilterParamsNatPolicyName_Type.__name__ = "TNamedItemOrEmpty"
_TIPFilterParamsNatPolicyName_Object = MibTableColumn
tIPFilterParamsNatPolicyName = _TIPFilterParamsNatPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 60),
    _TIPFilterParamsNatPolicyName_Type()
)
tIPFilterParamsNatPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsNatPolicyName.setStatus("current")


class _TIPFilterParamsFwdLsp_Type(TmnxVRtrMplsLspID):
    """Custom type tIPFilterParamsFwdLsp based on TmnxVRtrMplsLspID"""
    defaultValue = 0


_TIPFilterParamsFwdLsp_Type.__name__ = "TmnxVRtrMplsLspID"
_TIPFilterParamsFwdLsp_Object = MibTableColumn
tIPFilterParamsFwdLsp = _TIPFilterParamsFwdLsp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 61),
    _TIPFilterParamsFwdLsp_Type()
)
tIPFilterParamsFwdLsp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsFwdLsp.setStatus("current")


class _TIPFilterParamsFwdLspRtrId_Type(TmnxVRtrIDOrZero):
    """Custom type tIPFilterParamsFwdLspRtrId based on TmnxVRtrIDOrZero"""
    defaultValue = 0


_TIPFilterParamsFwdLspRtrId_Type.__name__ = "TmnxVRtrIDOrZero"
_TIPFilterParamsFwdLspRtrId_Object = MibTableColumn
tIPFilterParamsFwdLspRtrId = _TIPFilterParamsFwdLspRtrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 62),
    _TIPFilterParamsFwdLspRtrId_Type()
)
tIPFilterParamsFwdLspRtrId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsFwdLspRtrId.setStatus("current")
_TMacFilterTable_Object = MibTable
tMacFilterTable = _TMacFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 3)
)
if mibBuilder.loadTexts:
    tMacFilterTable.setStatus("current")
_TMacFilterEntry_Object = MibTableRow
tMacFilterEntry = _TMacFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 3, 1)
)
tMacFilterEntry.setIndexNames(
    (0, "TIMETRA-FILTER-MIB", "tMacFilterId"),
)
if mibBuilder.loadTexts:
    tMacFilterEntry.setStatus("current")


class _TMacFilterId_Type(TMACFilterID):
    """Custom type tMacFilterId based on TMACFilterID"""
    subtypeSpec = TMACFilterID.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TMacFilterId_Type.__name__ = "TMACFilterID"
_TMacFilterId_Object = MibTableColumn
tMacFilterId = _TMacFilterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 3, 1, 1),
    _TMacFilterId_Type()
)
tMacFilterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tMacFilterId.setStatus("current")
_TMacFilterRowStatus_Type = RowStatus
_TMacFilterRowStatus_Object = MibTableColumn
tMacFilterRowStatus = _TMacFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 3, 1, 2),
    _TMacFilterRowStatus_Type()
)
tMacFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMacFilterRowStatus.setStatus("current")


class _TMacFilterScope_Type(TFilterScope):
    """Custom type tMacFilterScope based on TFilterScope"""
    defaultValue = 2


_TMacFilterScope_Type.__name__ = "TFilterScope"
_TMacFilterScope_Object = MibTableColumn
tMacFilterScope = _TMacFilterScope_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 3, 1, 3),
    _TMacFilterScope_Type()
)
tMacFilterScope.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMacFilterScope.setStatus("current")


class _TMacFilterDescription_Type(TItemDescription):
    """Custom type tMacFilterDescription based on TItemDescription"""
    defaultHexValue = ""


_TMacFilterDescription_Type.__name__ = "TItemDescription"
_TMacFilterDescription_Object = MibTableColumn
tMacFilterDescription = _TMacFilterDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 3, 1, 4),
    _TMacFilterDescription_Type()
)
tMacFilterDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMacFilterDescription.setStatus("current")


class _TMacFilterDefaultAction_Type(TFilterAction):
    """Custom type tMacFilterDefaultAction based on TFilterAction"""
    defaultValue = 1


_TMacFilterDefaultAction_Type.__name__ = "TFilterAction"
_TMacFilterDefaultAction_Object = MibTableColumn
tMacFilterDefaultAction = _TMacFilterDefaultAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 3, 1, 5),
    _TMacFilterDefaultAction_Type()
)
tMacFilterDefaultAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMacFilterDefaultAction.setStatus("current")


class _TMacFilterType_Type(TMacFilterType):
    """Custom type tMacFilterType based on TMacFilterType"""
    defaultValue = 1


_TMacFilterType_Type.__name__ = "TMacFilterType"
_TMacFilterType_Object = MibTableColumn
tMacFilterType = _TMacFilterType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 3, 1, 6),
    _TMacFilterType_Type()
)
tMacFilterType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMacFilterType.setStatus("current")


class _TMacFilterName_Type(TLNamedItemOrEmpty):
    """Custom type tMacFilterName based on TLNamedItemOrEmpty"""
    defaultHexValue = ""


_TMacFilterName_Type.__name__ = "TLNamedItemOrEmpty"
_TMacFilterName_Object = MibTableColumn
tMacFilterName = _TMacFilterName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 3, 1, 7),
    _TMacFilterName_Type()
)
tMacFilterName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMacFilterName.setStatus("current")
_TMacFilterParamsTable_Object = MibTable
tMacFilterParamsTable = _TMacFilterParamsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 4)
)
if mibBuilder.loadTexts:
    tMacFilterParamsTable.setStatus("current")
_TMacFilterParamsEntry_Object = MibTableRow
tMacFilterParamsEntry = _TMacFilterParamsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 4, 1)
)
tMacFilterParamsEntry.setIndexNames(
    (0, "TIMETRA-FILTER-MIB", "tMacFilterId"),
    (0, "TIMETRA-FILTER-MIB", "tMacFilterParamsIndex"),
)
if mibBuilder.loadTexts:
    tMacFilterParamsEntry.setStatus("current")
_TMacFilterParamsIndex_Type = TEntryId
_TMacFilterParamsIndex_Object = MibTableColumn
tMacFilterParamsIndex = _TMacFilterParamsIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 4, 1, 1),
    _TMacFilterParamsIndex_Type()
)
tMacFilterParamsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tMacFilterParamsIndex.setStatus("current")
_TMacFilterParamsRowStatus_Type = RowStatus
_TMacFilterParamsRowStatus_Object = MibTableColumn
tMacFilterParamsRowStatus = _TMacFilterParamsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 4, 1, 2),
    _TMacFilterParamsRowStatus_Type()
)
tMacFilterParamsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMacFilterParamsRowStatus.setStatus("current")


class _TMacFilterParamsLogId_Type(TFilterLogId):
    """Custom type tMacFilterParamsLogId based on TFilterLogId"""
    defaultValue = 0


_TMacFilterParamsLogId_Type.__name__ = "TFilterLogId"
_TMacFilterParamsLogId_Object = MibTableColumn
tMacFilterParamsLogId = _TMacFilterParamsLogId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 4, 1, 3),
    _TMacFilterParamsLogId_Type()
)
tMacFilterParamsLogId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMacFilterParamsLogId.setStatus("current")


class _TMacFilterParamsDescription_Type(TItemDescription):
    """Custom type tMacFilterParamsDescription based on TItemDescription"""
    defaultHexValue = ""


_TMacFilterParamsDescription_Type.__name__ = "TItemDescription"
_TMacFilterParamsDescription_Object = MibTableColumn
tMacFilterParamsDescription = _TMacFilterParamsDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 4, 1, 4),
    _TMacFilterParamsDescription_Type()
)
tMacFilterParamsDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMacFilterParamsDescription.setStatus("current")


class _TMacFilterParamsAction_Type(TFilterActionOrDefault):
    """Custom type tMacFilterParamsAction based on TFilterActionOrDefault"""
    defaultValue = 1


_TMacFilterParamsAction_Type.__name__ = "TFilterActionOrDefault"
_TMacFilterParamsAction_Object = MibTableColumn
tMacFilterParamsAction = _TMacFilterParamsAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 4, 1, 5),
    _TMacFilterParamsAction_Type()
)
tMacFilterParamsAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMacFilterParamsAction.setStatus("current")


class _TMacFilterParamsFrameType_Type(TFrameType):
    """Custom type tMacFilterParamsFrameType based on TFrameType"""
    defaultValue = 0


_TMacFilterParamsFrameType_Type.__name__ = "TFrameType"
_TMacFilterParamsFrameType_Object = MibTableColumn
tMacFilterParamsFrameType = _TMacFilterParamsFrameType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 4, 1, 6),
    _TMacFilterParamsFrameType_Type()
)
tMacFilterParamsFrameType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMacFilterParamsFrameType.setStatus("current")


class _TMacFilterParamsSrcMAC_Type(MacAddress):
    """Custom type tMacFilterParamsSrcMAC based on MacAddress"""
    defaultHexValue = "000000000000"


_TMacFilterParamsSrcMAC_Type.__name__ = "MacAddress"
_TMacFilterParamsSrcMAC_Object = MibTableColumn
tMacFilterParamsSrcMAC = _TMacFilterParamsSrcMAC_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 4, 1, 8),
    _TMacFilterParamsSrcMAC_Type()
)
tMacFilterParamsSrcMAC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMacFilterParamsSrcMAC.setStatus("current")


class _TMacFilterParamsSrcMACMask_Type(MacAddress):
    """Custom type tMacFilterParamsSrcMACMask based on MacAddress"""
    defaultHexValue = "000000000000"


_TMacFilterParamsSrcMACMask_Type.__name__ = "MacAddress"
_TMacFilterParamsSrcMACMask_Object = MibTableColumn
tMacFilterParamsSrcMACMask = _TMacFilterParamsSrcMACMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 4, 1, 9),
    _TMacFilterParamsSrcMACMask_Type()
)
tMacFilterParamsSrcMACMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMacFilterParamsSrcMACMask.setStatus("current")


class _TMacFilterParamsDstMAC_Type(MacAddress):
    """Custom type tMacFilterParamsDstMAC based on MacAddress"""
    defaultHexValue = "000000000000"


_TMacFilterParamsDstMAC_Type.__name__ = "MacAddress"
_TMacFilterParamsDstMAC_Object = MibTableColumn
tMacFilterParamsDstMAC = _TMacFilterParamsDstMAC_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 4, 1, 10),
    _TMacFilterParamsDstMAC_Type()
)
tMacFilterParamsDstMAC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMacFilterParamsDstMAC.setStatus("current")


class _TMacFilterParamsDstMACMask_Type(MacAddress):
    """Custom type tMacFilterParamsDstMACMask based on MacAddress"""
    defaultHexValue = "000000000000"


_TMacFilterParamsDstMACMask_Type.__name__ = "MacAddress"
_TMacFilterParamsDstMACMask_Object = MibTableColumn
tMacFilterParamsDstMACMask = _TMacFilterParamsDstMACMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 4, 1, 11),
    _TMacFilterParamsDstMACMask_Type()
)
tMacFilterParamsDstMACMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMacFilterParamsDstMACMask.setStatus("current")


class _TMacFilterParamsDot1pValue_Type(Dot1PPriority):
    """Custom type tMacFilterParamsDot1pValue based on Dot1PPriority"""
    defaultValue = -1


_TMacFilterParamsDot1pValue_Type.__name__ = "Dot1PPriority"
_TMacFilterParamsDot1pValue_Object = MibTableColumn
tMacFilterParamsDot1pValue = _TMacFilterParamsDot1pValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 4, 1, 12),
    _TMacFilterParamsDot1pValue_Type()
)
tMacFilterParamsDot1pValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMacFilterParamsDot1pValue.setStatus("current")


class _TMacFilterParamsDot1pMask_Type(Dot1PPriority):
    """Custom type tMacFilterParamsDot1pMask based on Dot1PPriority"""
    defaultValue = 0

    subtypeSpec = Dot1PPriority.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TMacFilterParamsDot1pMask_Type.__name__ = "Dot1PPriority"
_TMacFilterParamsDot1pMask_Object = MibTableColumn
tMacFilterParamsDot1pMask = _TMacFilterParamsDot1pMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 4, 1, 13),
    _TMacFilterParamsDot1pMask_Type()
)
tMacFilterParamsDot1pMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMacFilterParamsDot1pMask.setStatus("current")


class _TMacFilterParamsEtherType_Type(Integer32):
    """Custom type tMacFilterParamsEtherType based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 65535),
    )


_TMacFilterParamsEtherType_Type.__name__ = "Integer32"
_TMacFilterParamsEtherType_Object = MibTableColumn
tMacFilterParamsEtherType = _TMacFilterParamsEtherType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 4, 1, 14),
    _TMacFilterParamsEtherType_Type()
)
tMacFilterParamsEtherType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMacFilterParamsEtherType.setStatus("current")


class _TMacFilterParamsDsap_Type(ServiceAccessPoint):
    """Custom type tMacFilterParamsDsap based on ServiceAccessPoint"""
    defaultValue = -1


_TMacFilterParamsDsap_Type.__name__ = "ServiceAccessPoint"
_TMacFilterParamsDsap_Object = MibTableColumn
tMacFilterParamsDsap = _TMacFilterParamsDsap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 4, 1, 15),
    _TMacFilterParamsDsap_Type()
)
tMacFilterParamsDsap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMacFilterParamsDsap.setStatus("current")


class _TMacFilterParamsDsapMask_Type(ServiceAccessPoint):
    """Custom type tMacFilterParamsDsapMask based on ServiceAccessPoint"""
    defaultValue = -1


_TMacFilterParamsDsapMask_Type.__name__ = "ServiceAccessPoint"
_TMacFilterParamsDsapMask_Object = MibTableColumn
tMacFilterParamsDsapMask = _TMacFilterParamsDsapMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 4, 1, 16),
    _TMacFilterParamsDsapMask_Type()
)
tMacFilterParamsDsapMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMacFilterParamsDsapMask.setStatus("current")


class _TMacFilterParamsSsap_Type(ServiceAccessPoint):
    """Custom type tMacFilterParamsSsap based on ServiceAccessPoint"""
    defaultValue = -1


_TMacFilterParamsSsap_Type.__name__ = "ServiceAccessPoint"
_TMacFilterParamsSsap_Object = MibTableColumn
tMacFilterParamsSsap = _TMacFilterParamsSsap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 4, 1, 17),
    _TMacFilterParamsSsap_Type()
)
tMacFilterParamsSsap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMacFilterParamsSsap.setStatus("current")


class _TMacFilterParamsSsapMask_Type(ServiceAccessPoint):
    """Custom type tMacFilterParamsSsapMask based on ServiceAccessPoint"""
    defaultValue = -1


_TMacFilterParamsSsapMask_Type.__name__ = "ServiceAccessPoint"
_TMacFilterParamsSsapMask_Object = MibTableColumn
tMacFilterParamsSsapMask = _TMacFilterParamsSsapMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 4, 1, 18),
    _TMacFilterParamsSsapMask_Type()
)
tMacFilterParamsSsapMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMacFilterParamsSsapMask.setStatus("current")


class _TMacFilterParamsSnapPid_Type(Integer32):
    """Custom type tMacFilterParamsSnapPid based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 65535),
    )


_TMacFilterParamsSnapPid_Type.__name__ = "Integer32"
_TMacFilterParamsSnapPid_Object = MibTableColumn
tMacFilterParamsSnapPid = _TMacFilterParamsSnapPid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 4, 1, 19),
    _TMacFilterParamsSnapPid_Type()
)
tMacFilterParamsSnapPid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMacFilterParamsSnapPid.setStatus("current")


class _TMacFilterParamsSnapOui_Type(Integer32):
    """Custom type tMacFilterParamsSnapOui based on Integer32"""
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
        *(("off", 1),
          ("zero", 2),
          ("nonZero", 3))
    )


_TMacFilterParamsSnapOui_Type.__name__ = "Integer32"
_TMacFilterParamsSnapOui_Object = MibTableColumn
tMacFilterParamsSnapOui = _TMacFilterParamsSnapOui_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 4, 1, 20),
    _TMacFilterParamsSnapOui_Type()
)
tMacFilterParamsSnapOui.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMacFilterParamsSnapOui.setStatus("current")
_TMacFilterParamsIngressHitCount_Type = Counter64
_TMacFilterParamsIngressHitCount_Object = MibTableColumn
tMacFilterParamsIngressHitCount = _TMacFilterParamsIngressHitCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 4, 1, 21),
    _TMacFilterParamsIngressHitCount_Type()
)
tMacFilterParamsIngressHitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMacFilterParamsIngressHitCount.setStatus("current")
_TMacFilterParamsEgressHitCount_Type = Counter64
_TMacFilterParamsEgressHitCount_Object = MibTableColumn
tMacFilterParamsEgressHitCount = _TMacFilterParamsEgressHitCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 4, 1, 22),
    _TMacFilterParamsEgressHitCount_Type()
)
tMacFilterParamsEgressHitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMacFilterParamsEgressHitCount.setStatus("current")
_TMacFilterParamsLogInstantiated_Type = TruthValue
_TMacFilterParamsLogInstantiated_Object = MibTableColumn
tMacFilterParamsLogInstantiated = _TMacFilterParamsLogInstantiated_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 4, 1, 23),
    _TMacFilterParamsLogInstantiated_Type()
)
tMacFilterParamsLogInstantiated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMacFilterParamsLogInstantiated.setStatus("current")
_TMacFilterParamsFwdSvcId_Type = TmnxServId
_TMacFilterParamsFwdSvcId_Object = MibTableColumn
tMacFilterParamsFwdSvcId = _TMacFilterParamsFwdSvcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 4, 1, 24),
    _TMacFilterParamsFwdSvcId_Type()
)
tMacFilterParamsFwdSvcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMacFilterParamsFwdSvcId.setStatus("current")


class _TMacFilterParamsFwdSapPortId_Type(TmnxPortID):
    """Custom type tMacFilterParamsFwdSapPortId based on TmnxPortID"""
    defaultValue = 0


_TMacFilterParamsFwdSapPortId_Type.__name__ = "TmnxPortID"
_TMacFilterParamsFwdSapPortId_Object = MibTableColumn
tMacFilterParamsFwdSapPortId = _TMacFilterParamsFwdSapPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 4, 1, 25),
    _TMacFilterParamsFwdSapPortId_Type()
)
tMacFilterParamsFwdSapPortId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMacFilterParamsFwdSapPortId.setStatus("current")


class _TMacFilterParamsFwdSapEncapVal_Type(TmnxEncapVal):
    """Custom type tMacFilterParamsFwdSapEncapVal based on TmnxEncapVal"""
    defaultValue = 0


_TMacFilterParamsFwdSapEncapVal_Type.__name__ = "TmnxEncapVal"
_TMacFilterParamsFwdSapEncapVal_Object = MibTableColumn
tMacFilterParamsFwdSapEncapVal = _TMacFilterParamsFwdSapEncapVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 4, 1, 26),
    _TMacFilterParamsFwdSapEncapVal_Type()
)
tMacFilterParamsFwdSapEncapVal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMacFilterParamsFwdSapEncapVal.setStatus("current")
_TMacFilterParamsFwdSdpBind_Type = SdpBindId
_TMacFilterParamsFwdSdpBind_Object = MibTableColumn
tMacFilterParamsFwdSdpBind = _TMacFilterParamsFwdSdpBind_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 4, 1, 27),
    _TMacFilterParamsFwdSdpBind_Type()
)
tMacFilterParamsFwdSdpBind.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMacFilterParamsFwdSdpBind.setStatus("current")


class _TMacFilterParamsTimeRangeName_Type(TNamedItemOrEmpty):
    """Custom type tMacFilterParamsTimeRangeName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TMacFilterParamsTimeRangeName_Type.__name__ = "TNamedItemOrEmpty"
_TMacFilterParamsTimeRangeName_Object = MibTableColumn
tMacFilterParamsTimeRangeName = _TMacFilterParamsTimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 4, 1, 28),
    _TMacFilterParamsTimeRangeName_Type()
)
tMacFilterParamsTimeRangeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMacFilterParamsTimeRangeName.setStatus("current")
_TMacFilterParamsTimeRangeState_Type = TTimeRangeState
_TMacFilterParamsTimeRangeState_Object = MibTableColumn
tMacFilterParamsTimeRangeState = _TMacFilterParamsTimeRangeState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 4, 1, 29),
    _TMacFilterParamsTimeRangeState_Type()
)
tMacFilterParamsTimeRangeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMacFilterParamsTimeRangeState.setStatus("current")


class _TMacFilterParamsRedirectURL_Type(TmnxHttpRedirectUrl):
    """Custom type tMacFilterParamsRedirectURL based on TmnxHttpRedirectUrl"""
    defaultHexValue = ""


_TMacFilterParamsRedirectURL_Type.__name__ = "TmnxHttpRedirectUrl"
_TMacFilterParamsRedirectURL_Object = MibTableColumn
tMacFilterParamsRedirectURL = _TMacFilterParamsRedirectURL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 4, 1, 30),
    _TMacFilterParamsRedirectURL_Type()
)
tMacFilterParamsRedirectURL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMacFilterParamsRedirectURL.setStatus("current")
_TMacFilterParamsIngrHitByteCount_Type = Counter64
_TMacFilterParamsIngrHitByteCount_Object = MibTableColumn
tMacFilterParamsIngrHitByteCount = _TMacFilterParamsIngrHitByteCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 4, 1, 31),
    _TMacFilterParamsIngrHitByteCount_Type()
)
tMacFilterParamsIngrHitByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMacFilterParamsIngrHitByteCount.setStatus("current")
_TMacFilterParamsEgrHitByteCount_Type = Counter64
_TMacFilterParamsEgrHitByteCount_Object = MibTableColumn
tMacFilterParamsEgrHitByteCount = _TMacFilterParamsEgrHitByteCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 4, 1, 32),
    _TMacFilterParamsEgrHitByteCount_Type()
)
tMacFilterParamsEgrHitByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMacFilterParamsEgrHitByteCount.setStatus("current")


class _TMacFilterParamsLowISID_Type(SvcISID):
    """Custom type tMacFilterParamsLowISID based on SvcISID"""
    defaultValue = -1


_TMacFilterParamsLowISID_Type.__name__ = "SvcISID"
_TMacFilterParamsLowISID_Object = MibTableColumn
tMacFilterParamsLowISID = _TMacFilterParamsLowISID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 4, 1, 33),
    _TMacFilterParamsLowISID_Type()
)
tMacFilterParamsLowISID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMacFilterParamsLowISID.setStatus("current")


class _TMacFilterParamsHighISID_Type(SvcISID):
    """Custom type tMacFilterParamsHighISID based on SvcISID"""
    defaultValue = -1


_TMacFilterParamsHighISID_Type.__name__ = "SvcISID"
_TMacFilterParamsHighISID_Object = MibTableColumn
tMacFilterParamsHighISID = _TMacFilterParamsHighISID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 4, 1, 34),
    _TMacFilterParamsHighISID_Type()
)
tMacFilterParamsHighISID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMacFilterParamsHighISID.setStatus("current")


class _TMacFilterParamsInnerTagValue_Type(QTagFullRangeOrNone):
    """Custom type tMacFilterParamsInnerTagValue based on QTagFullRangeOrNone"""
    defaultValue = -1


_TMacFilterParamsInnerTagValue_Type.__name__ = "QTagFullRangeOrNone"
_TMacFilterParamsInnerTagValue_Object = MibTableColumn
tMacFilterParamsInnerTagValue = _TMacFilterParamsInnerTagValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 4, 1, 35),
    _TMacFilterParamsInnerTagValue_Type()
)
tMacFilterParamsInnerTagValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMacFilterParamsInnerTagValue.setStatus("current")


class _TMacFilterParamsInnerTagMask_Type(QTagFullRange):
    """Custom type tMacFilterParamsInnerTagMask based on QTagFullRange"""
    defaultValue = 4095

    subtypeSpec = QTagFullRange.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_TMacFilterParamsInnerTagMask_Type.__name__ = "QTagFullRange"
_TMacFilterParamsInnerTagMask_Object = MibTableColumn
tMacFilterParamsInnerTagMask = _TMacFilterParamsInnerTagMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 4, 1, 36),
    _TMacFilterParamsInnerTagMask_Type()
)
tMacFilterParamsInnerTagMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMacFilterParamsInnerTagMask.setStatus("current")


class _TMacFilterParamsOuterTagValue_Type(QTagFullRangeOrNone):
    """Custom type tMacFilterParamsOuterTagValue based on QTagFullRangeOrNone"""
    defaultValue = -1


_TMacFilterParamsOuterTagValue_Type.__name__ = "QTagFullRangeOrNone"
_TMacFilterParamsOuterTagValue_Object = MibTableColumn
tMacFilterParamsOuterTagValue = _TMacFilterParamsOuterTagValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 4, 1, 37),
    _TMacFilterParamsOuterTagValue_Type()
)
tMacFilterParamsOuterTagValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMacFilterParamsOuterTagValue.setStatus("current")


class _TMacFilterParamsOuterTagMask_Type(QTagFullRange):
    """Custom type tMacFilterParamsOuterTagMask based on QTagFullRange"""
    defaultValue = 4095

    subtypeSpec = QTagFullRange.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_TMacFilterParamsOuterTagMask_Type.__name__ = "QTagFullRange"
_TMacFilterParamsOuterTagMask_Object = MibTableColumn
tMacFilterParamsOuterTagMask = _TMacFilterParamsOuterTagMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 4, 1, 38),
    _TMacFilterParamsOuterTagMask_Type()
)
tMacFilterParamsOuterTagMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMacFilterParamsOuterTagMask.setStatus("current")
_TFilterLogTable_Object = MibTable
tFilterLogTable = _TFilterLogTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 5)
)
if mibBuilder.loadTexts:
    tFilterLogTable.setStatus("current")
_TFilterLogEntry_Object = MibTableRow
tFilterLogEntry = _TFilterLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 5, 1)
)
tFilterLogEntry.setIndexNames(
    (0, "TIMETRA-FILTER-MIB", "tFilterLogId"),
)
if mibBuilder.loadTexts:
    tFilterLogEntry.setStatus("current")
_TFilterLogId_Type = TFilterLogId
_TFilterLogId_Object = MibTableColumn
tFilterLogId = _TFilterLogId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 5, 1, 1),
    _TFilterLogId_Type()
)
tFilterLogId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFilterLogId.setStatus("current")
_TFilterLogRowStatus_Type = RowStatus
_TFilterLogRowStatus_Object = MibTableColumn
tFilterLogRowStatus = _TFilterLogRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 5, 1, 2),
    _TFilterLogRowStatus_Type()
)
tFilterLogRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterLogRowStatus.setStatus("current")


class _TFilterLogDestination_Type(TFilterLogDestination):
    """Custom type tFilterLogDestination based on TFilterLogDestination"""
    defaultValue = 1


_TFilterLogDestination_Type.__name__ = "TFilterLogDestination"
_TFilterLogDestination_Object = MibTableColumn
tFilterLogDestination = _TFilterLogDestination_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 5, 1, 3),
    _TFilterLogDestination_Type()
)
tFilterLogDestination.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterLogDestination.setStatus("current")


class _TFilterLogDescription_Type(TItemDescription):
    """Custom type tFilterLogDescription based on TItemDescription"""
    defaultHexValue = ""


_TFilterLogDescription_Type.__name__ = "TItemDescription"
_TFilterLogDescription_Object = MibTableColumn
tFilterLogDescription = _TFilterLogDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 5, 1, 4),
    _TFilterLogDescription_Type()
)
tFilterLogDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterLogDescription.setStatus("current")


class _TFilterLogMaxNumEntries_Type(Unsigned32):
    """Custom type tFilterLogMaxNumEntries based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000),
    )


_TFilterLogMaxNumEntries_Type.__name__ = "Unsigned32"
_TFilterLogMaxNumEntries_Object = MibTableColumn
tFilterLogMaxNumEntries = _TFilterLogMaxNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 5, 1, 5),
    _TFilterLogMaxNumEntries_Type()
)
tFilterLogMaxNumEntries.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterLogMaxNumEntries.setStatus("current")


class _TFilterLogSysLogId_Type(Unsigned32):
    """Custom type tFilterLogSysLogId based on Unsigned32"""
    defaultValue = 0


_TFilterLogSysLogId_Type.__name__ = "Unsigned32"
_TFilterLogSysLogId_Object = MibTableColumn
tFilterLogSysLogId = _TFilterLogSysLogId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 5, 1, 6),
    _TFilterLogSysLogId_Type()
)
tFilterLogSysLogId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterLogSysLogId.setStatus("current")


class _TFilterLogFileId_Type(Unsigned32):
    """Custom type tFilterLogFileId based on Unsigned32"""
    defaultValue = 0


_TFilterLogFileId_Type.__name__ = "Unsigned32"
_TFilterLogFileId_Object = MibTableColumn
tFilterLogFileId = _TFilterLogFileId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 5, 1, 7),
    _TFilterLogFileId_Type()
)
tFilterLogFileId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterLogFileId.setStatus("current")


class _TFilterLogStopOnFull_Type(TruthValue):
    """Custom type tFilterLogStopOnFull based on TruthValue"""
    defaultValue = 2


_TFilterLogStopOnFull_Type.__name__ = "TruthValue"
_TFilterLogStopOnFull_Object = MibTableColumn
tFilterLogStopOnFull = _TFilterLogStopOnFull_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 5, 1, 8),
    _TFilterLogStopOnFull_Type()
)
tFilterLogStopOnFull.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterLogStopOnFull.setStatus("current")


class _TFilterLogEnabled_Type(TruthValue):
    """Custom type tFilterLogEnabled based on TruthValue"""
    defaultValue = 1


_TFilterLogEnabled_Type.__name__ = "TruthValue"
_TFilterLogEnabled_Object = MibTableColumn
tFilterLogEnabled = _TFilterLogEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 5, 1, 9),
    _TFilterLogEnabled_Type()
)
tFilterLogEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterLogEnabled.setStatus("current")


class _TFilterLogSummaryEnabled_Type(TruthValue):
    """Custom type tFilterLogSummaryEnabled based on TruthValue"""
    defaultValue = 2


_TFilterLogSummaryEnabled_Type.__name__ = "TruthValue"
_TFilterLogSummaryEnabled_Object = MibTableColumn
tFilterLogSummaryEnabled = _TFilterLogSummaryEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 5, 1, 10),
    _TFilterLogSummaryEnabled_Type()
)
tFilterLogSummaryEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterLogSummaryEnabled.setStatus("current")


class _TFilterLogSummaryCrit1_Type(TFilterLogSummaryCriterium):
    """Custom type tFilterLogSummaryCrit1 based on TFilterLogSummaryCriterium"""
    defaultValue = 0


_TFilterLogSummaryCrit1_Type.__name__ = "TFilterLogSummaryCriterium"
_TFilterLogSummaryCrit1_Object = MibTableColumn
tFilterLogSummaryCrit1 = _TFilterLogSummaryCrit1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 5, 1, 11),
    _TFilterLogSummaryCrit1_Type()
)
tFilterLogSummaryCrit1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterLogSummaryCrit1.setStatus("current")
_TFilterLogScalars_ObjectIdentity = ObjectIdentity
tFilterLogScalars = _TFilterLogScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 6)
)
_TFilterLogMaxInstances_Type = Gauge32
_TFilterLogMaxInstances_Object = MibScalar
tFilterLogMaxInstances = _TFilterLogMaxInstances_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 6, 1),
    _TFilterLogMaxInstances_Type()
)
tFilterLogMaxInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterLogMaxInstances.setStatus("current")
_TFilterLogInstances_Type = Gauge32
_TFilterLogInstances_Object = MibScalar
tFilterLogInstances = _TFilterLogInstances_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 6, 2),
    _TFilterLogInstances_Type()
)
tFilterLogInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterLogInstances.setStatus("current")
_TFilterLogBindings_Type = Gauge32
_TFilterLogBindings_Object = MibScalar
tFilterLogBindings = _TFilterLogBindings_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 6, 3),
    _TFilterLogBindings_Type()
)
tFilterLogBindings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterLogBindings.setStatus("current")
_TFilterNotificationObjects_ObjectIdentity = ObjectIdentity
tFilterNotificationObjects = _TFilterNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 8)
)


class _TFilterPBRDropReason_Type(Integer32):
    """Custom type tFilterPBRDropReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("invalidInterface", 0),
          ("interfaceDown", 1))
    )


_TFilterPBRDropReason_Type.__name__ = "Integer32"
_TFilterPBRDropReason_Object = MibScalar
tFilterPBRDropReason = _TFilterPBRDropReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 8, 1),
    _TFilterPBRDropReason_Type()
)
tFilterPBRDropReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tFilterPBRDropReason.setStatus("current")
_TFilterParmRow_Type = RowPointer
_TFilterParmRow_Object = MibScalar
tFilterParmRow = _TFilterParmRow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 8, 2),
    _TFilterParmRow_Type()
)
tFilterParmRow.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tFilterParmRow.setStatus("current")
_TFilterAlarmDescription_Type = DisplayString
_TFilterAlarmDescription_Object = MibScalar
tFilterAlarmDescription = _TFilterAlarmDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 8, 3),
    _TFilterAlarmDescription_Type()
)
tFilterAlarmDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tFilterAlarmDescription.setStatus("current")
_TFilterId_Type = TFilterID
_TFilterId_Object = MibScalar
tFilterId = _TFilterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 8, 4),
    _TFilterId_Type()
)
tFilterId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tFilterId.setStatus("current")
_TFilterType_Type = TFilterType
_TFilterType_Object = MibScalar
tFilterType = _TFilterType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 8, 5),
    _TFilterType_Type()
)
tFilterType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tFilterType.setStatus("current")
_TFilterSubInsSpaceOwner_Type = TFilterSubInsSpaceOwner
_TFilterSubInsSpaceOwner_Object = MibScalar
tFilterSubInsSpaceOwner = _TFilterSubInsSpaceOwner_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 8, 6),
    _TFilterSubInsSpaceOwner_Type()
)
tFilterSubInsSpaceOwner.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tFilterSubInsSpaceOwner.setStatus("current")
_TFilterThresholdReached_Type = Integer32
_TFilterThresholdReached_Object = MibScalar
tFilterThresholdReached = _TFilterThresholdReached_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 8, 7),
    _TFilterThresholdReached_Type()
)
tFilterThresholdReached.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tFilterThresholdReached.setStatus("current")


class _TFltrFlowSpecProblem_Type(Integer32):
    """Custom type tFltrFlowSpecProblem based on Integer32"""
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
        *(("nlriDecodeProblem", 0),
          ("maxNbrFlowSpecEntriesReached", 1),
          ("fltrResourceProblem", 2),
          ("other", 3))
    )


_TFltrFlowSpecProblem_Type.__name__ = "Integer32"
_TFltrFlowSpecProblem_Object = MibScalar
tFltrFlowSpecProblem = _TFltrFlowSpecProblem_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 8, 8),
    _TFltrFlowSpecProblem_Type()
)
tFltrFlowSpecProblem.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tFltrFlowSpecProblem.setStatus("current")
_TFltrFlowSpecProblemDescription_Type = DisplayString
_TFltrFlowSpecProblemDescription_Object = MibScalar
tFltrFlowSpecProblemDescription = _TFltrFlowSpecProblemDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 8, 9),
    _TFltrFlowSpecProblemDescription_Type()
)
tFltrFlowSpecProblemDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tFltrFlowSpecProblemDescription.setStatus("current")
_TFltrFLowSpecNLRI_Type = OctetString
_TFltrFLowSpecNLRI_Object = MibScalar
tFltrFLowSpecNLRI = _TFltrFLowSpecNLRI_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 8, 10),
    _TFltrFLowSpecNLRI_Type()
)
tFltrFLowSpecNLRI.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tFltrFLowSpecNLRI.setStatus("current")
_TFltrFlowSpecVrtrId_Type = Unsigned32
_TFltrFlowSpecVrtrId_Object = MibScalar
tFltrFlowSpecVrtrId = _TFltrFlowSpecVrtrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 8, 11),
    _TFltrFlowSpecVrtrId_Type()
)
tFltrFlowSpecVrtrId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tFltrFlowSpecVrtrId.setStatus("current")
_TFltrPrefixListType_Type = TFltrPrefixListType
_TFltrPrefixListType_Object = MibScalar
tFltrPrefixListType = _TFltrPrefixListType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 8, 12),
    _TFltrPrefixListType_Type()
)
tFltrPrefixListType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tFltrPrefixListType.setStatus("current")
_TFltrPrefixListName_Type = TNamedItem
_TFltrPrefixListName_Object = MibScalar
tFltrPrefixListName = _TFltrPrefixListName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 8, 13),
    _TFltrPrefixListName_Type()
)
tFltrPrefixListName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tFltrPrefixListName.setStatus("current")
_TFltrApplyPathSource_Type = TmnxFilterApplyPathSource
_TFltrApplyPathSource_Object = MibScalar
tFltrApplyPathSource = _TFltrApplyPathSource_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 8, 14),
    _TFltrApplyPathSource_Type()
)
tFltrApplyPathSource.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tFltrApplyPathSource.setStatus("current")
_TFltrApplyPathIndex_Type = Unsigned32
_TFltrApplyPathIndex_Object = MibScalar
tFltrApplyPathIndex = _TFltrApplyPathIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 8, 15),
    _TFltrApplyPathIndex_Type()
)
tFltrApplyPathIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tFltrApplyPathIndex.setStatus("current")
_TFltrNotifDescription_Type = DisplayString
_TFltrNotifDescription_Object = MibScalar
tFltrNotifDescription = _TFltrNotifDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 8, 16),
    _TFltrNotifDescription_Type()
)
tFltrNotifDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tFltrNotifDescription.setStatus("current")
_TFltrMdaId_Type = TmnxPortID
_TFltrMdaId_Object = MibScalar
tFltrMdaId = _TFltrMdaId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 8, 17),
    _TFltrMdaId_Type()
)
tFltrMdaId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tFltrMdaId.setStatus("current")
_TFilterTimeStampObjects_ObjectIdentity = ObjectIdentity
tFilterTimeStampObjects = _TFilterTimeStampObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 9)
)
_TFilterDomainLastChanged_Type = TimeStamp
_TFilterDomainLastChanged_Object = MibScalar
tFilterDomainLastChanged = _TFilterDomainLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 9, 1),
    _TFilterDomainLastChanged_Type()
)
tFilterDomainLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterDomainLastChanged.setStatus("current")
_TFilterRedirectPolicyTable_Object = MibTable
tFilterRedirectPolicyTable = _TFilterRedirectPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 10)
)
if mibBuilder.loadTexts:
    tFilterRedirectPolicyTable.setStatus("current")
_TFilterRedirectPolicyEntry_Object = MibTableRow
tFilterRedirectPolicyEntry = _TFilterRedirectPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 10, 1)
)
tFilterRedirectPolicyEntry.setIndexNames(
    (0, "TIMETRA-FILTER-MIB", "tFilterRedirectPolicy"),
)
if mibBuilder.loadTexts:
    tFilterRedirectPolicyEntry.setStatus("current")
_TFilterRedirectPolicy_Type = TNamedItem
_TFilterRedirectPolicy_Object = MibTableColumn
tFilterRedirectPolicy = _TFilterRedirectPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 10, 1, 1),
    _TFilterRedirectPolicy_Type()
)
tFilterRedirectPolicy.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFilterRedirectPolicy.setStatus("current")
_TFilterRPRowStatus_Type = RowStatus
_TFilterRPRowStatus_Object = MibTableColumn
tFilterRPRowStatus = _TFilterRPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 10, 1, 2),
    _TFilterRPRowStatus_Type()
)
tFilterRPRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterRPRowStatus.setStatus("current")


class _TFilterRPDescription_Type(TItemDescription):
    """Custom type tFilterRPDescription based on TItemDescription"""
    defaultHexValue = ""


_TFilterRPDescription_Type.__name__ = "TItemDescription"
_TFilterRPDescription_Object = MibTableColumn
tFilterRPDescription = _TFilterRPDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 10, 1, 3),
    _TFilterRPDescription_Type()
)
tFilterRPDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterRPDescription.setStatus("current")


class _TFilterRPAdminState_Type(TmnxAdminState):
    """Custom type tFilterRPAdminState based on TmnxAdminState"""
    defaultValue = 3


_TFilterRPAdminState_Type.__name__ = "TmnxAdminState"
_TFilterRPAdminState_Object = MibTableColumn
tFilterRPAdminState = _TFilterRPAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 10, 1, 4),
    _TFilterRPAdminState_Type()
)
tFilterRPAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterRPAdminState.setStatus("current")
_TFilterRPActiveDest_Type = IpAddress
_TFilterRPActiveDest_Object = MibTableColumn
tFilterRPActiveDest = _TFilterRPActiveDest_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 10, 1, 5),
    _TFilterRPActiveDest_Type()
)
tFilterRPActiveDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterRPActiveDest.setStatus("current")
_TFilterRedirectDestTable_Object = MibTable
tFilterRedirectDestTable = _TFilterRedirectDestTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 11)
)
if mibBuilder.loadTexts:
    tFilterRedirectDestTable.setStatus("current")
_TFilterRedirectDestEntry_Object = MibTableRow
tFilterRedirectDestEntry = _TFilterRedirectDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 11, 1)
)
tFilterRedirectDestEntry.setIndexNames(
    (0, "TIMETRA-FILTER-MIB", "tFilterRedirectPolicy"),
    (0, "TIMETRA-FILTER-MIB", "tFilterRedirectDest"),
)
if mibBuilder.loadTexts:
    tFilterRedirectDestEntry.setStatus("current")
_TFilterRedirectDest_Type = IpAddress
_TFilterRedirectDest_Object = MibTableColumn
tFilterRedirectDest = _TFilterRedirectDest_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 11, 1, 1),
    _TFilterRedirectDest_Type()
)
tFilterRedirectDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFilterRedirectDest.setStatus("current")
_TFilterRDRowStatus_Type = RowStatus
_TFilterRDRowStatus_Object = MibTableColumn
tFilterRDRowStatus = _TFilterRDRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 11, 1, 2),
    _TFilterRDRowStatus_Type()
)
tFilterRDRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterRDRowStatus.setStatus("current")


class _TFilterRDDescription_Type(TItemDescription):
    """Custom type tFilterRDDescription based on TItemDescription"""
    defaultHexValue = ""


_TFilterRDDescription_Type.__name__ = "TItemDescription"
_TFilterRDDescription_Object = MibTableColumn
tFilterRDDescription = _TFilterRDDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 11, 1, 3),
    _TFilterRDDescription_Type()
)
tFilterRDDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterRDDescription.setStatus("current")


class _TFilterRDAdminPriority_Type(Unsigned32):
    """Custom type tFilterRDAdminPriority based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TFilterRDAdminPriority_Type.__name__ = "Unsigned32"
_TFilterRDAdminPriority_Object = MibTableColumn
tFilterRDAdminPriority = _TFilterRDAdminPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 11, 1, 4),
    _TFilterRDAdminPriority_Type()
)
tFilterRDAdminPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterRDAdminPriority.setStatus("current")


class _TFilterRDOperPriority_Type(Unsigned32):
    """Custom type tFilterRDOperPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TFilterRDOperPriority_Type.__name__ = "Unsigned32"
_TFilterRDOperPriority_Object = MibTableColumn
tFilterRDOperPriority = _TFilterRDOperPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 11, 1, 5),
    _TFilterRDOperPriority_Type()
)
tFilterRDOperPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterRDOperPriority.setStatus("current")


class _TFilterRDAdminState_Type(TmnxAdminState):
    """Custom type tFilterRDAdminState based on TmnxAdminState"""
    defaultValue = 3


_TFilterRDAdminState_Type.__name__ = "TmnxAdminState"
_TFilterRDAdminState_Object = MibTableColumn
tFilterRDAdminState = _TFilterRDAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 11, 1, 6),
    _TFilterRDAdminState_Type()
)
tFilterRDAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterRDAdminState.setStatus("current")
_TFilterRDOperState_Type = TmnxOperState
_TFilterRDOperState_Object = MibTableColumn
tFilterRDOperState = _TFilterRDOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 11, 1, 7),
    _TFilterRDOperState_Type()
)
tFilterRDOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterRDOperState.setStatus("current")
_TFilterRedirectSNMPTestTable_Object = MibTable
tFilterRedirectSNMPTestTable = _TFilterRedirectSNMPTestTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 12)
)
if mibBuilder.loadTexts:
    tFilterRedirectSNMPTestTable.setStatus("current")
_TFilterRedirectSNMPTestEntry_Object = MibTableRow
tFilterRedirectSNMPTestEntry = _TFilterRedirectSNMPTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 12, 1)
)
tFilterRedirectSNMPTestEntry.setIndexNames(
    (0, "TIMETRA-FILTER-MIB", "tFilterRedirectPolicy"),
    (0, "TIMETRA-FILTER-MIB", "tFilterRedirectDest"),
    (0, "TIMETRA-FILTER-MIB", "tFilterRedirectSNMPTest"),
)
if mibBuilder.loadTexts:
    tFilterRedirectSNMPTestEntry.setStatus("current")
_TFilterRedirectSNMPTest_Type = TNamedItem
_TFilterRedirectSNMPTest_Object = MibTableColumn
tFilterRedirectSNMPTest = _TFilterRedirectSNMPTest_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 12, 1, 1),
    _TFilterRedirectSNMPTest_Type()
)
tFilterRedirectSNMPTest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFilterRedirectSNMPTest.setStatus("current")
_TFilterRSTRowStatus_Type = RowStatus
_TFilterRSTRowStatus_Object = MibTableColumn
tFilterRSTRowStatus = _TFilterRSTRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 12, 1, 2),
    _TFilterRSTRowStatus_Type()
)
tFilterRSTRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterRSTRowStatus.setStatus("current")
_TFilterRSTOID_Type = ObjectIdentifier
_TFilterRSTOID_Object = MibTableColumn
tFilterRSTOID = _TFilterRSTOID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 12, 1, 3),
    _TFilterRSTOID_Type()
)
tFilterRSTOID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterRSTOID.setStatus("current")


class _TFilterRSTCommunity_Type(DisplayString):
    """Custom type tFilterRSTCommunity based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TFilterRSTCommunity_Type.__name__ = "DisplayString"
_TFilterRSTCommunity_Object = MibTableColumn
tFilterRSTCommunity = _TFilterRSTCommunity_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 12, 1, 4),
    _TFilterRSTCommunity_Type()
)
tFilterRSTCommunity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterRSTCommunity.setStatus("current")


class _TFilterRSTSNMPVersion_Type(Integer32):
    """Custom type tFilterRSTSNMPVersion based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("snmpv1", 1),
          ("snmpv2c", 2),
          ("snmpv3", 3))
    )


_TFilterRSTSNMPVersion_Type.__name__ = "Integer32"
_TFilterRSTSNMPVersion_Object = MibTableColumn
tFilterRSTSNMPVersion = _TFilterRSTSNMPVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 12, 1, 5),
    _TFilterRSTSNMPVersion_Type()
)
tFilterRSTSNMPVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterRSTSNMPVersion.setStatus("current")


class _TFilterRSTInterval_Type(Unsigned32):
    """Custom type tFilterRSTInterval based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_TFilterRSTInterval_Type.__name__ = "Unsigned32"
_TFilterRSTInterval_Object = MibTableColumn
tFilterRSTInterval = _TFilterRSTInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 12, 1, 6),
    _TFilterRSTInterval_Type()
)
tFilterRSTInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterRSTInterval.setStatus("current")
if mibBuilder.loadTexts:
    tFilterRSTInterval.setUnits("seconds")


class _TFilterRSTTimeout_Type(Unsigned32):
    """Custom type tFilterRSTTimeout based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_TFilterRSTTimeout_Type.__name__ = "Unsigned32"
_TFilterRSTTimeout_Object = MibTableColumn
tFilterRSTTimeout = _TFilterRSTTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 12, 1, 7),
    _TFilterRSTTimeout_Type()
)
tFilterRSTTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterRSTTimeout.setStatus("current")
if mibBuilder.loadTexts:
    tFilterRSTTimeout.setUnits("seconds")


class _TFilterRSTDropCount_Type(Unsigned32):
    """Custom type tFilterRSTDropCount based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_TFilterRSTDropCount_Type.__name__ = "Unsigned32"
_TFilterRSTDropCount_Object = MibTableColumn
tFilterRSTDropCount = _TFilterRSTDropCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 12, 1, 8),
    _TFilterRSTDropCount_Type()
)
tFilterRSTDropCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterRSTDropCount.setStatus("current")


class _TFilterRSTHoldDown_Type(Unsigned32):
    """Custom type tFilterRSTHoldDown based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_TFilterRSTHoldDown_Type.__name__ = "Unsigned32"
_TFilterRSTHoldDown_Object = MibTableColumn
tFilterRSTHoldDown = _TFilterRSTHoldDown_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 12, 1, 9),
    _TFilterRSTHoldDown_Type()
)
tFilterRSTHoldDown.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterRSTHoldDown.setStatus("current")
if mibBuilder.loadTexts:
    tFilterRSTHoldDown.setUnits("seconds")


class _TFilterRSTHoldDownRemain_Type(Unsigned32):
    """Custom type tFilterRSTHoldDownRemain based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_TFilterRSTHoldDownRemain_Type.__name__ = "Unsigned32"
_TFilterRSTHoldDownRemain_Object = MibTableColumn
tFilterRSTHoldDownRemain = _TFilterRSTHoldDownRemain_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 12, 1, 10),
    _TFilterRSTHoldDownRemain_Type()
)
tFilterRSTHoldDownRemain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterRSTHoldDownRemain.setStatus("current")
if mibBuilder.loadTexts:
    tFilterRSTHoldDownRemain.setUnits("seconds")
_TFilterRSTLastActionTime_Type = TimeStamp
_TFilterRSTLastActionTime_Object = MibTableColumn
tFilterRSTLastActionTime = _TFilterRSTLastActionTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 12, 1, 11),
    _TFilterRSTLastActionTime_Type()
)
tFilterRSTLastActionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterRSTLastActionTime.setStatus("current")
_TFilterRSTLastOID_Type = ObjectIdentifier
_TFilterRSTLastOID_Object = MibTableColumn
tFilterRSTLastOID = _TFilterRSTLastOID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 12, 1, 12),
    _TFilterRSTLastOID_Type()
)
tFilterRSTLastOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterRSTLastOID.setStatus("current")


class _TFilterRSTLastType_Type(Integer32):
    """Custom type tFilterRSTLastType based on Integer32"""
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
          ("counter32", 1),
          ("unsigned32", 2),
          ("timeTicks", 3),
          ("integer32", 4),
          ("ipAddress", 5),
          ("octetString", 6),
          ("objectId", 7),
          ("counter64", 8),
          ("opaque", 9))
    )


_TFilterRSTLastType_Type.__name__ = "Integer32"
_TFilterRSTLastType_Object = MibTableColumn
tFilterRSTLastType = _TFilterRSTLastType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 12, 1, 13),
    _TFilterRSTLastType_Type()
)
tFilterRSTLastType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterRSTLastType.setStatus("current")
_TFilterRSTLastCounter32Val_Type = Counter32
_TFilterRSTLastCounter32Val_Object = MibTableColumn
tFilterRSTLastCounter32Val = _TFilterRSTLastCounter32Val_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 12, 1, 14),
    _TFilterRSTLastCounter32Val_Type()
)
tFilterRSTLastCounter32Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterRSTLastCounter32Val.setStatus("current")
_TFilterRSTLastUnsigned32Val_Type = Unsigned32
_TFilterRSTLastUnsigned32Val_Object = MibTableColumn
tFilterRSTLastUnsigned32Val = _TFilterRSTLastUnsigned32Val_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 12, 1, 15),
    _TFilterRSTLastUnsigned32Val_Type()
)
tFilterRSTLastUnsigned32Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterRSTLastUnsigned32Val.setStatus("current")
_TFilterRSTLastTimeTicksVal_Type = TimeTicks
_TFilterRSTLastTimeTicksVal_Object = MibTableColumn
tFilterRSTLastTimeTicksVal = _TFilterRSTLastTimeTicksVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 12, 1, 16),
    _TFilterRSTLastTimeTicksVal_Type()
)
tFilterRSTLastTimeTicksVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterRSTLastTimeTicksVal.setStatus("current")
_TFilterRSTLastInt32Val_Type = Integer32
_TFilterRSTLastInt32Val_Object = MibTableColumn
tFilterRSTLastInt32Val = _TFilterRSTLastInt32Val_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 12, 1, 17),
    _TFilterRSTLastInt32Val_Type()
)
tFilterRSTLastInt32Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterRSTLastInt32Val.setStatus("current")
_TFilterRSTLastOctetStringVal_Type = OctetString
_TFilterRSTLastOctetStringVal_Object = MibTableColumn
tFilterRSTLastOctetStringVal = _TFilterRSTLastOctetStringVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 12, 1, 18),
    _TFilterRSTLastOctetStringVal_Type()
)
tFilterRSTLastOctetStringVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterRSTLastOctetStringVal.setStatus("current")
_TFilterRSTLastIpAddressVal_Type = IpAddress
_TFilterRSTLastIpAddressVal_Object = MibTableColumn
tFilterRSTLastIpAddressVal = _TFilterRSTLastIpAddressVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 12, 1, 19),
    _TFilterRSTLastIpAddressVal_Type()
)
tFilterRSTLastIpAddressVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterRSTLastIpAddressVal.setStatus("current")
_TFilterRSTLastOidVal_Type = ObjectIdentifier
_TFilterRSTLastOidVal_Object = MibTableColumn
tFilterRSTLastOidVal = _TFilterRSTLastOidVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 12, 1, 20),
    _TFilterRSTLastOidVal_Type()
)
tFilterRSTLastOidVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterRSTLastOidVal.setStatus("current")
_TFilterRSTLastCounter64Val_Type = Counter64
_TFilterRSTLastCounter64Val_Object = MibTableColumn
tFilterRSTLastCounter64Val = _TFilterRSTLastCounter64Val_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 12, 1, 21),
    _TFilterRSTLastCounter64Val_Type()
)
tFilterRSTLastCounter64Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterRSTLastCounter64Val.setStatus("current")
_TFilterRSTLastOpaqueVal_Type = Opaque
_TFilterRSTLastOpaqueVal_Object = MibTableColumn
tFilterRSTLastOpaqueVal = _TFilterRSTLastOpaqueVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 12, 1, 22),
    _TFilterRSTLastOpaqueVal_Type()
)
tFilterRSTLastOpaqueVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterRSTLastOpaqueVal.setStatus("current")


class _TFilterRSTLastAction_Type(Integer32):
    """Custom type tFilterRSTLastAction based on Integer32"""
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
          ("none", 3))
    )


_TFilterRSTLastAction_Type.__name__ = "Integer32"
_TFilterRSTLastAction_Object = MibTableColumn
tFilterRSTLastAction = _TFilterRSTLastAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 12, 1, 23),
    _TFilterRSTLastAction_Type()
)
tFilterRSTLastAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterRSTLastAction.setStatus("current")


class _TFilterRSTLastPrioChange_Type(Integer32):
    """Custom type tFilterRSTLastPrioChange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-255, 255),
    )


_TFilterRSTLastPrioChange_Type.__name__ = "Integer32"
_TFilterRSTLastPrioChange_Object = MibTableColumn
tFilterRSTLastPrioChange = _TFilterRSTLastPrioChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 12, 1, 24),
    _TFilterRSTLastPrioChange_Type()
)
tFilterRSTLastPrioChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterRSTLastPrioChange.setStatus("current")


class _TFilterRSTNextRespIndex_Type(Integer32):
    """Custom type tFilterRSTNextRespIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 2147483647),
    )


_TFilterRSTNextRespIndex_Type.__name__ = "Integer32"
_TFilterRSTNextRespIndex_Object = MibTableColumn
tFilterRSTNextRespIndex = _TFilterRSTNextRespIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 12, 1, 25),
    _TFilterRSTNextRespIndex_Type()
)
tFilterRSTNextRespIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterRSTNextRespIndex.setStatus("current")
_TFilterRedirectSNMPRespTable_Object = MibTable
tFilterRedirectSNMPRespTable = _TFilterRedirectSNMPRespTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 13)
)
if mibBuilder.loadTexts:
    tFilterRedirectSNMPRespTable.setStatus("current")
_TFilterRedirectSNMPRespEntry_Object = MibTableRow
tFilterRedirectSNMPRespEntry = _TFilterRedirectSNMPRespEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 13, 1)
)
tFilterRedirectSNMPRespEntry.setIndexNames(
    (0, "TIMETRA-FILTER-MIB", "tFilterRedirectPolicy"),
    (0, "TIMETRA-FILTER-MIB", "tFilterRedirectDest"),
    (0, "TIMETRA-FILTER-MIB", "tFilterRedirectSNMPTest"),
    (0, "TIMETRA-FILTER-MIB", "tFilterRSTRespId"),
)
if mibBuilder.loadTexts:
    tFilterRedirectSNMPRespEntry.setStatus("current")


class _TFilterRSTRespId_Type(Integer32):
    """Custom type tFilterRSTRespId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_TFilterRSTRespId_Type.__name__ = "Integer32"
_TFilterRSTRespId_Object = MibTableColumn
tFilterRSTRespId = _TFilterRSTRespId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 13, 1, 1),
    _TFilterRSTRespId_Type()
)
tFilterRSTRespId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFilterRSTRespId.setStatus("current")
_TFilterRSTRespRowStatus_Type = RowStatus
_TFilterRSTRespRowStatus_Object = MibTableColumn
tFilterRSTRespRowStatus = _TFilterRSTRespRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 13, 1, 2),
    _TFilterRSTRespRowStatus_Type()
)
tFilterRSTRespRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterRSTRespRowStatus.setStatus("current")


class _TFilterRSTRespAction_Type(Integer32):
    """Custom type tFilterRSTRespAction based on Integer32"""
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
        *(("increase", 1),
          ("decrease", 2),
          ("disable", 3))
    )


_TFilterRSTRespAction_Type.__name__ = "Integer32"
_TFilterRSTRespAction_Object = MibTableColumn
tFilterRSTRespAction = _TFilterRSTRespAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 13, 1, 3),
    _TFilterRSTRespAction_Type()
)
tFilterRSTRespAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterRSTRespAction.setStatus("current")


class _TFilterRSTRespPrioChange_Type(Unsigned32):
    """Custom type tFilterRSTRespPrioChange based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TFilterRSTRespPrioChange_Type.__name__ = "Unsigned32"
_TFilterRSTRespPrioChange_Object = MibTableColumn
tFilterRSTRespPrioChange = _TFilterRSTRespPrioChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 13, 1, 4),
    _TFilterRSTRespPrioChange_Type()
)
tFilterRSTRespPrioChange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterRSTRespPrioChange.setStatus("current")
_TFilterRSTRespOID_Type = ObjectIdentifier
_TFilterRSTRespOID_Object = MibTableColumn
tFilterRSTRespOID = _TFilterRSTRespOID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 13, 1, 5),
    _TFilterRSTRespOID_Type()
)
tFilterRSTRespOID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterRSTRespOID.setStatus("current")


class _TFilterRSTRespType_Type(Integer32):
    """Custom type tFilterRSTRespType based on Integer32"""
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
        *(("counter32", 1),
          ("unsigned32", 2),
          ("timeTicks", 3),
          ("integer32", 4),
          ("ipAddress", 5),
          ("octetString", 6),
          ("objectId", 7),
          ("counter64", 8),
          ("opaque", 9))
    )


_TFilterRSTRespType_Type.__name__ = "Integer32"
_TFilterRSTRespType_Object = MibTableColumn
tFilterRSTRespType = _TFilterRSTRespType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 13, 1, 6),
    _TFilterRSTRespType_Type()
)
tFilterRSTRespType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterRSTRespType.setStatus("current")
_TFilterRSTCounter32Val_Type = Counter32
_TFilterRSTCounter32Val_Object = MibTableColumn
tFilterRSTCounter32Val = _TFilterRSTCounter32Val_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 13, 1, 7),
    _TFilterRSTCounter32Val_Type()
)
tFilterRSTCounter32Val.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterRSTCounter32Val.setStatus("current")
_TFilterRSTUnsigned32Val_Type = Unsigned32
_TFilterRSTUnsigned32Val_Object = MibTableColumn
tFilterRSTUnsigned32Val = _TFilterRSTUnsigned32Val_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 13, 1, 8),
    _TFilterRSTUnsigned32Val_Type()
)
tFilterRSTUnsigned32Val.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterRSTUnsigned32Val.setStatus("current")
_TFilterRSTTimeTicksVal_Type = TimeTicks
_TFilterRSTTimeTicksVal_Object = MibTableColumn
tFilterRSTTimeTicksVal = _TFilterRSTTimeTicksVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 13, 1, 9),
    _TFilterRSTTimeTicksVal_Type()
)
tFilterRSTTimeTicksVal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterRSTTimeTicksVal.setStatus("current")
_TFilterRSTInt32Val_Type = Integer32
_TFilterRSTInt32Val_Object = MibTableColumn
tFilterRSTInt32Val = _TFilterRSTInt32Val_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 13, 1, 10),
    _TFilterRSTInt32Val_Type()
)
tFilterRSTInt32Val.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterRSTInt32Val.setStatus("current")
_TFilterRSTOctetStringVal_Type = OctetString
_TFilterRSTOctetStringVal_Object = MibTableColumn
tFilterRSTOctetStringVal = _TFilterRSTOctetStringVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 13, 1, 11),
    _TFilterRSTOctetStringVal_Type()
)
tFilterRSTOctetStringVal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterRSTOctetStringVal.setStatus("current")
_TFilterRSTIpAddressVal_Type = IpAddress
_TFilterRSTIpAddressVal_Object = MibTableColumn
tFilterRSTIpAddressVal = _TFilterRSTIpAddressVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 13, 1, 12),
    _TFilterRSTIpAddressVal_Type()
)
tFilterRSTIpAddressVal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterRSTIpAddressVal.setStatus("current")
_TFilterRSTOidVal_Type = ObjectIdentifier
_TFilterRSTOidVal_Object = MibTableColumn
tFilterRSTOidVal = _TFilterRSTOidVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 13, 1, 13),
    _TFilterRSTOidVal_Type()
)
tFilterRSTOidVal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterRSTOidVal.setStatus("current")
_TFilterRSTCounter64Val_Type = Counter64
_TFilterRSTCounter64Val_Object = MibTableColumn
tFilterRSTCounter64Val = _TFilterRSTCounter64Val_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 13, 1, 14),
    _TFilterRSTCounter64Val_Type()
)
tFilterRSTCounter64Val.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterRSTCounter64Val.setStatus("current")
_TFilterRSTOpaqueVal_Type = Opaque
_TFilterRSTOpaqueVal_Object = MibTableColumn
tFilterRSTOpaqueVal = _TFilterRSTOpaqueVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 13, 1, 15),
    _TFilterRSTOpaqueVal_Type()
)
tFilterRSTOpaqueVal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterRSTOpaqueVal.setStatus("current")
_TFilterRedirectURLTestTable_Object = MibTable
tFilterRedirectURLTestTable = _TFilterRedirectURLTestTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 14)
)
if mibBuilder.loadTexts:
    tFilterRedirectURLTestTable.setStatus("current")
_TFilterRedirectURLTestEntry_Object = MibTableRow
tFilterRedirectURLTestEntry = _TFilterRedirectURLTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 14, 1)
)
tFilterRedirectURLTestEntry.setIndexNames(
    (0, "TIMETRA-FILTER-MIB", "tFilterRedirectPolicy"),
    (0, "TIMETRA-FILTER-MIB", "tFilterRedirectDest"),
    (0, "TIMETRA-FILTER-MIB", "tFilterRedirectURLTest"),
)
if mibBuilder.loadTexts:
    tFilterRedirectURLTestEntry.setStatus("current")
_TFilterRedirectURLTest_Type = TNamedItem
_TFilterRedirectURLTest_Object = MibTableColumn
tFilterRedirectURLTest = _TFilterRedirectURLTest_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 14, 1, 1),
    _TFilterRedirectURLTest_Type()
)
tFilterRedirectURLTest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFilterRedirectURLTest.setStatus("current")
_TFilterRUTRowStatus_Type = RowStatus
_TFilterRUTRowStatus_Object = MibTableColumn
tFilterRUTRowStatus = _TFilterRUTRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 14, 1, 2),
    _TFilterRUTRowStatus_Type()
)
tFilterRUTRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterRUTRowStatus.setStatus("current")


class _TFilterRUTURL_Type(DisplayString):
    """Custom type tFilterRUTURL based on DisplayString"""
    defaultHexValue = ""


_TFilterRUTURL_Type.__name__ = "DisplayString"
_TFilterRUTURL_Object = MibTableColumn
tFilterRUTURL = _TFilterRUTURL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 14, 1, 3),
    _TFilterRUTURL_Type()
)
tFilterRUTURL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterRUTURL.setStatus("current")


class _TFilterRUTHTTPVersion_Type(DisplayString):
    """Custom type tFilterRUTHTTPVersion based on DisplayString"""
    defaultHexValue = ""


_TFilterRUTHTTPVersion_Type.__name__ = "DisplayString"
_TFilterRUTHTTPVersion_Object = MibTableColumn
tFilterRUTHTTPVersion = _TFilterRUTHTTPVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 14, 1, 4),
    _TFilterRUTHTTPVersion_Type()
)
tFilterRUTHTTPVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterRUTHTTPVersion.setStatus("current")


class _TFilterRUTInterval_Type(Unsigned32):
    """Custom type tFilterRUTInterval based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_TFilterRUTInterval_Type.__name__ = "Unsigned32"
_TFilterRUTInterval_Object = MibTableColumn
tFilterRUTInterval = _TFilterRUTInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 14, 1, 5),
    _TFilterRUTInterval_Type()
)
tFilterRUTInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterRUTInterval.setStatus("current")
if mibBuilder.loadTexts:
    tFilterRUTInterval.setUnits("seconds")


class _TFilterRUTTimeout_Type(Unsigned32):
    """Custom type tFilterRUTTimeout based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_TFilterRUTTimeout_Type.__name__ = "Unsigned32"
_TFilterRUTTimeout_Object = MibTableColumn
tFilterRUTTimeout = _TFilterRUTTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 14, 1, 6),
    _TFilterRUTTimeout_Type()
)
tFilterRUTTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterRUTTimeout.setStatus("current")
if mibBuilder.loadTexts:
    tFilterRUTTimeout.setUnits("seconds")


class _TFilterRUTDropCount_Type(Unsigned32):
    """Custom type tFilterRUTDropCount based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_TFilterRUTDropCount_Type.__name__ = "Unsigned32"
_TFilterRUTDropCount_Object = MibTableColumn
tFilterRUTDropCount = _TFilterRUTDropCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 14, 1, 7),
    _TFilterRUTDropCount_Type()
)
tFilterRUTDropCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterRUTDropCount.setStatus("current")


class _TFilterRUTHoldDown_Type(Unsigned32):
    """Custom type tFilterRUTHoldDown based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_TFilterRUTHoldDown_Type.__name__ = "Unsigned32"
_TFilterRUTHoldDown_Object = MibTableColumn
tFilterRUTHoldDown = _TFilterRUTHoldDown_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 14, 1, 8),
    _TFilterRUTHoldDown_Type()
)
tFilterRUTHoldDown.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterRUTHoldDown.setStatus("current")
if mibBuilder.loadTexts:
    tFilterRUTHoldDown.setUnits("seconds")


class _TFilterRUTHoldDownRemain_Type(Unsigned32):
    """Custom type tFilterRUTHoldDownRemain based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_TFilterRUTHoldDownRemain_Type.__name__ = "Unsigned32"
_TFilterRUTHoldDownRemain_Object = MibTableColumn
tFilterRUTHoldDownRemain = _TFilterRUTHoldDownRemain_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 14, 1, 9),
    _TFilterRUTHoldDownRemain_Type()
)
tFilterRUTHoldDownRemain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterRUTHoldDownRemain.setStatus("current")
if mibBuilder.loadTexts:
    tFilterRUTHoldDownRemain.setUnits("seconds")
_TFilterRUTLastActionTime_Type = TimeStamp
_TFilterRUTLastActionTime_Object = MibTableColumn
tFilterRUTLastActionTime = _TFilterRUTLastActionTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 14, 1, 10),
    _TFilterRUTLastActionTime_Type()
)
tFilterRUTLastActionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterRUTLastActionTime.setStatus("current")
_TFilterRUTLastRetCode_Type = Unsigned32
_TFilterRUTLastRetCode_Object = MibTableColumn
tFilterRUTLastRetCode = _TFilterRUTLastRetCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 14, 1, 11),
    _TFilterRUTLastRetCode_Type()
)
tFilterRUTLastRetCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterRUTLastRetCode.setStatus("current")


class _TFilterRUTLastAction_Type(Integer32):
    """Custom type tFilterRUTLastAction based on Integer32"""
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
          ("none", 3))
    )


_TFilterRUTLastAction_Type.__name__ = "Integer32"
_TFilterRUTLastAction_Object = MibTableColumn
tFilterRUTLastAction = _TFilterRUTLastAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 14, 1, 12),
    _TFilterRUTLastAction_Type()
)
tFilterRUTLastAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterRUTLastAction.setStatus("current")


class _TFilterRUTLastPrioChange_Type(Integer32):
    """Custom type tFilterRUTLastPrioChange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-255, 255),
    )


_TFilterRUTLastPrioChange_Type.__name__ = "Integer32"
_TFilterRUTLastPrioChange_Object = MibTableColumn
tFilterRUTLastPrioChange = _TFilterRUTLastPrioChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 14, 1, 13),
    _TFilterRUTLastPrioChange_Type()
)
tFilterRUTLastPrioChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterRUTLastPrioChange.setStatus("current")
_TFilterRedirectURLRespTable_Object = MibTable
tFilterRedirectURLRespTable = _TFilterRedirectURLRespTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 15)
)
if mibBuilder.loadTexts:
    tFilterRedirectURLRespTable.setStatus("current")
_TFilterRedirectURLRespEntry_Object = MibTableRow
tFilterRedirectURLRespEntry = _TFilterRedirectURLRespEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 15, 1)
)
tFilterRedirectURLRespEntry.setIndexNames(
    (0, "TIMETRA-FILTER-MIB", "tFilterRedirectPolicy"),
    (0, "TIMETRA-FILTER-MIB", "tFilterRedirectDest"),
    (0, "TIMETRA-FILTER-MIB", "tFilterRedirectURLTest"),
    (0, "TIMETRA-FILTER-MIB", "tFilterRedirectURLLowRespCode"),
    (0, "TIMETRA-FILTER-MIB", "tFilterRedirectURLHighRespCode"),
)
if mibBuilder.loadTexts:
    tFilterRedirectURLRespEntry.setStatus("current")
_TFilterRedirectURLLowRespCode_Type = Unsigned32
_TFilterRedirectURLLowRespCode_Object = MibTableColumn
tFilterRedirectURLLowRespCode = _TFilterRedirectURLLowRespCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 15, 1, 1),
    _TFilterRedirectURLLowRespCode_Type()
)
tFilterRedirectURLLowRespCode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFilterRedirectURLLowRespCode.setStatus("current")
_TFilterRedirectURLHighRespCode_Type = Unsigned32
_TFilterRedirectURLHighRespCode_Object = MibTableColumn
tFilterRedirectURLHighRespCode = _TFilterRedirectURLHighRespCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 15, 1, 2),
    _TFilterRedirectURLHighRespCode_Type()
)
tFilterRedirectURLHighRespCode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFilterRedirectURLHighRespCode.setStatus("current")
_TFilterRUTRespRowStatus_Type = RowStatus
_TFilterRUTRespRowStatus_Object = MibTableColumn
tFilterRUTRespRowStatus = _TFilterRUTRespRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 15, 1, 3),
    _TFilterRUTRespRowStatus_Type()
)
tFilterRUTRespRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterRUTRespRowStatus.setStatus("current")


class _TFilterRUTRespAction_Type(Integer32):
    """Custom type tFilterRUTRespAction based on Integer32"""
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
        *(("increase", 1),
          ("decrease", 2),
          ("disable", 3))
    )


_TFilterRUTRespAction_Type.__name__ = "Integer32"
_TFilterRUTRespAction_Object = MibTableColumn
tFilterRUTRespAction = _TFilterRUTRespAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 15, 1, 4),
    _TFilterRUTRespAction_Type()
)
tFilterRUTRespAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterRUTRespAction.setStatus("current")


class _TFilterRUTRespPrioChange_Type(Unsigned32):
    """Custom type tFilterRUTRespPrioChange based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TFilterRUTRespPrioChange_Type.__name__ = "Unsigned32"
_TFilterRUTRespPrioChange_Object = MibTableColumn
tFilterRUTRespPrioChange = _TFilterRUTRespPrioChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 15, 1, 5),
    _TFilterRUTRespPrioChange_Type()
)
tFilterRUTRespPrioChange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterRUTRespPrioChange.setStatus("current")
_TFilterRedirectPingTestTable_Object = MibTable
tFilterRedirectPingTestTable = _TFilterRedirectPingTestTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 16)
)
if mibBuilder.loadTexts:
    tFilterRedirectPingTestTable.setStatus("current")
_TFilterRedirectPingTestEntry_Object = MibTableRow
tFilterRedirectPingTestEntry = _TFilterRedirectPingTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 16, 1)
)
tFilterRedirectPingTestEntry.setIndexNames(
    (0, "TIMETRA-FILTER-MIB", "tFilterRedirectPolicy"),
    (0, "TIMETRA-FILTER-MIB", "tFilterRedirectDest"),
)
if mibBuilder.loadTexts:
    tFilterRedirectPingTestEntry.setStatus("current")
_TFilterRPTRowStatus_Type = RowStatus
_TFilterRPTRowStatus_Object = MibTableColumn
tFilterRPTRowStatus = _TFilterRPTRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 16, 1, 1),
    _TFilterRPTRowStatus_Type()
)
tFilterRPTRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterRPTRowStatus.setStatus("current")


class _TFilterRPTInterval_Type(Unsigned32):
    """Custom type tFilterRPTInterval based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_TFilterRPTInterval_Type.__name__ = "Unsigned32"
_TFilterRPTInterval_Object = MibTableColumn
tFilterRPTInterval = _TFilterRPTInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 16, 1, 2),
    _TFilterRPTInterval_Type()
)
tFilterRPTInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterRPTInterval.setStatus("current")
if mibBuilder.loadTexts:
    tFilterRPTInterval.setUnits("seconds")


class _TFilterRPTTimeout_Type(Unsigned32):
    """Custom type tFilterRPTTimeout based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_TFilterRPTTimeout_Type.__name__ = "Unsigned32"
_TFilterRPTTimeout_Object = MibTableColumn
tFilterRPTTimeout = _TFilterRPTTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 16, 1, 3),
    _TFilterRPTTimeout_Type()
)
tFilterRPTTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterRPTTimeout.setStatus("current")
if mibBuilder.loadTexts:
    tFilterRPTTimeout.setUnits("seconds")


class _TFilterRPTDropCount_Type(Unsigned32):
    """Custom type tFilterRPTDropCount based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_TFilterRPTDropCount_Type.__name__ = "Unsigned32"
_TFilterRPTDropCount_Object = MibTableColumn
tFilterRPTDropCount = _TFilterRPTDropCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 16, 1, 4),
    _TFilterRPTDropCount_Type()
)
tFilterRPTDropCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterRPTDropCount.setStatus("current")


class _TFilterRPTHoldDown_Type(Unsigned32):
    """Custom type tFilterRPTHoldDown based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_TFilterRPTHoldDown_Type.__name__ = "Unsigned32"
_TFilterRPTHoldDown_Object = MibTableColumn
tFilterRPTHoldDown = _TFilterRPTHoldDown_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 16, 1, 5),
    _TFilterRPTHoldDown_Type()
)
tFilterRPTHoldDown.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterRPTHoldDown.setStatus("current")
if mibBuilder.loadTexts:
    tFilterRPTHoldDown.setUnits("seconds")


class _TFilterRPTHoldDownRemain_Type(Unsigned32):
    """Custom type tFilterRPTHoldDownRemain based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_TFilterRPTHoldDownRemain_Type.__name__ = "Unsigned32"
_TFilterRPTHoldDownRemain_Object = MibTableColumn
tFilterRPTHoldDownRemain = _TFilterRPTHoldDownRemain_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 16, 1, 6),
    _TFilterRPTHoldDownRemain_Type()
)
tFilterRPTHoldDownRemain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterRPTHoldDownRemain.setStatus("current")
if mibBuilder.loadTexts:
    tFilterRPTHoldDownRemain.setUnits("seconds")
_TFilterRPTLastActionTime_Type = TimeStamp
_TFilterRPTLastActionTime_Object = MibTableColumn
tFilterRPTLastActionTime = _TFilterRPTLastActionTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 16, 1, 7),
    _TFilterRPTLastActionTime_Type()
)
tFilterRPTLastActionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterRPTLastActionTime.setStatus("current")


class _TFilterRPTLastAction_Type(Integer32):
    """Custom type tFilterRPTLastAction based on Integer32"""
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
          ("none", 3))
    )


_TFilterRPTLastAction_Type.__name__ = "Integer32"
_TFilterRPTLastAction_Object = MibTableColumn
tFilterRPTLastAction = _TFilterRPTLastAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 16, 1, 8),
    _TFilterRPTLastAction_Type()
)
tFilterRPTLastAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterRPTLastAction.setStatus("current")
_TAutoIPFilterEntryTable_Object = MibTable
tAutoIPFilterEntryTable = _TAutoIPFilterEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 17)
)
if mibBuilder.loadTexts:
    tAutoIPFilterEntryTable.setStatus("obsolete")
_TAutoIPFilterEntry_Object = MibTableRow
tAutoIPFilterEntry = _TAutoIPFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 17, 1)
)
tAutoIPFilterEntry.setIndexNames(
    (0, "TIMETRA-FILTER-MIB", "tAutoIPFilterId"),
    (0, "TIMETRA-FILTER-MIB", "tAutoIPFilterEntrySourceIpAddr"),
)
if mibBuilder.loadTexts:
    tAutoIPFilterEntry.setStatus("obsolete")


class _TAutoIPFilterId_Type(TFilterID):
    """Custom type tAutoIPFilterId based on TFilterID"""
    subtypeSpec = TFilterID.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TAutoIPFilterId_Type.__name__ = "TFilterID"
_TAutoIPFilterId_Object = MibTableColumn
tAutoIPFilterId = _TAutoIPFilterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 17, 1, 1),
    _TAutoIPFilterId_Type()
)
tAutoIPFilterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tAutoIPFilterId.setStatus("obsolete")
_TAutoIPFilterEntrySourceIpAddr_Type = IpAddress
_TAutoIPFilterEntrySourceIpAddr_Object = MibTableColumn
tAutoIPFilterEntrySourceIpAddr = _TAutoIPFilterEntrySourceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 17, 1, 2),
    _TAutoIPFilterEntrySourceIpAddr_Type()
)
tAutoIPFilterEntrySourceIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tAutoIPFilterEntrySourceIpAddr.setStatus("obsolete")
_TAutoIPFilterEntrySourceIpMask_Type = IpAddressPrefixLength
_TAutoIPFilterEntrySourceIpMask_Object = MibTableColumn
tAutoIPFilterEntrySourceIpMask = _TAutoIPFilterEntrySourceIpMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 17, 1, 3),
    _TAutoIPFilterEntrySourceIpMask_Type()
)
tAutoIPFilterEntrySourceIpMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAutoIPFilterEntrySourceIpMask.setStatus("obsolete")
_TIPv6FilterTable_Object = MibTable
tIPv6FilterTable = _TIPv6FilterTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 18)
)
if mibBuilder.loadTexts:
    tIPv6FilterTable.setStatus("current")
_TIPv6FilterEntry_Object = MibTableRow
tIPv6FilterEntry = _TIPv6FilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 18, 1)
)
tIPv6FilterEntry.setIndexNames(
    (0, "TIMETRA-FILTER-MIB", "tIPv6FilterId"),
)
if mibBuilder.loadTexts:
    tIPv6FilterEntry.setStatus("current")
_TIPv6FilterId_Type = TAnyFilterID
_TIPv6FilterId_Object = MibTableColumn
tIPv6FilterId = _TIPv6FilterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 18, 1, 1),
    _TIPv6FilterId_Type()
)
tIPv6FilterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tIPv6FilterId.setStatus("current")
_TIPv6FilterRowStatus_Type = RowStatus
_TIPv6FilterRowStatus_Object = MibTableColumn
tIPv6FilterRowStatus = _TIPv6FilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 18, 1, 2),
    _TIPv6FilterRowStatus_Type()
)
tIPv6FilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterRowStatus.setStatus("current")


class _TIPv6FilterScope_Type(TFilterScope):
    """Custom type tIPv6FilterScope based on TFilterScope"""
    defaultValue = 2


_TIPv6FilterScope_Type.__name__ = "TFilterScope"
_TIPv6FilterScope_Object = MibTableColumn
tIPv6FilterScope = _TIPv6FilterScope_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 18, 1, 3),
    _TIPv6FilterScope_Type()
)
tIPv6FilterScope.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterScope.setStatus("current")


class _TIPv6FilterDescription_Type(TItemDescription):
    """Custom type tIPv6FilterDescription based on TItemDescription"""
    defaultHexValue = ""


_TIPv6FilterDescription_Type.__name__ = "TItemDescription"
_TIPv6FilterDescription_Object = MibTableColumn
tIPv6FilterDescription = _TIPv6FilterDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 18, 1, 4),
    _TIPv6FilterDescription_Type()
)
tIPv6FilterDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterDescription.setStatus("current")


class _TIPv6FilterDefaultAction_Type(TFilterAction):
    """Custom type tIPv6FilterDefaultAction based on TFilterAction"""
    defaultValue = 1


_TIPv6FilterDefaultAction_Type.__name__ = "TFilterAction"
_TIPv6FilterDefaultAction_Object = MibTableColumn
tIPv6FilterDefaultAction = _TIPv6FilterDefaultAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 18, 1, 5),
    _TIPv6FilterDefaultAction_Type()
)
tIPv6FilterDefaultAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterDefaultAction.setStatus("current")


class _TIPv6FilterRadiusInsertPt_Type(TEntryIdOrZero):
    """Custom type tIPv6FilterRadiusInsertPt based on TEntryIdOrZero"""
    defaultValue = 0


_TIPv6FilterRadiusInsertPt_Type.__name__ = "TEntryIdOrZero"
_TIPv6FilterRadiusInsertPt_Object = MibTableColumn
tIPv6FilterRadiusInsertPt = _TIPv6FilterRadiusInsertPt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 18, 1, 6),
    _TIPv6FilterRadiusInsertPt_Type()
)
tIPv6FilterRadiusInsertPt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterRadiusInsertPt.setStatus("current")


class _TIPv6FilterRadiusInsertSize_Type(TEntryIdOrZero):
    """Custom type tIPv6FilterRadiusInsertSize based on TEntryIdOrZero"""
    defaultValue = 0


_TIPv6FilterRadiusInsertSize_Type.__name__ = "TEntryIdOrZero"
_TIPv6FilterRadiusInsertSize_Object = MibTableColumn
tIPv6FilterRadiusInsertSize = _TIPv6FilterRadiusInsertSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 18, 1, 7),
    _TIPv6FilterRadiusInsertSize_Type()
)
tIPv6FilterRadiusInsertSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterRadiusInsertSize.setStatus("current")


class _TIPv6FilterCreditCntrlInsertPt_Type(TEntryIdOrZero):
    """Custom type tIPv6FilterCreditCntrlInsertPt based on TEntryIdOrZero"""
    defaultValue = 0


_TIPv6FilterCreditCntrlInsertPt_Type.__name__ = "TEntryIdOrZero"
_TIPv6FilterCreditCntrlInsertPt_Object = MibTableColumn
tIPv6FilterCreditCntrlInsertPt = _TIPv6FilterCreditCntrlInsertPt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 18, 1, 8),
    _TIPv6FilterCreditCntrlInsertPt_Type()
)
tIPv6FilterCreditCntrlInsertPt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterCreditCntrlInsertPt.setStatus("current")


class _TIPv6FilterCreditCntrlInsertSize_Type(TEntryIdOrZero):
    """Custom type tIPv6FilterCreditCntrlInsertSize based on TEntryIdOrZero"""
    defaultValue = 0


_TIPv6FilterCreditCntrlInsertSize_Type.__name__ = "TEntryIdOrZero"
_TIPv6FilterCreditCntrlInsertSize_Object = MibTableColumn
tIPv6FilterCreditCntrlInsertSize = _TIPv6FilterCreditCntrlInsertSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 18, 1, 9),
    _TIPv6FilterCreditCntrlInsertSize_Type()
)
tIPv6FilterCreditCntrlInsertSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterCreditCntrlInsertSize.setStatus("current")


class _TIPv6FilterSubInsertHighWmark_Type(Integer32):
    """Custom type tIPv6FilterSubInsertHighWmark based on Integer32"""
    defaultValue = 95

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TIPv6FilterSubInsertHighWmark_Type.__name__ = "Integer32"
_TIPv6FilterSubInsertHighWmark_Object = MibTableColumn
tIPv6FilterSubInsertHighWmark = _TIPv6FilterSubInsertHighWmark_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 18, 1, 10),
    _TIPv6FilterSubInsertHighWmark_Type()
)
tIPv6FilterSubInsertHighWmark.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterSubInsertHighWmark.setStatus("current")


class _TIPv6FilterSubInsertLowWmark_Type(Integer32):
    """Custom type tIPv6FilterSubInsertLowWmark based on Integer32"""
    defaultValue = 90

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TIPv6FilterSubInsertLowWmark_Type.__name__ = "Integer32"
_TIPv6FilterSubInsertLowWmark_Object = MibTableColumn
tIPv6FilterSubInsertLowWmark = _TIPv6FilterSubInsertLowWmark_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 18, 1, 11),
    _TIPv6FilterSubInsertLowWmark_Type()
)
tIPv6FilterSubInsertLowWmark.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterSubInsertLowWmark.setStatus("current")
_TIpv6FilterCreditCntrlNbrInsertd_Type = Unsigned32
_TIpv6FilterCreditCntrlNbrInsertd_Object = MibTableColumn
tIpv6FilterCreditCntrlNbrInsertd = _TIpv6FilterCreditCntrlNbrInsertd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 18, 1, 12),
    _TIpv6FilterCreditCntrlNbrInsertd_Type()
)
tIpv6FilterCreditCntrlNbrInsertd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIpv6FilterCreditCntrlNbrInsertd.setStatus("current")
_TIpv6FilterRadiusNbrInsertd_Type = Unsigned32
_TIpv6FilterRadiusNbrInsertd_Object = MibTableColumn
tIpv6FilterRadiusNbrInsertd = _TIpv6FilterRadiusNbrInsertd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 18, 1, 13),
    _TIpv6FilterRadiusNbrInsertd_Type()
)
tIpv6FilterRadiusNbrInsertd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIpv6FilterRadiusNbrInsertd.setStatus("current")


class _TIpv6FilterName_Type(TLNamedItemOrEmpty):
    """Custom type tIpv6FilterName based on TLNamedItemOrEmpty"""
    defaultHexValue = ""


_TIpv6FilterName_Type.__name__ = "TLNamedItemOrEmpty"
_TIpv6FilterName_Object = MibTableColumn
tIpv6FilterName = _TIpv6FilterName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 18, 1, 14),
    _TIpv6FilterName_Type()
)
tIpv6FilterName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIpv6FilterName.setStatus("current")


class _TIPv6FilterHostSharedInsertPt_Type(TEntryIdOrZero):
    """Custom type tIPv6FilterHostSharedInsertPt based on TEntryIdOrZero"""
    defaultValue = 0


_TIPv6FilterHostSharedInsertPt_Type.__name__ = "TEntryIdOrZero"
_TIPv6FilterHostSharedInsertPt_Object = MibTableColumn
tIPv6FilterHostSharedInsertPt = _TIPv6FilterHostSharedInsertPt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 18, 1, 15),
    _TIPv6FilterHostSharedInsertPt_Type()
)
tIPv6FilterHostSharedInsertPt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterHostSharedInsertPt.setStatus("current")


class _TIPv6FilterHostSharedInsertSize_Type(TEntryIdOrZero):
    """Custom type tIPv6FilterHostSharedInsertSize based on TEntryIdOrZero"""
    defaultValue = 0


_TIPv6FilterHostSharedInsertSize_Type.__name__ = "TEntryIdOrZero"
_TIPv6FilterHostSharedInsertSize_Object = MibTableColumn
tIPv6FilterHostSharedInsertSize = _TIPv6FilterHostSharedInsertSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 18, 1, 16),
    _TIPv6FilterHostSharedInsertSize_Type()
)
tIPv6FilterHostSharedInsertSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterHostSharedInsertSize.setStatus("current")
_TIpv6FilterHostSharedNbrInsertd_Type = Unsigned32
_TIpv6FilterHostSharedNbrInsertd_Object = MibTableColumn
tIpv6FilterHostSharedNbrInsertd = _TIpv6FilterHostSharedNbrInsertd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 18, 1, 17),
    _TIpv6FilterHostSharedNbrInsertd_Type()
)
tIpv6FilterHostSharedNbrInsertd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIpv6FilterHostSharedNbrInsertd.setStatus("current")


class _TIPv6FilterHostSharedHighWmark_Type(Integer32):
    """Custom type tIPv6FilterHostSharedHighWmark based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 8000),
    )


_TIPv6FilterHostSharedHighWmark_Type.__name__ = "Integer32"
_TIPv6FilterHostSharedHighWmark_Object = MibTableColumn
tIPv6FilterHostSharedHighWmark = _TIPv6FilterHostSharedHighWmark_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 18, 1, 18),
    _TIPv6FilterHostSharedHighWmark_Type()
)
tIPv6FilterHostSharedHighWmark.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterHostSharedHighWmark.setStatus("current")


class _TIPv6FilterHostSharedLowWmark_Type(Integer32):
    """Custom type tIPv6FilterHostSharedLowWmark based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 8000),
    )


_TIPv6FilterHostSharedLowWmark_Type.__name__ = "Integer32"
_TIPv6FilterHostSharedLowWmark_Object = MibTableColumn
tIPv6FilterHostSharedLowWmark = _TIPv6FilterHostSharedLowWmark_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 18, 1, 19),
    _TIPv6FilterHostSharedLowWmark_Type()
)
tIPv6FilterHostSharedLowWmark.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterHostSharedLowWmark.setStatus("current")
_TIPv6FilterNbrHostSharedFltrs_Type = Unsigned32
_TIPv6FilterNbrHostSharedFltrs_Object = MibTableColumn
tIPv6FilterNbrHostSharedFltrs = _TIPv6FilterNbrHostSharedFltrs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 18, 1, 20),
    _TIPv6FilterNbrHostSharedFltrs_Type()
)
tIPv6FilterNbrHostSharedFltrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPv6FilterNbrHostSharedFltrs.setStatus("current")
_TIPv6FilterParamsTable_Object = MibTable
tIPv6FilterParamsTable = _TIPv6FilterParamsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19)
)
if mibBuilder.loadTexts:
    tIPv6FilterParamsTable.setStatus("current")
_TIPv6FilterParamsEntry_Object = MibTableRow
tIPv6FilterParamsEntry = _TIPv6FilterParamsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1)
)
tIPv6FilterParamsEntry.setIndexNames(
    (0, "TIMETRA-FILTER-MIB", "tIPv6FilterId"),
    (0, "TIMETRA-FILTER-MIB", "tIPv6FilterParamsIndex"),
)
if mibBuilder.loadTexts:
    tIPv6FilterParamsEntry.setStatus("current")
_TIPv6FilterParamsIndex_Type = TAnyEntryId
_TIPv6FilterParamsIndex_Object = MibTableColumn
tIPv6FilterParamsIndex = _TIPv6FilterParamsIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 1),
    _TIPv6FilterParamsIndex_Type()
)
tIPv6FilterParamsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tIPv6FilterParamsIndex.setStatus("current")
_TIPv6FilterParamsRowStatus_Type = RowStatus
_TIPv6FilterParamsRowStatus_Object = MibTableColumn
tIPv6FilterParamsRowStatus = _TIPv6FilterParamsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 2),
    _TIPv6FilterParamsRowStatus_Type()
)
tIPv6FilterParamsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsRowStatus.setStatus("current")


class _TIPv6FilterParamsLogId_Type(TFilterLogId):
    """Custom type tIPv6FilterParamsLogId based on TFilterLogId"""
    defaultValue = 0


_TIPv6FilterParamsLogId_Type.__name__ = "TFilterLogId"
_TIPv6FilterParamsLogId_Object = MibTableColumn
tIPv6FilterParamsLogId = _TIPv6FilterParamsLogId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 3),
    _TIPv6FilterParamsLogId_Type()
)
tIPv6FilterParamsLogId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsLogId.setStatus("current")


class _TIPv6FilterParamsDescription_Type(TItemDescription):
    """Custom type tIPv6FilterParamsDescription based on TItemDescription"""
    defaultHexValue = ""


_TIPv6FilterParamsDescription_Type.__name__ = "TItemDescription"
_TIPv6FilterParamsDescription_Object = MibTableColumn
tIPv6FilterParamsDescription = _TIPv6FilterParamsDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 4),
    _TIPv6FilterParamsDescription_Type()
)
tIPv6FilterParamsDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsDescription.setStatus("current")


class _TIPv6FilterParamsAction_Type(TFilterActionOrDefault):
    """Custom type tIPv6FilterParamsAction based on TFilterActionOrDefault"""
    defaultValue = 1


_TIPv6FilterParamsAction_Type.__name__ = "TFilterActionOrDefault"
_TIPv6FilterParamsAction_Object = MibTableColumn
tIPv6FilterParamsAction = _TIPv6FilterParamsAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 5),
    _TIPv6FilterParamsAction_Type()
)
tIPv6FilterParamsAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsAction.setStatus("current")


class _TIPv6FilterParamsForwardNH_Type(InetAddressIPv6):
    """Custom type tIPv6FilterParamsForwardNH based on InetAddressIPv6"""
    defaultHexValue = "00000000000000000000000000000000"


_TIPv6FilterParamsForwardNH_Type.__name__ = "InetAddressIPv6"
_TIPv6FilterParamsForwardNH_Object = MibTableColumn
tIPv6FilterParamsForwardNH = _TIPv6FilterParamsForwardNH_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 6),
    _TIPv6FilterParamsForwardNH_Type()
)
tIPv6FilterParamsForwardNH.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsForwardNH.setStatus("current")


class _TIPv6FilterParamsForwardNHIndirect_Type(TruthValue):
    """Custom type tIPv6FilterParamsForwardNHIndirect based on TruthValue"""
    defaultValue = 2


_TIPv6FilterParamsForwardNHIndirect_Type.__name__ = "TruthValue"
_TIPv6FilterParamsForwardNHIndirect_Object = MibTableColumn
tIPv6FilterParamsForwardNHIndirect = _TIPv6FilterParamsForwardNHIndirect_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 7),
    _TIPv6FilterParamsForwardNHIndirect_Type()
)
tIPv6FilterParamsForwardNHIndirect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsForwardNHIndirect.setStatus("current")


class _TIPv6FilterParamsRemarkDSCP_Type(TDSCPFilterActionValue):
    """Custom type tIPv6FilterParamsRemarkDSCP based on TDSCPFilterActionValue"""
    defaultValue = -1


_TIPv6FilterParamsRemarkDSCP_Type.__name__ = "TDSCPFilterActionValue"
_TIPv6FilterParamsRemarkDSCP_Object = MibTableColumn
tIPv6FilterParamsRemarkDSCP = _TIPv6FilterParamsRemarkDSCP_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 8),
    _TIPv6FilterParamsRemarkDSCP_Type()
)
tIPv6FilterParamsRemarkDSCP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsRemarkDSCP.setStatus("current")


class _TIPv6FilterParamsRemarkDSCPMask_Type(TDSCPFilterActionValue):
    """Custom type tIPv6FilterParamsRemarkDSCPMask based on TDSCPFilterActionValue"""
    defaultValue = 255


_TIPv6FilterParamsRemarkDSCPMask_Type.__name__ = "TDSCPFilterActionValue"
_TIPv6FilterParamsRemarkDSCPMask_Object = MibTableColumn
tIPv6FilterParamsRemarkDSCPMask = _TIPv6FilterParamsRemarkDSCPMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 9),
    _TIPv6FilterParamsRemarkDSCPMask_Type()
)
tIPv6FilterParamsRemarkDSCPMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsRemarkDSCPMask.setStatus("current")


class _TIPv6FilterParamsRemarkDot1p_Type(Dot1PPriority):
    """Custom type tIPv6FilterParamsRemarkDot1p based on Dot1PPriority"""
    defaultValue = -1


_TIPv6FilterParamsRemarkDot1p_Type.__name__ = "Dot1PPriority"
_TIPv6FilterParamsRemarkDot1p_Object = MibTableColumn
tIPv6FilterParamsRemarkDot1p = _TIPv6FilterParamsRemarkDot1p_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 10),
    _TIPv6FilterParamsRemarkDot1p_Type()
)
tIPv6FilterParamsRemarkDot1p.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsRemarkDot1p.setStatus("current")


class _TIPv6FilterParamsSourceIpAddr_Type(InetAddressIPv6):
    """Custom type tIPv6FilterParamsSourceIpAddr based on InetAddressIPv6"""
    defaultHexValue = "00000000000000000000000000000000"


_TIPv6FilterParamsSourceIpAddr_Type.__name__ = "InetAddressIPv6"
_TIPv6FilterParamsSourceIpAddr_Object = MibTableColumn
tIPv6FilterParamsSourceIpAddr = _TIPv6FilterParamsSourceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 11),
    _TIPv6FilterParamsSourceIpAddr_Type()
)
tIPv6FilterParamsSourceIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsSourceIpAddr.setStatus("current")


class _TIPv6FilterParamsSourceIpMask_Type(InetAddressPrefixLength):
    """Custom type tIPv6FilterParamsSourceIpMask based on InetAddressPrefixLength"""
    defaultValue = 0

    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_TIPv6FilterParamsSourceIpMask_Type.__name__ = "InetAddressPrefixLength"
_TIPv6FilterParamsSourceIpMask_Object = MibTableColumn
tIPv6FilterParamsSourceIpMask = _TIPv6FilterParamsSourceIpMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 12),
    _TIPv6FilterParamsSourceIpMask_Type()
)
tIPv6FilterParamsSourceIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsSourceIpMask.setStatus("current")


class _TIPv6FilterParamsDestinationIpAddr_Type(InetAddressIPv6):
    """Custom type tIPv6FilterParamsDestinationIpAddr based on InetAddressIPv6"""
    defaultHexValue = "00000000000000000000000000000000"


_TIPv6FilterParamsDestinationIpAddr_Type.__name__ = "InetAddressIPv6"
_TIPv6FilterParamsDestinationIpAddr_Object = MibTableColumn
tIPv6FilterParamsDestinationIpAddr = _TIPv6FilterParamsDestinationIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 13),
    _TIPv6FilterParamsDestinationIpAddr_Type()
)
tIPv6FilterParamsDestinationIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsDestinationIpAddr.setStatus("current")


class _TIPv6FilterParamsDestinationIpMask_Type(InetAddressPrefixLength):
    """Custom type tIPv6FilterParamsDestinationIpMask based on InetAddressPrefixLength"""
    defaultValue = 0

    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_TIPv6FilterParamsDestinationIpMask_Type.__name__ = "InetAddressPrefixLength"
_TIPv6FilterParamsDestinationIpMask_Object = MibTableColumn
tIPv6FilterParamsDestinationIpMask = _TIPv6FilterParamsDestinationIpMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 14),
    _TIPv6FilterParamsDestinationIpMask_Type()
)
tIPv6FilterParamsDestinationIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsDestinationIpMask.setStatus("current")


class _TIPv6FilterParamsNextHeader_Type(TIpProtocol):
    """Custom type tIPv6FilterParamsNextHeader based on TIpProtocol"""
    defaultValue = -1


_TIPv6FilterParamsNextHeader_Type.__name__ = "TIpProtocol"
_TIPv6FilterParamsNextHeader_Object = MibTableColumn
tIPv6FilterParamsNextHeader = _TIPv6FilterParamsNextHeader_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 15),
    _TIPv6FilterParamsNextHeader_Type()
)
tIPv6FilterParamsNextHeader.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsNextHeader.setStatus("current")


class _TIPv6FilterParamsSourcePortValue1_Type(TTcpUdpPort):
    """Custom type tIPv6FilterParamsSourcePortValue1 based on TTcpUdpPort"""
    defaultValue = 0


_TIPv6FilterParamsSourcePortValue1_Type.__name__ = "TTcpUdpPort"
_TIPv6FilterParamsSourcePortValue1_Object = MibTableColumn
tIPv6FilterParamsSourcePortValue1 = _TIPv6FilterParamsSourcePortValue1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 16),
    _TIPv6FilterParamsSourcePortValue1_Type()
)
tIPv6FilterParamsSourcePortValue1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsSourcePortValue1.setStatus("current")


class _TIPv6FilterParamsSourcePortValue2_Type(TTcpUdpPort):
    """Custom type tIPv6FilterParamsSourcePortValue2 based on TTcpUdpPort"""
    defaultValue = 0


_TIPv6FilterParamsSourcePortValue2_Type.__name__ = "TTcpUdpPort"
_TIPv6FilterParamsSourcePortValue2_Object = MibTableColumn
tIPv6FilterParamsSourcePortValue2 = _TIPv6FilterParamsSourcePortValue2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 17),
    _TIPv6FilterParamsSourcePortValue2_Type()
)
tIPv6FilterParamsSourcePortValue2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsSourcePortValue2.setStatus("current")


class _TIPv6FilterParamsSourcePortOperator_Type(TTcpUdpPortOperator):
    """Custom type tIPv6FilterParamsSourcePortOperator based on TTcpUdpPortOperator"""
    defaultValue = 0


_TIPv6FilterParamsSourcePortOperator_Type.__name__ = "TTcpUdpPortOperator"
_TIPv6FilterParamsSourcePortOperator_Object = MibTableColumn
tIPv6FilterParamsSourcePortOperator = _TIPv6FilterParamsSourcePortOperator_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 18),
    _TIPv6FilterParamsSourcePortOperator_Type()
)
tIPv6FilterParamsSourcePortOperator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsSourcePortOperator.setStatus("current")


class _TIPv6FilterParamsDestPortValue1_Type(TTcpUdpPort):
    """Custom type tIPv6FilterParamsDestPortValue1 based on TTcpUdpPort"""
    defaultValue = 0


_TIPv6FilterParamsDestPortValue1_Type.__name__ = "TTcpUdpPort"
_TIPv6FilterParamsDestPortValue1_Object = MibTableColumn
tIPv6FilterParamsDestPortValue1 = _TIPv6FilterParamsDestPortValue1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 19),
    _TIPv6FilterParamsDestPortValue1_Type()
)
tIPv6FilterParamsDestPortValue1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsDestPortValue1.setStatus("current")


class _TIPv6FilterParamsDestPortValue2_Type(TTcpUdpPort):
    """Custom type tIPv6FilterParamsDestPortValue2 based on TTcpUdpPort"""
    defaultValue = 0


_TIPv6FilterParamsDestPortValue2_Type.__name__ = "TTcpUdpPort"
_TIPv6FilterParamsDestPortValue2_Object = MibTableColumn
tIPv6FilterParamsDestPortValue2 = _TIPv6FilterParamsDestPortValue2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 20),
    _TIPv6FilterParamsDestPortValue2_Type()
)
tIPv6FilterParamsDestPortValue2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsDestPortValue2.setStatus("current")


class _TIPv6FilterParamsDestPortOperator_Type(TTcpUdpPortOperator):
    """Custom type tIPv6FilterParamsDestPortOperator based on TTcpUdpPortOperator"""
    defaultValue = 0


_TIPv6FilterParamsDestPortOperator_Type.__name__ = "TTcpUdpPortOperator"
_TIPv6FilterParamsDestPortOperator_Object = MibTableColumn
tIPv6FilterParamsDestPortOperator = _TIPv6FilterParamsDestPortOperator_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 21),
    _TIPv6FilterParamsDestPortOperator_Type()
)
tIPv6FilterParamsDestPortOperator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsDestPortOperator.setStatus("current")


class _TIPv6FilterParamsDSCP_Type(TDSCPNameOrEmpty):
    """Custom type tIPv6FilterParamsDSCP based on TDSCPNameOrEmpty"""
    defaultHexValue = ""


_TIPv6FilterParamsDSCP_Type.__name__ = "TDSCPNameOrEmpty"
_TIPv6FilterParamsDSCP_Object = MibTableColumn
tIPv6FilterParamsDSCP = _TIPv6FilterParamsDSCP_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 22),
    _TIPv6FilterParamsDSCP_Type()
)
tIPv6FilterParamsDSCP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsDSCP.setStatus("current")


class _TIPv6FilterParamsTcpSyn_Type(TItemMatch):
    """Custom type tIPv6FilterParamsTcpSyn based on TItemMatch"""
    defaultValue = 1


_TIPv6FilterParamsTcpSyn_Type.__name__ = "TItemMatch"
_TIPv6FilterParamsTcpSyn_Object = MibTableColumn
tIPv6FilterParamsTcpSyn = _TIPv6FilterParamsTcpSyn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 23),
    _TIPv6FilterParamsTcpSyn_Type()
)
tIPv6FilterParamsTcpSyn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsTcpSyn.setStatus("current")


class _TIPv6FilterParamsTcpAck_Type(TItemMatch):
    """Custom type tIPv6FilterParamsTcpAck based on TItemMatch"""
    defaultValue = 1


_TIPv6FilterParamsTcpAck_Type.__name__ = "TItemMatch"
_TIPv6FilterParamsTcpAck_Object = MibTableColumn
tIPv6FilterParamsTcpAck = _TIPv6FilterParamsTcpAck_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 24),
    _TIPv6FilterParamsTcpAck_Type()
)
tIPv6FilterParamsTcpAck.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsTcpAck.setStatus("current")


class _TIPv6FilterParamsIcmpCode_Type(Integer32):
    """Custom type tIPv6FilterParamsIcmpCode based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 255),
    )


_TIPv6FilterParamsIcmpCode_Type.__name__ = "Integer32"
_TIPv6FilterParamsIcmpCode_Object = MibTableColumn
tIPv6FilterParamsIcmpCode = _TIPv6FilterParamsIcmpCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 25),
    _TIPv6FilterParamsIcmpCode_Type()
)
tIPv6FilterParamsIcmpCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsIcmpCode.setStatus("current")


class _TIPv6FilterParamsIcmpType_Type(Integer32):
    """Custom type tIPv6FilterParamsIcmpType based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 255),
    )


_TIPv6FilterParamsIcmpType_Type.__name__ = "Integer32"
_TIPv6FilterParamsIcmpType_Object = MibTableColumn
tIPv6FilterParamsIcmpType = _TIPv6FilterParamsIcmpType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 26),
    _TIPv6FilterParamsIcmpType_Type()
)
tIPv6FilterParamsIcmpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsIcmpType.setStatus("current")


class _TIPv6FilterParamsCflowdSample_Type(TruthValue):
    """Custom type tIPv6FilterParamsCflowdSample based on TruthValue"""
    defaultValue = 2


_TIPv6FilterParamsCflowdSample_Type.__name__ = "TruthValue"
_TIPv6FilterParamsCflowdSample_Object = MibTableColumn
tIPv6FilterParamsCflowdSample = _TIPv6FilterParamsCflowdSample_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 27),
    _TIPv6FilterParamsCflowdSample_Type()
)
tIPv6FilterParamsCflowdSample.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsCflowdSample.setStatus("current")


class _TIPv6FilterParamsCflowdIfSample_Type(TruthValue):
    """Custom type tIPv6FilterParamsCflowdIfSample based on TruthValue"""
    defaultValue = 1


_TIPv6FilterParamsCflowdIfSample_Type.__name__ = "TruthValue"
_TIPv6FilterParamsCflowdIfSample_Object = MibTableColumn
tIPv6FilterParamsCflowdIfSample = _TIPv6FilterParamsCflowdIfSample_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 28),
    _TIPv6FilterParamsCflowdIfSample_Type()
)
tIPv6FilterParamsCflowdIfSample.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsCflowdIfSample.setStatus("current")


class _TIPv6FilterParamsForwardNHInterface_Type(DisplayString):
    """Custom type tIPv6FilterParamsForwardNHInterface based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TIPv6FilterParamsForwardNHInterface_Type.__name__ = "DisplayString"
_TIPv6FilterParamsForwardNHInterface_Object = MibTableColumn
tIPv6FilterParamsForwardNHInterface = _TIPv6FilterParamsForwardNHInterface_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 29),
    _TIPv6FilterParamsForwardNHInterface_Type()
)
tIPv6FilterParamsForwardNHInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsForwardNHInterface.setStatus("current")
_TIPv6FilterParamsIngressHitCount_Type = Counter64
_TIPv6FilterParamsIngressHitCount_Object = MibTableColumn
tIPv6FilterParamsIngressHitCount = _TIPv6FilterParamsIngressHitCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 30),
    _TIPv6FilterParamsIngressHitCount_Type()
)
tIPv6FilterParamsIngressHitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPv6FilterParamsIngressHitCount.setStatus("current")
_TIPv6FilterParamsEgressHitCount_Type = Counter64
_TIPv6FilterParamsEgressHitCount_Object = MibTableColumn
tIPv6FilterParamsEgressHitCount = _TIPv6FilterParamsEgressHitCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 31),
    _TIPv6FilterParamsEgressHitCount_Type()
)
tIPv6FilterParamsEgressHitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPv6FilterParamsEgressHitCount.setStatus("current")
_TIPv6FilterParamsLogInstantiated_Type = TruthValue
_TIPv6FilterParamsLogInstantiated_Object = MibTableColumn
tIPv6FilterParamsLogInstantiated = _TIPv6FilterParamsLogInstantiated_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 32),
    _TIPv6FilterParamsLogInstantiated_Type()
)
tIPv6FilterParamsLogInstantiated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPv6FilterParamsLogInstantiated.setStatus("current")


class _TIPv6FilterParamsForwardRedPlcy_Type(TNamedItemOrEmpty):
    """Custom type tIPv6FilterParamsForwardRedPlcy based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TIPv6FilterParamsForwardRedPlcy_Type.__name__ = "TNamedItemOrEmpty"
_TIPv6FilterParamsForwardRedPlcy_Object = MibTableColumn
tIPv6FilterParamsForwardRedPlcy = _TIPv6FilterParamsForwardRedPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 33),
    _TIPv6FilterParamsForwardRedPlcy_Type()
)
tIPv6FilterParamsForwardRedPlcy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsForwardRedPlcy.setStatus("current")
_TIPv6FilterParamsActiveDest_Type = InetAddressIPv6
_TIPv6FilterParamsActiveDest_Object = MibTableColumn
tIPv6FilterParamsActiveDest = _TIPv6FilterParamsActiveDest_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 34),
    _TIPv6FilterParamsActiveDest_Type()
)
tIPv6FilterParamsActiveDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPv6FilterParamsActiveDest.setStatus("current")


class _TIPv6FilterParamsTimeRangeName_Type(TNamedItemOrEmpty):
    """Custom type tIPv6FilterParamsTimeRangeName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TIPv6FilterParamsTimeRangeName_Type.__name__ = "TNamedItemOrEmpty"
_TIPv6FilterParamsTimeRangeName_Object = MibTableColumn
tIPv6FilterParamsTimeRangeName = _TIPv6FilterParamsTimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 35),
    _TIPv6FilterParamsTimeRangeName_Type()
)
tIPv6FilterParamsTimeRangeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsTimeRangeName.setStatus("current")
_TIPv6FilterParamsTimeRangeState_Type = TTimeRangeState
_TIPv6FilterParamsTimeRangeState_Object = MibTableColumn
tIPv6FilterParamsTimeRangeState = _TIPv6FilterParamsTimeRangeState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 36),
    _TIPv6FilterParamsTimeRangeState_Type()
)
tIPv6FilterParamsTimeRangeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPv6FilterParamsTimeRangeState.setStatus("current")
_TIPv6FilterParamsIngrHitByteCount_Type = Counter64
_TIPv6FilterParamsIngrHitByteCount_Object = MibTableColumn
tIPv6FilterParamsIngrHitByteCount = _TIPv6FilterParamsIngrHitByteCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 37),
    _TIPv6FilterParamsIngrHitByteCount_Type()
)
tIPv6FilterParamsIngrHitByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPv6FilterParamsIngrHitByteCount.setStatus("current")
_TIPv6FilterParamsEgrHitByteCount_Type = Counter64
_TIPv6FilterParamsEgrHitByteCount_Object = MibTableColumn
tIPv6FilterParamsEgrHitByteCount = _TIPv6FilterParamsEgrHitByteCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 38),
    _TIPv6FilterParamsEgrHitByteCount_Type()
)
tIPv6FilterParamsEgrHitByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPv6FilterParamsEgrHitByteCount.setStatus("current")
_TIPv6FilterParamsFwdSvcId_Type = TmnxServId
_TIPv6FilterParamsFwdSvcId_Object = MibTableColumn
tIPv6FilterParamsFwdSvcId = _TIPv6FilterParamsFwdSvcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 39),
    _TIPv6FilterParamsFwdSvcId_Type()
)
tIPv6FilterParamsFwdSvcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPv6FilterParamsFwdSvcId.setStatus("current")


class _TIPv6FilterParamsFwdSapPortId_Type(TmnxPortID):
    """Custom type tIPv6FilterParamsFwdSapPortId based on TmnxPortID"""
    defaultValue = 0


_TIPv6FilterParamsFwdSapPortId_Type.__name__ = "TmnxPortID"
_TIPv6FilterParamsFwdSapPortId_Object = MibTableColumn
tIPv6FilterParamsFwdSapPortId = _TIPv6FilterParamsFwdSapPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 40),
    _TIPv6FilterParamsFwdSapPortId_Type()
)
tIPv6FilterParamsFwdSapPortId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsFwdSapPortId.setStatus("current")


class _TIPv6FilterParamsFwdSapEncapVal_Type(TmnxEncapVal):
    """Custom type tIPv6FilterParamsFwdSapEncapVal based on TmnxEncapVal"""
    defaultValue = 0


_TIPv6FilterParamsFwdSapEncapVal_Type.__name__ = "TmnxEncapVal"
_TIPv6FilterParamsFwdSapEncapVal_Object = MibTableColumn
tIPv6FilterParamsFwdSapEncapVal = _TIPv6FilterParamsFwdSapEncapVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 41),
    _TIPv6FilterParamsFwdSapEncapVal_Type()
)
tIPv6FilterParamsFwdSapEncapVal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsFwdSapEncapVal.setStatus("current")
_TIPv6FilterParamsFwdSdpBind_Type = SdpBindId
_TIPv6FilterParamsFwdSdpBind_Object = MibTableColumn
tIPv6FilterParamsFwdSdpBind = _TIPv6FilterParamsFwdSdpBind_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 42),
    _TIPv6FilterParamsFwdSdpBind_Type()
)
tIPv6FilterParamsFwdSdpBind.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsFwdSdpBind.setStatus("current")


class _TIPv6FilterParamsRedirectURL_Type(TmnxHttpRedirectUrl):
    """Custom type tIPv6FilterParamsRedirectURL based on TmnxHttpRedirectUrl"""
    defaultHexValue = ""


_TIPv6FilterParamsRedirectURL_Type.__name__ = "TmnxHttpRedirectUrl"
_TIPv6FilterParamsRedirectURL_Object = MibTableColumn
tIPv6FilterParamsRedirectURL = _TIPv6FilterParamsRedirectURL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 43),
    _TIPv6FilterParamsRedirectURL_Type()
)
tIPv6FilterParamsRedirectURL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsRedirectURL.setStatus("current")


class _TIPv6FilterParamsSrcIpPrefixList_Type(TNamedItemOrEmpty):
    """Custom type tIPv6FilterParamsSrcIpPrefixList based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TIPv6FilterParamsSrcIpPrefixList_Type.__name__ = "TNamedItemOrEmpty"
_TIPv6FilterParamsSrcIpPrefixList_Object = MibTableColumn
tIPv6FilterParamsSrcIpPrefixList = _TIPv6FilterParamsSrcIpPrefixList_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 44),
    _TIPv6FilterParamsSrcIpPrefixList_Type()
)
tIPv6FilterParamsSrcIpPrefixList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsSrcIpPrefixList.setStatus("current")


class _TIPv6FilterParamsDstIpPrefixList_Type(TNamedItemOrEmpty):
    """Custom type tIPv6FilterParamsDstIpPrefixList based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TIPv6FilterParamsDstIpPrefixList_Type.__name__ = "TNamedItemOrEmpty"
_TIPv6FilterParamsDstIpPrefixList_Object = MibTableColumn
tIPv6FilterParamsDstIpPrefixList = _TIPv6FilterParamsDstIpPrefixList_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 45),
    _TIPv6FilterParamsDstIpPrefixList_Type()
)
tIPv6FilterParamsDstIpPrefixList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsDstIpPrefixList.setStatus("current")


class _TIPv6FilterParamsFragment_Type(Integer32):
    """Custom type tIPv6FilterParamsFragment based on Integer32"""
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
        *(("off", 1),
          ("false", 2),
          ("true", 3),
          ("first-only", 4),
          ("non-first-only", 5))
    )


_TIPv6FilterParamsFragment_Type.__name__ = "Integer32"
_TIPv6FilterParamsFragment_Object = MibTableColumn
tIPv6FilterParamsFragment = _TIPv6FilterParamsFragment_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 46),
    _TIPv6FilterParamsFragment_Type()
)
tIPv6FilterParamsFragment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsFragment.setStatus("current")


class _TIPv6FilterParamsHopByHopOpt_Type(TItemMatch):
    """Custom type tIPv6FilterParamsHopByHopOpt based on TItemMatch"""
    defaultValue = 1


_TIPv6FilterParamsHopByHopOpt_Type.__name__ = "TItemMatch"
_TIPv6FilterParamsHopByHopOpt_Object = MibTableColumn
tIPv6FilterParamsHopByHopOpt = _TIPv6FilterParamsHopByHopOpt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 47),
    _TIPv6FilterParamsHopByHopOpt_Type()
)
tIPv6FilterParamsHopByHopOpt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsHopByHopOpt.setStatus("current")


class _TIPv6FilterParamsRoutingType0_Type(TItemMatch):
    """Custom type tIPv6FilterParamsRoutingType0 based on TItemMatch"""
    defaultValue = 1


_TIPv6FilterParamsRoutingType0_Type.__name__ = "TItemMatch"
_TIPv6FilterParamsRoutingType0_Object = MibTableColumn
tIPv6FilterParamsRoutingType0 = _TIPv6FilterParamsRoutingType0_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 48),
    _TIPv6FilterParamsRoutingType0_Type()
)
tIPv6FilterParamsRoutingType0.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsRoutingType0.setStatus("current")


class _TIPv6FilterParamsPortSelector_Type(TFltrPortSelector):
    """Custom type tIPv6FilterParamsPortSelector based on TFltrPortSelector"""
    defaultValue = 0


_TIPv6FilterParamsPortSelector_Type.__name__ = "TFltrPortSelector"
_TIPv6FilterParamsPortSelector_Object = MibTableColumn
tIPv6FilterParamsPortSelector = _TIPv6FilterParamsPortSelector_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 49),
    _TIPv6FilterParamsPortSelector_Type()
)
tIPv6FilterParamsPortSelector.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsPortSelector.setStatus("current")


class _TIPv6FilterParamsSrcPortList_Type(TNamedItemOrEmpty):
    """Custom type tIPv6FilterParamsSrcPortList based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TIPv6FilterParamsSrcPortList_Type.__name__ = "TNamedItemOrEmpty"
_TIPv6FilterParamsSrcPortList_Object = MibTableColumn
tIPv6FilterParamsSrcPortList = _TIPv6FilterParamsSrcPortList_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 50),
    _TIPv6FilterParamsSrcPortList_Type()
)
tIPv6FilterParamsSrcPortList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsSrcPortList.setStatus("current")


class _TIPv6FilterParamsDstPortList_Type(TNamedItemOrEmpty):
    """Custom type tIPv6FilterParamsDstPortList based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TIPv6FilterParamsDstPortList_Type.__name__ = "TNamedItemOrEmpty"
_TIPv6FilterParamsDstPortList_Object = MibTableColumn
tIPv6FilterParamsDstPortList = _TIPv6FilterParamsDstPortList_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 51),
    _TIPv6FilterParamsDstPortList_Type()
)
tIPv6FilterParamsDstPortList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsDstPortList.setStatus("current")


class _TIPv6FilterParamsRdirAllwRadOvrd_Type(TruthValue):
    """Custom type tIPv6FilterParamsRdirAllwRadOvrd based on TruthValue"""
    defaultValue = 2


_TIPv6FilterParamsRdirAllwRadOvrd_Type.__name__ = "TruthValue"
_TIPv6FilterParamsRdirAllwRadOvrd_Object = MibTableColumn
tIPv6FilterParamsRdirAllwRadOvrd = _TIPv6FilterParamsRdirAllwRadOvrd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 52),
    _TIPv6FilterParamsRdirAllwRadOvrd_Type()
)
tIPv6FilterParamsRdirAllwRadOvrd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsRdirAllwRadOvrd.setStatus("current")


class _TIPv6FilterParamsFwdRtrId_Type(TmnxVRtrIDOrZero):
    """Custom type tIPv6FilterParamsFwdRtrId based on TmnxVRtrIDOrZero"""
    defaultValue = 0


_TIPv6FilterParamsFwdRtrId_Type.__name__ = "TmnxVRtrIDOrZero"
_TIPv6FilterParamsFwdRtrId_Object = MibTableColumn
tIPv6FilterParamsFwdRtrId = _TIPv6FilterParamsFwdRtrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 53),
    _TIPv6FilterParamsFwdRtrId_Type()
)
tIPv6FilterParamsFwdRtrId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsFwdRtrId.setStatus("current")


class _TIPv6FilterParamsSrcIpFullMask_Type(InetAddressIPv6):
    """Custom type tIPv6FilterParamsSrcIpFullMask based on InetAddressIPv6"""
    defaultHexValue = "00000000000000000000000000000000"


_TIPv6FilterParamsSrcIpFullMask_Type.__name__ = "InetAddressIPv6"
_TIPv6FilterParamsSrcIpFullMask_Object = MibTableColumn
tIPv6FilterParamsSrcIpFullMask = _TIPv6FilterParamsSrcIpFullMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 54),
    _TIPv6FilterParamsSrcIpFullMask_Type()
)
tIPv6FilterParamsSrcIpFullMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsSrcIpFullMask.setStatus("current")


class _TIPv6FilterParamsDstIpFullMask_Type(InetAddressIPv6):
    """Custom type tIPv6FilterParamsDstIpFullMask based on InetAddressIPv6"""
    defaultHexValue = "00000000000000000000000000000000"


_TIPv6FilterParamsDstIpFullMask_Type.__name__ = "InetAddressIPv6"
_TIPv6FilterParamsDstIpFullMask_Object = MibTableColumn
tIPv6FilterParamsDstIpFullMask = _TIPv6FilterParamsDstIpFullMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 55),
    _TIPv6FilterParamsDstIpFullMask_Type()
)
tIPv6FilterParamsDstIpFullMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsDstIpFullMask.setStatus("current")


class _TIPv6FilterParamsNatPolicyName_Type(TNamedItemOrEmpty):
    """Custom type tIPv6FilterParamsNatPolicyName based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TIPv6FilterParamsNatPolicyName_Type.__name__ = "TNamedItemOrEmpty"
_TIPv6FilterParamsNatPolicyName_Object = MibTableColumn
tIPv6FilterParamsNatPolicyName = _TIPv6FilterParamsNatPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 56),
    _TIPv6FilterParamsNatPolicyName_Type()
)
tIPv6FilterParamsNatPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsNatPolicyName.setStatus("current")


class _TIPv6FilterParamsFlowLabel_Type(IPv6FlowLabel):
    """Custom type tIPv6FilterParamsFlowLabel based on IPv6FlowLabel"""
    defaultValue = -1


_TIPv6FilterParamsFlowLabel_Type.__name__ = "IPv6FlowLabel"
_TIPv6FilterParamsFlowLabel_Object = MibTableColumn
tIPv6FilterParamsFlowLabel = _TIPv6FilterParamsFlowLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 57),
    _TIPv6FilterParamsFlowLabel_Type()
)
tIPv6FilterParamsFlowLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsFlowLabel.setStatus("current")


class _TIPv6FilterParamsFlowLabelMask_Type(IPv6FlowLabelMask):
    """Custom type tIPv6FilterParamsFlowLabelMask based on IPv6FlowLabelMask"""
    defaultValue = 1048575


_TIPv6FilterParamsFlowLabelMask_Type.__name__ = "IPv6FlowLabelMask"
_TIPv6FilterParamsFlowLabelMask_Object = MibTableColumn
tIPv6FilterParamsFlowLabelMask = _TIPv6FilterParamsFlowLabelMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 58),
    _TIPv6FilterParamsFlowLabelMask_Type()
)
tIPv6FilterParamsFlowLabelMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsFlowLabelMask.setStatus("current")


class _TIPv6FilterParamsFwdLsp_Type(TmnxVRtrMplsLspID):
    """Custom type tIPv6FilterParamsFwdLsp based on TmnxVRtrMplsLspID"""
    defaultValue = 0


_TIPv6FilterParamsFwdLsp_Type.__name__ = "TmnxVRtrMplsLspID"
_TIPv6FilterParamsFwdLsp_Object = MibTableColumn
tIPv6FilterParamsFwdLsp = _TIPv6FilterParamsFwdLsp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 59),
    _TIPv6FilterParamsFwdLsp_Type()
)
tIPv6FilterParamsFwdLsp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsFwdLsp.setStatus("current")


class _TIPv6FilterParamsFwdLspRtrId_Type(TmnxVRtrIDOrZero):
    """Custom type tIPv6FilterParamsFwdLspRtrId based on TmnxVRtrIDOrZero"""
    defaultValue = 0


_TIPv6FilterParamsFwdLspRtrId_Type.__name__ = "TmnxVRtrIDOrZero"
_TIPv6FilterParamsFwdLspRtrId_Object = MibTableColumn
tIPv6FilterParamsFwdLspRtrId = _TIPv6FilterParamsFwdLspRtrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 60),
    _TIPv6FilterParamsFwdLspRtrId_Type()
)
tIPv6FilterParamsFwdLspRtrId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsFwdLspRtrId.setStatus("current")
_TFilterGroupInsertedEntries_ObjectIdentity = ObjectIdentity
tFilterGroupInsertedEntries = _TFilterGroupInsertedEntries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 20)
)


class _TFltrGrpInsrtdEntriesFilterType_Type(TFilterType):
    """Custom type tFltrGrpInsrtdEntriesFilterType based on TFilterType"""
    defaultValue = 0


_TFltrGrpInsrtdEntriesFilterType_Type.__name__ = "TFilterType"
_TFltrGrpInsrtdEntriesFilterType_Object = MibScalar
tFltrGrpInsrtdEntriesFilterType = _TFltrGrpInsrtdEntriesFilterType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 20, 1),
    _TFltrGrpInsrtdEntriesFilterType_Type()
)
tFltrGrpInsrtdEntriesFilterType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tFltrGrpInsrtdEntriesFilterType.setStatus("current")


class _TFltrGrpInsrtdEntriesFilterId_Type(TFilterID):
    """Custom type tFltrGrpInsrtdEntriesFilterId based on TFilterID"""
    defaultValue = 0


_TFltrGrpInsrtdEntriesFilterId_Type.__name__ = "TFilterID"
_TFltrGrpInsrtdEntriesFilterId_Object = MibScalar
tFltrGrpInsrtdEntriesFilterId = _TFltrGrpInsrtdEntriesFilterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 20, 2),
    _TFltrGrpInsrtdEntriesFilterId_Type()
)
tFltrGrpInsrtdEntriesFilterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tFltrGrpInsrtdEntriesFilterId.setStatus("current")


class _TFltrGrpInsrtdEntriesApplication_Type(TFilterSubInsSpaceOwner):
    """Custom type tFltrGrpInsrtdEntriesApplication based on TFilterSubInsSpaceOwner"""
    defaultValue = 0


_TFltrGrpInsrtdEntriesApplication_Type.__name__ = "TFilterSubInsSpaceOwner"
_TFltrGrpInsrtdEntriesApplication_Object = MibScalar
tFltrGrpInsrtdEntriesApplication = _TFltrGrpInsrtdEntriesApplication_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 20, 3),
    _TFltrGrpInsrtdEntriesApplication_Type()
)
tFltrGrpInsrtdEntriesApplication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tFltrGrpInsrtdEntriesApplication.setStatus("current")


class _TFltrGrpInsrtdEntriesLocation_Type(Integer32):
    """Custom type tFltrGrpInsrtdEntriesLocation based on Integer32"""
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
          ("top", 1),
          ("bottom", 2))
    )


_TFltrGrpInsrtdEntriesLocation_Type.__name__ = "Integer32"
_TFltrGrpInsrtdEntriesLocation_Object = MibScalar
tFltrGrpInsrtdEntriesLocation = _TFltrGrpInsrtdEntriesLocation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 20, 4),
    _TFltrGrpInsrtdEntriesLocation_Type()
)
tFltrGrpInsrtdEntriesLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tFltrGrpInsrtdEntriesLocation.setStatus("current")


class _TFltrGrpInsrtdEntriesResult_Type(Integer32):
    """Custom type tFltrGrpInsrtdEntriesResult based on Integer32"""
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
          ("success", 1),
          ("failure", 2))
    )


_TFltrGrpInsrtdEntriesResult_Type.__name__ = "Integer32"
_TFltrGrpInsrtdEntriesResult_Object = MibScalar
tFltrGrpInsrtdEntriesResult = _TFltrGrpInsrtdEntriesResult_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 20, 5),
    _TFltrGrpInsrtdEntriesResult_Type()
)
tFltrGrpInsrtdEntriesResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFltrGrpInsrtdEntriesResult.setStatus("current")


class _TFltrGrpInsrtdEntriesFeedback_Type(DisplayString):
    """Custom type tFltrGrpInsrtdEntriesFeedback based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_TFltrGrpInsrtdEntriesFeedback_Type.__name__ = "DisplayString"
_TFltrGrpInsrtdEntriesFeedback_Object = MibScalar
tFltrGrpInsrtdEntriesFeedback = _TFltrGrpInsrtdEntriesFeedback_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 20, 6),
    _TFltrGrpInsrtdEntriesFeedback_Type()
)
tFltrGrpInsrtdEntriesFeedback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFltrGrpInsrtdEntriesFeedback.setStatus("current")


class _TFltrGrpInsrtdEntriesExecute_Type(TruthValue):
    """Custom type tFltrGrpInsrtdEntriesExecute based on TruthValue"""
    defaultValue = 2


_TFltrGrpInsrtdEntriesExecute_Type.__name__ = "TruthValue"
_TFltrGrpInsrtdEntriesExecute_Object = MibScalar
tFltrGrpInsrtdEntriesExecute = _TFltrGrpInsrtdEntriesExecute_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 20, 7),
    _TFltrGrpInsrtdEntriesExecute_Type()
)
tFltrGrpInsrtdEntriesExecute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tFltrGrpInsrtdEntriesExecute.setStatus("current")
_TDhcpFilterTableLastChanged_Type = TimeStamp
_TDhcpFilterTableLastChanged_Object = MibScalar
tDhcpFilterTableLastChanged = _TDhcpFilterTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 21),
    _TDhcpFilterTableLastChanged_Type()
)
tDhcpFilterTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tDhcpFilterTableLastChanged.setStatus("current")
_TDhcpFilterTable_Object = MibTable
tDhcpFilterTable = _TDhcpFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 22)
)
if mibBuilder.loadTexts:
    tDhcpFilterTable.setStatus("current")
_TDhcpFilterEntry_Object = MibTableRow
tDhcpFilterEntry = _TDhcpFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 22, 1)
)
tDhcpFilterEntry.setIndexNames(
    (0, "TIMETRA-FILTER-MIB", "tDhcpFilterId"),
)
if mibBuilder.loadTexts:
    tDhcpFilterEntry.setStatus("current")


class _TDhcpFilterId_Type(TDHCPFilterID):
    """Custom type tDhcpFilterId based on TDHCPFilterID"""
    subtypeSpec = TDHCPFilterID.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TDhcpFilterId_Type.__name__ = "TDHCPFilterID"
_TDhcpFilterId_Object = MibTableColumn
tDhcpFilterId = _TDhcpFilterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 22, 1, 1),
    _TDhcpFilterId_Type()
)
tDhcpFilterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tDhcpFilterId.setStatus("current")
_TDhcpFilterRowStatus_Type = RowStatus
_TDhcpFilterRowStatus_Object = MibTableColumn
tDhcpFilterRowStatus = _TDhcpFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 22, 1, 2),
    _TDhcpFilterRowStatus_Type()
)
tDhcpFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tDhcpFilterRowStatus.setStatus("current")
_TDhcpFilterLastChanged_Type = TimeStamp
_TDhcpFilterLastChanged_Object = MibTableColumn
tDhcpFilterLastChanged = _TDhcpFilterLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 22, 1, 3),
    _TDhcpFilterLastChanged_Type()
)
tDhcpFilterLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tDhcpFilterLastChanged.setStatus("current")


class _TDhcpFilterDescription_Type(TItemDescription):
    """Custom type tDhcpFilterDescription based on TItemDescription"""
    defaultHexValue = ""


_TDhcpFilterDescription_Type.__name__ = "TItemDescription"
_TDhcpFilterDescription_Object = MibTableColumn
tDhcpFilterDescription = _TDhcpFilterDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 22, 1, 4),
    _TDhcpFilterDescription_Type()
)
tDhcpFilterDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tDhcpFilterDescription.setStatus("current")
_TDhcpFilterParamsTblLastChanged_Type = TimeStamp
_TDhcpFilterParamsTblLastChanged_Object = MibScalar
tDhcpFilterParamsTblLastChanged = _TDhcpFilterParamsTblLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 23),
    _TDhcpFilterParamsTblLastChanged_Type()
)
tDhcpFilterParamsTblLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tDhcpFilterParamsTblLastChanged.setStatus("current")
_TDhcpFilterParamsTable_Object = MibTable
tDhcpFilterParamsTable = _TDhcpFilterParamsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 24)
)
if mibBuilder.loadTexts:
    tDhcpFilterParamsTable.setStatus("current")
_TDhcpFilterParamsEntry_Object = MibTableRow
tDhcpFilterParamsEntry = _TDhcpFilterParamsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 24, 1)
)
tDhcpFilterParamsEntry.setIndexNames(
    (0, "TIMETRA-FILTER-MIB", "tDhcpFilterId"),
    (0, "TIMETRA-FILTER-MIB", "tDhcpFilterParamsId"),
)
if mibBuilder.loadTexts:
    tDhcpFilterParamsEntry.setStatus("current")
_TDhcpFilterParamsId_Type = TEntryId
_TDhcpFilterParamsId_Object = MibTableColumn
tDhcpFilterParamsId = _TDhcpFilterParamsId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 24, 1, 1),
    _TDhcpFilterParamsId_Type()
)
tDhcpFilterParamsId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tDhcpFilterParamsId.setStatus("current")
_TDhcpFilterParamsRowStatus_Type = RowStatus
_TDhcpFilterParamsRowStatus_Object = MibTableColumn
tDhcpFilterParamsRowStatus = _TDhcpFilterParamsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 24, 1, 2),
    _TDhcpFilterParamsRowStatus_Type()
)
tDhcpFilterParamsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tDhcpFilterParamsRowStatus.setStatus("current")
_TDhcpFilterParamsLastChanged_Type = TimeStamp
_TDhcpFilterParamsLastChanged_Object = MibTableColumn
tDhcpFilterParamsLastChanged = _TDhcpFilterParamsLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 24, 1, 3),
    _TDhcpFilterParamsLastChanged_Type()
)
tDhcpFilterParamsLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tDhcpFilterParamsLastChanged.setStatus("current")


class _TDhcpFilterParamsOptionNumber_Type(Integer32):
    """Custom type tDhcpFilterParamsOptionNumber based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 255),
    )


_TDhcpFilterParamsOptionNumber_Type.__name__ = "Integer32"
_TDhcpFilterParamsOptionNumber_Object = MibTableColumn
tDhcpFilterParamsOptionNumber = _TDhcpFilterParamsOptionNumber_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 24, 1, 4),
    _TDhcpFilterParamsOptionNumber_Type()
)
tDhcpFilterParamsOptionNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tDhcpFilterParamsOptionNumber.setStatus("current")


class _TDhcpFilterParamsOptionMatch_Type(TDhcpFilterMatch):
    """Custom type tDhcpFilterParamsOptionMatch based on TDhcpFilterMatch"""
    defaultValue = 1


_TDhcpFilterParamsOptionMatch_Type.__name__ = "TDhcpFilterMatch"
_TDhcpFilterParamsOptionMatch_Object = MibTableColumn
tDhcpFilterParamsOptionMatch = _TDhcpFilterParamsOptionMatch_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 24, 1, 5),
    _TDhcpFilterParamsOptionMatch_Type()
)
tDhcpFilterParamsOptionMatch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tDhcpFilterParamsOptionMatch.setStatus("current")


class _TDhcpFilterParamsAction_Type(TDhcpFilterAction):
    """Custom type tDhcpFilterParamsAction based on TDhcpFilterAction"""
    defaultValue = 1


_TDhcpFilterParamsAction_Type.__name__ = "TDhcpFilterAction"
_TDhcpFilterParamsAction_Object = MibTableColumn
tDhcpFilterParamsAction = _TDhcpFilterParamsAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 24, 1, 6),
    _TDhcpFilterParamsAction_Type()
)
tDhcpFilterParamsAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tDhcpFilterParamsAction.setStatus("current")


class _TDhcpFilterParamsOptionValue_Type(OctetString):
    """Custom type tDhcpFilterParamsOptionValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_TDhcpFilterParamsOptionValue_Type.__name__ = "OctetString"
_TDhcpFilterParamsOptionValue_Object = MibTableColumn
tDhcpFilterParamsOptionValue = _TDhcpFilterParamsOptionValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 24, 1, 7),
    _TDhcpFilterParamsOptionValue_Type()
)
tDhcpFilterParamsOptionValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tDhcpFilterParamsOptionValue.setStatus("current")
_TMacFilterNameTableLastChgd_Type = TimeStamp
_TMacFilterNameTableLastChgd_Object = MibScalar
tMacFilterNameTableLastChgd = _TMacFilterNameTableLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 25),
    _TMacFilterNameTableLastChgd_Type()
)
tMacFilterNameTableLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMacFilterNameTableLastChgd.setStatus("current")
_TMacFilterNameTable_Object = MibTable
tMacFilterNameTable = _TMacFilterNameTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 26)
)
if mibBuilder.loadTexts:
    tMacFilterNameTable.setStatus("current")
_TMacFilterNameEntry_Object = MibTableRow
tMacFilterNameEntry = _TMacFilterNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 26, 1)
)
tMacFilterNameEntry.setIndexNames(
    (0, "TIMETRA-FILTER-MIB", "tMacFilterName"),
)
if mibBuilder.loadTexts:
    tMacFilterNameEntry.setStatus("current")
_TMacFilterNameId_Type = TAnyFilterID
_TMacFilterNameId_Object = MibTableColumn
tMacFilterNameId = _TMacFilterNameId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 26, 1, 1),
    _TMacFilterNameId_Type()
)
tMacFilterNameId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMacFilterNameId.setStatus("current")
_TMacFilterNameRowStatus_Type = RowStatus
_TMacFilterNameRowStatus_Object = MibTableColumn
tMacFilterNameRowStatus = _TMacFilterNameRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 26, 1, 2),
    _TMacFilterNameRowStatus_Type()
)
tMacFilterNameRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMacFilterNameRowStatus.setStatus("current")
_TMacFilterNameLastChanged_Type = TimeStamp
_TMacFilterNameLastChanged_Object = MibTableColumn
tMacFilterNameLastChanged = _TMacFilterNameLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 26, 1, 3),
    _TMacFilterNameLastChanged_Type()
)
tMacFilterNameLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMacFilterNameLastChanged.setStatus("current")
_TIpFilterNameTableLastChgd_Type = TimeStamp
_TIpFilterNameTableLastChgd_Object = MibScalar
tIpFilterNameTableLastChgd = _TIpFilterNameTableLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 27),
    _TIpFilterNameTableLastChgd_Type()
)
tIpFilterNameTableLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIpFilterNameTableLastChgd.setStatus("current")
_TIpFilterNameTable_Object = MibTable
tIpFilterNameTable = _TIpFilterNameTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 28)
)
if mibBuilder.loadTexts:
    tIpFilterNameTable.setStatus("current")
_TIpFilterNameEntry_Object = MibTableRow
tIpFilterNameEntry = _TIpFilterNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 28, 1)
)
tIpFilterNameEntry.setIndexNames(
    (0, "TIMETRA-FILTER-MIB", "tIpFilterName"),
)
if mibBuilder.loadTexts:
    tIpFilterNameEntry.setStatus("current")
_TIpFilterNameId_Type = TAnyFilterID
_TIpFilterNameId_Object = MibTableColumn
tIpFilterNameId = _TIpFilterNameId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 28, 1, 1),
    _TIpFilterNameId_Type()
)
tIpFilterNameId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIpFilterNameId.setStatus("current")
_TIpFilterNameRowStatus_Type = RowStatus
_TIpFilterNameRowStatus_Object = MibTableColumn
tIpFilterNameRowStatus = _TIpFilterNameRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 28, 1, 2),
    _TIpFilterNameRowStatus_Type()
)
tIpFilterNameRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIpFilterNameRowStatus.setStatus("current")
_TIpFilterNameLastChanged_Type = TimeStamp
_TIpFilterNameLastChanged_Object = MibTableColumn
tIpFilterNameLastChanged = _TIpFilterNameLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 28, 1, 3),
    _TIpFilterNameLastChanged_Type()
)
tIpFilterNameLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIpFilterNameLastChanged.setStatus("current")
_TIpv6FilterNameTableLastChgd_Type = TimeStamp
_TIpv6FilterNameTableLastChgd_Object = MibScalar
tIpv6FilterNameTableLastChgd = _TIpv6FilterNameTableLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 29),
    _TIpv6FilterNameTableLastChgd_Type()
)
tIpv6FilterNameTableLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIpv6FilterNameTableLastChgd.setStatus("current")
_TIpv6FilterNameTable_Object = MibTable
tIpv6FilterNameTable = _TIpv6FilterNameTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 30)
)
if mibBuilder.loadTexts:
    tIpv6FilterNameTable.setStatus("current")
_TIpv6FilterNameEntry_Object = MibTableRow
tIpv6FilterNameEntry = _TIpv6FilterNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 30, 1)
)
tIpv6FilterNameEntry.setIndexNames(
    (0, "TIMETRA-FILTER-MIB", "tIpv6FilterName"),
)
if mibBuilder.loadTexts:
    tIpv6FilterNameEntry.setStatus("current")
_TIpv6FilterNameId_Type = TAnyFilterID
_TIpv6FilterNameId_Object = MibTableColumn
tIpv6FilterNameId = _TIpv6FilterNameId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 30, 1, 1),
    _TIpv6FilterNameId_Type()
)
tIpv6FilterNameId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIpv6FilterNameId.setStatus("current")
_TIpv6FilterNameRowStatus_Type = RowStatus
_TIpv6FilterNameRowStatus_Object = MibTableColumn
tIpv6FilterNameRowStatus = _TIpv6FilterNameRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 30, 1, 2),
    _TIpv6FilterNameRowStatus_Type()
)
tIpv6FilterNameRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIpv6FilterNameRowStatus.setStatus("current")
_TIpv6FilterNameLastChanged_Type = TimeStamp
_TIpv6FilterNameLastChanged_Object = MibTableColumn
tIpv6FilterNameLastChanged = _TIpv6FilterNameLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 30, 1, 3),
    _TIpv6FilterNameLastChanged_Type()
)
tIpv6FilterNameLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIpv6FilterNameLastChanged.setStatus("current")
_TFilterLiObjects_ObjectIdentity = ObjectIdentity
tFilterLiObjects = _TFilterLiObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31)
)
_TLiReservedBlockTableLastChanged_Type = TimeStamp
_TLiReservedBlockTableLastChanged_Object = MibScalar
tLiReservedBlockTableLastChanged = _TLiReservedBlockTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 1),
    _TLiReservedBlockTableLastChanged_Type()
)
tLiReservedBlockTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tLiReservedBlockTableLastChanged.setStatus("current")
_TLiReservedBlockTable_Object = MibTable
tLiReservedBlockTable = _TLiReservedBlockTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 2)
)
if mibBuilder.loadTexts:
    tLiReservedBlockTable.setStatus("current")
_TLiReservedBlockEntry_Object = MibTableRow
tLiReservedBlockEntry = _TLiReservedBlockEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 2, 1)
)
tLiReservedBlockEntry.setIndexNames(
    (0, "TIMETRA-FILTER-MIB", "tLiReservedBlockName"),
)
if mibBuilder.loadTexts:
    tLiReservedBlockEntry.setStatus("current")
_TLiReservedBlockName_Type = TNamedItem
_TLiReservedBlockName_Object = MibTableColumn
tLiReservedBlockName = _TLiReservedBlockName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 2, 1, 1),
    _TLiReservedBlockName_Type()
)
tLiReservedBlockName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tLiReservedBlockName.setStatus("current")
_TLiReservedBlockRowStatus_Type = RowStatus
_TLiReservedBlockRowStatus_Object = MibTableColumn
tLiReservedBlockRowStatus = _TLiReservedBlockRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 2, 1, 2),
    _TLiReservedBlockRowStatus_Type()
)
tLiReservedBlockRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLiReservedBlockRowStatus.setStatus("current")
_TLiReservedBlockLastChanged_Type = TimeStamp
_TLiReservedBlockLastChanged_Object = MibTableColumn
tLiReservedBlockLastChanged = _TLiReservedBlockLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 2, 1, 3),
    _TLiReservedBlockLastChanged_Type()
)
tLiReservedBlockLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tLiReservedBlockLastChanged.setStatus("current")


class _TLiReservedBlockDescription_Type(TItemDescription):
    """Custom type tLiReservedBlockDescription based on TItemDescription"""
    defaultHexValue = ""


_TLiReservedBlockDescription_Type.__name__ = "TItemDescription"
_TLiReservedBlockDescription_Object = MibTableColumn
tLiReservedBlockDescription = _TLiReservedBlockDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 2, 1, 4),
    _TLiReservedBlockDescription_Type()
)
tLiReservedBlockDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLiReservedBlockDescription.setStatus("current")


class _TLiReservedBlockStart_Type(TEntryIdOrZero):
    """Custom type tLiReservedBlockStart based on TEntryIdOrZero"""
    defaultValue = 0


_TLiReservedBlockStart_Type.__name__ = "TEntryIdOrZero"
_TLiReservedBlockStart_Object = MibTableColumn
tLiReservedBlockStart = _TLiReservedBlockStart_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 2, 1, 5),
    _TLiReservedBlockStart_Type()
)
tLiReservedBlockStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLiReservedBlockStart.setStatus("current")


class _TLiReservedBlockSize_Type(TEntryIdOrZero):
    """Custom type tLiReservedBlockSize based on TEntryIdOrZero"""
    defaultValue = 0

    subtypeSpec = TEntryIdOrZero.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8192),
    )


_TLiReservedBlockSize_Type.__name__ = "TEntryIdOrZero"
_TLiReservedBlockSize_Object = MibTableColumn
tLiReservedBlockSize = _TLiReservedBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 2, 1, 6),
    _TLiReservedBlockSize_Type()
)
tLiReservedBlockSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLiReservedBlockSize.setStatus("current")
_TLiReservedBlockFltrTableLastChg_Type = TimeStamp
_TLiReservedBlockFltrTableLastChg_Object = MibScalar
tLiReservedBlockFltrTableLastChg = _TLiReservedBlockFltrTableLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 3),
    _TLiReservedBlockFltrTableLastChg_Type()
)
tLiReservedBlockFltrTableLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tLiReservedBlockFltrTableLastChg.setStatus("current")
_TLiReservedBlockFltrTable_Object = MibTable
tLiReservedBlockFltrTable = _TLiReservedBlockFltrTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 4)
)
if mibBuilder.loadTexts:
    tLiReservedBlockFltrTable.setStatus("current")
_TLiReservedBlockFltrEntry_Object = MibTableRow
tLiReservedBlockFltrEntry = _TLiReservedBlockFltrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 4, 1)
)
tLiReservedBlockFltrEntry.setIndexNames(
    (0, "TIMETRA-FILTER-MIB", "tLiReservedBlockName"),
    (0, "TIMETRA-FILTER-MIB", "tLiReservedBlockFltrType"),
    (0, "TIMETRA-FILTER-MIB", "tLiReservedBlockFltrIdStart"),
    (0, "TIMETRA-FILTER-MIB", "tLiReservedBlockFltrIdEnd"),
)
if mibBuilder.loadTexts:
    tLiReservedBlockFltrEntry.setStatus("current")
_TLiReservedBlockFltrType_Type = TFilterType
_TLiReservedBlockFltrType_Object = MibTableColumn
tLiReservedBlockFltrType = _TLiReservedBlockFltrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 4, 1, 1),
    _TLiReservedBlockFltrType_Type()
)
tLiReservedBlockFltrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tLiReservedBlockFltrType.setStatus("current")
_TLiReservedBlockFltrIdStart_Type = TFilterID
_TLiReservedBlockFltrIdStart_Object = MibTableColumn
tLiReservedBlockFltrIdStart = _TLiReservedBlockFltrIdStart_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 4, 1, 2),
    _TLiReservedBlockFltrIdStart_Type()
)
tLiReservedBlockFltrIdStart.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tLiReservedBlockFltrIdStart.setStatus("current")
_TLiReservedBlockFltrIdEnd_Type = TFilterID
_TLiReservedBlockFltrIdEnd_Object = MibTableColumn
tLiReservedBlockFltrIdEnd = _TLiReservedBlockFltrIdEnd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 4, 1, 3),
    _TLiReservedBlockFltrIdEnd_Type()
)
tLiReservedBlockFltrIdEnd.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tLiReservedBlockFltrIdEnd.setStatus("current")
_TLiReservedBlockFltrRowStatus_Type = RowStatus
_TLiReservedBlockFltrRowStatus_Object = MibTableColumn
tLiReservedBlockFltrRowStatus = _TLiReservedBlockFltrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 4, 1, 4),
    _TLiReservedBlockFltrRowStatus_Type()
)
tLiReservedBlockFltrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLiReservedBlockFltrRowStatus.setStatus("current")
_TLiReservedBlockFltrLastChanged_Type = TimeStamp
_TLiReservedBlockFltrLastChanged_Object = MibTableColumn
tLiReservedBlockFltrLastChanged = _TLiReservedBlockFltrLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 4, 1, 5),
    _TLiReservedBlockFltrLastChanged_Type()
)
tLiReservedBlockFltrLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tLiReservedBlockFltrLastChanged.setStatus("current")
_TLiFilterTableLastChanged_Type = TimeStamp
_TLiFilterTableLastChanged_Object = MibScalar
tLiFilterTableLastChanged = _TLiFilterTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 5),
    _TLiFilterTableLastChanged_Type()
)
tLiFilterTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tLiFilterTableLastChanged.setStatus("current")
_TLiFilterTable_Object = MibTable
tLiFilterTable = _TLiFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 6)
)
if mibBuilder.loadTexts:
    tLiFilterTable.setStatus("current")
_TLiFilterEntry_Object = MibTableRow
tLiFilterEntry = _TLiFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 6, 1)
)
tLiFilterEntry.setIndexNames(
    (0, "TIMETRA-FILTER-MIB", "tLiFilterType"),
    (0, "TIMETRA-FILTER-MIB", "tLiFilterName"),
)
if mibBuilder.loadTexts:
    tLiFilterEntry.setStatus("current")
_TLiFilterType_Type = TFilterType
_TLiFilterType_Object = MibTableColumn
tLiFilterType = _TLiFilterType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 6, 1, 1),
    _TLiFilterType_Type()
)
tLiFilterType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tLiFilterType.setStatus("current")
_TLiFilterName_Type = TNamedItem
_TLiFilterName_Object = MibTableColumn
tLiFilterName = _TLiFilterName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 6, 1, 2),
    _TLiFilterName_Type()
)
tLiFilterName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tLiFilterName.setStatus("current")
_TLiFilterRowStatus_Type = RowStatus
_TLiFilterRowStatus_Object = MibTableColumn
tLiFilterRowStatus = _TLiFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 6, 1, 3),
    _TLiFilterRowStatus_Type()
)
tLiFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLiFilterRowStatus.setStatus("current")
_TLiFilterLastChanged_Type = TimeStamp
_TLiFilterLastChanged_Object = MibTableColumn
tLiFilterLastChanged = _TLiFilterLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 6, 1, 4),
    _TLiFilterLastChanged_Type()
)
tLiFilterLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tLiFilterLastChanged.setStatus("current")


class _TLiFilterDescription_Type(TItemDescription):
    """Custom type tLiFilterDescription based on TItemDescription"""
    defaultHexValue = ""


_TLiFilterDescription_Type.__name__ = "TItemDescription"
_TLiFilterDescription_Object = MibTableColumn
tLiFilterDescription = _TLiFilterDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 6, 1, 5),
    _TLiFilterDescription_Type()
)
tLiFilterDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLiFilterDescription.setStatus("current")
_TLiFilterAssociationTableLastChg_Type = TimeStamp
_TLiFilterAssociationTableLastChg_Object = MibScalar
tLiFilterAssociationTableLastChg = _TLiFilterAssociationTableLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 7),
    _TLiFilterAssociationTableLastChg_Type()
)
tLiFilterAssociationTableLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tLiFilterAssociationTableLastChg.setStatus("current")
_TLiFilterAssociationTable_Object = MibTable
tLiFilterAssociationTable = _TLiFilterAssociationTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 8)
)
if mibBuilder.loadTexts:
    tLiFilterAssociationTable.setStatus("current")
_TLiFilterAssociationEntry_Object = MibTableRow
tLiFilterAssociationEntry = _TLiFilterAssociationEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 8, 1)
)
tLiFilterAssociationEntry.setIndexNames(
    (0, "TIMETRA-FILTER-MIB", "tLiFilterType"),
    (0, "TIMETRA-FILTER-MIB", "tLiFilterName"),
    (0, "TIMETRA-FILTER-MIB", "tLiFilterAssociationFltrId"),
)
if mibBuilder.loadTexts:
    tLiFilterAssociationEntry.setStatus("current")
_TLiFilterAssociationFltrId_Type = TFilterID
_TLiFilterAssociationFltrId_Object = MibTableColumn
tLiFilterAssociationFltrId = _TLiFilterAssociationFltrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 8, 1, 1),
    _TLiFilterAssociationFltrId_Type()
)
tLiFilterAssociationFltrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tLiFilterAssociationFltrId.setStatus("current")
_TLiFilterAssociationRowStatus_Type = RowStatus
_TLiFilterAssociationRowStatus_Object = MibTableColumn
tLiFilterAssociationRowStatus = _TLiFilterAssociationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 8, 1, 2),
    _TLiFilterAssociationRowStatus_Type()
)
tLiFilterAssociationRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLiFilterAssociationRowStatus.setStatus("current")
_TLiFilterAssociationLastChg_Type = TimeStamp
_TLiFilterAssociationLastChg_Object = MibTableColumn
tLiFilterAssociationLastChg = _TLiFilterAssociationLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 8, 1, 3),
    _TLiFilterAssociationLastChg_Type()
)
tLiFilterAssociationLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tLiFilterAssociationLastChg.setStatus("current")
_TLiMacFilterParamsTableLastChg_Type = TimeStamp
_TLiMacFilterParamsTableLastChg_Object = MibScalar
tLiMacFilterParamsTableLastChg = _TLiMacFilterParamsTableLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 9),
    _TLiMacFilterParamsTableLastChg_Type()
)
tLiMacFilterParamsTableLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tLiMacFilterParamsTableLastChg.setStatus("current")
_TLiMacFilterParamsTable_Object = MibTable
tLiMacFilterParamsTable = _TLiMacFilterParamsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 10)
)
if mibBuilder.loadTexts:
    tLiMacFilterParamsTable.setStatus("current")
_TLiMacFilterParamsEntry_Object = MibTableRow
tLiMacFilterParamsEntry = _TLiMacFilterParamsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 10, 1)
)
tLiMacFilterParamsEntry.setIndexNames(
    (0, "TIMETRA-FILTER-MIB", "tLiFilterType"),
    (0, "TIMETRA-FILTER-MIB", "tLiFilterName"),
    (0, "TIMETRA-FILTER-MIB", "tLiMacFilterParamsId"),
)
if mibBuilder.loadTexts:
    tLiMacFilterParamsEntry.setStatus("current")
_TLiMacFilterParamsId_Type = TEntryId
_TLiMacFilterParamsId_Object = MibTableColumn
tLiMacFilterParamsId = _TLiMacFilterParamsId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 10, 1, 1),
    _TLiMacFilterParamsId_Type()
)
tLiMacFilterParamsId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tLiMacFilterParamsId.setStatus("current")
_TLiMacFilterParamsRowStatus_Type = RowStatus
_TLiMacFilterParamsRowStatus_Object = MibTableColumn
tLiMacFilterParamsRowStatus = _TLiMacFilterParamsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 10, 1, 2),
    _TLiMacFilterParamsRowStatus_Type()
)
tLiMacFilterParamsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLiMacFilterParamsRowStatus.setStatus("current")
_TLiMacFilterParamsLastChanged_Type = TimeStamp
_TLiMacFilterParamsLastChanged_Object = MibTableColumn
tLiMacFilterParamsLastChanged = _TLiMacFilterParamsLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 10, 1, 3),
    _TLiMacFilterParamsLastChanged_Type()
)
tLiMacFilterParamsLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tLiMacFilterParamsLastChanged.setStatus("current")


class _TLiMacFilterParamsDescription_Type(TItemDescription):
    """Custom type tLiMacFilterParamsDescription based on TItemDescription"""
    defaultHexValue = ""


_TLiMacFilterParamsDescription_Type.__name__ = "TItemDescription"
_TLiMacFilterParamsDescription_Object = MibTableColumn
tLiMacFilterParamsDescription = _TLiMacFilterParamsDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 10, 1, 4),
    _TLiMacFilterParamsDescription_Type()
)
tLiMacFilterParamsDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLiMacFilterParamsDescription.setStatus("current")


class _TLiMacFilterParamsFrameType_Type(TFrameType):
    """Custom type tLiMacFilterParamsFrameType based on TFrameType"""
    defaultValue = 0


_TLiMacFilterParamsFrameType_Type.__name__ = "TFrameType"
_TLiMacFilterParamsFrameType_Object = MibTableColumn
tLiMacFilterParamsFrameType = _TLiMacFilterParamsFrameType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 10, 1, 5),
    _TLiMacFilterParamsFrameType_Type()
)
tLiMacFilterParamsFrameType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLiMacFilterParamsFrameType.setStatus("current")


class _TLiMacFilterParamsSrcMAC_Type(MacAddress):
    """Custom type tLiMacFilterParamsSrcMAC based on MacAddress"""
    defaultHexValue = "000000000000"


_TLiMacFilterParamsSrcMAC_Type.__name__ = "MacAddress"
_TLiMacFilterParamsSrcMAC_Object = MibTableColumn
tLiMacFilterParamsSrcMAC = _TLiMacFilterParamsSrcMAC_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 10, 1, 6),
    _TLiMacFilterParamsSrcMAC_Type()
)
tLiMacFilterParamsSrcMAC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLiMacFilterParamsSrcMAC.setStatus("current")


class _TLiMacFilterParamsSrcMACMask_Type(MacAddress):
    """Custom type tLiMacFilterParamsSrcMACMask based on MacAddress"""
    defaultHexValue = "000000000000"


_TLiMacFilterParamsSrcMACMask_Type.__name__ = "MacAddress"
_TLiMacFilterParamsSrcMACMask_Object = MibTableColumn
tLiMacFilterParamsSrcMACMask = _TLiMacFilterParamsSrcMACMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 10, 1, 7),
    _TLiMacFilterParamsSrcMACMask_Type()
)
tLiMacFilterParamsSrcMACMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLiMacFilterParamsSrcMACMask.setStatus("current")


class _TLiMacFilterParamsDstMAC_Type(MacAddress):
    """Custom type tLiMacFilterParamsDstMAC based on MacAddress"""
    defaultHexValue = "000000000000"


_TLiMacFilterParamsDstMAC_Type.__name__ = "MacAddress"
_TLiMacFilterParamsDstMAC_Object = MibTableColumn
tLiMacFilterParamsDstMAC = _TLiMacFilterParamsDstMAC_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 10, 1, 8),
    _TLiMacFilterParamsDstMAC_Type()
)
tLiMacFilterParamsDstMAC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLiMacFilterParamsDstMAC.setStatus("current")


class _TLiMacFilterParamsDstMACMask_Type(MacAddress):
    """Custom type tLiMacFilterParamsDstMACMask based on MacAddress"""
    defaultHexValue = "000000000000"


_TLiMacFilterParamsDstMACMask_Type.__name__ = "MacAddress"
_TLiMacFilterParamsDstMACMask_Object = MibTableColumn
tLiMacFilterParamsDstMACMask = _TLiMacFilterParamsDstMACMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 10, 1, 9),
    _TLiMacFilterParamsDstMACMask_Type()
)
tLiMacFilterParamsDstMACMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLiMacFilterParamsDstMACMask.setStatus("current")
_TLiMacFilterParamsIngrHitCount_Type = Counter64
_TLiMacFilterParamsIngrHitCount_Object = MibTableColumn
tLiMacFilterParamsIngrHitCount = _TLiMacFilterParamsIngrHitCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 10, 1, 10),
    _TLiMacFilterParamsIngrHitCount_Type()
)
tLiMacFilterParamsIngrHitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tLiMacFilterParamsIngrHitCount.setStatus("current")
_TLiMacFilterParamsEgrHitCount_Type = Counter64
_TLiMacFilterParamsEgrHitCount_Object = MibTableColumn
tLiMacFilterParamsEgrHitCount = _TLiMacFilterParamsEgrHitCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 10, 1, 11),
    _TLiMacFilterParamsEgrHitCount_Type()
)
tLiMacFilterParamsEgrHitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tLiMacFilterParamsEgrHitCount.setStatus("current")
_TLiMacFilterParamsIngrHitBytes_Type = Counter64
_TLiMacFilterParamsIngrHitBytes_Object = MibTableColumn
tLiMacFilterParamsIngrHitBytes = _TLiMacFilterParamsIngrHitBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 10, 1, 12),
    _TLiMacFilterParamsIngrHitBytes_Type()
)
tLiMacFilterParamsIngrHitBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tLiMacFilterParamsIngrHitBytes.setStatus("current")
_TLiMacFilterParamsEgrHitBytes_Type = Counter64
_TLiMacFilterParamsEgrHitBytes_Object = MibTableColumn
tLiMacFilterParamsEgrHitBytes = _TLiMacFilterParamsEgrHitBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 10, 1, 13),
    _TLiMacFilterParamsEgrHitBytes_Type()
)
tLiMacFilterParamsEgrHitBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tLiMacFilterParamsEgrHitBytes.setStatus("current")
_TLiIpFilterParamsTableLastChg_Type = TimeStamp
_TLiIpFilterParamsTableLastChg_Object = MibScalar
tLiIpFilterParamsTableLastChg = _TLiIpFilterParamsTableLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 15),
    _TLiIpFilterParamsTableLastChg_Type()
)
tLiIpFilterParamsTableLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tLiIpFilterParamsTableLastChg.setStatus("current")
_TLiIpFilterParamsTable_Object = MibTable
tLiIpFilterParamsTable = _TLiIpFilterParamsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 16)
)
if mibBuilder.loadTexts:
    tLiIpFilterParamsTable.setStatus("current")
_TLiIpFilterParamsEntry_Object = MibTableRow
tLiIpFilterParamsEntry = _TLiIpFilterParamsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 16, 1)
)
tLiIpFilterParamsEntry.setIndexNames(
    (0, "TIMETRA-FILTER-MIB", "tLiFilterType"),
    (0, "TIMETRA-FILTER-MIB", "tLiFilterName"),
    (0, "TIMETRA-FILTER-MIB", "tLiIpFilterParamsId"),
)
if mibBuilder.loadTexts:
    tLiIpFilterParamsEntry.setStatus("current")
_TLiIpFilterParamsId_Type = TEntryId
_TLiIpFilterParamsId_Object = MibTableColumn
tLiIpFilterParamsId = _TLiIpFilterParamsId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 16, 1, 1),
    _TLiIpFilterParamsId_Type()
)
tLiIpFilterParamsId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tLiIpFilterParamsId.setStatus("current")
_TLiIpFilterParamsLastChanged_Type = TimeStamp
_TLiIpFilterParamsLastChanged_Object = MibTableColumn
tLiIpFilterParamsLastChanged = _TLiIpFilterParamsLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 16, 1, 2),
    _TLiIpFilterParamsLastChanged_Type()
)
tLiIpFilterParamsLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tLiIpFilterParamsLastChanged.setStatus("current")
_TLiIpFilterParamsRowStatus_Type = RowStatus
_TLiIpFilterParamsRowStatus_Object = MibTableColumn
tLiIpFilterParamsRowStatus = _TLiIpFilterParamsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 16, 1, 3),
    _TLiIpFilterParamsRowStatus_Type()
)
tLiIpFilterParamsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLiIpFilterParamsRowStatus.setStatus("current")


class _TLiIpFilterParamsDescription_Type(TItemDescription):
    """Custom type tLiIpFilterParamsDescription based on TItemDescription"""
    defaultHexValue = ""


_TLiIpFilterParamsDescription_Type.__name__ = "TItemDescription"
_TLiIpFilterParamsDescription_Object = MibTableColumn
tLiIpFilterParamsDescription = _TLiIpFilterParamsDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 16, 1, 4),
    _TLiIpFilterParamsDescription_Type()
)
tLiIpFilterParamsDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLiIpFilterParamsDescription.setStatus("current")


class _TLiIpFilterParamsSrcIpAddrType_Type(InetAddressType):
    """Custom type tLiIpFilterParamsSrcIpAddrType based on InetAddressType"""
    defaultValue = 0


_TLiIpFilterParamsSrcIpAddrType_Type.__name__ = "InetAddressType"
_TLiIpFilterParamsSrcIpAddrType_Object = MibTableColumn
tLiIpFilterParamsSrcIpAddrType = _TLiIpFilterParamsSrcIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 16, 1, 5),
    _TLiIpFilterParamsSrcIpAddrType_Type()
)
tLiIpFilterParamsSrcIpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLiIpFilterParamsSrcIpAddrType.setStatus("current")


class _TLiIpFilterParamsSrcIpAddr_Type(InetAddress):
    """Custom type tLiIpFilterParamsSrcIpAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TLiIpFilterParamsSrcIpAddr_Type.__name__ = "InetAddress"
_TLiIpFilterParamsSrcIpAddr_Object = MibTableColumn
tLiIpFilterParamsSrcIpAddr = _TLiIpFilterParamsSrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 16, 1, 6),
    _TLiIpFilterParamsSrcIpAddr_Type()
)
tLiIpFilterParamsSrcIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLiIpFilterParamsSrcIpAddr.setStatus("current")


class _TLiIpFilterParamsSrcIpFullMask_Type(InetAddress):
    """Custom type tLiIpFilterParamsSrcIpFullMask based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TLiIpFilterParamsSrcIpFullMask_Type.__name__ = "InetAddress"
_TLiIpFilterParamsSrcIpFullMask_Object = MibTableColumn
tLiIpFilterParamsSrcIpFullMask = _TLiIpFilterParamsSrcIpFullMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 16, 1, 7),
    _TLiIpFilterParamsSrcIpFullMask_Type()
)
tLiIpFilterParamsSrcIpFullMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLiIpFilterParamsSrcIpFullMask.setStatus("current")


class _TLiIpFilterParamsDstIpAddrType_Type(InetAddressType):
    """Custom type tLiIpFilterParamsDstIpAddrType based on InetAddressType"""
    defaultValue = 0


_TLiIpFilterParamsDstIpAddrType_Type.__name__ = "InetAddressType"
_TLiIpFilterParamsDstIpAddrType_Object = MibTableColumn
tLiIpFilterParamsDstIpAddrType = _TLiIpFilterParamsDstIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 16, 1, 8),
    _TLiIpFilterParamsDstIpAddrType_Type()
)
tLiIpFilterParamsDstIpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLiIpFilterParamsDstIpAddrType.setStatus("current")


class _TLiIpFilterParamsDstIpAddr_Type(InetAddress):
    """Custom type tLiIpFilterParamsDstIpAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TLiIpFilterParamsDstIpAddr_Type.__name__ = "InetAddress"
_TLiIpFilterParamsDstIpAddr_Object = MibTableColumn
tLiIpFilterParamsDstIpAddr = _TLiIpFilterParamsDstIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 16, 1, 9),
    _TLiIpFilterParamsDstIpAddr_Type()
)
tLiIpFilterParamsDstIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLiIpFilterParamsDstIpAddr.setStatus("current")


class _TLiIpFilterParamsDstIpFullMask_Type(InetAddress):
    """Custom type tLiIpFilterParamsDstIpFullMask based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TLiIpFilterParamsDstIpFullMask_Type.__name__ = "InetAddress"
_TLiIpFilterParamsDstIpFullMask_Object = MibTableColumn
tLiIpFilterParamsDstIpFullMask = _TLiIpFilterParamsDstIpFullMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 16, 1, 10),
    _TLiIpFilterParamsDstIpFullMask_Type()
)
tLiIpFilterParamsDstIpFullMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLiIpFilterParamsDstIpFullMask.setStatus("current")


class _TLiIpFilterParamsProtocolNextHdr_Type(TIpProtocol):
    """Custom type tLiIpFilterParamsProtocolNextHdr based on TIpProtocol"""
    defaultValue = -1


_TLiIpFilterParamsProtocolNextHdr_Type.__name__ = "TIpProtocol"
_TLiIpFilterParamsProtocolNextHdr_Object = MibTableColumn
tLiIpFilterParamsProtocolNextHdr = _TLiIpFilterParamsProtocolNextHdr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 16, 1, 11),
    _TLiIpFilterParamsProtocolNextHdr_Type()
)
tLiIpFilterParamsProtocolNextHdr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLiIpFilterParamsProtocolNextHdr.setStatus("current")


class _TLiIpFilterParamsSrcPortValue1_Type(TTcpUdpPort):
    """Custom type tLiIpFilterParamsSrcPortValue1 based on TTcpUdpPort"""
    defaultValue = 0


_TLiIpFilterParamsSrcPortValue1_Type.__name__ = "TTcpUdpPort"
_TLiIpFilterParamsSrcPortValue1_Object = MibTableColumn
tLiIpFilterParamsSrcPortValue1 = _TLiIpFilterParamsSrcPortValue1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 16, 1, 12),
    _TLiIpFilterParamsSrcPortValue1_Type()
)
tLiIpFilterParamsSrcPortValue1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLiIpFilterParamsSrcPortValue1.setStatus("current")


class _TLiIpFilterParamsSrcPortValue2_Type(TTcpUdpPort):
    """Custom type tLiIpFilterParamsSrcPortValue2 based on TTcpUdpPort"""
    defaultValue = 0


_TLiIpFilterParamsSrcPortValue2_Type.__name__ = "TTcpUdpPort"
_TLiIpFilterParamsSrcPortValue2_Object = MibTableColumn
tLiIpFilterParamsSrcPortValue2 = _TLiIpFilterParamsSrcPortValue2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 16, 1, 13),
    _TLiIpFilterParamsSrcPortValue2_Type()
)
tLiIpFilterParamsSrcPortValue2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLiIpFilterParamsSrcPortValue2.setStatus("current")


class _TLiIpFilterParamsSrcPortOper_Type(TTcpUdpPortOperator):
    """Custom type tLiIpFilterParamsSrcPortOper based on TTcpUdpPortOperator"""
    defaultValue = 0


_TLiIpFilterParamsSrcPortOper_Type.__name__ = "TTcpUdpPortOperator"
_TLiIpFilterParamsSrcPortOper_Object = MibTableColumn
tLiIpFilterParamsSrcPortOper = _TLiIpFilterParamsSrcPortOper_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 16, 1, 14),
    _TLiIpFilterParamsSrcPortOper_Type()
)
tLiIpFilterParamsSrcPortOper.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLiIpFilterParamsSrcPortOper.setStatus("current")


class _TLiIpFilterParamsDstPortValue1_Type(TTcpUdpPort):
    """Custom type tLiIpFilterParamsDstPortValue1 based on TTcpUdpPort"""
    defaultValue = 0


_TLiIpFilterParamsDstPortValue1_Type.__name__ = "TTcpUdpPort"
_TLiIpFilterParamsDstPortValue1_Object = MibTableColumn
tLiIpFilterParamsDstPortValue1 = _TLiIpFilterParamsDstPortValue1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 16, 1, 15),
    _TLiIpFilterParamsDstPortValue1_Type()
)
tLiIpFilterParamsDstPortValue1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLiIpFilterParamsDstPortValue1.setStatus("current")


class _TLiIpFilterParamsDstPortValue2_Type(TTcpUdpPort):
    """Custom type tLiIpFilterParamsDstPortValue2 based on TTcpUdpPort"""
    defaultValue = 0


_TLiIpFilterParamsDstPortValue2_Type.__name__ = "TTcpUdpPort"
_TLiIpFilterParamsDstPortValue2_Object = MibTableColumn
tLiIpFilterParamsDstPortValue2 = _TLiIpFilterParamsDstPortValue2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 16, 1, 16),
    _TLiIpFilterParamsDstPortValue2_Type()
)
tLiIpFilterParamsDstPortValue2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLiIpFilterParamsDstPortValue2.setStatus("current")


class _TLiIpFilterParamsDstPortOper_Type(TTcpUdpPortOperator):
    """Custom type tLiIpFilterParamsDstPortOper based on TTcpUdpPortOperator"""
    defaultValue = 0


_TLiIpFilterParamsDstPortOper_Type.__name__ = "TTcpUdpPortOperator"
_TLiIpFilterParamsDstPortOper_Object = MibTableColumn
tLiIpFilterParamsDstPortOper = _TLiIpFilterParamsDstPortOper_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 16, 1, 17),
    _TLiIpFilterParamsDstPortOper_Type()
)
tLiIpFilterParamsDstPortOper.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLiIpFilterParamsDstPortOper.setStatus("current")
_TLiIpFilterParamsInfoTable_Object = MibTable
tLiIpFilterParamsInfoTable = _TLiIpFilterParamsInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 17)
)
if mibBuilder.loadTexts:
    tLiIpFilterParamsInfoTable.setStatus("current")
_TLiIpFilterParamsInfoEntry_Object = MibTableRow
tLiIpFilterParamsInfoEntry = _TLiIpFilterParamsInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 17, 1)
)
if mibBuilder.loadTexts:
    tLiIpFilterParamsInfoEntry.setStatus("current")
_TLiIpFltrParamsInfIngrHitCount_Type = Counter64
_TLiIpFltrParamsInfIngrHitCount_Object = MibTableColumn
tLiIpFltrParamsInfIngrHitCount = _TLiIpFltrParamsInfIngrHitCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 17, 1, 1),
    _TLiIpFltrParamsInfIngrHitCount_Type()
)
tLiIpFltrParamsInfIngrHitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tLiIpFltrParamsInfIngrHitCount.setStatus("current")
_TLiIpFltrParamsInfEgrHitCount_Type = Counter64
_TLiIpFltrParamsInfEgrHitCount_Object = MibTableColumn
tLiIpFltrParamsInfEgrHitCount = _TLiIpFltrParamsInfEgrHitCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 17, 1, 2),
    _TLiIpFltrParamsInfEgrHitCount_Type()
)
tLiIpFltrParamsInfEgrHitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tLiIpFltrParamsInfEgrHitCount.setStatus("current")
_TLiIpFltrParamsInfIngrHitBytes_Type = Counter64
_TLiIpFltrParamsInfIngrHitBytes_Object = MibTableColumn
tLiIpFltrParamsInfIngrHitBytes = _TLiIpFltrParamsInfIngrHitBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 17, 1, 3),
    _TLiIpFltrParamsInfIngrHitBytes_Type()
)
tLiIpFltrParamsInfIngrHitBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tLiIpFltrParamsInfIngrHitBytes.setStatus("current")
_TLiIpFltrParamsInfEgrHitBytes_Type = Counter64
_TLiIpFltrParamsInfEgrHitBytes_Object = MibTableColumn
tLiIpFltrParamsInfEgrHitBytes = _TLiIpFltrParamsInfEgrHitBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 17, 1, 4),
    _TLiIpFltrParamsInfEgrHitBytes_Type()
)
tLiIpFltrParamsInfEgrHitBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tLiIpFltrParamsInfEgrHitBytes.setStatus("current")
_TFilterPrefixListTableLstChng_Type = TimeStamp
_TFilterPrefixListTableLstChng_Object = MibScalar
tFilterPrefixListTableLstChng = _TFilterPrefixListTableLstChng_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 32),
    _TFilterPrefixListTableLstChng_Type()
)
tFilterPrefixListTableLstChng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterPrefixListTableLstChng.setStatus("current")
_TFilterPrefixListTable_Object = MibTable
tFilterPrefixListTable = _TFilterPrefixListTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 33)
)
if mibBuilder.loadTexts:
    tFilterPrefixListTable.setStatus("current")
_TFilterPrefixListEntry_Object = MibTableRow
tFilterPrefixListEntry = _TFilterPrefixListEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 33, 1)
)
tFilterPrefixListEntry.setIndexNames(
    (0, "TIMETRA-FILTER-MIB", "tFilterPrefixListType"),
    (1, "TIMETRA-FILTER-MIB", "tFilterPrefixListName"),
)
if mibBuilder.loadTexts:
    tFilterPrefixListEntry.setStatus("current")
_TFilterPrefixListType_Type = TFltrPrefixListType
_TFilterPrefixListType_Object = MibTableColumn
tFilterPrefixListType = _TFilterPrefixListType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 33, 1, 1),
    _TFilterPrefixListType_Type()
)
tFilterPrefixListType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFilterPrefixListType.setStatus("current")
_TFilterPrefixListName_Type = TNamedItem
_TFilterPrefixListName_Object = MibTableColumn
tFilterPrefixListName = _TFilterPrefixListName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 33, 1, 2),
    _TFilterPrefixListName_Type()
)
tFilterPrefixListName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFilterPrefixListName.setStatus("current")
_TFilterPrefixListRowStatus_Type = RowStatus
_TFilterPrefixListRowStatus_Object = MibTableColumn
tFilterPrefixListRowStatus = _TFilterPrefixListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 33, 1, 3),
    _TFilterPrefixListRowStatus_Type()
)
tFilterPrefixListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterPrefixListRowStatus.setStatus("current")
_TFilterPrefixListLastChanged_Type = TimeStamp
_TFilterPrefixListLastChanged_Object = MibTableColumn
tFilterPrefixListLastChanged = _TFilterPrefixListLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 33, 1, 4),
    _TFilterPrefixListLastChanged_Type()
)
tFilterPrefixListLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterPrefixListLastChanged.setStatus("current")


class _TFilterPrefixListDescription_Type(TItemDescription):
    """Custom type tFilterPrefixListDescription based on TItemDescription"""
    defaultHexValue = ""


_TFilterPrefixListDescription_Type.__name__ = "TItemDescription"
_TFilterPrefixListDescription_Object = MibTableColumn
tFilterPrefixListDescription = _TFilterPrefixListDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 33, 1, 5),
    _TFilterPrefixListDescription_Type()
)
tFilterPrefixListDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterPrefixListDescription.setStatus("current")
_TFilterPrefixListEntryTblLstChg_Type = TimeStamp
_TFilterPrefixListEntryTblLstChg_Object = MibScalar
tFilterPrefixListEntryTblLstChg = _TFilterPrefixListEntryTblLstChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 34),
    _TFilterPrefixListEntryTblLstChg_Type()
)
tFilterPrefixListEntryTblLstChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterPrefixListEntryTblLstChg.setStatus("current")
_TFilterPrefixListEntryTable_Object = MibTable
tFilterPrefixListEntryTable = _TFilterPrefixListEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 35)
)
if mibBuilder.loadTexts:
    tFilterPrefixListEntryTable.setStatus("current")
_TFilterPrefixListEntryEntry_Object = MibTableRow
tFilterPrefixListEntryEntry = _TFilterPrefixListEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 35, 1)
)
tFilterPrefixListEntryEntry.setIndexNames(
    (0, "TIMETRA-FILTER-MIB", "tFilterPrefixListType"),
    (0, "TIMETRA-FILTER-MIB", "tFilterPrefixListName"),
    (0, "TIMETRA-FILTER-MIB", "tFilterPrefixListEntryPrefixType"),
    (0, "TIMETRA-FILTER-MIB", "tFilterPrefixListEntryPrefix"),
    (0, "TIMETRA-FILTER-MIB", "tFilterPrefixListEntryPrefixLen"),
)
if mibBuilder.loadTexts:
    tFilterPrefixListEntryEntry.setStatus("current")
_TFilterPrefixListEntryPrefixType_Type = InetAddressType
_TFilterPrefixListEntryPrefixType_Object = MibTableColumn
tFilterPrefixListEntryPrefixType = _TFilterPrefixListEntryPrefixType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 35, 1, 1),
    _TFilterPrefixListEntryPrefixType_Type()
)
tFilterPrefixListEntryPrefixType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFilterPrefixListEntryPrefixType.setStatus("current")


class _TFilterPrefixListEntryPrefix_Type(InetAddress):
    """Custom type tFilterPrefixListEntryPrefix based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TFilterPrefixListEntryPrefix_Type.__name__ = "InetAddress"
_TFilterPrefixListEntryPrefix_Object = MibTableColumn
tFilterPrefixListEntryPrefix = _TFilterPrefixListEntryPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 35, 1, 2),
    _TFilterPrefixListEntryPrefix_Type()
)
tFilterPrefixListEntryPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFilterPrefixListEntryPrefix.setStatus("current")
_TFilterPrefixListEntryPrefixLen_Type = InetAddressPrefixLength
_TFilterPrefixListEntryPrefixLen_Object = MibTableColumn
tFilterPrefixListEntryPrefixLen = _TFilterPrefixListEntryPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 35, 1, 3),
    _TFilterPrefixListEntryPrefixLen_Type()
)
tFilterPrefixListEntryPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFilterPrefixListEntryPrefixLen.setStatus("current")
_TFilterPrefixListEntryRowStatus_Type = RowStatus
_TFilterPrefixListEntryRowStatus_Object = MibTableColumn
tFilterPrefixListEntryRowStatus = _TFilterPrefixListEntryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 35, 1, 4),
    _TFilterPrefixListEntryRowStatus_Type()
)
tFilterPrefixListEntryRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterPrefixListEntryRowStatus.setStatus("current")
_TFilterEmbeddedRefTableLstChg_Type = TimeStamp
_TFilterEmbeddedRefTableLstChg_Object = MibScalar
tFilterEmbeddedRefTableLstChg = _TFilterEmbeddedRefTableLstChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 36),
    _TFilterEmbeddedRefTableLstChg_Type()
)
tFilterEmbeddedRefTableLstChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterEmbeddedRefTableLstChg.setStatus("current")
_TFilterEmbeddedRefTable_Object = MibTable
tFilterEmbeddedRefTable = _TFilterEmbeddedRefTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 37)
)
if mibBuilder.loadTexts:
    tFilterEmbeddedRefTable.setStatus("current")
_TFilterEmbeddedRefTableEntry_Object = MibTableRow
tFilterEmbeddedRefTableEntry = _TFilterEmbeddedRefTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 37, 1)
)
tFilterEmbeddedRefTableEntry.setIndexNames(
    (0, "TIMETRA-FILTER-MIB", "tFilterEmbeddedRefFilterType"),
    (0, "TIMETRA-FILTER-MIB", "tFilterEmbeddedRefInsertFltrId"),
    (0, "TIMETRA-FILTER-MIB", "tFilterEmbeddedRefEmbeddedFltrId"),
    (0, "TIMETRA-FILTER-MIB", "tFilterEmbeddedRefOffset"),
)
if mibBuilder.loadTexts:
    tFilterEmbeddedRefTableEntry.setStatus("current")
_TFilterEmbeddedRefFilterType_Type = TFilterType
_TFilterEmbeddedRefFilterType_Object = MibTableColumn
tFilterEmbeddedRefFilterType = _TFilterEmbeddedRefFilterType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 37, 1, 1),
    _TFilterEmbeddedRefFilterType_Type()
)
tFilterEmbeddedRefFilterType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFilterEmbeddedRefFilterType.setStatus("current")
_TFilterEmbeddedRefInsertFltrId_Type = TFilterID
_TFilterEmbeddedRefInsertFltrId_Object = MibTableColumn
tFilterEmbeddedRefInsertFltrId = _TFilterEmbeddedRefInsertFltrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 37, 1, 2),
    _TFilterEmbeddedRefInsertFltrId_Type()
)
tFilterEmbeddedRefInsertFltrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFilterEmbeddedRefInsertFltrId.setStatus("current")
_TFilterEmbeddedRefEmbeddedFltrId_Type = TFilterID
_TFilterEmbeddedRefEmbeddedFltrId_Object = MibTableColumn
tFilterEmbeddedRefEmbeddedFltrId = _TFilterEmbeddedRefEmbeddedFltrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 37, 1, 3),
    _TFilterEmbeddedRefEmbeddedFltrId_Type()
)
tFilterEmbeddedRefEmbeddedFltrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFilterEmbeddedRefEmbeddedFltrId.setStatus("current")


class _TFilterEmbeddedRefOffset_Type(Unsigned32):
    """Custom type tFilterEmbeddedRefOffset based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TFilterEmbeddedRefOffset_Type.__name__ = "Unsigned32"
_TFilterEmbeddedRefOffset_Object = MibTableColumn
tFilterEmbeddedRefOffset = _TFilterEmbeddedRefOffset_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 37, 1, 4),
    _TFilterEmbeddedRefOffset_Type()
)
tFilterEmbeddedRefOffset.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFilterEmbeddedRefOffset.setStatus("current")
_TFilterEmbeddedRefRowStatus_Type = RowStatus
_TFilterEmbeddedRefRowStatus_Object = MibTableColumn
tFilterEmbeddedRefRowStatus = _TFilterEmbeddedRefRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 37, 1, 5),
    _TFilterEmbeddedRefRowStatus_Type()
)
tFilterEmbeddedRefRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterEmbeddedRefRowStatus.setStatus("current")


class _TFilterEmbeddedRefAdminState_Type(Integer32):
    """Custom type tFilterEmbeddedRefAdminState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_TFilterEmbeddedRefAdminState_Type.__name__ = "Integer32"
_TFilterEmbeddedRefAdminState_Object = MibTableColumn
tFilterEmbeddedRefAdminState = _TFilterEmbeddedRefAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 37, 1, 6),
    _TFilterEmbeddedRefAdminState_Type()
)
tFilterEmbeddedRefAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterEmbeddedRefAdminState.setStatus("current")
_TFilterEmbeddedRefOperState_Type = TmnxEmbeddedFltrOperState
_TFilterEmbeddedRefOperState_Object = MibTableColumn
tFilterEmbeddedRefOperState = _TFilterEmbeddedRefOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 37, 1, 7),
    _TFilterEmbeddedRefOperState_Type()
)
tFilterEmbeddedRefOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterEmbeddedRefOperState.setStatus("current")
_TFilterPortListTableLstChng_Type = TimeStamp
_TFilterPortListTableLstChng_Object = MibScalar
tFilterPortListTableLstChng = _TFilterPortListTableLstChng_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 38),
    _TFilterPortListTableLstChng_Type()
)
tFilterPortListTableLstChng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterPortListTableLstChng.setStatus("current")
_TFilterPortListTable_Object = MibTable
tFilterPortListTable = _TFilterPortListTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 39)
)
if mibBuilder.loadTexts:
    tFilterPortListTable.setStatus("current")
_TFilterPortListEntry_Object = MibTableRow
tFilterPortListEntry = _TFilterPortListEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 39, 1)
)
tFilterPortListEntry.setIndexNames(
    (1, "TIMETRA-FILTER-MIB", "tFilterPortListName"),
)
if mibBuilder.loadTexts:
    tFilterPortListEntry.setStatus("current")
_TFilterPortListName_Type = TNamedItem
_TFilterPortListName_Object = MibTableColumn
tFilterPortListName = _TFilterPortListName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 39, 1, 1),
    _TFilterPortListName_Type()
)
tFilterPortListName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFilterPortListName.setStatus("current")
_TFilterPortListRowStatus_Type = RowStatus
_TFilterPortListRowStatus_Object = MibTableColumn
tFilterPortListRowStatus = _TFilterPortListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 39, 1, 2),
    _TFilterPortListRowStatus_Type()
)
tFilterPortListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterPortListRowStatus.setStatus("current")
_TFilterPortListLastChanged_Type = TimeStamp
_TFilterPortListLastChanged_Object = MibTableColumn
tFilterPortListLastChanged = _TFilterPortListLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 39, 1, 3),
    _TFilterPortListLastChanged_Type()
)
tFilterPortListLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterPortListLastChanged.setStatus("current")


class _TFilterPortListDescription_Type(TItemDescription):
    """Custom type tFilterPortListDescription based on TItemDescription"""
    defaultHexValue = ""


_TFilterPortListDescription_Type.__name__ = "TItemDescription"
_TFilterPortListDescription_Object = MibTableColumn
tFilterPortListDescription = _TFilterPortListDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 39, 1, 4),
    _TFilterPortListDescription_Type()
)
tFilterPortListDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterPortListDescription.setStatus("current")
_TFilterPortListEntryTblLstChg_Type = TimeStamp
_TFilterPortListEntryTblLstChg_Object = MibScalar
tFilterPortListEntryTblLstChg = _TFilterPortListEntryTblLstChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 40),
    _TFilterPortListEntryTblLstChg_Type()
)
tFilterPortListEntryTblLstChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterPortListEntryTblLstChg.setStatus("current")
_TFilterPortListEntryTable_Object = MibTable
tFilterPortListEntryTable = _TFilterPortListEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 41)
)
if mibBuilder.loadTexts:
    tFilterPortListEntryTable.setStatus("current")
_TFilterPortListEntryEntry_Object = MibTableRow
tFilterPortListEntryEntry = _TFilterPortListEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 41, 1)
)
tFilterPortListEntryEntry.setIndexNames(
    (0, "TIMETRA-FILTER-MIB", "tFilterPortListName"),
    (0, "TIMETRA-FILTER-MIB", "tFilterPortListEntryPortLow"),
    (0, "TIMETRA-FILTER-MIB", "tFilterPortListEntryPortHigh"),
)
if mibBuilder.loadTexts:
    tFilterPortListEntryEntry.setStatus("current")


class _TFilterPortListEntryPortLow_Type(TTcpUdpPort):
    """Custom type tFilterPortListEntryPortLow based on TTcpUdpPort"""
    defaultValue = 0


_TFilterPortListEntryPortLow_Type.__name__ = "TTcpUdpPort"
_TFilterPortListEntryPortLow_Object = MibTableColumn
tFilterPortListEntryPortLow = _TFilterPortListEntryPortLow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 41, 1, 1),
    _TFilterPortListEntryPortLow_Type()
)
tFilterPortListEntryPortLow.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFilterPortListEntryPortLow.setStatus("current")


class _TFilterPortListEntryPortHigh_Type(TTcpUdpPort):
    """Custom type tFilterPortListEntryPortHigh based on TTcpUdpPort"""
    defaultValue = 65535


_TFilterPortListEntryPortHigh_Type.__name__ = "TTcpUdpPort"
_TFilterPortListEntryPortHigh_Object = MibTableColumn
tFilterPortListEntryPortHigh = _TFilterPortListEntryPortHigh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 41, 1, 2),
    _TFilterPortListEntryPortHigh_Type()
)
tFilterPortListEntryPortHigh.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFilterPortListEntryPortHigh.setStatus("current")
_TFilterPortListEntryRowStatus_Type = RowStatus
_TFilterPortListEntryRowStatus_Object = MibTableColumn
tFilterPortListEntryRowStatus = _TFilterPortListEntryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 41, 1, 3),
    _TFilterPortListEntryRowStatus_Type()
)
tFilterPortListEntryRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterPortListEntryRowStatus.setStatus("current")
_TFilterApplyPathTableLstChng_Type = TimeStamp
_TFilterApplyPathTableLstChng_Object = MibScalar
tFilterApplyPathTableLstChng = _TFilterApplyPathTableLstChng_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 42),
    _TFilterApplyPathTableLstChng_Type()
)
tFilterApplyPathTableLstChng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterApplyPathTableLstChng.setStatus("current")
_TFilterApplyPathTable_Object = MibTable
tFilterApplyPathTable = _TFilterApplyPathTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 43)
)
if mibBuilder.loadTexts:
    tFilterApplyPathTable.setStatus("current")
_TFilterApplyPathEntry_Object = MibTableRow
tFilterApplyPathEntry = _TFilterApplyPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 43, 1)
)
tFilterApplyPathEntry.setIndexNames(
    (0, "TIMETRA-FILTER-MIB", "tFilterPrefixListType"),
    (0, "TIMETRA-FILTER-MIB", "tFilterPrefixListName"),
    (0, "TIMETRA-FILTER-MIB", "tFilterApplyPathSource"),
    (0, "TIMETRA-FILTER-MIB", "tFilterApplyPathIndex"),
)
if mibBuilder.loadTexts:
    tFilterApplyPathEntry.setStatus("current")


class _TFilterApplyPathSource_Type(TmnxFilterApplyPathSource):
    """Custom type tFilterApplyPathSource based on TmnxFilterApplyPathSource"""
    defaultValue = 0


_TFilterApplyPathSource_Type.__name__ = "TmnxFilterApplyPathSource"
_TFilterApplyPathSource_Object = MibTableColumn
tFilterApplyPathSource = _TFilterApplyPathSource_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 43, 1, 1),
    _TFilterApplyPathSource_Type()
)
tFilterApplyPathSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFilterApplyPathSource.setStatus("current")


class _TFilterApplyPathIndex_Type(Unsigned32):
    """Custom type tFilterApplyPathIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_TFilterApplyPathIndex_Type.__name__ = "Unsigned32"
_TFilterApplyPathIndex_Object = MibTableColumn
tFilterApplyPathIndex = _TFilterApplyPathIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 43, 1, 2),
    _TFilterApplyPathIndex_Type()
)
tFilterApplyPathIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFilterApplyPathIndex.setStatus("current")
_TFilterApplyPathRowStatus_Type = RowStatus
_TFilterApplyPathRowStatus_Object = MibTableColumn
tFilterApplyPathRowStatus = _TFilterApplyPathRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 43, 1, 3),
    _TFilterApplyPathRowStatus_Type()
)
tFilterApplyPathRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterApplyPathRowStatus.setStatus("current")
_TFilterApplyPathLastChanged_Type = TimeStamp
_TFilterApplyPathLastChanged_Object = MibTableColumn
tFilterApplyPathLastChanged = _TFilterApplyPathLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 43, 1, 4),
    _TFilterApplyPathLastChanged_Type()
)
tFilterApplyPathLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterApplyPathLastChanged.setStatus("current")


class _TFilterApplyPathMatch1_Type(TRegularExpression):
    """Custom type tFilterApplyPathMatch1 based on TRegularExpression"""
    defaultHexValue = ""


_TFilterApplyPathMatch1_Type.__name__ = "TRegularExpression"
_TFilterApplyPathMatch1_Object = MibTableColumn
tFilterApplyPathMatch1 = _TFilterApplyPathMatch1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 43, 1, 5),
    _TFilterApplyPathMatch1_Type()
)
tFilterApplyPathMatch1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterApplyPathMatch1.setStatus("current")


class _TFilterApplyPathMatch2_Type(TRegularExpression):
    """Custom type tFilterApplyPathMatch2 based on TRegularExpression"""
    defaultHexValue = ""


_TFilterApplyPathMatch2_Type.__name__ = "TRegularExpression"
_TFilterApplyPathMatch2_Object = MibTableColumn
tFilterApplyPathMatch2 = _TFilterApplyPathMatch2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 43, 1, 6),
    _TFilterApplyPathMatch2_Type()
)
tFilterApplyPathMatch2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterApplyPathMatch2.setStatus("current")
_TFilterEmbeddedRefInfoTable_Object = MibTable
tFilterEmbeddedRefInfoTable = _TFilterEmbeddedRefInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 44)
)
if mibBuilder.loadTexts:
    tFilterEmbeddedRefInfoTable.setStatus("current")
_TFilterEmbeddedRefInfoEntry_Object = MibTableRow
tFilterEmbeddedRefInfoEntry = _TFilterEmbeddedRefInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 44, 1)
)
if mibBuilder.loadTexts:
    tFilterEmbeddedRefInfoEntry.setStatus("current")
_TFltrEmbedRefInfEntryCnt_Type = Unsigned32
_TFltrEmbedRefInfEntryCnt_Object = MibTableColumn
tFltrEmbedRefInfEntryCnt = _TFltrEmbedRefInfEntryCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 44, 1, 1),
    _TFltrEmbedRefInfEntryCnt_Type()
)
tFltrEmbedRefInfEntryCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFltrEmbedRefInfEntryCnt.setStatus("current")
_TFltrEmbedRefInfEntryCntInsrtd_Type = Unsigned32
_TFltrEmbedRefInfEntryCntInsrtd_Object = MibTableColumn
tFltrEmbedRefInfEntryCntInsrtd = _TFltrEmbedRefInfEntryCntInsrtd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 44, 1, 2),
    _TFltrEmbedRefInfEntryCntInsrtd_Type()
)
tFltrEmbedRefInfEntryCntInsrtd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFltrEmbedRefInfEntryCntInsrtd.setStatus("current")
_TFilterEmbeddedEntryRefInfoTable_Object = MibTable
tFilterEmbeddedEntryRefInfoTable = _TFilterEmbeddedEntryRefInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 45)
)
if mibBuilder.loadTexts:
    tFilterEmbeddedEntryRefInfoTable.setStatus("current")
_TFilterEmbeddedEntryRefInfoEntry_Object = MibTableRow
tFilterEmbeddedEntryRefInfoEntry = _TFilterEmbeddedEntryRefInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 45, 1)
)
tFilterEmbeddedEntryRefInfoEntry.setIndexNames(
    (0, "TIMETRA-FILTER-MIB", "tFltrEmbedEntryFilterType"),
    (0, "TIMETRA-FILTER-MIB", "tFltrEmbedEntryInsertFltrId"),
    (0, "TIMETRA-FILTER-MIB", "tFltrEmbedEntryEmbeddedFltrId"),
    (0, "TIMETRA-FILTER-MIB", "tFltrEmbedEntryEmbeddedEntryId"),
)
if mibBuilder.loadTexts:
    tFilterEmbeddedEntryRefInfoEntry.setStatus("current")
_TFltrEmbedEntryFilterType_Type = TFilterType
_TFltrEmbedEntryFilterType_Object = MibTableColumn
tFltrEmbedEntryFilterType = _TFltrEmbedEntryFilterType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 45, 1, 1),
    _TFltrEmbedEntryFilterType_Type()
)
tFltrEmbedEntryFilterType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFltrEmbedEntryFilterType.setStatus("current")
_TFltrEmbedEntryInsertFltrId_Type = TFilterID
_TFltrEmbedEntryInsertFltrId_Object = MibTableColumn
tFltrEmbedEntryInsertFltrId = _TFltrEmbedEntryInsertFltrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 45, 1, 2),
    _TFltrEmbedEntryInsertFltrId_Type()
)
tFltrEmbedEntryInsertFltrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFltrEmbedEntryInsertFltrId.setStatus("current")
_TFltrEmbedEntryEmbeddedFltrId_Type = TFilterID
_TFltrEmbedEntryEmbeddedFltrId_Object = MibTableColumn
tFltrEmbedEntryEmbeddedFltrId = _TFltrEmbedEntryEmbeddedFltrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 45, 1, 3),
    _TFltrEmbedEntryEmbeddedFltrId_Type()
)
tFltrEmbedEntryEmbeddedFltrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFltrEmbedEntryEmbeddedFltrId.setStatus("current")
_TFltrEmbedEntryEmbeddedEntryId_Type = TEntryId
_TFltrEmbedEntryEmbeddedEntryId_Object = MibTableColumn
tFltrEmbedEntryEmbeddedEntryId = _TFltrEmbedEntryEmbeddedEntryId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 45, 1, 4),
    _TFltrEmbedEntryEmbeddedEntryId_Type()
)
tFltrEmbedEntryEmbeddedEntryId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFltrEmbedEntryEmbeddedEntryId.setStatus("current")
_TFltrEmbedEntryInsrtEntryId_Type = TEntryId
_TFltrEmbedEntryInsrtEntryId_Object = MibTableColumn
tFltrEmbedEntryInsrtEntryId = _TFltrEmbedEntryInsrtEntryId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 45, 1, 5),
    _TFltrEmbedEntryInsrtEntryId_Type()
)
tFltrEmbedEntryInsrtEntryId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFltrEmbedEntryInsrtEntryId.setStatus("current")
_TFltrEmbedEntryRefOperState_Type = TmnxFltrEmbeddedEntryState
_TFltrEmbedEntryRefOperState_Object = MibTableColumn
tFltrEmbedEntryRefOperState = _TFltrEmbedEntryRefOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 45, 1, 6),
    _TFltrEmbedEntryRefOperState_Type()
)
tFltrEmbedEntryRefOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFltrEmbedEntryRefOperState.setStatus("current")
_TIPv6FilterParamsExtTbleLstChgd_Type = TimeStamp
_TIPv6FilterParamsExtTbleLstChgd_Object = MibScalar
tIPv6FilterParamsExtTbleLstChgd = _TIPv6FilterParamsExtTbleLstChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 46),
    _TIPv6FilterParamsExtTbleLstChgd_Type()
)
tIPv6FilterParamsExtTbleLstChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPv6FilterParamsExtTbleLstChgd.setStatus("current")
_TIPv6FilterParamsExtTable_Object = MibTable
tIPv6FilterParamsExtTable = _TIPv6FilterParamsExtTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 47)
)
if mibBuilder.loadTexts:
    tIPv6FilterParamsExtTable.setStatus("current")
_TIPv6FilterParamsExtEntry_Object = MibTableRow
tIPv6FilterParamsExtEntry = _TIPv6FilterParamsExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 47, 1)
)
if mibBuilder.loadTexts:
    tIPv6FilterParamsExtEntry.setStatus("current")
_TIPv6FilterParamsExtLastChanged_Type = TimeStamp
_TIPv6FilterParamsExtLastChanged_Object = MibTableColumn
tIPv6FilterParamsExtLastChanged = _TIPv6FilterParamsExtLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 47, 1, 1),
    _TIPv6FilterParamsExtLastChanged_Type()
)
tIPv6FilterParamsExtLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPv6FilterParamsExtLastChanged.setStatus("current")


class _TIPv6FilterParamsExtAhExtHdr_Type(TItemMatch):
    """Custom type tIPv6FilterParamsExtAhExtHdr based on TItemMatch"""
    defaultValue = 1


_TIPv6FilterParamsExtAhExtHdr_Type.__name__ = "TItemMatch"
_TIPv6FilterParamsExtAhExtHdr_Object = MibTableColumn
tIPv6FilterParamsExtAhExtHdr = _TIPv6FilterParamsExtAhExtHdr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 47, 1, 2),
    _TIPv6FilterParamsExtAhExtHdr_Type()
)
tIPv6FilterParamsExtAhExtHdr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsExtAhExtHdr.setStatus("current")


class _TIPv6FilterParamsExtEspExtHdr_Type(TItemMatch):
    """Custom type tIPv6FilterParamsExtEspExtHdr based on TItemMatch"""
    defaultValue = 1


_TIPv6FilterParamsExtEspExtHdr_Type.__name__ = "TItemMatch"
_TIPv6FilterParamsExtEspExtHdr_Object = MibTableColumn
tIPv6FilterParamsExtEspExtHdr = _TIPv6FilterParamsExtEspExtHdr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 47, 1, 3),
    _TIPv6FilterParamsExtEspExtHdr_Type()
)
tIPv6FilterParamsExtEspExtHdr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsExtEspExtHdr.setStatus("current")


class _TIPv6FilterParamsExtNatType_Type(TmnxNatSubscriberType):
    """Custom type tIPv6FilterParamsExtNatType based on TmnxNatSubscriberType"""
    defaultValue = 3

    subtypeSpec = TmnxNatSubscriberType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("dsliteLsnSub", 3),
          ("nat64LsnSub", 4))
    )


_TIPv6FilterParamsExtNatType_Type.__name__ = "TmnxNatSubscriberType"
_TIPv6FilterParamsExtNatType_Object = MibTableColumn
tIPv6FilterParamsExtNatType = _TIPv6FilterParamsExtNatType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 47, 1, 4),
    _TIPv6FilterParamsExtNatType_Type()
)
tIPv6FilterParamsExtNatType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsExtNatType.setStatus("current")
_TFilterEmbedOpenflowTableLstChg_Type = TimeStamp
_TFilterEmbedOpenflowTableLstChg_Object = MibScalar
tFilterEmbedOpenflowTableLstChg = _TFilterEmbedOpenflowTableLstChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 48),
    _TFilterEmbedOpenflowTableLstChg_Type()
)
tFilterEmbedOpenflowTableLstChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterEmbedOpenflowTableLstChg.setStatus("current")
_TFilterEmbedOpenflowTable_Object = MibTable
tFilterEmbedOpenflowTable = _TFilterEmbedOpenflowTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 49)
)
if mibBuilder.loadTexts:
    tFilterEmbedOpenflowTable.setStatus("current")
_TFilterEmbedOpenflowEntry_Object = MibTableRow
tFilterEmbedOpenflowEntry = _TFilterEmbedOpenflowEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 49, 1)
)
tFilterEmbedOpenflowEntry.setIndexNames(
    (0, "TIMETRA-FILTER-MIB", "tFilterEmbedOpenflowOfsName"),
    (0, "TIMETRA-FILTER-MIB", "tFilterEmbedOpenflowFilterType"),
    (0, "TIMETRA-FILTER-MIB", "tFilterEmbedOpenflowInsertFltrId"),
    (0, "TIMETRA-FILTER-MIB", "tFilterEmbedOpenflowOffset"),
)
if mibBuilder.loadTexts:
    tFilterEmbedOpenflowEntry.setStatus("current")
_TFilterEmbedOpenflowOfsName_Type = TNamedItem
_TFilterEmbedOpenflowOfsName_Object = MibTableColumn
tFilterEmbedOpenflowOfsName = _TFilterEmbedOpenflowOfsName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 49, 1, 1),
    _TFilterEmbedOpenflowOfsName_Type()
)
tFilterEmbedOpenflowOfsName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFilterEmbedOpenflowOfsName.setStatus("current")
_TFilterEmbedOpenflowFilterType_Type = TFilterType
_TFilterEmbedOpenflowFilterType_Object = MibTableColumn
tFilterEmbedOpenflowFilterType = _TFilterEmbedOpenflowFilterType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 49, 1, 2),
    _TFilterEmbedOpenflowFilterType_Type()
)
tFilterEmbedOpenflowFilterType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFilterEmbedOpenflowFilterType.setStatus("current")
_TFilterEmbedOpenflowInsertFltrId_Type = TFilterID
_TFilterEmbedOpenflowInsertFltrId_Object = MibTableColumn
tFilterEmbedOpenflowInsertFltrId = _TFilterEmbedOpenflowInsertFltrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 49, 1, 3),
    _TFilterEmbedOpenflowInsertFltrId_Type()
)
tFilterEmbedOpenflowInsertFltrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFilterEmbedOpenflowInsertFltrId.setStatus("current")


class _TFilterEmbedOpenflowOffset_Type(Unsigned32):
    """Custom type tFilterEmbedOpenflowOffset based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TFilterEmbedOpenflowOffset_Type.__name__ = "Unsigned32"
_TFilterEmbedOpenflowOffset_Object = MibTableColumn
tFilterEmbedOpenflowOffset = _TFilterEmbedOpenflowOffset_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 49, 1, 4),
    _TFilterEmbedOpenflowOffset_Type()
)
tFilterEmbedOpenflowOffset.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFilterEmbedOpenflowOffset.setStatus("current")
_TFilterEmbedOpenflowRowStatus_Type = RowStatus
_TFilterEmbedOpenflowRowStatus_Object = MibTableColumn
tFilterEmbedOpenflowRowStatus = _TFilterEmbedOpenflowRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 49, 1, 5),
    _TFilterEmbedOpenflowRowStatus_Type()
)
tFilterEmbedOpenflowRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterEmbedOpenflowRowStatus.setStatus("current")


class _TFilterEmbedOpenflowAdminState_Type(Integer32):
    """Custom type tFilterEmbedOpenflowAdminState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_TFilterEmbedOpenflowAdminState_Type.__name__ = "Integer32"
_TFilterEmbedOpenflowAdminState_Object = MibTableColumn
tFilterEmbedOpenflowAdminState = _TFilterEmbedOpenflowAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 49, 1, 6),
    _TFilterEmbedOpenflowAdminState_Type()
)
tFilterEmbedOpenflowAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterEmbedOpenflowAdminState.setStatus("current")
_TFilterEmbedOpenflowOperState_Type = TmnxEmbeddedFltrOperState
_TFilterEmbedOpenflowOperState_Object = MibTableColumn
tFilterEmbedOpenflowOperState = _TFilterEmbedOpenflowOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 49, 1, 7),
    _TFilterEmbedOpenflowOperState_Type()
)
tFilterEmbedOpenflowOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterEmbedOpenflowOperState.setStatus("current")
_TFilterEmbedOpenflowInfoTable_Object = MibTable
tFilterEmbedOpenflowInfoTable = _TFilterEmbedOpenflowInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 50)
)
if mibBuilder.loadTexts:
    tFilterEmbedOpenflowInfoTable.setStatus("current")
_TFilterEmbedOpenflowInfoEntry_Object = MibTableRow
tFilterEmbedOpenflowInfoEntry = _TFilterEmbedOpenflowInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 50, 1)
)
if mibBuilder.loadTexts:
    tFilterEmbedOpenflowInfoEntry.setStatus("current")
_TFltrEmbedOfInfoEntryCnt_Type = Unsigned32
_TFltrEmbedOfInfoEntryCnt_Object = MibTableColumn
tFltrEmbedOfInfoEntryCnt = _TFltrEmbedOfInfoEntryCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 50, 1, 1),
    _TFltrEmbedOfInfoEntryCnt_Type()
)
tFltrEmbedOfInfoEntryCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFltrEmbedOfInfoEntryCnt.setStatus("current")
_TFltrEmbedOfInfoEntryCntInsrtd_Type = Unsigned32
_TFltrEmbedOfInfoEntryCntInsrtd_Object = MibTableColumn
tFltrEmbedOfInfoEntryCntInsrtd = _TFltrEmbedOfInfoEntryCntInsrtd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 50, 1, 2),
    _TFltrEmbedOfInfoEntryCntInsrtd_Type()
)
tFltrEmbedOfInfoEntryCntInsrtd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFltrEmbedOfInfoEntryCntInsrtd.setStatus("current")
_TFilterOpenflowEntryInfoTable_Object = MibTable
tFilterOpenflowEntryInfoTable = _TFilterOpenflowEntryInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 51)
)
if mibBuilder.loadTexts:
    tFilterOpenflowEntryInfoTable.setStatus("current")
_TFilterOpenflowEntryInfoEntry_Object = MibTableRow
tFilterOpenflowEntryInfoEntry = _TFilterOpenflowEntryInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 51, 1)
)
tFilterOpenflowEntryInfoEntry.setIndexNames(
    (0, "TIMETRA-FILTER-MIB", "tFltrEmbedOfEntryOfsName"),
    (0, "TIMETRA-FILTER-MIB", "tFltrEmbedOfEntryFilterType"),
    (0, "TIMETRA-FILTER-MIB", "tFltrEmbedOfEntryInsertFltrId"),
    (0, "TIMETRA-FILTER-MIB", "tFltrEmbedOfEntryOfEntryId"),
)
if mibBuilder.loadTexts:
    tFilterOpenflowEntryInfoEntry.setStatus("current")
_TFltrEmbedOfEntryOfsName_Type = TNamedItem
_TFltrEmbedOfEntryOfsName_Object = MibTableColumn
tFltrEmbedOfEntryOfsName = _TFltrEmbedOfEntryOfsName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 51, 1, 1),
    _TFltrEmbedOfEntryOfsName_Type()
)
tFltrEmbedOfEntryOfsName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFltrEmbedOfEntryOfsName.setStatus("current")
_TFltrEmbedOfEntryFilterType_Type = TFilterType
_TFltrEmbedOfEntryFilterType_Object = MibTableColumn
tFltrEmbedOfEntryFilterType = _TFltrEmbedOfEntryFilterType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 51, 1, 2),
    _TFltrEmbedOfEntryFilterType_Type()
)
tFltrEmbedOfEntryFilterType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFltrEmbedOfEntryFilterType.setStatus("current")
_TFltrEmbedOfEntryInsertFltrId_Type = TFilterID
_TFltrEmbedOfEntryInsertFltrId_Object = MibTableColumn
tFltrEmbedOfEntryInsertFltrId = _TFltrEmbedOfEntryInsertFltrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 51, 1, 3),
    _TFltrEmbedOfEntryInsertFltrId_Type()
)
tFltrEmbedOfEntryInsertFltrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFltrEmbedOfEntryInsertFltrId.setStatus("current")
_TFltrEmbedOfEntryOfEntryId_Type = TEntryId
_TFltrEmbedOfEntryOfEntryId_Object = MibTableColumn
tFltrEmbedOfEntryOfEntryId = _TFltrEmbedOfEntryOfEntryId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 51, 1, 4),
    _TFltrEmbedOfEntryOfEntryId_Type()
)
tFltrEmbedOfEntryOfEntryId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFltrEmbedOfEntryOfEntryId.setStatus("current")
_TFltrEmbedOfEntryInsrtEntryId_Type = TEntryId
_TFltrEmbedOfEntryInsrtEntryId_Object = MibTableColumn
tFltrEmbedOfEntryInsrtEntryId = _TFltrEmbedOfEntryInsrtEntryId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 51, 1, 5),
    _TFltrEmbedOfEntryInsrtEntryId_Type()
)
tFltrEmbedOfEntryInsrtEntryId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFltrEmbedOfEntryInsrtEntryId.setStatus("current")
_TFltrEmbedOfEntryInsrtEntryState_Type = TmnxFltrEmbeddedEntryState
_TFltrEmbedOfEntryInsrtEntryState_Object = MibTableColumn
tFltrEmbedOfEntryInsrtEntryState = _TFltrEmbedOfEntryInsrtEntryState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 51, 1, 6),
    _TFltrEmbedOfEntryInsrtEntryState_Type()
)
tFltrEmbedOfEntryInsrtEntryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFltrEmbedOfEntryInsrtEntryState.setStatus("current")
_TIPFilterParamsExtTbleLstChgd_Type = TimeStamp
_TIPFilterParamsExtTbleLstChgd_Object = MibScalar
tIPFilterParamsExtTbleLstChgd = _TIPFilterParamsExtTbleLstChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 52),
    _TIPFilterParamsExtTbleLstChgd_Type()
)
tIPFilterParamsExtTbleLstChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPFilterParamsExtTbleLstChgd.setStatus("current")
_TIPFilterParamsExtTable_Object = MibTable
tIPFilterParamsExtTable = _TIPFilterParamsExtTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 53)
)
if mibBuilder.loadTexts:
    tIPFilterParamsExtTable.setStatus("current")
_TIPFilterParamsExtEntry_Object = MibTableRow
tIPFilterParamsExtEntry = _TIPFilterParamsExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 53, 1)
)
if mibBuilder.loadTexts:
    tIPFilterParamsExtEntry.setStatus("current")
_TIPFilterParamsExtLastChanged_Type = TimeStamp
_TIPFilterParamsExtLastChanged_Object = MibTableColumn
tIPFilterParamsExtLastChanged = _TIPFilterParamsExtLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 53, 1, 1),
    _TIPFilterParamsExtLastChanged_Type()
)
tIPFilterParamsExtLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPFilterParamsExtLastChanged.setStatus("current")


class _TIPFilterParamsExtPktLenVal1_Type(TFilterPacketLength):
    """Custom type tIPFilterParamsExtPktLenVal1 based on TFilterPacketLength"""
    defaultValue = 0


_TIPFilterParamsExtPktLenVal1_Type.__name__ = "TFilterPacketLength"
_TIPFilterParamsExtPktLenVal1_Object = MibTableColumn
tIPFilterParamsExtPktLenVal1 = _TIPFilterParamsExtPktLenVal1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 53, 1, 2),
    _TIPFilterParamsExtPktLenVal1_Type()
)
tIPFilterParamsExtPktLenVal1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsExtPktLenVal1.setStatus("current")


class _TIPFilterParamsExtPktLenVal2_Type(TFilterPacketLength):
    """Custom type tIPFilterParamsExtPktLenVal2 based on TFilterPacketLength"""
    defaultValue = 0


_TIPFilterParamsExtPktLenVal2_Type.__name__ = "TFilterPacketLength"
_TIPFilterParamsExtPktLenVal2_Object = MibTableColumn
tIPFilterParamsExtPktLenVal2 = _TIPFilterParamsExtPktLenVal2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 53, 1, 3),
    _TIPFilterParamsExtPktLenVal2_Type()
)
tIPFilterParamsExtPktLenVal2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsExtPktLenVal2.setStatus("current")


class _TIPFilterParamsExtPktLenOper_Type(TOperator):
    """Custom type tIPFilterParamsExtPktLenOper based on TOperator"""
    defaultValue = 0


_TIPFilterParamsExtPktLenOper_Type.__name__ = "TOperator"
_TIPFilterParamsExtPktLenOper_Object = MibTableColumn
tIPFilterParamsExtPktLenOper = _TIPFilterParamsExtPktLenOper_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 53, 1, 4),
    _TIPFilterParamsExtPktLenOper_Type()
)
tIPFilterParamsExtPktLenOper.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsExtPktLenOper.setStatus("current")
_TFilterNotificationsPrefix_ObjectIdentity = ObjectIdentity
tFilterNotificationsPrefix = _TFilterNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 21)
)
_TFilterNotifications_ObjectIdentity = ObjectIdentity
tFilterNotifications = _TFilterNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 21, 0)
)
tLiIpFilterParamsEntry.registerAugmentions(
    ("TIMETRA-FILTER-MIB",
     "tLiIpFilterParamsInfoEntry")
)
tLiIpFilterParamsInfoEntry.setIndexNames(*tLiIpFilterParamsEntry.getIndexNames())
tFilterEmbeddedRefTableEntry.registerAugmentions(
    ("TIMETRA-FILTER-MIB",
     "tFilterEmbeddedRefInfoEntry")
)
tFilterEmbeddedRefInfoEntry.setIndexNames(*tFilterEmbeddedRefTableEntry.getIndexNames())
tIPv6FilterParamsEntry.registerAugmentions(
    ("TIMETRA-FILTER-MIB",
     "tIPv6FilterParamsExtEntry")
)
tIPv6FilterParamsExtEntry.setIndexNames(*tIPv6FilterParamsEntry.getIndexNames())
tFilterEmbedOpenflowEntry.registerAugmentions(
    ("TIMETRA-FILTER-MIB",
     "tFilterEmbedOpenflowInfoEntry")
)
tFilterEmbedOpenflowInfoEntry.setIndexNames(*tFilterEmbedOpenflowEntry.getIndexNames())
tIPFilterParamsEntry.registerAugmentions(
    ("TIMETRA-FILTER-MIB",
     "tIPFilterParamsExtEntry")
)
tIPFilterParamsExtEntry.setIndexNames(*tIPFilterParamsEntry.getIndexNames())

# Managed Objects groups

tFilterLogGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 3)
)
tFilterLogGroup.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFilterLogRowStatus"),
        ("TIMETRA-FILTER-MIB", "tFilterLogDestination"),
        ("TIMETRA-FILTER-MIB", "tFilterLogDescription"),
        ("TIMETRA-FILTER-MIB", "tFilterLogMaxNumEntries"),
        ("TIMETRA-FILTER-MIB", "tFilterLogSysLogId"),
        ("TIMETRA-FILTER-MIB", "tFilterLogFileId"),
        ("TIMETRA-FILTER-MIB", "tFilterLogStopOnFull"),
        ("TIMETRA-FILTER-MIB", "tFilterLogEnabled"),
        ("TIMETRA-FILTER-MIB", "tFilterLogMaxInstances"),
        ("TIMETRA-FILTER-MIB", "tFilterLogInstances"),
        ("TIMETRA-FILTER-MIB", "tFilterLogBindings"))
)
if mibBuilder.loadTexts:
    tFilterLogGroup.setStatus("current")

tFilterRedirectPolicyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 4)
)
tFilterRedirectPolicyGroup.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFilterRPRowStatus"),
        ("TIMETRA-FILTER-MIB", "tFilterRPDescription"),
        ("TIMETRA-FILTER-MIB", "tFilterRPAdminState"),
        ("TIMETRA-FILTER-MIB", "tFilterRPActiveDest"),
        ("TIMETRA-FILTER-MIB", "tFilterRDRowStatus"),
        ("TIMETRA-FILTER-MIB", "tFilterRDDescription"),
        ("TIMETRA-FILTER-MIB", "tFilterRDAdminPriority"),
        ("TIMETRA-FILTER-MIB", "tFilterRDOperPriority"),
        ("TIMETRA-FILTER-MIB", "tFilterRDAdminState"),
        ("TIMETRA-FILTER-MIB", "tFilterRDOperState"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTRowStatus"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTOID"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTCommunity"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTSNMPVersion"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTInterval"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTTimeout"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTDropCount"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTHoldDown"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTHoldDownRemain"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTLastActionTime"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTLastOID"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTLastType"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTLastCounter32Val"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTLastUnsigned32Val"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTLastTimeTicksVal"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTLastInt32Val"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTLastOctetStringVal"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTLastIpAddressVal"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTLastOidVal"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTLastCounter64Val"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTLastOpaqueVal"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTLastAction"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTLastPrioChange"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTNextRespIndex"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTRespRowStatus"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTRespAction"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTRespPrioChange"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTRespOID"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTRespType"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTCounter32Val"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTUnsigned32Val"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTTimeTicksVal"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTInt32Val"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTOctetStringVal"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTIpAddressVal"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTOidVal"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTCounter64Val"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTOpaqueVal"),
        ("TIMETRA-FILTER-MIB", "tFilterRUTRowStatus"),
        ("TIMETRA-FILTER-MIB", "tFilterRUTURL"),
        ("TIMETRA-FILTER-MIB", "tFilterRUTHTTPVersion"),
        ("TIMETRA-FILTER-MIB", "tFilterRUTInterval"),
        ("TIMETRA-FILTER-MIB", "tFilterRUTTimeout"),
        ("TIMETRA-FILTER-MIB", "tFilterRUTDropCount"),
        ("TIMETRA-FILTER-MIB", "tFilterRUTHoldDown"),
        ("TIMETRA-FILTER-MIB", "tFilterRUTHoldDownRemain"),
        ("TIMETRA-FILTER-MIB", "tFilterRUTLastActionTime"),
        ("TIMETRA-FILTER-MIB", "tFilterRUTLastRetCode"),
        ("TIMETRA-FILTER-MIB", "tFilterRUTLastAction"),
        ("TIMETRA-FILTER-MIB", "tFilterRUTLastPrioChange"),
        ("TIMETRA-FILTER-MIB", "tFilterRUTRespRowStatus"),
        ("TIMETRA-FILTER-MIB", "tFilterRUTRespAction"),
        ("TIMETRA-FILTER-MIB", "tFilterRUTRespPrioChange"),
        ("TIMETRA-FILTER-MIB", "tFilterRPTRowStatus"),
        ("TIMETRA-FILTER-MIB", "tFilterRPTInterval"),
        ("TIMETRA-FILTER-MIB", "tFilterRPTTimeout"),
        ("TIMETRA-FILTER-MIB", "tFilterRPTDropCount"),
        ("TIMETRA-FILTER-MIB", "tFilterRPTHoldDown"),
        ("TIMETRA-FILTER-MIB", "tFilterRPTHoldDownRemain"),
        ("TIMETRA-FILTER-MIB", "tFilterRPTLastActionTime"),
        ("TIMETRA-FILTER-MIB", "tFilterRPTLastAction"))
)
if mibBuilder.loadTexts:
    tFilterRedirectPolicyGroup.setStatus("current")

tFilterScalarGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 7)
)
tFilterScalarGroup.setObjects(
    ("TIMETRA-FILTER-MIB", "tFilterDomainLastChanged")
)
if mibBuilder.loadTexts:
    tFilterScalarGroup.setStatus("current")

tFilterNotificationObjGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 8)
)
tFilterNotificationObjGroup.setObjects(
    ("TIMETRA-FILTER-MIB", "tFilterPBRDropReason")
)
if mibBuilder.loadTexts:
    tFilterNotificationObjGroup.setStatus("obsolete")

tIPv6FilterV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 11)
)
tIPv6FilterV4v0Group.setObjects(
      *(("TIMETRA-FILTER-MIB", "tIPv6FilterRowStatus"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterScope"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterDescription"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterDefaultAction"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsRowStatus"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsLogId"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDescription"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsAction"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsForwardNH"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsForwardNHIndirect"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsRemarkDSCP"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsRemarkDSCPMask"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsRemarkDot1p"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsSourceIpAddr"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsSourceIpMask"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDestinationIpAddr"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDestinationIpMask"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsNextHeader"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsSourcePortValue1"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsSourcePortValue2"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsSourcePortOperator"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDestPortValue1"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDestPortValue2"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDestPortOperator"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDSCP"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsTcpSyn"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsTcpAck"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsIcmpCode"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsIcmpType"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsCflowdSample"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsCflowdIfSample"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsForwardNHInterface"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsIngressHitCount"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsEgressHitCount"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsLogInstantiated"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsForwardRedPlcy"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsActiveDest"))
)
if mibBuilder.loadTexts:
    tIPv6FilterV4v0Group.setStatus("obsolete")

tIPFilterV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 12)
)
tIPFilterV4v0Group.setObjects(
      *(("TIMETRA-FILTER-MIB", "tIPFilterRowStatus"),
        ("TIMETRA-FILTER-MIB", "tIPFilterScope"),
        ("TIMETRA-FILTER-MIB", "tIPFilterDescription"),
        ("TIMETRA-FILTER-MIB", "tIPFilterDefaultAction"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsRowStatus"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsLogId"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDescription"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsAction"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsForwardNH"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsForwardNHIndirect"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsRemarkDSCP"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsRemarkDSCPMask"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsRemarkDot1p"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSourceIpAddr"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSourceIpMask"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDestinationIpAddr"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDestinationIpMask"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsProtocol"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSourcePortValue1"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSourcePortValue2"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSourcePortOperator"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDestPortValue1"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDestPortValue2"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDestPortOperator"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDSCP"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsFragment"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsOptionPresent"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsIpOptionValue"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsIpOptionMask"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsMultipleOption"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsTcpSyn"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsTcpAck"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsIcmpCode"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsIcmpType"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsCflowdSample"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsCflowdIfSample"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsForwardNHInterface"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsIngressHitCount"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsEgressHitCount"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsLogInstantiated"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsForwardRedPlcy"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsActiveDest"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsFwdSvcId"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsFwdSapPortId"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsFwdSapEncapVal"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsFwdSdpBind"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsRedirectURL"))
)
if mibBuilder.loadTexts:
    tIPFilterV4v0Group.setStatus("obsolete")

tMacFilterV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 13)
)
tMacFilterV4v0Group.setObjects(
      *(("TIMETRA-FILTER-MIB", "tMacFilterRowStatus"),
        ("TIMETRA-FILTER-MIB", "tMacFilterScope"),
        ("TIMETRA-FILTER-MIB", "tMacFilterDescription"),
        ("TIMETRA-FILTER-MIB", "tMacFilterDefaultAction"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsRowStatus"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsLogId"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsDescription"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsAction"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsFrameType"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsSrcMAC"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsSrcMACMask"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsDstMAC"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsDstMACMask"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsDot1pValue"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsDot1pMask"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsEtherType"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsDsap"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsDsapMask"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsSsap"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsSsapMask"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsSnapPid"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsSnapOui"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsIngressHitCount"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsEgressHitCount"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsLogInstantiated"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsFwdSvcId"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsFwdSapPortId"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsFwdSapEncapVal"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsFwdSdpBind"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsRedirectURL"))
)
if mibBuilder.loadTexts:
    tMacFilterV4v0Group.setStatus("obsolete")

tTodPoliciesV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 14)
)
tTodPoliciesV4v0Group.setObjects(
      *(("TIMETRA-FILTER-MIB", "tIPFilterParamsTimeRangeName"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsTimeRangeState"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsTimeRangeName"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsTimeRangeState"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsTimeRangeName"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsTimeRangeState"))
)
if mibBuilder.loadTexts:
    tTodPoliciesV4v0Group.setStatus("obsolete")

tmnxFilterObsoleteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 15)
)
tmnxFilterObsoleteGroup.setObjects(
    ("TIMETRA-FILTER-MIB", "tAutoIPFilterEntrySourceIpMask")
)
if mibBuilder.loadTexts:
    tmnxFilterObsoleteGroup.setStatus("current")

tIPFilterV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 17)
)
tIPFilterV5v0Group.setObjects(
      *(("TIMETRA-FILTER-MIB", "tIPFilterRowStatus"),
        ("TIMETRA-FILTER-MIB", "tIPFilterScope"),
        ("TIMETRA-FILTER-MIB", "tIPFilterDescription"),
        ("TIMETRA-FILTER-MIB", "tIPFilterDefaultAction"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsRowStatus"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsLogId"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDescription"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsAction"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsForwardNH"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsForwardNHIndirect"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsRemarkDSCP"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsRemarkDSCPMask"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsRemarkDot1p"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSourceIpAddr"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSourceIpMask"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDestinationIpAddr"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDestinationIpMask"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsProtocol"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSourcePortValue1"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSourcePortValue2"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSourcePortOperator"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDestPortValue1"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDestPortValue2"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDestPortOperator"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDSCP"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsFragment"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsOptionPresent"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsIpOptionValue"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsIpOptionMask"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsMultipleOption"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsTcpSyn"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsTcpAck"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsIcmpCode"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsIcmpType"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsCflowdSample"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsCflowdIfSample"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsForwardNHInterface"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsIngressHitCount"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsEgressHitCount"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsLogInstantiated"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsForwardRedPlcy"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsActiveDest"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsFwdSvcId"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsFwdSapPortId"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsFwdSapEncapVal"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsFwdSdpBind"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsRedirectURL"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSrcIpFullMask"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDestIpFullMask"))
)
if mibBuilder.loadTexts:
    tIPFilterV5v0Group.setStatus("obsolete")

tFilterLogV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 18)
)
tFilterLogV5v0Group.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFilterLogSummaryEnabled"),
        ("TIMETRA-FILTER-MIB", "tFilterLogSummaryCrit1"))
)
if mibBuilder.loadTexts:
    tFilterLogV5v0Group.setStatus("current")

tTodPolicies77450V5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 19)
)
tTodPolicies77450V5v0Group.setObjects(
      *(("TIMETRA-FILTER-MIB", "tIPFilterParamsTimeRangeName"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsTimeRangeState"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsTimeRangeName"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsTimeRangeState"))
)
if mibBuilder.loadTexts:
    tTodPolicies77450V5v0Group.setStatus("obsolete")

tTodPolicies77x0V5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 20)
)
tTodPolicies77x0V5v0Group.setObjects(
      *(("TIMETRA-FILTER-MIB", "tIPFilterParamsTimeRangeName"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsTimeRangeState"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsTimeRangeName"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsTimeRangeState"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsTimeRangeName"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsTimeRangeState"))
)
if mibBuilder.loadTexts:
    tTodPolicies77x0V5v0Group.setStatus("current")

tFilterNotificationObjV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 21)
)
tFilterNotificationObjV5v0Group.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFilterPBRDropReason"),
        ("TIMETRA-FILTER-MIB", "tFilterParmRow"),
        ("TIMETRA-FILTER-MIB", "tFilterAlarmDescription"))
)
if mibBuilder.loadTexts:
    tFilterNotificationObjV5v0Group.setStatus("obsolete")

tIPFilterV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 22)
)
tIPFilterV6v0Group.setObjects(
      *(("TIMETRA-FILTER-MIB", "tIPFilterRowStatus"),
        ("TIMETRA-FILTER-MIB", "tIPFilterScope"),
        ("TIMETRA-FILTER-MIB", "tIPFilterDescription"),
        ("TIMETRA-FILTER-MIB", "tIPFilterDefaultAction"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsRowStatus"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsLogId"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDescription"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsAction"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsForwardNH"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsForwardNHIndirect"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsRemarkDSCP"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsRemarkDSCPMask"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsRemarkDot1p"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSourceIpAddr"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSourceIpMask"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDestinationIpAddr"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDestinationIpMask"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsProtocol"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSourcePortValue1"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSourcePortValue2"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSourcePortOperator"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDestPortValue1"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDestPortValue2"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDestPortOperator"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDSCP"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsFragment"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsOptionPresent"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsIpOptionValue"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsIpOptionMask"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsMultipleOption"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsTcpSyn"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsTcpAck"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsIcmpCode"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsIcmpType"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsCflowdSample"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsCflowdIfSample"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsForwardNHInterface"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsIngressHitCount"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsEgressHitCount"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsLogInstantiated"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsForwardRedPlcy"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsActiveDest"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsFwdSvcId"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsFwdSapPortId"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsFwdSapEncapVal"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsFwdSdpBind"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsRedirectURL"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSrcIpFullMask"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDestIpFullMask"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsIngrHitByteCount"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsEgrHitByteCount"))
)
if mibBuilder.loadTexts:
    tIPFilterV6v0Group.setStatus("obsolete")

tMacFilterV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 23)
)
tMacFilterV6v0Group.setObjects(
      *(("TIMETRA-FILTER-MIB", "tMacFilterRowStatus"),
        ("TIMETRA-FILTER-MIB", "tMacFilterScope"),
        ("TIMETRA-FILTER-MIB", "tMacFilterDescription"),
        ("TIMETRA-FILTER-MIB", "tMacFilterDefaultAction"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsRowStatus"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsLogId"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsDescription"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsAction"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsFrameType"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsSrcMAC"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsSrcMACMask"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsDstMAC"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsDstMACMask"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsDot1pValue"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsDot1pMask"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsEtherType"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsDsap"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsDsapMask"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsSsap"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsSsapMask"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsSnapPid"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsSnapOui"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsIngressHitCount"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsEgressHitCount"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsLogInstantiated"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsFwdSvcId"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsFwdSapPortId"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsFwdSapEncapVal"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsFwdSdpBind"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsRedirectURL"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsIngrHitByteCount"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsEgrHitByteCount"))
)
if mibBuilder.loadTexts:
    tMacFilterV6v0Group.setStatus("obsolete")

tIPv6FilterV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 24)
)
tIPv6FilterV6v0Group.setObjects(
      *(("TIMETRA-FILTER-MIB", "tIPv6FilterRowStatus"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterScope"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterDescription"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterDefaultAction"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsRowStatus"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsLogId"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDescription"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsAction"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsForwardNH"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsForwardNHIndirect"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsRemarkDSCP"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsRemarkDSCPMask"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsRemarkDot1p"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsSourceIpAddr"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsSourceIpMask"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDestinationIpAddr"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDestinationIpMask"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsNextHeader"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsSourcePortValue1"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsSourcePortValue2"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsSourcePortOperator"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDestPortValue1"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDestPortValue2"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDestPortOperator"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDSCP"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsTcpSyn"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsTcpAck"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsIcmpCode"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsIcmpType"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsCflowdSample"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsCflowdIfSample"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsForwardNHInterface"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsIngressHitCount"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsEgressHitCount"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsLogInstantiated"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsForwardRedPlcy"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsActiveDest"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsIngrHitByteCount"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsEgrHitByteCount"))
)
if mibBuilder.loadTexts:
    tIPv6FilterV6v0Group.setStatus("obsolete")

tIPFilterV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 25)
)
tIPFilterV8v0Group.setObjects(
      *(("TIMETRA-FILTER-MIB", "tIPFilterRowStatus"),
        ("TIMETRA-FILTER-MIB", "tIPFilterScope"),
        ("TIMETRA-FILTER-MIB", "tIPFilterDescription"),
        ("TIMETRA-FILTER-MIB", "tIPFilterDefaultAction"),
        ("TIMETRA-FILTER-MIB", "tIPFilterRadiusInsertPt"),
        ("TIMETRA-FILTER-MIB", "tIPFilterRadiusInsertSize"),
        ("TIMETRA-FILTER-MIB", "tIPFilterCreditCntrlInsertPt"),
        ("TIMETRA-FILTER-MIB", "tIPFilterCreditCntrlInsertSize"),
        ("TIMETRA-FILTER-MIB", "tIPFilterSubInsertHighWmark"),
        ("TIMETRA-FILTER-MIB", "tIPFilterSubInsertLowWmark"),
        ("TIMETRA-FILTER-MIB", "tIpFilterCreditCntrlNbrInsertd"),
        ("TIMETRA-FILTER-MIB", "tIpFilterRadiusNbrInsertd"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsRowStatus"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsLogId"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDescription"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsAction"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsForwardNH"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsForwardNHIndirect"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsRemarkDSCP"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsRemarkDSCPMask"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsRemarkDot1p"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSourceIpAddr"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSourceIpMask"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDestinationIpAddr"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDestinationIpMask"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsProtocol"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSourcePortValue1"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSourcePortValue2"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSourcePortOperator"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDestPortValue1"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDestPortValue2"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDestPortOperator"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDSCP"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsFragment"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsOptionPresent"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsIpOptionValue"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsIpOptionMask"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsMultipleOption"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsTcpSyn"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsTcpAck"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsIcmpCode"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsIcmpType"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsCflowdSample"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsCflowdIfSample"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsForwardNHInterface"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsIngressHitCount"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsEgressHitCount"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsLogInstantiated"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsForwardRedPlcy"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsActiveDest"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsFwdSvcId"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsFwdSapPortId"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsFwdSapEncapVal"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsFwdSdpBind"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsRedirectURL"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSrcIpFullMask"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDestIpFullMask"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsIngrHitByteCount"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsEgrHitByteCount"),
        ("TIMETRA-FILTER-MIB", "tFltrGrpInsrtdEntriesFilterType"),
        ("TIMETRA-FILTER-MIB", "tFltrGrpInsrtdEntriesFilterId"),
        ("TIMETRA-FILTER-MIB", "tFltrGrpInsrtdEntriesApplication"),
        ("TIMETRA-FILTER-MIB", "tFltrGrpInsrtdEntriesLocation"),
        ("TIMETRA-FILTER-MIB", "tFltrGrpInsrtdEntriesResult"),
        ("TIMETRA-FILTER-MIB", "tFltrGrpInsrtdEntriesFeedback"),
        ("TIMETRA-FILTER-MIB", "tFltrGrpInsrtdEntriesExecute"))
)
if mibBuilder.loadTexts:
    tIPFilterV8v0Group.setStatus("obsolete")

tIPv6FilterV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 26)
)
tIPv6FilterV8v0Group.setObjects(
      *(("TIMETRA-FILTER-MIB", "tIPv6FilterRowStatus"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterScope"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterDescription"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterDefaultAction"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterRadiusInsertPt"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterRadiusInsertSize"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterCreditCntrlInsertPt"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterCreditCntrlInsertSize"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterSubInsertHighWmark"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterSubInsertLowWmark"),
        ("TIMETRA-FILTER-MIB", "tIpv6FilterCreditCntrlNbrInsertd"),
        ("TIMETRA-FILTER-MIB", "tIpv6FilterRadiusNbrInsertd"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsRowStatus"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsLogId"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDescription"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsAction"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsForwardNH"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsForwardNHIndirect"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsRemarkDSCP"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsRemarkDSCPMask"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsRemarkDot1p"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsSourceIpAddr"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsSourceIpMask"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDestinationIpAddr"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDestinationIpMask"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsNextHeader"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsSourcePortValue1"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsSourcePortValue2"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsSourcePortOperator"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDestPortValue1"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDestPortValue2"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDestPortOperator"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDSCP"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsTcpSyn"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsTcpAck"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsIcmpCode"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsIcmpType"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsCflowdSample"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsCflowdIfSample"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsForwardNHInterface"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsIngressHitCount"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsEgressHitCount"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsLogInstantiated"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsForwardRedPlcy"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsActiveDest"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsIngrHitByteCount"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsEgrHitByteCount"))
)
if mibBuilder.loadTexts:
    tIPv6FilterV8v0Group.setStatus("obsolete")

tFilterNotificationObjV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 27)
)
tFilterNotificationObjV8v0Group.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFilterPBRDropReason"),
        ("TIMETRA-FILTER-MIB", "tFilterParmRow"),
        ("TIMETRA-FILTER-MIB", "tFilterAlarmDescription"),
        ("TIMETRA-FILTER-MIB", "tFilterId"),
        ("TIMETRA-FILTER-MIB", "tFilterType"),
        ("TIMETRA-FILTER-MIB", "tFilterSubInsSpaceOwner"),
        ("TIMETRA-FILTER-MIB", "tFilterThresholdReached"))
)
if mibBuilder.loadTexts:
    tFilterNotificationObjV8v0Group.setStatus("obsolete")

tMacFilterV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 29)
)
tMacFilterV8v0Group.setObjects(
      *(("TIMETRA-FILTER-MIB", "tMacFilterRowStatus"),
        ("TIMETRA-FILTER-MIB", "tMacFilterScope"),
        ("TIMETRA-FILTER-MIB", "tMacFilterDescription"),
        ("TIMETRA-FILTER-MIB", "tMacFilterDefaultAction"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsRowStatus"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsLogId"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsDescription"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsAction"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsFrameType"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsSrcMAC"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsSrcMACMask"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsDstMAC"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsDstMACMask"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsDot1pValue"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsDot1pMask"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsEtherType"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsDsap"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsDsapMask"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsSsap"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsSsapMask"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsSnapPid"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsSnapOui"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsIngressHitCount"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsEgressHitCount"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsLogInstantiated"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsFwdSvcId"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsFwdSapPortId"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsFwdSapEncapVal"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsFwdSdpBind"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsRedirectURL"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsIngrHitByteCount"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsEgrHitByteCount"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsLowISID"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsHighISID"),
        ("TIMETRA-FILTER-MIB", "tMacFilterType"))
)
if mibBuilder.loadTexts:
    tMacFilterV8v0Group.setStatus("current")

tMacFilterVidFilteringV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 30)
)
tMacFilterVidFilteringV9v0Group.setObjects(
      *(("TIMETRA-FILTER-MIB", "tMacFilterParamsInnerTagValue"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsInnerTagMask"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsOuterTagValue"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsOuterTagMask"))
)
if mibBuilder.loadTexts:
    tMacFilterVidFilteringV9v0Group.setStatus("current")

tIPFilterV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 31)
)
tIPFilterV9v0Group.setObjects(
      *(("TIMETRA-FILTER-MIB", "tIPFilterRowStatus"),
        ("TIMETRA-FILTER-MIB", "tIPFilterScope"),
        ("TIMETRA-FILTER-MIB", "tIPFilterDescription"),
        ("TIMETRA-FILTER-MIB", "tIPFilterDefaultAction"),
        ("TIMETRA-FILTER-MIB", "tIPFilterRadiusInsertPt"),
        ("TIMETRA-FILTER-MIB", "tIPFilterRadiusInsertSize"),
        ("TIMETRA-FILTER-MIB", "tIPFilterCreditCntrlInsertPt"),
        ("TIMETRA-FILTER-MIB", "tIPFilterCreditCntrlInsertSize"),
        ("TIMETRA-FILTER-MIB", "tIPFilterSubInsertHighWmark"),
        ("TIMETRA-FILTER-MIB", "tIPFilterSubInsertLowWmark"),
        ("TIMETRA-FILTER-MIB", "tIpFilterCreditCntrlNbrInsertd"),
        ("TIMETRA-FILTER-MIB", "tIpFilterRadiusNbrInsertd"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsRowStatus"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsLogId"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDescription"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsAction"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsForwardNH"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsForwardNHIndirect"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsRemarkDSCP"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsRemarkDSCPMask"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsRemarkDot1p"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSourceIpAddr"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSourceIpMask"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDestinationIpAddr"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDestinationIpMask"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsProtocol"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSourcePortValue1"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSourcePortValue2"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSourcePortOperator"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDestPortValue1"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDestPortValue2"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDestPortOperator"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDSCP"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsFragment"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsOptionPresent"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsIpOptionValue"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsIpOptionMask"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsMultipleOption"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsTcpSyn"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsTcpAck"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsIcmpCode"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsIcmpType"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsCflowdSample"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsCflowdIfSample"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsForwardNHInterface"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsIngressHitCount"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsEgressHitCount"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsLogInstantiated"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsForwardRedPlcy"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsActiveDest"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsFwdSvcId"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsFwdSapPortId"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsFwdSapEncapVal"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsFwdSdpBind"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsRedirectURL"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSrcIpFullMask"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDestIpFullMask"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsIngrHitByteCount"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsEgrHitByteCount"),
        ("TIMETRA-FILTER-MIB", "tFltrGrpInsrtdEntriesFilterType"),
        ("TIMETRA-FILTER-MIB", "tFltrGrpInsrtdEntriesFilterId"),
        ("TIMETRA-FILTER-MIB", "tFltrGrpInsrtdEntriesApplication"),
        ("TIMETRA-FILTER-MIB", "tFltrGrpInsrtdEntriesLocation"),
        ("TIMETRA-FILTER-MIB", "tFltrGrpInsrtdEntriesResult"),
        ("TIMETRA-FILTER-MIB", "tFltrGrpInsrtdEntriesFeedback"),
        ("TIMETRA-FILTER-MIB", "tFltrGrpInsrtdEntriesExecute"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsFwdRtrId"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSrcRouteOption"))
)
if mibBuilder.loadTexts:
    tIPFilterV9v0Group.setStatus("obsolete")

tFilterNotificationObjV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 33)
)
tFilterNotificationObjV9v0Group.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFilterPBRDropReason"),
        ("TIMETRA-FILTER-MIB", "tFilterParmRow"),
        ("TIMETRA-FILTER-MIB", "tFilterAlarmDescription"),
        ("TIMETRA-FILTER-MIB", "tFilterId"),
        ("TIMETRA-FILTER-MIB", "tFilterType"),
        ("TIMETRA-FILTER-MIB", "tFilterSubInsSpaceOwner"),
        ("TIMETRA-FILTER-MIB", "tFilterThresholdReached"),
        ("TIMETRA-FILTER-MIB", "tFltrFlowSpecProblem"),
        ("TIMETRA-FILTER-MIB", "tFltrFlowSpecProblemDescription"),
        ("TIMETRA-FILTER-MIB", "tFltrFLowSpecNLRI"),
        ("TIMETRA-FILTER-MIB", "tFltrFlowSpecVrtrId"))
)
if mibBuilder.loadTexts:
    tFilterNotificationObjV9v0Group.setStatus("obsolete")

tDhcpFilterV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 34)
)
tDhcpFilterV9v0Group.setObjects(
      *(("TIMETRA-FILTER-MIB", "tDhcpFilterTableLastChanged"),
        ("TIMETRA-FILTER-MIB", "tDhcpFilterRowStatus"),
        ("TIMETRA-FILTER-MIB", "tDhcpFilterLastChanged"),
        ("TIMETRA-FILTER-MIB", "tDhcpFilterDescription"),
        ("TIMETRA-FILTER-MIB", "tDhcpFilterParamsTblLastChanged"),
        ("TIMETRA-FILTER-MIB", "tDhcpFilterParamsRowStatus"),
        ("TIMETRA-FILTER-MIB", "tDhcpFilterParamsLastChanged"),
        ("TIMETRA-FILTER-MIB", "tDhcpFilterParamsOptionNumber"),
        ("TIMETRA-FILTER-MIB", "tDhcpFilterParamsOptionMatch"),
        ("TIMETRA-FILTER-MIB", "tDhcpFilterParamsAction"))
)
if mibBuilder.loadTexts:
    tDhcpFilterV9v0Group.setStatus("obsolete")

tIPv6FilterV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 35)
)
tIPv6FilterV10v0Group.setObjects(
      *(("TIMETRA-FILTER-MIB", "tIPv6FilterRowStatus"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterScope"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterDescription"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterDefaultAction"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterRadiusInsertPt"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterRadiusInsertSize"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterCreditCntrlInsertPt"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterCreditCntrlInsertSize"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterSubInsertHighWmark"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterSubInsertLowWmark"),
        ("TIMETRA-FILTER-MIB", "tIpv6FilterCreditCntrlNbrInsertd"),
        ("TIMETRA-FILTER-MIB", "tIpv6FilterRadiusNbrInsertd"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsRowStatus"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsLogId"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDescription"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsAction"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsForwardNH"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsForwardNHIndirect"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsRemarkDSCP"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsRemarkDSCPMask"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsRemarkDot1p"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsSourceIpAddr"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsSourceIpMask"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDestinationIpAddr"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDestinationIpMask"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsNextHeader"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsSourcePortValue1"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsSourcePortValue2"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsSourcePortOperator"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDestPortValue1"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDestPortValue2"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDestPortOperator"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDSCP"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsTcpSyn"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsTcpAck"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsIcmpCode"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsIcmpType"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsCflowdSample"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsCflowdIfSample"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsForwardNHInterface"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsIngressHitCount"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsEgressHitCount"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsLogInstantiated"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsForwardRedPlcy"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsActiveDest"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsIngrHitByteCount"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsEgrHitByteCount"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsFwdSvcId"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsFwdSapPortId"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsFwdSapEncapVal"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsFwdSdpBind"))
)
if mibBuilder.loadTexts:
    tIPv6FilterV10v0Group.setStatus("obsolete")

tFilterNameV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 36)
)
tFilterNameV10v0Group.setObjects(
      *(("TIMETRA-FILTER-MIB", "tIpFilterName"),
        ("TIMETRA-FILTER-MIB", "tIpFilterNameId"),
        ("TIMETRA-FILTER-MIB", "tIpFilterNameLastChanged"),
        ("TIMETRA-FILTER-MIB", "tIpFilterNameRowStatus"),
        ("TIMETRA-FILTER-MIB", "tIpFilterNameTableLastChgd"),
        ("TIMETRA-FILTER-MIB", "tIpv6FilterName"),
        ("TIMETRA-FILTER-MIB", "tIpv6FilterNameId"),
        ("TIMETRA-FILTER-MIB", "tIpv6FilterNameLastChanged"),
        ("TIMETRA-FILTER-MIB", "tIpv6FilterNameRowStatus"),
        ("TIMETRA-FILTER-MIB", "tIpv6FilterNameTableLastChgd"),
        ("TIMETRA-FILTER-MIB", "tMacFilterName"),
        ("TIMETRA-FILTER-MIB", "tMacFilterNameId"),
        ("TIMETRA-FILTER-MIB", "tMacFilterNameLastChanged"),
        ("TIMETRA-FILTER-MIB", "tMacFilterNameRowStatus"),
        ("TIMETRA-FILTER-MIB", "tMacFilterNameTableLastChgd"))
)
if mibBuilder.loadTexts:
    tFilterNameV10v0Group.setStatus("current")

tDhcpFilterV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 37)
)
tDhcpFilterV10v0Group.setObjects(
      *(("TIMETRA-FILTER-MIB", "tDhcpFilterTableLastChanged"),
        ("TIMETRA-FILTER-MIB", "tDhcpFilterRowStatus"),
        ("TIMETRA-FILTER-MIB", "tDhcpFilterLastChanged"),
        ("TIMETRA-FILTER-MIB", "tDhcpFilterDescription"),
        ("TIMETRA-FILTER-MIB", "tDhcpFilterParamsTblLastChanged"),
        ("TIMETRA-FILTER-MIB", "tDhcpFilterParamsRowStatus"),
        ("TIMETRA-FILTER-MIB", "tDhcpFilterParamsLastChanged"),
        ("TIMETRA-FILTER-MIB", "tDhcpFilterParamsOptionNumber"),
        ("TIMETRA-FILTER-MIB", "tDhcpFilterParamsOptionMatch"),
        ("TIMETRA-FILTER-MIB", "tDhcpFilterParamsAction"),
        ("TIMETRA-FILTER-MIB", "tDhcpFilterParamsOptionValue"))
)
if mibBuilder.loadTexts:
    tDhcpFilterV10v0Group.setStatus("current")

tLiFilterV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 38)
)
tLiFilterV10v0Group.setObjects(
      *(("TIMETRA-FILTER-MIB", "tLiReservedBlockRowStatus"),
        ("TIMETRA-FILTER-MIB", "tLiReservedBlockDescription"),
        ("TIMETRA-FILTER-MIB", "tLiReservedBlockStart"),
        ("TIMETRA-FILTER-MIB", "tLiReservedBlockSize"),
        ("TIMETRA-FILTER-MIB", "tLiReservedBlockLastChanged"),
        ("TIMETRA-FILTER-MIB", "tLiReservedBlockTableLastChanged"),
        ("TIMETRA-FILTER-MIB", "tLiReservedBlockFltrRowStatus"),
        ("TIMETRA-FILTER-MIB", "tLiReservedBlockFltrLastChanged"),
        ("TIMETRA-FILTER-MIB", "tLiReservedBlockFltrTableLastChg"),
        ("TIMETRA-FILTER-MIB", "tLiFilterDescription"),
        ("TIMETRA-FILTER-MIB", "tLiFilterRowStatus"),
        ("TIMETRA-FILTER-MIB", "tLiFilterLastChanged"),
        ("TIMETRA-FILTER-MIB", "tLiFilterTableLastChanged"),
        ("TIMETRA-FILTER-MIB", "tLiFilterAssociationRowStatus"),
        ("TIMETRA-FILTER-MIB", "tLiFilterAssociationLastChg"),
        ("TIMETRA-FILTER-MIB", "tLiFilterAssociationTableLastChg"),
        ("TIMETRA-FILTER-MIB", "tLiMacFilterParamsDescription"),
        ("TIMETRA-FILTER-MIB", "tLiMacFilterParamsDstMAC"),
        ("TIMETRA-FILTER-MIB", "tLiMacFilterParamsDstMACMask"),
        ("TIMETRA-FILTER-MIB", "tLiMacFilterParamsFrameType"),
        ("TIMETRA-FILTER-MIB", "tLiMacFilterParamsRowStatus"),
        ("TIMETRA-FILTER-MIB", "tLiMacFilterParamsSrcMAC"),
        ("TIMETRA-FILTER-MIB", "tLiMacFilterParamsSrcMACMask"),
        ("TIMETRA-FILTER-MIB", "tLiMacFilterParamsLastChanged"),
        ("TIMETRA-FILTER-MIB", "tLiMacFilterParamsTableLastChg"),
        ("TIMETRA-FILTER-MIB", "tLiMacFilterParamsIngrHitCount"),
        ("TIMETRA-FILTER-MIB", "tLiMacFilterParamsEgrHitCount"),
        ("TIMETRA-FILTER-MIB", "tLiMacFilterParamsIngrHitBytes"),
        ("TIMETRA-FILTER-MIB", "tLiMacFilterParamsEgrHitBytes"))
)
if mibBuilder.loadTexts:
    tLiFilterV10v0Group.setStatus("obsolete")

tFilterPrefixListV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 39)
)
tFilterPrefixListV10v0Group.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFilterPrefixListTableLstChng"),
        ("TIMETRA-FILTER-MIB", "tFilterPrefixListRowStatus"),
        ("TIMETRA-FILTER-MIB", "tFilterPrefixListLastChanged"),
        ("TIMETRA-FILTER-MIB", "tFilterPrefixListDescription"),
        ("TIMETRA-FILTER-MIB", "tFilterPrefixListEntryTblLstChg"),
        ("TIMETRA-FILTER-MIB", "tFilterPrefixListEntryRowStatus"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSrcIpPrefixList"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDstIpPrefixList"))
)
if mibBuilder.loadTexts:
    tFilterPrefixListV10v0Group.setStatus("obsolete")

tIPv6FilterV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 40)
)
tIPv6FilterV11v0Group.setObjects(
      *(("TIMETRA-FILTER-MIB", "tIPv6FilterRowStatus"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterScope"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterDescription"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterDefaultAction"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterRadiusInsertPt"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterRadiusInsertSize"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterCreditCntrlInsertPt"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterCreditCntrlInsertSize"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterSubInsertHighWmark"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterSubInsertLowWmark"),
        ("TIMETRA-FILTER-MIB", "tIpv6FilterCreditCntrlNbrInsertd"),
        ("TIMETRA-FILTER-MIB", "tIpv6FilterRadiusNbrInsertd"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterHostSharedInsertPt"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterHostSharedInsertSize"),
        ("TIMETRA-FILTER-MIB", "tIpv6FilterHostSharedNbrInsertd"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterHostSharedHighWmark"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterHostSharedLowWmark"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterNbrHostSharedFltrs"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsRowStatus"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsLogId"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDescription"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsAction"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsForwardNH"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsForwardNHIndirect"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsRemarkDSCP"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsRemarkDSCPMask"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsRemarkDot1p"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsSourceIpAddr"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsSourceIpMask"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDestinationIpAddr"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDestinationIpMask"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsNextHeader"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsSourcePortValue1"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsSourcePortValue2"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsSourcePortOperator"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDestPortValue1"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDestPortValue2"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDestPortOperator"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDSCP"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsTcpSyn"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsTcpAck"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsIcmpCode"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsIcmpType"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsCflowdSample"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsCflowdIfSample"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsForwardNHInterface"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsIngressHitCount"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsEgressHitCount"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsLogInstantiated"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsForwardRedPlcy"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsActiveDest"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsIngrHitByteCount"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsEgrHitByteCount"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsFwdSvcId"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsFwdSapPortId"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsFwdSapEncapVal"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsFwdSdpBind"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsRedirectURL"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsSrcIpPrefixList"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDstIpPrefixList"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsFragment"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsHopByHopOpt"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsRoutingType0"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsPortSelector"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsSrcPortList"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDstPortList"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsFwdRtrId"))
)
if mibBuilder.loadTexts:
    tIPv6FilterV11v0Group.setStatus("obsolete")

tFilterEmbeddedInsertV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 41)
)
tFilterEmbeddedInsertV11v0Group.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFilterEmbeddedRefRowStatus"),
        ("TIMETRA-FILTER-MIB", "tFilterEmbeddedRefTableLstChg"),
        ("TIMETRA-FILTER-MIB", "tFilterEmbeddedRefOperState"),
        ("TIMETRA-FILTER-MIB", "tFilterEmbeddedRefAdminState"),
        ("TIMETRA-FILTER-MIB", "tFltrEmbedRefInfEntryCnt"),
        ("TIMETRA-FILTER-MIB", "tFltrEmbedRefInfEntryCntInsrtd"),
        ("TIMETRA-FILTER-MIB", "tFltrEmbedEntryInsrtEntryId"),
        ("TIMETRA-FILTER-MIB", "tFltrEmbedEntryRefOperState"))
)
if mibBuilder.loadTexts:
    tFilterEmbeddedInsertV11v0Group.setStatus("current")

tFilterPortListV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 42)
)
tFilterPortListV11v0Group.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFilterPortListTableLstChng"),
        ("TIMETRA-FILTER-MIB", "tFilterPortListRowStatus"),
        ("TIMETRA-FILTER-MIB", "tFilterPortListLastChanged"),
        ("TIMETRA-FILTER-MIB", "tFilterPortListDescription"),
        ("TIMETRA-FILTER-MIB", "tFilterPortListEntryTblLstChg"),
        ("TIMETRA-FILTER-MIB", "tFilterPortListEntryRowStatus"))
)
if mibBuilder.loadTexts:
    tFilterPortListV11v0Group.setStatus("current")

tFilterPrefixListV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 43)
)
tFilterPrefixListV11v0Group.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFilterPrefixListTableLstChng"),
        ("TIMETRA-FILTER-MIB", "tFilterPrefixListRowStatus"),
        ("TIMETRA-FILTER-MIB", "tFilterPrefixListLastChanged"),
        ("TIMETRA-FILTER-MIB", "tFilterPrefixListDescription"),
        ("TIMETRA-FILTER-MIB", "tFilterPrefixListEntryTblLstChg"),
        ("TIMETRA-FILTER-MIB", "tFilterPrefixListEntryRowStatus"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSrcIpPrefixList"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDstIpPrefixList"),
        ("TIMETRA-FILTER-MIB", "tFilterApplyPathTableLstChng"),
        ("TIMETRA-FILTER-MIB", "tFilterApplyPathRowStatus"),
        ("TIMETRA-FILTER-MIB", "tFilterApplyPathLastChanged"),
        ("TIMETRA-FILTER-MIB", "tFilterApplyPathMatch1"),
        ("TIMETRA-FILTER-MIB", "tFilterApplyPathMatch2"))
)
if mibBuilder.loadTexts:
    tFilterPrefixListV11v0Group.setStatus("current")

tIPFilterV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 44)
)
tIPFilterV11v0Group.setObjects(
      *(("TIMETRA-FILTER-MIB", "tIPFilterRowStatus"),
        ("TIMETRA-FILTER-MIB", "tIPFilterScope"),
        ("TIMETRA-FILTER-MIB", "tIPFilterDescription"),
        ("TIMETRA-FILTER-MIB", "tIPFilterDefaultAction"),
        ("TIMETRA-FILTER-MIB", "tIPFilterRadiusInsertPt"),
        ("TIMETRA-FILTER-MIB", "tIPFilterRadiusInsertSize"),
        ("TIMETRA-FILTER-MIB", "tIPFilterCreditCntrlInsertPt"),
        ("TIMETRA-FILTER-MIB", "tIPFilterCreditCntrlInsertSize"),
        ("TIMETRA-FILTER-MIB", "tIPFilterSubInsertHighWmark"),
        ("TIMETRA-FILTER-MIB", "tIPFilterSubInsertLowWmark"),
        ("TIMETRA-FILTER-MIB", "tIpFilterCreditCntrlNbrInsertd"),
        ("TIMETRA-FILTER-MIB", "tIpFilterRadiusNbrInsertd"),
        ("TIMETRA-FILTER-MIB", "tIPFilterHostSharedInsertPt"),
        ("TIMETRA-FILTER-MIB", "tIPFilterHostSharedInsertSize"),
        ("TIMETRA-FILTER-MIB", "tIpFilterHostSharedNbrInsertd"),
        ("TIMETRA-FILTER-MIB", "tIPFilterHostSharedHighWmark"),
        ("TIMETRA-FILTER-MIB", "tIPFilterHostSharedLowWmark"),
        ("TIMETRA-FILTER-MIB", "tIPFilterNbrHostSharedFltrs"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsRowStatus"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsLogId"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDescription"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsAction"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsForwardNH"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsForwardNHIndirect"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsRemarkDSCP"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsRemarkDSCPMask"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsRemarkDot1p"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSourceIpAddr"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSourceIpMask"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDestinationIpAddr"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDestinationIpMask"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsProtocol"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSourcePortValue1"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSourcePortValue2"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSourcePortOperator"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDestPortValue1"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDestPortValue2"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDestPortOperator"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDSCP"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsFragment"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsOptionPresent"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsIpOptionValue"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsIpOptionMask"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsMultipleOption"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsTcpSyn"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsTcpAck"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsIcmpCode"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsIcmpType"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsCflowdSample"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsCflowdIfSample"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsForwardNHInterface"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsIngressHitCount"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsEgressHitCount"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsLogInstantiated"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsForwardRedPlcy"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsActiveDest"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsFwdSvcId"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsFwdSapPortId"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsFwdSapEncapVal"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsFwdSdpBind"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsRedirectURL"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSrcIpFullMask"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDestIpFullMask"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsIngrHitByteCount"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsEgrHitByteCount"),
        ("TIMETRA-FILTER-MIB", "tFltrGrpInsrtdEntriesFilterType"),
        ("TIMETRA-FILTER-MIB", "tFltrGrpInsrtdEntriesFilterId"),
        ("TIMETRA-FILTER-MIB", "tFltrGrpInsrtdEntriesApplication"),
        ("TIMETRA-FILTER-MIB", "tFltrGrpInsrtdEntriesLocation"),
        ("TIMETRA-FILTER-MIB", "tFltrGrpInsrtdEntriesResult"),
        ("TIMETRA-FILTER-MIB", "tFltrGrpInsrtdEntriesFeedback"),
        ("TIMETRA-FILTER-MIB", "tFltrGrpInsrtdEntriesExecute"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsFwdRtrId"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSrcRouteOption"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsPortSelector"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSrcPortList"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDstPortList"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsExtTbleLstChgd"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsExtLastChanged"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsExtPktLenVal1"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsExtPktLenVal2"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsExtPktLenOper"))
)
if mibBuilder.loadTexts:
    tIPFilterV11v0Group.setStatus("obsolete")

tFilterNotificationObjV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 46)
)
tFilterNotificationObjV11v0Group.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFilterPBRDropReason"),
        ("TIMETRA-FILTER-MIB", "tFilterParmRow"),
        ("TIMETRA-FILTER-MIB", "tFilterAlarmDescription"),
        ("TIMETRA-FILTER-MIB", "tFilterId"),
        ("TIMETRA-FILTER-MIB", "tFilterType"),
        ("TIMETRA-FILTER-MIB", "tFilterSubInsSpaceOwner"),
        ("TIMETRA-FILTER-MIB", "tFilterThresholdReached"),
        ("TIMETRA-FILTER-MIB", "tFltrFlowSpecProblem"),
        ("TIMETRA-FILTER-MIB", "tFltrFlowSpecProblemDescription"),
        ("TIMETRA-FILTER-MIB", "tFltrFLowSpecNLRI"),
        ("TIMETRA-FILTER-MIB", "tFltrFlowSpecVrtrId"),
        ("TIMETRA-FILTER-MIB", "tFltrPrefixListType"),
        ("TIMETRA-FILTER-MIB", "tFltrPrefixListName"),
        ("TIMETRA-FILTER-MIB", "tFltrApplyPathSource"),
        ("TIMETRA-FILTER-MIB", "tFltrApplyPathIndex"),
        ("TIMETRA-FILTER-MIB", "tFltrNotifDescription"))
)
if mibBuilder.loadTexts:
    tFilterNotificationObjV11v0Group.setStatus("obsolete")

tIPFilterV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 47)
)
tIPFilterV12v0Group.setObjects(
      *(("TIMETRA-FILTER-MIB", "tIPFilterRowStatus"),
        ("TIMETRA-FILTER-MIB", "tIPFilterScope"),
        ("TIMETRA-FILTER-MIB", "tIPFilterDescription"),
        ("TIMETRA-FILTER-MIB", "tIPFilterDefaultAction"),
        ("TIMETRA-FILTER-MIB", "tIPFilterRadiusInsertPt"),
        ("TIMETRA-FILTER-MIB", "tIPFilterRadiusInsertSize"),
        ("TIMETRA-FILTER-MIB", "tIPFilterCreditCntrlInsertPt"),
        ("TIMETRA-FILTER-MIB", "tIPFilterCreditCntrlInsertSize"),
        ("TIMETRA-FILTER-MIB", "tIPFilterSubInsertHighWmark"),
        ("TIMETRA-FILTER-MIB", "tIPFilterSubInsertLowWmark"),
        ("TIMETRA-FILTER-MIB", "tIpFilterCreditCntrlNbrInsertd"),
        ("TIMETRA-FILTER-MIB", "tIpFilterRadiusNbrInsertd"),
        ("TIMETRA-FILTER-MIB", "tIPFilterHostSharedInsertPt"),
        ("TIMETRA-FILTER-MIB", "tIPFilterHostSharedInsertSize"),
        ("TIMETRA-FILTER-MIB", "tIpFilterHostSharedNbrInsertd"),
        ("TIMETRA-FILTER-MIB", "tIPFilterHostSharedHighWmark"),
        ("TIMETRA-FILTER-MIB", "tIPFilterHostSharedLowWmark"),
        ("TIMETRA-FILTER-MIB", "tIPFilterNbrHostSharedFltrs"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsRowStatus"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsLogId"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDescription"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsAction"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsForwardNH"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsForwardNHIndirect"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsRemarkDSCP"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsRemarkDSCPMask"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsRemarkDot1p"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSourceIpAddr"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSourceIpMask"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDestinationIpAddr"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDestinationIpMask"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsProtocol"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSourcePortValue1"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSourcePortValue2"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSourcePortOperator"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDestPortValue1"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDestPortValue2"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDestPortOperator"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDSCP"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsFragment"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsOptionPresent"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsIpOptionValue"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsIpOptionMask"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsMultipleOption"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsTcpSyn"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsTcpAck"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsIcmpCode"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsIcmpType"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsCflowdSample"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsCflowdIfSample"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsForwardNHInterface"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsIngressHitCount"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsEgressHitCount"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsLogInstantiated"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsForwardRedPlcy"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsActiveDest"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsFwdSvcId"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsFwdSapPortId"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsFwdSapEncapVal"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsFwdSdpBind"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsRedirectURL"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSrcIpFullMask"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDestIpFullMask"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsIngrHitByteCount"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsEgrHitByteCount"),
        ("TIMETRA-FILTER-MIB", "tFltrGrpInsrtdEntriesFilterType"),
        ("TIMETRA-FILTER-MIB", "tFltrGrpInsrtdEntriesFilterId"),
        ("TIMETRA-FILTER-MIB", "tFltrGrpInsrtdEntriesApplication"),
        ("TIMETRA-FILTER-MIB", "tFltrGrpInsrtdEntriesLocation"),
        ("TIMETRA-FILTER-MIB", "tFltrGrpInsrtdEntriesResult"),
        ("TIMETRA-FILTER-MIB", "tFltrGrpInsrtdEntriesFeedback"),
        ("TIMETRA-FILTER-MIB", "tFltrGrpInsrtdEntriesExecute"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsFwdRtrId"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSrcRouteOption"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsPortSelector"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSrcPortList"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDstPortList"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsExtTbleLstChgd"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsExtLastChanged"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsExtPktLenVal1"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsExtPktLenVal2"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsExtPktLenOper"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsRdirAllwRadOvrd"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsNatPolicyName"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsFwdLsp"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsFwdLspRtrId"))
)
if mibBuilder.loadTexts:
    tIPFilterV12v0Group.setStatus("current")

tIPv6FilterV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 48)
)
tIPv6FilterV12v0Group.setObjects(
      *(("TIMETRA-FILTER-MIB", "tIPv6FilterRowStatus"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterScope"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterDescription"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterDefaultAction"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterRadiusInsertPt"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterRadiusInsertSize"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterCreditCntrlInsertPt"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterCreditCntrlInsertSize"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterSubInsertHighWmark"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterSubInsertLowWmark"),
        ("TIMETRA-FILTER-MIB", "tIpv6FilterCreditCntrlNbrInsertd"),
        ("TIMETRA-FILTER-MIB", "tIpv6FilterRadiusNbrInsertd"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterHostSharedInsertPt"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterHostSharedInsertSize"),
        ("TIMETRA-FILTER-MIB", "tIpv6FilterHostSharedNbrInsertd"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterHostSharedHighWmark"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterHostSharedLowWmark"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterNbrHostSharedFltrs"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsRowStatus"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsLogId"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDescription"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsAction"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsForwardNH"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsForwardNHIndirect"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsRemarkDSCP"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsRemarkDSCPMask"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsRemarkDot1p"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsSourceIpAddr"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsSourceIpMask"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDestinationIpAddr"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDestinationIpMask"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsNextHeader"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsSourcePortValue1"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsSourcePortValue2"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsSourcePortOperator"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDestPortValue1"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDestPortValue2"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDestPortOperator"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDSCP"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsTcpSyn"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsTcpAck"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsIcmpCode"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsIcmpType"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsCflowdSample"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsCflowdIfSample"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsForwardNHInterface"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsIngressHitCount"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsEgressHitCount"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsLogInstantiated"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsForwardRedPlcy"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsActiveDest"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsIngrHitByteCount"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsEgrHitByteCount"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsFwdSvcId"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsFwdSapPortId"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsFwdSapEncapVal"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsFwdSdpBind"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsRedirectURL"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsSrcIpPrefixList"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDstIpPrefixList"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsFragment"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsHopByHopOpt"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsRoutingType0"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsPortSelector"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsSrcPortList"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDstPortList"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsRdirAllwRadOvrd"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsFwdRtrId"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsSrcIpFullMask"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDstIpFullMask"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsNatPolicyName"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsFlowLabel"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsFlowLabelMask"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsFwdLspRtrId"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsFwdLsp"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsExtTbleLstChgd"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsExtLastChanged"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsExtAhExtHdr"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsExtEspExtHdr"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsExtNatType"))
)
if mibBuilder.loadTexts:
    tIPv6FilterV12v0Group.setStatus("current")

tLiFilterV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 49)
)
tLiFilterV12v0Group.setObjects(
      *(("TIMETRA-FILTER-MIB", "tLiReservedBlockRowStatus"),
        ("TIMETRA-FILTER-MIB", "tLiReservedBlockDescription"),
        ("TIMETRA-FILTER-MIB", "tLiReservedBlockStart"),
        ("TIMETRA-FILTER-MIB", "tLiReservedBlockSize"),
        ("TIMETRA-FILTER-MIB", "tLiReservedBlockLastChanged"),
        ("TIMETRA-FILTER-MIB", "tLiReservedBlockTableLastChanged"),
        ("TIMETRA-FILTER-MIB", "tLiReservedBlockFltrRowStatus"),
        ("TIMETRA-FILTER-MIB", "tLiReservedBlockFltrLastChanged"),
        ("TIMETRA-FILTER-MIB", "tLiReservedBlockFltrTableLastChg"),
        ("TIMETRA-FILTER-MIB", "tLiFilterDescription"),
        ("TIMETRA-FILTER-MIB", "tLiFilterRowStatus"),
        ("TIMETRA-FILTER-MIB", "tLiFilterLastChanged"),
        ("TIMETRA-FILTER-MIB", "tLiFilterTableLastChanged"),
        ("TIMETRA-FILTER-MIB", "tLiFilterAssociationRowStatus"),
        ("TIMETRA-FILTER-MIB", "tLiFilterAssociationLastChg"),
        ("TIMETRA-FILTER-MIB", "tLiFilterAssociationTableLastChg"),
        ("TIMETRA-FILTER-MIB", "tLiMacFilterParamsDescription"),
        ("TIMETRA-FILTER-MIB", "tLiMacFilterParamsDstMAC"),
        ("TIMETRA-FILTER-MIB", "tLiMacFilterParamsDstMACMask"),
        ("TIMETRA-FILTER-MIB", "tLiMacFilterParamsFrameType"),
        ("TIMETRA-FILTER-MIB", "tLiMacFilterParamsRowStatus"),
        ("TIMETRA-FILTER-MIB", "tLiMacFilterParamsSrcMAC"),
        ("TIMETRA-FILTER-MIB", "tLiMacFilterParamsSrcMACMask"),
        ("TIMETRA-FILTER-MIB", "tLiMacFilterParamsLastChanged"),
        ("TIMETRA-FILTER-MIB", "tLiMacFilterParamsTableLastChg"),
        ("TIMETRA-FILTER-MIB", "tLiMacFilterParamsIngrHitCount"),
        ("TIMETRA-FILTER-MIB", "tLiMacFilterParamsEgrHitCount"),
        ("TIMETRA-FILTER-MIB", "tLiMacFilterParamsIngrHitBytes"),
        ("TIMETRA-FILTER-MIB", "tLiMacFilterParamsEgrHitBytes"),
        ("TIMETRA-FILTER-MIB", "tLiIpFilterParamsTableLastChg"),
        ("TIMETRA-FILTER-MIB", "tLiIpFilterParamsLastChanged"),
        ("TIMETRA-FILTER-MIB", "tLiIpFilterParamsRowStatus"),
        ("TIMETRA-FILTER-MIB", "tLiIpFilterParamsDescription"),
        ("TIMETRA-FILTER-MIB", "tLiIpFilterParamsSrcIpAddrType"),
        ("TIMETRA-FILTER-MIB", "tLiIpFilterParamsSrcIpAddr"),
        ("TIMETRA-FILTER-MIB", "tLiIpFilterParamsSrcIpFullMask"),
        ("TIMETRA-FILTER-MIB", "tLiIpFilterParamsDstIpAddrType"),
        ("TIMETRA-FILTER-MIB", "tLiIpFilterParamsDstIpAddr"),
        ("TIMETRA-FILTER-MIB", "tLiIpFilterParamsDstIpFullMask"),
        ("TIMETRA-FILTER-MIB", "tLiIpFilterParamsProtocolNextHdr"),
        ("TIMETRA-FILTER-MIB", "tLiIpFilterParamsSrcPortValue1"),
        ("TIMETRA-FILTER-MIB", "tLiIpFilterParamsSrcPortValue2"),
        ("TIMETRA-FILTER-MIB", "tLiIpFilterParamsSrcPortOper"),
        ("TIMETRA-FILTER-MIB", "tLiIpFilterParamsDstPortValue1"),
        ("TIMETRA-FILTER-MIB", "tLiIpFilterParamsDstPortValue2"),
        ("TIMETRA-FILTER-MIB", "tLiIpFilterParamsDstPortOper"),
        ("TIMETRA-FILTER-MIB", "tLiIpFltrParamsInfIngrHitCount"),
        ("TIMETRA-FILTER-MIB", "tLiIpFltrParamsInfEgrHitCount"),
        ("TIMETRA-FILTER-MIB", "tLiIpFltrParamsInfIngrHitBytes"),
        ("TIMETRA-FILTER-MIB", "tLiIpFltrParamsInfEgrHitBytes"))
)
if mibBuilder.loadTexts:
    tLiFilterV12v0Group.setStatus("current")

tFilterEmbeddedInsertV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 50)
)
tFilterEmbeddedInsertV12v0Group.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFilterEmbedOpenflowRowStatus"),
        ("TIMETRA-FILTER-MIB", "tFilterEmbedOpenflowTableLstChg"),
        ("TIMETRA-FILTER-MIB", "tFilterEmbedOpenflowOperState"),
        ("TIMETRA-FILTER-MIB", "tFilterEmbedOpenflowAdminState"),
        ("TIMETRA-FILTER-MIB", "tFltrEmbedOfInfoEntryCnt"),
        ("TIMETRA-FILTER-MIB", "tFltrEmbedOfInfoEntryCntInsrtd"),
        ("TIMETRA-FILTER-MIB", "tFltrEmbedOfEntryInsrtEntryId"),
        ("TIMETRA-FILTER-MIB", "tFltrEmbedOfEntryInsrtEntryState"))
)
if mibBuilder.loadTexts:
    tFilterEmbeddedInsertV12v0Group.setStatus("current")

tFilterNotificationObjV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 53)
)
tFilterNotificationObjV12v0Group.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFilterPBRDropReason"),
        ("TIMETRA-FILTER-MIB", "tFilterParmRow"),
        ("TIMETRA-FILTER-MIB", "tFilterAlarmDescription"),
        ("TIMETRA-FILTER-MIB", "tFilterId"),
        ("TIMETRA-FILTER-MIB", "tFilterType"),
        ("TIMETRA-FILTER-MIB", "tFilterSubInsSpaceOwner"),
        ("TIMETRA-FILTER-MIB", "tFilterThresholdReached"),
        ("TIMETRA-FILTER-MIB", "tFltrFlowSpecProblem"),
        ("TIMETRA-FILTER-MIB", "tFltrFlowSpecProblemDescription"),
        ("TIMETRA-FILTER-MIB", "tFltrFLowSpecNLRI"),
        ("TIMETRA-FILTER-MIB", "tFltrFlowSpecVrtrId"),
        ("TIMETRA-FILTER-MIB", "tFltrPrefixListType"),
        ("TIMETRA-FILTER-MIB", "tFltrPrefixListName"),
        ("TIMETRA-FILTER-MIB", "tFltrApplyPathSource"),
        ("TIMETRA-FILTER-MIB", "tFltrApplyPathIndex"),
        ("TIMETRA-FILTER-MIB", "tFltrNotifDescription"),
        ("TIMETRA-FILTER-MIB", "tFltrMdaId"))
)
if mibBuilder.loadTexts:
    tFilterNotificationObjV12v0Group.setStatus("current")


# Notification objects

tIPFilterPBRPacketsDrop = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 21, 0, 1)
)
tIPFilterPBRPacketsDrop.setObjects(
      *(("TIMETRA-FILTER-MIB", "tIPFilterParamsForwardNHInterface"),
        ("TIMETRA-FILTER-MIB", "tFilterPBRDropReason"))
)
if mibBuilder.loadTexts:
    tIPFilterPBRPacketsDrop.setStatus(
        "current"
    )

tFilterEntryActivationFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 21, 0, 2)
)
tFilterEntryActivationFailed.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFilterParmRow"),
        ("TIMETRA-FILTER-MIB", "tFilterAlarmDescription"))
)
if mibBuilder.loadTexts:
    tFilterEntryActivationFailed.setStatus(
        "current"
    )

tFilterEntryActivationRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 21, 0, 3)
)
tFilterEntryActivationRestored.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFilterParmRow"),
        ("TIMETRA-FILTER-MIB", "tFilterAlarmDescription"))
)
if mibBuilder.loadTexts:
    tFilterEntryActivationRestored.setStatus(
        "current"
    )

tFilterSubInsSpaceAlarmRaised = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 21, 0, 4)
)
tFilterSubInsSpaceAlarmRaised.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFilterType"),
        ("TIMETRA-FILTER-MIB", "tFilterId"),
        ("TIMETRA-FILTER-MIB", "tFilterSubInsSpaceOwner"),
        ("TIMETRA-FILTER-MIB", "tFilterThresholdReached"))
)
if mibBuilder.loadTexts:
    tFilterSubInsSpaceAlarmRaised.setStatus(
        "current"
    )

tFilterSubInsSpaceAlarmCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 21, 0, 5)
)
tFilterSubInsSpaceAlarmCleared.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFilterType"),
        ("TIMETRA-FILTER-MIB", "tFilterId"),
        ("TIMETRA-FILTER-MIB", "tFilterSubInsSpaceOwner"),
        ("TIMETRA-FILTER-MIB", "tFilterThresholdReached"))
)
if mibBuilder.loadTexts:
    tFilterSubInsSpaceAlarmCleared.setStatus(
        "current"
    )

tFilterSubInsFltrEntryDropped = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 21, 0, 6)
)
tFilterSubInsFltrEntryDropped.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFilterType"),
        ("TIMETRA-FILTER-MIB", "tFilterId"),
        ("TIMETRA-FILTER-MIB", "tFilterSubInsSpaceOwner"),
        ("TIMETRA-FILTER-MIB", "tFilterAlarmDescription"))
)
if mibBuilder.loadTexts:
    tFilterSubInsFltrEntryDropped.setStatus(
        "current"
    )

tFilterBgpFlowSpecProblem = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 21, 0, 7)
)
tFilterBgpFlowSpecProblem.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFilterType"),
        ("TIMETRA-FILTER-MIB", "tFltrFlowSpecVrtrId"),
        ("TIMETRA-FILTER-MIB", "tFltrFlowSpecProblem"),
        ("TIMETRA-FILTER-MIB", "tFltrFlowSpecProblemDescription"),
        ("TIMETRA-FILTER-MIB", "tFltrFLowSpecNLRI"))
)
if mibBuilder.loadTexts:
    tFilterBgpFlowSpecProblem.setStatus(
        "current"
    )

tFilterApplyPathProblem = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 21, 0, 8)
)
tFilterApplyPathProblem.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFltrPrefixListType"),
        ("TIMETRA-FILTER-MIB", "tFltrPrefixListName"),
        ("TIMETRA-FILTER-MIB", "tFltrApplyPathSource"),
        ("TIMETRA-FILTER-MIB", "tFltrApplyPathIndex"),
        ("TIMETRA-FILTER-MIB", "tFilterAlarmDescription"))
)
if mibBuilder.loadTexts:
    tFilterApplyPathProblem.setStatus(
        "current"
    )

tFilterRadSharedFltrAlarmRaised = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 21, 0, 9)
)
tFilterRadSharedFltrAlarmRaised.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFilterType"),
        ("TIMETRA-FILTER-MIB", "tFilterId"),
        ("TIMETRA-FILTER-MIB", "tFilterThresholdReached"))
)
if mibBuilder.loadTexts:
    tFilterRadSharedFltrAlarmRaised.setStatus(
        "current"
    )

tFilterRadSharedFltrAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 21, 0, 10)
)
tFilterRadSharedFltrAlarmClear.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFilterType"),
        ("TIMETRA-FILTER-MIB", "tFilterId"),
        ("TIMETRA-FILTER-MIB", "tFilterThresholdReached"))
)
if mibBuilder.loadTexts:
    tFilterRadSharedFltrAlarmClear.setStatus(
        "current"
    )

tFilterEmbeddingOperStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 21, 0, 11)
)
tFilterEmbeddingOperStateChange.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFilterEmbeddedRefOperState"),
        ("TIMETRA-FILTER-MIB", "tFltrNotifDescription"))
)
if mibBuilder.loadTexts:
    tFilterEmbeddingOperStateChange.setStatus(
        "current"
    )

tFilterEmbedOpenflowOperStateChg = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 21, 0, 12)
)
tFilterEmbedOpenflowOperStateChg.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFilterEmbedOpenflowOperState"),
        ("TIMETRA-FILTER-MIB", "tFltrNotifDescription"))
)
if mibBuilder.loadTexts:
    tFilterEmbedOpenflowOperStateChg.setStatus(
        "current"
    )

tFilterTmsEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 21, 0, 13)
)
tFilterTmsEvent.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFltrMdaId"),
        ("TIMETRA-FILTER-MIB", "tFltrNotifDescription"))
)
if mibBuilder.loadTexts:
    tFilterTmsEvent.setStatus(
        "current"
    )


# Notifications groups

tFilterNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 9)
)
tFilterNotificationsGroup.setObjects(
    ("TIMETRA-FILTER-MIB", "tIPFilterPBRPacketsDrop")
)
if mibBuilder.loadTexts:
    tFilterNotificationsGroup.setStatus(
        "obsolete"
    )

tToDPoliciesV5v0NotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 16)
)
tToDPoliciesV5v0NotifyGroup.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFilterEntryActivationFailed"),
        ("TIMETRA-FILTER-MIB", "tFilterEntryActivationRestored"))
)
if mibBuilder.loadTexts:
    tToDPoliciesV5v0NotifyGroup.setStatus(
        "current"
    )

tFilterNotificationsV8v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 28)
)
tFilterNotificationsV8v0Group.setObjects(
      *(("TIMETRA-FILTER-MIB", "tIPFilterPBRPacketsDrop"),
        ("TIMETRA-FILTER-MIB", "tFilterSubInsSpaceAlarmRaised"),
        ("TIMETRA-FILTER-MIB", "tFilterSubInsSpaceAlarmCleared"),
        ("TIMETRA-FILTER-MIB", "tFilterSubInsFltrEntryDropped"))
)
if mibBuilder.loadTexts:
    tFilterNotificationsV8v0Group.setStatus(
        "obsolete"
    )

tFilterNotificationsV9v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 32)
)
tFilterNotificationsV9v0Group.setObjects(
      *(("TIMETRA-FILTER-MIB", "tIPFilterPBRPacketsDrop"),
        ("TIMETRA-FILTER-MIB", "tFilterSubInsSpaceAlarmRaised"),
        ("TIMETRA-FILTER-MIB", "tFilterSubInsSpaceAlarmCleared"),
        ("TIMETRA-FILTER-MIB", "tFilterSubInsFltrEntryDropped"),
        ("TIMETRA-FILTER-MIB", "tFilterBgpFlowSpecProblem"))
)
if mibBuilder.loadTexts:
    tFilterNotificationsV9v0Group.setStatus(
        "obsolete"
    )

tFilterNotificationsV11v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 45)
)
tFilterNotificationsV11v0Group.setObjects(
      *(("TIMETRA-FILTER-MIB", "tIPFilterPBRPacketsDrop"),
        ("TIMETRA-FILTER-MIB", "tFilterSubInsSpaceAlarmRaised"),
        ("TIMETRA-FILTER-MIB", "tFilterSubInsSpaceAlarmCleared"),
        ("TIMETRA-FILTER-MIB", "tFilterSubInsFltrEntryDropped"),
        ("TIMETRA-FILTER-MIB", "tFilterBgpFlowSpecProblem"),
        ("TIMETRA-FILTER-MIB", "tFilterApplyPathProblem"),
        ("TIMETRA-FILTER-MIB", "tFilterRadSharedFltrAlarmRaised"),
        ("TIMETRA-FILTER-MIB", "tFilterRadSharedFltrAlarmClear"),
        ("TIMETRA-FILTER-MIB", "tFilterEmbeddingOperStateChange"))
)
if mibBuilder.loadTexts:
    tFilterNotificationsV11v0Group.setStatus(
        "current"
    )

tFilterNotificationsV12v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 51)
)
tFilterNotificationsV12v0Group.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFilterEmbedOpenflowOperStateChg"),
        ("TIMETRA-FILTER-MIB", "tFilterTmsEvent"))
)
if mibBuilder.loadTexts:
    tFilterNotificationsV12v0Group.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tFilter7450V4v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 1, 4)
)
tFilter7450V4v0Compliance.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFilterScalarGroup"),
        ("TIMETRA-FILTER-MIB", "tIPFilterV4v0Group"),
        ("TIMETRA-FILTER-MIB", "tMacFilterV4v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterLogGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterRedirectPolicyGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterNotificationsGroup"))
)
if mibBuilder.loadTexts:
    tFilter7450V4v0Compliance.setStatus(
        "obsolete"
    )

tFilter7750V4v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 1, 5)
)
tFilter7750V4v0Compliance.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFilterScalarGroup"),
        ("TIMETRA-FILTER-MIB", "tIPFilterV4v0Group"),
        ("TIMETRA-FILTER-MIB", "tMacFilterV4v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterLogGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterRedirectPolicyGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterNotificationsGroup"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterV4v0Group"))
)
if mibBuilder.loadTexts:
    tFilter7750V4v0Compliance.setStatus(
        "obsolete"
    )

tFilter7450V5v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 1, 6)
)
tFilter7450V5v0Compliance.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFilterScalarGroup"),
        ("TIMETRA-FILTER-MIB", "tIPFilterV5v0Group"),
        ("TIMETRA-FILTER-MIB", "tMacFilterV4v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterLogGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterRedirectPolicyGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterNotificationsGroup"),
        ("TIMETRA-FILTER-MIB", "tTodPolicies77450V5v0Group"),
        ("TIMETRA-FILTER-MIB", "tToDPoliciesV5v0NotifyGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterLogV5v0Group"))
)
if mibBuilder.loadTexts:
    tFilter7450V5v0Compliance.setStatus(
        "obsolete"
    )

tFilter77x0V5v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 1, 7)
)
tFilter77x0V5v0Compliance.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFilterScalarGroup"),
        ("TIMETRA-FILTER-MIB", "tIPFilterV5v0Group"),
        ("TIMETRA-FILTER-MIB", "tMacFilterV4v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterLogGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterRedirectPolicyGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterNotificationsGroup"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterV4v0Group"),
        ("TIMETRA-FILTER-MIB", "tTodPolicies77x0V5v0Group"),
        ("TIMETRA-FILTER-MIB", "tToDPoliciesV5v0NotifyGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterLogV5v0Group"))
)
if mibBuilder.loadTexts:
    tFilter77x0V5v0Compliance.setStatus(
        "obsolete"
    )

tFilter7450V6v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 1, 8)
)
tFilter7450V6v0Compliance.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFilterScalarGroup"),
        ("TIMETRA-FILTER-MIB", "tIPFilterV6v0Group"),
        ("TIMETRA-FILTER-MIB", "tMacFilterV6v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterLogGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterRedirectPolicyGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterNotificationsGroup"),
        ("TIMETRA-FILTER-MIB", "tTodPolicies77450V5v0Group"),
        ("TIMETRA-FILTER-MIB", "tToDPoliciesV5v0NotifyGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterLogV5v0Group"))
)
if mibBuilder.loadTexts:
    tFilter7450V6v0Compliance.setStatus(
        "obsolete"
    )

tFilter77x0V6v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 1, 9)
)
tFilter77x0V6v0Compliance.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFilterScalarGroup"),
        ("TIMETRA-FILTER-MIB", "tIPFilterV6v0Group"),
        ("TIMETRA-FILTER-MIB", "tMacFilterV6v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterLogGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterRedirectPolicyGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterNotificationsGroup"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterV6v0Group"),
        ("TIMETRA-FILTER-MIB", "tTodPolicies77x0V5v0Group"),
        ("TIMETRA-FILTER-MIB", "tToDPoliciesV5v0NotifyGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterLogV5v0Group"))
)
if mibBuilder.loadTexts:
    tFilter77x0V6v0Compliance.setStatus(
        "obsolete"
    )

tFilter7450V8v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 1, 10)
)
tFilter7450V8v0Compliance.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFilterScalarGroup"),
        ("TIMETRA-FILTER-MIB", "tIPFilterV8v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterLogGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterLogV5v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterRedirectPolicyGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterNotificationsV8v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterNotificationObjV8v0Group"),
        ("TIMETRA-FILTER-MIB", "tTodPolicies77450V5v0Group"),
        ("TIMETRA-FILTER-MIB", "tToDPoliciesV5v0NotifyGroup"))
)
if mibBuilder.loadTexts:
    tFilter7450V8v0Compliance.setStatus(
        "obsolete"
    )

tFilter77x0V8v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 1, 11)
)
tFilter77x0V8v0Compliance.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFilterScalarGroup"),
        ("TIMETRA-FILTER-MIB", "tIPFilterV8v0Group"),
        ("TIMETRA-FILTER-MIB", "tMacFilterV8v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterLogGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterLogV5v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterRedirectPolicyGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterNotificationsV8v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterNotificationObjV8v0Group"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterV8v0Group"),
        ("TIMETRA-FILTER-MIB", "tTodPolicies77x0V5v0Group"),
        ("TIMETRA-FILTER-MIB", "tToDPoliciesV5v0NotifyGroup"))
)
if mibBuilder.loadTexts:
    tFilter77x0V8v0Compliance.setStatus(
        "obsolete"
    )

tFilter7xxxV9v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 1, 12)
)
tFilter7xxxV9v0Compliance.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFilterScalarGroup"),
        ("TIMETRA-FILTER-MIB", "tIPFilterV9v0Group"),
        ("TIMETRA-FILTER-MIB", "tMacFilterV8v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterLogGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterLogV5v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterRedirectPolicyGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterNotificationsV9v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterNotificationObjV9v0Group"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterV8v0Group"),
        ("TIMETRA-FILTER-MIB", "tTodPolicies77x0V5v0Group"),
        ("TIMETRA-FILTER-MIB", "tToDPoliciesV5v0NotifyGroup"),
        ("TIMETRA-FILTER-MIB", "tMacFilterVidFilteringV9v0Group"),
        ("TIMETRA-FILTER-MIB", "tDhcpFilterV9v0Group"))
)
if mibBuilder.loadTexts:
    tFilter7xxxV9v0Compliance.setStatus(
        "obsolete"
    )

tFilter7xxxV10v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 1, 13)
)
tFilter7xxxV10v0Compliance.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFilterScalarGroup"),
        ("TIMETRA-FILTER-MIB", "tIPFilterV9v0Group"),
        ("TIMETRA-FILTER-MIB", "tMacFilterV8v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterLogGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterLogV5v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterRedirectPolicyGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterNotificationsV9v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterNotificationObjV9v0Group"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterV10v0Group"),
        ("TIMETRA-FILTER-MIB", "tTodPolicies77x0V5v0Group"),
        ("TIMETRA-FILTER-MIB", "tToDPoliciesV5v0NotifyGroup"),
        ("TIMETRA-FILTER-MIB", "tMacFilterVidFilteringV9v0Group"),
        ("TIMETRA-FILTER-MIB", "tDhcpFilterV10v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterNameV10v0Group"),
        ("TIMETRA-FILTER-MIB", "tLiFilterV10v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterPrefixListV10v0Group"))
)
if mibBuilder.loadTexts:
    tFilter7xxxV10v0Compliance.setStatus(
        "obsolete"
    )

tFilter7xxxV11v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 1, 14)
)
tFilter7xxxV11v0Compliance.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFilterScalarGroup"),
        ("TIMETRA-FILTER-MIB", "tIPFilterV11v0Group"),
        ("TIMETRA-FILTER-MIB", "tMacFilterV8v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterLogGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterLogV5v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterRedirectPolicyGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterNotificationsV11v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterNotificationObjV11v0Group"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterV11v0Group"),
        ("TIMETRA-FILTER-MIB", "tTodPolicies77x0V5v0Group"),
        ("TIMETRA-FILTER-MIB", "tToDPoliciesV5v0NotifyGroup"),
        ("TIMETRA-FILTER-MIB", "tMacFilterVidFilteringV9v0Group"),
        ("TIMETRA-FILTER-MIB", "tDhcpFilterV10v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterNameV10v0Group"),
        ("TIMETRA-FILTER-MIB", "tLiFilterV10v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterPrefixListV11v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterEmbeddedInsertV11v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterPortListV11v0Group"))
)
if mibBuilder.loadTexts:
    tFilter7xxxV11v0Compliance.setStatus(
        "obsolete"
    )

tFilter7xxxV12v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 1, 15)
)
tFilter7xxxV12v0Compliance.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFilterScalarGroup"),
        ("TIMETRA-FILTER-MIB", "tIPFilterV12v0Group"),
        ("TIMETRA-FILTER-MIB", "tMacFilterV8v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterLogGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterLogV5v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterRedirectPolicyGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterNotificationsV11v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterNotificationsV12v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterNotificationObjV12v0Group"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterV12v0Group"),
        ("TIMETRA-FILTER-MIB", "tTodPolicies77x0V5v0Group"),
        ("TIMETRA-FILTER-MIB", "tToDPoliciesV5v0NotifyGroup"),
        ("TIMETRA-FILTER-MIB", "tMacFilterVidFilteringV9v0Group"),
        ("TIMETRA-FILTER-MIB", "tDhcpFilterV10v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterNameV10v0Group"),
        ("TIMETRA-FILTER-MIB", "tLiFilterV12v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterPrefixListV11v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterEmbeddedInsertV11v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterEmbeddedInsertV12v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterPortListV11v0Group"))
)
if mibBuilder.loadTexts:
    tFilter7xxxV12v0Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-FILTER-MIB",
    **{"TFilterID": TFilterID,
       "TIPFilterID": TIPFilterID,
       "TIPFilterIdOrEmpty": TIPFilterIdOrEmpty,
       "TMACFilterID": TMACFilterID,
       "TAnyFilterID": TAnyFilterID,
       "TFilterScope": TFilterScope,
       "TItemMatch": TItemMatch,
       "TEntryIndicator": TEntryIndicator,
       "TEntryId": TEntryId,
       "TAnyEntryId": TAnyEntryId,
       "TEntryIdOrZero": TEntryIdOrZero,
       "TFilterAction": TFilterAction,
       "TFilterActionOrDefault": TFilterActionOrDefault,
       "TFilterLogId": TFilterLogId,
       "TFilterLogDestination": TFilterLogDestination,
       "TTimeRangeState": TTimeRangeState,
       "TFilterLogSummaryCriterium": TFilterLogSummaryCriterium,
       "TFilterType": TFilterType,
       "TFilterSubInsSpaceOwner": TFilterSubInsSpaceOwner,
       "TDHCPFilterID": TDHCPFilterID,
       "TDhcpFilterAction": TDhcpFilterAction,
       "TDhcpFilterMatch": TDhcpFilterMatch,
       "TFltrPrefixListType": TFltrPrefixListType,
       "TmnxEmbeddedFltrOperState": TmnxEmbeddedFltrOperState,
       "TmnxFltrEmbeddedEntryState": TmnxFltrEmbeddedEntryState,
       "TmnxFilterApplyPathSource": TmnxFilterApplyPathSource,
       "TFltrPortSelector": TFltrPortSelector,
       "TFilterPacketLength": TFilterPacketLength,
       "timetraFilterMIBModule": timetraFilterMIBModule,
       "tFilterMIBConformance": tFilterMIBConformance,
       "tFilterMIBCompliances": tFilterMIBCompliances,
       "tFilter7450V4v0Compliance": tFilter7450V4v0Compliance,
       "tFilter7750V4v0Compliance": tFilter7750V4v0Compliance,
       "tFilter7450V5v0Compliance": tFilter7450V5v0Compliance,
       "tFilter77x0V5v0Compliance": tFilter77x0V5v0Compliance,
       "tFilter7450V6v0Compliance": tFilter7450V6v0Compliance,
       "tFilter77x0V6v0Compliance": tFilter77x0V6v0Compliance,
       "tFilter7450V8v0Compliance": tFilter7450V8v0Compliance,
       "tFilter77x0V8v0Compliance": tFilter77x0V8v0Compliance,
       "tFilter7xxxV9v0Compliance": tFilter7xxxV9v0Compliance,
       "tFilter7xxxV10v0Compliance": tFilter7xxxV10v0Compliance,
       "tFilter7xxxV11v0Compliance": tFilter7xxxV11v0Compliance,
       "tFilter7xxxV12v0Compliance": tFilter7xxxV12v0Compliance,
       "tFilterMIBGroups": tFilterMIBGroups,
       "tFilterLogGroup": tFilterLogGroup,
       "tFilterRedirectPolicyGroup": tFilterRedirectPolicyGroup,
       "tFilterScalarGroup": tFilterScalarGroup,
       "tFilterNotificationObjGroup": tFilterNotificationObjGroup,
       "tFilterNotificationsGroup": tFilterNotificationsGroup,
       "tIPv6FilterV4v0Group": tIPv6FilterV4v0Group,
       "tIPFilterV4v0Group": tIPFilterV4v0Group,
       "tMacFilterV4v0Group": tMacFilterV4v0Group,
       "tTodPoliciesV4v0Group": tTodPoliciesV4v0Group,
       "tmnxFilterObsoleteGroup": tmnxFilterObsoleteGroup,
       "tToDPoliciesV5v0NotifyGroup": tToDPoliciesV5v0NotifyGroup,
       "tIPFilterV5v0Group": tIPFilterV5v0Group,
       "tFilterLogV5v0Group": tFilterLogV5v0Group,
       "tTodPolicies77450V5v0Group": tTodPolicies77450V5v0Group,
       "tTodPolicies77x0V5v0Group": tTodPolicies77x0V5v0Group,
       "tFilterNotificationObjV5v0Group": tFilterNotificationObjV5v0Group,
       "tIPFilterV6v0Group": tIPFilterV6v0Group,
       "tMacFilterV6v0Group": tMacFilterV6v0Group,
       "tIPv6FilterV6v0Group": tIPv6FilterV6v0Group,
       "tIPFilterV8v0Group": tIPFilterV8v0Group,
       "tIPv6FilterV8v0Group": tIPv6FilterV8v0Group,
       "tFilterNotificationObjV8v0Group": tFilterNotificationObjV8v0Group,
       "tFilterNotificationsV8v0Group": tFilterNotificationsV8v0Group,
       "tMacFilterV8v0Group": tMacFilterV8v0Group,
       "tMacFilterVidFilteringV9v0Group": tMacFilterVidFilteringV9v0Group,
       "tIPFilterV9v0Group": tIPFilterV9v0Group,
       "tFilterNotificationsV9v0Group": tFilterNotificationsV9v0Group,
       "tFilterNotificationObjV9v0Group": tFilterNotificationObjV9v0Group,
       "tDhcpFilterV9v0Group": tDhcpFilterV9v0Group,
       "tIPv6FilterV10v0Group": tIPv6FilterV10v0Group,
       "tFilterNameV10v0Group": tFilterNameV10v0Group,
       "tDhcpFilterV10v0Group": tDhcpFilterV10v0Group,
       "tLiFilterV10v0Group": tLiFilterV10v0Group,
       "tFilterPrefixListV10v0Group": tFilterPrefixListV10v0Group,
       "tIPv6FilterV11v0Group": tIPv6FilterV11v0Group,
       "tFilterEmbeddedInsertV11v0Group": tFilterEmbeddedInsertV11v0Group,
       "tFilterPortListV11v0Group": tFilterPortListV11v0Group,
       "tFilterPrefixListV11v0Group": tFilterPrefixListV11v0Group,
       "tIPFilterV11v0Group": tIPFilterV11v0Group,
       "tFilterNotificationsV11v0Group": tFilterNotificationsV11v0Group,
       "tFilterNotificationObjV11v0Group": tFilterNotificationObjV11v0Group,
       "tIPFilterV12v0Group": tIPFilterV12v0Group,
       "tIPv6FilterV12v0Group": tIPv6FilterV12v0Group,
       "tLiFilterV12v0Group": tLiFilterV12v0Group,
       "tFilterEmbeddedInsertV12v0Group": tFilterEmbeddedInsertV12v0Group,
       "tFilterNotificationsV12v0Group": tFilterNotificationsV12v0Group,
       "tFilterNotificationObjV12v0Group": tFilterNotificationObjV12v0Group,
       "tFilterObjects": tFilterObjects,
       "tIPFilterTable": tIPFilterTable,
       "tIPFilterEntry": tIPFilterEntry,
       "tIPFilterId": tIPFilterId,
       "tIPFilterRowStatus": tIPFilterRowStatus,
       "tIPFilterScope": tIPFilterScope,
       "tIPFilterDescription": tIPFilterDescription,
       "tIPFilterDefaultAction": tIPFilterDefaultAction,
       "tIPFilterRadiusInsertPt": tIPFilterRadiusInsertPt,
       "tIPFilterRadiusInsertSize": tIPFilterRadiusInsertSize,
       "tIPFilterCreditCntrlInsertPt": tIPFilterCreditCntrlInsertPt,
       "tIPFilterCreditCntrlInsertSize": tIPFilterCreditCntrlInsertSize,
       "tIPFilterSubInsertHighWmark": tIPFilterSubInsertHighWmark,
       "tIPFilterSubInsertLowWmark": tIPFilterSubInsertLowWmark,
       "tIpFilterCreditCntrlNbrInsertd": tIpFilterCreditCntrlNbrInsertd,
       "tIpFilterRadiusNbrInsertd": tIpFilterRadiusNbrInsertd,
       "tIpFilterName": tIpFilterName,
       "tIPFilterHostSharedInsertPt": tIPFilterHostSharedInsertPt,
       "tIPFilterHostSharedInsertSize": tIPFilterHostSharedInsertSize,
       "tIpFilterHostSharedNbrInsertd": tIpFilterHostSharedNbrInsertd,
       "tIPFilterHostSharedHighWmark": tIPFilterHostSharedHighWmark,
       "tIPFilterHostSharedLowWmark": tIPFilterHostSharedLowWmark,
       "tIPFilterNbrHostSharedFltrs": tIPFilterNbrHostSharedFltrs,
       "tIPFilterParamsTable": tIPFilterParamsTable,
       "tIPFilterParamsEntry": tIPFilterParamsEntry,
       "tIPFilterParamsIndex": tIPFilterParamsIndex,
       "tIPFilterParamsRowStatus": tIPFilterParamsRowStatus,
       "tIPFilterParamsLogId": tIPFilterParamsLogId,
       "tIPFilterParamsDescription": tIPFilterParamsDescription,
       "tIPFilterParamsAction": tIPFilterParamsAction,
       "tIPFilterParamsForwardNH": tIPFilterParamsForwardNH,
       "tIPFilterParamsForwardNHIndirect": tIPFilterParamsForwardNHIndirect,
       "tIPFilterParamsRemarkDSCP": tIPFilterParamsRemarkDSCP,
       "tIPFilterParamsRemarkDSCPMask": tIPFilterParamsRemarkDSCPMask,
       "tIPFilterParamsRemarkDot1p": tIPFilterParamsRemarkDot1p,
       "tIPFilterParamsSourceIpAddr": tIPFilterParamsSourceIpAddr,
       "tIPFilterParamsSourceIpMask": tIPFilterParamsSourceIpMask,
       "tIPFilterParamsDestinationIpAddr": tIPFilterParamsDestinationIpAddr,
       "tIPFilterParamsDestinationIpMask": tIPFilterParamsDestinationIpMask,
       "tIPFilterParamsProtocol": tIPFilterParamsProtocol,
       "tIPFilterParamsSourcePortValue1": tIPFilterParamsSourcePortValue1,
       "tIPFilterParamsSourcePortValue2": tIPFilterParamsSourcePortValue2,
       "tIPFilterParamsSourcePortOperator": tIPFilterParamsSourcePortOperator,
       "tIPFilterParamsDestPortValue1": tIPFilterParamsDestPortValue1,
       "tIPFilterParamsDestPortValue2": tIPFilterParamsDestPortValue2,
       "tIPFilterParamsDestPortOperator": tIPFilterParamsDestPortOperator,
       "tIPFilterParamsDSCP": tIPFilterParamsDSCP,
       "tIPFilterParamsFragment": tIPFilterParamsFragment,
       "tIPFilterParamsOptionPresent": tIPFilterParamsOptionPresent,
       "tIPFilterParamsIpOptionValue": tIPFilterParamsIpOptionValue,
       "tIPFilterParamsIpOptionMask": tIPFilterParamsIpOptionMask,
       "tIPFilterParamsMultipleOption": tIPFilterParamsMultipleOption,
       "tIPFilterParamsTcpSyn": tIPFilterParamsTcpSyn,
       "tIPFilterParamsTcpAck": tIPFilterParamsTcpAck,
       "tIPFilterParamsIcmpCode": tIPFilterParamsIcmpCode,
       "tIPFilterParamsIcmpType": tIPFilterParamsIcmpType,
       "tIPFilterParamsCflowdSample": tIPFilterParamsCflowdSample,
       "tIPFilterParamsCflowdIfSample": tIPFilterParamsCflowdIfSample,
       "tIPFilterParamsForwardNHInterface": tIPFilterParamsForwardNHInterface,
       "tIPFilterParamsIngressHitCount": tIPFilterParamsIngressHitCount,
       "tIPFilterParamsEgressHitCount": tIPFilterParamsEgressHitCount,
       "tIPFilterParamsLogInstantiated": tIPFilterParamsLogInstantiated,
       "tIPFilterParamsForwardRedPlcy": tIPFilterParamsForwardRedPlcy,
       "tIPFilterParamsActiveDest": tIPFilterParamsActiveDest,
       "tIPFilterParamsFwdSvcId": tIPFilterParamsFwdSvcId,
       "tIPFilterParamsFwdSapPortId": tIPFilterParamsFwdSapPortId,
       "tIPFilterParamsFwdSapEncapVal": tIPFilterParamsFwdSapEncapVal,
       "tIPFilterParamsFwdSdpBind": tIPFilterParamsFwdSdpBind,
       "tIPFilterParamsTimeRangeName": tIPFilterParamsTimeRangeName,
       "tIPFilterParamsTimeRangeState": tIPFilterParamsTimeRangeState,
       "tIPFilterParamsRedirectURL": tIPFilterParamsRedirectURL,
       "tIPFilterParamsSrcIpFullMask": tIPFilterParamsSrcIpFullMask,
       "tIPFilterParamsDestIpFullMask": tIPFilterParamsDestIpFullMask,
       "tIPFilterParamsIngrHitByteCount": tIPFilterParamsIngrHitByteCount,
       "tIPFilterParamsEgrHitByteCount": tIPFilterParamsEgrHitByteCount,
       "tIPFilterParamsFwdRtrId": tIPFilterParamsFwdRtrId,
       "tIPFilterParamsSrcRouteOption": tIPFilterParamsSrcRouteOption,
       "tIPFilterParamsSrcIpPrefixList": tIPFilterParamsSrcIpPrefixList,
       "tIPFilterParamsDstIpPrefixList": tIPFilterParamsDstIpPrefixList,
       "tIPFilterParamsPortSelector": tIPFilterParamsPortSelector,
       "tIPFilterParamsSrcPortList": tIPFilterParamsSrcPortList,
       "tIPFilterParamsDstPortList": tIPFilterParamsDstPortList,
       "tIPFilterParamsRdirAllwRadOvrd": tIPFilterParamsRdirAllwRadOvrd,
       "tIPFilterParamsNatPolicyName": tIPFilterParamsNatPolicyName,
       "tIPFilterParamsFwdLsp": tIPFilterParamsFwdLsp,
       "tIPFilterParamsFwdLspRtrId": tIPFilterParamsFwdLspRtrId,
       "tMacFilterTable": tMacFilterTable,
       "tMacFilterEntry": tMacFilterEntry,
       "tMacFilterId": tMacFilterId,
       "tMacFilterRowStatus": tMacFilterRowStatus,
       "tMacFilterScope": tMacFilterScope,
       "tMacFilterDescription": tMacFilterDescription,
       "tMacFilterDefaultAction": tMacFilterDefaultAction,
       "tMacFilterType": tMacFilterType,
       "tMacFilterName": tMacFilterName,
       "tMacFilterParamsTable": tMacFilterParamsTable,
       "tMacFilterParamsEntry": tMacFilterParamsEntry,
       "tMacFilterParamsIndex": tMacFilterParamsIndex,
       "tMacFilterParamsRowStatus": tMacFilterParamsRowStatus,
       "tMacFilterParamsLogId": tMacFilterParamsLogId,
       "tMacFilterParamsDescription": tMacFilterParamsDescription,
       "tMacFilterParamsAction": tMacFilterParamsAction,
       "tMacFilterParamsFrameType": tMacFilterParamsFrameType,
       "tMacFilterParamsSrcMAC": tMacFilterParamsSrcMAC,
       "tMacFilterParamsSrcMACMask": tMacFilterParamsSrcMACMask,
       "tMacFilterParamsDstMAC": tMacFilterParamsDstMAC,
       "tMacFilterParamsDstMACMask": tMacFilterParamsDstMACMask,
       "tMacFilterParamsDot1pValue": tMacFilterParamsDot1pValue,
       "tMacFilterParamsDot1pMask": tMacFilterParamsDot1pMask,
       "tMacFilterParamsEtherType": tMacFilterParamsEtherType,
       "tMacFilterParamsDsap": tMacFilterParamsDsap,
       "tMacFilterParamsDsapMask": tMacFilterParamsDsapMask,
       "tMacFilterParamsSsap": tMacFilterParamsSsap,
       "tMacFilterParamsSsapMask": tMacFilterParamsSsapMask,
       "tMacFilterParamsSnapPid": tMacFilterParamsSnapPid,
       "tMacFilterParamsSnapOui": tMacFilterParamsSnapOui,
       "tMacFilterParamsIngressHitCount": tMacFilterParamsIngressHitCount,
       "tMacFilterParamsEgressHitCount": tMacFilterParamsEgressHitCount,
       "tMacFilterParamsLogInstantiated": tMacFilterParamsLogInstantiated,
       "tMacFilterParamsFwdSvcId": tMacFilterParamsFwdSvcId,
       "tMacFilterParamsFwdSapPortId": tMacFilterParamsFwdSapPortId,
       "tMacFilterParamsFwdSapEncapVal": tMacFilterParamsFwdSapEncapVal,
       "tMacFilterParamsFwdSdpBind": tMacFilterParamsFwdSdpBind,
       "tMacFilterParamsTimeRangeName": tMacFilterParamsTimeRangeName,
       "tMacFilterParamsTimeRangeState": tMacFilterParamsTimeRangeState,
       "tMacFilterParamsRedirectURL": tMacFilterParamsRedirectURL,
       "tMacFilterParamsIngrHitByteCount": tMacFilterParamsIngrHitByteCount,
       "tMacFilterParamsEgrHitByteCount": tMacFilterParamsEgrHitByteCount,
       "tMacFilterParamsLowISID": tMacFilterParamsLowISID,
       "tMacFilterParamsHighISID": tMacFilterParamsHighISID,
       "tMacFilterParamsInnerTagValue": tMacFilterParamsInnerTagValue,
       "tMacFilterParamsInnerTagMask": tMacFilterParamsInnerTagMask,
       "tMacFilterParamsOuterTagValue": tMacFilterParamsOuterTagValue,
       "tMacFilterParamsOuterTagMask": tMacFilterParamsOuterTagMask,
       "tFilterLogTable": tFilterLogTable,
       "tFilterLogEntry": tFilterLogEntry,
       "tFilterLogId": tFilterLogId,
       "tFilterLogRowStatus": tFilterLogRowStatus,
       "tFilterLogDestination": tFilterLogDestination,
       "tFilterLogDescription": tFilterLogDescription,
       "tFilterLogMaxNumEntries": tFilterLogMaxNumEntries,
       "tFilterLogSysLogId": tFilterLogSysLogId,
       "tFilterLogFileId": tFilterLogFileId,
       "tFilterLogStopOnFull": tFilterLogStopOnFull,
       "tFilterLogEnabled": tFilterLogEnabled,
       "tFilterLogSummaryEnabled": tFilterLogSummaryEnabled,
       "tFilterLogSummaryCrit1": tFilterLogSummaryCrit1,
       "tFilterLogScalars": tFilterLogScalars,
       "tFilterLogMaxInstances": tFilterLogMaxInstances,
       "tFilterLogInstances": tFilterLogInstances,
       "tFilterLogBindings": tFilterLogBindings,
       "tFilterNotificationObjects": tFilterNotificationObjects,
       "tFilterPBRDropReason": tFilterPBRDropReason,
       "tFilterParmRow": tFilterParmRow,
       "tFilterAlarmDescription": tFilterAlarmDescription,
       "tFilterId": tFilterId,
       "tFilterType": tFilterType,
       "tFilterSubInsSpaceOwner": tFilterSubInsSpaceOwner,
       "tFilterThresholdReached": tFilterThresholdReached,
       "tFltrFlowSpecProblem": tFltrFlowSpecProblem,
       "tFltrFlowSpecProblemDescription": tFltrFlowSpecProblemDescription,
       "tFltrFLowSpecNLRI": tFltrFLowSpecNLRI,
       "tFltrFlowSpecVrtrId": tFltrFlowSpecVrtrId,
       "tFltrPrefixListType": tFltrPrefixListType,
       "tFltrPrefixListName": tFltrPrefixListName,
       "tFltrApplyPathSource": tFltrApplyPathSource,
       "tFltrApplyPathIndex": tFltrApplyPathIndex,
       "tFltrNotifDescription": tFltrNotifDescription,
       "tFltrMdaId": tFltrMdaId,
       "tFilterTimeStampObjects": tFilterTimeStampObjects,
       "tFilterDomainLastChanged": tFilterDomainLastChanged,
       "tFilterRedirectPolicyTable": tFilterRedirectPolicyTable,
       "tFilterRedirectPolicyEntry": tFilterRedirectPolicyEntry,
       "tFilterRedirectPolicy": tFilterRedirectPolicy,
       "tFilterRPRowStatus": tFilterRPRowStatus,
       "tFilterRPDescription": tFilterRPDescription,
       "tFilterRPAdminState": tFilterRPAdminState,
       "tFilterRPActiveDest": tFilterRPActiveDest,
       "tFilterRedirectDestTable": tFilterRedirectDestTable,
       "tFilterRedirectDestEntry": tFilterRedirectDestEntry,
       "tFilterRedirectDest": tFilterRedirectDest,
       "tFilterRDRowStatus": tFilterRDRowStatus,
       "tFilterRDDescription": tFilterRDDescription,
       "tFilterRDAdminPriority": tFilterRDAdminPriority,
       "tFilterRDOperPriority": tFilterRDOperPriority,
       "tFilterRDAdminState": tFilterRDAdminState,
       "tFilterRDOperState": tFilterRDOperState,
       "tFilterRedirectSNMPTestTable": tFilterRedirectSNMPTestTable,
       "tFilterRedirectSNMPTestEntry": tFilterRedirectSNMPTestEntry,
       "tFilterRedirectSNMPTest": tFilterRedirectSNMPTest,
       "tFilterRSTRowStatus": tFilterRSTRowStatus,
       "tFilterRSTOID": tFilterRSTOID,
       "tFilterRSTCommunity": tFilterRSTCommunity,
       "tFilterRSTSNMPVersion": tFilterRSTSNMPVersion,
       "tFilterRSTInterval": tFilterRSTInterval,
       "tFilterRSTTimeout": tFilterRSTTimeout,
       "tFilterRSTDropCount": tFilterRSTDropCount,
       "tFilterRSTHoldDown": tFilterRSTHoldDown,
       "tFilterRSTHoldDownRemain": tFilterRSTHoldDownRemain,
       "tFilterRSTLastActionTime": tFilterRSTLastActionTime,
       "tFilterRSTLastOID": tFilterRSTLastOID,
       "tFilterRSTLastType": tFilterRSTLastType,
       "tFilterRSTLastCounter32Val": tFilterRSTLastCounter32Val,
       "tFilterRSTLastUnsigned32Val": tFilterRSTLastUnsigned32Val,
       "tFilterRSTLastTimeTicksVal": tFilterRSTLastTimeTicksVal,
       "tFilterRSTLastInt32Val": tFilterRSTLastInt32Val,
       "tFilterRSTLastOctetStringVal": tFilterRSTLastOctetStringVal,
       "tFilterRSTLastIpAddressVal": tFilterRSTLastIpAddressVal,
       "tFilterRSTLastOidVal": tFilterRSTLastOidVal,
       "tFilterRSTLastCounter64Val": tFilterRSTLastCounter64Val,
       "tFilterRSTLastOpaqueVal": tFilterRSTLastOpaqueVal,
       "tFilterRSTLastAction": tFilterRSTLastAction,
       "tFilterRSTLastPrioChange": tFilterRSTLastPrioChange,
       "tFilterRSTNextRespIndex": tFilterRSTNextRespIndex,
       "tFilterRedirectSNMPRespTable": tFilterRedirectSNMPRespTable,
       "tFilterRedirectSNMPRespEntry": tFilterRedirectSNMPRespEntry,
       "tFilterRSTRespId": tFilterRSTRespId,
       "tFilterRSTRespRowStatus": tFilterRSTRespRowStatus,
       "tFilterRSTRespAction": tFilterRSTRespAction,
       "tFilterRSTRespPrioChange": tFilterRSTRespPrioChange,
       "tFilterRSTRespOID": tFilterRSTRespOID,
       "tFilterRSTRespType": tFilterRSTRespType,
       "tFilterRSTCounter32Val": tFilterRSTCounter32Val,
       "tFilterRSTUnsigned32Val": tFilterRSTUnsigned32Val,
       "tFilterRSTTimeTicksVal": tFilterRSTTimeTicksVal,
       "tFilterRSTInt32Val": tFilterRSTInt32Val,
       "tFilterRSTOctetStringVal": tFilterRSTOctetStringVal,
       "tFilterRSTIpAddressVal": tFilterRSTIpAddressVal,
       "tFilterRSTOidVal": tFilterRSTOidVal,
       "tFilterRSTCounter64Val": tFilterRSTCounter64Val,
       "tFilterRSTOpaqueVal": tFilterRSTOpaqueVal,
       "tFilterRedirectURLTestTable": tFilterRedirectURLTestTable,
       "tFilterRedirectURLTestEntry": tFilterRedirectURLTestEntry,
       "tFilterRedirectURLTest": tFilterRedirectURLTest,
       "tFilterRUTRowStatus": tFilterRUTRowStatus,
       "tFilterRUTURL": tFilterRUTURL,
       "tFilterRUTHTTPVersion": tFilterRUTHTTPVersion,
       "tFilterRUTInterval": tFilterRUTInterval,
       "tFilterRUTTimeout": tFilterRUTTimeout,
       "tFilterRUTDropCount": tFilterRUTDropCount,
       "tFilterRUTHoldDown": tFilterRUTHoldDown,
       "tFilterRUTHoldDownRemain": tFilterRUTHoldDownRemain,
       "tFilterRUTLastActionTime": tFilterRUTLastActionTime,
       "tFilterRUTLastRetCode": tFilterRUTLastRetCode,
       "tFilterRUTLastAction": tFilterRUTLastAction,
       "tFilterRUTLastPrioChange": tFilterRUTLastPrioChange,
       "tFilterRedirectURLRespTable": tFilterRedirectURLRespTable,
       "tFilterRedirectURLRespEntry": tFilterRedirectURLRespEntry,
       "tFilterRedirectURLLowRespCode": tFilterRedirectURLLowRespCode,
       "tFilterRedirectURLHighRespCode": tFilterRedirectURLHighRespCode,
       "tFilterRUTRespRowStatus": tFilterRUTRespRowStatus,
       "tFilterRUTRespAction": tFilterRUTRespAction,
       "tFilterRUTRespPrioChange": tFilterRUTRespPrioChange,
       "tFilterRedirectPingTestTable": tFilterRedirectPingTestTable,
       "tFilterRedirectPingTestEntry": tFilterRedirectPingTestEntry,
       "tFilterRPTRowStatus": tFilterRPTRowStatus,
       "tFilterRPTInterval": tFilterRPTInterval,
       "tFilterRPTTimeout": tFilterRPTTimeout,
       "tFilterRPTDropCount": tFilterRPTDropCount,
       "tFilterRPTHoldDown": tFilterRPTHoldDown,
       "tFilterRPTHoldDownRemain": tFilterRPTHoldDownRemain,
       "tFilterRPTLastActionTime": tFilterRPTLastActionTime,
       "tFilterRPTLastAction": tFilterRPTLastAction,
       "tAutoIPFilterEntryTable": tAutoIPFilterEntryTable,
       "tAutoIPFilterEntry": tAutoIPFilterEntry,
       "tAutoIPFilterId": tAutoIPFilterId,
       "tAutoIPFilterEntrySourceIpAddr": tAutoIPFilterEntrySourceIpAddr,
       "tAutoIPFilterEntrySourceIpMask": tAutoIPFilterEntrySourceIpMask,
       "tIPv6FilterTable": tIPv6FilterTable,
       "tIPv6FilterEntry": tIPv6FilterEntry,
       "tIPv6FilterId": tIPv6FilterId,
       "tIPv6FilterRowStatus": tIPv6FilterRowStatus,
       "tIPv6FilterScope": tIPv6FilterScope,
       "tIPv6FilterDescription": tIPv6FilterDescription,
       "tIPv6FilterDefaultAction": tIPv6FilterDefaultAction,
       "tIPv6FilterRadiusInsertPt": tIPv6FilterRadiusInsertPt,
       "tIPv6FilterRadiusInsertSize": tIPv6FilterRadiusInsertSize,
       "tIPv6FilterCreditCntrlInsertPt": tIPv6FilterCreditCntrlInsertPt,
       "tIPv6FilterCreditCntrlInsertSize": tIPv6FilterCreditCntrlInsertSize,
       "tIPv6FilterSubInsertHighWmark": tIPv6FilterSubInsertHighWmark,
       "tIPv6FilterSubInsertLowWmark": tIPv6FilterSubInsertLowWmark,
       "tIpv6FilterCreditCntrlNbrInsertd": tIpv6FilterCreditCntrlNbrInsertd,
       "tIpv6FilterRadiusNbrInsertd": tIpv6FilterRadiusNbrInsertd,
       "tIpv6FilterName": tIpv6FilterName,
       "tIPv6FilterHostSharedInsertPt": tIPv6FilterHostSharedInsertPt,
       "tIPv6FilterHostSharedInsertSize": tIPv6FilterHostSharedInsertSize,
       "tIpv6FilterHostSharedNbrInsertd": tIpv6FilterHostSharedNbrInsertd,
       "tIPv6FilterHostSharedHighWmark": tIPv6FilterHostSharedHighWmark,
       "tIPv6FilterHostSharedLowWmark": tIPv6FilterHostSharedLowWmark,
       "tIPv6FilterNbrHostSharedFltrs": tIPv6FilterNbrHostSharedFltrs,
       "tIPv6FilterParamsTable": tIPv6FilterParamsTable,
       "tIPv6FilterParamsEntry": tIPv6FilterParamsEntry,
       "tIPv6FilterParamsIndex": tIPv6FilterParamsIndex,
       "tIPv6FilterParamsRowStatus": tIPv6FilterParamsRowStatus,
       "tIPv6FilterParamsLogId": tIPv6FilterParamsLogId,
       "tIPv6FilterParamsDescription": tIPv6FilterParamsDescription,
       "tIPv6FilterParamsAction": tIPv6FilterParamsAction,
       "tIPv6FilterParamsForwardNH": tIPv6FilterParamsForwardNH,
       "tIPv6FilterParamsForwardNHIndirect": tIPv6FilterParamsForwardNHIndirect,
       "tIPv6FilterParamsRemarkDSCP": tIPv6FilterParamsRemarkDSCP,
       "tIPv6FilterParamsRemarkDSCPMask": tIPv6FilterParamsRemarkDSCPMask,
       "tIPv6FilterParamsRemarkDot1p": tIPv6FilterParamsRemarkDot1p,
       "tIPv6FilterParamsSourceIpAddr": tIPv6FilterParamsSourceIpAddr,
       "tIPv6FilterParamsSourceIpMask": tIPv6FilterParamsSourceIpMask,
       "tIPv6FilterParamsDestinationIpAddr": tIPv6FilterParamsDestinationIpAddr,
       "tIPv6FilterParamsDestinationIpMask": tIPv6FilterParamsDestinationIpMask,
       "tIPv6FilterParamsNextHeader": tIPv6FilterParamsNextHeader,
       "tIPv6FilterParamsSourcePortValue1": tIPv6FilterParamsSourcePortValue1,
       "tIPv6FilterParamsSourcePortValue2": tIPv6FilterParamsSourcePortValue2,
       "tIPv6FilterParamsSourcePortOperator": tIPv6FilterParamsSourcePortOperator,
       "tIPv6FilterParamsDestPortValue1": tIPv6FilterParamsDestPortValue1,
       "tIPv6FilterParamsDestPortValue2": tIPv6FilterParamsDestPortValue2,
       "tIPv6FilterParamsDestPortOperator": tIPv6FilterParamsDestPortOperator,
       "tIPv6FilterParamsDSCP": tIPv6FilterParamsDSCP,
       "tIPv6FilterParamsTcpSyn": tIPv6FilterParamsTcpSyn,
       "tIPv6FilterParamsTcpAck": tIPv6FilterParamsTcpAck,
       "tIPv6FilterParamsIcmpCode": tIPv6FilterParamsIcmpCode,
       "tIPv6FilterParamsIcmpType": tIPv6FilterParamsIcmpType,
       "tIPv6FilterParamsCflowdSample": tIPv6FilterParamsCflowdSample,
       "tIPv6FilterParamsCflowdIfSample": tIPv6FilterParamsCflowdIfSample,
       "tIPv6FilterParamsForwardNHInterface": tIPv6FilterParamsForwardNHInterface,
       "tIPv6FilterParamsIngressHitCount": tIPv6FilterParamsIngressHitCount,
       "tIPv6FilterParamsEgressHitCount": tIPv6FilterParamsEgressHitCount,
       "tIPv6FilterParamsLogInstantiated": tIPv6FilterParamsLogInstantiated,
       "tIPv6FilterParamsForwardRedPlcy": tIPv6FilterParamsForwardRedPlcy,
       "tIPv6FilterParamsActiveDest": tIPv6FilterParamsActiveDest,
       "tIPv6FilterParamsTimeRangeName": tIPv6FilterParamsTimeRangeName,
       "tIPv6FilterParamsTimeRangeState": tIPv6FilterParamsTimeRangeState,
       "tIPv6FilterParamsIngrHitByteCount": tIPv6FilterParamsIngrHitByteCount,
       "tIPv6FilterParamsEgrHitByteCount": tIPv6FilterParamsEgrHitByteCount,
       "tIPv6FilterParamsFwdSvcId": tIPv6FilterParamsFwdSvcId,
       "tIPv6FilterParamsFwdSapPortId": tIPv6FilterParamsFwdSapPortId,
       "tIPv6FilterParamsFwdSapEncapVal": tIPv6FilterParamsFwdSapEncapVal,
       "tIPv6FilterParamsFwdSdpBind": tIPv6FilterParamsFwdSdpBind,
       "tIPv6FilterParamsRedirectURL": tIPv6FilterParamsRedirectURL,
       "tIPv6FilterParamsSrcIpPrefixList": tIPv6FilterParamsSrcIpPrefixList,
       "tIPv6FilterParamsDstIpPrefixList": tIPv6FilterParamsDstIpPrefixList,
       "tIPv6FilterParamsFragment": tIPv6FilterParamsFragment,
       "tIPv6FilterParamsHopByHopOpt": tIPv6FilterParamsHopByHopOpt,
       "tIPv6FilterParamsRoutingType0": tIPv6FilterParamsRoutingType0,
       "tIPv6FilterParamsPortSelector": tIPv6FilterParamsPortSelector,
       "tIPv6FilterParamsSrcPortList": tIPv6FilterParamsSrcPortList,
       "tIPv6FilterParamsDstPortList": tIPv6FilterParamsDstPortList,
       "tIPv6FilterParamsRdirAllwRadOvrd": tIPv6FilterParamsRdirAllwRadOvrd,
       "tIPv6FilterParamsFwdRtrId": tIPv6FilterParamsFwdRtrId,
       "tIPv6FilterParamsSrcIpFullMask": tIPv6FilterParamsSrcIpFullMask,
       "tIPv6FilterParamsDstIpFullMask": tIPv6FilterParamsDstIpFullMask,
       "tIPv6FilterParamsNatPolicyName": tIPv6FilterParamsNatPolicyName,
       "tIPv6FilterParamsFlowLabel": tIPv6FilterParamsFlowLabel,
       "tIPv6FilterParamsFlowLabelMask": tIPv6FilterParamsFlowLabelMask,
       "tIPv6FilterParamsFwdLsp": tIPv6FilterParamsFwdLsp,
       "tIPv6FilterParamsFwdLspRtrId": tIPv6FilterParamsFwdLspRtrId,
       "tFilterGroupInsertedEntries": tFilterGroupInsertedEntries,
       "tFltrGrpInsrtdEntriesFilterType": tFltrGrpInsrtdEntriesFilterType,
       "tFltrGrpInsrtdEntriesFilterId": tFltrGrpInsrtdEntriesFilterId,
       "tFltrGrpInsrtdEntriesApplication": tFltrGrpInsrtdEntriesApplication,
       "tFltrGrpInsrtdEntriesLocation": tFltrGrpInsrtdEntriesLocation,
       "tFltrGrpInsrtdEntriesResult": tFltrGrpInsrtdEntriesResult,
       "tFltrGrpInsrtdEntriesFeedback": tFltrGrpInsrtdEntriesFeedback,
       "tFltrGrpInsrtdEntriesExecute": tFltrGrpInsrtdEntriesExecute,
       "tDhcpFilterTableLastChanged": tDhcpFilterTableLastChanged,
       "tDhcpFilterTable": tDhcpFilterTable,
       "tDhcpFilterEntry": tDhcpFilterEntry,
       "tDhcpFilterId": tDhcpFilterId,
       "tDhcpFilterRowStatus": tDhcpFilterRowStatus,
       "tDhcpFilterLastChanged": tDhcpFilterLastChanged,
       "tDhcpFilterDescription": tDhcpFilterDescription,
       "tDhcpFilterParamsTblLastChanged": tDhcpFilterParamsTblLastChanged,
       "tDhcpFilterParamsTable": tDhcpFilterParamsTable,
       "tDhcpFilterParamsEntry": tDhcpFilterParamsEntry,
       "tDhcpFilterParamsId": tDhcpFilterParamsId,
       "tDhcpFilterParamsRowStatus": tDhcpFilterParamsRowStatus,
       "tDhcpFilterParamsLastChanged": tDhcpFilterParamsLastChanged,
       "tDhcpFilterParamsOptionNumber": tDhcpFilterParamsOptionNumber,
       "tDhcpFilterParamsOptionMatch": tDhcpFilterParamsOptionMatch,
       "tDhcpFilterParamsAction": tDhcpFilterParamsAction,
       "tDhcpFilterParamsOptionValue": tDhcpFilterParamsOptionValue,
       "tMacFilterNameTableLastChgd": tMacFilterNameTableLastChgd,
       "tMacFilterNameTable": tMacFilterNameTable,
       "tMacFilterNameEntry": tMacFilterNameEntry,
       "tMacFilterNameId": tMacFilterNameId,
       "tMacFilterNameRowStatus": tMacFilterNameRowStatus,
       "tMacFilterNameLastChanged": tMacFilterNameLastChanged,
       "tIpFilterNameTableLastChgd": tIpFilterNameTableLastChgd,
       "tIpFilterNameTable": tIpFilterNameTable,
       "tIpFilterNameEntry": tIpFilterNameEntry,
       "tIpFilterNameId": tIpFilterNameId,
       "tIpFilterNameRowStatus": tIpFilterNameRowStatus,
       "tIpFilterNameLastChanged": tIpFilterNameLastChanged,
       "tIpv6FilterNameTableLastChgd": tIpv6FilterNameTableLastChgd,
       "tIpv6FilterNameTable": tIpv6FilterNameTable,
       "tIpv6FilterNameEntry": tIpv6FilterNameEntry,
       "tIpv6FilterNameId": tIpv6FilterNameId,
       "tIpv6FilterNameRowStatus": tIpv6FilterNameRowStatus,
       "tIpv6FilterNameLastChanged": tIpv6FilterNameLastChanged,
       "tFilterLiObjects": tFilterLiObjects,
       "tLiReservedBlockTableLastChanged": tLiReservedBlockTableLastChanged,
       "tLiReservedBlockTable": tLiReservedBlockTable,
       "tLiReservedBlockEntry": tLiReservedBlockEntry,
       "tLiReservedBlockName": tLiReservedBlockName,
       "tLiReservedBlockRowStatus": tLiReservedBlockRowStatus,
       "tLiReservedBlockLastChanged": tLiReservedBlockLastChanged,
       "tLiReservedBlockDescription": tLiReservedBlockDescription,
       "tLiReservedBlockStart": tLiReservedBlockStart,
       "tLiReservedBlockSize": tLiReservedBlockSize,
       "tLiReservedBlockFltrTableLastChg": tLiReservedBlockFltrTableLastChg,
       "tLiReservedBlockFltrTable": tLiReservedBlockFltrTable,
       "tLiReservedBlockFltrEntry": tLiReservedBlockFltrEntry,
       "tLiReservedBlockFltrType": tLiReservedBlockFltrType,
       "tLiReservedBlockFltrIdStart": tLiReservedBlockFltrIdStart,
       "tLiReservedBlockFltrIdEnd": tLiReservedBlockFltrIdEnd,
       "tLiReservedBlockFltrRowStatus": tLiReservedBlockFltrRowStatus,
       "tLiReservedBlockFltrLastChanged": tLiReservedBlockFltrLastChanged,
       "tLiFilterTableLastChanged": tLiFilterTableLastChanged,
       "tLiFilterTable": tLiFilterTable,
       "tLiFilterEntry": tLiFilterEntry,
       "tLiFilterType": tLiFilterType,
       "tLiFilterName": tLiFilterName,
       "tLiFilterRowStatus": tLiFilterRowStatus,
       "tLiFilterLastChanged": tLiFilterLastChanged,
       "tLiFilterDescription": tLiFilterDescription,
       "tLiFilterAssociationTableLastChg": tLiFilterAssociationTableLastChg,
       "tLiFilterAssociationTable": tLiFilterAssociationTable,
       "tLiFilterAssociationEntry": tLiFilterAssociationEntry,
       "tLiFilterAssociationFltrId": tLiFilterAssociationFltrId,
       "tLiFilterAssociationRowStatus": tLiFilterAssociationRowStatus,
       "tLiFilterAssociationLastChg": tLiFilterAssociationLastChg,
       "tLiMacFilterParamsTableLastChg": tLiMacFilterParamsTableLastChg,
       "tLiMacFilterParamsTable": tLiMacFilterParamsTable,
       "tLiMacFilterParamsEntry": tLiMacFilterParamsEntry,
       "tLiMacFilterParamsId": tLiMacFilterParamsId,
       "tLiMacFilterParamsRowStatus": tLiMacFilterParamsRowStatus,
       "tLiMacFilterParamsLastChanged": tLiMacFilterParamsLastChanged,
       "tLiMacFilterParamsDescription": tLiMacFilterParamsDescription,
       "tLiMacFilterParamsFrameType": tLiMacFilterParamsFrameType,
       "tLiMacFilterParamsSrcMAC": tLiMacFilterParamsSrcMAC,
       "tLiMacFilterParamsSrcMACMask": tLiMacFilterParamsSrcMACMask,
       "tLiMacFilterParamsDstMAC": tLiMacFilterParamsDstMAC,
       "tLiMacFilterParamsDstMACMask": tLiMacFilterParamsDstMACMask,
       "tLiMacFilterParamsIngrHitCount": tLiMacFilterParamsIngrHitCount,
       "tLiMacFilterParamsEgrHitCount": tLiMacFilterParamsEgrHitCount,
       "tLiMacFilterParamsIngrHitBytes": tLiMacFilterParamsIngrHitBytes,
       "tLiMacFilterParamsEgrHitBytes": tLiMacFilterParamsEgrHitBytes,
       "tLiIpFilterParamsTableLastChg": tLiIpFilterParamsTableLastChg,
       "tLiIpFilterParamsTable": tLiIpFilterParamsTable,
       "tLiIpFilterParamsEntry": tLiIpFilterParamsEntry,
       "tLiIpFilterParamsId": tLiIpFilterParamsId,
       "tLiIpFilterParamsLastChanged": tLiIpFilterParamsLastChanged,
       "tLiIpFilterParamsRowStatus": tLiIpFilterParamsRowStatus,
       "tLiIpFilterParamsDescription": tLiIpFilterParamsDescription,
       "tLiIpFilterParamsSrcIpAddrType": tLiIpFilterParamsSrcIpAddrType,
       "tLiIpFilterParamsSrcIpAddr": tLiIpFilterParamsSrcIpAddr,
       "tLiIpFilterParamsSrcIpFullMask": tLiIpFilterParamsSrcIpFullMask,
       "tLiIpFilterParamsDstIpAddrType": tLiIpFilterParamsDstIpAddrType,
       "tLiIpFilterParamsDstIpAddr": tLiIpFilterParamsDstIpAddr,
       "tLiIpFilterParamsDstIpFullMask": tLiIpFilterParamsDstIpFullMask,
       "tLiIpFilterParamsProtocolNextHdr": tLiIpFilterParamsProtocolNextHdr,
       "tLiIpFilterParamsSrcPortValue1": tLiIpFilterParamsSrcPortValue1,
       "tLiIpFilterParamsSrcPortValue2": tLiIpFilterParamsSrcPortValue2,
       "tLiIpFilterParamsSrcPortOper": tLiIpFilterParamsSrcPortOper,
       "tLiIpFilterParamsDstPortValue1": tLiIpFilterParamsDstPortValue1,
       "tLiIpFilterParamsDstPortValue2": tLiIpFilterParamsDstPortValue2,
       "tLiIpFilterParamsDstPortOper": tLiIpFilterParamsDstPortOper,
       "tLiIpFilterParamsInfoTable": tLiIpFilterParamsInfoTable,
       "tLiIpFilterParamsInfoEntry": tLiIpFilterParamsInfoEntry,
       "tLiIpFltrParamsInfIngrHitCount": tLiIpFltrParamsInfIngrHitCount,
       "tLiIpFltrParamsInfEgrHitCount": tLiIpFltrParamsInfEgrHitCount,
       "tLiIpFltrParamsInfIngrHitBytes": tLiIpFltrParamsInfIngrHitBytes,
       "tLiIpFltrParamsInfEgrHitBytes": tLiIpFltrParamsInfEgrHitBytes,
       "tFilterPrefixListTableLstChng": tFilterPrefixListTableLstChng,
       "tFilterPrefixListTable": tFilterPrefixListTable,
       "tFilterPrefixListEntry": tFilterPrefixListEntry,
       "tFilterPrefixListType": tFilterPrefixListType,
       "tFilterPrefixListName": tFilterPrefixListName,
       "tFilterPrefixListRowStatus": tFilterPrefixListRowStatus,
       "tFilterPrefixListLastChanged": tFilterPrefixListLastChanged,
       "tFilterPrefixListDescription": tFilterPrefixListDescription,
       "tFilterPrefixListEntryTblLstChg": tFilterPrefixListEntryTblLstChg,
       "tFilterPrefixListEntryTable": tFilterPrefixListEntryTable,
       "tFilterPrefixListEntryEntry": tFilterPrefixListEntryEntry,
       "tFilterPrefixListEntryPrefixType": tFilterPrefixListEntryPrefixType,
       "tFilterPrefixListEntryPrefix": tFilterPrefixListEntryPrefix,
       "tFilterPrefixListEntryPrefixLen": tFilterPrefixListEntryPrefixLen,
       "tFilterPrefixListEntryRowStatus": tFilterPrefixListEntryRowStatus,
       "tFilterEmbeddedRefTableLstChg": tFilterEmbeddedRefTableLstChg,
       "tFilterEmbeddedRefTable": tFilterEmbeddedRefTable,
       "tFilterEmbeddedRefTableEntry": tFilterEmbeddedRefTableEntry,
       "tFilterEmbeddedRefFilterType": tFilterEmbeddedRefFilterType,
       "tFilterEmbeddedRefInsertFltrId": tFilterEmbeddedRefInsertFltrId,
       "tFilterEmbeddedRefEmbeddedFltrId": tFilterEmbeddedRefEmbeddedFltrId,
       "tFilterEmbeddedRefOffset": tFilterEmbeddedRefOffset,
       "tFilterEmbeddedRefRowStatus": tFilterEmbeddedRefRowStatus,
       "tFilterEmbeddedRefAdminState": tFilterEmbeddedRefAdminState,
       "tFilterEmbeddedRefOperState": tFilterEmbeddedRefOperState,
       "tFilterPortListTableLstChng": tFilterPortListTableLstChng,
       "tFilterPortListTable": tFilterPortListTable,
       "tFilterPortListEntry": tFilterPortListEntry,
       "tFilterPortListName": tFilterPortListName,
       "tFilterPortListRowStatus": tFilterPortListRowStatus,
       "tFilterPortListLastChanged": tFilterPortListLastChanged,
       "tFilterPortListDescription": tFilterPortListDescription,
       "tFilterPortListEntryTblLstChg": tFilterPortListEntryTblLstChg,
       "tFilterPortListEntryTable": tFilterPortListEntryTable,
       "tFilterPortListEntryEntry": tFilterPortListEntryEntry,
       "tFilterPortListEntryPortLow": tFilterPortListEntryPortLow,
       "tFilterPortListEntryPortHigh": tFilterPortListEntryPortHigh,
       "tFilterPortListEntryRowStatus": tFilterPortListEntryRowStatus,
       "tFilterApplyPathTableLstChng": tFilterApplyPathTableLstChng,
       "tFilterApplyPathTable": tFilterApplyPathTable,
       "tFilterApplyPathEntry": tFilterApplyPathEntry,
       "tFilterApplyPathSource": tFilterApplyPathSource,
       "tFilterApplyPathIndex": tFilterApplyPathIndex,
       "tFilterApplyPathRowStatus": tFilterApplyPathRowStatus,
       "tFilterApplyPathLastChanged": tFilterApplyPathLastChanged,
       "tFilterApplyPathMatch1": tFilterApplyPathMatch1,
       "tFilterApplyPathMatch2": tFilterApplyPathMatch2,
       "tFilterEmbeddedRefInfoTable": tFilterEmbeddedRefInfoTable,
       "tFilterEmbeddedRefInfoEntry": tFilterEmbeddedRefInfoEntry,
       "tFltrEmbedRefInfEntryCnt": tFltrEmbedRefInfEntryCnt,
       "tFltrEmbedRefInfEntryCntInsrtd": tFltrEmbedRefInfEntryCntInsrtd,
       "tFilterEmbeddedEntryRefInfoTable": tFilterEmbeddedEntryRefInfoTable,
       "tFilterEmbeddedEntryRefInfoEntry": tFilterEmbeddedEntryRefInfoEntry,
       "tFltrEmbedEntryFilterType": tFltrEmbedEntryFilterType,
       "tFltrEmbedEntryInsertFltrId": tFltrEmbedEntryInsertFltrId,
       "tFltrEmbedEntryEmbeddedFltrId": tFltrEmbedEntryEmbeddedFltrId,
       "tFltrEmbedEntryEmbeddedEntryId": tFltrEmbedEntryEmbeddedEntryId,
       "tFltrEmbedEntryInsrtEntryId": tFltrEmbedEntryInsrtEntryId,
       "tFltrEmbedEntryRefOperState": tFltrEmbedEntryRefOperState,
       "tIPv6FilterParamsExtTbleLstChgd": tIPv6FilterParamsExtTbleLstChgd,
       "tIPv6FilterParamsExtTable": tIPv6FilterParamsExtTable,
       "tIPv6FilterParamsExtEntry": tIPv6FilterParamsExtEntry,
       "tIPv6FilterParamsExtLastChanged": tIPv6FilterParamsExtLastChanged,
       "tIPv6FilterParamsExtAhExtHdr": tIPv6FilterParamsExtAhExtHdr,
       "tIPv6FilterParamsExtEspExtHdr": tIPv6FilterParamsExtEspExtHdr,
       "tIPv6FilterParamsExtNatType": tIPv6FilterParamsExtNatType,
       "tFilterEmbedOpenflowTableLstChg": tFilterEmbedOpenflowTableLstChg,
       "tFilterEmbedOpenflowTable": tFilterEmbedOpenflowTable,
       "tFilterEmbedOpenflowEntry": tFilterEmbedOpenflowEntry,
       "tFilterEmbedOpenflowOfsName": tFilterEmbedOpenflowOfsName,
       "tFilterEmbedOpenflowFilterType": tFilterEmbedOpenflowFilterType,
       "tFilterEmbedOpenflowInsertFltrId": tFilterEmbedOpenflowInsertFltrId,
       "tFilterEmbedOpenflowOffset": tFilterEmbedOpenflowOffset,
       "tFilterEmbedOpenflowRowStatus": tFilterEmbedOpenflowRowStatus,
       "tFilterEmbedOpenflowAdminState": tFilterEmbedOpenflowAdminState,
       "tFilterEmbedOpenflowOperState": tFilterEmbedOpenflowOperState,
       "tFilterEmbedOpenflowInfoTable": tFilterEmbedOpenflowInfoTable,
       "tFilterEmbedOpenflowInfoEntry": tFilterEmbedOpenflowInfoEntry,
       "tFltrEmbedOfInfoEntryCnt": tFltrEmbedOfInfoEntryCnt,
       "tFltrEmbedOfInfoEntryCntInsrtd": tFltrEmbedOfInfoEntryCntInsrtd,
       "tFilterOpenflowEntryInfoTable": tFilterOpenflowEntryInfoTable,
       "tFilterOpenflowEntryInfoEntry": tFilterOpenflowEntryInfoEntry,
       "tFltrEmbedOfEntryOfsName": tFltrEmbedOfEntryOfsName,
       "tFltrEmbedOfEntryFilterType": tFltrEmbedOfEntryFilterType,
       "tFltrEmbedOfEntryInsertFltrId": tFltrEmbedOfEntryInsertFltrId,
       "tFltrEmbedOfEntryOfEntryId": tFltrEmbedOfEntryOfEntryId,
       "tFltrEmbedOfEntryInsrtEntryId": tFltrEmbedOfEntryInsrtEntryId,
       "tFltrEmbedOfEntryInsrtEntryState": tFltrEmbedOfEntryInsrtEntryState,
       "tIPFilterParamsExtTbleLstChgd": tIPFilterParamsExtTbleLstChgd,
       "tIPFilterParamsExtTable": tIPFilterParamsExtTable,
       "tIPFilterParamsExtEntry": tIPFilterParamsExtEntry,
       "tIPFilterParamsExtLastChanged": tIPFilterParamsExtLastChanged,
       "tIPFilterParamsExtPktLenVal1": tIPFilterParamsExtPktLenVal1,
       "tIPFilterParamsExtPktLenVal2": tIPFilterParamsExtPktLenVal2,
       "tIPFilterParamsExtPktLenOper": tIPFilterParamsExtPktLenOper,
       "tFilterNotificationsPrefix": tFilterNotificationsPrefix,
       "tFilterNotifications": tFilterNotifications,
       "tIPFilterPBRPacketsDrop": tIPFilterPBRPacketsDrop,
       "tFilterEntryActivationFailed": tFilterEntryActivationFailed,
       "tFilterEntryActivationRestored": tFilterEntryActivationRestored,
       "tFilterSubInsSpaceAlarmRaised": tFilterSubInsSpaceAlarmRaised,
       "tFilterSubInsSpaceAlarmCleared": tFilterSubInsSpaceAlarmCleared,
       "tFilterSubInsFltrEntryDropped": tFilterSubInsFltrEntryDropped,
       "tFilterBgpFlowSpecProblem": tFilterBgpFlowSpecProblem,
       "tFilterApplyPathProblem": tFilterApplyPathProblem,
       "tFilterRadSharedFltrAlarmRaised": tFilterRadSharedFltrAlarmRaised,
       "tFilterRadSharedFltrAlarmClear": tFilterRadSharedFltrAlarmClear,
       "tFilterEmbeddingOperStateChange": tFilterEmbeddingOperStateChange,
       "tFilterEmbedOpenflowOperStateChg": tFilterEmbedOpenflowOperStateChg,
       "tFilterTmsEvent": tFilterTmsEvent}
)
