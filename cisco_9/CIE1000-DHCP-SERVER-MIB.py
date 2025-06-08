# SNMP MIB module (CIE1000-DHCP-SERVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CIE1000-DHCP-SERVER-MIB.mib
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

(CIE1000DisplayString,
 CIE1000InterfaceIndex,
 CIE1000RowEditorState,
 CIE1000Unsigned16) = mibBuilder.importSymbols(
    "CIE1000-TC",
    "CIE1000DisplayString",
    "CIE1000InterfaceIndex",
    "CIE1000RowEditorState",
    "CIE1000Unsigned16")

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

cie1000DhcpServerMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109)
)
if mibBuilder.loadTexts:
    cie1000DhcpServerMib.setRevisions(
        ("2015-08-24 00:00",
         "2014-11-27 00:00",
         "2014-07-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class CIE1000DhcpServerBindingEnum(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("automatic", 1),
          ("manual", 2),
          ("expired", 3))
    )



class CIE1000DhcpServerBindingStateEnum(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("allocated", 1),
          ("committed", 2),
          ("expired", 3))
    )



class CIE1000DhcpServerClientIdentifierEnum(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("name", 1),
          ("mac", 2))
    )



class CIE1000DhcpServerNetbiosNodeEnum(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("nodeNone", 0),
          ("nodeB", 1),
          ("nodeP", 2),
          ("nodeM", 3),
          ("nodeH", 4))
    )



class CIE1000DhcpServerPoolEnum(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("network", 1),
          ("host", 2))
    )



# MIB Managed Objects in the order of their OIDs

_Cie1000DhcpServerMibObjects_ObjectIdentity = ObjectIdentity
cie1000DhcpServerMibObjects = _Cie1000DhcpServerMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1)
)
_Cie1000DhcpServerConfig_ObjectIdentity = ObjectIdentity
cie1000DhcpServerConfig = _Cie1000DhcpServerConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2)
)
_Cie1000DhcpServerConfigGlobals_ObjectIdentity = ObjectIdentity
cie1000DhcpServerConfigGlobals = _Cie1000DhcpServerConfigGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 1)
)
_Cie1000DhcpServerConfigGlobalsMode_Type = TruthValue
_Cie1000DhcpServerConfigGlobalsMode_Object = MibScalar
cie1000DhcpServerConfigGlobalsMode = _Cie1000DhcpServerConfigGlobalsMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 1, 1),
    _Cie1000DhcpServerConfigGlobalsMode_Type()
)
cie1000DhcpServerConfigGlobalsMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigGlobalsMode.setStatus("current")
_Cie1000DhcpServerConfigVlanTable_Object = MibTable
cie1000DhcpServerConfigVlanTable = _Cie1000DhcpServerConfigVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigVlanTable.setStatus("current")
_Cie1000DhcpServerConfigVlanEntry_Object = MibTableRow
cie1000DhcpServerConfigVlanEntry = _Cie1000DhcpServerConfigVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 2, 1)
)
cie1000DhcpServerConfigVlanEntry.setIndexNames(
    (0, "CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigVlanIfIndex"),
)
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigVlanEntry.setStatus("current")
_Cie1000DhcpServerConfigVlanIfIndex_Type = CIE1000InterfaceIndex
_Cie1000DhcpServerConfigVlanIfIndex_Object = MibTableColumn
cie1000DhcpServerConfigVlanIfIndex = _Cie1000DhcpServerConfigVlanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 2, 1, 1),
    _Cie1000DhcpServerConfigVlanIfIndex_Type()
)
cie1000DhcpServerConfigVlanIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigVlanIfIndex.setStatus("current")
_Cie1000DhcpServerConfigVlanMode_Type = TruthValue
_Cie1000DhcpServerConfigVlanMode_Object = MibTableColumn
cie1000DhcpServerConfigVlanMode = _Cie1000DhcpServerConfigVlanMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 2, 1, 2),
    _Cie1000DhcpServerConfigVlanMode_Type()
)
cie1000DhcpServerConfigVlanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigVlanMode.setStatus("current")
_Cie1000DhcpServerConfigExcludedTable_Object = MibTable
cie1000DhcpServerConfigExcludedTable = _Cie1000DhcpServerConfigExcludedTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 3)
)
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigExcludedTable.setStatus("current")
_Cie1000DhcpServerConfigExcludedEntry_Object = MibTableRow
cie1000DhcpServerConfigExcludedEntry = _Cie1000DhcpServerConfigExcludedEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 3, 1)
)
cie1000DhcpServerConfigExcludedEntry.setIndexNames(
    (0, "CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigExcludedLowIpAddress"),
    (0, "CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigExcludedHighIpAddress"),
)
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigExcludedEntry.setStatus("current")
_Cie1000DhcpServerConfigExcludedLowIpAddress_Type = IpAddress
_Cie1000DhcpServerConfigExcludedLowIpAddress_Object = MibTableColumn
cie1000DhcpServerConfigExcludedLowIpAddress = _Cie1000DhcpServerConfigExcludedLowIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 3, 1, 1),
    _Cie1000DhcpServerConfigExcludedLowIpAddress_Type()
)
cie1000DhcpServerConfigExcludedLowIpAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigExcludedLowIpAddress.setStatus("current")
_Cie1000DhcpServerConfigExcludedHighIpAddress_Type = IpAddress
_Cie1000DhcpServerConfigExcludedHighIpAddress_Object = MibTableColumn
cie1000DhcpServerConfigExcludedHighIpAddress = _Cie1000DhcpServerConfigExcludedHighIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 3, 1, 2),
    _Cie1000DhcpServerConfigExcludedHighIpAddress_Type()
)
cie1000DhcpServerConfigExcludedHighIpAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigExcludedHighIpAddress.setStatus("current")
_Cie1000DhcpServerConfigExcludedAction_Type = CIE1000RowEditorState
_Cie1000DhcpServerConfigExcludedAction_Object = MibTableColumn
cie1000DhcpServerConfigExcludedAction = _Cie1000DhcpServerConfigExcludedAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 3, 1, 100),
    _Cie1000DhcpServerConfigExcludedAction_Type()
)
cie1000DhcpServerConfigExcludedAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigExcludedAction.setStatus("current")
_Cie1000DhcpServerConfigExcludedIpTableRowEditor_ObjectIdentity = ObjectIdentity
cie1000DhcpServerConfigExcludedIpTableRowEditor = _Cie1000DhcpServerConfigExcludedIpTableRowEditor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 4)
)
_Cie1000DhcpServerConfigExcludedIpTableRowEditorLowIpAddress_Type = IpAddress
_Cie1000DhcpServerConfigExcludedIpTableRowEditorLowIpAddress_Object = MibScalar
cie1000DhcpServerConfigExcludedIpTableRowEditorLowIpAddress = _Cie1000DhcpServerConfigExcludedIpTableRowEditorLowIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 4, 1),
    _Cie1000DhcpServerConfigExcludedIpTableRowEditorLowIpAddress_Type()
)
cie1000DhcpServerConfigExcludedIpTableRowEditorLowIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigExcludedIpTableRowEditorLowIpAddress.setStatus("current")
_Cie1000DhcpServerConfigExcludedIpTableRowEditorHighIpAddress_Type = IpAddress
_Cie1000DhcpServerConfigExcludedIpTableRowEditorHighIpAddress_Object = MibScalar
cie1000DhcpServerConfigExcludedIpTableRowEditorHighIpAddress = _Cie1000DhcpServerConfigExcludedIpTableRowEditorHighIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 4, 2),
    _Cie1000DhcpServerConfigExcludedIpTableRowEditorHighIpAddress_Type()
)
cie1000DhcpServerConfigExcludedIpTableRowEditorHighIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigExcludedIpTableRowEditorHighIpAddress.setStatus("current")
_Cie1000DhcpServerConfigExcludedIpTableRowEditorAction_Type = CIE1000RowEditorState
_Cie1000DhcpServerConfigExcludedIpTableRowEditorAction_Object = MibScalar
cie1000DhcpServerConfigExcludedIpTableRowEditorAction = _Cie1000DhcpServerConfigExcludedIpTableRowEditorAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 4, 100),
    _Cie1000DhcpServerConfigExcludedIpTableRowEditorAction_Type()
)
cie1000DhcpServerConfigExcludedIpTableRowEditorAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigExcludedIpTableRowEditorAction.setStatus("current")
_Cie1000DhcpServerConfigPoolTable_Object = MibTable
cie1000DhcpServerConfigPoolTable = _Cie1000DhcpServerConfigPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 5)
)
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigPoolTable.setStatus("current")
_Cie1000DhcpServerConfigPoolEntry_Object = MibTableRow
cie1000DhcpServerConfigPoolEntry = _Cie1000DhcpServerConfigPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 5, 1)
)
cie1000DhcpServerConfigPoolEntry.setIndexNames(
    (0, "CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigPoolPoolName"),
)
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigPoolEntry.setStatus("current")


class _Cie1000DhcpServerConfigPoolPoolName_Type(CIE1000DisplayString):
    """Custom type cie1000DhcpServerConfigPoolPoolName based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Cie1000DhcpServerConfigPoolPoolName_Type.__name__ = "CIE1000DisplayString"
_Cie1000DhcpServerConfigPoolPoolName_Object = MibTableColumn
cie1000DhcpServerConfigPoolPoolName = _Cie1000DhcpServerConfigPoolPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 5, 1, 1),
    _Cie1000DhcpServerConfigPoolPoolName_Type()
)
cie1000DhcpServerConfigPoolPoolName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigPoolPoolName.setStatus("current")
_Cie1000DhcpServerConfigPoolPoolType_Type = CIE1000DhcpServerPoolEnum
_Cie1000DhcpServerConfigPoolPoolType_Object = MibTableColumn
cie1000DhcpServerConfigPoolPoolType = _Cie1000DhcpServerConfigPoolPoolType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 5, 1, 2),
    _Cie1000DhcpServerConfigPoolPoolType_Type()
)
cie1000DhcpServerConfigPoolPoolType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigPoolPoolType.setStatus("current")
_Cie1000DhcpServerConfigPoolIpv4Address_Type = IpAddress
_Cie1000DhcpServerConfigPoolIpv4Address_Object = MibTableColumn
cie1000DhcpServerConfigPoolIpv4Address = _Cie1000DhcpServerConfigPoolIpv4Address_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 5, 1, 3),
    _Cie1000DhcpServerConfigPoolIpv4Address_Type()
)
cie1000DhcpServerConfigPoolIpv4Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigPoolIpv4Address.setStatus("current")
_Cie1000DhcpServerConfigPoolSubnetMask_Type = IpAddress
_Cie1000DhcpServerConfigPoolSubnetMask_Object = MibTableColumn
cie1000DhcpServerConfigPoolSubnetMask = _Cie1000DhcpServerConfigPoolSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 5, 1, 4),
    _Cie1000DhcpServerConfigPoolSubnetMask_Type()
)
cie1000DhcpServerConfigPoolSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigPoolSubnetMask.setStatus("current")
_Cie1000DhcpServerConfigPoolSubnetBroadcast_Type = IpAddress
_Cie1000DhcpServerConfigPoolSubnetBroadcast_Object = MibTableColumn
cie1000DhcpServerConfigPoolSubnetBroadcast = _Cie1000DhcpServerConfigPoolSubnetBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 5, 1, 5),
    _Cie1000DhcpServerConfigPoolSubnetBroadcast_Type()
)
cie1000DhcpServerConfigPoolSubnetBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigPoolSubnetBroadcast.setStatus("current")
_Cie1000DhcpServerConfigPoolLeaseDay_Type = Unsigned32
_Cie1000DhcpServerConfigPoolLeaseDay_Object = MibTableColumn
cie1000DhcpServerConfigPoolLeaseDay = _Cie1000DhcpServerConfigPoolLeaseDay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 5, 1, 6),
    _Cie1000DhcpServerConfigPoolLeaseDay_Type()
)
cie1000DhcpServerConfigPoolLeaseDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigPoolLeaseDay.setStatus("current")
_Cie1000DhcpServerConfigPoolLeaseHour_Type = Unsigned32
_Cie1000DhcpServerConfigPoolLeaseHour_Object = MibTableColumn
cie1000DhcpServerConfigPoolLeaseHour = _Cie1000DhcpServerConfigPoolLeaseHour_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 5, 1, 7),
    _Cie1000DhcpServerConfigPoolLeaseHour_Type()
)
cie1000DhcpServerConfigPoolLeaseHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigPoolLeaseHour.setStatus("current")
_Cie1000DhcpServerConfigPoolLeaseMinute_Type = Unsigned32
_Cie1000DhcpServerConfigPoolLeaseMinute_Object = MibTableColumn
cie1000DhcpServerConfigPoolLeaseMinute = _Cie1000DhcpServerConfigPoolLeaseMinute_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 5, 1, 8),
    _Cie1000DhcpServerConfigPoolLeaseMinute_Type()
)
cie1000DhcpServerConfigPoolLeaseMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigPoolLeaseMinute.setStatus("current")


class _Cie1000DhcpServerConfigPoolDomainName_Type(CIE1000DisplayString):
    """Custom type cie1000DhcpServerConfigPoolDomainName based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Cie1000DhcpServerConfigPoolDomainName_Type.__name__ = "CIE1000DisplayString"
