# SNMP MIB module (CISCO-LWAPP-IPV6-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-LWAPP-IPV6-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:55:05 2025
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

(cldcClientMacAddress,) = mibBuilder.importSymbols(
    "CISCO-LWAPP-DOT11-CLIENT-MIB",
    "cldcClientMacAddress")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoLwappIpv6MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 847)
)
if mibBuilder.loadTexts:
    ciscoLwappIpv6MIB.setRevisions(
        ("2017-05-23 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoLwappIpv6MIBNotifs_ObjectIdentity = ObjectIdentity
ciscoLwappIpv6MIBNotifs = _CiscoLwappIpv6MIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 0)
)
_CiscoLwappIpv6MIBObjects_ObjectIdentity = ObjectIdentity
ciscoLwappIpv6MIBObjects = _CiscoLwappIpv6MIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 1)
)
_CiscoLwappIpv6Config_ObjectIdentity = ObjectIdentity
ciscoLwappIpv6Config = _CiscoLwappIpv6Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 1, 1)
)
_CLIpv6AclTable_Object = MibTable
cLIpv6AclTable = _CLIpv6AclTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cLIpv6AclTable.setStatus("current")
_CLIpv6AclEntry_Object = MibTableRow
cLIpv6AclEntry = _CLIpv6AclEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 1, 1, 1, 1)
)
cLIpv6AclEntry.setIndexNames(
    (0, "CISCO-LWAPP-IPV6-MIB", "cLIpv6AclName"),
)
if mibBuilder.loadTexts:
    cLIpv6AclEntry.setStatus("current")


class _CLIpv6AclName_Type(SnmpAdminString):
    """Custom type cLIpv6AclName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CLIpv6AclName_Type.__name__ = "SnmpAdminString"
_CLIpv6AclName_Object = MibTableColumn
cLIpv6AclName = _CLIpv6AclName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 1, 1, 1, 1, 1),
    _CLIpv6AclName_Type()
)
cLIpv6AclName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLIpv6AclName.setStatus("current")


class _CLIpv6AclApplyMode_Type(Integer32):
    """Custom type cLIpv6AclApplyMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notapplied", 0),
          ("applied", 1))
    )


_CLIpv6AclApplyMode_Type.__name__ = "Integer32"
_CLIpv6AclApplyMode_Object = MibTableColumn
cLIpv6AclApplyMode = _CLIpv6AclApplyMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 1, 1, 1, 1, 2),
    _CLIpv6AclApplyMode_Type()
)
cLIpv6AclApplyMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLIpv6AclApplyMode.setStatus("current")


class _CLIpv6AclCounterClear_Type(TruthValue):
    """Custom type cLIpv6AclCounterClear based on TruthValue"""
    defaultValue = 2


_CLIpv6AclCounterClear_Type.__name__ = "TruthValue"
_CLIpv6AclCounterClear_Object = MibTableColumn
cLIpv6AclCounterClear = _CLIpv6AclCounterClear_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 1, 1, 1, 1, 3),
    _CLIpv6AclCounterClear_Type()
)
cLIpv6AclCounterClear.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLIpv6AclCounterClear.setStatus("current")
_CLIpv6AclRowStatus_Type = RowStatus
_CLIpv6AclRowStatus_Object = MibTableColumn
cLIpv6AclRowStatus = _CLIpv6AclRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 1, 1, 1, 1, 4),
    _CLIpv6AclRowStatus_Type()
)
cLIpv6AclRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLIpv6AclRowStatus.setStatus("current")
_CLIpv6AclRuleTable_Object = MibTable
cLIpv6AclRuleTable = _CLIpv6AclRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cLIpv6AclRuleTable.setStatus("current")
_CLIpv6AclRuleEntry_Object = MibTableRow
cLIpv6AclRuleEntry = _CLIpv6AclRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 1, 1, 2, 1)
)
cLIpv6AclRuleEntry.setIndexNames(
    (0, "CISCO-LWAPP-IPV6-MIB", "cLIpv6AclName"),
    (0, "CISCO-LWAPP-IPV6-MIB", "cLIpv6AclRuleIndex"),
)
if mibBuilder.loadTexts:
    cLIpv6AclRuleEntry.setStatus("current")


class _CLIpv6AclRuleIndex_Type(Unsigned32):
    """Custom type cLIpv6AclRuleIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_CLIpv6AclRuleIndex_Type.__name__ = "Unsigned32"
_CLIpv6AclRuleIndex_Object = MibTableColumn
cLIpv6AclRuleIndex = _CLIpv6AclRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 1, 1, 2, 1, 1),
    _CLIpv6AclRuleIndex_Type()
)
cLIpv6AclRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLIpv6AclRuleIndex.setStatus("current")


class _CLIpv6AclRuleAction_Type(Integer32):
    """Custom type cLIpv6AclRuleAction based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("deny", 0),
          ("permit", 1))
    )


_CLIpv6AclRuleAction_Type.__name__ = "Integer32"
_CLIpv6AclRuleAction_Object = MibTableColumn
cLIpv6AclRuleAction = _CLIpv6AclRuleAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 1, 1, 2, 1, 2),
    _CLIpv6AclRuleAction_Type()
)
cLIpv6AclRuleAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLIpv6AclRuleAction.setStatus("current")


class _CLIpv6AclRuleDirection_Type(Integer32):
    """Custom type cLIpv6AclRuleDirection based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 0),
          ("outbound", 1),
          ("any", 2))
    )


_CLIpv6AclRuleDirection_Type.__name__ = "Integer32"
_CLIpv6AclRuleDirection_Object = MibTableColumn
cLIpv6AclRuleDirection = _CLIpv6AclRuleDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 1, 1, 2, 1, 3),
    _CLIpv6AclRuleDirection_Type()
)
cLIpv6AclRuleDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLIpv6AclRuleDirection.setStatus("current")
_CLIpv6AclRuleSourceInetAddressType_Type = InetAddressType
_CLIpv6AclRuleSourceInetAddressType_Object = MibTableColumn
cLIpv6AclRuleSourceInetAddressType = _CLIpv6AclRuleSourceInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 1, 1, 2, 1, 4),
    _CLIpv6AclRuleSourceInetAddressType_Type()
)
cLIpv6AclRuleSourceInetAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLIpv6AclRuleSourceInetAddressType.setStatus("current")
_CLIpv6AclRuleSourceInetAddress_Type = InetAddress
_CLIpv6AclRuleSourceInetAddress_Object = MibTableColumn
cLIpv6AclRuleSourceInetAddress = _CLIpv6AclRuleSourceInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 1, 1, 2, 1, 5),
    _CLIpv6AclRuleSourceInetAddress_Type()
)
cLIpv6AclRuleSourceInetAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLIpv6AclRuleSourceInetAddress.setStatus("current")


class _CLIpv6AclRuleSourcePrefixLength_Type(Unsigned32):
    """Custom type cLIpv6AclRuleSourcePrefixLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_CLIpv6AclRuleSourcePrefixLength_Type.__name__ = "Unsigned32"
_CLIpv6AclRuleSourcePrefixLength_Object = MibTableColumn
cLIpv6AclRuleSourcePrefixLength = _CLIpv6AclRuleSourcePrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 1, 1, 2, 1, 6),
    _CLIpv6AclRuleSourcePrefixLength_Type()
)
cLIpv6AclRuleSourcePrefixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLIpv6AclRuleSourcePrefixLength.setStatus("current")
_CLIpv6AclRuleDestinationInetAddressType_Type = InetAddressType
_CLIpv6AclRuleDestinationInetAddressType_Object = MibTableColumn
cLIpv6AclRuleDestinationInetAddressType = _CLIpv6AclRuleDestinationInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 1, 1, 2, 1, 7),
    _CLIpv6AclRuleDestinationInetAddressType_Type()
)
cLIpv6AclRuleDestinationInetAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLIpv6AclRuleDestinationInetAddressType.setStatus("current")
_CLIpv6AclRuleDestinationInetAddress_Type = InetAddress
_CLIpv6AclRuleDestinationInetAddress_Object = MibTableColumn
cLIpv6AclRuleDestinationInetAddress = _CLIpv6AclRuleDestinationInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 1, 1, 2, 1, 8),
    _CLIpv6AclRuleDestinationInetAddress_Type()
)
cLIpv6AclRuleDestinationInetAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLIpv6AclRuleDestinationInetAddress.setStatus("current")


