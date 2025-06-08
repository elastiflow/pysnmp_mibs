# SNMP MIB module (BELAIR-CEM) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ericsson_15768/BELAIR-CEM.mib
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

(belairApplications,) = mibBuilder.importSymbols(
    "BELAIR-SMI",
    "belairApplications")

(BelAirAdminState,
 BelAirVlanIdOrZero) = mibBuilder.importSymbols(
    "BELAIR-TC",
    "BelAirAdminState",
    "BelAirVlanIdOrZero")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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

belairCemMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 6, 2)
)
if mibBuilder.loadTexts:
    belairCemMib.setRevisions(
        ("2006-03-02 17:40",
         "2006-01-25 14:30")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BelairCemObjects_ObjectIdentity = ObjectIdentity
belairCemObjects = _BelairCemObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 6, 2, 1)
)
_BelairCemConfigTable_Object = MibTable
belairCemConfigTable = _BelairCemConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 2, 1, 1)
)
if mibBuilder.loadTexts:
    belairCemConfigTable.setStatus("current")
_BelairCemConfigEntry_Object = MibTableRow
belairCemConfigEntry = _BelairCemConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 2, 1, 1, 1)
)
belairCemConfigEntry.setIndexNames(
    (0, "BELAIR-CEM", "belairCemIndex"),
)
if mibBuilder.loadTexts:
    belairCemConfigEntry.setStatus("current")


class _BelairCemIndex_Type(Integer32):
    """Custom type belairCemIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_BelairCemIndex_Type.__name__ = "Integer32"
_BelairCemIndex_Object = MibTableColumn
belairCemIndex = _BelairCemIndex_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 2, 1, 1, 1, 1),
    _BelairCemIndex_Type()
)
belairCemIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    belairCemIndex.setStatus("current")
_BelairCemAdminState_Type = BelAirAdminState
_BelairCemAdminState_Object = MibTableColumn
belairCemAdminState = _BelairCemAdminState_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 2, 1, 1, 1, 2),
    _BelairCemAdminState_Type()
)
belairCemAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairCemAdminState.setStatus("current")


class _BelairCemOperStatus_Type(Integer32):
    """Custom type belairCemOperStatus based on Integer32"""
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


_BelairCemOperStatus_Type.__name__ = "Integer32"
_BelairCemOperStatus_Object = MibTableColumn
belairCemOperStatus = _BelairCemOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 2, 1, 1, 1, 3),
    _BelairCemOperStatus_Type()
)
belairCemOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairCemOperStatus.setStatus("current")


class _BelairCemMode_Type(Integer32):
    """Custom type belairCemMode based on Integer32"""
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
        *(("t1Structured", 1),
          ("t1Unstructured", 2),
          ("e1Structured", 3),
          ("e1Unstructured", 4))
    )


_BelairCemMode_Type.__name__ = "Integer32"
_BelairCemMode_Object = MibTableColumn
belairCemMode = _BelairCemMode_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 2, 1, 1, 1, 4),
    _BelairCemMode_Type()
)
belairCemMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairCemMode.setStatus("current")


class _BelairCemTimingSource_Type(Integer32):
    """Custom type belairCemTimingSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tdm", 1),
          ("packet", 2),
          ("local", 3))
    )


_BelairCemTimingSource_Type.__name__ = "Integer32"
_BelairCemTimingSource_Object = MibTableColumn
belairCemTimingSource = _BelairCemTimingSource_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 2, 1, 1, 1, 5),
    _BelairCemTimingSource_Type()
)
belairCemTimingSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairCemTimingSource.setStatus("current")
_BelairCemTimingId_Type = Integer32
_BelairCemTimingId_Object = MibTableColumn
belairCemTimingId = _BelairCemTimingId_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 2, 1, 1, 1, 6),
    _BelairCemTimingId_Type()
)
belairCemTimingId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairCemTimingId.setStatus("current")
_BelairCemMacAddress_Type = MacAddress
_BelairCemMacAddress_Object = MibTableColumn
belairCemMacAddress = _BelairCemMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 2, 1, 1, 1, 7),
    _BelairCemMacAddress_Type()
)
belairCemMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairCemMacAddress.setStatus("current")
_BelairCemIpAddress_Type = IpAddress
_BelairCemIpAddress_Object = MibTableColumn
belairCemIpAddress = _BelairCemIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 2, 1, 1, 1, 8),
    _BelairCemIpAddress_Type()
)
belairCemIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairCemIpAddress.setStatus("current")
_BelairCemNetmask_Type = IpAddress
_BelairCemNetmask_Object = MibTableColumn
belairCemNetmask = _BelairCemNetmask_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 2, 1, 1, 1, 9),
    _BelairCemNetmask_Type()
)
belairCemNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairCemNetmask.setStatus("current")
_BelairCemConfigIpGateway_Type = IpAddress
_BelairCemConfigIpGateway_Object = MibTableColumn
belairCemConfigIpGateway = _BelairCemConfigIpGateway_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 2, 1, 1, 1, 10),
    _BelairCemConfigIpGateway_Type()
)
belairCemConfigIpGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairCemConfigIpGateway.setStatus("current")
_BelairCemVlanId_Type = BelAirVlanIdOrZero
_BelairCemVlanId_Object = MibTableColumn
belairCemVlanId = _BelairCemVlanId_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 2, 1, 1, 1, 11),
    _BelairCemVlanId_Type()
)
belairCemVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairCemVlanId.setStatus("current")
_BelairCemVlanEnabled_Type = TruthValue
_BelairCemVlanEnabled_Object = MibTableColumn
belairCemVlanEnabled = _BelairCemVlanEnabled_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 2, 1, 1, 1, 12),
    _BelairCemVlanEnabled_Type()
)
belairCemVlanEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairCemVlanEnabled.setStatus("current")


