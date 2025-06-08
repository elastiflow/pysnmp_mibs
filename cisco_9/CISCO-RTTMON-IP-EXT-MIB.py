# SNMP MIB module (CISCO-RTTMON-IP-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-RTTMON-IP-EXT-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 00:18:37 2025
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

(rttMonCtrlAdminEntry,
 rttMonCtrlAdminIndex,
 rttMonCtrlOperEntry,
 rttMonEchoAdminEntry,
 rttMonEchoPathAdminEntry,
 rttMonHistoryCollectionEntry,
 rttMonLpdGrpStatsEntry,
 rttMonStatsCollectEntry) = mibBuilder.importSymbols(
    "CISCO-RTTMON-MIB",
    "rttMonCtrlAdminEntry",
    "rttMonCtrlAdminIndex",
    "rttMonCtrlOperEntry",
    "rttMonEchoAdminEntry",
    "rttMonEchoPathAdminEntry",
    "rttMonHistoryCollectionEntry",
    "rttMonLpdGrpStatsEntry",
    "rttMonStatsCollectEntry")

(CipslaPercentileVar,) = mibBuilder.importSymbols(
    "CISCO-RTTMON-TC-MIB",
    "CipslaPercentileVar")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(DscpOrAny,) = mibBuilder.importSymbols(
    "DIFFSERV-DSCP-TC",
    "DscpOrAny")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(IPv6FlowLabelOrAny,) = mibBuilder.importSymbols(
    "IPV6-FLOW-LABEL-MIB",
    "IPv6FlowLabelOrAny")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ciscoRttMonIPExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 572)
)
if mibBuilder.loadTexts:
    ciscoRttMonIPExtMIB.setRevisions(
        ("2018-04-09 00:00",
         "2017-09-06 00:00",
         "2006-08-02 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CrttMonIPExtObjects_ObjectIdentity = ObjectIdentity
crttMonIPExtObjects = _CrttMonIPExtObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 572, 1)
)
_CrttMonIPEchoAdminTable_Object = MibTable
crttMonIPEchoAdminTable = _CrttMonIPEchoAdminTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 1)
)
if mibBuilder.loadTexts:
    crttMonIPEchoAdminTable.setStatus("current")
_CrttMonIPEchoAdminEntry_Object = MibTableRow
crttMonIPEchoAdminEntry = _CrttMonIPEchoAdminEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 1, 1)
)
if mibBuilder.loadTexts:
    crttMonIPEchoAdminEntry.setStatus("current")


class _CrttMonIPEchoAdminTargetAddrType_Type(InetAddressType):
    """Custom type crttMonIPEchoAdminTargetAddrType based on InetAddressType"""
    defaultValue = 0


_CrttMonIPEchoAdminTargetAddrType_Type.__name__ = "InetAddressType"
_CrttMonIPEchoAdminTargetAddrType_Object = MibTableColumn
crttMonIPEchoAdminTargetAddrType = _CrttMonIPEchoAdminTargetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 1, 1, 1),
    _CrttMonIPEchoAdminTargetAddrType_Type()
)
crttMonIPEchoAdminTargetAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crttMonIPEchoAdminTargetAddrType.setStatus("current")


class _CrttMonIPEchoAdminTargetAddress_Type(InetAddress):
    """Custom type crttMonIPEchoAdminTargetAddress based on InetAddress"""
    defaultValue = OctetString("")


_CrttMonIPEchoAdminTargetAddress_Type.__name__ = "InetAddress"
_CrttMonIPEchoAdminTargetAddress_Object = MibTableColumn
crttMonIPEchoAdminTargetAddress = _CrttMonIPEchoAdminTargetAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 1, 1, 2),
    _CrttMonIPEchoAdminTargetAddress_Type()
)
crttMonIPEchoAdminTargetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crttMonIPEchoAdminTargetAddress.setStatus("current")


class _CrttMonIPEchoAdminSourceAddrType_Type(InetAddressType):
    """Custom type crttMonIPEchoAdminSourceAddrType based on InetAddressType"""
    defaultValue = 0


_CrttMonIPEchoAdminSourceAddrType_Type.__name__ = "InetAddressType"
_CrttMonIPEchoAdminSourceAddrType_Object = MibTableColumn
crttMonIPEchoAdminSourceAddrType = _CrttMonIPEchoAdminSourceAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 1, 1, 3),
    _CrttMonIPEchoAdminSourceAddrType_Type()
)
crttMonIPEchoAdminSourceAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crttMonIPEchoAdminSourceAddrType.setStatus("current")


class _CrttMonIPEchoAdminSourceAddress_Type(InetAddress):
    """Custom type crttMonIPEchoAdminSourceAddress based on InetAddress"""
    defaultValue = OctetString("")


_CrttMonIPEchoAdminSourceAddress_Type.__name__ = "InetAddress"
_CrttMonIPEchoAdminSourceAddress_Object = MibTableColumn
crttMonIPEchoAdminSourceAddress = _CrttMonIPEchoAdminSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 1, 1, 4),
    _CrttMonIPEchoAdminSourceAddress_Type()
)
crttMonIPEchoAdminSourceAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crttMonIPEchoAdminSourceAddress.setStatus("current")