class _CLIpv6AclRuleDestinationPrefixLength_Type(Unsigned32):
    """Custom type cLIpv6AclRuleDestinationPrefixLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_CLIpv6AclRuleDestinationPrefixLength_Type.__name__ = "Unsigned32"
_CLIpv6AclRuleDestinationPrefixLength_Object = MibTableColumn
cLIpv6AclRuleDestinationPrefixLength = _CLIpv6AclRuleDestinationPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 1, 1, 2, 1, 9),
    _CLIpv6AclRuleDestinationPrefixLength_Type()
)
cLIpv6AclRuleDestinationPrefixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLIpv6AclRuleDestinationPrefixLength.setStatus("current")


class _CLIpv6AclRuleProtocol_Type(Unsigned32):
    """Custom type cLIpv6AclRuleProtocol based on Unsigned32"""
    defaultValue = 256

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_CLIpv6AclRuleProtocol_Type.__name__ = "Unsigned32"
_CLIpv6AclRuleProtocol_Object = MibTableColumn
cLIpv6AclRuleProtocol = _CLIpv6AclRuleProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 1, 1, 2, 1, 10),
    _CLIpv6AclRuleProtocol_Type()
)
cLIpv6AclRuleProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLIpv6AclRuleProtocol.setStatus("current")


class _CLIpv6AclRuleStartSourcePort_Type(InetPortNumber):
    """Custom type cLIpv6AclRuleStartSourcePort based on InetPortNumber"""
    defaultValue = 0


_CLIpv6AclRuleStartSourcePort_Type.__name__ = "InetPortNumber"
_CLIpv6AclRuleStartSourcePort_Object = MibTableColumn
cLIpv6AclRuleStartSourcePort = _CLIpv6AclRuleStartSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 1, 1, 2, 1, 11),
    _CLIpv6AclRuleStartSourcePort_Type()
)
cLIpv6AclRuleStartSourcePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLIpv6AclRuleStartSourcePort.setStatus("current")


class _CLIpv6AclRuleEndSourcePort_Type(InetPortNumber):
    """Custom type cLIpv6AclRuleEndSourcePort based on InetPortNumber"""
    defaultValue = 65535


_CLIpv6AclRuleEndSourcePort_Type.__name__ = "InetPortNumber"
_CLIpv6AclRuleEndSourcePort_Object = MibTableColumn
cLIpv6AclRuleEndSourcePort = _CLIpv6AclRuleEndSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 1, 1, 2, 1, 12),
    _CLIpv6AclRuleEndSourcePort_Type()
)
cLIpv6AclRuleEndSourcePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLIpv6AclRuleEndSourcePort.setStatus("current")


class _CLIpv6AclRuleStartDestinationPort_Type(InetPortNumber):
    """Custom type cLIpv6AclRuleStartDestinationPort based on InetPortNumber"""
    defaultValue = 0


_CLIpv6AclRuleStartDestinationPort_Type.__name__ = "InetPortNumber"
_CLIpv6AclRuleStartDestinationPort_Object = MibTableColumn
cLIpv6AclRuleStartDestinationPort = _CLIpv6AclRuleStartDestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 1, 1, 2, 1, 13),
    _CLIpv6AclRuleStartDestinationPort_Type()
)
cLIpv6AclRuleStartDestinationPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLIpv6AclRuleStartDestinationPort.setStatus("current")


class _CLIpv6AclRuleEndDestinationPort_Type(InetPortNumber):
    """Custom type cLIpv6AclRuleEndDestinationPort based on InetPortNumber"""
    defaultValue = 65535


_CLIpv6AclRuleEndDestinationPort_Type.__name__ = "InetPortNumber"
_CLIpv6AclRuleEndDestinationPort_Object = MibTableColumn
cLIpv6AclRuleEndDestinationPort = _CLIpv6AclRuleEndDestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 1, 1, 2, 1, 14),
    _CLIpv6AclRuleEndDestinationPort_Type()
)
cLIpv6AclRuleEndDestinationPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLIpv6AclRuleEndDestinationPort.setStatus("current")


class _CLIpv6AclRuleDscp_Type(Unsigned32):
    """Custom type cLIpv6AclRuleDscp based on Unsigned32"""
    defaultValue = 256

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_CLIpv6AclRuleDscp_Type.__name__ = "Unsigned32"
_CLIpv6AclRuleDscp_Object = MibTableColumn
cLIpv6AclRuleDscp = _CLIpv6AclRuleDscp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 1, 1, 2, 1, 15),
    _CLIpv6AclRuleDscp_Type()
)
cLIpv6AclRuleDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLIpv6AclRuleDscp.setStatus("current")


class _CLIpv6AclNewRuleIndex_Type(Unsigned32):
    """Custom type cLIpv6AclNewRuleIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_CLIpv6AclNewRuleIndex_Type.__name__ = "Unsigned32"
_CLIpv6AclNewRuleIndex_Object = MibTableColumn
cLIpv6AclNewRuleIndex = _CLIpv6AclNewRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 1, 1, 2, 1, 16),
    _CLIpv6AclNewRuleIndex_Type()
)
cLIpv6AclNewRuleIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLIpv6AclNewRuleIndex.setStatus("current")
_CLIpv6AclRuleHits_Type = Counter32
_CLIpv6AclRuleHits_Object = MibTableColumn
cLIpv6AclRuleHits = _CLIpv6AclRuleHits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 1, 1, 2, 1, 17),
    _CLIpv6AclRuleHits_Type()
)
cLIpv6AclRuleHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLIpv6AclRuleHits.setStatus("current")
_CLIpv6AclRuleRowStatus_Type = RowStatus
_CLIpv6AclRuleRowStatus_Object = MibTableColumn
cLIpv6AclRuleRowStatus = _CLIpv6AclRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 1, 1, 2, 1, 18),
    _CLIpv6AclRuleRowStatus_Type()
)
cLIpv6AclRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLIpv6AclRuleRowStatus.setStatus("current")
_CiscoLwappIpv6RaFiltering_ObjectIdentity = ObjectIdentity
ciscoLwappIpv6RaFiltering = _CiscoLwappIpv6RaFiltering_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 1, 1, 3)
)


class _CLIpv6RaFilteringEnabled_Type(TruthValue):
    """Custom type cLIpv6RaFilteringEnabled based on TruthValue"""
    defaultValue = 2


_CLIpv6RaFilteringEnabled_Type.__name__ = "TruthValue"
_CLIpv6RaFilteringEnabled_Object = MibScalar
cLIpv6RaFilteringEnabled = _CLIpv6RaFilteringEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 1, 1, 3, 1),
    _CLIpv6RaFilteringEnabled_Type()
)
cLIpv6RaFilteringEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLIpv6RaFilteringEnabled.setStatus("current")


class _CLIpv6RaFilteringOnApEnabled_Type(TruthValue):
    """Custom type cLIpv6RaFilteringOnApEnabled based on TruthValue"""
    defaultValue = 2


_CLIpv6RaFilteringOnApEnabled_Type.__name__ = "TruthValue"
_CLIpv6RaFilteringOnApEnabled_Object = MibScalar
cLIpv6RaFilteringOnApEnabled = _CLIpv6RaFilteringOnApEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 1, 1, 3, 2),
    _CLIpv6RaFilteringOnApEnabled_Type()
)
cLIpv6RaFilteringOnApEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLIpv6RaFilteringOnApEnabled.setStatus("current")
_CLIpv6RaFilteringClientInfoTable_Object = MibTable
cLIpv6RaFilteringClientInfoTable = _CLIpv6RaFilteringClientInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 1, 1, 3, 3)
)
if mibBuilder.loadTexts:
    cLIpv6RaFilteringClientInfoTable.setStatus("current")
_CLIpv6RaFilteringClientInfoEntry_Object = MibTableRow
cLIpv6RaFilteringClientInfoEntry = _CLIpv6RaFilteringClientInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 1, 1, 3, 3, 1)
)
cLIpv6RaFilteringClientInfoEntry.setIndexNames(
    (0, "CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"),
)
if mibBuilder.loadTexts:
    cLIpv6RaFilteringClientInfoEntry.setStatus("current")


class _CLIpv6RaFilteringClientInfoApName_Type(SnmpAdminString):
    """Custom type cLIpv6RaFilteringClientInfoApName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CLIpv6RaFilteringClientInfoApName_Type.__name__ = "SnmpAdminString"
_CLIpv6RaFilteringClientInfoApName_Object = MibTableColumn
cLIpv6RaFilteringClientInfoApName = _CLIpv6RaFilteringClientInfoApName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 1, 1, 3, 3, 1, 1),
    _CLIpv6RaFilteringClientInfoApName_Type()
)
cLIpv6RaFilteringClientInfoApName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLIpv6RaFilteringClientInfoApName.setStatus("current")
_CLIpv6RaFilteringClientInfoWlan_Type = Unsigned32
_CLIpv6RaFilteringClientInfoWlan_Object = MibTableColumn
cLIpv6RaFilteringClientInfoWlan = _CLIpv6RaFilteringClientInfoWlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 1, 1, 3, 3, 1, 2),
    _CLIpv6RaFilteringClientInfoWlan_Type()
)
cLIpv6RaFilteringClientInfoWlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLIpv6RaFilteringClientInfoWlan.setStatus("current")
_CLIpv6RaFilteringClientInfoPktsDropped_Type = Counter32
_CLIpv6RaFilteringClientInfoPktsDropped_Object = MibTableColumn
cLIpv6RaFilteringClientInfoPktsDropped = _CLIpv6RaFilteringClientInfoPktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 1, 1, 3, 3, 1, 3),
    _CLIpv6RaFilteringClientInfoPktsDropped_Type()
)
cLIpv6RaFilteringClientInfoPktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLIpv6RaFilteringClientInfoPktsDropped.setStatus("current")
_CiscoLwappIpv6NbRaThrottleConfig_ObjectIdentity = ObjectIdentity
ciscoLwappIpv6NbRaThrottleConfig = _CiscoLwappIpv6NbRaThrottleConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 1, 1, 4)
)


class _CLIpv6NbRaThrottleEnabled_Type(TruthValue):
    """Custom type cLIpv6NbRaThrottleEnabled based on TruthValue"""
    defaultValue = 2


_CLIpv6NbRaThrottleEnabled_Type.__name__ = "TruthValue"
_CLIpv6NbRaThrottleEnabled_Object = MibScalar
cLIpv6NbRaThrottleEnabled = _CLIpv6NbRaThrottleEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 1, 1, 4, 1),
    _CLIpv6NbRaThrottleEnabled_Type()
)
cLIpv6NbRaThrottleEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLIpv6NbRaThrottleEnabled.setStatus("current")


class _CLIpv6NbRaThrottlePeriod_Type(Unsigned32):
    """Custom type cLIpv6NbRaThrottlePeriod based on Unsigned32"""
    defaultValue = 600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 86400),
    )


_CLIpv6NbRaThrottlePeriod_Type.__name__ = "Unsigned32"
_CLIpv6NbRaThrottlePeriod_Object = MibScalar
cLIpv6NbRaThrottlePeriod = _CLIpv6NbRaThrottlePeriod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 1, 1, 4, 2),
    _CLIpv6NbRaThrottlePeriod_Type()
)
cLIpv6NbRaThrottlePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLIpv6NbRaThrottlePeriod.setStatus("current")
if mibBuilder.loadTexts:
    cLIpv6NbRaThrottlePeriod.setUnits("Seconds")


class _CLIpv6NbRaThrottleMaxThrough_Type(Unsigned32):
    """Custom type cLIpv6NbRaThrottleMaxThrough based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_CLIpv6NbRaThrottleMaxThrough_Type.__name__ = "Unsigned32"
