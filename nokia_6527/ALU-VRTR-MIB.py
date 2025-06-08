# SNMP MIB module (ALU-VRTR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_6527/ALU-VRTR-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 17:45:25 2025
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

(aluSARConfs,
 aluSARMIBModules,
 aluSARNotifyPrefix,
 aluSARObjs) = mibBuilder.importSymbols(
    "ALU-SAR-GLOBAL-MIB",
    "aluSARConfs",
    "aluSARMIBModules",
    "aluSARNotifyPrefix",
    "aluSARObjs")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(MplsLabel,) = mibBuilder.importSymbols(
    "MPLS-LSR-MIB",
    "MplsLabel")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")

(tmnxCardHwIndex,) = mibBuilder.importSymbols(
    "TIMETRA-CHASSIS-MIB",
    "tmnxCardHwIndex")

(vRtrMplsIfStatEntry,) = mibBuilder.importSymbols(
    "TIMETRA-MPLS-MIB",
    "vRtrMplsIfStatEntry")

(vRtrPimNgIfRxPkts,
 vRtrPimNgNotifyGroupAddr,
 vRtrPimNgNotifyGroupAddrType,
 vRtrPimNgNotifyMsgType) = mibBuilder.importSymbols(
    "TIMETRA-PIM-NG-MIB",
    "vRtrPimNgIfRxPkts",
    "vRtrPimNgNotifyGroupAddr",
    "vRtrPimNgNotifyGroupAddrType",
    "vRtrPimNgNotifyMsgType")

(TLNamedItemOrEmpty,
 TNamedItemOrEmpty,
 TPortSchedulerCIR,
 TPortSchedulerPIR,
 TQueueId,
 TTcpUdpPort) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TLNamedItemOrEmpty",
    "TNamedItemOrEmpty",
    "TPortSchedulerCIR",
    "TPortSchedulerPIR",
    "TQueueId",
    "TTcpUdpPort")

(tmnxTwampSrvNotifClientAddr,
 tmnxTwampSrvNotifClientAddrType) = mibBuilder.importSymbols(
    "TIMETRA-TWAMP-MIB",
    "tmnxTwampSrvNotifClientAddr",
    "tmnxTwampSrvNotifClientAddrType")

(vRtrConfExtEntry,
 vRtrID,
 vRtrIfEntry,
 vRtrIfExtEntry,
 vRtrIfIndex,
 vRtrIfStatsEntry) = mibBuilder.importSymbols(
    "TIMETRA-VRTR-MIB",
    "vRtrConfExtEntry",
    "vRtrID",
    "vRtrIfEntry",
    "vRtrIfExtEntry",
    "vRtrIfIndex",
    "vRtrIfStatsEntry")


# MODULE-IDENTITY

aluVRTRMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 1, 1, 3, 7)
)
if mibBuilder.loadTexts:
    aluVRTRMIBModule.setRevisions(
        ("1908-12-16 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AluVrtrIfMIBConformance_ObjectIdentity = ObjectIdentity
aluVrtrIfMIBConformance = _AluVrtrIfMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 8)
)
_AluVrtrIfConformance_ObjectIdentity = ObjectIdentity
aluVrtrIfConformance = _AluVrtrIfConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 8, 1)
)
_AluVrtrIfCompliances_ObjectIdentity = ObjectIdentity
aluVrtrIfCompliances = _AluVrtrIfCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 8, 1, 1)
)
_AluVrtrIfComp7705_ObjectIdentity = ObjectIdentity
aluVrtrIfComp7705 = _AluVrtrIfComp7705_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 8, 1, 1, 1)
)
_AluVrtrIfGroups_ObjectIdentity = ObjectIdentity
aluVrtrIfGroups = _AluVrtrIfGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 8, 1, 2)
)
_AluVrtrIpAddrMIBConformance_ObjectIdentity = ObjectIdentity
aluVrtrIpAddrMIBConformance = _AluVrtrIpAddrMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 14)
)
_AluVrtrIpAddrConformance_ObjectIdentity = ObjectIdentity
aluVrtrIpAddrConformance = _AluVrtrIpAddrConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 14, 1)
)
_AluVrtrIpAddrCompliances_ObjectIdentity = ObjectIdentity
aluVrtrIpAddrCompliances = _AluVrtrIpAddrCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 14, 1, 1)
)
_AluVrtrIpAddrComp7705_ObjectIdentity = ObjectIdentity
aluVrtrIpAddrComp7705 = _AluVrtrIpAddrComp7705_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 14, 1, 1, 1)
)
_AluVrtrIpAddrGroups_ObjectIdentity = ObjectIdentity
aluVrtrIpAddrGroups = _AluVrtrIpAddrGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 14, 1, 2)
)
_AluTwampMIBConformance_ObjectIdentity = ObjectIdentity
aluTwampMIBConformance = _AluTwampMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 15)
)
_AluTwampConformance_ObjectIdentity = ObjectIdentity
aluTwampConformance = _AluTwampConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 15, 1)
)
_AluTwampComplianceObjs_ObjectIdentity = ObjectIdentity
aluTwampComplianceObjs = _AluTwampComplianceObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 15, 1, 1)
)
_AluTwampGroupObjs_ObjectIdentity = ObjectIdentity
aluTwampGroupObjs = _AluTwampGroupObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 15, 1, 2)
)
_AluTwampV6v0GroupObjs_ObjectIdentity = ObjectIdentity
aluTwampV6v0GroupObjs = _AluTwampV6v0GroupObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 15, 1, 2, 1)
)
_AluVrtrConfMIBConformance_ObjectIdentity = ObjectIdentity
aluVrtrConfMIBConformance = _AluVrtrConfMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 18)
)
_AluVrtrConfConformance_ObjectIdentity = ObjectIdentity
aluVrtrConfConformance = _AluVrtrConfConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 18, 1)
)
_AluVrtrConfConformanceObjs_ObjectIdentity = ObjectIdentity
aluVrtrConfConformanceObjs = _AluVrtrConfConformanceObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 18, 1, 1)
)
_AluVrtrConfGroupObjs_ObjectIdentity = ObjectIdentity
aluVrtrConfGroupObjs = _AluVrtrConfGroupObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 18, 1, 2)
)
_AluVrtrConfV6V0GroupObjs_ObjectIdentity = ObjectIdentity
aluVrtrConfV6V0GroupObjs = _AluVrtrConfV6V0GroupObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 18, 1, 2, 1)
)
_AluVrtrIfObjs_ObjectIdentity = ObjectIdentity
aluVrtrIfObjs = _AluVrtrIfObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8)
)
_AluVrtrIfTable_Object = MibTable
aluVrtrIfTable = _AluVrtrIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 1)
)
if mibBuilder.loadTexts:
    aluVrtrIfTable.setStatus("current")
_AluVrtrIfEntry_Object = MibTableRow
aluVrtrIfEntry = _AluVrtrIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 1, 1)
)
if mibBuilder.loadTexts:
    aluVrtrIfEntry.setStatus("current")
_AluVrtrIf1588Ptp_Type = TruthValue
_AluVrtrIf1588Ptp_Object = MibTableColumn
aluVrtrIf1588Ptp = _AluVrtrIf1588Ptp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 1, 1, 1),
    _AluVrtrIf1588Ptp_Type()
)
aluVrtrIf1588Ptp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVrtrIf1588Ptp.setStatus("current")
_AluVRtrIfStatsTable_Object = MibTable
aluVRtrIfStatsTable = _AluVRtrIfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2)
)
if mibBuilder.loadTexts:
    aluVRtrIfStatsTable.setStatus("current")
_AluVRtrIfStatsEntry_Object = MibTableRow
aluVRtrIfStatsEntry = _AluVRtrIfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1)
)
if mibBuilder.loadTexts:
    aluVRtrIfStatsEntry.setStatus("current")
