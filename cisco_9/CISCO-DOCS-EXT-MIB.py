# SNMP MIB module (CISCO-DOCS-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-DOCS-EXT-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:05:18 2025
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(TenthdBmV,
 docsIfCmtsCmStatusDownChannelIfIndex,
 docsIfCmtsCmStatusEntry,
 docsIfCmtsCmStatusIndex,
 docsIfCmtsCmStatusInetAddress,
 docsIfCmtsCmStatusInetAddressType,
 docsIfCmtsCmStatusMacAddress,
 docsIfCmtsCmStatusUpChannelIfIndex,
 docsIfCmtsMacEntry,
 docsIfCmtsServiceEntry,
 docsIfUpstreamChannelEntry) = mibBuilder.importSymbols(
    "DOCS-IF-MIB",
    "TenthdBmV",
    "docsIfCmtsCmStatusDownChannelIfIndex",
    "docsIfCmtsCmStatusEntry",
    "docsIfCmtsCmStatusIndex",
    "docsIfCmtsCmStatusInetAddress",
    "docsIfCmtsCmStatusInetAddressType",
    "docsIfCmtsCmStatusMacAddress",
    "docsIfCmtsCmStatusUpChannelIfIndex",
    "docsIfCmtsMacEntry",
    "docsIfCmtsServiceEntry",
    "docsIfUpstreamChannelEntry")

(ChSetId,) = mibBuilder.importSymbols(
    "DOCS-IF3-MIB",
    "ChSetId")

(InterfaceIndex,
 InterfaceIndexOrZero,
 ifDescr,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
    "ifDescr",
    "ifIndex")

(InetAddress,
 InetAddressIPv6,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressIPv6",
    "InetAddressPrefixLength",
    "InetAddressType")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(SnmpTagList,) = mibBuilder.importSymbols(
    "SNMP-TARGET-MIB",
    "SnmpTagList")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoDocsExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 116)
)
if mibBuilder.loadTexts:
    ciscoDocsExtMIB.setRevisions(
        ("2024-05-10 00:00",
         "2017-11-10 00:00",
         "2017-07-20 00:00",
         "2017-02-18 00:00",
         "2016-06-08 00:00",
         "2018-08-16 00:00",
         "2013-12-10 00:00",
         "2013-03-27 00:00",
         "2012-09-07 00:00",
         "2010-06-09 00:00",
         "2006-03-06 00:00",
         "2005-07-01 00:00",
         "2005-04-25 00:00",
         "2004-07-22 00:00",
         "2003-07-30 00:00",
         "2003-02-20 00:00",
         "2002-10-11 00:00",
         "2001-10-07 00:00",
         "2001-08-06 00:00",
         "2001-04-01 00:00",
         "2000-07-19 00:00",
         "2000-05-17 00:00",
         "1999-12-28 00:00",
         "1999-01-21 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class CdxResettableCounter32(TextualConvention, Gauge32):
    status = "current"


class CdxUpstreamBondGrpList(TextualConvention, OctetString):
    status = "current"
    displayHint = "320a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 320),
    )



# MIB Managed Objects in the order of their OIDs

_CiscoDocsExtMIBObjects_ObjectIdentity = ObjectIdentity
ciscoDocsExtMIBObjects = _CiscoDocsExtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1)
)
_CdxQosCtrlObjects_ObjectIdentity = ObjectIdentity
cdxQosCtrlObjects = _CdxQosCtrlObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 1)
)
_CdxQosCtrlUpTable_Object = MibTable
cdxQosCtrlUpTable = _CdxQosCtrlUpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cdxQosCtrlUpTable.setStatus("current")
_CdxQosCtrlUpEntry_Object = MibTableRow
cdxQosCtrlUpEntry = _CdxQosCtrlUpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 1, 1, 1)
)
cdxQosCtrlUpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cdxQosCtrlUpEntry.setStatus("current")
_CdxQosCtrlUpAdmissionCtrl_Type = TruthValue
_CdxQosCtrlUpAdmissionCtrl_Object = MibTableColumn
cdxQosCtrlUpAdmissionCtrl = _CdxQosCtrlUpAdmissionCtrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 1, 1, 1, 1),
    _CdxQosCtrlUpAdmissionCtrl_Type()
)
cdxQosCtrlUpAdmissionCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdxQosCtrlUpAdmissionCtrl.setStatus("current")


class _CdxQosCtrlUpMaxRsvdBWPercent_Type(Integer32):
    """Custom type cdxQosCtrlUpMaxRsvdBWPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000),
    )


_CdxQosCtrlUpMaxRsvdBWPercent_Type.__name__ = "Integer32"
_CdxQosCtrlUpMaxRsvdBWPercent_Object = MibTableColumn
cdxQosCtrlUpMaxRsvdBWPercent = _CdxQosCtrlUpMaxRsvdBWPercent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 1, 1, 1, 2),
    _CdxQosCtrlUpMaxRsvdBWPercent_Type()
)
cdxQosCtrlUpMaxRsvdBWPercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdxQosCtrlUpMaxRsvdBWPercent.setStatus("current")
if mibBuilder.loadTexts:
    cdxQosCtrlUpMaxRsvdBWPercent.setUnits("percent")
_CdxQosCtrlUpAdmissionRejects_Type = Counter32
_CdxQosCtrlUpAdmissionRejects_Object = MibTableColumn
cdxQosCtrlUpAdmissionRejects = _CdxQosCtrlUpAdmissionRejects_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 1, 1, 1, 3),
    _CdxQosCtrlUpAdmissionRejects_Type()
)
cdxQosCtrlUpAdmissionRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxQosCtrlUpAdmissionRejects.setStatus("current")


class _CdxQosCtrlUpReservedBW_Type(Integer32):
    """Custom type cdxQosCtrlUpReservedBW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 102400000),
    )


_CdxQosCtrlUpReservedBW_Type.__name__ = "Integer32"
_CdxQosCtrlUpReservedBW_Object = MibTableColumn
cdxQosCtrlUpReservedBW = _CdxQosCtrlUpReservedBW_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 1, 1, 1, 4),
    _CdxQosCtrlUpReservedBW_Type()
)
cdxQosCtrlUpReservedBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxQosCtrlUpReservedBW.setStatus("current")
if mibBuilder.loadTexts:
    cdxQosCtrlUpReservedBW.setUnits("bits/second")


class _CdxQosCtrlUpMaxVirtualBW_Type(Integer32):
    """Custom type cdxQosCtrlUpMaxVirtualBW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 102400000),
    )


_CdxQosCtrlUpMaxVirtualBW_Type.__name__ = "Integer32"
_CdxQosCtrlUpMaxVirtualBW_Object = MibTableColumn
cdxQosCtrlUpMaxVirtualBW = _CdxQosCtrlUpMaxVirtualBW_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 1, 1, 1, 5),
    _CdxQosCtrlUpMaxVirtualBW_Type()
)
cdxQosCtrlUpMaxVirtualBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxQosCtrlUpMaxVirtualBW.setStatus("current")
if mibBuilder.loadTexts:
    cdxQosCtrlUpMaxVirtualBW.setUnits("bits/second")
_CdxQosIfRateLimitTable_Object = MibTable
cdxQosIfRateLimitTable = _CdxQosIfRateLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cdxQosIfRateLimitTable.setStatus("current")
_CdxQosIfRateLimitEntry_Object = MibTableRow
cdxQosIfRateLimitEntry = _CdxQosIfRateLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 1, 2, 1)
)
cdxQosIfRateLimitEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cdxQosIfRateLimitEntry.setStatus("current")


class _CdxQosIfRateLimitAlgm_Type(Integer32):
    """Custom type cdxQosIfRateLimitAlgm based on Integer32"""
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
        *(("noRateLimit", 1),
          ("oneSecBurst", 2),
          ("carLike", 3),
          ("wtExPacketDiscard", 4),
          ("shaping", 5))
    )


_CdxQosIfRateLimitAlgm_Type.__name__ = "Integer32"
_CdxQosIfRateLimitAlgm_Object = MibTableColumn
cdxQosIfRateLimitAlgm = _CdxQosIfRateLimitAlgm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 1, 2, 1, 1),
    _CdxQosIfRateLimitAlgm_Type()
)
cdxQosIfRateLimitAlgm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdxQosIfRateLimitAlgm.setStatus("current")


class _CdxQosIfRateLimitExpWt_Type(Integer32):
    """Custom type cdxQosIfRateLimitExpWt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_CdxQosIfRateLimitExpWt_Type.__name__ = "Integer32"
_CdxQosIfRateLimitExpWt_Object = MibTableColumn
cdxQosIfRateLimitExpWt = _CdxQosIfRateLimitExpWt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 1, 2, 1, 2),
    _CdxQosIfRateLimitExpWt_Type()
)
cdxQosIfRateLimitExpWt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdxQosIfRateLimitExpWt.setStatus("current")


class _CdxQosIfRateLimitShpMaxDelay_Type(Integer32):
    """Custom type cdxQosIfRateLimitShpMaxDelay based on Integer32"""
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
        *(("na", 1),
          ("msec128", 2),
          ("msec256", 3),
          ("msec512", 4),
          ("msec1024", 5))
    )


_CdxQosIfRateLimitShpMaxDelay_Type.__name__ = "Integer32"
_CdxQosIfRateLimitShpMaxDelay_Object = MibTableColumn
cdxQosIfRateLimitShpMaxDelay = _CdxQosIfRateLimitShpMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 1, 2, 1, 3),
    _CdxQosIfRateLimitShpMaxDelay_Type()
)
cdxQosIfRateLimitShpMaxDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdxQosIfRateLimitShpMaxDelay.setStatus("current")


class _CdxQosIfRateLimitShpGranularity_Type(Integer32):
    """Custom type cdxQosIfRateLimitShpGranularity based on Integer32"""
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
        *(("na", 1),
          ("msec1", 2),
          ("msec2", 3),
          ("msec4", 4),
          ("msec8", 5),
          ("msec16", 6))
    )


_CdxQosIfRateLimitShpGranularity_Type.__name__ = "Integer32"
_CdxQosIfRateLimitShpGranularity_Object = MibTableColumn
cdxQosIfRateLimitShpGranularity = _CdxQosIfRateLimitShpGranularity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 1, 2, 1, 4),
    _CdxQosIfRateLimitShpGranularity_Type()
)
cdxQosIfRateLimitShpGranularity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdxQosIfRateLimitShpGranularity.setStatus("current")
_CdxCmtsServiceExtTable_Object = MibTable
cdxCmtsServiceExtTable = _CdxCmtsServiceExtTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cdxCmtsServiceExtTable.setStatus("current")
_CdxCmtsServiceExtEntry_Object = MibTableRow
cdxCmtsServiceExtEntry = _CdxCmtsServiceExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cdxCmtsServiceExtEntry.setStatus("current")
_CdxIfCmtsServiceOutOctets_Type = Counter32
_CdxIfCmtsServiceOutOctets_Object = MibTableColumn
cdxIfCmtsServiceOutOctets = _CdxIfCmtsServiceOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 1, 3, 1, 1),
    _CdxIfCmtsServiceOutOctets_Type()
)
cdxIfCmtsServiceOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxIfCmtsServiceOutOctets.setStatus("current")
_CdxIfCmtsServiceOutPackets_Type = Counter32
_CdxIfCmtsServiceOutPackets_Object = MibTableColumn
cdxIfCmtsServiceOutPackets = _CdxIfCmtsServiceOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 1, 3, 1, 2),
    _CdxIfCmtsServiceOutPackets_Type()
)
cdxIfCmtsServiceOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxIfCmtsServiceOutPackets.setStatus("current")
_CdxQosMaxUpBWExcessRequests_Type = Counter32
_CdxQosMaxUpBWExcessRequests_Object = MibTableColumn
cdxQosMaxUpBWExcessRequests = _CdxQosMaxUpBWExcessRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 1, 3, 1, 3),
    _CdxQosMaxUpBWExcessRequests_Type()
)
cdxQosMaxUpBWExcessRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxQosMaxUpBWExcessRequests.setStatus("current")
_CdxQosMaxDownBWExcessPackets_Type = Counter32
_CdxQosMaxDownBWExcessPackets_Object = MibTableColumn
cdxQosMaxDownBWExcessPackets = _CdxQosMaxDownBWExcessPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 1, 3, 1, 4),
    _CdxQosMaxDownBWExcessPackets_Type()
)
cdxQosMaxDownBWExcessPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxQosMaxDownBWExcessPackets.setStatus("current")
_CdxIfCmtsServiceHCInOctets_Type = Counter64
_CdxIfCmtsServiceHCInOctets_Object = MibTableColumn
cdxIfCmtsServiceHCInOctets = _CdxIfCmtsServiceHCInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 1, 3, 1, 5),
    _CdxIfCmtsServiceHCInOctets_Type()
)
cdxIfCmtsServiceHCInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxIfCmtsServiceHCInOctets.setStatus("current")
_CdxIfCmtsServiceHCInPackets_Type = Counter64
_CdxIfCmtsServiceHCInPackets_Object = MibTableColumn
cdxIfCmtsServiceHCInPackets = _CdxIfCmtsServiceHCInPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 1, 3, 1, 6),
    _CdxIfCmtsServiceHCInPackets_Type()
)
cdxIfCmtsServiceHCInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxIfCmtsServiceHCInPackets.setStatus("current")
_CdxIfCmtsServiceHCOutOctets_Type = Counter64
_CdxIfCmtsServiceHCOutOctets_Object = MibTableColumn
cdxIfCmtsServiceHCOutOctets = _CdxIfCmtsServiceHCOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 1, 3, 1, 7),
    _CdxIfCmtsServiceHCOutOctets_Type()
)
cdxIfCmtsServiceHCOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxIfCmtsServiceHCOutOctets.setStatus("current")
_CdxIfCmtsServiceHCOutPackets_Type = Counter64
_CdxIfCmtsServiceHCOutPackets_Object = MibTableColumn
cdxIfCmtsServiceHCOutPackets = _CdxIfCmtsServiceHCOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 1, 3, 1, 8),
    _CdxIfCmtsServiceHCOutPackets_Type()
)
cdxIfCmtsServiceHCOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxIfCmtsServiceHCOutPackets.setStatus("current")
_CdxUpInfoElemStatsTable_Object = MibTable
cdxUpInfoElemStatsTable = _CdxUpInfoElemStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 1, 4)
)
if mibBuilder.loadTexts:
    cdxUpInfoElemStatsTable.setStatus("current")
_CdxUpInfoElemStatsEntry_Object = MibTableRow
cdxUpInfoElemStatsEntry = _CdxUpInfoElemStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 1, 4, 1)
)
cdxUpInfoElemStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-DOCS-EXT-MIB", "cdxUpInfoElemStatsNameCode"),
)
if mibBuilder.loadTexts:
    cdxUpInfoElemStatsEntry.setStatus("current")


class _CdxUpInfoElemStatsNameCode_Type(Integer32):
    """Custom type cdxUpInfoElemStatsNameCode based on Integer32"""
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
        *(("reqIE", 1),
          ("reqOrDataIE", 2),
          ("initMtnIE", 3),
          ("stnMtnIE", 4),
          ("shortGrantIE", 5),
          ("longGrantIE", 6))
    )


_CdxUpInfoElemStatsNameCode_Type.__name__ = "Integer32"
_CdxUpInfoElemStatsNameCode_Object = MibTableColumn
cdxUpInfoElemStatsNameCode = _CdxUpInfoElemStatsNameCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 1, 4, 1, 1),
    _CdxUpInfoElemStatsNameCode_Type()
)
cdxUpInfoElemStatsNameCode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdxUpInfoElemStatsNameCode.setStatus("current")
_CdxUpInfoElemStatsIEType_Type = Integer32
_CdxUpInfoElemStatsIEType_Object = MibTableColumn
cdxUpInfoElemStatsIEType = _CdxUpInfoElemStatsIEType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 1, 4, 1, 2),
    _CdxUpInfoElemStatsIEType_Type()
)
cdxUpInfoElemStatsIEType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxUpInfoElemStatsIEType.setStatus("current")
_CdxQosQueueObjects_ObjectIdentity = ObjectIdentity
cdxQosQueueObjects = _CdxQosQueueObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 2)
)
_CdxBWQueueTable_Object = MibTable
cdxBWQueueTable = _CdxBWQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cdxBWQueueTable.setStatus("current")
_CdxBWQueueEntry_Object = MibTableRow
cdxBWQueueEntry = _CdxBWQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 2, 1, 1)
)
cdxBWQueueEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-DOCS-EXT-MIB", "cdxBWQueueNameCode"),
)
if mibBuilder.loadTexts:
    cdxBWQueueEntry.setStatus("current")


class _CdxBWQueueNameCode_Type(Integer32):
    """Custom type cdxBWQueueNameCode based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("cirQ", 1),
          ("tbeQ", 2),
          ("p0BEGrantQ", 3),
          ("p1BEGrantQ", 4),
          ("p2BEGrantQ", 5),
          ("p3BEGrantQ", 6),
          ("p4BEGrantQ", 7),
          ("p5BEGrantQ", 8),
          ("p6BEGrantQ", 9),
          ("p7BEGrantQ", 10),
          ("rngPollQ", 11))
    )


_CdxBWQueueNameCode_Type.__name__ = "Integer32"
_CdxBWQueueNameCode_Object = MibTableColumn
cdxBWQueueNameCode = _CdxBWQueueNameCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 2, 1, 1, 1),
    _CdxBWQueueNameCode_Type()
)
cdxBWQueueNameCode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdxBWQueueNameCode.setStatus("current")


class _CdxBWQueueOrder_Type(Integer32):
    """Custom type cdxBWQueueOrder based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_CdxBWQueueOrder_Type.__name__ = "Integer32"
_CdxBWQueueOrder_Object = MibTableColumn
cdxBWQueueOrder = _CdxBWQueueOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 2, 1, 1, 2),
    _CdxBWQueueOrder_Type()
)
cdxBWQueueOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxBWQueueOrder.setStatus("current")


class _CdxBWQueueNumServedBeforeYield_Type(Integer32):
    """Custom type cdxBWQueueNumServedBeforeYield based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_CdxBWQueueNumServedBeforeYield_Type.__name__ = "Integer32"
_CdxBWQueueNumServedBeforeYield_Object = MibTableColumn
cdxBWQueueNumServedBeforeYield = _CdxBWQueueNumServedBeforeYield_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 2, 1, 1, 3),
    _CdxBWQueueNumServedBeforeYield_Type()
)
cdxBWQueueNumServedBeforeYield.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxBWQueueNumServedBeforeYield.setStatus("current")


class _CdxBWQueueType_Type(Integer32):
    """Custom type cdxBWQueueType based on Integer32"""
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
        *(("unknown", 1),
          ("other", 2),
          ("fifo", 3),
          ("priority", 4))
    )


_CdxBWQueueType_Type.__name__ = "Integer32"
_CdxBWQueueType_Object = MibTableColumn
cdxBWQueueType = _CdxBWQueueType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 2, 1, 1, 4),
    _CdxBWQueueType_Type()
)
cdxBWQueueType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxBWQueueType.setStatus("current")


class _CdxBWQueueMaxDepth_Type(Integer32):
    """Custom type cdxBWQueueMaxDepth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_CdxBWQueueMaxDepth_Type.__name__ = "Integer32"
_CdxBWQueueMaxDepth_Object = MibTableColumn
cdxBWQueueMaxDepth = _CdxBWQueueMaxDepth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 2, 1, 1, 5),
    _CdxBWQueueMaxDepth_Type()
)
cdxBWQueueMaxDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxBWQueueMaxDepth.setStatus("current")


class _CdxBWQueueDepth_Type(Integer32):
    """Custom type cdxBWQueueDepth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_CdxBWQueueDepth_Type.__name__ = "Integer32"
_CdxBWQueueDepth_Object = MibTableColumn
cdxBWQueueDepth = _CdxBWQueueDepth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 2, 1, 1, 6),
    _CdxBWQueueDepth_Type()
)
cdxBWQueueDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxBWQueueDepth.setStatus("current")
_CdxBWQueueDiscards_Type = Counter32
_CdxBWQueueDiscards_Object = MibTableColumn
cdxBWQueueDiscards = _CdxBWQueueDiscards_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 2, 1, 1, 7),
    _CdxBWQueueDiscards_Type()
)
cdxBWQueueDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxBWQueueDiscards.setStatus("current")
_CdxCmtsCmCpeObjects_ObjectIdentity = ObjectIdentity
cdxCmtsCmCpeObjects = _CdxCmtsCmCpeObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3)
)
_CdxCmCpeTable_Object = MibTable
cdxCmCpeTable = _CdxCmCpeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cdxCmCpeTable.setStatus("current")
_CdxCmCpeEntry_Object = MibTableRow
cdxCmCpeEntry = _CdxCmCpeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 1, 1)
)
cdxCmCpeEntry.setIndexNames(
    (0, "CISCO-DOCS-EXT-MIB", "cdxCmCpeMacAddress"),
)
if mibBuilder.loadTexts:
    cdxCmCpeEntry.setStatus("current")
_CdxCmCpeMacAddress_Type = MacAddress
_CdxCmCpeMacAddress_Object = MibTableColumn
cdxCmCpeMacAddress = _CdxCmCpeMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 1, 1, 1),
    _CdxCmCpeMacAddress_Type()
)
cdxCmCpeMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdxCmCpeMacAddress.setStatus("current")


class _CdxCmCpeType_Type(Integer32):
    """Custom type cdxCmCpeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cm", 1),
          ("cpe", 2))
    )


_CdxCmCpeType_Type.__name__ = "Integer32"
_CdxCmCpeType_Object = MibTableColumn
cdxCmCpeType = _CdxCmCpeType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 1, 1, 2),
    _CdxCmCpeType_Type()
)
cdxCmCpeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxCmCpeType.setStatus("current")
_CdxCmCpeIpAddress_Type = IpAddress
_CdxCmCpeIpAddress_Object = MibTableColumn
cdxCmCpeIpAddress = _CdxCmCpeIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 1, 1, 3),
    _CdxCmCpeIpAddress_Type()
)
cdxCmCpeIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxCmCpeIpAddress.setStatus("current")
_CdxCmCpeIfIndex_Type = InterfaceIndex
_CdxCmCpeIfIndex_Object = MibTableColumn
cdxCmCpeIfIndex = _CdxCmCpeIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 1, 1, 4),
    _CdxCmCpeIfIndex_Type()
)
cdxCmCpeIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxCmCpeIfIndex.setStatus("current")


class _CdxCmCpeCmtsServiceId_Type(Integer32):
    """Custom type cdxCmCpeCmtsServiceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16383),
    )


_CdxCmCpeCmtsServiceId_Type.__name__ = "Integer32"
_CdxCmCpeCmtsServiceId_Object = MibTableColumn
cdxCmCpeCmtsServiceId = _CdxCmCpeCmtsServiceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 1, 1, 5),
    _CdxCmCpeCmtsServiceId_Type()
)
cdxCmCpeCmtsServiceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxCmCpeCmtsServiceId.setStatus("current")


class _CdxCmCpeCmStatusIndex_Type(Integer32):
    """Custom type cdxCmCpeCmStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CdxCmCpeCmStatusIndex_Type.__name__ = "Integer32"
