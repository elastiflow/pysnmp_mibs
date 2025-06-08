# SNMP MIB module (CLAB-GRE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cablelabs_4491/CLAB-GRE-MIB.mib
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

clabGREMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 4, 3)
)
if mibBuilder.loadTexts:
    clabGREMib.setRevisions(
        ("2015-02-04 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ClabGREObjects_ObjectIdentity = ObjectIdentity
clabGREObjects = _ClabGREObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 4, 3, 1)
)


class _ClabGRETunnelNumberOfEntries_Type(Unsigned32):
    """Custom type clabGRETunnelNumberOfEntries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_ClabGRETunnelNumberOfEntries_Type.__name__ = "Unsigned32"
_ClabGRETunnelNumberOfEntries_Object = MibScalar
clabGRETunnelNumberOfEntries = _ClabGRETunnelNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 3, 1, 1),
    _ClabGRETunnelNumberOfEntries_Type()
)
clabGRETunnelNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabGRETunnelNumberOfEntries.setStatus("current")


class _ClabGREFilterNumberOfEntries_Type(Unsigned32):
    """Custom type clabGREFilterNumberOfEntries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_ClabGREFilterNumberOfEntries_Type.__name__ = "Unsigned32"
_ClabGREFilterNumberOfEntries_Object = MibScalar
clabGREFilterNumberOfEntries = _ClabGREFilterNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 3, 1, 2),
    _ClabGREFilterNumberOfEntries_Type()
)
clabGREFilterNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabGREFilterNumberOfEntries.setStatus("current")
_ClabGRETunnelTable_Object = MibTable
clabGRETunnelTable = _ClabGRETunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 3, 1, 3)
)
if mibBuilder.loadTexts:
    clabGRETunnelTable.setStatus("current")
_ClabGRETunnelEntry_Object = MibTableRow
clabGRETunnelEntry = _ClabGRETunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 3, 1, 3, 1)
)
clabGRETunnelEntry.setIndexNames(
    (0, "CLAB-GRE-MIB", "clabGRETunnelIndex"),
)
if mibBuilder.loadTexts:
    clabGRETunnelEntry.setStatus("current")


class _ClabGRETunnelIndex_Type(Unsigned32):
    """Custom type clabGRETunnelIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(400, 499),
    )


_ClabGRETunnelIndex_Type.__name__ = "Unsigned32"
_ClabGRETunnelIndex_Object = MibTableColumn
clabGRETunnelIndex = _ClabGRETunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 3, 1, 3, 1, 1),
    _ClabGRETunnelIndex_Type()
)
clabGRETunnelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clabGRETunnelIndex.setStatus("current")
_ClabGRETunnelRowStatus_Type = RowStatus
_ClabGRETunnelRowStatus_Object = MibTableColumn
clabGRETunnelRowStatus = _ClabGRETunnelRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 3, 1, 3, 1, 2),
    _ClabGRETunnelRowStatus_Type()
)
clabGRETunnelRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabGRETunnelRowStatus.setStatus("current")
_ClabGRETunnelEnable_Type = TruthValue
_ClabGRETunnelEnable_Object = MibTableColumn
clabGRETunnelEnable = _ClabGRETunnelEnable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 3, 1, 3, 1, 3),
    _ClabGRETunnelEnable_Type()
)
clabGRETunnelEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabGRETunnelEnable.setStatus("current")


class _ClabGRETunnelStatus_Type(Integer32):
    """Custom type clabGRETunnelStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("error", 3),
          ("errorMisconfigured", 4),
          ("retryWait", 5))
    )


_ClabGRETunnelStatus_Type.__name__ = "Integer32"
_ClabGRETunnelStatus_Object = MibTableColumn
clabGRETunnelStatus = _ClabGRETunnelStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 3, 1, 3, 1, 4),
    _ClabGRETunnelStatus_Type()
)
clabGRETunnelStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabGRETunnelStatus.setStatus("current")
_ClabGRETunnelAlias_Type = SnmpAdminString
_ClabGRETunnelAlias_Object = MibTableColumn
clabGRETunnelAlias = _ClabGRETunnelAlias_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 3, 1, 3, 1, 5),
    _ClabGRETunnelAlias_Type()
)
clabGRETunnelAlias.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabGRETunnelAlias.setStatus("current")


class _ClabGRETunnelRemoteEndpoints_Type(OctetString):
    """Custom type clabGRETunnelRemoteEndpoints based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1040),
    )


_ClabGRETunnelRemoteEndpoints_Type.__name__ = "OctetString"
_ClabGRETunnelRemoteEndpoints_Object = MibTableColumn
clabGRETunnelRemoteEndpoints = _ClabGRETunnelRemoteEndpoints_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 3, 1, 3, 1, 6),
    _ClabGRETunnelRemoteEndpoints_Type()
)
clabGRETunnelRemoteEndpoints.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabGRETunnelRemoteEndpoints.setStatus("current")


class _ClabGRETunnelKeepAlivePolicy_Type(Integer32):
    """Custom type clabGRETunnelKeepAlivePolicy based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("icmp", 1),
          ("none", 2))
    )


_ClabGRETunnelKeepAlivePolicy_Type.__name__ = "Integer32"
_ClabGRETunnelKeepAlivePolicy_Object = MibTableColumn
clabGRETunnelKeepAlivePolicy = _ClabGRETunnelKeepAlivePolicy_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 3, 1, 3, 1, 7),
    _ClabGRETunnelKeepAlivePolicy_Type()
)
clabGRETunnelKeepAlivePolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabGRETunnelKeepAlivePolicy.setStatus("current")


class _ClabGRETunnelKeepAliveTimeout_Type(Unsigned32):
    """Custom type clabGRETunnelKeepAliveTimeout based on Unsigned32"""
    defaultValue = 10


_ClabGRETunnelKeepAliveTimeout_Type.__name__ = "Unsigned32"
_ClabGRETunnelKeepAliveTimeout_Object = MibTableColumn
clabGRETunnelKeepAliveTimeout = _ClabGRETunnelKeepAliveTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 3, 1, 3, 1, 8),
    _ClabGRETunnelKeepAliveTimeout_Type()
)
clabGRETunnelKeepAliveTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabGRETunnelKeepAliveTimeout.setStatus("current")
if mibBuilder.loadTexts:
    clabGRETunnelKeepAliveTimeout.setUnits("seconds")


class _ClabGRETunnelKeepAliveThreshold_Type(Unsigned32):
    """Custom type clabGRETunnelKeepAliveThreshold based on Unsigned32"""
    defaultValue = 3


_ClabGRETunnelKeepAliveThreshold_Type.__name__ = "Unsigned32"
_ClabGRETunnelKeepAliveThreshold_Object = MibTableColumn
clabGRETunnelKeepAliveThreshold = _ClabGRETunnelKeepAliveThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 3, 1, 3, 1, 9),
    _ClabGRETunnelKeepAliveThreshold_Type()
)
clabGRETunnelKeepAliveThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabGRETunnelKeepAliveThreshold.setStatus("current")
if mibBuilder.loadTexts:
    clabGRETunnelKeepAliveThreshold.setUnits("errors")


