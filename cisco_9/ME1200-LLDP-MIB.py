# SNMP MIB module (ME1200-LLDP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/ME1200-LLDP-MIB.mib
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

(ME1200DisplayString,
 ME1200InterfaceIndex,
 ME1200Unsigned16,
 ME1200Unsigned64,
 ME1200Unsigned8) = mibBuilder.importSymbols(
    "ME1200-TC",
    "ME1200DisplayString",
    "ME1200InterfaceIndex",
    "ME1200Unsigned16",
    "ME1200Unsigned64",
    "ME1200Unsigned8")

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

me1200LldpMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 34)
)
if mibBuilder.loadTexts:
    me1200LldpMib.setRevisions(
        ("2014-03-11 00:00",
         "2014-02-18 00:00",
         "2014-01-29 00:00",
         "2013-10-08 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ME1200lldpAdminState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("txAndRx", 1),
          ("txOnly", 2),
          ("rxOnly", 3))
    )



# MIB Managed Objects in the order of their OIDs

_Me1200LldpObjects_ObjectIdentity = ObjectIdentity
me1200LldpObjects = _Me1200LldpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 34, 1)
)
_Me1200LldpConfig_ObjectIdentity = ObjectIdentity
me1200LldpConfig = _Me1200LldpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 34, 1, 2)
)
_Me1200LldpGlobal_ObjectIdentity = ObjectIdentity
me1200LldpGlobal = _Me1200LldpGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 34, 1, 2, 1)
)
_Me1200LldpGlobalInitDelay_Type = ME1200Unsigned16
_Me1200LldpGlobalInitDelay_Object = MibScalar
me1200LldpGlobalInitDelay = _Me1200LldpGlobalInitDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 34, 1, 2, 1, 1),
    _Me1200LldpGlobalInitDelay_Type()
)
me1200LldpGlobalInitDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200LldpGlobalInitDelay.setStatus("current")
_Me1200LldpGlobalMsgTxHold_Type = ME1200Unsigned16
_Me1200LldpGlobalMsgTxHold_Object = MibScalar
me1200LldpGlobalMsgTxHold = _Me1200LldpGlobalMsgTxHold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 34, 1, 2, 1, 2),
    _Me1200LldpGlobalMsgTxHold_Type()
)
me1200LldpGlobalMsgTxHold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200LldpGlobalMsgTxHold.setStatus("current")
_Me1200LldpGlobalMsgTxInterval_Type = ME1200Unsigned16
_Me1200LldpGlobalMsgTxInterval_Object = MibScalar
me1200LldpGlobalMsgTxInterval = _Me1200LldpGlobalMsgTxInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 34, 1, 2, 1, 3),
    _Me1200LldpGlobalMsgTxInterval_Type()
)
me1200LldpGlobalMsgTxInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200LldpGlobalMsgTxInterval.setStatus("current")
_Me1200LldpGlobalTxDelay_Type = ME1200Unsigned16
_Me1200LldpGlobalTxDelay_Object = MibScalar
me1200LldpGlobalTxDelay = _Me1200LldpGlobalTxDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 34, 1, 2, 1, 4),
    _Me1200LldpGlobalTxDelay_Type()
)
me1200LldpGlobalTxDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200LldpGlobalTxDelay.setStatus("current")
_Me1200LldpConfigurationTable_Object = MibTable
me1200LldpConfigurationTable = _Me1200LldpConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 34, 1, 2, 2)
)
if mibBuilder.loadTexts:
    me1200LldpConfigurationTable.setStatus("current")
_Me1200LldpConfigurationEntry_Object = MibTableRow
me1200LldpConfigurationEntry = _Me1200LldpConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 34, 1, 2, 2, 1)
)
me1200LldpConfigurationEntry.setIndexNames(
    (0, "ME1200-LLDP-MIB", "me1200LldpConfigurationIfIndex"),
)
if mibBuilder.loadTexts:
    me1200LldpConfigurationEntry.setStatus("current")
_Me1200LldpConfigurationIfIndex_Type = ME1200InterfaceIndex
_Me1200LldpConfigurationIfIndex_Object = MibTableColumn
me1200LldpConfigurationIfIndex = _Me1200LldpConfigurationIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 34, 1, 2, 2, 1, 1),
    _Me1200LldpConfigurationIfIndex_Type()
)
me1200LldpConfigurationIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200LldpConfigurationIfIndex.setStatus("current")
_Me1200LldpConfigurationAdminState_Type = ME1200lldpAdminState
_Me1200LldpConfigurationAdminState_Object = MibTableColumn
me1200LldpConfigurationAdminState = _Me1200LldpConfigurationAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 34, 1, 2, 2, 1, 3),
    _Me1200LldpConfigurationAdminState_Type()
)
me1200LldpConfigurationAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200LldpConfigurationAdminState.setStatus("current")
_Me1200LldpConfigurationCdpAware_Type = TruthValue
_Me1200LldpConfigurationCdpAware_Object = MibTableColumn
me1200LldpConfigurationCdpAware = _Me1200LldpConfigurationCdpAware_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 34, 1, 2, 2, 1, 4),
    _Me1200LldpConfigurationCdpAware_Type()
)
me1200LldpConfigurationCdpAware.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200LldpConfigurationCdpAware.setStatus("current")


