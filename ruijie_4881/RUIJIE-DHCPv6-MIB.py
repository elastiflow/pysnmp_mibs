# SNMP MIB module (RUIJIE-DHCPv6-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-DHCPV6-MIB.mib
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

(InetAddressIPv6,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv6")

(Ipv6Address,
 Ipv6AddressPrefix) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address",
    "Ipv6AddressPrefix")

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
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeInterval) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval")


# MODULE-IDENTITY

ruijieDhcpv6MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 45)
)
if mibBuilder.loadTexts:
    ruijieDhcpv6MIB.setRevisions(
        ("2009-03-16 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieDhcpv6MIBObjects_ObjectIdentity = ObjectIdentity
ruijieDhcpv6MIBObjects = _RuijieDhcpv6MIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 45, 1)
)
if mibBuilder.loadTexts:
    ruijieDhcpv6MIBObjects.setStatus("current")
_RuijieDhcpv6ServerMIBObjects_ObjectIdentity = ObjectIdentity
ruijieDhcpv6ServerMIBObjects = _RuijieDhcpv6ServerMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 45, 1, 1)
)
if mibBuilder.loadTexts:
    ruijieDhcpv6ServerMIBObjects.setStatus("current")
_RuijieDhcpv6ServerCounters_ObjectIdentity = ObjectIdentity
ruijieDhcpv6ServerCounters = _RuijieDhcpv6ServerCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 45, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ruijieDhcpv6ServerCounters.setStatus("current")
_RuijieDhcpv6ServerHCountSolicits_Type = Counter64
_RuijieDhcpv6ServerHCountSolicits_Object = MibScalar
ruijieDhcpv6ServerHCountSolicits = _RuijieDhcpv6ServerHCountSolicits_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 45, 1, 1, 1, 1),
    _RuijieDhcpv6ServerHCountSolicits_Type()
)
ruijieDhcpv6ServerHCountSolicits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDhcpv6ServerHCountSolicits.setStatus("current")
_RuijieDhcpv6ServerHCountRequests_Type = Counter64
_RuijieDhcpv6ServerHCountRequests_Object = MibScalar
ruijieDhcpv6ServerHCountRequests = _RuijieDhcpv6ServerHCountRequests_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 45, 1, 1, 1, 2),
    _RuijieDhcpv6ServerHCountRequests_Type()
)
ruijieDhcpv6ServerHCountRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDhcpv6ServerHCountRequests.setStatus("current")
_RuijieDhcpv6ServerHCountRenews_Type = Counter64
_RuijieDhcpv6ServerHCountRenews_Object = MibScalar
ruijieDhcpv6ServerHCountRenews = _RuijieDhcpv6ServerHCountRenews_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 45, 1, 1, 1, 3),
    _RuijieDhcpv6ServerHCountRenews_Type()
)
ruijieDhcpv6ServerHCountRenews.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDhcpv6ServerHCountRenews.setStatus("current")
_RuijieDhcpv6ServerHCountDeclines_Type = Counter64
_RuijieDhcpv6ServerHCountDeclines_Object = MibScalar
ruijieDhcpv6ServerHCountDeclines = _RuijieDhcpv6ServerHCountDeclines_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 45, 1, 1, 1, 4),
    _RuijieDhcpv6ServerHCountDeclines_Type()
)
ruijieDhcpv6ServerHCountDeclines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDhcpv6ServerHCountDeclines.setStatus("current")
_RuijieDhcpv6ServerHCountReleases_Type = Counter64
_RuijieDhcpv6ServerHCountReleases_Object = MibScalar
ruijieDhcpv6ServerHCountReleases = _RuijieDhcpv6ServerHCountReleases_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 45, 1, 1, 1, 5),
    _RuijieDhcpv6ServerHCountReleases_Type()
)
ruijieDhcpv6ServerHCountReleases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDhcpv6ServerHCountReleases.setStatus("current")
_RuijieDhcpv6ServerHCountInforms_Type = Counter64
_RuijieDhcpv6ServerHCountInforms_Object = MibScalar
ruijieDhcpv6ServerHCountInforms = _RuijieDhcpv6ServerHCountInforms_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 45, 1, 1, 1, 6),
    _RuijieDhcpv6ServerHCountInforms_Type()
)
ruijieDhcpv6ServerHCountInforms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDhcpv6ServerHCountInforms.setStatus("current")
_RuijieDhcpv6ServerHCountConfirms_Type = Counter64
_RuijieDhcpv6ServerHCountConfirms_Object = MibScalar
ruijieDhcpv6ServerHCountConfirms = _RuijieDhcpv6ServerHCountConfirms_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 45, 1, 1, 1, 7),
    _RuijieDhcpv6ServerHCountConfirms_Type()
)
ruijieDhcpv6ServerHCountConfirms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDhcpv6ServerHCountConfirms.setStatus("current")
_RuijieDhcpv6ServerHCountRebinds_Type = Counter64
_RuijieDhcpv6ServerHCountRebinds_Object = MibScalar
ruijieDhcpv6ServerHCountRebinds = _RuijieDhcpv6ServerHCountRebinds_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 45, 1, 1, 1, 8),
    _RuijieDhcpv6ServerHCountRebinds_Type()
)
ruijieDhcpv6ServerHCountRebinds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDhcpv6ServerHCountRebinds.setStatus("current")
_RuijieDhcpv6ServerHCountAdvertises_Type = Counter64
_RuijieDhcpv6ServerHCountAdvertises_Object = MibScalar
ruijieDhcpv6ServerHCountAdvertises = _RuijieDhcpv6ServerHCountAdvertises_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 45, 1, 1, 1, 9),
    _RuijieDhcpv6ServerHCountAdvertises_Type()
)
ruijieDhcpv6ServerHCountAdvertises.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDhcpv6ServerHCountAdvertises.setStatus("current")
_RuijieDhcpv6ServerHCountSuccReplies_Type = Counter64
_RuijieDhcpv6ServerHCountSuccReplies_Object = MibScalar
ruijieDhcpv6ServerHCountSuccReplies = _RuijieDhcpv6ServerHCountSuccReplies_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 45, 1, 1, 1, 10),
    _RuijieDhcpv6ServerHCountSuccReplies_Type()
)
ruijieDhcpv6ServerHCountSuccReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDhcpv6ServerHCountSuccReplies.setStatus("current")
_RuijieDhcpv6ServerHCountFailReplies_Type = Counter64
_RuijieDhcpv6ServerHCountFailReplies_Object = MibScalar
ruijieDhcpv6ServerHCountFailReplies = _RuijieDhcpv6ServerHCountFailReplies_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 45, 1, 1, 1, 11),
    _RuijieDhcpv6ServerHCountFailReplies_Type()
)
ruijieDhcpv6ServerHCountFailReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDhcpv6ServerHCountFailReplies.setStatus("current")
_RuijieDhcpv6ServerHCountInPkts_Type = Counter64
_RuijieDhcpv6ServerHCountInPkts_Object = MibScalar
ruijieDhcpv6ServerHCountInPkts = _RuijieDhcpv6ServerHCountInPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 45, 1, 1, 1, 12),
    _RuijieDhcpv6ServerHCountInPkts_Type()
)
ruijieDhcpv6ServerHCountInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDhcpv6ServerHCountInPkts.setStatus("current")
_RuijieDhcpv6ServerHCountOutPkts_Type = Counter64
_RuijieDhcpv6ServerHCountOutPkts_Object = MibScalar
ruijieDhcpv6ServerHCountOutPkts = _RuijieDhcpv6ServerHCountOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 45, 1, 1, 1, 13),
    _RuijieDhcpv6ServerHCountOutPkts_Type()
)
ruijieDhcpv6ServerHCountOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDhcpv6ServerHCountOutPkts.setStatus("current")
_RuijieDhcpv6ServerHCountDroppedUnknown_Type = Counter64
_RuijieDhcpv6ServerHCountDroppedUnknown_Object = MibScalar
ruijieDhcpv6ServerHCountDroppedUnknown = _RuijieDhcpv6ServerHCountDroppedUnknown_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 45, 1, 1, 1, 14),
    _RuijieDhcpv6ServerHCountDroppedUnknown_Type()
)
ruijieDhcpv6ServerHCountDroppedUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDhcpv6ServerHCountDroppedUnknown.setStatus("current")
_RuijieDhcpv6ServerHCountDroppedError_Type = Counter64
_RuijieDhcpv6ServerHCountDroppedError_Object = MibScalar
ruijieDhcpv6ServerHCountDroppedError = _RuijieDhcpv6ServerHCountDroppedError_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 45, 1, 1, 1, 15),
    _RuijieDhcpv6ServerHCountDroppedError_Type()
)
ruijieDhcpv6ServerHCountDroppedError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDhcpv6ServerHCountDroppedError.setStatus("current")
_RuijieDhcpv6ServerHCountRelayforward_Type = Counter64
_RuijieDhcpv6ServerHCountRelayforward_Object = MibScalar
ruijieDhcpv6ServerHCountRelayforward = _RuijieDhcpv6ServerHCountRelayforward_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 45, 1, 1, 1, 16),
    _RuijieDhcpv6ServerHCountRelayforward_Type()
)
ruijieDhcpv6ServerHCountRelayforward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDhcpv6ServerHCountRelayforward.setStatus("current")
_RuijieDhcpv6ServerHCountRelayreply_Type = Counter64
_RuijieDhcpv6ServerHCountRelayreply_Object = MibScalar
ruijieDhcpv6ServerHCountRelayreply = _RuijieDhcpv6ServerHCountRelayreply_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 45, 1, 1, 1, 17),
    _RuijieDhcpv6ServerHCountRelayreply_Type()
)
ruijieDhcpv6ServerHCountRelayreply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDhcpv6ServerHCountRelayreply.setStatus("current")
_RuijieDhcpv6ServerHCountReqtimes_Type = Counter64
_RuijieDhcpv6ServerHCountReqtimes_Object = MibScalar
ruijieDhcpv6ServerHCountReqtimes = _RuijieDhcpv6ServerHCountReqtimes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 45, 1, 1, 1, 18),
    _RuijieDhcpv6ServerHCountReqtimes_Type()
)
ruijieDhcpv6ServerHCountReqtimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDhcpv6ServerHCountReqtimes.setStatus("current")
_RuijieDhcpv6ServerHCountReqSuctimes_Type = Counter64
_RuijieDhcpv6ServerHCountReqSuctimes_Object = MibScalar
ruijieDhcpv6ServerHCountReqSuctimes = _RuijieDhcpv6ServerHCountReqSuctimes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 45, 1, 1, 1, 19),
    _RuijieDhcpv6ServerHCountReqSuctimes_Type()
)
ruijieDhcpv6ServerHCountReqSuctimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDhcpv6ServerHCountReqSuctimes.setStatus("current")
_RuijieDhcpv6ServerConfiguration_ObjectIdentity = ObjectIdentity
ruijieDhcpv6ServerConfiguration = _RuijieDhcpv6ServerConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 45, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ruijieDhcpv6ServerConfiguration.setStatus("current")
_RuijieDhcpv6ServerNumBindings_Type = Counter32
_RuijieDhcpv6ServerNumBindings_Object = MibScalar
ruijieDhcpv6ServerNumBindings = _RuijieDhcpv6ServerNumBindings_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 45, 1, 1, 2, 1),
    _RuijieDhcpv6ServerNumBindings_Type()
)
ruijieDhcpv6ServerNumBindings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDhcpv6ServerNumBindings.setStatus("current")
_RuijieDhcpv6ServerBindingsTable_Object = MibTable
ruijieDhcpv6ServerBindingsTable = _RuijieDhcpv6ServerBindingsTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 45, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    ruijieDhcpv6ServerBindingsTable.setStatus("current")
_RuijieDhcpv6ServerBindingsEntry_Object = MibTableRow
ruijieDhcpv6ServerBindingsEntry = _RuijieDhcpv6ServerBindingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 45, 1, 1, 2, 2, 1)
)
ruijieDhcpv6ServerBindingsEntry.setIndexNames(
    (0, "RUIJIE-DHCPv6-MIB", "ruijieDhcpv6ServerBindingsPoolName"),
    (0, "RUIJIE-DHCPv6-MIB", "ruijieDhcpv6ServerBindingsClientDuid"),
    (0, "RUIJIE-DHCPv6-MIB", "ruijieDhcpv6ServerBindingsIaType"),
    (0, "RUIJIE-DHCPv6-MIB", "ruijieDhcpv6ServerBindingsIaId"),
)
if mibBuilder.loadTexts:
    ruijieDhcpv6ServerBindingsEntry.setStatus("current")


