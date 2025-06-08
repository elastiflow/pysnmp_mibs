# SNMP MIB module (TN-FILTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_7483/TN-FILTER-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 18:08:43 2025
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

(InetAddressIPv6,
 InetAddressPrefixLength) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv6",
    "InetAddressPrefixLength")

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

(Dot1PPriority,
 IpAddressPrefixLength,
 SdpBindId,
 ServiceAccessPoint,
 TDSCPFilterActionValue,
 TDSCPNameOrEmpty,
 TEntryId,
 TEntryIndicator,
 TFrameType,
 TIpOption,
 TIpProtocol,
 TItemDescription,
 TItemMatch,
 TItemScope,
 TLNamedItemOrEmpty,
 TMacFilterType,
 TNamedItem,
 TNamedItemOrEmpty,
 TTcpUdpPort,
 TTcpUdpPortOperator,
 TmnxAdminState,
 TmnxEncapVal,
 TmnxOperState,
 TmnxPortID,
 TmnxServId) = mibBuilder.importSymbols(
    "TN-TC-MIB",
    "Dot1PPriority",
    "IpAddressPrefixLength",
    "SdpBindId",
    "ServiceAccessPoint",
    "TDSCPFilterActionValue",
    "TDSCPNameOrEmpty",
    "TEntryId",
    "TEntryIndicator",
    "TFrameType",
    "TIpOption",
    "TIpProtocol",
    "TItemDescription",
    "TItemMatch",
    "TItemScope",
    "TLNamedItemOrEmpty",
    "TMacFilterType",
    "TNamedItem",
    "TNamedItemOrEmpty",
    "TTcpUdpPort",
    "TTcpUdpPortOperator",
    "TmnxAdminState",
    "TmnxEncapVal",
    "TmnxOperState",
    "TmnxPortID",
    "TmnxServId")

(tnSRMIBModules,
 tnSRNotifyPrefix,
 tnSRObjs) = mibBuilder.importSymbols(
    "TROPIC-GLOBAL-REG",
    "tnSRMIBModules",
    "tnSRNotifyPrefix",
    "tnSRObjs")

(tnSysSwitchId,) = mibBuilder.importSymbols(
    "TROPIC-SYSTEM-MIB",
    "tnSysSwitchId")


# MODULE-IDENTITY

tnFilterMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 5, 1, 3, 21)
)
if mibBuilder.loadTexts:
    tnFilterMIBModule.setRevisions(
        ("1913-08-22 00:00",
         "1912-12-05 00:00",
         "1908-07-01 00:00",
         "1908-01-01 00:00",
         "1907-01-01 00:00",
         "1906-02-28 00:00",
         "1905-08-31 00:00",
         "1905-01-24 00:00",
         "1904-01-15 00:00",
         "1903-08-15 00:00",
         "1903-01-29 00:00")
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


class TMACFilterID(TFilterID):
    status = "current"


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
              4)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("forward", 2),
          ("httpRedirect", 4))
    )



class TFilterActionOrDefault(TextualConvention, Integer32):
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
        *(("drop", 1),
          ("forward", 2),
          ("default", 3),
          ("httpRedirect", 4))
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



# MIB Managed Objects in the order of their OIDs

_TnFilterObjects_ObjectIdentity = ObjectIdentity
tnFilterObjects = _TnFilterObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 21)
)
_TnMacFilterTable_Object = MibTable
tnMacFilterTable = _TnMacFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 21, 3)
)
if mibBuilder.loadTexts:
    tnMacFilterTable.setStatus("current")
_TnMacFilterEntry_Object = MibTableRow
tnMacFilterEntry = _TnMacFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 21, 3, 1)
)
tnMacFilterEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-FILTER-MIB", "tnMacFilterId"),
)
if mibBuilder.loadTexts:
    tnMacFilterEntry.setStatus("current")


class _TnMacFilterId_Type(TMACFilterID):
    """Custom type tnMacFilterId based on TMACFilterID"""
    subtypeSpec = TMACFilterID.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TnMacFilterId_Type.__name__ = "TMACFilterID"