_Cie1000DhcpServerConfigPoolDomainName_Object = MibTableColumn
cie1000DhcpServerConfigPoolDomainName = _Cie1000DhcpServerConfigPoolDomainName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 5, 1, 9),
    _Cie1000DhcpServerConfigPoolDomainName_Type()
)
cie1000DhcpServerConfigPoolDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigPoolDomainName.setStatus("current")
_Cie1000DhcpServerConfigPoolDefaultRouter1_Type = IpAddress
_Cie1000DhcpServerConfigPoolDefaultRouter1_Object = MibTableColumn
cie1000DhcpServerConfigPoolDefaultRouter1 = _Cie1000DhcpServerConfigPoolDefaultRouter1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 5, 1, 10),
    _Cie1000DhcpServerConfigPoolDefaultRouter1_Type()
)
cie1000DhcpServerConfigPoolDefaultRouter1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigPoolDefaultRouter1.setStatus("current")
_Cie1000DhcpServerConfigPoolDefaultRouter2_Type = IpAddress
_Cie1000DhcpServerConfigPoolDefaultRouter2_Object = MibTableColumn
cie1000DhcpServerConfigPoolDefaultRouter2 = _Cie1000DhcpServerConfigPoolDefaultRouter2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 5, 1, 11),
    _Cie1000DhcpServerConfigPoolDefaultRouter2_Type()
)
cie1000DhcpServerConfigPoolDefaultRouter2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigPoolDefaultRouter2.setStatus("current")
_Cie1000DhcpServerConfigPoolDefaultRouter3_Type = IpAddress
_Cie1000DhcpServerConfigPoolDefaultRouter3_Object = MibTableColumn
cie1000DhcpServerConfigPoolDefaultRouter3 = _Cie1000DhcpServerConfigPoolDefaultRouter3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 5, 1, 12),
    _Cie1000DhcpServerConfigPoolDefaultRouter3_Type()
)
cie1000DhcpServerConfigPoolDefaultRouter3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigPoolDefaultRouter3.setStatus("current")
_Cie1000DhcpServerConfigPoolDefaultRouter4_Type = IpAddress
_Cie1000DhcpServerConfigPoolDefaultRouter4_Object = MibTableColumn
cie1000DhcpServerConfigPoolDefaultRouter4 = _Cie1000DhcpServerConfigPoolDefaultRouter4_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 5, 1, 13),
    _Cie1000DhcpServerConfigPoolDefaultRouter4_Type()
)
cie1000DhcpServerConfigPoolDefaultRouter4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigPoolDefaultRouter4.setStatus("current")
_Cie1000DhcpServerConfigPoolDnsServer1_Type = IpAddress
_Cie1000DhcpServerConfigPoolDnsServer1_Object = MibTableColumn
cie1000DhcpServerConfigPoolDnsServer1 = _Cie1000DhcpServerConfigPoolDnsServer1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 5, 1, 14),
    _Cie1000DhcpServerConfigPoolDnsServer1_Type()
)
cie1000DhcpServerConfigPoolDnsServer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigPoolDnsServer1.setStatus("current")
_Cie1000DhcpServerConfigPoolDnsServer2_Type = IpAddress
_Cie1000DhcpServerConfigPoolDnsServer2_Object = MibTableColumn
cie1000DhcpServerConfigPoolDnsServer2 = _Cie1000DhcpServerConfigPoolDnsServer2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 5, 1, 15),
    _Cie1000DhcpServerConfigPoolDnsServer2_Type()
)
cie1000DhcpServerConfigPoolDnsServer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigPoolDnsServer2.setStatus("current")
_Cie1000DhcpServerConfigPoolDnsServer3_Type = IpAddress
_Cie1000DhcpServerConfigPoolDnsServer3_Object = MibTableColumn
cie1000DhcpServerConfigPoolDnsServer3 = _Cie1000DhcpServerConfigPoolDnsServer3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 5, 1, 16),
    _Cie1000DhcpServerConfigPoolDnsServer3_Type()
)
cie1000DhcpServerConfigPoolDnsServer3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigPoolDnsServer3.setStatus("current")
_Cie1000DhcpServerConfigPoolDnsServer4_Type = IpAddress
_Cie1000DhcpServerConfigPoolDnsServer4_Object = MibTableColumn
cie1000DhcpServerConfigPoolDnsServer4 = _Cie1000DhcpServerConfigPoolDnsServer4_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 5, 1, 17),
    _Cie1000DhcpServerConfigPoolDnsServer4_Type()
)
cie1000DhcpServerConfigPoolDnsServer4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigPoolDnsServer4.setStatus("current")
_Cie1000DhcpServerConfigPoolNtpServer1_Type = IpAddress
_Cie1000DhcpServerConfigPoolNtpServer1_Object = MibTableColumn
cie1000DhcpServerConfigPoolNtpServer1 = _Cie1000DhcpServerConfigPoolNtpServer1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 5, 1, 18),
    _Cie1000DhcpServerConfigPoolNtpServer1_Type()
)
cie1000DhcpServerConfigPoolNtpServer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigPoolNtpServer1.setStatus("current")
_Cie1000DhcpServerConfigPoolNtpServer2_Type = IpAddress
_Cie1000DhcpServerConfigPoolNtpServer2_Object = MibTableColumn
cie1000DhcpServerConfigPoolNtpServer2 = _Cie1000DhcpServerConfigPoolNtpServer2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 5, 1, 19),
    _Cie1000DhcpServerConfigPoolNtpServer2_Type()
)
cie1000DhcpServerConfigPoolNtpServer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigPoolNtpServer2.setStatus("current")
_Cie1000DhcpServerConfigPoolNtpServer3_Type = IpAddress
_Cie1000DhcpServerConfigPoolNtpServer3_Object = MibTableColumn
cie1000DhcpServerConfigPoolNtpServer3 = _Cie1000DhcpServerConfigPoolNtpServer3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 5, 1, 20),
    _Cie1000DhcpServerConfigPoolNtpServer3_Type()
)
cie1000DhcpServerConfigPoolNtpServer3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigPoolNtpServer3.setStatus("current")
_Cie1000DhcpServerConfigPoolNtpServer4_Type = IpAddress
_Cie1000DhcpServerConfigPoolNtpServer4_Object = MibTableColumn
cie1000DhcpServerConfigPoolNtpServer4 = _Cie1000DhcpServerConfigPoolNtpServer4_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 5, 1, 21),
    _Cie1000DhcpServerConfigPoolNtpServer4_Type()
)
cie1000DhcpServerConfigPoolNtpServer4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigPoolNtpServer4.setStatus("current")
_Cie1000DhcpServerConfigPoolNetbiosNodeType_Type = CIE1000DhcpServerNetbiosNodeEnum
_Cie1000DhcpServerConfigPoolNetbiosNodeType_Object = MibTableColumn
cie1000DhcpServerConfigPoolNetbiosNodeType = _Cie1000DhcpServerConfigPoolNetbiosNodeType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 5, 1, 22),
    _Cie1000DhcpServerConfigPoolNetbiosNodeType_Type()
)
cie1000DhcpServerConfigPoolNetbiosNodeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigPoolNetbiosNodeType.setStatus("current")


class _Cie1000DhcpServerConfigPoolNetbiosScope_Type(CIE1000DisplayString):
    """Custom type cie1000DhcpServerConfigPoolNetbiosScope based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Cie1000DhcpServerConfigPoolNetbiosScope_Type.__name__ = "CIE1000DisplayString"
_Cie1000DhcpServerConfigPoolNetbiosScope_Object = MibTableColumn
cie1000DhcpServerConfigPoolNetbiosScope = _Cie1000DhcpServerConfigPoolNetbiosScope_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 5, 1, 23),
    _Cie1000DhcpServerConfigPoolNetbiosScope_Type()
)
cie1000DhcpServerConfigPoolNetbiosScope.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigPoolNetbiosScope.setStatus("current")
_Cie1000DhcpServerConfigPoolNetbiosNameServer1_Type = IpAddress
_Cie1000DhcpServerConfigPoolNetbiosNameServer1_Object = MibTableColumn
cie1000DhcpServerConfigPoolNetbiosNameServer1 = _Cie1000DhcpServerConfigPoolNetbiosNameServer1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 5, 1, 24),
    _Cie1000DhcpServerConfigPoolNetbiosNameServer1_Type()
)
cie1000DhcpServerConfigPoolNetbiosNameServer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigPoolNetbiosNameServer1.setStatus("current")
_Cie1000DhcpServerConfigPoolNetbiosNameServer2_Type = IpAddress
_Cie1000DhcpServerConfigPoolNetbiosNameServer2_Object = MibTableColumn
cie1000DhcpServerConfigPoolNetbiosNameServer2 = _Cie1000DhcpServerConfigPoolNetbiosNameServer2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 5, 1, 25),
    _Cie1000DhcpServerConfigPoolNetbiosNameServer2_Type()
)
cie1000DhcpServerConfigPoolNetbiosNameServer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigPoolNetbiosNameServer2.setStatus("current")
_Cie1000DhcpServerConfigPoolNetbiosNameServer3_Type = IpAddress
_Cie1000DhcpServerConfigPoolNetbiosNameServer3_Object = MibTableColumn
cie1000DhcpServerConfigPoolNetbiosNameServer3 = _Cie1000DhcpServerConfigPoolNetbiosNameServer3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 5, 1, 26),
    _Cie1000DhcpServerConfigPoolNetbiosNameServer3_Type()
)
cie1000DhcpServerConfigPoolNetbiosNameServer3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigPoolNetbiosNameServer3.setStatus("current")
_Cie1000DhcpServerConfigPoolNetbiosNameServer4_Type = IpAddress
_Cie1000DhcpServerConfigPoolNetbiosNameServer4_Object = MibTableColumn
cie1000DhcpServerConfigPoolNetbiosNameServer4 = _Cie1000DhcpServerConfigPoolNetbiosNameServer4_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 5, 1, 27),
    _Cie1000DhcpServerConfigPoolNetbiosNameServer4_Type()
)
cie1000DhcpServerConfigPoolNetbiosNameServer4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigPoolNetbiosNameServer4.setStatus("current")


class _Cie1000DhcpServerConfigPoolNisDomainName_Type(CIE1000DisplayString):
    """Custom type cie1000DhcpServerConfigPoolNisDomainName based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Cie1000DhcpServerConfigPoolNisDomainName_Type.__name__ = "CIE1000DisplayString"
_Cie1000DhcpServerConfigPoolNisDomainName_Object = MibTableColumn
cie1000DhcpServerConfigPoolNisDomainName = _Cie1000DhcpServerConfigPoolNisDomainName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 5, 1, 28),
    _Cie1000DhcpServerConfigPoolNisDomainName_Type()
)
cie1000DhcpServerConfigPoolNisDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigPoolNisDomainName.setStatus("current")
_Cie1000DhcpServerConfigPoolNisServer1_Type = IpAddress
_Cie1000DhcpServerConfigPoolNisServer1_Object = MibTableColumn
cie1000DhcpServerConfigPoolNisServer1 = _Cie1000DhcpServerConfigPoolNisServer1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 5, 1, 29),
    _Cie1000DhcpServerConfigPoolNisServer1_Type()
)
cie1000DhcpServerConfigPoolNisServer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigPoolNisServer1.setStatus("current")
_Cie1000DhcpServerConfigPoolNisServer2_Type = IpAddress
_Cie1000DhcpServerConfigPoolNisServer2_Object = MibTableColumn
cie1000DhcpServerConfigPoolNisServer2 = _Cie1000DhcpServerConfigPoolNisServer2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 5, 1, 30),
    _Cie1000DhcpServerConfigPoolNisServer2_Type()
)
cie1000DhcpServerConfigPoolNisServer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigPoolNisServer2.setStatus("current")
_Cie1000DhcpServerConfigPoolNisServer3_Type = IpAddress
_Cie1000DhcpServerConfigPoolNisServer3_Object = MibTableColumn
cie1000DhcpServerConfigPoolNisServer3 = _Cie1000DhcpServerConfigPoolNisServer3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 5, 1, 31),
    _Cie1000DhcpServerConfigPoolNisServer3_Type()
)
cie1000DhcpServerConfigPoolNisServer3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigPoolNisServer3.setStatus("current")
_Cie1000DhcpServerConfigPoolNisServer4_Type = IpAddress
_Cie1000DhcpServerConfigPoolNisServer4_Object = MibTableColumn
cie1000DhcpServerConfigPoolNisServer4 = _Cie1000DhcpServerConfigPoolNisServer4_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 5, 1, 32),
    _Cie1000DhcpServerConfigPoolNisServer4_Type()
)
cie1000DhcpServerConfigPoolNisServer4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigPoolNisServer4.setStatus("current")
_Cie1000DhcpServerConfigPoolClientIdentifierType_Type = CIE1000DhcpServerClientIdentifierEnum
_Cie1000DhcpServerConfigPoolClientIdentifierType_Object = MibTableColumn
cie1000DhcpServerConfigPoolClientIdentifierType = _Cie1000DhcpServerConfigPoolClientIdentifierType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 5, 1, 33),
    _Cie1000DhcpServerConfigPoolClientIdentifierType_Type()
)
cie1000DhcpServerConfigPoolClientIdentifierType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigPoolClientIdentifierType.setStatus("current")


class _Cie1000DhcpServerConfigPoolClientIdentifierName_Type(CIE1000DisplayString):
    """Custom type cie1000DhcpServerConfigPoolClientIdentifierName based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Cie1000DhcpServerConfigPoolClientIdentifierName_Type.__name__ = "CIE1000DisplayString"
_Cie1000DhcpServerConfigPoolClientIdentifierName_Object = MibTableColumn
cie1000DhcpServerConfigPoolClientIdentifierName = _Cie1000DhcpServerConfigPoolClientIdentifierName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 5, 1, 34),
    _Cie1000DhcpServerConfigPoolClientIdentifierName_Type()
)
cie1000DhcpServerConfigPoolClientIdentifierName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigPoolClientIdentifierName.setStatus("current")
_Cie1000DhcpServerConfigPoolClientIdentifierMac_Type = MacAddress
_Cie1000DhcpServerConfigPoolClientIdentifierMac_Object = MibTableColumn
cie1000DhcpServerConfigPoolClientIdentifierMac = _Cie1000DhcpServerConfigPoolClientIdentifierMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 5, 1, 35),
    _Cie1000DhcpServerConfigPoolClientIdentifierMac_Type()
)
cie1000DhcpServerConfigPoolClientIdentifierMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigPoolClientIdentifierMac.setStatus("current")
_Cie1000DhcpServerConfigPoolClientHardwareAddress_Type = MacAddress
_Cie1000DhcpServerConfigPoolClientHardwareAddress_Object = MibTableColumn
cie1000DhcpServerConfigPoolClientHardwareAddress = _Cie1000DhcpServerConfigPoolClientHardwareAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 5, 1, 36),
    _Cie1000DhcpServerConfigPoolClientHardwareAddress_Type()
)
cie1000DhcpServerConfigPoolClientHardwareAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigPoolClientHardwareAddress.setStatus("current")


class _Cie1000DhcpServerConfigPoolClientName_Type(CIE1000DisplayString):
    """Custom type cie1000DhcpServerConfigPoolClientName based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Cie1000DhcpServerConfigPoolClientName_Type.__name__ = "CIE1000DisplayString"
_Cie1000DhcpServerConfigPoolClientName_Object = MibTableColumn
cie1000DhcpServerConfigPoolClientName = _Cie1000DhcpServerConfigPoolClientName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 5, 1, 37),
    _Cie1000DhcpServerConfigPoolClientName_Type()
)
cie1000DhcpServerConfigPoolClientName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigPoolClientName.setStatus("current")


class _Cie1000DhcpServerConfigPoolVendorClassId1_Type(CIE1000DisplayString):
    """Custom type cie1000DhcpServerConfigPoolVendorClassId1 based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Cie1000DhcpServerConfigPoolVendorClassId1_Type.__name__ = "CIE1000DisplayString"
_Cie1000DhcpServerConfigPoolVendorClassId1_Object = MibTableColumn
cie1000DhcpServerConfigPoolVendorClassId1 = _Cie1000DhcpServerConfigPoolVendorClassId1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 5, 1, 38),
    _Cie1000DhcpServerConfigPoolVendorClassId1_Type()
)
cie1000DhcpServerConfigPoolVendorClassId1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigPoolVendorClassId1.setStatus("current")


class _Cie1000DhcpServerConfigPoolVendorSpecificInfo1_Type(CIE1000DisplayString):
    """Custom type cie1000DhcpServerConfigPoolVendorSpecificInfo1 based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 66),
    )


_Cie1000DhcpServerConfigPoolVendorSpecificInfo1_Type.__name__ = "CIE1000DisplayString"
_Cie1000DhcpServerConfigPoolVendorSpecificInfo1_Object = MibTableColumn
cie1000DhcpServerConfigPoolVendorSpecificInfo1 = _Cie1000DhcpServerConfigPoolVendorSpecificInfo1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 5, 1, 39),
    _Cie1000DhcpServerConfigPoolVendorSpecificInfo1_Type()
)
cie1000DhcpServerConfigPoolVendorSpecificInfo1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigPoolVendorSpecificInfo1.setStatus("current")


class _Cie1000DhcpServerConfigPoolVendorClassId2_Type(CIE1000DisplayString):
    """Custom type cie1000DhcpServerConfigPoolVendorClassId2 based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Cie1000DhcpServerConfigPoolVendorClassId2_Type.__name__ = "CIE1000DisplayString"
_Cie1000DhcpServerConfigPoolVendorClassId2_Object = MibTableColumn
cie1000DhcpServerConfigPoolVendorClassId2 = _Cie1000DhcpServerConfigPoolVendorClassId2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 5, 1, 40),
    _Cie1000DhcpServerConfigPoolVendorClassId2_Type()
)
cie1000DhcpServerConfigPoolVendorClassId2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigPoolVendorClassId2.setStatus("current")


class _Cie1000DhcpServerConfigPoolVendorSpecificInfo2_Type(CIE1000DisplayString):
    """Custom type cie1000DhcpServerConfigPoolVendorSpecificInfo2 based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 66),
    )


