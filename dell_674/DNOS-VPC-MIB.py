# SNMP MIB module (DNOS-VPC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/dell_674/DNOS-VPC-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 09:25:39 2025
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

(AgentPortMask,
 dnOS) = mibBuilder.importSymbols(
    "DELL-REF-MIB",
    "AgentPortMask",
    "dnOS")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

fastPathVpc = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 200)
)
if mibBuilder.loadTexts:
    fastPathVpc.setRevisions(
        ("2014-01-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AgentVpcConfigGroup_ObjectIdentity = ObjectIdentity
agentVpcConfigGroup = _AgentVpcConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 200, 1)
)


class _AgentVpcMode_Type(Integer32):
    """Custom type agentVpcMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AgentVpcMode_Type.__name__ = "Integer32"
_AgentVpcMode_Object = MibScalar
agentVpcMode = _AgentVpcMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 200, 1, 1),
    _AgentVpcMode_Type()
)
agentVpcMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentVpcMode.setStatus("current")


class _AgentKeepalivePriority_Type(Unsigned32):
    """Custom type agentKeepalivePriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AgentKeepalivePriority_Type.__name__ = "Unsigned32"
_AgentKeepalivePriority_Object = MibScalar
agentKeepalivePriority = _AgentKeepalivePriority_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 200, 1, 2),
    _AgentKeepalivePriority_Type()
)
agentKeepalivePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentKeepalivePriority.setStatus("obsolete")


class _AgentKeepaliveTimeout_Type(Unsigned32):
    """Custom type agentKeepaliveTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 15),
    )


_AgentKeepaliveTimeout_Type.__name__ = "Unsigned32"
_AgentKeepaliveTimeout_Object = MibScalar
agentKeepaliveTimeout = _AgentKeepaliveTimeout_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 200, 1, 3),
    _AgentKeepaliveTimeout_Type()
)
agentKeepaliveTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentKeepaliveTimeout.setStatus("obsolete")


class _AgentKeepaliveMode_Type(Integer32):
    """Custom type agentKeepaliveMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AgentKeepaliveMode_Type.__name__ = "Integer32"
_AgentKeepaliveMode_Object = MibScalar
agentKeepaliveMode = _AgentKeepaliveMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 200, 1, 4),
    _AgentKeepaliveMode_Type()
)
agentKeepaliveMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentKeepaliveMode.setStatus("obsolete")
_AgentPeerLink_Type = InterfaceIndex
_AgentPeerLink_Object = MibScalar
agentPeerLink = _AgentPeerLink_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 200, 1, 5),
    _AgentPeerLink_Type()
)
agentPeerLink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPeerLink.setStatus("current")


class _AgentPeerDetectionMode_Type(Integer32):
    """Custom type agentPeerDetectionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AgentPeerDetectionMode_Type.__name__ = "Integer32"
_AgentPeerDetectionMode_Object = MibScalar
agentPeerDetectionMode = _AgentPeerDetectionMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 200, 1, 6),
    _AgentPeerDetectionMode_Type()
)
agentPeerDetectionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPeerDetectionMode.setStatus("obsolete")
_AgentVpcConfigTable_Object = MibTable
agentVpcConfigTable = _AgentVpcConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 200, 1, 7)
)
if mibBuilder.loadTexts:
    agentVpcConfigTable.setStatus("obsolete")
_AgentVpcConfigEntry_Object = MibTableRow
agentVpcConfigEntry = _AgentVpcConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 200, 1, 7, 1)
)
agentVpcConfigEntry.setIndexNames(
    (0, "DNOS-VPC-MIB", "agentVpcConfigId"),
)
if mibBuilder.loadTexts:
    agentVpcConfigEntry.setStatus("obsolete")


class _AgentVpcConfigId_Type(Unsigned32):
    """Custom type agentVpcConfigId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_AgentVpcConfigId_Type.__name__ = "Unsigned32"
_AgentVpcConfigId_Object = MibTableColumn
agentVpcConfigId = _AgentVpcConfigId_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 200, 1, 7, 1, 1),
    _AgentVpcConfigId_Type()
)
agentVpcConfigId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentVpcConfigId.setStatus("obsolete")
_AgentVpcTrackPortMask_Type = AgentPortMask
_AgentVpcTrackPortMask_Object = MibTableColumn
agentVpcTrackPortMask = _AgentVpcTrackPortMask_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 200, 1, 7, 1, 2),
    _AgentVpcTrackPortMask_Type()
)
agentVpcTrackPortMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentVpcTrackPortMask.setStatus("obsolete")
_AgentPeerConfigTable_Object = MibTable
agentPeerConfigTable = _AgentPeerConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 200, 1, 8)
)
if mibBuilder.loadTexts:
    agentPeerConfigTable.setStatus("obsolete")
_AgentPeerConfigEntry_Object = MibTableRow
agentPeerConfigEntry = _AgentPeerConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 200, 1, 8, 1)
)
agentPeerConfigEntry.setIndexNames(
    (0, "DNOS-VPC-MIB", "agentPeerConfigRowIndex"),
)
if mibBuilder.loadTexts:
    agentPeerConfigEntry.setStatus("obsolete")


class _AgentPeerConfigRowIndex_Type(Unsigned32):
    """Custom type agentPeerConfigRowIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_AgentPeerConfigRowIndex_Type.__name__ = "Unsigned32"
_AgentPeerConfigRowIndex_Object = MibTableColumn
agentPeerConfigRowIndex = _AgentPeerConfigRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 200, 1, 8, 1, 1),
    _AgentPeerConfigRowIndex_Type()
)
agentPeerConfigRowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentPeerConfigRowIndex.setStatus("obsolete")
_AgentPeerIpAddr_Type = IpAddress
_AgentPeerIpAddr_Object = MibTableColumn
agentPeerIpAddr = _AgentPeerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 200, 1, 8, 1, 2),
    _AgentPeerIpAddr_Type()
)
agentPeerIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPeerIpAddr.setStatus("obsolete")
_AgentSourceIpAddr_Type = IpAddress
_AgentSourceIpAddr_Object = MibTableColumn
agentSourceIpAddr = _AgentSourceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 200, 1, 8, 1, 3),
    _AgentSourceIpAddr_Type()
)
agentSourceIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSourceIpAddr.setStatus("obsolete")


class _AgentDcpdpUdpPort_Type(Unsigned32):
    """Custom type agentDcpdpUdpPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AgentDcpdpUdpPort_Type.__name__ = "Unsigned32"
