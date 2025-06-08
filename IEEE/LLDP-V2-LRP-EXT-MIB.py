# SNMP MIB module (LLDP-V2-LRP-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/IEEE/LLDP-V2-LRP-EXT-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 18:14:26 2025
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

(InetAddress,
 InetAddressIPv4,
 InetAddressIPv6,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressIPv4",
    "InetAddressIPv6",
    "InetPortNumber")

(lldpXdot1StandAloneExtensions,) = mibBuilder.importSymbols(
    "LLDP-EXT-DOT1-EVB-EXTENSIONS-MIB",
    "lldpXdot1StandAloneExtensions")

(LldpV2DestAddressTableIndex,) = mibBuilder.importSymbols(
    "LLDP-V2-TC-MIB",
    "LldpV2DestAddressTableIndex")

(LrpAppId,
 LrpInetAddressInfo) = mibBuilder.importSymbols(
    "LRP-TC-MIB",
    "LrpAppId",
    "LrpInetAddressInfo")

(TimeFilter,) = mibBuilder.importSymbols(
    "RMON2-MIB",
    "TimeFilter")

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


# MODULE-IDENTITY

lldpXDot1LrpExtensions = ModuleIdentity(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 3)
)
if mibBuilder.loadTexts:
    lldpXDot1LrpExtensions.setRevisions(
        ("2024-02-15 00:00",
         "2020-12-03 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LldpV2ExtLrpObjects_ObjectIdentity = ObjectIdentity
lldpV2ExtLrpObjects = _LldpV2ExtLrpObjects_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 3, 1)
)
_LldpV2ExtConfigLrp_ObjectIdentity = ObjectIdentity
lldpV2ExtConfigLrp = _LldpV2ExtConfigLrp_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 3, 1, 1)
)
_LldpV2ConfigLrpTcpControlledTable_Object = MibTable
lldpV2ConfigLrpTcpControlledTable = _LldpV2ConfigLrpTcpControlledTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 3, 1, 1, 1)
)
if mibBuilder.loadTexts:
    lldpV2ConfigLrpTcpControlledTable.setStatus("current")
_LldpV2ConfigLrpTcpControlledEntry_Object = MibTableRow
lldpV2ConfigLrpTcpControlledEntry = _LldpV2ConfigLrpTcpControlledEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 3, 1, 1, 1, 1)
)
lldpV2ConfigLrpTcpControlledEntry.setIndexNames(
    (0, "LLDP-V2-LRP-EXT-MIB", "lldpV2ConfigLrpTcpControlledApplicationId"),
)
if mibBuilder.loadTexts:
    lldpV2ConfigLrpTcpControlledEntry.setStatus("current")
_LldpV2ConfigLrpTcpControlledApplicationId_Type = LrpAppId
_LldpV2ConfigLrpTcpControlledApplicationId_Object = MibTableColumn
lldpV2ConfigLrpTcpControlledApplicationId = _LldpV2ConfigLrpTcpControlledApplicationId_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 3, 1, 1, 1, 1, 1),
    _LldpV2ConfigLrpTcpControlledApplicationId_Type()
)
lldpV2ConfigLrpTcpControlledApplicationId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpV2ConfigLrpTcpControlledApplicationId.setStatus("current")
_LldpV2ConfigLrpTcpControlledTcpPortNumber_Type = InetPortNumber
_LldpV2ConfigLrpTcpControlledTcpPortNumber_Object = MibTableColumn
lldpV2ConfigLrpTcpControlledTcpPortNumber = _LldpV2ConfigLrpTcpControlledTcpPortNumber_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 3, 1, 1, 1, 1, 2),
    _LldpV2ConfigLrpTcpControlledTcpPortNumber_Type()
)
lldpV2ConfigLrpTcpControlledTcpPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpV2ConfigLrpTcpControlledTcpPortNumber.setStatus("current")
_LldpV2ConfigLrpTcpControlledIpV4Enable_Type = TruthValue
_LldpV2ConfigLrpTcpControlledIpV4Enable_Object = MibTableColumn
lldpV2ConfigLrpTcpControlledIpV4Enable = _LldpV2ConfigLrpTcpControlledIpV4Enable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 3, 1, 1, 1, 1, 3),
    _LldpV2ConfigLrpTcpControlledIpV4Enable_Type()
)
lldpV2ConfigLrpTcpControlledIpV4Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpV2ConfigLrpTcpControlledIpV4Enable.setStatus("current")
_LldpV2ConfigLrpTcpControlledIpV4Address_Type = InetAddressIPv4
_LldpV2ConfigLrpTcpControlledIpV4Address_Object = MibTableColumn
lldpV2ConfigLrpTcpControlledIpV4Address = _LldpV2ConfigLrpTcpControlledIpV4Address_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 3, 1, 1, 1, 1, 4),
    _LldpV2ConfigLrpTcpControlledIpV4Address_Type()
)
lldpV2ConfigLrpTcpControlledIpV4Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpV2ConfigLrpTcpControlledIpV4Address.setStatus("current")
_LldpV2ConfigLrpTcpControlledIpV6Enable_Type = TruthValue
_LldpV2ConfigLrpTcpControlledIpV6Enable_Object = MibTableColumn
lldpV2ConfigLrpTcpControlledIpV6Enable = _LldpV2ConfigLrpTcpControlledIpV6Enable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 3, 1, 1, 1, 1, 5),
    _LldpV2ConfigLrpTcpControlledIpV6Enable_Type()
)
lldpV2ConfigLrpTcpControlledIpV6Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpV2ConfigLrpTcpControlledIpV6Enable.setStatus("current")
_LldpV2ConfigLrpTcpControlledIpV6Address_Type = InetAddressIPv6
_LldpV2ConfigLrpTcpControlledIpV6Address_Object = MibTableColumn
lldpV2ConfigLrpTcpControlledIpV6Address = _LldpV2ConfigLrpTcpControlledIpV6Address_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 3, 1, 1, 1, 1, 6),
    _LldpV2ConfigLrpTcpControlledIpV6Address_Type()
)
lldpV2ConfigLrpTcpControlledIpV6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpV2ConfigLrpTcpControlledIpV6Address.setStatus("current")
_LldpV2ExtLrpLocalData_ObjectIdentity = ObjectIdentity
lldpV2ExtLrpLocalData = _LldpV2ExtLrpLocalData_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 3, 1, 2)
)
_LldpV2ConfigLrpEcpTxTable_Object = MibTable
lldpV2ConfigLrpEcpTxTable = _LldpV2ConfigLrpEcpTxTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 3, 1, 2, 1)
)
if mibBuilder.loadTexts:
    lldpV2ConfigLrpEcpTxTable.setStatus("current")