class _RuijieDhcpv6ServerBindingsPoolName_Type(DisplayString):
    """Custom type ruijieDhcpv6ServerBindingsPoolName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuijieDhcpv6ServerBindingsPoolName_Type.__name__ = "DisplayString"
_RuijieDhcpv6ServerBindingsPoolName_Object = MibTableColumn
ruijieDhcpv6ServerBindingsPoolName = _RuijieDhcpv6ServerBindingsPoolName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 45, 1, 1, 2, 2, 1, 1),
    _RuijieDhcpv6ServerBindingsPoolName_Type()
)
ruijieDhcpv6ServerBindingsPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDhcpv6ServerBindingsPoolName.setStatus("current")


class _RuijieDhcpv6ServerBindingsClientDuid_Type(OctetString):
    """Custom type ruijieDhcpv6ServerBindingsClientDuid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 130),
    )


_RuijieDhcpv6ServerBindingsClientDuid_Type.__name__ = "OctetString"
_RuijieDhcpv6ServerBindingsClientDuid_Object = MibTableColumn
ruijieDhcpv6ServerBindingsClientDuid = _RuijieDhcpv6ServerBindingsClientDuid_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 45, 1, 1, 2, 2, 1, 2),
    _RuijieDhcpv6ServerBindingsClientDuid_Type()
)
ruijieDhcpv6ServerBindingsClientDuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDhcpv6ServerBindingsClientDuid.setStatus("current")