_AgentDcpdpUdpPort_Object = MibTableColumn
agentDcpdpUdpPort = _AgentDcpdpUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 200, 1, 8, 1, 4),
    _AgentDcpdpUdpPort_Type()
)
agentDcpdpUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDcpdpUdpPort.setStatus("obsolete")
_AgentPeerRowStatus_Type = RowStatus
_AgentPeerRowStatus_Object = MibTableColumn
agentPeerRowStatus = _AgentPeerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 200, 1, 8, 1, 5),
    _AgentPeerRowStatus_Type()
)
agentPeerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentPeerRowStatus.setStatus("obsolete")
_AgentVpcDomainConfigTable_Object = MibTable
agentVpcDomainConfigTable = _AgentVpcDomainConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 200, 1, 9)
)
if mibBuilder.loadTexts:
    agentVpcDomainConfigTable.setStatus("current")
_AgentVpcDomainConfigEntry_Object = MibTableRow
agentVpcDomainConfigEntry = _AgentVpcDomainConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 200, 1, 9, 1)
)
agentVpcDomainConfigEntry.setIndexNames(
    (0, "DNOS-VPC-MIB", "agentVpcDomainIndex"),
)
if mibBuilder.loadTexts:
    agentVpcDomainConfigEntry.setStatus("current")


class _AgentVpcDomainIndex_Type(Unsigned32):
    """Custom type agentVpcDomainIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AgentVpcDomainIndex_Type.__name__ = "Unsigned32"
_AgentVpcDomainIndex_Object = MibTableColumn
agentVpcDomainIndex = _AgentVpcDomainIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 200, 1, 9, 1, 1),
    _AgentVpcDomainIndex_Type()
)
agentVpcDomainIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentVpcDomainIndex.setStatus("current")


class _AgentVpcDomainKeepalivePriority_Type(Unsigned32):
    """Custom type agentVpcDomainKeepalivePriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AgentVpcDomainKeepalivePriority_Type.__name__ = "Unsigned32"
_AgentVpcDomainKeepalivePriority_Object = MibTableColumn
agentVpcDomainKeepalivePriority = _AgentVpcDomainKeepalivePriority_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 200, 1, 9, 1, 2),
    _AgentVpcDomainKeepalivePriority_Type()
)
agentVpcDomainKeepalivePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentVpcDomainKeepalivePriority.setStatus("current")


class _AgentVpcDomainKeepaliveTimeout_Type(Unsigned32):
    """Custom type agentVpcDomainKeepaliveTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 15),
    )


_AgentVpcDomainKeepaliveTimeout_Type.__name__ = "Unsigned32"
_AgentVpcDomainKeepaliveTimeout_Object = MibTableColumn
agentVpcDomainKeepaliveTimeout = _AgentVpcDomainKeepaliveTimeout_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 200, 1, 9, 1, 3),
    _AgentVpcDomainKeepaliveTimeout_Type()
)
agentVpcDomainKeepaliveTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentVpcDomainKeepaliveTimeout.setStatus("current")


class _AgentVpcDomainKeepaliveMode_Type(Integer32):
    """Custom type agentVpcDomainKeepaliveMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AgentVpcDomainKeepaliveMode_Type.__name__ = "Integer32"
_AgentVpcDomainKeepaliveMode_Object = MibTableColumn
agentVpcDomainKeepaliveMode = _AgentVpcDomainKeepaliveMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 200, 1, 9, 1, 4),
    _AgentVpcDomainKeepaliveMode_Type()
)
agentVpcDomainKeepaliveMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentVpcDomainKeepaliveMode.setStatus("current")


class _AgentVpcDomainPeerDetectionMode_Type(Integer32):
    """Custom type agentVpcDomainPeerDetectionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AgentVpcDomainPeerDetectionMode_Type.__name__ = "Integer32"
_AgentVpcDomainPeerDetectionMode_Object = MibTableColumn
agentVpcDomainPeerDetectionMode = _AgentVpcDomainPeerDetectionMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 200, 1, 9, 1, 5),
    _AgentVpcDomainPeerDetectionMode_Type()
)
agentVpcDomainPeerDetectionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentVpcDomainPeerDetectionMode.setStatus("current")
_AgentVpcDomainSystemMac_Type = MacAddress
_AgentVpcDomainSystemMac_Object = MibTableColumn
agentVpcDomainSystemMac = _AgentVpcDomainSystemMac_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 200, 1, 9, 1, 6),
    _AgentVpcDomainSystemMac_Type()
)
agentVpcDomainSystemMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentVpcDomainSystemMac.setStatus("current")


class _AgentVpcDomainSystemPriority_Type(Unsigned32):
    """Custom type agentVpcDomainSystemPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AgentVpcDomainSystemPriority_Type.__name__ = "Unsigned32"
_AgentVpcDomainSystemPriority_Object = MibTableColumn
agentVpcDomainSystemPriority = _AgentVpcDomainSystemPriority_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 200, 1, 9, 1, 7),
    _AgentVpcDomainSystemPriority_Type()
)
agentVpcDomainSystemPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentVpcDomainSystemPriority.setStatus("current")


class _AgentVpcDomainPeerDetectionInterval_Type(Unsigned32):
    """Custom type agentVpcDomainPeerDetectionInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 4000),
    )


_AgentVpcDomainPeerDetectionInterval_Type.__name__ = "Unsigned32"
_AgentVpcDomainPeerDetectionInterval_Object = MibTableColumn
agentVpcDomainPeerDetectionInterval = _AgentVpcDomainPeerDetectionInterval_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 200, 1, 9, 1, 8),
    _AgentVpcDomainPeerDetectionInterval_Type()
)
agentVpcDomainPeerDetectionInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentVpcDomainPeerDetectionInterval.setStatus("current")


class _AgentVpcDomainPeerDetectionTimeout_Type(Unsigned32):
    """Custom type agentVpcDomainPeerDetectionTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(700, 14000),
    )


