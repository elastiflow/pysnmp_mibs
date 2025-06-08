# SNMP MIB module (CIE1000-DHCP-SNOOPING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CIE1000-DHCP-SNOOPING-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 20:26:41 2025
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

(CIE1000InterfaceIndex,) = mibBuilder.importSymbols(
    "CIE1000-TC",
    "CIE1000InterfaceIndex")

(cie1000SwitchMgmt,) = mibBuilder.importSymbols(
    "CISCO-IE1000-MIB",
    "cie1000SwitchMgmt")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

cie1000DhcpSnoopingMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 56)
)
if mibBuilder.loadTexts:
    cie1000DhcpSnoopingMib.setRevisions(
        ("2014-10-10 00:00",
         "2014-07-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Cie1000DhcpSnoopingMibObjects_ObjectIdentity = ObjectIdentity
cie1000DhcpSnoopingMibObjects = _Cie1000DhcpSnoopingMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 56, 1)
)
_Cie1000DhcpSnoopingConfig_ObjectIdentity = ObjectIdentity
cie1000DhcpSnoopingConfig = _Cie1000DhcpSnoopingConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 56, 1, 2)
)
_Cie1000DhcpSnoopingConfigGlobals_ObjectIdentity = ObjectIdentity
cie1000DhcpSnoopingConfigGlobals = _Cie1000DhcpSnoopingConfigGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 56, 1, 2, 1)
)
_Cie1000DhcpSnoopingConfigGlobalsMode_Type = TruthValue
_Cie1000DhcpSnoopingConfigGlobalsMode_Object = MibScalar
cie1000DhcpSnoopingConfigGlobalsMode = _Cie1000DhcpSnoopingConfigGlobalsMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 56, 1, 2, 1, 1),
    _Cie1000DhcpSnoopingConfigGlobalsMode_Type()
)
cie1000DhcpSnoopingConfigGlobalsMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpSnoopingConfigGlobalsMode.setStatus("current")
_Cie1000DhcpSnoopingConfigInterfaceTable_Object = MibTable
cie1000DhcpSnoopingConfigInterfaceTable = _Cie1000DhcpSnoopingConfigInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 56, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cie1000DhcpSnoopingConfigInterfaceTable.setStatus("current")
_Cie1000DhcpSnoopingConfigInterfaceEntry_Object = MibTableRow
cie1000DhcpSnoopingConfigInterfaceEntry = _Cie1000DhcpSnoopingConfigInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 56, 1, 2, 2, 1)
)
cie1000DhcpSnoopingConfigInterfaceEntry.setIndexNames(
    (0, "CIE1000-DHCP-SNOOPING-MIB", "cie1000DhcpSnoopingConfigInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    cie1000DhcpSnoopingConfigInterfaceEntry.setStatus("current")
_Cie1000DhcpSnoopingConfigInterfaceIfIndex_Type = CIE1000InterfaceIndex
_Cie1000DhcpSnoopingConfigInterfaceIfIndex_Object = MibTableColumn
cie1000DhcpSnoopingConfigInterfaceIfIndex = _Cie1000DhcpSnoopingConfigInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 56, 1, 2, 2, 1, 1),
    _Cie1000DhcpSnoopingConfigInterfaceIfIndex_Type()
)
cie1000DhcpSnoopingConfigInterfaceIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000DhcpSnoopingConfigInterfaceIfIndex.setStatus("current")
_Cie1000DhcpSnoopingConfigInterfaceTrustMode_Type = TruthValue
_Cie1000DhcpSnoopingConfigInterfaceTrustMode_Object = MibTableColumn
cie1000DhcpSnoopingConfigInterfaceTrustMode = _Cie1000DhcpSnoopingConfigInterfaceTrustMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 56, 1, 2, 2, 1, 2),
    _Cie1000DhcpSnoopingConfigInterfaceTrustMode_Type()
)
cie1000DhcpSnoopingConfigInterfaceTrustMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpSnoopingConfigInterfaceTrustMode.setStatus("current")
_Cie1000DhcpSnoopingStatus_ObjectIdentity = ObjectIdentity
cie1000DhcpSnoopingStatus = _Cie1000DhcpSnoopingStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 56, 1, 3)
)
_Cie1000DhcpSnoopingStatusAssignedIpTable_Object = MibTable
cie1000DhcpSnoopingStatusAssignedIpTable = _Cie1000DhcpSnoopingStatusAssignedIpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 56, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cie1000DhcpSnoopingStatusAssignedIpTable.setStatus("current")
_Cie1000DhcpSnoopingStatusAssignedIpEntry_Object = MibTableRow
cie1000DhcpSnoopingStatusAssignedIpEntry = _Cie1000DhcpSnoopingStatusAssignedIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 56, 1, 3, 1, 1)
)
cie1000DhcpSnoopingStatusAssignedIpEntry.setIndexNames(
    (0, "CIE1000-DHCP-SNOOPING-MIB", "cie1000DhcpSnoopingStatusAssignedIpMacAddress"),
    (0, "CIE1000-DHCP-SNOOPING-MIB", "cie1000DhcpSnoopingStatusAssignedIpVlanId"),
)
if mibBuilder.loadTexts:
    cie1000DhcpSnoopingStatusAssignedIpEntry.setStatus("current")
_Cie1000DhcpSnoopingStatusAssignedIpMacAddress_Type = MacAddress
_Cie1000DhcpSnoopingStatusAssignedIpMacAddress_Object = MibTableColumn
cie1000DhcpSnoopingStatusAssignedIpMacAddress = _Cie1000DhcpSnoopingStatusAssignedIpMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 56, 1, 3, 1, 1, 1),
    _Cie1000DhcpSnoopingStatusAssignedIpMacAddress_Type()
)
cie1000DhcpSnoopingStatusAssignedIpMacAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000DhcpSnoopingStatusAssignedIpMacAddress.setStatus("current")