class _CrttMonIPEchoAdminNameServerAddrType_Type(InetAddressType):
    """Custom type crttMonIPEchoAdminNameServerAddrType based on InetAddressType"""
    defaultValue = 0


_CrttMonIPEchoAdminNameServerAddrType_Type.__name__ = "InetAddressType"
_CrttMonIPEchoAdminNameServerAddrType_Object = MibTableColumn
crttMonIPEchoAdminNameServerAddrType = _CrttMonIPEchoAdminNameServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 1, 1, 5),
    _CrttMonIPEchoAdminNameServerAddrType_Type()
)
crttMonIPEchoAdminNameServerAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crttMonIPEchoAdminNameServerAddrType.setStatus("current")


class _CrttMonIPEchoAdminNameServerAddress_Type(InetAddress):
    """Custom type crttMonIPEchoAdminNameServerAddress based on InetAddress"""
    defaultValue = OctetString("")


_CrttMonIPEchoAdminNameServerAddress_Type.__name__ = "InetAddress"
_CrttMonIPEchoAdminNameServerAddress_Object = MibTableColumn
crttMonIPEchoAdminNameServerAddress = _CrttMonIPEchoAdminNameServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 1, 1, 6),
    _CrttMonIPEchoAdminNameServerAddress_Type()
)
crttMonIPEchoAdminNameServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crttMonIPEchoAdminNameServerAddress.setStatus("current")


class _CrttMonIPEchoAdminLSPSelAddrType_Type(InetAddressType):
    """Custom type crttMonIPEchoAdminLSPSelAddrType based on InetAddressType"""
    defaultValue = 0


_CrttMonIPEchoAdminLSPSelAddrType_Type.__name__ = "InetAddressType"
_CrttMonIPEchoAdminLSPSelAddrType_Object = MibTableColumn
crttMonIPEchoAdminLSPSelAddrType = _CrttMonIPEchoAdminLSPSelAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 1, 1, 7),
    _CrttMonIPEchoAdminLSPSelAddrType_Type()
)
crttMonIPEchoAdminLSPSelAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crttMonIPEchoAdminLSPSelAddrType.setStatus("current")


class _CrttMonIPEchoAdminLSPSelAddress_Type(InetAddress):
    """Custom type crttMonIPEchoAdminLSPSelAddress based on InetAddress"""
    defaultValue = OctetString("")


_CrttMonIPEchoAdminLSPSelAddress_Type.__name__ = "InetAddress"
_CrttMonIPEchoAdminLSPSelAddress_Object = MibTableColumn
crttMonIPEchoAdminLSPSelAddress = _CrttMonIPEchoAdminLSPSelAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 1, 1, 8),
    _CrttMonIPEchoAdminLSPSelAddress_Type()
)
crttMonIPEchoAdminLSPSelAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crttMonIPEchoAdminLSPSelAddress.setStatus("current")


class _CrttMonIPEchoAdminDscp_Type(DscpOrAny):
    """Custom type crttMonIPEchoAdminDscp based on DscpOrAny"""
    defaultValue = -1


_CrttMonIPEchoAdminDscp_Type.__name__ = "DscpOrAny"
_CrttMonIPEchoAdminDscp_Object = MibTableColumn
crttMonIPEchoAdminDscp = _CrttMonIPEchoAdminDscp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 1, 1, 9),
    _CrttMonIPEchoAdminDscp_Type()
)
crttMonIPEchoAdminDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crttMonIPEchoAdminDscp.setStatus("current")
_CrttMonIPEchoAdminFlowLabel_Type = IPv6FlowLabelOrAny
_CrttMonIPEchoAdminFlowLabel_Object = MibTableColumn
crttMonIPEchoAdminFlowLabel = _CrttMonIPEchoAdminFlowLabel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 1, 1, 10),
    _CrttMonIPEchoAdminFlowLabel_Type()
)
crttMonIPEchoAdminFlowLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crttMonIPEchoAdminFlowLabel.setStatus("current")
_CrttMonIPLatestRttOperTable_Object = MibTable
crttMonIPLatestRttOperTable = _CrttMonIPLatestRttOperTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 2)
)
if mibBuilder.loadTexts:
    crttMonIPLatestRttOperTable.setStatus("current")
_CrttMonIPLatestRttOperEntry_Object = MibTableRow
crttMonIPLatestRttOperEntry = _CrttMonIPLatestRttOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 2, 1)
)
crttMonIPLatestRttOperEntry.setIndexNames(
    (0, "CISCO-RTTMON-MIB", "rttMonCtrlAdminIndex"),
)
if mibBuilder.loadTexts:
    crttMonIPLatestRttOperEntry.setStatus("current")


class _CrttMonIPLatestRttOperAddressType_Type(InetAddressType):
    """Custom type crttMonIPLatestRttOperAddressType based on InetAddressType"""
    defaultValue = 0


