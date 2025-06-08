# SNMP MIB module (BELAIR-TUNNEL) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ericsson_15768/BELAIR-TUNNEL.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 16:08:43 2025
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

(belairProtocols,) = mibBuilder.importSymbols(
    "BELAIR-SMI",
    "belairProtocols")

(BelAirAdminState,
 BelAirRowStatus,
 BelAirVlanIdOrZero) = mibBuilder.importSymbols(
    "BELAIR-TC",
    "BelAirAdminState",
    "BelAirRowStatus",
    "BelAirVlanIdOrZero")

(PerfCurrentCount,
 PerfIntervalCount,
 PerfTotalCount) = mibBuilder.importSymbols(
    "PerfHist-TC-MIB",
    "PerfCurrentCount",
    "PerfIntervalCount",
    "PerfTotalCount")

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

belairTunnelMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 5, 1)
)
if mibBuilder.loadTexts:
    belairTunnelMib.setRevisions(
        ("2009-09-28 15:55",
         "2009-05-28 09:30",
         "2008-11-26 14:45")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BelairTunnelObjects_ObjectIdentity = ObjectIdentity
belairTunnelObjects = _BelairTunnelObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 5, 1, 1)
)
_BaTunnelEngineTable_Object = MibTable
baTunnelEngineTable = _BaTunnelEngineTable_Object(
    (1, 3, 6, 1, 4, 1, 15768, 5, 1, 1, 1)
)
if mibBuilder.loadTexts:
    baTunnelEngineTable.setStatus("current")
_BaTunnelEngineEntry_Object = MibTableRow
baTunnelEngineEntry = _BaTunnelEngineEntry_Object(
    (1, 3, 6, 1, 4, 1, 15768, 5, 1, 1, 1, 1)
)
baTunnelEngineEntry.setIndexNames(
    (0, "BELAIR-TUNNEL", "baTunnelEngineIndex"),
)
if mibBuilder.loadTexts:
    baTunnelEngineEntry.setStatus("current")


class _BaTunnelEngineIndex_Type(Integer32):
    """Custom type baTunnelEngineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_BaTunnelEngineIndex_Type.__name__ = "Integer32"
_BaTunnelEngineIndex_Object = MibTableColumn
baTunnelEngineIndex = _BaTunnelEngineIndex_Object(
    (1, 3, 6, 1, 4, 1, 15768, 5, 1, 1, 1, 1, 1),
    _BaTunnelEngineIndex_Type()
)
baTunnelEngineIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    baTunnelEngineIndex.setStatus("current")
_BaTunnelEngineAdminState_Type = BelAirAdminState
_BaTunnelEngineAdminState_Object = MibTableColumn
baTunnelEngineAdminState = _BaTunnelEngineAdminState_Object(
    (1, 3, 6, 1, 4, 1, 15768, 5, 1, 1, 1, 1, 2),
    _BaTunnelEngineAdminState_Type()
)
baTunnelEngineAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    baTunnelEngineAdminState.setStatus("current")
_BaTunnelEngineLocalIp_Type = IpAddress
_BaTunnelEngineLocalIp_Object = MibTableColumn
baTunnelEngineLocalIp = _BaTunnelEngineLocalIp_Object(
    (1, 3, 6, 1, 4, 1, 15768, 5, 1, 1, 1, 1, 3),
    _BaTunnelEngineLocalIp_Type()
)
baTunnelEngineLocalIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    baTunnelEngineLocalIp.setStatus("current")
_BaTunnelEngineNetMask_Type = IpAddress
_BaTunnelEngineNetMask_Object = MibTableColumn
baTunnelEngineNetMask = _BaTunnelEngineNetMask_Object(
    (1, 3, 6, 1, 4, 1, 15768, 5, 1, 1, 1, 1, 4),
    _BaTunnelEngineNetMask_Type()
)
baTunnelEngineNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    baTunnelEngineNetMask.setStatus("current")
_BaTunnelEngineGateway_Type = IpAddress
_BaTunnelEngineGateway_Object = MibTableColumn
baTunnelEngineGateway = _BaTunnelEngineGateway_Object(
    (1, 3, 6, 1, 4, 1, 15768, 5, 1, 1, 1, 1, 5),
    _BaTunnelEngineGateway_Type()
)
baTunnelEngineGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    baTunnelEngineGateway.setStatus("current")
_BaTunnelEngineVlanId_Type = BelAirVlanIdOrZero
_BaTunnelEngineVlanId_Object = MibTableColumn
baTunnelEngineVlanId = _BaTunnelEngineVlanId_Object(
    (1, 3, 6, 1, 4, 1, 15768, 5, 1, 1, 1, 1, 6),
    _BaTunnelEngineVlanId_Type()
)
baTunnelEngineVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    baTunnelEngineVlanId.setStatus("current")


class _BaTunnelEngineMode_Type(Integer32):
    """Custom type baTunnelEngineMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("egress", 2))
    )


