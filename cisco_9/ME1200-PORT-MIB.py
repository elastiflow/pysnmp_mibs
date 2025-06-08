# SNMP MIB module (ME1200-PORT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/ME1200-PORT-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 09:05:31 2025
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
 ME1200Unsigned8) = mibBuilder.importSymbols(
    "ME1200-TC",
    "ME1200DisplayString",
    "ME1200InterfaceIndex",
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

me1200PortMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11)
)
if mibBuilder.loadTexts:
    me1200PortMib.setRevisions(
        ("2016-05-23 00:00",
         "2016-05-18 00:00",
         "2014-03-11 00:00",
         "2014-02-18 00:00",
         "2014-01-29 00:00",
         "2013-10-08 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ME1200PortDuplex(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("forceFullDuplex", 0),
          ("forceHalfDuplex", 1),
          ("autoNegAdvertiseFdx", 2),
          ("autoNegAdvertiseHdx", 3),
          ("autoNegAdvertiseBoth", 4))
    )



class ME1200PortFc(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )



class ME1200PortMedia(TextualConvention, Integer32):
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
        *(("rj45", 0),
          ("sfp", 1),
          ("dual", 2))
    )



class ME1200PortPhyVeriPhyStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("correctlyTerminatedPair", 0),
          ("openPair", 1),
          ("shortPair", 2),
          ("abnormalTermination", 4),
          ("crossPairShortToPairA", 8),
          ("crossPairShortToPairB", 9),
          ("crossPairShortToPairC", 10),
          ("crossPairShortToPairD", 11),
          ("abnormalCrossPairCouplingToPairA", 12),
          ("abnormalCrossPairCouplingToPairB", 13),
          ("abnormalCrossPairCouplingToPairC", 14),
          ("abnormalCrossPairCouplingToPairD", 15),
          ("unknownResult", 16),
          ("veriPhyRunning", 17))
    )



class ME1200PortSFPTransceiver(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("notSupported", 1),
          ("sfp100FX", 2),
          ("sfp1000BaseT", 7),
          ("sfp1000BaseCx", 8),
          ("sfp1000BaseSx", 9),
          ("sfp1000BaseLx", 10),
          ("sfp1000BaseX", 11),
          ("sfp2G5", 12),
          ("sfp5G", 13),
          ("sfp10G", 14))
    )



class ME1200PortSpeed(TextualConvention, Integer32):
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
        *(("force10Mode", 0),
          ("force100Mode", 1),
          ("force1GMode", 2),
          ("autoNegMode", 3))
    )



class ME1200PortStatusSpeed(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("speed10M", 1),
          ("speed100M", 2),
          ("speed1G", 3),
          ("speed2G5", 4),
          ("speed5G", 5),
          ("speed10G", 6),
          ("speed12G", 7))
    )



# MIB Managed Objects in the order of their OIDs

_Me1200PortObjects_ObjectIdentity = ObjectIdentity
me1200PortObjects = _Me1200PortObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1)
)
_Me1200PortConfig_ObjectIdentity = ObjectIdentity
me1200PortConfig = _Me1200PortConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 2)
)
_Me1200PortConfigTable_Object = MibTable
me1200PortConfigTable = _Me1200PortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 2, 1)
)
if mibBuilder.loadTexts:
    me1200PortConfigTable.setStatus("current")
_Me1200PortConfigEntry_Object = MibTableRow
me1200PortConfigEntry = _Me1200PortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 2, 1, 1)
)
me1200PortConfigEntry.setIndexNames(
    (0, "ME1200-PORT-MIB", "me1200PortConfigIfIndex"),
)
if mibBuilder.loadTexts:
    me1200PortConfigEntry.setStatus("current")
_Me1200PortConfigIfIndex_Type = ME1200InterfaceIndex
_Me1200PortConfigIfIndex_Object = MibTableColumn
me1200PortConfigIfIndex = _Me1200PortConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 2, 1, 1, 1),
    _Me1200PortConfigIfIndex_Type()
)
me1200PortConfigIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200PortConfigIfIndex.setStatus("current")
_Me1200PortConfigShutdown_Type = TruthValue
_Me1200PortConfigShutdown_Object = MibTableColumn
me1200PortConfigShutdown = _Me1200PortConfigShutdown_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 2, 1, 1, 2),
    _Me1200PortConfigShutdown_Type()
)
me1200PortConfigShutdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PortConfigShutdown.setStatus("current")
_Me1200PortConfigSpeed_Type = ME1200PortSpeed
_Me1200PortConfigSpeed_Object = MibTableColumn
me1200PortConfigSpeed = _Me1200PortConfigSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 2, 1, 1, 3),
    _Me1200PortConfigSpeed_Type()
)
me1200PortConfigSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PortConfigSpeed.setStatus("current")
_Me1200PortConfigMediaType_Type = ME1200PortMedia
_Me1200PortConfigMediaType_Object = MibTableColumn
me1200PortConfigMediaType = _Me1200PortConfigMediaType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 2, 1, 1, 4),
    _Me1200PortConfigMediaType_Type()
)
me1200PortConfigMediaType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PortConfigMediaType.setStatus("current")
_Me1200PortConfigDuplex_Type = ME1200PortDuplex
_Me1200PortConfigDuplex_Object = MibTableColumn
me1200PortConfigDuplex = _Me1200PortConfigDuplex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 2, 1, 1, 5),
    _Me1200PortConfigDuplex_Type()
)
me1200PortConfigDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PortConfigDuplex.setStatus("current")
_Me1200PortConfigFC_Type = ME1200PortFc
_Me1200PortConfigFC_Object = MibTableColumn
me1200PortConfigFC = _Me1200PortConfigFC_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 2, 1, 1, 6),
    _Me1200PortConfigFC_Type()
)
me1200PortConfigFC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PortConfigFC.setStatus("current")
_Me1200PortConfigMTU_Type = Unsigned32
_Me1200PortConfigMTU_Object = MibTableColumn
me1200PortConfigMTU = _Me1200PortConfigMTU_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 2, 1, 1, 7),
    _Me1200PortConfigMTU_Type()
)
me1200PortConfigMTU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PortConfigMTU.setStatus("current")
_Me1200PortConfigExcessiveRestart_Type = TruthValue
_Me1200PortConfigExcessiveRestart_Object = MibTableColumn
me1200PortConfigExcessiveRestart = _Me1200PortConfigExcessiveRestart_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 2, 1, 1, 8),
    _Me1200PortConfigExcessiveRestart_Type()
)
me1200PortConfigExcessiveRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PortConfigExcessiveRestart.setStatus("current")
_Me1200PortStatus_ObjectIdentity = ObjectIdentity
me1200PortStatus = _Me1200PortStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 3)
)
_Me1200PortInformationTable_Object = MibTable
me1200PortInformationTable = _Me1200PortInformationTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 3, 1)
)
if mibBuilder.loadTexts:
    me1200PortInformationTable.setStatus("current")
_Me1200PortInformationEntry_Object = MibTableRow
me1200PortInformationEntry = _Me1200PortInformationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 3, 1, 1)
)
me1200PortInformationEntry.setIndexNames(
    (0, "ME1200-PORT-MIB", "me1200PortInformationIfIndex"),
)
if mibBuilder.loadTexts:
    me1200PortInformationEntry.setStatus("current")
_Me1200PortInformationIfIndex_Type = ME1200InterfaceIndex
_Me1200PortInformationIfIndex_Object = MibTableColumn
me1200PortInformationIfIndex = _Me1200PortInformationIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 3, 1, 1, 1),
    _Me1200PortInformationIfIndex_Type()
)
me1200PortInformationIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200PortInformationIfIndex.setStatus("current")
_Me1200PortInformationLink_Type = TruthValue
_Me1200PortInformationLink_Object = MibTableColumn
me1200PortInformationLink = _Me1200PortInformationLink_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 3, 1, 1, 2),
    _Me1200PortInformationLink_Type()
)
me1200PortInformationLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PortInformationLink.setStatus("current")
_Me1200PortInformationFdx_Type = TruthValue
_Me1200PortInformationFdx_Object = MibTableColumn
me1200PortInformationFdx = _Me1200PortInformationFdx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 3, 1, 1, 3),
    _Me1200PortInformationFdx_Type()
)
me1200PortInformationFdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PortInformationFdx.setStatus("current")
_Me1200PortInformationFiber_Type = TruthValue
_Me1200PortInformationFiber_Object = MibTableColumn
me1200PortInformationFiber = _Me1200PortInformationFiber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 3, 1, 1, 4),
    _Me1200PortInformationFiber_Type()
)
me1200PortInformationFiber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PortInformationFiber.setStatus("current")
_Me1200PortInformationSpeed_Type = ME1200PortStatusSpeed
_Me1200PortInformationSpeed_Object = MibTableColumn
me1200PortInformationSpeed = _Me1200PortInformationSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 3, 1, 1, 5),
    _Me1200PortInformationSpeed_Type()
)
me1200PortInformationSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PortInformationSpeed.setStatus("current")
_Me1200PortInformationSFPType_Type = ME1200PortSFPTransceiver
_Me1200PortInformationSFPType_Object = MibTableColumn
me1200PortInformationSFPType = _Me1200PortInformationSFPType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 3, 1, 1, 6),
    _Me1200PortInformationSFPType_Type()
)
me1200PortInformationSFPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PortInformationSFPType.setStatus("current")


class _Me1200PortInformationSFPVendorName_Type(ME1200DisplayString):
    """Custom type me1200PortInformationSFPVendorName based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_Me1200PortInformationSFPVendorName_Type.__name__ = "ME1200DisplayString"
_Me1200PortInformationSFPVendorName_Object = MibTableColumn
me1200PortInformationSFPVendorName = _Me1200PortInformationSFPVendorName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 3, 1, 1, 7),
    _Me1200PortInformationSFPVendorName_Type()
)
me1200PortInformationSFPVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PortInformationSFPVendorName.setStatus("current")


class _Me1200PortInformationSFPVendorPN_Type(ME1200DisplayString):
    """Custom type me1200PortInformationSFPVendorPN based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_Me1200PortInformationSFPVendorPN_Type.__name__ = "ME1200DisplayString"