_CrttMonIPLatestRttOperAddressType_Type.__name__ = "InetAddressType"
_CrttMonIPLatestRttOperAddressType_Object = MibTableColumn
crttMonIPLatestRttOperAddressType = _CrttMonIPLatestRttOperAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 2, 1, 1),
    _CrttMonIPLatestRttOperAddressType_Type()
)
crttMonIPLatestRttOperAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crttMonIPLatestRttOperAddressType.setStatus("current")


class _CrttMonIPLatestRttOperAddress_Type(InetAddress):
    """Custom type crttMonIPLatestRttOperAddress based on InetAddress"""
    defaultValue = OctetString("")


_CrttMonIPLatestRttOperAddress_Type.__name__ = "InetAddress"
_CrttMonIPLatestRttOperAddress_Object = MibTableColumn
crttMonIPLatestRttOperAddress = _CrttMonIPLatestRttOperAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 2, 1, 2),
    _CrttMonIPLatestRttOperAddress_Type()
)
crttMonIPLatestRttOperAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crttMonIPLatestRttOperAddress.setStatus("current")
_CrttMonIPEchoPathAdminTable_Object = MibTable
crttMonIPEchoPathAdminTable = _CrttMonIPEchoPathAdminTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 3)
)
if mibBuilder.loadTexts:
    crttMonIPEchoPathAdminTable.setStatus("current")
_CrttMonIPEchoPathAdminEntry_Object = MibTableRow
crttMonIPEchoPathAdminEntry = _CrttMonIPEchoPathAdminEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 3, 1)
)
if mibBuilder.loadTexts:
    crttMonIPEchoPathAdminEntry.setStatus("current")


class _CrttMonIPEchoPathAdminHopAddrType_Type(InetAddressType):
    """Custom type crttMonIPEchoPathAdminHopAddrType based on InetAddressType"""
    defaultValue = 0


_CrttMonIPEchoPathAdminHopAddrType_Type.__name__ = "InetAddressType"
_CrttMonIPEchoPathAdminHopAddrType_Object = MibTableColumn
crttMonIPEchoPathAdminHopAddrType = _CrttMonIPEchoPathAdminHopAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 3, 1, 1),
    _CrttMonIPEchoPathAdminHopAddrType_Type()
)
crttMonIPEchoPathAdminHopAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crttMonIPEchoPathAdminHopAddrType.setStatus("current")


class _CrttMonIPEchoPathAdminHopAddress_Type(InetAddress):
    """Custom type crttMonIPEchoPathAdminHopAddress based on InetAddress"""
    defaultValue = OctetString("")


_CrttMonIPEchoPathAdminHopAddress_Type.__name__ = "InetAddress"
_CrttMonIPEchoPathAdminHopAddress_Object = MibTableColumn
crttMonIPEchoPathAdminHopAddress = _CrttMonIPEchoPathAdminHopAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 3, 1, 2),
    _CrttMonIPEchoPathAdminHopAddress_Type()
)
crttMonIPEchoPathAdminHopAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crttMonIPEchoPathAdminHopAddress.setStatus("current")
_CrttMonIPStatsCollectTable_Object = MibTable
crttMonIPStatsCollectTable = _CrttMonIPStatsCollectTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 4)
)
if mibBuilder.loadTexts:
    crttMonIPStatsCollectTable.setStatus("current")
_CrttMonIPStatsCollectEntry_Object = MibTableRow
crttMonIPStatsCollectEntry = _CrttMonIPStatsCollectEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 4, 1)
)
if mibBuilder.loadTexts:
    crttMonIPStatsCollectEntry.setStatus("current")


class _CrttMonIPStatsCollectAddressType_Type(InetAddressType):
    """Custom type crttMonIPStatsCollectAddressType based on InetAddressType"""
    defaultValue = 0


_CrttMonIPStatsCollectAddressType_Type.__name__ = "InetAddressType"
_CrttMonIPStatsCollectAddressType_Object = MibTableColumn
crttMonIPStatsCollectAddressType = _CrttMonIPStatsCollectAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 4, 1, 1),
    _CrttMonIPStatsCollectAddressType_Type()
)
crttMonIPStatsCollectAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crttMonIPStatsCollectAddressType.setStatus("current")


class _CrttMonIPStatsCollectAddress_Type(InetAddress):
    """Custom type crttMonIPStatsCollectAddress based on InetAddress"""
    defaultValue = OctetString("")


_CrttMonIPStatsCollectAddress_Type.__name__ = "InetAddress"
_CrttMonIPStatsCollectAddress_Object = MibTableColumn
crttMonIPStatsCollectAddress = _CrttMonIPStatsCollectAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 4, 1, 2),
    _CrttMonIPStatsCollectAddress_Type()
)
crttMonIPStatsCollectAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crttMonIPStatsCollectAddress.setStatus("current")
_CrttMonIPLpdGrpStatsTable_Object = MibTable
crttMonIPLpdGrpStatsTable = _CrttMonIPLpdGrpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 5)
)
if mibBuilder.loadTexts:
    crttMonIPLpdGrpStatsTable.setStatus("current")
