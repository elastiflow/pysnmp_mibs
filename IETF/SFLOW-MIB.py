# SNMP MIB module (SFLOW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/Standards/IETF/SFLOW-MIB.mib
# Produced by pysmi-1.5.11 at Wed May 21 15:01:16 2025
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(OwnerString,) = mibBuilder.importSymbols(
    "RMON-MIB",
    "OwnerString")

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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

sFlowMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4300, 1)
)
if mibBuilder.loadTexts:
    sFlowMIB.setRevisions(
        ("2001-05-15 00:00",
         "2001-05-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SFlowAgent_ObjectIdentity = ObjectIdentity
sFlowAgent = _SFlowAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4300, 1, 1)
)


class _SFlowVersion_Type(SnmpAdminString):
    """Custom type sFlowVersion based on SnmpAdminString"""
    defaultValue = OctetString("1.2;;")


_SFlowVersion_Type.__name__ = "SnmpAdminString"
_SFlowVersion_Object = MibScalar
sFlowVersion = _SFlowVersion_Object(
    (1, 3, 6, 1, 4, 1, 4300, 1, 1, 1),
    _SFlowVersion_Type()
)
sFlowVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sFlowVersion.setStatus("current")
_SFlowAgentAddressType_Type = InetAddressType
_SFlowAgentAddressType_Object = MibScalar
sFlowAgentAddressType = _SFlowAgentAddressType_Object(
    (1, 3, 6, 1, 4, 1, 4300, 1, 1, 2),
    _SFlowAgentAddressType_Type()
)
sFlowAgentAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sFlowAgentAddressType.setStatus("current")
_SFlowAgentAddress_Type = InetAddress
_SFlowAgentAddress_Object = MibScalar
sFlowAgentAddress = _SFlowAgentAddress_Object(
    (1, 3, 6, 1, 4, 1, 4300, 1, 1, 3),
    _SFlowAgentAddress_Type()
)
sFlowAgentAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sFlowAgentAddress.setStatus("current")
_SFlowTable_Object = MibTable
sFlowTable = _SFlowTable_Object(
    (1, 3, 6, 1, 4, 1, 4300, 1, 1, 4)
)
if mibBuilder.loadTexts:
    sFlowTable.setStatus("current")
_SFlowEntry_Object = MibTableRow
sFlowEntry = _SFlowEntry_Object(
    (1, 3, 6, 1, 4, 1, 4300, 1, 1, 4, 1)
)
sFlowEntry.setIndexNames(
    (0, "SFLOW-MIB", "sFlowDataSource"),
)
if mibBuilder.loadTexts:
    sFlowEntry.setStatus("current")
_SFlowDataSource_Type = ObjectIdentifier
_SFlowDataSource_Object = MibTableColumn
sFlowDataSource = _SFlowDataSource_Object(
    (1, 3, 6, 1, 4, 1, 4300, 1, 1, 4, 1, 1),
    _SFlowDataSource_Type()
)
sFlowDataSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sFlowDataSource.setStatus("current")


class _SFlowOwner_Type(OwnerString):
    """Custom type sFlowOwner based on OwnerString"""
    defaultValue = OctetString("")


_SFlowOwner_Type.__name__ = "OwnerString"
_SFlowOwner_Object = MibTableColumn
sFlowOwner = _SFlowOwner_Object(
    (1, 3, 6, 1, 4, 1, 4300, 1, 1, 4, 1, 2),
    _SFlowOwner_Type()
)
sFlowOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sFlowOwner.setStatus("current")


class _SFlowTimeout_Type(Integer32):
    """Custom type sFlowTimeout based on Integer32"""
    defaultValue = 0


_SFlowTimeout_Type.__name__ = "Integer32"
_SFlowTimeout_Object = MibTableColumn
sFlowTimeout = _SFlowTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4300, 1, 1, 4, 1, 3),
    _SFlowTimeout_Type()
)
sFlowTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sFlowTimeout.setStatus("current")


class _SFlowPacketSamplingRate_Type(Integer32):
    """Custom type sFlowPacketSamplingRate based on Integer32"""
    defaultValue = 0