_AluVRtrIfRxV4Pkts_Type = Counter64
_AluVRtrIfRxV4Pkts_Object = MibTableColumn
aluVRtrIfRxV4Pkts = _AluVRtrIfRxV4Pkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 1),
    _AluVRtrIfRxV4Pkts_Type()
)
aluVRtrIfRxV4Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfRxV4Pkts.setStatus("current")
_AluVRtrIfRxV4Bytes_Type = Counter64
_AluVRtrIfRxV4Bytes_Object = MibTableColumn
aluVRtrIfRxV4Bytes = _AluVRtrIfRxV4Bytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 2),
    _AluVRtrIfRxV4Bytes_Type()
)
aluVRtrIfRxV4Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfRxV4Bytes.setStatus("current")
_AluVRtrIfRxV6Pkts_Type = Counter64
_AluVRtrIfRxV6Pkts_Object = MibTableColumn
aluVRtrIfRxV6Pkts = _AluVRtrIfRxV6Pkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 3),
    _AluVRtrIfRxV6Pkts_Type()
)
aluVRtrIfRxV6Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfRxV6Pkts.setStatus("current")
_AluVRtrIfRxV6Bytes_Type = Counter64
_AluVRtrIfRxV6Bytes_Object = MibTableColumn
aluVRtrIfRxV6Bytes = _AluVRtrIfRxV6Bytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 4),
    _AluVRtrIfRxV6Bytes_Type()
)
aluVRtrIfRxV6Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfRxV6Bytes.setStatus("current")
_AluVRtrIfRxV4DiscardPkts_Type = Counter64
_AluVRtrIfRxV4DiscardPkts_Object = MibTableColumn
aluVRtrIfRxV4DiscardPkts = _AluVRtrIfRxV4DiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 5),
    _AluVRtrIfRxV4DiscardPkts_Type()
)
aluVRtrIfRxV4DiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfRxV4DiscardPkts.setStatus("current")
_AluVRtrIfRxV4DiscardBytes_Type = Counter64
_AluVRtrIfRxV4DiscardBytes_Object = MibTableColumn
aluVRtrIfRxV4DiscardBytes = _AluVRtrIfRxV4DiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 6),
    _AluVRtrIfRxV4DiscardBytes_Type()
)
aluVRtrIfRxV4DiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfRxV4DiscardBytes.setStatus("current")
_AluVRtrIfRxV4DiscardInvHdrCRCPkts_Type = Counter64
_AluVRtrIfRxV4DiscardInvHdrCRCPkts_Object = MibTableColumn
aluVRtrIfRxV4DiscardInvHdrCRCPkts = _AluVRtrIfRxV4DiscardInvHdrCRCPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 7),
    _AluVRtrIfRxV4DiscardInvHdrCRCPkts_Type()
)
aluVRtrIfRxV4DiscardInvHdrCRCPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfRxV4DiscardInvHdrCRCPkts.setStatus("current")
_AluVRtrIfRxV4DiscardInvHdrCRCBytes_Type = Counter64
_AluVRtrIfRxV4DiscardInvHdrCRCBytes_Object = MibTableColumn
aluVRtrIfRxV4DiscardInvHdrCRCBytes = _AluVRtrIfRxV4DiscardInvHdrCRCBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 8),
    _AluVRtrIfRxV4DiscardInvHdrCRCBytes_Type()
)
aluVRtrIfRxV4DiscardInvHdrCRCBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfRxV4DiscardInvHdrCRCBytes.setStatus("current")
_AluVRtrIfRxV4DiscardInvLenPkts_Type = Counter64
_AluVRtrIfRxV4DiscardInvLenPkts_Object = MibTableColumn
aluVRtrIfRxV4DiscardInvLenPkts = _AluVRtrIfRxV4DiscardInvLenPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 9),
    _AluVRtrIfRxV4DiscardInvLenPkts_Type()
)
aluVRtrIfRxV4DiscardInvLenPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfRxV4DiscardInvLenPkts.setStatus("current")
_AluVRtrIfRxV4DiscardInvLenBytes_Type = Counter64
_AluVRtrIfRxV4DiscardInvLenBytes_Object = MibTableColumn
aluVRtrIfRxV4DiscardInvLenBytes = _AluVRtrIfRxV4DiscardInvLenBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 10),
    _AluVRtrIfRxV4DiscardInvLenBytes_Type()
)
aluVRtrIfRxV4DiscardInvLenBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfRxV4DiscardInvLenBytes.setStatus("current")
_AluVRtrIfRxV4DiscardInvGREProtPkts_Type = Counter64
_AluVRtrIfRxV4DiscardInvGREProtPkts_Object = MibTableColumn
aluVRtrIfRxV4DiscardInvGREProtPkts = _AluVRtrIfRxV4DiscardInvGREProtPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 11),
    _AluVRtrIfRxV4DiscardInvGREProtPkts_Type()
)
aluVRtrIfRxV4DiscardInvGREProtPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfRxV4DiscardInvGREProtPkts.setStatus("current")
_AluVRtrIfRxV4DiscardInvGREProtBytes_Type = Counter64
_AluVRtrIfRxV4DiscardInvGREProtBytes_Object = MibTableColumn
aluVRtrIfRxV4DiscardInvGREProtBytes = _AluVRtrIfRxV4DiscardInvGREProtBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 12),
    _AluVRtrIfRxV4DiscardInvGREProtBytes_Type()
)
aluVRtrIfRxV4DiscardInvGREProtBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfRxV4DiscardInvGREProtBytes.setStatus("current")
_AluVRtrIfRxV4DiscardDestUnreachPkts_Type = Counter64
_AluVRtrIfRxV4DiscardDestUnreachPkts_Object = MibTableColumn
aluVRtrIfRxV4DiscardDestUnreachPkts = _AluVRtrIfRxV4DiscardDestUnreachPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 13),
    _AluVRtrIfRxV4DiscardDestUnreachPkts_Type()
)
aluVRtrIfRxV4DiscardDestUnreachPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfRxV4DiscardDestUnreachPkts.setStatus("current")
_AluVRtrIfRxV4DiscardDestUnreachBytes_Type = Counter64
_AluVRtrIfRxV4DiscardDestUnreachBytes_Object = MibTableColumn
aluVRtrIfRxV4DiscardDestUnreachBytes = _AluVRtrIfRxV4DiscardDestUnreachBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 14),
    _AluVRtrIfRxV4DiscardDestUnreachBytes_Type()
)
aluVRtrIfRxV4DiscardDestUnreachBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfRxV4DiscardDestUnreachBytes.setStatus("current")
_AluVRtrIfRxV4DiscardInvMcastPkts_Type = Counter64
_AluVRtrIfRxV4DiscardInvMcastPkts_Object = MibTableColumn
aluVRtrIfRxV4DiscardInvMcastPkts = _AluVRtrIfRxV4DiscardInvMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 15),
    _AluVRtrIfRxV4DiscardInvMcastPkts_Type()
)
aluVRtrIfRxV4DiscardInvMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfRxV4DiscardInvMcastPkts.setStatus("current")
_AluVRtrIfRxV4DiscardInvMcastBytes_Type = Counter64
_AluVRtrIfRxV4DiscardInvMcastBytes_Object = MibTableColumn
aluVRtrIfRxV4DiscardInvMcastBytes = _AluVRtrIfRxV4DiscardInvMcastBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 16),
    _AluVRtrIfRxV4DiscardInvMcastBytes_Type()
)
aluVRtrIfRxV4DiscardInvMcastBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfRxV4DiscardInvMcastBytes.setStatus("current")
_AluVRtrIfRxV4DiscardDirectBcastPkts_Type = Counter64
_AluVRtrIfRxV4DiscardDirectBcastPkts_Object = MibTableColumn
aluVRtrIfRxV4DiscardDirectBcastPkts = _AluVRtrIfRxV4DiscardDirectBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 17),
    _AluVRtrIfRxV4DiscardDirectBcastPkts_Type()
)
aluVRtrIfRxV4DiscardDirectBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfRxV4DiscardDirectBcastPkts.setStatus("current")
_AluVRtrIfRxV4DiscardDirectBcastBytes_Type = Counter64
_AluVRtrIfRxV4DiscardDirectBcastBytes_Object = MibTableColumn
aluVRtrIfRxV4DiscardDirectBcastBytes = _AluVRtrIfRxV4DiscardDirectBcastBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 18),
    _AluVRtrIfRxV4DiscardDirectBcastBytes_Type()
)
aluVRtrIfRxV4DiscardDirectBcastBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfRxV4DiscardDirectBcastBytes.setStatus("current")
_AluVRtrIfRxV4DiscardSrcMartianAddrPkts_Type = Counter64
_AluVRtrIfRxV4DiscardSrcMartianAddrPkts_Object = MibTableColumn
aluVRtrIfRxV4DiscardSrcMartianAddrPkts = _AluVRtrIfRxV4DiscardSrcMartianAddrPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 19),
    _AluVRtrIfRxV4DiscardSrcMartianAddrPkts_Type()
)
aluVRtrIfRxV4DiscardSrcMartianAddrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfRxV4DiscardSrcMartianAddrPkts.setStatus("current")
_AluVRtrIfRxV4DiscardSrcMartianAddrBytes_Type = Counter64
_AluVRtrIfRxV4DiscardSrcMartianAddrBytes_Object = MibTableColumn
aluVRtrIfRxV4DiscardSrcMartianAddrBytes = _AluVRtrIfRxV4DiscardSrcMartianAddrBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 20),
    _AluVRtrIfRxV4DiscardSrcMartianAddrBytes_Type()
)
aluVRtrIfRxV4DiscardSrcMartianAddrBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfRxV4DiscardSrcMartianAddrBytes.setStatus("current")
_AluVRtrIfRxV4DiscardDestMartianAddrPkts_Type = Counter64
_AluVRtrIfRxV4DiscardDestMartianAddrPkts_Object = MibTableColumn
aluVRtrIfRxV4DiscardDestMartianAddrPkts = _AluVRtrIfRxV4DiscardDestMartianAddrPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 21),
    _AluVRtrIfRxV4DiscardDestMartianAddrPkts_Type()
)
aluVRtrIfRxV4DiscardDestMartianAddrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfRxV4DiscardDestMartianAddrPkts.setStatus("current")
_AluVRtrIfRxV4DiscardDestMartianAddrBytes_Type = Counter64
_AluVRtrIfRxV4DiscardDestMartianAddrBytes_Object = MibTableColumn
aluVRtrIfRxV4DiscardDestMartianAddrBytes = _AluVRtrIfRxV4DiscardDestMartianAddrBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 22),
    _AluVRtrIfRxV4DiscardDestMartianAddrBytes_Type()
)
aluVRtrIfRxV4DiscardDestMartianAddrBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfRxV4DiscardDestMartianAddrBytes.setStatus("current")
_AluVRtrIfRxV4DiscardBlackHolePkts_Type = Counter64
_AluVRtrIfRxV4DiscardBlackHolePkts_Object = MibTableColumn
aluVRtrIfRxV4DiscardBlackHolePkts = _AluVRtrIfRxV4DiscardBlackHolePkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 23),
    _AluVRtrIfRxV4DiscardBlackHolePkts_Type()
)
aluVRtrIfRxV4DiscardBlackHolePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfRxV4DiscardBlackHolePkts.setStatus("current")
_AluVRtrIfRxV4DiscardBlackHoleBytes_Type = Counter64
_AluVRtrIfRxV4DiscardBlackHoleBytes_Object = MibTableColumn
aluVRtrIfRxV4DiscardBlackHoleBytes = _AluVRtrIfRxV4DiscardBlackHoleBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 24),
    _AluVRtrIfRxV4DiscardBlackHoleBytes_Type()
)
aluVRtrIfRxV4DiscardBlackHoleBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfRxV4DiscardBlackHoleBytes.setStatus("current")
_AluVRtrIfRxV4DiscardFltrActionDropPkts_Type = Counter64
_AluVRtrIfRxV4DiscardFltrActionDropPkts_Object = MibTableColumn
aluVRtrIfRxV4DiscardFltrActionDropPkts = _AluVRtrIfRxV4DiscardFltrActionDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 25),
    _AluVRtrIfRxV4DiscardFltrActionDropPkts_Type()
)
aluVRtrIfRxV4DiscardFltrActionDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfRxV4DiscardFltrActionDropPkts.setStatus("current")
_AluVRtrIfRxV4DiscardFltrActionDropBytes_Type = Counter64
_AluVRtrIfRxV4DiscardFltrActionDropBytes_Object = MibTableColumn
aluVRtrIfRxV4DiscardFltrActionDropBytes = _AluVRtrIfRxV4DiscardFltrActionDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 26),
    _AluVRtrIfRxV4DiscardFltrActionDropBytes_Type()
)
aluVRtrIfRxV4DiscardFltrActionDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfRxV4DiscardFltrActionDropBytes.setStatus("current")
_AluVRtrIfRxV4DiscardFltrNxtHopUnreachPkts_Type = Counter64
_AluVRtrIfRxV4DiscardFltrNxtHopUnreachPkts_Object = MibTableColumn
aluVRtrIfRxV4DiscardFltrNxtHopUnreachPkts = _AluVRtrIfRxV4DiscardFltrNxtHopUnreachPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 27),
    _AluVRtrIfRxV4DiscardFltrNxtHopUnreachPkts_Type()
)
aluVRtrIfRxV4DiscardFltrNxtHopUnreachPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfRxV4DiscardFltrNxtHopUnreachPkts.setStatus("current")
_AluVRtrIfRxV4DiscardFltrNxtHopUnreachBytes_Type = Counter64
_AluVRtrIfRxV4DiscardFltrNxtHopUnreachBytes_Object = MibTableColumn
aluVRtrIfRxV4DiscardFltrNxtHopUnreachBytes = _AluVRtrIfRxV4DiscardFltrNxtHopUnreachBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 28),
    _AluVRtrIfRxV4DiscardFltrNxtHopUnreachBytes_Type()
)
aluVRtrIfRxV4DiscardFltrNxtHopUnreachBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfRxV4DiscardFltrNxtHopUnreachBytes.setStatus("current")
_AluVRtrIfRxV4DiscardFltrNxtHopNotDirectPkts_Type = Counter64
_AluVRtrIfRxV4DiscardFltrNxtHopNotDirectPkts_Object = MibTableColumn
aluVRtrIfRxV4DiscardFltrNxtHopNotDirectPkts = _AluVRtrIfRxV4DiscardFltrNxtHopNotDirectPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 29),
    _AluVRtrIfRxV4DiscardFltrNxtHopNotDirectPkts_Type()
)
aluVRtrIfRxV4DiscardFltrNxtHopNotDirectPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfRxV4DiscardFltrNxtHopNotDirectPkts.setStatus("current")
_AluVRtrIfRxV4DiscardFltrNxtHopNotDirectBytes_Type = Counter64
_AluVRtrIfRxV4DiscardFltrNxtHopNotDirectBytes_Object = MibTableColumn
aluVRtrIfRxV4DiscardFltrNxtHopNotDirectBytes = _AluVRtrIfRxV4DiscardFltrNxtHopNotDirectBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 30),
    _AluVRtrIfRxV4DiscardFltrNxtHopNotDirectBytes_Type()
)
aluVRtrIfRxV4DiscardFltrNxtHopNotDirectBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfRxV4DiscardFltrNxtHopNotDirectBytes.setStatus("current")
_AluVRtrIfRxV4DiscardTTLExpiredPkts_Type = Counter64
_AluVRtrIfRxV4DiscardTTLExpiredPkts_Object = MibTableColumn
aluVRtrIfRxV4DiscardTTLExpiredPkts = _AluVRtrIfRxV4DiscardTTLExpiredPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 31),
    _AluVRtrIfRxV4DiscardTTLExpiredPkts_Type()
)
aluVRtrIfRxV4DiscardTTLExpiredPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfRxV4DiscardTTLExpiredPkts.setStatus("current")
_AluVRtrIfRxV4DiscardTTLExpiredBytes_Type = Counter64
_AluVRtrIfRxV4DiscardTTLExpiredBytes_Object = MibTableColumn
aluVRtrIfRxV4DiscardTTLExpiredBytes = _AluVRtrIfRxV4DiscardTTLExpiredBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 32),
    _AluVRtrIfRxV4DiscardTTLExpiredBytes_Type()
)
aluVRtrIfRxV4DiscardTTLExpiredBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfRxV4DiscardTTLExpiredBytes.setStatus("current")
_AluVRtrIfRxV4DiscardSlowpathPkts_Type = Counter64
_AluVRtrIfRxV4DiscardSlowpathPkts_Object = MibTableColumn
aluVRtrIfRxV4DiscardSlowpathPkts = _AluVRtrIfRxV4DiscardSlowpathPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 33),
    _AluVRtrIfRxV4DiscardSlowpathPkts_Type()
)
aluVRtrIfRxV4DiscardSlowpathPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfRxV4DiscardSlowpathPkts.setStatus("current")
_AluVRtrIfRxV4DiscardSlowpathBytes_Type = Counter64
_AluVRtrIfRxV4DiscardSlowpathBytes_Object = MibTableColumn
aluVRtrIfRxV4DiscardSlowpathBytes = _AluVRtrIfRxV4DiscardSlowpathBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 34),
    _AluVRtrIfRxV4DiscardSlowpathBytes_Type()
)
aluVRtrIfRxV4DiscardSlowpathBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfRxV4DiscardSlowpathBytes.setStatus("current")
_AluVRtrIfRxV4DiscardMtuExceededPkts_Type = Counter64
_AluVRtrIfRxV4DiscardMtuExceededPkts_Object = MibTableColumn
aluVRtrIfRxV4DiscardMtuExceededPkts = _AluVRtrIfRxV4DiscardMtuExceededPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 35),
    _AluVRtrIfRxV4DiscardMtuExceededPkts_Type()
)
aluVRtrIfRxV4DiscardMtuExceededPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfRxV4DiscardMtuExceededPkts.setStatus("current")
_AluVRtrIfRxV4DiscardMtuExceededBytes_Type = Counter64
_AluVRtrIfRxV4DiscardMtuExceededBytes_Object = MibTableColumn
aluVRtrIfRxV4DiscardMtuExceededBytes = _AluVRtrIfRxV4DiscardMtuExceededBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 36),
    _AluVRtrIfRxV4DiscardMtuExceededBytes_Type()
)
aluVRtrIfRxV4DiscardMtuExceededBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfRxV4DiscardMtuExceededBytes.setStatus("current")
_AluVRtrIfRxV4DiscardQueuePkts_Type = Counter64
_AluVRtrIfRxV4DiscardQueuePkts_Object = MibTableColumn
aluVRtrIfRxV4DiscardQueuePkts = _AluVRtrIfRxV4DiscardQueuePkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 37),
    _AluVRtrIfRxV4DiscardQueuePkts_Type()
)
aluVRtrIfRxV4DiscardQueuePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfRxV4DiscardQueuePkts.setStatus("current")
_AluVRtrIfRxV4DiscardQueueBytes_Type = Counter64
_AluVRtrIfRxV4DiscardQueueBytes_Object = MibTableColumn
aluVRtrIfRxV4DiscardQueueBytes = _AluVRtrIfRxV4DiscardQueueBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 38),
    _AluVRtrIfRxV4DiscardQueueBytes_Type()
)
aluVRtrIfRxV4DiscardQueueBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfRxV4DiscardQueueBytes.setStatus("current")
_AluVRtrIfRxV4DiscardEncryptionPkts_Type = Counter64
_AluVRtrIfRxV4DiscardEncryptionPkts_Object = MibTableColumn
aluVRtrIfRxV4DiscardEncryptionPkts = _AluVRtrIfRxV4DiscardEncryptionPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 39),
    _AluVRtrIfRxV4DiscardEncryptionPkts_Type()
)
aluVRtrIfRxV4DiscardEncryptionPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfRxV4DiscardEncryptionPkts.setStatus("current")
_AluVRtrIfRxV4DiscardEncryptionBytes_Type = Counter64
_AluVRtrIfRxV4DiscardEncryptionBytes_Object = MibTableColumn
aluVRtrIfRxV4DiscardEncryptionBytes = _AluVRtrIfRxV4DiscardEncryptionBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 40),
    _AluVRtrIfRxV4DiscardEncryptionBytes_Type()
)
aluVRtrIfRxV4DiscardEncryptionBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfRxV4DiscardEncryptionBytes.setStatus("current")


class _AluVRtrIfRxV4DiscardEncryptionLastTunnel_Type(TLNamedItemOrEmpty):
    """Custom type aluVRtrIfRxV4DiscardEncryptionLastTunnel based on TLNamedItemOrEmpty"""
    defaultHexValue = ""