_CLIpv6NbRaThrottleMaxThrough_Object = MibScalar
cLIpv6NbRaThrottleMaxThrough = _CLIpv6NbRaThrottleMaxThrough_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 1, 1, 4, 3),
    _CLIpv6NbRaThrottleMaxThrough_Type()
)
cLIpv6NbRaThrottleMaxThrough.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLIpv6NbRaThrottleMaxThrough.setStatus("current")


class _CLIpv6NbRaThrottleMaxThroughNoLimitEnabled_Type(TruthValue):
    """Custom type cLIpv6NbRaThrottleMaxThroughNoLimitEnabled based on TruthValue"""
    defaultValue = 2


_CLIpv6NbRaThrottleMaxThroughNoLimitEnabled_Type.__name__ = "TruthValue"
_CLIpv6NbRaThrottleMaxThroughNoLimitEnabled_Object = MibScalar
cLIpv6NbRaThrottleMaxThroughNoLimitEnabled = _CLIpv6NbRaThrottleMaxThroughNoLimitEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 1, 1, 4, 4),
    _CLIpv6NbRaThrottleMaxThroughNoLimitEnabled_Type()
)
cLIpv6NbRaThrottleMaxThroughNoLimitEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLIpv6NbRaThrottleMaxThroughNoLimitEnabled.setStatus("current")


class _CLIpv6NbRaThrottleIntervalOption_Type(Integer32):
    """Custom type cLIpv6NbRaThrottleIntervalOption based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ignore", 1),
          ("passthrough", 2),
          ("throttle", 3))
    )


_CLIpv6NbRaThrottleIntervalOption_Type.__name__ = "Integer32"
_CLIpv6NbRaThrottleIntervalOption_Object = MibScalar
cLIpv6NbRaThrottleIntervalOption = _CLIpv6NbRaThrottleIntervalOption_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 1, 1, 4, 5),
    _CLIpv6NbRaThrottleIntervalOption_Type()
)
cLIpv6NbRaThrottleIntervalOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLIpv6NbRaThrottleIntervalOption.setStatus("current")


class _CLIpv6NbRaThrottleAllowAtleast_Type(Unsigned32):
    """Custom type cLIpv6NbRaThrottleAllowAtleast based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_CLIpv6NbRaThrottleAllowAtleast_Type.__name__ = "Unsigned32"
_CLIpv6NbRaThrottleAllowAtleast_Object = MibScalar
cLIpv6NbRaThrottleAllowAtleast = _CLIpv6NbRaThrottleAllowAtleast_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 1, 1, 4, 6),
    _CLIpv6NbRaThrottleAllowAtleast_Type()
)
cLIpv6NbRaThrottleAllowAtleast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLIpv6NbRaThrottleAllowAtleast.setStatus("current")


class _CLIpv6NbRaThrottleAllowAtmost_Type(Unsigned32):
    """Custom type cLIpv6NbRaThrottleAllowAtmost based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_CLIpv6NbRaThrottleAllowAtmost_Type.__name__ = "Unsigned32"
_CLIpv6NbRaThrottleAllowAtmost_Object = MibScalar
cLIpv6NbRaThrottleAllowAtmost = _CLIpv6NbRaThrottleAllowAtmost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 1, 1, 4, 7),
    _CLIpv6NbRaThrottleAllowAtmost_Type()
)
cLIpv6NbRaThrottleAllowAtmost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLIpv6NbRaThrottleAllowAtmost.setStatus("current")


class _CLIpv6NbRaThrottleAllowNoLimitEnabled_Type(TruthValue):
    """Custom type cLIpv6NbRaThrottleAllowNoLimitEnabled based on TruthValue"""
    defaultValue = 2


_CLIpv6NbRaThrottleAllowNoLimitEnabled_Type.__name__ = "TruthValue"
_CLIpv6NbRaThrottleAllowNoLimitEnabled_Object = MibScalar
cLIpv6NbRaThrottleAllowNoLimitEnabled = _CLIpv6NbRaThrottleAllowNoLimitEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 1, 1, 4, 8),
    _CLIpv6NbRaThrottleAllowNoLimitEnabled_Type()
)
cLIpv6NbRaThrottleAllowNoLimitEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLIpv6NbRaThrottleAllowNoLimitEnabled.setStatus("current")
_CiscoLwappIpv6NbTimerConfig_ObjectIdentity = ObjectIdentity
ciscoLwappIpv6NbTimerConfig = _CiscoLwappIpv6NbTimerConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 1, 1, 5)
)


class _CLIpv6NbTimerDownLifeTimeEnabled_Type(TruthValue):
    """Custom type cLIpv6NbTimerDownLifeTimeEnabled based on TruthValue"""
    defaultValue = 2


_CLIpv6NbTimerDownLifeTimeEnabled_Type.__name__ = "TruthValue"
_CLIpv6NbTimerDownLifeTimeEnabled_Object = MibScalar
cLIpv6NbTimerDownLifeTimeEnabled = _CLIpv6NbTimerDownLifeTimeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 1, 1, 5, 1),
    _CLIpv6NbTimerDownLifeTimeEnabled_Type()
)
cLIpv6NbTimerDownLifeTimeEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLIpv6NbTimerDownLifeTimeEnabled.setStatus("current")


class _CLIpv6NbTimerDownLifeTimeInterval_Type(Unsigned32):
    """Custom type cLIpv6NbTimerDownLifeTimeInterval based on Unsigned32"""
    defaultValue = 86400

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_CLIpv6NbTimerDownLifeTimeInterval_Type.__name__ = "Unsigned32"
_CLIpv6NbTimerDownLifeTimeInterval_Object = MibScalar
cLIpv6NbTimerDownLifeTimeInterval = _CLIpv6NbTimerDownLifeTimeInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 1, 1, 5, 2),
    _CLIpv6NbTimerDownLifeTimeInterval_Type()
)
cLIpv6NbTimerDownLifeTimeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLIpv6NbTimerDownLifeTimeInterval.setStatus("current")
if mibBuilder.loadTexts:
    cLIpv6NbTimerDownLifeTimeInterval.setUnits("Seconds")


class _CLIpv6NbTimerStaleLifeTimeEnabled_Type(TruthValue):
    """Custom type cLIpv6NbTimerStaleLifeTimeEnabled based on TruthValue"""
    defaultValue = 2


_CLIpv6NbTimerStaleLifeTimeEnabled_Type.__name__ = "TruthValue"
_CLIpv6NbTimerStaleLifeTimeEnabled_Object = MibScalar
cLIpv6NbTimerStaleLifeTimeEnabled = _CLIpv6NbTimerStaleLifeTimeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 1, 1, 5, 3),
    _CLIpv6NbTimerStaleLifeTimeEnabled_Type()
)
cLIpv6NbTimerStaleLifeTimeEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLIpv6NbTimerStaleLifeTimeEnabled.setStatus("current")


class _CLIpv6NbTimerStaleLifeTimeInterval_Type(Unsigned32):
    """Custom type cLIpv6NbTimerStaleLifeTimeInterval based on Unsigned32"""
    defaultValue = 86400

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_CLIpv6NbTimerStaleLifeTimeInterval_Type.__name__ = "Unsigned32"
_CLIpv6NbTimerStaleLifeTimeInterval_Object = MibScalar
cLIpv6NbTimerStaleLifeTimeInterval = _CLIpv6NbTimerStaleLifeTimeInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 1, 1, 5, 4),
    _CLIpv6NbTimerStaleLifeTimeInterval_Type()
)
cLIpv6NbTimerStaleLifeTimeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLIpv6NbTimerStaleLifeTimeInterval.setStatus("current")
if mibBuilder.loadTexts:
    cLIpv6NbTimerStaleLifeTimeInterval.setUnits("Seconds")


class _CLIpv6NbTimerReachableLifeTimeEnabled_Type(TruthValue):
    """Custom type cLIpv6NbTimerReachableLifeTimeEnabled based on TruthValue"""
    defaultValue = 2


_CLIpv6NbTimerReachableLifeTimeEnabled_Type.__name__ = "TruthValue"
_CLIpv6NbTimerReachableLifeTimeEnabled_Object = MibScalar
cLIpv6NbTimerReachableLifeTimeEnabled = _CLIpv6NbTimerReachableLifeTimeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 1, 1, 5, 5),
    _CLIpv6NbTimerReachableLifeTimeEnabled_Type()
)
cLIpv6NbTimerReachableLifeTimeEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLIpv6NbTimerReachableLifeTimeEnabled.setStatus("current")


class _CLIpv6NbTimerReachableLifeTimeInterval_Type(Unsigned32):
    """Custom type cLIpv6NbTimerReachableLifeTimeInterval based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_CLIpv6NbTimerReachableLifeTimeInterval_Type.__name__ = "Unsigned32"
_CLIpv6NbTimerReachableLifeTimeInterval_Object = MibScalar
cLIpv6NbTimerReachableLifeTimeInterval = _CLIpv6NbTimerReachableLifeTimeInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 1, 1, 5, 6),
    _CLIpv6NbTimerReachableLifeTimeInterval_Type()
)
cLIpv6NbTimerReachableLifeTimeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLIpv6NbTimerReachableLifeTimeInterval.setStatus("current")
if mibBuilder.loadTexts:
    cLIpv6NbTimerReachableLifeTimeInterval.setUnits("Seconds")


class _CLIpv6NbTimerNsMulticastCacheMissForward_Type(TruthValue):
    """Custom type cLIpv6NbTimerNsMulticastCacheMissForward based on TruthValue"""
    defaultValue = 2


_CLIpv6NbTimerNsMulticastCacheMissForward_Type.__name__ = "TruthValue"
_CLIpv6NbTimerNsMulticastCacheMissForward_Object = MibScalar
cLIpv6NbTimerNsMulticastCacheMissForward = _CLIpv6NbTimerNsMulticastCacheMissForward_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 1, 1, 5, 7),
    _CLIpv6NbTimerNsMulticastCacheMissForward_Type()
)
cLIpv6NbTimerNsMulticastCacheMissForward.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLIpv6NbTimerNsMulticastCacheMissForward.setStatus("current")


