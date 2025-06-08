# SNMP MIB module (CLAB-MAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cablelabs_4491/CLAB-MAP-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 22:39:27 2025
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

(clabCommonMibs,) = mibBuilder.importSymbols(
    "CLAB-DEF-MIB",
    "clabCommonMibs")

(InetAddressIPv4,
 InetAddressIPv6,
 InetAddressPrefixLength) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv4",
    "InetAddressIPv6",
    "InetAddressPrefixLength")

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

clabMAPMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 4, 4)
)
if mibBuilder.loadTexts:
    clabMAPMib.setRevisions(
        ("2015-12-16 00:00",
         "2015-10-28 00:00",
         "2015-07-29 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ClabMAPNotifications_ObjectIdentity = ObjectIdentity
clabMAPNotifications = _ClabMAPNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 4, 4, 0)
)
_ClabMAPObjects_ObjectIdentity = ObjectIdentity
clabMAPObjects = _ClabMAPObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 4, 4, 1)
)


class _ClabMAPEnable_Type(TruthValue):
    """Custom type clabMAPEnable based on TruthValue"""
    defaultValue = 2


_ClabMAPEnable_Type.__name__ = "TruthValue"
_ClabMAPEnable_Object = MibScalar
clabMAPEnable = _ClabMAPEnable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 4, 1, 1),
    _ClabMAPEnable_Type()
)
clabMAPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clabMAPEnable.setStatus("current")


class _ClabMAPTunnelDomainNumEntries_Type(Unsigned32):
    """Custom type clabMAPTunnelDomainNumEntries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_ClabMAPTunnelDomainNumEntries_Type.__name__ = "Unsigned32"
_ClabMAPTunnelDomainNumEntries_Object = MibScalar
clabMAPTunnelDomainNumEntries = _ClabMAPTunnelDomainNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 4, 1, 2),
    _ClabMAPTunnelDomainNumEntries_Type()
)
clabMAPTunnelDomainNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabMAPTunnelDomainNumEntries.setStatus("current")


class _ClabMAPDomainRuleNumEntries_Type(Unsigned32):
    """Custom type clabMAPDomainRuleNumEntries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ClabMAPDomainRuleNumEntries_Type.__name__ = "Unsigned32"
_ClabMAPDomainRuleNumEntries_Object = MibScalar
clabMAPDomainRuleNumEntries = _ClabMAPDomainRuleNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 4, 1, 3),
    _ClabMAPDomainRuleNumEntries_Type()
)
clabMAPDomainRuleNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabMAPDomainRuleNumEntries.setStatus("current")
_ClabMAPDomainTable_Object = MibTable
clabMAPDomainTable = _ClabMAPDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 4, 1, 4)
)
if mibBuilder.loadTexts:
    clabMAPDomainTable.setStatus("current")
_ClabMAPDomainEntry_Object = MibTableRow
clabMAPDomainEntry = _ClabMAPDomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 4, 1, 4, 1)
)
clabMAPDomainEntry.setIndexNames(
    (0, "CLAB-MAP-MIB", "clabMAPDomainIndex"),
)
if mibBuilder.loadTexts:
    clabMAPDomainEntry.setStatus("current")


class _ClabMAPDomainIndex_Type(Unsigned32):
    """Custom type clabMAPDomainIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_ClabMAPDomainIndex_Type.__name__ = "Unsigned32"
_ClabMAPDomainIndex_Object = MibTableColumn
clabMAPDomainIndex = _ClabMAPDomainIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 4, 1, 4, 1, 1),
    _ClabMAPDomainIndex_Type()
)
clabMAPDomainIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clabMAPDomainIndex.setStatus("current")


class _ClabMAPDomainEnable_Type(TruthValue):
    """Custom type clabMAPDomainEnable based on TruthValue"""
    defaultValue = 2


_ClabMAPDomainEnable_Type.__name__ = "TruthValue"
_ClabMAPDomainEnable_Object = MibTableColumn
clabMAPDomainEnable = _ClabMAPDomainEnable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 4, 1, 4, 1, 2),
    _ClabMAPDomainEnable_Type()
)
clabMAPDomainEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabMAPDomainEnable.setStatus("current")


class _ClabMAPDomainStatus_Type(Integer32):
    """Custom type clabMAPDomainStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("errorMisconfigured", 3),
          ("error", 4))
    )


_ClabMAPDomainStatus_Type.__name__ = "Integer32"
_ClabMAPDomainStatus_Object = MibTableColumn
clabMAPDomainStatus = _ClabMAPDomainStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 4, 1, 4, 1, 3),
    _ClabMAPDomainStatus_Type()
)
clabMAPDomainStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabMAPDomainStatus.setStatus("current")
_ClabMAPDomainAlias_Type = SnmpAdminString
_ClabMAPDomainAlias_Object = MibTableColumn
clabMAPDomainAlias = _ClabMAPDomainAlias_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 4, 1, 4, 1, 4),
    _ClabMAPDomainAlias_Type()
)
clabMAPDomainAlias.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabMAPDomainAlias.setStatus("current")


class _ClabMAPDomainTransportMode_Type(Integer32):
    """Custom type clabMAPDomainTransportMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("encapsulation", 1),
          ("translation", 2))
    )


_ClabMAPDomainTransportMode_Type.__name__ = "Integer32"
_ClabMAPDomainTransportMode_Object = MibTableColumn
clabMAPDomainTransportMode = _ClabMAPDomainTransportMode_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 4, 1, 4, 1, 5),
    _ClabMAPDomainTransportMode_Type()
)
clabMAPDomainTransportMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabMAPDomainTransportMode.setStatus("current")


class _ClabMAPDomainWANInterface_Type(OctetString):
    """Custom type clabMAPDomainWANInterface based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_ClabMAPDomainWANInterface_Type.__name__ = "OctetString"