_CdxCmCpeCmStatusIndex_Object = MibTableColumn
cdxCmCpeCmStatusIndex = _CdxCmCpeCmStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 1, 1, 6),
    _CdxCmCpeCmStatusIndex_Type()
)
cdxCmCpeCmStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxCmCpeCmStatusIndex.setStatus("current")
_CdxCmCpeAccessGroup_Type = DisplayString
_CdxCmCpeAccessGroup_Object = MibTableColumn
cdxCmCpeAccessGroup = _CdxCmCpeAccessGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 1, 1, 7),
    _CdxCmCpeAccessGroup_Type()
)
cdxCmCpeAccessGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdxCmCpeAccessGroup.setStatus("current")
_CdxCmCpeResetNow_Type = TruthValue
_CdxCmCpeResetNow_Object = MibTableColumn
cdxCmCpeResetNow = _CdxCmCpeResetNow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 1, 1, 8),
    _CdxCmCpeResetNow_Type()
)
cdxCmCpeResetNow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdxCmCpeResetNow.setStatus("current")
_CdxCmCpeDeleteNow_Type = TruthValue
_CdxCmCpeDeleteNow_Object = MibTableColumn
cdxCmCpeDeleteNow = _CdxCmCpeDeleteNow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 1, 1, 9),
    _CdxCmCpeDeleteNow_Type()
)
cdxCmCpeDeleteNow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdxCmCpeDeleteNow.setStatus("current")
_CdxCmtsCmStatusExtTable_Object = MibTable
cdxCmtsCmStatusExtTable = _CdxCmtsCmStatusExtTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 2)
)
if mibBuilder.loadTexts:
    cdxCmtsCmStatusExtTable.setStatus("current")
_CdxCmtsCmStatusExtEntry_Object = MibTableRow
cdxCmtsCmStatusExtEntry = _CdxCmtsCmStatusExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    cdxCmtsCmStatusExtEntry.setStatus("current")


class _CdxCmtsCmStatusValue_Type(Integer32):
    """Custom type cdxCmtsCmStatusValue based on Integer32"""
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
              27)
        )
    )
    namedValues = NamedValues(
        *(("offline", 1),
          ("others", 2),
          ("initRangingRcvd", 3),
          ("initDhcpReqRcvd", 4),
          ("onlineNetAccessDisabled", 5),
          ("onlineKekAssigned", 6),
          ("onlineTekAssigned", 7),
          ("rejectBadMic", 8),
          ("rejectBadCos", 9),
          ("kekRejected", 10),
          ("tekRejected", 11),
          ("online", 12),
          ("initTftpPacketRcvd", 13),
          ("initTodRequestRcvd", 14),
          ("reset", 15),
          ("rangingInProgress", 16),
          ("rangingCompleted", 17),
          ("dhcpGotIpAddr", 18),
          ("rejStaleConfig", 19),
          ("rejIpSpoof", 20),
          ("rejClassFail", 21),
          ("rejRegNack", 22),
          ("bpiKekExpired", 23),
          ("bpiTekExpired", 24),
          ("shutdown", 25),
          ("channelChgInitRangingRcvd", 26),
          ("channelChgRangingInProgress", 27))
    )


_CdxCmtsCmStatusValue_Type.__name__ = "Integer32"
_CdxCmtsCmStatusValue_Object = MibTableColumn
cdxCmtsCmStatusValue = _CdxCmtsCmStatusValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 2, 1, 1),
    _CdxCmtsCmStatusValue_Type()
)
cdxCmtsCmStatusValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxCmtsCmStatusValue.setStatus("current")
_CdxIfCmtsCmStatusOnlineTimes_Type = Counter32
_CdxIfCmtsCmStatusOnlineTimes_Object = MibTableColumn
cdxIfCmtsCmStatusOnlineTimes = _CdxIfCmtsCmStatusOnlineTimes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 2, 1, 2),
    _CdxIfCmtsCmStatusOnlineTimes_Type()
)
cdxIfCmtsCmStatusOnlineTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxIfCmtsCmStatusOnlineTimes.setStatus("current")


class _CdxIfCmtsCmStatusPercentOnline_Type(Integer32):
    """Custom type cdxIfCmtsCmStatusPercentOnline based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_CdxIfCmtsCmStatusPercentOnline_Type.__name__ = "Integer32"
_CdxIfCmtsCmStatusPercentOnline_Object = MibTableColumn
cdxIfCmtsCmStatusPercentOnline = _CdxIfCmtsCmStatusPercentOnline_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 2, 1, 3),
    _CdxIfCmtsCmStatusPercentOnline_Type()
)
cdxIfCmtsCmStatusPercentOnline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxIfCmtsCmStatusPercentOnline.setStatus("current")
_CdxIfCmtsCmStatusMinOnlineTime_Type = TimeInterval
_CdxIfCmtsCmStatusMinOnlineTime_Object = MibTableColumn
cdxIfCmtsCmStatusMinOnlineTime = _CdxIfCmtsCmStatusMinOnlineTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 2, 1, 4),
    _CdxIfCmtsCmStatusMinOnlineTime_Type()
)
cdxIfCmtsCmStatusMinOnlineTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxIfCmtsCmStatusMinOnlineTime.setStatus("current")
_CdxIfCmtsCmStatusAvgOnlineTime_Type = TimeInterval
_CdxIfCmtsCmStatusAvgOnlineTime_Object = MibTableColumn
cdxIfCmtsCmStatusAvgOnlineTime = _CdxIfCmtsCmStatusAvgOnlineTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 2, 1, 5),
    _CdxIfCmtsCmStatusAvgOnlineTime_Type()
)
cdxIfCmtsCmStatusAvgOnlineTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxIfCmtsCmStatusAvgOnlineTime.setStatus("current")
_CdxIfCmtsCmStatusMaxOnlineTime_Type = TimeInterval
_CdxIfCmtsCmStatusMaxOnlineTime_Object = MibTableColumn
cdxIfCmtsCmStatusMaxOnlineTime = _CdxIfCmtsCmStatusMaxOnlineTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 2, 1, 6),
    _CdxIfCmtsCmStatusMaxOnlineTime_Type()
)
cdxIfCmtsCmStatusMaxOnlineTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxIfCmtsCmStatusMaxOnlineTime.setStatus("current")
_CdxIfCmtsCmStatusMinOfflineTime_Type = TimeInterval
_CdxIfCmtsCmStatusMinOfflineTime_Object = MibTableColumn
cdxIfCmtsCmStatusMinOfflineTime = _CdxIfCmtsCmStatusMinOfflineTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 2, 1, 7),
    _CdxIfCmtsCmStatusMinOfflineTime_Type()
)
cdxIfCmtsCmStatusMinOfflineTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxIfCmtsCmStatusMinOfflineTime.setStatus("current")
_CdxIfCmtsCmStatusAvgOfflineTime_Type = TimeInterval
_CdxIfCmtsCmStatusAvgOfflineTime_Object = MibTableColumn
cdxIfCmtsCmStatusAvgOfflineTime = _CdxIfCmtsCmStatusAvgOfflineTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 2, 1, 8),
    _CdxIfCmtsCmStatusAvgOfflineTime_Type()
)
cdxIfCmtsCmStatusAvgOfflineTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxIfCmtsCmStatusAvgOfflineTime.setStatus("current")
_CdxIfCmtsCmStatusMaxOfflineTime_Type = TimeInterval
_CdxIfCmtsCmStatusMaxOfflineTime_Object = MibTableColumn
cdxIfCmtsCmStatusMaxOfflineTime = _CdxIfCmtsCmStatusMaxOfflineTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 2, 1, 9),
    _CdxIfCmtsCmStatusMaxOfflineTime_Type()
)
cdxIfCmtsCmStatusMaxOfflineTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxIfCmtsCmStatusMaxOfflineTime.setStatus("current")


class _CdxIfCmtsCmStatusDynSidCount_Type(Integer32):
    """Custom type cdxIfCmtsCmStatusDynSidCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_CdxIfCmtsCmStatusDynSidCount_Type.__name__ = "Integer32"
_CdxIfCmtsCmStatusDynSidCount_Object = MibTableColumn
cdxIfCmtsCmStatusDynSidCount = _CdxIfCmtsCmStatusDynSidCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 2, 1, 10),
    _CdxIfCmtsCmStatusDynSidCount_Type()
)
cdxIfCmtsCmStatusDynSidCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxIfCmtsCmStatusDynSidCount.setStatus("current")


class _CdxIfCmtsCmStatusAddlInfo_Type(Bits):
    """Custom type cdxIfCmtsCmStatusAddlInfo based on Bits"""
    namedValues = NamedValues(
        *(("noisyPlant", 0),
          ("modemPowerMaxOut", 1))
    )

_CdxIfCmtsCmStatusAddlInfo_Type.__name__ = "Bits"
_CdxIfCmtsCmStatusAddlInfo_Object = MibTableColumn
cdxIfCmtsCmStatusAddlInfo = _CdxIfCmtsCmStatusAddlInfo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 2, 1, 11),
    _CdxIfCmtsCmStatusAddlInfo_Type()
)
cdxIfCmtsCmStatusAddlInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxIfCmtsCmStatusAddlInfo.setStatus("current")
_CdxIfCmtsCmStatusOnlineTimesNum_Type = CdxResettableCounter32
_CdxIfCmtsCmStatusOnlineTimesNum_Object = MibTableColumn
cdxIfCmtsCmStatusOnlineTimesNum = _CdxIfCmtsCmStatusOnlineTimesNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 2, 1, 12),
    _CdxIfCmtsCmStatusOnlineTimesNum_Type()
)
cdxIfCmtsCmStatusOnlineTimesNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxIfCmtsCmStatusOnlineTimesNum.setStatus("current")
_CdxIfCmtsCmStatusLastResetTime_Type = TimeStamp
_CdxIfCmtsCmStatusLastResetTime_Object = MibTableColumn
cdxIfCmtsCmStatusLastResetTime = _CdxIfCmtsCmStatusLastResetTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 2, 1, 13),
    _CdxIfCmtsCmStatusLastResetTime_Type()
)
cdxIfCmtsCmStatusLastResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxIfCmtsCmStatusLastResetTime.setStatus("current")
_CdxCmtsMacExtTable_Object = MibTable
cdxCmtsMacExtTable = _CdxCmtsMacExtTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 3)
)
if mibBuilder.loadTexts:
    cdxCmtsMacExtTable.setStatus("current")
_CdxCmtsMacExtEntry_Object = MibTableRow
cdxCmtsMacExtEntry = _CdxCmtsMacExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 3, 1)
)
if mibBuilder.loadTexts:
    cdxCmtsMacExtEntry.setStatus("current")
_CdxCmtsCmOnOffTrapEnable_Type = TruthValue
_CdxCmtsCmOnOffTrapEnable_Object = MibTableColumn
cdxCmtsCmOnOffTrapEnable = _CdxCmtsCmOnOffTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 3, 1, 1),
    _CdxCmtsCmOnOffTrapEnable_Type()
)
cdxCmtsCmOnOffTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdxCmtsCmOnOffTrapEnable.setStatus("current")


class _CdxCmtsCmOnOffTrapInterval_Type(Integer32):
    """Custom type cdxCmtsCmOnOffTrapInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_CdxCmtsCmOnOffTrapInterval_Type.__name__ = "Integer32"
_CdxCmtsCmOnOffTrapInterval_Object = MibTableColumn
cdxCmtsCmOnOffTrapInterval = _CdxCmtsCmOnOffTrapInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 3, 1, 2),
    _CdxCmtsCmOnOffTrapInterval_Type()
)
cdxCmtsCmOnOffTrapInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdxCmtsCmOnOffTrapInterval.setStatus("current")
if mibBuilder.loadTexts:
    cdxCmtsCmOnOffTrapInterval.setUnits("seconds")


class _CdxCmtsCmDefaultMaxCpes_Type(Integer32):
    """Custom type cdxCmtsCmDefaultMaxCpes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_CdxCmtsCmDefaultMaxCpes_Type.__name__ = "Integer32"
_CdxCmtsCmDefaultMaxCpes_Object = MibTableColumn
cdxCmtsCmDefaultMaxCpes = _CdxCmtsCmDefaultMaxCpes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 3, 1, 3),
    _CdxCmtsCmDefaultMaxCpes_Type()
)
cdxCmtsCmDefaultMaxCpes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdxCmtsCmDefaultMaxCpes.setStatus("current")


class _CdxCmtsCmTotal_Type(Integer32):
    """Custom type cdxCmtsCmTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CdxCmtsCmTotal_Type.__name__ = "Integer32"
_CdxCmtsCmTotal_Object = MibTableColumn
cdxCmtsCmTotal = _CdxCmtsCmTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 3, 1, 4),
    _CdxCmtsCmTotal_Type()
)
cdxCmtsCmTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxCmtsCmTotal.setStatus("current")


class _CdxCmtsCmActive_Type(Integer32):
    """Custom type cdxCmtsCmActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CdxCmtsCmActive_Type.__name__ = "Integer32"
_CdxCmtsCmActive_Object = MibTableColumn
cdxCmtsCmActive = _CdxCmtsCmActive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 3, 1, 5),
    _CdxCmtsCmActive_Type()
)
cdxCmtsCmActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxCmtsCmActive.setStatus("current")


class _CdxCmtsCmRegistered_Type(Integer32):
    """Custom type cdxCmtsCmRegistered based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CdxCmtsCmRegistered_Type.__name__ = "Integer32"
_CdxCmtsCmRegistered_Object = MibTableColumn
cdxCmtsCmRegistered = _CdxCmtsCmRegistered_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 3, 1, 6),
    _CdxCmtsCmRegistered_Type()
)
cdxCmtsCmRegistered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxCmtsCmRegistered.setStatus("current")


class _CdxCmtsCmDMICMode_Type(Integer32):
    """Custom type cdxCmtsCmDMICMode based on Integer32"""
    defaultValue = 2

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
        *(("notConfigured", 1),
          ("mark", 2),
          ("lock", 3),
          ("reject", 4))
    )


_CdxCmtsCmDMICMode_Type.__name__ = "Integer32"
_CdxCmtsCmDMICMode_Object = MibTableColumn
cdxCmtsCmDMICMode = _CdxCmtsCmDMICMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 3, 1, 7),
    _CdxCmtsCmDMICMode_Type()
)
cdxCmtsCmDMICMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdxCmtsCmDMICMode.setStatus("current")


class _CdxCmtsCmDMICLockQos_Type(Integer32):
    """Custom type cdxCmtsCmDMICLockQos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16383),
    )


_CdxCmtsCmDMICLockQos_Type.__name__ = "Integer32"
_CdxCmtsCmDMICLockQos_Object = MibTableColumn
cdxCmtsCmDMICLockQos = _CdxCmtsCmDMICLockQos_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 3, 1, 8),
    _CdxCmtsCmDMICLockQos_Type()
)
cdxCmtsCmDMICLockQos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdxCmtsCmDMICLockQos.setStatus("current")


class _CdxCmtsCmChOverTimeExpiration_Type(Integer32):
    """Custom type cdxCmtsCmChOverTimeExpiration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 86400),
    )


_CdxCmtsCmChOverTimeExpiration_Type.__name__ = "Integer32"
_CdxCmtsCmChOverTimeExpiration_Object = MibScalar
cdxCmtsCmChOverTimeExpiration = _CdxCmtsCmChOverTimeExpiration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 4),
    _CdxCmtsCmChOverTimeExpiration_Type()
)
cdxCmtsCmChOverTimeExpiration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdxCmtsCmChOverTimeExpiration.setStatus("current")
if mibBuilder.loadTexts:
    cdxCmtsCmChOverTimeExpiration.setUnits("minutes")
_CdxCmtsCmChOverTable_Object = MibTable
cdxCmtsCmChOverTable = _CdxCmtsCmChOverTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 5)
)
if mibBuilder.loadTexts:
    cdxCmtsCmChOverTable.setStatus("current")
_CdxCmtsCmChOverEntry_Object = MibTableRow
cdxCmtsCmChOverEntry = _CdxCmtsCmChOverEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 5, 1)
)
cdxCmtsCmChOverEntry.setIndexNames(
    (0, "CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverSerialNumber"),
)
if mibBuilder.loadTexts:
    cdxCmtsCmChOverEntry.setStatus("current")


class _CdxCmtsCmChOverSerialNumber_Type(Integer32):
    """Custom type cdxCmtsCmChOverSerialNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CdxCmtsCmChOverSerialNumber_Type.__name__ = "Integer32"
_CdxCmtsCmChOverSerialNumber_Object = MibTableColumn
cdxCmtsCmChOverSerialNumber = _CdxCmtsCmChOverSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 5, 1, 1),
    _CdxCmtsCmChOverSerialNumber_Type()
)
cdxCmtsCmChOverSerialNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdxCmtsCmChOverSerialNumber.setStatus("current")
_CdxCmtsCmChOverMacAddress_Type = MacAddress
_CdxCmtsCmChOverMacAddress_Object = MibTableColumn
cdxCmtsCmChOverMacAddress = _CdxCmtsCmChOverMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 5, 1, 2),
    _CdxCmtsCmChOverMacAddress_Type()
)
cdxCmtsCmChOverMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdxCmtsCmChOverMacAddress.setStatus("current")


class _CdxCmtsCmChOverDownFrequency_Type(Integer32):
    """Custom type cdxCmtsCmChOverDownFrequency based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000000),
    )


_CdxCmtsCmChOverDownFrequency_Type.__name__ = "Integer32"
_CdxCmtsCmChOverDownFrequency_Object = MibTableColumn
cdxCmtsCmChOverDownFrequency = _CdxCmtsCmChOverDownFrequency_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 5, 1, 3),
    _CdxCmtsCmChOverDownFrequency_Type()
)
cdxCmtsCmChOverDownFrequency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdxCmtsCmChOverDownFrequency.setStatus("current")
if mibBuilder.loadTexts:
    cdxCmtsCmChOverDownFrequency.setUnits("hertz")


class _CdxCmtsCmChOverUpChannelId_Type(Integer32):
    """Custom type cdxCmtsCmChOverUpChannelId based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_CdxCmtsCmChOverUpChannelId_Type.__name__ = "Integer32"
_CdxCmtsCmChOverUpChannelId_Object = MibTableColumn
cdxCmtsCmChOverUpChannelId = _CdxCmtsCmChOverUpChannelId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 5, 1, 4),
    _CdxCmtsCmChOverUpChannelId_Type()
)
cdxCmtsCmChOverUpChannelId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdxCmtsCmChOverUpChannelId.setStatus("current")


class _CdxCmtsCmChOverTrapOnCompletion_Type(TruthValue):
    """Custom type cdxCmtsCmChOverTrapOnCompletion based on TruthValue"""
    defaultValue = 2


_CdxCmtsCmChOverTrapOnCompletion_Type.__name__ = "TruthValue"
_CdxCmtsCmChOverTrapOnCompletion_Object = MibTableColumn
cdxCmtsCmChOverTrapOnCompletion = _CdxCmtsCmChOverTrapOnCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 5, 1, 5),
    _CdxCmtsCmChOverTrapOnCompletion_Type()
)
cdxCmtsCmChOverTrapOnCompletion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdxCmtsCmChOverTrapOnCompletion.setStatus("current")
_CdxCmtsCmChOverOpInitiatedTime_Type = TimeStamp
_CdxCmtsCmChOverOpInitiatedTime_Object = MibTableColumn
cdxCmtsCmChOverOpInitiatedTime = _CdxCmtsCmChOverOpInitiatedTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 5, 1, 6),
    _CdxCmtsCmChOverOpInitiatedTime_Type()
)
cdxCmtsCmChOverOpInitiatedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxCmtsCmChOverOpInitiatedTime.setStatus("current")


class _CdxCmtsCmChOverState_Type(Integer32):
    """Custom type cdxCmtsCmChOverState based on Integer32"""
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
        *(("messageSent", 1),
          ("commandNotActive", 2),
          ("noOpNeeded", 3),
          ("modemNotFound", 4),
          ("waitToSendMessage", 5),
          ("timeOut", 6))
    )


_CdxCmtsCmChOverState_Type.__name__ = "Integer32"
_CdxCmtsCmChOverState_Object = MibTableColumn
cdxCmtsCmChOverState = _CdxCmtsCmChOverState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 5, 1, 7),
    _CdxCmtsCmChOverState_Type()
)
cdxCmtsCmChOverState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxCmtsCmChOverState.setStatus("current")
_CdxCmtsCmChOverRowStatus_Type = RowStatus
_CdxCmtsCmChOverRowStatus_Object = MibTableColumn
cdxCmtsCmChOverRowStatus = _CdxCmtsCmChOverRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 5, 1, 8),
    _CdxCmtsCmChOverRowStatus_Type()
)
cdxCmtsCmChOverRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdxCmtsCmChOverRowStatus.setStatus("current")
_CdxCmtsCmTable_Object = MibTable
cdxCmtsCmTable = _CdxCmtsCmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 6)
)
if mibBuilder.loadTexts:
    cdxCmtsCmTable.setStatus("current")
_CdxCmtsCmEntry_Object = MibTableRow
cdxCmtsCmEntry = _CdxCmtsCmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 6, 1)
)
cdxCmtsCmEntry.setIndexNames(
    (0, "DOCS-IF-MIB", "docsIfCmtsCmStatusIndex"),
)
if mibBuilder.loadTexts:
    cdxCmtsCmEntry.setStatus("current")


class _CdxCmtsCmMaxCpeNumber_Type(Integer32):
    """Custom type cdxCmtsCmMaxCpeNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_CdxCmtsCmMaxCpeNumber_Type.__name__ = "Integer32"
_CdxCmtsCmMaxCpeNumber_Object = MibTableColumn
cdxCmtsCmMaxCpeNumber = _CdxCmtsCmMaxCpeNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 6, 1, 1),
    _CdxCmtsCmMaxCpeNumber_Type()
)
cdxCmtsCmMaxCpeNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdxCmtsCmMaxCpeNumber.setStatus("current")


class _CdxCmtsCmCurrCpeNumber_Type(Integer32):
    """Custom type cdxCmtsCmCurrCpeNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CdxCmtsCmCurrCpeNumber_Type.__name__ = "Integer32"
_CdxCmtsCmCurrCpeNumber_Object = MibTableColumn
cdxCmtsCmCurrCpeNumber = _CdxCmtsCmCurrCpeNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 6, 1, 2),
    _CdxCmtsCmCurrCpeNumber_Type()
)
cdxCmtsCmCurrCpeNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxCmtsCmCurrCpeNumber.setStatus("current")