class _Me1200LldpConfigurationOptionalTlvs_Type(ME1200Unsigned8):
    """Custom type me1200LldpConfigurationOptionalTlvs based on ME1200Unsigned8"""
    subtypeSpec = ME1200Unsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_Me1200LldpConfigurationOptionalTlvs_Type.__name__ = "ME1200Unsigned8"
_Me1200LldpConfigurationOptionalTlvs_Object = MibTableColumn
me1200LldpConfigurationOptionalTlvs = _Me1200LldpConfigurationOptionalTlvs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 34, 1, 2, 2, 1, 5),
    _Me1200LldpConfigurationOptionalTlvs_Type()
)
me1200LldpConfigurationOptionalTlvs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200LldpConfigurationOptionalTlvs.setStatus("current")
_Me1200LldpStatus_ObjectIdentity = ObjectIdentity
me1200LldpStatus = _Me1200LldpStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 34, 1, 3)
)
_Me1200LldpStatistics_ObjectIdentity = ObjectIdentity
me1200LldpStatistics = _Me1200LldpStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 34, 1, 3, 2)
)
_Me1200LldpStatisticsGlobalCounters_ObjectIdentity = ObjectIdentity
me1200LldpStatisticsGlobalCounters = _Me1200LldpStatisticsGlobalCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 34, 1, 3, 2, 1)
)
_Me1200LldpStatisticsGlobalCountersTableInserts_Type = Unsigned32
_Me1200LldpStatisticsGlobalCountersTableInserts_Object = MibScalar
me1200LldpStatisticsGlobalCountersTableInserts = _Me1200LldpStatisticsGlobalCountersTableInserts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 34, 1, 3, 2, 1, 1),
    _Me1200LldpStatisticsGlobalCountersTableInserts_Type()
)
me1200LldpStatisticsGlobalCountersTableInserts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200LldpStatisticsGlobalCountersTableInserts.setStatus("current")
_Me1200LldpStatisticsGlobalCountersTableDeletes_Type = Unsigned32
_Me1200LldpStatisticsGlobalCountersTableDeletes_Object = MibScalar
me1200LldpStatisticsGlobalCountersTableDeletes = _Me1200LldpStatisticsGlobalCountersTableDeletes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 34, 1, 3, 2, 1, 2),
    _Me1200LldpStatisticsGlobalCountersTableDeletes_Type()
)
me1200LldpStatisticsGlobalCountersTableDeletes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200LldpStatisticsGlobalCountersTableDeletes.setStatus("current")
_Me1200LldpStatisticsGlobalCountersTableDrops_Type = Unsigned32
_Me1200LldpStatisticsGlobalCountersTableDrops_Object = MibScalar
me1200LldpStatisticsGlobalCountersTableDrops = _Me1200LldpStatisticsGlobalCountersTableDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 34, 1, 3, 2, 1, 3),
    _Me1200LldpStatisticsGlobalCountersTableDrops_Type()
)
me1200LldpStatisticsGlobalCountersTableDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200LldpStatisticsGlobalCountersTableDrops.setStatus("current")
_Me1200LldpStatisticsGlobalCountersTableAgeOuts_Type = Unsigned32
_Me1200LldpStatisticsGlobalCountersTableAgeOuts_Object = MibScalar
me1200LldpStatisticsGlobalCountersTableAgeOuts = _Me1200LldpStatisticsGlobalCountersTableAgeOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 34, 1, 3, 2, 1, 4),
    _Me1200LldpStatisticsGlobalCountersTableAgeOuts_Type()
)
me1200LldpStatisticsGlobalCountersTableAgeOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200LldpStatisticsGlobalCountersTableAgeOuts.setStatus("current")
_Me1200LldpStatisticsGlobalCountersLastChangeTime_Type = ME1200Unsigned64
_Me1200LldpStatisticsGlobalCountersLastChangeTime_Object = MibScalar
me1200LldpStatisticsGlobalCountersLastChangeTime = _Me1200LldpStatisticsGlobalCountersLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 34, 1, 3, 2, 1, 5),
    _Me1200LldpStatisticsGlobalCountersLastChangeTime_Type()
)
me1200LldpStatisticsGlobalCountersLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200LldpStatisticsGlobalCountersLastChangeTime.setStatus("current")
_Me1200LldpStatisticsTable_Object = MibTable
me1200LldpStatisticsTable = _Me1200LldpStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 34, 1, 3, 2, 2)
)
if mibBuilder.loadTexts:
    me1200LldpStatisticsTable.setStatus("current")
_Me1200LldpStatisticsEntry_Object = MibTableRow
me1200LldpStatisticsEntry = _Me1200LldpStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 34, 1, 3, 2, 2, 1)
)
me1200LldpStatisticsEntry.setIndexNames(
    (0, "ME1200-LLDP-MIB", "me1200LldpStatisticsIfIndex"),
)
if mibBuilder.loadTexts:
    me1200LldpStatisticsEntry.setStatus("current")