_ClabMAPDomainWANInterface_Object = MibTableColumn
clabMAPDomainWANInterface = _ClabMAPDomainWANInterface_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 4, 1, 4, 1, 6),
    _ClabMAPDomainWANInterface_Type()
)
clabMAPDomainWANInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabMAPDomainWANInterface.setStatus("current")
_ClabMAPDomainIPv6Prefix_Type = InetAddressIPv6
_ClabMAPDomainIPv6Prefix_Object = MibTableColumn
clabMAPDomainIPv6Prefix = _ClabMAPDomainIPv6Prefix_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 4, 1, 4, 1, 7),
    _ClabMAPDomainIPv6Prefix_Type()
)
clabMAPDomainIPv6Prefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabMAPDomainIPv6Prefix.setStatus("current")


class _ClabMAPDomainIPv6PrefixLen_Type(InetAddressPrefixLength):
    """Custom type clabMAPDomainIPv6PrefixLen based on InetAddressPrefixLength"""
    defaultValue = 0


_ClabMAPDomainIPv6PrefixLen_Type.__name__ = "InetAddressPrefixLength"
_ClabMAPDomainIPv6PrefixLen_Object = MibTableColumn
clabMAPDomainIPv6PrefixLen = _ClabMAPDomainIPv6PrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 4, 1, 4, 1, 8),
    _ClabMAPDomainIPv6PrefixLen_Type()
)
clabMAPDomainIPv6PrefixLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabMAPDomainIPv6PrefixLen.setStatus("current")
_ClabMAPDomainBRIPv6Prefix_Type = InetAddressIPv6
_ClabMAPDomainBRIPv6Prefix_Object = MibTableColumn
clabMAPDomainBRIPv6Prefix = _ClabMAPDomainBRIPv6Prefix_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 4, 1, 4, 1, 9),
    _ClabMAPDomainBRIPv6Prefix_Type()
)
clabMAPDomainBRIPv6Prefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabMAPDomainBRIPv6Prefix.setStatus("current")
_ClabMAPDomainBRIPv6PrefixLen_Type = InetAddressPrefixLength
_ClabMAPDomainBRIPv6PrefixLen_Object = MibTableColumn
clabMAPDomainBRIPv6PrefixLen = _ClabMAPDomainBRIPv6PrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 4, 1, 4, 1, 10),
    _ClabMAPDomainBRIPv6PrefixLen_Type()
)
clabMAPDomainBRIPv6PrefixLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabMAPDomainBRIPv6PrefixLen.setStatus("current")


class _ClabMAPDomainDSCPMarkPolicy_Type(Integer32):
    """Custom type clabMAPDomainDSCPMarkPolicy based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 63),
    )


_ClabMAPDomainDSCPMarkPolicy_Type.__name__ = "Integer32"
_ClabMAPDomainDSCPMarkPolicy_Object = MibTableColumn
clabMAPDomainDSCPMarkPolicy = _ClabMAPDomainDSCPMarkPolicy_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 4, 1, 4, 1, 11),
    _ClabMAPDomainDSCPMarkPolicy_Type()
)
clabMAPDomainDSCPMarkPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabMAPDomainDSCPMarkPolicy.setStatus("current")


class _ClabMAPDomainPSIDOffset_Type(Unsigned32):
    """Custom type clabMAPDomainPSIDOffset based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_ClabMAPDomainPSIDOffset_Type.__name__ = "Unsigned32"
_ClabMAPDomainPSIDOffset_Object = MibTableColumn
clabMAPDomainPSIDOffset = _ClabMAPDomainPSIDOffset_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 4, 1, 4, 1, 12),
    _ClabMAPDomainPSIDOffset_Type()
)
clabMAPDomainPSIDOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabMAPDomainPSIDOffset.setStatus("current")


class _ClabMAPDomainPSIDLength_Type(Unsigned32):
    """Custom type clabMAPDomainPSIDLength based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_ClabMAPDomainPSIDLength_Type.__name__ = "Unsigned32"
_ClabMAPDomainPSIDLength_Object = MibTableColumn
clabMAPDomainPSIDLength = _ClabMAPDomainPSIDLength_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 4, 1, 4, 1, 13),
    _ClabMAPDomainPSIDLength_Type()
)
clabMAPDomainPSIDLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabMAPDomainPSIDLength.setStatus("current")


class _ClabMAPDomainPSID_Type(Unsigned32):
    """Custom type clabMAPDomainPSID based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ClabMAPDomainPSID_Type.__name__ = "Unsigned32"
_ClabMAPDomainPSID_Object = MibTableColumn
clabMAPDomainPSID = _ClabMAPDomainPSID_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 4, 1, 4, 1, 14),
    _ClabMAPDomainPSID_Type()
)
clabMAPDomainPSID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabMAPDomainPSID.setStatus("current")


class _ClabMAPDomainIncludeSystemPorts_Type(TruthValue):
    """Custom type clabMAPDomainIncludeSystemPorts based on TruthValue"""
    defaultValue = 2


_ClabMAPDomainIncludeSystemPorts_Type.__name__ = "TruthValue"
_ClabMAPDomainIncludeSystemPorts_Object = MibTableColumn
clabMAPDomainIncludeSystemPorts = _ClabMAPDomainIncludeSystemPorts_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 4, 1, 4, 1, 15),
    _ClabMAPDomainIncludeSystemPorts_Type()
)
clabMAPDomainIncludeSystemPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabMAPDomainIncludeSystemPorts.setStatus("current")
_ClabMAPDomainRowStatus_Type = RowStatus
_ClabMAPDomainRowStatus_Object = MibTableColumn
clabMAPDomainRowStatus = _ClabMAPDomainRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 4, 1, 4, 1, 16),
    _ClabMAPDomainRowStatus_Type()
)
clabMAPDomainRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabMAPDomainRowStatus.setStatus("current")
_ClabMAPDomainRuleTable_Object = MibTable
clabMAPDomainRuleTable = _ClabMAPDomainRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 4, 1, 5)
)
if mibBuilder.loadTexts:
    clabMAPDomainRuleTable.setStatus("current")