class _RuijieDhcpv6ServerBindingsIaType_Type(Integer32):
    """Custom type ruijieDhcpv6ServerBindingsIaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("iana", 1),
          ("iata", 2),
          ("iapd", 3))
    )


_RuijieDhcpv6ServerBindingsIaType_Type.__name__ = "Integer32"
_RuijieDhcpv6ServerBindingsIaType_Object = MibTableColumn
ruijieDhcpv6ServerBindingsIaType = _RuijieDhcpv6ServerBindingsIaType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 45, 1, 1, 2, 2, 1, 3),
    _RuijieDhcpv6ServerBindingsIaType_Type()
)
ruijieDhcpv6ServerBindingsIaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDhcpv6ServerBindingsIaType.setStatus("current")
_RuijieDhcpv6ServerBindingsIaId_Type = Unsigned32
_RuijieDhcpv6ServerBindingsIaId_Object = MibTableColumn
ruijieDhcpv6ServerBindingsIaId = _RuijieDhcpv6ServerBindingsIaId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 45, 1, 1, 2, 2, 1, 4),
    _RuijieDhcpv6ServerBindingsIaId_Type()
)
ruijieDhcpv6ServerBindingsIaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDhcpv6ServerBindingsIaId.setStatus("current")
_RuijieDhcpv6ServerBindingsAddress_Type = Ipv6Address
_RuijieDhcpv6ServerBindingsAddress_Object = MibTableColumn
ruijieDhcpv6ServerBindingsAddress = _RuijieDhcpv6ServerBindingsAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 45, 1, 1, 2, 2, 1, 5),
    _RuijieDhcpv6ServerBindingsAddress_Type()
)
ruijieDhcpv6ServerBindingsAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDhcpv6ServerBindingsAddress.setStatus("current")
_RuijieDhcpv6ServerBindingsPrefix_Type = Ipv6AddressPrefix
_RuijieDhcpv6ServerBindingsPrefix_Object = MibTableColumn
ruijieDhcpv6ServerBindingsPrefix = _RuijieDhcpv6ServerBindingsPrefix_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 45, 1, 1, 2, 2, 1, 6),
    _RuijieDhcpv6ServerBindingsPrefix_Type()
)
ruijieDhcpv6ServerBindingsPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDhcpv6ServerBindingsPrefix.setStatus("current")


class _RuijieDhcpv6ServerBindingsPrefixLength_Type(Integer32):
    """Custom type ruijieDhcpv6ServerBindingsPrefixLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_RuijieDhcpv6ServerBindingsPrefixLength_Type.__name__ = "Integer32"
