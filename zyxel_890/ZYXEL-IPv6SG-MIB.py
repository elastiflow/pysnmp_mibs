# SNMP MIB module (ZYXEL-IPv6SG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/zyxel_890/ZYXEL-IPv6SG-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 08:46:21 2025
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

(dot1dBasePort,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "dot1dBasePort")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

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

(esMgmt,) = mibBuilder.importSymbols(
    "ZYXEL-ES-SMI",
    "esMgmt")


# MODULE-IDENTITY

zyxelIpv6sg = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 108)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelIpv6sgSetup_ObjectIdentity = ObjectIdentity
zyxelIpv6sgSetup = _ZyxelIpv6sgSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 108, 1)
)
_ZyxelIpv6sgStaticBindingMaxNumberOfRules_Type = Integer32
_ZyxelIpv6sgStaticBindingMaxNumberOfRules_Object = MibScalar
zyxelIpv6sgStaticBindingMaxNumberOfRules = _ZyxelIpv6sgStaticBindingMaxNumberOfRules_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 108, 1, 1),
    _ZyxelIpv6sgStaticBindingMaxNumberOfRules_Type()
)
zyxelIpv6sgStaticBindingMaxNumberOfRules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyxelIpv6sgStaticBindingMaxNumberOfRules.setStatus("current")
_ZyxelIpv6sgStaticBindingTable_Object = MibTable
zyxelIpv6sgStaticBindingTable = _ZyxelIpv6sgStaticBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 108, 1, 2)
)
if mibBuilder.loadTexts:
    zyxelIpv6sgStaticBindingTable.setStatus("current")
_ZyxelIpv6sgStaticBindingEntry_Object = MibTableRow
zyxelIpv6sgStaticBindingEntry = _ZyxelIpv6sgStaticBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 108, 1, 2, 1)
)
zyxelIpv6sgStaticBindingEntry.setIndexNames(
    (0, "ZYXEL-IPv6SG-MIB", "zyIpv6sgStaticBindingIpv6AddressType"),
    (0, "ZYXEL-IPv6SG-MIB", "zyIpv6sgStaticBindingIpv6Address"),
    (0, "ZYXEL-IPv6SG-MIB", "zyIpv6sgStaticBindingIpv6PrefixLength"),
)
if mibBuilder.loadTexts:
    zyxelIpv6sgStaticBindingEntry.setStatus("current")