class _BelairCemVlanPriority_Type(Integer32):
    """Custom type belairCemVlanPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_BelairCemVlanPriority_Type.__name__ = "Integer32"
_BelairCemVlanPriority_Object = MibTableColumn
belairCemVlanPriority = _BelairCemVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 2, 1, 1, 1, 13),
    _BelairCemVlanPriority_Type()
)
belairCemVlanPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairCemVlanPriority.setStatus("current")
_BelairCemRtpEnabled_Type = TruthValue
_BelairCemRtpEnabled_Object = MibTableColumn
belairCemRtpEnabled = _BelairCemRtpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 2, 1, 1, 1, 14),
    _BelairCemRtpEnabled_Type()
)
belairCemRtpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairCemRtpEnabled.setStatus("current")
_BelairCemVcTable_Object = MibTable
belairCemVcTable = _BelairCemVcTable_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 2, 1, 2)
)
if mibBuilder.loadTexts:
    belairCemVcTable.setStatus("current")
_BelairCemVcEntry_Object = MibTableRow
belairCemVcEntry = _BelairCemVcEntry_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 2, 1, 2, 1)
)
belairCemVcEntry.setIndexNames(
    (0, "BELAIR-CEM", "belairCemIndex"),
    (0, "BELAIR-CEM", "belairCemVcIndex"),
)
if mibBuilder.loadTexts:
    belairCemVcEntry.setStatus("current")


class _BelairCemVcIndex_Type(Integer32):
    """Custom type belairCemVcIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_BelairCemVcIndex_Type.__name__ = "Integer32"
_BelairCemVcIndex_Object = MibTableColumn
belairCemVcIndex = _BelairCemVcIndex_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 2, 1, 2, 1, 1),
    _BelairCemVcIndex_Type()
)
belairCemVcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    belairCemVcIndex.setStatus("current")
_BelairCemVcIfIndex_Type = InterfaceIndex
_BelairCemVcIfIndex_Object = MibTableColumn
belairCemVcIfIndex = _BelairCemVcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 2, 1, 2, 1, 2),
    _BelairCemVcIfIndex_Type()
)
belairCemVcIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairCemVcIfIndex.setStatus("current")
_BelairCemVcAdminState_Type = BelAirAdminState
_BelairCemVcAdminState_Object = MibTableColumn
belairCemVcAdminState = _BelairCemVcAdminState_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 2, 1, 2, 1, 3),
    _BelairCemVcAdminState_Type()
)
belairCemVcAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairCemVcAdminState.setStatus("current")


class _BelairCemVcOperStatus_Type(Integer32):
    """Custom type belairCemVcOperStatus based on Integer32"""
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


_BelairCemVcOperStatus_Type.__name__ = "Integer32"
_BelairCemVcOperStatus_Object = MibTableColumn
belairCemVcOperStatus = _BelairCemVcOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 2, 1, 2, 1, 4),
    _BelairCemVcOperStatus_Type()
)
belairCemVcOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairCemVcOperStatus.setStatus("current")
_BelairCemVcDestMacAddress_Type = MacAddress
_BelairCemVcDestMacAddress_Object = MibTableColumn
belairCemVcDestMacAddress = _BelairCemVcDestMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 2, 1, 2, 1, 5),
    _BelairCemVcDestMacAddress_Type()
)
belairCemVcDestMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairCemVcDestMacAddress.setStatus("current")
_BelairCemVcArpEnabled_Type = TruthValue
_BelairCemVcArpEnabled_Object = MibTableColumn
belairCemVcArpEnabled = _BelairCemVcArpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 2, 1, 2, 1, 6),
    _BelairCemVcArpEnabled_Type()
)
belairCemVcArpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairCemVcArpEnabled.setStatus("current")
_BelairCemVcDestIpAddress_Type = IpAddress
_BelairCemVcDestIpAddress_Object = MibTableColumn
belairCemVcDestIpAddress = _BelairCemVcDestIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 2, 1, 2, 1, 7),
    _BelairCemVcDestIpAddress_Type()
)
belairCemVcDestIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairCemVcDestIpAddress.setStatus("current")


class _BelairCemVcTos_Type(Integer32):
    """Custom type belairCemVcTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BelairCemVcTos_Type.__name__ = "Integer32"
_BelairCemVcTos_Object = MibTableColumn
belairCemVcTos = _BelairCemVcTos_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 2, 1, 2, 1, 8),
    _BelairCemVcTos_Type()
)
belairCemVcTos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairCemVcTos.setStatus("current")


class _BelairCemVcDestUdpPort_Type(Integer32):
    """Custom type belairCemVcDestUdpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BelairCemVcDestUdpPort_Type.__name__ = "Integer32"
_BelairCemVcDestUdpPort_Object = MibTableColumn
belairCemVcDestUdpPort = _BelairCemVcDestUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 2, 1, 2, 1, 9),
    _BelairCemVcDestUdpPort_Type()
)
belairCemVcDestUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairCemVcDestUdpPort.setStatus("current")


class _BelairCemVcSrcUdpPort_Type(Integer32):
    """Custom type belairCemVcSrcUdpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BelairCemVcSrcUdpPort_Type.__name__ = "Integer32"
_BelairCemVcSrcUdpPort_Object = MibTableColumn
belairCemVcSrcUdpPort = _BelairCemVcSrcUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 2, 1, 2, 1, 10),
    _BelairCemVcSrcUdpPort_Type()
)
belairCemVcSrcUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairCemVcSrcUdpPort.setStatus("current")


class _BelairCemVcRtpPayloadType_Type(Integer32):
    """Custom type belairCemVcRtpPayloadType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(96, 127),
    )


_BelairCemVcRtpPayloadType_Type.__name__ = "Integer32"
_BelairCemVcRtpPayloadType_Object = MibTableColumn
belairCemVcRtpPayloadType = _BelairCemVcRtpPayloadType_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 2, 1, 2, 1, 11),
    _BelairCemVcRtpPayloadType_Type()
)
belairCemVcRtpPayloadType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairCemVcRtpPayloadType.setStatus("current")
_BelairCemVcRtpSsrc_Type = Integer32
_BelairCemVcRtpSsrc_Object = MibTableColumn
belairCemVcRtpSsrc = _BelairCemVcRtpSsrc_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 2, 1, 2, 1, 12),
    _BelairCemVcRtpSsrc_Type()
)
belairCemVcRtpSsrc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairCemVcRtpSsrc.setStatus("current")