class _CdxCmtsCmQosProfile_Type(Integer32):
    """Custom type cdxCmtsCmQosProfile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_CdxCmtsCmQosProfile_Type.__name__ = "Integer32"
_CdxCmtsCmQosProfile_Object = MibTableColumn
cdxCmtsCmQosProfile = _CdxCmtsCmQosProfile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 6, 1, 3),
    _CdxCmtsCmQosProfile_Type()
)
cdxCmtsCmQosProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdxCmtsCmQosProfile.setStatus("current")
_CdxCmtsCmStatusDMICTable_Object = MibTable
cdxCmtsCmStatusDMICTable = _CdxCmtsCmStatusDMICTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 7)
)
if mibBuilder.loadTexts:
    cdxCmtsCmStatusDMICTable.setStatus("current")
_CdxCmtsCmStatusDMICEntry_Object = MibTableRow
cdxCmtsCmStatusDMICEntry = _CdxCmtsCmStatusDMICEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 7, 1)
)
cdxCmtsCmStatusDMICEntry.setIndexNames(
    (0, "DOCS-IF-MIB", "docsIfCmtsCmStatusIndex"),
)
if mibBuilder.loadTexts:
    cdxCmtsCmStatusDMICEntry.setStatus("current")


class _CdxCmtsCmStatusDMICMode_Type(Integer32):
    """Custom type cdxCmtsCmStatusDMICMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mark", 1),
          ("lock", 2),
          ("reject", 3))
    )


_CdxCmtsCmStatusDMICMode_Type.__name__ = "Integer32"
_CdxCmtsCmStatusDMICMode_Object = MibTableColumn
cdxCmtsCmStatusDMICMode = _CdxCmtsCmStatusDMICMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 7, 1, 1),
    _CdxCmtsCmStatusDMICMode_Type()
)
cdxCmtsCmStatusDMICMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxCmtsCmStatusDMICMode.setStatus("current")


class _CdxCmtsCmStatusDMICUnLock_Type(TruthValue):
    """Custom type cdxCmtsCmStatusDMICUnLock based on TruthValue"""
    defaultValue = 2


_CdxCmtsCmStatusDMICUnLock_Type.__name__ = "TruthValue"
_CdxCmtsCmStatusDMICUnLock_Object = MibTableColumn
cdxCmtsCmStatusDMICUnLock = _CdxCmtsCmStatusDMICUnLock_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 7, 1, 2),
    _CdxCmtsCmStatusDMICUnLock_Type()
)
cdxCmtsCmStatusDMICUnLock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdxCmtsCmStatusDMICUnLock.setStatus("current")
_CdxCmToCpeTable_Object = MibTable
cdxCmToCpeTable = _CdxCmToCpeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 8)
)
if mibBuilder.loadTexts:
    cdxCmToCpeTable.setStatus("current")
_CdxCmToCpeEntry_Object = MibTableRow
cdxCmToCpeEntry = _CdxCmToCpeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 8, 1)
)
cdxCmToCpeEntry.setIndexNames(
    (0, "CISCO-DOCS-EXT-MIB", "cdxCmToCpeCmMacAddress"),
    (0, "CISCO-DOCS-EXT-MIB", "cdxCmToCpeInetAddressType"),
    (0, "CISCO-DOCS-EXT-MIB", "cdxCmToCpeInetAddress"),
)
if mibBuilder.loadTexts:
    cdxCmToCpeEntry.setStatus("current")
_CdxCmToCpeCmMacAddress_Type = MacAddress
_CdxCmToCpeCmMacAddress_Object = MibTableColumn
cdxCmToCpeCmMacAddress = _CdxCmToCpeCmMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 8, 1, 1),
    _CdxCmToCpeCmMacAddress_Type()
)
cdxCmToCpeCmMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdxCmToCpeCmMacAddress.setStatus("current")
_CdxCmToCpeInetAddressType_Type = InetAddressType
_CdxCmToCpeInetAddressType_Object = MibTableColumn
cdxCmToCpeInetAddressType = _CdxCmToCpeInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 8, 1, 2),
    _CdxCmToCpeInetAddressType_Type()
)
cdxCmToCpeInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxCmToCpeInetAddressType.setStatus("current")
_CdxCmToCpeInetAddress_Type = InetAddress
_CdxCmToCpeInetAddress_Object = MibTableColumn
cdxCmToCpeInetAddress = _CdxCmToCpeInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 8, 1, 3),
    _CdxCmToCpeInetAddress_Type()
)
cdxCmToCpeInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxCmToCpeInetAddress.setStatus("current")
_CdxCpeToCmTable_Object = MibTable
cdxCpeToCmTable = _CdxCpeToCmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 9)
)
if mibBuilder.loadTexts:
    cdxCpeToCmTable.setStatus("current")
_CdxCpeToCmEntry_Object = MibTableRow
cdxCpeToCmEntry = _CdxCpeToCmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 9, 1)
)
cdxCpeToCmEntry.setIndexNames(
    (0, "CISCO-DOCS-EXT-MIB", "cdxCpeToCmCpeMacAddress"),
)
if mibBuilder.loadTexts:
    cdxCpeToCmEntry.setStatus("current")
_CdxCpeToCmCpeMacAddress_Type = MacAddress
_CdxCpeToCmCpeMacAddress_Object = MibTableColumn
cdxCpeToCmCpeMacAddress = _CdxCpeToCmCpeMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 9, 1, 1),
    _CdxCpeToCmCpeMacAddress_Type()
)
cdxCpeToCmCpeMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdxCpeToCmCpeMacAddress.setStatus("current")
_CdxCpeToCmMacAddress_Type = MacAddress
_CdxCpeToCmMacAddress_Object = MibTableColumn
cdxCpeToCmMacAddress = _CdxCpeToCmMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 9, 1, 2),
    _CdxCpeToCmMacAddress_Type()
)
cdxCpeToCmMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxCpeToCmMacAddress.setStatus("current")
_CdxCpeToCmInetAddressType_Type = InetAddressType
_CdxCpeToCmInetAddressType_Object = MibTableColumn
cdxCpeToCmInetAddressType = _CdxCpeToCmInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 9, 1, 3),
    _CdxCpeToCmInetAddressType_Type()
)
cdxCpeToCmInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxCpeToCmInetAddressType.setStatus("current")
_CdxCpeToCmInetAddress_Type = InetAddress
_CdxCpeToCmInetAddress_Object = MibTableColumn
cdxCpeToCmInetAddress = _CdxCpeToCmInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 9, 1, 4),
    _CdxCpeToCmInetAddress_Type()
)
cdxCpeToCmInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxCpeToCmInetAddress.setStatus("current")


class _CdxCpeToCmStatusIndex_Type(Integer32):
    """Custom type cdxCpeToCmStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CdxCpeToCmStatusIndex_Type.__name__ = "Integer32"
_CdxCpeToCmStatusIndex_Object = MibTableColumn
cdxCpeToCmStatusIndex = _CdxCpeToCmStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 9, 1, 5),
    _CdxCpeToCmStatusIndex_Type()
)
cdxCpeToCmStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxCpeToCmStatusIndex.setStatus("current")
_CdxCpeIpPrefixTable_Object = MibTable
cdxCpeIpPrefixTable = _CdxCpeIpPrefixTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 10)
)
if mibBuilder.loadTexts:
    cdxCpeIpPrefixTable.setStatus("current")
_CdxCpeIpPrefixEntry_Object = MibTableRow
cdxCpeIpPrefixEntry = _CdxCpeIpPrefixEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 10, 1)
)
cdxCpeIpPrefixEntry.setIndexNames(
    (0, "CISCO-DOCS-EXT-MIB", "cdxCpeIpPrefixCmMacAddress"),
    (0, "CISCO-DOCS-EXT-MIB", "cdxCpeIpPrefixType"),
    (0, "CISCO-DOCS-EXT-MIB", "cdxCpeIpPrefixAddress"),
    (0, "CISCO-DOCS-EXT-MIB", "cdxCpeIpPrefixLen"),
)
if mibBuilder.loadTexts:
    cdxCpeIpPrefixEntry.setStatus("current")
_CdxCpeIpPrefixCmMacAddress_Type = MacAddress
_CdxCpeIpPrefixCmMacAddress_Object = MibTableColumn
cdxCpeIpPrefixCmMacAddress = _CdxCpeIpPrefixCmMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 10, 1, 1),
    _CdxCpeIpPrefixCmMacAddress_Type()
)
cdxCpeIpPrefixCmMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdxCpeIpPrefixCmMacAddress.setStatus("current")
_CdxCpeIpPrefixType_Type = InetAddressType
_CdxCpeIpPrefixType_Object = MibTableColumn
cdxCpeIpPrefixType = _CdxCpeIpPrefixType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 10, 1, 2),
    _CdxCpeIpPrefixType_Type()
)
cdxCpeIpPrefixType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdxCpeIpPrefixType.setStatus("current")


class _CdxCpeIpPrefixAddress_Type(InetAddress):
    """Custom type cdxCpeIpPrefixAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 96),
    )


_CdxCpeIpPrefixAddress_Type.__name__ = "InetAddress"
_CdxCpeIpPrefixAddress_Object = MibTableColumn
cdxCpeIpPrefixAddress = _CdxCpeIpPrefixAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 10, 1, 3),
    _CdxCpeIpPrefixAddress_Type()
)
cdxCpeIpPrefixAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdxCpeIpPrefixAddress.setStatus("current")
_CdxCpeIpPrefixLen_Type = InetAddressPrefixLength
_CdxCpeIpPrefixLen_Object = MibTableColumn
cdxCpeIpPrefixLen = _CdxCpeIpPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 10, 1, 4),
    _CdxCpeIpPrefixLen_Type()
)
cdxCpeIpPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdxCpeIpPrefixLen.setStatus("current")
_CdxCpeIpPrefixCpeMacAddress_Type = MacAddress
_CdxCpeIpPrefixCpeMacAddress_Object = MibTableColumn
cdxCpeIpPrefixCpeMacAddress = _CdxCpeIpPrefixCpeMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 10, 1, 5),
    _CdxCpeIpPrefixCpeMacAddress_Type()
)
cdxCpeIpPrefixCpeMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxCpeIpPrefixCpeMacAddress.setStatus("current")
_CdxCpeIpPrefixCpeType_Type = SnmpAdminString
_CdxCpeIpPrefixCpeType_Object = MibTableColumn
cdxCpeIpPrefixCpeType = _CdxCpeIpPrefixCpeType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 10, 1, 6),
    _CdxCpeIpPrefixCpeType_Type()
)
cdxCpeIpPrefixCpeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxCpeIpPrefixCpeType.setStatus("current")
_CdxSpecMgmtObjects_ObjectIdentity = ObjectIdentity
cdxSpecMgmtObjects = _CdxSpecMgmtObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 4)
)
_CdxIfUpstreamChannelExtTable_Object = MibTable
cdxIfUpstreamChannelExtTable = _CdxIfUpstreamChannelExtTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cdxIfUpstreamChannelExtTable.setStatus("current")
_CdxIfUpstreamChannelExtEntry_Object = MibTableRow
cdxIfUpstreamChannelExtEntry = _CdxIfUpstreamChannelExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    cdxIfUpstreamChannelExtEntry.setStatus("current")


class _CdxIfUpChannelWidth_Type(Integer32):
    """Custom type cdxIfUpChannelWidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16000000),
    )


_CdxIfUpChannelWidth_Type.__name__ = "Integer32"
_CdxIfUpChannelWidth_Object = MibTableColumn
cdxIfUpChannelWidth = _CdxIfUpChannelWidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 4, 1, 1, 1),
    _CdxIfUpChannelWidth_Type()
)
cdxIfUpChannelWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdxIfUpChannelWidth.setStatus("current")
if mibBuilder.loadTexts:
    cdxIfUpChannelWidth.setUnits("hertz")
_CdxIfUpChannelModulationProfile_Type = Unsigned32
_CdxIfUpChannelModulationProfile_Object = MibTableColumn
cdxIfUpChannelModulationProfile = _CdxIfUpChannelModulationProfile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 4, 1, 1, 2),
    _CdxIfUpChannelModulationProfile_Type()
)
cdxIfUpChannelModulationProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdxIfUpChannelModulationProfile.setStatus("current")


class _CdxIfUpChannelCmTotal_Type(Integer32):
    """Custom type cdxIfUpChannelCmTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
    )


_CdxIfUpChannelCmTotal_Type.__name__ = "Integer32"
_CdxIfUpChannelCmTotal_Object = MibTableColumn
cdxIfUpChannelCmTotal = _CdxIfUpChannelCmTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 4, 1, 1, 3),
    _CdxIfUpChannelCmTotal_Type()
)
cdxIfUpChannelCmTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxIfUpChannelCmTotal.setStatus("current")


class _CdxIfUpChannelCmActive_Type(Integer32):
    """Custom type cdxIfUpChannelCmActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
    )


_CdxIfUpChannelCmActive_Type.__name__ = "Integer32"
_CdxIfUpChannelCmActive_Object = MibTableColumn
cdxIfUpChannelCmActive = _CdxIfUpChannelCmActive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 4, 1, 1, 4),
    _CdxIfUpChannelCmActive_Type()
)
cdxIfUpChannelCmActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxIfUpChannelCmActive.setStatus("current")


class _CdxIfUpChannelCmRegistered_Type(Integer32):
    """Custom type cdxIfUpChannelCmRegistered based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
    )


_CdxIfUpChannelCmRegistered_Type.__name__ = "Integer32"
_CdxIfUpChannelCmRegistered_Object = MibTableColumn
cdxIfUpChannelCmRegistered = _CdxIfUpChannelCmRegistered_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 4, 1, 1, 5),
    _CdxIfUpChannelCmRegistered_Type()
)
cdxIfUpChannelCmRegistered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxIfUpChannelCmRegistered.setStatus("current")


class _CdxIfUpChannelInputPowerLevel_Type(TenthdBmV):
    """Custom type cdxIfUpChannelInputPowerLevel based on TenthdBmV"""
    subtypeSpec = TenthdBmV.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 250),
    )


_CdxIfUpChannelInputPowerLevel_Type.__name__ = "TenthdBmV"
_CdxIfUpChannelInputPowerLevel_Object = MibTableColumn
cdxIfUpChannelInputPowerLevel = _CdxIfUpChannelInputPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 4, 1, 1, 6),
    _CdxIfUpChannelInputPowerLevel_Type()
)
cdxIfUpChannelInputPowerLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdxIfUpChannelInputPowerLevel.setStatus("current")


class _CdxIfUpChannelAvgUtil_Type(Integer32):
    """Custom type cdxIfUpChannelAvgUtil based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CdxIfUpChannelAvgUtil_Type.__name__ = "Integer32"
_CdxIfUpChannelAvgUtil_Object = MibTableColumn
cdxIfUpChannelAvgUtil = _CdxIfUpChannelAvgUtil_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 4, 1, 1, 7),
    _CdxIfUpChannelAvgUtil_Type()
)
cdxIfUpChannelAvgUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxIfUpChannelAvgUtil.setStatus("current")
if mibBuilder.loadTexts:
    cdxIfUpChannelAvgUtil.setUnits("percent")


class _CdxIfUpChannelAvgContSlots_Type(Integer32):
    """Custom type cdxIfUpChannelAvgContSlots based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CdxIfUpChannelAvgContSlots_Type.__name__ = "Integer32"
_CdxIfUpChannelAvgContSlots_Object = MibTableColumn
cdxIfUpChannelAvgContSlots = _CdxIfUpChannelAvgContSlots_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 4, 1, 1, 8),
    _CdxIfUpChannelAvgContSlots_Type()
)
cdxIfUpChannelAvgContSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxIfUpChannelAvgContSlots.setStatus("current")
if mibBuilder.loadTexts:
    cdxIfUpChannelAvgContSlots.setUnits("percent")


class _CdxIfUpChannelRangeSlots_Type(Integer32):
    """Custom type cdxIfUpChannelRangeSlots based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CdxIfUpChannelRangeSlots_Type.__name__ = "Integer32"
_CdxIfUpChannelRangeSlots_Object = MibTableColumn
cdxIfUpChannelRangeSlots = _CdxIfUpChannelRangeSlots_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 4, 1, 1, 9),
    _CdxIfUpChannelRangeSlots_Type()
)
cdxIfUpChannelRangeSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxIfUpChannelRangeSlots.setStatus("current")
if mibBuilder.loadTexts:
    cdxIfUpChannelRangeSlots.setUnits("percent")
_CdxIfUpChannelNumActiveUGS_Type = Unsigned32
_CdxIfUpChannelNumActiveUGS_Object = MibTableColumn
cdxIfUpChannelNumActiveUGS = _CdxIfUpChannelNumActiveUGS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 4, 1, 1, 10),
    _CdxIfUpChannelNumActiveUGS_Type()
)
cdxIfUpChannelNumActiveUGS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxIfUpChannelNumActiveUGS.setStatus("current")
_CdxIfUpChannelMaxUGSLastOneHour_Type = Unsigned32
_CdxIfUpChannelMaxUGSLastOneHour_Object = MibTableColumn
cdxIfUpChannelMaxUGSLastOneHour = _CdxIfUpChannelMaxUGSLastOneHour_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 4, 1, 1, 11),
    _CdxIfUpChannelMaxUGSLastOneHour_Type()
)
cdxIfUpChannelMaxUGSLastOneHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxIfUpChannelMaxUGSLastOneHour.setStatus("current")
_CdxIfUpChannelMinUGSLastOneHour_Type = Unsigned32
_CdxIfUpChannelMinUGSLastOneHour_Object = MibTableColumn
cdxIfUpChannelMinUGSLastOneHour = _CdxIfUpChannelMinUGSLastOneHour_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 4, 1, 1, 12),
    _CdxIfUpChannelMinUGSLastOneHour_Type()
)
cdxIfUpChannelMinUGSLastOneHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxIfUpChannelMinUGSLastOneHour.setStatus("current")
_CdxIfUpChannelAvgUGSLastOneHour_Type = Unsigned32
_CdxIfUpChannelAvgUGSLastOneHour_Object = MibTableColumn
cdxIfUpChannelAvgUGSLastOneHour = _CdxIfUpChannelAvgUGSLastOneHour_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 4, 1, 1, 13),
    _CdxIfUpChannelAvgUGSLastOneHour_Type()
)
cdxIfUpChannelAvgUGSLastOneHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxIfUpChannelAvgUGSLastOneHour.setStatus("current")
_CdxIfUpChannelMaxUGSLastFiveMins_Type = Unsigned32
_CdxIfUpChannelMaxUGSLastFiveMins_Object = MibTableColumn
cdxIfUpChannelMaxUGSLastFiveMins = _CdxIfUpChannelMaxUGSLastFiveMins_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 4, 1, 1, 14),
    _CdxIfUpChannelMaxUGSLastFiveMins_Type()
)
cdxIfUpChannelMaxUGSLastFiveMins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxIfUpChannelMaxUGSLastFiveMins.setStatus("current")
_CdxIfUpChannelMinUGSLastFiveMins_Type = Unsigned32
_CdxIfUpChannelMinUGSLastFiveMins_Object = MibTableColumn
cdxIfUpChannelMinUGSLastFiveMins = _CdxIfUpChannelMinUGSLastFiveMins_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 4, 1, 1, 15),
    _CdxIfUpChannelMinUGSLastFiveMins_Type()
)
cdxIfUpChannelMinUGSLastFiveMins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxIfUpChannelMinUGSLastFiveMins.setStatus("current")
_CdxIfUpChannelAvgUGSLastFiveMins_Type = Unsigned32
_CdxIfUpChannelAvgUGSLastFiveMins_Object = MibTableColumn
cdxIfUpChannelAvgUGSLastFiveMins = _CdxIfUpChannelAvgUGSLastFiveMins_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 4, 1, 1, 16),
    _CdxIfUpChannelAvgUGSLastFiveMins_Type()
)
cdxIfUpChannelAvgUGSLastFiveMins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxIfUpChannelAvgUGSLastFiveMins.setStatus("current")
_CdxWBResilObjects_ObjectIdentity = ObjectIdentity
cdxWBResilObjects = _CdxWBResilObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 5)
)


class _CdxWBResilRFChangeDampenTime_Type(Integer32):
    """Custom type cdxWBResilRFChangeDampenTime based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CdxWBResilRFChangeDampenTime_Type.__name__ = "Integer32"
_CdxWBResilRFChangeDampenTime_Object = MibScalar
cdxWBResilRFChangeDampenTime = _CdxWBResilRFChangeDampenTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 5, 1),
    _CdxWBResilRFChangeDampenTime_Type()
)
cdxWBResilRFChangeDampenTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdxWBResilRFChangeDampenTime.setStatus("current")
if mibBuilder.loadTexts:
    cdxWBResilRFChangeDampenTime.setUnits("Second")


class _CdxWBResilRFChangeTriggerPercentage_Type(Integer32):
    """Custom type cdxWBResilRFChangeTriggerPercentage based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CdxWBResilRFChangeTriggerPercentage_Type.__name__ = "Integer32"
_CdxWBResilRFChangeTriggerPercentage_Object = MibScalar
cdxWBResilRFChangeTriggerPercentage = _CdxWBResilRFChangeTriggerPercentage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 5, 2),
    _CdxWBResilRFChangeTriggerPercentage_Type()
)
cdxWBResilRFChangeTriggerPercentage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdxWBResilRFChangeTriggerPercentage.setStatus("current")
if mibBuilder.loadTexts:
    cdxWBResilRFChangeTriggerPercentage.setUnits("Percentage")


class _CdxWBResilRFChangeTriggerCount_Type(Integer32):
    """Custom type cdxWBResilRFChangeTriggerCount based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CdxWBResilRFChangeTriggerCount_Type.__name__ = "Integer32"
_CdxWBResilRFChangeTriggerCount_Object = MibScalar
cdxWBResilRFChangeTriggerCount = _CdxWBResilRFChangeTriggerCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 5, 3),
    _CdxWBResilRFChangeTriggerCount_Type()
)
cdxWBResilRFChangeTriggerCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdxWBResilRFChangeTriggerCount.setStatus("current")


class _CdxWBResilRFChangeTriggerMoveSecondary_Type(TruthValue):
    """Custom type cdxWBResilRFChangeTriggerMoveSecondary based on TruthValue"""
    defaultValue = 2


_CdxWBResilRFChangeTriggerMoveSecondary_Type.__name__ = "TruthValue"
_CdxWBResilRFChangeTriggerMoveSecondary_Object = MibScalar
cdxWBResilRFChangeTriggerMoveSecondary = _CdxWBResilRFChangeTriggerMoveSecondary_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 5, 4),
    _CdxWBResilRFChangeTriggerMoveSecondary_Type()
)
cdxWBResilRFChangeTriggerMoveSecondary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdxWBResilRFChangeTriggerMoveSecondary.setStatus("current")