_ClabMAPDomainRuleEntry_Object = MibTableRow
clabMAPDomainRuleEntry = _ClabMAPDomainRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 4, 1, 5, 1)
)
clabMAPDomainRuleEntry.setIndexNames(
    (0, "CLAB-MAP-MIB", "clabMAPDomainIndex"),
    (0, "CLAB-MAP-MIB", "clabMAPDomainRuleIndex"),
)
if mibBuilder.loadTexts:
    clabMAPDomainRuleEntry.setStatus("current")


class _ClabMAPDomainRuleIndex_Type(Unsigned32):
    """Custom type clabMAPDomainRuleIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_ClabMAPDomainRuleIndex_Type.__name__ = "Unsigned32"
_ClabMAPDomainRuleIndex_Object = MibTableColumn
clabMAPDomainRuleIndex = _ClabMAPDomainRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 4, 1, 5, 1, 1),
    _ClabMAPDomainRuleIndex_Type()
)
clabMAPDomainRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clabMAPDomainRuleIndex.setStatus("current")
_ClabMAPDomainRuleEnable_Type = TruthValue
_ClabMAPDomainRuleEnable_Object = MibTableColumn
clabMAPDomainRuleEnable = _ClabMAPDomainRuleEnable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 4, 1, 5, 1, 2),
    _ClabMAPDomainRuleEnable_Type()
)
clabMAPDomainRuleEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabMAPDomainRuleEnable.setStatus("current")


class _ClabMAPDomainRuleStatus_Type(Integer32):
    """Custom type clabMAPDomainRuleStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("error", 3))
    )


_ClabMAPDomainRuleStatus_Type.__name__ = "Integer32"
_ClabMAPDomainRuleStatus_Object = MibTableColumn
clabMAPDomainRuleStatus = _ClabMAPDomainRuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 4, 1, 5, 1, 3),
    _ClabMAPDomainRuleStatus_Type()
)
clabMAPDomainRuleStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabMAPDomainRuleStatus.setStatus("current")
_ClabMAPDomainRuleAlias_Type = SnmpAdminString
_ClabMAPDomainRuleAlias_Object = MibTableColumn
clabMAPDomainRuleAlias = _ClabMAPDomainRuleAlias_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 4, 1, 5, 1, 4),
    _ClabMAPDomainRuleAlias_Type()
)
clabMAPDomainRuleAlias.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabMAPDomainRuleAlias.setStatus("current")


class _ClabMAPDomainRuleOrigin_Type(Integer32):
    """Custom type clabMAPDomainRuleOrigin based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dhcpv6", 1),
          ("static", 2))
    )


_ClabMAPDomainRuleOrigin_Type.__name__ = "Integer32"
_ClabMAPDomainRuleOrigin_Object = MibTableColumn
clabMAPDomainRuleOrigin = _ClabMAPDomainRuleOrigin_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 4, 1, 5, 1, 5),
    _ClabMAPDomainRuleOrigin_Type()
)
clabMAPDomainRuleOrigin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabMAPDomainRuleOrigin.setStatus("current")
_ClabMAPDomainRuleIPv6Prefix_Type = InetAddressIPv6
_ClabMAPDomainRuleIPv6Prefix_Object = MibTableColumn
clabMAPDomainRuleIPv6Prefix = _ClabMAPDomainRuleIPv6Prefix_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 4, 1, 5, 1, 6),
    _ClabMAPDomainRuleIPv6Prefix_Type()
)
clabMAPDomainRuleIPv6Prefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabMAPDomainRuleIPv6Prefix.setStatus("current")


class _ClabMAPDomainRuleIPv6PrefixLen_Type(InetAddressPrefixLength):
    """Custom type clabMAPDomainRuleIPv6PrefixLen based on InetAddressPrefixLength"""
    defaultValue = 0


_ClabMAPDomainRuleIPv6PrefixLen_Type.__name__ = "InetAddressPrefixLength"
_ClabMAPDomainRuleIPv6PrefixLen_Object = MibTableColumn
clabMAPDomainRuleIPv6PrefixLen = _ClabMAPDomainRuleIPv6PrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 4, 1, 5, 1, 7),
    _ClabMAPDomainRuleIPv6PrefixLen_Type()
)
clabMAPDomainRuleIPv6PrefixLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabMAPDomainRuleIPv6PrefixLen.setStatus("current")
_ClabMAPDomainRuleIPv4Prefix_Type = InetAddressIPv4
_ClabMAPDomainRuleIPv4Prefix_Object = MibTableColumn
clabMAPDomainRuleIPv4Prefix = _ClabMAPDomainRuleIPv4Prefix_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 4, 1, 5, 1, 8),
    _ClabMAPDomainRuleIPv4Prefix_Type()
)
clabMAPDomainRuleIPv4Prefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabMAPDomainRuleIPv4Prefix.setStatus("current")


class _ClabMAPDomainRuleIPv4PrefixLen_Type(InetAddressPrefixLength):
    """Custom type clabMAPDomainRuleIPv4PrefixLen based on InetAddressPrefixLength"""
    defaultValue = 0


_ClabMAPDomainRuleIPv4PrefixLen_Type.__name__ = "InetAddressPrefixLength"
_ClabMAPDomainRuleIPv4PrefixLen_Object = MibTableColumn
clabMAPDomainRuleIPv4PrefixLen = _ClabMAPDomainRuleIPv4PrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 4, 1, 5, 1, 9),
    _ClabMAPDomainRuleIPv4PrefixLen_Type()
)
clabMAPDomainRuleIPv4PrefixLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabMAPDomainRuleIPv4PrefixLen.setStatus("current")


class _ClabMAPDomainRuleEABitsLength_Type(Unsigned32):
    """Custom type clabMAPDomainRuleEABitsLength based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 48),
    )