_LldpV2ConfigLrpEcpTxEntry_Object = MibTableRow
lldpV2ConfigLrpEcpTxEntry = _LldpV2ConfigLrpEcpTxEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 3, 1, 2, 1, 1)
)
lldpV2ConfigLrpEcpTxEntry.setIndexNames(
    (0, "LLDP-V2-LRP-EXT-MIB", "lldpV2ConfigLrpEcpTxLocalIfIndex"),
    (0, "LLDP-V2-LRP-EXT-MIB", "lldpV2ConfigLrpEcpTxLocalDestMACAddress"),
)
if mibBuilder.loadTexts:
    lldpV2ConfigLrpEcpTxEntry.setStatus("current")
_LldpV2ConfigLrpEcpTxLocalIfIndex_Type = InterfaceIndex
_LldpV2ConfigLrpEcpTxLocalIfIndex_Object = MibTableColumn
lldpV2ConfigLrpEcpTxLocalIfIndex = _LldpV2ConfigLrpEcpTxLocalIfIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 3, 1, 2, 1, 1, 1),
    _LldpV2ConfigLrpEcpTxLocalIfIndex_Type()
)
lldpV2ConfigLrpEcpTxLocalIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpV2ConfigLrpEcpTxLocalIfIndex.setStatus("current")
_LldpV2ConfigLrpEcpTxLocalDestMACAddress_Type = LldpV2DestAddressTableIndex
_LldpV2ConfigLrpEcpTxLocalDestMACAddress_Object = MibTableColumn
lldpV2ConfigLrpEcpTxLocalDestMACAddress = _LldpV2ConfigLrpEcpTxLocalDestMACAddress_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 3, 1, 2, 1, 1, 2),
    _LldpV2ConfigLrpEcpTxLocalDestMACAddress_Type()
)
lldpV2ConfigLrpEcpTxLocalDestMACAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpV2ConfigLrpEcpTxLocalDestMACAddress.setStatus("current")


class _LldpV2ConfigLrpEcpTxEnable_Type(TruthValue):
    """Custom type lldpV2ConfigLrpEcpTxEnable based on TruthValue"""
    defaultValue = 2


_LldpV2ConfigLrpEcpTxEnable_Type.__name__ = "TruthValue"
_LldpV2ConfigLrpEcpTxEnable_Object = MibTableColumn
lldpV2ConfigLrpEcpTxEnable = _LldpV2ConfigLrpEcpTxEnable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 3, 1, 2, 1, 1, 3),
    _LldpV2ConfigLrpEcpTxEnable_Type()
)
lldpV2ConfigLrpEcpTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpV2ConfigLrpEcpTxEnable.setStatus("current")
_LldpV2ConfigLrpTcpTxTable_Object = MibTable
lldpV2ConfigLrpTcpTxTable = _LldpV2ConfigLrpTcpTxTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 3, 1, 2, 2)
)
if mibBuilder.loadTexts:
    lldpV2ConfigLrpTcpTxTable.setStatus("current")
_LldpV2ConfigLrpTcpTxEntry_Object = MibTableRow
lldpV2ConfigLrpTcpTxEntry = _LldpV2ConfigLrpTcpTxEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 3, 1, 2, 2, 1)
)
lldpV2ConfigLrpTcpTxEntry.setIndexNames(
    (0, "LLDP-V2-LRP-EXT-MIB", "lldpV2ConfigLrpTcpTxLocalIfIndex"),
    (0, "LLDP-V2-LRP-EXT-MIB", "lldpV2ConfigLrpTcpTxLocalDestMACAddress"),
)
if mibBuilder.loadTexts:
    lldpV2ConfigLrpTcpTxEntry.setStatus("current")
_LldpV2ConfigLrpTcpTxLocalIfIndex_Type = InterfaceIndex
_LldpV2ConfigLrpTcpTxLocalIfIndex_Object = MibTableColumn
lldpV2ConfigLrpTcpTxLocalIfIndex = _LldpV2ConfigLrpTcpTxLocalIfIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 3, 1, 2, 2, 1, 1),
    _LldpV2ConfigLrpTcpTxLocalIfIndex_Type()
)
lldpV2ConfigLrpTcpTxLocalIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpV2ConfigLrpTcpTxLocalIfIndex.setStatus("current")
_LldpV2ConfigLrpTcpTxLocalDestMACAddress_Type = LldpV2DestAddressTableIndex
_LldpV2ConfigLrpTcpTxLocalDestMACAddress_Object = MibTableColumn
lldpV2ConfigLrpTcpTxLocalDestMACAddress = _LldpV2ConfigLrpTcpTxLocalDestMACAddress_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 3, 1, 2, 2, 1, 2),
    _LldpV2ConfigLrpTcpTxLocalDestMACAddress_Type()
)
lldpV2ConfigLrpTcpTxLocalDestMACAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpV2ConfigLrpTcpTxLocalDestMACAddress.setStatus("current")