class _CdxWBResilNotificationEnable_Type(Bits):
    """Custom type cdxWBResilNotificationEnable based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("event", 0),
          ("cm-recover", 1),
          ("cm-pmode", 2),
          ("rf-up", 3),
          ("rf-down", 4),
          ("us-resil-recover", 5),
          ("us-resil-pmode", 6))
    )

_CdxWBResilNotificationEnable_Type.__name__ = "Bits"
_CdxWBResilNotificationEnable_Object = MibScalar
cdxWBResilNotificationEnable = _CdxWBResilNotificationEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 5, 5),
    _CdxWBResilNotificationEnable_Type()
)
cdxWBResilNotificationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdxWBResilNotificationEnable.setStatus("current")


class _CdxWBResilNotificationsInterval_Type(Integer32):
    """Custom type cdxWBResilNotificationsInterval based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_CdxWBResilNotificationsInterval_Type.__name__ = "Integer32"
_CdxWBResilNotificationsInterval_Object = MibScalar
cdxWBResilNotificationsInterval = _CdxWBResilNotificationsInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 5, 6),
    _CdxWBResilNotificationsInterval_Type()
)
cdxWBResilNotificationsInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdxWBResilNotificationsInterval.setStatus("current")
if mibBuilder.loadTexts:
    cdxWBResilNotificationsInterval.setUnits("Second")


class _CdxWBResilEventLevel_Type(Integer32):
    """Custom type cdxWBResilEventLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("info", 1),
          ("warning", 2),
          ("error", 3))
    )


_CdxWBResilEventLevel_Type.__name__ = "Integer32"
_CdxWBResilEventLevel_Object = MibScalar
cdxWBResilEventLevel = _CdxWBResilEventLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 5, 7),
    _CdxWBResilEventLevel_Type()
)
cdxWBResilEventLevel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cdxWBResilEventLevel.setStatus("current")


class _CdxWBResilEventType_Type(Integer32):
    """Custom type cdxWBResilEventType based on Integer32"""
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
        *(("cmEventMddTimeout", 1),
          ("cmEventQamFecFailure", 2),
          ("cmEventMddRecovery", 3),
          ("cmEventQamFecRecovery", 4))
    )


_CdxWBResilEventType_Type.__name__ = "Integer32"
_CdxWBResilEventType_Object = MibScalar
cdxWBResilEventType = _CdxWBResilEventType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 5, 8),
    _CdxWBResilEventType_Type()
)
cdxWBResilEventType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cdxWBResilEventType.setStatus("current")
_CdxWBResilUpdateTime_Type = DateAndTime
_CdxWBResilUpdateTime_Object = MibScalar
cdxWBResilUpdateTime = _CdxWBResilUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 5, 9),
    _CdxWBResilUpdateTime_Type()
)
cdxWBResilUpdateTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cdxWBResilUpdateTime.setStatus("current")
_CdxWBResilEventTotalCount_Type = Counter32
_CdxWBResilEventTotalCount_Object = MibScalar
cdxWBResilEventTotalCount = _CdxWBResilEventTotalCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 5, 10),
    _CdxWBResilEventTotalCount_Type()
)
cdxWBResilEventTotalCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cdxWBResilEventTotalCount.setStatus("current")
_CdxWBResilEventTotalDupCount_Type = Counter32
_CdxWBResilEventTotalDupCount_Object = MibScalar
cdxWBResilEventTotalDupCount = _CdxWBResilEventTotalDupCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 5, 11),
    _CdxWBResilEventTotalDupCount_Type()
)
cdxWBResilEventTotalDupCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cdxWBResilEventTotalDupCount.setStatus("current")


class _CdxUsResilEventType_Type(Integer32):
    """Custom type cdxUsResilEventType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("ranging", 2),
          ("dataBurst", 3))
    )


_CdxUsResilEventType_Type.__name__ = "Integer32"
_CdxUsResilEventType_Object = MibScalar
cdxUsResilEventType = _CdxUsResilEventType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 5, 12),
    _CdxUsResilEventType_Type()
)
cdxUsResilEventType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cdxUsResilEventType.setStatus("current")
_CdxWBResilCmTable_Object = MibTable
cdxWBResilCmTable = _CdxWBResilCmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 5, 13)
)
if mibBuilder.loadTexts:
    cdxWBResilCmTable.setStatus("current")
_CdxWBResilCmEntry_Object = MibTableRow
cdxWBResilCmEntry = _CdxWBResilCmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 5, 13, 1)
)
cdxWBResilCmEntry.setIndexNames(
    (0, "CISCO-DOCS-EXT-MIB", "cdxWBResilCmIndex"),
)
if mibBuilder.loadTexts:
    cdxWBResilCmEntry.setStatus("current")


class _CdxWBResilCmIndex_Type(Unsigned32):
    """Custom type cdxWBResilCmIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CdxWBResilCmIndex_Type.__name__ = "Unsigned32"
_CdxWBResilCmIndex_Object = MibTableColumn
cdxWBResilCmIndex = _CdxWBResilCmIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 5, 13, 1, 1),
    _CdxWBResilCmIndex_Type()
)
cdxWBResilCmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdxWBResilCmIndex.setStatus("current")
_CdxWBResilCmMacAddr_Type = MacAddress
_CdxWBResilCmMacAddr_Object = MibTableColumn
cdxWBResilCmMacAddr = _CdxWBResilCmMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 5, 13, 1, 2),
    _CdxWBResilCmMacAddr_Type()
)
cdxWBResilCmMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxWBResilCmMacAddr.setStatus("current")
_CdxWBResilCmTotalDsNum_Type = Unsigned32
_CdxWBResilCmTotalDsNum_Object = MibTableColumn
cdxWBResilCmTotalDsNum = _CdxWBResilCmTotalDsNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 5, 13, 1, 3),
    _CdxWBResilCmTotalDsNum_Type()
)
cdxWBResilCmTotalDsNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxWBResilCmTotalDsNum.setStatus("current")
_CdxWBResilCmTotalUsNum_Type = Unsigned32
_CdxWBResilCmTotalUsNum_Object = MibTableColumn
cdxWBResilCmTotalUsNum = _CdxWBResilCmTotalUsNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 5, 13, 1, 4),
    _CdxWBResilCmTotalUsNum_Type()
)
cdxWBResilCmTotalUsNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxWBResilCmTotalUsNum.setStatus("current")
_CdxWBResilCmCurrentDsNum_Type = Unsigned32
_CdxWBResilCmCurrentDsNum_Object = MibTableColumn
cdxWBResilCmCurrentDsNum = _CdxWBResilCmCurrentDsNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 5, 13, 1, 5),
    _CdxWBResilCmCurrentDsNum_Type()
)
cdxWBResilCmCurrentDsNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxWBResilCmCurrentDsNum.setStatus("current")
_CdxWBResilCmCurrentUsNum_Type = Unsigned32
_CdxWBResilCmCurrentUsNum_Object = MibTableColumn
cdxWBResilCmCurrentUsNum = _CdxWBResilCmCurrentUsNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 5, 13, 1, 6),
    _CdxWBResilCmCurrentUsNum_Type()
)
cdxWBResilCmCurrentUsNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxWBResilCmCurrentUsNum.setStatus("current")


class _CdxWBResilCmImpairedDsChIndex_Type(SnmpTagList):
    """Custom type cdxWBResilCmImpairedDsChIndex based on SnmpTagList"""
    defaultValue = OctetString("")


_CdxWBResilCmImpairedDsChIndex_Type.__name__ = "SnmpTagList"
_CdxWBResilCmImpairedDsChIndex_Object = MibTableColumn
cdxWBResilCmImpairedDsChIndex = _CdxWBResilCmImpairedDsChIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 5, 13, 1, 7),
    _CdxWBResilCmImpairedDsChIndex_Type()
)
cdxWBResilCmImpairedDsChIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxWBResilCmImpairedDsChIndex.setStatus("current")


class _CdxWBResilCmImpairedUsChIndex_Type(SnmpTagList):
    """Custom type cdxWBResilCmImpairedUsChIndex based on SnmpTagList"""
    defaultValue = OctetString("")


_CdxWBResilCmImpairedUsChIndex_Type.__name__ = "SnmpTagList"
_CdxWBResilCmImpairedUsChIndex_Object = MibTableColumn
cdxWBResilCmImpairedUsChIndex = _CdxWBResilCmImpairedUsChIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 5, 13, 1, 8),
    _CdxWBResilCmImpairedUsChIndex_Type()
)
cdxWBResilCmImpairedUsChIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxWBResilCmImpairedUsChIndex.setStatus("current")
_CdxDownstreamObjects_ObjectIdentity = ObjectIdentity
cdxDownstreamObjects = _CdxDownstreamObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 6)
)
_CdxRFtoPrimaryChannelMappingTable_Object = MibTable
cdxRFtoPrimaryChannelMappingTable = _CdxRFtoPrimaryChannelMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 6, 1)
)
if mibBuilder.loadTexts:
    cdxRFtoPrimaryChannelMappingTable.setStatus("current")
_CdxRFtoPrimaryChannelMappingEntry_Object = MibTableRow
cdxRFtoPrimaryChannelMappingEntry = _CdxRFtoPrimaryChannelMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 6, 1, 1)
)
cdxRFtoPrimaryChannelMappingEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cdxRFtoPrimaryChannelMappingEntry.setStatus("current")
_CdxPrimaryChannelIfIndex_Type = InterfaceIndex
_CdxPrimaryChannelIfIndex_Object = MibTableColumn
cdxPrimaryChannelIfIndex = _CdxPrimaryChannelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 6, 1, 1, 1),
    _CdxPrimaryChannelIfIndex_Type()
)
cdxPrimaryChannelIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxPrimaryChannelIfIndex.setStatus("current")
_CdxPrimaryChanneltoRFMappingTable_Object = MibTable
cdxPrimaryChanneltoRFMappingTable = _CdxPrimaryChanneltoRFMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 6, 2)
)
if mibBuilder.loadTexts:
    cdxPrimaryChanneltoRFMappingTable.setStatus("current")
_CdxPrimaryChanneltoRFMappingEntry_Object = MibTableRow
cdxPrimaryChanneltoRFMappingEntry = _CdxPrimaryChanneltoRFMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 6, 2, 1)
)
cdxPrimaryChanneltoRFMappingEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cdxPrimaryChanneltoRFMappingEntry.setStatus("current")
_CdxPhysicalRFIfIndex_Type = InterfaceIndex
_CdxPhysicalRFIfIndex_Object = MibTableColumn
cdxPhysicalRFIfIndex = _CdxPhysicalRFIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 6, 2, 1, 1),
    _CdxPhysicalRFIfIndex_Type()
)
cdxPhysicalRFIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxPhysicalRFIfIndex.setStatus("current")
_CdxCmtsMtcCmSfObjects_ObjectIdentity = ObjectIdentity
cdxCmtsMtcCmSfObjects = _CdxCmtsMtcCmSfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 7)
)
_CdxCmtsMtcCmTable_Object = MibTable
cdxCmtsMtcCmTable = _CdxCmtsMtcCmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 7, 1)
)
if mibBuilder.loadTexts:
    cdxCmtsMtcCmTable.setStatus("current")
_CdxCmtsMtcCmEntry_Object = MibTableRow
cdxCmtsMtcCmEntry = _CdxCmtsMtcCmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 7, 1, 1)
)
cdxCmtsMtcCmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-DOCS-EXT-MIB", "cdxCmtsMtcTcsId"),
)
if mibBuilder.loadTexts:
    cdxCmtsMtcCmEntry.setStatus("current")
_CdxCmtsMtcTcsId_Type = ChSetId
_CdxCmtsMtcTcsId_Object = MibTableColumn
cdxCmtsMtcTcsId = _CdxCmtsMtcTcsId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 7, 1, 1, 1),
    _CdxCmtsMtcTcsId_Type()
)
cdxCmtsMtcTcsId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdxCmtsMtcTcsId.setStatus("current")
_CdxCmtsMtcCmTotal_Type = Unsigned32
_CdxCmtsMtcCmTotal_Object = MibTableColumn
cdxCmtsMtcCmTotal = _CdxCmtsMtcCmTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 7, 1, 1, 2),
    _CdxCmtsMtcCmTotal_Type()
)
cdxCmtsMtcCmTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxCmtsMtcCmTotal.setStatus("current")
_CdxCMtsMtcCmOperational_Type = Unsigned32
_CdxCMtsMtcCmOperational_Object = MibTableColumn
cdxCMtsMtcCmOperational = _CdxCMtsMtcCmOperational_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 7, 1, 1, 3),
    _CdxCMtsMtcCmOperational_Type()
)
cdxCMtsMtcCmOperational.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxCMtsMtcCmOperational.setStatus("current")
_CdxCmtsMtcCmRegistered_Type = Unsigned32
_CdxCmtsMtcCmRegistered_Object = MibTableColumn
cdxCmtsMtcCmRegistered = _CdxCmtsMtcCmRegistered_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 7, 1, 1, 4),
    _CdxCmtsMtcCmRegistered_Type()
)
cdxCmtsMtcCmRegistered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxCmtsMtcCmRegistered.setStatus("current")
_CdxCmtsMtcCmUnregistered_Type = Unsigned32
_CdxCmtsMtcCmUnregistered_Object = MibTableColumn
cdxCmtsMtcCmUnregistered = _CdxCmtsMtcCmUnregistered_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 7, 1, 1, 5),
    _CdxCmtsMtcCmUnregistered_Type()
)
cdxCmtsMtcCmUnregistered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxCmtsMtcCmUnregistered.setStatus("current")
_CdxCmtsMtcCmOffline_Type = Unsigned32
_CdxCmtsMtcCmOffline_Object = MibTableColumn
cdxCmtsMtcCmOffline = _CdxCmtsMtcCmOffline_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 7, 1, 1, 6),
    _CdxCmtsMtcCmOffline_Type()
)
cdxCmtsMtcCmOffline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxCmtsMtcCmOffline.setStatus("current")
_CdxCmtsMtcCmWideband_Type = Unsigned32
_CdxCmtsMtcCmWideband_Object = MibTableColumn
cdxCmtsMtcCmWideband = _CdxCmtsMtcCmWideband_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 7, 1, 1, 7),
    _CdxCmtsMtcCmWideband_Type()
)
cdxCmtsMtcCmWideband.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxCmtsMtcCmWideband.setStatus("current")
_CdxCmtsMtcUpstreamBondGrp_Type = CdxUpstreamBondGrpList
_CdxCmtsMtcUpstreamBondGrp_Object = MibTableColumn
cdxCmtsMtcUpstreamBondGrp = _CdxCmtsMtcUpstreamBondGrp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 7, 1, 1, 8),
    _CdxCmtsMtcUpstreamBondGrp_Type()
)
cdxCmtsMtcUpstreamBondGrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxCmtsMtcUpstreamBondGrp.setStatus("current")
_CdxCmtsUscbSflowTable_Object = MibTable
cdxCmtsUscbSflowTable = _CdxCmtsUscbSflowTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 7, 2)
)
if mibBuilder.loadTexts:
    cdxCmtsUscbSflowTable.setStatus("current")
_CdxCmtsUscbSflowEntry_Object = MibTableRow
cdxCmtsUscbSflowEntry = _CdxCmtsUscbSflowEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 7, 2, 1)
)
cdxCmtsUscbSflowEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-DOCS-EXT-MIB", "cdxCmtsUsBondingGrpId"),
)
if mibBuilder.loadTexts:
    cdxCmtsUscbSflowEntry.setStatus("current")


class _CdxCmtsUsBondingGrpId_Type(Unsigned32):
    """Custom type cdxCmtsUsBondingGrpId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CdxCmtsUsBondingGrpId_Type.__name__ = "Unsigned32"
_CdxCmtsUsBondingGrpId_Object = MibTableColumn
cdxCmtsUsBondingGrpId = _CdxCmtsUsBondingGrpId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 7, 2, 1, 1),
    _CdxCmtsUsBondingGrpId_Type()
)
cdxCmtsUsBondingGrpId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdxCmtsUsBondingGrpId.setStatus("current")
_CdxCmtsUscbSfTotal_Type = Unsigned32
_CdxCmtsUscbSfTotal_Object = MibTableColumn
cdxCmtsUscbSfTotal = _CdxCmtsUscbSfTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 7, 2, 1, 2),
    _CdxCmtsUscbSfTotal_Type()
)
cdxCmtsUscbSfTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxCmtsUscbSfTotal.setStatus("current")
_CdxCmtsUscbSfPri_Type = Unsigned32
_CdxCmtsUscbSfPri_Object = MibTableColumn
cdxCmtsUscbSfPri = _CdxCmtsUscbSfPri_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 7, 2, 1, 3),
    _CdxCmtsUscbSfPri_Type()
)
cdxCmtsUscbSfPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxCmtsUscbSfPri.setStatus("current")
_CdxCmtsUscbStaticSfBe_Type = Unsigned32
_CdxCmtsUscbStaticSfBe_Object = MibTableColumn
cdxCmtsUscbStaticSfBe = _CdxCmtsUscbStaticSfBe_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 7, 2, 1, 4),
    _CdxCmtsUscbStaticSfBe_Type()
)
cdxCmtsUscbStaticSfBe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxCmtsUscbStaticSfBe.setStatus("current")
_CdxCmtsUscbStaticSfUgs_Type = Unsigned32
_CdxCmtsUscbStaticSfUgs_Object = MibTableColumn
cdxCmtsUscbStaticSfUgs = _CdxCmtsUscbStaticSfUgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 7, 2, 1, 5),
    _CdxCmtsUscbStaticSfUgs_Type()
)
cdxCmtsUscbStaticSfUgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxCmtsUscbStaticSfUgs.setStatus("current")
_CdxCmtsUscbStaticSfUgsad_Type = Unsigned32
_CdxCmtsUscbStaticSfUgsad_Object = MibTableColumn
cdxCmtsUscbStaticSfUgsad = _CdxCmtsUscbStaticSfUgsad_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 7, 2, 1, 6),
    _CdxCmtsUscbStaticSfUgsad_Type()
)
cdxCmtsUscbStaticSfUgsad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxCmtsUscbStaticSfUgsad.setStatus("current")
_CdxCmtsUscbStaticSfRtps_Type = Unsigned32
_CdxCmtsUscbStaticSfRtps_Object = MibTableColumn
cdxCmtsUscbStaticSfRtps = _CdxCmtsUscbStaticSfRtps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 7, 2, 1, 7),
    _CdxCmtsUscbStaticSfRtps_Type()
)
cdxCmtsUscbStaticSfRtps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxCmtsUscbStaticSfRtps.setStatus("current")
_CdxCmtsUscbStaticSfNrtps_Type = Unsigned32
_CdxCmtsUscbStaticSfNrtps_Object = MibTableColumn
cdxCmtsUscbStaticSfNrtps = _CdxCmtsUscbStaticSfNrtps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 7, 2, 1, 8),
    _CdxCmtsUscbStaticSfNrtps_Type()
)
cdxCmtsUscbStaticSfNrtps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxCmtsUscbStaticSfNrtps.setStatus("current")
_CdxCmtsUscbDynSfBe_Type = Unsigned32
_CdxCmtsUscbDynSfBe_Object = MibTableColumn
cdxCmtsUscbDynSfBe = _CdxCmtsUscbDynSfBe_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 7, 2, 1, 9),
    _CdxCmtsUscbDynSfBe_Type()
)
cdxCmtsUscbDynSfBe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxCmtsUscbDynSfBe.setStatus("current")
_CdxCmtsUscbDynSfUgs_Type = Unsigned32
_CdxCmtsUscbDynSfUgs_Object = MibTableColumn
cdxCmtsUscbDynSfUgs = _CdxCmtsUscbDynSfUgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 7, 2, 1, 10),
    _CdxCmtsUscbDynSfUgs_Type()
)
cdxCmtsUscbDynSfUgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxCmtsUscbDynSfUgs.setStatus("current")
_CdxCmtsUscbDynSfUgsad_Type = Unsigned32
_CdxCmtsUscbDynSfUgsad_Object = MibTableColumn
cdxCmtsUscbDynSfUgsad = _CdxCmtsUscbDynSfUgsad_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 7, 2, 1, 11),
    _CdxCmtsUscbDynSfUgsad_Type()
)
cdxCmtsUscbDynSfUgsad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxCmtsUscbDynSfUgsad.setStatus("current")
_CdxCmtsUscbDynSfRtps_Type = Unsigned32
_CdxCmtsUscbDynSfRtps_Object = MibTableColumn
cdxCmtsUscbDynSfRtps = _CdxCmtsUscbDynSfRtps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 7, 2, 1, 12),
    _CdxCmtsUscbDynSfRtps_Type()
)
cdxCmtsUscbDynSfRtps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxCmtsUscbDynSfRtps.setStatus("current")
_CdxCmtsUscbDynSfNrtps_Type = Unsigned32
_CdxCmtsUscbDynSfNrtps_Object = MibTableColumn
cdxCmtsUscbDynSfNrtps = _CdxCmtsUscbDynSfNrtps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 7, 2, 1, 13),
    _CdxCmtsUscbDynSfNrtps_Type()
)
cdxCmtsUscbDynSfNrtps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxCmtsUscbDynSfNrtps.setStatus("current")
_CdxCmtsUscbDescr_Type = SnmpAdminString
_CdxCmtsUscbDescr_Object = MibTableColumn
cdxCmtsUscbDescr = _CdxCmtsUscbDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 7, 2, 1, 14),
    _CdxCmtsUscbDescr_Type()
)
cdxCmtsUscbDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdxCmtsUscbDescr.setStatus("current")
_CdxCmtsDocsisLBObjects_ObjectIdentity = ObjectIdentity
cdxCmtsDocsisLBObjects = _CdxCmtsDocsisLBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 8)
)


class _CdxCmtsDocsisLBEnable_Type(Integer32):
    """Custom type cdxCmtsDocsisLBEnable based on Integer32"""
    defaultValue = 2

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


_CdxCmtsDocsisLBEnable_Type.__name__ = "Integer32"
_CdxCmtsDocsisLBEnable_Object = MibScalar
cdxCmtsDocsisLBEnable = _CdxCmtsDocsisLBEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 8, 1),
    _CdxCmtsDocsisLBEnable_Type()
)
cdxCmtsDocsisLBEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdxCmtsDocsisLBEnable.setStatus("current")


class _CdxCmtsD30LBEnable_Type(Integer32):
    """Custom type cdxCmtsD30LBEnable based on Integer32"""
    defaultValue = 2

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


_CdxCmtsD30LBEnable_Type.__name__ = "Integer32"
_CdxCmtsD30LBEnable_Object = MibScalar
cdxCmtsD30LBEnable = _CdxCmtsD30LBEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 8, 2),
    _CdxCmtsD30LBEnable_Type()
)
cdxCmtsD30LBEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdxCmtsD30LBEnable.setStatus("current")