_AluVRtrIfRxV4DiscardEncryptionLastTunnel_Type.__name__ = "TLNamedItemOrEmpty"
_AluVRtrIfRxV4DiscardEncryptionLastTunnel_Object = MibTableColumn
aluVRtrIfRxV4DiscardEncryptionLastTunnel = _AluVRtrIfRxV4DiscardEncryptionLastTunnel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 41),
    _AluVRtrIfRxV4DiscardEncryptionLastTunnel_Type()
)
aluVRtrIfRxV4DiscardEncryptionLastTunnel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfRxV4DiscardEncryptionLastTunnel.setStatus("current")
_AluVRtrIfRxV4OtherDiscardsPkts_Type = Counter64
_AluVRtrIfRxV4OtherDiscardsPkts_Object = MibTableColumn
aluVRtrIfRxV4OtherDiscardsPkts = _AluVRtrIfRxV4OtherDiscardsPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 42),
    _AluVRtrIfRxV4OtherDiscardsPkts_Type()
)
aluVRtrIfRxV4OtherDiscardsPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfRxV4OtherDiscardsPkts.setStatus("current")
_AluVRtrIfRxV4OtherDiscardsBytes_Type = Counter64
_AluVRtrIfRxV4OtherDiscardsBytes_Object = MibTableColumn
aluVRtrIfRxV4OtherDiscardsBytes = _AluVRtrIfRxV4OtherDiscardsBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 43),
    _AluVRtrIfRxV4OtherDiscardsBytes_Type()
)
aluVRtrIfRxV4OtherDiscardsBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfRxV4OtherDiscardsBytes.setStatus("current")
_AluVRtrIfRxV6DiscardPkts_Type = Counter64
_AluVRtrIfRxV6DiscardPkts_Object = MibTableColumn
aluVRtrIfRxV6DiscardPkts = _AluVRtrIfRxV6DiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 44),
    _AluVRtrIfRxV6DiscardPkts_Type()
)
aluVRtrIfRxV6DiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfRxV6DiscardPkts.setStatus("current")
_AluVRtrIfRxV6DiscardBytes_Type = Counter64
_AluVRtrIfRxV6DiscardBytes_Object = MibTableColumn
aluVRtrIfRxV6DiscardBytes = _AluVRtrIfRxV6DiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 45),
    _AluVRtrIfRxV6DiscardBytes_Type()
)
aluVRtrIfRxV6DiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfRxV6DiscardBytes.setStatus("current")
_AluVRtrIfRxV6DiscardInvLenPkts_Type = Counter64
_AluVRtrIfRxV6DiscardInvLenPkts_Object = MibTableColumn
aluVRtrIfRxV6DiscardInvLenPkts = _AluVRtrIfRxV6DiscardInvLenPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 46),
    _AluVRtrIfRxV6DiscardInvLenPkts_Type()
)
aluVRtrIfRxV6DiscardInvLenPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfRxV6DiscardInvLenPkts.setStatus("current")
_AluVRtrIfRxV6DiscardInvLenBytes_Type = Counter64
_AluVRtrIfRxV6DiscardInvLenBytes_Object = MibTableColumn
aluVRtrIfRxV6DiscardInvLenBytes = _AluVRtrIfRxV6DiscardInvLenBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 47),
    _AluVRtrIfRxV6DiscardInvLenBytes_Type()
)
aluVRtrIfRxV6DiscardInvLenBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfRxV6DiscardInvLenBytes.setStatus("current")
_AluVRtrIfRxV6DiscardDestUnreachPkts_Type = Counter64
_AluVRtrIfRxV6DiscardDestUnreachPkts_Object = MibTableColumn
aluVRtrIfRxV6DiscardDestUnreachPkts = _AluVRtrIfRxV6DiscardDestUnreachPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 48),
    _AluVRtrIfRxV6DiscardDestUnreachPkts_Type()
)
aluVRtrIfRxV6DiscardDestUnreachPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfRxV6DiscardDestUnreachPkts.setStatus("current")
_AluVRtrIfRxV6DiscardDestUnreachBytes_Type = Counter64
_AluVRtrIfRxV6DiscardDestUnreachBytes_Object = MibTableColumn
aluVRtrIfRxV6DiscardDestUnreachBytes = _AluVRtrIfRxV6DiscardDestUnreachBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 49),
    _AluVRtrIfRxV6DiscardDestUnreachBytes_Type()
)
aluVRtrIfRxV6DiscardDestUnreachBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfRxV6DiscardDestUnreachBytes.setStatus("current")
_AluVRtrIfRxV6DiscardInvMcastPkts_Type = Counter64
_AluVRtrIfRxV6DiscardInvMcastPkts_Object = MibTableColumn
aluVRtrIfRxV6DiscardInvMcastPkts = _AluVRtrIfRxV6DiscardInvMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 50),
    _AluVRtrIfRxV6DiscardInvMcastPkts_Type()
)
aluVRtrIfRxV6DiscardInvMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfRxV6DiscardInvMcastPkts.setStatus("current")
_AluVRtrIfRxV6DiscardInvMcastBytes_Type = Counter64
_AluVRtrIfRxV6DiscardInvMcastBytes_Object = MibTableColumn
aluVRtrIfRxV6DiscardInvMcastBytes = _AluVRtrIfRxV6DiscardInvMcastBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 51),
    _AluVRtrIfRxV6DiscardInvMcastBytes_Type()
)
aluVRtrIfRxV6DiscardInvMcastBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfRxV6DiscardInvMcastBytes.setStatus("current")
_AluVRtrIfRxV6DiscardSrcMartianAddrPkts_Type = Counter64
_AluVRtrIfRxV6DiscardSrcMartianAddrPkts_Object = MibTableColumn
aluVRtrIfRxV6DiscardSrcMartianAddrPkts = _AluVRtrIfRxV6DiscardSrcMartianAddrPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 52),
    _AluVRtrIfRxV6DiscardSrcMartianAddrPkts_Type()
)
aluVRtrIfRxV6DiscardSrcMartianAddrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfRxV6DiscardSrcMartianAddrPkts.setStatus("current")
_AluVRtrIfRxV6DiscardSrcMartianAddrBytes_Type = Counter64
_AluVRtrIfRxV6DiscardSrcMartianAddrBytes_Object = MibTableColumn
aluVRtrIfRxV6DiscardSrcMartianAddrBytes = _AluVRtrIfRxV6DiscardSrcMartianAddrBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 53),
    _AluVRtrIfRxV6DiscardSrcMartianAddrBytes_Type()
)
aluVRtrIfRxV6DiscardSrcMartianAddrBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfRxV6DiscardSrcMartianAddrBytes.setStatus("current")
_AluVRtrIfRxV6DiscardDestMartianAddrPkts_Type = Counter64
_AluVRtrIfRxV6DiscardDestMartianAddrPkts_Object = MibTableColumn
aluVRtrIfRxV6DiscardDestMartianAddrPkts = _AluVRtrIfRxV6DiscardDestMartianAddrPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 54),
    _AluVRtrIfRxV6DiscardDestMartianAddrPkts_Type()
)
aluVRtrIfRxV6DiscardDestMartianAddrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfRxV6DiscardDestMartianAddrPkts.setStatus("current")
_AluVRtrIfRxV6DiscardDestMartianAddrBytes_Type = Counter64
_AluVRtrIfRxV6DiscardDestMartianAddrBytes_Object = MibTableColumn
aluVRtrIfRxV6DiscardDestMartianAddrBytes = _AluVRtrIfRxV6DiscardDestMartianAddrBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 55),
    _AluVRtrIfRxV6DiscardDestMartianAddrBytes_Type()
)
aluVRtrIfRxV6DiscardDestMartianAddrBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfRxV6DiscardDestMartianAddrBytes.setStatus("current")
_AluVRtrIfRxV6DiscardBlackHolePkts_Type = Counter64
_AluVRtrIfRxV6DiscardBlackHolePkts_Object = MibTableColumn
aluVRtrIfRxV6DiscardBlackHolePkts = _AluVRtrIfRxV6DiscardBlackHolePkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 56),
    _AluVRtrIfRxV6DiscardBlackHolePkts_Type()
)
aluVRtrIfRxV6DiscardBlackHolePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfRxV6DiscardBlackHolePkts.setStatus("current")
_AluVRtrIfRxV6DiscardBlackHoleBytes_Type = Counter64
_AluVRtrIfRxV6DiscardBlackHoleBytes_Object = MibTableColumn
aluVRtrIfRxV6DiscardBlackHoleBytes = _AluVRtrIfRxV6DiscardBlackHoleBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 57),
    _AluVRtrIfRxV6DiscardBlackHoleBytes_Type()
)
aluVRtrIfRxV6DiscardBlackHoleBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfRxV6DiscardBlackHoleBytes.setStatus("current")
_AluVRtrIfRxV6DiscardTTLExpiredPkts_Type = Counter64
_AluVRtrIfRxV6DiscardTTLExpiredPkts_Object = MibTableColumn
aluVRtrIfRxV6DiscardTTLExpiredPkts = _AluVRtrIfRxV6DiscardTTLExpiredPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 58),
    _AluVRtrIfRxV6DiscardTTLExpiredPkts_Type()
)
aluVRtrIfRxV6DiscardTTLExpiredPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfRxV6DiscardTTLExpiredPkts.setStatus("current")
_AluVRtrIfRxV6DiscardTTLExpiredBytes_Type = Counter64
_AluVRtrIfRxV6DiscardTTLExpiredBytes_Object = MibTableColumn
aluVRtrIfRxV6DiscardTTLExpiredBytes = _AluVRtrIfRxV6DiscardTTLExpiredBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 59),
    _AluVRtrIfRxV6DiscardTTLExpiredBytes_Type()
)
aluVRtrIfRxV6DiscardTTLExpiredBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfRxV6DiscardTTLExpiredBytes.setStatus("current")
_AluVRtrIfRxV6DiscardSlowpathPkts_Type = Counter64
_AluVRtrIfRxV6DiscardSlowpathPkts_Object = MibTableColumn
aluVRtrIfRxV6DiscardSlowpathPkts = _AluVRtrIfRxV6DiscardSlowpathPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 60),
    _AluVRtrIfRxV6DiscardSlowpathPkts_Type()
)
aluVRtrIfRxV6DiscardSlowpathPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfRxV6DiscardSlowpathPkts.setStatus("current")
_AluVRtrIfRxV6DiscardSlowpathBytes_Type = Counter64
_AluVRtrIfRxV6DiscardSlowpathBytes_Object = MibTableColumn
aluVRtrIfRxV6DiscardSlowpathBytes = _AluVRtrIfRxV6DiscardSlowpathBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 61),
    _AluVRtrIfRxV6DiscardSlowpathBytes_Type()
)
aluVRtrIfRxV6DiscardSlowpathBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfRxV6DiscardSlowpathBytes.setStatus("current")
_AluVRtrIfRxV6DiscardMtuExceededPkts_Type = Counter64
_AluVRtrIfRxV6DiscardMtuExceededPkts_Object = MibTableColumn
aluVRtrIfRxV6DiscardMtuExceededPkts = _AluVRtrIfRxV6DiscardMtuExceededPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 62),
    _AluVRtrIfRxV6DiscardMtuExceededPkts_Type()
)
aluVRtrIfRxV6DiscardMtuExceededPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfRxV6DiscardMtuExceededPkts.setStatus("current")
_AluVRtrIfRxV6DiscardMtuExceededBytes_Type = Counter64
_AluVRtrIfRxV6DiscardMtuExceededBytes_Object = MibTableColumn
aluVRtrIfRxV6DiscardMtuExceededBytes = _AluVRtrIfRxV6DiscardMtuExceededBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 63),
    _AluVRtrIfRxV6DiscardMtuExceededBytes_Type()
)
aluVRtrIfRxV6DiscardMtuExceededBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfRxV6DiscardMtuExceededBytes.setStatus("current")
_AluVRtrIfRxV6DiscardFltrActionDropPkts_Type = Counter64
_AluVRtrIfRxV6DiscardFltrActionDropPkts_Object = MibTableColumn
aluVRtrIfRxV6DiscardFltrActionDropPkts = _AluVRtrIfRxV6DiscardFltrActionDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 64),
    _AluVRtrIfRxV6DiscardFltrActionDropPkts_Type()
)
aluVRtrIfRxV6DiscardFltrActionDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfRxV6DiscardFltrActionDropPkts.setStatus("current")
_AluVRtrIfRxV6DiscardFltrActionDropBytes_Type = Counter64
_AluVRtrIfRxV6DiscardFltrActionDropBytes_Object = MibTableColumn
aluVRtrIfRxV6DiscardFltrActionDropBytes = _AluVRtrIfRxV6DiscardFltrActionDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 65),
    _AluVRtrIfRxV6DiscardFltrActionDropBytes_Type()
)
aluVRtrIfRxV6DiscardFltrActionDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfRxV6DiscardFltrActionDropBytes.setStatus("current")
_AluVRtrIfRxV6DiscardQueuePkts_Type = Counter64
_AluVRtrIfRxV6DiscardQueuePkts_Object = MibTableColumn
aluVRtrIfRxV6DiscardQueuePkts = _AluVRtrIfRxV6DiscardQueuePkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 66),
    _AluVRtrIfRxV6DiscardQueuePkts_Type()
)
aluVRtrIfRxV6DiscardQueuePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfRxV6DiscardQueuePkts.setStatus("current")
_AluVRtrIfRxV6DiscardQueueBytes_Type = Counter64
_AluVRtrIfRxV6DiscardQueueBytes_Object = MibTableColumn
aluVRtrIfRxV6DiscardQueueBytes = _AluVRtrIfRxV6DiscardQueueBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 67),
    _AluVRtrIfRxV6DiscardQueueBytes_Type()
)
aluVRtrIfRxV6DiscardQueueBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfRxV6DiscardQueueBytes.setStatus("current")
_AluVRtrIfRxV6OtherDiscardsPkts_Type = Counter64
_AluVRtrIfRxV6OtherDiscardsPkts_Object = MibTableColumn
aluVRtrIfRxV6OtherDiscardsPkts = _AluVRtrIfRxV6OtherDiscardsPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 68),
    _AluVRtrIfRxV6OtherDiscardsPkts_Type()
)
aluVRtrIfRxV6OtherDiscardsPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfRxV6OtherDiscardsPkts.setStatus("current")
_AluVRtrIfRxV6OtherDiscardsBytes_Type = Counter64
_AluVRtrIfRxV6OtherDiscardsBytes_Object = MibTableColumn
aluVRtrIfRxV6OtherDiscardsBytes = _AluVRtrIfRxV6OtherDiscardsBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 69),
    _AluVRtrIfRxV6OtherDiscardsBytes_Type()
)
aluVRtrIfRxV6OtherDiscardsBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfRxV6OtherDiscardsBytes.setStatus("current")
_AluVRtrIfTxV4DiscardPkts_Type = Counter64
_AluVRtrIfTxV4DiscardPkts_Object = MibTableColumn
aluVRtrIfTxV4DiscardPkts = _AluVRtrIfTxV4DiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 70),
    _AluVRtrIfTxV4DiscardPkts_Type()
)
aluVRtrIfTxV4DiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfTxV4DiscardPkts.setStatus("current")
_AluVRtrIfTxV4DiscardBytes_Type = Counter64
_AluVRtrIfTxV4DiscardBytes_Object = MibTableColumn
aluVRtrIfTxV4DiscardBytes = _AluVRtrIfTxV4DiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 71),
    _AluVRtrIfTxV4DiscardBytes_Type()
)
aluVRtrIfTxV4DiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfTxV4DiscardBytes.setStatus("current")
_AluVRtrIfTxV4DiscardFltrActionDropPkts_Type = Counter64
_AluVRtrIfTxV4DiscardFltrActionDropPkts_Object = MibTableColumn
aluVRtrIfTxV4DiscardFltrActionDropPkts = _AluVRtrIfTxV4DiscardFltrActionDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 72),
    _AluVRtrIfTxV4DiscardFltrActionDropPkts_Type()
)
aluVRtrIfTxV4DiscardFltrActionDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfTxV4DiscardFltrActionDropPkts.setStatus("current")
_AluVRtrIfTxV4DiscardFltrActionDropBytes_Type = Counter64
_AluVRtrIfTxV4DiscardFltrActionDropBytes_Object = MibTableColumn
aluVRtrIfTxV4DiscardFltrActionDropBytes = _AluVRtrIfTxV4DiscardFltrActionDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 73),
    _AluVRtrIfTxV4DiscardFltrActionDropBytes_Type()
)
aluVRtrIfTxV4DiscardFltrActionDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfTxV4DiscardFltrActionDropBytes.setStatus("current")
_AluVRtrIfTxV4DiscardEncryptionPkts_Type = Counter64
_AluVRtrIfTxV4DiscardEncryptionPkts_Object = MibTableColumn
aluVRtrIfTxV4DiscardEncryptionPkts = _AluVRtrIfTxV4DiscardEncryptionPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 74),
    _AluVRtrIfTxV4DiscardEncryptionPkts_Type()
)
aluVRtrIfTxV4DiscardEncryptionPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfTxV4DiscardEncryptionPkts.setStatus("current")
_AluVRtrIfTxV4DiscardEncryptionBytes_Type = Counter64
_AluVRtrIfTxV4DiscardEncryptionBytes_Object = MibTableColumn
aluVRtrIfTxV4DiscardEncryptionBytes = _AluVRtrIfTxV4DiscardEncryptionBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 75),
    _AluVRtrIfTxV4DiscardEncryptionBytes_Type()
)
aluVRtrIfTxV4DiscardEncryptionBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfTxV4DiscardEncryptionBytes.setStatus("current")


class _AluVRtrIfTxV4DiscardEncryptionLastTunnel_Type(TLNamedItemOrEmpty):
    """Custom type aluVRtrIfTxV4DiscardEncryptionLastTunnel based on TLNamedItemOrEmpty"""
    defaultHexValue = ""