_ClabMAPDomainRuleEABitsLength_Type.__name__ = "Unsigned32"
_ClabMAPDomainRuleEABitsLength_Object = MibTableColumn
clabMAPDomainRuleEABitsLength = _ClabMAPDomainRuleEABitsLength_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 4, 1, 5, 1, 10),
    _ClabMAPDomainRuleEABitsLength_Type()
)
clabMAPDomainRuleEABitsLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabMAPDomainRuleEABitsLength.setStatus("current")


class _ClabMAPDomainRuleIsFMR_Type(TruthValue):
    """Custom type clabMAPDomainRuleIsFMR based on TruthValue"""
    defaultValue = 2


_ClabMAPDomainRuleIsFMR_Type.__name__ = "TruthValue"
_ClabMAPDomainRuleIsFMR_Object = MibTableColumn
clabMAPDomainRuleIsFMR = _ClabMAPDomainRuleIsFMR_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 4, 1, 5, 1, 11),
    _ClabMAPDomainRuleIsFMR_Type()
)
clabMAPDomainRuleIsFMR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabMAPDomainRuleIsFMR.setStatus("current")
_ClabMAPDomainRuleRowStatus_Type = RowStatus
_ClabMAPDomainRuleRowStatus_Object = MibTableColumn
clabMAPDomainRuleRowStatus = _ClabMAPDomainRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 4, 1, 5, 1, 12),
    _ClabMAPDomainRuleRowStatus_Type()
)
clabMAPDomainRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabMAPDomainRuleRowStatus.setStatus("current")
_ClabMAPDomainIfTable_Object = MibTable
clabMAPDomainIfTable = _ClabMAPDomainIfTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 4, 1, 6)
)
if mibBuilder.loadTexts:
    clabMAPDomainIfTable.setStatus("current")
_ClabMAPDomainIfEntry_Object = MibTableRow
clabMAPDomainIfEntry = _ClabMAPDomainIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 4, 1, 6, 1)
)
clabMAPDomainIfEntry.setIndexNames(
    (0, "CLAB-MAP-MIB", "clabMAPDomainIndex"),
    (0, "CLAB-MAP-MIB", "clabMAPDomainIfIndex"),
)
if mibBuilder.loadTexts:
    clabMAPDomainIfEntry.setStatus("current")


class _ClabMAPDomainIfIndex_Type(Unsigned32):
    """Custom type clabMAPDomainIfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_ClabMAPDomainIfIndex_Type.__name__ = "Unsigned32"
_ClabMAPDomainIfIndex_Object = MibTableColumn
clabMAPDomainIfIndex = _ClabMAPDomainIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 4, 1, 6, 1, 1),
    _ClabMAPDomainIfIndex_Type()
)
clabMAPDomainIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clabMAPDomainIfIndex.setStatus("current")


class _ClabMAPDomainIfEnable_Type(TruthValue):
    """Custom type clabMAPDomainIfEnable based on TruthValue"""
    defaultValue = 2


_ClabMAPDomainIfEnable_Type.__name__ = "TruthValue"
_ClabMAPDomainIfEnable_Object = MibTableColumn
clabMAPDomainIfEnable = _ClabMAPDomainIfEnable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 4, 1, 6, 1, 2),
    _ClabMAPDomainIfEnable_Type()
)
clabMAPDomainIfEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabMAPDomainIfEnable.setStatus("current")


class _ClabMAPDomainIfStatus_Type(Integer32):
    """Custom type clabMAPDomainIfStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("unknown", 3),
          ("dormant", 4),
          ("notPresent", 5),
          ("lowerLayerDown", 6),
          ("error", 7))
    )


_ClabMAPDomainIfStatus_Type.__name__ = "Integer32"
_ClabMAPDomainIfStatus_Object = MibTableColumn
clabMAPDomainIfStatus = _ClabMAPDomainIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 4, 1, 6, 1, 3),
    _ClabMAPDomainIfStatus_Type()
)
clabMAPDomainIfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabMAPDomainIfStatus.setStatus("current")
_ClabMAPDomainIfAlias_Type = SnmpAdminString
_ClabMAPDomainIfAlias_Object = MibTableColumn
clabMAPDomainIfAlias = _ClabMAPDomainIfAlias_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 4, 1, 6, 1, 4),
    _ClabMAPDomainIfAlias_Type()
)
clabMAPDomainIfAlias.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabMAPDomainIfAlias.setStatus("current")
_ClabMAPDomainIfName_Type = SnmpAdminString
_ClabMAPDomainIfName_Object = MibTableColumn
clabMAPDomainIfName = _ClabMAPDomainIfName_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 4, 1, 6, 1, 5),
    _ClabMAPDomainIfName_Type()
)
clabMAPDomainIfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabMAPDomainIfName.setStatus("current")
_ClabMAPDomainIfLastChange_Type = Unsigned32
_ClabMAPDomainIfLastChange_Object = MibTableColumn
clabMAPDomainIfLastChange = _ClabMAPDomainIfLastChange_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 4, 1, 6, 1, 6),
    _ClabMAPDomainIfLastChange_Type()
)
clabMAPDomainIfLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabMAPDomainIfLastChange.setStatus("current")
if mibBuilder.loadTexts:
    clabMAPDomainIfLastChange.setUnits("seconds")