class _BelairCemVcJitterBufferSize_Type(Integer32):
    """Custom type belairCemVcJitterBufferSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_BelairCemVcJitterBufferSize_Type.__name__ = "Integer32"
_BelairCemVcJitterBufferSize_Object = MibTableColumn
belairCemVcJitterBufferSize = _BelairCemVcJitterBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 2, 1, 2, 1, 13),
    _BelairCemVcJitterBufferSize_Type()
)
belairCemVcJitterBufferSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairCemVcJitterBufferSize.setStatus("current")
if mibBuilder.loadTexts:
    belairCemVcJitterBufferSize.setUnits("pkts")


class _BelairCemVcFramesPerPktRx_Type(Integer32):
    """Custom type belairCemVcFramesPerPktRx based on Integer32"""
    defaultValue = 32

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 40),
    )


_BelairCemVcFramesPerPktRx_Type.__name__ = "Integer32"
_BelairCemVcFramesPerPktRx_Object = MibTableColumn
belairCemVcFramesPerPktRx = _BelairCemVcFramesPerPktRx_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 2, 1, 2, 1, 14),
    _BelairCemVcFramesPerPktRx_Type()
)
belairCemVcFramesPerPktRx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairCemVcFramesPerPktRx.setStatus("current")


class _BelairCemVcFramesPerPktTx_Type(Integer32):
    """Custom type belairCemVcFramesPerPktTx based on Integer32"""
    defaultValue = 32

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 40),
    )


_BelairCemVcFramesPerPktTx_Type.__name__ = "Integer32"
_BelairCemVcFramesPerPktTx_Object = MibTableColumn
belairCemVcFramesPerPktTx = _BelairCemVcFramesPerPktTx_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 2, 1, 2, 1, 15),
    _BelairCemVcFramesPerPktTx_Type()
)
belairCemVcFramesPerPktTx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairCemVcFramesPerPktTx.setStatus("current")


class _BelairCemVcCurrentIndications_Type(Bits):
    """Custom type belairCemVcCurrentIndications based on Bits"""
    namedValues = NamedValues(
        *(("noAlarm", 0),
          ("pktLoss", 1),
          ("pktLossRemote", 2),
          ("excessPktLoss", 3),
          ("invalidPkts", 4),
          ("bufferOverrun", 5),
          ("peerInactive", 6))
    )

_BelairCemVcCurrentIndications_Type.__name__ = "Bits"
_BelairCemVcCurrentIndications_Object = MibTableColumn
belairCemVcCurrentIndications = _BelairCemVcCurrentIndications_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 2, 1, 2, 1, 16),
    _BelairCemVcCurrentIndications_Type()
)
belairCemVcCurrentIndications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairCemVcCurrentIndications.setStatus("current")
_BelairCemVcPerfCurrTable_Object = MibTable
belairCemVcPerfCurrTable = _BelairCemVcPerfCurrTable_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 2, 1, 3)
)
if mibBuilder.loadTexts:
    belairCemVcPerfCurrTable.setStatus("current")
_BelairCemVcPerfCurrEntry_Object = MibTableRow
belairCemVcPerfCurrEntry = _BelairCemVcPerfCurrEntry_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    belairCemVcPerfCurrEntry.setStatus("current")
_BelairCemVcPerfCurrESs_Type = PerfCurrentCount
_BelairCemVcPerfCurrESs_Object = MibTableColumn
belairCemVcPerfCurrESs = _BelairCemVcPerfCurrESs_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 2, 1, 3, 1, 1),
    _BelairCemVcPerfCurrESs_Type()
)
belairCemVcPerfCurrESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairCemVcPerfCurrESs.setStatus("current")
_BelairCemVcPerfCurrSESs_Type = PerfCurrentCount
_BelairCemVcPerfCurrSESs_Object = MibTableColumn
belairCemVcPerfCurrSESs = _BelairCemVcPerfCurrSESs_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 2, 1, 3, 1, 2),
    _BelairCemVcPerfCurrSESs_Type()
)
belairCemVcPerfCurrSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairCemVcPerfCurrSESs.setStatus("current")
_BelairCemVcPerfCurrUASs_Type = PerfCurrentCount
_BelairCemVcPerfCurrUASs_Object = MibTableColumn
belairCemVcPerfCurrUASs = _BelairCemVcPerfCurrUASs_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 2, 1, 3, 1, 3),
    _BelairCemVcPerfCurrUASs_Type()
)
belairCemVcPerfCurrUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairCemVcPerfCurrUASs.setStatus("current")
_BelairCemVcPerfCurrFarEndESs_Type = PerfCurrentCount
_BelairCemVcPerfCurrFarEndESs_Object = MibTableColumn
belairCemVcPerfCurrFarEndESs = _BelairCemVcPerfCurrFarEndESs_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 2, 1, 3, 1, 4),
    _BelairCemVcPerfCurrFarEndESs_Type()
)
belairCemVcPerfCurrFarEndESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairCemVcPerfCurrFarEndESs.setStatus("current")
_BelairCemVcPerfCurrFarEndSESs_Type = PerfCurrentCount
_BelairCemVcPerfCurrFarEndSESs_Object = MibTableColumn
belairCemVcPerfCurrFarEndSESs = _BelairCemVcPerfCurrFarEndSESs_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 2, 1, 3, 1, 5),
    _BelairCemVcPerfCurrFarEndSESs_Type()
)
belairCemVcPerfCurrFarEndSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairCemVcPerfCurrFarEndSESs.setStatus("current")
_BelairCemVcPerfCurrFarEndUASs_Type = PerfCurrentCount
_BelairCemVcPerfCurrFarEndUASs_Object = MibTableColumn
belairCemVcPerfCurrFarEndUASs = _BelairCemVcPerfCurrFarEndUASs_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 2, 1, 3, 1, 6),
    _BelairCemVcPerfCurrFarEndUASs_Type()
)
belairCemVcPerfCurrFarEndUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairCemVcPerfCurrFarEndUASs.setStatus("current")
_BelairCemVcPerfCurrEarlyPkts_Type = PerfCurrentCount
_BelairCemVcPerfCurrEarlyPkts_Object = MibTableColumn
belairCemVcPerfCurrEarlyPkts = _BelairCemVcPerfCurrEarlyPkts_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 2, 1, 3, 1, 7),
    _BelairCemVcPerfCurrEarlyPkts_Type()
)
belairCemVcPerfCurrEarlyPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairCemVcPerfCurrEarlyPkts.setStatus("current")
_BelairCemVcPerfCurrLatePkts_Type = PerfCurrentCount
_BelairCemVcPerfCurrLatePkts_Object = MibTableColumn
belairCemVcPerfCurrLatePkts = _BelairCemVcPerfCurrLatePkts_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 2, 1, 3, 1, 8),
    _BelairCemVcPerfCurrLatePkts_Type()
)
belairCemVcPerfCurrLatePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairCemVcPerfCurrLatePkts.setStatus("current")
_BelairCemVcPerfCurrUnderrunPkts_Type = PerfCurrentCount
_BelairCemVcPerfCurrUnderrunPkts_Object = MibTableColumn
belairCemVcPerfCurrUnderrunPkts = _BelairCemVcPerfCurrUnderrunPkts_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 2, 1, 3, 1, 9),
    _BelairCemVcPerfCurrUnderrunPkts_Type()
)
belairCemVcPerfCurrUnderrunPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairCemVcPerfCurrUnderrunPkts.setStatus("current")
_BelairCemVcPerfCurrLBitESs_Type = PerfCurrentCount
_BelairCemVcPerfCurrLBitESs_Object = MibTableColumn
belairCemVcPerfCurrLBitESs = _BelairCemVcPerfCurrLBitESs_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 2, 1, 3, 1, 10),
    _BelairCemVcPerfCurrLBitESs_Type()
)
belairCemVcPerfCurrLBitESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairCemVcPerfCurrLBitESs.setStatus("current")
_BelairCemVcPerfCurrLBitSESs_Type = PerfCurrentCount
_BelairCemVcPerfCurrLBitSESs_Object = MibTableColumn
belairCemVcPerfCurrLBitSESs = _BelairCemVcPerfCurrLBitSESs_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 2, 1, 3, 1, 11),
    _BelairCemVcPerfCurrLBitSESs_Type()
)
belairCemVcPerfCurrLBitSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairCemVcPerfCurrLBitSESs.setStatus("current")
_BelairCemVcPerfIntervalTable_Object = MibTable
belairCemVcPerfIntervalTable = _BelairCemVcPerfIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 2, 1, 4)
)
if mibBuilder.loadTexts:
    belairCemVcPerfIntervalTable.setStatus("current")
_BelairCemVcPerfIntervalEntry_Object = MibTableRow
belairCemVcPerfIntervalEntry = _BelairCemVcPerfIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 2, 1, 4, 1)
)
belairCemVcPerfIntervalEntry.setIndexNames(
    (0, "BELAIR-CEM", "belairCemIndex"),
    (0, "BELAIR-CEM", "belairCemVcIndex"),
    (0, "BELAIR-CEM", "belairCemVcPerfIntervalNumber"),
)
if mibBuilder.loadTexts:
    belairCemVcPerfIntervalEntry.setStatus("current")


class _BelairCemVcPerfIntervalNumber_Type(Integer32):
    """Custom type belairCemVcPerfIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_BelairCemVcPerfIntervalNumber_Type.__name__ = "Integer32"
