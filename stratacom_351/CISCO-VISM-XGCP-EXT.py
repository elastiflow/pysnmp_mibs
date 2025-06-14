# SNMP MIB module (CISCO-VISM-XGCP-EXT) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/stratacom_351/CISCO-VISM-XGCP-EXT.mib
# Produced by pysmi-1.5.11 at Sat May 24 00:08:16 2025
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

(voice,) = mibBuilder.importSymbols(
    "BASIS-MIB",
    "voice")

(ciscoWan,) = mibBuilder.importSymbols(
    "CISCOWAN-SMI",
    "ciscoWan")

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

ciscoVismXgcpExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 94)
)
if mibBuilder.loadTexts:
    ciscoVismXgcpExtMIB.setRevisions(
        ("2003-07-11 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VismXgcpExtensionGrp_ObjectIdentity = ObjectIdentity
vismXgcpExtensionGrp = _VismXgcpExtensionGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5)
)
_VismXgcpCoreObjects_ObjectIdentity = ObjectIdentity
vismXgcpCoreObjects = _VismXgcpCoreObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1)
)


class _VismXgcpRequestMaxTimeout_Type(Integer32):
    """Custom type vismXgcpRequestMaxTimeout based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100000),
    )


_VismXgcpRequestMaxTimeout_Type.__name__ = "Integer32"
_VismXgcpRequestMaxTimeout_Object = MibScalar
vismXgcpRequestMaxTimeout = _VismXgcpRequestMaxTimeout_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 1),
    _VismXgcpRequestMaxTimeout_Type()
)
vismXgcpRequestMaxTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismXgcpRequestMaxTimeout.setStatus("current")


class _VismXgcpPort_Type(Integer32):
    """Custom type vismXgcpPort based on Integer32"""
    defaultValue = 2427

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1025, 65535),
    )


_VismXgcpPort_Type.__name__ = "Integer32"
_VismXgcpPort_Object = MibScalar
vismXgcpPort = _VismXgcpPort_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 2),
    _VismXgcpPort_Type()
)
vismXgcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismXgcpPort.setStatus("current")
_VismXgcpPeerTable_Object = MibTable
vismXgcpPeerTable = _VismXgcpPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 3)
)
if mibBuilder.loadTexts:
    vismXgcpPeerTable.setStatus("current")
_VismXgcpPeerEntry_Object = MibTableRow
vismXgcpPeerEntry = _VismXgcpPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 3, 1)
)
vismXgcpPeerEntry.setIndexNames(
    (0, "CISCO-VISM-XGCP-EXT", "vismXgcpPeerNumber"),
    (0, "CISCO-VISM-XGCP-EXT", "vismXgcpPeerProtocolNumber"),
)
if mibBuilder.loadTexts:
    vismXgcpPeerEntry.setStatus("current")


class _VismXgcpPeerNumber_Type(Integer32):
    """Custom type vismXgcpPeerNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_VismXgcpPeerNumber_Type.__name__ = "Integer32"
_VismXgcpPeerNumber_Object = MibTableColumn
vismXgcpPeerNumber = _VismXgcpPeerNumber_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 3, 1, 1),
    _VismXgcpPeerNumber_Type()
)
vismXgcpPeerNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismXgcpPeerNumber.setStatus("current")