class _CdxCmtsD30LBUpstreamEnable_Type(Integer32):
    """Custom type cdxCmtsD30LBUpstreamEnable based on Integer32"""
    defaultValue = 2

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


_CdxCmtsD30LBUpstreamEnable_Type.__name__ = "Integer32"
_CdxCmtsD30LBUpstreamEnable_Object = MibScalar
cdxCmtsD30LBUpstreamEnable = _CdxCmtsD30LBUpstreamEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 8, 3),
    _CdxCmtsD30LBUpstreamEnable_Type()
)
cdxCmtsD30LBUpstreamEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdxCmtsD30LBUpstreamEnable.setStatus("current")


class _CdxCmtsD30LBStaticEnable_Type(Integer32):
    """Custom type cdxCmtsD30LBStaticEnable based on Integer32"""
    defaultValue = 2

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


_CdxCmtsD30LBStaticEnable_Type.__name__ = "Integer32"
_CdxCmtsD30LBStaticEnable_Object = MibScalar
cdxCmtsD30LBStaticEnable = _CdxCmtsD30LBStaticEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 8, 4),
    _CdxCmtsD30LBStaticEnable_Type()
)
cdxCmtsD30LBStaticEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdxCmtsD30LBStaticEnable.setStatus("current")


class _CdxCmtsD30LBDynEnable_Type(Integer32):
    """Custom type cdxCmtsD30LBDynEnable based on Integer32"""
    defaultValue = 2

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


_CdxCmtsD30LBDynEnable_Type.__name__ = "Integer32"
_CdxCmtsD30LBDynEnable_Object = MibScalar
cdxCmtsD30LBDynEnable = _CdxCmtsD30LBDynEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 8, 5),
    _CdxCmtsD30LBDynEnable_Type()
)
cdxCmtsD30LBDynEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdxCmtsD30LBDynEnable.setStatus("current")
_CdxRPDGS7KObjects_ObjectIdentity = ObjectIdentity
cdxRPDGS7KObjects = _CdxRPDGS7KObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 9)
)
_CdxRPDGS7KTable_Object = MibTable
cdxRPDGS7KTable = _CdxRPDGS7KTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 9, 1)
)
if mibBuilder.loadTexts:
    cdxRPDGS7KTable.setStatus("current")
_CdxRPDGS7KEntry_Object = MibTableRow
cdxRPDGS7KEntry = _CdxRPDGS7KEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 9, 1, 1)
)
cdxRPDGS7KEntry.setIndexNames(
    (0, "CISCO-DOCS-EXT-MIB", "cdxRPDGS7KMacAddress"),
)
if mibBuilder.loadTexts:
    cdxRPDGS7KEntry.setStatus("current")
_CdxRPDGS7KMacAddress_Type = MacAddress
_CdxRPDGS7KMacAddress_Object = MibTableColumn
cdxRPDGS7KMacAddress = _CdxRPDGS7KMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 9, 1, 1, 1),
    _CdxRPDGS7KMacAddress_Type()
)
cdxRPDGS7KMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxRPDGS7KMacAddress.setStatus("current")


class _CdxRPDGS7KPS1p24v_Type(Integer32):
    """Custom type cdxRPDGS7KPS1p24v based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3000),
    )


_CdxRPDGS7KPS1p24v_Type.__name__ = "Integer32"
_CdxRPDGS7KPS1p24v_Object = MibTableColumn
cdxRPDGS7KPS1p24v = _CdxRPDGS7KPS1p24v_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 9, 1, 1, 2),
    _CdxRPDGS7KPS1p24v_Type()
)
cdxRPDGS7KPS1p24v.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxRPDGS7KPS1p24v.setStatus("current")
if mibBuilder.loadTexts:
    cdxRPDGS7KPS1p24v.setUnits("0.01VDC")


class _CdxRPDGS7KPS1p8v_Type(Integer32):
    """Custom type cdxRPDGS7KPS1p8v based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_CdxRPDGS7KPS1p8v_Type.__name__ = "Integer32"
_CdxRPDGS7KPS1p8v_Object = MibTableColumn
cdxRPDGS7KPS1p8v = _CdxRPDGS7KPS1p8v_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 9, 1, 1, 3),
    _CdxRPDGS7KPS1p8v_Type()
)
cdxRPDGS7KPS1p8v.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxRPDGS7KPS1p8v.setStatus("current")
if mibBuilder.loadTexts:
    cdxRPDGS7KPS1p8v.setUnits("0.01VDC")


class _CdxRPDGS7KPS1p5v_Type(Integer32):
    """Custom type cdxRPDGS7KPS1p5v based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 625),
    )


_CdxRPDGS7KPS1p5v_Type.__name__ = "Integer32"
_CdxRPDGS7KPS1p5v_Object = MibTableColumn
cdxRPDGS7KPS1p5v = _CdxRPDGS7KPS1p5v_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 9, 1, 1, 4),
    _CdxRPDGS7KPS1p5v_Type()
)
cdxRPDGS7KPS1p5v.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxRPDGS7KPS1p5v.setStatus("current")
if mibBuilder.loadTexts:
    cdxRPDGS7KPS1p5v.setUnits("0.01VDC")


class _CdxRPDGS7KPS1n6v_Type(Integer32):
    """Custom type cdxRPDGS7KPS1n6v based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 800),
    )


_CdxRPDGS7KPS1n6v_Type.__name__ = "Integer32"
_CdxRPDGS7KPS1n6v_Object = MibTableColumn
cdxRPDGS7KPS1n6v = _CdxRPDGS7KPS1n6v_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 9, 1, 1, 5),
    _CdxRPDGS7KPS1n6v_Type()
)
cdxRPDGS7KPS1n6v.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxRPDGS7KPS1n6v.setStatus("current")
if mibBuilder.loadTexts:
    cdxRPDGS7KPS1n6v.setUnits("0.01VDC")


class _CdxRPDGS7KPS1AC_Type(Integer32):
    """Custom type cdxRPDGS7KPS1AC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 2000),
    )


_CdxRPDGS7KPS1AC_Type.__name__ = "Integer32"
_CdxRPDGS7KPS1AC_Object = MibTableColumn
cdxRPDGS7KPS1AC = _CdxRPDGS7KPS1AC_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 9, 1, 1, 6),
    _CdxRPDGS7KPS1AC_Type()
)
cdxRPDGS7KPS1AC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxRPDGS7KPS1AC.setStatus("current")
if mibBuilder.loadTexts:
    cdxRPDGS7KPS1AC.setUnits("0.1VAC")


class _CdxRPDGS7KPS2p24v_Type(Integer32):
    """Custom type cdxRPDGS7KPS2p24v based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3000),
    )


_CdxRPDGS7KPS2p24v_Type.__name__ = "Integer32"
_CdxRPDGS7KPS2p24v_Object = MibTableColumn
cdxRPDGS7KPS2p24v = _CdxRPDGS7KPS2p24v_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 9, 1, 1, 7),
    _CdxRPDGS7KPS2p24v_Type()
)
cdxRPDGS7KPS2p24v.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxRPDGS7KPS2p24v.setStatus("current")
if mibBuilder.loadTexts:
    cdxRPDGS7KPS2p24v.setUnits("0.01VDC")


class _CdxRPDGS7KPS2p8v_Type(Integer32):
    """Custom type cdxRPDGS7KPS2p8v based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_CdxRPDGS7KPS2p8v_Type.__name__ = "Integer32"
_CdxRPDGS7KPS2p8v_Object = MibTableColumn
cdxRPDGS7KPS2p8v = _CdxRPDGS7KPS2p8v_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 9, 1, 1, 8),
    _CdxRPDGS7KPS2p8v_Type()
)
cdxRPDGS7KPS2p8v.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxRPDGS7KPS2p8v.setStatus("current")
if mibBuilder.loadTexts:
    cdxRPDGS7KPS2p8v.setUnits("0.01VDC")


class _CdxRPDGS7KPS2p5v_Type(Integer32):
    """Custom type cdxRPDGS7KPS2p5v based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 625),
    )


_CdxRPDGS7KPS2p5v_Type.__name__ = "Integer32"
_CdxRPDGS7KPS2p5v_Object = MibTableColumn
cdxRPDGS7KPS2p5v = _CdxRPDGS7KPS2p5v_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 9, 1, 1, 9),
    _CdxRPDGS7KPS2p5v_Type()
)
cdxRPDGS7KPS2p5v.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxRPDGS7KPS2p5v.setStatus("current")
if mibBuilder.loadTexts:
    cdxRPDGS7KPS2p5v.setUnits("0.01VDC")


class _CdxRPDGS7KPS2n6v_Type(Integer32):
    """Custom type cdxRPDGS7KPS2n6v based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 800),
    )


_CdxRPDGS7KPS2n6v_Type.__name__ = "Integer32"
_CdxRPDGS7KPS2n6v_Object = MibTableColumn
cdxRPDGS7KPS2n6v = _CdxRPDGS7KPS2n6v_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 9, 1, 1, 10),
    _CdxRPDGS7KPS2n6v_Type()
)
cdxRPDGS7KPS2n6v.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxRPDGS7KPS2n6v.setStatus("current")
if mibBuilder.loadTexts:
    cdxRPDGS7KPS2n6v.setUnits("0.01VDC")


class _CdxRPDGS7KPS2AC_Type(Integer32):
    """Custom type cdxRPDGS7KPS2AC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 2000),
    )


_CdxRPDGS7KPS2AC_Type.__name__ = "Integer32"
_CdxRPDGS7KPS2AC_Object = MibTableColumn
cdxRPDGS7KPS2AC = _CdxRPDGS7KPS2AC_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 9, 1, 1, 11),
    _CdxRPDGS7KPS2AC_Type()
)
cdxRPDGS7KPS2AC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxRPDGS7KPS2AC.setStatus("current")
if mibBuilder.loadTexts:
    cdxRPDGS7KPS2AC.setUnits("0.1VAC")


class _CdxRPDGS7KTx1OptPower_Type(Integer32):
    """Custom type cdxRPDGS7KTx1OptPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_CdxRPDGS7KTx1OptPower_Type.__name__ = "Integer32"
_CdxRPDGS7KTx1OptPower_Object = MibTableColumn
cdxRPDGS7KTx1OptPower = _CdxRPDGS7KTx1OptPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 9, 1, 1, 12),
    _CdxRPDGS7KTx1OptPower_Type()
)
cdxRPDGS7KTx1OptPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxRPDGS7KTx1OptPower.setStatus("current")
if mibBuilder.loadTexts:
    cdxRPDGS7KTx1OptPower.setUnits("0.01mW")


class _CdxRPDGS7KRx1OptPower_Type(Integer32):
    """Custom type cdxRPDGS7KRx1OptPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_CdxRPDGS7KRx1OptPower_Type.__name__ = "Integer32"
_CdxRPDGS7KRx1OptPower_Object = MibTableColumn
cdxRPDGS7KRx1OptPower = _CdxRPDGS7KRx1OptPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 9, 1, 1, 13),
    _CdxRPDGS7KRx1OptPower_Type()
)
cdxRPDGS7KRx1OptPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxRPDGS7KRx1OptPower.setStatus("current")
if mibBuilder.loadTexts:
    cdxRPDGS7KRx1OptPower.setUnits("0.01mW")


class _CdxRPDGS7KTriSwitch_Type(Integer32):
    """Custom type cdxRPDGS7KTriSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("low", 1),
          ("high", 2),
          ("pad", 3))
    )


_CdxRPDGS7KTriSwitch_Type.__name__ = "Integer32"
_CdxRPDGS7KTriSwitch_Object = MibTableColumn
cdxRPDGS7KTriSwitch = _CdxRPDGS7KTriSwitch_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 9, 1, 1, 14),
    _CdxRPDGS7KTriSwitch_Type()
)
cdxRPDGS7KTriSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdxRPDGS7KTriSwitch.setStatus("current")


class _CdxRPDGS7KTamp_Type(Integer32):
    """Custom type cdxRPDGS7KTamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("intact", 1),
          ("compromised", 2))
    )


_CdxRPDGS7KTamp_Type.__name__ = "Integer32"
_CdxRPDGS7KTamp_Object = MibTableColumn
cdxRPDGS7KTamp = _CdxRPDGS7KTamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 9, 1, 1, 15),
    _CdxRPDGS7KTamp_Type()
)
cdxRPDGS7KTamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxRPDGS7KTamp.setStatus("current")
_CdxCmtsDHCPRelayObjects_ObjectIdentity = ObjectIdentity
cdxCmtsDHCPRelayObjects = _CdxCmtsDHCPRelayObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 10)
)
_CdxBundleIpHelperTable_Object = MibTable
cdxBundleIpHelperTable = _CdxBundleIpHelperTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 10, 1)
)
if mibBuilder.loadTexts:
    cdxBundleIpHelperTable.setStatus("current")
_CdxBundleIpHelperEntry_Object = MibTableRow
cdxBundleIpHelperEntry = _CdxBundleIpHelperEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 10, 1, 1)
)
cdxBundleIpHelperEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-DOCS-EXT-MIB", "cdxBundleHelperAddr"),
)
if mibBuilder.loadTexts:
    cdxBundleIpHelperEntry.setStatus("current")
_CdxBundleHelperAddr_Type = InetAddress
_CdxBundleHelperAddr_Object = MibTableColumn
cdxBundleHelperAddr = _CdxBundleHelperAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 10, 1, 1, 1),
    _CdxBundleHelperAddr_Type()
)
cdxBundleHelperAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdxBundleHelperAddr.setStatus("current")


class _CdxBundleHelperType_Type(Bits):
    """Custom type cdxBundleHelperType based on Bits"""
    namedValues = NamedValues(
        *(("dva", 0),
          ("ps", 2),
          ("stb", 3),
          ("mta", 4),
          ("customized", 5),
          ("host", 6),
          ("cm", 7))
    )

_CdxBundleHelperType_Type.__name__ = "Bits"
_CdxBundleHelperType_Object = MibTableColumn
cdxBundleHelperType = _CdxBundleHelperType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 10, 1, 1, 2),
    _CdxBundleHelperType_Type()
)
cdxBundleHelperType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxBundleHelperType.setStatus("current")
_CdxCmtsIPv6DHCPRelayObjects_ObjectIdentity = ObjectIdentity
cdxCmtsIPv6DHCPRelayObjects = _CdxCmtsIPv6DHCPRelayObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 11)
)
_CdxBundleIPv6DHCPRelayTable_Object = MibTable
cdxBundleIPv6DHCPRelayTable = _CdxBundleIPv6DHCPRelayTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 11, 1)
)
if mibBuilder.loadTexts:
    cdxBundleIPv6DHCPRelayTable.setStatus("current")
_CdxBundleIPv6DHCPRelayEntry_Object = MibTableRow
cdxBundleIPv6DHCPRelayEntry = _CdxBundleIPv6DHCPRelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 11, 1, 1)
)
cdxBundleIPv6DHCPRelayEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cdxBundleIPv6DHCPRelayEntry.setStatus("current")


class _CdxBundleIPv6DHCPRelayInsertVSSOption_Type(TruthValue):
    """Custom type cdxBundleIPv6DHCPRelayInsertVSSOption based on TruthValue"""
    defaultValue = 2


_CdxBundleIPv6DHCPRelayInsertVSSOption_Type.__name__ = "TruthValue"
_CdxBundleIPv6DHCPRelayInsertVSSOption_Object = MibTableColumn
cdxBundleIPv6DHCPRelayInsertVSSOption = _CdxBundleIPv6DHCPRelayInsertVSSOption_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 11, 1, 1, 1),
    _CdxBundleIPv6DHCPRelayInsertVSSOption_Type()
)
cdxBundleIPv6DHCPRelayInsertVSSOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxBundleIPv6DHCPRelayInsertVSSOption.setStatus("current")


class _CdxBundleIPv6DHCPRelayTrustToRelayReply_Type(TruthValue):
    """Custom type cdxBundleIPv6DHCPRelayTrustToRelayReply based on TruthValue"""
    defaultValue = 2


_CdxBundleIPv6DHCPRelayTrustToRelayReply_Type.__name__ = "TruthValue"
_CdxBundleIPv6DHCPRelayTrustToRelayReply_Object = MibTableColumn
cdxBundleIPv6DHCPRelayTrustToRelayReply = _CdxBundleIPv6DHCPRelayTrustToRelayReply_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 11, 1, 1, 2),
    _CdxBundleIPv6DHCPRelayTrustToRelayReply_Type()
)
cdxBundleIPv6DHCPRelayTrustToRelayReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxBundleIPv6DHCPRelayTrustToRelayReply.setStatus("current")
_CdxBundleIPv6DHDPRelaySourceIfname_Type = SnmpAdminString
_CdxBundleIPv6DHDPRelaySourceIfname_Object = MibTableColumn
cdxBundleIPv6DHDPRelaySourceIfname = _CdxBundleIPv6DHDPRelaySourceIfname_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 11, 1, 1, 3),
    _CdxBundleIPv6DHDPRelaySourceIfname_Type()
)
cdxBundleIPv6DHDPRelaySourceIfname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxBundleIPv6DHDPRelaySourceIfname.setStatus("current")
_CdxBundleIPv6DHCPRelayDestTable_Object = MibTable
cdxBundleIPv6DHCPRelayDestTable = _CdxBundleIPv6DHCPRelayDestTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 11, 2)
)
if mibBuilder.loadTexts:
    cdxBundleIPv6DHCPRelayDestTable.setStatus("current")
_CdxBundleIPv6DHCPRelayDestEntry_Object = MibTableRow
cdxBundleIPv6DHCPRelayDestEntry = _CdxBundleIPv6DHCPRelayDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 11, 2, 1)
)
cdxBundleIPv6DHCPRelayDestEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-DOCS-EXT-MIB", "cdxBundleIPv6DHCPRelayDestOutIfVrfIndex"),
    (0, "CISCO-DOCS-EXT-MIB", "cdxBundleIPv6DHCPRelayDestAddr"),
    (0, "CISCO-DOCS-EXT-MIB", "cdxBundleIPv6DHCPRelayDestOutIfIndex"),
)
if mibBuilder.loadTexts:
    cdxBundleIPv6DHCPRelayDestEntry.setStatus("current")


class _CdxBundleIPv6DHCPRelayDestOutIfVrfIndex_Type(Unsigned32):
    """Custom type cdxBundleIPv6DHCPRelayDestOutIfVrfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CdxBundleIPv6DHCPRelayDestOutIfVrfIndex_Type.__name__ = "Unsigned32"
_CdxBundleIPv6DHCPRelayDestOutIfVrfIndex_Object = MibTableColumn
cdxBundleIPv6DHCPRelayDestOutIfVrfIndex = _CdxBundleIPv6DHCPRelayDestOutIfVrfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 11, 2, 1, 1),
    _CdxBundleIPv6DHCPRelayDestOutIfVrfIndex_Type()
)
cdxBundleIPv6DHCPRelayDestOutIfVrfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdxBundleIPv6DHCPRelayDestOutIfVrfIndex.setStatus("current")
_CdxBundleIPv6DHCPRelayDestAddr_Type = InetAddress
_CdxBundleIPv6DHCPRelayDestAddr_Object = MibTableColumn
cdxBundleIPv6DHCPRelayDestAddr = _CdxBundleIPv6DHCPRelayDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 11, 2, 1, 2),
    _CdxBundleIPv6DHCPRelayDestAddr_Type()
)
cdxBundleIPv6DHCPRelayDestAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdxBundleIPv6DHCPRelayDestAddr.setStatus("current")
_CdxBundleIPv6DHCPRelayDestOutIfIndex_Type = InterfaceIndexOrZero
_CdxBundleIPv6DHCPRelayDestOutIfIndex_Object = MibTableColumn
cdxBundleIPv6DHCPRelayDestOutIfIndex = _CdxBundleIPv6DHCPRelayDestOutIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 11, 2, 1, 3),
    _CdxBundleIPv6DHCPRelayDestOutIfIndex_Type()
)
cdxBundleIPv6DHCPRelayDestOutIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdxBundleIPv6DHCPRelayDestOutIfIndex.setStatus("current")
_CdxBundleIPv6DHCPRelayDestSourceAddress_Type = InetAddressIPv6
_CdxBundleIPv6DHCPRelayDestSourceAddress_Object = MibTableColumn
cdxBundleIPv6DHCPRelayDestSourceAddress = _CdxBundleIPv6DHCPRelayDestSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 11, 2, 1, 4),
    _CdxBundleIPv6DHCPRelayDestSourceAddress_Type()
)
cdxBundleIPv6DHCPRelayDestSourceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxBundleIPv6DHCPRelayDestSourceAddress.setStatus("current")
_CdxBundleIPv6DHCPRelayDestLinkAddress_Type = InetAddressIPv6
_CdxBundleIPv6DHCPRelayDestLinkAddress_Object = MibTableColumn
cdxBundleIPv6DHCPRelayDestLinkAddress = _CdxBundleIPv6DHCPRelayDestLinkAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 11, 2, 1, 5),
    _CdxBundleIPv6DHCPRelayDestLinkAddress_Type()
)
cdxBundleIPv6DHCPRelayDestLinkAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxBundleIPv6DHCPRelayDestLinkAddress.setStatus("current")
_CdxCmtsCmNotificationObjects_ObjectIdentity = ObjectIdentity
cdxCmtsCmNotificationObjects = _CdxCmtsCmNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 12)
)
_CdxCmtsCmFiberNodeId_Type = Unsigned32
_CdxCmtsCmFiberNodeId_Object = MibScalar
cdxCmtsCmFiberNodeId = _CdxCmtsCmFiberNodeId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 12, 1),
    _CdxCmtsCmFiberNodeId_Type()
)
cdxCmtsCmFiberNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cdxCmtsCmFiberNodeId.setStatus("current")
_CdxCmtsCmRpdMacAddress_Type = MacAddress
_CdxCmtsCmRpdMacAddress_Object = MibScalar
cdxCmtsCmRpdMacAddress = _CdxCmtsCmRpdMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 12, 2),
    _CdxCmtsCmRpdMacAddress_Type()
)
cdxCmtsCmRpdMacAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cdxCmtsCmRpdMacAddress.setStatus("current")


class _CdxCmtsCmRpdName_Type(SnmpAdminString):
    """Custom type cdxCmtsCmRpdName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CdxCmtsCmRpdName_Type.__name__ = "SnmpAdminString"
