# SNMP MIB module (RUIJIE-DHCP-SNOOPING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-DHCP-SNOOPING-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 11:05:39 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(VlanIndex,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ruijieDhcpSnoopingMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 42)
)
if mibBuilder.loadTexts:
    ruijieDhcpSnoopingMIB.setRevisions(
        ("2007-10-18 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieDhcpSnoopingMIBTraps_ObjectIdentity = ObjectIdentity
ruijieDhcpSnoopingMIBTraps = _RuijieDhcpSnoopingMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 42, 0)
)
_RuijieDhcpSnoopingMIBObjects_ObjectIdentity = ObjectIdentity
ruijieDhcpSnoopingMIBObjects = _RuijieDhcpSnoopingMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 42, 1)
)
_RuijieSNDhcpGlobal_ObjectIdentity = ObjectIdentity
ruijieSNDhcpGlobal = _RuijieSNDhcpGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 42, 1, 1)
)
_RuijieSNDhcpFeatureEnable_Type = TruthValue
_RuijieSNDhcpFeatureEnable_Object = MibScalar
ruijieSNDhcpFeatureEnable = _RuijieSNDhcpFeatureEnable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 42, 1, 1, 1),
    _RuijieSNDhcpFeatureEnable_Type()
)
ruijieSNDhcpFeatureEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieSNDhcpFeatureEnable.setStatus("current")
_RuijieSNDhcpDatabaseUpdateInterval_Type = Unsigned32
_RuijieSNDhcpDatabaseUpdateInterval_Object = MibScalar
ruijieSNDhcpDatabaseUpdateInterval = _RuijieSNDhcpDatabaseUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 42, 1, 1, 2),
    _RuijieSNDhcpDatabaseUpdateInterval_Type()
)
ruijieSNDhcpDatabaseUpdateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieSNDhcpDatabaseUpdateInterval.setStatus("current")
if mibBuilder.loadTexts:
    ruijieSNDhcpDatabaseUpdateInterval.setUnits("seconds")
_RuijieSNDhcpRelayAgentInfoOptEnable_Type = TruthValue
_RuijieSNDhcpRelayAgentInfoOptEnable_Object = MibScalar
ruijieSNDhcpRelayAgentInfoOptEnable = _RuijieSNDhcpRelayAgentInfoOptEnable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 42, 1, 1, 3),
    _RuijieSNDhcpRelayAgentInfoOptEnable_Type()
)
ruijieSNDhcpRelayAgentInfoOptEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieSNDhcpRelayAgentInfoOptEnable.setStatus("current")
_RuijieSNDhcpMatchMacAddressEnable_Type = TruthValue
_RuijieSNDhcpMatchMacAddressEnable_Object = MibScalar
ruijieSNDhcpMatchMacAddressEnable = _RuijieSNDhcpMatchMacAddressEnable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 42, 1, 1, 4),
    _RuijieSNDhcpMatchMacAddressEnable_Type()
)
ruijieSNDhcpMatchMacAddressEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieSNDhcpMatchMacAddressEnable.setStatus("current")
_RuijieSNDhcpInterface_ObjectIdentity = ObjectIdentity
ruijieSNDhcpInterface = _RuijieSNDhcpInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 42, 1, 2)
)
_RuijieSNDhcpIfTrustTable_Object = MibTable
ruijieSNDhcpIfTrustTable = _RuijieSNDhcpIfTrustTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 42, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ruijieSNDhcpIfTrustTable.setStatus("current")
_RuijieSNDhcpIfTrustEntry_Object = MibTableRow
ruijieSNDhcpIfTrustEntry = _RuijieSNDhcpIfTrustEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 42, 1, 2, 1, 1)
)
ruijieSNDhcpIfTrustEntry.setIndexNames(
    (0, "RUIJIE-DHCP-SNOOPING-MIB", "ruijieSNDhcpIfTrustIndex"),
)
if mibBuilder.loadTexts:
    ruijieSNDhcpIfTrustEntry.setStatus("current")