_BelairCemVcPerfIntervalNumber_Object = MibTableColumn
belairCemVcPerfIntervalNumber = _BelairCemVcPerfIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 2, 1, 4, 1, 1),
    _BelairCemVcPerfIntervalNumber_Type()
)
belairCemVcPerfIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    belairCemVcPerfIntervalNumber.setStatus("current")
_BelairCemVcPerfIntervalValid_Type = TruthValue
_BelairCemVcPerfIntervalValid_Object = MibTableColumn
belairCemVcPerfIntervalValid = _BelairCemVcPerfIntervalValid_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 2, 1, 4, 1, 2),
    _BelairCemVcPerfIntervalValid_Type()
)
belairCemVcPerfIntervalValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairCemVcPerfIntervalValid.setStatus("current")
_BelairCemVcPerfIntervalESs_Type = PerfIntervalCount
_BelairCemVcPerfIntervalESs_Object = MibTableColumn
belairCemVcPerfIntervalESs = _BelairCemVcPerfIntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 2, 1, 4, 1, 3),
    _BelairCemVcPerfIntervalESs_Type()
)
belairCemVcPerfIntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairCemVcPerfIntervalESs.setStatus("current")
_BelairCemVcPerfIntervalSESs_Type = PerfIntervalCount
_BelairCemVcPerfIntervalSESs_Object = MibTableColumn
belairCemVcPerfIntervalSESs = _BelairCemVcPerfIntervalSESs_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 2, 1, 4, 1, 4),
    _BelairCemVcPerfIntervalSESs_Type()
)
belairCemVcPerfIntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairCemVcPerfIntervalSESs.setStatus("current")
_BelairCemVcPerfIntervalUASs_Type = PerfIntervalCount
_BelairCemVcPerfIntervalUASs_Object = MibTableColumn
belairCemVcPerfIntervalUASs = _BelairCemVcPerfIntervalUASs_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 2, 1, 4, 1, 5),
    _BelairCemVcPerfIntervalUASs_Type()
)
belairCemVcPerfIntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairCemVcPerfIntervalUASs.setStatus("current")
_BelairCemVcPerfIntervalFarEndESs_Type = PerfIntervalCount
_BelairCemVcPerfIntervalFarEndESs_Object = MibTableColumn
belairCemVcPerfIntervalFarEndESs = _BelairCemVcPerfIntervalFarEndESs_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 2, 1, 4, 1, 6),
    _BelairCemVcPerfIntervalFarEndESs_Type()
)
belairCemVcPerfIntervalFarEndESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairCemVcPerfIntervalFarEndESs.setStatus("current")
_BelairCemVcPerfIntervalFarEndSESs_Type = PerfIntervalCount
_BelairCemVcPerfIntervalFarEndSESs_Object = MibTableColumn
belairCemVcPerfIntervalFarEndSESs = _BelairCemVcPerfIntervalFarEndSESs_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 2, 1, 4, 1, 7),
    _BelairCemVcPerfIntervalFarEndSESs_Type()
)
belairCemVcPerfIntervalFarEndSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairCemVcPerfIntervalFarEndSESs.setStatus("current")
_BelairCemVcPerfIntervalFarEndUASs_Type = PerfIntervalCount
_BelairCemVcPerfIntervalFarEndUASs_Object = MibTableColumn
belairCemVcPerfIntervalFarEndUASs = _BelairCemVcPerfIntervalFarEndUASs_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 2, 1, 4, 1, 8),
    _BelairCemVcPerfIntervalFarEndUASs_Type()
)
belairCemVcPerfIntervalFarEndUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairCemVcPerfIntervalFarEndUASs.setStatus("current")
_BelairCemVcPerfIntervalEarlyPkts_Type = PerfIntervalCount
_BelairCemVcPerfIntervalEarlyPkts_Object = MibTableColumn
belairCemVcPerfIntervalEarlyPkts = _BelairCemVcPerfIntervalEarlyPkts_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 2, 1, 4, 1, 9),
    _BelairCemVcPerfIntervalEarlyPkts_Type()
)
belairCemVcPerfIntervalEarlyPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairCemVcPerfIntervalEarlyPkts.setStatus("current")
_BelairCemVcPerfIntervalLatePkts_Type = PerfIntervalCount
_BelairCemVcPerfIntervalLatePkts_Object = MibTableColumn
belairCemVcPerfIntervalLatePkts = _BelairCemVcPerfIntervalLatePkts_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 2, 1, 4, 1, 10),
    _BelairCemVcPerfIntervalLatePkts_Type()
)
belairCemVcPerfIntervalLatePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairCemVcPerfIntervalLatePkts.setStatus("current")
_BelairCemVcPerfIntervalUnderrunPkts_Type = PerfIntervalCount
_BelairCemVcPerfIntervalUnderrunPkts_Object = MibTableColumn
belairCemVcPerfIntervalUnderrunPkts = _BelairCemVcPerfIntervalUnderrunPkts_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 2, 1, 4, 1, 11),
    _BelairCemVcPerfIntervalUnderrunPkts_Type()
)
belairCemVcPerfIntervalUnderrunPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairCemVcPerfIntervalUnderrunPkts.setStatus("current")
_BelairCemVcPerfIntervalLBitESs_Type = PerfIntervalCount
_BelairCemVcPerfIntervalLBitESs_Object = MibTableColumn
belairCemVcPerfIntervalLBitESs = _BelairCemVcPerfIntervalLBitESs_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 2, 1, 4, 1, 12),
    _BelairCemVcPerfIntervalLBitESs_Type()
)
belairCemVcPerfIntervalLBitESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairCemVcPerfIntervalLBitESs.setStatus("current")
_BelairCemVcPerfIntervalLBitSESs_Type = PerfIntervalCount
_BelairCemVcPerfIntervalLBitSESs_Object = MibTableColumn
belairCemVcPerfIntervalLBitSESs = _BelairCemVcPerfIntervalLBitSESs_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 2, 1, 4, 1, 13),
    _BelairCemVcPerfIntervalLBitSESs_Type()
)
belairCemVcPerfIntervalLBitSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairCemVcPerfIntervalLBitSESs.setStatus("current")
_BelairCemVcPerfTotalTable_Object = MibTable
belairCemVcPerfTotalTable = _BelairCemVcPerfTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 2, 1, 5)
)
if mibBuilder.loadTexts:
    belairCemVcPerfTotalTable.setStatus("current")