_RuijieDhcpv6ServerBindingsPrefixLength_Object = MibTableColumn
ruijieDhcpv6ServerBindingsPrefixLength = _RuijieDhcpv6ServerBindingsPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 45, 1, 1, 2, 2, 1, 7),
    _RuijieDhcpv6ServerBindingsPrefixLength_Type()
)
ruijieDhcpv6ServerBindingsPrefixLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDhcpv6ServerBindingsPrefixLength.setStatus("current")
_RuijieDhcpv6ServerBindingsDuration_Type = Unsigned32
_RuijieDhcpv6ServerBindingsDuration_Object = MibTableColumn
ruijieDhcpv6ServerBindingsDuration = _RuijieDhcpv6ServerBindingsDuration_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 45, 1, 1, 2, 2, 1, 8),
    _RuijieDhcpv6ServerBindingsDuration_Type()
)
ruijieDhcpv6ServerBindingsDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDhcpv6ServerBindingsDuration.setStatus("current")
_RuijieDhcpv6ServerBindingsIfIndex_Type = InterfaceIndex
_RuijieDhcpv6ServerBindingsIfIndex_Object = MibTableColumn
ruijieDhcpv6ServerBindingsIfIndex = _RuijieDhcpv6ServerBindingsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 45, 1, 1, 2, 2, 1, 9),
    _RuijieDhcpv6ServerBindingsIfIndex_Type()
)
ruijieDhcpv6ServerBindingsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDhcpv6ServerBindingsIfIndex.setStatus("current")
_RuijieDhcpv6ServerPoolUsageTable_Object = MibTable
ruijieDhcpv6ServerPoolUsageTable = _RuijieDhcpv6ServerPoolUsageTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 45, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    ruijieDhcpv6ServerPoolUsageTable.setStatus("current")
_RuijieDhcpv6ServerPoolEntry_Object = MibTableRow
ruijieDhcpv6ServerPoolEntry = _RuijieDhcpv6ServerPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 45, 1, 1, 2, 3, 1)
)
ruijieDhcpv6ServerPoolEntry.setIndexNames(
    (0, "RUIJIE-DHCPv6-MIB", "ruijieIPv6PoolUsageIndex"),
)
if mibBuilder.loadTexts:
    ruijieDhcpv6ServerPoolEntry.setStatus("current")
_RuijieIPv6PoolUsageIndex_Type = Unsigned32
_RuijieIPv6PoolUsageIndex_Object = MibTableColumn
ruijieIPv6PoolUsageIndex = _RuijieIPv6PoolUsageIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 45, 1, 1, 2, 3, 1, 1),
    _RuijieIPv6PoolUsageIndex_Type()
)
ruijieIPv6PoolUsageIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPv6PoolUsageIndex.setStatus("current")