_Me1200LldpStatisticsIfIndex_Type = ME1200InterfaceIndex
_Me1200LldpStatisticsIfIndex_Object = MibTableColumn
me1200LldpStatisticsIfIndex = _Me1200LldpStatisticsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 34, 1, 3, 2, 2, 1, 1),
    _Me1200LldpStatisticsIfIndex_Type()
)
me1200LldpStatisticsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200LldpStatisticsIfIndex.setStatus("current")
_Me1200LldpStatisticsTxTotal_Type = Unsigned32
_Me1200LldpStatisticsTxTotal_Object = MibTableColumn
me1200LldpStatisticsTxTotal = _Me1200LldpStatisticsTxTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 34, 1, 3, 2, 2, 1, 2),
    _Me1200LldpStatisticsTxTotal_Type()
)
me1200LldpStatisticsTxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200LldpStatisticsTxTotal.setStatus("current")
_Me1200LldpStatisticsRxTotal_Type = Unsigned32
_Me1200LldpStatisticsRxTotal_Object = MibTableColumn
me1200LldpStatisticsRxTotal = _Me1200LldpStatisticsRxTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 34, 1, 3, 2, 2, 1, 3),
    _Me1200LldpStatisticsRxTotal_Type()
)
me1200LldpStatisticsRxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200LldpStatisticsRxTotal.setStatus("current")
_Me1200LldpStatisticsRxError_Type = Unsigned32
_Me1200LldpStatisticsRxError_Object = MibTableColumn
me1200LldpStatisticsRxError = _Me1200LldpStatisticsRxError_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 34, 1, 3, 2, 2, 1, 4),
    _Me1200LldpStatisticsRxError_Type()
)
me1200LldpStatisticsRxError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200LldpStatisticsRxError.setStatus("current")
_Me1200LldpStatisticsRxDiscarded_Type = Unsigned32
_Me1200LldpStatisticsRxDiscarded_Object = MibTableColumn
me1200LldpStatisticsRxDiscarded = _Me1200LldpStatisticsRxDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 34, 1, 3, 2, 2, 1, 5),
    _Me1200LldpStatisticsRxDiscarded_Type()
)
me1200LldpStatisticsRxDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200LldpStatisticsRxDiscarded.setStatus("current")
_Me1200LldpStatisticsTLVsDiscarded_Type = Unsigned32
_Me1200LldpStatisticsTLVsDiscarded_Object = MibTableColumn
me1200LldpStatisticsTLVsDiscarded = _Me1200LldpStatisticsTLVsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 34, 1, 3, 2, 2, 1, 6),
    _Me1200LldpStatisticsTLVsDiscarded_Type()
)
me1200LldpStatisticsTLVsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200LldpStatisticsTLVsDiscarded.setStatus("current")
_Me1200LldpStatisticsTLVsUnrecognized_Type = Unsigned32
_Me1200LldpStatisticsTLVsUnrecognized_Object = MibTableColumn
me1200LldpStatisticsTLVsUnrecognized = _Me1200LldpStatisticsTLVsUnrecognized_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 34, 1, 3, 2, 2, 1, 7),
    _Me1200LldpStatisticsTLVsUnrecognized_Type()
)
me1200LldpStatisticsTLVsUnrecognized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200LldpStatisticsTLVsUnrecognized.setStatus("current")
_Me1200LldpStatisticsTLVsOrgDiscarded_Type = Unsigned32
_Me1200LldpStatisticsTLVsOrgDiscarded_Object = MibTableColumn
me1200LldpStatisticsTLVsOrgDiscarded = _Me1200LldpStatisticsTLVsOrgDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 34, 1, 3, 2, 2, 1, 8),
    _Me1200LldpStatisticsTLVsOrgDiscarded_Type()
)
me1200LldpStatisticsTLVsOrgDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200LldpStatisticsTLVsOrgDiscarded.setStatus("current")
_Me1200LldpStatisticsAgeOuts_Type = Unsigned32
_Me1200LldpStatisticsAgeOuts_Object = MibTableColumn
me1200LldpStatisticsAgeOuts = _Me1200LldpStatisticsAgeOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 34, 1, 3, 2, 2, 1, 9),
    _Me1200LldpStatisticsAgeOuts_Type()
)
me1200LldpStatisticsAgeOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200LldpStatisticsAgeOuts.setStatus("current")
_Me1200LldpNeighborsInformationTable_Object = MibTable
me1200LldpNeighborsInformationTable = _Me1200LldpNeighborsInformationTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 34, 1, 3, 3)
)
if mibBuilder.loadTexts:
    me1200LldpNeighborsInformationTable.setStatus("current")
_Me1200LldpNeighborsInformationEntry_Object = MibTableRow
me1200LldpNeighborsInformationEntry = _Me1200LldpNeighborsInformationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 34, 1, 3, 3, 1)
)
me1200LldpNeighborsInformationEntry.setIndexNames(
    (0, "ME1200-LLDP-MIB", "me1200LldpNeighborsInformationIfIndex"),
    (0, "ME1200-LLDP-MIB", "me1200LldpNeighborsInformationLldpIndex"),
)
if mibBuilder.loadTexts:
    me1200LldpNeighborsInformationEntry.setStatus("current")
_Me1200LldpNeighborsInformationIfIndex_Type = ME1200InterfaceIndex
_Me1200LldpNeighborsInformationIfIndex_Object = MibTableColumn
me1200LldpNeighborsInformationIfIndex = _Me1200LldpNeighborsInformationIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 34, 1, 3, 3, 1, 1),
    _Me1200LldpNeighborsInformationIfIndex_Type()
)
me1200LldpNeighborsInformationIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200LldpNeighborsInformationIfIndex.setStatus("current")


