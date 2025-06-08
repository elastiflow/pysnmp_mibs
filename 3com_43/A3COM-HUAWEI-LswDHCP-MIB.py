# SNMP MIB module (A3COM-HUAWEI-LswDHCP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/3com_43/A3COM-HUAWEI-LswDHCP-MIB.mib
# Produced by pysmi-1.6.1 at Thu Jun  5 23:04:06 2025
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

(lswCommon,) = mibBuilder.importSymbols(
    "A3COM-HUAWEI-OID-MIB",
    "lswCommon")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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

hwLswDhcpMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 8)
)
if mibBuilder.loadTexts:
    hwLswDhcpMib.setRevisions(
        ("2001-06-29 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwLswDhcpMibObject_ObjectIdentity = ObjectIdentity
hwLswDhcpMibObject = _HwLswDhcpMibObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 8, 1)
)
_HwDhcpGroupTable_Object = MibTable
hwDhcpGroupTable = _HwDhcpGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 8, 1, 1)
)
if mibBuilder.loadTexts:
    hwDhcpGroupTable.setStatus("current")
_HwDhcpGroupEntry_Object = MibTableRow
hwDhcpGroupEntry = _HwDhcpGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 8, 1, 1, 1)
)
hwDhcpGroupEntry.setIndexNames(
    (0, "A3COM-HUAWEI-LswDHCP-MIB", "hwDhcpGroupID"),
)
if mibBuilder.loadTexts:
    hwDhcpGroupEntry.setStatus("current")


class _HwDhcpGroupID_Type(Integer32):
    """Custom type hwDhcpGroupID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 19),
    )


_HwDhcpGroupID_Type.__name__ = "Integer32"
_HwDhcpGroupID_Object = MibTableColumn
hwDhcpGroupID = _HwDhcpGroupID_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 8, 1, 1, 1, 1),
    _HwDhcpGroupID_Type()
)
hwDhcpGroupID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDhcpGroupID.setStatus("current")
_HwIpDhcpServerAddress1_Type = IpAddress
_HwIpDhcpServerAddress1_Object = MibTableColumn
hwIpDhcpServerAddress1 = _HwIpDhcpServerAddress1_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 8, 1, 1, 1, 2),
    _HwIpDhcpServerAddress1_Type()
)
hwIpDhcpServerAddress1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIpDhcpServerAddress1.setStatus("current")
_HwIpDhcpServerAddress2_Type = IpAddress
_HwIpDhcpServerAddress2_Object = MibTableColumn
hwIpDhcpServerAddress2 = _HwIpDhcpServerAddress2_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 8, 1, 1, 1, 3),
    _HwIpDhcpServerAddress2_Type()
)
hwIpDhcpServerAddress2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIpDhcpServerAddress2.setStatus("current")
_HwDhcpRowStatus_Type = RowStatus
_HwDhcpRowStatus_Object = MibTableColumn
hwDhcpRowStatus = _HwDhcpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 8, 1, 1, 1, 4),
    _HwDhcpRowStatus_Type()
)
hwDhcpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDhcpRowStatus.setStatus("current")
_HwDhcpSecurityTable_Object = MibTable
hwDhcpSecurityTable = _HwDhcpSecurityTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 8, 1, 2)
)
if mibBuilder.loadTexts:
    hwDhcpSecurityTable.setStatus("current")
_HwDhcpSecurityEntry_Object = MibTableRow
hwDhcpSecurityEntry = _HwDhcpSecurityEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 8, 1, 2, 1)
)
hwDhcpSecurityEntry.setIndexNames(
    (0, "A3COM-HUAWEI-LswDHCP-MIB", "hwDhcpClientIpAddress"),
)
if mibBuilder.loadTexts:
    hwDhcpSecurityEntry.setStatus("current")
_HwDhcpClientIpAddress_Type = IpAddress
_HwDhcpClientIpAddress_Object = MibTableColumn
hwDhcpClientIpAddress = _HwDhcpClientIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 8, 1, 2, 1, 1),
    _HwDhcpClientIpAddress_Type()
)
hwDhcpClientIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDhcpClientIpAddress.setStatus("current")
_HwDhcpClientMacAddress_Type = MacAddress
_HwDhcpClientMacAddress_Object = MibTableColumn
hwDhcpClientMacAddress = _HwDhcpClientMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 8, 1, 2, 1, 2),
    _HwDhcpClientMacAddress_Type()
)
hwDhcpClientMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDhcpClientMacAddress.setStatus("current")


class _HwDhcpClientProperty_Type(Integer32):
    """Custom type hwDhcpClientProperty based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("dynamic", 2))
    )


