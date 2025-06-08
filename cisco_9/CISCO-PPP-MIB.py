# SNMP MIB module (CISCO-PPP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-PPP-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 00:13:25 2025
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(InterfaceIndex,
 InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
    "ifIndex")

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

ciscoPPPMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 419)
)
if mibBuilder.loadTexts:
    ciscoPPPMIB.setRevisions(
        ("2004-08-10 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoPPPMIBObjects_ObjectIdentity = ObjectIdentity
ciscoPPPMIBObjects = _CiscoPPPMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 419, 1)
)
_CpppLinkConfig_ObjectIdentity = ObjectIdentity
cpppLinkConfig = _CpppLinkConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 419, 1, 1)
)
_CpppLinkTable_Object = MibTable
cpppLinkTable = _CpppLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 419, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cpppLinkTable.setStatus("current")
_CpppLinkEntry_Object = MibTableRow
cpppLinkEntry = _CpppLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 419, 1, 1, 1, 1)
)
cpppLinkEntry.setIndexNames(
    (0, "CISCO-PPP-MIB", "cpppLinkIndex"),
)
if mibBuilder.loadTexts:
    cpppLinkEntry.setStatus("current")


class _CpppLinkIndex_Type(Unsigned32):
    """Custom type cpppLinkIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CpppLinkIndex_Type.__name__ = "Unsigned32"
_CpppLinkIndex_Object = MibTableColumn
cpppLinkIndex = _CpppLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 419, 1, 1, 1, 1, 1),
    _CpppLinkIndex_Type()
)
cpppLinkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpppLinkIndex.setStatus("current")
_CpppLinkIfIndex_Type = InterfaceIndex
_CpppLinkIfIndex_Object = MibTableColumn
cpppLinkIfIndex = _CpppLinkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 419, 1, 1, 1, 1, 2),
    _CpppLinkIfIndex_Type()
)
cpppLinkIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpppLinkIfIndex.setStatus("current")
_CpppLinkPhyIfIndex_Type = InterfaceIndex
_CpppLinkPhyIfIndex_Object = MibTableColumn
cpppLinkPhyIfIndex = _CpppLinkPhyIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 419, 1, 1, 1, 1, 3),
    _CpppLinkPhyIfIndex_Type()
)
cpppLinkPhyIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpppLinkPhyIfIndex.setStatus("current")


class _CpppLinkBundleIfIndex_Type(InterfaceIndexOrZero):
    """Custom type cpppLinkBundleIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_CpppLinkBundleIfIndex_Type.__name__ = "InterfaceIndexOrZero"
_CpppLinkBundleIfIndex_Object = MibTableColumn
cpppLinkBundleIfIndex = _CpppLinkBundleIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 419, 1, 1, 1, 1, 4),
    _CpppLinkBundleIfIndex_Type()
)
cpppLinkBundleIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpppLinkBundleIfIndex.setStatus("current")
_CpppLinkDescriptor_Type = SnmpAdminString
_CpppLinkDescriptor_Object = MibTableColumn
cpppLinkDescriptor = _CpppLinkDescriptor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 419, 1, 1, 1, 1, 5),
    _CpppLinkDescriptor_Type()
)
cpppLinkDescriptor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpppLinkDescriptor.setStatus("current")


class _CpppLinkRestartTimer_Type(Unsigned32):
    """Custom type cpppLinkRestartTimer based on Unsigned32"""
    defaultValue = 3000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_CpppLinkRestartTimer_Type.__name__ = "Unsigned32"
_CpppLinkRestartTimer_Object = MibTableColumn
cpppLinkRestartTimer = _CpppLinkRestartTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 419, 1, 1, 1, 1, 6),
    _CpppLinkRestartTimer_Type()
)
cpppLinkRestartTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpppLinkRestartTimer.setStatus("current")
if mibBuilder.loadTexts:
    cpppLinkRestartTimer.setUnits("milliseconds")


class _CpppLinkMaxConfigReqRetry_Type(Unsigned32):
    """Custom type cpppLinkMaxConfigReqRetry based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CpppLinkMaxConfigReqRetry_Type.__name__ = "Unsigned32"
_CpppLinkMaxConfigReqRetry_Object = MibTableColumn
cpppLinkMaxConfigReqRetry = _CpppLinkMaxConfigReqRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 419, 1, 1, 1, 1, 7),
    _CpppLinkMaxConfigReqRetry_Type()
)
cpppLinkMaxConfigReqRetry.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpppLinkMaxConfigReqRetry.setStatus("current")


class _CpppLinkMaxTerminateReqRetry_Type(Unsigned32):
    """Custom type cpppLinkMaxTerminateReqRetry based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CpppLinkMaxTerminateReqRetry_Type.__name__ = "Unsigned32"
_CpppLinkMaxTerminateReqRetry_Object = MibTableColumn
cpppLinkMaxTerminateReqRetry = _CpppLinkMaxTerminateReqRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 419, 1, 1, 1, 1, 8),
    _CpppLinkMaxTerminateReqRetry_Type()
)
cpppLinkMaxTerminateReqRetry.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpppLinkMaxTerminateReqRetry.setStatus("current")