class _ClabGRETunnelKeepAliveCount_Type(Unsigned32):
    """Custom type clabGRETunnelKeepAliveCount based on Unsigned32"""
    defaultValue = 3


_ClabGRETunnelKeepAliveCount_Type.__name__ = "Unsigned32"
_ClabGRETunnelKeepAliveCount_Object = MibTableColumn
clabGRETunnelKeepAliveCount = _ClabGRETunnelKeepAliveCount_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 3, 1, 3, 1, 10),
    _ClabGRETunnelKeepAliveCount_Type()
)
clabGRETunnelKeepAliveCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabGRETunnelKeepAliveCount.setStatus("current")
if mibBuilder.loadTexts:
    clabGRETunnelKeepAliveCount.setUnits("packets")


class _ClabGRETunnelKeepAliveInterval_Type(Unsigned32):
    """Custom type clabGRETunnelKeepAliveInterval based on Unsigned32"""
    defaultValue = 60


_ClabGRETunnelKeepAliveInterval_Type.__name__ = "Unsigned32"
_ClabGRETunnelKeepAliveInterval_Object = MibTableColumn
clabGRETunnelKeepAliveInterval = _ClabGRETunnelKeepAliveInterval_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 3, 1, 3, 1, 11),
    _ClabGRETunnelKeepAliveInterval_Type()
)
clabGRETunnelKeepAliveInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabGRETunnelKeepAliveInterval.setStatus("current")
if mibBuilder.loadTexts:
    clabGRETunnelKeepAliveInterval.setUnits("seconds")


class _ClabGRETunnelKeepAliveFailureInterval_Type(Unsigned32):
    """Custom type clabGRETunnelKeepAliveFailureInterval based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ClabGRETunnelKeepAliveFailureInterval_Type.__name__ = "Unsigned32"
_ClabGRETunnelKeepAliveFailureInterval_Object = MibTableColumn
clabGRETunnelKeepAliveFailureInterval = _ClabGRETunnelKeepAliveFailureInterval_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 3, 1, 3, 1, 12),
    _ClabGRETunnelKeepAliveFailureInterval_Type()
)
clabGRETunnelKeepAliveFailureInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabGRETunnelKeepAliveFailureInterval.setStatus("current")
if mibBuilder.loadTexts:
    clabGRETunnelKeepAliveFailureInterval.setUnits("seconds")


class _ClabGRETunnelKeepAliveRecoverInterval_Type(Unsigned32):
    """Custom type clabGRETunnelKeepAliveRecoverInterval based on Unsigned32"""
    defaultValue = 43200


_ClabGRETunnelKeepAliveRecoverInterval_Type.__name__ = "Unsigned32"
_ClabGRETunnelKeepAliveRecoverInterval_Object = MibTableColumn
clabGRETunnelKeepAliveRecoverInterval = _ClabGRETunnelKeepAliveRecoverInterval_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 3, 1, 3, 1, 13),
    _ClabGRETunnelKeepAliveRecoverInterval_Type()
)
clabGRETunnelKeepAliveRecoverInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabGRETunnelKeepAliveRecoverInterval.setStatus("current")
if mibBuilder.loadTexts:
    clabGRETunnelKeepAliveRecoverInterval.setUnits("seconds")


class _ClabGRETunnelDeliveryHeaderProtocol_Type(Integer32):
    """Custom type clabGRETunnelDeliveryHeaderProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_ClabGRETunnelDeliveryHeaderProtocol_Type.__name__ = "Integer32"
_ClabGRETunnelDeliveryHeaderProtocol_Object = MibTableColumn
clabGRETunnelDeliveryHeaderProtocol = _ClabGRETunnelDeliveryHeaderProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 3, 1, 3, 1, 14),
    _ClabGRETunnelDeliveryHeaderProtocol_Type()
)
clabGRETunnelDeliveryHeaderProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabGRETunnelDeliveryHeaderProtocol.setStatus("current")
_ClabGRETunnelDefaultDscpMark_Type = Unsigned32
_ClabGRETunnelDefaultDscpMark_Object = MibTableColumn
clabGRETunnelDefaultDscpMark = _ClabGRETunnelDefaultDscpMark_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 3, 1, 3, 1, 15),
    _ClabGRETunnelDefaultDscpMark_Type()
)
clabGRETunnelDefaultDscpMark.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabGRETunnelDefaultDscpMark.setStatus("current")
_ClabGRETunnelConnectedRemoteEndpoint_Type = SnmpAdminString
_ClabGRETunnelConnectedRemoteEndpoint_Object = MibTableColumn
clabGRETunnelConnectedRemoteEndpoint = _ClabGRETunnelConnectedRemoteEndpoint_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 3, 1, 3, 1, 16),
    _ClabGRETunnelConnectedRemoteEndpoint_Type()
)
clabGRETunnelConnectedRemoteEndpoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabGRETunnelConnectedRemoteEndpoint.setStatus("current")


class _ClabGRETunnelInterfaceNumberOfEntries_Type(Unsigned32):
    """Custom type clabGRETunnelInterfaceNumberOfEntries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_ClabGRETunnelInterfaceNumberOfEntries_Type.__name__ = "Unsigned32"
_ClabGRETunnelInterfaceNumberOfEntries_Object = MibTableColumn
clabGRETunnelInterfaceNumberOfEntries = _ClabGRETunnelInterfaceNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 3, 1, 3, 1, 17),
    _ClabGRETunnelInterfaceNumberOfEntries_Type()
)
clabGRETunnelInterfaceNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabGRETunnelInterfaceNumberOfEntries.setStatus("current")


class _ClabGRETunnelTcpMssClamping_Type(Unsigned32):
    """Custom type clabGRETunnelTcpMssClamping based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1420),
    )


_ClabGRETunnelTcpMssClamping_Type.__name__ = "Unsigned32"
_ClabGRETunnelTcpMssClamping_Object = MibTableColumn
clabGRETunnelTcpMssClamping = _ClabGRETunnelTcpMssClamping_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 3, 1, 3, 1, 18),
    _ClabGRETunnelTcpMssClamping_Type()
)
clabGRETunnelTcpMssClamping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabGRETunnelTcpMssClamping.setStatus("current")
_ClabGRETunnelConcentratorServiceName_Type = SnmpAdminString
_ClabGRETunnelConcentratorServiceName_Object = MibTableColumn
clabGRETunnelConcentratorServiceName = _ClabGRETunnelConcentratorServiceName_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 3, 1, 3, 1, 19),
    _ClabGRETunnelConcentratorServiceName_Type()
)
clabGRETunnelConcentratorServiceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabGRETunnelConcentratorServiceName.setStatus("current")