_Me1200PortInformationSFPVendorPN_Object = MibTableColumn
me1200PortInformationSFPVendorPN = _Me1200PortInformationSFPVendorPN_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 3, 1, 1, 8),
    _Me1200PortInformationSFPVendorPN_Type()
)
me1200PortInformationSFPVendorPN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PortInformationSFPVendorPN.setStatus("current")


class _Me1200PortInformationSFPVendorRev_Type(ME1200DisplayString):
    """Custom type me1200PortInformationSFPVendorRev based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_Me1200PortInformationSFPVendorRev_Type.__name__ = "ME1200DisplayString"
_Me1200PortInformationSFPVendorRev_Object = MibTableColumn
me1200PortInformationSFPVendorRev = _Me1200PortInformationSFPVendorRev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 3, 1, 1, 9),
    _Me1200PortInformationSFPVendorRev_Type()
)
me1200PortInformationSFPVendorRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PortInformationSFPVendorRev.setStatus("current")
_Me1200PortStatistics_ObjectIdentity = ObjectIdentity
me1200PortStatistics = _Me1200PortStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 3, 2)
)
_Me1200PortRmonStatisticsTable_Object = MibTable
me1200PortRmonStatisticsTable = _Me1200PortRmonStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    me1200PortRmonStatisticsTable.setStatus("current")
_Me1200PortRmonStatisticsEntry_Object = MibTableRow
me1200PortRmonStatisticsEntry = _Me1200PortRmonStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 3, 2, 1, 1)
)
me1200PortRmonStatisticsEntry.setIndexNames(
    (0, "ME1200-PORT-MIB", "me1200PortRmonStatisticsIfIndex"),
)
if mibBuilder.loadTexts:
    me1200PortRmonStatisticsEntry.setStatus("current")
_Me1200PortRmonStatisticsIfIndex_Type = ME1200InterfaceIndex
_Me1200PortRmonStatisticsIfIndex_Object = MibTableColumn
me1200PortRmonStatisticsIfIndex = _Me1200PortRmonStatisticsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 3, 2, 1, 1, 1),
    _Me1200PortRmonStatisticsIfIndex_Type()
)
me1200PortRmonStatisticsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200PortRmonStatisticsIfIndex.setStatus("current")
_Me1200PortRmonStatisticsRxDropEvents_Type = Counter64
_Me1200PortRmonStatisticsRxDropEvents_Object = MibTableColumn
me1200PortRmonStatisticsRxDropEvents = _Me1200PortRmonStatisticsRxDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 3, 2, 1, 1, 2),
    _Me1200PortRmonStatisticsRxDropEvents_Type()
)
me1200PortRmonStatisticsRxDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PortRmonStatisticsRxDropEvents.setStatus("current")
_Me1200PortRmonStatisticsRxOctects_Type = Counter64
_Me1200PortRmonStatisticsRxOctects_Object = MibTableColumn
me1200PortRmonStatisticsRxOctects = _Me1200PortRmonStatisticsRxOctects_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 3, 2, 1, 1, 3),
    _Me1200PortRmonStatisticsRxOctects_Type()
)
me1200PortRmonStatisticsRxOctects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PortRmonStatisticsRxOctects.setStatus("current")
_Me1200PortRmonStatisticsRxPkts_Type = Counter64
_Me1200PortRmonStatisticsRxPkts_Object = MibTableColumn
me1200PortRmonStatisticsRxPkts = _Me1200PortRmonStatisticsRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 3, 2, 1, 1, 4),
    _Me1200PortRmonStatisticsRxPkts_Type()
)
me1200PortRmonStatisticsRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PortRmonStatisticsRxPkts.setStatus("current")
_Me1200PortRmonStatisticsRxBroadcastPkts_Type = Counter64
_Me1200PortRmonStatisticsRxBroadcastPkts_Object = MibTableColumn
me1200PortRmonStatisticsRxBroadcastPkts = _Me1200PortRmonStatisticsRxBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 3, 2, 1, 1, 5),
    _Me1200PortRmonStatisticsRxBroadcastPkts_Type()
)
me1200PortRmonStatisticsRxBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PortRmonStatisticsRxBroadcastPkts.setStatus("current")
_Me1200PortRmonStatisticsRxMulticastPkts_Type = Counter64
_Me1200PortRmonStatisticsRxMulticastPkts_Object = MibTableColumn
me1200PortRmonStatisticsRxMulticastPkts = _Me1200PortRmonStatisticsRxMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 3, 2, 1, 1, 6),
    _Me1200PortRmonStatisticsRxMulticastPkts_Type()
)
me1200PortRmonStatisticsRxMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PortRmonStatisticsRxMulticastPkts.setStatus("current")
_Me1200PortRmonStatisticsRxCrcAlignErrPkts_Type = Counter64
_Me1200PortRmonStatisticsRxCrcAlignErrPkts_Object = MibTableColumn
me1200PortRmonStatisticsRxCrcAlignErrPkts = _Me1200PortRmonStatisticsRxCrcAlignErrPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 3, 2, 1, 1, 7),
    _Me1200PortRmonStatisticsRxCrcAlignErrPkts_Type()
)
me1200PortRmonStatisticsRxCrcAlignErrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PortRmonStatisticsRxCrcAlignErrPkts.setStatus("current")
_Me1200PortRmonStatisticsRxUndersizePkts_Type = Counter64
_Me1200PortRmonStatisticsRxUndersizePkts_Object = MibTableColumn
me1200PortRmonStatisticsRxUndersizePkts = _Me1200PortRmonStatisticsRxUndersizePkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 3, 2, 1, 1, 8),
    _Me1200PortRmonStatisticsRxUndersizePkts_Type()
)
me1200PortRmonStatisticsRxUndersizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PortRmonStatisticsRxUndersizePkts.setStatus("current")
_Me1200PortRmonStatisticsRxOverizePkts_Type = Counter64
_Me1200PortRmonStatisticsRxOverizePkts_Object = MibTableColumn
me1200PortRmonStatisticsRxOverizePkts = _Me1200PortRmonStatisticsRxOverizePkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 3, 2, 1, 1, 9),
    _Me1200PortRmonStatisticsRxOverizePkts_Type()
)
me1200PortRmonStatisticsRxOverizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PortRmonStatisticsRxOverizePkts.setStatus("current")
_Me1200PortRmonStatisticsRxFragmentsPkts_Type = Counter64
_Me1200PortRmonStatisticsRxFragmentsPkts_Object = MibTableColumn
me1200PortRmonStatisticsRxFragmentsPkts = _Me1200PortRmonStatisticsRxFragmentsPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 3, 2, 1, 1, 10),
    _Me1200PortRmonStatisticsRxFragmentsPkts_Type()
)
me1200PortRmonStatisticsRxFragmentsPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PortRmonStatisticsRxFragmentsPkts.setStatus("current")
_Me1200PortRmonStatisticsRxJabbersPkts_Type = Counter64
_Me1200PortRmonStatisticsRxJabbersPkts_Object = MibTableColumn
me1200PortRmonStatisticsRxJabbersPkts = _Me1200PortRmonStatisticsRxJabbersPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 3, 2, 1, 1, 11),
    _Me1200PortRmonStatisticsRxJabbersPkts_Type()
)
me1200PortRmonStatisticsRxJabbersPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PortRmonStatisticsRxJabbersPkts.setStatus("current")
_Me1200PortRmonStatisticsRx64Pkts_Type = Counter64
_Me1200PortRmonStatisticsRx64Pkts_Object = MibTableColumn
me1200PortRmonStatisticsRx64Pkts = _Me1200PortRmonStatisticsRx64Pkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 3, 2, 1, 1, 12),
    _Me1200PortRmonStatisticsRx64Pkts_Type()
)
me1200PortRmonStatisticsRx64Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PortRmonStatisticsRx64Pkts.setStatus("current")
_Me1200PortRmonStatisticsRx65to127Pkts_Type = Counter64
_Me1200PortRmonStatisticsRx65to127Pkts_Object = MibTableColumn
me1200PortRmonStatisticsRx65to127Pkts = _Me1200PortRmonStatisticsRx65to127Pkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 3, 2, 1, 1, 13),
    _Me1200PortRmonStatisticsRx65to127Pkts_Type()
)
me1200PortRmonStatisticsRx65to127Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PortRmonStatisticsRx65to127Pkts.setStatus("current")
_Me1200PortRmonStatisticsRx128to255Pkts_Type = Counter64
_Me1200PortRmonStatisticsRx128to255Pkts_Object = MibTableColumn
me1200PortRmonStatisticsRx128to255Pkts = _Me1200PortRmonStatisticsRx128to255Pkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 3, 2, 1, 1, 14),
    _Me1200PortRmonStatisticsRx128to255Pkts_Type()
)
me1200PortRmonStatisticsRx128to255Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PortRmonStatisticsRx128to255Pkts.setStatus("current")
_Me1200PortRmonStatisticsRx256to511Pkts_Type = Counter64
_Me1200PortRmonStatisticsRx256to511Pkts_Object = MibTableColumn
me1200PortRmonStatisticsRx256to511Pkts = _Me1200PortRmonStatisticsRx256to511Pkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 3, 2, 1, 1, 15),
    _Me1200PortRmonStatisticsRx256to511Pkts_Type()
)
me1200PortRmonStatisticsRx256to511Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PortRmonStatisticsRx256to511Pkts.setStatus("current")
_Me1200PortRmonStatisticsRx512to1023Pkts_Type = Counter64
_Me1200PortRmonStatisticsRx512to1023Pkts_Object = MibTableColumn
me1200PortRmonStatisticsRx512to1023Pkts = _Me1200PortRmonStatisticsRx512to1023Pkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 3, 2, 1, 1, 16),
    _Me1200PortRmonStatisticsRx512to1023Pkts_Type()
)
me1200PortRmonStatisticsRx512to1023Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PortRmonStatisticsRx512to1023Pkts.setStatus("current")
_Me1200PortRmonStatisticsRx1024to1518Pkts_Type = Counter64
_Me1200PortRmonStatisticsRx1024to1518Pkts_Object = MibTableColumn
me1200PortRmonStatisticsRx1024to1518Pkts = _Me1200PortRmonStatisticsRx1024to1518Pkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 3, 2, 1, 1, 17),
    _Me1200PortRmonStatisticsRx1024to1518Pkts_Type()
)
me1200PortRmonStatisticsRx1024to1518Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PortRmonStatisticsRx1024to1518Pkts.setStatus("current")
_Me1200PortRmonStatisticsRx1519PktsToMax_Type = Counter64
_Me1200PortRmonStatisticsRx1519PktsToMax_Object = MibTableColumn
me1200PortRmonStatisticsRx1519PktsToMax = _Me1200PortRmonStatisticsRx1519PktsToMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 3, 2, 1, 1, 18),
    _Me1200PortRmonStatisticsRx1519PktsToMax_Type()
)
me1200PortRmonStatisticsRx1519PktsToMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PortRmonStatisticsRx1519PktsToMax.setStatus("current")
_Me1200PortRmonStatisticsTxDropEvents_Type = Counter64
_Me1200PortRmonStatisticsTxDropEvents_Object = MibTableColumn
me1200PortRmonStatisticsTxDropEvents = _Me1200PortRmonStatisticsTxDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 3, 2, 1, 1, 19),
    _Me1200PortRmonStatisticsTxDropEvents_Type()
)
me1200PortRmonStatisticsTxDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PortRmonStatisticsTxDropEvents.setStatus("current")
_Me1200PortRmonStatisticsTxOctects_Type = Counter64
_Me1200PortRmonStatisticsTxOctects_Object = MibTableColumn
me1200PortRmonStatisticsTxOctects = _Me1200PortRmonStatisticsTxOctects_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 3, 2, 1, 1, 20),
    _Me1200PortRmonStatisticsTxOctects_Type()
)
me1200PortRmonStatisticsTxOctects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PortRmonStatisticsTxOctects.setStatus("current")
_Me1200PortRmonStatisticsTxPkts_Type = Counter64
_Me1200PortRmonStatisticsTxPkts_Object = MibTableColumn
me1200PortRmonStatisticsTxPkts = _Me1200PortRmonStatisticsTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 3, 2, 1, 1, 21),
    _Me1200PortRmonStatisticsTxPkts_Type()
)
me1200PortRmonStatisticsTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PortRmonStatisticsTxPkts.setStatus("current")
_Me1200PortRmonStatisticsTxBroadcastPkts_Type = Counter64
_Me1200PortRmonStatisticsTxBroadcastPkts_Object = MibTableColumn
me1200PortRmonStatisticsTxBroadcastPkts = _Me1200PortRmonStatisticsTxBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 3, 2, 1, 1, 22),
    _Me1200PortRmonStatisticsTxBroadcastPkts_Type()
)
me1200PortRmonStatisticsTxBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PortRmonStatisticsTxBroadcastPkts.setStatus("current")
_Me1200PortRmonStatisticsTxMulticastPkts_Type = Counter64
_Me1200PortRmonStatisticsTxMulticastPkts_Object = MibTableColumn
me1200PortRmonStatisticsTxMulticastPkts = _Me1200PortRmonStatisticsTxMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 3, 2, 1, 1, 23),
    _Me1200PortRmonStatisticsTxMulticastPkts_Type()
)
me1200PortRmonStatisticsTxMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PortRmonStatisticsTxMulticastPkts.setStatus("current")
_Me1200PortRmonStatisticsTx64Pkts_Type = Counter64
_Me1200PortRmonStatisticsTx64Pkts_Object = MibTableColumn
me1200PortRmonStatisticsTx64Pkts = _Me1200PortRmonStatisticsTx64Pkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 3, 2, 1, 1, 24),
    _Me1200PortRmonStatisticsTx64Pkts_Type()
)
me1200PortRmonStatisticsTx64Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PortRmonStatisticsTx64Pkts.setStatus("current")
_Me1200PortRmonStatisticsTx65to127Pkts_Type = Counter64
_Me1200PortRmonStatisticsTx65to127Pkts_Object = MibTableColumn
me1200PortRmonStatisticsTx65to127Pkts = _Me1200PortRmonStatisticsTx65to127Pkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 3, 2, 1, 1, 25),
    _Me1200PortRmonStatisticsTx65to127Pkts_Type()
)
me1200PortRmonStatisticsTx65to127Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PortRmonStatisticsTx65to127Pkts.setStatus("current")
_Me1200PortRmonStatisticsTx128to255Pkts_Type = Counter64
_Me1200PortRmonStatisticsTx128to255Pkts_Object = MibTableColumn
me1200PortRmonStatisticsTx128to255Pkts = _Me1200PortRmonStatisticsTx128to255Pkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 3, 2, 1, 1, 26),
    _Me1200PortRmonStatisticsTx128to255Pkts_Type()
)
me1200PortRmonStatisticsTx128to255Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PortRmonStatisticsTx128to255Pkts.setStatus("current")
_Me1200PortRmonStatisticsTx256to511Pkts_Type = Counter64
_Me1200PortRmonStatisticsTx256to511Pkts_Object = MibTableColumn
me1200PortRmonStatisticsTx256to511Pkts = _Me1200PortRmonStatisticsTx256to511Pkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 3, 2, 1, 1, 27),
    _Me1200PortRmonStatisticsTx256to511Pkts_Type()
)
me1200PortRmonStatisticsTx256to511Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PortRmonStatisticsTx256to511Pkts.setStatus("current")
_Me1200PortRmonStatisticsTx512to1023Pkts_Type = Counter64
_Me1200PortRmonStatisticsTx512to1023Pkts_Object = MibTableColumn
me1200PortRmonStatisticsTx512to1023Pkts = _Me1200PortRmonStatisticsTx512to1023Pkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 3, 2, 1, 1, 28),
    _Me1200PortRmonStatisticsTx512to1023Pkts_Type()
)
me1200PortRmonStatisticsTx512to1023Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PortRmonStatisticsTx512to1023Pkts.setStatus("current")
_Me1200PortRmonStatisticsTx1024to1518Pkts_Type = Counter64
_Me1200PortRmonStatisticsTx1024to1518Pkts_Object = MibTableColumn
me1200PortRmonStatisticsTx1024to1518Pkts = _Me1200PortRmonStatisticsTx1024to1518Pkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 3, 2, 1, 1, 29),
    _Me1200PortRmonStatisticsTx1024to1518Pkts_Type()
)
me1200PortRmonStatisticsTx1024to1518Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PortRmonStatisticsTx1024to1518Pkts.setStatus("current")
_Me1200PortRmonStatisticsTx1519PktsToMax_Type = Counter64
_Me1200PortRmonStatisticsTx1519PktsToMax_Object = MibTableColumn
me1200PortRmonStatisticsTx1519PktsToMax = _Me1200PortRmonStatisticsTx1519PktsToMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 3, 2, 1, 1, 30),
    _Me1200PortRmonStatisticsTx1519PktsToMax_Type()
)
me1200PortRmonStatisticsTx1519PktsToMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PortRmonStatisticsTx1519PktsToMax.setStatus("current")
_Me1200PortIfGroupStatisticsTable_Object = MibTable
me1200PortIfGroupStatisticsTable = _Me1200PortIfGroupStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 3, 2, 2)
)
if mibBuilder.loadTexts:
    me1200PortIfGroupStatisticsTable.setStatus("current")
_Me1200PortIfGroupStatisticsEntry_Object = MibTableRow
me1200PortIfGroupStatisticsEntry = _Me1200PortIfGroupStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 3, 2, 2, 1)
)
me1200PortIfGroupStatisticsEntry.setIndexNames(
    (0, "ME1200-PORT-MIB", "me1200PortIfGroupStatisticsIfIndex"),
)
if mibBuilder.loadTexts:
    me1200PortIfGroupStatisticsEntry.setStatus("current")
_Me1200PortIfGroupStatisticsIfIndex_Type = ME1200InterfaceIndex
_Me1200PortIfGroupStatisticsIfIndex_Object = MibTableColumn
me1200PortIfGroupStatisticsIfIndex = _Me1200PortIfGroupStatisticsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 3, 2, 2, 1, 1),
    _Me1200PortIfGroupStatisticsIfIndex_Type()
)
me1200PortIfGroupStatisticsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200PortIfGroupStatisticsIfIndex.setStatus("current")
_Me1200PortIfGroupStatisticsRxOctets_Type = Counter64
_Me1200PortIfGroupStatisticsRxOctets_Object = MibTableColumn
me1200PortIfGroupStatisticsRxOctets = _Me1200PortIfGroupStatisticsRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 3, 2, 2, 1, 2),
    _Me1200PortIfGroupStatisticsRxOctets_Type()
)
me1200PortIfGroupStatisticsRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PortIfGroupStatisticsRxOctets.setStatus("current")
_Me1200PortIfGroupStatisticsRxUnicastPkts_Type = Counter64
_Me1200PortIfGroupStatisticsRxUnicastPkts_Object = MibTableColumn
me1200PortIfGroupStatisticsRxUnicastPkts = _Me1200PortIfGroupStatisticsRxUnicastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 3, 2, 2, 1, 3),
    _Me1200PortIfGroupStatisticsRxUnicastPkts_Type()
)
me1200PortIfGroupStatisticsRxUnicastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PortIfGroupStatisticsRxUnicastPkts.setStatus("current")
_Me1200PortIfGroupStatisticsRxMulticastPkts_Type = Counter64
_Me1200PortIfGroupStatisticsRxMulticastPkts_Object = MibTableColumn
me1200PortIfGroupStatisticsRxMulticastPkts = _Me1200PortIfGroupStatisticsRxMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 3, 2, 2, 1, 4),
    _Me1200PortIfGroupStatisticsRxMulticastPkts_Type()
)
me1200PortIfGroupStatisticsRxMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PortIfGroupStatisticsRxMulticastPkts.setStatus("current")
_Me1200PortIfGroupStatisticsRxBroadcastPkts_Type = Counter64
_Me1200PortIfGroupStatisticsRxBroadcastPkts_Object = MibTableColumn
me1200PortIfGroupStatisticsRxBroadcastPkts = _Me1200PortIfGroupStatisticsRxBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 3, 2, 2, 1, 5),
    _Me1200PortIfGroupStatisticsRxBroadcastPkts_Type()
)
me1200PortIfGroupStatisticsRxBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PortIfGroupStatisticsRxBroadcastPkts.setStatus("current")
_Me1200PortIfGroupStatisticsRxNonUnicastPkts_Type = Counter64
_Me1200PortIfGroupStatisticsRxNonUnicastPkts_Object = MibTableColumn
me1200PortIfGroupStatisticsRxNonUnicastPkts = _Me1200PortIfGroupStatisticsRxNonUnicastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 3, 2, 2, 1, 6),
    _Me1200PortIfGroupStatisticsRxNonUnicastPkts_Type()
)
me1200PortIfGroupStatisticsRxNonUnicastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PortIfGroupStatisticsRxNonUnicastPkts.setStatus("current")
_Me1200PortIfGroupStatisticsRxDiscards_Type = Counter64
_Me1200PortIfGroupStatisticsRxDiscards_Object = MibTableColumn
me1200PortIfGroupStatisticsRxDiscards = _Me1200PortIfGroupStatisticsRxDiscards_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 3, 2, 2, 1, 7),
    _Me1200PortIfGroupStatisticsRxDiscards_Type()
)
me1200PortIfGroupStatisticsRxDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PortIfGroupStatisticsRxDiscards.setStatus("current")
_Me1200PortIfGroupStatisticsRxErrors_Type = Counter64
_Me1200PortIfGroupStatisticsRxErrors_Object = MibTableColumn
me1200PortIfGroupStatisticsRxErrors = _Me1200PortIfGroupStatisticsRxErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 3, 2, 2, 1, 8),
    _Me1200PortIfGroupStatisticsRxErrors_Type()
)
me1200PortIfGroupStatisticsRxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PortIfGroupStatisticsRxErrors.setStatus("current")
_Me1200PortIfGroupStatisticsTxOctets_Type = Counter64
_Me1200PortIfGroupStatisticsTxOctets_Object = MibTableColumn
me1200PortIfGroupStatisticsTxOctets = _Me1200PortIfGroupStatisticsTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 3, 2, 2, 1, 9),
    _Me1200PortIfGroupStatisticsTxOctets_Type()
)
me1200PortIfGroupStatisticsTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PortIfGroupStatisticsTxOctets.setStatus("current")
_Me1200PortIfGroupStatisticsTxUnicastPkts_Type = Counter64
_Me1200PortIfGroupStatisticsTxUnicastPkts_Object = MibTableColumn
me1200PortIfGroupStatisticsTxUnicastPkts = _Me1200PortIfGroupStatisticsTxUnicastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 3, 2, 2, 1, 10),
    _Me1200PortIfGroupStatisticsTxUnicastPkts_Type()
)
me1200PortIfGroupStatisticsTxUnicastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PortIfGroupStatisticsTxUnicastPkts.setStatus("current")
_Me1200PortIfGroupStatisticsTxMulticastPkts_Type = Counter64
_Me1200PortIfGroupStatisticsTxMulticastPkts_Object = MibTableColumn
me1200PortIfGroupStatisticsTxMulticastPkts = _Me1200PortIfGroupStatisticsTxMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 3, 2, 2, 1, 11),
    _Me1200PortIfGroupStatisticsTxMulticastPkts_Type()
)
me1200PortIfGroupStatisticsTxMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PortIfGroupStatisticsTxMulticastPkts.setStatus("current")
_Me1200PortIfGroupStatisticsTxBroadcastPkts_Type = Counter64
_Me1200PortIfGroupStatisticsTxBroadcastPkts_Object = MibTableColumn
me1200PortIfGroupStatisticsTxBroadcastPkts = _Me1200PortIfGroupStatisticsTxBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 3, 2, 2, 1, 12),
    _Me1200PortIfGroupStatisticsTxBroadcastPkts_Type()
)
me1200PortIfGroupStatisticsTxBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PortIfGroupStatisticsTxBroadcastPkts.setStatus("current")
_Me1200PortIfGroupStatisticsTxNonUnicastPkts_Type = Counter64
_Me1200PortIfGroupStatisticsTxNonUnicastPkts_Object = MibTableColumn
me1200PortIfGroupStatisticsTxNonUnicastPkts = _Me1200PortIfGroupStatisticsTxNonUnicastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 3, 2, 2, 1, 13),
    _Me1200PortIfGroupStatisticsTxNonUnicastPkts_Type()
)
me1200PortIfGroupStatisticsTxNonUnicastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PortIfGroupStatisticsTxNonUnicastPkts.setStatus("current")
_Me1200PortIfGroupStatisticsTxDiscardPkts_Type = Counter64
_Me1200PortIfGroupStatisticsTxDiscardPkts_Object = MibTableColumn
me1200PortIfGroupStatisticsTxDiscardPkts = _Me1200PortIfGroupStatisticsTxDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 3, 2, 2, 1, 14),
    _Me1200PortIfGroupStatisticsTxDiscardPkts_Type()
)
me1200PortIfGroupStatisticsTxDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PortIfGroupStatisticsTxDiscardPkts.setStatus("current")
_Me1200PortIfGroupStatisticsTxErrorPkts_Type = Counter64
_Me1200PortIfGroupStatisticsTxErrorPkts_Object = MibTableColumn
me1200PortIfGroupStatisticsTxErrorPkts = _Me1200PortIfGroupStatisticsTxErrorPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 3, 2, 2, 1, 15),
    _Me1200PortIfGroupStatisticsTxErrorPkts_Type()
)
me1200PortIfGroupStatisticsTxErrorPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PortIfGroupStatisticsTxErrorPkts.setStatus("current")
_Me1200PortEthernetLikeStatisticsTable_Object = MibTable
me1200PortEthernetLikeStatisticsTable = _Me1200PortEthernetLikeStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 3, 2, 3)
)
if mibBuilder.loadTexts:
    me1200PortEthernetLikeStatisticsTable.setStatus("current")
_Me1200PortEthernetLikeStatisticsEntry_Object = MibTableRow
me1200PortEthernetLikeStatisticsEntry = _Me1200PortEthernetLikeStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 3, 2, 3, 1)
)
me1200PortEthernetLikeStatisticsEntry.setIndexNames(
    (0, "ME1200-PORT-MIB", "me1200PortEthernetLikeStatisticsIfIndex"),
)
if mibBuilder.loadTexts:
    me1200PortEthernetLikeStatisticsEntry.setStatus("current")
_Me1200PortEthernetLikeStatisticsIfIndex_Type = ME1200InterfaceIndex
_Me1200PortEthernetLikeStatisticsIfIndex_Object = MibTableColumn
me1200PortEthernetLikeStatisticsIfIndex = _Me1200PortEthernetLikeStatisticsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 3, 2, 3, 1, 1),
    _Me1200PortEthernetLikeStatisticsIfIndex_Type()
)
me1200PortEthernetLikeStatisticsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200PortEthernetLikeStatisticsIfIndex.setStatus("current")
_Me1200PortEthernetLikeStatisticsRxPauseFrames_Type = Counter64
_Me1200PortEthernetLikeStatisticsRxPauseFrames_Object = MibTableColumn
me1200PortEthernetLikeStatisticsRxPauseFrames = _Me1200PortEthernetLikeStatisticsRxPauseFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 3, 2, 3, 1, 2),
    _Me1200PortEthernetLikeStatisticsRxPauseFrames_Type()
)
me1200PortEthernetLikeStatisticsRxPauseFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PortEthernetLikeStatisticsRxPauseFrames.setStatus("current")
_Me1200PortEthernetLikeStatisticsTxPauseFrames_Type = Counter64
_Me1200PortEthernetLikeStatisticsTxPauseFrames_Object = MibTableColumn
me1200PortEthernetLikeStatisticsTxPauseFrames = _Me1200PortEthernetLikeStatisticsTxPauseFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 3, 2, 3, 1, 3),
    _Me1200PortEthernetLikeStatisticsTxPauseFrames_Type()
)
me1200PortEthernetLikeStatisticsTxPauseFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PortEthernetLikeStatisticsTxPauseFrames.setStatus("current")
_Me1200PortQueuesStatisticsTable_Object = MibTable
me1200PortQueuesStatisticsTable = _Me1200PortQueuesStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 3, 2, 4)
)
if mibBuilder.loadTexts:
    me1200PortQueuesStatisticsTable.setStatus("current")
_Me1200PortQueuesStatisticsEntry_Object = MibTableRow
me1200PortQueuesStatisticsEntry = _Me1200PortQueuesStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 3, 2, 4, 1)
)
me1200PortQueuesStatisticsEntry.setIndexNames(
    (0, "ME1200-PORT-MIB", "me1200PortQueuesStatisticsIfIndex"),
    (0, "ME1200-PORT-MIB", "me1200PortQueuesStatisticsQueue"),
)
if mibBuilder.loadTexts:
    me1200PortQueuesStatisticsEntry.setStatus("current")
_Me1200PortQueuesStatisticsIfIndex_Type = ME1200InterfaceIndex
_Me1200PortQueuesStatisticsIfIndex_Object = MibTableColumn
me1200PortQueuesStatisticsIfIndex = _Me1200PortQueuesStatisticsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 3, 2, 4, 1, 1),
    _Me1200PortQueuesStatisticsIfIndex_Type()
)
me1200PortQueuesStatisticsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200PortQueuesStatisticsIfIndex.setStatus("current")


class _Me1200PortQueuesStatisticsQueue_Type(Integer32):
    """Custom type me1200PortQueuesStatisticsQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Me1200PortQueuesStatisticsQueue_Type.__name__ = "Integer32"