_AgentVpcDomainPeerDetectionTimeout_Type.__name__ = "Unsigned32"
_AgentVpcDomainPeerDetectionTimeout_Object = MibTableColumn
agentVpcDomainPeerDetectionTimeout = _AgentVpcDomainPeerDetectionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 200, 1, 9, 1, 9),
    _AgentVpcDomainPeerDetectionTimeout_Type()
)
agentVpcDomainPeerDetectionTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentVpcDomainPeerDetectionTimeout.setStatus("current")
_AgentVpcDomainPeerIpAddr_Type = IpAddress
_AgentVpcDomainPeerIpAddr_Object = MibTableColumn
agentVpcDomainPeerIpAddr = _AgentVpcDomainPeerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 200, 1, 9, 1, 10),
    _AgentVpcDomainPeerIpAddr_Type()
)
agentVpcDomainPeerIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentVpcDomainPeerIpAddr.setStatus("current")
_AgentVpcDomainSourceIpAddr_Type = IpAddress
_AgentVpcDomainSourceIpAddr_Object = MibTableColumn
agentVpcDomainSourceIpAddr = _AgentVpcDomainSourceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 200, 1, 9, 1, 11),
    _AgentVpcDomainSourceIpAddr_Type()
)
agentVpcDomainSourceIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentVpcDomainSourceIpAddr.setStatus("current")