_TnMacFilterId_Object = MibTableColumn
tnMacFilterId = _TnMacFilterId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 21, 3, 1, 1),
    _TnMacFilterId_Type()
)
tnMacFilterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnMacFilterId.setStatus("current")
_TnMacFilterRowStatus_Type = RowStatus
_TnMacFilterRowStatus_Object = MibTableColumn
tnMacFilterRowStatus = _TnMacFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 21, 3, 1, 2),
    _TnMacFilterRowStatus_Type()
)
tnMacFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnMacFilterRowStatus.setStatus("current")


class _TnMacFilterScope_Type(TItemScope):
    """Custom type tnMacFilterScope based on TItemScope"""
    defaultValue = 2


_TnMacFilterScope_Type.__name__ = "TItemScope"
_TnMacFilterScope_Object = MibTableColumn
tnMacFilterScope = _TnMacFilterScope_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 21, 3, 1, 3),
    _TnMacFilterScope_Type()
)
tnMacFilterScope.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnMacFilterScope.setStatus("current")


class _TnMacFilterDescription_Type(TItemDescription):
    """Custom type tnMacFilterDescription based on TItemDescription"""
    defaultHexValue = ""


_TnMacFilterDescription_Type.__name__ = "TItemDescription"
_TnMacFilterDescription_Object = MibTableColumn
tnMacFilterDescription = _TnMacFilterDescription_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 21, 3, 1, 4),
    _TnMacFilterDescription_Type()
)
tnMacFilterDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnMacFilterDescription.setStatus("current")


class _TnMacFilterDefaultAction_Type(TFilterAction):
    """Custom type tnMacFilterDefaultAction based on TFilterAction"""
    defaultValue = 1


_TnMacFilterDefaultAction_Type.__name__ = "TFilterAction"
_TnMacFilterDefaultAction_Object = MibTableColumn
tnMacFilterDefaultAction = _TnMacFilterDefaultAction_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 21, 3, 1, 5),
    _TnMacFilterDefaultAction_Type()
)
tnMacFilterDefaultAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnMacFilterDefaultAction.setStatus("current")


class _TnMacFilterType_Type(TMacFilterType):
    """Custom type tnMacFilterType based on TMacFilterType"""
    defaultValue = 1


_TnMacFilterType_Type.__name__ = "TMacFilterType"
_TnMacFilterType_Object = MibTableColumn
tnMacFilterType = _TnMacFilterType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 21, 3, 1, 6),
    _TnMacFilterType_Type()
)
tnMacFilterType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnMacFilterType.setStatus("current")


class _TnMacFilterName_Type(TLNamedItemOrEmpty):
    """Custom type tnMacFilterName based on TLNamedItemOrEmpty"""
    defaultHexValue = ""


_TnMacFilterName_Type.__name__ = "TLNamedItemOrEmpty"
_TnMacFilterName_Object = MibTableColumn
tnMacFilterName = _TnMacFilterName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 21, 3, 1, 7),
    _TnMacFilterName_Type()
)
tnMacFilterName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnMacFilterName.setStatus("current")
_TnMacFilterParamsTable_Object = MibTable
tnMacFilterParamsTable = _TnMacFilterParamsTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 21, 4)
)
if mibBuilder.loadTexts:
    tnMacFilterParamsTable.setStatus("current")
_TnMacFilterParamsEntry_Object = MibTableRow
tnMacFilterParamsEntry = _TnMacFilterParamsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 21, 4, 1)
)
tnMacFilterParamsEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-FILTER-MIB", "tnMacFilterId"),
    (0, "TN-FILTER-MIB", "tnMacFilterParamsIndex"),
)
if mibBuilder.loadTexts:
    tnMacFilterParamsEntry.setStatus("current")
_TnMacFilterParamsIndex_Type = TEntryId
_TnMacFilterParamsIndex_Object = MibTableColumn
tnMacFilterParamsIndex = _TnMacFilterParamsIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 21, 4, 1, 1),
    _TnMacFilterParamsIndex_Type()
)
tnMacFilterParamsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnMacFilterParamsIndex.setStatus("current")
_TnMacFilterParamsRowStatus_Type = RowStatus
_TnMacFilterParamsRowStatus_Object = MibTableColumn
tnMacFilterParamsRowStatus = _TnMacFilterParamsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 21, 4, 1, 2),
    _TnMacFilterParamsRowStatus_Type()
)
tnMacFilterParamsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnMacFilterParamsRowStatus.setStatus("current")


