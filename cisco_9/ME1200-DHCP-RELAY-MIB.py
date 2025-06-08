# SNMP MIB module (ME1200-DHCP-RELAY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/ME1200-DHCP-RELAY-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 09:05:30 2025
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

(me1200SwitchMgmt,) = mibBuilder.importSymbols(
    "CISCOME1200-MIB",
    "me1200SwitchMgmt")

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

me1200DhcpRelayMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 55)
)
if mibBuilder.loadTexts:
    me1200DhcpRelayMIB.setRevisions(
        ("2014-04-28 00:00",
         "2014-01-29 00:00",
         "2013-10-29 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ME1200DhcpRelayInformationPolicyType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("replace", 0),
          ("keep", 1),
          ("drop", 2))
    )



# MIB Managed Objects in the order of their OIDs

_Me1200DhcpRelayMIBObjects_ObjectIdentity = ObjectIdentity
me1200DhcpRelayMIBObjects = _Me1200DhcpRelayMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 55, 1)
)
_Me1200DhcpRelayConfig_ObjectIdentity = ObjectIdentity
me1200DhcpRelayConfig = _Me1200DhcpRelayConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 55, 1, 2)
)
_Me1200DhcpRelayGlobals_ObjectIdentity = ObjectIdentity
me1200DhcpRelayGlobals = _Me1200DhcpRelayGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 55, 1, 2, 1)
)
_Me1200DhcpRelayGlobalsMode_Type = TruthValue
_Me1200DhcpRelayGlobalsMode_Object = MibScalar
me1200DhcpRelayGlobalsMode = _Me1200DhcpRelayGlobalsMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 55, 1, 2, 1, 1),
    _Me1200DhcpRelayGlobalsMode_Type()
)
me1200DhcpRelayGlobalsMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpRelayGlobalsMode.setStatus("current")
_Me1200DhcpRelayGlobalsServerIpAddress_Type = IpAddress
_Me1200DhcpRelayGlobalsServerIpAddress_Object = MibScalar
me1200DhcpRelayGlobalsServerIpAddress = _Me1200DhcpRelayGlobalsServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 55, 1, 2, 1, 2),
    _Me1200DhcpRelayGlobalsServerIpAddress_Type()
)
me1200DhcpRelayGlobalsServerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpRelayGlobalsServerIpAddress.setStatus("current")
_Me1200DhcpRelayGlobalsInformationMode_Type = TruthValue
_Me1200DhcpRelayGlobalsInformationMode_Object = MibScalar
me1200DhcpRelayGlobalsInformationMode = _Me1200DhcpRelayGlobalsInformationMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 55, 1, 2, 1, 3),
    _Me1200DhcpRelayGlobalsInformationMode_Type()
)
me1200DhcpRelayGlobalsInformationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpRelayGlobalsInformationMode.setStatus("current")
_Me1200DhcpRelayGlobalsInformationPolicy_Type = ME1200DhcpRelayInformationPolicyType
_Me1200DhcpRelayGlobalsInformationPolicy_Object = MibScalar
me1200DhcpRelayGlobalsInformationPolicy = _Me1200DhcpRelayGlobalsInformationPolicy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 55, 1, 2, 1, 4),
    _Me1200DhcpRelayGlobalsInformationPolicy_Type()
)
me1200DhcpRelayGlobalsInformationPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpRelayGlobalsInformationPolicy.setStatus("current")
_Me1200DhcpRelayStatus_ObjectIdentity = ObjectIdentity
me1200DhcpRelayStatus = _Me1200DhcpRelayStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 55, 1, 3)
)
_Me1200DhcpRelayStatistics_ObjectIdentity = ObjectIdentity
me1200DhcpRelayStatistics = _Me1200DhcpRelayStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 55, 1, 3, 1)
)
_Me1200DhcpRelayStatisticsServerPacketsRelayed_Type = Unsigned32
_Me1200DhcpRelayStatisticsServerPacketsRelayed_Object = MibScalar
me1200DhcpRelayStatisticsServerPacketsRelayed = _Me1200DhcpRelayStatisticsServerPacketsRelayed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 55, 1, 3, 1, 1),
    _Me1200DhcpRelayStatisticsServerPacketsRelayed_Type()
)
me1200DhcpRelayStatisticsServerPacketsRelayed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DhcpRelayStatisticsServerPacketsRelayed.setStatus("current")
_Me1200DhcpRelayStatisticsServerPacketErrors_Type = Unsigned32
_Me1200DhcpRelayStatisticsServerPacketErrors_Object = MibScalar
me1200DhcpRelayStatisticsServerPacketErrors = _Me1200DhcpRelayStatisticsServerPacketErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 55, 1, 3, 1, 2),
    _Me1200DhcpRelayStatisticsServerPacketErrors_Type()
)
me1200DhcpRelayStatisticsServerPacketErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DhcpRelayStatisticsServerPacketErrors.setStatus("current")
_Me1200DhcpRelayStatisticsClientPacketsRelayed_Type = Unsigned32
_Me1200DhcpRelayStatisticsClientPacketsRelayed_Object = MibScalar
me1200DhcpRelayStatisticsClientPacketsRelayed = _Me1200DhcpRelayStatisticsClientPacketsRelayed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 55, 1, 3, 1, 3),
    _Me1200DhcpRelayStatisticsClientPacketsRelayed_Type()
)
me1200DhcpRelayStatisticsClientPacketsRelayed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DhcpRelayStatisticsClientPacketsRelayed.setStatus("current")
_Me1200DhcpRelayStatisticsClientPacketErrors_Type = Unsigned32
_Me1200DhcpRelayStatisticsClientPacketErrors_Object = MibScalar
me1200DhcpRelayStatisticsClientPacketErrors = _Me1200DhcpRelayStatisticsClientPacketErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 55, 1, 3, 1, 4),
    _Me1200DhcpRelayStatisticsClientPacketErrors_Type()
)
me1200DhcpRelayStatisticsClientPacketErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DhcpRelayStatisticsClientPacketErrors.setStatus("current")
_Me1200DhcpRelayStatisticsAgentOptionErrors_Type = Unsigned32
_Me1200DhcpRelayStatisticsAgentOptionErrors_Object = MibScalar
me1200DhcpRelayStatisticsAgentOptionErrors = _Me1200DhcpRelayStatisticsAgentOptionErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 55, 1, 3, 1, 5),
    _Me1200DhcpRelayStatisticsAgentOptionErrors_Type()
)
me1200DhcpRelayStatisticsAgentOptionErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DhcpRelayStatisticsAgentOptionErrors.setStatus("current")
_Me1200DhcpRelayStatisticsMissingAgentOption_Type = Unsigned32
_Me1200DhcpRelayStatisticsMissingAgentOption_Object = MibScalar
me1200DhcpRelayStatisticsMissingAgentOption = _Me1200DhcpRelayStatisticsMissingAgentOption_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 55, 1, 3, 1, 6),
    _Me1200DhcpRelayStatisticsMissingAgentOption_Type()
)
me1200DhcpRelayStatisticsMissingAgentOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DhcpRelayStatisticsMissingAgentOption.setStatus("current")
_Me1200DhcpRelayStatisticsBadCircuitId_Type = Unsigned32
_Me1200DhcpRelayStatisticsBadCircuitId_Object = MibScalar
me1200DhcpRelayStatisticsBadCircuitId = _Me1200DhcpRelayStatisticsBadCircuitId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 55, 1, 3, 1, 7),
    _Me1200DhcpRelayStatisticsBadCircuitId_Type()
)
me1200DhcpRelayStatisticsBadCircuitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DhcpRelayStatisticsBadCircuitId.setStatus("current")
_Me1200DhcpRelayStatisticsMissingCircuitId_Type = Unsigned32
_Me1200DhcpRelayStatisticsMissingCircuitId_Object = MibScalar
me1200DhcpRelayStatisticsMissingCircuitId = _Me1200DhcpRelayStatisticsMissingCircuitId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 55, 1, 3, 1, 8),
    _Me1200DhcpRelayStatisticsMissingCircuitId_Type()
)
me1200DhcpRelayStatisticsMissingCircuitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DhcpRelayStatisticsMissingCircuitId.setStatus("current")
_Me1200DhcpRelayStatisticsBadRemoteId_Type = Unsigned32
_Me1200DhcpRelayStatisticsBadRemoteId_Object = MibScalar
me1200DhcpRelayStatisticsBadRemoteId = _Me1200DhcpRelayStatisticsBadRemoteId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 55, 1, 3, 1, 9),
    _Me1200DhcpRelayStatisticsBadRemoteId_Type()
)
me1200DhcpRelayStatisticsBadRemoteId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DhcpRelayStatisticsBadRemoteId.setStatus("current")
_Me1200DhcpRelayStatisticsMissingRemoteId_Type = Unsigned32
_Me1200DhcpRelayStatisticsMissingRemoteId_Object = MibScalar
me1200DhcpRelayStatisticsMissingRemoteId = _Me1200DhcpRelayStatisticsMissingRemoteId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 55, 1, 3, 1, 10),
    _Me1200DhcpRelayStatisticsMissingRemoteId_Type()
)
me1200DhcpRelayStatisticsMissingRemoteId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DhcpRelayStatisticsMissingRemoteId.setStatus("current")
_Me1200DhcpRelayStatisticsReceiveServerPackets_Type = Unsigned32
_Me1200DhcpRelayStatisticsReceiveServerPackets_Object = MibScalar
me1200DhcpRelayStatisticsReceiveServerPackets = _Me1200DhcpRelayStatisticsReceiveServerPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 55, 1, 3, 1, 11),
    _Me1200DhcpRelayStatisticsReceiveServerPackets_Type()
)
me1200DhcpRelayStatisticsReceiveServerPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DhcpRelayStatisticsReceiveServerPackets.setStatus("current")
_Me1200DhcpRelayStatisticsReceiveClientPackets_Type = Unsigned32
_Me1200DhcpRelayStatisticsReceiveClientPackets_Object = MibScalar
me1200DhcpRelayStatisticsReceiveClientPackets = _Me1200DhcpRelayStatisticsReceiveClientPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 55, 1, 3, 1, 12),
    _Me1200DhcpRelayStatisticsReceiveClientPackets_Type()
)
me1200DhcpRelayStatisticsReceiveClientPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DhcpRelayStatisticsReceiveClientPackets.setStatus("current")
_Me1200DhcpRelayStatisticsReceiveClientAgentOption_Type = Unsigned32
_Me1200DhcpRelayStatisticsReceiveClientAgentOption_Object = MibScalar
me1200DhcpRelayStatisticsReceiveClientAgentOption = _Me1200DhcpRelayStatisticsReceiveClientAgentOption_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 55, 1, 3, 1, 13),
    _Me1200DhcpRelayStatisticsReceiveClientAgentOption_Type()
)
me1200DhcpRelayStatisticsReceiveClientAgentOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DhcpRelayStatisticsReceiveClientAgentOption.setStatus("current")
_Me1200DhcpRelayStatisticsReplaceAgentOption_Type = Unsigned32
_Me1200DhcpRelayStatisticsReplaceAgentOption_Object = MibScalar
me1200DhcpRelayStatisticsReplaceAgentOption = _Me1200DhcpRelayStatisticsReplaceAgentOption_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 55, 1, 3, 1, 14),
    _Me1200DhcpRelayStatisticsReplaceAgentOption_Type()
)
me1200DhcpRelayStatisticsReplaceAgentOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DhcpRelayStatisticsReplaceAgentOption.setStatus("current")
_Me1200DhcpRelayStatisticsKeepAgentOption_Type = Unsigned32
_Me1200DhcpRelayStatisticsKeepAgentOption_Object = MibScalar
me1200DhcpRelayStatisticsKeepAgentOption = _Me1200DhcpRelayStatisticsKeepAgentOption_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 55, 1, 3, 1, 15),
    _Me1200DhcpRelayStatisticsKeepAgentOption_Type()
)
me1200DhcpRelayStatisticsKeepAgentOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DhcpRelayStatisticsKeepAgentOption.setStatus("current")
_Me1200DhcpRelayStatisticsDropAgentOption_Type = Unsigned32
_Me1200DhcpRelayStatisticsDropAgentOption_Object = MibScalar
me1200DhcpRelayStatisticsDropAgentOption = _Me1200DhcpRelayStatisticsDropAgentOption_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 55, 1, 3, 1, 16),
    _Me1200DhcpRelayStatisticsDropAgentOption_Type()
)
me1200DhcpRelayStatisticsDropAgentOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DhcpRelayStatisticsDropAgentOption.setStatus("current")
_Me1200DhcpRelayControl_ObjectIdentity = ObjectIdentity
me1200DhcpRelayControl = _Me1200DhcpRelayControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 55, 1, 4)
)
_Me1200DhcpRelayControlClearStatistics_Type = TruthValue
_Me1200DhcpRelayControlClearStatistics_Object = MibScalar
me1200DhcpRelayControlClearStatistics = _Me1200DhcpRelayControlClearStatistics_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 55, 1, 4, 1),
    _Me1200DhcpRelayControlClearStatistics_Type()
)
me1200DhcpRelayControlClearStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DhcpRelayControlClearStatistics.setStatus("current")
_Me1200DhcpRelayMIBConformance_ObjectIdentity = ObjectIdentity
me1200DhcpRelayMIBConformance = _Me1200DhcpRelayMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 55, 2)
)
_Me1200DhcpRelayMIBCompliances_ObjectIdentity = ObjectIdentity
me1200DhcpRelayMIBCompliances = _Me1200DhcpRelayMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 55, 2, 1)
)
_Me1200DhcpRelayMIBGroups_ObjectIdentity = ObjectIdentity
me1200DhcpRelayMIBGroups = _Me1200DhcpRelayMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 55, 2, 2)
)