_Me1200PortQueuesStatisticsQueue_Object = MibTableColumn
me1200PortQueuesStatisticsQueue = _Me1200PortQueuesStatisticsQueue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 3, 2, 4, 1, 2),
    _Me1200PortQueuesStatisticsQueue_Type()
)
me1200PortQueuesStatisticsQueue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200PortQueuesStatisticsQueue.setStatus("current")
_Me1200PortQueuesStatisticsRxPrio_Type = Counter64
_Me1200PortQueuesStatisticsRxPrio_Object = MibTableColumn
me1200PortQueuesStatisticsRxPrio = _Me1200PortQueuesStatisticsRxPrio_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 3, 2, 4, 1, 3),
    _Me1200PortQueuesStatisticsRxPrio_Type()
)
me1200PortQueuesStatisticsRxPrio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PortQueuesStatisticsRxPrio.setStatus("current")
_Me1200PortQueuesStatisticsTxPrio_Type = Counter64
_Me1200PortQueuesStatisticsTxPrio_Object = MibTableColumn
me1200PortQueuesStatisticsTxPrio = _Me1200PortQueuesStatisticsTxPrio_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 3, 2, 4, 1, 4),
    _Me1200PortQueuesStatisticsTxPrio_Type()
)
me1200PortQueuesStatisticsTxPrio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PortQueuesStatisticsTxPrio.setStatus("current")
_Me1200PortBridgeStatisticsTable_Object = MibTable
me1200PortBridgeStatisticsTable = _Me1200PortBridgeStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 3, 2, 5)
)
if mibBuilder.loadTexts:
    me1200PortBridgeStatisticsTable.setStatus("current")