class _LldpV2ConfigLrpTcpTxEnable_Type(TruthValue):
    """Custom type lldpV2ConfigLrpTcpTxEnable based on TruthValue"""
    defaultValue = 2


_LldpV2ConfigLrpTcpTxEnable_Type.__name__ = "TruthValue"
_LldpV2ConfigLrpTcpTxEnable_Object = MibTableColumn
lldpV2ConfigLrpTcpTxEnable = _LldpV2ConfigLrpTcpTxEnable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 3, 1, 2, 2, 1, 3),
    _LldpV2ConfigLrpTcpTxEnable_Type()
)
lldpV2ConfigLrpTcpTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpV2ConfigLrpTcpTxEnable.setStatus("current")
_LldpV2LocLrpEcpTable_Object = MibTable
lldpV2LocLrpEcpTable = _LldpV2LocLrpEcpTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 3, 1, 2, 3)
)
if mibBuilder.loadTexts:
    lldpV2LocLrpEcpTable.setStatus("current")
_LldpV2LocLrpEcpEntry_Object = MibTableRow
lldpV2LocLrpEcpEntry = _LldpV2LocLrpEcpEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 3, 1, 2, 3, 1)
)
lldpV2LocLrpEcpEntry.setIndexNames(
    (0, "LLDP-V2-LRP-EXT-MIB", "lldpV2LocLrpEcpLocalIfIndex"),
    (0, "LLDP-V2-LRP-EXT-MIB", "lldpV2LocLrpEcpLocalDestMACAddress"),
    (0, "LLDP-V2-LRP-EXT-MIB", "lldpV2LocLrpEcpApplicationIndex"),
)
if mibBuilder.loadTexts:
    lldpV2LocLrpEcpEntry.setStatus("current")
_LldpV2LocLrpEcpLocalIfIndex_Type = InterfaceIndex
_LldpV2LocLrpEcpLocalIfIndex_Object = MibTableColumn
lldpV2LocLrpEcpLocalIfIndex = _LldpV2LocLrpEcpLocalIfIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 3, 1, 2, 3, 1, 1),
    _LldpV2LocLrpEcpLocalIfIndex_Type()
)
lldpV2LocLrpEcpLocalIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpV2LocLrpEcpLocalIfIndex.setStatus("current")
_LldpV2LocLrpEcpLocalDestMACAddress_Type = LldpV2DestAddressTableIndex
_LldpV2LocLrpEcpLocalDestMACAddress_Object = MibTableColumn
lldpV2LocLrpEcpLocalDestMACAddress = _LldpV2LocLrpEcpLocalDestMACAddress_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 3, 1, 2, 3, 1, 2),
    _LldpV2LocLrpEcpLocalDestMACAddress_Type()
)
lldpV2LocLrpEcpLocalDestMACAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpV2LocLrpEcpLocalDestMACAddress.setStatus("current")


class _LldpV2LocLrpEcpApplicationIndex_Type(Unsigned32):
    """Custom type lldpV2LocLrpEcpApplicationIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_LldpV2LocLrpEcpApplicationIndex_Type.__name__ = "Unsigned32"
_LldpV2LocLrpEcpApplicationIndex_Object = MibTableColumn
lldpV2LocLrpEcpApplicationIndex = _LldpV2LocLrpEcpApplicationIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 3, 1, 2, 3, 1, 3),
    _LldpV2LocLrpEcpApplicationIndex_Type()
)
lldpV2LocLrpEcpApplicationIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpV2LocLrpEcpApplicationIndex.setStatus("current")
_LldpV2LocLrpEcpApplicationId_Type = LrpAppId
_LldpV2LocLrpEcpApplicationId_Object = MibTableColumn
lldpV2LocLrpEcpApplicationId = _LldpV2LocLrpEcpApplicationId_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 3, 1, 2, 3, 1, 4),
    _LldpV2LocLrpEcpApplicationId_Type()
)
lldpV2LocLrpEcpApplicationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2LocLrpEcpApplicationId.setStatus("current")
_LldpV2LocLrpTcpTable_Object = MibTable
lldpV2LocLrpTcpTable = _LldpV2LocLrpTcpTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 3, 1, 2, 4)
)
if mibBuilder.loadTexts:
    lldpV2LocLrpTcpTable.setStatus("current")
_LldpV2LocLrpTcpEntry_Object = MibTableRow
lldpV2LocLrpTcpEntry = _LldpV2LocLrpTcpEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 3, 1, 2, 4, 1)
)
lldpV2LocLrpTcpEntry.setIndexNames(
    (0, "LLDP-V2-LRP-EXT-MIB", "lldpV2LocLrpTcpLocalIfIndex"),
    (0, "LLDP-V2-LRP-EXT-MIB", "lldpV2LocLrpTcpLocalDestMACAddress"),
    (0, "LLDP-V2-LRP-EXT-MIB", "lldpV2LocLrpTcpApplicationIndex"),
)
if mibBuilder.loadTexts:
    lldpV2LocLrpTcpEntry.setStatus("current")
_LldpV2LocLrpTcpLocalIfIndex_Type = InterfaceIndex
_LldpV2LocLrpTcpLocalIfIndex_Object = MibTableColumn
lldpV2LocLrpTcpLocalIfIndex = _LldpV2LocLrpTcpLocalIfIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 3, 1, 2, 4, 1, 1),
    _LldpV2LocLrpTcpLocalIfIndex_Type()
)
lldpV2LocLrpTcpLocalIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpV2LocLrpTcpLocalIfIndex.setStatus("current")
_LldpV2LocLrpTcpLocalDestMACAddress_Type = LldpV2DestAddressTableIndex
_LldpV2LocLrpTcpLocalDestMACAddress_Object = MibTableColumn
lldpV2LocLrpTcpLocalDestMACAddress = _LldpV2LocLrpTcpLocalDestMACAddress_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 3, 1, 2, 4, 1, 2),
    _LldpV2LocLrpTcpLocalDestMACAddress_Type()
)
lldpV2LocLrpTcpLocalDestMACAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpV2LocLrpTcpLocalDestMACAddress.setStatus("current")


class _LldpV2LocLrpTcpApplicationIndex_Type(Unsigned32):
    """Custom type lldpV2LocLrpTcpApplicationIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_LldpV2LocLrpTcpApplicationIndex_Type.__name__ = "Unsigned32"