class _CpppLinkMaxFailures_Type(Unsigned32):
    """Custom type cpppLinkMaxFailures based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CpppLinkMaxFailures_Type.__name__ = "Unsigned32"
_CpppLinkMaxFailures_Object = MibTableColumn
cpppLinkMaxFailures = _CpppLinkMaxFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 419, 1, 1, 1, 1, 9),
    _CpppLinkMaxFailures_Type()
)
cpppLinkMaxFailures.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpppLinkMaxFailures.setStatus("current")


class _CpppLinkLcpTimeout_Type(Unsigned32):
    """Custom type cpppLinkLcpTimeout based on Unsigned32"""
    defaultValue = 10000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CpppLinkLcpTimeout_Type.__name__ = "Unsigned32"
_CpppLinkLcpTimeout_Object = MibTableColumn
cpppLinkLcpTimeout = _CpppLinkLcpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 419, 1, 1, 1, 1, 10),
    _CpppLinkLcpTimeout_Type()
)
cpppLinkLcpTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpppLinkLcpTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cpppLinkLcpTimeout.setUnits("milliseconds")


class _CpppLinkLcpMRU_Type(Unsigned32):
    """Custom type cpppLinkLcpMRU based on Unsigned32"""
    defaultValue = 1500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CpppLinkLcpMRU_Type.__name__ = "Unsigned32"
_CpppLinkLcpMRU_Object = MibTableColumn
cpppLinkLcpMRU = _CpppLinkLcpMRU_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 419, 1, 1, 1, 1, 11),
    _CpppLinkLcpMRU_Type()
)
cpppLinkLcpMRU.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpppLinkLcpMRU.setStatus("current")
if mibBuilder.loadTexts:
    cpppLinkLcpMRU.setUnits("octets")


class _CpppLinkLcpPFCTransmit_Type(TruthValue):
    """Custom type cpppLinkLcpPFCTransmit based on TruthValue"""
    defaultValue = 2


_CpppLinkLcpPFCTransmit_Type.__name__ = "TruthValue"
_CpppLinkLcpPFCTransmit_Object = MibTableColumn
cpppLinkLcpPFCTransmit = _CpppLinkLcpPFCTransmit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 419, 1, 1, 1, 1, 12),
    _CpppLinkLcpPFCTransmit_Type()
)
cpppLinkLcpPFCTransmit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpppLinkLcpPFCTransmit.setStatus("current")
_CpppLinkLcpPFCTransmitOper_Type = TruthValue
_CpppLinkLcpPFCTransmitOper_Object = MibTableColumn
cpppLinkLcpPFCTransmitOper = _CpppLinkLcpPFCTransmitOper_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 419, 1, 1, 1, 1, 13),
    _CpppLinkLcpPFCTransmitOper_Type()
)
cpppLinkLcpPFCTransmitOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpppLinkLcpPFCTransmitOper.setStatus("current")


class _CpppLinkLcpPFCReceive_Type(TruthValue):
    """Custom type cpppLinkLcpPFCReceive based on TruthValue"""
    defaultValue = 2


_CpppLinkLcpPFCReceive_Type.__name__ = "TruthValue"
_CpppLinkLcpPFCReceive_Object = MibTableColumn
cpppLinkLcpPFCReceive = _CpppLinkLcpPFCReceive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 419, 1, 1, 1, 1, 14),
    _CpppLinkLcpPFCReceive_Type()
)
cpppLinkLcpPFCReceive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpppLinkLcpPFCReceive.setStatus("current")


class _CpppLinkLcpACFCTransmit_Type(TruthValue):
    """Custom type cpppLinkLcpACFCTransmit based on TruthValue"""
    defaultValue = 2


_CpppLinkLcpACFCTransmit_Type.__name__ = "TruthValue"
_CpppLinkLcpACFCTransmit_Object = MibTableColumn
cpppLinkLcpACFCTransmit = _CpppLinkLcpACFCTransmit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 419, 1, 1, 1, 1, 15),
    _CpppLinkLcpACFCTransmit_Type()
)
cpppLinkLcpACFCTransmit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpppLinkLcpACFCTransmit.setStatus("current")
_CpppLinkLcpACFCTransmitOper_Type = TruthValue
_CpppLinkLcpACFCTransmitOper_Object = MibTableColumn
cpppLinkLcpACFCTransmitOper = _CpppLinkLcpACFCTransmitOper_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 419, 1, 1, 1, 1, 16),
    _CpppLinkLcpACFCTransmitOper_Type()
)
cpppLinkLcpACFCTransmitOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpppLinkLcpACFCTransmitOper.setStatus("current")


class _CpppLinkLcpACFCReceive_Type(TruthValue):
    """Custom type cpppLinkLcpACFCReceive based on TruthValue"""
    defaultValue = 2


_CpppLinkLcpACFCReceive_Type.__name__ = "TruthValue"
_CpppLinkLcpACFCReceive_Object = MibTableColumn
cpppLinkLcpACFCReceive = _CpppLinkLcpACFCReceive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 419, 1, 1, 1, 1, 17),
    _CpppLinkLcpACFCReceive_Type()
)
cpppLinkLcpACFCReceive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpppLinkLcpACFCReceive.setStatus("current")


class _CpppLinkLcpLoopCheck_Type(TruthValue):
    """Custom type cpppLinkLcpLoopCheck based on TruthValue"""
    defaultValue = 2


_CpppLinkLcpLoopCheck_Type.__name__ = "TruthValue"
_CpppLinkLcpLoopCheck_Object = MibTableColumn
cpppLinkLcpLoopCheck = _CpppLinkLcpLoopCheck_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 419, 1, 1, 1, 1, 18),
    _CpppLinkLcpLoopCheck_Type()
)
cpppLinkLcpLoopCheck.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpppLinkLcpLoopCheck.setStatus("current")


class _CpppLinkLcpMaxEchoReqRetry_Type(Unsigned32):
    """Custom type cpppLinkLcpMaxEchoReqRetry based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CpppLinkLcpMaxEchoReqRetry_Type.__name__ = "Unsigned32"
