# SNMP MIB module (RUIJIE-CAPWAP-MOBILITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-CAPWAP-MOBILITY-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 11:05:45 2025
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
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

(ruijieMgmt,) = mibBuilder.importSymbols(
    "RUIJIE-SMI",
    "ruijieMgmt")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

ruijieMobilityMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64)
)
if mibBuilder.loadTexts:
    ruijieMobilityMIB.setRevisions(
        ("2009-09-18 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieMobilityMIBObjects_ObjectIdentity = ObjectIdentity
ruijieMobilityMIBObjects = _RuijieMobilityMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1)
)
_RuijieMobility_ObjectIdentity = ObjectIdentity
ruijieMobility = _RuijieMobility_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1)
)
_RuijieMobilityEntryTable_Object = MibTable
ruijieMobilityEntryTable = _RuijieMobilityEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ruijieMobilityEntryTable.setStatus("current")
_RuijieMobilityEntry_Object = MibTableRow
ruijieMobilityEntry = _RuijieMobilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 1, 1)
)
ruijieMobilityEntry.setIndexNames(
    (0, "RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieRoamGroupId"),
)
if mibBuilder.loadTexts:
    ruijieMobilityEntry.setStatus("current")


class _RuijieRoamGroupId_Type(Integer32):
    """Custom type ruijieRoamGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_RuijieRoamGroupId_Type.__name__ = "Integer32"
_RuijieRoamGroupId_Object = MibTableColumn
ruijieRoamGroupId = _RuijieRoamGroupId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 1, 1, 1),
    _RuijieRoamGroupId_Type()
)
ruijieRoamGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRoamGroupId.setStatus("current")
_RuijieRoamGroupName_Type = DisplayString
_RuijieRoamGroupName_Object = MibTableColumn
ruijieRoamGroupName = _RuijieRoamGroupName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 1, 1, 2),
    _RuijieRoamGroupName_Type()
)
ruijieRoamGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieRoamGroupName.setStatus("current")
_RuijieRoamGroupMyAddress_Type = IpAddress
_RuijieRoamGroupMyAddress_Object = MibTableColumn
ruijieRoamGroupMyAddress = _RuijieRoamGroupMyAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 1, 1, 3),
    _RuijieRoamGroupMyAddress_Type()
)
ruijieRoamGroupMyAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRoamGroupMyAddress.setStatus("current")
_RuijieRoamGroupMcEnable_Type = Integer32
_RuijieRoamGroupMcEnable_Object = MibTableColumn
ruijieRoamGroupMcEnable = _RuijieRoamGroupMcEnable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 1, 1, 4),
    _RuijieRoamGroupMcEnable_Type()
)
ruijieRoamGroupMcEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieRoamGroupMcEnable.setStatus("current")
_RuijieRoamGroupMcAddress_Type = IpAddress
_RuijieRoamGroupMcAddress_Object = MibTableColumn
ruijieRoamGroupMcAddress = _RuijieRoamGroupMcAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 1, 1, 5),
    _RuijieRoamGroupMcAddress_Type()
)
ruijieRoamGroupMcAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieRoamGroupMcAddress.setStatus("current")


class _RuijieRoamGroupKeepaliveCount_Type(Integer32):
    """Custom type ruijieRoamGroupKeepaliveCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 30),
    )


_RuijieRoamGroupKeepaliveCount_Type.__name__ = "Integer32"
_RuijieRoamGroupKeepaliveCount_Object = MibTableColumn
ruijieRoamGroupKeepaliveCount = _RuijieRoamGroupKeepaliveCount_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 1, 1, 6),
    _RuijieRoamGroupKeepaliveCount_Type()
)
ruijieRoamGroupKeepaliveCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieRoamGroupKeepaliveCount.setStatus("current")


class _RuijieRoamGroupKeepaliveInterval_Type(Integer32):
    """Custom type ruijieRoamGroupKeepaliveInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_RuijieRoamGroupKeepaliveInterval_Type.__name__ = "Integer32"
_RuijieRoamGroupKeepaliveInterval_Object = MibTableColumn
ruijieRoamGroupKeepaliveInterval = _RuijieRoamGroupKeepaliveInterval_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 1, 1, 7),
    _RuijieRoamGroupKeepaliveInterval_Type()
)
ruijieRoamGroupKeepaliveInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieRoamGroupKeepaliveInterval.setStatus("current")
_RuijieRoamGroupIsFast_Type = Integer32
_RuijieRoamGroupIsFast_Object = MibTableColumn
ruijieRoamGroupIsFast = _RuijieRoamGroupIsFast_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 1, 1, 8),
    _RuijieRoamGroupIsFast_Type()
)
ruijieRoamGroupIsFast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieRoamGroupIsFast.setStatus("current")
_RuijieRoamGroupCreateStatus_Type = RowStatus
_RuijieRoamGroupCreateStatus_Object = MibTableColumn
ruijieRoamGroupCreateStatus = _RuijieRoamGroupCreateStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 1, 1, 9),
    _RuijieRoamGroupCreateStatus_Type()
)
ruijieRoamGroupCreateStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieRoamGroupCreateStatus.setStatus("current")
_RuijieRoamGroupMyAddressIPv6_Type = Ipv6Address
_RuijieRoamGroupMyAddressIPv6_Object = MibTableColumn
ruijieRoamGroupMyAddressIPv6 = _RuijieRoamGroupMyAddressIPv6_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 1, 1, 10),
    _RuijieRoamGroupMyAddressIPv6_Type()
)
ruijieRoamGroupMyAddressIPv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRoamGroupMyAddressIPv6.setStatus("current")
_RuijieMobilityMemberEntryTable_Object = MibTable
ruijieMobilityMemberEntryTable = _RuijieMobilityMemberEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ruijieMobilityMemberEntryTable.setStatus("current")
_RuijieMobilityMemberEntry_Object = MibTableRow
ruijieMobilityMemberEntry = _RuijieMobilityMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 2, 1)
)
ruijieMobilityMemberEntry.setIndexNames(
    (0, "RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieRoamMemberGroupId"),
    (0, "RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieRoamMemberPeerAddress"),
)
if mibBuilder.loadTexts:
    ruijieMobilityMemberEntry.setStatus("current")


class _RuijieRoamMemberGroupId_Type(Integer32):
    """Custom type ruijieRoamMemberGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_RuijieRoamMemberGroupId_Type.__name__ = "Integer32"
_RuijieRoamMemberGroupId_Object = MibTableColumn
ruijieRoamMemberGroupId = _RuijieRoamMemberGroupId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 2, 1, 1),
    _RuijieRoamMemberGroupId_Type()
)
ruijieRoamMemberGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRoamMemberGroupId.setStatus("current")
_RuijieRoamMemberPeerAddress_Type = IpAddress
_RuijieRoamMemberPeerAddress_Object = MibTableColumn
ruijieRoamMemberPeerAddress = _RuijieRoamMemberPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 2, 1, 2),
    _RuijieRoamMemberPeerAddress_Type()
)
ruijieRoamMemberPeerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRoamMemberPeerAddress.setStatus("current")


class _RuijieRoamMemberIsList_Type(Integer32):
    """Custom type ruijieRoamMemberIsList based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RuijieRoamMemberIsList_Type.__name__ = "Integer32"
_RuijieRoamMemberIsList_Object = MibTableColumn
ruijieRoamMemberIsList = _RuijieRoamMemberIsList_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 2, 1, 3),
    _RuijieRoamMemberIsList_Type()
)
ruijieRoamMemberIsList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieRoamMemberIsList.setStatus("current")


class _RuijieRoamMemberDataChannelIsOK_Type(Integer32):
    """Custom type ruijieRoamMemberDataChannelIsOK based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RuijieRoamMemberDataChannelIsOK_Type.__name__ = "Integer32"
_RuijieRoamMemberDataChannelIsOK_Object = MibTableColumn
ruijieRoamMemberDataChannelIsOK = _RuijieRoamMemberDataChannelIsOK_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 2, 1, 4),
    _RuijieRoamMemberDataChannelIsOK_Type()
)
ruijieRoamMemberDataChannelIsOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRoamMemberDataChannelIsOK.setStatus("current")
_RuijieRoamMemberDataChannelFailTimes_Type = Integer32
_RuijieRoamMemberDataChannelFailTimes_Object = MibTableColumn
ruijieRoamMemberDataChannelFailTimes = _RuijieRoamMemberDataChannelFailTimes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 2, 1, 5),
    _RuijieRoamMemberDataChannelFailTimes_Type()
)
ruijieRoamMemberDataChannelFailTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRoamMemberDataChannelFailTimes.setStatus("current")
_RuijieRoamMemberDTLSIsClient_Type = Integer32
_RuijieRoamMemberDTLSIsClient_Object = MibTableColumn
ruijieRoamMemberDTLSIsClient = _RuijieRoamMemberDTLSIsClient_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 2, 1, 6),
    _RuijieRoamMemberDTLSIsClient_Type()
)
ruijieRoamMemberDTLSIsClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRoamMemberDTLSIsClient.setStatus("current")