_Cie1000DhcpServerConfigPoolVendorSpecificInfo2_Type.__name__ = "CIE1000DisplayString"
_Cie1000DhcpServerConfigPoolVendorSpecificInfo2_Object = MibTableColumn
cie1000DhcpServerConfigPoolVendorSpecificInfo2 = _Cie1000DhcpServerConfigPoolVendorSpecificInfo2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 5, 1, 41),
    _Cie1000DhcpServerConfigPoolVendorSpecificInfo2_Type()
)
cie1000DhcpServerConfigPoolVendorSpecificInfo2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigPoolVendorSpecificInfo2.setStatus("current")


class _Cie1000DhcpServerConfigPoolVendorClassId3_Type(CIE1000DisplayString):
    """Custom type cie1000DhcpServerConfigPoolVendorClassId3 based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Cie1000DhcpServerConfigPoolVendorClassId3_Type.__name__ = "CIE1000DisplayString"
_Cie1000DhcpServerConfigPoolVendorClassId3_Object = MibTableColumn
cie1000DhcpServerConfigPoolVendorClassId3 = _Cie1000DhcpServerConfigPoolVendorClassId3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 5, 1, 42),
    _Cie1000DhcpServerConfigPoolVendorClassId3_Type()
)
cie1000DhcpServerConfigPoolVendorClassId3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigPoolVendorClassId3.setStatus("current")


class _Cie1000DhcpServerConfigPoolVendorSpecificInfo3_Type(CIE1000DisplayString):
    """Custom type cie1000DhcpServerConfigPoolVendorSpecificInfo3 based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 66),
    )


_Cie1000DhcpServerConfigPoolVendorSpecificInfo3_Type.__name__ = "CIE1000DisplayString"
_Cie1000DhcpServerConfigPoolVendorSpecificInfo3_Object = MibTableColumn
cie1000DhcpServerConfigPoolVendorSpecificInfo3 = _Cie1000DhcpServerConfigPoolVendorSpecificInfo3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 5, 1, 43),
    _Cie1000DhcpServerConfigPoolVendorSpecificInfo3_Type()
)
cie1000DhcpServerConfigPoolVendorSpecificInfo3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigPoolVendorSpecificInfo3.setStatus("current")


class _Cie1000DhcpServerConfigPoolVendorClassId4_Type(CIE1000DisplayString):
    """Custom type cie1000DhcpServerConfigPoolVendorClassId4 based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Cie1000DhcpServerConfigPoolVendorClassId4_Type.__name__ = "CIE1000DisplayString"
_Cie1000DhcpServerConfigPoolVendorClassId4_Object = MibTableColumn
cie1000DhcpServerConfigPoolVendorClassId4 = _Cie1000DhcpServerConfigPoolVendorClassId4_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 5, 1, 44),
    _Cie1000DhcpServerConfigPoolVendorClassId4_Type()
)
cie1000DhcpServerConfigPoolVendorClassId4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigPoolVendorClassId4.setStatus("current")


class _Cie1000DhcpServerConfigPoolVendorSpecificInfo4_Type(CIE1000DisplayString):
    """Custom type cie1000DhcpServerConfigPoolVendorSpecificInfo4 based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 66),
    )


_Cie1000DhcpServerConfigPoolVendorSpecificInfo4_Type.__name__ = "CIE1000DisplayString"
_Cie1000DhcpServerConfigPoolVendorSpecificInfo4_Object = MibTableColumn
cie1000DhcpServerConfigPoolVendorSpecificInfo4 = _Cie1000DhcpServerConfigPoolVendorSpecificInfo4_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 5, 1, 45),
    _Cie1000DhcpServerConfigPoolVendorSpecificInfo4_Type()
)
cie1000DhcpServerConfigPoolVendorSpecificInfo4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigPoolVendorSpecificInfo4.setStatus("current")
_Cie1000DhcpServerConfigPoolAction_Type = CIE1000RowEditorState
_Cie1000DhcpServerConfigPoolAction_Object = MibTableColumn
cie1000DhcpServerConfigPoolAction = _Cie1000DhcpServerConfigPoolAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 5, 1, 100),
    _Cie1000DhcpServerConfigPoolAction_Type()
)
cie1000DhcpServerConfigPoolAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigPoolAction.setStatus("current")
_Cie1000DhcpServerConfigPoolTableRowEditor_ObjectIdentity = ObjectIdentity
cie1000DhcpServerConfigPoolTableRowEditor = _Cie1000DhcpServerConfigPoolTableRowEditor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 6)
)


class _Cie1000DhcpServerConfigPoolTableRowEditorPoolName_Type(CIE1000DisplayString):
    """Custom type cie1000DhcpServerConfigPoolTableRowEditorPoolName based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Cie1000DhcpServerConfigPoolTableRowEditorPoolName_Type.__name__ = "CIE1000DisplayString"
_Cie1000DhcpServerConfigPoolTableRowEditorPoolName_Object = MibScalar
cie1000DhcpServerConfigPoolTableRowEditorPoolName = _Cie1000DhcpServerConfigPoolTableRowEditorPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 6, 1),
    _Cie1000DhcpServerConfigPoolTableRowEditorPoolName_Type()
)
cie1000DhcpServerConfigPoolTableRowEditorPoolName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigPoolTableRowEditorPoolName.setStatus("current")
_Cie1000DhcpServerConfigPoolTableRowEditorPoolType_Type = CIE1000DhcpServerPoolEnum
_Cie1000DhcpServerConfigPoolTableRowEditorPoolType_Object = MibScalar
cie1000DhcpServerConfigPoolTableRowEditorPoolType = _Cie1000DhcpServerConfigPoolTableRowEditorPoolType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 6, 2),
    _Cie1000DhcpServerConfigPoolTableRowEditorPoolType_Type()
)
cie1000DhcpServerConfigPoolTableRowEditorPoolType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigPoolTableRowEditorPoolType.setStatus("current")
_Cie1000DhcpServerConfigPoolTableRowEditorIpv4Address_Type = IpAddress
_Cie1000DhcpServerConfigPoolTableRowEditorIpv4Address_Object = MibScalar
cie1000DhcpServerConfigPoolTableRowEditorIpv4Address = _Cie1000DhcpServerConfigPoolTableRowEditorIpv4Address_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 6, 3),
    _Cie1000DhcpServerConfigPoolTableRowEditorIpv4Address_Type()
)
cie1000DhcpServerConfigPoolTableRowEditorIpv4Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigPoolTableRowEditorIpv4Address.setStatus("current")
_Cie1000DhcpServerConfigPoolTableRowEditorSubnetMask_Type = IpAddress
_Cie1000DhcpServerConfigPoolTableRowEditorSubnetMask_Object = MibScalar
cie1000DhcpServerConfigPoolTableRowEditorSubnetMask = _Cie1000DhcpServerConfigPoolTableRowEditorSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 6, 4),
    _Cie1000DhcpServerConfigPoolTableRowEditorSubnetMask_Type()
)
cie1000DhcpServerConfigPoolTableRowEditorSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigPoolTableRowEditorSubnetMask.setStatus("current")
_Cie1000DhcpServerConfigPoolTableRowEditorSubnetBroadcast_Type = IpAddress
_Cie1000DhcpServerConfigPoolTableRowEditorSubnetBroadcast_Object = MibScalar
cie1000DhcpServerConfigPoolTableRowEditorSubnetBroadcast = _Cie1000DhcpServerConfigPoolTableRowEditorSubnetBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 6, 5),
    _Cie1000DhcpServerConfigPoolTableRowEditorSubnetBroadcast_Type()
)
cie1000DhcpServerConfigPoolTableRowEditorSubnetBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigPoolTableRowEditorSubnetBroadcast.setStatus("current")
_Cie1000DhcpServerConfigPoolTableRowEditorLeaseDay_Type = Unsigned32
_Cie1000DhcpServerConfigPoolTableRowEditorLeaseDay_Object = MibScalar
cie1000DhcpServerConfigPoolTableRowEditorLeaseDay = _Cie1000DhcpServerConfigPoolTableRowEditorLeaseDay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 6, 6),
    _Cie1000DhcpServerConfigPoolTableRowEditorLeaseDay_Type()
)
cie1000DhcpServerConfigPoolTableRowEditorLeaseDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigPoolTableRowEditorLeaseDay.setStatus("current")
_Cie1000DhcpServerConfigPoolTableRowEditorLeaseHour_Type = Unsigned32
_Cie1000DhcpServerConfigPoolTableRowEditorLeaseHour_Object = MibScalar
cie1000DhcpServerConfigPoolTableRowEditorLeaseHour = _Cie1000DhcpServerConfigPoolTableRowEditorLeaseHour_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 6, 7),
    _Cie1000DhcpServerConfigPoolTableRowEditorLeaseHour_Type()
)
cie1000DhcpServerConfigPoolTableRowEditorLeaseHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigPoolTableRowEditorLeaseHour.setStatus("current")
_Cie1000DhcpServerConfigPoolTableRowEditorLeaseMinute_Type = Unsigned32
_Cie1000DhcpServerConfigPoolTableRowEditorLeaseMinute_Object = MibScalar
cie1000DhcpServerConfigPoolTableRowEditorLeaseMinute = _Cie1000DhcpServerConfigPoolTableRowEditorLeaseMinute_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 6, 8),
    _Cie1000DhcpServerConfigPoolTableRowEditorLeaseMinute_Type()
)
cie1000DhcpServerConfigPoolTableRowEditorLeaseMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigPoolTableRowEditorLeaseMinute.setStatus("current")


class _Cie1000DhcpServerConfigPoolTableRowEditorDomainName_Type(CIE1000DisplayString):
    """Custom type cie1000DhcpServerConfigPoolTableRowEditorDomainName based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Cie1000DhcpServerConfigPoolTableRowEditorDomainName_Type.__name__ = "CIE1000DisplayString"
_Cie1000DhcpServerConfigPoolTableRowEditorDomainName_Object = MibScalar
cie1000DhcpServerConfigPoolTableRowEditorDomainName = _Cie1000DhcpServerConfigPoolTableRowEditorDomainName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 6, 9),
    _Cie1000DhcpServerConfigPoolTableRowEditorDomainName_Type()
)
cie1000DhcpServerConfigPoolTableRowEditorDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigPoolTableRowEditorDomainName.setStatus("current")
_Cie1000DhcpServerConfigPoolTableRowEditorDefaultRouter1_Type = IpAddress
_Cie1000DhcpServerConfigPoolTableRowEditorDefaultRouter1_Object = MibScalar
cie1000DhcpServerConfigPoolTableRowEditorDefaultRouter1 = _Cie1000DhcpServerConfigPoolTableRowEditorDefaultRouter1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 6, 10),
    _Cie1000DhcpServerConfigPoolTableRowEditorDefaultRouter1_Type()
)
cie1000DhcpServerConfigPoolTableRowEditorDefaultRouter1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigPoolTableRowEditorDefaultRouter1.setStatus("current")
_Cie1000DhcpServerConfigPoolTableRowEditorDefaultRouter2_Type = IpAddress
_Cie1000DhcpServerConfigPoolTableRowEditorDefaultRouter2_Object = MibScalar
cie1000DhcpServerConfigPoolTableRowEditorDefaultRouter2 = _Cie1000DhcpServerConfigPoolTableRowEditorDefaultRouter2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 6, 11),
    _Cie1000DhcpServerConfigPoolTableRowEditorDefaultRouter2_Type()
)
cie1000DhcpServerConfigPoolTableRowEditorDefaultRouter2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigPoolTableRowEditorDefaultRouter2.setStatus("current")
_Cie1000DhcpServerConfigPoolTableRowEditorDefaultRouter3_Type = IpAddress
_Cie1000DhcpServerConfigPoolTableRowEditorDefaultRouter3_Object = MibScalar
cie1000DhcpServerConfigPoolTableRowEditorDefaultRouter3 = _Cie1000DhcpServerConfigPoolTableRowEditorDefaultRouter3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 6, 12),
    _Cie1000DhcpServerConfigPoolTableRowEditorDefaultRouter3_Type()
)
cie1000DhcpServerConfigPoolTableRowEditorDefaultRouter3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigPoolTableRowEditorDefaultRouter3.setStatus("current")
_Cie1000DhcpServerConfigPoolTableRowEditorDefaultRouter4_Type = IpAddress
_Cie1000DhcpServerConfigPoolTableRowEditorDefaultRouter4_Object = MibScalar
cie1000DhcpServerConfigPoolTableRowEditorDefaultRouter4 = _Cie1000DhcpServerConfigPoolTableRowEditorDefaultRouter4_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 6, 13),
    _Cie1000DhcpServerConfigPoolTableRowEditorDefaultRouter4_Type()
)
cie1000DhcpServerConfigPoolTableRowEditorDefaultRouter4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigPoolTableRowEditorDefaultRouter4.setStatus("current")
_Cie1000DhcpServerConfigPoolTableRowEditorDnsServer1_Type = IpAddress
_Cie1000DhcpServerConfigPoolTableRowEditorDnsServer1_Object = MibScalar
cie1000DhcpServerConfigPoolTableRowEditorDnsServer1 = _Cie1000DhcpServerConfigPoolTableRowEditorDnsServer1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 6, 14),
    _Cie1000DhcpServerConfigPoolTableRowEditorDnsServer1_Type()
)
cie1000DhcpServerConfigPoolTableRowEditorDnsServer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigPoolTableRowEditorDnsServer1.setStatus("current")
_Cie1000DhcpServerConfigPoolTableRowEditorDnsServer2_Type = IpAddress
_Cie1000DhcpServerConfigPoolTableRowEditorDnsServer2_Object = MibScalar
cie1000DhcpServerConfigPoolTableRowEditorDnsServer2 = _Cie1000DhcpServerConfigPoolTableRowEditorDnsServer2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 6, 15),
    _Cie1000DhcpServerConfigPoolTableRowEditorDnsServer2_Type()
)
cie1000DhcpServerConfigPoolTableRowEditorDnsServer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigPoolTableRowEditorDnsServer2.setStatus("current")
_Cie1000DhcpServerConfigPoolTableRowEditorDnsServer3_Type = IpAddress
_Cie1000DhcpServerConfigPoolTableRowEditorDnsServer3_Object = MibScalar
cie1000DhcpServerConfigPoolTableRowEditorDnsServer3 = _Cie1000DhcpServerConfigPoolTableRowEditorDnsServer3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 6, 16),
    _Cie1000DhcpServerConfigPoolTableRowEditorDnsServer3_Type()
)
cie1000DhcpServerConfigPoolTableRowEditorDnsServer3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigPoolTableRowEditorDnsServer3.setStatus("current")
_Cie1000DhcpServerConfigPoolTableRowEditorDnsServer4_Type = IpAddress
_Cie1000DhcpServerConfigPoolTableRowEditorDnsServer4_Object = MibScalar
cie1000DhcpServerConfigPoolTableRowEditorDnsServer4 = _Cie1000DhcpServerConfigPoolTableRowEditorDnsServer4_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 6, 17),
    _Cie1000DhcpServerConfigPoolTableRowEditorDnsServer4_Type()
)
cie1000DhcpServerConfigPoolTableRowEditorDnsServer4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigPoolTableRowEditorDnsServer4.setStatus("current")
_Cie1000DhcpServerConfigPoolTableRowEditorNtpServer1_Type = IpAddress
_Cie1000DhcpServerConfigPoolTableRowEditorNtpServer1_Object = MibScalar
cie1000DhcpServerConfigPoolTableRowEditorNtpServer1 = _Cie1000DhcpServerConfigPoolTableRowEditorNtpServer1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 6, 18),
    _Cie1000DhcpServerConfigPoolTableRowEditorNtpServer1_Type()
)
cie1000DhcpServerConfigPoolTableRowEditorNtpServer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigPoolTableRowEditorNtpServer1.setStatus("current")
_Cie1000DhcpServerConfigPoolTableRowEditorNtpServer2_Type = IpAddress
_Cie1000DhcpServerConfigPoolTableRowEditorNtpServer2_Object = MibScalar
cie1000DhcpServerConfigPoolTableRowEditorNtpServer2 = _Cie1000DhcpServerConfigPoolTableRowEditorNtpServer2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 6, 19),
    _Cie1000DhcpServerConfigPoolTableRowEditorNtpServer2_Type()
)
cie1000DhcpServerConfigPoolTableRowEditorNtpServer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigPoolTableRowEditorNtpServer2.setStatus("current")
_Cie1000DhcpServerConfigPoolTableRowEditorNtpServer3_Type = IpAddress
_Cie1000DhcpServerConfigPoolTableRowEditorNtpServer3_Object = MibScalar
cie1000DhcpServerConfigPoolTableRowEditorNtpServer3 = _Cie1000DhcpServerConfigPoolTableRowEditorNtpServer3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 6, 20),
    _Cie1000DhcpServerConfigPoolTableRowEditorNtpServer3_Type()
)
cie1000DhcpServerConfigPoolTableRowEditorNtpServer3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigPoolTableRowEditorNtpServer3.setStatus("current")
_Cie1000DhcpServerConfigPoolTableRowEditorNtpServer4_Type = IpAddress
_Cie1000DhcpServerConfigPoolTableRowEditorNtpServer4_Object = MibScalar
cie1000DhcpServerConfigPoolTableRowEditorNtpServer4 = _Cie1000DhcpServerConfigPoolTableRowEditorNtpServer4_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 6, 21),
    _Cie1000DhcpServerConfigPoolTableRowEditorNtpServer4_Type()
)
cie1000DhcpServerConfigPoolTableRowEditorNtpServer4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigPoolTableRowEditorNtpServer4.setStatus("current")
_Cie1000DhcpServerConfigPoolTableRowEditorNetbiosNodeType_Type = CIE1000DhcpServerNetbiosNodeEnum
_Cie1000DhcpServerConfigPoolTableRowEditorNetbiosNodeType_Object = MibScalar
cie1000DhcpServerConfigPoolTableRowEditorNetbiosNodeType = _Cie1000DhcpServerConfigPoolTableRowEditorNetbiosNodeType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 6, 22),
    _Cie1000DhcpServerConfigPoolTableRowEditorNetbiosNodeType_Type()
)
cie1000DhcpServerConfigPoolTableRowEditorNetbiosNodeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigPoolTableRowEditorNetbiosNodeType.setStatus("current")