class _ClabGRETunnnelRemoteEndpointConnectivityState_Type(OctetString):
    """Custom type clabGRETunnnelRemoteEndpointConnectivityState based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_ClabGRETunnnelRemoteEndpointConnectivityState_Type.__name__ = "OctetString"
_ClabGRETunnnelRemoteEndpointConnectivityState_Object = MibTableColumn
clabGRETunnnelRemoteEndpointConnectivityState = _ClabGRETunnnelRemoteEndpointConnectivityState_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 3, 1, 3, 1, 20),
    _ClabGRETunnnelRemoteEndpointConnectivityState_Type()
)
clabGRETunnnelRemoteEndpointConnectivityState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabGRETunnnelRemoteEndpointConnectivityState.setStatus("current")
_ClabGRETunnelStatsTable_Object = MibTable
clabGRETunnelStatsTable = _ClabGRETunnelStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 3, 1, 4)
)
if mibBuilder.loadTexts:
    clabGRETunnelStatsTable.setStatus("current")
_ClabGRETunnelStatsEntry_Object = MibTableRow
clabGRETunnelStatsEntry = _ClabGRETunnelStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 3, 1, 4, 1)
)
if mibBuilder.loadTexts:
    clabGRETunnelStatsEntry.setStatus("current")
_ClabGRETunnelStatsKeepAliveSent_Type = Counter64
_ClabGRETunnelStatsKeepAliveSent_Object = MibTableColumn
clabGRETunnelStatsKeepAliveSent = _ClabGRETunnelStatsKeepAliveSent_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 3, 1, 4, 1, 1),
    _ClabGRETunnelStatsKeepAliveSent_Type()
)
clabGRETunnelStatsKeepAliveSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabGRETunnelStatsKeepAliveSent.setStatus("current")
if mibBuilder.loadTexts:
    clabGRETunnelStatsKeepAliveSent.setUnits("packets")
_ClabGRETunnelStatsKeepAliveReceived_Type = Counter64
_ClabGRETunnelStatsKeepAliveReceived_Object = MibTableColumn
clabGRETunnelStatsKeepAliveReceived = _ClabGRETunnelStatsKeepAliveReceived_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 3, 1, 4, 1, 2),
    _ClabGRETunnelStatsKeepAliveReceived_Type()
)
clabGRETunnelStatsKeepAliveReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabGRETunnelStatsKeepAliveReceived.setStatus("current")
if mibBuilder.loadTexts:
    clabGRETunnelStatsKeepAliveReceived.setUnits("packets")
_ClabGRETunnelStatsBytesSent_Type = Counter64
_ClabGRETunnelStatsBytesSent_Object = MibTableColumn
clabGRETunnelStatsBytesSent = _ClabGRETunnelStatsBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 3, 1, 4, 1, 3),
    _ClabGRETunnelStatsBytesSent_Type()
)
clabGRETunnelStatsBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabGRETunnelStatsBytesSent.setStatus("current")
if mibBuilder.loadTexts:
    clabGRETunnelStatsBytesSent.setUnits("bytes")
_ClabGRETunnelStatsBytesReceived_Type = Counter64
_ClabGRETunnelStatsBytesReceived_Object = MibTableColumn
clabGRETunnelStatsBytesReceived = _ClabGRETunnelStatsBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 3, 1, 4, 1, 4),
    _ClabGRETunnelStatsBytesReceived_Type()
)
clabGRETunnelStatsBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabGRETunnelStatsBytesReceived.setStatus("current")
if mibBuilder.loadTexts:
    clabGRETunnelStatsBytesReceived.setUnits("bytes")
_ClabGRETunnelStatsPacketsSent_Type = Counter64
_ClabGRETunnelStatsPacketsSent_Object = MibTableColumn
clabGRETunnelStatsPacketsSent = _ClabGRETunnelStatsPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 3, 1, 4, 1, 5),
    _ClabGRETunnelStatsPacketsSent_Type()
)
clabGRETunnelStatsPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabGRETunnelStatsPacketsSent.setStatus("current")
if mibBuilder.loadTexts:
    clabGRETunnelStatsPacketsSent.setUnits("packets")
_ClabGRETunnelStatsPacketsReceived_Type = Counter64
_ClabGRETunnelStatsPacketsReceived_Object = MibTableColumn
clabGRETunnelStatsPacketsReceived = _ClabGRETunnelStatsPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 3, 1, 4, 1, 6),
    _ClabGRETunnelStatsPacketsReceived_Type()
)
clabGRETunnelStatsPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabGRETunnelStatsPacketsReceived.setStatus("current")
if mibBuilder.loadTexts:
    clabGRETunnelStatsPacketsReceived.setUnits("packets")
_ClabGRETunnelStatsErrorsSent_Type = Counter64
_ClabGRETunnelStatsErrorsSent_Object = MibTableColumn
clabGRETunnelStatsErrorsSent = _ClabGRETunnelStatsErrorsSent_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 3, 1, 4, 1, 7),
    _ClabGRETunnelStatsErrorsSent_Type()
)
clabGRETunnelStatsErrorsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabGRETunnelStatsErrorsSent.setStatus("current")
if mibBuilder.loadTexts:
    clabGRETunnelStatsErrorsSent.setUnits("packets")
_ClabGRETunnelStatsErrorsReceived_Type = Counter64
_ClabGRETunnelStatsErrorsReceived_Object = MibTableColumn
clabGRETunnelStatsErrorsReceived = _ClabGRETunnelStatsErrorsReceived_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 3, 1, 4, 1, 8),
    _ClabGRETunnelStatsErrorsReceived_Type()
)
clabGRETunnelStatsErrorsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabGRETunnelStatsErrorsReceived.setStatus("current")
if mibBuilder.loadTexts:
    clabGRETunnelStatsErrorsReceived.setUnits("packets")
_ClabGRETunnelInterfaceTable_Object = MibTable
clabGRETunnelInterfaceTable = _ClabGRETunnelInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 3, 1, 5)
)
if mibBuilder.loadTexts:
    clabGRETunnelInterfaceTable.setStatus("current")
_ClabGRETunnelInterfaceEntry_Object = MibTableRow
clabGRETunnelInterfaceEntry = _ClabGRETunnelInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 3, 1, 5, 1)
)
clabGRETunnelInterfaceEntry.setIndexNames(
    (0, "CLAB-GRE-MIB", "clabGRETunnelIndex"),
    (0, "CLAB-GRE-MIB", "clabGRETunnelInterfaceIndex"),
)
if mibBuilder.loadTexts:
    clabGRETunnelInterfaceEntry.setStatus("current")


class _ClabGRETunnelInterfaceIndex_Type(Unsigned32):
    """Custom type clabGRETunnelInterfaceIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_ClabGRETunnelInterfaceIndex_Type.__name__ = "Unsigned32"