class _RuijieRoamMemberDTLSIsOK_Type(Integer32):
    """Custom type ruijieRoamMemberDTLSIsOK based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RuijieRoamMemberDTLSIsOK_Type.__name__ = "Integer32"
_RuijieRoamMemberDTLSIsOK_Object = MibTableColumn
ruijieRoamMemberDTLSIsOK = _RuijieRoamMemberDTLSIsOK_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 2, 1, 7),
    _RuijieRoamMemberDTLSIsOK_Type()
)
ruijieRoamMemberDTLSIsOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRoamMemberDTLSIsOK.setStatus("current")
_RuijieRoamMemberCreateStatus_Type = RowStatus
_RuijieRoamMemberCreateStatus_Object = MibTableColumn
ruijieRoamMemberCreateStatus = _RuijieRoamMemberCreateStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 2, 1, 8),
    _RuijieRoamMemberCreateStatus_Type()
)
ruijieRoamMemberCreateStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieRoamMemberCreateStatus.setStatus("current")
_RuijieAPCtrlCreatEntryTable_Object = MibTable
ruijieAPCtrlCreatEntryTable = _RuijieAPCtrlCreatEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 3)
)
if mibBuilder.loadTexts:
    ruijieAPCtrlCreatEntryTable.setStatus("current")
_RuijieAPCtrlCreatEntry_Object = MibTableRow
ruijieAPCtrlCreatEntry = _RuijieAPCtrlCreatEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 3, 1)
)
ruijieAPCtrlCreatEntry.setIndexNames(
    (0, "RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieAPName"),
)
if mibBuilder.loadTexts:
    ruijieAPCtrlCreatEntry.setStatus("current")
_RuijieAPName_Type = DisplayString
_RuijieAPName_Object = MibTableColumn
ruijieAPName = _RuijieAPName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 3, 1, 1),
    _RuijieAPName_Type()
)
ruijieAPName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieAPName.setStatus("current")


class _RuijiePriority_Type(Integer32):
    """Custom type ruijiePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_RuijiePriority_Type.__name__ = "Integer32"
_RuijiePriority_Object = MibTableColumn
ruijiePriority = _RuijiePriority_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 3, 1, 2),
    _RuijiePriority_Type()
)
ruijiePriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijiePriority.setStatus("current")
_RuijiePrimaryACIP_Type = IpAddress
_RuijiePrimaryACIP_Object = MibTableColumn
ruijiePrimaryACIP = _RuijiePrimaryACIP_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 3, 1, 3),
    _RuijiePrimaryACIP_Type()
)
ruijiePrimaryACIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijiePrimaryACIP.setStatus("current")
_RuijiePrimaryACName_Type = DisplayString
_RuijiePrimaryACName_Object = MibTableColumn
ruijiePrimaryACName = _RuijiePrimaryACName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 3, 1, 4),
    _RuijiePrimaryACName_Type()
)
ruijiePrimaryACName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijiePrimaryACName.setStatus("current")
_RuijieSecondaryACIP_Type = IpAddress
_RuijieSecondaryACIP_Object = MibTableColumn
ruijieSecondaryACIP = _RuijieSecondaryACIP_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 3, 1, 5),
    _RuijieSecondaryACIP_Type()
)
ruijieSecondaryACIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieSecondaryACIP.setStatus("current")
_RuijieSecondaryACName_Type = DisplayString
_RuijieSecondaryACName_Object = MibTableColumn
ruijieSecondaryACName = _RuijieSecondaryACName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 3, 1, 6),
    _RuijieSecondaryACName_Type()
)
ruijieSecondaryACName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieSecondaryACName.setStatus("current")
_RuijieTertiaryACIP_Type = IpAddress
_RuijieTertiaryACIP_Object = MibTableColumn
ruijieTertiaryACIP = _RuijieTertiaryACIP_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 3, 1, 7),
    _RuijieTertiaryACIP_Type()
)
ruijieTertiaryACIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieTertiaryACIP.setStatus("current")
_RuijieTertiaryACName_Type = DisplayString
_RuijieTertiaryACName_Object = MibTableColumn
ruijieTertiaryACName = _RuijieTertiaryACName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 3, 1, 8),
    _RuijieTertiaryACName_Type()
)
ruijieTertiaryACName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieTertiaryACName.setStatus("current")
_RuijieAPCtrlCreatStatus_Type = RowStatus
_RuijieAPCtrlCreatStatus_Object = MibTableColumn
ruijieAPCtrlCreatStatus = _RuijieAPCtrlCreatStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 3, 1, 9),
    _RuijieAPCtrlCreatStatus_Type()
)
ruijieAPCtrlCreatStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAPCtrlCreatStatus.setStatus("current")
_RuijieWLANCtrlCreatEntryTable_Object = MibTable
ruijieWLANCtrlCreatEntryTable = _RuijieWLANCtrlCreatEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 4)
)
if mibBuilder.loadTexts:
    ruijieWLANCtrlCreatEntryTable.setStatus("current")
_RuijieWLANCtrlCreatEntry_Object = MibTableRow
ruijieWLANCtrlCreatEntry = _RuijieWLANCtrlCreatEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 4, 1)
)
ruijieWLANCtrlCreatEntry.setIndexNames(
    (0, "RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieWLANID"),
)
if mibBuilder.loadTexts:
    ruijieWLANCtrlCreatEntry.setStatus("current")