class _AgentVpcDomainDcpdpUdpPort_Type(Unsigned32):
    """Custom type agentVpcDomainDcpdpUdpPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AgentVpcDomainDcpdpUdpPort_Type.__name__ = "Unsigned32"
_AgentVpcDomainDcpdpUdpPort_Object = MibTableColumn
agentVpcDomainDcpdpUdpPort = _AgentVpcDomainDcpdpUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 200, 1, 9, 1, 12),
    _AgentVpcDomainDcpdpUdpPort_Type()
)
agentVpcDomainDcpdpUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentVpcDomainDcpdpUdpPort.setStatus("current")
_AgentVpcDomainStatus_Type = RowStatus
_AgentVpcDomainStatus_Object = MibTableColumn
agentVpcDomainStatus = _AgentVpcDomainStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 200, 1, 9, 1, 13),
    _AgentVpcDomainStatus_Type()
)
agentVpcDomainStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentVpcDomainStatus.setStatus("current")
_AgentVpcPeerKeepAliveStatsGroup_ObjectIdentity = ObjectIdentity
agentVpcPeerKeepAliveStatsGroup = _AgentVpcPeerKeepAliveStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 200, 2)
)
_AgentVpcPeerKeepAliveTotalTx_Type = Unsigned32
_AgentVpcPeerKeepAliveTotalTx_Object = MibScalar
agentVpcPeerKeepAliveTotalTx = _AgentVpcPeerKeepAliveTotalTx_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 200, 2, 1),
    _AgentVpcPeerKeepAliveTotalTx_Type()
)
agentVpcPeerKeepAliveTotalTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentVpcPeerKeepAliveTotalTx.setStatus("current")
_AgentVpcPeerKeepAliveSuccessTx_Type = Unsigned32
_AgentVpcPeerKeepAliveSuccessTx_Object = MibScalar
agentVpcPeerKeepAliveSuccessTx = _AgentVpcPeerKeepAliveSuccessTx_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 200, 2, 2),
    _AgentVpcPeerKeepAliveSuccessTx_Type()
)
agentVpcPeerKeepAliveSuccessTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentVpcPeerKeepAliveSuccessTx.setStatus("current")
_AgentVpcPeerKeepAliveTxErrors_Type = Unsigned32
_AgentVpcPeerKeepAliveTxErrors_Object = MibScalar
agentVpcPeerKeepAliveTxErrors = _AgentVpcPeerKeepAliveTxErrors_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 200, 2, 3),
    _AgentVpcPeerKeepAliveTxErrors_Type()
)
agentVpcPeerKeepAliveTxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentVpcPeerKeepAliveTxErrors.setStatus("current")
_AgentVpcPeerKeepAliveTotalRx_Type = Unsigned32
_AgentVpcPeerKeepAliveTotalRx_Object = MibScalar
agentVpcPeerKeepAliveTotalRx = _AgentVpcPeerKeepAliveTotalRx_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 200, 2, 4),
    _AgentVpcPeerKeepAliveTotalRx_Type()
)
agentVpcPeerKeepAliveTotalRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentVpcPeerKeepAliveTotalRx.setStatus("current")
_AgentVpcPeerKeepAliveSuccessRx_Type = Unsigned32
_AgentVpcPeerKeepAliveSuccessRx_Object = MibScalar
agentVpcPeerKeepAliveSuccessRx = _AgentVpcPeerKeepAliveSuccessRx_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 200, 2, 5),
    _AgentVpcPeerKeepAliveSuccessRx_Type()
)
agentVpcPeerKeepAliveSuccessRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentVpcPeerKeepAliveSuccessRx.setStatus("current")
_AgentVpcPeerKeepAliveRxErrors_Type = Unsigned32
_AgentVpcPeerKeepAliveRxErrors_Object = MibScalar
agentVpcPeerKeepAliveRxErrors = _AgentVpcPeerKeepAliveRxErrors_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 200, 2, 6),
    _AgentVpcPeerKeepAliveRxErrors_Type()
)
agentVpcPeerKeepAliveRxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentVpcPeerKeepAliveRxErrors.setStatus("current")
_AgentVpcPeerKeepAliveTimeoutCount_Type = Unsigned32
_AgentVpcPeerKeepAliveTimeoutCount_Object = MibScalar
agentVpcPeerKeepAliveTimeoutCount = _AgentVpcPeerKeepAliveTimeoutCount_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 200, 2, 7),
    _AgentVpcPeerKeepAliveTimeoutCount_Type()
)
agentVpcPeerKeepAliveTimeoutCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentVpcPeerKeepAliveTimeoutCount.setStatus("current")
_AgentVpcPeerLinkStatsGroup_ObjectIdentity = ObjectIdentity
agentVpcPeerLinkStatsGroup = _AgentVpcPeerLinkStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 200, 3)
)
_AgentVpcPeerLinkControlMsgTx_Type = Unsigned32
_AgentVpcPeerLinkControlMsgTx_Object = MibScalar
agentVpcPeerLinkControlMsgTx = _AgentVpcPeerLinkControlMsgTx_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 200, 3, 1),
    _AgentVpcPeerLinkControlMsgTx_Type()
)
agentVpcPeerLinkControlMsgTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentVpcPeerLinkControlMsgTx.setStatus("current")
_AgentVpcPeerLinkTxErrors_Type = Unsigned32
_AgentVpcPeerLinkTxErrors_Object = MibScalar
agentVpcPeerLinkTxErrors = _AgentVpcPeerLinkTxErrors_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 200, 3, 2),
    _AgentVpcPeerLinkTxErrors_Type()
)
agentVpcPeerLinkTxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentVpcPeerLinkTxErrors.setStatus("current")
_AgentVpcPeerLinkTxTimeout_Type = Unsigned32
_AgentVpcPeerLinkTxTimeout_Object = MibScalar
agentVpcPeerLinkTxTimeout = _AgentVpcPeerLinkTxTimeout_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 200, 3, 3),
    _AgentVpcPeerLinkTxTimeout_Type()
)
agentVpcPeerLinkTxTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentVpcPeerLinkTxTimeout.setStatus("current")
_AgentVpcPeerLinkControlMsgAckTx_Type = Unsigned32
_AgentVpcPeerLinkControlMsgAckTx_Object = MibScalar
agentVpcPeerLinkControlMsgAckTx = _AgentVpcPeerLinkControlMsgAckTx_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 200, 3, 4),
    _AgentVpcPeerLinkControlMsgAckTx_Type()
)
agentVpcPeerLinkControlMsgAckTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentVpcPeerLinkControlMsgAckTx.setStatus("current")
_AgentVpcPeerLinkControlMsgAckErrors_Type = Unsigned32
_AgentVpcPeerLinkControlMsgAckErrors_Object = MibScalar
agentVpcPeerLinkControlMsgAckErrors = _AgentVpcPeerLinkControlMsgAckErrors_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 200, 3, 5),
    _AgentVpcPeerLinkControlMsgAckErrors_Type()
)
agentVpcPeerLinkControlMsgAckErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentVpcPeerLinkControlMsgAckErrors.setStatus("current")
_AgentVpcPeerLinkControlMsgRx_Type = Unsigned32
_AgentVpcPeerLinkControlMsgRx_Object = MibScalar
agentVpcPeerLinkControlMsgRx = _AgentVpcPeerLinkControlMsgRx_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 200, 3, 6),
    _AgentVpcPeerLinkControlMsgRx_Type()
)
agentVpcPeerLinkControlMsgRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentVpcPeerLinkControlMsgRx.setStatus("current")
_AgentVpcPeerLinkDataMsgTx_Type = Unsigned32
_AgentVpcPeerLinkDataMsgTx_Object = MibScalar
agentVpcPeerLinkDataMsgTx = _AgentVpcPeerLinkDataMsgTx_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 200, 3, 7),
    _AgentVpcPeerLinkDataMsgTx_Type()
)
agentVpcPeerLinkDataMsgTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentVpcPeerLinkDataMsgTx.setStatus("current")
_AgentVpcPeerLinkDataMsgTxErrors_Type = Unsigned32
_AgentVpcPeerLinkDataMsgTxErrors_Object = MibScalar
agentVpcPeerLinkDataMsgTxErrors = _AgentVpcPeerLinkDataMsgTxErrors_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 200, 3, 8),
    _AgentVpcPeerLinkDataMsgTxErrors_Type()
)
agentVpcPeerLinkDataMsgTxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentVpcPeerLinkDataMsgTxErrors.setStatus("current")
_AgentVpcPeerLinkDataMsgTxTimeout_Type = Unsigned32
_AgentVpcPeerLinkDataMsgTxTimeout_Object = MibScalar
agentVpcPeerLinkDataMsgTxTimeout = _AgentVpcPeerLinkDataMsgTxTimeout_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 200, 3, 9),
    _AgentVpcPeerLinkDataMsgTxTimeout_Type()
)
agentVpcPeerLinkDataMsgTxTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentVpcPeerLinkDataMsgTxTimeout.setStatus("current")
_AgentVpcPeerLinkDataMsgRx_Type = Unsigned32
_AgentVpcPeerLinkDataMsgRx_Object = MibScalar
agentVpcPeerLinkDataMsgRx = _AgentVpcPeerLinkDataMsgRx_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 200, 3, 10),
    _AgentVpcPeerLinkDataMsgRx_Type()
)
agentVpcPeerLinkDataMsgRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentVpcPeerLinkDataMsgRx.setStatus("current")
_AgentVpcPeerLinkBPDUTx_Type = Unsigned32
_AgentVpcPeerLinkBPDUTx_Object = MibScalar
agentVpcPeerLinkBPDUTx = _AgentVpcPeerLinkBPDUTx_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 200, 3, 11),
    _AgentVpcPeerLinkBPDUTx_Type()
)
agentVpcPeerLinkBPDUTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentVpcPeerLinkBPDUTx.setStatus("current")
_AgentVpcPeerLinkBPDUTxErrors_Type = Unsigned32
_AgentVpcPeerLinkBPDUTxErrors_Object = MibScalar
agentVpcPeerLinkBPDUTxErrors = _AgentVpcPeerLinkBPDUTxErrors_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 200, 3, 12),
    _AgentVpcPeerLinkBPDUTxErrors_Type()
)
agentVpcPeerLinkBPDUTxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentVpcPeerLinkBPDUTxErrors.setStatus("current")
_AgentVpcPeerLinkBPDUrx_Type = Unsigned32
_AgentVpcPeerLinkBPDUrx_Object = MibScalar
agentVpcPeerLinkBPDUrx = _AgentVpcPeerLinkBPDUrx_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 200, 3, 13),
    _AgentVpcPeerLinkBPDUrx_Type()
)
agentVpcPeerLinkBPDUrx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentVpcPeerLinkBPDUrx.setStatus("current")
_AgentVpcPeerLinkBPDURxErrors_Type = Unsigned32
_AgentVpcPeerLinkBPDURxErrors_Object = MibScalar
agentVpcPeerLinkBPDURxErrors = _AgentVpcPeerLinkBPDURxErrors_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 200, 3, 14),
    _AgentVpcPeerLinkBPDURxErrors_Type()
)
agentVpcPeerLinkBPDURxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentVpcPeerLinkBPDURxErrors.setStatus("current")
_AgentVpcPeerLinkLACPDUTx_Type = Unsigned32
_AgentVpcPeerLinkLACPDUTx_Object = MibScalar
agentVpcPeerLinkLACPDUTx = _AgentVpcPeerLinkLACPDUTx_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 200, 3, 15),
    _AgentVpcPeerLinkLACPDUTx_Type()
)
agentVpcPeerLinkLACPDUTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentVpcPeerLinkLACPDUTx.setStatus("current")
_AgentVpcPeerLinkLACPDUTxErrors_Type = Unsigned32
_AgentVpcPeerLinkLACPDUTxErrors_Object = MibScalar
agentVpcPeerLinkLACPDUTxErrors = _AgentVpcPeerLinkLACPDUTxErrors_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 200, 3, 16),
    _AgentVpcPeerLinkLACPDUTxErrors_Type()
)
agentVpcPeerLinkLACPDUTxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentVpcPeerLinkLACPDUTxErrors.setStatus("current")
_AgentVpcPeerLinkLACPDUrx_Type = Unsigned32
_AgentVpcPeerLinkLACPDUrx_Object = MibScalar
agentVpcPeerLinkLACPDUrx = _AgentVpcPeerLinkLACPDUrx_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 200, 3, 17),
    _AgentVpcPeerLinkLACPDUrx_Type()
)
agentVpcPeerLinkLACPDUrx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentVpcPeerLinkLACPDUrx.setStatus("current")
_AgentVpcPeerLinkLACPDURxErrors_Type = Unsigned32
_AgentVpcPeerLinkLACPDURxErrors_Object = MibScalar
agentVpcPeerLinkLACPDURxErrors = _AgentVpcPeerLinkLACPDURxErrors_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 200, 3, 18),
    _AgentVpcPeerLinkLACPDURxErrors_Type()
)
agentVpcPeerLinkLACPDURxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentVpcPeerLinkLACPDURxErrors.setStatus("current")
_AgentVpcStatusGroup_ObjectIdentity = ObjectIdentity
agentVpcStatusGroup = _AgentVpcStatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 200, 4)
)
_AgentVpcPeerLinkStatus_Type = TruthValue
_AgentVpcPeerLinkStatus_Object = MibScalar
agentVpcPeerLinkStatus = _AgentVpcPeerLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 200, 4, 1),
    _AgentVpcPeerLinkStatus_Type()
)
agentVpcPeerLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentVpcPeerLinkStatus.setStatus("current")
_AgentVpcTotalVpcConfigured_Type = Unsigned32
_AgentVpcTotalVpcConfigured_Object = MibScalar
agentVpcTotalVpcConfigured = _AgentVpcTotalVpcConfigured_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 200, 4, 2),
    _AgentVpcTotalVpcConfigured_Type()
)
agentVpcTotalVpcConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentVpcTotalVpcConfigured.setStatus("current")
_AgentVpcTotalVpcOperational_Type = Unsigned32
_AgentVpcTotalVpcOperational_Object = MibScalar
agentVpcTotalVpcOperational = _AgentVpcTotalVpcOperational_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 200, 4, 3),
    _AgentVpcTotalVpcOperational_Type()
)
agentVpcTotalVpcOperational.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentVpcTotalVpcOperational.setStatus("current")


class _AgentVpcSelfRole_Type(Integer32):
    """Custom type agentVpcSelfRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("primary", 2),
          ("secondary", 3))
    )