_BaTunnelEngineMode_Type.__name__ = "Integer32"
_BaTunnelEngineMode_Object = MibTableColumn
baTunnelEngineMode = _BaTunnelEngineMode_Object(
    (1, 3, 6, 1, 4, 1, 15768, 5, 1, 1, 1, 1, 7),
    _BaTunnelEngineMode_Type()
)
baTunnelEngineMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    baTunnelEngineMode.setStatus("current")
_BaTunnelConfigTable_Object = MibTable
baTunnelConfigTable = _BaTunnelConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 15768, 5, 1, 1, 2)
)
if mibBuilder.loadTexts:
    baTunnelConfigTable.setStatus("current")
_BaTunnelConfigEntry_Object = MibTableRow
baTunnelConfigEntry = _BaTunnelConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 15768, 5, 1, 1, 2, 1)
)
baTunnelConfigEntry.setIndexNames(
    (0, "BELAIR-TUNNEL", "baTunnelEngineIndex"),
    (0, "BELAIR-TUNNEL", "baTunnelIndex"),
)
if mibBuilder.loadTexts:
    baTunnelConfigEntry.setStatus("current")


class _BaTunnelIndex_Type(Integer32):
    """Custom type baTunnelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_BaTunnelIndex_Type.__name__ = "Integer32"
_BaTunnelIndex_Object = MibTableColumn
baTunnelIndex = _BaTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 15768, 5, 1, 1, 2, 1, 1),
    _BaTunnelIndex_Type()
)
baTunnelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    baTunnelIndex.setStatus("current")


class _BaTunnelPrimaryName_Type(OctetString):
    """Custom type baTunnelPrimaryName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BaTunnelPrimaryName_Type.__name__ = "OctetString"
_BaTunnelPrimaryName_Object = MibTableColumn
baTunnelPrimaryName = _BaTunnelPrimaryName_Object(
    (1, 3, 6, 1, 4, 1, 15768, 5, 1, 1, 2, 1, 2),
    _BaTunnelPrimaryName_Type()
)
baTunnelPrimaryName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    baTunnelPrimaryName.setStatus("current")


class _BaTunnelSecondaryName_Type(OctetString):
    """Custom type baTunnelSecondaryName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BaTunnelSecondaryName_Type.__name__ = "OctetString"
_BaTunnelSecondaryName_Object = MibTableColumn
baTunnelSecondaryName = _BaTunnelSecondaryName_Object(
    (1, 3, 6, 1, 4, 1, 15768, 5, 1, 1, 2, 1, 3),
    _BaTunnelSecondaryName_Type()
)
baTunnelSecondaryName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    baTunnelSecondaryName.setStatus("current")
_BaTunnelAuthenState_Type = BelAirAdminState
_BaTunnelAuthenState_Object = MibTableColumn
baTunnelAuthenState = _BaTunnelAuthenState_Object(
    (1, 3, 6, 1, 4, 1, 15768, 5, 1, 1, 2, 1, 4),
    _BaTunnelAuthenState_Type()
)
baTunnelAuthenState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    baTunnelAuthenState.setStatus("current")
_BaTunnelPrimaryPeerIp_Type = IpAddress
_BaTunnelPrimaryPeerIp_Object = MibTableColumn
baTunnelPrimaryPeerIp = _BaTunnelPrimaryPeerIp_Object(
    (1, 3, 6, 1, 4, 1, 15768, 5, 1, 1, 2, 1, 5),
    _BaTunnelPrimaryPeerIp_Type()
)
baTunnelPrimaryPeerIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    baTunnelPrimaryPeerIp.setStatus("current")


class _BaTunnelPrimarySecret_Type(OctetString):
    """Custom type baTunnelPrimarySecret based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BaTunnelPrimarySecret_Type.__name__ = "OctetString"
_BaTunnelPrimarySecret_Object = MibTableColumn
baTunnelPrimarySecret = _BaTunnelPrimarySecret_Object(
    (1, 3, 6, 1, 4, 1, 15768, 5, 1, 1, 2, 1, 6),
    _BaTunnelPrimarySecret_Type()
)
baTunnelPrimarySecret.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    baTunnelPrimarySecret.setStatus("current")


class _BaTunnelPrimaryPppName_Type(OctetString):
    """Custom type baTunnelPrimaryPppName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BaTunnelPrimaryPppName_Type.__name__ = "OctetString"
_BaTunnelPrimaryPppName_Object = MibTableColumn
baTunnelPrimaryPppName = _BaTunnelPrimaryPppName_Object(
    (1, 3, 6, 1, 4, 1, 15768, 5, 1, 1, 2, 1, 7),
    _BaTunnelPrimaryPppName_Type()
)
baTunnelPrimaryPppName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    baTunnelPrimaryPppName.setStatus("current")


class _BaTunnelPrimaryPppPassword_Type(OctetString):
    """Custom type baTunnelPrimaryPppPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BaTunnelPrimaryPppPassword_Type.__name__ = "OctetString"