_LldpV2LocLrpTcpApplicationIndex_Object = MibTableColumn
lldpV2LocLrpTcpApplicationIndex = _LldpV2LocLrpTcpApplicationIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 3, 1, 2, 4, 1, 3),
    _LldpV2LocLrpTcpApplicationIndex_Type()
)
lldpV2LocLrpTcpApplicationIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpV2LocLrpTcpApplicationIndex.setStatus("current")
_LldpV2LocLrpTcpApplicationId_Type = LrpAppId
_LldpV2LocLrpTcpApplicationId_Object = MibTableColumn
lldpV2LocLrpTcpApplicationId = _LldpV2LocLrpTcpApplicationId_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 3, 1, 2, 4, 1, 4),
    _LldpV2LocLrpTcpApplicationId_Type()
)
lldpV2LocLrpTcpApplicationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2LocLrpTcpApplicationId.setStatus("current")
_LldpV2LocLrpTcpPortNumber_Type = InetPortNumber
_LldpV2LocLrpTcpPortNumber_Object = MibTableColumn
lldpV2LocLrpTcpPortNumber = _LldpV2LocLrpTcpPortNumber_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 3, 1, 2, 4, 1, 5),
    _LldpV2LocLrpTcpPortNumber_Type()
)
lldpV2LocLrpTcpPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2LocLrpTcpPortNumber.setStatus("current")
_LldpV2LocLrpTcpAddressInfo1_Type = LrpInetAddressInfo
_LldpV2LocLrpTcpAddressInfo1_Object = MibTableColumn
lldpV2LocLrpTcpAddressInfo1 = _LldpV2LocLrpTcpAddressInfo1_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 3, 1, 2, 4, 1, 6),
    _LldpV2LocLrpTcpAddressInfo1_Type()
)
lldpV2LocLrpTcpAddressInfo1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2LocLrpTcpAddressInfo1.setStatus("current")
_LldpV2LocLrpTcpAddress1_Type = InetAddress
_LldpV2LocLrpTcpAddress1_Object = MibTableColumn
lldpV2LocLrpTcpAddress1 = _LldpV2LocLrpTcpAddress1_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 3, 1, 2, 4, 1, 7),
    _LldpV2LocLrpTcpAddress1_Type()
)
lldpV2LocLrpTcpAddress1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2LocLrpTcpAddress1.setStatus("current")
_LldpV2LocLrpTcpAddressInfo2_Type = LrpInetAddressInfo
_LldpV2LocLrpTcpAddressInfo2_Object = MibTableColumn
lldpV2LocLrpTcpAddressInfo2 = _LldpV2LocLrpTcpAddressInfo2_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 3, 1, 2, 4, 1, 8),
    _LldpV2LocLrpTcpAddressInfo2_Type()
)
lldpV2LocLrpTcpAddressInfo2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2LocLrpTcpAddressInfo2.setStatus("current")
_LldpV2LocLrpTcpAddress2_Type = InetAddress
_LldpV2LocLrpTcpAddress2_Object = MibTableColumn
lldpV2LocLrpTcpAddress2 = _LldpV2LocLrpTcpAddress2_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 3, 1, 2, 4, 1, 9),
    _LldpV2LocLrpTcpAddress2_Type()
)
lldpV2LocLrpTcpAddress2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2LocLrpTcpAddress2.setStatus("current")
_LldpV2ExtLrpRemoteData_ObjectIdentity = ObjectIdentity
lldpV2ExtLrpRemoteData = _LldpV2ExtLrpRemoteData_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 3, 1, 3)
)
_LldpV2RemLrpEcpTable_Object = MibTable
lldpV2RemLrpEcpTable = _LldpV2RemLrpEcpTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 3, 1, 3, 1)
)
if mibBuilder.loadTexts:
    lldpV2RemLrpEcpTable.setStatus("current")
_LldpV2RemLrpEcpEntry_Object = MibTableRow
lldpV2RemLrpEcpEntry = _LldpV2RemLrpEcpEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 3, 1, 3, 1, 1)
)
lldpV2RemLrpEcpEntry.setIndexNames(
    (0, "LLDP-V2-LRP-EXT-MIB", "lldpV2RemLrpEcpTimeMark"),
    (0, "LLDP-V2-LRP-EXT-MIB", "lldpV2RemLrpEcpLocalIfIndex"),
    (0, "LLDP-V2-LRP-EXT-MIB", "lldpV2RemLrpEcpLocalDestMACAddress"),
    (0, "LLDP-V2-LRP-EXT-MIB", "lldpV2RemLrpEcpIndex"),
    (0, "LLDP-V2-LRP-EXT-MIB", "lldpV2RemLrpEcpApplicationIndex"),
)
if mibBuilder.loadTexts:
    lldpV2RemLrpEcpEntry.setStatus("current")
