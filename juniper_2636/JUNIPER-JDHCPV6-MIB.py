# SNMP MIB module (JUNIPER-JDHCPV6-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/juniper_2636/JUNIPER-JDHCPV6-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 30 16:49:53 2025
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

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(Ipv6Address,
 Ipv6AddressPrefix) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address",
    "Ipv6AddressPrefix")

(jnxJdhcpv6MibRoot,) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxJdhcpv6MibRoot")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

jnxJdhcpv6MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62)
)
if mibBuilder.loadTexts:
    jnxJdhcpv6MIB.setRevisions(
        ("2021-06-15 00:00",
         "2011-03-15 00:00",
         "2011-01-25 00:00",
         "2010-02-15 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxJdhcpv6Objects_ObjectIdentity = ObjectIdentity
jnxJdhcpv6Objects = _JnxJdhcpv6Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 1)
)
_JnxJdhcpv6LocalServerObjects_ObjectIdentity = ObjectIdentity
jnxJdhcpv6LocalServerObjects = _JnxJdhcpv6LocalServerObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2)
)
_JnxJdhcpv6LocalServerStatistics_ObjectIdentity = ObjectIdentity
jnxJdhcpv6LocalServerStatistics = _JnxJdhcpv6LocalServerStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 1)
)
_JnxJdhcpv6LocalServerTotalDropped_Type = Counter32
_JnxJdhcpv6LocalServerTotalDropped_Object = MibScalar
jnxJdhcpv6LocalServerTotalDropped = _JnxJdhcpv6LocalServerTotalDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 1, 1),
    _JnxJdhcpv6LocalServerTotalDropped_Type()
)
jnxJdhcpv6LocalServerTotalDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerTotalDropped.setStatus("current")
_JnxJdhcpv6LocalServerNoSafdDropped_Type = Counter32
_JnxJdhcpv6LocalServerNoSafdDropped_Object = MibScalar
jnxJdhcpv6LocalServerNoSafdDropped = _JnxJdhcpv6LocalServerNoSafdDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 1, 2),
    _JnxJdhcpv6LocalServerNoSafdDropped_Type()
)
jnxJdhcpv6LocalServerNoSafdDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerNoSafdDropped.setStatus("current")
_JnxJdhcpv6LocalServerBadSendDropped_Type = Counter32
_JnxJdhcpv6LocalServerBadSendDropped_Object = MibScalar
jnxJdhcpv6LocalServerBadSendDropped = _JnxJdhcpv6LocalServerBadSendDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 1, 3),
    _JnxJdhcpv6LocalServerBadSendDropped_Type()
)
jnxJdhcpv6LocalServerBadSendDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerBadSendDropped.setStatus("current")
_JnxJdhcpv6LocalServerShortPacketDropped_Type = Counter32
_JnxJdhcpv6LocalServerShortPacketDropped_Object = MibScalar
jnxJdhcpv6LocalServerShortPacketDropped = _JnxJdhcpv6LocalServerShortPacketDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 1, 4),
    _JnxJdhcpv6LocalServerShortPacketDropped_Type()
)
jnxJdhcpv6LocalServerShortPacketDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerShortPacketDropped.setStatus("current")
_JnxJdhcpv6LocalServerBadMsgtypeDropped_Type = Counter32
_JnxJdhcpv6LocalServerBadMsgtypeDropped_Object = MibScalar
jnxJdhcpv6LocalServerBadMsgtypeDropped = _JnxJdhcpv6LocalServerBadMsgtypeDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 1, 5),
    _JnxJdhcpv6LocalServerBadMsgtypeDropped_Type()
)
jnxJdhcpv6LocalServerBadMsgtypeDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerBadMsgtypeDropped.setStatus("current")
_JnxJdhcpv6LocalServerBadOptionsDropped_Type = Counter32
_JnxJdhcpv6LocalServerBadOptionsDropped_Object = MibScalar
jnxJdhcpv6LocalServerBadOptionsDropped = _JnxJdhcpv6LocalServerBadOptionsDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 1, 6),
    _JnxJdhcpv6LocalServerBadOptionsDropped_Type()
)
jnxJdhcpv6LocalServerBadOptionsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerBadOptionsDropped.setStatus("current")
_JnxJdhcpv6LocalServerBadSrcAddressDropped_Type = Counter32
_JnxJdhcpv6LocalServerBadSrcAddressDropped_Object = MibScalar
jnxJdhcpv6LocalServerBadSrcAddressDropped = _JnxJdhcpv6LocalServerBadSrcAddressDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 1, 7),
    _JnxJdhcpv6LocalServerBadSrcAddressDropped_Type()
)
jnxJdhcpv6LocalServerBadSrcAddressDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerBadSrcAddressDropped.setStatus("current")
_JnxJdhcpv6LocalServerRelayHopCountDropped_Type = Counter32
_JnxJdhcpv6LocalServerRelayHopCountDropped_Object = MibScalar
jnxJdhcpv6LocalServerRelayHopCountDropped = _JnxJdhcpv6LocalServerRelayHopCountDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 1, 8),
    _JnxJdhcpv6LocalServerRelayHopCountDropped_Type()
)
jnxJdhcpv6LocalServerRelayHopCountDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerRelayHopCountDropped.setStatus("current")
_JnxJdhcpv6LocalServerNoClientIdDropped_Type = Counter32
_JnxJdhcpv6LocalServerNoClientIdDropped_Object = MibScalar
jnxJdhcpv6LocalServerNoClientIdDropped = _JnxJdhcpv6LocalServerNoClientIdDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 1, 9),
    _JnxJdhcpv6LocalServerNoClientIdDropped_Type()
)
jnxJdhcpv6LocalServerNoClientIdDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerNoClientIdDropped.setStatus("current")
_JnxJdhcpv6LocalServerDeclineReceived_Type = Counter32
_JnxJdhcpv6LocalServerDeclineReceived_Object = MibScalar
jnxJdhcpv6LocalServerDeclineReceived = _JnxJdhcpv6LocalServerDeclineReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 1, 10),
    _JnxJdhcpv6LocalServerDeclineReceived_Type()
)
jnxJdhcpv6LocalServerDeclineReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerDeclineReceived.setStatus("current")
_JnxJdhcpv6LocalServerSolicitReceived_Type = Counter32
_JnxJdhcpv6LocalServerSolicitReceived_Object = MibScalar
jnxJdhcpv6LocalServerSolicitReceived = _JnxJdhcpv6LocalServerSolicitReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 1, 11),
    _JnxJdhcpv6LocalServerSolicitReceived_Type()
)
jnxJdhcpv6LocalServerSolicitReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerSolicitReceived.setStatus("current")
_JnxJdhcpv6LocalServerInformationRequestReceived_Type = Counter32
_JnxJdhcpv6LocalServerInformationRequestReceived_Object = MibScalar
jnxJdhcpv6LocalServerInformationRequestReceived = _JnxJdhcpv6LocalServerInformationRequestReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 1, 12),
    _JnxJdhcpv6LocalServerInformationRequestReceived_Type()
)
jnxJdhcpv6LocalServerInformationRequestReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerInformationRequestReceived.setStatus("current")
_JnxJdhcpv6LocalServerReleaseReceived_Type = Counter32
_JnxJdhcpv6LocalServerReleaseReceived_Object = MibScalar
jnxJdhcpv6LocalServerReleaseReceived = _JnxJdhcpv6LocalServerReleaseReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 1, 13),
    _JnxJdhcpv6LocalServerReleaseReceived_Type()
)
jnxJdhcpv6LocalServerReleaseReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerReleaseReceived.setStatus("current")
_JnxJdhcpv6LocalServerRequestReceived_Type = Counter32
_JnxJdhcpv6LocalServerRequestReceived_Object = MibScalar
jnxJdhcpv6LocalServerRequestReceived = _JnxJdhcpv6LocalServerRequestReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 1, 14),
    _JnxJdhcpv6LocalServerRequestReceived_Type()
)
jnxJdhcpv6LocalServerRequestReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerRequestReceived.setStatus("current")
_JnxJdhcpv6LocalServerConfirmReceived_Type = Counter32
_JnxJdhcpv6LocalServerConfirmReceived_Object = MibScalar
jnxJdhcpv6LocalServerConfirmReceived = _JnxJdhcpv6LocalServerConfirmReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 1, 15),
    _JnxJdhcpv6LocalServerConfirmReceived_Type()
)
jnxJdhcpv6LocalServerConfirmReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerConfirmReceived.setStatus("current")
_JnxJdhcpv6LocalServerRenewReceived_Type = Counter32
_JnxJdhcpv6LocalServerRenewReceived_Object = MibScalar
jnxJdhcpv6LocalServerRenewReceived = _JnxJdhcpv6LocalServerRenewReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 1, 16),
    _JnxJdhcpv6LocalServerRenewReceived_Type()
)
jnxJdhcpv6LocalServerRenewReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerRenewReceived.setStatus("current")
_JnxJdhcpv6LocalServerRebindReceived_Type = Counter32
_JnxJdhcpv6LocalServerRebindReceived_Object = MibScalar
jnxJdhcpv6LocalServerRebindReceived = _JnxJdhcpv6LocalServerRebindReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 1, 17),
    _JnxJdhcpv6LocalServerRebindReceived_Type()
)
jnxJdhcpv6LocalServerRebindReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerRebindReceived.setStatus("current")
_JnxJdhcpv6LocalServerRelayForwReceived_Type = Counter32
_JnxJdhcpv6LocalServerRelayForwReceived_Object = MibScalar
jnxJdhcpv6LocalServerRelayForwReceived = _JnxJdhcpv6LocalServerRelayForwReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 1, 18),
    _JnxJdhcpv6LocalServerRelayForwReceived_Type()
)
jnxJdhcpv6LocalServerRelayForwReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerRelayForwReceived.setStatus("current")
_JnxJdhcpv6LocalServerRelayReplReceived_Type = Counter32
_JnxJdhcpv6LocalServerRelayReplReceived_Object = MibScalar
jnxJdhcpv6LocalServerRelayReplReceived = _JnxJdhcpv6LocalServerRelayReplReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 1, 19),
    _JnxJdhcpv6LocalServerRelayReplReceived_Type()
)
jnxJdhcpv6LocalServerRelayReplReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerRelayReplReceived.setStatus("current")
_JnxJdhcpv6LocalServerAdvertiseSent_Type = Counter32
_JnxJdhcpv6LocalServerAdvertiseSent_Object = MibScalar
jnxJdhcpv6LocalServerAdvertiseSent = _JnxJdhcpv6LocalServerAdvertiseSent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 1, 20),
    _JnxJdhcpv6LocalServerAdvertiseSent_Type()
)
jnxJdhcpv6LocalServerAdvertiseSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerAdvertiseSent.setStatus("current")
_JnxJdhcpv6LocalServerReplySent_Type = Counter32
_JnxJdhcpv6LocalServerReplySent_Object = MibScalar
jnxJdhcpv6LocalServerReplySent = _JnxJdhcpv6LocalServerReplySent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 1, 21),
    _JnxJdhcpv6LocalServerReplySent_Type()
)
jnxJdhcpv6LocalServerReplySent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerReplySent.setStatus("current")
_JnxJdhcpv6LocalServerReconfigureSent_Type = Counter32
_JnxJdhcpv6LocalServerReconfigureSent_Object = MibScalar
jnxJdhcpv6LocalServerReconfigureSent = _JnxJdhcpv6LocalServerReconfigureSent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 1, 22),
    _JnxJdhcpv6LocalServerReconfigureSent_Type()
)
jnxJdhcpv6LocalServerReconfigureSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerReconfigureSent.setStatus("current")
_JnxJdhcpv6LocalServerTotalLeaseCount_Type = Counter32
_JnxJdhcpv6LocalServerTotalLeaseCount_Object = MibScalar
jnxJdhcpv6LocalServerTotalLeaseCount = _JnxJdhcpv6LocalServerTotalLeaseCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 1, 23),
    _JnxJdhcpv6LocalServerTotalLeaseCount_Type()
)
jnxJdhcpv6LocalServerTotalLeaseCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerTotalLeaseCount.setStatus("current")
_JnxJdhcpv6LocalServerBindings_ObjectIdentity = ObjectIdentity
jnxJdhcpv6LocalServerBindings = _JnxJdhcpv6LocalServerBindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 2)
)
_JnxJdhcpv6LocalServerBindingsTable_Object = MibTable
jnxJdhcpv6LocalServerBindingsTable = _JnxJdhcpv6LocalServerBindingsTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 2, 1)
)
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerBindingsTable.setStatus("current")
_JnxJdhcpv6LocalServerBindingsEntry_Object = MibTableRow
jnxJdhcpv6LocalServerBindingsEntry = _JnxJdhcpv6LocalServerBindingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 2, 1, 1)
)
jnxJdhcpv6LocalServerBindingsEntry.setIndexNames(
    (0, "JUNIPER-JDHCPV6-MIB", "jnxJdhcpv6LocalServerBindingsPrefix"),
    (0, "JUNIPER-JDHCPV6-MIB", "jnxJdhcpv6LocalServerBindingsLength"),
)
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerBindingsEntry.setStatus("current")
_JnxJdhcpv6LocalServerBindingsPrefix_Type = Ipv6AddressPrefix
_JnxJdhcpv6LocalServerBindingsPrefix_Object = MibTableColumn
jnxJdhcpv6LocalServerBindingsPrefix = _JnxJdhcpv6LocalServerBindingsPrefix_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 2, 1, 1, 1),
    _JnxJdhcpv6LocalServerBindingsPrefix_Type()
)
jnxJdhcpv6LocalServerBindingsPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerBindingsPrefix.setStatus("current")
_JnxJdhcpv6LocalServerBindingsLength_Type = Unsigned32
_JnxJdhcpv6LocalServerBindingsLength_Object = MibTableColumn
jnxJdhcpv6LocalServerBindingsLength = _JnxJdhcpv6LocalServerBindingsLength_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 2, 1, 1, 2),
    _JnxJdhcpv6LocalServerBindingsLength_Type()
)
jnxJdhcpv6LocalServerBindingsLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerBindingsLength.setStatus("current")
_JnxJdhcpv6LocalServerBindingsState_Type = DisplayString
_JnxJdhcpv6LocalServerBindingsState_Object = MibTableColumn
jnxJdhcpv6LocalServerBindingsState = _JnxJdhcpv6LocalServerBindingsState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 2, 1, 1, 3),
    _JnxJdhcpv6LocalServerBindingsState_Type()
)
jnxJdhcpv6LocalServerBindingsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerBindingsState.setStatus("current")
_JnxJdhcpv6LocalServerBindingsLeaseEndTime_Type = DateAndTime
_JnxJdhcpv6LocalServerBindingsLeaseEndTime_Object = MibTableColumn
jnxJdhcpv6LocalServerBindingsLeaseEndTime = _JnxJdhcpv6LocalServerBindingsLeaseEndTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 2, 1, 1, 4),
    _JnxJdhcpv6LocalServerBindingsLeaseEndTime_Type()
)
jnxJdhcpv6LocalServerBindingsLeaseEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerBindingsLeaseEndTime.setStatus("current")
_JnxJdhcpv6LocalServerBindingsLeaseExpireTime_Type = Unsigned32
_JnxJdhcpv6LocalServerBindingsLeaseExpireTime_Object = MibTableColumn
jnxJdhcpv6LocalServerBindingsLeaseExpireTime = _JnxJdhcpv6LocalServerBindingsLeaseExpireTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 2, 1, 1, 5),
    _JnxJdhcpv6LocalServerBindingsLeaseExpireTime_Type()
)
jnxJdhcpv6LocalServerBindingsLeaseExpireTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerBindingsLeaseExpireTime.setStatus("current")
_JnxJdhcpv6LocalServerBindingsLeaseStartTime_Type = DateAndTime
_JnxJdhcpv6LocalServerBindingsLeaseStartTime_Object = MibTableColumn
jnxJdhcpv6LocalServerBindingsLeaseStartTime = _JnxJdhcpv6LocalServerBindingsLeaseStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 2, 1, 1, 6),
    _JnxJdhcpv6LocalServerBindingsLeaseStartTime_Type()
)
jnxJdhcpv6LocalServerBindingsLeaseStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerBindingsLeaseStartTime.setStatus("current")
_JnxJdhcpv6LocalServerBindingsIncomingClientInterface_Type = DisplayString
_JnxJdhcpv6LocalServerBindingsIncomingClientInterface_Object = MibTableColumn
jnxJdhcpv6LocalServerBindingsIncomingClientInterface = _JnxJdhcpv6LocalServerBindingsIncomingClientInterface_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 2, 1, 1, 7),
    _JnxJdhcpv6LocalServerBindingsIncomingClientInterface_Type()
)
jnxJdhcpv6LocalServerBindingsIncomingClientInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerBindingsIncomingClientInterface.setStatus("current")
_JnxJdhcpv6LocalServerBindingsClientInterfaceVlanId_Type = Unsigned32
_JnxJdhcpv6LocalServerBindingsClientInterfaceVlanId_Object = MibTableColumn
jnxJdhcpv6LocalServerBindingsClientInterfaceVlanId = _JnxJdhcpv6LocalServerBindingsClientInterfaceVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 2, 1, 1, 8),
    _JnxJdhcpv6LocalServerBindingsClientInterfaceVlanId_Type()
)
jnxJdhcpv6LocalServerBindingsClientInterfaceVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerBindingsClientInterfaceVlanId.setStatus("current")
_JnxJdhcpv6LocalServerBindingsDemuxInterfaceName_Type = DisplayString
_JnxJdhcpv6LocalServerBindingsDemuxInterfaceName_Object = MibTableColumn
jnxJdhcpv6LocalServerBindingsDemuxInterfaceName = _JnxJdhcpv6LocalServerBindingsDemuxInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 2, 1, 1, 9),
    _JnxJdhcpv6LocalServerBindingsDemuxInterfaceName_Type()
)
jnxJdhcpv6LocalServerBindingsDemuxInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerBindingsDemuxInterfaceName.setStatus("current")
_JnxJdhcpv6LocalServerBindingsServerIpAddress_Type = IpAddress
_JnxJdhcpv6LocalServerBindingsServerIpAddress_Object = MibTableColumn
jnxJdhcpv6LocalServerBindingsServerIpAddress = _JnxJdhcpv6LocalServerBindingsServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 2, 1, 1, 10),
    _JnxJdhcpv6LocalServerBindingsServerIpAddress_Type()
)
jnxJdhcpv6LocalServerBindingsServerIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerBindingsServerIpAddress.setStatus("current")
_JnxJdhcpv6LocalServerBindingsBootpRelayAddress_Type = IpAddress
_JnxJdhcpv6LocalServerBindingsBootpRelayAddress_Object = MibTableColumn
jnxJdhcpv6LocalServerBindingsBootpRelayAddress = _JnxJdhcpv6LocalServerBindingsBootpRelayAddress_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 2, 1, 1, 11),
    _JnxJdhcpv6LocalServerBindingsBootpRelayAddress_Type()
)
jnxJdhcpv6LocalServerBindingsBootpRelayAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerBindingsBootpRelayAddress.setStatus("current")
_JnxJdhcpv6LocalServerBindingsPreviousBootpRelayAddress_Type = IpAddress
_JnxJdhcpv6LocalServerBindingsPreviousBootpRelayAddress_Object = MibTableColumn
jnxJdhcpv6LocalServerBindingsPreviousBootpRelayAddress = _JnxJdhcpv6LocalServerBindingsPreviousBootpRelayAddress_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 2, 1, 1, 12),
    _JnxJdhcpv6LocalServerBindingsPreviousBootpRelayAddress_Type()
)
jnxJdhcpv6LocalServerBindingsPreviousBootpRelayAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerBindingsPreviousBootpRelayAddress.setStatus("current")
_JnxJdhcpv6LocalServerBindingsClientPoolName_Type = DisplayString
_JnxJdhcpv6LocalServerBindingsClientPoolName_Object = MibTableColumn
jnxJdhcpv6LocalServerBindingsClientPoolName = _JnxJdhcpv6LocalServerBindingsClientPoolName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 2, 1, 1, 13),
    _JnxJdhcpv6LocalServerBindingsClientPoolName_Type()
)
jnxJdhcpv6LocalServerBindingsClientPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerBindingsClientPoolName.setStatus("current")
_JnxJdhcpv6LocalServerBindingsClientProfileName_Type = DisplayString
_JnxJdhcpv6LocalServerBindingsClientProfileName_Object = MibTableColumn
jnxJdhcpv6LocalServerBindingsClientProfileName = _JnxJdhcpv6LocalServerBindingsClientProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 2, 1, 1, 14),
    _JnxJdhcpv6LocalServerBindingsClientProfileName_Type()
)
jnxJdhcpv6LocalServerBindingsClientProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerBindingsClientProfileName.setStatus("current")
_JnxJdhcpv6LocalServerTraps_ObjectIdentity = ObjectIdentity
jnxJdhcpv6LocalServerTraps = _JnxJdhcpv6LocalServerTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 3)
)
_JnxJdhcpv6LocalServerTrapVars_ObjectIdentity = ObjectIdentity
jnxJdhcpv6LocalServerTrapVars = _JnxJdhcpv6LocalServerTrapVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 4)
)
_JnxJdhcpv6RouterName_Type = DisplayString
_JnxJdhcpv6RouterName_Object = MibScalar
jnxJdhcpv6RouterName = _JnxJdhcpv6RouterName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 4, 1),
    _JnxJdhcpv6RouterName_Type()
)
jnxJdhcpv6RouterName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJdhcpv6RouterName.setStatus("current")
_JnxJdhcpv6LocalServerInterfaceName_Type = DisplayString
_JnxJdhcpv6LocalServerInterfaceName_Object = MibScalar
jnxJdhcpv6LocalServerInterfaceName = _JnxJdhcpv6LocalServerInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 4, 2),
    _JnxJdhcpv6LocalServerInterfaceName_Type()
)
jnxJdhcpv6LocalServerInterfaceName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerInterfaceName.setStatus("current")
_JnxJdhcpv6LocalServerInterfaceLimit_Type = Unsigned32
_JnxJdhcpv6LocalServerInterfaceLimit_Object = MibScalar
jnxJdhcpv6LocalServerInterfaceLimit = _JnxJdhcpv6LocalServerInterfaceLimit_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 4, 3),
    _JnxJdhcpv6LocalServerInterfaceLimit_Type()
)
jnxJdhcpv6LocalServerInterfaceLimit.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerInterfaceLimit.setStatus("current")