_Me1200PortBridgeStatisticsEntry_Object = MibTableRow
me1200PortBridgeStatisticsEntry = _Me1200PortBridgeStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 3, 2, 5, 1)
)
me1200PortBridgeStatisticsEntry.setIndexNames(
    (0, "ME1200-PORT-MIB", "me1200PortBridgeStatisticsIfIndex"),
)
if mibBuilder.loadTexts:
    me1200PortBridgeStatisticsEntry.setStatus("current")
_Me1200PortBridgeStatisticsIfIndex_Type = ME1200InterfaceIndex
_Me1200PortBridgeStatisticsIfIndex_Object = MibTableColumn
me1200PortBridgeStatisticsIfIndex = _Me1200PortBridgeStatisticsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 3, 2, 5, 1, 1),
    _Me1200PortBridgeStatisticsIfIndex_Type()
)
me1200PortBridgeStatisticsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200PortBridgeStatisticsIfIndex.setStatus("current")
_Me1200PortBridgeStatisticsRxBridgeDiscard_Type = Counter64
_Me1200PortBridgeStatisticsRxBridgeDiscard_Object = MibTableColumn
me1200PortBridgeStatisticsRxBridgeDiscard = _Me1200PortBridgeStatisticsRxBridgeDiscard_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 3, 2, 5, 1, 2),
    _Me1200PortBridgeStatisticsRxBridgeDiscard_Type()
)
me1200PortBridgeStatisticsRxBridgeDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PortBridgeStatisticsRxBridgeDiscard.setStatus("current")
_Me1200PortVeriPhyResult_ObjectIdentity = ObjectIdentity
me1200PortVeriPhyResult = _Me1200PortVeriPhyResult_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 3, 3)
)
_Me1200PortVeriPhyResultTable_Object = MibTable
me1200PortVeriPhyResultTable = _Me1200PortVeriPhyResultTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 3, 3, 1)
)
if mibBuilder.loadTexts:
    me1200PortVeriPhyResultTable.setStatus("current")