_RuijieSNDhcpIfTrustIndex_Type = InterfaceIndex
_RuijieSNDhcpIfTrustIndex_Object = MibTableColumn
ruijieSNDhcpIfTrustIndex = _RuijieSNDhcpIfTrustIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 42, 1, 2, 1, 1, 1),
    _RuijieSNDhcpIfTrustIndex_Type()
)
ruijieSNDhcpIfTrustIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieSNDhcpIfTrustIndex.setStatus("current")
_RuijieSNDhcpIfTrustEnable_Type = TruthValue
_RuijieSNDhcpIfTrustEnable_Object = MibTableColumn
ruijieSNDhcpIfTrustEnable = _RuijieSNDhcpIfTrustEnable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 42, 1, 2, 1, 1, 2),
    _RuijieSNDhcpIfTrustEnable_Type()
)
ruijieSNDhcpIfTrustEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieSNDhcpIfTrustEnable.setStatus("current")
_RuijieSNDhcpIfSuppressionTable_Object = MibTable
ruijieSNDhcpIfSuppressionTable = _RuijieSNDhcpIfSuppressionTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 42, 1, 2, 2)
)
if mibBuilder.loadTexts:
    ruijieSNDhcpIfSuppressionTable.setStatus("current")
_RuijieSNDhcpIfSuppressionEntry_Object = MibTableRow
ruijieSNDhcpIfSuppressionEntry = _RuijieSNDhcpIfSuppressionEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 42, 1, 2, 2, 1)
)
ruijieSNDhcpIfSuppressionEntry.setIndexNames(
    (0, "RUIJIE-DHCP-SNOOPING-MIB", "ruijieSNDhcpIfSuppressionIndex"),
)
if mibBuilder.loadTexts:
    ruijieSNDhcpIfSuppressionEntry.setStatus("current")
_RuijieSNDhcpIfSuppressionIndex_Type = InterfaceIndex
_RuijieSNDhcpIfSuppressionIndex_Object = MibTableColumn
ruijieSNDhcpIfSuppressionIndex = _RuijieSNDhcpIfSuppressionIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 42, 1, 2, 2, 1, 1),
    _RuijieSNDhcpIfSuppressionIndex_Type()
)
ruijieSNDhcpIfSuppressionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieSNDhcpIfSuppressionIndex.setStatus("current")
_RuijieSNDhcpIfSuppressionEnable_Type = TruthValue
_RuijieSNDhcpIfSuppressionEnable_Object = MibTableColumn
ruijieSNDhcpIfSuppressionEnable = _RuijieSNDhcpIfSuppressionEnable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 42, 1, 2, 2, 1, 2),
    _RuijieSNDhcpIfSuppressionEnable_Type()
)
ruijieSNDhcpIfSuppressionEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieSNDhcpIfSuppressionEnable.setStatus("current")
_RuijieSNDhcpAddressBindTable_Object = MibTable
ruijieSNDhcpAddressBindTable = _RuijieSNDhcpAddressBindTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 42, 1, 2, 3)
)
if mibBuilder.loadTexts:
    ruijieSNDhcpAddressBindTable.setStatus("current")
_RuijieSNDhcpAddressBindEntry_Object = MibTableRow
ruijieSNDhcpAddressBindEntry = _RuijieSNDhcpAddressBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 42, 1, 2, 3, 1)
)
ruijieSNDhcpAddressBindEntry.setIndexNames(
    (0, "RUIJIE-DHCP-SNOOPING-MIB", "ruijieSNDhcpAddressBindIndex"),
)
if mibBuilder.loadTexts:
    ruijieSNDhcpAddressBindEntry.setStatus("current")
_RuijieSNDhcpAddressBindIndex_Type = InterfaceIndex
_RuijieSNDhcpAddressBindIndex_Object = MibTableColumn
ruijieSNDhcpAddressBindIndex = _RuijieSNDhcpAddressBindIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 42, 1, 2, 3, 1, 1),
    _RuijieSNDhcpAddressBindIndex_Type()
)
ruijieSNDhcpAddressBindIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieSNDhcpAddressBindIndex.setStatus("current")
_RuijieSNDhcpAddressBindEnable_Type = TruthValue
_RuijieSNDhcpAddressBindEnable_Object = MibTableColumn
ruijieSNDhcpAddressBindEnable = _RuijieSNDhcpAddressBindEnable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 42, 1, 2, 3, 1, 2),
    _RuijieSNDhcpAddressBindEnable_Type()
)
ruijieSNDhcpAddressBindEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieSNDhcpAddressBindEnable.setStatus("current")
_RuijieDhcpSnpFalsePktStatisticTable_Object = MibTable
ruijieDhcpSnpFalsePktStatisticTable = _RuijieDhcpSnpFalsePktStatisticTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 42, 1, 2, 4)
)
if mibBuilder.loadTexts:
    ruijieDhcpSnpFalsePktStatisticTable.setStatus("current")