_CpppLinkLcpMaxEchoReqRetry_Object = MibTableColumn
cpppLinkLcpMaxEchoReqRetry = _CpppLinkLcpMaxEchoReqRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 419, 1, 1, 1, 1, 19),
    _CpppLinkLcpMaxEchoReqRetry_Type()
)
cpppLinkLcpMaxEchoReqRetry.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpppLinkLcpMaxEchoReqRetry.setStatus("current")


class _CpppLinkStatus_Type(Bits):
    """Custom type cpppLinkStatus based on Bits"""
    namedValues = NamedValues(
        *(("pppLinkNoAlarm", 0),
          ("pppLinkLowerLayerDown", 1),
          ("pppLinkAdminDown", 2),
          ("pppKeepAliveTimeOut", 3),
          ("pppRecGoodConfigInOpen", 4),
          ("pppRecBadConfigInOpen", 5),
          ("pppRecConfigAck", 6),
          ("pppRecConfigNackReject", 7),
          ("pppRecTerminateAck", 8),
          ("pppRecTerminateReq", 9),
          ("pppRecUnknowCode", 10),
          ("pppRecGoodCodeReject", 11),
          ("pppRecBadCodeReject", 12),
          ("pppRecGoodProtoReject", 13),
          ("pppRecBadProtoReject", 14),
          ("pppNegotiationFail", 15),
          ("pppHardwareFail", 16),
          ("pppMaxFailures", 17),
          ("pppMaxConfigures", 18),
          ("pppInLoopback", 19),
          ("pppUnspecified", 20))
    )

_CpppLinkStatus_Type.__name__ = "Bits"
_CpppLinkStatus_Object = MibTableColumn
cpppLinkStatus = _CpppLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 419, 1, 1, 1, 1, 20),
    _CpppLinkStatus_Type()
)
cpppLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpppLinkStatus.setStatus("current")


class _CpppLinkRemoteMRU_Type(Unsigned32):
    """Custom type cpppLinkRemoteMRU based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CpppLinkRemoteMRU_Type.__name__ = "Unsigned32"
_CpppLinkRemoteMRU_Object = MibTableColumn
cpppLinkRemoteMRU = _CpppLinkRemoteMRU_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 419, 1, 1, 1, 1, 21),
    _CpppLinkRemoteMRU_Type()
)
cpppLinkRemoteMRU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpppLinkRemoteMRU.setStatus("current")
if mibBuilder.loadTexts:
    cpppLinkRemoteMRU.setUnits("octets")


class _CpppLinkMagicNumber_Type(Unsigned32):
    """Custom type cpppLinkMagicNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CpppLinkMagicNumber_Type.__name__ = "Unsigned32"
_CpppLinkMagicNumber_Object = MibTableColumn
cpppLinkMagicNumber = _CpppLinkMagicNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 419, 1, 1, 1, 1, 22),
    _CpppLinkMagicNumber_Type()
)
cpppLinkMagicNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpppLinkMagicNumber.setStatus("current")
_CpppLinkRowStatus_Type = RowStatus
_CpppLinkRowStatus_Object = MibTableColumn
cpppLinkRowStatus = _CpppLinkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 419, 1, 1, 1, 1, 23),
    _CpppLinkRowStatus_Type()
)
cpppLinkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpppLinkRowStatus.setStatus("current")
_CpppStatsTable_Object = MibTable
cpppStatsTable = _CpppStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 419, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cpppStatsTable.setStatus("current")
_CpppStatsEntry_Object = MibTableRow
cpppStatsEntry = _CpppStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 419, 1, 1, 2, 1)
)
cpppStatsEntry.setIndexNames(
    (0, "CISCO-PPP-MIB", "cpppLinkIndex"),
)
if mibBuilder.loadTexts:
    cpppStatsEntry.setStatus("current")
_CpppReceivePackets_Type = Counter32
_CpppReceivePackets_Object = MibTableColumn
cpppReceivePackets = _CpppReceivePackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 419, 1, 1, 2, 1, 1),
    _CpppReceivePackets_Type()
)
cpppReceivePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpppReceivePackets.setStatus("current")
if mibBuilder.loadTexts:
    cpppReceivePackets.setUnits("packets")