_ClabMAPDomainIfLowerLayers_Type = SnmpAdminString
_ClabMAPDomainIfLowerLayers_Object = MibTableColumn
clabMAPDomainIfLowerLayers = _ClabMAPDomainIfLowerLayers_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 4, 1, 6, 1, 7),
    _ClabMAPDomainIfLowerLayers_Type()
)
clabMAPDomainIfLowerLayers.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabMAPDomainIfLowerLayers.setStatus("current")
_ClabMAPDomainIfRowStatus_Type = RowStatus
_ClabMAPDomainIfRowStatus_Object = MibTableColumn
clabMAPDomainIfRowStatus = _ClabMAPDomainIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 4, 1, 6, 1, 8),
    _ClabMAPDomainIfRowStatus_Type()
)
clabMAPDomainIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabMAPDomainIfRowStatus.setStatus("current")
_ClabMAPDomainIfStatsTable_Object = MibTable
clabMAPDomainIfStatsTable = _ClabMAPDomainIfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 4, 1, 7)
)
if mibBuilder.loadTexts:
    clabMAPDomainIfStatsTable.setStatus("current")
_ClabMAPDomainIfStatsEntry_Object = MibTableRow
clabMAPDomainIfStatsEntry = _ClabMAPDomainIfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 4, 1, 7, 1)
)
if mibBuilder.loadTexts:
    clabMAPDomainIfStatsEntry.setStatus("current")
_ClabMAPDomainIfStatsBytesSent_Type = Counter64
_ClabMAPDomainIfStatsBytesSent_Object = MibTableColumn
clabMAPDomainIfStatsBytesSent = _ClabMAPDomainIfStatsBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 4, 1, 7, 1, 1),
    _ClabMAPDomainIfStatsBytesSent_Type()
)
clabMAPDomainIfStatsBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabMAPDomainIfStatsBytesSent.setStatus("current")
if mibBuilder.loadTexts:
    clabMAPDomainIfStatsBytesSent.setUnits("bytes")
_ClabMAPDomainIfStatsBytesRcvd_Type = Counter64
_ClabMAPDomainIfStatsBytesRcvd_Object = MibTableColumn
clabMAPDomainIfStatsBytesRcvd = _ClabMAPDomainIfStatsBytesRcvd_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 4, 1, 7, 1, 2),
    _ClabMAPDomainIfStatsBytesRcvd_Type()
)
clabMAPDomainIfStatsBytesRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabMAPDomainIfStatsBytesRcvd.setStatus("current")
if mibBuilder.loadTexts:
    clabMAPDomainIfStatsBytesRcvd.setUnits("bytes")
_ClabMAPDomainIfStatsPktSent_Type = Counter64
_ClabMAPDomainIfStatsPktSent_Object = MibTableColumn
clabMAPDomainIfStatsPktSent = _ClabMAPDomainIfStatsPktSent_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 4, 1, 7, 1, 3),
    _ClabMAPDomainIfStatsPktSent_Type()
)
clabMAPDomainIfStatsPktSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabMAPDomainIfStatsPktSent.setStatus("current")
if mibBuilder.loadTexts:
    clabMAPDomainIfStatsPktSent.setUnits("packets")
_ClabMAPDomainIfStatsPktRcvd_Type = Counter64
_ClabMAPDomainIfStatsPktRcvd_Object = MibTableColumn
clabMAPDomainIfStatsPktRcvd = _ClabMAPDomainIfStatsPktRcvd_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 4, 1, 7, 1, 4),
    _ClabMAPDomainIfStatsPktRcvd_Type()
)
clabMAPDomainIfStatsPktRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabMAPDomainIfStatsPktRcvd.setStatus("current")
if mibBuilder.loadTexts:
    clabMAPDomainIfStatsPktRcvd.setUnits("packets")
_ClabMAPDomainIfStatsErrorsSent_Type = Counter64
_ClabMAPDomainIfStatsErrorsSent_Object = MibTableColumn
clabMAPDomainIfStatsErrorsSent = _ClabMAPDomainIfStatsErrorsSent_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 4, 1, 7, 1, 5),
    _ClabMAPDomainIfStatsErrorsSent_Type()
)
clabMAPDomainIfStatsErrorsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabMAPDomainIfStatsErrorsSent.setStatus("current")
if mibBuilder.loadTexts:
    clabMAPDomainIfStatsErrorsSent.setUnits("packets")
_ClabMAPDomainIfStatsErrsRcvd_Type = Counter64
_ClabMAPDomainIfStatsErrsRcvd_Object = MibTableColumn
clabMAPDomainIfStatsErrsRcvd = _ClabMAPDomainIfStatsErrsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 4, 1, 7, 1, 6),
    _ClabMAPDomainIfStatsErrsRcvd_Type()
)
clabMAPDomainIfStatsErrsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabMAPDomainIfStatsErrsRcvd.setStatus("current")
if mibBuilder.loadTexts:
    clabMAPDomainIfStatsErrsRcvd.setUnits("packets")
_ClabMAPDomainIfStatsUcastPktSent_Type = Counter64
_ClabMAPDomainIfStatsUcastPktSent_Object = MibTableColumn
clabMAPDomainIfStatsUcastPktSent = _ClabMAPDomainIfStatsUcastPktSent_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 4, 1, 7, 1, 7),
    _ClabMAPDomainIfStatsUcastPktSent_Type()
)
clabMAPDomainIfStatsUcastPktSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabMAPDomainIfStatsUcastPktSent.setStatus("current")
if mibBuilder.loadTexts:
    clabMAPDomainIfStatsUcastPktSent.setUnits("packets")
_ClabMAPDomainIfStatsUcastPktRcvd_Type = Counter64
_ClabMAPDomainIfStatsUcastPktRcvd_Object = MibTableColumn
clabMAPDomainIfStatsUcastPktRcvd = _ClabMAPDomainIfStatsUcastPktRcvd_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 4, 1, 7, 1, 8),
    _ClabMAPDomainIfStatsUcastPktRcvd_Type()
)
clabMAPDomainIfStatsUcastPktRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabMAPDomainIfStatsUcastPktRcvd.setStatus("current")
if mibBuilder.loadTexts:
    clabMAPDomainIfStatsUcastPktRcvd.setUnits("packets")