class _VismXgcpPeerProtocolNumber_Type(Integer32):
    """Custom type vismXgcpPeerProtocolNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_VismXgcpPeerProtocolNumber_Type.__name__ = "Integer32"
_VismXgcpPeerProtocolNumber_Object = MibTableColumn
vismXgcpPeerProtocolNumber = _VismXgcpPeerProtocolNumber_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 3, 1, 2),
    _VismXgcpPeerProtocolNumber_Type()
)
vismXgcpPeerProtocolNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismXgcpPeerProtocolNumber.setStatus("current")


class _VismXgcpPeerPort_Type(Integer32):
    """Custom type vismXgcpPeerPort based on Integer32"""
    defaultValue = 2427

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1025, 65535),
    )


_VismXgcpPeerPort_Type.__name__ = "Integer32"
_VismXgcpPeerPort_Object = MibTableColumn
vismXgcpPeerPort = _VismXgcpPeerPort_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 3, 1, 3),
    _VismXgcpPeerPort_Type()
)
vismXgcpPeerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismXgcpPeerPort.setStatus("current")
_VismXgcpMsgStatTable_Object = MibTable
vismXgcpMsgStatTable = _VismXgcpMsgStatTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 4)
)
if mibBuilder.loadTexts:
    vismXgcpMsgStatTable.setStatus("current")
_VismXgcpMsgStatEntry_Object = MibTableRow
vismXgcpMsgStatEntry = _VismXgcpMsgStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 4, 1)
)
vismXgcpMsgStatEntry.setIndexNames(
    (0, "CISCO-VISM-XGCP-EXT", "vismXgcpIpAddress"),
)
if mibBuilder.loadTexts:
    vismXgcpMsgStatEntry.setStatus("current")
_VismXgcpIpAddress_Type = IpAddress
_VismXgcpIpAddress_Object = MibTableColumn
vismXgcpIpAddress = _VismXgcpIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 4, 1, 1),
    _VismXgcpIpAddress_Type()
)
vismXgcpIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismXgcpIpAddress.setStatus("current")
_VismXgcpCrcxCnts_Type = Counter32
_VismXgcpCrcxCnts_Object = MibTableColumn
vismXgcpCrcxCnts = _VismXgcpCrcxCnts_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 4, 1, 2),
    _VismXgcpCrcxCnts_Type()
)
vismXgcpCrcxCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismXgcpCrcxCnts.setStatus("current")
_VismXgcpCrcxFailCnts_Type = Counter32
_VismXgcpCrcxFailCnts_Object = MibTableColumn
vismXgcpCrcxFailCnts = _VismXgcpCrcxFailCnts_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 4, 1, 3),
    _VismXgcpCrcxFailCnts_Type()
)
vismXgcpCrcxFailCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismXgcpCrcxFailCnts.setStatus("current")
_VismXgcpMdcxCnts_Type = Counter32
_VismXgcpMdcxCnts_Object = MibTableColumn
vismXgcpMdcxCnts = _VismXgcpMdcxCnts_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 4, 1, 4),
    _VismXgcpMdcxCnts_Type()
)
vismXgcpMdcxCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismXgcpMdcxCnts.setStatus("current")
_VismXgcpMdcxFailCnts_Type = Counter32
_VismXgcpMdcxFailCnts_Object = MibTableColumn
vismXgcpMdcxFailCnts = _VismXgcpMdcxFailCnts_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 4, 1, 5),
    _VismXgcpMdcxFailCnts_Type()
)
vismXgcpMdcxFailCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismXgcpMdcxFailCnts.setStatus("current")
_VismXgcpDlcxRcvCnts_Type = Counter32
_VismXgcpDlcxRcvCnts_Object = MibTableColumn
vismXgcpDlcxRcvCnts = _VismXgcpDlcxRcvCnts_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 4, 1, 6),
    _VismXgcpDlcxRcvCnts_Type()
)
vismXgcpDlcxRcvCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismXgcpDlcxRcvCnts.setStatus("current")
_VismXgcpDlcxRcvFailCnts_Type = Counter32
_VismXgcpDlcxRcvFailCnts_Object = MibTableColumn
vismXgcpDlcxRcvFailCnts = _VismXgcpDlcxRcvFailCnts_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 4, 1, 7),
    _VismXgcpDlcxRcvFailCnts_Type()
)
vismXgcpDlcxRcvFailCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismXgcpDlcxRcvFailCnts.setStatus("current")
_VismXgcpDlcxSentCnts_Type = Counter32
_VismXgcpDlcxSentCnts_Object = MibTableColumn
vismXgcpDlcxSentCnts = _VismXgcpDlcxSentCnts_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 4, 1, 8),
    _VismXgcpDlcxSentCnts_Type()
)
vismXgcpDlcxSentCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismXgcpDlcxSentCnts.setStatus("current")
_VismXgcpDlcxSentFailCnts_Type = Counter32
_VismXgcpDlcxSentFailCnts_Object = MibTableColumn
vismXgcpDlcxSentFailCnts = _VismXgcpDlcxSentFailCnts_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 4, 1, 9),
    _VismXgcpDlcxSentFailCnts_Type()
)
vismXgcpDlcxSentFailCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismXgcpDlcxSentFailCnts.setStatus("current")
_VismXgcpRqntCnts_Type = Counter32
_VismXgcpRqntCnts_Object = MibTableColumn
vismXgcpRqntCnts = _VismXgcpRqntCnts_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 4, 1, 10),
    _VismXgcpRqntCnts_Type()
)
vismXgcpRqntCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismXgcpRqntCnts.setStatus("current")
_VismXgcpRqntFailCnts_Type = Counter32
_VismXgcpRqntFailCnts_Object = MibTableColumn
vismXgcpRqntFailCnts = _VismXgcpRqntFailCnts_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 4, 1, 11),
    _VismXgcpRqntFailCnts_Type()
)
vismXgcpRqntFailCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismXgcpRqntFailCnts.setStatus("current")
_VismXgcpNtfyCnts_Type = Counter32
_VismXgcpNtfyCnts_Object = MibTableColumn
vismXgcpNtfyCnts = _VismXgcpNtfyCnts_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 4, 1, 12),
    _VismXgcpNtfyCnts_Type()
)
vismXgcpNtfyCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismXgcpNtfyCnts.setStatus("current")
_VismXgcpNtfyFailCnts_Type = Counter32
_VismXgcpNtfyFailCnts_Object = MibTableColumn
vismXgcpNtfyFailCnts = _VismXgcpNtfyFailCnts_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 4, 1, 13),
    _VismXgcpNtfyFailCnts_Type()
)
vismXgcpNtfyFailCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismXgcpNtfyFailCnts.setStatus("current")
_VismXgcpAuepCnts_Type = Counter32
_VismXgcpAuepCnts_Object = MibTableColumn
vismXgcpAuepCnts = _VismXgcpAuepCnts_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 4, 1, 14),
    _VismXgcpAuepCnts_Type()
)
vismXgcpAuepCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismXgcpAuepCnts.setStatus("current")
_VismXgcpAuepFailCnts_Type = Counter32
_VismXgcpAuepFailCnts_Object = MibTableColumn
vismXgcpAuepFailCnts = _VismXgcpAuepFailCnts_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 4, 1, 15),
    _VismXgcpAuepFailCnts_Type()
)
vismXgcpAuepFailCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismXgcpAuepFailCnts.setStatus("current")
_VismXgcpAucxCnts_Type = Counter32
_VismXgcpAucxCnts_Object = MibTableColumn
vismXgcpAucxCnts = _VismXgcpAucxCnts_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 4, 1, 16),
    _VismXgcpAucxCnts_Type()
)
vismXgcpAucxCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismXgcpAucxCnts.setStatus("current")
_VismXgcpAucxFailCnts_Type = Counter32
_VismXgcpAucxFailCnts_Object = MibTableColumn
vismXgcpAucxFailCnts = _VismXgcpAucxFailCnts_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 4, 1, 17),
    _VismXgcpAucxFailCnts_Type()
)
vismXgcpAucxFailCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismXgcpAucxFailCnts.setStatus("current")
_VismXgcpRsipCnts_Type = Counter32
_VismXgcpRsipCnts_Object = MibTableColumn
vismXgcpRsipCnts = _VismXgcpRsipCnts_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 4, 1, 18),
    _VismXgcpRsipCnts_Type()
)
vismXgcpRsipCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismXgcpRsipCnts.setStatus("current")
_VismXgcpRsipFailCnts_Type = Counter32
_VismXgcpRsipFailCnts_Object = MibTableColumn
vismXgcpRsipFailCnts = _VismXgcpRsipFailCnts_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 4, 1, 19),
    _VismXgcpRsipFailCnts_Type()
)
vismXgcpRsipFailCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismXgcpRsipFailCnts.setStatus("current")
_VismXgcpEnhancementsObjects_ObjectIdentity = ObjectIdentity
vismXgcpEnhancementsObjects = _VismXgcpEnhancementsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 2)
)


class _VismXgcpRestartInProgressTdinit_Type(Integer32):
    """Custom type vismXgcpRestartInProgressTdinit based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_VismXgcpRestartInProgressTdinit_Type.__name__ = "Integer32"