_ZyIpv6sgStaticBindingIpv6AddressType_Type = InetAddressType
_ZyIpv6sgStaticBindingIpv6AddressType_Object = MibTableColumn
zyIpv6sgStaticBindingIpv6AddressType = _ZyIpv6sgStaticBindingIpv6AddressType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 108, 1, 2, 1, 1),
    _ZyIpv6sgStaticBindingIpv6AddressType_Type()
)
zyIpv6sgStaticBindingIpv6AddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyIpv6sgStaticBindingIpv6AddressType.setStatus("current")
_ZyIpv6sgStaticBindingIpv6Address_Type = InetAddress
_ZyIpv6sgStaticBindingIpv6Address_Object = MibTableColumn
zyIpv6sgStaticBindingIpv6Address = _ZyIpv6sgStaticBindingIpv6Address_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 108, 1, 2, 1, 2),
    _ZyIpv6sgStaticBindingIpv6Address_Type()
)
zyIpv6sgStaticBindingIpv6Address.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyIpv6sgStaticBindingIpv6Address.setStatus("current")
_ZyIpv6sgStaticBindingIpv6PrefixLength_Type = Integer32
_ZyIpv6sgStaticBindingIpv6PrefixLength_Object = MibTableColumn
zyIpv6sgStaticBindingIpv6PrefixLength = _ZyIpv6sgStaticBindingIpv6PrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 108, 1, 2, 1, 3),
    _ZyIpv6sgStaticBindingIpv6PrefixLength_Type()
)
zyIpv6sgStaticBindingIpv6PrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyIpv6sgStaticBindingIpv6PrefixLength.setStatus("current")
_ZyIpv6sgStaticBindingMacAddress_Type = MacAddress
_ZyIpv6sgStaticBindingMacAddress_Object = MibTableColumn
zyIpv6sgStaticBindingMacAddress = _ZyIpv6sgStaticBindingMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 108, 1, 2, 1, 4),
    _ZyIpv6sgStaticBindingMacAddress_Type()
)
zyIpv6sgStaticBindingMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyIpv6sgStaticBindingMacAddress.setStatus("current")
_ZyIpv6sgStaticBindingVid_Type = Integer32
_ZyIpv6sgStaticBindingVid_Object = MibTableColumn
zyIpv6sgStaticBindingVid = _ZyIpv6sgStaticBindingVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 108, 1, 2, 1, 5),
    _ZyIpv6sgStaticBindingVid_Type()
)
zyIpv6sgStaticBindingVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyIpv6sgStaticBindingVid.setStatus("current")
_ZyIpv6sgStaticBindingPort_Type = Integer32
_ZyIpv6sgStaticBindingPort_Object = MibTableColumn
zyIpv6sgStaticBindingPort = _ZyIpv6sgStaticBindingPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 108, 1, 2, 1, 6),
    _ZyIpv6sgStaticBindingPort_Type()
)
zyIpv6sgStaticBindingPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyIpv6sgStaticBindingPort.setStatus("current")
_ZyIpv6sgStaticBindingRowStatus_Type = RowStatus
_ZyIpv6sgStaticBindingRowStatus_Object = MibTableColumn
zyIpv6sgStaticBindingRowStatus = _ZyIpv6sgStaticBindingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 108, 1, 2, 1, 7),
    _ZyIpv6sgStaticBindingRowStatus_Type()
)
zyIpv6sgStaticBindingRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyIpv6sgStaticBindingRowStatus.setStatus("current")
_ZyxelIpv6sgPolicyMaxNumberOfRules_Type = Integer32
_ZyxelIpv6sgPolicyMaxNumberOfRules_Object = MibScalar
zyxelIpv6sgPolicyMaxNumberOfRules = _ZyxelIpv6sgPolicyMaxNumberOfRules_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 108, 1, 3),
    _ZyxelIpv6sgPolicyMaxNumberOfRules_Type()
)
zyxelIpv6sgPolicyMaxNumberOfRules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyxelIpv6sgPolicyMaxNumberOfRules.setStatus("current")
_ZyxelIpv6sgPolicyTable_Object = MibTable
zyxelIpv6sgPolicyTable = _ZyxelIpv6sgPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 108, 1, 4)
)
if mibBuilder.loadTexts:
    zyxelIpv6sgPolicyTable.setStatus("current")
_ZyxelIpv6sgPolicyEntry_Object = MibTableRow
zyxelIpv6sgPolicyEntry = _ZyxelIpv6sgPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 108, 1, 4, 1)
)
zyxelIpv6sgPolicyEntry.setIndexNames(
    (0, "ZYXEL-IPv6SG-MIB", "zyIpv6sgPolicyName"),
)
if mibBuilder.loadTexts:
    zyxelIpv6sgPolicyEntry.setStatus("current")