_BaTunnelPrimaryPppPassword_Object = MibTableColumn
baTunnelPrimaryPppPassword = _BaTunnelPrimaryPppPassword_Object(
    (1, 3, 6, 1, 4, 1, 15768, 5, 1, 1, 2, 1, 8),
    _BaTunnelPrimaryPppPassword_Type()
)
baTunnelPrimaryPppPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    baTunnelPrimaryPppPassword.setStatus("current")
_BaTunnelSecondaryPeerIp_Type = IpAddress
_BaTunnelSecondaryPeerIp_Object = MibTableColumn
baTunnelSecondaryPeerIp = _BaTunnelSecondaryPeerIp_Object(
    (1, 3, 6, 1, 4, 1, 15768, 5, 1, 1, 2, 1, 9),
    _BaTunnelSecondaryPeerIp_Type()
)
baTunnelSecondaryPeerIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    baTunnelSecondaryPeerIp.setStatus("current")


class _BaTunnelSecondarySecret_Type(OctetString):
    """Custom type baTunnelSecondarySecret based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BaTunnelSecondarySecret_Type.__name__ = "OctetString"
_BaTunnelSecondarySecret_Object = MibTableColumn
baTunnelSecondarySecret = _BaTunnelSecondarySecret_Object(
    (1, 3, 6, 1, 4, 1, 15768, 5, 1, 1, 2, 1, 10),
    _BaTunnelSecondarySecret_Type()
)
baTunnelSecondarySecret.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    baTunnelSecondarySecret.setStatus("current")


class _BaTunnelSecondaryPppName_Type(OctetString):
    """Custom type baTunnelSecondaryPppName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BaTunnelSecondaryPppName_Type.__name__ = "OctetString"
_BaTunnelSecondaryPppName_Object = MibTableColumn
baTunnelSecondaryPppName = _BaTunnelSecondaryPppName_Object(
    (1, 3, 6, 1, 4, 1, 15768, 5, 1, 1, 2, 1, 11),
    _BaTunnelSecondaryPppName_Type()
)
baTunnelSecondaryPppName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    baTunnelSecondaryPppName.setStatus("current")


class _BaTunnelSecondaryPppPassword_Type(OctetString):
    """Custom type baTunnelSecondaryPppPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BaTunnelSecondaryPppPassword_Type.__name__ = "OctetString"
_BaTunnelSecondaryPppPassword_Object = MibTableColumn
baTunnelSecondaryPppPassword = _BaTunnelSecondaryPppPassword_Object(
    (1, 3, 6, 1, 4, 1, 15768, 5, 1, 1, 2, 1, 12),
    _BaTunnelSecondaryPppPassword_Type()
)
baTunnelSecondaryPppPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    baTunnelSecondaryPppPassword.setStatus("current")
_BaTunnelConfigRowStatus_Type = BelAirRowStatus
_BaTunnelConfigRowStatus_Object = MibTableColumn
baTunnelConfigRowStatus = _BaTunnelConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15768, 5, 1, 1, 2, 1, 13),
    _BaTunnelConfigRowStatus_Type()
)
baTunnelConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    baTunnelConfigRowStatus.setStatus("current")
_BaTunnelRxBandwidthLimit_Type = Unsigned32
_BaTunnelRxBandwidthLimit_Object = MibTableColumn
baTunnelRxBandwidthLimit = _BaTunnelRxBandwidthLimit_Object(
    (1, 3, 6, 1, 4, 1, 15768, 5, 1, 1, 2, 1, 14),
    _BaTunnelRxBandwidthLimit_Type()
)
baTunnelRxBandwidthLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    baTunnelRxBandwidthLimit.setStatus("current")
if mibBuilder.loadTexts:
    baTunnelRxBandwidthLimit.setUnits("bps")
_BaTunnelTxBandwidthLimit_Type = Unsigned32
_BaTunnelTxBandwidthLimit_Object = MibTableColumn
baTunnelTxBandwidthLimit = _BaTunnelTxBandwidthLimit_Object(
    (1, 3, 6, 1, 4, 1, 15768, 5, 1, 1, 2, 1, 15),
    _BaTunnelTxBandwidthLimit_Type()
)
baTunnelTxBandwidthLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    baTunnelTxBandwidthLimit.setStatus("current")
if mibBuilder.loadTexts:
    baTunnelTxBandwidthLimit.setUnits("bps")


class _BaTunnelGroupName_Type(OctetString):
    """Custom type baTunnelGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BaTunnelGroupName_Type.__name__ = "OctetString"