_ClabMAPDomainIfStatsDcardPktSent_Type = Counter64
_ClabMAPDomainIfStatsDcardPktSent_Object = MibTableColumn
clabMAPDomainIfStatsDcardPktSent = _ClabMAPDomainIfStatsDcardPktSent_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 4, 1, 7, 1, 9),
    _ClabMAPDomainIfStatsDcardPktSent_Type()
)
clabMAPDomainIfStatsDcardPktSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabMAPDomainIfStatsDcardPktSent.setStatus("current")
if mibBuilder.loadTexts:
    clabMAPDomainIfStatsDcardPktSent.setUnits("packets")
_ClabMAPDomainIfStatsDcardPktRcvd_Type = Counter64
_ClabMAPDomainIfStatsDcardPktRcvd_Object = MibTableColumn
clabMAPDomainIfStatsDcardPktRcvd = _ClabMAPDomainIfStatsDcardPktRcvd_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 4, 1, 7, 1, 10),
    _ClabMAPDomainIfStatsDcardPktRcvd_Type()
)
clabMAPDomainIfStatsDcardPktRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabMAPDomainIfStatsDcardPktRcvd.setStatus("current")
if mibBuilder.loadTexts:
    clabMAPDomainIfStatsDcardPktRcvd.setUnits("packets")
_ClabMAPDomainIfStatsMcastPktSent_Type = Counter64
_ClabMAPDomainIfStatsMcastPktSent_Object = MibTableColumn
clabMAPDomainIfStatsMcastPktSent = _ClabMAPDomainIfStatsMcastPktSent_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 4, 1, 7, 1, 11),
    _ClabMAPDomainIfStatsMcastPktSent_Type()
)
clabMAPDomainIfStatsMcastPktSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabMAPDomainIfStatsMcastPktSent.setStatus("current")
if mibBuilder.loadTexts:
    clabMAPDomainIfStatsMcastPktSent.setUnits("packets")
_ClabMAPDomainIfStatsMcastPktRcvd_Type = Counter64
_ClabMAPDomainIfStatsMcastPktRcvd_Object = MibTableColumn
clabMAPDomainIfStatsMcastPktRcvd = _ClabMAPDomainIfStatsMcastPktRcvd_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 4, 1, 7, 1, 12),
    _ClabMAPDomainIfStatsMcastPktRcvd_Type()
)
clabMAPDomainIfStatsMcastPktRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabMAPDomainIfStatsMcastPktRcvd.setStatus("current")
if mibBuilder.loadTexts:
    clabMAPDomainIfStatsMcastPktRcvd.setUnits("packets")
_ClabMAPDomainIfStatsBcastPktSent_Type = Counter64
_ClabMAPDomainIfStatsBcastPktSent_Object = MibTableColumn
clabMAPDomainIfStatsBcastPktSent = _ClabMAPDomainIfStatsBcastPktSent_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 4, 1, 7, 1, 13),
    _ClabMAPDomainIfStatsBcastPktSent_Type()
)
clabMAPDomainIfStatsBcastPktSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabMAPDomainIfStatsBcastPktSent.setStatus("current")
if mibBuilder.loadTexts:
    clabMAPDomainIfStatsBcastPktSent.setUnits("packets")
_ClabMAPDomainIfStatsBcastPktRcvd_Type = Counter64
_ClabMAPDomainIfStatsBcastPktRcvd_Object = MibTableColumn
clabMAPDomainIfStatsBcastPktRcvd = _ClabMAPDomainIfStatsBcastPktRcvd_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 4, 1, 7, 1, 14),
    _ClabMAPDomainIfStatsBcastPktRcvd_Type()
)
clabMAPDomainIfStatsBcastPktRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabMAPDomainIfStatsBcastPktRcvd.setStatus("current")
if mibBuilder.loadTexts:
    clabMAPDomainIfStatsBcastPktRcvd.setUnits("packets")
_ClabMAPDomainIfStatsUkwnProtoPkt_Type = Counter64
_ClabMAPDomainIfStatsUkwnProtoPkt_Object = MibTableColumn
clabMAPDomainIfStatsUkwnProtoPkt = _ClabMAPDomainIfStatsUkwnProtoPkt_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 4, 1, 7, 1, 15),
    _ClabMAPDomainIfStatsUkwnProtoPkt_Type()
)
clabMAPDomainIfStatsUkwnProtoPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabMAPDomainIfStatsUkwnProtoPkt.setStatus("current")
if mibBuilder.loadTexts:
    clabMAPDomainIfStatsUkwnProtoPkt.setUnits("packets")
_ClabMAPDomainIfStatsInvV4Pkts_Type = Counter64
_ClabMAPDomainIfStatsInvV4Pkts_Object = MibTableColumn
clabMAPDomainIfStatsInvV4Pkts = _ClabMAPDomainIfStatsInvV4Pkts_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 4, 1, 7, 1, 16),
    _ClabMAPDomainIfStatsInvV4Pkts_Type()
)
clabMAPDomainIfStatsInvV4Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabMAPDomainIfStatsInvV4Pkts.setStatus("current")
if mibBuilder.loadTexts:
    clabMAPDomainIfStatsInvV4Pkts.setUnits("packets")
_ClabMAPMibConformance_ObjectIdentity = ObjectIdentity
clabMAPMibConformance = _ClabMAPMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 4, 4, 2)
)
_ClabMAPMibCompliances_ObjectIdentity = ObjectIdentity
clabMAPMibCompliances = _ClabMAPMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 4, 4, 2, 1)
)
_ClabMAPMibGroups_ObjectIdentity = ObjectIdentity
clabMAPMibGroups = _ClabMAPMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 4, 4, 2, 2)
)
clabMAPDomainIfEntry.registerAugmentions(
    ("CLAB-MAP-MIB",
     "clabMAPDomainIfStatsEntry")
)
clabMAPDomainIfStatsEntry.setIndexNames(*clabMAPDomainIfEntry.getIndexNames())