_CrttMonIPLpdGrpStatsEntry_Object = MibTableRow
crttMonIPLpdGrpStatsEntry = _CrttMonIPLpdGrpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 5, 1)
)
if mibBuilder.loadTexts:
    crttMonIPLpdGrpStatsEntry.setStatus("current")


class _CrttMonIPLpdGrpStatsTargetPEAddrType_Type(InetAddressType):
    """Custom type crttMonIPLpdGrpStatsTargetPEAddrType based on InetAddressType"""
    defaultValue = 0


_CrttMonIPLpdGrpStatsTargetPEAddrType_Type.__name__ = "InetAddressType"
_CrttMonIPLpdGrpStatsTargetPEAddrType_Object = MibTableColumn
crttMonIPLpdGrpStatsTargetPEAddrType = _CrttMonIPLpdGrpStatsTargetPEAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 5, 1, 1),
    _CrttMonIPLpdGrpStatsTargetPEAddrType_Type()
)
crttMonIPLpdGrpStatsTargetPEAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crttMonIPLpdGrpStatsTargetPEAddrType.setStatus("current")


class _CrttMonIPLpdGrpStatsTargetPEAddr_Type(InetAddress):
    """Custom type crttMonIPLpdGrpStatsTargetPEAddr based on InetAddress"""
    defaultValue = OctetString("")


_CrttMonIPLpdGrpStatsTargetPEAddr_Type.__name__ = "InetAddress"
_CrttMonIPLpdGrpStatsTargetPEAddr_Object = MibTableColumn
crttMonIPLpdGrpStatsTargetPEAddr = _CrttMonIPLpdGrpStatsTargetPEAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 5, 1, 2),
    _CrttMonIPLpdGrpStatsTargetPEAddr_Type()
)
crttMonIPLpdGrpStatsTargetPEAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crttMonIPLpdGrpStatsTargetPEAddr.setStatus("current")
_CrttMonIPHistoryCollectionTable_Object = MibTable
crttMonIPHistoryCollectionTable = _CrttMonIPHistoryCollectionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 6)
)
if mibBuilder.loadTexts:
    crttMonIPHistoryCollectionTable.setStatus("current")
_CrttMonIPHistoryCollectionEntry_Object = MibTableRow
crttMonIPHistoryCollectionEntry = _CrttMonIPHistoryCollectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 6, 1)
)
if mibBuilder.loadTexts:
    crttMonIPHistoryCollectionEntry.setStatus("current")


class _CrttMonIPHistoryCollectionAddrType_Type(InetAddressType):
    """Custom type crttMonIPHistoryCollectionAddrType based on InetAddressType"""
    defaultValue = 0


_CrttMonIPHistoryCollectionAddrType_Type.__name__ = "InetAddressType"
_CrttMonIPHistoryCollectionAddrType_Object = MibTableColumn
crttMonIPHistoryCollectionAddrType = _CrttMonIPHistoryCollectionAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 6, 1, 1),
    _CrttMonIPHistoryCollectionAddrType_Type()
)
crttMonIPHistoryCollectionAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crttMonIPHistoryCollectionAddrType.setStatus("current")


class _CrttMonIPHistoryCollectionAddress_Type(InetAddress):
    """Custom type crttMonIPHistoryCollectionAddress based on InetAddress"""
    defaultValue = OctetString("")


_CrttMonIPHistoryCollectionAddress_Type.__name__ = "InetAddress"
_CrttMonIPHistoryCollectionAddress_Object = MibTableColumn
crttMonIPHistoryCollectionAddress = _CrttMonIPHistoryCollectionAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 6, 1, 2),
    _CrttMonIPHistoryCollectionAddress_Type()
)
crttMonIPHistoryCollectionAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crttMonIPHistoryCollectionAddress.setStatus("current")
_CipslaPercentileConfigTable_Object = MibTable
cipslaPercentileConfigTable = _CipslaPercentileConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 7)
)
if mibBuilder.loadTexts:
    cipslaPercentileConfigTable.setStatus("current")
_CipslaPercentileConfigEntry_Object = MibTableRow
cipslaPercentileConfigEntry = _CipslaPercentileConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 7, 1)
)
cipslaPercentileConfigEntry.setIndexNames(
    (0, "CISCO-RTTMON-MIB", "rttMonCtrlAdminIndex"),
)
if mibBuilder.loadTexts:
    cipslaPercentileConfigEntry.setStatus("current")


class _CipslaPercentileRTT_Type(Integer32):
    """Custom type cipslaPercentileRTT based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(90, 100),
    )


_CipslaPercentileRTT_Type.__name__ = "Integer32"
_CipslaPercentileRTT_Object = MibTableColumn
cipslaPercentileRTT = _CipslaPercentileRTT_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 7, 1, 1),
    _CipslaPercentileRTT_Type()
)
cipslaPercentileRTT.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaPercentileRTT.setStatus("current")
if mibBuilder.loadTexts:
    cipslaPercentileRTT.setUnits("percent")


class _CipslaPercentileOWSD_Type(Integer32):
    """Custom type cipslaPercentileOWSD based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(90, 100),
    )