_HwDhcpClientProperty_Type.__name__ = "Integer32"
_HwDhcpClientProperty_Object = MibTableColumn
hwDhcpClientProperty = _HwDhcpClientProperty_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 8, 1, 2, 1, 3),
    _HwDhcpClientProperty_Type()
)
hwDhcpClientProperty.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDhcpClientProperty.setStatus("current")
_HwDhcpClientRowStatus_Type = RowStatus
_HwDhcpClientRowStatus_Object = MibTableColumn
hwDhcpClientRowStatus = _HwDhcpClientRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 8, 1, 2, 1, 4),
    _HwDhcpClientRowStatus_Type()
)
hwDhcpClientRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDhcpClientRowStatus.setStatus("current")
_HwDhcpToL3IfTable_Object = MibTable
hwDhcpToL3IfTable = _HwDhcpToL3IfTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 8, 1, 3)
)
if mibBuilder.loadTexts:
    hwDhcpToL3IfTable.setStatus("current")
_HwDhcpToL3IfEntry_Object = MibTableRow
hwDhcpToL3IfEntry = _HwDhcpToL3IfEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 8, 1, 3, 1)
)
hwDhcpToL3IfEntry.setIndexNames(
    (0, "A3COM-HUAWEI-LswDHCP-MIB", "hwDhcpToL3VlanIfIndex"),
)
if mibBuilder.loadTexts:
    hwDhcpToL3IfEntry.setStatus("current")
_HwDhcpToL3VlanIfIndex_Type = Integer32
_HwDhcpToL3VlanIfIndex_Object = MibTableColumn
hwDhcpToL3VlanIfIndex = _HwDhcpToL3VlanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 8, 1, 3, 1, 1),
    _HwDhcpToL3VlanIfIndex_Type()
)
hwDhcpToL3VlanIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDhcpToL3VlanIfIndex.setStatus("current")


class _HwDhcpToL3GroupId_Type(Integer32):
    """Custom type hwDhcpToL3GroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 19),
    )


_HwDhcpToL3GroupId_Type.__name__ = "Integer32"
_HwDhcpToL3GroupId_Object = MibTableColumn
hwDhcpToL3GroupId = _HwDhcpToL3GroupId_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 8, 1, 3, 1, 2),
    _HwDhcpToL3GroupId_Type()
)
hwDhcpToL3GroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDhcpToL3GroupId.setStatus("current")


class _HwDhcpToL3AddressCheck_Type(Integer32):
    """Custom type hwDhcpToL3AddressCheck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_HwDhcpToL3AddressCheck_Type.__name__ = "Integer32"
_HwDhcpToL3AddressCheck_Object = MibTableColumn
hwDhcpToL3AddressCheck = _HwDhcpToL3AddressCheck_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 8, 1, 3, 1, 3),
    _HwDhcpToL3AddressCheck_Type()
)
hwDhcpToL3AddressCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDhcpToL3AddressCheck.setStatus("current")
_HwDhcpToL3RowStatus_Type = RowStatus
_HwDhcpToL3RowStatus_Object = MibTableColumn
hwDhcpToL3RowStatus = _HwDhcpToL3RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 8, 1, 3, 1, 4),
    _HwDhcpToL3RowStatus_Type()
)
hwDhcpToL3RowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDhcpToL3RowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-HUAWEI-LswDHCP-MIB",
    **{"hwLswDhcpMib": hwLswDhcpMib,
       "hwLswDhcpMibObject": hwLswDhcpMibObject,
       "hwDhcpGroupTable": hwDhcpGroupTable,
       "hwDhcpGroupEntry": hwDhcpGroupEntry,
       "hwDhcpGroupID": hwDhcpGroupID,
       "hwIpDhcpServerAddress1": hwIpDhcpServerAddress1,
       "hwIpDhcpServerAddress2": hwIpDhcpServerAddress2,
       "hwDhcpRowStatus": hwDhcpRowStatus,
       "hwDhcpSecurityTable": hwDhcpSecurityTable,
       "hwDhcpSecurityEntry": hwDhcpSecurityEntry,
       "hwDhcpClientIpAddress": hwDhcpClientIpAddress,
       "hwDhcpClientMacAddress": hwDhcpClientMacAddress,
       "hwDhcpClientProperty": hwDhcpClientProperty,
       "hwDhcpClientRowStatus": hwDhcpClientRowStatus,
       "hwDhcpToL3IfTable": hwDhcpToL3IfTable,
       "hwDhcpToL3IfEntry": hwDhcpToL3IfEntry,
       "hwDhcpToL3VlanIfIndex": hwDhcpToL3VlanIfIndex,
       "hwDhcpToL3GroupId": hwDhcpToL3GroupId,
       "hwDhcpToL3AddressCheck": hwDhcpToL3AddressCheck,
       "hwDhcpToL3RowStatus": hwDhcpToL3RowStatus}
)