_ClabGRETunnelInterfaceIndex_Object = MibTableColumn
clabGRETunnelInterfaceIndex = _ClabGRETunnelInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 3, 1, 5, 1, 1),
    _ClabGRETunnelInterfaceIndex_Type()
)
clabGRETunnelInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clabGRETunnelInterfaceIndex.setStatus("current")
_ClabGRETunnelInterfaceRowStatus_Type = RowStatus
_ClabGRETunnelInterfaceRowStatus_Object = MibTableColumn
clabGRETunnelInterfaceRowStatus = _ClabGRETunnelInterfaceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 3, 1, 5, 1, 2),
    _ClabGRETunnelInterfaceRowStatus_Type()
)
clabGRETunnelInterfaceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabGRETunnelInterfaceRowStatus.setStatus("current")
_ClabGRETunnelInterfaceEnable_Type = TruthValue
_ClabGRETunnelInterfaceEnable_Object = MibTableColumn
clabGRETunnelInterfaceEnable = _ClabGRETunnelInterfaceEnable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 3, 1, 5, 1, 3),
    _ClabGRETunnelInterfaceEnable_Type()
)
clabGRETunnelInterfaceEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabGRETunnelInterfaceEnable.setStatus("current")


class _ClabGRETunnelInterfaceStatus_Type(Integer32):
    """Custom type clabGRETunnelInterfaceStatus based on Integer32"""
    defaultValue = 1

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
        *(("down", 1),
          ("up", 2),
          ("unknown", 3),
          ("dormant", 4),
          ("notPresent", 5),
          ("lowerLayerDown", 6),
          ("error", 7))
    )


_ClabGRETunnelInterfaceStatus_Type.__name__ = "Integer32"
_ClabGRETunnelInterfaceStatus_Object = MibTableColumn
clabGRETunnelInterfaceStatus = _ClabGRETunnelInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 3, 1, 5, 1, 4),
    _ClabGRETunnelInterfaceStatus_Type()
)
clabGRETunnelInterfaceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabGRETunnelInterfaceStatus.setStatus("current")
_ClabGRETunnelInterfaceAlias_Type = SnmpAdminString
_ClabGRETunnelInterfaceAlias_Object = MibTableColumn
clabGRETunnelInterfaceAlias = _ClabGRETunnelInterfaceAlias_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 3, 1, 5, 1, 5),
    _ClabGRETunnelInterfaceAlias_Type()
)
clabGRETunnelInterfaceAlias.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabGRETunnelInterfaceAlias.setStatus("current")
_ClabGRETunnelInterfaceName_Type = SnmpAdminString
_ClabGRETunnelInterfaceName_Object = MibTableColumn
clabGRETunnelInterfaceName = _ClabGRETunnelInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 3, 1, 5, 1, 6),
    _ClabGRETunnelInterfaceName_Type()
)
clabGRETunnelInterfaceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabGRETunnelInterfaceName.setStatus("current")
_ClabGRETunnelInterfaceLastChange_Type = Unsigned32
_ClabGRETunnelInterfaceLastChange_Object = MibTableColumn
clabGRETunnelInterfaceLastChange = _ClabGRETunnelInterfaceLastChange_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 3, 1, 5, 1, 7),
    _ClabGRETunnelInterfaceLastChange_Type()
)
clabGRETunnelInterfaceLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabGRETunnelInterfaceLastChange.setStatus("current")
if mibBuilder.loadTexts:
    clabGRETunnelInterfaceLastChange.setUnits("seconds")
_ClabGRETunnelInterfaceLowerLayers_Type = SnmpAdminString
_ClabGRETunnelInterfaceLowerLayers_Object = MibTableColumn
clabGRETunnelInterfaceLowerLayers = _ClabGRETunnelInterfaceLowerLayers_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 3, 1, 5, 1, 8),
    _ClabGRETunnelInterfaceLowerLayers_Type()
)
clabGRETunnelInterfaceLowerLayers.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabGRETunnelInterfaceLowerLayers.setStatus("current")
_ClabGRETunnelInterfaceProtocolIdOverride_Type = Unsigned32
_ClabGRETunnelInterfaceProtocolIdOverride_Object = MibTableColumn
clabGRETunnelInterfaceProtocolIdOverride = _ClabGRETunnelInterfaceProtocolIdOverride_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 3, 1, 5, 1, 9),
    _ClabGRETunnelInterfaceProtocolIdOverride_Type()
)
clabGRETunnelInterfaceProtocolIdOverride.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabGRETunnelInterfaceProtocolIdOverride.setStatus("current")


class _ClabGRETunnelInterfaceUseChecksum_Type(TruthValue):
    """Custom type clabGRETunnelInterfaceUseChecksum based on TruthValue"""
    defaultValue = 2


_ClabGRETunnelInterfaceUseChecksum_Type.__name__ = "TruthValue"
_ClabGRETunnelInterfaceUseChecksum_Object = MibTableColumn
clabGRETunnelInterfaceUseChecksum = _ClabGRETunnelInterfaceUseChecksum_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 3, 1, 5, 1, 10),
    _ClabGRETunnelInterfaceUseChecksum_Type()
)
clabGRETunnelInterfaceUseChecksum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabGRETunnelInterfaceUseChecksum.setStatus("current")


class _ClabGRETunnelInterfaceKeyIdentifierGenerationPolicy_Type(Integer32):
    """Custom type clabGRETunnelInterfaceKeyIdentifierGenerationPolicy based on Integer32"""
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
          ("provisioned", 2),
          ("generated", 3))
    )


_ClabGRETunnelInterfaceKeyIdentifierGenerationPolicy_Type.__name__ = "Integer32"
_ClabGRETunnelInterfaceKeyIdentifierGenerationPolicy_Object = MibTableColumn
clabGRETunnelInterfaceKeyIdentifierGenerationPolicy = _ClabGRETunnelInterfaceKeyIdentifierGenerationPolicy_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 3, 1, 5, 1, 11),
    _ClabGRETunnelInterfaceKeyIdentifierGenerationPolicy_Type()
)
clabGRETunnelInterfaceKeyIdentifierGenerationPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabGRETunnelInterfaceKeyIdentifierGenerationPolicy.setStatus("current")
_ClabGRETunnelInterfaceKeyIdentifier_Type = Unsigned32
_ClabGRETunnelInterfaceKeyIdentifier_Object = MibTableColumn
clabGRETunnelInterfaceKeyIdentifier = _ClabGRETunnelInterfaceKeyIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 3, 1, 5, 1, 12),
    _ClabGRETunnelInterfaceKeyIdentifier_Type()
)
clabGRETunnelInterfaceKeyIdentifier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabGRETunnelInterfaceKeyIdentifier.setStatus("current")


class _ClabGRETunnelInterfaceUseSequenceNumber_Type(TruthValue):
    """Custom type clabGRETunnelInterfaceUseSequenceNumber based on TruthValue"""
    defaultValue = 2