_BelairCemVcPerfTotalEntry_Object = MibTableRow
belairCemVcPerfTotalEntry = _BelairCemVcPerfTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 2, 1, 5, 1)
)
if mibBuilder.loadTexts:
    belairCemVcPerfTotalEntry.setStatus("current")
_BelairCemVcPerfTotalESs_Type = PerfTotalCount
_BelairCemVcPerfTotalESs_Object = MibTableColumn
belairCemVcPerfTotalESs = _BelairCemVcPerfTotalESs_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 2, 1, 5, 1, 1),
    _BelairCemVcPerfTotalESs_Type()
)
belairCemVcPerfTotalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairCemVcPerfTotalESs.setStatus("current")
_BelairCemVcPerfTotalSESs_Type = PerfTotalCount
_BelairCemVcPerfTotalSESs_Object = MibTableColumn
belairCemVcPerfTotalSESs = _BelairCemVcPerfTotalSESs_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 2, 1, 5, 1, 2),
    _BelairCemVcPerfTotalSESs_Type()
)
belairCemVcPerfTotalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairCemVcPerfTotalSESs.setStatus("current")
_BelairCemVcPerfTotalUASs_Type = PerfTotalCount
_BelairCemVcPerfTotalUASs_Object = MibTableColumn
belairCemVcPerfTotalUASs = _BelairCemVcPerfTotalUASs_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 2, 1, 5, 1, 3),
    _BelairCemVcPerfTotalUASs_Type()
)
belairCemVcPerfTotalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairCemVcPerfTotalUASs.setStatus("current")
_BelairCemVcPerfTotalFarEndESs_Type = PerfTotalCount
_BelairCemVcPerfTotalFarEndESs_Object = MibTableColumn
belairCemVcPerfTotalFarEndESs = _BelairCemVcPerfTotalFarEndESs_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 2, 1, 5, 1, 4),
    _BelairCemVcPerfTotalFarEndESs_Type()
)
belairCemVcPerfTotalFarEndESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairCemVcPerfTotalFarEndESs.setStatus("current")
_BelairCemVcPerfTotalFarEndSESs_Type = PerfTotalCount
_BelairCemVcPerfTotalFarEndSESs_Object = MibTableColumn
belairCemVcPerfTotalFarEndSESs = _BelairCemVcPerfTotalFarEndSESs_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 2, 1, 5, 1, 5),
    _BelairCemVcPerfTotalFarEndSESs_Type()
)
belairCemVcPerfTotalFarEndSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairCemVcPerfTotalFarEndSESs.setStatus("current")
_BelairCemVcPerfTotalFarEndUASs_Type = PerfTotalCount
_BelairCemVcPerfTotalFarEndUASs_Object = MibTableColumn
belairCemVcPerfTotalFarEndUASs = _BelairCemVcPerfTotalFarEndUASs_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 2, 1, 5, 1, 6),
    _BelairCemVcPerfTotalFarEndUASs_Type()
)
belairCemVcPerfTotalFarEndUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairCemVcPerfTotalFarEndUASs.setStatus("current")
_BelairCemVcPerfTotalEarlyPkts_Type = PerfTotalCount
_BelairCemVcPerfTotalEarlyPkts_Object = MibTableColumn
belairCemVcPerfTotalEarlyPkts = _BelairCemVcPerfTotalEarlyPkts_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 2, 1, 5, 1, 7),
    _BelairCemVcPerfTotalEarlyPkts_Type()
)
belairCemVcPerfTotalEarlyPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairCemVcPerfTotalEarlyPkts.setStatus("current")
_BelairCemVcPerfTotalLatePkts_Type = PerfTotalCount
_BelairCemVcPerfTotalLatePkts_Object = MibTableColumn
belairCemVcPerfTotalLatePkts = _BelairCemVcPerfTotalLatePkts_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 2, 1, 5, 1, 8),
    _BelairCemVcPerfTotalLatePkts_Type()
)
belairCemVcPerfTotalLatePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairCemVcPerfTotalLatePkts.setStatus("current")
_BelairCemVcPerfTotalUnderrunPkts_Type = PerfTotalCount
_BelairCemVcPerfTotalUnderrunPkts_Object = MibTableColumn
belairCemVcPerfTotalUnderrunPkts = _BelairCemVcPerfTotalUnderrunPkts_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 2, 1, 5, 1, 9),
    _BelairCemVcPerfTotalUnderrunPkts_Type()
)
belairCemVcPerfTotalUnderrunPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairCemVcPerfTotalUnderrunPkts.setStatus("current")
_BelairCemVcPerfTotalLBitESs_Type = PerfTotalCount
_BelairCemVcPerfTotalLBitESs_Object = MibTableColumn
belairCemVcPerfTotalLBitESs = _BelairCemVcPerfTotalLBitESs_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 2, 1, 5, 1, 10),
    _BelairCemVcPerfTotalLBitESs_Type()
)
belairCemVcPerfTotalLBitESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairCemVcPerfTotalLBitESs.setStatus("current")
_BelairCemVcPerfTotalLBitSESs_Type = PerfTotalCount
_BelairCemVcPerfTotalLBitSESs_Object = MibTableColumn
belairCemVcPerfTotalLBitSESs = _BelairCemVcPerfTotalLBitSESs_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 2, 1, 5, 1, 11),
    _BelairCemVcPerfTotalLBitSESs_Type()
)
belairCemVcPerfTotalLBitSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairCemVcPerfTotalLBitSESs.setStatus("current")
_BelairCemTraps_ObjectIdentity = ObjectIdentity
belairCemTraps = _BelairCemTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 6, 2, 2)
)
_BelairCemTrapsV2_ObjectIdentity = ObjectIdentity
belairCemTrapsV2 = _BelairCemTrapsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 6, 2, 2, 0)
)
_BelairCemConformance_ObjectIdentity = ObjectIdentity
belairCemConformance = _BelairCemConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 6, 2, 3)
)
belairCemVcEntry.registerAugmentions(
    ("BELAIR-CEM",
     "belairCemVcPerfCurrEntry")
)
belairCemVcPerfCurrEntry.setIndexNames(*belairCemVcEntry.getIndexNames())
belairCemVcEntry.registerAugmentions(
    ("BELAIR-CEM",
     "belairCemVcPerfTotalEntry")
)
belairCemVcPerfTotalEntry.setIndexNames(*belairCemVcEntry.getIndexNames())