_AluVRtrIfTxV4DiscardEncryptionLastTunnel_Type.__name__ = "TLNamedItemOrEmpty"
_AluVRtrIfTxV4DiscardEncryptionLastTunnel_Object = MibTableColumn
aluVRtrIfTxV4DiscardEncryptionLastTunnel = _AluVRtrIfTxV4DiscardEncryptionLastTunnel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 76),
    _AluVRtrIfTxV4DiscardEncryptionLastTunnel_Type()
)
aluVRtrIfTxV4DiscardEncryptionLastTunnel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfTxV4DiscardEncryptionLastTunnel.setStatus("current")
_AluVRtrIfTxV4DiscardOtherDiscardsPkts_Type = Counter64
_AluVRtrIfTxV4DiscardOtherDiscardsPkts_Object = MibTableColumn
aluVRtrIfTxV4DiscardOtherDiscardsPkts = _AluVRtrIfTxV4DiscardOtherDiscardsPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 77),
    _AluVRtrIfTxV4DiscardOtherDiscardsPkts_Type()
)
aluVRtrIfTxV4DiscardOtherDiscardsPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfTxV4DiscardOtherDiscardsPkts.setStatus("current")
_AluVRtrIfTxV4DiscardOtherDiscardsBytes_Type = Counter64
_AluVRtrIfTxV4DiscardOtherDiscardsBytes_Object = MibTableColumn
aluVRtrIfTxV4DiscardOtherDiscardsBytes = _AluVRtrIfTxV4DiscardOtherDiscardsBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 78),
    _AluVRtrIfTxV4DiscardOtherDiscardsBytes_Type()
)
aluVRtrIfTxV4DiscardOtherDiscardsBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfTxV4DiscardOtherDiscardsBytes.setStatus("current")
_AluVRtrIfTxV6DiscardPkts_Type = Counter64
_AluVRtrIfTxV6DiscardPkts_Object = MibTableColumn
aluVRtrIfTxV6DiscardPkts = _AluVRtrIfTxV6DiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 79),
    _AluVRtrIfTxV6DiscardPkts_Type()
)
aluVRtrIfTxV6DiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfTxV6DiscardPkts.setStatus("current")
_AluVRtrIfTxV6DiscardBytes_Type = Counter64
_AluVRtrIfTxV6DiscardBytes_Object = MibTableColumn
aluVRtrIfTxV6DiscardBytes = _AluVRtrIfTxV6DiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 80),
    _AluVRtrIfTxV6DiscardBytes_Type()
)
aluVRtrIfTxV6DiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfTxV6DiscardBytes.setStatus("current")
_AluVRtrIfTxV6DiscardFltrActionDropPkts_Type = Counter64
_AluVRtrIfTxV6DiscardFltrActionDropPkts_Object = MibTableColumn
aluVRtrIfTxV6DiscardFltrActionDropPkts = _AluVRtrIfTxV6DiscardFltrActionDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 81),
    _AluVRtrIfTxV6DiscardFltrActionDropPkts_Type()
)
aluVRtrIfTxV6DiscardFltrActionDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfTxV6DiscardFltrActionDropPkts.setStatus("current")
_AluVRtrIfTxV6DiscardFltrActionDropBytes_Type = Counter64
_AluVRtrIfTxV6DiscardFltrActionDropBytes_Object = MibTableColumn
aluVRtrIfTxV6DiscardFltrActionDropBytes = _AluVRtrIfTxV6DiscardFltrActionDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 82),
    _AluVRtrIfTxV6DiscardFltrActionDropBytes_Type()
)
aluVRtrIfTxV6DiscardFltrActionDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfTxV6DiscardFltrActionDropBytes.setStatus("current")
_AluVRtrIfTxV6DiscardOtherDiscardsPkts_Type = Counter64
_AluVRtrIfTxV6DiscardOtherDiscardsPkts_Object = MibTableColumn
aluVRtrIfTxV6DiscardOtherDiscardsPkts = _AluVRtrIfTxV6DiscardOtherDiscardsPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 83),
    _AluVRtrIfTxV6DiscardOtherDiscardsPkts_Type()
)
aluVRtrIfTxV6DiscardOtherDiscardsPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfTxV6DiscardOtherDiscardsPkts.setStatus("current")
_AluVRtrIfTxV6DiscardOtherDiscardsBytes_Type = Counter64
_AluVRtrIfTxV6DiscardOtherDiscardsBytes_Object = MibTableColumn
aluVRtrIfTxV6DiscardOtherDiscardsBytes = _AluVRtrIfTxV6DiscardOtherDiscardsBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 84),
    _AluVRtrIfTxV6DiscardOtherDiscardsBytes_Type()
)
aluVRtrIfTxV6DiscardOtherDiscardsBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfTxV6DiscardOtherDiscardsBytes.setStatus("current")
_AluVRtrIfSecRxCtrlQueueFwdPkts_Type = Counter64
_AluVRtrIfSecRxCtrlQueueFwdPkts_Object = MibTableColumn
aluVRtrIfSecRxCtrlQueueFwdPkts = _AluVRtrIfSecRxCtrlQueueFwdPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 85),
    _AluVRtrIfSecRxCtrlQueueFwdPkts_Type()
)
aluVRtrIfSecRxCtrlQueueFwdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfSecRxCtrlQueueFwdPkts.setStatus("current")
_AluVRtrIfSecRxCtrlQueueFwdBytes_Type = Counter64
_AluVRtrIfSecRxCtrlQueueFwdBytes_Object = MibTableColumn
aluVRtrIfSecRxCtrlQueueFwdBytes = _AluVRtrIfSecRxCtrlQueueFwdBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 86),
    _AluVRtrIfSecRxCtrlQueueFwdBytes_Type()
)
aluVRtrIfSecRxCtrlQueueFwdBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfSecRxCtrlQueueFwdBytes.setStatus("current")
_AluVRtrIfSecRxCtrlQueueDroPkts_Type = Counter64
_AluVRtrIfSecRxCtrlQueueDroPkts_Object = MibTableColumn
aluVRtrIfSecRxCtrlQueueDroPkts = _AluVRtrIfSecRxCtrlQueueDroPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 87),
    _AluVRtrIfSecRxCtrlQueueDroPkts_Type()
)
aluVRtrIfSecRxCtrlQueueDroPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfSecRxCtrlQueueDroPkts.setStatus("current")
_AluVRtrIfSecRxCtrlQueueDroBytes_Type = Counter64
_AluVRtrIfSecRxCtrlQueueDroBytes_Object = MibTableColumn
aluVRtrIfSecRxCtrlQueueDroBytes = _AluVRtrIfSecRxCtrlQueueDroBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 88),
    _AluVRtrIfSecRxCtrlQueueDroBytes_Type()
)
aluVRtrIfSecRxCtrlQueueDroBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfSecRxCtrlQueueDroBytes.setStatus("current")
_AluVRtrIfSecBadProtoDroPkts_Type = Counter64
_AluVRtrIfSecBadProtoDroPkts_Object = MibTableColumn
aluVRtrIfSecBadProtoDroPkts = _AluVRtrIfSecBadProtoDroPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 89),
    _AluVRtrIfSecBadProtoDroPkts_Type()
)
aluVRtrIfSecBadProtoDroPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfSecBadProtoDroPkts.setStatus("current")
_AluVRtrIfSecBadProtoDroBytes_Type = Counter64
_AluVRtrIfSecBadProtoDroBytes_Object = MibTableColumn
aluVRtrIfSecBadProtoDroBytes = _AluVRtrIfSecBadProtoDroBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 90),
    _AluVRtrIfSecBadProtoDroBytes_Type()
)
aluVRtrIfSecBadProtoDroBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfSecBadProtoDroBytes.setStatus("current")
_AluVRtrIfSecBadServiceDroPkts_Type = Counter64
_AluVRtrIfSecBadServiceDroPkts_Object = MibTableColumn
aluVRtrIfSecBadServiceDroPkts = _AluVRtrIfSecBadServiceDroPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 91),
    _AluVRtrIfSecBadServiceDroPkts_Type()
)
aluVRtrIfSecBadServiceDroPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfSecBadServiceDroPkts.setStatus("current")
_AluVRtrIfSecBadServiceDroBytes_Type = Counter64
_AluVRtrIfSecBadServiceDroBytes_Object = MibTableColumn
aluVRtrIfSecBadServiceDroBytes = _AluVRtrIfSecBadServiceDroBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 92),
    _AluVRtrIfSecBadServiceDroBytes_Type()
)
aluVRtrIfSecBadServiceDroBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfSecBadServiceDroBytes.setStatus("current")
_AluVRtrIfSecNoSessionDroPkts_Type = Counter64
_AluVRtrIfSecNoSessionDroPkts_Object = MibTableColumn
aluVRtrIfSecNoSessionDroPkts = _AluVRtrIfSecNoSessionDroPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 93),
    _AluVRtrIfSecNoSessionDroPkts_Type()
)
aluVRtrIfSecNoSessionDroPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfSecNoSessionDroPkts.setStatus("current")
_AluVRtrIfSecNoSessionDroBytes_Type = Counter64
_AluVRtrIfSecNoSessionDroBytes_Object = MibTableColumn
aluVRtrIfSecNoSessionDroBytes = _AluVRtrIfSecNoSessionDroBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 94),
    _AluVRtrIfSecNoSessionDroBytes_Type()
)
aluVRtrIfSecNoSessionDroBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfSecNoSessionDroBytes.setStatus("current")
_AluVRtrIfSecFragmentsDroPkts_Type = Counter64
_AluVRtrIfSecFragmentsDroPkts_Object = MibTableColumn
aluVRtrIfSecFragmentsDroPkts = _AluVRtrIfSecFragmentsDroPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 95),
    _AluVRtrIfSecFragmentsDroPkts_Type()
)
aluVRtrIfSecFragmentsDroPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfSecFragmentsDroPkts.setStatus("current")
_AluVRtrIfSecFragmentsDroBytes_Type = Counter64
_AluVRtrIfSecFragmentsDroBytes_Object = MibTableColumn
aluVRtrIfSecFragmentsDroBytes = _AluVRtrIfSecFragmentsDroBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 96),
    _AluVRtrIfSecFragmentsDroBytes_Type()
)
aluVRtrIfSecFragmentsDroBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfSecFragmentsDroBytes.setStatus("current")
_AluVRtrIfSecBadIcmpTypeDroPkts_Type = Counter64
_AluVRtrIfSecBadIcmpTypeDroPkts_Object = MibTableColumn
aluVRtrIfSecBadIcmpTypeDroPkts = _AluVRtrIfSecBadIcmpTypeDroPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 97),
    _AluVRtrIfSecBadIcmpTypeDroPkts_Type()
)
aluVRtrIfSecBadIcmpTypeDroPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfSecBadIcmpTypeDroPkts.setStatus("current")
_AluVRtrIfSecBadIcmpTypeDroBytes_Type = Counter64
_AluVRtrIfSecBadIcmpTypeDroBytes_Object = MibTableColumn
aluVRtrIfSecBadIcmpTypeDroBytes = _AluVRtrIfSecBadIcmpTypeDroBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 98),
    _AluVRtrIfSecBadIcmpTypeDroBytes_Type()
)
aluVRtrIfSecBadIcmpTypeDroBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfSecBadIcmpTypeDroBytes.setStatus("current")
_AluVRtrIfSecRouteLoopDroPkts_Type = Counter64
_AluVRtrIfSecRouteLoopDroPkts_Object = MibTableColumn
aluVRtrIfSecRouteLoopDroPkts = _AluVRtrIfSecRouteLoopDroPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 99),
    _AluVRtrIfSecRouteLoopDroPkts_Type()
)
aluVRtrIfSecRouteLoopDroPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfSecRouteLoopDroPkts.setStatus("current")
_AluVRtrIfSecRouteLoopDroBytes_Type = Counter64
_AluVRtrIfSecRouteLoopDroBytes_Object = MibTableColumn
aluVRtrIfSecRouteLoopDroBytes = _AluVRtrIfSecRouteLoopDroBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 100),
    _AluVRtrIfSecRouteLoopDroBytes_Type()
)
aluVRtrIfSecRouteLoopDroBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfSecRouteLoopDroBytes.setStatus("current")
_AluVRtrIfSecOtherDroPkts_Type = Counter64
_AluVRtrIfSecOtherDroPkts_Object = MibTableColumn
aluVRtrIfSecOtherDroPkts = _AluVRtrIfSecOtherDroPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 101),
    _AluVRtrIfSecOtherDroPkts_Type()
)
aluVRtrIfSecOtherDroPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfSecOtherDroPkts.setStatus("current")
_AluVRtrIfSecOtherDroBytes_Type = Counter64
_AluVRtrIfSecOtherDroBytes_Object = MibTableColumn
aluVRtrIfSecOtherDroBytes = _AluVRtrIfSecOtherDroBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 2, 1, 102),
    _AluVRtrIfSecOtherDroBytes_Type()
)
aluVRtrIfSecOtherDroBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrIfSecOtherDroBytes.setStatus("current")
_AluVRtrMplsIfStatTable_Object = MibTable
aluVRtrMplsIfStatTable = _AluVRtrMplsIfStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 3)
)
if mibBuilder.loadTexts:
    aluVRtrMplsIfStatTable.setStatus("current")
_AluVRtrMplsIfStatEntry_Object = MibTableRow
aluVRtrMplsIfStatEntry = _AluVRtrMplsIfStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 3, 1)
)
if mibBuilder.loadTexts:
    aluVRtrMplsIfStatEntry.setStatus("current")
_AluVRtrMplsIfRxInvLabels_Type = Counter64
_AluVRtrMplsIfRxInvLabels_Object = MibTableColumn
aluVRtrMplsIfRxInvLabels = _AluVRtrMplsIfRxInvLabels_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 3, 1, 1),
    _AluVRtrMplsIfRxInvLabels_Type()
)
aluVRtrMplsIfRxInvLabels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrMplsIfRxInvLabels.setStatus("current")
_AluVRtrMplsIfRxInvIpoMplsPkts_Type = Counter64
_AluVRtrMplsIfRxInvIpoMplsPkts_Object = MibTableColumn
aluVRtrMplsIfRxInvIpoMplsPkts = _AluVRtrMplsIfRxInvIpoMplsPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 3, 1, 2),
    _AluVRtrMplsIfRxInvIpoMplsPkts_Type()
)
aluVRtrMplsIfRxInvIpoMplsPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrMplsIfRxInvIpoMplsPkts.setStatus("current")
_AluVRtrMplsIfRxStackTooBigPkts_Type = Counter64
_AluVRtrMplsIfRxStackTooBigPkts_Object = MibTableColumn
aluVRtrMplsIfRxStackTooBigPkts = _AluVRtrMplsIfRxStackTooBigPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 3, 1, 3),
    _AluVRtrMplsIfRxStackTooBigPkts_Type()
)
aluVRtrMplsIfRxStackTooBigPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrMplsIfRxStackTooBigPkts.setStatus("current")
_AluVRtrMplsIfRxOtherDiscardPkts_Type = Counter64
_AluVRtrMplsIfRxOtherDiscardPkts_Object = MibTableColumn
aluVRtrMplsIfRxOtherDiscardPkts = _AluVRtrMplsIfRxOtherDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 3, 1, 4),
    _AluVRtrMplsIfRxOtherDiscardPkts_Type()
)
aluVRtrMplsIfRxOtherDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrMplsIfRxOtherDiscardPkts.setStatus("current")
_AluVRtrMplsIfLastInvalidLabel_Type = MplsLabel
_AluVRtrMplsIfLastInvalidLabel_Object = MibTableColumn
aluVRtrMplsIfLastInvalidLabel = _AluVRtrMplsIfLastInvalidLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 3, 1, 5),
    _AluVRtrMplsIfLastInvalidLabel_Type()
)
aluVRtrMplsIfLastInvalidLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrMplsIfLastInvalidLabel.setStatus("current")
_AluVRtrMplsIfLastInvalidPos_Type = Unsigned32
_AluVRtrMplsIfLastInvalidPos_Object = MibTableColumn
aluVRtrMplsIfLastInvalidPos = _AluVRtrMplsIfLastInvalidPos_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 3, 1, 6),
    _AluVRtrMplsIfLastInvalidPos_Type()
)
aluVRtrMplsIfLastInvalidPos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrMplsIfLastInvalidPos.setStatus("current")
_AluVRtrMplsIfRxTTLExpiredPkts_Type = Counter64
_AluVRtrMplsIfRxTTLExpiredPkts_Object = MibTableColumn
aluVRtrMplsIfRxTTLExpiredPkts = _AluVRtrMplsIfRxTTLExpiredPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 3, 1, 7),
    _AluVRtrMplsIfRxTTLExpiredPkts_Type()
)
aluVRtrMplsIfRxTTLExpiredPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrMplsIfRxTTLExpiredPkts.setStatus("current")
_AluVRtrMplsIfRxMtuExceedPkts_Type = Counter64
_AluVRtrMplsIfRxMtuExceedPkts_Object = MibTableColumn
aluVRtrMplsIfRxMtuExceedPkts = _AluVRtrMplsIfRxMtuExceedPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 3, 1, 8),
    _AluVRtrMplsIfRxMtuExceedPkts_Type()
)
aluVRtrMplsIfRxMtuExceedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrMplsIfRxMtuExceedPkts.setStatus("current")
_AluVRtrMplsIfRxQueueDiscardPkts_Type = Counter64
_AluVRtrMplsIfRxQueueDiscardPkts_Object = MibTableColumn
aluVRtrMplsIfRxQueueDiscardPkts = _AluVRtrMplsIfRxQueueDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 3, 1, 9),
    _AluVRtrMplsIfRxQueueDiscardPkts_Type()
)
aluVRtrMplsIfRxQueueDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVRtrMplsIfRxQueueDiscardPkts.setStatus("current")
_AluVRtrNotificationObjects_ObjectIdentity = ObjectIdentity
aluVRtrNotificationObjects = _AluVRtrNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 4)
)
_VRtrFibV6UnsupportedRoute_Type = TruthValue
_VRtrFibV6UnsupportedRoute_Object = MibScalar
vRtrFibV6UnsupportedRoute = _VRtrFibV6UnsupportedRoute_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 4, 1),
    _VRtrFibV6UnsupportedRoute_Type()
)
vRtrFibV6UnsupportedRoute.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrFibV6UnsupportedRoute.setStatus("obsolete")
_VRtrFibV6TableThresholdExceed_Type = TruthValue
_VRtrFibV6TableThresholdExceed_Object = MibScalar
vRtrFibV6TableThresholdExceed = _VRtrFibV6TableThresholdExceed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 4, 2),
    _VRtrFibV6TableThresholdExceed_Type()
)
vRtrFibV6TableThresholdExceed.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrFibV6TableThresholdExceed.setStatus("current")
_AluVRtrPimNgNtfySGLmtExcd_Type = TruthValue
_AluVRtrPimNgNtfySGLmtExcd_Object = MibScalar
aluVRtrPimNgNtfySGLmtExcd = _AluVRtrPimNgNtfySGLmtExcd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 4, 3),
    _AluVRtrPimNgNtfySGLmtExcd_Type()
)
aluVRtrPimNgNtfySGLmtExcd.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    aluVRtrPimNgNtfySGLmtExcd.setStatus("current")
_AluVRtrPimNgNtfyMaxSG_Type = Unsigned32
_AluVRtrPimNgNtfyMaxSG_Object = MibScalar
aluVRtrPimNgNtfyMaxSG = _AluVRtrPimNgNtfyMaxSG_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 4, 4),
    _AluVRtrPimNgNtfyMaxSG_Type()
)
aluVRtrPimNgNtfyMaxSG.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    aluVRtrPimNgNtfyMaxSG.setStatus("current")
_AluVrtrIfExtTable_Object = MibTable
aluVrtrIfExtTable = _AluVrtrIfExtTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 5)
)
if mibBuilder.loadTexts:
    aluVrtrIfExtTable.setStatus("current")
_AluVrtrIfExtEntry_Object = MibTableRow
aluVrtrIfExtEntry = _AluVrtrIfExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 5, 1)
)
if mibBuilder.loadTexts:
    aluVrtrIfExtEntry.setStatus("current")


class _AluVrtrIfL4LoadBalancing_Type(Integer32):
    """Custom type aluVrtrIfL4LoadBalancing based on Integer32"""
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
        *(("system", 0),
          ("includeL4", 1),
          ("excludeL4", 2))
    )


_AluVrtrIfL4LoadBalancing_Type.__name__ = "Integer32"
_AluVrtrIfL4LoadBalancing_Object = MibTableColumn
aluVrtrIfL4LoadBalancing = _AluVrtrIfL4LoadBalancing_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 5, 1, 1),
    _AluVrtrIfL4LoadBalancing_Type()
)
aluVrtrIfL4LoadBalancing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluVrtrIfL4LoadBalancing.setStatus("current")