_RuijieWLANID_Type = Integer32
_RuijieWLANID_Object = MibTableColumn
ruijieWLANID = _RuijieWLANID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 4, 1, 1),
    _RuijieWLANID_Type()
)
ruijieWLANID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieWLANID.setStatus("current")
_RuijieAnchorACIPaddr_Type = IpAddress
_RuijieAnchorACIPaddr_Object = MibTableColumn
ruijieAnchorACIPaddr = _RuijieAnchorACIPaddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 4, 1, 2),
    _RuijieAnchorACIPaddr_Type()
)
ruijieAnchorACIPaddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAnchorACIPaddr.setStatus("current")
_RuijieWLANCtrlCreatStatus_Type = RowStatus
_RuijieWLANCtrlCreatStatus_Object = MibTableColumn
ruijieWLANCtrlCreatStatus = _RuijieWLANCtrlCreatStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 4, 1, 3),
    _RuijieWLANCtrlCreatStatus_Type()
)
ruijieWLANCtrlCreatStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieWLANCtrlCreatStatus.setStatus("current")
_RuijieAnchorACIPaddrIPv6_Type = Ipv6Address
_RuijieAnchorACIPaddrIPv6_Object = MibTableColumn
ruijieAnchorACIPaddrIPv6 = _RuijieAnchorACIPaddrIPv6_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 4, 1, 4),
    _RuijieAnchorACIPaddrIPv6_Type()
)
ruijieAnchorACIPaddrIPv6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAnchorACIPaddrIPv6.setStatus("current")
_RuijieMobilityACPing_Type = IpAddress
_RuijieMobilityACPing_Object = MibScalar
ruijieMobilityACPing = _RuijieMobilityACPing_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 5),
    _RuijieMobilityACPing_Type()
)
ruijieMobilityACPing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieMobilityACPing.setStatus("current")
_RuijieGlobalHandoffRequestsReceived_Type = Integer32
_RuijieGlobalHandoffRequestsReceived_Object = MibScalar
ruijieGlobalHandoffRequestsReceived = _RuijieGlobalHandoffRequestsReceived_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 6),
    _RuijieGlobalHandoffRequestsReceived_Type()
)
ruijieGlobalHandoffRequestsReceived.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieGlobalHandoffRequestsReceived.setStatus("current")
_RuijieGlobalHandoffEndRequestsReceived_Type = Integer32
_RuijieGlobalHandoffEndRequestsReceived_Object = MibScalar
ruijieGlobalHandoffEndRequestsReceived = _RuijieGlobalHandoffEndRequestsReceived_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 7),
    _RuijieGlobalHandoffEndRequestsReceived_Type()
)
ruijieGlobalHandoffEndRequestsReceived.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieGlobalHandoffEndRequestsReceived.setStatus("current")
_RuijieGlobalStateTransitionsDisabled_Type = Integer32
_RuijieGlobalStateTransitionsDisabled_Object = MibScalar
ruijieGlobalStateTransitionsDisabled = _RuijieGlobalStateTransitionsDisabled_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 8),
    _RuijieGlobalStateTransitionsDisabled_Type()
)
ruijieGlobalStateTransitionsDisabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieGlobalStateTransitionsDisabled.setStatus("current")
_RuijieGlobalResourceUnavailable_Type = Integer32
_RuijieGlobalResourceUnavailable_Object = MibScalar
ruijieGlobalResourceUnavailable = _RuijieGlobalResourceUnavailable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 9),
    _RuijieGlobalResourceUnavailable_Type()
)
ruijieGlobalResourceUnavailable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieGlobalResourceUnavailable.setStatus("current")
_RuijieRespondeHandoffRequestIgnored_Type = Integer32
_RuijieRespondeHandoffRequestIgnored_Object = MibScalar
ruijieRespondeHandoffRequestIgnored = _RuijieRespondeHandoffRequestIgnored_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 10),
    _RuijieRespondeHandoffRequestIgnored_Type()
)
ruijieRespondeHandoffRequestIgnored.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRespondeHandoffRequestIgnored.setStatus("current")
_RuijieRespondePingPongHandoffRequestsDropped_Type = Integer32
_RuijieRespondePingPongHandoffRequestsDropped_Object = MibScalar
ruijieRespondePingPongHandoffRequestsDropped = _RuijieRespondePingPongHandoffRequestsDropped_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 11),
    _RuijieRespondePingPongHandoffRequestsDropped_Type()
)
ruijieRespondePingPongHandoffRequestsDropped.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRespondePingPongHandoffRequestsDropped.setStatus("current")
_RuijieRespondeHandoffRequestsDroped_Type = Integer32
_RuijieRespondeHandoffRequestsDroped_Object = MibScalar
ruijieRespondeHandoffRequestsDroped = _RuijieRespondeHandoffRequestsDroped_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 12),
    _RuijieRespondeHandoffRequestsDroped_Type()
)
ruijieRespondeHandoffRequestsDroped.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRespondeHandoffRequestsDroped.setStatus("current")
_RuijieRespondeHandoffRequestsDenied_Type = Integer32
_RuijieRespondeHandoffRequestsDenied_Object = MibScalar
ruijieRespondeHandoffRequestsDenied = _RuijieRespondeHandoffRequestsDenied_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 13),
    _RuijieRespondeHandoffRequestsDenied_Type()
)
ruijieRespondeHandoffRequestsDenied.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRespondeHandoffRequestsDenied.setStatus("current")
_RuijieRespondeClientHandoffasLocal_Type = Integer32
_RuijieRespondeClientHandoffasLocal_Object = MibScalar
ruijieRespondeClientHandoffasLocal = _RuijieRespondeClientHandoffasLocal_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 14),
    _RuijieRespondeClientHandoffasLocal_Type()
)
ruijieRespondeClientHandoffasLocal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRespondeClientHandoffasLocal.setStatus("current")
_RuijieRespondeClientHandoffasForeign_Type = Integer32
_RuijieRespondeClientHandoffasForeign_Object = MibScalar
ruijieRespondeClientHandoffasForeign = _RuijieRespondeClientHandoffasForeign_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 15),
    _RuijieRespondeClientHandoffasForeign_Type()
)
ruijieRespondeClientHandoffasForeign.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRespondeClientHandoffasForeign.setStatus("current")
_RuijieRespondeAnchorRequestsReceived_Type = Integer32
_RuijieRespondeAnchorRequestsReceived_Object = MibScalar
ruijieRespondeAnchorRequestsReceived = _RuijieRespondeAnchorRequestsReceived_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 16),
    _RuijieRespondeAnchorRequestsReceived_Type()
)
ruijieRespondeAnchorRequestsReceived.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRespondeAnchorRequestsReceived.setStatus("current")
_RuijieRespondeAnchorRequestDenied_Type = Integer32
_RuijieRespondeAnchorRequestDenied_Object = MibScalar
ruijieRespondeAnchorRequestDenied = _RuijieRespondeAnchorRequestDenied_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 17),
    _RuijieRespondeAnchorRequestDenied_Type()
)
ruijieRespondeAnchorRequestDenied.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRespondeAnchorRequestDenied.setStatus("current")
_RuijieRespondeAnchorTransferred_Type = Integer32
_RuijieRespondeAnchorTransferred_Object = MibScalar
ruijieRespondeAnchorTransferred = _RuijieRespondeAnchorTransferred_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 18),
    _RuijieRespondeAnchorTransferred_Type()
)
ruijieRespondeAnchorTransferred.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRespondeAnchorTransferred.setStatus("current")
_RuijieInitHandoffRequestsSent_Type = Integer32
_RuijieInitHandoffRequestsSent_Object = MibScalar
ruijieInitHandoffRequestsSent = _RuijieInitHandoffRequestsSent_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 19),
    _RuijieInitHandoffRequestsSent_Type()
)
ruijieInitHandoffRequestsSent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieInitHandoffRequestsSent.setStatus("current")
_RuijieInitHandoffReplyReceived_Type = Integer32
_RuijieInitHandoffReplyReceived_Object = MibScalar
ruijieInitHandoffReplyReceived = _RuijieInitHandoffReplyReceived_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 20),
    _RuijieInitHandoffReplyReceived_Type()
)
ruijieInitHandoffReplyReceived.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieInitHandoffReplyReceived.setStatus("current")
_RuijieInitHandoffasLocalReceived_Type = Integer32
_RuijieInitHandoffasLocalReceived_Object = MibScalar
ruijieInitHandoffasLocalReceived = _RuijieInitHandoffasLocalReceived_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 21),
    _RuijieInitHandoffasLocalReceived_Type()
)
ruijieInitHandoffasLocalReceived.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieInitHandoffasLocalReceived.setStatus("current")
_RuijieInitHandoffasForeignReceived_Type = Integer32
_RuijieInitHandoffasForeignReceived_Object = MibScalar
ruijieInitHandoffasForeignReceived = _RuijieInitHandoffasForeignReceived_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 22),
    _RuijieInitHandoffasForeignReceived_Type()
)
ruijieInitHandoffasForeignReceived.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieInitHandoffasForeignReceived.setStatus("current")
_RuijieInitHandoffDenyReceived_Type = Integer32
_RuijieInitHandoffDenyReceived_Object = MibScalar
ruijieInitHandoffDenyReceived = _RuijieInitHandoffDenyReceived_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 23),
    _RuijieInitHandoffDenyReceived_Type()
)
ruijieInitHandoffDenyReceived.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieInitHandoffDenyReceived.setStatus("current")
_RuijieInitAnchorRequestSent_Type = Integer32
_RuijieInitAnchorRequestSent_Object = MibScalar
ruijieInitAnchorRequestSent = _RuijieInitAnchorRequestSent_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 24),
    _RuijieInitAnchorRequestSent_Type()
)
ruijieInitAnchorRequestSent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieInitAnchorRequestSent.setStatus("current")
_RuijieInitAnchorDenyReceived_Type = Integer32
_RuijieInitAnchorDenyReceived_Object = MibScalar
ruijieInitAnchorDenyReceived = _RuijieInitAnchorDenyReceived_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 25),
    _RuijieInitAnchorDenyReceived_Type()
)
ruijieInitAnchorDenyReceived.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieInitAnchorDenyReceived.setStatus("current")
_RuijieAPPriorityEnable_Type = Integer32
_RuijieAPPriorityEnable_Object = MibScalar
ruijieAPPriorityEnable = _RuijieAPPriorityEnable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 26),
    _RuijieAPPriorityEnable_Type()
)
ruijieAPPriorityEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAPPriorityEnable.setStatus("current")
_RuijiePrimaryBackUpACIP_Type = IpAddress
_RuijiePrimaryBackUpACIP_Object = MibScalar
ruijiePrimaryBackUpACIP = _RuijiePrimaryBackUpACIP_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 27),
    _RuijiePrimaryBackUpACIP_Type()
)
ruijiePrimaryBackUpACIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijiePrimaryBackUpACIP.setStatus("current")
_RuijiePrimaryBackUpACName_Type = DisplayString
_RuijiePrimaryBackUpACName_Object = MibScalar
ruijiePrimaryBackUpACName = _RuijiePrimaryBackUpACName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 28),
    _RuijiePrimaryBackUpACName_Type()
)
ruijiePrimaryBackUpACName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijiePrimaryBackUpACName.setStatus("current")
_RuijieSecondaryBackUpACIP_Type = IpAddress
_RuijieSecondaryBackUpACIP_Object = MibScalar
ruijieSecondaryBackUpACIP = _RuijieSecondaryBackUpACIP_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 29),
    _RuijieSecondaryBackUpACIP_Type()
)
ruijieSecondaryBackUpACIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieSecondaryBackUpACIP.setStatus("current")
_RuijieSecondaryBackUpACName_Type = DisplayString
_RuijieSecondaryBackUpACName_Object = MibScalar
ruijieSecondaryBackUpACName = _RuijieSecondaryBackUpACName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 30),
    _RuijieSecondaryBackUpACName_Type()
)
ruijieSecondaryBackUpACName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieSecondaryBackUpACName.setStatus("current")
_RuijieTeriaryBackUpACip_Type = IpAddress
_RuijieTeriaryBackUpACip_Object = MibScalar
ruijieTeriaryBackUpACip = _RuijieTeriaryBackUpACip_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 31),
    _RuijieTeriaryBackUpACip_Type()
)
ruijieTeriaryBackUpACip.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieTeriaryBackUpACip.setStatus("current")
_RuijieTeriaryBackUpACName_Type = DisplayString
_RuijieTeriaryBackUpACName_Object = MibScalar
ruijieTeriaryBackUpACName = _RuijieTeriaryBackUpACName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 32),
    _RuijieTeriaryBackUpACName_Type()
)
ruijieTeriaryBackUpACName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieTeriaryBackUpACName.setStatus("current")
_RuijieACIntraRoam_Type = Counter32
_RuijieACIntraRoam_Object = MibScalar
ruijieACIntraRoam = _RuijieACIntraRoam_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 33),
    _RuijieACIntraRoam_Type()
)
ruijieACIntraRoam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieACIntraRoam.setStatus("current")
_RuijieACInterRoamIn_Type = Counter32
_RuijieACInterRoamIn_Object = MibScalar
ruijieACInterRoamIn = _RuijieACInterRoamIn_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 34),
    _RuijieACInterRoamIn_Type()
)
ruijieACInterRoamIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieACInterRoamIn.setStatus("current")
_RuijieACInterRoamOut_Type = Counter32
_RuijieACInterRoamOut_Object = MibScalar
ruijieACInterRoamOut = _RuijieACInterRoamOut_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 35),
    _RuijieACInterRoamOut_Type()
)
ruijieACInterRoamOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieACInterRoamOut.setStatus("current")
_RuijieMobilityACPingIPv6_Type = Ipv6Address
_RuijieMobilityACPingIPv6_Object = MibScalar
ruijieMobilityACPingIPv6 = _RuijieMobilityACPingIPv6_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 36),
    _RuijieMobilityACPingIPv6_Type()
)
ruijieMobilityACPingIPv6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieMobilityACPingIPv6.setStatus("current")
_RuijieMobilityIPv6MemberEntryTable_Object = MibTable
ruijieMobilityIPv6MemberEntryTable = _RuijieMobilityIPv6MemberEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 37)
)
if mibBuilder.loadTexts:
    ruijieMobilityIPv6MemberEntryTable.setStatus("current")