class _JnxJdhcpv6LocalServerEventSeverity_Type(Integer32):
    """Custom type jnxJdhcpv6LocalServerEventSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("debug", 0),
          ("warning", 1),
          ("critical", 2))
    )


_JnxJdhcpv6LocalServerEventSeverity_Type.__name__ = "Integer32"
_JnxJdhcpv6LocalServerEventSeverity_Object = MibScalar
jnxJdhcpv6LocalServerEventSeverity = _JnxJdhcpv6LocalServerEventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 4, 4),
    _JnxJdhcpv6LocalServerEventSeverity_Type()
)
jnxJdhcpv6LocalServerEventSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerEventSeverity.setStatus("current")
_JnxJdhcpv6LocalServerEventString_Type = DisplayString
_JnxJdhcpv6LocalServerEventString_Object = MibScalar
jnxJdhcpv6LocalServerEventString = _JnxJdhcpv6LocalServerEventString_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 4, 5),
    _JnxJdhcpv6LocalServerEventString_Type()
)
jnxJdhcpv6LocalServerEventString.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerEventString.setStatus("current")
_JnxJdhcpv6LocalServerIfcStats_ObjectIdentity = ObjectIdentity
jnxJdhcpv6LocalServerIfcStats = _JnxJdhcpv6LocalServerIfcStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 5)
)
_JnxJdhcpv6LocalServerIfcStatsTable_Object = MibTable
jnxJdhcpv6LocalServerIfcStatsTable = _JnxJdhcpv6LocalServerIfcStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 5, 1)
)
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerIfcStatsTable.setStatus("current")
_JnxJdhcpv6LocalServerIfcStatsEntry_Object = MibTableRow
jnxJdhcpv6LocalServerIfcStatsEntry = _JnxJdhcpv6LocalServerIfcStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 5, 1, 1)
)
jnxJdhcpv6LocalServerIfcStatsEntry.setIndexNames(
    (0, "JUNIPER-JDHCPV6-MIB", "jnxJdhcpv6LocalServerIfcStatsIfIndex"),
)
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerIfcStatsEntry.setStatus("current")
_JnxJdhcpv6LocalServerIfcStatsIfIndex_Type = InterfaceIndex
_JnxJdhcpv6LocalServerIfcStatsIfIndex_Object = MibTableColumn
jnxJdhcpv6LocalServerIfcStatsIfIndex = _JnxJdhcpv6LocalServerIfcStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 5, 1, 1, 1),
    _JnxJdhcpv6LocalServerIfcStatsIfIndex_Type()
)
jnxJdhcpv6LocalServerIfcStatsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerIfcStatsIfIndex.setStatus("current")
_JnxJdhcpv6LocalServerIfcStatsTotalDropped_Type = Counter32
_JnxJdhcpv6LocalServerIfcStatsTotalDropped_Object = MibTableColumn
jnxJdhcpv6LocalServerIfcStatsTotalDropped = _JnxJdhcpv6LocalServerIfcStatsTotalDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 5, 1, 1, 2),
    _JnxJdhcpv6LocalServerIfcStatsTotalDropped_Type()
)
jnxJdhcpv6LocalServerIfcStatsTotalDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerIfcStatsTotalDropped.setStatus("current")
_JnxJdhcpv6LocalServerIfcStatsNoSafdDropped_Type = Counter32
_JnxJdhcpv6LocalServerIfcStatsNoSafdDropped_Object = MibTableColumn
jnxJdhcpv6LocalServerIfcStatsNoSafdDropped = _JnxJdhcpv6LocalServerIfcStatsNoSafdDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 5, 1, 1, 3),
    _JnxJdhcpv6LocalServerIfcStatsNoSafdDropped_Type()
)
jnxJdhcpv6LocalServerIfcStatsNoSafdDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerIfcStatsNoSafdDropped.setStatus("current")
_JnxJdhcpv6LocalServerIfcStatsBadSendDropped_Type = Counter32
_JnxJdhcpv6LocalServerIfcStatsBadSendDropped_Object = MibTableColumn
jnxJdhcpv6LocalServerIfcStatsBadSendDropped = _JnxJdhcpv6LocalServerIfcStatsBadSendDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 5, 1, 1, 4),
    _JnxJdhcpv6LocalServerIfcStatsBadSendDropped_Type()
)
jnxJdhcpv6LocalServerIfcStatsBadSendDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerIfcStatsBadSendDropped.setStatus("current")
_JnxJdhcpv6LocalServerIfcStatsShortPacketDropped_Type = Counter32
_JnxJdhcpv6LocalServerIfcStatsShortPacketDropped_Object = MibTableColumn
jnxJdhcpv6LocalServerIfcStatsShortPacketDropped = _JnxJdhcpv6LocalServerIfcStatsShortPacketDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 5, 1, 1, 5),
    _JnxJdhcpv6LocalServerIfcStatsShortPacketDropped_Type()
)
jnxJdhcpv6LocalServerIfcStatsShortPacketDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerIfcStatsShortPacketDropped.setStatus("current")
_JnxJdhcpv6LocalServerIfcStatsBadMsgtypeDropped_Type = Counter32
_JnxJdhcpv6LocalServerIfcStatsBadMsgtypeDropped_Object = MibTableColumn
jnxJdhcpv6LocalServerIfcStatsBadMsgtypeDropped = _JnxJdhcpv6LocalServerIfcStatsBadMsgtypeDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 5, 1, 1, 6),
    _JnxJdhcpv6LocalServerIfcStatsBadMsgtypeDropped_Type()
)
jnxJdhcpv6LocalServerIfcStatsBadMsgtypeDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerIfcStatsBadMsgtypeDropped.setStatus("current")
_JnxJdhcpv6LocalServerIfcStatsBadOptionsDropped_Type = Counter32
_JnxJdhcpv6LocalServerIfcStatsBadOptionsDropped_Object = MibTableColumn
jnxJdhcpv6LocalServerIfcStatsBadOptionsDropped = _JnxJdhcpv6LocalServerIfcStatsBadOptionsDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 5, 1, 1, 7),
    _JnxJdhcpv6LocalServerIfcStatsBadOptionsDropped_Type()
)
jnxJdhcpv6LocalServerIfcStatsBadOptionsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerIfcStatsBadOptionsDropped.setStatus("current")
_JnxJdhcpv6LocalServerIfcStatsBadSrcAddressDropped_Type = Counter32
_JnxJdhcpv6LocalServerIfcStatsBadSrcAddressDropped_Object = MibTableColumn
jnxJdhcpv6LocalServerIfcStatsBadSrcAddressDropped = _JnxJdhcpv6LocalServerIfcStatsBadSrcAddressDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 5, 1, 1, 8),
    _JnxJdhcpv6LocalServerIfcStatsBadSrcAddressDropped_Type()
)
jnxJdhcpv6LocalServerIfcStatsBadSrcAddressDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerIfcStatsBadSrcAddressDropped.setStatus("current")
_JnxJdhcpv6LocalServerIfcStatsRelayCountDropped_Type = Counter32
_JnxJdhcpv6LocalServerIfcStatsRelayCountDropped_Object = MibTableColumn
jnxJdhcpv6LocalServerIfcStatsRelayCountDropped = _JnxJdhcpv6LocalServerIfcStatsRelayCountDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 5, 1, 1, 9),
    _JnxJdhcpv6LocalServerIfcStatsRelayCountDropped_Type()
)
jnxJdhcpv6LocalServerIfcStatsRelayCountDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerIfcStatsRelayCountDropped.setStatus("current")
_JnxJdhcpv6LocalServerIfcStatsNoClientIdDropped_Type = Counter32
_JnxJdhcpv6LocalServerIfcStatsNoClientIdDropped_Object = MibTableColumn
jnxJdhcpv6LocalServerIfcStatsNoClientIdDropped = _JnxJdhcpv6LocalServerIfcStatsNoClientIdDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 5, 1, 1, 10),
    _JnxJdhcpv6LocalServerIfcStatsNoClientIdDropped_Type()
)
jnxJdhcpv6LocalServerIfcStatsNoClientIdDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerIfcStatsNoClientIdDropped.setStatus("current")
_JnxJdhcpv6LocalServerIfcStatsDeclineReceived_Type = Counter32
_JnxJdhcpv6LocalServerIfcStatsDeclineReceived_Object = MibTableColumn
jnxJdhcpv6LocalServerIfcStatsDeclineReceived = _JnxJdhcpv6LocalServerIfcStatsDeclineReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 5, 1, 1, 11),
    _JnxJdhcpv6LocalServerIfcStatsDeclineReceived_Type()
)
jnxJdhcpv6LocalServerIfcStatsDeclineReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerIfcStatsDeclineReceived.setStatus("current")
_JnxJdhcpv6LocalServerIfcStatsSolicitReceived_Type = Counter32
_JnxJdhcpv6LocalServerIfcStatsSolicitReceived_Object = MibTableColumn
jnxJdhcpv6LocalServerIfcStatsSolicitReceived = _JnxJdhcpv6LocalServerIfcStatsSolicitReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 5, 1, 1, 12),
    _JnxJdhcpv6LocalServerIfcStatsSolicitReceived_Type()
)
jnxJdhcpv6LocalServerIfcStatsSolicitReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerIfcStatsSolicitReceived.setStatus("current")
_JnxJdhcpv6LocalServerIfcStatsInformationRequestReceived_Type = Counter32
_JnxJdhcpv6LocalServerIfcStatsInformationRequestReceived_Object = MibTableColumn
jnxJdhcpv6LocalServerIfcStatsInformationRequestReceived = _JnxJdhcpv6LocalServerIfcStatsInformationRequestReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 5, 1, 1, 13),
    _JnxJdhcpv6LocalServerIfcStatsInformationRequestReceived_Type()
)
jnxJdhcpv6LocalServerIfcStatsInformationRequestReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerIfcStatsInformationRequestReceived.setStatus("current")
_JnxJdhcpv6LocalServerIfcStatsReleaseReceived_Type = Counter32
_JnxJdhcpv6LocalServerIfcStatsReleaseReceived_Object = MibTableColumn
jnxJdhcpv6LocalServerIfcStatsReleaseReceived = _JnxJdhcpv6LocalServerIfcStatsReleaseReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 5, 1, 1, 14),
    _JnxJdhcpv6LocalServerIfcStatsReleaseReceived_Type()
)
jnxJdhcpv6LocalServerIfcStatsReleaseReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerIfcStatsReleaseReceived.setStatus("current")
_JnxJdhcpv6LocalServerIfcStatsRequestReceived_Type = Counter32
_JnxJdhcpv6LocalServerIfcStatsRequestReceived_Object = MibTableColumn
jnxJdhcpv6LocalServerIfcStatsRequestReceived = _JnxJdhcpv6LocalServerIfcStatsRequestReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 5, 1, 1, 15),
    _JnxJdhcpv6LocalServerIfcStatsRequestReceived_Type()
)
jnxJdhcpv6LocalServerIfcStatsRequestReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerIfcStatsRequestReceived.setStatus("current")
_JnxJdhcpv6LocalServerIfcStatsConfirmReceived_Type = Counter32
_JnxJdhcpv6LocalServerIfcStatsConfirmReceived_Object = MibTableColumn
jnxJdhcpv6LocalServerIfcStatsConfirmReceived = _JnxJdhcpv6LocalServerIfcStatsConfirmReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 5, 1, 1, 16),
    _JnxJdhcpv6LocalServerIfcStatsConfirmReceived_Type()
)
jnxJdhcpv6LocalServerIfcStatsConfirmReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerIfcStatsConfirmReceived.setStatus("current")
_JnxJdhcpv6LocalServerIfcStatsRenewReceived_Type = Counter32
_JnxJdhcpv6LocalServerIfcStatsRenewReceived_Object = MibTableColumn
jnxJdhcpv6LocalServerIfcStatsRenewReceived = _JnxJdhcpv6LocalServerIfcStatsRenewReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 5, 1, 1, 17),
    _JnxJdhcpv6LocalServerIfcStatsRenewReceived_Type()
)
jnxJdhcpv6LocalServerIfcStatsRenewReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerIfcStatsRenewReceived.setStatus("current")
_JnxJdhcpv6LocalServerIfcStatsRebindReceived_Type = Counter32
_JnxJdhcpv6LocalServerIfcStatsRebindReceived_Object = MibTableColumn
jnxJdhcpv6LocalServerIfcStatsRebindReceived = _JnxJdhcpv6LocalServerIfcStatsRebindReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 5, 1, 1, 18),
    _JnxJdhcpv6LocalServerIfcStatsRebindReceived_Type()
)
jnxJdhcpv6LocalServerIfcStatsRebindReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerIfcStatsRebindReceived.setStatus("current")
_JnxJdhcpv6LocalServerIfcStatsRelayForwReceived_Type = Counter32
_JnxJdhcpv6LocalServerIfcStatsRelayForwReceived_Object = MibTableColumn
jnxJdhcpv6LocalServerIfcStatsRelayForwReceived = _JnxJdhcpv6LocalServerIfcStatsRelayForwReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 5, 1, 1, 19),
    _JnxJdhcpv6LocalServerIfcStatsRelayForwReceived_Type()
)
jnxJdhcpv6LocalServerIfcStatsRelayForwReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerIfcStatsRelayForwReceived.setStatus("current")
_JnxJdhcpv6LocalServerIfcStatsRelayReplReceived_Type = Counter32
_JnxJdhcpv6LocalServerIfcStatsRelayReplReceived_Object = MibTableColumn
jnxJdhcpv6LocalServerIfcStatsRelayReplReceived = _JnxJdhcpv6LocalServerIfcStatsRelayReplReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 5, 1, 1, 20),
    _JnxJdhcpv6LocalServerIfcStatsRelayReplReceived_Type()
)
jnxJdhcpv6LocalServerIfcStatsRelayReplReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerIfcStatsRelayReplReceived.setStatus("current")
_JnxJdhcpv6LocalServerIfcStatsAdvertiseSent_Type = Counter32
_JnxJdhcpv6LocalServerIfcStatsAdvertiseSent_Object = MibTableColumn
jnxJdhcpv6LocalServerIfcStatsAdvertiseSent = _JnxJdhcpv6LocalServerIfcStatsAdvertiseSent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 5, 1, 1, 21),
    _JnxJdhcpv6LocalServerIfcStatsAdvertiseSent_Type()
)
jnxJdhcpv6LocalServerIfcStatsAdvertiseSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerIfcStatsAdvertiseSent.setStatus("current")
_JnxJdhcpv6LocalServerIfcStatsReplySent_Type = Counter32
_JnxJdhcpv6LocalServerIfcStatsReplySent_Object = MibTableColumn
jnxJdhcpv6LocalServerIfcStatsReplySent = _JnxJdhcpv6LocalServerIfcStatsReplySent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 5, 1, 1, 22),
    _JnxJdhcpv6LocalServerIfcStatsReplySent_Type()
)
jnxJdhcpv6LocalServerIfcStatsReplySent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerIfcStatsReplySent.setStatus("current")
_JnxJdhcpv6LocalServerIfcStatsReconfigureSent_Type = Counter32
_JnxJdhcpv6LocalServerIfcStatsReconfigureSent_Object = MibTableColumn
jnxJdhcpv6LocalServerIfcStatsReconfigureSent = _JnxJdhcpv6LocalServerIfcStatsReconfigureSent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 5, 1, 1, 23),
    _JnxJdhcpv6LocalServerIfcStatsReconfigureSent_Type()
)
jnxJdhcpv6LocalServerIfcStatsReconfigureSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerIfcStatsReconfigureSent.setStatus("current")
_JnxJdhcpv6LocalServerIfcStatsTotalLeaseCount_Type = Counter32
_JnxJdhcpv6LocalServerIfcStatsTotalLeaseCount_Object = MibTableColumn
jnxJdhcpv6LocalServerIfcStatsTotalLeaseCount = _JnxJdhcpv6LocalServerIfcStatsTotalLeaseCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 5, 1, 1, 24),
    _JnxJdhcpv6LocalServerIfcStatsTotalLeaseCount_Type()
)
jnxJdhcpv6LocalServerIfcStatsTotalLeaseCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerIfcStatsTotalLeaseCount.setStatus("current")
_JnxJdhcpv6LocalServerIfcStatsStrictReconfigDropped_Type = Counter32
_JnxJdhcpv6LocalServerIfcStatsStrictReconfigDropped_Object = MibTableColumn
jnxJdhcpv6LocalServerIfcStatsStrictReconfigDropped = _JnxJdhcpv6LocalServerIfcStatsStrictReconfigDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 5, 1, 1, 25),
    _JnxJdhcpv6LocalServerIfcStatsStrictReconfigDropped_Type()
)
jnxJdhcpv6LocalServerIfcStatsStrictReconfigDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerIfcStatsStrictReconfigDropped.setStatus("current")
_JnxJdhcpv6LocalServerIfcStatsAuthenticationDropped_Type = Counter32
_JnxJdhcpv6LocalServerIfcStatsAuthenticationDropped_Object = MibTableColumn
jnxJdhcpv6LocalServerIfcStatsAuthenticationDropped = _JnxJdhcpv6LocalServerIfcStatsAuthenticationDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 5, 1, 1, 26),
    _JnxJdhcpv6LocalServerIfcStatsAuthenticationDropped_Type()
)
jnxJdhcpv6LocalServerIfcStatsAuthenticationDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerIfcStatsAuthenticationDropped.setStatus("current")
_JnxJdhcpv6LocalServerIfcStatsDynamicProfileDropped_Type = Counter32
_JnxJdhcpv6LocalServerIfcStatsDynamicProfileDropped_Object = MibTableColumn
jnxJdhcpv6LocalServerIfcStatsDynamicProfileDropped = _JnxJdhcpv6LocalServerIfcStatsDynamicProfileDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 5, 1, 1, 27),
    _JnxJdhcpv6LocalServerIfcStatsDynamicProfileDropped_Type()
)
jnxJdhcpv6LocalServerIfcStatsDynamicProfileDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerIfcStatsDynamicProfileDropped.setStatus("current")
_JnxJdhcpv6LocalServerIfcStatsLicenseDropped_Type = Counter32
_JnxJdhcpv6LocalServerIfcStatsLicenseDropped_Object = MibTableColumn
jnxJdhcpv6LocalServerIfcStatsLicenseDropped = _JnxJdhcpv6LocalServerIfcStatsLicenseDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 5, 1, 1, 28),
    _JnxJdhcpv6LocalServerIfcStatsLicenseDropped_Type()
)
jnxJdhcpv6LocalServerIfcStatsLicenseDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerIfcStatsLicenseDropped.setStatus("current")
_JnxJdhcpv6RelayObjects_ObjectIdentity = ObjectIdentity
jnxJdhcpv6RelayObjects = _JnxJdhcpv6RelayObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 3)
)
_JnxJdhcpv6RelayStatistics_ObjectIdentity = ObjectIdentity
jnxJdhcpv6RelayStatistics = _JnxJdhcpv6RelayStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 3, 1)
)
_JnxJdhcpv6RelayTotalDropped_Type = Counter32
_JnxJdhcpv6RelayTotalDropped_Object = MibScalar
jnxJdhcpv6RelayTotalDropped = _JnxJdhcpv6RelayTotalDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 3, 1, 1),
    _JnxJdhcpv6RelayTotalDropped_Type()
)
jnxJdhcpv6RelayTotalDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6RelayTotalDropped.setStatus("current")
_JnxJdhcpv6RelayNoSafdDropped_Type = Counter32
_JnxJdhcpv6RelayNoSafdDropped_Object = MibScalar
jnxJdhcpv6RelayNoSafdDropped = _JnxJdhcpv6RelayNoSafdDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 3, 1, 2),
    _JnxJdhcpv6RelayNoSafdDropped_Type()
)
jnxJdhcpv6RelayNoSafdDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6RelayNoSafdDropped.setStatus("current")
_JnxJdhcpv6RelayBadSendDropped_Type = Counter32
_JnxJdhcpv6RelayBadSendDropped_Object = MibScalar
jnxJdhcpv6RelayBadSendDropped = _JnxJdhcpv6RelayBadSendDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 3, 1, 3),
    _JnxJdhcpv6RelayBadSendDropped_Type()
)
jnxJdhcpv6RelayBadSendDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6RelayBadSendDropped.setStatus("current")
_JnxJdhcpv6RelayShortPacketDropped_Type = Counter32
_JnxJdhcpv6RelayShortPacketDropped_Object = MibScalar
jnxJdhcpv6RelayShortPacketDropped = _JnxJdhcpv6RelayShortPacketDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 3, 1, 4),
    _JnxJdhcpv6RelayShortPacketDropped_Type()
)
jnxJdhcpv6RelayShortPacketDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6RelayShortPacketDropped.setStatus("current")
_JnxJdhcpv6RelayBadMsgtypeDropped_Type = Counter32
_JnxJdhcpv6RelayBadMsgtypeDropped_Object = MibScalar
jnxJdhcpv6RelayBadMsgtypeDropped = _JnxJdhcpv6RelayBadMsgtypeDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 3, 1, 5),
    _JnxJdhcpv6RelayBadMsgtypeDropped_Type()
)
jnxJdhcpv6RelayBadMsgtypeDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6RelayBadMsgtypeDropped.setStatus("current")
_JnxJdhcpv6RelayBadOptionsDropped_Type = Counter32
_JnxJdhcpv6RelayBadOptionsDropped_Object = MibScalar
jnxJdhcpv6RelayBadOptionsDropped = _JnxJdhcpv6RelayBadOptionsDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 3, 1, 6),
    _JnxJdhcpv6RelayBadOptionsDropped_Type()
)
jnxJdhcpv6RelayBadOptionsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6RelayBadOptionsDropped.setStatus("current")
_JnxJdhcpv6RelayBadSrcAddressDropped_Type = Counter32
_JnxJdhcpv6RelayBadSrcAddressDropped_Object = MibScalar
jnxJdhcpv6RelayBadSrcAddressDropped = _JnxJdhcpv6RelayBadSrcAddressDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 3, 1, 7),
    _JnxJdhcpv6RelayBadSrcAddressDropped_Type()
)
jnxJdhcpv6RelayBadSrcAddressDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6RelayBadSrcAddressDropped.setStatus("current")
_JnxJdhcpv6RelayRelayHopCountDropped_Type = Counter32
_JnxJdhcpv6RelayRelayHopCountDropped_Object = MibScalar
jnxJdhcpv6RelayRelayHopCountDropped = _JnxJdhcpv6RelayRelayHopCountDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 3, 1, 8),
    _JnxJdhcpv6RelayRelayHopCountDropped_Type()
)
jnxJdhcpv6RelayRelayHopCountDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6RelayRelayHopCountDropped.setStatus("current")
_JnxJdhcpv6RelayNoClientIdDropped_Type = Counter32
_JnxJdhcpv6RelayNoClientIdDropped_Object = MibScalar
jnxJdhcpv6RelayNoClientIdDropped = _JnxJdhcpv6RelayNoClientIdDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 3, 1, 9),
    _JnxJdhcpv6RelayNoClientIdDropped_Type()
)
jnxJdhcpv6RelayNoClientIdDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6RelayNoClientIdDropped.setStatus("current")
_JnxJdhcpv6RelayDeclineReceived_Type = Counter32
_JnxJdhcpv6RelayDeclineReceived_Object = MibScalar
jnxJdhcpv6RelayDeclineReceived = _JnxJdhcpv6RelayDeclineReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 3, 1, 10),
    _JnxJdhcpv6RelayDeclineReceived_Type()
)
jnxJdhcpv6RelayDeclineReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6RelayDeclineReceived.setStatus("current")
_JnxJdhcpv6RelaySolicitReceived_Type = Counter32
_JnxJdhcpv6RelaySolicitReceived_Object = MibScalar
jnxJdhcpv6RelaySolicitReceived = _JnxJdhcpv6RelaySolicitReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 3, 1, 11),
    _JnxJdhcpv6RelaySolicitReceived_Type()
)
jnxJdhcpv6RelaySolicitReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6RelaySolicitReceived.setStatus("current")
_JnxJdhcpv6RelayInformationRequestReceived_Type = Counter32
_JnxJdhcpv6RelayInformationRequestReceived_Object = MibScalar
jnxJdhcpv6RelayInformationRequestReceived = _JnxJdhcpv6RelayInformationRequestReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 3, 1, 12),
    _JnxJdhcpv6RelayInformationRequestReceived_Type()
)
jnxJdhcpv6RelayInformationRequestReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6RelayInformationRequestReceived.setStatus("current")
_JnxJdhcpv6RelayReleaseReceived_Type = Counter32
_JnxJdhcpv6RelayReleaseReceived_Object = MibScalar
jnxJdhcpv6RelayReleaseReceived = _JnxJdhcpv6RelayReleaseReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 3, 1, 13),
    _JnxJdhcpv6RelayReleaseReceived_Type()
)
jnxJdhcpv6RelayReleaseReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6RelayReleaseReceived.setStatus("current")
_JnxJdhcpv6RelayRequestReceived_Type = Counter32
_JnxJdhcpv6RelayRequestReceived_Object = MibScalar
jnxJdhcpv6RelayRequestReceived = _JnxJdhcpv6RelayRequestReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 3, 1, 14),
    _JnxJdhcpv6RelayRequestReceived_Type()
)
jnxJdhcpv6RelayRequestReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6RelayRequestReceived.setStatus("current")
_JnxJdhcpv6RelayConfirmReceived_Type = Counter32
_JnxJdhcpv6RelayConfirmReceived_Object = MibScalar
jnxJdhcpv6RelayConfirmReceived = _JnxJdhcpv6RelayConfirmReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 3, 1, 15),
    _JnxJdhcpv6RelayConfirmReceived_Type()
)
jnxJdhcpv6RelayConfirmReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6RelayConfirmReceived.setStatus("current")
_JnxJdhcpv6RelayRenewReceived_Type = Counter32
_JnxJdhcpv6RelayRenewReceived_Object = MibScalar
jnxJdhcpv6RelayRenewReceived = _JnxJdhcpv6RelayRenewReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 3, 1, 16),
    _JnxJdhcpv6RelayRenewReceived_Type()
)
jnxJdhcpv6RelayRenewReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6RelayRenewReceived.setStatus("current")
_JnxJdhcpv6RelayRebindReceived_Type = Counter32
_JnxJdhcpv6RelayRebindReceived_Object = MibScalar
jnxJdhcpv6RelayRebindReceived = _JnxJdhcpv6RelayRebindReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 3, 1, 17),
    _JnxJdhcpv6RelayRebindReceived_Type()
)
jnxJdhcpv6RelayRebindReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6RelayRebindReceived.setStatus("current")
_JnxJdhcpv6RelayRelayForwReceived_Type = Counter32
_JnxJdhcpv6RelayRelayForwReceived_Object = MibScalar
jnxJdhcpv6RelayRelayForwReceived = _JnxJdhcpv6RelayRelayForwReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 3, 1, 18),
    _JnxJdhcpv6RelayRelayForwReceived_Type()
)
jnxJdhcpv6RelayRelayForwReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6RelayRelayForwReceived.setStatus("current")
_JnxJdhcpv6RelayRelayReplReceived_Type = Counter32
_JnxJdhcpv6RelayRelayReplReceived_Object = MibScalar
jnxJdhcpv6RelayRelayReplReceived = _JnxJdhcpv6RelayRelayReplReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 3, 1, 19),
    _JnxJdhcpv6RelayRelayReplReceived_Type()
)
jnxJdhcpv6RelayRelayReplReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6RelayRelayReplReceived.setStatus("current")
_JnxJdhcpv6RelayAdvertiseSent_Type = Counter32
_JnxJdhcpv6RelayAdvertiseSent_Object = MibScalar
jnxJdhcpv6RelayAdvertiseSent = _JnxJdhcpv6RelayAdvertiseSent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 3, 1, 20),
    _JnxJdhcpv6RelayAdvertiseSent_Type()
)
jnxJdhcpv6RelayAdvertiseSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6RelayAdvertiseSent.setStatus("current")
_JnxJdhcpv6RelayReplySent_Type = Counter32
_JnxJdhcpv6RelayReplySent_Object = MibScalar
jnxJdhcpv6RelayReplySent = _JnxJdhcpv6RelayReplySent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 3, 1, 21),
    _JnxJdhcpv6RelayReplySent_Type()
)
jnxJdhcpv6RelayReplySent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6RelayReplySent.setStatus("current")
_JnxJdhcpv6RelayReconfigureSent_Type = Counter32
_JnxJdhcpv6RelayReconfigureSent_Object = MibScalar
jnxJdhcpv6RelayReconfigureSent = _JnxJdhcpv6RelayReconfigureSent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 3, 1, 22),
    _JnxJdhcpv6RelayReconfigureSent_Type()
)
jnxJdhcpv6RelayReconfigureSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6RelayReconfigureSent.setStatus("current")
_JnxJdhcpv6RelayTotalLeaseCount_Type = Counter32
_JnxJdhcpv6RelayTotalLeaseCount_Object = MibScalar
jnxJdhcpv6RelayTotalLeaseCount = _JnxJdhcpv6RelayTotalLeaseCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 3, 1, 23),
    _JnxJdhcpv6RelayTotalLeaseCount_Type()
)
jnxJdhcpv6RelayTotalLeaseCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6RelayTotalLeaseCount.setStatus("current")
_JnxJdhcpv6RelayIfcStats_ObjectIdentity = ObjectIdentity
jnxJdhcpv6RelayIfcStats = _JnxJdhcpv6RelayIfcStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 3, 2)
)
_JnxJdhcpv6RelayIfcStatsTable_Object = MibTable
jnxJdhcpv6RelayIfcStatsTable = _JnxJdhcpv6RelayIfcStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 3, 2, 1)
)
if mibBuilder.loadTexts:
    jnxJdhcpv6RelayIfcStatsTable.setStatus("current")
_JnxJdhcpv6RelayIfcStatsEntry_Object = MibTableRow
jnxJdhcpv6RelayIfcStatsEntry = _JnxJdhcpv6RelayIfcStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 3, 2, 1, 1)
)
jnxJdhcpv6RelayIfcStatsEntry.setIndexNames(
    (0, "JUNIPER-JDHCPV6-MIB", "jnxJdhcpv6RelayIfcStatsIfIndex"),
)
if mibBuilder.loadTexts:
    jnxJdhcpv6RelayIfcStatsEntry.setStatus("current")
_JnxJdhcpv6RelayIfcStatsIfIndex_Type = InterfaceIndex
_JnxJdhcpv6RelayIfcStatsIfIndex_Object = MibTableColumn
jnxJdhcpv6RelayIfcStatsIfIndex = _JnxJdhcpv6RelayIfcStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 3, 2, 1, 1, 1),
    _JnxJdhcpv6RelayIfcStatsIfIndex_Type()
)
jnxJdhcpv6RelayIfcStatsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxJdhcpv6RelayIfcStatsIfIndex.setStatus("current")
_JnxJdhcpv6RelayIfcStatsTotalDropped_Type = Counter32
_JnxJdhcpv6RelayIfcStatsTotalDropped_Object = MibTableColumn
jnxJdhcpv6RelayIfcStatsTotalDropped = _JnxJdhcpv6RelayIfcStatsTotalDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 3, 2, 1, 1, 2),
    _JnxJdhcpv6RelayIfcStatsTotalDropped_Type()
)
jnxJdhcpv6RelayIfcStatsTotalDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6RelayIfcStatsTotalDropped.setStatus("current")
_JnxJdhcpv6RelayIfcStatsNoSafdDropped_Type = Counter32
_JnxJdhcpv6RelayIfcStatsNoSafdDropped_Object = MibTableColumn
jnxJdhcpv6RelayIfcStatsNoSafdDropped = _JnxJdhcpv6RelayIfcStatsNoSafdDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 3, 2, 1, 1, 3),
    _JnxJdhcpv6RelayIfcStatsNoSafdDropped_Type()
)
jnxJdhcpv6RelayIfcStatsNoSafdDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6RelayIfcStatsNoSafdDropped.setStatus("current")
_JnxJdhcpv6RelayIfcStatsBadSendDropped_Type = Counter32
_JnxJdhcpv6RelayIfcStatsBadSendDropped_Object = MibTableColumn
jnxJdhcpv6RelayIfcStatsBadSendDropped = _JnxJdhcpv6RelayIfcStatsBadSendDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 3, 2, 1, 1, 4),
    _JnxJdhcpv6RelayIfcStatsBadSendDropped_Type()
)
jnxJdhcpv6RelayIfcStatsBadSendDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6RelayIfcStatsBadSendDropped.setStatus("current")
_JnxJdhcpv6RelayIfcStatsShortPacketDropped_Type = Counter32
_JnxJdhcpv6RelayIfcStatsShortPacketDropped_Object = MibTableColumn
jnxJdhcpv6RelayIfcStatsShortPacketDropped = _JnxJdhcpv6RelayIfcStatsShortPacketDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 3, 2, 1, 1, 5),
    _JnxJdhcpv6RelayIfcStatsShortPacketDropped_Type()
)
jnxJdhcpv6RelayIfcStatsShortPacketDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6RelayIfcStatsShortPacketDropped.setStatus("current")
_JnxJdhcpv6RelayIfcStatsBadMsgtypeDropped_Type = Counter32
_JnxJdhcpv6RelayIfcStatsBadMsgtypeDropped_Object = MibTableColumn
jnxJdhcpv6RelayIfcStatsBadMsgtypeDropped = _JnxJdhcpv6RelayIfcStatsBadMsgtypeDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 3, 2, 1, 1, 6),
    _JnxJdhcpv6RelayIfcStatsBadMsgtypeDropped_Type()
)
jnxJdhcpv6RelayIfcStatsBadMsgtypeDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6RelayIfcStatsBadMsgtypeDropped.setStatus("current")
_JnxJdhcpv6RelayIfcStatsBadOptionsDropped_Type = Counter32
_JnxJdhcpv6RelayIfcStatsBadOptionsDropped_Object = MibTableColumn
jnxJdhcpv6RelayIfcStatsBadOptionsDropped = _JnxJdhcpv6RelayIfcStatsBadOptionsDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 3, 2, 1, 1, 7),
    _JnxJdhcpv6RelayIfcStatsBadOptionsDropped_Type()
)
jnxJdhcpv6RelayIfcStatsBadOptionsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6RelayIfcStatsBadOptionsDropped.setStatus("current")
_JnxJdhcpv6RelayIfcStatsBadSrcAddressDropped_Type = Counter32
_JnxJdhcpv6RelayIfcStatsBadSrcAddressDropped_Object = MibTableColumn
jnxJdhcpv6RelayIfcStatsBadSrcAddressDropped = _JnxJdhcpv6RelayIfcStatsBadSrcAddressDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 3, 2, 1, 1, 8),
    _JnxJdhcpv6RelayIfcStatsBadSrcAddressDropped_Type()
)
jnxJdhcpv6RelayIfcStatsBadSrcAddressDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6RelayIfcStatsBadSrcAddressDropped.setStatus("current")
_JnxJdhcpv6RelayIfcStatsRelayCountDropped_Type = Counter32
_JnxJdhcpv6RelayIfcStatsRelayCountDropped_Object = MibTableColumn
jnxJdhcpv6RelayIfcStatsRelayCountDropped = _JnxJdhcpv6RelayIfcStatsRelayCountDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 3, 2, 1, 1, 9),
    _JnxJdhcpv6RelayIfcStatsRelayCountDropped_Type()
)
jnxJdhcpv6RelayIfcStatsRelayCountDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6RelayIfcStatsRelayCountDropped.setStatus("current")
_JnxJdhcpv6RelayIfcStatsNoClientIdDropped_Type = Counter32
_JnxJdhcpv6RelayIfcStatsNoClientIdDropped_Object = MibTableColumn
jnxJdhcpv6RelayIfcStatsNoClientIdDropped = _JnxJdhcpv6RelayIfcStatsNoClientIdDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 3, 2, 1, 1, 10),
    _JnxJdhcpv6RelayIfcStatsNoClientIdDropped_Type()
)
jnxJdhcpv6RelayIfcStatsNoClientIdDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6RelayIfcStatsNoClientIdDropped.setStatus("current")
_JnxJdhcpv6RelayIfcStatsDeclineReceived_Type = Counter32
_JnxJdhcpv6RelayIfcStatsDeclineReceived_Object = MibTableColumn
jnxJdhcpv6RelayIfcStatsDeclineReceived = _JnxJdhcpv6RelayIfcStatsDeclineReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 3, 2, 1, 1, 11),
    _JnxJdhcpv6RelayIfcStatsDeclineReceived_Type()
)
jnxJdhcpv6RelayIfcStatsDeclineReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6RelayIfcStatsDeclineReceived.setStatus("current")
_JnxJdhcpv6RelayIfcStatsSolicitReceived_Type = Counter32
_JnxJdhcpv6RelayIfcStatsSolicitReceived_Object = MibTableColumn
jnxJdhcpv6RelayIfcStatsSolicitReceived = _JnxJdhcpv6RelayIfcStatsSolicitReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 3, 2, 1, 1, 12),
    _JnxJdhcpv6RelayIfcStatsSolicitReceived_Type()
)
jnxJdhcpv6RelayIfcStatsSolicitReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6RelayIfcStatsSolicitReceived.setStatus("current")
_JnxJdhcpv6RelayIfcStatsInformationRequestReceived_Type = Counter32
_JnxJdhcpv6RelayIfcStatsInformationRequestReceived_Object = MibTableColumn
jnxJdhcpv6RelayIfcStatsInformationRequestReceived = _JnxJdhcpv6RelayIfcStatsInformationRequestReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 3, 2, 1, 1, 13),
    _JnxJdhcpv6RelayIfcStatsInformationRequestReceived_Type()
)
jnxJdhcpv6RelayIfcStatsInformationRequestReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6RelayIfcStatsInformationRequestReceived.setStatus("current")
_JnxJdhcpv6RelayIfcStatsReleaseReceived_Type = Counter32
_JnxJdhcpv6RelayIfcStatsReleaseReceived_Object = MibTableColumn
jnxJdhcpv6RelayIfcStatsReleaseReceived = _JnxJdhcpv6RelayIfcStatsReleaseReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 3, 2, 1, 1, 14),
    _JnxJdhcpv6RelayIfcStatsReleaseReceived_Type()
)
jnxJdhcpv6RelayIfcStatsReleaseReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6RelayIfcStatsReleaseReceived.setStatus("current")
_JnxJdhcpv6RelayIfcStatsRequestReceived_Type = Counter32
_JnxJdhcpv6RelayIfcStatsRequestReceived_Object = MibTableColumn
jnxJdhcpv6RelayIfcStatsRequestReceived = _JnxJdhcpv6RelayIfcStatsRequestReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 3, 2, 1, 1, 15),
    _JnxJdhcpv6RelayIfcStatsRequestReceived_Type()
)
jnxJdhcpv6RelayIfcStatsRequestReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6RelayIfcStatsRequestReceived.setStatus("current")
_JnxJdhcpv6RelayIfcStatsConfirmReceived_Type = Counter32
_JnxJdhcpv6RelayIfcStatsConfirmReceived_Object = MibTableColumn
jnxJdhcpv6RelayIfcStatsConfirmReceived = _JnxJdhcpv6RelayIfcStatsConfirmReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 3, 2, 1, 1, 16),
    _JnxJdhcpv6RelayIfcStatsConfirmReceived_Type()
)
jnxJdhcpv6RelayIfcStatsConfirmReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6RelayIfcStatsConfirmReceived.setStatus("current")
_JnxJdhcpv6RelayIfcStatsRenewReceived_Type = Counter32
_JnxJdhcpv6RelayIfcStatsRenewReceived_Object = MibTableColumn
jnxJdhcpv6RelayIfcStatsRenewReceived = _JnxJdhcpv6RelayIfcStatsRenewReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 3, 2, 1, 1, 17),
    _JnxJdhcpv6RelayIfcStatsRenewReceived_Type()
)
jnxJdhcpv6RelayIfcStatsRenewReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6RelayIfcStatsRenewReceived.setStatus("current")
_JnxJdhcpv6RelayIfcStatsRebindReceived_Type = Counter32
_JnxJdhcpv6RelayIfcStatsRebindReceived_Object = MibTableColumn
jnxJdhcpv6RelayIfcStatsRebindReceived = _JnxJdhcpv6RelayIfcStatsRebindReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 3, 2, 1, 1, 18),
    _JnxJdhcpv6RelayIfcStatsRebindReceived_Type()
)
jnxJdhcpv6RelayIfcStatsRebindReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6RelayIfcStatsRebindReceived.setStatus("current")
_JnxJdhcpv6RelayIfcStatsRelayForwReceived_Type = Counter32
_JnxJdhcpv6RelayIfcStatsRelayForwReceived_Object = MibTableColumn
jnxJdhcpv6RelayIfcStatsRelayForwReceived = _JnxJdhcpv6RelayIfcStatsRelayForwReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 3, 2, 1, 1, 19),
    _JnxJdhcpv6RelayIfcStatsRelayForwReceived_Type()
)
jnxJdhcpv6RelayIfcStatsRelayForwReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6RelayIfcStatsRelayForwReceived.setStatus("current")
_JnxJdhcpv6RelayIfcStatsRelayReplReceived_Type = Counter32
_JnxJdhcpv6RelayIfcStatsRelayReplReceived_Object = MibTableColumn
jnxJdhcpv6RelayIfcStatsRelayReplReceived = _JnxJdhcpv6RelayIfcStatsRelayReplReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 3, 2, 1, 1, 20),
    _JnxJdhcpv6RelayIfcStatsRelayReplReceived_Type()
)
jnxJdhcpv6RelayIfcStatsRelayReplReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6RelayIfcStatsRelayReplReceived.setStatus("current")
_JnxJdhcpv6RelayIfcStatsAdvertiseSent_Type = Counter32
_JnxJdhcpv6RelayIfcStatsAdvertiseSent_Object = MibTableColumn
jnxJdhcpv6RelayIfcStatsAdvertiseSent = _JnxJdhcpv6RelayIfcStatsAdvertiseSent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 3, 2, 1, 1, 21),
    _JnxJdhcpv6RelayIfcStatsAdvertiseSent_Type()
)
jnxJdhcpv6RelayIfcStatsAdvertiseSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6RelayIfcStatsAdvertiseSent.setStatus("current")
_JnxJdhcpv6RelayIfcStatsReplySent_Type = Counter32
_JnxJdhcpv6RelayIfcStatsReplySent_Object = MibTableColumn
jnxJdhcpv6RelayIfcStatsReplySent = _JnxJdhcpv6RelayIfcStatsReplySent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 3, 2, 1, 1, 22),
    _JnxJdhcpv6RelayIfcStatsReplySent_Type()
)
jnxJdhcpv6RelayIfcStatsReplySent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6RelayIfcStatsReplySent.setStatus("current")
_JnxJdhcpv6RelayIfcStatsReconfigureSent_Type = Counter32
_JnxJdhcpv6RelayIfcStatsReconfigureSent_Object = MibTableColumn
jnxJdhcpv6RelayIfcStatsReconfigureSent = _JnxJdhcpv6RelayIfcStatsReconfigureSent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 3, 2, 1, 1, 23),
    _JnxJdhcpv6RelayIfcStatsReconfigureSent_Type()
)
jnxJdhcpv6RelayIfcStatsReconfigureSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6RelayIfcStatsReconfigureSent.setStatus("current")
_JnxJdhcpv6RelayIfcStatsTotalLeaseCount_Type = Counter32
_JnxJdhcpv6RelayIfcStatsTotalLeaseCount_Object = MibTableColumn
jnxJdhcpv6RelayIfcStatsTotalLeaseCount = _JnxJdhcpv6RelayIfcStatsTotalLeaseCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 3, 2, 1, 1, 24),
    _JnxJdhcpv6RelayIfcStatsTotalLeaseCount_Type()
)
jnxJdhcpv6RelayIfcStatsTotalLeaseCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6RelayIfcStatsTotalLeaseCount.setStatus("current")
_JnxJdhcpv6RelayIfcStatsStrictReconfigDropped_Type = Counter32
_JnxJdhcpv6RelayIfcStatsStrictReconfigDropped_Object = MibTableColumn
jnxJdhcpv6RelayIfcStatsStrictReconfigDropped = _JnxJdhcpv6RelayIfcStatsStrictReconfigDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 3, 2, 1, 1, 25),
    _JnxJdhcpv6RelayIfcStatsStrictReconfigDropped_Type()
)
jnxJdhcpv6RelayIfcStatsStrictReconfigDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6RelayIfcStatsStrictReconfigDropped.setStatus("current")
_JnxJdhcpv6RelayIfcStatsAuthenticationDropped_Type = Counter32
_JnxJdhcpv6RelayIfcStatsAuthenticationDropped_Object = MibTableColumn
jnxJdhcpv6RelayIfcStatsAuthenticationDropped = _JnxJdhcpv6RelayIfcStatsAuthenticationDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 3, 2, 1, 1, 26),
    _JnxJdhcpv6RelayIfcStatsAuthenticationDropped_Type()
)
jnxJdhcpv6RelayIfcStatsAuthenticationDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6RelayIfcStatsAuthenticationDropped.setStatus("current")
_JnxJdhcpv6RelayIfcStatsDynamicProfileDropped_Type = Counter32
_JnxJdhcpv6RelayIfcStatsDynamicProfileDropped_Object = MibTableColumn
jnxJdhcpv6RelayIfcStatsDynamicProfileDropped = _JnxJdhcpv6RelayIfcStatsDynamicProfileDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 3, 2, 1, 1, 27),
    _JnxJdhcpv6RelayIfcStatsDynamicProfileDropped_Type()
)
jnxJdhcpv6RelayIfcStatsDynamicProfileDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6RelayIfcStatsDynamicProfileDropped.setStatus("current")
_JnxJdhcpv6RelayIfcStatsLicenseDropped_Type = Counter32
_JnxJdhcpv6RelayIfcStatsLicenseDropped_Object = MibTableColumn
jnxJdhcpv6RelayIfcStatsLicenseDropped = _JnxJdhcpv6RelayIfcStatsLicenseDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 3, 2, 1, 1, 28),
    _JnxJdhcpv6RelayIfcStatsLicenseDropped_Type()
)
jnxJdhcpv6RelayIfcStatsLicenseDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6RelayIfcStatsLicenseDropped.setStatus("current")

# Managed Objects groups


# Notification objects

jnxJdhcpv6LocalServerInterfaceLimitExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 3, 1)
)
jnxJdhcpv6LocalServerInterfaceLimitExceeded.setObjects(
      *(("JUNIPER-JDHCPV6-MIB", "jnxJdhcpv6RouterName"),
        ("JUNIPER-JDHCPV6-MIB", "jnxJdhcpv6LocalServerInterfaceName"),
        ("JUNIPER-JDHCPV6-MIB", "jnxJdhcpv6LocalServerInterfaceLimit"))
)
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerInterfaceLimitExceeded.setStatus(
        "current"
    )

jnxJdhcpv6LocalServerInterfaceLimitAbated = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 3, 2)
)
jnxJdhcpv6LocalServerInterfaceLimitAbated.setObjects(
      *(("JUNIPER-JDHCPV6-MIB", "jnxJdhcpv6RouterName"),
        ("JUNIPER-JDHCPV6-MIB", "jnxJdhcpv6LocalServerInterfaceName"),
        ("JUNIPER-JDHCPV6-MIB", "jnxJdhcpv6LocalServerInterfaceLimit"))
)
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerInterfaceLimitAbated.setStatus(
        "current"
    )

jnxJdhcpv6LocalServerHealth = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 3, 4)
)
jnxJdhcpv6LocalServerHealth.setObjects(
      *(("JUNIPER-JDHCPV6-MIB", "jnxJdhcpv6RouterName"),
        ("JUNIPER-JDHCPV6-MIB", "jnxJdhcpv6LocalServerEventSeverity"),
        ("JUNIPER-JDHCPV6-MIB", "jnxJdhcpv6LocalServerEventString"))
)
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerHealth.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-JDHCPV6-MIB",
    **{"jnxJdhcpv6MIB": jnxJdhcpv6MIB,
       "jnxJdhcpv6Objects": jnxJdhcpv6Objects,
       "jnxJdhcpv6LocalServerObjects": jnxJdhcpv6LocalServerObjects,
       "jnxJdhcpv6LocalServerStatistics": jnxJdhcpv6LocalServerStatistics,
       "jnxJdhcpv6LocalServerTotalDropped": jnxJdhcpv6LocalServerTotalDropped,
       "jnxJdhcpv6LocalServerNoSafdDropped": jnxJdhcpv6LocalServerNoSafdDropped,
       "jnxJdhcpv6LocalServerBadSendDropped": jnxJdhcpv6LocalServerBadSendDropped,
       "jnxJdhcpv6LocalServerShortPacketDropped": jnxJdhcpv6LocalServerShortPacketDropped,
       "jnxJdhcpv6LocalServerBadMsgtypeDropped": jnxJdhcpv6LocalServerBadMsgtypeDropped,
       "jnxJdhcpv6LocalServerBadOptionsDropped": jnxJdhcpv6LocalServerBadOptionsDropped,
       "jnxJdhcpv6LocalServerBadSrcAddressDropped": jnxJdhcpv6LocalServerBadSrcAddressDropped,
       "jnxJdhcpv6LocalServerRelayHopCountDropped": jnxJdhcpv6LocalServerRelayHopCountDropped,
       "jnxJdhcpv6LocalServerNoClientIdDropped": jnxJdhcpv6LocalServerNoClientIdDropped,
       "jnxJdhcpv6LocalServerDeclineReceived": jnxJdhcpv6LocalServerDeclineReceived,
       "jnxJdhcpv6LocalServerSolicitReceived": jnxJdhcpv6LocalServerSolicitReceived,
       "jnxJdhcpv6LocalServerInformationRequestReceived": jnxJdhcpv6LocalServerInformationRequestReceived,
       "jnxJdhcpv6LocalServerReleaseReceived": jnxJdhcpv6LocalServerReleaseReceived,
       "jnxJdhcpv6LocalServerRequestReceived": jnxJdhcpv6LocalServerRequestReceived,
       "jnxJdhcpv6LocalServerConfirmReceived": jnxJdhcpv6LocalServerConfirmReceived,
       "jnxJdhcpv6LocalServerRenewReceived": jnxJdhcpv6LocalServerRenewReceived,
       "jnxJdhcpv6LocalServerRebindReceived": jnxJdhcpv6LocalServerRebindReceived,
       "jnxJdhcpv6LocalServerRelayForwReceived": jnxJdhcpv6LocalServerRelayForwReceived,
       "jnxJdhcpv6LocalServerRelayReplReceived": jnxJdhcpv6LocalServerRelayReplReceived,
       "jnxJdhcpv6LocalServerAdvertiseSent": jnxJdhcpv6LocalServerAdvertiseSent,
       "jnxJdhcpv6LocalServerReplySent": jnxJdhcpv6LocalServerReplySent,
       "jnxJdhcpv6LocalServerReconfigureSent": jnxJdhcpv6LocalServerReconfigureSent,
       "jnxJdhcpv6LocalServerTotalLeaseCount": jnxJdhcpv6LocalServerTotalLeaseCount,
       "jnxJdhcpv6LocalServerBindings": jnxJdhcpv6LocalServerBindings,
       "jnxJdhcpv6LocalServerBindingsTable": jnxJdhcpv6LocalServerBindingsTable,
       "jnxJdhcpv6LocalServerBindingsEntry": jnxJdhcpv6LocalServerBindingsEntry,
       "jnxJdhcpv6LocalServerBindingsPrefix": jnxJdhcpv6LocalServerBindingsPrefix,
       "jnxJdhcpv6LocalServerBindingsLength": jnxJdhcpv6LocalServerBindingsLength,
       "jnxJdhcpv6LocalServerBindingsState": jnxJdhcpv6LocalServerBindingsState,
       "jnxJdhcpv6LocalServerBindingsLeaseEndTime": jnxJdhcpv6LocalServerBindingsLeaseEndTime,
       "jnxJdhcpv6LocalServerBindingsLeaseExpireTime": jnxJdhcpv6LocalServerBindingsLeaseExpireTime,
       "jnxJdhcpv6LocalServerBindingsLeaseStartTime": jnxJdhcpv6LocalServerBindingsLeaseStartTime,
       "jnxJdhcpv6LocalServerBindingsIncomingClientInterface": jnxJdhcpv6LocalServerBindingsIncomingClientInterface,
       "jnxJdhcpv6LocalServerBindingsClientInterfaceVlanId": jnxJdhcpv6LocalServerBindingsClientInterfaceVlanId,
       "jnxJdhcpv6LocalServerBindingsDemuxInterfaceName": jnxJdhcpv6LocalServerBindingsDemuxInterfaceName,
       "jnxJdhcpv6LocalServerBindingsServerIpAddress": jnxJdhcpv6LocalServerBindingsServerIpAddress,
       "jnxJdhcpv6LocalServerBindingsBootpRelayAddress": jnxJdhcpv6LocalServerBindingsBootpRelayAddress,
       "jnxJdhcpv6LocalServerBindingsPreviousBootpRelayAddress": jnxJdhcpv6LocalServerBindingsPreviousBootpRelayAddress,
       "jnxJdhcpv6LocalServerBindingsClientPoolName": jnxJdhcpv6LocalServerBindingsClientPoolName,
       "jnxJdhcpv6LocalServerBindingsClientProfileName": jnxJdhcpv6LocalServerBindingsClientProfileName,
       "jnxJdhcpv6LocalServerTraps": jnxJdhcpv6LocalServerTraps,
       "jnxJdhcpv6LocalServerInterfaceLimitExceeded": jnxJdhcpv6LocalServerInterfaceLimitExceeded,
       "jnxJdhcpv6LocalServerInterfaceLimitAbated": jnxJdhcpv6LocalServerInterfaceLimitAbated,
       "jnxJdhcpv6LocalServerHealth": jnxJdhcpv6LocalServerHealth,
       "jnxJdhcpv6LocalServerTrapVars": jnxJdhcpv6LocalServerTrapVars,
       "jnxJdhcpv6RouterName": jnxJdhcpv6RouterName,
       "jnxJdhcpv6LocalServerInterfaceName": jnxJdhcpv6LocalServerInterfaceName,
       "jnxJdhcpv6LocalServerInterfaceLimit": jnxJdhcpv6LocalServerInterfaceLimit,
       "jnxJdhcpv6LocalServerEventSeverity": jnxJdhcpv6LocalServerEventSeverity,
       "jnxJdhcpv6LocalServerEventString": jnxJdhcpv6LocalServerEventString,
       "jnxJdhcpv6LocalServerIfcStats": jnxJdhcpv6LocalServerIfcStats,
       "jnxJdhcpv6LocalServerIfcStatsTable": jnxJdhcpv6LocalServerIfcStatsTable,
       "jnxJdhcpv6LocalServerIfcStatsEntry": jnxJdhcpv6LocalServerIfcStatsEntry,
       "jnxJdhcpv6LocalServerIfcStatsIfIndex": jnxJdhcpv6LocalServerIfcStatsIfIndex,
       "jnxJdhcpv6LocalServerIfcStatsTotalDropped": jnxJdhcpv6LocalServerIfcStatsTotalDropped,
       "jnxJdhcpv6LocalServerIfcStatsNoSafdDropped": jnxJdhcpv6LocalServerIfcStatsNoSafdDropped,
       "jnxJdhcpv6LocalServerIfcStatsBadSendDropped": jnxJdhcpv6LocalServerIfcStatsBadSendDropped,
       "jnxJdhcpv6LocalServerIfcStatsShortPacketDropped": jnxJdhcpv6LocalServerIfcStatsShortPacketDropped,
       "jnxJdhcpv6LocalServerIfcStatsBadMsgtypeDropped": jnxJdhcpv6LocalServerIfcStatsBadMsgtypeDropped,
       "jnxJdhcpv6LocalServerIfcStatsBadOptionsDropped": jnxJdhcpv6LocalServerIfcStatsBadOptionsDropped,
       "jnxJdhcpv6LocalServerIfcStatsBadSrcAddressDropped": jnxJdhcpv6LocalServerIfcStatsBadSrcAddressDropped,
       "jnxJdhcpv6LocalServerIfcStatsRelayCountDropped": jnxJdhcpv6LocalServerIfcStatsRelayCountDropped,
       "jnxJdhcpv6LocalServerIfcStatsNoClientIdDropped": jnxJdhcpv6LocalServerIfcStatsNoClientIdDropped,
       "jnxJdhcpv6LocalServerIfcStatsDeclineReceived": jnxJdhcpv6LocalServerIfcStatsDeclineReceived,
       "jnxJdhcpv6LocalServerIfcStatsSolicitReceived": jnxJdhcpv6LocalServerIfcStatsSolicitReceived,
       "jnxJdhcpv6LocalServerIfcStatsInformationRequestReceived": jnxJdhcpv6LocalServerIfcStatsInformationRequestReceived,
       "jnxJdhcpv6LocalServerIfcStatsReleaseReceived": jnxJdhcpv6LocalServerIfcStatsReleaseReceived,
       "jnxJdhcpv6LocalServerIfcStatsRequestReceived": jnxJdhcpv6LocalServerIfcStatsRequestReceived,
       "jnxJdhcpv6LocalServerIfcStatsConfirmReceived": jnxJdhcpv6LocalServerIfcStatsConfirmReceived,
       "jnxJdhcpv6LocalServerIfcStatsRenewReceived": jnxJdhcpv6LocalServerIfcStatsRenewReceived,
       "jnxJdhcpv6LocalServerIfcStatsRebindReceived": jnxJdhcpv6LocalServerIfcStatsRebindReceived,
       "jnxJdhcpv6LocalServerIfcStatsRelayForwReceived": jnxJdhcpv6LocalServerIfcStatsRelayForwReceived,
       "jnxJdhcpv6LocalServerIfcStatsRelayReplReceived": jnxJdhcpv6LocalServerIfcStatsRelayReplReceived,
       "jnxJdhcpv6LocalServerIfcStatsAdvertiseSent": jnxJdhcpv6LocalServerIfcStatsAdvertiseSent,
       "jnxJdhcpv6LocalServerIfcStatsReplySent": jnxJdhcpv6LocalServerIfcStatsReplySent,
       "jnxJdhcpv6LocalServerIfcStatsReconfigureSent": jnxJdhcpv6LocalServerIfcStatsReconfigureSent,
       "jnxJdhcpv6LocalServerIfcStatsTotalLeaseCount": jnxJdhcpv6LocalServerIfcStatsTotalLeaseCount,
       "jnxJdhcpv6LocalServerIfcStatsStrictReconfigDropped": jnxJdhcpv6LocalServerIfcStatsStrictReconfigDropped,
       "jnxJdhcpv6LocalServerIfcStatsAuthenticationDropped": jnxJdhcpv6LocalServerIfcStatsAuthenticationDropped,
       "jnxJdhcpv6LocalServerIfcStatsDynamicProfileDropped": jnxJdhcpv6LocalServerIfcStatsDynamicProfileDropped,
       "jnxJdhcpv6LocalServerIfcStatsLicenseDropped": jnxJdhcpv6LocalServerIfcStatsLicenseDropped,
       "jnxJdhcpv6RelayObjects": jnxJdhcpv6RelayObjects,
       "jnxJdhcpv6RelayStatistics": jnxJdhcpv6RelayStatistics,
       "jnxJdhcpv6RelayTotalDropped": jnxJdhcpv6RelayTotalDropped,
       "jnxJdhcpv6RelayNoSafdDropped": jnxJdhcpv6RelayNoSafdDropped,
       "jnxJdhcpv6RelayBadSendDropped": jnxJdhcpv6RelayBadSendDropped,
       "jnxJdhcpv6RelayShortPacketDropped": jnxJdhcpv6RelayShortPacketDropped,
       "jnxJdhcpv6RelayBadMsgtypeDropped": jnxJdhcpv6RelayBadMsgtypeDropped,
       "jnxJdhcpv6RelayBadOptionsDropped": jnxJdhcpv6RelayBadOptionsDropped,
       "jnxJdhcpv6RelayBadSrcAddressDropped": jnxJdhcpv6RelayBadSrcAddressDropped,
       "jnxJdhcpv6RelayRelayHopCountDropped": jnxJdhcpv6RelayRelayHopCountDropped,
       "jnxJdhcpv6RelayNoClientIdDropped": jnxJdhcpv6RelayNoClientIdDropped,
       "jnxJdhcpv6RelayDeclineReceived": jnxJdhcpv6RelayDeclineReceived,
       "jnxJdhcpv6RelaySolicitReceived": jnxJdhcpv6RelaySolicitReceived,
       "jnxJdhcpv6RelayInformationRequestReceived": jnxJdhcpv6RelayInformationRequestReceived,
       "jnxJdhcpv6RelayReleaseReceived": jnxJdhcpv6RelayReleaseReceived,
       "jnxJdhcpv6RelayRequestReceived": jnxJdhcpv6RelayRequestReceived,
       "jnxJdhcpv6RelayConfirmReceived": jnxJdhcpv6RelayConfirmReceived,
       "jnxJdhcpv6RelayRenewReceived": jnxJdhcpv6RelayRenewReceived,
       "jnxJdhcpv6RelayRebindReceived": jnxJdhcpv6RelayRebindReceived,
       "jnxJdhcpv6RelayRelayForwReceived": jnxJdhcpv6RelayRelayForwReceived,
       "jnxJdhcpv6RelayRelayReplReceived": jnxJdhcpv6RelayRelayReplReceived,
       "jnxJdhcpv6RelayAdvertiseSent": jnxJdhcpv6RelayAdvertiseSent,
       "jnxJdhcpv6RelayReplySent": jnxJdhcpv6RelayReplySent,
       "jnxJdhcpv6RelayReconfigureSent": jnxJdhcpv6RelayReconfigureSent,
       "jnxJdhcpv6RelayTotalLeaseCount": jnxJdhcpv6RelayTotalLeaseCount,
       "jnxJdhcpv6RelayIfcStats": jnxJdhcpv6RelayIfcStats,
       "jnxJdhcpv6RelayIfcStatsTable": jnxJdhcpv6RelayIfcStatsTable,
       "jnxJdhcpv6RelayIfcStatsEntry": jnxJdhcpv6RelayIfcStatsEntry,
       "jnxJdhcpv6RelayIfcStatsIfIndex": jnxJdhcpv6RelayIfcStatsIfIndex,
       "jnxJdhcpv6RelayIfcStatsTotalDropped": jnxJdhcpv6RelayIfcStatsTotalDropped,
       "jnxJdhcpv6RelayIfcStatsNoSafdDropped": jnxJdhcpv6RelayIfcStatsNoSafdDropped,
       "jnxJdhcpv6RelayIfcStatsBadSendDropped": jnxJdhcpv6RelayIfcStatsBadSendDropped,
       "jnxJdhcpv6RelayIfcStatsShortPacketDropped": jnxJdhcpv6RelayIfcStatsShortPacketDropped,
       "jnxJdhcpv6RelayIfcStatsBadMsgtypeDropped": jnxJdhcpv6RelayIfcStatsBadMsgtypeDropped,
       "jnxJdhcpv6RelayIfcStatsBadOptionsDropped": jnxJdhcpv6RelayIfcStatsBadOptionsDropped,
       "jnxJdhcpv6RelayIfcStatsBadSrcAddressDropped": jnxJdhcpv6RelayIfcStatsBadSrcAddressDropped,
       "jnxJdhcpv6RelayIfcStatsRelayCountDropped": jnxJdhcpv6RelayIfcStatsRelayCountDropped,
       "jnxJdhcpv6RelayIfcStatsNoClientIdDropped": jnxJdhcpv6RelayIfcStatsNoClientIdDropped,
       "jnxJdhcpv6RelayIfcStatsDeclineReceived": jnxJdhcpv6RelayIfcStatsDeclineReceived,
       "jnxJdhcpv6RelayIfcStatsSolicitReceived": jnxJdhcpv6RelayIfcStatsSolicitReceived,
       "jnxJdhcpv6RelayIfcStatsInformationRequestReceived": jnxJdhcpv6RelayIfcStatsInformationRequestReceived,
       "jnxJdhcpv6RelayIfcStatsReleaseReceived": jnxJdhcpv6RelayIfcStatsReleaseReceived,
       "jnxJdhcpv6RelayIfcStatsRequestReceived": jnxJdhcpv6RelayIfcStatsRequestReceived,
       "jnxJdhcpv6RelayIfcStatsConfirmReceived": jnxJdhcpv6RelayIfcStatsConfirmReceived,
       "jnxJdhcpv6RelayIfcStatsRenewReceived": jnxJdhcpv6RelayIfcStatsRenewReceived,
       "jnxJdhcpv6RelayIfcStatsRebindReceived": jnxJdhcpv6RelayIfcStatsRebindReceived,
       "jnxJdhcpv6RelayIfcStatsRelayForwReceived": jnxJdhcpv6RelayIfcStatsRelayForwReceived,
       "jnxJdhcpv6RelayIfcStatsRelayReplReceived": jnxJdhcpv6RelayIfcStatsRelayReplReceived,
       "jnxJdhcpv6RelayIfcStatsAdvertiseSent": jnxJdhcpv6RelayIfcStatsAdvertiseSent,
       "jnxJdhcpv6RelayIfcStatsReplySent": jnxJdhcpv6RelayIfcStatsReplySent,
       "jnxJdhcpv6RelayIfcStatsReconfigureSent": jnxJdhcpv6RelayIfcStatsReconfigureSent,
       "jnxJdhcpv6RelayIfcStatsTotalLeaseCount": jnxJdhcpv6RelayIfcStatsTotalLeaseCount,
       "jnxJdhcpv6RelayIfcStatsStrictReconfigDropped": jnxJdhcpv6RelayIfcStatsStrictReconfigDropped,
       "jnxJdhcpv6RelayIfcStatsAuthenticationDropped": jnxJdhcpv6RelayIfcStatsAuthenticationDropped,
       "jnxJdhcpv6RelayIfcStatsDynamicProfileDropped": jnxJdhcpv6RelayIfcStatsDynamicProfileDropped,
       "jnxJdhcpv6RelayIfcStatsLicenseDropped": jnxJdhcpv6RelayIfcStatsLicenseDropped}
)