class _RuijieIPv6PoolUsageName_Type(DisplayString):
    """Custom type ruijieIPv6PoolUsageName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuijieIPv6PoolUsageName_Type.__name__ = "DisplayString"
_RuijieIPv6PoolUsageName_Object = MibTableColumn
ruijieIPv6PoolUsageName = _RuijieIPv6PoolUsageName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 45, 1, 1, 2, 3, 1, 2),
    _RuijieIPv6PoolUsageName_Type()
)
ruijieIPv6PoolUsageName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieIPv6PoolUsageName.setStatus("current")
_RuijieIPv6DHCPIPPoolUsage_Type = Unsigned32
_RuijieIPv6DHCPIPPoolUsage_Object = MibTableColumn
ruijieIPv6DHCPIPPoolUsage = _RuijieIPv6DHCPIPPoolUsage_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 45, 1, 1, 2, 3, 1, 3),
    _RuijieIPv6DHCPIPPoolUsage_Type()
)
ruijieIPv6DHCPIPPoolUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPv6DHCPIPPoolUsage.setStatus("current")
_RuijieIPv6PoolUsageRawStatus_Type = RowStatus
_RuijieIPv6PoolUsageRawStatus_Object = MibTableColumn
ruijieIPv6PoolUsageRawStatus = _RuijieIPv6PoolUsageRawStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 45, 1, 1, 2, 3, 1, 4),
    _RuijieIPv6PoolUsageRawStatus_Type()
)
ruijieIPv6PoolUsageRawStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieIPv6PoolUsageRawStatus.setStatus("current")
_RuijieDhcpv6ServerPoolConfigTable_Object = MibTable
ruijieDhcpv6ServerPoolConfigTable = _RuijieDhcpv6ServerPoolConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 45, 1, 1, 2, 4)
)
if mibBuilder.loadTexts:
    ruijieDhcpv6ServerPoolConfigTable.setStatus("current")
_RuijieDhcpv6ServerPoolCfgEntry_Object = MibTableRow
ruijieDhcpv6ServerPoolCfgEntry = _RuijieDhcpv6ServerPoolCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 45, 1, 1, 2, 4, 1)
)
ruijieDhcpv6ServerPoolCfgEntry.setIndexNames(
    (0, "RUIJIE-DHCPv6-MIB", "ruijieIPv6PoolCfgIndex"),
)
if mibBuilder.loadTexts:
    ruijieDhcpv6ServerPoolCfgEntry.setStatus("current")
_RuijieIPv6PoolCfgIndex_Type = Unsigned32
_RuijieIPv6PoolCfgIndex_Object = MibTableColumn
ruijieIPv6PoolCfgIndex = _RuijieIPv6PoolCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 45, 1, 1, 2, 4, 1, 1),
    _RuijieIPv6PoolCfgIndex_Type()
)
ruijieIPv6PoolCfgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPv6PoolCfgIndex.setStatus("current")


class _RuijieIPv6PoolName_Type(DisplayString):
    """Custom type ruijieIPv6PoolName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuijieIPv6PoolName_Type.__name__ = "DisplayString"
_RuijieIPv6PoolName_Object = MibTableColumn
ruijieIPv6PoolName = _RuijieIPv6PoolName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 45, 1, 1, 2, 4, 1, 2),
    _RuijieIPv6PoolName_Type()
)
ruijieIPv6PoolName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieIPv6PoolName.setStatus("current")
_RuijieIPv6PoolStartAddr_Type = InetAddressIPv6
_RuijieIPv6PoolStartAddr_Object = MibTableColumn
ruijieIPv6PoolStartAddr = _RuijieIPv6PoolStartAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 45, 1, 1, 2, 4, 1, 3),
    _RuijieIPv6PoolStartAddr_Type()
)
ruijieIPv6PoolStartAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieIPv6PoolStartAddr.setStatus("current")
_RuijieIPv6PoolStopAddr_Type = InetAddressIPv6
_RuijieIPv6PoolStopAddr_Object = MibTableColumn
ruijieIPv6PoolStopAddr = _RuijieIPv6PoolStopAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 45, 1, 1, 2, 4, 1, 4),
    _RuijieIPv6PoolStopAddr_Type()
)
ruijieIPv6PoolStopAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieIPv6PoolStopAddr.setStatus("current")
_RuijieIPv6NetPrefixLen_Type = Unsigned32
_RuijieIPv6NetPrefixLen_Object = MibTableColumn
ruijieIPv6NetPrefixLen = _RuijieIPv6NetPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 45, 1, 1, 2, 4, 1, 5),
    _RuijieIPv6NetPrefixLen_Type()
)
ruijieIPv6NetPrefixLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieIPv6NetPrefixLen.setStatus("current")
_RuijiePrimDNSServerIPv6Address_Type = InetAddressIPv6
_RuijiePrimDNSServerIPv6Address_Object = MibTableColumn
ruijiePrimDNSServerIPv6Address = _RuijiePrimDNSServerIPv6Address_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 45, 1, 1, 2, 4, 1, 6),
    _RuijiePrimDNSServerIPv6Address_Type()
)
ruijiePrimDNSServerIPv6Address.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijiePrimDNSServerIPv6Address.setStatus("current")
_RuijieSeconDNSServerIPv6Address_Type = InetAddressIPv6
_RuijieSeconDNSServerIPv6Address_Object = MibTableColumn
ruijieSeconDNSServerIPv6Address = _RuijieSeconDNSServerIPv6Address_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 45, 1, 1, 2, 4, 1, 7),
    _RuijieSeconDNSServerIPv6Address_Type()
)
ruijieSeconDNSServerIPv6Address.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieSeconDNSServerIPv6Address.setStatus("current")
_RuijieIPv6AddrLease_Type = TimeTicks
_RuijieIPv6AddrLease_Object = MibTableColumn
ruijieIPv6AddrLease = _RuijieIPv6AddrLease_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 45, 1, 1, 2, 4, 1, 8),
    _RuijieIPv6AddrLease_Type()
)
ruijieIPv6AddrLease.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieIPv6AddrLease.setStatus("current")
_RuijieIPv6RawStatus_Type = RowStatus
_RuijieIPv6RawStatus_Object = MibTableColumn
ruijieIPv6RawStatus = _RuijieIPv6RawStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 45, 1, 1, 2, 4, 1, 9),
    _RuijieIPv6RawStatus_Type()
)
ruijieIPv6RawStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieIPv6RawStatus.setStatus("current")
_RuijieDhcpv6MIBConformance_ObjectIdentity = ObjectIdentity
ruijieDhcpv6MIBConformance = _RuijieDhcpv6MIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 45, 2)
)
if mibBuilder.loadTexts:
    ruijieDhcpv6MIBConformance.setStatus("current")