# Managed Objects groups

me1200DhcpRelayGlobalsInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 55, 2, 2, 1)
)
me1200DhcpRelayGlobalsInfoGroup.setObjects(
      *(("ME1200-DHCP-RELAY-MIB", "me1200DhcpRelayGlobalsMode"),
        ("ME1200-DHCP-RELAY-MIB", "me1200DhcpRelayGlobalsServerIpAddress"),
        ("ME1200-DHCP-RELAY-MIB", "me1200DhcpRelayGlobalsInformationMode"),
        ("ME1200-DHCP-RELAY-MIB", "me1200DhcpRelayGlobalsInformationPolicy"))
)
if mibBuilder.loadTexts:
    me1200DhcpRelayGlobalsInfoGroup.setStatus("current")

me1200DhcpRelayStatisticsInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 55, 2, 2, 2)
)
me1200DhcpRelayStatisticsInfoGroup.setObjects(
      *(("ME1200-DHCP-RELAY-MIB", "me1200DhcpRelayStatisticsServerPacketsRelayed"),
        ("ME1200-DHCP-RELAY-MIB", "me1200DhcpRelayStatisticsServerPacketErrors"),
        ("ME1200-DHCP-RELAY-MIB", "me1200DhcpRelayStatisticsClientPacketsRelayed"),
        ("ME1200-DHCP-RELAY-MIB", "me1200DhcpRelayStatisticsClientPacketErrors"),
        ("ME1200-DHCP-RELAY-MIB", "me1200DhcpRelayStatisticsAgentOptionErrors"),
        ("ME1200-DHCP-RELAY-MIB", "me1200DhcpRelayStatisticsMissingAgentOption"),
        ("ME1200-DHCP-RELAY-MIB", "me1200DhcpRelayStatisticsBadCircuitId"),
        ("ME1200-DHCP-RELAY-MIB", "me1200DhcpRelayStatisticsMissingCircuitId"),
        ("ME1200-DHCP-RELAY-MIB", "me1200DhcpRelayStatisticsBadRemoteId"),
        ("ME1200-DHCP-RELAY-MIB", "me1200DhcpRelayStatisticsMissingRemoteId"),
        ("ME1200-DHCP-RELAY-MIB", "me1200DhcpRelayStatisticsReceiveServerPackets"),
        ("ME1200-DHCP-RELAY-MIB", "me1200DhcpRelayStatisticsReceiveClientPackets"),
        ("ME1200-DHCP-RELAY-MIB", "me1200DhcpRelayStatisticsReceiveClientAgentOption"),
        ("ME1200-DHCP-RELAY-MIB", "me1200DhcpRelayStatisticsReplaceAgentOption"),
        ("ME1200-DHCP-RELAY-MIB", "me1200DhcpRelayStatisticsKeepAgentOption"),
        ("ME1200-DHCP-RELAY-MIB", "me1200DhcpRelayStatisticsDropAgentOption"))
)
if mibBuilder.loadTexts:
    me1200DhcpRelayStatisticsInfoGroup.setStatus("current")