_CipslaPercentileOWSD_Type.__name__ = "Integer32"
_CipslaPercentileOWSD_Object = MibTableColumn
cipslaPercentileOWSD = _CipslaPercentileOWSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 7, 1, 2),
    _CipslaPercentileOWSD_Type()
)
cipslaPercentileOWSD.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaPercentileOWSD.setStatus("current")
if mibBuilder.loadTexts:
    cipslaPercentileOWSD.setUnits("percent")


class _CipslaPercentileOWDS_Type(Integer32):
    """Custom type cipslaPercentileOWDS based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(90, 100),
    )


_CipslaPercentileOWDS_Type.__name__ = "Integer32"
_CipslaPercentileOWDS_Object = MibTableColumn
cipslaPercentileOWDS = _CipslaPercentileOWDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 7, 1, 3),
    _CipslaPercentileOWDS_Type()
)
cipslaPercentileOWDS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaPercentileOWDS.setStatus("current")
if mibBuilder.loadTexts:
    cipslaPercentileOWDS.setUnits("percent")


class _CipslaPercentileJitterSD_Type(Integer32):
    """Custom type cipslaPercentileJitterSD based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(90, 100),
    )


_CipslaPercentileJitterSD_Type.__name__ = "Integer32"
_CipslaPercentileJitterSD_Object = MibTableColumn
cipslaPercentileJitterSD = _CipslaPercentileJitterSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 7, 1, 4),
    _CipslaPercentileJitterSD_Type()
)
cipslaPercentileJitterSD.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaPercentileJitterSD.setStatus("current")
if mibBuilder.loadTexts:
    cipslaPercentileJitterSD.setUnits("percent")


class _CipslaPercentileJitterDS_Type(Integer32):
    """Custom type cipslaPercentileJitterDS based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(90, 100),
    )


_CipslaPercentileJitterDS_Type.__name__ = "Integer32"
_CipslaPercentileJitterDS_Object = MibTableColumn
cipslaPercentileJitterDS = _CipslaPercentileJitterDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 7, 1, 5),
    _CipslaPercentileJitterDS_Type()
)
cipslaPercentileJitterDS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaPercentileJitterDS.setStatus("current")
if mibBuilder.loadTexts:
    cipslaPercentileJitterDS.setUnits("percent")


class _CipslaPercentileJitterAvg_Type(Integer32):
    """Custom type cipslaPercentileJitterAvg based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(90, 100),
    )


_CipslaPercentileJitterAvg_Type.__name__ = "Integer32"
_CipslaPercentileJitterAvg_Object = MibTableColumn
cipslaPercentileJitterAvg = _CipslaPercentileJitterAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 7, 1, 6),
    _CipslaPercentileJitterAvg_Type()
)
cipslaPercentileJitterAvg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaPercentileJitterAvg.setStatus("current")
if mibBuilder.loadTexts:
    cipslaPercentileJitterAvg.setUnits("percent")
_CipslaPercentileLatestStatsTable_Object = MibTable
cipslaPercentileLatestStatsTable = _CipslaPercentileLatestStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 8)
)
if mibBuilder.loadTexts:
    cipslaPercentileLatestStatsTable.setStatus("current")
_CipslaPercentileLatestStatsEntry_Object = MibTableRow
cipslaPercentileLatestStatsEntry = _CipslaPercentileLatestStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 8, 1)
)
cipslaPercentileLatestStatsEntry.setIndexNames(
    (0, "CISCO-RTTMON-IP-EXT-MIB", "cipslaPercentileTypeVar"),
    (0, "CISCO-RTTMON-MIB", "rttMonCtrlAdminIndex"),
)
if mibBuilder.loadTexts:
    cipslaPercentileLatestStatsEntry.setStatus("current")


class _CipslaPercentileTypeVar_Type(CipslaPercentileVar):
    """Custom type cipslaPercentileTypeVar based on CipslaPercentileVar"""
    subtypeSpec = CipslaPercentileVar.subtypeSpec
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
        *(("rtt", 1),
          ("owsd", 2),
          ("owds", 3),
          ("jittersd", 4),
          ("jitterds", 5),
          ("jitteravg", 6))
    )