_AgentVpcSelfRole_Type.__name__ = "Integer32"
_AgentVpcSelfRole_Object = MibScalar
agentVpcSelfRole = _AgentVpcSelfRole_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 200, 4, 4),
    _AgentVpcSelfRole_Type()
)
agentVpcSelfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentVpcSelfRole.setStatus("current")


class _AgentVpcOperationMode_Type(Integer32):
    """Custom type agentVpcOperationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AgentVpcOperationMode_Type.__name__ = "Integer32"
_AgentVpcOperationMode_Object = MibScalar
agentVpcOperationMode = _AgentVpcOperationMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 200, 4, 5),
    _AgentVpcOperationMode_Type()
)
agentVpcOperationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentVpcOperationMode.setStatus("current")


class _AgentVpcPeerRole_Type(Integer32):
    """Custom type agentVpcPeerRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("primary", 2),
          ("secondary", 3))
    )


_AgentVpcPeerRole_Type.__name__ = "Integer32"
_AgentVpcPeerRole_Object = MibScalar
agentVpcPeerRole = _AgentVpcPeerRole_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 200, 4, 6),
    _AgentVpcPeerRole_Type()
)
agentVpcPeerRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentVpcPeerRole.setStatus("current")


class _AgentVpcKeepaliveOperationalMode_Type(Integer32):
    """Custom type agentVpcKeepaliveOperationalMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AgentVpcKeepaliveOperationalMode_Type.__name__ = "Integer32"
_AgentVpcKeepaliveOperationalMode_Object = MibScalar
agentVpcKeepaliveOperationalMode = _AgentVpcKeepaliveOperationalMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 200, 4, 7),
    _AgentVpcKeepaliveOperationalMode_Type()
)
agentVpcKeepaliveOperationalMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentVpcKeepaliveOperationalMode.setStatus("current")
_AgentVpcSystemMac_Type = MacAddress
_AgentVpcSystemMac_Object = MibScalar
agentVpcSystemMac = _AgentVpcSystemMac_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 200, 4, 8),
    _AgentVpcSystemMac_Type()
)
agentVpcSystemMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentVpcSystemMac.setStatus("current")


class _AgentVpcState_Type(Integer32):
    """Custom type agentVpcState based on Integer32"""
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
        *(("disable", 1),
          ("listen", 2),
          ("ready", 3),
          ("primary", 4),
          ("secondary", 5))
    )


_AgentVpcState_Type.__name__ = "Integer32"
_AgentVpcState_Object = MibScalar
agentVpcState = _AgentVpcState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 200, 4, 9),
    _AgentVpcState_Type()
)
agentVpcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentVpcState.setStatus("current")
_AgentVpcPeerPriority_Type = Unsigned32
_AgentVpcPeerPriority_Object = MibScalar
agentVpcPeerPriority = _AgentVpcPeerPriority_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 200, 4, 10),
    _AgentVpcPeerPriority_Type()
)
agentVpcPeerPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentVpcPeerPriority.setStatus("current")
_AgentVpcPeerMac_Type = MacAddress
_AgentVpcPeerMac_Object = MibScalar
agentVpcPeerMac = _AgentVpcPeerMac_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 200, 4, 11),
    _AgentVpcPeerMac_Type()
)
agentVpcPeerMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentVpcPeerMac.setStatus("current")
_AgentVpcPeerDetectionStatus_Type = TruthValue
_AgentVpcPeerDetectionStatus_Object = MibScalar
agentVpcPeerDetectionStatus = _AgentVpcPeerDetectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 200, 4, 12),
    _AgentVpcPeerDetectionStatus_Type()
)
agentVpcPeerDetectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentVpcPeerDetectionStatus.setStatus("current")
_AgentVpcIsPeerDetected_Type = TruthValue
_AgentVpcIsPeerDetected_Object = MibScalar
agentVpcIsPeerDetected = _AgentVpcIsPeerDetected_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 200, 4, 13),
    _AgentVpcIsPeerDetected_Type()
)
agentVpcIsPeerDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentVpcIsPeerDetected.setStatus("current")
_AgentVpcSelfMemberStatusTable_Object = MibTable
agentVpcSelfMemberStatusTable = _AgentVpcSelfMemberStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 200, 4, 14)
)
if mibBuilder.loadTexts:
    agentVpcSelfMemberStatusTable.setStatus("current")
_AgentVpcSelfMemberStatusEntry_Object = MibTableRow
agentVpcSelfMemberStatusEntry = _AgentVpcSelfMemberStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 200, 4, 14, 1)
)
agentVpcSelfMemberStatusEntry.setIndexNames(
    (0, "DNOS-VPC-MIB", "agentVpcSelfMemberStatusVpcId"),
    (0, "DNOS-VPC-MIB", "agentVpcSelfMemberStatusIntfId"),
)
if mibBuilder.loadTexts:
    agentVpcSelfMemberStatusEntry.setStatus("current")


class _AgentVpcSelfMemberStatusVpcId_Type(Unsigned32):
    """Custom type agentVpcSelfMemberStatusVpcId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_AgentVpcSelfMemberStatusVpcId_Type.__name__ = "Unsigned32"