class _TnMacFilterParamsLogId_Type(TFilterLogId):
    """Custom type tnMacFilterParamsLogId based on TFilterLogId"""
    defaultValue = 0


_TnMacFilterParamsLogId_Type.__name__ = "TFilterLogId"
_TnMacFilterParamsLogId_Object = MibTableColumn
tnMacFilterParamsLogId = _TnMacFilterParamsLogId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 21, 4, 1, 3),
    _TnMacFilterParamsLogId_Type()
)
tnMacFilterParamsLogId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnMacFilterParamsLogId.setStatus("current")


class _TnMacFilterParamsDescription_Type(TItemDescription):
    """Custom type tnMacFilterParamsDescription based on TItemDescription"""
    defaultHexValue = ""


_TnMacFilterParamsDescription_Type.__name__ = "TItemDescription"
_TnMacFilterParamsDescription_Object = MibTableColumn
tnMacFilterParamsDescription = _TnMacFilterParamsDescription_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 21, 4, 1, 4),
    _TnMacFilterParamsDescription_Type()
)
tnMacFilterParamsDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnMacFilterParamsDescription.setStatus("current")


class _TnMacFilterParamsAction_Type(TFilterActionOrDefault):
    """Custom type tnMacFilterParamsAction based on TFilterActionOrDefault"""
    defaultValue = 1


_TnMacFilterParamsAction_Type.__name__ = "TFilterActionOrDefault"
_TnMacFilterParamsAction_Object = MibTableColumn
tnMacFilterParamsAction = _TnMacFilterParamsAction_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 21, 4, 1, 5),
    _TnMacFilterParamsAction_Type()
)
tnMacFilterParamsAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnMacFilterParamsAction.setStatus("current")


class _TnMacFilterParamsFrameType_Type(TFrameType):
    """Custom type tnMacFilterParamsFrameType based on TFrameType"""
    defaultValue = 0


_TnMacFilterParamsFrameType_Type.__name__ = "TFrameType"
_TnMacFilterParamsFrameType_Object = MibTableColumn
tnMacFilterParamsFrameType = _TnMacFilterParamsFrameType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 21, 4, 1, 6),
    _TnMacFilterParamsFrameType_Type()
)
tnMacFilterParamsFrameType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnMacFilterParamsFrameType.setStatus("current")


class _TnMacFilterParamsSrcMAC_Type(MacAddress):
    """Custom type tnMacFilterParamsSrcMAC based on MacAddress"""
    defaultHexValue = "000000000000"


_TnMacFilterParamsSrcMAC_Type.__name__ = "MacAddress"
_TnMacFilterParamsSrcMAC_Object = MibTableColumn
tnMacFilterParamsSrcMAC = _TnMacFilterParamsSrcMAC_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 21, 4, 1, 8),
    _TnMacFilterParamsSrcMAC_Type()
)
tnMacFilterParamsSrcMAC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnMacFilterParamsSrcMAC.setStatus("current")


class _TnMacFilterParamsSrcMACMask_Type(MacAddress):
    """Custom type tnMacFilterParamsSrcMACMask based on MacAddress"""
    defaultHexValue = "000000000000"


_TnMacFilterParamsSrcMACMask_Type.__name__ = "MacAddress"
_TnMacFilterParamsSrcMACMask_Object = MibTableColumn
tnMacFilterParamsSrcMACMask = _TnMacFilterParamsSrcMACMask_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 21, 4, 1, 9),
    _TnMacFilterParamsSrcMACMask_Type()
)
tnMacFilterParamsSrcMACMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnMacFilterParamsSrcMACMask.setStatus("current")


class _TnMacFilterParamsDstMAC_Type(MacAddress):
    """Custom type tnMacFilterParamsDstMAC based on MacAddress"""
    defaultHexValue = "000000000000"


_TnMacFilterParamsDstMAC_Type.__name__ = "MacAddress"
_TnMacFilterParamsDstMAC_Object = MibTableColumn
tnMacFilterParamsDstMAC = _TnMacFilterParamsDstMAC_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 21, 4, 1, 10),
    _TnMacFilterParamsDstMAC_Type()
)
tnMacFilterParamsDstMAC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnMacFilterParamsDstMAC.setStatus("current")


class _TnMacFilterParamsDstMACMask_Type(MacAddress):
    """Custom type tnMacFilterParamsDstMACMask based on MacAddress"""
    defaultHexValue = "000000000000"