_CdxCmtsCmRpdName_Object = MibScalar
cdxCmtsCmRpdName = _CdxCmtsCmRpdName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 12, 3),
    _CdxCmtsCmRpdName_Type()
)
cdxCmtsCmRpdName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cdxCmtsCmRpdName.setStatus("current")
_CdxCmtsCmRpdUpstreamPort_Type = Unsigned32
_CdxCmtsCmRpdUpstreamPort_Object = MibScalar
cdxCmtsCmRpdUpstreamPort = _CdxCmtsCmRpdUpstreamPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 12, 4),
    _CdxCmtsCmRpdUpstreamPort_Type()
)
cdxCmtsCmRpdUpstreamPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cdxCmtsCmRpdUpstreamPort.setStatus("current")
_CdxCmtsCmRpdDownstreamPort_Type = Unsigned32
_CdxCmtsCmRpdDownstreamPort_Object = MibScalar
cdxCmtsCmRpdDownstreamPort = _CdxCmtsCmRpdDownstreamPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 12, 5),
    _CdxCmtsCmRpdDownstreamPort_Type()
)
cdxCmtsCmRpdDownstreamPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cdxCmtsCmRpdDownstreamPort.setStatus("current")
_CdxCmtsCmRegistrationTime_Type = DateAndTime
_CdxCmtsCmRegistrationTime_Object = MibScalar
cdxCmtsCmRegistrationTime = _CdxCmtsCmRegistrationTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 12, 6),
    _CdxCmtsCmRegistrationTime_Type()
)
cdxCmtsCmRegistrationTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cdxCmtsCmRegistrationTime.setStatus("current")
_CiscoDocsExtNotificationsPrefix_ObjectIdentity = ObjectIdentity
ciscoDocsExtNotificationsPrefix = _CiscoDocsExtNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 2)
)
_CiscoDocsExtNotifications_ObjectIdentity = ObjectIdentity
ciscoDocsExtNotifications = _CiscoDocsExtNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 2, 0)
)
_CiscoDocsExtConformance_ObjectIdentity = ObjectIdentity
ciscoDocsExtConformance = _CiscoDocsExtConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 3)
)
_CdxDocsExtCompliances_ObjectIdentity = ObjectIdentity
cdxDocsExtCompliances = _CdxDocsExtCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 3, 1)
)
_CdxDocsExtGroups_ObjectIdentity = ObjectIdentity
cdxDocsExtGroups = _CdxDocsExtGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 3, 2)
)
docsIfCmtsServiceEntry.registerAugmentions(
    ("CISCO-DOCS-EXT-MIB",
     "cdxCmtsServiceExtEntry")
)
cdxCmtsServiceExtEntry.setIndexNames(*docsIfCmtsServiceEntry.getIndexNames())
docsIfCmtsCmStatusEntry.registerAugmentions(
    ("CISCO-DOCS-EXT-MIB",
     "cdxCmtsCmStatusExtEntry")
)
cdxCmtsCmStatusExtEntry.setIndexNames(*docsIfCmtsCmStatusEntry.getIndexNames())
docsIfCmtsMacEntry.registerAugmentions(
    ("CISCO-DOCS-EXT-MIB",
     "cdxCmtsMacExtEntry")
)
cdxCmtsMacExtEntry.setIndexNames(*docsIfCmtsMacEntry.getIndexNames())
docsIfUpstreamChannelEntry.registerAugmentions(
    ("CISCO-DOCS-EXT-MIB",
     "cdxIfUpstreamChannelExtEntry")
)
cdxIfUpstreamChannelExtEntry.setIndexNames(*docsIfUpstreamChannelEntry.getIndexNames())

# Managed Objects groups

cdxQosCtrlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 3, 2, 1)
)
cdxQosCtrlGroup.setObjects(
      *(("CISCO-DOCS-EXT-MIB", "cdxQosCtrlUpAdmissionCtrl"),
        ("CISCO-DOCS-EXT-MIB", "cdxQosCtrlUpMaxRsvdBWPercent"),
        ("CISCO-DOCS-EXT-MIB", "cdxQosCtrlUpAdmissionRejects"),
        ("CISCO-DOCS-EXT-MIB", "cdxQosCtrlUpReservedBW"),
        ("CISCO-DOCS-EXT-MIB", "cdxQosCtrlUpMaxVirtualBW"),
        ("CISCO-DOCS-EXT-MIB", "cdxQosIfRateLimitAlgm"),
        ("CISCO-DOCS-EXT-MIB", "cdxQosIfRateLimitExpWt"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsServiceOutOctets"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsServiceOutPackets"),
        ("CISCO-DOCS-EXT-MIB", "cdxQosMaxUpBWExcessRequests"),
        ("CISCO-DOCS-EXT-MIB", "cdxQosMaxDownBWExcessPackets"))
)
if mibBuilder.loadTexts:
    cdxQosCtrlGroup.setStatus("obsolete")

cdxQosQueueGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 3, 2, 2)
)
cdxQosQueueGroup.setObjects(
      *(("CISCO-DOCS-EXT-MIB", "cdxBWQueueOrder"),
        ("CISCO-DOCS-EXT-MIB", "cdxBWQueueNumServedBeforeYield"),
        ("CISCO-DOCS-EXT-MIB", "cdxBWQueueType"),
        ("CISCO-DOCS-EXT-MIB", "cdxBWQueueMaxDepth"),
        ("CISCO-DOCS-EXT-MIB", "cdxBWQueueDepth"),
        ("CISCO-DOCS-EXT-MIB", "cdxBWQueueDiscards"))
)
if mibBuilder.loadTexts:
    cdxQosQueueGroup.setStatus("current")

cdxCmtsCmCpeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 3, 2, 3)
)
cdxCmtsCmCpeGroup.setObjects(
      *(("CISCO-DOCS-EXT-MIB", "cdxCmCpeType"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeIpAddress"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeIfIndex"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeCmtsServiceId"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeCmStatusIndex"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeAccessGroup"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmStatusValue"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusOnlineTimes"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusPercentOnline"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusMinOnlineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusAvgOnlineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusMaxOnlineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusMinOfflineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusAvgOfflineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusMaxOfflineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmOnOffTrapEnable"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmOnOffTrapInterval"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmDefaultMaxCpes"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverTimeExpiration"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverMacAddress"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverDownFrequency"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverUpChannelId"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverTrapOnCompletion"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverOpInitiatedTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverState"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverRowStatus"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmMaxCpeNumber"))
)
if mibBuilder.loadTexts:
    cdxCmtsCmCpeGroup.setStatus("obsolete")

cdxQosCtrlGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 3, 2, 4)
)
cdxQosCtrlGroupRev1.setObjects(
      *(("CISCO-DOCS-EXT-MIB", "cdxQosCtrlUpAdmissionCtrl"),
        ("CISCO-DOCS-EXT-MIB", "cdxQosCtrlUpMaxRsvdBWPercent"),
        ("CISCO-DOCS-EXT-MIB", "cdxQosCtrlUpAdmissionRejects"),
        ("CISCO-DOCS-EXT-MIB", "cdxQosCtrlUpReservedBW"),
        ("CISCO-DOCS-EXT-MIB", "cdxQosCtrlUpMaxVirtualBW"),
        ("CISCO-DOCS-EXT-MIB", "cdxQosIfRateLimitAlgm"),
        ("CISCO-DOCS-EXT-MIB", "cdxQosIfRateLimitExpWt"),
        ("CISCO-DOCS-EXT-MIB", "cdxQosIfRateLimitShpGranularity"),
        ("CISCO-DOCS-EXT-MIB", "cdxQosIfRateLimitShpMaxDelay"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsServiceOutOctets"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsServiceOutPackets"),
        ("CISCO-DOCS-EXT-MIB", "cdxQosMaxUpBWExcessRequests"),
        ("CISCO-DOCS-EXT-MIB", "cdxQosMaxDownBWExcessPackets"))
)
if mibBuilder.loadTexts:
    cdxQosCtrlGroupRev1.setStatus("obsolete")

cdxCmtsCmCpeGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 3, 2, 5)
)
cdxCmtsCmCpeGroupRev1.setObjects(
      *(("CISCO-DOCS-EXT-MIB", "cdxCmCpeType"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeIpAddress"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeIfIndex"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeCmtsServiceId"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeCmStatusIndex"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeAccessGroup"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmStatusValue"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusOnlineTimes"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusPercentOnline"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusMinOnlineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusAvgOnlineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusMaxOnlineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusMinOfflineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusAvgOfflineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusMaxOfflineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusDynSidCount"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmOnOffTrapEnable"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmOnOffTrapInterval"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmDefaultMaxCpes"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverTimeExpiration"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverMacAddress"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverDownFrequency"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverUpChannelId"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverTrapOnCompletion"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverOpInitiatedTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverState"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverRowStatus"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmMaxCpeNumber"))
)
if mibBuilder.loadTexts:
    cdxCmtsCmCpeGroupRev1.setStatus("obsolete")

cdxSpecMgmtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 3, 2, 6)
)
cdxSpecMgmtGroup.setObjects(
      *(("CISCO-DOCS-EXT-MIB", "cdxIfUpChannelWidth"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfUpChannelModulationProfile"))
)
if mibBuilder.loadTexts:
    cdxSpecMgmtGroup.setStatus("obsolete")

cdxCmtsCmCpeGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 3, 2, 7)
)
cdxCmtsCmCpeGroupRev2.setObjects(
      *(("CISCO-DOCS-EXT-MIB", "cdxCmCpeType"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeIpAddress"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeIfIndex"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeCmtsServiceId"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeCmStatusIndex"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeAccessGroup"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeResetNow"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmStatusValue"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusOnlineTimes"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusPercentOnline"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusMinOnlineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusAvgOnlineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusMaxOnlineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusMinOfflineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusAvgOfflineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusMaxOfflineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusDynSidCount"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmOnOffTrapEnable"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmOnOffTrapInterval"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmDefaultMaxCpes"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverTimeExpiration"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverMacAddress"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverDownFrequency"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverUpChannelId"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverTrapOnCompletion"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverOpInitiatedTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverState"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverRowStatus"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmMaxCpeNumber"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmCurrCpeNumber"))
)
if mibBuilder.loadTexts:
    cdxCmtsCmCpeGroupRev2.setStatus("obsolete")

cdxSpecMgmtGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 3, 2, 8)
)
cdxSpecMgmtGroupRev1.setObjects(
      *(("CISCO-DOCS-EXT-MIB", "cdxIfUpChannelWidth"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfUpChannelModulationProfile"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfUpChannelCmTotal"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfUpChannelCmActive"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfUpChannelCmRegistered"))
)
if mibBuilder.loadTexts:
    cdxSpecMgmtGroupRev1.setStatus("obsolete")

cdxCmtsCmCpeGroupRev3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 3, 2, 9)
)
cdxCmtsCmCpeGroupRev3.setObjects(
      *(("CISCO-DOCS-EXT-MIB", "cdxCmCpeType"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeIpAddress"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeIfIndex"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeCmtsServiceId"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeCmStatusIndex"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeAccessGroup"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeResetNow"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmStatusValue"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusOnlineTimes"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusPercentOnline"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusMinOnlineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusAvgOnlineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusMaxOnlineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusMinOfflineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusAvgOfflineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusMaxOfflineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusDynSidCount"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmOnOffTrapEnable"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmOnOffTrapInterval"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmDefaultMaxCpes"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmTotal"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmActive"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmRegistered"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverTimeExpiration"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverMacAddress"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverDownFrequency"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverUpChannelId"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverTrapOnCompletion"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverOpInitiatedTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverState"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverRowStatus"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmMaxCpeNumber"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmCurrCpeNumber"))
)
if mibBuilder.loadTexts:
    cdxCmtsCmCpeGroupRev3.setStatus("obsolete")

cdxQosCtrlGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 3, 2, 10)
)
cdxQosCtrlGroupRev2.setObjects(
      *(("CISCO-DOCS-EXT-MIB", "cdxQosCtrlUpAdmissionCtrl"),
        ("CISCO-DOCS-EXT-MIB", "cdxQosCtrlUpMaxRsvdBWPercent"),
        ("CISCO-DOCS-EXT-MIB", "cdxQosCtrlUpAdmissionRejects"),
        ("CISCO-DOCS-EXT-MIB", "cdxQosCtrlUpReservedBW"),
        ("CISCO-DOCS-EXT-MIB", "cdxQosCtrlUpMaxVirtualBW"),
        ("CISCO-DOCS-EXT-MIB", "cdxQosIfRateLimitAlgm"),
        ("CISCO-DOCS-EXT-MIB", "cdxQosIfRateLimitExpWt"),
        ("CISCO-DOCS-EXT-MIB", "cdxQosIfRateLimitShpGranularity"),
        ("CISCO-DOCS-EXT-MIB", "cdxQosIfRateLimitShpMaxDelay"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsServiceOutOctets"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsServiceOutPackets"),
        ("CISCO-DOCS-EXT-MIB", "cdxQosMaxUpBWExcessRequests"),
        ("CISCO-DOCS-EXT-MIB", "cdxQosMaxDownBWExcessPackets"),
        ("CISCO-DOCS-EXT-MIB", "cdxUpInfoElemStatsIEType"))
)
if mibBuilder.loadTexts:
    cdxQosCtrlGroupRev2.setStatus("current")

cdxCmtsCmCpeGroupRev4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 3, 2, 11)
)
cdxCmtsCmCpeGroupRev4.setObjects(
      *(("CISCO-DOCS-EXT-MIB", "cdxCmCpeType"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeIpAddress"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeIfIndex"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeCmtsServiceId"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeCmStatusIndex"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeAccessGroup"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeResetNow"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmStatusValue"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusOnlineTimes"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusPercentOnline"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusMinOnlineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusAvgOnlineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusMaxOnlineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusMinOfflineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusAvgOfflineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusMaxOfflineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusDynSidCount"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusAddlInfo"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmOnOffTrapEnable"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmOnOffTrapInterval"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmDefaultMaxCpes"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmTotal"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmActive"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmRegistered"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverTimeExpiration"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverMacAddress"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverDownFrequency"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverUpChannelId"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverTrapOnCompletion"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverOpInitiatedTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverState"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverRowStatus"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmMaxCpeNumber"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmCurrCpeNumber"))
)
if mibBuilder.loadTexts:
    cdxCmtsCmCpeGroupRev4.setStatus("obsolete")

cdxSpecMgmtGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 3, 2, 12)
)
cdxSpecMgmtGroupRev2.setObjects(
      *(("CISCO-DOCS-EXT-MIB", "cdxIfUpChannelWidth"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfUpChannelModulationProfile"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfUpChannelCmTotal"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfUpChannelCmActive"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfUpChannelCmRegistered"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfUpChannelInputPowerLevel"))
)
if mibBuilder.loadTexts:
    cdxSpecMgmtGroupRev2.setStatus("obsolete")

cdxSpecMgmtGroupRev3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 3, 2, 14)
)
cdxSpecMgmtGroupRev3.setObjects(
      *(("CISCO-DOCS-EXT-MIB", "cdxIfUpChannelWidth"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfUpChannelModulationProfile"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfUpChannelCmTotal"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfUpChannelCmActive"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfUpChannelCmRegistered"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfUpChannelInputPowerLevel"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfUpChannelAvgUtil"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfUpChannelAvgContSlots"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfUpChannelRangeSlots"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfUpChannelNumActiveUGS"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfUpChannelMaxUGSLastOneHour"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfUpChannelMinUGSLastOneHour"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfUpChannelAvgUGSLastOneHour"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfUpChannelMaxUGSLastFiveMins"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfUpChannelMinUGSLastFiveMins"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfUpChannelAvgUGSLastFiveMins"))
)
if mibBuilder.loadTexts:
    cdxSpecMgmtGroupRev3.setStatus("current")

cdxCmtsCmCpeGroupRev5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 3, 2, 15)
)
cdxCmtsCmCpeGroupRev5.setObjects(
      *(("CISCO-DOCS-EXT-MIB", "cdxCmCpeType"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeIfIndex"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeCmtsServiceId"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeCmStatusIndex"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeAccessGroup"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeResetNow"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmStatusValue"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusOnlineTimes"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusPercentOnline"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusMinOnlineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusAvgOnlineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusMaxOnlineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusMinOfflineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusAvgOfflineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusMaxOfflineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusDynSidCount"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusAddlInfo"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmOnOffTrapEnable"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmOnOffTrapInterval"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmDefaultMaxCpes"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmTotal"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmActive"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmRegistered"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverTimeExpiration"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverMacAddress"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverDownFrequency"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverUpChannelId"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverTrapOnCompletion"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverOpInitiatedTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverState"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverRowStatus"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmMaxCpeNumber"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmCurrCpeNumber"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusOnlineTimesNum"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusLastResetTime"))
)
if mibBuilder.loadTexts:
    cdxCmtsCmCpeGroupRev5.setStatus("obsolete")

cdxCmtsCmCpeGroupRev6 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 3, 2, 16)
)
cdxCmtsCmCpeGroupRev6.setObjects(
      *(("CISCO-DOCS-EXT-MIB", "cdxCmCpeType"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeIfIndex"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeCmtsServiceId"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeCmStatusIndex"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeAccessGroup"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeResetNow"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmStatusValue"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusOnlineTimes"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusPercentOnline"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusMinOnlineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusAvgOnlineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusMaxOnlineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusMinOfflineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusAvgOfflineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusMaxOfflineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusDynSidCount"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusAddlInfo"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmOnOffTrapEnable"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmOnOffTrapInterval"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmDefaultMaxCpes"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmTotal"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmActive"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmRegistered"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverTimeExpiration"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverMacAddress"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverDownFrequency"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverUpChannelId"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverTrapOnCompletion"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverOpInitiatedTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverState"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverRowStatus"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmMaxCpeNumber"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmCurrCpeNumber"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmQosProfile"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusOnlineTimesNum"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusLastResetTime"))
)
if mibBuilder.loadTexts:
    cdxCmtsCmCpeGroupRev6.setStatus("obsolete")

cdxCmtsCmCpeGroupRev7 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 3, 2, 17)
)
cdxCmtsCmCpeGroupRev7.setObjects(
      *(("CISCO-DOCS-EXT-MIB", "cdxCmCpeType"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeIpAddress"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeIfIndex"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeCmtsServiceId"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeCmStatusIndex"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeAccessGroup"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeResetNow"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmStatusValue"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusOnlineTimes"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusPercentOnline"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusMinOnlineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusAvgOnlineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusMaxOnlineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusMinOfflineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusAvgOfflineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusMaxOfflineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusDynSidCount"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusAddlInfo"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmOnOffTrapEnable"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmOnOffTrapInterval"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmDefaultMaxCpes"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmTotal"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmActive"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmRegistered"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmDMICMode"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmDMICLockQos"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverTimeExpiration"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverMacAddress"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverDownFrequency"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverUpChannelId"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverTrapOnCompletion"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverOpInitiatedTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverState"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverRowStatus"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmMaxCpeNumber"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmCurrCpeNumber"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmQosProfile"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmStatusDMICMode"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmStatusDMICUnLock"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusOnlineTimesNum"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusLastResetTime"))
)
if mibBuilder.loadTexts:
    cdxCmtsCmCpeGroupRev7.setStatus("obsolete")

cdxCmtsCmCpeGroupRev8 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 3, 2, 18)
)
cdxCmtsCmCpeGroupRev8.setObjects(
      *(("CISCO-DOCS-EXT-MIB", "cdxCmCpeType"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeIpAddress"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeIfIndex"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeCmtsServiceId"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeCmStatusIndex"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeAccessGroup"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeResetNow"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmStatusValue"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusOnlineTimes"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusPercentOnline"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusMinOnlineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusAvgOnlineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusMaxOnlineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusMinOfflineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusAvgOfflineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusMaxOfflineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusDynSidCount"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusAddlInfo"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmOnOffTrapEnable"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmOnOffTrapInterval"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmDefaultMaxCpes"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmTotal"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmActive"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmRegistered"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmDMICMode"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmDMICLockQos"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverTimeExpiration"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverMacAddress"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverDownFrequency"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverUpChannelId"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverTrapOnCompletion"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverOpInitiatedTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverState"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverRowStatus"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmMaxCpeNumber"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmCurrCpeNumber"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmQosProfile"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmStatusDMICMode"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmStatusDMICUnLock"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusOnlineTimesNum"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusLastResetTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmToCpeInetAddressType"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmToCpeInetAddress"),
        ("CISCO-DOCS-EXT-MIB", "cdxCpeToCmMacAddress"),
        ("CISCO-DOCS-EXT-MIB", "cdxCpeToCmInetAddressType"),
        ("CISCO-DOCS-EXT-MIB", "cdxCpeToCmInetAddress"),
        ("CISCO-DOCS-EXT-MIB", "cdxCpeToCmStatusIndex"))
)
if mibBuilder.loadTexts:
    cdxCmtsCmCpeGroupRev8.setStatus("current")

cdxCmtsCmCpeDeleteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 3, 2, 20)
)
cdxCmtsCmCpeDeleteGroup.setObjects(
    ("CISCO-DOCS-EXT-MIB", "cdxCmCpeDeleteNow")
)
if mibBuilder.loadTexts:
    cdxCmtsCmCpeDeleteGroup.setStatus("current")

cdxWBResilGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 3, 2, 21)
)
cdxWBResilGroup.setObjects(
      *(("CISCO-DOCS-EXT-MIB", "cdxWBResilRFChangeDampenTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxWBResilRFChangeTriggerPercentage"),
        ("CISCO-DOCS-EXT-MIB", "cdxWBResilRFChangeTriggerCount"),
        ("CISCO-DOCS-EXT-MIB", "cdxWBResilRFChangeTriggerMoveSecondary"),
        ("CISCO-DOCS-EXT-MIB", "cdxWBResilNotificationEnable"),
        ("CISCO-DOCS-EXT-MIB", "cdxWBResilNotificationsInterval"),
        ("CISCO-DOCS-EXT-MIB", "cdxWBResilEventLevel"),
        ("CISCO-DOCS-EXT-MIB", "cdxWBResilEventType"),
        ("CISCO-DOCS-EXT-MIB", "cdxWBResilUpdateTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxWBResilEventTotalCount"),
        ("CISCO-DOCS-EXT-MIB", "cdxWBResilEventTotalDupCount"))
)
if mibBuilder.loadTexts:
    cdxWBResilGroup.setStatus("current")

cdxQosCtrlGroupExt = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 3, 2, 23)
)
cdxQosCtrlGroupExt.setObjects(
      *(("CISCO-DOCS-EXT-MIB", "cdxIfCmtsServiceHCInOctets"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsServiceHCInPackets"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsServiceHCOutOctets"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsServiceHCOutPackets"))
)
if mibBuilder.loadTexts:
    cdxQosCtrlGroupExt.setStatus("current")

cdxDownstreamGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 3, 2, 24)
)
cdxDownstreamGroup.setObjects(
      *(("CISCO-DOCS-EXT-MIB", "cdxPrimaryChannelIfIndex"),
        ("CISCO-DOCS-EXT-MIB", "cdxPhysicalRFIfIndex"))
)
if mibBuilder.loadTexts:
    cdxDownstreamGroup.setStatus("current")

cdxCpeIpPrefixGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 3, 2, 25)
)
cdxCpeIpPrefixGroup.setObjects(
      *(("CISCO-DOCS-EXT-MIB", "cdxCpeIpPrefixCpeMacAddress"),
        ("CISCO-DOCS-EXT-MIB", "cdxCpeIpPrefixCpeType"))
)
if mibBuilder.loadTexts:
    cdxCpeIpPrefixGroup.setStatus("current")

cdxCmtsMtcCmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 3, 2, 26)
)
cdxCmtsMtcCmGroup.setObjects(
      *(("CISCO-DOCS-EXT-MIB", "cdxCmtsMtcCmTotal"),
        ("CISCO-DOCS-EXT-MIB", "cdxCMtsMtcCmOperational"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsMtcCmRegistered"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsMtcCmUnregistered"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsMtcCmOffline"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsMtcCmWideband"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsMtcUpstreamBondGrp"))
)
if mibBuilder.loadTexts:
    cdxCmtsMtcCmGroup.setStatus("current")

cdxCmtsUscbSflowGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 3, 2, 27)
)
cdxCmtsUscbSflowGroup.setObjects(
      *(("CISCO-DOCS-EXT-MIB", "cdxCmtsUscbSfTotal"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsUscbSfPri"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsUscbStaticSfBe"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsUscbStaticSfUgs"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsUscbStaticSfUgsad"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsUscbStaticSfRtps"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsUscbStaticSfNrtps"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsUscbDynSfBe"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsUscbDynSfUgs"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsUscbDynSfUgsad"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsUscbDynSfRtps"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsUscbDynSfNrtps"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsUscbDescr"))
)
if mibBuilder.loadTexts:
    cdxCmtsUscbSflowGroup.setStatus("current")

cdxCmtsDocsisLBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 3, 2, 28)
)
cdxCmtsDocsisLBGroup.setObjects(
      *(("CISCO-DOCS-EXT-MIB", "cdxCmtsD30LBEnable"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsD30LBUpstreamEnable"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsD30LBStaticEnable"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsD30LBDynEnable"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsDocsisLBEnable"))
)
if mibBuilder.loadTexts:
    cdxCmtsDocsisLBGroup.setStatus("current")


# Notification objects

cdxCmtsCmOnOffNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 2, 0, 1)
)
cdxCmtsCmOnOffNotification.setObjects(
      *(("DOCS-IF-MIB", "docsIfCmtsCmStatusMacAddress"),
        ("DOCS-IF-MIB", "docsIfCmtsCmStatusInetAddressType"),
        ("DOCS-IF-MIB", "docsIfCmtsCmStatusInetAddress"),
        ("DOCS-IF-MIB", "docsIfCmtsCmStatusDownChannelIfIndex"),
        ("DOCS-IF-MIB", "docsIfCmtsCmStatusUpChannelIfIndex"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeCmtsServiceId"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmStatusValue"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmFiberNodeId"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmRpdMacAddress"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmRpdName"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmRpdUpstreamPort"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmRpdDownstreamPort"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmRegistrationTime"))
)
if mibBuilder.loadTexts:
    cdxCmtsCmOnOffNotification.setStatus(
        "current"
    )

cdxCmtsCmChOverNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 2, 0, 2)
)
cdxCmtsCmChOverNotification.setObjects(
      *(("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverMacAddress"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverDownFrequency"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverUpChannelId"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverOpInitiatedTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverState"))
)
if mibBuilder.loadTexts:
    cdxCmtsCmChOverNotification.setStatus(
        "current"
    )

cdxCmtsCmDMICLockNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 2, 0, 3)
)
cdxCmtsCmDMICLockNotification.setObjects(
    ("DOCS-IF-MIB", "docsIfCmtsCmStatusMacAddress")
)
if mibBuilder.loadTexts:
    cdxCmtsCmDMICLockNotification.setStatus(
        "current"
    )

cdxWBResilRFDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 2, 0, 4)
)
cdxWBResilRFDown.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("CISCO-DOCS-EXT-MIB", "cdxWBResilEventLevel"))
)
if mibBuilder.loadTexts:
    cdxWBResilRFDown.setStatus(
        "current"
    )

cdxWBResilRFUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 2, 0, 5)
)
cdxWBResilRFUp.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("CISCO-DOCS-EXT-MIB", "cdxWBResilEventLevel"))
)
if mibBuilder.loadTexts:
    cdxWBResilRFUp.setStatus(
        "current"
    )

cdxWBResilCMPartialServiceNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 2, 0, 6)
)
cdxWBResilCMPartialServiceNotif.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("DOCS-IF-MIB", "docsIfCmtsCmStatusMacAddress"),
        ("DOCS-IF-MIB", "docsIfCmtsCmStatusDownChannelIfIndex"),
        ("CISCO-DOCS-EXT-MIB", "cdxWBResilEventLevel"),
        ("CISCO-DOCS-EXT-MIB", "cdxWBResilUpdateTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxWBResilCmImpairedDsChIndex"))
)
if mibBuilder.loadTexts:
    cdxWBResilCMPartialServiceNotif.setStatus(
        "current"
    )

cdxWBResilCMFullServiceNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 2, 0, 7)
)
cdxWBResilCMFullServiceNotif.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("DOCS-IF-MIB", "docsIfCmtsCmStatusMacAddress"),
        ("DOCS-IF-MIB", "docsIfCmtsCmStatusDownChannelIfIndex"),
        ("CISCO-DOCS-EXT-MIB", "cdxWBResilEventLevel"),
        ("CISCO-DOCS-EXT-MIB", "cdxWBResilUpdateTime"))
)
if mibBuilder.loadTexts:
    cdxWBResilCMFullServiceNotif.setStatus(
        "current"
    )

cdxWBResilEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 2, 0, 8)
)
cdxWBResilEvent.setObjects(
      *(("DOCS-IF-MIB", "docsIfCmtsCmStatusMacAddress"),
        ("CISCO-DOCS-EXT-MIB", "cdxWBResilEventType"),
        ("CISCO-DOCS-EXT-MIB", "cdxWBResilUpdateTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxWBResilEventTotalCount"),
        ("CISCO-DOCS-EXT-MIB", "cdxWBResilEventTotalDupCount"),
        ("CISCO-DOCS-EXT-MIB", "cdxWBResilEventLevel"))
)
if mibBuilder.loadTexts:
    cdxWBResilEvent.setStatus(
        "current"
    )

cdxWBResilUsPartialServiceNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 2, 0, 9)
)
cdxWBResilUsPartialServiceNotif.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("DOCS-IF-MIB", "docsIfCmtsCmStatusMacAddress"),
        ("DOCS-IF-MIB", "docsIfCmtsCmStatusUpChannelIfIndex"),
        ("CISCO-DOCS-EXT-MIB", "cdxUsResilEventType"),
        ("CISCO-DOCS-EXT-MIB", "cdxWBResilEventLevel"),
        ("CISCO-DOCS-EXT-MIB", "cdxWBResilUpdateTime"))
)
if mibBuilder.loadTexts:
    cdxWBResilUsPartialServiceNotif.setStatus(
        "current"
    )

cdxWBResilUsFullServiceNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 2, 0, 10)
)
cdxWBResilUsFullServiceNotif.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("DOCS-IF-MIB", "docsIfCmtsCmStatusMacAddress"),
        ("DOCS-IF-MIB", "docsIfCmtsCmStatusUpChannelIfIndex"),
        ("CISCO-DOCS-EXT-MIB", "cdxUsResilEventType"),
        ("CISCO-DOCS-EXT-MIB", "cdxWBResilEventLevel"),
        ("CISCO-DOCS-EXT-MIB", "cdxWBResilUpdateTime"))
)
if mibBuilder.loadTexts:
    cdxWBResilUsFullServiceNotif.setStatus(
        "current"
    )


# Notifications groups

cdxNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 3, 2, 13)
)
cdxNotifGroup.setObjects(
      *(("CISCO-DOCS-EXT-MIB", "cdxCmtsCmOnOffNotification"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverNotification"))
)
if mibBuilder.loadTexts:
    cdxNotifGroup.setStatus(
        "obsolete"
    )

cdxNotifGroupRev1 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 3, 2, 19)
)
cdxNotifGroupRev1.setObjects(
      *(("CISCO-DOCS-EXT-MIB", "cdxCmtsCmOnOffNotification"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverNotification"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmDMICLockNotification"))
)
if mibBuilder.loadTexts:
    cdxNotifGroupRev1.setStatus(
        "current"
    )