_ClabGRETunnelInterfaceUseSequenceNumber_Type.__name__ = "TruthValue"
_ClabGRETunnelInterfaceUseSequenceNumber_Object = MibTableColumn
clabGRETunnelInterfaceUseSequenceNumber = _ClabGRETunnelInterfaceUseSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 3, 1, 5, 1, 13),
    _ClabGRETunnelInterfaceUseSequenceNumber_Type()
)
clabGRETunnelInterfaceUseSequenceNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabGRETunnelInterfaceUseSequenceNumber.setStatus("current")
_ClabGRETunnelInterfaceStatsTable_Object = MibTable
clabGRETunnelInterfaceStatsTable = _ClabGRETunnelInterfaceStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 3, 1, 6)
)
if mibBuilder.loadTexts:
    clabGRETunnelInterfaceStatsTable.setStatus("current")
_ClabGRETunnelInterfaceStatsEntry_Object = MibTableRow
clabGRETunnelInterfaceStatsEntry = _ClabGRETunnelInterfaceStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 3, 1, 6, 1)
)
if mibBuilder.loadTexts:
    clabGRETunnelInterfaceStatsEntry.setStatus("current")
_ClabGRETunnelInterfaceStatsBytesSent_Type = Counter64
_ClabGRETunnelInterfaceStatsBytesSent_Object = MibTableColumn
clabGRETunnelInterfaceStatsBytesSent = _ClabGRETunnelInterfaceStatsBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 3, 1, 6, 1, 1),
    _ClabGRETunnelInterfaceStatsBytesSent_Type()
)
clabGRETunnelInterfaceStatsBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabGRETunnelInterfaceStatsBytesSent.setStatus("current")
if mibBuilder.loadTexts:
    clabGRETunnelInterfaceStatsBytesSent.setUnits("bytes")
_ClabGRETunnelInterfaceStatsBytesReceived_Type = Counter64
_ClabGRETunnelInterfaceStatsBytesReceived_Object = MibTableColumn
clabGRETunnelInterfaceStatsBytesReceived = _ClabGRETunnelInterfaceStatsBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 3, 1, 6, 1, 2),
    _ClabGRETunnelInterfaceStatsBytesReceived_Type()
)
clabGRETunnelInterfaceStatsBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabGRETunnelInterfaceStatsBytesReceived.setStatus("current")
if mibBuilder.loadTexts:
    clabGRETunnelInterfaceStatsBytesReceived.setUnits("bytes")
_ClabGRETunnelInterfaceStatsPacketsSent_Type = Counter64
_ClabGRETunnelInterfaceStatsPacketsSent_Object = MibTableColumn
clabGRETunnelInterfaceStatsPacketsSent = _ClabGRETunnelInterfaceStatsPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 3, 1, 6, 1, 3),
    _ClabGRETunnelInterfaceStatsPacketsSent_Type()
)
clabGRETunnelInterfaceStatsPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabGRETunnelInterfaceStatsPacketsSent.setStatus("current")
if mibBuilder.loadTexts:
    clabGRETunnelInterfaceStatsPacketsSent.setUnits("packets")
_ClabGRETunnelInterfaceStatsPacketsReceived_Type = Counter64
_ClabGRETunnelInterfaceStatsPacketsReceived_Object = MibTableColumn
clabGRETunnelInterfaceStatsPacketsReceived = _ClabGRETunnelInterfaceStatsPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 3, 1, 6, 1, 4),
    _ClabGRETunnelInterfaceStatsPacketsReceived_Type()
)
clabGRETunnelInterfaceStatsPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabGRETunnelInterfaceStatsPacketsReceived.setStatus("current")
if mibBuilder.loadTexts:
    clabGRETunnelInterfaceStatsPacketsReceived.setUnits("packets")
_ClabGRETunnelInterfaceStatsErrorsSent_Type = Counter64
_ClabGRETunnelInterfaceStatsErrorsSent_Object = MibTableColumn
clabGRETunnelInterfaceStatsErrorsSent = _ClabGRETunnelInterfaceStatsErrorsSent_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 3, 1, 6, 1, 5),
    _ClabGRETunnelInterfaceStatsErrorsSent_Type()
)
clabGRETunnelInterfaceStatsErrorsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabGRETunnelInterfaceStatsErrorsSent.setStatus("current")
if mibBuilder.loadTexts:
    clabGRETunnelInterfaceStatsErrorsSent.setUnits("packets")
_ClabGRETunnelInterfaceStatsErrorsReceived_Type = Counter64
_ClabGRETunnelInterfaceStatsErrorsReceived_Object = MibTableColumn
clabGRETunnelInterfaceStatsErrorsReceived = _ClabGRETunnelInterfaceStatsErrorsReceived_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 3, 1, 6, 1, 6),
    _ClabGRETunnelInterfaceStatsErrorsReceived_Type()
)
clabGRETunnelInterfaceStatsErrorsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabGRETunnelInterfaceStatsErrorsReceived.setStatus("current")
if mibBuilder.loadTexts:
    clabGRETunnelInterfaceStatsErrorsReceived.setUnits("packets")
_ClabGRETunnelInterfaceStatsDiscardChecksumReceived_Type = Counter64
_ClabGRETunnelInterfaceStatsDiscardChecksumReceived_Object = MibTableColumn
clabGRETunnelInterfaceStatsDiscardChecksumReceived = _ClabGRETunnelInterfaceStatsDiscardChecksumReceived_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 3, 1, 6, 1, 7),
    _ClabGRETunnelInterfaceStatsDiscardChecksumReceived_Type()
)
clabGRETunnelInterfaceStatsDiscardChecksumReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabGRETunnelInterfaceStatsDiscardChecksumReceived.setStatus("current")
if mibBuilder.loadTexts:
    clabGRETunnelInterfaceStatsDiscardChecksumReceived.setUnits("packets")
_ClabGRETunnelInterfaceStatsDiscardSequenceNumberReceived_Type = Counter64
_ClabGRETunnelInterfaceStatsDiscardSequenceNumberReceived_Object = MibTableColumn
clabGRETunnelInterfaceStatsDiscardSequenceNumberReceived = _ClabGRETunnelInterfaceStatsDiscardSequenceNumberReceived_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 3, 1, 6, 1, 8),
    _ClabGRETunnelInterfaceStatsDiscardSequenceNumberReceived_Type()
)
clabGRETunnelInterfaceStatsDiscardSequenceNumberReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabGRETunnelInterfaceStatsDiscardSequenceNumberReceived.setStatus("current")
if mibBuilder.loadTexts:
    clabGRETunnelInterfaceStatsDiscardSequenceNumberReceived.setUnits("packets")
_ClabGREFilterTable_Object = MibTable
clabGREFilterTable = _ClabGREFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 3, 1, 7)
)
if mibBuilder.loadTexts:
    clabGREFilterTable.setStatus("current")