_RuijieDhcpv6MIBCompliances_ObjectIdentity = ObjectIdentity
ruijieDhcpv6MIBCompliances = _RuijieDhcpv6MIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 45, 2, 1)
)
_RuijieDhcpv6MIBGroups_ObjectIdentity = ObjectIdentity
ruijieDhcpv6MIBGroups = _RuijieDhcpv6MIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 45, 2, 2)
)

# Managed Objects groups

ruijieDhcpv6ServerCountersObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 45, 2, 2, 1)
)
ruijieDhcpv6ServerCountersObjects.setObjects(
      *(("RUIJIE-DHCPv6-MIB", "ruijieDhcpv6ServerHCountSolicits"),
        ("RUIJIE-DHCPv6-MIB", "ruijieDhcpv6ServerHCountRenews"),
        ("RUIJIE-DHCPv6-MIB", "ruijieDhcpv6ServerHCountDeclines"),
        ("RUIJIE-DHCPv6-MIB", "ruijieDhcpv6ServerHCountReleases"),
        ("RUIJIE-DHCPv6-MIB", "ruijieDhcpv6ServerHCountInforms"),
        ("RUIJIE-DHCPv6-MIB", "ruijieDhcpv6ServerHCountConfirms"),
        ("RUIJIE-DHCPv6-MIB", "ruijieDhcpv6ServerHCountRebinds"),
        ("RUIJIE-DHCPv6-MIB", "ruijieDhcpv6ServerHCountAdvertises"),
        ("RUIJIE-DHCPv6-MIB", "ruijieDhcpv6ServerHCountSuccReplies"),
        ("RUIJIE-DHCPv6-MIB", "ruijieDhcpv6ServerHCountFailReplies"),
        ("RUIJIE-DHCPv6-MIB", "ruijieDhcpv6ServerHCountInPkts"),
        ("RUIJIE-DHCPv6-MIB", "ruijieDhcpv6ServerHCountOutPkts"),
        ("RUIJIE-DHCPv6-MIB", "ruijieDhcpv6ServerHCountDroppedUnknown"),
        ("RUIJIE-DHCPv6-MIB", "ruijieDhcpv6ServerHCountDroppedError"),
        ("RUIJIE-DHCPv6-MIB", "ruijieDhcpv6ServerHCountRelayforward"),
        ("RUIJIE-DHCPv6-MIB", "ruijieDhcpv6ServerHCountRelayreply"),
        ("RUIJIE-DHCPv6-MIB", "ruijieDhcpv6ServerHCountReqtimes"),
        ("RUIJIE-DHCPv6-MIB", "ruijieDhcpv6ServerHCountReqSuctimes"))
)
if mibBuilder.loadTexts:
    ruijieDhcpv6ServerCountersObjects.setStatus("current")