_RuijieMobilityIPv6MemberEntry_Object = MibTableRow
ruijieMobilityIPv6MemberEntry = _RuijieMobilityIPv6MemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 37, 1)
)
ruijieMobilityIPv6MemberEntry.setIndexNames(
    (0, "RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieRoamIPv6MemberGroupId"),
    (0, "RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieRoamIPv6MemberPeerAddress"),
)
if mibBuilder.loadTexts:
    ruijieMobilityIPv6MemberEntry.setStatus("current")


class _RuijieRoamIPv6MemberGroupId_Type(Integer32):
    """Custom type ruijieRoamIPv6MemberGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_RuijieRoamIPv6MemberGroupId_Type.__name__ = "Integer32"
_RuijieRoamIPv6MemberGroupId_Object = MibTableColumn
ruijieRoamIPv6MemberGroupId = _RuijieRoamIPv6MemberGroupId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 37, 1, 1),
    _RuijieRoamIPv6MemberGroupId_Type()
)
ruijieRoamIPv6MemberGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRoamIPv6MemberGroupId.setStatus("current")
_RuijieRoamIPv6MemberPeerAddress_Type = Ipv6Address
_RuijieRoamIPv6MemberPeerAddress_Object = MibTableColumn
ruijieRoamIPv6MemberPeerAddress = _RuijieRoamIPv6MemberPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 37, 1, 2),
    _RuijieRoamIPv6MemberPeerAddress_Type()
)
ruijieRoamIPv6MemberPeerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRoamIPv6MemberPeerAddress.setStatus("current")


class _RuijieRoamIPv6MemberIsList_Type(Integer32):
    """Custom type ruijieRoamIPv6MemberIsList based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RuijieRoamIPv6MemberIsList_Type.__name__ = "Integer32"
_RuijieRoamIPv6MemberIsList_Object = MibTableColumn
ruijieRoamIPv6MemberIsList = _RuijieRoamIPv6MemberIsList_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 37, 1, 3),
    _RuijieRoamIPv6MemberIsList_Type()
)
ruijieRoamIPv6MemberIsList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieRoamIPv6MemberIsList.setStatus("current")


class _RuijieRoamIPv6MemberDataChannelIsOK_Type(Integer32):
    """Custom type ruijieRoamIPv6MemberDataChannelIsOK based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RuijieRoamIPv6MemberDataChannelIsOK_Type.__name__ = "Integer32"
_RuijieRoamIPv6MemberDataChannelIsOK_Object = MibTableColumn
ruijieRoamIPv6MemberDataChannelIsOK = _RuijieRoamIPv6MemberDataChannelIsOK_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 37, 1, 4),
    _RuijieRoamIPv6MemberDataChannelIsOK_Type()
)
ruijieRoamIPv6MemberDataChannelIsOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRoamIPv6MemberDataChannelIsOK.setStatus("current")
_RuijieRoamIPv6MemberDataChannelFailTimes_Type = Integer32
_RuijieRoamIPv6MemberDataChannelFailTimes_Object = MibTableColumn
ruijieRoamIPv6MemberDataChannelFailTimes = _RuijieRoamIPv6MemberDataChannelFailTimes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 37, 1, 5),
    _RuijieRoamIPv6MemberDataChannelFailTimes_Type()
)
ruijieRoamIPv6MemberDataChannelFailTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRoamIPv6MemberDataChannelFailTimes.setStatus("current")
_RuijieRoamIPv6MemberDTLSIsClient_Type = Integer32
_RuijieRoamIPv6MemberDTLSIsClient_Object = MibTableColumn
ruijieRoamIPv6MemberDTLSIsClient = _RuijieRoamIPv6MemberDTLSIsClient_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 37, 1, 6),
    _RuijieRoamIPv6MemberDTLSIsClient_Type()
)
ruijieRoamIPv6MemberDTLSIsClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRoamIPv6MemberDTLSIsClient.setStatus("current")


class _RuijieRoamIPv6MemberDTLSIsOK_Type(Integer32):
    """Custom type ruijieRoamIPv6MemberDTLSIsOK based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RuijieRoamIPv6MemberDTLSIsOK_Type.__name__ = "Integer32"
_RuijieRoamIPv6MemberDTLSIsOK_Object = MibTableColumn
ruijieRoamIPv6MemberDTLSIsOK = _RuijieRoamIPv6MemberDTLSIsOK_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 37, 1, 7),
    _RuijieRoamIPv6MemberDTLSIsOK_Type()
)
ruijieRoamIPv6MemberDTLSIsOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRoamIPv6MemberDTLSIsOK.setStatus("current")
_RuijieRoamIPv6MemberCreateStatus_Type = RowStatus
_RuijieRoamIPv6MemberCreateStatus_Object = MibTableColumn
ruijieRoamIPv6MemberCreateStatus = _RuijieRoamIPv6MemberCreateStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 37, 1, 8),
    _RuijieRoamIPv6MemberCreateStatus_Type()
)
ruijieRoamIPv6MemberCreateStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieRoamIPv6MemberCreateStatus.setStatus("current")
_RuijieMobilityUserEntryTable_Object = MibTable
ruijieMobilityUserEntryTable = _RuijieMobilityUserEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 38)
)
if mibBuilder.loadTexts:
    ruijieMobilityUserEntryTable.setStatus("current")
_RuijieMobilityUserEntry_Object = MibTableRow
ruijieMobilityUserEntry = _RuijieMobilityUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 38, 1)
)
ruijieMobilityUserEntry.setIndexNames(
    (0, "RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieRoamUserMac"),
)
if mibBuilder.loadTexts:
    ruijieMobilityUserEntry.setStatus("current")
_RuijieRoamUserMac_Type = MacAddress
_RuijieRoamUserMac_Object = MibTableColumn
ruijieRoamUserMac = _RuijieRoamUserMac_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 38, 1, 1),
    _RuijieRoamUserMac_Type()
)
ruijieRoamUserMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRoamUserMac.setStatus("current")
_RuijieRoamUserRoamType_Type = Integer32
_RuijieRoamUserRoamType_Object = MibTableColumn
ruijieRoamUserRoamType = _RuijieRoamUserRoamType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 38, 1, 2),
    _RuijieRoamUserRoamType_Type()
)
ruijieRoamUserRoamType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRoamUserRoamType.setStatus("current")
_RuijieRoamUserRoamOutAcAddressType_Type = InetAddressType
_RuijieRoamUserRoamOutAcAddressType_Object = MibTableColumn
ruijieRoamUserRoamOutAcAddressType = _RuijieRoamUserRoamOutAcAddressType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 38, 1, 3),
    _RuijieRoamUserRoamOutAcAddressType_Type()
)
ruijieRoamUserRoamOutAcAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRoamUserRoamOutAcAddressType.setStatus("current")
_RuijieRoamUserRoamOutAcAddress_Type = InetAddress
_RuijieRoamUserRoamOutAcAddress_Object = MibTableColumn
ruijieRoamUserRoamOutAcAddress = _RuijieRoamUserRoamOutAcAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 38, 1, 4),
    _RuijieRoamUserRoamOutAcAddress_Type()
)
ruijieRoamUserRoamOutAcAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRoamUserRoamOutAcAddress.setStatus("current")
_RuijieRoamUserRoamInAcAddressType_Type = InetAddressType
_RuijieRoamUserRoamInAcAddressType_Object = MibTableColumn
ruijieRoamUserRoamInAcAddressType = _RuijieRoamUserRoamInAcAddressType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 38, 1, 5),
    _RuijieRoamUserRoamInAcAddressType_Type()
)
ruijieRoamUserRoamInAcAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRoamUserRoamInAcAddressType.setStatus("current")
_RuijieRoamUserRoamInAcAddress_Type = InetAddress
_RuijieRoamUserRoamInAcAddress_Object = MibTableColumn
ruijieRoamUserRoamInAcAddress = _RuijieRoamUserRoamInAcAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 38, 1, 6),
    _RuijieRoamUserRoamInAcAddress_Type()
)
ruijieRoamUserRoamInAcAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRoamUserRoamInAcAddress.setStatus("current")
_RuijieRoamUserRoamOutApMac_Type = MacAddress
_RuijieRoamUserRoamOutApMac_Object = MibTableColumn
ruijieRoamUserRoamOutApMac = _RuijieRoamUserRoamOutApMac_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 38, 1, 7),
    _RuijieRoamUserRoamOutApMac_Type()
)
ruijieRoamUserRoamOutApMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRoamUserRoamOutApMac.setStatus("current")
_RuijieRoamUserRoamInApMac_Type = MacAddress
_RuijieRoamUserRoamInApMac_Object = MibTableColumn
ruijieRoamUserRoamInApMac = _RuijieRoamUserRoamInApMac_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 38, 1, 8),
    _RuijieRoamUserRoamInApMac_Type()
)
ruijieRoamUserRoamInApMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRoamUserRoamInApMac.setStatus("current")
_RuijieRoamUserRoamOutVid_Type = Integer32
_RuijieRoamUserRoamOutVid_Object = MibTableColumn
ruijieRoamUserRoamOutVid = _RuijieRoamUserRoamOutVid_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 38, 1, 9),
    _RuijieRoamUserRoamOutVid_Type()
)
ruijieRoamUserRoamOutVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRoamUserRoamOutVid.setStatus("current")
_RuijieRoamUserRoamInVid_Type = Integer32
_RuijieRoamUserRoamInVid_Object = MibTableColumn
ruijieRoamUserRoamInVid = _RuijieRoamUserRoamInVid_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 38, 1, 10),
    _RuijieRoamUserRoamInVid_Type()
)
ruijieRoamUserRoamInVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRoamUserRoamInVid.setStatus("current")
_RuijieMobilityTrackEntryTable_Object = MibTable
ruijieMobilityTrackEntryTable = _RuijieMobilityTrackEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 39)
)
if mibBuilder.loadTexts:
    ruijieMobilityTrackEntryTable.setStatus("current")