_TnMacFilterParamsDstMACMask_Type.__name__ = "MacAddress"
_TnMacFilterParamsDstMACMask_Object = MibTableColumn
tnMacFilterParamsDstMACMask = _TnMacFilterParamsDstMACMask_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 21, 4, 1, 11),
    _TnMacFilterParamsDstMACMask_Type()
)
tnMacFilterParamsDstMACMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnMacFilterParamsDstMACMask.setStatus("current")


class _TnMacFilterParamsDot1pValue_Type(Dot1PPriority):
    """Custom type tnMacFilterParamsDot1pValue based on Dot1PPriority"""
    defaultValue = -1


_TnMacFilterParamsDot1pValue_Type.__name__ = "Dot1PPriority"
_TnMacFilterParamsDot1pValue_Object = MibTableColumn
tnMacFilterParamsDot1pValue = _TnMacFilterParamsDot1pValue_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 21, 4, 1, 12),
    _TnMacFilterParamsDot1pValue_Type()
)
tnMacFilterParamsDot1pValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnMacFilterParamsDot1pValue.setStatus("current")


class _TnMacFilterParamsDot1pMask_Type(Dot1PPriority):
    """Custom type tnMacFilterParamsDot1pMask based on Dot1PPriority"""
    defaultValue = 0

    subtypeSpec = Dot1PPriority.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnMacFilterParamsDot1pMask_Type.__name__ = "Dot1PPriority"
_TnMacFilterParamsDot1pMask_Object = MibTableColumn
tnMacFilterParamsDot1pMask = _TnMacFilterParamsDot1pMask_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 21, 4, 1, 13),
    _TnMacFilterParamsDot1pMask_Type()
)
tnMacFilterParamsDot1pMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnMacFilterParamsDot1pMask.setStatus("current")


class _TnMacFilterParamsEtherType_Type(Integer32):
    """Custom type tnMacFilterParamsEtherType based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 65535),
    )


_TnMacFilterParamsEtherType_Type.__name__ = "Integer32"
_TnMacFilterParamsEtherType_Object = MibTableColumn
tnMacFilterParamsEtherType = _TnMacFilterParamsEtherType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 21, 4, 1, 14),
    _TnMacFilterParamsEtherType_Type()
)
tnMacFilterParamsEtherType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnMacFilterParamsEtherType.setStatus("current")


class _TnMacFilterParamsDsap_Type(ServiceAccessPoint):
    """Custom type tnMacFilterParamsDsap based on ServiceAccessPoint"""
    defaultValue = -1


_TnMacFilterParamsDsap_Type.__name__ = "ServiceAccessPoint"
_TnMacFilterParamsDsap_Object = MibTableColumn
tnMacFilterParamsDsap = _TnMacFilterParamsDsap_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 21, 4, 1, 15),
    _TnMacFilterParamsDsap_Type()
)
tnMacFilterParamsDsap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnMacFilterParamsDsap.setStatus("current")


class _TnMacFilterParamsDsapMask_Type(ServiceAccessPoint):
    """Custom type tnMacFilterParamsDsapMask based on ServiceAccessPoint"""
    defaultValue = -1


_TnMacFilterParamsDsapMask_Type.__name__ = "ServiceAccessPoint"
_TnMacFilterParamsDsapMask_Object = MibTableColumn
tnMacFilterParamsDsapMask = _TnMacFilterParamsDsapMask_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 21, 4, 1, 16),
    _TnMacFilterParamsDsapMask_Type()
)
tnMacFilterParamsDsapMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnMacFilterParamsDsapMask.setStatus("current")


class _TnMacFilterParamsSsap_Type(ServiceAccessPoint):
    """Custom type tnMacFilterParamsSsap based on ServiceAccessPoint"""
    defaultValue = -1


_TnMacFilterParamsSsap_Type.__name__ = "ServiceAccessPoint"
_TnMacFilterParamsSsap_Object = MibTableColumn
tnMacFilterParamsSsap = _TnMacFilterParamsSsap_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 21, 4, 1, 17),
    _TnMacFilterParamsSsap_Type()
)
tnMacFilterParamsSsap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnMacFilterParamsSsap.setStatus("current")


class _TnMacFilterParamsSsapMask_Type(ServiceAccessPoint):
    """Custom type tnMacFilterParamsSsapMask based on ServiceAccessPoint"""
    defaultValue = -1


_TnMacFilterParamsSsapMask_Type.__name__ = "ServiceAccessPoint"
_TnMacFilterParamsSsapMask_Object = MibTableColumn
tnMacFilterParamsSsapMask = _TnMacFilterParamsSsapMask_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 21, 4, 1, 18),
    _TnMacFilterParamsSsapMask_Type()
)
tnMacFilterParamsSsapMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnMacFilterParamsSsapMask.setStatus("current")


class _TnMacFilterParamsSnapPid_Type(Integer32):
    """Custom type tnMacFilterParamsSnapPid based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 65535),
    )