class _CLIpv6NeighborBindingCounterClear_Type(TruthValue):
    """Custom type cLIpv6NeighborBindingCounterClear based on TruthValue"""
    defaultValue = 2


_CLIpv6NeighborBindingCounterClear_Type.__name__ = "TruthValue"
_CLIpv6NeighborBindingCounterClear_Object = MibScalar
cLIpv6NeighborBindingCounterClear = _CLIpv6NeighborBindingCounterClear_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 1, 1, 6),
    _CLIpv6NeighborBindingCounterClear_Type()
)
cLIpv6NeighborBindingCounterClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLIpv6NeighborBindingCounterClear.setStatus("current")


class _CLIpv6GlobalEnabled_Type(TruthValue):
    """Custom type cLIpv6GlobalEnabled based on TruthValue"""
    defaultValue = 2


_CLIpv6GlobalEnabled_Type.__name__ = "TruthValue"
_CLIpv6GlobalEnabled_Object = MibScalar
cLIpv6GlobalEnabled = _CLIpv6GlobalEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 1, 1, 7),
    _CLIpv6GlobalEnabled_Type()
)
cLIpv6GlobalEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLIpv6GlobalEnabled.setStatus("current")
_CiscoLwappIpv6Stats_ObjectIdentity = ObjectIdentity
ciscoLwappIpv6Stats = _CiscoLwappIpv6Stats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 1, 2)
)
_CLIpv6NeighborBindingCounterTable_Object = MibTable
cLIpv6NeighborBindingCounterTable = _CLIpv6NeighborBindingCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cLIpv6NeighborBindingCounterTable.setStatus("current")
_CLIpv6NeighborBindingCounterEntry_Object = MibTableRow
cLIpv6NeighborBindingCounterEntry = _CLIpv6NeighborBindingCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 1, 2, 1, 1)
)
cLIpv6NeighborBindingCounterEntry.setIndexNames(
    (0, "CISCO-LWAPP-IPV6-MIB", "cLIpv6NeighborBindingCounterType"),
)
if mibBuilder.loadTexts:
    cLIpv6NeighborBindingCounterEntry.setStatus("current")