_ZyIpv6sgPolicyName_Type = DisplayString
_ZyIpv6sgPolicyName_Object = MibTableColumn
zyIpv6sgPolicyName = _ZyIpv6sgPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 108, 1, 4, 1, 1),
    _ZyIpv6sgPolicyName_Type()
)
zyIpv6sgPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyIpv6sgPolicyName.setStatus("current")
_ZyIpv6sgPolicyValidateAddressState_Type = EnabledStatus
_ZyIpv6sgPolicyValidateAddressState_Object = MibTableColumn
zyIpv6sgPolicyValidateAddressState = _ZyIpv6sgPolicyValidateAddressState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 108, 1, 4, 1, 2),
    _ZyIpv6sgPolicyValidateAddressState_Type()
)
zyIpv6sgPolicyValidateAddressState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyIpv6sgPolicyValidateAddressState.setStatus("current")
_ZyIpv6sgPolicyValidatePrefixState_Type = EnabledStatus
_ZyIpv6sgPolicyValidatePrefixState_Object = MibTableColumn
zyIpv6sgPolicyValidatePrefixState = _ZyIpv6sgPolicyValidatePrefixState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 108, 1, 4, 1, 3),
    _ZyIpv6sgPolicyValidatePrefixState_Type()
)
zyIpv6sgPolicyValidatePrefixState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyIpv6sgPolicyValidatePrefixState.setStatus("current")
_ZyIpv6sgPolicyPermitLinkLocalState_Type = EnabledStatus
_ZyIpv6sgPolicyPermitLinkLocalState_Object = MibTableColumn
zyIpv6sgPolicyPermitLinkLocalState = _ZyIpv6sgPolicyPermitLinkLocalState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 108, 1, 4, 1, 4),
    _ZyIpv6sgPolicyPermitLinkLocalState_Type()
)
zyIpv6sgPolicyPermitLinkLocalState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyIpv6sgPolicyPermitLinkLocalState.setStatus("current")
_ZyIpv6sgPolicyRowStatus_Type = RowStatus
_ZyIpv6sgPolicyRowStatus_Object = MibTableColumn
zyIpv6sgPolicyRowStatus = _ZyIpv6sgPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 108, 1, 4, 1, 100),
    _ZyIpv6sgPolicyRowStatus_Type()
)
zyIpv6sgPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zyIpv6sgPolicyRowStatus.setStatus("current")
_ZyxelIpv6sgPolicyPortTable_Object = MibTable
zyxelIpv6sgPolicyPortTable = _ZyxelIpv6sgPolicyPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 108, 1, 5)
)
if mibBuilder.loadTexts:
    zyxelIpv6sgPolicyPortTable.setStatus("current")
_ZyxelIpv6sgPolicyPortEntry_Object = MibTableRow
zyxelIpv6sgPolicyPortEntry = _ZyxelIpv6sgPolicyPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 108, 1, 5, 1)
)
zyxelIpv6sgPolicyPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    zyxelIpv6sgPolicyPortEntry.setStatus("current")
_ZyIpv6sgPolicyPortAttachPolicy_Type = DisplayString
_ZyIpv6sgPolicyPortAttachPolicy_Object = MibTableColumn
zyIpv6sgPolicyPortAttachPolicy = _ZyIpv6sgPolicyPortAttachPolicy_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 108, 1, 5, 1, 1),
    _ZyIpv6sgPolicyPortAttachPolicy_Type()
)
zyIpv6sgPolicyPortAttachPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyIpv6sgPolicyPortAttachPolicy.setStatus("current")
_ZyxelIpv6sgStatus_ObjectIdentity = ObjectIdentity
zyxelIpv6sgStatus = _ZyxelIpv6sgStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 108, 2)
)
_ZyIpv6sgBindingClearAll_Type = EnabledStatus
_ZyIpv6sgBindingClearAll_Object = MibScalar
zyIpv6sgBindingClearAll = _ZyIpv6sgBindingClearAll_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 108, 2, 1),
    _ZyIpv6sgBindingClearAll_Type()
)
zyIpv6sgBindingClearAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyIpv6sgBindingClearAll.setStatus("current")
_ZyxelIpv6sgBindingTable_Object = MibTable
zyxelIpv6sgBindingTable = _ZyxelIpv6sgBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 108, 2, 2)
)
if mibBuilder.loadTexts:
    zyxelIpv6sgBindingTable.setStatus("current")
_ZyxelIpv6sgBindingEntry_Object = MibTableRow
zyxelIpv6sgBindingEntry = _ZyxelIpv6sgBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 108, 2, 2, 1)
)
zyxelIpv6sgBindingEntry.setIndexNames(
    (0, "ZYXEL-IPv6SG-MIB", "zyIpv6sgBindingIpv6AddressType"),
    (0, "ZYXEL-IPv6SG-MIB", "zyIpv6sgBindingIpv6Address"),
    (0, "ZYXEL-IPv6SG-MIB", "zyIpv6sgBindingIpv6PrefixLength"),
)
if mibBuilder.loadTexts:
    zyxelIpv6sgBindingEntry.setStatus("current")