_Me1200PortVeriPhyResultEntry_Object = MibTableRow
me1200PortVeriPhyResultEntry = _Me1200PortVeriPhyResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 3, 3, 1, 1)
)
me1200PortVeriPhyResultEntry.setIndexNames(
    (0, "ME1200-PORT-MIB", "me1200PortVeriPhyResultIfIndex"),
)
if mibBuilder.loadTexts:
    me1200PortVeriPhyResultEntry.setStatus("current")
_Me1200PortVeriPhyResultIfIndex_Type = ME1200InterfaceIndex
_Me1200PortVeriPhyResultIfIndex_Object = MibTableColumn
me1200PortVeriPhyResultIfIndex = _Me1200PortVeriPhyResultIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 3, 3, 1, 1, 1),
    _Me1200PortVeriPhyResultIfIndex_Type()
)
me1200PortVeriPhyResultIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200PortVeriPhyResultIfIndex.setStatus("current")
_Me1200PortVeriPhyResultVeriPhyStatusPairA_Type = ME1200PortPhyVeriPhyStatus
_Me1200PortVeriPhyResultVeriPhyStatusPairA_Object = MibTableColumn
me1200PortVeriPhyResultVeriPhyStatusPairA = _Me1200PortVeriPhyResultVeriPhyStatusPairA_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 3, 3, 1, 1, 2),
    _Me1200PortVeriPhyResultVeriPhyStatusPairA_Type()
)
me1200PortVeriPhyResultVeriPhyStatusPairA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PortVeriPhyResultVeriPhyStatusPairA.setStatus("current")
_Me1200PortVeriPhyResultVeriPhyStatusPairB_Type = ME1200PortPhyVeriPhyStatus
_Me1200PortVeriPhyResultVeriPhyStatusPairB_Object = MibTableColumn
me1200PortVeriPhyResultVeriPhyStatusPairB = _Me1200PortVeriPhyResultVeriPhyStatusPairB_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 3, 3, 1, 1, 3),
    _Me1200PortVeriPhyResultVeriPhyStatusPairB_Type()
)
me1200PortVeriPhyResultVeriPhyStatusPairB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PortVeriPhyResultVeriPhyStatusPairB.setStatus("current")
_Me1200PortVeriPhyResultVeriPhyStatusPairC_Type = ME1200PortPhyVeriPhyStatus
_Me1200PortVeriPhyResultVeriPhyStatusPairC_Object = MibTableColumn
me1200PortVeriPhyResultVeriPhyStatusPairC = _Me1200PortVeriPhyResultVeriPhyStatusPairC_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 3, 3, 1, 1, 4),
    _Me1200PortVeriPhyResultVeriPhyStatusPairC_Type()
)
me1200PortVeriPhyResultVeriPhyStatusPairC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PortVeriPhyResultVeriPhyStatusPairC.setStatus("current")
_Me1200PortVeriPhyResultVeriPhyStatusPairD_Type = ME1200PortPhyVeriPhyStatus
_Me1200PortVeriPhyResultVeriPhyStatusPairD_Object = MibTableColumn
me1200PortVeriPhyResultVeriPhyStatusPairD = _Me1200PortVeriPhyResultVeriPhyStatusPairD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 3, 3, 1, 1, 5),
    _Me1200PortVeriPhyResultVeriPhyStatusPairD_Type()
)
me1200PortVeriPhyResultVeriPhyStatusPairD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PortVeriPhyResultVeriPhyStatusPairD.setStatus("current")
_Me1200PortVeriPhyResultVeriPhyLengthStatusPairA_Type = ME1200Unsigned8
_Me1200PortVeriPhyResultVeriPhyLengthStatusPairA_Object = MibTableColumn
me1200PortVeriPhyResultVeriPhyLengthStatusPairA = _Me1200PortVeriPhyResultVeriPhyLengthStatusPairA_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 3, 3, 1, 1, 6),
    _Me1200PortVeriPhyResultVeriPhyLengthStatusPairA_Type()
)
me1200PortVeriPhyResultVeriPhyLengthStatusPairA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PortVeriPhyResultVeriPhyLengthStatusPairA.setStatus("current")
_Me1200PortVeriPhyResultVeriPhyLengthStatusPairB_Type = ME1200Unsigned8
_Me1200PortVeriPhyResultVeriPhyLengthStatusPairB_Object = MibTableColumn
me1200PortVeriPhyResultVeriPhyLengthStatusPairB = _Me1200PortVeriPhyResultVeriPhyLengthStatusPairB_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 3, 3, 1, 1, 7),
    _Me1200PortVeriPhyResultVeriPhyLengthStatusPairB_Type()
)
me1200PortVeriPhyResultVeriPhyLengthStatusPairB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PortVeriPhyResultVeriPhyLengthStatusPairB.setStatus("current")
_Me1200PortVeriPhyResultVeriPhyLengthStatusPairC_Type = ME1200Unsigned8
_Me1200PortVeriPhyResultVeriPhyLengthStatusPairC_Object = MibTableColumn
me1200PortVeriPhyResultVeriPhyLengthStatusPairC = _Me1200PortVeriPhyResultVeriPhyLengthStatusPairC_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 3, 3, 1, 1, 8),
    _Me1200PortVeriPhyResultVeriPhyLengthStatusPairC_Type()
)
me1200PortVeriPhyResultVeriPhyLengthStatusPairC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PortVeriPhyResultVeriPhyLengthStatusPairC.setStatus("current")
_Me1200PortVeriPhyResultVeriPhyLengthStatusPairD_Type = ME1200Unsigned8
_Me1200PortVeriPhyResultVeriPhyLengthStatusPairD_Object = MibTableColumn
me1200PortVeriPhyResultVeriPhyLengthStatusPairD = _Me1200PortVeriPhyResultVeriPhyLengthStatusPairD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 3, 3, 1, 1, 9),
    _Me1200PortVeriPhyResultVeriPhyLengthStatusPairD_Type()
)
me1200PortVeriPhyResultVeriPhyLengthStatusPairD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PortVeriPhyResultVeriPhyLengthStatusPairD.setStatus("current")
_Me1200PortControl_ObjectIdentity = ObjectIdentity
me1200PortControl = _Me1200PortControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 4)
)
_Me1200PortStatisticsClear_ObjectIdentity = ObjectIdentity
me1200PortStatisticsClear = _Me1200PortStatisticsClear_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 4, 1)
)
_Me1200PortStatsClearTable_Object = MibTable
me1200PortStatsClearTable = _Me1200PortStatsClearTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    me1200PortStatsClearTable.setStatus("current")
_Me1200PortStatsClearEntry_Object = MibTableRow
me1200PortStatsClearEntry = _Me1200PortStatsClearEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 4, 1, 1, 1)
)
me1200PortStatsClearEntry.setIndexNames(
    (0, "ME1200-PORT-MIB", "me1200PortStatsClearIfIndex"),
)
if mibBuilder.loadTexts:
    me1200PortStatsClearEntry.setStatus("current")