ruijieDhcpv6ServerConfigurationObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 45, 2, 2, 2)
)
ruijieDhcpv6ServerConfigurationObjects.setObjects(
      *(("RUIJIE-DHCPv6-MIB", "ruijieDhcpv6ServerNumBindings"),
        ("RUIJIE-DHCPv6-MIB", "ruijieDhcpv6ServerBindingsPoolName"),
        ("RUIJIE-DHCPv6-MIB", "ruijieDhcpv6ServerBindingsClientDuid"),
        ("RUIJIE-DHCPv6-MIB", "ruijieDhcpv6ServerBindingsIaType"),
        ("RUIJIE-DHCPv6-MIB", "ruijieDhcpv6ServerBindingsIaId"),
        ("RUIJIE-DHCPv6-MIB", "ruijieDhcpv6ServerBindingsAddress"),
        ("RUIJIE-DHCPv6-MIB", "ruijieDhcpv6ServerBindingsPrefix"),
        ("RUIJIE-DHCPv6-MIB", "ruijieDhcpv6ServerBindingsPrefixLength"),
        ("RUIJIE-DHCPv6-MIB", "ruijieDhcpv6ServerBindingsDuration"),
        ("RUIJIE-DHCPv6-MIB", "ruijieDhcpv6ServerBindingsIfIndex"))
)
if mibBuilder.loadTexts:
    ruijieDhcpv6ServerConfigurationObjects.setStatus("current")

ruijieDhcpv6ServerPoolUsageTableObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 45, 2, 2, 3)
)
ruijieDhcpv6ServerPoolUsageTableObjects.setObjects(
      *(("RUIJIE-DHCPv6-MIB", "ruijieIPv6PoolUsageIndex"),
        ("RUIJIE-DHCPv6-MIB", "ruijieIPv6PoolName"),
        ("RUIJIE-DHCPv6-MIB", "ruijieIPv6DHCPIPPoolUsage"),
        ("RUIJIE-DHCPv6-MIB", "ruijieIPv6PoolUsageRawStatus"))
)
if mibBuilder.loadTexts:
    ruijieDhcpv6ServerPoolUsageTableObjects.setStatus("current")