_RuijieDhcpSnpFalsePktStatisticEntry_Object = MibTableRow
ruijieDhcpSnpFalsePktStatisticEntry = _RuijieDhcpSnpFalsePktStatisticEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 42, 1, 2, 4, 1)
)
ruijieDhcpSnpFalsePktStatisticEntry.setIndexNames(
    (0, "RUIJIE-DHCP-SNOOPING-MIB", "ruijieDhcpSnpStatisticIfIndex"),
    (0, "RUIJIE-DHCP-SNOOPING-MIB", "ruijieDhcpSnpStatisticVlanIndex"),
)
if mibBuilder.loadTexts:
    ruijieDhcpSnpFalsePktStatisticEntry.setStatus("current")
_RuijieDhcpSnpStatisticIfIndex_Type = InterfaceIndex
_RuijieDhcpSnpStatisticIfIndex_Object = MibTableColumn
ruijieDhcpSnpStatisticIfIndex = _RuijieDhcpSnpStatisticIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 42, 1, 2, 4, 1, 1),
    _RuijieDhcpSnpStatisticIfIndex_Type()
)
ruijieDhcpSnpStatisticIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieDhcpSnpStatisticIfIndex.setStatus("current")
_RuijieDhcpSnpStatisticVlanIndex_Type = VlanIndex
_RuijieDhcpSnpStatisticVlanIndex_Object = MibTableColumn
ruijieDhcpSnpStatisticVlanIndex = _RuijieDhcpSnpStatisticVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 42, 1, 2, 4, 1, 2),
    _RuijieDhcpSnpStatisticVlanIndex_Type()
)
ruijieDhcpSnpStatisticVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieDhcpSnpStatisticVlanIndex.setStatus("current")


