# SNMP MIB module (Ethernet-aggregation) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/exalt_25651/Ethernet-aggregation.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 16:22:49 2025
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

(locSysAlarms,
 radioConfig,
 remSysAlarms) = mibBuilder.importSymbols(
    "ExaltComProducts",
    "locSysAlarms",
    "radioConfig",
    "remSysAlarms")

(AlarmLevelT,
 EnableStatusT) = mibBuilder.importSymbols(
    "ExaltComm",
    "AlarmLevelT",
    "EnableStatusT")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdvSystemConfig_ObjectIdentity = ObjectIdentity
advSystemConfig = _AdvSystemConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5)
)
if mibBuilder.loadTexts:
    advSystemConfig.setStatus("current")
_EthernetAggregation_ObjectIdentity = ObjectIdentity
ethernetAggregation = _EthernetAggregation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 1)
)
if mibBuilder.loadTexts:
    ethernetAggregation.setStatus("current")
_Enable_Type = EnableStatusT
_Enable_Object = MibScalar
enable = _Enable_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 1, 1),
    _Enable_Type()
)
enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enable.setStatus("current")


class _Group_Type(Integer32):
    """Custom type group based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("east", 0),
          ("west", 1))
    )


_Group_Type.__name__ = "Integer32"
_Group_Object = MibScalar
group = _Group_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 1, 2),
    _Group_Type()
)
group.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    group.setStatus("current")
_NumOfRadioLinks_Type = Integer32
_NumOfRadioLinks_Object = MibScalar
numOfRadioLinks = _NumOfRadioLinks_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 1, 3),
    _NumOfRadioLinks_Type()
)
numOfRadioLinks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    numOfRadioLinks.setStatus("current")
_AggregatorId_Type = Integer32
_AggregatorId_Object = MibScalar
aggregatorId = _AggregatorId_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 1, 4),
    _AggregatorId_Type()
)
aggregatorId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aggregatorId.setStatus("current")
_AggregationThroughput_Object = MibTable
aggregationThroughput = _AggregationThroughput_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 1, 5)
)
if mibBuilder.loadTexts:
    aggregationThroughput.setStatus("current")
_AggregationThroughputEntry_Object = MibTableRow
aggregationThroughputEntry = _AggregationThroughputEntry_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 1, 5, 1)
)
aggregationThroughputEntry.setIndexNames(
    (0, "Ethernet-aggregation", "throughput"),
)
if mibBuilder.loadTexts:
    aggregationThroughputEntry.setStatus("current")
_Throughput_Type = Integer32
_Throughput_Object = MibTableColumn
throughput = _Throughput_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 1, 5, 1, 1),
    _Throughput_Type()
)
throughput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    throughput.setStatus("current")


class _CommitEthernetAggregationSettings_Type(DisplayString):
    """Custom type commitEthernetAggregationSettings based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 200),
    )


_CommitEthernetAggregationSettings_Type.__name__ = "DisplayString"
_CommitEthernetAggregationSettings_Object = MibScalar
commitEthernetAggregationSettings = _CommitEthernetAggregationSettings_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 1, 1000),
    _CommitEthernetAggregationSettings_Type()
)
commitEthernetAggregationSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commitEthernetAggregationSettings.setStatus("current")
_LocAggregationExpansionPortAlarm_Type = AlarmLevelT
_LocAggregationExpansionPortAlarm_Object = MibScalar
locAggregationExpansionPortAlarm = _LocAggregationExpansionPortAlarm_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 2, 3, 1, 12),
    _LocAggregationExpansionPortAlarm_Type()
)
locAggregationExpansionPortAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locAggregationExpansionPortAlarm.setStatus("current")
_RemAggregationExpansionPortAlarm_Type = AlarmLevelT
_RemAggregationExpansionPortAlarm_Object = MibScalar
remAggregationExpansionPortAlarm = _RemAggregationExpansionPortAlarm_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 2, 4, 1, 12),
    _RemAggregationExpansionPortAlarm_Type()
)
remAggregationExpansionPortAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remAggregationExpansionPortAlarm.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Ethernet-aggregation",
    **{"advSystemConfig": advSystemConfig,
       "ethernetAggregation": ethernetAggregation,
       "enable": enable,
       "group": group,
       "numOfRadioLinks": numOfRadioLinks,
       "aggregatorId": aggregatorId,
       "aggregationThroughput": aggregationThroughput,
       "aggregationThroughputEntry": aggregationThroughputEntry,
       "throughput": throughput,
       "commitEthernetAggregationSettings": commitEthernetAggregationSettings,
       "locAggregationExpansionPortAlarm": locAggregationExpansionPortAlarm,
       "remAggregationExpansionPortAlarm": remAggregationExpansionPortAlarm}
)