class _AluVrtrIfSecurityConfigZoneId_Type(Unsigned32):
    """Custom type aluVrtrIfSecurityConfigZoneId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AluVrtrIfSecurityConfigZoneId_Type.__name__ = "Unsigned32"
_AluVrtrIfSecurityConfigZoneId_Object = MibTableColumn
aluVrtrIfSecurityConfigZoneId = _AluVrtrIfSecurityConfigZoneId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 5, 1, 2),
    _AluVrtrIfSecurityConfigZoneId_Type()
)
aluVrtrIfSecurityConfigZoneId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluVrtrIfSecurityConfigZoneId.setStatus("current")


class _AluVrtrIfSecurityOperZoneId_Type(Unsigned32):
    """Custom type aluVrtrIfSecurityOperZoneId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AluVrtrIfSecurityOperZoneId_Type.__name__ = "Unsigned32"
_AluVrtrIfSecurityOperZoneId_Object = MibTableColumn
aluVrtrIfSecurityOperZoneId = _AluVrtrIfSecurityOperZoneId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 5, 1, 3),
    _AluVrtrIfSecurityOperZoneId_Type()
)
aluVrtrIfSecurityOperZoneId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVrtrIfSecurityOperZoneId.setStatus("current")


class _AluVrtrIfSecurityBypass_Type(TruthValue):
    """Custom type aluVrtrIfSecurityBypass based on TruthValue"""
    defaultValue = 2


_AluVrtrIfSecurityBypass_Type.__name__ = "TruthValue"
_AluVrtrIfSecurityBypass_Object = MibTableColumn
aluVrtrIfSecurityBypass = _AluVrtrIfSecurityBypass_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 5, 1, 4),
    _AluVrtrIfSecurityBypass_Type()
)
aluVrtrIfSecurityBypass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluVrtrIfSecurityBypass.setStatus("current")


class _AluVrtrIfNetworkEgrQueuePol_Type(TNamedItemOrEmpty):
    """Custom type aluVrtrIfNetworkEgrQueuePol based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_AluVrtrIfNetworkEgrQueuePol_Type.__name__ = "TNamedItemOrEmpty"
_AluVrtrIfNetworkEgrQueuePol_Object = MibTableColumn
aluVrtrIfNetworkEgrQueuePol = _AluVrtrIfNetworkEgrQueuePol_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 5, 1, 5),
    _AluVrtrIfNetworkEgrQueuePol_Type()
)
aluVrtrIfNetworkEgrQueuePol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluVrtrIfNetworkEgrQueuePol.setStatus("current")


class _AluVrtrIfNetworkEgrAggRate_Type(TPortSchedulerPIR):
    """Custom type aluVrtrIfNetworkEgrAggRate based on TPortSchedulerPIR"""
    defaultValue = -1

    subtypeSpec = TPortSchedulerPIR.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 10000000),
    )


_AluVrtrIfNetworkEgrAggRate_Type.__name__ = "TPortSchedulerPIR"
_AluVrtrIfNetworkEgrAggRate_Object = MibTableColumn
aluVrtrIfNetworkEgrAggRate = _AluVrtrIfNetworkEgrAggRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 5, 1, 6),
    _AluVrtrIfNetworkEgrAggRate_Type()
)
aluVrtrIfNetworkEgrAggRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluVrtrIfNetworkEgrAggRate.setStatus("current")
if mibBuilder.loadTexts:
    aluVrtrIfNetworkEgrAggRate.setUnits("kbps")


class _AluVrtrIfNetworkEgrAggCir_Type(TPortSchedulerCIR):
    """Custom type aluVrtrIfNetworkEgrAggCir based on TPortSchedulerCIR"""
    defaultValue = 0

    subtypeSpec = TPortSchedulerCIR.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 10000000),
    )


_AluVrtrIfNetworkEgrAggCir_Type.__name__ = "TPortSchedulerCIR"
_AluVrtrIfNetworkEgrAggCir_Object = MibTableColumn
aluVrtrIfNetworkEgrAggCir = _AluVrtrIfNetworkEgrAggCir_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 5, 1, 7),
    _AluVrtrIfNetworkEgrAggCir_Type()
)
aluVrtrIfNetworkEgrAggCir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluVrtrIfNetworkEgrAggCir.setStatus("current")
if mibBuilder.loadTexts:
    aluVrtrIfNetworkEgrAggCir.setUnits("kbps")
_AluVrtrIfNetEgrStatsTable_Object = MibTable
aluVrtrIfNetEgrStatsTable = _AluVrtrIfNetEgrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 6)
)
if mibBuilder.loadTexts:
    aluVrtrIfNetEgrStatsTable.setStatus("current")
_AluVrtrIfNetEgrStatsEntry_Object = MibTableRow
aluVrtrIfNetEgrStatsEntry = _AluVrtrIfNetEgrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 6, 1)
)
aluVrtrIfNetEgrStatsEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-VRTR-MIB", "vRtrIfIndex"),
    (0, "ALU-VRTR-MIB", "aluVrtrIfNetEgrQueueIndex"),
)
if mibBuilder.loadTexts:
    aluVrtrIfNetEgrStatsEntry.setStatus("current")


class _AluVrtrIfNetEgrQueueIndex_Type(TQueueId):
    """Custom type aluVrtrIfNetEgrQueueIndex based on TQueueId"""
    subtypeSpec = TQueueId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AluVrtrIfNetEgrQueueIndex_Type.__name__ = "TQueueId"
_AluVrtrIfNetEgrQueueIndex_Object = MibTableColumn
aluVrtrIfNetEgrQueueIndex = _AluVrtrIfNetEgrQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 6, 1, 1),
    _AluVrtrIfNetEgrQueueIndex_Type()
)
aluVrtrIfNetEgrQueueIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluVrtrIfNetEgrQueueIndex.setStatus("current")
_AluVrtrIfNetEgrFwdInProfPkts_Type = Counter64
_AluVrtrIfNetEgrFwdInProfPkts_Object = MibTableColumn
aluVrtrIfNetEgrFwdInProfPkts = _AluVrtrIfNetEgrFwdInProfPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 6, 1, 2),
    _AluVrtrIfNetEgrFwdInProfPkts_Type()
)
aluVrtrIfNetEgrFwdInProfPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVrtrIfNetEgrFwdInProfPkts.setStatus("current")
_AluVrtrIfNetEgrFwdOutProfPkts_Type = Counter64
_AluVrtrIfNetEgrFwdOutProfPkts_Object = MibTableColumn
aluVrtrIfNetEgrFwdOutProfPkts = _AluVrtrIfNetEgrFwdOutProfPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 6, 1, 3),
    _AluVrtrIfNetEgrFwdOutProfPkts_Type()
)
aluVrtrIfNetEgrFwdOutProfPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVrtrIfNetEgrFwdOutProfPkts.setStatus("current")
_AluVrtrIfNetEgrFwdInProfOcts_Type = Counter64
_AluVrtrIfNetEgrFwdInProfOcts_Object = MibTableColumn
aluVrtrIfNetEgrFwdInProfOcts = _AluVrtrIfNetEgrFwdInProfOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 6, 1, 4),
    _AluVrtrIfNetEgrFwdInProfOcts_Type()
)
aluVrtrIfNetEgrFwdInProfOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVrtrIfNetEgrFwdInProfOcts.setStatus("current")
_AluVrtrIfNetEgrFwdOutProfOcts_Type = Counter64
_AluVrtrIfNetEgrFwdOutProfOcts_Object = MibTableColumn
aluVrtrIfNetEgrFwdOutProfOcts = _AluVrtrIfNetEgrFwdOutProfOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 6, 1, 5),
    _AluVrtrIfNetEgrFwdOutProfOcts_Type()
)
aluVrtrIfNetEgrFwdOutProfOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVrtrIfNetEgrFwdOutProfOcts.setStatus("current")
_AluVrtrIfNetEgrDroInProfPkts_Type = Counter64
_AluVrtrIfNetEgrDroInProfPkts_Object = MibTableColumn
aluVrtrIfNetEgrDroInProfPkts = _AluVrtrIfNetEgrDroInProfPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 6, 1, 6),
    _AluVrtrIfNetEgrDroInProfPkts_Type()
)
aluVrtrIfNetEgrDroInProfPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVrtrIfNetEgrDroInProfPkts.setStatus("current")
_AluVrtrIfNetEgrDroOutProfPkts_Type = Counter64
_AluVrtrIfNetEgrDroOutProfPkts_Object = MibTableColumn
aluVrtrIfNetEgrDroOutProfPkts = _AluVrtrIfNetEgrDroOutProfPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 6, 1, 7),
    _AluVrtrIfNetEgrDroOutProfPkts_Type()
)
aluVrtrIfNetEgrDroOutProfPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVrtrIfNetEgrDroOutProfPkts.setStatus("current")
_AluVrtrIfNetEgrDroInProfOcts_Type = Counter64
_AluVrtrIfNetEgrDroInProfOcts_Object = MibTableColumn
aluVrtrIfNetEgrDroInProfOcts = _AluVrtrIfNetEgrDroInProfOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 6, 1, 8),
    _AluVrtrIfNetEgrDroInProfOcts_Type()
)
aluVrtrIfNetEgrDroInProfOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVrtrIfNetEgrDroInProfOcts.setStatus("current")
_AluVrtrIfNetEgrDroOutProfOcts_Type = Counter64
_AluVrtrIfNetEgrDroOutProfOcts_Object = MibTableColumn
aluVrtrIfNetEgrDroOutProfOcts = _AluVrtrIfNetEgrDroOutProfOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 8, 6, 1, 9),
    _AluVrtrIfNetEgrDroOutProfOcts_Type()
)
aluVrtrIfNetEgrDroOutProfOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluVrtrIfNetEgrDroOutProfOcts.setStatus("current")
_AluVrtrIpAddrObjs_ObjectIdentity = ObjectIdentity
aluVrtrIpAddrObjs = _AluVrtrIpAddrObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 14)
)
_AluVrtrIpAddrTable_Object = MibTable
aluVrtrIpAddrTable = _AluVrtrIpAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 14, 1)
)
if mibBuilder.loadTexts:
    aluVrtrIpAddrTable.setStatus("current")
_AluVrtrIpAddrEntry_Object = MibTableRow
aluVrtrIpAddrEntry = _AluVrtrIpAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 14, 1, 1)
)
if mibBuilder.loadTexts:
    aluVrtrIpAddrEntry.setStatus("current")


class _AluVrtrIpAddrDhcpClient_Type(TruthValue):
    """Custom type aluVrtrIpAddrDhcpClient based on TruthValue"""
    defaultValue = 2


_AluVrtrIpAddrDhcpClient_Type.__name__ = "TruthValue"
_AluVrtrIpAddrDhcpClient_Object = MibTableColumn
aluVrtrIpAddrDhcpClient = _AluVrtrIpAddrDhcpClient_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 14, 1, 1, 1),
    _AluVrtrIpAddrDhcpClient_Type()
)
aluVrtrIpAddrDhcpClient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluVrtrIpAddrDhcpClient.setStatus("current")


class _AluVrtrIpAddrClientId_Type(DisplayString):
    """Custom type aluVrtrIpAddrClientId based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AluVrtrIpAddrClientId_Type.__name__ = "DisplayString"
_AluVrtrIpAddrClientId_Object = MibTableColumn
aluVrtrIpAddrClientId = _AluVrtrIpAddrClientId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 14, 1, 1, 2),
    _AluVrtrIpAddrClientId_Type()
)
aluVrtrIpAddrClientId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluVrtrIpAddrClientId.setStatus("current")


class _AluVrtrIpAddrClassId_Type(DisplayString):
    """Custom type aluVrtrIpAddrClassId based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AluVrtrIpAddrClassId_Type.__name__ = "DisplayString"
_AluVrtrIpAddrClassId_Object = MibTableColumn
aluVrtrIpAddrClassId = _AluVrtrIpAddrClassId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 14, 1, 1, 3),
    _AluVrtrIpAddrClassId_Type()
)
aluVrtrIpAddrClassId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluVrtrIpAddrClassId.setStatus("current")
_AluTwampObjs_ObjectIdentity = ObjectIdentity
aluTwampObjs = _AluTwampObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 15)
)
_AluTwampConfigObjs_ObjectIdentity = ObjectIdentity
aluTwampConfigObjs = _AluTwampConfigObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 15, 1)
)


class _AluTwampRefInactTimeout_Type(Unsigned32):
    """Custom type aluTwampRefInactTimeout based on Unsigned32"""
    defaultValue = 900

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3600),
    )


_AluTwampRefInactTimeout_Type.__name__ = "Unsigned32"
_AluTwampRefInactTimeout_Object = MibScalar
aluTwampRefInactTimeout = _AluTwampRefInactTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 15, 1, 1),
    _AluTwampRefInactTimeout_Type()
)
aluTwampRefInactTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluTwampRefInactTimeout.setStatus("current")
if mibBuilder.loadTexts:
    aluTwampRefInactTimeout.setUnits("seconds")
_AluTwampNotificationObjs_ObjectIdentity = ObjectIdentity
aluTwampNotificationObjs = _AluTwampNotificationObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 15, 2)
)
_AluTwampRefNotifLocalAddrType_Type = InetAddressType
_AluTwampRefNotifLocalAddrType_Object = MibScalar
aluTwampRefNotifLocalAddrType = _AluTwampRefNotifLocalAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 15, 2, 1),
    _AluTwampRefNotifLocalAddrType_Type()
)
aluTwampRefNotifLocalAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    aluTwampRefNotifLocalAddrType.setStatus("current")


class _AluTwampRefNotifLocalAddr_Type(InetAddress):
    """Custom type aluTwampRefNotifLocalAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_AluTwampRefNotifLocalAddr_Type.__name__ = "InetAddress"
_AluTwampRefNotifLocalAddr_Object = MibScalar
aluTwampRefNotifLocalAddr = _AluTwampRefNotifLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 15, 2, 2),
    _AluTwampRefNotifLocalAddr_Type()
)
aluTwampRefNotifLocalAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    aluTwampRefNotifLocalAddr.setStatus("current")
_AluTwampRefNotifLocalPort_Type = TTcpUdpPort
_AluTwampRefNotifLocalPort_Object = MibScalar
aluTwampRefNotifLocalPort = _AluTwampRefNotifLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 15, 2, 3),
    _AluTwampRefNotifLocalPort_Type()
)
aluTwampRefNotifLocalPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    aluTwampRefNotifLocalPort.setStatus("current")
_AluTwampRefNotifRemoteAddrType_Type = InetAddressType
_AluTwampRefNotifRemoteAddrType_Object = MibScalar
aluTwampRefNotifRemoteAddrType = _AluTwampRefNotifRemoteAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 15, 2, 4),
    _AluTwampRefNotifRemoteAddrType_Type()
)
aluTwampRefNotifRemoteAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    aluTwampRefNotifRemoteAddrType.setStatus("current")