_RuijieMobilityTrackEntry_Object = MibTableRow
ruijieMobilityTrackEntry = _RuijieMobilityTrackEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 39, 1)
)
ruijieMobilityTrackEntry.setIndexNames(
    (0, "RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieRoamTrackStaMac"),
    (0, "RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieRoamTrackId"),
)
if mibBuilder.loadTexts:
    ruijieMobilityTrackEntry.setStatus("current")
_RuijieRoamTrackStaMac_Type = MacAddress
_RuijieRoamTrackStaMac_Object = MibTableColumn
ruijieRoamTrackStaMac = _RuijieRoamTrackStaMac_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 39, 1, 1),
    _RuijieRoamTrackStaMac_Type()
)
ruijieRoamTrackStaMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRoamTrackStaMac.setStatus("current")
_RuijieRoamTrackId_Type = Integer32
_RuijieRoamTrackId_Object = MibTableColumn
ruijieRoamTrackId = _RuijieRoamTrackId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 39, 1, 2),
    _RuijieRoamTrackId_Type()
)
ruijieRoamTrackId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRoamTrackId.setStatus("current")
_RuijieRoamTrackAcAddressType_Type = InetAddressType
_RuijieRoamTrackAcAddressType_Object = MibTableColumn
ruijieRoamTrackAcAddressType = _RuijieRoamTrackAcAddressType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 39, 1, 3),
    _RuijieRoamTrackAcAddressType_Type()
)
ruijieRoamTrackAcAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRoamTrackAcAddressType.setStatus("current")
_RuijieRoamTrackAcAddress_Type = InetAddress
_RuijieRoamTrackAcAddress_Object = MibTableColumn
ruijieRoamTrackAcAddress = _RuijieRoamTrackAcAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 39, 1, 4),
    _RuijieRoamTrackAcAddress_Type()
)
ruijieRoamTrackAcAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRoamTrackAcAddress.setStatus("current")
_RuijieRoamTrackApMac_Type = MacAddress
_RuijieRoamTrackApMac_Object = MibTableColumn
ruijieRoamTrackApMac = _RuijieRoamTrackApMac_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 39, 1, 5),
    _RuijieRoamTrackApMac_Type()
)
ruijieRoamTrackApMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRoamTrackApMac.setStatus("current")
_RuijieRoamTrackRadioId_Type = Integer32
_RuijieRoamTrackRadioId_Object = MibTableColumn
ruijieRoamTrackRadioId = _RuijieRoamTrackRadioId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 39, 1, 6),
    _RuijieRoamTrackRadioId_Type()
)
ruijieRoamTrackRadioId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRoamTrackRadioId.setStatus("current")
_RuijieRoamTrackStaIp_Type = IpAddress
_RuijieRoamTrackStaIp_Object = MibTableColumn
ruijieRoamTrackStaIp = _RuijieRoamTrackStaIp_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 39, 1, 7),
    _RuijieRoamTrackStaIp_Type()
)
ruijieRoamTrackStaIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRoamTrackStaIp.setStatus("current")
_RuijieRoamTrackStaIpv6_Type = Ipv6Address
_RuijieRoamTrackStaIpv6_Object = MibTableColumn
ruijieRoamTrackStaIpv6 = _RuijieRoamTrackStaIpv6_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 39, 1, 8),
    _RuijieRoamTrackStaIpv6_Type()
)
ruijieRoamTrackStaIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRoamTrackStaIpv6.setStatus("current")
_RuijieRoamTrackStaOnlineTime_Type = Integer32
_RuijieRoamTrackStaOnlineTime_Object = MibTableColumn
ruijieRoamTrackStaOnlineTime = _RuijieRoamTrackStaOnlineTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 39, 1, 9),
    _RuijieRoamTrackStaOnlineTime_Type()
)
ruijieRoamTrackStaOnlineTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRoamTrackStaOnlineTime.setStatus("current")
_RuijieMobilityUserJsonTable_Object = MibTable
ruijieMobilityUserJsonTable = _RuijieMobilityUserJsonTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 40)
)
if mibBuilder.loadTexts:
    ruijieMobilityUserJsonTable.setStatus("current")
_RuijieMobilityUserJsonEntry_Object = MibTableRow
ruijieMobilityUserJsonEntry = _RuijieMobilityUserJsonEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 40, 1)
)
ruijieMobilityUserJsonEntry.setIndexNames(
    (0, "RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieMobilityUserJsonMacAddr"),
)
if mibBuilder.loadTexts:
    ruijieMobilityUserJsonEntry.setStatus("current")
_RuijieMobilityUserJsonMacAddr_Type = MacAddress
_RuijieMobilityUserJsonMacAddr_Object = MibTableColumn
ruijieMobilityUserJsonMacAddr = _RuijieMobilityUserJsonMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 40, 1, 1),
    _RuijieMobilityUserJsonMacAddr_Type()
)
ruijieMobilityUserJsonMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMobilityUserJsonMacAddr.setStatus("current")


class _RuijieMobilityUserJsonContent_Type(OctetString):
    """Custom type ruijieMobilityUserJsonContent based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1023),
    )


_RuijieMobilityUserJsonContent_Type.__name__ = "OctetString"
_RuijieMobilityUserJsonContent_Object = MibTableColumn
ruijieMobilityUserJsonContent = _RuijieMobilityUserJsonContent_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 1, 40, 1, 2),
    _RuijieMobilityUserJsonContent_Type()
)
ruijieMobilityUserJsonContent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMobilityUserJsonContent.setStatus("current")
_RuijieMobilityIf_ObjectIdentity = ObjectIdentity
ruijieMobilityIf = _RuijieMobilityIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 2)
)
_RuijieMobilityMIBCompliances_ObjectIdentity = ObjectIdentity
ruijieMobilityMIBCompliances = _RuijieMobilityMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 2, 1)
)
_RuijieMobilityMIBGroups_ObjectIdentity = ObjectIdentity
ruijieMobilityMIBGroups = _RuijieMobilityMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 2, 2)
)
_RuijieMobilityTrap_ObjectIdentity = ObjectIdentity
ruijieMobilityTrap = _RuijieMobilityTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 3)
)
_RuijieMobilityTrapSta_ObjectIdentity = ObjectIdentity
ruijieMobilityTrapSta = _RuijieMobilityTrapSta_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 3, 1)
)
_RuijieMobilityNotifyApMac_Type = MacAddress
_RuijieMobilityNotifyApMac_Object = MibScalar
ruijieMobilityNotifyApMac = _RuijieMobilityNotifyApMac_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 3, 1, 1),
    _RuijieMobilityNotifyApMac_Type()
)
ruijieMobilityNotifyApMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieMobilityNotifyApMac.setStatus("current")
_RuijieMobilityNotifyStaMac_Type = MacAddress
_RuijieMobilityNotifyStaMac_Object = MibScalar
ruijieMobilityNotifyStaMac = _RuijieMobilityNotifyStaMac_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 3, 1, 2),
    _RuijieMobilityNotifyStaMac_Type()
)
ruijieMobilityNotifyStaMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieMobilityNotifyStaMac.setStatus("current")
_RuijieMobilityNotifyApIp_Type = IpAddress
_RuijieMobilityNotifyApIp_Object = MibScalar
ruijieMobilityNotifyApIp = _RuijieMobilityNotifyApIp_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 3, 1, 3),
    _RuijieMobilityNotifyApIp_Type()
)
ruijieMobilityNotifyApIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieMobilityNotifyApIp.setStatus("current")
_RuijieMobilityNotifyStaIp_Type = IpAddress
_RuijieMobilityNotifyStaIp_Object = MibScalar
ruijieMobilityNotifyStaIp = _RuijieMobilityNotifyStaIp_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 3, 1, 4),
    _RuijieMobilityNotifyStaIp_Type()
)
ruijieMobilityNotifyStaIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieMobilityNotifyStaIp.setStatus("current")
_RuijieMobilityNotifyStaOperType_Type = Integer32
_RuijieMobilityNotifyStaOperType_Object = MibScalar
ruijieMobilityNotifyStaOperType = _RuijieMobilityNotifyStaOperType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 3, 1, 5),
    _RuijieMobilityNotifyStaOperType_Type()
)
ruijieMobilityNotifyStaOperType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieMobilityNotifyStaOperType.setStatus("current")


class _RuijieMobilityNotifyStaApRadioId_Type(Integer32):
    """Custom type ruijieMobilityNotifyStaApRadioId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_RuijieMobilityNotifyStaApRadioId_Type.__name__ = "Integer32"