_CipslaPercentileTypeVar_Type.__name__ = "CipslaPercentileVar"
_CipslaPercentileTypeVar_Object = MibTableColumn
cipslaPercentileTypeVar = _CipslaPercentileTypeVar_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 8, 1, 1),
    _CipslaPercentileTypeVar_Type()
)
cipslaPercentileTypeVar.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cipslaPercentileTypeVar.setStatus("current")
_CipslaPercentileLatestMin_Type = Gauge32
_CipslaPercentileLatestMin_Object = MibTableColumn
cipslaPercentileLatestMin = _CipslaPercentileLatestMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 8, 1, 2),
    _CipslaPercentileLatestMin_Type()
)
cipslaPercentileLatestMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipslaPercentileLatestMin.setStatus("current")
_CipslaPercentileLatestMax_Type = Gauge32
_CipslaPercentileLatestMax_Object = MibTableColumn
cipslaPercentileLatestMax = _CipslaPercentileLatestMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 8, 1, 3),
    _CipslaPercentileLatestMax_Type()
)
cipslaPercentileLatestMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipslaPercentileLatestMax.setStatus("current")
_CipslaPercentileLatestAvg_Type = Gauge32
_CipslaPercentileLatestAvg_Object = MibTableColumn
cipslaPercentileLatestAvg = _CipslaPercentileLatestAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 8, 1, 4),
    _CipslaPercentileLatestAvg_Type()
)
cipslaPercentileLatestAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipslaPercentileLatestAvg.setStatus("current")
_CipslaPercentileLatestNum_Type = Gauge32
_CipslaPercentileLatestNum_Object = MibTableColumn
cipslaPercentileLatestNum = _CipslaPercentileLatestNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 8, 1, 5),
    _CipslaPercentileLatestNum_Type()
)
cipslaPercentileLatestNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipslaPercentileLatestNum.setStatus("current")
if mibBuilder.loadTexts:
    cipslaPercentileLatestNum.setUnits("packets")
_CipslaPercentileLatestSum_Type = Gauge32
_CipslaPercentileLatestSum_Object = MibTableColumn
cipslaPercentileLatestSum = _CipslaPercentileLatestSum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 8, 1, 6),
    _CipslaPercentileLatestSum_Type()
)
cipslaPercentileLatestSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipslaPercentileLatestSum.setStatus("current")
_CipslaPercentileLatestSum2_Type = Gauge32
_CipslaPercentileLatestSum2_Object = MibTableColumn
cipslaPercentileLatestSum2 = _CipslaPercentileLatestSum2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 8, 1, 7),
    _CipslaPercentileLatestSum2_Type()
)
cipslaPercentileLatestSum2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipslaPercentileLatestSum2.setStatus("current")
_CiscoRttMonIPExtMibConformance_ObjectIdentity = ObjectIdentity
ciscoRttMonIPExtMibConformance = _CiscoRttMonIPExtMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 572, 2)
)
_CiscoRttMonIPExtMibCompliances_ObjectIdentity = ObjectIdentity
ciscoRttMonIPExtMibCompliances = _CiscoRttMonIPExtMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 572, 2, 1)
)
_CiscoRttMonIPExtMibGroups_ObjectIdentity = ObjectIdentity
ciscoRttMonIPExtMibGroups = _CiscoRttMonIPExtMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 572, 2, 2)
)
rttMonEchoAdminEntry.registerAugmentions(
    ("CISCO-RTTMON-IP-EXT-MIB",
     "crttMonIPEchoAdminEntry")
)
crttMonIPEchoAdminEntry.setIndexNames(*rttMonEchoAdminEntry.getIndexNames())
rttMonEchoPathAdminEntry.registerAugmentions(
    ("CISCO-RTTMON-IP-EXT-MIB",
     "crttMonIPEchoPathAdminEntry")
)
crttMonIPEchoPathAdminEntry.setIndexNames(*rttMonEchoPathAdminEntry.getIndexNames())
rttMonStatsCollectEntry.registerAugmentions(
    ("CISCO-RTTMON-IP-EXT-MIB",
     "crttMonIPStatsCollectEntry")
)
crttMonIPStatsCollectEntry.setIndexNames(*rttMonStatsCollectEntry.getIndexNames())
rttMonLpdGrpStatsEntry.registerAugmentions(
    ("CISCO-RTTMON-IP-EXT-MIB",
     "crttMonIPLpdGrpStatsEntry")
)
crttMonIPLpdGrpStatsEntry.setIndexNames(*rttMonLpdGrpStatsEntry.getIndexNames())
rttMonHistoryCollectionEntry.registerAugmentions(
    ("CISCO-RTTMON-IP-EXT-MIB",
     "crttMonIPHistoryCollectionEntry")
)
crttMonIPHistoryCollectionEntry.setIndexNames(*rttMonHistoryCollectionEntry.getIndexNames())

# Managed Objects groups

ciscoIPExtCtrlGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 572, 2, 2, 1)
)
ciscoIPExtCtrlGroupRev1.setObjects(
      *(("CISCO-RTTMON-IP-EXT-MIB", "crttMonIPEchoAdminTargetAddrType"),
        ("CISCO-RTTMON-IP-EXT-MIB", "crttMonIPEchoAdminTargetAddress"),
        ("CISCO-RTTMON-IP-EXT-MIB", "crttMonIPEchoAdminSourceAddrType"),
        ("CISCO-RTTMON-IP-EXT-MIB", "crttMonIPEchoAdminSourceAddress"),
        ("CISCO-RTTMON-IP-EXT-MIB", "crttMonIPEchoAdminNameServerAddrType"),
        ("CISCO-RTTMON-IP-EXT-MIB", "crttMonIPEchoAdminNameServerAddress"),
        ("CISCO-RTTMON-IP-EXT-MIB", "crttMonIPEchoAdminLSPSelAddrType"),
        ("CISCO-RTTMON-IP-EXT-MIB", "crttMonIPEchoAdminLSPSelAddress"),
        ("CISCO-RTTMON-IP-EXT-MIB", "crttMonIPEchoAdminDscp"),
        ("CISCO-RTTMON-IP-EXT-MIB", "crttMonIPEchoAdminFlowLabel"),
        ("CISCO-RTTMON-IP-EXT-MIB", "crttMonIPLatestRttOperAddressType"),
        ("CISCO-RTTMON-IP-EXT-MIB", "crttMonIPLatestRttOperAddress"),
        ("CISCO-RTTMON-IP-EXT-MIB", "crttMonIPEchoPathAdminHopAddrType"),
        ("CISCO-RTTMON-IP-EXT-MIB", "crttMonIPEchoPathAdminHopAddress"),
        ("CISCO-RTTMON-IP-EXT-MIB", "crttMonIPStatsCollectAddressType"),
        ("CISCO-RTTMON-IP-EXT-MIB", "crttMonIPStatsCollectAddress"),
        ("CISCO-RTTMON-IP-EXT-MIB", "crttMonIPLpdGrpStatsTargetPEAddrType"),
        ("CISCO-RTTMON-IP-EXT-MIB", "crttMonIPLpdGrpStatsTargetPEAddr"),
        ("CISCO-RTTMON-IP-EXT-MIB", "crttMonIPHistoryCollectionAddrType"),
        ("CISCO-RTTMON-IP-EXT-MIB", "crttMonIPHistoryCollectionAddress"))
)
if mibBuilder.loadTexts:
    ciscoIPExtCtrlGroupRev1.setStatus("current")

ciscoIPExtCtrlGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 572, 2, 2, 2)
)
ciscoIPExtCtrlGroupRev2.setObjects(
      *(("CISCO-RTTMON-IP-EXT-MIB", "cipslaPercentileRTT"),
        ("CISCO-RTTMON-IP-EXT-MIB", "cipslaPercentileOWSD"),
        ("CISCO-RTTMON-IP-EXT-MIB", "cipslaPercentileOWDS"),
        ("CISCO-RTTMON-IP-EXT-MIB", "cipslaPercentileJitterSD"),
        ("CISCO-RTTMON-IP-EXT-MIB", "cipslaPercentileJitterDS"),
        ("CISCO-RTTMON-IP-EXT-MIB", "cipslaPercentileJitterAvg"),
        ("CISCO-RTTMON-IP-EXT-MIB", "cipslaPercentileLatestMin"),
        ("CISCO-RTTMON-IP-EXT-MIB", "cipslaPercentileLatestMax"),
        ("CISCO-RTTMON-IP-EXT-MIB", "cipslaPercentileLatestAvg"),
        ("CISCO-RTTMON-IP-EXT-MIB", "cipslaPercentileLatestNum"),
        ("CISCO-RTTMON-IP-EXT-MIB", "cipslaPercentileLatestSum"),
        ("CISCO-RTTMON-IP-EXT-MIB", "cipslaPercentileLatestSum2"))
)
if mibBuilder.loadTexts:
    ciscoIPExtCtrlGroupRev2.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoRttMonIPExtMibComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 572, 2, 1, 1)
)
ciscoRttMonIPExtMibComplianceRev1.setObjects(
    ("CISCO-RTTMON-IP-EXT-MIB", "ciscoIPExtCtrlGroupRev1")
)
if mibBuilder.loadTexts:
    ciscoRttMonIPExtMibComplianceRev1.setStatus(
        "deprecated"
    )

ciscoRttMonIPExtMibComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 572, 2, 1, 2)
)
ciscoRttMonIPExtMibComplianceRev2.setObjects(
      *(("CISCO-RTTMON-IP-EXT-MIB", "ciscoIPExtCtrlGroupRev1"),
        ("CISCO-RTTMON-IP-EXT-MIB", "ciscoIPExtCtrlGroupRev2"))
)
if mibBuilder.loadTexts:
    ciscoRttMonIPExtMibComplianceRev2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-RTTMON-IP-EXT-MIB",
    **{"ciscoRttMonIPExtMIB": ciscoRttMonIPExtMIB,
       "crttMonIPExtObjects": crttMonIPExtObjects,
       "crttMonIPEchoAdminTable": crttMonIPEchoAdminTable,
       "crttMonIPEchoAdminEntry": crttMonIPEchoAdminEntry,
       "crttMonIPEchoAdminTargetAddrType": crttMonIPEchoAdminTargetAddrType,
       "crttMonIPEchoAdminTargetAddress": crttMonIPEchoAdminTargetAddress,
       "crttMonIPEchoAdminSourceAddrType": crttMonIPEchoAdminSourceAddrType,
       "crttMonIPEchoAdminSourceAddress": crttMonIPEchoAdminSourceAddress,
       "crttMonIPEchoAdminNameServerAddrType": crttMonIPEchoAdminNameServerAddrType,
       "crttMonIPEchoAdminNameServerAddress": crttMonIPEchoAdminNameServerAddress,
       "crttMonIPEchoAdminLSPSelAddrType": crttMonIPEchoAdminLSPSelAddrType,
       "crttMonIPEchoAdminLSPSelAddress": crttMonIPEchoAdminLSPSelAddress,
       "crttMonIPEchoAdminDscp": crttMonIPEchoAdminDscp,
       "crttMonIPEchoAdminFlowLabel": crttMonIPEchoAdminFlowLabel,
       "crttMonIPLatestRttOperTable": crttMonIPLatestRttOperTable,
       "crttMonIPLatestRttOperEntry": crttMonIPLatestRttOperEntry,
       "crttMonIPLatestRttOperAddressType": crttMonIPLatestRttOperAddressType,
       "crttMonIPLatestRttOperAddress": crttMonIPLatestRttOperAddress,
       "crttMonIPEchoPathAdminTable": crttMonIPEchoPathAdminTable,
       "crttMonIPEchoPathAdminEntry": crttMonIPEchoPathAdminEntry,
       "crttMonIPEchoPathAdminHopAddrType": crttMonIPEchoPathAdminHopAddrType,
       "crttMonIPEchoPathAdminHopAddress": crttMonIPEchoPathAdminHopAddress,
       "crttMonIPStatsCollectTable": crttMonIPStatsCollectTable,
       "crttMonIPStatsCollectEntry": crttMonIPStatsCollectEntry,
       "crttMonIPStatsCollectAddressType": crttMonIPStatsCollectAddressType,
       "crttMonIPStatsCollectAddress": crttMonIPStatsCollectAddress,
       "crttMonIPLpdGrpStatsTable": crttMonIPLpdGrpStatsTable,
       "crttMonIPLpdGrpStatsEntry": crttMonIPLpdGrpStatsEntry,
       "crttMonIPLpdGrpStatsTargetPEAddrType": crttMonIPLpdGrpStatsTargetPEAddrType,
       "crttMonIPLpdGrpStatsTargetPEAddr": crttMonIPLpdGrpStatsTargetPEAddr,
       "crttMonIPHistoryCollectionTable": crttMonIPHistoryCollectionTable,
       "crttMonIPHistoryCollectionEntry": crttMonIPHistoryCollectionEntry,
       "crttMonIPHistoryCollectionAddrType": crttMonIPHistoryCollectionAddrType,
       "crttMonIPHistoryCollectionAddress": crttMonIPHistoryCollectionAddress,
       "cipslaPercentileConfigTable": cipslaPercentileConfigTable,
       "cipslaPercentileConfigEntry": cipslaPercentileConfigEntry,
       "cipslaPercentileRTT": cipslaPercentileRTT,
       "cipslaPercentileOWSD": cipslaPercentileOWSD,
       "cipslaPercentileOWDS": cipslaPercentileOWDS,
       "cipslaPercentileJitterSD": cipslaPercentileJitterSD,
       "cipslaPercentileJitterDS": cipslaPercentileJitterDS,
       "cipslaPercentileJitterAvg": cipslaPercentileJitterAvg,
       "cipslaPercentileLatestStatsTable": cipslaPercentileLatestStatsTable,
       "cipslaPercentileLatestStatsEntry": cipslaPercentileLatestStatsEntry,
       "cipslaPercentileTypeVar": cipslaPercentileTypeVar,
       "cipslaPercentileLatestMin": cipslaPercentileLatestMin,
       "cipslaPercentileLatestMax": cipslaPercentileLatestMax,
       "cipslaPercentileLatestAvg": cipslaPercentileLatestAvg,
       "cipslaPercentileLatestNum": cipslaPercentileLatestNum,
       "cipslaPercentileLatestSum": cipslaPercentileLatestSum,
       "cipslaPercentileLatestSum2": cipslaPercentileLatestSum2,
       "ciscoRttMonIPExtMibConformance": ciscoRttMonIPExtMibConformance,
       "ciscoRttMonIPExtMibCompliances": ciscoRttMonIPExtMibCompliances,
       "ciscoRttMonIPExtMibComplianceRev1": ciscoRttMonIPExtMibComplianceRev1,
       "ciscoRttMonIPExtMibComplianceRev2": ciscoRttMonIPExtMibComplianceRev2,
       "ciscoRttMonIPExtMibGroups": ciscoRttMonIPExtMibGroups,
       "ciscoIPExtCtrlGroupRev1": ciscoIPExtCtrlGroupRev1,
       "ciscoIPExtCtrlGroupRev2": ciscoIPExtCtrlGroupRev2}
)