class _CLIpv6NeighborBindingCounterType_Type(Integer32):
    """Custom type cLIpv6NeighborBindingCounterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("receivedMessages", 1),
          ("bridgedMessages", 2))
    )


_CLIpv6NeighborBindingCounterType_Type.__name__ = "Integer32"
_CLIpv6NeighborBindingCounterType_Object = MibTableColumn
cLIpv6NeighborBindingCounterType = _CLIpv6NeighborBindingCounterType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 1, 2, 1, 1, 1),
    _CLIpv6NeighborBindingCounterType_Type()
)
cLIpv6NeighborBindingCounterType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLIpv6NeighborBindingCounterType.setStatus("current")
_CLIpv6NeighborBindingCounterNdpRs_Type = Counter32
_CLIpv6NeighborBindingCounterNdpRs_Object = MibTableColumn
cLIpv6NeighborBindingCounterNdpRs = _CLIpv6NeighborBindingCounterNdpRs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 1, 2, 1, 1, 2),
    _CLIpv6NeighborBindingCounterNdpRs_Type()
)
cLIpv6NeighborBindingCounterNdpRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLIpv6NeighborBindingCounterNdpRs.setStatus("current")
_CLIpv6NeighborBindingCounterNdpRa_Type = Counter32
_CLIpv6NeighborBindingCounterNdpRa_Object = MibTableColumn
cLIpv6NeighborBindingCounterNdpRa = _CLIpv6NeighborBindingCounterNdpRa_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 1, 2, 1, 1, 3),
    _CLIpv6NeighborBindingCounterNdpRa_Type()
)
cLIpv6NeighborBindingCounterNdpRa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLIpv6NeighborBindingCounterNdpRa.setStatus("current")
_CLIpv6NeighborBindingCounterNdpNs_Type = Counter32
_CLIpv6NeighborBindingCounterNdpNs_Object = MibTableColumn
cLIpv6NeighborBindingCounterNdpNs = _CLIpv6NeighborBindingCounterNdpNs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 1, 2, 1, 1, 4),
    _CLIpv6NeighborBindingCounterNdpNs_Type()
)
cLIpv6NeighborBindingCounterNdpNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLIpv6NeighborBindingCounterNdpNs.setStatus("current")
_CLIpv6NeighborBindingCounterNdpNa_Type = Counter32
_CLIpv6NeighborBindingCounterNdpNa_Object = MibTableColumn
cLIpv6NeighborBindingCounterNdpNa = _CLIpv6NeighborBindingCounterNdpNa_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 1, 2, 1, 1, 5),
    _CLIpv6NeighborBindingCounterNdpNa_Type()
)
cLIpv6NeighborBindingCounterNdpNa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLIpv6NeighborBindingCounterNdpNa.setStatus("current")
_CLIpv6NeighborBindingCounterNdpRedirect_Type = Counter32
_CLIpv6NeighborBindingCounterNdpRedirect_Object = MibTableColumn
cLIpv6NeighborBindingCounterNdpRedirect = _CLIpv6NeighborBindingCounterNdpRedirect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 1, 2, 1, 1, 6),
    _CLIpv6NeighborBindingCounterNdpRedirect_Type()
)
cLIpv6NeighborBindingCounterNdpRedirect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLIpv6NeighborBindingCounterNdpRedirect.setStatus("current")
_CLIpv6NeighborBindingCounterNdpCertSol_Type = Counter32
_CLIpv6NeighborBindingCounterNdpCertSol_Object = MibTableColumn
cLIpv6NeighborBindingCounterNdpCertSol = _CLIpv6NeighborBindingCounterNdpCertSol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 1, 2, 1, 1, 7),
    _CLIpv6NeighborBindingCounterNdpCertSol_Type()
)
cLIpv6NeighborBindingCounterNdpCertSol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLIpv6NeighborBindingCounterNdpCertSol.setStatus("current")
_CLIpv6NeighborBindingCounterNdpCertAdv_Type = Counter32
_CLIpv6NeighborBindingCounterNdpCertAdv_Object = MibTableColumn
cLIpv6NeighborBindingCounterNdpCertAdv = _CLIpv6NeighborBindingCounterNdpCertAdv_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 1, 2, 1, 1, 8),
    _CLIpv6NeighborBindingCounterNdpCertAdv_Type()
)
cLIpv6NeighborBindingCounterNdpCertAdv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLIpv6NeighborBindingCounterNdpCertAdv.setStatus("current")
_CLIpv6NeighborBindingCounterDhcpV6Sol_Type = Counter32
_CLIpv6NeighborBindingCounterDhcpV6Sol_Object = MibTableColumn
cLIpv6NeighborBindingCounterDhcpV6Sol = _CLIpv6NeighborBindingCounterDhcpV6Sol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 1, 2, 1, 1, 9),
    _CLIpv6NeighborBindingCounterDhcpV6Sol_Type()
)
cLIpv6NeighborBindingCounterDhcpV6Sol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLIpv6NeighborBindingCounterDhcpV6Sol.setStatus("current")
_CLIpv6NeighborBindingCounterDhcpV6Adv_Type = Counter32
_CLIpv6NeighborBindingCounterDhcpV6Adv_Object = MibTableColumn
cLIpv6NeighborBindingCounterDhcpV6Adv = _CLIpv6NeighborBindingCounterDhcpV6Adv_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 1, 2, 1, 1, 10),
    _CLIpv6NeighborBindingCounterDhcpV6Adv_Type()
)
cLIpv6NeighborBindingCounterDhcpV6Adv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLIpv6NeighborBindingCounterDhcpV6Adv.setStatus("current")
_CLIpv6NeighborBindingCounterDhcpV6Request_Type = Counter32
_CLIpv6NeighborBindingCounterDhcpV6Request_Object = MibTableColumn
cLIpv6NeighborBindingCounterDhcpV6Request = _CLIpv6NeighborBindingCounterDhcpV6Request_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 1, 2, 1, 1, 11),
    _CLIpv6NeighborBindingCounterDhcpV6Request_Type()
)
cLIpv6NeighborBindingCounterDhcpV6Request.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLIpv6NeighborBindingCounterDhcpV6Request.setStatus("current")
_CLIpv6NeighborBindingCounterDhcpV6Confirm_Type = Counter32
_CLIpv6NeighborBindingCounterDhcpV6Confirm_Object = MibTableColumn
cLIpv6NeighborBindingCounterDhcpV6Confirm = _CLIpv6NeighborBindingCounterDhcpV6Confirm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 1, 2, 1, 1, 12),
    _CLIpv6NeighborBindingCounterDhcpV6Confirm_Type()
)
cLIpv6NeighborBindingCounterDhcpV6Confirm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLIpv6NeighborBindingCounterDhcpV6Confirm.setStatus("current")
_CLIpv6NeighborBindingCounterDhcpV6Renew_Type = Counter32
_CLIpv6NeighborBindingCounterDhcpV6Renew_Object = MibTableColumn
cLIpv6NeighborBindingCounterDhcpV6Renew = _CLIpv6NeighborBindingCounterDhcpV6Renew_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 1, 2, 1, 1, 13),
    _CLIpv6NeighborBindingCounterDhcpV6Renew_Type()
)
cLIpv6NeighborBindingCounterDhcpV6Renew.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLIpv6NeighborBindingCounterDhcpV6Renew.setStatus("current")
_CLIpv6NeighborBindingCounterDhcpV6Rebind_Type = Counter32
_CLIpv6NeighborBindingCounterDhcpV6Rebind_Object = MibTableColumn
cLIpv6NeighborBindingCounterDhcpV6Rebind = _CLIpv6NeighborBindingCounterDhcpV6Rebind_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 1, 2, 1, 1, 14),
    _CLIpv6NeighborBindingCounterDhcpV6Rebind_Type()
)
cLIpv6NeighborBindingCounterDhcpV6Rebind.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLIpv6NeighborBindingCounterDhcpV6Rebind.setStatus("current")
_CLIpv6NeighborBindingCounterDhcpV6Reply_Type = Counter32
_CLIpv6NeighborBindingCounterDhcpV6Reply_Object = MibTableColumn
cLIpv6NeighborBindingCounterDhcpV6Reply = _CLIpv6NeighborBindingCounterDhcpV6Reply_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 1, 2, 1, 1, 15),
    _CLIpv6NeighborBindingCounterDhcpV6Reply_Type()
)
cLIpv6NeighborBindingCounterDhcpV6Reply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLIpv6NeighborBindingCounterDhcpV6Reply.setStatus("current")
_CLIpv6NeighborBindingCounterDhcpV6Release_Type = Counter32
_CLIpv6NeighborBindingCounterDhcpV6Release_Object = MibTableColumn
cLIpv6NeighborBindingCounterDhcpV6Release = _CLIpv6NeighborBindingCounterDhcpV6Release_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 1, 2, 1, 1, 16),
    _CLIpv6NeighborBindingCounterDhcpV6Release_Type()
)
cLIpv6NeighborBindingCounterDhcpV6Release.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLIpv6NeighborBindingCounterDhcpV6Release.setStatus("current")
_CLIpv6NeighborBindingCounterDhcpV6Decline_Type = Counter32
_CLIpv6NeighborBindingCounterDhcpV6Decline_Object = MibTableColumn
cLIpv6NeighborBindingCounterDhcpV6Decline = _CLIpv6NeighborBindingCounterDhcpV6Decline_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 1, 2, 1, 1, 17),
    _CLIpv6NeighborBindingCounterDhcpV6Decline_Type()
)
cLIpv6NeighborBindingCounterDhcpV6Decline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLIpv6NeighborBindingCounterDhcpV6Decline.setStatus("current")
_CLIpv6NeighborBindingCounterDhcpV6Recfg_Type = Counter32
_CLIpv6NeighborBindingCounterDhcpV6Recfg_Object = MibTableColumn
cLIpv6NeighborBindingCounterDhcpV6Recfg = _CLIpv6NeighborBindingCounterDhcpV6Recfg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 1, 2, 1, 1, 18),
    _CLIpv6NeighborBindingCounterDhcpV6Recfg_Type()
)
cLIpv6NeighborBindingCounterDhcpV6Recfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLIpv6NeighborBindingCounterDhcpV6Recfg.setStatus("current")
_CLIpv6NeighborBindingCounterDhcpV6InfoReq_Type = Counter32
_CLIpv6NeighborBindingCounterDhcpV6InfoReq_Object = MibTableColumn
cLIpv6NeighborBindingCounterDhcpV6InfoReq = _CLIpv6NeighborBindingCounterDhcpV6InfoReq_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 1, 2, 1, 1, 19),
    _CLIpv6NeighborBindingCounterDhcpV6InfoReq_Type()
)
cLIpv6NeighborBindingCounterDhcpV6InfoReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLIpv6NeighborBindingCounterDhcpV6InfoReq.setStatus("current")
_CLIpv6NeighborBindingCounterDhcpV6RelayForward_Type = Counter32
_CLIpv6NeighborBindingCounterDhcpV6RelayForward_Object = MibTableColumn
cLIpv6NeighborBindingCounterDhcpV6RelayForward = _CLIpv6NeighborBindingCounterDhcpV6RelayForward_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 1, 2, 1, 1, 20),
    _CLIpv6NeighborBindingCounterDhcpV6RelayForward_Type()
)
cLIpv6NeighborBindingCounterDhcpV6RelayForward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLIpv6NeighborBindingCounterDhcpV6RelayForward.setStatus("current")
_CLIpv6NeighborBindingCounterDhcpV6RelayReplay_Type = Counter32
_CLIpv6NeighborBindingCounterDhcpV6RelayReplay_Object = MibTableColumn
cLIpv6NeighborBindingCounterDhcpV6RelayReplay = _CLIpv6NeighborBindingCounterDhcpV6RelayReplay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 1, 2, 1, 1, 21),
    _CLIpv6NeighborBindingCounterDhcpV6RelayReplay_Type()
)
cLIpv6NeighborBindingCounterDhcpV6RelayReplay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLIpv6NeighborBindingCounterDhcpV6RelayReplay.setStatus("current")
_CLIpv6NbNdSuppressDropCounter_ObjectIdentity = ObjectIdentity
cLIpv6NbNdSuppressDropCounter = _CLIpv6NbNdSuppressDropCounter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 1, 2, 2)
)
_CLIpv6NbNdSuppressDropCounterTotal_Type = Counter32
_CLIpv6NbNdSuppressDropCounterTotal_Object = MibScalar
cLIpv6NbNdSuppressDropCounterTotal = _CLIpv6NbNdSuppressDropCounterTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 1, 2, 2, 1),
    _CLIpv6NbNdSuppressDropCounterTotal_Type()
)
cLIpv6NbNdSuppressDropCounterTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLIpv6NbNdSuppressDropCounterTotal.setStatus("current")
_CLIpv6NbNdSuppressDropCounterReasonSilent_Type = Counter32
_CLIpv6NbNdSuppressDropCounterReasonSilent_Object = MibScalar
cLIpv6NbNdSuppressDropCounterReasonSilent = _CLIpv6NbNdSuppressDropCounterReasonSilent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 1, 2, 2, 2),
    _CLIpv6NbNdSuppressDropCounterReasonSilent_Type()
)
cLIpv6NbNdSuppressDropCounterReasonSilent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLIpv6NbNdSuppressDropCounterReasonSilent.setStatus("current")
_CIpv6NbNdSuppressDropCounterReasonInOut_Type = Counter32
_CIpv6NbNdSuppressDropCounterReasonInOut_Object = MibScalar
cIpv6NbNdSuppressDropCounterReasonInOut = _CIpv6NbNdSuppressDropCounterReasonInOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 1, 2, 2, 3),
    _CIpv6NbNdSuppressDropCounterReasonInOut_Type()
)
cIpv6NbNdSuppressDropCounterReasonInOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpv6NbNdSuppressDropCounterReasonInOut.setStatus("current")
_CLIpv6NbNdSuppressDropCounterReasonDad_Type = Counter32
_CLIpv6NbNdSuppressDropCounterReasonDad_Object = MibScalar
cLIpv6NbNdSuppressDropCounterReasonDad = _CLIpv6NbNdSuppressDropCounterReasonDad_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 1, 2, 2, 4),
    _CLIpv6NbNdSuppressDropCounterReasonDad_Type()
)
cLIpv6NbNdSuppressDropCounterReasonDad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLIpv6NbNdSuppressDropCounterReasonDad.setStatus("current")
_CLIpv6NbNdSuppressDropCounterReasonUnicast_Type = Counter32
_CLIpv6NbNdSuppressDropCounterReasonUnicast_Object = MibScalar
cLIpv6NbNdSuppressDropCounterReasonUnicast = _CLIpv6NbNdSuppressDropCounterReasonUnicast_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 1, 2, 2, 5),
    _CLIpv6NbNdSuppressDropCounterReasonUnicast_Type()
)
cLIpv6NbNdSuppressDropCounterReasonUnicast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLIpv6NbNdSuppressDropCounterReasonUnicast.setStatus("current")
_CLIpv6NbNdSuppressDropCounterReasonMulticast_Type = Counter32
_CLIpv6NbNdSuppressDropCounterReasonMulticast_Object = MibScalar
cLIpv6NbNdSuppressDropCounterReasonMulticast = _CLIpv6NbNdSuppressDropCounterReasonMulticast_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 1, 2, 2, 6),
    _CLIpv6NbNdSuppressDropCounterReasonMulticast_Type()
)
cLIpv6NbNdSuppressDropCounterReasonMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLIpv6NbNdSuppressDropCounterReasonMulticast.setStatus("current")
_CLIpv6NbNdSuppressDropCounterReasonInt_Type = Counter32
_CLIpv6NbNdSuppressDropCounterReasonInt_Object = MibScalar
cLIpv6NbNdSuppressDropCounterReasonInt = _CLIpv6NbNdSuppressDropCounterReasonInt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 1, 2, 2, 7),
    _CLIpv6NbNdSuppressDropCounterReasonInt_Type()
)
cLIpv6NbNdSuppressDropCounterReasonInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLIpv6NbNdSuppressDropCounterReasonInt.setStatus("current")
_CLIpv6NbSnoopingDropCounterTable_Object = MibTable
cLIpv6NbSnoopingDropCounterTable = _CLIpv6NbSnoopingDropCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 1, 2, 3)
)
if mibBuilder.loadTexts:
    cLIpv6NbSnoopingDropCounterTable.setStatus("current")
_CLIpv6NbSnoopingDropCounterEntry_Object = MibTableRow
cLIpv6NbSnoopingDropCounterEntry = _CLIpv6NbSnoopingDropCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 1, 2, 3, 1)
)
cLIpv6NbSnoopingDropCounterEntry.setIndexNames(
    (0, "CISCO-LWAPP-IPV6-MIB", "cLIpv6NbSnoopingDropCounterType"),
)
if mibBuilder.loadTexts:
    cLIpv6NbSnoopingDropCounterEntry.setStatus("current")


class _CLIpv6NbSnoopingDropCounterType_Type(Integer32):
    """Custom type cLIpv6NbSnoopingDropCounterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20)
        )
    )
    namedValues = NamedValues(
        *(("ndpRs", 1),
          ("ndpRa", 2),
          ("ndpNs", 3),
          ("ndpNa", 4),
          ("ndpRedirect", 5),
          ("ndpCertSol", 6),
          ("ndpCertAdv", 7),
          ("dhcpV6Sol", 8),
          ("dhcpV6Adv", 9),
          ("dhcpV6Request", 10),
          ("dhcpV6Confirm", 11),
          ("dhcpV6Renew", 12),
          ("dhcpV6Rebind", 13),
          ("dhcpV6Reply", 14),
          ("dhcpV6Release", 15),
          ("dhcpV6Decline", 16),
          ("dhcpV6Recfg", 17),
          ("dhcpV6InfoReq", 18),
          ("dhcpV6RelayForward", 19),
          ("dhcpV6RelayReplay", 20))
    )