_BaTunnelGroupName_Object = MibTableColumn
baTunnelGroupName = _BaTunnelGroupName_Object(
    (1, 3, 6, 1, 4, 1, 15768, 5, 1, 1, 2, 1, 16),
    _BaTunnelGroupName_Type()
)
baTunnelGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    baTunnelGroupName.setStatus("current")
_BaTunnelRevertive_Type = TruthValue
_BaTunnelRevertive_Object = MibTableColumn
baTunnelRevertive = _BaTunnelRevertive_Object(
    (1, 3, 6, 1, 4, 1, 15768, 5, 1, 1, 2, 1, 17),
    _BaTunnelRevertive_Type()
)
baTunnelRevertive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    baTunnelRevertive.setStatus("current")
_BaTunnelSecondaryAuthenState_Type = BelAirAdminState
_BaTunnelSecondaryAuthenState_Object = MibTableColumn
baTunnelSecondaryAuthenState = _BaTunnelSecondaryAuthenState_Object(
    (1, 3, 6, 1, 4, 1, 15768, 5, 1, 1, 2, 1, 18),
    _BaTunnelSecondaryAuthenState_Type()
)
baTunnelSecondaryAuthenState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    baTunnelSecondaryAuthenState.setStatus("current")
_BaTunnelStatusTable_Object = MibTable
baTunnelStatusTable = _BaTunnelStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 15768, 5, 1, 1, 3)
)
if mibBuilder.loadTexts:
    baTunnelStatusTable.setStatus("current")
_BaTunnelStatusEntry_Object = MibTableRow
baTunnelStatusEntry = _BaTunnelStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 15768, 5, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    baTunnelStatusEntry.setStatus("current")


class _BaTunnelOperStatus_Type(Integer32):
    """Custom type baTunnelOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_BaTunnelOperStatus_Type.__name__ = "Integer32"
_BaTunnelOperStatus_Object = MibTableColumn
baTunnelOperStatus = _BaTunnelOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 15768, 5, 1, 1, 3, 1, 1),
    _BaTunnelOperStatus_Type()
)
baTunnelOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baTunnelOperStatus.setStatus("current")
_BaTunnelUpTime_Type = TimeTicks
_BaTunnelUpTime_Object = MibTableColumn
baTunnelUpTime = _BaTunnelUpTime_Object(
    (1, 3, 6, 1, 4, 1, 15768, 5, 1, 1, 3, 1, 2),
    _BaTunnelUpTime_Type()
)
baTunnelUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baTunnelUpTime.setStatus("current")
_BaTunnelPrimaryActive_Type = TruthValue
_BaTunnelPrimaryActive_Object = MibTableColumn
baTunnelPrimaryActive = _BaTunnelPrimaryActive_Object(
    (1, 3, 6, 1, 4, 1, 15768, 5, 1, 1, 3, 1, 3),
    _BaTunnelPrimaryActive_Type()
)
baTunnelPrimaryActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baTunnelPrimaryActive.setStatus("current")
_BaTunnelSecondaryActive_Type = TruthValue
_BaTunnelSecondaryActive_Object = MibTableColumn
baTunnelSecondaryActive = _BaTunnelSecondaryActive_Object(
    (1, 3, 6, 1, 4, 1, 15768, 5, 1, 1, 3, 1, 4),
    _BaTunnelSecondaryActive_Type()
)
baTunnelSecondaryActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baTunnelSecondaryActive.setStatus("current")
_BaTunnelRxPkts_Type = Counter32
_BaTunnelRxPkts_Object = MibTableColumn
baTunnelRxPkts = _BaTunnelRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 15768, 5, 1, 1, 3, 1, 5),
    _BaTunnelRxPkts_Type()
)
baTunnelRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baTunnelRxPkts.setStatus("current")
_BaTunnelTxPkts_Type = Counter32
_BaTunnelTxPkts_Object = MibTableColumn
baTunnelTxPkts = _BaTunnelTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 15768, 5, 1, 1, 3, 1, 6),
    _BaTunnelTxPkts_Type()
)
baTunnelTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baTunnelTxPkts.setStatus("current")
_BaTunnelRxOctets_Type = Counter32
_BaTunnelRxOctets_Object = MibTableColumn
baTunnelRxOctets = _BaTunnelRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 15768, 5, 1, 1, 3, 1, 7),
    _BaTunnelRxOctets_Type()
)
baTunnelRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baTunnelRxOctets.setStatus("current")
_BaTunnelTxOctets_Type = Counter32
_BaTunnelTxOctets_Object = MibTableColumn
baTunnelTxOctets = _BaTunnelTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 15768, 5, 1, 1, 3, 1, 8),
    _BaTunnelTxOctets_Type()
)
baTunnelTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baTunnelTxOctets.setStatus("current")
_BaTunnelFragmentedPkts_Type = Counter32
_BaTunnelFragmentedPkts_Object = MibTableColumn
baTunnelFragmentedPkts = _BaTunnelFragmentedPkts_Object(
    (1, 3, 6, 1, 4, 1, 15768, 5, 1, 1, 3, 1, 9),
    _BaTunnelFragmentedPkts_Type()
)
baTunnelFragmentedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baTunnelFragmentedPkts.setStatus("current")
_BaTunnelReassembledPkts_Type = Counter32
_BaTunnelReassembledPkts_Object = MibTableColumn
baTunnelReassembledPkts = _BaTunnelReassembledPkts_Object(
    (1, 3, 6, 1, 4, 1, 15768, 5, 1, 1, 3, 1, 10),
    _BaTunnelReassembledPkts_Type()
)
baTunnelReassembledPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baTunnelReassembledPkts.setStatus("current")
_BaTunnelRxBcastPkts_Type = Counter32
_BaTunnelRxBcastPkts_Object = MibTableColumn
baTunnelRxBcastPkts = _BaTunnelRxBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 15768, 5, 1, 1, 3, 1, 11),
    _BaTunnelRxBcastPkts_Type()
)
baTunnelRxBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baTunnelRxBcastPkts.setStatus("current")
_BaTunnelTxBcastPkts_Type = Counter32
_BaTunnelTxBcastPkts_Object = MibTableColumn
baTunnelTxBcastPkts = _BaTunnelTxBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 15768, 5, 1, 1, 3, 1, 12),
    _BaTunnelTxBcastPkts_Type()
)
baTunnelTxBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baTunnelTxBcastPkts.setStatus("current")
_BaTunnelRxMulticastPkts_Type = Counter32
_BaTunnelRxMulticastPkts_Object = MibTableColumn
baTunnelRxMulticastPkts = _BaTunnelRxMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 15768, 5, 1, 1, 3, 1, 13),
    _BaTunnelRxMulticastPkts_Type()
)
baTunnelRxMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baTunnelRxMulticastPkts.setStatus("current")
_BaTunnelTxMulticastPkts_Type = Counter32
_BaTunnelTxMulticastPkts_Object = MibTableColumn
baTunnelTxMulticastPkts = _BaTunnelTxMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 15768, 5, 1, 1, 3, 1, 14),
    _BaTunnelTxMulticastPkts_Type()
)
baTunnelTxMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baTunnelTxMulticastPkts.setStatus("current")
_BaTunnelVlanMappingTable_Object = MibTable
baTunnelVlanMappingTable = _BaTunnelVlanMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 15768, 5, 1, 1, 4)
)
if mibBuilder.loadTexts:
    baTunnelVlanMappingTable.setStatus("current")
_BaTunnelVlanMappingEntry_Object = MibTableRow
baTunnelVlanMappingEntry = _BaTunnelVlanMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 15768, 5, 1, 1, 4, 1)
)
baTunnelVlanMappingEntry.setIndexNames(
    (0, "BELAIR-TUNNEL", "baTunnelEngineIndex"),
    (0, "BELAIR-TUNNEL", "baTunnelMappingVlan"),
)
if mibBuilder.loadTexts:
    baTunnelVlanMappingEntry.setStatus("current")
_BaTunnelMappingVlan_Type = BelAirVlanIdOrZero
_BaTunnelMappingVlan_Object = MibTableColumn
baTunnelMappingVlan = _BaTunnelMappingVlan_Object(
    (1, 3, 6, 1, 4, 1, 15768, 5, 1, 1, 4, 1, 1),
    _BaTunnelMappingVlan_Type()
)
baTunnelMappingVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    baTunnelMappingVlan.setStatus("current")


class _BaTunnelMappingTunnelIndex_Type(Integer32):
    """Custom type baTunnelMappingTunnelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_BaTunnelMappingTunnelIndex_Type.__name__ = "Integer32"