_CpppReceiveBytes_Type = Counter32
_CpppReceiveBytes_Object = MibTableColumn
cpppReceiveBytes = _CpppReceiveBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 419, 1, 1, 2, 1, 2),
    _CpppReceiveBytes_Type()
)
cpppReceiveBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpppReceiveBytes.setStatus("current")
if mibBuilder.loadTexts:
    cpppReceiveBytes.setUnits("bytes")
_CpppReceiveErrorBytes_Type = Counter32
_CpppReceiveErrorBytes_Object = MibTableColumn
cpppReceiveErrorBytes = _CpppReceiveErrorBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 419, 1, 1, 2, 1, 3),
    _CpppReceiveErrorBytes_Type()
)
cpppReceiveErrorBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpppReceiveErrorBytes.setStatus("current")
if mibBuilder.loadTexts:
    cpppReceiveErrorBytes.setUnits("bytes")
_CpppReceiveMRUErrors_Type = Counter32
_CpppReceiveMRUErrors_Object = MibTableColumn
cpppReceiveMRUErrors = _CpppReceiveMRUErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 419, 1, 1, 2, 1, 4),
    _CpppReceiveMRUErrors_Type()
)
cpppReceiveMRUErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpppReceiveMRUErrors.setStatus("current")
if mibBuilder.loadTexts:
    cpppReceiveMRUErrors.setUnits("packets")
_CpppReceiveDiscardPackets_Type = Counter32
_CpppReceiveDiscardPackets_Object = MibTableColumn
cpppReceiveDiscardPackets = _CpppReceiveDiscardPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 419, 1, 1, 2, 1, 5),
    _CpppReceiveDiscardPackets_Type()
)
cpppReceiveDiscardPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpppReceiveDiscardPackets.setStatus("current")
if mibBuilder.loadTexts:
    cpppReceiveDiscardPackets.setUnits("packets")
_CpppReceiveFCSErrorPackets_Type = Counter32
_CpppReceiveFCSErrorPackets_Object = MibTableColumn
cpppReceiveFCSErrorPackets = _CpppReceiveFCSErrorPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 419, 1, 1, 2, 1, 6),
    _CpppReceiveFCSErrorPackets_Type()
)
cpppReceiveFCSErrorPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpppReceiveFCSErrorPackets.setStatus("current")
if mibBuilder.loadTexts:
    cpppReceiveFCSErrorPackets.setUnits("packets")
_CpppReceiveACFCErrorPackets_Type = Counter32
_CpppReceiveACFCErrorPackets_Object = MibTableColumn
cpppReceiveACFCErrorPackets = _CpppReceiveACFCErrorPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 419, 1, 1, 2, 1, 7),
    _CpppReceiveACFCErrorPackets_Type()
)
cpppReceiveACFCErrorPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpppReceiveACFCErrorPackets.setStatus("current")
if mibBuilder.loadTexts:
    cpppReceiveACFCErrorPackets.setUnits("packets")
_CpppReceiveUnrecogPIDs_Type = Counter32
_CpppReceiveUnrecogPIDs_Object = MibTableColumn
cpppReceiveUnrecogPIDs = _CpppReceiveUnrecogPIDs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 419, 1, 1, 2, 1, 8),
    _CpppReceiveUnrecogPIDs_Type()
)
cpppReceiveUnrecogPIDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpppReceiveUnrecogPIDs.setStatus("current")
_CpppSendPackets_Type = Counter32
_CpppSendPackets_Object = MibTableColumn
cpppSendPackets = _CpppSendPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 419, 1, 1, 2, 1, 9),
    _CpppSendPackets_Type()
)
cpppSendPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpppSendPackets.setStatus("current")
if mibBuilder.loadTexts:
    cpppSendPackets.setUnits("packets")
_CpppSendBytes_Type = Counter32
_CpppSendBytes_Object = MibTableColumn
cpppSendBytes = _CpppSendBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 419, 1, 1, 2, 1, 10),
    _CpppSendBytes_Type()
)
cpppSendBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpppSendBytes.setStatus("current")
if mibBuilder.loadTexts:
    cpppSendBytes.setUnits("bytes")
_CpppMuxTable_Object = MibTable
cpppMuxTable = _CpppMuxTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 419, 1, 1, 4)
)
if mibBuilder.loadTexts:
    cpppMuxTable.setStatus("current")
_CpppMuxEntry_Object = MibTableRow
cpppMuxEntry = _CpppMuxEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 419, 1, 1, 4, 1)
)
cpppMuxEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cpppMuxEntry.setStatus("current")


class _CpppMuxEnable_Type(TruthValue):
    """Custom type cpppMuxEnable based on TruthValue"""
    defaultValue = 2


_CpppMuxEnable_Type.__name__ = "TruthValue"
_CpppMuxEnable_Object = MibTableColumn
cpppMuxEnable = _CpppMuxEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 419, 1, 1, 4, 1, 1),
    _CpppMuxEnable_Type()
)
cpppMuxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpppMuxEnable.setStatus("current")