_AgentVpcSelfMemberStatusVpcId_Object = MibTableColumn
agentVpcSelfMemberStatusVpcId = _AgentVpcSelfMemberStatusVpcId_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 200, 4, 14, 1, 1),
    _AgentVpcSelfMemberStatusVpcId_Type()
)
agentVpcSelfMemberStatusVpcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentVpcSelfMemberStatusVpcId.setStatus("current")
_AgentVpcSelfMemberStatusIntfId_Type = InterfaceIndex
_AgentVpcSelfMemberStatusIntfId_Object = MibTableColumn
agentVpcSelfMemberStatusIntfId = _AgentVpcSelfMemberStatusIntfId_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 200, 4, 14, 1, 2),
    _AgentVpcSelfMemberStatusIntfId_Type()
)
agentVpcSelfMemberStatusIntfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentVpcSelfMemberStatusIntfId.setStatus("current")


class _AgentVpcSelfMemberStatusIntfState_Type(Integer32):
    """Custom type agentVpcSelfMemberStatusIntfState based on Integer32"""
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


_AgentVpcSelfMemberStatusIntfState_Type.__name__ = "Integer32"
_AgentVpcSelfMemberStatusIntfState_Object = MibTableColumn
agentVpcSelfMemberStatusIntfState = _AgentVpcSelfMemberStatusIntfState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 200, 4, 14, 1, 3),
    _AgentVpcSelfMemberStatusIntfState_Type()
)
agentVpcSelfMemberStatusIntfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentVpcSelfMemberStatusIntfState.setStatus("current")
_AgentVpcPeerMemberStatusTable_Object = MibTable
agentVpcPeerMemberStatusTable = _AgentVpcPeerMemberStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 200, 4, 15)
)
if mibBuilder.loadTexts:
    agentVpcPeerMemberStatusTable.setStatus("current")
_AgentVpcPeerMemberStatusEntry_Object = MibTableRow
agentVpcPeerMemberStatusEntry = _AgentVpcPeerMemberStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 200, 4, 15, 1)
)
agentVpcPeerMemberStatusEntry.setIndexNames(
    (0, "DNOS-VPC-MIB", "agentVpcPeerMemberStatusVpcId"),
    (0, "DNOS-VPC-MIB", "agentVpcPeerMemberStatusIntfId"),
)
if mibBuilder.loadTexts:
    agentVpcPeerMemberStatusEntry.setStatus("current")