_TnMacFilterParamsSnapPid_Type.__name__ = "Integer32"
_TnMacFilterParamsSnapPid_Object = MibTableColumn
tnMacFilterParamsSnapPid = _TnMacFilterParamsSnapPid_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 21, 4, 1, 19),
    _TnMacFilterParamsSnapPid_Type()
)
tnMacFilterParamsSnapPid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnMacFilterParamsSnapPid.setStatus("current")


class _TnMacFilterParamsSnapOui_Type(Integer32):
    """Custom type tnMacFilterParamsSnapOui based on Integer32"""
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


_TnMacFilterParamsSnapOui_Type.__name__ = "Integer32"
_TnMacFilterParamsSnapOui_Object = MibTableColumn
tnMacFilterParamsSnapOui = _TnMacFilterParamsSnapOui_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 21, 4, 1, 20),
    _TnMacFilterParamsSnapOui_Type()
)
tnMacFilterParamsSnapOui.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnMacFilterParamsSnapOui.setStatus("current")
_TnMacFilterParamsIngressHitCount_Type = Counter64
_TnMacFilterParamsIngressHitCount_Object = MibTableColumn
tnMacFilterParamsIngressHitCount = _TnMacFilterParamsIngressHitCount_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 21, 4, 1, 21),
    _TnMacFilterParamsIngressHitCount_Type()
)
tnMacFilterParamsIngressHitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMacFilterParamsIngressHitCount.setStatus("current")
_TnMacFilterParamsEgressHitCount_Type = Counter64
_TnMacFilterParamsEgressHitCount_Object = MibTableColumn
tnMacFilterParamsEgressHitCount = _TnMacFilterParamsEgressHitCount_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 21, 4, 1, 22),
    _TnMacFilterParamsEgressHitCount_Type()
)
tnMacFilterParamsEgressHitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMacFilterParamsEgressHitCount.setStatus("current")
_TnMacFilterParamsLogInstantiated_Type = TruthValue
_TnMacFilterParamsLogInstantiated_Object = MibTableColumn
tnMacFilterParamsLogInstantiated = _TnMacFilterParamsLogInstantiated_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 21, 4, 1, 23),
    _TnMacFilterParamsLogInstantiated_Type()
)
tnMacFilterParamsLogInstantiated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMacFilterParamsLogInstantiated.setStatus("current")
_TnMacFilterParamsFwdSvcId_Type = TmnxServId
_TnMacFilterParamsFwdSvcId_Object = MibTableColumn
tnMacFilterParamsFwdSvcId = _TnMacFilterParamsFwdSvcId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 21, 4, 1, 24),
    _TnMacFilterParamsFwdSvcId_Type()
)
tnMacFilterParamsFwdSvcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMacFilterParamsFwdSvcId.setStatus("current")


class _TnMacFilterParamsFwdSapPortId_Type(TmnxPortID):
    """Custom type tnMacFilterParamsFwdSapPortId based on TmnxPortID"""
    defaultValue = 0


_TnMacFilterParamsFwdSapPortId_Type.__name__ = "TmnxPortID"
_TnMacFilterParamsFwdSapPortId_Object = MibTableColumn
tnMacFilterParamsFwdSapPortId = _TnMacFilterParamsFwdSapPortId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 21, 4, 1, 25),
    _TnMacFilterParamsFwdSapPortId_Type()
)
tnMacFilterParamsFwdSapPortId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnMacFilterParamsFwdSapPortId.setStatus("current")