class _RuijieDhcpSnpStatisticIfDescr_Type(DisplayString):
    """Custom type ruijieDhcpSnpStatisticIfDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RuijieDhcpSnpStatisticIfDescr_Type.__name__ = "DisplayString"
_RuijieDhcpSnpStatisticIfDescr_Object = MibTableColumn
ruijieDhcpSnpStatisticIfDescr = _RuijieDhcpSnpStatisticIfDescr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 42, 1, 2, 4, 1, 3),
    _RuijieDhcpSnpStatisticIfDescr_Type()
)
ruijieDhcpSnpStatisticIfDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDhcpSnpStatisticIfDescr.setStatus("current")
_RuijieDhcpSnpStatisticVlanId_Type = VlanIndex
_RuijieDhcpSnpStatisticVlanId_Object = MibTableColumn
ruijieDhcpSnpStatisticVlanId = _RuijieDhcpSnpStatisticVlanId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 42, 1, 2, 4, 1, 4),
    _RuijieDhcpSnpStatisticVlanId_Type()
)
ruijieDhcpSnpStatisticVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDhcpSnpStatisticVlanId.setStatus("current")
_RuijieChaddrNomatchSrcMacDhcpPktNum_Type = Counter32
_RuijieChaddrNomatchSrcMacDhcpPktNum_Object = MibTableColumn
ruijieChaddrNomatchSrcMacDhcpPktNum = _RuijieChaddrNomatchSrcMacDhcpPktNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 42, 1, 2, 4, 1, 5),
    _RuijieChaddrNomatchSrcMacDhcpPktNum_Type()
)
ruijieChaddrNomatchSrcMacDhcpPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieChaddrNomatchSrcMacDhcpPktNum.setStatus("current")
_RuijieArpNomatchSnpBindTblPktNum_Type = Counter32
_RuijieArpNomatchSnpBindTblPktNum_Object = MibTableColumn
ruijieArpNomatchSnpBindTblPktNum = _RuijieArpNomatchSnpBindTblPktNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 42, 1, 2, 4, 1, 6),
    _RuijieArpNomatchSnpBindTblPktNum_Type()
)
ruijieArpNomatchSnpBindTblPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieArpNomatchSnpBindTblPktNum.setStatus("current")
_RuijieIpNomatchSnpBindTblPktNum_Type = Counter32
_RuijieIpNomatchSnpBindTblPktNum_Object = MibTableColumn
ruijieIpNomatchSnpBindTblPktNum = _RuijieIpNomatchSnpBindTblPktNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 42, 1, 2, 4, 1, 7),
    _RuijieIpNomatchSnpBindTblPktNum_Type()
)
ruijieIpNomatchSnpBindTblPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIpNomatchSnpBindTblPktNum.setStatus("current")
_RuijieNomatchSnpBindTblDhcpPktNum_Type = Counter32
_RuijieNomatchSnpBindTblDhcpPktNum_Object = MibTableColumn
ruijieNomatchSnpBindTblDhcpPktNum = _RuijieNomatchSnpBindTblDhcpPktNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 42, 1, 2, 4, 1, 8),
    _RuijieNomatchSnpBindTblDhcpPktNum_Type()
)
ruijieNomatchSnpBindTblDhcpPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieNomatchSnpBindTblDhcpPktNum.setStatus("current")
_RuijieUntrustedReplyPktNum_Type = Counter32
_RuijieUntrustedReplyPktNum_Object = MibTableColumn
ruijieUntrustedReplyPktNum = _RuijieUntrustedReplyPktNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 42, 1, 2, 4, 1, 9),
    _RuijieUntrustedReplyPktNum_Type()
)
ruijieUntrustedReplyPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieUntrustedReplyPktNum.setStatus("current")
_RuijieDhcpPktIfRateDiscardNum_Type = Counter32
_RuijieDhcpPktIfRateDiscardNum_Object = MibTableColumn
ruijieDhcpPktIfRateDiscardNum = _RuijieDhcpPktIfRateDiscardNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 42, 1, 2, 4, 1, 10),
    _RuijieDhcpPktIfRateDiscardNum_Type()
)
ruijieDhcpPktIfRateDiscardNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDhcpPktIfRateDiscardNum.setStatus("current")
_RuijieSNDhcpBindings_ObjectIdentity = ObjectIdentity
ruijieSNDhcpBindings = _RuijieSNDhcpBindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 42, 1, 3)
)
_RuijieSNDhcpBindingsTable_Object = MibTable
ruijieSNDhcpBindingsTable = _RuijieSNDhcpBindingsTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 42, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ruijieSNDhcpBindingsTable.setStatus("current")
_RuijieSNDhcpBindingsEntry_Object = MibTableRow
ruijieSNDhcpBindingsEntry = _RuijieSNDhcpBindingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 42, 1, 3, 1, 1)
)
ruijieSNDhcpBindingsEntry.setIndexNames(
    (0, "RUIJIE-DHCP-SNOOPING-MIB", "ruijieSNDhcpBindingsVlan"),
    (0, "RUIJIE-DHCP-SNOOPING-MIB", "ruijieSNDhcpBindingsMacAddress"),
    (0, "RUIJIE-DHCP-SNOOPING-MIB", "ruijieSNDhcpBindingsAddrType"),
)
if mibBuilder.loadTexts:
    ruijieSNDhcpBindingsEntry.setStatus("current")
_RuijieSNDhcpBindingsVlan_Type = VlanIndex
_RuijieSNDhcpBindingsVlan_Object = MibTableColumn
ruijieSNDhcpBindingsVlan = _RuijieSNDhcpBindingsVlan_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 42, 1, 3, 1, 1, 1),
    _RuijieSNDhcpBindingsVlan_Type()
)
ruijieSNDhcpBindingsVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieSNDhcpBindingsVlan.setStatus("current")
_RuijieSNDhcpBindingsMacAddress_Type = MacAddress
_RuijieSNDhcpBindingsMacAddress_Object = MibTableColumn
ruijieSNDhcpBindingsMacAddress = _RuijieSNDhcpBindingsMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 42, 1, 3, 1, 1, 2),
    _RuijieSNDhcpBindingsMacAddress_Type()
)
ruijieSNDhcpBindingsMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieSNDhcpBindingsMacAddress.setStatus("current")


class _RuijieSNDhcpBindingsAddrType_Type(Integer32):
    """Custom type ruijieSNDhcpBindingsAddrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("static", 2))
    )