class _Cie1000DhcpServerConfigPoolTableRowEditorNetbiosScope_Type(CIE1000DisplayString):
    """Custom type cie1000DhcpServerConfigPoolTableRowEditorNetbiosScope based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Cie1000DhcpServerConfigPoolTableRowEditorNetbiosScope_Type.__name__ = "CIE1000DisplayString"
_Cie1000DhcpServerConfigPoolTableRowEditorNetbiosScope_Object = MibScalar
cie1000DhcpServerConfigPoolTableRowEditorNetbiosScope = _Cie1000DhcpServerConfigPoolTableRowEditorNetbiosScope_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 6, 23),
    _Cie1000DhcpServerConfigPoolTableRowEditorNetbiosScope_Type()
)
cie1000DhcpServerConfigPoolTableRowEditorNetbiosScope.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigPoolTableRowEditorNetbiosScope.setStatus("current")
_Cie1000DhcpServerConfigPoolTableRowEditorNetbiosNameServer1_Type = IpAddress
_Cie1000DhcpServerConfigPoolTableRowEditorNetbiosNameServer1_Object = MibScalar
cie1000DhcpServerConfigPoolTableRowEditorNetbiosNameServer1 = _Cie1000DhcpServerConfigPoolTableRowEditorNetbiosNameServer1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 6, 24),
    _Cie1000DhcpServerConfigPoolTableRowEditorNetbiosNameServer1_Type()
)
cie1000DhcpServerConfigPoolTableRowEditorNetbiosNameServer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigPoolTableRowEditorNetbiosNameServer1.setStatus("current")
_Cie1000DhcpServerConfigPoolTableRowEditorNetbiosNameServer2_Type = IpAddress
_Cie1000DhcpServerConfigPoolTableRowEditorNetbiosNameServer2_Object = MibScalar
cie1000DhcpServerConfigPoolTableRowEditorNetbiosNameServer2 = _Cie1000DhcpServerConfigPoolTableRowEditorNetbiosNameServer2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 6, 25),
    _Cie1000DhcpServerConfigPoolTableRowEditorNetbiosNameServer2_Type()
)
cie1000DhcpServerConfigPoolTableRowEditorNetbiosNameServer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigPoolTableRowEditorNetbiosNameServer2.setStatus("current")
_Cie1000DhcpServerConfigPoolTableRowEditorNetbiosNameServer3_Type = IpAddress
_Cie1000DhcpServerConfigPoolTableRowEditorNetbiosNameServer3_Object = MibScalar
cie1000DhcpServerConfigPoolTableRowEditorNetbiosNameServer3 = _Cie1000DhcpServerConfigPoolTableRowEditorNetbiosNameServer3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 6, 26),
    _Cie1000DhcpServerConfigPoolTableRowEditorNetbiosNameServer3_Type()
)
cie1000DhcpServerConfigPoolTableRowEditorNetbiosNameServer3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigPoolTableRowEditorNetbiosNameServer3.setStatus("current")
_Cie1000DhcpServerConfigPoolTableRowEditorNetbiosNameServer4_Type = IpAddress
_Cie1000DhcpServerConfigPoolTableRowEditorNetbiosNameServer4_Object = MibScalar
cie1000DhcpServerConfigPoolTableRowEditorNetbiosNameServer4 = _Cie1000DhcpServerConfigPoolTableRowEditorNetbiosNameServer4_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 6, 27),
    _Cie1000DhcpServerConfigPoolTableRowEditorNetbiosNameServer4_Type()
)
cie1000DhcpServerConfigPoolTableRowEditorNetbiosNameServer4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigPoolTableRowEditorNetbiosNameServer4.setStatus("current")


class _Cie1000DhcpServerConfigPoolTableRowEditorNisDomainName_Type(CIE1000DisplayString):
    """Custom type cie1000DhcpServerConfigPoolTableRowEditorNisDomainName based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Cie1000DhcpServerConfigPoolTableRowEditorNisDomainName_Type.__name__ = "CIE1000DisplayString"
_Cie1000DhcpServerConfigPoolTableRowEditorNisDomainName_Object = MibScalar
cie1000DhcpServerConfigPoolTableRowEditorNisDomainName = _Cie1000DhcpServerConfigPoolTableRowEditorNisDomainName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 6, 28),
    _Cie1000DhcpServerConfigPoolTableRowEditorNisDomainName_Type()
)
cie1000DhcpServerConfigPoolTableRowEditorNisDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigPoolTableRowEditorNisDomainName.setStatus("current")
_Cie1000DhcpServerConfigPoolTableRowEditorNisServer1_Type = IpAddress
_Cie1000DhcpServerConfigPoolTableRowEditorNisServer1_Object = MibScalar
cie1000DhcpServerConfigPoolTableRowEditorNisServer1 = _Cie1000DhcpServerConfigPoolTableRowEditorNisServer1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 6, 29),
    _Cie1000DhcpServerConfigPoolTableRowEditorNisServer1_Type()
)
cie1000DhcpServerConfigPoolTableRowEditorNisServer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigPoolTableRowEditorNisServer1.setStatus("current")
_Cie1000DhcpServerConfigPoolTableRowEditorNisServer2_Type = IpAddress
_Cie1000DhcpServerConfigPoolTableRowEditorNisServer2_Object = MibScalar
cie1000DhcpServerConfigPoolTableRowEditorNisServer2 = _Cie1000DhcpServerConfigPoolTableRowEditorNisServer2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 6, 30),
    _Cie1000DhcpServerConfigPoolTableRowEditorNisServer2_Type()
)
cie1000DhcpServerConfigPoolTableRowEditorNisServer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigPoolTableRowEditorNisServer2.setStatus("current")
_Cie1000DhcpServerConfigPoolTableRowEditorNisServer3_Type = IpAddress
_Cie1000DhcpServerConfigPoolTableRowEditorNisServer3_Object = MibScalar
cie1000DhcpServerConfigPoolTableRowEditorNisServer3 = _Cie1000DhcpServerConfigPoolTableRowEditorNisServer3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 6, 31),
    _Cie1000DhcpServerConfigPoolTableRowEditorNisServer3_Type()
)
cie1000DhcpServerConfigPoolTableRowEditorNisServer3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigPoolTableRowEditorNisServer3.setStatus("current")
_Cie1000DhcpServerConfigPoolTableRowEditorNisServer4_Type = IpAddress
_Cie1000DhcpServerConfigPoolTableRowEditorNisServer4_Object = MibScalar
cie1000DhcpServerConfigPoolTableRowEditorNisServer4 = _Cie1000DhcpServerConfigPoolTableRowEditorNisServer4_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 6, 32),
    _Cie1000DhcpServerConfigPoolTableRowEditorNisServer4_Type()
)
cie1000DhcpServerConfigPoolTableRowEditorNisServer4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigPoolTableRowEditorNisServer4.setStatus("current")
_Cie1000DhcpServerConfigPoolTableRowEditorClientIdentifierType_Type = CIE1000DhcpServerClientIdentifierEnum
_Cie1000DhcpServerConfigPoolTableRowEditorClientIdentifierType_Object = MibScalar
cie1000DhcpServerConfigPoolTableRowEditorClientIdentifierType = _Cie1000DhcpServerConfigPoolTableRowEditorClientIdentifierType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 6, 33),
    _Cie1000DhcpServerConfigPoolTableRowEditorClientIdentifierType_Type()
)
cie1000DhcpServerConfigPoolTableRowEditorClientIdentifierType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigPoolTableRowEditorClientIdentifierType.setStatus("current")


class _Cie1000DhcpServerConfigPoolTableRowEditorClientIdentifierName_Type(CIE1000DisplayString):
    """Custom type cie1000DhcpServerConfigPoolTableRowEditorClientIdentifierName based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Cie1000DhcpServerConfigPoolTableRowEditorClientIdentifierName_Type.__name__ = "CIE1000DisplayString"
_Cie1000DhcpServerConfigPoolTableRowEditorClientIdentifierName_Object = MibScalar
cie1000DhcpServerConfigPoolTableRowEditorClientIdentifierName = _Cie1000DhcpServerConfigPoolTableRowEditorClientIdentifierName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 6, 34),
    _Cie1000DhcpServerConfigPoolTableRowEditorClientIdentifierName_Type()
)
cie1000DhcpServerConfigPoolTableRowEditorClientIdentifierName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigPoolTableRowEditorClientIdentifierName.setStatus("current")
_Cie1000DhcpServerConfigPoolTableRowEditorClientIdentifierMac_Type = MacAddress
_Cie1000DhcpServerConfigPoolTableRowEditorClientIdentifierMac_Object = MibScalar
cie1000DhcpServerConfigPoolTableRowEditorClientIdentifierMac = _Cie1000DhcpServerConfigPoolTableRowEditorClientIdentifierMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 6, 35),
    _Cie1000DhcpServerConfigPoolTableRowEditorClientIdentifierMac_Type()
)
cie1000DhcpServerConfigPoolTableRowEditorClientIdentifierMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigPoolTableRowEditorClientIdentifierMac.setStatus("current")
_Cie1000DhcpServerConfigPoolTableRowEditorClientHardwareAddress_Type = MacAddress
_Cie1000DhcpServerConfigPoolTableRowEditorClientHardwareAddress_Object = MibScalar
cie1000DhcpServerConfigPoolTableRowEditorClientHardwareAddress = _Cie1000DhcpServerConfigPoolTableRowEditorClientHardwareAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 6, 36),
    _Cie1000DhcpServerConfigPoolTableRowEditorClientHardwareAddress_Type()
)
cie1000DhcpServerConfigPoolTableRowEditorClientHardwareAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigPoolTableRowEditorClientHardwareAddress.setStatus("current")


class _Cie1000DhcpServerConfigPoolTableRowEditorClientName_Type(CIE1000DisplayString):
    """Custom type cie1000DhcpServerConfigPoolTableRowEditorClientName based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Cie1000DhcpServerConfigPoolTableRowEditorClientName_Type.__name__ = "CIE1000DisplayString"
_Cie1000DhcpServerConfigPoolTableRowEditorClientName_Object = MibScalar
cie1000DhcpServerConfigPoolTableRowEditorClientName = _Cie1000DhcpServerConfigPoolTableRowEditorClientName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 6, 37),
    _Cie1000DhcpServerConfigPoolTableRowEditorClientName_Type()
)
cie1000DhcpServerConfigPoolTableRowEditorClientName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigPoolTableRowEditorClientName.setStatus("current")


class _Cie1000DhcpServerConfigPoolTableRowEditorVendorClassId1_Type(CIE1000DisplayString):
    """Custom type cie1000DhcpServerConfigPoolTableRowEditorVendorClassId1 based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Cie1000DhcpServerConfigPoolTableRowEditorVendorClassId1_Type.__name__ = "CIE1000DisplayString"
_Cie1000DhcpServerConfigPoolTableRowEditorVendorClassId1_Object = MibScalar
cie1000DhcpServerConfigPoolTableRowEditorVendorClassId1 = _Cie1000DhcpServerConfigPoolTableRowEditorVendorClassId1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 6, 38),
    _Cie1000DhcpServerConfigPoolTableRowEditorVendorClassId1_Type()
)
cie1000DhcpServerConfigPoolTableRowEditorVendorClassId1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigPoolTableRowEditorVendorClassId1.setStatus("current")


class _Cie1000DhcpServerConfigPoolTableRowEditorVendorSpecificInfo1_Type(CIE1000DisplayString):
    """Custom type cie1000DhcpServerConfigPoolTableRowEditorVendorSpecificInfo1 based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 66),
    )


_Cie1000DhcpServerConfigPoolTableRowEditorVendorSpecificInfo1_Type.__name__ = "CIE1000DisplayString"
_Cie1000DhcpServerConfigPoolTableRowEditorVendorSpecificInfo1_Object = MibScalar
cie1000DhcpServerConfigPoolTableRowEditorVendorSpecificInfo1 = _Cie1000DhcpServerConfigPoolTableRowEditorVendorSpecificInfo1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 6, 39),
    _Cie1000DhcpServerConfigPoolTableRowEditorVendorSpecificInfo1_Type()
)
cie1000DhcpServerConfigPoolTableRowEditorVendorSpecificInfo1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigPoolTableRowEditorVendorSpecificInfo1.setStatus("current")