_ClabGREFilterEntry_Object = MibTableRow
clabGREFilterEntry = _ClabGREFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 3, 1, 7, 1)
)
clabGREFilterEntry.setIndexNames(
    (0, "CLAB-GRE-MIB", "clabGREFilterIndex"),
)
if mibBuilder.loadTexts:
    clabGREFilterEntry.setStatus("current")


class _ClabGREFilterIndex_Type(Unsigned32):
    """Custom type clabGREFilterIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_ClabGREFilterIndex_Type.__name__ = "Unsigned32"
_ClabGREFilterIndex_Object = MibTableColumn
clabGREFilterIndex = _ClabGREFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 3, 1, 7, 1, 1),
    _ClabGREFilterIndex_Type()
)
clabGREFilterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clabGREFilterIndex.setStatus("current")
_ClabGREFilterRowStatus_Type = RowStatus
_ClabGREFilterRowStatus_Object = MibTableColumn
clabGREFilterRowStatus = _ClabGREFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 3, 1, 7, 1, 2),
    _ClabGREFilterRowStatus_Type()
)
clabGREFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabGREFilterRowStatus.setStatus("current")


class _ClabGREFilterEnable_Type(TruthValue):
    """Custom type clabGREFilterEnable based on TruthValue"""
    defaultValue = 2


_ClabGREFilterEnable_Type.__name__ = "TruthValue"
_ClabGREFilterEnable_Object = MibTableColumn
clabGREFilterEnable = _ClabGREFilterEnable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 3, 1, 7, 1, 3),
    _ClabGREFilterEnable_Type()
)
clabGREFilterEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabGREFilterEnable.setStatus("current")


class _ClabGREFilterStatus_Type(Integer32):
    """Custom type clabGREFilterStatus based on Integer32"""
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


_ClabGREFilterStatus_Type.__name__ = "Integer32"
_ClabGREFilterStatus_Object = MibTableColumn
clabGREFilterStatus = _ClabGREFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 3, 1, 7, 1, 4),
    _ClabGREFilterStatus_Type()
)
clabGREFilterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabGREFilterStatus.setStatus("current")


class _ClabGREFilterOrder_Type(Unsigned32):
    """Custom type clabGREFilterOrder based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_ClabGREFilterOrder_Type.__name__ = "Unsigned32"
_ClabGREFilterOrder_Object = MibTableColumn
clabGREFilterOrder = _ClabGREFilterOrder_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 3, 1, 7, 1, 5),
    _ClabGREFilterOrder_Type()
)
clabGREFilterOrder.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabGREFilterOrder.setStatus("current")
_ClabGREFilterAlias_Type = SnmpAdminString
_ClabGREFilterAlias_Object = MibTableColumn
clabGREFilterAlias = _ClabGREFilterAlias_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 3, 1, 7, 1, 6),
    _ClabGREFilterAlias_Type()
)
clabGREFilterAlias.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabGREFilterAlias.setStatus("current")
_ClabGREFilterInterface_Type = SnmpAdminString
_ClabGREFilterInterface_Object = MibTableColumn
clabGREFilterInterface = _ClabGREFilterInterface_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 3, 1, 7, 1, 7),
    _ClabGREFilterInterface_Type()
)
clabGREFilterInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabGREFilterInterface.setStatus("current")
_ClabGREFilterAllInterfaces_Type = TruthValue
_ClabGREFilterAllInterfaces_Object = MibTableColumn
clabGREFilterAllInterfaces = _ClabGREFilterAllInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 3, 1, 7, 1, 8),
    _ClabGREFilterAllInterfaces_Type()
)
clabGREFilterAllInterfaces.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabGREFilterAllInterfaces.setStatus("current")


class _ClabGREFilterVlanIdCheck_Type(Integer32):
    """Custom type clabGREFilterVlanIdCheck based on Integer32"""
    defaultValue = -1


_ClabGREFilterVlanIdCheck_Type.__name__ = "Integer32"
_ClabGREFilterVlanIdCheck_Object = MibTableColumn
clabGREFilterVlanIdCheck = _ClabGREFilterVlanIdCheck_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 3, 1, 7, 1, 9),
    _ClabGREFilterVlanIdCheck_Type()
)
clabGREFilterVlanIdCheck.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabGREFilterVlanIdCheck.setStatus("current")


class _ClabGREFilterVlanIdExclude_Type(TruthValue):
    """Custom type clabGREFilterVlanIdExclude based on TruthValue"""
    defaultValue = 2


_ClabGREFilterVlanIdExclude_Type.__name__ = "TruthValue"
_ClabGREFilterVlanIdExclude_Object = MibTableColumn
clabGREFilterVlanIdExclude = _ClabGREFilterVlanIdExclude_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 3, 1, 7, 1, 10),
    _ClabGREFilterVlanIdExclude_Type()
)
clabGREFilterVlanIdExclude.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabGREFilterVlanIdExclude.setStatus("current")