cdxNotifGroupExt = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 3, 2, 22)
)
cdxNotifGroupExt.setObjects(
      *(("CISCO-DOCS-EXT-MIB", "cdxWBResilRFDown"),
        ("CISCO-DOCS-EXT-MIB", "cdxWBResilRFUp"),
        ("CISCO-DOCS-EXT-MIB", "cdxWBResilCMPartialServiceNotif"),
        ("CISCO-DOCS-EXT-MIB", "cdxWBResilCMFullServiceNotif"),
        ("CISCO-DOCS-EXT-MIB", "cdxWBResilEvent"))
)
if mibBuilder.loadTexts:
    cdxNotifGroupExt.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cdxDocsExtCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 3, 1, 1)
)
cdxDocsExtCompliance.setObjects(
      *(("CISCO-DOCS-EXT-MIB", "cdxQosCtrlGroup"),
        ("CISCO-DOCS-EXT-MIB", "cdxQosQueueGroup"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmCpeGroup"))
)
if mibBuilder.loadTexts:
    cdxDocsExtCompliance.setStatus(
        "obsolete"
    )

cdxDocsExtComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 3, 1, 2)
)
cdxDocsExtComplianceRev1.setObjects(
      *(("CISCO-DOCS-EXT-MIB", "cdxQosCtrlGroupRev1"),
        ("CISCO-DOCS-EXT-MIB", "cdxQosQueueGroup"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmCpeGroupRev1"),
        ("CISCO-DOCS-EXT-MIB", "cdxSpecMgmtGroup"))
)
if mibBuilder.loadTexts:
    cdxDocsExtComplianceRev1.setStatus(
        "obsolete"
    )

cdxDocsExtComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 3, 1, 3)
)
cdxDocsExtComplianceRev2.setObjects(
      *(("CISCO-DOCS-EXT-MIB", "cdxQosCtrlGroupRev1"),
        ("CISCO-DOCS-EXT-MIB", "cdxQosQueueGroup"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmCpeGroupRev2"),
        ("CISCO-DOCS-EXT-MIB", "cdxSpecMgmtGroup"))
)
if mibBuilder.loadTexts:
    cdxDocsExtComplianceRev2.setStatus(
        "obsolete"
    )

cdxDocsExtComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 3, 1, 4)
)
cdxDocsExtComplianceRev3.setObjects(
      *(("CISCO-DOCS-EXT-MIB", "cdxQosCtrlGroupRev1"),
        ("CISCO-DOCS-EXT-MIB", "cdxQosQueueGroup"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmCpeGroupRev3"),
        ("CISCO-DOCS-EXT-MIB", "cdxSpecMgmtGroupRev1"))
)
if mibBuilder.loadTexts:
    cdxDocsExtComplianceRev3.setStatus(
        "obsolete"
    )

cdxDocsExtComplianceRev4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 3, 1, 5)
)
cdxDocsExtComplianceRev4.setObjects(
      *(("CISCO-DOCS-EXT-MIB", "cdxQosCtrlGroupRev2"),
        ("CISCO-DOCS-EXT-MIB", "cdxQosQueueGroup"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmCpeGroupRev4"),
        ("CISCO-DOCS-EXT-MIB", "cdxSpecMgmtGroupRev1"))
)
if mibBuilder.loadTexts:
    cdxDocsExtComplianceRev4.setStatus(
        "obsolete"
    )

cdxDocsExtComplianceRev5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 3, 1, 6)
)
cdxDocsExtComplianceRev5.setObjects(
      *(("CISCO-DOCS-EXT-MIB", "cdxQosCtrlGroupRev2"),
        ("CISCO-DOCS-EXT-MIB", "cdxQosQueueGroup"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmCpeGroupRev4"),
        ("CISCO-DOCS-EXT-MIB", "cdxSpecMgmtGroupRev2"),
        ("CISCO-DOCS-EXT-MIB", "cdxNotifGroup"))
)
if mibBuilder.loadTexts:
    cdxDocsExtComplianceRev5.setStatus(
        "obsolete"
    )

cdxDocsExtComplianceRev6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 3, 1, 7)
)
cdxDocsExtComplianceRev6.setObjects(
      *(("CISCO-DOCS-EXT-MIB", "cdxQosCtrlGroupRev2"),
        ("CISCO-DOCS-EXT-MIB", "cdxQosQueueGroup"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmCpeGroupRev4"),
        ("CISCO-DOCS-EXT-MIB", "cdxSpecMgmtGroupRev3"),
        ("CISCO-DOCS-EXT-MIB", "cdxNotifGroup"))
)
if mibBuilder.loadTexts:
    cdxDocsExtComplianceRev6.setStatus(
        "obsolete"
    )

cdxDocsExtComplianceRev7 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 3, 1, 8)
)
cdxDocsExtComplianceRev7.setObjects(
      *(("CISCO-DOCS-EXT-MIB", "cdxQosCtrlGroupRev2"),
        ("CISCO-DOCS-EXT-MIB", "cdxQosQueueGroup"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmCpeGroupRev5"),
        ("CISCO-DOCS-EXT-MIB", "cdxSpecMgmtGroupRev3"),
        ("CISCO-DOCS-EXT-MIB", "cdxNotifGroup"))
)
if mibBuilder.loadTexts:
    cdxDocsExtComplianceRev7.setStatus(
        "obsolete"
    )

cdxDocsExtComplianceRev8 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 3, 1, 9)
)
cdxDocsExtComplianceRev8.setObjects(
      *(("CISCO-DOCS-EXT-MIB", "cdxQosCtrlGroupRev2"),
        ("CISCO-DOCS-EXT-MIB", "cdxQosQueueGroup"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmCpeGroupRev6"),
        ("CISCO-DOCS-EXT-MIB", "cdxSpecMgmtGroupRev3"),
        ("CISCO-DOCS-EXT-MIB", "cdxNotifGroup"))
)
if mibBuilder.loadTexts:
    cdxDocsExtComplianceRev8.setStatus(
        "obsolete"
    )

cdxDocsExtComplianceRev9 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 3, 1, 10)
)
cdxDocsExtComplianceRev9.setObjects(
      *(("CISCO-DOCS-EXT-MIB", "cdxQosCtrlGroupRev2"),
        ("CISCO-DOCS-EXT-MIB", "cdxQosQueueGroup"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmCpeGroupRev7"),
        ("CISCO-DOCS-EXT-MIB", "cdxSpecMgmtGroupRev3"),
        ("CISCO-DOCS-EXT-MIB", "cdxNotifGroupRev1"))
)
if mibBuilder.loadTexts:
    cdxDocsExtComplianceRev9.setStatus(
        "obsolete"
    )

cdxDocsExtComplianceRev10 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 3, 1, 11)
)
cdxDocsExtComplianceRev10.setObjects(
      *(("CISCO-DOCS-EXT-MIB", "cdxQosCtrlGroupRev2"),
        ("CISCO-DOCS-EXT-MIB", "cdxQosQueueGroup"),
        ("CISCO-DOCS-EXT-MIB", "cdxSpecMgmtGroupRev3"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmCpeGroupRev8"),
        ("CISCO-DOCS-EXT-MIB", "cdxNotifGroupRev1"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmCpeDeleteGroup"))
)
if mibBuilder.loadTexts:
    cdxDocsExtComplianceRev10.setStatus(
        "obsolete"
    )

cdxDocsExtComplianceRev11 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 3, 1, 12)
)
cdxDocsExtComplianceRev11.setObjects(
      *(("CISCO-DOCS-EXT-MIB", "cdxQosCtrlGroupRev2"),
        ("CISCO-DOCS-EXT-MIB", "cdxQosCtrlGroupExt"),
        ("CISCO-DOCS-EXT-MIB", "cdxNotifGroupRev1"),
        ("CISCO-DOCS-EXT-MIB", "cdxQosQueueGroup"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmCpeGroupRev8"),
        ("CISCO-DOCS-EXT-MIB", "cdxSpecMgmtGroupRev3"),
        ("CISCO-DOCS-EXT-MIB", "cdxDownstreamGroup"),
        ("CISCO-DOCS-EXT-MIB", "cdxNotifGroupExt"),
        ("CISCO-DOCS-EXT-MIB", "cdxWBResilGroup"))
)
if mibBuilder.loadTexts:
    cdxDocsExtComplianceRev11.setStatus(
        "deprecated"
    )

cdxDocsExtComplianceRev12 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 3, 1, 13)
)
cdxDocsExtComplianceRev12.setObjects(
      *(("CISCO-DOCS-EXT-MIB", "cdxQosCtrlGroupRev2"),
        ("CISCO-DOCS-EXT-MIB", "cdxQosCtrlGroupExt"),
        ("CISCO-DOCS-EXT-MIB", "cdxNotifGroupRev1"),
        ("CISCO-DOCS-EXT-MIB", "cdxQosQueueGroup"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmCpeGroupRev8"),
        ("CISCO-DOCS-EXT-MIB", "cdxSpecMgmtGroupRev3"),
        ("CISCO-DOCS-EXT-MIB", "cdxDownstreamGroup"),
        ("CISCO-DOCS-EXT-MIB", "cdxNotifGroupExt"),
        ("CISCO-DOCS-EXT-MIB", "cdxWBResilGroup"),
        ("CISCO-DOCS-EXT-MIB", "cdxCpeIpPrefixGroup"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsMtcCmGroup"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsUscbSflowGroup"))
)
if mibBuilder.loadTexts:
    cdxDocsExtComplianceRev12.setStatus(
        "current"
    )

cdxDocsExtComplianceRev13 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 3, 1, 14)
)
cdxDocsExtComplianceRev13.setObjects(
      *(("CISCO-DOCS-EXT-MIB", "cdxQosCtrlGroupRev2"),
        ("CISCO-DOCS-EXT-MIB", "cdxQosCtrlGroupExt"),
        ("CISCO-DOCS-EXT-MIB", "cdxNotifGroupRev1"),
        ("CISCO-DOCS-EXT-MIB", "cdxQosQueueGroup"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmCpeGroupRev8"),
        ("CISCO-DOCS-EXT-MIB", "cdxSpecMgmtGroupRev3"),
        ("CISCO-DOCS-EXT-MIB", "cdxDownstreamGroup"),
        ("CISCO-DOCS-EXT-MIB", "cdxNotifGroupExt"),
        ("CISCO-DOCS-EXT-MIB", "cdxWBResilGroup"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsDocsisLBGroup"),
        ("CISCO-DOCS-EXT-MIB", "cdxCpeIpPrefixGroup"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsMtcCmGroup"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsUscbSflowGroup"))
)
if mibBuilder.loadTexts:
    cdxDocsExtComplianceRev13.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-DOCS-EXT-MIB",
    **{"CdxResettableCounter32": CdxResettableCounter32,
       "CdxUpstreamBondGrpList": CdxUpstreamBondGrpList,
       "ciscoDocsExtMIB": ciscoDocsExtMIB,
       "ciscoDocsExtMIBObjects": ciscoDocsExtMIBObjects,
       "cdxQosCtrlObjects": cdxQosCtrlObjects,
       "cdxQosCtrlUpTable": cdxQosCtrlUpTable,
       "cdxQosCtrlUpEntry": cdxQosCtrlUpEntry,
       "cdxQosCtrlUpAdmissionCtrl": cdxQosCtrlUpAdmissionCtrl,
       "cdxQosCtrlUpMaxRsvdBWPercent": cdxQosCtrlUpMaxRsvdBWPercent,
       "cdxQosCtrlUpAdmissionRejects": cdxQosCtrlUpAdmissionRejects,
       "cdxQosCtrlUpReservedBW": cdxQosCtrlUpReservedBW,
       "cdxQosCtrlUpMaxVirtualBW": cdxQosCtrlUpMaxVirtualBW,
       "cdxQosIfRateLimitTable": cdxQosIfRateLimitTable,
       "cdxQosIfRateLimitEntry": cdxQosIfRateLimitEntry,
       "cdxQosIfRateLimitAlgm": cdxQosIfRateLimitAlgm,
       "cdxQosIfRateLimitExpWt": cdxQosIfRateLimitExpWt,
       "cdxQosIfRateLimitShpMaxDelay": cdxQosIfRateLimitShpMaxDelay,
       "cdxQosIfRateLimitShpGranularity": cdxQosIfRateLimitShpGranularity,
       "cdxCmtsServiceExtTable": cdxCmtsServiceExtTable,
       "cdxCmtsServiceExtEntry": cdxCmtsServiceExtEntry,
       "cdxIfCmtsServiceOutOctets": cdxIfCmtsServiceOutOctets,
       "cdxIfCmtsServiceOutPackets": cdxIfCmtsServiceOutPackets,
       "cdxQosMaxUpBWExcessRequests": cdxQosMaxUpBWExcessRequests,
       "cdxQosMaxDownBWExcessPackets": cdxQosMaxDownBWExcessPackets,
       "cdxIfCmtsServiceHCInOctets": cdxIfCmtsServiceHCInOctets,
       "cdxIfCmtsServiceHCInPackets": cdxIfCmtsServiceHCInPackets,
       "cdxIfCmtsServiceHCOutOctets": cdxIfCmtsServiceHCOutOctets,
       "cdxIfCmtsServiceHCOutPackets": cdxIfCmtsServiceHCOutPackets,
       "cdxUpInfoElemStatsTable": cdxUpInfoElemStatsTable,
       "cdxUpInfoElemStatsEntry": cdxUpInfoElemStatsEntry,
       "cdxUpInfoElemStatsNameCode": cdxUpInfoElemStatsNameCode,
       "cdxUpInfoElemStatsIEType": cdxUpInfoElemStatsIEType,
       "cdxQosQueueObjects": cdxQosQueueObjects,
       "cdxBWQueueTable": cdxBWQueueTable,
       "cdxBWQueueEntry": cdxBWQueueEntry,
       "cdxBWQueueNameCode": cdxBWQueueNameCode,
       "cdxBWQueueOrder": cdxBWQueueOrder,
       "cdxBWQueueNumServedBeforeYield": cdxBWQueueNumServedBeforeYield,
       "cdxBWQueueType": cdxBWQueueType,
       "cdxBWQueueMaxDepth": cdxBWQueueMaxDepth,
       "cdxBWQueueDepth": cdxBWQueueDepth,
       "cdxBWQueueDiscards": cdxBWQueueDiscards,
       "cdxCmtsCmCpeObjects": cdxCmtsCmCpeObjects,
       "cdxCmCpeTable": cdxCmCpeTable,
       "cdxCmCpeEntry": cdxCmCpeEntry,
       "cdxCmCpeMacAddress": cdxCmCpeMacAddress,
       "cdxCmCpeType": cdxCmCpeType,
       "cdxCmCpeIpAddress": cdxCmCpeIpAddress,
       "cdxCmCpeIfIndex": cdxCmCpeIfIndex,
       "cdxCmCpeCmtsServiceId": cdxCmCpeCmtsServiceId,
       "cdxCmCpeCmStatusIndex": cdxCmCpeCmStatusIndex,
       "cdxCmCpeAccessGroup": cdxCmCpeAccessGroup,
       "cdxCmCpeResetNow": cdxCmCpeResetNow,
       "cdxCmCpeDeleteNow": cdxCmCpeDeleteNow,
       "cdxCmtsCmStatusExtTable": cdxCmtsCmStatusExtTable,
       "cdxCmtsCmStatusExtEntry": cdxCmtsCmStatusExtEntry,
       "cdxCmtsCmStatusValue": cdxCmtsCmStatusValue,
       "cdxIfCmtsCmStatusOnlineTimes": cdxIfCmtsCmStatusOnlineTimes,
       "cdxIfCmtsCmStatusPercentOnline": cdxIfCmtsCmStatusPercentOnline,
       "cdxIfCmtsCmStatusMinOnlineTime": cdxIfCmtsCmStatusMinOnlineTime,
       "cdxIfCmtsCmStatusAvgOnlineTime": cdxIfCmtsCmStatusAvgOnlineTime,
       "cdxIfCmtsCmStatusMaxOnlineTime": cdxIfCmtsCmStatusMaxOnlineTime,
       "cdxIfCmtsCmStatusMinOfflineTime": cdxIfCmtsCmStatusMinOfflineTime,
       "cdxIfCmtsCmStatusAvgOfflineTime": cdxIfCmtsCmStatusAvgOfflineTime,
       "cdxIfCmtsCmStatusMaxOfflineTime": cdxIfCmtsCmStatusMaxOfflineTime,
       "cdxIfCmtsCmStatusDynSidCount": cdxIfCmtsCmStatusDynSidCount,
       "cdxIfCmtsCmStatusAddlInfo": cdxIfCmtsCmStatusAddlInfo,
       "cdxIfCmtsCmStatusOnlineTimesNum": cdxIfCmtsCmStatusOnlineTimesNum,
       "cdxIfCmtsCmStatusLastResetTime": cdxIfCmtsCmStatusLastResetTime,
       "cdxCmtsMacExtTable": cdxCmtsMacExtTable,
       "cdxCmtsMacExtEntry": cdxCmtsMacExtEntry,
       "cdxCmtsCmOnOffTrapEnable": cdxCmtsCmOnOffTrapEnable,
       "cdxCmtsCmOnOffTrapInterval": cdxCmtsCmOnOffTrapInterval,
       "cdxCmtsCmDefaultMaxCpes": cdxCmtsCmDefaultMaxCpes,
       "cdxCmtsCmTotal": cdxCmtsCmTotal,
       "cdxCmtsCmActive": cdxCmtsCmActive,
       "cdxCmtsCmRegistered": cdxCmtsCmRegistered,
       "cdxCmtsCmDMICMode": cdxCmtsCmDMICMode,
       "cdxCmtsCmDMICLockQos": cdxCmtsCmDMICLockQos,
       "cdxCmtsCmChOverTimeExpiration": cdxCmtsCmChOverTimeExpiration,
       "cdxCmtsCmChOverTable": cdxCmtsCmChOverTable,
       "cdxCmtsCmChOverEntry": cdxCmtsCmChOverEntry,
       "cdxCmtsCmChOverSerialNumber": cdxCmtsCmChOverSerialNumber,
       "cdxCmtsCmChOverMacAddress": cdxCmtsCmChOverMacAddress,
       "cdxCmtsCmChOverDownFrequency": cdxCmtsCmChOverDownFrequency,
       "cdxCmtsCmChOverUpChannelId": cdxCmtsCmChOverUpChannelId,
       "cdxCmtsCmChOverTrapOnCompletion": cdxCmtsCmChOverTrapOnCompletion,
       "cdxCmtsCmChOverOpInitiatedTime": cdxCmtsCmChOverOpInitiatedTime,
       "cdxCmtsCmChOverState": cdxCmtsCmChOverState,
       "cdxCmtsCmChOverRowStatus": cdxCmtsCmChOverRowStatus,
       "cdxCmtsCmTable": cdxCmtsCmTable,
       "cdxCmtsCmEntry": cdxCmtsCmEntry,
       "cdxCmtsCmMaxCpeNumber": cdxCmtsCmMaxCpeNumber,
       "cdxCmtsCmCurrCpeNumber": cdxCmtsCmCurrCpeNumber,
       "cdxCmtsCmQosProfile": cdxCmtsCmQosProfile,
       "cdxCmtsCmStatusDMICTable": cdxCmtsCmStatusDMICTable,
       "cdxCmtsCmStatusDMICEntry": cdxCmtsCmStatusDMICEntry,
       "cdxCmtsCmStatusDMICMode": cdxCmtsCmStatusDMICMode,
       "cdxCmtsCmStatusDMICUnLock": cdxCmtsCmStatusDMICUnLock,
       "cdxCmToCpeTable": cdxCmToCpeTable,
       "cdxCmToCpeEntry": cdxCmToCpeEntry,
       "cdxCmToCpeCmMacAddress": cdxCmToCpeCmMacAddress,
       "cdxCmToCpeInetAddressType": cdxCmToCpeInetAddressType,
       "cdxCmToCpeInetAddress": cdxCmToCpeInetAddress,
       "cdxCpeToCmTable": cdxCpeToCmTable,
       "cdxCpeToCmEntry": cdxCpeToCmEntry,
       "cdxCpeToCmCpeMacAddress": cdxCpeToCmCpeMacAddress,
       "cdxCpeToCmMacAddress": cdxCpeToCmMacAddress,
       "cdxCpeToCmInetAddressType": cdxCpeToCmInetAddressType,
       "cdxCpeToCmInetAddress": cdxCpeToCmInetAddress,
       "cdxCpeToCmStatusIndex": cdxCpeToCmStatusIndex,
       "cdxCpeIpPrefixTable": cdxCpeIpPrefixTable,
       "cdxCpeIpPrefixEntry": cdxCpeIpPrefixEntry,
       "cdxCpeIpPrefixCmMacAddress": cdxCpeIpPrefixCmMacAddress,
       "cdxCpeIpPrefixType": cdxCpeIpPrefixType,
       "cdxCpeIpPrefixAddress": cdxCpeIpPrefixAddress,
       "cdxCpeIpPrefixLen": cdxCpeIpPrefixLen,
       "cdxCpeIpPrefixCpeMacAddress": cdxCpeIpPrefixCpeMacAddress,
       "cdxCpeIpPrefixCpeType": cdxCpeIpPrefixCpeType,
       "cdxSpecMgmtObjects": cdxSpecMgmtObjects,
       "cdxIfUpstreamChannelExtTable": cdxIfUpstreamChannelExtTable,
       "cdxIfUpstreamChannelExtEntry": cdxIfUpstreamChannelExtEntry,
       "cdxIfUpChannelWidth": cdxIfUpChannelWidth,
       "cdxIfUpChannelModulationProfile": cdxIfUpChannelModulationProfile,
       "cdxIfUpChannelCmTotal": cdxIfUpChannelCmTotal,
       "cdxIfUpChannelCmActive": cdxIfUpChannelCmActive,
       "cdxIfUpChannelCmRegistered": cdxIfUpChannelCmRegistered,
       "cdxIfUpChannelInputPowerLevel": cdxIfUpChannelInputPowerLevel,
       "cdxIfUpChannelAvgUtil": cdxIfUpChannelAvgUtil,
       "cdxIfUpChannelAvgContSlots": cdxIfUpChannelAvgContSlots,
       "cdxIfUpChannelRangeSlots": cdxIfUpChannelRangeSlots,
       "cdxIfUpChannelNumActiveUGS": cdxIfUpChannelNumActiveUGS,
       "cdxIfUpChannelMaxUGSLastOneHour": cdxIfUpChannelMaxUGSLastOneHour,
       "cdxIfUpChannelMinUGSLastOneHour": cdxIfUpChannelMinUGSLastOneHour,
       "cdxIfUpChannelAvgUGSLastOneHour": cdxIfUpChannelAvgUGSLastOneHour,
       "cdxIfUpChannelMaxUGSLastFiveMins": cdxIfUpChannelMaxUGSLastFiveMins,
       "cdxIfUpChannelMinUGSLastFiveMins": cdxIfUpChannelMinUGSLastFiveMins,
       "cdxIfUpChannelAvgUGSLastFiveMins": cdxIfUpChannelAvgUGSLastFiveMins,
       "cdxWBResilObjects": cdxWBResilObjects,
       "cdxWBResilRFChangeDampenTime": cdxWBResilRFChangeDampenTime,
       "cdxWBResilRFChangeTriggerPercentage": cdxWBResilRFChangeTriggerPercentage,
       "cdxWBResilRFChangeTriggerCount": cdxWBResilRFChangeTriggerCount,
       "cdxWBResilRFChangeTriggerMoveSecondary": cdxWBResilRFChangeTriggerMoveSecondary,
       "cdxWBResilNotificationEnable": cdxWBResilNotificationEnable,
       "cdxWBResilNotificationsInterval": cdxWBResilNotificationsInterval,
       "cdxWBResilEventLevel": cdxWBResilEventLevel,
       "cdxWBResilEventType": cdxWBResilEventType,
       "cdxWBResilUpdateTime": cdxWBResilUpdateTime,
       "cdxWBResilEventTotalCount": cdxWBResilEventTotalCount,
       "cdxWBResilEventTotalDupCount": cdxWBResilEventTotalDupCount,
       "cdxUsResilEventType": cdxUsResilEventType,
       "cdxWBResilCmTable": cdxWBResilCmTable,
       "cdxWBResilCmEntry": cdxWBResilCmEntry,
       "cdxWBResilCmIndex": cdxWBResilCmIndex,
       "cdxWBResilCmMacAddr": cdxWBResilCmMacAddr,
       "cdxWBResilCmTotalDsNum": cdxWBResilCmTotalDsNum,
       "cdxWBResilCmTotalUsNum": cdxWBResilCmTotalUsNum,
       "cdxWBResilCmCurrentDsNum": cdxWBResilCmCurrentDsNum,
       "cdxWBResilCmCurrentUsNum": cdxWBResilCmCurrentUsNum,
       "cdxWBResilCmImpairedDsChIndex": cdxWBResilCmImpairedDsChIndex,
       "cdxWBResilCmImpairedUsChIndex": cdxWBResilCmImpairedUsChIndex,
       "cdxDownstreamObjects": cdxDownstreamObjects,
       "cdxRFtoPrimaryChannelMappingTable": cdxRFtoPrimaryChannelMappingTable,
       "cdxRFtoPrimaryChannelMappingEntry": cdxRFtoPrimaryChannelMappingEntry,
       "cdxPrimaryChannelIfIndex": cdxPrimaryChannelIfIndex,
       "cdxPrimaryChanneltoRFMappingTable": cdxPrimaryChanneltoRFMappingTable,
       "cdxPrimaryChanneltoRFMappingEntry": cdxPrimaryChanneltoRFMappingEntry,
       "cdxPhysicalRFIfIndex": cdxPhysicalRFIfIndex,
       "cdxCmtsMtcCmSfObjects": cdxCmtsMtcCmSfObjects,
       "cdxCmtsMtcCmTable": cdxCmtsMtcCmTable,
       "cdxCmtsMtcCmEntry": cdxCmtsMtcCmEntry,
       "cdxCmtsMtcTcsId": cdxCmtsMtcTcsId,
       "cdxCmtsMtcCmTotal": cdxCmtsMtcCmTotal,
       "cdxCMtsMtcCmOperational": cdxCMtsMtcCmOperational,
       "cdxCmtsMtcCmRegistered": cdxCmtsMtcCmRegistered,
       "cdxCmtsMtcCmUnregistered": cdxCmtsMtcCmUnregistered,
       "cdxCmtsMtcCmOffline": cdxCmtsMtcCmOffline,
       "cdxCmtsMtcCmWideband": cdxCmtsMtcCmWideband,
       "cdxCmtsMtcUpstreamBondGrp": cdxCmtsMtcUpstreamBondGrp,
       "cdxCmtsUscbSflowTable": cdxCmtsUscbSflowTable,
       "cdxCmtsUscbSflowEntry": cdxCmtsUscbSflowEntry,
       "cdxCmtsUsBondingGrpId": cdxCmtsUsBondingGrpId,
       "cdxCmtsUscbSfTotal": cdxCmtsUscbSfTotal,
       "cdxCmtsUscbSfPri": cdxCmtsUscbSfPri,
       "cdxCmtsUscbStaticSfBe": cdxCmtsUscbStaticSfBe,
       "cdxCmtsUscbStaticSfUgs": cdxCmtsUscbStaticSfUgs,
       "cdxCmtsUscbStaticSfUgsad": cdxCmtsUscbStaticSfUgsad,
       "cdxCmtsUscbStaticSfRtps": cdxCmtsUscbStaticSfRtps,
       "cdxCmtsUscbStaticSfNrtps": cdxCmtsUscbStaticSfNrtps,
       "cdxCmtsUscbDynSfBe": cdxCmtsUscbDynSfBe,
       "cdxCmtsUscbDynSfUgs": cdxCmtsUscbDynSfUgs,
       "cdxCmtsUscbDynSfUgsad": cdxCmtsUscbDynSfUgsad,
       "cdxCmtsUscbDynSfRtps": cdxCmtsUscbDynSfRtps,
       "cdxCmtsUscbDynSfNrtps": cdxCmtsUscbDynSfNrtps,
       "cdxCmtsUscbDescr": cdxCmtsUscbDescr,
       "cdxCmtsDocsisLBObjects": cdxCmtsDocsisLBObjects,
       "cdxCmtsDocsisLBEnable": cdxCmtsDocsisLBEnable,
       "cdxCmtsD30LBEnable": cdxCmtsD30LBEnable,
       "cdxCmtsD30LBUpstreamEnable": cdxCmtsD30LBUpstreamEnable,
       "cdxCmtsD30LBStaticEnable": cdxCmtsD30LBStaticEnable,
       "cdxCmtsD30LBDynEnable": cdxCmtsD30LBDynEnable,
       "cdxRPDGS7KObjects": cdxRPDGS7KObjects,
       "cdxRPDGS7KTable": cdxRPDGS7KTable,
       "cdxRPDGS7KEntry": cdxRPDGS7KEntry,
       "cdxRPDGS7KMacAddress": cdxRPDGS7KMacAddress,
       "cdxRPDGS7KPS1p24v": cdxRPDGS7KPS1p24v,
       "cdxRPDGS7KPS1p8v": cdxRPDGS7KPS1p8v,
       "cdxRPDGS7KPS1p5v": cdxRPDGS7KPS1p5v,
       "cdxRPDGS7KPS1n6v": cdxRPDGS7KPS1n6v,
       "cdxRPDGS7KPS1AC": cdxRPDGS7KPS1AC,
       "cdxRPDGS7KPS2p24v": cdxRPDGS7KPS2p24v,
       "cdxRPDGS7KPS2p8v": cdxRPDGS7KPS2p8v,
       "cdxRPDGS7KPS2p5v": cdxRPDGS7KPS2p5v,
       "cdxRPDGS7KPS2n6v": cdxRPDGS7KPS2n6v,
       "cdxRPDGS7KPS2AC": cdxRPDGS7KPS2AC,
       "cdxRPDGS7KTx1OptPower": cdxRPDGS7KTx1OptPower,
       "cdxRPDGS7KRx1OptPower": cdxRPDGS7KRx1OptPower,
       "cdxRPDGS7KTriSwitch": cdxRPDGS7KTriSwitch,
       "cdxRPDGS7KTamp": cdxRPDGS7KTamp,
       "cdxCmtsDHCPRelayObjects": cdxCmtsDHCPRelayObjects,
       "cdxBundleIpHelperTable": cdxBundleIpHelperTable,
       "cdxBundleIpHelperEntry": cdxBundleIpHelperEntry,
       "cdxBundleHelperAddr": cdxBundleHelperAddr,
       "cdxBundleHelperType": cdxBundleHelperType,
       "cdxCmtsIPv6DHCPRelayObjects": cdxCmtsIPv6DHCPRelayObjects,
       "cdxBundleIPv6DHCPRelayTable": cdxBundleIPv6DHCPRelayTable,
       "cdxBundleIPv6DHCPRelayEntry": cdxBundleIPv6DHCPRelayEntry,
       "cdxBundleIPv6DHCPRelayInsertVSSOption": cdxBundleIPv6DHCPRelayInsertVSSOption,
       "cdxBundleIPv6DHCPRelayTrustToRelayReply": cdxBundleIPv6DHCPRelayTrustToRelayReply,
       "cdxBundleIPv6DHDPRelaySourceIfname": cdxBundleIPv6DHDPRelaySourceIfname,
       "cdxBundleIPv6DHCPRelayDestTable": cdxBundleIPv6DHCPRelayDestTable,
       "cdxBundleIPv6DHCPRelayDestEntry": cdxBundleIPv6DHCPRelayDestEntry,
       "cdxBundleIPv6DHCPRelayDestOutIfVrfIndex": cdxBundleIPv6DHCPRelayDestOutIfVrfIndex,
       "cdxBundleIPv6DHCPRelayDestAddr": cdxBundleIPv6DHCPRelayDestAddr,
       "cdxBundleIPv6DHCPRelayDestOutIfIndex": cdxBundleIPv6DHCPRelayDestOutIfIndex,
       "cdxBundleIPv6DHCPRelayDestSourceAddress": cdxBundleIPv6DHCPRelayDestSourceAddress,
       "cdxBundleIPv6DHCPRelayDestLinkAddress": cdxBundleIPv6DHCPRelayDestLinkAddress,
       "cdxCmtsCmNotificationObjects": cdxCmtsCmNotificationObjects,
       "cdxCmtsCmFiberNodeId": cdxCmtsCmFiberNodeId,
       "cdxCmtsCmRpdMacAddress": cdxCmtsCmRpdMacAddress,
       "cdxCmtsCmRpdName": cdxCmtsCmRpdName,
       "cdxCmtsCmRpdUpstreamPort": cdxCmtsCmRpdUpstreamPort,
       "cdxCmtsCmRpdDownstreamPort": cdxCmtsCmRpdDownstreamPort,
       "cdxCmtsCmRegistrationTime": cdxCmtsCmRegistrationTime,
       "ciscoDocsExtNotificationsPrefix": ciscoDocsExtNotificationsPrefix,
       "ciscoDocsExtNotifications": ciscoDocsExtNotifications,
       "cdxCmtsCmOnOffNotification": cdxCmtsCmOnOffNotification,
       "cdxCmtsCmChOverNotification": cdxCmtsCmChOverNotification,
       "cdxCmtsCmDMICLockNotification": cdxCmtsCmDMICLockNotification,
       "cdxWBResilRFDown": cdxWBResilRFDown,
       "cdxWBResilRFUp": cdxWBResilRFUp,
       "cdxWBResilCMPartialServiceNotif": cdxWBResilCMPartialServiceNotif,
       "cdxWBResilCMFullServiceNotif": cdxWBResilCMFullServiceNotif,
       "cdxWBResilEvent": cdxWBResilEvent,
       "cdxWBResilUsPartialServiceNotif": cdxWBResilUsPartialServiceNotif,
       "cdxWBResilUsFullServiceNotif": cdxWBResilUsFullServiceNotif,
       "ciscoDocsExtConformance": ciscoDocsExtConformance,
       "cdxDocsExtCompliances": cdxDocsExtCompliances,
       "cdxDocsExtCompliance": cdxDocsExtCompliance,
       "cdxDocsExtComplianceRev1": cdxDocsExtComplianceRev1,
       "cdxDocsExtComplianceRev2": cdxDocsExtComplianceRev2,
       "cdxDocsExtComplianceRev3": cdxDocsExtComplianceRev3,
       "cdxDocsExtComplianceRev4": cdxDocsExtComplianceRev4,
       "cdxDocsExtComplianceRev5": cdxDocsExtComplianceRev5,
       "cdxDocsExtComplianceRev6": cdxDocsExtComplianceRev6,
       "cdxDocsExtComplianceRev7": cdxDocsExtComplianceRev7,
       "cdxDocsExtComplianceRev8": cdxDocsExtComplianceRev8,
       "cdxDocsExtComplianceRev9": cdxDocsExtComplianceRev9,
       "cdxDocsExtComplianceRev10": cdxDocsExtComplianceRev10,
       "cdxDocsExtComplianceRev11": cdxDocsExtComplianceRev11,
       "cdxDocsExtComplianceRev12": cdxDocsExtComplianceRev12,
       "cdxDocsExtComplianceRev13": cdxDocsExtComplianceRev13,
       "cdxDocsExtGroups": cdxDocsExtGroups,
       "cdxQosCtrlGroup": cdxQosCtrlGroup,
       "cdxQosQueueGroup": cdxQosQueueGroup,
       "cdxCmtsCmCpeGroup": cdxCmtsCmCpeGroup,
       "cdxQosCtrlGroupRev1": cdxQosCtrlGroupRev1,
       "cdxCmtsCmCpeGroupRev1": cdxCmtsCmCpeGroupRev1,
       "cdxSpecMgmtGroup": cdxSpecMgmtGroup,
       "cdxCmtsCmCpeGroupRev2": cdxCmtsCmCpeGroupRev2,
       "cdxSpecMgmtGroupRev1": cdxSpecMgmtGroupRev1,
       "cdxCmtsCmCpeGroupRev3": cdxCmtsCmCpeGroupRev3,
       "cdxQosCtrlGroupRev2": cdxQosCtrlGroupRev2,
       "cdxCmtsCmCpeGroupRev4": cdxCmtsCmCpeGroupRev4,
       "cdxSpecMgmtGroupRev2": cdxSpecMgmtGroupRev2,
       "cdxNotifGroup": cdxNotifGroup,
       "cdxSpecMgmtGroupRev3": cdxSpecMgmtGroupRev3,
       "cdxCmtsCmCpeGroupRev5": cdxCmtsCmCpeGroupRev5,
       "cdxCmtsCmCpeGroupRev6": cdxCmtsCmCpeGroupRev6,
       "cdxCmtsCmCpeGroupRev7": cdxCmtsCmCpeGroupRev7,
       "cdxCmtsCmCpeGroupRev8": cdxCmtsCmCpeGroupRev8,
       "cdxNotifGroupRev1": cdxNotifGroupRev1,
       "cdxCmtsCmCpeDeleteGroup": cdxCmtsCmCpeDeleteGroup,
       "cdxWBResilGroup": cdxWBResilGroup,
       "cdxNotifGroupExt": cdxNotifGroupExt,
       "cdxQosCtrlGroupExt": cdxQosCtrlGroupExt,
       "cdxDownstreamGroup": cdxDownstreamGroup,
       "cdxCpeIpPrefixGroup": cdxCpeIpPrefixGroup,
       "cdxCmtsMtcCmGroup": cdxCmtsMtcCmGroup,
       "cdxCmtsUscbSflowGroup": cdxCmtsUscbSflowGroup,
       "cdxCmtsDocsisLBGroup": cdxCmtsDocsisLBGroup}
)