# Managed Objects groups

clabMAPGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 4, 4, 2, 2, 1)
)
clabMAPGroup.setObjects(
      *(("CLAB-MAP-MIB", "clabMAPEnable"),
        ("CLAB-MAP-MIB", "clabMAPTunnelDomainNumEntries"),
        ("CLAB-MAP-MIB", "clabMAPDomainRuleNumEntries"),
        ("CLAB-MAP-MIB", "clabMAPDomainEnable"),
        ("CLAB-MAP-MIB", "clabMAPDomainStatus"),
        ("CLAB-MAP-MIB", "clabMAPDomainAlias"),
        ("CLAB-MAP-MIB", "clabMAPDomainTransportMode"),
        ("CLAB-MAP-MIB", "clabMAPDomainWANInterface"),
        ("CLAB-MAP-MIB", "clabMAPDomainIPv6Prefix"),
        ("CLAB-MAP-MIB", "clabMAPDomainIPv6PrefixLen"),
        ("CLAB-MAP-MIB", "clabMAPDomainBRIPv6Prefix"),
        ("CLAB-MAP-MIB", "clabMAPDomainBRIPv6PrefixLen"),
        ("CLAB-MAP-MIB", "clabMAPDomainDSCPMarkPolicy"),
        ("CLAB-MAP-MIB", "clabMAPDomainPSIDOffset"),
        ("CLAB-MAP-MIB", "clabMAPDomainPSIDLength"),
        ("CLAB-MAP-MIB", "clabMAPDomainPSID"),
        ("CLAB-MAP-MIB", "clabMAPDomainIncludeSystemPorts"),
        ("CLAB-MAP-MIB", "clabMAPDomainRowStatus"),
        ("CLAB-MAP-MIB", "clabMAPDomainRuleEnable"),
        ("CLAB-MAP-MIB", "clabMAPDomainRuleStatus"),
        ("CLAB-MAP-MIB", "clabMAPDomainRuleAlias"),
        ("CLAB-MAP-MIB", "clabMAPDomainRuleOrigin"),
        ("CLAB-MAP-MIB", "clabMAPDomainRuleIPv6Prefix"),
        ("CLAB-MAP-MIB", "clabMAPDomainRuleIPv6PrefixLen"),
        ("CLAB-MAP-MIB", "clabMAPDomainRuleIPv4Prefix"),
        ("CLAB-MAP-MIB", "clabMAPDomainRuleIPv4PrefixLen"),
        ("CLAB-MAP-MIB", "clabMAPDomainRuleEABitsLength"),
        ("CLAB-MAP-MIB", "clabMAPDomainRuleIsFMR"),
        ("CLAB-MAP-MIB", "clabMAPDomainRuleRowStatus"),
        ("CLAB-MAP-MIB", "clabMAPDomainIfEnable"),
        ("CLAB-MAP-MIB", "clabMAPDomainIfStatus"),
        ("CLAB-MAP-MIB", "clabMAPDomainIfAlias"),
        ("CLAB-MAP-MIB", "clabMAPDomainIfName"),
        ("CLAB-MAP-MIB", "clabMAPDomainIfLastChange"),
        ("CLAB-MAP-MIB", "clabMAPDomainIfLowerLayers"),
        ("CLAB-MAP-MIB", "clabMAPDomainIfRowStatus"),
        ("CLAB-MAP-MIB", "clabMAPDomainIfStatsBytesSent"),
        ("CLAB-MAP-MIB", "clabMAPDomainIfStatsBytesRcvd"),
        ("CLAB-MAP-MIB", "clabMAPDomainIfStatsPktSent"),
        ("CLAB-MAP-MIB", "clabMAPDomainIfStatsPktRcvd"),
        ("CLAB-MAP-MIB", "clabMAPDomainIfStatsErrorsSent"),
        ("CLAB-MAP-MIB", "clabMAPDomainIfStatsErrsRcvd"),
        ("CLAB-MAP-MIB", "clabMAPDomainIfStatsUcastPktSent"),
        ("CLAB-MAP-MIB", "clabMAPDomainIfStatsUcastPktRcvd"),
        ("CLAB-MAP-MIB", "clabMAPDomainIfStatsDcardPktSent"),
        ("CLAB-MAP-MIB", "clabMAPDomainIfStatsDcardPktRcvd"),
        ("CLAB-MAP-MIB", "clabMAPDomainIfStatsMcastPktSent"),
        ("CLAB-MAP-MIB", "clabMAPDomainIfStatsMcastPktRcvd"),
        ("CLAB-MAP-MIB", "clabMAPDomainIfStatsBcastPktSent"),
        ("CLAB-MAP-MIB", "clabMAPDomainIfStatsBcastPktRcvd"),
        ("CLAB-MAP-MIB", "clabMAPDomainIfStatsUkwnProtoPkt"),
        ("CLAB-MAP-MIB", "clabMAPDomainIfStatsInvV4Pkts"))
)
if mibBuilder.loadTexts:
    clabMAPGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

clabMAPCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4491, 4, 4, 2, 1, 1)
)
clabMAPCompliance.setObjects(
    ("CLAB-MAP-MIB", "clabMAPGroup")
)
if mibBuilder.loadTexts:
    clabMAPCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CLAB-MAP-MIB",
    **{"clabMAPMib": clabMAPMib,
       "clabMAPNotifications": clabMAPNotifications,
       "clabMAPObjects": clabMAPObjects,
       "clabMAPEnable": clabMAPEnable,
       "clabMAPTunnelDomainNumEntries": clabMAPTunnelDomainNumEntries,
       "clabMAPDomainRuleNumEntries": clabMAPDomainRuleNumEntries,
       "clabMAPDomainTable": clabMAPDomainTable,
       "clabMAPDomainEntry": clabMAPDomainEntry,
       "clabMAPDomainIndex": clabMAPDomainIndex,
       "clabMAPDomainEnable": clabMAPDomainEnable,
       "clabMAPDomainStatus": clabMAPDomainStatus,
       "clabMAPDomainAlias": clabMAPDomainAlias,
       "clabMAPDomainTransportMode": clabMAPDomainTransportMode,
       "clabMAPDomainWANInterface": clabMAPDomainWANInterface,
       "clabMAPDomainIPv6Prefix": clabMAPDomainIPv6Prefix,
       "clabMAPDomainIPv6PrefixLen": clabMAPDomainIPv6PrefixLen,
       "clabMAPDomainBRIPv6Prefix": clabMAPDomainBRIPv6Prefix,
       "clabMAPDomainBRIPv6PrefixLen": clabMAPDomainBRIPv6PrefixLen,
       "clabMAPDomainDSCPMarkPolicy": clabMAPDomainDSCPMarkPolicy,
       "clabMAPDomainPSIDOffset": clabMAPDomainPSIDOffset,
       "clabMAPDomainPSIDLength": clabMAPDomainPSIDLength,
       "clabMAPDomainPSID": clabMAPDomainPSID,
       "clabMAPDomainIncludeSystemPorts": clabMAPDomainIncludeSystemPorts,
       "clabMAPDomainRowStatus": clabMAPDomainRowStatus,
       "clabMAPDomainRuleTable": clabMAPDomainRuleTable,
       "clabMAPDomainRuleEntry": clabMAPDomainRuleEntry,
       "clabMAPDomainRuleIndex": clabMAPDomainRuleIndex,
       "clabMAPDomainRuleEnable": clabMAPDomainRuleEnable,
       "clabMAPDomainRuleStatus": clabMAPDomainRuleStatus,
       "clabMAPDomainRuleAlias": clabMAPDomainRuleAlias,
       "clabMAPDomainRuleOrigin": clabMAPDomainRuleOrigin,
       "clabMAPDomainRuleIPv6Prefix": clabMAPDomainRuleIPv6Prefix,
       "clabMAPDomainRuleIPv6PrefixLen": clabMAPDomainRuleIPv6PrefixLen,
       "clabMAPDomainRuleIPv4Prefix": clabMAPDomainRuleIPv4Prefix,
       "clabMAPDomainRuleIPv4PrefixLen": clabMAPDomainRuleIPv4PrefixLen,
       "clabMAPDomainRuleEABitsLength": clabMAPDomainRuleEABitsLength,
       "clabMAPDomainRuleIsFMR": clabMAPDomainRuleIsFMR,
       "clabMAPDomainRuleRowStatus": clabMAPDomainRuleRowStatus,
       "clabMAPDomainIfTable": clabMAPDomainIfTable,
       "clabMAPDomainIfEntry": clabMAPDomainIfEntry,
       "clabMAPDomainIfIndex": clabMAPDomainIfIndex,
       "clabMAPDomainIfEnable": clabMAPDomainIfEnable,
       "clabMAPDomainIfStatus": clabMAPDomainIfStatus,
       "clabMAPDomainIfAlias": clabMAPDomainIfAlias,
       "clabMAPDomainIfName": clabMAPDomainIfName,
       "clabMAPDomainIfLastChange": clabMAPDomainIfLastChange,
       "clabMAPDomainIfLowerLayers": clabMAPDomainIfLowerLayers,
       "clabMAPDomainIfRowStatus": clabMAPDomainIfRowStatus,
       "clabMAPDomainIfStatsTable": clabMAPDomainIfStatsTable,
       "clabMAPDomainIfStatsEntry": clabMAPDomainIfStatsEntry,
       "clabMAPDomainIfStatsBytesSent": clabMAPDomainIfStatsBytesSent,
       "clabMAPDomainIfStatsBytesRcvd": clabMAPDomainIfStatsBytesRcvd,
       "clabMAPDomainIfStatsPktSent": clabMAPDomainIfStatsPktSent,
       "clabMAPDomainIfStatsPktRcvd": clabMAPDomainIfStatsPktRcvd,
       "clabMAPDomainIfStatsErrorsSent": clabMAPDomainIfStatsErrorsSent,
       "clabMAPDomainIfStatsErrsRcvd": clabMAPDomainIfStatsErrsRcvd,
       "clabMAPDomainIfStatsUcastPktSent": clabMAPDomainIfStatsUcastPktSent,
       "clabMAPDomainIfStatsUcastPktRcvd": clabMAPDomainIfStatsUcastPktRcvd,
       "clabMAPDomainIfStatsDcardPktSent": clabMAPDomainIfStatsDcardPktSent,
       "clabMAPDomainIfStatsDcardPktRcvd": clabMAPDomainIfStatsDcardPktRcvd,
       "clabMAPDomainIfStatsMcastPktSent": clabMAPDomainIfStatsMcastPktSent,
       "clabMAPDomainIfStatsMcastPktRcvd": clabMAPDomainIfStatsMcastPktRcvd,
       "clabMAPDomainIfStatsBcastPktSent": clabMAPDomainIfStatsBcastPktSent,
       "clabMAPDomainIfStatsBcastPktRcvd": clabMAPDomainIfStatsBcastPktRcvd,
       "clabMAPDomainIfStatsUkwnProtoPkt": clabMAPDomainIfStatsUkwnProtoPkt,
       "clabMAPDomainIfStatsInvV4Pkts": clabMAPDomainIfStatsInvV4Pkts,
       "clabMAPMibConformance": clabMAPMibConformance,
       "clabMAPMibCompliances": clabMAPMibCompliances,
       "clabMAPCompliance": clabMAPCompliance,
       "clabMAPMibGroups": clabMAPMibGroups,
       "clabMAPGroup": clabMAPGroup}
)