_BaTunnelMappingTunnelIndex_Object = MibTableColumn
baTunnelMappingTunnelIndex = _BaTunnelMappingTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 15768, 5, 1, 1, 4, 1, 2),
    _BaTunnelMappingTunnelIndex_Type()
)
baTunnelMappingTunnelIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    baTunnelMappingTunnelIndex.setStatus("current")
_BaTunnelMappingRowStatus_Type = BelAirRowStatus
_BaTunnelMappingRowStatus_Object = MibTableColumn
baTunnelMappingRowStatus = _BaTunnelMappingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15768, 5, 1, 1, 4, 1, 3),
    _BaTunnelMappingRowStatus_Type()
)
baTunnelMappingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    baTunnelMappingRowStatus.setStatus("current")
_BaTunnelCurrentTable_Object = MibTable
baTunnelCurrentTable = _BaTunnelCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 15768, 5, 1, 1, 5)
)
if mibBuilder.loadTexts:
    baTunnelCurrentTable.setStatus("current")
_BaTunnelCurrentEntry_Object = MibTableRow
baTunnelCurrentEntry = _BaTunnelCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 15768, 5, 1, 1, 5, 1)
)
baTunnelCurrentEntry.setIndexNames(
    (0, "BELAIR-TUNNEL", "baTunnelEngineIndex"),
    (0, "BELAIR-TUNNEL", "baTunnelIndex"),
)
if mibBuilder.loadTexts:
    baTunnelCurrentEntry.setStatus("current")
_BaTunnelCurrentUASs_Type = PerfCurrentCount
_BaTunnelCurrentUASs_Object = MibTableColumn
baTunnelCurrentUASs = _BaTunnelCurrentUASs_Object(
    (1, 3, 6, 1, 4, 1, 15768, 5, 1, 1, 5, 1, 1),
    _BaTunnelCurrentUASs_Type()
)
baTunnelCurrentUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baTunnelCurrentUASs.setStatus("current")
_BaTunnelIntervalTable_Object = MibTable
baTunnelIntervalTable = _BaTunnelIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 15768, 5, 1, 1, 6)
)
if mibBuilder.loadTexts:
    baTunnelIntervalTable.setStatus("current")