class _Me1200LldpNeighborsInformationLldpIndex_Type(Integer32):
    """Custom type me1200LldpNeighborsInformationLldpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 192),
    )


_Me1200LldpNeighborsInformationLldpIndex_Type.__name__ = "Integer32"
_Me1200LldpNeighborsInformationLldpIndex_Object = MibTableColumn
me1200LldpNeighborsInformationLldpIndex = _Me1200LldpNeighborsInformationLldpIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 34, 1, 3, 3, 1, 2),
    _Me1200LldpNeighborsInformationLldpIndex_Type()
)
me1200LldpNeighborsInformationLldpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200LldpNeighborsInformationLldpIndex.setStatus("current")


class _Me1200LldpNeighborsInformationChassisId_Type(ME1200DisplayString):
    """Custom type me1200LldpNeighborsInformationChassisId based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_Me1200LldpNeighborsInformationChassisId_Type.__name__ = "ME1200DisplayString"
_Me1200LldpNeighborsInformationChassisId_Object = MibTableColumn
me1200LldpNeighborsInformationChassisId = _Me1200LldpNeighborsInformationChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 34, 1, 3, 3, 1, 4),
    _Me1200LldpNeighborsInformationChassisId_Type()
)
me1200LldpNeighborsInformationChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200LldpNeighborsInformationChassisId.setStatus("current")


class _Me1200LldpNeighborsInformationPortId_Type(ME1200DisplayString):
    """Custom type me1200LldpNeighborsInformationPortId based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_Me1200LldpNeighborsInformationPortId_Type.__name__ = "ME1200DisplayString"
_Me1200LldpNeighborsInformationPortId_Object = MibTableColumn
me1200LldpNeighborsInformationPortId = _Me1200LldpNeighborsInformationPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 34, 1, 3, 3, 1, 5),
    _Me1200LldpNeighborsInformationPortId_Type()
)
me1200LldpNeighborsInformationPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200LldpNeighborsInformationPortId.setStatus("current")


class _Me1200LldpNeighborsInformationPortDescription_Type(ME1200DisplayString):
    """Custom type me1200LldpNeighborsInformationPortDescription based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_Me1200LldpNeighborsInformationPortDescription_Type.__name__ = "ME1200DisplayString"
_Me1200LldpNeighborsInformationPortDescription_Object = MibTableColumn
me1200LldpNeighborsInformationPortDescription = _Me1200LldpNeighborsInformationPortDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 34, 1, 3, 3, 1, 6),
    _Me1200LldpNeighborsInformationPortDescription_Type()
)
me1200LldpNeighborsInformationPortDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200LldpNeighborsInformationPortDescription.setStatus("current")


class _Me1200LldpNeighborsInformationSystemName_Type(ME1200DisplayString):
    """Custom type me1200LldpNeighborsInformationSystemName based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_Me1200LldpNeighborsInformationSystemName_Type.__name__ = "ME1200DisplayString"
_Me1200LldpNeighborsInformationSystemName_Object = MibTableColumn
me1200LldpNeighborsInformationSystemName = _Me1200LldpNeighborsInformationSystemName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 34, 1, 3, 3, 1, 7),
    _Me1200LldpNeighborsInformationSystemName_Type()
)
me1200LldpNeighborsInformationSystemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200LldpNeighborsInformationSystemName.setStatus("current")


class _Me1200LldpNeighborsInformationSystemDescription_Type(ME1200DisplayString):
    """Custom type me1200LldpNeighborsInformationSystemDescription based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_Me1200LldpNeighborsInformationSystemDescription_Type.__name__ = "ME1200DisplayString"
_Me1200LldpNeighborsInformationSystemDescription_Object = MibTableColumn
me1200LldpNeighborsInformationSystemDescription = _Me1200LldpNeighborsInformationSystemDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 34, 1, 3, 3, 1, 8),
    _Me1200LldpNeighborsInformationSystemDescription_Type()
)
me1200LldpNeighborsInformationSystemDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200LldpNeighborsInformationSystemDescription.setStatus("current")
_Me1200LldpNeighborsInformationSystemCapabilities_Type = ME1200Unsigned16
_Me1200LldpNeighborsInformationSystemCapabilities_Object = MibTableColumn
me1200LldpNeighborsInformationSystemCapabilities = _Me1200LldpNeighborsInformationSystemCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 34, 1, 3, 3, 1, 9),
    _Me1200LldpNeighborsInformationSystemCapabilities_Type()
)
me1200LldpNeighborsInformationSystemCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200LldpNeighborsInformationSystemCapabilities.setStatus("current")
_Me1200LldpNeighborsInformationSystemCapabilitiesEnable_Type = ME1200Unsigned16
_Me1200LldpNeighborsInformationSystemCapabilitiesEnable_Object = MibTableColumn
me1200LldpNeighborsInformationSystemCapabilitiesEnable = _Me1200LldpNeighborsInformationSystemCapabilitiesEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 34, 1, 3, 3, 1, 10),
    _Me1200LldpNeighborsInformationSystemCapabilitiesEnable_Type()
)
me1200LldpNeighborsInformationSystemCapabilitiesEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200LldpNeighborsInformationSystemCapabilitiesEnable.setStatus("current")
_Me1200LldpNeighborsManagementInformationTable_Object = MibTable
me1200LldpNeighborsManagementInformationTable = _Me1200LldpNeighborsManagementInformationTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 34, 1, 3, 4)
)
if mibBuilder.loadTexts:
    me1200LldpNeighborsManagementInformationTable.setStatus("current")