_LldpV2RemLrpEcpTimeMark_Type = TimeFilter
_LldpV2RemLrpEcpTimeMark_Object = MibTableColumn
lldpV2RemLrpEcpTimeMark = _LldpV2RemLrpEcpTimeMark_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 3, 1, 3, 1, 1, 1),
    _LldpV2RemLrpEcpTimeMark_Type()
)
lldpV2RemLrpEcpTimeMark.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpV2RemLrpEcpTimeMark.setStatus("current")
_LldpV2RemLrpEcpLocalIfIndex_Type = InterfaceIndex
_LldpV2RemLrpEcpLocalIfIndex_Object = MibTableColumn
lldpV2RemLrpEcpLocalIfIndex = _LldpV2RemLrpEcpLocalIfIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 3, 1, 3, 1, 1, 2),
    _LldpV2RemLrpEcpLocalIfIndex_Type()
)
lldpV2RemLrpEcpLocalIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpV2RemLrpEcpLocalIfIndex.setStatus("current")
_LldpV2RemLrpEcpLocalDestMACAddress_Type = LldpV2DestAddressTableIndex
_LldpV2RemLrpEcpLocalDestMACAddress_Object = MibTableColumn
lldpV2RemLrpEcpLocalDestMACAddress = _LldpV2RemLrpEcpLocalDestMACAddress_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 3, 1, 3, 1, 1, 3),
    _LldpV2RemLrpEcpLocalDestMACAddress_Type()
)
lldpV2RemLrpEcpLocalDestMACAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpV2RemLrpEcpLocalDestMACAddress.setStatus("current")


class _LldpV2RemLrpEcpIndex_Type(Unsigned32):
    """Custom type lldpV2RemLrpEcpIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LldpV2RemLrpEcpIndex_Type.__name__ = "Unsigned32"
_LldpV2RemLrpEcpIndex_Object = MibTableColumn
lldpV2RemLrpEcpIndex = _LldpV2RemLrpEcpIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 3, 1, 3, 1, 1, 4),
    _LldpV2RemLrpEcpIndex_Type()
)
lldpV2RemLrpEcpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpV2RemLrpEcpIndex.setStatus("current")


class _LldpV2RemLrpEcpApplicationIndex_Type(Unsigned32):
    """Custom type lldpV2RemLrpEcpApplicationIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_LldpV2RemLrpEcpApplicationIndex_Type.__name__ = "Unsigned32"
_LldpV2RemLrpEcpApplicationIndex_Object = MibTableColumn
lldpV2RemLrpEcpApplicationIndex = _LldpV2RemLrpEcpApplicationIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 3, 1, 3, 1, 1, 5),
    _LldpV2RemLrpEcpApplicationIndex_Type()
)
lldpV2RemLrpEcpApplicationIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpV2RemLrpEcpApplicationIndex.setStatus("current")
_LldpV2RemLrpEcpApplicationId_Type = LrpAppId
_LldpV2RemLrpEcpApplicationId_Object = MibTableColumn
lldpV2RemLrpEcpApplicationId = _LldpV2RemLrpEcpApplicationId_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 3, 1, 3, 1, 1, 6),
    _LldpV2RemLrpEcpApplicationId_Type()
)
lldpV2RemLrpEcpApplicationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2RemLrpEcpApplicationId.setStatus("current")
_LldpV2RemLrpTcpTable_Object = MibTable
lldpV2RemLrpTcpTable = _LldpV2RemLrpTcpTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 3, 1, 3, 2)
)
if mibBuilder.loadTexts:
    lldpV2RemLrpTcpTable.setStatus("current")
_LldpV2RemLrpTcpEntry_Object = MibTableRow
lldpV2RemLrpTcpEntry = _LldpV2RemLrpTcpEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 3, 1, 3, 2, 1)
)
lldpV2RemLrpTcpEntry.setIndexNames(
    (0, "LLDP-V2-LRP-EXT-MIB", "lldpV2RemLrpTcpTimeMark"),
    (0, "LLDP-V2-LRP-EXT-MIB", "lldpV2RemLrpTcpLocalIfIndex"),
    (0, "LLDP-V2-LRP-EXT-MIB", "lldpV2RemLrpTcpLocalDestMACAddress"),
    (0, "LLDP-V2-LRP-EXT-MIB", "lldpV2RemLrpTcpIndex"),
    (0, "LLDP-V2-LRP-EXT-MIB", "lldpV2RemLrpTcpApplicationIndex"),
)
if mibBuilder.loadTexts:
    lldpV2RemLrpTcpEntry.setStatus("current")