# Managed Objects groups

belairCemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15768, 6, 2, 3, 1)
)
belairCemGroup.setObjects(
      *(("BELAIR-CEM", "belairCemAdminState"),
        ("BELAIR-CEM", "belairCemOperStatus"),
        ("BELAIR-CEM", "belairCemMode"),
        ("BELAIR-CEM", "belairCemTimingSource"),
        ("BELAIR-CEM", "belairCemTimingId"),
        ("BELAIR-CEM", "belairCemMacAddress"),
        ("BELAIR-CEM", "belairCemIpAddress"),
        ("BELAIR-CEM", "belairCemNetmask"),
        ("BELAIR-CEM", "belairCemConfigIpGateway"),
        ("BELAIR-CEM", "belairCemVlanId"),
        ("BELAIR-CEM", "belairCemVlanEnabled"),
        ("BELAIR-CEM", "belairCemVlanPriority"),
        ("BELAIR-CEM", "belairCemRtpEnabled"),
        ("BELAIR-CEM", "belairCemVcIfIndex"),
        ("BELAIR-CEM", "belairCemVcAdminState"),
        ("BELAIR-CEM", "belairCemVcOperStatus"),
        ("BELAIR-CEM", "belairCemVcDestMacAddress"),
        ("BELAIR-CEM", "belairCemVcArpEnabled"),
        ("BELAIR-CEM", "belairCemVcDestIpAddress"),
        ("BELAIR-CEM", "belairCemVcTos"),
        ("BELAIR-CEM", "belairCemVcDestUdpPort"),
        ("BELAIR-CEM", "belairCemVcSrcUdpPort"),
        ("BELAIR-CEM", "belairCemVcRtpPayloadType"),
        ("BELAIR-CEM", "belairCemVcRtpSsrc"),
        ("BELAIR-CEM", "belairCemVcJitterBufferSize"),
        ("BELAIR-CEM", "belairCemVcCurrentIndications"),
        ("BELAIR-CEM", "belairCemVcPerfCurrESs"),
        ("BELAIR-CEM", "belairCemVcPerfCurrSESs"),
        ("BELAIR-CEM", "belairCemVcPerfCurrUASs"),
        ("BELAIR-CEM", "belairCemVcPerfCurrFarEndESs"),
        ("BELAIR-CEM", "belairCemVcPerfCurrFarEndSESs"),
        ("BELAIR-CEM", "belairCemVcPerfCurrFarEndUASs"),
        ("BELAIR-CEM", "belairCemVcPerfCurrEarlyPkts"),
        ("BELAIR-CEM", "belairCemVcPerfCurrLatePkts"),
        ("BELAIR-CEM", "belairCemVcPerfCurrUnderrunPkts"),
        ("BELAIR-CEM", "belairCemVcPerfCurrLBitESs"),
        ("BELAIR-CEM", "belairCemVcPerfCurrLBitSESs"),
        ("BELAIR-CEM", "belairCemVcPerfIntervalValid"),
        ("BELAIR-CEM", "belairCemVcPerfIntervalESs"),
        ("BELAIR-CEM", "belairCemVcPerfIntervalSESs"),
        ("BELAIR-CEM", "belairCemVcPerfIntervalUASs"),
        ("BELAIR-CEM", "belairCemVcPerfIntervalFarEndESs"),
        ("BELAIR-CEM", "belairCemVcPerfIntervalFarEndSESs"),
        ("BELAIR-CEM", "belairCemVcPerfIntervalFarEndUASs"),
        ("BELAIR-CEM", "belairCemVcPerfIntervalEarlyPkts"),
        ("BELAIR-CEM", "belairCemVcPerfIntervalLatePkts"),
        ("BELAIR-CEM", "belairCemVcPerfIntervalUnderrunPkts"),
        ("BELAIR-CEM", "belairCemVcPerfIntervalLBitESs"),
        ("BELAIR-CEM", "belairCemVcPerfIntervalLBitSESs"),
        ("BELAIR-CEM", "belairCemVcPerfTotalESs"),
        ("BELAIR-CEM", "belairCemVcPerfTotalSESs"),
        ("BELAIR-CEM", "belairCemVcPerfTotalUASs"),
        ("BELAIR-CEM", "belairCemVcPerfTotalFarEndESs"),
        ("BELAIR-CEM", "belairCemVcPerfTotalFarEndSESs"),
        ("BELAIR-CEM", "belairCemVcPerfTotalFarEndUASs"),
        ("BELAIR-CEM", "belairCemVcPerfTotalEarlyPkts"),
        ("BELAIR-CEM", "belairCemVcPerfTotalLatePkts"),
        ("BELAIR-CEM", "belairCemVcPerfTotalUnderrunPkts"),
        ("BELAIR-CEM", "belairCemVcPerfTotalLBitESs"),
        ("BELAIR-CEM", "belairCemVcPerfTotalLBitSESs"),
        ("BELAIR-CEM", "belairCemVcFramesPerPktTx"),
        ("BELAIR-CEM", "belairCemVcFramesPerPktRx"))
)
if mibBuilder.loadTexts:
    belairCemGroup.setStatus("current")