class _Cie1000DhcpServerConfigPoolTableRowEditorVendorClassId2_Type(CIE1000DisplayString):
    """Custom type cie1000DhcpServerConfigPoolTableRowEditorVendorClassId2 based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Cie1000DhcpServerConfigPoolTableRowEditorVendorClassId2_Type.__name__ = "CIE1000DisplayString"
_Cie1000DhcpServerConfigPoolTableRowEditorVendorClassId2_Object = MibScalar
cie1000DhcpServerConfigPoolTableRowEditorVendorClassId2 = _Cie1000DhcpServerConfigPoolTableRowEditorVendorClassId2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 6, 40),
    _Cie1000DhcpServerConfigPoolTableRowEditorVendorClassId2_Type()
)
cie1000DhcpServerConfigPoolTableRowEditorVendorClassId2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigPoolTableRowEditorVendorClassId2.setStatus("current")


class _Cie1000DhcpServerConfigPoolTableRowEditorVendorSpecificInfo2_Type(CIE1000DisplayString):
    """Custom type cie1000DhcpServerConfigPoolTableRowEditorVendorSpecificInfo2 based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 66),
    )


_Cie1000DhcpServerConfigPoolTableRowEditorVendorSpecificInfo2_Type.__name__ = "CIE1000DisplayString"
_Cie1000DhcpServerConfigPoolTableRowEditorVendorSpecificInfo2_Object = MibScalar
cie1000DhcpServerConfigPoolTableRowEditorVendorSpecificInfo2 = _Cie1000DhcpServerConfigPoolTableRowEditorVendorSpecificInfo2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 6, 41),
    _Cie1000DhcpServerConfigPoolTableRowEditorVendorSpecificInfo2_Type()
)
cie1000DhcpServerConfigPoolTableRowEditorVendorSpecificInfo2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigPoolTableRowEditorVendorSpecificInfo2.setStatus("current")


class _Cie1000DhcpServerConfigPoolTableRowEditorVendorClassId3_Type(CIE1000DisplayString):
    """Custom type cie1000DhcpServerConfigPoolTableRowEditorVendorClassId3 based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Cie1000DhcpServerConfigPoolTableRowEditorVendorClassId3_Type.__name__ = "CIE1000DisplayString"
_Cie1000DhcpServerConfigPoolTableRowEditorVendorClassId3_Object = MibScalar
cie1000DhcpServerConfigPoolTableRowEditorVendorClassId3 = _Cie1000DhcpServerConfigPoolTableRowEditorVendorClassId3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 6, 42),
    _Cie1000DhcpServerConfigPoolTableRowEditorVendorClassId3_Type()
)
cie1000DhcpServerConfigPoolTableRowEditorVendorClassId3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigPoolTableRowEditorVendorClassId3.setStatus("current")


class _Cie1000DhcpServerConfigPoolTableRowEditorVendorSpecificInfo3_Type(CIE1000DisplayString):
    """Custom type cie1000DhcpServerConfigPoolTableRowEditorVendorSpecificInfo3 based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 66),
    )


_Cie1000DhcpServerConfigPoolTableRowEditorVendorSpecificInfo3_Type.__name__ = "CIE1000DisplayString"
_Cie1000DhcpServerConfigPoolTableRowEditorVendorSpecificInfo3_Object = MibScalar
cie1000DhcpServerConfigPoolTableRowEditorVendorSpecificInfo3 = _Cie1000DhcpServerConfigPoolTableRowEditorVendorSpecificInfo3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 6, 43),
    _Cie1000DhcpServerConfigPoolTableRowEditorVendorSpecificInfo3_Type()
)
cie1000DhcpServerConfigPoolTableRowEditorVendorSpecificInfo3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigPoolTableRowEditorVendorSpecificInfo3.setStatus("current")


class _Cie1000DhcpServerConfigPoolTableRowEditorVendorClassId4_Type(CIE1000DisplayString):
    """Custom type cie1000DhcpServerConfigPoolTableRowEditorVendorClassId4 based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Cie1000DhcpServerConfigPoolTableRowEditorVendorClassId4_Type.__name__ = "CIE1000DisplayString"
_Cie1000DhcpServerConfigPoolTableRowEditorVendorClassId4_Object = MibScalar
cie1000DhcpServerConfigPoolTableRowEditorVendorClassId4 = _Cie1000DhcpServerConfigPoolTableRowEditorVendorClassId4_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 6, 44),
    _Cie1000DhcpServerConfigPoolTableRowEditorVendorClassId4_Type()
)
cie1000DhcpServerConfigPoolTableRowEditorVendorClassId4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigPoolTableRowEditorVendorClassId4.setStatus("current")


class _Cie1000DhcpServerConfigPoolTableRowEditorVendorSpecificInfo4_Type(CIE1000DisplayString):
    """Custom type cie1000DhcpServerConfigPoolTableRowEditorVendorSpecificInfo4 based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 66),
    )


_Cie1000DhcpServerConfigPoolTableRowEditorVendorSpecificInfo4_Type.__name__ = "CIE1000DisplayString"
_Cie1000DhcpServerConfigPoolTableRowEditorVendorSpecificInfo4_Object = MibScalar
cie1000DhcpServerConfigPoolTableRowEditorVendorSpecificInfo4 = _Cie1000DhcpServerConfigPoolTableRowEditorVendorSpecificInfo4_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 6, 45),
    _Cie1000DhcpServerConfigPoolTableRowEditorVendorSpecificInfo4_Type()
)
cie1000DhcpServerConfigPoolTableRowEditorVendorSpecificInfo4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigPoolTableRowEditorVendorSpecificInfo4.setStatus("current")
_Cie1000DhcpServerConfigPoolTableRowEditorAction_Type = CIE1000RowEditorState
_Cie1000DhcpServerConfigPoolTableRowEditorAction_Object = MibScalar
cie1000DhcpServerConfigPoolTableRowEditorAction = _Cie1000DhcpServerConfigPoolTableRowEditorAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 6, 100),
    _Cie1000DhcpServerConfigPoolTableRowEditorAction_Type()
)
cie1000DhcpServerConfigPoolTableRowEditorAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigPoolTableRowEditorAction.setStatus("current")
_Cie1000DhcpServerConfigReservedTable_Object = MibTable
cie1000DhcpServerConfigReservedTable = _Cie1000DhcpServerConfigReservedTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 7)
)
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigReservedTable.setStatus("current")
_Cie1000DhcpServerConfigReservedEntry_Object = MibTableRow
cie1000DhcpServerConfigReservedEntry = _Cie1000DhcpServerConfigReservedEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 7, 1)
)
cie1000DhcpServerConfigReservedEntry.setIndexNames(
    (0, "CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigReservedPoolName"),
    (0, "CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigReservedIpAddress"),
)
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigReservedEntry.setStatus("current")


class _Cie1000DhcpServerConfigReservedPoolName_Type(CIE1000DisplayString):
    """Custom type cie1000DhcpServerConfigReservedPoolName based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Cie1000DhcpServerConfigReservedPoolName_Type.__name__ = "CIE1000DisplayString"
_Cie1000DhcpServerConfigReservedPoolName_Object = MibTableColumn
cie1000DhcpServerConfigReservedPoolName = _Cie1000DhcpServerConfigReservedPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 7, 1, 1),
    _Cie1000DhcpServerConfigReservedPoolName_Type()
)
cie1000DhcpServerConfigReservedPoolName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigReservedPoolName.setStatus("current")
_Cie1000DhcpServerConfigReservedIpAddress_Type = IpAddress
_Cie1000DhcpServerConfigReservedIpAddress_Object = MibTableColumn
cie1000DhcpServerConfigReservedIpAddress = _Cie1000DhcpServerConfigReservedIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 7, 1, 2),
    _Cie1000DhcpServerConfigReservedIpAddress_Type()
)
cie1000DhcpServerConfigReservedIpAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigReservedIpAddress.setStatus("current")
_Cie1000DhcpServerConfigReservedIfIndex_Type = CIE1000InterfaceIndex
_Cie1000DhcpServerConfigReservedIfIndex_Object = MibTableColumn
cie1000DhcpServerConfigReservedIfIndex = _Cie1000DhcpServerConfigReservedIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 7, 1, 3),
    _Cie1000DhcpServerConfigReservedIfIndex_Type()
)
cie1000DhcpServerConfigReservedIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigReservedIfIndex.setStatus("current")
_Cie1000DhcpServerConfigReservedAction_Type = CIE1000RowEditorState
_Cie1000DhcpServerConfigReservedAction_Object = MibTableColumn
cie1000DhcpServerConfigReservedAction = _Cie1000DhcpServerConfigReservedAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 7, 1, 100),
    _Cie1000DhcpServerConfigReservedAction_Type()
)
cie1000DhcpServerConfigReservedAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigReservedAction.setStatus("current")
_Cie1000DhcpServerConfigReservedIpTableRowEditor_ObjectIdentity = ObjectIdentity
cie1000DhcpServerConfigReservedIpTableRowEditor = _Cie1000DhcpServerConfigReservedIpTableRowEditor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 8)
)


class _Cie1000DhcpServerConfigReservedIpTableRowEditorPoolName_Type(CIE1000DisplayString):
    """Custom type cie1000DhcpServerConfigReservedIpTableRowEditorPoolName based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Cie1000DhcpServerConfigReservedIpTableRowEditorPoolName_Type.__name__ = "CIE1000DisplayString"
_Cie1000DhcpServerConfigReservedIpTableRowEditorPoolName_Object = MibScalar
cie1000DhcpServerConfigReservedIpTableRowEditorPoolName = _Cie1000DhcpServerConfigReservedIpTableRowEditorPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 8, 1),
    _Cie1000DhcpServerConfigReservedIpTableRowEditorPoolName_Type()
)
cie1000DhcpServerConfigReservedIpTableRowEditorPoolName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigReservedIpTableRowEditorPoolName.setStatus("current")
_Cie1000DhcpServerConfigReservedIpTableRowEditorIpAddress_Type = IpAddress
_Cie1000DhcpServerConfigReservedIpTableRowEditorIpAddress_Object = MibScalar
cie1000DhcpServerConfigReservedIpTableRowEditorIpAddress = _Cie1000DhcpServerConfigReservedIpTableRowEditorIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 8, 2),
    _Cie1000DhcpServerConfigReservedIpTableRowEditorIpAddress_Type()
)
cie1000DhcpServerConfigReservedIpTableRowEditorIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigReservedIpTableRowEditorIpAddress.setStatus("current")
_Cie1000DhcpServerConfigReservedIpTableRowEditorIfIndex_Type = CIE1000InterfaceIndex
_Cie1000DhcpServerConfigReservedIpTableRowEditorIfIndex_Object = MibScalar
cie1000DhcpServerConfigReservedIpTableRowEditorIfIndex = _Cie1000DhcpServerConfigReservedIpTableRowEditorIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 8, 3),
    _Cie1000DhcpServerConfigReservedIpTableRowEditorIfIndex_Type()
)
cie1000DhcpServerConfigReservedIpTableRowEditorIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigReservedIpTableRowEditorIfIndex.setStatus("current")
_Cie1000DhcpServerConfigReservedIpTableRowEditorAction_Type = CIE1000RowEditorState
_Cie1000DhcpServerConfigReservedIpTableRowEditorAction_Object = MibScalar
cie1000DhcpServerConfigReservedIpTableRowEditorAction = _Cie1000DhcpServerConfigReservedIpTableRowEditorAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 2, 8, 100),
    _Cie1000DhcpServerConfigReservedIpTableRowEditorAction_Type()
)
cie1000DhcpServerConfigReservedIpTableRowEditorAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigReservedIpTableRowEditorAction.setStatus("current")
_Cie1000DhcpServerStatus_ObjectIdentity = ObjectIdentity
cie1000DhcpServerStatus = _Cie1000DhcpServerStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 3)
)
_Cie1000DhcpServerStatusDeclinedTable_Object = MibTable
cie1000DhcpServerStatusDeclinedTable = _Cie1000DhcpServerStatusDeclinedTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cie1000DhcpServerStatusDeclinedTable.setStatus("current")
_Cie1000DhcpServerStatusDeclinedEntry_Object = MibTableRow
cie1000DhcpServerStatusDeclinedEntry = _Cie1000DhcpServerStatusDeclinedEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 3, 1, 1)
)
cie1000DhcpServerStatusDeclinedEntry.setIndexNames(
    (0, "CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerStatusDeclinedEntryNo"),
)
if mibBuilder.loadTexts:
    cie1000DhcpServerStatusDeclinedEntry.setStatus("current")