_LldpV2RemLrpTcpTimeMark_Type = TimeFilter
_LldpV2RemLrpTcpTimeMark_Object = MibTableColumn
lldpV2RemLrpTcpTimeMark = _LldpV2RemLrpTcpTimeMark_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 3, 1, 3, 2, 1, 1),
    _LldpV2RemLrpTcpTimeMark_Type()
)
lldpV2RemLrpTcpTimeMark.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpV2RemLrpTcpTimeMark.setStatus("current")
_LldpV2RemLrpTcpLocalIfIndex_Type = InterfaceIndex
_LldpV2RemLrpTcpLocalIfIndex_Object = MibTableColumn
lldpV2RemLrpTcpLocalIfIndex = _LldpV2RemLrpTcpLocalIfIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 3, 1, 3, 2, 1, 2),
    _LldpV2RemLrpTcpLocalIfIndex_Type()
)
lldpV2RemLrpTcpLocalIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpV2RemLrpTcpLocalIfIndex.setStatus("current")
_LldpV2RemLrpTcpLocalDestMACAddress_Type = LldpV2DestAddressTableIndex
_LldpV2RemLrpTcpLocalDestMACAddress_Object = MibTableColumn
lldpV2RemLrpTcpLocalDestMACAddress = _LldpV2RemLrpTcpLocalDestMACAddress_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 3, 1, 3, 2, 1, 3),
    _LldpV2RemLrpTcpLocalDestMACAddress_Type()
)
lldpV2RemLrpTcpLocalDestMACAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpV2RemLrpTcpLocalDestMACAddress.setStatus("current")


class _LldpV2RemLrpTcpIndex_Type(Unsigned32):
    """Custom type lldpV2RemLrpTcpIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LldpV2RemLrpTcpIndex_Type.__name__ = "Unsigned32"
_LldpV2RemLrpTcpIndex_Object = MibTableColumn
lldpV2RemLrpTcpIndex = _LldpV2RemLrpTcpIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 3, 1, 3, 2, 1, 4),
    _LldpV2RemLrpTcpIndex_Type()
)
lldpV2RemLrpTcpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpV2RemLrpTcpIndex.setStatus("current")


class _LldpV2RemLrpTcpApplicationIndex_Type(Unsigned32):
    """Custom type lldpV2RemLrpTcpApplicationIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_LldpV2RemLrpTcpApplicationIndex_Type.__name__ = "Unsigned32"
_LldpV2RemLrpTcpApplicationIndex_Object = MibTableColumn
lldpV2RemLrpTcpApplicationIndex = _LldpV2RemLrpTcpApplicationIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 3, 1, 3, 2, 1, 5),
    _LldpV2RemLrpTcpApplicationIndex_Type()
)
lldpV2RemLrpTcpApplicationIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpV2RemLrpTcpApplicationIndex.setStatus("current")
_LldpV2RemLrpTcpApplicationId_Type = LrpAppId
_LldpV2RemLrpTcpApplicationId_Object = MibTableColumn
lldpV2RemLrpTcpApplicationId = _LldpV2RemLrpTcpApplicationId_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 3, 1, 3, 2, 1, 6),
    _LldpV2RemLrpTcpApplicationId_Type()
)
lldpV2RemLrpTcpApplicationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2RemLrpTcpApplicationId.setStatus("current")
_LldpV2RemLrpTcpPortNumber_Type = InetPortNumber
_LldpV2RemLrpTcpPortNumber_Object = MibTableColumn
lldpV2RemLrpTcpPortNumber = _LldpV2RemLrpTcpPortNumber_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 3, 1, 3, 2, 1, 7),
    _LldpV2RemLrpTcpPortNumber_Type()
)
lldpV2RemLrpTcpPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2RemLrpTcpPortNumber.setStatus("current")
_LldpV2RemLrpTcpAddressInfo1_Type = LrpInetAddressInfo
_LldpV2RemLrpTcpAddressInfo1_Object = MibTableColumn
lldpV2RemLrpTcpAddressInfo1 = _LldpV2RemLrpTcpAddressInfo1_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 3, 1, 3, 2, 1, 8),
    _LldpV2RemLrpTcpAddressInfo1_Type()
)
lldpV2RemLrpTcpAddressInfo1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2RemLrpTcpAddressInfo1.setStatus("current")
_LldpV2RemLrpTcpAddress1_Type = InetAddress
_LldpV2RemLrpTcpAddress1_Object = MibTableColumn
lldpV2RemLrpTcpAddress1 = _LldpV2RemLrpTcpAddress1_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 3, 1, 3, 2, 1, 9),
    _LldpV2RemLrpTcpAddress1_Type()
)
lldpV2RemLrpTcpAddress1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2RemLrpTcpAddress1.setStatus("current")
_LldpV2RemLrpTcpAddressInfo2_Type = LrpInetAddressInfo
_LldpV2RemLrpTcpAddressInfo2_Object = MibTableColumn
lldpV2RemLrpTcpAddressInfo2 = _LldpV2RemLrpTcpAddressInfo2_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 3, 1, 3, 2, 1, 10),
    _LldpV2RemLrpTcpAddressInfo2_Type()
)
lldpV2RemLrpTcpAddressInfo2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2RemLrpTcpAddressInfo2.setStatus("current")
_LldpV2RemLrpTcpAddress2_Type = InetAddress
_LldpV2RemLrpTcpAddress2_Object = MibTableColumn
lldpV2RemLrpTcpAddress2 = _LldpV2RemLrpTcpAddress2_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 3, 1, 3, 2, 1, 11),
    _LldpV2RemLrpTcpAddress2_Type()
)
lldpV2RemLrpTcpAddress2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2RemLrpTcpAddress2.setStatus("current")
_LldpV2ExtLrpConformance_ObjectIdentity = ObjectIdentity
lldpV2ExtLrpConformance = _LldpV2ExtLrpConformance_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 9)
)
_LldpV2ExtLrpCompliances_ObjectIdentity = ObjectIdentity
lldpV2ExtLrpCompliances = _LldpV2ExtLrpCompliances_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 9, 1)
)
_LldpV2ExtLrpGroups_ObjectIdentity = ObjectIdentity
lldpV2ExtLrpGroups = _LldpV2ExtLrpGroups_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 9, 2)
)