_RuijieSNDhcpBindingsAddrType_Type.__name__ = "Integer32"
_RuijieSNDhcpBindingsAddrType_Object = MibTableColumn
ruijieSNDhcpBindingsAddrType = _RuijieSNDhcpBindingsAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 42, 1, 3, 1, 1, 3),
    _RuijieSNDhcpBindingsAddrType_Type()
)
ruijieSNDhcpBindingsAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieSNDhcpBindingsAddrType.setStatus("current")
_RuijieSNDhcpBindingsIpAddress_Type = IpAddress
_RuijieSNDhcpBindingsIpAddress_Object = MibTableColumn
ruijieSNDhcpBindingsIpAddress = _RuijieSNDhcpBindingsIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 42, 1, 3, 1, 1, 4),
    _RuijieSNDhcpBindingsIpAddress_Type()
)
ruijieSNDhcpBindingsIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieSNDhcpBindingsIpAddress.setStatus("current")
_RuijieSNDhcpBindingsInterface_Type = InterfaceIndex
_RuijieSNDhcpBindingsInterface_Object = MibTableColumn
ruijieSNDhcpBindingsInterface = _RuijieSNDhcpBindingsInterface_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 42, 1, 3, 1, 1, 5),
    _RuijieSNDhcpBindingsInterface_Type()
)
ruijieSNDhcpBindingsInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieSNDhcpBindingsInterface.setStatus("current")
_RuijieSNDhcpBindingsLeasedTime_Type = Unsigned32
_RuijieSNDhcpBindingsLeasedTime_Object = MibTableColumn
ruijieSNDhcpBindingsLeasedTime = _RuijieSNDhcpBindingsLeasedTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 42, 1, 3, 1, 1, 6),
    _RuijieSNDhcpBindingsLeasedTime_Type()
)
ruijieSNDhcpBindingsLeasedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSNDhcpBindingsLeasedTime.setStatus("current")
if mibBuilder.loadTexts:
    ruijieSNDhcpBindingsLeasedTime.setUnits("seconds")
_RuijieSNDhcpBindingsStatus_Type = RowStatus
_RuijieSNDhcpBindingsStatus_Object = MibTableColumn
ruijieSNDhcpBindingsStatus = _RuijieSNDhcpBindingsStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 42, 1, 3, 1, 1, 7),
    _RuijieSNDhcpBindingsStatus_Type()
)
ruijieSNDhcpBindingsStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieSNDhcpBindingsStatus.setStatus("current")
_RuijieDhcpTrapMacAddress_Type = MacAddress
_RuijieDhcpTrapMacAddress_Object = MibScalar
ruijieDhcpTrapMacAddress = _RuijieDhcpTrapMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 42, 1, 4),
    _RuijieDhcpTrapMacAddress_Type()
)
ruijieDhcpTrapMacAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieDhcpTrapMacAddress.setStatus("current")
_RuijieDhcpSnoopingMIBConformance_ObjectIdentity = ObjectIdentity
ruijieDhcpSnoopingMIBConformance = _RuijieDhcpSnoopingMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 42, 2)
)
_RuijieDhcpSnoopingMIBCompliances_ObjectIdentity = ObjectIdentity
ruijieDhcpSnoopingMIBCompliances = _RuijieDhcpSnoopingMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 42, 2, 1)
)
_RuijieDhcpSnoopingMIBGroups_ObjectIdentity = ObjectIdentity
ruijieDhcpSnoopingMIBGroups = _RuijieDhcpSnoopingMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 42, 2, 2)
)

# Managed Objects groups

ruijieDhcpSnoopingMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 42, 2, 2, 1)
)
ruijieDhcpSnoopingMIBGroup.setObjects(
      *(("RUIJIE-DHCP-SNOOPING-MIB", "ruijieSNDhcpFeatureEnable"),
        ("RUIJIE-DHCP-SNOOPING-MIB", "ruijieSNDhcpDatabaseUpdateInterval"),
        ("RUIJIE-DHCP-SNOOPING-MIB", "ruijieSNDhcpRelayAgentInfoOptEnable"),
        ("RUIJIE-DHCP-SNOOPING-MIB", "ruijieSNDhcpMatchMacAddressEnable"),
        ("RUIJIE-DHCP-SNOOPING-MIB", "ruijieSNDhcpIfTrustEnable"),
        ("RUIJIE-DHCP-SNOOPING-MIB", "ruijieSNDhcpIfSuppressionEnable"),
        ("RUIJIE-DHCP-SNOOPING-MIB", "ruijieSNDhcpAddressBindEnable"),
        ("RUIJIE-DHCP-SNOOPING-MIB", "ruijieDhcpSnpStatisticIfDescr"),
        ("RUIJIE-DHCP-SNOOPING-MIB", "ruijieDhcpSnpStatisticVlanId"),
        ("RUIJIE-DHCP-SNOOPING-MIB", "ruijieChaddrNomatchSrcMacDhcpPktNum"),
        ("RUIJIE-DHCP-SNOOPING-MIB", "ruijieArpNomatchSnpBindTblPktNum"),
        ("RUIJIE-DHCP-SNOOPING-MIB", "ruijieIpNomatchSnpBindTblPktNum"),
        ("RUIJIE-DHCP-SNOOPING-MIB", "ruijieNomatchSnpBindTblDhcpPktNum"),
        ("RUIJIE-DHCP-SNOOPING-MIB", "ruijieUntrustedReplyPktNum"),
        ("RUIJIE-DHCP-SNOOPING-MIB", "ruijieDhcpPktIfRateDiscardNum"),
        ("RUIJIE-DHCP-SNOOPING-MIB", "ruijieSNDhcpBindingsIpAddress"),
        ("RUIJIE-DHCP-SNOOPING-MIB", "ruijieSNDhcpBindingsInterface"),
        ("RUIJIE-DHCP-SNOOPING-MIB", "ruijieSNDhcpBindingsLeasedTime"),
        ("RUIJIE-DHCP-SNOOPING-MIB", "ruijieSNDhcpBindingsStatus"),
        ("RUIJIE-DHCP-SNOOPING-MIB", "ruijieDhcpTrapMacAddress"))
)
if mibBuilder.loadTexts:
    ruijieDhcpSnoopingMIBGroup.setStatus("current")


# Notification objects

ruijieDhcpSnoopingNoResponseTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 42, 0, 1)
)
ruijieDhcpSnoopingNoResponseTrap.setObjects(
    ("RUIJIE-DHCP-SNOOPING-MIB", "ruijieDhcpTrapMacAddress")
)
if mibBuilder.loadTexts:
    ruijieDhcpSnoopingNoResponseTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

ruijieDhcpSnoopingMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 42, 2, 1, 1)
)
ruijieDhcpSnoopingMIBCompliance.setObjects(
    ("RUIJIE-DHCP-SNOOPING-MIB", "ruijieDhcpSnoopingMIBGroup")
)
if mibBuilder.loadTexts:
    ruijieDhcpSnoopingMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-DHCP-SNOOPING-MIB",
    **{"ruijieDhcpSnoopingMIB": ruijieDhcpSnoopingMIB,
       "ruijieDhcpSnoopingMIBTraps": ruijieDhcpSnoopingMIBTraps,
       "ruijieDhcpSnoopingNoResponseTrap": ruijieDhcpSnoopingNoResponseTrap,
       "ruijieDhcpSnoopingMIBObjects": ruijieDhcpSnoopingMIBObjects,
       "ruijieSNDhcpGlobal": ruijieSNDhcpGlobal,
       "ruijieSNDhcpFeatureEnable": ruijieSNDhcpFeatureEnable,
       "ruijieSNDhcpDatabaseUpdateInterval": ruijieSNDhcpDatabaseUpdateInterval,
       "ruijieSNDhcpRelayAgentInfoOptEnable": ruijieSNDhcpRelayAgentInfoOptEnable,
       "ruijieSNDhcpMatchMacAddressEnable": ruijieSNDhcpMatchMacAddressEnable,
       "ruijieSNDhcpInterface": ruijieSNDhcpInterface,
       "ruijieSNDhcpIfTrustTable": ruijieSNDhcpIfTrustTable,
       "ruijieSNDhcpIfTrustEntry": ruijieSNDhcpIfTrustEntry,
       "ruijieSNDhcpIfTrustIndex": ruijieSNDhcpIfTrustIndex,
       "ruijieSNDhcpIfTrustEnable": ruijieSNDhcpIfTrustEnable,
       "ruijieSNDhcpIfSuppressionTable": ruijieSNDhcpIfSuppressionTable,
       "ruijieSNDhcpIfSuppressionEntry": ruijieSNDhcpIfSuppressionEntry,
       "ruijieSNDhcpIfSuppressionIndex": ruijieSNDhcpIfSuppressionIndex,
       "ruijieSNDhcpIfSuppressionEnable": ruijieSNDhcpIfSuppressionEnable,
       "ruijieSNDhcpAddressBindTable": ruijieSNDhcpAddressBindTable,
       "ruijieSNDhcpAddressBindEntry": ruijieSNDhcpAddressBindEntry,
       "ruijieSNDhcpAddressBindIndex": ruijieSNDhcpAddressBindIndex,
       "ruijieSNDhcpAddressBindEnable": ruijieSNDhcpAddressBindEnable,
       "ruijieDhcpSnpFalsePktStatisticTable": ruijieDhcpSnpFalsePktStatisticTable,
       "ruijieDhcpSnpFalsePktStatisticEntry": ruijieDhcpSnpFalsePktStatisticEntry,
       "ruijieDhcpSnpStatisticIfIndex": ruijieDhcpSnpStatisticIfIndex,
       "ruijieDhcpSnpStatisticVlanIndex": ruijieDhcpSnpStatisticVlanIndex,
       "ruijieDhcpSnpStatisticIfDescr": ruijieDhcpSnpStatisticIfDescr,
       "ruijieDhcpSnpStatisticVlanId": ruijieDhcpSnpStatisticVlanId,
       "ruijieChaddrNomatchSrcMacDhcpPktNum": ruijieChaddrNomatchSrcMacDhcpPktNum,
       "ruijieArpNomatchSnpBindTblPktNum": ruijieArpNomatchSnpBindTblPktNum,
       "ruijieIpNomatchSnpBindTblPktNum": ruijieIpNomatchSnpBindTblPktNum,
       "ruijieNomatchSnpBindTblDhcpPktNum": ruijieNomatchSnpBindTblDhcpPktNum,
       "ruijieUntrustedReplyPktNum": ruijieUntrustedReplyPktNum,
       "ruijieDhcpPktIfRateDiscardNum": ruijieDhcpPktIfRateDiscardNum,
       "ruijieSNDhcpBindings": ruijieSNDhcpBindings,
       "ruijieSNDhcpBindingsTable": ruijieSNDhcpBindingsTable,
       "ruijieSNDhcpBindingsEntry": ruijieSNDhcpBindingsEntry,
       "ruijieSNDhcpBindingsVlan": ruijieSNDhcpBindingsVlan,
       "ruijieSNDhcpBindingsMacAddress": ruijieSNDhcpBindingsMacAddress,
       "ruijieSNDhcpBindingsAddrType": ruijieSNDhcpBindingsAddrType,
       "ruijieSNDhcpBindingsIpAddress": ruijieSNDhcpBindingsIpAddress,
       "ruijieSNDhcpBindingsInterface": ruijieSNDhcpBindingsInterface,
       "ruijieSNDhcpBindingsLeasedTime": ruijieSNDhcpBindingsLeasedTime,
       "ruijieSNDhcpBindingsStatus": ruijieSNDhcpBindingsStatus,
       "ruijieDhcpTrapMacAddress": ruijieDhcpTrapMacAddress,
       "ruijieDhcpSnoopingMIBConformance": ruijieDhcpSnoopingMIBConformance,
       "ruijieDhcpSnoopingMIBCompliances": ruijieDhcpSnoopingMIBCompliances,
       "ruijieDhcpSnoopingMIBCompliance": ruijieDhcpSnoopingMIBCompliance,
       "ruijieDhcpSnoopingMIBGroups": ruijieDhcpSnoopingMIBGroups,
       "ruijieDhcpSnoopingMIBGroup": ruijieDhcpSnoopingMIBGroup}
)