_VismXgcpRestartInProgressTdinit_Object = MibScalar
vismXgcpRestartInProgressTdinit = _VismXgcpRestartInProgressTdinit_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 2, 1),
    _VismXgcpRestartInProgressTdinit_Type()
)
vismXgcpRestartInProgressTdinit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismXgcpRestartInProgressTdinit.setStatus("current")


class _VismXgcpRestartInProgressTdmin_Type(Integer32):
    """Custom type vismXgcpRestartInProgressTdmin based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VismXgcpRestartInProgressTdmin_Type.__name__ = "Integer32"
_VismXgcpRestartInProgressTdmin_Object = MibScalar
vismXgcpRestartInProgressTdmin = _VismXgcpRestartInProgressTdmin_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 2, 2),
    _VismXgcpRestartInProgressTdmin_Type()
)
vismXgcpRestartInProgressTdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismXgcpRestartInProgressTdmin.setStatus("current")


class _VismXgcpRestartInProgressTdmax_Type(Integer32):
    """Custom type vismXgcpRestartInProgressTdmax based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5000),
    )


_VismXgcpRestartInProgressTdmax_Type.__name__ = "Integer32"
_VismXgcpRestartInProgressTdmax_Object = MibScalar
vismXgcpRestartInProgressTdmax = _VismXgcpRestartInProgressTdmax_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 2, 3),
    _VismXgcpRestartInProgressTdmax_Type()
)
vismXgcpRestartInProgressTdmax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismXgcpRestartInProgressTdmax.setStatus("current")
_CiscoVismXgcpExtMIBConformance_ObjectIdentity = ObjectIdentity
ciscoVismXgcpExtMIBConformance = _CiscoVismXgcpExtMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 94, 2)
)
_CiscoVismXgcpExtMIBGroups_ObjectIdentity = ObjectIdentity
ciscoVismXgcpExtMIBGroups = _CiscoVismXgcpExtMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 94, 2, 1)
)
_CiscoVismXgcpExtMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoVismXgcpExtMIBCompliances = _CiscoVismXgcpExtMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 94, 2, 2)
)