class _Cie1000DhcpServerStatusDeclinedEntryNo_Type(Integer32):
    """Custom type cie1000DhcpServerStatusDeclinedEntryNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cie1000DhcpServerStatusDeclinedEntryNo_Type.__name__ = "Integer32"
_Cie1000DhcpServerStatusDeclinedEntryNo_Object = MibTableColumn
cie1000DhcpServerStatusDeclinedEntryNo = _Cie1000DhcpServerStatusDeclinedEntryNo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 3, 1, 1, 1),
    _Cie1000DhcpServerStatusDeclinedEntryNo_Type()
)
cie1000DhcpServerStatusDeclinedEntryNo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000DhcpServerStatusDeclinedEntryNo.setStatus("current")
_Cie1000DhcpServerStatusDeclinedIpv4Address_Type = IpAddress
_Cie1000DhcpServerStatusDeclinedIpv4Address_Object = MibTableColumn
cie1000DhcpServerStatusDeclinedIpv4Address = _Cie1000DhcpServerStatusDeclinedIpv4Address_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 3, 1, 1, 2),
    _Cie1000DhcpServerStatusDeclinedIpv4Address_Type()
)
cie1000DhcpServerStatusDeclinedIpv4Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000DhcpServerStatusDeclinedIpv4Address.setStatus("current")
_Cie1000DhcpServerStatusStatistics_ObjectIdentity = ObjectIdentity
cie1000DhcpServerStatusStatistics = _Cie1000DhcpServerStatusStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 3, 2)
)
_Cie1000DhcpServerStatusStatisticsDiscoverCnt_Type = Unsigned32
_Cie1000DhcpServerStatusStatisticsDiscoverCnt_Object = MibScalar
cie1000DhcpServerStatusStatisticsDiscoverCnt = _Cie1000DhcpServerStatusStatisticsDiscoverCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 3, 2, 1),
    _Cie1000DhcpServerStatusStatisticsDiscoverCnt_Type()
)
cie1000DhcpServerStatusStatisticsDiscoverCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000DhcpServerStatusStatisticsDiscoverCnt.setStatus("current")
_Cie1000DhcpServerStatusStatisticsOfferCnt_Type = Unsigned32
_Cie1000DhcpServerStatusStatisticsOfferCnt_Object = MibScalar
cie1000DhcpServerStatusStatisticsOfferCnt = _Cie1000DhcpServerStatusStatisticsOfferCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 3, 2, 2),
    _Cie1000DhcpServerStatusStatisticsOfferCnt_Type()
)
cie1000DhcpServerStatusStatisticsOfferCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000DhcpServerStatusStatisticsOfferCnt.setStatus("current")
_Cie1000DhcpServerStatusStatisticsRequestCnt_Type = Unsigned32
_Cie1000DhcpServerStatusStatisticsRequestCnt_Object = MibScalar
cie1000DhcpServerStatusStatisticsRequestCnt = _Cie1000DhcpServerStatusStatisticsRequestCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 3, 2, 3),
    _Cie1000DhcpServerStatusStatisticsRequestCnt_Type()
)
cie1000DhcpServerStatusStatisticsRequestCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000DhcpServerStatusStatisticsRequestCnt.setStatus("current")
_Cie1000DhcpServerStatusStatisticsAckCnt_Type = Unsigned32
_Cie1000DhcpServerStatusStatisticsAckCnt_Object = MibScalar
cie1000DhcpServerStatusStatisticsAckCnt = _Cie1000DhcpServerStatusStatisticsAckCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 3, 2, 4),
    _Cie1000DhcpServerStatusStatisticsAckCnt_Type()
)
cie1000DhcpServerStatusStatisticsAckCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000DhcpServerStatusStatisticsAckCnt.setStatus("current")
_Cie1000DhcpServerStatusStatisticsNakCnt_Type = Unsigned32
_Cie1000DhcpServerStatusStatisticsNakCnt_Object = MibScalar
cie1000DhcpServerStatusStatisticsNakCnt = _Cie1000DhcpServerStatusStatisticsNakCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 3, 2, 5),
    _Cie1000DhcpServerStatusStatisticsNakCnt_Type()
)
cie1000DhcpServerStatusStatisticsNakCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000DhcpServerStatusStatisticsNakCnt.setStatus("current")
_Cie1000DhcpServerStatusStatisticsDeclineCnt_Type = Unsigned32
_Cie1000DhcpServerStatusStatisticsDeclineCnt_Object = MibScalar
cie1000DhcpServerStatusStatisticsDeclineCnt = _Cie1000DhcpServerStatusStatisticsDeclineCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 3, 2, 6),
    _Cie1000DhcpServerStatusStatisticsDeclineCnt_Type()
)
cie1000DhcpServerStatusStatisticsDeclineCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000DhcpServerStatusStatisticsDeclineCnt.setStatus("current")
_Cie1000DhcpServerStatusStatisticsReleaseCnt_Type = Unsigned32
_Cie1000DhcpServerStatusStatisticsReleaseCnt_Object = MibScalar
cie1000DhcpServerStatusStatisticsReleaseCnt = _Cie1000DhcpServerStatusStatisticsReleaseCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 3, 2, 7),
    _Cie1000DhcpServerStatusStatisticsReleaseCnt_Type()
)
cie1000DhcpServerStatusStatisticsReleaseCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000DhcpServerStatusStatisticsReleaseCnt.setStatus("current")
_Cie1000DhcpServerStatusStatisticsInformCnt_Type = Unsigned32
_Cie1000DhcpServerStatusStatisticsInformCnt_Object = MibScalar
cie1000DhcpServerStatusStatisticsInformCnt = _Cie1000DhcpServerStatusStatisticsInformCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 3, 2, 8),
    _Cie1000DhcpServerStatusStatisticsInformCnt_Type()
)
cie1000DhcpServerStatusStatisticsInformCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000DhcpServerStatusStatisticsInformCnt.setStatus("current")
_Cie1000DhcpServerStatusBindingTable_Object = MibTable
cie1000DhcpServerStatusBindingTable = _Cie1000DhcpServerStatusBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 3, 3)
)
if mibBuilder.loadTexts:
    cie1000DhcpServerStatusBindingTable.setStatus("current")
_Cie1000DhcpServerStatusBindingEntry_Object = MibTableRow
cie1000DhcpServerStatusBindingEntry = _Cie1000DhcpServerStatusBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 3, 3, 1)
)
cie1000DhcpServerStatusBindingEntry.setIndexNames(
    (0, "CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerStatusBindingIpAddress"),
)
if mibBuilder.loadTexts:
    cie1000DhcpServerStatusBindingEntry.setStatus("current")
_Cie1000DhcpServerStatusBindingIpAddress_Type = IpAddress
_Cie1000DhcpServerStatusBindingIpAddress_Object = MibTableColumn
cie1000DhcpServerStatusBindingIpAddress = _Cie1000DhcpServerStatusBindingIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 3, 3, 1, 1),
    _Cie1000DhcpServerStatusBindingIpAddress_Type()
)
cie1000DhcpServerStatusBindingIpAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000DhcpServerStatusBindingIpAddress.setStatus("current")
_Cie1000DhcpServerStatusBindingState_Type = CIE1000DhcpServerBindingStateEnum
_Cie1000DhcpServerStatusBindingState_Object = MibTableColumn
cie1000DhcpServerStatusBindingState = _Cie1000DhcpServerStatusBindingState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 3, 3, 1, 2),
    _Cie1000DhcpServerStatusBindingState_Type()
)
cie1000DhcpServerStatusBindingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000DhcpServerStatusBindingState.setStatus("current")
_Cie1000DhcpServerStatusBindingType_Type = CIE1000DhcpServerBindingEnum
_Cie1000DhcpServerStatusBindingType_Object = MibTableColumn
cie1000DhcpServerStatusBindingType = _Cie1000DhcpServerStatusBindingType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 3, 3, 1, 3),
    _Cie1000DhcpServerStatusBindingType_Type()
)
cie1000DhcpServerStatusBindingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000DhcpServerStatusBindingType.setStatus("current")


class _Cie1000DhcpServerStatusBindingPoolName_Type(CIE1000DisplayString):
    """Custom type cie1000DhcpServerStatusBindingPoolName based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Cie1000DhcpServerStatusBindingPoolName_Type.__name__ = "CIE1000DisplayString"
_Cie1000DhcpServerStatusBindingPoolName_Object = MibTableColumn
cie1000DhcpServerStatusBindingPoolName = _Cie1000DhcpServerStatusBindingPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 3, 3, 1, 4),
    _Cie1000DhcpServerStatusBindingPoolName_Type()
)
cie1000DhcpServerStatusBindingPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000DhcpServerStatusBindingPoolName.setStatus("current")
_Cie1000DhcpServerStatusBindingServerId_Type = IpAddress
_Cie1000DhcpServerStatusBindingServerId_Object = MibTableColumn
cie1000DhcpServerStatusBindingServerId = _Cie1000DhcpServerStatusBindingServerId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 3, 3, 1, 5),
    _Cie1000DhcpServerStatusBindingServerId_Type()
)
cie1000DhcpServerStatusBindingServerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000DhcpServerStatusBindingServerId.setStatus("current")
_Cie1000DhcpServerStatusBindingVlanId_Type = CIE1000Unsigned16
_Cie1000DhcpServerStatusBindingVlanId_Object = MibTableColumn
cie1000DhcpServerStatusBindingVlanId = _Cie1000DhcpServerStatusBindingVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 3, 3, 1, 6),
    _Cie1000DhcpServerStatusBindingVlanId_Type()
)
cie1000DhcpServerStatusBindingVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000DhcpServerStatusBindingVlanId.setStatus("current")
_Cie1000DhcpServerStatusBindingSubnetMask_Type = IpAddress
_Cie1000DhcpServerStatusBindingSubnetMask_Object = MibTableColumn
cie1000DhcpServerStatusBindingSubnetMask = _Cie1000DhcpServerStatusBindingSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 3, 3, 1, 7),
    _Cie1000DhcpServerStatusBindingSubnetMask_Type()
)
cie1000DhcpServerStatusBindingSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000DhcpServerStatusBindingSubnetMask.setStatus("current")
_Cie1000DhcpServerStatusBindingClientIdentifierType_Type = CIE1000DhcpServerClientIdentifierEnum
_Cie1000DhcpServerStatusBindingClientIdentifierType_Object = MibTableColumn
cie1000DhcpServerStatusBindingClientIdentifierType = _Cie1000DhcpServerStatusBindingClientIdentifierType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 3, 3, 1, 8),
    _Cie1000DhcpServerStatusBindingClientIdentifierType_Type()
)
cie1000DhcpServerStatusBindingClientIdentifierType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000DhcpServerStatusBindingClientIdentifierType.setStatus("current")


class _Cie1000DhcpServerStatusBindingClientIdentifierName_Type(CIE1000DisplayString):
    """Custom type cie1000DhcpServerStatusBindingClientIdentifierName based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Cie1000DhcpServerStatusBindingClientIdentifierName_Type.__name__ = "CIE1000DisplayString"
_Cie1000DhcpServerStatusBindingClientIdentifierName_Object = MibTableColumn
cie1000DhcpServerStatusBindingClientIdentifierName = _Cie1000DhcpServerStatusBindingClientIdentifierName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 3, 3, 1, 9),
    _Cie1000DhcpServerStatusBindingClientIdentifierName_Type()
)
cie1000DhcpServerStatusBindingClientIdentifierName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000DhcpServerStatusBindingClientIdentifierName.setStatus("current")
_Cie1000DhcpServerStatusBindingClientIdentifierMac_Type = MacAddress
_Cie1000DhcpServerStatusBindingClientIdentifierMac_Object = MibTableColumn
cie1000DhcpServerStatusBindingClientIdentifierMac = _Cie1000DhcpServerStatusBindingClientIdentifierMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 3, 3, 1, 10),
    _Cie1000DhcpServerStatusBindingClientIdentifierMac_Type()
)
cie1000DhcpServerStatusBindingClientIdentifierMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000DhcpServerStatusBindingClientIdentifierMac.setStatus("current")
_Cie1000DhcpServerStatusBindingMacAddress_Type = MacAddress
_Cie1000DhcpServerStatusBindingMacAddress_Object = MibTableColumn
cie1000DhcpServerStatusBindingMacAddress = _Cie1000DhcpServerStatusBindingMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 3, 3, 1, 11),
    _Cie1000DhcpServerStatusBindingMacAddress_Type()
)
cie1000DhcpServerStatusBindingMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000DhcpServerStatusBindingMacAddress.setStatus("current")


class _Cie1000DhcpServerStatusBindingLease_Type(CIE1000DisplayString):
    """Custom type cie1000DhcpServerStatusBindingLease based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Cie1000DhcpServerStatusBindingLease_Type.__name__ = "CIE1000DisplayString"
_Cie1000DhcpServerStatusBindingLease_Object = MibTableColumn
cie1000DhcpServerStatusBindingLease = _Cie1000DhcpServerStatusBindingLease_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 3, 3, 1, 12),
    _Cie1000DhcpServerStatusBindingLease_Type()
)
cie1000DhcpServerStatusBindingLease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000DhcpServerStatusBindingLease.setStatus("current")