_Me1200PortStatsClearIfIndex_Type = ME1200InterfaceIndex
_Me1200PortStatsClearIfIndex_Object = MibTableColumn
me1200PortStatsClearIfIndex = _Me1200PortStatsClearIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 4, 1, 1, 1, 1),
    _Me1200PortStatsClearIfIndex_Type()
)
me1200PortStatsClearIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200PortStatsClearIfIndex.setStatus("current")
_Me1200PortStatsClearStatisticsClear_Type = TruthValue
_Me1200PortStatsClearStatisticsClear_Object = MibTableColumn
me1200PortStatsClearStatisticsClear = _Me1200PortStatsClearStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 4, 1, 1, 1, 2),
    _Me1200PortStatsClearStatisticsClear_Type()
)
me1200PortStatsClearStatisticsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PortStatsClearStatisticsClear.setStatus("current")
_Me1200PortVeriPhyStart_ObjectIdentity = ObjectIdentity
me1200PortVeriPhyStart = _Me1200PortVeriPhyStart_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 4, 2)
)
_Me1200PortVeriPhyStartTable_Object = MibTable
me1200PortVeriPhyStartTable = _Me1200PortVeriPhyStartTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 4, 2, 1)
)
if mibBuilder.loadTexts:
    me1200PortVeriPhyStartTable.setStatus("current")
_Me1200PortVeriPhyStartEntry_Object = MibTableRow
me1200PortVeriPhyStartEntry = _Me1200PortVeriPhyStartEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 4, 2, 1, 1)
)
me1200PortVeriPhyStartEntry.setIndexNames(
    (0, "ME1200-PORT-MIB", "me1200PortVeriPhyStartIfIndex"),
)
if mibBuilder.loadTexts:
    me1200PortVeriPhyStartEntry.setStatus("current")
_Me1200PortVeriPhyStartIfIndex_Type = ME1200InterfaceIndex
_Me1200PortVeriPhyStartIfIndex_Object = MibTableColumn
me1200PortVeriPhyStartIfIndex = _Me1200PortVeriPhyStartIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 4, 2, 1, 1, 1),
    _Me1200PortVeriPhyStartIfIndex_Type()
)
me1200PortVeriPhyStartIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200PortVeriPhyStartIfIndex.setStatus("current")
_Me1200PortVeriPhyStartStart_Type = TruthValue
_Me1200PortVeriPhyStartStart_Object = MibTableColumn
me1200PortVeriPhyStartStart = _Me1200PortVeriPhyStartStart_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 4, 2, 1, 1, 2),
    _Me1200PortVeriPhyStartStart_Type()
)
me1200PortVeriPhyStartStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PortVeriPhyStartStart.setStatus("current")
_Me1200PortNotificationPrefix_ObjectIdentity = ObjectIdentity
me1200PortNotificationPrefix = _Me1200PortNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 5)
)
_Me1200PortNotification_ObjectIdentity = ObjectIdentity
me1200PortNotification = _Me1200PortNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 5, 0)
)
_Me1200PortMibConformance_ObjectIdentity = ObjectIdentity
me1200PortMibConformance = _Me1200PortMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 3)
)
_Me1200PortMibCompliances_ObjectIdentity = ObjectIdentity
me1200PortMibCompliances = _Me1200PortMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 3, 1)
)
_Me1200PortMibGroups_ObjectIdentity = ObjectIdentity
me1200PortMibGroups = _Me1200PortMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 3, 2)
)

# Managed Objects groups

me1200PortConfigInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 3, 2, 1)
)
me1200PortConfigInfoGroup.setObjects(
      *(("ME1200-PORT-MIB", "me1200PortConfigShutdown"),
        ("ME1200-PORT-MIB", "me1200PortConfigSpeed"),
        ("ME1200-PORT-MIB", "me1200PortConfigMediaType"),
        ("ME1200-PORT-MIB", "me1200PortConfigDuplex"),
        ("ME1200-PORT-MIB", "me1200PortConfigFC"),
        ("ME1200-PORT-MIB", "me1200PortConfigMTU"),
        ("ME1200-PORT-MIB", "me1200PortConfigExcessiveRestart"))
)
if mibBuilder.loadTexts:
    me1200PortConfigInfoGroup.setStatus("current")

me1200PortInformationTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 3, 2, 2)
)
me1200PortInformationTableInfoGroup.setObjects(
      *(("ME1200-PORT-MIB", "me1200PortInformationLink"),
        ("ME1200-PORT-MIB", "me1200PortInformationFdx"),
        ("ME1200-PORT-MIB", "me1200PortInformationFiber"),
        ("ME1200-PORT-MIB", "me1200PortInformationSpeed"),
        ("ME1200-PORT-MIB", "me1200PortInformationSFPType"),
        ("ME1200-PORT-MIB", "me1200PortInformationSFPVendorName"),
        ("ME1200-PORT-MIB", "me1200PortInformationSFPVendorPN"),
        ("ME1200-PORT-MIB", "me1200PortInformationSFPVendorRev"))
)
if mibBuilder.loadTexts:
    me1200PortInformationTableInfoGroup.setStatus("current")

me1200PortRmonStatisticsTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 3, 2, 3)
)
me1200PortRmonStatisticsTableInfoGroup.setObjects(
      *(("ME1200-PORT-MIB", "me1200PortRmonStatisticsRxDropEvents"),
        ("ME1200-PORT-MIB", "me1200PortRmonStatisticsRxOctects"),
        ("ME1200-PORT-MIB", "me1200PortRmonStatisticsRxPkts"),
        ("ME1200-PORT-MIB", "me1200PortRmonStatisticsRxBroadcastPkts"),
        ("ME1200-PORT-MIB", "me1200PortRmonStatisticsRxMulticastPkts"),
        ("ME1200-PORT-MIB", "me1200PortRmonStatisticsRxCrcAlignErrPkts"),
        ("ME1200-PORT-MIB", "me1200PortRmonStatisticsRxUndersizePkts"),
        ("ME1200-PORT-MIB", "me1200PortRmonStatisticsRxOverizePkts"),
        ("ME1200-PORT-MIB", "me1200PortRmonStatisticsRxFragmentsPkts"),
        ("ME1200-PORT-MIB", "me1200PortRmonStatisticsRxJabbersPkts"),
        ("ME1200-PORT-MIB", "me1200PortRmonStatisticsRx64Pkts"),
        ("ME1200-PORT-MIB", "me1200PortRmonStatisticsRx65to127Pkts"),
        ("ME1200-PORT-MIB", "me1200PortRmonStatisticsRx128to255Pkts"),
        ("ME1200-PORT-MIB", "me1200PortRmonStatisticsRx256to511Pkts"),
        ("ME1200-PORT-MIB", "me1200PortRmonStatisticsRx512to1023Pkts"),
        ("ME1200-PORT-MIB", "me1200PortRmonStatisticsRx1024to1518Pkts"),
        ("ME1200-PORT-MIB", "me1200PortRmonStatisticsRx1519PktsToMax"),
        ("ME1200-PORT-MIB", "me1200PortRmonStatisticsTxDropEvents"),
        ("ME1200-PORT-MIB", "me1200PortRmonStatisticsTxOctects"),
        ("ME1200-PORT-MIB", "me1200PortRmonStatisticsTxPkts"),
        ("ME1200-PORT-MIB", "me1200PortRmonStatisticsTxBroadcastPkts"),
        ("ME1200-PORT-MIB", "me1200PortRmonStatisticsTxMulticastPkts"),
        ("ME1200-PORT-MIB", "me1200PortRmonStatisticsTx64Pkts"),
        ("ME1200-PORT-MIB", "me1200PortRmonStatisticsTx65to127Pkts"),
        ("ME1200-PORT-MIB", "me1200PortRmonStatisticsTx128to255Pkts"),
        ("ME1200-PORT-MIB", "me1200PortRmonStatisticsTx256to511Pkts"),
        ("ME1200-PORT-MIB", "me1200PortRmonStatisticsTx512to1023Pkts"),
        ("ME1200-PORT-MIB", "me1200PortRmonStatisticsTx1024to1518Pkts"),
        ("ME1200-PORT-MIB", "me1200PortRmonStatisticsTx1519PktsToMax"))
)
if mibBuilder.loadTexts:
    me1200PortRmonStatisticsTableInfoGroup.setStatus("current")

me1200PortIfGroupStatisticsTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 3, 2, 4)
)
me1200PortIfGroupStatisticsTableInfoGroup.setObjects(
      *(("ME1200-PORT-MIB", "me1200PortIfGroupStatisticsRxOctets"),
        ("ME1200-PORT-MIB", "me1200PortIfGroupStatisticsRxUnicastPkts"),
        ("ME1200-PORT-MIB", "me1200PortIfGroupStatisticsRxMulticastPkts"),
        ("ME1200-PORT-MIB", "me1200PortIfGroupStatisticsRxBroadcastPkts"),
        ("ME1200-PORT-MIB", "me1200PortIfGroupStatisticsRxNonUnicastPkts"),
        ("ME1200-PORT-MIB", "me1200PortIfGroupStatisticsRxDiscards"),
        ("ME1200-PORT-MIB", "me1200PortIfGroupStatisticsRxErrors"),
        ("ME1200-PORT-MIB", "me1200PortIfGroupStatisticsTxOctets"),
        ("ME1200-PORT-MIB", "me1200PortIfGroupStatisticsTxUnicastPkts"),
        ("ME1200-PORT-MIB", "me1200PortIfGroupStatisticsTxMulticastPkts"),
        ("ME1200-PORT-MIB", "me1200PortIfGroupStatisticsTxBroadcastPkts"),
        ("ME1200-PORT-MIB", "me1200PortIfGroupStatisticsTxNonUnicastPkts"),
        ("ME1200-PORT-MIB", "me1200PortIfGroupStatisticsTxDiscardPkts"),
        ("ME1200-PORT-MIB", "me1200PortIfGroupStatisticsTxErrorPkts"))
)
if mibBuilder.loadTexts:
    me1200PortIfGroupStatisticsTableInfoGroup.setStatus("current")

me1200PortEthernetLikeStatisticsTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 3, 2, 5)
)
me1200PortEthernetLikeStatisticsTableInfoGroup.setObjects(
      *(("ME1200-PORT-MIB", "me1200PortEthernetLikeStatisticsRxPauseFrames"),
        ("ME1200-PORT-MIB", "me1200PortEthernetLikeStatisticsTxPauseFrames"))
)
if mibBuilder.loadTexts:
    me1200PortEthernetLikeStatisticsTableInfoGroup.setStatus("current")

me1200PortQueuesStatisticsTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 3, 2, 6)
)
me1200PortQueuesStatisticsTableInfoGroup.setObjects(
      *(("ME1200-PORT-MIB", "me1200PortQueuesStatisticsRxPrio"),
        ("ME1200-PORT-MIB", "me1200PortQueuesStatisticsTxPrio"))
)
if mibBuilder.loadTexts:
    me1200PortQueuesStatisticsTableInfoGroup.setStatus("current")

me1200PortBridgeStatisticsTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 3, 2, 7)
)
me1200PortBridgeStatisticsTableInfoGroup.setObjects(
    ("ME1200-PORT-MIB", "me1200PortBridgeStatisticsRxBridgeDiscard")
)
if mibBuilder.loadTexts:
    me1200PortBridgeStatisticsTableInfoGroup.setStatus("current")

me1200PortVeriPhyResultTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 3, 2, 8)
)
me1200PortVeriPhyResultTableInfoGroup.setObjects(
      *(("ME1200-PORT-MIB", "me1200PortVeriPhyResultVeriPhyStatusPairA"),
        ("ME1200-PORT-MIB", "me1200PortVeriPhyResultVeriPhyStatusPairB"),
        ("ME1200-PORT-MIB", "me1200PortVeriPhyResultVeriPhyStatusPairC"),
        ("ME1200-PORT-MIB", "me1200PortVeriPhyResultVeriPhyStatusPairD"),
        ("ME1200-PORT-MIB", "me1200PortVeriPhyResultVeriPhyLengthStatusPairA"),
        ("ME1200-PORT-MIB", "me1200PortVeriPhyResultVeriPhyLengthStatusPairB"),
        ("ME1200-PORT-MIB", "me1200PortVeriPhyResultVeriPhyLengthStatusPairC"),
        ("ME1200-PORT-MIB", "me1200PortVeriPhyResultVeriPhyLengthStatusPairD"))
)
if mibBuilder.loadTexts:
    me1200PortVeriPhyResultTableInfoGroup.setStatus("current")

me1200PortStatsClearTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 3, 2, 9)
)
me1200PortStatsClearTableInfoGroup.setObjects(
    ("ME1200-PORT-MIB", "me1200PortStatsClearStatisticsClear")
)
if mibBuilder.loadTexts:
    me1200PortStatsClearTableInfoGroup.setStatus("current")

me1200PortVeriPhyStartTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 3, 2, 10)
)
me1200PortVeriPhyStartTableInfoGroup.setObjects(
    ("ME1200-PORT-MIB", "me1200PortVeriPhyStartStart")
)
if mibBuilder.loadTexts:
    me1200PortVeriPhyStartTableInfoGroup.setStatus("current")


# Notification objects

me1200PortNotificationEthAmdinSpeedIncompatible = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 5, 0, 1)
)
me1200PortNotificationEthAmdinSpeedIncompatible.setObjects(
      *(("ME1200-PORT-MIB", "me1200PortConfigSpeed"),
        ("ME1200-PORT-MIB", "me1200PortInformationSpeed"),
        ("ME1200-PORT-MIB", "me1200PortInformationSFPType"))
)
if mibBuilder.loadTexts:
    me1200PortNotificationEthAmdinSpeedIncompatible.setStatus(
        "current"
    )

me1200PortNotificationSFPSpeedInfoMissing = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 1, 5, 0, 2)
)
me1200PortNotificationSFPSpeedInfoMissing.setObjects(
    ("ME1200-PORT-MIB", "me1200PortInformationSFPType")
)
if mibBuilder.loadTexts:
    me1200PortNotificationSFPSpeedInfoMissing.setStatus(
        "current"
    )


# Notifications groups

me1200PortNotificationInfoGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 3, 2, 11)
)
me1200PortNotificationInfoGroup.setObjects(
      *(("ME1200-PORT-MIB", "me1200PortNotificationEthAmdinSpeedIncompatible"),
        ("ME1200-PORT-MIB", "me1200PortNotificationSFPSpeedInfoMissing"))
)
if mibBuilder.loadTexts:
    me1200PortNotificationInfoGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

