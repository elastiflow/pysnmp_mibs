# SNMP MIB module (ZYXEL-IPV6-SNOOPING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/zyxel_890/ZYXEL-IPV6-SNOOPING-MIB.mib
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

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")

(esMgmt,) = mibBuilder.importSymbols(
    "ZYXEL-ES-SMI",
    "esMgmt")


# MODULE-IDENTITY

zyxelIpv6Snooping = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 109)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelIpv6SnoopingSetup_ObjectIdentity = ObjectIdentity
zyxelIpv6SnoopingSetup = _ZyxelIpv6SnoopingSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 109, 1)
)
_ZyIpv6SnoopingPolicyMaxNumberOfPolicies_Type = Integer32
_ZyIpv6SnoopingPolicyMaxNumberOfPolicies_Object = MibScalar
zyIpv6SnoopingPolicyMaxNumberOfPolicies = _ZyIpv6SnoopingPolicyMaxNumberOfPolicies_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 109, 1, 1),
    _ZyIpv6SnoopingPolicyMaxNumberOfPolicies_Type()
)
zyIpv6SnoopingPolicyMaxNumberOfPolicies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyIpv6SnoopingPolicyMaxNumberOfPolicies.setStatus("current")
_ZyxelIpv6SnoopingPolicyTable_Object = MibTable
zyxelIpv6SnoopingPolicyTable = _ZyxelIpv6SnoopingPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 109, 1, 2)
)
if mibBuilder.loadTexts:
    zyxelIpv6SnoopingPolicyTable.setStatus("current")
_ZyxelIpv6SnoopingPolicyEntry_Object = MibTableRow
zyxelIpv6SnoopingPolicyEntry = _ZyxelIpv6SnoopingPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 109, 1, 2, 1)
)
zyxelIpv6SnoopingPolicyEntry.setIndexNames(
    (0, "ZYXEL-IPV6-SNOOPING-MIB", "zyIpv6SnoopingPolicyName"),
)
if mibBuilder.loadTexts:
    zyxelIpv6SnoopingPolicyEntry.setStatus("current")
_ZyIpv6SnoopingPolicyName_Type = DisplayString
_ZyIpv6SnoopingPolicyName_Object = MibTableColumn
zyIpv6SnoopingPolicyName = _ZyIpv6SnoopingPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 109, 1, 2, 1, 1),
    _ZyIpv6SnoopingPolicyName_Type()
)
zyIpv6SnoopingPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyIpv6SnoopingPolicyName.setStatus("current")


class _ZyIpv6SnoopingPolicyProtocol_Type(Bits):
    """Custom type zyIpv6SnoopingPolicyProtocol based on Bits"""
    namedValues = NamedValues(
        ("dhcp", 0)
    )

_ZyIpv6SnoopingPolicyProtocol_Type.__name__ = "Bits"
_ZyIpv6SnoopingPolicyProtocol_Object = MibTableColumn
zyIpv6SnoopingPolicyProtocol = _ZyIpv6SnoopingPolicyProtocol_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 109, 1, 2, 1, 2),
    _ZyIpv6SnoopingPolicyProtocol_Type()
)
zyIpv6SnoopingPolicyProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyIpv6SnoopingPolicyProtocol.setStatus("current")
_ZyIpv6SnoopingPolicyPrefixGleanState_Type = EnabledStatus
_ZyIpv6SnoopingPolicyPrefixGleanState_Object = MibTableColumn
zyIpv6SnoopingPolicyPrefixGleanState = _ZyIpv6SnoopingPolicyPrefixGleanState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 109, 1, 2, 1, 3),
    _ZyIpv6SnoopingPolicyPrefixGleanState_Type()
)
zyIpv6SnoopingPolicyPrefixGleanState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyIpv6SnoopingPolicyPrefixGleanState.setStatus("current")
_ZyIpv6SnoopingPolicyLimitAddressCount_Type = Integer32
_ZyIpv6SnoopingPolicyLimitAddressCount_Object = MibTableColumn
zyIpv6SnoopingPolicyLimitAddressCount = _ZyIpv6SnoopingPolicyLimitAddressCount_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 109, 1, 2, 1, 4),
    _ZyIpv6SnoopingPolicyLimitAddressCount_Type()
)
zyIpv6SnoopingPolicyLimitAddressCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyIpv6SnoopingPolicyLimitAddressCount.setStatus("current")
_ZyIpv6SnoopingPolicyRowStatus_Type = RowStatus
_ZyIpv6SnoopingPolicyRowStatus_Object = MibTableColumn
zyIpv6SnoopingPolicyRowStatus = _ZyIpv6SnoopingPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 109, 1, 2, 1, 100),
    _ZyIpv6SnoopingPolicyRowStatus_Type()
)
zyIpv6SnoopingPolicyRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyIpv6SnoopingPolicyRowStatus.setStatus("current")
_ZyxelIpv6SnoopingPolicyIfTable_Object = MibTable
zyxelIpv6SnoopingPolicyIfTable = _ZyxelIpv6SnoopingPolicyIfTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 109, 1, 3)
)
if mibBuilder.loadTexts:
    zyxelIpv6SnoopingPolicyIfTable.setStatus("current")