_BaTunnelIntervalEntry_Object = MibTableRow
baTunnelIntervalEntry = _BaTunnelIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 15768, 5, 1, 1, 6, 1)
)
baTunnelIntervalEntry.setIndexNames(
    (0, "BELAIR-TUNNEL", "baTunnelEngineIndex"),
    (0, "BELAIR-TUNNEL", "baTunnelIndex"),
    (0, "BELAIR-TUNNEL", "baTunnelIntervalIndex"),
)
if mibBuilder.loadTexts:
    baTunnelIntervalEntry.setStatus("current")


class _BaTunnelIntervalIndex_Type(Integer32):
    """Custom type baTunnelIntervalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_BaTunnelIntervalIndex_Type.__name__ = "Integer32"
_BaTunnelIntervalIndex_Object = MibTableColumn
baTunnelIntervalIndex = _BaTunnelIntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 15768, 5, 1, 1, 6, 1, 1),
    _BaTunnelIntervalIndex_Type()
)
baTunnelIntervalIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    baTunnelIntervalIndex.setStatus("current")
_BaTunnelIntervalUASs_Type = PerfIntervalCount
_BaTunnelIntervalUASs_Object = MibTableColumn
baTunnelIntervalUASs = _BaTunnelIntervalUASs_Object(
    (1, 3, 6, 1, 4, 1, 15768, 5, 1, 1, 6, 1, 2),
    _BaTunnelIntervalUASs_Type()
)
baTunnelIntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baTunnelIntervalUASs.setStatus("current")
_BaTunnelTotalTable_Object = MibTable
baTunnelTotalTable = _BaTunnelTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 15768, 5, 1, 1, 7)
)
if mibBuilder.loadTexts:
    baTunnelTotalTable.setStatus("current")
_BaTunnelTotalEntry_Object = MibTableRow
baTunnelTotalEntry = _BaTunnelTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 15768, 5, 1, 1, 7, 1)
)
baTunnelTotalEntry.setIndexNames(
    (0, "BELAIR-TUNNEL", "baTunnelEngineIndex"),
    (0, "BELAIR-TUNNEL", "baTunnelIndex"),
)
if mibBuilder.loadTexts:
    baTunnelTotalEntry.setStatus("current")
_BaTunnelTotalUASs_Type = PerfTotalCount
_BaTunnelTotalUASs_Object = MibTableColumn
baTunnelTotalUASs = _BaTunnelTotalUASs_Object(
    (1, 3, 6, 1, 4, 1, 15768, 5, 1, 1, 7, 1, 1),
    _BaTunnelTotalUASs_Type()
)
baTunnelTotalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baTunnelTotalUASs.setStatus("current")
_BaTunnel24HrIntervalTable_Object = MibTable
baTunnel24HrIntervalTable = _BaTunnel24HrIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 15768, 5, 1, 1, 8)
)
if mibBuilder.loadTexts:
    baTunnel24HrIntervalTable.setStatus("current")
_BaTunnel24HrIntervalEntry_Object = MibTableRow
baTunnel24HrIntervalEntry = _BaTunnel24HrIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 15768, 5, 1, 1, 8, 1)
)
baTunnel24HrIntervalEntry.setIndexNames(
    (0, "BELAIR-TUNNEL", "baTunnelEngineIndex"),
    (0, "BELAIR-TUNNEL", "baTunnelIndex"),
    (0, "BELAIR-TUNNEL", "baTunnel24HrIntervalIndex"),
)
if mibBuilder.loadTexts:
    baTunnel24HrIntervalEntry.setStatus("current")


class _BaTunnel24HrIntervalIndex_Type(Integer32):
    """Custom type baTunnel24HrIntervalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_BaTunnel24HrIntervalIndex_Type.__name__ = "Integer32"
_BaTunnel24HrIntervalIndex_Object = MibTableColumn
baTunnel24HrIntervalIndex = _BaTunnel24HrIntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 15768, 5, 1, 1, 8, 1, 1),
    _BaTunnel24HrIntervalIndex_Type()
)
baTunnel24HrIntervalIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    baTunnel24HrIntervalIndex.setStatus("current")
_BaTunnel24HrIntervalUASs_Type = Gauge32
_BaTunnel24HrIntervalUASs_Object = MibTableColumn
baTunnel24HrIntervalUASs = _BaTunnel24HrIntervalUASs_Object(
    (1, 3, 6, 1, 4, 1, 15768, 5, 1, 1, 8, 1, 2),
    _BaTunnel24HrIntervalUASs_Type()
)
baTunnel24HrIntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baTunnel24HrIntervalUASs.setStatus("current")
_BelairTunnelTraps_ObjectIdentity = ObjectIdentity
belairTunnelTraps = _BelairTunnelTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 5, 1, 2)
)
_BelairTunnelTrapsV2_ObjectIdentity = ObjectIdentity
belairTunnelTrapsV2 = _BelairTunnelTrapsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 5, 1, 2, 0)
)
_BelairTunnelConformance_ObjectIdentity = ObjectIdentity
belairTunnelConformance = _BelairTunnelConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 5, 1, 3)
)
baTunnelConfigEntry.registerAugmentions(
    ("BELAIR-TUNNEL",
     "baTunnelStatusEntry")
)
baTunnelStatusEntry.setIndexNames(*baTunnelConfigEntry.getIndexNames())