# Managed Objects groups

lldpV2ExtLrpControlledTcpControlGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 9, 2, 1)
)
lldpV2ExtLrpControlledTcpControlGroup.setObjects(
      *(("LLDP-V2-LRP-EXT-MIB", "lldpV2ConfigLrpTcpControlledTcpPortNumber"),
        ("LLDP-V2-LRP-EXT-MIB", "lldpV2ConfigLrpTcpControlledIpV4Enable"),
        ("LLDP-V2-LRP-EXT-MIB", "lldpV2ConfigLrpTcpControlledIpV4Address"),
        ("LLDP-V2-LRP-EXT-MIB", "lldpV2ConfigLrpTcpControlledIpV6Enable"),
        ("LLDP-V2-LRP-EXT-MIB", "lldpV2ConfigLrpTcpControlledIpV6Address"))
)
if mibBuilder.loadTexts:
    lldpV2ExtLrpControlledTcpControlGroup.setStatus("current")

lldpV2ExtLrpEcpTlvGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 9, 2, 2)
)
lldpV2ExtLrpEcpTlvGroup.setObjects(
      *(("LLDP-V2-LRP-EXT-MIB", "lldpV2ConfigLrpEcpTxEnable"),
        ("LLDP-V2-LRP-EXT-MIB", "lldpV2LocLrpEcpApplicationId"),
        ("LLDP-V2-LRP-EXT-MIB", "lldpV2RemLrpEcpApplicationId"))
)
if mibBuilder.loadTexts:
    lldpV2ExtLrpEcpTlvGroup.setStatus("current")

lldpV2ExtLrpTcpTlvGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 9, 2, 3)
)
lldpV2ExtLrpTcpTlvGroup.setObjects(
      *(("LLDP-V2-LRP-EXT-MIB", "lldpV2ConfigLrpTcpTxEnable"),
        ("LLDP-V2-LRP-EXT-MIB", "lldpV2LocLrpTcpApplicationId"),
        ("LLDP-V2-LRP-EXT-MIB", "lldpV2LocLrpTcpPortNumber"),
        ("LLDP-V2-LRP-EXT-MIB", "lldpV2LocLrpTcpAddressInfo1"),
        ("LLDP-V2-LRP-EXT-MIB", "lldpV2LocLrpTcpAddress1"),
        ("LLDP-V2-LRP-EXT-MIB", "lldpV2LocLrpTcpAddressInfo2"),
        ("LLDP-V2-LRP-EXT-MIB", "lldpV2LocLrpTcpAddress2"),
        ("LLDP-V2-LRP-EXT-MIB", "lldpV2RemLrpTcpApplicationId"),
        ("LLDP-V2-LRP-EXT-MIB", "lldpV2RemLrpTcpPortNumber"),
        ("LLDP-V2-LRP-EXT-MIB", "lldpV2RemLrpTcpAddressInfo1"),
        ("LLDP-V2-LRP-EXT-MIB", "lldpV2RemLrpTcpAddress1"),
        ("LLDP-V2-LRP-EXT-MIB", "lldpV2RemLrpTcpAddressInfo2"),
        ("LLDP-V2-LRP-EXT-MIB", "lldpV2RemLrpTcpAddress2"))
)
if mibBuilder.loadTexts:
    lldpV2ExtLrpTcpTlvGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