_CLIpv6NbSnoopingDropCounterType_Type.__name__ = "Integer32"
_CLIpv6NbSnoopingDropCounterType_Object = MibTableColumn
cLIpv6NbSnoopingDropCounterType = _CLIpv6NbSnoopingDropCounterType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 1, 2, 3, 1, 1),
    _CLIpv6NbSnoopingDropCounterType_Type()
)
cLIpv6NbSnoopingDropCounterType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLIpv6NbSnoopingDropCounterType.setStatus("current")
_CLIpv6NbSnoopingDropCounterTotal_Type = Counter32
_CLIpv6NbSnoopingDropCounterTotal_Object = MibTableColumn
cLIpv6NbSnoopingDropCounterTotal = _CLIpv6NbSnoopingDropCounterTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 1, 2, 3, 1, 2),
    _CLIpv6NbSnoopingDropCounterTotal_Type()
)
cLIpv6NbSnoopingDropCounterTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLIpv6NbSnoopingDropCounterTotal.setStatus("current")
_CLIpv6NbSnoopingDropCounterSilent_Type = Counter32
_CLIpv6NbSnoopingDropCounterSilent_Object = MibTableColumn
cLIpv6NbSnoopingDropCounterSilent = _CLIpv6NbSnoopingDropCounterSilent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 1, 2, 3, 1, 3),
    _CLIpv6NbSnoopingDropCounterSilent_Type()
)
cLIpv6NbSnoopingDropCounterSilent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLIpv6NbSnoopingDropCounterSilent.setStatus("current")
_CLIpv6NbSnoopingDropCounterReasonInt_Type = Counter32
_CLIpv6NbSnoopingDropCounterReasonInt_Object = MibTableColumn
cLIpv6NbSnoopingDropCounterReasonInt = _CLIpv6NbSnoopingDropCounterReasonInt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 1, 2, 3, 1, 4),
    _CLIpv6NbSnoopingDropCounterReasonInt_Type()
)
cLIpv6NbSnoopingDropCounterReasonInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLIpv6NbSnoopingDropCounterReasonInt.setStatus("current")
_CLIpv6NbSnoopingDropCounterReasonCga_Type = Counter32
_CLIpv6NbSnoopingDropCounterReasonCga_Object = MibTableColumn
cLIpv6NbSnoopingDropCounterReasonCga = _CLIpv6NbSnoopingDropCounterReasonCga_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 1, 2, 3, 1, 5),
    _CLIpv6NbSnoopingDropCounterReasonCga_Type()
)
cLIpv6NbSnoopingDropCounterReasonCga.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLIpv6NbSnoopingDropCounterReasonCga.setStatus("current")
_CLIpv6NbSnoopingDropCounterReasonRsa_Type = Counter32
_CLIpv6NbSnoopingDropCounterReasonRsa_Object = MibTableColumn
cLIpv6NbSnoopingDropCounterReasonRsa = _CLIpv6NbSnoopingDropCounterReasonRsa_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 1, 2, 3, 1, 6),
    _CLIpv6NbSnoopingDropCounterReasonRsa_Type()
)
cLIpv6NbSnoopingDropCounterReasonRsa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLIpv6NbSnoopingDropCounterReasonRsa.setStatus("current")
_CLIpv6NbSnoopingDropCounterReasonLimit_Type = Counter32
_CLIpv6NbSnoopingDropCounterReasonLimit_Object = MibTableColumn
cLIpv6NbSnoopingDropCounterReasonLimit = _CLIpv6NbSnoopingDropCounterReasonLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 1, 2, 3, 1, 7),
    _CLIpv6NbSnoopingDropCounterReasonLimit_Type()
)
cLIpv6NbSnoopingDropCounterReasonLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLIpv6NbSnoopingDropCounterReasonLimit.setStatus("current")
_CLIpv6NbSnoopingDropCounterReasonMartian_Type = Counter32
_CLIpv6NbSnoopingDropCounterReasonMartian_Object = MibTableColumn
cLIpv6NbSnoopingDropCounterReasonMartian = _CLIpv6NbSnoopingDropCounterReasonMartian_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 1, 2, 3, 1, 8),
    _CLIpv6NbSnoopingDropCounterReasonMartian_Type()
)
cLIpv6NbSnoopingDropCounterReasonMartian.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLIpv6NbSnoopingDropCounterReasonMartian.setStatus("current")
_CLIpv6NbSnoopingDropCounterReasonMartianMac_Type = Counter32
_CLIpv6NbSnoopingDropCounterReasonMartianMac_Object = MibTableColumn
cLIpv6NbSnoopingDropCounterReasonMartianMac = _CLIpv6NbSnoopingDropCounterReasonMartianMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 1, 2, 3, 1, 9),
    _CLIpv6NbSnoopingDropCounterReasonMartianMac_Type()
)
cLIpv6NbSnoopingDropCounterReasonMartianMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLIpv6NbSnoopingDropCounterReasonMartianMac.setStatus("current")
_CLIpv6NbSnoopingDropCounterReasonNotAllowed_Type = Counter32
_CLIpv6NbSnoopingDropCounterReasonNotAllowed_Object = MibTableColumn
cLIpv6NbSnoopingDropCounterReasonNotAllowed = _CLIpv6NbSnoopingDropCounterReasonNotAllowed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 1, 2, 3, 1, 10),
    _CLIpv6NbSnoopingDropCounterReasonNotAllowed_Type()
)
cLIpv6NbSnoopingDropCounterReasonNotAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLIpv6NbSnoopingDropCounterReasonNotAllowed.setStatus("current")
_CLIpv6NbSnoopingDropCounterReasonNotAuthorised_Type = Counter32
_CLIpv6NbSnoopingDropCounterReasonNotAuthorised_Object = MibTableColumn
cLIpv6NbSnoopingDropCounterReasonNotAuthorised = _CLIpv6NbSnoopingDropCounterReasonNotAuthorised_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 1, 2, 3, 1, 11),
    _CLIpv6NbSnoopingDropCounterReasonNotAuthorised_Type()
)
cLIpv6NbSnoopingDropCounterReasonNotAuthorised.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLIpv6NbSnoopingDropCounterReasonNotAuthorised.setStatus("current")
_CLIpv6NbSnoopingDropCounterReasonStop_Type = Counter32
_CLIpv6NbSnoopingDropCounterReasonStop_Object = MibTableColumn
cLIpv6NbSnoopingDropCounterReasonStop = _CLIpv6NbSnoopingDropCounterReasonStop_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 1, 2, 3, 1, 12),
    _CLIpv6NbSnoopingDropCounterReasonStop_Type()
)
cLIpv6NbSnoopingDropCounterReasonStop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLIpv6NbSnoopingDropCounterReasonStop.setStatus("current")
_CiscoLwappIpv6MIBConform_ObjectIdentity = ObjectIdentity
ciscoLwappIpv6MIBConform = _CiscoLwappIpv6MIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 2)
)
_CiscoLwappIpv6MIBCompliances_ObjectIdentity = ObjectIdentity
ciscoLwappIpv6MIBCompliances = _CiscoLwappIpv6MIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 2, 1)
)
_CiscoLwappIpv6MIBGroups_ObjectIdentity = ObjectIdentity
ciscoLwappIpv6MIBGroups = _CiscoLwappIpv6MIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 2, 2)
)

# Managed Objects groups

ciscoLwappIpv6MIBConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 2, 2, 1)
)
ciscoLwappIpv6MIBConfigGroup.setObjects(
      *(("CISCO-LWAPP-IPV6-MIB", "cLIpv6NbRaThrottleEnabled"),
        ("CISCO-LWAPP-IPV6-MIB", "cLIpv6NbRaThrottlePeriod"),
        ("CISCO-LWAPP-IPV6-MIB", "cLIpv6NbRaThrottleMaxThrough"),
        ("CISCO-LWAPP-IPV6-MIB", "cLIpv6NbRaThrottleMaxThroughNoLimitEnabled"),
        ("CISCO-LWAPP-IPV6-MIB", "cLIpv6NbRaThrottleIntervalOption"),
        ("CISCO-LWAPP-IPV6-MIB", "cLIpv6NbRaThrottleAllowAtleast"),
        ("CISCO-LWAPP-IPV6-MIB", "cLIpv6NbRaThrottleAllowAtmost"),
        ("CISCO-LWAPP-IPV6-MIB", "cLIpv6NbRaThrottleAllowNoLimitEnabled"),
        ("CISCO-LWAPP-IPV6-MIB", "cLIpv6NbTimerDownLifeTimeEnabled"),
        ("CISCO-LWAPP-IPV6-MIB", "cLIpv6NbTimerDownLifeTimeInterval"),
        ("CISCO-LWAPP-IPV6-MIB", "cLIpv6NbTimerStaleLifeTimeEnabled"),
        ("CISCO-LWAPP-IPV6-MIB", "cLIpv6NbTimerStaleLifeTimeInterval"),
        ("CISCO-LWAPP-IPV6-MIB", "cLIpv6NbTimerReachableLifeTimeEnabled"),
        ("CISCO-LWAPP-IPV6-MIB", "cLIpv6NbTimerReachableLifeTimeInterval"),
        ("CISCO-LWAPP-IPV6-MIB", "cLIpv6NbTimerNsMulticastCacheMissForward"),
        ("CISCO-LWAPP-IPV6-MIB", "cLIpv6AclApplyMode"),
        ("CISCO-LWAPP-IPV6-MIB", "cLIpv6AclCounterClear"),
        ("CISCO-LWAPP-IPV6-MIB", "cLIpv6AclRowStatus"),
        ("CISCO-LWAPP-IPV6-MIB", "cLIpv6AclRuleAction"),
        ("CISCO-LWAPP-IPV6-MIB", "cLIpv6AclRuleDirection"),
        ("CISCO-LWAPP-IPV6-MIB", "cLIpv6AclRuleSourceInetAddressType"),
        ("CISCO-LWAPP-IPV6-MIB", "cLIpv6AclRuleSourceInetAddress"),
        ("CISCO-LWAPP-IPV6-MIB", "cLIpv6AclRuleSourcePrefixLength"),
        ("CISCO-LWAPP-IPV6-MIB", "cLIpv6AclRuleDestinationInetAddressType"),
        ("CISCO-LWAPP-IPV6-MIB", "cLIpv6AclRuleDestinationInetAddress"),
        ("CISCO-LWAPP-IPV6-MIB", "cLIpv6AclRuleDestinationPrefixLength"),
        ("CISCO-LWAPP-IPV6-MIB", "cLIpv6AclRuleProtocol"),
        ("CISCO-LWAPP-IPV6-MIB", "cLIpv6AclRuleStartSourcePort"),
        ("CISCO-LWAPP-IPV6-MIB", "cLIpv6AclRuleEndSourcePort"),
        ("CISCO-LWAPP-IPV6-MIB", "cLIpv6AclRuleStartDestinationPort"),
        ("CISCO-LWAPP-IPV6-MIB", "cLIpv6AclRuleEndDestinationPort"),
        ("CISCO-LWAPP-IPV6-MIB", "cLIpv6AclRuleDscp"),
        ("CISCO-LWAPP-IPV6-MIB", "cLIpv6AclNewRuleIndex"),
        ("CISCO-LWAPP-IPV6-MIB", "cLIpv6AclRuleHits"),
        ("CISCO-LWAPP-IPV6-MIB", "cLIpv6AclRuleRowStatus"),
        ("CISCO-LWAPP-IPV6-MIB", "cLIpv6RaFilteringEnabled"),
        ("CISCO-LWAPP-IPV6-MIB", "cLIpv6RaFilteringOnApEnabled"),
        ("CISCO-LWAPP-IPV6-MIB", "cLIpv6RaFilteringClientInfoApName"),
        ("CISCO-LWAPP-IPV6-MIB", "cLIpv6RaFilteringClientInfoWlan"),
        ("CISCO-LWAPP-IPV6-MIB", "cLIpv6RaFilteringClientInfoPktsDropped"),
        ("CISCO-LWAPP-IPV6-MIB", "cLIpv6NeighborBindingCounterClear"),
        ("CISCO-LWAPP-IPV6-MIB", "cLIpv6GlobalEnabled"))
)
if mibBuilder.loadTexts:
    ciscoLwappIpv6MIBConfigGroup.setStatus("current")