class _AgentVpcPeerMemberStatusVpcId_Type(Unsigned32):
    """Custom type agentVpcPeerMemberStatusVpcId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_AgentVpcPeerMemberStatusVpcId_Type.__name__ = "Unsigned32"
_AgentVpcPeerMemberStatusVpcId_Object = MibTableColumn
agentVpcPeerMemberStatusVpcId = _AgentVpcPeerMemberStatusVpcId_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 200, 4, 15, 1, 1),
    _AgentVpcPeerMemberStatusVpcId_Type()
)
agentVpcPeerMemberStatusVpcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentVpcPeerMemberStatusVpcId.setStatus("current")
_AgentVpcPeerMemberStatusIntfId_Type = InterfaceIndex
_AgentVpcPeerMemberStatusIntfId_Object = MibTableColumn
agentVpcPeerMemberStatusIntfId = _AgentVpcPeerMemberStatusIntfId_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 200, 4, 15, 1, 2),
    _AgentVpcPeerMemberStatusIntfId_Type()
)
agentVpcPeerMemberStatusIntfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentVpcPeerMemberStatusIntfId.setStatus("current")


class _AgentVpcPeerMemberStatusIntfState_Type(Integer32):
    """Custom type agentVpcPeerMemberStatusIntfState based on Integer32"""
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


_AgentVpcPeerMemberStatusIntfState_Type.__name__ = "Integer32"
_AgentVpcPeerMemberStatusIntfState_Object = MibTableColumn
agentVpcPeerMemberStatusIntfState = _AgentVpcPeerMemberStatusIntfState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 200, 4, 15, 1, 3),
    _AgentVpcPeerMemberStatusIntfState_Type()
)
agentVpcPeerMemberStatusIntfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentVpcPeerMemberStatusIntfState.setStatus("current")
_AgentVpcStatusTable_Object = MibTable
agentVpcStatusTable = _AgentVpcStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 200, 4, 16)
)
if mibBuilder.loadTexts:
    agentVpcStatusTable.setStatus("current")
_AgentVpcStatusEntry_Object = MibTableRow
agentVpcStatusEntry = _AgentVpcStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 200, 4, 16, 1)
)
agentVpcStatusEntry.setIndexNames(
    (0, "DNOS-VPC-MIB", "agentVpcStatusId"),
)
if mibBuilder.loadTexts:
    agentVpcStatusEntry.setStatus("current")


class _AgentVpcStatusId_Type(Unsigned32):
    """Custom type agentVpcStatusId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_AgentVpcStatusId_Type.__name__ = "Unsigned32"
_AgentVpcStatusId_Object = MibTableColumn
agentVpcStatusId = _AgentVpcStatusId_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 200, 4, 16, 1, 1),
    _AgentVpcStatusId_Type()
)
agentVpcStatusId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentVpcStatusId.setStatus("current")