_Me1200LldpNeighborsManagementInformationEntry_Object = MibTableRow
me1200LldpNeighborsManagementInformationEntry = _Me1200LldpNeighborsManagementInformationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 34, 1, 3, 4, 1)
)
me1200LldpNeighborsManagementInformationEntry.setIndexNames(
    (0, "ME1200-LLDP-MIB", "me1200LldpNeighborsManagementInformationIfIndex"),
    (0, "ME1200-LLDP-MIB", "me1200LldpNeighborsManagementInformationLldpIndex"),
    (0, "ME1200-LLDP-MIB", "me1200LldpNeighborsManagementInformationLldpManagement"),
)
if mibBuilder.loadTexts:
    me1200LldpNeighborsManagementInformationEntry.setStatus("current")
_Me1200LldpNeighborsManagementInformationIfIndex_Type = ME1200InterfaceIndex
_Me1200LldpNeighborsManagementInformationIfIndex_Object = MibTableColumn
me1200LldpNeighborsManagementInformationIfIndex = _Me1200LldpNeighborsManagementInformationIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 34, 1, 3, 4, 1, 1),
    _Me1200LldpNeighborsManagementInformationIfIndex_Type()
)
me1200LldpNeighborsManagementInformationIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200LldpNeighborsManagementInformationIfIndex.setStatus("current")


class _Me1200LldpNeighborsManagementInformationLldpIndex_Type(Integer32):
    """Custom type me1200LldpNeighborsManagementInformationLldpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 192),
    )


_Me1200LldpNeighborsManagementInformationLldpIndex_Type.__name__ = "Integer32"
_Me1200LldpNeighborsManagementInformationLldpIndex_Object = MibTableColumn
me1200LldpNeighborsManagementInformationLldpIndex = _Me1200LldpNeighborsManagementInformationLldpIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 34, 1, 3, 4, 1, 2),
    _Me1200LldpNeighborsManagementInformationLldpIndex_Type()
)
me1200LldpNeighborsManagementInformationLldpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200LldpNeighborsManagementInformationLldpIndex.setStatus("current")


class _Me1200LldpNeighborsManagementInformationLldpManagement_Type(Integer32):
    """Custom type me1200LldpNeighborsManagementInformationLldpManagement based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Me1200LldpNeighborsManagementInformationLldpManagement_Type.__name__ = "Integer32"
_Me1200LldpNeighborsManagementInformationLldpManagement_Object = MibTableColumn
me1200LldpNeighborsManagementInformationLldpManagement = _Me1200LldpNeighborsManagementInformationLldpManagement_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 34, 1, 3, 4, 1, 3),
    _Me1200LldpNeighborsManagementInformationLldpManagement_Type()
)
me1200LldpNeighborsManagementInformationLldpManagement.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200LldpNeighborsManagementInformationLldpManagement.setStatus("current")