# Managed Objects groups

baTunnelObjGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15768, 5, 1, 3, 1)
)
baTunnelObjGroup.setObjects(
      *(("BELAIR-TUNNEL", "baTunnelEngineAdminState"),
        ("BELAIR-TUNNEL", "baTunnelEngineLocalIp"),
        ("BELAIR-TUNNEL", "baTunnelEngineNetMask"),
        ("BELAIR-TUNNEL", "baTunnelEngineGateway"),
        ("BELAIR-TUNNEL", "baTunnelEngineVlanId"),
        ("BELAIR-TUNNEL", "baTunnelEngineMode"),
        ("BELAIR-TUNNEL", "baTunnelAuthenState"),
        ("BELAIR-TUNNEL", "baTunnelPrimaryPeerIp"),
        ("BELAIR-TUNNEL", "baTunnelPrimarySecret"),
        ("BELAIR-TUNNEL", "baTunnelPrimaryPppName"),
        ("BELAIR-TUNNEL", "baTunnelPrimaryPppPassword"),
        ("BELAIR-TUNNEL", "baTunnelSecondaryPeerIp"),
        ("BELAIR-TUNNEL", "baTunnelSecondarySecret"),
        ("BELAIR-TUNNEL", "baTunnelSecondaryPppName"),
        ("BELAIR-TUNNEL", "baTunnelSecondaryPppPassword"),
        ("BELAIR-TUNNEL", "baTunnelConfigRowStatus"),
        ("BELAIR-TUNNEL", "baTunnelOperStatus"),
        ("BELAIR-TUNNEL", "baTunnelUpTime"),
        ("BELAIR-TUNNEL", "baTunnelPrimaryActive"),
        ("BELAIR-TUNNEL", "baTunnelSecondaryActive"),
        ("BELAIR-TUNNEL", "baTunnelRxPkts"),
        ("BELAIR-TUNNEL", "baTunnelTxPkts"),
        ("BELAIR-TUNNEL", "baTunnelMappingTunnelIndex"),
        ("BELAIR-TUNNEL", "baTunnelReassembledPkts"),
        ("BELAIR-TUNNEL", "baTunnelFragmentedPkts"),
        ("BELAIR-TUNNEL", "baTunnelTxOctets"),
        ("BELAIR-TUNNEL", "baTunnelRxOctets"),
        ("BELAIR-TUNNEL", "baTunnelTxBandwidthLimit"),
        ("BELAIR-TUNNEL", "baTunnelRxBandwidthLimit"),
        ("BELAIR-TUNNEL", "baTunnelGroupName"),
        ("BELAIR-TUNNEL", "baTunnelTxMulticastPkts"),
        ("BELAIR-TUNNEL", "baTunnelRxMulticastPkts"),
        ("BELAIR-TUNNEL", "baTunnelTxBcastPkts"),
        ("BELAIR-TUNNEL", "baTunnelRxBcastPkts"),
        ("BELAIR-TUNNEL", "baTunnelSecondaryAuthenState"),
        ("BELAIR-TUNNEL", "baTunnelMappingRowStatus"),
        ("BELAIR-TUNNEL", "baTunnelPrimaryName"),
        ("BELAIR-TUNNEL", "baTunnelSecondaryName"),
        ("BELAIR-TUNNEL", "baTunnelRevertive"),
        ("BELAIR-TUNNEL", "baTunnelCurrentUASs"),
        ("BELAIR-TUNNEL", "baTunnelIntervalUASs"),
        ("BELAIR-TUNNEL", "baTunnel24HrIntervalUASs"),
        ("BELAIR-TUNNEL", "baTunnelTotalUASs"))
)
if mibBuilder.loadTexts:
    baTunnelObjGroup.setStatus("current")


# Notification objects

baTunnelStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 15768, 5, 1, 2, 0, 1)
)
baTunnelStatusChange.setObjects(
      *(("BELAIR-TUNNEL", "baTunnelOperStatus"),
        ("BELAIR-TUNNEL", "baTunnelPrimaryActive"),
        ("BELAIR-TUNNEL", "baTunnelSecondaryActive"))
)
if mibBuilder.loadTexts:
    baTunnelStatusChange.setStatus(
        "current"
    )


# Notifications groups

baTunnelTrapObjGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 15768, 5, 1, 3, 2)
)
baTunnelTrapObjGroup.setObjects(
    ("BELAIR-TUNNEL", "baTunnelStatusChange")
)
if mibBuilder.loadTexts:
    baTunnelTrapObjGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BELAIR-TUNNEL",
    **{"belairTunnelMib": belairTunnelMib,
       "belairTunnelObjects": belairTunnelObjects,
       "baTunnelEngineTable": baTunnelEngineTable,
       "baTunnelEngineEntry": baTunnelEngineEntry,
       "baTunnelEngineIndex": baTunnelEngineIndex,
       "baTunnelEngineAdminState": baTunnelEngineAdminState,
       "baTunnelEngineLocalIp": baTunnelEngineLocalIp,
       "baTunnelEngineNetMask": baTunnelEngineNetMask,
       "baTunnelEngineGateway": baTunnelEngineGateway,
       "baTunnelEngineVlanId": baTunnelEngineVlanId,
       "baTunnelEngineMode": baTunnelEngineMode,
       "baTunnelConfigTable": baTunnelConfigTable,
       "baTunnelConfigEntry": baTunnelConfigEntry,
       "baTunnelIndex": baTunnelIndex,
       "baTunnelPrimaryName": baTunnelPrimaryName,
       "baTunnelSecondaryName": baTunnelSecondaryName,
       "baTunnelAuthenState": baTunnelAuthenState,
       "baTunnelPrimaryPeerIp": baTunnelPrimaryPeerIp,
       "baTunnelPrimarySecret": baTunnelPrimarySecret,
       "baTunnelPrimaryPppName": baTunnelPrimaryPppName,
       "baTunnelPrimaryPppPassword": baTunnelPrimaryPppPassword,
       "baTunnelSecondaryPeerIp": baTunnelSecondaryPeerIp,
       "baTunnelSecondarySecret": baTunnelSecondarySecret,
       "baTunnelSecondaryPppName": baTunnelSecondaryPppName,
       "baTunnelSecondaryPppPassword": baTunnelSecondaryPppPassword,
       "baTunnelConfigRowStatus": baTunnelConfigRowStatus,
       "baTunnelRxBandwidthLimit": baTunnelRxBandwidthLimit,
       "baTunnelTxBandwidthLimit": baTunnelTxBandwidthLimit,
       "baTunnelGroupName": baTunnelGroupName,
       "baTunnelRevertive": baTunnelRevertive,
       "baTunnelSecondaryAuthenState": baTunnelSecondaryAuthenState,
       "baTunnelStatusTable": baTunnelStatusTable,
       "baTunnelStatusEntry": baTunnelStatusEntry,
       "baTunnelOperStatus": baTunnelOperStatus,
       "baTunnelUpTime": baTunnelUpTime,
       "baTunnelPrimaryActive": baTunnelPrimaryActive,
       "baTunnelSecondaryActive": baTunnelSecondaryActive,
       "baTunnelRxPkts": baTunnelRxPkts,
       "baTunnelTxPkts": baTunnelTxPkts,
       "baTunnelRxOctets": baTunnelRxOctets,
       "baTunnelTxOctets": baTunnelTxOctets,
       "baTunnelFragmentedPkts": baTunnelFragmentedPkts,
       "baTunnelReassembledPkts": baTunnelReassembledPkts,
       "baTunnelRxBcastPkts": baTunnelRxBcastPkts,
       "baTunnelTxBcastPkts": baTunnelTxBcastPkts,
       "baTunnelRxMulticastPkts": baTunnelRxMulticastPkts,
       "baTunnelTxMulticastPkts": baTunnelTxMulticastPkts,
       "baTunnelVlanMappingTable": baTunnelVlanMappingTable,
       "baTunnelVlanMappingEntry": baTunnelVlanMappingEntry,
       "baTunnelMappingVlan": baTunnelMappingVlan,
       "baTunnelMappingTunnelIndex": baTunnelMappingTunnelIndex,
       "baTunnelMappingRowStatus": baTunnelMappingRowStatus,
       "baTunnelCurrentTable": baTunnelCurrentTable,
       "baTunnelCurrentEntry": baTunnelCurrentEntry,
       "baTunnelCurrentUASs": baTunnelCurrentUASs,
       "baTunnelIntervalTable": baTunnelIntervalTable,
       "baTunnelIntervalEntry": baTunnelIntervalEntry,
       "baTunnelIntervalIndex": baTunnelIntervalIndex,
       "baTunnelIntervalUASs": baTunnelIntervalUASs,
       "baTunnelTotalTable": baTunnelTotalTable,
       "baTunnelTotalEntry": baTunnelTotalEntry,
       "baTunnelTotalUASs": baTunnelTotalUASs,
       "baTunnel24HrIntervalTable": baTunnel24HrIntervalTable,
       "baTunnel24HrIntervalEntry": baTunnel24HrIntervalEntry,
       "baTunnel24HrIntervalIndex": baTunnel24HrIntervalIndex,
       "baTunnel24HrIntervalUASs": baTunnel24HrIntervalUASs,
       "belairTunnelTraps": belairTunnelTraps,
       "belairTunnelTrapsV2": belairTunnelTrapsV2,
       "baTunnelStatusChange": baTunnelStatusChange,
       "belairTunnelConformance": belairTunnelConformance,
       "baTunnelObjGroup": baTunnelObjGroup,
       "baTunnelTrapObjGroup": baTunnelTrapObjGroup}
)