# Notification objects

belairCemOperStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 15768, 6, 2, 2, 0, 1)
)
belairCemOperStatusChange.setObjects(
      *(("BELAIR-CEM", "belairCemAdminState"),
        ("BELAIR-CEM", "belairCemOperStatus"))
)
if mibBuilder.loadTexts:
    belairCemOperStatusChange.setStatus(
        "current"
    )

belairCemVcOperStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 15768, 6, 2, 2, 0, 2)
)
belairCemVcOperStatusChange.setObjects(
      *(("BELAIR-CEM", "belairCemVcAdminState"),
        ("BELAIR-CEM", "belairCemVcOperStatus"))
)
if mibBuilder.loadTexts:
    belairCemVcOperStatusChange.setStatus(
        "current"
    )

belairCemVcAlarmStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 15768, 6, 2, 2, 0, 3)
)
belairCemVcAlarmStatusChange.setObjects(
    ("BELAIR-CEM", "belairCemVcCurrentIndications")
)
if mibBuilder.loadTexts:
    belairCemVcAlarmStatusChange.setStatus(
        "current"
    )


# Notifications groups

belairCemNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 15768, 6, 2, 3, 2)
)
belairCemNotificationGroup.setObjects(
      *(("BELAIR-CEM", "belairCemOperStatusChange"),
        ("BELAIR-CEM", "belairCemVcOperStatusChange"),
        ("BELAIR-CEM", "belairCemVcAlarmStatusChange"))
)
if mibBuilder.loadTexts:
    belairCemNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BELAIR-CEM",
    **{"belairCemMib": belairCemMib,
       "belairCemObjects": belairCemObjects,
       "belairCemConfigTable": belairCemConfigTable,
       "belairCemConfigEntry": belairCemConfigEntry,
       "belairCemIndex": belairCemIndex,
       "belairCemAdminState": belairCemAdminState,
       "belairCemOperStatus": belairCemOperStatus,
       "belairCemMode": belairCemMode,
       "belairCemTimingSource": belairCemTimingSource,
       "belairCemTimingId": belairCemTimingId,
       "belairCemMacAddress": belairCemMacAddress,
       "belairCemIpAddress": belairCemIpAddress,
       "belairCemNetmask": belairCemNetmask,
       "belairCemConfigIpGateway": belairCemConfigIpGateway,
       "belairCemVlanId": belairCemVlanId,
       "belairCemVlanEnabled": belairCemVlanEnabled,
       "belairCemVlanPriority": belairCemVlanPriority,
       "belairCemRtpEnabled": belairCemRtpEnabled,
       "belairCemVcTable": belairCemVcTable,
       "belairCemVcEntry": belairCemVcEntry,
       "belairCemVcIndex": belairCemVcIndex,
       "belairCemVcIfIndex": belairCemVcIfIndex,
       "belairCemVcAdminState": belairCemVcAdminState,
       "belairCemVcOperStatus": belairCemVcOperStatus,
       "belairCemVcDestMacAddress": belairCemVcDestMacAddress,
       "belairCemVcArpEnabled": belairCemVcArpEnabled,
       "belairCemVcDestIpAddress": belairCemVcDestIpAddress,
       "belairCemVcTos": belairCemVcTos,
       "belairCemVcDestUdpPort": belairCemVcDestUdpPort,
       "belairCemVcSrcUdpPort": belairCemVcSrcUdpPort,
       "belairCemVcRtpPayloadType": belairCemVcRtpPayloadType,
       "belairCemVcRtpSsrc": belairCemVcRtpSsrc,
       "belairCemVcJitterBufferSize": belairCemVcJitterBufferSize,
       "belairCemVcFramesPerPktRx": belairCemVcFramesPerPktRx,
       "belairCemVcFramesPerPktTx": belairCemVcFramesPerPktTx,
       "belairCemVcCurrentIndications": belairCemVcCurrentIndications,
       "belairCemVcPerfCurrTable": belairCemVcPerfCurrTable,
       "belairCemVcPerfCurrEntry": belairCemVcPerfCurrEntry,
       "belairCemVcPerfCurrESs": belairCemVcPerfCurrESs,
       "belairCemVcPerfCurrSESs": belairCemVcPerfCurrSESs,
       "belairCemVcPerfCurrUASs": belairCemVcPerfCurrUASs,
       "belairCemVcPerfCurrFarEndESs": belairCemVcPerfCurrFarEndESs,
       "belairCemVcPerfCurrFarEndSESs": belairCemVcPerfCurrFarEndSESs,
       "belairCemVcPerfCurrFarEndUASs": belairCemVcPerfCurrFarEndUASs,
       "belairCemVcPerfCurrEarlyPkts": belairCemVcPerfCurrEarlyPkts,
       "belairCemVcPerfCurrLatePkts": belairCemVcPerfCurrLatePkts,
       "belairCemVcPerfCurrUnderrunPkts": belairCemVcPerfCurrUnderrunPkts,
       "belairCemVcPerfCurrLBitESs": belairCemVcPerfCurrLBitESs,
       "belairCemVcPerfCurrLBitSESs": belairCemVcPerfCurrLBitSESs,
       "belairCemVcPerfIntervalTable": belairCemVcPerfIntervalTable,
       "belairCemVcPerfIntervalEntry": belairCemVcPerfIntervalEntry,
       "belairCemVcPerfIntervalNumber": belairCemVcPerfIntervalNumber,
       "belairCemVcPerfIntervalValid": belairCemVcPerfIntervalValid,
       "belairCemVcPerfIntervalESs": belairCemVcPerfIntervalESs,
       "belairCemVcPerfIntervalSESs": belairCemVcPerfIntervalSESs,
       "belairCemVcPerfIntervalUASs": belairCemVcPerfIntervalUASs,
       "belairCemVcPerfIntervalFarEndESs": belairCemVcPerfIntervalFarEndESs,
       "belairCemVcPerfIntervalFarEndSESs": belairCemVcPerfIntervalFarEndSESs,
       "belairCemVcPerfIntervalFarEndUASs": belairCemVcPerfIntervalFarEndUASs,
       "belairCemVcPerfIntervalEarlyPkts": belairCemVcPerfIntervalEarlyPkts,
       "belairCemVcPerfIntervalLatePkts": belairCemVcPerfIntervalLatePkts,
       "belairCemVcPerfIntervalUnderrunPkts": belairCemVcPerfIntervalUnderrunPkts,
       "belairCemVcPerfIntervalLBitESs": belairCemVcPerfIntervalLBitESs,
       "belairCemVcPerfIntervalLBitSESs": belairCemVcPerfIntervalLBitSESs,
       "belairCemVcPerfTotalTable": belairCemVcPerfTotalTable,
       "belairCemVcPerfTotalEntry": belairCemVcPerfTotalEntry,
       "belairCemVcPerfTotalESs": belairCemVcPerfTotalESs,
       "belairCemVcPerfTotalSESs": belairCemVcPerfTotalSESs,
       "belairCemVcPerfTotalUASs": belairCemVcPerfTotalUASs,
       "belairCemVcPerfTotalFarEndESs": belairCemVcPerfTotalFarEndESs,
       "belairCemVcPerfTotalFarEndSESs": belairCemVcPerfTotalFarEndSESs,
       "belairCemVcPerfTotalFarEndUASs": belairCemVcPerfTotalFarEndUASs,
       "belairCemVcPerfTotalEarlyPkts": belairCemVcPerfTotalEarlyPkts,
       "belairCemVcPerfTotalLatePkts": belairCemVcPerfTotalLatePkts,
       "belairCemVcPerfTotalUnderrunPkts": belairCemVcPerfTotalUnderrunPkts,
       "belairCemVcPerfTotalLBitESs": belairCemVcPerfTotalLBitESs,
       "belairCemVcPerfTotalLBitSESs": belairCemVcPerfTotalLBitSESs,
       "belairCemTraps": belairCemTraps,
       "belairCemTrapsV2": belairCemTrapsV2,
       "belairCemOperStatusChange": belairCemOperStatusChange,
       "belairCemVcOperStatusChange": belairCemVcOperStatusChange,
       "belairCemVcAlarmStatusChange": belairCemVcAlarmStatusChange,
       "belairCemConformance": belairCemConformance,
       "belairCemGroup": belairCemGroup,
       "belairCemNotificationGroup": belairCemNotificationGroup}
)