class _Me1200LldpNeighborsManagementInformationSystemManagementAddress_Type(ME1200DisplayString):
    """Custom type me1200LldpNeighborsManagementInformationSystemManagementAddress based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 166),
    )


_Me1200LldpNeighborsManagementInformationSystemManagementAddress_Type.__name__ = "ME1200DisplayString"
_Me1200LldpNeighborsManagementInformationSystemManagementAddress_Object = MibTableColumn
me1200LldpNeighborsManagementInformationSystemManagementAddress = _Me1200LldpNeighborsManagementInformationSystemManagementAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 34, 1, 3, 4, 1, 5),
    _Me1200LldpNeighborsManagementInformationSystemManagementAddress_Type()
)
me1200LldpNeighborsManagementInformationSystemManagementAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200LldpNeighborsManagementInformationSystemManagementAddress.setStatus("current")
_Me1200LldpControl_ObjectIdentity = ObjectIdentity
me1200LldpControl = _Me1200LldpControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 34, 1, 4)
)
_Me1200LldpStatisticsClear_ObjectIdentity = ObjectIdentity
me1200LldpStatisticsClear = _Me1200LldpStatisticsClear_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 34, 1, 4, 1)
)
_Me1200LldpControlStatisticsClearTable_Object = MibTable
me1200LldpControlStatisticsClearTable = _Me1200LldpControlStatisticsClearTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 34, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    me1200LldpControlStatisticsClearTable.setStatus("current")
_Me1200LldpControlStatisticsClearEntry_Object = MibTableRow
me1200LldpControlStatisticsClearEntry = _Me1200LldpControlStatisticsClearEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 34, 1, 4, 1, 1, 1)
)
me1200LldpControlStatisticsClearEntry.setIndexNames(
    (0, "ME1200-LLDP-MIB", "me1200LldpControlStatisticsClearIfIndex"),
)
if mibBuilder.loadTexts:
    me1200LldpControlStatisticsClearEntry.setStatus("current")
_Me1200LldpControlStatisticsClearIfIndex_Type = ME1200InterfaceIndex
_Me1200LldpControlStatisticsClearIfIndex_Object = MibTableColumn
me1200LldpControlStatisticsClearIfIndex = _Me1200LldpControlStatisticsClearIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 34, 1, 4, 1, 1, 1, 1),
    _Me1200LldpControlStatisticsClearIfIndex_Type()
)
me1200LldpControlStatisticsClearIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200LldpControlStatisticsClearIfIndex.setStatus("current")
_Me1200LldpControlStatisticsClearStatisticsClear_Type = TruthValue
_Me1200LldpControlStatisticsClearStatisticsClear_Object = MibTableColumn
me1200LldpControlStatisticsClearStatisticsClear = _Me1200LldpControlStatisticsClearStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 34, 1, 4, 1, 1, 1, 2),
    _Me1200LldpControlStatisticsClearStatisticsClear_Type()
)
me1200LldpControlStatisticsClearStatisticsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200LldpControlStatisticsClearStatisticsClear.setStatus("current")
_Me1200LldpControlStatisticsClearGlobal_ObjectIdentity = ObjectIdentity
me1200LldpControlStatisticsClearGlobal = _Me1200LldpControlStatisticsClearGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 34, 1, 4, 1, 2)
)
_Me1200LldpControlStatisticsClearGlobalClear_Type = TruthValue
_Me1200LldpControlStatisticsClearGlobalClear_Object = MibScalar
me1200LldpControlStatisticsClearGlobalClear = _Me1200LldpControlStatisticsClearGlobalClear_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 34, 1, 4, 1, 2, 1),
    _Me1200LldpControlStatisticsClearGlobalClear_Type()
)
me1200LldpControlStatisticsClearGlobalClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200LldpControlStatisticsClearGlobalClear.setStatus("current")
_Me1200LldpMibConformance_ObjectIdentity = ObjectIdentity
me1200LldpMibConformance = _Me1200LldpMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 34, 3)
)
_Me1200LldpMibCompliances_ObjectIdentity = ObjectIdentity
me1200LldpMibCompliances = _Me1200LldpMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 34, 3, 1)
)
_Me1200LldpMibGroups_ObjectIdentity = ObjectIdentity
me1200LldpMibGroups = _Me1200LldpMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 34, 3, 2)
)

# Managed Objects groups

me1200LldpGlobalInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 34, 3, 2, 1)
)
me1200LldpGlobalInfoGroup.setObjects(
      *(("ME1200-LLDP-MIB", "me1200LldpGlobalInitDelay"),
        ("ME1200-LLDP-MIB", "me1200LldpGlobalMsgTxHold"),
        ("ME1200-LLDP-MIB", "me1200LldpGlobalMsgTxInterval"),
        ("ME1200-LLDP-MIB", "me1200LldpGlobalTxDelay"))
)
if mibBuilder.loadTexts:
    me1200LldpGlobalInfoGroup.setStatus("current")

me1200LldpConfigurationInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 34, 3, 2, 2)
)
me1200LldpConfigurationInfoGroup.setObjects(
      *(("ME1200-LLDP-MIB", "me1200LldpConfigurationAdminState"),
        ("ME1200-LLDP-MIB", "me1200LldpConfigurationCdpAware"),
        ("ME1200-LLDP-MIB", "me1200LldpConfigurationOptionalTlvs"))
)
if mibBuilder.loadTexts:
    me1200LldpConfigurationInfoGroup.setStatus("current")

me1200LldpStatisticsGlobalCountersInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 34, 3, 2, 3)
)
me1200LldpStatisticsGlobalCountersInfoGroup.setObjects(
      *(("ME1200-LLDP-MIB", "me1200LldpStatisticsGlobalCountersTableInserts"),
        ("ME1200-LLDP-MIB", "me1200LldpStatisticsGlobalCountersTableDeletes"),
        ("ME1200-LLDP-MIB", "me1200LldpStatisticsGlobalCountersTableDrops"),
        ("ME1200-LLDP-MIB", "me1200LldpStatisticsGlobalCountersTableAgeOuts"),
        ("ME1200-LLDP-MIB", "me1200LldpStatisticsGlobalCountersLastChangeTime"))
)
if mibBuilder.loadTexts:
    me1200LldpStatisticsGlobalCountersInfoGroup.setStatus("current")

me1200LldpStatisticsTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 34, 3, 2, 4)
)
me1200LldpStatisticsTableInfoGroup.setObjects(
      *(("ME1200-LLDP-MIB", "me1200LldpStatisticsTxTotal"),
        ("ME1200-LLDP-MIB", "me1200LldpStatisticsRxTotal"),
        ("ME1200-LLDP-MIB", "me1200LldpStatisticsRxError"),
        ("ME1200-LLDP-MIB", "me1200LldpStatisticsRxDiscarded"),
        ("ME1200-LLDP-MIB", "me1200LldpStatisticsTLVsDiscarded"),
        ("ME1200-LLDP-MIB", "me1200LldpStatisticsTLVsUnrecognized"),
        ("ME1200-LLDP-MIB", "me1200LldpStatisticsTLVsOrgDiscarded"),
        ("ME1200-LLDP-MIB", "me1200LldpStatisticsAgeOuts"))
)
if mibBuilder.loadTexts:
    me1200LldpStatisticsTableInfoGroup.setStatus("current")

me1200LldpNeighborsInformationInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 34, 3, 2, 5)
)
me1200LldpNeighborsInformationInfoGroup.setObjects(
      *(("ME1200-LLDP-MIB", "me1200LldpNeighborsInformationChassisId"),
        ("ME1200-LLDP-MIB", "me1200LldpNeighborsInformationPortId"),
        ("ME1200-LLDP-MIB", "me1200LldpNeighborsInformationPortDescription"),
        ("ME1200-LLDP-MIB", "me1200LldpNeighborsInformationSystemName"),
        ("ME1200-LLDP-MIB", "me1200LldpNeighborsInformationSystemDescription"),
        ("ME1200-LLDP-MIB", "me1200LldpNeighborsInformationSystemCapabilities"),
        ("ME1200-LLDP-MIB", "me1200LldpNeighborsInformationSystemCapabilitiesEnable"))
)
if mibBuilder.loadTexts:
    me1200LldpNeighborsInformationInfoGroup.setStatus("current")

me1200LldpNeighborsManagementInformationInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 34, 3, 2, 6)
)
me1200LldpNeighborsManagementInformationInfoGroup.setObjects(
    ("ME1200-LLDP-MIB", "me1200LldpNeighborsManagementInformationSystemManagementAddress")
)
if mibBuilder.loadTexts:
    me1200LldpNeighborsManagementInformationInfoGroup.setStatus("current")

me1200LldpControlStatisticsClearTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 34, 3, 2, 7)
)
me1200LldpControlStatisticsClearTableInfoGroup.setObjects(
    ("ME1200-LLDP-MIB", "me1200LldpControlStatisticsClearStatisticsClear")
)
if mibBuilder.loadTexts:
    me1200LldpControlStatisticsClearTableInfoGroup.setStatus("current")

me1200LldpControlStatisticsClearGlobalInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 34, 3, 2, 8)
)
me1200LldpControlStatisticsClearGlobalInfoGroup.setObjects(
    ("ME1200-LLDP-MIB", "me1200LldpControlStatisticsClearGlobalClear")
)
if mibBuilder.loadTexts:
    me1200LldpControlStatisticsClearGlobalInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

me1200LldpMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 34, 3, 1, 1)
)
me1200LldpMibCompliance.setObjects(
      *(("ME1200-LLDP-MIB", "me1200LldpGlobalInfoGroup"),
        ("ME1200-LLDP-MIB", "me1200LldpConfigurationInfoGroup"),
        ("ME1200-LLDP-MIB", "me1200LldpStatisticsGlobalCountersInfoGroup"),
        ("ME1200-LLDP-MIB", "me1200LldpStatisticsTableInfoGroup"),
        ("ME1200-LLDP-MIB", "me1200LldpNeighborsInformationInfoGroup"),
        ("ME1200-LLDP-MIB", "me1200LldpNeighborsManagementInformationInfoGroup"),
        ("ME1200-LLDP-MIB", "me1200LldpControlStatisticsClearTableInfoGroup"),
        ("ME1200-LLDP-MIB", "me1200LldpControlStatisticsClearGlobalInfoGroup"))
)
if mibBuilder.loadTexts:
    me1200LldpMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ME1200-LLDP-MIB",
    **{"ME1200lldpAdminState": ME1200lldpAdminState,
       "me1200LldpMib": me1200LldpMib,
       "me1200LldpObjects": me1200LldpObjects,
       "me1200LldpConfig": me1200LldpConfig,
       "me1200LldpGlobal": me1200LldpGlobal,
       "me1200LldpGlobalInitDelay": me1200LldpGlobalInitDelay,
       "me1200LldpGlobalMsgTxHold": me1200LldpGlobalMsgTxHold,
       "me1200LldpGlobalMsgTxInterval": me1200LldpGlobalMsgTxInterval,
       "me1200LldpGlobalTxDelay": me1200LldpGlobalTxDelay,
       "me1200LldpConfigurationTable": me1200LldpConfigurationTable,
       "me1200LldpConfigurationEntry": me1200LldpConfigurationEntry,
       "me1200LldpConfigurationIfIndex": me1200LldpConfigurationIfIndex,
       "me1200LldpConfigurationAdminState": me1200LldpConfigurationAdminState,
       "me1200LldpConfigurationCdpAware": me1200LldpConfigurationCdpAware,
       "me1200LldpConfigurationOptionalTlvs": me1200LldpConfigurationOptionalTlvs,
       "me1200LldpStatus": me1200LldpStatus,
       "me1200LldpStatistics": me1200LldpStatistics,
       "me1200LldpStatisticsGlobalCounters": me1200LldpStatisticsGlobalCounters,
       "me1200LldpStatisticsGlobalCountersTableInserts": me1200LldpStatisticsGlobalCountersTableInserts,
       "me1200LldpStatisticsGlobalCountersTableDeletes": me1200LldpStatisticsGlobalCountersTableDeletes,
       "me1200LldpStatisticsGlobalCountersTableDrops": me1200LldpStatisticsGlobalCountersTableDrops,
       "me1200LldpStatisticsGlobalCountersTableAgeOuts": me1200LldpStatisticsGlobalCountersTableAgeOuts,
       "me1200LldpStatisticsGlobalCountersLastChangeTime": me1200LldpStatisticsGlobalCountersLastChangeTime,
       "me1200LldpStatisticsTable": me1200LldpStatisticsTable,
       "me1200LldpStatisticsEntry": me1200LldpStatisticsEntry,
       "me1200LldpStatisticsIfIndex": me1200LldpStatisticsIfIndex,
       "me1200LldpStatisticsTxTotal": me1200LldpStatisticsTxTotal,
       "me1200LldpStatisticsRxTotal": me1200LldpStatisticsRxTotal,
       "me1200LldpStatisticsRxError": me1200LldpStatisticsRxError,
       "me1200LldpStatisticsRxDiscarded": me1200LldpStatisticsRxDiscarded,
       "me1200LldpStatisticsTLVsDiscarded": me1200LldpStatisticsTLVsDiscarded,
       "me1200LldpStatisticsTLVsUnrecognized": me1200LldpStatisticsTLVsUnrecognized,
       "me1200LldpStatisticsTLVsOrgDiscarded": me1200LldpStatisticsTLVsOrgDiscarded,
       "me1200LldpStatisticsAgeOuts": me1200LldpStatisticsAgeOuts,
       "me1200LldpNeighborsInformationTable": me1200LldpNeighborsInformationTable,
       "me1200LldpNeighborsInformationEntry": me1200LldpNeighborsInformationEntry,
       "me1200LldpNeighborsInformationIfIndex": me1200LldpNeighborsInformationIfIndex,
       "me1200LldpNeighborsInformationLldpIndex": me1200LldpNeighborsInformationLldpIndex,
       "me1200LldpNeighborsInformationChassisId": me1200LldpNeighborsInformationChassisId,
       "me1200LldpNeighborsInformationPortId": me1200LldpNeighborsInformationPortId,
       "me1200LldpNeighborsInformationPortDescription": me1200LldpNeighborsInformationPortDescription,
       "me1200LldpNeighborsInformationSystemName": me1200LldpNeighborsInformationSystemName,
       "me1200LldpNeighborsInformationSystemDescription": me1200LldpNeighborsInformationSystemDescription,
       "me1200LldpNeighborsInformationSystemCapabilities": me1200LldpNeighborsInformationSystemCapabilities,
       "me1200LldpNeighborsInformationSystemCapabilitiesEnable": me1200LldpNeighborsInformationSystemCapabilitiesEnable,
       "me1200LldpNeighborsManagementInformationTable": me1200LldpNeighborsManagementInformationTable,
       "me1200LldpNeighborsManagementInformationEntry": me1200LldpNeighborsManagementInformationEntry,
       "me1200LldpNeighborsManagementInformationIfIndex": me1200LldpNeighborsManagementInformationIfIndex,
       "me1200LldpNeighborsManagementInformationLldpIndex": me1200LldpNeighborsManagementInformationLldpIndex,
       "me1200LldpNeighborsManagementInformationLldpManagement": me1200LldpNeighborsManagementInformationLldpManagement,
       "me1200LldpNeighborsManagementInformationSystemManagementAddress": me1200LldpNeighborsManagementInformationSystemManagementAddress,
       "me1200LldpControl": me1200LldpControl,
       "me1200LldpStatisticsClear": me1200LldpStatisticsClear,
       "me1200LldpControlStatisticsClearTable": me1200LldpControlStatisticsClearTable,
       "me1200LldpControlStatisticsClearEntry": me1200LldpControlStatisticsClearEntry,
       "me1200LldpControlStatisticsClearIfIndex": me1200LldpControlStatisticsClearIfIndex,
       "me1200LldpControlStatisticsClearStatisticsClear": me1200LldpControlStatisticsClearStatisticsClear,
       "me1200LldpControlStatisticsClearGlobal": me1200LldpControlStatisticsClearGlobal,
       "me1200LldpControlStatisticsClearGlobalClear": me1200LldpControlStatisticsClearGlobalClear,
       "me1200LldpMibConformance": me1200LldpMibConformance,
       "me1200LldpMibCompliances": me1200LldpMibCompliances,
       "me1200LldpMibCompliance": me1200LldpMibCompliance,
       "me1200LldpMibGroups": me1200LldpMibGroups,
       "me1200LldpGlobalInfoGroup": me1200LldpGlobalInfoGroup,
       "me1200LldpConfigurationInfoGroup": me1200LldpConfigurationInfoGroup,
       "me1200LldpStatisticsGlobalCountersInfoGroup": me1200LldpStatisticsGlobalCountersInfoGroup,
       "me1200LldpStatisticsTableInfoGroup": me1200LldpStatisticsTableInfoGroup,
       "me1200LldpNeighborsInformationInfoGroup": me1200LldpNeighborsInformationInfoGroup,
       "me1200LldpNeighborsManagementInformationInfoGroup": me1200LldpNeighborsManagementInformationInfoGroup,
       "me1200LldpControlStatisticsClearTableInfoGroup": me1200LldpControlStatisticsClearTableInfoGroup,
       "me1200LldpControlStatisticsClearGlobalInfoGroup": me1200LldpControlStatisticsClearGlobalInfoGroup}
)
