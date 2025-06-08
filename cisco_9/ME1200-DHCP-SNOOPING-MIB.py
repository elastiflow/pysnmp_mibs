# SNMP MIB module (ME1200-DHCP-SNOOPING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/ME1200-DHCP-SNOOPING-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 09:05:30 2025
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

(me1200SwitchMgmt,) = mibBuilder.importSymbols(
    "CISCOME1200-MIB",
    "me1200SwitchMgmt")

(ME1200InterfaceIndex,) = mibBuilder.importSymbols(
    "ME1200-TC",
    "ME1200InterfaceIndex")

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

me1200DhcpSnoopingMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 56)
)
if mibBuilder.loadTexts:
    me1200DhcpSnoopingMIB.setRevisions(
        ("2014-03-28 00:00",
         "2014-03-11 00:00",
         "2014-02-18 00:00",
         "2014-01-29 00:00",
         "2013-10-30 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Me1200DhcpSnoopingMIBObjects_ObjectIdentity = ObjectIdentity
me1200DhcpSnoopingMIBObjects = _Me1200DhcpSnoopingMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 56, 1)
)
_Me1200DhcpSnoopingConfig_ObjectIdentity = ObjectIdentity
me1200DhcpSnoopingConfig = _Me1200DhcpSnoopingConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 56, 1, 2)
)
_Me1200DhcpSnoopingGlobals_ObjectIdentity = ObjectIdentity
me1200DhcpSnoopingGlobals = _Me1200DhcpSnoopingGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 56, 1, 2, 1)
)
_Me1200DhcpSnoopingGlobalsMode_Type = TruthValue
_Me1200DhcpSnoopingGlobalsMode_Object = MibScalar
me1200DhcpSnoopingGlobalsMode = _Me1200DhcpSnoopingGlobalsMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 56, 1, 2, 1, 1),
    _Me1200DhcpSnoopingGlobalsMode_Type()
)
me1200DhcpSnoopingGlobalsMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpSnoopingGlobalsMode.setStatus("current")
_Me1200DhcpSnoopingInterfaceTable_Object = MibTable
me1200DhcpSnoopingInterfaceTable = _Me1200DhcpSnoopingInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 56, 1, 2, 2)
)
if mibBuilder.loadTexts:
    me1200DhcpSnoopingInterfaceTable.setStatus("current")
_Me1200DhcpSnoopingInterfaceEntry_Object = MibTableRow
me1200DhcpSnoopingInterfaceEntry = _Me1200DhcpSnoopingInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 56, 1, 2, 2, 1)
)
me1200DhcpSnoopingInterfaceEntry.setIndexNames(
    (0, "ME1200-DHCP-SNOOPING-MIB", "me1200DhcpSnoopingInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    me1200DhcpSnoopingInterfaceEntry.setStatus("current")
_Me1200DhcpSnoopingInterfaceIfIndex_Type = ME1200InterfaceIndex
_Me1200DhcpSnoopingInterfaceIfIndex_Object = MibTableColumn
me1200DhcpSnoopingInterfaceIfIndex = _Me1200DhcpSnoopingInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 56, 1, 2, 2, 1, 1),
    _Me1200DhcpSnoopingInterfaceIfIndex_Type()
)
me1200DhcpSnoopingInterfaceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200DhcpSnoopingInterfaceIfIndex.setStatus("current")
_Me1200DhcpSnoopingInterfaceTrustMode_Type = TruthValue
_Me1200DhcpSnoopingInterfaceTrustMode_Object = MibTableColumn
me1200DhcpSnoopingInterfaceTrustMode = _Me1200DhcpSnoopingInterfaceTrustMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 56, 1, 2, 2, 1, 2),
    _Me1200DhcpSnoopingInterfaceTrustMode_Type()
)
me1200DhcpSnoopingInterfaceTrustMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpSnoopingInterfaceTrustMode.setStatus("current")
_Me1200DhcpSnoopingStatus_ObjectIdentity = ObjectIdentity
me1200DhcpSnoopingStatus = _Me1200DhcpSnoopingStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 56, 1, 3)
)
_Me1200DhcpSnoopingAssignedIpTable_Object = MibTable
me1200DhcpSnoopingAssignedIpTable = _Me1200DhcpSnoopingAssignedIpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 56, 1, 3, 1)
)
if mibBuilder.loadTexts:
    me1200DhcpSnoopingAssignedIpTable.setStatus("current")
_Me1200DhcpSnoopingAssignedIpEntry_Object = MibTableRow
me1200DhcpSnoopingAssignedIpEntry = _Me1200DhcpSnoopingAssignedIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 56, 1, 3, 1, 1)
)
me1200DhcpSnoopingAssignedIpEntry.setIndexNames(
    (0, "ME1200-DHCP-SNOOPING-MIB", "me1200DhcpSnoopingAssignedIpMacAddress"),
    (0, "ME1200-DHCP-SNOOPING-MIB", "me1200DhcpSnoopingAssignedIpVlanId"),
)
if mibBuilder.loadTexts:
    me1200DhcpSnoopingAssignedIpEntry.setStatus("current")
_Me1200DhcpSnoopingAssignedIpMacAddress_Type = MacAddress
_Me1200DhcpSnoopingAssignedIpMacAddress_Object = MibTableColumn
me1200DhcpSnoopingAssignedIpMacAddress = _Me1200DhcpSnoopingAssignedIpMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 56, 1, 3, 1, 1, 1),
    _Me1200DhcpSnoopingAssignedIpMacAddress_Type()
)
me1200DhcpSnoopingAssignedIpMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200DhcpSnoopingAssignedIpMacAddress.setStatus("current")


