# SNMP MIB module (CISCO-COMPRESSION-SERVICE-ADAPTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-COMPRESSION-SERVICE-ADAPTER-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 22:55:31 2025
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

(cardIndex,) = mibBuilder.importSymbols(
    "OLD-CISCO-CHASSIS-MIB",
    "cardIndex")

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

ciscoCompressionServiceAdapterMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 57)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoCSAMIBObjects_ObjectIdentity = ObjectIdentity
ciscoCSAMIBObjects = _CiscoCSAMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 57, 1)
)
_CsaStats_ObjectIdentity = ObjectIdentity
csaStats = _CsaStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 57, 1, 1)
)
_CsaStatsTable_Object = MibTable
csaStatsTable = _CsaStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 57, 1, 1, 1)
)
if mibBuilder.loadTexts:
    csaStatsTable.setStatus("current")
_CsaStatsEntry_Object = MibTableRow
csaStatsEntry = _CsaStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 57, 1, 1, 1, 1)
)
csaStatsEntry.setIndexNames(
    (0, "OLD-CISCO-CHASSIS-MIB", "cardIndex"),
)
if mibBuilder.loadTexts:
    csaStatsEntry.setStatus("current")
_CsaInOctets_Type = Counter32
_CsaInOctets_Object = MibTableColumn
csaInOctets = _CsaInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 57, 1, 1, 1, 1, 1),
    _CsaInOctets_Type()
)
csaInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csaInOctets.setStatus("current")
_CsaOutOctets_Type = Counter32
_CsaOutOctets_Object = MibTableColumn
csaOutOctets = _CsaOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 57, 1, 1, 1, 1, 2),
    _CsaOutOctets_Type()
)
csaOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csaOutOctets.setStatus("current")
_CsaInPackets_Type = Counter32
_CsaInPackets_Object = MibTableColumn
csaInPackets = _CsaInPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 57, 1, 1, 1, 1, 3),
    _CsaInPackets_Type()
)
csaInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csaInPackets.setStatus("current")
_CsaOutPackets_Type = Counter32
_CsaOutPackets_Object = MibTableColumn
csaOutPackets = _CsaOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 57, 1, 1, 1, 1, 4),
    _CsaOutPackets_Type()
)
csaOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csaOutPackets.setStatus("current")
_CsaInPacketsDrop_Type = Counter32
_CsaInPacketsDrop_Object = MibTableColumn
csaInPacketsDrop = _CsaInPacketsDrop_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 57, 1, 1, 1, 1, 5),
    _CsaInPacketsDrop_Type()
)
csaInPacketsDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csaInPacketsDrop.setStatus("current")
_CsaOutPacketsDrop_Type = Counter32
_CsaOutPacketsDrop_Object = MibTableColumn
csaOutPacketsDrop = _CsaOutPacketsDrop_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 57, 1, 1, 1, 1, 6),
    _CsaOutPacketsDrop_Type()
)
csaOutPacketsDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csaOutPacketsDrop.setStatus("current")
_CsaNumberOfRestarts_Type = Counter32
_CsaNumberOfRestarts_Object = MibTableColumn
csaNumberOfRestarts = _CsaNumberOfRestarts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 57, 1, 1, 1, 1, 7),
    _CsaNumberOfRestarts_Type()
)
csaNumberOfRestarts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csaNumberOfRestarts.setStatus("current")


class _CsaCompressionRatio_Type(Gauge32):
    """Custom type csaCompressionRatio based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CsaCompressionRatio_Type.__name__ = "Gauge32"
_CsaCompressionRatio_Object = MibTableColumn
csaCompressionRatio = _CsaCompressionRatio_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 57, 1, 1, 1, 1, 8),
    _CsaCompressionRatio_Type()
)
csaCompressionRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csaCompressionRatio.setStatus("current")


class _CsaDecompressionRatio_Type(Gauge32):
    """Custom type csaDecompressionRatio based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CsaDecompressionRatio_Type.__name__ = "Gauge32"