lldpV2ExtLrpTxRxCompliance = ModuleCompliance(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 9, 1, 1)
)
if mibBuilder.loadTexts:
    lldpV2ExtLrpTxRxCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LLDP-V2-LRP-EXT-MIB",
    **{"lldpXDot1LrpExtensions": lldpXDot1LrpExtensions,
       "lldpV2ExtLrpObjects": lldpV2ExtLrpObjects,
       "lldpV2ExtConfigLrp": lldpV2ExtConfigLrp,
       "lldpV2ConfigLrpTcpControlledTable": lldpV2ConfigLrpTcpControlledTable,
       "lldpV2ConfigLrpTcpControlledEntry": lldpV2ConfigLrpTcpControlledEntry,
       "lldpV2ConfigLrpTcpControlledApplicationId": lldpV2ConfigLrpTcpControlledApplicationId,
       "lldpV2ConfigLrpTcpControlledTcpPortNumber": lldpV2ConfigLrpTcpControlledTcpPortNumber,
       "lldpV2ConfigLrpTcpControlledIpV4Enable": lldpV2ConfigLrpTcpControlledIpV4Enable,
       "lldpV2ConfigLrpTcpControlledIpV4Address": lldpV2ConfigLrpTcpControlledIpV4Address,
       "lldpV2ConfigLrpTcpControlledIpV6Enable": lldpV2ConfigLrpTcpControlledIpV6Enable,
       "lldpV2ConfigLrpTcpControlledIpV6Address": lldpV2ConfigLrpTcpControlledIpV6Address,
       "lldpV2ExtLrpLocalData": lldpV2ExtLrpLocalData,
       "lldpV2ConfigLrpEcpTxTable": lldpV2ConfigLrpEcpTxTable,
       "lldpV2ConfigLrpEcpTxEntry": lldpV2ConfigLrpEcpTxEntry,
       "lldpV2ConfigLrpEcpTxLocalIfIndex": lldpV2ConfigLrpEcpTxLocalIfIndex,
       "lldpV2ConfigLrpEcpTxLocalDestMACAddress": lldpV2ConfigLrpEcpTxLocalDestMACAddress,
       "lldpV2ConfigLrpEcpTxEnable": lldpV2ConfigLrpEcpTxEnable,
       "lldpV2ConfigLrpTcpTxTable": lldpV2ConfigLrpTcpTxTable,
       "lldpV2ConfigLrpTcpTxEntry": lldpV2ConfigLrpTcpTxEntry,
       "lldpV2ConfigLrpTcpTxLocalIfIndex": lldpV2ConfigLrpTcpTxLocalIfIndex,
       "lldpV2ConfigLrpTcpTxLocalDestMACAddress": lldpV2ConfigLrpTcpTxLocalDestMACAddress,
       "lldpV2ConfigLrpTcpTxEnable": lldpV2ConfigLrpTcpTxEnable,
       "lldpV2LocLrpEcpTable": lldpV2LocLrpEcpTable,
       "lldpV2LocLrpEcpEntry": lldpV2LocLrpEcpEntry,
       "lldpV2LocLrpEcpLocalIfIndex": lldpV2LocLrpEcpLocalIfIndex,
       "lldpV2LocLrpEcpLocalDestMACAddress": lldpV2LocLrpEcpLocalDestMACAddress,
       "lldpV2LocLrpEcpApplicationIndex": lldpV2LocLrpEcpApplicationIndex,
       "lldpV2LocLrpEcpApplicationId": lldpV2LocLrpEcpApplicationId,
       "lldpV2LocLrpTcpTable": lldpV2LocLrpTcpTable,
       "lldpV2LocLrpTcpEntry": lldpV2LocLrpTcpEntry,
       "lldpV2LocLrpTcpLocalIfIndex": lldpV2LocLrpTcpLocalIfIndex,
       "lldpV2LocLrpTcpLocalDestMACAddress": lldpV2LocLrpTcpLocalDestMACAddress,
       "lldpV2LocLrpTcpApplicationIndex": lldpV2LocLrpTcpApplicationIndex,
       "lldpV2LocLrpTcpApplicationId": lldpV2LocLrpTcpApplicationId,
       "lldpV2LocLrpTcpPortNumber": lldpV2LocLrpTcpPortNumber,
       "lldpV2LocLrpTcpAddressInfo1": lldpV2LocLrpTcpAddressInfo1,
       "lldpV2LocLrpTcpAddress1": lldpV2LocLrpTcpAddress1,
       "lldpV2LocLrpTcpAddressInfo2": lldpV2LocLrpTcpAddressInfo2,
       "lldpV2LocLrpTcpAddress2": lldpV2LocLrpTcpAddress2,
       "lldpV2ExtLrpRemoteData": lldpV2ExtLrpRemoteData,
       "lldpV2RemLrpEcpTable": lldpV2RemLrpEcpTable,
       "lldpV2RemLrpEcpEntry": lldpV2RemLrpEcpEntry,
       "lldpV2RemLrpEcpTimeMark": lldpV2RemLrpEcpTimeMark,
       "lldpV2RemLrpEcpLocalIfIndex": lldpV2RemLrpEcpLocalIfIndex,
       "lldpV2RemLrpEcpLocalDestMACAddress": lldpV2RemLrpEcpLocalDestMACAddress,
       "lldpV2RemLrpEcpIndex": lldpV2RemLrpEcpIndex,
       "lldpV2RemLrpEcpApplicationIndex": lldpV2RemLrpEcpApplicationIndex,
       "lldpV2RemLrpEcpApplicationId": lldpV2RemLrpEcpApplicationId,
       "lldpV2RemLrpTcpTable": lldpV2RemLrpTcpTable,
       "lldpV2RemLrpTcpEntry": lldpV2RemLrpTcpEntry,
       "lldpV2RemLrpTcpTimeMark": lldpV2RemLrpTcpTimeMark,
       "lldpV2RemLrpTcpLocalIfIndex": lldpV2RemLrpTcpLocalIfIndex,
       "lldpV2RemLrpTcpLocalDestMACAddress": lldpV2RemLrpTcpLocalDestMACAddress,
       "lldpV2RemLrpTcpIndex": lldpV2RemLrpTcpIndex,
       "lldpV2RemLrpTcpApplicationIndex": lldpV2RemLrpTcpApplicationIndex,
       "lldpV2RemLrpTcpApplicationId": lldpV2RemLrpTcpApplicationId,
       "lldpV2RemLrpTcpPortNumber": lldpV2RemLrpTcpPortNumber,
       "lldpV2RemLrpTcpAddressInfo1": lldpV2RemLrpTcpAddressInfo1,
       "lldpV2RemLrpTcpAddress1": lldpV2RemLrpTcpAddress1,
       "lldpV2RemLrpTcpAddressInfo2": lldpV2RemLrpTcpAddressInfo2,
       "lldpV2RemLrpTcpAddress2": lldpV2RemLrpTcpAddress2,
       "lldpV2ExtLrpConformance": lldpV2ExtLrpConformance,
       "lldpV2ExtLrpCompliances": lldpV2ExtLrpCompliances,
       "lldpV2ExtLrpTxRxCompliance": lldpV2ExtLrpTxRxCompliance,
       "lldpV2ExtLrpGroups": lldpV2ExtLrpGroups,
       "lldpV2ExtLrpControlledTcpControlGroup": lldpV2ExtLrpControlledTcpControlGroup,
       "lldpV2ExtLrpEcpTlvGroup": lldpV2ExtLrpEcpTlvGroup,
       "lldpV2ExtLrpTcpTlvGroup": lldpV2ExtLrpTcpTlvGroup}
)