class _CpppMuxOperStatus_Type(Integer32):
    """Custom type cpppMuxOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2),
          ("notInService", 3))
    )


_CpppMuxOperStatus_Type.__name__ = "Integer32"
_CpppMuxOperStatus_Object = MibTableColumn
cpppMuxOperStatus = _CpppMuxOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 419, 1, 1, 4, 1, 2),
    _CpppMuxOperStatus_Type()
)
cpppMuxOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpppMuxOperStatus.setStatus("current")


class _CpppDeMuxEnable_Type(TruthValue):
    """Custom type cpppDeMuxEnable based on TruthValue"""
    defaultValue = 2


_CpppDeMuxEnable_Type.__name__ = "TruthValue"
_CpppDeMuxEnable_Object = MibTableColumn
cpppDeMuxEnable = _CpppDeMuxEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 419, 1, 1, 4, 1, 3),
    _CpppDeMuxEnable_Type()
)
cpppDeMuxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpppDeMuxEnable.setStatus("current")


class _CpppDeMuxOperStatus_Type(Integer32):
    """Custom type cpppDeMuxOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2),
          ("notInService", 3))
    )


_CpppDeMuxOperStatus_Type.__name__ = "Integer32"
_CpppDeMuxOperStatus_Object = MibTableColumn
cpppDeMuxOperStatus = _CpppDeMuxOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 419, 1, 1, 4, 1, 4),
    _CpppDeMuxOperStatus_Type()
)
cpppDeMuxOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpppDeMuxOperStatus.setStatus("current")


class _CpppDeMuxPid_Type(Unsigned32):
    """Custom type cpppDeMuxPid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpppDeMuxPid_Type.__name__ = "Unsigned32"
_CpppDeMuxPid_Object = MibTableColumn
cpppDeMuxPid = _CpppDeMuxPid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 419, 1, 1, 4, 1, 5),
    _CpppDeMuxPid_Type()
)
cpppDeMuxPid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpppDeMuxPid.setStatus("current")


class _CpppDeMuxRemotePid_Type(Unsigned32):
    """Custom type cpppDeMuxRemotePid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpppDeMuxRemotePid_Type.__name__ = "Unsigned32"
_CpppDeMuxRemotePid_Object = MibTableColumn
cpppDeMuxRemotePid = _CpppDeMuxRemotePid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 419, 1, 1, 4, 1, 6),
    _CpppDeMuxRemotePid_Type()
)
cpppDeMuxRemotePid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpppDeMuxRemotePid.setStatus("current")