_ZyIpv6sgBindingIpv6AddressType_Type = InetAddressType
_ZyIpv6sgBindingIpv6AddressType_Object = MibTableColumn
zyIpv6sgBindingIpv6AddressType = _ZyIpv6sgBindingIpv6AddressType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 108, 2, 2, 1, 1),
    _ZyIpv6sgBindingIpv6AddressType_Type()
)
zyIpv6sgBindingIpv6AddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyIpv6sgBindingIpv6AddressType.setStatus("current")
_ZyIpv6sgBindingIpv6Address_Type = InetAddress
_ZyIpv6sgBindingIpv6Address_Object = MibTableColumn
zyIpv6sgBindingIpv6Address = _ZyIpv6sgBindingIpv6Address_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 108, 2, 2, 1, 2),
    _ZyIpv6sgBindingIpv6Address_Type()
)
zyIpv6sgBindingIpv6Address.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyIpv6sgBindingIpv6Address.setStatus("current")
_ZyIpv6sgBindingIpv6PrefixLength_Type = Integer32
_ZyIpv6sgBindingIpv6PrefixLength_Object = MibTableColumn
zyIpv6sgBindingIpv6PrefixLength = _ZyIpv6sgBindingIpv6PrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 108, 2, 2, 1, 3),
    _ZyIpv6sgBindingIpv6PrefixLength_Type()
)
zyIpv6sgBindingIpv6PrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyIpv6sgBindingIpv6PrefixLength.setStatus("current")
_ZyIpv6sgBindingMacAddress_Type = MacAddress
_ZyIpv6sgBindingMacAddress_Object = MibTableColumn
zyIpv6sgBindingMacAddress = _ZyIpv6sgBindingMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 108, 2, 2, 1, 4),
    _ZyIpv6sgBindingMacAddress_Type()
)
zyIpv6sgBindingMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyIpv6sgBindingMacAddress.setStatus("current")
_ZyIpv6sgBindingVid_Type = Integer32
_ZyIpv6sgBindingVid_Object = MibTableColumn
zyIpv6sgBindingVid = _ZyIpv6sgBindingVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 108, 2, 2, 1, 5),
    _ZyIpv6sgBindingVid_Type()
)
zyIpv6sgBindingVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyIpv6sgBindingVid.setStatus("current")
_ZyIpv6sgBindingPort_Type = Integer32
_ZyIpv6sgBindingPort_Object = MibTableColumn
zyIpv6sgBindingPort = _ZyIpv6sgBindingPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 108, 2, 2, 1, 6),
    _ZyIpv6sgBindingPort_Type()
)
zyIpv6sgBindingPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyIpv6sgBindingPort.setStatus("current")
_ZyIpv6sgBindingLeaseTime_Type = Integer32
_ZyIpv6sgBindingLeaseTime_Object = MibTableColumn
zyIpv6sgBindingLeaseTime = _ZyIpv6sgBindingLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 108, 2, 2, 1, 7),
    _ZyIpv6sgBindingLeaseTime_Type()
)
zyIpv6sgBindingLeaseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyIpv6sgBindingLeaseTime.setStatus("current")