_SFlowPacketSamplingRate_Type.__name__ = "Integer32"
_SFlowPacketSamplingRate_Object = MibTableColumn
sFlowPacketSamplingRate = _SFlowPacketSamplingRate_Object(
    (1, 3, 6, 1, 4, 1, 4300, 1, 1, 4, 1, 4),
    _SFlowPacketSamplingRate_Type()
)
sFlowPacketSamplingRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sFlowPacketSamplingRate.setStatus("current")


class _SFlowCounterSamplingInterval_Type(Integer32):
    """Custom type sFlowCounterSamplingInterval based on Integer32"""
    defaultValue = 0


_SFlowCounterSamplingInterval_Type.__name__ = "Integer32"
_SFlowCounterSamplingInterval_Object = MibTableColumn
sFlowCounterSamplingInterval = _SFlowCounterSamplingInterval_Object(
    (1, 3, 6, 1, 4, 1, 4300, 1, 1, 4, 1, 5),
    _SFlowCounterSamplingInterval_Type()
)
sFlowCounterSamplingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sFlowCounterSamplingInterval.setStatus("current")


class _SFlowMaximumHeaderSize_Type(Integer32):
    """Custom type sFlowMaximumHeaderSize based on Integer32"""
    defaultValue = 128


_SFlowMaximumHeaderSize_Type.__name__ = "Integer32"
_SFlowMaximumHeaderSize_Object = MibTableColumn
sFlowMaximumHeaderSize = _SFlowMaximumHeaderSize_Object(
    (1, 3, 6, 1, 4, 1, 4300, 1, 1, 4, 1, 6),
    _SFlowMaximumHeaderSize_Type()
)
sFlowMaximumHeaderSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sFlowMaximumHeaderSize.setStatus("current")


class _SFlowMaximumDatagramSize_Type(Integer32):
    """Custom type sFlowMaximumDatagramSize based on Integer32"""
    defaultValue = 1400


_SFlowMaximumDatagramSize_Type.__name__ = "Integer32"
_SFlowMaximumDatagramSize_Object = MibTableColumn
sFlowMaximumDatagramSize = _SFlowMaximumDatagramSize_Object(
    (1, 3, 6, 1, 4, 1, 4300, 1, 1, 4, 1, 7),
    _SFlowMaximumDatagramSize_Type()
)
sFlowMaximumDatagramSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sFlowMaximumDatagramSize.setStatus("current")


class _SFlowCollectorAddressType_Type(InetAddressType):
    """Custom type sFlowCollectorAddressType based on InetAddressType"""
    defaultValue = 1


_SFlowCollectorAddressType_Type.__name__ = "InetAddressType"
_SFlowCollectorAddressType_Object = MibTableColumn
sFlowCollectorAddressType = _SFlowCollectorAddressType_Object(
    (1, 3, 6, 1, 4, 1, 4300, 1, 1, 4, 1, 8),
    _SFlowCollectorAddressType_Type()
)
sFlowCollectorAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sFlowCollectorAddressType.setStatus("current")


class _SFlowCollectorAddress_Type(InetAddress):
    """Custom type sFlowCollectorAddress based on InetAddress"""
    defaultValue = OctetString("0.0.0.0")


_SFlowCollectorAddress_Type.__name__ = "InetAddress"
_SFlowCollectorAddress_Object = MibTableColumn
sFlowCollectorAddress = _SFlowCollectorAddress_Object(
    (1, 3, 6, 1, 4, 1, 4300, 1, 1, 4, 1, 9),
    _SFlowCollectorAddress_Type()
)
sFlowCollectorAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sFlowCollectorAddress.setStatus("current")


class _SFlowCollectorPort_Type(Integer32):
    """Custom type sFlowCollectorPort based on Integer32"""
    defaultValue = 6343


_SFlowCollectorPort_Type.__name__ = "Integer32"
_SFlowCollectorPort_Object = MibTableColumn
sFlowCollectorPort = _SFlowCollectorPort_Object(
    (1, 3, 6, 1, 4, 1, 4300, 1, 1, 4, 1, 10),
    _SFlowCollectorPort_Type()
)
sFlowCollectorPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sFlowCollectorPort.setStatus("current")