ruijieDhcpv6ServerPoolConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 45, 2, 2, 4)
)
ruijieDhcpv6ServerPoolConfigGroup.setObjects(
      *(("RUIJIE-DHCPv6-MIB", "ruijieIPv6PoolCfgIndex"),
        ("RUIJIE-DHCPv6-MIB", "ruijieIPv6PoolName"),
        ("RUIJIE-DHCPv6-MIB", "ruijieIPv6PoolStartAddr"),
        ("RUIJIE-DHCPv6-MIB", "ruijieIPv6PoolStopAddr"),
        ("RUIJIE-DHCPv6-MIB", "ruijieIPv6NetPrefixLen"),
        ("RUIJIE-DHCPv6-MIB", "ruijiePrimDNSServerIPv6Address"),
        ("RUIJIE-DHCPv6-MIB", "ruijieSeconDNSServerIPv6Address"),
        ("RUIJIE-DHCPv6-MIB", "ruijieIPv6AddrLease"),
        ("RUIJIE-DHCPv6-MIB", "ruijieIPv6RawStatus"))
)
if mibBuilder.loadTexts:
    ruijieDhcpv6ServerPoolConfigGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ruijieDhcpv6ServerCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 45, 2, 1, 1)
)
ruijieDhcpv6ServerCompliance.setObjects(
      *(("RUIJIE-DHCPv6-MIB", "ruijieDhcpv6ServerCountersObjects"),
        ("RUIJIE-DHCPv6-MIB", "ruijieDhcpv6ServerConfigurationObjects"))
)
if mibBuilder.loadTexts:
    ruijieDhcpv6ServerCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-DHCPv6-MIB",
    **{"ruijieDhcpv6MIB": ruijieDhcpv6MIB,
       "ruijieDhcpv6MIBObjects": ruijieDhcpv6MIBObjects,
       "ruijieDhcpv6ServerMIBObjects": ruijieDhcpv6ServerMIBObjects,
       "ruijieDhcpv6ServerCounters": ruijieDhcpv6ServerCounters,
       "ruijieDhcpv6ServerHCountSolicits": ruijieDhcpv6ServerHCountSolicits,
       "ruijieDhcpv6ServerHCountRequests": ruijieDhcpv6ServerHCountRequests,
       "ruijieDhcpv6ServerHCountRenews": ruijieDhcpv6ServerHCountRenews,
       "ruijieDhcpv6ServerHCountDeclines": ruijieDhcpv6ServerHCountDeclines,
       "ruijieDhcpv6ServerHCountReleases": ruijieDhcpv6ServerHCountReleases,
       "ruijieDhcpv6ServerHCountInforms": ruijieDhcpv6ServerHCountInforms,
       "ruijieDhcpv6ServerHCountConfirms": ruijieDhcpv6ServerHCountConfirms,
       "ruijieDhcpv6ServerHCountRebinds": ruijieDhcpv6ServerHCountRebinds,
       "ruijieDhcpv6ServerHCountAdvertises": ruijieDhcpv6ServerHCountAdvertises,
       "ruijieDhcpv6ServerHCountSuccReplies": ruijieDhcpv6ServerHCountSuccReplies,
       "ruijieDhcpv6ServerHCountFailReplies": ruijieDhcpv6ServerHCountFailReplies,
       "ruijieDhcpv6ServerHCountInPkts": ruijieDhcpv6ServerHCountInPkts,
       "ruijieDhcpv6ServerHCountOutPkts": ruijieDhcpv6ServerHCountOutPkts,
       "ruijieDhcpv6ServerHCountDroppedUnknown": ruijieDhcpv6ServerHCountDroppedUnknown,
       "ruijieDhcpv6ServerHCountDroppedError": ruijieDhcpv6ServerHCountDroppedError,
       "ruijieDhcpv6ServerHCountRelayforward": ruijieDhcpv6ServerHCountRelayforward,
       "ruijieDhcpv6ServerHCountRelayreply": ruijieDhcpv6ServerHCountRelayreply,
       "ruijieDhcpv6ServerHCountReqtimes": ruijieDhcpv6ServerHCountReqtimes,
       "ruijieDhcpv6ServerHCountReqSuctimes": ruijieDhcpv6ServerHCountReqSuctimes,
       "ruijieDhcpv6ServerConfiguration": ruijieDhcpv6ServerConfiguration,
       "ruijieDhcpv6ServerNumBindings": ruijieDhcpv6ServerNumBindings,
       "ruijieDhcpv6ServerBindingsTable": ruijieDhcpv6ServerBindingsTable,
       "ruijieDhcpv6ServerBindingsEntry": ruijieDhcpv6ServerBindingsEntry,
       "ruijieDhcpv6ServerBindingsPoolName": ruijieDhcpv6ServerBindingsPoolName,
       "ruijieDhcpv6ServerBindingsClientDuid": ruijieDhcpv6ServerBindingsClientDuid,
       "ruijieDhcpv6ServerBindingsIaType": ruijieDhcpv6ServerBindingsIaType,
       "ruijieDhcpv6ServerBindingsIaId": ruijieDhcpv6ServerBindingsIaId,
       "ruijieDhcpv6ServerBindingsAddress": ruijieDhcpv6ServerBindingsAddress,
       "ruijieDhcpv6ServerBindingsPrefix": ruijieDhcpv6ServerBindingsPrefix,
       "ruijieDhcpv6ServerBindingsPrefixLength": ruijieDhcpv6ServerBindingsPrefixLength,
       "ruijieDhcpv6ServerBindingsDuration": ruijieDhcpv6ServerBindingsDuration,
       "ruijieDhcpv6ServerBindingsIfIndex": ruijieDhcpv6ServerBindingsIfIndex,
       "ruijieDhcpv6ServerPoolUsageTable": ruijieDhcpv6ServerPoolUsageTable,
       "ruijieDhcpv6ServerPoolEntry": ruijieDhcpv6ServerPoolEntry,
       "ruijieIPv6PoolUsageIndex": ruijieIPv6PoolUsageIndex,
       "ruijieIPv6PoolUsageName": ruijieIPv6PoolUsageName,
       "ruijieIPv6DHCPIPPoolUsage": ruijieIPv6DHCPIPPoolUsage,
       "ruijieIPv6PoolUsageRawStatus": ruijieIPv6PoolUsageRawStatus,
       "ruijieDhcpv6ServerPoolConfigTable": ruijieDhcpv6ServerPoolConfigTable,
       "ruijieDhcpv6ServerPoolCfgEntry": ruijieDhcpv6ServerPoolCfgEntry,
       "ruijieIPv6PoolCfgIndex": ruijieIPv6PoolCfgIndex,
       "ruijieIPv6PoolName": ruijieIPv6PoolName,
       "ruijieIPv6PoolStartAddr": ruijieIPv6PoolStartAddr,
       "ruijieIPv6PoolStopAddr": ruijieIPv6PoolStopAddr,
       "ruijieIPv6NetPrefixLen": ruijieIPv6NetPrefixLen,
       "ruijiePrimDNSServerIPv6Address": ruijiePrimDNSServerIPv6Address,
       "ruijieSeconDNSServerIPv6Address": ruijieSeconDNSServerIPv6Address,
       "ruijieIPv6AddrLease": ruijieIPv6AddrLease,
       "ruijieIPv6RawStatus": ruijieIPv6RawStatus,
       "ruijieDhcpv6MIBConformance": ruijieDhcpv6MIBConformance,
       "ruijieDhcpv6MIBCompliances": ruijieDhcpv6MIBCompliances,
       "ruijieDhcpv6ServerCompliance": ruijieDhcpv6ServerCompliance,
       "ruijieDhcpv6MIBGroups": ruijieDhcpv6MIBGroups,
       "ruijieDhcpv6ServerCountersObjects": ruijieDhcpv6ServerCountersObjects,
       "ruijieDhcpv6ServerConfigurationObjects": ruijieDhcpv6ServerConfigurationObjects,
       "ruijieDhcpv6ServerPoolUsageTableObjects": ruijieDhcpv6ServerPoolUsageTableObjects,
       "ruijieDhcpv6ServerPoolConfigGroup": ruijieDhcpv6ServerPoolConfigGroup}
)