class _AgentVpcOperationalStatus_Type(Integer32):
    """Custom type agentVpcOperationalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AgentVpcOperationalStatus_Type.__name__ = "Integer32"
_AgentVpcOperationalStatus_Object = MibTableColumn
agentVpcOperationalStatus = _AgentVpcOperationalStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 200, 4, 16, 1, 2),
    _AgentVpcOperationalStatus_Type()
)
agentVpcOperationalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentVpcOperationalStatus.setStatus("current")
_AgentPortChannelId_Type = InterfaceIndex
_AgentPortChannelId_Object = MibTableColumn
agentPortChannelId = _AgentPortChannelId_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 200, 4, 16, 1, 3),
    _AgentPortChannelId_Type()
)
agentPortChannelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentPortChannelId.setStatus("current")


class _AgentVpcInterfaceState_Type(Integer32):
    """Custom type agentVpcInterfaceState based on Integer32"""
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
        *(("disable", 1),
          ("wait", 2),
          ("error", 3),
          ("active", 4),
          ("inactive", 5))
    )


_AgentVpcInterfaceState_Type.__name__ = "Integer32"
_AgentVpcInterfaceState_Object = MibTableColumn
agentVpcInterfaceState = _AgentVpcInterfaceState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 200, 4, 16, 1, 4),
    _AgentVpcInterfaceState_Type()
)
agentVpcInterfaceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentVpcInterfaceState.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DNOS-VPC-MIB",
    **{"fastPathVpc": fastPathVpc,
       "agentVpcConfigGroup": agentVpcConfigGroup,
       "agentVpcMode": agentVpcMode,
       "agentKeepalivePriority": agentKeepalivePriority,
       "agentKeepaliveTimeout": agentKeepaliveTimeout,
       "agentKeepaliveMode": agentKeepaliveMode,
       "agentPeerLink": agentPeerLink,
       "agentPeerDetectionMode": agentPeerDetectionMode,
       "agentVpcConfigTable": agentVpcConfigTable,
       "agentVpcConfigEntry": agentVpcConfigEntry,
       "agentVpcConfigId": agentVpcConfigId,
       "agentVpcTrackPortMask": agentVpcTrackPortMask,
       "agentPeerConfigTable": agentPeerConfigTable,
       "agentPeerConfigEntry": agentPeerConfigEntry,
       "agentPeerConfigRowIndex": agentPeerConfigRowIndex,
       "agentPeerIpAddr": agentPeerIpAddr,
       "agentSourceIpAddr": agentSourceIpAddr,
       "agentDcpdpUdpPort": agentDcpdpUdpPort,
       "agentPeerRowStatus": agentPeerRowStatus,
       "agentVpcDomainConfigTable": agentVpcDomainConfigTable,
       "agentVpcDomainConfigEntry": agentVpcDomainConfigEntry,
       "agentVpcDomainIndex": agentVpcDomainIndex,
       "agentVpcDomainKeepalivePriority": agentVpcDomainKeepalivePriority,
       "agentVpcDomainKeepaliveTimeout": agentVpcDomainKeepaliveTimeout,
       "agentVpcDomainKeepaliveMode": agentVpcDomainKeepaliveMode,
       "agentVpcDomainPeerDetectionMode": agentVpcDomainPeerDetectionMode,
       "agentVpcDomainSystemMac": agentVpcDomainSystemMac,
       "agentVpcDomainSystemPriority": agentVpcDomainSystemPriority,
       "agentVpcDomainPeerDetectionInterval": agentVpcDomainPeerDetectionInterval,
       "agentVpcDomainPeerDetectionTimeout": agentVpcDomainPeerDetectionTimeout,
       "agentVpcDomainPeerIpAddr": agentVpcDomainPeerIpAddr,
       "agentVpcDomainSourceIpAddr": agentVpcDomainSourceIpAddr,
       "agentVpcDomainDcpdpUdpPort": agentVpcDomainDcpdpUdpPort,
       "agentVpcDomainStatus": agentVpcDomainStatus,
       "agentVpcPeerKeepAliveStatsGroup": agentVpcPeerKeepAliveStatsGroup,
       "agentVpcPeerKeepAliveTotalTx": agentVpcPeerKeepAliveTotalTx,
       "agentVpcPeerKeepAliveSuccessTx": agentVpcPeerKeepAliveSuccessTx,
       "agentVpcPeerKeepAliveTxErrors": agentVpcPeerKeepAliveTxErrors,
       "agentVpcPeerKeepAliveTotalRx": agentVpcPeerKeepAliveTotalRx,
       "agentVpcPeerKeepAliveSuccessRx": agentVpcPeerKeepAliveSuccessRx,
       "agentVpcPeerKeepAliveRxErrors": agentVpcPeerKeepAliveRxErrors,
       "agentVpcPeerKeepAliveTimeoutCount": agentVpcPeerKeepAliveTimeoutCount,
       "agentVpcPeerLinkStatsGroup": agentVpcPeerLinkStatsGroup,
       "agentVpcPeerLinkControlMsgTx": agentVpcPeerLinkControlMsgTx,
       "agentVpcPeerLinkTxErrors": agentVpcPeerLinkTxErrors,
       "agentVpcPeerLinkTxTimeout": agentVpcPeerLinkTxTimeout,
       "agentVpcPeerLinkControlMsgAckTx": agentVpcPeerLinkControlMsgAckTx,
       "agentVpcPeerLinkControlMsgAckErrors": agentVpcPeerLinkControlMsgAckErrors,
       "agentVpcPeerLinkControlMsgRx": agentVpcPeerLinkControlMsgRx,
       "agentVpcPeerLinkDataMsgTx": agentVpcPeerLinkDataMsgTx,
       "agentVpcPeerLinkDataMsgTxErrors": agentVpcPeerLinkDataMsgTxErrors,
       "agentVpcPeerLinkDataMsgTxTimeout": agentVpcPeerLinkDataMsgTxTimeout,
       "agentVpcPeerLinkDataMsgRx": agentVpcPeerLinkDataMsgRx,
       "agentVpcPeerLinkBPDUTx": agentVpcPeerLinkBPDUTx,
       "agentVpcPeerLinkBPDUTxErrors": agentVpcPeerLinkBPDUTxErrors,
       "agentVpcPeerLinkBPDUrx": agentVpcPeerLinkBPDUrx,
       "agentVpcPeerLinkBPDURxErrors": agentVpcPeerLinkBPDURxErrors,
       "agentVpcPeerLinkLACPDUTx": agentVpcPeerLinkLACPDUTx,
       "agentVpcPeerLinkLACPDUTxErrors": agentVpcPeerLinkLACPDUTxErrors,
       "agentVpcPeerLinkLACPDUrx": agentVpcPeerLinkLACPDUrx,
       "agentVpcPeerLinkLACPDURxErrors": agentVpcPeerLinkLACPDURxErrors,
       "agentVpcStatusGroup": agentVpcStatusGroup,
       "agentVpcPeerLinkStatus": agentVpcPeerLinkStatus,
       "agentVpcTotalVpcConfigured": agentVpcTotalVpcConfigured,
       "agentVpcTotalVpcOperational": agentVpcTotalVpcOperational,
       "agentVpcSelfRole": agentVpcSelfRole,
       "agentVpcOperationMode": agentVpcOperationMode,
       "agentVpcPeerRole": agentVpcPeerRole,
       "agentVpcKeepaliveOperationalMode": agentVpcKeepaliveOperationalMode,
       "agentVpcSystemMac": agentVpcSystemMac,
       "agentVpcState": agentVpcState,
       "agentVpcPeerPriority": agentVpcPeerPriority,
       "agentVpcPeerMac": agentVpcPeerMac,
       "agentVpcPeerDetectionStatus": agentVpcPeerDetectionStatus,
       "agentVpcIsPeerDetected": agentVpcIsPeerDetected,
       "agentVpcSelfMemberStatusTable": agentVpcSelfMemberStatusTable,
       "agentVpcSelfMemberStatusEntry": agentVpcSelfMemberStatusEntry,
       "agentVpcSelfMemberStatusVpcId": agentVpcSelfMemberStatusVpcId,
       "agentVpcSelfMemberStatusIntfId": agentVpcSelfMemberStatusIntfId,
       "agentVpcSelfMemberStatusIntfState": agentVpcSelfMemberStatusIntfState,
       "agentVpcPeerMemberStatusTable": agentVpcPeerMemberStatusTable,
       "agentVpcPeerMemberStatusEntry": agentVpcPeerMemberStatusEntry,
       "agentVpcPeerMemberStatusVpcId": agentVpcPeerMemberStatusVpcId,
       "agentVpcPeerMemberStatusIntfId": agentVpcPeerMemberStatusIntfId,
       "agentVpcPeerMemberStatusIntfState": agentVpcPeerMemberStatusIntfState,
       "agentVpcStatusTable": agentVpcStatusTable,
       "agentVpcStatusEntry": agentVpcStatusEntry,
       "agentVpcStatusId": agentVpcStatusId,
       "agentVpcOperationalStatus": agentVpcOperationalStatus,
       "agentPortChannelId": agentPortChannelId,
       "agentVpcInterfaceState": agentVpcInterfaceState}
)