class _AluTwampRefNotifRemoteAddr_Type(InetAddress):
    """Custom type aluTwampRefNotifRemoteAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_AluTwampRefNotifRemoteAddr_Type.__name__ = "InetAddress"
_AluTwampRefNotifRemoteAddr_Object = MibScalar
aluTwampRefNotifRemoteAddr = _AluTwampRefNotifRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 15, 2, 5),
    _AluTwampRefNotifRemoteAddr_Type()
)
aluTwampRefNotifRemoteAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    aluTwampRefNotifRemoteAddr.setStatus("current")
_AluTwampRefNotifRemotePort_Type = TTcpUdpPort
_AluTwampRefNotifRemotePort_Object = MibScalar
aluTwampRefNotifRemotePort = _AluTwampRefNotifRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 15, 2, 6),
    _AluTwampRefNotifRemotePort_Type()
)
aluTwampRefNotifRemotePort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    aluTwampRefNotifRemotePort.setStatus("current")
_AluVrtrConfObjs_ObjectIdentity = ObjectIdentity
aluVrtrConfObjs = _AluVrtrConfObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 18)
)
_AluVrtrConfExtTable_Object = MibTable
aluVrtrConfExtTable = _AluVrtrConfExtTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 18, 1)
)
if mibBuilder.loadTexts:
    aluVrtrConfExtTable.setStatus("current")
_AluVrtrConfExtEntry_Object = MibTableRow
aluVrtrConfExtEntry = _AluVrtrConfExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 18, 1, 1)
)
if mibBuilder.loadTexts:
    aluVrtrConfExtEntry.setStatus("current")


class _AluVrtr7705GrtState_Type(TruthValue):
    """Custom type aluVrtr7705GrtState based on TruthValue"""
    defaultValue = 2


_AluVrtr7705GrtState_Type.__name__ = "TruthValue"
_AluVrtr7705GrtState_Object = MibTableColumn
aluVrtr7705GrtState = _AluVrtr7705GrtState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 18, 1, 1, 1),
    _AluVrtr7705GrtState_Type()
)
aluVrtr7705GrtState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluVrtr7705GrtState.setStatus("current")
_AluVRtrNotifyPrefix_ObjectIdentity = ObjectIdentity
aluVRtrNotifyPrefix = _AluVRtrNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 11)
)
_AluVRtrNotifications_ObjectIdentity = ObjectIdentity
aluVRtrNotifications = _AluVRtrNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 11, 0)
)
_AluTwampNotifyPrefix_ObjectIdentity = ObjectIdentity
aluTwampNotifyPrefix = _AluTwampNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 12)
)
_AluTwampNotifications_ObjectIdentity = ObjectIdentity
aluTwampNotifications = _AluTwampNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 12, 0)
)
vRtrIfEntry.registerAugmentions(
    ("ALU-VRTR-MIB",
     "aluVrtrIfEntry")
)
aluVrtrIfEntry.setIndexNames(*vRtrIfEntry.getIndexNames())
vRtrIfStatsEntry.registerAugmentions(
    ("ALU-VRTR-MIB",
     "aluVRtrIfStatsEntry")
)
aluVRtrIfStatsEntry.setIndexNames(*vRtrIfStatsEntry.getIndexNames())
vRtrMplsIfStatEntry.registerAugmentions(
    ("ALU-VRTR-MIB",
     "aluVRtrMplsIfStatEntry")
)
aluVRtrMplsIfStatEntry.setIndexNames(*vRtrMplsIfStatEntry.getIndexNames())
vRtrIfExtEntry.registerAugmentions(
    ("ALU-VRTR-MIB",
     "aluVrtrIfExtEntry")
)
aluVrtrIfExtEntry.setIndexNames(*vRtrIfExtEntry.getIndexNames())
vRtrIfEntry.registerAugmentions(
    ("ALU-VRTR-MIB",
     "aluVrtrIpAddrEntry")
)
aluVrtrIpAddrEntry.setIndexNames(*vRtrIfEntry.getIndexNames())
vRtrConfExtEntry.registerAugmentions(
    ("ALU-VRTR-MIB",
     "aluVrtrConfExtEntry")
)
aluVrtrConfExtEntry.setIndexNames(*vRtrConfExtEntry.getIndexNames())

# Managed Objects groups

aluVrtrIf1588PtpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 8, 1, 2, 1)
)
aluVrtrIf1588PtpGroup.setObjects(
    ("ALU-VRTR-MIB", "aluVrtrIf1588Ptp")
)
if mibBuilder.loadTexts:
    aluVrtrIf1588PtpGroup.setStatus("current")

aluVrtrIfStatsV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 8, 1, 2, 2)
)
aluVrtrIfStatsV5v0Group.setObjects(
      *(("ALU-VRTR-MIB", "aluVRtrIfRxV4Pkts"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV4Bytes"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV6Pkts"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV6Bytes"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV4DiscardPkts"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV4DiscardBytes"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV4DiscardInvHdrCRCPkts"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV4DiscardInvHdrCRCBytes"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV4DiscardInvLenPkts"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV4DiscardInvLenBytes"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV4DiscardInvGREProtPkts"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV4DiscardInvGREProtBytes"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV4DiscardDestUnreachPkts"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV4DiscardDestUnreachBytes"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV4DiscardInvMcastPkts"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV4DiscardInvMcastBytes"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV4DiscardDirectBcastPkts"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV4DiscardDirectBcastBytes"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV4DiscardSrcMartianAddrPkts"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV4DiscardSrcMartianAddrBytes"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV4DiscardDestMartianAddrPkts"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV4DiscardDestMartianAddrBytes"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV4DiscardBlackHolePkts"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV4DiscardBlackHoleBytes"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV4DiscardFltrActionDropPkts"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV4DiscardFltrActionDropBytes"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV4DiscardFltrNxtHopUnreachPkts"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV4DiscardFltrNxtHopUnreachBytes"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV4DiscardFltrNxtHopNotDirectPkts"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV4DiscardFltrNxtHopNotDirectBytes"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV4OtherDiscardsPkts"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV4OtherDiscardsBytes"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV6DiscardPkts"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV6DiscardBytes"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV6DiscardInvLenPkts"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV6DiscardInvLenBytes"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV6DiscardDestUnreachPkts"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV6DiscardDestUnreachBytes"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV6DiscardInvMcastPkts"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV6DiscardInvMcastBytes"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV6DiscardSrcMartianAddrPkts"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV6DiscardSrcMartianAddrBytes"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV6DiscardDestMartianAddrPkts"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV6DiscardDestMartianAddrBytes"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV6DiscardBlackHolePkts"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV6DiscardBlackHoleBytes"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV6OtherDiscardsPkts"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV6OtherDiscardsBytes"))
)
if mibBuilder.loadTexts:
    aluVrtrIfStatsV5v0Group.setStatus("obsolete")

aluVrtrMplsIfStatsV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 8, 1, 2, 3)
)
aluVrtrMplsIfStatsV5v0Group.setObjects(
      *(("ALU-VRTR-MIB", "aluVRtrMplsIfRxInvLabels"),
        ("ALU-VRTR-MIB", "aluVRtrMplsIfRxInvIpoMplsPkts"),
        ("ALU-VRTR-MIB", "aluVRtrMplsIfRxStackTooBigPkts"),
        ("ALU-VRTR-MIB", "aluVRtrMplsIfRxOtherDiscardPkts"),
        ("ALU-VRTR-MIB", "aluVRtrMplsIfLastInvalidLabel"),
        ("ALU-VRTR-MIB", "aluVRtrMplsIfLastInvalidPos"))
)
if mibBuilder.loadTexts:
    aluVrtrMplsIfStatsV5v0Group.setStatus("current")

aluVRtrNotificationObjV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 8, 1, 2, 4)
)
aluVRtrNotificationObjV5v0Group.setObjects(
      *(("ALU-VRTR-MIB", "vRtrFibV6UnsupportedRoute"),
        ("ALU-VRTR-MIB", "vRtrFibV6TableThresholdExceed"))
)
if mibBuilder.loadTexts:
    aluVRtrNotificationObjV5v0Group.setStatus("current")

aluVRtrNotificationObjV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 8, 1, 2, 6)
)
aluVRtrNotificationObjV6v0Group.setObjects(
      *(("ALU-VRTR-MIB", "aluVRtrPimNgNtfySGLmtExcd"),
        ("ALU-VRTR-MIB", "aluVRtrPimNgNtfyMaxSG"))
)
if mibBuilder.loadTexts:
    aluVRtrNotificationObjV6v0Group.setStatus("current")

aluVRtrObsoletedObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 8, 1, 2, 8)
)
aluVRtrObsoletedObjectsGroup.setObjects(
    ("ALU-VRTR-MIB", "vRtrFibV6UnsupportedRoute")
)
if mibBuilder.loadTexts:
    aluVRtrObsoletedObjectsGroup.setStatus("current")

aluVrtrIfV6v1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 8, 1, 2, 10)
)
aluVrtrIfV6v1Group.setObjects(
    ("ALU-VRTR-MIB", "aluVrtrIfL4LoadBalancing")
)
if mibBuilder.loadTexts:
    aluVrtrIfV6v1Group.setStatus("current")

aluVrtrIfSecurityV6v1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 8, 1, 2, 11)
)
aluVrtrIfSecurityV6v1Group.setObjects(
      *(("ALU-VRTR-MIB", "aluVrtrIfSecurityConfigZoneId"),
        ("ALU-VRTR-MIB", "aluVrtrIfSecurityBypass"),
        ("ALU-VRTR-MIB", "aluVrtrIfSecurityOperZoneId"))
)
if mibBuilder.loadTexts:
    aluVrtrIfSecurityV6v1Group.setStatus("current")

aluVrtrMplsIfStatsV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 8, 1, 2, 12)
)
aluVrtrMplsIfStatsV6v0Group.setObjects(
      *(("ALU-VRTR-MIB", "aluVRtrMplsIfRxInvLabels"),
        ("ALU-VRTR-MIB", "aluVRtrMplsIfRxInvIpoMplsPkts"),
        ("ALU-VRTR-MIB", "aluVRtrMplsIfRxStackTooBigPkts"),
        ("ALU-VRTR-MIB", "aluVRtrMplsIfRxOtherDiscardPkts"),
        ("ALU-VRTR-MIB", "aluVRtrMplsIfLastInvalidLabel"),
        ("ALU-VRTR-MIB", "aluVRtrMplsIfLastInvalidPos"),
        ("ALU-VRTR-MIB", "aluVRtrMplsIfRxTTLExpiredPkts"))
)
if mibBuilder.loadTexts:
    aluVrtrMplsIfStatsV6v0Group.setStatus("current")

aluVrtrIfStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 8, 1, 2, 13)
)
aluVrtrIfStatsGroup.setObjects(
      *(("ALU-VRTR-MIB", "aluVRtrIfRxV4Pkts"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV4Bytes"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV6Pkts"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV6Bytes"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV4DiscardPkts"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV4DiscardBytes"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV4DiscardInvHdrCRCPkts"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV4DiscardInvHdrCRCBytes"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV4DiscardInvLenPkts"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV4DiscardInvLenBytes"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV4DiscardInvGREProtPkts"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV4DiscardInvGREProtBytes"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV4DiscardDestUnreachPkts"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV4DiscardDestUnreachBytes"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV4DiscardInvMcastPkts"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV4DiscardInvMcastBytes"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV4DiscardDirectBcastPkts"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV4DiscardDirectBcastBytes"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV4DiscardSrcMartianAddrPkts"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV4DiscardSrcMartianAddrBytes"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV4DiscardDestMartianAddrPkts"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV4DiscardDestMartianAddrBytes"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV4DiscardBlackHolePkts"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV4DiscardBlackHoleBytes"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV4DiscardFltrActionDropPkts"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV4DiscardFltrActionDropBytes"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV4DiscardFltrNxtHopUnreachPkts"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV4DiscardFltrNxtHopUnreachBytes"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV4DiscardFltrNxtHopNotDirectPkts"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV4DiscardFltrNxtHopNotDirectBytes"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV4DiscardTTLExpiredPkts"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV4DiscardTTLExpiredBytes"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV4DiscardSlowpathPkts"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV4DiscardSlowpathBytes"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV4DiscardMtuExceededPkts"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV4DiscardMtuExceededBytes"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV4DiscardQueuePkts"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV4DiscardQueueBytes"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV4DiscardEncryptionPkts"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV4DiscardEncryptionBytes"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV4DiscardEncryptionLastTunnel"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV4OtherDiscardsPkts"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV4OtherDiscardsBytes"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV6DiscardPkts"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV6DiscardBytes"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV6DiscardInvLenPkts"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV6DiscardInvLenBytes"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV6DiscardDestUnreachPkts"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV6DiscardDestUnreachBytes"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV6DiscardInvMcastPkts"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV6DiscardInvMcastBytes"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV6DiscardSrcMartianAddrPkts"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV6DiscardSrcMartianAddrBytes"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV6DiscardDestMartianAddrPkts"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV6DiscardDestMartianAddrBytes"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV6DiscardBlackHolePkts"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV6DiscardBlackHoleBytes"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV6DiscardTTLExpiredPkts"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV6DiscardTTLExpiredBytes"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV6DiscardSlowpathPkts"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV6DiscardSlowpathBytes"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV6DiscardMtuExceededPkts"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV6DiscardMtuExceededBytes"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV6DiscardQueuePkts"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV6DiscardQueueBytes"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV6DiscardFltrActionDropPkts"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV6DiscardFltrActionDropBytes"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV6OtherDiscardsPkts"),
        ("ALU-VRTR-MIB", "aluVRtrIfRxV6OtherDiscardsBytes"),
        ("ALU-VRTR-MIB", "aluVRtrIfTxV4DiscardPkts"),
        ("ALU-VRTR-MIB", "aluVRtrIfTxV4DiscardBytes"),
        ("ALU-VRTR-MIB", "aluVRtrIfTxV4DiscardFltrActionDropPkts"),
        ("ALU-VRTR-MIB", "aluVRtrIfTxV4DiscardFltrActionDropBytes"),
        ("ALU-VRTR-MIB", "aluVRtrIfTxV4DiscardEncryptionPkts"),
        ("ALU-VRTR-MIB", "aluVRtrIfTxV4DiscardEncryptionBytes"),
        ("ALU-VRTR-MIB", "aluVRtrIfTxV4DiscardEncryptionLastTunnel"),
        ("ALU-VRTR-MIB", "aluVRtrIfTxV4DiscardOtherDiscardsPkts"),
        ("ALU-VRTR-MIB", "aluVRtrIfTxV4DiscardOtherDiscardsBytes"),
        ("ALU-VRTR-MIB", "aluVRtrIfTxV6DiscardPkts"),
        ("ALU-VRTR-MIB", "aluVRtrIfTxV6DiscardBytes"),
        ("ALU-VRTR-MIB", "aluVRtrIfTxV6DiscardFltrActionDropPkts"),
        ("ALU-VRTR-MIB", "aluVRtrIfTxV6DiscardFltrActionDropBytes"),
        ("ALU-VRTR-MIB", "aluVRtrIfTxV6DiscardOtherDiscardsPkts"),
        ("ALU-VRTR-MIB", "aluVRtrIfTxV6DiscardOtherDiscardsBytes"),
        ("ALU-VRTR-MIB", "aluVRtrIfSecRxCtrlQueueFwdPkts"),
        ("ALU-VRTR-MIB", "aluVRtrIfSecRxCtrlQueueFwdBytes"),
        ("ALU-VRTR-MIB", "aluVRtrIfSecRxCtrlQueueDroPkts"),
        ("ALU-VRTR-MIB", "aluVRtrIfSecRxCtrlQueueDroBytes"),
        ("ALU-VRTR-MIB", "aluVRtrIfSecBadProtoDroPkts"),
        ("ALU-VRTR-MIB", "aluVRtrIfSecBadProtoDroBytes"),
        ("ALU-VRTR-MIB", "aluVRtrIfSecBadServiceDroPkts"),
        ("ALU-VRTR-MIB", "aluVRtrIfSecBadServiceDroBytes"),
        ("ALU-VRTR-MIB", "aluVRtrIfSecNoSessionDroPkts"),
        ("ALU-VRTR-MIB", "aluVRtrIfSecNoSessionDroBytes"),
        ("ALU-VRTR-MIB", "aluVRtrIfSecFragmentsDroPkts"),
        ("ALU-VRTR-MIB", "aluVRtrIfSecFragmentsDroBytes"),
        ("ALU-VRTR-MIB", "aluVRtrIfSecBadIcmpTypeDroPkts"),
        ("ALU-VRTR-MIB", "aluVRtrIfSecBadIcmpTypeDroBytes"),
        ("ALU-VRTR-MIB", "aluVRtrIfSecRouteLoopDroPkts"),
        ("ALU-VRTR-MIB", "aluVRtrIfSecRouteLoopDroBytes"),
        ("ALU-VRTR-MIB", "aluVRtrIfSecOtherDroPkts"),
        ("ALU-VRTR-MIB", "aluVRtrIfSecOtherDroBytes"))
)
if mibBuilder.loadTexts:
    aluVrtrIfStatsGroup.setStatus("current")

aluVrtrIfNetworkEgrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 8, 1, 2, 14)
)
aluVrtrIfNetworkEgrGroup.setObjects(
      *(("ALU-VRTR-MIB", "aluVrtrIfNetworkEgrQueuePol"),
        ("ALU-VRTR-MIB", "aluVrtrIfNetworkEgrAggRate"),
        ("ALU-VRTR-MIB", "aluVrtrIfNetworkEgrAggCir"),
        ("ALU-VRTR-MIB", "aluVrtrIfNetEgrFwdInProfPkts"),
        ("ALU-VRTR-MIB", "aluVrtrIfNetEgrFwdOutProfPkts"),
        ("ALU-VRTR-MIB", "aluVrtrIfNetEgrFwdInProfOcts"),
        ("ALU-VRTR-MIB", "aluVrtrIfNetEgrFwdOutProfOcts"),
        ("ALU-VRTR-MIB", "aluVrtrIfNetEgrDroInProfPkts"),
        ("ALU-VRTR-MIB", "aluVrtrIfNetEgrDroOutProfPkts"),
        ("ALU-VRTR-MIB", "aluVrtrIfNetEgrDroInProfOcts"),
        ("ALU-VRTR-MIB", "aluVrtrIfNetEgrDroOutProfOcts"))
)
if mibBuilder.loadTexts:
    aluVrtrIfNetworkEgrGroup.setStatus("current")

aluVrtrMplsIfStatsV6v1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 8, 1, 2, 15)
)
aluVrtrMplsIfStatsV6v1Group.setObjects(
      *(("ALU-VRTR-MIB", "aluVRtrMplsIfRxMtuExceedPkts"),
        ("ALU-VRTR-MIB", "aluVRtrMplsIfRxQueueDiscardPkts"))
)
if mibBuilder.loadTexts:
    aluVrtrMplsIfStatsV6v1Group.setStatus("current")

aluVrtrIpAddrDhcpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 14, 1, 2, 1)
)
aluVrtrIpAddrDhcpGroup.setObjects(
      *(("ALU-VRTR-MIB", "aluVrtrIpAddrDhcpClient"),
        ("ALU-VRTR-MIB", "aluVrtrIpAddrClientId"),
        ("ALU-VRTR-MIB", "aluVrtrIpAddrClassId"))
)
if mibBuilder.loadTexts:
    aluVrtrIpAddrDhcpGroup.setStatus("current")

aluTwampV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 15, 1, 2, 1, 1)
)
aluTwampV6v0Group.setObjects(
    ("ALU-VRTR-MIB", "aluTwampRefInactTimeout")
)
if mibBuilder.loadTexts:
    aluTwampV6v0Group.setStatus("current")

aluTwampNotifyObjsV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 15, 1, 2, 1, 3)
)
aluTwampNotifyObjsV6v0Group.setObjects(
      *(("ALU-VRTR-MIB", "aluTwampRefNotifLocalAddrType"),
        ("ALU-VRTR-MIB", "aluTwampRefNotifLocalAddr"),
        ("ALU-VRTR-MIB", "aluTwampRefNotifLocalPort"),
        ("ALU-VRTR-MIB", "aluTwampRefNotifRemoteAddrType"),
        ("ALU-VRTR-MIB", "aluTwampRefNotifRemoteAddr"),
        ("ALU-VRTR-MIB", "aluTwampRefNotifRemotePort"))
)
if mibBuilder.loadTexts:
    aluTwampNotifyObjsV6v0Group.setStatus("current")

aluVrtrConfV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 18, 1, 2, 1, 1)
)
aluVrtrConfV6v0Group.setObjects(
    ("ALU-VRTR-MIB", "aluVrtr7705GrtState")
)
if mibBuilder.loadTexts:
    aluVrtrConfV6v0Group.setStatus("current")


# Notification objects

aluVRtrFibV6UnsupportedRoute = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 11, 0, 1)
)
aluVRtrFibV6UnsupportedRoute.setObjects(
    ("ALU-VRTR-MIB", "vRtrFibV6UnsupportedRoute")
)
if mibBuilder.loadTexts:
    aluVRtrFibV6UnsupportedRoute.setStatus(
        "obsolete"
    )

aluVRtrFibV6TableThresholdExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 11, 0, 2)
)
aluVRtrFibV6TableThresholdExceed.setObjects(
    ("ALU-VRTR-MIB", "vRtrFibV6TableThresholdExceed")
)
if mibBuilder.loadTexts:
    aluVRtrFibV6TableThresholdExceed.setStatus(
        "current"
    )

aluVRtrPimNgUnsupportedStarG = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 11, 0, 3)
)
aluVRtrPimNgUnsupportedStarG.setObjects(
      *(("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfRxPkts"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgNotifyGroupAddrType"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgNotifyGroupAddr"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgNotifyMsgType"))
)
if mibBuilder.loadTexts:
    aluVRtrPimNgUnsupportedStarG.setStatus(
        "current"
    )

aluVRtrPimNgSGLimitExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 11, 0, 4)
)
aluVRtrPimNgSGLimitExceeded.setObjects(
      *(("ALU-VRTR-MIB", "aluVRtrPimNgNtfySGLmtExcd"),
        ("ALU-VRTR-MIB", "aluVRtrPimNgNtfyMaxSG"))
)
if mibBuilder.loadTexts:
    aluVRtrPimNgSGLimitExceeded.setStatus(
        "current"
    )

aluTwampRefInactivityTimeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 12, 0, 1)
)
aluTwampRefInactivityTimeout.setObjects(
      *(("TIMETRA-TWAMP-MIB", "tmnxTwampSrvNotifClientAddrType"),
        ("TIMETRA-TWAMP-MIB", "tmnxTwampSrvNotifClientAddr"),
        ("ALU-VRTR-MIB", "aluTwampRefNotifLocalAddrType"),
        ("ALU-VRTR-MIB", "aluTwampRefNotifLocalAddr"),
        ("ALU-VRTR-MIB", "aluTwampRefNotifLocalPort"),
        ("ALU-VRTR-MIB", "aluTwampRefNotifRemoteAddrType"),
        ("ALU-VRTR-MIB", "aluTwampRefNotifRemoteAddr"),
        ("ALU-VRTR-MIB", "aluTwampRefNotifRemotePort"))
)
if mibBuilder.loadTexts:
    aluTwampRefInactivityTimeout.setStatus(
        "current"
    )


# Notifications groups

aluVRtrNotificationV5v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 8, 1, 2, 5)
)
aluVRtrNotificationV5v0Group.setObjects(
      *(("ALU-VRTR-MIB", "aluVRtrFibV6UnsupportedRoute"),
        ("ALU-VRTR-MIB", "aluVRtrFibV6TableThresholdExceed"))
)
if mibBuilder.loadTexts:
    aluVRtrNotificationV5v0Group.setStatus(
        "current"
    )

aluVRtrNotificationV6v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 8, 1, 2, 7)
)
aluVRtrNotificationV6v0Group.setObjects(
      *(("ALU-VRTR-MIB", "aluVRtrPimNgUnsupportedStarG"),
        ("ALU-VRTR-MIB", "aluVRtrPimNgSGLimitExceeded"))
)
if mibBuilder.loadTexts:
    aluVRtrNotificationV6v0Group.setStatus(
        "current"
    )

aluVRtrObsoleteNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 8, 1, 2, 9)
)
aluVRtrObsoleteNotificationGroup.setObjects(
    ("ALU-VRTR-MIB", "aluVRtrFibV6UnsupportedRoute")
)
if mibBuilder.loadTexts:
    aluVRtrObsoleteNotificationGroup.setStatus(
        "current"
    )

aluTwampNotifyV6v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 15, 1, 2, 1, 2)
)
aluTwampNotifyV6v0Group.setObjects(
    ("ALU-VRTR-MIB", "aluTwampRefInactivityTimeout")
)
if mibBuilder.loadTexts:
    aluTwampNotifyV6v0Group.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

aluVrtrIfComp7705V1v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 8, 1, 1, 1, 1)
)
aluVrtrIfComp7705V1v0.setObjects(
    ("ALU-VRTR-MIB", "aluVrtrIf1588PtpGroup")
)
if mibBuilder.loadTexts:
    aluVrtrIfComp7705V1v0.setStatus(
        "current"
    )

aluVrtrIfComp7705V5v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 8, 1, 1, 1, 2)
)
aluVrtrIfComp7705V5v0.setObjects(
      *(("ALU-VRTR-MIB", "aluVrtrIfStatsV5v0Group"),
        ("ALU-VRTR-MIB", "aluVrtrMplsIfStatsV5v0Group"),
        ("ALU-VRTR-MIB", "aluVRtrNotificationV5v0Group"))
)
if mibBuilder.loadTexts:
    aluVrtrIfComp7705V5v0.setStatus(
        "current"
    )

aluVrtrIfComp7705V6v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 8, 1, 1, 1, 3)
)
aluVrtrIfComp7705V6v0.setObjects(
      *(("ALU-VRTR-MIB", "aluVrtrIf1588PtpGroup"),
        ("ALU-VRTR-MIB", "aluVrtrIfStatsV5v0Group"),
        ("ALU-VRTR-MIB", "aluVrtrMplsIfStatsV6v0Group"),
        ("ALU-VRTR-MIB", "aluVRtrNotificationV5v0Group"),
        ("ALU-VRTR-MIB", "aluVRtrNotificationV6v0Group"))
)
if mibBuilder.loadTexts:
    aluVrtrIfComp7705V6v0.setStatus(
        "current"
    )

aluVrtrIfComp7705V6v1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 8, 1, 1, 1, 4)
)
aluVrtrIfComp7705V6v1.setObjects(
      *(("ALU-VRTR-MIB", "aluVrtrIf1588PtpGroup"),
        ("ALU-VRTR-MIB", "aluVrtrIfStatsV5v0Group"),
        ("ALU-VRTR-MIB", "aluVrtrMplsIfStatsV6v0Group"),
        ("ALU-VRTR-MIB", "aluVRtrNotificationV5v0Group"),
        ("ALU-VRTR-MIB", "aluVRtrNotificationV6v0Group"),
        ("ALU-VRTR-MIB", "aluVrtrIfV6v1Group"),
        ("ALU-VRTR-MIB", "aluVrtrMplsIfStatsV6v1Group"))
)
if mibBuilder.loadTexts:
    aluVrtrIfComp7705V6v1.setStatus(
        "current"
    )

aluVrtrIpAddrComp7705V6v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 14, 1, 1, 1, 1)
)
aluVrtrIpAddrComp7705V6v0.setObjects(
    ("ALU-VRTR-MIB", "aluVrtrIpAddrDhcpGroup")
)
if mibBuilder.loadTexts:
    aluVrtrIpAddrComp7705V6v0.setStatus(
        "current"
    )

aluTwampCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 15, 1, 1, 1)
)
aluTwampCompliance.setObjects(
      *(("ALU-VRTR-MIB", "aluTwampV6v0Group"),
        ("ALU-VRTR-MIB", "aluTwampNotifyV6v0Group"),
        ("ALU-VRTR-MIB", "aluTwampNotifyObjsV6v0Group"))
)
if mibBuilder.loadTexts:
    aluTwampCompliance.setStatus(
        "current"
    )

aluVrtrConfCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 18, 1, 1, 1)
)
aluVrtrConfCompliance.setObjects(
    ("ALU-VRTR-MIB", "aluVrtrConfV6v0Group")
)
if mibBuilder.loadTexts:
    aluVrtrConfCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALU-VRTR-MIB",
    **{"aluVRTRMIBModule": aluVRTRMIBModule,
       "aluVrtrIfMIBConformance": aluVrtrIfMIBConformance,
       "aluVrtrIfConformance": aluVrtrIfConformance,
       "aluVrtrIfCompliances": aluVrtrIfCompliances,
       "aluVrtrIfComp7705": aluVrtrIfComp7705,
       "aluVrtrIfComp7705V1v0": aluVrtrIfComp7705V1v0,
       "aluVrtrIfComp7705V5v0": aluVrtrIfComp7705V5v0,
       "aluVrtrIfComp7705V6v0": aluVrtrIfComp7705V6v0,
       "aluVrtrIfComp7705V6v1": aluVrtrIfComp7705V6v1,
       "aluVrtrIfGroups": aluVrtrIfGroups,
       "aluVrtrIf1588PtpGroup": aluVrtrIf1588PtpGroup,
       "aluVrtrIfStatsV5v0Group": aluVrtrIfStatsV5v0Group,
       "aluVrtrMplsIfStatsV5v0Group": aluVrtrMplsIfStatsV5v0Group,
       "aluVRtrNotificationObjV5v0Group": aluVRtrNotificationObjV5v0Group,
       "aluVRtrNotificationV5v0Group": aluVRtrNotificationV5v0Group,
       "aluVRtrNotificationObjV6v0Group": aluVRtrNotificationObjV6v0Group,
       "aluVRtrNotificationV6v0Group": aluVRtrNotificationV6v0Group,
       "aluVRtrObsoletedObjectsGroup": aluVRtrObsoletedObjectsGroup,
       "aluVRtrObsoleteNotificationGroup": aluVRtrObsoleteNotificationGroup,
       "aluVrtrIfV6v1Group": aluVrtrIfV6v1Group,
       "aluVrtrIfSecurityV6v1Group": aluVrtrIfSecurityV6v1Group,
       "aluVrtrMplsIfStatsV6v0Group": aluVrtrMplsIfStatsV6v0Group,
       "aluVrtrIfStatsGroup": aluVrtrIfStatsGroup,
       "aluVrtrIfNetworkEgrGroup": aluVrtrIfNetworkEgrGroup,
       "aluVrtrMplsIfStatsV6v1Group": aluVrtrMplsIfStatsV6v1Group,
       "aluVrtrIpAddrMIBConformance": aluVrtrIpAddrMIBConformance,
       "aluVrtrIpAddrConformance": aluVrtrIpAddrConformance,
       "aluVrtrIpAddrCompliances": aluVrtrIpAddrCompliances,
       "aluVrtrIpAddrComp7705": aluVrtrIpAddrComp7705,
       "aluVrtrIpAddrComp7705V6v0": aluVrtrIpAddrComp7705V6v0,
       "aluVrtrIpAddrGroups": aluVrtrIpAddrGroups,
       "aluVrtrIpAddrDhcpGroup": aluVrtrIpAddrDhcpGroup,
       "aluTwampMIBConformance": aluTwampMIBConformance,
       "aluTwampConformance": aluTwampConformance,
       "aluTwampComplianceObjs": aluTwampComplianceObjs,
       "aluTwampCompliance": aluTwampCompliance,
       "aluTwampGroupObjs": aluTwampGroupObjs,
       "aluTwampV6v0GroupObjs": aluTwampV6v0GroupObjs,
       "aluTwampV6v0Group": aluTwampV6v0Group,
       "aluTwampNotifyV6v0Group": aluTwampNotifyV6v0Group,
       "aluTwampNotifyObjsV6v0Group": aluTwampNotifyObjsV6v0Group,
       "aluVrtrConfMIBConformance": aluVrtrConfMIBConformance,
       "aluVrtrConfConformance": aluVrtrConfConformance,
       "aluVrtrConfConformanceObjs": aluVrtrConfConformanceObjs,
       "aluVrtrConfCompliance": aluVrtrConfCompliance,
       "aluVrtrConfGroupObjs": aluVrtrConfGroupObjs,
       "aluVrtrConfV6V0GroupObjs": aluVrtrConfV6V0GroupObjs,
       "aluVrtrConfV6v0Group": aluVrtrConfV6v0Group,
       "aluVrtrIfObjs": aluVrtrIfObjs,
       "aluVrtrIfTable": aluVrtrIfTable,
       "aluVrtrIfEntry": aluVrtrIfEntry,
       "aluVrtrIf1588Ptp": aluVrtrIf1588Ptp,
       "aluVRtrIfStatsTable": aluVRtrIfStatsTable,
       "aluVRtrIfStatsEntry": aluVRtrIfStatsEntry,
       "aluVRtrIfRxV4Pkts": aluVRtrIfRxV4Pkts,
       "aluVRtrIfRxV4Bytes": aluVRtrIfRxV4Bytes,
       "aluVRtrIfRxV6Pkts": aluVRtrIfRxV6Pkts,
       "aluVRtrIfRxV6Bytes": aluVRtrIfRxV6Bytes,
       "aluVRtrIfRxV4DiscardPkts": aluVRtrIfRxV4DiscardPkts,
       "aluVRtrIfRxV4DiscardBytes": aluVRtrIfRxV4DiscardBytes,
       "aluVRtrIfRxV4DiscardInvHdrCRCPkts": aluVRtrIfRxV4DiscardInvHdrCRCPkts,
       "aluVRtrIfRxV4DiscardInvHdrCRCBytes": aluVRtrIfRxV4DiscardInvHdrCRCBytes,
       "aluVRtrIfRxV4DiscardInvLenPkts": aluVRtrIfRxV4DiscardInvLenPkts,
       "aluVRtrIfRxV4DiscardInvLenBytes": aluVRtrIfRxV4DiscardInvLenBytes,
       "aluVRtrIfRxV4DiscardInvGREProtPkts": aluVRtrIfRxV4DiscardInvGREProtPkts,
       "aluVRtrIfRxV4DiscardInvGREProtBytes": aluVRtrIfRxV4DiscardInvGREProtBytes,
       "aluVRtrIfRxV4DiscardDestUnreachPkts": aluVRtrIfRxV4DiscardDestUnreachPkts,
       "aluVRtrIfRxV4DiscardDestUnreachBytes": aluVRtrIfRxV4DiscardDestUnreachBytes,
       "aluVRtrIfRxV4DiscardInvMcastPkts": aluVRtrIfRxV4DiscardInvMcastPkts,
       "aluVRtrIfRxV4DiscardInvMcastBytes": aluVRtrIfRxV4DiscardInvMcastBytes,
       "aluVRtrIfRxV4DiscardDirectBcastPkts": aluVRtrIfRxV4DiscardDirectBcastPkts,
       "aluVRtrIfRxV4DiscardDirectBcastBytes": aluVRtrIfRxV4DiscardDirectBcastBytes,
       "aluVRtrIfRxV4DiscardSrcMartianAddrPkts": aluVRtrIfRxV4DiscardSrcMartianAddrPkts,
       "aluVRtrIfRxV4DiscardSrcMartianAddrBytes": aluVRtrIfRxV4DiscardSrcMartianAddrBytes,
       "aluVRtrIfRxV4DiscardDestMartianAddrPkts": aluVRtrIfRxV4DiscardDestMartianAddrPkts,
       "aluVRtrIfRxV4DiscardDestMartianAddrBytes": aluVRtrIfRxV4DiscardDestMartianAddrBytes,
       "aluVRtrIfRxV4DiscardBlackHolePkts": aluVRtrIfRxV4DiscardBlackHolePkts,
       "aluVRtrIfRxV4DiscardBlackHoleBytes": aluVRtrIfRxV4DiscardBlackHoleBytes,
       "aluVRtrIfRxV4DiscardFltrActionDropPkts": aluVRtrIfRxV4DiscardFltrActionDropPkts,
       "aluVRtrIfRxV4DiscardFltrActionDropBytes": aluVRtrIfRxV4DiscardFltrActionDropBytes,
       "aluVRtrIfRxV4DiscardFltrNxtHopUnreachPkts": aluVRtrIfRxV4DiscardFltrNxtHopUnreachPkts,
       "aluVRtrIfRxV4DiscardFltrNxtHopUnreachBytes": aluVRtrIfRxV4DiscardFltrNxtHopUnreachBytes,
       "aluVRtrIfRxV4DiscardFltrNxtHopNotDirectPkts": aluVRtrIfRxV4DiscardFltrNxtHopNotDirectPkts,
       "aluVRtrIfRxV4DiscardFltrNxtHopNotDirectBytes": aluVRtrIfRxV4DiscardFltrNxtHopNotDirectBytes,
       "aluVRtrIfRxV4DiscardTTLExpiredPkts": aluVRtrIfRxV4DiscardTTLExpiredPkts,
       "aluVRtrIfRxV4DiscardTTLExpiredBytes": aluVRtrIfRxV4DiscardTTLExpiredBytes,
       "aluVRtrIfRxV4DiscardSlowpathPkts": aluVRtrIfRxV4DiscardSlowpathPkts,
       "aluVRtrIfRxV4DiscardSlowpathBytes": aluVRtrIfRxV4DiscardSlowpathBytes,
       "aluVRtrIfRxV4DiscardMtuExceededPkts": aluVRtrIfRxV4DiscardMtuExceededPkts,
       "aluVRtrIfRxV4DiscardMtuExceededBytes": aluVRtrIfRxV4DiscardMtuExceededBytes,
       "aluVRtrIfRxV4DiscardQueuePkts": aluVRtrIfRxV4DiscardQueuePkts,
       "aluVRtrIfRxV4DiscardQueueBytes": aluVRtrIfRxV4DiscardQueueBytes,
       "aluVRtrIfRxV4DiscardEncryptionPkts": aluVRtrIfRxV4DiscardEncryptionPkts,
       "aluVRtrIfRxV4DiscardEncryptionBytes": aluVRtrIfRxV4DiscardEncryptionBytes,
       "aluVRtrIfRxV4DiscardEncryptionLastTunnel": aluVRtrIfRxV4DiscardEncryptionLastTunnel,
       "aluVRtrIfRxV4OtherDiscardsPkts": aluVRtrIfRxV4OtherDiscardsPkts,
       "aluVRtrIfRxV4OtherDiscardsBytes": aluVRtrIfRxV4OtherDiscardsBytes,
       "aluVRtrIfRxV6DiscardPkts": aluVRtrIfRxV6DiscardPkts,
       "aluVRtrIfRxV6DiscardBytes": aluVRtrIfRxV6DiscardBytes,
       "aluVRtrIfRxV6DiscardInvLenPkts": aluVRtrIfRxV6DiscardInvLenPkts,
       "aluVRtrIfRxV6DiscardInvLenBytes": aluVRtrIfRxV6DiscardInvLenBytes,
       "aluVRtrIfRxV6DiscardDestUnreachPkts": aluVRtrIfRxV6DiscardDestUnreachPkts,
       "aluVRtrIfRxV6DiscardDestUnreachBytes": aluVRtrIfRxV6DiscardDestUnreachBytes,
       "aluVRtrIfRxV6DiscardInvMcastPkts": aluVRtrIfRxV6DiscardInvMcastPkts,
       "aluVRtrIfRxV6DiscardInvMcastBytes": aluVRtrIfRxV6DiscardInvMcastBytes,
       "aluVRtrIfRxV6DiscardSrcMartianAddrPkts": aluVRtrIfRxV6DiscardSrcMartianAddrPkts,
       "aluVRtrIfRxV6DiscardSrcMartianAddrBytes": aluVRtrIfRxV6DiscardSrcMartianAddrBytes,
       "aluVRtrIfRxV6DiscardDestMartianAddrPkts": aluVRtrIfRxV6DiscardDestMartianAddrPkts,
       "aluVRtrIfRxV6DiscardDestMartianAddrBytes": aluVRtrIfRxV6DiscardDestMartianAddrBytes,
       "aluVRtrIfRxV6DiscardBlackHolePkts": aluVRtrIfRxV6DiscardBlackHolePkts,
       "aluVRtrIfRxV6DiscardBlackHoleBytes": aluVRtrIfRxV6DiscardBlackHoleBytes,
       "aluVRtrIfRxV6DiscardTTLExpiredPkts": aluVRtrIfRxV6DiscardTTLExpiredPkts,
       "aluVRtrIfRxV6DiscardTTLExpiredBytes": aluVRtrIfRxV6DiscardTTLExpiredBytes,
       "aluVRtrIfRxV6DiscardSlowpathPkts": aluVRtrIfRxV6DiscardSlowpathPkts,
       "aluVRtrIfRxV6DiscardSlowpathBytes": aluVRtrIfRxV6DiscardSlowpathBytes,
       "aluVRtrIfRxV6DiscardMtuExceededPkts": aluVRtrIfRxV6DiscardMtuExceededPkts,
       "aluVRtrIfRxV6DiscardMtuExceededBytes": aluVRtrIfRxV6DiscardMtuExceededBytes,
       "aluVRtrIfRxV6DiscardFltrActionDropPkts": aluVRtrIfRxV6DiscardFltrActionDropPkts,
       "aluVRtrIfRxV6DiscardFltrActionDropBytes": aluVRtrIfRxV6DiscardFltrActionDropBytes,
       "aluVRtrIfRxV6DiscardQueuePkts": aluVRtrIfRxV6DiscardQueuePkts,
       "aluVRtrIfRxV6DiscardQueueBytes": aluVRtrIfRxV6DiscardQueueBytes,
       "aluVRtrIfRxV6OtherDiscardsPkts": aluVRtrIfRxV6OtherDiscardsPkts,
       "aluVRtrIfRxV6OtherDiscardsBytes": aluVRtrIfRxV6OtherDiscardsBytes,
       "aluVRtrIfTxV4DiscardPkts": aluVRtrIfTxV4DiscardPkts,
       "aluVRtrIfTxV4DiscardBytes": aluVRtrIfTxV4DiscardBytes,
       "aluVRtrIfTxV4DiscardFltrActionDropPkts": aluVRtrIfTxV4DiscardFltrActionDropPkts,
       "aluVRtrIfTxV4DiscardFltrActionDropBytes": aluVRtrIfTxV4DiscardFltrActionDropBytes,
       "aluVRtrIfTxV4DiscardEncryptionPkts": aluVRtrIfTxV4DiscardEncryptionPkts,
       "aluVRtrIfTxV4DiscardEncryptionBytes": aluVRtrIfTxV4DiscardEncryptionBytes,
       "aluVRtrIfTxV4DiscardEncryptionLastTunnel": aluVRtrIfTxV4DiscardEncryptionLastTunnel,
       "aluVRtrIfTxV4DiscardOtherDiscardsPkts": aluVRtrIfTxV4DiscardOtherDiscardsPkts,
       "aluVRtrIfTxV4DiscardOtherDiscardsBytes": aluVRtrIfTxV4DiscardOtherDiscardsBytes,
       "aluVRtrIfTxV6DiscardPkts": aluVRtrIfTxV6DiscardPkts,
       "aluVRtrIfTxV6DiscardBytes": aluVRtrIfTxV6DiscardBytes,
       "aluVRtrIfTxV6DiscardFltrActionDropPkts": aluVRtrIfTxV6DiscardFltrActionDropPkts,
       "aluVRtrIfTxV6DiscardFltrActionDropBytes": aluVRtrIfTxV6DiscardFltrActionDropBytes,
       "aluVRtrIfTxV6DiscardOtherDiscardsPkts": aluVRtrIfTxV6DiscardOtherDiscardsPkts,
       "aluVRtrIfTxV6DiscardOtherDiscardsBytes": aluVRtrIfTxV6DiscardOtherDiscardsBytes,
       "aluVRtrIfSecRxCtrlQueueFwdPkts": aluVRtrIfSecRxCtrlQueueFwdPkts,
       "aluVRtrIfSecRxCtrlQueueFwdBytes": aluVRtrIfSecRxCtrlQueueFwdBytes,
       "aluVRtrIfSecRxCtrlQueueDroPkts": aluVRtrIfSecRxCtrlQueueDroPkts,
       "aluVRtrIfSecRxCtrlQueueDroBytes": aluVRtrIfSecRxCtrlQueueDroBytes,
       "aluVRtrIfSecBadProtoDroPkts": aluVRtrIfSecBadProtoDroPkts,
       "aluVRtrIfSecBadProtoDroBytes": aluVRtrIfSecBadProtoDroBytes,
       "aluVRtrIfSecBadServiceDroPkts": aluVRtrIfSecBadServiceDroPkts,
       "aluVRtrIfSecBadServiceDroBytes": aluVRtrIfSecBadServiceDroBytes,
       "aluVRtrIfSecNoSessionDroPkts": aluVRtrIfSecNoSessionDroPkts,
       "aluVRtrIfSecNoSessionDroBytes": aluVRtrIfSecNoSessionDroBytes,
       "aluVRtrIfSecFragmentsDroPkts": aluVRtrIfSecFragmentsDroPkts,
       "aluVRtrIfSecFragmentsDroBytes": aluVRtrIfSecFragmentsDroBytes,
       "aluVRtrIfSecBadIcmpTypeDroPkts": aluVRtrIfSecBadIcmpTypeDroPkts,
       "aluVRtrIfSecBadIcmpTypeDroBytes": aluVRtrIfSecBadIcmpTypeDroBytes,
       "aluVRtrIfSecRouteLoopDroPkts": aluVRtrIfSecRouteLoopDroPkts,
       "aluVRtrIfSecRouteLoopDroBytes": aluVRtrIfSecRouteLoopDroBytes,
       "aluVRtrIfSecOtherDroPkts": aluVRtrIfSecOtherDroPkts,
       "aluVRtrIfSecOtherDroBytes": aluVRtrIfSecOtherDroBytes,
       "aluVRtrMplsIfStatTable": aluVRtrMplsIfStatTable,
       "aluVRtrMplsIfStatEntry": aluVRtrMplsIfStatEntry,
       "aluVRtrMplsIfRxInvLabels": aluVRtrMplsIfRxInvLabels,
       "aluVRtrMplsIfRxInvIpoMplsPkts": aluVRtrMplsIfRxInvIpoMplsPkts,
       "aluVRtrMplsIfRxStackTooBigPkts": aluVRtrMplsIfRxStackTooBigPkts,
       "aluVRtrMplsIfRxOtherDiscardPkts": aluVRtrMplsIfRxOtherDiscardPkts,
       "aluVRtrMplsIfLastInvalidLabel": aluVRtrMplsIfLastInvalidLabel,
       "aluVRtrMplsIfLastInvalidPos": aluVRtrMplsIfLastInvalidPos,
       "aluVRtrMplsIfRxTTLExpiredPkts": aluVRtrMplsIfRxTTLExpiredPkts,
       "aluVRtrMplsIfRxMtuExceedPkts": aluVRtrMplsIfRxMtuExceedPkts,
       "aluVRtrMplsIfRxQueueDiscardPkts": aluVRtrMplsIfRxQueueDiscardPkts,
       "aluVRtrNotificationObjects": aluVRtrNotificationObjects,
       "vRtrFibV6UnsupportedRoute": vRtrFibV6UnsupportedRoute,
       "vRtrFibV6TableThresholdExceed": vRtrFibV6TableThresholdExceed,
       "aluVRtrPimNgNtfySGLmtExcd": aluVRtrPimNgNtfySGLmtExcd,
       "aluVRtrPimNgNtfyMaxSG": aluVRtrPimNgNtfyMaxSG,
       "aluVrtrIfExtTable": aluVrtrIfExtTable,
       "aluVrtrIfExtEntry": aluVrtrIfExtEntry,
       "aluVrtrIfL4LoadBalancing": aluVrtrIfL4LoadBalancing,
       "aluVrtrIfSecurityConfigZoneId": aluVrtrIfSecurityConfigZoneId,
       "aluVrtrIfSecurityOperZoneId": aluVrtrIfSecurityOperZoneId,
       "aluVrtrIfSecurityBypass": aluVrtrIfSecurityBypass,
       "aluVrtrIfNetworkEgrQueuePol": aluVrtrIfNetworkEgrQueuePol,
       "aluVrtrIfNetworkEgrAggRate": aluVrtrIfNetworkEgrAggRate,
       "aluVrtrIfNetworkEgrAggCir": aluVrtrIfNetworkEgrAggCir,
       "aluVrtrIfNetEgrStatsTable": aluVrtrIfNetEgrStatsTable,
       "aluVrtrIfNetEgrStatsEntry": aluVrtrIfNetEgrStatsEntry,
       "aluVrtrIfNetEgrQueueIndex": aluVrtrIfNetEgrQueueIndex,
       "aluVrtrIfNetEgrFwdInProfPkts": aluVrtrIfNetEgrFwdInProfPkts,
       "aluVrtrIfNetEgrFwdOutProfPkts": aluVrtrIfNetEgrFwdOutProfPkts,
       "aluVrtrIfNetEgrFwdInProfOcts": aluVrtrIfNetEgrFwdInProfOcts,
       "aluVrtrIfNetEgrFwdOutProfOcts": aluVrtrIfNetEgrFwdOutProfOcts,
       "aluVrtrIfNetEgrDroInProfPkts": aluVrtrIfNetEgrDroInProfPkts,
       "aluVrtrIfNetEgrDroOutProfPkts": aluVrtrIfNetEgrDroOutProfPkts,
       "aluVrtrIfNetEgrDroInProfOcts": aluVrtrIfNetEgrDroInProfOcts,
       "aluVrtrIfNetEgrDroOutProfOcts": aluVrtrIfNetEgrDroOutProfOcts,
       "aluVrtrIpAddrObjs": aluVrtrIpAddrObjs,
       "aluVrtrIpAddrTable": aluVrtrIpAddrTable,
       "aluVrtrIpAddrEntry": aluVrtrIpAddrEntry,
       "aluVrtrIpAddrDhcpClient": aluVrtrIpAddrDhcpClient,
       "aluVrtrIpAddrClientId": aluVrtrIpAddrClientId,
       "aluVrtrIpAddrClassId": aluVrtrIpAddrClassId,
       "aluTwampObjs": aluTwampObjs,
       "aluTwampConfigObjs": aluTwampConfigObjs,
       "aluTwampRefInactTimeout": aluTwampRefInactTimeout,
       "aluTwampNotificationObjs": aluTwampNotificationObjs,
       "aluTwampRefNotifLocalAddrType": aluTwampRefNotifLocalAddrType,
       "aluTwampRefNotifLocalAddr": aluTwampRefNotifLocalAddr,
       "aluTwampRefNotifLocalPort": aluTwampRefNotifLocalPort,
       "aluTwampRefNotifRemoteAddrType": aluTwampRefNotifRemoteAddrType,
       "aluTwampRefNotifRemoteAddr": aluTwampRefNotifRemoteAddr,
       "aluTwampRefNotifRemotePort": aluTwampRefNotifRemotePort,
       "aluVrtrConfObjs": aluVrtrConfObjs,
       "aluVrtrConfExtTable": aluVrtrConfExtTable,
       "aluVrtrConfExtEntry": aluVrtrConfExtEntry,
       "aluVrtr7705GrtState": aluVrtr7705GrtState,
       "aluVRtrNotifyPrefix": aluVRtrNotifyPrefix,
       "aluVRtrNotifications": aluVRtrNotifications,
       "aluVRtrFibV6UnsupportedRoute": aluVRtrFibV6UnsupportedRoute,
       "aluVRtrFibV6TableThresholdExceed": aluVRtrFibV6TableThresholdExceed,
       "aluVRtrPimNgUnsupportedStarG": aluVRtrPimNgUnsupportedStarG,
       "aluVRtrPimNgSGLimitExceeded": aluVRtrPimNgSGLimitExceeded,
       "aluTwampNotifyPrefix": aluTwampNotifyPrefix,
       "aluTwampNotifications": aluTwampNotifications,
       "aluTwampRefInactivityTimeout": aluTwampRefInactivityTimeout}
)