class _ZyIpv6sgBindingType_Type(Integer32):
    """Custom type zyIpv6sgBindingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("dhcp", 2))
    )


_ZyIpv6sgBindingType_Type.__name__ = "Integer32"
_ZyIpv6sgBindingType_Object = MibTableColumn
zyIpv6sgBindingType = _ZyIpv6sgBindingType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 108, 2, 2, 1, 8),
    _ZyIpv6sgBindingType_Type()
)
zyIpv6sgBindingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyIpv6sgBindingType.setStatus("current")
_ZyIpv6sgBindingClear_Type = EnabledStatus
_ZyIpv6sgBindingClear_Object = MibTableColumn
zyIpv6sgBindingClear = _ZyIpv6sgBindingClear_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 108, 2, 2, 1, 9),
    _ZyIpv6sgBindingClear_Type()
)
zyIpv6sgBindingClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyIpv6sgBindingClear.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-IPv6SG-MIB",
    **{"zyxelIpv6sg": zyxelIpv6sg,
       "zyxelIpv6sgSetup": zyxelIpv6sgSetup,
       "zyxelIpv6sgStaticBindingMaxNumberOfRules": zyxelIpv6sgStaticBindingMaxNumberOfRules,
       "zyxelIpv6sgStaticBindingTable": zyxelIpv6sgStaticBindingTable,
       "zyxelIpv6sgStaticBindingEntry": zyxelIpv6sgStaticBindingEntry,
       "zyIpv6sgStaticBindingIpv6AddressType": zyIpv6sgStaticBindingIpv6AddressType,
       "zyIpv6sgStaticBindingIpv6Address": zyIpv6sgStaticBindingIpv6Address,
       "zyIpv6sgStaticBindingIpv6PrefixLength": zyIpv6sgStaticBindingIpv6PrefixLength,
       "zyIpv6sgStaticBindingMacAddress": zyIpv6sgStaticBindingMacAddress,
       "zyIpv6sgStaticBindingVid": zyIpv6sgStaticBindingVid,
       "zyIpv6sgStaticBindingPort": zyIpv6sgStaticBindingPort,
       "zyIpv6sgStaticBindingRowStatus": zyIpv6sgStaticBindingRowStatus,
       "zyxelIpv6sgPolicyMaxNumberOfRules": zyxelIpv6sgPolicyMaxNumberOfRules,
       "zyxelIpv6sgPolicyTable": zyxelIpv6sgPolicyTable,
       "zyxelIpv6sgPolicyEntry": zyxelIpv6sgPolicyEntry,
       "zyIpv6sgPolicyName": zyIpv6sgPolicyName,
       "zyIpv6sgPolicyValidateAddressState": zyIpv6sgPolicyValidateAddressState,
       "zyIpv6sgPolicyValidatePrefixState": zyIpv6sgPolicyValidatePrefixState,
       "zyIpv6sgPolicyPermitLinkLocalState": zyIpv6sgPolicyPermitLinkLocalState,
       "zyIpv6sgPolicyRowStatus": zyIpv6sgPolicyRowStatus,
       "zyxelIpv6sgPolicyPortTable": zyxelIpv6sgPolicyPortTable,
       "zyxelIpv6sgPolicyPortEntry": zyxelIpv6sgPolicyPortEntry,
       "zyIpv6sgPolicyPortAttachPolicy": zyIpv6sgPolicyPortAttachPolicy,
       "zyxelIpv6sgStatus": zyxelIpv6sgStatus,
       "zyIpv6sgBindingClearAll": zyIpv6sgBindingClearAll,
       "zyxelIpv6sgBindingTable": zyxelIpv6sgBindingTable,
       "zyxelIpv6sgBindingEntry": zyxelIpv6sgBindingEntry,
       "zyIpv6sgBindingIpv6AddressType": zyIpv6sgBindingIpv6AddressType,
       "zyIpv6sgBindingIpv6Address": zyIpv6sgBindingIpv6Address,
       "zyIpv6sgBindingIpv6PrefixLength": zyIpv6sgBindingIpv6PrefixLength,
       "zyIpv6sgBindingMacAddress": zyIpv6sgBindingMacAddress,
       "zyIpv6sgBindingVid": zyIpv6sgBindingVid,
       "zyIpv6sgBindingPort": zyIpv6sgBindingPort,
       "zyIpv6sgBindingLeaseTime": zyIpv6sgBindingLeaseTime,
       "zyIpv6sgBindingType": zyIpv6sgBindingType,
       "zyIpv6sgBindingClear": zyIpv6sgBindingClear}
)