class _CpppMuxMaxSubFrameCount_Type(Unsigned32):
    """Custom type cpppMuxMaxSubFrameCount based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpppMuxMaxSubFrameCount_Type.__name__ = "Unsigned32"
_CpppMuxMaxSubFrameCount_Object = MibTableColumn
cpppMuxMaxSubFrameCount = _CpppMuxMaxSubFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 419, 1, 1, 4, 1, 7),
    _CpppMuxMaxSubFrameCount_Type()
)
cpppMuxMaxSubFrameCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpppMuxMaxSubFrameCount.setStatus("current")


class _CpppMuxMaxSubFrameLen_Type(Unsigned32):
    """Custom type cpppMuxMaxSubFrameLen based on Unsigned32"""
    defaultValue = 64

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CpppMuxMaxSubFrameLen_Type.__name__ = "Unsigned32"
_CpppMuxMaxSubFrameLen_Object = MibTableColumn
cpppMuxMaxSubFrameLen = _CpppMuxMaxSubFrameLen_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 419, 1, 1, 4, 1, 8),
    _CpppMuxMaxSubFrameLen_Type()
)
cpppMuxMaxSubFrameLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpppMuxMaxSubFrameLen.setStatus("current")
if mibBuilder.loadTexts:
    cpppMuxMaxSubFrameLen.setUnits("bytes")


class _CpppMuxMaxFrameLen_Type(Unsigned32):
    """Custom type cpppMuxMaxFrameLen based on Unsigned32"""
    defaultValue = 256

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CpppMuxMaxFrameLen_Type.__name__ = "Unsigned32"
_CpppMuxMaxFrameLen_Object = MibTableColumn
cpppMuxMaxFrameLen = _CpppMuxMaxFrameLen_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 419, 1, 1, 4, 1, 9),
    _CpppMuxMaxFrameLen_Type()
)
cpppMuxMaxFrameLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpppMuxMaxFrameLen.setStatus("current")
if mibBuilder.loadTexts:
    cpppMuxMaxFrameLen.setUnits("bytes")


class _CpppMuxTimer_Type(Unsigned32):
    """Custom type cpppMuxTimer based on Unsigned32"""
    defaultValue = 600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CpppMuxTimer_Type.__name__ = "Unsigned32"
_CpppMuxTimer_Object = MibTableColumn
cpppMuxTimer = _CpppMuxTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 419, 1, 1, 4, 1, 10),
    _CpppMuxTimer_Type()
)
cpppMuxTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpppMuxTimer.setStatus("current")
if mibBuilder.loadTexts:
    cpppMuxTimer.setUnits("microseconds")


class _CpppMuxProtocolStatus_Type(Bits):
    """Custom type cpppMuxProtocolStatus based on Bits"""
    namedValues = NamedValues(
        *(("pppMuxNotInService", 0),
          ("pppMuxActive", 1),
          ("pppMuxLowerLayerDown", 2),
          ("pppMuxRecGoodConfig", 3),
          ("pppMuxRecBadConfig", 4),
          ("pppMuxRecConfigAck", 5),
          ("pppMuxRecConfigNackReject", 6),
          ("pppMuxRecTerminateAck", 7),
          ("pppMuxRecTerminateRequest", 8),
          ("pppMuxRecUnknowCode", 9),
          ("pppMuxRecGoodCodeReject", 10),
          ("pppMuxRecBadCodeReject", 11),
          ("pppMuxRecGoodProtoReject", 12),
          ("pppMuxRecBadProtoReject", 13),
          ("pppMuxNegotiationFail", 14),
          ("pppMuxHardwareFail", 15),
          ("pppMuxMaxFailures", 16),
          ("pppMuxMaxConfigures", 17),
          ("pppMuxUnspecified", 18))
    )

_CpppMuxProtocolStatus_Type.__name__ = "Bits"
_CpppMuxProtocolStatus_Object = MibTableColumn
cpppMuxProtocolStatus = _CpppMuxProtocolStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 419, 1, 1, 4, 1, 11),
    _CpppMuxProtocolStatus_Type()
)
cpppMuxProtocolStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpppMuxProtocolStatus.setStatus("current")
_CpppMuxStatsTable_Object = MibTable
cpppMuxStatsTable = _CpppMuxStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 419, 1, 1, 5)
)
if mibBuilder.loadTexts:
    cpppMuxStatsTable.setStatus("current")
_CpppMuxStatsEntry_Object = MibTableRow
cpppMuxStatsEntry = _CpppMuxStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 419, 1, 1, 5, 1)
)
cpppMuxStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cpppMuxStatsEntry.setStatus("current")
_CpppMuxReceiveSubframes_Type = Counter32
_CpppMuxReceiveSubframes_Object = MibTableColumn
cpppMuxReceiveSubframes = _CpppMuxReceiveSubframes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 419, 1, 1, 5, 1, 1),
    _CpppMuxReceiveSubframes_Type()
)
cpppMuxReceiveSubframes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpppMuxReceiveSubframes.setStatus("current")
if mibBuilder.loadTexts:
    cpppMuxReceiveSubframes.setUnits("frames")
_CpppMuxReceivePackets_Type = Counter32
_CpppMuxReceivePackets_Object = MibTableColumn
cpppMuxReceivePackets = _CpppMuxReceivePackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 419, 1, 1, 5, 1, 2),
    _CpppMuxReceivePackets_Type()
)
cpppMuxReceivePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpppMuxReceivePackets.setStatus("current")
if mibBuilder.loadTexts:
    cpppMuxReceivePackets.setUnits("packets")
_CpppMuxReceiveErrorPackets_Type = Counter32
_CpppMuxReceiveErrorPackets_Object = MibTableColumn
cpppMuxReceiveErrorPackets = _CpppMuxReceiveErrorPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 419, 1, 1, 5, 1, 3),
    _CpppMuxReceiveErrorPackets_Type()
)
cpppMuxReceiveErrorPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpppMuxReceiveErrorPackets.setStatus("current")
if mibBuilder.loadTexts:
    cpppMuxReceiveErrorPackets.setUnits("packets")
_CpppMuxSendSubframes_Type = Counter32
_CpppMuxSendSubframes_Object = MibTableColumn
cpppMuxSendSubframes = _CpppMuxSendSubframes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 419, 1, 1, 5, 1, 4),
    _CpppMuxSendSubframes_Type()
)
cpppMuxSendSubframes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpppMuxSendSubframes.setStatus("current")
if mibBuilder.loadTexts:
    cpppMuxSendSubframes.setUnits("frames")
_CpppMuxSendPackets_Type = Counter32
_CpppMuxSendPackets_Object = MibTableColumn
cpppMuxSendPackets = _CpppMuxSendPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 419, 1, 1, 5, 1, 5),
    _CpppMuxSendPackets_Type()
)
cpppMuxSendPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpppMuxSendPackets.setStatus("current")
if mibBuilder.loadTexts:
    cpppMuxSendPackets.setUnits("packets")
_CpppMuxSendNotMuxPackets_Type = Counter32
_CpppMuxSendNotMuxPackets_Object = MibTableColumn
cpppMuxSendNotMuxPackets = _CpppMuxSendNotMuxPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 419, 1, 1, 5, 1, 6),
    _CpppMuxSendNotMuxPackets_Type()
)
cpppMuxSendNotMuxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpppMuxSendNotMuxPackets.setStatus("current")
_CiscoPPPMIBConform_ObjectIdentity = ObjectIdentity
ciscoPPPMIBConform = _CiscoPPPMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 419, 2)
)
_CiscoPPPMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoPPPMIBCompliances = _CiscoPPPMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 419, 2, 1)
)
_CiscoPPPMIBGroups_ObjectIdentity = ObjectIdentity
ciscoPPPMIBGroups = _CiscoPPPMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 419, 2, 2)
)

# Managed Objects groups

ciscoPPPLinkGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 419, 2, 2, 1)
)
ciscoPPPLinkGroup.setObjects(
      *(("CISCO-PPP-MIB", "cpppLinkIfIndex"),
        ("CISCO-PPP-MIB", "cpppLinkRowStatus"),
        ("CISCO-PPP-MIB", "cpppLinkPhyIfIndex"),
        ("CISCO-PPP-MIB", "cpppLinkBundleIfIndex"),
        ("CISCO-PPP-MIB", "cpppLinkDescriptor"),
        ("CISCO-PPP-MIB", "cpppLinkRestartTimer"),
        ("CISCO-PPP-MIB", "cpppLinkMaxConfigReqRetry"),
        ("CISCO-PPP-MIB", "cpppLinkMaxTerminateReqRetry"),
        ("CISCO-PPP-MIB", "cpppLinkMaxFailures"),
        ("CISCO-PPP-MIB", "cpppLinkLcpTimeout"),
        ("CISCO-PPP-MIB", "cpppLinkLcpMRU"),
        ("CISCO-PPP-MIB", "cpppLinkLcpPFCTransmit"),
        ("CISCO-PPP-MIB", "cpppLinkLcpPFCTransmitOper"),
        ("CISCO-PPP-MIB", "cpppLinkLcpPFCReceive"),
        ("CISCO-PPP-MIB", "cpppLinkLcpACFCTransmit"),
        ("CISCO-PPP-MIB", "cpppLinkLcpACFCTransmitOper"),
        ("CISCO-PPP-MIB", "cpppLinkLcpACFCReceive"),
        ("CISCO-PPP-MIB", "cpppLinkLcpLoopCheck"),
        ("CISCO-PPP-MIB", "cpppLinkLcpMaxEchoReqRetry"),
        ("CISCO-PPP-MIB", "cpppLinkStatus"),
        ("CISCO-PPP-MIB", "cpppLinkRemoteMRU"),
        ("CISCO-PPP-MIB", "cpppLinkMagicNumber"))
)
if mibBuilder.loadTexts:
    ciscoPPPLinkGroup.setStatus("current")

ciscoPPPLinkStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 419, 2, 2, 2)
)
ciscoPPPLinkStatsGroup.setObjects(
      *(("CISCO-PPP-MIB", "cpppReceivePackets"),
        ("CISCO-PPP-MIB", "cpppReceiveBytes"),
        ("CISCO-PPP-MIB", "cpppReceiveErrorBytes"),
        ("CISCO-PPP-MIB", "cpppReceiveMRUErrors"),
        ("CISCO-PPP-MIB", "cpppReceiveDiscardPackets"),
        ("CISCO-PPP-MIB", "cpppReceiveFCSErrorPackets"),
        ("CISCO-PPP-MIB", "cpppReceiveACFCErrorPackets"),
        ("CISCO-PPP-MIB", "cpppReceiveUnrecogPIDs"),
        ("CISCO-PPP-MIB", "cpppSendPackets"),
        ("CISCO-PPP-MIB", "cpppSendBytes"))
)
if mibBuilder.loadTexts:
    ciscoPPPLinkStatsGroup.setStatus("current")

ciscoPPPMuxGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 419, 2, 2, 3)
)
ciscoPPPMuxGroup.setObjects(
      *(("CISCO-PPP-MIB", "cpppMuxEnable"),
        ("CISCO-PPP-MIB", "cpppMuxOperStatus"),
        ("CISCO-PPP-MIB", "cpppDeMuxEnable"),
        ("CISCO-PPP-MIB", "cpppDeMuxOperStatus"),
        ("CISCO-PPP-MIB", "cpppDeMuxPid"),
        ("CISCO-PPP-MIB", "cpppDeMuxRemotePid"),
        ("CISCO-PPP-MIB", "cpppMuxMaxSubFrameCount"),
        ("CISCO-PPP-MIB", "cpppMuxMaxSubFrameLen"),
        ("CISCO-PPP-MIB", "cpppMuxMaxFrameLen"),
        ("CISCO-PPP-MIB", "cpppMuxTimer"),
        ("CISCO-PPP-MIB", "cpppMuxProtocolStatus"))
)
if mibBuilder.loadTexts:
    ciscoPPPMuxGroup.setStatus("current")

ciscoPPPMuxStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 419, 2, 2, 4)
)
ciscoPPPMuxStatsGroup.setObjects(
      *(("CISCO-PPP-MIB", "cpppMuxReceiveSubframes"),
        ("CISCO-PPP-MIB", "cpppMuxReceivePackets"),
        ("CISCO-PPP-MIB", "cpppMuxReceiveErrorPackets"),
        ("CISCO-PPP-MIB", "cpppMuxSendSubframes"),
        ("CISCO-PPP-MIB", "cpppMuxSendPackets"),
        ("CISCO-PPP-MIB", "cpppMuxSendNotMuxPackets"))
)
if mibBuilder.loadTexts:
    ciscoPPPMuxStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoPPPMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 419, 2, 1, 1)
)
ciscoPPPMIBCompliance.setObjects(
      *(("CISCO-PPP-MIB", "ciscoPPPLinkGroup"),
        ("CISCO-PPP-MIB", "ciscoPPPLinkStatsGroup"),
        ("CISCO-PPP-MIB", "ciscoPPPMuxGroup"),
        ("CISCO-PPP-MIB", "ciscoPPPMuxStatsGroup"))
)
if mibBuilder.loadTexts:
    ciscoPPPMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-PPP-MIB",
    **{"ciscoPPPMIB": ciscoPPPMIB,
       "ciscoPPPMIBObjects": ciscoPPPMIBObjects,
       "cpppLinkConfig": cpppLinkConfig,
       "cpppLinkTable": cpppLinkTable,
       "cpppLinkEntry": cpppLinkEntry,
       "cpppLinkIndex": cpppLinkIndex,
       "cpppLinkIfIndex": cpppLinkIfIndex,
       "cpppLinkPhyIfIndex": cpppLinkPhyIfIndex,
       "cpppLinkBundleIfIndex": cpppLinkBundleIfIndex,
       "cpppLinkDescriptor": cpppLinkDescriptor,
       "cpppLinkRestartTimer": cpppLinkRestartTimer,
       "cpppLinkMaxConfigReqRetry": cpppLinkMaxConfigReqRetry,
       "cpppLinkMaxTerminateReqRetry": cpppLinkMaxTerminateReqRetry,
       "cpppLinkMaxFailures": cpppLinkMaxFailures,
       "cpppLinkLcpTimeout": cpppLinkLcpTimeout,
       "cpppLinkLcpMRU": cpppLinkLcpMRU,
       "cpppLinkLcpPFCTransmit": cpppLinkLcpPFCTransmit,
       "cpppLinkLcpPFCTransmitOper": cpppLinkLcpPFCTransmitOper,
       "cpppLinkLcpPFCReceive": cpppLinkLcpPFCReceive,
       "cpppLinkLcpACFCTransmit": cpppLinkLcpACFCTransmit,
       "cpppLinkLcpACFCTransmitOper": cpppLinkLcpACFCTransmitOper,
       "cpppLinkLcpACFCReceive": cpppLinkLcpACFCReceive,
       "cpppLinkLcpLoopCheck": cpppLinkLcpLoopCheck,
       "cpppLinkLcpMaxEchoReqRetry": cpppLinkLcpMaxEchoReqRetry,
       "cpppLinkStatus": cpppLinkStatus,
       "cpppLinkRemoteMRU": cpppLinkRemoteMRU,
       "cpppLinkMagicNumber": cpppLinkMagicNumber,
       "cpppLinkRowStatus": cpppLinkRowStatus,
       "cpppStatsTable": cpppStatsTable,
       "cpppStatsEntry": cpppStatsEntry,
       "cpppReceivePackets": cpppReceivePackets,
       "cpppReceiveBytes": cpppReceiveBytes,
       "cpppReceiveErrorBytes": cpppReceiveErrorBytes,
       "cpppReceiveMRUErrors": cpppReceiveMRUErrors,
       "cpppReceiveDiscardPackets": cpppReceiveDiscardPackets,
       "cpppReceiveFCSErrorPackets": cpppReceiveFCSErrorPackets,
       "cpppReceiveACFCErrorPackets": cpppReceiveACFCErrorPackets,
       "cpppReceiveUnrecogPIDs": cpppReceiveUnrecogPIDs,
       "cpppSendPackets": cpppSendPackets,
       "cpppSendBytes": cpppSendBytes,
       "cpppMuxTable": cpppMuxTable,
       "cpppMuxEntry": cpppMuxEntry,
       "cpppMuxEnable": cpppMuxEnable,
       "cpppMuxOperStatus": cpppMuxOperStatus,
       "cpppDeMuxEnable": cpppDeMuxEnable,
       "cpppDeMuxOperStatus": cpppDeMuxOperStatus,
       "cpppDeMuxPid": cpppDeMuxPid,
       "cpppDeMuxRemotePid": cpppDeMuxRemotePid,
       "cpppMuxMaxSubFrameCount": cpppMuxMaxSubFrameCount,
       "cpppMuxMaxSubFrameLen": cpppMuxMaxSubFrameLen,
       "cpppMuxMaxFrameLen": cpppMuxMaxFrameLen,
       "cpppMuxTimer": cpppMuxTimer,
       "cpppMuxProtocolStatus": cpppMuxProtocolStatus,
       "cpppMuxStatsTable": cpppMuxStatsTable,
       "cpppMuxStatsEntry": cpppMuxStatsEntry,
       "cpppMuxReceiveSubframes": cpppMuxReceiveSubframes,
       "cpppMuxReceivePackets": cpppMuxReceivePackets,
       "cpppMuxReceiveErrorPackets": cpppMuxReceiveErrorPackets,
       "cpppMuxSendSubframes": cpppMuxSendSubframes,
       "cpppMuxSendPackets": cpppMuxSendPackets,
       "cpppMuxSendNotMuxPackets": cpppMuxSendNotMuxPackets,
       "ciscoPPPMIBConform": ciscoPPPMIBConform,
       "ciscoPPPMIBCompliances": ciscoPPPMIBCompliances,
       "ciscoPPPMIBCompliance": ciscoPPPMIBCompliance,
       "ciscoPPPMIBGroups": ciscoPPPMIBGroups,
       "ciscoPPPLinkGroup": ciscoPPPLinkGroup,
       "ciscoPPPLinkStatsGroup": ciscoPPPLinkStatsGroup,
       "ciscoPPPMuxGroup": ciscoPPPMuxGroup,
       "ciscoPPPMuxStatsGroup": ciscoPPPMuxStatsGroup}
)