me1200DhcpRelayControlInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 55, 2, 2, 3)
)
me1200DhcpRelayControlInfoGroup.setObjects(
    ("ME1200-DHCP-RELAY-MIB", "me1200DhcpRelayControlClearStatistics")
)
if mibBuilder.loadTexts:
    me1200DhcpRelayControlInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

me1200DhcpRelayMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 55, 2, 1, 1)
)
me1200DhcpRelayMIBCompliance.setObjects(
      *(("ME1200-DHCP-RELAY-MIB", "me1200DhcpRelayGlobalsInfoGroup"),
        ("ME1200-DHCP-RELAY-MIB", "me1200DhcpRelayStatisticsInfoGroup"),
        ("ME1200-DHCP-RELAY-MIB", "me1200DhcpRelayControlInfoGroup"))
)
if mibBuilder.loadTexts:
    me1200DhcpRelayMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ME1200-DHCP-RELAY-MIB",
    **{"ME1200DhcpRelayInformationPolicyType": ME1200DhcpRelayInformationPolicyType,
       "me1200DhcpRelayMIB": me1200DhcpRelayMIB,
       "me1200DhcpRelayMIBObjects": me1200DhcpRelayMIBObjects,
       "me1200DhcpRelayConfig": me1200DhcpRelayConfig,
       "me1200DhcpRelayGlobals": me1200DhcpRelayGlobals,
       "me1200DhcpRelayGlobalsMode": me1200DhcpRelayGlobalsMode,
       "me1200DhcpRelayGlobalsServerIpAddress": me1200DhcpRelayGlobalsServerIpAddress,
       "me1200DhcpRelayGlobalsInformationMode": me1200DhcpRelayGlobalsInformationMode,
       "me1200DhcpRelayGlobalsInformationPolicy": me1200DhcpRelayGlobalsInformationPolicy,
       "me1200DhcpRelayStatus": me1200DhcpRelayStatus,
       "me1200DhcpRelayStatistics": me1200DhcpRelayStatistics,
       "me1200DhcpRelayStatisticsServerPacketsRelayed": me1200DhcpRelayStatisticsServerPacketsRelayed,
       "me1200DhcpRelayStatisticsServerPacketErrors": me1200DhcpRelayStatisticsServerPacketErrors,
       "me1200DhcpRelayStatisticsClientPacketsRelayed": me1200DhcpRelayStatisticsClientPacketsRelayed,
       "me1200DhcpRelayStatisticsClientPacketErrors": me1200DhcpRelayStatisticsClientPacketErrors,
       "me1200DhcpRelayStatisticsAgentOptionErrors": me1200DhcpRelayStatisticsAgentOptionErrors,
       "me1200DhcpRelayStatisticsMissingAgentOption": me1200DhcpRelayStatisticsMissingAgentOption,
       "me1200DhcpRelayStatisticsBadCircuitId": me1200DhcpRelayStatisticsBadCircuitId,
       "me1200DhcpRelayStatisticsMissingCircuitId": me1200DhcpRelayStatisticsMissingCircuitId,
       "me1200DhcpRelayStatisticsBadRemoteId": me1200DhcpRelayStatisticsBadRemoteId,
       "me1200DhcpRelayStatisticsMissingRemoteId": me1200DhcpRelayStatisticsMissingRemoteId,
       "me1200DhcpRelayStatisticsReceiveServerPackets": me1200DhcpRelayStatisticsReceiveServerPackets,
       "me1200DhcpRelayStatisticsReceiveClientPackets": me1200DhcpRelayStatisticsReceiveClientPackets,
       "me1200DhcpRelayStatisticsReceiveClientAgentOption": me1200DhcpRelayStatisticsReceiveClientAgentOption,
       "me1200DhcpRelayStatisticsReplaceAgentOption": me1200DhcpRelayStatisticsReplaceAgentOption,
       "me1200DhcpRelayStatisticsKeepAgentOption": me1200DhcpRelayStatisticsKeepAgentOption,
       "me1200DhcpRelayStatisticsDropAgentOption": me1200DhcpRelayStatisticsDropAgentOption,
       "me1200DhcpRelayControl": me1200DhcpRelayControl,
       "me1200DhcpRelayControlClearStatistics": me1200DhcpRelayControlClearStatistics,
       "me1200DhcpRelayMIBConformance": me1200DhcpRelayMIBConformance,
       "me1200DhcpRelayMIBCompliances": me1200DhcpRelayMIBCompliances,
       "me1200DhcpRelayMIBCompliance": me1200DhcpRelayMIBCompliance,
       "me1200DhcpRelayMIBGroups": me1200DhcpRelayMIBGroups,
       "me1200DhcpRelayGlobalsInfoGroup": me1200DhcpRelayGlobalsInfoGroup,
       "me1200DhcpRelayStatisticsInfoGroup": me1200DhcpRelayStatisticsInfoGroup,
       "me1200DhcpRelayControlInfoGroup": me1200DhcpRelayControlInfoGroup}
)