# Managed Objects groups

ciscoVismXgcpExtensionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 94, 2, 1, 1)
)
ciscoVismXgcpExtensionGroup.setObjects(
      *(("CISCO-VISM-XGCP-EXT", "vismXgcpRequestMaxTimeout"),
        ("CISCO-VISM-XGCP-EXT", "vismXgcpPort"))
)
if mibBuilder.loadTexts:
    ciscoVismXgcpExtensionGroup.setStatus("current")

ciscoVismXgcpCoreGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 94, 2, 1, 2)
)
ciscoVismXgcpCoreGroup.setObjects(
      *(("CISCO-VISM-XGCP-EXT", "vismXgcpPeerNumber"),
        ("CISCO-VISM-XGCP-EXT", "vismXgcpPeerProtocolNumber"),
        ("CISCO-VISM-XGCP-EXT", "vismXgcpPeerPort"))
)
if mibBuilder.loadTexts:
    ciscoVismXgcpCoreGroup.setStatus("current")

ciscoVismXgcpStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 94, 2, 1, 3)
)
ciscoVismXgcpStatsGroup.setObjects(
      *(("CISCO-VISM-XGCP-EXT", "vismXgcpIpAddress"),
        ("CISCO-VISM-XGCP-EXT", "vismXgcpCrcxCnts"),
        ("CISCO-VISM-XGCP-EXT", "vismXgcpCrcxFailCnts"),
        ("CISCO-VISM-XGCP-EXT", "vismXgcpMdcxCnts"),
        ("CISCO-VISM-XGCP-EXT", "vismXgcpMdcxFailCnts"),
        ("CISCO-VISM-XGCP-EXT", "vismXgcpDlcxRcvCnts"),
        ("CISCO-VISM-XGCP-EXT", "vismXgcpDlcxRcvFailCnts"),
        ("CISCO-VISM-XGCP-EXT", "vismXgcpDlcxSentCnts"),
        ("CISCO-VISM-XGCP-EXT", "vismXgcpDlcxSentFailCnts"),
        ("CISCO-VISM-XGCP-EXT", "vismXgcpRqntCnts"),
        ("CISCO-VISM-XGCP-EXT", "vismXgcpRqntFailCnts"),
        ("CISCO-VISM-XGCP-EXT", "vismXgcpNtfyCnts"),
        ("CISCO-VISM-XGCP-EXT", "vismXgcpNtfyFailCnts"),
        ("CISCO-VISM-XGCP-EXT", "vismXgcpAuepCnts"),
        ("CISCO-VISM-XGCP-EXT", "vismXgcpAuepFailCnts"),
        ("CISCO-VISM-XGCP-EXT", "vismXgcpAucxCnts"),
        ("CISCO-VISM-XGCP-EXT", "vismXgcpAucxFailCnts"),
        ("CISCO-VISM-XGCP-EXT", "vismXgcpRsipCnts"),
        ("CISCO-VISM-XGCP-EXT", "vismXgcpRsipFailCnts"))
)
if mibBuilder.loadTexts:
    ciscoVismXgcpStatsGroup.setStatus("current")

ciscoVismXgcpEnhancementGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 94, 2, 1, 4)
)
ciscoVismXgcpEnhancementGroup.setObjects(
      *(("CISCO-VISM-XGCP-EXT", "vismXgcpRestartInProgressTdinit"),
        ("CISCO-VISM-XGCP-EXT", "vismXgcpRestartInProgressTdmin"),
        ("CISCO-VISM-XGCP-EXT", "vismXgcpRestartInProgressTdmax"))
)
if mibBuilder.loadTexts:
    ciscoVismXgcpEnhancementGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoVismXgcpExtCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 94, 2, 2, 1)
)
ciscoVismXgcpExtCompliance.setObjects(
      *(("CISCO-VISM-XGCP-EXT", "ciscoVismXgcpExtensionGroup"),
        ("CISCO-VISM-XGCP-EXT", "ciscoVismXgcpCoreGroup"),
        ("CISCO-VISM-XGCP-EXT", "ciscoVismXgcpStatsGroup"),
        ("CISCO-VISM-XGCP-EXT", "ciscoVismXgcpEnhancementGroup"))
)
if mibBuilder.loadTexts:
    ciscoVismXgcpExtCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-VISM-XGCP-EXT",
    **{"vismXgcpExtensionGrp": vismXgcpExtensionGrp,
       "vismXgcpCoreObjects": vismXgcpCoreObjects,
       "vismXgcpRequestMaxTimeout": vismXgcpRequestMaxTimeout,
       "vismXgcpPort": vismXgcpPort,
       "vismXgcpPeerTable": vismXgcpPeerTable,
       "vismXgcpPeerEntry": vismXgcpPeerEntry,
       "vismXgcpPeerNumber": vismXgcpPeerNumber,
       "vismXgcpPeerProtocolNumber": vismXgcpPeerProtocolNumber,
       "vismXgcpPeerPort": vismXgcpPeerPort,
       "vismXgcpMsgStatTable": vismXgcpMsgStatTable,
       "vismXgcpMsgStatEntry": vismXgcpMsgStatEntry,
       "vismXgcpIpAddress": vismXgcpIpAddress,
       "vismXgcpCrcxCnts": vismXgcpCrcxCnts,
       "vismXgcpCrcxFailCnts": vismXgcpCrcxFailCnts,
       "vismXgcpMdcxCnts": vismXgcpMdcxCnts,
       "vismXgcpMdcxFailCnts": vismXgcpMdcxFailCnts,
       "vismXgcpDlcxRcvCnts": vismXgcpDlcxRcvCnts,
       "vismXgcpDlcxRcvFailCnts": vismXgcpDlcxRcvFailCnts,
       "vismXgcpDlcxSentCnts": vismXgcpDlcxSentCnts,
       "vismXgcpDlcxSentFailCnts": vismXgcpDlcxSentFailCnts,
       "vismXgcpRqntCnts": vismXgcpRqntCnts,
       "vismXgcpRqntFailCnts": vismXgcpRqntFailCnts,
       "vismXgcpNtfyCnts": vismXgcpNtfyCnts,
       "vismXgcpNtfyFailCnts": vismXgcpNtfyFailCnts,
       "vismXgcpAuepCnts": vismXgcpAuepCnts,
       "vismXgcpAuepFailCnts": vismXgcpAuepFailCnts,
       "vismXgcpAucxCnts": vismXgcpAucxCnts,
       "vismXgcpAucxFailCnts": vismXgcpAucxFailCnts,
       "vismXgcpRsipCnts": vismXgcpRsipCnts,
       "vismXgcpRsipFailCnts": vismXgcpRsipFailCnts,
       "vismXgcpEnhancementsObjects": vismXgcpEnhancementsObjects,
       "vismXgcpRestartInProgressTdinit": vismXgcpRestartInProgressTdinit,
       "vismXgcpRestartInProgressTdmin": vismXgcpRestartInProgressTdmin,
       "vismXgcpRestartInProgressTdmax": vismXgcpRestartInProgressTdmax,
       "ciscoVismXgcpExtMIB": ciscoVismXgcpExtMIB,
       "ciscoVismXgcpExtMIBConformance": ciscoVismXgcpExtMIBConformance,
       "ciscoVismXgcpExtMIBGroups": ciscoVismXgcpExtMIBGroups,
       "ciscoVismXgcpExtensionGroup": ciscoVismXgcpExtensionGroup,
       "ciscoVismXgcpCoreGroup": ciscoVismXgcpCoreGroup,
       "ciscoVismXgcpStatsGroup": ciscoVismXgcpStatsGroup,
       "ciscoVismXgcpEnhancementGroup": ciscoVismXgcpEnhancementGroup,
       "ciscoVismXgcpExtMIBCompliances": ciscoVismXgcpExtMIBCompliances,
       "ciscoVismXgcpExtCompliance": ciscoVismXgcpExtCompliance}
)