ciscoLwappIpv6MIBStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 2, 2, 2)
)
ciscoLwappIpv6MIBStatsGroup.setObjects(
      *(("CISCO-LWAPP-IPV6-MIB", "cLIpv6NeighborBindingCounterNdpRs"),
        ("CISCO-LWAPP-IPV6-MIB", "cLIpv6NeighborBindingCounterNdpRa"),
        ("CISCO-LWAPP-IPV6-MIB", "cLIpv6NeighborBindingCounterNdpNs"),
        ("CISCO-LWAPP-IPV6-MIB", "cLIpv6NeighborBindingCounterNdpNa"),
        ("CISCO-LWAPP-IPV6-MIB", "cLIpv6NeighborBindingCounterNdpRedirect"),
        ("CISCO-LWAPP-IPV6-MIB", "cLIpv6NeighborBindingCounterNdpCertSol"),
        ("CISCO-LWAPP-IPV6-MIB", "cLIpv6NeighborBindingCounterNdpCertAdv"),
        ("CISCO-LWAPP-IPV6-MIB", "cLIpv6NeighborBindingCounterDhcpV6Sol"),
        ("CISCO-LWAPP-IPV6-MIB", "cLIpv6NeighborBindingCounterDhcpV6Adv"),
        ("CISCO-LWAPP-IPV6-MIB", "cLIpv6NeighborBindingCounterDhcpV6Request"),
        ("CISCO-LWAPP-IPV6-MIB", "cLIpv6NeighborBindingCounterDhcpV6Confirm"),
        ("CISCO-LWAPP-IPV6-MIB", "cLIpv6NeighborBindingCounterDhcpV6Renew"),
        ("CISCO-LWAPP-IPV6-MIB", "cLIpv6NeighborBindingCounterDhcpV6Rebind"),
        ("CISCO-LWAPP-IPV6-MIB", "cLIpv6NeighborBindingCounterDhcpV6Reply"),
        ("CISCO-LWAPP-IPV6-MIB", "cLIpv6NeighborBindingCounterDhcpV6Release"),
        ("CISCO-LWAPP-IPV6-MIB", "cLIpv6NeighborBindingCounterDhcpV6Decline"),
        ("CISCO-LWAPP-IPV6-MIB", "cLIpv6NeighborBindingCounterDhcpV6Recfg"),
        ("CISCO-LWAPP-IPV6-MIB", "cLIpv6NeighborBindingCounterDhcpV6InfoReq"),
        ("CISCO-LWAPP-IPV6-MIB", "cLIpv6NeighborBindingCounterDhcpV6RelayForward"),
        ("CISCO-LWAPP-IPV6-MIB", "cLIpv6NeighborBindingCounterDhcpV6RelayReplay"),
        ("CISCO-LWAPP-IPV6-MIB", "cLIpv6NbNdSuppressDropCounterTotal"),
        ("CISCO-LWAPP-IPV6-MIB", "cLIpv6NbNdSuppressDropCounterReasonSilent"),
        ("CISCO-LWAPP-IPV6-MIB", "cIpv6NbNdSuppressDropCounterReasonInOut"),
        ("CISCO-LWAPP-IPV6-MIB", "cLIpv6NbNdSuppressDropCounterReasonDad"),
        ("CISCO-LWAPP-IPV6-MIB", "cLIpv6NbNdSuppressDropCounterReasonUnicast"),
        ("CISCO-LWAPP-IPV6-MIB", "cLIpv6NbNdSuppressDropCounterReasonMulticast"),
        ("CISCO-LWAPP-IPV6-MIB", "cLIpv6NbNdSuppressDropCounterReasonInt"),
        ("CISCO-LWAPP-IPV6-MIB", "cLIpv6NbSnoopingDropCounterTotal"),
        ("CISCO-LWAPP-IPV6-MIB", "cLIpv6NbSnoopingDropCounterSilent"),
        ("CISCO-LWAPP-IPV6-MIB", "cLIpv6NbSnoopingDropCounterReasonInt"),
        ("CISCO-LWAPP-IPV6-MIB", "cLIpv6NbSnoopingDropCounterReasonCga"),
        ("CISCO-LWAPP-IPV6-MIB", "cLIpv6NbSnoopingDropCounterReasonRsa"),
        ("CISCO-LWAPP-IPV6-MIB", "cLIpv6NbSnoopingDropCounterReasonLimit"),
        ("CISCO-LWAPP-IPV6-MIB", "cLIpv6NbSnoopingDropCounterReasonMartian"),
        ("CISCO-LWAPP-IPV6-MIB", "cLIpv6NbSnoopingDropCounterReasonMartianMac"),
        ("CISCO-LWAPP-IPV6-MIB", "cLIpv6NbSnoopingDropCounterReasonNotAllowed"),
        ("CISCO-LWAPP-IPV6-MIB", "cLIpv6NbSnoopingDropCounterReasonNotAuthorised"),
        ("CISCO-LWAPP-IPV6-MIB", "cLIpv6NbSnoopingDropCounterReasonStop"))
)
if mibBuilder.loadTexts:
    ciscoLwappIpv6MIBStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoLwappIpv6MIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 847, 2, 1, 1)
)
ciscoLwappIpv6MIBCompliance.setObjects(
      *(("CISCO-LWAPP-IPV6-MIB", "ciscoLwappIpv6MIBConfigGroup"),
        ("CISCO-LWAPP-IPV6-MIB", "ciscoLwappIpv6MIBStatsGroup"))
)
if mibBuilder.loadTexts:
    ciscoLwappIpv6MIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-LWAPP-IPV6-MIB",
    **{"ciscoLwappIpv6MIB": ciscoLwappIpv6MIB,
       "ciscoLwappIpv6MIBNotifs": ciscoLwappIpv6MIBNotifs,
       "ciscoLwappIpv6MIBObjects": ciscoLwappIpv6MIBObjects,
       "ciscoLwappIpv6Config": ciscoLwappIpv6Config,
       "cLIpv6AclTable": cLIpv6AclTable,
       "cLIpv6AclEntry": cLIpv6AclEntry,
       "cLIpv6AclName": cLIpv6AclName,
       "cLIpv6AclApplyMode": cLIpv6AclApplyMode,
       "cLIpv6AclCounterClear": cLIpv6AclCounterClear,
       "cLIpv6AclRowStatus": cLIpv6AclRowStatus,
       "cLIpv6AclRuleTable": cLIpv6AclRuleTable,
       "cLIpv6AclRuleEntry": cLIpv6AclRuleEntry,
       "cLIpv6AclRuleIndex": cLIpv6AclRuleIndex,
       "cLIpv6AclRuleAction": cLIpv6AclRuleAction,
       "cLIpv6AclRuleDirection": cLIpv6AclRuleDirection,
       "cLIpv6AclRuleSourceInetAddressType": cLIpv6AclRuleSourceInetAddressType,
       "cLIpv6AclRuleSourceInetAddress": cLIpv6AclRuleSourceInetAddress,
       "cLIpv6AclRuleSourcePrefixLength": cLIpv6AclRuleSourcePrefixLength,
       "cLIpv6AclRuleDestinationInetAddressType": cLIpv6AclRuleDestinationInetAddressType,
       "cLIpv6AclRuleDestinationInetAddress": cLIpv6AclRuleDestinationInetAddress,
       "cLIpv6AclRuleDestinationPrefixLength": cLIpv6AclRuleDestinationPrefixLength,
       "cLIpv6AclRuleProtocol": cLIpv6AclRuleProtocol,
       "cLIpv6AclRuleStartSourcePort": cLIpv6AclRuleStartSourcePort,
       "cLIpv6AclRuleEndSourcePort": cLIpv6AclRuleEndSourcePort,
       "cLIpv6AclRuleStartDestinationPort": cLIpv6AclRuleStartDestinationPort,
       "cLIpv6AclRuleEndDestinationPort": cLIpv6AclRuleEndDestinationPort,
       "cLIpv6AclRuleDscp": cLIpv6AclRuleDscp,
       "cLIpv6AclNewRuleIndex": cLIpv6AclNewRuleIndex,
       "cLIpv6AclRuleHits": cLIpv6AclRuleHits,
       "cLIpv6AclRuleRowStatus": cLIpv6AclRuleRowStatus,
       "ciscoLwappIpv6RaFiltering": ciscoLwappIpv6RaFiltering,
       "cLIpv6RaFilteringEnabled": cLIpv6RaFilteringEnabled,
       "cLIpv6RaFilteringOnApEnabled": cLIpv6RaFilteringOnApEnabled,
       "cLIpv6RaFilteringClientInfoTable": cLIpv6RaFilteringClientInfoTable,
       "cLIpv6RaFilteringClientInfoEntry": cLIpv6RaFilteringClientInfoEntry,
       "cLIpv6RaFilteringClientInfoApName": cLIpv6RaFilteringClientInfoApName,
       "cLIpv6RaFilteringClientInfoWlan": cLIpv6RaFilteringClientInfoWlan,
       "cLIpv6RaFilteringClientInfoPktsDropped": cLIpv6RaFilteringClientInfoPktsDropped,
       "ciscoLwappIpv6NbRaThrottleConfig": ciscoLwappIpv6NbRaThrottleConfig,
       "cLIpv6NbRaThrottleEnabled": cLIpv6NbRaThrottleEnabled,
       "cLIpv6NbRaThrottlePeriod": cLIpv6NbRaThrottlePeriod,
       "cLIpv6NbRaThrottleMaxThrough": cLIpv6NbRaThrottleMaxThrough,
       "cLIpv6NbRaThrottleMaxThroughNoLimitEnabled": cLIpv6NbRaThrottleMaxThroughNoLimitEnabled,
       "cLIpv6NbRaThrottleIntervalOption": cLIpv6NbRaThrottleIntervalOption,
       "cLIpv6NbRaThrottleAllowAtleast": cLIpv6NbRaThrottleAllowAtleast,
       "cLIpv6NbRaThrottleAllowAtmost": cLIpv6NbRaThrottleAllowAtmost,
       "cLIpv6NbRaThrottleAllowNoLimitEnabled": cLIpv6NbRaThrottleAllowNoLimitEnabled,
       "ciscoLwappIpv6NbTimerConfig": ciscoLwappIpv6NbTimerConfig,
       "cLIpv6NbTimerDownLifeTimeEnabled": cLIpv6NbTimerDownLifeTimeEnabled,
       "cLIpv6NbTimerDownLifeTimeInterval": cLIpv6NbTimerDownLifeTimeInterval,
       "cLIpv6NbTimerStaleLifeTimeEnabled": cLIpv6NbTimerStaleLifeTimeEnabled,
       "cLIpv6NbTimerStaleLifeTimeInterval": cLIpv6NbTimerStaleLifeTimeInterval,
       "cLIpv6NbTimerReachableLifeTimeEnabled": cLIpv6NbTimerReachableLifeTimeEnabled,
       "cLIpv6NbTimerReachableLifeTimeInterval": cLIpv6NbTimerReachableLifeTimeInterval,
       "cLIpv6NbTimerNsMulticastCacheMissForward": cLIpv6NbTimerNsMulticastCacheMissForward,
       "cLIpv6NeighborBindingCounterClear": cLIpv6NeighborBindingCounterClear,
       "cLIpv6GlobalEnabled": cLIpv6GlobalEnabled,
       "ciscoLwappIpv6Stats": ciscoLwappIpv6Stats,
       "cLIpv6NeighborBindingCounterTable": cLIpv6NeighborBindingCounterTable,
       "cLIpv6NeighborBindingCounterEntry": cLIpv6NeighborBindingCounterEntry,
       "cLIpv6NeighborBindingCounterType": cLIpv6NeighborBindingCounterType,
       "cLIpv6NeighborBindingCounterNdpRs": cLIpv6NeighborBindingCounterNdpRs,
       "cLIpv6NeighborBindingCounterNdpRa": cLIpv6NeighborBindingCounterNdpRa,
       "cLIpv6NeighborBindingCounterNdpNs": cLIpv6NeighborBindingCounterNdpNs,
       "cLIpv6NeighborBindingCounterNdpNa": cLIpv6NeighborBindingCounterNdpNa,
       "cLIpv6NeighborBindingCounterNdpRedirect": cLIpv6NeighborBindingCounterNdpRedirect,
       "cLIpv6NeighborBindingCounterNdpCertSol": cLIpv6NeighborBindingCounterNdpCertSol,
       "cLIpv6NeighborBindingCounterNdpCertAdv": cLIpv6NeighborBindingCounterNdpCertAdv,
       "cLIpv6NeighborBindingCounterDhcpV6Sol": cLIpv6NeighborBindingCounterDhcpV6Sol,
       "cLIpv6NeighborBindingCounterDhcpV6Adv": cLIpv6NeighborBindingCounterDhcpV6Adv,
       "cLIpv6NeighborBindingCounterDhcpV6Request": cLIpv6NeighborBindingCounterDhcpV6Request,
       "cLIpv6NeighborBindingCounterDhcpV6Confirm": cLIpv6NeighborBindingCounterDhcpV6Confirm,
       "cLIpv6NeighborBindingCounterDhcpV6Renew": cLIpv6NeighborBindingCounterDhcpV6Renew,
       "cLIpv6NeighborBindingCounterDhcpV6Rebind": cLIpv6NeighborBindingCounterDhcpV6Rebind,
       "cLIpv6NeighborBindingCounterDhcpV6Reply": cLIpv6NeighborBindingCounterDhcpV6Reply,
       "cLIpv6NeighborBindingCounterDhcpV6Release": cLIpv6NeighborBindingCounterDhcpV6Release,
       "cLIpv6NeighborBindingCounterDhcpV6Decline": cLIpv6NeighborBindingCounterDhcpV6Decline,
       "cLIpv6NeighborBindingCounterDhcpV6Recfg": cLIpv6NeighborBindingCounterDhcpV6Recfg,
       "cLIpv6NeighborBindingCounterDhcpV6InfoReq": cLIpv6NeighborBindingCounterDhcpV6InfoReq,
       "cLIpv6NeighborBindingCounterDhcpV6RelayForward": cLIpv6NeighborBindingCounterDhcpV6RelayForward,
       "cLIpv6NeighborBindingCounterDhcpV6RelayReplay": cLIpv6NeighborBindingCounterDhcpV6RelayReplay,
       "cLIpv6NbNdSuppressDropCounter": cLIpv6NbNdSuppressDropCounter,
       "cLIpv6NbNdSuppressDropCounterTotal": cLIpv6NbNdSuppressDropCounterTotal,
       "cLIpv6NbNdSuppressDropCounterReasonSilent": cLIpv6NbNdSuppressDropCounterReasonSilent,
       "cIpv6NbNdSuppressDropCounterReasonInOut": cIpv6NbNdSuppressDropCounterReasonInOut,
       "cLIpv6NbNdSuppressDropCounterReasonDad": cLIpv6NbNdSuppressDropCounterReasonDad,
       "cLIpv6NbNdSuppressDropCounterReasonUnicast": cLIpv6NbNdSuppressDropCounterReasonUnicast,
       "cLIpv6NbNdSuppressDropCounterReasonMulticast": cLIpv6NbNdSuppressDropCounterReasonMulticast,
       "cLIpv6NbNdSuppressDropCounterReasonInt": cLIpv6NbNdSuppressDropCounterReasonInt,
       "cLIpv6NbSnoopingDropCounterTable": cLIpv6NbSnoopingDropCounterTable,
       "cLIpv6NbSnoopingDropCounterEntry": cLIpv6NbSnoopingDropCounterEntry,
       "cLIpv6NbSnoopingDropCounterType": cLIpv6NbSnoopingDropCounterType,
       "cLIpv6NbSnoopingDropCounterTotal": cLIpv6NbSnoopingDropCounterTotal,
       "cLIpv6NbSnoopingDropCounterSilent": cLIpv6NbSnoopingDropCounterSilent,
       "cLIpv6NbSnoopingDropCounterReasonInt": cLIpv6NbSnoopingDropCounterReasonInt,
       "cLIpv6NbSnoopingDropCounterReasonCga": cLIpv6NbSnoopingDropCounterReasonCga,
       "cLIpv6NbSnoopingDropCounterReasonRsa": cLIpv6NbSnoopingDropCounterReasonRsa,
       "cLIpv6NbSnoopingDropCounterReasonLimit": cLIpv6NbSnoopingDropCounterReasonLimit,
       "cLIpv6NbSnoopingDropCounterReasonMartian": cLIpv6NbSnoopingDropCounterReasonMartian,
       "cLIpv6NbSnoopingDropCounterReasonMartianMac": cLIpv6NbSnoopingDropCounterReasonMartianMac,
       "cLIpv6NbSnoopingDropCounterReasonNotAllowed": cLIpv6NbSnoopingDropCounterReasonNotAllowed,
       "cLIpv6NbSnoopingDropCounterReasonNotAuthorised": cLIpv6NbSnoopingDropCounterReasonNotAuthorised,
       "cLIpv6NbSnoopingDropCounterReasonStop": cLIpv6NbSnoopingDropCounterReasonStop,
       "ciscoLwappIpv6MIBConform": ciscoLwappIpv6MIBConform,
       "ciscoLwappIpv6MIBCompliances": ciscoLwappIpv6MIBCompliances,
       "ciscoLwappIpv6MIBCompliance": ciscoLwappIpv6MIBCompliance,
       "ciscoLwappIpv6MIBGroups": ciscoLwappIpv6MIBGroups,
       "ciscoLwappIpv6MIBConfigGroup": ciscoLwappIpv6MIBConfigGroup,
       "ciscoLwappIpv6MIBStatsGroup": ciscoLwappIpv6MIBStatsGroup}
)