_RuijieMobilityNotifyStaApRadioId_Object = MibScalar
ruijieMobilityNotifyStaApRadioId = _RuijieMobilityNotifyStaApRadioId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 3, 1, 6),
    _RuijieMobilityNotifyStaApRadioId_Type()
)
ruijieMobilityNotifyStaApRadioId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieMobilityNotifyStaApRadioId.setStatus("current")


class _RuijieMobilityNotifyStaApRadioType_Type(Integer32):
    """Custom type ruijieMobilityNotifyStaApRadioType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_RuijieMobilityNotifyStaApRadioType_Type.__name__ = "Integer32"
_RuijieMobilityNotifyStaApRadioType_Object = MibScalar
ruijieMobilityNotifyStaApRadioType = _RuijieMobilityNotifyStaApRadioType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 3, 1, 7),
    _RuijieMobilityNotifyStaApRadioType_Type()
)
ruijieMobilityNotifyStaApRadioType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieMobilityNotifyStaApRadioType.setStatus("current")


class _RuijieMobilityNotifyStaVlanId_Type(Integer32):
    """Custom type ruijieMobilityNotifyStaVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_RuijieMobilityNotifyStaVlanId_Type.__name__ = "Integer32"
_RuijieMobilityNotifyStaVlanId_Object = MibScalar
ruijieMobilityNotifyStaVlanId = _RuijieMobilityNotifyStaVlanId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 3, 1, 8),
    _RuijieMobilityNotifyStaVlanId_Type()
)
ruijieMobilityNotifyStaVlanId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieMobilityNotifyStaVlanId.setStatus("current")


class _RuijieMobilityNotifyStaWlanId_Type(Integer32):
    """Custom type ruijieMobilityNotifyStaWlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_RuijieMobilityNotifyStaWlanId_Type.__name__ = "Integer32"
_RuijieMobilityNotifyStaWlanId_Object = MibScalar
ruijieMobilityNotifyStaWlanId = _RuijieMobilityNotifyStaWlanId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 3, 1, 9),
    _RuijieMobilityNotifyStaWlanId_Type()
)
ruijieMobilityNotifyStaWlanId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieMobilityNotifyStaWlanId.setStatus("current")
_RuijieMobilityNotifyStaIpv6_Type = Ipv6Address
_RuijieMobilityNotifyStaIpv6_Object = MibScalar
ruijieMobilityNotifyStaIpv6 = _RuijieMobilityNotifyStaIpv6_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 3, 1, 10),
    _RuijieMobilityNotifyStaIpv6_Type()
)
ruijieMobilityNotifyStaIpv6.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieMobilityNotifyStaIpv6.setStatus("current")


class _RuijieMobilityNotifyStaAssoAuthMode_Type(Integer32):
    """Custom type ruijieMobilityNotifyStaAssoAuthMode based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("open", 0),
          ("wep", 1),
          ("dot1x-wep", 2),
          ("dot1x-wpa", 3),
          ("dot1x-wpa2", 4),
          ("mab", 5),
          ("psk-wpa", 6),
          ("psk-wpa2", 7),
          ("wapi", 8))
    )


_RuijieMobilityNotifyStaAssoAuthMode_Type.__name__ = "Integer32"
_RuijieMobilityNotifyStaAssoAuthMode_Object = MibScalar
ruijieMobilityNotifyStaAssoAuthMode = _RuijieMobilityNotifyStaAssoAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 3, 1, 11),
    _RuijieMobilityNotifyStaAssoAuthMode_Type()
)
ruijieMobilityNotifyStaAssoAuthMode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieMobilityNotifyStaAssoAuthMode.setStatus("current")