_ZyxelIpv6SnoopingPolicyIfEntry_Object = MibTableRow
zyxelIpv6SnoopingPolicyIfEntry = _ZyxelIpv6SnoopingPolicyIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 109, 1, 3, 1)
)
zyxelIpv6SnoopingPolicyIfEntry.setIndexNames(
    (0, "ZYXEL-IPV6-SNOOPING-MIB", "zyIpv6SnoopingPolicyIfIndex"),
)
if mibBuilder.loadTexts:
    zyxelIpv6SnoopingPolicyIfEntry.setStatus("current")
_ZyIpv6SnoopingPolicyIfIndex_Type = Integer32
_ZyIpv6SnoopingPolicyIfIndex_Object = MibTableColumn
zyIpv6SnoopingPolicyIfIndex = _ZyIpv6SnoopingPolicyIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 109, 1, 3, 1, 1),
    _ZyIpv6SnoopingPolicyIfIndex_Type()
)
zyIpv6SnoopingPolicyIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyIpv6SnoopingPolicyIfIndex.setStatus("current")
_ZyIpv6SnoopingPolicyIfAttachPolicy_Type = DisplayString
_ZyIpv6SnoopingPolicyIfAttachPolicy_Object = MibTableColumn
zyIpv6SnoopingPolicyIfAttachPolicy = _ZyIpv6SnoopingPolicyIfAttachPolicy_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 109, 1, 3, 1, 2),
    _ZyIpv6SnoopingPolicyIfAttachPolicy_Type()
)
zyIpv6SnoopingPolicyIfAttachPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyIpv6SnoopingPolicyIfAttachPolicy.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-IPV6-SNOOPING-MIB",
    **{"zyxelIpv6Snooping": zyxelIpv6Snooping,
       "zyxelIpv6SnoopingSetup": zyxelIpv6SnoopingSetup,
       "zyIpv6SnoopingPolicyMaxNumberOfPolicies": zyIpv6SnoopingPolicyMaxNumberOfPolicies,
       "zyxelIpv6SnoopingPolicyTable": zyxelIpv6SnoopingPolicyTable,
       "zyxelIpv6SnoopingPolicyEntry": zyxelIpv6SnoopingPolicyEntry,
       "zyIpv6SnoopingPolicyName": zyIpv6SnoopingPolicyName,
       "zyIpv6SnoopingPolicyProtocol": zyIpv6SnoopingPolicyProtocol,
       "zyIpv6SnoopingPolicyPrefixGleanState": zyIpv6SnoopingPolicyPrefixGleanState,
       "zyIpv6SnoopingPolicyLimitAddressCount": zyIpv6SnoopingPolicyLimitAddressCount,
       "zyIpv6SnoopingPolicyRowStatus": zyIpv6SnoopingPolicyRowStatus,
       "zyxelIpv6SnoopingPolicyIfTable": zyxelIpv6SnoopingPolicyIfTable,
       "zyxelIpv6SnoopingPolicyIfEntry": zyxelIpv6SnoopingPolicyIfEntry,
       "zyIpv6SnoopingPolicyIfIndex": zyIpv6SnoopingPolicyIfIndex,
       "zyIpv6SnoopingPolicyIfAttachPolicy": zyIpv6SnoopingPolicyIfAttachPolicy}
)