_CsaDecompressionRatio_Object = MibTableColumn
csaDecompressionRatio = _CsaDecompressionRatio_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 57, 1, 1, 1, 1, 9),
    _CsaDecompressionRatio_Type()
)
csaDecompressionRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csaDecompressionRatio.setStatus("current")
_CsaEnable_Type = TruthValue
_CsaEnable_Object = MibTableColumn
csaEnable = _CsaEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 57, 1, 1, 1, 1, 10),
    _CsaEnable_Type()
)
csaEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csaEnable.setStatus("current")
_CiscoCSAMIBConformance_ObjectIdentity = ObjectIdentity
ciscoCSAMIBConformance = _CiscoCSAMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 57, 3)
)
_CsaMIBCompliances_ObjectIdentity = ObjectIdentity
csaMIBCompliances = _CsaMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 57, 3, 1)
)
_CsaMIBGroups_ObjectIdentity = ObjectIdentity
csaMIBGroups = _CsaMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 57, 3, 2)
)

# Managed Objects groups

csaMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 57, 3, 2, 1)
)
csaMIBGroup.setObjects(
      *(("CISCO-COMPRESSION-SERVICE-ADAPTER-MIB", "csaInOctets"),
        ("CISCO-COMPRESSION-SERVICE-ADAPTER-MIB", "csaOutOctets"),
        ("CISCO-COMPRESSION-SERVICE-ADAPTER-MIB", "csaInPackets"),
        ("CISCO-COMPRESSION-SERVICE-ADAPTER-MIB", "csaOutPackets"),
        ("CISCO-COMPRESSION-SERVICE-ADAPTER-MIB", "csaInPacketsDrop"),
        ("CISCO-COMPRESSION-SERVICE-ADAPTER-MIB", "csaOutPacketsDrop"),
        ("CISCO-COMPRESSION-SERVICE-ADAPTER-MIB", "csaNumberOfRestarts"),
        ("CISCO-COMPRESSION-SERVICE-ADAPTER-MIB", "csaCompressionRatio"),
        ("CISCO-COMPRESSION-SERVICE-ADAPTER-MIB", "csaDecompressionRatio"),
        ("CISCO-COMPRESSION-SERVICE-ADAPTER-MIB", "csaEnable"))
)
if mibBuilder.loadTexts:
    csaMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

csaMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 57, 3, 1, 1)
)
csaMIBCompliance.setObjects(
    ("CISCO-COMPRESSION-SERVICE-ADAPTER-MIB", "csaMIBGroup")
)
if mibBuilder.loadTexts:
    csaMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-COMPRESSION-SERVICE-ADAPTER-MIB",
    **{"ciscoCompressionServiceAdapterMIB": ciscoCompressionServiceAdapterMIB,
       "ciscoCSAMIBObjects": ciscoCSAMIBObjects,
       "csaStats": csaStats,
       "csaStatsTable": csaStatsTable,
       "csaStatsEntry": csaStatsEntry,
       "csaInOctets": csaInOctets,
       "csaOutOctets": csaOutOctets,
       "csaInPackets": csaInPackets,
       "csaOutPackets": csaOutPackets,
       "csaInPacketsDrop": csaInPacketsDrop,
       "csaOutPacketsDrop": csaOutPacketsDrop,
       "csaNumberOfRestarts": csaNumberOfRestarts,
       "csaCompressionRatio": csaCompressionRatio,
       "csaDecompressionRatio": csaDecompressionRatio,
       "csaEnable": csaEnable,
       "ciscoCSAMIBConformance": ciscoCSAMIBConformance,
       "csaMIBCompliances": csaMIBCompliances,
       "csaMIBCompliance": csaMIBCompliance,
       "csaMIBGroups": csaMIBGroups,
       "csaMIBGroup": csaMIBGroup}
)