class _SFlowDatagramVersion_Type(Integer32):
    """Custom type sFlowDatagramVersion based on Integer32"""
    defaultValue = 4


_SFlowDatagramVersion_Type.__name__ = "Integer32"
_SFlowDatagramVersion_Object = MibTableColumn
sFlowDatagramVersion = _SFlowDatagramVersion_Object(
    (1, 3, 6, 1, 4, 1, 4300, 1, 1, 4, 1, 11),
    _SFlowDatagramVersion_Type()
)
sFlowDatagramVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sFlowDatagramVersion.setStatus("current")
_SFlowMIBConformance_ObjectIdentity = ObjectIdentity
sFlowMIBConformance = _SFlowMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4300, 1, 2)
)
_SFlowMIBGroups_ObjectIdentity = ObjectIdentity
sFlowMIBGroups = _SFlowMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4300, 1, 2, 1)
)
_SFlowMIBCompliances_ObjectIdentity = ObjectIdentity
sFlowMIBCompliances = _SFlowMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4300, 1, 2, 2)
)

# Managed Objects groups

sFlowAgentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4300, 1, 2, 1, 1)
)
sFlowAgentGroup.setObjects(
      *(("SFLOW-MIB", "sFlowVersion"),
        ("SFLOW-MIB", "sFlowAgentAddressType"),
        ("SFLOW-MIB", "sFlowAgentAddress"),
        ("SFLOW-MIB", "sFlowDataSource"),
        ("SFLOW-MIB", "sFlowOwner"),
        ("SFLOW-MIB", "sFlowTimeout"),
        ("SFLOW-MIB", "sFlowPacketSamplingRate"),
        ("SFLOW-MIB", "sFlowCounterSamplingInterval"),
        ("SFLOW-MIB", "sFlowMaximumHeaderSize"),
        ("SFLOW-MIB", "sFlowMaximumDatagramSize"),
        ("SFLOW-MIB", "sFlowCollectorAddressType"),
        ("SFLOW-MIB", "sFlowCollectorAddress"),
        ("SFLOW-MIB", "sFlowCollectorPort"),
        ("SFLOW-MIB", "sFlowDatagramVersion"))
)
if mibBuilder.loadTexts:
    sFlowAgentGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

sFlowCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4300, 1, 2, 2, 1)
)
sFlowCompliance.setObjects(
    ("SFLOW-MIB", "sFlowAgentGroup")
)
if mibBuilder.loadTexts:
    sFlowCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SFLOW-MIB",
    **{"sFlowMIB": sFlowMIB,
       "sFlowAgent": sFlowAgent,
       "sFlowVersion": sFlowVersion,
       "sFlowAgentAddressType": sFlowAgentAddressType,
       "sFlowAgentAddress": sFlowAgentAddress,
       "sFlowTable": sFlowTable,
       "sFlowEntry": sFlowEntry,
       "sFlowDataSource": sFlowDataSource,
       "sFlowOwner": sFlowOwner,
       "sFlowTimeout": sFlowTimeout,
       "sFlowPacketSamplingRate": sFlowPacketSamplingRate,
       "sFlowCounterSamplingInterval": sFlowCounterSamplingInterval,
       "sFlowMaximumHeaderSize": sFlowMaximumHeaderSize,
       "sFlowMaximumDatagramSize": sFlowMaximumDatagramSize,
       "sFlowCollectorAddressType": sFlowCollectorAddressType,
       "sFlowCollectorAddress": sFlowCollectorAddress,
       "sFlowCollectorPort": sFlowCollectorPort,
       "sFlowDatagramVersion": sFlowDatagramVersion,
       "sFlowMIBConformance": sFlowMIBConformance,
       "sFlowMIBGroups": sFlowMIBGroups,
       "sFlowAgentGroup": sFlowAgentGroup,
       "sFlowMIBCompliances": sFlowMIBCompliances,
       "sFlowCompliance": sFlowCompliance}
)