me1200PortMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 11, 3, 1, 1)
)
me1200PortMibCompliance.setObjects(
      *(("ME1200-PORT-MIB", "me1200PortConfigInfoGroup"),
        ("ME1200-PORT-MIB", "me1200PortInformationTableInfoGroup"),
        ("ME1200-PORT-MIB", "me1200PortRmonStatisticsTableInfoGroup"),
        ("ME1200-PORT-MIB", "me1200PortIfGroupStatisticsTableInfoGroup"),
        ("ME1200-PORT-MIB", "me1200PortEthernetLikeStatisticsTableInfoGroup"),
        ("ME1200-PORT-MIB", "me1200PortQueuesStatisticsTableInfoGroup"),
        ("ME1200-PORT-MIB", "me1200PortBridgeStatisticsTableInfoGroup"),
        ("ME1200-PORT-MIB", "me1200PortVeriPhyResultTableInfoGroup"),
        ("ME1200-PORT-MIB", "me1200PortStatsClearTableInfoGroup"),
        ("ME1200-PORT-MIB", "me1200PortVeriPhyStartTableInfoGroup"),
        ("ME1200-PORT-MIB", "me1200PortNotificationInfoGroup"))
)
if mibBuilder.loadTexts:
    me1200PortMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ME1200-PORT-MIB",
    **{"ME1200PortDuplex": ME1200PortDuplex,
       "ME1200PortFc": ME1200PortFc,
       "ME1200PortMedia": ME1200PortMedia,
       "ME1200PortPhyVeriPhyStatus": ME1200PortPhyVeriPhyStatus,
       "ME1200PortSFPTransceiver": ME1200PortSFPTransceiver,
       "ME1200PortSpeed": ME1200PortSpeed,
       "ME1200PortStatusSpeed": ME1200PortStatusSpeed,
       "me1200PortMib": me1200PortMib,
       "me1200PortObjects": me1200PortObjects,
       "me1200PortConfig": me1200PortConfig,
       "me1200PortConfigTable": me1200PortConfigTable,
       "me1200PortConfigEntry": me1200PortConfigEntry,
       "me1200PortConfigIfIndex": me1200PortConfigIfIndex,
       "me1200PortConfigShutdown": me1200PortConfigShutdown,
       "me1200PortConfigSpeed": me1200PortConfigSpeed,
       "me1200PortConfigMediaType": me1200PortConfigMediaType,
       "me1200PortConfigDuplex": me1200PortConfigDuplex,
       "me1200PortConfigFC": me1200PortConfigFC,
       "me1200PortConfigMTU": me1200PortConfigMTU,
       "me1200PortConfigExcessiveRestart": me1200PortConfigExcessiveRestart,
       "me1200PortStatus": me1200PortStatus,
       "me1200PortInformationTable": me1200PortInformationTable,
       "me1200PortInformationEntry": me1200PortInformationEntry,
       "me1200PortInformationIfIndex": me1200PortInformationIfIndex,
       "me1200PortInformationLink": me1200PortInformationLink,
       "me1200PortInformationFdx": me1200PortInformationFdx,
       "me1200PortInformationFiber": me1200PortInformationFiber,
       "me1200PortInformationSpeed": me1200PortInformationSpeed,
       "me1200PortInformationSFPType": me1200PortInformationSFPType,
       "me1200PortInformationSFPVendorName": me1200PortInformationSFPVendorName,
       "me1200PortInformationSFPVendorPN": me1200PortInformationSFPVendorPN,
       "me1200PortInformationSFPVendorRev": me1200PortInformationSFPVendorRev,
       "me1200PortStatistics": me1200PortStatistics,
       "me1200PortRmonStatisticsTable": me1200PortRmonStatisticsTable,
       "me1200PortRmonStatisticsEntry": me1200PortRmonStatisticsEntry,
       "me1200PortRmonStatisticsIfIndex": me1200PortRmonStatisticsIfIndex,
       "me1200PortRmonStatisticsRxDropEvents": me1200PortRmonStatisticsRxDropEvents,
       "me1200PortRmonStatisticsRxOctects": me1200PortRmonStatisticsRxOctects,
       "me1200PortRmonStatisticsRxPkts": me1200PortRmonStatisticsRxPkts,
       "me1200PortRmonStatisticsRxBroadcastPkts": me1200PortRmonStatisticsRxBroadcastPkts,
       "me1200PortRmonStatisticsRxMulticastPkts": me1200PortRmonStatisticsRxMulticastPkts,
       "me1200PortRmonStatisticsRxCrcAlignErrPkts": me1200PortRmonStatisticsRxCrcAlignErrPkts,
       "me1200PortRmonStatisticsRxUndersizePkts": me1200PortRmonStatisticsRxUndersizePkts,
       "me1200PortRmonStatisticsRxOverizePkts": me1200PortRmonStatisticsRxOverizePkts,
       "me1200PortRmonStatisticsRxFragmentsPkts": me1200PortRmonStatisticsRxFragmentsPkts,
       "me1200PortRmonStatisticsRxJabbersPkts": me1200PortRmonStatisticsRxJabbersPkts,
       "me1200PortRmonStatisticsRx64Pkts": me1200PortRmonStatisticsRx64Pkts,
       "me1200PortRmonStatisticsRx65to127Pkts": me1200PortRmonStatisticsRx65to127Pkts,
       "me1200PortRmonStatisticsRx128to255Pkts": me1200PortRmonStatisticsRx128to255Pkts,
       "me1200PortRmonStatisticsRx256to511Pkts": me1200PortRmonStatisticsRx256to511Pkts,
       "me1200PortRmonStatisticsRx512to1023Pkts": me1200PortRmonStatisticsRx512to1023Pkts,
       "me1200PortRmonStatisticsRx1024to1518Pkts": me1200PortRmonStatisticsRx1024to1518Pkts,
       "me1200PortRmonStatisticsRx1519PktsToMax": me1200PortRmonStatisticsRx1519PktsToMax,
       "me1200PortRmonStatisticsTxDropEvents": me1200PortRmonStatisticsTxDropEvents,
       "me1200PortRmonStatisticsTxOctects": me1200PortRmonStatisticsTxOctects,
       "me1200PortRmonStatisticsTxPkts": me1200PortRmonStatisticsTxPkts,
       "me1200PortRmonStatisticsTxBroadcastPkts": me1200PortRmonStatisticsTxBroadcastPkts,
       "me1200PortRmonStatisticsTxMulticastPkts": me1200PortRmonStatisticsTxMulticastPkts,
       "me1200PortRmonStatisticsTx64Pkts": me1200PortRmonStatisticsTx64Pkts,
       "me1200PortRmonStatisticsTx65to127Pkts": me1200PortRmonStatisticsTx65to127Pkts,
       "me1200PortRmonStatisticsTx128to255Pkts": me1200PortRmonStatisticsTx128to255Pkts,
       "me1200PortRmonStatisticsTx256to511Pkts": me1200PortRmonStatisticsTx256to511Pkts,
       "me1200PortRmonStatisticsTx512to1023Pkts": me1200PortRmonStatisticsTx512to1023Pkts,
       "me1200PortRmonStatisticsTx1024to1518Pkts": me1200PortRmonStatisticsTx1024to1518Pkts,
       "me1200PortRmonStatisticsTx1519PktsToMax": me1200PortRmonStatisticsTx1519PktsToMax,
       "me1200PortIfGroupStatisticsTable": me1200PortIfGroupStatisticsTable,
       "me1200PortIfGroupStatisticsEntry": me1200PortIfGroupStatisticsEntry,
       "me1200PortIfGroupStatisticsIfIndex": me1200PortIfGroupStatisticsIfIndex,
       "me1200PortIfGroupStatisticsRxOctets": me1200PortIfGroupStatisticsRxOctets,
       "me1200PortIfGroupStatisticsRxUnicastPkts": me1200PortIfGroupStatisticsRxUnicastPkts,
       "me1200PortIfGroupStatisticsRxMulticastPkts": me1200PortIfGroupStatisticsRxMulticastPkts,
       "me1200PortIfGroupStatisticsRxBroadcastPkts": me1200PortIfGroupStatisticsRxBroadcastPkts,
       "me1200PortIfGroupStatisticsRxNonUnicastPkts": me1200PortIfGroupStatisticsRxNonUnicastPkts,
       "me1200PortIfGroupStatisticsRxDiscards": me1200PortIfGroupStatisticsRxDiscards,
       "me1200PortIfGroupStatisticsRxErrors": me1200PortIfGroupStatisticsRxErrors,
       "me1200PortIfGroupStatisticsTxOctets": me1200PortIfGroupStatisticsTxOctets,
       "me1200PortIfGroupStatisticsTxUnicastPkts": me1200PortIfGroupStatisticsTxUnicastPkts,
       "me1200PortIfGroupStatisticsTxMulticastPkts": me1200PortIfGroupStatisticsTxMulticastPkts,
       "me1200PortIfGroupStatisticsTxBroadcastPkts": me1200PortIfGroupStatisticsTxBroadcastPkts,
       "me1200PortIfGroupStatisticsTxNonUnicastPkts": me1200PortIfGroupStatisticsTxNonUnicastPkts,
       "me1200PortIfGroupStatisticsTxDiscardPkts": me1200PortIfGroupStatisticsTxDiscardPkts,
       "me1200PortIfGroupStatisticsTxErrorPkts": me1200PortIfGroupStatisticsTxErrorPkts,
       "me1200PortEthernetLikeStatisticsTable": me1200PortEthernetLikeStatisticsTable,
       "me1200PortEthernetLikeStatisticsEntry": me1200PortEthernetLikeStatisticsEntry,
       "me1200PortEthernetLikeStatisticsIfIndex": me1200PortEthernetLikeStatisticsIfIndex,
       "me1200PortEthernetLikeStatisticsRxPauseFrames": me1200PortEthernetLikeStatisticsRxPauseFrames,
       "me1200PortEthernetLikeStatisticsTxPauseFrames": me1200PortEthernetLikeStatisticsTxPauseFrames,
       "me1200PortQueuesStatisticsTable": me1200PortQueuesStatisticsTable,
       "me1200PortQueuesStatisticsEntry": me1200PortQueuesStatisticsEntry,
       "me1200PortQueuesStatisticsIfIndex": me1200PortQueuesStatisticsIfIndex,
       "me1200PortQueuesStatisticsQueue": me1200PortQueuesStatisticsQueue,
       "me1200PortQueuesStatisticsRxPrio": me1200PortQueuesStatisticsRxPrio,
       "me1200PortQueuesStatisticsTxPrio": me1200PortQueuesStatisticsTxPrio,
       "me1200PortBridgeStatisticsTable": me1200PortBridgeStatisticsTable,
       "me1200PortBridgeStatisticsEntry": me1200PortBridgeStatisticsEntry,
       "me1200PortBridgeStatisticsIfIndex": me1200PortBridgeStatisticsIfIndex,
       "me1200PortBridgeStatisticsRxBridgeDiscard": me1200PortBridgeStatisticsRxBridgeDiscard,
       "me1200PortVeriPhyResult": me1200PortVeriPhyResult,
       "me1200PortVeriPhyResultTable": me1200PortVeriPhyResultTable,
       "me1200PortVeriPhyResultEntry": me1200PortVeriPhyResultEntry,
       "me1200PortVeriPhyResultIfIndex": me1200PortVeriPhyResultIfIndex,
       "me1200PortVeriPhyResultVeriPhyStatusPairA": me1200PortVeriPhyResultVeriPhyStatusPairA,
       "me1200PortVeriPhyResultVeriPhyStatusPairB": me1200PortVeriPhyResultVeriPhyStatusPairB,
       "me1200PortVeriPhyResultVeriPhyStatusPairC": me1200PortVeriPhyResultVeriPhyStatusPairC,
       "me1200PortVeriPhyResultVeriPhyStatusPairD": me1200PortVeriPhyResultVeriPhyStatusPairD,
       "me1200PortVeriPhyResultVeriPhyLengthStatusPairA": me1200PortVeriPhyResultVeriPhyLengthStatusPairA,
       "me1200PortVeriPhyResultVeriPhyLengthStatusPairB": me1200PortVeriPhyResultVeriPhyLengthStatusPairB,
       "me1200PortVeriPhyResultVeriPhyLengthStatusPairC": me1200PortVeriPhyResultVeriPhyLengthStatusPairC,
       "me1200PortVeriPhyResultVeriPhyLengthStatusPairD": me1200PortVeriPhyResultVeriPhyLengthStatusPairD,
       "me1200PortControl": me1200PortControl,
       "me1200PortStatisticsClear": me1200PortStatisticsClear,
       "me1200PortStatsClearTable": me1200PortStatsClearTable,
       "me1200PortStatsClearEntry": me1200PortStatsClearEntry,
       "me1200PortStatsClearIfIndex": me1200PortStatsClearIfIndex,
       "me1200PortStatsClearStatisticsClear": me1200PortStatsClearStatisticsClear,
       "me1200PortVeriPhyStart": me1200PortVeriPhyStart,
       "me1200PortVeriPhyStartTable": me1200PortVeriPhyStartTable,
       "me1200PortVeriPhyStartEntry": me1200PortVeriPhyStartEntry,
       "me1200PortVeriPhyStartIfIndex": me1200PortVeriPhyStartIfIndex,
       "me1200PortVeriPhyStartStart": me1200PortVeriPhyStartStart,
       "me1200PortNotificationPrefix": me1200PortNotificationPrefix,
       "me1200PortNotification": me1200PortNotification,
       "me1200PortNotificationEthAmdinSpeedIncompatible": me1200PortNotificationEthAmdinSpeedIncompatible,
       "me1200PortNotificationSFPSpeedInfoMissing": me1200PortNotificationSFPSpeedInfoMissing,
       "me1200PortMibConformance": me1200PortMibConformance,
       "me1200PortMibCompliances": me1200PortMibCompliances,
       "me1200PortMibCompliance": me1200PortMibCompliance,
       "me1200PortMibGroups": me1200PortMibGroups,
       "me1200PortConfigInfoGroup": me1200PortConfigInfoGroup,
       "me1200PortInformationTableInfoGroup": me1200PortInformationTableInfoGroup,
       "me1200PortRmonStatisticsTableInfoGroup": me1200PortRmonStatisticsTableInfoGroup,
       "me1200PortIfGroupStatisticsTableInfoGroup": me1200PortIfGroupStatisticsTableInfoGroup,
       "me1200PortEthernetLikeStatisticsTableInfoGroup": me1200PortEthernetLikeStatisticsTableInfoGroup,
       "me1200PortQueuesStatisticsTableInfoGroup": me1200PortQueuesStatisticsTableInfoGroup,
       "me1200PortBridgeStatisticsTableInfoGroup": me1200PortBridgeStatisticsTableInfoGroup,
       "me1200PortVeriPhyResultTableInfoGroup": me1200PortVeriPhyResultTableInfoGroup,
       "me1200PortStatsClearTableInfoGroup": me1200PortStatsClearTableInfoGroup,
       "me1200PortVeriPhyStartTableInfoGroup": me1200PortVeriPhyStartTableInfoGroup,
       "me1200PortNotificationInfoGroup": me1200PortNotificationInfoGroup}
)