class _Me1200DhcpSnoopingAssignedIpVlanId_Type(Integer32):
    """Custom type me1200DhcpSnoopingAssignedIpVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Me1200DhcpSnoopingAssignedIpVlanId_Type.__name__ = "Integer32"
_Me1200DhcpSnoopingAssignedIpVlanId_Object = MibTableColumn
me1200DhcpSnoopingAssignedIpVlanId = _Me1200DhcpSnoopingAssignedIpVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 56, 1, 3, 1, 1, 2),
    _Me1200DhcpSnoopingAssignedIpVlanId_Type()
)
me1200DhcpSnoopingAssignedIpVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200DhcpSnoopingAssignedIpVlanId.setStatus("current")
_Me1200DhcpSnoopingAssignedIpIfIndex_Type = ME1200InterfaceIndex
_Me1200DhcpSnoopingAssignedIpIfIndex_Object = MibTableColumn
me1200DhcpSnoopingAssignedIpIfIndex = _Me1200DhcpSnoopingAssignedIpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 56, 1, 3, 1, 1, 3),
    _Me1200DhcpSnoopingAssignedIpIfIndex_Type()
)
me1200DhcpSnoopingAssignedIpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DhcpSnoopingAssignedIpIfIndex.setStatus("current")
_Me1200DhcpSnoopingAssignedIpIpAddress_Type = IpAddress
_Me1200DhcpSnoopingAssignedIpIpAddress_Object = MibTableColumn
me1200DhcpSnoopingAssignedIpIpAddress = _Me1200DhcpSnoopingAssignedIpIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 56, 1, 3, 1, 1, 4),
    _Me1200DhcpSnoopingAssignedIpIpAddress_Type()
)
me1200DhcpSnoopingAssignedIpIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DhcpSnoopingAssignedIpIpAddress.setStatus("current")
_Me1200DhcpSnoopingAssignedIpNetmask_Type = IpAddress
_Me1200DhcpSnoopingAssignedIpNetmask_Object = MibTableColumn
me1200DhcpSnoopingAssignedIpNetmask = _Me1200DhcpSnoopingAssignedIpNetmask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 56, 1, 3, 1, 1, 5),
    _Me1200DhcpSnoopingAssignedIpNetmask_Type()
)
me1200DhcpSnoopingAssignedIpNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DhcpSnoopingAssignedIpNetmask.setStatus("current")
_Me1200DhcpSnoopingAssignedIpDhcpServerIp_Type = IpAddress
_Me1200DhcpSnoopingAssignedIpDhcpServerIp_Object = MibTableColumn
me1200DhcpSnoopingAssignedIpDhcpServerIp = _Me1200DhcpSnoopingAssignedIpDhcpServerIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 56, 1, 3, 1, 1, 6),
    _Me1200DhcpSnoopingAssignedIpDhcpServerIp_Type()
)
me1200DhcpSnoopingAssignedIpDhcpServerIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DhcpSnoopingAssignedIpDhcpServerIp.setStatus("current")
_Me1200DhcpSnoopingInterfaceStatisticsTable_Object = MibTable
me1200DhcpSnoopingInterfaceStatisticsTable = _Me1200DhcpSnoopingInterfaceStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 56, 1, 3, 2)
)
if mibBuilder.loadTexts:
    me1200DhcpSnoopingInterfaceStatisticsTable.setStatus("current")
_Me1200DhcpSnoopingInterfaceStatisticsEntry_Object = MibTableRow
me1200DhcpSnoopingInterfaceStatisticsEntry = _Me1200DhcpSnoopingInterfaceStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 56, 1, 3, 2, 1)
)
me1200DhcpSnoopingInterfaceStatisticsEntry.setIndexNames(
    (0, "ME1200-DHCP-SNOOPING-MIB", "me1200DhcpSnoopingInterfaceStatisticsIfIndex"),
)
if mibBuilder.loadTexts:
    me1200DhcpSnoopingInterfaceStatisticsEntry.setStatus("current")
_Me1200DhcpSnoopingInterfaceStatisticsIfIndex_Type = ME1200InterfaceIndex
_Me1200DhcpSnoopingInterfaceStatisticsIfIndex_Object = MibTableColumn
me1200DhcpSnoopingInterfaceStatisticsIfIndex = _Me1200DhcpSnoopingInterfaceStatisticsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 56, 1, 3, 2, 1, 1),
    _Me1200DhcpSnoopingInterfaceStatisticsIfIndex_Type()
)
me1200DhcpSnoopingInterfaceStatisticsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200DhcpSnoopingInterfaceStatisticsIfIndex.setStatus("current")
_Me1200DhcpSnoopingInterfaceStatisticsRxDiscover_Type = Unsigned32
_Me1200DhcpSnoopingInterfaceStatisticsRxDiscover_Object = MibTableColumn
me1200DhcpSnoopingInterfaceStatisticsRxDiscover = _Me1200DhcpSnoopingInterfaceStatisticsRxDiscover_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 56, 1, 3, 2, 1, 2),
    _Me1200DhcpSnoopingInterfaceStatisticsRxDiscover_Type()
)
me1200DhcpSnoopingInterfaceStatisticsRxDiscover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DhcpSnoopingInterfaceStatisticsRxDiscover.setStatus("current")
_Me1200DhcpSnoopingInterfaceStatisticsRxOffer_Type = Unsigned32
_Me1200DhcpSnoopingInterfaceStatisticsRxOffer_Object = MibTableColumn
me1200DhcpSnoopingInterfaceStatisticsRxOffer = _Me1200DhcpSnoopingInterfaceStatisticsRxOffer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 56, 1, 3, 2, 1, 3),
    _Me1200DhcpSnoopingInterfaceStatisticsRxOffer_Type()
)
me1200DhcpSnoopingInterfaceStatisticsRxOffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DhcpSnoopingInterfaceStatisticsRxOffer.setStatus("current")
_Me1200DhcpSnoopingInterfaceStatisticsRxRequest_Type = Unsigned32
_Me1200DhcpSnoopingInterfaceStatisticsRxRequest_Object = MibTableColumn
me1200DhcpSnoopingInterfaceStatisticsRxRequest = _Me1200DhcpSnoopingInterfaceStatisticsRxRequest_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 56, 1, 3, 2, 1, 4),
    _Me1200DhcpSnoopingInterfaceStatisticsRxRequest_Type()
)
me1200DhcpSnoopingInterfaceStatisticsRxRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DhcpSnoopingInterfaceStatisticsRxRequest.setStatus("current")
_Me1200DhcpSnoopingInterfaceStatisticsRxDecline_Type = Unsigned32
_Me1200DhcpSnoopingInterfaceStatisticsRxDecline_Object = MibTableColumn
me1200DhcpSnoopingInterfaceStatisticsRxDecline = _Me1200DhcpSnoopingInterfaceStatisticsRxDecline_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 56, 1, 3, 2, 1, 5),
    _Me1200DhcpSnoopingInterfaceStatisticsRxDecline_Type()
)
me1200DhcpSnoopingInterfaceStatisticsRxDecline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DhcpSnoopingInterfaceStatisticsRxDecline.setStatus("current")
_Me1200DhcpSnoopingInterfaceStatisticsRxAck_Type = Unsigned32
_Me1200DhcpSnoopingInterfaceStatisticsRxAck_Object = MibTableColumn
me1200DhcpSnoopingInterfaceStatisticsRxAck = _Me1200DhcpSnoopingInterfaceStatisticsRxAck_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 56, 1, 3, 2, 1, 6),
    _Me1200DhcpSnoopingInterfaceStatisticsRxAck_Type()
)
me1200DhcpSnoopingInterfaceStatisticsRxAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DhcpSnoopingInterfaceStatisticsRxAck.setStatus("current")
_Me1200DhcpSnoopingInterfaceStatisticsRxNak_Type = Unsigned32
_Me1200DhcpSnoopingInterfaceStatisticsRxNak_Object = MibTableColumn
me1200DhcpSnoopingInterfaceStatisticsRxNak = _Me1200DhcpSnoopingInterfaceStatisticsRxNak_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 56, 1, 3, 2, 1, 7),
    _Me1200DhcpSnoopingInterfaceStatisticsRxNak_Type()
)
me1200DhcpSnoopingInterfaceStatisticsRxNak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DhcpSnoopingInterfaceStatisticsRxNak.setStatus("current")
_Me1200DhcpSnoopingInterfaceStatisticsRxRelease_Type = Unsigned32
_Me1200DhcpSnoopingInterfaceStatisticsRxRelease_Object = MibTableColumn
me1200DhcpSnoopingInterfaceStatisticsRxRelease = _Me1200DhcpSnoopingInterfaceStatisticsRxRelease_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 56, 1, 3, 2, 1, 8),
    _Me1200DhcpSnoopingInterfaceStatisticsRxRelease_Type()
)
me1200DhcpSnoopingInterfaceStatisticsRxRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DhcpSnoopingInterfaceStatisticsRxRelease.setStatus("current")
_Me1200DhcpSnoopingInterfaceStatisticsRxInform_Type = Unsigned32
_Me1200DhcpSnoopingInterfaceStatisticsRxInform_Object = MibTableColumn
me1200DhcpSnoopingInterfaceStatisticsRxInform = _Me1200DhcpSnoopingInterfaceStatisticsRxInform_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 56, 1, 3, 2, 1, 9),
    _Me1200DhcpSnoopingInterfaceStatisticsRxInform_Type()
)
me1200DhcpSnoopingInterfaceStatisticsRxInform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DhcpSnoopingInterfaceStatisticsRxInform.setStatus("current")
_Me1200DhcpSnoopingInterfaceStatisticsRxLeaseQuery_Type = Unsigned32
_Me1200DhcpSnoopingInterfaceStatisticsRxLeaseQuery_Object = MibTableColumn
me1200DhcpSnoopingInterfaceStatisticsRxLeaseQuery = _Me1200DhcpSnoopingInterfaceStatisticsRxLeaseQuery_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 56, 1, 3, 2, 1, 10),
    _Me1200DhcpSnoopingInterfaceStatisticsRxLeaseQuery_Type()
)
me1200DhcpSnoopingInterfaceStatisticsRxLeaseQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DhcpSnoopingInterfaceStatisticsRxLeaseQuery.setStatus("current")
_Me1200DhcpSnoopingInterfaceStatisticsRxLeaseUnassigned_Type = Unsigned32
_Me1200DhcpSnoopingInterfaceStatisticsRxLeaseUnassigned_Object = MibTableColumn
me1200DhcpSnoopingInterfaceStatisticsRxLeaseUnassigned = _Me1200DhcpSnoopingInterfaceStatisticsRxLeaseUnassigned_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 56, 1, 3, 2, 1, 11),
    _Me1200DhcpSnoopingInterfaceStatisticsRxLeaseUnassigned_Type()
)
me1200DhcpSnoopingInterfaceStatisticsRxLeaseUnassigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DhcpSnoopingInterfaceStatisticsRxLeaseUnassigned.setStatus("current")
_Me1200DhcpSnoopingInterfaceStatisticsRxLeaseUnknown_Type = Unsigned32
_Me1200DhcpSnoopingInterfaceStatisticsRxLeaseUnknown_Object = MibTableColumn
me1200DhcpSnoopingInterfaceStatisticsRxLeaseUnknown = _Me1200DhcpSnoopingInterfaceStatisticsRxLeaseUnknown_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 56, 1, 3, 2, 1, 12),
    _Me1200DhcpSnoopingInterfaceStatisticsRxLeaseUnknown_Type()
)
me1200DhcpSnoopingInterfaceStatisticsRxLeaseUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DhcpSnoopingInterfaceStatisticsRxLeaseUnknown.setStatus("current")
_Me1200DhcpSnoopingInterfaceStatisticsRxLeaseActive_Type = Unsigned32
_Me1200DhcpSnoopingInterfaceStatisticsRxLeaseActive_Object = MibTableColumn
me1200DhcpSnoopingInterfaceStatisticsRxLeaseActive = _Me1200DhcpSnoopingInterfaceStatisticsRxLeaseActive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 56, 1, 3, 2, 1, 13),
    _Me1200DhcpSnoopingInterfaceStatisticsRxLeaseActive_Type()
)
me1200DhcpSnoopingInterfaceStatisticsRxLeaseActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DhcpSnoopingInterfaceStatisticsRxLeaseActive.setStatus("current")
_Me1200DhcpSnoopingInterfaceStatisticsRxDiscardChksumErr_Type = Unsigned32
_Me1200DhcpSnoopingInterfaceStatisticsRxDiscardChksumErr_Object = MibTableColumn
me1200DhcpSnoopingInterfaceStatisticsRxDiscardChksumErr = _Me1200DhcpSnoopingInterfaceStatisticsRxDiscardChksumErr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 56, 1, 3, 2, 1, 14),
    _Me1200DhcpSnoopingInterfaceStatisticsRxDiscardChksumErr_Type()
)
me1200DhcpSnoopingInterfaceStatisticsRxDiscardChksumErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DhcpSnoopingInterfaceStatisticsRxDiscardChksumErr.setStatus("current")
_Me1200DhcpSnoopingInterfaceStatisticsRxDiscardUntrust_Type = Unsigned32
_Me1200DhcpSnoopingInterfaceStatisticsRxDiscardUntrust_Object = MibTableColumn
me1200DhcpSnoopingInterfaceStatisticsRxDiscardUntrust = _Me1200DhcpSnoopingInterfaceStatisticsRxDiscardUntrust_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 56, 1, 3, 2, 1, 15),
    _Me1200DhcpSnoopingInterfaceStatisticsRxDiscardUntrust_Type()
)
me1200DhcpSnoopingInterfaceStatisticsRxDiscardUntrust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DhcpSnoopingInterfaceStatisticsRxDiscardUntrust.setStatus("current")
_Me1200DhcpSnoopingInterfaceStatisticsTxDiscover_Type = Unsigned32
_Me1200DhcpSnoopingInterfaceStatisticsTxDiscover_Object = MibTableColumn
me1200DhcpSnoopingInterfaceStatisticsTxDiscover = _Me1200DhcpSnoopingInterfaceStatisticsTxDiscover_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 56, 1, 3, 2, 1, 16),
    _Me1200DhcpSnoopingInterfaceStatisticsTxDiscover_Type()
)
me1200DhcpSnoopingInterfaceStatisticsTxDiscover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DhcpSnoopingInterfaceStatisticsTxDiscover.setStatus("current")
_Me1200DhcpSnoopingInterfaceStatisticsTxOffer_Type = Unsigned32
_Me1200DhcpSnoopingInterfaceStatisticsTxOffer_Object = MibTableColumn
me1200DhcpSnoopingInterfaceStatisticsTxOffer = _Me1200DhcpSnoopingInterfaceStatisticsTxOffer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 56, 1, 3, 2, 1, 17),
    _Me1200DhcpSnoopingInterfaceStatisticsTxOffer_Type()
)
me1200DhcpSnoopingInterfaceStatisticsTxOffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DhcpSnoopingInterfaceStatisticsTxOffer.setStatus("current")
_Me1200DhcpSnoopingInterfaceStatisticsTxRequest_Type = Unsigned32
_Me1200DhcpSnoopingInterfaceStatisticsTxRequest_Object = MibTableColumn
me1200DhcpSnoopingInterfaceStatisticsTxRequest = _Me1200DhcpSnoopingInterfaceStatisticsTxRequest_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 56, 1, 3, 2, 1, 18),
    _Me1200DhcpSnoopingInterfaceStatisticsTxRequest_Type()
)
me1200DhcpSnoopingInterfaceStatisticsTxRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DhcpSnoopingInterfaceStatisticsTxRequest.setStatus("current")
_Me1200DhcpSnoopingInterfaceStatisticsTxDecline_Type = Unsigned32
_Me1200DhcpSnoopingInterfaceStatisticsTxDecline_Object = MibTableColumn
me1200DhcpSnoopingInterfaceStatisticsTxDecline = _Me1200DhcpSnoopingInterfaceStatisticsTxDecline_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 56, 1, 3, 2, 1, 19),
    _Me1200DhcpSnoopingInterfaceStatisticsTxDecline_Type()
)
me1200DhcpSnoopingInterfaceStatisticsTxDecline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DhcpSnoopingInterfaceStatisticsTxDecline.setStatus("current")
_Me1200DhcpSnoopingInterfaceStatisticsTxAck_Type = Unsigned32
_Me1200DhcpSnoopingInterfaceStatisticsTxAck_Object = MibTableColumn
me1200DhcpSnoopingInterfaceStatisticsTxAck = _Me1200DhcpSnoopingInterfaceStatisticsTxAck_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 56, 1, 3, 2, 1, 20),
    _Me1200DhcpSnoopingInterfaceStatisticsTxAck_Type()
)
me1200DhcpSnoopingInterfaceStatisticsTxAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DhcpSnoopingInterfaceStatisticsTxAck.setStatus("current")
_Me1200DhcpSnoopingInterfaceStatisticsTxNak_Type = Unsigned32
_Me1200DhcpSnoopingInterfaceStatisticsTxNak_Object = MibTableColumn
me1200DhcpSnoopingInterfaceStatisticsTxNak = _Me1200DhcpSnoopingInterfaceStatisticsTxNak_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 56, 1, 3, 2, 1, 21),
    _Me1200DhcpSnoopingInterfaceStatisticsTxNak_Type()
)
me1200DhcpSnoopingInterfaceStatisticsTxNak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DhcpSnoopingInterfaceStatisticsTxNak.setStatus("current")
_Me1200DhcpSnoopingInterfaceStatisticsTxRelease_Type = Unsigned32
_Me1200DhcpSnoopingInterfaceStatisticsTxRelease_Object = MibTableColumn
me1200DhcpSnoopingInterfaceStatisticsTxRelease = _Me1200DhcpSnoopingInterfaceStatisticsTxRelease_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 56, 1, 3, 2, 1, 22),
    _Me1200DhcpSnoopingInterfaceStatisticsTxRelease_Type()
)
me1200DhcpSnoopingInterfaceStatisticsTxRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DhcpSnoopingInterfaceStatisticsTxRelease.setStatus("current")
_Me1200DhcpSnoopingInterfaceStatisticsTxInform_Type = Unsigned32
_Me1200DhcpSnoopingInterfaceStatisticsTxInform_Object = MibTableColumn
me1200DhcpSnoopingInterfaceStatisticsTxInform = _Me1200DhcpSnoopingInterfaceStatisticsTxInform_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 56, 1, 3, 2, 1, 23),
    _Me1200DhcpSnoopingInterfaceStatisticsTxInform_Type()
)
me1200DhcpSnoopingInterfaceStatisticsTxInform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DhcpSnoopingInterfaceStatisticsTxInform.setStatus("current")
_Me1200DhcpSnoopingInterfaceStatisticsTxLeaseQuery_Type = Unsigned32
_Me1200DhcpSnoopingInterfaceStatisticsTxLeaseQuery_Object = MibTableColumn
me1200DhcpSnoopingInterfaceStatisticsTxLeaseQuery = _Me1200DhcpSnoopingInterfaceStatisticsTxLeaseQuery_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 56, 1, 3, 2, 1, 24),
    _Me1200DhcpSnoopingInterfaceStatisticsTxLeaseQuery_Type()
)
me1200DhcpSnoopingInterfaceStatisticsTxLeaseQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DhcpSnoopingInterfaceStatisticsTxLeaseQuery.setStatus("current")
_Me1200DhcpSnoopingInterfaceStatisticsTxLeaseUnassigned_Type = Unsigned32
_Me1200DhcpSnoopingInterfaceStatisticsTxLeaseUnassigned_Object = MibTableColumn
me1200DhcpSnoopingInterfaceStatisticsTxLeaseUnassigned = _Me1200DhcpSnoopingInterfaceStatisticsTxLeaseUnassigned_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 56, 1, 3, 2, 1, 25),
    _Me1200DhcpSnoopingInterfaceStatisticsTxLeaseUnassigned_Type()
)
me1200DhcpSnoopingInterfaceStatisticsTxLeaseUnassigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DhcpSnoopingInterfaceStatisticsTxLeaseUnassigned.setStatus("current")
_Me1200DhcpSnoopingInterfaceStatisticsTxLeaseUnknown_Type = Unsigned32
_Me1200DhcpSnoopingInterfaceStatisticsTxLeaseUnknown_Object = MibTableColumn
me1200DhcpSnoopingInterfaceStatisticsTxLeaseUnknown = _Me1200DhcpSnoopingInterfaceStatisticsTxLeaseUnknown_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 56, 1, 3, 2, 1, 26),
    _Me1200DhcpSnoopingInterfaceStatisticsTxLeaseUnknown_Type()
)
me1200DhcpSnoopingInterfaceStatisticsTxLeaseUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DhcpSnoopingInterfaceStatisticsTxLeaseUnknown.setStatus("current")
_Me1200DhcpSnoopingInterfaceStatisticsTxLeaseActive_Type = Unsigned32
_Me1200DhcpSnoopingInterfaceStatisticsTxLeaseActive_Object = MibTableColumn
me1200DhcpSnoopingInterfaceStatisticsTxLeaseActive = _Me1200DhcpSnoopingInterfaceStatisticsTxLeaseActive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 56, 1, 3, 2, 1, 27),
    _Me1200DhcpSnoopingInterfaceStatisticsTxLeaseActive_Type()
)
me1200DhcpSnoopingInterfaceStatisticsTxLeaseActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DhcpSnoopingInterfaceStatisticsTxLeaseActive.setStatus("current")
_Me1200DhcpSnoopingControl_ObjectIdentity = ObjectIdentity
me1200DhcpSnoopingControl = _Me1200DhcpSnoopingControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 56, 1, 4)
)
_Me1200DhcpSnoopingInterfaceClearStatisticsTable_Object = MibTable
me1200DhcpSnoopingInterfaceClearStatisticsTable = _Me1200DhcpSnoopingInterfaceClearStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 56, 1, 4, 1)
)
if mibBuilder.loadTexts:
    me1200DhcpSnoopingInterfaceClearStatisticsTable.setStatus("current")
_Me1200DhcpSnoopingInterfaceClearStatisticsEntry_Object = MibTableRow
me1200DhcpSnoopingInterfaceClearStatisticsEntry = _Me1200DhcpSnoopingInterfaceClearStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 56, 1, 4, 1, 1)
)
me1200DhcpSnoopingInterfaceClearStatisticsEntry.setIndexNames(
    (0, "ME1200-DHCP-SNOOPING-MIB", "me1200DhcpSnoopingInterfaceClearStatisticsIfIndex"),
)
if mibBuilder.loadTexts:
    me1200DhcpSnoopingInterfaceClearStatisticsEntry.setStatus("current")
_Me1200DhcpSnoopingInterfaceClearStatisticsIfIndex_Type = ME1200InterfaceIndex
_Me1200DhcpSnoopingInterfaceClearStatisticsIfIndex_Object = MibTableColumn
me1200DhcpSnoopingInterfaceClearStatisticsIfIndex = _Me1200DhcpSnoopingInterfaceClearStatisticsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 56, 1, 4, 1, 1, 1),
    _Me1200DhcpSnoopingInterfaceClearStatisticsIfIndex_Type()
)
me1200DhcpSnoopingInterfaceClearStatisticsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200DhcpSnoopingInterfaceClearStatisticsIfIndex.setStatus("current")
_Me1200DhcpSnoopingInterfaceClearStatisticsClear_Type = TruthValue
_Me1200DhcpSnoopingInterfaceClearStatisticsClear_Object = MibTableColumn
me1200DhcpSnoopingInterfaceClearStatisticsClear = _Me1200DhcpSnoopingInterfaceClearStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 56, 1, 4, 1, 1, 2),
    _Me1200DhcpSnoopingInterfaceClearStatisticsClear_Type()
)
me1200DhcpSnoopingInterfaceClearStatisticsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpSnoopingInterfaceClearStatisticsClear.setStatus("current")
_Me1200DhcpSnoopingMIBConformance_ObjectIdentity = ObjectIdentity
me1200DhcpSnoopingMIBConformance = _Me1200DhcpSnoopingMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 56, 2)
)
_Me1200DhcpSnoopingMIBCompliances_ObjectIdentity = ObjectIdentity
me1200DhcpSnoopingMIBCompliances = _Me1200DhcpSnoopingMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 56, 2, 1)
)
_Me1200DhcpSnoopingMIBGroups_ObjectIdentity = ObjectIdentity
me1200DhcpSnoopingMIBGroups = _Me1200DhcpSnoopingMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 56, 2, 2)
)

# Managed Objects groups

me1200DhcpSnoopingGlobalsInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 56, 2, 2, 1)
)
me1200DhcpSnoopingGlobalsInfoGroup.setObjects(
    ("ME1200-DHCP-SNOOPING-MIB", "me1200DhcpSnoopingGlobalsMode")
)
if mibBuilder.loadTexts:
    me1200DhcpSnoopingGlobalsInfoGroup.setStatus("current")

me1200DhcpSnoopingInterfaceInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 56, 2, 2, 2)
)
me1200DhcpSnoopingInterfaceInfoGroup.setObjects(
    ("ME1200-DHCP-SNOOPING-MIB", "me1200DhcpSnoopingInterfaceTrustMode")
)
if mibBuilder.loadTexts:
    me1200DhcpSnoopingInterfaceInfoGroup.setStatus("current")

me1200DhcpSnoopingAssignedIpTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 56, 2, 2, 3)
)
me1200DhcpSnoopingAssignedIpTableInfoGroup.setObjects(
      *(("ME1200-DHCP-SNOOPING-MIB", "me1200DhcpSnoopingAssignedIpIfIndex"),
        ("ME1200-DHCP-SNOOPING-MIB", "me1200DhcpSnoopingAssignedIpIpAddress"),
        ("ME1200-DHCP-SNOOPING-MIB", "me1200DhcpSnoopingAssignedIpNetmask"),
        ("ME1200-DHCP-SNOOPING-MIB", "me1200DhcpSnoopingAssignedIpDhcpServerIp"))
)
if mibBuilder.loadTexts:
    me1200DhcpSnoopingAssignedIpTableInfoGroup.setStatus("current")

me1200DhcpSnoopingInterfaceStatisticsTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 56, 2, 2, 4)
)
me1200DhcpSnoopingInterfaceStatisticsTableInfoGroup.setObjects(
      *(("ME1200-DHCP-SNOOPING-MIB", "me1200DhcpSnoopingInterfaceStatisticsRxDiscover"),
        ("ME1200-DHCP-SNOOPING-MIB", "me1200DhcpSnoopingInterfaceStatisticsRxOffer"),
        ("ME1200-DHCP-SNOOPING-MIB", "me1200DhcpSnoopingInterfaceStatisticsRxRequest"),
        ("ME1200-DHCP-SNOOPING-MIB", "me1200DhcpSnoopingInterfaceStatisticsRxDecline"),
        ("ME1200-DHCP-SNOOPING-MIB", "me1200DhcpSnoopingInterfaceStatisticsRxAck"),
        ("ME1200-DHCP-SNOOPING-MIB", "me1200DhcpSnoopingInterfaceStatisticsRxNak"),
        ("ME1200-DHCP-SNOOPING-MIB", "me1200DhcpSnoopingInterfaceStatisticsRxRelease"),
        ("ME1200-DHCP-SNOOPING-MIB", "me1200DhcpSnoopingInterfaceStatisticsRxInform"),
        ("ME1200-DHCP-SNOOPING-MIB", "me1200DhcpSnoopingInterfaceStatisticsRxLeaseQuery"),
        ("ME1200-DHCP-SNOOPING-MIB", "me1200DhcpSnoopingInterfaceStatisticsRxLeaseUnassigned"),
        ("ME1200-DHCP-SNOOPING-MIB", "me1200DhcpSnoopingInterfaceStatisticsRxLeaseUnknown"),
        ("ME1200-DHCP-SNOOPING-MIB", "me1200DhcpSnoopingInterfaceStatisticsRxLeaseActive"),
        ("ME1200-DHCP-SNOOPING-MIB", "me1200DhcpSnoopingInterfaceStatisticsRxDiscardChksumErr"),
        ("ME1200-DHCP-SNOOPING-MIB", "me1200DhcpSnoopingInterfaceStatisticsRxDiscardUntrust"),
        ("ME1200-DHCP-SNOOPING-MIB", "me1200DhcpSnoopingInterfaceStatisticsTxDiscover"),
        ("ME1200-DHCP-SNOOPING-MIB", "me1200DhcpSnoopingInterfaceStatisticsTxOffer"),
        ("ME1200-DHCP-SNOOPING-MIB", "me1200DhcpSnoopingInterfaceStatisticsTxRequest"),
        ("ME1200-DHCP-SNOOPING-MIB", "me1200DhcpSnoopingInterfaceStatisticsTxDecline"),
        ("ME1200-DHCP-SNOOPING-MIB", "me1200DhcpSnoopingInterfaceStatisticsTxAck"),
        ("ME1200-DHCP-SNOOPING-MIB", "me1200DhcpSnoopingInterfaceStatisticsTxNak"),
        ("ME1200-DHCP-SNOOPING-MIB", "me1200DhcpSnoopingInterfaceStatisticsTxRelease"),
        ("ME1200-DHCP-SNOOPING-MIB", "me1200DhcpSnoopingInterfaceStatisticsTxInform"),
        ("ME1200-DHCP-SNOOPING-MIB", "me1200DhcpSnoopingInterfaceStatisticsTxLeaseQuery"),
        ("ME1200-DHCP-SNOOPING-MIB", "me1200DhcpSnoopingInterfaceStatisticsTxLeaseUnassigned"),
        ("ME1200-DHCP-SNOOPING-MIB", "me1200DhcpSnoopingInterfaceStatisticsTxLeaseUnknown"),
        ("ME1200-DHCP-SNOOPING-MIB", "me1200DhcpSnoopingInterfaceStatisticsTxLeaseActive"))
)
if mibBuilder.loadTexts:
    me1200DhcpSnoopingInterfaceStatisticsTableInfoGroup.setStatus("current")

me1200DhcpSnoopingInterfaceClearStatisticsTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 56, 2, 2, 5)
)
me1200DhcpSnoopingInterfaceClearStatisticsTableInfoGroup.setObjects(
    ("ME1200-DHCP-SNOOPING-MIB", "me1200DhcpSnoopingInterfaceClearStatisticsClear")
)
if mibBuilder.loadTexts:
    me1200DhcpSnoopingInterfaceClearStatisticsTableInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

me1200DhcpSnoopingMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 56, 2, 1, 1)
)
me1200DhcpSnoopingMIBCompliance.setObjects(
      *(("ME1200-DHCP-SNOOPING-MIB", "me1200DhcpSnoopingGlobalsInfoGroup"),
        ("ME1200-DHCP-SNOOPING-MIB", "me1200DhcpSnoopingInterfaceInfoGroup"),
        ("ME1200-DHCP-SNOOPING-MIB", "me1200DhcpSnoopingAssignedIpTableInfoGroup"),
        ("ME1200-DHCP-SNOOPING-MIB", "me1200DhcpSnoopingInterfaceStatisticsTableInfoGroup"),
        ("ME1200-DHCP-SNOOPING-MIB", "me1200DhcpSnoopingInterfaceClearStatisticsTableInfoGroup"))
)
if mibBuilder.loadTexts:
    me1200DhcpSnoopingMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ME1200-DHCP-SNOOPING-MIB",
    **{"me1200DhcpSnoopingMIB": me1200DhcpSnoopingMIB,
       "me1200DhcpSnoopingMIBObjects": me1200DhcpSnoopingMIBObjects,
       "me1200DhcpSnoopingConfig": me1200DhcpSnoopingConfig,
       "me1200DhcpSnoopingGlobals": me1200DhcpSnoopingGlobals,
       "me1200DhcpSnoopingGlobalsMode": me1200DhcpSnoopingGlobalsMode,
       "me1200DhcpSnoopingInterfaceTable": me1200DhcpSnoopingInterfaceTable,
       "me1200DhcpSnoopingInterfaceEntry": me1200DhcpSnoopingInterfaceEntry,
       "me1200DhcpSnoopingInterfaceIfIndex": me1200DhcpSnoopingInterfaceIfIndex,
       "me1200DhcpSnoopingInterfaceTrustMode": me1200DhcpSnoopingInterfaceTrustMode,
       "me1200DhcpSnoopingStatus": me1200DhcpSnoopingStatus,
       "me1200DhcpSnoopingAssignedIpTable": me1200DhcpSnoopingAssignedIpTable,
       "me1200DhcpSnoopingAssignedIpEntry": me1200DhcpSnoopingAssignedIpEntry,
       "me1200DhcpSnoopingAssignedIpMacAddress": me1200DhcpSnoopingAssignedIpMacAddress,
       "me1200DhcpSnoopingAssignedIpVlanId": me1200DhcpSnoopingAssignedIpVlanId,
       "me1200DhcpSnoopingAssignedIpIfIndex": me1200DhcpSnoopingAssignedIpIfIndex,
       "me1200DhcpSnoopingAssignedIpIpAddress": me1200DhcpSnoopingAssignedIpIpAddress,
       "me1200DhcpSnoopingAssignedIpNetmask": me1200DhcpSnoopingAssignedIpNetmask,
       "me1200DhcpSnoopingAssignedIpDhcpServerIp": me1200DhcpSnoopingAssignedIpDhcpServerIp,
       "me1200DhcpSnoopingInterfaceStatisticsTable": me1200DhcpSnoopingInterfaceStatisticsTable,
       "me1200DhcpSnoopingInterfaceStatisticsEntry": me1200DhcpSnoopingInterfaceStatisticsEntry,
       "me1200DhcpSnoopingInterfaceStatisticsIfIndex": me1200DhcpSnoopingInterfaceStatisticsIfIndex,
       "me1200DhcpSnoopingInterfaceStatisticsRxDiscover": me1200DhcpSnoopingInterfaceStatisticsRxDiscover,
       "me1200DhcpSnoopingInterfaceStatisticsRxOffer": me1200DhcpSnoopingInterfaceStatisticsRxOffer,
       "me1200DhcpSnoopingInterfaceStatisticsRxRequest": me1200DhcpSnoopingInterfaceStatisticsRxRequest,
       "me1200DhcpSnoopingInterfaceStatisticsRxDecline": me1200DhcpSnoopingInterfaceStatisticsRxDecline,
       "me1200DhcpSnoopingInterfaceStatisticsRxAck": me1200DhcpSnoopingInterfaceStatisticsRxAck,
       "me1200DhcpSnoopingInterfaceStatisticsRxNak": me1200DhcpSnoopingInterfaceStatisticsRxNak,
       "me1200DhcpSnoopingInterfaceStatisticsRxRelease": me1200DhcpSnoopingInterfaceStatisticsRxRelease,
       "me1200DhcpSnoopingInterfaceStatisticsRxInform": me1200DhcpSnoopingInterfaceStatisticsRxInform,
       "me1200DhcpSnoopingInterfaceStatisticsRxLeaseQuery": me1200DhcpSnoopingInterfaceStatisticsRxLeaseQuery,
       "me1200DhcpSnoopingInterfaceStatisticsRxLeaseUnassigned": me1200DhcpSnoopingInterfaceStatisticsRxLeaseUnassigned,
       "me1200DhcpSnoopingInterfaceStatisticsRxLeaseUnknown": me1200DhcpSnoopingInterfaceStatisticsRxLeaseUnknown,
       "me1200DhcpSnoopingInterfaceStatisticsRxLeaseActive": me1200DhcpSnoopingInterfaceStatisticsRxLeaseActive,
       "me1200DhcpSnoopingInterfaceStatisticsRxDiscardChksumErr": me1200DhcpSnoopingInterfaceStatisticsRxDiscardChksumErr,
       "me1200DhcpSnoopingInterfaceStatisticsRxDiscardUntrust": me1200DhcpSnoopingInterfaceStatisticsRxDiscardUntrust,
       "me1200DhcpSnoopingInterfaceStatisticsTxDiscover": me1200DhcpSnoopingInterfaceStatisticsTxDiscover,
       "me1200DhcpSnoopingInterfaceStatisticsTxOffer": me1200DhcpSnoopingInterfaceStatisticsTxOffer,
       "me1200DhcpSnoopingInterfaceStatisticsTxRequest": me1200DhcpSnoopingInterfaceStatisticsTxRequest,
       "me1200DhcpSnoopingInterfaceStatisticsTxDecline": me1200DhcpSnoopingInterfaceStatisticsTxDecline,
       "me1200DhcpSnoopingInterfaceStatisticsTxAck": me1200DhcpSnoopingInterfaceStatisticsTxAck,
       "me1200DhcpSnoopingInterfaceStatisticsTxNak": me1200DhcpSnoopingInterfaceStatisticsTxNak,
       "me1200DhcpSnoopingInterfaceStatisticsTxRelease": me1200DhcpSnoopingInterfaceStatisticsTxRelease,
       "me1200DhcpSnoopingInterfaceStatisticsTxInform": me1200DhcpSnoopingInterfaceStatisticsTxInform,
       "me1200DhcpSnoopingInterfaceStatisticsTxLeaseQuery": me1200DhcpSnoopingInterfaceStatisticsTxLeaseQuery,
       "me1200DhcpSnoopingInterfaceStatisticsTxLeaseUnassigned": me1200DhcpSnoopingInterfaceStatisticsTxLeaseUnassigned,
       "me1200DhcpSnoopingInterfaceStatisticsTxLeaseUnknown": me1200DhcpSnoopingInterfaceStatisticsTxLeaseUnknown,
       "me1200DhcpSnoopingInterfaceStatisticsTxLeaseActive": me1200DhcpSnoopingInterfaceStatisticsTxLeaseActive,
       "me1200DhcpSnoopingControl": me1200DhcpSnoopingControl,
       "me1200DhcpSnoopingInterfaceClearStatisticsTable": me1200DhcpSnoopingInterfaceClearStatisticsTable,
       "me1200DhcpSnoopingInterfaceClearStatisticsEntry": me1200DhcpSnoopingInterfaceClearStatisticsEntry,
       "me1200DhcpSnoopingInterfaceClearStatisticsIfIndex": me1200DhcpSnoopingInterfaceClearStatisticsIfIndex,
       "me1200DhcpSnoopingInterfaceClearStatisticsClear": me1200DhcpSnoopingInterfaceClearStatisticsClear,
       "me1200DhcpSnoopingMIBConformance": me1200DhcpSnoopingMIBConformance,
       "me1200DhcpSnoopingMIBCompliances": me1200DhcpSnoopingMIBCompliances,
       "me1200DhcpSnoopingMIBCompliance": me1200DhcpSnoopingMIBCompliance,
       "me1200DhcpSnoopingMIBGroups": me1200DhcpSnoopingMIBGroups,
       "me1200DhcpSnoopingGlobalsInfoGroup": me1200DhcpSnoopingGlobalsInfoGroup,
       "me1200DhcpSnoopingInterfaceInfoGroup": me1200DhcpSnoopingInterfaceInfoGroup,
       "me1200DhcpSnoopingAssignedIpTableInfoGroup": me1200DhcpSnoopingAssignedIpTableInfoGroup,
       "me1200DhcpSnoopingInterfaceStatisticsTableInfoGroup": me1200DhcpSnoopingInterfaceStatisticsTableInfoGroup,
       "me1200DhcpSnoopingInterfaceClearStatisticsTableInfoGroup": me1200DhcpSnoopingInterfaceClearStatisticsTableInfoGroup}
)