class _Cie1000DhcpServerStatusBindingTimeToExpire_Type(CIE1000DisplayString):
    """Custom type cie1000DhcpServerStatusBindingTimeToExpire based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Cie1000DhcpServerStatusBindingTimeToExpire_Type.__name__ = "CIE1000DisplayString"
_Cie1000DhcpServerStatusBindingTimeToExpire_Object = MibTableColumn
cie1000DhcpServerStatusBindingTimeToExpire = _Cie1000DhcpServerStatusBindingTimeToExpire_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 3, 3, 1, 13),
    _Cie1000DhcpServerStatusBindingTimeToExpire_Type()
)
cie1000DhcpServerStatusBindingTimeToExpire.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000DhcpServerStatusBindingTimeToExpire.setStatus("current")
_Cie1000DhcpServerControl_ObjectIdentity = ObjectIdentity
cie1000DhcpServerControl = _Cie1000DhcpServerControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 4)
)
_Cie1000DhcpServerControlStatistics_ObjectIdentity = ObjectIdentity
cie1000DhcpServerControlStatistics = _Cie1000DhcpServerControlStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 4, 1)
)
_Cie1000DhcpServerControlStatisticsClear_Type = TruthValue
_Cie1000DhcpServerControlStatisticsClear_Object = MibScalar
cie1000DhcpServerControlStatisticsClear = _Cie1000DhcpServerControlStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 4, 1, 1),
    _Cie1000DhcpServerControlStatisticsClear_Type()
)
cie1000DhcpServerControlStatisticsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerControlStatisticsClear.setStatus("current")
_Cie1000DhcpServerControlBinding_ObjectIdentity = ObjectIdentity
cie1000DhcpServerControlBinding = _Cie1000DhcpServerControlBinding_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 4, 2)
)
_Cie1000DhcpServerControlBindingClearByIp_Type = IpAddress
_Cie1000DhcpServerControlBindingClearByIp_Object = MibScalar
cie1000DhcpServerControlBindingClearByIp = _Cie1000DhcpServerControlBindingClearByIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 4, 2, 1),
    _Cie1000DhcpServerControlBindingClearByIp_Type()
)
cie1000DhcpServerControlBindingClearByIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerControlBindingClearByIp.setStatus("current")
_Cie1000DhcpServerControlBindingClearByType_Type = CIE1000DhcpServerBindingEnum
_Cie1000DhcpServerControlBindingClearByType_Object = MibScalar
cie1000DhcpServerControlBindingClearByType = _Cie1000DhcpServerControlBindingClearByType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 1, 4, 2, 2),
    _Cie1000DhcpServerControlBindingClearByType_Type()
)
cie1000DhcpServerControlBindingClearByType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000DhcpServerControlBindingClearByType.setStatus("current")
_Cie1000DhcpServerMibConformance_ObjectIdentity = ObjectIdentity
cie1000DhcpServerMibConformance = _Cie1000DhcpServerMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 2)
)
_Cie1000DhcpServerMibCompliances_ObjectIdentity = ObjectIdentity
cie1000DhcpServerMibCompliances = _Cie1000DhcpServerMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 2, 1)
)
_Cie1000DhcpServerMibGroups_ObjectIdentity = ObjectIdentity
cie1000DhcpServerMibGroups = _Cie1000DhcpServerMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 2, 2)
)

# Managed Objects groups

cie1000DhcpServerConfigGlobalsInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 2, 2, 1)
)
cie1000DhcpServerConfigGlobalsInfoGroup.setObjects(
    ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigGlobalsMode")
)
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigGlobalsInfoGroup.setStatus("current")

cie1000DhcpServerConfigVlanTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 2, 2, 2)
)
cie1000DhcpServerConfigVlanTableInfoGroup.setObjects(
      *(("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigVlanIfIndex"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigVlanMode"))
)
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigVlanTableInfoGroup.setStatus("current")

cie1000DhcpServerConfigExcludedTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 2, 2, 3)
)
cie1000DhcpServerConfigExcludedTableInfoGroup.setObjects(
      *(("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigExcludedLowIpAddress"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigExcludedHighIpAddress"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigExcludedAction"))
)
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigExcludedTableInfoGroup.setStatus("current")

cie1000DhcpServerConfigExcludedIpTableRowEditorInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 2, 2, 4)
)
cie1000DhcpServerConfigExcludedIpTableRowEditorInfoGroup.setObjects(
      *(("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigExcludedIpTableRowEditorLowIpAddress"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigExcludedIpTableRowEditorHighIpAddress"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigExcludedIpTableRowEditorAction"))
)
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigExcludedIpTableRowEditorInfoGroup.setStatus("current")

cie1000DhcpServerConfigPoolTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 2, 2, 5)
)
cie1000DhcpServerConfigPoolTableInfoGroup.setObjects(
      *(("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigPoolPoolName"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigPoolPoolType"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigPoolIpv4Address"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigPoolSubnetMask"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigPoolSubnetBroadcast"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigPoolLeaseDay"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigPoolLeaseHour"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigPoolLeaseMinute"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigPoolDomainName"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigPoolDefaultRouter1"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigPoolDefaultRouter2"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigPoolDefaultRouter3"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigPoolDefaultRouter4"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigPoolDnsServer1"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigPoolDnsServer2"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigPoolDnsServer3"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigPoolDnsServer4"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigPoolNtpServer1"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigPoolNtpServer2"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigPoolNtpServer3"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigPoolNtpServer4"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigPoolNetbiosNodeType"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigPoolNetbiosScope"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigPoolNetbiosNameServer1"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigPoolNetbiosNameServer2"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigPoolNetbiosNameServer3"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigPoolNetbiosNameServer4"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigPoolNisDomainName"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigPoolNisServer1"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigPoolNisServer2"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigPoolNisServer3"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigPoolNisServer4"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigPoolClientIdentifierType"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigPoolClientIdentifierName"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigPoolClientIdentifierMac"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigPoolClientHardwareAddress"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigPoolClientName"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigPoolVendorClassId1"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigPoolVendorSpecificInfo1"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigPoolVendorClassId2"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigPoolVendorSpecificInfo2"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigPoolVendorClassId3"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigPoolVendorSpecificInfo3"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigPoolVendorClassId4"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigPoolVendorSpecificInfo4"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigPoolAction"))
)
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigPoolTableInfoGroup.setStatus("current")

cie1000DhcpServerConfigPoolTableRowEditorInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 2, 2, 6)
)
cie1000DhcpServerConfigPoolTableRowEditorInfoGroup.setObjects(
      *(("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigPoolTableRowEditorPoolName"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigPoolTableRowEditorPoolType"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigPoolTableRowEditorIpv4Address"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigPoolTableRowEditorSubnetMask"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigPoolTableRowEditorSubnetBroadcast"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigPoolTableRowEditorLeaseDay"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigPoolTableRowEditorLeaseHour"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigPoolTableRowEditorLeaseMinute"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigPoolTableRowEditorDomainName"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigPoolTableRowEditorDefaultRouter1"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigPoolTableRowEditorDefaultRouter2"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigPoolTableRowEditorDefaultRouter3"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigPoolTableRowEditorDefaultRouter4"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigPoolTableRowEditorDnsServer1"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigPoolTableRowEditorDnsServer2"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigPoolTableRowEditorDnsServer3"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigPoolTableRowEditorDnsServer4"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigPoolTableRowEditorNtpServer1"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigPoolTableRowEditorNtpServer2"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigPoolTableRowEditorNtpServer3"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigPoolTableRowEditorNtpServer4"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigPoolTableRowEditorNetbiosNodeType"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigPoolTableRowEditorNetbiosScope"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigPoolTableRowEditorNetbiosNameServer1"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigPoolTableRowEditorNetbiosNameServer2"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigPoolTableRowEditorNetbiosNameServer3"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigPoolTableRowEditorNetbiosNameServer4"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigPoolTableRowEditorNisDomainName"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigPoolTableRowEditorNisServer1"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigPoolTableRowEditorNisServer2"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigPoolTableRowEditorNisServer3"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigPoolTableRowEditorNisServer4"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigPoolTableRowEditorClientIdentifierType"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigPoolTableRowEditorClientIdentifierName"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigPoolTableRowEditorClientIdentifierMac"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigPoolTableRowEditorClientHardwareAddress"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigPoolTableRowEditorClientName"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigPoolTableRowEditorVendorClassId1"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigPoolTableRowEditorVendorSpecificInfo1"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigPoolTableRowEditorVendorClassId2"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigPoolTableRowEditorVendorSpecificInfo2"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigPoolTableRowEditorVendorClassId3"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigPoolTableRowEditorVendorSpecificInfo3"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigPoolTableRowEditorVendorClassId4"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigPoolTableRowEditorVendorSpecificInfo4"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigPoolTableRowEditorAction"))
)
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigPoolTableRowEditorInfoGroup.setStatus("current")

cie1000DhcpServerConfigReservedTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 2, 2, 7)
)
cie1000DhcpServerConfigReservedTableInfoGroup.setObjects(
      *(("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigReservedPoolName"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigReservedIpAddress"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigReservedIfIndex"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigReservedAction"))
)
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigReservedTableInfoGroup.setStatus("current")

cie1000DhcpServerConfigReservedIpTableRowEditorInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 2, 2, 8)
)
cie1000DhcpServerConfigReservedIpTableRowEditorInfoGroup.setObjects(
      *(("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigReservedIpTableRowEditorPoolName"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigReservedIpTableRowEditorIpAddress"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigReservedIpTableRowEditorIfIndex"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigReservedIpTableRowEditorAction"))
)
if mibBuilder.loadTexts:
    cie1000DhcpServerConfigReservedIpTableRowEditorInfoGroup.setStatus("current")

cie1000DhcpServerStatusDeclinedTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 2, 2, 9)
)
cie1000DhcpServerStatusDeclinedTableInfoGroup.setObjects(
      *(("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerStatusDeclinedEntryNo"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerStatusDeclinedIpv4Address"))
)
if mibBuilder.loadTexts:
    cie1000DhcpServerStatusDeclinedTableInfoGroup.setStatus("current")

cie1000DhcpServerStatusStatisticsInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 2, 2, 10)
)
cie1000DhcpServerStatusStatisticsInfoGroup.setObjects(
      *(("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerStatusStatisticsDiscoverCnt"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerStatusStatisticsOfferCnt"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerStatusStatisticsRequestCnt"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerStatusStatisticsAckCnt"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerStatusStatisticsNakCnt"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerStatusStatisticsDeclineCnt"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerStatusStatisticsReleaseCnt"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerStatusStatisticsInformCnt"))
)
if mibBuilder.loadTexts:
    cie1000DhcpServerStatusStatisticsInfoGroup.setStatus("current")

cie1000DhcpServerStatusBindingTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 2, 2, 11)
)
cie1000DhcpServerStatusBindingTableInfoGroup.setObjects(
      *(("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerStatusBindingIpAddress"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerStatusBindingState"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerStatusBindingType"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerStatusBindingPoolName"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerStatusBindingServerId"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerStatusBindingVlanId"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerStatusBindingSubnetMask"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerStatusBindingClientIdentifierType"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerStatusBindingClientIdentifierName"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerStatusBindingClientIdentifierMac"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerStatusBindingMacAddress"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerStatusBindingLease"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerStatusBindingTimeToExpire"))
)
if mibBuilder.loadTexts:
    cie1000DhcpServerStatusBindingTableInfoGroup.setStatus("current")

cie1000DhcpServerControlStatisticsInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 2, 2, 12)
)
cie1000DhcpServerControlStatisticsInfoGroup.setObjects(
    ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerControlStatisticsClear")
)
if mibBuilder.loadTexts:
    cie1000DhcpServerControlStatisticsInfoGroup.setStatus("current")

cie1000DhcpServerControlBindingInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 2, 2, 13)
)
cie1000DhcpServerControlBindingInfoGroup.setObjects(
      *(("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerControlBindingClearByIp"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerControlBindingClearByType"))
)
if mibBuilder.loadTexts:
    cie1000DhcpServerControlBindingInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cie1000DhcpServerMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 109, 2, 1, 1)
)
cie1000DhcpServerMibCompliance.setObjects(
      *(("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigGlobalsInfoGroup"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigVlanTableInfoGroup"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigExcludedTableInfoGroup"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigExcludedIpTableRowEditorInfoGroup"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigPoolTableInfoGroup"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigPoolTableRowEditorInfoGroup"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigReservedTableInfoGroup"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerConfigReservedIpTableRowEditorInfoGroup"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerStatusDeclinedTableInfoGroup"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerStatusStatisticsInfoGroup"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerStatusBindingTableInfoGroup"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerControlStatisticsInfoGroup"),
        ("CIE1000-DHCP-SERVER-MIB", "cie1000DhcpServerControlBindingInfoGroup"))
)
if mibBuilder.loadTexts:
    cie1000DhcpServerMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIE1000-DHCP-SERVER-MIB",
    **{"CIE1000DhcpServerBindingEnum": CIE1000DhcpServerBindingEnum,
       "CIE1000DhcpServerBindingStateEnum": CIE1000DhcpServerBindingStateEnum,
       "CIE1000DhcpServerClientIdentifierEnum": CIE1000DhcpServerClientIdentifierEnum,
       "CIE1000DhcpServerNetbiosNodeEnum": CIE1000DhcpServerNetbiosNodeEnum,
       "CIE1000DhcpServerPoolEnum": CIE1000DhcpServerPoolEnum,
       "cie1000DhcpServerMib": cie1000DhcpServerMib,
       "cie1000DhcpServerMibObjects": cie1000DhcpServerMibObjects,
       "cie1000DhcpServerConfig": cie1000DhcpServerConfig,
       "cie1000DhcpServerConfigGlobals": cie1000DhcpServerConfigGlobals,
       "cie1000DhcpServerConfigGlobalsMode": cie1000DhcpServerConfigGlobalsMode,
       "cie1000DhcpServerConfigVlanTable": cie1000DhcpServerConfigVlanTable,
       "cie1000DhcpServerConfigVlanEntry": cie1000DhcpServerConfigVlanEntry,
       "cie1000DhcpServerConfigVlanIfIndex": cie1000DhcpServerConfigVlanIfIndex,
       "cie1000DhcpServerConfigVlanMode": cie1000DhcpServerConfigVlanMode,
       "cie1000DhcpServerConfigExcludedTable": cie1000DhcpServerConfigExcludedTable,
       "cie1000DhcpServerConfigExcludedEntry": cie1000DhcpServerConfigExcludedEntry,
       "cie1000DhcpServerConfigExcludedLowIpAddress": cie1000DhcpServerConfigExcludedLowIpAddress,
       "cie1000DhcpServerConfigExcludedHighIpAddress": cie1000DhcpServerConfigExcludedHighIpAddress,
       "cie1000DhcpServerConfigExcludedAction": cie1000DhcpServerConfigExcludedAction,
       "cie1000DhcpServerConfigExcludedIpTableRowEditor": cie1000DhcpServerConfigExcludedIpTableRowEditor,
       "cie1000DhcpServerConfigExcludedIpTableRowEditorLowIpAddress": cie1000DhcpServerConfigExcludedIpTableRowEditorLowIpAddress,
       "cie1000DhcpServerConfigExcludedIpTableRowEditorHighIpAddress": cie1000DhcpServerConfigExcludedIpTableRowEditorHighIpAddress,
       "cie1000DhcpServerConfigExcludedIpTableRowEditorAction": cie1000DhcpServerConfigExcludedIpTableRowEditorAction,
       "cie1000DhcpServerConfigPoolTable": cie1000DhcpServerConfigPoolTable,
       "cie1000DhcpServerConfigPoolEntry": cie1000DhcpServerConfigPoolEntry,
       "cie1000DhcpServerConfigPoolPoolName": cie1000DhcpServerConfigPoolPoolName,
       "cie1000DhcpServerConfigPoolPoolType": cie1000DhcpServerConfigPoolPoolType,
       "cie1000DhcpServerConfigPoolIpv4Address": cie1000DhcpServerConfigPoolIpv4Address,
       "cie1000DhcpServerConfigPoolSubnetMask": cie1000DhcpServerConfigPoolSubnetMask,
       "cie1000DhcpServerConfigPoolSubnetBroadcast": cie1000DhcpServerConfigPoolSubnetBroadcast,
       "cie1000DhcpServerConfigPoolLeaseDay": cie1000DhcpServerConfigPoolLeaseDay,
       "cie1000DhcpServerConfigPoolLeaseHour": cie1000DhcpServerConfigPoolLeaseHour,
       "cie1000DhcpServerConfigPoolLeaseMinute": cie1000DhcpServerConfigPoolLeaseMinute,
       "cie1000DhcpServerConfigPoolDomainName": cie1000DhcpServerConfigPoolDomainName,
       "cie1000DhcpServerConfigPoolDefaultRouter1": cie1000DhcpServerConfigPoolDefaultRouter1,
       "cie1000DhcpServerConfigPoolDefaultRouter2": cie1000DhcpServerConfigPoolDefaultRouter2,
       "cie1000DhcpServerConfigPoolDefaultRouter3": cie1000DhcpServerConfigPoolDefaultRouter3,
       "cie1000DhcpServerConfigPoolDefaultRouter4": cie1000DhcpServerConfigPoolDefaultRouter4,
       "cie1000DhcpServerConfigPoolDnsServer1": cie1000DhcpServerConfigPoolDnsServer1,
       "cie1000DhcpServerConfigPoolDnsServer2": cie1000DhcpServerConfigPoolDnsServer2,
       "cie1000DhcpServerConfigPoolDnsServer3": cie1000DhcpServerConfigPoolDnsServer3,
       "cie1000DhcpServerConfigPoolDnsServer4": cie1000DhcpServerConfigPoolDnsServer4,
       "cie1000DhcpServerConfigPoolNtpServer1": cie1000DhcpServerConfigPoolNtpServer1,
       "cie1000DhcpServerConfigPoolNtpServer2": cie1000DhcpServerConfigPoolNtpServer2,
       "cie1000DhcpServerConfigPoolNtpServer3": cie1000DhcpServerConfigPoolNtpServer3,
       "cie1000DhcpServerConfigPoolNtpServer4": cie1000DhcpServerConfigPoolNtpServer4,
       "cie1000DhcpServerConfigPoolNetbiosNodeType": cie1000DhcpServerConfigPoolNetbiosNodeType,
       "cie1000DhcpServerConfigPoolNetbiosScope": cie1000DhcpServerConfigPoolNetbiosScope,
       "cie1000DhcpServerConfigPoolNetbiosNameServer1": cie1000DhcpServerConfigPoolNetbiosNameServer1,
       "cie1000DhcpServerConfigPoolNetbiosNameServer2": cie1000DhcpServerConfigPoolNetbiosNameServer2,
       "cie1000DhcpServerConfigPoolNetbiosNameServer3": cie1000DhcpServerConfigPoolNetbiosNameServer3,
       "cie1000DhcpServerConfigPoolNetbiosNameServer4": cie1000DhcpServerConfigPoolNetbiosNameServer4,
       "cie1000DhcpServerConfigPoolNisDomainName": cie1000DhcpServerConfigPoolNisDomainName,
       "cie1000DhcpServerConfigPoolNisServer1": cie1000DhcpServerConfigPoolNisServer1,
       "cie1000DhcpServerConfigPoolNisServer2": cie1000DhcpServerConfigPoolNisServer2,
       "cie1000DhcpServerConfigPoolNisServer3": cie1000DhcpServerConfigPoolNisServer3,
       "cie1000DhcpServerConfigPoolNisServer4": cie1000DhcpServerConfigPoolNisServer4,
       "cie1000DhcpServerConfigPoolClientIdentifierType": cie1000DhcpServerConfigPoolClientIdentifierType,
       "cie1000DhcpServerConfigPoolClientIdentifierName": cie1000DhcpServerConfigPoolClientIdentifierName,
       "cie1000DhcpServerConfigPoolClientIdentifierMac": cie1000DhcpServerConfigPoolClientIdentifierMac,
       "cie1000DhcpServerConfigPoolClientHardwareAddress": cie1000DhcpServerConfigPoolClientHardwareAddress,
       "cie1000DhcpServerConfigPoolClientName": cie1000DhcpServerConfigPoolClientName,
       "cie1000DhcpServerConfigPoolVendorClassId1": cie1000DhcpServerConfigPoolVendorClassId1,
       "cie1000DhcpServerConfigPoolVendorSpecificInfo1": cie1000DhcpServerConfigPoolVendorSpecificInfo1,
       "cie1000DhcpServerConfigPoolVendorClassId2": cie1000DhcpServerConfigPoolVendorClassId2,
       "cie1000DhcpServerConfigPoolVendorSpecificInfo2": cie1000DhcpServerConfigPoolVendorSpecificInfo2,
       "cie1000DhcpServerConfigPoolVendorClassId3": cie1000DhcpServerConfigPoolVendorClassId3,
       "cie1000DhcpServerConfigPoolVendorSpecificInfo3": cie1000DhcpServerConfigPoolVendorSpecificInfo3,
       "cie1000DhcpServerConfigPoolVendorClassId4": cie1000DhcpServerConfigPoolVendorClassId4,
       "cie1000DhcpServerConfigPoolVendorSpecificInfo4": cie1000DhcpServerConfigPoolVendorSpecificInfo4,
       "cie1000DhcpServerConfigPoolAction": cie1000DhcpServerConfigPoolAction,
       "cie1000DhcpServerConfigPoolTableRowEditor": cie1000DhcpServerConfigPoolTableRowEditor,
       "cie1000DhcpServerConfigPoolTableRowEditorPoolName": cie1000DhcpServerConfigPoolTableRowEditorPoolName,
       "cie1000DhcpServerConfigPoolTableRowEditorPoolType": cie1000DhcpServerConfigPoolTableRowEditorPoolType,
       "cie1000DhcpServerConfigPoolTableRowEditorIpv4Address": cie1000DhcpServerConfigPoolTableRowEditorIpv4Address,
       "cie1000DhcpServerConfigPoolTableRowEditorSubnetMask": cie1000DhcpServerConfigPoolTableRowEditorSubnetMask,
       "cie1000DhcpServerConfigPoolTableRowEditorSubnetBroadcast": cie1000DhcpServerConfigPoolTableRowEditorSubnetBroadcast,
       "cie1000DhcpServerConfigPoolTableRowEditorLeaseDay": cie1000DhcpServerConfigPoolTableRowEditorLeaseDay,
       "cie1000DhcpServerConfigPoolTableRowEditorLeaseHour": cie1000DhcpServerConfigPoolTableRowEditorLeaseHour,
       "cie1000DhcpServerConfigPoolTableRowEditorLeaseMinute": cie1000DhcpServerConfigPoolTableRowEditorLeaseMinute,
       "cie1000DhcpServerConfigPoolTableRowEditorDomainName": cie1000DhcpServerConfigPoolTableRowEditorDomainName,
       "cie1000DhcpServerConfigPoolTableRowEditorDefaultRouter1": cie1000DhcpServerConfigPoolTableRowEditorDefaultRouter1,
       "cie1000DhcpServerConfigPoolTableRowEditorDefaultRouter2": cie1000DhcpServerConfigPoolTableRowEditorDefaultRouter2,
       "cie1000DhcpServerConfigPoolTableRowEditorDefaultRouter3": cie1000DhcpServerConfigPoolTableRowEditorDefaultRouter3,
       "cie1000DhcpServerConfigPoolTableRowEditorDefaultRouter4": cie1000DhcpServerConfigPoolTableRowEditorDefaultRouter4,
       "cie1000DhcpServerConfigPoolTableRowEditorDnsServer1": cie1000DhcpServerConfigPoolTableRowEditorDnsServer1,
       "cie1000DhcpServerConfigPoolTableRowEditorDnsServer2": cie1000DhcpServerConfigPoolTableRowEditorDnsServer2,
       "cie1000DhcpServerConfigPoolTableRowEditorDnsServer3": cie1000DhcpServerConfigPoolTableRowEditorDnsServer3,
       "cie1000DhcpServerConfigPoolTableRowEditorDnsServer4": cie1000DhcpServerConfigPoolTableRowEditorDnsServer4,
       "cie1000DhcpServerConfigPoolTableRowEditorNtpServer1": cie1000DhcpServerConfigPoolTableRowEditorNtpServer1,
       "cie1000DhcpServerConfigPoolTableRowEditorNtpServer2": cie1000DhcpServerConfigPoolTableRowEditorNtpServer2,
       "cie1000DhcpServerConfigPoolTableRowEditorNtpServer3": cie1000DhcpServerConfigPoolTableRowEditorNtpServer3,
       "cie1000DhcpServerConfigPoolTableRowEditorNtpServer4": cie1000DhcpServerConfigPoolTableRowEditorNtpServer4,
       "cie1000DhcpServerConfigPoolTableRowEditorNetbiosNodeType": cie1000DhcpServerConfigPoolTableRowEditorNetbiosNodeType,
       "cie1000DhcpServerConfigPoolTableRowEditorNetbiosScope": cie1000DhcpServerConfigPoolTableRowEditorNetbiosScope,
       "cie1000DhcpServerConfigPoolTableRowEditorNetbiosNameServer1": cie1000DhcpServerConfigPoolTableRowEditorNetbiosNameServer1,
       "cie1000DhcpServerConfigPoolTableRowEditorNetbiosNameServer2": cie1000DhcpServerConfigPoolTableRowEditorNetbiosNameServer2,
       "cie1000DhcpServerConfigPoolTableRowEditorNetbiosNameServer3": cie1000DhcpServerConfigPoolTableRowEditorNetbiosNameServer3,
       "cie1000DhcpServerConfigPoolTableRowEditorNetbiosNameServer4": cie1000DhcpServerConfigPoolTableRowEditorNetbiosNameServer4,
       "cie1000DhcpServerConfigPoolTableRowEditorNisDomainName": cie1000DhcpServerConfigPoolTableRowEditorNisDomainName,
       "cie1000DhcpServerConfigPoolTableRowEditorNisServer1": cie1000DhcpServerConfigPoolTableRowEditorNisServer1,
       "cie1000DhcpServerConfigPoolTableRowEditorNisServer2": cie1000DhcpServerConfigPoolTableRowEditorNisServer2,
       "cie1000DhcpServerConfigPoolTableRowEditorNisServer3": cie1000DhcpServerConfigPoolTableRowEditorNisServer3,
       "cie1000DhcpServerConfigPoolTableRowEditorNisServer4": cie1000DhcpServerConfigPoolTableRowEditorNisServer4,
       "cie1000DhcpServerConfigPoolTableRowEditorClientIdentifierType": cie1000DhcpServerConfigPoolTableRowEditorClientIdentifierType,
       "cie1000DhcpServerConfigPoolTableRowEditorClientIdentifierName": cie1000DhcpServerConfigPoolTableRowEditorClientIdentifierName,
       "cie1000DhcpServerConfigPoolTableRowEditorClientIdentifierMac": cie1000DhcpServerConfigPoolTableRowEditorClientIdentifierMac,
       "cie1000DhcpServerConfigPoolTableRowEditorClientHardwareAddress": cie1000DhcpServerConfigPoolTableRowEditorClientHardwareAddress,
       "cie1000DhcpServerConfigPoolTableRowEditorClientName": cie1000DhcpServerConfigPoolTableRowEditorClientName,
       "cie1000DhcpServerConfigPoolTableRowEditorVendorClassId1": cie1000DhcpServerConfigPoolTableRowEditorVendorClassId1,
       "cie1000DhcpServerConfigPoolTableRowEditorVendorSpecificInfo1": cie1000DhcpServerConfigPoolTableRowEditorVendorSpecificInfo1,
       "cie1000DhcpServerConfigPoolTableRowEditorVendorClassId2": cie1000DhcpServerConfigPoolTableRowEditorVendorClassId2,
       "cie1000DhcpServerConfigPoolTableRowEditorVendorSpecificInfo2": cie1000DhcpServerConfigPoolTableRowEditorVendorSpecificInfo2,
       "cie1000DhcpServerConfigPoolTableRowEditorVendorClassId3": cie1000DhcpServerConfigPoolTableRowEditorVendorClassId3,
       "cie1000DhcpServerConfigPoolTableRowEditorVendorSpecificInfo3": cie1000DhcpServerConfigPoolTableRowEditorVendorSpecificInfo3,
       "cie1000DhcpServerConfigPoolTableRowEditorVendorClassId4": cie1000DhcpServerConfigPoolTableRowEditorVendorClassId4,
       "cie1000DhcpServerConfigPoolTableRowEditorVendorSpecificInfo4": cie1000DhcpServerConfigPoolTableRowEditorVendorSpecificInfo4,
       "cie1000DhcpServerConfigPoolTableRowEditorAction": cie1000DhcpServerConfigPoolTableRowEditorAction,
       "cie1000DhcpServerConfigReservedTable": cie1000DhcpServerConfigReservedTable,
       "cie1000DhcpServerConfigReservedEntry": cie1000DhcpServerConfigReservedEntry,
       "cie1000DhcpServerConfigReservedPoolName": cie1000DhcpServerConfigReservedPoolName,
       "cie1000DhcpServerConfigReservedIpAddress": cie1000DhcpServerConfigReservedIpAddress,
       "cie1000DhcpServerConfigReservedIfIndex": cie1000DhcpServerConfigReservedIfIndex,
       "cie1000DhcpServerConfigReservedAction": cie1000DhcpServerConfigReservedAction,
       "cie1000DhcpServerConfigReservedIpTableRowEditor": cie1000DhcpServerConfigReservedIpTableRowEditor,
       "cie1000DhcpServerConfigReservedIpTableRowEditorPoolName": cie1000DhcpServerConfigReservedIpTableRowEditorPoolName,
       "cie1000DhcpServerConfigReservedIpTableRowEditorIpAddress": cie1000DhcpServerConfigReservedIpTableRowEditorIpAddress,
       "cie1000DhcpServerConfigReservedIpTableRowEditorIfIndex": cie1000DhcpServerConfigReservedIpTableRowEditorIfIndex,
       "cie1000DhcpServerConfigReservedIpTableRowEditorAction": cie1000DhcpServerConfigReservedIpTableRowEditorAction,
       "cie1000DhcpServerStatus": cie1000DhcpServerStatus,
       "cie1000DhcpServerStatusDeclinedTable": cie1000DhcpServerStatusDeclinedTable,
       "cie1000DhcpServerStatusDeclinedEntry": cie1000DhcpServerStatusDeclinedEntry,
       "cie1000DhcpServerStatusDeclinedEntryNo": cie1000DhcpServerStatusDeclinedEntryNo,
       "cie1000DhcpServerStatusDeclinedIpv4Address": cie1000DhcpServerStatusDeclinedIpv4Address,
       "cie1000DhcpServerStatusStatistics": cie1000DhcpServerStatusStatistics,
       "cie1000DhcpServerStatusStatisticsDiscoverCnt": cie1000DhcpServerStatusStatisticsDiscoverCnt,
       "cie1000DhcpServerStatusStatisticsOfferCnt": cie1000DhcpServerStatusStatisticsOfferCnt,
       "cie1000DhcpServerStatusStatisticsRequestCnt": cie1000DhcpServerStatusStatisticsRequestCnt,
       "cie1000DhcpServerStatusStatisticsAckCnt": cie1000DhcpServerStatusStatisticsAckCnt,
       "cie1000DhcpServerStatusStatisticsNakCnt": cie1000DhcpServerStatusStatisticsNakCnt,
       "cie1000DhcpServerStatusStatisticsDeclineCnt": cie1000DhcpServerStatusStatisticsDeclineCnt,
       "cie1000DhcpServerStatusStatisticsReleaseCnt": cie1000DhcpServerStatusStatisticsReleaseCnt,
       "cie1000DhcpServerStatusStatisticsInformCnt": cie1000DhcpServerStatusStatisticsInformCnt,
       "cie1000DhcpServerStatusBindingTable": cie1000DhcpServerStatusBindingTable,
       "cie1000DhcpServerStatusBindingEntry": cie1000DhcpServerStatusBindingEntry,
       "cie1000DhcpServerStatusBindingIpAddress": cie1000DhcpServerStatusBindingIpAddress,
       "cie1000DhcpServerStatusBindingState": cie1000DhcpServerStatusBindingState,
       "cie1000DhcpServerStatusBindingType": cie1000DhcpServerStatusBindingType,
       "cie1000DhcpServerStatusBindingPoolName": cie1000DhcpServerStatusBindingPoolName,
       "cie1000DhcpServerStatusBindingServerId": cie1000DhcpServerStatusBindingServerId,
       "cie1000DhcpServerStatusBindingVlanId": cie1000DhcpServerStatusBindingVlanId,
       "cie1000DhcpServerStatusBindingSubnetMask": cie1000DhcpServerStatusBindingSubnetMask,
       "cie1000DhcpServerStatusBindingClientIdentifierType": cie1000DhcpServerStatusBindingClientIdentifierType,
       "cie1000DhcpServerStatusBindingClientIdentifierName": cie1000DhcpServerStatusBindingClientIdentifierName,
       "cie1000DhcpServerStatusBindingClientIdentifierMac": cie1000DhcpServerStatusBindingClientIdentifierMac,
       "cie1000DhcpServerStatusBindingMacAddress": cie1000DhcpServerStatusBindingMacAddress,
       "cie1000DhcpServerStatusBindingLease": cie1000DhcpServerStatusBindingLease,
       "cie1000DhcpServerStatusBindingTimeToExpire": cie1000DhcpServerStatusBindingTimeToExpire,
       "cie1000DhcpServerControl": cie1000DhcpServerControl,
       "cie1000DhcpServerControlStatistics": cie1000DhcpServerControlStatistics,
       "cie1000DhcpServerControlStatisticsClear": cie1000DhcpServerControlStatisticsClear,
       "cie1000DhcpServerControlBinding": cie1000DhcpServerControlBinding,
       "cie1000DhcpServerControlBindingClearByIp": cie1000DhcpServerControlBindingClearByIp,
       "cie1000DhcpServerControlBindingClearByType": cie1000DhcpServerControlBindingClearByType,
       "cie1000DhcpServerMibConformance": cie1000DhcpServerMibConformance,
       "cie1000DhcpServerMibCompliances": cie1000DhcpServerMibCompliances,
       "cie1000DhcpServerMibCompliance": cie1000DhcpServerMibCompliance,
       "cie1000DhcpServerMibGroups": cie1000DhcpServerMibGroups,
       "cie1000DhcpServerConfigGlobalsInfoGroup": cie1000DhcpServerConfigGlobalsInfoGroup,
       "cie1000DhcpServerConfigVlanTableInfoGroup": cie1000DhcpServerConfigVlanTableInfoGroup,
       "cie1000DhcpServerConfigExcludedTableInfoGroup": cie1000DhcpServerConfigExcludedTableInfoGroup,
       "cie1000DhcpServerConfigExcludedIpTableRowEditorInfoGroup": cie1000DhcpServerConfigExcludedIpTableRowEditorInfoGroup,
       "cie1000DhcpServerConfigPoolTableInfoGroup": cie1000DhcpServerConfigPoolTableInfoGroup,
       "cie1000DhcpServerConfigPoolTableRowEditorInfoGroup": cie1000DhcpServerConfigPoolTableRowEditorInfoGroup,
       "cie1000DhcpServerConfigReservedTableInfoGroup": cie1000DhcpServerConfigReservedTableInfoGroup,
       "cie1000DhcpServerConfigReservedIpTableRowEditorInfoGroup": cie1000DhcpServerConfigReservedIpTableRowEditorInfoGroup,
       "cie1000DhcpServerStatusDeclinedTableInfoGroup": cie1000DhcpServerStatusDeclinedTableInfoGroup,
       "cie1000DhcpServerStatusStatisticsInfoGroup": cie1000DhcpServerStatusStatisticsInfoGroup,
       "cie1000DhcpServerStatusBindingTableInfoGroup": cie1000DhcpServerStatusBindingTableInfoGroup,
       "cie1000DhcpServerControlStatisticsInfoGroup": cie1000DhcpServerControlStatisticsInfoGroup,
       "cie1000DhcpServerControlBindingInfoGroup": cie1000DhcpServerControlBindingInfoGroup}
)