class _RuijieMobilityNotifyStaNetAuthMode_Type(Integer32):
    """Custom type ruijieMobilityNotifyStaNetAuthMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("open", 0),
          ("web", 1))
    )


_RuijieMobilityNotifyStaNetAuthMode_Type.__name__ = "Integer32"
_RuijieMobilityNotifyStaNetAuthMode_Object = MibScalar
ruijieMobilityNotifyStaNetAuthMode = _RuijieMobilityNotifyStaNetAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 3, 1, 12),
    _RuijieMobilityNotifyStaNetAuthMode_Type()
)
ruijieMobilityNotifyStaNetAuthMode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieMobilityNotifyStaNetAuthMode.setStatus("current")
_RuijieMobilityNotifyStaSsid_Type = DisplayString
_RuijieMobilityNotifyStaSsid_Object = MibScalar
ruijieMobilityNotifyStaSsid = _RuijieMobilityNotifyStaSsid_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 3, 1, 13),
    _RuijieMobilityNotifyStaSsid_Type()
)
ruijieMobilityNotifyStaSsid.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieMobilityNotifyStaSsid.setStatus("current")
_RuijieMobilityNotifyStaLinkRate_Type = Integer32
_RuijieMobilityNotifyStaLinkRate_Object = MibScalar
ruijieMobilityNotifyStaLinkRate = _RuijieMobilityNotifyStaLinkRate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 3, 1, 14),
    _RuijieMobilityNotifyStaLinkRate_Type()
)
ruijieMobilityNotifyStaLinkRate.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieMobilityNotifyStaLinkRate.setStatus("current")
_RuijieMobilityNotifyStaCurChan_Type = Integer32
_RuijieMobilityNotifyStaCurChan_Object = MibScalar
ruijieMobilityNotifyStaCurChan = _RuijieMobilityNotifyStaCurChan_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 3, 1, 15),
    _RuijieMobilityNotifyStaCurChan_Type()
)
ruijieMobilityNotifyStaCurChan.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieMobilityNotifyStaCurChan.setStatus("current")
_RuijieMobilityNotifyStaClientType_Type = DisplayString
_RuijieMobilityNotifyStaClientType_Object = MibScalar
ruijieMobilityNotifyStaClientType = _RuijieMobilityNotifyStaClientType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 3, 1, 16),
    _RuijieMobilityNotifyStaClientType_Type()
)
ruijieMobilityNotifyStaClientType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieMobilityNotifyStaClientType.setStatus("current")
_RuijieMobilityNotifyStaRssi_Type = Integer32
_RuijieMobilityNotifyStaRssi_Object = MibScalar
ruijieMobilityNotifyStaRssi = _RuijieMobilityNotifyStaRssi_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 3, 1, 17),
    _RuijieMobilityNotifyStaRssi_Type()
)
ruijieMobilityNotifyStaRssi.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieMobilityNotifyStaRssi.setStatus("current")
_RuijieMobilityNotifyStaReason_Type = DisplayString
_RuijieMobilityNotifyStaReason_Object = MibScalar
ruijieMobilityNotifyStaReason = _RuijieMobilityNotifyStaReason_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 3, 1, 18),
    _RuijieMobilityNotifyStaReason_Type()
)
ruijieMobilityNotifyStaReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieMobilityNotifyStaReason.setStatus("current")
_RuijieMobilityTrapStaIf_ObjectIdentity = ObjectIdentity
ruijieMobilityTrapStaIf = _RuijieMobilityTrapStaIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 3, 2)
)

# Managed Objects groups

ruijieMobilityMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 2, 2, 1)
)
ruijieMobilityMIBGroup.setObjects(
      *(("RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieRoamGroupName"),
        ("RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieRoamGroupMyAddress"),
        ("RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieRoamGroupMcEnable"),
        ("RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieRoamGroupMcAddress"),
        ("RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieRoamGroupKeepaliveCount"),
        ("RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieRoamGroupKeepaliveInterval"),
        ("RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieRoamGroupIsFast"),
        ("RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieRoamGroupCreateStatus"),
        ("RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieRoamMemberIsList"),
        ("RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieRoamMemberDataChannelIsOK"),
        ("RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieRoamMemberDataChannelFailTimes"),
        ("RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieRoamMemberDTLSIsClient"),
        ("RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieRoamMemberDTLSIsOK"),
        ("RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieRoamMemberCreateStatus"),
        ("RUIJIE-CAPWAP-MOBILITY-MIB", "ruijiePriority"),
        ("RUIJIE-CAPWAP-MOBILITY-MIB", "ruijiePrimaryACIP"),
        ("RUIJIE-CAPWAP-MOBILITY-MIB", "ruijiePrimaryACName"),
        ("RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieSecondaryACIP"),
        ("RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieSecondaryACName"),
        ("RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieTertiaryACIP"),
        ("RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieTertiaryACName"),
        ("RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieAPCtrlCreatStatus"),
        ("RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieAnchorACIPaddr"),
        ("RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieWLANCtrlCreatStatus"),
        ("RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieGlobalHandoffRequestsReceived"),
        ("RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieGlobalHandoffEndRequestsReceived"),
        ("RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieGlobalStateTransitionsDisabled"),
        ("RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieGlobalResourceUnavailable"),
        ("RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieRespondeHandoffRequestIgnored"),
        ("RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieRespondePingPongHandoffRequestsDropped"),
        ("RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieRespondeHandoffRequestsDroped"),
        ("RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieRespondeHandoffRequestsDenied"),
        ("RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieRespondeClientHandoffasLocal"),
        ("RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieRespondeClientHandoffasForeign"),
        ("RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieRespondeAnchorRequestsReceived"),
        ("RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieRespondeAnchorRequestDenied"),
        ("RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieRespondeAnchorTransferred"),
        ("RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieInitHandoffRequestsSent"),
        ("RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieInitHandoffReplyReceived"),
        ("RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieInitHandoffasLocalReceived"),
        ("RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieInitHandoffasForeignReceived"),
        ("RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieInitHandoffDenyReceived"),
        ("RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieInitAnchorRequestSent"),
        ("RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieInitAnchorDenyReceived"),
        ("RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieAPPriorityEnable"),
        ("RUIJIE-CAPWAP-MOBILITY-MIB", "ruijiePrimaryBackUpACIP"),
        ("RUIJIE-CAPWAP-MOBILITY-MIB", "ruijiePrimaryBackUpACName"),
        ("RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieSecondaryBackUpACIP"),
        ("RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieSecondaryBackUpACName"),
        ("RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieTeriaryBackUpACip"),
        ("RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieTeriaryBackUpACName"),
        ("RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieACIntraRoam"),
        ("RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieACInterRoamIn"),
        ("RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieACInterRoamOut"),
        ("RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieMobilityACPingIPv6"),
        ("RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieRoamIPv6MemberGroupId"),
        ("RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieRoamIPv6MemberPeerAddress"),
        ("RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieRoamIPv6MemberIsList"),
        ("RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieRoamIPv6MemberDataChannelIsOK"),
        ("RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieRoamIPv6MemberDataChannelFailTimes"),
        ("RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieRoamIPv6MemberDTLSIsClient"),
        ("RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieRoamIPv6MemberDTLSIsOK"),
        ("RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieRoamIPv6MemberCreateStatus"),
        ("RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieRoamUserMac"),
        ("RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieRoamUserRoamType"),
        ("RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieRoamUserRoamOutAcAddressType"),
        ("RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieRoamUserRoamOutAcAddress"),
        ("RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieRoamUserRoamInAcAddressType"),
        ("RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieRoamUserRoamInAcAddress"),
        ("RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieRoamUserRoamOutApMac"),
        ("RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieRoamUserRoamInApMac"),
        ("RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieRoamUserRoamOutVid"),
        ("RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieRoamUserRoamInVid"),
        ("RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieRoamTrackStaMac"),
        ("RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieRoamTrackId"),
        ("RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieRoamTrackAcAddressType"),
        ("RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieRoamTrackAcAddress"),
        ("RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieRoamTrackApMac"),
        ("RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieRoamTrackRadioId"),
        ("RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieRoamTrackStaIp"),
        ("RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieRoamTrackStaIpv6"),
        ("RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieRoamTrackStaOnlineTime"))
)
if mibBuilder.loadTexts:
    ruijieMobilityMIBGroup.setStatus("current")


# Notification objects

ruijieMobilityNotifyStaOper = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 3, 2, 1)
)
ruijieMobilityNotifyStaOper.setObjects(
      *(("RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieMobilityNotifyApMac"),
        ("RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieMobilityNotifyStaMac"),
        ("RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieMobilityNotifyApIp"),
        ("RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieMobilityNotifyStaIp"),
        ("RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieMobilityNotifyStaOperType"),
        ("RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieMobilityNotifyStaApRadioId"),
        ("RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieMobilityNotifyStaApRadioType"),
        ("RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieMobilityNotifyStaVlanId"),
        ("RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieMobilityNotifyStaWlanId"),
        ("RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieMobilityNotifyStaIpv6"),
        ("RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieMobilityNotifyStaAssoAuthMode"),
        ("RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieMobilityNotifyStaNetAuthMode"),
        ("RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieMobilityNotifyStaSsid"),
        ("RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieMobilityNotifyStaLinkRate"),
        ("RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieMobilityNotifyStaCurChan"),
        ("RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieMobilityNotifyStaClientType"),
        ("RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieMobilityNotifyStaRssi"),
        ("RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieMobilityNotifyStaReason"))
)
if mibBuilder.loadTexts:
    ruijieMobilityNotifyStaOper.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

ruijieMobilityMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 64, 1, 2, 1, 1)
)
ruijieMobilityMIBCompliance.setObjects(
    ("RUIJIE-CAPWAP-MOBILITY-MIB", "ruijieMobilityMIBGroup")
)
if mibBuilder.loadTexts:
    ruijieMobilityMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-CAPWAP-MOBILITY-MIB",
    **{"ruijieMobilityMIB": ruijieMobilityMIB,
       "ruijieMobilityMIBObjects": ruijieMobilityMIBObjects,
       "ruijieMobility": ruijieMobility,
       "ruijieMobilityEntryTable": ruijieMobilityEntryTable,
       "ruijieMobilityEntry": ruijieMobilityEntry,
       "ruijieRoamGroupId": ruijieRoamGroupId,
       "ruijieRoamGroupName": ruijieRoamGroupName,
       "ruijieRoamGroupMyAddress": ruijieRoamGroupMyAddress,
       "ruijieRoamGroupMcEnable": ruijieRoamGroupMcEnable,
       "ruijieRoamGroupMcAddress": ruijieRoamGroupMcAddress,
       "ruijieRoamGroupKeepaliveCount": ruijieRoamGroupKeepaliveCount,
       "ruijieRoamGroupKeepaliveInterval": ruijieRoamGroupKeepaliveInterval,
       "ruijieRoamGroupIsFast": ruijieRoamGroupIsFast,
       "ruijieRoamGroupCreateStatus": ruijieRoamGroupCreateStatus,
       "ruijieRoamGroupMyAddressIPv6": ruijieRoamGroupMyAddressIPv6,
       "ruijieMobilityMemberEntryTable": ruijieMobilityMemberEntryTable,
       "ruijieMobilityMemberEntry": ruijieMobilityMemberEntry,
       "ruijieRoamMemberGroupId": ruijieRoamMemberGroupId,
       "ruijieRoamMemberPeerAddress": ruijieRoamMemberPeerAddress,
       "ruijieRoamMemberIsList": ruijieRoamMemberIsList,
       "ruijieRoamMemberDataChannelIsOK": ruijieRoamMemberDataChannelIsOK,
       "ruijieRoamMemberDataChannelFailTimes": ruijieRoamMemberDataChannelFailTimes,
       "ruijieRoamMemberDTLSIsClient": ruijieRoamMemberDTLSIsClient,
       "ruijieRoamMemberDTLSIsOK": ruijieRoamMemberDTLSIsOK,
       "ruijieRoamMemberCreateStatus": ruijieRoamMemberCreateStatus,
       "ruijieAPCtrlCreatEntryTable": ruijieAPCtrlCreatEntryTable,
       "ruijieAPCtrlCreatEntry": ruijieAPCtrlCreatEntry,
       "ruijieAPName": ruijieAPName,
       "ruijiePriority": ruijiePriority,
       "ruijiePrimaryACIP": ruijiePrimaryACIP,
       "ruijiePrimaryACName": ruijiePrimaryACName,
       "ruijieSecondaryACIP": ruijieSecondaryACIP,
       "ruijieSecondaryACName": ruijieSecondaryACName,
       "ruijieTertiaryACIP": ruijieTertiaryACIP,
       "ruijieTertiaryACName": ruijieTertiaryACName,
       "ruijieAPCtrlCreatStatus": ruijieAPCtrlCreatStatus,
       "ruijieWLANCtrlCreatEntryTable": ruijieWLANCtrlCreatEntryTable,
       "ruijieWLANCtrlCreatEntry": ruijieWLANCtrlCreatEntry,
       "ruijieWLANID": ruijieWLANID,
       "ruijieAnchorACIPaddr": ruijieAnchorACIPaddr,
       "ruijieWLANCtrlCreatStatus": ruijieWLANCtrlCreatStatus,
       "ruijieAnchorACIPaddrIPv6": ruijieAnchorACIPaddrIPv6,
       "ruijieMobilityACPing": ruijieMobilityACPing,
       "ruijieGlobalHandoffRequestsReceived": ruijieGlobalHandoffRequestsReceived,
       "ruijieGlobalHandoffEndRequestsReceived": ruijieGlobalHandoffEndRequestsReceived,
       "ruijieGlobalStateTransitionsDisabled": ruijieGlobalStateTransitionsDisabled,
       "ruijieGlobalResourceUnavailable": ruijieGlobalResourceUnavailable,
       "ruijieRespondeHandoffRequestIgnored": ruijieRespondeHandoffRequestIgnored,
       "ruijieRespondePingPongHandoffRequestsDropped": ruijieRespondePingPongHandoffRequestsDropped,
       "ruijieRespondeHandoffRequestsDroped": ruijieRespondeHandoffRequestsDroped,
       "ruijieRespondeHandoffRequestsDenied": ruijieRespondeHandoffRequestsDenied,
       "ruijieRespondeClientHandoffasLocal": ruijieRespondeClientHandoffasLocal,
       "ruijieRespondeClientHandoffasForeign": ruijieRespondeClientHandoffasForeign,
       "ruijieRespondeAnchorRequestsReceived": ruijieRespondeAnchorRequestsReceived,
       "ruijieRespondeAnchorRequestDenied": ruijieRespondeAnchorRequestDenied,
       "ruijieRespondeAnchorTransferred": ruijieRespondeAnchorTransferred,
       "ruijieInitHandoffRequestsSent": ruijieInitHandoffRequestsSent,
       "ruijieInitHandoffReplyReceived": ruijieInitHandoffReplyReceived,
       "ruijieInitHandoffasLocalReceived": ruijieInitHandoffasLocalReceived,
       "ruijieInitHandoffasForeignReceived": ruijieInitHandoffasForeignReceived,
       "ruijieInitHandoffDenyReceived": ruijieInitHandoffDenyReceived,
       "ruijieInitAnchorRequestSent": ruijieInitAnchorRequestSent,
       "ruijieInitAnchorDenyReceived": ruijieInitAnchorDenyReceived,
       "ruijieAPPriorityEnable": ruijieAPPriorityEnable,
       "ruijiePrimaryBackUpACIP": ruijiePrimaryBackUpACIP,
       "ruijiePrimaryBackUpACName": ruijiePrimaryBackUpACName,
       "ruijieSecondaryBackUpACIP": ruijieSecondaryBackUpACIP,
       "ruijieSecondaryBackUpACName": ruijieSecondaryBackUpACName,
       "ruijieTeriaryBackUpACip": ruijieTeriaryBackUpACip,
       "ruijieTeriaryBackUpACName": ruijieTeriaryBackUpACName,
       "ruijieACIntraRoam": ruijieACIntraRoam,
       "ruijieACInterRoamIn": ruijieACInterRoamIn,
       "ruijieACInterRoamOut": ruijieACInterRoamOut,
       "ruijieMobilityACPingIPv6": ruijieMobilityACPingIPv6,
       "ruijieMobilityIPv6MemberEntryTable": ruijieMobilityIPv6MemberEntryTable,
       "ruijieMobilityIPv6MemberEntry": ruijieMobilityIPv6MemberEntry,
       "ruijieRoamIPv6MemberGroupId": ruijieRoamIPv6MemberGroupId,
       "ruijieRoamIPv6MemberPeerAddress": ruijieRoamIPv6MemberPeerAddress,
       "ruijieRoamIPv6MemberIsList": ruijieRoamIPv6MemberIsList,
       "ruijieRoamIPv6MemberDataChannelIsOK": ruijieRoamIPv6MemberDataChannelIsOK,
       "ruijieRoamIPv6MemberDataChannelFailTimes": ruijieRoamIPv6MemberDataChannelFailTimes,
       "ruijieRoamIPv6MemberDTLSIsClient": ruijieRoamIPv6MemberDTLSIsClient,
       "ruijieRoamIPv6MemberDTLSIsOK": ruijieRoamIPv6MemberDTLSIsOK,
       "ruijieRoamIPv6MemberCreateStatus": ruijieRoamIPv6MemberCreateStatus,
       "ruijieMobilityUserEntryTable": ruijieMobilityUserEntryTable,
       "ruijieMobilityUserEntry": ruijieMobilityUserEntry,
       "ruijieRoamUserMac": ruijieRoamUserMac,
       "ruijieRoamUserRoamType": ruijieRoamUserRoamType,
       "ruijieRoamUserRoamOutAcAddressType": ruijieRoamUserRoamOutAcAddressType,
       "ruijieRoamUserRoamOutAcAddress": ruijieRoamUserRoamOutAcAddress,
       "ruijieRoamUserRoamInAcAddressType": ruijieRoamUserRoamInAcAddressType,
       "ruijieRoamUserRoamInAcAddress": ruijieRoamUserRoamInAcAddress,
       "ruijieRoamUserRoamOutApMac": ruijieRoamUserRoamOutApMac,
       "ruijieRoamUserRoamInApMac": ruijieRoamUserRoamInApMac,
       "ruijieRoamUserRoamOutVid": ruijieRoamUserRoamOutVid,
       "ruijieRoamUserRoamInVid": ruijieRoamUserRoamInVid,
       "ruijieMobilityTrackEntryTable": ruijieMobilityTrackEntryTable,
       "ruijieMobilityTrackEntry": ruijieMobilityTrackEntry,
       "ruijieRoamTrackStaMac": ruijieRoamTrackStaMac,
       "ruijieRoamTrackId": ruijieRoamTrackId,
       "ruijieRoamTrackAcAddressType": ruijieRoamTrackAcAddressType,
       "ruijieRoamTrackAcAddress": ruijieRoamTrackAcAddress,
       "ruijieRoamTrackApMac": ruijieRoamTrackApMac,
       "ruijieRoamTrackRadioId": ruijieRoamTrackRadioId,
       "ruijieRoamTrackStaIp": ruijieRoamTrackStaIp,
       "ruijieRoamTrackStaIpv6": ruijieRoamTrackStaIpv6,
       "ruijieRoamTrackStaOnlineTime": ruijieRoamTrackStaOnlineTime,
       "ruijieMobilityUserJsonTable": ruijieMobilityUserJsonTable,
       "ruijieMobilityUserJsonEntry": ruijieMobilityUserJsonEntry,
       "ruijieMobilityUserJsonMacAddr": ruijieMobilityUserJsonMacAddr,
       "ruijieMobilityUserJsonContent": ruijieMobilityUserJsonContent,
       "ruijieMobilityIf": ruijieMobilityIf,
       "ruijieMobilityMIBCompliances": ruijieMobilityMIBCompliances,
       "ruijieMobilityMIBCompliance": ruijieMobilityMIBCompliance,
       "ruijieMobilityMIBGroups": ruijieMobilityMIBGroups,
       "ruijieMobilityMIBGroup": ruijieMobilityMIBGroup,
       "ruijieMobilityTrap": ruijieMobilityTrap,
       "ruijieMobilityTrapSta": ruijieMobilityTrapSta,
       "ruijieMobilityNotifyApMac": ruijieMobilityNotifyApMac,
       "ruijieMobilityNotifyStaMac": ruijieMobilityNotifyStaMac,
       "ruijieMobilityNotifyApIp": ruijieMobilityNotifyApIp,
       "ruijieMobilityNotifyStaIp": ruijieMobilityNotifyStaIp,
       "ruijieMobilityNotifyStaOperType": ruijieMobilityNotifyStaOperType,
       "ruijieMobilityNotifyStaApRadioId": ruijieMobilityNotifyStaApRadioId,
       "ruijieMobilityNotifyStaApRadioType": ruijieMobilityNotifyStaApRadioType,
       "ruijieMobilityNotifyStaVlanId": ruijieMobilityNotifyStaVlanId,
       "ruijieMobilityNotifyStaWlanId": ruijieMobilityNotifyStaWlanId,
       "ruijieMobilityNotifyStaIpv6": ruijieMobilityNotifyStaIpv6,
       "ruijieMobilityNotifyStaAssoAuthMode": ruijieMobilityNotifyStaAssoAuthMode,
       "ruijieMobilityNotifyStaNetAuthMode": ruijieMobilityNotifyStaNetAuthMode,
       "ruijieMobilityNotifyStaSsid": ruijieMobilityNotifyStaSsid,
       "ruijieMobilityNotifyStaLinkRate": ruijieMobilityNotifyStaLinkRate,
       "ruijieMobilityNotifyStaCurChan": ruijieMobilityNotifyStaCurChan,
       "ruijieMobilityNotifyStaClientType": ruijieMobilityNotifyStaClientType,
       "ruijieMobilityNotifyStaRssi": ruijieMobilityNotifyStaRssi,
       "ruijieMobilityNotifyStaReason": ruijieMobilityNotifyStaReason,
       "ruijieMobilityTrapStaIf": ruijieMobilityTrapStaIf,
       "ruijieMobilityNotifyStaOper": ruijieMobilityNotifyStaOper}
)