class _Cie1000DhcpSnoopingStatusAssignedIpVlanId_Type(Integer32):
    """Custom type cie1000DhcpSnoopingStatusAssignedIpVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Cie1000DhcpSnoopingStatusAssignedIpVlanId_Type.__name__ = "Integer32"
_Cie1000DhcpSnoopingStatusAssignedIpVlanId_Object = MibTableColumn
cie1000DhcpSnoopingStatusAssignedIpVlanId = _Cie1000DhcpSnoopingStatusAssignedIpVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 56, 1, 3, 1, 1, 2),
    _Cie1000DhcpSnoopingStatusAssignedIpVlanId_Type()
)
cie1000DhcpSnoopingStatusAssignedIpVlanId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000DhcpSnoopingStatusAssignedIpVlanId.setStatus("current")
_Cie1000DhcpSnoopingStatusAssignedIpIfIndex_Type = CIE1000InterfaceIndex
_Cie1000DhcpSnoopingStatusAssignedIpIfIndex_Object = MibTableColumn
cie1000DhcpSnoopingStatusAssignedIpIfIndex = _Cie1000DhcpSnoopingStatusAssignedIpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 56, 1, 3, 1, 1, 3),
    _Cie1000DhcpSnoopingStatusAssignedIpIfIndex_Type()
)
cie1000DhcpSnoopingStatusAssignedIpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000DhcpSnoopingStatusAssignedIpIfIndex.setStatus("current")
_Cie1000DhcpSnoopingStatusAssignedIpIpAddress_Type = IpAddress
_Cie1000DhcpSnoopingStatusAssignedIpIpAddress_Object = MibTableColumn
cie1000DhcpSnoopingStatusAssignedIpIpAddress = _Cie1000DhcpSnoopingStatusAssignedIpIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 56, 1, 3, 1, 1, 4),
    _Cie1000DhcpSnoopingStatusAssignedIpIpAddress_Type()
)
cie1000DhcpSnoopingStatusAssignedIpIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000DhcpSnoopingStatusAssignedIpIpAddress.setStatus("current")
_Cie1000DhcpSnoopingStatusAssignedIpNetmask_Type = IpAddress
_Cie1000DhcpSnoopingStatusAssignedIpNetmask_Object = MibTableColumn
cie1000DhcpSnoopingStatusAssignedIpNetmask = _Cie1000DhcpSnoopingStatusAssignedIpNetmask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 56, 1, 3, 1, 1, 5),
    _Cie1000DhcpSnoopingStatusAssignedIpNetmask_Type()
)
cie1000DhcpSnoopingStatusAssignedIpNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000DhcpSnoopingStatusAssignedIpNetmask.setStatus("current")
_Cie1000DhcpSnoopingStatusAssignedIpDhcpServerIp_Type = IpAddress
_Cie1000DhcpSnoopingStatusAssignedIpDhcpServerIp_Object = MibTableColumn
cie1000DhcpSnoopingStatusAssignedIpDhcpServerIp = _Cie1000DhcpSnoopingStatusAssignedIpDhcpServerIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 56, 1, 3, 1, 1, 6),
    _Cie1000DhcpSnoopingStatusAssignedIpDhcpServerIp_Type()
)
cie1000DhcpSnoopingStatusAssignedIpDhcpServerIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000DhcpSnoopingStatusAssignedIpDhcpServerIp.setStatus("current")
_Cie1000DhcpSnoopingControl_ObjectIdentity = ObjectIdentity
cie1000DhcpSnoopingControl = _Cie1000DhcpSnoopingControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 56, 1, 4)
)
_Cie1000DhcpSnoopingControlInterfaceClearStatisticsTable_Object = MibTable
cie1000DhcpSnoopingControlInterfaceClearStatisticsTable = _Cie1000DhcpSnoopingControlInterfaceClearStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 56, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cie1000DhcpSnoopingControlInterfaceClearStatisticsTable.setStatus("current")
_Cie1000DhcpSnoopingControlInterfaceClearStatisticsEntry_Object = MibTableRow
cie1000DhcpSnoopingControlInterfaceClearStatisticsEntry = _Cie1000DhcpSnoopingControlInterfaceClearStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 56, 1, 4, 1, 1)
)
cie1000DhcpSnoopingControlInterfaceClearStatisticsEntry.setIndexNames(
    (0, "CIE1000-DHCP-SNOOPING-MIB", "cie1000DhcpSnoopingControlInterfaceClearStatisticsIfIndex"),
)
if mibBuilder.loadTexts:
    cie1000DhcpSnoopingControlInterfaceClearStatisticsEntry.setStatus("current")
_Cie1000DhcpSnoopingControlInterfaceClearStatisticsIfIndex_Type = CIE1000InterfaceIndex
_Cie1000DhcpSnoopingControlInterfaceClearStatisticsIfIndex_Object = MibTableColumn
cie1000DhcpSnoopingControlInterfaceClearStatisticsIfIndex = _Cie1000DhcpSnoopingControlInterfaceClearStatisticsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 56, 1, 4, 1, 1, 1),
    _Cie1000DhcpSnoopingControlInterfaceClearStatisticsIfIndex_Type()
)
cie1000DhcpSnoopingControlInterfaceClearStatisticsIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000DhcpSnoopingControlInterfaceClearStatisticsIfIndex.setStatus("current")
_Cie1000DhcpSnoopingControlInterfaceClearStatisticsClear_Type = TruthValue
_Cie1000DhcpSnoopingControlInterfaceClearStatisticsClear_Object = MibTableColumn
cie1000DhcpSnoopingControlInterfaceClearStatisticsClear = _Cie1000DhcpSnoopingControlInterfaceClearStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 56, 1, 4, 1, 1, 2),
    _Cie1000DhcpSnoopingControlInterfaceClearStatisticsClear_Type()
)
cie1000DhcpSnoopingControlInterfaceClearStatisticsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpSnoopingControlInterfaceClearStatisticsClear.setStatus("current")
_Cie1000DhcpSnoopingStatistics_ObjectIdentity = ObjectIdentity
cie1000DhcpSnoopingStatistics = _Cie1000DhcpSnoopingStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 56, 1, 5)
)
_Cie1000DhcpSnoopingStatisticsInterfaceTable_Object = MibTable
cie1000DhcpSnoopingStatisticsInterfaceTable = _Cie1000DhcpSnoopingStatisticsInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 56, 1, 5, 2)
)
if mibBuilder.loadTexts:
    cie1000DhcpSnoopingStatisticsInterfaceTable.setStatus("current")
_Cie1000DhcpSnoopingStatisticsInterfaceEntry_Object = MibTableRow
cie1000DhcpSnoopingStatisticsInterfaceEntry = _Cie1000DhcpSnoopingStatisticsInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 56, 1, 5, 2, 1)
)
cie1000DhcpSnoopingStatisticsInterfaceEntry.setIndexNames(
    (0, "CIE1000-DHCP-SNOOPING-MIB", "cie1000DhcpSnoopingStatisticsInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    cie1000DhcpSnoopingStatisticsInterfaceEntry.setStatus("current")
_Cie1000DhcpSnoopingStatisticsInterfaceIfIndex_Type = CIE1000InterfaceIndex
_Cie1000DhcpSnoopingStatisticsInterfaceIfIndex_Object = MibTableColumn
cie1000DhcpSnoopingStatisticsInterfaceIfIndex = _Cie1000DhcpSnoopingStatisticsInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 56, 1, 5, 2, 1, 1),
    _Cie1000DhcpSnoopingStatisticsInterfaceIfIndex_Type()
)
cie1000DhcpSnoopingStatisticsInterfaceIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000DhcpSnoopingStatisticsInterfaceIfIndex.setStatus("current")
_Cie1000DhcpSnoopingStatisticsInterfaceRxDiscover_Type = Unsigned32
_Cie1000DhcpSnoopingStatisticsInterfaceRxDiscover_Object = MibTableColumn
cie1000DhcpSnoopingStatisticsInterfaceRxDiscover = _Cie1000DhcpSnoopingStatisticsInterfaceRxDiscover_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 56, 1, 5, 2, 1, 2),
    _Cie1000DhcpSnoopingStatisticsInterfaceRxDiscover_Type()
)
cie1000DhcpSnoopingStatisticsInterfaceRxDiscover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000DhcpSnoopingStatisticsInterfaceRxDiscover.setStatus("current")
_Cie1000DhcpSnoopingStatisticsInterfaceRxOffer_Type = Unsigned32
_Cie1000DhcpSnoopingStatisticsInterfaceRxOffer_Object = MibTableColumn
cie1000DhcpSnoopingStatisticsInterfaceRxOffer = _Cie1000DhcpSnoopingStatisticsInterfaceRxOffer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 56, 1, 5, 2, 1, 3),
    _Cie1000DhcpSnoopingStatisticsInterfaceRxOffer_Type()
)
cie1000DhcpSnoopingStatisticsInterfaceRxOffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000DhcpSnoopingStatisticsInterfaceRxOffer.setStatus("current")
_Cie1000DhcpSnoopingStatisticsInterfaceRxRequest_Type = Unsigned32
_Cie1000DhcpSnoopingStatisticsInterfaceRxRequest_Object = MibTableColumn
cie1000DhcpSnoopingStatisticsInterfaceRxRequest = _Cie1000DhcpSnoopingStatisticsInterfaceRxRequest_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 56, 1, 5, 2, 1, 4),
    _Cie1000DhcpSnoopingStatisticsInterfaceRxRequest_Type()
)
cie1000DhcpSnoopingStatisticsInterfaceRxRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000DhcpSnoopingStatisticsInterfaceRxRequest.setStatus("current")
_Cie1000DhcpSnoopingStatisticsInterfaceRxDecline_Type = Unsigned32
_Cie1000DhcpSnoopingStatisticsInterfaceRxDecline_Object = MibTableColumn
cie1000DhcpSnoopingStatisticsInterfaceRxDecline = _Cie1000DhcpSnoopingStatisticsInterfaceRxDecline_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 56, 1, 5, 2, 1, 5),
    _Cie1000DhcpSnoopingStatisticsInterfaceRxDecline_Type()
)
cie1000DhcpSnoopingStatisticsInterfaceRxDecline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000DhcpSnoopingStatisticsInterfaceRxDecline.setStatus("current")
_Cie1000DhcpSnoopingStatisticsInterfaceRxAck_Type = Unsigned32
_Cie1000DhcpSnoopingStatisticsInterfaceRxAck_Object = MibTableColumn
cie1000DhcpSnoopingStatisticsInterfaceRxAck = _Cie1000DhcpSnoopingStatisticsInterfaceRxAck_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 56, 1, 5, 2, 1, 6),
    _Cie1000DhcpSnoopingStatisticsInterfaceRxAck_Type()
)
cie1000DhcpSnoopingStatisticsInterfaceRxAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000DhcpSnoopingStatisticsInterfaceRxAck.setStatus("current")
_Cie1000DhcpSnoopingStatisticsInterfaceRxNak_Type = Unsigned32
_Cie1000DhcpSnoopingStatisticsInterfaceRxNak_Object = MibTableColumn
cie1000DhcpSnoopingStatisticsInterfaceRxNak = _Cie1000DhcpSnoopingStatisticsInterfaceRxNak_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 56, 1, 5, 2, 1, 7),
    _Cie1000DhcpSnoopingStatisticsInterfaceRxNak_Type()
)
cie1000DhcpSnoopingStatisticsInterfaceRxNak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000DhcpSnoopingStatisticsInterfaceRxNak.setStatus("current")
_Cie1000DhcpSnoopingStatisticsInterfaceRxRelease_Type = Unsigned32
_Cie1000DhcpSnoopingStatisticsInterfaceRxRelease_Object = MibTableColumn
cie1000DhcpSnoopingStatisticsInterfaceRxRelease = _Cie1000DhcpSnoopingStatisticsInterfaceRxRelease_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 56, 1, 5, 2, 1, 8),
    _Cie1000DhcpSnoopingStatisticsInterfaceRxRelease_Type()
)
cie1000DhcpSnoopingStatisticsInterfaceRxRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000DhcpSnoopingStatisticsInterfaceRxRelease.setStatus("current")
_Cie1000DhcpSnoopingStatisticsInterfaceRxInform_Type = Unsigned32
_Cie1000DhcpSnoopingStatisticsInterfaceRxInform_Object = MibTableColumn
cie1000DhcpSnoopingStatisticsInterfaceRxInform = _Cie1000DhcpSnoopingStatisticsInterfaceRxInform_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 56, 1, 5, 2, 1, 9),
    _Cie1000DhcpSnoopingStatisticsInterfaceRxInform_Type()
)
cie1000DhcpSnoopingStatisticsInterfaceRxInform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000DhcpSnoopingStatisticsInterfaceRxInform.setStatus("current")
_Cie1000DhcpSnoopingStatisticsInterfaceRxLeaseQuery_Type = Unsigned32
_Cie1000DhcpSnoopingStatisticsInterfaceRxLeaseQuery_Object = MibTableColumn
cie1000DhcpSnoopingStatisticsInterfaceRxLeaseQuery = _Cie1000DhcpSnoopingStatisticsInterfaceRxLeaseQuery_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 56, 1, 5, 2, 1, 10),
    _Cie1000DhcpSnoopingStatisticsInterfaceRxLeaseQuery_Type()
)
cie1000DhcpSnoopingStatisticsInterfaceRxLeaseQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000DhcpSnoopingStatisticsInterfaceRxLeaseQuery.setStatus("current")
_Cie1000DhcpSnoopingStatisticsInterfaceRxLeaseUnassigned_Type = Unsigned32
_Cie1000DhcpSnoopingStatisticsInterfaceRxLeaseUnassigned_Object = MibTableColumn
cie1000DhcpSnoopingStatisticsInterfaceRxLeaseUnassigned = _Cie1000DhcpSnoopingStatisticsInterfaceRxLeaseUnassigned_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 56, 1, 5, 2, 1, 11),
    _Cie1000DhcpSnoopingStatisticsInterfaceRxLeaseUnassigned_Type()
)
cie1000DhcpSnoopingStatisticsInterfaceRxLeaseUnassigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000DhcpSnoopingStatisticsInterfaceRxLeaseUnassigned.setStatus("current")
_Cie1000DhcpSnoopingStatisticsInterfaceRxLeaseUnknown_Type = Unsigned32
_Cie1000DhcpSnoopingStatisticsInterfaceRxLeaseUnknown_Object = MibTableColumn
cie1000DhcpSnoopingStatisticsInterfaceRxLeaseUnknown = _Cie1000DhcpSnoopingStatisticsInterfaceRxLeaseUnknown_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 56, 1, 5, 2, 1, 12),
    _Cie1000DhcpSnoopingStatisticsInterfaceRxLeaseUnknown_Type()
)
cie1000DhcpSnoopingStatisticsInterfaceRxLeaseUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000DhcpSnoopingStatisticsInterfaceRxLeaseUnknown.setStatus("current")
_Cie1000DhcpSnoopingStatisticsInterfaceRxLeaseActive_Type = Unsigned32
_Cie1000DhcpSnoopingStatisticsInterfaceRxLeaseActive_Object = MibTableColumn
cie1000DhcpSnoopingStatisticsInterfaceRxLeaseActive = _Cie1000DhcpSnoopingStatisticsInterfaceRxLeaseActive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 56, 1, 5, 2, 1, 13),
    _Cie1000DhcpSnoopingStatisticsInterfaceRxLeaseActive_Type()
)
cie1000DhcpSnoopingStatisticsInterfaceRxLeaseActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000DhcpSnoopingStatisticsInterfaceRxLeaseActive.setStatus("current")
_Cie1000DhcpSnoopingStatisticsInterfaceRxDiscardChksumErr_Type = Unsigned32
_Cie1000DhcpSnoopingStatisticsInterfaceRxDiscardChksumErr_Object = MibTableColumn
cie1000DhcpSnoopingStatisticsInterfaceRxDiscardChksumErr = _Cie1000DhcpSnoopingStatisticsInterfaceRxDiscardChksumErr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 56, 1, 5, 2, 1, 14),
    _Cie1000DhcpSnoopingStatisticsInterfaceRxDiscardChksumErr_Type()
)
cie1000DhcpSnoopingStatisticsInterfaceRxDiscardChksumErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000DhcpSnoopingStatisticsInterfaceRxDiscardChksumErr.setStatus("current")
_Cie1000DhcpSnoopingStatisticsInterfaceRxDiscardUntrust_Type = Unsigned32
_Cie1000DhcpSnoopingStatisticsInterfaceRxDiscardUntrust_Object = MibTableColumn
cie1000DhcpSnoopingStatisticsInterfaceRxDiscardUntrust = _Cie1000DhcpSnoopingStatisticsInterfaceRxDiscardUntrust_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 56, 1, 5, 2, 1, 15),
    _Cie1000DhcpSnoopingStatisticsInterfaceRxDiscardUntrust_Type()
)
cie1000DhcpSnoopingStatisticsInterfaceRxDiscardUntrust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000DhcpSnoopingStatisticsInterfaceRxDiscardUntrust.setStatus("current")
_Cie1000DhcpSnoopingStatisticsInterfaceTxDiscover_Type = Unsigned32
_Cie1000DhcpSnoopingStatisticsInterfaceTxDiscover_Object = MibTableColumn
cie1000DhcpSnoopingStatisticsInterfaceTxDiscover = _Cie1000DhcpSnoopingStatisticsInterfaceTxDiscover_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 56, 1, 5, 2, 1, 16),
    _Cie1000DhcpSnoopingStatisticsInterfaceTxDiscover_Type()
)
cie1000DhcpSnoopingStatisticsInterfaceTxDiscover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000DhcpSnoopingStatisticsInterfaceTxDiscover.setStatus("current")
_Cie1000DhcpSnoopingStatisticsInterfaceTxOffer_Type = Unsigned32
_Cie1000DhcpSnoopingStatisticsInterfaceTxOffer_Object = MibTableColumn
cie1000DhcpSnoopingStatisticsInterfaceTxOffer = _Cie1000DhcpSnoopingStatisticsInterfaceTxOffer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 56, 1, 5, 2, 1, 17),
    _Cie1000DhcpSnoopingStatisticsInterfaceTxOffer_Type()
)
cie1000DhcpSnoopingStatisticsInterfaceTxOffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000DhcpSnoopingStatisticsInterfaceTxOffer.setStatus("current")
_Cie1000DhcpSnoopingStatisticsInterfaceTxRequest_Type = Unsigned32
_Cie1000DhcpSnoopingStatisticsInterfaceTxRequest_Object = MibTableColumn
cie1000DhcpSnoopingStatisticsInterfaceTxRequest = _Cie1000DhcpSnoopingStatisticsInterfaceTxRequest_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 56, 1, 5, 2, 1, 18),
    _Cie1000DhcpSnoopingStatisticsInterfaceTxRequest_Type()
)
cie1000DhcpSnoopingStatisticsInterfaceTxRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000DhcpSnoopingStatisticsInterfaceTxRequest.setStatus("current")
_Cie1000DhcpSnoopingStatisticsInterfaceTxDecline_Type = Unsigned32
_Cie1000DhcpSnoopingStatisticsInterfaceTxDecline_Object = MibTableColumn
cie1000DhcpSnoopingStatisticsInterfaceTxDecline = _Cie1000DhcpSnoopingStatisticsInterfaceTxDecline_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 56, 1, 5, 2, 1, 19),
    _Cie1000DhcpSnoopingStatisticsInterfaceTxDecline_Type()
)
cie1000DhcpSnoopingStatisticsInterfaceTxDecline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000DhcpSnoopingStatisticsInterfaceTxDecline.setStatus("current")
_Cie1000DhcpSnoopingStatisticsInterfaceTxAck_Type = Unsigned32
_Cie1000DhcpSnoopingStatisticsInterfaceTxAck_Object = MibTableColumn
cie1000DhcpSnoopingStatisticsInterfaceTxAck = _Cie1000DhcpSnoopingStatisticsInterfaceTxAck_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 56, 1, 5, 2, 1, 20),
    _Cie1000DhcpSnoopingStatisticsInterfaceTxAck_Type()
)
cie1000DhcpSnoopingStatisticsInterfaceTxAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000DhcpSnoopingStatisticsInterfaceTxAck.setStatus("current")
_Cie1000DhcpSnoopingStatisticsInterfaceTxNak_Type = Unsigned32
_Cie1000DhcpSnoopingStatisticsInterfaceTxNak_Object = MibTableColumn
cie1000DhcpSnoopingStatisticsInterfaceTxNak = _Cie1000DhcpSnoopingStatisticsInterfaceTxNak_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 56, 1, 5, 2, 1, 21),
    _Cie1000DhcpSnoopingStatisticsInterfaceTxNak_Type()
)
cie1000DhcpSnoopingStatisticsInterfaceTxNak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000DhcpSnoopingStatisticsInterfaceTxNak.setStatus("current")
_Cie1000DhcpSnoopingStatisticsInterfaceTxRelease_Type = Unsigned32
_Cie1000DhcpSnoopingStatisticsInterfaceTxRelease_Object = MibTableColumn
cie1000DhcpSnoopingStatisticsInterfaceTxRelease = _Cie1000DhcpSnoopingStatisticsInterfaceTxRelease_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 56, 1, 5, 2, 1, 22),
    _Cie1000DhcpSnoopingStatisticsInterfaceTxRelease_Type()
)
cie1000DhcpSnoopingStatisticsInterfaceTxRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000DhcpSnoopingStatisticsInterfaceTxRelease.setStatus("current")
_Cie1000DhcpSnoopingStatisticsInterfaceTxInform_Type = Unsigned32
_Cie1000DhcpSnoopingStatisticsInterfaceTxInform_Object = MibTableColumn
cie1000DhcpSnoopingStatisticsInterfaceTxInform = _Cie1000DhcpSnoopingStatisticsInterfaceTxInform_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 56, 1, 5, 2, 1, 23),
    _Cie1000DhcpSnoopingStatisticsInterfaceTxInform_Type()
)
cie1000DhcpSnoopingStatisticsInterfaceTxInform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000DhcpSnoopingStatisticsInterfaceTxInform.setStatus("current")
_Cie1000DhcpSnoopingStatisticsInterfaceTxLeaseQuery_Type = Unsigned32
_Cie1000DhcpSnoopingStatisticsInterfaceTxLeaseQuery_Object = MibTableColumn
cie1000DhcpSnoopingStatisticsInterfaceTxLeaseQuery = _Cie1000DhcpSnoopingStatisticsInterfaceTxLeaseQuery_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 56, 1, 5, 2, 1, 24),
    _Cie1000DhcpSnoopingStatisticsInterfaceTxLeaseQuery_Type()
)
cie1000DhcpSnoopingStatisticsInterfaceTxLeaseQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000DhcpSnoopingStatisticsInterfaceTxLeaseQuery.setStatus("current")
_Cie1000DhcpSnoopingStatisticsInterfaceTxLeaseUnassigned_Type = Unsigned32
_Cie1000DhcpSnoopingStatisticsInterfaceTxLeaseUnassigned_Object = MibTableColumn
cie1000DhcpSnoopingStatisticsInterfaceTxLeaseUnassigned = _Cie1000DhcpSnoopingStatisticsInterfaceTxLeaseUnassigned_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 56, 1, 5, 2, 1, 25),
    _Cie1000DhcpSnoopingStatisticsInterfaceTxLeaseUnassigned_Type()
)
cie1000DhcpSnoopingStatisticsInterfaceTxLeaseUnassigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000DhcpSnoopingStatisticsInterfaceTxLeaseUnassigned.setStatus("current")
_Cie1000DhcpSnoopingStatisticsInterfaceTxLeaseUnknown_Type = Unsigned32
_Cie1000DhcpSnoopingStatisticsInterfaceTxLeaseUnknown_Object = MibTableColumn
cie1000DhcpSnoopingStatisticsInterfaceTxLeaseUnknown = _Cie1000DhcpSnoopingStatisticsInterfaceTxLeaseUnknown_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 56, 1, 5, 2, 1, 26),
    _Cie1000DhcpSnoopingStatisticsInterfaceTxLeaseUnknown_Type()
)
cie1000DhcpSnoopingStatisticsInterfaceTxLeaseUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000DhcpSnoopingStatisticsInterfaceTxLeaseUnknown.setStatus("current")
_Cie1000DhcpSnoopingStatisticsInterfaceTxLeaseActive_Type = Unsigned32
_Cie1000DhcpSnoopingStatisticsInterfaceTxLeaseActive_Object = MibTableColumn
cie1000DhcpSnoopingStatisticsInterfaceTxLeaseActive = _Cie1000DhcpSnoopingStatisticsInterfaceTxLeaseActive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 56, 1, 5, 2, 1, 27),
    _Cie1000DhcpSnoopingStatisticsInterfaceTxLeaseActive_Type()
)
cie1000DhcpSnoopingStatisticsInterfaceTxLeaseActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000DhcpSnoopingStatisticsInterfaceTxLeaseActive.setStatus("current")
_Cie1000DhcpSnoopingMibConformance_ObjectIdentity = ObjectIdentity
cie1000DhcpSnoopingMibConformance = _Cie1000DhcpSnoopingMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 56, 2)
)
_Cie1000DhcpSnoopingMibCompliances_ObjectIdentity = ObjectIdentity
cie1000DhcpSnoopingMibCompliances = _Cie1000DhcpSnoopingMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 56, 2, 1)
)
_Cie1000DhcpSnoopingMibGroups_ObjectIdentity = ObjectIdentity
cie1000DhcpSnoopingMibGroups = _Cie1000DhcpSnoopingMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 56, 2, 2)
)

# Managed Objects groups

cie1000DhcpSnoopingConfigGlobalsInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 56, 2, 2, 1)
)
cie1000DhcpSnoopingConfigGlobalsInfoGroup.setObjects(
    ("CIE1000-DHCP-SNOOPING-MIB", "cie1000DhcpSnoopingConfigGlobalsMode")
)
if mibBuilder.loadTexts:
    cie1000DhcpSnoopingConfigGlobalsInfoGroup.setStatus("current")

cie1000DhcpSnoopingConfigInterfaceInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 56, 2, 2, 2)
)
cie1000DhcpSnoopingConfigInterfaceInfoGroup.setObjects(
      *(("CIE1000-DHCP-SNOOPING-MIB", "cie1000DhcpSnoopingConfigInterfaceIfIndex"),
        ("CIE1000-DHCP-SNOOPING-MIB", "cie1000DhcpSnoopingConfigInterfaceTrustMode"))
)
if mibBuilder.loadTexts:
    cie1000DhcpSnoopingConfigInterfaceInfoGroup.setStatus("current")

cie1000DhcpSnoopingStatusAssignedIpTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 56, 2, 2, 3)
)
cie1000DhcpSnoopingStatusAssignedIpTableInfoGroup.setObjects(
      *(("CIE1000-DHCP-SNOOPING-MIB", "cie1000DhcpSnoopingStatusAssignedIpMacAddress"),
        ("CIE1000-DHCP-SNOOPING-MIB", "cie1000DhcpSnoopingStatusAssignedIpVlanId"),
        ("CIE1000-DHCP-SNOOPING-MIB", "cie1000DhcpSnoopingStatusAssignedIpIfIndex"),
        ("CIE1000-DHCP-SNOOPING-MIB", "cie1000DhcpSnoopingStatusAssignedIpIpAddress"),
        ("CIE1000-DHCP-SNOOPING-MIB", "cie1000DhcpSnoopingStatusAssignedIpNetmask"),
        ("CIE1000-DHCP-SNOOPING-MIB", "cie1000DhcpSnoopingStatusAssignedIpDhcpServerIp"))
)
if mibBuilder.loadTexts:
    cie1000DhcpSnoopingStatusAssignedIpTableInfoGroup.setStatus("current")

cie1000DhcpSnoopingControlInterfaceClearStatisticsTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 56, 2, 2, 4)
)
cie1000DhcpSnoopingControlInterfaceClearStatisticsTableInfoGroup.setObjects(
      *(("CIE1000-DHCP-SNOOPING-MIB", "cie1000DhcpSnoopingControlInterfaceClearStatisticsIfIndex"),
        ("CIE1000-DHCP-SNOOPING-MIB", "cie1000DhcpSnoopingControlInterfaceClearStatisticsClear"))
)
if mibBuilder.loadTexts:
    cie1000DhcpSnoopingControlInterfaceClearStatisticsTableInfoGroup.setStatus("current")

cie1000DhcpSnoopingStatisticsInterfaceTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 56, 2, 2, 5)
)
cie1000DhcpSnoopingStatisticsInterfaceTableInfoGroup.setObjects(
      *(("CIE1000-DHCP-SNOOPING-MIB", "cie1000DhcpSnoopingStatisticsInterfaceIfIndex"),
        ("CIE1000-DHCP-SNOOPING-MIB", "cie1000DhcpSnoopingStatisticsInterfaceRxDiscover"),
        ("CIE1000-DHCP-SNOOPING-MIB", "cie1000DhcpSnoopingStatisticsInterfaceRxOffer"),
        ("CIE1000-DHCP-SNOOPING-MIB", "cie1000DhcpSnoopingStatisticsInterfaceRxRequest"),
        ("CIE1000-DHCP-SNOOPING-MIB", "cie1000DhcpSnoopingStatisticsInterfaceRxDecline"),
        ("CIE1000-DHCP-SNOOPING-MIB", "cie1000DhcpSnoopingStatisticsInterfaceRxAck"),
        ("CIE1000-DHCP-SNOOPING-MIB", "cie1000DhcpSnoopingStatisticsInterfaceRxNak"),
        ("CIE1000-DHCP-SNOOPING-MIB", "cie1000DhcpSnoopingStatisticsInterfaceRxRelease"),
        ("CIE1000-DHCP-SNOOPING-MIB", "cie1000DhcpSnoopingStatisticsInterfaceRxInform"),
        ("CIE1000-DHCP-SNOOPING-MIB", "cie1000DhcpSnoopingStatisticsInterfaceRxLeaseQuery"),
        ("CIE1000-DHCP-SNOOPING-MIB", "cie1000DhcpSnoopingStatisticsInterfaceRxLeaseUnassigned"),
        ("CIE1000-DHCP-SNOOPING-MIB", "cie1000DhcpSnoopingStatisticsInterfaceRxLeaseUnknown"),
        ("CIE1000-DHCP-SNOOPING-MIB", "cie1000DhcpSnoopingStatisticsInterfaceRxLeaseActive"),
        ("CIE1000-DHCP-SNOOPING-MIB", "cie1000DhcpSnoopingStatisticsInterfaceRxDiscardChksumErr"),
        ("CIE1000-DHCP-SNOOPING-MIB", "cie1000DhcpSnoopingStatisticsInterfaceRxDiscardUntrust"),
        ("CIE1000-DHCP-SNOOPING-MIB", "cie1000DhcpSnoopingStatisticsInterfaceTxDiscover"),
        ("CIE1000-DHCP-SNOOPING-MIB", "cie1000DhcpSnoopingStatisticsInterfaceTxOffer"),
        ("CIE1000-DHCP-SNOOPING-MIB", "cie1000DhcpSnoopingStatisticsInterfaceTxRequest"),
        ("CIE1000-DHCP-SNOOPING-MIB", "cie1000DhcpSnoopingStatisticsInterfaceTxDecline"),
        ("CIE1000-DHCP-SNOOPING-MIB", "cie1000DhcpSnoopingStatisticsInterfaceTxAck"),
        ("CIE1000-DHCP-SNOOPING-MIB", "cie1000DhcpSnoopingStatisticsInterfaceTxNak"),
        ("CIE1000-DHCP-SNOOPING-MIB", "cie1000DhcpSnoopingStatisticsInterfaceTxRelease"),
        ("CIE1000-DHCP-SNOOPING-MIB", "cie1000DhcpSnoopingStatisticsInterfaceTxInform"),
        ("CIE1000-DHCP-SNOOPING-MIB", "cie1000DhcpSnoopingStatisticsInterfaceTxLeaseQuery"),
        ("CIE1000-DHCP-SNOOPING-MIB", "cie1000DhcpSnoopingStatisticsInterfaceTxLeaseUnassigned"),
        ("CIE1000-DHCP-SNOOPING-MIB", "cie1000DhcpSnoopingStatisticsInterfaceTxLeaseUnknown"),
        ("CIE1000-DHCP-SNOOPING-MIB", "cie1000DhcpSnoopingStatisticsInterfaceTxLeaseActive"))
)
if mibBuilder.loadTexts:
    cie1000DhcpSnoopingStatisticsInterfaceTableInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cie1000DhcpSnoopingMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 56, 2, 1, 1)
)
cie1000DhcpSnoopingMibCompliance.setObjects(
      *(("CIE1000-DHCP-SNOOPING-MIB", "cie1000DhcpSnoopingConfigGlobalsInfoGroup"),
        ("CIE1000-DHCP-SNOOPING-MIB", "cie1000DhcpSnoopingConfigInterfaceInfoGroup"),
        ("CIE1000-DHCP-SNOOPING-MIB", "cie1000DhcpSnoopingStatusAssignedIpTableInfoGroup"),
        ("CIE1000-DHCP-SNOOPING-MIB", "cie1000DhcpSnoopingControlInterfaceClearStatisticsTableInfoGroup"),
        ("CIE1000-DHCP-SNOOPING-MIB", "cie1000DhcpSnoopingStatisticsInterfaceTableInfoGroup"))
)
if mibBuilder.loadTexts:
    cie1000DhcpSnoopingMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIE1000-DHCP-SNOOPING-MIB",
    **{"cie1000DhcpSnoopingMib": cie1000DhcpSnoopingMib,
       "cie1000DhcpSnoopingMibObjects": cie1000DhcpSnoopingMibObjects,
       "cie1000DhcpSnoopingConfig": cie1000DhcpSnoopingConfig,
       "cie1000DhcpSnoopingConfigGlobals": cie1000DhcpSnoopingConfigGlobals,
       "cie1000DhcpSnoopingConfigGlobalsMode": cie1000DhcpSnoopingConfigGlobalsMode,
       "cie1000DhcpSnoopingConfigInterfaceTable": cie1000DhcpSnoopingConfigInterfaceTable,
       "cie1000DhcpSnoopingConfigInterfaceEntry": cie1000DhcpSnoopingConfigInterfaceEntry,
       "cie1000DhcpSnoopingConfigInterfaceIfIndex": cie1000DhcpSnoopingConfigInterfaceIfIndex,
       "cie1000DhcpSnoopingConfigInterfaceTrustMode": cie1000DhcpSnoopingConfigInterfaceTrustMode,
       "cie1000DhcpSnoopingStatus": cie1000DhcpSnoopingStatus,
       "cie1000DhcpSnoopingStatusAssignedIpTable": cie1000DhcpSnoopingStatusAssignedIpTable,
       "cie1000DhcpSnoopingStatusAssignedIpEntry": cie1000DhcpSnoopingStatusAssignedIpEntry,
       "cie1000DhcpSnoopingStatusAssignedIpMacAddress": cie1000DhcpSnoopingStatusAssignedIpMacAddress,
       "cie1000DhcpSnoopingStatusAssignedIpVlanId": cie1000DhcpSnoopingStatusAssignedIpVlanId,
       "cie1000DhcpSnoopingStatusAssignedIpIfIndex": cie1000DhcpSnoopingStatusAssignedIpIfIndex,
       "cie1000DhcpSnoopingStatusAssignedIpIpAddress": cie1000DhcpSnoopingStatusAssignedIpIpAddress,
       "cie1000DhcpSnoopingStatusAssignedIpNetmask": cie1000DhcpSnoopingStatusAssignedIpNetmask,
       "cie1000DhcpSnoopingStatusAssignedIpDhcpServerIp": cie1000DhcpSnoopingStatusAssignedIpDhcpServerIp,
       "cie1000DhcpSnoopingControl": cie1000DhcpSnoopingControl,
       "cie1000DhcpSnoopingControlInterfaceClearStatisticsTable": cie1000DhcpSnoopingControlInterfaceClearStatisticsTable,
       "cie1000DhcpSnoopingControlInterfaceClearStatisticsEntry": cie1000DhcpSnoopingControlInterfaceClearStatisticsEntry,
       "cie1000DhcpSnoopingControlInterfaceClearStatisticsIfIndex": cie1000DhcpSnoopingControlInterfaceClearStatisticsIfIndex,
       "cie1000DhcpSnoopingControlInterfaceClearStatisticsClear": cie1000DhcpSnoopingControlInterfaceClearStatisticsClear,
       "cie1000DhcpSnoopingStatistics": cie1000DhcpSnoopingStatistics,
       "cie1000DhcpSnoopingStatisticsInterfaceTable": cie1000DhcpSnoopingStatisticsInterfaceTable,
       "cie1000DhcpSnoopingStatisticsInterfaceEntry": cie1000DhcpSnoopingStatisticsInterfaceEntry,
       "cie1000DhcpSnoopingStatisticsInterfaceIfIndex": cie1000DhcpSnoopingStatisticsInterfaceIfIndex,
       "cie1000DhcpSnoopingStatisticsInterfaceRxDiscover": cie1000DhcpSnoopingStatisticsInterfaceRxDiscover,
       "cie1000DhcpSnoopingStatisticsInterfaceRxOffer": cie1000DhcpSnoopingStatisticsInterfaceRxOffer,
       "cie1000DhcpSnoopingStatisticsInterfaceRxRequest": cie1000DhcpSnoopingStatisticsInterfaceRxRequest,
       "cie1000DhcpSnoopingStatisticsInterfaceRxDecline": cie1000DhcpSnoopingStatisticsInterfaceRxDecline,
       "cie1000DhcpSnoopingStatisticsInterfaceRxAck": cie1000DhcpSnoopingStatisticsInterfaceRxAck,
       "cie1000DhcpSnoopingStatisticsInterfaceRxNak": cie1000DhcpSnoopingStatisticsInterfaceRxNak,
       "cie1000DhcpSnoopingStatisticsInterfaceRxRelease": cie1000DhcpSnoopingStatisticsInterfaceRxRelease,
       "cie1000DhcpSnoopingStatisticsInterfaceRxInform": cie1000DhcpSnoopingStatisticsInterfaceRxInform,
       "cie1000DhcpSnoopingStatisticsInterfaceRxLeaseQuery": cie1000DhcpSnoopingStatisticsInterfaceRxLeaseQuery,
       "cie1000DhcpSnoopingStatisticsInterfaceRxLeaseUnassigned": cie1000DhcpSnoopingStatisticsInterfaceRxLeaseUnassigned,
       "cie1000DhcpSnoopingStatisticsInterfaceRxLeaseUnknown": cie1000DhcpSnoopingStatisticsInterfaceRxLeaseUnknown,
       "cie1000DhcpSnoopingStatisticsInterfaceRxLeaseActive": cie1000DhcpSnoopingStatisticsInterfaceRxLeaseActive,
       "cie1000DhcpSnoopingStatisticsInterfaceRxDiscardChksumErr": cie1000DhcpSnoopingStatisticsInterfaceRxDiscardChksumErr,
       "cie1000DhcpSnoopingStatisticsInterfaceRxDiscardUntrust": cie1000DhcpSnoopingStatisticsInterfaceRxDiscardUntrust,
       "cie1000DhcpSnoopingStatisticsInterfaceTxDiscover": cie1000DhcpSnoopingStatisticsInterfaceTxDiscover,
       "cie1000DhcpSnoopingStatisticsInterfaceTxOffer": cie1000DhcpSnoopingStatisticsInterfaceTxOffer,
       "cie1000DhcpSnoopingStatisticsInterfaceTxRequest": cie1000DhcpSnoopingStatisticsInterfaceTxRequest,
       "cie1000DhcpSnoopingStatisticsInterfaceTxDecline": cie1000DhcpSnoopingStatisticsInterfaceTxDecline,
       "cie1000DhcpSnoopingStatisticsInterfaceTxAck": cie1000DhcpSnoopingStatisticsInterfaceTxAck,
       "cie1000DhcpSnoopingStatisticsInterfaceTxNak": cie1000DhcpSnoopingStatisticsInterfaceTxNak,
       "cie1000DhcpSnoopingStatisticsInterfaceTxRelease": cie1000DhcpSnoopingStatisticsInterfaceTxRelease,
       "cie1000DhcpSnoopingStatisticsInterfaceTxInform": cie1000DhcpSnoopingStatisticsInterfaceTxInform,
       "cie1000DhcpSnoopingStatisticsInterfaceTxLeaseQuery": cie1000DhcpSnoopingStatisticsInterfaceTxLeaseQuery,
       "cie1000DhcpSnoopingStatisticsInterfaceTxLeaseUnassigned": cie1000DhcpSnoopingStatisticsInterfaceTxLeaseUnassigned,
       "cie1000DhcpSnoopingStatisticsInterfaceTxLeaseUnknown": cie1000DhcpSnoopingStatisticsInterfaceTxLeaseUnknown,
       "cie1000DhcpSnoopingStatisticsInterfaceTxLeaseActive": cie1000DhcpSnoopingStatisticsInterfaceTxLeaseActive,
       "cie1000DhcpSnoopingMibConformance": cie1000DhcpSnoopingMibConformance,
       "cie1000DhcpSnoopingMibCompliances": cie1000DhcpSnoopingMibCompliances,
       "cie1000DhcpSnoopingMibCompliance": cie1000DhcpSnoopingMibCompliance,
       "cie1000DhcpSnoopingMibGroups": cie1000DhcpSnoopingMibGroups,
       "cie1000DhcpSnoopingConfigGlobalsInfoGroup": cie1000DhcpSnoopingConfigGlobalsInfoGroup,
       "cie1000DhcpSnoopingConfigInterfaceInfoGroup": cie1000DhcpSnoopingConfigInterfaceInfoGroup,
       "cie1000DhcpSnoopingStatusAssignedIpTableInfoGroup": cie1000DhcpSnoopingStatusAssignedIpTableInfoGroup,
       "cie1000DhcpSnoopingControlInterfaceClearStatisticsTableInfoGroup": cie1000DhcpSnoopingControlInterfaceClearStatisticsTableInfoGroup,
       "cie1000DhcpSnoopingStatisticsInterfaceTableInfoGroup": cie1000DhcpSnoopingStatisticsInterfaceTableInfoGroup}
)