class _TnMacFilterParamsFwdSapEncapVal_Type(TmnxEncapVal):
    """Custom type tnMacFilterParamsFwdSapEncapVal based on TmnxEncapVal"""
    defaultValue = 0


_TnMacFilterParamsFwdSapEncapVal_Type.__name__ = "TmnxEncapVal"
_TnMacFilterParamsFwdSapEncapVal_Object = MibTableColumn
tnMacFilterParamsFwdSapEncapVal = _TnMacFilterParamsFwdSapEncapVal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 21, 4, 1, 26),
    _TnMacFilterParamsFwdSapEncapVal_Type()
)
tnMacFilterParamsFwdSapEncapVal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnMacFilterParamsFwdSapEncapVal.setStatus("current")
_TnMacFilterParamsFwdSdpBind_Type = SdpBindId
_TnMacFilterParamsFwdSdpBind_Object = MibTableColumn
tnMacFilterParamsFwdSdpBind = _TnMacFilterParamsFwdSdpBind_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 21, 4, 1, 27),
    _TnMacFilterParamsFwdSdpBind_Type()
)
tnMacFilterParamsFwdSdpBind.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnMacFilterParamsFwdSdpBind.setStatus("current")


class _TnMacFilterParamsTimeRangeName_Type(TNamedItemOrEmpty):
    """Custom type tnMacFilterParamsTimeRangeName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TnMacFilterParamsTimeRangeName_Type.__name__ = "TNamedItemOrEmpty"
_TnMacFilterParamsTimeRangeName_Object = MibTableColumn
tnMacFilterParamsTimeRangeName = _TnMacFilterParamsTimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 21, 4, 1, 28),
    _TnMacFilterParamsTimeRangeName_Type()
)
tnMacFilterParamsTimeRangeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnMacFilterParamsTimeRangeName.setStatus("current")
_TnMacFilterParamsTimeRangeState_Type = TTimeRangeState
_TnMacFilterParamsTimeRangeState_Object = MibTableColumn
tnMacFilterParamsTimeRangeState = _TnMacFilterParamsTimeRangeState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 21, 4, 1, 29),
    _TnMacFilterParamsTimeRangeState_Type()
)
tnMacFilterParamsTimeRangeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMacFilterParamsTimeRangeState.setStatus("current")
_TnMacFilterParamsRedirectURL_Type = DisplayString
_TnMacFilterParamsRedirectURL_Object = MibTableColumn
tnMacFilterParamsRedirectURL = _TnMacFilterParamsRedirectURL_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 21, 4, 1, 30),
    _TnMacFilterParamsRedirectURL_Type()
)
tnMacFilterParamsRedirectURL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnMacFilterParamsRedirectURL.setStatus("current")
_TnMacFilterParamsIngrHitByteCount_Type = Counter64
_TnMacFilterParamsIngrHitByteCount_Object = MibTableColumn
tnMacFilterParamsIngrHitByteCount = _TnMacFilterParamsIngrHitByteCount_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 21, 4, 1, 31),
    _TnMacFilterParamsIngrHitByteCount_Type()
)
tnMacFilterParamsIngrHitByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMacFilterParamsIngrHitByteCount.setStatus("current")
_TnMacFilterParamsEgrHitByteCount_Type = Counter64
_TnMacFilterParamsEgrHitByteCount_Object = MibTableColumn
tnMacFilterParamsEgrHitByteCount = _TnMacFilterParamsEgrHitByteCount_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 21, 4, 1, 32),
    _TnMacFilterParamsEgrHitByteCount_Type()
)
tnMacFilterParamsEgrHitByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMacFilterParamsEgrHitByteCount.setStatus("current")
_TnFilterScalar1_Type = Unsigned32
_TnFilterScalar1_Object = MibScalar
tnFilterScalar1 = _TnFilterScalar1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 21, 101),
    _TnFilterScalar1_Type()
)
tnFilterScalar1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnFilterScalar1.setStatus("current")
_TnFilterScalar2_Type = Unsigned32
_TnFilterScalar2_Object = MibScalar
tnFilterScalar2 = _TnFilterScalar2_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 21, 102),
    _TnFilterScalar2_Type()
)
tnFilterScalar2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnFilterScalar2.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TN-FILTER-MIB",
    **{"TFilterID": TFilterID,
       "TIPFilterID": TIPFilterID,
       "TMACFilterID": TMACFilterID,
       "TEntryIdOrZero": TEntryIdOrZero,
       "TFilterAction": TFilterAction,
       "TFilterActionOrDefault": TFilterActionOrDefault,
       "TFilterLogId": TFilterLogId,
       "TFilterLogDestination": TFilterLogDestination,
       "TTimeRangeState": TTimeRangeState,
       "TFilterLogSummaryCriterium": TFilterLogSummaryCriterium,
       "TFilterType": TFilterType,
       "tnFilterMIBModule": tnFilterMIBModule,
       "tnFilterObjects": tnFilterObjects,
       "tnMacFilterTable": tnMacFilterTable,
       "tnMacFilterEntry": tnMacFilterEntry,
       "tnMacFilterId": tnMacFilterId,
       "tnMacFilterRowStatus": tnMacFilterRowStatus,
       "tnMacFilterScope": tnMacFilterScope,
       "tnMacFilterDescription": tnMacFilterDescription,
       "tnMacFilterDefaultAction": tnMacFilterDefaultAction,
       "tnMacFilterType": tnMacFilterType,
       "tnMacFilterName": tnMacFilterName,
       "tnMacFilterParamsTable": tnMacFilterParamsTable,
       "tnMacFilterParamsEntry": tnMacFilterParamsEntry,
       "tnMacFilterParamsIndex": tnMacFilterParamsIndex,
       "tnMacFilterParamsRowStatus": tnMacFilterParamsRowStatus,
       "tnMacFilterParamsLogId": tnMacFilterParamsLogId,
       "tnMacFilterParamsDescription": tnMacFilterParamsDescription,
       "tnMacFilterParamsAction": tnMacFilterParamsAction,
       "tnMacFilterParamsFrameType": tnMacFilterParamsFrameType,
       "tnMacFilterParamsSrcMAC": tnMacFilterParamsSrcMAC,
       "tnMacFilterParamsSrcMACMask": tnMacFilterParamsSrcMACMask,
       "tnMacFilterParamsDstMAC": tnMacFilterParamsDstMAC,
       "tnMacFilterParamsDstMACMask": tnMacFilterParamsDstMACMask,
       "tnMacFilterParamsDot1pValue": tnMacFilterParamsDot1pValue,
       "tnMacFilterParamsDot1pMask": tnMacFilterParamsDot1pMask,
       "tnMacFilterParamsEtherType": tnMacFilterParamsEtherType,
       "tnMacFilterParamsDsap": tnMacFilterParamsDsap,
       "tnMacFilterParamsDsapMask": tnMacFilterParamsDsapMask,
       "tnMacFilterParamsSsap": tnMacFilterParamsSsap,
       "tnMacFilterParamsSsapMask": tnMacFilterParamsSsapMask,
       "tnMacFilterParamsSnapPid": tnMacFilterParamsSnapPid,
       "tnMacFilterParamsSnapOui": tnMacFilterParamsSnapOui,
       "tnMacFilterParamsIngressHitCount": tnMacFilterParamsIngressHitCount,
       "tnMacFilterParamsEgressHitCount": tnMacFilterParamsEgressHitCount,
       "tnMacFilterParamsLogInstantiated": tnMacFilterParamsLogInstantiated,
       "tnMacFilterParamsFwdSvcId": tnMacFilterParamsFwdSvcId,
       "tnMacFilterParamsFwdSapPortId": tnMacFilterParamsFwdSapPortId,
       "tnMacFilterParamsFwdSapEncapVal": tnMacFilterParamsFwdSapEncapVal,
       "tnMacFilterParamsFwdSdpBind": tnMacFilterParamsFwdSdpBind,
       "tnMacFilterParamsTimeRangeName": tnMacFilterParamsTimeRangeName,
       "tnMacFilterParamsTimeRangeState": tnMacFilterParamsTimeRangeState,
       "tnMacFilterParamsRedirectURL": tnMacFilterParamsRedirectURL,
       "tnMacFilterParamsIngrHitByteCount": tnMacFilterParamsIngrHitByteCount,
       "tnMacFilterParamsEgrHitByteCount": tnMacFilterParamsEgrHitByteCount,
       "tnFilterScalar1": tnFilterScalar1,
       "tnFilterScalar2": tnFilterScalar2}
)