class _ClabGREFilterDscpMarkPolicy_Type(Integer32):
    """Custom type clabGREFilterDscpMarkPolicy based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 63),
    )


_ClabGREFilterDscpMarkPolicy_Type.__name__ = "Integer32"
_ClabGREFilterDscpMarkPolicy_Object = MibTableColumn
clabGREFilterDscpMarkPolicy = _ClabGREFilterDscpMarkPolicy_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 3, 1, 7, 1, 11),
    _ClabGREFilterDscpMarkPolicy_Type()
)
clabGREFilterDscpMarkPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabGREFilterDscpMarkPolicy.setStatus("current")


class _ClabGREFilterVlanTag_Type(Unsigned32):
    """Custom type clabGREFilterVlanTag based on Unsigned32"""
    defaultValue = 0


_ClabGREFilterVlanTag_Type.__name__ = "Unsigned32"
_ClabGREFilterVlanTag_Object = MibTableColumn
clabGREFilterVlanTag = _ClabGREFilterVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 3, 1, 7, 1, 12),
    _ClabGREFilterVlanTag_Type()
)
clabGREFilterVlanTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabGREFilterVlanTag.setStatus("current")
_ClabGREMibConformance_ObjectIdentity = ObjectIdentity
clabGREMibConformance = _ClabGREMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 4, 3, 2)
)
_ClabGREMibCompliances_ObjectIdentity = ObjectIdentity
clabGREMibCompliances = _ClabGREMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 4, 3, 2, 1)
)
_ClabGREMibGroups_ObjectIdentity = ObjectIdentity
clabGREMibGroups = _ClabGREMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 4, 3, 2, 2)
)
clabGRETunnelEntry.registerAugmentions(
    ("CLAB-GRE-MIB",
     "clabGRETunnelStatsEntry")
)
clabGRETunnelStatsEntry.setIndexNames(*clabGRETunnelEntry.getIndexNames())
clabGRETunnelInterfaceEntry.registerAugmentions(
    ("CLAB-GRE-MIB",
     "clabGRETunnelInterfaceStatsEntry")
)
clabGRETunnelInterfaceStatsEntry.setIndexNames(*clabGRETunnelInterfaceEntry.getIndexNames())

# Managed Objects groups

clabGREGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 4, 3, 2, 2, 1)
)
clabGREGroup.setObjects(
      *(("CLAB-GRE-MIB", "clabGRETunnelNumberOfEntries"),
        ("CLAB-GRE-MIB", "clabGREFilterNumberOfEntries"),
        ("CLAB-GRE-MIB", "clabGRETunnelRowStatus"),
        ("CLAB-GRE-MIB", "clabGRETunnelEnable"),
        ("CLAB-GRE-MIB", "clabGRETunnelStatus"),
        ("CLAB-GRE-MIB", "clabGRETunnelAlias"),
        ("CLAB-GRE-MIB", "clabGRETunnelRemoteEndpoints"),
        ("CLAB-GRE-MIB", "clabGRETunnelKeepAlivePolicy"),
        ("CLAB-GRE-MIB", "clabGRETunnelKeepAliveTimeout"),
        ("CLAB-GRE-MIB", "clabGRETunnelKeepAliveThreshold"),
        ("CLAB-GRE-MIB", "clabGRETunnelKeepAliveCount"),
        ("CLAB-GRE-MIB", "clabGRETunnelKeepAliveInterval"),
        ("CLAB-GRE-MIB", "clabGRETunnelKeepAliveFailureInterval"),
        ("CLAB-GRE-MIB", "clabGRETunnelKeepAliveRecoverInterval"),
        ("CLAB-GRE-MIB", "clabGRETunnelDeliveryHeaderProtocol"),
        ("CLAB-GRE-MIB", "clabGRETunnelDefaultDscpMark"),
        ("CLAB-GRE-MIB", "clabGRETunnelConnectedRemoteEndpoint"),
        ("CLAB-GRE-MIB", "clabGRETunnelInterfaceNumberOfEntries"),
        ("CLAB-GRE-MIB", "clabGRETunnelTcpMssClamping"),
        ("CLAB-GRE-MIB", "clabGRETunnelConcentratorServiceName"),
        ("CLAB-GRE-MIB", "clabGRETunnnelRemoteEndpointConnectivityState"),
        ("CLAB-GRE-MIB", "clabGRETunnelStatsKeepAliveSent"),
        ("CLAB-GRE-MIB", "clabGRETunnelStatsKeepAliveReceived"),
        ("CLAB-GRE-MIB", "clabGRETunnelStatsBytesSent"),
        ("CLAB-GRE-MIB", "clabGRETunnelStatsBytesReceived"),
        ("CLAB-GRE-MIB", "clabGRETunnelStatsPacketsSent"),
        ("CLAB-GRE-MIB", "clabGRETunnelStatsPacketsReceived"),
        ("CLAB-GRE-MIB", "clabGRETunnelStatsErrorsSent"),
        ("CLAB-GRE-MIB", "clabGRETunnelStatsErrorsReceived"),
        ("CLAB-GRE-MIB", "clabGRETunnelInterfaceRowStatus"),
        ("CLAB-GRE-MIB", "clabGRETunnelInterfaceStatus"),
        ("CLAB-GRE-MIB", "clabGRETunnelInterfaceAlias"),
        ("CLAB-GRE-MIB", "clabGRETunnelInterfaceName"),
        ("CLAB-GRE-MIB", "clabGRETunnelInterfaceLastChange"),
        ("CLAB-GRE-MIB", "clabGRETunnelInterfaceLowerLayers"),
        ("CLAB-GRE-MIB", "clabGRETunnelInterfaceEnable"),
        ("CLAB-GRE-MIB", "clabGRETunnelInterfaceProtocolIdOverride"),
        ("CLAB-GRE-MIB", "clabGRETunnelInterfaceUseChecksum"),
        ("CLAB-GRE-MIB", "clabGRETunnelInterfaceKeyIdentifierGenerationPolicy"),
        ("CLAB-GRE-MIB", "clabGRETunnelInterfaceKeyIdentifier"),
        ("CLAB-GRE-MIB", "clabGRETunnelInterfaceUseSequenceNumber"),
        ("CLAB-GRE-MIB", "clabGRETunnelInterfaceStatsBytesSent"),
        ("CLAB-GRE-MIB", "clabGRETunnelInterfaceStatsBytesReceived"),
        ("CLAB-GRE-MIB", "clabGRETunnelInterfaceStatsPacketsSent"),
        ("CLAB-GRE-MIB", "clabGRETunnelInterfaceStatsPacketsReceived"),
        ("CLAB-GRE-MIB", "clabGRETunnelInterfaceStatsErrorsSent"),
        ("CLAB-GRE-MIB", "clabGRETunnelInterfaceStatsErrorsReceived"),
        ("CLAB-GRE-MIB", "clabGRETunnelInterfaceStatsDiscardChecksumReceived"),
        ("CLAB-GRE-MIB", "clabGRETunnelInterfaceStatsDiscardSequenceNumberReceived"),
        ("CLAB-GRE-MIB", "clabGREFilterRowStatus"),
        ("CLAB-GRE-MIB", "clabGREFilterEnable"),
        ("CLAB-GRE-MIB", "clabGREFilterStatus"),
        ("CLAB-GRE-MIB", "clabGREFilterOrder"),
        ("CLAB-GRE-MIB", "clabGREFilterAlias"),
        ("CLAB-GRE-MIB", "clabGREFilterInterface"),
        ("CLAB-GRE-MIB", "clabGREFilterAllInterfaces"),
        ("CLAB-GRE-MIB", "clabGREFilterVlanIdCheck"),
        ("CLAB-GRE-MIB", "clabGREFilterVlanIdExclude"),
        ("CLAB-GRE-MIB", "clabGREFilterVlanTag"),
        ("CLAB-GRE-MIB", "clabGREFilterDscpMarkPolicy"))
)
if mibBuilder.loadTexts:
    clabGREGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

clabGRECompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4491, 4, 3, 2, 1, 1)
)
clabGRECompliance.setObjects(
    ("CLAB-GRE-MIB", "clabGREGroup")
)
if mibBuilder.loadTexts:
    clabGRECompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CLAB-GRE-MIB",
    **{"clabGREMib": clabGREMib,
       "clabGREObjects": clabGREObjects,
       "clabGRETunnelNumberOfEntries": clabGRETunnelNumberOfEntries,
       "clabGREFilterNumberOfEntries": clabGREFilterNumberOfEntries,
       "clabGRETunnelTable": clabGRETunnelTable,
       "clabGRETunnelEntry": clabGRETunnelEntry,
       "clabGRETunnelIndex": clabGRETunnelIndex,
       "clabGRETunnelRowStatus": clabGRETunnelRowStatus,
       "clabGRETunnelEnable": clabGRETunnelEnable,
       "clabGRETunnelStatus": clabGRETunnelStatus,
       "clabGRETunnelAlias": clabGRETunnelAlias,
       "clabGRETunnelRemoteEndpoints": clabGRETunnelRemoteEndpoints,
       "clabGRETunnelKeepAlivePolicy": clabGRETunnelKeepAlivePolicy,
       "clabGRETunnelKeepAliveTimeout": clabGRETunnelKeepAliveTimeout,
       "clabGRETunnelKeepAliveThreshold": clabGRETunnelKeepAliveThreshold,
       "clabGRETunnelKeepAliveCount": clabGRETunnelKeepAliveCount,
       "clabGRETunnelKeepAliveInterval": clabGRETunnelKeepAliveInterval,
       "clabGRETunnelKeepAliveFailureInterval": clabGRETunnelKeepAliveFailureInterval,
       "clabGRETunnelKeepAliveRecoverInterval": clabGRETunnelKeepAliveRecoverInterval,
       "clabGRETunnelDeliveryHeaderProtocol": clabGRETunnelDeliveryHeaderProtocol,
       "clabGRETunnelDefaultDscpMark": clabGRETunnelDefaultDscpMark,
       "clabGRETunnelConnectedRemoteEndpoint": clabGRETunnelConnectedRemoteEndpoint,
       "clabGRETunnelInterfaceNumberOfEntries": clabGRETunnelInterfaceNumberOfEntries,
       "clabGRETunnelTcpMssClamping": clabGRETunnelTcpMssClamping,
       "clabGRETunnelConcentratorServiceName": clabGRETunnelConcentratorServiceName,
       "clabGRETunnnelRemoteEndpointConnectivityState": clabGRETunnnelRemoteEndpointConnectivityState,
       "clabGRETunnelStatsTable": clabGRETunnelStatsTable,
       "clabGRETunnelStatsEntry": clabGRETunnelStatsEntry,
       "clabGRETunnelStatsKeepAliveSent": clabGRETunnelStatsKeepAliveSent,
       "clabGRETunnelStatsKeepAliveReceived": clabGRETunnelStatsKeepAliveReceived,
       "clabGRETunnelStatsBytesSent": clabGRETunnelStatsBytesSent,
       "clabGRETunnelStatsBytesReceived": clabGRETunnelStatsBytesReceived,
       "clabGRETunnelStatsPacketsSent": clabGRETunnelStatsPacketsSent,
       "clabGRETunnelStatsPacketsReceived": clabGRETunnelStatsPacketsReceived,
       "clabGRETunnelStatsErrorsSent": clabGRETunnelStatsErrorsSent,
       "clabGRETunnelStatsErrorsReceived": clabGRETunnelStatsErrorsReceived,
       "clabGRETunnelInterfaceTable": clabGRETunnelInterfaceTable,
       "clabGRETunnelInterfaceEntry": clabGRETunnelInterfaceEntry,
       "clabGRETunnelInterfaceIndex": clabGRETunnelInterfaceIndex,
       "clabGRETunnelInterfaceRowStatus": clabGRETunnelInterfaceRowStatus,
       "clabGRETunnelInterfaceEnable": clabGRETunnelInterfaceEnable,
       "clabGRETunnelInterfaceStatus": clabGRETunnelInterfaceStatus,
       "clabGRETunnelInterfaceAlias": clabGRETunnelInterfaceAlias,
       "clabGRETunnelInterfaceName": clabGRETunnelInterfaceName,
       "clabGRETunnelInterfaceLastChange": clabGRETunnelInterfaceLastChange,
       "clabGRETunnelInterfaceLowerLayers": clabGRETunnelInterfaceLowerLayers,
       "clabGRETunnelInterfaceProtocolIdOverride": clabGRETunnelInterfaceProtocolIdOverride,
       "clabGRETunnelInterfaceUseChecksum": clabGRETunnelInterfaceUseChecksum,
       "clabGRETunnelInterfaceKeyIdentifierGenerationPolicy": clabGRETunnelInterfaceKeyIdentifierGenerationPolicy,
       "clabGRETunnelInterfaceKeyIdentifier": clabGRETunnelInterfaceKeyIdentifier,
       "clabGRETunnelInterfaceUseSequenceNumber": clabGRETunnelInterfaceUseSequenceNumber,
       "clabGRETunnelInterfaceStatsTable": clabGRETunnelInterfaceStatsTable,
       "clabGRETunnelInterfaceStatsEntry": clabGRETunnelInterfaceStatsEntry,
       "clabGRETunnelInterfaceStatsBytesSent": clabGRETunnelInterfaceStatsBytesSent,
       "clabGRETunnelInterfaceStatsBytesReceived": clabGRETunnelInterfaceStatsBytesReceived,
       "clabGRETunnelInterfaceStatsPacketsSent": clabGRETunnelInterfaceStatsPacketsSent,
       "clabGRETunnelInterfaceStatsPacketsReceived": clabGRETunnelInterfaceStatsPacketsReceived,
       "clabGRETunnelInterfaceStatsErrorsSent": clabGRETunnelInterfaceStatsErrorsSent,
       "clabGRETunnelInterfaceStatsErrorsReceived": clabGRETunnelInterfaceStatsErrorsReceived,
       "clabGRETunnelInterfaceStatsDiscardChecksumReceived": clabGRETunnelInterfaceStatsDiscardChecksumReceived,
       "clabGRETunnelInterfaceStatsDiscardSequenceNumberReceived": clabGRETunnelInterfaceStatsDiscardSequenceNumberReceived,
       "clabGREFilterTable": clabGREFilterTable,
       "clabGREFilterEntry": clabGREFilterEntry,
       "clabGREFilterIndex": clabGREFilterIndex,
       "clabGREFilterRowStatus": clabGREFilterRowStatus,
       "clabGREFilterEnable": clabGREFilterEnable,
       "clabGREFilterStatus": clabGREFilterStatus,
       "clabGREFilterOrder": clabGREFilterOrder,
       "clabGREFilterAlias": clabGREFilterAlias,
       "clabGREFilterInterface": clabGREFilterInterface,
       "clabGREFilterAllInterfaces": clabGREFilterAllInterfaces,
       "clabGREFilterVlanIdCheck": clabGREFilterVlanIdCheck,
       "clabGREFilterVlanIdExclude": clabGREFilterVlanIdExclude,
       "clabGREFilterDscpMarkPolicy": clabGREFilterDscpMarkPolicy,
       "clabGREFilterVlanTag": clabGREFilterVlanTag,
       "clabGREMibConformance": clabGREMibConformance,
       "clabGREMibCompliances": clabGREMibCompliances,
       "clabGRECompliance": clabGRECompliance,
       "clabGREMibGroups": clabGREMibGroups,
       "clabGREGroup": clabGREGroup}
)
